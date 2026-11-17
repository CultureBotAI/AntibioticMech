"""Replay MexXY bibliography and primary host context without experimental identity assignment."""

import argparse
import json
from pathlib import Path

import audit_mex_host_context as host

members, mex = host.members, host.mex
reference, require, read_json = host.reference, host.require, host.read_json
PREFIX = "research/2026-10-15-mexxy-context"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
SCOPE = "MEXXY_REFERENCE_BIBLIOGRAPHY_AND_PRIMARY_HOST_CONTEXT_NOT_EXPERIMENTAL_ALLELES"
TERMS = {"ARO:3003032": "MexXY-OprM", "ARO:3003038": "MexXY-OprA"}
CITATIONS = {
    "ARO:3003032": ["PMID:12654672", "PMID:21149619", "PMID:23233851", "PMID:9925549"],
    "ARO:3003038": ["PMID:22282519"],
}
BIBLIOGRAPHY = {
    "I0IYR3": ("mexZ", "22282519", "PAGU 1504", "REGULATOR_NOT_STRUCTURAL_COMPONENT"),
    "I0IYR4": ("oprA", "22282519", "PAGU 1504", "REFERENCE_ONLY_UNRESOLVED_EXPERIMENTAL_JOIN"),
    "I0IYR5": ("oprA", "22282519", "PAGU 1503", "REFERENCE_ONLY_UNRESOLVED_EXPERIMENTAL_JOIN"),
    "Q9ZNG8": ("mexY", "9925549", "PAO1", "SOURCE_REFERENCE_NOT_HETEROLOGOUS_HOST"),
    "Q9ZNG9": ("mexX", "9925549", "PAO1", "SOURCE_REFERENCE_NOT_HETEROLOGOUS_HOST"),
}
HELD_DOI = "10.1099/mic.0.054320-0"
HELD_URL = (
    "https://www.microbiologyresearch.org/deliver/fulltext/micro/158/4/1071.html"
    "?itemId=/content/journal/micro/" + HELD_DOI + "&mimeType=html&fmt=ahah"
)
FALSE_FIELDS = {
    "primary": (
        "deposit_version_reported",
        "deposit_independently_verified",
        "deposit_is_genome_or_assembly_identifier",
        "deposit_assigned_to_assay_host",
        "source_reference_is_assay_host",
        "experimental_derivatives_assigned_reference_taxon",
        "laboratory_result_is_species_wide_resistance",
        "host_and_component_contexts_interchangeable",
        "source_inference_is_direct_native_complex_measurement",
        "numeric_ast_exported",
        "exact_chemical_forms_verified",
        "clinical_resistance_calls_assigned",
        "figures_visually_reviewed",
        "typeset_tables_visually_verified",
        "whole_paper_signoff",
    ),
    "held_primary": (
        "primary_results_reviewed",
        "pagu_to_pa7_or_other_named_strain_crosswalk_resolved",
        "title_names_every_native_reference_strain",
        "lack_of_biological_support_established",
    ),
    "": (
        "reference_strain_comments_are_strain_taxonomy_nodes",
        "same_symbol_references_collapsed",
        "primary_paper_citation_ownership_transferred_between_complexes",
        "biological_curation_completed",
        "exact_experimental_alleles_assigned",
        "sequence_variant_primer_construct_protocol_exports",
        "manual_reading_independently_verified_by_code",
    ),
}


