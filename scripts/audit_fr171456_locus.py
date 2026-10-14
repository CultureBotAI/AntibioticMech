"""Retain a primary locus-label conflict alongside a scoped UniProt ORF mapping."""

import argparse
import csv
import hashlib
import json
from pathlib import Path

import audit_topoisomerase_references as reference
from lxml import etree

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-fr171456-locus")
OUTPUT = Path("research/2026-10-14-fr171456-locus.json")
PRIMARY_SHA = "7364cf1e078b711ee9533017797f01c274543f2d088fc1eb05fc27381a70d293"
SCOPE = "REFERENCE_ORF_NAME_MAPPING_NOT_EXPERIMENTAL_DELETION_OR_RESISTANCE_ASSIGNMENT"


def primary_context(body):
    if hashlib.sha256(body).hexdigest() != PRIMARY_SHA:
        raise ValueError("primary source differs from inspected payload")
    tree = etree.fromstring(body)
    paragraph, = tree.xpath("body/sec[1]/sec[3]/p[2]")
    text = "".join(paragraph.itertext())
    if not all(label in text for label in ("YPR090w", "YPL090w", "hypersensitivity")):
        raise ValueError("primary locus or effect context changed")
    secondary, = tree.xpath("back/ref-list/ref[@id='b26']")
    if secondary.xpath(".//pub-id[@pub-id-type='pmid']/text()") != ["17553796"]:
        raise ValueError("secondary bibliography identity changed")
    return {
        "reference": "PMID:26456460", "doi": "10.1038/ncomms9613",
        "paragraph_location": "/article/body/sec[1]/sec[3]/p[2]",
        "source_locus_labels": ["YPR090w", "YPL090w"],
        "effect_context": "SOURCE_REPORTED_HYPERSENSITIVITY_NOT_A_NEW_RESISTANCE_CLAIM",
        "figure_2_panels_reviewed": ["c", "d"], "figure_locus_label": "YPR090w",
        "native_figure_visually_reviewed_this_checkpoint": True,
        "source_conflict_resolved": False, "source_typo_corrected": False,
        "cited_background_paper": {"reference": "PMID:17553796", "doi": "10.1074/jbc.M608505200",
                                   "citation_location": "b26", "primary_results_reviewed_here": False},
    }


def project_reference(entry, strain, species):
    if (entry.get("primaryAccession") != "O13585"
            or entry.get("entryType") != "UniProtKB reviewed (Swiss-Prot)"
            or "sequence" in entry or "features" in entry
            or entry.get("entryAudit") != {"entryVersion": 162, "sequenceVersion": 2}):
        raise ValueError("reference identity, version or metadata-only scope changed")
    genes = entry.get("genes")
    if (not isinstance(genes, list) or len(genes) != 1
            or genes[0].get("orderedLocusNames") != [{"value": "YPR089W"}]
            or genes[0].get("orfNames") != [{"value": "YPR090W"}]
            or genes[0].get("geneName") or genes[0].get("synonyms")):
        raise ValueError("ordered locus and ORF-name roles changed")
    if (entry["organism"]["taxonId"] != 559292 or strain.get("taxonId") != 559292
            or strain.get("active") is not True or strain.get("rank") != "strain"
            or species.get("taxonId") != 4932 or species.get("active") is not True
            or species.get("rank") != "species"
            or species.get("scientificName") != "Saccharomyces cerevisiae"):
        raise ValueError("reference taxonomy changed")
    ancestors = [node for node in strain["lineage"] if node["rank"] == "species"]
    if len(ancestors) != 1 or ancestors[0]["taxonId"] != 4932:
        raise ValueError("reference species lineage changed")
    pmids = sorted({xref["id"] for row in entry.get("references", [])
                    for xref in row.get("citation", {}).get("citationCrossReferences", [])
                    if xref["database"] == "PubMed"})
    return {
        "accession": "UniProtKB:O13585", "entry_type": entry["entryType"],
        "entry_version": 162, "sequence_version": 2,
        "ordered_locus_names": ["YPR089W"], "orf_names": ["YPR090W"],
        "gene_symbol": None, "matched_source_label_role": "ORF_NAME_NOT_ORDERED_LOCUS_NAME",
        "reference_taxon_id": "NCBITaxon:559292", "reference_taxon_rank": "strain",
        "reference_organism_name": strain["scientificName"],
        "species_taxon_id": "NCBITaxon:4932", "species_name": species["scientificName"],
        "pubmed_ids": pmids, "focal_paper_cited": "26456460" in pmids,
        "experimental_deletion_identity_established": False,
        "exact_allele_assignment": False, "resistance_effect_assigned": False,
        "annotation_change_history_inferred": False,
    }


def query_projection(body):
    if not isinstance(body.get("results"), list):
        raise ValueError("missing query result list")
    return {"result_count": len(body["results"]), "complete_for_query": True,
            "suggested_queries_not_selected": len(body.get("suggestions", [])),
            "suggestions_are_results": False, "zero_results_establish_absence": False}


