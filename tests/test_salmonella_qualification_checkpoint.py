"""Source qualification changes only approved notes and one history event per record."""

import copy
import hashlib
import json
from pathlib import Path

import pytest
import yaml

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = "research/2026-10-16-salmonella-qualification-transition.json"


def transition():
    return json.loads((ROOT / RECEIPT).read_bytes())


@pytest.mark.parametrize("index", range(17))
def test_exact_note_only_transition(
    pre_salmonella_qualification_root, pre_uniprot_protein_examples_root, index
):
    receipt = transition()
    delta = receipt["record_deltas"][index]
    live = pre_uniprot_protein_examples_root / delta["path"]
    historical = pre_salmonella_qualification_root / delta["path"]
    assert hashlib.sha256(live.read_bytes()).hexdigest() == delta["after_sha256"]
    assert hashlib.sha256(historical.read_bytes()).hexdigest() == delta["before_sha256"]
    current, before = load_record(live), load_record(historical)
    restored = copy.deepcopy(current)
    assert restored["curation_history"].pop() == delta["added_history_event"]
    assert delta["added_history_event"]["action"] == "RESEEDED_FROM_SOURCES"
    assert len(delta["claims"]) == 1
    change = delta["claims"][0]
    old = before["resistance_mechanisms"][change["index"]]
    new = restored["resistance_mechanisms"][change["index"]]
    assert old["aro_id"] == new["aro_id"] == change["aro_id"]
    assert change["changed_fields"] == ["note"]
    assert new.pop("note") == change["after_note"]
    assert new == {k: v for k, v in old.items() if k != "note"}
    if change["before_note"] is not None:
        assert change["after_note"] == change["before_note"].replace(
            receipt["review_file"]["before_sha256"], receipt["review_file"]["after_sha256"]
        )
        new["note"] = change["before_note"]
    else:
        assert change["aro_id"] == "ARO:3003317" and "note" not in old
        assert "indirect contribution remained unresolved" in change["after_note"]
        assert "not a universal inactivity claim" in change["after_note"]
    assert restored == before


def test_active_review_appends_only_verified_draft(
    pre_salmonella_qualification_root, pre_uniprot_protein_examples_root
):
    receipt = transition()
    old = json.loads((pre_salmonella_qualification_root / receipt["review_file"]["path"]).read_bytes())
    live = json.loads((pre_uniprot_protein_examples_root / receipt["review_file"]["path"]).read_bytes())
    draft = json.loads((ROOT / receipt["proposed_review"]["path"]).read_bytes())
    old["reviews"] += draft["reviews"]
    assert live == old
    assert receipt["corpus_records_checked"] == 2939
    assert receipt["unchanged_records"] == 2922
    assert receipt["new_evidence_qualification_claims"] == 13
    assert receipt["existing_note_provenance_updates"] == 4
    assert receipt["experimental_identifiers_assigned"] == receipt["ncbi_requests"] == 0
    assert receipt["issue_1040"] == "DEFERRED"
    assert not receipt["numeric_ast_exported"]
    assert not receipt["variant_specifications_exported"]
    assert not receipt["protocols_exported"]


def test_all_record_hashes_match_exactly_one_approved_transition(
    pre_salmonella_qualification_root, pre_uniprot_protein_examples_root
):
    previous = json.loads((ROOT / "research/2026-10-15-card-reference-reconciled.json").read_bytes())
    deltas = {d["path"]: d for d in transition()["record_deltas"]}
    assert len(deltas) == 17
    assert {
        p.relative_to(pre_uniprot_protein_examples_root).as_posix()
        for p in (pre_uniprot_protein_examples_root / "data/antibiotics").rglob("*.yaml")
    } == {
        r["path"] for r in previous["records"]
    }
    for record in previous["records"]:
        path = record["path"]
        before = hashlib.sha256((pre_salmonella_qualification_root / path).read_bytes()).hexdigest()
        after = hashlib.sha256((pre_uniprot_protein_examples_root / path).read_bytes()).hexdigest()
        assert before == record["record_sha256"]
        assert after == deltas.get(path, {}).get("after_sha256", before)


@pytest.mark.parametrize("change", ["receipt", "label", "history", "note", "unrelated_claim"])
def test_reconstruction_rejects_unregistered_changes(
    tmp_path, restore_pre_salmonella_qualification, pre_uniprot_protein_examples_root, change
):
    delta = next(d for d in transition()["record_deltas"] if d["identifier"] == "CHEBI:100241")
    receipt = tmp_path / RECEIPT
    receipt.parent.mkdir(parents=True)
    receipt.write_bytes((ROOT / RECEIPT).read_bytes())
    source = tmp_path / delta["path"]
    source.parent.mkdir(parents=True)
    source.write_bytes((pre_uniprot_protein_examples_root / delta["path"]).read_bytes())
    if change == "receipt":
        receipt.write_bytes(receipt.read_bytes() + b"\n")
    else:
        document = yaml.safe_load(source.read_bytes())
        if change == "label":
            document["label"] = "unregistered label"
        elif change == "history":
            document["curation_history"].pop()
        elif change == "note":
            document["resistance_mechanisms"][delta["claims"][0]["index"]]["note"] = "changed"
        else:
            document["resistance_mechanisms"][0]["note"] = "unregistered claim"
        source.write_text(yaml.safe_dump(document, sort_keys=False))
    original = source.read_bytes()
    output = tmp_path / "before.yaml"
    with pytest.raises(AssertionError):
        restore_pre_salmonella_qualification(tmp_path, delta["path"], output)
    assert source.read_bytes() == original
    assert not output.exists()
