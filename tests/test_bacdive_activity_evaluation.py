"""Unit tests for the non-writing BacDive activity evaluator."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from evaluate_bacdive_activity import (  # noqa: E402
    DRUG_MAP_COLUMNS,
    DRUG_REPORT_COLUMNS,
    corpus_name_candidates,
    evaluate_records,
    read_bacdive_fetch,
    read_drug_map,
    write_drug_map_template,
    write_drug_report,
)

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "evaluate_bacdive_activity.py"
SOURCE_VERSION = "2026-10-02-v2-fetch"
AMPICILLIN_INCHI_KEY = "AVKUERGKIZMTKX-NJBDSQKTSA-N"


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
  standard_inchi_key: {AMPICILLIN_INCHI_KEY}
synonyms:
  - synonym_text: D-(-)-alpha-Aminobenzylpenicillin
""".lstrip().format(AMPICILLIN_INCHI_KEY=AMPICILLIN_INCHI_KEY),
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


def bacdive_drug_map_row(**overrides: str) -> dict[str, str]:
    row = {
        "source_version": SOURCE_VERSION,
        "source_record_id": "ampicillin",
        "source_name": "Ampicillin",
        "mapping_status": "EXACT",
        "identifier": "CHEBI:28971",
        "standard_inchi_key": AMPICILLIN_INCHI_KEY,
        "mapping_basis": "exact_name",
        "notes": "BacDive names the exact ampicillin corpus record.",
    }
    row.update(overrides)
    return row


