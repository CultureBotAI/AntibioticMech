"""Lexical literature discovery must not claim exact identities or phenotypes."""

import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import discover_resistance_literature as discovery  # noqa: E402


def response(parameters, count=1):
    payload = {
        "version": "6.9", "hitCount": count,
        "request": {"queryString": parameters["query"], "resultType": "lite",
                    "cursorMark": "*", "pageSize": 100, "synonym": False},
        "resultList": {"result": [{"source": "MED", "id": str(i), "title": "Candidate paper"}
                                  for i in range(min(max(count, 0), 100))]},
    }
    if count > 100:
        payload["nextCursorMark"] = "another-page"
    body = json.dumps(payload)
    return {"url": discovery.URL, "status": 200, "params": parameters, "body": body,
            "sha256": discovery.common.digest(body.encode()), "headers": {}}


@pytest.fixture
def cohort(tmp_path, monkeypatch):
    monkeypatch.setattr(discovery.common, "OUT", tmp_path)
    monkeypatch.setattr(discovery.common, "ALLOW_NETWORK", False)
    records = [{
        "identifier": f"CHEBI:{i}", "label": f"Compound {i}", "path": f"{i}.yaml",
        "sha256": str(i), "standard_inchi_key": str(i), "class": cls,
        "resistance_mechanisms": [], "score_rules": [],
    } for i, cls in enumerate(["A", "A", "B", "C"], 1)]
    records[-1]["resistance_mechanisms"] = [{"label": "Already has a claim"}]
    monkeypatch.setattr(discovery.card, "current_corpus", lambda _: records)
    discovery.common.write("corpus.json", {"records": records})
    discovery.plan(tmp_path)
    return tmp_path, discovery.load_plan(tmp_path)[0]["records"]


def test_plan_retains_every_empty_record_and_balances_classes(cohort):
    _, records = cohort
    assert [r["identifier"] for r in records] == ["CHEBI:1", "CHEBI:3", "CHEBI:2"]
    assert len({r["identifier"] for r in records}) == 3


def test_query_quotes_labels_without_dropping_stereochemistry():
    assert discovery.query('(2R)-compound "A"').startswith('TITLE_ABS:"(2R)-compound \\"A\\""')
    with pytest.raises(ValueError, match="invalid canonical label"):
        discovery.query("compound\nOR anything")


@pytest.mark.parametrize("count", [0, 1, 100, 101])
def test_zero_and_truncated_searches_are_explicit(cohort, count):
    root, records = cohort
    parameters = discovery.params(records[0])
    discovery.common.write(discovery.cache_path(parameters).name, response(parameters, count))
    discovery.analyze(root)
    result = json.loads((root / "discovery-candidates.json").read_text())
    record = result["records"][0]
    assert record["hit_count"] == count
    assert record["status"] == (
        "NO_HITS_IN_LIMITED_QUERY" if count == 0 else
        "TRUNCATED_REFINEMENT_REQUIRED" if count > 100 else "CANDIDATES_REQUIRE_REVIEW"
    )
    assert record["primary_review_status"] == "PENDING"
    assert all("protein_accession" not in c and "taxon_id" not in c for c in record["candidates"])
    assert result["summary"]["NOT_SEARCHED"] == 2


@pytest.mark.parametrize("change", ["wrong_query", "negative_count", "duplicate", "missing_rows", "abstract"])
def test_bad_responses_are_not_reported_as_search_results(change):
    parameters = discovery.params({"query": "test"})
    raw = response(parameters, 2)
    body = json.loads(raw["body"])
    if change == "wrong_query":
        body["request"]["queryString"] = "other"
    elif change == "negative_count":
        body["hitCount"] = -1
    elif change == "duplicate":
        body["resultList"]["result"] *= 2
        body["hitCount"] = 4
    elif change == "missing_rows":
        body["resultList"]["result"] = []
    else:
        body["resultList"]["result"][0]["abstractText"] = "Do not export"
    raw["body"] = json.dumps(body)
    raw["sha256"] = discovery.common.digest(raw["body"].encode())
    with pytest.raises(ValueError):
        discovery.validate(raw, parameters)


def test_http_error_does_not_look_like_no_hits(cohort, monkeypatch):
    root, records = cohort
    monkeypatch.setattr(discovery.common, "ALLOW_NETWORK", True)

    def get(url, **kwargs):
        assert url == discovery.URL
        assert kwargs["allow_redirects"] is False
        return SimpleNamespace(url=url, status_code=302, headers={}, content=b"", text="")

    monkeypatch.setattr(discovery.requests, "get", get)
    with pytest.raises(ValueError, match="unsuccessful or corrupt"):
        discovery.fetch(discovery.params(records[0]))
    assert not list(root.glob("epmc-discovery-*.json"))


def test_network_remains_opt_in(cohort):
    _, records = cohort
    with pytest.raises(ValueError, match="network is disabled"):
        discovery.fetch(discovery.params(records[0]))


