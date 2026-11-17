"""V2 expansion preserves historical identity, cursor boundaries and review scope."""

import argparse
import copy
import csv
import json
import sys
from collections import Counter
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import expand_resistance_vocabulary as expansion  # noqa: E402

base = expansion.expansion
discovery = expansion.discovery
common = expansion.common
aliases = expansion.aliases


def response(params, count=1002, offset=0):
    rows = [{"source": "MED", "id": str(i), "title": "Citation metadata"}
            for i in range(offset, min(offset + params["pageSize"], count))]
    body = {"version": "6.9", "hitCount": count,
            "request": {"queryString": params["query"], "resultType": "lite",
                        "pageSize": params["pageSize"], "cursorMark": params["cursorMark"],
                        "synonym": False, "sort": params.get("sort", "")},
            "resultList": {"result": rows}, "nextCursorMark": "after-" + str(offset + len(rows))}
    raw = {"url": discovery.URL, "status": 200, "params": params, "headers": {},
           "retrieved_at": "2026-10-09T00:00:00Z"}
    return repack(raw, body)


def repack(raw, body):
    raw["body"] = json.dumps(body)
    raw["sha256"] = common.digest(raw["body"].encode())
    return raw


@pytest.fixture
def cohort(tmp_path, monkeypatch):
    root, out = tmp_path / "root", tmp_path / "cache"
    (root / "data/antibiotics").mkdir(parents=True)
    out.mkdir()
    monkeypatch.setattr(common, "OUT", out)
    monkeypatch.setattr(common, "ALLOW_NETWORK", False)
    records, census, found = [], [], []
    for i, (label, cls) in enumerate((("Shared", "A"), ("Small", "B"), ("Shared", "A"), ("Third", "C")), 1):
        path = root / f"data/antibiotics/{i}.yaml"
        doc = {"identifier": f"CHEBI:{i}", "label": label, "antimicrobial_class": cls,
               "chemical_structure": {"standard_inchi_key": str(i)}}
        path.write_text(json.dumps(doc))
        record = {"identifier": doc["identifier"], "label": label, "class": cls,
                  "path": str(path.relative_to(root)), "standard_inchi_key": str(i),
                  "sha256": common.digest(path.read_bytes()), "names": aliases.record_names(doc)}
        records.append(record)
        census.append({**{k: record[k] for k in expansion.union.IDENTITY if k != "class"},
                       "record_sha256": record["sha256"]})
    for record in records:
        for name in record["names"]:
            name["shared_with_record_ids"] = sorted(r["identifier"] for r in records
                if r["label"] == name["text"] and r["identifier"] != record["identifier"])
        record["queries"] = aliases.make_queries(record["names"], profile=expansion.PROFILE)
        query, = record["queries"]
        raw = response(discovery.params(query), 5 if record["label"] == "Small" else 1002)
        common.write(discovery.cache_path(raw["params"]).name, raw)
        found.append(aliases.analyze_record(record))
    planned = {"criteria": expansion.PROFILE.criteria, "corpus_sha256": "historical-census",
               "records": records}
    expansion.freeze(root / "initial-plan.json", planned)
    statuses = Counter(q["status"] for r in found for q in r["queries"])
    candidates = {"criteria": planned["criteria"], "corpus_sha256": planned["corpus_sha256"],
                  "plan_sha256": expansion.pin(root, "initial-plan.json")["sha256"], "records": found,
                  "summary": {"query_status": dict(statuses)}}
    expansion.freeze(root / "initial-candidates.json", candidates)
    descriptor = {"criteria": planned["criteria"], "plan": expansion.pin(root, "initial-plan.json"),
                  "candidate_index": expansion.pin(root, "initial-candidates.json")}
    expansion.freeze(root / "initial.json", descriptor)
    # A changed non-name annotation may be bridged without rewriting its historical hash.
    path = root / records[0]["path"]
    doc = json.loads(path.read_bytes())
    doc["description"] = "Later curation"
    path.write_text(json.dumps(doc))
    census[0]["record_sha256"] = common.digest(path.read_bytes())
    with (root / "census.tsv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=census[0], delimiter="\t")
        writer.writeheader()
        writer.writerows(census)
    result = expansion.build_plan(root, "initial.json", "census.tsv")
    expansion.freeze(out / expansion.PLAN, result)
    return root, out, result, planned, candidates


def network(monkeypatch, mutate=None):
    calls = []
    monkeypatch.setattr(common, "ALLOW_NETWORK", True)
    monkeypatch.setattr(discovery.time, "sleep", lambda _: None)

    class Session:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def get(self, url, **kwargs):
            assert url == discovery.URL and kwargs["allow_redirects"] is False
            params = kwargs["params"]
            calls.append(params)
            offset = 0 if params["cursorMark"] == "*" else int(params["cursorMark"].split("-")[1])
            raw = response(params, offset=offset)
            if mutate:
                raw = mutate(params, raw)
            return SimpleNamespace(url=url, status_code=200, headers={},
                                   content=raw["body"].encode(), text=raw["body"])

    monkeypatch.setattr(discovery.requests, "Session", Session)
    return calls


def test_plan_reconciles_every_record_without_rewriting_historical_hashes(cohort):
    root, out, planned, old, _ = cohort
    assert planned["name_bridge"]["records_verified"] == 4
    assert planned["name_bridge"]["record_hashes_changed_since_historical_plan"] == 1
    assert planned["name_bridge"]["ignored_files_included"]
    assert not planned["name_bridge"]["historical_record_pins_rewritten"]
    assert len(planned["queries"]) == 2
    assert sum(len(q["members"]) for q in planned["queries"]) == 3
    assert [q["members"][0]["class"] for q in planned["queries"]] == ["A", "C"]
    assert planned["queries"][0]["members"][0]["sha256"] == old["records"][0]["sha256"]
    assert expansion.load_plan(root)[0] == planned
    assert json.loads((out / expansion.PLAN).read_bytes())["scope"] == expansion.SCOPE


def test_shared_query_membership_is_not_a_chemical_merge(cohort):
    _, _, planned, _, _ = cohort
    members = planned["queries"][0]["members"]
    assert [m["identifier"] for m in members] == ["CHEBI:1", "CHEBI:3"]
    assert members[0]["standard_inchi_key"] != members[1]["standard_inchi_key"]
    assert members[0]["names"][0]["text"] == "Shared"


@pytest.mark.parametrize("change", ["v1", "hash", "count", "name", "query", "candidate_pin"])
def test_invalid_initial_inputs_are_rejected(cohort, change):
    root, _, _, old, found = cohort
    descriptor = json.loads((root / "initial.json").read_bytes())
    if change == "v1":
        descriptor["criteria"] = aliases.LEGACY_PROFILE.criteria
    elif change == "hash":
        found["plan_sha256"] = "changed"
    elif change == "count":
        found["records"][0]["queries"][0]["hit_count"] = 99
    elif change == "name":
        old["records"][0]["names"][0]["text"] = "Changed name"
    elif change == "query":
        old["records"][0]["queries"][0]["query"] = "Changed query"
    else:
        descriptor["candidate_index"]["sha256"] = "invalid"
    (root / "initial-plan.json").write_text(json.dumps(old))
    (root / "initial-candidates.json").write_text(json.dumps(found))
    if change != "candidate_pin":
        descriptor["candidate_index"] = expansion.pin(root, "initial-candidates.json")
    descriptor["plan"] = expansion.pin(root, "initial-plan.json")
    if change not in {"hash", "candidate_pin", "v1"}:
        found["plan_sha256"] = descriptor["plan"]["sha256"]
        (root / "initial-candidates.json").write_text(json.dumps(found))
        descriptor["candidate_index"] = expansion.pin(root, "initial-candidates.json")
    (root / "initial.json").write_text(json.dumps(descriptor))
    with pytest.raises(ValueError):
        expansion.build_plan(root, "initial.json", "census.tsv")


@pytest.mark.parametrize("change", ["ignored", "record", "census", "names", "class"])
def test_bridge_checks_ignored_files_and_live_names(cohort, change):
    root, _, _, old, _ = cohort
    if change == "ignored":
        directory = root / "data/antibiotics/.ignored"
        directory.mkdir()
        (root / ".gitignore").write_text(".ignored/\n")
        (directory / "hidden.yaml").write_text("{}")
    elif change == "record":
        (root / "data/antibiotics/1.yaml").write_text("{}")
    elif change == "census":
        with (root / "census.tsv").open("a") as stream:
            stream.write("CHEBI:1\tduplicate\n")
    elif change == "names":
        old["records"][0]["names"][0]["origins"] = []
    else:
        old["records"][0]["class"] = "Different"
    with pytest.raises(ValueError):
        expansion.name_bridge(root, old, "census.tsv")


def test_sort_is_opt_in_and_separates_cache_keys(cohort):
    _, _, planned, _, _ = cohort
    query = planned["queries"][0]
    legacy = base.parameters(query)
    sorted_params = base.parameters(query, sort=expansion.SORT)
    assert "sort" not in legacy
    assert sorted_params == dict(legacy, sort=expansion.SORT)
    assert discovery.cache_path(legacy) != discovery.cache_path(sorted_params)
    with pytest.raises(ValueError, match="unsupported"):
        base.parameters(query, sort="unsupported")


def test_sort_echo_must_match_before_caching(cohort, monkeypatch):
    root, _, planned, _, _ = cohort

    def mutate(params, raw):
        body = json.loads(raw["body"])
        body["request"]["sort"] = ""
        return repack(raw, body)

    network(monkeypatch, mutate)
    with pytest.raises(ValueError, match="sort echo"):
        expansion.search(root, 1, [])
    assert not discovery.cache_path(base.parameters(planned["queries"][0], sort=expansion.SORT)).exists()


def test_query_local_bound_resume_and_offline_replay(cohort, monkeypatch):
    root, out, planned, _, _ = cohort
    calls = network(monkeypatch)
    expansion.search(root, 1, [])
    assert len(calls) == 1
    summary = expansion.analyze(root)
    assert summary["query_status"] == {"PARTIAL_CURSOR_TRAVERSAL": 1, "NOT_STARTED": 1}
    expansion.search(root, 2, [])
    assert [p["query"] for p in calls[:2]] == [planned["queries"][0]["query"]] * 2
    assert calls[2]["query"] == planned["queries"][1]["query"]
    expansion.search(root, 1, [])
    assert len(calls) == 4
    summary = expansion.analyze(root)
    assert summary["query_status"] == {"CURSOR_TRAVERSAL_COMPLETE": 2}
    first = (out / expansion.CANDIDATES).read_bytes()
    monkeypatch.setattr(common, "ALLOW_NETWORK", False)
    expansion.search(root, 10, [])
    expansion.analyze(root)
    assert len(calls) == 4 and (out / expansion.CANDIDATES).read_bytes() == first
    found = json.loads(first)
    assert found["scope"] == expansion.SCOPE
    assert all(q["primary_review_status"] == "PENDING" for q in found["queries"])
    assert sum(len(q["candidates"]) for q in found["queries"]) == 2004
    assert all(set(c) <= set(discovery.CITATION_FIELDS) for q in found["queries"] for c in q["candidates"])


@pytest.mark.parametrize("change", ["count", "overlap"])
def test_conflicts_reject_whole_page_and_never_resume_it(cohort, monkeypatch, change):
    root, out, planned, _, _ = cohort

    def mutate(params, raw):
        if params["cursorMark"] != "*":
            body = json.loads(raw["body"])
            if change == "count":
                body["hitCount"] += 1
            else:
                body["resultList"]["result"][0]["id"] = "0"
            return repack(raw, body)
        return raw

    calls = network(monkeypatch, mutate)
    only = [planned["queries"][0]["query_key"]]
    expansion.search(root, 5, only)
    assert len(calls) == 2
    expansion.search(root, 5, only)
    assert len(calls) == 2
    expansion.analyze(root)
    query = json.loads((out / expansion.CANDIDATES).read_bytes())["queries"][0]
    assert query["status"] == base.CONFLICT_STATUS
    assert query["rejected_page"]["accepted_prefix_citations"] == len(query["candidates"]) == 1000
    assert "MED:1001" not in {c["source"] + ":" + c["id"] for c in query["candidates"]}


@pytest.mark.parametrize("maximum", [0, -1, True, 1.5])
def test_invalid_bounds_do_not_contact_service(cohort, monkeypatch, maximum):
    root, _, _, _, _ = cohort
    calls = network(monkeypatch)
    with pytest.raises(ValueError, match="bound"):
        expansion.search(root, maximum, [])
    assert not calls


def test_unknown_query_and_network_opt_in(cohort, monkeypatch):
    root, _, _, _, _ = cohort
    with pytest.raises(ValueError, match="unknown"):
        expansion.search(root, 1, ["not-planned"])
    with pytest.raises(ValueError, match="network is disabled"):
        expansion.search(root, 1, [])


def test_record_change_during_search_is_not_a_verified_checkpoint(cohort, monkeypatch):
    root, _, _, _, _ = cohort

    def mutate(params, raw):
        (root / "data/antibiotics/1.yaml").write_text("{}")
        return raw

    calls = network(monkeypatch, mutate)
    with pytest.raises(ValueError, match="record changed"):
        expansion.search(root, 1, [])
    assert len(calls) == 1
    with pytest.raises(ValueError, match="checksum drift"):
        expansion.analyze(root)


def test_plan_and_input_changes_are_rejected(cohort):
    root, out, planned, _, _ = cohort
    before = common.digest((out / expansion.PLAN).read_bytes())
    altered = copy.deepcopy(planned)
    altered["requested_sort"] = "different"
    (out / expansion.PLAN).write_text(json.dumps(altered))
    with pytest.raises(ValueError, match="altered"):
        expansion.load_plan(root)
    with pytest.raises(ValueError, match="plan changed"):
        expansion.unchanged(root, planned, before)
    with pytest.raises(ValueError, match="frozen"):
        expansion.freeze(out / expansion.PLAN, planned)
    (root / "initial.json").write_text("{}")
    with pytest.raises(ValueError, match="input changed"):
        expansion.verify_inputs(root, planned)


def test_cli_bound_requires_positive_integer():
    assert expansion.positive_integer("25") == 25
    with pytest.raises(argparse.ArgumentTypeError):
        expansion.positive_integer("0")
    with pytest.raises(ValueError):
        expansion.positive_integer("1.5")
