"""All-record name discovery preserves scope without implying exact identities."""

import copy
import csv
import json
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import discover_resistance_aliases as aliases  # noqa: E402


def response(query, ids=()):
    params = aliases.discovery.params(query)
    body = json.dumps({
        "version": "6.9", "hitCount": len(ids),
        "request": {"queryString": params["query"], "resultType": "lite",
                    "pageSize": 100, "cursorMark": "*", "synonym": False},
        "resultList": {"result": [{"source": source, "id": value, "title": "Discovery lead"}
                                  for source, value in ids[:100]]},
        "nextCursorMark": "next" if len(ids) > 100 else None,
    })
    return {"url": aliases.discovery.URL, "params": params, "status": 200, "body": body,
            "sha256": aliases.common.digest(body.encode()), "headers": {}, "retrieved_at": "fixture"}


def cache(query, ids=()):
    item = response(query, ids)
    aliases.common.write(aliases.discovery.cache_path(item["params"]).name, item)


@pytest.fixture
def cohort(tmp_path, monkeypatch):
    out = tmp_path / "reports"
    out.mkdir()
    monkeypatch.setattr(aliases.common, "OUT", out)
    monkeypatch.setattr(aliases.common, "ALLOW_NETWORK", False)
    docs, records = {}, []
    for index, cls in enumerate(["A", "A", "B"], 1):
        path = Path("data/antibiotics") / f"{index}.yaml"
        absolute = tmp_path / path
        absolute.parent.mkdir(parents=True, exist_ok=True)
        doc = {
            "identifier": f"CHEBI:{index}", "label": f"Compound {index}", "antimicrobial_class": cls,
            "chemical_structure": {"standard_inchi_key": f"KEY{index}"},
            "synonyms": [
                {"synonym_text": "Shared name", "synonym_type": "RELATED_SYNONYM", "source": "chebi"},
                {"synonym_text": f"Alias {index}", "synonym_type": "INN", "source": "chebi"},
            ],
            "source_concepts": [{"source": "CHEBI", "source_id": f"CHEBI:{index}",
                                 "source_label": f"Compound {index}"}],
        }
        absolute.write_text(json.dumps(doc))
        docs[absolute] = doc
        records.append({
            "identifier": doc["identifier"], "label": doc["label"], "path": str(path),
            "sha256": aliases.common.digest(absolute.read_bytes()), "class": cls,
            "standard_inchi_key": f"KEY{index}",
            "resistance_mechanisms": [{"label": "existing"}] if index == 2 else [],
            "score_rules": [{"source": "HIVDB"}] if index == 3 else [],
        })
    monkeypatch.setattr(aliases, "load_record", lambda path: copy.deepcopy(docs[path]))
    aliases.common.write("corpus.json", {"records": records})
    aliases.plan(tmp_path)
    return tmp_path, out, docs


def read_plan(out):
    return json.loads((out / aliases.PLAN).read_bytes())


def test_every_record_and_name_including_related_names_is_retained(cohort):
    _, out, docs = cohort
    planned = read_plan(out)["records"]
    assert [r["identifier"] for r in planned] == ["CHEBI:1", "CHEBI:3", "CHEBI:2"]
    assert sum(r["has_existing_resistance_evidence"] for r in planned) == 2
    for item in planned:
        assert len(item["names"]) == 3
        assert sorted(i for q in item["queries"] for i in q["name_indices"]) == [0, 1, 2]
        assert item["names"][0]["origins"] == [
            {"kind": "CANONICAL_LABEL"},
            {"kind": "SOURCE_LABEL", "index": 0, "source": "CHEBI", "source_id": item["identifier"]},
        ]
        shared = item["names"][1]
        assert shared["origins"][0]["synonym_type"] == "RELATED_SYNONYM"
        expected = {"CHEBI:1", "CHEBI:2", "CHEBI:3"} - {item["identifier"]}
        assert set(shared["shared_with_record_ids"]) == expected
    assert len(docs) == len(planned)


