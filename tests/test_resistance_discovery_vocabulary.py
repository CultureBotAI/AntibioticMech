"""A broader vocabulary supplements rather than rewrites historical discovery."""

import copy
import json
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import discover_resistance_aliases as aliases  # noqa: E402

PROFILE = aliases.IMMUNITY_PROFILE


@pytest.fixture
def cohort(tmp_path, monkeypatch):
    out = tmp_path / "reports"
    out.mkdir()
    monkeypatch.setattr(aliases.common, "OUT", out)
    monkeypatch.setattr(aliases.common, "ALLOW_NETWORK", False)
    docs, rows = {}, []
    for index, cls in enumerate(("A", "A", "B"), 1):
        path = Path("data/antibiotics") / f"{index}.yaml"
        absolute = tmp_path / path
        absolute.parent.mkdir(parents=True, exist_ok=True)
        doc = {"identifier": f"CHEBI:{index}", "label": f"Compound {index}",
               "antimicrobial_class": cls, "chemical_structure": {"standard_inchi_key": f"KEY{index}"},
               "synonyms": [{"synonym_text": "Shared alias", "synonym_type": "RELATED_SYNONYM"}]}
        absolute.write_text(json.dumps(doc))
        docs[absolute] = doc
        rows.append({"identifier": doc["identifier"], "label": doc["label"], "path": str(path),
                     "sha256": aliases.common.digest(absolute.read_bytes()), "class": cls,
                     "standard_inchi_key": f"KEY{index}",
                     "resistance_mechanisms": [{"label": "existing"}] if index == 2 else [],
                     "score_rules": [{"source": "HIVDB"}] if index == 3 else []})
    monkeypatch.setattr(aliases, "load_record", lambda path: copy.deepcopy(docs[path]))
    aliases.common.write("corpus.json", {"records": rows})
    aliases.plan(tmp_path)
    aliases.plan(tmp_path, profile=PROFILE)
    return tmp_path, out


def response(parameters, ids=()):
    body = json.dumps({
        "version": "6.9", "hitCount": len(ids),
        "request": {"queryString": parameters["query"], "resultType": "lite",
                    "pageSize": 100, "cursorMark": "*", "synonym": False},
        "resultList": {"result": [{"source": source, "id": value, "title": "Reference lead"}
                                  for source, value in ids[:100]]},
        "nextCursorMark": "next" if len(ids) > 100 else None,
    })
    return {"url": aliases.discovery.URL, "params": parameters, "status": 200, "body": body,
            "sha256": aliases.common.digest(body.encode()), "headers": {}, "retrieved_at": "fixture"}


def test_expanded_query_retains_old_concepts_and_adds_known_missing_vocabulary():
    names = ['(2R)-A "quote"', r"B\C"]
    old = aliases.discovery.query_names(names)
    new = PROFILE.query_names(names)
    assert old.startswith(aliases.discovery.name_clause(names) + " AND ")
    assert new.startswith(aliases.discovery.name_clause(names) + " AND ")
    for term in ("resistan*", "susceptib*", "toleran*", "allele*",
                 "mutan*", "mutation*", "genetic*", "genom*"):
        assert "TITLE_ABS:" + term in old and "TITLE_ABS:" + term in new
    assert "TITLE_ABS:gene*" in new and "TITLE_ABS:gene OR" in old
    assert all("TITLE_ABS:" + term in new for term in ("immun*", "sensitiv*"))
    assert " NOT " not in new
    assert aliases.discovery.params({"query": old}) != aliases.discovery.params({"query": new})


@pytest.mark.parametrize("names", [[], [""], ["  "], ["valid", "bad\nOR anything"]])
def test_expanded_names_fail_closed(names):
    with pytest.raises(ValueError, match="empty name query|invalid canonical label"):
        PROFILE.query_names(names)


def test_all_saved_v1_queries_remain_byte_compatible():
    path = ROOT / "research/2026-10-08-resistance-alias-discovery-plan.json"
    plan = json.loads(path.read_bytes())
    assert len(plan["records"]) == 2939
    for record in plan["records"]:
        assert aliases.make_queries(record["names"]) == record["queries"]
    assert sum(len(r["queries"]) for r in plan["records"]) == 7469


