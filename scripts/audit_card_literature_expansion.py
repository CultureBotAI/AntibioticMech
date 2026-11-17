"""Replay the remaining unlinked CARD bibliography without biological writes."""

import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import audit_card_citation_concordance as concordance
import audit_card_definition_citations as definitions
import audit_card_grounding as card
import audit_card_literature_proteins as literature
import audit_topoisomerase_references as reference

DIRECTORY = Path("reports/resistance-grounding-2026-10-13-card-literature-expansion")
OUTPUT = Path("research/2026-10-13-card-literature-expansion.json")
SCOPE = "LITERATURE_CONSTRAINED_REFERENCE_CANDIDATES_NOT_EXPERIMENTAL_ALLELES_OR_PHENOTYPES"
NONPROTEIN = {"RNA_TERM_NOT_A_PROTEIN_PRODUCT", "GENE_CLUSTER_NOT_ONE_PROTEIN",
              "MULTIPLE_ENTITY_SCOPES_REQUIRE_REVIEW"}
IDENTITY_REVIEW = {
    "path": "research/2026-10-09-rpld-reference-grounding.json",
    "sha256": "803fb2091d65211f9e399c5a9e28899afa42c34af96484585229428f0fc2b56c",
}


def scope_reviews(root, source_scope_pin):
    review = json.loads(reference.check_pin(root, IDENTITY_REVIEW).read_bytes())
    if (review["status"] != "PROTEIN_PRODUCT_IDENTITY_SUPPORTED_EXPERIMENTAL_GROUNDING_PENDING"
            or review["source_claim"]["aro_id"] != "ARO:3004956"
            or source_scope_pin not in review["ontology_conflict"]["historical_audits"]):
        raise ValueError("identity review does not match the historical scope audit")
    return {"ARO:3004956": {
        "entity_scope": "PROTEIN_PRODUCT_WITH_CONFLICTING_RNA_ANCESTRY",
        "historical_entity_scope": review["ontology_conflict"]["historical_entity_scope"],
        "source": IDENTITY_REVIEW, "experimental_identity_assigned": False,
        "status": review["status"],
    }}


def selection(direct, source, prior, scopes, labels):
    if set(labels) != set(direct["determinants"]) or set(labels) != set(source["terms"]):
        raise ValueError("source term membership drift")
    selected = {}
    for tid, row in source["terms"].items():
        if definitions.text_hash(labels[tid]) != row["label_sha256"]:
            raise ValueError("source label digest differs")
        if direct["determinants"][tid]["candidates"] or tid in prior["terms"]:
            continue
        selected[tid] = {
            "source_label": labels[tid], "source_label_sha256": row["label_sha256"],
            "definition_citation_ids": row["definition_citation_ids"],
            "record_memberships": row["record_memberships"],
            "entity_scope": scopes["terms"][tid]["entity_scope"],
        }
    return selected


def read_query(root, directory, pmid):
    """Only complete, validated cursor chains contribute candidate entries."""
    path = directory / f"pmid-{pmid}-response.bin"
    receipt_path = directory / f"pmid-{pmid}-receipt.json"
    if not path.exists() and not receipt_path.exists():
        return {}, {"status": "NOT_QUERIED", "complete_for_query": False}
    if not path.exists() or not receipt_path.exists():
        raise ValueError("orphaned first-page response or receipt")
    receipt = json.loads(receipt_path.read_bytes())
    parameters = literature.parameters(pmid)
    url = urlparse(receipt["url"])
    if (url.scheme != "https" or url.netloc != "rest.uniprot.org"
            or url.path != "/uniprotkb/search" or url.fragment
            or parse_qs(url.query, keep_blank_values=True) != {k: [v] for k, v in parameters.items()}
            or receipt["query"] != parameters["query"]):
        raise ValueError("first-page request identity drift")
    if receipt["sha256"] != reference.digest(path) or receipt["bytes"] != path.stat().st_size:
        raise ValueError("first-page response digest or length mismatch")
    first = {"cache": reference.pin(root, path), "receipt": reference.pin(root, receipt_path)}
    if receipt["status"] != 200:
        return {}, {"status": "SOURCE_REQUEST_FAILED", "http_status": receipt["status"],
                    "first_page": first, "complete_for_query": False}
    try:
        entries, query = literature.read_query(root, directory, pmid)
    except FileNotFoundError:
        return {}, {"status": "CURSOR_TRAVERSAL_PENDING", "first_page": first,
                    "complete_for_query": False}
    return entries, {**query, "status": "COMPLETE_QUERY_NOT_PRIMARY_REVIEW"}


