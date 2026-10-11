"""Cursor expansion must not promote partial searches to biological findings."""

import csv
import gzip
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import expand_resistance_discovery as expansion  # noqa: E402

discovery = expansion.discovery
common = expansion.common


def test_compressed_export_is_lossless_deterministic_and_pins_both_encodings(tmp_path):
    source, first, second = (tmp_path / name for name in ("source.json", "first.gz", "second.gz"))
    payload = b'{"queries": [{"status": "PENDING", "members": ["CHEBI:1", "CHEBI:2"]}]}\n'
    source.write_bytes(payload)
    metadata = expansion.write_compressed_candidate_export(source, first)
    assert metadata == expansion.write_compressed_candidate_export(source, second)
    assert first.read_bytes() == second.read_bytes()
    assert gzip.decompress(first.read_bytes()) == source.read_bytes() == payload
    assert metadata == {
        "encoding": "gzip", "sha256": common.digest(first.read_bytes()),
        "stored_bytes": first.stat().st_size, "uncompressed_sha256": common.digest(payload),
        "uncompressed_bytes": len(payload),
    }
    assert first.read_bytes()[4:8] == b"\x00\x00\x00\x00"
    assert not first.read_bytes()[3] & 8


def test_compressed_export_cannot_overwrite_its_source(tmp_path):
    source = tmp_path / "source.json"
    source.write_bytes(b"{}\n")
    with pytest.raises(ValueError, match="must not replace its source"):
        expansion.write_compressed_candidate_export(source, source)
    assert source.read_bytes() == b"{}\n"


def test_compressed_export_detects_source_change_without_clobbering_target(tmp_path, monkeypatch):
    source, target = tmp_path / "source.json", tmp_path / "target.gz"
    source.write_bytes(b"{}\n")
    target.write_bytes(b"previous verified export")
    original = expansion.gzip.decompress

    def mutate(stored):
        source.write_bytes(b"changed")
        return original(stored)

    monkeypatch.setattr(expansion.gzip, "decompress", mutate)
    with pytest.raises(ValueError, match="source changed"):
        expansion.write_compressed_candidate_export(source, target)
    assert target.read_bytes() == b"previous verified export"


def test_compressed_export_rejects_round_trip_mismatch(tmp_path, monkeypatch):
    source, target = tmp_path / "source.json", tmp_path / "target.gz"
    source.write_bytes(b"{}\n")
    monkeypatch.setattr(expansion.gzip, "decompress", lambda _: b"different")
    with pytest.raises(ValueError, match="byte-for-byte"):
        expansion.write_compressed_candidate_export(source, target)
    assert not target.exists()


def test_compressed_export_rejects_corrupt_temporary_file_and_preserves_previous(tmp_path, monkeypatch):
    source, target = tmp_path / "source.json", tmp_path / "target.gz"
    source.write_bytes(b"{}\n")
    target.write_bytes(b"previous verified export")
    original = Path.write_bytes

    def corrupt(path, data):
        return original(path, b"corrupt" if path.parent.name.startswith(".candidate-export-") else data)

    monkeypatch.setattr(Path, "write_bytes", corrupt)
    with pytest.raises(ValueError, match="changed before publication"):
        expansion.write_compressed_candidate_export(source, target)
    assert target.read_bytes() == b"previous verified export"
    assert not list(tmp_path.glob(".candidate-export-*"))


def response(params, count=1002, offset=0):
    rows = [{"source": "MED", "id": str(i), "title": "Citation only"}
            for i in range(offset, min(offset + params["pageSize"], count))]
    body = {
        "version": "6.9", "hitCount": count,
        "request": {"queryString": params["query"], "resultType": "lite",
                    "pageSize": params["pageSize"], "cursorMark": params["cursorMark"], "synonym": False},
        "resultList": {"result": rows},
        "nextCursorMark": "after-" + str(offset + len(rows)),
    }
    raw = {"url": discovery.URL, "params": params, "status": 200, "headers": {},
           "retrieved_at": "2026-10-08T00:00:00+00:00"}
    return repack(raw, body)


def repack(raw, body):
    raw["body"] = json.dumps(body)
    raw["sha256"] = common.digest(raw["body"].encode())
    return raw


