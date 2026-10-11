"""Bibliographic history survives a broader live search without biological credit."""

import copy
import gzip
import json
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import summarize_resistance_vocabulary as union  # noqa: E402


def citation(source, identifier):
    return {"source": source, "id": identifier, "title": "Reference lead"}


def record(identifier):
    names = [{"text": "Shared name", "origins": [{"kind": "CANONICAL_LABEL"}],
              "shared_with_record_ids": []}]
    return {"identifier": identifier, "label": "Shared name", "path": identifier + ".yaml",
            "sha256": "current", "standard_inchi_key": identifier + "-KEY", "class": "ANTIBACTERIAL",
            "names": names,
            "queries": union.aliases.make_queries(names, profile=union.aliases.IMMUNITY_PROFILE)}


def search(record, citations):
    current = copy.deepcopy(record)
    query = current["queries"][0]
    query.update(candidates=citations, hit_count=len(citations), status="CANDIDATES_REQUIRE_REVIEW",
                 request={"url": union.aliases.discovery.URL, "status": 200,
                          "params": union.aliases.discovery.params(query)})
    current.update(searched_queries=1, search_status="ALL_INITIAL_NAME_QUERIES_SEARCHED",
                   primary_review_status="PENDING", candidate_ids=sorted(union.citation_ids(citations)))
    return current


def write_json(path, value):
    payload = json.dumps(value).encode()
    path.write_bytes(gzip.compress(payload, mtime=0) if path.suffix == ".gz" else payload)
    return union.digest(payload)


@pytest.fixture
def inputs(tmp_path):
    records = [record("CHEBI:1"), record("CHEBI:2")]
    plan = {"records": records, "criteria": union.aliases.IMMUNITY_PROFILE.criteria,
            "corpus_sha256": "corpus"}
    plan_hash = write_json(tmp_path / "plan.json", plan)
    found = {"records": [search(r, [citation("MED", "new"), citation("PMC", "new")]) for r in records],
             "criteria": plan["criteria"], "corpus_sha256": "corpus", "plan_sha256": plan_hash,
             "summary": {"query_status": {"CANDIDATES_REQUIRE_REVIEW": 2}}}
    write_json(tmp_path / "found.json", found)
    old = {**records[0], "sha256": "historical", "candidates": [citation("MED", "old")]}
    del old["queries"]
    write_json(tmp_path / "canonical.json", {"records": [old]})
    query = "historical-query"
    historical = {"queries": [{
        "query": query, "query_key": union.digest(query.encode()), "members": records,
        "candidates": [citation("MED", "old"), citation("MED", "prefix")],
        "status": "CURSOR_CONFLICT_REQUIRES_RESTART",
        "rejected_page": {"accepted_prefix_citations": 2, "candidates": [citation("MED", "rejected")]},
    }]}
    write_json(tmp_path / "expanded.json.gz", historical)
    return tmp_path, plan, found, historical


def build(root):
    return union.build_union(root, "plan.json", "found.json", history=("canonical.json", "expanded.json.gz"))


def test_union_retains_old_prefixes_namespaces_and_shared_record_memberships(inputs):
    root, _, _, _ = inputs
    value = build(root)
    assert value["scope"] == union.SCOPE
    assert value["summary"]["records"] == 2
    assert value["summary"]["distinct_queries"] == 1
    assert value["summary"]["query_memberships"] == 2
    assert value["summary"]["union_distinct_citations"] == 4
    assert value["summary"]["union_record_citation_memberships"] == 8
    assert value["summary"]["historical_memberships_lost"] == 0
    for row in value["records"]:
        assert row["union_candidate_ids"] == ["MED:new", "MED:old", "MED:prefix", "PMC:new"]
        assert row["historical_ids_not_in_v2_initial_pages"] == ["MED:old", "MED:prefix"]
        assert row["added_vs_history_ids"] == ["MED:new", "PMC:new"]
        assert row["primary_review_status"] == "PENDING"
    assert "MED:rejected" not in json.dumps(value["records"])
    assert value["historical_inputs"][1]["sha256"] != value["historical_inputs"][1]["uncompressed_sha256"]
    assert build(root) == value


