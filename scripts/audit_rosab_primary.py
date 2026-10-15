"""Bind a manual RosAB primary-text assessment to exact source claims, offline."""

import argparse
import json
from pathlib import Path

import audit_card_complex_members as members

reference, require = members.reference, members.require
read_json = members.prior.mex.read_json
PREFIX = "research/2026-10-15-rosab-primary"
PLAN = Path(PREFIX + "-plan.json")
OUTPUT = Path(PREFIX + ".json")
SCOPE = "ROSAB_PRIMARY_TEXT_SCOPE_NOT_COMPONENT_SPECIFIC_AST_OR_EXPERIMENTAL_ALLELES"
PARENT = "ARO:3004030"
MEMBERS = {"ARO:3003048": "rosA", "ARO:3003049": "rosB"}
ACCESSIONS = {"UniProtKB:Q56877": "ARO:3003048", "UniProtKB:Q56876": "ARO:3003049"}
DOI = "10.1046/j.1365-2958.2000.01956.x"
HELD_DOI = "10.1046/j.1365-2958.2002.02940.x"


def validate_assessment(notes):
    primary, held, handoff = notes["primary"], notes["second_citation"], notes["handoff"]
    require(
        notes["scope"] == SCOPE
        and primary["doi"] == DOI
        and primary["pmid"] == "10931306"
        and primary["url"] == "https://onlinelibrary.wiley.com/doi/full/" + DOI
        and primary["source_kind"] == "PUBLISHER_HTML_VIA_WEB_READER_NOT_VISUAL_PDF_REVIEW"
        and primary["paper_compound_label"] == "polymyxin B"
        and primary["paper_species_name"] == "Yersinia enterocolitica"
        and primary["paper_parent_context_label"] == "YeO8c"
        and primary["paper_parent_context_table_label"] == "8081-res"
        and primary["paper_reference_parent_label"] == "8081-c"
        and primary["phenotype_direction"] == "LOSS_OF_FUNCTION_SENSITIVITY_NOT_A_NEW_RESISTANT_ALLELE"
        and set(primary["locations"]) == {"organism", "compound", "phenotype_scope", "measurement_scope"},
        "primary assessment identity or evidence scope changed",
    )
    require(
        primary["measurement_types_kept_separate"]
        == ["SURVIVAL_PERCENTAGE", "RADIAL_DIFFUSION_DERIVED_ESTIMATE", "DISK_DIFFUSION"]
        and primary["displayed_disk_diffusion_unit_statement"] == "1 unit equal to 10 mm"
        and primary["displayed_radial_diffusion_unit_statement"] == "10 units = 1 mm"
        and primary["displayed_disk_units_require_typeset_verification"] is True,
        "measurement scope changed or rendered units silently repaired",
    )
    false_primary = (
        "tested_derivative_is_reference_parent",
        "component_specific_assay_established",
        "direct_vs_indirect_action_resolved_by_single_gene_comparison",
        "heterologous_and_native_contexts_merged",
        "disk_units_silently_corrected",
        "numeric_ast_exported",
        "clinical_resistance_interpretation_assigned",
        "figures_visually_reviewed",
        "table_layout_visually_verified",
        "whole_paper_signoff",
        "display_date_is_new_experiment",
    )
    false_handoff = (
        "qualification_already_applied",
        "experimental_protein_or_strain_assignment",
        "exact_allele_assignment",
        "experimental_genome_assignment",
        "sequence_variant_construct_protocol_exports",
        "broader_gene_or_record_review_complete",
    )
    require(
        all(primary[k] is False for k in false_primary)
        and all(handoff[k] is False for k in false_handoff)
        and handoff["all_four_source_assertions_preserved"] is True
        and handoff["primary_text_scope_qualification_candidate"] is True
        and handoff["disposition"] == "WITHHOLD_COMPONENT_SPECIFIC_BIOLOGICAL_CURATION",
        "assessment promoted beyond inspected evidence",
    )
    require(
        held["doi"] == HELD_DOI
        and held["pmid"] == "12010497"
        and held["url"] == "https://onlinelibrary.wiley.com/doi/full/" + HELD_DOI
        and held["reader_result"] == "HTTP_403_FORBIDDEN"
        and held["primary_results_reviewed"] is False
        and held["disposition"] == "ACCESS_HOLD_NO_ALTERNATE_ROUTE_OR_RETRY"
        and held["absence_of_component_evidence_in_this_paper_established"] is False,
        "held paper promoted or access denial treated as biological absence",
    )
    access = notes["access_accounting"]
    require(
        access["new_native_http_script_requests"] == access["ncbi_endpoints_opened"] == 0
        and access["web_search_queries"] == 5
        and access["web_reader_open_operations"] == 4
        and access["web_reader_find_operations"] == 5
        and access["web_service_upstream_http_request_count_known"] is False
        and access["held_source_retried"] is access["author_contacted"] is False,
        "access accounting changed",
    )


