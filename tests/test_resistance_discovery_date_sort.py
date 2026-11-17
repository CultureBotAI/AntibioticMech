"""Sorted citation recovery must not promote reference leads to biological evidence."""

import csv
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SORT = "P_PDATE_D desc"


def pinned(value):
    payload = (ROOT / value["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == value["sha256"]
    return payload


@pytest.fixture(scope="module")
def checkpoint():
    dossier = json.loads((ROOT / "research/2026-10-09-resistance-discovery-date-sort.json").read_bytes())
    delta = json.loads(gzip.decompress(pinned(dossier["delta_candidate_index"])))
    parent = json.loads(pinned(dossier["parent_descriptor"]))
    previous = json.loads(gzip.decompress(pinned(parent["delta_candidate_index"])))
    plan = json.loads(pinned(dossier["plan"]))
    return dossier, delta, parent, previous, plan


def test_only_the_five_conflicted_whole_chains_are_replaced(checkpoint):
    dossier, delta, parent, previous, plan = checkpoint
    expected = {q["query_key"] for q in plan["queries"]}
    reused = set(dossier["reused_complete_query_keys"])
    replaced = {q["query_key"] for q in delta["queries"]}
    assert len(expected) == 611 and len(reused) == 606 and len(replaced) == len(delta["queries"]) == 5
    assert reused.isdisjoint(replaced) and reused | replaced == expected
    assert replaced == {q["query_key"] for q in previous["queries"]
                        if q["status"] == "CURSOR_CONFLICT_REQUIRES_RESTART"}
    assert reused == set(parent["reused_complete_query_keys"]) | {
        q["query_key"] for q in previous["queries"] if q["status"] == "CURSOR_TRAVERSAL_COMPLETE"
    }
    assert dossier["parent_descriptor"]["path"] == "research/2026-10-09-resistance-discovery-query-local.json"


def test_query_text_names_origins_and_chemical_memberships_are_preserved(checkpoint):
    dossier, delta, _, _, plan = checkpoint
    expected = {q["query_key"]: q for q in plan["queries"]}
    assert dossier["query_text_changed"] is False
    assert dossier["request_parameter_changes"] == {"sort": {"from": None, "to": SORT}}
    for chain in delta["queries"]:
        original = expected[chain["query_key"]]
        assert chain["query"] == original["query"] and chain["members"] == original["members"]
        assert chain["requested_sort"] == SORT
        assert hashlib.sha256(chain["query"].encode()).hexdigest() == chain["query_key"]
    assert delta["plan_sha256"] == dossier["plan"]["sha256"]
    assert delta["historical_query_census_sha256"] == plan["corpus_sha256"]


def test_cursor_parameters_and_page_pins_keep_attempts_separate(checkpoint):
    _, delta, _, _, _ = checkpoint
    paths = set()
    for chain in delta["queries"]:
        cursor = "*"
        for page in chain["pages"]:
            assert page["request"] == {
                "query": chain["query"], "format": "json", "resultType": "lite", "pageSize": 1000,
                "cursorMark": cursor, "synonym": "false", "sort": SORT,
            }
            assert page["cache"]["path"] not in paths
            paths.add(page["cache"]["path"])
            assert "expansion-date-sort-20261009/epmc-discovery-" in page["cache"]["path"]
            assert len(page["cache"]["sha256"]) == len(page["response_body_sha256"]) == 64
            assert page["reported_count"] == chain["hit_count"]
            assert page["api_version"] == chain["api_version"]
            cursor = page["next_cursor"]


def test_completed_chains_have_unique_citations_equal_to_the_reported_count(checkpoint):
    _, delta, _, _, _ = checkpoint
    for chain in delta["queries"]:
        ids = [(c["source"], c["id"]) for c in chain["candidates"]]
        assert len(ids) == len(set(ids)) == sum(p["returned_citations"] for p in chain["pages"])
        assert chain["status"] in {"CURSOR_TRAVERSAL_COMPLETE", "CURSOR_CONFLICT_REQUIRES_RESTART"}
        if chain["status"] == "CURSOR_TRAVERSAL_COMPLETE":
            assert len(ids) == chain["hit_count"] and chain["next_cursor"] is None
            assert "rejected_page" not in chain
        else:
            assert chain["rejected_page"]["accepted_prefix_citations"] == len(ids)


def test_summary_replaces_prefixes_instead_of_adding_duplicate_histories(checkpoint):
    dossier, delta, parent, previous, _ = checkpoint
    old = {q["query_key"]: q for q in previous["queries"]}
    retained = parent["summary"]["retained_query_citation_memberships"] - sum(
        len(old[q["query_key"]]["candidates"]) for q in delta["queries"]
    ) + sum(len(q["candidates"]) for q in delta["queries"])
    assert dossier["summary"]["retained_query_citation_memberships"] == retained
    counts = Counter(q["status"] for q in delta["queries"])
    assert dict(counts) == dossier["retry_status"]
    counts["CURSOR_TRAVERSAL_COMPLETE"] += 606
    assert dict(counts) == dossier["summary"]["query_status"]
    assert dossier["summary"]["corpus_records"] == 2939
    assert dossier["summary"]["records_with_truncated_queries"] == 384
    assert dossier["summary"]["query_record_memberships"] == 612


def test_each_transition_counts_added_and_missing_previous_candidates(checkpoint):
    dossier, delta, _, previous, _ = checkpoint
    old = {q["query_key"]: q for q in previous["queries"]}
    transitions = {t["query_key"]: t for t in dossier["retry_transitions"]}
    assert len(transitions) == len(dossier["retry_transitions"]) == 5
    for query in delta["queries"]:
        transition = transitions[query["query_key"]]
        before = {(c["source"], c["id"]) for c in old[query["query_key"]]["candidates"]}
        after = {(c["source"], c["id"]) for c in query["candidates"]}
        assert transition["previous_retained_citations"] == len(before)
        assert transition["new_retained_citations"] == len(after)
        assert transition["added_vs_previous_valid_prefix"] == len(after - before)
        assert transition["previous_prefix_ids_not_in_selected_chain"] == len(before - after)
        assert transition["new_status"] == query["status"]


def test_current_name_bridge_does_not_rewrite_historical_record_hashes(checkpoint):
    dossier, delta, _, _, plan = checkpoint
    bridge = dossier["name_bridge_summary"]
    assert bridge["records_verified"] == dossier["record_hashes_verified"] == 2939
    assert bridge["names_verified"] == 16030 and bridge["queries_verified"] == 7469
    assert bridge["record_hashes_changed_since_historical_plan"] == 22
    assert bridge["historical_name_plan"]["sha256"] == plan["alias_plan_sha256"]
    assert bridge["historical_record_pins_rewritten"] is False
    assert bridge["current_census"] == dossier["current_census"]
    assert bridge["current_census"]["sha256"] != delta["historical_query_census_sha256"]
    assert set(bridge["unchanged_projection_fields"]) == {
        "identifier", "label", "path", "standard_inchi_key", "class", "names", "queries",
    }
    assert dossier["record_path_search_includes_ignored"] is True


def test_canary_agreement_does_not_claim_sorting_caused_recovery(checkpoint):
    dossier, delta, _, _, _ = checkpoint
    canary = dossier["ordering_canary"]
    chain, = [q for q in delta["queries"] if q["query_key"] == canary["query_key"]]
    assert canary["default_pages"] == canary["date_sorted_pages"] == len(chain["pages"]) == 7
    assert canary["unique_citations_per_order"] == chain["hit_count"] == 6611
    assert canary["citation_identity_sets_equal"] is True
    assert "no cause" in canary["interpretation"]
    pages = sum(len(q["pages"]) + ("rejected_page" in q) for q in delta["queries"])
    assert dossier["date_sorted_pages"] == pages
    assert dossier["fresh_cached_responses"] == pages + 7
    assert pages - 7 <= dossier["max_batch_pages"] == 100
    assert dossier["stored_response_count_excludes_transient_failed_attempts"] is True


def test_ledger_retains_every_original_query_record_membership(checkpoint):
    dossier, delta, _, _, plan = checkpoint
    rows = list(csv.DictReader(pinned(dossier["ledger"]).decode().splitlines(), delimiter="\t"))
    assert len(rows) == 612
    assert [(r["query_key"], r["identifier"], r["query_id"]) for r in rows] == [
        (q["query_key"], m["identifier"], m["query_id"]) for q in plan["queries"] for m in q["members"]
    ]
    replaced = {q["query_key"]: q for q in delta["queries"]}
    for row in rows:
        assert row["primary_review_status"] == "PENDING"
        if row["query_key"] in replaced:
            chain = replaced[row["query_key"]]
            assert row["requested_sort"] == SORT and row["status"] == chain["status"]
            assert int(row["retained_citations"]) == len(chain["candidates"])
        else:
            assert row["requested_sort"] == "" and row["status"] == "CURSOR_TRAVERSAL_COMPLETE"


def test_short_aliases_remain_ambiguous_not_verified_chemical_matches(checkpoint):
    dossier, delta, _, _, _ = checkpoint
    chain, = [q for q in delta["queries"] if any(m["identifier"] == "CHEBI:17909" for m in q["members"])]
    member, = chain["members"]
    assert [n["text"] for n in member["names"]] == ["S", "Sn", "Sulfur", "sulphur"]
    assert "Short aliases and stop words" in " ".join(dossier["limitations"])
    assert dossier["primary_review_status"] == "PENDING"


def test_lossless_citation_only_export_and_scope(checkpoint):
    dossier, delta, _, _, _ = checkpoint
    artifact = dossier["delta_candidate_index"]
    stored = pinned(artifact)
    expanded = gzip.decompress(stored)
    assert stored[4:8] == b"\x00\x00\x00\x00"
    assert len(stored) == artifact["stored_bytes"] and len(expanded) == artifact["uncompressed_bytes"]
    assert hashlib.sha256(expanded).hexdigest() == artifact["uncompressed_sha256"]
    fields = {"id", "source", "pmid", "pmcid", "doi", "title", "pubYear", "pubType"}
    assert all(set(c) <= fields for q in delta["queries"] for c in q["candidates"])
    assert dossier["scope"] == delta["scope"] == (
        "CITATION_DISCOVERY_ONLY; NO_COMPOUND_ALLELE_OR_AST_ASSIGNMENTS"
    )
    assert dossier["biological_record_changes"] == dossier["curation_events_added"] == 0
    assert all(q["primary_review_status"] == "PENDING" for q in delta["queries"])
    assert "no NCBI request" in dossier["network"]
    assert all(not {"body", "headers"} & set(p) for q in delta["queries"] for p in q["pages"])
    complete = dossier["summary"]["query_status"] == {"CURSOR_TRAVERSAL_COMPLETE": 611}
    assert dossier["status"] == ("PLANNED_CURSOR_TRAVERSALS_COMPLETE_NOT_PRIMARY_REVIEW" if complete
                                 else "PARTIAL_CITATION_DISCOVERY_NOT_PRIMARY_REVIEW")


def test_history_union_is_not_a_validated_search_snapshot(checkpoint):
    dossier, _, parent, _, _ = checkpoint
    union = dossier["history_union"]
    assert union["previous_distinct_citations"] == parent["summary"]["unique_retained_citations"]
    assert union["selected_distinct_citations"] == dossier["summary"]["unique_retained_citations"]
    assert union["union_distinct_citations"] == (
        union["previous_distinct_citations"] + union["selected_ids_absent_from_previous_index"]
    ) == union["selected_distinct_citations"] + union["previous_ids_absent_from_selected_index"]
    assert "NOT_ONE_VALIDATED_CURSOR_CHAIN" in union["scope"]
