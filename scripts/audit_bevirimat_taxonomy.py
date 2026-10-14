"""Ground an existing HIV-1 claim at species rank without assigning viral alleles."""

import argparse
import copy
import csv
import hashlib
import json
from pathlib import Path

import audit_card_structure_links as cached
import audit_caspofungin_context as native_context
import audit_topoisomerase_references as reference
from lxml import etree
from resistance_checkpoint_records import checkpoint_path

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-bevirimat")
OUTPUT = Path("research/2026-10-14-bevirimat-taxonomy.json")
PRIMARY = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2873507/fullTextXML"
PRIMARY_SHA = "e10a8d91e352eca2e5769a5f3f7f1015288bd33832e67ac2502b386ca6febb4b"
SPECIES_SHA = "25b4c314a4dc5ed2e4efd97fad3ee5de4b18fb7045fa0bca82b92ed42ec48f8e"
EMPTY_SHA = "5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84"
CLAIM_SHA = "65f38c45202d14f1f51dee47ac64c135ff012e32c0ebeae9e601e480ff1fa1d4"
SPECIES = {"taxon_id": "NCBITaxon:3418650", "taxon_label": "Lentivirus humimdef1"}
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_embl,lit_pubmed_id,sequence_version,version"
)


def grounded_claims(identifier, claims):
    if identifier != "CHEBI:65484" or len(claims) != 1:
        raise ValueError("curation cohort changed")
    checksum = hashlib.sha256(json.dumps(claims[0], sort_keys=True, ensure_ascii=True).encode()).hexdigest()
    if checksum != CLAIM_SHA:
        raise ValueError("existing curator claim changed; reassessment required")
    result = copy.deepcopy(claims)
    result[0].update(SPECIES)
    result[0]["note"] += (
        " Species-grounding update (2026-10-14): the existing HIV-1 claim is placed in "
        "Lentivirus humimdef1 (NCBITaxon:3418650). UniProt's Human immunodeficiency virus type 1 "
        "node NCBITaxon:11676 is unranked beneath that species, not itself a species-rank node. "
        "The 2010 paper's Results and Conclusions describe laboratory comparisons in the "
        "NL4-3 background; that background is not an exact identifier for the tested derivatives "
        "or a patient-isolate assignment. This update does not revalidate every inherited "
        "variant assertion or the tested compound's exact formulation. No protein accession, "
        "strain TaxID, experimental genome or normalized allele is assigned."
    )
    result[0]["evidence"].append({
        "reference": "https://rest.uniprot.org/taxonomy/3418650",
        "notes": (
            "Species context only: UniProt release 2026_03, retrieved 2026-10-14, identifies active "
            "species Lentivirus humimdef1, NCBITaxon:3418650. The separately pinned native "
            "taxonomy/11676 response (retrieved 2026-10-08, same release) identifies HIV-1 as "
            "an active unranked child of this species. These taxonomy records do not establish "
            "experimental strain, protein, allele, genome or patient identity."
        ),
    })
    return result


def project_taxonomy(parent, species):
    lineage = [x for x in parent.get("lineage", []) if x.get("rank") == "species"]
    if (
        parent.get("taxonId") != 11676 or parent.get("rank") != "no rank"
        or parent.get("active") is not True or parent.get("commonName") != "HIV-1"
        or parent.get("scientificName") != "Human immunodeficiency virus type 1"
        or parent.get("parent") != {"taxonId": 3418650, "scientificName": "Lentivirus humimdef1"}
        or len(lineage) != 1 or lineage[0].get("taxonId") != 3418650
        or lineage[0].get("scientificName") != "Lentivirus humimdef1"
        or species.get("taxonId") != 3418650 or species.get("scientificName") != "Lentivirus humimdef1"
        or species.get("rank") != "species" or species.get("active") is not True
        or species.get("parent") != {"taxonId": 11646, "scientificName": "Lentivirus"}
    ):
        raise ValueError("HIV-1 source-name, rank or species lineage changed")
    return {
        "source_name": parent["scientificName"], "source_common_name": "HIV-1",
        "source_context_id": "NCBITaxon:11676", "source_context_rank": "no rank",
        "species": SPECIES, "species_rank": "species",
        "assignment_scope": "SPECIES_LINEAGE_ONLY_NOT_TESTED_DERIVATIVE_OR_PATIENT",
        "experimental_allele_assignment": None, "experimental_genome_assignment": None,
        "experimental_strain_taxon_assignment": None, "protein_accession_assignment": None,
    }