def build(root, directory=CACHE, *, record_resolver=None):
    directory = root / directory
    cohort_path = directory / "cohort.json"
    cohort = json.loads(cohort_path.read_bytes())
    inputs = {key: cohort[key] for key in (
        "record", "prior_context", "prior_checkpoint", "source_queue", "census")}
    paths = {key: (record_resolver(root, {**pin, "identifier": cohort["record_identifier"]})
                   if key == "record" and record_resolver else reference.check_pin(root, pin))
             for key, pin in inputs.items()}
    with paths["census"].open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (len(census) != 2939 or len({row["path"] for row in census}) != len(census)
            or {row["path"] for row in census} != {
                str(path.relative_to(root)) for path in (root / "data/antibiotics").rglob("*.yaml")}):
        raise ValueError("census membership changed")
    for row in census:
        if record_resolver:
            path = record_resolver(root, row)
            if reference.digest(path) != row["record_sha256"]:
                raise ValueError("historical record checksum changed")
        else:
            reference.check_pin(root, {"path": row["path"], "sha256": row["record_sha256"]})
    record = load_record(paths["record"])
    if (record["identifier"] != "CHEBI:88298"
            or record["chemical_structure"]["standard_inchi_key"] != "JAHGNOXPMXOEJS-BSPLYONXSA-N"
            or len(record["resistance_mechanisms"]) != 1
            or record["resistance_mechanisms"][0]["gene_families"] != ["ERG26"]):
        raise ValueError("existing compound or resistance claim changed")
    prior = json.loads(paths["prior_context"].read_bytes())
    reused = {key: prior["requests"][key] for key in ("primary", "reference-strain", "species", "figure-2")}
    raw = {}
    for key, request in reused.items():
        raw[key] = reference.check_pin(root, request["body"]).read_bytes()
        reference.check_pin(root, request["receipt"])
    queries, entries = {}, {}
    for key, query in cohort["queries"].items():
        body, request = reference.read_response(root, directory, key, "/uniprotkb/search", {
            "query": [query], "format": ["json"], "size": ["500"], "fields": [cohort["query_fields"]],
        })
        if request["release"] != cohort["release"]:
            raise ValueError("query release differs from plan")
        receipt = json.loads(reference.check_pin(root, request["receipt"]).read_bytes())
        if receipt["retry_performed"] is not False:
            raise ValueError("query was retried")
        entries[key] = body["results"]
        queries[key] = {"query": query, "request": request, **query_projection(body)}
    if len(entries["YPR090W"]) != 1 or entries["YPL090W"]:
        raise ValueError("reviewed query result cohort changed")
    protein = project_reference(entries["YPR090W"][0], json.loads(raw["reference-strain"]),
                                json.loads(raw["species"]))
    return {
        "date": "2026-10-14", "scope": SCOPE, "release": cohort["release"],
        "inputs": {**inputs, "cohort": reference.pin(root, cohort_path)},
        "identifier": record["identifier"],
        "standard_inchi_key": record["chemical_structure"]["standard_inchi_key"],
        "primary": primary_context(raw["primary"]), "reused_sources": reused,
        "queries": queries, "reference_protein": protein,
        "attribution": "UniProt Consortium, CC BY 4.0; Helliwell et al. 2015, CC BY 4.0.",
        "summary": {"corpus_record_hashes_checked": len(census), "new_reference_entries": 1,
                    "new_network_requests": 2, "biological_record_changes": 0,
                    "experimental_deletion_or_allele_assignments": 0, "whole_record_reviews_completed": 0},
        "limitations": [
            "A historical ORF name and current ordered locus name are different annotation roles.",
            "The reference mapping does not establish the gene-model history "
            "or the historical deletion boundaries.",
            "The YPL090W query is scoped to reviewed entries; "
            "no result does not establish biological absence.",
            "Alternative-query suggestions were not selected or treated as protein results.",
            "Hypersensitivity context is not promoted to a new resistance claim or drug target.",
            "The primary label conflict, exact experimental identity "
            "and other earlier holds remain unresolved.",
            "Existing ERG26 evidence and all prior record fields remain unchanged.",
        ],
        "constraints": {"ncbi_requests": 0, "issue_1040": "DEFERRED", "github_mutations": 0,
                        "source_adoptions": 0, "held_sources_retried": False,
                        "sequences_variants_protocols_or_numeric_AST_exported": False,
                        "full_corpus_records_in_scope": 2939, "full_corpus_goal_status": "OPEN"},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=CACHE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd(), args.cache)
    if args.check:
        if json.loads(args.output.read_bytes()) != result:
            raise SystemExit("locus-context dossier does not reproduce")
    else:
        with args.output.open("x") as stream:
            stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
