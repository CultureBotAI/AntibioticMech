"""Keep yeast ATP reference identity separate from conditional phenotype evidence."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode, urlsplit

import audit_topoisomerase_references as reference
from lxml import etree, html
from resistance_checkpoint_records import (
    CLOTRIMAZOLE_FIXTURE as CLOTRIMAZOLE_FIXTURE,
)
from resistance_checkpoint_records import (
    CLOTRIMAZOLE_PATH as CLOTRIMAZOLE_PATH,
)
from resistance_checkpoint_records import (
    checkpoint_path as checkpoint_path,
)

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-13-yeast-atp")
OUTPUT = Path("research/2026-10-13-yeast-atp-context.json")
FIELDS = ("accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
          "xref_sgd,lit_pubmed_id,sequence_version,version")
GENES = {"ATP1": ("P07251", "YBL099W", "S000000195", "alpha"),
         "ATP2": ("P00830", "YJR121W", "S000003882", "beta")}
METADATA_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode({
    "query": "EXT_ID:40790106 AND SRC:MED", "format": "json", "resultType": "core", "pageSize": "1"})
PRIMARY_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9635649/fullTextXML"
PUBLISHER_URL = "https://oup.silverchair-cdn.com/article-minimal/6730751"
PMID = "36173330"
DOI = "10.1093/g3journal/jkac246"


def project_protein(entry, gene, taxonomy):
    protein = reference.project_reference(entry, gene, 4932, taxonomy)
    accession, locus, sgd_id, subunit = GENES[gene]
    block, = entry["genes"]
    links = [r for r in entry.get("uniProtKBCrossReferences", []) if r["database"] == "SGD"]
    if (entry["primaryAccession"] != accession or entry["organism"]["taxonId"] != 559292
            or taxonomy["rank"] != "strain" or block["geneName"]["value"] != gene
            or protein["ordered_locus_names"] != [locus] or "features" in entry
            or links != [{"database": "SGD", "id": sgd_id,
                          "properties": [{"key": "GeneName", "value": gene}]}]
            or protein["protein_name"] != f"ATP synthase subunit {subunit}, mitochondrial"):
        raise ValueError("reference subunit, locus, strain, SGD mapping or field scope changed")
    ids = {r["id"] for c in protein.pop("bibliography") for r in c["identifiers"]}
    return {**protein, "sgd_id": sgd_id, "gene": gene,
            "database_paper_in_bibliography": "40790106" in ids,
            "independent_primary_in_bibliography": PMID in ids or DOI in ids,
            "role": "REFERENCE_IDENTITY_NOT_EXPERIMENTAL_ALLELE_OR_PHENOTYPE"}


def request(root, directory, key, url):
    attempt_path = directory / f"{key}-attempt.json"
    receipt_path = directory / f"{key}-receipt.json"
    response = directory / f"{key}-response.bin"
    attempt, receipt = [json.loads(p.read_bytes()) for p in (attempt_path, receipt_path)]
    if (attempt.get("url") != url or receipt.get("url") != url
            or receipt.get("status") != 200 or receipt.get("retry_performed") is not False
            or receipt.get("sha256") != reference.digest(response)
            or receipt.get("bytes") != response.stat().st_size):
        raise ValueError("request identity, status or content changed")
    # Signed public asset links remain in the private receipts, not this export.
    return {"url_without_query": urlsplit(url)._replace(query="").geturl(),
            "attempt": reference.pin(root, attempt_path), "receipt": reference.pin(root, receipt_path),
            "response": reference.pin(root, response), "status": 200,
            "retrieved_at": receipt["retrieved_at"]}


def primary_context(payload):
    tree = etree.fromstring(payload, parser=etree.XMLParser(resolve_entities=False, no_network=True))
    ids = {e.get("pub-id-type"): e.text for e in tree.findall("./front/article-meta/article-id")}
    if (ids.get("doi") != DOI or ids.get("pmid") != PMID or ids.get("pmcid") != "PMC9635649"
            or "https://creativecommons.org/licenses/by/4.0/" not in tree.xpath("string(.//permissions)")):
        raise ValueError("primary article identity or reuse license changed")
    locations = {"subjects": "sec3", "associations": "sec27", "comparison": "sec29", "discussion": "sec35"}
    sections = {}
    for key, identifier in locations.items():
        nodes = tree.xpath(".//sec[@id=$identifier]", identifier=identifier)
        if len(nodes) != 1:
            raise ValueError("primary source section is absent or ambiguous")
        sections[key] = {"section_id": identifier,
                         "xml_sha256": hashlib.sha256(etree.tostring(nodes[0])).hexdigest()}
    if (any(label not in tree.xpath("string(.//sec[@id='sec3'])")
            for label in ("BY4741", "BY4742", "Saccharomyces cerevisiae"))
            or "PRJNA742704" not in tree.xpath("string(.//sec[@id='sec40'])")):
        raise ValueError("primary background labels changed")
    figure, = tree.xpath(".//fig[@id='jkac246-F5']")
    return {"doi": DOI, "pmid": PMID, "pmcid": "PMC9635649", "license": "CC BY 4.0",
            "license_url": "https://creativecommons.org/licenses/by/4.0/",
            "locations": sections,
            "figure_caption_xml_sha256": hashlib.sha256(etree.tostring(figure.find("caption"))).hexdigest(),
            "background_labels": ["BY4741", "BY4742"], "diploid_derivatives_also_reported": True,
            "reference_strain_is_exact_tested_derivative": False,
            "source_study_accession": "PRJNA742704", "study_accession_is_genome_assignment": False,
            "experimental_protein_allele_or_genome_assignment": False}


def build(root, directory):
    plan_path = directory / "cohort.json"
    plan = json.loads(plan_path.read_bytes())
    for key in ("prior_verification", "protected", "census", "definitions", "expansion"):
        reference.check_pin(root, plan[key])
    if (plan["fields"] != FIELDS or plan["queries"] != {
            g: f"gene_exact:{g} AND organism_id:559292 AND reviewed:true" for g in GENES}
            or plan["complete_collection_aware_records_loaded"] is not True):
        raise ValueError("gene query or inspected-record scope changed")
    definitions = json.loads((root / plan["definitions"]["path"]).read_bytes())
    terms = {k: {f: v[f] for f in ("definition_citation_ids", "record_memberships")}
             for k, v in definitions["terms"].items() if "PMID:40790106" in v["definition_citation_ids"]}
    if terms != plan["terms"] or len(terms) != 19:
        raise ValueError("shared database-citation membership changed")
    with (root / plan["census"]["path"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (len(census) != 2939 or len({r["path"] for r in census}) != len(census)
            or {r["path"] for r in census} != {str(p.relative_to(root))
                                              for p in (root / "data/antibiotics").rglob("*.yaml")}
            or any(reference.digest(checkpoint_path(root, r)) != r["record_sha256"] for r in census)):
        raise ValueError("whole-corpus membership or record bytes changed")
    records = plan["records"]
    if (len(records) != 10 or {r["identifier"] for r in records}
            != {i for t in terms.values() for i in t["record_memberships"]}):
        raise ValueError("citation record cohort changed")
    for item in records:
        record = load_record(checkpoint_path(root, item))
        row, = [r for r in census if r["identifier"] == item["identifier"]]
        if (any(item[k] != row[k] for k in ("path", "label", "record_sha256", "standard_inchi_key"))
                or record["identifier"] != item["identifier"]
                or record["chemical_structure"]["standard_inchi_key"] != item["standard_inchi_key"]
                or {c["aro_id"] for c in record.get("resistance_mechanisms", []) if c.get("aro_id") in terms}
                != set(item["citation_terms"])):
            raise ValueError("record identity or source assertion membership changed")
    expansion = json.loads((root / plan["expansion"]["path"]).read_bytes())
    old_query = expansion["queries"]["40790106"]
    if old_query != plan["prior_literature_query"] or old_query["result_count"] != 0:
        raise ValueError("prior literature query changed")
    for page in old_query["pages"]:
        for key in ("cache", "receipt"):
            reference.check_pin(root, page[key])
        if json.loads((root / page["cache"]["path"]).read_bytes())["results"] != []:
            raise ValueError("prior zero-result response changed")
    tax_request = plan["reference_taxonomy_reused"]
    taxonomy, checked_tax = reference.read_response(root, (root / tax_request["cache"]["path"]).parent,
                                                    "tax-559292", "/taxonomy/559292")
    if checked_tax != tax_request:
        raise ValueError("reused taxonomy request changed")
    proteins, queries = {}, {}
    for gene in GENES:
        body, queries[gene] = reference.read_response(root, directory, gene, "/uniprotkb/search", {
            "query": [plan["queries"][gene]], "format": ["json"], "size": ["50"], "fields": [FIELDS]})
        if queries[gene]["release"] != "2026_03":
            raise ValueError("reference release changed")
        entry, = body["results"]
        proteins[gene] = project_protein(entry, gene, taxonomy)
    canary = json.loads((directory / "canary-reviewed.json").read_bytes())
    if (canary["source"] != queries["ATP1"]["cache"] or canary["receipt"] != queries["ATP1"]["receipt"]
            or canary["manually_reviewed"] is not True):
        raise ValueError("reference canary changed")
    sources = {k: request(root, directory, k, url) for k, url in (
        ("metadata", METADATA_URL), ("primary", PRIMARY_URL), ("publisher", PUBLISHER_URL))}
    metadata = json.loads((directory / "metadata-response.bin").read_bytes())
    item, = metadata["resultList"]["result"]
    if (metadata["hitCount"] != 1 or item["pmid"] != "40790106" or item["source"] != "MED"
            or item["doi"] != "10.1038/s41564-025-02084-7" or not item["title"].startswith("FungAMR:")):
        raise ValueError("database paper identity changed")
    primary = primary_context((directory / "primary-response.bin").read_bytes())
    publisher = html.fromstring((directory / "publisher-response.bin").read_bytes())
    image_url, = {e.get("src") for e in publisher.xpath("//img[@src]")
                  if "/m_jkac246f5.jpeg?" in e.get("src")}
    figure_plan = json.loads((directory / "figure-plan.json").read_bytes())
    if figure_plan["url"] != image_url or figure_plan["publisher"] != sources["publisher"]["response"]:
        raise ValueError("native figure source changed")
    sources["figure"] = request(root, directory, "figure", image_url)
    inspection_path = directory / "inspection.json"
    inspection = json.loads(inspection_path.read_bytes())
    if (inspection["primary"] != sources["primary"]["response"]
            or inspection["figure"] != sources["figure"]["response"]
            or inspection["native_figure_5_visually_reviewed"] is not True):
        raise ValueError("primary interpretation is not bound to inspected sources")
    return {"date": "2026-10-13",
            "scope": "REFERENCE_GROUNDING_WITH_PRIMARY_COUNTEREVIDENCE_NOT_ALLELE_ASSIGNMENT",
            "inputs": {k: plan[k] for k in ("census", "definitions", "expansion", "prior_verification")},
            "plans": {"cohort": reference.pin(root, plan_path),
                      "inspection": reference.pin(root, inspection_path)},
            "database_citation": {"pmid": "40790106", "doi": item["doi"], "title": item["title"],
                "terms": terms, "isOpenAccess": item["isOpenAccess"],
                "database_rows_inspected_or_imported": False,
                "all_claims_from_this_citation_are_original_experiments": False},
            "records": records, "reference_proteins": proteins, "uniprot_queries": queries,
            "reference_taxonomy_reused": checked_tax, "prior_literature_query": old_query,
            "sources": sources, "independent_primary": {**primary, **inspection["interpretation"]},
            "curation_decision": "HOLD_EXACT_SOURCE_ROW_SUBJECT_AND_CONDITIONAL_EFFECT_RECONCILIATION",
            "summary": {"corpus_records_checked": 2939, "shared_citation_terms": 19,
                "shared_citation_records": 10, "new_reference_proteins": 2,
                "independent_primary_texts_inspected": 1, "native_figures_reviewed": 1,
                "biological_records_changed": 0, "experimental_allele_assignments": 0,
                "whole_record_reviews_completed": 0, "full_corpus_goal_status": "OPEN"},
            "limitations": [
                "A reference gene identity is not the identity or effect of a tested allele.",
                "The independent 2022 study has not been crosswalked to exact FungAMR source rows.",
                "The source-owned CARD target-alteration classification is retained, not newly validated.",
                "Supplementary tables and Figure S3 have not been inspected; "
                "broad assay review remains open.",
                "No single clone, species-wide resistance, clinical phenotype "
                "or direct ATP-synthase target is inferred.",
                "No sequences, exact variant specifications, protocols or numeric AST are exported."],
            "attribution": {"reference": "UniProt Consortium, UniProtKB and UniProt Taxonomy, "
                                         "release 2026_03, CC BY 4.0",
                            "primary": "Taylor et al. (2022), G3, DOI:10.1093/g3journal/jkac246, CC BY 4.0"},
            "constraints": {**{k: v for k, v in plan["constraints"].items() if k != "automatic_redirects"},
                            "cli_automatic_redirects": False, "web_public_publisher_redirect_observed": True}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=CACHE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd(), Path.cwd() / args.cache)
    if args.check:
        if json.loads(args.output.read_bytes()) != result:
            raise SystemExit("Yeast ATP context does not reproduce")
    else:
        with args.output.open("x") as stream:
            stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
