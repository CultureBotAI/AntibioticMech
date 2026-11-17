"""Historical replay cannot conceal unregistered record or receipt drift."""

import hashlib
import json
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = "research/2026-10-15-card-evidence-qualifications-verification.json"
DELTAS = json.loads((ROOT / RECEIPT).read_bytes())["record_deltas"]


@pytest.mark.parametrize("delta", DELTAS, ids=lambda row: row["identifier"])
def test_restored_record_matches_both_pins_without_modifying_live_input(
    tmp_path,
    restore_pre_card_qualification,
    pre_cdsa_qualification_root,
    delta,
):
    source = pre_cdsa_qualification_root / delta["path"]
    original = source.read_bytes()
    output = restore_pre_card_qualification(
        pre_cdsa_qualification_root, delta["path"], tmp_path / "before.yaml"
    )
    assert source.read_bytes() == original
    assert hashlib.sha256(original).hexdigest() == delta["after_sha256"]
    assert hashlib.sha256(output.read_bytes()).hexdigest() == delta["before_sha256"]


@pytest.mark.parametrize("change", ["receipt", "label", "history", "note", "unrelated_claim"])
def test_restoration_rejects_unregistered_drift(
    tmp_path, restore_pre_card_qualification, pre_cdsa_qualification_root, change
):
    delta = DELTAS[0]
    receipt = tmp_path / RECEIPT
    receipt.parent.mkdir(parents=True)
    receipt.write_bytes((ROOT / RECEIPT).read_bytes())
    source = tmp_path / delta["path"]
    source.parent.mkdir(parents=True)
    source.write_bytes((pre_cdsa_qualification_root / delta["path"]).read_bytes())
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
        restore_pre_card_qualification(tmp_path, delta["path"], output)
    assert source.read_bytes() == original
    assert not output.exists()
