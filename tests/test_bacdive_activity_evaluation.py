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
    ACTIVITY_REPORT_COLUMNS,
    DRUG_MAP_COLUMNS,
    DRUG_REPORT_COLUMNS,
    corpus_name_candidates,
    evaluate_records,
    exact_activity_rows,
    merge_bacdive_records,
    read_activity_report,
    read_bacdive_fetch,
    read_drug_map,
    require_activity_report_matches_current,
    require_standard_inchi_key,
    source_activity_id,
    write_activity_report,
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
                    "concentration": "10 mg/L",
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


def write_raw_activity_report(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=ACTIVITY_REPORT_COLUMNS,
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


def test_exact_activity_rows_preserve_exact_mapped_bacdive_context(tmp_path):
    mappings = {
        "ampicillin": bacdive_drug_map_row(),
        "trimethoprimsulfamethoxazole119": bacdive_drug_map_row(
            source_record_id="trimethoprimsulfamethoxazole119",
            source_name="Trimethoprim-sulfamethoxazole (1:19)",
            mapping_status="COMBINATION",
            identifier="",
            standard_inchi_key="",
            mapping_basis="none",
            notes="Fixed trimethoprim and sulfamethoxazole combination.",
        ),
    }

    rows = exact_activity_rows(
        {"24493": bacdive_record()},
        mappings,
        SOURCE_VERSION,
    )

    assert len(rows) == 2
    assert [row["source_section"] for row in rows] == [
        "met_antibiotica",
        "met_antibiogram_v2",
    ]
    assert {row["source_activity_id"] for row in rows} == {
        "bacdive:5038512ce05fd01f",
        "bacdive:928d8199da6513ce",
    }
    assert rows[0] == {
        "source_activity_id": "bacdive:5038512ce05fd01f",
        "source_version": SOURCE_VERSION,
        "source_record_id": "ampicillin",
        "source_name": "Ampicillin",
        "identifier": "CHEBI:28971",
        "standard_inchi_key": AMPICILLIN_INCHI_KEY,
        "bacdive_id": "24493",
        "taxon_label": "Phaeobacter gallaeciensis",
        "strain": "BS 107",
        "source_section": "met_antibiotica",
        "source_row_index": "1",
        "source_field": "metabolite",
        "source_reference_ids": "119508",
        "activity": "RESISTANT",
        "source_concentration": "10 mg/L",
        "disk_diffusion_value": "",
        "disk_diffusion_units": "",
        "assay": "",
        "medium": "",
    }
    assert rows[1] == {
        "source_activity_id": "bacdive:928d8199da6513ce",
        "source_version": SOURCE_VERSION,
        "source_record_id": "ampicillin",
        "source_name": "Ampicillin",
        "identifier": "CHEBI:28971",
        "standard_inchi_key": AMPICILLIN_INCHI_KEY,
        "bacdive_id": "24493",
        "taxon_label": "Phaeobacter gallaeciensis",
        "strain": "BS 107",
        "source_section": "met_antibiogram_v2",
        "source_row_index": "1",
        "source_field": "AMP_antibiogramV2",
        "source_reference_ids": "119508",
        "activity": "",
        "source_concentration": "",
        "disk_diffusion_value": "18",
        "disk_diffusion_units": "mm",
        "assay": "BacDive met_antibiogram_v2 disk diffusion",
        "medium": "Mueller Hinton",
    }


def test_exact_activity_rows_preserves_scalar_reference_arrays():
    record = bacdive_record()
    record["Physiology and metabolism"]["antibiotic resistance"][0]["@ref"] = [
        "119509",
        119508,
        "",
    ]

    rows = exact_activity_rows(
        {"24493": record},
        {"ampicillin": bacdive_drug_map_row()},
        SOURCE_VERSION,
    )

    assert rows[0]["source_reference_ids"] == "119508|119509"


def test_exact_activity_rows_preserves_scalar_antibiogram_reference_arrays():
    record = bacdive_record()
    record["Physiology and metabolism"]["antibiogram"]["@ref"] = [
        "119509",
        119508,
        "",
    ]

    rows = exact_activity_rows(
        {"24493": record},
        {"ampicillin": bacdive_drug_map_row()},
        SOURCE_VERSION,
    )

    assert rows[1]["source_reference_ids"] == "119508|119509"


def test_write_activity_report_rejects_stale_ids(tmp_path):
    rows = exact_activity_rows(
        {"24493": bacdive_record()},
        {"ampicillin": bacdive_drug_map_row()},
        SOURCE_VERSION,
    )
    rows[0]["source_row_index"] = "2"

    with pytest.raises(ValueError, match="source_activity_id is stale"):
        write_activity_report(rows, tmp_path / "bacdive_activity.tsv")


def test_read_activity_report_accepts_exact_activity_rows(tmp_path):
    path = tmp_path / "bacdive_activity.tsv"
    rows = exact_activity_rows(
        {"24493": bacdive_record()},
        {"ampicillin": bacdive_drug_map_row()},
        SOURCE_VERSION,
    )
    write_activity_report(rows, path)

    assert read_activity_report(
        path,
        {"CHEBI:28971": AMPICILLIN_INCHI_KEY},
        SOURCE_VERSION,
    ) == rows


def test_write_activity_report_rejects_leading_or_trailing_whitespace(tmp_path):
    rows = exact_activity_rows(
        {"24493": bacdive_record()},
        {"ampicillin": bacdive_drug_map_row()},
        SOURCE_VERSION,
    )
    rows[0]["taxon_label"] = " Phaeobacter gallaeciensis"

    with pytest.raises(ValueError, match="taxon_label has leading or trailing whitespace"):
        write_activity_report(rows, tmp_path / "bacdive_activity.tsv")


def test_write_activity_report_rejects_invalid_standard_inchi_key(tmp_path):
    rows = exact_activity_rows(
        {"24493": bacdive_record()},
        {"ampicillin": bacdive_drug_map_row()},
        SOURCE_VERSION,
    )
    rows[0]["standard_inchi_key"] = "WRONGINCHIKEY"
    rows[0]["source_activity_id"] = source_activity_id(rows[0])

    with pytest.raises(ValueError, match="invalid standard_inchi_key value"):
        write_activity_report(rows, tmp_path / "bacdive_activity.tsv")


def test_require_standard_inchi_key_rejects_trailing_newline():
    with pytest.raises(ValueError, match="invalid standard_inchi_key value"):
        require_standard_inchi_key(
            f"{AMPICILLIN_INCHI_KEY}\n",
            "standard_inchi_key",
            "bacdive_activity.tsv: row 1",
        )


def test_read_activity_report_rejects_header_drift(tmp_path):
    path = tmp_path / "bacdive_activity.tsv"
    path.write_text("source_activity_id\tunexpected\n", encoding="utf-8")

    with pytest.raises(ValueError, match="unexpected BacDive activity report columns"):
        read_activity_report(
            path,
            {"CHEBI:28971": AMPICILLIN_INCHI_KEY},
            SOURCE_VERSION,
        )


def test_read_activity_report_rejects_header_only_reports(tmp_path):
    path = tmp_path / "bacdive_activity.tsv"
    write_raw_activity_report(path, [])

    with pytest.raises(ValueError, match="BacDive activity report has no rows"):
        read_activity_report(
            path,
            {"CHEBI:28971": AMPICILLIN_INCHI_KEY},
            SOURCE_VERSION,
        )


def test_read_activity_report_rejects_short_rows(tmp_path):
    path = tmp_path / "bacdive_activity.tsv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(ACTIVITY_REPORT_COLUMNS)
        writer.writerow(["bacdive:short"])

    with pytest.raises(ValueError, match="source_version is missing"):
        read_activity_report(
            path,
            {"CHEBI:28971": AMPICILLIN_INCHI_KEY},
            SOURCE_VERSION,
        )


@pytest.mark.parametrize(
    ("overrides", "refresh_activity_id", "match"),
    [
        (
            {"source_version": "2026-10-01-v2-fetch"},
            False,
            "source_version '2026-10-01-v2-fetch'",
        ),
        ({"source_row_index": "2"}, False, "source_activity_id is stale"),
        (
            {"source_row_index": "01"},
            True,
            "source_row_index must use canonical integer",
        ),
        (
            {"identifier": "CHEBI:999999"},
            True,
            "mapped identifier CHEBI:999999 is not in the corpus",
        ),
        (
            {"standard_inchi_key": "AAAAAAAAAAAAAA-AAAAAAAAAA-A"},
            True,
            "does not match CHEBI:28971",
        ),
        (
            {"source_name": "Ampicillin sodium"},
            False,
            "source_record_id must be the normalized source_name",
        ),
        (
            {"source_record_id": "ampicillinsodium"},
            True,
            "source_record_id must be the normalized source_name",
        ),
        (
            {"source_field": "AMP_antibiogramV2"},
            True,
            "unsupported met_antibiotica source_field",
        ),
        (
            {
                "activity": "",
                "disk_diffusion_value": "18",
                "disk_diffusion_units": "mm",
                "assay": "BacDive met_antibiotica disk diffusion",
            },
            False,
            "met_antibiotica rows require activity",
        ),
        (
            {
                "disk_diffusion_value": "18",
                "disk_diffusion_units": "mm",
                "assay": "BacDive met_antibiogram_v2 disk diffusion",
                "medium": "Mueller Hinton",
            },
            False,
            "met_antibiotica rows must not carry disk-diffusion fields",
        ),
        ({"bacdive_id": "24493.0"}, True, "bacdive_id must be a positive integer"),
        (
            {"source_reference_ids": "119509|119508"},
            False,
            "source_reference_ids must be a sorted unique pipe-delimited list",
        ),
        (
            {"source_reference_ids": "119508|119508"},
            False,
            "source_reference_ids must be a sorted unique pipe-delimited list",
        ),
        (
            {"source_reference_ids": "|119508"},
            False,
            "source_reference_ids has an empty segment",
        ),
    ],
)
def test_read_activity_report_rejects_stale_or_malformed_rows(
    tmp_path,
    overrides,
    refresh_activity_id,
    match,
):
    path = tmp_path / "bacdive_activity.tsv"
    rows = exact_activity_rows(
        {"24493": bacdive_record()},
        {"ampicillin": bacdive_drug_map_row()},
        SOURCE_VERSION,
    )
    rows[0].update(overrides)
    if refresh_activity_id:
        rows[0]["source_activity_id"] = source_activity_id(rows[0])
    write_raw_activity_report(path, rows)

    with pytest.raises(ValueError, match=match):
        read_activity_report(
            path,
            {"CHEBI:28971": AMPICILLIN_INCHI_KEY},
            SOURCE_VERSION,
        )


@pytest.mark.parametrize(
    ("overrides", "match"),
    [
        ({"activity": "RESISTANT"}, "disk-diffusion rows must not carry activity"),
        (
            {"source_concentration": "10 mg/L"},
            "disk-diffusion rows must not carry source_concentration",
        ),
        ({"assay": "disk diffusion"}, "assay must be 'BacDive met_antibiogram_v2"),
        (
            {"source_field": "NOTREAL_antibiogramV2"},
            "unsupported disk-diffusion source_field",
        ),
        (
            {"source_field": "AMP_antibiogram"},
            "belongs to met_antibiogram, not met_antibiogram_v2",
        ),
        (
            {"source_field": "CAZ_antibiogramV2"},
            "maps to 'Ceftazidime', not source_name 'Ampicillin'",
        ),
    ],
)
def test_read_activity_report_rejects_malformed_disk_rows(
    tmp_path,
    overrides,
    match,
):
    path = tmp_path / "bacdive_activity.tsv"
    rows = exact_activity_rows(
        {"24493": bacdive_record()},
        {"ampicillin": bacdive_drug_map_row()},
        SOURCE_VERSION,
    )
    rows[1].update(overrides)
    rows[1]["source_activity_id"] = source_activity_id(rows[1])
    write_raw_activity_report(path, rows)

    with pytest.raises(ValueError, match=match):
        read_activity_report(
            path,
            {"CHEBI:28971": AMPICILLIN_INCHI_KEY},
            SOURCE_VERSION,
        )


def test_require_activity_report_matches_current_rejects_stale_source_values(
    tmp_path,
):
    current_rows = exact_activity_rows(
        {"24493": bacdive_record()},
        {"ampicillin": bacdive_drug_map_row()},
        SOURCE_VERSION,
    )
    stale_rows = [dict(row) for row in current_rows]
    stale_rows[0]["source_concentration"] = "20 mg/L"

    with pytest.raises(
        ValueError,
        match=(
            r"bacdive:5038512ce05fd01f source_concentration "
            r"'20 mg/L' != current BacDive '10 mg/L'"
        ),
    ):
        require_activity_report_matches_current(
            stale_rows,
            current_rows,
            tmp_path / "bacdive_activity.tsv",
        )


def test_require_activity_report_matches_current_rejects_missing_rows(tmp_path):
    current_rows = exact_activity_rows(
        {"24493": bacdive_record()},
        {"ampicillin": bacdive_drug_map_row()},
        SOURCE_VERSION,
    )

    with pytest.raises(
        ValueError,
        match="missing current BacDive activity row bacdive:928d8199da6513ce",
    ):
        require_activity_report_matches_current(
            current_rows[:1],
            current_rows,
            tmp_path / "bacdive_activity.tsv",
        )


def test_require_activity_report_matches_current_rejects_unexpected_rows(
    tmp_path,
):
    current_rows = exact_activity_rows(
        {"24493": bacdive_record()},
        {"ampicillin": bacdive_drug_map_row()},
        SOURCE_VERSION,
    )
    previous_record = bacdive_record()
    previous_record["Physiology and metabolism"]["antibiotic resistance"].append(
        {
            "metabolite": "Ampicillin",
            "concentration": "20 mg/L",
            "is resistant": "yes",
        }
    )
    stale_rows = exact_activity_rows(
        {"24493": previous_record},
        {"ampicillin": bacdive_drug_map_row()},
        SOURCE_VERSION,
    )

    with pytest.raises(
        ValueError,
        match="unexpected stale BacDive activity row bacdive:b390fefb074550b0",
    ):
        require_activity_report_matches_current(
            stale_rows,
            current_rows,
            tmp_path / "bacdive_activity.tsv",
        )


def test_require_activity_report_matches_current_rejects_duplicate_current_rows(
    tmp_path,
):
    current_rows = exact_activity_rows(
        {"24493": bacdive_record()},
        {"ampicillin": bacdive_drug_map_row()},
        SOURCE_VERSION,
    )

    with pytest.raises(ValueError, match="duplicate source_activity_id"):
        require_activity_report_matches_current(
            current_rows[:1],
            [current_rows[0], current_rows[0]],
            tmp_path / "bacdive_activity.tsv",
        )


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


def test_read_bacdive_fetch_uses_positive_integer_result_keys_as_id_fallback(tmp_path):
    path = tmp_path / "bacdive.json"
    record = bacdive_record()
    del record["General"]
    path.write_text(json.dumps({"results": {" 24493 ": record}}), encoding="utf-8")

    assert read_bacdive_fetch(path) == {"24493": record}


def test_read_bacdive_fetch_rejects_non_record_results(tmp_path):
    path = tmp_path / "bacdive.json"
    path.write_text(json.dumps({"results": {"24493": "not a record"}}), encoding="utf-8")

    with pytest.raises(ValueError, match="result 24493 is not a BacDive record object"):
        read_bacdive_fetch(path)


def test_read_bacdive_fetch_rejects_duplicate_bacdive_ids(tmp_path):
    path = tmp_path / "bacdive.json"
    path.write_text(
        json.dumps({"results": {"first": bacdive_record(), "second": bacdive_record()}}),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="duplicate BacDive-ID 24493"):
        read_bacdive_fetch(path)


def test_read_bacdive_fetch_rejects_malformed_general_section(tmp_path):
    path = tmp_path / "bacdive.json"
    record = bacdive_record()
    record["General"] = ["not metadata"]
    path.write_text(json.dumps({"results": {"24493": record}}), encoding="utf-8")

    with pytest.raises(
        ValueError,
        match="BacDive record 24493 General must be an object",
    ):
        read_bacdive_fetch(path)


def test_read_bacdive_fetch_rejects_malformed_general_bacdive_id(tmp_path):
    path = tmp_path / "bacdive.json"
    record = bacdive_record()
    record["General"]["BacDive-ID"] = {"value": 24493}
    path.write_text(json.dumps({"results": {"24493": record}}), encoding="utf-8")

    with pytest.raises(
        ValueError,
        match="BacDive record 24493 General BacDive-ID must be a scalar",
    ):
        read_bacdive_fetch(path)


@pytest.mark.parametrize("bacdive_id_value", [0, -1, True, "24493.0"])
def test_read_bacdive_fetch_rejects_malformed_scalar_general_bacdive_id(
    tmp_path,
    bacdive_id_value,
):
    path = tmp_path / "bacdive.json"
    record = bacdive_record()
    record["General"]["BacDive-ID"] = bacdive_id_value
    path.write_text(json.dumps({"results": {"24493": record}}), encoding="utf-8")

    with pytest.raises(
        ValueError,
        match="BacDive record 24493 General BacDive-ID must be a positive integer",
    ):
        read_bacdive_fetch(path)


def test_read_bacdive_fetch_rejects_single_records_without_general_bacdive_id(tmp_path):
    path = tmp_path / "bacdive.json"
    record = bacdive_record()
    record["General"] = {}
    path.write_text(json.dumps(record), encoding="utf-8")

    with pytest.raises(
        ValueError,
        match="BacDive record 1 is missing General BacDive-ID",
    ):
        read_bacdive_fetch(path)


def test_read_bacdive_fetch_rejects_list_records_without_general_bacdive_id(tmp_path):
    path = tmp_path / "bacdive.json"
    record = bacdive_record()
    del record["General"]
    path.write_text(json.dumps({"results": [record]}), encoding="utf-8")

    with pytest.raises(
        ValueError,
        match="BacDive record 1 is missing General BacDive-ID",
    ):
        read_bacdive_fetch(path)


@pytest.mark.parametrize(
    ("section_name", "section_value", "match"),
    [
        (
            "antibiotic resistance",
            ["not a row"],
            "BacDive-ID 24493 antibiotic resistance row 1 is not an object",
        ),
        (
            "antibiotic resistance",
            "not rows",
            "BacDive-ID 24493 antibiotic resistance must be an object or array",
        ),
        (
            "antibiogram",
            ["not a row"],
            "BacDive-ID 24493 antibiogram row 1 is not an object",
        ),
        (
            "antibiogram",
            "not rows",
            "BacDive-ID 24493 antibiogram must be an object or array",
        ),
    ],
)
def test_evaluate_records_rejects_malformed_activity_section_rows(
    section_name,
    section_value,
    match,
):
    record = bacdive_record()
    record["Physiology and metabolism"][section_name] = section_value

    with pytest.raises(ValueError, match=match):
        evaluate_records({"24493": record}, {}, {})


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("metabolite", ["ampicillin"]),
        ("Chebi-ID", {"value": "CHEBI:28971"}),
        ("is resistant", ["yes"]),
    ],
)
def test_evaluate_records_rejects_malformed_met_antibiotica_scalar_fields(
    field,
    value,
):
    record = bacdive_record()
    record["Physiology and metabolism"]["antibiotic resistance"][0][field] = value

    with pytest.raises(
        ValueError,
        match=f"BacDive-ID 24493 antibiotic resistance row 1 {field} must be a scalar",
    ):
        evaluate_records({"24493": record}, {}, {})


