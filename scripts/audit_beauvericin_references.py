"""Ground reference genes while retaining the primary-source technical hold."""

import argparse
import csv
import gzip
import json
from pathlib import Path
from urllib.parse import urlencode

import audit_card_reference_lineages as lineages
import audit_stth_reference as metadata
import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-beauvericin")
OUTPUT = Path("research/2026-10-14-beauvericin-reference-context.json")
COHORT_SHA = "135215fd18e24a5934e72056627308563498deb72ea3dcd1d5b5c67029a3547d"
TAXON_NAME = "Candida albicans (strain SC5314 / ATCC MYA-2876)"
QUERIES = {
    "reference-2016": ("lit_pubmed:27736764", "reference-plan.json", 1),
    "reference-2018": ("lit_pubmed:30249688", "reference-followup-plan.json", 0),
    "reference-names": (
        "(gene_exact:YOR1 OR gene_exact:STB5) AND taxonomy_id:5476 AND reviewed:true",
        "named-reference-plan.json",
        0,
    ),
    "reference-inclusive": (
        "(gene_exact:YOR1 OR gene_exact:STB5) AND taxonomy_id:5476",
        "inclusive-reference-plan.json",
        2,
    ),
}
PROTEINS = {
    "A0A1D8PRB7": (
        "ZCF29",
        True,
        48,
        ["CAALFM_C703220CA", "orf19.12598"],
        "Zinc cluster transcription factor ZCF29",
    ),
    "Q5A926": ("STB5", False, 148, ["CAALFM_C101200WA", "orf19.10818"], "Stb5p"),
    "A0A1D8PIM2": ("YOR1", False, 45, ["CAALFM_C209990CA", "orf19.9349"], "ATP-binding cassette transporter"),
}
LEADS = {
    "27736764": ("10.1128/aac.01959-16", "PMC5119031"),
    "30249688": ("10.1128/aac.01655-18", "PMC6256747"),
    "27571477": ("10.1038/nchembio.2165", "PMC5030160"),
}


def complete_query(payload, headers, count):
    headers = {k.lower(): v for k, v in headers.items()}
    if (
        not isinstance(payload, dict)
        or not isinstance(payload.get("results"), list)
        or len(payload["results"]) != count
        or headers.get("x-total-results") != str(count)
        or headers.get("link")
        or headers.get("x-uniprot-release") != "2026_03"
    ):
        raise ValueError("reference query incomplete or malformed")
    return payload["results"]


def project_reference(entry, taxon):
    if (
        not isinstance(entry, dict)
        or entry.get("primaryAccession") not in PROTEINS
        or {"sequence", "features", "comments"}.intersection(entry)
    ):
        raise ValueError("reference membership or payload scope changed")
    gene, reviewed, version, loci, name = PROTEINS[entry["primaryAccession"]]
    if (
        lineages.identity(taxon) != {"taxonId": 237561, "scientificName": TAXON_NAME, "rank": "strain"}
        or entry["organism"].get("scientificName") != TAXON_NAME
    ):
        raise ValueError("reference taxon identity changed")
    result = reference.project_reference(entry, gene, 5476, taxon, reviewed=reviewed)
    names = [{"kind": "submissionNames", "value": name}]
    if (
        result["entry_version"] != version
        or result["sequence_version"] != 1
        or result["gene_names"] != [gene]
        or result["ordered_locus_names"] != loci
        or (result.get("protein_name") != name if reviewed else result["protein_names"] != names)
    ):
        raise ValueError("reference annotation identity changed")
    citations = {
        x["id"] for c in result["bibliography"] for x in c["identifiers"] if x["database"] == "PubMed"
    }
    selected = citations & set(LEADS)
    if selected != ({"27736764"} if reviewed else set()):
        raise ValueError("selected publication citation membership changed")
    result["reference_species_taxon_id"] = result.pop("source_species_taxon_id")
    return {
        **result,
        "reference_gene": gene,
        "discovery_basis": "PUBLICATION_CITATION" if reviewed else "TITLE_GENE_NAME_AND_SPECIES",
        "selected_publication_citations": sorted("PMID:" + p for p in selected),
        "database_review_status_is_primary_results_review": False,
        "experimental_role_or_resistance_allele_established": False,
        "other_species_YOR1_mapping_substituted": False,
    }


