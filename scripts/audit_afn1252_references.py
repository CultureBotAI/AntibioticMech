"""Ground AFN-1252 reference leads without treating access-held studies as reviewed."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlencode

import audit_card_reference_lineages as lineages
import audit_topoisomerase_references as reference
from audit_beauvericin_references import complete_query
from audit_stth_reference import FIELDS
from audit_valinomycin_abcb1 import planned_source
from lxml import html

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-afn1252")
OUTPUT = Path("research/2026-10-14-afn1252-reference-context.json")
COHORT_SHA = "9e711ff16957bfbc83d4d27550368154a5480fb9ed908f1574a3f4b79def627b"
IDENTIFIER = "antibioticmech:curator-8edc5e6516"
INCHIKEY = "QXTWSUQCXCWEHF-JXMROGBWSA-N"
METADATA_QUERY = "(EXT_ID:24189061 OR EXT_ID:22948878) AND SRC:MED"
LEADS = {
    "24189061": (
        "10.1074/jbc.m113.512905",
        "PMC3868742",
        "2013",
        "46c2e46cce19be0caba2b4800e47d305c55ec9fbe9d403d94f1605464d9b6bc6",
    ),
    "22948878": (
        "10.1128/aac.01411-12",
        "PMC3486558",
        "2012",
        "2f5349e7e921ae9be1294ae527d2b0b3111a943db13a324b3afbf0c2e044ddb1",
    ),
}
QUERIES = {
    "reference-2013": ("lit_pubmed:24189061", "reference-plan.json", 0),
    "reference-2012": ("lit_pubmed:22948878", "reference-followup-plan.json", 0),
    "reference-names": (
        "gene_exact:fabI AND taxonomy_id:1280 AND reviewed:true",
        "named-reference-plan.json",
        2,
    ),
}
PUBLISHERS = {
    "doi-2013": ("request-plan.json", "https://doi.org/10.1074/jbc.M113.512905", 302),
    "publisher-2013": (
        "publisher-plan.json",
        "https://linkinghub.elsevier.com/retrieve/pii/S0021925820553234",
        200,
    ),
    "journal-2013": ("journal-plan.json", "https://jbc.org/retrieve/pii/S0021925820553234", 403),
    "article-2012": ("second-primary-plan.json", "https://journals.asm.org/doi/10.1128/AAC.01411-12", 403),
}
PROTEINS = {
    "Q2FZQ3": (93061, "Staphylococcus aureus (strain NCTC 8325 / PS 47)", "SAOUHSC_00947", 116),
    "Q6GI75": (282458, "Staphylococcus aureus (strain MRSA252)", "SAR0978", 134),
}


def discovery_context(row):
    if (
        row["identifier"] != IDENTIFIER
        or row["standard_inchi_key"] != INCHIKEY
        or row["candidate_ids"] != ["MED:22948878", "MED:24189061"]
        or len(row["queries"]) != 2
        or row["has_existing_resistance_evidence"] is not False
    ):
        raise ValueError("selected discovery record changed")
    leads = {}
    for query, count in zip(row["queries"], (2, 0), strict=True):
        if (
            query["hit_count"] != count
            or len(query["candidates"]) != count
            or query["next_cursor"] is not None
            or query["request"]["status"] != 200
        ):
            raise ValueError("discovery query incomplete")
        for candidate in query["candidates"]:
            key = candidate["id"]
            if key not in LEADS or key in leads:
                raise ValueError("unexpected or duplicated discovery citation")
            doi, pmcid, year, _ = LEADS[key]
            if (
                candidate.get("source") != "MED"
                or candidate.get("pmid") != key
                or candidate.get("doi") != doi
                or candidate.get("pmcid") != pmcid
                or candidate.get("pubYear") != year
            ):
                raise ValueError("discovery publication identity changed")
            leads[key] = candidate
    if set(leads) != set(LEADS):
        raise ValueError("discovery citation coverage changed")
    return leads


def metadata_context(payload, leads):
    request = payload.get("request", {})
    rows = payload.get("resultList", {}).get("result", [])
    if (
        type(payload.get("hitCount")) is not int
        or payload["hitCount"] != 2
        or len(rows) != 2
        or len({r["id"] for r in rows}) != 2
        or {r["id"] for r in rows} != set(LEADS)
        or request.get("queryString") != METADATA_QUERY
        or request.get("resultType") != "core"
        or type(request.get("pageSize")) is not int
        or request["pageSize"] != 2
        or payload.get("nextCursorMark")
    ):
        raise ValueError("metadata query identity or completeness changed")
    papers = {}
    for row in rows:
        pmid = row["id"]
        if (
            any(
                row.get(k) != leads[pmid][k]
                for k in ("id", "source", "pmid", "pmcid", "doi", "title", "pubYear")
            )
            or not isinstance(row.get("abstractText"), str)
            or hashlib.sha256(row["abstractText"].encode()).hexdigest() != LEADS[pmid][3]
        ):
            raise ValueError("publication or indexed abstract changed")
        papers[pmid] = {
            "reference": "PMID:" + pmid,
            "doi": "DOI:" + LEADS[pmid][0],
            "title": row["title"],
            "abstract_sha256": LEADS[pmid][3],
            "evidence_scope": "INDEXED_ABSTRACT_ONLY_NOT_PRIMARY_RESULTS_REVIEW",
            "primary_access_status": "PUBLISHER_HTTP_403_HOLD_NO_ALTERNATE_ROUTE_REQUESTED",
            "source_gene_label": "fabI",
            "source_species_name": "Staphylococcus aureus",
            "reported_context": (
                "TARGET_ALTERATION_AND_BACKGROUND_DEPENDENT_RESPONSES"
                if pmid == "24189061"
                else "MODE_OF_ACTION_AND_ACTIVITY_ACROSS_CLINICAL_BACKGROUNDS"
            ),
            "primary_results_figures_supplements_reviewed": False,
            "exact_tested_chemical_structure_or_form_verified": False,
            "experimental_allele_strain_or_genome_assignment": None,
            "raw_abstract_variants_numeric_AST_or_protocols_exported": False,
        }
    return dict(sorted(papers.items()))


def publisher_chain(doi_receipt, locator):
    headers = {k.casefold(): v for k, v in doi_receipt["headers"].items()}
    if doi_receipt["status"] != 302 or headers.get("location") != PUBLISHERS["publisher-2013"][1]:
        raise ValueError("DOI publisher destination changed")
    tree = html.fromstring(locator)
    destinations = tree.xpath('//input[@id="redirectURL"]/@value')
    if len(destinations) != 1 or unquote(destinations[0]) != PUBLISHERS["journal-2013"][1]:
        raise ValueError("publisher journal destination changed")
    return {
        "doi_resolution": "HTTP_302_INSPECTED_NO_AUTOMATIC_REDIRECT",
        "publisher_locator": "HTTP_200_LOCATOR_NOT_PRIMARY_ARTICLE",
        "journal_response": "HTTP_403_ACCESS_HOLD",
        "primary_full_text_obtained": False,
    }


def project_protein(entry, taxon):
    accession = entry.get("primaryAccession")
    if accession not in PROTEINS or {"sequence", "features", "comments"}.intersection(entry):
        raise ValueError("protein membership or payload scope changed")
    taxid, organism, locus, version = PROTEINS[accession]
    _, species = lineages.lineage(taxon)
    if (
        lineages.identity(taxon) != {"taxonId": taxid, "scientificName": organism, "rank": "strain"}
        or species != {"taxonId": 1280, "scientificName": "Staphylococcus aureus", "rank": "species"}
        or entry["organism"].get("scientificName") != organism
    ):
        raise ValueError("protein reference taxonomy changed")
    result = reference.project_reference(entry, "fabI", 1280, taxon)
    if (
        result["entry_version"] != version
        or result["sequence_version"] != 1
        or result["gene_names"] != ["fabI"]
        or result["ordered_locus_names"] != [locus]
        or result["protein_name"] != "Enoyl-[acyl-carrier-protein] reductase [NADPH] FabI"
    ):
        raise ValueError("versioned reference annotation changed")
    cited = {x["id"] for r in result["bibliography"] for x in r["identifiers"] if x["database"] == "PubMed"}
    if cited.intersection(LEADS):
        raise ValueError("selected paper citation membership changed")
    result.pop("bibliography")
    result["reference_species_taxon_id"] = result.pop("source_species_taxon_id")
    return {
        **result,
        "reference_gene": "fabI",
        "evidence_basis": "GENE_AND_SPECIES_NAME_REFERENCE_QUERY",
        "selected_paper_bibliography_matches": [],
        "experimental_genome_assignment": False,
        "compound_specific_resistance_verified": False,
        "other_drug_annotation_transferred": False,
        "database_review_status_is_primary_results_review": False,
    }


def build(root, directory=CACHE):
    directory = root / directory
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen research cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    for key in ("record", "snapshot", "census", "discovery", "source_queue", "prior_checkpoint"):
        reference.check_pin(root, cohort[key])
    current = load_record(root / cohort["record"]["path"])
    if (
        current != load_record(root / cohort["snapshot"]["path"])
        or current["identifier"] != IDENTIFIER
        or current["chemical_structure"]["standard_inchi_key"] != INCHIKEY
        or current.get("resistance_mechanisms")
    ):
        raise ValueError("selected biological record changed")
    with (root / cohort["census"]["path"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        or any(reference.digest(root / r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("corpus census or record bytes changed")
    discovery = json.loads((root / cohort["discovery"]["path"]).read_bytes())
    selected = [r for r in discovery["records"] if r["identifier"] == IDENTIFIER]
    if selected != [cohort["discovery_record"]] or selected[0]["sha256"] != cohort["record"]["sha256"]:
        raise ValueError("frozen discovery binding changed")
    leads = discovery_context(selected[0])
    sources, query_results, entries = {}, {}, []
    for key, (plan, url, status) in PUBLISHERS.items():
        sources[key] = planned_source(root, directory, key, plan, url, (status,))
    doi = json.loads((directory / "doi-2013-receipt.json").read_bytes())
    chain = publisher_chain(doi, (directory / "publisher-2013-response.bin").read_bytes())
    for key, (query, plan, count) in QUERIES.items():
        parameters = {"query": query, "format": "json", "size": 500, "fields": FIELDS}
        url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(parameters)
        sources[key] = planned_source(root, directory, key, plan, url)
        receipt = json.loads((directory / (key + "-receipt.json")).read_bytes())
        payload = json.loads((directory / (key + "-response.bin")).read_bytes())
        found = complete_query(payload, receipt["headers"], count)
        entries.extend(found)
        query_results[key] = {
            "query": query,
            "count": count,
            "release": "2026_03",
            "complete": True,
            "accessions": ["UniProtKB:" + e["primaryAccession"] for e in found],
            "zero_hits_are_protein_absence": False,
            "experimental_identity_assignment": False,
        }
    if len(entries) != 2 or {e["primaryAccession"] for e in entries} != set(PROTEINS):
        raise ValueError("reference candidate coverage changed")
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode(
        {"query": METADATA_QUERY, "format": "json", "resultType": "core", "pageSize": 2}
    )
    sources["metadata-papers"] = planned_source(root, directory, "metadata-papers", "metadata-plan.json", url)
    papers = metadata_context(json.loads((directory / "metadata-papers-response.bin").read_bytes()), leads)
    reuse_path = directory / "taxonomy-reuse.json"
    reuse = json.loads(reuse_path.read_bytes())
    if (
        reuse["cohort"] != reference.pin(root, cohort_path)
        or set(reuse["sources"]) != {"1280", "93061", "282458"}
        or reuse["new_taxonomy_requests"] != 0
        or reuse["experimental_assignments"] is not False
    ):
        raise ValueError("taxonomy reuse scope changed")
    reference.check_pin(root, reuse["lineage_checkpoint"])
    taxa = {}
    for taxid, item in reuse["sources"].items():
        taxa[taxid], sources["taxonomy-" + taxid] = lineages.native_taxon(root, item, taxid, "2026_03")
    if lineages.identity(taxa["1280"]) != {
        "taxonId": 1280,
        "scientificName": "Staphylococcus aureus",
        "rank": "species",
    }:
        raise ValueError("standalone species identity changed")
    proteins = {
        e["primaryAccession"]: project_protein(e, taxa[str(e["organism"]["taxonId"])]) for e in entries
    }
    expected_keys = set(PUBLISHERS) | set(QUERIES) | {"metadata-papers"}
    if {p.name.removesuffix("-attempt.json") for p in directory.glob("*-attempt.json")} != expected_keys:
        raise ValueError("unexpected or missing native attempt")
    return {
        "date": "2026-10-14",
        "scope": "ACCESS_HELD_PRIMARY_LEADS_AND_REFERENCE_GENES_NOT_ALLELE_CURATION",
        "cohort": reference.pin(root, cohort_path),
        "record": cohort["record"],
        "identifier": IDENTIFIER,
        "standard_inchi_key": INCHIKEY,
        "census": cohort["census"],
        "discovery": cohort["discovery"],
        "sources": sources,
        "publisher_chain_2013": chain,
        "papers": papers,
        "reference_queries": query_results,
        "reference_proteins": proteins,
        "taxonomy_reuse": reference.pin(root, reuse_path),
        "reference_species": {
            "taxon_id": "NCBITaxon:1280",
            "label": "Staphylococcus aureus",
            "rank": "species",
            "experimental_subject_assignment": False,
        },
        "curation": {
            "decision": "NO_BIOLOGICAL_WRITE_PRIMARY_RESULTS_AND_EXPERIMENTAL_IDENTITIES_UNRESOLVED",
            "exact_resistance_allele_assignment": False,
            "whole_record_primary_review": "OPEN",
        },
        "limitations": [
            "Both primary papers are publisher-access-held; abstracts and locator pages "
            "are not primary Results review.",
            "The two reference strains are not selected as tested resistant subjects; "
            "reviewed UniProt status is annotation status.",
            "Citation-query zero hits do not establish protein absence. "
            "Gene/species candidates do not establish exact alleles.",
            "Neither a clinical isolate's resistance to another drug nor an annotation "
            "for another inhibitor proves AFN-1252 resistance.",
            "Exact experimental chemical form, variant/subject joins, "
            "figures and supplements remain unresolved.",
            "No sequence, operational variant details, constructs, protocols "
            "or numerical susceptibility values are exported.",
        ],
        "limits": {
            "native_http_attempts": 8,
            "native_http_status_counts": {"200": 5, "302": 1, "403": 2},
            "reused_taxonomy_responses": 3,
            "new_taxonomy_requests": 0,
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "outreach": 0,
            "primary_results_reviews": 0,
            "biological_record_changes": 0,
            "source_adoptions": 0,
            "github_mutations": 0,
            "whole_record_signoffs": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": [
            "UniProt Consortium, UniProtKB and UniProt Taxonomy (CC BY 4.0)",
            "EMBL-EBI Europe PMC citation metadata and indexed abstracts, reference use only",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != payload:
            raise SystemExit("AFN-1252 reference checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {"references": len(result["reference_proteins"]), "primary_reviews": 0, "record_changes": 0}
        )
    )


if __name__ == "__main__":
    main()
