"""Keep same-symbol, same-species SttH references distinct across publications."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode

import audit_card_reference_lineages as lineages
import audit_stth_reference as prior_audit
import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import planned_source

CACHE = Path("reports/resistance-grounding-2026-10-14-stth-followup")
OUTPUT = Path("research/2026-10-14-stth-followup-context.json")
COHORT_SHA = "8543ab6ccd2fd4e02282e0d932e6bacc7e0259ba50e15fa9d82ed4c2944ae79d"
DOI = "10.1271/bbb.90499"
PUBLISHER = "https://academic.oup.com/bbb/article/73/11/2494-2500/5947804"
VERSIONS = {
    "Q1MW86": (58, 2),
    "C5NU54": (41, 1),
    "C5NU51": (51, 1),
    "C5NU50": (46, 1),
    "C5NU55": (53, 1),
    "C5NU48": (38, 1),
    "C5NU49": (35, 1),
    "C5NU52": (15, 1),
    "C5NU53": (19, 1),
}
GENES = {"Q1MW86": ["sttH"], "C5NU54": ["sttH", "sttH-sn"]}


def project_references(payload, headers, taxonomy):
    headers = {key.lower(): value for key, value in headers.items()}
    if (
        not isinstance(payload, dict)
        or not isinstance(payload.get("results"), list)
        or len(payload["results"]) != 9
        or not all(isinstance(row, dict) for row in payload["results"])
        or headers.get("x-total-results") != "9"
        or headers.get("link")
        or headers.get("x-uniprot-release") != "2026_03"
    ):
        raise ValueError("publication query incomplete or malformed")
    rows = payload["results"]
    if {row.get("primaryAccession") for row in rows} != set(VERSIONS):
        raise ValueError("publication reference membership changed")
    name = prior_audit.synonym_scope(taxonomy)
    selected, shared = [], []
    for entry in rows:
        accession = entry["primaryAccession"]
        reviewed = accession in GENES
        kind = "UniProtKB reviewed (Swiss-Prot)" if reviewed else "UniProtKB unreviewed (TrEMBL)"
        versions, organism = entry.get("entryAudit", {}), entry.get("organism", {})
        if (
            {"sequence", "features", "comments"}.intersection(entry)
            or entry.get("entryType") != kind
            or not isinstance(versions, dict)
            or any(type(versions.get(k)) is not int for k in ("entryVersion", "sequenceVersion"))
            or (versions["entryVersion"], versions["sequenceVersion"]) != VERSIONS[accession]
            or not isinstance(organism, dict)
            or type(organism.get("taxonId")) is not int
            or organism["taxonId"] != 1971
            or organism.get("scientificName") != taxonomy["scientificName"]
        ):
            raise ValueError("reference metadata or payload scope changed")
        citations = [
            r.get("citation", {}).get("citationCrossReferences", []) for r in entry.get("references", [])
        ]
        wanted = {("PubMed", "19897889"), ("DOI", DOI)}
        if not any(
            wanted <= {(r["database"], r["id"].lower() if r["database"] == "DOI" else r["id"]) for r in refs}
            for refs in citations
        ):
            raise ValueError("shared publication identity changed")
        if reviewed:
            result = reference.project_reference(entry, "sttH", 1971, taxonomy)
            if (
                result["gene_names"] != GENES[accession]
                or result["protein_name"] != "Streptothricin hydrolase"
            ):
                raise ValueError("focal reference identity changed")
            result["reference_species_taxon_id"] = result.pop("source_species_taxon_id")
            selected.append(
                {
                    **result,
                    "role": "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE",
                    "primary_results_reviewed": False,
                }
            )
        else:
            shared.append(
                {
                    "accession": "UniProtKB:" + accession,
                    "entry_type": kind,
                    "entry_version": versions["entryVersion"],
                    "sequence_version": versions["sequenceVersion"],
                    "reference_taxon_id": "NCBITaxon:1971",
                    "role": "SHARED_CITATION_NOT_SELECTED_AS_RESISTANCE_DETERMINANT",
                    "resistance_absence_inferred": False,
                }
            )
    return {
        "query_complete": True,
        "entries_checked": 9,
        "release": "2026_03",
        "selected_references": sorted(selected, key=lambda row: row["protein_accession"]),
        "other_citation_entries": sorted(shared, key=lambda row: row["accession"]),
        "name_resolution": name,
        "shared_citation_is_causality": False,
        "same_symbol_or_species_establishes_same_locus_or_allele": False,
        "reference_accessions_merged": False,
        "protein_versions_equated_to_experimental_alleles": False,
    }


def build(root, directory=CACHE):
    directory = root / directory
    keys = {"primary-doi", "primary-publisher", "reference-2009"}
    if any(
        {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} != keys
        for suffix in ("-receipt.json", "-attempt.json")
    ):
        raise ValueError("research request coverage changed")
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen research cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    for key in ("prior", "census", "protected", "discovery", "source_queue"):
        reference.check_pin(root, cohort[key])
    prior = json.loads(reference.check_pin(root, cohort["prior"]).read_bytes())
    if prior != prior_audit.build(root) or cohort["records"] != prior["records"]:
        raise ValueError("prior reference checkpoint or exact-structure cohort changed")
    protected = json.loads(reference.check_pin(root, cohort["protected"]).read_bytes())
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or any(protected.get(r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("complete corpus preflight changed")
    discovery = json.loads(reference.check_pin(root, cohort["discovery"]).read_bytes())
    if (
        discovery["status"] != 200
        or hashlib.sha256(discovery["body"].encode()).hexdigest() != discovery["sha256"]
    ):
        raise ValueError("discovery metadata receipt changed")
    matches = [
        r for r in json.loads(discovery["body"])["resultList"]["result"] if r.get("pmid") == "19897889"
    ]
    if matches != [cohort["selected_citation"]] or matches[0].get("doi") != DOI:
        raise ValueError("distinct follow-up publication identity changed")
    query = {"query": "lit_pubmed:19897889", "format": "json", "size": "500", "fields": prior_audit.FIELDS}
    urls = {
        "primary-doi": "https://doi.org/" + DOI,
        "primary-publisher": PUBLISHER,
        "reference-2009": "https://rest.uniprot.org/uniprotkb/search?" + urlencode(query),
    }
    sources = {
        key: planned_source(root, directory, key, "request-plan.json", urls[key], (status,))
        for key, status in (("primary-doi", 302), ("reference-2009", 200))
    }
    sources["primary-publisher"] = planned_source(
        root, directory, "primary-publisher", "primary-publisher-plan.json", PUBLISHER, (403,)
    )
    redirect = json.loads(reference.check_pin(root, sources["primary-doi"]["receipt"]).read_bytes())
    plan = json.loads(reference.check_pin(root, sources["primary-publisher"]["plan"]).read_bytes())
    if (
        {k.lower(): v for k, v in redirect["headers"].items()}.get("location") != PUBLISHER
        or plan.get("manual_redirect_reviewed") is not True
        or plan.get("redirect_receipt") != sources["primary-doi"]["receipt"]
    ):
        raise ValueError("manual publisher redirect provenance changed")
    taxon, tax_source = lineages.native_taxon(root, prior["reference_taxonomy"], "1971", "2026_03")
    payload = json.loads(reference.check_pin(root, sources["reference-2009"]["body"]).read_bytes())
    receipt = json.loads(reference.check_pin(root, sources["reference-2009"]["receipt"]).read_bytes())
    proteins = project_references(payload, receipt["headers"], taxon)
    (shared,) = [r for r in proteins["selected_references"] if r["protein_accession"] == "UniProtKB:Q1MW86"]
    if shared != prior["reference_context"]["selected_reference"]:
        raise ValueError("shared protein reference changed between publication queries")
    return {
        "date": "2026-10-14",
        "scope": "DISTINCT_PUBLICATION_REFERENCE_FOLLOWUP_NOT_EXPERIMENTAL_GROUNDING",
        "cohort": reference.pin(root, cohort_path),
        "baseline_commit": cohort["baseline_commit"],
        "census": cohort["census"],
        "corpus_records_hash_checked_at_preflight": len(census),
        "prior_reference_checkpoint": cohort["prior"],
        "records": cohort["records"],
        "sources": sources,
        "reference_context": proteins,
        "reference_retrieved_at": receipt["retrieved_at"],
        "reference_taxonomy": tax_source,
        "reference_comparison": {
            "retained_prior_reference": "UniProtKB:Q1MW86",
            "additional_reference_relative_to_prior_checkpoint": "UniProtKB:C5NU54",
            "shared_reference_projection_identical": True,
            "shared_species_taxon_id": "NCBITaxon:1971",
            "experimental_subjects_equated": False,
            "chemical_scope_holds_preserved": True,
        },
        "primary_access": {
            "reference": "PMID:19897889",
            "doi": "DOI:" + DOI,
            "terminal_status": 403,
            "disposition": "ACCESS_HOLD",
            "primary_results_reviewed": False,
            "retry_or_alternate_route_attempted": False,
            "distinct_study_not_alternate_copy_of_held_2006_paper": True,
        },
        "curation_decision": "NO_NEW_RESISTANCE_ASSERTION_OR_EXPERIMENTAL_IDENTIFIER",
        "limits": {
            "scientific_http_attempts": len(keys),
            "manually_inspected_redirect_hops": 1,
            "retries": 0,
            "automatic_redirects": 0,
            "native_taxonomy_responses_reused": 1,
            "biological_records_changed": 0,
            "experimental_allele_assignments": 0,
            "experimental_genome_assignments": 0,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "numeric_AST_variants_sequences_constructs_or_protocols_exported": False,
            "issue_1040": "DEFERRED",
            "source_adoptions": 0,
            "reuse_terms_review_resumed": False,
            "held_2006_and_2017_primary_studies_not_retried": True,
            "whole_record_primary_review": "OPEN",
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": {"source": "UniProt Consortium", "license": "CC BY 4.0", "release": "2026_03"},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != payload:
            raise SystemExit("SttH follow-up checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {
                "publication_entries_checked": 9,
                "focal_reference_candidates": 2,
                "shared_citation_entries_not_promoted": 7,
                "new_resistance_assertions": 0,
            }
        )
    )


if __name__ == "__main__":
    main()
