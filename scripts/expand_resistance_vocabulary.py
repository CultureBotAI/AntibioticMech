"""Expand v2 citation searches without rewriting historical names or record pins.

The live corpus must match a current census and every historical query-name
projection. Fresh date-sorted cursor chains stay separate from initial pages,
v1 searches, primary evidence review and biological grounding.
"""

import argparse
import csv
import json
from collections import Counter, defaultdict
from itertools import zip_longest
from pathlib import Path

import expand_resistance_discovery as expansion
import summarize_resistance_vocabulary as union

from antibioticmech.activity_collections import load_record

aliases = expansion.aliases
discovery = expansion.discovery
common = expansion.common
PROFILE = aliases.IMMUNITY_PROFILE
SORT = "P_PDATE_D desc"
CRITERIA = "truncated-immunity-v2-date-sorted-citation-expansion-v1"
PLAN = "vocabulary-expansion-plan.json"
CANDIDATES = "vocabulary-expansion-candidates.json"
LEDGER = "vocabulary-expansion-ledger.tsv"
SCOPE = "CITATION_DISCOVERY_ONLY; NO_COMPOUND_ALLELE_OR_AST_ASSIGNMENTS"
LIMITATIONS = [*expansion.EXPORT_LIMITATIONS,
    "V2 is the broader genetics/immunity vocabulary, not completion of historical v1 searches.",
    "Date ordering and query-local traversal do not establish a stable index or prevent all conflicts.",
    "Historical record hashes are preserved; a current name/identity bridge is not biological review.",
    "Short aliases and stop words remain ambiguous; large result counts are not relevance estimates.",
    "Historical citation identities must be preserved separately, not discarded when live results differ.",
]


def pin(root, path):
    path = root / path
    return {"path": str(path.resolve().relative_to(root.resolve())),
            "sha256": common.digest(path.read_bytes())}


def checked_input(root, expected):
    value, actual = union.read_pinned(root, expected["path"])
    if any(actual[k] != v for k, v in expected.items() if k in actual):
        raise ValueError("pinned discovery input changed")
    if "sha256" not in expected:
        raise ValueError("missing discovery input checksum")
    return value


