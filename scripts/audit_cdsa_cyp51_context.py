"""Replay source-scope limits and an inactive, note-only CdsA curation draft."""

import argparse
import copy
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import audit_card_explicit_identifiers as identifiers
import audit_m35_porin_context as previous
import audit_vmlr2_structure_context as native
import card_evidence_reviews as review

from antibioticmech.activity_collections import load_record

prior, aliases, mex = previous.prior, previous.aliases, previous.mex
reference, require, read_json = prior.reference, prior.require, prior.read_json
PREFIX = "research/2026-10-15-cdsa-cyp51-context"
PLAN, OUTPUT = Path(PREFIX + "-audit-plan.json"), Path(PREFIX + ".json")
SCOPE = "CDSA_TAXONOMIC_CONFLICT_AND_CYP51_DISCOVERY_NOT_EXPERIMENTAL_GROUNDING"
FUNGAL = {f"ARO:{i}" for i in range(3009535, 3009539)}
TERMS = FUNGAL | {"ARO:3004097", "ARO:3004578"}
QUERIES = {"cdsa-locus": 'gene_exact:"sm351-26"', "cyp51-publication": "lit_pubmed:24298976"}
SOURCE_TAXA = {
    "Streptococcus mitis": ("28037", "cdsa"),
    "Acinetobacter baumannii": ("470", "abuo"),
    "Pyrenopeziza brassicae": ("76659", "cyp51"),
}


def check_assessment(a):
    c, f, b = a["cdsa"], a["cyp51"], a["abuo"]
    require(
        a["scope"] == "PAPER_LOCUS_AND_TAXONOMIC_SCOPE_NOT_EXPERIMENTAL_ALLELE_ASSIGNMENT"
        and a["ncbi_requests"] == 0
        and a["issue_1040"] == "DEFERRED"
        and c["aro_id"] == "ARO:3004097"
        and c["pmid"] == "28115347"
        and c["doi"] == "10.1128/aac.02435-16"
        and c["source_url"] == "https://journals.asm.org/doi/full/10.1128/aac.02435-16"
        and c["access"] == "WEB_TOOL_PUBLISHER_HTML_READ"
        and c["source_label_species"] == "Streptococcus mitis"
        and c["paper_subject_label"] == "Streptococcus mitis/oralis 351"
        and c["paper_background_strain"] == "351"
        and c["paper_gene"] == "cdsA"
        and c["paper_orf"] == "sm351-26"
        and "Addendum in proof" in c["selected_locations"],
        "paper identity context changed",
    )
    require(
        c["alternative_species_assignment"] is c["experimental_taxon_id"] is None
        and c["study_project"]
        == {
            "namespace": "BioProject",
            "accession": "PRJNA358614",
            "basis": "PAPER_REPORTED_NOT_INDEPENDENTLY_VERIFIED",
            "scope": "STUDY_PROJECT_NOT_ASSEMBLY_GENE_OR_PROTEIN_ACCESSION",
            "ncbi_link_followed": False,
            "versioned_assembly_assigned": None,
            "experimental_genome_identity_verified": False,
        },
        "unresolved taxon or project promoted to experimental identity",
    )
    for doc, keys in (
        (
            a,
            (
                "native_local_publisher_receipts_available",
                "publisher_assessment_is_offline_body_replay",
                "experimental_allele_assignments",
                "numeric_ast_exported",
                "variant_specifications_exported",
                "protocols_exported",
                "biological_record_writes",
            ),
        ),
        (
            c,
            (
                "source_species_is_verified_experimental_species",
                "figures_visually_reviewed",
                "supplements_reviewed",
                "primary_results_reviewed_for_ast_curation",
                "whole_paper_signoff",
            ),
        ),
        (
            f,
            (
                "source_definition_has_own_citation",
                "discovery_is_inherited_source_citation",
                "http_status_inferred",
                "primary_results_reviewed",
                "global_unavailability_inferred",
            ),
        ),
        (b, ("http_status_inferred", "primary_results_reviewed", "global_unavailability_inferred")),
    ):
        require(all(doc[k] is False for k in keys), "evidence scope was promoted")
    require(
        set(f["aro_ids"]) == FUNGAL
        and f["source_species"] == "Pyrenopeziza brassicae"
        and f["discovery_pmid"] == "24298976"
        and f["discovery_doi"] == "10.1111/mpp.12106"
        and f["source_url"]
        == "https://repository.rothamsted.ac.uk/download/"
        "d691add8b8d898fdc35d342aa5f216a5cc0ffc97304fd167cd612019bb2800ea/"
        "3845595/Carter_et_al-2014-Molecular_Plant_Pathology.pdf"
        and f["web_tool_result"] == "URL is not accessible via this tool"
        and b["aro_id"] == "ARO:3004578"
        and b["pmid"] == "25512405"
        and b["doi"] == "10.1128/aac.03626-14"
        and b["source_url"] == "https://journals.asm.org/doi/full/10.1128/aac.03626-14"
        and b["web_tool_result"] == "Failed to fetch: Error fetching URL"
        and b["inactive_accessions_remain_withheld"] == ["A0A225SC95", "Q2FD57"]
        and f["alternate_primary_routes_requested"] == b["alternate_primary_routes_requested"] == 0,
        "discovery or access hold changed",
    )