def write_drug_map(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=DRUG_MAP_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def test_read_drug_map_accepts_exact_and_non_exact_rows(tmp_path):
    write_corpus_record(tmp_path)
    name_candidates, structure_keys = corpus_name_candidates(tmp_path)
    rows = evaluate_records(
        {"24493": bacdive_record()},
        name_candidates,
        structure_keys,
    )
    path = tmp_path / "bacdive_drug_map.tsv"
    write_drug_map(
        path,
        [
            bacdive_drug_map_row(),
            bacdive_drug_map_row(
                source_record_id="trimethoprimsulfamethoxazole119",
                source_name="Trimethoprim-sulfamethoxazole (1:19)",
                mapping_status="COMBINATION",
                identifier="",
                standard_inchi_key="",
                mapping_basis="none",
                notes="Fixed trimethoprim and sulfamethoxazole combination.",
            ),
        ],
    )

    mappings = read_drug_map(
        path,
        structure_keys,
        rows,
        source_version=SOURCE_VERSION,
    )
    mapped_rows = evaluate_records(
        {"24493": bacdive_record()},
        name_candidates,
        structure_keys,
        mappings,
    )
    mapped_by_id = {row["source_record_id"]: row for row in mapped_rows}

    assert mapped_by_id["ampicillin"]["mapping_status"] == "EXACT"
    assert mapped_by_id["ampicillin"]["identifier"] == "CHEBI:28971"
    assert mapped_by_id["ampicillin"]["standard_inchi_key"] == AMPICILLIN_INCHI_KEY
    assert mapped_by_id["ampicillin"]["mapping_basis"] == "exact_name"
    assert mapped_by_id["ampicillin"]["mapping_notes"] == "BacDive names the exact ampicillin corpus record."
    assert mapped_by_id["trimethoprimsulfamethoxazole119"]["mapping_status"] == "COMBINATION"
    assert mapped_by_id["trimethoprimsulfamethoxazole119"]["identifier"] == ""


@pytest.mark.parametrize(
    ("overrides", "match"),
    [
        (
            {"source_version": "2026-10-01-v2-fetch"},
            "source_version '2026-10-01-v2-fetch'",
        ),
        ({"mapping_status": ""}, "mapping_status is required"),
        ({"mapping_status": "NOT_EXACT"}, "unknown mapping_status 'NOT_EXACT'"),
        ({"identifier": ""}, "EXACT mapping needs identifier and standard_inchi_key"),
        ({"standard_inchi_key": ""}, "EXACT mapping needs identifier"),
        ({"mapping_basis": ""}, "mapping_basis is required"),
        ({"notes": ""}, "notes is required"),
        (
            {"mapping_status": "MIXTURE"},
            "non-EXACT mapping must not carry structure fields",
        ),
        ({"source_name": "ampicillin sodium"}, "source_name 'ampicillin sodium'"),
        (
            {"source_record_id": "ghost", "source_name": "Ghost"},
            "is not in the current BacDive report",
        ),
        ({"standard_inchi_key": "WRONGINCHIKEY"}, "does not match CHEBI:28971"),
        ({"notes": "line\nbreak"}, "notes contains a tab or newline"),
    ],
)
def test_read_drug_map_rejects_stale_or_malformed_rows(
    tmp_path,
    overrides,
    match,
):
    path = tmp_path / "bacdive_drug_map.tsv"
    write_drug_map(path, [bacdive_drug_map_row(**overrides)])

    with pytest.raises(ValueError, match=match):
        read_drug_map(
            path,
            {"CHEBI:28971": AMPICILLIN_INCHI_KEY},
            report_rows(tmp_path),
            source_version=SOURCE_VERSION,
        )


def test_read_drug_map_rejects_duplicate_source_record_ids(tmp_path):
    path = tmp_path / "bacdive_drug_map.tsv"
    write_drug_map(
        path,
        [
            bacdive_drug_map_row(),
            bacdive_drug_map_row(notes="duplicate"),
        ],
    )

    with pytest.raises(ValueError, match="duplicate BacDive drug mapping: ampicillin"):
        read_drug_map(
            path,
            {"CHEBI:28971": AMPICILLIN_INCHI_KEY},
            report_rows(tmp_path),
            source_version=SOURCE_VERSION,
        )


def test_read_drug_map_rejects_header_only_maps(tmp_path):
    path = tmp_path / "bacdive_drug_map.tsv"
    write_drug_map(path, [])

    with pytest.raises(ValueError, match="BacDive drug map has no rows"):
        read_drug_map(
            path,
            {"CHEBI:28971": AMPICILLIN_INCHI_KEY},
            report_rows(tmp_path),
            source_version=SOURCE_VERSION,
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
    write_drug_map_template(rows, template, SOURCE_VERSION)

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
        "source_version": SOURCE_VERSION,
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
            SOURCE_VERSION,
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


def test_cli_reads_drug_map_without_prefilling_template(tmp_path):
    path = tmp_path / "bacdive.json"
    drug_map = tmp_path / "bacdive_drug_map.tsv"
    report = tmp_path / "bacdive_antibiotics.tsv"
    template = tmp_path / "bacdive_drug_map_template.tsv"
    path.write_text(
        json.dumps({"results": {"24493": bacdive_record()}}),
        encoding="utf-8",
    )
    write_drug_map(drug_map, [bacdive_drug_map_row()])

    subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--bacdive",
            str(path),
            "--source-version",
            SOURCE_VERSION,
            "--drug-map",
            str(drug_map),
            "--drug-report",
            str(report),
            "--drug-map-template",
            str(template),
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    with report.open(newline="", encoding="utf-8") as handle:
        report_rows_by_id = {row["source_record_id"]: row for row in csv.DictReader(handle, delimiter="\t")}
    with template.open(newline="", encoding="utf-8") as handle:
        template_rows_by_id = {row["source_record_id"]: row for row in csv.DictReader(handle, delimiter="\t")}

    assert report_rows_by_id["ampicillin"]["mapping_status"] == "EXACT"
    assert report_rows_by_id["ampicillin"]["identifier"] == "CHEBI:28971"
    assert template_rows_by_id["ampicillin"]["mapping_status"] == ""
    assert template_rows_by_id["ampicillin"]["identifier"] == ""


def test_cli_rejects_drug_map_without_source_version(tmp_path):
    path = tmp_path / "bacdive.json"
    path.write_text(json.dumps({"results": {"24493": bacdive_record()}}), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--bacdive",
            str(path),
            "--drug-map",
            str(tmp_path / "bacdive_drug_map.tsv"),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "--drug-map and --drug-map-template require --source-version" in result.stderr


def test_cli_rejects_drug_map_template_over_curated_drug_map(tmp_path):
    path = tmp_path / "bacdive.json"
    drug_map = tmp_path / "bacdive_drug_map.tsv"
    path.write_text(json.dumps({"results": {"24493": bacdive_record()}}), encoding="utf-8")
    drug_map.write_text("keep curated map\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--bacdive",
            str(path),
            "--source-version",
            SOURCE_VERSION,
            "--drug-map",
            str(drug_map),
            "--drug-map-template",
            str(drug_map),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "--drug-map-template must not reuse --drug-map path" in result.stderr
    assert drug_map.read_text(encoding="utf-8") == "keep curated map\n"
