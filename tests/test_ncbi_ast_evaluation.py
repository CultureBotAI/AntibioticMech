"""Unit tests for the non-writing NCBI AST evaluator."""

from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from evaluate_ncbi_ast import (  # noqa: E402
    DRUG_MAP_COLUMNS,
    corpus_name_candidates,
    evaluate_rows,
    exact_activity_rows,
    normalize_header,
    read_drug_map,
    read_table,
    write_activity_report,
    write_antibiotic_report,
    write_drug_map_template,
)

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "evaluate_ncbi_ast.py"


def test_evaluate_rows_summarizes_submitted_antibiotic_names():
    rows = [
        {
            "Antibiotic": "amikacin",
            "BioSample": "SAMN00000001",
            "BioProject": "PRJNA1",
            "target_acc": "GCF_000000001.1",
            "Scientific name": "Escherichia coli",
            "Phenotype": "R",
            "MIC": "4",
        },
        {
            "Antibiotic": "CYCLOSERINE",
            "BioSample": "SAMN00000002",
            "Disk diffusion": "12",
        },
        {
            "Antibiotic": "not in corpus",
            "Measurement sign": "<=",
            "MIC": "0.25",
        },
        {
            "BioSample": "SAMN00000003",
            "MIC": "2",
        },
    ]
    candidates = {
        "amikacin": {"CHEBI:2637"},
        "cycloserine": {"CHEBI:40009", "CHEBI:44650"},
    }
    structure_keys = {
        "CHEBI:2637": "LKCWBDHBTVXHDL-RMDFUYIESA-N",
        "CHEBI:40009": "ONE",
        "CHEBI:44650": "TWO",
    }

    result = evaluate_rows(rows, candidates, structure_keys)

    assert result["rows_with_antibiotic"] == 3
    assert result["rows_without_antibiotic"] == 1
    assert result["exact_name_matched_antibiotics"] == 1
    assert result["exact_name_matched_rows"] == 1
    assert result["ambiguous_name_antibiotics"] == 1
    assert result["unmatched_antibiotics"] == 1
    assert result["rows_with_biosample"] == 2
    assert result["rows_with_bioproject"] == 1
    assert result["rows_with_target_acc"] == 1

    amikacin = result["antibiotic_rows"][0]
    assert amikacin["antibiotic"] == "amikacin"
    assert amikacin["exact_name_candidate_identifiers"] == "CHEBI:2637"
    assert amikacin["mapping_status"] == ""
    assert amikacin["mic_count"] == 1
    assert amikacin["disk_diffusion_count"] == 0
    assert amikacin["taxon_labels"] == "Escherichia coli"


def test_evaluate_rows_coalesces_antibiotic_spellings_for_drug_maps(tmp_path):
    result = evaluate_rows(
        [
            {"Antibiotic": "amikacin", "BioSample": "SAMN00000001"},
            {"Antibiotic": "AMIKACIN", "BioSample": "SAMN00000002"},
        ],
        {"amikacin": {"CHEBI:2637"}},
        {"CHEBI:2637": "LKCWBDHBTVXHDL-RMDFUYIESA-N"},
    )

    assert result["antibiotic_values"] == 1
    assert result["antibiotic_rows"][0]["normalized_antibiotic"] == "amikacin"
    assert result["antibiotic_rows"][0]["ast_rows"] == 2

    path = tmp_path / "ncbi_ast_drug_map.tsv"
    write_drug_map_template(result["antibiotic_rows"], path)

    with path.open(newline="", encoding="utf-8") as handle:
        template_rows = list(csv.DictReader(handle, delimiter="\t"))

    assert [row["source_record_id"] for row in template_rows] == ["amikacin"]


