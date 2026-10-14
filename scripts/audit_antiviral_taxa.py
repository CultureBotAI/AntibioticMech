"""Ground one existing claim's species while retaining the complete curator taxon-gap set."""

import argparse
import copy
import csv
import hashlib
import json
from pathlib import Path

import audit_bevirimat_taxonomy as hiv_taxonomy
import audit_card_structure_links as cached
import audit_caspofungin_context as native_context
import audit_topoisomerase_references as reference
from lxml import etree
from resistance_checkpoint_records import checkpoint_path

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-antiviral-taxa")
OUTPUT = Path("research/2026-10-14-antiviral-taxa.json")
PRIMARY = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5118987/fullTextXML"
PRIMARY_SHA = "d51a50d1766b074eabe21ed9edb5b794cd04224597ccbf3e302de65cc20ad9bd"
CLAIM_SHA = "b687b6b02c1223e0358f546f0e1f3e64a3a5cd44a7d054f47fa7fe2ce88d23aa"
GAPS = {
    "bictegravir": "SPECIES_ONLY_CURATION_SUPPORTED",
    "dolutegravir": "PRIMARY_NOT_REQUESTED_AFTER_EBI_SERVER_ERROR",
    "sg85": "EBI_HTTP_500_TECHNICAL_HOLD_NO_RETRY",
    "boceprevir": "EXISTING_PRIMARY_ACCESS_HOLD_UNCHANGED",
    "vaniprevir": "EXISTING_PRIMARY_NOT_REVIEWED_UNCHANGED",
    "dasabuvir": "EXISTING_CHEMICAL_FORM_HOLD_UNCHANGED",
    "paritaprevir": "EXISTING_CHEMICAL_FORM_HOLD_UNCHANGED",
    "oleandomycin": "BIOCHEMICAL_SCOPE_NOT_AUTOMATIC_ORGANISM_ASSIGNMENT",
    "microcin-c": "BIOCHEMICAL_SCOPE_NOT_AUTOMATIC_ORGANISM_ASSIGNMENT",
}


def grounded_claims(identifier, claims):
    if identifier != "CHEBI:172943" or len(claims) != 1:
        raise ValueError("curation cohort changed")
    checksum = hashlib.sha256(json.dumps(claims[0], sort_keys=True, ensure_ascii=True).encode()).hexdigest()
    if checksum != CLAIM_SHA:
        raise ValueError("existing curator claim changed; reassessment required")
    result = copy.deepcopy(claims)
    result[0].update(hiv_taxonomy.SPECIES)
    result[0]["note"] += (
        " Species-grounding update (2026-10-14): the existing laboratory HIV-1 claim is placed "
        "in Lentivirus humimdef1 (NCBITaxon:3418650). The cited paper's Results distinguish "
        "selected viral populations, site-directed test viruses and patient-derived isolates; "
        "these are not interchangeable experimental subjects. This species-only update does "
        "not independently revalidate the inherited variant or quantitative statement, "
        "establish the tested compound's exact formulation, or assign a protein accession, "
        "strain TaxID, experimental genome, patient identity or normalized allele. UniProt's "
        "HIV-1 name node NCBITaxon:11676 is unranked beneath this species."
    )
    result[0]["evidence"].append({
        "reference": "https://rest.uniprot.org/taxonomy/3418650",
        "notes": (
            "Species context only: native UniProt Taxonomy release 2026_03 responses for "
            "11676 (retrieved 2026-10-08) and 3418650 (retrieved 2026-10-14) place the active "
            "HIV-1 name node under active species Lentivirus humimdef1. Cached responses "
            "were reused, not newly queried. PMID:27645238 Results identify HIV-1 in the "
            "laboratory comparison behind the existing claim. Taxonomy does not identify "
            "the tested derivative or establish an experimental protein, allele or genome."
        ),
    })
    return result