def cache(params, count=1002, offset=0):
    raw = response(params, count, offset)
    common.write(discovery.cache_path(params).name, raw)
    return raw


@pytest.fixture
def cohort(tmp_path, monkeypatch):
    out, root = tmp_path / "cache", tmp_path / "root"
    out.mkdir()
    (root / "data/antibiotics").mkdir(parents=True)
    monkeypatch.setattr(common, "OUT", out)
    monkeypatch.setattr(common, "ALLOW_NETWORK", False)
    records = []
    for i, (label, cls) in enumerate([("Shared", "A"), ("Second", "B"), ("Shared", "A"), ("Small", "C")]):
        path = root / f"data/antibiotics/{i}.yaml"
        path.write_text(f"identifier: CHEBI:{i}\n")
        record = {"identifier": f"CHEBI:{i}", "label": label, "class": cls,
                  "path": str(path.relative_to(root)), "sha256": common.digest(path.read_bytes()),
                  "standard_inchi_key": str(i), "names": [{"text": label, "origins": []}],
                  "queries": [{"query": discovery.query(label), "query_id": "0",
                               "kind": "CANONICAL", "name_indices": [0]}]}
        records.append(record)
        cache(discovery.params(record["queries"][0]), count=5 if label == "Small" else 1002)
    common.write("corpus.json", {"records": records})
    aliases_plan = {"records": records, "corpus_sha256": common.digest((out / "corpus.json").read_bytes())}
    common.write(expansion.aliases.PLAN, aliases_plan)
    monkeypatch.setattr(expansion.aliases, "load_plan", lambda _: (
        aliases_plan, common.digest((out / expansion.aliases.PLAN).read_bytes()),
    ))
    expansion.plan(root)
    return root, out, json.loads((out / expansion.PLAN).read_bytes())


def mock_network(monkeypatch, modify_response=None):
    calls, closed = [], []
    monkeypatch.setattr(common, "ALLOW_NETWORK", True)
    monkeypatch.setattr(discovery.time, "sleep", lambda _: None)

    class Session:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            closed.append(self)

        def get(self, url, **kwargs):
            assert url == discovery.URL
            assert kwargs["allow_redirects"] is False
            params = kwargs["params"]
            calls.append(params)
            offset = 0 if params["cursorMark"] == "*" else 1000
            raw = response(params, offset=offset)
            if modify_response:
                raw = modify_response(params, raw)
            return SimpleNamespace(url=url, status_code=200, headers={},
                                   content=raw["body"].encode(), text=raw["body"])

    monkeypatch.setattr(discovery.requests, "Session", Session)
    return calls, closed


def test_plan_deduplicates_queries_without_losing_record_or_name_context(cohort):
    _, _, plan = cohort
    assert plan["corpus_records"] == 4
    assert len(plan["queries"]) == 2
    assert [m["identifier"] for m in plan["queries"][0]["members"]] == ["CHEBI:0", "CHEBI:2"]
    assert plan["queries"][0]["members"][1]["names"][0]["text"] == "Shared"
    query = plan["queries"][0]
    assert expansion.parameters(query)["pageSize"] == 1000
    assert discovery.params(query)["pageSize"] == 100
    assert discovery.cache_path(expansion.parameters(query)) != discovery.cache_path(discovery.params(query))


def test_eligible_queries_are_rebalanced_after_filtering(cohort, monkeypatch):
    root, out, _ = cohort
    initial = json.loads((out / expansion.aliases.PLAN).read_bytes())
    initial["records"] = [initial["records"][i] for i in (1, 0, 2, 3)]
    common.write(expansion.aliases.PLAN, initial)
    monkeypatch.setattr(expansion.aliases, "load_plan", lambda _: (
        initial, common.digest((out / expansion.aliases.PLAN).read_bytes()),
    ))
    result = expansion.build_plan(root)
    assert [q["members"][0]["class"] for q in result["queries"]] == ["A", "B"]


