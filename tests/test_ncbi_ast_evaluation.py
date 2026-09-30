"""Unit tests for the non-writing NCBI AST evaluator."""

from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import evaluate_ncbi_ast  # noqa: E402
from evaluate_ncbi_ast import (  # noqa: E402
    ACTIVITY_REPORT_COLUMNS,
    ANTIBIOTIC_REPORT_COLUMNS,
    DRUG_MAP_COLUMNS,
    PROJECT_DEDUPE_COLUMNS,
    PROJECT_DEDUPE_REPORT_COLUMNS,
    activity_group_id,
    corpus_name_candidates,
    evaluate_rows,
    exact_activity_rows,
    has_invalid_taxon_id,
    normalize_header,
    project_dedupe_report_rows,
    project_dedupe_source_versions,
    read_drug_map,
    read_project_dedupe_map,
    read_table,
    valid_taxon_id,
    write_activity_report,
    write_antibiotic_report,
    write_drug_map_template,
    write_project_dedupe_map_template,
    write_project_dedupe_report,
)
from seed_from_sources import load_ncbi_ast_activity_inventory  # noqa: E402

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "evaluate_ncbi_ast.py"


def ncbi_ast_activity_report_row(**overrides: str) -> dict:
    activity_rows = exact_activity_rows(
        [
            {
                "antibiotic": "cefepime",
                "biosample_acc": "SAMN11953777",
                "bioproject_acc": "PRJNA292666",
                "taxgroup_name": "Escherichia coli",
                "phenotype": "R",
                "mic": "2",
                "method": "MIC",
            },
        ],
        {
            "cefepime": {
                "mapping_status": "EXACT",
                "source_name": "cefepime",
                "identifier": "CHEBI:478164",
                "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
            },
        },
        source_version="2026-09-26-ast-browser",
        source_retrieved_on="2026-09-26",
    )

    row = activity_rows[0]
    row.update(overrides)
    return row


def ncbi_ast_antibiotic_report_row(**overrides: object) -> dict:
    row = {field: "" for field in ANTIBIOTIC_REPORT_COLUMNS}
    row.update({
        "antibiotic": "cefepime",
        "normalized_antibiotic": "cefepime",
        "mapping_basis": "parent_base",
        "mapping_notes": "NCBI names the active cefepime parent.",
    })
    row.update(overrides)
    return row


def ncbi_ast_project_dedupe_report_row(**overrides: object) -> dict:
    row = {field: "" for field in PROJECT_DEDUPE_REPORT_COLUMNS}
    row.update({
        "accession_type": "BioProject",
        "accession": "PRJNA292666",
        "ast_rows": 7,
        "exact_mapped_rows": 6,
        "exact_mapped_antibiotic_values": 2,
        "exact_mapped_antibiotics": "amikacin|cefepime",
        "exact_mapped_identifiers": "CHEBI:2637|CHEBI:478164",
        "biosample_count": 3,
        "bioproject_count": 1,
        "antibiotic_values": 2,
        "antibiotics": "amikacin|cefepime",
        "taxon_ids": "NCBITaxon:562",
        "taxon_labels": "Escherichia coli",
    })
    row.update(overrides)
    return row


def ncbi_ast_drug_map_template_row(**overrides: object) -> dict:
    row = {
        "antibiotic": "cefepime",
        "normalized_antibiotic": "cefepime",
        "mapping_status": "EXACT",
        "identifier": "CHEBI:478164",
        "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        "mapping_basis": "parent_base",
        "mapping_notes": "NCBI names the active cefepime parent.",
    }
    row.update(overrides)
    return row


def ncbi_ast_project_dedupe_template_row(**overrides: object) -> dict:
    row = {
        "accession_type": "BioProject",
        "accession": "PRJNA292666",
    }
    row.update(overrides)
    return row