def primary_context(payload):
    if hashlib.sha256(payload).hexdigest() != PRIMARY_SHA:
        raise ValueError("inspected primary payload changed")
    tree = etree.fromstring(payload, etree.XMLParser(resolve_entities=False, no_network=True))
    for kind, expected in (("pmid", "27645238"), ("doi", "10.1128/aac.01474-16"),
                           ("pmcid", "PMC5118987")):
        values = tree.xpath(f"front/article-meta/article-id[@pub-id-type='{kind}']/text()")
        if len(values) != 1 or values[0].lower() != expected.lower():
            raise ValueError("primary identity changed")
    if tree.xpath("front/article-meta/permissions/license/license-p/ext-link/@*[local-name()='href']") != [
        "http://creativecommons.org/licenses/by/4.0/",
    ]:
        raise ValueError("native article license changed")
    section = ("body/sec[title='RESULTS']/"
               "sec[title='BIC selected for HIV variants with low-level resistance.']")
    locations = {}
    for name, xpath, required in (
        ("laboratory_organism", section + "/p[1]", ["HIV-1"]),
        ("phenotyped_subject_context", section + "/p[5]", ["site-directed HIV-1"]),
        ("separate_patient_derived_context", "body/sec[title='RESULTS']/sec[5]/p[1]", ["clinical isolates"]),
        ("compound_source", "body/sec[title='MATERIALS AND METHODS']/sec[title='Compounds.']/p[1]", ["BIC"]),
    ):
        rows = tree.xpath(xpath)
        if len(rows) != 1:
            raise ValueError("primary evidence location changed")
        text = " ".join(rows[0].itertext())
        if not all(value in text for value in required):
            raise ValueError("primary organism or subject context changed")
        locations[name] = {"xpath": xpath, "text_sha256": hashlib.sha256(text.encode()).hexdigest()}
    return {
        "pmid": "27645238", "pmcid": "PMC5118987", "doi": "10.1128/AAC.01474-16",
        "attribution": "Tsiang et al. (2016), CC BY 4.0", "locations": locations,
        "review_scope": ("Selected Results subsections and compound-source paragraph; "
                         "organism/subject scope only"),
        "source_organism_label": "HIV-1", "existing_claim_context": "LABORATORY_NOT_PATIENT_ASSIGNMENT",
        "selected_populations_and_site_directed_test_viruses_are_interchangeable": False,
        "native_figures_or_supplements_reviewed": False, "exact_compound_form_newly_resolved": False,
        "all_inherited_variant_or_quantitative_claims_revalidated": False,
        "new_sequences_variants_constructs_protocols_or_numeric_AST_exported": False,
    }


