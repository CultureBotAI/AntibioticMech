"""Structural identity and primary scope must not imply a whole-cell allele join."""

import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-producer-primary-context.json").read_bytes())


@pytest.mark.parametrize("pdb_id,version", [("4IAG", (1, 5)), ("5CJ3", (1, 4))])
def test_explicit_structure_reference_links(dossier, pdb_id, version):
    identity = dossier["structural_identity"]
    entry = identity["pdb_entries"][pdb_id]
    revision = entry["rcsb_accession_info"]
    assert (revision["major_revision"], revision["minor_revision"]) == version
    assert entry["rcsb_primary_citation"]["pdbx_database_id_PubMed"] == 26512730
    assert entry["rcsb_primary_citation"]["pdbx_database_id_DOI"] == "10.1021/acs.biochem.5b01008"
    entity, = entry["polymer_entities"]
    assert entity["rcsb_id"] == pdb_id + "_1"
    assert entity["rcsb_polymer_entity_container_identifiers"]["reference_sequence_identifiers"] == [
        {"database_accession": "B9UIZ4", "database_name": "UniProt"},
    ]
    assert entity["rcsb_entity_source_organism"] == [
        {"ncbi_taxonomy_id": 28893, "scientific_name": "Streptomyces flavoviridis"},
    ]
    assert identity["current_uniprot_name"] == "Streptomyces pilosus"
    assert identity["scope"] == "STRUCTURAL_ENTITY_REFERENCE_NOT_WHOLE_CELL_RESISTANCE_OR_EXACT_ALLELE"


def test_component_identity_is_not_metal_complex_identity(dossier):
    identity = dossier["structural_identity"]
    record = load_record(ROOT / "data/antibiotics/unspecified/zorbamycin.yaml")
    assert identity["identifier"] == record["identifier"] == "CHEBI:67811"
    assert identity["component_id"] == "52G"
    assert identity["component_inchi_key"] == record["chemical_structure"]["standard_inchi_key"]
    ligands = {k: {r["pdbx_entity_nonpoly"]["comp_id"] for r in v["nonpolymer_entities"]}
               for k, v in identity["pdb_entries"].items()}
    assert ligands == {"4IAG": {"GOL", "EDO"}, "5CJ3": {"52G", "CU", "CL"}}
    assert "metal-complex assay" in dossier["limitations"][0]


def test_primary_review_keeps_forms_and_backgrounds_separate(dossier):
    primary = dossier["primary_context"]
    assert primary["reference"] == "PMID:25299801"
    assert primary["medium"] == "PUBLISHER_INDEXED_PRIMARY_RESULTS_TEXT"
    assert primary["relevant_results_text_inspected"] is True
    assert primary["figures_visually_inspected"] is False
    assert primary["supplement_inspected"] is False
    assert primary["native_primary_file_cached"] is False
    findings = " ".join(primary["qualitative_findings"])
    assert "metal-free" in findings and "copper-bound" in findings
    assert "not the ancestral ATCC21892" in findings
    assert "does not isolate the contribution of zbmA alone" in findings
    assert "ATCC31154" in primary["donor_label_caveat"]
    assert "ATCC31158" in primary["donor_labels"]["TlmB"]
    assert "non-commercial" in primary["reuse"]


@pytest.mark.parametrize("identifier", ["CHEBI:67811", "CHEBI:75046", "antibioticmech:aro-e05426a76f"])
def test_record_memberships_preserve_exact_identity(dossier, identifier):
    member, = [r for r in dossier["records"] if r["identifier"] == identifier]
    current = load_record(ROOT / member["path"])
    assert current["identifier"] == identifier
    assert current["chemical_structure"]["standard_inchi_key"] == member["standard_inchi_key"]
    assert len(member["sha256"]) == 64


def test_symbol_collision_and_reference_leads_are_not_assignments(dossier):
    candidates = {r["accession"]: r for r in dossier["reference_candidates"]}
    assert len(candidates) == 4
    assert not any(r["experimental_assignment"] for r in candidates.values())
    rejected = candidates["UniProtKB:A0A0P0FBH4"]
    assert rejected["gene_symbols"] == ["tlmB"]
    assert rejected["organism"]["scientificName"] == "Salinispora pacifica DSM 45543 = CNS-863"
    assert rejected["citation_ids"] == ["26458099"]
    assert rejected["decision"] == "REJECTED_FOCAL_MAPPING_DIFFERENT_DONOR_AND_CITATION"
    older = candidates["UniProtKB:Q53796"]
    assert older["gene_symbols"] == [] and older["reference_strain_labels"] == ["ATCC 15003"]
    assert older["citation_ids"] == ["19889644", "7530225"]
    assert "25299801" not in {c for r in candidates.values() for c in r["citation_ids"]}
    assert candidates["UniProtKB:A4KUD4"]["reference_strain_labels"] == ["DSM 44523"]
    assert candidates["UniProtKB:A0A5N5VYK2"]["organism"]["taxonId"] == 35621


@pytest.mark.parametrize("query,count", [
    ("gene_exact:blmB", 1), ("gene_exact:tlmB", 1), ("lit_pubmed:25299801", 0),
    ("tallysomycin AND acetyltransferase", 7), ("bleomycin AND acetyltransferase", 382),
])
def test_complete_searches_do_not_prove_primary_coverage(dossier, query, count):
    receipt, = [r for r in dossier["uniprot_requests"] if r.get("query") == query]
    assert receipt["result_count"] == count and receipt["complete_for_query"] is True
    assert receipt["establishes_biological_absence"] is False
    assert receipt["release"] == "2026_03"
    assert urlsplit(receipt["url"]).hostname == "rest.uniprot.org"
    assert len(receipt["sha256"]) == len(receipt["cache"]["sha256"]) == 64


def test_reference_taxonomy_and_failed_access_are_scoped(dossier):
    assert {k: (r["scientificName"], r["rank"]) for k, r in dossier["taxonomy"].items()} == {
        "2017": ("Streptoalloteichus hindustanus", "species"),
        "29309": ("Streptomyces verticillus", "species"),
    }
    assert len(dossier["uniprot_requests"]) == 7
    assert [r["status"] for r in dossier["retrieval_attempts"]] == [202, 301, 404]
    assert all(not r["pdf_obtained"] for r in dossier["retrieval_attempts"])
    assert dossier["tallysomycin_lookup"]["scope"] == (
        "ALL_DATA_ANTIBIOTICS_YAML_TEXT_NOT_EXHAUSTIVE_CHEMICAL_SYNONYMY"
    )
    assert dossier["tallysomycin_lookup"]["ignored_files_included"] is True


def test_historical_checkpoint_and_corpus_scope_are_preserved(dossier):
    prior = dossier["prior_checkpoint"]
    assert hashlib.sha256((ROOT / prior["path"]).read_bytes()).hexdigest() == prior["sha256"]
    assert dossier["scope"] == {
        "corpus_records": 2939, "record_memberships": 3,
        "whole_records_completed_by_this_review": 0, "full_corpus_primary_review": "OPEN",
    }
    assert dossier["preservation"]["record_hashes_verified"] == 2939
    assert dossier["preservation"]["ignored_files_included"] is True
    assert dossier["preservation"]["biological_record_changes"] == 0
    assert dossier["preservation"]["curation_events_added"] == 0


def test_public_export_excludes_experimental_specifications(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {
        "sequence", "features", "variants", "alteration", "resistance_mechanisms",
        "activity_spectrum", "mic", "measurement_value", "protocol", "primers", "coordinates",
    }
    assert "No NCBI request" in " ".join(dossier["limitations"])
