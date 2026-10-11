"""Bounded citation-only cursor expansion of truncated all-record name queries.

Fresh 1000-citation pages never mix with the historical 100-citation pages.
Traversal completion is not a stable database snapshot or primary-paper review.
"""

import argparse
import csv
import gzip
import io
import json
import tempfile
from collections import Counter, defaultdict
from itertools import zip_longest
from pathlib import Path

import discover_resistance_aliases as aliases

discovery = aliases.discovery
common = aliases.common
PAGE_SIZE = 1000
CRITERIA = "truncated-name-query-citation-cursor-expansion-v1"
PLAN = "discovery-expansion-plan.json"
CANDIDATES = "discovery-expansion-candidates.json"
LEDGER = "discovery-expansion-ledger.tsv"
CONFLICT_STATUS = "CURSOR_CONFLICT_REQUIRES_RESTART"
LEDGER_FIELDS = (
    "identifier", "query_id", "query_key", "status", "baseline_hit_count", "hit_count",
    "pages", "retained_citations", "added_vs_original_query_page", "primary_review_status",
)
LIMITATIONS = [
    "Queries are unchanged name-co-occurrence searches, not exact compound or biological evidence.",
    "The 1000-row cursor chain is separate from historical 100-row caches; counts may change.",
    "Completion means unique rows equal the reported hit count across consistent cached pages.",
    "Europe PMC is live: consistent counts and API versions do not prove an atomic index snapshot.",
    "Added citations are relative to one original query page, not all citations for the record.",
    "A shared query retains each record/name membership without merging chemical identities.",
    "No abstracts, full text, sequences, new gene/allele, protein, taxon or AST assignments exported.",
    "All candidates require primary review; search completion does not establish biological absence.",
]
EXPORT_LIMITATIONS = LIMITATIONS + [
    "A conflicting page is rejected in full and pinned separately; only its valid prefix is retained.",
    "Conflicted queries remain incomplete and are not retried by resuming the same cursor chain.",
]


def parameters(query, cursor="*", *, sort=None):
    result = dict(discovery.params(query), pageSize=PAGE_SIZE, cursorMark=cursor)
    if sort is not None:
        if sort != "P_PDATE_D desc":
            raise ValueError("unsupported citation traversal sort")
        result["sort"] = sort
    return result


def baseline_inputs(planned):
    paths = {discovery.cache_path(discovery.params(q)) for r in planned["records"]
             for q in r["queries"]}
    return common.digest(json.dumps(
        {p.name: common.digest(p.read_bytes()) for p in sorted(paths)}, sort_keys=True,
    ).encode())


def build_plan(root):
    planned, alias_hash = aliases.load_plan(root)
    before = baseline_inputs(planned)
    queries = {}
    records = planned["records"]
    # One query per record per layer, retaining the existing class-balanced order.
    for layer in zip_longest(*(r["queries"] for r in records)):
        for record, query in zip(records, layer, strict=True):
            if query is None:
                continue
            params = discovery.params(query)
            path = discovery.cache_path(params)
            raw = path.read_bytes()
            response = json.loads(raw)
            payload = discovery.validate(response, params)
            if payload["hitCount"] <= discovery.PAGE_SIZE:
                continue
            key = common.digest(query["query"].encode())
            entry = queries.setdefault(key, {
                "query_key": key, "query": query["query"], "members": [],
                "baseline_cache": path.name, "baseline_cache_sha256": common.digest(raw),
                "baseline_hit_count": payload["hitCount"],
                "baseline_candidate_ids": [r["source"] + ":" + r["id"]
                                           for r in payload["resultList"]["result"]],
            })
            entry["members"].append({
                **{k: record[k] for k in aliases.IDENTITY_FIELDS},
                **{k: query[k] for k in ("query_id", "kind", "name_indices")},
                "names": [record["names"][i] for i in query["name_indices"]],
            })
    aliases.unchanged(root, planned, alias_hash)
    if baseline_inputs(planned) != before:
        raise ValueError("initial discovery caches changed during planning")
    groups = defaultdict(list)
    for query in queries.values():
        groups[query["members"][0]["class"]].append(query)
    # Filtering can destroy the original class balance; rebalance eligible queries.
    balanced = [q for layer in zip_longest(*(groups[k] for k in sorted(groups))) for q in layer if q]
    return {
        "criteria": CRITERIA, "page_size": PAGE_SIZE, "alias_plan_sha256": alias_hash,
        "corpus_sha256": planned["corpus_sha256"], "corpus_records": len(records),
        "baseline_inputs_sha256": before, "queries": balanced,
        "limitations": LIMITATIONS,
    }


def plan(root):
    result = build_plan(root)
    common.write(PLAN, result)
    print(f"Planned {len(result['queries'])} unique truncated queries", flush=True)


