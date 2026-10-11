"""Bounded, citation-only discovery for records lacking resistance assertions.

Search co-occurrence is neither exact chemical identity nor biological evidence.
Only EMBL-EBI Europe PMC is contacted, with explicit network opt-in.
"""

import argparse
import csv
import json
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from itertools import zip_longest
from pathlib import Path
from urllib.parse import urlparse

import audit_card_grounding as card
import audit_resistance_grounding as common
import requests

URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
PAGE_SIZE = 100
CRITERIA = "canonical-title-abstract-resistance-genetics-v1"
CITATION_FIELDS = ("id", "source", "pmid", "pmcid", "doi", "title", "pubYear", "pubType")
LEDGER_FIELDS = (
    "identifier", "label", "path", "record_sha256", "standard_inchi_key", "class",
    "query", "status", "hit_count", "retained_citations", "candidate_ids", "primary_review_status",
)


class CitationPageConflict(ValueError):
    """An intact citation response cannot extend the requested cursor chain."""

    def __init__(self, message, reason, payload):
        super().__init__(message)
        self.reason = reason
        self.payload = payload


def query(label):
    return query_names([label])


def name_clause(names):
    if not names:
        raise ValueError("empty name query")
    clauses = []
    for label in names:
        if not label.strip() or any(ord(c) < 32 for c in label):
            raise ValueError("invalid canonical label")
        literal = label.replace("\\", "\\\\").replace('"', '\\"')
        clauses.append(f'TITLE_ABS:"{literal}"')
    return clauses[0] if len(clauses) == 1 else "(" + " OR ".join(clauses) + ")"


def query_names(names):
    term = name_clause(names)
    return (
        f'{term} AND '
        '(TITLE_ABS:resistan* OR TITLE_ABS:susceptib* OR TITLE_ABS:toleran*) AND '
        '(TITLE_ABS:gene OR TITLE_ABS:allele* OR TITLE_ABS:mutan* OR '
        'TITLE_ABS:mutation* OR TITLE_ABS:genetic* OR TITLE_ABS:genom*)'
    )


def query_names_immunity(names):
    """Broaden v1 recall without subtracting live matches absent from old snapshots."""
    return (
        f'{name_clause(names)} AND '
        '(TITLE_ABS:resistan* OR TITLE_ABS:susceptib* OR TITLE_ABS:toleran* OR '
        'TITLE_ABS:immun* OR TITLE_ABS:sensitiv*) AND '
        '(TITLE_ABS:gene* OR TITLE_ABS:allele* OR TITLE_ABS:mutan* OR '
        'TITLE_ABS:mutation* OR TITLE_ABS:genetic* OR TITLE_ABS:genom*)'
    )


def params(record):
    return {"query": record["query"], "format": "json", "resultType": "lite",
            "pageSize": PAGE_SIZE, "cursorMark": "*", "synonym": "false"}


def cache_path(parameters):
    key = common.digest(json.dumps([URL, parameters], sort_keys=True).encode())
    return common.OUT / ("epmc-discovery-" + key + ".json")


