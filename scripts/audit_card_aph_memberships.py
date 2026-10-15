"""Reconcile APH/ANT/aad/mph follow-ups with every CARD reference membership."""

import argparse
import copy
import json
from collections import Counter, defaultdict
from pathlib import Path

import audit_aph_ant_aad_mph_gaps as gaps
import audit_card_aac6_memberships as prior
from audit_card_reference_lineages import lineage
from audit_card_topoisomerase_memberships import check_live_claims

reference, require, registry = prior.reference, prior.require, prior.registry
progress, pointer, rebase, shared = prior.progress, prior.pointer, prior.rebase, prior.shared
PREFIX = "research/2026-10-15-card-aph-memberships"
PLAN = Path(PREFIX + "-plan.json")
SCOPE = "CARD_REFERENCE_INDEX_WITH_APH_ANT_AAD_MPH_FOLLOWUPS_NOT_EXPERIMENTAL_ALLELES"
QUALIFIED = "UNREVIEWED_APH_NOMENCLATURE_CITATION_TAXON_REFERENCE_ONLY"
COLUMNS = {**prior.COLUMNS, QUALIFIED: "unreviewed_aph_nomenclature_reference_claims"}
UNSELECTED = prior.UNSELECTED


def reference_identity(row):
    taxon, review = row["reference_taxonomy"], row["historical_nomenclature_review"]
    nodes, species = lineage(
        {
            "taxonId": 37734,
            "scientificName": taxon["scientific_name"],
            "rank": taxon["native_rank"],
            "active": taxon["active"],
            "parent": taxon["parent"],
            "lineage": taxon["lineage"][:-1],
        }
    )
    require(
        row["accession"] == gaps.ACCESSION
        and row["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
        and row["entry_audit"] == {"entryVersion": 113, "sequenceVersion": 1}
        and row["gene_symbols"] == ["aph(2'')-Id"]
        and row["protein_names"] == [{"field": "submissionNames", "index": 0, "value": "APH(2'')-Id"}]
        and row["scope"] == gaps.QUALIFIED
        and row["source_citation"] == "PMID:9593155"
        and taxon["taxon_id"] == "NCBITaxon:37734"
        and taxon["scientific_name"] == "Enterococcus casseliflavus"
        and taxon["native_rank"] == "species"
        and nodes == taxon["lineage"]
        and species == nodes[-1]
        and taxon["experimental_subject_assignment"] is taxon["strain_label_in_name_changes_rank"] is False
        and review["source_name"] == "APH(2'')-Id"
        and review["revised_name"] == "APH(2'')-IVa"
        and review["reference"] == "PMID:19158087"
        and review["doi"] == "10.1074/jbc.M808148200"
        and review["decision"] == "EXPLICIT_REFERENCE_NOMENCLATURE_RELATION_VERIFIED"
        and review["review_medium"] == "PUBLISHER_INDEXED_PRIMARY_DISCUSSION_TEXT"
        and all(
            review[k] is False
            for k in (
                "native_primary_file_cached",
                "table_5_visually_inspected",
                "figures_visually_inspected",
                "supplements_inspected",
                "whole_paper_review_complete",
            )
        )
        and row["structural_reference"]
        == {"pdb_id": "3N4T", "entity_id": "3N4T_1", "protein_accession": gaps.ACCESSION}
        and row["native_protein_flag"] is row["experimental_genome_assignment"] is None
        and all(
            row[k] is False
            for k in (
                "explicit_card_xref",
                "submission_name_is_expert_review",
                "unflagged_means_complete",
                "nomenclature_primary_text_replayed_here",
                "new_primary_results_review",
                "experimental_subject_assignment",
                "exact_allele_assignment",
            )
        ),
        "APH reference identity or evidence scope changed",
    )
    bibliography = row["native_bibliography"]
    require(
        [b["reference_number"] for b in bibliography] == list(range(1, 12))
        and Counter(b["citation_type"] for b in bibliography) == {"journal article": 10, "submission": 1}
        and bibliography[0]["identifiers"] == [{"database": "PubMed", "id": "9593155"}],
        "APH reference bibliography changed",
    )
    return registry.reference_identity(
        {
            "entry_type": row["entry_type"],
            "entry_version": row["entry_audit"]["entryVersion"],
            "sequence_version": row["entry_audit"]["sequenceVersion"],
            "reference_taxon_id": taxon["taxon_id"],
            "reference_taxon_rank": taxon["native_rank"],
            "reference_species_taxon_id": taxon["taxon_id"],
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
    )


def reconcile_rows(data, result):
    census = progress.index_unique(data["census"], "identifier", "census")
    previous = progress.index_unique(data["base_rows"], "identifier", "prior row")
    require(set(census) == set(previous), "row coverage changed")
    old_claims, new_claims = defaultdict(list), defaultdict(list)
    for old, new in zip(data["base"]["claims"], result["claims"], strict=True):
        require({**new, "reference_status": old["reference_status"]} == old, "claim identity changed")
        old_claims[old["record_identifier"]].append(old)
        new_claims[new["record_identifier"]].append(new)
    require(set(old_claims) <= set(census), "claim outside census")
    rows = []
    numeric = {
        *prior.COLUMNS.values(),
        "card_assertions",
        "phi_claims_not_reassessed",
        "curator_claims_not_reassessed",
        "score_rules_not_reassessed",
    }
    for rid, record in sorted(census.items()):
        old = previous[rid]
        old_counts = Counter(c["reference_status"] for c in old_claims[rid])

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
            and all(int(old[col]) == old_counts[status] for status, col in prior.COLUMNS.items())
            and old["selected_reference_accessions"] == accessions(data["base"])
            and old["whole_record_primary_review"] == "OPEN",
            "prior row identity or accounting changed",
        )
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
    base, dossier, gap_plan = data["base"], data["gaps"], data["gaps_plan"]
    require(
        plan["selection"] == "ALL_CARD_MEMBERSHIPS_WITH_COMPLETE_UNLINKED_APH_ANT_AAD_MPH_LABEL_CONTEXT"
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
        and dossier["scope"] == gaps.SCOPE
        and dossier["plan"] == plan["inputs"]["gaps_plan"]
        and dossier["inputs"] == gap_plan["inputs"]
        and dossier["inputs"]["index"] == plan["inputs"]["base"]
        and dossier["inputs"]["index_verification"] == plan["inputs"]["base_verification"],
        "successor provenance or scope changed",
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
        if key in dossier["inputs"]:
            require(plan["inputs"][key] == dossier["inputs"][key], "cohort source pin changed")
    shared.check_checkpoint(data, plan, "base")
    receipt = data["gaps_verification"]
    require(
        plan["inputs"]["gaps"] in receipt["files"]
        and plan["inputs"]["gaps_plan"] in receipt["files"]
        and receipt["summary"] == dossier["summary"]
        and receipt["biological_record_changes"] == receipt["whole_record_primary_signoffs"] == 0
        and receipt["full_corpus_goal_status"] == "OPEN"
        and receipt["broad_index_updated"] is False
        and dossier["limits"]
        == {
            "network_requests": 0,
            "ncbi_requests": 0,
            "biological_records_changed": 0,
            "new_primary_results_reviews": 0,
            "experimental_assignments": 0,
            "curated_ast_observations": 0,
            "primary_access_holds_retried": 0,
            "source_adoptions": 0,
            "outreach": 0,
            "github_mutations": 0,
            "all_aliases_or_sources_searched": False,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "whole_record_primary_signoffs": 0,
            "broad_index_updated": False,
            "full_corpus_goal_status": "OPEN",
        },
        "cohort checkpoint receipt or limits changed",
    )
    selected = gaps.select_terms(base, data["direct_candidates"])
    claims = [c for c in base["claims"] if c["aro_id"] in selected]
    records = progress.index_unique(dossier["records"], "identifier", "cohort record")
    census = progress.index_unique(data["census"], "identifier", "census")
    require(
        set(dossier["terms"]) == set(selected)
        and selected == gap_plan["terms"]
        and len(selected) == 14
        and dossier["claims"] == claims
        and len(claims) == 38
        and len(records) == 16
        and set(records) == {c["record_identifier"] for c in claims}
        and all(row == census[rid] for rid, row in records.items())
        and set(dossier["citation_queries"]) == set(gap_plan["queries"])
        and len(dossier["citation_queries"]) == 14,
        "complete cohort or membership coverage changed",
    )
    for pmid, query in dossier["citation_queries"].items():
        require(
            query == gap_plan["queries"][pmid]["query"]
            and query["complete_for_query"] is True
            and query["release"] == "2026_03"
            and query["establishes_biological_absence"] is False
            and type(query["result_count"]) is int
            and query["result_count"] == len(gap_plan["queries"][pmid]["accessions"]),
            "citation query scope changed",
        )
    result = rebase(base)
    for tid, label in selected.items():
        row, old = dossier["terms"][tid], base["terms"][tid]
        definition = data["definition_citations"]["terms"][tid]
        accessions = sorted(
            {
                "UniProtKB:" + a
                for pmid in definition["definition_citation_ids"]
                for a in gap_plan["queries"][pmid.removeprefix("PMID:")]["accessions"]
            }
        )
        status = gaps.QUALIFIED if tid == gaps.TERM else gaps.UNMATCHED if accessions else gaps.EMPTY
        require(
            row["source_label"] == label
            and progress.digest(label.encode()) == old["source_label_sha256"]
            and row["record_memberships"] == old["record_memberships"]
            and row["definition_citation_ids"] == definition["definition_citation_ids"]
            and row["definition_annotation_sha256"] == registry.checksum(definition)
            and row["complete_citation_query_accessions"] == accessions
            and row["status"] == status
            and row["reference_candidates"] == ([gaps.ACCESSION] if tid == gaps.TERM else [])
            and row["other_citation_hits_not_selected"] == ([] if tid == gaps.TERM else accessions)
            and row["literal_name_match_found"]
            is row["experimental_subject_assignment"]
            is row["biological_absence_inferred"]
            is False,
            "cohort term evidence or disposition changed",
        )
        result["terms"][tid]["aph_ant_aad_mph_followup"] = pointer("gaps", "terms", tid)
    require(
        set(dossier["references"]) == {gaps.ACCESSION}
        and gaps.ACCESSION not in result["proteins"]
        and not result["terms"][gaps.TERM]["links"],
        "reference coverage or duplication changed",
    )
    identity = reference_identity(dossier["references"][gaps.ACCESSION])
    source = pointer("gaps", "references", gaps.ACCESSION)
    result["proteins"][gaps.ACCESSION] = {
        "identity": identity,
        "sources": [source],
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
    }
    result["terms"][gaps.TERM]["links"] = [
        {
            "protein_accession": gaps.ACCESSION,
            "kind": QUALIFIED,
            "explicit_card_xref": False,
            "source_citation_ids": ["PMID:9593155"],
            "matched_reference_numbers": [1],
            "source": source,
            "query": pointer("gaps", "citation_queries", "9593155"),
            "nomenclature_evidence": pointer(
                "gaps", "references", gaps.ACCESSION, "historical_nomenclature_review"
            ),
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
    ]
    result["terms"][gaps.TERM]["reference_status"] = QUALIFIED
    memberships = [
        {
            "record_identifier": rid,
            "source_term_id": gaps.TERM,
            "protein_accession": gaps.ACCESSION,
            "scope": gaps.QUALIFIED,
            "experimental_subject_assignment": False,
        }
        for rid in base["terms"][gaps.TERM]["record_memberships"]
    ]
    require(
        memberships == dossier["reference_memberships"] and len(memberships) == 4,
        "qualified membership coverage changed",
    )
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
            "aph_ant_aad_mph_followup": {"input": "gaps", "pointer": ""},
            "aph_historical_access_limitations": pointer("gaps", "inherited_access_limitations"),
            "new_reference_memberships": [{**m, "scope": QUALIFIED} for m in memberships],
            "prior_interpretation": pointer("base", "interpretation"),
            "prior_summary": pointer("base", "summary"),
            "interpretation": [
                "All 14 prefix-selected APH/ANT/aad/mph follow-ups retain their distinct dispositions.",
                "One unreviewed nomenclature/citation/taxon reference adds four memberships, "
                "not AST observations.",
                "The historical Id-to-IVa assessment is reused; its primary text was not replayed here.",
                "Submission names and reference taxonomy do not identify experimental alleles, "
                "hosts or genomes.",
                "Seven nonmatching-hit and six empty-query terms remain unselected, not biologically absent.",
                "All inherited references, access holds, record identities and non-CARD "
                "source counts remain.",
            ],
            "attribution": {"base": base["attribution"], "gaps": dossier["attribution"]},
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
                "added_reference_terms": 1,
                "added_reference_proteins": 1,
                "added_reference_links": 1,
                "added_reference_memberships": len(memberships),
                "additional_evidence_for_existing_links": 0,
                "newly_checked_native_reference_entries": 0,
                "reconciled_prior_reference_entries": 1,
                "followup_terms": len(selected),
                "followup_claims": len(claims),
                "followup_records": len(records),
                "new_cohort_summaries": {"aph_ant_aad_mph": dossier["summary"]},
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
    require(gaps.build(root) == data["gaps"], "native cohort dossier does not reproduce")
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
            require(path.read_bytes() == body, "APH index does not reproduce")
        else:
            missing.append((path, body))
    for path, body in missing:
        with path.open("xb") as stream:
            stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
