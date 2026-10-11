"""A retrieval restart preserves historical evidence and does not imply primary review."""

import csv
import gzip
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def checkpoint():
    dossier = json.loads((ROOT / "research/2026-10-09-resistance-discovery-restart.json").read_bytes())
    stored = (ROOT / dossier["delta_candidate_index"]["path"]).read_bytes()
    return dossier, json.loads(gzip.decompress(stored))


def read_pin(pin):
    path = ROOT / pin["path"]
    payload = path.read_bytes()
    assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
    return json.loads(payload)


def test_restart_covers_every_original_query_and_retains_chemical_memberships(checkpoint):
    dossier, delta = checkpoint
    planned = read_pin(dossier["plan"])
    by_key = {q["query_key"]: q for q in planned["queries"]}
    reused = set(dossier["reused_complete_query_keys"])
    restarted = {q["query_key"] for q in delta["queries"]}
    assert len(by_key) == 611 and len(reused) == 520 and len(restarted) == 91
    assert reused.isdisjoint(restarted) and reused | restarted == set(by_key)
    assert dossier["summary"]["corpus_records"] == planned["corpus_records"] == 2939
    assert dossier["summary"]["query_record_memberships"] == sum(
        len(q["members"]) for q in planned["queries"]
    ) == 612
    assert dossier["corpus_sha256"] == planned["corpus_sha256"] == delta["corpus_sha256"]
    assert delta["plan_sha256"] == dossier["plan"]["sha256"]
    for query in delta["queries"]:
        original = by_key[query["query_key"]]
        assert {k: query[k] for k in original} == original


def test_only_previously_conflicted_chains_are_retried(checkpoint):
    dossier, delta = checkpoint
    parent = read_pin(dossier["parent_descriptor"])
    conflicts = {q["query_key"]: q for q in parent["query_conflicts"]}
    assert set(conflicts) == {q["query_key"] for q in delta["queries"]}
    transitions = {q["query_key"]: q for q in dossier["retry_transitions"]}
    assert set(transitions) == set(conflicts)
    for query in delta["queries"]:
        key = query["query_key"]
        transition = transitions[key]
        previous = conflicts[key]
        assert transition["previous_status"] == "CURSOR_CONFLICT_REQUIRES_RESTART"
        assert transition["new_status"] == query["status"]
        assert transition["record_identifiers"] == previous["record_identifiers"]
        old_prefix_count = previous["rejected_page"]["accepted_prefix_citations"]
        assert transition["previous_retained_citations"] == old_prefix_count
        assert transition["new_retained_citations"] == len(query["candidates"])
        assert query["pages"][0]["request"]["params"]["cursorMark"] == "*"
        assert datetime.fromisoformat(query["pages"][0]["request"]["retrieved_at"]) > datetime.fromisoformat(
            previous["rejected_page"]["request"]["retrieved_at"]
        )


def test_summary_does_not_double_count_retried_prefixes(checkpoint):
    dossier, delta = checkpoint
    parent = read_pin(dossier["parent_descriptor"])
    old_prefixes = sum(c["rejected_page"]["accepted_prefix_citations"] for c in parent["query_conflicts"])
    retained = parent["summary"]["retained_query_citation_memberships"] - old_prefixes
    retained += sum(len(q["candidates"]) for q in delta["queries"])
    assert dossier["summary"]["retained_query_citation_memberships"] == retained
    retry_status = Counter(q["status"] for q in delta["queries"])
    assert dict(retry_status) == dossier["retry_status"]
    retry_status["CURSOR_TRAVERSAL_COMPLETE"] += 520
    assert dict(retry_status) == dossier["summary"]["query_status"]
    assert dossier["completed_historical_pages_reused"] == 660
    retry_pages = sum(len(q["pages"]) + ("rejected_page" in q) for q in delta["queries"])
    assert dossier["fresh_retry_pages_including_canary"] == retry_pages
    union = dossier["expansion_history_union"]
    assert union["historical_distinct_citations"] == parent["summary"]["unique_retained_citations"]
    assert union["selected_retry_distinct_citations"] == dossier["summary"]["unique_retained_citations"]
    assert union["union_distinct_citations"] == (
        union["historical_distinct_citations"] + union["retry_ids_absent_from_historical_index"]
    )
    assert union["union_distinct_citations"] == (
        union["selected_retry_distinct_citations"] + union["historical_ids_absent_from_selected_retry_index"]
    )
    assert "NOT_ONE_VALIDATED_CURSOR_CHAIN" in union["scope"]


