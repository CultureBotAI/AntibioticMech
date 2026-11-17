"""Replay yeast sensitivity evidence without promoting it to resistant alleles."""

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

CACHE = Path("reports/resistance-grounding-2026-10-14-eugenol")
OUTPUT = Path("research/2026-10-14-eugenol-context.json")
ARTICLE = "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0076028"
ARTICLE_SHA = "9d0c074c81821b711a8d8ab254e3311cd47b1dd0ade5824a9d2a0b415ffd692e"
ASSETS = {
    "figure1": ("g001", "b7e4cc4a41416b3297814d6103024ad0ac16257c554665ba9a1348cd76866f37"),
    "figure2": ("g002", "a8e98c1ff557917958b98581b4cbdcc953ef1f7c541cbbe4286d9097ac5250e4"),
    "figure3": ("g003", "3c0f848b620d9b61427b8c1d85a8ddacb453ef561cf69b631156c96ffec7cd3a"),
    "figure4": ("g004", "e7a849b82febcc097271bdce124c841687c87b3f16ddee83ffba481de6d12f03"),
    "table1": ("t001", "a09048fb5dbe8a3c935913ca0b29ad8a03cdb2028957e3c6733b6172e0cb87da"),
}
TABLE_GENES = {
    "ARO1": "YDR127W", "ARO2": "YGL148W", "ARO7": "YPR060C", "TRP1": "YDR007W", "ILV1": "YER086W",
    "BAP2": "YBR068C", "AGP3": "YFL055W", "SLM4": "YBR077C", "SPF1": "YEL031W", "WSC4": "YHL028W",
    "BUB3": "YOR026W", "TOF1": "YNL273W", "KEM1": "YGL173C", "ISW1": "YBR245C", "SNF6": "YHL025W",
    "SSN3": "YPL042C", "SSF2": "YDR312W", "ERG2": "YMR202W", "YDR442W": "YDR442W",
    "YMR326C": "YMR326C", "VPS69": "YPR087W",
}
FIGURE3 = [
    "ARO4", "ARO1", "ARO2", "ARO7", "PHA2", "TYR1", "ARO8", "ARO9",
    "TRP1", "TRP2", "TRP3", "TRP4", "TRP5", "ILV1", "ILV6", "BAT2",
]
FIGURE4 = ["BAP2", "GAP1", "TAT1", "TAT2"]
GENES = set(TABLE_GENES) | set(FIGURE3) | set(FIGURE4)
HELD = {"YDR442W", "YMR326C"}
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_sgd,lit_pubmed_id,sequence_version,version"
)
REFERENCE_SHA = {
    "reference-canary": "128d2d7419ceeb3aec7e7dd8c06455d98160537e6e3e894a45843f43780e8091",
    "reference-cohort": "d072ccc4512e337797eeb9567d386bad1f3eecaab413c36fa54310009f2b2aeb",
}
TAXONOMY = Path("reports/resistance-grounding-2026-10-13-tavaborole")
TAXONOMY_SHA = "9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810"
REUSE = Path("reports/resistance-grounding-2026-10-13-ionophore-yeast")


def project_gene(entry, gene, taxonomy):
    if gene not in GENES - HELD or {"sequence", "features", "comments"}.intersection(entry):
        raise ValueError("unplanned or held gene, or unexpected biological payload")
    result = reference.project_reference(entry, gene, 4932, taxonomy)
    blocks = entry.get("genes", [])
    links = [x for x in entry.get("uniProtKBCrossReferences", []) if x.get("database") == "SGD"]
    species = [x for x in taxonomy["lineage"] if x.get("rank") == "species"]
    if (
        len(blocks) != 1 or not blocks[0].get("geneName", {}).get("value")
        or len(result["ordered_locus_names"]) != 1
        or (gene in TABLE_GENES and result["ordered_locus_names"] != [TABLE_GENES[gene]])
        or len(links) != 1 or not links[0].get("id")
        or entry["organism"]["taxonId"] != 559292 or taxonomy["rank"] != "strain"
        or taxonomy["scientificName"] != "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)"
        or entry["organism"]["scientificName"] != taxonomy["scientificName"]
        or len(species) != 1 or species[0].get("scientificName") != "Saccharomyces cerevisiae"
    ):
        raise ValueError("source gene/locus or reference taxonomy mismatch")
    result.pop("bibliography")
    return {
        **result, "source_symbol": gene, "canonical_gene": blocks[0]["geneName"]["value"],
        "sgd_id": "SGD:" + links[0]["id"], "role": "REFERENCE_ONLY_NOT_TESTED_ALLELE_OR_GENOME",
        "resistance_inferred_from_reference": False,
    }


