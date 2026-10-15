"""Bind primary donor/host distinctions to current Mex claims and reference proteins, offline."""

import argparse
import json
from pathlib import Path

import audit_card_complex_members as members

mex = members.prior.mex
reference, require, read_json = members.reference, members.require, mex.read_json
PREFIX = "research/2026-10-15-mex-host-context"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
SCOPE = "MEX_PRIMARY_HOST_CONTEXT_NOT_EXPERIMENTAL_ALLELE_OR_DONOR_PHENOTYPE_ASSIGNMENT"
TERMS = {"ARO:3000386": "MexAB-OprM", "ARO:3000797": "MexCD-OprJ"}
COMPONENTS = {
    "ARO:3000386": {"mexA": "UniProtKB:P52477", "mexB": "UniProtKB:P52002", "oprM": "UniProtKB:Q51487"},
    "ARO:3000797": {"mexC": "UniProtKB:G3XD25", "mexD": "UniProtKB:Q9HVI9", "oprJ": "UniProtKB:Q51397"},
}
QUALIFICATIONS = {
    (
        "ARO:3000386",
        "CHEBI:100241",
    ): "NO_INCREASE_IN_SELECTED_HETEROLOGOUS_COMPARISON_NOT_DONOR_SPECIES_ABSENCE",
    ("ARO:3000386", "CHEBI:3508"): "MINIMAL_OR_LACKING_HETEROLOGOUS_EFFECT_NOT_DONOR_SPECIES_ABSENCE",
    ("ARO:3000386", "CHEBI:29007"): "MINIMAL_OR_LACKING_HETEROLOGOUS_EFFECT_NOT_DONOR_SPECIES_ABSENCE",
    (
        "ARO:3000797",
        "CHEBI:28368",
    ): "NO_INCREASE_IN_SELECTED_HETEROLOGOUS_COMPARISON_NOT_DONOR_SPECIES_ABSENCE",
    ("ARO:3000386", "CHEBI:42355"): "ERYTHROMYCIN_LABEL_NOT_EXACT_ERYTHROMYCIN_A_FORM_CONFIRMATION",
    ("ARO:3000797", "CHEBI:42355"): "ERYTHROMYCIN_LABEL_NOT_EXACT_ERYTHROMYCIN_A_FORM_CONFIRMATION",
}
FALSE_FIELDS = (
    "reference_strain_is_tested_subject",
    "heterologous_results_generalized_to_donor_species",
    "all_compounds_have_same_effect",
    "protein_expression_alone_establishes_resistance",
    "individual_subunit_is_complete_complex",
    "reference_accession_identifies_tested_allele",
    "experimental_genome_assigned",
    "numeric_ast_exported",
    "clinical_resistance_interpretation_assigned",
    "figures_visually_reviewed",
    "typeset_tables_visually_verified",
    "whole_paper_signoff",
    "all_definition_citations_reviewed",
    "sequence_variant_primer_construct_protocol_exports",
    "manual_reading_independently_verified_by_code",
    "qualification_is_correction_of_card_assertion",
    "other_claims_without_selected_qualification_are_verified",
)


def validate_assessment(notes):
    require(
        notes["scope"] == SCOPE
        and notes["pmid"] == "9449262"
        and notes["doi"] == "10.1128/aac.42.1.65"
        and notes["url"] == "https://journals.asm.org/doi/10.1128/aac.42.1.65"
        and notes["source_species_name"] == "Pseudomonas aeruginosa"
        and notes["assay_host_species_name"] == "Escherichia coli"
        and notes["source_kind"] == "PUBLISHER_HTML_PRIMARY_TEXT_NOT_VISUAL_PDF_REVIEW"
        and notes["selected_host_labels"] == ["KZM120", "LBB1201"],
        "primary identity changed",
    )
    require(all(notes[k] is False for k in FALSE_FIELDS), "primary scope promoted beyond inspected evidence")
    alias = notes["source_reported_host_alias"]
    require(
        alias["label"] == "KZM120"
        and alias["alias"] == "HN818"
        and alias["location"] == "Table 1 footnote b"
        and alias["independently_verified"] is alias["strain_taxon_id_assigned"] is False,
        "source alias promoted to independent experimental identity",
    )
    rows = notes["claim_qualifications"]
    require(
        len(rows) == 6
        and {(r["aro_id"], r["record_identifier"]): r["status"] for r in rows} == QUALIFICATIONS
        and all(r["location"] for r in rows),
        "claim qualification coverage or interpretation changed",
    )
    access = notes["access"]
    require(
        access["new_native_script_http_requests"]
        == access["ncbi_endpoints_opened"]
        == access["new_access_holds"]
        == 0
        and access["access_holds_retried"] is access["outreach"] is False
        and access["web_search_queries"] == access["web_reader_find_operations"] == 2
        and access["web_reader_open_operations"] == 1
        and access["web_service_upstream_http_request_count_known"] is False,
        "access scope changed",
    )


def species_context(taxon, name):
    require(
        taxon["scientificName"] == name and taxon["rank"] == "species" and taxon["active"] is True,
        "source species name or rank changed",
    )
    _, species = members.prior.lineages.lineage(taxon)
    return {
        "source_name": name,
        "species_node": species,
        "taxon_id": "NCBITaxon:" + str(taxon["taxonId"]),
        "basis": "EXACT_SOURCE_NAME_TO_CACHED_UNIPROT_SPECIES_NODE",
        "experimental_strain_taxon_assigned": False,
        "reference_protein_assigned_to_host": False,
        "record_taxon_assignment": False,
    }


