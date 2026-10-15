"""Reconcile all AAC6 follow-up contexts with the complete CARD reference index."""

import argparse
import copy
import json
from collections import Counter, defaultdict
from pathlib import Path

import audit_aac6_gaps as aac6
import audit_aac34_followup as aac34
import audit_card_bla_memberships as prior
from audit_card_topoisomerase_memberships import check_live_claims

reference, require, registry = prior.reference, prior.require, prior.registry
progress, pointer, rebase, shared = prior.progress, prior.pointer, prior.rebase, prior.shared
PREFIX = "research/2026-10-15-card-aac6-memberships"
PLAN = Path(PREFIX + "-plan.json")
SCOPE = "CARD_REFERENCE_INDEX_WITH_COMPLETE_AAC6_LABEL_FOLLOWUP_NOT_EXPERIMENTAL_ALLELES"
QUALIFIED = "UNREVIEWED_AAC6_NAME_GENE_CITATION_TAXON_REFERENCE_ONLY"
COLUMNS = {**prior.COLUMNS, QUALIFIED: "unreviewed_aac6_reference_claims"}
UNSELECTED = prior.UNSELECTED
TERMS = {r["term"] for r in aac6.SELECTED.values()}


def check_aac34(dossier):
    require(
        dossier["scope"] == aac34.SCOPE
        and dossier["source_term_id"] == aac34.TERM
        and dossier["summary"]
        == {
            "complete_cached_name_queries": 2,
            "complete_cached_organism_queries": 1,
            "selected_reference_proteins": 0,
            "selected_reagent_paragraphs_reviewed": 1,
        }
        and dossier["limits"]
        == {
            "new_network_requests": 0,
            "earlier_name_query_requests_replayed": 2,
            "ncbi_requests": 0,
            "experimental_assignments": 0,
            "biological_records_changed": 0,
            "primary_access_holds_retried": 0,
            "all_aliases_or_sources_searched": False,
            "genome_assignment": None,
            "clinical_resistance_category_inferred": False,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "full_corpus_goal_status": "OPEN",
        },
        "AAC34 scope or disposition changed",
    )
    require(set(dossier["name_queries"]) == {"reviewed", "unreviewed"}, "name-query coverage changed")
    for key, reviewed in (("reviewed", True), ("unreviewed", False)):
        q = dossier["name_queries"][key]
        require(
            q["source"]["url"] == aac34.query_url(reviewed)
            and q["source"]["status"] == 200
            and q["source"]["release"] == "2026_03"
            and q["reviewed_subset"] is reviewed
            and type(q["result_count"]) is int
            and q["result_count"] == 0
            and q["complete_for_query"] is True
            and q["biological_absence_inferred"] is False
            and q["query_scope"] == "GLOBAL_ASCII_SOURCE_LABEL_IN_GENE_OR_PROTEIN_NAME_NOT_ALL_ALIASES",
            "AAC34 query or absence interpretation changed",
        )
    q, chemical = dossier["exact_organism_query"], dossier["chemical_context"]
    require(
        q["result_count"] == 0
        and type(q["result_count"]) is int
        and q["complete_for_query"] is True
        and q["biological_absence_inferred"] is False
        and q["reference_taxon_id"] == "NCBITaxon:1120679"
        and q["source"]["status"] == 200
        and q["source"]["release"] == "2026_03"
        and q["source"]["url"] == aac34.ORGANISM_URL
        and q["query_scope"] == "EXACT_ORGANISM_ID_NOT_ALL_TAXONOMIC_DESCENDANTS_OR_REFERENCE_ORGANISMS"
        and chemical["paragraph_sha256"] == aac34.PARAGRAPH_SHA
        and chemical["pmid"] == "PMID:27929110"
        and chemical["doi"] == "DOI:10.1038/ncomms13803"
        and chemical["exact_corpus_structure_assignment"] is None
        and all(
            chemical[k] is False
            for k in (
                "whole_article_or_supplement_identifier_absence_claimed",
                "activity_observation_curated",
                "operational_paragraph_exported",
                "kanamycin_specific_product_identifier_in_selected_paragraph",
            )
        ),
        "AAC34 chemical or organism context changed",
    )