def validate_assessment(notes):
    primary, held = notes["primary"], notes["held_primary"]
    require(
        notes["scope"] == SCOPE
        and primary["pmid"] == "9925549"
        and primary["doi"] == "10.1128/aac.43.2.415"
        and primary["url"] == "https://journals.asm.org/doi/10.1128/aac.43.2.415"
        and primary["source_kind"] == "PUBLISHER_HTML_PRIMARY_TEXT_NOT_VISUAL_PDF_REVIEW"
        and primary["source_species_name"] == "Pseudomonas aeruginosa"
        and primary["source_reference_label"] == "PAO1"
        and primary["assay_host_species_name"] == "Escherichia coli"
        and primary["assay_background_labels"] == ["KAM3", "N43"]
        and primary["source_reported_nucleotide_deposit"] == "AB015853"
        and primary["result_scope"] == "HETEROLOGOUS_ASSAY_AND_NATIVE_COMPLEX_INFERENCE_KEPT_SEPARATE"
        and set(primary["locations"])
        == {"source_and_host", "component_and_inference_scope", "deposit", "compound_scope"}
        and all(primary["locations"].values()),
        "primary identity or scope changed",
    )
    for group, keys in FALSE_FIELDS.items():
        context = notes[group] if group else notes
        require(all(context[k] is False for k in keys), "assessment promoted beyond inspected evidence")
    require(
        held["pmid"] == "22282519"
        and held["doi"] == HELD_DOI
        and held["landing_url"] == "https://www.microbiologyresearch.org/content/journal/micro/" + HELD_DOI
        and held["abstract_inspected"] is True
        and held["advertised_fulltext_reader_result"]
        == "TOOL_INACCESSIBLE_WITHOUT_HTTP_STATUS_NOT_AN_ACCESS_DENIAL"
        and held["single_native_fulltext_request_status"] == 403
        and held["disposition"] == "ACCESS_HOLD_NO_RETRY_OR_ALTERNATE_ROUTE",
        "held source identity or disposition changed",
    )
    require(
        notes["bibliography_scope"]
        == {
            a: dict(zip(("gene", "pmid", "strain_comment", "role"), values, strict=True))
            for a, values in BIBLIOGRAPHY.items()
        },
        "bibliography identity or role changed",
    )
    require(
        notes["access"]
        == {
            "web_search_queries": 3,
            "web_reader_open_operations": 3,
            "web_reader_find_operations": 0,
            "web_service_upstream_http_request_count_known": False,
            "new_native_publisher_requests": 1,
            "new_uniprot_requests": 0,
            "ncbi_requests": 0,
            "outreach": False,
            "reuse_terms_review_resumed": False,
        },
        "access accounting changed",
    )


def access_hold(root, plan):
    request, attempt, receipt = [
        read_json(root, plan[k]) for k in ("request_plan", "primary_attempt", "primary_receipt")
    ]
    require(
        request["url"] == attempt["url"] == receipt["url"] == HELD_URL
        and request["pmid"] == "22282519"
        and request["doi"] == HELD_DOI
        and request["native_request_limit"] == 1
        and request["web_reader_result"] == "TOOL_INACCESSIBLE_WITHOUT_HTTP_STATUS_NOT_AN_ACCESS_DENIAL"
        and attempt["request_plan"] == plan["request_plan"]
        and receipt["status"] == 403
        and request["ncbi_requests"] == attempt["ncbi_requests"] == 0
        and all(
            obj[k] == 0 for obj in (request, attempt, receipt) for k in ("retries", "redirects_followed")
        ),
        "held primary request identity or accounting changed",
    )
    body = reference.check_pin(root, receipt["body"])
    require(
        receipt["sha256"] == receipt["body"]["sha256"] and receipt["bytes"] == body.stat().st_size,
        "held response body differs",
    )
    directory = (root / plan["request_plan"]["path"]).parent
    require(
        set(directory.rglob("*-attempt.json")) == {root / plan["primary_attempt"]["path"]}
        and not list(directory.rglob("*-error.json")),
        "unaccounted primary attempt or failure",
    )
    return {
        "request_plan": plan["request_plan"],
        "attempt": plan["primary_attempt"],
        "receipt": plan["primary_receipt"],
        "response_body": receipt["body"],
        "url": receipt["url"],
        "status": receipt["status"],
        "bytes": receipt["bytes"],
        "retrieved_at": receipt["retrieved_at"],
        "native_attempts": 1,
        "primary_results_reviewed": False,
        "establishes_biological_absence": False,
        "disposition": "ACCESS_HOLD_NO_RETRY_OR_ALTERNATE_ROUTE",
    }


