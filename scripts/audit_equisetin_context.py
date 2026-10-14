"""Distinguish equisetin activity from resistance alleles and producer loci."""

import argparse
import csv
import gzip
import hashlib
import json
from pathlib import Path

import audit_card_reference_lineages as lineages
import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import planned_source
from lxml import etree

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-equisetin")
OUTPUT = Path("research/2026-10-14-equisetin-context.json")
COHORT_SHA = "dfd4bad7054379a49846f546178b19fb1bfa8f58924d33b36c404fae2936a61c"
ARTICLE_SHA = "06fff8d0c21801f1a6dcb66377b2f245a17770ead760408772af9c33f1d4a5ec"
ARTICLE = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8632820/fullTextXML"
DOI = "10.3389/fchem.2021.772858"
LEADS = {
    "AGR:IND608566932",
    "MED:10934347",
    "MED:17707105",
    "MED:23715404",
    "MED:26431450",
    "MED:34869220",
    "MED:38327434",
    "MED:41317882",
}
LOCATIONS = {
    "organisms": ("/article/body/sec[2]/sec[1]/p", "Bacillus subtilis ATCC6051"),
    "comparative_genomes": ("/article/body/sec[2]/sec[3]/p", "sources of ftd-like gene clusters"),
    "chemical_source": ("/article/body/sec[2]/sec[4]/p", "Ikarugamycin and equisetin were ordered"),
    "assay_subject": ("/article/body/sec[2]/sec[8]/p", "Bacillus subtilis ATCC 6051"),
    "producer_locus": ("/article/body/sec[3]/sec[1]/p", "putative PTM BGC"),
    "isolated_compound": ("/article/body/sec[3]/sec[2]/p[2]", "identical to xanthobaccin A"),
    "activity_result": (
        "/article/body/sec[3]/sec[3]/p[1]",
        "All three tetramates had antimicrobial activity",
    ),
    "metal_binding": ("/article/body/sec[3]/sec[3]/p[3]", "two different enolic tautomers of equisetin"),
    "other_compound_stress": (
        "/article/body/sec[3]/sec[3]/p[4]",
        "HSAF-mutant was less susceptible to oxidative stress",
    ),
    "other_compound_transcriptomics": (
        "/article/body/sec[3]/sec[3]/p[6]",
        "evidence from HSAF in Candida albicans",
    ),
    "non_genetic_modulation": (
        "/article/body/sec[3]/sec[3]/p[8]",
        "vitamin C reduced the antibacterial effects",
    ),
    "proposed_mechanism": ("/article/body/sec[3]/sec[3]/fig[2]/caption/p", "Proposed mode-of-action"),
}