def test_evaluate_rows_summarizes_submitted_antibiotic_names():
    rows = [
        {
            "Antibiotic": "amikacin",
            "BioSample": "SAMN00000001",
            "BioProject": "PRJNA1",
            "target_acc": "PDT000000001.1",
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

    result = evaluate_rows(
        rows,
        candidates,
        structure_keys,
        project_dedupe={
            ("BioSample", "SAMN00000001"): {
                "accession_type": "BioSample",
                "accession": "SAMN00000001",
                "source": "CRYPTIC",
                "source_version": "3.4.0",
                "notes": "already represented in an adopted project dataset",
            },
        },
    )

    assert result["rows_with_antibiotic"] == 3
    assert result["rows_without_antibiotic"] == 1
    assert result["exact_name_matched_antibiotics"] == 1
    assert result["exact_name_matched_rows"] == 1
    assert result["ambiguous_name_antibiotics"] == 1
    assert result["unmatched_antibiotics"] == 1
    assert result["rows_with_biosample"] == 2
    assert result["rows_with_bioproject"] == 1
    assert result["rows_with_project_context"] == 1
    assert result["rows_with_valid_project_context"] == 1
    assert result["rows_with_target_acc"] == 1
    assert result["rows_with_taxon"] == 1
    assert result["rows_with_assay_method"] == 0
    assert result["rows_with_dedupe_context"] == 1

    amikacin = result["antibiotic_rows"][0]
    assert amikacin["antibiotic"] == "amikacin"
    assert amikacin["exact_name_candidate_identifiers"] == "CHEBI:2637"
    assert amikacin["mapping_status"] == ""
    assert amikacin["project_context_count"] == 1
    assert amikacin["valid_project_context_count"] == 1
    assert amikacin["dedupe_context_count"] == 1
    assert amikacin["taxon_count"] == 1
    assert amikacin["assay_method_count"] == 0
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
    write_drug_map_template(
        result["antibiotic_rows"],
        path,
        source_version="2026-09-26-ast-browser",
    )

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
        "oldncbirow": {
            "mapping_status": "EXACT",
            "source_name": "old NCBI row",
            "identifier": "CHEBI:2637",
            "standard_inchi_key": "LKCWBDHBTVXHDL-RMDFUYIESA-N",
            "mapping_basis": "parent_base",
            "notes": "Stale row from an older AST export.",
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
    assert result["exact_mapped_activity_report_candidate_rows"] == 0
    assert result["non_exact_mapped_antibiotics"] == 1
    assert result["non_exact_mapped_rows"] == 1
    assert result["unmapped_antibiotics"] == 0
    assert result["unmapped_rows"] == 0
    assert result["unused_mapping_antibiotics"] == 1
    assert result["unused_mapping_antibiotic_values"] == "oldncbirow"

    amikacin = result["antibiotic_rows"][0]
    assert amikacin["antibiotic"] == "amikacin"
    assert amikacin["mapping_status"] == "EXACT"
    assert amikacin["identifier"] == "CHEBI:2637"
    assert amikacin["mapping_basis"] == "parent_base"

    gentamicin = result["antibiotic_rows"][1]
    assert gentamicin["mapping_status"] == "MIXTURE"
    assert gentamicin["identifier"] == ""


def test_evaluate_rows_counts_exact_activity_report_candidates_after_dedupe():
    rows = [
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "PDT000001234.1",
            "taxgroup_name": "Escherichia coli",
            "mic": "2",
            "platform": "AST",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953778",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "not-a-target",
            "taxgroup_name": "Escherichia coli",
            "mic": "4",
            "platform": "AST",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953779",
            "bioproject_acc": "PRJNA292667",
            "asm_acc": "not-an-assembly",
            "target_acc": "PDT000001234.1",
            "taxgroup_name": "Escherichia coli",
            "mic": "8",
            "platform": "AST",
        },
        {
            "antibiotic": "gentamicin",
            "biosample_acc": "SAMN11953780",
            "bioproject_acc": "PRJNA292668",
            "target_acc": "PDT000001234.1",
            "taxgroup_name": "Escherichia coli",
            "mic": "16",
            "platform": "AST",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953781",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "PDT000001234.1",
            "Run": "not-an-sra-accession",
            "taxgroup_name": "Escherichia coli",
            "mic": "32",
            "platform": "AST",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953782",
            "bioproject_acc": "PRJNA292667",
            "target_acc": "PDT000001236.1",
            "taxgroup_name": "Escherichia coli",
            "mic": "64",
            "platform": "AST",
        },
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

    result = evaluate_rows(
        rows,
        {"cefepime": {"CHEBI:478164"}},
        {"CHEBI:478164": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
        mappings=mappings,
        project_dedupe={
            ("BioProject", "PRJNA292667"): {
                "accession_type": "BioProject",
                "accession": "PRJNA292667",
                "source": "CRYPTIC",
                "source_version": "3.4.0",
                "notes": "Project represented in an adopted source lane.",
            },
        },
    )

    assert result["exact_mapped_rows"] == 5
    assert result["rows_with_invalid_target_acc"] == 1
    assert result["rows_with_invalid_assembly_acc"] == 1
    assert result["rows_with_invalid_sra_accessions"] == 1
    assert result["rows_with_assay_method"] == 6
    assert result["rows_with_dedupe_context"] == 2
    assert result["rows_with_invalid_phenotype"] == 0
    assert result["exact_mapped_activity_report_candidate_rows"] == 1
    assert result["exact_mapped_activity_report_dedupe_excluded_rows"] == 1
    assert result["antibiotic_rows"][0]["activity_report_candidate_count"] == 1
    assert result["antibiotic_rows"][0]["activity_report_dedupe_excluded_count"] == 1
    assert result["antibiotic_rows"][0]["invalid_target_acc_count"] == 1
    assert result["antibiotic_rows"][0]["assembly_acc_count"] == 1
    assert result["antibiotic_rows"][0]["invalid_assembly_acc_count"] == 1
    assert result["antibiotic_rows"][0]["invalid_sra_accessions_count"] == 1
    assert result["antibiotic_rows"][1]["activity_report_candidate_count"] == 1


def test_exact_activity_rows_groups_exact_mapped_valid_measurements():
    rows = [
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "PDT000001234.1",
            "asm_acc": "GCF_003123125.1",
            "Run": "SRR222222,ERR111111 SRR222222",
            "TaxID": "562",
            "taxgroup_name": "Escherichia coli and Shigella",
            "scientific_name": "Escherichia coli",
            "strain": "CDC-1234",
            "phenotype": "R",
            "measurement_sign": "<=",
            "mic": "2",
            "method": "MIC",
            "platform": "AST",
            "vendor": "NCBI",
            "reagent": "Sensititre GNX2F",
            "standard": "CLSI",
        },
        {
            "antibiotic": "CEFEPIME",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "PDT000001234.1",
            "asm_acc": "GCF_003123125.1",
            "Run": "ERR111111|SRR222222",
            "TaxID": "NCBITaxon:562",
            "taxgroup_name": "Escherichia coli and Shigella",
            "scientific_name": "Escherichia coli",
            "strain": "CDC-1234",
            "phenotype": "R",
            "measurement_sign": "<=",
            "mic": "2.0",
            "method": "MIC",
            "platform": "AST",
            "vendor": "NCBI",
            "reagent": "Sensititre GNX2F",
            "standard": "CLSI",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "PDT000001234.1",
            "asm_acc": "GCF_003123125.1",
            "Run": "ERR111111|SRR222222",
            "TaxID": "562",
            "taxgroup_name": "Escherichia coli and Shigella",
            "scientific_name": "Escherichia coli",
            "strain": "CDC-1234",
            "phenotype": "R",
            "measurement_sign": "<=",
            "mic": "02.00",
            "method": "MIC",
            "platform": "AST",
            "vendor": "NCBI",
            "reagent": "Sensititre GNX2F",
            "standard": "CLSI",
        },
        {
            "Antibiotic": "cefepime",
            "BioSample": "SAMEA11953778",
            "BioProject": "PRJEB292666",
            "Assembly Accession": "GCA_003123126",
            "NCBI Taxonomy ID": "NCBITaxon:573",
            "Organism group": "Klebsiella pneumoniae",
            "Resistance phenotype": "S",
            "Measurement sign": "==",
            "Disk diffusion (mm)": "18.0",
            "Laboratory typing method": "disk diffusion",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953779",
            "taxgroup_name": "Escherichia coli and Shigella",
            "phenotype": "R",
            "measurement_sign": "<=",
            "mic": "2",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953785",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia coli and Shigella",
            "phenotype": "R",
            "measurement_sign": "<=",
            "mic": "2",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953782",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "not-a-target",
            "taxgroup_name": "Escherichia coli and Shigella",
            "phenotype": "R",
            "measurement_sign": "<=",
            "mic": "2",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "not-a-biosample",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia coli and Shigella",
            "phenotype": "R",
            "measurement_sign": "<=",
            "mic": "2",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953781",
            "bioproject_acc": "not-a-bioproject",
            "taxgroup_name": "Escherichia coli and Shigella",
            "phenotype": "R",
            "measurement_sign": "<=",
            "mic": "2",
        },
        {
            "antibiotic": "cefepime",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia coli and Shigella",
            "phenotype": "R",
            "measurement_sign": "<=",
            "mic": "2",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953780",
            "bioproject_acc": "PRJNA292666",
            "phenotype": "R",
            "measurement_sign": "<=",
            "mic": "2",
        },
        {"antibiotic": "cefepime", "measurement_sign": "<", "mic": ">4"},
        {"antibiotic": "cefepime", "phenotype": "R"},
        {"antibiotic": "gentamicin", "measurement_sign": "<=", "mic": "1"},
        {"antibiotic": "not in map", "measurement_sign": "<=", "mic": "1"},
    ]
    mappings = {
        "cefepime": {
            "mapping_status": "EXACT",
            "source_name": "cefepime",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        },
        "gentamicin": {
            "mapping_status": "MIXTURE",
            "identifier": "",
            "standard_inchi_key": "",
        },
    }

    activity_rows = exact_activity_rows(
        rows,
        mappings,
        source_version="2026-09-26-ast-browser",
        source_retrieved_on="2026-09-26",
    )

    assert len(activity_rows) == 2
    assert activity_rows[0] == {
        "activity_group_id": activity_rows[0]["activity_group_id"],
        "source_version": "2026-09-26-ast-browser",
        "source_retrieved_on": "2026-09-26",
        "ast_row_count": 3,
        "isolate_count": 1,
        "source_name": "cefepime",
        "normalized_antibiotic": "cefepime",
        "identifier": "CHEBI:478164",
        "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        "taxon_id": "NCBITaxon:562",
        "taxon_label": "Escherichia coli",
        "strain": "CDC-1234",
        "biosample_accession": "SAMN11953777",
        "bioproject_accession": "PRJNA292666",
        "target_accession": "PDT000001234.1",
        "assembly_accession": "GCF_003123125.1",
        "sra_accessions": "ERR111111|SRR222222",
        "isolation_type": "",
        "location": "",
        "collection_date": "",
        "create_date": "",
        "host": "",
        "isolation_source": "",
        "phenotype": "R",
        "activity": "RESISTANT",
        "mic_value": "2",
        "mic_qualifier": "<=",
        "mic_units": "mg/L",
        "disk_diffusion_value": "",
        "disk_diffusion_qualifier": "",
        "disk_diffusion_units": "",
        "method": "MIC",
        "platform": "AST",
        "vendor": "NCBI",
        "reagent": "Sensititre GNX2F",
        "standard": "CLSI",
    }
    assert activity_rows[0]["activity_group_id"].startswith("ncbi_ast:")
    assert activity_rows[0]["target_accession"] == "PDT000001234.1"
    assert activity_rows[1]["ast_row_count"] == 1
    assert activity_rows[1]["taxon_id"] == "NCBITaxon:573"
    assert activity_rows[1]["biosample_accession"] == "SAMEA11953778"
    assert activity_rows[1]["bioproject_accession"] == "PRJEB292666"
    assert activity_rows[1]["assembly_accession"] == "GCA_003123126"
    assert activity_rows[1]["activity"] == "SUSCEPTIBLE"
    assert activity_rows[1]["disk_diffusion_value"] == "18"
    assert activity_rows[1]["disk_diffusion_qualifier"] == ""
    assert activity_rows[1]["disk_diffusion_units"] == "mm"
    assert activity_rows[1]["mic_value"] == ""


def test_exact_activity_rows_preserves_source_isolation_context():
    rows = [
        {
            "Antibiotic": "cefepime",
            "BioSample": "SAMN11953777",
            "BioProject": "PRJNA292666",
            "Organism group": "Escherichia coli",
            "Phenotype": "R",
            "MIC": "2",
            "Laboratory typing platform": "AST",
            "Isolation type": "clinical",
            "Location": "USA",
            "Collection date": "2020",
            "Create date": "2020-01-31",
            "Host": "Homo sapiens",
            "Isolation source": "blood",
        },
    ]
    mappings = {
        "cefepime": {
            "mapping_status": "EXACT",
            "source_name": "cefepime",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        },
    }

    activity_rows = exact_activity_rows(
        rows,
        mappings,
        source_version="2026-09-26-ast-browser",
        source_retrieved_on="2026-09-26",
    )

    assert activity_rows[0]["isolation_type"] == "clinical"
    assert activity_rows[0]["location"] == "USA"
    assert activity_rows[0]["collection_date"] == "2020"
    assert activity_rows[0]["create_date"] == "2020-01-31"
    assert activity_rows[0]["host"] == "Homo sapiens"
    assert activity_rows[0]["isolation_source"] == "blood"


def test_exact_activity_rows_preserves_gcp_isolate_context_aliases():
    rows = [
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia coli",
            "phenotype": "R",
            "mic": "2",
            "platform": "AST",
            "strain": "KPNIH1",
            "epi_type": "clinical",
            "geo_loc_name": "USA",
            "creation_date": "2020-01-31",
        },
    ]
    mappings = {
        "cefepime": {
            "mapping_status": "EXACT",
            "source_name": "cefepime",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        },
    }

    result = evaluate_rows(
        rows,
        {"cefepime": {"CHEBI:478164"}},
        {"CHEBI:478164": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
        mappings=mappings,
    )
    activity_rows = exact_activity_rows(
        rows,
        mappings,
        source_version="2026-09-26-ast-browser",
        source_retrieved_on="2026-09-26",
    )

    assert result["rows_with_isolation_type"] == 1
    assert result["rows_with_location"] == 1
    assert result["rows_with_create_date"] == 1
    assert result["rows_with_invalid_create_date"] == 0
    assert result["antibiotic_rows"][0]["isolation_type_count"] == 1
    assert result["antibiotic_rows"][0]["location_count"] == 1
    assert result["antibiotic_rows"][0]["create_date_count"] == 1
    assert result["antibiotic_rows"][0]["invalid_create_date_count"] == 0
    assert len(activity_rows) == 1
    assert activity_rows[0]["strain"] == "KPNIH1"
    assert activity_rows[0]["isolation_type"] == "clinical"
    assert activity_rows[0]["location"] == "USA"
    assert activity_rows[0]["create_date"] == "2020-01-31"


def test_exact_activity_rows_excludes_invalid_create_dates():
    rows = [
        {
            "Antibiotic": "cefepime",
            "BioSample": "SAMN11953777",
            "BioProject": "PRJNA292666",
            "Organism group": "Escherichia coli",
            "Phenotype": "R",
            "MIC": "2",
            "Laboratory typing platform": "AST",
            "Create date": "20200131",
        },
        {
            "Antibiotic": "cefepime",
            "BioSample": "SAMN11953778",
            "BioProject": "PRJNA292666",
            "Organism group": "Escherichia coli",
            "Phenotype": "R",
            "MIC": "2",
            "Laboratory typing platform": "AST",
            "Create date": "2020-01-31",
        },
    ]
    mappings = {
        "cefepime": {
            "mapping_status": "EXACT",
            "source_name": "cefepime",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        },
    }

    result = evaluate_rows(
        rows,
        {"cefepime": {"CHEBI:478164"}},
        {"CHEBI:478164": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
        mappings=mappings,
    )
    activity_rows = exact_activity_rows(
        rows,
        mappings,
        source_version="2026-09-26-ast-browser",
        source_retrieved_on="2026-09-26",
    )

    assert result["rows_with_create_date"] == 2
    assert result["rows_with_invalid_create_date"] == 1
    assert result["exact_mapped_activity_report_candidate_rows"] == 1
    assert result["antibiotic_rows"][0]["invalid_create_date_count"] == 1
    assert [row["biosample_accession"] for row in activity_rows] == ["SAMN11953778"]
    assert activity_rows[0]["create_date"] == "2020-01-31"


def test_exact_activity_rows_normalizes_raw_source_tsv_controls(tmp_path):
    rows = [
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia\ncoli",
            "phenotype": "R",
            "mic": "2",
            "Laboratory typing method": "broth\tmicrodilution",
            "Laboratory typing platform": "AST\rGCP",
            "Laboratory typing method version or reagent": "Sensititre\nGNX2F",
            "Testing standard": "CLSI\tM100",
            "epi_type": "human\rclinical",
            "geo_loc_name": "USA\nCalifornia",
            "host": "Homo\tsapiens",
            "isolation_source": "blood\nculture",
        },
    ]
    mappings = {
        "cefepime": {
            "mapping_status": "EXACT",
            "source_name": "cefepime",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        },
    }

    activity_rows = exact_activity_rows(
        rows,
        mappings,
        source_version="2026-09-26-ast-browser",
        source_retrieved_on="2026-09-26",
    )
    path = tmp_path / "ncbi_ast_activity.tsv"
    write_activity_report(activity_rows, path)
    loaded_rows = load_ncbi_ast_activity_inventory(path)

    assert len(loaded_rows) == 1
    assert all(
        not any(control in value for control in "\t\r\n")
        for row in loaded_rows
        for value in row.values()
    )
    assert loaded_rows[0]["taxon_label"] == "Escherichia coli"
    assert loaded_rows[0]["method"] == "broth microdilution"
    assert loaded_rows[0]["platform"] == "AST GCP"
    assert loaded_rows[0]["reagent"] == "Sensititre GNX2F"
    assert loaded_rows[0]["standard"] == "CLSI M100"
    assert loaded_rows[0]["isolation_type"] == "human clinical"
    assert loaded_rows[0]["location"] == "USA California"
    assert loaded_rows[0]["host"] == "Homo sapiens"
    assert loaded_rows[0]["isolation_source"] == "blood culture"


def test_exact_activity_rows_normalizes_microgram_mic_headers_to_mg_per_l():
    rows = [
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "PDT000001234.1",
            "taxgroup_name": "Escherichia coli",
            "Laboratory typing method": "MIC",
            "MIC (µg/mL)": "2",
        },
    ]
    mappings = {
        "cefepime": {
            "mapping_status": "EXACT",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
            "source_name": "cefepime",
        },
    }

    activity_rows = exact_activity_rows(
        rows,
        mappings,
        source_version="2026-09-26-ast-browser",
        source_retrieved_on="2026-09-26",
    )

    assert len(activity_rows) == 1
    assert activity_rows[0]["mic_value"] == "2"
    assert activity_rows[0]["mic_qualifier"] == ""
    assert activity_rows[0]["mic_units"] == "mg/L"


def test_exact_activity_rows_excludes_unknown_phenotypes():
    rows = [
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia coli",
            "phenotype": "R",
            "mic": "2",
            "platform": "AST",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953778",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia coli",
            "phenotype": "non-susceptible",
            "mic": "4",
            "platform": "AST",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953779",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia coli",
            "mic": "8",
            "platform": "AST",
        },
    ]
    mappings = {
        "cefepime": {
            "mapping_status": "EXACT",
            "source_name": "cefepime",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        },
    }

    result = evaluate_rows(
        rows,
        {"cefepime": {"CHEBI:478164"}},
        {"CHEBI:478164": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
        mappings=mappings,
    )
    activity_rows = exact_activity_rows(
        rows,
        mappings,
        source_version="2026-09-26-ast-browser",
        source_retrieved_on="2026-09-26",
    )

    assert result["rows_with_phenotype"] == 2
    assert result["rows_with_invalid_phenotype"] == 1
    assert result["exact_mapped_activity_report_candidate_rows"] == 2
    assert result["antibiotic_rows"][0]["invalid_phenotype_count"] == 1
    assert {row["biosample_accession"] for row in activity_rows} == {
        "SAMN11953777",
        "SAMN11953779",
    }
    assert {
        row["activity"] for row in activity_rows
    } == {
        "",
        "RESISTANT",
    }


def test_exact_activity_rows_excludes_known_source_context():
    rows = [
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia coli",
            "phenotype": "R",
            "mic": "2",
            "platform": "AST",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953778",
            "bioproject_acc": "PRJNA292667",
            "taxgroup_name": "Escherichia coli",
            "phenotype": "S",
            "mic": "4",
            "platform": "AST",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953779",
            "bioproject_acc": "PRJNA292668",
            "taxgroup_name": "Escherichia coli",
            "phenotype": "S",
            "mic": "8",
            "platform": "AST",
        },
    ]
    mappings = {
        "cefepime": {
            "mapping_status": "EXACT",
            "source_name": "cefepime",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        },
    }

    activity_rows = exact_activity_rows(
        rows,
        mappings,
        source_version="2026-09-26-ast-browser",
        source_retrieved_on="2026-09-26",
        project_dedupe={
            ("BioSample", "SAMN11953777"): {
                "accession_type": "BioSample",
                "accession": "SAMN11953777",
                "source": "CRYPTIC",
                "source_version": "3.4.0",
                "notes": "already represented in an adopted project dataset",
            },
            ("BioProject", "PRJNA292667"): {
                "accession_type": "BioProject",
                "accession": "PRJNA292667",
                "source": "CRYPTIC",
                "source_version": "3.4.0",
                "notes": "already represented in an adopted project dataset",
            },
        },
    )

    assert [row["biosample_accession"] for row in activity_rows] == ["SAMN11953779"]


def test_exact_activity_rows_keeps_target_accession_separate_from_assembly():
    rows = [
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "PDT000001234.1",
            "taxgroup_name": "Escherichia coli",
            "phenotype": "R",
            "mic": "2",
            "platform": "AST",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953778",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "GCF_003123125.1",
            "taxgroup_name": "Escherichia coli",
            "phenotype": "R",
            "mic": "4",
            "platform": "AST",
        },
    ]
    mappings = {
        "cefepime": {
            "mapping_status": "EXACT",
            "source_name": "cefepime",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        },
    }

    activity_rows = exact_activity_rows(
        rows,
        mappings,
        source_version="2026-09-26-ast-browser",
        source_retrieved_on="2026-09-26",
    )

    assert len(activity_rows) == 1
    assert activity_rows[0]["target_accession"] == "PDT000001234.1"
    assert activity_rows[0]["assembly_accession"] == ""


