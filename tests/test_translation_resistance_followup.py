"""Biochemical results and reference identifiers must retain their actual scope."""

import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-translation-reference-followup.json").read_bytes())


def test_prior_checkpoint_is_preserved_and_corpus_scope_stays_open(dossier):
    for name in ("prior_checkpoint", "prior_verification", "current_census", "citation_union"):
        pin = dossier[name]
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    assert dossier["scope"] == {
        "corpus_records": 2939, "record_memberships": 4,
        "whole_records_completed_by_this_review": 0, "full_corpus_primary_review": "OPEN",
    }
    assert dossier["preservation"] == {
        "record_hashes_verified": 2939, "ignored_files_included": True,
        "biological_record_changes": 0, "curation_events_added": 0,
    }


@pytest.mark.parametrize(
    "identifier", ["antibioticmech:aro-8b2f0e38fa", "CHEBI:29584", "CHEBI:29668", "CHEBI:29693"]
)
def test_record_identity_and_held_scope(dossier, identifier):
    row, = [r for r in dossier["records"] if r["identifier"] == identifier]
    doc = load_record(ROOT / row["path"])
    assert doc["identifier"] == identifier
    assert doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"]
    assert row["complete_record_read_through_collection_loader"]
    assert row["whole_record_review"] == "OPEN" and row["decision"].startswith("HOLD_")
    assert row["record_action"] == "PRESERVE_NO_NEW_BIOLOGICAL_CLAIM"


def test_kirromycin_named_reference_is_not_an_exact_chemical_match(dossier):
    row, = [r for r in dossier["records"] if r["label"] == "kirromycin"]
    assert row["standard_inchi_key"] == "HMSYAPGFKGSXAJ-GFNGQHCCSA-N"
    reference = row["current_chebi_reference"]
    assert reference["identifier"] == "CHEBI:190786" and reference["label"] == "Mocimycin"
    assert reference["standard_inchi_key"] == "HMSYAPGFKGSXAJ-PAHGNTJYSA-N"
    assert reference["connectivity_block_matches"] and not reference["full_key_matches"]
    assert reference["inchi_layers_equal"] == {
        "complete": False, "double_bond_stereochemistry": False, "tetrahedral_stereochemistry": True,
    }
    assert row["diagnostics"]["inchi_recomputed_key"] == row["standard_inchi_key"]
    assert reference["diagnostics"]["inchi_recomputed_key"] == reference["standard_inchi_key"]
    assert not reference["diagnostics"]["smiles_parses_strictly"]
    memberships = dossier["chemical_diagnostics"]["named_reference_key_membership"]
    assert memberships[reference["standard_inchi_key"]] == []
    assert dossier["chemical_diagnostics"]["ignored_records_included"]
    assert "not proof" in dossier["chemical_diagnostics"]["interpretation"]


def test_unspecified_stereochemistry_does_not_identify_tested_material(dossier):
    expected = {"GE2270A": (6, 6), "pulvomycin": (13, 8), "thiostrepton": (17, 0)}
    for row in dossier["records"]:
        if row["label"] in expected:
            diagnostics = row["diagnostics"]
            actual = (diagnostics["tetrahedral_centers"], diagnostics["unassigned_tetrahedral_centers"])
            assert actual == expected[row["label"]]
    assert dossier["chemical_diagnostics"]["rdkit_version"] == "2026.03.5"


def test_biochemical_response_does_not_prove_native_self_protection(dossier):
    paper = dossier["primary_papers"]["17337575"]
    assert paper["relevant_results_text_inspected"]
    assert not paper["native_producer_self_protection_established"]
    assert not paper["coelicolor_pulvomycin_resistance_established"]
    assert not paper["exact_experimental_protein_assignment"]
    assert paper["subject_context"]["M145_is_not_the_tested_derivative"]
    assert paper["subject_context"]["thiostrepton_used_as_selection_marker_not_focal_resistance_outcome"]
    assert "crude material" in " ".join(paper["qualitative_findings"])
    assert "sensitive EF-Tu1" in " ".join(paper["qualitative_findings"])


