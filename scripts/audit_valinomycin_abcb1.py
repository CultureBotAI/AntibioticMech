"""Replay human donor/yeast host evidence without assigning resistant alleles."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urljoin, urlsplit

import audit_caspofungin_context as native_context
import audit_topoisomerase_references as reference
from lxml import html

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-valinomycin-abcb1")
OUTPUT = Path("research/2026-10-14-valinomycin-abcb1-context.json")
ARTICLE = "https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.0030039"
ARTICLE_SHA = "90c6afb0a1bd7333a4467a9dd0e784a2b06d8c4e54a73f1751449a51ad649c05"
FIGURE_SHA = "076aa41bddb66d52fb070414773b6dddbffe65a4b49dc446bd67467fb77d8ee9"
REFERENCE_SHA = "e8835e9c914f736c871339c296c5503c5c5fcabcdd398f899070125f3b94667a"
TAXONOMY = Path("reports/resistance-grounding-2026-10-13-tavaborole")
TAXONOMY_SHA = "9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810"
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "lit_pubmed_id,sequence_version,version"
)
QUERY = "gene_exact:ABCB1 AND organism_id:9606 AND reviewed:true"


def planned_source(root, directory, key, plan_name, url, statuses=(200,)):
    path = directory / plan_name
    plan = json.loads(path.read_bytes())
    attempt = json.loads((directory / (key + "-attempt.json")).read_bytes())
    if (plan["requests"][key]["url"] != url
            or attempt["plan_sha256"] != reference.digest(path)
            or attempt.get("retry_performed") is not False):
        raise ValueError("planned source changed or retried")
    result = native_context.native(root, directory, key, url, statuses)
    receipt = json.loads(reference.check_pin(root, result["receipt"]).read_bytes())
    if receipt.get("redirects_followed") is not False:
        raise ValueError("automatic redirect not permitted")
    return {**result, "plan": reference.pin(root, path)}


def primary_context(payload):
    if hashlib.sha256(payload).hexdigest() != ARTICLE_SHA:
        raise ValueError("reviewed article changed")
    tree = html.fromstring(payload)
    if tree.xpath('//meta[@name="citation_doi"]/@content') != ["10.1371/journal.pgen.0030039"]:
        raise ValueError("primary DOI changed")
    markers = {
        "donor_and_host": "To address the function of human P-gp in yeast",
        "measurement": "The relative resistance of each P-gp variant",
        "figure4_caption": "(A) Alterations in resistance of P-gp variants to valinomycin",
        "substrate_specificity": "We tested the statistical significance of all comparisons",
        "different_drug_host": "Yeast MATa ste6 strains",
        "chemical_identity": "Valinomycin and actinomycin D were from Sigma",
        "reported_gene_id": "accession numbers for the genes described in this paper are 5243",
    }
    locations = {}
    for key, marker in markers.items():
        matches = [p for p in tree.xpath('//div[@id="artText"]//p')
                   if marker in " ".join(p.text_content().split())]
        if len(matches) != 1:
            raise ValueError("primary evidence location absent or ambiguous")
        text = " ".join(matches[0].text_content().split())
        locations[key] = {"xpath": tree.getroottree().getpath(matches[0]),
                          "normalized_text_sha256": hashlib.sha256(text.encode()).hexdigest()}
    return {
        "doi": "DOI:10.1371/journal.pgen.0030039", "pmid": "PMID:17352537",
        "locations": locations, "evidence_type": "HETEROLOGOUS_FUNCTIONAL_EXPERIMENT",
        "donor_gene": "ABCB1", "donor_species": "Homo sapiens",
        "source_reported_donor_gene_id": "NCBIGene:5243",
        "assay_host_species": "Saccharomyces cerevisiae",
        "host_context": "ENGINEERED_LABORATORY_BACKGROUND_NOT_NATIVE_YEAST_ABCB1",
        "endpoint": "EC30", "source_units": "micromolar",
        "endpoint_is_MIC": False, "converted_to_MIC": False,
        "valinomycin_EC50_unavailable_reason": "SOLUBILITY_LIMIT_IN_SOURCE_ASSAY",
        "qualitative_result": "HUMAN_ABCB1_REFERENCE_AND_VARIANT_DEPENDENT_EC30_IN_YEAST",
        "effect_transferred_across_drugs": False,
        "actinomycin_host_transferred_to_valinomycin": False,
        "chemical_scope": "PAPER_NAMES_VALINOMYCIN_AND_SHOWS_A_STRUCTURAL_DEPICTION",
        "exact_product_or_lot_structure_independently_verified": False,
        "supplement_tables_reviewed": False, "per_allele_signoff": False,
        "experimental_genome_assignment": None, "numeric_AST_exported": False,
        "species_wide_or_clinical_resistance_inferred": False,
    }


def project_donor(entry, taxonomy):
    if {"sequence", "features", "comments"}.intersection(entry):
        raise ValueError("unplanned biological payload")
    result = reference.project_reference(entry, "ABCB1", 9606, taxonomy)
    if (entry["primaryAccession"] != "P08183"
            or entry["organism"]["taxonId"] != 9606
            or entry["organism"]["scientificName"] != "Homo sapiens"
            or taxonomy["rank"] != "species" or taxonomy["scientificName"] != "Homo sapiens"
            or result["entry_version"] != 258 or result["sequence_version"] != 3
            or result["gene_names"] != ["ABCB1", "MDR1", "PGY1"]):
        raise ValueError("human donor reference identity changed")
    present = any(i == {"database": "PubMed", "id": "17352537"}
                  for r in result.pop("bibliography") for i in r["identifiers"])
    if present:
        raise ValueError("dated selected citation membership changed")
    return {
        **result, "role": "HUMAN_DONOR_REFERENCE_NOT_TESTED_ALLELE_OR_YEAST_GENE",
        "selected_pmid_in_returned_bibliography": False,
        "citation_absence_disproves_paper_gene_relationship": False,
        "study_reference_allele_equated_to_current_uniprot_sequence": False,
    }


def host_species(taxonomy):
    species = [r for r in taxonomy.get("lineage", []) if r["rank"] == "species"]
    if (taxonomy["taxonId"] != 559292 or taxonomy["rank"] != "strain"
            or taxonomy.get("active") is not True or len(species) != 1
            or species[0]["taxonId"] != 4932
            or species[0]["scientificName"] != "Saccharomyces cerevisiae"):
        raise ValueError("host species reference lineage changed")
    return {"source_species": "Saccharomyces cerevisiae", "species_taxon_id": "NCBITaxon:4932",
            "rank": "species", "reference_strain_taxon_assigned_to_assay_host": False,
            "experimental_strain_taxon_id": None, "experimental_genome_assignment": None}


def build(root, directory=CACHE):
    directory = root / directory
    cohort = json.loads((directory / "cohort.json").read_bytes())
    for key in ("baseline", "protected", "discovery", "census", "previous_checkpoint", "source_queue"):
        reference.check_pin(root, cohort[key])
    record = load_record(reference.check_pin(root, cohort["baseline"]))
    if ((record["identifier"], record["chemical_structure"]["standard_inchi_key"]) != (
            "CHEBI:28545", "FCFNRCROJUBPLU-DNDCDFAISA-N")
            or record.get("resistance_mechanisms") or record.get("activity_spectrum")
            or cohort["record"]["sha256"] != cohort["baseline"]["sha256"]):
        raise ValueError("dated compound identity or claim baseline changed")
    if (cohort["record"]["identifier"] != record["identifier"]
            or cohort["record"]["standard_inchi_key"] != record["chemical_structure"]["standard_inchi_key"]):
        raise ValueError("cohort label differs from dated compound")
    with reference.check_pin(root, cohort["census"]).open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    members = [r for r in rows if r["identifier"] == record["identifier"]]
    if (len(rows) != 2939 or len({r["identifier"] for r in rows}) != 2939 or len(members) != 1
            or members[0]["record_sha256"] != cohort["record"]["sha256"]
            or members[0]["path"] != cohort["record"]["path"]
            or members[0]["standard_inchi_key"] != cohort["record"]["standard_inchi_key"]):
        raise ValueError("dated corpus membership changed")
    sources = {"article": planned_source(root, directory, "article", "request-plan.json", ARTICLE)}
    payload = reference.check_pin(root, sources["article"]["body"]).read_bytes()
    context = primary_context(payload)
    tree = html.fromstring(payload)
    links = {urljoin(ARTICLE, s) for s in tree.xpath('//a/@href')
             if "download&size=large" in s and s.endswith("0030039.g004")}
    if len(links) != 1:
        raise ValueError("native figure link absent or ambiguous")
    sources["figure4"] = planned_source(root, directory, "figure4", "followup-plan.json",
                                        links.pop(), (302,))
    receipt = json.loads(reference.check_pin(root, sources["figure4"]["receipt"]).read_bytes())
    url = {k.lower(): v for k, v in receipt["headers"].items()}["location"]
    parsed = urlsplit(url)
    if (parsed.scheme, parsed.netloc, parsed.path) != (
        "https", "storage.googleapis.com",
        "/plos-corpus-prod/10.1371/journal.pgen.0030039/1/pgen.0030039.g004.PNG_L",
    ):
        raise ValueError("native asset redirect identity changed")
    sources["figure4-storage"] = planned_source(root, directory, "figure4-storage", "asset-plan.json", url)
    assessment = json.loads((directory / "reviewed-assets.json").read_bytes())
    if (sources["figure4-storage"]["body"]["sha256"] != FIGURE_SHA
            or assessment != {"figure_sha256": FIGURE_SHA, "visually_inspected": True,
                              "valinomycin_endpoint": "EC30", "other_endpoint": "EC50",
                              "allele_labels_and_numeric_values_exported": False}):
        raise ValueError("reviewed figure scope changed")
    donor_tax, sources["donor-taxonomy"] = reference.read_response(
        root, directory, "tax-9606", "/taxonomy/9606")
    host_tax, sources["host-taxonomy-reused"] = reference.read_response(
        root, root / TAXONOMY, "tax-559292", "/taxonomy/559292")
    proteins, sources["donor-reference"] = reference.read_response(
        root, directory, "abcb1-reference", "/uniprotkb/search", {
            "query": [QUERY], "fields": [FIELDS], "format": ["json"], "size": ["500"]})
    if (sources["host-taxonomy-reused"]["cache"]["sha256"] != TAXONOMY_SHA
            or sources["donor-reference"]["cache"]["sha256"] != REFERENCE_SHA
            or len(proteins["results"]) != 1
            or any(sources[k]["release"] != "2026_03" for k in (
                "donor-taxonomy", "host-taxonomy-reused", "donor-reference"))):
        raise ValueError("reference result count, checksum or release changed")
    for key, source in (("tax-9606", "donor-taxonomy"), ("abcb1-reference", "donor-reference")):
        sources[key + "-request"] = planned_source(root, directory, key, "followup-plan.json",
                                                    sources[source]["url"])
    return {
        "date": "2026-10-14", "scope": "HUMAN_DONOR_YEAST_HOST_PRIMARY_CONTEXT_NOT_ALLELE_CURATION",
        "cohort": reference.pin(root, directory / "cohort.json"), "record": cohort["record"],
        "inputs": {k: cohort[k] for k in ("baseline", "census", "source_queue", "previous_checkpoint")},
        "sources": sources, "primary": context,
        "reviewed_asset": reference.pin(root, directory / "reviewed-assets.json"),
        "donor_reference": project_donor(proteins["results"][0], donor_tax),
        "host_species_context": host_species(host_tax),
        "curation": {
            "decision": "RETAIN_RESEARCH_DOSSIER_NO_RESISTANCE_OR_ACTIVITY_RECORD_WRITE",
            "reason": "DONOR_HOST_AND_EC30_CONTEXT_REQUIRE_EXPLICIT_REPRESENTATION",
            "proposed_model_followup":
                "Separate donor-protein reference from experimental host and endpoint.",
            "whole_record_primary_review": "OPEN",
        },
        "limitations": [
            "The reviewed figure is not a full supplement or per-allele audit.",
            "The reference accession does not identify the tested reference or variant sequences.",
            "Host species grounding does not assign a strain, genome or species-wide resistance phenotype.",
            "EC30 is not MIC; solubility-limited EC50 is not a negative resistance result.",
            "Drug-dependent effects and different assay backgrounds are not interchangeable.",
            "The separate 2016 ionophore source hold and unresolved cohort remain unchanged.",
        ],
        "limits": {"new_scientific_http_attempts": 5, "ncbi_requests": 0, "ncbi_contact": 0,
                   "issue_1040": "DEFERRED", "reuse_terms_review_resumed": False,
                   "biological_changes": 0, "new_experimental_allele_or_genome_assignments": 0,
                   "whole_record_primary_signoffs": 0, "source_adoptions": 0, "github_mutations": 0,
                   "sequences_variants_constructs_protocols_or_numeric_AST_exported": False},
        "attribution": [
            {"source": "Jeong et al. (2007), PLOS Genetics", "license": "CC BY",
             "url": ARTICLE, "transformation": "Qualitative scope summary and source-location hashes"},
            {"source": "UniProt Consortium", "license": "CC BY 4.0", "release": "2026_03",
             "url": "https://www.uniprot.org/help/license"},
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    body = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != body:
            raise SystemExit("dated valinomycin donor/host checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(body)
    print(json.dumps({"donor": result["donor_reference"]["protein_accession"],
                      "host": result["host_species_context"]["species_taxon_id"],
                      "endpoint": result["primary"]["endpoint"]}))


if __name__ == "__main__":
    main()
