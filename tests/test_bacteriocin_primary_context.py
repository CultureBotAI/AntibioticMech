"""Bacteriocin names and reference accessions must not hide identity conflicts."""

import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-bacteriocin-primary-context.json").read_bytes())


def test_scope_and_historical_pins(dossier):
    assert dossier["scope"] == {
        "corpus_records": 2939, "record_memberships": 5,
        "whole_records_completed_by_this_review": 0, "full_corpus_primary_review": "OPEN",
    }
    for key in ("prior_checkpoint", "current_census"):
        pin = dossier[key]
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    assert dossier["preservation"]["record_hashes_verified"] == 2939
    assert dossier["preservation"]["biological_record_changes"] == 0
    assert dossier["preservation"]["curation_events_added"] == 0
    assert dossier["preservation"]["ignored_files_included"] is True


@pytest.mark.parametrize("identifier", [
    "CHEBI:71629", "CHEBI:71659", "CHEBI:64624", "CHEBI:82754", "antibioticmech:aro-0a1c492c45",
])
def test_record_identity_and_open_disposition(dossier, identifier):
    row, = [r for r in dossier["records"] if r["identifier"] == identifier]
    record = load_record(ROOT / row["path"])
    assert record["identifier"] == identifier
    assert record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"]
    assert row["whole_record_review"] == "OPEN"
    assert row["record_action"] == "PRESERVE_NO_NEW_BIOLOGICAL_CLAIM"
    assert row["decision"].startswith("HOLD_")
    if identifier == "antibioticmech:aro-0a1c492c45":
        assert row["preserved_source_assertions"] == ["ARO:3003952"]
        assert any(m.get("aro_id") == "ARO:3003952" for m in record["resistance_mechanisms"])


def test_current_chebi_match_does_not_resolve_graph_conflicts(dossier):
    checks = {c["identifier"]: c for c in dossier["chemical_identity_checks"]}
    assert all(c["current_chebi_key_matches_record"] for c in checks.values())
    b17 = checks["CHEBI:64624"]
    assert b17["stored_smiles_parses_strictly"] is False
    assert b17["current_chebi_smiles_parses_strictly"] is False
    assert b17["graph_input"] == "STORED_STANDARD_INCHI"
    assert b17["ring_sizes"] == [5]
    assert b17["aromatic_sulfur_atoms"] == b17["aromatic_oxygen_atoms"] == 0
    assert b17["recomputed_key_matches_record"] is True
    j25 = checks["antibioticmech:aro-0a1c492c45"]
    assert j25["graph_input"] == "STORED_SMILES"
    assert j25["stored_smiles_parses_strictly"] is True
    assert max(j25["ring_sizes"]) == 63
    assert j25["specified_atom_stereo"] == 0
    assert j25["recomputed_key_matches_record"] is True
    assert j25["rdkit_version"] == b17["rdkit_version"] == "2026.03.5"


def test_nisin_primary_scope_does_not_promote_congener_or_mechanism(dossier):
    papers = dossier["primary_papers"]
    for pmid in ("25014359", "25176038"):
        p = papers[pmid]
        assert p["relevant_results_text_inspected"] is True
        assert p["epmc_open_access_flag"] == "Y"
        assert p["donor_label"] == "Lactococcus lactis NZ9700"
        assert p["experimental_background_label"] == "Lactococcus lactis NZ9000"
        assert p["tested_material_label"] == "commercial nisin"
        assert p["exact_congener_to_record_match_verified"] is False
        assert p["endpoint_kind"] == "growth IC50, not MIC or clinical susceptibility category"
        assert p["figures_visually_inspected"] is False
        assert p["supplement_inspected"] is False
        assert p["whole_paper_review_complete"] is False
    assert "proposed explanation" in " ".join(papers["25014359"]["qualitative_findings"])
    assert "separately assessed" in " ".join(papers["25176038"]["qualitative_findings"])


def test_reference_versions_and_scope(dossier):
    expected = {"P42708": 73, "Q54002": 112, "Q54003": 51, "Q54004": 38,
                "Q47510": 122, "Q47511": 91, "Q2KKH5": 73, "B0EYN8": 79,
                "Q83Y55": 86, "Q2KKH9": 69}
    assert set(dossier["proteins"]) == set(expected)
    for accession, version in expected.items():
        p = dossier["proteins"][accession]
        assert p["entry_audit"] == {"entryVersion": version, "sequenceVersion": 1}
        assert p["accession"] == "UniProtKB:" + accession
        assert p["experimental_assignment"] is False
        assert p["scope"] == "REFERENCE_METADATA_NOT_EXACT_EXPERIMENTAL_ALLELE_OR_TESTED_ORGANISM"