def test_changed_census_is_not_silently_reused(cohort):
    root, _ = cohort
    discovery.common.write("corpus.json", {"changed": True})
    with pytest.raises(ValueError, match="stale discovery plan"):
        discovery.load_plan(root)


def test_request_bound_and_resume_keep_all_record_ids(cohort, monkeypatch):
    root, records = cohort
    calls = []

    def fetch(parameters, session=None):
        path = discovery.cache_path(parameters)
        if not path.exists():
            calls.append(parameters)
            discovery.common.write(path.name, response(parameters, 0))
        return json.loads(path.read_text())

    monkeypatch.setattr(discovery, "fetch", fetch)
    discovery.search(root, 1, [])
    assert len(calls) == 1
    discovery.search(root, 1, [])
    assert len(calls) == 2
    discovery.analyze(root)
    result = json.loads((root / "discovery-candidates.json").read_text())
    assert len(result["records"]) == len(records) == 3
    assert result["summary"] == {"NO_HITS_IN_LIMITED_QUERY": 2, "NOT_SEARCHED": 1}


def test_empty_cohort_still_emits_a_ledger(cohort, monkeypatch):
    root, _ = cohort
    monkeypatch.setattr(discovery.card, "current_corpus", lambda _: [])
    discovery.common.write("corpus.json", {"records": []})
    discovery.plan(root)
    discovery.analyze(root)
    result = json.loads((root / "discovery-candidates.json").read_text())
    assert result["summary"] == {}
    assert result["records"] == []
    assert (root / "discovery-ledger.tsv").read_text() == "\t".join(discovery.LEDGER_FIELDS) + "\n"


def test_search_reuses_and_closes_one_http_session(cohort, monkeypatch):
    root, _ = cohort
    calls, sessions, closed = [], [], []
    monkeypatch.setattr(discovery.common, "ALLOW_NETWORK", True)
    monkeypatch.setattr(discovery.time, "sleep", lambda _: None)

    class Session:
        def __enter__(self):
            sessions.append(self)
            return self

        def __exit__(self, *args):
            closed.append(self)

        def get(self, url, **kwargs):
            calls.append((self, kwargs["params"]))
            assert url == discovery.URL
            assert kwargs["allow_redirects"] is False
            raw = response(kwargs["params"], 0)
            return SimpleNamespace(url=url, status_code=200, headers={},
                                   content=raw["body"].encode(), text=raw["body"])

    monkeypatch.setattr(discovery.requests, "Session", Session)
    discovery.search(root, 2, [])
    assert len(sessions) == 1 and closed == sessions
    assert len(calls) == 2 and all(client is sessions[0] for client, _ in calls)


@pytest.mark.parametrize("url", [
    "https://example.org/europepmc/webservices/rest/search",
    "http://www.ebi.ac.uk/europepmc/webservices/rest/search",
    discovery.URL + "#untrusted",
])
def test_cached_response_must_have_the_expected_origin(url):
    parameters = discovery.params({"query": "test"})
    raw = response(parameters)
    raw["url"] = url
    with pytest.raises(ValueError, match="response origin"):
        discovery.validate(raw, parameters)


@pytest.mark.parametrize("failure", ["timeout", "connection", "server", "rate_limit"])
def test_transient_retries_are_bounded_without_caching_errors(cohort, monkeypatch, failure):
    root, records = cohort
    monkeypatch.setattr(discovery.common, "ALLOW_NETWORK", True)
    monkeypatch.setattr(discovery.time, "sleep", lambda _: None)
    calls = []

    def get(url, **kwargs):
        calls.append(url)
        assert kwargs["allow_redirects"] is False
        if failure == "timeout":
            raise discovery.requests.Timeout()
        if failure == "connection":
            raise discovery.requests.ConnectionError()
        return SimpleNamespace(url=url, status_code=503 if failure == "server" else 429,
                               headers={}, content=b"", text="")

    monkeypatch.setattr(discovery.requests, "get", get)
    with pytest.raises((ValueError, discovery.requests.RequestException)):
        discovery.fetch(discovery.params(records[0]))
    assert len(calls) == 3
    assert not list(root.glob("epmc-discovery-*.json"))


def test_retry_success_is_cached_and_replayed_offline(cohort, monkeypatch):
    _, records = cohort
    parameters = discovery.params(records[0])
    raw = response(parameters, 0)
    calls = []
    monkeypatch.setattr(discovery.common, "ALLOW_NETWORK", True)
    monkeypatch.setattr(discovery.time, "sleep", lambda _: None)

    def get(url, **kwargs):
        calls.append(url)
        if len(calls) == 1:
            raise discovery.requests.Timeout()
        return SimpleNamespace(url=url, status_code=200, headers={},
                               content=raw["body"].encode(), text=raw["body"])

    monkeypatch.setattr(discovery.requests, "get", get)
    fetched = discovery.fetch(parameters)
    monkeypatch.setattr(discovery.common, "ALLOW_NETWORK", False)
    assert discovery.fetch(parameters) == fetched
    assert len(calls) == 2