def primary_context(payload):
    if hashlib.sha256(payload).hexdigest() != PRIMARY_SHA:
        raise ValueError("reviewed primary article changed")
    tree = etree.fromstring(payload, parser=etree.XMLParser(resolve_entities=False, no_network=True))
    for kind, expected in (("pmid", "20406463"), ("doi", "10.1186/1742-4690-7-36"), ("pmcid", "PMC2873507")):
        if tree.xpath(f"front/article-meta/article-id[@pub-id-type='{kind}']/text()") != [expected]:
            raise ValueError("primary identity changed")
    if tree.xpath("front/article-meta/permissions/license/@*[local-name()='href']") != [
        "http://creativecommons.org/licenses/by/2.0",
    ]:
        raise ValueError("primary attribution license changed")
    locations = {}
    for name, xpath in (
        ("laboratory_background", "body/sec[title='Results and Discussion']/sec[1]/p[1]"),
        ("conclusion_scope", "body/sec[title='Conclusions']/p[1]"),
    ):
        rows = tree.xpath(xpath)
        if len(rows) != 1:
            raise ValueError("primary evidence location absent or ambiguous")
        text = " ".join(rows[0].itertext())
        if "HIV-1" not in text or "NL4-3" not in text:
            raise ValueError("primary organism or background context changed")
        locations[name] = {"xpath": xpath, "text_sha256": hashlib.sha256(text.encode()).hexdigest()}
    return {
        "pmid": "20406463", "doi": "10.1186/1742-4690-7-36", "pmcid": "PMC2873507",
        "locations": locations, "source_organism_label": "HIV-1", "laboratory_background_label": "NL4-3",
        "review_scope": "Results and Discussion, Conclusions and figure legends",
        "native_images_visually_inspected": False, "patient_isolates_tested_in_this_study": False,
        "background_is_exact_experimental_derivative": False, "exact_compound_form_newly_resolved": False,
        "functional_claims_newly_curated": False,
        "sequences_variants_protocols_or_numeric_AST_exported": False,
        "attribution": "Adamson et al., Retrovirology 7:36 (2010), CC BY 2.0",
    }


