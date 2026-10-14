"""Replay bibliographic access checks and a reference-only Sub1 mapping offline."""

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import urlencode

import audit_caspofungin_context as native_context
import audit_mycophenolic_context as prior_context
import audit_topoisomerase_references as reference

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-mycophenolic/literature-followup")
OUTPUT = Path("research/2026-10-14-mycophenolic-literature.json")
STUDIES = {
    "2005": ("16278936", "10.1002/yea.1300"),
    "2008": ("18823333", "10.1111/j.1365-2443.2008.01229.x"),
}
QUERY = "gene_exact:SUB1 AND organism_id:559292 AND reviewed:true"
TAXONOMY = Path("reports/resistance-grounding-2026-10-13-tavaborole")
TAXONOMY_SHA = "9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810"


def project_metadata(payload, year):
    """Access labels are kept as metadata, never interpreted as reuse permission."""
    pmid, doi = STUDIES[year]
    rows = payload.get("resultList", {}).get("result", [])
    if type(payload.get("hitCount")) is not int or payload["hitCount"] != 1 or len(rows) != 1:
        raise ValueError("bibliographic result is missing or ambiguous")
    row = rows[0]
    if row.get("id") != pmid or row.get("source") != "MED" or row.get("doi", "").lower() != doi:
        raise ValueError("bibliographic identity changed")
    links = row.get("fullTextUrlList", {}).get("fullTextUrl", [])
    selected = [item for item in links if item.get("documentStyle") == "pdf"]
    if len(selected) != 1 or selected[0].get("url") != "https://onlinelibrary.wiley.com/doi/pdfdirect/" + doi:
        raise ValueError("publisher PDF link missing or ambiguous")
    return {
        "pmid": "PMID:" + pmid, "doi": "DOI:" + doi,
        "title": row["title"], "authors": row["authorString"],
        "source_is_open_access": row.get("isOpenAccess"),
        "selected_link": {key: selected[0].get(key) for key in
                          ("url", "site", "documentStyle", "availability", "availabilityCode")},
        "primary_results_reviewed": False,
        "reuse_permission_inferred": False,
        "phenotype_or_causality_inferred": False,
    }


def project_sub1(entry, taxonomy):
    if {"sequence", "features", "comments"}.intersection(entry):
        raise ValueError("unexpected biological payload")
    projected = reference.project_reference(entry, "SUB1", 4932, taxonomy)
    species = [row for row in taxonomy["lineage"] if row["rank"] == "species"]
    genes = entry.get("genes", [])
    links = [row for row in entry.get("uniProtKBCrossReferences", []) if row.get("database") == "SGD"]
    if (
        entry["primaryAccession"] != "P54000"
        or entry["entryAudit"] != {"entryVersion": 190, "sequenceVersion": 1}
        or len(genes) != 1 or genes[0].get("geneName", {}).get("value") != "SUB1"
        or projected["gene_names"] != ["SUB1", "TSP1"]
        or projected["ordered_locus_names"] != ["YMR039C"]
        or len(links) != 1 or links[0].get("id") != "S000004642"
        or entry["organism"]["taxonId"] != 559292 or taxonomy["rank"] != "strain"
        or taxonomy["scientificName"] != "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)"
        or entry["organism"]["scientificName"] != taxonomy["scientificName"]
        or len(species) != 1 or species[0].get("scientificName") != "Saccharomyces cerevisiae"
    ):
        raise ValueError("Sub1 reference identity, version or taxonomy changed")
    bibliography = projected.pop("bibliography")
    cited = any(item == {"database": "PubMed", "id": STUDIES["2008"][0]}
                for row in bibliography for item in row["identifiers"])
    return {
        **projected, "canonical_gene": "SUB1", "sgd_id": "SGD:S000004642",
        "role": "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE_OR_GENOME",
        "selected_2008_paper_in_uniprot_bibliography": cited,
        "resistance_asserted_from_reference": False,
    }


