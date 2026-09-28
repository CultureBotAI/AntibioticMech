#!/usr/bin/env python3
"""Evaluate an exported NCBI Pathogen Detection AST table for exact-structure fit.

NCBI AST rows identify the tested drug by a submitted antibiotic string, not by
a stable chemical structure identifier. This preflight keeps lexical corpus
matches as an audit signal only: a future seeder still needs a curated,
versioned crosswalk for every accepted NCBI antibiotic value.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from collections import Counter, defaultdict
from collections.abc import Iterable
from datetime import date
from decimal import Decimal
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]

DRUG_MAP_COLUMNS = [
    "source_record_id",
    "source_name",
    "mapping_status",
    "identifier",
    "standard_inchi_key",
    "mapping_basis",
    "notes",
]
PROJECT_DEDUPE_COLUMNS = [
    "accession_type",
    "accession",
    "source",
    "source_version",
    "notes",
]
PROJECT_DEDUPE_REPORT_COLUMNS = [
    "accession_type",
    "accession",
    "ast_rows",
    "exact_mapped_rows",
    "exact_mapped_antibiotic_values",
    "exact_mapped_antibiotics",
    "exact_mapped_identifiers",
    "biosample_count",
    "bioproject_count",
    "antibiotic_values",
    "antibiotics",
    "taxon_labels",
]
# Bump with ACTIVITY_REPORT_GROUP_COLUMNS because those columns define the
# stable activity_group_id digest for committed exact reports.
ACTIVITY_GROUP_ID_VERSION = "ncbi_ast_activity_group_v3"
ACTIVITY_REPORT_GROUP_COLUMNS = [
    "source_name",
    "normalized_antibiotic",
    "identifier",
    "standard_inchi_key",
    "taxon_label",
    "biosample_accession",
    "bioproject_accession",
    "target_accession",
    "assembly_accession",
    "sra_accessions",
    "phenotype",
    "activity",
    "mic_value",
    "mic_qualifier",
    "mic_units",
    "disk_diffusion_value",
    "disk_diffusion_qualifier",
    "disk_diffusion_units",
    "platform",
    "vendor",
    "reagent",
    "standard",
]
ACTIVITY_REPORT_COLUMNS = [
    "activity_group_id",
    "source_version",
    "source_retrieved_on",
    "ast_row_count",
    "isolate_count",
    *ACTIVITY_REPORT_GROUP_COLUMNS,
]
EXACT_MAPPING_STATUS = "EXACT"
PROJECT_DEDUPE_SELF_SOURCE = "NCBI_AST"
CURATED_TSV_CONTROL_CHARS = frozenset("\t\r\n")
MAPPING_STATUSES = {
    EXACT_MAPPING_STATUS,
    "AMBIGUOUS_STEREOCHEMISTRY",
    "COMBINATION",
    "DRUG_CLASS",
    "MISSING_CORPUS_RECORD",
    "MIXTURE",
}

ANTIBIOTIC_ALIASES = (
    "antibiotic",
    "astantibiotic",
    "amrantibiotic",
    "agent",
    "drug",
)
BIOSAMPLE_ALIASES = ("biosample", "biosampleaccession", "biosampleacc")
BIOPROJECT_ALIASES = ("bioproject", "bioprojectaccession", "bioprojectacc")
TARGET_ALIASES = ("targetacc", "targetaccession", "target", "isolate")
ASSEMBLY_ALIASES = ("assemblyaccession", "assembly", "asmacc")
SRA_ALIASES = ("sra", "sraaccession", "sraaccessions", "sraacc", "run", "runs")
MIC_ALIASES = ("mic", "micvalue", "minimuminhibitoryconcentration")
DISK_ALIASES = ("diskdiffusion", "diskdiameter", "diskzone")
MEASUREMENT_SIGN_ALIASES = ("measurementsign", "sign")
PLATFORM_ALIASES = ("platform", "laboratorytypingplatform")
REAGENT_ALIASES = ("reagent", "laboratorytypingmethodversionorreagent")
STANDARD_ALIASES = ("standard", "testingstandard")
VENDOR_ALIASES = ("vendor",)
PHENOTYPE_ALIASES = (
    "phenotype",
    "astphenotype",
    "resistancephenotype",
    "sir",
    "interpretation",
)
MEASUREMENT_PATTERN = re.compile(r"^(?P<qualifier><=|>=|<|>|=)?\s*(?P<value>(?:\d+(?:\.\d*)?|\.\d+))$")
MEASUREMENT_SIGNS = {"", "<=", ">=", "<", ">", "="}
MIC_UNITS = "mg/L"
DISK_DIFFUSION_UNITS = "mm"
BIOSAMPLE_PATTERN = re.compile(r"^SAM(N|D|EA)[0-9]+$")
BIOPROJECT_PATTERN = re.compile(r"^PRJ(NA|EB|DB)[0-9]+$")
TARGET_PATTERN = re.compile(r"^PDT[0-9]+(\.[0-9]+)?$")
ASSEMBLY_PATTERN = re.compile(r"^GC[AF]_[0-9]+(\.[0-9]+)?$")
SRA_ACCESSION_PATTERN = re.compile(r"^(SRR|ERR|DRR|SRX|ERX|DRX|SRP|ERP|DRP|SRS|ERS|DRS)[0-9]+$")
SRA_SPLIT_PATTERN = re.compile(r"[\s,;|]+")
PROJECT_DEDUPE_ACCESSIONS = {
    "BioSample": (BIOSAMPLE_ALIASES, BIOSAMPLE_PATTERN),
    "BioProject": (BIOPROJECT_ALIASES, BIOPROJECT_PATTERN),
}
ACTIVITY_CALLS = {
    "i": "INTERMEDIATE",
    "intermediate": "INTERMEDIATE",
    "r": "RESISTANT",
    "resistant": "RESISTANT",
    "s": "SUSCEPTIBLE",
    "susceptible": "SUSCEPTIBLE",
}
TAXON_ALIASES = (
    "scientificname",
    "organismname",
    "taxonlabel",
    "taxname",
    "organism",
    "organismgroup",
    "taxgroupname",
    "taxgroup",
)


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def normalize_header(value: str) -> str:
    return normalize(value.removeprefix("AST.").removeprefix("AMR."))


def first_value(row: dict[str, str], aliases: Iterable[str]) -> str:
    for alias in aliases:
        for key, value in row.items():
            if key is None:
                continue
            if value is None:
                continue
            if normalize_header(key) == alias and value.strip():
                return value.strip()
    return ""


def has_value(row: dict[str, str], aliases: Iterable[str]) -> bool:
    return bool(first_value(row, aliases))


def has_project_context(row: dict[str, str]) -> bool:
    return has_value(row, BIOSAMPLE_ALIASES) and has_value(row, BIOPROJECT_ALIASES)


def has_valid_project_context(row: dict[str, str]) -> bool:
    biosample_accession = first_value(row, BIOSAMPLE_ALIASES)
    bioproject_accession = first_value(row, BIOPROJECT_ALIASES)
    return (
        BIOSAMPLE_PATTERN.match(biosample_accession) is not None
        and BIOPROJECT_PATTERN.match(bioproject_accession) is not None
    )


def valid_accession(
    row: dict[str, str],
    aliases: Iterable[str],
    pattern: re.Pattern[str],
) -> str | None:
    accession = first_value(row, aliases)
    if not accession:
        return ""
    if pattern.match(accession) is None:
        return None
    return accession


def valid_target_accession(row: dict[str, str]) -> str | None:
    return valid_accession(row, TARGET_ALIASES, TARGET_PATTERN)


def valid_assembly_accession(row: dict[str, str]) -> str | None:
    return valid_accession(row, ASSEMBLY_ALIASES, ASSEMBLY_PATTERN)


def valid_sra_accessions(row: dict[str, str]) -> str | None:
    accessions = SRA_SPLIT_PATTERN.split(first_value(row, SRA_ALIASES))
    if not any(accessions):
        return ""
    normalized = []
    for accession in accessions:
        if not accession:
            continue
        if SRA_ACCESSION_PATTERN.match(accession) is None:
            return None
        normalized.append(accession)
    return "|".join(sorted(set(normalized)))


def has_invalid_target_accession(row: dict[str, str]) -> bool:
    return valid_target_accession(row) is None


def has_invalid_assembly_accession(row: dict[str, str]) -> bool:
    return valid_assembly_accession(row) is None


def has_invalid_sra_accessions(row: dict[str, str]) -> bool:
    return valid_sra_accessions(row) is None


def has_assay_method(row: dict[str, str]) -> bool:
    return has_value(row, PLATFORM_ALIASES) or has_value(row, REAGENT_ALIASES)


def standardized_measurement(
    row: dict[str, str],
    aliases: Iterable[str],
    units: str,
) -> tuple[str, str, str] | None:
    raw_value = first_value(row, aliases)
    if not raw_value:
        return "", "", ""

    match = MEASUREMENT_PATTERN.match(raw_value.strip())
    if match is None:
        return None
    value = Decimal(match.group("value"))
    if value <= 0:
        return None

    value_qualifier = match.group("qualifier") or ""
    sign_qualifier = first_value(row, MEASUREMENT_SIGN_ALIASES)
    if sign_qualifier not in MEASUREMENT_SIGNS:
        return None
    if value_qualifier and sign_qualifier and value_qualifier != sign_qualifier:
        return None
    qualifier = sign_qualifier or value_qualifier
    if qualifier == "=":
        qualifier = ""
    return format(value.normalize(), "f"), qualifier, units


def measurement_label(measurement: tuple[str, str, str]) -> str:
    value, qualifier, units = measurement
    return f"{qualifier}{value} {units}"


def standardized_activity_measurements(
    row: dict[str, str],
) -> tuple[tuple[str, str, str], tuple[str, str, str]] | None:
    mic = standardized_measurement(row, MIC_ALIASES, MIC_UNITS)
    disk = standardized_measurement(row, DISK_ALIASES, DISK_DIFFUSION_UNITS)
    if mic is None or disk is None:
        return None
    if not mic[0] and not disk[0]:
        return None
    return mic, disk


def standardized_activity_call(row: dict[str, str]) -> tuple[str, str] | None:
    phenotype = first_value(row, PHENOTYPE_ALIASES)
    if not phenotype:
        return "", ""
    activity = ACTIVITY_CALLS.get(phenotype.casefold())
    if activity is None:
        return None
    return phenotype, activity


def has_invalid_phenotype(row: dict[str, str]) -> bool:
    return standardized_activity_call(row) is None


def activity_group_id(row: dict[str, str]) -> str:
    digest = hashlib.sha256()
    digest.update(ACTIVITY_GROUP_ID_VERSION.encode("utf-8"))
    digest.update(b"\0")
    for column in ACTIVITY_REPORT_GROUP_COLUMNS:
        digest.update(row[column].encode("utf-8"))
        digest.update(b"\0")
    return f"ncbi_ast:{digest.hexdigest()[:16]}"


def validate_table_header(path: Path, fieldnames: list[str] | None) -> None:
    """Reject malformed headers before DictReader can drop duplicate columns."""
    if not fieldnames:
        raise ValueError(f"{path}: missing header")

    seen = {}
    for index, field in enumerate(fieldnames, start=1):
        if not field:
            raise ValueError(f"{path}: header column {index} is empty")
        normalized = normalize_header(field)
        if not normalized:
            raise ValueError(f"{path}: header column {index} normalizes to empty")
        if normalized in seen:
            raise ValueError(
                f"{path}: duplicate header {field!r} "
                f"normalizes to {normalized!r}; already saw {seen[normalized]!r}"
            )
        seen[normalized] = field


def require_exact_table_row(row: dict, path: Path, line_number: int) -> None:
    """Reject rows whose cells do not match an already-validated header."""
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


def strip_table_row(row: dict[str, str]) -> dict[str, str]:
    return {field: value.strip() for field, value in row.items()}


def strip_curated_tsv_row(
    row: dict[str, str],
    path: Path,
    line_number: int,
) -> dict[str, str]:
    for field, value in row.items():
        if any(char in value for char in CURATED_TSV_CONTROL_CHARS):
            raise ValueError(f"{path}:{line_number}: {field} contains a tab or newline")
    return strip_table_row(row)


def read_table(path: Path) -> list[dict[str, str]]:
    sample = path.read_text(encoding="utf-8", errors="replace")[:4096]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t")
    except csv.Error:
        dialect = csv.excel_tab if path.suffix.lower() in {".tsv", ".tab"} else csv.excel

    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        reader = csv.DictReader(handle, dialect=dialect)
        validate_table_header(path, reader.fieldnames)
        rows = []
        for row in reader:
            require_exact_table_row(row, path, reader.line_num)
            rows.append(row)
        return rows


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


def read_drug_map(path: Path, structure_keys: dict[str, str]) -> dict[str, dict[str, str]]:
    """Read a partial NCBI antibiotic-value crosswalk and validate exact rows."""

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != DRUG_MAP_COLUMNS:
            raise ValueError(f"unexpected NCBI AST drug map columns: {reader.fieldnames}")

        rows = {}
        for line_number, row in enumerate(reader, start=2):
            require_exact_table_row(row, path, line_number)
            row = strip_curated_tsv_row(row, path, line_number)
            require_non_blank_fields(
                row,
                (
                    "source_record_id",
                    "source_name",
                    "mapping_status",
                    "mapping_basis",
                    "notes",
                ),
                path,
                line_number,
            )

            normalized_name = normalize(row["source_name"])
            if row["source_record_id"] != normalized_name:
                raise ValueError(
                    f"{row['source_name']}: source_record_id "
                    f"{row['source_record_id']!r} != normalized source_name {normalized_name!r}"
                )
            if normalized_name in rows:
                raise ValueError(f"duplicate NCBI AST antibiotic mapping: {normalized_name}")
            if row["mapping_status"] not in MAPPING_STATUSES:
                raise ValueError(
                    f"{row['source_name']}: unknown mapping_status {row['mapping_status']!r}"
                )

            has_mapping = bool(row["identifier"] or row["standard_inchi_key"])
            if row["mapping_status"] != EXACT_MAPPING_STATUS:
                if has_mapping:
                    raise ValueError(
                        f"{row['source_name']}: non-EXACT mapping must not carry structure fields"
                    )
                rows[normalized_name] = row
                continue

            identifier = row["identifier"]
            if not identifier or not row["standard_inchi_key"]:
                raise ValueError(
                    f"{row['source_name']}: EXACT mapping needs identifier and standard_inchi_key"
                )
            expected = structure_keys.get(identifier)
            if expected is None:
                raise ValueError(
                    f"{row['source_name']}: mapped identifier {identifier} is not in the corpus"
                )
            if row["standard_inchi_key"] != expected:
                raise ValueError(
                    f"{row['source_name']}: mapped InChIKey {row['standard_inchi_key']} "
                    f"does not match {identifier} ({expected})"
                )
            rows[normalized_name] = row
        return rows


def read_project_dedupe_map(path: Path) -> dict[tuple[str, str], dict[str, str]]:
    """Read curated source-context exclusions used before seeding NCBI AST rows."""

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != PROJECT_DEDUPE_COLUMNS:
            raise ValueError(f"unexpected NCBI AST project dedupe columns: {reader.fieldnames}")

        rows = {}
        for line_number, row in enumerate(reader, start=2):
            require_exact_table_row(row, path, line_number)
            row = strip_curated_tsv_row(row, path, line_number)
            accession_type = row["accession_type"]
            accession = row["accession"]
            if accession_type not in PROJECT_DEDUPE_ACCESSIONS:
                raise ValueError(f"{accession}: unsupported accession_type {accession_type!r}")

            _, pattern = PROJECT_DEDUPE_ACCESSIONS[accession_type]
            if pattern.match(accession) is None:
                raise ValueError(f"{accession}: invalid {accession_type} accession")
            require_non_blank_fields(
                row,
                ("source", "source_version", "notes"),
                path,
                line_number,
            )
            if normalize(row["source"]) == normalize(PROJECT_DEDUPE_SELF_SOURCE):
                raise ValueError(
                    f"{accession}: project dedupe source cannot be {PROJECT_DEDUPE_SELF_SOURCE}"
                )

            key = (accession_type, accession)
            if key in rows:
                raise ValueError(f"duplicate NCBI AST project dedupe key: {key}")
            rows[key] = row
        return rows


def project_dedupe_hit(
    row: dict[str, str],
    project_dedupe: dict[tuple[str, str], dict[str, str]],
) -> dict[str, str] | None:
    for accession_type, (aliases, _) in PROJECT_DEDUPE_ACCESSIONS.items():
        accession = first_value(row, aliases)
        if not accession:
            continue
        hit = project_dedupe.get((accession_type, accession))
        if hit is not None:
            return hit
    return None


def activity_report_context(
    row: dict[str, str],
    project_dedupe: dict[tuple[str, str], dict[str, str]],
) -> dict[str, str] | None:
    """Return the mapping-independent grouped activity fields a row can support."""

    measurements = standardized_activity_measurements(row)
    if measurements is None:
        return None
    activity_call = standardized_activity_call(row)
    if activity_call is None:
        return None

    taxon_label = first_value(row, TAXON_ALIASES)
    biosample_accession = first_value(row, BIOSAMPLE_ALIASES)
    bioproject_accession = first_value(row, BIOPROJECT_ALIASES)
    if not taxon_label or not has_valid_project_context(row):
        return None
    if not has_assay_method(row):
        return None

    target_accession = valid_target_accession(row)
    if target_accession is None:
        return None
    assembly_accession = valid_assembly_accession(row)
    if assembly_accession is None:
        return None
    sra_accessions = valid_sra_accessions(row)
    if sra_accessions is None:
        return None
    if project_dedupe_hit(row, project_dedupe):
        return None

    mic, disk = measurements
    phenotype, activity = activity_call
    return {
        "taxon_label": taxon_label,
        "biosample_accession": biosample_accession,
        "bioproject_accession": bioproject_accession,
        "target_accession": target_accession,
        "assembly_accession": assembly_accession,
        "sra_accessions": sra_accessions,
        "phenotype": phenotype,
        "activity": activity,
        "mic_value": mic[0],
        "mic_qualifier": mic[1],
        "mic_units": mic[2],
        "disk_diffusion_value": disk[0],
        "disk_diffusion_qualifier": disk[1],
        "disk_diffusion_units": disk[2],
        "platform": first_value(row, PLATFORM_ALIASES),
        "vendor": first_value(row, VENDOR_ALIASES),
        "reagent": first_value(row, REAGENT_ALIASES),
        "standard": first_value(row, STANDARD_ALIASES),
    }


def project_dedupe_report_rows(
    rows: list[dict[str, str]],
    mappings: dict[str, dict[str, str]] | None = None,
    project_dedupe: dict[tuple[str, str], dict[str, str]] | None = None,
) -> list[dict]:
    """Return valid BioSample/BioProject accessions worth dedupe curation."""

    mappings = mappings or {}
    project_dedupe = project_dedupe or {}
    contexts: dict[tuple[str, str], dict[str, int | str]] = {}
    biosample_accessions: dict[tuple[str, str], set[str]] = defaultdict(set)
    bioproject_accessions: dict[tuple[str, str], set[str]] = defaultdict(set)
    antibiotics: dict[tuple[str, str], set[str]] = defaultdict(set)
    exact_mapped_antibiotics: dict[tuple[str, str], set[str]] = defaultdict(set)
    exact_mapped_identifiers: dict[tuple[str, str], set[str]] = defaultdict(set)
    taxon_labels: dict[tuple[str, str], set[str]] = defaultdict(set)

    for row in rows:
        if not has_valid_project_context(row):
            continue

        source_name = first_value(row, ANTIBIOTIC_ALIASES)
        if not source_name:
            continue
        if activity_report_context(row, project_dedupe) is None:
            continue
        biosample_accession = first_value(row, BIOSAMPLE_ALIASES)
        bioproject_accession = first_value(row, BIOPROJECT_ALIASES)
        normalized_antibiotic = normalize(source_name)
        mapping = mappings.get(normalized_antibiotic, {})
        exact_mapped = mapping.get("mapping_status") == EXACT_MAPPING_STATUS
        taxon_label = first_value(row, TAXON_ALIASES)

        for accession_type, (aliases, pattern) in PROJECT_DEDUPE_ACCESSIONS.items():
            accession = first_value(row, aliases)
            if pattern.match(accession) is None:
                continue
            key = (accession_type, accession)
            if key not in contexts:
                contexts[key] = {
                    "accession_type": accession_type,
                    "accession": accession,
                    "ast_rows": 0,
                    "exact_mapped_rows": 0,
                }
            contexts[key]["ast_rows"] += 1
            contexts[key]["exact_mapped_rows"] += int(exact_mapped)
            biosample_accessions[key].add(biosample_accession)
            bioproject_accessions[key].add(bioproject_accession)
            if normalized_antibiotic:
                antibiotics[key].add(normalized_antibiotic)
            if exact_mapped:
                exact_mapped_antibiotics[key].add(normalized_antibiotic)
                exact_mapped_identifiers[key].add(mapping["identifier"])
            if taxon_label:
                taxon_labels[key].add(taxon_label)

    report_rows = []
    for key, row in contexts.items():
        row["exact_mapped_antibiotic_values"] = len(exact_mapped_antibiotics[key])
        row["exact_mapped_antibiotics"] = "|".join(
            sorted(exact_mapped_antibiotics[key])
        )
        row["exact_mapped_identifiers"] = "|".join(
            sorted(exact_mapped_identifiers[key])
        )
        row["biosample_count"] = len(biosample_accessions[key])
        row["bioproject_count"] = len(bioproject_accessions[key])
        row["antibiotic_values"] = len(antibiotics[key])
        row["antibiotics"] = "|".join(sorted(antibiotics[key]))
        row["taxon_labels"] = "|".join(sorted(taxon_labels[key]))
        report_rows.append(row)
    return sorted(
        report_rows,
        key=lambda row: (
            -row["exact_mapped_rows"],
            -row["ast_rows"],
            row["accession_type"],
            row["accession"],
        ),
    )


def exact_activity_rows(
    rows: list[dict[str, str]],
    mappings: dict[str, dict[str, str]],
    *,
    source_version: str,
    source_retrieved_on: str,
    project_dedupe: dict[tuple[str, str], dict[str, str]] | None = None,
) -> list[dict[str, str]]:
    """Return grouped, dedupe-ready exact AST measurements without seeding claims."""

    project_dedupe = project_dedupe or {}
    grouped: dict[tuple[str, ...], dict[str, str]] = {}
    counts: Counter[tuple[str, ...]] = Counter()
    isolates: dict[tuple[str, ...], set[str]] = defaultdict(set)
    for row in rows:
        source_name = first_value(row, ANTIBIOTIC_ALIASES)
        mapping = mappings.get(normalize(source_name))
        if not mapping or mapping.get("mapping_status") != EXACT_MAPPING_STATUS:
            continue

        context = activity_report_context(row, project_dedupe)
        if context is None:
            continue

        out = {
            "source_name": mapping["source_name"],
            "normalized_antibiotic": normalize(source_name),
            "identifier": mapping["identifier"],
            "standard_inchi_key": mapping["standard_inchi_key"],
            **context,
        }
        group_key = tuple(out[column] for column in ACTIVITY_REPORT_GROUP_COLUMNS)
        grouped[group_key] = out
        counts[group_key] += 1
        isolates[group_key].add(context["biosample_accession"])

    activity_rows = []
    for group_key, row in grouped.items():
        activity_rows.append({
            "activity_group_id": activity_group_id(row),
            "source_version": source_version,
            "source_retrieved_on": source_retrieved_on,
            "ast_row_count": counts[group_key],
            "isolate_count": len(isolates[group_key]),
            **row,
        })
    return sorted(
        activity_rows,
        key=lambda row: (
            -row["ast_row_count"],
            row["identifier"],
            row["source_name"].casefold(),
            row["taxon_label"].casefold(),
            row["phenotype"],
            row["activity_group_id"],
        ),
    )


def evaluate_rows(
    rows: list[dict[str, str]],
    candidates: dict[str, set[str]],
    structure_keys: dict[str, str],
    mappings: dict[str, dict[str, str]] | None = None,
    project_dedupe: dict[tuple[str, str], dict[str, str]] | None = None,
) -> dict:
    mappings = mappings or {}
    project_dedupe = project_dedupe or {}
    rows_by_antibiotic: dict[str, list[dict[str, str]]] = defaultdict(list)
    names_by_antibiotic: dict[str, set[str]] = defaultdict(set)
    rows_without_antibiotic = 0
    rows_with_biosample = 0
    rows_with_bioproject = 0
    rows_with_project_context = 0
    rows_with_valid_project_context = 0
    rows_with_target_acc = 0
    rows_with_assembly_acc = 0
    rows_with_sra_accessions = 0
    rows_with_invalid_target_acc = 0
    rows_with_invalid_assembly_acc = 0
    rows_with_invalid_sra_accessions = 0
    rows_with_taxon = 0
    rows_with_phenotype = 0
    rows_with_invalid_phenotype = 0
    rows_with_assay_method = 0
    rows_with_dedupe_context = 0

    for row in rows:
        antibiotic = first_value(row, ANTIBIOTIC_ALIASES)
        if not antibiotic:
            rows_without_antibiotic += 1
            continue
        normalized = normalize(antibiotic)
        rows_by_antibiotic[normalized].append(row)
        names_by_antibiotic[normalized].add(antibiotic)
        rows_with_biosample += int(has_value(row, BIOSAMPLE_ALIASES))
        rows_with_bioproject += int(has_value(row, BIOPROJECT_ALIASES))
        rows_with_project_context += int(has_project_context(row))
        rows_with_valid_project_context += int(has_valid_project_context(row))
        rows_with_target_acc += int(has_value(row, TARGET_ALIASES))
        rows_with_assembly_acc += int(has_value(row, ASSEMBLY_ALIASES))
        rows_with_sra_accessions += int(has_value(row, SRA_ALIASES))
        rows_with_invalid_target_acc += int(has_invalid_target_accession(row))
        rows_with_invalid_assembly_acc += int(has_invalid_assembly_accession(row))
        rows_with_invalid_sra_accessions += int(has_invalid_sra_accessions(row))
        rows_with_taxon += int(has_value(row, TAXON_ALIASES))
        rows_with_phenotype += int(has_value(row, PHENOTYPE_ALIASES))
        rows_with_invalid_phenotype += int(has_invalid_phenotype(row))
        rows_with_assay_method += int(has_assay_method(row))
        rows_with_dedupe_context += int(project_dedupe_hit(row, project_dedupe) is not None)

    antibiotic_rows = []
    exact_name_matched_rows = 0
    ambiguous_name_rows = 0
    unmatched_rows = 0
    exact_mapped_rows = 0
    exact_mapped_activity_report_candidate_rows = 0
    non_exact_mapped_rows = 0
    unmapped_rows = 0
    for normalized, antibiotic_ast_rows in sorted(
        rows_by_antibiotic.items(),
        key=lambda item: (-len(item[1]), item[0]),
    ):
        antibiotic = sorted(
            names_by_antibiotic[normalized],
            key=lambda name: (name.casefold(), name),
        )[0]
        identifiers = sorted(candidates.get(normalized, set()))
        mapping = mappings.get(normalized, {})
        row_count = len(antibiotic_ast_rows)
        activity_report_candidate_count = sum(
            activity_report_context(row, project_dedupe) is not None
            for row in antibiotic_ast_rows
        )
        if len(identifiers) == 1:
            exact_name_matched_rows += row_count
        elif len(identifiers) > 1:
            ambiguous_name_rows += row_count
        else:
            unmatched_rows += row_count
        if mapping.get("mapping_status") == EXACT_MAPPING_STATUS:
            exact_mapped_rows += row_count
            exact_mapped_activity_report_candidate_rows += activity_report_candidate_count
        elif mapping.get("mapping_status"):
            non_exact_mapped_rows += row_count
        else:
            unmapped_rows += row_count

        mic_measurements = [
            standardized_measurement(row, MIC_ALIASES, MIC_UNITS)
            for row in antibiotic_ast_rows
        ]
        disk_measurements = [
            standardized_measurement(row, DISK_ALIASES, DISK_DIFFUSION_UNITS)
            for row in antibiotic_ast_rows
        ]
        valid_mic_measurements = [
            measurement for measurement in mic_measurements
            if measurement and measurement[0]
        ]
        valid_disk_measurements = [
            measurement for measurement in disk_measurements
            if measurement and measurement[0]
        ]

        antibiotic_rows.append(
            {
                "antibiotic": antibiotic,
                "normalized_antibiotic": normalized,
                "ast_rows": row_count,
                "mapping_status": mapping.get("mapping_status", ""),
                "identifier": mapping.get("identifier", ""),
                "standard_inchi_key": mapping.get("standard_inchi_key", ""),
                "mapping_basis": mapping.get("mapping_basis", ""),
                "mapping_notes": mapping.get("notes", ""),
                "exact_name_candidate_count": len(identifiers),
                "exact_name_candidate_identifiers": "|".join(identifiers),
                "exact_name_candidate_inchi_keys": "|".join(
                    structure_keys[identifier] for identifier in identifiers
                ),
                "biosample_count": sum(has_value(row, BIOSAMPLE_ALIASES) for row in antibiotic_ast_rows),
                "bioproject_count": sum(has_value(row, BIOPROJECT_ALIASES) for row in antibiotic_ast_rows),
                "project_context_count": sum(has_project_context(row) for row in antibiotic_ast_rows),
                "valid_project_context_count": sum(
                    has_valid_project_context(row) for row in antibiotic_ast_rows
                ),
                "dedupe_context_count": sum(
                    project_dedupe_hit(row, project_dedupe) is not None
                    for row in antibiotic_ast_rows
                ),
                "activity_report_candidate_count": activity_report_candidate_count,
                "target_acc_count": sum(has_value(row, TARGET_ALIASES) for row in antibiotic_ast_rows),
                "invalid_target_acc_count": sum(
                    has_invalid_target_accession(row) for row in antibiotic_ast_rows
                ),
                "assembly_acc_count": sum(
                    has_value(row, ASSEMBLY_ALIASES) for row in antibiotic_ast_rows
                ),
                "invalid_assembly_acc_count": sum(
                    has_invalid_assembly_accession(row) for row in antibiotic_ast_rows
                ),
                "sra_accessions_count": sum(
                    has_value(row, SRA_ALIASES) for row in antibiotic_ast_rows
                ),
                "invalid_sra_accessions_count": sum(
                    has_invalid_sra_accessions(row) for row in antibiotic_ast_rows
                ),
                "taxon_count": sum(has_value(row, TAXON_ALIASES) for row in antibiotic_ast_rows),
                "phenotype_count": sum(has_value(row, PHENOTYPE_ALIASES) for row in antibiotic_ast_rows),
                "invalid_phenotype_count": sum(
                    has_invalid_phenotype(row) for row in antibiotic_ast_rows
                ),
                "assay_method_count": sum(has_assay_method(row) for row in antibiotic_ast_rows),
                "mic_count": sum(has_value(row, MIC_ALIASES) for row in antibiotic_ast_rows),
                "standardized_mic_count": len(valid_mic_measurements),
                "invalid_mic_count": sum(measurement is None for measurement in mic_measurements),
                "standardized_mic_values": "|".join(
                    sorted({measurement_label(measurement) for measurement in valid_mic_measurements})
                ),
                "disk_diffusion_count": sum(has_value(row, DISK_ALIASES) for row in antibiotic_ast_rows),
                "standardized_disk_diffusion_count": len(valid_disk_measurements),
                "invalid_disk_diffusion_count": sum(
                    measurement is None for measurement in disk_measurements
                ),
                "standardized_disk_diffusion_values": "|".join(
                    sorted({
                        measurement_label(measurement)
                        for measurement in valid_disk_measurements
                    })
                ),
                "taxon_labels": "|".join(sorted({
                    first_value(row, TAXON_ALIASES) for row in antibiotic_ast_rows
                    if first_value(row, TAXON_ALIASES)
                })),
                "phenotypes": "|".join(sorted({
                    first_value(row, PHENOTYPE_ALIASES) for row in antibiotic_ast_rows
                    if first_value(row, PHENOTYPE_ALIASES)
                })),
            }
        )

    return {
        "total_rows": len(rows),
        "rows_without_antibiotic": rows_without_antibiotic,
        "rows_with_antibiotic": len(rows) - rows_without_antibiotic,
        "antibiotic_values": len(rows_by_antibiotic),
        "rows_with_biosample": rows_with_biosample,
        "rows_with_bioproject": rows_with_bioproject,
        "rows_with_project_context": rows_with_project_context,
        "rows_with_valid_project_context": rows_with_valid_project_context,
        "rows_with_target_acc": rows_with_target_acc,
        "rows_with_assembly_acc": rows_with_assembly_acc,
        "rows_with_sra_accessions": rows_with_sra_accessions,
        "rows_with_invalid_target_acc": rows_with_invalid_target_acc,
        "rows_with_invalid_assembly_acc": rows_with_invalid_assembly_acc,
        "rows_with_invalid_sra_accessions": rows_with_invalid_sra_accessions,
        "rows_with_taxon": rows_with_taxon,
        "rows_with_phenotype": rows_with_phenotype,
        "rows_with_invalid_phenotype": rows_with_invalid_phenotype,
        "rows_with_assay_method": rows_with_assay_method,
        "rows_with_dedupe_context": rows_with_dedupe_context,
        "exact_name_matched_antibiotics": sum(
            row["exact_name_candidate_count"] == 1 for row in antibiotic_rows
        ),
        "ambiguous_name_antibiotics": sum(row["exact_name_candidate_count"] > 1 for row in antibiotic_rows),
        "unmatched_antibiotics": sum(row["exact_name_candidate_count"] == 0 for row in antibiotic_rows),
        "exact_name_matched_rows": exact_name_matched_rows,
        "ambiguous_name_rows": ambiguous_name_rows,
        "unmatched_rows": unmatched_rows,
        "exact_mapped_antibiotics": sum(
            row["mapping_status"] == EXACT_MAPPING_STATUS for row in antibiotic_rows
        ),
        "exact_mapped_activity_report_candidate_rows": (
            exact_mapped_activity_report_candidate_rows
        ),
        "non_exact_mapped_antibiotics": sum(
            bool(row["mapping_status"]) and row["mapping_status"] != EXACT_MAPPING_STATUS
            for row in antibiotic_rows
        ),
        "unmapped_antibiotics": sum(not row["mapping_status"] for row in antibiotic_rows),
        "exact_mapped_rows": exact_mapped_rows,
        "non_exact_mapped_rows": non_exact_mapped_rows,
        "unmapped_rows": unmapped_rows,
        "antibiotic_rows": antibiotic_rows,
    }


def write_antibiotic_report(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "antibiotic",
        "normalized_antibiotic",
        "ast_rows",
        "mapping_status",
        "identifier",
        "standard_inchi_key",
        "mapping_basis",
        "mapping_notes",
        "exact_name_candidate_count",
        "exact_name_candidate_identifiers",
        "exact_name_candidate_inchi_keys",
        "biosample_count",
        "bioproject_count",
        "project_context_count",
        "valid_project_context_count",
        "dedupe_context_count",
        "activity_report_candidate_count",
        "target_acc_count",
        "invalid_target_acc_count",
        "assembly_acc_count",
        "invalid_assembly_acc_count",
        "sra_accessions_count",
        "invalid_sra_accessions_count",
        "taxon_count",
        "phenotype_count",
        "invalid_phenotype_count",
        "assay_method_count",
        "mic_count",
        "standardized_mic_count",
        "invalid_mic_count",
        "standardized_mic_values",
        "disk_diffusion_count",
        "standardized_disk_diffusion_count",
        "invalid_disk_diffusion_count",
        "standardized_disk_diffusion_values",
        "taxon_labels",
        "phenotypes",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_drug_map_template(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=DRUG_MAP_COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({
                "source_record_id": row["normalized_antibiotic"],
                "source_name": row["antibiotic"],
                "mapping_status": row["mapping_status"],
                "identifier": row["identifier"],
                "standard_inchi_key": row["standard_inchi_key"],
                "mapping_basis": row["mapping_basis"],
                "notes": row["mapping_notes"],
            })


def write_project_dedupe_report(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=PROJECT_DEDUPE_REPORT_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_activity_report(rows: list[dict], path: Path) -> None:
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


def is_iso_date(value: str) -> bool:
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        return False
    return parsed.isoformat() == value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ast", type=Path, required=True, help="NCBI AST Browser CSV/TSV export.")
    parser.add_argument(
        "--antibiotic-report",
        type=Path,
        help="Optional TSV summarizing each submitted antibiotic value.",
    )
    parser.add_argument(
        "--activity-report",
        type=Path,
        help=(
            "Optional TSV of grouped exact-mapped AST rows with valid MIC or disk "
            "measurements and BioSample/BioProject context; requires --drug-map."
        ),
    )
    parser.add_argument(
        "--source-version",
        default="",
        help=(
            "Optional AST export or BigQuery snapshot version to stamp on "
            "--activity-report rows."
        ),
    )
    parser.add_argument(
        "--source-retrieved-on",
        default="",
        help=(
            "Optional ISO retrieval date for the AST export to stamp on "
            "--activity-report rows."
        ),
    )
    parser.add_argument(
        "--drug-map-template",
        type=Path,
        help="Optional fillable TSV crosswalk for every submitted antibiotic string.",
    )
    parser.add_argument(
        "--drug-map",
        type=Path,
        help="Optional partial curated crosswalk from submitted antibiotic strings to exact structures.",
    )
    parser.add_argument(
        "--project-dedupe-map",
        type=Path,
        help=(
            "Optional TSV of BioSample/BioProject accessions already represented "
            "by another source; matching rows are counted and excluded from "
            "--activity-report."
        ),
    )
    parser.add_argument(
        "--project-dedupe-report",
        type=Path,
        help=(
            "Optional TSV ranking valid BioSample/BioProject accessions for "
            "curating --project-dedupe-map exclusions."
        ),
    )
    args = parser.parse_args()
    if args.activity_report and not args.drug_map:
        parser.error("--activity-report requires --drug-map with exact curated mappings.")
    if args.activity_report and not args.source_version.strip():
        parser.error("--activity-report requires --source-version.")
    if args.source_version != args.source_version.strip():
        parser.error("--source-version must not have leading or trailing whitespace.")
    if args.activity_report and not args.source_retrieved_on:
        parser.error("--activity-report requires --source-retrieved-on.")
    if args.source_retrieved_on and not is_iso_date(args.source_retrieved_on):
        parser.error("--source-retrieved-on must be an ISO date.")

    rows = read_table(args.ast)
    candidates, structure_keys = corpus_name_candidates()
    mappings = read_drug_map(args.drug_map, structure_keys) if args.drug_map else {}
    project_dedupe = (
        read_project_dedupe_map(args.project_dedupe_map)
        if args.project_dedupe_map
        else {}
    )
    result = evaluate_rows(
        rows,
        candidates,
        structure_keys,
        mappings=mappings,
        project_dedupe=project_dedupe,
    )

    if args.antibiotic_report:
        write_antibiotic_report(result["antibiotic_rows"], args.antibiotic_report)
    if args.drug_map_template:
        write_drug_map_template(result["antibiotic_rows"], args.drug_map_template)
    if args.project_dedupe_report:
        write_project_dedupe_report(
            project_dedupe_report_rows(rows, mappings, project_dedupe),
            args.project_dedupe_report,
        )
    activity_rows = (
        exact_activity_rows(
            rows,
            mappings,
            source_version=args.source_version,
            source_retrieved_on=args.source_retrieved_on,
            project_dedupe=project_dedupe,
        )
        if args.activity_report
        else []
    )
    if args.activity_report:
        write_activity_report(activity_rows, args.activity_report)

    leading = Counter({
        row["antibiotic"]: row["ast_rows"]
        for row in result["antibiotic_rows"]
    }).most_common(10)

    print("NCBI Pathogen Detection AST audit")
    print(
        f"  rows={result['total_rows']} rows_with_antibiotic={result['rows_with_antibiotic']} "
        f"antibiotic_values={result['antibiotic_values']}"
    )
    print(
        f"  identifiers: biosample_rows={result['rows_with_biosample']} "
        f"bioproject_rows={result['rows_with_bioproject']} "
        f"project_context_rows={result['rows_with_project_context']} "
        f"valid_project_context_rows={result['rows_with_valid_project_context']} "
        f"target_acc_rows={result['rows_with_target_acc']} "
        f"assembly_acc_rows={result['rows_with_assembly_acc']} "
        f"sra_accession_rows={result['rows_with_sra_accessions']}"
    )
    print(
        f"  invalid identifiers: target_acc_rows="
        f"{result['rows_with_invalid_target_acc']} "
        f"assembly_acc_rows={result['rows_with_invalid_assembly_acc']} "
        f"sra_accession_rows={result['rows_with_invalid_sra_accessions']}"
    )
    print(
        f"  context: taxon_rows={result['rows_with_taxon']} "
        f"phenotype_rows={result['rows_with_phenotype']} "
        f"invalid_phenotype_rows={result['rows_with_invalid_phenotype']} "
        f"assay_method_rows={result['rows_with_assay_method']}"
    )
    print(f"  dedupe: source_context_rows={result['rows_with_dedupe_context']}")
    print(
        f"  lexical exact-name candidates: antibiotics={result['exact_name_matched_antibiotics']} "
        f"rows={result['exact_name_matched_rows']}"
    )
    print(
        f"  curated exact mappings: antibiotics={result['exact_mapped_antibiotics']} "
        f"rows={result['exact_mapped_rows']} "
        f"activity_report_candidate_rows="
        f"{result['exact_mapped_activity_report_candidate_rows']}"
    )
    print(
        f"  ambiguous names: antibiotics={result['ambiguous_name_antibiotics']} "
        f"rows={result['ambiguous_name_rows']}"
    )
    print(
        f"  unmatched names: antibiotics={result['unmatched_antibiotics']} "
        f"rows={result['unmatched_rows']}"
    )
    print("  leading antibiotics: " + ", ".join(f"{name}={count}" for name, count in leading))
    if args.antibiotic_report:
        print(f"  antibiotic_report={args.antibiotic_report}")
    if args.drug_map_template:
        print(f"  drug_map_template={args.drug_map_template}")
    if args.project_dedupe_report:
        print(f"  project_dedupe_report={args.project_dedupe_report}")
    if args.activity_report:
        print(
            f"  exact_mapped_activity_groups={len(activity_rows)} "
            f"activity_report={args.activity_report}"
        )
    print("--audit: no rows seeded; submitted antibiotic names are not exact structure identifiers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
