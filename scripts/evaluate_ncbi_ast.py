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
from decimal import Decimal, InvalidOperation
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
STANDARD_INCHI_KEY_PATTERN = re.compile(r"^[A-Z]{14}-[A-Z]{10}-[A-Z]$")

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
DRUG_MAP_TEMPLATE_INPUT_COLUMNS = [
    "antibiotic",
    "normalized_antibiotic",
    "mapping_status",
    "identifier",
    "standard_inchi_key",
    "mapping_basis",
    "mapping_notes",
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
    "taxon_ids",
    "taxon_labels",
]
PROJECT_DEDUPE_MAP_TEMPLATE_INPUT_COLUMNS = [
    "accession_type",
    "accession",
]
ANTIBIOTIC_REPORT_COLUMNS = [
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
    "activity_report_dedupe_excluded_count",
    "target_acc_count",
    "invalid_target_acc_count",
    "assembly_acc_count",
    "invalid_assembly_acc_count",
    "sra_accessions_count",
    "invalid_sra_accessions_count",
    "isolation_type_count",
    "location_count",
    "collection_date_count",
    "create_date_count",
    "invalid_create_date_count",
    "host_count",
    "isolation_source_count",
    "taxon_id_count",
    "invalid_taxon_id_count",
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
    "taxon_ids",
    "taxon_labels",
    "phenotypes",
]
# Bump with ACTIVITY_REPORT_GROUP_COLUMNS because those columns define the
# stable activity_group_id digest for committed exact reports.
ACTIVITY_GROUP_ID_VERSION = "ncbi_ast_activity_group_v7"
ACTIVITY_REPORT_GROUP_COLUMNS = [
    "source_name",
    "normalized_antibiotic",
    "identifier",
    "standard_inchi_key",
    "taxon_id",
    "taxon_label",
    "strain",
    "biosample_accession",
    "bioproject_accession",
    "target_accession",
    "assembly_accession",
    "sra_accessions",
    "isolation_type",
    "location",
    "collection_date",
    "create_date",
    "host",
    "isolation_source",
    "phenotype",
    "activity",
    "mic_value",
    "mic_qualifier",
    "mic_units",
    "disk_diffusion_value",
    "disk_diffusion_qualifier",
    "disk_diffusion_units",
    "method",
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
REQUIRED_ACTIVITY_REPORT_COLUMNS = (
    "activity_group_id",
    "source_version",
    "source_retrieved_on",
    "ast_row_count",
    "isolate_count",
    "source_name",
    "normalized_antibiotic",
    "identifier",
    "standard_inchi_key",
    "taxon_label",
    "biosample_accession",
    "bioproject_accession",
)
EXACT_MAPPING_STATUS = "EXACT"
PROJECT_DEDUPE_SELF_SOURCE = "NCBI_AST"
PROJECT_DEDUPE_SOURCE_INVENTORIES = {
    "CRYPTIC": REPO_ROOT / "data" / "raw" / "cryptic_activity.tsv",
}
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
STRAIN_ALIASES = ("strain",)
ISOLATION_TYPE_ALIASES = ("isolationtype", "epitype")
LOCATION_ALIASES = ("location", "geolocname")
COLLECTION_DATE_ALIASES = ("collectiondate",)
CREATE_DATE_ALIASES = ("createdate", "creationdate")
HOST_ALIASES = ("host",)
ISOLATION_SOURCE_ALIASES = ("isolationsource",)
SOURCE_CONTEXT_ALIASES = (
    ("isolation_type", ISOLATION_TYPE_ALIASES),
    ("location", LOCATION_ALIASES),
    ("collection_date", COLLECTION_DATE_ALIASES),
    ("create_date", CREATE_DATE_ALIASES),
    ("host", HOST_ALIASES),
    ("isolation_source", ISOLATION_SOURCE_ALIASES),
)
MIC_ALIASES = (
    "mic",
    "micmgl",
    "micugml",
    "micvalue",
    "minimuminhibitoryconcentration",
)
DISK_ALIASES = ("diskdiffusion", "diskdiffusionmm", "diskdiameter", "diskzone")
MEASUREMENT_SIGN_ALIASES = ("measurementsign", "sign")
METHOD_ALIASES = ("method", "laboratorytypingmethod", "labtypingmethod")
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
MEASUREMENT_SIGNS = {"", "<=", ">=", "<", ">", "=", "=="}
MEASUREMENT_QUALIFIERS = {"", "<", "<=", ">", ">="}
MIC_UNITS = "mg/L"
DISK_DIFFUSION_UNITS = "mm"
MIC_MAX_VALUE = Decimal("1024")
DISK_DIFFUSION_MIN_VALUE = Decimal("6")
DISK_DIFFUSION_MAX_VALUE = Decimal("150")
MICROGRAM_HEADER_TRANSLATION = str.maketrans({"µ": "u", "μ": "u"})
# Raw AST CSV cells can legally quote these, but exact TSV reports cannot.
SOURCE_TSV_CONTROL_TRANSLATION = str.maketrans({"\t": " ", "\r": " ", "\n": " "})
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
TAXON_ID_ALIASES = (
    "taxid",
    "taxonid",
    "taxonomyid",
    "ncbitaxid",
    "ncbitaxonid",
    "ncbitaxonomyid",
)
TAXON_ID_PATTERN = re.compile(r"^(?:NCBITaxon:)?([1-9][0-9]*)$")
ACTIVITY_REPORT_TAXON_ID_PATTERN = re.compile(r"^NCBITaxon:[1-9][0-9]*$")


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def normalize_header(value: str) -> str:
    header = value.removeprefix("AST.").removeprefix("AMR.")
    return normalize(header.translate(MICROGRAM_HEADER_TRANSLATION))


def first_value(row: dict[str, str], aliases: Iterable[str]) -> str:
    for alias in aliases:
        for key, value in row.items():
            if key is None:
                continue
            if value is None:
                continue
            cleaned = value.translate(SOURCE_TSV_CONTROL_TRANSLATION).strip()
            if normalize_header(key) == alias and cleaned:
                return cleaned
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


def is_iso_date(value: str) -> bool:
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        return False
    return parsed.isoformat() == value


def valid_create_date(row: dict[str, str]) -> str | None:
    create_date = first_value(row, CREATE_DATE_ALIASES)
    if not create_date:
        return ""
    if not is_iso_date(create_date):
        return None
    return create_date


def valid_taxon_id(row: dict[str, str]) -> str | None:
    taxon_id = first_value(row, TAXON_ID_ALIASES)
    if not taxon_id:
        return ""
    match = TAXON_ID_PATTERN.match(taxon_id)
    if match is None:
        return None
    return f"NCBITaxon:{match.group(1)}"


def has_invalid_target_accession(row: dict[str, str]) -> bool:
    return valid_target_accession(row) is None


def has_invalid_assembly_accession(row: dict[str, str]) -> bool:
    return valid_assembly_accession(row) is None


def has_invalid_sra_accessions(row: dict[str, str]) -> bool:
    return valid_sra_accessions(row) is None


def has_invalid_taxon_id(row: dict[str, str]) -> bool:
    return valid_taxon_id(row) is None


def has_invalid_create_date(row: dict[str, str]) -> bool:
    return valid_create_date(row) is None


def has_assay_method(row: dict[str, str]) -> bool:
    return (
        has_value(row, METHOD_ALIASES)
        or has_value(row, PLATFORM_ALIASES)
        or has_value(row, REAGENT_ALIASES)
    )


def standardized_measurement(
    row: dict[str, str],
    aliases: Iterable[str],
    units: str,
    *,
    minimum: Decimal | None = None,
    maximum: Decimal | None = None,
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
    if minimum is not None and value < minimum:
        return None
    if maximum is not None and value > maximum:
        return None

    value_qualifier = match.group("qualifier") or ""
    sign_qualifier = first_value(row, MEASUREMENT_SIGN_ALIASES)
    if sign_qualifier not in MEASUREMENT_SIGNS:
        return None
    value_comparator = "=" if value_qualifier == "=" else value_qualifier
    sign_comparator = "=" if sign_qualifier in {"=", "=="} else sign_qualifier
    if value_comparator and sign_comparator and value_comparator != sign_comparator:
        return None
    qualifier = sign_qualifier or value_qualifier
    if qualifier in {"=", "=="}:
        qualifier = ""
    return format(value.normalize(), "f"), qualifier, units


def measurement_label(measurement: tuple[str, str, str]) -> str:
    value, qualifier, units = measurement
    return f"{qualifier}{value} {units}"


def standardized_activity_measurements(
    row: dict[str, str],
) -> tuple[tuple[str, str, str], tuple[str, str, str]] | None:
    mic = standardized_measurement(
        row,
        MIC_ALIASES,
        MIC_UNITS,
        maximum=MIC_MAX_VALUE,
    )
    disk = standardized_measurement(
        row,
        DISK_ALIASES,
        DISK_DIFFUSION_UNITS,
        minimum=DISK_DIFFUSION_MIN_VALUE,
        maximum=DISK_DIFFUSION_MAX_VALUE,
    )
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


def require_output_columns(
    row: dict,
    fieldnames: list[str],
    path: Path,
    row_number: int,
) -> None:
    missing = [field for field in fieldnames if field not in row]
    if missing:
        columns = ", ".join(missing)
        raise ValueError(f"{path}: output row {row_number} is missing columns: {columns}")
    unexpected = [field for field in row if field not in fieldnames]
    if unexpected:
        columns = ", ".join(unexpected)
        raise ValueError(f"{path}: output row {row_number} has unexpected columns: {columns}")


def require_tsv_safe_value(value: object, field: str, prefix: str) -> str:
    if value is None:
        raise ValueError(f"{prefix}: {field} is missing")

    string_value = str(value)
    if any(char in string_value for char in CURATED_TSV_CONTROL_CHARS):
        raise ValueError(f"{prefix}: {field} contains a tab or newline")
    if string_value != string_value.strip():
        raise ValueError(f"{prefix}: {field} has leading or trailing whitespace")
    return string_value


def require_output_rows(rows: list[dict], fieldnames: list[str], path: Path) -> None:
    for row_number, row in enumerate(rows, start=1):
        require_output_columns(row, fieldnames, path, row_number)
        prefix = f"{path}: output row {row_number}"
        for field in fieldnames:
            require_tsv_safe_value(row[field], field, prefix)


def require_input_rows(rows: list[dict], fieldnames: list[str], path: Path) -> None:
    for row_number, row in enumerate(rows, start=1):
        missing = [field for field in fieldnames if field not in row]
        if missing:
            columns = ", ".join(missing)
            raise ValueError(
                f"{path}: template input row {row_number} "
                f"is missing columns: {columns}"
            )
        prefix = f"{path}: template input row {row_number}"
        for field in fieldnames:
            require_tsv_safe_value(row[field], field, prefix)


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


def project_dedupe_inventory_source_version(source: str, path: Path) -> str:
    """Return the single source_version represented by an adopted compact report."""

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        validate_table_header(path, reader.fieldnames)
        if "source_version" not in reader.fieldnames:
            raise ValueError(
                f"{path}: missing source_version column for {source} project dedupe"
            )

        versions = set()
        for line_number, row in enumerate(reader, start=2):
            prefix = f"{path}:{line_number}"
            if None in row:
                raise ValueError(f"{prefix}: unexpected extra delimited field")
            source_version = row["source_version"]
            if source_version is None:
                raise ValueError(f"{prefix}: source_version is missing")
            if any(char in source_version for char in CURATED_TSV_CONTROL_CHARS):
                raise ValueError(f"{prefix}: source_version contains a tab or newline")
            if source_version != source_version.strip():
                raise ValueError(
                    f"{prefix}: source_version has leading or trailing whitespace"
                )
            if not source_version:
                raise ValueError(f"{prefix}: source_version is required")
            versions.add(source_version)

    if not versions:
        raise ValueError(f"{path}: no {source} source_version values for project dedupe")
    if len(versions) > 1:
        raise ValueError(
            f"{path}: expected one {source} source_version for project dedupe, "
            f"found {', '.join(sorted(versions))}"
        )
    return next(iter(versions))


def project_dedupe_source_versions(
    source_inventories: dict[str, Path] | None = None,
) -> dict[str, str]:
    """Return supported dedupe sources and the inventory versions they own now."""

    if source_inventories is None:
        source_inventories = PROJECT_DEDUPE_SOURCE_INVENTORIES
    return {
        source: project_dedupe_inventory_source_version(source, path)
        for source, path in source_inventories.items()
    }


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
        if not rows:
            raise ValueError(f"{path}: NCBI AST table has no rows")
        return rows


def require_any_antibiotic_value(rows: list[dict[str, str]], path: Path) -> None:
    if not any(has_value(row, ANTIBIOTIC_ALIASES) for row in rows):
        raise ValueError(f"{path}: NCBI AST table has no rows with antibiotic values")


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


def read_drug_map(
    path: Path,
    structure_keys: dict[str, str],
    source_version: str,
) -> dict[str, dict[str, str]]:
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

            normalized_name = normalize(row["source_name"])
            if row["source_record_id"] != normalized_name:
                raise ValueError(
                    f"{row['source_name']}: source_record_id "
                    f"{row['source_record_id']!r} != normalized source_name {normalized_name!r}"
                )
            if normalized_name in rows:
                raise ValueError(f"duplicate NCBI AST antibiotic mapping: {normalized_name}")
            if row["source_version"] != source_version:
                raise ValueError(
                    f"{row['source_name']}: source_version {row['source_version']!r} "
                    f"!= {source_version!r}"
                )
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
        if not rows:
            raise ValueError(f"{path}: NCBI AST drug map has no rows")
        return rows


def read_project_dedupe_map(
    path: Path,
    source_versions: dict[str, str] | None = None,
) -> dict[tuple[str, str], dict[str, str]]:
    """Read curated source-context exclusions used before seeding NCBI AST rows."""

    if source_versions is None:
        source_versions = project_dedupe_source_versions()
    allowed_sources = frozenset(source_versions)
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
            if row["source"] not in allowed_sources:
                allowed = ", ".join(sorted(allowed_sources))
                raise ValueError(
                    f"{accession}: unsupported project dedupe source {row['source']!r}; "
                    f"expected one of {allowed}"
                )
            expected_source_version = source_versions[row["source"]]
            if row["source_version"] != expected_source_version:
                raise ValueError(
                    f"{accession}: {row['source']} project dedupe source_version "
                    f"{row['source_version']!r} != {expected_source_version!r}"
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

    taxon_id = valid_taxon_id(row)
    taxon_label = first_value(row, TAXON_ALIASES)
    biosample_accession = first_value(row, BIOSAMPLE_ALIASES)
    bioproject_accession = first_value(row, BIOPROJECT_ALIASES)
    if not taxon_label or not has_valid_project_context(row):
        return None
    if taxon_id is None:
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
    create_date = valid_create_date(row)
    if create_date is None:
        return None
    if project_dedupe_hit(row, project_dedupe):
        return None

    mic, disk = measurements
    phenotype, activity = activity_call
    source_context = {
        field: first_value(row, aliases)
        for field, aliases in SOURCE_CONTEXT_ALIASES
    }
    source_context["create_date"] = create_date
    return {
        "taxon_id": taxon_id,
        "taxon_label": taxon_label,
        "strain": first_value(row, STRAIN_ALIASES),
        "biosample_accession": biosample_accession,
        "bioproject_accession": bioproject_accession,
        "target_accession": target_accession,
        "assembly_accession": assembly_accession,
        "sra_accessions": sra_accessions,
        **source_context,
        "phenotype": phenotype,
        "activity": activity,
        "mic_value": mic[0],
        "mic_qualifier": mic[1],
        "mic_units": mic[2],
        "disk_diffusion_value": disk[0],
        "disk_diffusion_qualifier": disk[1],
        "disk_diffusion_units": disk[2],
        "method": first_value(row, METHOD_ALIASES),
        "platform": first_value(row, PLATFORM_ALIASES),
        "vendor": first_value(row, VENDOR_ALIASES),
        "reagent": first_value(row, REAGENT_ALIASES),
        "standard": first_value(row, STANDARD_ALIASES),
    }


def project_dedupe_excludes_activity_report(
    row: dict[str, str],
    project_dedupe: dict[tuple[str, str], dict[str, str]],
) -> bool:
    return (
        project_dedupe_hit(row, project_dedupe) is not None
        and activity_report_context(row, {}) is not None
    )


def project_dedupe_key_label(key: tuple[str, str]) -> str:
    accession_type, accession = key
    return f"{accession_type}:{accession}"


def used_project_dedupe_keys(
    rows: list[dict[str, str]],
    mappings: dict[str, dict[str, str]],
    project_dedupe: dict[tuple[str, str], dict[str, str]],
) -> set[tuple[str, str]]:
    """Return curated source-context exclusions exercised by exact AST rows."""

    used_keys = set()
    for row in rows:
        source_name = first_value(row, ANTIBIOTIC_ALIASES)
        mapping = mappings.get(normalize(source_name))
        if not mapping or mapping.get("mapping_status") != EXACT_MAPPING_STATUS:
            continue
        if activity_report_context(row, {}) is None:
            continue

        for accession_type, (aliases, _) in PROJECT_DEDUPE_ACCESSIONS.items():
            key = (accession_type, first_value(row, aliases))
            if key in project_dedupe:
                used_keys.add(key)
    return used_keys


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
    taxon_ids: dict[tuple[str, str], set[str]] = defaultdict(set)
    taxon_labels: dict[tuple[str, str], set[str]] = defaultdict(set)

    for row in rows:
        if not has_valid_project_context(row):
            continue

        source_name = first_value(row, ANTIBIOTIC_ALIASES)
        if not source_name:
            continue
        context = activity_report_context(row, project_dedupe)
        if context is None:
            continue
        biosample_accession = first_value(row, BIOSAMPLE_ALIASES)
        bioproject_accession = first_value(row, BIOPROJECT_ALIASES)
        normalized_antibiotic = normalize(source_name)
        mapping = mappings.get(normalized_antibiotic, {})
        exact_mapped = mapping.get("mapping_status") == EXACT_MAPPING_STATUS
        taxon_id = context["taxon_id"]
        taxon_label = context["taxon_label"]

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
            if taxon_id:
                taxon_ids[key].add(taxon_id)
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
        row["taxon_ids"] = "|".join(sorted(taxon_ids[key]))
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
    rows_with_taxon_id = 0
    rows_with_invalid_target_acc = 0
    rows_with_invalid_assembly_acc = 0
    rows_with_invalid_sra_accessions = 0
    rows_with_invalid_taxon_id = 0
    rows_with_taxon = 0
    rows_with_phenotype = 0
    rows_with_invalid_phenotype = 0
    rows_with_invalid_create_date = 0
    rows_with_assay_method = 0
    rows_with_dedupe_context = 0
    rows_with_source_context = Counter()

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
        rows_with_taxon_id += int(has_value(row, TAXON_ID_ALIASES))
        rows_with_invalid_target_acc += int(has_invalid_target_accession(row))
        rows_with_invalid_assembly_acc += int(has_invalid_assembly_accession(row))
        rows_with_invalid_sra_accessions += int(has_invalid_sra_accessions(row))
        rows_with_invalid_taxon_id += int(has_invalid_taxon_id(row))
        rows_with_invalid_create_date += int(has_invalid_create_date(row))
        rows_with_taxon += int(has_value(row, TAXON_ALIASES))
        rows_with_phenotype += int(has_value(row, PHENOTYPE_ALIASES))
        rows_with_invalid_phenotype += int(has_invalid_phenotype(row))
        rows_with_assay_method += int(has_assay_method(row))
        rows_with_dedupe_context += int(project_dedupe_hit(row, project_dedupe) is not None)
        for field, aliases in SOURCE_CONTEXT_ALIASES:
            rows_with_source_context[field] += int(has_value(row, aliases))

    unused_project_dedupe_keys = sorted(
        set(project_dedupe) - used_project_dedupe_keys(rows, mappings, project_dedupe),
        key=lambda key: (key[0], key[1]),
    )
    antibiotic_rows = []
    exact_name_matched_rows = 0
    ambiguous_name_rows = 0
    unmatched_rows = 0
    exact_mapped_rows = 0
    exact_mapped_activity_report_candidate_rows = 0
    exact_mapped_activity_report_dedupe_excluded_rows = 0
    non_exact_mapped_rows = 0
    unmapped_rows = 0
    unused_mapping_antibiotics = sorted(set(mappings) - set(rows_by_antibiotic))
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
        activity_report_dedupe_excluded_count = sum(
            project_dedupe_excludes_activity_report(row, project_dedupe)
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
            exact_mapped_activity_report_dedupe_excluded_rows += (
                activity_report_dedupe_excluded_count
            )
        elif mapping.get("mapping_status"):
            non_exact_mapped_rows += row_count
        else:
            unmapped_rows += row_count

        mic_measurements = [
            standardized_measurement(
                row,
                MIC_ALIASES,
                MIC_UNITS,
                maximum=MIC_MAX_VALUE,
            )
            for row in antibiotic_ast_rows
        ]
        disk_measurements = [
            standardized_measurement(
                row,
                DISK_ALIASES,
                DISK_DIFFUSION_UNITS,
                minimum=DISK_DIFFUSION_MIN_VALUE,
                maximum=DISK_DIFFUSION_MAX_VALUE,
            )
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
                "activity_report_dedupe_excluded_count": (
                    activity_report_dedupe_excluded_count
                ),
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
                **{
                    f"{field}_count": sum(
                        has_value(row, aliases) for row in antibiotic_ast_rows
                    )
                    for field, aliases in SOURCE_CONTEXT_ALIASES
                },
                "invalid_create_date_count": sum(
                    has_invalid_create_date(row) for row in antibiotic_ast_rows
                ),
                "taxon_id_count": sum(
                    has_value(row, TAXON_ID_ALIASES) for row in antibiotic_ast_rows
                ),
                "invalid_taxon_id_count": sum(
                    has_invalid_taxon_id(row) for row in antibiotic_ast_rows
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
                "taxon_ids": "|".join(sorted({
                    taxon_id for taxon_id in (
                        valid_taxon_id(row) for row in antibiotic_ast_rows
                    )
                    if taxon_id
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
        "rows_with_taxon_id": rows_with_taxon_id,
        "rows_with_invalid_target_acc": rows_with_invalid_target_acc,
        "rows_with_invalid_assembly_acc": rows_with_invalid_assembly_acc,
        "rows_with_invalid_sra_accessions": rows_with_invalid_sra_accessions,
        "rows_with_invalid_taxon_id": rows_with_invalid_taxon_id,
        "rows_with_taxon": rows_with_taxon,
        "rows_with_phenotype": rows_with_phenotype,
        "rows_with_invalid_phenotype": rows_with_invalid_phenotype,
        "rows_with_invalid_create_date": rows_with_invalid_create_date,
        "rows_with_assay_method": rows_with_assay_method,
        "rows_with_dedupe_context": rows_with_dedupe_context,
        **{
            f"rows_with_{field}": rows_with_source_context[field]
            for field, _ in SOURCE_CONTEXT_ALIASES
        },
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
        "exact_mapped_activity_report_dedupe_excluded_rows": (
            exact_mapped_activity_report_dedupe_excluded_rows
        ),
        "non_exact_mapped_antibiotics": sum(
            bool(row["mapping_status"]) and row["mapping_status"] != EXACT_MAPPING_STATUS
            for row in antibiotic_rows
        ),
        "unmapped_antibiotics": sum(not row["mapping_status"] for row in antibiotic_rows),
        "exact_mapped_rows": exact_mapped_rows,
        "non_exact_mapped_rows": non_exact_mapped_rows,
        "unmapped_rows": unmapped_rows,
        "unused_mapping_antibiotics": len(unused_mapping_antibiotics),
        "unused_mapping_antibiotic_values": "|".join(unused_mapping_antibiotics),
        "unused_project_dedupe_contexts": len(unused_project_dedupe_keys),
        "unused_project_dedupe_values": "|".join(
            project_dedupe_key_label(key) for key in unused_project_dedupe_keys
        ),
        "antibiotic_rows": antibiotic_rows,
    }


ANTIBIOTIC_REPORT_COUNT_FIELDS = tuple(
    field
    for field in ANTIBIOTIC_REPORT_COLUMNS
    if field == "ast_rows" or field.endswith("_count")
)
ANTIBIOTIC_REPORT_AST_ROW_BOUNDED_COUNT_FIELDS = tuple(
    field
    for field in ANTIBIOTIC_REPORT_COUNT_FIELDS
    if field not in {"ast_rows", "exact_name_candidate_count"}
)
ANTIBIOTIC_REPORT_COUNT_BOUNDS = (
    ("project_context_count", "biosample_count"),
    ("project_context_count", "bioproject_count"),
    ("valid_project_context_count", "project_context_count"),
    ("invalid_target_acc_count", "target_acc_count"),
    ("invalid_assembly_acc_count", "assembly_acc_count"),
    ("invalid_sra_accessions_count", "sra_accessions_count"),
    ("invalid_create_date_count", "create_date_count"),
    ("invalid_taxon_id_count", "taxon_id_count"),
    ("invalid_phenotype_count", "phenotype_count"),
)


def require_report_integer(
    row: dict[str, str],
    field: str,
    prefix: str,
    *,
    minimum: int = 0,
) -> int:
    try:
        parsed = int(row[field])
    except ValueError as error:
        raise ValueError(f"{prefix}: {field} must be an integer") from error
    if parsed < minimum:
        raise ValueError(f"{prefix}: {field} must be at least {minimum}")
    canonical = str(parsed)
    if row[field] != canonical:
        raise ValueError(f"{prefix}: {field} must use canonical integer {canonical!r}")
    return parsed


def require_antibiotic_report_rows(rows: list[dict], path: Path) -> None:
    require_output_rows(rows, ANTIBIOTIC_REPORT_COLUMNS, path)

    seen_antibiotics = set()
    for row_number, raw_row in enumerate(rows, start=1):
        prefix = f"{path}: output row {row_number}"
        row = {
            field: str(raw_row[field])
            for field in ANTIBIOTIC_REPORT_COLUMNS
        }

        normalized_antibiotic = row["normalized_antibiotic"]
        if not normalized_antibiotic:
            raise ValueError(f"{prefix}: normalized_antibiotic is required")
        if normalized_antibiotic != normalize(row["antibiotic"]):
            raise ValueError(f"{prefix}: normalized_antibiotic must match antibiotic")
        if normalized_antibiotic in seen_antibiotics:
            raise ValueError(
                f"{prefix}: duplicate NCBI AST antibiotic report row "
                f"{normalized_antibiotic!r}"
            )
        seen_antibiotics.add(normalized_antibiotic)

        mapping_status = row["mapping_status"]
        if mapping_status and mapping_status not in MAPPING_STATUSES:
            raise ValueError(
                f"{prefix}: unknown mapping_status {mapping_status!r}"
            )
        has_mapping = bool(row["identifier"] or row["standard_inchi_key"])
        if mapping_status:
            require_non_blank_fields(
                row,
                ("mapping_basis", "mapping_notes"),
                path,
                row_number,
            )
        elif row["mapping_basis"] or row["mapping_notes"]:
            raise ValueError(
                f"{prefix}: unmapped row must not carry mapping rationale"
            )
        if mapping_status == EXACT_MAPPING_STATUS:
            if not row["identifier"] or not row["standard_inchi_key"]:
                raise ValueError(
                    f"{prefix}: EXACT mapping needs identifier and standard_inchi_key"
                )
        elif has_mapping:
            raise ValueError(
                f"{prefix}: non-EXACT mapping must not carry structure fields"
            )

        counts = {
            field: require_report_integer(
                row,
                field,
                prefix,
                minimum=1 if field == "ast_rows" else 0,
            )
            for field in ANTIBIOTIC_REPORT_COUNT_FIELDS
        }
        for field in ANTIBIOTIC_REPORT_AST_ROW_BOUNDED_COUNT_FIELDS:
            if counts[field] > counts["ast_rows"]:
                raise ValueError(f"{prefix}: {field} must be <= ast_rows")

        for field, maximum_field in ANTIBIOTIC_REPORT_COUNT_BOUNDS:
            if counts[field] > counts[maximum_field]:
                raise ValueError(
                    f"{prefix}: {field} must be <= {maximum_field}"
                )
        if (
            counts["activity_report_candidate_count"]
            + counts["activity_report_dedupe_excluded_count"]
            > counts["ast_rows"]
        ):
            raise ValueError(
                f"{prefix}: activity_report_candidate_count plus "
                "activity_report_dedupe_excluded_count must be <= ast_rows"
            )
        if (
            counts["standardized_mic_count"]
            + counts["invalid_mic_count"]
            != counts["mic_count"]
        ):
            raise ValueError(
                f"{prefix}: mic_count must match standardized_mic_count plus "
                "invalid_mic_count"
            )
        if (
            counts["standardized_disk_diffusion_count"]
            + counts["invalid_disk_diffusion_count"]
            != counts["disk_diffusion_count"]
        ):
            raise ValueError(
                f"{prefix}: disk_diffusion_count must match "
                "standardized_disk_diffusion_count plus "
                "invalid_disk_diffusion_count"
            )

        candidate_identifiers = require_sorted_pipe_values(
            row,
            "exact_name_candidate_identifiers",
            prefix,
        )
        candidate_keys = require_pipe_values(
            row,
            "exact_name_candidate_inchi_keys",
            prefix,
            pattern=STANDARD_INCHI_KEY_PATTERN,
        )
        if len(candidate_identifiers) != counts["exact_name_candidate_count"]:
            raise ValueError(
                f"{prefix}: exact_name_candidate_count must match "
                "exact_name_candidate_identifiers"
            )
        if len(candidate_keys) != counts["exact_name_candidate_count"]:
            raise ValueError(
                f"{prefix}: exact_name_candidate_count must match "
                "exact_name_candidate_inchi_keys"
            )

        valid_taxon_id_count = (
            counts["taxon_id_count"] - counts["invalid_taxon_id_count"]
        )
        require_count_bounded_pipe_values(
            row,
            "taxon_ids",
            prefix,
            valid_taxon_id_count,
            "valid_taxon_id_count",
            pattern=ACTIVITY_REPORT_TAXON_ID_PATTERN,
        )
        require_count_bounded_pipe_values(
            row,
            "taxon_labels",
            prefix,
            counts["taxon_count"],
            "taxon_count",
        )
        require_count_bounded_pipe_values(
            row,
            "phenotypes",
            prefix,
            counts["phenotype_count"],
            "phenotype_count",
        )
        require_count_bounded_pipe_values(
            row,
            "standardized_mic_values",
            prefix,
            counts["standardized_mic_count"],
            "standardized_mic_count",
        )
        require_count_bounded_pipe_values(
            row,
            "standardized_disk_diffusion_values",
            prefix,
            counts["standardized_disk_diffusion_count"],
            "standardized_disk_diffusion_count",
        )


def write_antibiotic_report(rows: list[dict], path: Path) -> None:
    require_antibiotic_report_rows(rows, path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=ANTIBIOTIC_REPORT_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def require_drug_map_template_rows(rows: list[dict], path: Path) -> None:
    require_input_rows(rows, DRUG_MAP_TEMPLATE_INPUT_COLUMNS, path)

    seen_source_record_ids = set()
    for row_number, row in enumerate(rows, start=1):
        prefix = f"{path}: template input row {row_number}"
        normalized_antibiotic = str(row["normalized_antibiotic"])
        if not normalized_antibiotic:
            raise ValueError(f"{prefix}: normalized_antibiotic is required")
        if normalized_antibiotic != normalize(str(row["antibiotic"])):
            raise ValueError(f"{prefix}: normalized_antibiotic must match antibiotic")
        if normalized_antibiotic in seen_source_record_ids:
            raise ValueError(
                f"{prefix}: duplicate NCBI AST antibiotic template row "
                f"{normalized_antibiotic!r}"
            )
        seen_source_record_ids.add(normalized_antibiotic)

        mapping_status = str(row["mapping_status"])
        if mapping_status and mapping_status not in MAPPING_STATUSES:
            raise ValueError(
                f"{prefix}: unknown mapping_status {mapping_status!r}"
            )
        identifier = str(row["identifier"])
        standard_inchi_key = str(row["standard_inchi_key"])
        mapping_basis = str(row["mapping_basis"])
        mapping_notes = str(row["mapping_notes"])
        has_mapping = bool(identifier or standard_inchi_key)
        if mapping_status:
            for field, value in (
                ("mapping_basis", mapping_basis),
                ("mapping_notes", mapping_notes),
            ):
                if not value:
                    raise ValueError(f"{prefix}: {field} is required")
        elif mapping_basis or mapping_notes:
            raise ValueError(
                f"{prefix}: unmapped row must not carry mapping rationale"
            )
        if mapping_status == EXACT_MAPPING_STATUS:
            if not identifier or not standard_inchi_key:
                raise ValueError(
                    f"{prefix}: EXACT mapping needs identifier and standard_inchi_key"
                )
        elif has_mapping:
            raise ValueError(
                f"{prefix}: non-EXACT mapping must not carry structure fields"
            )


def write_drug_map_template(rows: list[dict], path: Path, source_version: str) -> None:
    require_drug_map_template_rows(rows, path)
    source_version = require_tsv_safe_value(source_version, "source_version", str(path))
    if not source_version:
        raise ValueError(f"{path}: source_version is required")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=DRUG_MAP_COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({
                "source_version": source_version,
                "source_record_id": row["normalized_antibiotic"],
                "source_name": row["antibiotic"],
                "mapping_status": row["mapping_status"],
                "identifier": row["identifier"],
                "standard_inchi_key": row["standard_inchi_key"],
                "mapping_basis": row["mapping_basis"],
                "notes": row["mapping_notes"],
            })


def require_sorted_pipe_values(
    row: dict[str, str],
    field: str,
    prefix: str,
    *,
    pattern: re.Pattern[str] | None = None,
) -> list[str]:
    values = require_pipe_values(row, field, prefix, pattern=pattern)
    canonical_values = sorted(set(values))
    if values != canonical_values:
        raise ValueError(f"{prefix}: {field} must be unique and sorted")
    return values


def require_pipe_values(
    row: dict[str, str],
    field: str,
    prefix: str,
    *,
    pattern: re.Pattern[str] | None = None,
) -> list[str]:
    values = row[field].split("|") if row[field] else []
    if any(not value for value in values):
        raise ValueError(f"{prefix}: {field} contains an empty value")
    if pattern is not None:
        for value in values:
            if pattern.match(value) is None:
                raise ValueError(f"{prefix}: invalid {field} value {value!r}")
    return values


def require_count_bounded_pipe_values(
    row: dict[str, str],
    field: str,
    prefix: str,
    count: int,
    count_field: str,
    *,
    pattern: re.Pattern[str] | None = None,
) -> list[str]:
    values = require_sorted_pipe_values(row, field, prefix, pattern=pattern)
    if count and not values:
        raise ValueError(f"{prefix}: {count_field} requires {field}")
    if len(values) > count:
        raise ValueError(
            f"{prefix}: {field} must have no more values than {count_field}"
        )
    return values


def require_project_dedupe_report_rows(rows: list[dict], path: Path) -> None:
    require_output_rows(rows, PROJECT_DEDUPE_REPORT_COLUMNS, path)

    seen_keys = set()
    for row_number, raw_row in enumerate(rows, start=1):
        prefix = f"{path}: output row {row_number}"
        row = {field: str(raw_row[field]) for field in PROJECT_DEDUPE_REPORT_COLUMNS}

        accession_type = row["accession_type"]
        if accession_type not in PROJECT_DEDUPE_ACCESSIONS:
            raise ValueError(f"{prefix}: unsupported accession_type {accession_type!r}")
        accession_pattern = PROJECT_DEDUPE_ACCESSIONS[accession_type][1]
        if accession_pattern.match(row["accession"]) is None:
            raise ValueError(f"{prefix}: invalid {accession_type} accession")
        key = (accession_type, row["accession"])
        if key in seen_keys:
            raise ValueError(f"{prefix}: duplicate project dedupe context {key}")
        seen_keys.add(key)

        ast_rows = require_report_integer(
            row,
            "ast_rows",
            prefix,
            minimum=1,
        )
        exact_mapped_rows = require_report_integer(
            row,
            "exact_mapped_rows",
            prefix,
        )
        exact_mapped_antibiotic_values = require_report_integer(
            row,
            "exact_mapped_antibiotic_values",
            prefix,
        )
        biosample_count = require_report_integer(
            row,
            "biosample_count",
            prefix,
            minimum=1,
        )
        bioproject_count = require_report_integer(
            row,
            "bioproject_count",
            prefix,
            minimum=1,
        )
        antibiotic_values = require_report_integer(
            row,
            "antibiotic_values",
            prefix,
            minimum=1,
        )

        if exact_mapped_rows > ast_rows:
            raise ValueError(f"{prefix}: exact_mapped_rows must be <= ast_rows")
        if antibiotic_values > ast_rows:
            raise ValueError(f"{prefix}: antibiotic_values must be <= ast_rows")
        if biosample_count > ast_rows:
            raise ValueError(f"{prefix}: biosample_count must be <= ast_rows")
        if bioproject_count > ast_rows:
            raise ValueError(f"{prefix}: bioproject_count must be <= ast_rows")
        if exact_mapped_antibiotic_values > antibiotic_values:
            raise ValueError(
                f"{prefix}: exact_mapped_antibiotic_values must be <= antibiotic_values"
            )
        if exact_mapped_antibiotic_values > exact_mapped_rows:
            raise ValueError(
                f"{prefix}: exact_mapped_antibiotic_values must be <= "
                "exact_mapped_rows"
            )
        if exact_mapped_rows and not exact_mapped_antibiotic_values:
            raise ValueError(
                f"{prefix}: exact_mapped_rows requires "
                "exact_mapped_antibiotic_values"
            )

        exact_mapped_antibiotics = require_sorted_pipe_values(
            row,
            "exact_mapped_antibiotics",
            prefix,
        )
        exact_mapped_identifiers = require_sorted_pipe_values(
            row,
            "exact_mapped_identifiers",
            prefix,
        )
        antibiotics = require_sorted_pipe_values(row, "antibiotics", prefix)
        require_sorted_pipe_values(
            row,
            "taxon_ids",
            prefix,
            pattern=ACTIVITY_REPORT_TAXON_ID_PATTERN,
        )
        taxon_labels = require_sorted_pipe_values(row, "taxon_labels", prefix)

        if len(exact_mapped_antibiotics) != exact_mapped_antibiotic_values:
            raise ValueError(
                f"{prefix}: exact_mapped_antibiotic_values must match "
                "exact_mapped_antibiotics"
            )
        if len(antibiotics) != antibiotic_values:
            raise ValueError(f"{prefix}: antibiotic_values must match antibiotics")
        if set(exact_mapped_antibiotics) - set(antibiotics):
            raise ValueError(
                f"{prefix}: exact_mapped_antibiotics must be a subset of antibiotics"
            )
        if len(exact_mapped_identifiers) > exact_mapped_antibiotic_values:
            raise ValueError(
                f"{prefix}: exact_mapped_identifiers must have no more values "
                "than exact_mapped_antibiotic_values"
            )
        if exact_mapped_antibiotics and not exact_mapped_identifiers:
            raise ValueError(
                f"{prefix}: exact_mapped_identifiers are required for exact mappings"
            )
        if not taxon_labels:
            raise ValueError(f"{prefix}: taxon_labels is required")
        if accession_type == "BioSample" and biosample_count != 1:
            raise ValueError(f"{prefix}: biosample_count must be 1 for BioSample rows")
        if accession_type == "BioProject" and bioproject_count != 1:
            raise ValueError(f"{prefix}: bioproject_count must be 1 for BioProject rows")


def write_project_dedupe_report(rows: list[dict], path: Path) -> None:
    require_project_dedupe_report_rows(rows, path)
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


def require_project_dedupe_template_rows(rows: list[dict], path: Path) -> None:
    require_input_rows(rows, PROJECT_DEDUPE_MAP_TEMPLATE_INPUT_COLUMNS, path)

    seen_keys = set()
    for row_number, row in enumerate(rows, start=1):
        prefix = f"{path}: template input row {row_number}"
        accession_type = str(row["accession_type"])
        if accession_type not in PROJECT_DEDUPE_ACCESSIONS:
            raise ValueError(f"{prefix}: unsupported accession_type {accession_type!r}")
        accession_pattern = PROJECT_DEDUPE_ACCESSIONS[accession_type][1]
        accession = str(row["accession"])
        if accession_pattern.match(accession) is None:
            raise ValueError(f"{prefix}: invalid {accession_type} accession")
        key = (accession_type, accession)
        if key in seen_keys:
            raise ValueError(f"{prefix}: duplicate project dedupe context {key}")
        seen_keys.add(key)


def write_project_dedupe_map_template(rows: list[dict], path: Path) -> None:
    require_project_dedupe_template_rows(rows, path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=PROJECT_DEDUPE_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({
                "accession_type": row["accession_type"],
                "accession": row["accession"],
                "source": "",
                "source_version": "",
                "notes": "",
            })


def require_activity_report_positive_integer(
    row: dict[str, str],
    field: str,
    prefix: str,
) -> int:
    try:
        parsed = int(row[field])
    except ValueError as error:
        raise ValueError(f"{prefix}: {field} must be an integer") from error
    if parsed <= 0:
        raise ValueError(f"{prefix}: {field} must be positive")
    canonical = str(parsed)
    if row[field] != canonical:
        raise ValueError(f"{prefix}: {field} must use canonical integer {canonical!r}")
    return parsed


def require_activity_report_measurement(
    row: dict[str, str],
    *,
    value_field: str,
    qualifier_field: str,
    units_field: str,
    expected_units: str,
    minimum: Decimal | None = None,
    maximum: Decimal | None = None,
    prefix: str,
) -> bool:
    value = row[value_field]
    qualifier = row[qualifier_field]
    units = row[units_field]

    if not value:
        if qualifier:
            raise ValueError(f"{prefix}: {qualifier_field} requires {value_field}")
        if units:
            raise ValueError(f"{prefix}: {units_field} requires {value_field}")
        return False

    if qualifier not in MEASUREMENT_QUALIFIERS:
        raise ValueError(f"{prefix}: {qualifier_field} has invalid qualifier {qualifier!r}")
    if units != expected_units:
        raise ValueError(f"{prefix}: {units_field} must be {expected_units!r}")
    try:
        parsed = Decimal(value)
    except InvalidOperation as error:
        raise ValueError(f"{prefix}: {value_field} must be numeric") from error
    if not parsed.is_finite():
        raise ValueError(f"{prefix}: {value_field} must be finite")
    if parsed <= 0:
        raise ValueError(f"{prefix}: {value_field} must be positive")
    if minimum is not None and parsed < minimum:
        raise ValueError(f"{prefix}: {value_field} must be at least {minimum:f}")
    if maximum is not None and parsed > maximum:
        raise ValueError(f"{prefix}: {value_field} must be at most {maximum:f}")
    canonical = format(parsed.normalize(), "f")
    if value != canonical:
        raise ValueError(
            f"{prefix}: {value_field} must use canonical decimal {canonical!r}"
        )
    return True


def require_activity_report_rows(rows: list[dict], path: Path) -> None:
    if not rows:
        raise ValueError(f"{path}: NCBI AST activity report has no rows")
    require_output_rows(rows, ACTIVITY_REPORT_COLUMNS, path)
    seen_group_ids = set()
    expected_source_version = None
    expected_source_retrieved_on = None
    for row_number, raw_row in enumerate(rows, start=1):
        prefix = f"{path}: output row {row_number}"
        for field, value in raw_row.items():
            if value is None:
                raise ValueError(f"{prefix}: {field} is missing")
            string_value = str(value)
            if any(char in string_value for char in CURATED_TSV_CONTROL_CHARS):
                raise ValueError(f"{prefix}: {field} contains a tab or newline")
            if string_value != string_value.strip():
                raise ValueError(f"{prefix}: {field} has leading or trailing whitespace")

        row = {
            field: str(raw_row[field])
            for field in ACTIVITY_REPORT_COLUMNS
        }
        for field in REQUIRED_ACTIVITY_REPORT_COLUMNS:
            if not row[field].strip():
                raise ValueError(f"{prefix}: {field} is required")

        if BIOSAMPLE_PATTERN.match(row["biosample_accession"]) is None:
            raise ValueError(f"{prefix}: invalid BioSample accession")
        if BIOPROJECT_PATTERN.match(row["bioproject_accession"]) is None:
            raise ValueError(f"{prefix}: invalid BioProject accession")
        if row["taxon_id"] and not ACTIVITY_REPORT_TAXON_ID_PATTERN.match(
            row["taxon_id"]
        ):
            raise ValueError(f"{prefix}: invalid NCBI Taxonomy CURIE")
        if row["target_accession"] and not TARGET_PATTERN.match(row["target_accession"]):
            raise ValueError(f"{prefix}: invalid Pathogen Detection target accession")
        if row["assembly_accession"] and not ASSEMBLY_PATTERN.match(
            row["assembly_accession"]
        ):
            raise ValueError(f"{prefix}: invalid Assembly accession")
        if row["sra_accessions"]:
            sra_accessions = row["sra_accessions"].split("|")
            invalid_sra_accessions = [
                accession
                for accession in sra_accessions
                if SRA_ACCESSION_PATTERN.match(accession) is None
            ]
            if invalid_sra_accessions:
                raise ValueError(f"{prefix}: invalid SRA accession")
            canonical_sra_accessions = "|".join(sorted(set(sra_accessions)))
            if row["sra_accessions"] != canonical_sra_accessions:
                raise ValueError(f"{prefix}: sra_accessions must be unique and sorted")
        if row["normalized_antibiotic"] != normalize(row["source_name"]):
            raise ValueError(f"{prefix}: normalized_antibiotic must match source_name")
        if not row["method"] and not row["platform"] and not row["reagent"]:
            raise ValueError(f"{prefix}: method, platform or reagent is required")

        if expected_source_version is None:
            expected_source_version = row["source_version"]
        elif row["source_version"] != expected_source_version:
            raise ValueError(
                f"{prefix}: source_version must be {expected_source_version!r}"
            )

        if not row["source_version"]:
            raise ValueError(f"{prefix}: source_version is required")

        source_retrieved_on = row["source_retrieved_on"]
        if not source_retrieved_on:
            raise ValueError(f"{prefix}: source_retrieved_on is required")
        if not is_iso_date(source_retrieved_on):
            raise ValueError(f"{prefix}: source_retrieved_on must be an ISO date")
        if expected_source_retrieved_on is None:
            expected_source_retrieved_on = source_retrieved_on
        elif source_retrieved_on != expected_source_retrieved_on:
            raise ValueError(
                f"{prefix}: source_retrieved_on must be "
                f"{expected_source_retrieved_on!r}"
            )

        if row["create_date"] and not is_iso_date(row["create_date"]):
            raise ValueError(f"{prefix}: create_date must be an ISO date")

        require_activity_report_positive_integer(row, "ast_row_count", prefix)
        isolate_count = require_activity_report_positive_integer(
            row,
            "isolate_count",
            prefix,
        )
        if isolate_count != 1:
            raise ValueError(
                f"{prefix}: isolate_count must be 1 for a BioSample-grouped row"
            )

        expected_activity = ACTIVITY_CALLS.get(row["phenotype"].casefold(), "")
        if row["phenotype"] and not expected_activity:
            raise ValueError(f"{prefix}: unsupported phenotype {row['phenotype']!r}")
        if row["activity"] != expected_activity:
            raise ValueError(
                f"{prefix}: activity must match phenotype {row['phenotype']!r}"
            )

        has_mic = require_activity_report_measurement(
            row,
            value_field="mic_value",
            qualifier_field="mic_qualifier",
            units_field="mic_units",
            expected_units=MIC_UNITS,
            maximum=MIC_MAX_VALUE,
            prefix=prefix,
        )
        has_disk_diffusion = require_activity_report_measurement(
            row,
            value_field="disk_diffusion_value",
            qualifier_field="disk_diffusion_qualifier",
            units_field="disk_diffusion_units",
            expected_units=DISK_DIFFUSION_UNITS,
            minimum=DISK_DIFFUSION_MIN_VALUE,
            maximum=DISK_DIFFUSION_MAX_VALUE,
            prefix=prefix,
        )
        if not has_mic and not has_disk_diffusion:
            raise ValueError(f"{prefix}: mic_value or disk_diffusion_value is required")

        expected_group_id = activity_group_id(row)
        if row["activity_group_id"] != expected_group_id:
            raise ValueError(
                f"{prefix}: activity_group_id must be {expected_group_id!r}"
            )
        if row["activity_group_id"] in seen_group_ids:
            raise ValueError(f"{prefix}: duplicate activity_group_id")
        seen_group_ids.add(row["activity_group_id"])


def write_activity_report(rows: list[dict], path: Path) -> None:
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
            "Optional AST export or BigQuery snapshot version to pin "
            "--drug-map mappings and stamp on --activity-report rows."
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
    parser.add_argument(
        "--project-dedupe-map-template",
        type=Path,
        help=(
            "Optional fillable TSV for curating BioSample/BioProject "
            "--project-dedupe-map exclusions."
        ),
    )
    args = parser.parse_args()
    if args.activity_report and not args.drug_map:
        parser.error("--activity-report requires --drug-map with exact curated mappings.")
    if args.activity_report and not args.source_version.strip():
        parser.error("--activity-report requires --source-version.")
    if (args.drug_map or args.drug_map_template) and not args.source_version.strip():
        parser.error("--drug-map and --drug-map-template require --source-version.")
    if args.source_version != args.source_version.strip():
        parser.error("--source-version must not have leading or trailing whitespace.")
    if any(char in args.source_version for char in CURATED_TSV_CONTROL_CHARS):
        parser.error("--source-version must not contain tabs or newlines.")
    if args.activity_report and not args.source_retrieved_on:
        parser.error("--activity-report requires --source-retrieved-on.")
    if args.source_retrieved_on and not is_iso_date(args.source_retrieved_on):
        parser.error("--source-retrieved-on must be an ISO date.")

    rows = read_table(args.ast)
    require_any_antibiotic_value(rows, args.ast)
    candidates, structure_keys = corpus_name_candidates()
    mappings = (
        read_drug_map(args.drug_map, structure_keys, source_version=args.source_version)
        if args.drug_map
        else {}
    )
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
        require_activity_report_rows(activity_rows, args.activity_report)

    if args.antibiotic_report:
        write_antibiotic_report(result["antibiotic_rows"], args.antibiotic_report)
    if args.drug_map_template:
        write_drug_map_template(
            result["antibiotic_rows"],
            args.drug_map_template,
            source_version=args.source_version,
        )
    project_dedupe_report_rows_ = []
    if args.project_dedupe_report or args.project_dedupe_map_template:
        project_dedupe_report_rows_ = project_dedupe_report_rows(
            rows,
            mappings,
            project_dedupe,
        )
    if args.project_dedupe_report:
        write_project_dedupe_report(
            project_dedupe_report_rows_,
            args.project_dedupe_report,
        )
    if args.project_dedupe_map_template:
        write_project_dedupe_map_template(
            project_dedupe_report_rows_,
            args.project_dedupe_map_template,
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
        f"sra_accession_rows={result['rows_with_sra_accessions']} "
        f"taxon_id_rows={result['rows_with_taxon_id']}"
    )
    print(
        f"  invalid identifiers: target_acc_rows="
        f"{result['rows_with_invalid_target_acc']} "
        f"assembly_acc_rows={result['rows_with_invalid_assembly_acc']} "
        f"sra_accession_rows={result['rows_with_invalid_sra_accessions']} "
        f"taxon_id_rows={result['rows_with_invalid_taxon_id']}"
    )
    print(
        f"  context: taxon_rows={result['rows_with_taxon']} "
        f"phenotype_rows={result['rows_with_phenotype']} "
        f"invalid_phenotype_rows={result['rows_with_invalid_phenotype']} "
        f"assay_method_rows={result['rows_with_assay_method']}"
    )
    print(
        f"  isolation context: isolation_type_rows={result['rows_with_isolation_type']} "
        f"location_rows={result['rows_with_location']} "
        f"collection_date_rows={result['rows_with_collection_date']} "
        f"create_date_rows={result['rows_with_create_date']} "
        f"invalid_create_date_rows={result['rows_with_invalid_create_date']} "
        f"host_rows={result['rows_with_host']} "
        f"isolation_source_rows={result['rows_with_isolation_source']}"
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
        f"{result['exact_mapped_activity_report_candidate_rows']} "
        f"activity_report_dedupe_excluded_rows="
        f"{result['exact_mapped_activity_report_dedupe_excluded_rows']}"
    )
    print(
        f"  ambiguous names: antibiotics={result['ambiguous_name_antibiotics']} "
        f"rows={result['ambiguous_name_rows']}"
    )
    print(
        f"  unmatched names: antibiotics={result['unmatched_antibiotics']} "
        f"rows={result['unmatched_rows']}"
    )
    if args.drug_map:
        drift = (
            f"  curated map drift: unused_antibiotics="
            f"{result['unused_mapping_antibiotics']}"
        )
        if result["unused_mapping_antibiotic_values"]:
            drift += f" values={result['unused_mapping_antibiotic_values']}"
        print(drift)
    if args.project_dedupe_map:
        drift = (
            f"  project dedupe drift: unused_source_contexts="
            f"{result['unused_project_dedupe_contexts']}"
        )
        if result["unused_project_dedupe_values"]:
            drift += f" values={result['unused_project_dedupe_values']}"
        print(drift)
    print("  leading antibiotics: " + ", ".join(f"{name}={count}" for name, count in leading))
    if args.antibiotic_report:
        print(f"  antibiotic_report={args.antibiotic_report}")
    if args.drug_map_template:
        print(f"  drug_map_template={args.drug_map_template}")
    if args.project_dedupe_report:
        print(f"  project_dedupe_report={args.project_dedupe_report}")
    if args.project_dedupe_map_template:
        print(f"  project_dedupe_map_template={args.project_dedupe_map_template}")
    if args.activity_report:
        print(
            f"  exact_mapped_activity_groups={len(activity_rows)} "
            f"activity_report={args.activity_report}"
        )
    print("--audit: no rows seeded; submitted antibiotic names are not exact structure identifiers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
