"""Corpus-wide reconciliation must preserve evidence scope and current source bytes."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_current_references as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline reconciliation attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture(scope="module")
def frozen():
    return audit.read_inputs(ROOT)


def test_complete_reference_reconciliation(frozen):
    plan, data = frozen
    sources = {name: data[name] for name in plan["qualified_dossiers"]}
    before = copy.deepcopy(sources)
    terms, proteins = audit.reconcile_terms(data["base"], sources)
    assert sources == before
    assert len(terms) == 2002
    assert sum(bool(t["reference_links"]) for t in terms.values()) == 1398
    assert sum(not t["reference_links"] for t in terms.values()) == 604
    assert sum(len(t["reference_links"]) for t in terms.values()) == 3064
    for tid, old in data["base"]["terms"].items():
        for i, link in enumerate(old["links"]):
            current = terms[tid]["reference_links"][i]
            assert current["protein_accession"] == link["protein_accession"]
            assert current["kind"] == link["kind"]
            assert current["evidence"] == audit.pointer("base", "terms", tid, "links", i)
        assert terms[tid]["record_memberships"] == old["record_memberships"]
        assert terms[tid]["whole_record_primary_review"] == "OPEN"
    for accession, old in data["base"]["proteins"].items():
        assert proteins[accession]["identity"] == old["identity"]
    assert terms["ARO:3009459"]["reference_links"] == []


def test_shared_reference_view_is_not_a_duplicate_biological_replicate(frozen):
    _, data = frozen
    view = data["card-gene-reference-followup"]["reference_views"]["UniProtKB:Q2G2M2"]
    identity = audit.view_identity(view)
    proteins = {}
    source = audit.pointer("source", "reference_views", "UniProtKB:Q2G2M2")
    audit.add_reference(proteins, "UniProtKB:Q2G2M2", identity, source)
    audit.add_reference(proteins, "UniProtKB:Q2G2M2", identity, source)
    assert proteins["UniProtKB:Q2G2M2"]["sources"] == [source]
    conflict = {**identity, "entry_version": identity["entry_version"] + 1}
    with pytest.raises(ValueError, match="conflicting reference"):
        audit.add_reference(proteins, "UniProtKB:Q2G2M2", conflict, audit.pointer("other", "reference"))


@pytest.mark.parametrize("change", ["taxon", "name", "active", "species", "allele", "subject", "version"])
def test_reference_identity_cannot_be_promoted_or_misgrounded(frozen, change):
    _, data = frozen
    view = copy.deepcopy(data["card-gene-reference-followup"]["reference_views"]["UniProtKB:Q2G2M2"])
    if change == "taxon":
        view["reference_taxonomy"]["taxon_id"] = "NCBITaxon:999"
    elif change == "name":
        view["native_protein_taxonomy"]["scientificName"] = "different"
    elif change == "active":
        view["reference_taxonomy"]["active"] = False
    elif change == "species":
        view["reference_taxonomy"]["species"] = None
    elif change == "allele":
        view["exact_allele_assignment"] = True
    elif change == "subject":
        view["experimental_subject_assignment"] = True
    else:
        view["entry_audit"]["entryVersion"] = True
    with pytest.raises(ValueError):
        audit.view_identity(view)


@pytest.mark.parametrize("change", ["membership", "label", "candidate", "duplicate", "subject"])
def test_changed_dossier_link_fails_closed(frozen, change):
    _, data = frozen
    dossier = copy.deepcopy(data["card-gene-reference-followup"])
    row = dossier["terms"]["ARO:3003319"]
    if change == "membership":
        row["record_memberships"] = ["WRONG_RECORD"]
    elif change == "label":
        row["source_label"] += " changed"
    elif change == "candidate":
        row["reference_candidates"][0]["qualified_reference"] = False
    elif change == "duplicate":
        row["qualified_reference_accessions"].append(row["qualified_reference_accessions"][0])
    else:
        row["reference_candidates"][0]["experimental_subject_assignment"] = True
    with pytest.raises(ValueError):
        audit.reconcile_terms(data["base"], {"source": dossier})


def test_current_census_applies_ordered_exact_transitions(frozen):
    _, data = frozen
    transitions = [data["first_transition"], data["cdsa_transition"]]
    updated = audit.current_census(data["census"], transitions)
    original = {r["identifier"]: r for r in data["census"]}
    changed = [r for r in updated if r != original[r["identifier"]]]
    assert len(updated) == 2939 and len(changed) == 4
    for row in changed:
        assert {**row, "record_sha256": original[row["identifier"]]["record_sha256"]} == original[
            row["identifier"]
        ]
    with pytest.raises(ValueError, match="discontinuous"):
        audit.current_census(data["census"], list(reversed(transitions)))


def test_current_claim_notes_restore_only_the_documented_history(frozen):
    _, data = frozen
    transitions = [data["first_transition"], data["cdsa_transition"]]
    for delta in data["cdsa_transition"]["record_deltas"]:
        for change in delta["claims"]:
            claim = {"aro_id": change["aro_id"], "note": change["after_note"], "untouched": "preserved"}
            expected = {"aro_id": change["aro_id"], "untouched": "preserved"}
            assert audit.original_claim(claim, delta["identifier"], change["index"], transitions) == expected
            claim["note"] = "unexpected"
            with pytest.raises(ValueError, match="note drift"):
                audit.original_claim(claim, delta["identifier"], change["index"], transitions)


def test_public_record_and_pointer_accounting(frozen):
    _, data = frozen
    doc = json.loads((ROOT / (audit.PREFIX + ".json")).read_bytes())
    assert len(doc["records"]) == 2939 and len(doc["claims"]) == 4538
    assert sum(r["card_assertions"] for r in doc["records"]) == 4538
    assert sum(r["phi_claims_not_reassessed"] for r in doc["records"]) == 217
    assert sum(r["curator_claims_not_reassessed"] for r in doc["records"]) == 133
    assert sum(r["score_rules_not_reassessed"] for r in doc["records"]) == 467
    assert doc["summary"]["current_source_qualified_claims"] == 4
    assert len(doc["unresolved_reference_worklist"]) == 604
    assert all(r["whole_record_primary_review"] == "OPEN" for r in doc["records"])
    assert all(not r["no_card_assertions_is_review_complete"] for r in doc["records"])
    assert doc["context_only_followups"]["bcmfs1-reference"]["aro_ids"] == ["ARO:3009459"]
    assert doc["terms"]["ARO:3009459"]["reference_accessions"] == []
    assert (ROOT / (audit.PREFIX + ".tsv")).read_text() == audit.render_rows(doc["records"])

    def visit(value):
        if isinstance(value, dict):
            if set(value) == {"input", "pointer"}:
                node = data[value["input"]]
                for key in value["pointer"].split("/")[1:]:
                    key = key.replace("~1", "/").replace("~0", "~")
                    node = node[int(key)] if isinstance(node, list) else node[key]
            else:
                for item in value.values():
                    visit(item)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(doc)
    assert not doc["constraints"]["full_investigation_complete"]
    assert not doc["constraints"]["experimental_identifiers_assigned"]
    assert doc["constraints"]["issue_1040"] == "DEFERRED"
