"""Note qualifications cannot alter reference identity or historical evidence."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_qualified_current as audit  # noqa: E402


@pytest.fixture(autouse=True)
def offline(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("qualification index attempted network")

    monkeypatch.setattr(socket, "getaddrinfo", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)


@pytest.fixture(scope="module")
def frozen():
    plan, data = audit.read_inputs(ROOT)
    result = json.loads((ROOT / (audit.PREFIX + ".json")).read_bytes())
    return plan, data, result


def test_full_current_corpus_replay(frozen, pre_uniprot_protein_examples_root):
    assert audit.build(pre_uniprot_protein_examples_root) == frozen[2]
    result = frozen[2]
    assert result["qualification_update_summary"] == {
        "records_checked": 2939, "card_claims_checked": 4538,
        "records_with_note_history_changes": 17, "unchanged_records": 2922,
        "new_reference_terms": 0, "new_reference_proteins": 0,
        "selected_reference_terms": 1405, "unresolved_reference_terms": 597,
        "experimental_assignments": 0, "whole_record_primary_signoffs": 0,
    }
    assert result["summary"]["current_source_qualified_claims"] == 17
    assert result["summary"]["context_only_dossiers"] == 25
    assert result["summary"]["new_followup_claims"] == 26
    assert result["summary"]["added_reference_terms"] == 0
    assert result["summary"]["added_reference_proteins"] == 0


def test_reference_registry_and_historical_claim_hashes_unchanged(frozen):
    _, data, result = frozen
    prior = data[audit.PRIOR]
    assert result["proteins"] == prior["proteins"]
    for term, old in prior["terms"].items():
        new = result["terms"][term]
        assert {**new, "followups": old["followups"]} == old
        if term in data[audit.FOLLOWUP]["terms"]:
            pointer = audit.previous.pointer(audit.FOLLOWUP, "terms", term)
            assert new["followups"] == old["followups"] + [pointer]
        else:
            assert new == old
        assert new["experimental_subject_assignment"] is False
        assert new["whole_record_primary_review"] == "OPEN"
    for new, old in zip(result["claims"], prior["claims"], strict=True):
        assert new["historical_claim_sha256"] == old["historical_claim_sha256"]
        assert {**new, **{k: old[k] for k in ("claim_sha256", "record_sha256")}} == old
    for new, old in zip(result["records"], prior["records"], strict=True):
        assert {**new, "record_sha256": old["record_sha256"]} == old


def test_historical_review_is_relocated_without_repinning_its_content(frozen):
    plan, data, result = frozen
    old = data[audit.PRIOR]["inputs"]
    for name, pin in old.items():
        if name == "active_reviews":
            assert plan["inputs"][name]["sha256"] == pin["sha256"]
            assert plan["inputs"][name]["path"].startswith("tests/fixtures/")
        else:
            assert plan["inputs"][name] == pin
    assert result["relocated_historical_inputs"] == plan["relocated_historical_inputs"]
    assert plan["inputs"]["salmonella_active_reviews"]["path"] == "curation/card_evidence_reviews.json"
    assert plan["inputs"]["salmonella_active_reviews"]["sha256"] != old["active_reviews"]["sha256"]


def test_all_evidence_pointers_and_tsv_resolve(frozen):
    _, data, result = frozen

    def visit(value):
        if isinstance(value, dict):
            if set(value) == {"input", "pointer"}:
                node = data[value["input"]]
                for key in value["pointer"].split("/")[1:]:
                    key = key.replace("~1", "/").replace("~0", "~")
                    node = node[int(key)] if isinstance(node, list) else node[key]
            else:
                for child in value.values():
                    visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(result)
    assert (ROOT / (audit.PREFIX + ".tsv")).read_text() == audit.previous.render_rows(result["records"])


@pytest.mark.parametrize("change", ["hash", "identifier", "duplicate", "non_note"])
def test_unregistered_transition_cannot_rebind_corpus(frozen, change):
    data = frozen[1]
    transition = copy.deepcopy(data["salmonella_transition"])
    delta = transition["record_deltas"][0]
    if change == "hash":
        delta["before_sha256"] = "0" * 64
    elif change == "identifier":
        delta["identifier"] = "CHEBI:1"
    elif change == "duplicate":
        transition["record_deltas"].append(copy.deepcopy(delta))
    else:
        delta["claims"][0]["changed_fields"] = ["protein_accession"]
    with pytest.raises(ValueError):
        audit.previous.current_census(data[audit.PRIOR]["records"], [transition])
