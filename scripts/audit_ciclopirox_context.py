"""Keep citation-linked induction references separate from resistance evidence."""

import argparse
import csv
import gzip
import json
from html import unescape
from pathlib import Path
from urllib.parse import urlencode

import audit_card_reference_lineages as lineages
import audit_topoisomerase_references as reference
from audit_beauvericin_references import complete_query
from audit_stth_reference import FIELDS
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-ciclopirox")
OUTPUT = Path("research/2026-10-14-ciclopirox-context.json")
COHORT_SHA = "da38d4415269e4212984e1713d6ae4f10acfef213ef4547322c5092997be93fe"
ARTICLE = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC155814/fullTextXML"
TAXON_NAME = "Candida albicans (strain SC5314 / ATCC MYA-2876)"
STRUCTURES = {
    "CHEBI:31398": ("ciclopirox-olamine", "HKUKJIQHPXYJTP-UHFFFAOYSA-O"),
    "CHEBI:453011": ("ciclopirox", "SCKYRAXSEDYPSA-UHFFFAOYSA-N"),
}
LEADS = {
    "12760852": ("10.1128/aac.47.6.1805-1817.2003", "PMC155814"),
    "15790671": ("10.1093/jac/dki089", None),
    "15814599": ("10.1093/jac/dki105", None),
}
QUERIES = {
    "reference-2003": ("12760852", "reference-plan.json", {"Q5A446"}),
    "reference-2005-oxygen": ("15790671", "reference-followup-plan.json", {"Q5A446", "G1UB63", "Q5AD05"}),
    "reference-2005-expression": ("15814599", "reference-followup-plan.json", {"Q59UT4", "Q59UT5"}),
}
PROTEINS = {
    "Q5A446": (
        "CFL1",
        125,
        2,
        ["CFL1", "FRE1"],
        "CAALFM_C405770CA",
        ["CaO19.1263", "CaO19.8848"],
        "Ferric/cupric reductase transmembrane component 1",
        {"12760852", "15790671"},
    ),
    "G1UB63": (
        "CSA1",
        61,
        1,
        ["CSA1", "WAP1"],
        "CAALFM_C700090CA",
        ["CaO19.7114"],
        "Cell wall protein 1",
        {"15790671"},
    ),
    "Q5AD05": (
        "SOD4",
        133,
        1,
        ["PGA2", "SOD32", "SOD4"],
        "CAALFM_C200660CA",
        ["CaO19.2062", "CaO19.9609"],
        "Cell surface superoxide dismutase [Cu-Zn] 4",
        {"15790671"},
    ),
    "Q59UT4": (
        "RBT5",
        104,
        1,
        ["RBT5"],
        "CAALFM_C400130WA",
        ["CaO19.13081", "CaO19.5636"],
        "GPI-anchored hemophore RBT5",
        {"15814599"},
    ),
    "Q59UT5": (
        "PGA7",
        98,
        1,
        ["CRW3", "PGA7", "RBT6"],
        "CAALFM_C400120WA",
        ["CaO19.13080", "CaO19.5635"],
        "GPI-anchored hemophore PGA7",
        {"15814599"},
    ),
}


def title(value):
    return " ".join(unescape(value).split()).casefold().rstrip(".")


def discovery_context(sources):
    expected_counts = ({"CHEBI:31398": 15, "CHEBI:453011": 34}, {"CHEBI:31398": 28, "CHEBI:453011": 81})
    if len(sources) != 2:
        raise ValueError("discovery checkpoint coverage changed")
    selected, result = {}, []
    all_ids = set()
    for source, expected in zip(sources, expected_counts, strict=True):
        rows = source["records"]
        if len(rows) != 2 or {r["identifier"] for r in rows} != set(STRUCTURES):
            raise ValueError("discovery compound membership changed")
        projected = []
        for row in rows:
            identifier = row["identifier"]
            ids, queries = row["candidate_ids"], row["queries"]
            if (
                len(ids) != len(set(ids))
                or len(ids) != expected[identifier]
                or len(queries) != (4 if identifier == "CHEBI:31398" else 2)
            ):
                raise ValueError("discovery candidate or query counts changed")
            observed = set()
            for query in queries:
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
                    if candidate["source"] == "MED" and pmid in LEADS:
                        doi, pmcid = LEADS[pmid]
                        if (
                            candidate.get("pmid") != pmid
                            or candidate.get("doi") != doi
                            or candidate.get("pmcid") != pmcid
                            or (pmid in selected and selected[pmid] != candidate)
                        ):
                            raise ValueError("selected publication identity changed")
                        selected[pmid] = candidate
            if observed != set(ids) or not {"MED:" + p for p in LEADS} <= observed:
                raise ValueError("discovery candidate union changed")
            all_ids.update(ids)
            projected.append(
                {
                    "identifier": identifier,
                    "retained_candidate_ids": sorted(ids),
                    "candidate_count": len(ids),
                    "complete_queries": len(queries),
                    "primary_results_reviewed": 0,
                }
            )
        result.append({"input": source["input"], "records": projected})
    return {
        "checkpoints": result,
        "selected_leads": selected,
        "distinct_retained_candidate_ids": sorted(all_ids),
        "distinct_candidates": len(all_ids),
        "all_candidates_primary_reviewed": False,
        "duplicate_query_memberships_are_independent_evidence": False,
    }


