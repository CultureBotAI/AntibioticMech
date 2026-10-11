"""Keep source bibliography, taxonomic names and experimental identity distinct."""

import json
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_topoisomerase_references as reference  # noqa: E402


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-salmonella-source-scope.json").read_bytes())


def test_source_scope_memberships_and_no_forced_experimental_assignment(dossier):
    assert len(dossier["terms"]) == 4
    assert sum(r["source_assertion_memberships"] for r in dossier["terms"].values()) == 30
    assert len({v for r in dossier["terms"].values() for v in r["record_ids"]}) == 13
    for row in dossier["terms"].values():
        assert row["experimental_subject_taxon_id"] is None
        assert row["experimental_protein_accession"] is None
        assert row["exact_allele_assignment"] is False
    assert dossier["summary"]["biological_records_changed"] == 0
    assert dossier["summary"]["whole_corpus_primary_review"] == "OPEN"


def test_other_names_are_not_promoted_to_species_synonyms(dossier):
    context = dossier["taxonomy_context"]["isangi"]
    assert context["candidate_taxon_id"] == "NCBITaxon:1386015"
    assert context["rank"] == "no rank"
    assert context["matching_name_field"] == "otherNames"
    assert context["synonym_match"] is False
    assert context["lineage_context"] == {
        "species": "NCBITaxon:28901", "genus": "NCBITaxon:590", "subspecies": "NCBITaxon:59201"}
    broad = dossier["taxonomy_context"]["broad_serovars"]
    assert broad["rank"] == "genus" and broad["taxon_id"] == "NCBITaxon:590"
    assert "NOT_A_SPECIES_OR_EXPERIMENTAL_SUBJECT" in broad["scope"]
    strains = dossier["taxonomy_context"]["strain_candidates"]
    assert len(strains) == 3
    assert all(r["selected_as_experimental_subject"] is False for r in strains)
    assert all(any("Enteritidis" in n for n in r["other_names"]) for r in strains)


def test_taxonomy_queries_and_release_remain_explicit(dossier):
    expected = {"tax-name-isangi": '"Isangi"',
                "tax-name-salmonella-genus": '"Salmonella" AND rank:genus'}
    for key, item in dossier["taxonomy_requests"].items():
        parsed = urlparse(item["url"])
        assert parsed.scheme == "https" and parsed.netloc == "rest.uniprot.org"
        assert parsed.path == "/taxonomy/search"
        assert parse_qs(parsed.query) == {"query": [expected[key]], "format": ["json"], "size": ["500"]}
        assert item["release"] == "2026_03" and item["status"] == 200
        assert len(item["cache"]["sha256"]) == len(item["receipt"]["sha256"]) == 64


def test_bibliography_identity_is_ebi_metadata_not_primary_results(dossier):
    expected = {"PMID:19104017": ("DOI:10.1128/aac.01005-08", "2009"),
                "PMID:37627729": ("DOI:10.3390/antibiotics12081309", "2023")}
    for identifier, item in dossier["bibliography"].items():
        parsed = urlparse(item["url"])
        assert parsed.scheme == "https" and parsed.netloc == "www.ebi.ac.uk"
        assert parsed.path == "/europepmc/webservices/rest/search"
        assert parse_qs(parsed.query)["query"] == ["EXT_ID:" + identifier.split(":")[1] + " AND SRC:MED"]
        assert (item["doi"], item["publication_year"]) == expected[identifier]
        assert item["bibliography_provider"] == "EMBL-EBI Europe PMC"
        assert len(item["cache"]["sha256"]) == len(item["receipt"]["sha256"]) == 64


def test_negative_result_and_access_failure_remain_explicit(dossier):
    review = dossier["primary_review"]["PMID:19104017"]
    assert review["whole_paper_review_complete"] is False
    assert review["tables_and_supplements_reviewed"] is False
    assert any("did not change" in text for text in review["findings"])
    assert any("not proof of no role" in text for text in review["findings"])
    assert "Do not promote ARO:3003317" in review["disposition"]
    unavailable = dossier["primary_review"]["PMID:37627729"]
    assert unavailable["publisher_access_status"] == "HTTP_429_STOPPED_WITHOUT_RETRY_OR_BYPASS"
    assert unavailable["primary_results_reviewed"] is False


def test_context_inputs_and_definition_citation_links_are_pinned(dossier):
    for item in dossier["inputs"].values():
        assert len(item["sha256"]) == 64
    citations = json.loads(reference.check_pin(ROOT, dossier["inputs"]["citation_audit"]).read_bytes())
    for tid, row in dossier["terms"].items():
        assert citations["terms"][tid]["definition_citation_ids"] == [row["definition_citation"]]
        assert citations["terms"][tid]["record_memberships"] == sorted(row["record_ids"])