def claim_dispositions(claims, records, notes):
    records = {r["identifier"]: r for r in records}
    qualifications = {(r["aro_id"], r["record_identifier"]): r for r in notes["claim_qualifications"]}
    require(
        set(qualifications) <= {(c["aro_id"], c["record_identifier"]) for c in claims},
        "qualification does not bind a selected source claim",
    )
    return [
        {
            "aro_id": c["aro_id"],
            "record_identifier": c["record_identifier"],
            "record_label": records[c["record_identifier"]]["label"],
            "standard_inchi_key": records[c["record_identifier"]]["standard_inchi_key"],
            "claim_sha256": c["claim_sha256"],
            "selected_primary_qualification": qualifications.get((c["aro_id"], c["record_identifier"])),
            "disposition": "KEEP_SOURCE_ASSERTION_WITHHOLD_EXPERIMENTAL_JOIN",
            "source_claim_removed": False,
            "exact_chemical_form_verified": False,
            "experimental_allele_assigned": False,
            "clinical_resistance_call_assigned": False,
            "whole_claim_primary_signoff": False,
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
    prior, old_mex = [read_json(root, plan[k]) for k in ("prior_members", "prior_mex")]
    require(plan["prior_mex_native_plan"] == old_mex["plan"], "native Mex plan binding changed")
    require(mex.build(root) == old_mex, "prior Mex native projection does not reproduce")
    require(
        plan["inputs"] == prior["inputs"] and plan["source_plan"] == prior["native_source_plan"],
        "source inputs changed",
    )
    index, update = [read_json(root, plan["inputs"][k]) for k in ("index", "corpus_update")]
    records, claims = members.current_context(root, index, update, set(TERMS), TERMS)
    require(
        len(records) == 17
        and len(claims) == 22
        and claims == [c for c in prior["claims"] if c["aro_id"] in TERMS]
        and claims == [c for c in old_mex["claims"] if c["aro_id"] in TERMS],
        "source claim coverage changed",
    )
    for tid in TERMS:
        require(
            "PMID:9449262" in prior["annotations"][tid]["definition_citation_ids"]
            and prior["annotations"][tid]["definition_citation_ids"]
            == old_mex["terms"][tid]["definition_citation_ids"],
            "own-citation binding changed",
        )
    query_plan = plan["own_citation_query"]
    pool, query = members.screen.literature.read_query(root, root / query_plan["directory"], "9449262")
    require(
        query == query_plan["query"] and query["complete_for_query"] and not pool,
        "own-citation query changed; reassess experimental protein join",
    )
    components = {}
    for tid, symbols in COMPONENTS.items():
        for symbol, accession in symbols.items():
            row = old_mex["reference_candidates"][accession]
            require(
                row["gene_symbols"] == [symbol]
                and row["reference_taxonomy"]["taxon_id"] == "NCBITaxon:208964"
                and old_mex["terms"][tid]["components"][symbol]["native_complex_component_references"]
                == [accession],
                "component reference context changed",
            )
            components[accession] = row
    source_plan = read_json(root, plan["source_plan"])
    entries, pages = members.prior.replay_proteins(
        root, source_plan, read_json(root, source_plan["inputs"]["proteins"])
    )
    member_views = {}
    for accession in sorted({a for tid in TERMS for a in prior["parents"][tid]["reference_accessions"]}):
        expected = prior["reference_proteins"][accession]
        taxid = expected["reference_taxonomy"]["taxon_id"].split(":")[1]
        taxon, _ = members.prior.lineages.native_taxon(
            root, prior["taxonomy_sources"][taxid], taxid, "2026_03"
        )
        projected = members.member_reference(entries[accession.split(":")[1]], taxon)
        require(projected == expected, "native member reference changed")
        member_views[accession] = projected
    require(
        len(member_views) == 4 and len(set(member_views) | set(components)) == 7,
        "distinct reference coverage changed",
    )
    source_taxon, source_provenance = members.prior.lineages.native_taxon(
        root, old_mex["taxonomy_sources"]["287"], "287", "2026_03"
    )
    host_taxon, host_provenance = members.prior.lineages.native_taxon(
        root, plan["host_species_taxonomy"], "562", "2026_03"
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
        "claim_dispositions": claim_dispositions(claims, records, notes),
        "component_references": components,
        "member_reference_views": member_views,
        "component_bindings": COMPONENTS,
        "own_citation_query": query,
        "source_species": species_context(source_taxon, notes["source_species_name"]),
        "assay_host_species": species_context(host_taxon, notes["assay_host_species_name"]),
        "taxonomy_sources": {"287": source_provenance, "562": host_provenance},
        "distinct_mexd_references": {
            "accessions": ["UniProtKB:Q51396", "UniProtKB:Q9HVI9"],
            "same_experimental_allele_established": False,
            "one_reference_selected_as_representative": False,
        },
        "summary": {
            "complete_selected_records_read": len(records),
            "source_claims": len(claims),
            "source_terms": len(TERMS),
            "selected_claim_qualifications": 6,
            "distinct_reference_proteins_preserved": 7,
            "native_mex_entries_replayed": 20,
            "native_card_entries_replayed": len(entries),
            "native_card_pages_replayed": len(pages),
            "new_primary_text_contexts_reviewed": 1,
            "species_name_crosswalks": 2,
            "new_uniprot_requests": 0,
            "corpus_records_hash_checked": 2939,
        },
        "limits": {
            **mex.LIMITS,
            "new_primary_results_reviews": 1,
            "new_review_is_text_only_not_whole_paper_signoff": True,
            "operational_exports": False,
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