def project_reference(entry, taxon, leads):
    if (
        not isinstance(entry, dict)
        or entry.get("primaryAccession") not in PROTEINS
        or {"sequence", "features", "comments"}.intersection(entry)
    ):
        raise ValueError("reference membership or payload scope changed")
    gene, version, seqversion, names, locus, orfs, protein, pmids = PROTEINS[entry["primaryAccession"]]
    species = [lineages.identity(row) for row in taxon.get("lineage", []) if row.get("rank") == "species"]
    if (
        lineages.identity(taxon) != {"taxonId": 237561, "scientificName": TAXON_NAME, "rank": "strain"}
        or entry["organism"].get("scientificName") != TAXON_NAME
        or species != [{"taxonId": 5476, "scientificName": "Candida albicans", "rank": "species"}]
    ):
        raise ValueError("reference taxonomy identity changed")
    if len(entry.get("genes", [])) != 1 or entry["genes"][0].get("geneName", {}).get("value") != gene:
        raise ValueError("primary gene name and synonyms changed roles")
    projected = reference.project_reference(entry, gene, 5476, taxon)
    native_orfs = sorted(v["value"] for block in entry["genes"] for v in block.get("orfNames", []))
    if (
        projected["entry_version"] != version
        or projected["sequence_version"] != seqversion
        or projected["gene_names"] != names
        or projected["ordered_locus_names"] != [locus]
        or native_orfs != orfs
        or projected["protein_name"] != protein
    ):
        raise ValueError("versioned reference gene, alias or locus changed")
    citations = {}
    for item in entry.get("references", []):
        citation = item.get("citation", {})
        identifiers = citation.get("citationCrossReferences", [])
        matches = [r["id"] for r in identifiers if r["database"] == "PubMed" and r["id"] in LEADS]
        if not matches:
            continue
        if len(matches) != 1 or matches[0] in citations:
            raise ValueError("selected publication duplicated or ambiguous")
        pmid = matches[0]
        dois = [r["id"].lower() for r in identifiers if r["database"] == "DOI"]
        if (
            dois != [LEADS[pmid][0]]
            or citation.get("id") != pmid
            or citation.get("citationType") != "journal article"
            or title(citation.get("title", "")) != title(leads[pmid]["title"])
            or citation.get("publicationDate") != leads[pmid]["pubYear"]
            or item.get("referencePositions") != ["INDUCTION"]
            or item.get("referenceComments")
        ):
            raise ValueError("citation identity or induction scope changed")
        citations[pmid] = {
            "reference": "PMID:" + pmid,
            "doi": "DOI:" + dois[0],
            "database_reference_scope": "INDUCTION",
            "primary_results_reviewed": False,
            "resistance_causality_established": False,
        }
    if set(citations) != pmids:
        raise ValueError("selected citation membership changed")
    projected.pop("bibliography")
    projected["reference_species_taxon_id"] = projected.pop("source_species_taxon_id")
    return {
        **projected,
        "gene_orf_names": native_orfs,
        "reference_gene": gene,
        "selected_citations": [citations[p] for p in sorted(citations)],
        "role": "CITATION_LINKED_INDUCTION_REFERENCE_NOT_RESISTANT_ALLELE",
        "database_review_status_is_primary_review": False,
        "experimental_genome_assignment": None,
        "compound_specific_resistance_verified": False,
    }


