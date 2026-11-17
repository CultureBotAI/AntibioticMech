#!/usr/bin/env python3
"""Audit Stanford HIVDB hivfacts drugs and HIV-1 mutation lists.

hivfacts names drugs by HIVDB abbreviations and includes boosted protease
inhibitors such as ATV/r. This preflight reports exact lexical corpus matches
as identity-curation leads only.

The HIV-1 DRMs, SDRMs and TSMs in hivfacts are class-level mutation catalogs.
They are curated mutation evidence, but not exact drug-specific rules. Evaluating
them here makes the mutation surface visible without flattening entire classes
such as NRTI into one compound assertion.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping
from pathlib import Path

import yaml

from antibioticmech.hivdb_score_rules import (
    HIVDB_SCORE_ASSIGNMENT_PATTERN,
    HIVDB_SCORE_RULE_COLUMNS,
    HIVDB_SCORE_RULE_GENE_BY_DRUG_CLASS,
    hivdb_score_rule_id,
)

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
MUTATION_REPORT_COLUMNS = [
    "source_list",
    "drug_class",
    "gene",
    "position",
    "aa",
    "expanded_mutation_count",
    "expanded_mutations",
]
PATTERN_REPORT_COLUMNS = [
    "source_pattern_file",
    "drug_class",
    "source_record_id",
    "source_name",
    "mapping_status",
    "identifier",
    "standard_inchi_key",
    "pattern_rows",
    "nonzero_score_rows",
    "max_level",
    "min_score",
    "max_score",
]
ALGORITHM_REPORT_COLUMNS = [
    "source_version",
    "algorithm_name",
    "algorithm_version",
    "algorithm_date",
    "source_record_id",
    "source_name",
    "algorithm_full_name",
    "full_name_matches",
    "drug_class",
    "gene",
    "mapping_status",
    "identifier",
    "standard_inchi_key",
    "score_terms",
    "score_assignments",
    "negative_score_assignments",
    "min_score",
    "max_score",
    "uses_global_range",
]
ALGORITHM_TERM_REPORT_COLUMNS = HIVDB_SCORE_RULE_COLUMNS
PATTERN_FIELDS = frozenset({"gene", "drugClass", "pattern", "count"})

EXACT_MAPPING_STATUS = "EXACT"
MAPPING_STATUSES = {
    EXACT_MAPPING_STATUS,
    "AMBIGUOUS_IDENTITY",
    "COMBINATION",
    "MISSING_CORPUS_RECORD",
}
CURATED_TSV_CONTROL_CHARS = frozenset("\t\r\n")
COMPACT_TOKEN_PATTERN = re.compile(r"^[A-Z0-9]+$")
COMPACT_AA_PATTERN = re.compile(r"^[A-Z_-]+$")
PATTERN_CONTROL_CHARS = frozenset("\t\r\n")


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


def read_class_mutation_list(path: Path, source_list: str) -> list[dict[str, str]]:
    """Read a hivfacts HIV-1 class-level mutation list.

    ``drms_hiv1.json`` and related files group compact AA strings by drug class;
    for example, ``{"position": 46, "aa": "IL"}`` means PR:46I and PR:46L.
    Keep the compact row and the expanded labels distinct so the report can
    preserve the source shape while still making the represented mutations
    countable.
    """

    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: expected a JSON object keyed by drug class")

    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str, str, str, str]] = set()
    seen_expanded: set[tuple[str, str, str]] = set()
    for drug_class, mutations in payload.items():
        if not isinstance(drug_class, str) or not drug_class.strip():
            raise ValueError(f"{path}: mutation list has a blank drug class")
        drug_class = drug_class.strip()
        if not COMPACT_TOKEN_PATTERN.fullmatch(drug_class):
            raise ValueError(f"{path}: mutation list has invalid drug class {drug_class!r}")
        if not isinstance(mutations, list):
            raise ValueError(f"{path}: {drug_class} mutation list is not an array")
        for index, mutation in enumerate(mutations, start=1):
            if not isinstance(mutation, dict):
                raise ValueError(f"{path}: {drug_class} row {index} is not an object")
            gene = mutation.get("gene")
            position = mutation.get("position")
            aa = mutation.get("aa")
            if not isinstance(gene, str) or not gene.strip():
                raise ValueError(f"{path}: {drug_class} row {index} has no gene")
            if not isinstance(position, int) or position <= 0:
                raise ValueError(f"{path}: {drug_class} row {index} has invalid position")
            if not isinstance(aa, str) or not aa.strip():
                raise ValueError(f"{path}: {drug_class} row {index} has no aa")
            gene = gene.strip()
            aa = aa.strip()
            if not COMPACT_TOKEN_PATTERN.fullmatch(gene):
                raise ValueError(f"{path}: {drug_class} row {index} has invalid gene {gene!r}")
            if not COMPACT_AA_PATTERN.fullmatch(aa):
                raise ValueError(f"{path}: {drug_class} row {index} has invalid aa {aa!r}")

            row = {
                "source_list": source_list,
                "drug_class": drug_class,
                "gene": gene,
                "position": str(position),
                "aa": aa,
            }
            key = (source_list, drug_class, gene, row["position"], aa)
            if key in seen:
                label = mutation_label(gene, position, aa)
                raise ValueError(f"{path}: duplicate {source_list} {drug_class} mutation {label}")
            seen.add(key)
            for label in expanded_mutations(row):
                expanded_key = (source_list, drug_class, label)
                if expanded_key in seen_expanded:
                    raise ValueError(
                        f"{path}: duplicate expanded {source_list} {drug_class} "
                        f"mutation {label}"
                    )
                seen_expanded.add(expanded_key)
            rows.append(row)

    return rows


def read_drug_patterns(
    path: Path,
    source_rows: list[dict[str, str]],
) -> list[dict]:
    """Read one hivfacts HIV-1 drug-class pattern score matrix."""

    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"{path}: expected a JSON array of drug patterns")

    source_ids_by_class: dict[str, list[str]] = defaultdict(list)
    for row in source_rows:
        source_ids_by_class[row["drug_class"]].append(row["source_record_id"])

    rows: list[dict] = []
    seen: set[tuple[str, str, str]] = set()
    file_drug_class = ""
    for index, item in enumerate(payload, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"{path}: row {index} is not an object")
        for field in PATTERN_FIELDS:
            if field not in item:
                raise ValueError(f"{path}: row {index} has no {field}")

        gene = item["gene"]
        drug_class = item["drugClass"]
        pattern = item["pattern"]
        count = item["count"]
        if not isinstance(gene, str) or not gene.strip():
            raise ValueError(f"{path}: row {index} has no gene")
        if not isinstance(drug_class, str) or not drug_class.strip():
            raise ValueError(f"{path}: row {index} has no drugClass")
        if not isinstance(pattern, str) or not pattern.strip():
            raise ValueError(f"{path}: row {index} has no pattern")
        if not isinstance(count, int) or isinstance(count, bool) or count <= 0:
            raise ValueError(f"{path}: row {index} has invalid count")

        gene = gene.strip()
        drug_class = drug_class.strip()
        pattern = pattern.strip()
        if not COMPACT_TOKEN_PATTERN.fullmatch(gene):
            raise ValueError(f"{path}: row {index} has invalid gene {gene!r}")
        if not COMPACT_TOKEN_PATTERN.fullmatch(drug_class):
            raise ValueError(f"{path}: row {index} has invalid drugClass {drug_class!r}")
        if any(char in pattern for char in PATTERN_CONTROL_CHARS):
            raise ValueError(f"{path}: row {index} pattern contains a tab or newline")
        if file_drug_class and file_drug_class != drug_class:
            raise ValueError(
                f"{path}: row {index} mixes drugClass {drug_class!r} "
                f"after {file_drug_class!r}"
            )
        file_drug_class = drug_class

        drug_ids = source_ids_by_class.get(drug_class)
        if not drug_ids:
            raise ValueError(f"{path}: row {index} has unknown drugClass {drug_class!r}")
        expected_fields = set(PATTERN_FIELDS)
        for source_record_id in drug_ids:
            expected_fields.add(f"{source_record_id} Level")
            expected_fields.add(f"{source_record_id} Score")
        if set(item) != expected_fields:
            missing = sorted(expected_fields - set(item))
            extra = sorted(set(item) - expected_fields)
            raise ValueError(
                f"{path}: {drug_class} row {index} has unexpected pattern columns "
                f"missing={missing} extra={extra}"
            )

        scores = {}
        for source_record_id in drug_ids:
            level = item[f"{source_record_id} Level"]
            score = item[f"{source_record_id} Score"]
            if not isinstance(level, int) or isinstance(level, bool) or not 1 <= level <= 5:
                raise ValueError(
                    f"{path}: {drug_class} row {index} has invalid "
                    f"{source_record_id} Level"
                )
            if (
                not isinstance(score, int | float)
                or isinstance(score, bool)
            ):
                raise ValueError(
                    f"{path}: {drug_class} row {index} has invalid "
                    f"{source_record_id} Score"
                )
            scores[source_record_id] = {
                "level": level,
                "score": float(score),
            }

        key = (drug_class, gene, pattern)
        if key in seen:
            raise ValueError(f"{path}: duplicate {drug_class} {gene} pattern {pattern}")
        seen.add(key)
        rows.append(
            {
                "source_pattern_file": path.name,
                "drug_class": drug_class,
                "gene": gene,
                "pattern": pattern,
                "count": count,
                "scores": scores,
            }
        )

    return rows


def xml_child_text(parent: ET.Element, child_name: str, path: Path, context: str) -> str:
    child = parent.find(child_name)
    if child is None or child.text is None or not child.text.strip():
        raise ValueError(f"{path}: {context} has no {child_name}")
    value = child.text.strip()
    if any(char in value for char in CURATED_TSV_CONTROL_CHARS):
        raise ValueError(f"{path}: {context} {child_name} contains a tab or newline")
    return value


def xml_block_text(parent: ET.Element, child_name: str, path: Path, context: str) -> str:
    child = parent.find(child_name)
    if child is None or child.text is None or not child.text.strip():
        raise ValueError(f"{path}: {context} has no {child_name}")
    value = child.text.strip()
    if any(char in value for char in "\t\r"):
        raise ValueError(f"{path}: {context} {child_name} contains a tab or carriage return")
    return value


def score_condition_terms(
    condition: str,
    path: Path,
    source_record_id: str,
) -> list[dict]:
    condition = condition.strip()
    prefix = "SCORE FROM ("
    if not condition.startswith(prefix) or not condition.endswith(")"):
        raise ValueError(f"{path}: {source_record_id} rule is not a SCORE FROM block")

    terms = []
    term_start = len(prefix)
    depth = 0
    for index, char in enumerate(condition[len(prefix) : -1], start=len(prefix)):
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth < 0:
                raise ValueError(f"{path}: {source_record_id} rule has unbalanced parentheses")
        elif char == "," and depth == 0:
            terms.append(condition[term_start:index].strip())
            term_start = index + 1

    if depth:
        raise ValueError(f"{path}: {source_record_id} rule has unbalanced parentheses")
    terms.append(condition[term_start:-1].strip())

    rows = []
    for index, term in enumerate(terms, start=1):
        if not term:
            raise ValueError(f"{path}: {source_record_id} score term {index} is blank")
        term_scores = [
            float(score) for score in HIVDB_SCORE_ASSIGNMENT_PATTERN.findall(term)
        ]
        if not term_scores:
            raise ValueError(
                f"{path}: {source_record_id} score term {index} "
                "has no score assignment"
            )
        rows.append(
            {
                "score_term_index": index,
                "score_term": " ".join(term.split()),
                "score_assignments": len(term_scores),
                "negative_score_assignments": sum(score < 0 for score in term_scores),
                "min_score": min(term_scores),
                "max_score": max(term_scores),
            }
        )

    return rows


def score_condition_stats(terms: list[dict]) -> dict:
    min_scores = [row["min_score"] for row in terms]
    max_scores = [row["max_score"] for row in terms]

    return {
        "score_terms": len(terms),
        "score_assignments": sum(row["score_assignments"] for row in terms),
        "negative_score_assignments": sum(
            row["negative_score_assignments"]
            for row in terms
        ),
        "min_score": min(min_scores),
        "max_score": max(max_scores),
    }


def read_hiv1_algorithm(path: Path, source_rows: list[dict[str, str]]) -> list[dict]:
    """Read drug-specific score rules from a hivfacts ASI HIVDB XML algorithm."""

    root = ET.parse(path).getroot()
    if root.tag != "ALGORITHM":
        raise ValueError(f"{path}: expected ALGORITHM root")

    algorithm_name = xml_child_text(root, "ALGNAME", path, "ALGORITHM")
    algorithm_version = xml_child_text(root, "ALGVERSION", path, "ALGORITHM")
    algorithm_date = xml_child_text(root, "ALGDATE", path, "ALGORITHM")
    try:
        dt.date.fromisoformat(algorithm_date)
    except ValueError as error:
        raise ValueError(f"{path}: invalid ALGDATE {algorithm_date!r}") from error

    source_rows_by_id = {row["source_record_id"]: row for row in source_rows}
    if len(source_rows_by_id) != len(source_rows):
        raise ValueError("duplicate HIVDB drug source rows")

    definitions = root.find("DEFINITIONS")
    if definitions is None:
        raise ValueError(f"{path}: ALGORITHM has no DEFINITIONS")

    defined_source_ids: set[str] = set()
    for index, drug_class_node in enumerate(definitions.findall("DRUGCLASS"), start=1):
        drug_class = xml_child_text(
            drug_class_node,
            "NAME",
            path,
            f"DRUGCLASS {index}",
        )
        raw_drug_list = xml_child_text(
            drug_class_node,
            "DRUGLIST",
            path,
            f"DRUGCLASS {drug_class}",
        )
        source_record_ids = [
            source_record_id.strip()
            for source_record_id in raw_drug_list.split(",")
            if source_record_id.strip()
        ]
        if not source_record_ids:
            raise ValueError(f"{path}: DRUGCLASS {drug_class} has no drugs")

        for source_record_id in source_record_ids:
            if source_record_id in defined_source_ids:
                raise ValueError(
                    f"{path}: duplicate algorithm drug class entry {source_record_id}"
                )
            defined_source_ids.add(source_record_id)
            source_row = source_rows_by_id.get(source_record_id)
            if source_row is None:
                raise ValueError(
                    f"{path}: algorithm class {drug_class} names unknown drug "
                    f"{source_record_id}"
                )
            if source_row["drug_class"] != drug_class:
                raise ValueError(
                    f"{path}: algorithm class {drug_class} for {source_record_id} "
                    f"!= hivfacts class {source_row['drug_class']}"
                )
            if drug_class not in HIVDB_SCORE_RULE_GENE_BY_DRUG_CLASS:
                raise ValueError(
                    f"{path}: algorithm class {drug_class} has no score-rule "
                    "gene mapping"
                )

    missing_defined_ids = set(source_rows_by_id) - defined_source_ids
    if missing_defined_ids:
        raise ValueError(
            f"{path}: algorithm drug classes omit {sorted(missing_defined_ids)}"
        )

    rows = []
    seen_drugs: set[str] = set()
    for index, drug_node in enumerate(root.findall("DRUG"), start=1):
        source_record_id = xml_child_text(drug_node, "NAME", path, f"DRUG {index}")
        algorithm_full_name = xml_child_text(
            drug_node,
            "FULLNAME",
            path,
            f"DRUG {source_record_id}",
        )
        source_row = source_rows_by_id.get(source_record_id)
        if source_row is None:
            raise ValueError(f"{path}: algorithm names unknown drug {source_record_id}")
        if source_record_id in seen_drugs:
            raise ValueError(f"{path}: duplicate algorithm drug {source_record_id}")
        seen_drugs.add(source_record_id)

        rules = drug_node.findall("RULE")
        if len(rules) != 1:
            raise ValueError(
                f"{path}: {source_record_id} must have exactly one score rule"
            )
        condition = xml_block_text(rules[0], "CONDITION", path, source_record_id)
        if rules[0].find("ACTIONS/SCORERANGE/USE_GLOBALRANGE") is None:
            raise ValueError(f"{path}: {source_record_id} does not use GLOBALRANGE")
        score_term_rows = score_condition_terms(condition, path, source_record_id)

        rows.append(
            {
                "algorithm_name": algorithm_name,
                "algorithm_version": algorithm_version,
                "algorithm_date": algorithm_date,
                "source_record_id": source_record_id,
                "source_name": source_row["full_name"],
                "algorithm_full_name": algorithm_full_name,
                "full_name_matches": (
                    "true"
                    if algorithm_full_name == source_row["full_name"]
                    else "false"
                ),
                "drug_class": source_row["drug_class"],
                "gene": HIVDB_SCORE_RULE_GENE_BY_DRUG_CLASS[source_row["drug_class"]],
                "uses_global_range": "true",
                **score_condition_stats(score_term_rows),
                "score_term_rows": score_term_rows,
            }
        )

    missing_drugs = set(source_rows_by_id) - seen_drugs
    if missing_drugs:
        raise ValueError(f"{path}: algorithm omits drugs {sorted(missing_drugs)}")

    return rows


def expanded_mutations(row: Mapping[str, str]) -> list[str]:
    return [
        mutation_label(row["gene"], int(row["position"]), aa)
        for aa in row["aa"]
    ]


def mutation_label(gene: str, position: int, aa: str) -> str:
    return f"{gene}:{position}{aa}"


def evaluate_class_mutations(rows: list[dict[str, str]]) -> dict:
    report_rows = []
    for row in rows:
        mutations = expanded_mutations(row)
        report_rows.append(
            {
                **row,
                "expanded_mutation_count": len(mutations),
                "expanded_mutations": "|".join(mutations),
            }
        )

    return {
        "mutation_rows": len(rows),
        "expanded_mutations": sum(len(row["aa"]) for row in rows),
        "source_lists": Counter(row["source_list"] for row in rows),
        "drug_classes": Counter(row["drug_class"] for row in rows),
        "genes": Counter(row["gene"] for row in rows),
        "mutation_rows_report": report_rows,
    }


def evaluate_drug_patterns(
    rows: list[dict],
    source_rows: list[dict[str, str]],
    mappings: Mapping[str, Mapping[str, str]],
) -> dict:
    source_rows_by_id = {
        row["source_record_id"]: row
        for row in source_rows
    }
    report_rows_by_key = {}
    exact_pattern_score_pairs = 0
    non_exact_pattern_score_pairs = 0

    for row in rows:
        for source_record_id, score_row in row["scores"].items():
            mapping = mappings.get(source_record_id, {})
            if mapping.get("mapping_status") == EXACT_MAPPING_STATUS:
                exact_pattern_score_pairs += 1
            else:
                non_exact_pattern_score_pairs += 1

            source_row = source_rows_by_id[source_record_id]
            key = (row["source_pattern_file"], row["drug_class"], source_record_id)
            report_row = report_rows_by_key.setdefault(
                key,
                {
                    "source_pattern_file": row["source_pattern_file"],
                    "drug_class": row["drug_class"],
                    "source_record_id": source_record_id,
                    "source_name": source_row["full_name"],
                    "mapping_status": mapping.get("mapping_status", ""),
                    "identifier": mapping.get("identifier", ""),
                    "standard_inchi_key": mapping.get("standard_inchi_key", ""),
                    "pattern_rows": 0,
                    "nonzero_score_rows": 0,
                    "max_level": 0,
                    "min_score": None,
                    "max_score": None,
                },
            )
            report_row["pattern_rows"] += 1
            if score_row["score"] != 0:
                report_row["nonzero_score_rows"] += 1
            report_row["max_level"] = max(report_row["max_level"], score_row["level"])
            report_row["min_score"] = (
                score_row["score"]
                if report_row["min_score"] is None
                else min(report_row["min_score"], score_row["score"])
            )
            report_row["max_score"] = (
                score_row["score"]
                if report_row["max_score"] is None
                else max(report_row["max_score"], score_row["score"])
            )

    return {
        "pattern_rows": len(rows),
        "drug_pattern_score_pairs": (
            exact_pattern_score_pairs + non_exact_pattern_score_pairs
        ),
        "exact_pattern_score_pairs": exact_pattern_score_pairs,
        "non_exact_pattern_score_pairs": non_exact_pattern_score_pairs,
        "drug_classes": Counter(row["drug_class"] for row in rows),
        "genes": Counter(row["gene"] for row in rows),
        "pattern_report_rows": [
            report_rows_by_key[key]
            for key in sorted(report_rows_by_key)
        ],
    }


def evaluate_hiv1_algorithm_rules(
    rows: list[dict],
    mappings: Mapping[str, Mapping[str, str]],
) -> dict:
    report_rows = []
    term_report_rows = []
    exact_score_assignments = 0
    non_exact_score_assignments = 0
    for row in rows:
        mapping = mappings.get(row["source_record_id"], {})
        score_assignments = row["score_assignments"]
        if mapping.get("mapping_status") == EXACT_MAPPING_STATUS:
            exact_score_assignments += score_assignments
        else:
            non_exact_score_assignments += score_assignments

        report_rows.append(
            {
                "source_version": HIVDB_HIVFACTS_COMMIT,
                "algorithm_name": row["algorithm_name"],
                "algorithm_version": row["algorithm_version"],
                "algorithm_date": row["algorithm_date"],
                "source_record_id": row["source_record_id"],
                "source_name": row["source_name"],
                "algorithm_full_name": row["algorithm_full_name"],
                "full_name_matches": row["full_name_matches"],
                "drug_class": row["drug_class"],
                "gene": row["gene"],
                "mapping_status": mapping.get("mapping_status", ""),
                "identifier": mapping.get("identifier", ""),
                "standard_inchi_key": mapping.get("standard_inchi_key", ""),
                "score_terms": row["score_terms"],
                "score_assignments": row["score_assignments"],
                "negative_score_assignments": row["negative_score_assignments"],
                "min_score": row["min_score"],
                "max_score": row["max_score"],
                "uses_global_range": row["uses_global_range"],
            }
        )
        for term_row in row["score_term_rows"]:
            report_row = {
                "source_rule_id": "",
                "source_version": HIVDB_HIVFACTS_COMMIT,
                "algorithm_name": row["algorithm_name"],
                "algorithm_version": row["algorithm_version"],
                "algorithm_date": row["algorithm_date"],
                "source_record_id": row["source_record_id"],
                "source_name": row["source_name"],
                "algorithm_full_name": row["algorithm_full_name"],
                "full_name_matches": row["full_name_matches"],
                "drug_class": row["drug_class"],
                "gene": row["gene"],
                "mapping_status": mapping.get("mapping_status", ""),
                "identifier": mapping.get("identifier", ""),
                "standard_inchi_key": mapping.get("standard_inchi_key", ""),
                **term_row,
            }
            report_row["source_rule_id"] = hivdb_score_rule_id(report_row)
            term_report_rows.append(report_row)

    return {
        "algorithm_drugs": len(rows),
        "score_terms": sum(row["score_terms"] for row in rows),
        "score_assignments": exact_score_assignments + non_exact_score_assignments,
        "exact_score_assignments": exact_score_assignments,
        "non_exact_score_assignments": non_exact_score_assignments,
        "full_name_mismatches": sum(row["full_name_matches"] != "true" for row in rows),
        "algorithm_report_rows": report_rows,
        "algorithm_term_report_rows": term_report_rows,
    }


def exact_algorithm_term_report_rows(rows: list[dict]) -> list[dict]:
    return [row for row in rows if row["mapping_status"] == EXACT_MAPPING_STATUS]


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


def write_mutation_report(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=MUTATION_REPORT_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_pattern_report(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=PATTERN_REPORT_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_algorithm_report(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=ALGORITHM_REPORT_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_algorithm_term_report(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=ALGORITHM_TERM_REPORT_COLUMNS,
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
    parser.add_argument("--hiv1-drms", type=Path, help="Optional hivfacts data/drms_hiv1.json.")
    parser.add_argument("--hiv1-sdrms", type=Path, help="Optional hivfacts data/sdrms_hiv1.json.")
    parser.add_argument("--hiv1-tsms", type=Path, help="Optional hivfacts data/tsms_hiv1.json.")
    parser.add_argument(
        "--mutation-report",
        type=Path,
        help="Optional TSV class-level HIV-1 DRM/SDRM/TSM audit.",
    )
    parser.add_argument(
        "--hiv1-patterns",
        action="append",
        type=Path,
        default=[],
        help="Optional hivfacts data/patterns-hiv1/patterns-*.json; repeatable.",
    )
    parser.add_argument(
        "--pattern-report",
        type=Path,
        help="Optional TSV HIV-1 drug pattern score audit.",
    )
    parser.add_argument(
        "--hiv1-algorithm",
        type=Path,
        help="Optional hivfacts data/algorithms/HIVDB_*.xml.",
    )
    parser.add_argument(
        "--algorithm-report",
        type=Path,
        help="Optional TSV HIV-1 drug-specific algorithm score audit.",
    )
    parser.add_argument(
        "--algorithm-term-report",
        type=Path,
        help="Optional TSV HIV-1 drug-specific algorithm score-term audit.",
    )
    parser.add_argument(
        "--exact-algorithm-term-report",
        type=Path,
        help="Optional TSV exact-mapped HIV-1 algorithm score-term seed inventory.",
    )
    parser.add_argument("--corpus-root", type=Path, default=REPO_ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()

    if not args.drugs.exists():
        raise SystemExit(f"missing hivfacts drugs input: {args.drugs}")

    candidates, structure_keys = corpus_name_candidates(args.corpus_root)
    drugs = read_drugs(args.drugs)
    mappings = read_drug_map(args.drug_map, structure_keys, drugs) if args.drug_map else {}
    result = evaluate_drugs(drugs, candidates, structure_keys, mappings=mappings)

    mutation_inputs = [
        ("DRM", args.hiv1_drms),
        ("SDRM", args.hiv1_sdrms),
        ("TSM", args.hiv1_tsms),
    ]
    missing_mutation_inputs = [
        path
        for _, path in mutation_inputs
        if path is not None and not path.exists()
    ]
    if missing_mutation_inputs:
        raise SystemExit(
            "missing hivfacts mutation input(s): "
            + ", ".join(str(path) for path in missing_mutation_inputs)
        )
    missing_pattern_inputs = [
        path
        for path in args.hiv1_patterns
        if not path.exists()
    ]
    if missing_pattern_inputs:
        raise SystemExit(
            "missing hivfacts pattern input(s): "
            + ", ".join(str(path) for path in missing_pattern_inputs)
        )
    if args.hiv1_algorithm is not None and not args.hiv1_algorithm.exists():
        raise SystemExit(f"missing hivfacts algorithm input: {args.hiv1_algorithm}")

    mutation_rows = [
        row
        for source_list, path in mutation_inputs
        if path is not None
        for row in read_class_mutation_list(path, source_list)
    ]
    mutation_result = evaluate_class_mutations(mutation_rows)
    pattern_rows = [
        row
        for path in args.hiv1_patterns
        for row in read_drug_patterns(path, drugs)
    ]
    pattern_result = evaluate_drug_patterns(pattern_rows, drugs, mappings)
    algorithm_rows = (
        read_hiv1_algorithm(args.hiv1_algorithm, drugs)
        if args.hiv1_algorithm is not None
        else []
    )
    algorithm_result = evaluate_hiv1_algorithm_rules(algorithm_rows, mappings)

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
    if mutation_rows:
        print(
            "  HIV-1 class-level mutation lists: "
            f"rows={mutation_result['mutation_rows']} "
            f"expanded_mutations={mutation_result['expanded_mutations']} "
            "source_lists="
            + ",".join(
                f"{name}={count}"
                for name, count in sorted(mutation_result["source_lists"].items())
            )
        )
    if args.hiv1_patterns:
        print(
            "  HIV-1 drug pattern matrices: "
            f"rows={pattern_result['pattern_rows']} "
            f"level_score_pairs={pattern_result['drug_pattern_score_pairs']} "
            f"exact_pairs={pattern_result['exact_pattern_score_pairs']} "
            f"non_exact_pairs={pattern_result['non_exact_pattern_score_pairs']}"
        )
    if args.hiv1_algorithm:
        print(
            "  HIV-1 algorithm score rules: "
            f"drugs={algorithm_result['algorithm_drugs']} "
            f"score_assignments={algorithm_result['score_assignments']} "
            f"exact_assignments={algorithm_result['exact_score_assignments']} "
            f"non_exact_assignments={algorithm_result['non_exact_score_assignments']} "
            f"full_name_mismatches={algorithm_result['full_name_mismatches']}"
        )

    if args.drug_report:
        write_drug_report(result["drug_rows"], args.drug_report)
        print(f"wrote {args.drug_report}")
    if args.drug_map_template:
        write_drug_map_template(result["drug_rows"], args.drug_map_template)
        print(f"wrote {args.drug_map_template}")
    if args.mutation_report:
        write_mutation_report(mutation_result["mutation_rows_report"], args.mutation_report)
        print(f"wrote {args.mutation_report}")
    if args.pattern_report:
        write_pattern_report(pattern_result["pattern_report_rows"], args.pattern_report)
        print(f"wrote {args.pattern_report}")
    if args.algorithm_report:
        write_algorithm_report(
            algorithm_result["algorithm_report_rows"],
            args.algorithm_report,
        )
        print(f"wrote {args.algorithm_report}")
    if args.algorithm_term_report:
        write_algorithm_term_report(
            algorithm_result["algorithm_term_report_rows"],
            args.algorithm_term_report,
        )
        print(f"wrote {args.algorithm_term_report}")
    if args.exact_algorithm_term_report:
        write_algorithm_term_report(
            exact_algorithm_term_report_rows(
                algorithm_result["algorithm_term_report_rows"]
            ),
            args.exact_algorithm_term_report,
        )
        print(f"wrote {args.exact_algorithm_term_report}")

    print(
        "--audit: no rows seeded; HIVDB drug-specific mutation rules need a "
        "schema-specific importer"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