def discovery_context(row):
    queries = row.get("queries", [])
    ids = row.get("candidate_ids", [])
    if (
        row.get("identifier") != "CHEBI:3000"
        or len(ids) != len(set(ids))
        or len(ids) != 58
        or len(queries) != 2
    ):
        raise ValueError("complete discovery cohort changed")
    candidates = []
    for query in queries:
        entries = query.get("candidates", [])
        if (
            query.get("hit_count") != 58
            or query.get("next_cursor") is not None
            or query.get("request", {}).get("status") != 200
            or len(entries) != 58
            or sorted(c["source"] + ":" + c["id"] for c in entries) != sorted(ids)
        ):
            raise ValueError("discovery request incomplete or membership changed")
        candidates.append({c["source"] + ":" + c["id"]: c for c in entries})
    if candidates[0] != candidates[1]:
        raise ValueError("canonical and alias candidate metadata differ")
    selected = {}
    for pmid, (doi, pmcid) in LEADS.items():
        entry = candidates[0].get("MED:" + pmid, {})
        if entry.get("pmid") != pmid or entry.get("doi") != doi or entry.get("pmcid") != pmcid:
            raise ValueError("selected publication identity changed")
        selected[pmid] = {
            **entry,
            "primary_review_status": "TECHNICAL_HTTP_500_HOLD"
            if pmid == "27736764"
            else "UNREQUESTED_AFTER_PRIMARY_CANARY_ERROR",
        }
    return {
        "candidate_identities": 58,
        "retained_candidate_ids": sorted(ids),
        "completed_queries": 2,
        "selected_leads": selected,
        "primary_results_reviews": 0,
        "primary_results_unreviewed_candidates": 58,
        "primary_requests_this_pass": 1,
        "primary_candidates_not_requested_this_pass": 57,
        "duplicate_query_memberships_are_independent_evidence": False,
        "title_gene_mentions_establish_resistance_alleles": False,
    }


