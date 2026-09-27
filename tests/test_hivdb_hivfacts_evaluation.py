"""Unit tests for the non-writing Stanford HIVDB hivfacts evaluator."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from evaluate_hivdb_hivfacts import (  # noqa: E402
    corpus_name_candidates,
    evaluate_drugs,
    read_drugs,
    write_drug_report,
)

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "evaluate_hivdb_hivfacts.py"


def test_evaluate_drugs_reports_exact_and_boosted_identity_matches():
    rows = [
        {
            "source_record_id": "ABC",
            "display_abbr": "ABC",
            "name": "ABC",
            "full_name": "abacavir",
            "drug_class": "NRTI",
            "synonyms": "",
        },
        {
            "source_record_id": "ATV/r",
            "display_abbr": "ATV/r",
            "name": "ATV",
            "full_name": "atazanavir/r",
            "drug_class": "PI",
            "synonyms": "",
        },
        {
            "source_record_id": "TDF",
            "display_abbr": "TDF",
            "name": "TDF",
            "full_name": "tenofovir",
            "drug_class": "NRTI",
            "synonyms": "",
        },
    ]

    result = evaluate_drugs(
        rows,
        {
            "abacavir": {"CHEBI:421707"},
            "tenofovir": {"CHEBI:63713", "CHEBI:192161"},
        },
        {
            "CHEBI:421707": "ABC",
            "CHEBI:63713": "TDF-ONE",
            "CHEBI:192161": "TDF-TWO",
        },
    )

    assert result["hivdb_drugs"] == 3
    assert result["exact_name_matched_drugs"] == 1
    assert result["ambiguous_name_drugs"] == 1
    assert result["unmatched_drugs"] == 1
    assert result["ritonavir_boosted_drugs"] == 1
    assert result["drug_classes"] == {"NRTI": 2, "PI": 1}

    boosted = result["drug_rows"][1]
    assert boosted["display_abbr"] == "ATV/r"
    assert boosted["ritonavir_boosted"] == "true"
    assert boosted["exact_name_candidate_count"] == 0


def test_read_drugs_validates_hivfacts_drug_abbreviations(tmp_path):
    path = tmp_path / "drugs.json"
    path.write_text(
        json.dumps(
            [
                {
                    "displayAbbr": "LEN",
                    "drugClass": "CAI",
                    "fullName": "lenacapavir",
                    "name": "LEN",
                },
                {
                    "displayAbbr": "LEN",
                    "drugClass": "CAI",
                    "fullName": "lenacapavir",
                    "name": "LEN2",
                },
            ]
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="duplicate HIVDB drug abbreviation LEN"):
        read_drugs(path)


def test_read_drugs_rejects_non_string_synonyms(tmp_path):
    path = tmp_path / "drugs.json"
    path.write_text(
        json.dumps(
            [
                {
                    "displayAbbr": "DTG",
                    "drugClass": "INSTI",
                    "fullName": "dolutegravir",
                    "name": "DTG",
                    "synonyms": [7],
                }
            ]
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="DTG synonym 1 is not a string"):
        read_drugs(path)


def test_corpus_name_candidates_include_record_labels_and_synonyms(tmp_path):
    directory = tmp_path / "data" / "antibiotics" / "antiviral"
    directory.mkdir(parents=True)
    record = {
        "identifier": "CHEBI:421707",
        "label": "abacavir",
        "chemical_structure": {"standard_inchi_key": "MCI"},
        "synonyms": [{"synonym_text": "ABC"}],
    }
    (directory / "abacavir.yaml").write_text(yaml.safe_dump(record), encoding="utf-8")

    candidates, structure_keys = corpus_name_candidates(tmp_path)

    assert candidates["abacavir"] == {"CHEBI:421707"}
    assert candidates["abc"] == {"CHEBI:421707"}
    assert structure_keys == {"CHEBI:421707": "MCI"}


def test_write_drug_report_preserves_hivdb_identity_columns(tmp_path):
    path = tmp_path / "hivdb_drug_report.tsv"

    write_drug_report(
        [
            {
                "source_record_id": "ABC",
                "display_abbr": "ABC",
                "name": "ABC",
                "full_name": "abacavir",
                "drug_class": "NRTI",
                "ritonavir_boosted": "false",
                "synonyms": "",
                "exact_name_candidate_count": 1,
                "exact_name_candidate_identifiers": "CHEBI:421707",
                "exact_name_candidate_inchi_keys": "MCI",
                "matched_aliases": "abacavir",
            }
        ],
        path,
    )

    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))

    assert rows == [
        {
            "source_record_id": "ABC",
            "display_abbr": "ABC",
            "name": "ABC",
            "full_name": "abacavir",
            "drug_class": "NRTI",
            "ritonavir_boosted": "false",
            "synonyms": "",
            "exact_name_candidate_count": "1",
            "exact_name_candidate_identifiers": "CHEBI:421707",
            "exact_name_candidate_inchi_keys": "MCI",
            "matched_aliases": "abacavir",
        }
    ]


def test_cli_writes_non_seeding_drug_audit(tmp_path):
    directory = tmp_path / "data" / "antibiotics" / "antiviral"
    directory.mkdir(parents=True)
    record = {
        "identifier": "CHEBI:421707",
        "label": "abacavir",
        "chemical_structure": {"standard_inchi_key": "MCI"},
    }
    (directory / "abacavir.yaml").write_text(yaml.safe_dump(record), encoding="utf-8")

    drugs = tmp_path / "drugs.json"
    drugs.write_text(
        json.dumps(
            [
                {
                    "displayAbbr": "ABC",
                    "drugClass": "NRTI",
                    "fullName": "abacavir",
                    "name": "ABC",
                }
            ]
        ),
        encoding="utf-8",
    )
    report = tmp_path / "hivdb.tsv"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--drugs",
            str(drugs),
            "--drug-report",
            str(report),
            "--corpus-root",
            str(tmp_path),
        ],
        check=True,
        cwd=Path(__file__).resolve().parents[1],
        text=True,
        capture_output=True,
    )

    assert report.exists()
    assert "Stanford HIVDB hivfacts drug identity audit" in result.stdout
    assert "no rows seeded" in result.stdout
