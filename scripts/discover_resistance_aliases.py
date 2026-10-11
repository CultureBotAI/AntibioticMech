"""Citation-only discovery over every record's labels and provenance-bearing names.

Names are query leads, not compound equivalences or biological assertions.
The network client contacts only EMBL-EBI Europe PMC with explicit opt-in.
"""

import argparse
import csv
import json
from collections import Counter, defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from itertools import zip_longest
from pathlib import Path
from urllib.parse import urlencode

import discover_resistance_literature as discovery

from antibioticmech.activity_collections import load_record

common = discovery.common
CRITERIA = "all-record-provenance-names-title-abstract-resistance-genetics-v1"
PLAN = "alias-discovery-plan.json"
CANDIDATES = "alias-discovery-candidates.json"
LEDGER = "alias-discovery-ledger.tsv"
MAX_NAMES = 4
MAX_URL_BYTES = 6000  # A client-side request bound, not a claimed provider limit.
IDENTITY_FIELDS = ("identifier", "label", "path", "sha256", "standard_inchi_key", "class")
LEDGER_FIELDS = (
    "identifier", "label", "path", "record_sha256", "standard_inchi_key", "class",
    "names", "shared_names", "queries", "searched_queries", "truncated_queries",
    "search_status", "canonical_query_status", "retained_unique_citations", "candidate_ids",
    "added_vs_canonical_retained_ids", "primary_review_status",
)
LIMITATIONS = [
    "Only names already present in records are covered; undiscovered historical names remain open.",
    "INN, brand, exact and related synonyms retain their source scope; none proves exact material identity.",
    "Shared names do not merge salts, stereoisomers, mixtures, structures or record identifiers.",
    "An OR-query hit does not identify which name matched or prove resistance to an exact structure.",
    "Only the first 100 provider-ranked citations per query are retained; truncated queries need refinement.",
    "Added citations are relative to the retained canonical page, not absence from its complete results.",
    "Completed searches are not primary review, allele grounding, phenotype evidence or biological absence.",
]


@dataclass(frozen=True)
class DiscoveryProfile:
    criteria: str
    plan: str
    candidates: str
    ledger: str
    query_names: Callable[[list[str]], str]
    limitations: tuple[str, ...]


LEGACY_PROFILE = DiscoveryProfile(
    CRITERIA, PLAN, CANDIDATES, LEDGER, discovery.query_names, tuple(LIMITATIONS),
)
IMMUNITY_PROFILE = DiscoveryProfile(
    "all-record-provenance-names-title-abstract-resistance-immunity-genetics-v2",
    "vocabulary-discovery-plan.json", "vocabulary-discovery-candidates.json",
    "vocabulary-discovery-ledger.tsv", discovery.query_names_immunity,
    (*LIMITATIONS,
     "Expanded vocabulary adds gene*, immun* and sensitiv*; historical v1 results remain separate.",
     "This is a full broader query, not a live-v1 subtraction; retain older citations when merging.",
     "Broader vocabulary improves the known-paper canaries, not proven corpus recall or precision."),
)
PROFILES = {"v1": LEGACY_PROFILE, "immunity-v2": IMMUNITY_PROFILE}


def record_names(doc):
    names = {}

    def add(text, origin):
        discovery.query(text)
        names.setdefault(text, {"text": text, "origins": []})["origins"].append(origin)

    add(doc["label"], {"kind": "CANONICAL_LABEL"})
    for index, entry in enumerate(doc.get("synonyms", [])):
        add(entry["synonym_text"], {
            "kind": "SYNONYM", "index": index,
            **{k: v for k, v in entry.items() if k != "synonym_text"},
        })
    for index, entry in enumerate(doc.get("source_concepts", [])):
        add(entry["source_label"], {
            "kind": "SOURCE_LABEL", "index": index,
            **{k: entry[k] for k in ("source", "source_id", "minted_identifier") if k in entry},
        })
    return list(names.values())


def make_queries(names, *, profile=LEGACY_PROFILE):
    def make(indices, kind):
        query = profile.query_names([names[i]["text"] for i in indices])
        parameters = discovery.params({"query": query})
        size = len((discovery.URL + "?" + urlencode(parameters)).encode())
        return {"kind": kind, "name_indices": indices, "query": query}, size

    canonical, size = make([0], "CANONICAL")
    if size > MAX_URL_BYTES:
        raise ValueError("canonical query exceeds client request bound; manual refinement required")
    queries, group = [canonical], []
    # Short names first improves bounded coverage without excluding systematic names.
    order = sorted(range(1, len(names)), key=lambda i: (len(names[i]["text"]), i))
    for index in order:
        _, size = make([*group, index], "ALIASES")
        if group and (len(group) == MAX_NAMES or size > MAX_URL_BYTES):
            queries.append(make(group, "ALIASES")[0])
            group = []
        _, size = make([*group, index], "ALIASES")
        if size > MAX_URL_BYTES:
            raise ValueError("single-name query exceeds client request bound; manual refinement required")
        group.append(index)
    if group:
        queries.append(make(group, "ALIASES")[0])
    for index, query in enumerate(queries):
        query["query_id"] = str(index)
    return queries


