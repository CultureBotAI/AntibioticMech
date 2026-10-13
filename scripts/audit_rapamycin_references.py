"""Replay reference identities while retaining the primary-paper access hold."""

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import urlsplit

import audit_topoisomerase_references as reference
import audit_yeast_regulator_context as yeast

from antibioticmech.activity_collections import load_record

DEFAULT_CACHE = Path("reports/resistance-grounding-2026-10-13-rapamycin")
DEFAULT_OUTPUT = Path("research/2026-10-13-rapamycin-references.json")
DOI = "10.1007/s11357-017-9988-4"
PMID = "28707282"
URL = f"https://link.springer.com/content/pdf/{DOI}.pdf"
QUERY = "gene_exact:TOR1 AND organism_id:559292 AND reviewed:true"
TARGETS = {"CHEBI:9168": "QFJCIRLUMZQUOT-HPLJOQBZSA-N",
           "CHEBI:68478": "HKVAMNSJSFKALM-GKUWKFKPSA-N"}


def project_protein(entry, gene, taxonomy):
    protein = reference.project_reference(entry, gene, 4932, taxonomy)
    block, = entry["genes"]
    sgd, = [row for row in entry["uniProtKBCrossReferences"] if row["database"] == "SGD"]
    if (entry["organism"]["taxonId"] != 559292 or taxonomy["rank"] != "strain"
            or block["geneName"]["value"] != gene or "features" in entry
            or sgd.get("properties") != [{"key": "GeneName", "value": gene}]):
        raise ValueError("reference strain, primary gene, SGD link or field scope changed")
    identifiers = [identifier for row in protein.pop("bibliography") for identifier in row["identifiers"]]
    protein.update({"primary_gene_name": gene, "sgd_id": sgd["id"],
                    "gene_orf_names": [row["value"] for row in block.get("orfNames", [])],
                    "source_bibliography_pmids": sorted(
                        {r["id"] for r in identifiers if r["database"] == "PubMed"}),
                    "focal_paper_in_bibliography": any(r["id"] in {DOI, PMID} for r in identifiers),
                    "bibliography_primary_results_reviewed": False,
                    "reuse_scope": "REFERENCE_IDENTITY_ONLY_NOT_A_TRANSFERRED_PHENOTYPE"})
    return protein


def read_hold(root, directory):
    body, receipt_path = directory / "article-response.bin", directory / "article-receipt.json"
    receipt = json.loads(receipt_path.read_bytes())
    attempt_path = directory / "article-attempt.json"
    attempt = json.loads(attempt_path.read_bytes())
    target = urlsplit({k.lower(): v for k, v in receipt["headers"].items()}["location"])
    if (attempt["url"] != URL or receipt["url"] != URL or receipt["status"] != 303
            or receipt["retry_performed"] is not False or receipt["bytes"] != 0
            or body.read_bytes() or reference.digest(body) != receipt["sha256"]
            or target.scheme != "https" or target.netloc != "idp.springer.com"
            or target.path != "/authorize" or not target.query or target.fragment):
        raise ValueError("publisher authorization hold provenance changed")
    return {"doi": DOI, "pmid": PMID, "source_url": URL,
            "attempt": reference.pin(root, attempt_path), "response": reference.pin(root, body),
            "receipt": reference.pin(root, receipt_path), "retrieved_at": receipt["retrieved_at"],
            "status": "AUTHORIZATION_REDIRECT_NOT_FOLLOWED", "http_status": 303,
            "redirect_endpoint_without_query": "https://idp.springer.com/authorize",
            "full_text_received": False, "primary_results_reviewed": False,
            "figures_or_supplements_reviewed": False, "alternate_route_attempted": False,
            "global_unavailability_inferred": False,
            "discovery_snippets_are_primary_evidence": False}


