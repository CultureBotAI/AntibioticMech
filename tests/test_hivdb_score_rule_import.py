"""Unit tests for seeding exact Stanford HIVDB score-rule reports."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import pytest

from antibioticmech.hivdb_score_rules import (
    HIVDB_SCORE_RULE_COLUMNS,
    HIVDB_SCORE_RULE_ID_VERSION,
    hivdb_score_rule_id,
)
from antibioticmech.validation.write_validated import validate_antibiotic

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import evaluate_hivdb_hivfacts  # noqa: E402
import seed_from_sources  # noqa: E402
from seed_from_sources import (  # noqa: E402
    HIVDB_SCORE_RULE_SOURCE,
    attach_hivdb_score_rules,
    hivdb_sourced_score_rule_view,
    load_hivdb_score_rule_inventory,
    merge_with_existing,
)


def write_score_rule_report(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=HIVDB_SCORE_RULE_COLUMNS,
            delimiter="\t",
        )
        writer.writeheader()
        writer.writerows(rows)


def hivdb_score_rule_row(**overrides: str) -> dict[str, str]:
    row = {column: "" for column in HIVDB_SCORE_RULE_COLUMNS}
    row.update({
        "source_version": "be1c11a5145fea9073fdb71801919d4a34265336",
        "algorithm_name": "HIVDB",
        "algorithm_version": "10.2",
        "algorithm_date": "2026-04-26",
        "source_record_id": "ABC",
        "source_name": "abacavir",
        "algorithm_full_name": "abacavir",
        "full_name_matches": "true",
        "drug_class": "NRTI",
        "gene": "RT",
        "mapping_status": "EXACT",
        "identifier": "CHEBI:421707",
        "standard_inchi_key": "MCI",
        "score_term_index": "2",
        "score_term": "MAX(184I => 15, 184V => 15)",
        "score_assignments": "2",
        "negative_score_assignments": "0",
        "min_score": "15.0",
        "max_score": "15.0",
    })
    row.update(overrides)
    if "source_rule_id" not in overrides:
        row["source_rule_id"] = hivdb_score_rule_id(row)
    return row


def test_hivdb_score_rule_columns_match_the_evaluator_contract():
    row = hivdb_score_rule_row()

    assert evaluate_hivdb_hivfacts.ALGORITHM_TERM_REPORT_COLUMNS == (
        HIVDB_SCORE_RULE_COLUMNS
    )
    assert HIVDB_SCORE_RULE_ID_VERSION == "hivdb_score_rule_v1"
    assert row["source_rule_id"] == hivdb_score_rule_id(row)


def test_load_hivdb_score_rule_inventory_accepts_exact_term_rows(tmp_path):
    path = tmp_path / "hivdb_algorithm_terms.tsv"
    row = hivdb_score_rule_row()
    write_score_rule_report(path, [row])

    assert load_hivdb_score_rule_inventory(path) == [row]


def test_load_hivdb_score_rule_inventory_rejects_empty_reports(tmp_path):
    path = tmp_path / "hivdb_algorithm_terms.tsv"
    write_score_rule_report(path, [])

    with pytest.raises(ValueError, match="HIVDB score-rule inventory has no rows"):
        load_hivdb_score_rule_inventory(path)


def test_load_hivdb_score_rule_inventory_rejects_duplicate_score_term_positions(
    tmp_path,
):
    path = tmp_path / "hivdb_algorithm_terms.tsv"
    write_score_rule_report(
        path,
        [
            hivdb_score_rule_row(
                score_term="65R => -10",
                score_assignments="1",
                negative_score_assignments="1",
                min_score="-10.0",
                max_score="-10.0",
            ),
            hivdb_score_rule_row(
                score_term="184V => 15",
                score_assignments="1",
                score_term_index="2",
            ),
        ],
    )

    with pytest.raises(
        ValueError,
        match="duplicate score_term_index 2 for source_record_id 'ABC'",
    ):
        load_hivdb_score_rule_inventory(path)


@pytest.mark.parametrize(
    ("overrides", "message"),
    [
        ({"score_assignments": "1"}, "score_assignments must match score_term"),
        (
            {"negative_score_assignments": "1"},
            "negative_score_assignments must match score_term",
        ),
        ({"min_score": "10.0"}, "min_score must match score_term"),
        ({"max_score": "20.0"}, "max_score must match score_term"),
        (
            {"score_term": "MAX(184I, 184V)"},
            "score_term has no score assignments",
        ),
    ],
)
def test_load_hivdb_score_rule_inventory_rejects_score_term_statistic_drift(
    tmp_path,
    overrides,
    message,
):
    path = tmp_path / "hivdb_algorithm_terms.tsv"
    write_score_rule_report(path, [hivdb_score_rule_row(**overrides)])

    with pytest.raises(ValueError, match=message):
        load_hivdb_score_rule_inventory(path)


@pytest.mark.parametrize(
    ("overrides", "message"),
    [
        ({"mapping_status": "COMBINATION"}, "mapping_status must be 'EXACT'"),
        ({"drug_class": "EI"}, "EI.*no score-rule gene mapping"),
        ({"gene": "PR"}, "gene must be 'RT'"),
        ({"source_rule_id": "hivdb_hivfacts:stale"}, "source_rule_id must be"),
        ({"score_term_index": "02"}, "score_term_index must use canonical"),
        ({"score_assignments": "0"}, "score_assignments must be at least 1"),
        (
            {"negative_score_assignments": "3"},
            "negative_score_assignments exceeds score_assignments",
        ),
        ({"min_score": "16.0"}, "min_score exceeds max_score"),
    ],
)
def test_load_hivdb_score_rule_inventory_rejects_malformed_rows(
    tmp_path,
    overrides,
    message,
):
    path = tmp_path / "hivdb_algorithm_terms.tsv"
    write_score_rule_report(path, [hivdb_score_rule_row(**overrides)])

    with pytest.raises(ValueError, match=message):
        load_hivdb_score_rule_inventory(path)


def test_attach_hivdb_score_rules_writes_source_rules(tmp_path, monkeypatch):
    path = tmp_path / "hivdb_algorithm_terms.tsv"
    row = hivdb_score_rule_row()
    write_score_rule_report(path, [row])
    monkeypatch.setattr(seed_from_sources, "HIVDB_SCORE_RULE_INVENTORY", path)
    records = {
        "CHEBI:421707": {
            "identifier": "CHEBI:421707",
            "chemical_structure": {"standard_inchi_key": "MCI"},
        }
    }

    counts = attach_hivdb_score_rules(records)

    assert counts["matched_rules"] == 1
    assert counts["matched_records"] == 1
    rule = records["CHEBI:421707"]["genotype_resistance_score_rules"][0]
    assert rule["pathogen_label"] == "Human immunodeficiency virus 1"
    assert rule["gene"] == "RT"
    assert rule["source"] == HIVDB_SCORE_RULE_SOURCE
    assert rule["source_version"] == row["source_version"]
    assert rule["source_rule_id"] == row["source_rule_id"]
    assert rule["score_term"] == "MAX(184I => 15, 184V => 15)"
    assert rule["score_assignments"] == 2
    assert rule["evidence"] == [
        {
            "reference": "https://github.com/hivdb/hivfacts",
            "notes": (
                "Stanford HIVDB hivfacts "
                "be1c11a5145fea9073fdb71801919d4a34265336 "
                "HIVDB 10.2 ABC score term 2: MAX(184I => 15, 184V => 15)"
            ),
        }
    ]


def test_attach_hivdb_score_rules_noops_without_inventory(tmp_path, monkeypatch):
    monkeypatch.setattr(
        seed_from_sources,
        "HIVDB_SCORE_RULE_INVENTORY",
        tmp_path / "missing.tsv",
    )
    records = {
        "CHEBI:421707": {
            "identifier": "CHEBI:421707",
            "chemical_structure": {"standard_inchi_key": "MCI"},
        }
    }

    counts = attach_hivdb_score_rules(records)

    assert counts["missing_inventory"] == 1
    assert records == {
        "CHEBI:421707": {
            "identifier": "CHEBI:421707",
            "chemical_structure": {"standard_inchi_key": "MCI"},
        }
    }


@pytest.mark.parametrize(
    ("row_overrides", "records", "message"),
    [
        (
            {},
            {
                "CHEBI:421707": {
                    "identifier": "CHEBI:421707",
                    "chemical_structure": {"standard_inchi_key": "STALE"},
                },
            },
            "mapped InChIKey MCI does not match CHEBI:421707",
        ),
        (
            {"identifier": "CHEBI:999999", "standard_inchi_key": "STALE"},
            {},
            "mapped identifier CHEBI:999999 is not in the corpus",
        ),
    ],
)
def test_attach_hivdb_score_rules_rejects_identity_drift(
    tmp_path,
    monkeypatch,
    row_overrides,
    records,
    message,
):
    path = tmp_path / "hivdb_algorithm_terms.tsv"
    write_score_rule_report(path, [hivdb_score_rule_row(**row_overrides)])
    monkeypatch.setattr(seed_from_sources, "HIVDB_SCORE_RULE_INVENTORY", path)

    with pytest.raises(ValueError, match=message):
        attach_hivdb_score_rules(records)


def test_hivdb_score_rules_are_closed_schema_valid():
    errors = validate_antibiotic(
        {
            "identifier": "CHEBI:421707",
            "label": "abacavir",
            "antimicrobial_class": "ANTIVIRAL",
            "curation_status": "SEEDED",
            "chemical_structure": {
                "standard_inchi_key": "MCGSCOLBFJQGHM-SCZZXKLOSA-N",
                "smiles": "C",
            },
            "grounding_status": "EXACT",
            "source_concepts": [
                {
                    "source": "CHEBI",
                    "source_id": "CHEBI:421707",
                    "source_label": "abacavir",
                    "minted_identifier": "antibioticmech:chebi-1",
                    "source_version": "2026-09-28",
                }
            ],
            "genotype_resistance_score_rules": [
                {
                    "pathogen_label": "Human immunodeficiency virus 1",
                    "gene": "RT",
                    "drug_class": "NRTI",
                    "algorithm_name": "HIVDB",
                    "algorithm_version": "10.2",
                    "algorithm_date": "2026-04-26",
                    "source_record_id": "ABC",
                    "source_rule_id": "hivdb_hivfacts:2b1a0df7a38caec7",
                    "score_term_index": 2,
                    "score_term": "MAX(184I => 15, 184V => 15)",
                    "score_assignments": 2,
                    "negative_score_assignments": 0,
                    "min_score": 15.0,
                    "max_score": 15.0,
                    "source": HIVDB_SCORE_RULE_SOURCE,
                    "source_version": "be1c11a5145fea9073fdb71801919d4a34265336",
                    "evidence": [
                        {
                            "reference": "https://github.com/hivdb/hivfacts",
                            "notes": "HIVDB score term.",
                        }
                    ],
                }
            ],
        }
    )

    assert errors == []


def test_reseed_replaces_only_the_hivdb_score_rule_slice():
    new_hivdb = {
        "pathogen_label": "Human immunodeficiency virus 1",
        "gene": "RT",
        "drug_class": "NRTI",
        "algorithm_name": "HIVDB",
        "algorithm_version": "10.2",
        "algorithm_date": "2026-04-26",
        "source_record_id": "ABC",
        "source_rule_id": "hivdb_hivfacts:new",
        "score_term_index": 1,
        "score_term": "65R => -10",
        "score_assignments": 1,
        "negative_score_assignments": 1,
        "min_score": -10.0,
        "max_score": -10.0,
        "source": HIVDB_SCORE_RULE_SOURCE,
        "source_version": "be1c11a5145fea9073fdb71801919d4a34265336",
        "evidence": [{"reference": "https://github.com/hivdb/hivfacts"}],
    }
    old_hivdb = new_hivdb | {"source_rule_id": "hivdb_hivfacts:stale"}
    curated = new_hivdb | {
        "source": "CURATOR",
        "source_rule_id": "curator:hivdb-score-rule",
    }
    base = {"identifier": "CHEBI:421707"}
    fresh = base | {"genotype_resistance_score_rules": [new_hivdb]}
    existing = base | {"genotype_resistance_score_rules": [old_hivdb, curated]}

    merged = merge_with_existing(fresh, existing)

    assert hivdb_sourced_score_rule_view(merged) == [new_hivdb]
    assert merged["genotype_resistance_score_rules"] == [new_hivdb, curated]
