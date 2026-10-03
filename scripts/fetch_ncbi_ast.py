#!/usr/bin/env python3
"""Snapshot the public NCBI AST Browser export for offline evaluation."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

ENDPOINT = "https://www.ncbi.nlm.nih.gov/pathogens/pathogens-srv/"
FIELDS = [
    ("id", "AST row ID"),
    ("biosample_acc", "BioSample"),
    ("taxgroup_name", "Organism group"),
    ("scientific_name", "Scientific name"),
    ("epi_type", "Isolation type"),
    ("geo_loc_name", "Location"),
    ("isolation_source", "Isolation source"),
    ("target_acc", "Isolate"),
    ("antibiotic", "Antibiotic"),
    ("phenotype", "Resistance phenotype"),
    ("measurement_sign", "Measurement sign"),
    ("mic", "MIC (mg/L)"),
    ("disk_diffusion", "Disk diffusion (mm)"),
    ("platform", "Laboratory typing platform"),
    ("vendor", "Vendor"),
    ("reagent", "Laboratory typing method version or reagent"),
    ("standard", "Testing standard"),
    ("host", "Host"),
    ("collection_date", "Collection date"),
    ("target_creation_date", "Create date"),
    ("bioproject_acc", "BioProject"),
]
EXPORT_HEADER = [label for _, label in FIELDS]
EXPORT_HEADER[0] = "#" + EXPORT_HEADER[0]


def source_count(query: str) -> int:
    params = dict(action="retrieve", collection="ast", fq=query, fl="id", limit=1)
    with urlopen(ENDPOINT + "?" + urlencode(params), timeout=60) as response:
        payload = json.load(response)
    if payload.get("success") is not True:
        raise ValueError(f"NCBI AST count request failed: {payload.get('error')}")
    count = payload["ngout"]["data"]["totalCount"]
    if type(count) is not int or count <= 0:
        raise ValueError(f"NCBI AST query returned no positive row count: {count!r}")
    return count


def export_url(query: str) -> str:
    # This is the request constructed by the AST Browser's Download action.
    expression = f"[display()].from(ast).usingschema(/schema/pathogen).matching(q=={json.dumps(query)})"
    return ENDPOINT + "?" + urlencode({
        "action": "solr2txt", "browser": "ast", "q": expression,
        "fields": ",".join(f"{field}|{label}" for field, label in FIELDS),
        "type": "tsv", "filename": "asts.tsv", "nolimit": "on",
    })


def inspect_export(path: Path) -> int:
    seen = set()
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != EXPORT_HEADER:
            raise ValueError("NCBI AST export header differs from requested columns")
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"NCBI AST export has a ragged row at line {reader.line_num}")
            row_id = row[EXPORT_HEADER[0]]
            if not row_id or row_id in seen:
                raise ValueError(f"NCBI AST export has a missing or duplicate row ID: {row_id!r}")
            seen.add(row_id)
    if not seen:
        raise ValueError("NCBI AST export contains no observations")
    return len(seen)


def fetch_snapshot(output_dir: Path, query: str) -> dict:
    """Publish a new directory only after the export and count checks pass."""
    if output_dir.exists():
        raise ValueError(f"snapshot directory already exists: {output_dir}")
    if not query.strip():
        raise ValueError("query must not be empty")
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc).isoformat()
    before = source_count(query)
    url = export_url(query)
    with tempfile.TemporaryDirectory(prefix=".ncbi-ast-", dir=output_dir.parent) as temporary:
        staged = Path(temporary) / "snapshot"
        staged.mkdir()
        export = staged / "ast.tsv"
        with urlopen(url, timeout=300) as response, export.open("wb") as handle:
            shutil.copyfileobj(response, handle)
        row_count = inspect_export(export)
        after = source_count(query)
        if row_count != before or row_count != after:
            raise ValueError(
                f"NCBI AST row count changed or export is incomplete: "
                f"before={before}, exported={row_count}, after={after}"
            )
        digest = hashlib.sha256()
        with export.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        checksum = digest.hexdigest()
        metadata = {
            "source": "NCBI_AST",
            "source_version": "ast-browser-sha256:" + checksum,
            "source_retrieved_on": started[:10],
            "retrieval_started_at": started,
            "retrieval_finished_at": datetime.now(timezone.utc).isoformat(),
            "query": query,
            "export_url": url,
            "file": "ast.tsv",
            "sha256": checksum,
            "bytes": export.stat().st_size,
            "rows": row_count,
            "count_before": before,
            "count_after": after,
        }
        (staged / "snapshot.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        if output_dir.exists():
            raise ValueError(f"snapshot directory already exists: {output_dir}")
        staged.rename(output_dir)
    return metadata


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--query", default="*:*", help="AST Browser Solr query (default: all rows).")
    args = parser.parse_args()
    metadata = fetch_snapshot(args.output_dir, args.query)
    print(f"Downloaded {metadata['rows']} AST observations to {args.output_dir}")
    print(f"Source version: {metadata['source_version']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
