#!/usr/bin/env python3
"""Evaluate BacDive v2 fetch exports for exact activity-observation fit.

BacDive names antibiotics in two activity-bearing physiology subsections:
``met_antibiotica`` stores name-level susceptible/intermediate/resistant calls
and ``met_antibiogram_v2`` stores disk-diffusion inhibition diameters in fixed
antibiotic columns. This preflight keeps lexical corpus matches as curation
leads only; a future seeder needs a curated exact-structure crosswalk before it
can attach any BacDive observation to an AntibioticRecord.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]

DRUG_MAP_COLUMNS = [
    "source_version",
    "source_record_id",
    "source_name",
    "mapping_status",
    "identifier",
    "standard_inchi_key",
    "mapping_basis",
    "notes",
]
DRUG_REPORT_COLUMNS = [
    "source_record_id",
    "source_name",
    "normalized_source_name",
    "source_sections",
    "bacdive_row_count",
    "bacdive_id_count",
    "bacdive_ids",
    "activity_call_count",
    "activity_calls",
    "disk_diffusion_count",
    "invalid_disk_diffusion_count",
    "standardized_disk_diffusion_values",
    "source_chebi_ids",
    "exact_name_candidate_count",
    "exact_name_candidate_identifiers",
    "exact_name_candidate_inchi_keys",
    "mapping_status",
    "identifier",
    "standard_inchi_key",
    "mapping_basis",
    "mapping_notes",
]

EXACT_MAPPING_STATUS = "EXACT"
MAPPING_STATUSES = {
    EXACT_MAPPING_STATUS,
    "AMBIGUOUS_STEREOCHEMISTRY",
    "COMBINATION",
    "DRUG_CLASS",
    "MISSING_CORPUS_RECORD",
    "MIXTURE",
}
CURATED_TSV_CONTROL_CHARS = frozenset("\t\r\n")
PHYSIOLOGY_SECTION_KEYS = {
    "physiologyandmetabolism",
    "physiologymetabolism",
}
ANTIBIOTICA_SECTION_KEYS = {
    "antibioticresistance",
    "metantibiotica",
}
ANTIBIOGRAM_SECTION_BY_KEY = {
    "antibiogram": "met_antibiogram",
    "metantibiogram": "met_antibiogram",
    "antibiogramv2": "met_antibiogram_v2",
    "metantibiogramv2": "met_antibiogram_v2",
}

ANTIBIOTICA_NAME_ALIASES = (
    "metabolite",
    "metaboliteantib",
    "antibiotic",
)
ANTIBIOTICA_CHEBI_ALIASES = ("chebiid",)
ANTIBIOTICA_ACTIVITY_ALIASES = {
    "SUSCEPTIBLE": ("issensitive", "absensitive"),
    "INTERMEDIATE": ("isintermediate", "abintermediate"),
    "RESISTANT": ("isresistant", "abresistant"),
}

ANTIBIOGRAM_V1_FIELDS = {
    "P": "Penicillin G",
    "OX": "Oxacillin",
    "AMP": "Ampicillin",
    "TIC": "Ticarcillin",
    "MEZ": "Mezlocillin",
    "KF": "Cefalotin",
    "KZ": "Cefazolin",
    "CTX": "Cefotaxime",
    "ATM": "Aztreonam",
    "IPM": "Imipenem",
    "TE": "Tetracycline",
    "C": "Chloramphenicol",
    "CN": "Gentamicin",
    "AK": "Amikacin",
    "VA": "Vancomycin",
    "E": "Erythromycin",
    "MY": "Lincomycin",
    "OFX": "Ofloxacin",
    "NOR": "Norfloxacin",
    "CT": "Colistin",
    "PIP": "Pipemidic acid",
    "F": "Nitrofurantoin",
    "B": "Bacitracin",
    "PB": "Polymyxin B",
    "K": "Kanamycin",
    "N": "Neomycin",
    "DO": "Doxycycline",
    "CRO": "Ceftriaxone",
    "DA": "Clindamycin",
    "FOS": "Fosfomycin",
    "MXF": "Moxifloxacin",
    "LZD": "Linezolid",
    "NS": "Nystatin",
    "QD": "Quinupristin/Dalfopristin",
    "TEC": "Teicoplanin",
    "TZP": "Piperacillin/Tazobactam",
}
ANTIBIOGRAM_V2_FIELDS = {
    "AMP": "Ampicillin",
    "OX": "Oxacillin",
    "P": "Penicillin G",
    "ATM": "Aztreonam",
    "TIC": "Ticarcillin",
    "CTX": "Cefotaxime",
    "CAZ": "Ceftazidime",
    "CRO": "Ceftriaxone",
    "FDC": "Cefiderocol",
    "TZP": "Piperacillin/Tazobactam",
    "IPM": "Imipenem",
    "MEM": "Meropenem",
    "CIP": "Ciprofloxacin",
    "LEV": "Levofloxacin",
    "MXF": "Moxifloxacin",
    "OFX": "Ofloxacin",
    "AK": "Amikacin",
    "CN": "Gentamicin",
    "TE": "Tetracycline",
    "TGC": "Tigecycline",
    "TEC": "Teicoplanin",
    "VA": "Vancomycin",
    "PB": "Polymyxin B",
    "CT": "Colistin sulphate",
    "DA": "Clindamycin",
    "E": "Erythromycin",
    "FOS": "Fosfomycin",
    "K": "Kanamycin",
    "C": "Chloramphenicol",
    "LZD": "Linezolid",
    "F": "Nitrofurantoin",
    "QD": "Quinupristin/Dalfopristin",
    "RD": "Rifampicin",
    "SXT": "Trimethoprim-sulfamethoxazole (1:19)",
}
ANTIBIOGRAM_FIELDS_BY_SECTION = {
    "met_antibiogram": ANTIBIOGRAM_V1_FIELDS,
    "met_antibiogram_v2": ANTIBIOGRAM_V2_FIELDS,
}

TRUE_ACTIVITY_VALUES = {"1", "+", "true", "yes", "positive"}
CHEBI_ID_PATTERN = re.compile(r"^(?:CHEBI[:_])?(?P<id>[1-9][0-9]*)$", re.IGNORECASE)
DISK_DIFFUSION_VALUE_PATTERN = re.compile(r"^(?:\d+(?:\.\d*)?|\.\d+)$")


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def normalized_disk_field(value: str, suffix: str) -> str:
    normalized = normalize(value)
    return normalized.removesuffix(suffix)


def antibiogram_source_name(
    field: str,
    fallback_section: str,
) -> tuple[str, str]:
    normalized_field = normalize(field)
    if normalized_field.endswith("antibiogramv2"):
        code = normalized_disk_field(field, "antibiogramv2").upper()
        return ANTIBIOGRAM_V2_FIELDS.get(code, ""), "met_antibiogram_v2"
    if normalized_field.endswith("antibiogram"):
        code = normalized_disk_field(field, "antibiogram").upper()
        return ANTIBIOGRAM_V1_FIELDS.get(code, ""), "met_antibiogram"

    code = normalized_field.upper()
    return ANTIBIOGRAM_FIELDS_BY_SECTION[fallback_section].get(code, ""), fallback_section


def bacdive_id(record_key: str, record: Mapping[str, Any]) -> str:
    general = record.get("General")
    if isinstance(general, Mapping):
        value = general.get("BacDive-ID") or general.get("BacDive ID")
        if value not in (None, ""):
            return str(value)
    return str(record_key)


def as_rows(value: Any) -> list[Mapping[str, Any]]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, Mapping)]
    if isinstance(value, Mapping):
        return [value]
    return []


def read_bacdive_fetch(path: Path) -> dict[str, Mapping[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"{path}: expected a BacDive v2 fetch JSON object")
    if "General" in payload:
        return {bacdive_id("1", payload): payload}

    results = payload.get("results", payload)
    if isinstance(results, list):
        return {
            bacdive_id(str(index), record): record
            for index, record in enumerate(results, start=1)
            if isinstance(record, Mapping)
        }
    if isinstance(results, Mapping):
        return {
            bacdive_id(str(record_key), record): record
            for record_key, record in results.items()
            if isinstance(record, Mapping)
        }
    raise ValueError(f"{path}: expected a results object or array")


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


def first_value(row: Mapping[str, Any], aliases: Iterable[str]) -> str:
    alias_set = set(aliases)
    for key, value in row.items():
        if value in (None, ""):
            continue
        if normalize(str(key)) in alias_set:
            return str(value).strip()
    return ""


def source_chebi_id(row: Mapping[str, Any]) -> str:
    chebi_id = first_value(row, ANTIBIOTICA_CHEBI_ALIASES)
    if not chebi_id:
        return ""
    match = CHEBI_ID_PATTERN.match(chebi_id.strip())
    if match is None:
        return ""
    return f"CHEBI:{match.group('id')}"


def activity_call(row: Mapping[str, Any]) -> str:
    observed = []
    for activity, aliases in ANTIBIOTICA_ACTIVITY_ALIASES.items():
        value = normalize(first_value(row, aliases))
        if value in TRUE_ACTIVITY_VALUES:
            observed.append(activity)
    if len(observed) != 1:
        return ""
    return observed[0]


def decimal_string(value: Decimal) -> str:
    return format(value.normalize(), "f")


def disk_diffusion_value(value: Any) -> str | None:
    if value in (None, ""):
        return ""
    text = str(value).strip()
    if not text:
        return ""
    if DISK_DIFFUSION_VALUE_PATTERN.match(text) is None:
        return None
    try:
        parsed = Decimal(text)
    except InvalidOperation:
        return None
    if parsed <= 0:
        return None
    return decimal_string(parsed)


def physiology_sections(record: Mapping[str, Any]) -> Iterable[Mapping[str, Any]]:
    for key, value in record.items():
        if normalize(str(key)) in PHYSIOLOGY_SECTION_KEYS and isinstance(value, Mapping):
            yield value


def source_section_rows(
    section: Mapping[str, Any],
    wanted_keys: Iterable[str],
) -> Iterable[Mapping[str, Any]]:
    wanted = set(wanted_keys)
    for key, value in section.items():
        if normalize(str(key)) in wanted:
            yield from as_rows(value)


def antibiotic_name_rows(record: Mapping[str, Any]) -> Iterable[tuple[str, str, str, str]]:
    for section in physiology_sections(record):
        for row in source_section_rows(section, ANTIBIOTICA_SECTION_KEYS):
            source_name = first_value(row, ANTIBIOTICA_NAME_ALIASES)
            if not source_name:
                continue
            yield (
                source_name,
                "met_antibiotica",
                activity_call(row),
                source_chebi_id(row),
            )


def antibiogram_rows(
    record: Mapping[str, Any],
) -> Iterable[tuple[str, str, str | None]]:
    for section in physiology_sections(record):
        for key, value in section.items():
            source_section = ANTIBIOGRAM_SECTION_BY_KEY.get(normalize(str(key)))
            if source_section is None:
                continue
            for row in as_rows(value):
                for field, cell in row.items():
                    source_name, row_source_section = antibiogram_source_name(
                        str(field),
                        source_section,
                    )
                    if not source_name:
                        continue
                    standardized_value = disk_diffusion_value(cell)
                    if standardized_value:
                        yield source_name, row_source_section, standardized_value
                    elif standardized_value is None:
                        yield source_name, row_source_section, None


def evaluate_records(
    records: Mapping[str, Mapping[str, Any]],
    name_candidates: Mapping[str, set[str]],
    structure_keys: Mapping[str, str],
) -> list[dict[str, str]]:
    entries: dict[str, dict[str, Any]] = {}

    def entry_for(source_name: str) -> dict[str, Any]:
        normalized = normalize(source_name)
        return entries.setdefault(
            normalized,
            {
                "source_record_id": normalized,
                "source_names": set(),
                "source_sections": set(),
                "bacdive_rows": 0,
                "bacdive_ids": set(),
                "activity_calls": Counter(),
                "disk_diffusion_count": 0,
                "invalid_disk_diffusion_count": 0,
                "disk_diffusion_values": set(),
                "source_chebi_ids": set(),
            },
        )

    for bacdive_id_value, record in sorted(records.items()):
        for source_name, section, activity, chebi_id in antibiotic_name_rows(record):
            entry = entry_for(source_name)
            entry["source_names"].add(source_name)
            entry["source_sections"].add(section)
            entry["bacdive_rows"] += 1
            entry["bacdive_ids"].add(bacdive_id_value)
            if activity:
                entry["activity_calls"][activity] += 1
            if chebi_id:
                entry["source_chebi_ids"].add(chebi_id)

        for source_name, section, value in antibiogram_rows(record):
            entry = entry_for(source_name)
            entry["source_names"].add(source_name)
            entry["source_sections"].add(section)
            entry["bacdive_rows"] += 1
            entry["bacdive_ids"].add(bacdive_id_value)
            if value is None:
                entry["invalid_disk_diffusion_count"] += 1
            else:
                entry["disk_diffusion_count"] += 1
                entry["disk_diffusion_values"].add(f"{value} mm")

    report_rows = []
    for normalized, entry in sorted(entries.items()):
        source_name = sorted(entry["source_names"], key=lambda name: (name.casefold(), name))[0]
        candidates = sorted(name_candidates.get(normalized, set()))
        report_rows.append({
            "source_record_id": normalized,
            "source_name": source_name,
            "normalized_source_name": normalized,
            "source_sections": "|".join(sorted(entry["source_sections"])),
            "bacdive_row_count": str(entry["bacdive_rows"]),
            "bacdive_id_count": str(len(entry["bacdive_ids"])),
            "bacdive_ids": "|".join(sorted(entry["bacdive_ids"])),
            "activity_call_count": str(sum(entry["activity_calls"].values())),
            "activity_calls": "|".join(
                f"{activity}:{count}"
                for activity, count in sorted(entry["activity_calls"].items())
            ),
            "disk_diffusion_count": str(entry["disk_diffusion_count"]),
            "invalid_disk_diffusion_count": str(entry["invalid_disk_diffusion_count"]),
            "standardized_disk_diffusion_values": "|".join(
                sorted(entry["disk_diffusion_values"])
            ),
            "source_chebi_ids": "|".join(sorted(entry["source_chebi_ids"])),
            "exact_name_candidate_count": str(len(candidates)),
            "exact_name_candidate_identifiers": "|".join(candidates),
            "exact_name_candidate_inchi_keys": "|".join(
                structure_keys[identifier] for identifier in candidates
            ),
            "mapping_status": "",
            "identifier": "",
            "standard_inchi_key": "",
            "mapping_basis": "",
            "mapping_notes": "",
        })
    return report_rows


def require_tsv_safe_value(value: str, field: str, prefix: str) -> str:
    value = str(value).strip()
    if any(char in value for char in CURATED_TSV_CONTROL_CHARS):
        raise ValueError(f"{prefix}: {field} contains a tab or newline")
    return value


def require_report_rows(rows: list[dict[str, str]], path: Path) -> None:
    for index, row in enumerate(rows, start=1):
        prefix = f"{path}: row {index}"
        for field in DRUG_REPORT_COLUMNS:
            if field not in row:
                raise ValueError(f"{prefix}: missing {field}")
            require_tsv_safe_value(row[field], field, prefix)
        if row["source_record_id"] != row["normalized_source_name"]:
            raise ValueError(f"{prefix}: source_record_id must be the normalized source_name")
        if row["source_record_id"] != normalize(row["source_name"]):
            raise ValueError(f"{prefix}: normalized_source_name drift for source_name")
        if row["mapping_status"] and row["mapping_status"] not in MAPPING_STATUSES:
            raise ValueError(f"{prefix}: unknown mapping_status {row['mapping_status']!r}")


def write_drug_report(rows: list[dict[str, str]], path: Path) -> None:
    require_report_rows(rows, path)
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


def write_drug_map_template(rows: list[dict[str, str]], path: Path, source_version: str) -> None:
    require_report_rows(rows, path)
    source_version = require_tsv_safe_value(source_version, "source_version", str(path))
    if not source_version:
        raise ValueError(f"{path}: source_version is required")

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
            writer.writerow({
                "source_version": source_version,
                "source_record_id": row["source_record_id"],
                "source_name": row["source_name"],
                "mapping_status": row["mapping_status"],
                "identifier": row["identifier"],
                "standard_inchi_key": row["standard_inchi_key"],
                "mapping_basis": row["mapping_basis"],
                "notes": row["mapping_notes"],
            })


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bacdive",
        type=Path,
        nargs="+",
        required=True,
        help="One or more BacDive v2 /fetch JSON exports.",
    )
    parser.add_argument(
        "--source-version",
        default="",
        help="Optional BacDive export version to stamp on --drug-map-template rows.",
    )
    parser.add_argument(
        "--drug-report",
        type=Path,
        help="Optional TSV summarizing BacDive antibiotic names seen in activity rows.",
    )
    parser.add_argument(
        "--drug-map-template",
        type=Path,
        help="Optional fillable TSV crosswalk from BacDive antibiotic names to exact structures.",
    )
    args = parser.parse_args()

    records: dict[str, Mapping[str, Any]] = {}
    for path in args.bacdive:
        records.update(read_bacdive_fetch(path))

    name_candidates, structure_keys = corpus_name_candidates()
    rows = evaluate_records(records, name_candidates, structure_keys)

    if args.drug_report:
        write_drug_report(rows, args.drug_report)
    if args.drug_map_template:
        write_drug_map_template(rows, args.drug_map_template, args.source_version)

    print(
        "BacDive activity preflight: "
        f"records={len(records)} antibiotic_values={len(rows)} "
        f"rows={sum(int(row['bacdive_row_count']) for row in rows)} "
        f"single_exact_name_candidates={sum(1 for row in rows if row['exact_name_candidate_count'] == '1')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
