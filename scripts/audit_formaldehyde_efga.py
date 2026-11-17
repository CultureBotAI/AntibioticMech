"""Replay qualified native EfgA/EfgB evidence without assigning tested alleles."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urljoin, urlsplit

import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import planned_source
from lxml import html

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-formaldehyde-efga")
OUTPUT = Path("research/2026-10-14-formaldehyde-context.json")
RECORD = Path("data/antibiotics/biocide/formaldehyde.yaml")
FIXTURE = Path("tests/fixtures/formaldehyde-before-2026-10-14.yaml")
ARTICLE = "https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001208"
ARTICLE_SHA = "e755e7d471e35a43e67b8de8efe065629df126b3cebfa992cb32500fa512f47a"
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,xref_pdb,sequence_version,version"
)
QUERIES = {
    "efga-reference": ("gene_exact:Mext_4158", "followup-plan.json"),
    "efgb-reference": ("gene_exact:Mext_0606", "followup-plan.json"),
    "efgb-name-reference": ("gene_exact:efgB AND organism_id:419610", "reference-followup-plan.json"),
}
FIGURES = {
    "g003": "33630c4c061023b8a17f6955ddbdf8091829e54d6280b2351c3fe898f4780288",
    "g005": "d78319b5aa1bb23016471ccc60d9d63ddabca5f2b0c764d32f064e15373aeaf0",
    "g009": "77ee2fceaf849f109b6b7fb000d231d49430ea20e70aa803f9d965f2746bc428",
    "g010": "6a7c8b283d8096b031d3047c21e66fdafa960cc3d1b81705bc81176a6f509361",
    "g011": "b666ffb97c3bd61d6750922abac0ebe4635f1ae4383cd6ce4ce594b5552e5365",
    "g012": "75c638563f93c9841f07d9940f1be29348d4dd9f429340acd270653dce1e7923",
    "g013": "b7eb2c59c53e0b38fc75e1a1b48a36f28e241d1051bf82d6f01031be2ab74d87",
}


def primary_context(payload):
    if hashlib.sha256(payload).hexdigest() != ARTICLE_SHA:
        raise ValueError("reviewed primary article changed")
    tree = html.fromstring(payload)
    if tree.xpath('//meta[@name="citation_doi"]/@content') != ["10.1371/journal.pbio.3001208"]:
        raise ValueError("primary DOI changed")
    markers = {
        "native_background": "Thus, the genotype referred to herein",
        "host_backgrounds": "E. coli strains used in the physiological studies",
        "source_loci": "Resequencing the genome of a representative isolate",
        "gene_names": "thus we renamed them efgA and efgB, respectively",
        "efga_functional_comparisons": "In order to understand how efgA is involved",
        "efgb_annotation": "efgB encodes a putative adenylate/guanylate cyclase",
        "efgb_negative_comparison": "Genetic analyses with efgB alleles indicate",
        "efgb_conditional_comparison": "To more clearly elucidate the role of EfgB",
        "endogenous_stress": "Taking advantage of mutants with partial",
        "phenotypic_tolerance": "Given that mutations in efgA impact genetic resistance",
        "heterologous_context": "Heterologous expression of EfgA in E. coli",
        "opposing_contexts": "The efgA-related phenotypes are paradoxical",
        "chemical_derivatives": "Curiously, the additional electron densities",
    }
    locations = {}
    for key, marker in markers.items():
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
        "pmid": "PMID:34038406",
        "doi": "DOI:10.1371/journal.pbio.3001208",
        "locations": locations,
        "source_gene_loci": {"efgA": "Mext_4158", "efgB": "Mext_0606"},
        "native_species": "Methylorubrum extorquens",
        "background": "PA1-derived laboratory strains; study baseline CM2730 is not unmodified PA1",
        "efga": "LOSS_OF_FUNCTION_ASSOCIATED_WITH_EXOGENOUS_FORMALDEHYDE_GROWTH",
        "efgb": "CONDITIONAL_CONTRIBUTION_IN_EFGA_ALTERED_BACKGROUNDS",
        "efgb_alone_sufficient_in_sole_formaldehyde_carbon_comparison": False,
        "efgb_cyclase_activity_experimentally_verified": False,
        "efga_protective_in_endogenous_stress_context": True,
        "phenotypic_heterogeneity_explained_by_efga_genotype_alone": False,
        "heterologous_host": "Escherichia coli",
        "heterologous_claim_curated": False,
        "heterologous_effect_transferred_to_native_background": False,
        "endpoints": ["LABORATORY_GROWTH", "COLONY_FREQUENCY_DISTRIBUTION", "DISK_DIFFUSION"],
        "endpoints_converted_to_MIC": False,
        "clinical_category_inferred": False,
        "numeric_AST_exported": False,
        "supplement_tables_reviewed": False,
        "exact_allele_or_genome_crosswalk_completed": False,
        "crystal_density_identifies_unmodified_formaldehyde_unambiguously": False,
        "whole_record_primary_review": "OPEN",
    }


def species_context(taxonomy):
    if (
        taxonomy["taxonId"] != 408
        or taxonomy["rank"] != "species"
        or taxonomy.get("active") is not True
        or taxonomy["scientificName"] != "Methylorubrum extorquens"
        or "Methylobacterium extorquens" not in taxonomy.get("synonyms", [])
    ):
        raise ValueError("source species identity changed")
    return {
        "taxon_id": "NCBITaxon:408",
        "name": taxonomy["scientificName"],
        "rank": "species",
        "species_wide_resistance_inferred": False,
        "experimental_strain_taxon_assigned": False,
    }


def efga_reference(entry, taxonomy):
    if {"sequence", "features", "comments"}.intersection(entry):
        raise ValueError("unplanned biological payload")
    result = reference.project_reference(entry, "efgA", 408, taxonomy)
    if (
        entry["primaryAccession"] != "P0DX96"
        or entry["organism"]["taxonId"] != 419610
        or taxonomy["rank"] != "strain"
        or taxonomy["scientificName"] != "Methylorubrum extorquens (strain PA1)"
        or taxonomy["scientificName"] != entry["organism"]["scientificName"]
        or result["ordered_locus_names"] != ["Mext_4158"]
        or result["entry_version"] != 8
        or result["sequence_version"] != 1
    ):
        raise ValueError("EfgA reference identity changed")
    result.pop("bibliography")
    return {
        **result,
        "reference_assigned_to_experimental_allele": False,
        "reference_strain_assigned_to_all_tested_derivatives": False,
        "experimental_genome_assignment": None,
    }


def empty_reference(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("results"), list) or payload["results"]:
        raise ValueError("dated empty EfgB result changed")
    return {
        "result_count": 0,
        "suggestions_used": False,
        "scope": "NO_RESULT_IN_THIS_EXACT_DATED_QUERY_NOT_PROTEIN_ABSENCE",
        "protein_accession_assigned": None,
    }


def claims(context):
    required = {
        "record": {"identifier": "CHEBI:16842", "standard_inchi_key": "WSFSSNUMVMOOMR-UHFFFAOYSA-N"},
        "reference_protein": {
            "protein_accession": "UniProtKB:P0DX96",
            "entry_version": 8,
            "sequence_version": 1,
            "entry_type": "UniProtKB reviewed (Swiss-Prot)",
            "gene_names": ["efgA"],
            "ordered_locus_names": ["Mext_4158"],
            "reference_organism_name": "Methylorubrum extorquens (strain PA1)",
            "reference_taxon_id": "NCBITaxon:419610",
            "reference_taxon_rank": "strain",
            "reference_taxon_scientific_name": "Methylorubrum extorquens (strain PA1)",
            "source_species_taxon_id": "NCBITaxon:408",
            "species_lineage_verified": True,
            "experimental_subject_assignment": False,
            "exact_resistance_allele": False,
            "reference_assigned_to_experimental_allele": False,
            "reference_strain_assigned_to_all_tested_derivatives": False,
            "experimental_genome_assignment": None,
        },
        "subject_species": {
            "taxon_id": "NCBITaxon:408",
            "name": "Methylorubrum extorquens",
            "rank": "species",
            "species_wide_resistance_inferred": False,
            "experimental_strain_taxon_assigned": False,
        },
        "primary": {
            "pmid": "PMID:34038406",
            "doi": "DOI:10.1371/journal.pbio.3001208",
            "source_gene_loci": {"efgA": "Mext_4158", "efgB": "Mext_0606"},
            "native_species": "Methylorubrum extorquens",
            "background": "PA1-derived laboratory strains; study baseline CM2730 is not unmodified PA1",
            "heterologous_host": "Escherichia coli",
            "efga": "LOSS_OF_FUNCTION_ASSOCIATED_WITH_EXOGENOUS_FORMALDEHYDE_GROWTH",
            "efgb": "CONDITIONAL_CONTRIBUTION_IN_EFGA_ALTERED_BACKGROUNDS",
            "efgb_alone_sufficient_in_sole_formaldehyde_carbon_comparison": False,
            "efgb_cyclase_activity_experimentally_verified": False,
            "efga_protective_in_endogenous_stress_context": True,
            "heterologous_claim_curated": False,
            "heterologous_effect_transferred_to_native_background": False,
            "endpoints_converted_to_MIC": False,
            "clinical_category_inferred": False,
            "exact_allele_or_genome_crosswalk_completed": False,
            "phenotypic_heterogeneity_explained_by_efga_genotype_alone": False,
        },
    }
    try:
        valid = all(
            type(context[group][key]) is type(value) and context[group][key] == value
            for group, fields in required.items()
            for key, value in fields.items()
        ) and all(
            context["efgb_queries"][key] == empty_reference({"results": []})
            for key in ("efgb-reference", "efgb-name-reference")
        )
    except (KeyError, TypeError):
        valid = False
    if not valid:
        raise ValueError("curation context identity or evidence scope changed")
    shared = {
        "taxon_id": "NCBITaxon:408",
        "taxon_label": "Methylorubrum extorquens",
        "phenotype_label": "Source-reported relative formaldehyde resistance in laboratory growth assays",
        "assay": "Comparative laboratory growth assays",
    }
    return [
        {
            **shared,
            "mechanism_type": "OTHER",
            "label": "Context-dependent EfgA-associated formaldehyde resistance",
            "gene_families": ["EfgA"],
            "gene_id": "Mext_4158",
            "note": "Native PA1-derived laboratory comparisons link loss of EfgA function to growth with "
            "externally supplied formaldehyde. This is not universal protection: EfgA was beneficial "
            "under endogenous formaldehyde stress. The study baseline CM2730 is already a laboratory "
            "derivative, not unmodified PA1. Reference-only UniProtKB:P0DX96 does not identify the "
            "tested alleles. Growth and translation responses are not MIC or clinical resistance categories; "
            "phenotypic heterogeneity remains distinct from this genotype association.",
            "evidence": [
                {
                    "reference": "PMID:34038406",
                    "notes": "DOI:10.1371/journal.pbio.3001208. Native functional "
                    "comparisons in Results and Figure 3; endogenous-stress and tolerance "
                    "limits in Figures 9-10; "
                    "Figure 13 and Discussion. Qualitative gene-level scope; no exact allele or genome "
                    "assignment.",
                },
                {
                    "reference": "UniProtKB:P0DX96",
                    "notes": "Reference identity only: efgA / Mext_4158; reviewed "
                    "UniProtKB 2026_03, entry 8, sequence 1. PA1 NCBITaxon:419610 is "
                    "reference context, not a "
                    "tested-derivative TaxID. Species NCBITaxon:408 independently checked through "
                    "UniProt taxonomy.",
                },
            ],
        },
        {
            **shared,
            "mechanism_type": "UNKNOWN",
            "label": "Conditional EfgB-associated formaldehyde resistance",
            "gene_families": ["EfgB"],
            "gene_id": "Mext_0606",
            "note": "The primary study supports a conditional EfgB contribution in EfgA-altered PA1-derived "
            "laboratory backgrounds; EfgB changes alone did not confer growth in the "
            "sole-formaldehyde-carbon comparison. The adenylate/guanylate cyclase annotation is "
            "putative, not demonstrated biochemical activity. Two dated UniProt queries returned no "
            "reference "
            "candidate; this is not evidence that the gene or protein is absent. No MIC, clinical "
            "category, exact allele, protein accession or experimental genome is assigned.",
            "evidence": [
                {
                    "reference": "PMID:34038406",
                    "notes": "DOI:10.1371/journal.pbio.3001208. Results, EfgB plays "
                    "a secondary role in formaldehyde resistance; negative comparison "
                    "in Figure 3 and conditional "
                    "comparison in Figure 5. Supplement-only claims are not curated.",
                },
                {
                    "reference": "NCBITaxon:408",
                    "notes": "Species identity checked through UniProt taxonomy "
                    "on 2026-10-14, release 2026_03. The PA1 reference lineage does not resolve the tested "
                    "laboratory derivatives as a single strain or genome.",
                },
            ],
        },
    ]


def build(root, directory=CACHE):
    directory = root / directory
    cohort = json.loads((directory / "cohort.json").read_bytes())
    for key in ("baseline", "protected", "census", "source_queue", "previous_checkpoint", "discovery_cache"):
        reference.check_pin(root, cohort[key])
    record = load_record(reference.check_pin(root, cohort["baseline"]))
    if (
        (record["identifier"], record["chemical_structure"]["standard_inchi_key"])
        != ("CHEBI:16842", "WSFSSNUMVMOOMR-UHFFFAOYSA-N")
        or cohort["record"]["identifier"] != record["identifier"]
        or cohort["record"]["standard_inchi_key"] != record["chemical_structure"]["standard_inchi_key"]
        or cohort["record"]["sha256"] != cohort["baseline"]["sha256"]
        or record.get("resistance_mechanisms")
        or record.get("activity_spectrum")
    ):
        raise ValueError("dated compound identity or baseline changed")
    with reference.check_pin(root, cohort["census"]).open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    members = [r for r in rows if r["identifier"] == record["identifier"]]
    if (
        len(rows) != 2939
        or len({r["identifier"] for r in rows}) != 2939
        or len(members) != 1
        or any(members[0][k] != cohort["record"][k] for k in ("path", "standard_inchi_key"))
        or members[0]["record_sha256"] != cohort["record"]["sha256"]
    ):
        raise ValueError("dated census membership changed")
    sources = {"article": planned_source(root, directory, "article", "request-plan.json", ARTICLE)}
    payload = reference.check_pin(root, sources["article"]["body"]).read_bytes()
    primary = primary_context(payload)
    tree = html.fromstring(payload)
    assessment = json.loads((directory / "reviewed-assets.json").read_bytes())
    if assessment != {
        "figures": {k: {"sha256": v, "visually_inspected": True} for k, v in FIGURES.items()},
        "numeric_values_or_constructs_exported": False,
    }:
        raise ValueError("native figure inspection scope changed")
    for key, digest in FIGURES.items():
        links = {
            urljoin(ARTICLE, url)
            for url in tree.xpath("//a/@href")
            if "download&size=large" in url and url.endswith("3001208." + key)
        }
        if len(links) != 1:
            raise ValueError("native figure link absent or ambiguous")
        sources[key] = planned_source(root, directory, key, "followup-plan.json", links.pop(), (302,))
        receipt = json.loads(reference.check_pin(root, sources[key]["receipt"]).read_bytes())
        url = {k.lower(): v for k, v in receipt["headers"].items()}["location"]
        parsed = urlsplit(url)
        if (parsed.scheme, parsed.netloc, parsed.path) != (
            "https",
            "storage.googleapis.com",
            f"/plos-corpus-prod/10.1371/journal.pbio.3001208/1/pbio.3001208.{key}.PNG_L",
        ):
            raise ValueError("native figure asset identity changed")
        source = planned_source(root, directory, key + "-storage", "asset-" + key + "-plan.json", url)
        if source["body"]["sha256"] != digest:
            raise ValueError("reviewed figure changed")
        sources[key + "-storage"] = source
    data = {}
    for key, (query, plan) in QUERIES.items():
        data[key], source = reference.read_response(
            root,
            directory,
            key,
            "/uniprotkb/search",
            {"query": [query], "format": ["json"], "size": ["500"], "fields": [FIELDS]},
        )
        if source["release"] != "2026_03":
            raise ValueError("reference release changed")
        sources[key] = {**source, "request": planned_source(root, directory, key, plan, source["url"])}
    for key, plan in (("tax-419610", "reference-followup-plan.json"), ("tax-408", "species-plan.json")):
        data[key], source = reference.read_response(
            root, directory, key, "/taxonomy/" + key.removeprefix("tax-")
        )
        if source["release"] != "2026_03":
            raise ValueError("taxonomy release changed")
        sources[key] = {**source, "request": planned_source(root, directory, key, plan, source["url"])}
    if len(data["efga-reference"]["results"]) != 1:
        raise ValueError("EfgA reference absent or ambiguous")
    return {
        "date": "2026-10-14",
        "scope": "QUALIFIED_NATIVE_GENE_EVIDENCE_NOT_EXACT_ALLELE_OR_GENOME_GROUNDING",
        "cohort": reference.pin(root, directory / "cohort.json"),
        "record": cohort["record"],
        "inputs": {
            k: cohort[k]
            for k in ("baseline", "census", "source_queue", "previous_checkpoint", "discovery_cache")
        },
        "sources": sources,
        "primary": primary,
        "reviewed_assets": reference.pin(root, directory / "reviewed-assets.json"),
        "reference_protein": efga_reference(data["efga-reference"]["results"][0], data["tax-419610"]),
        "subject_species": species_context(data["tax-408"]),
        "efgb_queries": {k: empty_reference(data[k]) for k in ("efgb-reference", "efgb-name-reference")},
        "curation_decision": "TWO_QUALIFIED_NATIVE_GENE_CLAIMS_WITH_CONTEXT_LIMITS",
        "limits": {
            "scientific_http_attempts": 20,
            "new_requests_this_continuation": 2,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "source_adoptions": 0,
            "github_mutations": 0,
            "experimental_alleles_or_genomes_assigned": 0,
            "numeric_AST_exported": False,
            "sequences_variants_constructs_or_protocols_exported": False,
            "whole_record_primary_signoffs": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": [
            {
                "source": "Bazurto et al. (2021), PLOS Biology",
                "license": "CC BY",
                "url": ARTICLE,
                "transformation": "Qualitative scope summary and evidence-location hashes",
            },
            {
                "source": "UniProt Consortium",
                "license": "CC BY 4.0",
                "release": "2026_03",
                "url": "https://www.uniprot.org/help/license",
            },
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
            raise SystemExit("formaldehyde evidence checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(body)
    print(
        json.dumps(
            {
                "reference": result["reference_protein"]["protein_accession"],
                "taxon": result["subject_species"]["taxon_id"],
                "qualified_claims": len(claims(result)),
            }
        )
    )


if __name__ == "__main__":
    main()
