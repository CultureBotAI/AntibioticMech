"""Unit tests for seeding curated NCBI AST activity reports."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import seed_from_sources  # noqa: E402
from evaluate_ncbi_ast import (  # noqa: E402
    ACTIVITY_GROUP_ID_VERSION,
    ACTIVITY_REPORT_COLUMNS,
    ACTIVITY_REPORT_GROUP_COLUMNS,
    activity_group_id,
)
from seed_from_sources import (  # noqa: E402
    NCBI_AST_ACTIVITY_COLUMNS,
    NCBI_AST_ACTIVITY_GROUP_COLUMNS,
    NCBI_AST_ACTIVITY_GROUP_ID_VERSION,
    NCBI_AST_ACTIVITY_SOURCE,
    attach_ncbi_ast_activity,
    load_ncbi_ast_activity_inventory,
    merge_with_existing,
    ncbi_ast_activity_group_id,
    ncbi_ast_sourced_activity_view,
)


def write_activity_report(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=ACTIVITY_REPORT_COLUMNS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def ncbi_ast_row(**overrides: str) -> dict[str, str]:
    row = {column: "" for column in ACTIVITY_REPORT_COLUMNS}
    row.update({
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
        "biosample_accession": "SAMN11953777",
        "bioproject_accession": "PRJNA292666",
        "target_accession": "PDT000001234.1",
        "assembly_accession": "GCF_003123125.1",
        "phenotype": "R",
        "activity": "RESISTANT",
        "mic_value": "2",
        "mic_qualifier": "<=",
        "mic_units": "mg/L",
        "platform": "AST",
        "vendor": "NCBI",
        "reagent": "broth microdilution",
        "standard": "CLSI",
    })
    row.update(overrides)
    if "activity_group_id" not in overrides:
        row["activity_group_id"] = activity_group_id(row)
    return row


def test_ncbi_ast_activity_columns_match_the_evaluator_contract():
    row = ncbi_ast_row()

    assert NCBI_AST_ACTIVITY_COLUMNS == ACTIVITY_REPORT_COLUMNS
    assert NCBI_AST_ACTIVITY_GROUP_ID_VERSION == ACTIVITY_GROUP_ID_VERSION
    assert ACTIVITY_GROUP_ID_VERSION == "ncbi_ast_activity_group_v4"
    assert NCBI_AST_ACTIVITY_GROUP_COLUMNS == ACTIVITY_REPORT_GROUP_COLUMNS
    assert ncbi_ast_activity_group_id(row) == activity_group_id(row)


def test_load_ncbi_ast_activity_inventory_accepts_disk_only_rows(tmp_path):
    path = tmp_path / "ncbi_ast_activity.tsv"
    row = ncbi_ast_row(
        mic_value="",
        mic_qualifier="",
        mic_units="",
        disk_diffusion_value="18",
        disk_diffusion_qualifier=">=",
        disk_diffusion_units="mm",
    )
    write_activity_report(path, [row])

    assert load_ncbi_ast_activity_inventory(path) == [row]


@pytest.mark.parametrize(
    ("biosample_accession", "bioproject_accession"),
    [
        ("SAMD11953777", "PRJDB292666"),
        ("SAMEA11953777", "PRJEB292666"),
    ],
)
def test_load_ncbi_ast_activity_inventory_accepts_insdc_project_context(
    tmp_path,
    biosample_accession,
    bioproject_accession,
):
    path = tmp_path / "ncbi_ast_activity.tsv"
    row = ncbi_ast_row(
        biosample_accession=biosample_accession,
        bioproject_accession=bioproject_accession,
    )
    write_activity_report(path, [row])

    assert load_ncbi_ast_activity_inventory(path) == [row]


def test_load_ncbi_ast_activity_inventory_accepts_versionless_gca_assembly(tmp_path):
    path = tmp_path / "ncbi_ast_activity.tsv"
    row = ncbi_ast_row(assembly_accession="GCA_003123125")
    write_activity_report(path, [row])

    assert load_ncbi_ast_activity_inventory(path) == [row]


def test_load_ncbi_ast_activity_inventory_rejects_header_drift(tmp_path):
    path = tmp_path / "ncbi_ast_activity.tsv"
    path.write_text("activity_group_id\tunexpected\n", encoding="utf-8")

    with pytest.raises(ValueError, match="expected NCBI AST activity header"):
        load_ncbi_ast_activity_inventory(path)


def test_load_ncbi_ast_activity_inventory_rejects_short_rows(tmp_path):
    path = tmp_path / "ncbi_ast_activity.tsv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(ACTIVITY_REPORT_COLUMNS)
        writer.writerow(["ncbi_ast:short"])

    with pytest.raises(ValueError, match="source_version is missing"):
        load_ncbi_ast_activity_inventory(path)


def test_load_ncbi_ast_activity_inventory_rejects_duplicate_groups(tmp_path):
    path = tmp_path / "ncbi_ast_activity.tsv"
    write_activity_report(path, [ncbi_ast_row(), ncbi_ast_row()])

    with pytest.raises(ValueError, match="duplicate activity_group_id"):
        load_ncbi_ast_activity_inventory(path)


def test_load_ncbi_ast_activity_inventory_rejects_mixed_source_metadata(tmp_path):
    path = tmp_path / "ncbi_ast_activity.tsv"
    write_activity_report(path, [
        ncbi_ast_row(),
        ncbi_ast_row(
            biosample_accession="SAMN11953778",
            source_version="2026-09-27-ast-browser",
        ),
    ])

    with pytest.raises(ValueError, match="source_version must be"):
        load_ncbi_ast_activity_inventory(path)

    write_activity_report(path, [
        ncbi_ast_row(),
        ncbi_ast_row(
            biosample_accession="SAMN11953778",
            source_retrieved_on="2026-09-27",
        ),
    ])

    with pytest.raises(ValueError, match="source_retrieved_on must be '2026-09-26'"):
        load_ncbi_ast_activity_inventory(path)


@pytest.mark.parametrize(
    ("overrides", "message"),
    [
        ({"source_retrieved_on": "20260926"}, "source_retrieved_on must be an ISO date"),
        ({"source_version": " "}, "source_version is required"),
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
        ({"platform": " AST"}, "platform has leading or trailing whitespace"),
        ({"platform": "", "reagent": ""}, "platform or reagent is required"),
        ({"platform": "AST\nCLSI"}, "platform contains a tab or newline"),
        ({"biosample_accession": "BioSample:SAMN11953777"}, "invalid BioSample accession"),
        ({"bioproject_accession": "SAMN11953777"}, "invalid BioProject accession"),
        ({"taxon_id": "562"}, "invalid NCBI Taxonomy CURIE"),
        ({"taxon_id": "NCBITaxon:0"}, "invalid NCBI Taxonomy CURIE"),
        ({"taxon_id": "NCBITaxon:000562"}, "invalid NCBI Taxonomy CURIE"),
        ({"target_accession": "GCF_003123125.1"}, "invalid Pathogen Detection target"),
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
        ({"normalized_antibiotic": "stale"}, "normalized_antibiotic must match source_name"),
        ({"phenotype": "non-susceptible", "activity": ""}, "unsupported phenotype"),
        ({"activity": "NON_SUSCEPTIBLE"}, "activity must match phenotype"),
        ({"phenotype": "S", "activity": "RESISTANT"}, "activity must match phenotype"),
        ({"activity_group_id": "ncbi_ast:stale"}, "activity_group_id must be"),
        ({"mic_value": "high"}, "mic_value must be numeric"),
        ({"mic_value": "2.0"}, "mic_value must use canonical decimal '2'"),
        ({"mic_value": "0"}, "mic_value must be positive"),
        ({"mic_value": "1024.1"}, "mic_value must be at most 1024"),
        ({"mic_qualifier": "MIC90"}, "mic_qualifier has invalid qualifier"),
        ({"mic_value": ""}, "mic_qualifier requires mic_value"),
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
    ],
)
def test_load_ncbi_ast_activity_inventory_rejects_malformed_rows(
    tmp_path,
    overrides,
    message,
):
    path = tmp_path / "ncbi_ast_activity.tsv"
    write_activity_report(path, [ncbi_ast_row(**overrides)])

    with pytest.raises(ValueError, match=message):
        load_ncbi_ast_activity_inventory(path)


def test_attach_ncbi_ast_activity_writes_source_observations(tmp_path, monkeypatch):
    path = tmp_path / "ncbi_ast_activity.tsv"
    row = ncbi_ast_row(
        disk_diffusion_value="18",
        disk_diffusion_qualifier=">=",
        disk_diffusion_units="mm",
        sra_accessions="ERR111111|SRR222222",
    )
    write_activity_report(path, [row])
    monkeypatch.setattr(seed_from_sources, "NCBI_AST_ACTIVITY_INVENTORY", path)
    records = {
        "CHEBI:478164": {
            "identifier": "CHEBI:478164",
            "chemical_structure": {"standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
            "curation_history": [],
        },
    }

    counts = attach_ncbi_ast_activity(records)
    observation = records["CHEBI:478164"]["activity_spectrum"][0]

    assert counts["matched_observations"] == 1
    assert counts["matched_records"] == 1
    assert observation["taxon_id"] == "NCBITaxon:562"
    assert observation["taxon_label"] == "Escherichia coli and Shigella"
    assert observation["activity"] == "RESISTANT"
    assert observation["mic_value"] == 2.0
    assert observation["mic_qualifier"] == "<="
    assert observation["mic_units"] == "mg/L"
    assert observation["disk_diffusion_value"] == 18.0
    assert observation["disk_diffusion_qualifier"] == ">="
    assert observation["disk_diffusion_units"] == "mm"
    assert observation["measurement_count"] == 2
    assert observation["isolate_count"] == 1
    assert observation["biosample_accession"] == "SAMN11953777"
    assert observation["bioproject_accession"] == "PRJNA292666"
    assert observation["pathogen_detection_target_accession"] == "PDT000001234.1"
    assert observation["assembly_accession"] == "GCF_003123125.1"
    assert observation["sra_accessions"] == ["ERR111111", "SRR222222"]
    assert observation["source"] == NCBI_AST_ACTIVITY_SOURCE
    assert observation["source_version"] == "2026-09-26-ast-browser"
    assert observation["source_retrieved_on"] == "2026-09-26"
    assert observation["source_observation_id"] == row["activity_group_id"]
    assert "platform AST" in observation["assay"]
    assert "isolate_count=1" in observation["evidence"][0]["notes"]
    assert "standard CLSI" in observation["assay"]
    assert "target_accession=PDT000001234.1" in observation["evidence"][0]["notes"]
    assert "sra_accessions=ERR111111|SRR222222" in observation["evidence"][0]["notes"]
    assert "BioSample, BioProject, target, assembly and SRA context" in observation["evidence"][0]["notes"]


def test_attach_ncbi_ast_activity_rejects_identity_drift(tmp_path, monkeypatch):
    path = tmp_path / "ncbi_ast_activity.tsv"
    write_activity_report(path, [ncbi_ast_row(standard_inchi_key="STALE")])
    monkeypatch.setattr(seed_from_sources, "NCBI_AST_ACTIVITY_INVENTORY", path)
    records = {
        "CHEBI:478164": {
            "identifier": "CHEBI:478164",
            "chemical_structure": {"standard_inchi_key": "HVFLCNVBZFFHBT-ZKDACBOMSA-N"},
            "curation_history": [],
        },
    }

    counts = attach_ncbi_ast_activity(records)

    assert counts["identity_drift"] == 1
    assert "activity_spectrum" not in records["CHEBI:478164"]


def test_reseed_replaces_only_the_ncbi_ast_activity_slice():
    new_ncbi_ast = {
        "taxon_label": "Escherichia coli and Shigella",
        "activity": "RESISTANT",
        "mic_value": 2.0,
        "mic_units": "mg/L",
        "assay": "NCBI Pathogen Detection AST",
        "source": NCBI_AST_ACTIVITY_SOURCE,
        "source_version": "2026-09-26-ast-browser",
        "source_observation_id": "ncbi_ast:new",
        "evidence": [{"reference": "https://www.ncbi.nlm.nih.gov/pathogens/docs/ast/"}],
    }
    old_ncbi_ast = new_ncbi_ast | {"source_observation_id": "ncbi_ast:stale"}
    curated = {
        "taxon_label": "Escherichia coli",
        "activity": "SUSCEPTIBLE",
        "assay": "curated broth microdilution",
        "source": "CURATOR",
        "evidence": [{"reference": "PMID:1"}],
    }
    base = {
        "identifier": "CHEBI:1",
        "label": "example",
        "antimicrobial_class": "ANTIBACTERIAL",
        "curation_status": "SEEDED",
        "grounding_status": "EXACT",
        "curation_history": [],
    }

    fresh = base | {"activity_spectrum": [new_ncbi_ast]}
    existing = base | {"activity_spectrum": [old_ncbi_ast, curated]}
    merged = merge_with_existing(fresh, existing)

    assert ncbi_ast_sourced_activity_view(merged) == [new_ncbi_ast]
    assert merged["activity_spectrum"] == [new_ncbi_ast, curated]


def test_reseed_drops_stale_ncbi_ast_activity_when_the_source_stops_emitting_it():
    old_ncbi_ast = {
        "taxon_label": "Escherichia coli and Shigella",
        "activity": "RESISTANT",
        "assay": "NCBI Pathogen Detection AST",
        "source": NCBI_AST_ACTIVITY_SOURCE,
        "source_version": "2026-09-26-ast-browser",
        "source_observation_id": "ncbi_ast:stale",
        "evidence": [{"reference": "https://www.ncbi.nlm.nih.gov/pathogens/docs/ast/"}],
    }
    base = {
        "identifier": "CHEBI:1",
        "label": "example",
        "antimicrobial_class": "ANTIBACTERIAL",
        "curation_status": "SEEDED",
        "grounding_status": "EXACT",
        "curation_history": [],
    }

    merged = merge_with_existing(base, base | {"activity_spectrum": [old_ncbi_ast]})

    assert "activity_spectrum" not in merged