def build_plan(root, *, profile=LEGACY_PROFILE):
    census_path = common.OUT / "corpus.json"
    before = common.digest(census_path.read_bytes())
    records = discovery.card.current_corpus(root)
    groups, owners = defaultdict(list), defaultdict(list)
    for number, record in enumerate(records, 1):
        path = root / record["path"]
        doc = load_record(path)
        if (common.digest(path.read_bytes()) != record["sha256"]
                or doc["identifier"] != record["identifier"] or doc["label"] != record["label"]
                or doc["chemical_structure"]["standard_inchi_key"] != record["standard_inchi_key"]
                or doc["antimicrobial_class"] != record["class"]):
            raise ValueError("record changed during name inventory")
        names = record_names(doc)
        for name in names:
            owners[name["text"]].append(record["identifier"])
        item = {k: record[k] for k in IDENTITY_FIELDS}
        item.update(
            names=names, queries=make_queries(names, profile=profile),
            has_existing_resistance_evidence=bool(record["resistance_mechanisms"] or record["score_rules"]),
        )
        groups[record["class"]].append(item)
        if number % 500 == 0:
            print(f"name inventory: {number}/{len(records)}", flush=True)
    balanced = [r for row in zip_longest(*(groups[k] for k in sorted(groups))) for r in row if r]
    for record in balanced:
        for name in record["names"]:
            name["shared_with_record_ids"] = sorted(
                i for i in owners[name["text"]] if i != record["identifier"]
            )
    if (common.digest(census_path.read_bytes()) != before
            or discovery.card.current_corpus(root) != records):
        raise ValueError("corpus changed during name inventory")
    return {
        "criteria": profile.criteria, "corpus_sha256": before, "records": balanced,
        "limits": {"max_names_per_alias_query": MAX_NAMES, "max_url_bytes": MAX_URL_BYTES},
        "limitations": list(profile.limitations),
    }


def plan(root, *, profile=LEGACY_PROFILE):
    result = build_plan(root, profile=profile)
    common.write(profile.plan, result)
    print(json.dumps({"records": len(result["records"]),
                      "names": sum(len(r["names"]) for r in result["records"]),
                      "queries": sum(len(r["queries"]) for r in result["records"])}), flush=True)


def load_plan(root, *, profile=LEGACY_PROFILE):
    payload = (common.OUT / profile.plan).read_bytes()
    actual = json.loads(payload)
    if actual != build_plan(root, profile=profile):
        raise ValueError("stale or altered alias plan; regenerate after reviewing record changes")
    return actual, common.digest(payload)


def unchanged(root, planned, plan_hash, *, profile=LEGACY_PROFILE):
    if (common.digest((common.OUT / profile.plan).read_bytes()) != plan_hash
            or common.digest((common.OUT / "corpus.json").read_bytes()) != planned["corpus_sha256"]):
        raise ValueError("alias discovery inputs changed during processing")
    discovery.card.current_corpus(root)


def search(root, maximum, only, *, profile=LEGACY_PROFILE):
    planned, plan_hash = load_plan(root, profile=profile)
    if type(maximum) is not int or maximum < 1 or set(only) - {r["identifier"] for r in planned["records"]}:
        raise ValueError("invalid request bound or unknown cohort identifier")
    selected = [r for r in planned["records"] if not only or r["identifier"] in only]
    fresh = 0
    with discovery.requests.Session() as session:
        # Visit one query per record per round; records with many names cannot monopolize a batch.
        for layer in zip_longest(*(r["queries"] for r in selected)):
            for record, query in zip(selected, layer, strict=True):
                if query is None:
                    continue
                parameters = discovery.params(query)
                cached = discovery.cache_path(parameters).exists()
                if not cached and fresh == maximum:
                    unchanged(root, planned, plan_hash, profile=profile)
                    print(f"Alias checkpoint: {fresh} new responses; remaining queries retained", flush=True)
                    return
                result = discovery.fetch(parameters, session=session)
                if not cached:
                    fresh += 1
                    count = json.loads(result["body"])["hitCount"]
                    print(f"new search {fresh}/{maximum}: {record['identifier']} "
                          f"{query['kind']} {query['query_id']} ({count} hits)", flush=True)
    unchanged(root, planned, plan_hash, profile=profile)
    print(f"Alias checkpoint: {fresh} new responses; all selected queries cached", flush=True)