@pytest.mark.parametrize(
    ("field", "value", "match"),
    [
        (
            "concentration",
            ["10 mg/L"],
            "BacDive-ID 24493 antibiotic resistance row 1 concentration",
        ),
        (
            "@ref",
            [{"id": 119508}],
            r"BacDive-ID 24493 antibiotic resistance row 1 @ref entry 1",
        ),
        (
            "@ref",
            "119508|119509",
            r"BacDive-ID 24493 antibiotic resistance row 1 @ref "
            r"must not contain '\|'",
        ),
    ],
)
def test_exact_activity_rows_rejects_malformed_met_antibiotica_activity_fields(
    field,
    value,
    match,
):
    record = bacdive_record()
    record["Physiology and metabolism"]["antibiotic resistance"][0][field] = value

    with pytest.raises(ValueError, match=match):
        exact_activity_rows(
            {"24493": record},
            {"ampicillin": bacdive_drug_map_row()},
            SOURCE_VERSION,
        )


def test_evaluate_records_rejects_malformed_physiology_sections():
    record = bacdive_record()
    record["Physiology and metabolism"] = ["not a section"]

    with pytest.raises(
        ValueError,
        match="BacDive-ID 24493 Physiology and metabolism must be an object",
    ):
        evaluate_records({"24493": record}, {}, {})