def test_bounded_resume_is_breadth_first_shared_query_reused_and_offline_idempotent(cohort, monkeypatch):
    root, out, _ = cohort
    calls, closed = mock_network(monkeypatch)
    expansion.search(root, 1, [])
    assert len(calls) == 1
    expansion.search(root, 2, [])
    assert len(calls) == 3
    assert calls[0]["query"] != calls[1]["query"]
    assert calls[0]["query"] == calls[2]["query"]
    assert [p["cursorMark"] for p in calls] == ["*", "*", "after-1000"]
    expansion.search(root, 1, [])
    assert len(calls) == 4 and len(closed) == 3
    before = {p.name: p.read_bytes() for p in out.glob("epmc-*.json")}
    monkeypatch.setattr(common, "ALLOW_NETWORK", False)
    expansion.search(root, 10, [])
    expansion.analyze(root)
    result = json.loads((out / expansion.CANDIDATES).read_bytes())
    assert result["summary"]["query_status"] == {"CURSOR_TRAVERSAL_COMPLETE": 2}
    assert result["summary"]["query_record_memberships"] == 3
    assert result["summary"]["unique_retained_citations"] == 1002
    assert all(q["primary_review_status"] == "PENDING" for q in result["queries"])
    assert before == {p.name: p.read_bytes() for p in out.glob("epmc-*.json")}
    assert len(calls) == 4
    with (out / expansion.LEDGER).open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(rows) == 3
    assert all(r["added_vs_original_query_page"] == "902" for r in rows)


def test_not_started_and_partial_are_not_complete_or_no_hits(cohort):
    root, out, plan = cohort
    expansion.analyze(root)
    result = json.loads((out / expansion.CANDIDATES).read_bytes())
    assert result["summary"]["query_status"] == {"NOT_STARTED": 2}
    assert result["queries"][0]["hit_count"] is None
    with (out / expansion.LEDGER).open() as handle:
        assert next(csv.DictReader(handle, delimiter="\t"))["added_vs_original_query_page"] == ""
    query = plan["queries"][0]
    cache(expansion.parameters(query))
    state = expansion.analyze_query(query)
    assert state["status"] == "PARTIAL_CURSOR_TRAVERSAL"
    assert len(state["candidates"]) == 1000


def test_query_local_order_is_bounded_resumable_shared_and_offline_idempotent(cohort, monkeypatch):
    root, out, plan = cohort
    calls, _ = mock_network(monkeypatch)
    expansion.search(root, 1, [], traversal_order="query-local")
    expansion.search(root, 2, [], traversal_order="query-local")
    assert len(calls) == 3
    assert calls[0]["query"] == calls[1]["query"] != calls[2]["query"]
    assert [p["cursorMark"] for p in calls] == ["*", "after-1000", "*"]
    assert calls == [expansion.parameters(plan["queries"][0]),
                     expansion.parameters(plan["queries"][0], "after-1000"),
                     expansion.parameters(plan["queries"][1])]
    assert expansion.analyze_query(plan["queries"][0])["status"] == "CURSOR_TRAVERSAL_COMPLETE"
    assert expansion.analyze_query(plan["queries"][1])["status"] == "PARTIAL_CURSOR_TRAVERSAL"
    expansion.search(root, 1, ["CHEBI:2"], traversal_order="query-local")
    assert len(calls) == 3
    expansion.search(root, 1, [], traversal_order="query-local")
    assert len(calls) == 4
    before = {p.name: p.read_bytes() for p in out.glob("epmc-*.json")}
    monkeypatch.setattr(common, "ALLOW_NETWORK", False)
    expansion.search(root, 10, [], traversal_order="query-local")
    expansion.analyze(root)
    result = json.loads((out / expansion.CANDIDATES).read_bytes())
    assert result["summary"]["query_status"] == {"CURSOR_TRAVERSAL_COMPLETE": 2}
    assert result["summary"]["query_record_memberships"] == 3
    assert all(q["primary_review_status"] == "PENDING" for q in result["queries"])
    assert before == {p.name: p.read_bytes() for p in out.glob("epmc-*.json")}
    assert len(calls) == 4


@pytest.mark.parametrize("order", ["", "depth-first", None, [], True])
def test_invalid_traversal_order_cannot_request(cohort, monkeypatch, order):
    root, _, _ = cohort
    calls, _ = mock_network(monkeypatch)
    with pytest.raises(ValueError, match="invalid traversal order"):
        expansion.search(root, 1, [], traversal_order=order)
    assert not calls


