"""Reproduce literature-constrained reference candidates without biological writes."""

import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import audit_card_citation_concordance as concordance
import audit_card_definition_citations as citations
import audit_card_grounding as card
import audit_topoisomerase_references as reference

DEFAULT_DIRECTORY = Path("reports/resistance-grounding-2026-10-09-card-literature-proteins")
DEFAULT_OUTPUT = Path("research/2026-10-09-card-literature-proteins.json")
SCOPE = "SOURCE_CITATION_AND_REFERENCE_NAME_MATCH_NOT_EXPERIMENTAL_GENE_ALLELE_OR_PHENOTYPE"


def parameters(pmid):
    return {"query": "lit_pubmed:" + pmid, "format": "json", "size": "500",
            "sort": "accession asc", "fields": card.FIELDS}


def read_query(root, directory, pmid):
    expected, request = parameters(pmid), parameters(pmid)
    page, entries, pages, seen_requests, used = 0, {}, [], set(), set()
    total, release, last_accession = None, None, None
    while request is not None:
        signature = json.dumps(request, sort_keys=True)
        if signature in seen_requests:
            raise ValueError("pagination cycle")
        seen_requests.add(signature)
        page += 1
        key = "pmid-" + pmid + (f"-page-{page:03d}" if page > 1 else "")
        path, receipt_path = directory / (key + "-response.bin"), directory / (key + "-receipt.json")
        raw, receipt = path.read_bytes(), json.loads(receipt_path.read_bytes())
        parsed = urlparse(receipt["url"])
        if (parsed.scheme != "https" or parsed.netloc != "rest.uniprot.org"
                or parsed.path != "/uniprotkb/search" or parsed.fragment
                or parse_qs(parsed.query, keep_blank_values=True) != {k: [v] for k, v in request.items()}
                or receipt["query"] != expected["query"]):
            raise ValueError("literature request identity drift")
        if (receipt["status"] != 200 or receipt["sha256"] != reference.digest(path)
                or receipt["bytes"] != len(raw)):
            raise ValueError("response status or digest mismatch")
        headers = {k.lower(): v for k, v in receipt["headers"].items()}
        count = int(headers["x-total-results"])
        if count < 0 or not headers.get("x-uniprot-release"):
            raise ValueError("invalid result count or missing release")
        if total is None:
            total, release = count, headers["x-uniprot-release"]
        if total != count or release != headers["x-uniprot-release"]:
            raise ValueError("result count or release changed across pages")
        rows = json.loads(raw)["results"]
        if len(rows) != min(500, max(total - len(entries), 0)):
            raise ValueError("page cardinality does not match query total")
        for entry in rows:
            accession = entry["primaryAccession"]
            if ("sequence" in entry or accession in entries
                    or (last_accession is not None and accession <= last_accession)):
                raise ValueError("sequence, duplicate or out-of-order search entry")
            if "PMID:" + pmid not in {v for r in concordance.entry_bibliography(entry)
                                     for v in r["identifiers"]}:
                raise ValueError("search entry does not cite the requested paper")
            entries[accession], last_accession = entry, accession
        request = card.next_page(headers.get("link", ""), expected)
        if (request is None) != (len(entries) == total):
            raise ValueError("pagination termination does not match declared total")
        pages.append({"page": page, "cache": reference.pin(root, path),
                      "receipt": reference.pin(root, receipt_path), "url": receipt["url"],
                      "retrieved_at": receipt["retrieved_at"], "status": receipt["status"]})
        if page > 1:
            used.update((path, receipt_path))
    actual = set(directory.glob(f"pmid-{pmid}-page-*-response.bin"))
    actual.update(directory.glob(f"pmid-{pmid}-page-*-receipt.json"))
    if actual != used:
        raise ValueError("orphaned continuation response or receipt")
    return entries, {"query": expected["query"], "result_count": total, "pages": pages,
                     "release": release, "complete_for_query": True, "establishes_biological_absence": False}


def match_entry(entry, tid, label):
    matches = []
    for block in entry.get("genes", []):
        for field in ("geneName", "synonyms"):
            values = ([block[field]] if field == "geneName" and field in block else
                      block.get(field, []) if field == "synonyms" else [])
            matches.extend({"field": field, "value": item["value"]} for item in values
                           if item["value"].casefold() == label.casefold())
    direct = any(row["database"] == "CARD" and row["id"] == tid
                 for row in entry.get("uniProtKBCrossReferences", []))
    return sorted(matches, key=lambda x: (x["field"], x["value"])), direct