def name_bridge(root, historical, census_path):
    before = pin(root, census_path)
    with (root / census_path).open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    census = union.index_records(rows)
    previous = union.index_records(historical["records"])
    paths = {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
    if (set(census) != set(previous) or paths != {r["path"] for r in rows}
            or len(paths) != len(rows)):
        raise ValueError("current corpus membership drift")
    names, owners, hashes = {}, defaultdict(list), {}
    for identifier, row in census.items():
        path = root / row["path"]
        digest = common.digest(path.read_bytes())
        if digest != row["record_sha256"]:
            raise ValueError("current census record checksum drift")
        doc = load_record(path)
        live = {"identifier": doc["identifier"], "label": doc["label"], "path": row["path"],
                "standard_inchi_key": doc["chemical_structure"]["standard_inchi_key"],
                "class": doc["antimicrobial_class"]}
        if any(live[k] != row[k] for k in union.IDENTITY if k != "class"):
            raise ValueError("current census identity drift")
        union.same_identity(live, previous[identifier])
        hashes[row["path"]] = digest
        names[identifier] = aliases.record_names(doc)
        for name in names[identifier]:
            owners[name["text"]].append(identifier)
    for identifier, entries in names.items():
        for name in entries:
            name["shared_with_record_ids"] = sorted(i for i in owners[name["text"]] if i != identifier)
        if (entries != previous[identifier]["names"]
                or aliases.make_queries(entries, profile=PROFILE) != previous[identifier]["queries"]):
            raise ValueError("historical query-name projection drift")
    if pin(root, census_path) != before:
        raise ValueError("census changed while checking names")
    verify_records(root, hashes)
    return hashes, {
        "current_census": before, "records_verified": len(rows),
        "names_verified": sum(map(len, names.values())),
        "queries_verified": sum(len(r["queries"]) for r in previous.values()),
        "record_hashes_changed_since_historical_plan": sum(
            r["record_sha256"] != previous[i]["sha256"] for i, r in census.items()),
        "historical_record_pins_rewritten": False, "ignored_files_included": True,
        "scope": "CURRENT_NAME_AND_CHEMICAL_IDENTITY_BRIDGE_NOT_BIOLOGICAL_REVIEW",
    }


def verify_records(root, hashes):
    paths = {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
    if paths != set(hashes) or any(common.digest((root / p).read_bytes()) != h for p, h in hashes.items()):
        raise ValueError("current record changed during expansion")


def eligible_queries(planned, found):
    union.current_memberships(planned, found)
    searched = union.index_records(found["records"])
    queries = {}
    for layer in zip_longest(*(r["queries"] for r in planned["records"])):
        for record, query in zip(planned["records"], layer, strict=True):
            if query is None:
                continue
            result, = [q for q in searched[record["identifier"]]["queries"]
                       if q["query_id"] == query["query_id"]]
            if result["hit_count"] <= discovery.PAGE_SIZE:
                continue
            key = common.digest(query["query"].encode())
            item = queries.setdefault(key, {
                "query_key": key, "query": query["query"], "members": [],
                "baseline_hit_count": result["hit_count"],
                "baseline_candidate_ids": sorted(union.citation_ids(result["candidates"])),
                "baseline_request": result["request"],
            })
            item["members"].append({
                **{k: record[k] for k in aliases.IDENTITY_FIELDS},
                **{k: query[k] for k in ("query_id", "kind", "name_indices")},
                "names": [record["names"][i] for i in query["name_indices"]],
            })
    groups = defaultdict(list)
    for query in queries.values():
        groups[query["members"][0]["class"]].append(query)
    return [q for layer in zip_longest(*(groups[k] for k in sorted(groups))) for q in layer if q]


def build_plan(root, initial_descriptor, census):
    descriptor_pin = pin(root, initial_descriptor)
    descriptor = json.loads((root / initial_descriptor).read_bytes())
    if descriptor["criteria"] != PROFILE.criteria:
        raise ValueError("initial descriptor is not the immunity-v2 vocabulary")
    planned = checked_input(root, descriptor["plan"])
    found = checked_input(root, descriptor["candidate_index"])
    plan_path = root / descriptor["plan"]["path"]
    _, plan_pin = union.read_pinned(root, str(plan_path.relative_to(root)))
    if found["plan_sha256"] != plan_pin["uncompressed_sha256"]:
        raise ValueError("initial candidate/plan checksum drift")
    queries = eligible_queries(planned, found)
    hashes, bridge = name_bridge(root, planned, census)
    result = {
        "criteria": CRITERIA, "vocabulary": "immunity-v2", "page_size": expansion.PAGE_SIZE,
        "requested_sort": SORT, "traversal_order": "query-local", "scope": SCOPE,
        "initial_descriptor": descriptor_pin, "historical_name_plan": descriptor["plan"],
        "initial_candidates": descriptor["candidate_index"], "current_census": bridge["current_census"],
        "historical_corpus_sha256": planned["corpus_sha256"], "name_bridge": bridge,
        "current_record_hashes": hashes, "corpus_records": len(hashes), "queries": queries,
        "limitations": LIMITATIONS,
    }
    verify_inputs(root, result)
    return result


def verify_inputs(root, planned):
    for name in ("initial_descriptor", "historical_name_plan", "initial_candidates", "current_census"):
        expected = planned[name]
        if pin(root, expected["path"])["sha256"] != expected["sha256"]:
            raise ValueError("vocabulary expansion input changed")
    verify_records(root, planned["current_record_hashes"])


def freeze(path, value):
    payload = (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()
    if path.exists() and path.read_bytes() != payload:
        raise ValueError("refusing to replace a different frozen expansion artifact")
    path.write_bytes(payload)


def load_plan(root):
    raw = (common.OUT / PLAN).read_bytes()
    planned = json.loads(raw)
    expected = build_plan(root, planned["initial_descriptor"]["path"], planned["current_census"]["path"])
    if planned != expected:
        raise ValueError("stale or altered vocabulary expansion plan")
    return planned, common.digest(raw)


def unchanged(root, planned, plan_hash):
    if common.digest((common.OUT / PLAN).read_bytes()) != plan_hash:
        raise ValueError("vocabulary expansion plan changed")
    verify_inputs(root, planned)


def search(root, maximum, only):
    if type(maximum) is not int or maximum < 1:
        raise ValueError("invalid page bound")
    planned, plan_hash = load_plan(root)
    if set(only) - {q["query_key"] for q in planned["queries"]}:
        raise ValueError("unknown truncated-query key")
    fresh, states = 0, []
    try:
        with discovery.requests.Session() as session:
            for query in planned["queries"]:
                if only and query["query_key"] not in only:
                    continue
                state = expansion.analyze_query(query, allow_conflicts=True, sort=SORT)
                states.append(state)
                while state["next_cursor"] is not None and "rejected_page" not in state and fresh < maximum:
                    params = expansion.parameters(query, state["next_cursor"], sort=SORT)
                    cached = discovery.cache_path(params).exists()
                    discovery.fetch(params, session=session, retained_before=len(state["candidates"]),
                                    expected_count=state["hit_count"], expected_version=state["api_version"],
                                    cache_conflicts=True)
                    state.update(expansion.analyze_query(query, allow_conflicts=True, sort=SORT))
                    fresh += not cached
                    if not cached:
                        print(f"new page {fresh}/{maximum}: {query['members'][0]['identifier']} "
                              f"q{query['members'][0]['query_id']} "
                              f"{len(state['candidates'])}/{state['hit_count']} citations; "
                              f"{state['status']}", flush=True)
                if fresh == maximum:
                    break
    finally:
        unchanged(root, planned, plan_hash)
        expansion.unchanged_pages(states)
    print(json.dumps({"new_responses": fresh, "visited_queries": len(states),
        "maximum_attempts_per_new_page": 3,
        "conflicted_queries": sum("rejected_page" in s for s in states)}), flush=True)


def analyze(root):
    planned, plan_hash = load_plan(root)
    queries = [expansion.analyze_query(q, allow_conflicts=True, sort=SORT) for q in planned["queries"]]
    summary = {
        "corpus_records": planned["corpus_records"], "unique_queries": len(queries),
        "query_record_memberships": sum(len(q["members"]) for q in queries),
        "records_with_truncated_queries": len({m["identifier"] for q in queries for m in q["members"]}),
        "query_status": dict(Counter(q["status"] for q in queries)),
        "cached_pages": sum(len(q["pages"]) for q in queries),
        "rejected_cached_pages": sum("rejected_page" in q for q in queries),
        "retained_query_citation_memberships": sum(len(q["candidates"]) for q in queries),
        "unique_retained_citations": len({(c["source"], c["id"]) for q in queries for c in q["candidates"]}),
        "queries_with_hit_count_drift": sum(q["hit_count_delta"] not in (None, 0) for q in queries),
    }
    unchanged(root, planned, plan_hash)
    expansion.unchanged_pages(queries)
    common.write(CANDIDATES, {"criteria": CRITERIA, "plan_sha256": plan_hash, "scope": SCOPE,
        "requested_sort": SORT, "name_bridge": planned["name_bridge"], "summary": summary,
        "queries": queries, "limitations": LIMITATIONS})
    with (common.OUT / LEDGER).open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=(*expansion.LEDGER_FIELDS, "requested_sort"),
                                delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for query in queries:
            for member in query["members"]:
                writer.writerow({**{k: member[k] for k in ("identifier", "query_id")},
                    **{k: query[k] for k in ("query_key", "status", "baseline_hit_count", "hit_count",
                                           "primary_review_status", "requested_sort")},
                    "pages": len(query["pages"]), "retained_citations": len(query["candidates"]),
                    "added_vs_original_query_page": len(query["added_vs_original_query_page_ids"])
                    if query["pages"] else None})
    print(json.dumps(summary, sort_keys=True), flush=True)
    return summary


def positive_integer(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("page bound must be positive")
    return number


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("plan", "search", "analyze"))
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--initial-descriptor", type=Path)
    parser.add_argument("--census", type=Path)
    parser.add_argument("--allow-network", action="store_true")
    parser.add_argument("--max-new-pages", type=positive_integer, default=25)
    parser.add_argument("--only-query", action="append", default=[])
    args = parser.parse_args()
    if args.stage == "plan" and (args.initial_descriptor is None or args.census is None):
        parser.error("planning requires --initial-descriptor and --census")
    if args.allow_network and args.stage != "search":
        parser.error("network is only available during search")
    common.OUT, common.ALLOW_NETWORK = args.output_dir.resolve(), args.allow_network
    common.OUT.mkdir(parents=True, exist_ok=True)
    root = args.root.resolve()
    if args.stage == "plan":
        result = build_plan(root, args.initial_descriptor, args.census)
        freeze(common.OUT / PLAN, result)
        print(json.dumps({"queries": len(result["queries"]),
                          "name_bridge": result["name_bridge"]}), flush=True)
    elif args.stage == "search":
        search(root, args.max_new_pages, args.only_query)
    else:
        analyze(root)