def test_evaluate_rows_keeps_curated_mappings_separate_from_lexical_candidates():
    rows = [
        {"Antibiotic": "amikacin", "BioSample": "SAMN00000001"},
        {"Antibiotic": "amikacin", "BioSample": "SAMN00000002"},
        {"Antibiotic": "gentamicin", "BioSample": "SAMN00000003"},
    ]
    mappings = {
        "amikacin": {
            "mapping_status": "EXACT",
            "identifier": "CHEBI:2637",
            "standard_inchi_key": "LKCWBDHBTVXHDL-RMDFUYIESA-N",
            "mapping_basis": "parent_base",
            "notes": "NCBI names the active amikacin parent.",
        },
        "gentamicin": {
            "mapping_status": "MIXTURE",
            "identifier": "",
            "standard_inchi_key": "",
            "mapping_basis": "none",
            "notes": "Gentamicin is not one grounded structure.",
        },
    }

    result = evaluate_rows(
        rows,
        {"amikacin": {"CHEBI:2637"}},
        {"CHEBI:2637": "LKCWBDHBTVXHDL-RMDFUYIESA-N"},
        mappings=mappings,
    )

    assert result["exact_mapped_antibiotics"] == 1
    assert result["exact_mapped_rows"] == 2
    assert result["non_exact_mapped_antibiotics"] == 1
    assert result["non_exact_mapped_rows"] == 1
    assert result["unmapped_antibiotics"] == 0
    assert result["unmapped_rows"] == 0

    amikacin = result["antibiotic_rows"][0]
    assert amikacin["antibiotic"] == "amikacin"
    assert amikacin["mapping_status"] == "EXACT"
    assert amikacin["identifier"] == "CHEBI:2637"
    assert amikacin["mapping_basis"] == "parent_base"

    gentamicin = result["antibiotic_rows"][1]
    assert gentamicin["mapping_status"] == "MIXTURE"
    assert gentamicin["identifier"] == ""


def test_exact_activity_rows_groups_exact_mapped_valid_measurements():
    rows = [
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "GCF_003123125.1",
            "taxgroup_name": "Escherichia coli and Shigella",
            "scientific_name": "Escherichia coli",
            "phenotype": "R",
            "measurement_sign": "<=",
            "mic": "2",
            "platform": "AST",
            "vendor": "NCBI",
            "reagent": "broth microdilution",
            "standard": "CLSI",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "GCF_003123125.1",
            "taxgroup_name": "Escherichia coli and Shigella",
            "scientific_name": "Escherichia coli",
            "phenotype": "R",
            "measurement_sign": "<=",
            "mic": "2",
            "platform": "AST",
            "vendor": "NCBI",
            "reagent": "broth microdilution",
            "standard": "CLSI",
        },
        {
            "Antibiotic": "cefepime",
            "BioSample": "SAMN11953778",
            "BioProject": "PRJNA292666",
            "Organism group": "Klebsiella pneumoniae",
            "Resistance phenotype": "S",
            "Measurement sign": ">",
            "Disk diffusion": "18",
        },
        {"antibiotic": "cefepime", "measurement_sign": "<", "mic": ">4"},
        {"antibiotic": "cefepime", "phenotype": "R"},
        {"antibiotic": "gentamicin", "measurement_sign": "<=", "mic": "1"},
        {"antibiotic": "not in map", "measurement_sign": "<=", "mic": "1"},
    ]
    mappings = {
        "cefepime": {
            "mapping_status": "EXACT",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        },
        "gentamicin": {
            "mapping_status": "MIXTURE",
            "identifier": "",
            "standard_inchi_key": "",
        },
    }

    activity_rows = exact_activity_rows(rows, mappings)

    assert len(activity_rows) == 2
    assert activity_rows[0] == {
        "activity_group_id": activity_rows[0]["activity_group_id"],
        "ast_row_count": 2,
        "source_name": "cefepime",
        "normalized_antibiotic": "cefepime",
        "identifier": "CHEBI:478164",
        "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        "taxon_label": "Escherichia coli",
        "biosample_accession": "SAMN11953777",
        "bioproject_accession": "PRJNA292666",
        "assembly_accession": "GCF_003123125.1",
        "phenotype": "R",
        "activity": "RESISTANT",
        "mic_value": "2",
        "mic_qualifier": "<=",
        "mic_units": "mg/L",
        "disk_diffusion_value": "",
        "disk_diffusion_qualifier": "",
        "disk_diffusion_units": "",
        "platform": "AST",
        "vendor": "NCBI",
        "reagent": "broth microdilution",
        "standard": "CLSI",
    }
    assert activity_rows[0]["activity_group_id"].startswith("ncbi_ast:")
    assert activity_rows[1]["ast_row_count"] == 1
    assert activity_rows[1]["activity"] == "SUSCEPTIBLE"
    assert activity_rows[1]["disk_diffusion_value"] == "18"
    assert activity_rows[1]["disk_diffusion_qualifier"] == ">"
    assert activity_rows[1]["disk_diffusion_units"] == "mm"
    assert activity_rows[1]["mic_value"] == ""