def project_queries(payloads, headers, taxon, leads):
    entries, memberships = {}, {}
    for key, (_, _, expected) in QUERIES.items():
        rows = complete_query(payloads[key], headers[key], len(expected))
        if {row.get("primaryAccession") for row in rows} != expected:
            raise ValueError("citation query reference membership changed")
        memberships[key] = sorted("UniProtKB:" + accession for accession in expected)
        for entry in rows:
            accession = entry["primaryAccession"]
            if accession in entries and entries[accession] != entry:
                raise ValueError("same reference differs across citation queries")
            entries[accession] = entry
    if set(entries) != set(PROTEINS):
        raise ValueError("distinct reference coverage changed")
    return {
        "query_memberships": memberships,
        "query_result_memberships": 6,
        "distinct_reference_proteins": len(entries),
        "reference_proteins": [project_reference(entries[a], taxon, leads) for a in sorted(entries)],
        "repeated_accessions_are_independent_proteins_or_experiments": False,
    }


def build(root, directory=CACHE):
    directory = root / directory
    keys = {"article-2003"} | set(QUERIES)
    if any(
        {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} != keys
        for suffix in ("-receipt.json", "-attempt.json")
    ):
        raise ValueError("request inventory changed")
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    protected = json.loads(reference.check_pin(root, cohort["protected"]).read_bytes())
    reference.check_pin(root, cohort["source_queue"])
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or any(protected.get(r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("full corpus preflight changed")
    if len(cohort["records"]) != 2 or {r["identifier"] for r in cohort["records"]} != set(STRUCTURES):
        raise ValueError("compound cohort changed")
    for row in cohort["records"]:
        record = load_record(reference.check_pin(root, row["snapshot"]))
        slug, key = STRUCTURES[row["identifier"]]
        if (
            row["record"]["path"] != f"data/antibiotics/antibacterial/{slug}.yaml"
            or record["identifier"] != row["identifier"]
            or record["label"] != row["label"]
            or record["chemical_structure"]["standard_inchi_key"] != key
            or row["standard_inchi_key"] != key
            or record.get("resistance_mechanisms")
            or record.get("genotype_resistance_score_rules")
            or row["snapshot"]["sha256"] != row["record"]["sha256"]
            or protected.get(row["record"]["path"]) != row["record"]["sha256"]
        ):
            raise ValueError("historical exact-structure record changed")
    for source in cohort["discovery"]:
        path = reference.check_pin(root, source["input"])
        payload = path.read_bytes()
        data = json.loads(gzip.decompress(payload) if path.suffix == ".gz" else payload)
        rows = [r for r in data["records"] if r["identifier"] in STRUCTURES]
        if rows != source["records"] or any(r["sha256"] != protected[r["path"]] for r in rows):
            raise ValueError("discovery snapshot binding changed")
    discovery = discovery_context(cohort["discovery"])
    sources = {
        "article-2003": planned_source(root, directory, "article-2003", "request-plan.json", ARTICLE, (500,))
    }
    hold_pin = reference.pin(root, directory / "primary-hold.json")
    hold = json.loads(reference.check_pin(root, hold_pin).read_bytes())
    error = json.loads(reference.check_pin(root, sources["article-2003"]["body"]).read_bytes())
    if (
        error.get("status") != 500
        or error.get("error") != "Internal Server Error"
        or error.get("path") != "/europepmc/webservices/rest/PMC155814/fullTextXML"
        or hold.get("disposition") != "TECHNICAL_HTTP_500_HOLD"
        or hold.get("source") != {k: sources["article-2003"][k] for k in ("body", "receipt")}
        or hold.get("primary_results_reviewed") is not False
        or hold.get("retry_or_alternate_route") is not False
        or hold.get("technical_error_is_negative_biological_evidence") is not False
        or hold.get("other_selected_primary_studies_unrequested") != ["PMID:15790671", "PMID:15814599"]
    ):
        raise ValueError("primary hold or evidence boundary changed")
    payloads, headers, plans = {}, {}, {}
    for key, (pmid, plan, _) in QUERIES.items():
        url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
            {"query": "lit_pubmed:" + pmid, "format": "json", "size": "500", "fields": FIELDS}
        )
        source = planned_source(root, directory, key, plan, url)
        sources[key] = source
        payloads[key] = json.loads(reference.check_pin(root, source["body"]).read_bytes())
        headers[key] = json.loads(reference.check_pin(root, source["receipt"]).read_bytes())["headers"]
        plans[key] = json.loads(reference.check_pin(root, source["plan"]).read_bytes())
        if (
            plans[key].get("cohort") != reference.pin(root, cohort_path)
            or plans[key].get("primary_hold") != hold_pin
        ):
            raise ValueError("reference plan cohort or hold changed")
    followup = plans["reference-2005-oxygen"]
    review_pin = reference.pin(root, directory / "reference-canary-review.json")
    review = json.loads(reference.check_pin(root, review_pin).read_bytes())
    if (
        followup != plans["reference-2005-expression"]
        or followup.get("canary_review") != review_pin
        or review.get("source") != {k: sources["reference-2003"][k] for k in ("body", "receipt")}
        or review.get("reference_accession") != "UniProtKB:Q5A446"
        or review.get("gene") != "CFL1"
        or review.get("synonym") != "FRE1"
        or review.get("reference_taxon") != "NCBITaxon:237561"
        or review.get("entry_version") != 125
        or review.get("sequence_version") != 2
        or review.get("primary_results_reviewed") is not False
        or review.get("experimental_role_or_allele_established") is not False
        or review.get("citation_match_is_causality") is not False
        or followup.get("selected_citations")
        != {p: discovery["selected_leads"][p] for p in ("15790671", "15814599")}
    ):
        raise ValueError("reference canary follow-up binding changed")
    checkpoint = followup["taxonomy_checkpoint"]
    previous = json.loads(reference.check_pin(root, checkpoint).read_bytes())
    if (
        checkpoint["sha256"] != protected.get(checkpoint["path"])
        or previous["taxonomy_source"] != followup["reused_taxonomy"]
    ):
        raise ValueError("native taxonomy reuse changed")
    taxon, tax_source = lineages.native_taxon(root, followup["reused_taxonomy"], "237561", "2026_03")
    references = project_queries(payloads, headers, taxon, discovery["selected_leads"])
    return {
        "date": "2026-10-14",
        "scope": "INDUCTION_REFERENCE_CONTEXT_NOT_RESISTANCE_ALLELES",
        "baseline_commit": cohort["baseline_commit"],
        "cohort": reference.pin(root, cohort_path),
        "records": cohort["records"],
        "census": cohort["census"],
        "corpus_records_hash_checked_at_preflight": 2939,
        "discovery": discovery,
        "sources": sources,
        "primary_hold": hold_pin,
        "reference_canary_review": review_pin,
        "taxonomy_checkpoint": checkpoint,
        "taxonomy_source": tax_source,
        **references,
        "chemical_scope": {
            "neutral_and_olamine_records_kept_distinct": True,
            "titles_establish_tested_chemical_form": False,
            "salt_and_neutral_results_transferred": False,
        },
        "curation_decision": "NO_RESISTANCE_ASSERTION_OR_EXPERIMENTAL_IDENTIFIERS_WITHOUT_PRIMARY_SUPPORT",
        "limits": {
            "http_attempts": 4,
            "http_status_counts": {"200": 3, "500": 1},
            "primary_results_reviews": 0,
            "new_taxonomy_requests": 0,
            "native_taxonomy_responses_reused": 1,
            "retries": 0,
            "automatic_redirects": 0,
            "biological_records_changed": 0,
            "figures_visually_reviewed": False,
            "supplements_reviewed": False,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "source_adoptions": 0,
            "reuse_terms_review_resumed": False,
            "numeric_AST_variants_sequences_constructs_or_protocols_exported": False,
            "issue_1040": "DEFERRED",
            "prior_source_holds_preserved": True,
            "whole_record_primary_review": "OPEN",
            "full_corpus_goal_status": "OPEN",
        },
        "reference_attribution": {
            "source": "UniProt Consortium",
            "license": "CC BY 4.0",
            "release": "2026_03",
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
            raise SystemExit("Ciclopirox checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {
                "records": 2,
                "distinct_reference_proteins": 5,
                "primary_access_holds": 1,
                "new_resistance_assertions": 0,
            }
        )
    )


if __name__ == "__main__":
    main()