def match_terms(selected, entries, members, queries, reviews=None):
    result = {}
    for tid, row in sorted(selected.items()):
        pmids = [c.removeprefix("PMID:") for c in row["definition_citation_ids"] if c.startswith("PMID:")]
        pool = {acc for pmid in pmids for acc in members[pmid]}
        matches = []
        for acc in sorted(pool):
            names, direct = literature.match_entry(entries[acc], tid, row["source_label"])
            if names or direct:
                matches.append({"protein_accession": "UniProtKB:" + acc,
                    "source_citation_ids": ["PMID:" + p for p in pmids if acc in members[p]],
                    "literal_gene_matches": names, "explicit_card_xref": direct,
                    "experimental_identity_assigned": False})
        review = (reviews or {}).get(tid)
        if review and review["historical_entity_scope"] != row["entity_scope"]:
            raise ValueError("reviewed term has a different source entity scope")
        scope = review["entity_scope"] if review else row["entity_scope"]
        withheld = scope in NONPROTEIN
        pending = ["PMID:" + p for p in pmids if not queries[p]["complete_for_query"]]
        other = [c for c in row["definition_citation_ids"] if not c.startswith("PMID:")]
        result[tid] = {k: row[k] for k in (
            "source_label_sha256", "definition_citation_ids", "record_memberships", "entity_scope")}
        result[tid].update({"reference_candidates": [] if withheld else matches,
            "source_entity_scope": row["entity_scope"], "entity_scope": scope,
            "entity_scope_basis": "REVIEWED_IDENTITY" if review else "ONTOLOGY_ANCESTRY_ONLY",
            "entity_identity_review": review,
            "entity_scope_withheld_matches": matches if withheld else [],
            "complete_query_entries_inspected": len(pool), "pending_pubmed_queries": pending,
            "other_citations_not_queried": other,
            "all_source_citations_queried": (
                bool(row["definition_citation_ids"]) and not pending and not other),
            "no_match_establishes_biological_absence": False,
            "primary_review_status": "OPEN_NOT_COMPLETED_BY_METADATA_LOOKUP"})
    return result


def record_summary(census, terms):
    result = {}
    for row in census:
        result[row["identifier"]] = {
            "identifier": row["identifier"], "path": row["path"],
            "record_sha256": row["record_sha256"], "standard_inchi_key": row["standard_inchi_key"],
            "cohort_terms": [], "terms_with_reference_candidates": [],
            "cohort_assertion_memberships": 0,
            "pending_citation_terms": [], "terms_without_source_citations": [],
            "whole_record_primary_review": "OPEN"}
    if len(result) != len(census):
        raise ValueError("duplicate record identity in census")
    for tid, row in sorted(terms.items()):
        for identifier in row["record_memberships"]:
            if identifier not in result:
                raise ValueError("term refers to a record outside the census")
            record = result[identifier]
            record["cohort_assertion_memberships"] += 1
            if tid in record["cohort_terms"]:
                continue
            record["cohort_terms"].append(tid)
            if row["reference_candidates"]:
                record["terms_with_reference_candidates"].append(tid)
            if row["pending_pubmed_queries"] or row["other_citations_not_queried"]:
                record["pending_citation_terms"].append(tid)
            if not row["definition_citation_ids"]:
                record["terms_without_source_citations"].append(tid)
    return list(result.values())


