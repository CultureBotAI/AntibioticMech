"""Replay myriocin reference identities and a YPK1 homonym, without network access."""

import argparse
import csv
import json
from pathlib import Path

import audit_topoisomerase_references as reference

from antibioticmech.activity_collections import load_record

DEFAULT_CACHE = Path("reports/resistance-grounding-2026-10-13-myriocin")
DEFAULT_OUTPUT = Path("research/2026-10-13-myriocin-reference-context.json")
QUERIES = {
    "sli1": "gene_exact:SLI1 AND organism_id:559292 AND reviewed:true",
    "ypk1": "gene_exact:YPK1 AND organism_id:559292 AND reviewed:true",
}
FOCAL = {"15025559": "10.1042/bj20040108", "10825204": "10.1128/mcb.20.12.4411-4419.2000"}


def project_candidate(entry, query_gene, taxonomy):
    if "features" in entry or entry["organism"]["taxonId"] != 559292:
        raise ValueError("unexpected feature export or reference organism")
    projected = reference.project_reference(entry, query_gene, 4932, taxonomy)
    primary_gene, = [g["geneName"]["value"] for g in entry["genes"]]
    ids = {i["id"].lower() for b in projected["bibliography"] for i in b["identifiers"]}
    projected.update({
        "primary_gene_name": primary_gene, "query_gene": query_gene,
        "query_match_kind": "PRIMARY_NAME" if primary_gene == query_gene else "SYNONYM",
        "focal_bibliography_matches": sorted(p for p, doi in FOCAL.items() if p in ids or doi in ids),
        "gene_orf_names": sorted({v["value"] for g in entry["genes"] for v in g.get("orfNames", [])}),
        "compound_specific_resistance_established": False,
    })
    return projected


def resolve_ypk1(candidates):
    """Use independent name, locus and citation context, not a first-hit choice."""
    decisions = {}
    for candidate in candidates:
        accession = candidate["protein_accession"]
        if accession in decisions:
            raise ValueError("duplicate reference candidate")
        checks = {
            "primary_name_ypk1": candidate["primary_gene_name"] == "YPK1",
            "sli2_alias": "SLI2" in candidate["gene_names"],
            "ykl126w_locus": "YKL126W" in candidate["ordered_locus_names"],
            "sli2_discovery_paper_in_bibliography": "10825204" in candidate["focal_bibliography_matches"],
        }
        decisions[accession] = {
            "identity_checks": checks,
            "disposition": "CONCORDANT_REFERENCE_IDENTITY" if all(checks.values())
            else "NOT_SUPPORTED_FOR_THIS_LEAD",
            "negative_resistance_phenotype_inferred": False,
        }
    selected = [key for key, value in decisions.items()
                if value["disposition"] == "CONCORDANT_REFERENCE_IDENTITY"]
    if len(selected) != 1:
        raise ValueError("YPK1/SLI2 reference identity remains unresolved or ambiguous")
    return {"selected_reference": selected[0], "candidates": decisions,
            "experimental_allele_assignment": False, "biological_claim_curated": False}