def test_exact_activity_rows_rejects_malformed_taxonomy_sections():
    record = bacdive_record()
    record["Name and taxonomic classification"] = ["not a section"]

    with pytest.raises(
        ValueError,
        match="BacDive-ID 24493 Name and taxonomic classification must be an object",
    ):
        exact_activity_rows(
            {"24493": record},
            {"ampicillin": bacdive_drug_map_row()},
            SOURCE_VERSION,
        )


@pytest.mark.parametrize(
    ("field", "value", "match"),
    [
        (
            "species",
            ["Phaeobacter gallaeciensis"],
            "BacDive-ID 24493 Name and taxonomic classification species",
        ),
        (
            "strain designation",
            {"value": "BS 107"},
            "BacDive-ID 24493 Name and taxonomic classification strain designation",
        ),
    ],
)
def test_exact_activity_rows_rejects_malformed_taxonomy_scalar_fields(
    field,
    value,
    match,
):
    record = bacdive_record()
    record["Name and taxonomic classification"][field] = value

    with pytest.raises(ValueError, match=match):
        exact_activity_rows(
            {"24493": record},
            {"ampicillin": bacdive_drug_map_row()},
            SOURCE_VERSION,
        )


def test_exact_activity_rows_rejects_malformed_antibiogram_medium():
    record = bacdive_record()
    record["Physiology and metabolism"]["antibiogram"]["Medium_antibiogramV2"] = [
        "Mueller Hinton",
    ]

    with pytest.raises(
        ValueError,
        match="BacDive-ID 24493 antibiogram row 1 Medium_antibiogramV2",
    ):
        exact_activity_rows(
            {"24493": record},
            {"ampicillin": bacdive_drug_map_row()},
            SOURCE_VERSION,
        )