def build(root, directory=CACHE):
    directory = root / directory
    cohort_path = directory / "cohort.json"
    cohort = json.loads(cohort_path.read_bytes())
    inputs = {key: cohort[key] for key in (
        "census", "field_index", "publications", "prior_checkpoint", "source_queue", "protected")}
    paths = {key: reference.check_pin(root, pin) for key, pin in inputs.items()}
    index = json.loads(paths["field_index"].read_bytes())
    gaps = [row for row in index["claims"] if row["taxon_id_slot"] is None]
    if gaps != cohort["all_curator_taxon_gap_claims"] or len(gaps) != 11:
        raise ValueError("complete historical taxon-gap selection changed")
    with paths["census"].open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (len(census) != 2939 or len({r["path"] for r in census}) != len(census)
            or {r["path"] for r in census} != {
                str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
            or any(reference.digest(checkpoint_path(root, row)) != row["record_sha256"] for row in census)):
        raise ValueError("historical corpus census changed")
    for item in cohort["records"].values():
        record = load_record(checkpoint_path(root, item))
        if (record["identifier"] != item["identifier"] or record["chemical_structure"]["standard_inchi_key"]
                != item["standard_inchi_key"]):
            raise ValueError("historical compound identity changed")
        if record["identifier"] == "CHEBI:172943":
            grounded_claims(record["identifier"], record["resistance_mechanisms"])
    source = native_context.native(root, directory, "bictegravir-primary", PRIMARY)
    primary = primary_context(reference.check_pin(root, source["body"]).read_bytes())
    canary_path = directory / "primary-canary-reviewed.json"
    canary = json.loads(canary_path.read_bytes())
    if canary["article"] != source["body"] or not canary["remaining_two_primary_requests_allowed"]:
        raise ValueError("primary canary changed")
    sg85 = native_context.native(root, directory, "sg85-primary",
        "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4538484/fullTextXML", statuses=(500,))
    error = json.loads(reference.check_pin(root, sg85["body"]).read_bytes())
    if (error.get("status") != 500 or error.get("error") != "Internal Server Error"
            or error.get("path") != "/europepmc/webservices/rest/PMC4538484/fullTextXML"):
        raise ValueError("technical failure body changed")
    if {p.name for p in directory.rglob("*-attempt.json")} != {
        "bictegravir-primary-attempt.json", "sg85-primary-attempt.json",
    }:
        raise ValueError("unplanned or post-stop request detected in this checkpoint cache")
    prior_path = root / "research/2026-10-14-bevirimat-taxonomy.json"
    prior = json.loads(prior_path.read_bytes())
    receipt, parent, parent_source = cached.receipt(
        root, reference.check_pin(root, prior["sources"]["parent_reused"]["cache"]), "rest.uniprot.org")
    if receipt["url"] != "https://rest.uniprot.org/taxonomy/11676":
        raise ValueError("cached HIV-1 taxonomy changed")
    species, species_source = reference.read_response(
        root, root / hiv_taxonomy.CACHE, "species-taxonomy", "/taxonomy/3418650")
    if (species_source != prior["sources"]["species"]
            or {k.lower(): v for k, v in receipt["headers"].items()}.get("x-uniprot-release") != "2026_03"):
        raise ValueError("reused taxonomy provenance changed")
    taxonomy = hiv_taxonomy.project_taxonomy(parent, species)
    dispositions = [{"record_identifier": row["record_identifier"], "record_path": row["record_path"],
                     "resistance_index": row["resistance_index"], "claim_sha256": row["claim_sha256"],
                     "status": GAPS[Path(row["record_path"]).stem]} for row in gaps]
    return {
        "date": "2026-10-14", "scope": "COMPLETE_CURATOR_TAXON_GAP_SELECTION_ONE_SPECIES_ONLY_CURATION",
        "inputs": {**inputs, "cohort": reference.pin(root, cohort_path),
                   "prior_taxonomy": reference.pin(root, prior_path)},
        "record_before": cohort["records"]["CHEBI:172943"], "primary": primary, "taxonomy": taxonomy,
        "sources": {"bictegravir_primary": source, "sg85_technical_failure": sg85,
                    "parent_taxonomy_reused": parent_source, "species_taxonomy_reused": species_source},
        "primary_canary": reference.pin(root, canary_path), "taxon_gap_dispositions": dispositions,
        "summary": {"corpus_record_hashes_checked": 2939, "historical_taxon_gap_claims": 11,
                    "historical_taxon_gap_records": 9, "claims_supported_for_species_grounding": 1,
                    "new_network_requests": 2, "new_taxonomy_or_protein_requests": 0,
                    "primary_technical_failures": 1, "primary_leads_not_requested_after_error": 1,
                    "new_resistance_claims": 0, "experimental_alleles_or_genomes_assigned": 0,
                    "whole_record_primary_signoffs": 0},
        "limits": {"ncbi_requests": 0, "issue_1040": "DEFERRED", "held_sources_retried": False,
                   "github_mutations": 0, "source_adoptions": 0, "full_corpus_goal_status": "OPEN",
                   "full_corpus_records_in_scope": 2939, "independent_scientific_signoff": False,
                   "sg85_error_establishes_permission_or_global_unavailability": False,
                   "dolutegravir_full_text_request_attempted": False,
                   "primary_or_taxonomy_references_are_experimental_allele_assignments": False},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    if args.check:
        if json.loads(OUTPUT.read_bytes()) != result:
            raise SystemExit("antiviral taxon dossier does not reproduce")
    else:
        with OUTPUT.open("x") as stream:
            stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