def test_new_first_page_count_drift_is_visible_without_mixing_old_results(cohort):
    _, _, plan = cohort
    query = plan["queries"][0]
    cache(expansion.parameters(query), count=0)
    state = expansion.analyze_query(query)
    assert state["status"] == "CURSOR_TRAVERSAL_COMPLETE"
    assert state["hit_count_delta"] == -1002 and state["candidates"] == []
    assert state["primary_review_status"] == "PENDING"


@pytest.mark.parametrize("change", ["duplicate", "count", "version", "query", "cursor", "short",
                                   "abstract", "cycle", "checksum", "origin", "identifier", "no_version"])
@pytest.mark.parametrize("allow_conflicts", [False, True])
def test_invalid_chains_fail_closed(cohort, change, allow_conflicts):
    _, _, plan = cohort
    query = plan["queries"][0]
    cache(expansion.parameters(query))
    params = expansion.parameters(query, "after-1000")
    raw = response(params, offset=1000)
    body = json.loads(raw["body"])
    if change == "duplicate":
        body["resultList"]["result"][0]["id"] = "0"
    elif change == "count":
        body["hitCount"] = 1003
        body["resultList"]["result"].append({"source": "MED", "id": "1002"})
    elif change == "version":
        body["version"] = "7.0"
    elif change == "no_version":
        body["version"] = None
    elif change in ("query", "cursor"):
        body["request"]["queryString" if change == "query" else "cursorMark"] = "different"
    elif change == "short":
        body["resultList"]["result"].pop()
    elif change == "abstract":
        body["resultList"]["result"][0]["abstractText"] = "Must not export"
    elif change == "identifier":
        body["resultList"]["result"][0]["id"] = None
    elif change == "cycle":
        params = expansion.parameters(query)
        raw = response(params)
        body = json.loads(raw["body"])
        body["nextCursorMark"] = "*"
    repack(raw, body)
    if change == "checksum":
        raw["sha256"] = "wrong"
    elif change == "origin":
        raw["url"] = "https://example.org/search"
    common.write(discovery.cache_path(params).name, raw)
    if change in ("duplicate", "count", "version", "short") and allow_conflicts:
        state = expansion.analyze_query(query, allow_conflicts=True)
        assert state["status"] == expansion.CONFLICT_STATUS
        assert len(state["candidates"]) == 1000 and len(state["pages"]) == 1
        assert state["hit_count"] == 1002 and state["api_version"] == "6.9"
        if change == "duplicate":
            assert state["rejected_page"]["repeated_publication_ids"] == ["MED:0"]
        else:
            assert state["rejected_page"]["reason"] == (
                "CURSOR_PAGE_LENGTH_MISMATCH" if change == "short" else "CURSOR_COUNT_OR_VERSION_CHANGED"
            )
            assert state["rejected_page"]["expected_hit_count"] == 1002
            assert state["rejected_page"]["expected_returned_citations"] == 2
        return
    with pytest.raises(ValueError):
        expansion.analyze_query(query, allow_conflicts=allow_conflicts)


def cache_overlap(query):
    cache(expansion.parameters(query))
    params = expansion.parameters(query, "after-1000")
    raw = response(params, offset=1000)
    body = json.loads(raw["body"])
    # A new citation before the overlap must also be rejected, not partially appended.
    body["resultList"]["result"][-1]["id"] = "0"
    common.write(discovery.cache_path(params).name, repack(raw, body))
    return discovery.cache_path(params)