def reference_context(entry, taxon, expected, member_id):
    projected = members.member_reference(entry, taxon)
    require(projected == expected, "native reference differs from pinned member audit")
    require(
        ACCESSIONS[projected["accession"]] == member_id
        and projected["gene_symbols"] == [MEMBERS[member_id]]
        and any(
            x["database"] == "CARD" and x["id"] == member_id
            for x in projected["native_card_cross_references"]
        ),
        "member reference cross-reference or gene symbol changed",
    )
    citations = []
    for row in entry["references"]:
        ids = row["citation"].get("citationCrossReferences", [])
        if {"database": "PubMed", "id": "10931306"} not in ids:
            continue
        require({"database": "DOI", "id": DOI} in ids, "native citation identifiers disagree")
        strains = sorted({c["value"] for c in row.get("referenceComments", []) if c["type"] == "STRAIN"})
        require(strains == ["8081-c"], "native bibliography strain context changed")
        citations.append(
            {
                "reference_number": row["referenceNumber"],
                "identifiers": ids,
                "reference_positions": row["referencePositions"],
                "reference_strain_comments": strains,
                "complete_native_reference_sha256": members.screen.checksum(row),
                "reference_comment_assigns_experimental_derivative": False,
            }
        )
    require(len(citations) == 1, "primary citation binding is absent or ambiguous")
    return {"member_aro": member_id, "reference": projected, "primary_citation_binding": citations[0]}


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["parent"] == PARENT
        and plan["members"] == MEMBERS
        and plan["reference_accessions"] == sorted(ACCESSIONS)
        and plan["selection"] == "ALL_CURRENT_ROSAB_SOURCE_CLAIMS_AND_BOTH_NATIVE_MEMBER_REFERENCES"
        and plan["biological_record_writes"] is False
        and plan["ncbi_requests"] == 0
        and plan["issue_1040"] == "DEFERRED"
        and plan["reuse_terms_review_resumed"] is False
        and plan["assessment_is_manual_primary_reading_not_automatically_verified_experiment"] is True,
        "research scope changed",
    )
    prior = read_json(root, plan["prior"])
    source_plan = read_json(root, plan["native_source_plan"])
    require(
        plan["native_source_plan"] == prior["native_source_plan"]
        and plan["inputs"]["proteins"] == source_plan["inputs"]["proteins"]
        and {k: plan["inputs"][k] for k in prior["inputs"]} == prior["inputs"],
        "native source provenance changed",
    )
    notes = read_json(root, plan["assessment"])
    validate_assessment(notes)
    parent = prior["parents"][PARENT]
    require(
        {e["member_aro"]: e["member_label"] for e in parent["member_edges"]} == MEMBERS
        and parent["reference_accessions"] == sorted(ACCESSIONS),
        "parent or member selection changed",
    )
    index, update = [read_json(root, plan["inputs"][k]) for k in ("index", "corpus_update")]
    for key in ("source_queue", "source_inventory"):
        reference.check_pin(root, index["inputs"][key])
    records, claims = members.current_context(root, index, update, {PARENT}, {PARENT: "RosAB"})
    require(len(records) == len(claims) == 4, "complete source claim coverage changed")
    require(claims == [c for c in prior["claims"] if c["aro_id"] == PARENT], "source claims changed")
    entries, pages = members.prior.replay_proteins(
        root, source_plan, read_json(root, plan["inputs"]["proteins"])
    )
    taxon, taxonomy_source = members.prior.lineages.native_taxon(root, plan["taxonomy"], "34054", "2026_03")
    _, species = members.prior.lineages.lineage(taxon)
    require(
        taxonomy_source == prior["taxonomy_sources"]["34054"]
        and taxon["rank"] == "serotype"
        and species
        == {"taxonId": 630, "rank": "species", "scientificName": notes["primary"]["paper_species_name"]},
        "source species-name or reference-serotype grounding changed",
    )
    proteins = {
        a: reference_context(entries[a.split(":")[1]], taxon, prior["reference_proteins"][a], tid)
        for a, tid in sorted(ACCESSIONS.items())
    }
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "assessment": plan["assessment"],
        "prior": plan["prior"],
        "inputs": plan["inputs"],
        "source_parent": parent,
        "records": records,
        "claims": claims,
        "reference_proteins": proteins,
        "native_protein_pages": pages,
        "taxonomy_source": taxonomy_source,
        "paper_species_name_crosswalk": {
            "source_name": notes["primary"]["paper_species_name"],
            "species_rank_node": species,
            "species_taxon_id": "NCBITaxon:630",
            "basis": "EXACT_NAME_MATCH_TO_NATIVE_REFERENCE_SPECIES_ANCESTOR",
            "reference_serotype_taxon_id": "NCBITaxon:34054",
            "reference_rank": "serotype",
            "experimentally_tested_derivative_taxon_assigned": False,
            "record_taxon_assignment": False,
        },
        "claim_dispositions": [
            {
                "record_identifier": c["record_identifier"],
                "claim_sha256": c["claim_sha256"],
                "disposition": notes["handoff"]["disposition"],
                "source_claim_removed": False,
                "individual_component_assay_established": False,
                "exact_experimental_allele_assigned": False,
            }
            for c in claims
        ],
        "manual_review_status": {
            "one_primary_text_reading": True,
            "assessment_is_independently_reproduced_by_code": False,
            "all_figures_and_tables_visually_reviewed": False,
            "second_citation_access_hold": True,
            "biological_curation_completed": False,
        },
        "summary": {
            "complete_records_read": len(records),
            "source_claims": len(claims),
            "reference_proteins": len(proteins),
            "primary_text_contexts_reviewed": 1,
            "held_primary_citations": 1,
            "name_level_species_crosswalks": 1,
            "corpus_records_hash_checked": 2939,
            "native_protein_entries_replayed": len(entries),
            "native_protein_pages_replayed": len(pages),
            "new_uniprot_requests": 0,
        },
        "limits": {
            **members.prior.mex.LIMITS,
            "new_primary_results_reviews": 1,
            "new_review_is_text_only_not_whole_paper_signoff": True,
            "operational_exports": False,
            "numeric_ast_exports": 0,
        },
        "attribution": (
            "CARD/ARO and UniProt metadata under CC BY 4.0; "
            "manual publisher-text assessment separately cited."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    payload = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
    output = args.root / args.output
    if args.check or output.exists():
        require(
            output.read_bytes() == payload, "primary-context audit does not reproduce; preserve prior output"
        )
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
