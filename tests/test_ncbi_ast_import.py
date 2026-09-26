"""Unit tests for seeding curated NCBI AST activity reports."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import seed_from_sources  # noqa: E402
from evaluate_ncbi_ast import ACTIVITY_REPORT_COLUMNS  # noqa: E402
from seed_from_sources import (  # noqa: E402
    NCBI_AST_ACTIVITY_SOURCE,
    attach_ncbi_ast_activity,
    merge_with_existing,
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
        "activity_group_id": "ncbi_ast:7fe9356073d90a3d",
        "source_version": "2026-09-26-ast-browser",
        "source_retrieved_on": "2026-09-26",
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
        "platform": "AST",
        "vendor": "NCBI",
        "reagent": "broth microdilution",
        "standard": "CLSI",
    })
    row.update(overrides)
    return row


def test_attach_ncbi_ast_activity_writes_source_observations(tmp_path, monkeypatch):
    path = tmp_path / "ncbi_ast_activity.tsv"
    write_activity_report(
        path,
        [
            ncbi_ast_row(
                disk_diffusion_value="18",
                disk_diffusion_qualifier=">=",
                disk_diffusion_units="mm",
            ),
        ],
    )
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
    assert observation["taxon_label"] == "Escherichia coli and Shigella"
    assert observation["activity"] == "RESISTANT"
    assert observation["mic_value"] == 2.0
    assert observation["mic_qualifier"] == "<="
    assert observation["mic_units"] == "mg/L"
    assert observation["disk_diffusion_value"] == 18.0
    assert observation["disk_diffusion_qualifier"] == ">="
    assert observation["disk_diffusion_units"] == "mm"
    assert observation["measurement_count"] == 2
    assert observation["biosample_accession"] == "SAMN11953777"
    assert observation["bioproject_accession"] == "PRJNA292666"
    assert observation["assembly_accession"] == "GCF_003123125.1"
    assert observation["source"] == NCBI_AST_ACTIVITY_SOURCE
    assert observation["source_version"] == "2026-09-26-ast-browser"
    assert observation["source_retrieved_on"] == "2026-09-26"
    assert observation["source_observation_id"] == "ncbi_ast:7fe9356073d90a3d"
    assert "platform AST" in observation["assay"]
    assert "standard CLSI" in observation["assay"]
    assert "BioSample, BioProject and assembly context" in observation["evidence"][0]["notes"]


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
