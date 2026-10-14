"""Verify reference context without equating consensus, isolate or patient alleles."""

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

import audit_caspofungin_context as native_context
import audit_hivdb_grounding as historical
import audit_topoisomerase_references as reference
from lxml import html

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-13-hivdb-reference-identity")
OUTPUT = Path("research/2026-10-13-hivdb-reference-identity.json")
PRODUCTS = {"PR": "Protease", "RT": "Reverse transcriptase/ribonuclease H", "IN": "Integrase"}
FAQ_SHA = "279a7643f52db8d86de0ddb84b098d6117230fc515e72d799e082c841912bea2"
SCOPE = "REFERENCE_CONTEXT_NOT_ALGORITHM_EQUIVALENCE_OR_PATIENT_ALLELES"


def source_regions(genes):
    """Only the three regions used by the adopted inventory belong to this audit."""
    result = {}
    for key in sorted(PRODUCTS):
        gene = genes.get(key, {})
        if (
            gene.get("abstractGene") != key
            or gene.get("name") != "HIV1" + key
            or gene.get("strain") != "HIV1"
            or not isinstance(gene.get("refSequence"), str)
            or not gene["refSequence"]
        ):
            raise ValueError("selected source reference region missing or malformed")
        result[key] = {
            "source_name": gene["name"],
            "abstract_gene": key,
            "source_strain_label": gene["strain"],
            "reference_length": len(gene["refSequence"]),
            "reference_sha256": hashlib.sha256(gene["refSequence"].encode()).hexdigest(),
        }
    return result


def faq_context(payload):
    if hashlib.sha256(payload).hexdigest() != FAQ_SHA:
        raise ValueError("reviewed FAQ content changed")
    tree = html.fromstring(payload)
    prefix = "/html/body/div[1]/div/table/tbody/tr/td/table/tr/td/p"
    locations = {}
    for name, number in (("reference_convention", 7), ("isolate_question", 10), ("isolate_distinction", 11)):
        path = f"{prefix}[{number}]"
        elements = tree.xpath(path)
        if len(elements) != 1:
            raise ValueError("FAQ evidence location changed")
        text = " ".join(elements[0].text_content().split())
        locations[name] = {"xpath": path, "normalized_text_sha256": hashlib.sha256(text.encode()).hexdigest()}
    return {
        "convention": "SUBTYPE_B_CONSENSUS",
        "locations": locations,
        "document_distinguishes_hxb2_from_consensus": True,
        "every_region_proven_sequence_different": False,
        "pinned_algorithm_sequence_equivalence_verified": False,
        "exact_consensus_uniprot_accession": None,
        "interpretation": (
            "Current source documentation uses a subtype-B consensus, not a particular isolate. "
            "Its HXB2 example rejects automatic identity; it does not establish differences in every region."
        ),
    }


def project_reference(entry, taxonomy, parent):
    audit = entry.get("entryAudit", {})
    genes = entry.get("genes", [])
    lineage = taxonomy.get("lineage", [])
    parent_nodes = [n for n in lineage if n.get("taxonId") == 11676]
    species_nodes = [n for n in lineage if n.get("rank") == "species"]
    name = "Human immunodeficiency virus type 1 group M subtype B (isolate HXB2)"
    if (
        entry.get("primaryAccession") != "P04585"
        or entry.get("entryType") != "UniProtKB reviewed (Swiss-Prot)"
        or any(k in entry for k in ("sequence", "features", "comments"))
        or any(type(audit.get(k)) is not int or audit[k] < 1 for k in ("entryVersion", "sequenceVersion"))
        or genes != [{"geneName": {"value": "gag-pol"}}]
        or entry.get("organism", {}).get("taxonId") != 11706
        or entry["organism"].get("scientificName") != name
        or taxonomy.get("taxonId") != 11706
        or taxonomy.get("scientificName") != name
        or taxonomy.get("rank") != "no rank"
        or taxonomy.get("active") is not True
        or parent.get("taxonId") != 11676
        or parent.get("rank") != "no rank"
        or parent.get("active") is not True
        or len(parent_nodes) != 1
        or len(species_nodes) != 1
        or parent_nodes[0]["rank"] != parent["rank"]
        or parent_nodes[0]["scientificName"] != parent["scientificName"]
        or species_nodes[0]["taxonId"] != 3418650
        or species_nodes[0]["scientificName"] != "Lentivirus humimdef1"
        or parent["parent"] != {k: species_nodes[0][k] for k in ("taxonId", "scientificName")}
    ):
        raise ValueError("reference identity, metadata scope, versions or taxonomy changed")
    description = entry["proteinDescription"]
    if description.get("recommendedName", {}).get("fullName", {}).get("value") != "Gag-Pol polyprotein":
        raise ValueError("polyprotein identity changed")
    components = [
        x.get("recommendedName", {}).get("fullName", {}).get("value") for x in description.get("contains", [])
    ]
    if any(components.count(name) != 1 for name in PRODUCTS.values()):
        raise ValueError("named reference products missing or ambiguous")
    return {
        "protein_accession": "UniProtKB:P04585",
        "entry_type": entry["entryType"],
        "entry_version": audit["entryVersion"],
        "sequence_version": audit["sequenceVersion"],
        "gene_name": "gag-pol",
        "protein_name": "Gag-Pol polyprotein",
        "named_products": PRODUCTS,
        "reference_taxon_id": "NCBITaxon:11706",
        "reference_taxon_rank": taxonomy["rank"],
        "reference_organism_name": name,
        "source_context_taxon_id": "NCBITaxon:11676",
        "source_context_taxon_rank": parent["rank"],
        "species_taxon_id": "NCBITaxon:3418650",
        "species_name": species_nodes[0]["scientificName"],
        "role": "COMPARATIVE_ISOLATE_REFERENCE_NOT_HIVDB_CONSENSUS_OR_PATIENT_ALLELE",
        "algorithm_reference_assignment": False,
        "experimental_allele_assignment": None,
        "experimental_genome_assignment": None,
        "resistance_phenotype_asserted": False,
        "region_coordinates_inferred": False,
    }