def validate(response, parameters, *, retained_before=0, expected_count=None, expected_version=None):
    size = parameters["pageSize"]
    cursor = parameters["cursorMark"]
    if (type(size) is not int or not 1 <= size <= 1000
            or type(retained_before) is not int or retained_before < 0
            or not isinstance(cursor, str) or not cursor
            or (cursor == "*") != (retained_before == 0)
            or parameters["format"] != "json" or parameters["resultType"] != "lite"
            or parameters["synonym"] != "false"):
        raise ValueError("invalid citation-page parameters or offset")
    location = urlparse(response["url"])
    expected = urlparse(URL)
    if (location.scheme, location.netloc, location.path) != (
        expected.scheme, expected.netloc, expected.path,
    ) or location.fragment:
        raise ValueError("unexpected Europe PMC response origin")
    if response["status"] != 200 or common.digest(response["body"].encode()) != response["sha256"]:
        raise ValueError("unsuccessful or corrupt Europe PMC response")
    if response["params"] != parameters:
        raise ValueError("cached query parameters differ")
    payload = json.loads(response["body"])
    if not isinstance(payload.get("version"), str) or not payload["version"]:
        raise ValueError("Europe PMC API version is missing")
    echoed = payload["request"]
    if (echoed["queryString"] != parameters["query"] or echoed["resultType"] != "lite"
            or echoed["pageSize"] != size or echoed["cursorMark"] != cursor
            or echoed["synonym"] is not False):
        raise ValueError("Europe PMC query echo differs")
    if "sort" in parameters and echoed.get("sort") != parameters["sort"]:
        raise ValueError("Europe PMC sort echo differs")
    count = payload["hitCount"]
    rows = payload["resultList"]["result"]
    if type(count) is not int or count < 0:
        raise ValueError("invalid reported result count")
    identifiers = [(r["source"], r["id"]) for r in rows]
    if any(not isinstance(v, str) or not v for pair in identifiers for v in pair):
        raise ValueError("invalid publication identifier")
    if len(set(identifiers)) != len(identifiers):
        raise ValueError("duplicate publication within search page")
    if any("abstractText" in r for r in rows):
        raise ValueError("citation-only search unexpectedly returned abstracts")
    if ((expected_count is not None and count != expected_count)
            or (expected_version is not None and payload["version"] != expected_version)):
        raise CitationPageConflict("Europe PMC count or version changed during cursor traversal",
                                   "CURSOR_COUNT_OR_VERSION_CHANGED", payload)
    if count < retained_before or len(rows) != min(count - retained_before, size):
        raise CitationPageConflict("unexpected result count; not an empty or complete search",
                                   "CURSOR_PAGE_LENGTH_MISMATCH", payload)
    if count > retained_before + len(rows) and not payload.get("nextCursorMark"):
        raise ValueError("truncated response lacks a continuation cursor")
    return payload


def fetch(parameters, session=None, *, retained_before=0, expected_count=None, expected_version=None,
          cache_conflicts=False):
    """Optionally retain intact cursor conflicts for audit, never as validated results."""
    context = {"retained_before": retained_before, "expected_count": expected_count,
               "expected_version": expected_version}
    path = cache_path(parameters)
    if path.exists():
        result = json.loads(path.read_text())
        try:
            validate(result, parameters, **context)
        except CitationPageConflict:
            if not cache_conflicts:
                raise
        return result
    if not common.ALLOW_NETWORK:
        raise ValueError("uncached query; network is disabled")
    client = requests if session is None else session
    for attempt in range(3):
        try:
            response = client.get(URL, params=parameters, timeout=(10, 60), allow_redirects=False)
        except (requests.Timeout, requests.ConnectionError):
            if attempt == 2:
                raise
        else:
            if response.status_code not in (429, 500, 502, 503, 504) or attempt == 2:
                break
        time.sleep(2**attempt)
    result = {
        "url": response.url, "params": parameters, "status": response.status_code,
        "headers": dict(response.headers), "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "sha256": common.digest(response.content), "body": response.text,
    }
    try:
        validate(result, parameters, **context)
    except CitationPageConflict:
        if not cache_conflicts:
            raise
    common.write(path.name, result)
    time.sleep(0.2)
    return result


def plan(root):
    records = card.current_corpus(root)
    groups = defaultdict(list)
    for record in records:
        if record["resistance_mechanisms"] or record["score_rules"]:
            continue
        item = {k: record[k] for k in (
            "identifier", "label", "path", "sha256", "standard_inchi_key", "class",
        )}
        item["query"] = query(record["label"])
        groups[record["class"]].append(item)
    # Round-robin classes prevents a bounded pass from covering only one filing group.
    balanced = [r for row in zip_longest(*(groups[k] for k in sorted(groups))) for r in row if r]
    common.write("discovery-plan.json", {
        "criteria": CRITERIA, "corpus_sha256": common.digest((common.OUT / "corpus.json").read_bytes()),
        "records": balanced,
        "limitations": [
            "Canonical labels only; aliases, historical names and broader sources remain unsearched.",
            "Phrase matching does not resolve exact structures, salts, mixtures or biological context.",
            "Co-occurrence can describe other drugs, cancer cells or non-resistance experiments.",
            "Only the first 100 provider-ranked citations are retained; truncated queries need refinement.",
            "Zero query hits do not establish that resistance is unknown or absent.",
        ],
    })
    print(f"Planned {len(balanced)} records across {len(groups)} classes", flush=True)