def test_epifeg_components_and_native_donor_are_not_tested_host(dossier):
    for accession, gene in (("Q54002", "epiF"), ("Q54003", "epiE"), ("Q54004", "epiG")):
        p = dossier["proteins"][accession]
        assert p["gene_symbols"] == [gene]
        assert p["organism"]["taxonId"] == 1282
        citation, = p["citation_contexts"]
        assert citation["identifiers"] == [{"database": "PubMed", "id": "8550476"}]
        assert [c["value"] for c in citation["context"] if c["type"] == "STRAIN"] == ["Tue3298"]
    papers = dossier["primary_papers"]
    assert "S. carnosus" in " ".join(papers["8550476"]["qualitative_findings"])
    assert "gallidermin" in " ".join(papers["11229936"]["qualitative_findings"])
    assert papers["8550476"]["review_medium"] == "PRIMARY_ABSTRACT"


def test_microcin_c_candidates_and_substrate_forms_remain_distinct(dossier):
    proteins = dossier["proteins"]
    assert {a for a, p in proteins.items() if p["organism"]["taxonId"] == 562} == {
        "Q47510", "Q47511", "Q2KKH5", "B0EYN8", "Q83Y55", "Q2KKH9",
    }
    assert {r["id"] for r in proteins["Q2KKH9"]["archive_references"]} == {"AY913945", "EF536825"}
    assert {r["id"] for r in proteins["Q83Y55"]["archive_references"]} == {"AJ487788"}
    assert "processed microcin C" in " ".join(dossier["primary_papers"]["20159968"]["qualitative_findings"])


def test_taxonomic_ranks_and_background_are_not_derivative_assignments(dossier):
    assert {k: v["rank"] for k, v in dossier["reference_taxonomy"].items()} == {
        "1282": "species", "1360": "subspecies", "562": "species",
    }
    background = dossier["background_taxonomy"]
    assert background["reference_taxon_id"] == "NCBITaxon:746361"
    assert background["scope"] == "NAMED_BACKGROUND_ONLY_NOT_EXPERIMENTAL_DERIVATIVE_OR_DONOR"
    assert {r["taxonId"] for r in background["candidates"]} == {746361, 416870}
    assert {r["parent"]["taxonId"] for r in background["candidates"]} == {2816960}
    nisi = dossier["proteins"]["P42708"]
    assert {c["value"] for r in nisi["citation_contexts"] for c in r["context"]
            if c["type"] == "STRAIN"} == {"NIZO R5", "6F3"}


def test_complete_queries_are_not_biological_absence_or_full_review(dossier):
    assert sorted(r["result_count"] for r in dossier["uniprot_requests"]) == [1, 3, 6]
    assert sorted(r["hit_count"] for r in dossier["bibliographic_requests"]) == [9, 47, 64]
    for request in dossier["uniprot_requests"] + dossier["bibliographic_requests"]:
        assert request["complete_for_query"] is True
        assert request["establishes_biological_absence"] is False
        assert urlsplit(request["url"]).hostname in {"rest.uniprot.org", "www.ebi.ac.uk"}
        assert len(request["sha256"]) == len(request["cache"]["sha256"]) == 64
    scope = dossier["discovery_scope"]
    assert "nickel-silicide" in scope["refinement_note"]
    assert "611" in scope["expanded_corpus_traversals"]
    assert "not complete" in scope["initial_nisin_cap"]
    assert len(dossier["primary_papers"]) == 10


def test_export_excludes_experimental_design_and_unearned_validation(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {
        "sequence", "features", "variants", "alteration", "protocol", "primers", "coordinates",
        "mic", "measurement_value", "activity_spectrum", "resistance_mechanisms", "headers", "body",
    }
    assert all(not p["whole_paper_review_complete"] for p in dossier["primary_papers"].values())
    assert "No NCBI request" in " ".join(dossier["limitations"])
    assert "not rerun" in " ".join(dossier["limitations"])