def build(root, directory):
    plan_path = directory / "native-plan.json"
    plan = json.loads(plan_path.read_bytes())
    cohort = json.loads(reference.check_pin(root, plan["cohort"]).read_bytes())
    for key in (
        "prior_verification",
        "prior_context",
        "census",
        "protected",
        "inventory",
        "manifest",
        "source_queue",
    ):
        reference.check_pin(root, cohort[key])
    prior = json.loads((root / cohort["prior_context"]["path"]).read_bytes())
    if reference.digest(root / historical.INVENTORY) != prior["source_inventory_sha256"]:
        raise ValueError("adopted inventory differs from historical reference audit")
    assets = {}
    for key, name in (
        ("faq-script", "documentation-assets-plan.json"),
        ("faq-router", "router-asset-plan.json"),
        ("faq-legacy", "legacy-asset-plan.json"),
        ("faq-content", "faq-content-plan.json"),
    ):
        path = directory / name
        asset_plan = json.loads(path.read_bytes())
        for value in asset_plan.values():
            if isinstance(value, dict) and set(value) == {"path", "sha256"}:
                reference.check_pin(root, value)
        assets[key] = {
            **native_context.native(root, directory, key, asset_plan["url"]),
            "plan": reference.pin(root, path),
        }
    sources = {
        key: native_context.native(root, directory, key, row["url"]) for key, row in plan["requests"].items()
    }
    sources.update(assets)
    canary_path = directory / "native-canary.json"
    canary = json.loads(canary_path.read_bytes())
    if (
        canary["body"] != sources["faq-content"]["body"]
        or canary["receipt"] != sources["faq-content"]["receipt"]
        or canary["manually_inspected"] is not True
    ):
        raise ValueError("reference-documentation canary changed")
    faq = faq_context(reference.check_pin(root, sources["faq-content"]["body"]).read_bytes())
    for key in ("protein", "taxonomy"):
        receipt = json.loads(reference.check_pin(root, sources[key]["receipt"]).read_bytes())
        headers = {k.lower(): v for k, v in receipt["headers"].items()}
        if headers.get("x-uniprot-release") != "2026_03" or headers.get("link"):
            raise ValueError("reference release or response completeness changed")
        sources[key]["release"] = headers["x-uniprot-release"]
        if key == "protein" and headers.get("x-total-results") != "1":
            raise ValueError("reference accession response not unique")
    proteins = json.loads(reference.check_pin(root, sources["protein"]["body"]).read_bytes())["results"]
    if len(proteins) != 1:
        raise ValueError("reference response is missing or ambiguous")
    taxonomy = json.loads(reference.check_pin(root, sources["taxonomy"]["body"]).read_bytes())
    parent_wrapper = json.loads(reference.check_pin(root, plan["cached_parent_taxonomy"]).read_bytes())
    if (
        parent_wrapper["url"] != "https://rest.uniprot.org/taxonomy/11676"
        or parent_wrapper["status"] != 200
        or hashlib.sha256(parent_wrapper["body"].encode()).hexdigest() != parent_wrapper["sha256"]
    ):
        raise ValueError("cached broader taxonomy provenance changed")
    parent = json.loads(parent_wrapper["body"])
    comparative = project_reference(proteins[0], taxonomy, parent)
    with reference.check_pin(root, cohort["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["path"] for r in census}) != 2939
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        or any(reference.digest(root / r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("current corpus membership or bytes changed")
    prior_records = {r["identifier"]: r for r in prior["records"]}
    records, counts, seen = [], Counter(), []
    for selected in cohort["records"]:
        doc = load_record(reference.check_pin(root, selected))
        old = prior_records[doc["identifier"]]
        rules = doc.get("genotype_resistance_score_rules", [])
        ids = [r["source_rule_id"] for r in rules]
        groups = Counter(r["gene"] for r in rules)
        if (
            doc["identifier"] != selected["identifier"]
            or doc["label"] != selected["label"]
            or doc["chemical_structure"]["standard_inchi_key"] != selected["standard_inchi_key"]
            or ids != selected["source_rule_ids"]
            or ids != old["source_rule_ids"]
            or groups != selected["region_rule_counts"]
            or groups != old["region_rule_counts"]
            or any(r["source"] != "HIVDB_HIVFACTS" for r in rules)
        ):
            raise ValueError("record identity or complete rule membership changed")
        counts.update(groups)
        seen.extend(ids)
        records.append(
            {
                **{k: selected[k] for k in ("identifier", "label", "path", "sha256", "standard_inchi_key")},
                "source_rule_ids": ids,
                "region_rule_counts": dict(groups),
                "current_documented_convention": "SUBTYPE_B_CONSENSUS",
                "comparative_reference": "UniProtKB:P04585",
                "comparative_reference_role": comparative["role"],
                "exact_algorithm_accession": None,
                "experimental_allele_assignment": None,
                "experimental_genome_assignment": None,
                "new_taxon_assignment": None,
                "status": "REFERENCE_CONTEXT_REVIEWED_PRIMARY_RESISTANCE_REVIEW_OPEN",
            }
        )
    if (
        len(records) != 16
        or {r["identifier"] for r in records} != set(prior_records)
        or len(seen) != len(set(seen))
        or len(seen) != 467
        or counts != {"RT": 231, "IN": 192, "PR": 44}
    ):
        raise ValueError("cohort membership or region totals changed")
    # Replay the already-cached source definitions without exposing their sequences.
    previous_cache = historical.common.OUT
    try:
        historical.common.OUT = root / "reports/resistance-grounding-2026-10-07"
        genes, strain, source_requests = historical.source_context()
    finally:
        historical.common.OUT = previous_cache
    regions = source_regions(genes)
    if regions != prior["reference_regions"] or strain != prior["source_strain_definition"]:
        raise ValueError("historical source reference definitions changed")
    return {
        "date": "2026-10-13",
        "retrieval_date_utc": "2026-10-14",
        "scope": SCOPE,
        "inputs": {
            "plan": reference.pin(root, plan_path),
            "cohort": plan["cohort"],
            "canary": reference.pin(root, canary_path),
            "prior_context": cohort["prior_context"],
            "cached_parent_taxonomy": plan["cached_parent_taxonomy"],
        },
        "sources": sources,
        "source_reference_requests_reused": source_requests,
        "source_reference_regions": regions,
        "current_documentation": faq,
        "comparative_reference": comparative,
        "records": records,
        "summary": {
            "corpus_records_hash_verified": 2939,
            "cohort_records": len(records),
            "source_rules": len(seen),
            "region_rule_counts": dict(counts),
            "new_reference_entries_verified": 1,
            "exact_algorithm_accessions_assigned": 0,
            "biological_records_changed": 0,
            "new_resistance_assertions": 0,
            "whole_record_reviews_completed": 0,
            "native_http_requests": len(sources),
        },
        "limitations": [
            "Current FAQ documentation is not a version-pinned proof "
            "of the adopted algorithm's reference bytes.",
            "HXB2 and consensus are not interchangeable by default; "
            "no region-by-region sequence comparison was performed.",
            "PR, RT and IN are source region labels; "
            "named UniProt products do not supply exact algorithm coordinates.",
            "A comparative reference is neither a tested allele nor a patient, isolate, "
            "genome or clinical-resistance assignment.",
            "Interpretation scores remain source rules, not measured phenotype or causal proof.",
            "The score-rule schema has no reference-accession slot; "
            "these findings remain in research, not biological records.",
            "No primary patient-study results or variant-specific evidence were reviewed in this checkpoint.",
        ],
        "attribution": {
            "source": "UniProt Consortium, UniProtKB and UniProt Taxonomy",
            "license": "CC BY 4.0",
        },
        "constraints": {
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "issue_1040": "DEFERRED",
            "github_mutations": 0,
            "source_adoptions": 0,
            "failed_source_retries": 0,
            "javascript_executed": False,
            "new_sequence_downloads": 0,
            "sequences_variants_protocols_exported": False,
            "numeric_ast_exported": False,
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=CACHE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    result = build(root, root / args.cache)
    encoded = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    path = root / args.output
    if path.exists() and path.read_text() != encoded:
        raise ValueError("refusing to overwrite a differing research checkpoint")
    path.write_text(encoded)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