@pytest.mark.parametrize("disk_value", [[18], {"value": 18}])
def test_evaluate_records_rejects_malformed_antibiogram_disk_values(disk_value):
    record = bacdive_record()
    record["Physiology and metabolism"]["antibiogram"]["AMP_antibiogramV2"] = (
        disk_value
    )

    with pytest.raises(
        ValueError,
        match="BacDive-ID 24493 antibiogram row 1 AMP_antibiogramV2",
    ):
        evaluate_records({"24493": record}, {}, {})


def test_exact_activity_rows_rejects_malformed_antibiogram_disk_values():
    record = bacdive_record()
    record["Physiology and metabolism"]["antibiogram"]["AMP_antibiogramV2"] = [
        18,
    ]

    with pytest.raises(
        ValueError,
        match="BacDive-ID 24493 antibiogram row 1 AMP_antibiogramV2",
    ):
        exact_activity_rows(
            {"24493": record},
            {"ampicillin": bacdive_drug_map_row()},
            SOURCE_VERSION,
        )


def test_merge_bacdive_records_rejects_duplicate_input_ids(tmp_path):
    with pytest.raises(ValueError, match="duplicate BacDive-ID across inputs: 24493"):
        merge_bacdive_records(
            {"24493": bacdive_record()},
            {"24493": bacdive_record()},
            tmp_path / "bacdive2.json",
        )