def collect(root, directory):
    plan_path = directory / "plan.json"
    plan = json.loads(plan_path.read_bytes())
    paths = {k: reference.check_pin(root, p) for k, p in plan["inputs"].items()}
    data = {k: json.loads(p.read_bytes()) for k, p in paths.items() if k != "census"}
    census, labels, memberships, records = definitions.read_corpus(root, paths["census"])
    selected = selection(data["direct"], data["definitions"], data["prior_literature"],
                         data["term_scope"], labels)
    if selected != plan["selected_terms"] or records != plan["records"]:
        raise ValueError("planned source cohort or record pins differ")
    if any(sorted(memberships[t]) != row["record_memberships"] for t, row in selected.items()):
        raise ValueError("source record membership drift")
    pmids = sorted({c.removeprefix("PMID:") for row in selected.values()
                    for c in row["definition_citation_ids"] if c.startswith("PMID:")}, key=int)
    if pmids != plan["pmids"] or plan["fields"] != card.FIELDS or plan["page_size"] != 500:
        raise ValueError("query plan drift")
    reused = {p: q for p, q in data["prior_literature"]["queries"].items() if p in pmids}
    if reused != plan["reused_queries"]:
        raise ValueError("reused query provenance differs")
    for query in reused.values():
        for page in query["pages"]:
            for key in ("cache", "receipt"):
                original = reference.check_pin(root, page[key])
                if reference.digest(directory / original.name) != page[key]["sha256"]:
                    raise ValueError("reused query copy differs from original")
    entries, members, queries = {}, {}, {}
    for pmid in pmids:
        rows, queries[pmid] = read_query(root, directory, pmid)
        members[pmid] = sorted(rows)
        if (queries[pmid]["complete_for_query"]
                and queries[pmid]["release"] != data["direct"]["summary"]["release"]):
            raise ValueError("query release differs from source reference audit")
        for acc, entry in rows.items():
            if acc in entries and entry != entries[acc]:
                raise ValueError("conflicting entry metadata across queries")
            entries[acc] = entry
    reviews = scope_reviews(root, plan["inputs"]["term_scope"])
    if not set(reviews) <= set(selected):
        raise ValueError("reviewed scope term is outside the cohort")
    terms = match_terms(selected, entries, members, queries, reviews)
    matched = {c["protein_accession"].removeprefix("UniProtKB:") for r in terms.values()
               for c in r["reference_candidates"]}
    prior = data["prior_literature"]
    snapshot = prior["inputs"]["taxonomy_snapshot"]
    taxa = json.loads(reference.check_pin(root, snapshot).read_bytes())["taxa"]
    taxonomy_sources = [snapshot]
    parent = json.loads(reference.check_pin(root, prior["inputs"]["concordance"]).read_bytes())
    for item in [*parent["taxonomy_requests"].values(), *prior["taxonomy_requests"].values()]:
        reference.check_pin(root, item["receipt"])
        taxon = json.loads(reference.check_pin(root, item["cache"]).read_bytes())
        key = str(taxon["taxonId"])
        if key in taxa and taxa[key] != taxon:
            raise ValueError("reused taxonomy conflict")
        taxa[key] = taxon
        taxonomy_sources.extend([item["cache"], item["receipt"]])
    missing = sorted({entries[acc]["organism"]["taxonId"] for acc in matched
                      if str(entries[acc]["organism"]["taxonId"]) not in taxa})
    return {"plan": plan, "paths": paths, "plan_path": plan_path, "census": census,
            "terms": terms, "entries": entries, "queries": queries, "matched": matched,
            "taxa": taxa, "taxonomy_sources": taxonomy_sources, "missing_taxa": missing}