def primary_context(payload):
    if hashlib.sha256(payload).hexdigest() != ARTICLE_SHA:
        raise ValueError("reviewed primary article changed")
    root = etree.fromstring(payload, parser=etree.XMLParser(resolve_entities=False, no_network=True))
    ids = {n.get("pub-id-type"): n.text for n in root.xpath("./front/article-meta/article-id")}
    if (
        root.get("article-type") != "research-article"
        or ids.get("pmid") != "34869220"
        or ids.get("pmcid") != "PMC8632820"
        or ids.get("doi") != DOI
    ):
        raise ValueError("primary publication identity changed")
    locations = {}
    for key, (xpath, marker) in LOCATIONS.items():
        nodes = root.xpath(xpath)
        if len(nodes) != 1:
            raise ValueError("reviewed primary location absent or ambiguous")
        text = " ".join("".join(nodes[0].itertext()).split())
        if marker not in text:
            raise ValueError("reviewed primary context changed")
        locations[key] = {"xpath": xpath, "normalized_text_sha256": hashlib.sha256(text.encode()).hexdigest()}
    return {
        "reference": "PMID:34869220",
        "doi": "DOI:" + DOI,
        "article_type": "research-article",
        "review_scope": "SELECTED_PRIMARY_TEXT_AND_CAPTIONS",
        "locations": locations,
        "figures_visually_reviewed": False,
        "supplements_reviewed": False,
        "evidence_type": "MEASURED_ACTIVITY_AND_NON_GENETIC_MODULATION_WITH_BIOCHEMICAL_SUPPORT",
        "chemical_scope": {
            "source_name": "equisetin",
            "source_material": "COMMERCIAL_SIGMA_ALDRICH_MATERIAL",
            "exact_product_lot_or_stereochemical_identity_independently_verified": False,
            "metal_complexes_equated_to_neutral_record": False,
            "paper_spelling_variants_added_as_corpus_synonyms": False,
        },
        "observations": {
            "antibacterial_activity_reported": True,
            "vitamin_C_reduces_antibacterial_effect": True,
            "modulation_is_resistant_genotype_evidence": False,
            "source_endpoints": ["MIC", "AGAR_DIFFUSION_INHIBITION_ZONE"],
            "source_MIC_units": "ug/mL",
            "standard_MIC_unit_if_curated": "mg/L",
            "source_zone_units": "mm",
            "zone_converted_to_MIC": False,
            "numeric_AST_exported": False,
            "clinical_resistance_call_inferred": False,
        },
        "gene_scope": {
            "producer_gene_cluster_compound": "xanthobaccin A",
            "producer_name": "Actinoalloteichus hymeniacidonis",
            "producer_locus_is_assay_subject_resistance_gene": False,
            "comparative_gene_cluster_accessions_are_assay_genomes": False,
            "HSAF_oxidative_stress_and_transcriptomic_results_transferred_to_equisetin": False,
            "gene_or_allele_link_established_for_equisetin_in_reviewed_results": False,
            "no_resistance_gene_exists_inferred": False,
            "uniprot_assignment": None,
        },
        "mechanism": {
            "scope": "AUTHOR_PROPOSED_FENTON_CHEMISTRY_WITH_CHEMICAL_AND_MODULATION_SUPPORT",
            "genetic_causality_or_complete_mechanism_established": False,
            "seeded_antiviral_role_replaced": False,
        },
    }


def ground_assay_species(taxon):
    if (
        lineages.identity(taxon)
        != {"taxonId": 1423, "scientificName": "Bacillus subtilis", "rank": "species"}
        or taxon.get("active") is not True
    ):
        raise ValueError("assay species identity changed")
    return {
        "source_species_name": "Bacillus subtilis",
        "taxon_id": "NCBITaxon:1423",
        "rank": "species",
        "source_strain_label": "ATCC 6051",
        "role": "ACTIVITY_ASSAY_ORGANISM_NOT_VERIFIED_RESISTANT_ISOLATE",
        "strain_taxon_id": None,
        "assembly_accession": None,
        "reference_strain_168_or_its_protein_identifiers_assigned": False,
        "species_wide_resistance_inferred": False,
    }


def project_discovery(row):
    if (
        row.get("identifier") != "CHEBI:142135"
        or set(row.get("candidate_ids", [])) != LEADS
        or len(row["candidate_ids"]) != 8
        or len(row.get("queries", [])) != 2
    ):
        raise ValueError("discovery cohort membership changed")
    candidates = None
    for query in row["queries"]:
        entries = query.get("candidates", [])
        mapping = {entry["source"] + ":" + entry["id"]: entry for entry in entries}
        if (
            query.get("hit_count") != 8
            or query.get("next_cursor") is not None
            or query.get("request", {}).get("status") != 200
            or len(entries) != 8
            or set(mapping) != LEADS
            or (candidates is not None and candidates != mapping)
        ):
            raise ValueError("discovery queries incomplete or inconsistent")
        candidates = mapping
    if (
        candidates["MED:34869220"].get("doi") != DOI
        or candidates["MED:34869220"].get("pmcid") != "PMC8632820"
    ):
        raise ValueError("selected primary lead identity changed")
    return {
        "retained_candidate_ids": sorted(LEADS),
        "candidate_count": 8,
        "scoped_primary_text_reviews": 1,
        "remaining_candidates_unreviewed": 7,
        "titles_do_not_prove_exact_compound_or_resistance": True,
        "AGR_MED_same_title_is_not_a_verified_crosswalk_or_independent_replication": True,
        "TA_289_title_lead_is_not_assigned_to_equisetin": True,
        "leads": [
            {
                **candidates[key],
                "review_status": "SCOPED_PRIMARY_TEXT_REVIEW" if key == "MED:34869220" else "UNREVIEWED",
            }
            for key in sorted(LEADS)
        ],
    }


