"""Screen cached bla-prefix leads and retain the observed SCO-1 primary-access hold."""

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

import audit_card_literature_expansion as literature
from audit_valinomycin_abcb1 import planned_source
from audit_vgb_evidence import read_json, reference, require
from lxml import html

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-15-sco1-primary")
OUTPUT = Path("research/2026-10-15-card-bla-alias-screen.json")
INDEX = Path("research/2026-10-15-card-followup-memberships.json")
INDEX_SHA = "dc3000fb1fd17444faa96e7bd11a6478b506cc1a2a0054878347312a70ce7177"
PLAN_SHA = "e07a50f844505075f102f78fba479b65e84e5596280f2fe9d8860c523100a9b0"
URL = "https://europepmc.org/articles/PMC1891400"
SCOPE = "CACHED_BLA_PREFIX_DISCOVERY_NOT_VERIFIED_REFERENCE_OR_EXPERIMENTAL_ASSIGNMENT"


def native_matches(entry, label):
    return [
        {"gene_index": i, "field": field, "value": node["value"]}
        for i, block in enumerate(entry.get("genes", []))
        for field in ("geneName", "synonyms")
        for node in (
            block.get(field, []) if field == "synonyms" else [block[field]] if field in block else []
        )
        if node["value"].casefold() == ("bla" + label).casefold()
    ]


def primary_hold(payload, receipt):
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    tree = html.fromstring(payload)
    require(
        receipt["url"] == URL
        and receipt["status"] == 403
        and receipt["retry_performed"] is receipt["redirects_followed"] is False
        and receipt["sha256"] == hashlib.sha256(payload).hexdigest()
        and receipt["bytes"] == len(payload)
        and headers.get("cf-mitigated") == "challenge"
        and tree.xpath("//title/text()") == ["Just a moment..."]
        and not tree.xpath('//meta[@name="citation_doi"]/@content'),
        "primary challenge identity changed",
    )
    return {
        "url": URL,
        "pmid": "PMID:17353248",
        "doi": "DOI:10.1128/aac.01439-06",
        "status": "PRIMARY_HTML_403_CHALLENGE_HELD_NO_RETRY_OR_ALTERNATE",
        "http_status": 403,
        "challenge_treated_as_primary": False,
        "primary_results_reviewed": False,
        "retrieved_primary_text": False,
        "retry_performed": False,
        "alternate_route_used": False,
        "hold_is_biological_negative_result": False,
        "permanent_unavailability_inferred": False,
        "revisit_requires": "USER_SUPPLIED_PRIMARY_COPY_OR_NEW_EXPLICIT_DIRECTION",
    }


def screen(root, index, definitions, direct):
    terms = {tid: row for tid, row in index["terms"].items() if not row["links"]}
    by_pmid = defaultdict(set)
    for tid, term in terms.items():
        (label,) = direct["determinants"][tid]["labels"]
        require(
            hashlib.sha256(label.encode()).hexdigest() == term["source_label_sha256"]
            and definitions["terms"][tid]["record_memberships"] == term["record_memberships"],
            "source label or memberships changed",
        )
        for citation in definitions["terms"][tid]["definition_citation_ids"]:
            if citation.startswith("PMID:"):
                by_pmid[citation.removeprefix("PMID:")].add(tid)
    queries, candidates = {}, {}
    for pmid, tids in sorted(by_pmid.items(), key=lambda item: int(item[0])):
        directories = [
            literature.DIRECTORY,
            Path("reports/resistance-grounding-2026-10-09-card-literature-proteins"),
        ]
        present = [
            d
            for d in directories
            if (root / d / ("pmid-" + pmid + "-receipt.json")).exists()
            or (root / d / ("pmid-" + pmid + "-response.bin")).exists()
        ]
        directory = present[0] if present else directories[0]
        entries, query = literature.read_query(root, root / directory, pmid)
        require(query["complete_for_query"] and query["release"] == "2026_03", "incomplete citation query")
        queries[pmid] = {"directory": str(directory), "query": query, "source_terms": sorted(tids)}
        for tid in tids:
            (label,) = direct["determinants"][tid]["labels"]
            for accession, entry in entries.items():
                matches = native_matches(entry, label)
                if not matches:
                    continue
                identity = {
                    "source_term_id": tid,
                    "source_label": label,
                    "protein_accession": "UniProtKB:" + accession,
                    "native_matches": matches,
                    "entry_type": entry["entryType"],
                    "entry_audit": entry["entryAudit"],
                    "native_taxon_id": entry["organism"]["taxonId"],
                    "native_organism_name": entry["organism"]["scientificName"],
                }
                key = tid + "|" + accession
                candidate = candidates.setdefault(
                    key,
                    {
                        "identity": identity,
                        "query_pmids": [],
                        "record_memberships": terms[tid]["record_memberships"],
                        "status": "DISCOVERY_LEAD_NOT_VERIFIED_REFERENCE_OR_ALLELE",
                    },
                )
                require(candidate["identity"] == identity, "cross-query candidate identity changed")
                candidate["query_pmids"].append(pmid)
    return sorted(terms), queries, candidates