def analyze_record(record):
    queries, identities = [], set()
    for query in record["queries"]:
        parameters = discovery.params(query)
        path = discovery.cache_path(parameters)
        item = dict(query, status="NOT_SEARCHED", hit_count=None, candidates=[])
        if path.exists():
            response = json.loads(path.read_bytes())
            payload = discovery.validate(response, parameters)
            count = payload["hitCount"]
            item.update(
                status="NO_HITS_IN_LIMITED_QUERY" if count == 0 else
                "TRUNCATED_REFINEMENT_REQUIRED" if count > discovery.PAGE_SIZE else
                "CANDIDATES_REQUIRE_REVIEW",
                hit_count=count, candidates=[{k: row[k] for k in discovery.CITATION_FIELDS if k in row}
                                            for row in payload["resultList"]["result"]],
                api_version=payload["version"], next_cursor=payload.get("nextCursorMark"),
                request={k: v for k, v in response.items() if k not in {"body", "headers"}},
            )
            identities.update((c["source"], c["id"]) for c in item["candidates"])
        queries.append(item)
    searched = sum(q["status"] != "NOT_SEARCHED" for q in queries)
    canonical = queries[0]
    baseline = {(c["source"], c["id"]) for c in canonical["candidates"]}
    added = None if canonical["status"] == "NOT_SEARCHED" else sorted(identities - baseline)
    return {
        **{k: v for k, v in record.items() if k != "queries"}, "queries": queries,
        "searched_queries": searched,
        "search_status": "NOT_SEARCHED" if not searched else
        "ALL_INITIAL_NAME_QUERIES_SEARCHED" if searched == len(queries) else "PARTIAL",
        "candidate_ids": [source + ":" + identifier for source, identifier in sorted(identities)],
        "added_vs_canonical_retained_ids": None if added is None else [s + ":" + i for s, i in added],
        "primary_review_status": "PENDING",
    }


def analyze(root, *, profile=LEGACY_PROFILE):
    planned, plan_hash = load_plan(root, profile=profile)
    records = [analyze_record(record) for record in planned["records"]]
    summary = {
        "records": len(records), "names": sum(len(r["names"]) for r in records),
        "queries": sum(len(r["queries"]) for r in records),
        "query_status": dict(Counter(q["status"] for r in records for q in r["queries"])),
        "record_search_status": dict(Counter(r["search_status"] for r in records)),
        "records_with_added_citations": sum(bool(r["added_vs_canonical_retained_ids"]) for r in records),
        "records_with_shared_names": sum(
            any(n["shared_with_record_ids"] for n in r["names"]) for r in records
        ),
    }
    unchanged(root, planned, plan_hash, profile=profile)
    common.write(profile.candidates, {
        "criteria": profile.criteria, "plan_sha256": plan_hash, "corpus_sha256": planned["corpus_sha256"],
        "summary": summary, "records": records, "limitations": list(profile.limitations),
        "scope": "CITATION_DISCOVERY_ONLY; NO_COMPOUND_ALLELE_OR_AST_ASSIGNMENTS",
        "source": "EMBL-EBI Europe PMC citation metadata; no abstracts or full text exported",
    })
    rows = [{
        **{k: r[k] for k in ("identifier", "label", "path", "standard_inchi_key", "class")},
        "record_sha256": r["sha256"], "names": len(r["names"]),
        "shared_names": sum(bool(n["shared_with_record_ids"]) for n in r["names"]),
        "queries": len(r["queries"]), "searched_queries": r["searched_queries"],
        "truncated_queries": sum(q["status"] == "TRUNCATED_REFINEMENT_REQUIRED" for q in r["queries"]),
        "search_status": r["search_status"], "canonical_query_status": r["queries"][0]["status"],
        "retained_unique_citations": len(r["candidate_ids"]),
        "candidate_ids": "|".join(r["candidate_ids"]),
        "added_vs_canonical_retained_ids": "|".join(r["added_vs_canonical_retained_ids"] or []),
        "primary_review_status": "PENDING",
    } for r in records]
    with (common.OUT / profile.ledger).open("w", newline="") as handle:
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
    parser.add_argument("--vocabulary", choices=PROFILES, default="v1",
                        help="Keep v1 snapshots intact; immunity-v2 uses separate versioned plan and exports")
    args = parser.parse_args()
    common.OUT = args.output_dir.resolve()
    common.OUT.mkdir(parents=True, exist_ok=True)
    common.ALLOW_NETWORK = args.allow_network
    profile = PROFILES[args.vocabulary]
    if args.stage == "search":
        search(args.root.resolve(), args.max_new_requests, args.only, profile=profile)
    else:
        globals()[args.stage](args.root.resolve(), profile=profile)
