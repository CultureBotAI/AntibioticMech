"""Separate IreK citation labels, reference taxonomy and unavailable primary evidence."""

import argparse
import csv
import json
from pathlib import Path

import audit_card_study_context as study
import audit_topoisomerase_references as reference
from resistance_checkpoint_records import checkpoint_path

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-13-irek-context")
OUTPUT = Path("research/2026-10-13-irek-context.json")
FIELDS = ("accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
          "lit_pubmed_id,sequence_version,version")
QUERIES = {
    "reference": "(gene_exact:ireK OR gene_exact:prkC) AND organism_name:OG1RF",
    "taxon-reference": "(gene_exact:ireK OR gene_exact:prkC) AND organism_id:474186",
}
SOURCES = {
    "paper2021": {"doi": "10.1021/acs.jproteome.1c00635", "pmid": "34672600",
                  "url": "https://europepmc.org/articles/PMC10037947?pdf=render"},
    "paper2023": {"doi": "10.1016/j.jmb.2023.168216", "pmid": "37517789",
                  "url": "https://www.sciencedirect.com/science/article/pii/S0022283623003157"},
}
SCOPE = "DISTINCT_REFERENCE_STRAIN_TAXONOMY_WITH_UNRESOLVED_PRIMARY_AND_PROTEIN_IDENTITY"


def project_taxon(taxon):
    if (type(taxon.get("taxonId")) is not int or taxon["taxonId"] != 474186
            or taxon.get("active") is not True or taxon.get("rank") != "strain"):
        raise ValueError("OG1RF reference taxon identity or rank changed")
    species = study.reference_lineage(taxon)
    if (species is None or species["taxon_id"] != "NCBITaxon:1351"
            or species["scientific_name"] != "Enterococcus faecalis"
            or taxon["parent"]["taxonId"] != 1351
            or taxon["scientificName"] != "Enterococcus faecalis (strain ATCC 47077 / OG1RF)"):
        raise ValueError("reference species or strain name changed")
    aliases = {value for row in taxon.get("strains", []) for value in row.get("synonyms", [])}
    if "OG1RF" not in aliases or "OG1" in aliases:
        raise ValueError("reference strain alias scope changed")
    return {"taxon_id": "NCBITaxon:474186", "rank": "strain",
            "scientific_name": taxon["scientificName"], "species_lineage": species,
            "strain_annotations": taxon["strains"], "other_names": taxon.get("otherNames", []),
            "active": True, "source_og1_equated_to_og1rf": False,
            "experimental_subject_assignment": False, "genome_assignment": False}


def read_empty_query(root, directory, key):
    body, request = reference.read_response(root, directory, key, "/uniprotkb/search", {
        "query": [QUERIES[key]], "format": ["json"], "size": ["50"], "fields": [FIELDS]})
    receipt = json.loads((directory / f"{key}-receipt.json").read_bytes())
    if (request["release"] != "2026_03" or body["results"] != []
            or receipt["retry_performed"] is not False
            or receipt["bytes"] != (directory / f"{key}-response.bin").stat().st_size):
        raise ValueError("frozen empty-query scope changed")
    suggestions = body.get("suggestions", [])
    if not isinstance(suggestions, list) or any(not isinstance(s, dict) for s in suggestions):
        raise ValueError("invalid query suggestions")
    return {**request, "query": QUERIES[key], "result_count": 0,
            "complete_for_exact_query": True, "suggested_queries_excluded": len(suggestions),
            "suggestions_used_as_results": False, "suggested_query_text_exported": False,
            "protein_absence_inferred": False, "all_strains_and_aliases_searched": False}


