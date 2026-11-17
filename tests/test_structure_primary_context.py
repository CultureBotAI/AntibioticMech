"""Structural references and name changes must not become experimental assignments."""

import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-structure-primary-context.json").read_bytes())


def test_full_scope_and_pinned_historical_inputs(dossier):
    assert dossier["scope"] == {
        "corpus_records": 2939, "record_memberships": 16,
        "source_assertions_reviewed_for_identity": 19, "reference_paths": 5,
        "whole_records_completed_by_this_review": 0, "full_corpus_primary_review": "OPEN",
    }
    for source in dossier["inputs"].values():
        assert hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest() == source["sha256"]
    assert dossier["preservation"]["record_hashes_verified"] == 2939
    assert dossier["preservation"]["ignored_files_included"] is True
    assert dossier["preservation"]["biological_record_changes"] == 0
    assert dossier["preservation"]["curation_events_added"] == 0


def test_all_selected_record_assertions_have_scoped_dispositions(dossier):
    counts = Counter()
    assert len({r["identifier"] for r in dossier["records"]}) == 16
    for member in dossier["records"]:
        record = load_record(ROOT / member["path"])
        assert record["identifier"] == member["identifier"]
        assert record["chemical_structure"]["standard_inchi_key"] == member["standard_inchi_key"]
        assert {r["aro_id"] for r in member["assertion_reviews"]} == set(member["aro_ids"])
        assert member["whole_record_review"] == "OPEN"
        for review in member["assertion_reviews"]:
            counts[review["aro_id"]] += 1
            assert review["exact_experimental_assignment"] is False
            assert review["record_action"] == "PRESERVE_SOURCE_ASSERTION_NO_NEW_BIOLOGICAL_CLAIM"
            assert any(m.get("aro_id") == review["aro_id"] for m in record["resistance_mechanisms"])
    assert counts == {"ARO:3000309": 1, "ARO:3001307": 9, "ARO:3002547": 4,
                      "ARO:3002637": 4, "ARO:3004042": 1}


@pytest.mark.parametrize("accession,entry,seq,taxon", [
    ("P31442", 174, 2, 83333), ("P17978", 97, 1, 1280),
    ("Q6SJ71", 156, 1, 562), ("O68183", 113, 1, 37734), ("P0AE06", 154, 1, 83333),
])
def test_versioned_reference_metadata_is_not_an_allele(dossier, accession, entry, seq, taxon):
    protein = dossier["proteins"][accession]
    assert protein["entry_audit"] == {"entryVersion": entry, "sequenceVersion": seq}
    assert protein["organism"]["taxonId"] == taxon
    assert protein["experimental_assignment"] is False
    assert protein["scope"] == "REFERENCE_METADATA_NOT_EXACT_EXPERIMENTAL_ALLELE_OR_TESTED_ORGANISM"


def test_aph_name_relation_resolved_without_promoting_an_assay(dossier):
    review = dossier["nomenclature_review"]
    assert review["reference"] == "PMID:19158087"
    assert review["doi"] == "10.1074/jbc.M808148200"
    assert (review["source_name"], review["revised_name"]) == ("APH(2'')-Id", "APH(2'')-IVa")
    assert review["review_medium"] == "PUBLISHER_INDEXED_PRIMARY_DISCUSSION_TEXT"
    assert review["decision"] == "EXPLICIT_REFERENCE_NOMENCLATURE_RELATION_VERIFIED"
    assert review["table_5_visually_inspected"] is False
    assert review["native_primary_file_cached"] is False
    assert review["whole_paper_review_complete"] is False
    path = dossier["reference_path_decisions"]["ARO:3002637"]
    assert path["decision"] == "NOMENCLATURE_RESOLVED_REFERENCE_ONLY"
    assert path["experimental_assignment"] is False
    references = dossier["proteins"]["O68183"]["selected_citation_contexts"]
    original, = [r for r in references if {"database": "PubMed", "id": "9593155"} in r["identifiers"]]
    structural, = [r for r in references if {"database": "PubMed", "id": "20556826"} in r["identifiers"]]
    assert original["context"][0]["value"] == "NC95"
    assert structural["context"] == []


