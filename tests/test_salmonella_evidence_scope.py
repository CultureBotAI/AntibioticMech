"""Keep a negative primary result distinct from absence and experimental identity."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_salmonella_evidence_scope as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline scope audit attempted network")

    monkeypatch.setattr(socket, "getaddrinfo", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)


@pytest.fixture(scope="module")
def frozen():
    plan, data = audit.read_inputs(ROOT)
    dossier = json.loads((ROOT / (audit.PREFIX + ".json")).read_bytes())
    draft = json.loads((ROOT / (audit.PREFIX + "-proposed-review.json")).read_bytes())
    docs = {r["identifier"]: load_record(ROOT / r["path"]) for r in dossier["records"]}
    return plan, data, dossier, draft, docs


def test_complete_public_replay_without_native_cache(frozen):
    result, draft = audit.build(ROOT)
    assert result == frozen[2] and draft == frozen[3]
    assert result["summary"] == {
        "corpus_records_hash_checked": 2939, "complete_records_read": 13,
        "source_claims": 26, "new_qualified_reference_terms": 0,
        "proposed_note_qualifications": 13, "experimental_identifiers_assigned": 0,
        "biological_records_changed": 0, "new_ncbi_requests": 0,
        "issue_1040": "DEFERRED", "whole_record_primary_signoffs": 0,
        "whole_corpus_goal_status": "OPEN",
    }


def test_query_native_replay_when_cache_available(frozen, require_native_inputs):
    expected = frozen[2]["cached_citation_query"]
    require_native_inputs(expected)
    entries, actual = audit.literature.read_query(ROOT, ROOT / audit.literature.DIRECTORY, "19104017")
    assert not entries and actual == expected


def test_empty_query_and_taxonomy_are_not_subject_assignments(frozen):
    dossier = frozen[2]
    query = dossier["cached_citation_query"]
    assert query["complete_for_query"] is True and query["result_count"] == 0
    assert query["establishes_biological_absence"] is False
    assert query["release"] == "2026_03"
    taxonomy = dossier["taxonomy_context"]
    assert taxonomy == frozen[1]["previous_scope"]["taxonomy_context"]
    assert taxonomy["broad_serovars"]["taxon_id"] == "NCBITaxon:590"
    assert taxonomy["broad_serovars"]["rank"] == "genus"
    assert all(s["selected_as_experimental_subject"] is False for s in taxonomy["strain_candidates"])
    for term in dossier["terms"].values():
        assert not term["references"] and not term["reference_accessions"]
        assert term["whole_record_primary_review"] == "OPEN"
        assert all(v is None for k, v in term.items() if k.startswith("experimental_"))


def test_draft_is_only_pare_and_does_not_mutate_records(frozen):
    plan, data, dossier, draft, docs = frozen
    before = copy.deepcopy(docs)
    actual, projected = audit.build_draft(ROOT, plan, data, dossier["records"], dossier["claims"], docs)
    assert actual == draft and projected == dossier["curation_handoff"]["projected_claims"]
    assert before == docs
    assert len(draft["reviews"]) == 1 and len(draft["reviews"][0]["source_rows"]) == 13
    assert {r["identifier"] for r in projected} == set(docs)
    assert all(r["changed_fields"] == ["note"] and r["aro_id"] == audit.PARE for r in projected)
    assert dossier["terms"]["ARO:3003307"]["draft_qualification_proposed"] is False
    assert dossier["curation_handoff"]["production_records_written"] is False
    assert dossier["curation_handoff"]["active_curation_changed"] is False


@pytest.mark.parametrize("key", [
    "native_publisher_body_cached", "offline_primary_body_replay", "tables_visually_verified",
    "figures_reviewed", "supplements_reviewed", "whole_paper_signoff",
    "experimental_identifiers_assigned", "numeric_ast_exported", "variant_specifications_exported",
    "protocols_exported",
])
def test_uninspected_evidence_cannot_be_promoted(frozen, key):
    assessment = copy.deepcopy(frozen[1]["assessment"])
    assessment[key] = True
    with pytest.raises(ValueError, match="review scope promoted"):
        audit.check_assessment(assessment)


@pytest.mark.parametrize("key,value", [
    ("pare_result", "PROVEN_CAUSAL_RESISTANCE"),
    ("indirect_pare_role", "EXCLUDED"),
    ("universal_pare_inactivity_inferred", True),
    ("all_serovars_or_inherited_compounds_verified", True),
    ("table_3_supplies_pare_specific_comparison", True),
    ("paper_organism_scope", "Salmonella serovars"),
])
def test_negative_result_and_scope_limits_cannot_be_reversed(frozen, key, value):
    assessment = copy.deepcopy(frozen[1]["assessment"])
    assessment["assessment"][key] = value
    with pytest.raises(ValueError, match="negative result"):
        audit.check_assessment(assessment)


@pytest.mark.parametrize("change", [
    "missing", "duplicate", "chemical", "claim", "index", "subject", "path", "hash",
])
def test_claim_binding_rejects_drift(frozen, change):
    dossier, docs = copy.deepcopy(frozen[2]), copy.deepcopy(frozen[4])
    claims = dossier["claims"]
    if change == "missing":
        claims.pop()
    elif change == "duplicate":
        claims[-1] = claims[0]
    elif change == "chemical":
        docs[claims[0]["record_identifier"]]["chemical_structure"]["standard_inchi_key"] = "OTHER"
    elif change == "claim":
        claim = docs[claims[0]["record_identifier"]]["resistance_mechanisms"][claims[0]["resistance_index"]]
        claim["label"] = "changed"
    elif change == "index":
        claims[0]["resistance_index"] = claims[1]["resistance_index"]
    elif change == "path":
        claims[0]["record_path"] = claims[-1]["record_path"]
    elif change == "hash":
        claims[0]["record_sha256"] = "0" * 64
    else:
        claims[0]["experimental_subject_assignment"] = True
    with pytest.raises(ValueError):
        audit.bind_claims(dossier["records"], claims, docs)


def test_active_draft_is_not_silently_replayed(frozen):
    plan, data, dossier, draft, docs = copy.deepcopy(frozen)
    data["active_reviews"]["reviews"] += draft["reviews"]
    with pytest.raises(ValueError, match="draft already active"):
        audit.build_draft(ROOT, plan, data, dossier["records"], dossier["claims"], docs)


def test_unbound_source_row_is_rejected(frozen):
    plan, data, dossier, _, docs = copy.deepcopy(frozen)
    doc = docs[dossier["claims"][0]["record_identifier"]]
    doc["source_concepts"] = [s for s in doc["source_concepts"] if s["source"] != "ARO"]
    with pytest.raises(ValueError, match="source row ownership"):
        audit.build_draft(ROOT, plan, data, dossier["records"], dossier["claims"], docs)
