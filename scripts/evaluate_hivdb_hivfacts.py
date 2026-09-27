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
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]

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
]


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


def evaluate_drugs(
    rows: list[dict[str, str]],
    candidates: dict[str, set[str]],
    structure_keys: dict[str, str],
) -> dict:
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--drugs", type=Path, required=True, help="hivfacts data/drugs.json.")
    parser.add_argument("--drug-report", type=Path, help="Optional TSV drug identity audit.")
    parser.add_argument("--corpus-root", type=Path, default=REPO_ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()

    if not args.drugs.exists():
        raise SystemExit(f"missing hivfacts drugs input: {args.drugs}")

    candidates, structure_keys = corpus_name_candidates(args.corpus_root)
    result = evaluate_drugs(read_drugs(args.drugs), candidates, structure_keys)

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

    print("--audit: no rows seeded; HIVDB mutation rules need a schema-specific importer")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
