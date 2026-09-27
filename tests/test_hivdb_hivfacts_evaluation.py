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
    DRUG_MAP_COLUMNS,
    corpus_name_candidates,
    evaluate_drugs,
    read_drug_map,
    read_drugs,
    write_drug_map_template,
    write_drug_report,
)

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "evaluate_hivdb_hivfacts.py"


def hivdb_source_rows() -> list[dict[str, str]]:
    return [
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
    ]


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


def test_evaluate_drugs_adds_curated_mapping_fields():
    result = evaluate_drugs(
        hivdb_source_rows(),
        {"abacavir": {"CHEBI:421707"}},
        {"CHEBI:421707": "MCI"},
        mappings={
            "ABC": {
                "mapping_status": "EXACT",
                "identifier": "CHEBI:421707",
                "standard_inchi_key": "MCI",
                "mapping_basis": "full_name",
                "notes": "HIVDB fullName is the exact corpus label.",
            }
        },
    )

    assert result["drug_rows"][0]["mapping_status"] == "EXACT"
    assert result["drug_rows"][0]["identifier"] == "CHEBI:421707"
    assert result["drug_rows"][0]["mapping_notes"] == "HIVDB fullName is the exact corpus label."
    assert result["drug_rows"][1]["mapping_status"] == ""


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


def test_read_drug_map_accepts_exact_and_non_exact_rows(tmp_path):
    path = tmp_path / "hivdb_drug_map.tsv"
    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + "\n".join(
            [
                "ABC\t abacavir \tABC\tNRTI\tEXACT\tCHEBI:421707\t"
                "MCI\tfull_name\tHIVDB fullName is the exact corpus label.",
                "ATV/r\tatazanavir/r\tATV\tPI\tCOMBINATION\t\t\t"
                "ritonavir_boosted\tBoosted protease-inhibitor row.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    mappings = read_drug_map(path, {"CHEBI:421707": "MCI"}, hivdb_source_rows())

    assert mappings["ABC"]["identifier"] == "CHEBI:421707"
    assert mappings["ABC"]["source_name"] == "abacavir"
    assert mappings["ATV/r"]["mapping_status"] == "COMBINATION"
    assert mappings["ATV/r"]["identifier"] == ""


def test_read_drug_map_rejects_identity_drift(tmp_path):
    path = tmp_path / "hivdb_drug_map.tsv"
    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + "ABC\tabacavir sulfate\tABC\tNRTI\tEXACT\tCHEBI:421707\t"
        + "MCI\tfull_name\twrong salt\n"
        + "ATV/r\tatazanavir/r\tATV\tPI\tCOMBINATION\t\t\t"
        + "ritonavir_boosted\tBoosted protease-inhibitor row.\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="mapped source_name 'abacavir sulfate'"):
        read_drug_map(path, {"CHEBI:421707": "MCI"}, hivdb_source_rows())

    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + "ABC\tabacavir\tABC\tNRTI\tEXACT\tCHEBI:421707\t"
        + "WRONGINCHIKEY\tfull_name\twrong structure\n"
        + "ATV/r\tatazanavir/r\tATV\tPI\tCOMBINATION\t\t\t"
        + "ritonavir_boosted\tBoosted protease-inhibitor row.\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="does not match CHEBI:421707"):
        read_drug_map(path, {"CHEBI:421707": "MCI"}, hivdb_source_rows())


def test_read_drug_map_rejects_stale_and_incomplete_maps(tmp_path):
    path = tmp_path / "hivdb_drug_map.tsv"
    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + "ABC\tabacavir\tABC\tNRTI\tEXACT\tCHEBI:421707\t"
        + "MCI\tfull_name\tok\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="missing=\\['ATV/r'\\] extra=\\[\\]"):
        read_drug_map(path, {"CHEBI:421707": "MCI"}, hivdb_source_rows())

    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + "ABC\tabacavir\tABC\tNRTI\tEXACT\tCHEBI:421707\t"
        + "MCI\tfull_name\tok\n"
        + "ATV/r\tatazanavir/r\tATV\tPI\tCOMBINATION\t\t\t"
        + "ritonavir_boosted\tBoosted protease-inhibitor row.\n"
        + "OLD\toldavir\tOLD\tNRTI\tMISSING_CORPUS_RECORD\t\t\tmissing\tstale\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="missing=\\[\\] extra=\\['OLD'\\]"):
        read_drug_map(path, {"CHEBI:421707": "MCI"}, hivdb_source_rows())


def test_read_drug_map_rejects_non_exact_structure_fields(tmp_path):
    path = tmp_path / "hivdb_drug_map.tsv"
    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + "ABC\tabacavir\tABC\tNRTI\tMISSING_CORPUS_RECORD\tCHEBI:421707\t"
        + "MCI\tmissing\twrong\n"
        + "ATV/r\tatazanavir/r\tATV\tPI\tCOMBINATION\t\t\t"
        + "ritonavir_boosted\tBoosted protease-inhibitor row.\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="non-EXACT mapping must not carry structure fields"):
        read_drug_map(path, {"CHEBI:421707": "MCI"}, hivdb_source_rows())


def test_write_drug_map_template_preserves_hivdb_source_columns(tmp_path):
    path = tmp_path / "hivdb_drug_map.tsv"
    write_drug_map_template(
        [
            {
                "source_record_id": "ABC",
                "display_abbr": "ABC",
                "name": "ABC",
                "full_name": "abacavir",
                "drug_class": "NRTI",
                "mapping_status": "",
                "identifier": "",
                "standard_inchi_key": "",
                "mapping_basis": "",
                "mapping_notes": "",
            }
        ],
        path,
    )

    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))

    assert rows == [
        {
            "source_record_id": "ABC",
            "source_name": "abacavir",
            "hivdb_name": "ABC",
            "drug_class": "NRTI",
            "mapping_status": "",
            "identifier": "",
            "standard_inchi_key": "",
            "mapping_basis": "",
            "notes": "",
        }
    ]


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
                "mapping_status": "",
                "identifier": "",
                "standard_inchi_key": "",
                "mapping_basis": "",
                "mapping_notes": "",
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
            "mapping_status": "",
            "identifier": "",
            "standard_inchi_key": "",
            "mapping_basis": "",
            "mapping_notes": "",
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
    drug_map = tmp_path / "hivdb_drug_map_in.tsv"
    drug_map.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + "ABC\tabacavir\tABC\tNRTI\tEXACT\tCHEBI:421707\t"
        + "MCI\tfull_name\tHIVDB fullName is the exact corpus label.\n",
        encoding="utf-8",
    )
    drug_map_template = tmp_path / "hivdb_drug_map.tsv"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--drugs",
            str(drugs),
            "--drug-report",
            str(report),
            "--drug-map",
            str(drug_map),
            "--drug-map-template",
            str(drug_map_template),
            "--corpus-root",
            str(tmp_path),
        ],
        check=True,
        cwd=Path(__file__).resolve().parents[1],
        text=True,
        capture_output=True,
    )

    assert report.exists()
    assert drug_map_template.exists()
    with report.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert rows[0]["mapping_status"] == "EXACT"
    assert rows[0]["identifier"] == "CHEBI:421707"
    assert "Stanford HIVDB hivfacts drug identity audit" in result.stdout
    assert "no rows seeded" in result.stdout
