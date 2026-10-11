"""Producer reference leads must not become exact allele or phenotype claims."""

import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-producer-gene-reference-grounding.json").read_bytes())


def record(dossier, identifier):
    return next(r for r in dossier["records"] if r["identifier"] == identifier)


@pytest.mark.parametrize("identifier", ["CHEBI:133621", "CHEBI:67811", "antibioticmech:aro-5d5ecfee72"])
def test_leads_retain_exact_compound_identity(dossier, identifier):
    lead = record(dossier, identifier)
    current = load_record(ROOT / lead["path"])
    assert current["identifier"] == identifier
    assert current["chemical_structure"]["standard_inchi_key"] == lead["standard_inchi_key"]
    assert len(lead["sha256"]) == 64
    assert lead["new_experimental_identifiers_assigned"] is False
    assert lead["primary"]["full_results_inspected"] is False
    assert lead["primary"]["figures_inspected"] is False


def test_valanimycin_citation_does_not_equate_deposits(dossier):
    lead = record(dossier, "CHEBI:133621")
    protein = lead["reference_protein"]
    assert protein["accession"] == "UniProtKB:Q9LA76"
    assert protein["entry_version"] == 81 and protein["sequence_version"] == 1
    assert protein["gene_symbols"] == []
    assert protein["reference_strain_labels"] == ["MG456-hf10"]
    assert "10708373" in protein["citation_ids"]
    assert protein["archive_cross_references"] == [
        {"database": "EMBL", "id": "AY116644", "protein_id": "AAN10244.1"},
    ]
    assert lead["primary"]["paper_reported_deposit"] == "AF148322"
    assert lead["source_organism"] == "Streptomyces viridifaciens MG456-hF10"
    assert lead["laboratory_hosts"] == ["Escherichia coli", "Streptomyces lividans"]
    assert lead["status"] == "REFERENCE_CITATION_LINK_EXACT_ARCHIVE_JOIN_UNRESOLVED"


def test_zorbamycin_other_name_is_not_subject_taxonomy(dossier):
    lead = record(dossier, "CHEBI:67811")
    protein = lead["reference_protein"]
    assert protein["accession"] == "UniProtKB:B9UIZ4"
    assert protein["gene_symbols"] == ["zbmA"]
    assert protein["entry_version"] == 41 and protein["sequence_version"] == 1
    assert "26512730" in protein["citation_ids"]
    assert protein["archive_cross_references"] == [
        {"database": "EMBL", "id": "EU670723", "protein_id": "ACG60763.1"},
    ]
    assert lead["source_organism"] == "Streptomyces flavoviridis ATCC21892"
    taxon = dossier["taxonomy"]["28893"]
    assert taxon["scientificName"] == protein["organism"]["scientificName"] == "Streptomyces pilosus"
    assert "Streptomyces flavoviridis" in taxon["otherNames"]
    assert "Streptomyces flavoviridis" not in taxon.get("synonyms", [])
    assert lead["status"] == "REFERENCE_CITATION_LINK_SUBJECT_TAXON_AND_PRIMARY_RESULTS_PENDING"


def test_efrotomycin_congener_scope_remains_open(dossier):
    lead = record(dossier, "antibioticmech:aro-5d5ecfee72")
    assert lead["gene_lead"] == "efrT"
    assert lead["primary"]["reference"] == "PMID:36445346"
    assert lead["status"] == "CONGENER_SCOPE_AND_PUTATIVE_DETERMINANT_HOLD"
    assert lead["exact_record_compound_join"] == "NOT_ESTABLISHED"
    assert lead["paper_compound_scope"] == [
        "efrotomycin A1", "efrotomycin A2", "efrotomycin A3", "efrotomycin A4", "efrotomycin B1",
    ]
    assert "reference_protein" not in lead
    assert "production effect does not establish measured resistance" in lead["context"]


@pytest.mark.parametrize("query,count", [
    ("gene_exact:vlmF", 0), ("gene_exact:zbmA", 1), ("gene_exact:efrT", 0),
    ("AF148322", 0), ("valanimycin", 25), ("efrotomycin", 0),
])
def test_no_hit_queries_do_not_establish_absence(dossier, query, count):
    receipt, = [r for r in dossier["uniprot_requests"] if r.get("query") == query]
    assert receipt["result_count"] == count
    assert receipt["complete_for_query"] is True
    assert receipt["zero_results_establish_absence"] is False
    assert parse_qs(urlsplit(receipt["url"]).query)["query"] == [query]


@pytest.mark.parametrize("taxon_id", ["28893", "48665"])
def test_reference_taxa_are_species_not_strains(dossier, taxon_id):
    taxon = dossier["taxonomy"][taxon_id]
    assert taxon["taxonId"] == int(taxon_id)
    assert taxon["rank"] == "species" and taxon["active"] is True
    assert taxon["parent"]["taxonId"] == 1883


def test_receipts_are_versioned_and_access_failures_are_not_results(dossier):
    assert len(dossier["uniprot_requests"]) == 8
    for receipt in dossier["uniprot_requests"]:
        assert urlsplit(receipt["url"]).hostname == "rest.uniprot.org"
        assert receipt["status"] == 200 and receipt["release"] == "2026_03"
        assert len(receipt["sha256"]) == len(receipt["cache"]["sha256"]) == 64
        assert receipt["retrieved_at"].startswith("2026-10-09")
    assert {(urlsplit(r["url"]).hostname, r["status"]) for r in dossier["primary_access_receipts"]} == {
        ("www.ebi.ac.uk", 500), ("www.microbiologyresearch.org", 403),
    }
    assert all(not r["full_text_obtained"] for r in dossier["primary_access_receipts"])


def test_reference_review_does_not_advance_whole_record_completion(dossier):
    assert dossier["status"] == "REFERENCE_LEADS_ONLY_NO_BIOLOGICAL_CURATION"
    assert dossier["scope"] == {
        "corpus_records": 2939, "selected_records": 3, "reference_candidates": 2,
        "whole_records_completed_by_this_review": 0, "full_corpus_primary_review": "OPEN",
    }
    assert dossier["preservation"]["record_hashes_verified"] == 2939
    assert dossier["preservation"]["ignored_files_included"] is True
    assert dossier["preservation"]["biological_record_changes"] == 0
    assert dossier["preservation"]["curation_events_added"] == 0
    for lead in dossier["records"]:
        if "reference_protein" in lead:
            assert lead["reference_protein"]["scope"] == (
                "DATABASE_REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE_ASSIGNMENT"
            )


def test_export_remains_identifiers_bibliography_and_context(dossier):
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
