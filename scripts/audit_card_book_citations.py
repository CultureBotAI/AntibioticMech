"""Recover source-bound book bibliography without promoting allele evidence."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path

import audit_card_definition_citations as citations
import audit_topoisomerase_references as reference
from rdflib import OWL, RDF, Graph, Literal

PRIOR = Path("research/2026-10-09-card-definition-citations.json")
CENSUS = Path("research/2026-10-13-blasticidin-deaminase-resistance-grounding.tsv")
EXPANSION = Path("research/2026-10-13-card-literature-expansion.json")
OUTPUT = Path("research/2026-10-13-card-book-citations.json")
SCOPE = "SOURCE_BOUND_BIBLIOGRAPHY_NOT_EXPERIMENTAL_GENE_ALLELE_OR_PHENOTYPE_EVIDENCE"


def isbn13(value):
    """Accept only explicit ISBN-13 literals with a valid checksum."""
    if not isinstance(value, Literal) or not re.fullmatch(r"ISBN:[0-9]+(?:-[0-9]+)*", str(value)):
        return None
    digits = str(value).removeprefix("ISBN:").replace("-", "")
    if len(digits) != 13 or not digits.startswith(("978", "979")):
        return None
    if sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits)) % 10:
        return None
    return "ISBN:" + digits


def project(graph, labels):
    original = citations.project_annotations(graph, labels)
    result = {tid: {"label_sha256": row["label_sha256"],
                    "definition_pubmed_doi_ids": row["definition_citation_ids"],
                    "isbn_definition_annotations": [], "unresolved_definition_xrefs": [],
                    "biological_support_inferred": False, "primary_review_status": "OPEN"}
              for tid, row in original.items()}
    # The original projection validates every selected annotated RDF triple first.
    for axiom in graph.subjects(RDF.type, OWL.Axiom):
        tid = citations.ontology.curie(str(graph.value(axiom, OWL.annotatedSource)))
        if tid not in result or graph.value(axiom, OWL.annotatedProperty) != citations.DEFINITION:
            continue
        target = citations.rdf_identity(graph.value(axiom, OWL.annotatedTarget))
        for value in graph.objects(axiom, citations.XREF):
            normalized = isbn13(value)
            if normalized:
                result[tid]["isbn_definition_annotations"].append({
                    "identifier": normalized, "source_identifier": str(value),
                    "source_identifier_sha256": citations.text_hash(value),
                    "predicate": str(citations.DEFINITION), "target": target})
            elif not citations.bibliography([value])["identifiers"]:
                result[tid]["unresolved_definition_xrefs"].append(citations.rdf_identity(value))
    for row in result.values():
        for key in ("isbn_definition_annotations", "unresolved_definition_xrefs"):
            row[key] = sorted({json.dumps(v, sort_keys=True) for v in row[key]})
            row[key] = [json.loads(v) for v in row[key]]
        row["definition_isbn13_ids"] = sorted({v["identifier"] for v in row["isbn_definition_annotations"]})
        paper, book, unresolved = [bool(row[k]) for k in (
            "definition_pubmed_doi_ids", "definition_isbn13_ids", "unresolved_definition_xrefs")]
        row["bibliography_status"] = (
            "PUBMED_DOI_AND_BOOK_REFERENCES" if paper and book else
            "BOOK_REFERENCE_WITHOUT_PUBMED_DOI" if book else
            "PUBMED_DOI_REFERENCES" if paper else
            "UNRECOGNIZED_DEFINITION_REFERENCES_REQUIRE_REVIEW" if unresolved else
            "NO_DEFINITION_BIBLIOGRAPHY_IN_PINNED_SOURCE")
    return result, original


def record_rows(census, terms):
    rows = {r["identifier"]: {
        "identifier": r["identifier"], "path": r["path"], "record_sha256": r["record_sha256"],
        "standard_inchi_key": r["standard_inchi_key"], "book_citing_terms": [],
        "book_reference_assertion_memberships": 0, "whole_record_primary_review": "OPEN"}
        for r in census}
    if len(rows) != len(census):
        raise ValueError("duplicate census identifier")
    for tid, term in sorted(terms.items()):
        for identifier in term["record_memberships"]:
            if identifier not in rows:
                raise ValueError("source membership outside census")
            if term["definition_isbn13_ids"]:
                rows[identifier]["book_reference_assertion_memberships"] += 1
                if tid not in rows[identifier]["book_citing_terms"]:
                    rows[identifier]["book_citing_terms"].append(tid)
    return list(rows.values())


def analyze(root):
    prior = json.loads((root / PRIOR).read_bytes())
    expansion = json.loads((root / EXPANSION).read_bytes())
    cache_path = reference.check_pin(root, prior["inputs"]["ontology_cache"])
    reference.check_pin(root, prior["inputs"]["source_inventory"])
    cache = json.loads(cache_path.read_bytes())
    if cache["status"] != 200 or citations.text_hash(cache["body"]) != cache["sha256"]:
        raise ValueError("ontology response status or checksum mismatch")
    census, labels, memberships, _ = citations.read_corpus(root, root / CENSUS)
    if set(labels) != set(prior["terms"]):
        raise ValueError("source term membership drift")
    graph = Graph().parse(data=cache["body"], format="xml")
    terms, original = project(graph, labels)
    for tid, row in original.items():
        row["record_memberships"] = sorted(memberships[tid])
        if row != prior["terms"][tid]:
            raise ValueError("original citation audit does not reproduce")
        terms[tid]["record_memberships"] = sorted(memberships[tid])
    uncited = {t for t, row in expansion["terms"].items() if not row["definition_citation_ids"]}
    if not uncited <= set(terms) or any(terms[t]["definition_pubmed_doi_ids"] for t in uncited):
        raise ValueError("historical no-PMID/DOI cohort drift")
    records = record_rows(census, terms)
    books = {t for t, row in terms.items() if row["definition_isbn13_ids"]}
    return {
        "scope": SCOPE, "date": "2026-10-13",
        "inputs": {"prior": reference.pin(root, root / PRIOR),
            "expansion": reference.pin(root, root / EXPANSION),
            "current_census": reference.pin(root, root / CENSUS),
            "ontology_cache": prior["inputs"]["ontology_cache"],
            "source_inventory": prior["inputs"]["source_inventory"]},
        "terms": terms, "records": records,
        "summary": {"records_checked": len(census), "card_terms_checked": len(terms),
            "terms_with_book_references": len(books),
            "book_identifiers": sorted({v for t in books for v in terms[t]["definition_isbn13_ids"]}),
            "book_reference_records": sum(bool(r["book_citing_terms"]) for r in records),
            "book_reference_assertion_memberships": sum(
                r["book_reference_assertion_memberships"] for r in records),
            "historical_expansion_terms_without_pubmed_doi": len(uncited),
            "historical_uncited_terms_with_book_references": len(uncited & books),
            "historical_uncited_terms_still_without_recognized_references": len(uncited - books),
            "bibliography_status_counts": dict(Counter(r["bibliography_status"] for r in terms.values())),
            "whole_records_completed": 0, "experimental_assignments": 0, "biological_records_changed": 0},
        "book_metadata": {"ISBN:9789240082410": {
            "publisher": "World Health Organization", "edition": "2nd", "publication_date": "2023-11-15",
            "title": "Catalogue of mutations in Mycobacterium tuberculosis complex "
                     "and their association with drug resistance",
            "landing_page": "https://www.who.int/southeastasia/publications/i/item/9789240082410",
            "metadata_checked_on": "2026-10-13", "inspection": "WEB_LANDING_PAGE_METADATA_ONLY",
            "corrigendum_listed": "2024-01-17", "corrigendum_inspected": False,
            "pdf_or_variant_catalogue_downloaded": False, "catalogue_rows_reviewed": False,
            "reuse_terms_assessed": False, "source_adopted": False}},
        "limits": [
            "The old no-citation counts meant no recognized PMID/DOI, not an absence of all bibliography.",
            "ISBN presence identifies a cited book, not a verified row, "
            "experimental allele, taxon or phenotype.",
            "Only direct definition-bound references are admitted; "
            "parent, synonym and class citations do not propagate.",
            "Unsupported or malformed identifiers remain hashed and unresolved, not silently discarded.",
            "Historical snapshots are unchanged; this is a bibliographic successor, "
            "not a biological rewrite.",
            "No sequences, variant specifications, constructs, protocols or numeric AST are exported.",
            "No new NCBI requests, source adoption or GitHub actions; issue 1040 remains deferred."],
        "attribution": {"source": "CARD curation team (ARO ontology)", "license": "CC BY 4.0",
                        "license_url": "https://github.com/arpcard/aro/blob/master/LICENSE"},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = analyze(args.root)
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    path = args.root / args.output
    if args.check:
        if path.read_bytes() != payload:
            raise ValueError("book citation audit does not reproduce")
    else:
        with path.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"]), flush=True)


if __name__ == "__main__":
    main()