def bibliography_context(entry, taxon):
    accession = entry["primaryAccession"]
    symbol, pmid, strain, role = BIBLIOGRAPHY[accession]
    projected = members.member_reference(entry, taxon)
    require(
        projected["gene_symbols"] == [symbol] and taxon["taxonId"] == 287 and taxon["rank"] == "species",
        "bibliography gene or native species context changed",
    )
    matches = [
        r
        for r in entry["references"]
        if {"database": "PubMed", "id": pmid} in r["citation"].get("citationCrossReferences", [])
    ]
    require(len(matches) == 1, "primary bibliography absent or ambiguous")
    row = matches[0]
    identifiers = row["citation"]["citationCrossReferences"]
    dois = [i["id"] for i in identifiers if i["database"] == "DOI"]
    strains = [c["value"] for c in row.get("referenceComments", []) if c["type"] == "STRAIN"]
    require(
        strains == [strain]
        and row["referencePositions"] == ["NUCLEOTIDE SEQUENCE"]
        and dois == ([HELD_DOI] if pmid == "22282519" else []),
        "native bibliography strain, position or DOI changed",
    )
    return {
        "reference": projected,
        "role": role,
        "primary_citation_binding": {
            "reference_number": row["referenceNumber"],
            "identifiers": identifiers,
            "reference_positions": row["referencePositions"],
            "reference_strain_comments": strains,
            "complete_native_reference_sha256": members.screen.checksum(row),
            "missing_native_doi_filled_from_external_source": False,
            "strain_comment_is_strain_taxonomy_assignment": False,
        },
        "experimental_allele_assigned": False,
        "experimental_host_assigned": False,
        "pagu_to_pa7_or_other_named_strain_crosswalk_resolved": False,
    }


