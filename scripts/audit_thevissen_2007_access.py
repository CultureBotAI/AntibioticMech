"""Replay a cited paper's publisher access hold without promoting metadata to evidence."""

import argparse
import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote

import audit_caspofungin_context as native_context
import audit_topoisomerase_references as reference
from lxml import html

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-thevissen-2007")
OUTPUT = Path("research/2026-10-14-thevissen-2007-access.json")
SCOPE = "BIBLIOGRAPHY_AND_ACCESS_HOLD_NOT_PRIMARY_RESULTS_REVIEW"
DOI = "10.1074/jbc.M608505200"
METADATA = "https://api.crossref.org/works/10.1074%2Fjbc.M608505200"
PUBLISHER = "https://linkinghub.elsevier.com/retrieve/pii/S002192582078110X"
PRIMARY = "https://jbc.org/retrieve/pii/S002192582078110X"
NATIVE_SHA = {
    "crossref": "da4531fc10ada0768a90c549683620cd3113d92e463bcf9ac9e26732d8033514",
    "publisher": "020b74c70f795b2f9be20311bdf7eda10f62544266945e864e37b4296730c53a",
    "primary": "9e72faeeb27fc87d431db02383bb79e99e16c112525a2b31215589eb066e97bb",
}


def project_metadata(payload):
    message = payload.get("message", {})
    if (payload.get("status") != "ok" or payload.get("message-type") != "work"
            or message.get("DOI", "").lower() != DOI.lower()
            or message.get("resource", {}).get("primary", {}).get("URL") != PUBLISHER
            or len(message.get("title", [])) != 1):
        raise ValueError("Crossref identity or canonical publisher link changed")
    return {
        "reference": "PMID:17553796", "doi": DOI, "title": message["title"][0],
        "publisher": message["publisher"], "canonical_publisher_url": PUBLISHER,
        "licenses_as_deposited": message.get("license", []),
        "license_scope": "CROSSREF_DEPOSIT_METADATA_NOT_INDEPENDENT_ARTICLE_TERMS_REVIEW",
        "primary_results_reviewed": False, "source_adoption_authorized": False,
        "access_availability_inferred_from_license": False,
    }


def routing_destination(body):
    tree = html.fromstring(body)
    values = tree.xpath("//input[@id='redirectURL']/@value")
    if (tree.xpath("//title/text()") != ["Redirecting"] or len(values) != 1
            or unquote(values[0]) != PRIMARY
            or tree.xpath("//meta[@name='tdm-reservation']/@content") != ["1"]):
        raise ValueError("routine publisher routing changed")
    return PRIMARY


def project_hold(receipt):
    headers = {key.lower(): value for key, value in receipt.get("headers", {}).items()}
    if (receipt.get("url") != PRIMARY or receipt.get("status") != 403
            or receipt.get("retry_performed") is not False
            or headers.get("cf-mitigated") != "challenge"):
        raise ValueError("publisher challenge or no-retry boundary changed")
    return {
        "status": "PUBLISHER_403_CHALLENGE_HELD_NO_RETRY", "url": PRIMARY,
        "retrieved_at": receipt["retrieved_at"], "primary_results_reviewed": False,
        "alternate_route_attempted": False, "global_inaccessibility_inferred": False,
        "requires_new_direction_or_user_supplied_primary": True,
    }


def planned_native(root, directory, key, url, status):
    request = native_context.native(root, directory, key, url, statuses=(status,))
    plan_path = directory / f"{key}-plan.json"
    plan = json.loads(plan_path.read_bytes())
    attempt = json.loads(reference.check_pin(root, request["attempt"]).read_bytes())
    receipt = json.loads(reference.check_pin(root, request["receipt"]).read_bytes())
    if (plan.get("url") != url or plan.get("redirects_followed") is not False
            or request["body"]["sha256"] != NATIVE_SHA[key]
            or type(plan.get("max_bytes")) is not int or receipt["bytes"] > plan["max_bytes"]
            or datetime.fromisoformat(attempt["started_at"])
            > datetime.fromisoformat(receipt["retrieved_at"])):
        raise ValueError("planned request or inspected payload changed")
    return {**request, "plan": reference.pin(root, plan_path)}


