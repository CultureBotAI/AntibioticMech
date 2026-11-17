"""Gene/deposit agreement does not make all nearby proteins Qnr or a host resistant."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_qnr_identity_context as audit  # noqa: E402


@pytest.fixture(autouse=True)
def offline(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline Qnr audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "getaddrinfo", denied)


@pytest.fixture(scope="module")
def frozen():
    plan, data = audit.inputs(ROOT)
    projection = json.loads((ROOT / audit.NATIVE).read_bytes())
    dossier = json.loads((ROOT / audit.OUTPUT).read_bytes())
    return plan, data, projection, dossier


def test_complete_public_replay(frozen, pre_uniprot_protein_examples_root):
    assert audit.build(pre_uniprot_protein_examples_root) == frozen[3]
    assert frozen[3]["summary"] == {
        "corpus_records_hash_checked": 2939,
        "complete_records_loaded": 7,
        "source_claims_bound": 8,
        "named_member_crosswalks_verified": 1,
        "other_deposit_proteins_excluded": 3,
        "new_uniprot_requests": 1,
        "new_taxonomy_requests": 0,
        "new_reference_selections": 0,
        "experimental_identifiers_assigned": 0,
        "whole_record_primary_signoffs": 0,
        "current_selected_reference_terms": 1405,
        "current_unresolved_reference_terms": 597,
    }


def test_native_replay_when_available(frozen, require_native_inputs):
    plan, data, projection, _ = frozen
    require_native_inputs(plan, projection, data["definitions"])
    assert audit.capture(ROOT) == projection


def test_source_claims_and_reference_selection_are_preserved(frozen):
    _, data, _, dossier = frozen
    index = data["current_index"]
    assert dossier["claims"] == [c for c in index["claims"] if c["aro_id"] in audit.TERMS]
    assert dossier["records"] == [r for r in index["records"] if audit.TERMS.intersection(r["card_terms"])]
    assert dossier["terms"][audit.PARENT]["prior_reference_accessions"] == []
    assert dossier["terms"][audit.CHILD]["prior_reference_accessions"] == [audit.ACCESSION]
    for row in dossier["terms"].values():
        member = row["named_member_reference"]
        assert not member["single_protein_identity_for_whole_family"]
        assert not member["native_isolate_resistance_inferred"]
        assert not member["new_whole_corpus_reference_selection"]
        assert member["identity"] == index["proteins"][audit.ACCESSION]["identity"]
        assert all(v is None for k, v in member.items() if k.startswith("experimental_"))
        assert all(v is None for k, v in row.items() if k.startswith("experimental_"))
    assert {e["accession"] for e in dossier["excluded_same_deposit_entries"]} == {
        "UniProtKB:C0J7J4",
        "UniProtKB:C0J7J5",
        "UniProtKB:C0J7J7",
    }


@pytest.mark.parametrize(
    "change",
    [
        "duplicate",
        "extra",
        "ambiguous_gene",
        "gene",
        "taxon",
        "species_rank",
        "inactive_taxon",
        "deposit",
        "protein_id",
        "citation",
        "strain",
        "edge",
        "query",
        "release",
        "truncated",
    ],
)
def test_crosswalk_rejects_independent_identity_failures(frozen, change):
    projection = copy.deepcopy(frozen[2])
    entry = next(e for e in projection["entries"] if e["accession"] == audit.ACCESSION)
    if change == "duplicate":
        projection["entries"].append(copy.deepcopy(entry))
    elif change == "extra":
        projection["entries"][0]["accession"] = "UniProtKB:Q00000"
    elif change == "ambiguous_gene":
        projection["entries"][0]["gene_names"] = ["qnrC"]
    elif change == "gene":
        entry["gene_names"] = []
    elif change == "taxon":
        entry["organism"]["taxonId"] = 562
    elif change == "species_rank":
        projection["taxonomy"]["rank"] = "strain"
    elif change == "inactive_taxon":
        projection["taxonomy"]["active"] = False
    elif change == "deposit":
        entry["embl"][0]["id"] = "EU917445"
    elif change == "protein_id":
        entry["embl"][0]["properties"][0]["value"] = "ACK75962.1"
    elif change == "citation":
        entry["citations"][0]["identifiers"] = []
    elif change == "strain":
        entry["citations"][0]["source_strains"] = ["different subject"]
    elif change == "edge":
        projection["ontology"]["verified_edges"] = []
    elif change == "query":
        projection["query"]["query"] = "gene:qnrC"
    elif change == "release":
        projection["query"]["release"] = "unknown"
    else:
        projection["query"]["complete_for_query"] = False
    with pytest.raises(ValueError):
        audit.select_member(projection, frozen[1]["assessment"])


@pytest.mark.parametrize(
    "key",
    [
        "all_inherited_compounds_verified",
        "native_body_cached",
        "tables_reviewed",
        "figures_reviewed",
        "supplements_reviewed",
        "whole_paper_signoff",
    ],
)
def test_uninspected_evidence_cannot_be_promoted(frozen, key):
    assessment = copy.deepcopy(frozen[1]["assessment"])
    assessment["primary"][key] = True
    with pytest.raises(ValueError):
        audit.select_member(frozen[2], assessment)


@pytest.mark.parametrize(
    "key",
    [
        "native_carriage_is_not_resistant_taxon_evidence",
        "heterologous_host_results_are_separate",
        "qnrC_is_named_member_not_whole_family_identity",
    ],
)
def test_host_and_family_distinctions_cannot_be_removed(frozen, key):
    assessment = copy.deepcopy(frozen[1]["assessment"])
    assessment["primary"][key] = False
    with pytest.raises(ValueError):
        audit.select_member(frozen[2], assessment)


def test_susceptible_native_isolate_cannot_be_relabelled(frozen):
    assessment = copy.deepcopy(frozen[1]["assessment"])
    assessment["primary"]["source_quinolone_category"] = "RESISTANT"
    with pytest.raises(ValueError):
        audit.select_member(frozen[2], assessment)


def test_other_parent_citations_are_not_reported_reviewed(frozen):
    assessment = frozen[1]["assessment"]
    assert set(assessment["other_parent_citations"]) == {"PMID:15933203", "PMID:19822894"}
    assert all(not v["primary_results_reviewed"] for v in assessment["other_parent_citations"].values())
    assert not assessment["other_parent_citations"]["PMID:15933203"]["permission_denial_inferred"]


@pytest.mark.parametrize("selected_entry", [False, True])
def test_qnrc_among_multiple_gene_names_is_not_ignored(frozen, selected_entry):
    projection = copy.deepcopy(frozen[2])
    other = next(e for e in projection["entries"] if (e["accession"] == audit.ACCESSION) == selected_entry)
    other["gene_names"] = ["other", "qnrC"]
    with pytest.raises(ValueError, match="ambiguous gene reference"):
        audit.select_member(projection, frozen[1]["assessment"])