def evidence_roles(gene):
    if gene not in GENES:
        raise ValueError("gene absent from inspected primary panels")
    roles = []
    if gene in TABLE_GENES:
        roles.append({"location": "Table 1", "evidence": "SENSITIVITY_SCREEN_HIT_NOT_RESISTANCE"})
    if gene in FIGURE3:
        roles.append({"location": "Figure 3", "evidence": "AUXOTROPH_COMPARISON_CONTEXT"})
    if gene in FIGURE4:
        roles.append({
            "location": "Figure 4", "background_gene_context": "ARO1",
            "evidence": "CONDITIONAL_PARTIAL_GROWTH_RESCUE" if gene in {"GAP1", "TAT1"}
            else "NO_SIGNIFICANT_RESCUE_REPORTED",
        })
    return roles


def primary_context(payload):
    if hashlib.sha256(payload).hexdigest() != ARTICLE_SHA:
        raise ValueError("reviewed article changed")
    tree = html.fromstring(payload)
    if tree.xpath('//meta[@name="citation_doi"]/@content') != ["10.1371/journal.pone.0076028"]:
        raise ValueError("primary DOI changed")
    locations = {}
    for name, marker in (
        ("chemical_identity", "G418 and eugenol were purchased from Sigma-Aldrich"),
        ("baseline_subject", "S. cerevisiae (S288C) was used in antifungal activity assays."),
        ("library_scope", "For high throughput phenotypic screenings"),
        ("auxotrophy_limit", "This putative interference with amino acid uptake"),
        ("suppression_comparisons", "To further test whether eugenol interferes"),
        ("direct_binding_limit", "Further investigations should be carried out to test whether or not"),
    ):
        matches = [p for p in tree.xpath('//div[@id="artText"]//p')
                   if marker in " ".join(p.text_content().split())]
        if len(matches) != 1:
            raise ValueError("primary evidence location missing or ambiguous")
        text = " ".join(matches[0].text_content().split())
        locations[name] = {"xpath": tree.getroottree().getpath(matches[0]),
                           "normalized_text_sha256": hashlib.sha256(text.encode()).hexdigest()}
    return {
        "doi": "DOI:10.1371/journal.pone.0076028", "pmid": "PMID:24204588", "locations": locations,
        "chemical_scope": "NAMED_EUGENOL_NOT_CLOVE_OIL_OR_RELATED_PHENYLPROPANOIDS",
        "baseline_subject_label": "S288C", "library_background_label": "BY4741",
        "background_is_unique_tested_derivative": False,
        "baseline_MIC_reported": True, "baseline_MIC_is_resistant_genotype_endpoint": False,
        "screen_direction": "INCREASED_SENSITIVITY", "screen_is_exhaustive_resistance_catalog": False,
        "multidrug_resistance_deletions_excluded_from_source_hit_list": True,
        "figure1_followup_spot_comparisons": 8,
        "figure2_scope": "MODEL_MEMBRANE_AND_TRANSLATION_REPORTER_NOT_DIRECT_PERMEASE_BINDING",
        "figure3_scope": "AUXOTROPHY_AND_MEDIUM_DEPENDENT_COMPARISONS",
        "figure4_scope": "PARTIAL_GROWTH_RESCUE_IN_SENSITIZED_BACKGROUND_NOT_CLINICAL_RESISTANCE",
        "direct_binding_demonstrated": False, "complete_mode_of_action_resolved": False,
        "new_resistance_curation_supported_by_this_checkpoint": False,
        "experimental_allele_assignment": None, "experimental_genome_assignment": None,
        "numeric_AST_exported": False,
    }