def primary_hold(root, directory, key):
    source = SOURCES[key]
    attempt_path, receipt_path = [directory / f"{key}-{suffix}.json" for suffix in ("attempt", "receipt")]
    attempt, receipt = [json.loads(p.read_bytes()) for p in (attempt_path, receipt_path)]
    if (attempt.get("url") != source["url"] or not attempt.get("started_at")
            or receipt.get("url") != source["url"] or receipt.get("retry_performed") is not False):
        raise ValueError("primary request binding changed")
    response = directory / f"{key}-response.bin"
    if key == "paper2021":
        if (receipt.get("error_type") != "ConnectionError" or "status" in receipt or response.exists()):
            raise ValueError("transport failure is not an HTTP refusal or received primary text")
        observation = {"status": "TRANSPORT_ERROR_NO_HTTP_RESPONSE", "http_status": None,
                       "error_type": receipt["error_type"], "response": None}
    else:
        if (receipt.get("status") != 403 or reference.digest(response) != receipt.get("sha256")
                or response.stat().st_size != receipt.get("bytes")):
            raise ValueError("publisher access-hold response changed")
        observation = {"status": "HTTP_ACCESS_HOLD", "http_status": 403,
                       "response": reference.pin(root, response)}
    return {**source, **observation, "attempt": reference.pin(root, attempt_path),
            "receipt": reference.pin(root, receipt_path), "attempted_at": attempt["started_at"],
            "full_text_reviewed": False, "native_figures_or_supplements_reviewed": False,
            "alternate_route_attempted": False, "global_unavailability_inferred": False,
            "search_snippets_are_primary_results": False}