def build(root, directory):
    cohort_path = directory / "cohort.json"
    cohort = json.loads(cohort_path.read_bytes())
    for key in ("census", "protected", "source_queue", "publications_reused", "curator_field_index",
                "prior_checkpoint", "prior_taxonomy_context", "baseline_record"):
        reference.check_pin(root, cohort[key])
    baseline = reference.check_pin(root, cohort["baseline_record"])
    if reference.digest(baseline) != cohort["record"]["sha256"]:
        raise ValueError("historical record baseline changed")
    record = load_record(baseline)
    if (record["identifier"], record["chemical_structure"]["standard_inchi_key"]) != (
        "CHEBI:65484", "YJEJKUQEXFSVCJ-WRFMNRASSA-N",
    ):
        raise ValueError("compound identity changed")
    grounded_claims(record["identifier"], record["resistance_mechanisms"])
    with reference.check_pin(root, cohort["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939 or len({r["identifier"] for r in census}) != 2939
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        or any(reference.digest(checkpoint_path(root, r)) != r["record_sha256"] for r in census)
    ):
        raise ValueError("historical corpus membership or hashes changed")
    publications = json.loads(
        reference.check_pin(root, cohort["publications_reused"]).read_bytes())["results"]
    cited = {key: {field: publications[key][field] for field in ("pmid", "pmcid", "doi", "isOpenAccess")}
             for key in ("19279107", "20406463")}
    if cited["20406463"] != {"pmid": "20406463", "pmcid": "PMC2873507",
                            "doi": "10.1186/1742-4690-7-36", "isOpenAccess": "Y"}:
        raise ValueError("reused cited-paper identity changed")
    source = native_context.native(root, directory, "primary-2010", PRIMARY)
    primary = primary_context(reference.check_pin(root, source["body"]).read_bytes())
    sources = {"primary": source}
    plan_path = directory / "reference-plan.json"
    plan = json.loads(plan_path.read_bytes())
    canary = json.loads(reference.check_pin(root, plan["canary"]).read_bytes())
    if canary["article"] != source["body"] or canary["reference_metadata_queries_approved"] is not True:
        raise ValueError("primary canary changed")
    species, sources["species"] = reference.read_response(
        root, directory, "species-taxonomy", "/taxonomy/3418650")
    if sources["species"]["cache"]["sha256"] != SPECIES_SHA:
        raise ValueError("reviewed species response changed")
    prior = json.loads(reference.check_pin(root, cohort["prior_taxonomy_context"]).read_bytes())
    parent_path = reference.check_pin(root, prior["inputs"]["cached_parent_taxonomy"])
    receipt, parent, sources["parent_reused"] = cached.receipt(root, parent_path, "rest.uniprot.org")
    if receipt["url"] != "https://rest.uniprot.org/taxonomy/11676":
        raise ValueError("reused HIV-1 taxonomy endpoint changed")
    if {k.lower(): v for k, v in receipt["headers"].items()}.get("x-uniprot-release") != "2026_03":
        raise ValueError("reused taxonomy release changed")
    taxonomy = project_taxonomy(parent, species)
    queries = {}
    for key, endpoint, parameters in (
        ("nl43-taxonomy", "/taxonomy/search", {"query": ["NL4-3"], "format": ["json"], "size": ["100"]}),
        ("gag-reference", "/uniprotkb/search", {"query": ["gene_exact:gag AND organism_name:NL4-3"],
            "format": ["json"], "size": ["100"], "sort": ["accession asc"], "fields": [FIELDS]}),
    ):
        payload, sources[key] = reference.read_response(root, directory, key, endpoint, parameters)
        if payload != {"results": []} or sources[key]["cache"]["sha256"] != EMPTY_SHA:
            raise ValueError("scoped empty reference query changed")
        queries[key] = {"query": parameters["query"][0], "result_count": 0,
                        "complete_for_query": True, "zero_results_establish_absence": False,
                        "alternate_reference_selected": False}
    for key in ("species", "nl43-taxonomy", "gag-reference"):
        if sources[key]["release"] != "2026_03":
            raise ValueError("reference release changed")
        native_key = "species-taxonomy" if key == "species" else key
        if plan["queries"][native_key] != sources[key]["url"]:
            raise ValueError("reference query differs from plan")
        sources[key + "_request"] = native_context.native(root, directory, native_key, sources[key]["url"])
    return {
        "date": "2026-10-14", "cohort": reference.pin(root, cohort_path), "record_before": cohort["record"],
        "baseline_record": cohort["baseline_record"], "reference_plan": reference.pin(root, plan_path),
        "sources": sources, "primary": primary, "cited_papers": cited,
        "taxonomy": taxonomy, "queries": queries,
        "curation_scope": {"existing_claims_grounded_at_species_rank": 1, "new_resistance_claims": 0,
                           "full_corpus_records_in_scope": 2939, "whole_record_primary_signoffs": 0,
                           "no_new_patient_strain_protein_allele_or_genome_assignment": True},
        "limits": {"ncbi_requests": 0, "issue_1040": "DEFERRED", "github_mutations": 0,
                   "source_adoptions": 0, "held_sources_retried": False,
                   "primary_2009_results_reviewed_in_this_checkpoint": False,
                   "all_inherited_variant_claims_revalidated": False,
                   "numeric_AST_exported": False, "independent_scientific_signoff": False,
                   "whole_record_primary_review": "OPEN"},
        "attribution": "UniProt Consortium, release 2026_03, CC BY 4.0; primary attribution retained above",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    result = build(root, root / CACHE)
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.output.exists() and args.output.read_bytes() != payload:
        raise ValueError("refusing to replace a historical checkpoint")
    args.output.write_bytes(payload)
    print(json.dumps(result["curation_scope"], sort_keys=True))


if __name__ == "__main__":
    main()
