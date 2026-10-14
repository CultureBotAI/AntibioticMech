"""Audit fungal reference gaps, held sources and a cross-species evidence risk."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode

import audit_caspofungin_context as native_audit
import audit_fungamr_cohort as cohort_audit
import audit_fungamr_references as fungal
import audit_topoisomerase_references as reference
from lxml import etree
from resistance_checkpoint_records import checkpoint_path

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-13-fungal-locus-gaps")
OUTPUT = Path("research/2026-10-13-fungal-locus-gaps.json")
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,xref_embl,sequence_version,version"
)
REFERENCES = {
    "wm276": ("E6R8Q4", "CGB_F6195W", "orderedLocusNames", 367775, 37769, "Cryptococcus gattii", 91),
    "h99-candidate": ("J9VUG0", "CNAG_05935", "orfNames", 235443, 5207, "Cryptococcus neoformans", 71),
}


def text(node):
    return " ".join(" ".join(node.itertext()).split())


def parse_primary(payload, doi, pmid):
    tree = etree.fromstring(payload, parser=etree.XMLParser(resolve_entities=False, no_network=True))
    ids = {n.get("pub-id-type"): n.text for n in tree.findall("./front/article-meta/article-id")}
    if (
        ids.get("doi") != doi
        or ids.get("pmid") != pmid
        or "creativecommons.org/licenses/by/4.0" not in tree.xpath("string(.//permissions)")
    ):
        raise ValueError("primary article identity or license changed")
    return tree


def gene_table_group(tree, table_id, gene):
    tables = tree.xpath(".//table-wrap[@id=$id]", id=table_id)
    if len(tables) != 1:
        raise ValueError("primary table absent or ambiguous")
    group, matches = None, []
    for index, row in enumerate(tables[0].xpath(".//tbody/tr")):
        cells = [text(cell) for cell in row]
        # Group headings mix colspan cells with separate empty cells in native JATS.
        if cells and not any(cells[1:]):
            group = cells[0]
        if any(gene in cell.split() for cell in cells):
            matches.append({"row_index_zero_based": index, "group": group})
    if len(matches) != 1 or not matches[0]["group"]:
        raise ValueError("gene row has no unique explicit table group")
    return {
        "table_id": table_id,
        **matches[0],
        "table_xml_sha256": hashlib.sha256(etree.tostring(tables[0])).hexdigest(),
    }


def project_reference(entry, taxonomy, key):
    accession, locus, field, taxon_id, species_id, species_name, version = REFERENCES[key]
    blocks = entry.get("genes", [])
    species = [t for t in taxonomy.get("lineage", []) if t.get("rank") == "species"]
    if (
        entry.get("primaryAccession") != accession
        or entry.get("entryType") != "UniProtKB unreviewed (TrEMBL)"
        or "sequence" in entry
        or "features" in entry
        or entry.get("entryAudit") != {"entryVersion": version, "sequenceVersion": 1}
        or type(entry["entryAudit"]["sequenceVersion"]) is not int
        or len(blocks) != 1
        or [v["value"] for v in blocks[0].get(field, [])] != [locus]
        or "geneName" in blocks[0]
        or blocks[0].get("synonyms")
        or entry.get("organism", {}).get("taxonId") != taxon_id
        or taxonomy.get("taxonId") != taxon_id
        or taxonomy.get("active") is not True
        or taxonomy.get("rank") != "strain"
        or len(species) != 1
        or species[0].get("taxonId") != species_id
        or species[0].get("scientificName") != species_name
        or taxonomy.get("scientificName") != entry["organism"].get("scientificName")
    ):
        raise ValueError("reference locus, field kind, version or taxonomy changed")
    return {
        "protein_accession": "UniProtKB:" + accession,
        "entry_type": entry["entryType"],
        "entry_version": version,
        "sequence_version": 1,
        "locus": locus,
        "uniprot_locus_field": field,
        "reference_taxon_id": f"NCBITaxon:{taxon_id}",
        "reference_taxon_rank": "strain",
        "reference_organism_name": taxonomy["scientificName"],
        "species_taxon_id": f"NCBITaxon:{species_id}",
        "species_name": species_name,
        "species_matches_card_term": species_id == 5207,
        "paper_resistance_context_matches_card_species": False,
        "primary_native_gene_alias_verified": key == "wm276",
        "role": "DIFFERENT_SPECIES_PRIMARY_REFERENCE_NOT_CARD_ASSIGNMENT"
        if key == "wm276"
        else "H99_IDENTITY_CANDIDATE_NOT_LINKED_RESISTANCE_EVIDENCE",
        "resistance_assertion_supported_by_identity_alone": False,
        "experimental_allele_assignment": None,
        "experimental_genome_assignment": None,
        "canonical_reference_established": False,
    }


def build(root, directory):
    selection_path = directory / "selection.json"
    selection = json.loads(selection_path.read_bytes())
    for item in selection["pins"]:
        reference.check_pin(root, item)
    cohort = json.loads((directory / "cohort.json").read_bytes())
    for key in ("prior", "prior_cohort", "prior_verification", "census", "protected"):
        reference.check_pin(root, cohort[key])
    with reference.check_pin(root, cohort["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        or any(reference.digest(checkpoint_path(root, r)) != r["record_sha256"] for r in census)
    ):
        raise ValueError("corpus membership or bytes changed")
    if set(cohort["terms"]) != {"ARO:3009287", "ARO:3009407", "ARO:3009633"} or len(cohort["records"]) != 3:
        raise ValueError("pending term or record scope changed")
    for item in cohort["records"]:
        record = load_record(checkpoint_path(root, item))
        if (
            record["identifier"] != item["identifier"]
            or record["chemical_structure"]["standard_inchi_key"] != item["standard_inchi_key"]
        ):
            raise ValueError("target compound identity changed")
    initial = json.loads((directory / "initial-plan.json").read_bytes())
    followup = json.loads((directory / "followup-plan.json").read_bytes())
    queries = {}
    for name in ("cyp51-reference-plan.json", "followup-plan.json", "ura6-reference-plan.json"):
        plan = json.loads((directory / name).read_bytes())
        queries.update({k: v for k, v in plan["requests"].items() if "query" in v})
    expected_queries = {
        "cyp51-reference": "xref:embl-KJ004673 AND taxonomy_id:1159556",
        "cyp51-alias": "gene_exact:VvCYP51 AND taxonomy_id:1159556",
        "ura6-wm276": "gene:CGB_F6195W",
        "ura6-h99-candidate": "accession:J9VUG0",
    }
    if {k: v["query"] for k, v in queries.items()} != expected_queries:
        raise ValueError("identifier or alias query scope changed")
    query_results, entries = {}, {}
    for key, query in expected_queries.items():
        url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
            {"query": query, "format": "json", "size": "500", "fields": FIELDS}
        )
        if url != queries[key]["url"]:
            raise ValueError("planned metadata fields changed")
        body, source = fungal.local_response(root, directory, key, url)
        expected_count = 0 if key.startswith("cyp51") else 1
        if len(body["results"]) != expected_count:
            raise ValueError("complete reference query result changed")
        query_results[key] = {
            "source": source,
            "result_count": expected_count,
            "zero_results_establish_absence": False,
        }
        if body["results"]:
            entries[key] = body["results"][0]
    taxonomy_plan = json.loads((directory / "taxonomy-plan.json").read_bytes())
    h99_tax, h99_source = cohort_audit.read_source(root, taxonomy_plan["sources"]["235443"])
    wm_tax, wm_source = fungal.local_response(
        root, directory, "taxonomy-367775", "https://rest.uniprot.org/taxonomy/367775"
    )
    refs = {
        "wm276": project_reference(entries["ura6-wm276"], wm_tax, "wm276"),
        "h99-candidate": project_reference(entries["ura6-h99-candidate"], h99_tax, "h99-candidate"),
    }
    primary = {}
    trees = {}
    for key, request in (
        ("cyp51-primary", initial["requests"]["cyp51-primary"]),
        (
            "ura6-primary",
            {**followup["requests"]["ura6-primary"], "doi": "10.1038/s41467-021-23745-1", "pmid": "34103502"},
        ),
    ):
        primary[key] = native_audit.native(root, directory, key, request["url"])
        trees[key] = parse_primary(
            (directory / f"{key}-response.bin").read_bytes(), request["doi"], request["pmid"]
        )
        primary[key].update(
            {
                "doi": request["doi"],
                "pmid": request["pmid"],
                "license": "CC BY 4.0",
                "medium": "NATIVE_JATS_XML",
                "pdf_or_figures_visually_inspected": False,
            }
        )
    cyp_tree = trees["cyp51-primary"]
    accession_paragraphs = [p for p in cyp_tree.xpath("./body//p") if "KJ004673" in text(p)]
    if (
        len(accession_paragraphs) != 1
        or "UV-8a" not in text(accession_paragraphs[0])
        or "Villosiclava virens (anamorph: Ustilaginoidea virens" not in text(cyp_tree)
        or not any("EC 50" in text(n) for n in cyp_tree.xpath(".//table-wrap[@id='t1']//th"))
    ):
        raise ValueError("CYP51 reference accession, organism relation or endpoint scope changed")
    ura_tree = trees["ura6-primary"]
    species_paragraph = ura_tree.xpath(".//p[@id='Par6']")
    locus_paragraph = ura_tree.xpath(".//p[@id='Par12']")
    if (
        len(species_paragraph) != 1
        or len(locus_paragraph) != 1
        or "WM276, a VGI reference strain of C. gattii" not in text(species_paragraph[0])
        or "CGB_F6195W" not in text(locus_paragraph[0])
        or "WM276" not in text(locus_paragraph[0])
    ):
        raise ValueError("URA6 primary species or locus changed")
    group = gene_table_group(ura_tree, "Tab2", "URA6")
    if group["group"] != "WM276 derived strains":
        raise ValueError("URA6 comparison is not in the reviewed WM276 table group")
    held = {
        "fks1-primary": native_audit.native(
            root, directory, "fks1-primary", initial["requests"]["fks1-primary"]["url"], (500,)
        ),
        "h99-model-paper": native_audit.native(
            root, directory, "model-paper", selection["model_paper_url"], (301,)
        ),
    }
    prior = json.loads(reference.check_pin(root, cohort["prior"]).read_bytes())
    for term in cohort["terms"]:
        if any(q["result_count"] != 0 for q in prior["terms"][term]["queries"]):
            raise ValueError("original exact-symbol query status changed")
    return {
        "date": "2026-10-13",
        "scope": "THREE_FUNGAL_REFERENCE_GAPS_NOT_WHOLE_RECORD_REVIEW",
        "inputs": {
            "selection": reference.pin(root, selection_path),
            **{k: cohort[k] for k in ("prior", "prior_cohort", "prior_verification", "census")},
        },
        "records": cohort["records"],
        "primary": primary,
        "queries": query_results,
        "ura6_references": refs,
        "taxonomy_sources": {"wm276": wm_source, "h99": h99_source},
        "ura6_table_scope": group,
        "ura6_primary_paragraphs": {
            p.get("id"): hashlib.sha256(etree.tostring(p)).hexdigest()
            for p in species_paragraph + locus_paragraph
        },
        "cyp51_reference_accession": {
            "accession": "KJ004673",
            "source_isolate_label": "UV-8a",
            "role": "PAPER_REPORTED_REFERENCE_NOT_GENOME_OR_TESTED_RESISTANT_ALLELE",
            "archive_endpoint_requested": False,
            "uniprot_match_found": False,
            "paragraph_sha256": hashlib.sha256(etree.tostring(accession_paragraphs[0])).hexdigest(),
        },
        "term_assessments": selection["term_assessments"],
        "held_sources": held,
        "limitations": selection["limitations"],
        "review_findings": selection["review_findings"],
        "attribution": [
            "Wang et al., Scientific Reports (2015), DOI:10.1038/srep17575, CC BY 4.0",
            "Chang et al., Nature Communications (2021), DOI:10.1038/s41467-021-23745-1, CC BY 4.0",
            "UniProt release 2026_03; protein names and identifiers are database annotations.",
        ],
        "summary": {
            "corpus_records_hash_verified": len(census),
            "terms_investigated": 3,
            "new_h99_identity_candidates": 1,
            "different_species_primary_references": 1,
            "new_uniprot_queries": 4,
            "new_taxonomy_queries": 1,
            "taxonomy_caches_reused": 1,
            "native_primary_articles_read": 2,
            "unread_primary_requests_held": 2,
            "biological_records_changed": 0,
            "new_resistance_assertions": 0,
            "exact_alleles_assigned": 0,
            "whole_record_reviews_completed": 0,
        },
        "constraints": {
            **cohort["constraints"],
            "numeric_ast_exported": False,
            "sequences_variants_protocols_exported": False,
            "cross_species_phenotype_transfer": False,
        },
        "independent_scientific_review": False,
        "goal_status": "OPEN",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    value = build(root, root / CACHE)
    data = (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.output.exists() and args.output.read_bytes() != data:
        raise ValueError("refusing to replace a different checkpoint")
    args.output.write_bytes(data)
    print(json.dumps(value["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
