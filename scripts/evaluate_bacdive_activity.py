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
import hashlib
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
ACTIVITY_ID_VERSION = "bacdive_activity_row_v1"
ACTIVITY_ID_COLUMNS = [
    "source_record_id",
    "identifier",
    "standard_inchi_key",
    "bacdive_id",
    "source_section",
    "source_row_index",
    "source_field",
]
ACTIVITY_REPORT_COLUMNS = [
    "source_activity_id",
    "source_version",
    "source_record_id",
    "source_name",
    "identifier",
    "standard_inchi_key",
    "bacdive_id",
    "taxon_label",
    "strain",
    "source_section",
    "source_row_index",
    "source_field",
    "source_reference_ids",
    "activity",
    "source_concentration",
    "disk_diffusion_value",
    "disk_diffusion_units",
    "assay",
    "medium",
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
ANTIBIOTICA_CONCENTRATION_ALIASES = (
    "concentration",
    "concentrationantib",
    "metaboliteconcentration",
)
ANTIBIOTICA_ACTIVITY_ALIASES = {
    "SUSCEPTIBLE": ("issensitive", "absensitive"),
    "INTERMEDIATE": ("isintermediate", "abintermediate"),
    "RESISTANT": ("isresistant", "abresistant"),
}
ACTIVITY_CALLS = frozenset(ANTIBIOTICA_ACTIVITY_ALIASES)
REFERENCE_ALIASES = ("ref",)
TAXONOMY_SECTION_KEYS = {
    "nameandtaxonomicclassification",
    "nametaxonomicclassification",
}
TAXON_LABEL_ALIASES = (
    "fullscientificname",
    "scientificname",
    "species",
)
STRAIN_ALIASES = (
    "straindesignation",
    "strain",
)
ANTIBIOGRAM_MEDIUM_ALIASES = (
    "medium",
    "mediumantibiogram",
    "mediumantibiogramv2",
)

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


def as_rows(value: Any, context: str) -> list[Mapping[str, Any]]:
    if isinstance(value, Mapping):
        return [value]
    if isinstance(value, list):
        rows = []
        for index, item in enumerate(value, start=1):
            if not isinstance(item, Mapping):
                raise ValueError(f"{context} row {index} is not an object")
            rows.append(item)
        return rows
    if value not in (None, ""):
        raise ValueError(f"{context} must be an object or array")
    return []


def bacdive_records_by_id(
    path: Path,
    entries: Iterable[tuple[str, Any]],
) -> dict[str, Mapping[str, Any]]:
    records: dict[str, Mapping[str, Any]] = {}
    for record_key, record in entries:
        if not isinstance(record, Mapping):
            raise ValueError(
                f"{path}: result {record_key} is not a BacDive record object"
            )
        identifier = bacdive_id(record_key, record)
        if identifier in records:
            raise ValueError(f"{path}: duplicate BacDive-ID {identifier}")
        records[identifier] = record
    return records


def read_bacdive_fetch(path: Path) -> dict[str, Mapping[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"{path}: expected a BacDive v2 fetch JSON object")
    if "General" in payload:
        return {bacdive_id("1", payload): payload}

    results = payload.get("results", payload)
    if isinstance(results, list):
        return bacdive_records_by_id(
            path,
            ((str(index), record) for index, record in enumerate(results, start=1)),
        )
    if isinstance(results, Mapping):
        return bacdive_records_by_id(
            path,
            ((str(record_key), record) for record_key, record in results.items()),
        )
    raise ValueError(f"{path}: expected a results object or array")


def merge_bacdive_records(
    records: dict[str, Mapping[str, Any]],
    incoming: Mapping[str, Mapping[str, Any]],
    path: Path,
) -> None:
    duplicate_ids = sorted(set(records) & set(incoming))
    if duplicate_ids:
        joined = ", ".join(duplicate_ids)
        raise ValueError(f"{path}: duplicate BacDive-ID across inputs: {joined}")
    records.update(incoming)


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
    _, value = first_field_value(row, aliases)
    return value


def first_field_value(
    row: Mapping[str, Any],
    aliases: Iterable[str],
) -> tuple[str, str]:
    alias_set = set(aliases)
    for key, value in row.items():
        if value in (None, ""):
            continue
        if normalize(str(key)) in alias_set:
            return str(key), str(value).strip()
    return "", ""


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


def source_reference_ids(row: Mapping[str, Any]) -> str:
    values: set[str] = set()
    for key, value in row.items():
        if normalize(str(key)) not in REFERENCE_ALIASES or value in (None, ""):
            continue
        raw_values = value if isinstance(value, list) else [value]
        for raw_value in raw_values:
            text = str(raw_value).strip()
            if text:
                values.add(text)
    return "|".join(sorted(values))


def record_sections(
    bacdive_id_value: str,
    record: Mapping[str, Any],
    wanted_keys: Iterable[str],
) -> Iterable[Mapping[str, Any]]:
    wanted = set(wanted_keys)
    for key, value in record.items():
        if normalize(str(key)) not in wanted:
            continue
        if isinstance(value, Mapping):
            yield value
        elif value not in (None, ""):
            raise ValueError(f"BacDive-ID {bacdive_id_value} {key} must be an object")


def taxon_context(bacdive_id_value: str, record: Mapping[str, Any]) -> dict[str, str]:
    for section in record_sections(
        bacdive_id_value,
        record,
        TAXONOMY_SECTION_KEYS,
    ):
        return {
            "taxon_label": first_value(section, TAXON_LABEL_ALIASES),
            "strain": first_value(section, STRAIN_ALIASES),
        }
    return {"taxon_label": "", "strain": ""}


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


def physiology_sections(
    bacdive_id_value: str,
    record: Mapping[str, Any],
) -> Iterable[Mapping[str, Any]]:
    yield from record_sections(
        bacdive_id_value,
        record,
        PHYSIOLOGY_SECTION_KEYS,
    )


def source_section_rows(
    section: Mapping[str, Any],
    wanted_keys: Iterable[str],
    *,
    bacdive_id_value: str,
) -> Iterable[Mapping[str, Any]]:
    wanted = set(wanted_keys)
    for key, value in section.items():
        if normalize(str(key)) in wanted:
            yield from as_rows(value, f"BacDive-ID {bacdive_id_value} {key}")


def antibiotic_name_rows(
    bacdive_id_value: str,
    record: Mapping[str, Any],
) -> Iterable[tuple[str, str, str, str]]:
    for section in physiology_sections(bacdive_id_value, record):
        for row in source_section_rows(
            section,
            ANTIBIOTICA_SECTION_KEYS,
            bacdive_id_value=bacdive_id_value,
        ):
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
    bacdive_id_value: str,
    record: Mapping[str, Any],
) -> Iterable[tuple[str, str, str | None]]:
    for section in physiology_sections(bacdive_id_value, record):
        for key, value in section.items():
            source_section = ANTIBIOGRAM_SECTION_BY_KEY.get(normalize(str(key)))
            if source_section is None:
                continue
            for row in as_rows(value, f"BacDive-ID {bacdive_id_value} {key}"):
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


def exact_activity_rows(
    records: Mapping[str, Mapping[str, Any]],
    drug_map: Mapping[str, Mapping[str, str]],
    source_version: str,
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for bacdive_id_value, record in sorted(records.items()):
        context = taxon_context(bacdive_id_value, record)
        if not context["taxon_label"]:
            continue

        for section in physiology_sections(bacdive_id_value, record):
            for source_row_index, row in enumerate(
                source_section_rows(
                    section,
                    ANTIBIOTICA_SECTION_KEYS,
                    bacdive_id_value=bacdive_id_value,
                ),
                start=1,
            ):
                source_field, source_name = first_field_value(
                    row,
                    ANTIBIOTICA_NAME_ALIASES,
                )
                mapping = drug_map.get(normalize(source_name))
                activity = activity_call(row)
                if (
                    not mapping
                    or mapping.get("mapping_status") != EXACT_MAPPING_STATUS
                    or not activity
                ):
                    continue

                rows.append(
                    activity_report_row(
                        mapping=mapping,
                        source_version=source_version,
                        bacdive_id=bacdive_id_value,
                        source_section="met_antibiotica",
                        source_row_index=source_row_index,
                        source_field=source_field,
                        source_reference_ids=source_reference_ids(row),
                        taxon_label=context["taxon_label"],
                        strain=context["strain"],
                        activity=activity,
                        source_concentration=first_value(
                            row,
                            ANTIBIOTICA_CONCENTRATION_ALIASES,
                        ),
                    )
                )

            for key, value in section.items():
                source_section = ANTIBIOGRAM_SECTION_BY_KEY.get(normalize(str(key)))
                if source_section is None:
                    continue

                for source_row_index, row in enumerate(
                    as_rows(value, f"BacDive-ID {bacdive_id_value} {key}"),
                    start=1,
                ):
                    medium = first_value(row, ANTIBIOGRAM_MEDIUM_ALIASES)
                    for field, cell in row.items():
                        source_name, row_source_section = antibiogram_source_name(
                            str(field),
                            source_section,
                        )
                        mapping = drug_map.get(normalize(source_name))
                        disk_value = disk_diffusion_value(cell)
                        if (
                            not mapping
                            or mapping.get("mapping_status") != EXACT_MAPPING_STATUS
                            or not disk_value
                        ):
                            continue

                        rows.append(
                            activity_report_row(
                                mapping=mapping,
                                source_version=source_version,
                                bacdive_id=bacdive_id_value,
                                source_section=row_source_section,
                                source_row_index=source_row_index,
                                source_field=str(field),
                                source_reference_ids=source_reference_ids(row),
                                taxon_label=context["taxon_label"],
                                strain=context["strain"],
                                disk_diffusion_value=disk_value,
                                medium=medium,
                                assay=f"BacDive {row_source_section} disk diffusion",
                            )
                        )

    return rows


def activity_report_row(
    *,
    mapping: Mapping[str, str],
    source_version: str,
    bacdive_id: str,
    source_section: str,
    source_row_index: int,
    source_field: str,
    source_reference_ids: str,
    taxon_label: str,
    strain: str,
    activity: str = "",
    source_concentration: str = "",
    disk_diffusion_value: str = "",
    medium: str = "",
    assay: str = "",
) -> dict[str, str]:
    row = {
        "source_version": source_version,
        "source_record_id": mapping["source_record_id"],
        "source_name": mapping["source_name"],
        "identifier": mapping["identifier"],
        "standard_inchi_key": mapping["standard_inchi_key"],
        "bacdive_id": bacdive_id,
        "taxon_label": taxon_label,
        "strain": strain,
        "source_section": source_section,
        "source_row_index": str(source_row_index),
        "source_field": source_field,
        "source_reference_ids": source_reference_ids,
        "activity": activity,
        "source_concentration": source_concentration,
        "disk_diffusion_value": disk_diffusion_value,
        "disk_diffusion_units": "mm" if disk_diffusion_value else "",
        "assay": assay,
        "medium": medium,
    }
    row["source_activity_id"] = source_activity_id(row)
    return row


def source_activity_id(row: Mapping[str, str]) -> str:
    payload = "\x1f".join(
        [
            ACTIVITY_ID_VERSION,
            *(row[column] for column in ACTIVITY_ID_COLUMNS),
        ]
    )
    return f"bacdive:{hashlib.sha256(payload.encode('utf-8')).hexdigest()[:16]}"


def evaluate_records(
    records: Mapping[str, Mapping[str, Any]],
    name_candidates: Mapping[str, set[str]],
    structure_keys: Mapping[str, str],
    drug_map: Mapping[str, Mapping[str, str]] | None = None,
) -> list[dict[str, str]]:
    entries: dict[str, dict[str, Any]] = {}
    drug_map = drug_map or {}

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
        for source_name, section, activity, chebi_id in antibiotic_name_rows(
            bacdive_id_value,
            record,
        ):
            entry = entry_for(source_name)
            entry["source_names"].add(source_name)
            entry["source_sections"].add(section)
            entry["bacdive_rows"] += 1
            entry["bacdive_ids"].add(bacdive_id_value)
            if activity:
                entry["activity_calls"][activity] += 1
            if chebi_id:
                entry["source_chebi_ids"].add(chebi_id)

        for source_name, section, value in antibiogram_rows(bacdive_id_value, record):
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
        mapping = drug_map.get(normalized, {})
        report_rows.append(
            {
                "source_record_id": normalized,
                "source_name": source_name,
                "normalized_source_name": normalized,
                "source_sections": "|".join(sorted(entry["source_sections"])),
                "bacdive_row_count": str(entry["bacdive_rows"]),
                "bacdive_id_count": str(len(entry["bacdive_ids"])),
                "bacdive_ids": "|".join(sorted(entry["bacdive_ids"])),
                "activity_call_count": str(sum(entry["activity_calls"].values())),
                "activity_calls": "|".join(
                    f"{activity}:{count}" for activity, count in sorted(entry["activity_calls"].items())
                ),
                "disk_diffusion_count": str(entry["disk_diffusion_count"]),
                "invalid_disk_diffusion_count": str(entry["invalid_disk_diffusion_count"]),
                "standardized_disk_diffusion_values": "|".join(sorted(entry["disk_diffusion_values"])),
                "source_chebi_ids": "|".join(sorted(entry["source_chebi_ids"])),
                "exact_name_candidate_count": str(len(candidates)),
                "exact_name_candidate_identifiers": "|".join(candidates),
                "exact_name_candidate_inchi_keys": "|".join(
                    structure_keys[identifier] for identifier in candidates
                ),
                "mapping_status": mapping.get("mapping_status", ""),
                "identifier": mapping.get("identifier", ""),
                "standard_inchi_key": mapping.get("standard_inchi_key", ""),
                "mapping_basis": mapping.get("mapping_basis", ""),
                "mapping_notes": mapping.get("notes", ""),
            }
        )
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


def require_activity_report_rows(rows: list[dict[str, str]], path: Path) -> None:
    seen_activity_ids = set()
    for index, row in enumerate(rows, start=1):
        prefix = f"{path}: row {index}"
        for field in ACTIVITY_REPORT_COLUMNS:
            if field not in row:
                raise ValueError(f"{prefix}: missing {field}")
            require_tsv_safe_value(row[field], field, prefix)

        require_non_blank_fields(
            row,
            (
                "source_activity_id",
                "source_version",
                "source_record_id",
                "source_name",
                "identifier",
                "standard_inchi_key",
                "bacdive_id",
                "taxon_label",
                "source_section",
                "source_row_index",
                "source_field",
            ),
            path,
            index,
        )
        if row["source_activity_id"] != source_activity_id(row):
            raise ValueError(f"{prefix}: source_activity_id is stale")
        if row["source_activity_id"] in seen_activity_ids:
            raise ValueError(f"{prefix}: duplicate source_activity_id")
        seen_activity_ids.add(row["source_activity_id"])
        if row["source_record_id"] != normalize(row["source_name"]):
            raise ValueError(
                f"{prefix}: source_record_id must be the normalized source_name"
            )

        try:
            source_row_index = int(row["source_row_index"])
        except ValueError as error:
            raise ValueError(f"{prefix}: source_row_index must be numeric") from error
        if source_row_index <= 0:
            raise ValueError(f"{prefix}: source_row_index must be positive")
        if row["source_row_index"] != str(source_row_index):
            raise ValueError(
                f"{prefix}: source_row_index must use canonical integer "
                f"{source_row_index!r}"
            )
        if row["source_section"] not in {
            "met_antibiogram",
            "met_antibiogram_v2",
            "met_antibiotica",
        }:
            raise ValueError(f"{prefix}: unsupported source_section {row['source_section']!r}")
        if row["activity"] and row["activity"] not in ACTIVITY_CALLS:
            raise ValueError(f"{prefix}: unsupported activity {row['activity']!r}")
        if not row["activity"] and not row["disk_diffusion_value"]:
            raise ValueError(f"{prefix}: activity or disk_diffusion_value is required")
        if row["source_section"] == "met_antibiotica":
            if normalize(row["source_field"]) not in ANTIBIOTICA_NAME_ALIASES:
                raise ValueError(
                    f"{prefix}: unsupported met_antibiotica source_field "
                    f"{row['source_field']!r}"
                )
            if not row["activity"]:
                raise ValueError(f"{prefix}: met_antibiotica rows require activity")
            if (
                row["disk_diffusion_value"]
                or row["disk_diffusion_units"]
                or row["assay"]
                or row["medium"]
            ):
                raise ValueError(
                    f"{prefix}: met_antibiotica rows must not carry "
                    "disk-diffusion fields"
                )
        else:
            if row["activity"]:
                raise ValueError(
                    f"{prefix}: disk-diffusion rows must not carry activity"
                )
            if row["source_concentration"]:
                raise ValueError(
                    f"{prefix}: disk-diffusion rows must not carry "
                    "source_concentration"
                )
            expected_assay = f"BacDive {row['source_section']} disk diffusion"
            if row["assay"] != expected_assay:
                raise ValueError(f"{prefix}: assay must be {expected_assay!r}")
            source_name, source_section = antibiogram_source_name(
                row["source_field"],
                row["source_section"],
            )
            if not source_name:
                raise ValueError(
                    f"{prefix}: unsupported disk-diffusion source_field "
                    f"{row['source_field']!r}"
                )
            if source_section != row["source_section"]:
                raise ValueError(
                    f"{prefix}: source_field {row['source_field']!r} belongs to "
                    f"{source_section}, not {row['source_section']}"
                )
            if source_name != row["source_name"]:
                raise ValueError(
                    f"{prefix}: source_field {row['source_field']!r} maps to "
                    f"{source_name!r}, not source_name {row['source_name']!r}"
                )

        if row["disk_diffusion_value"] and row["disk_diffusion_units"] != "mm":
            raise ValueError(f"{prefix}: disk_diffusion_units must be mm")
        if row["disk_diffusion_units"] and not row["disk_diffusion_value"]:
            raise ValueError(f"{prefix}: disk_diffusion_units requires disk_diffusion_value")
        if row["disk_diffusion_value"] and not row["assay"]:
            raise ValueError(f"{prefix}: assay is required for disk_diffusion_value")
        if (
            row["disk_diffusion_value"]
            and disk_diffusion_value(row["disk_diffusion_value"]) != row["disk_diffusion_value"]
        ):
            raise ValueError(f"{prefix}: invalid disk_diffusion_value")


def require_exact_table_row(row: dict, path: Path, line_number: int) -> None:
    prefix = f"{path}:{line_number}"
    if None in row:
        raise ValueError(f"{prefix}: unexpected extra delimited field")
    for field, value in row.items():
        if value is None:
            raise ValueError(f"{prefix}: {field} is missing")


def require_curated_tsv_value(value: str, field: str, prefix: str) -> str:
    if any(char in value for char in CURATED_TSV_CONTROL_CHARS):
        raise ValueError(f"{prefix}: {field} contains a tab or newline")
    if value != value.strip():
        raise ValueError(f"{prefix}: {field} has leading or trailing whitespace")
    return value


def require_curated_tsv_row(
    row: dict[str, str],
    path: Path,
    line_number: int,
) -> dict[str, str]:
    prefix = f"{path}:{line_number}"
    return {field: require_curated_tsv_value(value, field, prefix) for field, value in row.items()}


def require_non_blank_fields(
    row: Mapping[str, str],
    fields: Iterable[str],
    path: Path,
    line_number: int,
) -> None:
    for field in fields:
        if not row[field]:
            raise ValueError(f"{path}:{line_number}: {field} is required")


def report_rows_by_source_record_id(
    rows: Iterable[Mapping[str, str]],
) -> dict[str, Mapping[str, str]]:
    by_source_record_id: dict[str, Mapping[str, str]] = {}
    for row in rows:
        source_record_id = row["source_record_id"]
        if source_record_id in by_source_record_id:
            raise ValueError(f"duplicate BacDive report source_record_id: {source_record_id}")
        by_source_record_id[source_record_id] = row
    return by_source_record_id


def read_drug_map(
    path: Path,
    structure_keys: Mapping[str, str],
    current_report_rows: Iterable[Mapping[str, str]],
    source_version: str,
) -> dict[str, dict[str, str]]:
    """Read and validate a curated BacDive antibiotic-name crosswalk."""

    current_rows = report_rows_by_source_record_id(current_report_rows)
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != DRUG_MAP_COLUMNS:
            raise ValueError(f"unexpected BacDive drug map columns: {reader.fieldnames}")

        rows = {}
        for line_number, row in enumerate(reader, start=2):
            require_exact_table_row(row, path, line_number)
            row = require_curated_tsv_row(row, path, line_number)
            require_non_blank_fields(
                row,
                (
                    "source_version",
                    "source_record_id",
                    "source_name",
                    "mapping_status",
                    "mapping_basis",
                    "notes",
                ),
                path,
                line_number,
            )

            source_record_id = row["source_record_id"]
            source_name = row["source_name"]
            current_row = current_rows.get(source_record_id)
            if current_row is None:
                raise ValueError(
                    f"{source_name}: source_record_id {source_record_id!r} "
                    "is not in the current BacDive report"
                )
            if source_name != current_row["source_name"]:
                raise ValueError(
                    f"{source_record_id}: source_name {source_name!r} "
                    f"!= current BacDive source_name {current_row['source_name']!r}"
                )
            if source_record_id in rows:
                raise ValueError(f"duplicate BacDive drug mapping: {source_record_id}")
            if row["source_version"] != source_version:
                raise ValueError(
                    f"{source_name}: source_version {row['source_version']!r} != {source_version!r}"
                )
            if row["mapping_status"] not in MAPPING_STATUSES:
                raise ValueError(f"{source_name}: unknown mapping_status {row['mapping_status']!r}")

            has_mapping = bool(row["identifier"] or row["standard_inchi_key"])
            if row["mapping_status"] != EXACT_MAPPING_STATUS:
                if has_mapping:
                    raise ValueError(f"{source_name}: non-EXACT mapping must not carry structure fields")
                rows[source_record_id] = row
                continue

            identifier = row["identifier"]
            if not identifier or not row["standard_inchi_key"]:
                raise ValueError(f"{source_name}: EXACT mapping needs identifier and standard_inchi_key")
            expected = structure_keys.get(identifier)
            if expected is None:
                raise ValueError(f"{source_name}: mapped identifier {identifier} is not in the corpus")
            if row["standard_inchi_key"] != expected:
                raise ValueError(
                    f"{source_name}: mapped InChIKey {row['standard_inchi_key']} "
                    f"does not match {identifier} ({expected})"
                )
            rows[source_record_id] = row

        if not rows:
            raise ValueError(f"{path}: BacDive drug map has no rows")
        return rows


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


def read_activity_report(
    path: Path,
    structure_keys: Mapping[str, str],
    source_version: str,
) -> list[dict[str, str]]:
    """Read and validate a BacDive exact activity report."""

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != ACTIVITY_REPORT_COLUMNS:
            raise ValueError(
                f"unexpected BacDive activity report columns: {reader.fieldnames}"
            )

        rows = []
        for line_number, row in enumerate(reader, start=2):
            require_exact_table_row(row, path, line_number)
            rows.append(require_curated_tsv_row(row, path, line_number))

    if not rows:
        raise ValueError(f"{path}: BacDive activity report has no rows")

    require_activity_report_rows(rows, path)
    for index, row in enumerate(rows, start=1):
        prefix = f"{path}: row {index}"
        if row["source_version"] != source_version:
            raise ValueError(
                f"{prefix}: source_version {row['source_version']!r} "
                f"!= {source_version!r}"
            )

        identifier = row["identifier"]
        expected = structure_keys.get(identifier)
        if expected is None:
            raise ValueError(
                f"{prefix}: mapped identifier {identifier} is not in the corpus"
            )
        if row["standard_inchi_key"] != expected:
            raise ValueError(
                f"{prefix}: mapped InChIKey {row['standard_inchi_key']} "
                f"does not match {identifier} ({expected})"
            )
    return rows


def write_activity_report(rows: list[dict[str, str]], path: Path) -> None:
    require_activity_report_rows(rows, path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=ACTIVITY_REPORT_COLUMNS,
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
            writer.writerow(
                {
                    "source_version": source_version,
                    "source_record_id": row["source_record_id"],
                    "source_name": row["source_name"],
                    "mapping_status": row["mapping_status"],
                    "identifier": row["identifier"],
                    "standard_inchi_key": row["standard_inchi_key"],
                    "mapping_basis": row["mapping_basis"],
                    "notes": row["mapping_notes"],
                }
            )


def reject_reused_cli_paths(
    parser: argparse.ArgumentParser,
    paths: Iterable[tuple[str, Path | None]],
) -> None:
    """Prevent one evaluator invocation from overwriting its own inputs/outputs."""

    seen: dict[Path, str] = {}
    for option, path in paths:
        if path is None:
            continue
        resolved = path.expanduser().resolve()
        previous = seen.get(resolved)
        if previous is not None:
            parser.error(f"{option} must not reuse {previous} path: {path}")
        seen[resolved] = option


def reject_unsafe_cli_output_paths(
    parser: argparse.ArgumentParser,
    paths: Iterable[tuple[str, Path | None]],
) -> None:
    """Reject output paths that would fail after sibling reports are written."""

    output_paths = []
    for option, path in paths:
        if path is None:
            continue

        expanded = path.expanduser()
        if expanded.exists() and expanded.is_dir():
            parser.error(f"{option} must be a file path, not a directory: {path}")
        if expanded.parent.exists() and not expanded.parent.is_dir():
            parser.error(f"{option} parent must be a directory: {expanded.parent}")
        output_paths.append((option, path, expanded.resolve(strict=False)))

    for child_option, child_path, child_resolved in output_paths:
        for parent_option, _, parent_resolved in output_paths:
            if child_option != parent_option and parent_resolved in child_resolved.parents:
                parser.error(f"{child_option} must not be nested under {parent_option} path: {child_path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bacdive",
        type=Path,
        nargs="+",
        default=[],
        help=(
            "One or more BacDive v2 /fetch JSON exports. Required unless "
            "only --validate-activity-report is used."
        ),
    )
    parser.add_argument(
        "--source-version",
        default="",
        help=(
            "Optional BacDive export version to pin --drug-map mappings, "
            "validate --validate-activity-report rows, and stamp on "
            "--drug-map-template and --activity-report rows."
        ),
    )
    parser.add_argument(
        "--drug-map",
        type=Path,
        help="Optional curated TSV crosswalk from BacDive antibiotic names to exact structures.",
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
    parser.add_argument(
        "--activity-report",
        type=Path,
        help="Optional exact-mapped TSV of BacDive activity rows with source context.",
    )
    parser.add_argument(
        "--validate-activity-report",
        type=Path,
        help="Optional existing BacDive exact activity TSV to validate.",
    )
    args = parser.parse_args()
    if args.activity_report and not args.drug_map:
        parser.error("--activity-report requires --drug-map.")
    if (
        args.drug_map
        or args.drug_map_template
        or args.activity_report
        or args.validate_activity_report
    ) and not args.source_version.strip():
        parser.error(
            "--drug-map, --drug-map-template, --activity-report and "
            "--validate-activity-report require --source-version."
        )
    if args.source_version != args.source_version.strip():
        parser.error("--source-version must not have leading or trailing whitespace.")
    if any(char in args.source_version for char in CURATED_TSV_CONTROL_CHARS):
        parser.error("--source-version must not contain tabs or newlines.")
    if not args.bacdive and (
        not args.validate_activity_report
        or args.drug_map
        or args.drug_report
        or args.drug_map_template
        or args.activity_report
    ):
        parser.error("--bacdive is required unless only --validate-activity-report is used.")
    reject_reused_cli_paths(
        parser,
        [("--bacdive", path) for path in args.bacdive]
        + [
            ("--drug-map", args.drug_map),
            ("--drug-report", args.drug_report),
            ("--drug-map-template", args.drug_map_template),
            ("--activity-report", args.activity_report),
            ("--validate-activity-report", args.validate_activity_report),
        ],
    )
    reject_unsafe_cli_output_paths(
        parser,
        (
            ("--drug-report", args.drug_report),
            ("--drug-map-template", args.drug_map_template),
            ("--activity-report", args.activity_report),
        ),
    )

    records: dict[str, Mapping[str, Any]] = {}
    for path in args.bacdive:
        merge_bacdive_records(records, read_bacdive_fetch(path), path)

    name_candidates, structure_keys = corpus_name_candidates()
    validated_activity_rows = (
        read_activity_report(
            args.validate_activity_report,
            structure_keys,
            args.source_version,
        )
        if args.validate_activity_report
        else []
    )
    template_rows = evaluate_records(records, name_candidates, structure_keys)
    drug_map = (
        read_drug_map(
            args.drug_map,
            structure_keys,
            template_rows,
            source_version=args.source_version,
        )
        if args.drug_map
        else {}
    )
    rows = evaluate_records(records, name_candidates, structure_keys, drug_map) if drug_map else template_rows

    if args.drug_report:
        write_drug_report(rows, args.drug_report)
    if args.drug_map_template:
        write_drug_map_template(
            template_rows,
            args.drug_map_template,
            args.source_version,
        )
    activity_rows = (
        exact_activity_rows(records, drug_map, args.source_version)
        if args.activity_report
        else []
    )
    if args.activity_report:
        write_activity_report(activity_rows, args.activity_report)

    print(
        "BacDive activity preflight: "
        f"records={len(records)} antibiotic_values={len(rows)} "
        f"rows={sum(int(row['bacdive_row_count']) for row in rows)} "
        f"single_exact_name_candidates={sum(1 for row in rows if row['exact_name_candidate_count'] == '1')} "
        f"exact_activity_rows={len(activity_rows)} "
        f"activity_report_rows={len(validated_activity_rows)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
