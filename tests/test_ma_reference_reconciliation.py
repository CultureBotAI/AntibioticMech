"""Prove the historical Ma transition using only committed census snapshots."""

import csv
import hashlib
import io
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-12-ma-reference"
TARGETS = {"CHEBI:28909", "CHEBI:81763"}


def census_rows(payload):
    rows = list(csv.DictReader(io.StringIO(payload.decode()), delimiter="\t"))
    indexed = {row["identifier"]: row for row in rows}
    assert len(indexed) == len(rows) == 2939
    assert len({row["path"] for row in rows}) == len(rows)
    return indexed


def assert_reconciliation(receipt, reconciliation, payloads):
    for key, payload in payloads.items():
        assert hashlib.sha256(payload).hexdigest() == reconciliation[key]["sha256"]
    before = census_rows(payloads["previous_census"])
    after = census_rows(payloads["current_census"])
    assert before.keys() == after.keys()
    changed = {identifier for identifier in before
               if before[identifier]["record_sha256"] != after[identifier]["record_sha256"]}
    transitions = {row["identifier"]: row for row in receipt["records"]}
    assert len(transitions) == len(receipt["records"]) == 22
    assert transitions.keys() == changed
    assert reconciliation["records"] == len(after)
    assert reconciliation["records_changed"] == len(changed)
    assert reconciliation["records_byte_identical"] == receipt["records_byte_identical"] == (
        len(after) - len(changed))
    assert {i for i, row in transitions.items() if row["scope_corrections"]} == TARGETS
    for identifier, old in before.items():
        new = after[identifier]
        if identifier not in changed:
            assert old == new
            continue
        transition = transitions[identifier]
        assert transition["path"] == old["path"] == new["path"]
        assert transition["before_sha256"] == old["record_sha256"]
        assert transition["after_sha256"] == new["record_sha256"]
        assert transition["scope_corrections"] == (2 if identifier in TARGETS else 0)
        assert type(transition["checksum_refreshes"]) is int
        assert transition["checksum_refreshes"] >= 0
        expected = {**old, "record_sha256": new["record_sha256"]}
        if identifier in TARGETS:
            references = set(old["primary_papers_pending"].split("|"))
            assert "PMID:38374637" in references
            expected["primary_papers_pending"] = "|".join(sorted(
                references | {"DOI:10.1021/acs.jafc.3c08093.s001"}))
        assert new == expected
    assert receipt["scope_corrections"] == reconciliation["new_identifier_scope_decisions"] == (
        sum(row["scope_corrections"] for row in transitions.values())) == 4
    assert receipt["checksum_refreshes"] == reconciliation["previous_decision_checksum_refreshes"] == (
        sum(row["checksum_refreshes"] for row in transitions.values())) == 185
    for key in ("resistance_assertions", "activity_observations"):
        assert reconciliation[key] == sum(int(row[key]) for row in after.values())
    assert reconciliation["whole_record_reviews_completed"] == 0
    assert reconciliation["whole_corpus_primary_review"] == "OPEN"


@pytest.fixture
def checkpoint():
    receipt = json.loads(Path(str(PREFIX) + "-curation.json").read_bytes())
    reconciliation = json.loads(Path(str(PREFIX) + "-reconciliation.json").read_bytes())
    payloads = {key: (ROOT / reconciliation[key]["path"]).read_bytes()
                for key in ("previous_census", "current_census")}
    return receipt, reconciliation, payloads


def test_full_historical_reconciliation_is_portable(checkpoint):
    assert_reconciliation(*checkpoint)


@pytest.mark.parametrize("mutation", [
    "before_hash", "after_hash", "path", "missing", "duplicate", "scope", "refreshes",
])
def test_non_card_bridge_receipt_drift_is_rejected(checkpoint, mutation):
    receipt, reconciliation, payloads = checkpoint
    row = next(r for r in receipt["records"] if r["identifier"] == "CHEBI:136340")
    if mutation in {"before_hash", "after_hash"}:
        row[mutation.replace("_hash", "_sha256")] = "0" * 64
    elif mutation == "path":
        row["path"] = "data/antibiotics/wrong.yaml"
    elif mutation == "missing":
        receipt["records"].remove(row)
    elif mutation == "duplicate":
        receipt["records"].append(dict(row))
    elif mutation == "scope":
        row["scope_corrections"] = 1
    else:
        row["checksum_refreshes"] += 1
    with pytest.raises(AssertionError):
        assert_reconciliation(receipt, reconciliation, payloads)


@pytest.mark.parametrize("key", [
    "records", "records_changed", "records_byte_identical", "new_identifier_scope_decisions",
    "previous_decision_checksum_refreshes", "resistance_assertions", "activity_observations",
    "whole_record_reviews_completed", "whole_corpus_primary_review",
])
def test_reconciliation_aggregate_drift_is_rejected(checkpoint, key):
    receipt, reconciliation, payloads = checkpoint
    reconciliation[key] = "COMPLETE" if key == "whole_corpus_primary_review" else reconciliation[key] + 1
    with pytest.raises(AssertionError):
        assert_reconciliation(receipt, reconciliation, payloads)


@pytest.mark.parametrize("repin", [False, True])
@pytest.mark.parametrize("mutation", ["hash", "membership", "duplicate", "unchanged_row", "pending"])
def test_census_drift_is_rejected_even_after_repinning(checkpoint, mutation, repin):
    receipt, reconciliation, payloads = checkpoint
    rows = list(csv.DictReader(io.StringIO(payloads["current_census"].decode()), delimiter="\t"))
    changed = {row["identifier"] for row in receipt["records"]}
    row = next(row for row in rows if row["identifier"] not in changed)
    if mutation == "hash":
        row["record_sha256"] = "0" * 64
    elif mutation == "membership":
        row["identifier"] = "CHEBI:unexpected"
    elif mutation == "duplicate":
        rows.append(dict(row))
    elif mutation == "unchanged_row":
        row["label"] += " unexpected"
    else:
        row = next(row for row in rows if row["identifier"] in TARGETS)
        row["primary_papers_pending"] = ""
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    payloads["current_census"] = buffer.getvalue().encode()
    if repin:
        reconciliation["current_census"]["sha256"] = hashlib.sha256(
            payloads["current_census"]).hexdigest()
    with pytest.raises(AssertionError):
        assert_reconciliation(receipt, reconciliation, payloads)