@pytest.mark.parametrize("change", ["missing", "duplicate", "identity", "record_hash", "incomplete",
                                   "query", "count", "status", "request", "summary", "namespace"])
def test_changed_or_incomplete_v2_fails_closed(inputs, change):
    root, _, found, _ = inputs
    row, query = found["records"][0], found["records"][0]["queries"][0]
    if change == "missing":
        found["records"].pop()
    elif change == "duplicate":
        found["records"].append(copy.deepcopy(row))
    elif change == "identity":
        row["standard_inchi_key"] = "wrong"
    elif change == "record_hash":
        row["sha256"] = "wrong"
    elif change == "incomplete":
        row["search_status"] = "PARTIAL"
    elif change == "query":
        query["query"] = "altered"
    elif change == "count":
        query["hit_count"] = True
    elif change == "status":
        query["status"] = "CURSOR_TRAVERSAL_COMPLETE"
    elif change == "request":
        query["request"]["params"]["synonym"] = "true"
    elif change == "summary":
        row["candidate_ids"] = ["MED:new"]
    else:
        query["candidates"][0]["source"] = ""
    write_json(root / "found.json", found)
    with pytest.raises(ValueError):
        build(root)


def test_changed_plan_hash_and_shared_query_response_are_rejected(inputs):
    root, _, found, _ = inputs
    original = found["plan_sha256"]
    found["plan_sha256"] = "changed"
    write_json(root / "found.json", found)
    with pytest.raises(ValueError, match="checksum"):
        build(root)
    found["plan_sha256"] = original
    found["records"][1]["queries"][0]["request"]["sha256"] = "different-response"
    write_json(root / "found.json", found)
    with pytest.raises(ValueError, match="shared query"):
        build(root)


def test_real_response_url_can_include_its_encoded_query_string(inputs):
    root, _, found, _ = inputs
    for row in found["records"]:
        request = row["queries"][0]["request"]
        request["url"] += "?" + urlencode(request["params"])
    write_json(root / "found.json", found)
    assert build(root)["summary"]["records"] == 2


@pytest.mark.parametrize("change", ["duplicate_query", "query_key", "compound", "unknown_record",
                                   "duplicate_citation", "unexpected_content", "rejected_prefix"])
def test_historical_identity_corruption_is_not_hidden_by_union(inputs, change):
    root, _, _, historical = inputs
    query = historical["queries"][0]
    if change == "duplicate_query":
        historical["queries"].append(copy.deepcopy(query))
    elif change == "query_key":
        query["query_key"] = "changed"
    elif change == "compound":
        query["members"][0]["standard_inchi_key"] = "wrong"
    elif change == "unknown_record":
        query["members"][0]["identifier"] = "unknown"
    elif change == "duplicate_citation":
        query["candidates"].append(copy.deepcopy(query["candidates"][0]))
    elif change == "unexpected_content":
        query["candidates"][0]["abstractText"] = "not citation metadata"
    else:
        query["rejected_page"]["accepted_prefix_citations"] = 0
    write_json(root / "expanded.json.gz", historical)
    with pytest.raises(ValueError):
        build(root)


def test_truncation_is_not_reported_as_complete_traversal(inputs):
    root, _, found, _ = inputs
    citations = [citation("MED", str(i)) for i in range(100)]
    for row in found["records"]:
        row["queries"][0].update(candidates=citations, hit_count=101, status="TRUNCATED_REFINEMENT_REQUIRED")
        row["candidate_ids"] = sorted(union.citation_ids(citations))
    found["summary"]["query_status"] = {"TRUNCATED_REFINEMENT_REQUIRED": 2}
    write_json(root / "found.json", found)
    result = build(root)
    assert result["summary"]["query_status"] == {"TRUNCATED_REFINEMENT_REQUIRED": 2}
    assert all(r["primary_review_status"] == "PENDING" for r in result["records"])