def build(root, directory):
    def read(path):
        return json.loads(path.read_bytes())

    cohort = read(directory / "cohort.json")
    for key in ("census", "discovery", "protected", "previous_checkpoint"):
        reference.check_pin(root, cohort[key])
    baseline = directory / "baseline-record.yaml"
    if reference.digest(baseline) != cohort["record"]["sha256"]:
        raise ValueError("historical baseline changed")
    record = load_record(baseline)
    if (record["identifier"], record["chemical_structure"]["standard_inchi_key"]) != (
        "CHEBI:4917", "RRAFCDWBNXTKKO-UHFFFAOYSA-N",
    ) or record.get("resistance_mechanisms"):
        raise ValueError("historical compound identity or claim state changed")
    with (root / cohort["census"]["path"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if len(census) != 2939 or len({row["identifier"] for row in census}) != 2939:
        raise ValueError("corpus membership changed")
    sources = {"article": native_context.native(root, directory, "article", ARTICLE)}
    article = reference.check_pin(root, sources["article"]["body"])
    context = primary_context(article.read_bytes())
    tree = html.fromstring(article.read_bytes())
    assessment = read(directory / "reviewed-assets.json")
    if (
        assessment["all_five_native_images_visually_inspected"] is not True
        or assessment["table1_gene_locus_columns_manually_transcribed"] != TABLE_GENES
        or assessment["figure3_labels"] != FIGURE3 or assessment["figure4_labels"] != FIGURE4
    ):
        raise ValueError("inspected source-panel coverage changed")
    for key, (suffix, checksum) in ASSETS.items():
        links = {urljoin(ARTICLE, a.get("href")) for a in tree.xpath('//a[@href]')
                 if "download&size=large" in a.get("href") and a.get("href").endswith("0076028." + suffix)}
        if len(links) != 1:
            raise ValueError("native asset link missing or ambiguous")
        sources[key] = native_context.native(root, directory, key, links.pop(), statuses=(302,))
        receipt = read(reference.check_pin(root, sources[key]["receipt"]))
        url = {k.lower(): v for k, v in receipt["headers"].items()}["location"]
        parsed = urlsplit(url)
        if (parsed.scheme, parsed.netloc, parsed.path) != (
            "https", "storage.googleapis.com",
            "/plos-corpus-prod/10.1371/journal.pone.0076028/1/pone.0076028." + suffix + ".PNG_L",
        ):
            raise ValueError("unrecognized native storage redirect")
        sources[key + "-storage"] = native_context.native(root, directory, key + "-storage", url)
        body = sources[key + "-storage"]["body"]
        if body["sha256"] != checksum or body != assessment["assets"][key]:
            raise ValueError("visually inspected asset changed")
    taxonomy, sources["taxonomy-reused"] = reference.read_response(
        root, root / TAXONOMY, "tax-559292", "/taxonomy/559292")
    if sources["taxonomy-reused"]["cache"]["sha256"] != TAXONOMY_SHA:
        raise ValueError("cached taxonomy changed")
    requested = GENES - HELD - {"ERG2"}
    queries = {
        "reference-canary": "gene_exact:ARO1 AND organism_id:559292 AND reviewed:true",
        "reference-cohort": "(" + " OR ".join("gene_exact:" + g for g in sorted(requested - {"ARO1"}))
        + ") AND organism_id:559292 AND reviewed:true",
    }
    proteins = {}
    for key, query in queries.items():
        payload, sources[key] = reference.read_response(root, directory, key, "/uniprotkb/search", {
            "query": [query], "fields": [FIELDS], "format": ["json"], "size": ["100"],
        })
        if sources[key]["release"] != "2026_03" or sources[key]["cache"]["sha256"] != REFERENCE_SHA[key]:
            raise ValueError("reviewed reference response or release changed")
        for entry in payload["results"]:
            names = {b["geneName"]["value"] for b in entry["genes"] if b.get("geneName")}
            names.update(x["value"] for b in entry["genes"] for x in b.get("synonyms", []))
            matches = requested.intersection(names)
            if len(matches) != 1 or matches.intersection(proteins):
                raise ValueError("reference gene match absent, ambiguous or duplicated")
            gene = matches.pop()
            proteins[gene] = project_gene(entry, gene, taxonomy)
        sources[key + "-request"] = native_context.native(root, directory, key, sources[key]["url"])
    if set(proteins) != requested or len({p["protein_accession"] for p in proteins.values()}) != 32:
        raise ValueError("reference cohort incomplete or ambiguous")
    old_plan = read(root / REUSE / "reference-plan.json")
    overlap = {g for g, locus in TABLE_GENES.items() if locus in old_plan["source_loci"]}
    if overlap != HELD | {"ERG2"}:
        raise ValueError("prior query overlap changed")
    hold = native_context.native(
        root, root / REUSE, "reference-cohort", old_plan["requests"]["reference-cohort"]["url"],
        statuses=(400,),
    )
    error = read(reference.check_pin(root, hold["body"]))
    if error.get("messages") != ["Too many OR conditions in query. Maximum allowed is 100."]:
        raise ValueError("prior query hold reason changed")
    old_fields = FIELDS.replace("lit_pubmed_id,", "")
    old, sources["erg2-reused"] = reference.read_response(
        root, root / REUSE, "reference-canary", "/uniprotkb/search", {
            "query": ["organism_id:559292 AND (gene_exact:YMR202W)"],
            "fields": [old_fields], "format": ["json"], "size": ["500"],
        })
    if len(old["results"]) != 1 or sources["erg2-reused"]["release"] != "2026_03":
        raise ValueError("reused ERG2 reference ambiguous or release changed")
    proteins["ERG2"] = project_gene(old["results"][0], "ERG2", taxonomy)
    if (
        proteins["ERG2"]["protein_accession"] != "UniProtKB:P32352"
        or proteins["ERG2"]["entry_version"] != 175 or proteins["ERG2"]["sequence_version"] != 1
    ):
        raise ValueError("cached ERG2 accession or version changed")
    return {
        "cohort": reference.pin(root, directory / "cohort.json"), "record": cohort["record"],
        "sources": sources, "primary": context, "references": proteins,
        "genes": [{"source_symbol": gene, "source_locus": TABLE_GENES.get(gene),
                   "evidence_roles": evidence_roles(gene),
                   "reference_status": "VERIFIED_REFERENCE_ONLY" if gene in proteins
                   else "UNCOMPLETED_PRIOR_QUERY_HOLD_NOT_NEGATIVE_SEARCH",
                   "reference_accession": proteins.get(gene, {}).get("protein_accession"),
                   "experimental_allele_assignment": None, "resistance_category_inferred": False}
                  for gene in sorted(GENES)],
        "prior_query_hold": {
            "plan": reference.pin(root, root / REUSE / "reference-plan.json"),
            "receipt": reference.pin(root, root / REUSE / "reference-cohort-receipt.json"),
            "overlapping_uncompleted_genes": sorted(HELD), "retried_or_split": False,
        },
        "summary": {"corpus_records_in_scope": 2939, "records_in_this_checkpoint": 1,
                    "source_gene_labels": 35, "table1_sensitivity_hits": 21,
                    "verified_reference_proteins": 33, "new_reference_proteins": 32,
                    "reused_reference_proteins": 1, "uncompleted_reference_mappings": 2,
                    "native_assets_visually_inspected": 5, "curated_resistance_assertions": 0,
                    "whole_record_primary_signoffs": 0},
        "limits": {"ncbi_requests": 0, "new_taxonomy_requests": 0, "issue_1040": "DEFERRED",
                   "source_adoption": False, "whole_record_primary_review": "OPEN",
                   "sequences_exported": False, "variants_exported": False, "numeric_AST_exported": False,
                   "clinical_category_inferred": False, "independent_scientific_signoff": False},
        "attribution": {"primary": "Darvishi et al. 2013, PLOS ONE, Creative Commons Attribution",
                        "reference": "UniProt Consortium, release 2026_03, CC BY 4.0"},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=CACHE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    result = build(Path.cwd(), Path.cwd() / args.cache)
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.output.exists() and args.output.read_bytes() != payload:
        raise ValueError("refusing to overwrite historical checkpoint")
    args.output.write_bytes(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