def test_conflict_export_preserves_only_valid_prefix_and_pins_entire_rejection(cohort):
    root, out, plan = cohort
    query = plan["queries"][0]
    rejected = cache_overlap(query)
    before = {p.name: p.read_bytes() for p in out.glob("epmc-*.json")}
    expansion.analyze(root)
    result = json.loads((out / expansion.CANDIDATES).read_bytes())
    state = result["queries"][0]
    assert state["status"] == expansion.CONFLICT_STATUS
    assert state["next_cursor"] == "after-1000"
    assert state["primary_review_status"] == "PENDING"
    assert len(state["pages"]) == 1 and len(state["candidates"]) == 1000
    assert "1000" not in {c["id"] for c in state["candidates"]}
    assert state["added_vs_original_query_page_ids"] == sorted(f"MED:{i}" for i in range(100, 1000))
    rejection = state["rejected_page"]
    assert rejection["cache"] == rejected.name
    assert rejection["cache_sha256"] == common.digest(rejected.read_bytes())
    assert rejection["reason"] == "CROSS_PAGE_PUBLICATION_OVERLAP"
    assert rejection["repeated_publication_ids"] == ["MED:0"]
    assert rejection["returned_citations"] == 2 and "retained_citations" not in rejection
    assert rejection["accepted_prefix_citations"] == 1000
    assert result["summary"]["cached_pages"] == result["summary"]["rejected_cached_pages"] == 1
    assert result["summary"]["retained_query_citation_memberships"] == 1000
    assert result["summary"]["unique_retained_citations"] == 1000
    assert result["limitations"] == expansion.EXPORT_LIMITATIONS
    with (out / expansion.LEDGER).open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert [r["status"] for r in rows] == [expansion.CONFLICT_STATUS] * 2 + ["NOT_STARTED"]
    assert before == {p.name: p.read_bytes() for p in out.glob("epmc-*.json")}
    first = (out / expansion.CANDIDATES).read_bytes()
    expansion.analyze(root)
    assert (out / expansion.CANDIDATES).read_bytes() == first


@pytest.mark.parametrize("order", ["breadth-first", "query-local"])
def test_rejected_new_response_consumes_bound_and_resume_skips_conflicted_query(cohort, monkeypatch, order):
    root, out, plan = cohort
    for query in plan["queries"]:
        cache(expansion.parameters(query))
    calls = []

    def fetch(params, **kwargs):
        calls.append(params)
        if params["query"] == plan["queries"][0]["query"]:
            cache_overlap(plan["queries"][0])
        else:
            cache(params, offset=1000)

    monkeypatch.setattr(discovery, "fetch", fetch)
    expansion.search(root, 1, [], traversal_order=order)
    assert len(calls) == 1
    rejected = discovery.cache_path(calls[0])
    before = rejected.read_bytes()
    expansion.search(root, 10, [], traversal_order=order)
    assert len(calls) == 2 and calls[1]["query"] != calls[0]["query"]
    expansion.search(root, 10, ["CHEBI:2"], traversal_order=order)
    assert len(calls) == 2 and rejected.read_bytes() == before
    expansion.analyze(root)
    result = json.loads((out / expansion.CANDIDATES).read_bytes())
    assert result["summary"]["query_status"] == {
        expansion.CONFLICT_STATUS: 1, "CURSOR_TRAVERSAL_COMPLETE": 1,
    }


def test_rejected_page_change_during_export_fails_closed(cohort, monkeypatch):
    root, out, plan = cohort
    rejected = cache_overlap(plan["queries"][0])
    original = expansion.unchanged

    def changed(*args):
        original(*args)
        rejected.write_bytes(rejected.read_bytes() + b"\n")

    monkeypatch.setattr(expansion, "unchanged", changed)
    with pytest.raises(ValueError, match="page cache changed"):
        expansion.analyze(root)
    assert not (out / expansion.CANDIDATES).exists()
    assert not (out / expansion.LEDGER).exists()


def test_source_qualified_ids_do_not_collapse_across_pages(cohort):
    _, _, plan = cohort
    query = plan["queries"][0]
    cache(expansion.parameters(query))
    params = expansion.parameters(query, "after-1000")
    raw = response(params, offset=1000)
    body = json.loads(raw["body"])
    body["resultList"]["result"][0].update(source="PMC", id="0")
    common.write(discovery.cache_path(params).name, repack(raw, body))
    assert expansion.analyze_query(query)["status"] == "CURSOR_TRAVERSAL_COMPLETE"


@pytest.mark.parametrize("maximum,only", [(0, []), (-1, []), (True, []), (1, ["CHEBI:3"]), (1, ["absent"])])
def test_invalid_scope_cannot_request(cohort, monkeypatch, maximum, only):
    root, _, _ = cohort
    calls, _ = mock_network(monkeypatch)
    with pytest.raises(ValueError, match="invalid page bound"):
        expansion.search(root, maximum, only)
    assert calls == []


def test_network_opt_in_and_selected_shared_membership(cohort, monkeypatch):
    root, _, _ = cohort
    with pytest.raises(ValueError, match="network is disabled"):
        expansion.search(root, 1, [])
    calls, _ = mock_network(monkeypatch)
    expansion.search(root, 1, ["CHEBI:2"])
    assert len(calls) == 1 and '"Shared"' in calls[0]["query"]