def test_write_drug_report_and_map_template(tmp_path):
    rows = report_rows(tmp_path)
    report = tmp_path / "bacdive_antibiotics.tsv"
    template = tmp_path / "bacdive_drug_map.tsv"
    activity = tmp_path / "bacdive_activity.tsv"

    write_drug_report(rows, report)
    write_drug_map_template(rows, template, SOURCE_VERSION)
    write_activity_report([], activity)

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

    with activity.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        assert reader.fieldnames == ACTIVITY_REPORT_COLUMNS
        assert list(reader) == []


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
    activity_report = tmp_path / "bacdive_activity.tsv"
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
            "--activity-report",
            str(activity_report),
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    with report.open(newline="", encoding="utf-8") as handle:
        report_rows_by_id = {row["source_record_id"]: row for row in csv.DictReader(handle, delimiter="\t")}
    with template.open(newline="", encoding="utf-8") as handle:
        template_rows_by_id = {row["source_record_id"]: row for row in csv.DictReader(handle, delimiter="\t")}
    with activity_report.open(newline="", encoding="utf-8") as handle:
        activity_rows = list(csv.DictReader(handle, delimiter="\t"))

    assert report_rows_by_id["ampicillin"]["mapping_status"] == "EXACT"
    assert report_rows_by_id["ampicillin"]["identifier"] == "CHEBI:28971"
    assert template_rows_by_id["ampicillin"]["mapping_status"] == ""
    assert template_rows_by_id["ampicillin"]["identifier"] == ""
    assert len(activity_rows) == 2
    assert {row["source_section"] for row in activity_rows} == {
        "met_antibiogram_v2",
        "met_antibiotica",
    }