def build(root, directory):
    plan_path = directory / "cohort.json"
    plan = json.loads(plan_path.read_bytes())
    if plan["queries"] != QUERIES or plan["fields"] != reference.FIELDS:
        raise ValueError("bounded query plan changed")
    canary_path = directory / "canary-reviewed.json"
    canary = json.loads(canary_path.read_bytes())
    if canary["manually_reviewed"] is not True:
        raise ValueError("canary review missing")
    for field, suffix in (("response", "response.bin"), ("receipt", "receipt.json")):
        expected = reference.pin(root, directory / f"sli1-{suffix}")
        if canary[field] != expected:
            raise ValueError("canary does not match the reviewed sli1 query")
    record = load_record(reference.check_pin(root, plan["record"]))
    if (record["identifier"] != "CHEBI:582124" or record.get("resistance_mechanisms")
            or record["chemical_structure"]["standard_inchi_key"] != "ZZIKIHCNFWXKDY-GNTQXERDSA-N"
            or plan["exact_alias"] not in record["synonyms"]):
        raise ValueError("compound identity or evidence changed")
    with reference.check_pin(root, plan["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    row, = [r for r in census if r["identifier"] == record["identifier"]]
    if len(census) != 2939 or row["record_sha256"] != plan["record"]["sha256"]:
        raise ValueError("historical corpus pin changed")
    discovery = json.loads(reference.check_pin(root, plan["discovery"]).read_bytes())
    lead, = [r for r in discovery["records"] if r["identifier"] == record["identifier"]]
    alias, = [n for n in lead["names"] if n["text"] == "ISP-1"]
    if alias["shared_with_record_ids"] or alias["origins"] != [{
        "index": 3, "kind": "SYNONYM", "source": "chebi", "synonym_type": "EXACT_SYNONYM",
    }]:
        raise ValueError("ISP-1 exact synonym grounding changed")
    papers = {c["pmid"]: c["doi"].lower() for q in lead["queries"] for c in q["candidates"]
              if c.get("pmid") in FOCAL}
    if papers != FOCAL:
        raise ValueError("focal DOI/PMID metadata changed")
    previous_tax = json.loads(reference.check_pin(root, plan["taxonomy_dossier"]).read_bytes())
    old = previous_tax["taxonomy_request"]
    for pin in (old["cache"], old["receipt"]):
        reference.check_pin(root, pin)
    taxonomy, tax_request = reference.read_response(
        root, (root / old["cache"]["path"]).parent, "tax-559292", "/taxonomy/559292")
    if tax_request != old:
        raise ValueError("taxonomy reuse changed")
    requests, proteins, raw_entries = {}, {}, {}
    for key, query in QUERIES.items():
        params = {"query": [query], "format": ["json"], "size": ["500"], "fields": [reference.FIELDS]}
        body, request = reference.read_response(root, directory, key, "/uniprotkb/search", params)
        if request["release"] != tax_request["release"]:
            raise ValueError("reference and taxonomy releases differ")
        expected_genes = {"SLI1"} if key == "sli1" else {"YPK1", "MCK1"}
        returned = []
        for entry in body["results"]:
            result = project_candidate(entry, key.upper(), taxonomy)
            returned.append(result["primary_gene_name"])
            proteins[result["protein_accession"]] = result
            raw_entries[result["primary_gene_name"]] = entry
        if set(returned) != expected_genes or len(returned) != len(expected_genes):
            raise ValueError("query candidate inventory changed")
        requests[key] = {**request, "results": len(returned), "complete_for_query": True,
                         "all_strains_or_unreviewed_entries_searched": False}
    resolution = resolve_ypk1([p for p in proteins.values() if p["query_gene"] == "YPK1"])
    sli1, = [p for p in proteins.values() if p["primary_gene_name"] == "SLI1"]
    if sli1["ordered_locus_names"] != ["YGR212W"] or "15025559" not in sli1["focal_bibliography_matches"]:
        raise ValueError("SLI1 locus and citation do not corroborate the discovery lead")
    archive = []
    for xref in raw_entries["SLI1"].get("uniProtKBCrossReferences", []):
        if xref["database"] == "EMBL":
            for prop in xref.get("properties", []):
                if prop["key"] == "ProteinId":
                    archive.append({"nucleotide_accession": xref["id"], "protein_accession": prop["value"]})
    if {"nucleotide_accession": "Z72997", "protein_accession": "CAA97239.1"} not in archive:
        raise ValueError("SLI1 reference archive crosswalk changed")
    receipt_path, body_path = directory / "publisher-receipt.json", directory / "publisher-response.bin"
    receipt = json.loads(receipt_path.read_bytes())
    if (receipt["url"] != plan["primary"]["pdf_url"] or receipt["status"] != 403
            or receipt["sha256"] != reference.digest(body_path) or receipt["is_pdf"]
            or body_path.read_bytes().startswith(b"%PDF-") or receipt["retry_performed"]):
        raise ValueError("publisher access observation changed")
    for key in ("prior_progress", "prior_checkpoint"):
        reference.check_pin(root, plan[key])
    return {
        "date": "2026-10-13",
        "scope": "REFERENCE_IDENTITY_AND_HOMONYM_REVIEW_NOT_PRIMARY_RESISTANCE_VALIDATION",
        "record": {**plan["record"], "whole_record_review": "OPEN", "resistance_assertions_added": []},
        "inputs": {"plan": reference.pin(root, plan_path), "canary": reference.pin(root, canary_path),
                   **{k: plan[k] for k in ("census", "discovery", "taxonomy_dossier",
                                         "prior_progress", "prior_checkpoint")}},
        "compound_name_grounding": {"ISP-1": {"identifier": record["identifier"], "name_snapshot": alias,
                                              "synonym": plan["exact_alias"]},
                                    "tested_preparation_independently_reidentified": False},
        "reference_proteins": proteins, "ypk1_name_resolution": resolution,
        "sli1_archive_crosswalk": {"source": "UNIPROT_ANNOTATION", "links": archive,
                                  "experimental_subject_assignment": False,
                                  "new_archive_endpoint_requests": 0},
        "uniprot_requests": requests,
        "taxonomy_request": {**tax_request, "reused_byte_identically": True, "new_request": False},
        "primary_access": [
            {**plan["primary"], "outcome": "HTTP_403_NON_PDF_BODY", "status": 403,
             "receipt": reference.pin(root, receipt_path), "response": reference.pin(root, body_path),
             "primary_results_verified": False, "retry_or_alternate_transport": False},
            {"doi": FOCAL["10825204"], "pmid": "10825204",
             "url": "https://journals.asm.org/doi/full/10.1128/mcb.20.12.4411-4419.2000",
             "outcome": "TOOL_REPORTED_URL_INACCESSIBLE", "local_primary_bytes_saved": False,
             "primary_results_verified": False, "retry_or_alternate_transport": False},
            {"doi": "10.7554/elife.03779", "url": "https://elifesciences.org/articles/03779",
             "outcome": "CLIENT_CHALLENGE_NOT_ARTICLE_TEXT", "local_primary_bytes_saved": False,
             "primary_results_verified": False, "retry_or_alternate_transport": False},
        ],
        "summary": {"corpus_records_in_scope": 2939, "selected_records": 1, "reference_candidates": 3,
                    "concordant_reference_identities": 2, "homonym_candidates_not_supported_for_lead": 1,
                    "complete_uniprot_queries": 2, "new_taxonomy_requests": 0,
                    "biological_records_changed": 0, "new_phi_decisions": 0,
                    "experimental_accessions_assigned": 0, "whole_records_completed": 0},
        "limits": [
            "Reference identity and citation concordance do not verify primary resistance results.",
            "YPK1 is also an MCK1 synonym; no first-hit or gene-name-only accession assignment is accepted.",
            "Rejecting a homonym for this lead is not evidence that its organism is susceptible.",
            "Archive identifiers are reference annotations, not exact experimental allele or genome joins.",
            "Reference-strain TaxID 559292 and species lineage 4932 do not identify tested derivatives.",
            "Biochemical inhibition, growth inhibition, MIC and clinical resistance are not interchangeable.",
            "No native figure, supplement or primary result was verified from the unavailable sources.",
            "The indexed abstracts are discovery only; no mechanistic claim is curated from them.",
            "Manual web-tool access observations are not automatically verified by metadata replay.",
            "No sequences, variant specifications, constructs, protocols or numeric AST are exported.",
            "No NCBI requests/contact, source adoption, GitHub mutation or reuse-terms work; "
            "#1040 stays deferred.",
        ],
        "attribution": {"source": "UniProt Consortium", "license": "CC BY 4.0",
                        "license_url": "https://www.uniprot.org/help/license"},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    root = Path.cwd()
    result = build(root, root / args.cache)
    with args.output.open("x") as stream:
        stream.write(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n")
    print(json.dumps(result["summary"]))


if __name__ == "__main__":
    main()