def build(root, directory=CACHE):
    directory = root / directory
    if any(
        {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} != {"article-2021"}
        for suffix in ("-receipt.json", "-attempt.json")
    ):
        raise ValueError("research request coverage changed")
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen research cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    for key in ("census", "protected", "discovery", "source_queue", "snapshot"):
        reference.check_pin(root, cohort[key])
    protected = json.loads(reference.check_pin(root, cohort["protected"]).read_bytes())
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or any(protected.get(r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("complete corpus preflight changed")
    record = load_record(reference.check_pin(root, cohort["snapshot"]))
    if (
        record["identifier"] != cohort["identifier"]
        or record["identifier"] != "CHEBI:142135"
        or record["chemical_structure"]["standard_inchi_key"] != "QNQBPPQLRODXET-HMHJLHGTSA-N"
        or record.get("resistance_mechanisms")
        or protected.get(cohort["record"]["path"]) != cohort["record"]["sha256"]
        or cohort["snapshot"]["sha256"] != cohort["record"]["sha256"]
    ):
        raise ValueError("historical exact-structure record changed")
    discovery = json.loads(gzip.decompress(reference.check_pin(root, cohort["discovery"]).read_bytes()))
    matching = [r for r in discovery["records"] if r["identifier"] == record["identifier"]]
    if matching != [cohort["discovery_record"]] or matching[0]["sha256"] != cohort["record"]["sha256"]:
        raise ValueError("discovery record provenance changed")
    source = planned_source(root, directory, "article-2021", "request-plan.json", ARTICLE)
    primary = primary_context(reference.check_pin(root, source["body"]).read_bytes())
    previous_path = root / "research/2026-10-14-streptothricin-context.json"
    if reference.digest(previous_path) != protected[str(previous_path.relative_to(root))]:
        raise ValueError("taxonomy source checkpoint changed")
    previous = json.loads(previous_path.read_bytes())
    taxon, tax_source = lineages.native_taxon(
        root, previous["reference_taxonomy_sources"]["1423"], "1423", "2026_03"
    )
    return {
        "date": "2026-10-14",
        "scope": "EXACT_COMPOUND_LEAD_ASSESSMENT_NOT_RESISTANT_ALLELE_CURATION",
        "cohort": reference.pin(root, cohort_path),
        "baseline_commit": cohort["baseline_commit"],
        "census": cohort["census"],
        "corpus_records_hash_checked_at_preflight": len(census),
        "record": {
            "identifier": record["identifier"],
            "label": record["label"],
            "standard_inchi_key": cohort["standard_inchi_key"],
            **cohort["record"],
            "historical_snapshot": cohort["snapshot"],
        },
        "discovery": project_discovery(matching[0]),
        "primary_source": source,
        "primary_context": primary,
        "assay_species": ground_assay_species(taxon),
        "taxonomy_source": tax_source,
        "taxonomy_source_checkpoint": reference.pin(root, previous_path),
        "curation_decision": "NO_RESISTANCE_ASSERTION_OR_EXPERIMENTAL_PROTEIN_GENOME_ASSIGNMENT",
        "limits": {
            "scientific_http_attempts": 1,
            "native_taxonomy_responses_reused": 1,
            "new_uniprot_requests": 0,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "retries": 0,
            "automatic_redirects": 0,
            "prior_source_holds_preserved": True,
            "biological_records_changed": 0,
            "numeric_AST_variants_sequences_constructs_or_protocols_exported": False,
            "issue_1040": "DEFERRED",
            "source_adoptions": 0,
            "reuse_terms_review_resumed": False,
            "whole_record_primary_review": "OPEN",
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": [
            {
                "source": "Ding et al. 2021, Frontiers in Chemistry",
                "doi": "DOI:" + DOI,
                "license": "CC BY 4.0",
            },
            {"source": "UniProt Consortium", "license": "CC BY 4.0", "release": "2026_03"},
            {"source": "Europe PMC", "scope": "previously captured bibliographic discovery metadata"},
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != payload:
            raise SystemExit("Equisetin checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {
                "scoped_primary_text_reviews": 1,
                "species_grounded": 1,
                "new_resistance_assertions": 0,
                "other_candidates_unreviewed": 7,
            }
        )
    )


if __name__ == "__main__":
    main()
