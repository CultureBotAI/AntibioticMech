"""Replay a susceptibility screen without promoting it to resistant-allele evidence."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode

import audit_card_reference_lineages as lineages
import audit_topoisomerase_references as reference
from audit_beauvericin_references import complete_query
from audit_ciclopirox_context import STRUCTURES, title
from audit_stth_reference import FIELDS
from audit_valinomycin_abcb1 import planned_source
from lxml import html

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-ciclopirox-primary")
OUTPUT = Path("research/2026-10-14-ciclopirox-primary-context.json")
COHORT_SHA = "ae69c355c087938d192f859844785bd5440c4022dcc15658104baef1fcff769e"
ARTICLE = "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0210547"
ARTICLE_SHA = "51a9812496ff1053e673c2fa811bd42c0b8c696712eef656ea8b76623ad5a1d1"
PMID = "30633761"
DOI = "10.1371/journal.pone.0210547"
QUERY = "lit_pubmed:" + PMID
TAX_CACHE = Path("reports/resistance-grounding-2026-10-09-topoisomerase-followup")
TAX_SOURCE = {
    "body": {
        "path": str(TAX_CACHE / "reference-tax-83333-response.bin"),
        "sha256": "83c59ae9694d1874b8a175d7ce7608f77f5688d35adf307a0859dbb20f9e1c17",
    },
    "receipt": {
        "path": str(TAX_CACHE / "reference-tax-83333-receipt.json"),
        "sha256": "748b6875ab51cbbbefe77a38ef7dbc7a2a0034cd368336e5f2717e002429b4f9",
    },
}
MARKERS = {
    "chemical_supplier": "Sodium molybdate, sodium nitrite, and ciclopirox were from Santa Cruz",
    "laboratory_subject": "BW25113 (the isogenic parent strain)",
    "measurement": "Minimum inhibitory concentrations (MICs) were measured using a broth dilution",
    "screen_scope": "We selected a group of 96 mutant strains",
    "screen_direction": "Forty-three of these mutant strains had significantly lower",
    "comparison_filters": "These efforts resulted in 21 deletion mutants with lower ciclopirox MICs",
    "prior_study_not_current_experiment": "In our previous work we found",
    "negative_resistance_context": "there was no change in ciclopirox MIC (S1 Table)",
    "target_caution": "we must consider other possibilities",
    "assay_specificity_limit": "The Arnow Assay measures catechol siderophores",
    "conclusion_limit": "While we cannot conclude that these different bacterial effects",
}


def selected_lead(previous, selected):
    matches = []
    for source in previous["discovery"]:
        for row in source["records"]:
            for query in row["queries"]:
                for candidate in query["candidates"]:
                    if candidate.get("source") == "MED" and candidate.get("id") == PMID:
                        if row["identifier"] != "CHEBI:453011":
                            raise ValueError("selected discovery compound changed")
                        matches.append(candidate)
    if (
        len(matches) != 2
        or any(candidate != selected for candidate in matches)
        or selected.get("pmid") != PMID
        or selected.get("doi") != DOI
        or selected.get("pmcid") != "PMC6329577"
        or selected.get("pubYear") != "2019"
    ):
        raise ValueError("selected discovery publication changed")
    return {"lead": selected, "query_memberships": 2, "independent_publications": 1}


def primary_context(payload, lead):
    if hashlib.sha256(payload).hexdigest() != ARTICLE_SHA:
        raise ValueError("reviewed primary body changed")
    tree = html.fromstring(payload)
    titles = tree.xpath('//meta[@name="citation_title"]/@content')
    if (
        tree.xpath('//meta[@name="citation_doi"]/@content') != [DOI]
        or tree.xpath('//meta[@name="citation_date"]/@content') != ["Jan 11, 2019"]
        or len(titles) != 1
        or title(titles[0]) != title(lead["title"])
    ):
        raise ValueError("primary publication identity changed")
    locations = {}
    for key, marker in MARKERS.items():
        matches = [
            p for p in tree.xpath('//div[@id="artText"]//p') if marker in " ".join(p.text_content().split())
        ]
        if len(matches) != 1:
            raise ValueError("primary evidence location absent or ambiguous")
        text = " ".join(matches[0].text_content().split())
        locations[key] = {
            "xpath": tree.getroottree().getpath(matches[0]),
            "normalized_text_sha256": hashlib.sha256(text.encode()).hexdigest(),
        }
    return {
        "pmid": "PMID:" + PMID,
        "doi": "DOI:" + DOI,
        "locations": locations,
        "review_scope": "SELECTED_PRIMARY_TEXT_NOT_FIGURES_OR_SUPPLEMENT_TABLES",
        "evidence_type": "LABORATORY_FUNCTIONAL_SUSCEPTIBILITY_SCREEN",
        "source_species": "Escherichia coli",
        "source_parent_strain": "BW25113",
        "source_background": "K-12",
        "screened_deletion_strains": 96,
        "source_reported_lower_MIC_strains": 43,
        "source_reported_specific_subset": 21,
        "phenotype_direction": "INCREASED_SUSCEPTIBILITY_NOT_INCREASED_RESISTANCE",
        "direct_target_established_by_screen": False,
        "prior_study_results_counted_as_current_experiments": False,
        "catechol_signal_is_exclusive_enterobactin_measurement": False,
        "endpoint": "MIC",
        "assay": "BROTH_DILUTION",
        "standard_for_future_MIC_normalization": "mg/L",
        "numeric_AST_exported_or_converted": False,
        "clinical_breakpoint_or_resistance_call_inferred": False,
        "alleles_variants_constructs_sequences_or_protocols_exported": False,
        "experimental_genome_assignment": None,
        "per_gene_or_allele_signoff": False,
    }


def species_context(taxon):
    _, species = lineages.lineage(taxon)
    if (
        lineages.identity(taxon)
        != {"taxonId": 83333, "scientificName": "Escherichia coli (strain K12)", "rank": "strain"}
        or species != {"taxonId": 562, "scientificName": "Escherichia coli", "rank": "species"}
        or [s for s in taxon.get("strains", []) if s.get("name") == "K12 / BW25113"]
        != [{"name": "K12 / BW25113"}]
    ):
        raise ValueError("reference species or K12 strain-list context changed")
    return {
        "source_species": species["scientificName"],
        "species_taxon_id": "NCBITaxon:562",
        "rank": "species",
        "grounding_basis": "SPECIES_NODE_IN_REUSED_UNIPROT_K12_LINEAGE",
        "reference_taxon_id": "NCBITaxon:83333",
        "reference_taxon_rank": "strain",
        "reference_lists_BW25113": True,
        "reference_taxon_uniquely_identifies_BW25113": False,
        "experimental_derivative_taxon_id": None,
        "experimental_genome_assignment": None,
        "phenotype_transferred_to_species_or_other_strains": False,
    }


def citation_context(payload, headers):
    complete_query(payload, headers, 0)
    return {
        "query": QUERY,
        "release": "2026_03",
        "returned_entries": 0,
        "query_complete": True,
        "result": "SCOPED_EMPTY_PUBLICATION_CITATION_QUERY",
        "protein_absence_or_lack_of_function_inferred": False,
        "gene_name_or_locus_queries_performed": False,
        "allele_or_protein_assignment": None,
    }


def build(root, directory=CACHE):
    directory = root / directory
    keys = {"article-2019", "reference-2019"}
    if any(
        {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} != keys
        for suffix in ("-attempt.json", "-receipt.json", "-response.bin")
    ):
        raise ValueError("request inventory changed")
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    for key in ("previous_cohort", "previous_context", "previous_verification", "source_queue"):
        reference.check_pin(root, cohort[key])
    protected = json.loads(reference.check_pin(root, cohort["protected"]).read_bytes())
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or any(protected.get(r["path"]) != r["record_sha256"] for r in census)
        or len(cohort["records"]) != 2
        or {r["identifier"] for r in cohort["records"]} != set(STRUCTURES)
    ):
        raise ValueError("corpus baseline changed")
    for row in cohort["records"]:
        record = load_record(reference.check_pin(root, row["snapshot"]))
        slug, structure = STRUCTURES[row["identifier"]]
        if (
            record["identifier"] != row["identifier"]
            or record["label"] != row["label"]
            or record["chemical_structure"]["standard_inchi_key"] != structure
            or row["standard_inchi_key"] != structure
            or row["record"]["path"] != f"data/antibiotics/antibacterial/{slug}.yaml"
            or row["record"]["sha256"] != row["snapshot"]["sha256"]
            or protected.get(row["record"]["path"]) != row["record"]["sha256"]
            or record.get("resistance_mechanisms")
            or record.get("genotype_resistance_score_rules")
        ):
            raise ValueError("historical exact-structure record changed")
    previous = json.loads(reference.check_pin(root, cohort["previous_cohort"]).read_bytes())
    discovery = selected_lead(previous, cohort["selected_lead"])
    url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {"query": QUERY, "format": "json", "size": 500, "fields": FIELDS}
    )
    sources = {}
    for key, plan_name, target in (
        ("article-2019", "request-plan.json", ARTICLE),
        ("reference-2019", "reference-plan.json", url),
    ):
        source = planned_source(root, directory, key, plan_name, target)
        plan = json.loads(reference.check_pin(root, source["plan"]).read_bytes())
        if (
            plan.get("cohort") != reference.pin(root, cohort_path)
            or set(plan["requests"]) != {key}
            or plan["requests"][key].get("canary") is not True
            or any(
                plan.get(flag) is not False
                for flag in ("automatic_redirects", "retry_performed", "prior_source_holds_retried")
            )
            or plan.get("ncbi_requests") != 0
        ):
            raise ValueError("source plan scope changed")
        sources[key] = source
        if key == "reference-2019" and plan.get("article") != sources["article-2019"]["body"]:
            raise ValueError("reference query primary canary binding changed")
    primary = primary_context(
        reference.check_pin(root, sources["article-2019"]["body"]).read_bytes(), cohort["selected_lead"]
    )
    source = sources["reference-2019"]
    citation = citation_context(
        json.loads(reference.check_pin(root, source["body"]).read_bytes()),
        json.loads(reference.check_pin(root, source["receipt"]).read_bytes())["headers"],
    )
    taxon, tax_source = lineages.native_taxon(root, TAX_SOURCE, "83333", "2026_03")
    return {
        "date": "2026-10-14",
        "scope": "PRIMARY_SUSCEPTIBILITY_SCREEN_CONTEXT_NOT_RESISTANT_ALLELE_CURATION",
        "cohort": reference.pin(root, cohort_path),
        "baseline_commit": cohort["baseline_commit"],
        "records": cohort["records"],
        "census": cohort["census"],
        "previous_context": cohort["previous_context"],
        "previous_verification": cohort["previous_verification"],
        "discovery": discovery,
        "sources": sources,
        "primary": primary,
        "citation_query": citation,
        "taxonomy_source_reused": tax_source,
        "species_context": species_context(taxon),
        "chemical_scope": {
            "source_compound_name": "ciclopirox",
            "source_supplier": "Santa Cruz Biotechnologies",
            "exact_product_or_lot_structure_independently_verified": False,
            "compound_record_assignment": None,
            "neutral_and_olamine_records_kept_distinct": True,
            "salt_and_neutral_results_transferred": False,
        },
        "curation_decision": "RETAIN_QUALITATIVE_DOSSIER_WITHOUT_BIOLOGICAL_RECORD_WRITE",
        "curation_limitations": [
            "The screen's lower MIC direction is not an increased-resistance phenotype.",
            "Native figures and supplementary MIC tables have not been reviewed.",
            "A compound name and supplier do not independently establish the tested exact structure.",
            "The empty citation query does not establish absence of reference proteins or gene function.",
            "K12 taxonomy context does not assign experimental derivatives or genomes.",
            "Prior-study results mentioned in the introduction or discussion are not revalidated here.",
        ],
        "limits": {
            "scientific_http_attempts": 2,
            "http_status_counts": {"200": 2},
            "selected_primary_text_reviews": 1,
            "native_figures_and_supplements_reviewed": False,
            "native_taxonomy_responses_reused": 1,
            "new_taxonomy_requests": 0,
            "biological_records_changed": 0,
            "new_resistance_assertions_or_experimental_identifiers": 0,
            "whole_record_primary_signoffs": 0,
            "retries": 0,
            "automatic_redirects": 0,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "prior_source_holds_preserved": True,
            "source_adoptions": 0,
            "github_mutations": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": [
            {
                "source": "Conley et al. (2019), PLOS ONE",
                "license": "CC BY",
                "url": ARTICLE,
                "transformation": "Qualitative scope summary and source-location hashes",
            },
            {"source": "UniProt Consortium", "license": "CC BY 4.0", "release": "2026_03"},
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != payload:
            raise SystemExit("Ciclopirox primary checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {
                "primary_text_reviews": 1,
                "citation_query_entries": 0,
                "species": "NCBITaxon:562",
                "biological_records_changed": 0,
            }
        )
    )


if __name__ == "__main__":
    main()