def build(root, directory):
    def read(path):
        return json.loads(path.read_bytes())

    cohort = read(directory / "cohort.json")
    for name in ("census", "protected", "prior_context", "prior_subjects"):
        reference.check_pin(root, cohort[name])
    record_pin = {**cohort["record"], "identifier": cohort["identifier"]}
    baseline = directory / "baseline-record.yaml"
    if reference.digest(baseline) != record_pin["sha256"]:
        raise ValueError("historical record baseline changed")
    record = load_record(baseline)
    if (
        record["identifier"] != "CHEBI:168396"
        or record["chemical_structure"]["standard_inchi_key"] != "HPNSFSBZBAHARI-RUDMXATFSA-N"
    ):
        raise ValueError("compound identity changed")
    with (root / cohort["census"]["path"]).open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    if len(rows) != 2939 or len({row["identifier"] for row in rows}) != 2939:
        raise ValueError("corpus checkpoint changed")
    sources, studies = {}, {}
    for year, (pmid, _) in STUDIES.items():
        key = "metadata-" + year
        url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode({
            "query": "EXT_ID:" + pmid + " AND SRC:MED", "format": "json",
            "resultType": "core", "pageSize": 10})
        sources[key] = native_context.native(root, directory, key, url)
        studies[year] = project_metadata(read(directory / (key + "-response.bin")), year)
    sources["primary-2005"] = native_context.native(
        root, directory, "primary-2005", studies["2005"]["selected_link"]["url"], statuses=(403,))
    if any((directory / ("primary-2008" + suffix)).exists()
           for suffix in ("-attempt.json", "-receipt.json", "-response.bin")):
        raise ValueError("2008 was not part of the executed publisher batch")
    studies["2005"]["primary_status"] = "PUBLISHER_403_HELD_NO_RETRY"
    studies["2008"]["primary_status"] = "NOT_REQUESTED_AFTER_PUBLISHER_CANARY_DENIAL"
    parameters = {"query": [QUERY], "fields": [prior_context.FIELDS], "format": ["json"], "size": ["10"]}
    payload, sources["sub1-reference"] = reference.read_response(
        root, directory, "sub1-reference", "/uniprotkb/search", parameters)
    sources["sub1-request"] = native_context.native(
        root, directory, "sub1-reference", sources["sub1-reference"]["url"])
    taxonomy, sources["taxonomy-reused"] = reference.read_response(
        root, root / TAXONOMY, "tax-559292", "/taxonomy/559292")
    if sources["taxonomy-reused"]["cache"]["sha256"] != TAXONOMY_SHA:
        raise ValueError("cached taxonomy changed")
    entries = payload.get("results", [])
    if len(entries) != 1 or sources["sub1-reference"]["release"] != "2026_03":
        raise ValueError("reference cardinality or release changed")
    sub1 = project_sub1(entries[0], taxonomy)
    if sub1["selected_2008_paper_in_uniprot_bibliography"]:
        raise ValueError("selected paper bibliography scope changed")
    return {
        "cohort": reference.pin(root, directory / "cohort.json"),
        "record": record_pin, "prior_context": cohort["prior_context"],
        "prior_subjects": cohort["prior_subjects"],
        "sources": sources, "studies": studies, "reference": sub1,
        "limits": {
            "whole_record_primary_review": "OPEN", "experimental_allele_assignment": None,
            "experimental_strain_taxon_assignment": None, "experimental_genome_assignment": None,
            "clinical_category_inferred": False, "numeric_ast_exported": False,
            "sequences_exported": False, "variants_exported": False,
            "source_adoption": False, "ncbi_requests": 0, "issue_1040": "DEFERRED",
            "independent_scientific_signoff": False,
            "prior_2002_and_2003_holds_retried": False,
        },
        "summary": {
            "corpus_records_in_scope": len(rows), "records_in_this_checkpoint": 1,
            "bibliographic_records_checked": 2, "new_reference_proteins": 1,
            "new_full_text_requests": 1, "new_full_text_access_holds": 1,
            "new_primary_results_reviewed": 0, "curated_resistance_assertions": 0,
            "whole_record_primary_signoffs": 0,
        },
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
