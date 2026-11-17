"""Replay bounded AAC34 metadata searches and a cached chemical-identity check."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode

from audit_fungamr_cohort import read_source
from audit_valinomycin_abcb1 import planned_source
from audit_vgb_evidence import PRIMARY_URL, read_json, reference, require, text, wrapped
from lxml import etree

CACHE = Path("reports/resistance-grounding-2026-10-15-aac34-followup")
OUTPUT = Path("research/2026-10-15-aac34-followup.json")
COHORT_SHA = "e1cc9a8ae30fceb4e60b9b0c665dfe79806646708a3da4782d5d70ae319d7554"
SCOPE = "AAC34_BOUNDED_NAME_QUERIES_AND_CHEMICAL_CONTEXT_NOT_EXPERIMENTAL_IDENTITY"
TERM = "ARO:3003989"
PARAGRAPH_SHA = "c6cab8f75deae3725163124b5abf79ad87ebef259c850c33688ed4dc5d54a9b3"
ORGANISM_URL = (
    "https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A1120679"
    "&format=json&size=25&fields=accession%2Creviewed%2Cprotein_name%2Cgene_names%2Corganism_id"
    "%2Corganism_name%2Csequence_version%2Cversion%2Cxref_embl%2Cxref_card%2Ccc_miscellaneous"
)


def query_url(reviewed):
    require(type(reviewed) is bool, "review subset must be Boolean")
    return "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {
            "query": '(gene_exact:"aac(6\')-34" OR protein_name:"AAC(6\')-34") AND reviewed:'
            + str(reviewed).lower(),
            "format": "json",
            "size": 500,
            "fields": "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
            "xref_card,lit_pubmed_id,sequence_version,version",
        }
    )


def chemical_context(payload):
    tree = etree.fromstring(payload, etree.XMLParser(resolve_entities=False, no_network=True))
    ids = {n.get("pub-id-type"): text(n) for n in tree.xpath("./front/article-meta/article-id")}
    sections = tree.xpath('//sec[@id="sec11"]')
    require(
        ids.get("pmid") == "27929110"
        and ids.get("doi") == "10.1038/ncomms13803"
        and len(sections) == 1
        and text(sections[0].find("title")) == "Antibiotics and reagents",
        "selected article or section changed",
    )
    paragraphs = sections[0].findall("p")
    require(len(paragraphs) == 1, "selected paragraph coverage changed")
    paragraph = text(paragraphs[0])
    require(
        hashlib.sha256(paragraph.encode()).hexdigest() == PARAGRAPH_SHA
        and len(paragraph) == 590
        and "kanamycin" not in paragraph.casefold(),
        "inspected reagent paragraph changed",
    )
    return {
        "pmid": "PMID:27929110",
        "doi": "DOI:10.1038/ncomms13803",
        "location": "Antibiotics and reagents / sec11 / sole direct paragraph",
        "paragraph_sha256": PARAGRAPH_SHA,
        "supplier_context": "General Sigma-Aldrich supplier statement with exceptions, not a drug identity.",
        "kanamycin_specific_product_identifier_in_selected_paragraph": False,
        "whole_article_or_supplement_identifier_absence_claimed": False,
        "exact_corpus_structure_assignment": None,
        "activity_observation_curated": False,
        "operational_paragraph_exported": False,
    }


def build(root):
    directory = root / CACHE
    require(reference.digest(directory / "cohort.json") == COHORT_SHA, "frozen cohort changed")
    cohort = json.loads((directory / "cohort.json").read_bytes())
    for value in cohort.values():
        if isinstance(value, dict) and set(value) == {"path", "sha256"}:
            reference.check_pin(root, value)
    require(cohort["source_term_id"] == TERM and cohort["source_label"] == "AAC(6')-34", "term changed")
    plan = json.loads((directory / "reference-plan.json").read_bytes())
    require(
        plan["cohort"] == reference.pin(root, directory / "cohort.json")
        and plan["canary_request"] == "reviewed"
        and plan["fallback_requires"] == "COMPLETE_REVIEWED_QUERY_WITH_ZERO_RESULTS"
        and plan["automatic_redirects"] is plan["retry_performed"] is False
        and plan["ncbi_requests"] == 0
        and plan["requests"]
        == {key: {"url": query_url(flag)} for key, flag in (("reviewed", True), ("unreviewed", False))},
        "recorded query plan changed",
    )
    queries = {}
    for key, reviewed in (("reviewed", True), ("unreviewed", False)):
        source = planned_source(root, directory, key, "reference-plan.json", query_url(reviewed))
        body, source = read_source(root, source)
        require(body["results"] == [], "name query no longer has zero results")
        queries[key] = {
            "source": source,
            "reviewed_subset": reviewed,
            "result_count": 0,
            "complete_for_query": True,
            "biological_absence_inferred": False,
            "query_scope": "GLOBAL_ASCII_SOURCE_LABEL_IN_GENE_OR_PROTEIN_NAME_NOT_ALL_ALIASES",
        }
    require(
        queries["reviewed"]["source"]["retrieved_at"] < queries["unreviewed"]["source"]["retrieved_at"],
        "reviewed-first retrieval order changed",
    )
    organism_wrapper = read_json(root, cohort["organism_query"])
    organism, organism_source = read_source(
        root, {"wrapper": cohort["organism_query"], "url": organism_wrapper["url"]}
    )
    require(
        organism_wrapper["url"] == ORGANISM_URL and organism["results"] == [],
        "exact-organism query changed",
    )
    _, primary = wrapped(root, cohort["primary"], PRIMARY_URL)
    return {
        "date": "2026-10-15",
        "scope": SCOPE,
        "source_term_id": TERM,
        "inputs": {
            **{k: cohort[k] for k in ("index", "aac6", "aac6_verification", "source_queue", "primary")},
            "cohort": reference.pin(root, directory / "cohort.json"),
        },
        "name_queries": queries,
        "exact_organism_query": {
            "source": organism_source,
            "reference_taxon_id": "NCBITaxon:1120679",
            "result_count": 0,
            "complete_for_query": True,
            "biological_absence_inferred": False,
            "query_scope": "EXACT_ORGANISM_ID_NOT_ALL_TAXONOMIC_DESCENDANTS_OR_REFERENCE_ORGANISMS",
        },
        "chemical_context": chemical_context(primary),
        "summary": {
            "complete_cached_name_queries": 2,
            "complete_cached_organism_queries": 1,
            "selected_reference_proteins": 0,
            "selected_reagent_paragraphs_reviewed": 1,
        },
        "limits": {
            "new_network_requests": 0,
            "earlier_name_query_requests_replayed": 2,
            "ncbi_requests": 0,
            "experimental_assignments": 0,
            "biological_records_changed": 0,
            "primary_access_holds_retried": 0,
            "all_aliases_or_sources_searched": False,
            "genome_assignment": None,
            "clinical_resistance_category_inferred": False,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": "UniProt Consortium metadata, release 2026_03. Pawlowski et al. (2016), "
        "DOI:10.1038/ncomms13803, narrowly inspected reagent context; no operational text exported.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    body = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
    if args.check or args.output.exists():
        require(args.output.read_bytes() == body, "AAC34 follow-up does not reproduce")
    else:
        with args.output.open("xb") as stream:
            stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