def derive_terms(selected, entries, query_members):
    result = {}
    for tid, row in sorted(selected.items()):
        pmids = [value.removeprefix("PMID:") for value in row["definition_citation_ids"]]
        pool = {acc for pmid in pmids for acc in query_members[pmid]}
        matches = []
        for acc in sorted(pool):
            names, direct = match_entry(entries[acc], tid, row["source_label"])
            if not names and not direct:
                continue
            matches.append({
                "protein_accession": "UniProtKB:" + acc,
                "source_citation_ids": sorted("PMID:" + pmid for pmid in pmids if acc in query_members[pmid]),
                "literal_gene_matches": names, "explicit_card_xref": direct,
                "scope": "REFERENCE_CANDIDATE_NOT_EXPERIMENTAL_IDENTITY",
            })
        result[tid] = {"source_label_sha256": row["source_label_sha256"],
                      "definition_citation_ids": row["definition_citation_ids"],
                      "record_memberships": row["record_memberships"], "reference_candidates": matches,
                      "literature_entries_inspected": len(pool),
                      "nonmatching_entries": len(pool) - len(matches),
                      "primary_review_status": "NOT_COMPLETED_BY_METADATA_LOOKUP",
                      "no_match_is_biological_absence": False}
    return result


def collect(root, directory):
    plan_path = directory / "plan.json"
    plan = json.loads(plan_path.read_bytes())
    paths = {key: reference.check_pin(root, item) for key, item in plan["inputs"].items()}
    prior = json.loads(paths["concordance"].read_bytes())
    selected = {t: row for t, row in prior["terms"].items()
                if not row["explicit_reference_candidates"] and row["citation_overlap_leads"]}
    census, labels, memberships, records = citations.read_corpus(root, paths["current_census"])
    if set(labels) != set(prior["terms"]) or set(selected) != set(plan["selected_terms"]):
        raise ValueError("current or selected source term membership drift")
    for tid, row in prior["terms"].items():
        if (row["source_label_sha256"] != citations.text_hash(labels[tid])
                or row["record_memberships"] != sorted(memberships[tid])):
            raise ValueError("source label or record membership drift")
    selected = {t: {**row, "source_label": labels[t]} for t, row in selected.items()}
    if selected != plan["selected_terms"] or plan["fields"] != card.FIELDS or plan["page_size"] != 500:
        raise ValueError("source selection or request fields differ from frozen plan")
    pmids = sorted({x.removeprefix("PMID:") for row in selected.values()
                    for x in row["definition_citation_ids"]}, key=int)
    if pmids != plan["pmids"]:
        raise ValueError("incomplete or duplicated source bibliography query plan")
    entries, queries, query_members = {}, {}, {}
    for pmid in pmids:
        rows, queries[pmid] = read_query(root, directory, pmid)
        query_members[pmid] = sorted(rows)
        for acc, entry in rows.items():
            if acc in entries and entries[acc] != entry:
                raise ValueError("protein metadata differs between literature queries")
            entries[acc] = entry
    releases = {row["release"] for row in queries.values()}
    if releases != {prior["release"]}:
        raise ValueError("literature responses do not share the prior reference release")
    terms = derive_terms(selected, entries, query_members)
    selected_ids = {v for row in terms.values() for v in row["record_memberships"]}
    records = [row for row in records if row["identifier"] in selected_ids]
    if records != plan["records"]:
        raise ValueError("selected record pins differ from preflight")
    tax_snapshot = json.loads(paths["taxonomy_snapshot"].read_bytes())
    taxa = dict(tax_snapshot["taxa"])
    reused_taxonomy = []
    for item in prior["taxonomy_requests"].values():
        path = reference.check_pin(root, item["cache"])
        reference.check_pin(root, item["receipt"])
        row = json.loads(path.read_bytes())
        if str(row["taxonId"]) in taxa:
            raise ValueError("reused taxonomy would overwrite a prior context")
        taxa[str(row["taxonId"])] = row
        reused_taxonomy.append(item["cache"])
    matched = {c["protein_accession"].removeprefix("UniProtKB:") for row in terms.values()
               for c in row["reference_candidates"]}
    missing = sorted({entries[acc]["organism"]["taxonId"] for acc in matched
                      if str(entries[acc]["organism"]["taxonId"]) not in taxa})
    tax_plan = {"source_plan": reference.pin(root, plan_path),
                "query_inputs": [item for row in queries.values() for page in row["pages"]
                                 for item in (page["cache"], page["receipt"])],
                "matched_accessions": sorted(matched), "new_taxon_ids": missing,
                "reused_taxonomy_caches": reused_taxonomy}
    return {"plan": plan, "plan_path": plan_path, "paths": paths, "census": census, "prior": prior,
            "terms": terms, "entries": entries, "queries": queries, "records": records,
            "taxa": taxa, "tax_plan": tax_plan}