def test_erratum_listing_is_not_a_retraction_or_reviewed_correction(dossier):
    paper = dossier["primary_papers"]["16675700"]
    correction, = paper["commentCorrectionList"]["commentCorrection"]
    assert correction["type"] == "Erratum in"
    assert correction["reference"] == "Science. 2007 Sep 21;317(5845):1682"
    path = dossier["reference_path_decisions"]["ARO:3000309"]
    assert path["decision"] == "HOLD_PRIMARY_RESULTS_AND_ERRATUM_REVIEW"
    assert dossier["proteins"]["P31442"]["focal_citation_present"] is False
    archive, = [r for r in dossier["proteins"]["P31442"]["archive_references"] if r["id"] == "L10328"]
    assert {"key": "Status", "value": "ALT_INIT"} in archive["properties"]


def test_aac_archive_multiplicity_and_later_citation_context_are_retained(dossier):
    protein = dossier["proteins"]["Q6SJ71"]
    assert len(protein["archive_references"]) == 27
    duplicate = [r for r in protein["archive_references"] if r["id"] == "LR595879"]
    assert {p["value"] for r in duplicate for p in r["properties"] if p["key"] == "ProteinId"} == {
        "VUD38711.1", "VUD38792.1",
    }
    citation, = protein["selected_citation_contexts"]
    assert citation["scope"] == "UNIPROT_CITATION_METADATA_NOT_VERIFIED_EXPERIMENTAL_SUBJECT"
    assert {e["id"] for c in citation["context"] for e in c["evidences"]} == {
        "VUD38711.1", "SPE00920.1", "SPE01475.1",
    }
    assert dossier["reference_path_decisions"]["ARO:3002547"]["decision"] == (
        "WILD_TYPE_REFERENCE_NOT_CR1_ALLELE_ASSIGNMENT"
    )


def test_entity_taxa_and_cross_species_rejection_are_preserved(dossier):
    vgb = dossier["reference_path_decisions"]["ARO:3001307"]
    enzyme, peptide = vgb["structural_entities"]
    assert enzyme["reference_accessions"] == ["UniProtKB:P17978"]
    assert enzyme["source_organisms"][0]["ncbi_taxonomy_id"] == 1280
    assert peptide["reference_accessions"] == []
    assert peptide["source_organisms"][0]["ncbi_taxonomy_id"] == 68212
    acra = dossier["reference_path_decisions"]["ARO:3004042"]
    assert acra["decision"] == "REJECTED_FOCAL_MAPPING_DIFFERENT_SPECIES"
    assert "Enterobacter cloacae" in acra["note"]
    assert dossier["taxonomy"]["83333"]["rank"] == "strain"
    assert dossier["taxonomy"]["83333"]["parent"]["taxonId"] == 562


def test_exact_compound_limits_and_existing_collision_are_retained(dossier):
    records = {r["label"]: r for r in dossier["records"]}
    for label in ("patricin A", "patricin B"):
        assert records[label]["assertion_reviews"][0]["compound_scope"] == (
            "EXISTING_STRUCTURE_COLLISION_TODO_REMAINS_OPEN"
        )
    assert records["patricin A"]["standard_inchi_key"] == records["patricin B"]["standard_inchi_key"]
    assert records["gentamycin A"]["assertion_reviews"][0]["compound_scope"] == (
        "GENERIC_GENTAMICIN_NOT_EXACT_GENTAMYCIN_A"
    )
    assert records["quinupristin"]["assertion_reviews"][0]["compound_scope"] == (
        "NAMED_COMPOUND_IN_PRIMARY_ABSTRACT_RESULTS_PENDING"
    )


def test_access_failures_and_complete_identifier_queries_are_scoped(dossier):
    assert sorted(r["result_count"] for r in dossier["uniprot_requests"]) == [1, 4]
    for request in dossier["uniprot_requests"]:
        assert request["complete_for_query"] is True
        assert request["establishes_biological_absence"] is False
        assert request["release"] == "2026_03"
        assert urlsplit(request["url"]).hostname == "rest.uniprot.org"
    assert all(urlsplit(r["url"]).hostname == "www.ebi.ac.uk" for r in dossier["bibliographic_requests"])
    assert len(dossier["primary_papers"]) == 5
    assert all(r["relevant_primary_results_review"] == "PENDING" for r in dossier["primary_papers"].values())
    access = dossier["access_limitations"]
    assert access["europe_pmc_canary"]["status"] == 403
    assert access["europe_pmc_followup"] == "HTTP_403_CHALLENGE_STOPPED_NO_BATCH_OR_BYPASS"
    assert access["oa_xml_api_used"] is False


def test_public_export_has_no_experimental_specifications(dossier):
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
        "headers", "set-cookie", "Set-Cookie",
    }
    assert "No NCBI request" in " ".join(dossier["limitations"])