def test_cli_rejects_duplicate_bacdive_ids_across_inputs(tmp_path):
    first = tmp_path / "bacdive1.json"
    second = tmp_path / "bacdive2.json"
    first.write_text(json.dumps({"results": {"24493": bacdive_record()}}), encoding="utf-8")
    second.write_text(json.dumps({"results": {"24493": bacdive_record()}}), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--bacdive",
            str(first),
            str(second),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "duplicate BacDive-ID across inputs: 24493" in result.stderr


def test_cli_validates_activity_report(tmp_path):
    activity_report = tmp_path / "bacdive_activity.tsv"
    write_activity_report(
        exact_activity_rows(
            {"24493": bacdive_record()},
            {"ampicillin": bacdive_drug_map_row()},
            SOURCE_VERSION,
        ),
        activity_report,
    )

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--source-version",
            SOURCE_VERSION,
            "--validate-activity-report",
            str(activity_report),
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert result.stdout.startswith("BacDive activity preflight: records=0 ")
    assert "activity_report_rows=2" in result.stdout


def test_cli_rejects_stale_activity_report_against_current_bacdive(tmp_path):
    bacdive_path = tmp_path / "bacdive.json"
    drug_map = tmp_path / "bacdive_drug_map.tsv"
    activity_report = tmp_path / "bacdive_activity.tsv"
    stale_record = bacdive_record()
    current_record = bacdive_record()
    current_record["Physiology and metabolism"]["antibiotic resistance"][0][
        "concentration"
    ] = "20 mg/L"
    bacdive_path.write_text(
        json.dumps({"results": {"24493": current_record}}),
        encoding="utf-8",
    )
    write_drug_map(drug_map, [bacdive_drug_map_row()])
    write_activity_report(
        exact_activity_rows(
            {"24493": stale_record},
            {"ampicillin": bacdive_drug_map_row()},
            SOURCE_VERSION,
        ),
        activity_report,
    )

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--bacdive",
            str(bacdive_path),
            "--source-version",
            SOURCE_VERSION,
            "--drug-map",
            str(drug_map),
            "--validate-activity-report",
            str(activity_report),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert (
        "bacdive:5038512ce05fd01f source_concentration "
        "'10 mg/L' != current BacDive '20 mg/L'"
    ) in result.stderr


def test_cli_rejects_drug_report_without_bacdive(tmp_path):
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--drug-report",
            str(tmp_path / "bacdive_antibiotics.tsv"),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "--bacdive is required unless only --validate-activity-report is used" in result.stderr


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
    assert (
        "--drug-map, --drug-map-template, --activity-report and "
        "--validate-activity-report require --source-version"
        in result.stderr
    )


def test_cli_rejects_validate_activity_report_without_source_version(tmp_path):
    path = tmp_path / "bacdive.json"
    path.write_text(json.dumps({"results": {"24493": bacdive_record()}}), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--bacdive",
            str(path),
            "--validate-activity-report",
            str(tmp_path / "bacdive_activity.tsv"),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert (
        "--drug-map, --drug-map-template, --activity-report and "
        "--validate-activity-report require --source-version"
        in result.stderr
    )


def test_cli_rejects_activity_report_without_drug_map(tmp_path):
    path = tmp_path / "bacdive.json"
    path.write_text(json.dumps({"results": {"24493": bacdive_record()}}), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--bacdive",
            str(path),
            "--source-version",
            SOURCE_VERSION,
            "--activity-report",
            str(tmp_path / "bacdive_activity.tsv"),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "--activity-report requires --drug-map" in result.stderr


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


def test_cli_rejects_activity_report_over_validated_activity_report(tmp_path):
    path = tmp_path / "bacdive.json"
    activity_report = tmp_path / "bacdive_activity.tsv"
    path.write_text(json.dumps({"results": {"24493": bacdive_record()}}), encoding="utf-8")
    activity_report.write_text("keep validation input\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--bacdive",
            str(path),
            "--source-version",
            SOURCE_VERSION,
            "--drug-map",
            str(tmp_path / "bacdive_drug_map.tsv"),
            "--activity-report",
            str(activity_report),
            "--validate-activity-report",
            str(activity_report),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "--validate-activity-report must not reuse --activity-report path" in result.stderr
    assert activity_report.read_text(encoding="utf-8") == "keep validation input\n"
