"""Replay MexXY definition-citation scope and regulator reference metadata offline."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode

import audit_mexxy_context as prior

members, mex = prior.members, prior.mex
reference, require, read_json = prior.reference, prior.require, prior.read_json
PREFIX = "research/2026-10-15-mexxy-definitions"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
SCOPE = "MEXXY_DEFINITION_CITATION_SCOPE_AND_REGULATOR_REFERENCE_GROUNDING"
PARENT = "ARO:3003032"
PRIMARY = "PRIMARY_TEXT_CONTEXT_REVIEW_NOT_WHOLE_PAPER_SIGNOFF"
SECONDARY = "SECONDARY_REVIEW_NOT_NEW_PRIMARY_EXPERIMENT"
PAPERS = {
    "12654672": ("10.1128/aac.47.4.1371-1375.2003", PRIMARY),
    "21149619": ("10.1128/aac.01252-10", PRIMARY),
    "23233851": ("10.3389/fmicb.2012.00408", SECONDARY),
}
LOCI = {"PA1799": ("parR", "Q9I2U3"), "PA1798": ("parS", "Q9I2U4")}
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_card,lit_pubmed_id,sequence_version,version"
)
QUALIFICATIONS = {
    "antibioticmech:aro-6407ce57f1": (
        ["12654672", "21149619"],
        "GENERIC_GENTAMICIN_NOT_EXACT_GENTAMICIN_C_CONFIRMATION",
    ),
    "CHEBI:43968": (["21149619"], "MULTIMECHANISM_PHENOTYPE_NOT_DIRECT_MEXXY_TRANSPORT_PROOF"),
    "CHEBI:17698": (["21149619"], "INDUCTION_NOT_TRANSPORT_OR_GLOBAL_SUBSTRATE_ABSENCE"),
}
FALSE_FIELDS = (
    "figure_images_visually_reviewed",
    "typeset_tables_visually_verified",
    "numeric_ast_exported",
    "clinical_resistance_calls_assigned",
    "exact_experimental_alleles_assigned",
    "experimental_genomes_assigned",
    "biological_curation_completed",
    "all_definition_citations_are_primary_studies",
    "all_definition_citation_statuses_complete_means_whole_claim_signoff",
    "other_claims_without_selected_qualification_are_verified",
    "sequence_variant_primer_construct_protocol_exports",
    "manual_primary_reading_independently_verified_by_code",
)
PAPER_FALSE_FIELDS = {
    "12654672": (
        "killing_endpoint_is_mic",
        "source_label_establishes_exact_gentamicin_c_structure",
        "laboratory_ecoli_hosts_are_resistance_assay_subjects",
        "reference_protein_is_tested_derivative",
    ),
    "21149619": (
        "background_label_is_pinned_pao1_reference_identity",
        "regulators_are_structural_efflux_components",
        "multimechanism_phenotype_is_direct_mexxy_transport",
        "induction_establishes_transport",
        "clinical_association_is_functional_validation_of_each_isolate",
        "negative_or_background_dependent_results_discarded",
        "disk_diffusion_and_mic_collapsed",
        "reference_identifier_silently_normalized",
        "reference_identifier_is_experimental_assembly_assignment",
    ),
    "23233851": (
        "cached_metadata_rewritten",
        "secondary_summary_promoted_to_primary_results",
        "historical_sequence_difference_explanation_independently_verified",
        "held_opra_paper_reconstructed_from_review",
    ),
}


def validate_assessment(notes):
    require(notes["scope"] == SCOPE and set(notes["citations"]) == set(PAPERS), "citation scope changed")
    require(all(notes[k] is False for k in FALSE_FIELDS), "assessment promoted beyond inspected evidence")
    for pmid, (doi, kind) in PAPERS.items():
        row = notes["citations"][pmid]
        url = (
            "https://journals.asm.org/doi/" + doi
            if kind == PRIMARY
            else "https://www.frontiersin.org/journals/microbiology/articles/" + doi + "/full"
        )
        require(
            row["doi"] == doi
            and row["classification"] == kind
            and row["url"] == url
            and bool(row["locations"]),
            "citation identity or classification changed",
        )
        require(
            all(row[k] is False for k in PAPER_FALSE_FIELDS[pmid]),
            "paper scope promoted beyond inspected evidence",
        )
    first, second, review = [notes["citations"][p] for p in PAPERS]
    require(
        first["assay_species"] == second["assay_species"] == "Pseudomonas aeruginosa"
        and first["source_background_label"] == "PAO1"
        and first["selected_subject_labels"] == ["PAO1", "11B", "PAO1T"]
        and first["evidence_scope"] == "TRANSIENT_ADAPTATION_NOT_A_NEW_HERITABLE_ALLELE"
        and first["source_compound_label"] == "gentamicin"
        and second["source_background_label"] == "PAO1Bes"
        and second["regulator_locus_labels"] == {locus: gene for locus, (gene, _) in LOCI.items()}
        and second["source_reference_identifier"] == "NC-002516",
        "primary subject or locus identity changed",
    )
    require(
        review["publisher_article_type"] == "REVIEW article"
        and review["cached_discovery_pub_type"] == "research-article; journal article",
        "publication type conflict lost",
    )
    rows = notes["claim_qualifications"]
    require(
        len(rows) == len(QUALIFICATIONS)
        and {r["record_identifier"]: (r["pmids"], r["status"]) for r in rows} == QUALIFICATIONS,
        "claim qualification coverage changed",
    )
    require(
        notes["access"]
        == {
            "web_search_queries": 2,
            "web_reader_open_operations": 6,
            "web_reader_find_operations": 9,
            "web_service_upstream_http_request_count_known": False,
            "new_native_publisher_requests": 0,
            "new_uniprot_requests": 2,
            "ncbi_requests": 0,
            "access_holds_retried": False,
            "outreach": False,
            "reuse_terms_review_resumed": False,
        },
        "access accounting changed",
    )


def parameters(locus):
    return {
        "query": f"gene_exact:{locus} AND organism_id:208964",
        "format": "json",
        "size": "500",
        "sort": "accession asc",
        "fields": FIELDS,
    }


def native_references(root, plan, taxon):
    request, canary = [read_json(root, plan[k]) for k in ("request_plan", "canary")]
    require(
        set(request["queries"]) == set(plan["queries"]) == set(plan["attempts"]) == set(LOCI)
        and request["request_limit"] == plan["new_uniprot_requests"] == 2
        and request["canary"] == "PA1799"
        and request["ncbi_requests"] == request["retries"] == request["redirects_followed"] == 0
        and request["sequence_or_variant_fields_requested"]
        is request["experimental_identity_assignment"]
        is False
        and request["biological_record_writes"] is request["reuse_terms_review_resumed"] is False
        and request["issue_1040"] == "DEFERRED",
        "request scope changed",
    )
    require(
        canary["accepted"] is True
        and canary["locus"] == "PA1799"
        and canary["gene"] == "parR"
        and canary["accession"] == "UniProtKB:Q9I2U3"
        and canary["receipt"] == plan["queries"]["PA1799"]
        and canary["release"] == "2026_03"
        and canary["native_taxon_id"] == 208964
        and canary["complete_result_count"] == 1
        and canary["sequence_or_variant_fields_present"]
        is canary["experimental_derivative_or_allele_assignment"]
        is False,
        "canary binding changed",
    )
    directory = (root / plan["request_plan"]["path"]).parent
    require(
        set(directory.rglob("*-attempt.json")) == {root / p["path"] for p in plan["attempts"].values()}
        and not list(directory.rglob("*-error.json")),
        "unaccounted native request or error",
    )
    results, sources = {}, {}
    for locus, (gene, accession) in LOCI.items():
        params = parameters(locus)
        url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(params)
        attempt = read_json(root, plan["attempts"][locus])
        require(
            request["queries"][locus] == {"gene": gene, "parameters": params, "url": url}
            and attempt["request_plan"] == plan["request_plan"]
            and attempt["url"] == url
            and attempt["ncbi_requests"] == attempt["retries"] == attempt["redirects_followed"] == 0,
            "native request differs from frozen plan",
        )
        entries, source = mex.native_query(root, plan["queries"][locus], {k: [v] for k, v in params.items()})
        require(set(entries) == {accession}, "locus query coverage changed")
        projected = members.member_reference(entries[accession], taxon)
        require(
            projected["gene_symbols"] == [gene]
            and projected["ordered_locus_names"] == [locus]
            and projected["reference_taxonomy"]["taxon_id"] == "NCBITaxon:208964"
            and projected["reference_taxonomy"]["native_rank"] == "strain",
            "native locus identity changed",
        )
        results[locus] = {
            "reference": projected,
            "source_paper": "PMID:21149619",
            "join_basis": "EXACT_SOURCE_LOCUS_AND_GENE_TO_PAO1_REFERENCE_NOT_TESTED_ALLELE",
            "structural_complex_component": False,
            "experimental_derivative_assignment": False,
        }
        sources[locus] = {"attempt": plan["attempts"][locus], "response": source}
    return results, sources


def review_metadata(root, source):
    receipt = read_json(root, source)
    require(
        receipt["status"] == 200
        and hashlib.sha256(receipt["body"].encode()).hexdigest() == receipt["sha256"],
        "cached discovery body changed",
    )
    payload = json.loads(receipt["body"])
    rows = [
        r for r in payload["resultList"]["result"] if r.get("id") == "23233851" and r.get("source") == "MED"
    ]
    require(len(rows) == 1, "review discovery identity absent or ambiguous")
    row = rows[0]
    require(
        row["pmid"] == "23233851"
        and row["doi"] == PAPERS["23233851"][0]
        and row["pubType"] == "research-article; journal article",
        "native publication identity changed",
    )
    return {
        "native_row_sha256": members.screen.checksum(row),
        "native_pub_type": row["pubType"],
        "publisher_type": "REVIEW article",
        "disposition": SECONDARY,
        "source": source,
        "native_metadata_rewritten": False,
        "new_primary_experiment": False,
    }


def dispositions(claims, records, notes):
    by_id = {r["identifier"]: r for r in records}
    qualifications = {r["record_identifier"]: r for r in notes["claim_qualifications"]}
    require(
        set(qualifications) <= {c["record_identifier"] for c in claims},
        "qualification not bound to a source claim",
    )
    return [
        {
            "aro_id": c["aro_id"],
            "record_identifier": c["record_identifier"],
            "claim_sha256": c["claim_sha256"],
            "standard_inchi_key": by_id[c["record_identifier"]]["standard_inchi_key"],
            "selected_qualification": qualifications.get(c["record_identifier"]),
            "source_claim_removed": False,
            "experimental_identity_assigned": False,
            "whole_claim_primary_signoff": False,
            "exact_chemical_form_verified": False,
            "disposition": "KEEP_SOURCE_ASSERTION_WITHHOLD_EXPERIMENTAL_JOIN",
        }
        for c in claims
    ]


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["selected_terms"] == {PARENT: "MexXY-OprM"}
        and plan["new_uniprot_requests"] == 2
        and plan["ncbi_requests"] == 0
        and plan["biological_record_writes"] is plan["reuse_terms_review_resumed"] is False
        and plan["issue_1040"] == "DEFERRED",
        "research scope changed",
    )
    notes, old = [read_json(root, plan[k]) for k in ("assessment", "prior")]
    validate_assessment(notes)
    require(
        prior.build(root) == old and plan["inputs"] == old["inputs"], "prior MexXY context does not reproduce"
    )
    index, update = [read_json(root, plan["inputs"][k]) for k in ("index", "corpus_update")]
    definitions = read_json(root, plan["definition_citations"])
    require(
        plan["definition_citations"] == index["inputs"]["definition_citations"], "definition source changed"
    )
    selected = {
        t
        for t, r in definitions["terms"].items()
        if set(r["definition_citation_ids"]) & {"PMID:" + p for p in PAPERS}
    }
    require(
        selected == {PARENT}
        and definitions["terms"][PARENT]["definition_citation_ids"] == prior.CITATIONS[PARENT],
        "complete own-citation term cohort changed",
    )
    records, claims = members.current_context(root, index, update, selected, plan["selected_terms"])
    require(
        len(records) == len(claims) == 11 and claims == [c for c in old["claims"] if c["aro_id"] == PARENT],
        "selected source claim coverage changed",
    )
    pools, queries = {}, {}
    require(set(plan["own_citation_queries"]) == set(PAPERS), "citation query coverage changed")
    for pmid, qp in plan["own_citation_queries"].items():
        pools[pmid], queries[pmid] = members.screen.literature.read_query(root, root / qp["directory"], pmid)
        require(
            queries[pmid] == qp["query"] and queries[pmid]["complete_for_query"],
            "cached own-citation query changed",
        )
    require(
        set(pools["12654672"]) == {"G3XCW2"} and not pools["21149619"] and not pools["23233851"],
        "own-citation protein result coverage changed",
    )
    taxon, tax_source = members.prior.lineages.native_taxon(
        root, old["taxonomy_sources"]["208964"], "208964", "2026_03"
    )
    regulators, sources = native_references(root, plan, taxon)
    entry = pools["12654672"]["G3XCW2"]
    mexy = members.member_reference(entry, taxon)
    require(
        mexy["gene_symbols"] == ["mexY"] and mexy["ordered_locus_names"] == ["PA2018"],
        "native MexY identity changed",
    )
    matches = [
        r
        for r in entry["references"]
        if {"database": "PubMed", "id": "12654672"} in r["citation"].get("citationCrossReferences", [])
    ]
    require(len(matches) == 1, "MexY primary bibliography absent or ambiguous")
    row = matches[0]
    require(
        {"database": "DOI", "id": PAPERS["12654672"][0]} in row["citation"]["citationCrossReferences"]
        and row["referencePositions"] == ["FUNCTION", "INDUCTION BY AMINOGLYCOSIDE"]
        and not row.get("referenceComments"),
        "MexY primary bibliography context changed",
    )
    citation_status = {p: r["classification"] for p, r in notes["citations"].items()}
    citation_status["9925549"] = "PRIOR_TEXT_CONTEXT_REVIEW_NOT_WHOLE_PAPER_SIGNOFF"
    require(
        {"PMID:" + p for p in citation_status} == set(prior.CITATIONS[PARENT]),
        "definition status accounting incomplete",
    )
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "assessment": plan["assessment"],
        "prior": plan["prior"],
        "inputs": plan["inputs"],
        "records": records,
        "claims": claims,
        "claim_dispositions": dispositions(claims, records, notes),
        "definition_citation_statuses": citation_status,
        "own_citation_queries": queries,
        "regulator_reference_loci": regulators,
        "native_request_sources": sources,
        "reference_taxonomy_source": tax_source,
        "paper_species_grounding": old["primary_source_species"],
        "mexy_own_citation_reference_view": mexy,
        "mexy_citation_binding": {
            "reference_number": row["referenceNumber"],
            "identifiers": row["citation"]["citationCrossReferences"],
            "reference_positions": row["referencePositions"],
            "complete_native_reference_sha256": members.screen.checksum(row),
            "experimental_derivative_assignment": False,
        },
        "review_type_conflict": review_metadata(root, plan["review_discovery_receipt"]),
        "preserved_opra_access_hold": old["primary_access_hold"],
        "summary": {
            "complete_selected_records_read": 11,
            "source_claims": 11,
            "source_terms": 1,
            "new_primary_text_contexts_reviewed": 2,
            "secondary_reviews_classified": 1,
            "definition_citations_with_scoped_status": 4,
            "selected_claim_qualifications": 3,
            "new_regulator_reference_loci": 2,
            "reused_own_citation_reference_entries": 1,
            "new_uniprot_requests": 2,
            "new_ncbi_requests": 0,
            "corpus_records_hash_checked": 2939,
        },
        "limits": {
            **mex.LIMITS,
            "new_primary_results_reviews": 2,
            "new_review_is_text_only_not_whole_paper_signoff": True,
            "operational_exports": False,
            "numeric_ast_exports": 0,
            "review_is_primary_experiment": False,
        },
        "attribution": "CARD/ARO and UniProt CC BY 4.0; manual publisher-text assessments separately cited.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    payload = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
    target = args.root / args.output
    if args.check or target.exists():
        require(target.read_bytes() == payload, "audit does not reproduce; preserve prior output")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