def claim_dispositions(claims, records):
    by_id = {r["identifier"]: r for r in records}
    return [
        {
            "aro_id": c["aro_id"],
            "record_identifier": c["record_identifier"],
            "standard_inchi_key": by_id[c["record_identifier"]]["standard_inchi_key"],
            "claim_sha256": c["claim_sha256"],
            "definition_citation_ids": CITATIONS[c["aro_id"]],
            "disposition": "KEEP_SOURCE_ASSERTION_WITHHOLD_EXPERIMENTAL_JOIN",
            "selected_own_primary_status": "TEXT_CONTEXT_REVIEW_NOT_WHOLE_CLAIM_SIGNOFF"
            if c["aro_id"] == "ARO:3003032"
            else "ACCESS_HOLD_ABSTRACT_ONLY",
            "exact_chemical_form_verified": False,
            "experimental_allele_assigned": False,
            "whole_claim_primary_signoff": False,
            "source_claim_removed": False,
        }
        for c in claims
    ]


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["terms"] == TERMS
        and plan["biological_record_writes"] is False
        and plan["ncbi_requests"] == plan["new_uniprot_requests"] == 0
        and plan["issue_1040"] == "DEFERRED"
        and plan["reuse_terms_review_resumed"] is False,
        "research scope changed",
    )
    notes = read_json(root, plan["assessment"])
    validate_assessment(notes)
    hold = access_hold(root, plan)
    prior, old_mex = [read_json(root, plan[k]) for k in ("prior_members", "prior_mex")]
    require(mex.build(root) == old_mex, "prior Mex native projection does not reproduce")
    require(
        plan["inputs"] == prior["inputs"] and plan["source_plan"] == prior["native_source_plan"],
        "source input binding changed",
    )
    index, update = [read_json(root, plan["inputs"][k]) for k in ("index", "corpus_update")]
    for key in ("source_inventory", "source_queue"):
        reference.check_pin(root, index["inputs"][key])
    records, claims = members.current_context(root, index, update, set(TERMS), TERMS)
    require(
        len(records) == 12
        and len(claims) == 21
        and claims == [c for c in prior["claims"] if c["aro_id"] in TERMS]
        and claims == [c for c in old_mex["claims"] if c["aro_id"] in TERMS],
        "selected source claim coverage changed",
    )
    for tid, citations in CITATIONS.items():
        require(
            prior["annotations"][tid]["definition_citation_ids"]
            == old_mex["terms"][tid]["definition_citation_ids"]
            == citations,
            "own-citation binding changed",
        )
    qp = plan["oprA_citation_query"]
    pool, query = members.screen.literature.read_query(root, root / qp["directory"], "22282519")
    require(
        query == qp["query"] and query["complete_for_query"] and set(pool) == {"I0IYR3", "I0IYR4", "I0IYR5"},
        "own-citation query coverage changed",
    )
    source_plan = read_json(root, plan["source_plan"])
    entries, pages = members.prior.replay_proteins(
        root, source_plan, read_json(root, source_plan["inputs"]["proteins"])
    )
    taxa, taxonomy_sources = {}, {}
    for taxid, source in {
        "287": old_mex["taxonomy_sources"]["287"],
        "208964": old_mex["taxonomy_sources"]["208964"],
        "562": plan["host_taxonomy"],
    }.items():
        taxa[taxid], taxonomy_sources[taxid] = members.prior.lineages.native_taxon(
            root, source, taxid, "2026_03"
        )
    component_ids = {
        a
        for tid in TERMS
        for c in old_mex["terms"][tid]["components"].values()
        for a in c["symbol_query_candidates"]
    }
    components = {a: old_mex["reference_candidates"][a] for a in sorted(component_ids)}
    member_views = {}
    for accession in sorted({a for tid in TERMS for a in prior["parents"][tid]["reference_accessions"]}):
        expected = prior["reference_proteins"][accession]
        taxid = expected["reference_taxonomy"]["taxon_id"].split(":")[1]
        projected = members.member_reference(entries[accession.split(":")[1]], taxa[taxid])
        require(projected == expected, "native member reference changed")
        member_views[accession] = projected
    require(
        len(components) == 5 and len(member_views) == 4 and len(set(components) | set(member_views)) == 7,
        "distinct reference coverage changed",
    )
    bibliography = {
        a: bibliography_context(pool[a] if a in pool else entries[a], taxa["287"]) for a in BIBLIOGRAPHY
    }
    require(
        "UniProtKB:I0IYR3" not in set(components) | set(member_views),
        "regulator promoted to structural component",
    )
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "assessment": plan["assessment"],
        "prior_members": plan["prior_members"],
        "prior_mex": plan["prior_mex"],
        "inputs": plan["inputs"],
        "records": records,
        "claims": claims,
        "claim_dispositions": claim_dispositions(claims, records),
        "source_terms": {tid: old_mex["terms"][tid] for tid in TERMS},
        "component_reference_candidates": components,
        "member_reference_views": member_views,
        "native_bibliography_contexts": bibliography,
        "oprA_own_citation_query": query,
        "primary_access_hold": hold,
        "taxonomy_sources": taxonomy_sources,
        "primary_source_species": host.species_context(taxa["287"], notes["primary"]["source_species_name"]),
        "primary_assay_host_species": host.species_context(
            taxa["562"], notes["primary"]["assay_host_species_name"]
        ),
        "summary": {
            "complete_selected_records_read": len(records),
            "source_claims": len(claims),
            "source_terms": 2,
            "distinct_component_reference_candidates": 7,
            "native_bibliography_contexts": 5,
            "regulators_excluded_from_structural_components": 1,
            "new_primary_text_contexts_reviewed": 1,
            "held_primary_citations": 1,
            "native_card_entries_replayed": len(entries),
            "native_card_pages_replayed": len(pages),
            "native_mex_entries_replayed": 20,
            "new_native_publisher_requests": 1,
            "new_uniprot_requests": 0,
            "corpus_records_hash_checked": 2939,
        },
        "limits": {
            **mex.LIMITS,
            "new_primary_results_reviews": 1,
            "new_review_is_text_only_not_whole_paper_signoff": True,
            "operational_exports": False,
            "numeric_ast_exports": 0,
        },
        "attribution": "CARD/ARO and UniProt CC BY 4.0; manual publisher-text assessment separately cited.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
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