def build(root, directory=CACHE):
    directory = root / directory
    keys = {"article-2016"} | set(QUERIES)
    if any(
        {p.name.removesuffix(s) for p in directory.glob("*" + s)} != keys
        for s in ("-receipt.json", "-attempt.json")
    ):
        raise ValueError("research request coverage changed")
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen beauvericin cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    protected = json.loads(reference.check_pin(root, cohort["protected"]).read_bytes())
    reference.check_pin(root, cohort["source_queue"])
    discovery = json.loads(gzip.decompress(reference.check_pin(root, cohort["discovery"]).read_bytes()))
    rows = [r for r in discovery["records"] if r["identifier"] == "CHEBI:3000"]
    if len(rows) != 1 or rows[0] != cohort["discovery_record"]:
        raise ValueError("pinned discovery row changed")
    discovery_result = discovery_context(rows[0])
    record = load_record(reference.check_pin(root, cohort["snapshot"]))
    if (
        record["identifier"] != cohort["identifier"]
        or record["label"] != cohort["label"]
        or record["chemical_structure"]["standard_inchi_key"] != cohort["standard_inchi_key"]
        or record.get("resistance_mechanisms")
        or cohort["record"]["sha256"] != rows[0]["sha256"]
        or cohort["snapshot"]["sha256"] != cohort["record"]["sha256"]
    ):
        raise ValueError("historical compound identity changed")
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or any(protected.get(r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("complete corpus preflight changed")
    sources = {
        "article-2016": planned_source(
            root,
            directory,
            "article-2016",
            "request-plan.json",
            "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5119031/fullTextXML",
            (500,),
        )
    }
    query_rows = {}
    for key, (query, plan, count) in QUERIES.items():
        url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
            {
                "query": query,
                "format": "json",
                "size": "500",
                "fields": metadata.FIELDS,
            }
        )
        sources[key] = planned_source(root, directory, key, plan, url)
        receipt = json.loads(reference.check_pin(root, sources[key]["receipt"]).read_bytes())
        payload = json.loads(reference.check_pin(root, sources[key]["body"]).read_bytes())
        query_rows[key] = complete_query(payload, receipt["headers"], count)

    def plan(key):
        return json.loads(reference.check_pin(root, sources[key]["plan"]).read_bytes())

    if any(plan(k).get("cohort") != reference.pin(root, cohort_path) for k in sources):
        raise ValueError("request cohort binding changed")
    hold_pin = reference.pin(root, directory / "primary-hold.json")
    hold = json.loads(reference.check_pin(root, hold_pin).read_bytes())
    error = json.loads(reference.check_pin(root, sources["article-2016"]["body"]).read_bytes())
    if (
        error.get("status") != 500
        or error.get("error") != "Internal Server Error"
        or error.get("path") != "/europepmc/webservices/rest/PMC5119031/fullTextXML"
        or hold.get("disposition") != "TECHNICAL_HTTP_500_HOLD"
        or hold.get("source") != {k: sources["article-2016"][k] for k in ("body", "receipt")}
        or hold.get("primary_results_reviewed") is not False
        or hold.get("retry_or_alternate_route") is not False
        or hold.get("remaining_primary_candidates_not_requested_after_canary_error")
        != ["PMID:30249688", "PMID:27571477"]
        or any(plan(k).get("primary_access_hold") != hold_pin for k in QUERIES)
    ):
        raise ValueError("primary technical hold provenance changed")
    review_pin = reference.pin(root, directory / "reference-2016-reviewed.json")
    review = json.loads(reference.check_pin(root, review_pin).read_bytes())
    followup = plan("reference-2018")
    selected2018 = {
        k: v
        for k, v in discovery_result["selected_leads"]["30249688"].items()
        if k != "primary_review_status"
    }
    if (
        followup.get("canary_review") != review_pin
        or review.get("source") != {k: sources["reference-2016"][k] for k in ("body", "receipt")}
        or review.get("primary_results_reviewed") is not False
        or followup.get("selected_citation") != selected2018
        or plan("reference-names").get("discovery_title_lead") != selected2018
        or plan("reference-names").get("completed_citation_query") != sources["reference-2018"]["receipt"]
        or plan("reference-names").get("prior_other_species_YOR1_queries_not_retried_or_substituted")
        is not True
        or plan("reference-inclusive").get("prior_name_plan") != sources["reference-names"]["plan"]
        or plan("reference-inclusive").get("completed_reviewed_only_query")
        != sources["reference-names"]["receipt"]
    ):
        raise ValueError("reference canary or scope follow-up provenance changed")
    checkpoint = followup["taxonomy_checkpoint"]
    if reference.digest(reference.check_pin(root, checkpoint)) != protected[checkpoint["path"]]:
        raise ValueError("prior taxonomy checkpoint changed")
    old_taxon = json.loads(reference.check_pin(root, checkpoint).read_bytes())["taxonomy"]["237561"]
    native = followup["reused_taxonomy"]
    if native["body"] != {
        "path": old_taxon["request"]["cache_path"],
        "sha256": old_taxon["request"]["sha256"],
    }:
        raise ValueError("native taxonomy reuse binding changed")
    taxon, taxonomy_source = lineages.native_taxon(root, native, "237561", "2026_03")
    if {e.get("primaryAccession") for e in query_rows["reference-2016"]} != {"A0A1D8PRB7"} or {
        e.get("primaryAccession") for e in query_rows["reference-inclusive"]
    } != {"Q5A926", "A0A1D8PIM2"}:
        raise ValueError("reference query membership changed")
    proteins = sorted(
        [
            project_reference(e, taxon)
            for k in ("reference-2016", "reference-inclusive")
            for e in query_rows[k]
        ],
        key=lambda p: p["reference_gene"],
    )
    return {
        "date": "2026-10-14",
        "scope": "REFERENCE_GENE_GROUNDING_NOT_PRIMARY_RESULTS_OR_ALLELE_CURATION",
        "baseline_commit": cohort["baseline_commit"],
        "cohort": reference.pin(root, cohort_path),
        "record": {
            **cohort["record"],
            "identifier": cohort["identifier"],
            "label": cohort["label"],
            "standard_inchi_key": cohort["standard_inchi_key"],
            "historical_snapshot": cohort["snapshot"],
        },
        "census": cohort["census"],
        "corpus_records_hash_checked_at_preflight": len(census),
        "discovery": discovery_result,
        "sources": sources,
        "primary_hold": hold_pin,
        "reference_canary_review": review_pin,
        "reference_proteins": proteins,
        "taxonomy_source": taxonomy_source,
        "taxonomy_checkpoint": checkpoint,
        "query_interpretation": {
            "complete_result_counts": {k: len(v) for k, v in query_rows.items()},
            "empty_citation_or_reviewed_query_establishes_gene_absence": False,
            "unreviewed_entries_promoted_to_reviewed": False,
            "genome_citations_are_compound_specific_resistance_validation": False,
            "same_strain_reference_is_experimental_subject_assignment": False,
        },
        "curation_decision": "NO_NEW_RESISTANCE_ASSERTION_OR_EXPERIMENTAL_IDENTIFIERS",
        "limits": {
            "http_attempts": 5,
            "primary_results_reviews": 0,
            "primary_2016_disposition": "TECHNICAL_HTTP_500_HOLD",
            "primary_2018_and_other_2016_study_requested": False,
            "native_taxonomy_responses_reused": 1,
            "automatic_redirects": 0,
            "retries": 0,
            "biological_records_changed": 0,
            "figures_visually_reviewed": False,
            "supplements_reviewed": False,
            "numeric_AST_variants_sequences_constructs_or_protocols_exported": False,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "source_adoptions": 0,
            "reuse_terms_review_resumed": False,
            "issue_1040": "DEFERRED",
            "whole_record_primary_review": "OPEN",
            "full_corpus_goal_status": "OPEN",
        },
        "reference_attribution": {
            "source": "UniProt Consortium",
            "release": "2026_03",
            "license": "CC BY 4.0",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != payload:
            raise SystemExit("Beauvericin reference checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {
                "reference_genes": 3,
                "reviewed_entries": 1,
                "unreviewed_entries": 2,
                "primary_access_holds": 1,
                "new_resistance_assertions": 0,
            }
        )
    )


if __name__ == "__main__":
    main()