def test_read_table_accepts_browser_tsv_exports(tmp_path):
    path = tmp_path / "ast.tsv"
    path.write_text(
        "AST.Antibiotic\tBioSample\tMeasurement sign\tMIC\n"
        "cefepime\tSAMN11953777\t<=\t2\n",
        encoding="utf-8",
    )

    rows = read_table(path)

    assert rows == [{
        "AST.Antibiotic": "cefepime",
        "BioSample": "SAMN11953777",
        "Measurement sign": "<=",
        "MIC": "2",
    }]
    assert normalize_header("AST.Antibiotic") == "antibiotic"


def test_read_table_ignores_ragged_extra_columns(tmp_path):
    path = tmp_path / "ast.tsv"
    path.write_text(
        "AST.Antibiotic\tBioSample\n"
        "cefepime\tSAMN11953777\textra\n",
        encoding="utf-8",
    )

    result = evaluate_rows(
        read_table(path),
        {"cefepime": {"CHEBI:478164"}},
        {"CHEBI:478164": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
    )

    assert result["rows_with_antibiotic"] == 1
    assert result["rows_with_biosample"] == 1


def test_evaluate_rows_accepts_ncbi_browser_field_names():
    rows = [
        {
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "assembly_accession": "GCF_003123125.1",
            "taxgroup_name": "Escherichia coli and Shigella",
            "scientific_name": "Escherichia coli",
            "antibiotic": "cefepime",
            "measurement_sign": "<=",
            "phenotype": "R",
            "mic": "2",
        },
        {
            "BioSample": "SAMN11953778",
            "BioProject": "PRJNA292666",
            "Organism group": "Klebsiella pneumoniae",
            "Antibiotic": "cefepime",
            "Measurement sign": ">",
            "Resistance phenotype": "S",
            "Disk diffusion": "18",
        },
    ]

    result = evaluate_rows(
        rows,
        {"cefepime": {"CHEBI:478164"}},
        {"CHEBI:478164": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
    )

    assert result["rows_with_biosample"] == 2
    assert result["rows_with_bioproject"] == 2
    assert result["rows_with_target_acc"] == 1
    assert result["antibiotic_rows"][0]["mic_count"] == 1
    assert result["antibiotic_rows"][0]["standardized_mic_count"] == 1
    assert result["antibiotic_rows"][0]["standardized_mic_values"] == "<=2 mg/L"
    assert result["antibiotic_rows"][0]["disk_diffusion_count"] == 1
    assert result["antibiotic_rows"][0]["standardized_disk_diffusion_count"] == 1
    assert result["antibiotic_rows"][0]["standardized_disk_diffusion_values"] == ">18 mm"
    assert (
        result["antibiotic_rows"][0]["taxon_labels"]
        == "Escherichia coli|Klebsiella pneumoniae"
    )
    assert result["antibiotic_rows"][0]["phenotypes"] == "R|S"


def test_evaluate_rows_counts_invalid_measurement_shapes():
    rows = [
        {"Antibiotic": "cefepime", "Measurement sign": "<=", "MIC": "2"},
        {"Antibiotic": "cefepime", "Measurement sign": "<", "MIC": ">4"},
        {"Antibiotic": "cefepime", "MIC": "not-numeric"},
        {"Antibiotic": "cefepime", "Measurement sign": ">", "Disk diffusion": "18"},
        {"Antibiotic": "cefepime", "Measurement sign": "approximately", "Disk diffusion": "19"},
    ]

    result = evaluate_rows(
        rows,
        {"cefepime": {"CHEBI:478164"}},
        {"CHEBI:478164": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
    )

    cefepime = result["antibiotic_rows"][0]
    assert cefepime["mic_count"] == 3
    assert cefepime["standardized_mic_count"] == 1
    assert cefepime["invalid_mic_count"] == 2
    assert cefepime["standardized_mic_values"] == "<=2 mg/L"
    assert cefepime["disk_diffusion_count"] == 2
    assert cefepime["standardized_disk_diffusion_count"] == 1
    assert cefepime["invalid_disk_diffusion_count"] == 1
    assert cefepime["standardized_disk_diffusion_values"] == ">18 mm"


def test_corpus_name_candidates_include_record_labels_and_synonyms(tmp_path):
    path = tmp_path / "data" / "antibiotics" / "antibacterial"
    path.mkdir(parents=True)
    (path / "amikacin.yaml").write_text(
        "\n".join([
            "identifier: CHEBI:2637",
            "label: amikacin",
            "chemical_structure:",
            "  standard_inchi_key: LKCWBDHBTVXHDL-RMDFUYIESA-N",
            "synonyms:",
            "  - synonym_text: AMIK",
        ]),
        encoding="utf-8",
    )

    candidates, structure_keys = corpus_name_candidates(root=tmp_path)

    assert candidates["amikacin"] == {"CHEBI:2637"}
    assert candidates["amik"] == {"CHEBI:2637"}
    assert structure_keys["CHEBI:2637"] == "LKCWBDHBTVXHDL-RMDFUYIESA-N"


def test_read_drug_map_accepts_exact_and_non_exact_rows(tmp_path):
    path = tmp_path / "ncbi_ast_antibiotic_map.tsv"
    path.write_text(
        "\t".join([
            "source_record_id",
            "source_name",
            "mapping_status",
            "identifier",
            "standard_inchi_key",
            "mapping_basis",
            "notes",
        ])
        + "\n"
        + "\n".join([
            "amikacin\tamikacin\tEXACT\tCHEBI:2637\t"
            "LKCWBDHBTVXHDL-RMDFUYIESA-N\tparent_base\tok",
            "gentamicin\tgentamicin\tMIXTURE\t\t\tnone\tmixture",
        ])
        + "\n",
        encoding="utf-8",
    )

    mappings = read_drug_map(path, {"CHEBI:2637": "LKCWBDHBTVXHDL-RMDFUYIESA-N"})

    assert mappings["amikacin"]["identifier"] == "CHEBI:2637"
    assert mappings["gentamicin"]["mapping_status"] == "MIXTURE"
    assert mappings["gentamicin"]["identifier"] == ""


def test_read_drug_map_rejects_identity_drift(tmp_path):
    path = tmp_path / "ncbi_ast_antibiotic_map.tsv"
    path.write_text(
        "\t".join([
            "source_record_id",
            "source_name",
            "mapping_status",
            "identifier",
            "standard_inchi_key",
            "mapping_basis",
            "notes",
        ])
        + "\namikacin\tamikacin\tEXACT\tCHEBI:2637\tWRONGINCHIKEY\tparent_base\tok\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="does not match CHEBI:2637"):
        read_drug_map(path, {"CHEBI:2637": "LKCWBDHBTVXHDL-RMDFUYIESA-N"})


def test_antibiotic_report_is_a_stable_tsv(tmp_path):
    path = tmp_path / "ncbi_ast_antibiotics.tsv"
    rows = [
        {
            "antibiotic": "cefepime",
            "normalized_antibiotic": "cefepime",
            "ast_rows": 7,
            "mapping_status": "EXACT",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
            "mapping_basis": "parent_base",
            "mapping_notes": "NCBI names the active cefepime parent.",
            "exact_name_candidate_count": 1,
            "exact_name_candidate_identifiers": "CHEBI:478164",
            "exact_name_candidate_inchi_keys": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
            "biosample_count": 7,
            "bioproject_count": 7,
            "target_acc_count": 7,
            "phenotype_count": 7,
            "mic_count": 7,
            "standardized_mic_count": 7,
            "invalid_mic_count": 0,
            "standardized_mic_values": "<=2 mg/L",
            "disk_diffusion_count": 0,
            "standardized_disk_diffusion_count": 0,
            "invalid_disk_diffusion_count": 0,
            "standardized_disk_diffusion_values": "",
            "taxon_labels": "Escherichia coli",
            "phenotypes": "R|S",
        }
    ]

    write_antibiotic_report(rows, path)

    with path.open(newline="", encoding="utf-8") as handle:
        actual = list(csv.DictReader(handle, delimiter="\t"))

    assert actual == [{
        "antibiotic": "cefepime",
        "normalized_antibiotic": "cefepime",
        "ast_rows": "7",
        "mapping_status": "EXACT",
        "identifier": "CHEBI:478164",
        "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        "mapping_basis": "parent_base",
        "mapping_notes": "NCBI names the active cefepime parent.",
        "exact_name_candidate_count": "1",
        "exact_name_candidate_identifiers": "CHEBI:478164",
        "exact_name_candidate_inchi_keys": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        "biosample_count": "7",
        "bioproject_count": "7",
        "target_acc_count": "7",
        "phenotype_count": "7",
        "mic_count": "7",
        "standardized_mic_count": "7",
        "invalid_mic_count": "0",
        "standardized_mic_values": "<=2 mg/L",
        "disk_diffusion_count": "0",
        "standardized_disk_diffusion_count": "0",
        "invalid_disk_diffusion_count": "0",
        "standardized_disk_diffusion_values": "",
        "taxon_labels": "Escherichia coli",
        "phenotypes": "R|S",
    }]


def test_drug_map_template_is_fillable_by_the_curator(tmp_path):
    path = tmp_path / "ncbi_ast_drug_map.tsv"
    rows = [
        {
            "antibiotic": "cefepime",
            "normalized_antibiotic": "cefepime",
            "mapping_status": "EXACT",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
            "mapping_basis": "parent_base",
            "mapping_notes": "NCBI names the active cefepime parent.",
        },
        {
            "antibiotic": "gentamicin",
            "normalized_antibiotic": "gentamicin",
            "mapping_status": "",
            "identifier": "",
            "standard_inchi_key": "",
            "mapping_basis": "",
            "mapping_notes": "",
        },
    ]

    write_drug_map_template(rows, path)

    with path.open(newline="", encoding="utf-8") as handle:
        actual = list(csv.DictReader(handle, delimiter="\t"))

    assert actual == [
        {
            "source_record_id": "cefepime",
            "source_name": "cefepime",
            "mapping_status": "EXACT",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
            "mapping_basis": "parent_base",
            "notes": "NCBI names the active cefepime parent.",
        },
        {
            "source_record_id": "gentamicin",
            "source_name": "gentamicin",
            "mapping_status": "",
            "identifier": "",
            "standard_inchi_key": "",
            "mapping_basis": "",
            "notes": "",
        },
    ]


def test_activity_report_is_a_stable_tsv(tmp_path):
    path = tmp_path / "ncbi_ast_activity.tsv"
    rows = [
        {
            "activity_group_id": "ncbi_ast:7fe9356073d90a3d",
            "ast_row_count": 2,
            "source_name": "cefepime",
            "normalized_antibiotic": "cefepime",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
            "taxon_label": "Escherichia coli and Shigella",
            "biosample_accession": "SAMN11953777",
            "bioproject_accession": "PRJNA292666",
            "assembly_accession": "GCF_003123125.1",
            "phenotype": "R",
            "activity": "RESISTANT",
            "mic_value": "2",
            "mic_qualifier": "<=",
            "mic_units": "mg/L",
            "disk_diffusion_value": "",
            "disk_diffusion_qualifier": "",
            "disk_diffusion_units": "",
            "platform": "AST",
            "vendor": "NCBI",
            "reagent": "broth microdilution",
            "standard": "CLSI",
        }
    ]

    write_activity_report(rows, path)

    with path.open(newline="", encoding="utf-8") as handle:
        actual = list(csv.DictReader(handle, delimiter="\t"))

    assert actual == [{
        "activity_group_id": "ncbi_ast:7fe9356073d90a3d",
        "ast_row_count": "2",
        "source_name": "cefepime",
        "normalized_antibiotic": "cefepime",
        "identifier": "CHEBI:478164",
        "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        "taxon_label": "Escherichia coli and Shigella",
        "biosample_accession": "SAMN11953777",
        "bioproject_accession": "PRJNA292666",
        "assembly_accession": "GCF_003123125.1",
        "phenotype": "R",
        "activity": "RESISTANT",
        "mic_value": "2",
        "mic_qualifier": "<=",
        "mic_units": "mg/L",
        "disk_diffusion_value": "",
        "disk_diffusion_qualifier": "",
        "disk_diffusion_units": "",
        "platform": "AST",
        "vendor": "NCBI",
        "reagent": "broth microdilution",
        "standard": "CLSI",
    }]


def test_cli_writes_all_ncbi_ast_reports(tmp_path):
    ast = tmp_path / "ast.tsv"
    with ast.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "antibiotic",
                "biosample_acc",
                "bioproject_acc",
                "target_acc",
                "scientific_name",
                "phenotype",
                "measurement_sign",
                "mic",
                "platform",
                "vendor",
                "reagent",
                "standard",
            ],
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerow({
            "antibiotic": "amikacin",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "GCF_003123125.1",
            "scientific_name": "Klebsiella pneumoniae",
            "phenotype": "R",
            "measurement_sign": ">",
            "mic": "64",
            "platform": "AST",
            "vendor": "NCBI",
            "reagent": "broth microdilution",
            "standard": "CLSI",
        })

    _, structure_keys = corpus_name_candidates()
    drug_map = tmp_path / "ncbi_ast_drug_map.tsv"
    with drug_map.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=DRUG_MAP_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerow({
            "source_record_id": "amikacin",
            "source_name": "amikacin",
            "mapping_status": "EXACT",
            "identifier": "CHEBI:2637",
            "standard_inchi_key": structure_keys["CHEBI:2637"],
            "mapping_basis": "parent_base",
            "notes": "NCBI names the active amikacin parent.",
        })

    antibiotic_report = tmp_path / "ncbi_ast_antibiotics.tsv"
    template = tmp_path / "ncbi_ast_drug_map_template.tsv"
    activity_report = tmp_path / "ncbi_ast_activity.tsv"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--ast",
            str(ast),
            "--drug-map",
            str(drug_map),
            "--antibiotic-report",
            str(antibiotic_report),
            "--drug-map-template",
            str(template),
            "--activity-report",
            str(activity_report),
        ],
        check=True,
        text=True,
        capture_output=True,
    )

    assert "exact_mapped_activity_groups=1" in result.stdout
    assert antibiotic_report.exists()

    with template.open(newline="", encoding="utf-8") as handle:
        assert list(csv.DictReader(handle, delimiter="\t"))[0]["source_record_id"] == "amikacin"

    with activity_report.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        activity_rows = list(reader)
        assert "assembly_accession" in (reader.fieldnames or [])
        assert "target_acc" not in (reader.fieldnames or [])

    assert activity_rows[0]["assembly_accession"] == "GCF_003123125.1"
    assert activity_rows[0]["mic_value"] == "64"
    assert activity_rows[0]["mic_qualifier"] == ">"
    assert activity_rows[0]["mic_units"] == "mg/L"


def test_cli_rejects_activity_report_without_drug_map(tmp_path):
    ast = tmp_path / "ast.tsv"
    ast.write_text("antibiotic\namikacin\n", encoding="utf-8")
    activity_report = tmp_path / "ncbi_ast_activity.tsv"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--ast",
            str(ast),
            "--activity-report",
            str(activity_report),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 2
    assert "--activity-report requires --drug-map" in result.stderr
    assert not activity_report.exists()