def build(root, directory):
    plan_path = directory / "cohort.json"
    plan = json.loads(plan_path.read_bytes())
    if (plan["query"] != QUERY or plan["fields"] != yeast.FIELDS or plan["size"] != "50"
            or plan["primary"] != {"doi": DOI, "pmid": PMID, "url": URL}
            or len(plan["records"]) != 2 or {r["identifier"] for r in plan["records"]} != set(TARGETS)):
        raise ValueError("compound, reference or primary-paper cohort changed")
    for key in ("baseline", "prior_verification", "progress"):
        reference.check_pin(root, plan[key])
    prior = json.loads(reference.check_pin(root, plan["prior"]).read_bytes())
    with reference.check_pin(root, plan["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if len(census) != 2939:
        raise ValueError("historical corpus census changed")
    records = []
    for item in plan["records"]:
        record = load_record(reference.check_pin(root, item))
        row, = [r for r in census if r["identifier"] == item["identifier"]]
        if (record["identifier"] != item["identifier"] or row["record_sha256"] != item["sha256"]
                or record["chemical_structure"]["standard_inchi_key"] != TARGETS[item["identifier"]]
                or record.get("resistance_mechanisms") or item["existing_assertions"] != 0
                or item["complete_collection_aware_record_loaded"] is not True):
            raise ValueError("compound identity, record bytes or assertion scope changed")
        records.append({**item, "assertions_added": 0, "whole_record_review": "OPEN",
                        "tested_preparation_independently_reidentified": False})
    taxonomy_request = prior["taxonomy_reused"]["559292"]
    for key in ("cache", "receipt"):
        reference.check_pin(root, taxonomy_request[key])
    taxonomy, checked_taxonomy = reference.read_response(
        root, (root / taxonomy_request["cache"]["path"]).parent, "tax-559292", "/taxonomy/559292")
    if checked_taxonomy != taxonomy_request:
        raise ValueError("reused taxonomy request changed")
    proteins, requests = {}, {}
    sources = {"tor1": directory, "fpr1": root / "reports/resistance-grounding-2026-10-13-calcineurin"}
    for key, source in sources.items():
        query = f"gene_exact:{key.upper()} AND organism_id:559292 AND reviewed:true"
        body, request = reference.read_response(root, source, key, "/uniprotkb/search",
            {"query": [query], "format": ["json"], "size": ["50"], "fields": [yeast.FIELDS]})
        entry, = body["results"]
        receipt = json.loads((source / f"{key}-receipt.json").read_bytes())
        if (receipt["retry_performed"] is not False
                or receipt["bytes"] != (source / f"{key}-response.bin").stat().st_size
                or request["release"] != taxonomy_request["release"]):
            raise ValueError("reference retrieval scope or taxonomy release changed")
        if key == "fpr1" and any(request[k] != prior["uniprot_requests"][key][k] for k in request):
            raise ValueError("reused FPR1 reference request changed")
        proteins[key] = project_protein(entry, key.upper(), taxonomy)
        requests[key] = {**request, "reused": key == "fpr1", "complete_for_query": True,
                         "all_strains_and_aliases_searched": False}
    inspection_path = directory / "inspection.json"
    inspection = json.loads(inspection_path.read_bytes())
    yeast.bind_canary(root, directory, inspection["tor1"], "tor1")
    if (inspection.get("reference_identity_only") is not True
            or inspection.get("publisher_authorization_not_followed") is not True
            or inspection.get("primary_receipt") != reference.pin(root, directory / "article-receipt.json")):
        raise ValueError("manual review or publisher hold binding changed")
    inputs = {k: plan[k] for k in ("baseline", "census", "prior", "prior_verification", "progress")}
    inputs.update({"cohort": reference.pin(root, plan_path),
                   "inspection": reference.pin(root, inspection_path)})
    return {"date": "2026-10-13", "scope": "REFERENCE_METADATA_WITH_PRIMARY_ACCESS_HOLD", "inputs": inputs,
            "records": records, "reference_proteins": proteins, "uniprot_requests": requests,
            "taxonomy_reused": taxonomy_request, "primary": read_hold(root, directory),
            "curation_decision": "HOLD_PRIMARY_EXPERIMENTAL_EVIDENCE_NOT_VERIFIED",
            "limitations": [
                "Reference proteins and S288c taxonomy are not exact experimental alleles or subjects.",
                "The protein name and bibliography do not establish compound-specific resistance.",
                "No phenotype is transferred from the earlier FPR1 combination-context study.",
                "Search snippets are discovery leads, not reviewed primary results or figure evidence.",
                "No MIC, clinical resistance category, genome or assembly assignment is inferred.",
                "No TOR2 query or complete record review is claimed."],
            "constraints": {"ncbi_requests": 0, "ncbi_contact": 0, "github_mutations": 0,
                            "source_adoptions": 0, "issue_1040": "DEFERRED", "sequence_downloads": 0},
            "summary": {"records_in_checkpoint": 2, "new_reference_mappings": 1,
                        "reused_reference_mappings": 1, "new_protein_queries": 1,
                        "new_taxonomy_requests": 0, "publisher_requests": 1,
                        "verified_primary_phenotypes": 0, "new_biological_assertions": 0,
                        "exact_experimental_alleles_assigned": 0,
                        "whole_record_reviews_completed": 0, "full_corpus_goal_status": "OPEN"}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path.cwd()
    result = build(root, root / args.cache)
    if args.check:
        if result != json.loads(args.output.read_bytes()):
            raise SystemExit("rapamycin reference dossier does not reproduce")
    else:
        with args.output.open("x") as stream:
            stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
