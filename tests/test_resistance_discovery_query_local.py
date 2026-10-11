"""Whole-chain retrieval recovery must preserve earlier evidence and review scope."""

import csv
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def pinned_bytes(pin):
    payload = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
    return payload


@pytest.fixture(scope="module")
def checkpoint():
    dossier = json.loads((ROOT / "research/2026-10-09-resistance-discovery-query-local.json").read_bytes())
    delta = json.loads(gzip.decompress(pinned_bytes(dossier["delta_candidate_index"])))
    parent = json.loads(pinned_bytes(dossier["parent_descriptor"]))
    previous_delta = json.loads(gzip.decompress(pinned_bytes(parent["delta_candidate_index"])))
    return dossier, delta, parent, previous_delta


def test_query_local_delta_preserves_the_exact_plan_and_every_membership(checkpoint):
    dossier, delta, parent, previous = checkpoint
    plan = json.loads(pinned_bytes(dossier["plan"]))
    expected = {q["query_key"]: q for q in plan["queries"]}
    reused = set(dossier["reused_complete_query_keys"])
    replaced = {q["query_key"] for q in delta["queries"]}
    assert len(reused) == 538 and len(replaced) == 73
    assert len(delta["queries"]) == len(replaced)
    assert reused.isdisjoint(replaced) and reused | replaced == set(expected)
    assert reused == set(parent["reused_complete_query_keys"]) | {
        q["query_key"] for q in previous["queries"] if q["status"] == "CURSOR_TRAVERSAL_COMPLETE"
    }
    assert replaced == {q["query_key"] for q in previous["queries"] if "rejected_page" in q}
    assert dossier["corpus_sha256"] == delta["corpus_sha256"] == plan["corpus_sha256"]
    assert delta["plan_sha256"] == dossier["plan"]["sha256"] == parent["plan"]["sha256"]
    for q in delta["queries"]:
        assert {k: q[k] for k in expected[q["query_key"]]} == expected[q["query_key"]]
    assert dossier["summary"]["corpus_records"] == plan["corpus_records"] == 2939
    assert len(expected) == 611
    assert sum(len(q["members"]) for q in expected.values()) == 612


def test_canary_is_explicitly_reused_as_one_complete_default_order_chain(checkpoint):
    dossier, delta, parent, _ = checkpoint
    key = dossier["reused_canary_query_key"]
    assert key == parent["ordering_canary"]["query_key"]
    query, = [q for q in delta["queries"] if q["query_key"] == key]
    outcome, = [o for o in parent["ordering_canary"]["outcomes"] if o["requested_sort"] is None]
    assert query["status"] == "CURSOR_TRAVERSAL_COMPLETE"
    assert len(query["pages"]) == dossier["complete_canary_pages_reused"] == 3
    assert query["hit_count"] == len(query["candidates"]) == outcome["hit_count"] == 2503
    assert len(query["pages"]) == len(outcome["responses"])
    for page, original in zip(query["pages"], outcome["responses"], strict=True):
        assert page["cache"] == Path(original["path"]).name
        assert page["cache_sha256"] == original["sha256"]
        assert page["request"]["params"] == original["params"]
        assert "sort" not in page["request"]["params"]


def test_summary_counts_whole_selected_chains_without_double_counting_prefixes(checkpoint):
    dossier, delta, parent, previous = checkpoint
    retained = parent["summary"]["retained_query_citation_memberships"] - sum(
        len(q["candidates"]) for q in previous["queries"] if "rejected_page" in q
    ) + sum(len(q["candidates"]) for q in delta["queries"])
    assert dossier["summary"]["retained_query_citation_memberships"] == retained
    statuses = Counter(q["status"] for q in delta["queries"])
    assert dict(statuses) == dossier["retry_status"]
    statuses["CURSOR_TRAVERSAL_COMPLETE"] += 538
    assert dict(statuses) == dossier["summary"]["query_status"]
    pages = sum(len(q["pages"]) for q in delta["queries"])
    rejected = sum("rejected_page" in q for q in delta["queries"])
    assert dossier["completed_parent_pages_reused"] == 704
    assert dossier["summary"]["cached_pages"] == pages + 704
    assert dossier["summary"]["rejected_cached_pages"] == rejected
    assert dossier["fresh_responses"] == pages + rejected - 3
    assert dossier["fresh_responses"] <= dossier["max_new_pages"] == 500


def test_fresh_queries_remain_distinct_from_canary_and_primary_review(checkpoint):
    dossier, delta, _, previous = checkpoint
    before = {q["query_key"]: q for q in previous["queries"]}
    transitions = {t["query_key"]: t for t in dossier["retry_transitions"]}
    assert len(transitions) == len(dossier["retry_transitions"]) == 73
    for q in delta["queries"]:
        key = q["query_key"]
        transition = transitions[key]
        old_ids = {(c["source"], c["id"]) for c in before[key]["candidates"]}
        ids = [(c["source"], c["id"]) for c in q["candidates"]]
        assert len(ids) == len(set(ids)) == sum(p["retained_citations"] for p in q["pages"])
        assert transition["new_retained_citations"] == len(ids)
        assert transition["previous_retained_citations"] == len(old_ids)
        assert transition["added_vs_previous_valid_prefix"] == len(set(ids) - old_ids)
        assert transition["previous_prefix_ids_not_in_selected_chain"] == len(old_ids - set(ids))
        assert transition["previous_status"] == before[key]["status"] == "CURSOR_CONFLICT_REQUIRES_RESTART"
        assert transition["new_status"] == q["status"]
        assert transition["retrieval_origin"] == (
            "REUSED_COMPLETE_CANARY" if key == dossier["reused_canary_query_key"]
            else "FRESH_QUERY_LOCAL_CHAIN"
        )
        if q["pages"]:
            assert q["pages"][0]["request"]["params"]["cursorMark"] == "*"
        if "rejected_page" in q:
            assert q["status"] == "CURSOR_CONFLICT_REQUIRES_RESTART"
            assert q["rejected_page"]["accepted_prefix_citations"] == len(ids)
        if q["status"] == "CURSOR_TRAVERSAL_COMPLETE":
            assert len(ids) == q["hit_count"] and q["next_cursor"] is None and "rejected_page" not in q
    assert dossier["observed_query_order"] == [
        q["query_key"] for q in delta["queries"] if q["query_key"] != dossier["reused_canary_query_key"]
        and (q["pages"] or "rejected_page" in q)
    ]