def build(root, directory):
    plan_path = directory / "cohort.json"
    plan = json.loads(plan_path.read_bytes())
    if (plan["primary_requests"] != {k: v["url"] for k, v in SOURCES.items()}
            or plan["previous_goal_turn"] != "PROGRESS"
            or plan["complete_collection_aware_record_loaded"] is not True):
        raise ValueError("primary selection or record-inspection scope changed")
    for key in ("protected", "prior_verification"):
        reference.check_pin(root, plan[key])
    prior = json.loads(reference.check_pin(root, plan["prior"]).read_bytes())
    if study.build(root, root / study.CACHE, record_resolver=checkpoint_path) != prior:
        raise ValueError("reused citation context no longer reproduces")
    with reference.check_pin(root, plan["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if len(census) != 2939:
        raise ValueError("corpus census coverage changed")
    item = plan["record"]
    record = load_record(reference.check_pin(root, item))
    if (item["identifier"] != record["identifier"] or record["identifier"] != "CHEBI:29007"
            or record["chemical_structure"]["standard_inchi_key"] != "VAAUVRVFOQPIGI-SPQHTLEESA-N"
            or len(record["resistance_mechanisms"]) != plan["existing_resistance_assertions"]
            or len(record["activity_spectrum"]) != plan["existing_activity_observations"]):
        raise ValueError("compound identity or existing evidence changed")
    claim, = [c for c in record["resistance_mechanisms"] if c.get("aro_id") == "ARO:3007678"]
    if claim != plan["source_assertion"]:
        raise ValueError("source-owned IreK assertion changed")
    protein = prior["proteins"]["UniProtKB:Q820A8"]
    contexts = prior["terms"]["ARO:3007678"]["reference_candidates"][0]["matched_study_contexts"]
    if (protein["reference_taxon_id"] != "NCBITaxon:226185"
            or not any("OG1RF" in a["value"] for c in protein["reference_contexts"]
                       for a in c["strain_annotations"])):
        raise ValueError("reference strain or exploratory label basis changed")
    query_plan_path = directory / "reference-plan.json"
    query_plan = json.loads(query_plan_path.read_bytes())
    if (query_plan["query"] != QUERIES["reference"] or query_plan["fields"] != FIELDS
            or query_plan["size"] != "50" or query_plan["prior"] != plan["prior"]
            or query_plan["cohort"] != reference.pin(root, plan_path)
            or query_plan["selection"] != "SEPARATE_OG1RF_REFERENCE_LOOKUP_NOT_OG1_EQUIVALENCE"):
        raise ValueError("reference query plan changed")
    queries = {key: read_empty_query(root, directory, key) for key in QUERIES}
    tax_body, tax_request = reference.read_response(root, directory, "taxonomy", "/taxonomy/search", {
        "query": ["OG1RF"], "format": ["json"], "size": ["50"]})
    taxon, = tax_body["results"]
    if tax_request["release"] != "2026_03":
        raise ValueError("reference taxonomy release changed")
    projected_taxon = project_taxon(taxon)
    tax_plan_path = directory / "taxonomy-plan.json"
    tax_plan = json.loads(tax_plan_path.read_bytes())
    follow_path = directory / "taxon-reference-plan.json"
    follow = json.loads(follow_path.read_bytes())
    if (tax_plan["query"] != "OG1RF" or tax_plan["size"] != "50" or tax_plan["format"] != "json"
            or tax_plan["canary_manually_reviewed"] is not True
            or tax_plan["source_og1_is_equated_to_og1rf"] is not False
            or tax_plan["reference_response"] != queries["reference"]["cache"]
            or tax_plan["reference_receipt"] != queries["reference"]["receipt"]
            or follow["query"] != QUERIES["taxon-reference"] or follow["fields"] != FIELDS
            or follow["size"] != "50" or follow["taxonomy_canary_manually_reviewed"] is not True
            or follow["taxonomy_response"] != tax_request["cache"]
            or follow["taxonomy_receipt"] != tax_request["receipt"]
            or follow["prior_successful_zero_hit_query"] != queries["reference"]["receipt"]
            or follow["retry_of_failed_request"] is not False):
        raise ValueError("taxonomy canary or taxon-query binding changed")
    return {"date": "2026-10-13", "scope": SCOPE,
            "inputs": {k: plan[k] for k in ("prior", "prior_verification", "census", "protected")},
            "plans": {k: reference.pin(root, p) for k, p in (
                ("cohort", plan_path), ("reference", query_plan_path),
                ("taxonomy", tax_plan_path), ("taxon_reference", follow_path))},
            "record": {**item, "source_assertions": len(record["resistance_mechanisms"]),
                       "source_owned_irek_assertion": claim, "source_route_newly_confirmed": False,
                       "whole_record_review": "OPEN"},
            "reused_reference_protein": protein, "focal_citation_contexts": contexts,
            "separate_og1rf_reference_taxonomy": projected_taxon, "taxonomy_request": tax_request,
            "queries": queries, "primary_holds": {k: primary_hold(root, directory, k) for k in SOURCES},
            "curation_decision": "HOLD_UNVERIFIED_PRIMARY_SUBJECT_PROTEIN_AND_MECHANISM",
            "summary": {"corpus_records_checked": len(census), "selected_records": 1,
                "reused_protein_references": 1, "new_protein_references": 0,
                "new_reference_strain_taxa": 1, "exact_gene_queries": len(queries),
                "exact_gene_query_results": 0,
                "suggested_queries_excluded": sum(q["suggested_queries_excluded"] for q in queries.values()),
                "primary_request_attempts": 2, "http_access_holds": 1, "transport_failures": 1,
                "new_primary_results_reviewed": 0, "biological_records_changed": 0,
                "experimental_allele_or_genome_assignments": 0, "whole_record_reviews_completed": 0,
                "full_corpus_goal_status": "OPEN"},
            "limitations": [
                "V583, the citation label OG1, and the separate OG1RF reference remain distinct.",
                "OG1RF taxonomy does not establish which subject either focal paper tested.",
                "A zero-result exact-alias query is not absence of IreK, homologs or sequence data.",
                "Suggested alternative gene or taxon queries are not hits for the requested query.",
                "No locus-specific, homology, sequence or genome analysis was performed.",
                "Neither focal primary result, figure nor supplement was newly reviewed.",
                "The CARD route is retained as source-owned evidence, not newly verified permeability.",
                "Transport failure does not establish publisher refusal or global source unavailability.",
                "Replay validates bytes and identifier boundaries, not experimental truth.",
                "No sequences, exact variants, constructs, protocols or numeric AST are exported."],
            "attribution": prior["attribution"],
            "constraints": {"ncbi_requests": 0, "ncbi_contact": 0, "issue_1040": "DEFERRED",
                            "github_mutations": 0, "source_adoptions": 0,
                            "reuse_terms_review_resumed": False, "failed_source_retries": 0}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=CACHE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path.cwd()
    result = build(root, root / args.cache)
    if args.check:
        if json.loads(args.output.read_bytes()) != result:
            raise SystemExit("IreK context does not reproduce")
    else:
        with args.output.open("x") as stream:
            stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
