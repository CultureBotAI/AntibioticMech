"""A structural reference and homolog discussion cannot become a focal allele claim."""

import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-11-emrd-primary-context.json").read_bytes())


def test_predecessor_is_preserved_and_record_identity_is_exact(dossier):
    predecessor = dossier["predecessor"]
    payload = (ROOT / predecessor["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == predecessor["sha256"]
    old = json.loads(payload)["reference_path_decisions"][predecessor["reference_path"]]
    assert old["decision"] == "HOLD_PRIMARY_RESULTS_AND_ERRATUM_REVIEW"
    member = dossier["record"]
    record = load_record(ROOT / member["path"])
    assert record["identifier"] == member["identifier"] == "CHEBI:17698"
    assert record["chemical_structure"]["standard_inchi_key"] == member["standard_inchi_key"]
    assert any(m.get("aro_id") == "ARO:3000309" for m in record["resistance_mechanisms"])
    assert member["record_action"] == "PRESERVE_CARD_ASSERTION_NO_PRIMARY_UPGRADE"
    assert member["whole_record_review"] == "OPEN"


def test_native_page_boundaries_and_incomplete_scope(dossier):
    review = dossier["primary_review"]
    assert review["reference"] == "PMID:16675700"
    assert review["doi"] == "10.1126/science.1125629"
    assert review["pdf_pages"] == 5
    assert review["inspected_pdf_pages_one_based"] == [2, 3, 4, 5]
    assert review["inspected_journal_pages"] == [741, 742, 743, 744]
    assert review["figures_visually_inspected"] == [1, 2, 3]
    assert review["main_article_text_reviewed"] is True
    assert review["supplements_inspected"] is False
    assert review["whole_paper_review_complete"] is False
    assert "different article" in review["page_boundary_note"]


def test_observation_comparison_and_proposal_stay_separate(dossier):
    findings = dossier["primary_review"]["findings"]
    assert [r["evidence_type"] for r in findings] == [
        "STRUCTURAL_OBSERVATION", "HOMOLOG_COMPARISON_NOT_FOCAL_PHENOTYPE", "PROPOSED_MODEL",
    ]
    assert "MdfA" in findings[1]["interpretation"]
    assert all(r["location"].startswith("Journal page") for r in findings)


def test_erratum_metadata_is_not_a_reviewed_notice(dossier):
    erratum = dossier["erratum_review"]
    assert erratum["content_inspected"] is False
    assert erratum["decision"] == "UNRESOLVED_NO_CORRECTION_OR_RETRACTION_INFERENCE"
    assert erratum["crossref_scope"] == "PAGE_LEVEL_METADATA_NOT_VERIFIED_EMRD_NOTICE_CONTENT"
    assert "Erratum content and relevance" in dossier["disposition"]["pending"]


def test_reference_identity_matches_pinned_predecessor(dossier):
    old = json.loads((ROOT / dossier["predecessor"]["path"]).read_bytes())
    protein = old["proteins"]["P31442"]
    ref = dossier["reference_grounding"]
    assert ref["accession"] == protein["accession"] == "UniProtKB:P31442"
    assert ref["gene"] == "emrD"
    assert ref["ordered_locus_names"] == ["b3673", "JW5634"]
    assert ref["entry_version"] == protein["entry_audit"]["entryVersion"]
    assert ref["sequence_version"] == protein["entry_audit"]["sequenceVersion"]
    assert ref["taxon_id"] == "NCBITaxon:83333"
    assert ref["taxon_rank"] == "strain"
    assert ref["parent_taxon_id"] == "NCBITaxon:562"
    assert ref["scope"] == "REFERENCE_IDENTITY_ONLY"
    for kind in ("allele", "strain", "genome"):
        assert ref[f"experimental_{kind}_assigned"] is False


def test_requests_are_identifier_only_and_query_completeness_is_bounded(dossier):
    search, taxonomy = dossier["uniprot_requests"]
    for request in (search, taxonomy):
        assert urlsplit(request["url"]).hostname == "rest.uniprot.org"
        assert request["status"] == 200
        assert request["release"] == "2026_03"
    query = parse_qs(urlsplit(search["url"]).query)
    assert query["query"] == ["accession:P31442"]
    assert "sequence" not in query["fields"][0].split(",")
    assert search["result_count"] == search["total_results"] == 1
    assert search["next_page_present"] is False
    assert search["complete_for_exact_accession_query_only"] is True
    assert urlsplit(taxonomy["url"]).path == "/taxonomy/83333.json"


@pytest.mark.parametrize("key", [
    "new_resistance_claims", "new_measurements", "curation_events_added", "whole_records_completed",
])
def test_followup_does_not_promote_unresolved_evidence(dossier, key):
    assert dossier["disposition"][key] == 0


def test_public_metadata_has_no_experimental_specifications(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {
        "sequence", "variants", "alteration", "protocol", "primers", "constructs",
        "measurement_value", "mic", "resistance_mechanisms", "activity_spectrum", "headers",
    }
    assert "No NCBI endpoint request" in " ".join(dossier["limitations"])
