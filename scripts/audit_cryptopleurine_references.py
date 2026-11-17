"""Resolve historical CRY paralogs without turning reference proteins into alleles."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode

import audit_card_reference_lineages as lineages
import audit_topoisomerase_references as reference
from audit_beauvericin_references import complete_query
from audit_ciclopirox_context import title
from audit_stth_reference import FIELDS
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-cryptopleurine")
OUTPUT = Path("research/2026-10-14-cryptopleurine-reference-context.json")
COHORT_SHA = "2f72741be73f830f3527bd2a892af437e4fba2aa454cba518d8c2325e157548d"
ARTICLE = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1205715/fullTextXML"
METADATA_QUERY = "EXT_ID:8293976 AND SRC:MED"
ABSTRACT_SHA = "3d4dfefc3991638c7f7fb920a70014f749b1bd7b4a2861468319e916b7e63493"
TAXON_NAME = "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)"
STRUCTURES = {
    "CHEBI:3932": ("antiviral/cryptopleurine", "RSHYSOGXGSUUIJ-OAHLLOKOSA-N", 19, 2),
    "CHEBI:4781": ("antiprotozoal/emetine", "AUVVAXYIELKVAI-CKBKHPSWSA-N", 95, 3),
}
LEADS = {
    "8293976": ("10.1093/genetics/135.3.719", "PMC1205715", "1993"),
    "3037334": ("10.1128/mcb.7.5.1764-1775.1987", "PMC365278", "1987"),
}
PROTEINS = {
    "P06367": (
        "RPS14A",
        "CRY1",
        ["CRY1", "RPL59", "RPS14A"],
        "YCR031C",
        "YCR31C",
        222,
        5,
        "Small ribosomal subunit protein uS11A",
        ["40S ribosomal protein S14-A", "RP59A"],
        "3037334",
    ),
    "P39516": (
        "RPS14B",
        "CRY2",
        ["CRY2", "RPS14B"],
        "YJL191W",
        "J0354",
        198,
        2,
        "Small ribosomal subunit protein uS11B",
        ["40S ribosomal protein S14-B", "RP59B"],
        "8293976",
    ),
}


def discovery_context(rows):
    if len(rows) != 2 or {r["identifier"] for r in rows} != set(STRUCTURES):
        raise ValueError("discovery compound membership changed")
    leads, memberships, all_ids = {}, {p: [] for p in LEADS}, set()
    for row in rows:
        _, _, count, queries = STRUCTURES[row["identifier"]]
        ids = row["candidate_ids"]
        if len(ids) != count or len(set(ids)) != count or len(row["queries"]) != queries:
            raise ValueError("discovery counts changed")
        observed = set()
        for query in row["queries"]:
            candidates = query["candidates"]
            keys = [c["source"] + ":" + c["id"] for c in candidates]
            if (
                type(query["hit_count"]) is not int
                or query["hit_count"] != len(candidates)
                or len(keys) != len(set(keys))
                or query["next_cursor"] is not None
                or query["request"]["status"] != 200
            ):
                raise ValueError("discovery query incomplete or duplicated")
            observed.update(keys)
            for candidate in candidates:
                pmid = candidate["id"]
                if candidate["source"] != "MED" or pmid not in LEADS:
                    continue
                doi, pmcid, year = LEADS[pmid]
                if (
                    candidate.get("pmid") != pmid
                    or candidate.get("doi") != doi
                    or candidate.get("pmcid") != pmcid
                    or candidate.get("pubYear") != year
                    or (pmid in leads and leads[pmid] != candidate)
                ):
                    raise ValueError("selected publication identity changed")
                leads[pmid] = candidate
                memberships[pmid].append(row["identifier"])
        if observed != set(ids):
            raise ValueError("discovery candidate union changed")
        all_ids.update(ids)
    if memberships != {"8293976": ["CHEBI:3932"], "3037334": ["CHEBI:4781", "CHEBI:4781", "CHEBI:3932"]}:
        raise ValueError("selected publication memberships changed")
    return {
        "selected_leads": leads,
        "selected_query_memberships": memberships,
        "distinct_retained_candidates": len(all_ids),
        "all_candidates_primary_reviewed": False,
        "query_membership_establishes_compound_specific_evidence": False,
    }


def metadata_context(payload, lead):
    request = payload.get("request", {})
    rows = payload.get("resultList", {}).get("result")
    if (
        type(payload.get("hitCount")) is not int
        or payload["hitCount"] != 1
        or not isinstance(rows, list)
        or len(rows) != 1
        or request.get("queryString") != METADATA_QUERY
        or request.get("internalQuery") != METADATA_QUERY
        or request.get("resultType") != "CORE"
        or type(request.get("pageSize")) is not int
        or request["pageSize"] != 1
        or payload.get("nextCursorMark")
    ):
        raise ValueError("metadata query identity or completeness changed")
    row = rows[0]
    if (
        any(row.get(k) != lead[k] for k in ("id", "source", "pmid", "pmcid", "doi", "title", "pubYear"))
        or not isinstance(row.get("abstractText"), str)
        or hashlib.sha256(row["abstractText"].encode()).hexdigest() != ABSTRACT_SHA
        or any(
            marker not in row["abstractText"]
            for marker in ("CRY1", "CRY2", "cryptopleurine", "Saccharomyces cerevisiae")
        )
        or {k: row.get(k) for k in ("isOpenAccess", "inEPMC", "inPMC")}
        != {"isOpenAccess": "N", "inEPMC": "Y", "inPMC": "Y"}
    ):
        raise ValueError("indexed publication or reviewed abstract changed")
    return {
        "reference": "PMID:8293976",
        "doi": "DOI:" + LEADS["8293976"][0],
        "abstract_sha256": hashlib.sha256(row["abstractText"].encode()).hexdigest(),
        "scope": "INDEXED_ABSTRACT_ONLY_NOT_PRIMARY_RESULTS_REVIEW",
        "source_gene_labels": ["CRY1", "CRY2"],
        "source_species": "Saccharomyces cerevisiae",
        "paralog_and_expression_background_dependence_reported": True,
        "single_gene_effect_inferred_from_combined_background": False,
        "primary_results_figures_supplements_reviewed": False,
        "tested_chemical_structure_or_form_verified": False,
        "experimental_allele_strain_or_genome_assignment": None,
        "numeric_AST_or_abstract_text_exported": False,
        "source_use": "REFERENCE_ONLY_NO_SOURCE_ADOPTION",
    }


def project_protein(entry, taxon, leads):
    if entry.get("primaryAccession") not in PROTEINS or {"sequence", "features", "comments"}.intersection(
        entry
    ):
        raise ValueError("reference membership or payload scope changed")
    gene, alias, names, locus, orf, version, seqversion, protein, alternatives, pmid = PROTEINS[
        entry["primaryAccession"]
    ]
    _, species = lineages.lineage(taxon)
    if (
        lineages.identity(taxon) != {"taxonId": 559292, "scientificName": TAXON_NAME, "rank": "strain"}
        or species != {"taxonId": 4932, "scientificName": "Saccharomyces cerevisiae", "rank": "species"}
        or entry["organism"].get("scientificName") != TAXON_NAME
        or len(entry.get("genes", [])) != 1
        or entry["genes"][0].get("geneName", {}).get("value") != gene
    ):
        raise ValueError("primary gene name or reference taxonomy changed")
    result = reference.project_reference(entry, gene, 4932, taxon)
    orfs = [v["value"] for v in entry["genes"][0].get("orfNames", [])]
    native_alternatives = sorted(
        a["fullName"]["value"] for a in entry["proteinDescription"].get("alternativeNames", [])
    )
    if (
        result["gene_names"] != names
        or result["ordered_locus_names"] != [locus]
        or orfs != [orf]
        or result["entry_version"] != version
        or result["sequence_version"] != seqversion
        or result["protein_name"] != protein
        or native_alternatives != alternatives
    ):
        raise ValueError("versioned gene, locus or protein name changed")
    selected = []
    for item in entry.get("references", []):
        citation = item.get("citation", {})
        ids = citation.get("citationCrossReferences", [])
        matched = [i["id"] for i in ids if i["database"] == "PubMed" and i["id"] in LEADS]
        if not matched:
            continue
        if (
            matched != [pmid]
            or citation.get("id") != pmid
            or citation.get("citationType") != "journal article"
            or [i["id"].lower() for i in ids if i["database"] == "DOI"] != [LEADS[pmid][0]]
            or title(citation.get("title", "")) != title(leads[pmid]["title"])
            or citation.get("publicationDate") != LEADS[pmid][2]
            or item.get("referencePositions") != ["NUCLEOTIDE SEQUENCE [GENOMIC DNA]"]
            or item.get("referenceComments")
        ):
            raise ValueError("same-citation identity or annotation scope changed")
        selected.append(pmid)
    if selected != [pmid]:
        raise ValueError("selected citation missing or duplicated")
    result.pop("bibliography")
    result["reference_species_taxon_id"] = result.pop("source_species_taxon_id")
    return {
        **result,
        "reference_gene": gene,
        "source_gene_alias": alias,
        "gene_orf_names": orfs,
        "alternative_protein_names": alternatives,
        "selected_citation": "PMID:" + pmid,
        "selected_citation_scope": "SEQUENCE_ANNOTATION_NOT_RESISTANCE_PHENOTYPE_PROOF",
        "role": "PARALOG_REFERENCE_NOT_TESTED_RESISTANT_ALLELE",
        "experimental_genome_assignment": None,
        "compound_specific_resistance_verified": False,
    }


def build(root, directory=CACHE):
    directory = root / directory
    keys = {"article-1993", "reference-1993", "metadata-1993", "reference-1987"}
    if any(
        {p.name.removesuffix(s) for p in directory.glob("*" + s)} != keys
        for s in ("-attempt.json", "-receipt.json", "-response.bin")
    ):
        raise ValueError("request inventory changed")
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    protected = json.loads(reference.check_pin(root, cohort["protected"]).read_bytes())
    for key in ("source_queue", "prior_checkpoint"):
        reference.check_pin(root, cohort[key])
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or any(protected.get(r["path"]) != r["record_sha256"] for r in census)
        or len(cohort["records"]) != 2
        or {r["identifier"] for r in cohort["records"]} != set(STRUCTURES)
    ):
        raise ValueError("corpus baseline changed")
    for row in cohort["records"]:
        record = load_record(reference.check_pin(root, row["snapshot"]))
        slug, key, _, _ = STRUCTURES[row["identifier"]]
        if (
            record["identifier"] != row["identifier"]
            or record["label"] != row["label"]
            or record["chemical_structure"]["standard_inchi_key"] != key
            or row["standard_inchi_key"] != key
            or row["record"]["path"] != f"data/antibiotics/{slug}.yaml"
            or row["snapshot"]["sha256"] != row["record"]["sha256"]
            or protected.get(row["record"]["path"]) != row["record"]["sha256"]
            or record.get("resistance_mechanisms")
            or record.get("genotype_resistance_score_rules")
        ):
            raise ValueError("historical exact-structure record changed")
    data = json.loads(reference.check_pin(root, cohort["discovery"]).read_bytes())
    rows = [r for r in data["records"] if r["identifier"] in STRUCTURES]
    if rows != cohort["discovery_records"] or any(r["sha256"] != protected.get(r["path"]) for r in rows):
        raise ValueError("discovery baseline binding changed")
    discovery = discovery_context(rows)
    metadata_url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode(
        {"query": METADATA_QUERY, "resultType": "core", "format": "json", "pageSize": 1}
    )
    requests = [
        ("article-1993", "request-plan.json", ARTICLE, (500,)),
        ("metadata-1993", "metadata-plan.json", metadata_url, (200,)),
    ]
    for year, pmid, plan in (
        ("1993", "8293976", "reference-plan.json"),
        ("1987", "3037334", "reference-followup-plan.json"),
    ):
        url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
            {"query": "lit_pubmed:" + pmid, "format": "json", "size": 500, "fields": FIELDS}
        )
        requests.append(("reference-" + year, plan, url, (200,)))
    sources, plans = {}, {}
    for key, filename, url, statuses in requests:
        source = planned_source(root, directory, key, filename, url, statuses)
        plan = json.loads(reference.check_pin(root, source["plan"]).read_bytes())
        if (
            plan.get("cohort") != reference.pin(root, cohort_path)
            or set(plan["requests"]) != {key}
            or plan["requests"][key].get("canary") is not True
            or plan.get("ncbi_requests") != 0
            or any(
                plan.get(flag) is not False
                for flag in ("automatic_redirects", "retry_performed", "prior_source_holds_retried")
            )
        ):
            raise ValueError("request plan scope changed")
        sources[key], plans[key] = source, plan
    error = json.loads(reference.check_pin(root, sources["article-1993"]["body"]).read_bytes())
    if (
        error.get("status") != 500
        or error.get("error") != "Internal Server Error"
        or error.get("path") != "/europepmc/webservices/rest/PMC1205715/fullTextXML"
        or any(
            plans[k].get("primary_receipt") != sources["article-1993"]["receipt"]
            for k in ("reference-1993", "metadata-1993")
        )
    ):
        raise ValueError("primary hold binding changed")
    metadata = metadata_context(
        json.loads(reference.check_pin(root, sources["metadata-1993"]["body"]).read_bytes()),
        discovery["selected_leads"]["8293976"],
    )
    followup = plans["reference-1987"]
    checkpoint = json.loads(reference.check_pin(root, followup["taxonomy_checkpoint"]).read_bytes())
    old_tax = checkpoint["sources"]["host-taxonomy-reused"]
    if (
        followup["taxonomy_checkpoint"]["sha256"] != protected.get(followup["taxonomy_checkpoint"]["path"])
        or followup["reused_taxonomy"] != {"body": old_tax["cache"], "receipt": old_tax["receipt"]}
        or followup.get("canary_body") != sources["reference-1993"]["body"]
        or followup.get("canary_receipt") != sources["reference-1993"]["receipt"]
        or followup.get("metadata") != sources["metadata-1993"]["body"]
    ):
        raise ValueError("reference canary or taxonomy reuse changed")
    taxon, tax_source = lineages.native_taxon(root, followup["reused_taxonomy"], "559292", "2026_03")
    proteins = []
    for key, accession in (("reference-1987", "P06367"), ("reference-1993", "P39516")):
        source = sources[key]
        payload = json.loads(reference.check_pin(root, source["body"]).read_bytes())
        headers = json.loads(reference.check_pin(root, source["receipt"]).read_bytes())["headers"]
        proteins.append(project_query(payload, headers, taxon, discovery["selected_leads"], accession))
    return {
        "date": "2026-10-14",
        "scope": "HISTORICAL_PARALOG_REFERENCE_CROSSWALK_NOT_ALLELE_CURATION",
        "cohort": reference.pin(root, cohort_path),
        "baseline_commit": cohort["baseline_commit"],
        "records": cohort["records"],
        "census": cohort["census"],
        "discovery": discovery,
        "sources": sources,
        "primary_1993_status": "TECHNICAL_HTTP_500_HOLD",
        "primary_1987_status": "UNREQUESTED",
        "technical_error_is_negative_biological_evidence": False,
        "indexed_context": metadata,
        "reference_proteins": proteins,
        "taxonomy_source": tax_source,
        "paralogs_equated_or_substituted": False,
        "chemical_scope": {
            "cryptopleurine_and_emetine_kept_distinct": True,
            "findings_transferred_between_compounds_or_salts": False,
            "tested_exact_structure_verified": False,
        },
        "curation_decision": "RETAIN_REFERENCE_DOSSIER_NO_RESISTANCE_OR_ACTIVITY_RECORD_WRITE",
        "limits": {
            "native_scientific_http_attempts": 4,
            "native_http_status_counts": {"200": 3, "500": 1},
            "domain_restricted_web_searches": 1,
            "new_taxonomy_requests": 0,
            "native_taxonomy_responses_reused": 1,
            "primary_results_reviews": 0,
            "biological_records_changed": 0,
            "whole_record_primary_signoffs": 0,
            "numeric_AST_sequences_variants_constructs_or_protocols_exported": False,
            "new_experimental_allele_strain_or_genome_assignments": 0,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "prior_source_holds_preserved": True,
            "retries": 0,
            "automatic_redirects": 0,
            "source_adoptions": 0,
            "github_mutations": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": {"source": "UniProt Consortium", "license": "CC BY 4.0", "release": "2026_03"},
    }


def project_query(payload, headers, taxon, leads, expected_accession):
    entries = complete_query(payload, headers, 1)
    if entries[0].get("primaryAccession") != expected_accession:
        raise ValueError("citation query returned another paralog")
    return project_protein(entries[0], taxon, leads)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != payload:
            raise SystemExit("Cryptopleurine reference checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {
                "reference_proteins": len(result["reference_proteins"]),
                "primary_status": result["primary_1993_status"],
                "records_changed": 0,
            }
        )
    )


if __name__ == "__main__":
    main()