def load_plan(root):
    raw = (common.OUT / PLAN).read_bytes()
    result = json.loads(raw)
    if result != build_plan(root):
        raise ValueError("stale or altered expansion plan")
    return result, common.digest(raw)


def unchanged(root, planned, plan_hash):
    aliases_plan = json.loads((common.OUT / aliases.PLAN).read_bytes())
    aliases.unchanged(root, aliases_plan, planned["alias_plan_sha256"])
    if (common.digest((common.OUT / PLAN).read_bytes()) != plan_hash
            or baseline_inputs(aliases_plan) != planned["baseline_inputs_sha256"]):
        raise ValueError("expansion inputs changed during processing")


def analyze_query(query, *, allow_conflicts=False, sort=None):
    candidates, pages, seen, cursors = [], [], set(), set()
    cursor, count, version = "*", None, None
    rejected_page = None
    while True:
        if cursor in cursors:
            raise ValueError("repeated cursor before traversal completion")
        cursors.add(cursor)
        params = parameters(query, cursor, sort=sort)
        path = discovery.cache_path(params)
        if not path.exists():
            break
        raw = path.read_bytes()
        response = json.loads(raw)
        conflict = None
        try:
            payload = discovery.validate(response, params, retained_before=len(candidates),
                                         expected_count=count, expected_version=version)
        except discovery.CitationPageConflict as error:
            if not allow_conflicts:
                raise
            payload = error.payload
            conflict = {"reason": error.reason, "expected_hit_count": count,
                        "reported_hit_count": payload["hitCount"], "expected_api_version": version,
                        "expected_returned_citations": min(PAGE_SIZE, (payload["hitCount"]
                         if count is None else count) - len(candidates))}
        rows = payload["resultList"]["result"]
        page = {
            "cache": path.name, "cache_sha256": common.digest(raw),
            "request": {k: v for k, v in response.items() if k not in ("body", "headers")},
            "api_version": payload["version"], "retained_citations": len(rows),
            "next_cursor": payload.get("nextCursorMark"),
        }
        identifiers = {row["source"] + ":" + row["id"] for row in rows}
        repeated = seen & identifiers
        if conflict or repeated:
            if not allow_conflicts:
                raise ValueError("repeated publication across cursor pages")
            # Preserve the response, but never salvage unique rows from an invalid page.
            rejected_page = dict(page, **(conflict or {"reason": "CROSS_PAGE_PUBLICATION_OVERLAP"}),
                                 accepted_prefix_citations=len(candidates))
            if repeated:
                rejected_page["repeated_publication_ids"] = sorted(repeated)
            rejected_page["returned_citations"] = rejected_page.pop("retained_citations")
            break
        count, version = payload["hitCount"], payload["version"]
        seen.update(identifiers)
        candidates.extend({k: row[k] for k in discovery.CITATION_FIELDS if k in row} for row in rows)
        pages.append(page)
        if len(candidates) == count:
            cursor = None
            break
        cursor = payload["nextCursorMark"]
        if not isinstance(cursor, str) or not cursor:
            raise ValueError("invalid continuation cursor")
    result = dict(query, pages=pages, candidates=candidates, hit_count=count, api_version=version,
                  next_cursor=cursor, primary_review_status="PENDING",
                  status=CONFLICT_STATUS if rejected_page else "NOT_STARTED" if not pages
                  else "CURSOR_TRAVERSAL_COMPLETE" if cursor is None else "PARTIAL_CURSOR_TRAVERSAL",
                  hit_count_delta=None if count is None else count - query["baseline_hit_count"],
                  added_vs_original_query_page_ids=sorted(seen - set(query["baseline_candidate_ids"])))
    if rejected_page:
        result["rejected_page"] = rejected_page
    if sort is not None:
        result["requested_sort"] = sort
    return result


def unchanged_pages(queries):
    for query in queries:
        pages = query["pages"] + ([query["rejected_page"]] if "rejected_page" in query else [])
        for page in pages:
            if common.digest((common.OUT / page["cache"]).read_bytes()) != page["cache_sha256"]:
                raise ValueError("expansion page cache changed during processing")