def test_project_dedupe_report_rows_rank_valid_project_contexts():
    rows = [
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia coli",
            "mic": "2",
            "platform": "AST",
        },
        {
            "antibiotic": "CEFEPIME",
            "biosample_acc": "SAMN11953778",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Klebsiella pneumoniae",
            "measurement_sign": ">=",
            "disk_diffusion": "18",
            "platform": "AST",
        },
        {
            "antibiotic": "gentamicin",
            "biosample_acc": "SAMN11953779",
            "bioproject_acc": "PRJNA292667",
            "taxgroup_name": "Escherichia coli",
            "mic": "4",
            "platform": "AST",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953785",
            "bioproject_acc": "PRJNA292669",
            "taxgroup_name": "Escherichia coli",
            "mic": "2",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953786",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia coli",
            "phenotype": "non-susceptible",
            "mic": "2",
            "platform": "AST",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "not-a-biosample",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia coli",
            "mic": "2",
        },
        {
            "biosample_acc": "SAMN11953780",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia coli",
            "mic": "2",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953781",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Escherichia coli",
            "measurement_sign": "<",
            "mic": ">4",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953782",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "not-a-target",
            "taxgroup_name": "Escherichia coli",
            "mic": "2",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953783",
            "bioproject_acc": "PRJNA292666",
            "mic": "2",
        },
        {
            "antibiotic": "cefepime",
            "biosample_acc": "SAMN11953784",
            "bioproject_acc": "PRJNA292666",
        },
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

    report_rows = project_dedupe_report_rows(rows, mappings)

    assert report_rows == [
        {
            "accession_type": "BioProject",
            "accession": "PRJNA292666",
            "ast_rows": 2,
            "exact_mapped_rows": 2,
            "exact_mapped_antibiotic_values": 1,
            "exact_mapped_antibiotics": "cefepime",
            "exact_mapped_identifiers": "CHEBI:478164",
            "biosample_count": 2,
            "bioproject_count": 1,
            "antibiotic_values": 1,
            "antibiotics": "cefepime",
            "taxon_ids": "",
            "taxon_labels": "Escherichia coli|Klebsiella pneumoniae",
        },
        {
            "accession_type": "BioSample",
            "accession": "SAMN11953777",
            "ast_rows": 1,
            "exact_mapped_rows": 1,
            "exact_mapped_antibiotic_values": 1,
            "exact_mapped_antibiotics": "cefepime",
            "exact_mapped_identifiers": "CHEBI:478164",
            "biosample_count": 1,
            "bioproject_count": 1,
            "antibiotic_values": 1,
            "antibiotics": "cefepime",
            "taxon_ids": "",
            "taxon_labels": "Escherichia coli",
        },
        {
            "accession_type": "BioSample",
            "accession": "SAMN11953778",
            "ast_rows": 1,
            "exact_mapped_rows": 1,
            "exact_mapped_antibiotic_values": 1,
            "exact_mapped_antibiotics": "cefepime",
            "exact_mapped_identifiers": "CHEBI:478164",
            "biosample_count": 1,
            "bioproject_count": 1,
            "antibiotic_values": 1,
            "antibiotics": "cefepime",
            "taxon_ids": "",
            "taxon_labels": "Klebsiella pneumoniae",
        },
        {
            "accession_type": "BioProject",
            "accession": "PRJNA292667",
            "ast_rows": 1,
            "exact_mapped_rows": 0,
            "exact_mapped_antibiotic_values": 0,
            "exact_mapped_antibiotics": "",
            "exact_mapped_identifiers": "",
            "biosample_count": 1,
            "bioproject_count": 1,
            "antibiotic_values": 1,
            "antibiotics": "gentamicin",
            "taxon_ids": "",
            "taxon_labels": "Escherichia coli",
        },
        {
            "accession_type": "BioSample",
            "accession": "SAMN11953779",
            "ast_rows": 1,
            "exact_mapped_rows": 0,
            "exact_mapped_antibiotic_values": 0,
            "exact_mapped_antibiotics": "",
            "exact_mapped_identifiers": "",
            "biosample_count": 1,
            "bioproject_count": 1,
            "antibiotic_values": 1,
            "antibiotics": "gentamicin",
            "taxon_ids": "",
            "taxon_labels": "Escherichia coli",
        },
    ]

    report_rows = project_dedupe_report_rows(
        rows,
        mappings,
        {
            ("BioProject", "PRJNA292666"): {
                "source": "CRYPTIC",
                "source_version": "3.4.0",
                "notes": "Project represented in an adopted source lane.",
            },
        },
    )

    assert [row["accession"] for row in report_rows] == [
        "PRJNA292667",
        "SAMN11953779",
    ]


def test_evaluate_rows_audits_unused_project_dedupe_contexts():
    rows = [
        {
            "antibiotic": "amikacin",
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "taxgroup_name": "Klebsiella pneumoniae",
            "mic": "64",
            "platform": "AST",
        },
        {
            "antibiotic": "amikacin",
            "biosample_acc": "SAMN11953778",
            "bioproject_acc": "PRJNA292667",
            "taxgroup_name": "Klebsiella pneumoniae",
            "mic": "64",
        },
        {
            "antibiotic": "gentamicin",
            "biosample_acc": "SAMN11953780",
            "bioproject_acc": "PRJNA292668",
            "taxgroup_name": "Klebsiella pneumoniae",
            "mic": "64",
            "platform": "AST",
        },
    ]
    project_dedupe = {
        ("BioProject", "PRJNA292666"): {
            "accession_type": "BioProject",
            "accession": "PRJNA292666",
            "source": "CRYPTIC",
            "source_version": "3.4.0",
            "notes": "Project represented in an adopted source lane.",
        },
        ("BioSample", "SAMN11953777"): {
            "accession_type": "BioSample",
            "accession": "SAMN11953777",
            "source": "CRYPTIC",
            "source_version": "3.4.0",
            "notes": "BioSample represented in an adopted source lane.",
        },
        ("BioProject", "PRJNA292667"): {
            "accession_type": "BioProject",
            "accession": "PRJNA292667",
            "source": "CRYPTIC",
            "source_version": "3.4.0",
            "notes": "Ineligible without an assay method.",
        },
        ("BioSample", "SAMN11953779"): {
            "accession_type": "BioSample",
            "accession": "SAMN11953779",
            "source": "CRYPTIC",
            "source_version": "3.4.0",
            "notes": "No longer appears in this export.",
        },
        ("BioProject", "PRJNA292668"): {
            "accession_type": "BioProject",
            "accession": "PRJNA292668",
            "source": "CRYPTIC",
            "source_version": "3.4.0",
            "notes": "Non-exact antibiotic mapping.",
        },
    }
    mappings = {
        "amikacin": {
            "mapping_status": "EXACT",
            "identifier": "CHEBI:2637",
            "standard_inchi_key": "LKCWBDHBTVXHDL-RMDFUYIESA-N",
        },
        "gentamicin": {
            "mapping_status": "MIXTURE",
            "identifier": "",
            "standard_inchi_key": "",
        },
    }

    result = evaluate_rows(
        rows,
        {"amikacin": {"CHEBI:2637"}},
        {"CHEBI:2637": "LKCWBDHBTVXHDL-RMDFUYIESA-N"},
        mappings=mappings,
        project_dedupe=project_dedupe,
    )

    assert result["rows_with_dedupe_context"] == 3
    assert result["unused_project_dedupe_contexts"] == 3
    assert (
        result["unused_project_dedupe_values"]
        == "BioProject:PRJNA292667|BioProject:PRJNA292668|BioSample:SAMN11953779"
    )


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