@pytest.mark.parametrize("target", ["plan", "baseline", "record"])
def test_input_changes_during_search_are_rejected(cohort, monkeypatch, target):
    root, out, plan = cohort

    def fetch(params, **kwargs):
        cache(params)
        if target == "plan":
            common.write(expansion.PLAN, {})
        elif target == "baseline":
            common.write(plan["queries"][0]["baseline_cache"], {})
        else:
            (root / plan["queries"][0]["members"][0]["path"]).write_text("changed")

    monkeypatch.setattr(discovery, "fetch", fetch)
    with pytest.raises(ValueError, match="inputs changed|snapshot drift"):
        expansion.search(root, 1, [])


def test_altered_plan_is_rejected_before_network(cohort, monkeypatch):
    root, _, plan = cohort
    plan["queries"].pop()
    common.write(expansion.PLAN, plan)
    calls, _ = mock_network(monkeypatch)
    with pytest.raises(ValueError, match="stale or altered"):
        expansion.search(root, 1, [])
    assert calls == []


def test_count_drift_response_is_not_cached(cohort, monkeypatch):
    _, _, plan = cohort
    query = plan["queries"][0]
    params = expansion.parameters(query, "after-1000")
    raw = response(params, count=1003, offset=1000)
    monkeypatch.setattr(common, "ALLOW_NETWORK", True)
    monkeypatch.setattr(discovery.requests, "get", lambda *args, **kwargs: SimpleNamespace(
        url=discovery.URL, status_code=200, headers={}, content=raw["body"].encode(), text=raw["body"],
    ))
    with pytest.raises(ValueError, match="count or version changed"):
        discovery.fetch(params, retained_before=1000, expected_count=1002, expected_version="6.9")
    assert not discovery.cache_path(params).exists()


@pytest.mark.parametrize("change", ["count", "version", "short"])
def test_intact_conflicts_are_cached_only_by_opt_in_and_remain_strictly_invalid(cohort, monkeypatch, change):
    _, _, plan = cohort
    params = expansion.parameters(plan["queries"][0], "after-1000")
    raw = response(params, offset=1000)
    body = json.loads(raw["body"])
    if change == "count":
        body["hitCount"] = 1003
    elif change == "version":
        body["version"] = "7.0"
    else:
        body["resultList"]["result"].pop()
    repack(raw, body)
    calls = []

    def get(*args, **kwargs):
        calls.append(kwargs["params"])
        return SimpleNamespace(url=discovery.URL, status_code=200, headers={},
                               content=raw["body"].encode(), text=raw["body"])

    monkeypatch.setattr(common, "ALLOW_NETWORK", True)
    monkeypatch.setattr(discovery.requests, "get", get)
    monkeypatch.setattr(discovery.time, "sleep", lambda _: None)
    context = {"retained_before": 1000, "expected_count": 1002, "expected_version": "6.9"}
    result = discovery.fetch(params, **context, cache_conflicts=True)
    assert json.loads(discovery.cache_path(params).read_bytes()) == result
    monkeypatch.setattr(common, "ALLOW_NETWORK", False)
    assert discovery.fetch(params, **context, cache_conflicts=True) == result
    with pytest.raises(discovery.CitationPageConflict):
        discovery.fetch(params, **context)
    assert len(calls) == 1


@pytest.mark.parametrize("change", ["origin", "query", "negative_count", "within_page_duplicate",
                                   "abstract", "empty_identifier", "no_version"])
def test_conflict_cache_opt_in_never_accepts_integrity_errors(cohort, monkeypatch, change):
    _, _, plan = cohort
    params = expansion.parameters(plan["queries"][0])
    raw = response(params)
    body = json.loads(raw["body"])
    # Combine a short page with invalid contents: the latter must still fail closed.
    body["resultList"]["result"].pop()
    if change == "query":
        body["request"]["queryString"] = "different"
    elif change == "negative_count":
        body["hitCount"] = -1
    elif change == "within_page_duplicate":
        body["resultList"]["result"][0]["id"] = "1"
    elif change == "abstract":
        body["resultList"]["result"][0]["abstractText"] = "Forbidden"
    elif change == "empty_identifier":
        body["resultList"]["result"][0]["id"] = ""
    elif change == "no_version":
        body["version"] = None
    repack(raw, body)
    monkeypatch.setattr(common, "ALLOW_NETWORK", True)
    monkeypatch.setattr(discovery.requests, "get", lambda *args, **kwargs: SimpleNamespace(
        url="https://example.org/search" if change == "origin" else discovery.URL,
        status_code=200, headers={}, content=raw["body"].encode(), text=raw["body"],
    ))
    with pytest.raises(ValueError) as error:
        discovery.fetch(params, cache_conflicts=True)
    assert not isinstance(error.value, discovery.CitationPageConflict)
    assert not discovery.cache_path(params).exists()