def search(root, maximum, only, *, traversal_order="breadth-first"):
    if traversal_order not in ("breadth-first", "query-local"):
        raise ValueError("invalid traversal order")
    planned, plan_hash = load_plan(root)
    ids = {m["identifier"] for q in planned["queries"] for m in q["members"]}
    if type(maximum) is not int or maximum < 1 or set(only) - ids:
        raise ValueError("invalid page bound or unknown truncated-query record")
    selected = [q for q in planned["queries"]
                if not only or any(m["identifier"] in only for m in q["members"])]
    states = [analyze_query(q, allow_conflicts=True) for q in selected]
    fresh = 0
    try:
        with discovery.requests.Session() as session:
            while fresh < maximum:
                pending = [s for s in states if s["next_cursor"] is not None and "rejected_page" not in s]
                if not pending:
                    break
                # Query-local order shortens inter-page gaps without changing query semantics.
                state = (pending[0] if traversal_order == "query-local"
                         else min(pending, key=lambda s: len(s["pages"])))
                query = next(q for q in selected if q["query_key"] == state["query_key"])
                params = parameters(query, state["next_cursor"])
                cached = discovery.cache_path(params).exists()
                discovery.fetch(params, session=session, retained_before=len(state["candidates"]),
                                expected_count=state["hit_count"], expected_version=state["api_version"],
                                cache_conflicts=True)
                state.update(analyze_query(query, allow_conflicts=True))
                if not cached:
                    fresh += 1
                    print(f"new page {fresh}/{maximum}: {query['members'][0]['identifier']} "
                          f"q{query['members'][0]['query_id']} "
                          f"{len(state['candidates'])}/{state['hit_count']} citations; "
                          f"{state['status']}", flush=True)
    finally:
        unchanged(root, planned, plan_hash)
        unchanged_pages(states)
    conflicts = sum("rejected_page" in state for state in states)
    print(f"Expansion checkpoint: {fresh} new responses (at most three HTTP attempts/page); "
          f"{conflicts} conflicted queries require a separate restart", flush=True)


def analyze(root):
    planned, plan_hash = load_plan(root)
    queries = [analyze_query(q, allow_conflicts=True) for q in planned["queries"]]
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
    unchanged_pages(queries)
    common.write(CANDIDATES, {
        "criteria": CRITERIA, "plan_sha256": plan_hash, "corpus_sha256": planned["corpus_sha256"],
        "scope": "CITATION_DISCOVERY_ONLY; NO_COMPOUND_ALLELE_OR_AST_ASSIGNMENTS",
        "summary": summary, "queries": queries, "limitations": EXPORT_LIMITATIONS,
    })
    with (common.OUT / LEDGER).open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=LEDGER_FIELDS, delimiter="\t")
        writer.writeheader()
        for query in queries:
            for member in query["members"]:
                writer.writerow({
                    **{k: member[k] for k in ("identifier", "query_id")},
                    **{k: query[k] for k in ("query_key", "status", "baseline_hit_count", "hit_count",
                                           "primary_review_status")},
                    "pages": len(query["pages"]), "retained_citations": len(query["candidates"]),
                    "added_vs_original_query_page": len(query["added_vs_original_query_page_ids"])
                    if query["pages"] else None,
                })
    print(json.dumps(summary, sort_keys=True), flush=True)


def write_compressed_candidate_export(source, target):
    """Publish exact candidate bytes with separate stored and expanded checksums."""
    source, target = Path(source), Path(target)
    if source.resolve() == target.resolve():
        raise ValueError("compressed export must not replace its source")
    payload = source.read_bytes()
    buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=buffer, mode="wb", filename="", mtime=0) as stream:
        stream.write(payload)
    stored = buffer.getvalue()
    if gzip.decompress(stored) != payload:
        raise ValueError("compressed export failed byte-for-byte verification")
    if source.read_bytes() != payload:
        raise ValueError("candidate source changed during compression")
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".candidate-export-", dir=target.parent) as directory:
        temporary = Path(directory) / "candidate.json.gz"
        temporary.write_bytes(stored)
        if temporary.read_bytes() != stored:
            raise ValueError("compressed export changed before publication")
        if source.read_bytes() != payload:
            raise ValueError("candidate source changed before publication")
        temporary.replace(target)
    return {
        "encoding": "gzip", "sha256": common.digest(stored), "stored_bytes": len(stored),
        "uncompressed_sha256": common.digest(payload), "uncompressed_bytes": len(payload),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("plan", "search", "analyze"))
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--allow-network", action="store_true")
    parser.add_argument("--max-new-pages", type=int, default=25,
                        help="Bound new responses, including rejected pages; at most three attempts each")
    parser.add_argument("--only", action="append", default=[])
    parser.add_argument("--traversal-order", choices=("breadth-first", "query-local"),
                        default="breadth-first",
                        help="Query-local finishes each eligible chain before advancing to the next")
    args = parser.parse_args()
    common.OUT = args.output_dir.resolve()
    common.OUT.mkdir(parents=True, exist_ok=True)
    common.ALLOW_NETWORK = args.allow_network
    if args.stage == "search":
        search(args.root.resolve(), args.max_new_pages, args.only,
               traversal_order=args.traversal_order)
    else:
        globals()[args.stage](args.root.resolve())