def test_read_table_rejects_ragged_rows(tmp_path):
    path = tmp_path / "ast.tsv"
    path.write_text(
        "AST.Antibiotic\tBioSample\n"
        "cefepime\tSAMN11953777\textra\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="unexpected extra delimited field"):
        read_table(path)

    path.write_text(
        "AST.Antibiotic\tBioSample\tMIC\n"
        "cefepime\tSAMN11953777\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="MIC is missing"):
        read_table(path)


def test_read_table_rejects_header_only_source_exports(tmp_path):
    path = tmp_path / "ast.tsv"
    path.write_text("AST.Antibiotic\tBioSample\tMIC\n", encoding="utf-8")

    with pytest.raises(ValueError, match="NCBI AST table has no rows"):
        read_table(path)


def test_read_table_rejects_malformed_headers(tmp_path):
    path = tmp_path / "ast.csv"
    path.write_text(
        "Antibiotic,Antibiotic\n"
        "cefepime,cefepime\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="duplicate header"):
        read_table(path)

    path.write_text(
        "Antibiotic,\n"
        "cefepime,SAMN11953777\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="header column 2 is empty"):
        read_table(path)

    path.write_text(
        "AST.Antibiotic,AMR.Antibiotic\n"
        "cefepime,cefepime\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="normalizes to 'antibiotic'"):
        read_table(path)

    path.write_text(
        "Antibiotic,AST.\n"
        "cefepime,ignored\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="normalizes to empty"):
        read_table(path)


@pytest.mark.parametrize(
    ("source_value", "expected"),
    [
        ("562", "NCBITaxon:562"),
        ("NCBITaxon:562", "NCBITaxon:562"),
        (" 562 ", "NCBITaxon:562"),
        ("", ""),
        ("0", None),
        ("000562", None),
        ("NCBITaxon:000562", None),
        ("not-a-taxid", None),
    ],
)
def test_valid_taxon_id_accepts_only_canonical_positive_taxids(source_value, expected):
    row = {"TaxID": source_value}

    assert valid_taxon_id(row) == expected
    assert has_invalid_taxon_id(row) is (expected is None)


def test_evaluate_rows_accepts_ncbi_browser_field_names():
    rows = [
        {
            "biosample_acc": "SAMN11953777",
            "bioproject_acc": "PRJNA292666",
            "target_acc": "PDT000001234.1",
            "assembly_accession": "GCF_003123125.1",
            "TaxID": "562",
            "Isolation type": "clinical",
            "Location": "USA",
            "Collection date": "2020",
            "Create date": "2020-01-31",
            "Host": "Homo sapiens",
            "Isolation source": "blood",
            "taxgroup_name": "Escherichia coli and Shigella",
            "scientific_name": "Escherichia coli",
            "antibiotic": "cefepime",
            "measurement_sign": "<=",
            "phenotype": "R",
            "MIC (mg/L)": "2",
        },
        {
            "BioSample": "SAMN11953778",
            "BioProject": "PRJNA292666",
            "Isolate": "PDT000001235.1",
            "Run": "SRR222222;ERR111111",
            "NCBI Taxonomy ID": "NCBITaxon:573",
            "Organism group": "Klebsiella pneumoniae",
            "Antibiotic": "cefepime",
            "Measurement sign": ">",
            "Resistance phenotype": "S",
            "Disk diffusion (mm)": "18",
        },
        {
            "BioSample": "SAMN11953779",
            "BioProject": "PRJNA292666",
            "TaxID": "not-a-taxid",
            "Organism group": "Klebsiella pneumoniae",
            "Antibiotic": "cefepime",
            "Measurement sign": "==",
            "Resistance phenotype": "S",
            "MIC (mg/L)": "4",
            "Laboratory typing platform": "AST",
        },
    ]

    result = evaluate_rows(
        rows,
        {"cefepime": {"CHEBI:478164"}},
        {"CHEBI:478164": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
    )

    assert result["rows_with_biosample"] == 3
    assert result["rows_with_bioproject"] == 3
    assert result["rows_with_project_context"] == 3
    assert result["rows_with_valid_project_context"] == 3
    assert result["rows_with_target_acc"] == 2
    assert result["rows_with_assembly_acc"] == 1
    assert result["rows_with_sra_accessions"] == 1
    assert result["rows_with_taxon_id"] == 3
    assert result["rows_with_isolation_type"] == 1
    assert result["rows_with_location"] == 1
    assert result["rows_with_collection_date"] == 1
    assert result["rows_with_create_date"] == 1
    assert result["rows_with_host"] == 1
    assert result["rows_with_isolation_source"] == 1
    assert result["rows_with_invalid_target_acc"] == 0
    assert result["rows_with_invalid_assembly_acc"] == 0
    assert result["rows_with_invalid_sra_accessions"] == 0
    assert result["rows_with_invalid_taxon_id"] == 1
    assert result["rows_with_taxon"] == 3
    assert result["antibiotic_rows"][0]["mic_count"] == 2
    assert result["antibiotic_rows"][0]["standardized_mic_count"] == 2
    assert result["antibiotic_rows"][0]["standardized_mic_values"] == "4 mg/L|<=2 mg/L"
    assert result["antibiotic_rows"][0]["disk_diffusion_count"] == 1
    assert result["antibiotic_rows"][0]["standardized_disk_diffusion_count"] == 1
    assert result["antibiotic_rows"][0]["standardized_disk_diffusion_values"] == ">18 mm"
    assert result["antibiotic_rows"][0]["taxon_id_count"] == 3
    assert result["antibiotic_rows"][0]["isolation_type_count"] == 1
    assert result["antibiotic_rows"][0]["location_count"] == 1
    assert result["antibiotic_rows"][0]["collection_date_count"] == 1
    assert result["antibiotic_rows"][0]["create_date_count"] == 1
    assert result["antibiotic_rows"][0]["host_count"] == 1
    assert result["antibiotic_rows"][0]["isolation_source_count"] == 1
    assert result["antibiotic_rows"][0]["invalid_taxon_id_count"] == 1
    assert result["antibiotic_rows"][0]["taxon_ids"] == "NCBITaxon:562|NCBITaxon:573"
    assert (
        result["antibiotic_rows"][0]["taxon_labels"]
        == "Escherichia coli|Klebsiella pneumoniae"
    )
    assert result["antibiotic_rows"][0]["phenotypes"] == "R|S"


def test_evaluate_rows_counts_valid_project_context_separately():
    rows = [
        {
            "Antibiotic": "cefepime",
            "BioSample": "SAMN11953777",
            "BioProject": "PRJNA292666",
        },
        {
            "Antibiotic": "cefepime",
            "BioSample": "not-a-biosample",
            "BioProject": "PRJNA292666",
        },
        {
            "Antibiotic": "cefepime",
            "BioSample": "SAMN11953779",
            "BioProject": "not-a-bioproject",
        },
    ]

    result = evaluate_rows(
        rows,
        {"cefepime": {"CHEBI:478164"}},
        {"CHEBI:478164": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
    )

    assert result["rows_with_project_context"] == 3
    assert result["rows_with_valid_project_context"] == 1
    assert result["antibiotic_rows"][0]["project_context_count"] == 3
    assert result["antibiotic_rows"][0]["valid_project_context_count"] == 1


def test_evaluate_rows_normalizes_microgram_mic_headers_to_mg_per_l():
    rows = [
        {"Antibiotic": "cefepime", "MIC (ug/mL)": "2"},
        {"Antibiotic": "cefepime", "MIC (µg/mL)": "4"},
        {"Antibiotic": "cefepime", "AMR.MIC (μg/mL)": "8"},
    ]

    result = evaluate_rows(
        rows,
        {"cefepime": {"CHEBI:478164"}},
        {"CHEBI:478164": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
    )

    cefepime = result["antibiotic_rows"][0]
    assert cefepime["mic_count"] == 3
    assert cefepime["standardized_mic_count"] == 3
    assert cefepime["standardized_mic_values"] == "2 mg/L|4 mg/L|8 mg/L"


def test_evaluate_rows_counts_invalid_measurement_shapes():
    rows = [
        {"Antibiotic": "cefepime", "Measurement sign": "<=", "MIC": "2"},
        {"Antibiotic": "cefepime", "Measurement sign": "==", "MIC": "=3"},
        {"Antibiotic": "cefepime", "MIC": "0"},
        {"Antibiotic": "cefepime", "Measurement sign": "<", "MIC": ">4"},
        {"Antibiotic": "cefepime", "MIC": "not-numeric"},
        {"Antibiotic": "cefepime", "Measurement sign": ">", "Disk diffusion": "18"},
        {"Antibiotic": "cefepime", "Disk diffusion": "0"},
        {"Antibiotic": "cefepime", "Measurement sign": "approximately", "Disk diffusion": "19"},
    ]

    result = evaluate_rows(
        rows,
        {"cefepime": {"CHEBI:478164"}},
        {"CHEBI:478164": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
    )

    cefepime = result["antibiotic_rows"][0]
    assert cefepime["mic_count"] == 5
    assert cefepime["standardized_mic_count"] == 2
    assert cefepime["invalid_mic_count"] == 3
    assert cefepime["standardized_mic_values"] == "3 mg/L|<=2 mg/L"
    assert cefepime["disk_diffusion_count"] == 3
    assert cefepime["standardized_disk_diffusion_count"] == 1
    assert cefepime["invalid_disk_diffusion_count"] == 2
    assert cefepime["standardized_disk_diffusion_values"] == ">18 mm"


def test_evaluate_rows_enforces_ncbi_measurement_ranges():
    rows = [
        {"Antibiotic": "cefepime", "MIC": "1024"},
        {"Antibiotic": "cefepime", "MIC": "1024.1"},
        {"Antibiotic": "cefepime", "Disk diffusion": "6"},
        {"Antibiotic": "cefepime", "Disk diffusion": "5.9"},
        {"Antibiotic": "cefepime", "Disk diffusion": "150"},
        {"Antibiotic": "cefepime", "Disk diffusion": "150.1"},
    ]

    result = evaluate_rows(
        rows,
        {"cefepime": {"CHEBI:478164"}},
        {"CHEBI:478164": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
    )

    cefepime = result["antibiotic_rows"][0]
    assert cefepime["mic_count"] == 2
    assert cefepime["standardized_mic_count"] == 1
    assert cefepime["invalid_mic_count"] == 1
    assert cefepime["standardized_mic_values"] == "1024 mg/L"
    assert cefepime["disk_diffusion_count"] == 4
    assert cefepime["standardized_disk_diffusion_count"] == 2
    assert cefepime["invalid_disk_diffusion_count"] == 2
    assert cefepime["standardized_disk_diffusion_values"] == "150 mm|6 mm"


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
            "source_version",
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
            "2026-09-26-ast-browser\tamikacin\t amikacin \tEXACT\tCHEBI:2637\t"
            "LKCWBDHBTVXHDL-RMDFUYIESA-N\tparent_base\tok",
            "2026-09-26-ast-browser\tgentamicin\tgentamicin\tMIXTURE\t\t\tnone\tmixture",
        ])
        + "\n",
        encoding="utf-8",
    )

    mappings = read_drug_map(
        path,
        {"CHEBI:2637": "LKCWBDHBTVXHDL-RMDFUYIESA-N"},
        source_version="2026-09-26-ast-browser",
    )

    assert mappings["amikacin"]["identifier"] == "CHEBI:2637"
    assert mappings["amikacin"]["source_name"] == "amikacin"
    assert mappings["gentamicin"]["mapping_status"] == "MIXTURE"
    assert mappings["gentamicin"]["identifier"] == ""


def test_read_drug_map_rejects_identity_drift(tmp_path):
    path = tmp_path / "ncbi_ast_antibiotic_map.tsv"
    path.write_text(
        "\t".join([
            "source_version",
            "source_record_id",
            "source_name",
            "mapping_status",
            "identifier",
            "standard_inchi_key",
            "mapping_basis",
            "notes",
        ])
        + (
            "\n2026-09-26-ast-browser\tamikacin\tamikacin\tEXACT\t"
            "CHEBI:2637\tWRONGINCHIKEY\tparent_base\tok\n"
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="does not match CHEBI:2637"):
        read_drug_map(
            path,
            {"CHEBI:2637": "LKCWBDHBTVXHDL-RMDFUYIESA-N"},
            source_version="2026-09-26-ast-browser",
        )


def test_read_drug_map_rejects_source_version_drift(tmp_path):
    path = tmp_path / "ncbi_ast_antibiotic_map.tsv"
    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + (
            "\n2026-09-25-ast-browser\tamikacin\tamikacin\tMIXTURE\t\t\t"
            "none\tmixture\n"
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="source_version '2026-09-25-ast-browser'"):
        read_drug_map(path, {}, source_version="2026-09-26-ast-browser")


def test_read_drug_map_rejects_header_only_maps(tmp_path):
    path = tmp_path / "ncbi_ast_antibiotic_map.tsv"
    path.write_text("\t".join(DRUG_MAP_COLUMNS) + "\n", encoding="utf-8")

    with pytest.raises(ValueError, match="NCBI AST drug map has no rows"):
        read_drug_map(path, {}, source_version="2026-09-26-ast-browser")


def test_read_drug_map_rejects_malformed_rows(tmp_path):
    path = tmp_path / "ncbi_ast_antibiotic_map.tsv"
    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + "2026-09-26-ast-browser\tamikacin\tamikacin\tMIXTURE\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="identifier is missing"):
        read_drug_map(path, {}, source_version="2026-09-26-ast-browser")

    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + "2026-09-26-ast-browser\tamikacin\tamikacin\tMIXTURE\t\t\tnone\tok\textra\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="unexpected extra delimited field"):
        read_drug_map(path, {}, source_version="2026-09-26-ast-browser")

    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + '2026-09-26-ast-browser\tamikacin\tamikacin\tMIXTURE\t\t\tnone\t"ambiguous\nname"\n',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="notes contains a tab or newline"):
        read_drug_map(path, {}, source_version="2026-09-26-ast-browser")

    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + '2026-09-26-ast-browser\tamikacin\tamikacin\tMIXTURE\t\t\tnone\t"ambiguous\tname"\n',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="notes contains a tab or newline"):
        read_drug_map(path, {}, source_version="2026-09-26-ast-browser")

    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + '2026-09-26-ast-browser\tamikacin\tamikacin\tMIXTURE\t\t\tnone\t"ambiguous\n"\n',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="notes contains a tab or newline"):
        read_drug_map(path, {}, source_version="2026-09-26-ast-browser")


def test_read_drug_map_requires_mapping_rationale(tmp_path):
    path = tmp_path / "ncbi_ast_antibiotic_map.tsv"
    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + "2026-09-26-ast-browser\tamikacin\tamikacin\tMIXTURE\t\t\t \tmixture\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="mapping_basis is required"):
        read_drug_map(path, {}, source_version="2026-09-26-ast-browser")

    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + "2026-09-26-ast-browser\tamikacin\tamikacin\tMIXTURE\t\t\tnone\t \n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="notes is required"):
        read_drug_map(path, {}, source_version="2026-09-26-ast-browser")


def test_read_project_dedupe_map_accepts_biosample_and_bioproject_keys(tmp_path):
    path = tmp_path / "ncbi_ast_project_dedupe.tsv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=PROJECT_DEDUPE_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows([
            {
                "accession_type": "BioSample",
                "accession": "SAMN11953777",
                "source": " CRYPTIC ",
                "source_version": "3.4.0",
                "notes": "BioSample represented in an adopted project dataset.",
            },
            {
                "accession_type": "BioProject",
                "accession": "PRJNA292666",
                "source": "CRYPTIC",
                "source_version": "3.4.0",
                "notes": "Whole project represented elsewhere.",
            },
        ])

    rows = read_project_dedupe_map(path)

    assert rows[("BioSample", "SAMN11953777")]["source"] == "CRYPTIC"
    assert rows[("BioProject", "PRJNA292666")]["source_version"] == "3.4.0"


def test_read_project_dedupe_map_uses_current_adopted_source_versions(
    tmp_path,
    monkeypatch,
):
    inventory = tmp_path / "cryptic_activity.tsv"
    inventory.write_text(
        "source_version\tactivity_group_id\n"
        "3.5.0\tcryptic:test\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        evaluate_ncbi_ast,
        "PROJECT_DEDUPE_SOURCE_INVENTORIES",
        {"CRYPTIC": inventory},
    )
    path = tmp_path / "ncbi_ast_project_dedupe.tsv"
    path.write_text(
        "\t".join(PROJECT_DEDUPE_COLUMNS)
        + "\n"
        + (
            "BioSample\tSAMN11953777\tCRYPTIC\t3.5.0\t"
            "BioSample represented in the current CRyPTIC report.\n"
        ),
        encoding="utf-8",
    )

    rows = read_project_dedupe_map(path)

    assert rows[("BioSample", "SAMN11953777")]["source_version"] == "3.5.0"


def test_project_dedupe_source_versions_require_one_version(tmp_path):
    inventory = tmp_path / "cryptic_activity.tsv"
    inventory.write_text(
        "source_version\tactivity_group_id\n"
        "3.4.0\tcryptic:one\n"
        "3.5.0\tcryptic:two\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="expected one CRYPTIC source_version for project dedupe",
    ):
        project_dedupe_source_versions({"CRYPTIC": inventory})


def test_read_project_dedupe_map_rejects_bad_accessions(tmp_path):
    path = tmp_path / "ncbi_ast_project_dedupe.tsv"
    path.write_text(
        "\t".join(PROJECT_DEDUPE_COLUMNS)
        + "\n"
        + "BioProject\tSAMN11953777\tCRYPTIC\t3.4.0\twrong accession type\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="invalid BioProject accession"):
        read_project_dedupe_map(path)


def test_read_project_dedupe_map_rejects_malformed_rows(tmp_path):
    path = tmp_path / "ncbi_ast_project_dedupe.tsv"
    path.write_text(
        "\t".join(PROJECT_DEDUPE_COLUMNS)
        + "\n"
        + "BioSample\tSAMN11953777\tCRYPTIC\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="source_version is missing"):
        read_project_dedupe_map(path)

    path.write_text(
        "\t".join(PROJECT_DEDUPE_COLUMNS)
        + "\n"
        + "BioSample\tSAMN11953777\tCRYPTIC\t3.4.0\tnotes\textra\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="unexpected extra delimited field"):
        read_project_dedupe_map(path)

    path.write_text(
        "\t".join(PROJECT_DEDUPE_COLUMNS)
        + "\n"
        + 'BioSample\tSAMN11953777\tCRYPTIC\t3.4.0\t"BioSample\nrepresented"\n',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="notes contains a tab or newline"):
        read_project_dedupe_map(path)

    path.write_text(
        "\t".join(PROJECT_DEDUPE_COLUMNS)
        + "\n"
        + 'BioSample\tSAMN11953777\tCRYPTIC\t3.4.0\t"BioSample\trepresented"\n',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="notes contains a tab or newline"):
        read_project_dedupe_map(path)

    path.write_text(
        "\t".join(PROJECT_DEDUPE_COLUMNS)
        + "\n"
        + 'BioSample\tSAMN11953777\tCRYPTIC\t3.4.0\t"\nrepresented"\n',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="notes contains a tab or newline"):
        read_project_dedupe_map(path)


def test_read_project_dedupe_map_requires_source_version(tmp_path):
    path = tmp_path / "ncbi_ast_project_dedupe.tsv"
    path.write_text(
        "\t".join(PROJECT_DEDUPE_COLUMNS)
        + "\n"
        + "BioSample\tSAMN11953777\tCRYPTIC\t \tBioSample represented elsewhere.\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="source_version is required"):
        read_project_dedupe_map(path)


def test_read_project_dedupe_map_requires_notes(tmp_path):
    path = tmp_path / "ncbi_ast_project_dedupe.tsv"
    path.write_text(
        "\t".join(PROJECT_DEDUPE_COLUMNS)
        + "\n"
        + "BioSample\tSAMN11953777\tCRYPTIC\t3.4.0\t \n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="notes is required"):
        read_project_dedupe_map(path)


def test_read_project_dedupe_map_rejects_self_source(tmp_path):
    path = tmp_path / "ncbi_ast_project_dedupe.tsv"
    path.write_text(
        "\t".join(PROJECT_DEDUPE_COLUMNS)
        + "\n"
        + "BioSample\tSAMN11953777\t NCBI AST \t2026-09\tnot a separate adopted source\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="source cannot be NCBI_AST"):
        read_project_dedupe_map(path)


def test_read_project_dedupe_map_rejects_unknown_source(tmp_path):
    path = tmp_path / "ncbi_ast_project_dedupe.tsv"
    path.write_text(
        "\t".join(PROJECT_DEDUPE_COLUMNS)
        + "\n"
        + "BioSample\tSAMN11953777\tCRPTIC\t3.4.0\tunknown source owner\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="unsupported project dedupe source 'CRPTIC'"):
        read_project_dedupe_map(path)


def test_read_project_dedupe_map_rejects_stale_source_version(tmp_path):
    path = tmp_path / "ncbi_ast_project_dedupe.tsv"
    path.write_text(
        "\t".join(PROJECT_DEDUPE_COLUMNS)
        + "\n"
        + (
            "BioSample\tSAMN11953777\tCRYPTIC\t3.3.0\t"
            "BioSample represented in an earlier CRyPTIC release.\n"
        ),
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match=r"CRYPTIC project dedupe source_version '3\.3\.0' != '3\.4\.0'",
    ):
        read_project_dedupe_map(path)


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
            "project_context_count": 7,
            "valid_project_context_count": 7,
            "dedupe_context_count": 0,
            "activity_report_candidate_count": 7,
            "activity_report_dedupe_excluded_count": 2,
            "target_acc_count": 7,
            "invalid_target_acc_count": 0,
            "assembly_acc_count": 7,
            "invalid_assembly_acc_count": 0,
            "sra_accessions_count": 7,
            "invalid_sra_accessions_count": 0,
            "isolation_type_count": 7,
            "location_count": 7,
            "collection_date_count": 7,
            "create_date_count": 7,
            "invalid_create_date_count": 0,
            "host_count": 7,
            "isolation_source_count": 7,
            "taxon_id_count": 7,
            "invalid_taxon_id_count": 0,
            "taxon_count": 7,
            "assay_method_count": 7,
            "phenotype_count": 7,
            "invalid_phenotype_count": 0,
            "mic_count": 7,
            "standardized_mic_count": 7,
            "invalid_mic_count": 0,
            "standardized_mic_values": "<=2 mg/L",
            "disk_diffusion_count": 0,
            "standardized_disk_diffusion_count": 0,
            "invalid_disk_diffusion_count": 0,
            "standardized_disk_diffusion_values": "",
            "taxon_ids": "NCBITaxon:562",
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
        "project_context_count": "7",
        "valid_project_context_count": "7",
        "dedupe_context_count": "0",
        "activity_report_candidate_count": "7",
        "activity_report_dedupe_excluded_count": "2",
        "target_acc_count": "7",
        "invalid_target_acc_count": "0",
        "assembly_acc_count": "7",
        "invalid_assembly_acc_count": "0",
        "sra_accessions_count": "7",
        "invalid_sra_accessions_count": "0",
        "isolation_type_count": "7",
        "location_count": "7",
        "collection_date_count": "7",
        "create_date_count": "7",
        "invalid_create_date_count": "0",
        "host_count": "7",
        "isolation_source_count": "7",
        "taxon_id_count": "7",
        "invalid_taxon_id_count": "0",
        "taxon_count": "7",
        "assay_method_count": "7",
        "phenotype_count": "7",
        "invalid_phenotype_count": "0",
        "mic_count": "7",
        "standardized_mic_count": "7",
        "invalid_mic_count": "0",
        "standardized_mic_values": "<=2 mg/L",
        "disk_diffusion_count": "0",
        "standardized_disk_diffusion_count": "0",
        "invalid_disk_diffusion_count": "0",
        "standardized_disk_diffusion_values": "",
        "taxon_ids": "NCBITaxon:562",
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

    write_drug_map_template(
        rows,
        path,
        source_version="2026-09-26-ast-browser",
    )

    with path.open(newline="", encoding="utf-8") as handle:
        actual = list(csv.DictReader(handle, delimiter="\t"))

    assert actual == [
        {
            "source_version": "2026-09-26-ast-browser",
            "source_record_id": "cefepime",
            "source_name": "cefepime",
            "mapping_status": "EXACT",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
            "mapping_basis": "parent_base",
            "notes": "NCBI names the active cefepime parent.",
        },
        {
            "source_version": "2026-09-26-ast-browser",
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
            "source_version": "2026-09-26-ast-browser",
            "source_retrieved_on": "2026-09-26",
            "ast_row_count": 2,
            "isolate_count": 1,
            "source_name": "cefepime",
            "normalized_antibiotic": "cefepime",
            "identifier": "CHEBI:478164",
            "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli and Shigella",
            "strain": "CDC-1234",
            "biosample_accession": "SAMN11953777",
            "bioproject_accession": "PRJNA292666",
            "target_accession": "PDT000001234.1",
            "assembly_accession": "GCF_003123125.1",
            "sra_accessions": "ERR111111|SRR222222",
            "isolation_type": "clinical",
            "location": "USA",
            "collection_date": "2020",
            "create_date": "2020-01-31",
            "host": "Homo sapiens",
            "isolation_source": "blood",
            "phenotype": "R",
            "activity": "RESISTANT",
            "mic_value": "2",
            "mic_qualifier": "<=",
            "mic_units": "mg/L",
            "disk_diffusion_value": "",
            "disk_diffusion_qualifier": "",
            "disk_diffusion_units": "",
            "method": "MIC",
            "platform": "AST",
            "vendor": "NCBI",
            "reagent": "Sensititre GNX2F",
            "standard": "CLSI",
        }
    ]
    rows[0]["activity_group_id"] = activity_group_id(rows[0])

    write_activity_report(rows, path)

    with path.open(newline="", encoding="utf-8") as handle:
        actual = list(csv.DictReader(handle, delimiter="\t"))

    assert actual == [{
        "activity_group_id": rows[0]["activity_group_id"],
        "source_version": "2026-09-26-ast-browser",
        "source_retrieved_on": "2026-09-26",
        "ast_row_count": "2",
        "isolate_count": "1",
        "source_name": "cefepime",
        "normalized_antibiotic": "cefepime",
        "identifier": "CHEBI:478164",
        "standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N",
        "taxon_id": "NCBITaxon:562",
        "taxon_label": "Escherichia coli and Shigella",
        "strain": "CDC-1234",
        "biosample_accession": "SAMN11953777",
        "bioproject_accession": "PRJNA292666",
        "target_accession": "PDT000001234.1",
        "assembly_accession": "GCF_003123125.1",
        "sra_accessions": "ERR111111|SRR222222",
        "isolation_type": "clinical",
        "location": "USA",
        "collection_date": "2020",
        "create_date": "2020-01-31",
        "host": "Homo sapiens",
        "isolation_source": "blood",
        "phenotype": "R",
        "activity": "RESISTANT",
        "mic_value": "2",
        "mic_qualifier": "<=",
        "mic_units": "mg/L",
        "disk_diffusion_value": "",
        "disk_diffusion_qualifier": "",
        "disk_diffusion_units": "",
        "method": "MIC",
        "platform": "AST",
        "vendor": "NCBI",
        "reagent": "Sensititre GNX2F",
        "standard": "CLSI",
    }]


def test_write_activity_report_rejects_empty_reports_before_opening(tmp_path):
    path = tmp_path / "ncbi_ast_activity.tsv"
    path.write_text("keep me\n", encoding="utf-8")

    with pytest.raises(ValueError, match="NCBI AST activity report has no rows"):
        write_activity_report([], path)

    assert path.read_text(encoding="utf-8") == "keep me\n"


@pytest.mark.parametrize(
    ("overrides", "message"),
    [
        ({"source_version": ""}, "source_version is required"),
        (
            {"source_version": " 2026-09-26-ast-browser "},
            "source_version has leading or trailing whitespace",
        ),
        ({"source_version": "2026-09-26\tast-browser"}, "source_version contains"),
        ({"source_retrieved_on": ""}, "source_retrieved_on is required"),
        (
            {"source_retrieved_on": "20260926"},
            "source_retrieved_on must be an ISO date",
        ),
        ({"method": "MIC\nbroth"}, "method contains"),
        ({"method": " MIC"}, "method has leading or trailing whitespace"),
        ({"ast_row_count": "0"}, "ast_row_count must be positive"),
        ({"ast_row_count": "02"}, "ast_row_count must use canonical integer '2'"),
        ({"isolate_count": "0"}, "isolate_count must be positive"),
        ({"isolate_count": "02"}, "isolate_count must use canonical integer '2'"),
        (
            {"isolate_count": "2"},
            "isolate_count must be 1 for a BioSample-grouped row",
        ),
        ({"taxon_label": ""}, "taxon_label is required"),
        ({"biosample_accession": ""}, "biosample_accession is required"),
        ({"biosample_accession": "BioSample:SAMN11953777"}, "invalid BioSample"),
        ({"bioproject_accession": "SAMN11953777"}, "invalid BioProject"),
        ({"taxon_id": "562"}, "invalid NCBI Taxonomy CURIE"),
        ({"taxon_id": "NCBITaxon:0"}, "invalid NCBI Taxonomy CURIE"),
        ({"taxon_id": "NCBITaxon:000562"}, "invalid NCBI Taxonomy CURIE"),
        (
            {"target_accession": "GCF_003123125.1"},
            "invalid Pathogen Detection target",
        ),
        ({"assembly_accession": "SAMN11953777"}, "invalid Assembly accession"),
        ({"sra_accessions": "SAMN11953777"}, "invalid SRA accession"),
        (
            {"sra_accessions": "SRR222222|ERR111111"},
            "sra_accessions must be unique and sorted",
        ),
        (
            {"sra_accessions": "ERR111111|ERR111111"},
            "sra_accessions must be unique and sorted",
        ),
        (
            {"normalized_antibiotic": "stale"},
            "normalized_antibiotic must match source_name",
        ),
        (
            {"method": "", "platform": "", "reagent": ""},
            "method, platform or reagent is required",
        ),
        ({"create_date": "20200131"}, "create_date must be an ISO date"),
        (
            {"phenotype": "non-susceptible", "activity": ""},
            "unsupported phenotype",
        ),
        ({"activity": "NON_SUSCEPTIBLE"}, "activity must match phenotype"),
        ({"phenotype": "S", "activity": "RESISTANT"}, "activity must match phenotype"),
        ({"mic_value": "high"}, "mic_value must be numeric"),
        ({"mic_value": "2.0"}, "mic_value must use canonical decimal '2'"),
        ({"mic_value": "0"}, "mic_value must be positive"),
        ({"mic_value": "1024.1"}, "mic_value must be at most 1024"),
        ({"mic_qualifier": "MIC90"}, "mic_qualifier has invalid qualifier"),
        (
            {"mic_value": "", "mic_qualifier": "<=", "mic_units": ""},
            "mic_qualifier requires mic_value",
        ),
        (
            {
                "mic_value": "",
                "mic_qualifier": "",
                "mic_units": "mg/L",
            },
            "mic_units requires mic_value",
        ),
        (
            {"disk_diffusion_value": "5", "disk_diffusion_units": "mm"},
            "disk_diffusion_value must be at least 6",
        ),
        (
            {"disk_diffusion_value": "150.1", "disk_diffusion_units": "mm"},
            "disk_diffusion_value must be at most 150",
        ),
        (
            {"disk_diffusion_value": "0", "disk_diffusion_units": "mm"},
            "disk_diffusion_value must be positive",
        ),
        (
            {"mic_value": "", "mic_qualifier": "", "mic_units": ""},
            "mic_value or disk_diffusion_value is required",
        ),
        ({"activity_group_id": "ncbi_ast:stale"}, "activity_group_id must be"),
    ],
)
def test_write_activity_report_rejects_malformed_rows_before_opening(
    tmp_path,
    overrides,
    message,
):
    path = tmp_path / "ncbi_ast_activity.tsv"
    path.write_text("keep me\n", encoding="utf-8")

    with pytest.raises(ValueError, match=message):
        write_activity_report([ncbi_ast_activity_report_row(**overrides)], path)

    assert path.read_text(encoding="utf-8") == "keep me\n"


def test_write_activity_report_rejects_mixed_source_metadata_before_opening(tmp_path):
    path = tmp_path / "ncbi_ast_activity.tsv"
    path.write_text("keep me\n", encoding="utf-8")

    with pytest.raises(ValueError, match="source_version must be"):
        write_activity_report(
            [
                ncbi_ast_activity_report_row(),
                ncbi_ast_activity_report_row(
                    biosample_accession="SAMN11953778",
                    source_version="2026-09-27-ast-browser",
                ),
            ],
            path,
        )

    with pytest.raises(ValueError, match="source_retrieved_on must be '2026-09-26'"):
        write_activity_report(
            [
                ncbi_ast_activity_report_row(),
                ncbi_ast_activity_report_row(
                    biosample_accession="SAMN11953778",
                    source_retrieved_on="2026-09-27",
                ),
            ],
            path,
        )

    assert path.read_text(encoding="utf-8") == "keep me\n"


def test_write_activity_report_rejects_duplicate_groups_before_opening(tmp_path):
    path = tmp_path / "ncbi_ast_activity.tsv"
    path.write_text("keep me\n", encoding="utf-8")
    row = ncbi_ast_activity_report_row()

    with pytest.raises(ValueError, match="duplicate activity_group_id"):
        write_activity_report([row, row], path)

    assert path.read_text(encoding="utf-8") == "keep me\n"


def test_project_dedupe_report_is_a_stable_tsv(tmp_path):
    path = tmp_path / "ncbi_ast_project_dedupe_report.tsv"
    rows = [
        {
            "accession_type": "BioProject",
            "accession": "PRJNA292666",
            "ast_rows": 7,
            "exact_mapped_rows": 6,
            "exact_mapped_antibiotic_values": 2,
            "exact_mapped_antibiotics": "amikacin|cefepime",
            "exact_mapped_identifiers": "CHEBI:2637|CHEBI:478164",
            "biosample_count": 3,
            "bioproject_count": 1,
            "antibiotic_values": 2,
            "antibiotics": "amikacin|cefepime",
            "taxon_ids": "NCBITaxon:562",
            "taxon_labels": "Escherichia coli",
        },
    ]

    write_project_dedupe_report(rows, path)

    with path.open(newline="", encoding="utf-8") as handle:
        actual = list(csv.DictReader(handle, delimiter="\t"))

    assert actual == [{
        "accession_type": "BioProject",
        "accession": "PRJNA292666",
        "ast_rows": "7",
        "exact_mapped_rows": "6",
        "exact_mapped_antibiotic_values": "2",
        "exact_mapped_antibiotics": "amikacin|cefepime",
        "exact_mapped_identifiers": "CHEBI:2637|CHEBI:478164",
        "biosample_count": "3",
        "bioproject_count": "1",
        "antibiotic_values": "2",
        "antibiotics": "amikacin|cefepime",
        "taxon_ids": "NCBITaxon:562",
        "taxon_labels": "Escherichia coli",
    }]


@pytest.mark.parametrize(
    ("writer", "partial_row", "missing_column"),
    [
        (write_antibiotic_report, {"antibiotic": "cefepime"}, "normalized_antibiotic"),
        (write_project_dedupe_report, {"accession_type": "BioProject"}, "accession"),
        (write_activity_report, {"activity_group_id": "ncbi_ast:test"}, "source_version"),
    ],
)
def test_report_writers_reject_missing_columns(
    tmp_path,
    writer,
    partial_row,
    missing_column,
):
    path = tmp_path / "report.tsv"
    path.write_text("keep me\n", encoding="utf-8")

    with pytest.raises(ValueError, match=fr"missing columns: {missing_column}"):
        writer([partial_row], path)

    assert path.read_text(encoding="utf-8") == "keep me\n"


@pytest.mark.parametrize(
    ("writer", "fieldnames"),
    [
        (write_antibiotic_report, ANTIBIOTIC_REPORT_COLUMNS),
        (write_project_dedupe_report, PROJECT_DEDUPE_REPORT_COLUMNS),
        (write_activity_report, ACTIVITY_REPORT_COLUMNS),
    ],
)
def test_report_writers_reject_unexpected_columns(tmp_path, writer, fieldnames):
    path = tmp_path / "report.tsv"
    path.write_text("keep me\n", encoding="utf-8")
    row = {field: "" for field in fieldnames}
    row["unexpected"] = "value"

    with pytest.raises(ValueError, match="unexpected columns: unexpected"):
        writer([row], path)

    assert path.read_text(encoding="utf-8") == "keep me\n"


def test_project_dedupe_map_template_is_fillable_by_the_curator(tmp_path):
    path = tmp_path / "ncbi_ast_project_dedupe.tsv"
    rows = [
        {
            "accession_type": "BioProject",
            "accession": "PRJNA292666",
            "ast_rows": 7,
        },
        {
            "accession_type": "BioSample",
            "accession": "SAMN11953777",
            "ast_rows": 1,
        },
    ]

    write_project_dedupe_map_template(rows, path)

    with path.open(newline="", encoding="utf-8") as handle:
        actual = list(csv.DictReader(handle, delimiter="\t"))

    assert actual == [
        {
            "accession_type": "BioProject",
            "accession": "PRJNA292666",
            "source": "",
            "source_version": "",
            "notes": "",
        },
        {
            "accession_type": "BioSample",
            "accession": "SAMN11953777",
            "source": "",
            "source_version": "",
            "notes": "",
        },
    ]


@pytest.mark.parametrize(
    ("writer", "partial_row", "missing_column"),
    [
        (
            lambda rows, path: write_drug_map_template(
                rows,
                path,
                source_version="2026-09-26-ast-browser",
            ),
            {"normalized_antibiotic": "cefepime"},
            "antibiotic",
        ),
        (
            write_project_dedupe_map_template,
            {"accession_type": "BioProject"},
            "accession",
        ),
    ],
)
def test_template_writers_reject_missing_input_columns(
    tmp_path,
    writer,
    partial_row,
    missing_column,
):
    path = tmp_path / "report.tsv"
    path.write_text("keep me\n", encoding="utf-8")

    with pytest.raises(ValueError, match=fr"missing columns: {missing_column}"):
        writer([partial_row], path)

    assert path.read_text(encoding="utf-8") == "keep me\n"


@pytest.mark.parametrize(
    ("writer", "row", "message"),
    [
        (
            write_antibiotic_report,
            ncbi_ast_antibiotic_report_row(antibiotic=None),
            "antibiotic is missing",
        ),
        (
            write_antibiotic_report,
            ncbi_ast_antibiotic_report_row(mapping_notes="curated\nnote"),
            "mapping_notes contains a tab or newline",
        ),
        (
            write_antibiotic_report,
            ncbi_ast_antibiotic_report_row(mapping_basis=" parent_base"),
            "mapping_basis has leading or trailing whitespace",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(accession=None),
            "accession is missing",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(taxon_labels="Escherichia\tcoli"),
            "taxon_labels contains a tab or newline",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(taxon_ids=" NCBITaxon:562"),
            "taxon_ids has leading or trailing whitespace",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(accession_type="Assembly"),
            "unsupported accession_type",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(accession="SAMN11953777"),
            "invalid BioProject accession",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(ast_rows="07"),
            "ast_rows must use canonical integer '7'",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(
                ast_rows=2,
                exact_mapped_rows=3,
            ),
            "exact_mapped_rows must be <= ast_rows",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(
                exact_mapped_antibiotic_values=1,
            ),
            "exact_mapped_antibiotic_values must match exact_mapped_antibiotics",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(
                exact_mapped_rows=1,
            ),
            "exact_mapped_antibiotic_values must be <= exact_mapped_rows",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(biosample_count=8),
            "biosample_count must be <= ast_rows",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(bioproject_count=8),
            "bioproject_count must be <= ast_rows",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(
                exact_mapped_identifiers="CHEBI:2637|CHEBI:478164|CHEBI:63638",
            ),
            "exact_mapped_identifiers must have no more values",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(antibiotics="cefepime|amikacin"),
            "antibiotics must be unique and sorted",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(taxon_ids="NCBITaxon:0"),
            "invalid taxon_ids value",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(taxon_labels="Klebsiella|Escherichia"),
            "taxon_labels must be unique and sorted",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(taxon_labels=""),
            "taxon_labels is required",
        ),
        (
            write_project_dedupe_report,
            ncbi_ast_project_dedupe_report_row(bioproject_count=2),
            "bioproject_count must be 1 for BioProject rows",
        ),
        (
            lambda rows, path: write_drug_map_template(
                rows,
                path,
                source_version="2026-09-26-ast-browser",
            ),
            ncbi_ast_drug_map_template_row(antibiotic=None),
            "antibiotic is missing",
        ),
        (
            lambda rows, path: write_drug_map_template(
                rows,
                path,
                source_version="2026-09-26-ast-browser",
            ),
            ncbi_ast_drug_map_template_row(mapping_notes="curated\nnote"),
            "mapping_notes contains a tab or newline",
        ),
        (
            write_project_dedupe_map_template,
            ncbi_ast_project_dedupe_template_row(accession_type=" BioProject"),
            "accession_type has leading or trailing whitespace",
        ),
        (
            write_project_dedupe_map_template,
            ncbi_ast_project_dedupe_template_row(accession="PRJNA292666\r"),
            "accession contains a tab or newline",
        ),
        (
            write_project_dedupe_map_template,
            ncbi_ast_project_dedupe_template_row(accession_type="Assembly"),
            "unsupported accession_type",
        ),
        (
            write_project_dedupe_map_template,
            ncbi_ast_project_dedupe_template_row(accession="SAMN11953777"),
            "invalid BioProject accession",
        ),
    ],
)
def test_curation_report_writers_reject_malformed_values_before_opening(
    tmp_path,
    writer,
    row,
    message,
):
    path = tmp_path / "report.tsv"
    path.write_text("keep me\n", encoding="utf-8")

    with pytest.raises(ValueError, match=message):
        writer([row], path)

    assert path.read_text(encoding="utf-8") == "keep me\n"


@pytest.mark.parametrize(
    ("source_version", "message"),
    [
        (None, "source_version is missing"),
        ("", "source_version is required"),
        ("2026-09-26\nast-browser", "source_version contains a tab or newline"),
        (
            " 2026-09-26-ast-browser ",
            "source_version has leading or trailing whitespace",
        ),
    ],
)
def test_drug_map_template_rejects_malformed_source_version_before_opening(
    tmp_path,
    source_version,
    message,
):
    path = tmp_path / "report.tsv"
    path.write_text("keep me\n", encoding="utf-8")

    with pytest.raises(ValueError, match=message):
        write_drug_map_template(
            [ncbi_ast_drug_map_template_row()],
            path,
            source_version=source_version,
        )

    assert path.read_text(encoding="utf-8") == "keep me\n"


def test_cli_writes_all_ncbi_ast_reports(tmp_path):
    ast = tmp_path / "ast.tsv"
    with ast.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "antibiotic",
                "biosample_acc",
                "bioproject_acc",
                "Isolate",
                "asm_acc",
                "Run",
                "Isolation type",
                "Location",
                "Collection date",
                "Create date",
                "Host",
                "Isolation source",
                "TaxID",
                "scientific_name",
                "strain",
                "Laboratory typing method",
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
            "Isolate": "PDT000001234.1",
            "asm_acc": "GCF_003123125.1",
            "Run": "SRR222222,ERR111111",
            "Isolation type": "clinical",
            "Location": "USA",
            "Collection date": "2020",
            "Create date": "2020-01-31",
            "Host": "Homo sapiens",
            "Isolation source": "blood",
            "TaxID": "573",
            "scientific_name": "Klebsiella pneumoniae",
            "strain": "KPNIH1",
            "Laboratory typing method": "MIC",
            "phenotype": "R",
            "measurement_sign": ">",
            "mic": "64",
            "platform": "AST",
            "vendor": "NCBI",
            "reagent": "broth microdilution",
            "standard": "CLSI",
        })
        writer.writerow({
            "antibiotic": "amikacin",
            "biosample_acc": "SAMN11953778",
            "bioproject_acc": "PRJNA292667",
            "Isolate": "PDT000001235.1",
            "asm_acc": "GCF_003123126.1",
            "Run": "SRR222223",
            "TaxID": "573",
            "scientific_name": "Klebsiella pneumoniae",
            "Laboratory typing method": "MIC",
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
            "source_version": "2026-09-26-ast-browser",
            "source_record_id": "amikacin",
            "source_name": "amikacin",
            "mapping_status": "EXACT",
            "identifier": "CHEBI:2637",
            "standard_inchi_key": structure_keys["CHEBI:2637"],
            "mapping_basis": "parent_base",
            "notes": "NCBI names the active amikacin parent.",
        })

    project_dedupe = tmp_path / "ncbi_ast_project_dedupe.tsv"
    with project_dedupe.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=PROJECT_DEDUPE_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerow({
            "accession_type": "BioProject",
            "accession": "PRJNA292667",
            "source": "CRYPTIC",
            "source_version": "3.4.0",
            "notes": "Project represented in an adopted source lane.",
        })

    antibiotic_report = tmp_path / "ncbi_ast_antibiotics.tsv"
    template = tmp_path / "ncbi_ast_drug_map_template.tsv"
    project_report = tmp_path / "ncbi_ast_project_dedupe_report.tsv"
    project_template = tmp_path / "ncbi_ast_project_dedupe_template.tsv"
    activity_report = tmp_path / "ncbi_ast_activity.tsv"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--ast",
            str(ast),
            "--drug-map",
            str(drug_map),
            "--project-dedupe-map",
            str(project_dedupe),
            "--antibiotic-report",
            str(antibiotic_report),
            "--drug-map-template",
            str(template),
            "--project-dedupe-report",
            str(project_report),
            "--project-dedupe-map-template",
            str(project_template),
            "--activity-report",
            str(activity_report),
            "--source-version",
            "2026-09-26-ast-browser",
            "--source-retrieved-on",
            "2026-09-26",
        ],
        check=True,
        text=True,
        capture_output=True,
    )

    assert "exact_mapped_activity_groups=1" in result.stdout
    assert "activity_report_candidate_rows=1" in result.stdout
    assert "project_context_rows=2" in result.stdout
    assert "valid_project_context_rows=2" in result.stdout
    assert "taxon_id_rows=2" in result.stdout
    assert "taxon_rows=2" in result.stdout
    assert "phenotype_rows=2" in result.stdout
    assert "invalid_phenotype_rows=0" in result.stdout
    assert "assay_method_rows=2" in result.stdout
    assert "isolation_type_rows=1" in result.stdout
    assert "location_rows=1" in result.stdout
    assert "collection_date_rows=1" in result.stdout
    assert "create_date_rows=1" in result.stdout
    assert "invalid_create_date_rows=0" in result.stdout
    assert "host_rows=1" in result.stdout
    assert "isolation_source_rows=1" in result.stdout
    assert "source_context_rows=1" in result.stdout
    assert "activity_report_dedupe_excluded_rows=1" in result.stdout
    assert "unused_antibiotics=0" in result.stdout
    assert "unused_source_contexts=0" in result.stdout
    assert "project_dedupe_report=" in result.stdout
    assert "project_dedupe_map_template=" in result.stdout
    assert antibiotic_report.exists()
    with antibiotic_report.open(newline="", encoding="utf-8") as handle:
        antibiotic_rows = list(csv.DictReader(handle, delimiter="\t"))

    assert antibiotic_rows[0]["isolation_type_count"] == "1"
    assert antibiotic_rows[0]["location_count"] == "1"
    assert antibiotic_rows[0]["collection_date_count"] == "1"
    assert antibiotic_rows[0]["create_date_count"] == "1"
    assert antibiotic_rows[0]["invalid_create_date_count"] == "0"
    assert antibiotic_rows[0]["host_count"] == "1"
    assert antibiotic_rows[0]["isolation_source_count"] == "1"
    assert antibiotic_rows[0]["activity_report_dedupe_excluded_count"] == "1"

    with template.open(newline="", encoding="utf-8") as handle:
        assert list(csv.DictReader(handle, delimiter="\t"))[0]["source_record_id"] == "amikacin"

    with activity_report.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        activity_rows = list(reader)
        assert "target_accession" in (reader.fieldnames or [])
        assert "assembly_accession" in (reader.fieldnames or [])
        assert "sra_accessions" in (reader.fieldnames or [])
        assert "isolation_type" in (reader.fieldnames or [])
        assert "isolation_source" in (reader.fieldnames or [])
        assert "taxon_id" in (reader.fieldnames or [])
        assert "strain" in (reader.fieldnames or [])
        assert "method" in (reader.fieldnames or [])
        assert "target_acc" not in (reader.fieldnames or [])

    with project_report.open(newline="", encoding="utf-8") as handle:
        project_rows = list(csv.DictReader(handle, delimiter="\t"))

    with project_template.open(newline="", encoding="utf-8") as handle:
        project_template_rows = list(csv.DictReader(handle, delimiter="\t"))

    assert [row["accession"] for row in project_rows] == [
        "PRJNA292666",
        "SAMN11953777",
    ]
    assert [row["accession"] for row in project_template_rows] == [
        "PRJNA292666",
        "SAMN11953777",
    ]
    assert project_template_rows[0] == {
        "accession_type": "BioProject",
        "accession": "PRJNA292666",
        "source": "",
        "source_version": "",
        "notes": "",
    }
    assert project_rows[0]["exact_mapped_antibiotics"] == "amikacin"
    assert project_rows[0]["exact_mapped_identifiers"] == "CHEBI:2637"
    assert project_rows[0]["taxon_ids"] == "NCBITaxon:573"

    assert activity_rows[0]["taxon_id"] == "NCBITaxon:573"
    assert activity_rows[0]["strain"] == "KPNIH1"
    assert activity_rows[0]["assembly_accession"] == "GCF_003123125.1"
    assert activity_rows[0]["target_accession"] == "PDT000001234.1"
    assert activity_rows[0]["sra_accessions"] == "ERR111111|SRR222222"
    assert activity_rows[0]["isolation_type"] == "clinical"
    assert activity_rows[0]["location"] == "USA"
    assert activity_rows[0]["collection_date"] == "2020"
    assert activity_rows[0]["create_date"] == "2020-01-31"
    assert activity_rows[0]["host"] == "Homo sapiens"
    assert activity_rows[0]["isolation_source"] == "blood"
    assert activity_rows[0]["method"] == "MIC"
    assert activity_rows[0]["source_version"] == "2026-09-26-ast-browser"
    assert activity_rows[0]["source_retrieved_on"] == "2026-09-26"
    assert activity_rows[0]["isolate_count"] == "1"
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


def test_cli_rejects_ast_without_antibiotic_values_before_opening_reports(tmp_path):
    ast = tmp_path / "ast.tsv"
    ast.write_text("BioSample\tMIC\nSAMN11953777\t2\n", encoding="utf-8")
    antibiotic_report = tmp_path / "ncbi_ast_antibiotics.tsv"
    template = tmp_path / "ncbi_ast_drug_map_template.tsv"
    antibiotic_report.write_text("keep antibiotic report\n", encoding="utf-8")
    template.write_text("keep template\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--ast",
            str(ast),
            "--antibiotic-report",
            str(antibiotic_report),
            "--drug-map-template",
            str(template),
            "--source-version",
            "2026-09-26-ast-browser",
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 1
    assert "NCBI AST table has no rows with antibiotic values" in result.stderr
    assert antibiotic_report.read_text(encoding="utf-8") == "keep antibiotic report\n"
    assert template.read_text(encoding="utf-8") == "keep template\n"


def test_cli_rejects_empty_activity_report_before_opening_sibling_reports(tmp_path):
    ast = tmp_path / "ast.tsv"
    ast.write_text(
        (
            "antibiotic\tbiosample_acc\tbioproject_acc\tTaxID\t"
            "scientific_name\tphenotype\tmic\n"
            "amikacin\tSAMN11953777\tPRJNA292666\t573\t"
            "Klebsiella pneumoniae\tR\t64\n"
        ),
        encoding="utf-8",
    )

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
            "source_version": "2026-09-26-ast-browser",
            "source_record_id": "amikacin",
            "source_name": "amikacin",
            "mapping_status": "EXACT",
            "identifier": "CHEBI:2637",
            "standard_inchi_key": "LKCWBDHBTVXHDL-RMDFUYIESA-N",
            "mapping_basis": "parent_base",
            "notes": "NCBI names the active amikacin parent.",
        })

    antibiotic_report = tmp_path / "ncbi_ast_antibiotics.tsv"
    template = tmp_path / "ncbi_ast_drug_map_template.tsv"
    activity_report = tmp_path / "ncbi_ast_activity.tsv"
    antibiotic_report.write_text("keep antibiotic report\n", encoding="utf-8")
    template.write_text("keep template\n", encoding="utf-8")
    activity_report.write_text("keep activity report\n", encoding="utf-8")

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
            "--source-version",
            "2026-09-26-ast-browser",
            "--source-retrieved-on",
            "2026-09-26",
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 1
    assert "NCBI AST activity report has no rows" in result.stderr
    assert antibiotic_report.read_text(encoding="utf-8") == "keep antibiotic report\n"
    assert template.read_text(encoding="utf-8") == "keep template\n"
    assert activity_report.read_text(encoding="utf-8") == "keep activity report\n"


def test_cli_rejects_activity_report_without_source_metadata(tmp_path):
    ast = tmp_path / "ast.tsv"
    ast.write_text("antibiotic\namikacin\n", encoding="utf-8")
    drug_map = tmp_path / "ncbi_ast_drug_map.tsv"
    drug_map.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + (
            "2026-09-26-ast-browser\tamikacin\tamikacin\t"
            "MISSING_CORPUS_RECORD\t\t\tnone\tmissing\n"
        ),
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--ast",
            str(ast),
            "--drug-map",
            str(drug_map),
            "--activity-report",
            str(tmp_path / "ncbi_ast_activity.tsv"),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 2
    assert "--activity-report requires --source-version" in result.stderr


def test_cli_rejects_drug_map_without_source_version(tmp_path):
    ast = tmp_path / "ast.tsv"
    ast.write_text("antibiotic\namikacin\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--ast",
            str(ast),
            "--drug-map",
            str(tmp_path / "ncbi_ast_drug_map.tsv"),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 2
    assert "--drug-map and --drug-map-template require --source-version" in result.stderr


def test_cli_rejects_drug_map_template_without_source_version(tmp_path):
    ast = tmp_path / "ast.tsv"
    ast.write_text("antibiotic\namikacin\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--ast",
            str(ast),
            "--drug-map-template",
            str(tmp_path / "ncbi_ast_drug_map.tsv"),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 2
    assert "--drug-map and --drug-map-template require --source-version" in result.stderr


def test_cli_rejects_activity_report_with_blank_source_version(tmp_path):
    ast = tmp_path / "ast.tsv"
    ast.write_text("antibiotic\namikacin\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--ast",
            str(ast),
            "--drug-map",
            str(tmp_path / "ncbi_ast_drug_map.tsv"),
            "--activity-report",
            str(tmp_path / "ncbi_ast_activity.tsv"),
            "--source-version",
            " ",
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 2
    assert "--activity-report requires --source-version" in result.stderr


def test_cli_rejects_padded_source_version(tmp_path):
    ast = tmp_path / "ast.tsv"
    ast.write_text("antibiotic\namikacin\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--ast",
            str(ast),
            "--antibiotic-report",
            str(tmp_path / "ncbi_ast_antibiotics.tsv"),
            "--source-version",
            " 2026-09-26-ast-browser ",
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 2
    assert "--source-version must not have leading or trailing whitespace" in result.stderr


@pytest.mark.parametrize("source_version", ["2026\t09", "2026\n09", "2026\r09"])
def test_cli_rejects_source_version_tsv_controls(tmp_path, source_version):
    ast = tmp_path / "ast.tsv"
    ast.write_text("antibiotic\namikacin\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--ast",
            str(ast),
            "--antibiotic-report",
            str(tmp_path / "ncbi_ast_antibiotics.tsv"),
            "--source-version",
            source_version,
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 2
    assert "--source-version must not contain tabs or newlines" in result.stderr


@pytest.mark.parametrize(
    "source_retrieved_on",
    [
        "September 26, 2026",
        "20260926",
    ],
)
def test_cli_rejects_non_iso_activity_report_retrieval_dates(
    tmp_path,
    source_retrieved_on,
):
    ast = tmp_path / "ast.tsv"
    ast.write_text("antibiotic\namikacin\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--ast",
            str(ast),
            "--antibiotic-report",
            str(tmp_path / "ncbi_ast_antibiotics.tsv"),
            "--source-retrieved-on",
            source_retrieved_on,
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 2
    assert "--source-retrieved-on must be an ISO date" in result.stderr