def test_canonical_query_cache_keys_are_unchanged(cohort):
    _, out, _ = cohort
    for record in read_plan(out)["records"]:
        # Keep the pre-alias query contract independent of the shared helper.
        old = {
            "query": (
                f'TITLE_ABS:"{record["label"]}" AND '
                '(TITLE_ABS:resistan* OR TITLE_ABS:susceptib* OR TITLE_ABS:toleran*) AND '
                '(TITLE_ABS:gene OR TITLE_ABS:allele* OR TITLE_ABS:mutan* OR '
                'TITLE_ABS:mutation* OR TITLE_ABS:genetic* OR TITLE_ABS:genom*)'
            ),
            "format": "json", "resultType": "lite", "pageSize": 100,
            "cursorMark": "*", "synonym": "false",
        }
        new = aliases.discovery.params(record["queries"][0])
        assert old == new
        assert aliases.discovery.cache_path(old) == aliases.discovery.cache_path(new)


def test_names_preserve_case_stereochemistry_and_all_origins():
    names = aliases.record_names({
        "label": "(2R)-A", "synonyms": [
            {"synonym_text": "(2S)-A", "synonym_type": "EXACT_SYNONYM"},
            {"synonym_text": "(2R)-A", "synonym_type": "INN"},
            {"synonym_text": "(2R)-a", "synonym_type": "RELATED_SYNONYM"},
        ],
    })
    assert [n["text"] for n in names] == ["(2R)-A", "(2S)-A", "(2R)-a"]
    assert len(names[0]["origins"]) == 2


def test_or_queries_are_parenthesized_and_names_are_escaped():
    query = aliases.discovery.query_names(['A "quote"', r"B\C"])
    assert query.startswith('(TITLE_ABS:"A \\"quote\\"" OR TITLE_ABS:"B\\\\C") AND ')
    with pytest.raises(ValueError, match="empty name query"):
        aliases.discovery.query_names([])
    with pytest.raises(ValueError, match="invalid canonical label"):
        aliases.discovery.query_names(["valid", "invalid\nOR everything"])


def test_chunking_preserves_all_names_and_request_bounds():
    names = [{"text": "canonical"}] + [{"text": f"name-{i}-" + "(R)-" * 200} for i in range(10)]
    queries = aliases.make_queries(names)
    assert sorted(i for q in queries for i in q["name_indices"]) == list(range(11))
    for query in queries:
        assert len(query["name_indices"]) <= aliases.MAX_NAMES
        url = aliases.discovery.URL + "?" + urlencode(aliases.discovery.params(query))
        assert len(url.encode()) <= aliases.MAX_URL_BYTES


def test_oversized_name_is_not_silently_dropped(monkeypatch):
    monkeypatch.setattr(aliases, "MAX_URL_BYTES", 700)
    with pytest.raises(ValueError, match="single-name query exceeds"):
        aliases.make_queries([{"text": "small"}, {"text": "X" * 800}])


@pytest.mark.parametrize("change", ["omit_alias", "origin", "query", "sharing", "drop_record", "corpus_pin"])
def test_tampered_plan_fails_against_live_name_inventory(cohort, change):
    root, out, _ = cohort
    planned = read_plan(out)
    record = planned["records"][0]
    if change == "omit_alias":
        record["names"].pop()
    elif change == "origin":
        record["names"][1]["origins"][0]["synonym_type"] = "EXACT_SYNONYM"
    elif change == "query":
        record["queries"][0]["query"] = "different"
    elif change == "sharing":
        record["names"][1]["shared_with_record_ids"] = []
    elif change == "drop_record":
        planned["records"].pop()
    else:
        planned["corpus_sha256"] = "changed"
    aliases.common.write(aliases.PLAN, planned)
    with pytest.raises(ValueError, match="stale or altered"):
        aliases.load_plan(root)


def test_record_changed_during_collection_aware_read_is_rejected(cohort, monkeypatch):
    root, _, docs = cohort

    def load(path):
        path.write_text("changed")
        return docs[path]

    monkeypatch.setattr(aliases, "load_record", load)
    with pytest.raises(ValueError, match="record changed"):
        aliases.build_plan(root)


