#!/usr/bin/env python3
"""Snapshot source TaxID lineages for AST overlap audits, not phenotype inference."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from ncbi_ast_inventory import activity_report_sha256
from ncbi_ast_isolates import require_iso_date

ENDPOINT = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
SOURCE = "NCBI_TAXONOMY_EFETCH"
SCOPE_TAXID = "77643"
SCOPE_NAME = "Mycobacterium tuberculosis complex"
SCOPE_REFERENCE = "https://zenodo.org/records/15680920"


def requested_taxids(rows: list[dict]) -> list[str]:
    taxids = {SCOPE_TAXID}
    for row in rows:
        value = row["taxon_id"]
        if value:
            if not re.fullmatch(r"NCBITaxon:[1-9][0-9]*", value):
                raise ValueError(f"invalid AST taxon_id: {value!r}")
            taxids.add(value.split(":", 1)[1])
    return sorted(taxids, key=int)


def _text(node: ET.Element, tag: str) -> str:
    elements = node.findall(tag)
    if len(elements) != 1 or not elements[0].text or not elements[0].text.strip():
        raise ValueError(f"taxonomy XML requires one nonempty {tag}")
    return elements[0].text.strip()


def _taxid(node: ET.Element, tag: str = "TaxId") -> str:
    value = _text(node, tag)
    if not re.fullmatch(r"[1-9][0-9]*", value):
        raise ValueError(f"invalid taxonomy XML {tag}: {value!r}")
    return value


def parse_taxonomy(payload: bytes, requested: list[str]) -> dict[str, dict]:
    root = ET.fromstring(payload)
    if root.tag != "TaxaSet" or any(node.tag != "Taxon" for node in root):
        raise ValueError("taxonomy response is not a successful TaxaSet")
    records, prefixes = {}, {}
    for node in root:
        taxid = _taxid(node)
        if taxid in records:
            raise ValueError(f"duplicate taxonomy record: {taxid}")
        name, parent = _text(node, "ScientificName"), _taxid(node, "ParentTaxId")
        lineage_nodes = node.findall("LineageEx")
        if len(lineage_nodes) != 1 or any(child.tag != "Taxon" for child in lineage_nodes[0]):
            raise ValueError(f"missing or invalid lineage: {taxid}")
        ancestors = lineage_nodes[0].findall("Taxon")
        lineage = [_taxid(ancestor) for ancestor in ancestors]
        names = [_text(ancestor, "ScientificName") for ancestor in ancestors]
        if (not lineage or lineage[-1] != parent or taxid in lineage
                or len(set(lineage)) != len(lineage)
                or _text(node, "Lineage") != "; ".join(names)):
            raise ValueError(f"incomplete or contradictory lineage: {taxid}")
        path = [*lineage, taxid]
        # Shared ancestors must have the same path in every returned lineage.
        for end, ancestor in enumerate(path, start=1):
            prefix = (path[:end], [*names, name][:end])
            if ancestor in prefixes and prefixes[ancestor] != prefix:
                raise ValueError(f"inconsistent lineage for ancestor: {ancestor}")
            prefixes[ancestor] = prefix
        records[taxid] = {"taxid": taxid, "scientific_name": name, "lineage_taxids": lineage}
    if set(records) != set(requested) or len(requested) != len(set(requested)):
        raise ValueError("taxonomy response does not cover exact requested TaxIDs; review missing/merged IDs")
    return records


def fetch_snapshot(activity_report: Path, output_dir: Path) -> dict:
    from seed_from_sources import load_ncbi_ast_activity_inventory

    if output_dir.exists():
        raise ValueError(f"snapshot directory already exists: {output_dir}")
    checksum = activity_report_sha256(activity_report)
    rows = load_ncbi_ast_activity_inventory(activity_report)
    if not rows:
        raise ValueError("taxonomy snapshot requires a nonempty activity report")
    requested = requested_taxids(rows)
    params = {"db": "taxonomy", "id": ",".join(requested), "retmode": "xml"}
    started = datetime.now(timezone.utc)
    # EFetch recommends POST for ID lists over 200; one request avoids batch drift.
    request = Request(ENDPOINT, data=urlencode(params).encode("ascii"))
    with urlopen(request, timeout=300) as response:
        payload = response.read()
    parse_taxonomy(payload, requested)
    if activity_report_sha256(activity_report) != checksum:
        raise ValueError("activity report changed during taxonomy retrieval")
    metadata = {
        "source": SOURCE, "source_retrieved_on": started.date().isoformat(),
        "started_at": started.isoformat(), "completed_at": datetime.now(timezone.utc).isoformat(),
        "endpoint": ENDPOINT, "file": "taxonomy.xml", "requested_taxids": requested,
        "activity_report_sha256": checksum, "sha256": hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
    }
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".ncbi-taxonomy-", dir=output_dir.parent) as temporary:
        staged = Path(temporary) / "snapshot"
        staged.mkdir()
        (staged / "taxonomy.xml").write_bytes(payload)
        (staged / "snapshot.json").write_text(json.dumps(metadata, indent=2) + "\n")
        load_snapshot(staged, activity_report, rows)
        if output_dir.exists():
            raise ValueError(f"snapshot directory already exists: {output_dir}")
        staged.rename(output_dir)
    return metadata


def load_snapshot(directory: Path, activity_report: Path, rows: list[dict]) -> dict[str, dict]:
    metadata = json.loads((directory / "snapshot.json").read_text())
    if (not isinstance(metadata, dict) or metadata.get("source") != SOURCE
            or metadata.get("file") != "taxonomy.xml" or metadata.get("endpoint") != ENDPOINT):
        raise ValueError("not an NCBI taxonomy snapshot")
    require_iso_date(metadata.get("source_retrieved_on"), "taxonomy snapshot")
    if metadata.get("activity_report_sha256") != activity_report_sha256(activity_report):
        raise ValueError("taxonomy snapshot activity report checksum mismatch")
    requested = requested_taxids(rows)
    if metadata.get("requested_taxids") != requested:
        raise ValueError("taxonomy snapshot requested TaxIDs differ from report")
    payload = (directory / "taxonomy.xml").read_bytes()
    if (metadata.get("sha256") != hashlib.sha256(payload).hexdigest()
            or metadata.get("bytes") != len(payload)):
        raise ValueError("taxonomy snapshot checksum/size mismatch")
    return parse_taxonomy(payload, requested)


def relationship(taxid: str, records: dict[str, dict]) -> str:
    scope, candidate = records.get(SCOPE_TAXID), records.get(taxid)
    if not scope or scope["scientific_name"] != SCOPE_NAME:
        raise ValueError("taxonomy snapshot does not establish the CRyPTIC complex identity")
    if not candidate:
        return "UNRESOLVED"
    scope_path = [*scope["lineage_taxids"], SCOPE_TAXID]
    candidate_path = [*candidate["lineage_taxids"], taxid]
    # A truncated lineage or a non-bacterial identifier cannot establish disjointness.
    if any(path[:2] != ["131567", "2"] for path in (scope_path, candidate_path)):
        return "UNRESOLVED"
    if SCOPE_TAXID in candidate_path:
        return "WITHIN_SCOPE"
    if taxid in scope_path:
        return "ANCESTOR_OF_SCOPE"
    return "OUTSIDE_SCOPE"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--activity-report", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    metadata = fetch_snapshot(args.activity_report, args.output_directory)
    print(f"Taxonomy snapshot: {args.output_directory}; {len(metadata['requested_taxids'])} TaxIDs")


if __name__ == "__main__":
    main()