def load_plan(root):
    records = card.current_corpus(root)
    payload = (common.OUT / "discovery-plan.json").read_bytes()
    result = json.loads(payload)
    if (result["criteria"] != CRITERIA
            or result["corpus_sha256"] != common.digest((common.OUT / "corpus.json").read_bytes())):
        raise ValueError("stale discovery plan")
    expected = {r["identifier"]: r for r in records
                if not r["resistance_mechanisms"] and not r["score_rules"]}
    if (len(result["records"]) != len(expected)
            or {r["identifier"] for r in result["records"]} != set(expected)):
        raise ValueError("discovery plan membership differs")
    for record in result["records"]:
        if any(record[k] != expected[record["identifier"]][k] for k in
               ("label", "path", "sha256", "standard_inchi_key", "class")):
            raise ValueError("discovery plan record differs")
        if record["query"] != query(record["label"]):
            raise ValueError("discovery query differs")
    return result, common.digest(payload)


def search(root, maximum, only):
    planned, before = load_plan(root)
    ids = {r["identifier"] for r in planned["records"]}
    if maximum < 1 or set(only) - ids:
        raise ValueError("invalid request bound or unknown cohort identifier")
    fresh = 0
    with requests.Session() as session:
        for record in planned["records"]:
            if only and record["identifier"] not in only:
                continue
            parameters = params(record)
            cached = cache_path(parameters).exists()
            if not cached and fresh == maximum:
                break
            result = fetch(parameters, session=session)
            if not cached:
                fresh += 1
                hits = json.loads(result["body"])["hitCount"]
                print(f"new search {fresh}/{maximum}: {record['identifier']} ({hits} hits)", flush=True)
    if load_plan(root)[1] != before:
        raise ValueError("discovery inputs changed during search")
    print(f"Search checkpoint: {fresh} new responses; previously cached queries reused", flush=True)


def analyze(root):
    planned, plan_hash = load_plan(root)
    rows, results = [], []
    for record in planned["records"]:
        parameters = params(record)
        path = cache_path(parameters)
        item = dict(record, status="NOT_SEARCHED", hit_count=None, candidates=[])
        if path.exists():
            response = json.loads(path.read_text())
            payload = validate(response, parameters)
            count = payload["hitCount"]
            item.update(
                status="NO_HITS_IN_LIMITED_QUERY" if count == 0 else
                "TRUNCATED_REFINEMENT_REQUIRED" if count > PAGE_SIZE else "CANDIDATES_REQUIRE_REVIEW",
                hit_count=count,
                candidates=[{k: r[k] for k in CITATION_FIELDS if k in r}
                            for r in payload["resultList"]["result"]],
                api_version=payload["version"], next_cursor=payload.get("nextCursorMark"),
                request={k: v for k, v in response.items() if k not in ("body", "headers")},
            )
        item["primary_review_status"] = "PENDING"
        results.append(item)
        rows.append({
            "identifier": item["identifier"], "label": item["label"], "path": item["path"],
            "record_sha256": item["sha256"], "standard_inchi_key": item["standard_inchi_key"],
            "class": item["class"], "query": item["query"], "status": item["status"],
            "hit_count": item["hit_count"], "retained_citations": len(item["candidates"]),
            "candidate_ids": "|".join(c["source"] + ":" + c["id"] for c in item["candidates"]),
            "primary_review_status": "PENDING",
        })
    if load_plan(root)[1] != plan_hash:
        raise ValueError("discovery inputs changed during analysis")
    summary = dict(Counter(r["status"] for r in rows))
    common.write("discovery-candidates.json", {
        "criteria": CRITERIA, "plan_sha256": plan_hash, "corpus_sha256": planned["corpus_sha256"],
        "summary": summary, "records": results, "limitations": planned["limitations"],
        "scope": "CITATION_DISCOVERY_ONLY; NO_COMPOUND_ALLELE_OR_AST_ASSIGNMENTS",
        "source": "EMBL-EBI Europe PMC citation metadata; no abstracts or full text exported",
    })
    with (common.OUT / "discovery-ledger.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=LEDGER_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("plan", "search", "analyze"))
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--allow-network", action="store_true")
    parser.add_argument("--max-new-requests", type=int, default=25)
    parser.add_argument("--only", action="append", default=[])
    args = parser.parse_args()
    common.OUT = args.output_dir.resolve()
    common.OUT.mkdir(parents=True, exist_ok=True)
    common.ALLOW_NETWORK = args.allow_network
    if args.stage == "search":
        search(args.root.resolve(), args.max_new_requests, args.only)
    else:
        globals()[args.stage](args.root.resolve())