def build(root):
    directory = root / CACHE
    require(
        reference.digest(directory / "request-plan.json") == PLAN_SHA
        and reference.digest(root / INDEX) == INDEX_SHA,
        "frozen plan or index changed",
    )
    plan = json.loads((directory / "request-plan.json").read_bytes())
    prior = read_json(root, plan["prior"])
    for key in ("prior_verification", "source_queue", "protected", "access_inventory"):
        reference.check_pin(root, plan[key])
    require(
        prior["metadata"]["17353248"]["pmcid"] == "PMC1891400"
        and plan["requests"]["primary"]["advertised_link"]
        in prior["metadata"]["17353248"]["advertised_primary_links"],
        "advertised source link changed",
    )
    source = planned_source(root, directory, "primary", "request-plan.json", URL, (403,))
    receipt = read_json(root, source["receipt"])
    hold = primary_hold(reference.check_pin(root, source["body"]).read_bytes(), receipt)
    index = json.loads((root / INDEX).read_bytes())
    definitions = read_json(root, index["inputs"]["definition_citations"])
    direct = read_json(root, index["inputs"]["direct_candidates"])
    terms, queries, candidates = screen(root, index, definitions, direct)
    draft = json.loads((directory / "bla-alias-screen.json").read_bytes())
    require(
        terms == draft["screened_terms"]
        and queries == draft["queries"]
        and candidates == draft["candidates"],
        "exploratory screen does not reproduce",
    )
    prior_pairs = {(prior["source_term_id"], accession) for accession in prior["references"]}
    for row in candidates.values():
        pair = (row["identity"]["source_term_id"], row["identity"]["protein_accession"])
        row["previously_reviewed_reference"] = pair in prior_pairs
        row["prior_reference_context"] = plan["prior"] if pair in prior_pairs else None
        row["native_citation_and_taxonomy_review_pending"] = pair not in prior_pairs
        row["experimental_subject_assignment"] = False
    with reference.check_pin(root, index["inputs"]["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    require(
        len(census) == len({r["identifier"] for r in census}) == 2939
        and {r["path"] for r in census}
        == {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        and all(reference.digest(root / r["path"]) == r["record_sha256"] for r in census),
        "corpus changed",
    )
    selected_terms = {r["identity"]["source_term_id"] for r in candidates.values()}
    ids = {rid for r in candidates.values() for rid in r["record_memberships"]}
    records, claims = [r for r in census if r["identifier"] in ids], []
    for row in records:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "record identity changed",
        )
        for i, claim in enumerate(doc.get("resistance_mechanisms", [])):
            if claim.get("aro_id") in selected_terms:
                (expected,) = [
                    c
                    for c in index["claims"]
                    if c["record_identifier"] == doc["identifier"] and c["resistance_index"] == i
                ]
                require(
                    expected["claim_sha256"]
                    == hashlib.sha256(
                        json.dumps(claim, sort_keys=True, ensure_ascii=True).encode()
                    ).hexdigest(),
                    "live claim content changed",
                )
                claims.append(expected)
    return {
        "date": "2026-10-15",
        "scope": SCOPE,
        "inputs": {
            "index": reference.pin(root, root / INDEX),
            "prior": plan["prior"],
            "request_plan": reference.pin(root, directory / "request-plan.json"),
            "exploratory_screen": reference.pin(root, directory / "bla-alias-screen.json"),
            "definitions": index["inputs"]["definition_citations"],
            "direct_candidates": index["inputs"]["direct_candidates"],
            "census": index["inputs"]["census"],
            "source_queue": plan["source_queue"],
        },
        "primary_access_hold": {**hold, "source": source},
        "screened_terms": terms,
        "queries": queries,
        "candidates": candidates,
        "records": records,
        "claims": claims,
        "summary": {
            "terms_screened": len(terms),
            "source_pmids": len(queries),
            "query_statuses": dict(Counter(q["query"]["status"] for q in queries.values())),
            "candidate_terms": len(selected_terms),
            "candidate_term_protein_pairs": len(candidates),
            "previously_reviewed_reference_pairs": sum(
                r["previously_reviewed_reference"] for r in candidates.values()
            ),
            "new_discovery_pairs": sum(not r["previously_reviewed_reference"] for r in candidates.values()),
            "candidate_records_read": len(records),
            "candidate_source_claims": len(claims),
            "corpus_records_hash_checked": len(census),
        },
        "limits": {
            "network_requests": 1,
            "screen_network_requests": 0,
            "candidate_free_is_biological_absence": False,
            "global_cache_completeness_claimed": False,
            "new_reference_or_experimental_assignments": 0,
            "primary_results_reviewed": False,
            "taxon_lineages_verified_by_this_screen": False,
            "biological_records_changed": 0,
            "whole_record_primary_signoffs": 0,
            "membership_index_updated": False,
            "ncbi_requests": 0,
            "outreach": 0,
            "github_mutations": 0,
            "source_adoptions": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": "CARD/ARO ontology: McMaster University, CC BY 4.0. "
        "UniProt Consortium metadata, release 2026_03. "
        "SCO-1 primary route advertised by Europe PMC; challenge page is not primary evidence.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    body = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
    if args.check or args.output.exists():
        require(args.output.read_bytes() == body, "alias screen does not reproduce")
    else:
        with args.output.open("xb") as stream:
            stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
