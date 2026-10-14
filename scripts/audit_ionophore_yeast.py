"""Audit qualitative ionophore evidence without assigning experimental alleles.

Offline replay reads a pinned, read-only xlrd extraction of the publisher XLS.
The full workbook remains private; only identifiers and categorical findings are
projected. Hidden comparison sheets are accounted for, not additional subjects.
"""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

import audit_caspofungin_context as native_context
import audit_topoisomerase_references as reference
from lxml import html
from resistance_checkpoint_records import checkpoint_path

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-13-ionophore-yeast")
OUTPUT = Path("research/2026-10-13-ionophore-yeast.json")
SCOPE = "QUALITATIVE_YEAST_SCREEN_AND_REFERENCE_CONTEXT_NOT_EXACT_ALLELES"
ARTICLE_SHA = "fd7492d7eed0f84df88511fbfa5995a1fedadc680e3e6c254c3c0eae74f46be2"
WORKBOOK_SHA = "94defdc4cdc4e74833981ace5672ce19d5cb890e14d90f96987cc8f26e410a9a"
FIGURE_SHA = "12d5bccd7845d58fdc863cd674c0210bd64a437d66f6f7b7f04f7f40da89dd7a"
CATEGORIES = {
    "Nig hypersensitive": (None, "HYPERSENSITIVE"),
    "Nig resistant": (None, "RESISTANT"),
    "Val and Nig hypersensitive": ("HYPERSENSITIVE", "HYPERSENSITIVE"),
    "Val and Nig resistant": ("RESISTANT", "RESISTANT"),
    "Val hypersensitive": ("HYPERSENSITIVE", None),
    "Val resistant": ("RESISTANT", None),
}
COUNTS = {
    "Nig hypersensitive": 14,
    "Nig resistant": 6,
    "Val and Nig hypersensitive": 15,
    "Val and Nig resistant": 8,
    "Val hypersensitive": 20,
    "Val resistant": 64,
}
# Visually transcribed from the lower table of S3 Figure, not inferred from spots.
FIGURE = {
    "ERG24": (["LETHAL"] * 3, "Val and Nig resistant", "LETHAL"),
    "ERG28": (["Val resistant"] * 3, "Nig resistant", "Val resistant"),
    "ERG6": (["Val and Nig resistant"] * 3, "Val and Nig resistant", "Val resistant"),
    "ERG2": (["Val resistant"] * 3, "Val resistant", "RESPIRATION_DEFICIENT"),
    "ERG3": (["Val and Nig hypersensitive"] * 3, "Val and Nig hypersensitive", "RESPIRATION_DEFICIENT"),
    "ERG5": (["NOT_DONE"] * 3, "Val resistant", "Val resistant"),
    "ERG4": (["Nig resistant"] * 3, "Nig resistant", "Val hypersensitive"),
}


def project_rows(values):
    if len(values) != 133 or any(len(row) != 10 for row in values):
        raise ValueError("source worksheet dimensions changed")
    if values[1][:3] != ["ORF", "standard name", "phenotype of the deletant on Val/Nig"]:
        raise ValueError("source worksheet headers changed")
    if any(any(row[:3]) for row in values[129:]):
        raise ValueError("unaccounted trailing source subjects")
    result, seen = [], set()
    for number, row in enumerate(values[2:129], 3):
        locus, symbol, category = row[:3]
        if not isinstance(locus, str) or not re.fullmatch(r"Y[A-P][LR]\d{3}[CW](?:-[A-Z])?", locus):
            raise ValueError("malformed source locus")
        if locus in seen or not isinstance(symbol, str) or not symbol:
            raise ValueError("duplicate locus or missing source symbol")
        if category not in CATEGORIES or row[7] not in ("", "*"):
            raise ValueError("unknown source category or stability marker")
        seen.add(locus)
        val, nig = CATEGORIES[category]
        result.append(
            {
                "source_excel_row": number,
                "source_locus": locus,
                "source_gene_label": None if symbol == "-" else symbol,
                "source_category": category,
                "valinomycin_label": val,
                "nigericin_label": nig,
                "source_stable_marker": row[7] == "*",
                "source_dubious_orf": "dubious" in row[5].lower(),
                "evidence_type": "QUALITATIVE_LIBRARY_SCREEN_ASSOCIATION",
                "experimental_allele_accession": None,
                "experimental_genome_accession": None,
                "reference_accessions": [],
                "reference_status": "NOT_COMPLETED_QUERY_LIMIT_HOLD",
            }
        )
    if Counter(r["source_category"] for r in result) != COUNTS:
        raise ValueError("final source categories do not reconcile")
    if (
        sum(r["source_stable_marker"] for r in result) != 61
        or sum(r["source_dubious_orf"] for r in result) != 15
    ):
        raise ValueError("source stability or dubious-ORF counts changed")
    return result


