"""Unit tests for the non-writing BacDive activity evaluator."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from evaluate_bacdive_activity import (  # noqa: E402
    DRUG_MAP_COLUMNS,
    DRUG_REPORT_COLUMNS,
    corpus_name_candidates,
    evaluate_records,
    read_bacdive_fetch,
    write_drug_map_template,
    write_drug_report,
)

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "evaluate_bacdive_activity.py"


def bacdive_record() -> dict:
    return {
        "General": {"BacDive-ID": 24493},
        "Name and taxonomic classification": {
            "species": "Phaeobacter gallaeciensis",
            "strain designation": "BS 107",
        },
        "Physiology and metabolism": {
            "antibiotic resistance": [
                {
                    "@ref": 119508,
                    "Chebi-ID": "chebi:28971",
                    "metabolite": "ampicillin",
                    "is sensitive": "no",
                    "is resistant": "yes",
                },
                {
                    "@ref": 119508,
                    "metabolite": "quinupristin/dalfopristin",
                    "is sensitive": "yes",
                    "is resistant": "no",
                },
            ],
            "antibiogram": {
                "@ref": 119508,
                "Medium_antibiogramV2": "Mueller Hinton",
                "AMP_antibiogramV2": 18,
                "CAZ_antibiogramV2": "17.0",
                "SXT_antibiogramV2": 0,
                "CIP_antibiogramV2": "trace",
            },
        },
    }


def write_corpus_record(root: Path) -> None:
    path = root / "data" / "antibiotics" / "antibacterial" / "ampicillin.yaml"
    path.parent.mkdir(parents=True)
    path.write_text(
        """
identifier: CHEBI:28971
label: Ampicillin
chemical_structure:
  standard_inchi_key: AVKUERGKIZMTKX-NJBDSQKTSA-N
synonyms:
  - synonym_text: D-(-)-alpha-Aminobenzylpenicillin
""".lstrip(),
        encoding="utf-8",
    )


def report_rows(tmp_path: Path) -> list[dict[str, str]]:
    write_corpus_record(tmp_path)
    name_candidates, structure_keys = corpus_name_candidates(tmp_path)
    return evaluate_records(
        {"24493": bacdive_record()},
        name_candidates,
        structure_keys,
    )


def test_evaluate_records_summarizes_met_antibiotica_and_disk_columns(tmp_path):
    rows = report_rows(tmp_path)

    assert [row["source_record_id"] for row in rows] == [
        "ampicillin",
        "ceftazidime",
        "ciprofloxacin",
        "quinupristindalfopristin",
        "trimethoprimsulfamethoxazole119",
    ]
    assert rows[0] == {
        "source_record_id": "ampicillin",
        "source_name": "Ampicillin",
        "normalized_source_name": "ampicillin",
        "source_sections": "met_antibiogram_v2|met_antibiotica",
        "bacdive_row_count": "2",
        "bacdive_id_count": "1",
        "bacdive_ids": "24493",
        "activity_call_count": "1",
        "activity_calls": "RESISTANT:1",
        "disk_diffusion_count": "1",
        "invalid_disk_diffusion_count": "0",
        "standardized_disk_diffusion_values": "18 mm",
        "source_chebi_ids": "CHEBI:28971",
        "exact_name_candidate_count": "1",
        "exact_name_candidate_identifiers": "CHEBI:28971",
        "exact_name_candidate_inchi_keys": "AVKUERGKIZMTKX-NJBDSQKTSA-N",
        "mapping_status": "",
        "identifier": "",
        "standard_inchi_key": "",
        "mapping_basis": "",
        "mapping_notes": "",
    }
    assert rows[1]["source_name"] == "Ceftazidime"
    assert rows[1]["source_sections"] == "met_antibiogram_v2"
    assert rows[1]["disk_diffusion_count"] == "1"
    assert rows[1]["standardized_disk_diffusion_values"] == "17 mm"
    assert rows[2]["source_name"] == "Ciprofloxacin"
    assert rows[2]["disk_diffusion_count"] == "0"
    assert rows[2]["invalid_disk_diffusion_count"] == "1"
    assert rows[3]["source_name"] == "quinupristin/dalfopristin"
    assert rows[3]["activity_calls"] == "SUSCEPTIBLE:1"
    assert rows[4]["disk_diffusion_count"] == "0"
    assert rows[4]["invalid_disk_diffusion_count"] == "1"


def test_read_bacdive_fetch_accepts_v2_results_objects(tmp_path):
    path = tmp_path / "bacdive.json"
    path.write_text(
        json.dumps({"count": 1, "next": None, "previous": None, "results": {"24493": bacdive_record()}}),
        encoding="utf-8",
    )

    assert read_bacdive_fetch(path) == {"24493": bacdive_record()}


def test_read_bacdive_fetch_accepts_single_record_objects(tmp_path):
    path = tmp_path / "bacdive.json"
    path.write_text(json.dumps(bacdive_record()), encoding="utf-8")

    assert read_bacdive_fetch(path) == {"24493": bacdive_record()}


def test_write_drug_report_and_map_template(tmp_path):
    rows = report_rows(tmp_path)
    report = tmp_path / "bacdive_antibiotics.tsv"
    template = tmp_path / "bacdive_drug_map.tsv"

    write_drug_report(rows, report)
    write_drug_map_template(rows, template, "2026-10-02-v2-fetch")

    with report.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        assert reader.fieldnames == DRUG_REPORT_COLUMNS
        assert [row["source_record_id"] for row in reader] == [
            "ampicillin",
            "ceftazidime",
            "ciprofloxacin",
            "quinupristindalfopristin",
            "trimethoprimsulfamethoxazole119",
        ]

    with template.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        assert reader.fieldnames == DRUG_MAP_COLUMNS
        template_rows = list(reader)

    assert template_rows[0] == {
        "source_version": "2026-10-02-v2-fetch",
        "source_record_id": "ampicillin",
        "source_name": "Ampicillin",
        "mapping_status": "",
        "identifier": "",
        "standard_inchi_key": "",
        "mapping_basis": "",
        "notes": "",
    }


def test_cli_writes_bacdive_reports(tmp_path):
    path = tmp_path / "bacdive.json"
    report = tmp_path / "bacdive_antibiotics.tsv"
    template = tmp_path / "bacdive_drug_map.tsv"
    path.write_text(
        json.dumps({"results": {"24493": bacdive_record()}}),
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--bacdive",
            str(path),
            "--source-version",
            "2026-10-02-v2-fetch",
            "--drug-report",
            str(report),
            "--drug-map-template",
            str(template),
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert result.stdout.startswith("BacDive activity preflight: records=1 ")
    assert report.exists()
    assert template.exists()