def test_reference_protein_versions_and_aliases_are_not_experimental_alleles(dossier):
    expected = {"P29544": (110, 1, 1925), "P40175": (156, 2, 100226), "P18644": (105, 1, 146537)}
    assert set(dossier["proteins"]) == set(expected)
    for accession, (entry_version, sequence_version, taxon) in expected.items():
        reference = dossier["proteins"][accession]
        assert reference["entry_audit"] == {
            "entryVersion": entry_version, "sequenceVersion": sequence_version,
        }
        assert reference["organism"]["taxonId"] == taxon and not reference["experimental_assignment"]
        assert reference["scope"] == "REFERENCE_IDENTITY_NOT_EXPERIMENTAL_ALLELE"
    gene, = dossier["proteins"]["P18644"]["gene_annotations"]
    assert gene["geneName"]["value"] == "tsnR"
    assert {g["value"] for g in gene["synonyms"]} == {"tsr"}


def test_strain_reference_does_not_replace_lab_derivative(dossier):
    reference = dossier["reference_taxonomy"]["100226"]
    assert reference["rank"] == "strain" and reference["parent"]["taxonId"] == 1902
    assert not reference["experimental_assignment"]
    assert dossier["archive_references"]["X77040"]["reference"]["taxon"] == 1902
    assert dossier["reference_taxonomy"]["1925"]["rank"] == "species"
    assert dossier["archive_references"]["X67059"]["reference"]["taxon"] == 1925
    for reference in dossier["archive_references"].values():
        assert reference["scope"] == "REFERENCE_GENE_DEPOSIT_NOT_GENOME_ASSEMBLY"
        assert not reference["experimental_genome_assignment"]


def test_ena_uniprot_taxon_disagreement_remains_explicit(dossier):
    conflict, = dossier["reference_disagreements"]
    assert conflict["protein_accession"] == "UniProtKB:P18644"
    assert conflict["archive_accession"] == "X02392.1"
    assert conflict["uniprot_taxon_id"] == "NCBITaxon:146537"
    assert conflict["ena_taxon_id"] == "NCBITaxon:1904"
    assert dossier["reference_taxonomy"]["1904"]["scientificName"] == "Streptomyces cyaneus"
    assert dossier["reference_taxonomy"]["146537"]["scientificName"] == "Streptomyces azureus"
    assert "UNRESOLVED_REFERENCE_TAXON_DISAGREEMENT" in conflict["disposition"]


def test_access_failure_and_incomplete_review_are_not_negative_evidence(dossier):
    assert sorted(r["status"] for r in dossier["access_constraints"]) == [403, 500, 500]
    assert all("NOT_A_BIOLOGICAL_NEGATIVE_RESULT" in r["disposition"] for r in dossier["access_constraints"])
    papers = dossier["primary_papers"]
    assert not papers["6806287"]["relevant_results_text_inspected"]
    assert not papers["25086036"]["relevant_results_text_inspected"]
    assert papers["25086036"]["review_medium"] == "BIBLIOGRAPHY_AND_ABSTRACT_ONLY"
    assert all(
        not p["whole_paper_review_complete"] and not p["native_figures_visually_inspected"]
        for p in papers.values()
    )


def test_known_reference_leads_do_not_rewrite_historical_searches(dossier):
    leads = dossier["supplemental_reference_leads"]
    assert leads["identifier"] == "CHEBI:29693"
    assert leads["references"] == ["PMID:25086036", "PMID:6806287"]
    assert not leads["present_in_prior_citation_union"] and not leads["biological_assignment"]
    assert "NOT_CORPUS_RECALL_ESTIMATE" in leads["scope"]


def test_export_is_non_operational_and_network_scope_is_explicit(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    prohibited = {"sequence", "variants", "alteration", "constructs", "primers", "protocol",
                  "coordinates", "mic", "measurement_value", "headers", "smiles", "inChI"}
    assert not set(keys(dossier)) & prohibited
    assert "Full authoritative QC not rerun" in dossier["validation_scope"]
    assert all(dossier[k] == 0 for k in ("ncbi_endpoint_requests", "github_mutations", "source_adoptions",
                                        "numerical_ast_added", "experimental_genome_assignments",
                                        "exact_experimental_protein_assignments", "outreach"))
    for request in dossier["uniprot_requests"]:
        assert urlsplit(request["url"]).hostname == "rest.uniprot.org"
        assert request["complete_for_query"] and not request["establishes_biological_absence"]
        assert request["release"] == "2026_03"
