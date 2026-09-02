#!/usr/bin/env python3
"""Audit AMRFinderPlus database coverage against committed CARD/ARO edges.

The audit reports only exact normalized lexical overlap.  It does not seed
AMRFinderPlus rows: family and drug-class strings are valuable coverage signals
but neither identifies an individual chemical structure nor proves that a
catalog family confers resistance to every member of a named class.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from collections import Counter, defaultdict
from pathlib import Path

VERSION = "2026-08-07.1"


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def read_families(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        header = handle.readline().lstrip("#").rstrip("\n").split("\t")
        return list(csv.DictReader(handle, fieldnames=header, delimiter="\t"))


def evaluate(catalog_path: Path, families_path: Path, aro_path: Path) -> dict:
    with catalog_path.open(newline="", encoding="utf-8") as handle:
        catalog = list(csv.DictReader(handle, delimiter="\t"))
    families = read_families(families_path)
    with aro_path.open(newline="", encoding="utf-8") as handle:
        aro = list(csv.DictReader(handle, delimiter="\t"))

    versions = {row["db_version"] for row in catalog}
    if versions != {VERSION}:
        raise ValueError(f"unexpected AMRFinderPlus catalog versions: {sorted(versions)}")
    reportable = [
        row for row in families
        if row["reportable"] != "0" and row["type"] == "AMR" and row["subtype"] == "AMR"
    ]
    aro_by_name: dict[str, set[str]] = defaultdict(set)
    for row in aro:
        aro_by_name[normalize(row["determinant_name"])].add(row["determinant_id"])
    matched_nodes = set()
    for row in reportable:
        for field in ("node_id", "gene_symbol", "family_name"):
            if normalize(row[field]) in aro_by_name:
                matched_nodes.add(row["node_id"])
                break

    amr_catalog = [
        row for row in catalog if row["type"] == "AMR" and row["subtype"] == "AMR"
    ]
    subclass_tokens = {
        normalize(token)
        for row in amr_catalog
        for token in row["subclass"].split("/")
        if normalize(token)
    }
    aro_drug_names = {normalize(row["antibiotic_name"]) for row in aro}
    return {
        "aro_edges": len(aro),
        "aro_determinants": len({row["determinant_id"] for row in aro}),
        "aro_drugs": len({row["antibiotic_id"] for row in aro}),
        "reportable_families": len(reportable),
        "exact_family_name_overlap": len(matched_nodes),
        "unmatched_family_names": len(reportable) - len(matched_nodes),
        "catalog_rows": len(amr_catalog),
        "catalog_families": len({row["gene_family"] for row in amr_catalog}),
        "catalog_rows_with_pubmed": sum(bool(row["pubmed_reference"]) for row in amr_catalog),
        "classes": Counter(row["class"] for row in amr_catalog),
        "subclass_tokens": len(subclass_tokens),
        "subclass_token_aro_name_overlap": len(subclass_tokens & aro_drug_names),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--families", type=Path, required=True)
    parser.add_argument("--aro", type=Path, required=True)
    args = parser.parse_args()
    missing = [str(path) for path in (args.catalog, args.families, args.aro) if not path.exists()]
    if missing:
        raise SystemExit(f"missing audit input(s): {', '.join(missing)}")
    result = evaluate(args.catalog, args.families, args.aro)
    print(f"AMRFinderPlus {VERSION} audit")
    print(f"  catalog_sha256={sha256_of(args.catalog)}")
    print(f"  families_sha256={sha256_of(args.families)}")
    print(
        f"  ARO: edges={result['aro_edges']} determinants={result['aro_determinants']} "
        f"drugs={result['aro_drugs']}"
    )
    print(
        f"  AMRFinderPlus: reportable_families={result['reportable_families']} "
        f"exact_name_overlap={result['exact_family_name_overlap']} "
        f"unmatched_names={result['unmatched_family_names']}"
    )
    print(
        f"  catalog: rows={result['catalog_rows']} families={result['catalog_families']} "
        f"rows_with_pubmed={result['catalog_rows_with_pubmed']}"
    )
    print(
        f"  drug subclass tokens={result['subclass_tokens']} "
        f"exact ARO drug-name overlap={result['subclass_token_aro_name_overlap']}"
    )
    print("  leading classes: " + ", ".join(
        f"{name}={count}" for name, count in result["classes"].most_common(10)
    ))
    print("--audit: no rows seeded; family/class strings do not establish structure-specific claims")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
