"""Acceptance tests for explicit target-role semantics (#93)."""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from curation_worklist import target_evidence_queue  # noqa: E402


def test_aro_target_role_map_covers_every_inventory_target(repo_root):
    raw = repo_root / "data" / "raw" / "aro_target_edges.tsv"
    roles = repo_root / "conf" / "aro_target_roles.tsv"
    with raw.open(newline="", encoding="utf-8") as handle:
        target_ids = {row["target_id"] for row in csv.DictReader(handle, delimiter="\t")}
    with roles.open(newline="", encoding="utf-8") as handle:
        mapped = list(csv.DictReader(handle, delimiter="\t"))
    assert len(mapped) == 54
    assert {row["target_id"] for row in mapped} == target_ids
    assert all(row["rationale"] for row in mapped)


def test_every_card_target_has_relation_type_context_and_ownership(records):
    problems = []
    counts = Counter()
    for path, record in records:
        for target in record.get("molecular_targets") or []:
            if target.get("source") != "CARD_ARO":
                continue
            counts[target["target_relation"]] += 1
            required = (
                "target_type",
                "target_relation",
                "experimental_context",
                "evidence_status",
                "source_version",
                "source_retrieved_on",
            )
            missing = [field for field in required if not target.get(field)]
            if missing:
                problems.append((path.name, target.get("target_label"), missing))
    assert problems == [], problems[:20]
    # Three inventory edges collapse during record harmonization; the count in
    # issue #93 was 249, and is 248 since iclaprim's record was withdrawn (#133)
    # — CARD's cross-reference put that DHFR target on Isoaminile citrate's
    # structure, so the edge had nothing true to attach to.
    assert sum(counts.values()) == 248
    assert counts["SUSCEPTIBILITY_DETERMINANT"] > 0
    assert counts["RESISTANCE_DETERMINANT"] > 0
    assert counts["REQUIRED_UPTAKE_OR_ACTIVATION_FACTOR"] > 0
    assert counts["DOWNSTREAM_AFFECTED_PROCESS"] > 0
    assert counts["ATTACKED_COMPONENT"] > 0


def test_daptomycin_determinants_are_not_presented_as_direct_targets(records):
    record = next(record for _, record in records if record["identifier"] == "CHEBI:600103")
    by_id = {
        target.get("target_id"): target
        for target in record["molecular_targets"]
        if target.get("source") == "CARD_ARO"
    }
    assert by_id["ARO:3003275"]["target_relation"] == "SUSCEPTIBILITY_DETERMINANT"
    assert by_id["ARO:3003278"]["target_relation"] == "DOWNSTREAM_AFFECTED_PROCESS"
    assert by_id["ARO:3003280"]["target_relation"] == "SUSCEPTIBILITY_DETERMINANT"
    assert by_id["ARO:3003281"]["target_relation"] == "SUSCEPTIBILITY_DETERMINANT"
    primary = [
        target
        for target in record["molecular_targets"]
        if target.get("evidence_status") == "PRIMARY_EVIDENCE"
    ]
    assert [(target["target_label"], target["target_relation"]) for target in primary] == [
        ("phosphatidylglycerol-rich bacterial membrane", "DIRECT_BINDING_TARGET")
    ]
    assert primary[0]["evidence"][0]["reference"] == "PMID:40455071"


def test_database_only_direct_targets_are_explicitly_queued(records):
    corpus = [record for _, record in records]
    queued = target_evidence_queue(corpus)
    queued_ids = {row["key"] for row in queued}
    direct_ids = {
        target["target_id"]
        for record in corpus
        for target in record.get("molecular_targets") or []
        if target.get("source") == "CARD_ARO"
        and target.get("target_relation") == "DIRECT_BINDING_TARGET"
    }
    assert queued_ids == direct_ids
    assert all("primary citation needed" in row["hint"] for row in queued)


def test_resistance_context_cannot_silently_claim_direct_binding(records):
    offenders = []
    for path, record in records:
        for target in record.get("molecular_targets") or []:
            if target.get("source") != "CARD_ARO":
                continue
            label = target.get("target_label", "").casefold()
            if "resistant" in label and target.get("target_relation") == "DIRECT_BINDING_TARGET":
                offenders.append((path.name, target.get("target_id"), label))
    assert offenders == []
