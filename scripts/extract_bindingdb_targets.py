#!/usr/bin/env python3
"""Extract provenance-complete BindingDB target measurements for this corpus.

Only rows carrying BindingDB's own literature-curation marker are eligible.
The ligand must match exactly by a reported and independently recomputed
Standard InChIKey, the article must have a PMID or DOI, the target organism must
resolve unambiguously below a microbial/viral NCBI Taxonomy root, and the
reaction set must resolve to a non-empty BindingDB assay description.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path

import yaml
from evaluate_bindingdb_targets import (
    CURATED_MARKER,
    archive_member,
    classify_candidates,
    collect_candidates,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
INVENTORY_NAME = "bindingdb_target_measurements.tsv"
SOURCE_VERSION = "2026-09"
SOURCE_RETRIEVED_ON = "2026-08-31"
VALUE_RE = re.compile(
    r"^\s*(?P<qualifier><=|>=|<|>|=|~|≈)?\s*"
    r"(?P<value>(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?)\s*$"
)
QUALIFIERS = {
    "<": "LT",
    "<=": "LE",
    "": "EQ",
    "=": "EQ",
    ">=": "GE",
    ">": "GT",
    "~": "APPROX",
    "≈": "APPROX",
}
UNIPROT_ACCESSION_RE = re.compile(r"^[A-Z0-9]+(?:-[0-9]+)?$")


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_measurement(raw: str) -> tuple[str, float] | None:
    """Return the closed qualifier and numeric value without changing raw text."""
    match = VALUE_RE.fullmatch(raw)
    if not match:
        return None
    return QUALIFIERS[match.group("qualifier") or ""], float(match.group("value"))


def read_reactant_assays(path: Path) -> dict[str, set[str]]:
    mapping: dict[str, set[str]] = {}
    csv.field_size_limit(sys.maxsize)
    with zipfile.ZipFile(path) as archive, archive.open(archive_member(path)) as binary:
        text = (line.decode("utf-8", errors="replace") for line in binary)
        for row in csv.DictReader(text, delimiter="\t"):
            reactant_set_id = row["REACTANT_SET_ID"].strip()
            entry_assay_id = row["ENTRYID_ASSAYID"].strip()
            if reactant_set_id and entry_assay_id:
                mapping.setdefault(reactant_set_id, set()).add(entry_assay_id)
    return mapping


def read_assays(path: Path, wanted: set[str]) -> dict[str, dict[str, str]]:
    assays: dict[str, dict[str, str]] = {}
    csv.field_size_limit(sys.maxsize)
    with zipfile.ZipFile(path) as archive, archive.open(archive_member(path)) as binary:
        text = (line.decode("utf-8", errors="replace") for line in binary)
        for row in csv.DictReader(text, delimiter="\t"):
            key = f"{row['ENTRYID'].strip()}_{row['ASSAYID'].strip()}"
            if key not in wanted:
                continue
            value = {
                "assay_name": html.unescape(row["ASSAY_NAME"].strip()),
                "assay_description": html.unescape(row["DESCRIPTION"].strip()),
            }
            previous = assays.get(key)
            if previous is not None and previous != value:
                raise ValueError(f"conflicting BindingDB assay rows for {key}")
            assays[key] = value
    return assays


def target_type(candidate: dict) -> str:
    if candidate["microbial_root"] == "Viruses":
        return "VIRAL_PROTEIN"
    try:
        chains = int(candidate.get("chain_count") or "1")
    except ValueError:
        chains = 1
    return "PROTEIN_COMPLEX" if chains > 1 else "PROTEIN"


def clean_proteins(candidate: dict, counts: Counter) -> list[dict]:
    proteins = []
    seen = set()
    for protein in candidate.get("protein_examples") or []:
        accession = protein["accession"]
        if not UNIPROT_ACCESSION_RE.fullmatch(accession):
            counts["omitted_invalid_uniprot_accession"] += 1
            continue
        if accession in seen:
            continue
        seen.add(accession)
        proteins.append(protein)
    return proteins


def extract(
    articles: Path,
    taxdump: Path,
    reactant_assays: Path,
    assays: Path,
) -> tuple[list[dict[str, str]], Counter]:
    candidates, initial = collect_candidates(articles)
    accepted, taxonomy = classify_candidates(candidates, taxdump)
    counts = initial + taxonomy

    rsid_map = read_reactant_assays(reactant_assays)
    wanted_assays = {
        entry_assay_id
        for candidate in accepted
        for entry_assay_id in rsid_map.get(candidate["bindingdb_reactant_set_id"], set())
    }
    assay_map = read_assays(assays, wanted_assays)

    rows: list[dict[str, str]] = []
    for candidate in accepted:
        rsid = candidate["bindingdb_reactant_set_id"]
        entry_assay_ids = rsid_map.get(rsid, set())
        if len(entry_assay_ids) != 1:
            counts["rejected_missing_or_ambiguous_assay_mapping"] += 1
            continue
        entry_assay_id = next(iter(entry_assay_ids))
        assay = assay_map.get(entry_assay_id)
        if not assay or not assay["assay_description"]:
            counts["rejected_missing_assay_description"] += 1
            continue
        proteins = clean_proteins(candidate, counts)
        for measurement_type, raw in sorted(candidate["measurements"].items()):
            parsed = parse_measurement(raw)
            if parsed is None:
                counts["rejected_unparseable_measurement"] += 1
                continue
            qualifier, value = parsed
            relation = (
                "DIRECT_BINDING_TARGET"
                if measurement_type == "Kd"
                else "MEASURED_TARGET_ASSOCIATION"
            )
            rows.append({
                "identifier": candidate["identifier"],
                "standard_inchi_key": candidate["standard_inchi_key"],
                "bindingdb_reactant_set_id": rsid,
                "bindingdb_monomer_id": candidate["bindingdb_monomer_id"],
                "target_name": candidate["target_name"],
                "target_type": target_type(candidate),
                "target_relation": relation,
                "taxon_id": str(candidate["taxon_id"]),
                "taxon_label": candidate["taxon_label"],
                "microbial_root": candidate["microbial_root"],
                "chain_count": candidate["chain_count"],
                "measurement_type": measurement_type.upper(),
                "original_value": raw,
                "qualifier": qualifier,
                "value": format(value, ".15g"),
                "unit": "nM",
                "bindingdb_entry_assay_id": entry_assay_id,
                "assay_name": assay["assay_name"],
                "assay_description": assay["assay_description"],
                "reference": candidate["reference"],
                "article_doi": candidate["article_doi"],
                "pmid": candidate["pmid"],
                "protein_examples_json": json.dumps(proteins, separators=(",", ":")),
                "source_version": SOURCE_VERSION,
                "source_retrieved_on": SOURCE_RETRIEVED_ON,
                "curation_source": CURATED_MARKER,
            })
            counts["inventory_measurements"] += 1
    rows.sort(key=lambda row: (
        row["identifier"],
        row["target_name"],
        row["taxon_id"],
        row["target_relation"],
        row["bindingdb_reactant_set_id"],
        row["measurement_type"],
    ))
    counts["inventory_records"] = len({row["identifier"] for row in rows})
    counts["inventory_target_assertions"] = len({
        (row["identifier"], row["target_name"], row["taxon_id"], row["target_relation"])
        for row in rows
    })
    return rows, counts


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        raise ValueError("refusing to write an empty BindingDB inventory")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def update_manifest(paths: list[Path], inventory: Path) -> None:
    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}
    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))["bindingdb"]
    manifest.setdefault("sources", {})["bindingdb"] = {
        "homepage": conf["homepage"],
        "license": conf["license"],
        "version": SOURCE_VERSION,
        "retrieved_on": SOURCE_RETRIEVED_ON,
        "row_policy": CURATED_MARKER,
    }
    downloads = manifest.setdefault("downloads", {})
    urls = {
        conf["articles_archive_name"]: conf["articles_archive_url"],
        conf["assays_archive_name"]: conf["assays_archive_url"],
        conf["reactant_assays_archive_name"]: conf["reactant_assays_archive_url"],
        conf["taxdump_archive_name"]: conf["taxdump_archive_url"],
    }
    for path in paths:
        downloads[path.name] = {
            "url": urls[path.name],
            "bytes": path.stat().st_size,
            "sha256": sha256_of(path),
        }
    with inventory.open(newline="", encoding="utf-8") as handle:
        row_count = sum(1 for _ in csv.DictReader(handle, delimiter="\t"))
    manifest.setdefault("inventories", {})[inventory.name] = {
        "rows": row_count,
        "bytes": inventory.stat().st_size,
        "sha256": sha256_of(inventory),
        "source": "BindingDB literature-curated rows with assay and NCBI Taxonomy joins",
    }
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--articles", type=Path, required=True)
    parser.add_argument("--taxdump", type=Path, required=True)
    parser.add_argument("--reactant-assays", type=Path, required=True)
    parser.add_argument("--assays", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    paths = [args.articles, args.assays, args.reactant_assays, args.taxdump]
    missing = [str(path) for path in paths if not path.exists()]
    if missing:
        raise SystemExit(f"missing pinned archive(s): {', '.join(missing)}")

    rows, counts = extract(args.articles, args.taxdump, args.reactant_assays, args.assays)
    print(f"BindingDB {SOURCE_VERSION}: {len(rows)} accepted measurements", file=sys.stderr)
    for name, count in sorted(counts.items()):
        print(f"  {name}: {count}", file=sys.stderr)
    if args.dry_run:
        print("--dry-run: nothing written", file=sys.stderr)
        return 0
    inventory = RAW_DIR / INVENTORY_NAME
    write_tsv(inventory, rows)
    update_manifest(paths, inventory)
    print(f"wrote {inventory.relative_to(REPO_ROOT)} and data/raw/MANIFEST.yaml", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
