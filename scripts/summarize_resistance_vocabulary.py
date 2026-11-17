"""Preserve source-qualified citation identities across discovery vocabularies.

Offline only. A union of discovery histories is not a cursor traversal, evidence
review, chemical match, biological replicate count or resistance assignment.
"""

import argparse
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

import discover_resistance_aliases as aliases

HISTORY = (
    "research/2026-10-07-resistance-discovery-candidates.json",
    "research/2026-10-07-resistance-discovery-current-candidates.json",
    "research/2026-10-08-resistance-alias-discovery-candidates.json",
    "research/2026-10-08-resistance-discovery-expansion-candidates.json.gz",
    "research/2026-10-09-resistance-discovery-restart-candidates.json.gz",
    "research/2026-10-09-resistance-discovery-query-local-candidates.json.gz",
    "research/2026-10-09-resistance-discovery-date-sort-candidates.json.gz",
)
IDENTITY = ("identifier", "label", "path", "standard_inchi_key", "class")
SCOPE = "CITATION_IDENTITY_UNION_NOT_ONE_CURSOR_CHAIN_OR_PRIMARY_REVIEW"


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def read_pinned(root, name):
    path = root / name
    stored = path.read_bytes()
    payload = gzip.decompress(stored) if path.suffix == ".gz" else stored
    return json.loads(payload), {
        "path": str(name), "sha256": digest(stored), "stored_bytes": len(stored),
        "uncompressed_sha256": digest(payload), "uncompressed_bytes": len(payload),
    }


def index_records(rows):
    result = {r["identifier"]: r for r in rows}
    if len(result) != len(rows) or not result:
        raise ValueError("empty or duplicate record membership")
    return result


def same_identity(current, previous, *, current_snapshot=False):
    fields = (*IDENTITY, "sha256") if current_snapshot else IDENTITY
    if any(current[k] != previous[k] for k in fields):
        raise ValueError("record identity drift")


def citation_ids(candidates):
    result = []
    for candidate in candidates:
        source, identifier = candidate["source"], candidate["id"]
        if any(not isinstance(v, str) or not v or any(c in v for c in "|\n\r\t")
               for v in (source, identifier)) or ":" in source:
            raise ValueError("invalid source-qualified citation identity")
        if set(candidate) - set(aliases.discovery.CITATION_FIELDS):
            raise ValueError("unexpected non-bibliographic candidate field")
        result.append(source + ":" + identifier)
    if len(set(result)) != len(result):
        raise ValueError("duplicate citation in a query")
    return set(result)


def historical_memberships(payload, records):
    result = {identifier: set() for identifier in records}
    if "records" in payload:
        for identifier, old in index_records(payload["records"]).items():
            if identifier not in records:
                raise ValueError("unknown historical record")
            same_identity(records[identifier], old)
            queries = old.get("queries", [old])
            retained = set().union(*(citation_ids(q["candidates"]) for q in queries))
            if "candidate_ids" in old and sorted(retained) != old["candidate_ids"]:
                raise ValueError("historical record citation summary drift")
            result[identifier].update(retained)
    else:
        seen = set()
        for query in payload["queries"]:
            key = query["query_key"]
            if key in seen or digest(query["query"].encode()) != key:
                raise ValueError("duplicate or altered historical query")
            seen.add(key)
            retained = citation_ids(query["candidates"])
            members = index_records(query["members"])
            for identifier, member in members.items():
                if identifier not in records:
                    raise ValueError("unknown historical query member")
                same_identity(records[identifier], member)
                result[identifier].update(retained)
            # Only accepted candidates are used, never rows from a rejected page.
            if ("rejected_page" in query
                    and query["rejected_page"]["accepted_prefix_citations"] != len(retained)):
                raise ValueError("rejected-page prefix drift")
    return result