def test_public_ledger_matches_every_plan_membership_and_selected_status(checkpoint):
    dossier, delta, _, _ = checkpoint
    plan = json.loads(pinned_bytes(dossier["plan"]))
    rows = list(csv.DictReader(pinned_bytes(dossier["ledger"]).decode().splitlines(), delimiter="\t"))
    assert len(rows) == 612
    assert [(r["query_key"], r["identifier"], r["query_id"]) for r in rows] == [
        (q["query_key"], m["identifier"], m["query_id"]) for q in plan["queries"] for m in q["members"]
    ]
    statuses = {k: "CURSOR_TRAVERSAL_COMPLETE" for k in dossier["reused_complete_query_keys"]}
    statuses.update({q["query_key"]: q["status"] for q in delta["queries"]})
    assert all(row["status"] == statuses[row["query_key"]] and row["primary_review_status"] == "PENDING"
               for row in rows)


def test_lossless_export_and_history_union_do_not_erase_earlier_candidates(checkpoint):
    dossier, delta, parent, _ = checkpoint
    artifact = dossier["delta_candidate_index"]
    stored = pinned_bytes(artifact)
    expanded = gzip.decompress(stored)
    assert hashlib.sha256(expanded).hexdigest() == artifact["uncompressed_sha256"]
    assert len(stored) == artifact["stored_bytes"] and len(expanded) == artifact["uncompressed_bytes"]
    assert stored[4:8] == b"\x00\x00\x00\x00"
    assert delta["manifest_sha256"] == dossier["manifest"]["sha256"]
    union = dossier["history_union"]
    assert union["previous_union_distinct_citations"] == (
        parent["expansion_history_union"]["union_distinct_citations"]
    )
    assert union["selected_index_distinct_citations"] == dossier["summary"]["unique_retained_citations"]
    assert union["union_distinct_citations"] == (
        union["previous_union_distinct_citations"] + union["selected_ids_absent_from_previous_union"]
    )
    assert union["union_distinct_citations"] == (
        union["selected_index_distinct_citations"] + union["previous_union_ids_absent_from_selected_index"]
    )
    assert "NOT_ONE_VALIDATED_CURSOR_CHAIN" in union["scope"]


def test_citation_recovery_is_not_biological_curation_or_completed_primary_review(checkpoint):
    dossier, delta, _, _ = checkpoint
    assert dossier["scope"] == delta["scope"] == (
        "CITATION_DISCOVERY_ONLY; NO_COMPOUND_ALLELE_OR_AST_ASSIGNMENTS"
    )
    assert dossier["primary_review_status"] == "PENDING"
    assert all(q["primary_review_status"] == "PENDING" for q in delta["queries"])
    assert dossier["biological_record_changes"] == dossier["curation_events_added"] == 0
    assert dossier["record_hashes_verified"] == 2939 and dossier["record_path_search_includes_ignored"]
    assert "no NCBI request" in dossier["network"]
    assert dossier["traversal_order"] == "query-local" and not dossier["queries_and_parameters_changed"]
    assert "Do not combine pages within a query" in dossier["composition"]
    fields = {"id", "source", "pmid", "pmcid", "doi", "title", "pubYear", "pubType"}
    assert all(set(c) <= fields for q in delta["queries"] for c in q["candidates"])
    complete = dossier["summary"]["query_status"] == {"CURSOR_TRAVERSAL_COMPLETE": 611}
    assert dossier["status"] == ("PLANNED_CURSOR_TRAVERSALS_COMPLETE_NOT_PRIMARY_REVIEW" if complete
                                 else "PARTIAL_CITATION_DISCOVERY_NOT_PRIMARY_REVIEW")


def test_short_alias_warning_retains_the_source_names_without_claiming_relevant_hits(checkpoint):
    dossier, delta, _, _ = checkpoint
    warning = dossier["short_alias_query_warning"]
    query, = [q for q in delta["queries"] if q["query_key"] == warning["query_key"]]
    member, = [m for m in query["members"] if m["identifier"] == warning["record_identifier"]]
    assert member["identifier"] == "CHEBI:17909" and member["query_id"] == "1"
    assert warning["source_aliases"] == member["names"]
    assert [n["text"] for n in member["names"]] == ["S", "Sn", "Sulfur", "sulphur"]
    assert warning["selected_status"] == query["status"]
    assert warning["selected_hit_count"] == query["hit_count"]
    assert "not sulfur-specific resistance evidence" in warning["interpretation"]
    assert "No estimate of relevant hits" in warning["interpretation"]
