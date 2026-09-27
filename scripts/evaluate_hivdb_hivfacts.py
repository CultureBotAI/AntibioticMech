#!/usr/bin/env python3
"""Audit Stanford HIVDB hivfacts drugs against corpus exact-structure records.

hivfacts names drugs by HIVDB abbreviations and includes boosted protease
inhibitors such as ATV/r. This preflight reports exact lexical corpus matches
as identity-curation leads only: HIVDB scoring rules still need a mutation model
before the repository can seed resistance assertions from them.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_DRUG_MAP = REPO_ROOT / "curation" / "hivdb_drug_map.tsv"
HIVDB_HIVFACTS_COMMIT = "be1c11a5145fea9073fdb71801919d4a34265336"

REQUIRED_DRUG_FIELDS = ("displayAbbr", "drugClass", "fullName", "name")
DRUG_REPORT_COLUMNS = [
    "source_record_id",
    "display_abbr",
    "name",
    "full_name",
    "drug_class",
    "ritonavir_boosted",
    "synonyms",
    "exact_name_candidate_count",
    "exact_name_candidate_identifiers",
    "exact_name_candidate_inchi_keys",
    "matched_aliases",
    "mapping_status",
    "identifier",
    "standard_inchi_key",
    "mapping_basis",
    "mapping_notes",
]
DRUG_MAP_COLUMNS = [
    "source_version",
    "source_record_id",
    "source_name",
    "hivdb_name",
    "drug_class",
    "mapping_status",
    "identifier",
    "standard_inchi_key",
    "mapping_basis",
    "notes",
]

EXACT_MAPPING_STATUS = "EXACT"
MAPPING_STATUSES = {
    EXACT_MAPPING_STATUS,
    "AMBIGUOUS_IDENTITY",
    "COMBINATION",
    "MISSING_CORPUS_RECORD",
}
CURATED_TSV_CONTROL_CHARS = frozenset("\t\r\n")


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def corpus_name_candidates(root: Path = REPO_ROOT) -> tuple[dict[str, set[str]], dict[str, str]]:
    candidates: dict[str, set[str]] = defaultdict(set)
    structure_keys: dict[str, str] = {}

    for path in sorted((root / "data" / "antibiotics").rglob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        identifier = record["identifier"]
        structure_keys[identifier] = record["chemical_structure"]["standard_inchi_key"]

        names = {record["label"]}
        names.update(
            synonym["synonym_text"]
            for synonym in (record.get("synonyms") or [])
            if synonym.get("synonym_text")
        )
        for name in names:
            candidates[normalize(name)].add(identifier)

    return candidates, structure_keys


def read_drugs(path: Path) -> list[dict[str, str]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"{path}: expected a JSON array")

    rows = []
    seen = set()
    for index, item in enumerate(payload, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"{path}: row {index} is not an object")
        for field in REQUIRED_DRUG_FIELDS:
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError(f"{path}: row {index} has no {field}")
        raw_synonyms = item.get("synonyms", [])
        if not isinstance(raw_synonyms, list):
            raise ValueError(f"{path}: {item['displayAbbr']} synonyms is not a list")
        for synonym_index, synonym in enumerate(raw_synonyms, start=1):
            if not isinstance(synonym, str):
                raise ValueError(
                    f"{path}: {item['displayAbbr']} synonym {synonym_index} is not a string"
                )

        display_abbr = item["displayAbbr"].strip()
        if display_abbr in seen:
            raise ValueError(f"{path}: duplicate HIVDB drug abbreviation {display_abbr}")
        seen.add(display_abbr)
        rows.append(
            {
                "source_record_id": display_abbr,
                "display_abbr": display_abbr,
                "name": item["name"].strip(),
                "full_name": item["fullName"].strip(),
                "drug_class": item["drugClass"].strip(),
                "synonyms": "|".join(
                    sorted(
                        synonym.strip()
                        for synonym in raw_synonyms
                        if synonym.strip()
                    )
                ),
            }
        )

    return rows


def drug_aliases(row: dict[str, str]) -> list[str]:
    aliases = {row["display_abbr"], row["name"], row["full_name"]}
    aliases.update(synonym for synonym in row["synonyms"].split("|") if synonym)
    return sorted(aliases, key=lambda alias: (alias.casefold(), alias))


def is_ritonavir_boosted(row: dict[str, str]) -> bool:
    return "/r" in row["display_abbr"] or "/r" in row["full_name"]


def require_exact_table_row(row: dict, path: Path, line_number: int) -> None:
    prefix = f"{path}:{line_number}"
    if None in row:
        raise ValueError(f"{prefix}: unexpected extra delimited field")
    for field, value in row.items():
        if value is None:
            raise ValueError(f"{prefix}: {field} is missing")


def require_non_blank_fields(
    row: dict[str, str],
    fields: Iterable[str],
    path: Path,
    line_number: int,
) -> None:
    for field in fields:
        if not row[field].strip():
            raise ValueError(f"{path}:{line_number}: {field} is required")


def strip_curated_tsv_row(
    row: dict[str, str],
    path: Path,
    line_number: int,
) -> dict[str, str]:
    for field, value in row.items():
        if any(char in value for char in CURATED_TSV_CONTROL_CHARS):
            raise ValueError(f"{path}:{line_number}: {field} contains a tab or newline")
    return {field: value.strip() for field, value in row.items()}


def read_drug_map(
    path: Path,
    structure_keys: dict[str, str],
    source_rows: list[dict[str, str]],
) -> dict[str, dict[str, str]]:
    """Read a curated HIVDB abbreviation-to-structure crosswalk."""

    sources = {row["source_record_id"]: row for row in source_rows}
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != DRUG_MAP_COLUMNS:
            raise ValueError(f"unexpected HIVDB drug map columns: {reader.fieldnames}")

        rows = {}
        for line_number, row in enumerate(reader, start=2):
            require_exact_table_row(row, path, line_number)
            row = strip_curated_tsv_row(row, path, line_number)
            require_non_blank_fields(
                row,
                (
                    "source_record_id",
                    "source_name",
                    "hivdb_name",
                    "drug_class",
                    "source_version",
                    "mapping_status",
                    "mapping_basis",
                    "notes",
                ),
                path,
                line_number,
            )

            source_record_id = row["source_record_id"]
            if source_record_id in rows:
                raise ValueError(f"duplicate HIVDB drug mapping: {source_record_id}")
            if row["source_version"] != HIVDB_HIVFACTS_COMMIT:
                raise ValueError(
                    f"{source_record_id}: source_version {row['source_version']!r} "
                    f"!= {HIVDB_HIVFACTS_COMMIT!r}"
                )
            if row["mapping_status"] not in MAPPING_STATUSES:
                raise ValueError(
                    f"{source_record_id}: unknown mapping_status {row['mapping_status']!r}"
                )

            has_mapping = bool(row["identifier"] or row["standard_inchi_key"])
            if row["mapping_status"] != EXACT_MAPPING_STATUS:
                if has_mapping:
                    raise ValueError(
                        f"{source_record_id}: non-EXACT mapping must not carry structure fields"
                    )
                rows[source_record_id] = row
                continue

            identifier = row["identifier"]
            if not identifier or not row["standard_inchi_key"]:
                raise ValueError(
                    f"{source_record_id}: EXACT mapping needs identifier and standard_inchi_key"
                )
            expected = structure_keys.get(identifier)
            if expected is None:
                raise ValueError(
                    f"{source_record_id}: mapped identifier {identifier} is not in the corpus"
                )
            if row["standard_inchi_key"] != expected:
                raise ValueError(
                    f"{source_record_id}: mapped InChIKey {row['standard_inchi_key']} "
                    f"does not match {identifier} ({expected})"
                )
            rows[source_record_id] = row

    missing = set(sources) - set(rows)
    extra = set(rows) - set(sources)
    if missing or extra:
        raise ValueError(
            "HIVDB drug map/source mismatch: "
            f"missing={sorted(missing)} extra={sorted(extra)}"
        )

    for source_record_id, source_row in sources.items():
        row = rows[source_record_id]
        expected = {
            "source_name": source_row["full_name"],
            "hivdb_name": source_row["name"],
            "drug_class": source_row["drug_class"],
        }
        for field, expected_value in expected.items():
            if row[field] != expected_value:
                raise ValueError(
                    f"{source_record_id}: mapped {field} {row[field]!r} != "
                    f"hivfacts {field} {expected_value!r}"
                )

    return rows


def evaluate_drugs(
    rows: list[dict[str, str]],
    candidates: dict[str, set[str]],
    structure_keys: dict[str, str],
    mappings: Mapping[str, Mapping[str, str]] | None = None,
) -> dict:
    if mappings is None:
        mappings = {}

    report_rows = []
    exact_name_matched = 0
    ambiguous = 0
    unmatched = 0

    for row in rows:
        matched_aliases = []
        identifiers = set()
        for alias in drug_aliases(row):
            alias_identifiers = candidates.get(normalize(alias), set())
            if alias_identifiers:
                matched_aliases.append(alias)
                identifiers.update(alias_identifiers)

        if len(identifiers) == 1:
            exact_name_matched += 1
        elif len(identifiers) > 1:
            ambiguous += 1
        else:
            unmatched += 1

        sorted_identifiers = sorted(identifiers)
        mapping = mappings.get(row["source_record_id"], {})
        report_rows.append(
            {
                **row,
                "ritonavir_boosted": "true" if is_ritonavir_boosted(row) else "false",
                "exact_name_candidate_count": len(sorted_identifiers),
                "exact_name_candidate_identifiers": "|".join(sorted_identifiers),
                "exact_name_candidate_inchi_keys": "|".join(
                    structure_keys[identifier] for identifier in sorted_identifiers
                ),
                "matched_aliases": "|".join(matched_aliases),
                "mapping_status": mapping.get("mapping_status", ""),
                "identifier": mapping.get("identifier", ""),
                "standard_inchi_key": mapping.get("standard_inchi_key", ""),
                "mapping_basis": mapping.get("mapping_basis", ""),
                "mapping_notes": mapping.get("notes", ""),
            }
        )

    return {
        "hivdb_drugs": len(rows),
        "drug_classes": Counter(row["drug_class"] for row in rows),
        "ritonavir_boosted_drugs": sum(is_ritonavir_boosted(row) for row in rows),
        "exact_name_matched_drugs": exact_name_matched,
        "ambiguous_name_drugs": ambiguous,
        "unmatched_drugs": unmatched,
        "drug_rows": report_rows,
    }


def write_drug_report(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=DRUG_REPORT_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_drug_map_template(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=DRUG_MAP_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "source_version": HIVDB_HIVFACTS_COMMIT,
                    "source_record_id": row["source_record_id"],
                    "source_name": row["full_name"],
                    "hivdb_name": row["name"],
                    "drug_class": row["drug_class"],
                    "mapping_status": row["mapping_status"],
                    "identifier": row["identifier"],
                    "standard_inchi_key": row["standard_inchi_key"],
                    "mapping_basis": row["mapping_basis"],
                    "notes": row["mapping_notes"],
                }
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--drugs", type=Path, required=True, help="hivfacts data/drugs.json.")
    parser.add_argument("--drug-report", type=Path, help="Optional TSV drug identity audit.")
    parser.add_argument("--drug-map", type=Path, help="Optional curated HIVDB drug crosswalk.")
    parser.add_argument(
        "--drug-map-template",
        type=Path,
        help="Optional TSV template for a curated HIVDB drug crosswalk.",
    )
    parser.add_argument("--corpus-root", type=Path, default=REPO_ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()

    if not args.drugs.exists():
        raise SystemExit(f"missing hivfacts drugs input: {args.drugs}")

    candidates, structure_keys = corpus_name_candidates(args.corpus_root)
    drugs = read_drugs(args.drugs)
    mappings = read_drug_map(args.drug_map, structure_keys, drugs) if args.drug_map else {}
    result = evaluate_drugs(drugs, candidates, structure_keys, mappings=mappings)

    print("Stanford HIVDB hivfacts drug identity audit")
    print(
        f"  hivdb_drugs={result['hivdb_drugs']} "
        f"exact_name_matched={result['exact_name_matched_drugs']} "
        f"ambiguous={result['ambiguous_name_drugs']} "
        f"unmatched={result['unmatched_drugs']} "
        f"ritonavir_boosted={result['ritonavir_boosted_drugs']}"
    )
    print(
        "  drug classes: "
        + ", ".join(f"{name}={count}" for name, count in sorted(result["drug_classes"].items()))
    )

    if args.drug_report:
        write_drug_report(result["drug_rows"], args.drug_report)
        print(f"wrote {args.drug_report}")
    if args.drug_map_template:
        write_drug_map_template(result["drug_rows"], args.drug_map_template)
        print(f"wrote {args.drug_map_template}")

    print("--audit: no rows seeded; HIVDB mutation rules need a schema-specific importer")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