def test_combined_ledger_preserves_all_memberships_and_pending_primary_review(checkpoint):
    dossier, _ = checkpoint
    plan = read_pin(dossier["plan"])
    path = ROOT / dossier["ledger"]["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == dossier["ledger"]["sha256"]
    with path.open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(rows) == 612
    assert [(r["query_key"], r["identifier"], r["query_id"]) for r in rows] == [
        (q["query_key"], m["identifier"], m["query_id"]) for q in plan["queries"] for m in q["members"]
    ]
    statuses = {}
    for row in rows:
        assert row["primary_review_status"] == "PENDING"
        assert statuses.setdefault(row["query_key"], row["status"]) == row["status"]
    assert dict(Counter(statuses.values())) == dossier["summary"]["query_status"]


def test_compressed_delta_is_pinned_separately_from_historical_index(checkpoint):
    dossier, delta = checkpoint
    artifact = dossier["delta_candidate_index"]
    stored = (ROOT / artifact["path"]).read_bytes()
    expanded = gzip.decompress(stored)
    assert hashlib.sha256(stored).hexdigest() == artifact["sha256"]
    assert hashlib.sha256(expanded).hexdigest() == artifact["uncompressed_sha256"]
    assert len(stored) == artifact["stored_bytes"] and len(expanded) == artifact["uncompressed_bytes"]
    assert stored[4:8] == b"\x00\x00\x00\x00"
    original = dossier["parent_candidate_index"]
    assert original["path"] != artifact["path"]
    assert hashlib.sha256((ROOT / original["path"]).read_bytes()).hexdigest() == original["sha256"]
    assert delta["restart_manifest_sha256"] == dossier["restart_manifest"]["sha256"]


def test_invalid_pages_are_not_salvaged_or_counted_as_complete(checkpoint):
    _, delta = checkpoint
    for query in delta["queries"]:
        identifiers = [(c["source"], c["id"]) for c in query["candidates"]]
        assert len(identifiers) == len(set(identifiers))
        assert len(identifiers) == sum(p["retained_citations"] for p in query["pages"])
        if "rejected_page" in query:
            assert query["status"] == "CURSOR_CONFLICT_REQUIRES_RESTART"
            assert query["rejected_page"]["accepted_prefix_citations"] == len(identifiers)
        if query["status"] == "CURSOR_TRAVERSAL_COMPLETE":
            assert query["next_cursor"] is None and "rejected_page" not in query
            assert len(identifiers) == query["hit_count"]


def test_citation_only_export_is_not_allele_or_curation_evidence(checkpoint):
    dossier, delta = checkpoint
    assert dossier["scope"] == delta["scope"] == (
        "CITATION_DISCOVERY_ONLY; NO_COMPOUND_ALLELE_OR_AST_ASSIGNMENTS"
    )
    assert dossier["primary_review_status"] == "PENDING"
    assert all(q["primary_review_status"] == "PENDING" for q in delta["queries"])
    assert dossier["biological_record_changes"] == dossier["curation_events_added"] == 0
    assert dossier["record_hashes_verified"] == 2939
    assert dossier["record_path_search_includes_ignored"] is True
    assert dossier["original_name_query_caches_preserved"] == 7466
    assert dossier["historical_expansion_responses_preserved"] == 886
    assert "no NCBI request" in dossier["network"]
    fields = {"id", "source", "pmid", "pmcid", "doi", "title", "pubYear", "pubType"}
    assert all(set(c) <= fields for q in delta["queries"] for c in q["candidates"])


def test_completion_label_matches_every_query_not_just_the_canary(checkpoint):
    dossier, _ = checkpoint
    complete = dossier["summary"]["query_status"] == {"CURSOR_TRAVERSAL_COMPLETE": 611}
    assert dossier["status"] == (
        "PLANNED_CURSOR_TRAVERSALS_COMPLETE_NOT_PRIMARY_REVIEW" if complete else
        "PARTIAL_CITATION_DISCOVERY_NOT_PRIMARY_REVIEW"
    )
    assert "Do not combine pages within a query" in dossier["composition"]


def test_ordering_canary_is_not_silently_spliced_into_the_batch(checkpoint):
    dossier, delta = checkpoint
    canary = dossier["ordering_canary"]
    assert canary["scope"] == "SEPARATE_CANARY_NOT_SUBSTITUTED_INTO_THE_BATCH_RETRY_CHAIN"
    query, = [q for q in delta["queries"] if q["query_key"] == canary["query_key"]]
    assert query["query"] == canary["query"] and query["members"] == canary["members"]
    assert [o["requested_sort"] for o in canary["outcomes"]] == [None, "P_PDATE_D desc"]
    for outcome in canary["outcomes"]:
        assert outcome["status"] == "CURSOR_TRAVERSAL_COMPLETE"
        assert outcome["retained_citations"] == outcome["hit_count"] == 2503
        assert len(outcome["responses"]) == 3
        assert outcome["responses"][0]["params"]["cursorMark"] == "*"
        assert all(r["params"].get("sort") == outcome["requested_sort"] for r in outcome["responses"])
        assert len(outcome["inter_page_retrieval_seconds"]) == 2
        assert all(value >= 0 for value in outcome["inter_page_retrieval_seconds"])
    same = len({o["citation_identity_set_sha256"] for o in canary["outcomes"]}) == 1
    assert canary["citation_identity_sets_equal"] == same
    assert "does not establish why" in canary["interpretation"]