def project_reference(entry, taxonomy):
    if set(entry).intersection({"sequence", "features", "comments"}):
        raise ValueError("reference contains unrequested biological payload")
    audit = entry.get("entryAudit", {})
    genes = entry.get("genes", [])
    species = [x for x in taxonomy.get("lineage", []) if x.get("rank") == "species"]
    if (
        entry.get("primaryAccession") != "P32352"
        or entry.get("entryType") != "UniProtKB reviewed (Swiss-Prot)"
        or len(genes) != 1
        or genes[0].get("geneName", {}).get("value") != "ERG2"
        or genes[0].get("orderedLocusNames") != [{"value": "YMR202W"}]
        or entry.get("organism", {}).get("taxonId") != 559292
        or taxonomy.get("taxonId") != 559292
        or taxonomy.get("rank") != "strain"
        or taxonomy.get("active") is not True
        or len(species) != 1
        or species[0].get("taxonId") != 4932
        or species[0].get("scientificName") != "Saccharomyces cerevisiae"
        or entry["organism"].get("scientificName") != taxonomy.get("scientificName")
        or any(type(audit.get(k)) is not int or audit[k] < 1 for k in ("entryVersion", "sequenceVersion"))
    ):
        raise ValueError("reference gene, locus, versions or taxonomic scope changed")
    links = [x for x in entry.get("uniProtKBCrossReferences", []) if x.get("database") == "SGD"]
    if len(links) != 1 or links[0].get("id") != "S000004815":
        raise ValueError("SGD reference crosswalk changed")
    return {
        "protein_accession": "UniProtKB:P32352",
        "gene": "ERG2",
        "locus": "YMR202W",
        "sgd_id": "SGD:S000004815",
        "entry_version": audit["entryVersion"],
        "sequence_version": audit["sequenceVersion"],
        "entry_type": entry["entryType"],
        "reference_taxon_id": "NCBITaxon:559292",
        "reference_taxon_rank": "strain",
        "reference_taxon_label": taxonomy["scientificName"],
        "species_taxon_id": "NCBITaxon:4932",
        "species_taxon_rank": "species",
        "species_taxon_label": species[0]["scientificName"],
        "role": "REFERENCE_IDENTITY_NOT_TESTED_ALLELE_OR_GENOME",
        "experimental_subject_assignment": False,
        "resistance_inferred_from_reference": False,
    }


def project_figure(rows):
    source_genes = {r["source_gene_label"] for r in rows}
    return [
        {
            "gene": gene,
            "location": "S3 Figure, lower table, " + gene + " row",
            "reconstructed_BY_clones": dict(zip(("S1", "S2", "S3"), reconstructed, strict=True)),
            "EUROSCARF_library": library,
            "SCY325_background": scy,
            "included_in_S3_Table_127": gene in source_genes,
            "reference_accessions": ["UniProtKB:P32352"] if gene == "ERG2" else [],
            "experimental_allele_accession": None,
            "experimental_genome_accession": None,
        }
        for gene, (reconstructed, library, scy) in FIGURE.items()
    ]