def test_short_first_page_is_not_a_zero_hit_or_complete_query(cohort):
    _, _, plan = cohort
    query = plan["queries"][0]
    params = expansion.parameters(query)
    raw = response(params)
    body = json.loads(raw["body"])
    body["resultList"]["result"] = []
    common.write(discovery.cache_path(params).name, repack(raw, body))
    state = expansion.analyze_query(query, allow_conflicts=True)
    assert state["status"] == expansion.CONFLICT_STATUS
    assert state["hit_count"] is None and state["api_version"] is None
    assert state["pages"] == state["candidates"] == []
    assert state["rejected_page"]["reported_hit_count"] == 1002
    assert state["rejected_page"]["returned_citations"] == 0
    assert state["rejected_page"]["expected_returned_citations"] == 1000


@pytest.mark.parametrize("change", ["count", "version", "short"])
def test_live_shape_conflict_consumes_bound_and_does_not_stall_other_queries(cohort, monkeypatch, change):
    root, out, plan = cohort
    for query in plan["queries"]:
        cache(expansion.parameters(query))

    def modify(params, raw):
        if params["query"] != plan["queries"][0]["query"]:
            return raw
        body = json.loads(raw["body"])
        if change == "count":
            body["hitCount"] = 1003
        elif change == "version":
            body["version"] = "7.0"
        else:
            body["resultList"]["result"].pop()
        return repack(raw, body)

    calls, _ = mock_network(monkeypatch, modify)
    expansion.search(root, 1, [])
    assert len(calls) == 1 and calls[0]["query"] == plan["queries"][0]["query"]
    rejected = discovery.cache_path(calls[0])
    before = rejected.read_bytes()
    expansion.search(root, 1, [])
    assert len(calls) == 2 and calls[1]["query"] == plan["queries"][1]["query"]
    monkeypatch.setattr(common, "ALLOW_NETWORK", False)
    expansion.search(root, 10, [])
    expansion.analyze(root)
    result = json.loads((out / expansion.CANDIDATES).read_bytes())
    assert result["summary"]["query_status"] == {
        expansion.CONFLICT_STATUS: 1, "CURSOR_TRAVERSAL_COMPLETE": 1,
    }
    assert result["queries"][0]["hit_count"] == 1002
    assert result["queries"][0]["api_version"] == "6.9"
    assert len(result["queries"][0]["candidates"]) == 1000
    assert len(calls) == 2 and rejected.read_bytes() == before


def test_empty_expansion_emits_header_only_ledger(cohort, monkeypatch):
    root, out, _ = cohort
    plan = json.loads((out / expansion.PLAN).read_bytes())
    plan["queries"] = []
    common.write(expansion.PLAN, plan)
    monkeypatch.setattr(expansion, "build_plan", lambda _: plan)
    expansion.analyze(root)
    result = json.loads((out / expansion.CANDIDATES).read_bytes())
    assert result["summary"]["query_status"] == {} and result["queries"] == []
    assert (out / expansion.LEDGER).read_text() == "\t".join(expansion.LEDGER_FIELDS) + "\n"


def test_page_changed_after_analysis_cannot_be_exported(cohort, monkeypatch):
    root, out, plan = cohort
    params = expansion.parameters(plan["queries"][0])
    cache(params)
    original = expansion.unchanged

    def changed(*args):
        original(*args)
        cache(params, count=0)

    monkeypatch.setattr(expansion, "unchanged", changed)
    with pytest.raises(ValueError, match="page cache changed"):
        expansion.analyze(root)
    assert not (out / expansion.CANDIDATES).exists()
    assert not (out / expansion.LEDGER).exists()