def test_bound_and_resume_visit_one_query_per_record_per_round(cohort, monkeypatch):
    root, out, _ = cohort
    planned = read_plan(out)
    for record in planned["records"]:
        cache(record["queries"][0])
    calls = []

    def fetch(parameters, session=None):
        path = aliases.discovery.cache_path(parameters)
        if not path.exists():
            calls.append(parameters["query"])
            cache(parameters)
        return json.loads(path.read_bytes())

    monkeypatch.setattr(aliases.discovery, "fetch", fetch)
    aliases.search(root, 1, [])
    aliases.search(root, 1, [])
    assert calls == [record["queries"][1]["query"] for record in planned["records"][:2]]
    aliases.analyze(root)
    results = json.loads((out / aliases.CANDIDATES).read_bytes())
    assert results["summary"]["records"] == 3
    expected = {"ALL_INITIAL_NAME_QUERIES_SEARCHED": 2, "PARTIAL": 1}
    assert results["summary"]["record_search_status"] == expected


def test_source_qualified_deduplication_does_not_imply_primary_evidence(cohort):
    root, out, _ = cohort
    record = read_plan(out)["records"][0]
    cache(record["queries"][0], [("MED", "1")])
    cache(record["queries"][1], [("MED", "1"), ("MED", "2"), ("PMC", "1")])
    aliases.analyze(root)
    item = json.loads((out / aliases.CANDIDATES).read_bytes())["records"][0]
    assert item["candidate_ids"] == ["MED:1", "MED:2", "PMC:1"]
    assert item["added_vs_canonical_retained_ids"] == ["MED:2", "PMC:1"]
    assert item["primary_review_status"] == "PENDING"
    assert item["queries"][1]["name_indices"] == [2, 1]


def test_missing_canonical_comparison_stays_unknown_and_truncation_visible(cohort):
    root, out, _ = cohort
    record = read_plan(out)["records"][0]
    cache(record["queries"][1], [("MED", str(i)) for i in range(101)])
    item = aliases.analyze_record(record)
    assert item["search_status"] == "PARTIAL"
    assert item["added_vs_canonical_retained_ids"] is None
    assert item["queries"][1]["status"] == "TRUNCATED_REFINEMENT_REQUIRED"
    assert len(item["candidate_ids"]) == 100
    aliases.analyze(root)
    with (out / aliases.LEDGER).open() as handle:
        row = next(csv.DictReader(handle, delimiter="\t"))
    assert row["canonical_query_status"] == "NOT_SEARCHED"
    assert row["added_vs_canonical_retained_ids"] == ""


@pytest.mark.parametrize("maximum,only", [(0, []), (-1, []), (1, ["CHEBI:999"])])
def test_invalid_bound_or_identifier_cannot_make_requests(cohort, monkeypatch, maximum, only):
    root, _, _ = cohort

    def fetch(*args, **kwargs):
        pytest.fail("No query may run for invalid scope")

    monkeypatch.setattr(aliases.discovery, "fetch", fetch)
    with pytest.raises(ValueError, match="invalid request bound or unknown cohort"):
        aliases.search(root, maximum, only)


def test_changed_plan_mid_search_is_rejected(cohort, monkeypatch):
    root, _, _ = cohort

    def fetch(parameters, session=None):
        aliases.common.write(aliases.PLAN, {"changed": True})
        return response(parameters)

    monkeypatch.setattr(aliases.discovery, "fetch", fetch)
    with pytest.raises(ValueError, match="inputs changed"):
        aliases.search(root, 1, [])


def test_offline_mode_cannot_request_uncached_queries(cohort):
    root, _, _ = cohort
    with pytest.raises(ValueError, match="network is disabled"):
        aliases.search(root, 1, [])


def test_empty_corpus_still_writes_header_only_ledger(cohort, monkeypatch):
    root, out, _ = cohort
    monkeypatch.setattr(aliases.discovery.card, "current_corpus", lambda _: [])
    aliases.common.write("corpus.json", {"records": []})
    aliases.plan(root)
    aliases.analyze(root)
    result = json.loads((out / aliases.CANDIDATES).read_bytes())
    assert result["records"] == [] and result["summary"]["queries"] == 0
    with (out / aliases.LEDGER).open() as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        assert tuple(reader.fieldnames) == aliases.LEDGER_FIELDS
        assert list(reader) == []
