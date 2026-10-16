"""CdsA qualification is note-only and cannot rewrite historical evidence."""

import copy
import hashlib
import json
from pathlib import Path

import pytest
import yaml

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = "research/2026-10-15-cdsa-qualification-transition.json"


def transition():
    return json.loads((ROOT / RECEIPT).read_bytes())


@pytest.mark.parametrize("index", range(4))
def test_exact_transition_preserves_all_non_note_content_and_history(
    pre_cdsa_qualification_root, index
):
    receipt = transition()
    delta = receipt["record_deltas"][index]
    live = ROOT / delta["path"]
    historical = pre_cdsa_qualification_root / delta["path"]
    assert hashlib.sha256(live.read_bytes()).hexdigest() == delta["after_sha256"]
    assert hashlib.sha256(historical.read_bytes()).hexdigest() == delta["before_sha256"]
    current, before = load_record(live), load_record(historical)
    restored = copy.deepcopy(current)
    assert restored["curation_history"].pop() == delta["added_history_event"]
    assert delta["added_history_event"]["action"] == "RESEEDED_FROM_SOURCES"
    assert len(delta["claims"]) == 1
    for change in delta["claims"]:
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
            assert current["identifier"] == "CHEBI:600103"
            assert change["aro_id"] == "ARO:3004097"
            assert "note" not in old
    assert restored == before


def test_active_review_is_only_the_original_reviews_plus_the_verified_draft(
    pre_cdsa_qualification_root,
):
    receipt = transition()
    old = json.loads((pre_cdsa_qualification_root / receipt["review_file"]["path"]).read_bytes())
    live = json.loads((ROOT / receipt["review_file"]["path"]).read_bytes())
    draft = json.loads((ROOT / receipt["proposed_review"]["path"]).read_bytes())
    old["reviews"] += draft["reviews"]
    assert live == old
    assert receipt["corpus_records_checked"] == 2939
    assert receipt["unchanged_records"] == 2935
    assert receipt["new_taxonomic_qualification_claims"] == 1
    assert receipt["existing_note_provenance_updates"] == 3
    assert receipt["experimental_identifiers_assigned"] == receipt["ncbi_requests"] == 0
    assert receipt["issue_1040"] == "DEFERRED"


@pytest.mark.parametrize("change", ["receipt", "label", "history", "note", "unrelated_claim"])
def test_historical_reconstruction_rejects_unregistered_drift(
    tmp_path, restore_pre_cdsa_qualification, change
):
    delta = next(row for row in transition()["record_deltas"] if row["identifier"] == "CHEBI:600103")
    receipt = tmp_path / RECEIPT
    receipt.parent.mkdir(parents=True)
    receipt.write_bytes((ROOT / RECEIPT).read_bytes())
    source = tmp_path / delta["path"]
    source.parent.mkdir(parents=True)
    source.write_bytes((ROOT / delta["path"]).read_bytes())
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
            document["resistance_mechanisms"][0]["note"] = "unregistered claim edit"
        source.write_text(yaml.safe_dump(document, sort_keys=False))
    original = source.read_bytes()
    output = tmp_path / "before.yaml"
    with pytest.raises(AssertionError):
        restore_pre_cdsa_qualification(tmp_path, delta["path"], output)
    assert source.read_bytes() == original
    assert not output.exists()