def discovery_metadata(wrapper):
    require(
        wrapper["status"] == 200
        and urlsplit(wrapper["url"]).netloc == "www.ebi.ac.uk"
        and hashlib.sha256(wrapper["body"].encode()).hexdigest() == wrapper["sha256"],
        "cached discovery provenance changed",
    )
    rows = [r for r in json.loads(wrapper["body"])["resultList"]["result"] if r["id"] == "24298976"]
    require(
        len(rows) == 1 and rows[0]["source"] == "MED" and rows[0]["doi"] == "10.1111/mpp.12106",
        "discovery publication identifier mismatch",
    )
    return {k: rows[0][k] for k in ("id", "source", "doi", "pmcid", "pubYear")}


def check_history(directory):
    for suffix in ("attempt", "receipt", "body"):
        require(
            set(directory.glob(f"*-{suffix}.json"))
            == {directory / f"{key}-{suffix}.json" for key in QUERIES},
            "unaccounted request artifact",
        )
    require(not list(directory.glob("*-error.json")), "unaccounted native request failure")


def draft_projection(root, plan, records, claims):
    document = read_json(root, plan["inputs"]["proposed_review"])
    active = read_json(root, plan["inputs"]["active_reviews"])
    require(
        len(document["reviews"]) == 1
        and document["reviews"][0]["review_id"] == "2026-10-15-cdsa-paper-taxonomic-scope",
        "draft review identity changed",
    )
    draft = document["reviews"][0]
    require(
        draft["review_id"] not in {r["review_id"] for r in active["reviews"]},
        "draft is already in active curation",
    )
    inventory = reference.check_pin(root, plan["inputs"]["source_inventory"])
    with inventory.open() as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    docs = {r["identifier"]: load_record(root / r["path"]) for r in records}
    accepted = review.load_reviews(
        inventory, rows, docs, reference.check_pin(root, plan["inputs"]["proposed_review"])
    )
    require(len(accepted) == 1 and len(draft["source_rows"]) == 1, "draft affects more than one assertion")
    key = next(iter(accepted))
    source_rows = [r for r in rows if review.row_digest(r) == key]
    selected_claims = [c for c in claims if c["aro_id"] == "ARO:3004097"]
    require(
        len(source_rows) == len(selected_claims) == 1 and source_rows[0]["determinant_id"] == "ARO:3004097",
        "draft source row changed",
    )
    c = selected_claims[0]
    original = docs[c["record_identifier"]]["resistance_mechanisms"][c["resistance_index"]]
    projected = copy.deepcopy(original)
    require(review.apply_review(projected, source_rows[0], accepted), "draft did not qualify its assertion")
    require(
        {k: v for k, v in projected.items() if k != "note"} == original
        and set(projected) - set(original) == {"note"},
        "draft changed more than a note",
    )
    return {
        "draft": plan["inputs"]["proposed_review"],
        "review_id": draft["review_id"],
        "source_row": draft["source_rows"][0],
        "loader_accepted": True,
        "projection_changes_only_note": True,
        "projection_performed_in_memory_only": True,
        "validation_record_scope": "THIRTEEN_SELECTED_COMPLETE_RECORDS_NOT_FULL_SEED_QC",
        "default_active_review_contains_draft": False,
        "rendered_note_or_record_written": False,
        "source_owned_curation_applied": False,
        "pending": [
            "Source-owned curation review and canary",
            "Validated writer and history",
            "Corpus reproduction, rendering and authoritative QC",
        ],
    }


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["draft_applied_to_active_curation"] is False
        and plan["whole_record_primary_signoff"] is False
        and plan["new_qualified_reference_terms"] == []
        and plan["ncbi_requests"] == 0
        and plan["issue_1040"] == "DEFERRED",
        "audit scope changed",
    )
    frozen = read_json(root, plan["inputs"]["source_plan"])
    for p in frozen["inputs"].values():
        reference.check_pin(root, p)
    inputs = {k: read_json(root, p) for k, p in frozen["inputs"].items() if k != "source_queue"}
    require(
        frozen["scope"] == SCOPE
        and frozen["fields"] == prior.FIELDS
        and frozen["release"] == "2026_03"
        and frozen["canary"] == "cdsa-locus"
        and frozen["constraints"]
        == {
            "retries": 0,
            "redirects_followed": 0,
            "ncbi_requests": 0,
            "biological_record_writes": False,
            "experimental_identity_assignments": False,
            "issue_1040": "DEFERRED",
            "full_corpus_goal_status": "OPEN",
        }
        and frozen["preflight"]["ignored_files_included"] is True
        and frozen["preflight"]["matching_native_query_paths"] == [],
        "frozen source scope changed",
    )
    require(
        inputs["previous_verification"]["artifacts"]["dossier"] == frozen["inputs"]["prior"],
        "prior verification binding changed",
    )
    check_assessment(inputs["assessment"])
    rows = {t: inputs["all_status"]["terms"][t] for t in TERMS}
    require(rows == frozen["source_context"], "source term contexts changed")
    records, claims = prior.prior.members.current_context(
        root, inputs["index"], inputs["corpus_update"], TERMS, {t: r["source_label"] for t, r in rows.items()}
    )
    require(records == frozen["records"] and claims == frozen["claims"], "complete source cohort changed")
    annotations = aliases.annotation_context(
        aliases.ontology_graph(root, inputs["definitions"]), rows, inputs["definitions"], {}
    )
    require(all(rows[t]["definition_citations"] == [] for t in FUNGAL), "fungal citation scope changed")
    directory = root / frozen["cache_directory"]
    check_history(directory)
    require(set(frozen["requests"]) == set(plan["receipts"]) == set(QUERIES), "request set changed")
    queries = {}
    for key, query in QUERIES.items():
        params = {
            "query": query,
            "format": "json",
            "size": "500",
            "sort": "accession asc",
            "fields": prior.FIELDS,
        }
        require(frozen["requests"][key]["parameters"] == params, "exact request changed")
        entries, source = mex.native_query(root, plan["receipts"][key], {k: [v] for k, v in params.items()})
        receipt, attempt = native.request_receipt(
            root, directory, key, plan["receipts"][key], plan["inputs"]["source_plan"], frozen["max_bytes"]
        )
        require(receipt["url"] == frozen["requests"][key]["url"], "request URL changed")
        body = read_json(root, receipt["body"])
        count = len(body.get("suggestions", []))
        require(
            entries == {} and plan["inspected_counts"][key] == {"results": 0, "suggestions_ignored": count},
            "native candidate or suggestion count changed",
        )
        queries[key] = {
            "source": source,
            "attempt": attempt,
            "result_count": 0,
            "suggestions_ignored": count,
            "suggestions_followed": False,
            "biological_absence_inferred": False,
        }
    canary = read_json(root, plan["inputs"]["canary"])
    require(
        canary["plan_sha256"] == plan["inputs"]["source_plan"]["sha256"]
        and canary["receipt"] == plan["receipts"]["cdsa-locus"]
        and canary["approved_second_metadata_query"] is True
        and canary["complete_result_count"] == 0
        and canary["suggestions_ignored"] == 5
        and canary["suggestions_followed"] is canary["biological_absence_inferred"] is False,
        "inspected canary changed",
    )
    require(
        queries["cyp51-publication"]["source"]["started_at"]
        > queries["cdsa-locus"]["source"]["retrieved_at"],
        "second request preceded canary response",
    )
    taxonomy, gene_queries = {}, {}
    for name, (tid, gene) in SOURCE_TAXA.items():
        binding = inputs["all_status"]["source_bindings"][name]
        node, source = prior.cached_node(root, {"taxon_id": tid, "source": binding["native_source"]})
        identity = prior.lineages.identity(node)
        require(
            identity == binding["identity"] and prior.prior.species_name_binding(name, node),
            "source taxonomy binding changed",
        )
        taxonomy[tid] = {"identity": identity, "source": source, "experimental_subject_assignment": False}
        old = inputs["all_status"]["queries"]["proteins-" + tid]
        q = f"(gene_exact:{gene}) AND taxonomy_id:{tid}"
        require(
            old["query"] == q and old["complete_for_query"] is True and len(old["pages"]) == 1,
            "prior query incomplete or changed",
        )
        entries, source = mex.native_query(
            root,
            old["pages"][0]["receipt"],
            {
                "query": [q],
                "format": ["json"],
                "size": ["500"],
                "sort": ["accession asc"],
                "fields": [prior.FIELDS],
            },
        )
        require(entries == {} and old["result_count"] == 0, "old query now has candidates")
        gene_queries[tid] = {"source": source, "result_count": 0, "biological_absence_inferred": False}
    citations = {}
    for pmid in ("28115347", "25512405"):
        old = inputs["citation_queries"]["queries"][pmid]
        entries, source = aliases.literature.read_query(root, root / old["directory"], pmid)
        require(
            source == old["query"] and source["complete_for_query"] is True and not entries,
            "own-citation query changed",
        )
        citations[pmid] = source
    old = inputs["explicit_identifiers"]["reference_queries"]["source-accessions"]
    q = "(accession:A0A225SC95 OR sec_acc:A0A225SC95 OR accession:Q2FD57 OR sec_acc:Q2FD57)"
    entries, inactive_source = mex.native_query(
        root,
        old["native_source"]["receipt"],
        {
            "query": [q],
            "format": ["json"],
            "size": ["500"],
            "sort": ["accession asc"],
            "fields": [identifiers.FIELDS],
        },
    )
    inactive = {k: identifiers.inactive_reference(e) for k, e in entries.items()}
    require(inactive == inputs["explicit_identifiers"]["inactive_accessions"], "inactive references changed")
    old_coverage = inputs["prior"]["coverage"]
    qualified, remaining = old_coverage["qualified_terms"], old_coverage["remaining_terms"]
    require(
        set(remaining) >= TERMS
        and len(set(qualified)) == len(qualified) == 108
        and len(set(remaining)) == len(remaining) == 70
        and not set(qualified) & set(remaining),
        "bounded coverage changed or overlaps",
    )
    terms = {
        t: {
            "source_label": r["source_label"],
            "record_memberships": r["record_memberships"],
            "definition_citations": r["definition_citations"],
            "qualified_reference_accessions": [],
            "status": "SOURCE_TAXONOMIC_SCOPE_CONFLICT"
            if t == "ARO:3004097"
            else "PRIMARY_IDENTITY_UNRESOLVED_NOT_BIOLOGICAL_ABSENCE",
            "experimental_taxon_assignment": None,
            "exact_allele_assignment": False,
            "whole_record_primary_review": "OPEN",
        }
        for t, r in sorted(rows.items())
    }
    result = {
        "date": frozen["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "inputs": frozen["inputs"],
        "records": records,
        "claims": claims,
        "terms": terms,
        "source_annotations": annotations,
        "primary_assessment": inputs["assessment"],
        "discovery_metadata": discovery_metadata(inputs["discovery"]),
        "queries": queries,
        "source_taxonomy": taxonomy,
        "reused_gene_queries": gene_queries,
        "reused_citation_queries": citations,
        "retained_inactive_references": inactive,
        "inactive_source": inactive_source,
        "curation_handoff": draft_projection(root, plan, records, claims),
        "coverage": {
            "cohort_terms": 178,
            "previous_qualified_count": 108,
            "new_qualified_terms": [],
            "qualified_terms": qualified,
            "remaining_terms": remaining,
            "whole_corpus_completion": False,
        },
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(records),
            "source_claims": len(claims),
            "source_terms": len(terms),
            "new_qualified_source_terms": 0,
            "combined_qualified_terms": 108,
            "combined_remaining_terms": 70,
            "new_metadata_requests": 2,
            "new_taxonomy_requests": 0,
            "reused_complete_queries": 6,
            "reused_taxonomy_nodes": 3,
            "reviewed_taxonomic_scope_conflicts": 1,
            "inactive_note_only_curation_drafts": 1,
            "biological_record_writes": 0,
            "experimental_allele_assignments": 0,
            "ncbi_requests": 0,
        },
        "limits": [
            "Source species nodes do not resolve the paper's mitis/oralis subject uncertainty.",
            "A BioProject is not a versioned assembly or a genotype-to-phenotype join.",
            "Exact empty queries do not establish biological absence; suggestions were ignored.",
            "The fungal publication is a discovery lead, not an inherited CARD citation or primary signoff.",
            "Publisher access failures have no inferred HTTP status; "
            "no alternate primary routes were requested.",
            "The curation draft is inactive; only its in-memory note-only projection was tested.",
            "No sequences, variant specifications, protocols or numeric AST were exported.",
            "The full-corpus investigation remains OPEN; NCBI / #1040 and reuse-terms work remain deferred.",
        ],
        "attribution": {
            "CARD_ARO": "CC BY 4.0",
            "UniProt": "CC BY 4.0",
            "primary_papers": "Cited context; no source adoption",
        },
    }
    native.reject_operational_fields(result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    output = args.root / args.output
    if args.check or output.exists():
        require(output.read_text() == payload, "saved CdsA scope audit differs from offline replay")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
