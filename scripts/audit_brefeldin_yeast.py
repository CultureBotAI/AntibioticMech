"""Replay dated Bfr1 reference identities without assigning experimental alleles."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import audit_caspofungin_context as native_context
import audit_topoisomerase_references as reference

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-brefeldin-yeast")
OUTPUT = Path("research/2026-10-14-brefeldin-yeast-context.json")
REUSE = Path("reports/resistance-grounding-2026-10-13-tavaborole")
REUSE_SHA = "9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810"
FIXED_URLS = {
    "bfr1-cerevisiae-primary": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC55738/fullTextXML",
    "bfr1-1994-publisher": "https://academic.oup.com/genetics/article-abstract/137/2/423/6012527",
    "tax-284812": "https://rest.uniprot.org/taxonomy/284812",
}
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_sgd,lit_pubmed_id,sequence_version,version"
)
IDENTITIES = {
    "cerevisiae-bfr1": {
        "query": "gene_exact:BFR1 AND organism_id:559292 AND reviewed:true",
        "gene": "BFR1", "accession": "P38934", "taxon": 559292, "species": 4932,
        "species_name": "Saccharomyces cerevisiae", "ordered_loci": ["YOR198C"], "orf_names": [],
        "entry_version": 182, "sequence_version": 1,
        "selected_pmids": ["8070655", "11410665"],
    },
    "pombe-bfr1": {
        "query": 'gene_exact:bfr1 AND organism_name:"Schizosaccharomyces pombe" AND reviewed:true',
        "gene": "bfr1", "accession": "P41820", "taxon": 284812, "species": 4896,
        "species_name": "Schizosaccharomyces pombe", "ordered_loci": [],
        "orf_names": ["SPCC18B5.01c", "SPCPJ732.04c"], "entry_version": 178, "sequence_version": 1,
        "selected_pmids": ["7883711", "7646493"],
    },
}


def citation_contexts(entry, selected):
    result = []
    seen = set()
    for row in entry.get("references", []):
        number = row["referenceNumber"]
        if type(number) is not int or number <= 0 or number in seen:
            raise ValueError("invalid or duplicate reference number")
        seen.add(number)
        ids = {r["database"] + ":" + r["id"] for r in row["citation"].get("citationCrossReferences", [])}
        matched = sorted(set("PubMed:" + p for p in selected) & ids)
        if not matched:
            continue
        result.append({
            "reference_number": number, "matched_citations": matched,
            "citation_identifiers": sorted(i for i in ids if i.startswith(("PubMed:", "DOI:"))),
            "source_title_sha256": hashlib.sha256(row["citation"]["title"].encode()).hexdigest(),
            "study_strain_annotations": [r["value"] for r in row.get("referenceComments", [])
                                         if r["type"] == "STRAIN"],
            "raw_role_annotations_exported": False, "experimental_subject_assignment": False,
            "primary_results_reviewed": False,
        })
    return result


def project(entry, key, taxonomy):
    expected = IDENTITIES[key]
    if {"sequence", "features", "comments"}.intersection(entry):
        raise ValueError("unplanned biological payload")
    item = reference.project_reference(entry, expected["gene"], expected["species"], taxonomy)
    species = [r for r in taxonomy["lineage"] if r["rank"] == "species"]
    orfs = sorted({r["value"] for g in entry["genes"] for r in g.get("orfNames", [])})
    if (
        entry["primaryAccession"] != expected["accession"]
        or entry["organism"]["taxonId"] != expected["taxon"]
        or taxonomy["rank"] != "strain"
        or taxonomy["scientificName"] != entry["organism"]["scientificName"]
        or len(species) != 1 or species[0]["scientificName"] != expected["species_name"]
        or item["ordered_locus_names"] != expected["ordered_loci"] or orfs != expected["orf_names"]
        or item["entry_version"] != expected["entry_version"]
        or item["sequence_version"] != expected["sequence_version"]
    ):
        raise ValueError("reference identity, locus field, version or species changed")
    contexts = citation_contexts(entry, expected["selected_pmids"])
    matched = {i.removeprefix("PubMed:") for r in contexts for i in r["matched_citations"]}
    missing = sorted(set(expected["selected_pmids"]) - matched)
    if missing != (["11410665"] if key == "cerevisiae-bfr1" else []):
        raise ValueError("selected citation projection changed")
    item.pop("bibliography")
    return {
        **item, "source_symbol": expected["gene"], "reference_orf_names": orfs,
        "reference_species_name": expected["species_name"], "selected_citation_contexts": contexts,
        "selected_pmids_not_in_returned_bibliography": missing,
        "missing_citation_proves_no_relationship": False,
        "resistant_phenotype_inferred_from_protein_name": False,
        "experimental_genome_assignment": None, "scope": "DATABASE_REFERENCE_NOT_TESTED_ALLELE",
    }


def planned_source(root, directory, key, plan_name, statuses=(200,)):
    plan_path = directory / plan_name
    plan = json.loads(plan_path.read_bytes())
    if key in FIXED_URLS and plan["requests"][key]["url"] != FIXED_URLS[key]:
        raise ValueError("planned source identity changed")
    attempt = json.loads((directory / (key + "-attempt.json")).read_bytes())
    if attempt["plan_sha256"] != reference.digest(plan_path):
        raise ValueError("request plan changed after attempt")
    source = native_context.native(root, directory, key, plan["requests"][key]["url"], statuses)
    receipt = json.loads(reference.check_pin(root, source["receipt"]).read_bytes())
    if receipt.get("redirects_followed") is not False:
        raise ValueError("unplanned redirect")
    return {**source, "plan": reference.pin(root, plan_path)}


def validate_discovery(root, discovery):
    caches = {}
    for key, candidate in discovery["candidates"].items():
        metadata = candidate["metadata"]
        if key != metadata["source"] + ":" + metadata["id"] or not candidate["sources"]:
            raise ValueError("discovery candidate identity or provenance missing")
        for pin in candidate["sources"]:
            path = reference.check_pin(root, pin)
            if pin["path"] not in caches:
                receipt = json.loads(path.read_bytes())
                parsed = urlsplit(receipt["url"])
                if (receipt["status"] != 200 or parsed.scheme != "https" or parsed.netloc != "www.ebi.ac.uk"
                        or parsed.path != "/europepmc/webservices/rest/search"
                        or hashlib.sha256(receipt["body"].encode()).hexdigest() != receipt["sha256"]):
                    raise ValueError("discovery source status, identity or body changed")
                caches[pin["path"]] = json.loads(receipt["body"])["resultList"]["result"]
            matches = [r for r in caches[pin["path"]] if r["source"] + ":" + r["id"] == key]
            if len(matches) != 1 or any(matches[0].get(k) != metadata.get(k)
                                       for k in ("title", "doi", "pmcid")):
                raise ValueError("discovery candidate differs from cited cache")
    return len(caches)


def build(root, directory=CACHE):
    directory = root / directory
    cohort = json.loads((directory / "cohort.json").read_bytes())
    for key in ("baseline", "protected", "discovery", "census", "previous_checkpoint", "source_queue"):
        reference.check_pin(root, cohort[key])
    record = load_record(reference.check_pin(root, cohort["baseline"]))
    if (record["identifier"], record["chemical_structure"]["standard_inchi_key"]) != (
        "CHEBI:48080", "KQNZDYYTLMIZCT-KQPMLPITSA-N",
    ) or cohort["record"]["sha256"] != cohort["baseline"]["sha256"]:
        raise ValueError("dated compound identity changed")
    with reference.check_pin(root, cohort["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    rows = [r for r in census if r["identifier"] == record["identifier"]]
    if (len(census) != 2939 or len({r["identifier"] for r in census}) != 2939 or len(rows) != 1
            or rows[0]["record_sha256"] != cohort["record"]["sha256"]
            or rows[0]["path"] != cohort["record"]["path"]
            or rows[0]["standard_inchi_key"] != cohort["record"]["standard_inchi_key"]):
        raise ValueError("dated corpus membership changed")
    sources = {}
    for key, plan_name, statuses in (
        ("bfr1-cerevisiae-primary", "request-plan.json", (500,)),
        ("bfr1-1994-publisher", "followup-plan.json", (403,)),
        ("cerevisiae-bfr1", "reference-plan.json", (200,)),
        ("pombe-bfr1", "reference-plan.json", (200,)),
        ("tax-284812", "followup-plan.json", (200,)),
    ):
        sources[key] = planned_source(root, directory, key, plan_name, statuses)
    taxonomy, tax_source = reference.read_response(root, root / REUSE, "tax-559292", "/taxonomy/559292")
    if reference.digest(root / REUSE / "tax-559292-response.bin") != REUSE_SHA:
        raise ValueError("reused taxonomy changed")
    pombe_taxonomy, pombe_source = reference.read_response(root, directory, "tax-284812", "/taxonomy/284812")
    if tax_source["release"] != pombe_source["release"] or tax_source["release"] != "2026_03":
        raise ValueError("taxonomy releases changed")
    proteins = {}
    for key, expected in IDENTITIES.items():
        params = {"query": [expected["query"]], "format": ["json"], "size": ["500"], "fields": [FIELDS]}
        payload, request = reference.read_response(root, directory, key, "/uniprotkb/search", params)
        if len(payload["results"]) != 1 or request["release"] != tax_source["release"]:
            raise ValueError("reference query cardinality or release changed")
        proteins[key] = project(payload["results"][0], key, taxonomy if key == "cerevisiae-bfr1"
                                else pombe_taxonomy)
    discovery = json.loads(reference.check_pin(root, cohort["discovery"]).read_bytes())
    if discovery["ignored_files_included"] is not True or len(discovery["candidates"]) != 35:
        raise ValueError("discovery cohort changed")
    validate_discovery(root, discovery)
    web_plan = directory / "independent-discovery-plan.json"
    web_result = directory / "independent-discovery-result.json"
    plan = json.loads(web_plan.read_bytes())
    if plan["selected_pmid"] != "8070655" or plan["selected_doi"] != "10.1093/genetics/137.2.423":
        raise ValueError("independent citation discovery identity changed")
    return {
        "date": "2026-10-14", "scope": "YEAST_BFR1_REFERENCE_DISAMBIGUATION_NOT_PRIMARY_RESISTANCE_SIGNOFF",
        "cohort": reference.pin(root, directory / "cohort.json"), "record": cohort["record"],
        "inputs": {k: cohort[k] for k in ("baseline", "census", "source_queue", "previous_checkpoint")},
        "sources": sources, "taxonomy_reuse": tax_source, "proteins": proteins,
        "discovery": {"local": cohort["discovery"],
                      "local_metadata_files": discovery["matching_metadata_files"],
                      "local_candidates": len(discovery["candidates"]),
                      "web_plan": reference.pin(root, web_plan),
                      "web_result": reference.pin(root, web_result),
                      "incidental_held_paper_search_result_received": True,
                      "incidental_result_used_as_native_primary_review": False},
        "primary_status": {
            "PMID:11410665": "TECHNICAL_HTTP_500_NO_FULL_TEXT_REVIEW",
            "PMID:8070655": "PUBLISHER_HTTP_403_SEARCH_ABSTRACT_ONLY_NOT_PRIMARY_RESULTS_REVIEW",
            "PMID:7883711": "NOT_REQUESTED_AFTER_EBI_CANARY_FAILURE",
            "PMID:7646493": "NOT_REQUESTED_AFTER_EBI_CANARY_FAILURE",
        },
        "identity_decisions": {
            "shared_symbol_establishes_same_gene_or_orthology": False,
            "reference_organism_is_experimental_subject": False,
            "ordered_locus_and_orf_name_fields_interchangeable": False,
            "multiple_pombe_orf_names_reduced_to_one": False,
            "existing_phibase_claim_changed": False, "whole_record_primary_review": "OPEN",
        },
        "limitations": [
            "Database names and citations do not verify the compound-specific experimental effect.",
            "S288c and 972 are reference backgrounds; citation strain labels are not assigned genomes.",
            "The 1994 budding-yeast citation annotation names FL100, not the S288c reference strain.",
            "The two fission-yeast ORF names remain separate labels; neither is chosen as a tested allele.",
            "The 2001 citation is absent from this returned bibliography, not disproven or globally absent.",
            "Primary access holds are local observations, not scientific negatives or global unavailability.",
            "Search-index text is not native figure, table, supplement or primary-result review.",
            "Earlier organism-specific claims and later manual investigations remain separate.",
        ],
        "limits": {"new_scientific_http_attempts": 5, "web_search_queries": 1, "ncbi_requests": 0,
                   "ncbi_contact": 0, "issue_1040": "DEFERRED", "reuse_terms_review_resumed": False,
                   "biological_changes": 0, "new_experimental_allele_or_genome_assignments": 0,
                   "whole_record_primary_signoffs": 0, "source_adoptions": 0, "github_mutations": 0,
                   "sequences_variants_constructs_protocols_or_numeric_AST_exported": False},
        "attribution": {"source": "UniProt Consortium", "license": "CC BY 4.0",
                        "license_url": "https://www.uniprot.org/help/license", "release": "2026_03"},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    body = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != body:
            raise SystemExit("dated Bfr1 reference checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(body)
    print(json.dumps({"reference_proteins": len(result["proteins"]),
                      "primary_status": result["primary_status"]}))


if __name__ == "__main__":
    main()