def test_profiles_preserve_every_record_origin_and_shared_name(cohort):
    root, out = cohort
    old, _ = aliases.load_plan(root)
    new, _ = aliases.load_plan(root, profile=PROFILE)
    assert old["criteria"] == aliases.CRITERIA != new["criteria"]
    assert new["criteria"].endswith("-v2")
    assert [r["identifier"] for r in new["records"]] == ["CHEBI:1", "CHEBI:3", "CHEBI:2"]
    assert sum(r["has_existing_resistance_evidence"] for r in new["records"]) == 2
    for previous, current in zip(old["records"], new["records"], strict=True):
        assert {k: v for k, v in previous.items() if k != "queries"} == {
            k: v for k, v in current.items() if k != "queries"}
        assert sorted(i for q in current["queries"] for i in q["name_indices"]) == [0, 1]
        assert all("immun*" in q["query"] for q in current["queries"])
    assert (out / aliases.PLAN).exists() and (out / PROFILE.plan).exists()
    assert {aliases.PLAN, aliases.CANDIDATES, aliases.LEDGER}.isdisjoint({
        PROFILE.plan, PROFILE.candidates, PROFILE.ledger})


def test_expanded_query_chunking_enforces_full_encoded_url_bound():
    names = [{"text": "canonical"}] + [{"text": f"alias-{i}-" + "(2R)-" * 190} for i in range(9)]
    queries = aliases.make_queries(names, profile=PROFILE)
    assert sorted(i for q in queries for i in q["name_indices"]) == list(range(len(names)))
    for query in queries:
        url = aliases.discovery.URL + "?" + urlencode(aliases.discovery.params(query))
        assert len(url.encode()) <= aliases.MAX_URL_BYTES
        assert len(query["name_indices"]) <= aliases.MAX_NAMES


def test_v2_does_not_reuse_v1_cache_or_overwrite_v1_exports(cohort, monkeypatch):
    root, out = cohort
    old, _ = aliases.load_plan(root)
    for record in old["records"]:
        for query in record["queries"]:
            params = aliases.discovery.params(query)
            aliases.common.write(aliases.discovery.cache_path(params).name,
                                 response(params, [("MED", "old")]))
    aliases.analyze(root)
    frozen = {p.name: p.read_bytes() for p in out.iterdir() if p.name != PROFILE.plan}
    calls = []

    def fetch(parameters, session=None):
        path = aliases.discovery.cache_path(parameters)
        if not path.exists():
            calls.append(parameters["query"])
            aliases.common.write(path.name, response(parameters, [("MED", "new"), ("PMC", "new")]))
        return json.loads(path.read_bytes())

    monkeypatch.setattr(aliases.discovery, "fetch", fetch)
    aliases.search(root, 1, [], profile=PROFILE)
    aliases.search(root, 1, [], profile=PROFILE)
    aliases.analyze(root, profile=PROFILE)
    assert len(calls) == 2
    result = json.loads((out / PROFILE.candidates).read_bytes())
    assert result["criteria"] == PROFILE.criteria
    assert result["summary"]["record_search_status"] == {"PARTIAL": 2, "NOT_SEARCHED": 1}
    assert result["records"][0]["candidate_ids"] == ["MED:new", "PMC:new"]
    assert all(r["primary_review_status"] == "PENDING" for r in result["records"])
    assert all((out / name).read_bytes() == payload for name, payload in frozen.items())


@pytest.mark.parametrize("change", ["criteria", "query", "names", "record"])
def test_v2_plan_tampering_is_not_masked_by_valid_v1(cohort, change):
    root, out = cohort
    value = json.loads((out / PROFILE.plan).read_bytes())
    if change == "criteria":
        value["criteria"] = aliases.CRITERIA
    elif change == "query":
        value["records"][0]["queries"][0]["query"] = "altered"
    elif change == "names":
        value["records"][0]["names"].pop()
    else:
        value["records"].pop()
    aliases.common.write(PROFILE.plan, value)
    aliases.load_plan(root)
    with pytest.raises(ValueError, match="stale or altered"):
        aliases.load_plan(root, profile=PROFILE)


@pytest.mark.parametrize("maximum", [True, 1.5, 0, -1])
def test_v2_request_bound_requires_positive_integer(cohort, monkeypatch, maximum):
    root, _ = cohort
    monkeypatch.setattr(aliases.discovery, "fetch", lambda *a, **kw: pytest.fail("unexpected request"))
    with pytest.raises(ValueError, match="invalid request bound"):
        aliases.search(root, maximum, [], profile=PROFILE)


def test_v2_network_is_still_explicitly_opt_in(cohort):
    root, _ = cohort
    with pytest.raises(ValueError, match="network is disabled"):
        aliases.search(root, 1, [], profile=PROFILE)