def current_memberships(plan, found):
    records = index_records(plan["records"])
    searched = index_records(found["records"])
    if (plan["criteria"] != aliases.IMMUNITY_PROFILE.criteria
            or found["criteria"] != plan["criteria"]
            or plan["corpus_sha256"] != found["corpus_sha256"]
            or set(records) != set(searched)):
        raise ValueError("vocabulary plan or membership drift")
    result, shared, statuses = {}, {}, Counter()
    for identifier, record in records.items():
        current = searched[identifier]
        same_identity(record, current, current_snapshot=True)
        queries = aliases.make_queries(record["names"], profile=aliases.IMMUNITY_PROFILE)
        if (record["queries"] != queries or current["names"] != record["names"]
                or len(current["queries"]) != len(queries)
                or current["search_status"] != "ALL_INITIAL_NAME_QUERIES_SEARCHED"
                or current["searched_queries"] != len(queries)
                or current["primary_review_status"] != "PENDING"):
            raise ValueError("changed or incomplete initial vocabulary search")
        result[identifier] = set()
        for expected, query in zip(queries, current["queries"], strict=True):
            if any(query[k] != v for k, v in expected.items()):
                raise ValueError("vocabulary query identity drift")
            ids = citation_ids(query["candidates"])
            count = query["hit_count"]
            if type(count) is not int or count < 0 or len(ids) != min(count, 100):
                raise ValueError("invalid initial-page count")
            status = ("NO_HITS_IN_LIMITED_QUERY" if count == 0 else
                      "TRUNCATED_REFINEMENT_REQUIRED" if count > 100 else "CANDIDATES_REQUIRE_REVIEW")
            if query["status"] != status:
                raise ValueError("invalid initial-page status")
            request = query["request"]
            location, endpoint = urlparse(request["url"]), urlparse(aliases.discovery.URL)
            if ((location.scheme, location.netloc, location.path)
                    != (endpoint.scheme, endpoint.netloc, endpoint.path)
                    or location.fragment or request["status"] != 200
                    or request["params"] != aliases.discovery.params(expected)):
                raise ValueError("unexpected citation request")
            state = (count, sorted(ids), query["request"])
            if shared.setdefault(query["query"], state) != state:
                raise ValueError("shared query response differs")
            statuses[status] += 1
            result[identifier].update(ids)
        if current["candidate_ids"] != sorted(result[identifier]):
            raise ValueError("vocabulary record citation summary drift")
    if found["summary"]["query_status"] != dict(statuses):
        raise ValueError("vocabulary query status summary drift")
    return result, dict(statuses), len(shared)


def build_union(root, plan_path, candidates_path, *, history=HISTORY):
    plan, plan_pin = read_pinned(root, plan_path)
    found, found_pin = read_pinned(root, candidates_path)
    if found["plan_sha256"] != plan_pin["uncompressed_sha256"]:
        raise ValueError("vocabulary plan checksum drift")
    records = index_records(plan["records"])
    current, statuses, distinct_queries = current_memberships(plan, found)
    previous = {identifier: set() for identifier in records}
    pins, summaries = [], []
    for name in history:
        payload, pin = read_pinned(root, name)
        memberships = historical_memberships(payload, records)
        pins.append(pin)
        summaries.append({"path": str(name), "distinct_citations": len(set().union(*memberships.values())),
                          "record_citation_memberships": sum(map(len, memberships.values()))})
        for identifier, ids in memberships.items():
            previous[identifier].update(ids)
    rows = []
    for identifier, record in records.items():
        old, new = previous[identifier], current[identifier]
        rows.append({
            **{k: record[k] for k in (*IDENTITY, "sha256")},
            "historical_candidate_ids": sorted(old), "v2_candidate_ids": sorted(new),
            "union_candidate_ids": sorted(old | new), "added_vs_history_ids": sorted(new - old),
            "historical_ids_not_in_v2_initial_pages": sorted(old - new),
            "primary_review_status": "PENDING",
        })
    before, after = set().union(*previous.values()), set().union(*current.values())
    return {
        "scope": SCOPE, "plan": plan_pin, "initial_candidates": found_pin,
        "historical_inputs": pins, "historical_input_summaries": summaries,
        "summary": {
            "records": len(rows), "query_memberships": sum(statuses.values()),
            "distinct_queries": distinct_queries, "query_status": statuses,
            "historical_distinct_citations": len(before), "v2_distinct_citations": len(after),
            "union_distinct_citations": len(before | after),
            "v2_distinct_citations_not_in_history": len(after - before),
            "historical_distinct_citations_not_in_v2_initial_pages": len(before - after),
            "records_with_added_citations": sum(bool(r["added_vs_history_ids"]) for r in rows),
            "historical_record_citation_memberships": sum(map(len, previous.values())),
            "v2_record_citation_memberships": sum(map(len, current.values())),
            "union_record_citation_memberships": sum(len(r["union_candidate_ids"]) for r in rows),
            "historical_memberships_lost": 0,
        },
        "limitations": [
            "This union retains accepted historical prefixes; it does not splice cursor chains.",
            "Different source-qualified citation identities are not independent biological replicates.",
            "Name co-occurrence and shared aliases do not establish exact compound identity.",
            "V2 stores only initial pages; truncated queries remain open for separate traversal.",
            "Live-index changes and ranking affect additions; not all differences are vocabulary effects.",
            "No new allele, protein, taxon, phenotype or mechanism assignments are made.",
            "All records remain in scope for primary evidence review; no-hit queries do not prove absence.",
        ],
        "records": rows,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build_union(args.root.resolve(), args.plan, args.candidates)
    payload = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
    if args.check:
        existing = args.output.read_bytes()
        if args.output.suffix == ".gz":
            existing = gzip.decompress(existing)
        if existing != payload:
            raise SystemExit("Citation union differs from its pinned inputs")
    else:
        inputs = [args.root / p for p in (args.plan, args.candidates, *HISTORY)]
        if args.output.resolve() in {p.resolve() for p in inputs} or args.output.exists():
            raise SystemExit("Refusing to overwrite a citation input or an existing output")
        args.output.write_bytes(payload)
    print(json.dumps(result["summary"], sort_keys=True, indent=2))