def build(root, directory=CACHE, *, record_resolver=None):
    directory = root / directory
    cohort_path = directory / "cohort.json"
    cohort = json.loads(cohort_path.read_bytes())
    inputs = {key: cohort[key] for key in (
        "prior_context", "prior_checkpoint", "reused_search", "source_queue", "census", "protected")}
    paths = {key: reference.check_pin(root, pin) for key, pin in inputs.items()}
    prior = json.loads(paths["prior_context"].read_bytes())
    cited = prior["primary"]["cited_background_paper"]
    if cited["reference"] != "PMID:17553796" or cited["doi"] != DOI:
        raise ValueError("prior citation lead changed")
    search = json.loads(paths["reused_search"].read_bytes())
    if search["status"] != 200 or hashlib.sha256(search["body"].encode()).hexdigest() != search["sha256"]:
        raise ValueError("reused discovery response changed")
    matches = [r for r in json.loads(search["body"])["resultList"]["result"]
               if r.get("id") == "17553796" and r.get("source") == "MED"]
    if (len(matches) != 1 or matches[0] != cohort["reused_metadata"]
            or matches[0].get("doi", "").lower() != DOI.lower()):
        raise ValueError("reused bibliographic identity changed")
    with paths["census"].open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (len(census) != 2939 or len({row["path"] for row in census}) != len(census)
            or {row["path"] for row in census} != {
                str(path.relative_to(root)) for path in (root / "data/antibiotics").rglob("*.yaml")}):
        raise ValueError("census membership changed")
    for row in census:
        path = (record_resolver(root, row) if record_resolver else reference.check_pin(
            root, {"path": row["path"], "sha256": row["record_sha256"]}))
        if reference.digest(path) != row["record_sha256"]:
            raise ValueError("census record checksum changed")
    for item in cohort["records"]:
        path = record_resolver(root, item) if record_resolver else reference.check_pin(root, item)
        doc = load_record(path)
        if (doc["identifier"] != item["identifier"]
                or doc["chemical_structure"]["standard_inchi_key"] != item["standard_inchi_key"]):
            raise ValueError("target compound identity changed")
    sources = {key: planned_native(root, directory, key, url, status)
               for key, url, status in (("crossref", METADATA, 200), ("publisher", PUBLISHER, 200),
                                         ("primary", PRIMARY, 403))}
    study = project_metadata(json.loads(reference.check_pin(root, sources["crossref"]["body"]).read_bytes()))
    routing_destination(reference.check_pin(root, sources["publisher"]["body"]).read_bytes())
    hold = project_hold(json.loads(reference.check_pin(root, sources["primary"]["receipt"]).read_bytes()))
    discoveries = {}
    for key, source in (("publisher", "crossref"), ("primary", "publisher")):
        path = directory / f"{key}-discovery.json"
        discovery = json.loads(path.read_bytes())
        if (discovery["source_body"] != sources[source]["body"]
                or discovery["source_receipt"] != sources[source]["receipt"]
                or discovery["selected_url"] != sources[key]["url"]
                or discovery["stop_on_access_denial"] is not True
                or discovery["no_alternate_route_on_hold"] is not True):
            raise ValueError("publisher link provenance or stop boundary changed")
        discoveries[key] = reference.pin(root, path)
    if {p.name.removesuffix("-attempt.json") for p in directory.rglob("*-attempt.json")} != set(sources):
        raise ValueError("unexpected extra request in this checkpoint cache")
    return {
        "date": "2026-10-14", "scope": SCOPE,
        "inputs": {**inputs, "cohort": reference.pin(root, cohort_path)},
        "records": cohort["records"], "citation_origin": cited, "study": study,
        "reused_literature_metadata": {
            "retrieved_at": search["retrieved_at"], "response_sha256": search["sha256"],
            "flags": {key: matches[0][key]
                      for key in ("isOpenAccess", "inEPMC", "inPMC", "hasPDF", "hasSuppl")},
            "scope": "DATED_DISCOVERY_FLAGS_NOT_GLOBAL_ACCESS_OR_REUSE_DECISION",
        },
        "sources": sources, "link_discovery": discoveries, "access_hold": hold,
        "routing_page": {"status": 200, "article_text": False, "destination": PRIMARY,
                         "tdm_reservation_as_returned": "1", "reuse_authority_inferred": False},
        "summary": {"corpus_record_hashes_checked": len(census),
                    "target_records_loaded": len(cohort["records"]),
                    "new_network_requests": 3, "new_access_holds": 1, "primary_results_reviewed": 0,
                    "new_reference_proteins": 0, "biological_record_changes": 0,
                    "experimental_allele_assignments": 0, "whole_record_reviews_completed": 0},
        "limitations": [
            "A DOI, deposited license or HTTP 200 routing page is not primary experimental evidence.",
            "The journal challenge was not solved, retried or bypassed through another route.",
            "Access status is scoped to this dated attempt, not all possible access paths.",
            "The FR171456 source-label conflict and historical deletion identity remain unresolved.",
            "The miconazole paper's tested chemical form and experimental subjects remain unverified.",
            "No phenotype, target, gene-model history, protein, allele or genome was inferred from metadata.",
            "Earlier primary/supplement holds remain unchanged and were not retried.",
        ],
        "constraints": {"ncbi_requests": 0, "issue_1040": "DEFERRED", "source_adoptions": 0,
                        "github_mutations": 0, "held_sources_retried": False,
                        "sequences_variants_protocols_or_numeric_AST_exported": False,
                        "full_corpus_records_in_scope": 2939, "full_corpus_goal_status": "OPEN"},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=CACHE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd(), args.cache)
    if args.check:
        if json.loads(args.output.read_bytes()) != result:
            raise SystemExit("publisher-access dossier does not reproduce")
    else:
        with args.output.open("x") as stream:
            stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