def reference_identity(accession, row):
    expected = aac6.SELECTED[accession.removeprefix("UniProtKB:")]
    require(
        row["accession"] == accession
        and row["source_term_id"] == expected["term"]
        and row["source_label"] == expected["label"]
        and row["gene_symbols"] == [expected["gene"]]
        and row["scope"] == aac6.REFERENCE
        and row["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
        and row["entry_audit"] == {"entryVersion": expected["version"], "sequenceVersion": 1}
        and row["reference_taxon_id"] == "NCBITaxon:287"
        and row["reference_taxon_label"] == "Pseudomonas aeruginosa"
        and row["native_reference_taxon_rank"] == "species"
        and row["experimental_allele_assignment"] is row["experimental_genome_assignment"] is None
        and row["native_protein_flag"] is None
        and all(
            row[k] is False
            for k in (
                "explicit_card_xref",
                "submission_name_is_expert_review",
                "unflagged_means_complete",
                "experimental_subject_assignment",
                "exact_allele_assignment",
                "primary_results_reviewed",
            )
        )
        and row["matched_bibliography"]
        == [{"reference_number": 1, "pmid": "PMID:11158753", "doi": "DOI:" + aac6.DOI}],
        "AAC29 reference identity or experimental scope changed",
    )
    return registry.reference_identity(
        {
            "entry_type": row["entry_type"],
            "entry_version": row["entry_audit"]["entryVersion"],
            "sequence_version": row["entry_audit"]["sequenceVersion"],
            "reference_taxon_id": row["reference_taxon_id"],
            "reference_taxon_rank": "species",
            "reference_species_taxon_id": row["reference_taxon_id"],
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
    )


def reconcile_rows(data, result):
    census = progress.index_unique(data["census"], "identifier", "census")
    old_rows = progress.index_unique(data["base_rows"], "identifier", "prior row")
    require(set(census) == set(old_rows), "row coverage changed")
    old_claims, new_claims = defaultdict(list), defaultdict(list)
    for old, new in zip(data["base"]["claims"], result["claims"], strict=True):
        require({**new, "reference_status": old["reference_status"]} == old, "claim identity changed")
        old_claims[old["record_identifier"]].append(old)
        new_claims[new["record_identifier"]].append(new)
    require(set(old_claims) <= set(census), "claim outside census")
    rows = []
    for rid, record in sorted(census.items()):
        old = old_rows[rid]
        counts = Counter(c["reference_status"] for c in old_claims[rid])

        def accessions(index, rid=rid):
            return "|".join(
                sorted(
                    {
                        link["protein_accession"]
                        for c in old_claims[rid]
                        for link in index["terms"][c["aro_id"]]["links"]
                    }
                )
            )

        require(
            all(old[k] == record[k] for k in ("path", "record_sha256", "standard_inchi_key"))
            and int(old["card_assertions"]) == len(old_claims[rid])
            and all(int(old[col]) == counts[status] for status, col in prior.COLUMNS.items())
            and old["selected_reference_accessions"] == accessions(data["base"])
            and old["whole_record_primary_review"] == "OPEN",
            "prior row identity or accounting changed",
        )
        numeric = {
            *prior.COLUMNS.values(),
            "card_assertions",
            "phi_claims_not_reassessed",
            "curator_claims_not_reassessed",
            "score_rules_not_reassessed",
        }
        row = {k: int(v) if k in numeric else v for k, v in old.items()}
        counts = Counter(c["reference_status"] for c in new_claims[rid])
        row.update({col: counts[status] for status, col in COLUMNS.items()})
        row["selected_reference_accessions"] = accessions(result)
        require(
            sum(row[col] for col in COLUMNS.values()) == row["card_assertions"]
            and row["card_assertions"]
            + row["phi_claims_not_reassessed"]
            + row["curator_claims_not_reassessed"]
            == int(record["resistance_assertions"])
            and row["score_rules_not_reassessed"] == int(record["score_rules"]),
            "source accounting changed",
        )
        rows.append(row)
    return rows


def project(data, plan, plan_pin):
    base, dossier, followup = data["base"], data["aac6"], data["aac34"]
    require(
        plan["selection"] == "ALL_CARD_MEMBERSHIPS_WITH_COMPLETE_UNLINKED_AAC6_LABEL_CONTEXT"
        and plan["constraints"]
        == {
            "network_requests": 0,
            "biological_writes": False,
            "experimental_assignments": False,
            "issue_1040": "DEFERRED",
        }
        and base["scope"] == prior.SCOPE
        and base["plan"] == plan["inputs"]["base_plan"]
        and base["inputs"] == data["base_plan"]["inputs"]
        and dossier["scope"] == aac6.SCOPE
        and dossier["inputs"]["index"] == followup["inputs"]["index"] == plan["inputs"]["base"]
        and followup["inputs"]["aac6"] == plan["inputs"]["aac6"]
        and followup["inputs"]["source_queue"] == plan["inputs"]["source_queue"]
        and not any(dossier["disposition"].values())
        and base["limits"]
        == {
            "biological_record_changes": 0,
            "experimental_allele_or_genome_assignments": 0,
            "full_corpus_goal_status": "OPEN",
            "github_mutations": 0,
            "issue_1040": "DEFERRED",
            "ncbi_requests": 0,
            "network_requests": 0,
            "outreach": 0,
            "reuse_terms_review_resumed": False,
            "source_adoptions": 0,
        },
        "index provenance or evidence scope changed",
    )
    for key in (
        "census",
        "curator",
        "source_queue",
        "source_inventory",
        "direct_candidates",
        "ledger",
        "definition_citations",
    ):
        require(plan["inputs"][key] == base["inputs"][key], "source pin changed")
    for name in ("base", "aac6"):
        shared.check_checkpoint(data, plan, name)
    check_aac34(followup)
    primary = dossier["aac34_primary_table_context"]
    require(
        primary["source_term_id"] == aac34.TERM
        and primary["evidence_type"] == "HETEROLOGOUS_FUNCTIONAL_EXPERIMENT"
        and primary["source_isolate_taxon_reference"] == "NCBITaxon:1120679"
        and primary["source_isolate_native_rank"] == "species"
        and primary["assay_host_species_taxon"] == "NCBITaxon:562"
        and all(
            primary[k] is None
            for k in (
                "assay_host_strain_assignment",
                "clinical_resistance_category",
                "exact_corpus_structure_assignment",
                "experimental_protein_assignment",
                "experimental_genome_assignment",
            )
        )
        and primary["native_isolate_MIC_inferred"] is primary["breakpoint_interpretation_applied"] is False,
        "AAC34 primary context promoted to an experimental or chemical identity",
    )
    selected = {
        tid
        for tid, term in base["terms"].items()
        if not term["links"]
        and "aac(6" in data["direct_candidates"]["determinants"][tid]["labels"][0].casefold()
    }
    require(set(dossier["terms"]) == selected and len(selected) == 15, "complete AAC6 label coverage changed")
    claims = [
        {
            "record_identifier": c["record_identifier"],
            "position": c["resistance_index"],
            "aro_id": c["aro_id"],
            "claim_sha256": c["claim_sha256"],
        }
        for c in base["claims"]
        if c["aro_id"] in selected
    ]
    records = progress.index_unique(dossier["records"], "identifier", "AAC6 records")
    census = progress.index_unique(data["census"], "identifier", "census")
    require(
        Counter(map(registry.checksum, claims)) == Counter(map(registry.checksum, dossier["claims"]))
        and len(claims) == 70
        and len(records) == 12
        and set(records) == {c["record_identifier"] for c in claims}
        and all(r == census[rid] for rid, r in records.items())
        and dossier["primary_access_hold"]["http_status"] == 403
        and dossier["primary_access_hold"]["primary_results_reviewed"] is False
        and dossier["primary_access_hold"]["retry_performed"] is False
        and dossier["primary_access_hold"]["alternate_route_used"] is False
        and dossier["primary_access_hold"]["revisit_requires"]
        == "USER_SUPPLIED_PRIMARY_COPY_OR_NEW_EXPLICIT_DIRECTION",
        "AAC6 membership coverage or primary hold changed",
    )
    result = rebase(base)
    for tid in sorted(selected):
        row, old = dossier["terms"][tid], base["terms"][tid]
        status = (
            aac6.REFERENCE
            if tid in TERMS
            else aac6.NO_CITATION
            if not row["definition_citation_ids"]
            else aac6.EMPTY
            if not row["complete_citation_query_accessions"]
            else aac6.AMBIGUOUS
        )
        require(
            row["prior_term"] == old
            and progress.digest(row["source_label"].encode()) == old["source_label_sha256"]
            and row["definition_annotation_sha256"]
            == registry.checksum(data["definition_citations"]["terms"][tid])
            and row["definition_citation_ids"]
            == data["definition_citations"]["terms"][tid]["definition_citation_ids"]
            and row["experimental_subject_assignment"] is row["biological_absence_inferred"] is False
            and row["status"] == status
            and (status == aac6.AMBIGUOUS) is bool(row["related_family_context"]),
            "AAC6 prior term, definition or scope changed",
        )
        result["terms"][tid]["aac6_evidence_followup"] = pointer("aac6", "terms", tid)
    require(
        set(dossier["references"]) == {"UniProtKB:" + a for a in aac6.SELECTED}, "reference coverage changed"
    )
    memberships = []
    for accession, row in sorted(dossier["references"].items()):
        identity = reference_identity(accession, row)
        tid = row["source_term_id"]
        require(
            accession not in result["proteins"]
            and not result["terms"][tid]["links"]
            and dossier["terms"][tid]["reference_candidates"] == [accession]
            and dossier["terms"][tid]["definition_citation_ids"] == ["PMID:11158753"],
            "duplicate reference or source-citation membership changed",
        )
        source = pointer("aac6", "references", accession)
        result["proteins"][accession] = {
            "identity": identity,
            "sources": [source],
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
        result["terms"][tid]["links"] = [
            {
                "protein_accession": accession,
                "kind": QUALIFIED,
                "explicit_card_xref": False,
                "source_citation_ids": ["PMID:11158753"],
                "matched_reference_numbers": [1],
                "source": source,
                "query": pointer("aac6", "citation_queries", "11158753"),
                "experimental_subject_assignment": False,
                "exact_allele_assignment": False,
            }
        ]
        result["terms"][tid]["reference_status"] = QUALIFIED
        memberships.extend(
            {
                "record_identifier": rid,
                "source_term_id": tid,
                "protein_accession": accession,
                "scope": aac6.REFERENCE,
                "experimental_subject_assignment": False,
            }
            for rid in base["terms"][tid]["record_memberships"]
        )
    require(
        Counter(map(registry.checksum, memberships))
        == Counter(map(registry.checksum, dossier["reference_memberships"]))
        and len(memberships) == 10,
        "AAC29 membership coverage changed",
    )
    result["terms"][aac34.TERM]["aac34_reference_followup"] = {"input": "aac34", "pointer": ""}
    result["terms"][aac34.TERM]["aac34_primary_context"] = pointer("aac6", "aac34_primary_table_context")
    for claim in result["claims"]:
        claim["reference_status"] = result["terms"][claim["aro_id"]]["reference_status"]
    rows = reconcile_rows(data, result)
    result.update(
        {
            "date": plan["date"],
            "scope": SCOPE,
            "plan": plan_pin,
            "inputs": plan["inputs"],
            "proteins": dict(sorted(result["proteins"].items())),
            "aac6_reference_reviews": pointer("aac6", "references"),
            "aac6_primary_access_hold": pointer("aac6", "primary_access_hold"),
            "aac6_followup": {"input": "aac6", "pointer": ""},
            "aac34_followup": {"input": "aac34", "pointer": ""},
            "new_reference_memberships": [{**m, "scope": QUALIFIED} for m in memberships],
            "prior_interpretation": pointer("base", "interpretation"),
            "interpretation": [
                "All 15 previously unlinked AAC(6)-label terms retain their distinct evidence dispositions.",
                "Two unreviewed submission-name/gene/citation/taxon references add ten memberships, "
                "not AST observations.",
                "AAC29 primary access remains held after a 403; no retry or alternative route was used.",
                "AAC34 zero name and exact-organism queries are bounded search results, "
                "not biological absence.",
                "The selected reagent paragraph does not resolve Kanamycin to the kanamycin A structure.",
                "No new experimental allele, genome, host-strain or clinical resistance assignment is made.",
                "All inherited reference contexts, primary-access holds and non-CARD source counts remain.",
            ],
            "attribution": {
                "base": base["attribution"],
                "aac6": dossier["attribution"],
                "aac34": followup["attribution"],
            },
            "summary": {
                **copy.deepcopy(base["summary"]),
                "selected_reference_terms": sum(bool(t["links"]) for t in result["terms"].values()),
                "selected_reference_proteins": len(result["proteins"]),
                "reference_links": sum(len(t["links"]) for t in result["terms"].values()),
                "term_statuses": dict(
                    sorted(Counter(t["reference_status"] for t in result["terms"].values()).items())
                ),
                "claim_statuses": dict(
                    sorted(Counter(c["reference_status"] for c in result["claims"]).items())
                ),
                "records_with_selected_references": sum(
                    bool(r["selected_reference_accessions"]) for r in rows
                ),
                "added_reference_terms": 2,
                "added_reference_proteins": 2,
                "added_reference_links": 2,
                "added_reference_memberships": len(memberships),
                "newly_checked_native_reference_entries": 0,
                "reconciled_prior_reference_entries": 2,
                "followup_terms": len(selected),
                "followup_claims": len(claims),
                "followup_records": len(records),
                "new_cohort_summaries": {"aac6": dossier["summary"], "aac34": followup["summary"]},
            },
        }
    )
    return result, rows


def build(root, plan_path=PLAN):
    data, plan, pin = shared.read_inputs(root, plan_path)
    base, rows = prior.build(root, Path(plan["inputs"]["base_plan"]["path"]))
    require(
        base == data["base"]
        and registry.render(base, rows)[1]
        == reference.check_pin(root, plan["inputs"]["base_rows"]).read_bytes(),
        "prior index does not reproduce",
    )
    require(aac6.build(root) == data["aac6"], "native AAC6 dossier does not reproduce")
    require(aac34.build(root) == data["aac34"], "native AAC34 follow-up does not reproduce")
    result, rows = project(data, plan, pin)
    records, _ = progress.current_records(root, data["census"])
    check_live_claims(records, result, rows)
    return result, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output-prefix", default=PREFIX)
    args = parser.parse_args()
    result, rows = build(Path.cwd())
    missing = []
    for suffix, body in zip((".json", ".tsv"), registry.render(result, rows), strict=True):
        path = Path(args.output_prefix + suffix)
        if args.check or path.exists():
            require(path.read_bytes() == body, "AAC6 index does not reproduce")
        else:
            missing.append((path, body))
    for path, body in missing:
        with path.open("xb") as stream:
            stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