def analyze(root, directory, *, prepare_taxonomy=False):
    data = collect(root, directory)
    tax_plan = {"source_plan": reference.pin(root, data["plan_path"]),
                "new_taxon_ids": data["missing_taxa"], "matched_accessions": sorted(data["matched"]),
                "reused_taxonomy_sources": data["taxonomy_sources"],
                "query_inputs": [p for q in data["queries"].values() for page in q.get("pages", [])
                                 for k, p in page.items() if k in {"cache", "receipt"}]}
    if prepare_taxonomy:
        return tax_plan
    tax_plan_path = directory / "taxonomy-plan.json"
    if json.loads(tax_plan_path.read_bytes()) != tax_plan:
        raise ValueError("taxonomy query plan differs")
    taxa, requests = data["taxa"], {}
    for taxid in data["missing_taxa"]:
        taxa[str(taxid)], requests[str(taxid)] = reference.read_response(
            root, directory, f"tax-{taxid}", f"/taxonomy/{taxid}")
        if requests[str(taxid)]["release"] != "2026_03":
            raise ValueError("taxonomy release differs")
    proteins = {"UniProtKB:" + acc: concordance.project_entry(
        data["entries"][acc], taxa[str(data["entries"][acc]["organism"]["taxonId"])])
        for acc in sorted(data["matched"])}
    terms, queries = data["terms"], data["queries"]
    record_ids = {i for row in terms.values() for i in row["record_memberships"]}
    result = {
        "scope": SCOPE, "selection": "COMPLEMENT_OF_PRIOR_59_TERM_LITERATURE_COHORT",
        "inputs": {**data["plan"]["inputs"],
            "identity_review": IDENTITY_REVIEW,
            "plan": reference.pin(root, data["plan_path"]),
            "taxonomy_plan": reference.pin(root, tax_plan_path)},
        "terms": terms, "proteins": proteins, "queries": queries, "taxonomy_requests": requests,
        "records": record_summary(data["census"], terms),
        "reused_queries": data["plan"]["reused_queries"], "taxonomy_sources": data["taxonomy_sources"],
        "summary": {"corpus_records_checked": len(data["census"]), "selected_terms": len(terms),
            "selected_records": len(record_ids),
            "selected_assertion_memberships": sum(len(r["record_memberships"]) for r in terms.values()),
            "citation_queries": len(queries),
            "query_status_counts": dict(Counter(q["status"] for q in queries.values())),
            "complete_query_zero_results": sum(q.get("result_count") == 0 for q in queries.values()),
            "terms_without_source_citations": sum(not r["definition_citation_ids"] for r in terms.values()),
            "terms_with_unqueried_other_citations": sum(
                bool(r["other_citations_not_queried"]) for r in terms.values()),
            "unique_entries_in_complete_queries": len(data["entries"]),
            "terms_with_reference_candidates": sum(bool(r["reference_candidates"]) for r in terms.values()),
            "reference_candidate_links": sum(len(r["reference_candidates"]) for r in terms.values()),
            "reference_proteins": len(proteins),
            "reference_taxa": len({p["reference_taxon_id"] for p in proteins.values()}),
            "reviewed_scope_conflicts": sum(bool(r["entity_identity_review"]) for r in terms.values()),
            "biological_records_changed": 0, "experimental_alleles_assigned": 0,
            "whole_records_completed": 0},
        "limits": ["No primary experimental evidence is verified by citation/name concordance.",
            "Incomplete searches contribute no entries and are not negative results.",
            "An empty query is not biological absence; missing annotations and synonyms remain possible.",
            "Whole clusters and RNA terms are not assigned individual protein candidates.",
            "Source entity scopes describe ontology ancestry, not biological identity; "
            "the prior rplD protein-identity review is preserved separately.",
            "Other entity scopes, including efflux terms, still require granularity and subject review.",
            "Gene names, reference organisms and shared papers do not establish "
            "experimental alleles or phenotypes.",
            "The previous direct-link and 59-term audits remain unchanged; this is a complementary cohort.",
            "No sequences, variant specifications, protocols or numeric AST are exported.",
            "NCBI requests and contact remain prohibited; issue 1040 and reuse-terms work remain deferred."],
        "attribution": {"source": "UniProt Consortium and CARD curation team",
            "uniprot_license": "CC BY 4.0", "uniprot_license_url": "https://www.uniprot.org/help/license",
            "card_ontology_attribution": json.loads(data["paths"]["term_scope"].read_bytes())["attribution"]},
    }
    for item in data["plan"]["inputs"].values():
        reference.check_pin(root, item)
    for row in data["census"]:
        reference.check_pin(root, {"path": row["path"], "sha256": row["record_sha256"]})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--directory", type=Path, default=DIRECTORY)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--prepare-taxonomy", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = analyze(args.root, args.root / args.directory, prepare_taxonomy=args.prepare_taxonomy)
    output = args.root / (args.directory / "taxonomy-plan.json" if args.prepare_taxonomy else args.output)
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.check:
        if output.read_bytes() != payload:
            raise ValueError("literature expansion does not reproduce")
    else:
        with output.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result.get("summary", {"new_taxon_ids": result.get("new_taxon_ids")})), flush=True)


if __name__ == "__main__":
    main()