def analyze(root, directory, only=None):
    data = collect(root, directory)
    tax_plan_path = directory / "taxonomy-plan.json"
    if json.loads(tax_plan_path.read_bytes()) != data["tax_plan"]:
        raise ValueError("taxonomy query plan does not reproduce")
    taxa, requests = data["taxa"], {}
    for taxid in data["tax_plan"]["new_taxon_ids"]:
        key = f"tax-{taxid}"
        taxa[str(taxid)], requests[key] = reference.read_response(root, directory, key, f"/taxonomy/{taxid}")
        if requests[key]["release"] != data["prior"]["release"]:
            raise ValueError("new taxonomy release differs from literature queries")
    selected = set(data["terms"]) if only is None else set(only)
    if not selected or not selected <= set(data["terms"]):
        raise ValueError("invalid term selection")
    terms = {tid: data["terms"][tid] for tid in sorted(selected)}
    matched = {c["protein_accession"].removeprefix("UniProtKB:") for row in terms.values()
               for c in row["reference_candidates"]}
    proteins = {"UniProtKB:" + acc: concordance.project_entry(data["entries"][acc],
                taxa[str(data["entries"][acc]["organism"]["taxonId"])]) for acc in sorted(matched)}
    old_entries = json.loads(data["paths"]["protein_snapshot"].read_bytes())["entries"]
    selected_records = {v for row in terms.values() for v in row["record_memberships"]}
    result = {
        "scope": SCOPE, "selection": "FULL_59_TERM_COHORT" if only is None else "CANARY_ONLY",
        "inputs": {**data["plan"]["inputs"], "plan": reference.pin(root, data["plan_path"]),
                   "taxonomy_plan": reference.pin(root, tax_plan_path)},
        "release": data["prior"]["release"], "queries": data["queries"], "taxonomy_requests": requests,
        "terms": terms, "proteins": proteins,
        "records": [r for r in data["records"] if r["identifier"] in selected_records],
        "summary": {
            "corpus_records_checked": len(data["census"]), "selected_terms": len(terms),
            "selected_assertion_memberships": sum(len(r["record_memberships"]) for r in terms.values()),
            "selected_records": len(selected_records), "completed_queries": len(data["queries"]),
            "response_pages": sum(len(q["pages"]) for q in data["queries"].values()),
            "queries_with_zero_results": sum(q["result_count"] == 0 for q in data["queries"].values()),
            "paginated_queries_completed": sum(len(q["pages"]) > 1 for q in data["queries"].values()),
            "unique_literature_entries_inspected": len(data["entries"]),
            "terms_with_reference_candidates": sum(bool(r["reference_candidates"]) for r in terms.values()),
            "reference_candidate_links": sum(len(r["reference_candidates"]) for r in terms.values()),
            "reference_proteins": len(proteins), "reference_taxa": len({p["reference_taxon_id"]
                                                                        for p in proteins.values()}),
            "references_outside_prior_card_snapshot": len(matched - set(old_entries)),
            "new_taxonomy_requests": len(requests),
            "entry_types": dict(sorted(Counter(p["entry_type"] for p in proteins.values()).items())),
            "biological_records_changed": 0, "exact_allele_assignments": 0, "whole_records_completed": 0,
        },
        "limits": [
            "This is the 59-term follow-up cohort, not completion of the whole 2939-record objective.",
            "All source citations in this cohort were queried without a CARD-database filter.",
            "Complete queries and matching names do not verify an experimental allele, isolate or phenotype.",
            "No hit is not evidence of absence: missing synonyms or unindexed literature may explain it.",
            "A reference TaxID and a paper containing several genes do not establish a same-isolate join.",
            "No sequences, exact variants, coordinates, protocols or numerical AST are exported.",
            "Biological records and prior source-link status remain unchanged; primary review remains OPEN.",
        ],
    }
    for item in data["plan"]["inputs"].values():
        reference.check_pin(root, item)
    for row in data["census"]:
        reference.check_pin(root, {"path": row["path"], "sha256": row["record_sha256"]})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--directory", type=Path, default=DEFAULT_DIRECTORY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--prepare-taxonomy", action="store_true")
    parser.add_argument("--only", action="append")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    directory = args.root / args.directory
    if args.prepare_taxonomy:
        if args.only or args.check:
            raise ValueError("taxonomy planning requires the full cohort without --check")
        result = collect(args.root, directory)["tax_plan"]
        output = directory / "taxonomy-plan.json"
    else:
        result = analyze(args.root, directory, args.only)
        output = args.root / args.output
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.check:
        if output.read_bytes() != payload:
            raise ValueError("literature-protein dossier does not reproduce")
    else:
        with output.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result.get("summary", {"new_taxon_ids": result.get("new_taxon_ids"),
        "matched_accessions": len(result.get("matched_accessions", []))}), sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