def build(root, directory):
    def read(path):
        return json.loads(path.read_bytes())

    plans = {k: read(directory / f"{k}-plan.json") for k in ("native", "supplement", "storage", "reference")}
    cohort = read(reference.check_pin(root, plans["native"]["cohort"]))
    for key in ("prior_verification", "census", "protected", "discovery"):
        reference.check_pin(root, cohort[key])
    for plan in plans.values():
        for item in plan.values():
            if isinstance(item, dict) and set(item) == {"path", "sha256"}:
                reference.check_pin(root, item)
    sources = {}
    for plan in plans.values():
        for key, row in plan["requests"].items():
            status = (
                302 if key in plans["supplement"]["requests"] else 400 if key == "reference-cohort" else 200
            )
            source = native_context.native(root, directory, key, row["url"], statuses=(status,))
            # Signed storage URLs belong in private receipts, not the public report.
            if key.endswith("-storage"):
                source["url"] = urlsplit(row["url"])._replace(query="").geturl()
            sources[key] = source
    article = reference.check_pin(root, sources["article"]["body"])
    if reference.digest(article) != ARTICLE_SHA:
        raise ValueError("reviewed primary article changed")
    tree = html.fromstring(article.read_bytes())
    if tree.xpath('//meta[@name="citation_doi"]/@content') != ["10.1371/journal.pone.0164175"]:
        raise ValueError("primary article identity changed")
    if "http://creativecommons.org/licenses/by/4.0/" not in tree.xpath("//a/@href"):
        raise ValueError("primary license changed")
    locations = {}
    paragraphs = tree.xpath('//div[@id="artText"]//p')
    for name, index in (
        ("experimental_subjects", 17),
        ("screen", 24),
        ("final_cohort", 25),
        ("annotation_limits", 31),
        ("secondary_changes", 36),
        ("reconstruction", 37),
    ):
        p = paragraphs[index]
        locations[name] = {
            "xpath": tree.getroottree().getpath(p),
            "normalized_text_sha256": hashlib.sha256(" ".join(p.text_content().split()).encode()).hexdigest(),
        }
    book = read(reference.check_pin(root, plans["reference"]["workbook"]))
    if book["source"] != sources["s3-table-storage"]["body"] or book["source"]["sha256"] != WORKBOOK_SHA:
        raise ValueError("workbook extraction source changed")
    sheets = book["sheets"]
    if [(s["name"], s["visibility"], s["rows"], s["columns"]) for s in sheets] != [
        ("Tab S2", 0, 133, 10),
        ("PO sensitivity", 1, 24, 9),
        ("H\u00e1rok3", 1, 56, 18),
    ]:
        raise ValueError("workbook sheet inventory changed")
    rows = project_rows(sheets[0]["values"])
    if [r["source_locus"] for r in rows] != plans["reference"]["source_loci"]:
        raise ValueError("planned reference cohort is not the complete source cohort")
    if sources["s3-figure-storage"]["body"]["sha256"] != FIGURE_SHA:
        raise ValueError("visually reviewed reconstruction figure changed")
    for name, source_key in (
        ("native-canary.json", "article"),
        ("reference-canary-review.json", "reference-canary"),
    ):
        canary = read(directory / name)
        if (
            canary.get("manually_inspected") is not True
            or canary["body"] != sources[source_key]["body"]
            or canary["receipt"] != sources[source_key]["receipt"]
        ):
            raise ValueError("canary provenance changed")
    canary_receipt = read(reference.check_pin(root, sources["reference-canary"]["receipt"]))
    headers = {k.lower(): v for k, v in canary_receipt["headers"].items()}
    if (
        headers.get("x-uniprot-release") != "2026_03"
        or headers.get("x-total-results") != "1"
        or headers.get("link")
    ):
        raise ValueError("reference canary release or completeness changed")
    tax_body = reference.check_pin(root, plans["reference"]["taxonomy_body"])
    tax_receipt = read(reference.check_pin(root, plans["reference"]["taxonomy_receipt"]))
    if (
        tax_receipt["url"] != "https://rest.uniprot.org/taxonomy/559292"
        or tax_receipt["status"] != 200
        or tax_receipt["sha256"] != reference.digest(tax_body)
    ):
        raise ValueError("cached taxonomy provenance changed")
    entries = read(reference.check_pin(root, sources["reference-canary"]["body"]))["results"]
    if len(entries) != 1:
        raise ValueError("reference canary not unique")
    protein = project_reference(entries[0], read(tax_body))
    error = read(reference.check_pin(root, sources["reference-cohort"]["body"]))
    if (
        error.get("messages") != ["Too many OR conditions in query. Maximum allowed is 100."]
        or "results" in error
    ):
        raise ValueError("reference query hold changed")
    for row in rows:
        if row["source_locus"] == protein["locus"]:
            row["reference_accessions"] = [protein["protein_accession"]]
            row["reference_status"] = "VERIFIED_REFERENCE_ONLY"
    records = []
    for item in cohort["records"]:
        path = reference.check_pin(root, {k: item[k] for k in ("path", "sha256")})
        record = load_record(path)
        if (
            record["identifier"] != item["identifier"]
            or record["chemical_structure"]["standard_inchi_key"] != item["standard_inchi_key"]
            or record.get("resistance_mechanisms")
            or record.get("genotype_resistance_score_rules")
        ):
            raise ValueError("complete selected record changed")
        records.append(
            {
                **item,
                "compound_scope": "NAME_MATCH_EXACT_REAGENT_FORM_NOT_ESTABLISHED",
                "new_assertions_curated": 0,
            }
        )
    with reference.check_pin(root, cohort["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        or any(reference.digest(checkpoint_path(root, r)) != r["record_sha256"] for r in census)
    ):
        raise ValueError("current corpus census changed")
    return {
        "scope": SCOPE,
        "primary": {
            "pmid": "27711131",
            "doi": "10.1371/journal.pone.0164175",
            "license": "CC-BY-4.0",
            "locations": locations,
        },
        "inputs": {
            "plans": [reference.pin(root, directory / f"{k}-plan.json") for k in plans],
            "workbook": plans["reference"]["workbook"],
            "sources": sources,
            "taxonomy": {k: v for k, v in plans["reference"].items() if k.startswith("taxonomy_")},
        },
        "records": records,
        "experimental_context": {
            "species_label": "Saccharomyces cerevisiae",
            "species_taxon_id": "NCBITaxon:4932",
            "taxon_grounding_basis": "Source species name matched to the cached UniProt taxonomy lineage.",
            "library_background": "BY4741",
            "reconstructed_background": "BY4743-derived haploid clones",
            "comparison_background": "SCY325 (W303-derived)",
            "strain_taxon_assignment": None,
            "experimental_genome_assignment": None,
            "assay": "Source-reported qualitative growth comparison",
            "reagent_supplier": "Applichem",
            "reagent_catalog_or_exact_form_verified": False,
        },
        "source_rows": rows,
        "reconstruction_figure": project_figure(rows),
        "references": [protein],
        "uniprot_release": "2026_03",
        "workbook_sheets": [{k: s[k] for k in ("name", "visibility", "rows", "columns")} for s in sheets],
        "summary": {
            "source_mutants": 127,
            "source_category_counts": COUNTS,
            "resistance_labeled_mutants": 78,
            "hypersensitivity_labeled_mutants": 49,
            "source_stable_marked": 61,
            "source_dubious_orfs": 15,
            "figure_genes": 7,
            "figure_genes_outside_final_table": ["ERG28", "ERG5", "ERG4"],
            "unique_source_loci_or_additional_figure_genes": 130,
            "verified_reference_loci": 1,
            "reference_identity_pending": 129,
            "records_unchanged": 2939,
            "whole_record_reviews_completed": 0,
        },
        "interpretation": {
            "screen_limits": (
                "About half the final phenotypes varied across experiments; "
                "secondary changes can confound single-gene attribution."
            ),
            "null_drug_label": (
                "Not classified for that drug in the source cell; not inferred susceptibility."
            ),
            "unstarred_row": "No stable marker; not automatically a proven unstable phenotype.",
            "hidden_sheets": (
                "Two ancillary comparison sheets retained privately; not extra independent subjects."
            ),
            "source_annotation": (
                "Protein/function descriptions and GO annotations are not direct-target proof."
            ),
            "ERG28": (
                "Figure reports library Nig resistance but reconstructed BY Val resistance; "
                "retain the discrepancy."
            ),
            "ERG24": (
                "Library association does not establish single-locus causality; "
                "reconstructed clones were nonviable."
            ),
            "ERG5": "Reconstruction not validated; not included in the independent-clone analysis.",
            "respiration_deficiency": "ERG2/ERG3 in SCY325 are not interpretable as drug hypersensitivity.",
            "compound_identity": (
                "S1 Table names reagents but does not establish exact form/catalog identity."
            ),
            "measurement": (
                "Qualitative laboratory growth categories; "
                "no MIC conversion or clinical breakpoint inference."
            ),
            "reference_hold": (
                "HTTP 400 query-size rejection, not absence of matching proteins; "
                "no retry or alternate route."
            ),
        },
        "constraints": {
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "issue_1040": "DEFERRED",
            "github_mutations": 0,
            "source_adoptions": 0,
            "numeric_ast_exported": False,
            "sequences_variants_protocols_exported": False,
            "independent_scientific_validation": False,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    root = args.root.resolve()
    result = build(root, root / CACHE)
    (root / args.output).write_text(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))
