"""Reconcile four saved evidence follow-ups with the complete CARD reference index."""

import argparse
import copy
import json
from collections import Counter, defaultdict
from pathlib import Path

import audit_aac3_evidence as aac3
import audit_card_cytb_outer_memberships as prior
import audit_card_fungal_memberships as shared
import audit_cipa_evidence as cipa
import audit_kpn_evidence as kpn
import audit_vgb_evidence as vgb

reference, require, registry = prior.reference, prior.require, prior.registry
progress, pointer, rebase = prior.progress, prior.pointer, prior.rebase
PREFIX = "research/2026-10-15-card-followup-memberships"
PLAN = Path(PREFIX + "-plan.json")
SCOPE = "CARD_REFERENCE_INDEX_WITH_AAC3_KPN_CIPA_VGB_CONTEXT_NOT_EXPERIMENTAL_GROUNDING"
IIIB = "UNREVIEWED_AAC3_IIIB_EXACT_GENE_TAXON_REFERENCE_ONLY"
UNSELECTED = "NO_PROTEIN_CANDIDATE_IN_SELECTED_INDEX_INPUTS_NOT_BIOLOGICAL_ABSENCE"
COLUMNS = {
    **{k: v for k, v in prior.COLUMNS.items() if k != prior.UNSELECTED},
    IIIB: "unreviewed_aac3_iiib_reference_claims",
    UNSELECTED: "unselected_candidate_claims",
}
FOLLOWUPS = {"aac3": aac3, "kpn": kpn, "cipa": cipa, "vgb": vgb}
TERM, ACCESSION = "ARO:3002537", "UniProtKB:Q51405"


def bind_context(name, data, result):
    dossier, base = data[name], data["base"]
    terms = {dossier["source_term_id"]: dossier["source_term"]} if name == "cipa" else dossier["terms"]
    expected = {"ARO:3003907"} if name == "cipa" else set(FOLLOWUPS[name].TERMS)
    require(set(terms) == expected, "complete follow-up term coverage changed")
    claims = [
        {
            "record_identifier": c["record_identifier"],
            "position": c["resistance_index"],
            "aro_id": c["aro_id"],
            "claim_sha256": c["claim_sha256"],
        }
        for c in base["claims"]
        if c["aro_id"] in terms
    ]
    require(
        Counter(map(registry.checksum, claims)) == Counter(map(registry.checksum, dossier["claims"])),
        "follow-up claim identity or coverage changed",
    )
    census = progress.index_unique(data["census"], "identifier", "census")
    records = progress.index_unique(dossier["records"], "identifier", "follow-up records")
    ids = {c["record_identifier"] for c in claims}
    require(
        set(records) == ids and all(r == census[rid] for rid, r in records.items()),
        "follow-up record identity or coverage changed",
    )
    for tid, term in terms.items():
        old = base["terms"][tid]
        label = dossier["source_label"] if name == "cipa" else term["source_label"]
        require(progress.digest(label.encode()) == old["source_label_sha256"], "source label changed")
        if name in {"aac3", "vgb"}:
            require(
                term["prior_term"] == old
                and term["definition"] == data["definition_citations"]["terms"][tid],
                "prior term or native definition changed",
            )
        elif name == "kpn":
            require(
                term["prior_links"] == old["links"]
                and term["record_memberships"] == old["record_memberships"]
                and term["source_label_sha256"] == old["source_label_sha256"]
                and term["definition_citation_ids"]
                == data["definition_citations"]["terms"][tid]["definition_citation_ids"],
                "complex prior identity changed",
            )
        else:
            require(term == old, "cipA prior identity changed")
        result["terms"][tid][name + "_evidence_followup"] = (
            pointer(name, "source_term") if name == "cipa" else pointer(name, "terms", tid)
        )
    return set(terms), ids, len(claims)


def add_iiib(data, result):
    dossier = data["aac3"]
    row = dossier["new_iiib_gene_reference"]
    require(
        row["accession"] == ACCESSION
        and row["source_term_id"] == TERM
        and row["source_label"] == "AAC(3)-IIIb"
        and row["gene_symbols"] == ["aac(3)-IIIb"]
        and row["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
        and row["entry_audit"] == {"entryVersion": 61, "sequenceVersion": 1}
        and row["reference_taxon_id"] == "NCBITaxon:287"
        and row["reference_taxon_label"] == "Pseudomonas aeruginosa"
        and row["native_reference_taxon_rank"] == "species"
        and row["native_citation_ids"] == ["PMID:30347146"]
        and row["scope"] == "EXACT_SOURCE_GENE_AND_TAXON_REFERENCE_NOT_EXPERIMENTAL_ALLELE"
        and row["experimental_allele_assignment"] is None
        and all(
            row[k] is False
            for k in (
                "experimental_subject_assignment",
                "explicit_card_xref",
                "aro_own_citation_in_native_bibliography",
                "aro_cited_tested_enzyme_equated_with_reference",
                "experimental_identity_primary_review_complete",
            )
        )
        and not any(dossier["disposition"].values()),
        "IIIb reference identity or experimental scope changed",
    )
    queries = dossier["iiib_exact_label_queries"]
    require(set(queries) == {"iiib-reviewed", "iiib-unreviewed"}, "IIIb query coverage changed")
    for key, reviewed in (("iiib-reviewed", True), ("iiib-unreviewed", False)):
        q = queries[key]
        require(
            q["source"]["url"] == aac3.gene_url(reviewed)
            and q["source"]["status"] == 200
            and q["reviewed_subset"] is reviewed
            and q["result_count"] == int(not reviewed)
            and q["complete_for_query"] is True
            and q["biological_absence_inferred"] is q["suggestions_followed"] is False,
            "IIIb reviewed-first query scope changed",
        )
    expected = [
        {
            "record_identifier": rid,
            "source_term_id": TERM,
            "protein_accession": ACCESSION,
            "scope": row["scope"],
            "experimental_allele_assigned": False,
        }
        for rid in data["base"]["terms"][TERM]["record_memberships"]
    ]
    require(dossier["new_gene_reference_memberships"] == expected, "IIIb memberships changed")
    target = result["terms"][TERM]
    require(not target["links"] and ACCESSION not in result["proteins"], "duplicate IIIb reference")
    source = pointer("aac3", "new_iiib_gene_reference")
    identity = registry.reference_identity(
        {
            "entry_type": row["entry_type"],
            "entry_version": row["entry_audit"]["entryVersion"],
            "sequence_version": row["entry_audit"]["sequenceVersion"],
            "reference_taxon_id": row["reference_taxon_id"],
            "reference_taxon_rank": row["native_reference_taxon_rank"],
            "reference_species_taxon_id": row["reference_taxon_id"],
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
    )
    result["proteins"][ACCESSION] = {
        "identity": identity,
        "sources": [source],
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
    }
    target["links"] = [
        {
            "protein_accession": ACCESSION,
            "kind": IIIB,
            "explicit_card_xref": False,
            "source_citation_ids": [],
            "matched_reference_numbers": [],
            "source": source,
            "query": pointer("aac3", "iiib_exact_label_queries", "iiib-unreviewed"),
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
    ]
    target["reference_status"] = IIIB
    target["named_organism_taxon_reference_only"] = pointer("aac3", "iiib_source_organism_context")


def reconcile_rows(data, result):
    census = progress.index_unique(data["census"], "identifier", "census")
    old_rows = progress.index_unique(data["base_rows"], "identifier", "prior rows")
    require(set(old_rows) == set(census), "record coverage changed")
    old_claims, new_claims = defaultdict(list), defaultdict(list)
    for old, claim in zip(data["base"]["claims"], result["claims"], strict=True):
        require({**claim, "reference_status": old["reference_status"]} == old, "claim identity changed")
        old_claims[old["record_identifier"]].append(old)
        new_claims[claim["record_identifier"]].append(claim)
    require(set(new_claims) <= set(census), "claim outside census")
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
            "prior row identity or counts changed",
        )
        row = {
            k: int(v)
            if k
            in {
                *prior.COLUMNS.values(),
                "card_assertions",
                "phi_claims_not_reassessed",
                "curator_claims_not_reassessed",
                "score_rules_not_reassessed",
            }
            else v
            for k, v in old.items()
        }
        counts = Counter(c["reference_status"] for c in new_claims[rid])
        row.update({col: counts[status] for status, col in COLUMNS.items()})
        row["selected_reference_accessions"] = accessions(result)
        require(
            sum(row[c] for c in COLUMNS.values()) == row["card_assertions"]
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
    base = data["base"]
    require(
        plan["selection"] == "ALL_CARD_MEMBERSHIPS_WITH_AAC3_KPN_CIPA_VGB_FOLLOWUPS"
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
        "index provenance or limits changed",
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
        require(plan["inputs"][key] == base["inputs"][key], "successor source pin changed")
    for name in ("base", *FOLLOWUPS):
        shared.check_checkpoint(data, plan, name)
    result = rebase(base)
    for term in result["terms"].values():
        require(
            term["experimental_subject_assignment"] is False
            and term["whole_record_primary_review"] == "OPEN"
            and term["reference_status"] in prior.COLUMNS
            and bool(term["links"]) is (term["reference_status"] != prior.UNSELECTED),
            "prior term scope changed",
        )
        if not term["links"]:
            term["reference_status"] = UNSELECTED
    touched, records, claim_count = set(), set(), 0
    for name, module in FOLLOWUPS.items():
        require(data[name]["scope"] == module.SCOPE, "follow-up evidence scope changed")
        terms, ids, count = bind_context(name, data, result)
        require(not touched & terms, "overlapping follow-up term coverage")
        touched.update(terms)
        records.update(ids)
        claim_count += count
    add_iiib(data, result)
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
            "evidence_followups": {name: {"input": name, "pointer": ""} for name in FOLLOWUPS},
            "prior_interpretation": pointer("base", "interpretation"),
            "interpretation": [
                "Selected reference inputs and four evidence follow-ups, "
                "not whole-corpus experimental signoff.",
                "Only AAC(3)-IIIb/Q51405 adds a gene-reference link; "
                "nine memberships are not nine AST results.",
                "The unreviewed reference has no explicit CARD xref "
                "or established experimental allele identity.",
                "Generic type-IV references are not exact IVa; "
                "Kpn complexes, cipA and Vgb retain their qualified context.",
                "All access holds and primary-review limitations remain in their pinned dossiers.",
                "No-candidate status means no reference in these selected index inputs, "
                "not biological absence.",
                "PHI, curator, HIVDB and no-claim records are retained, not reassessed by this index update.",
            ],
            "attribution": {name: data[name]["attribution"] for name in ("base", *FOLLOWUPS)},
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
                "added_reference_memberships": len(data["aac3"]["new_gene_reference_memberships"]),
                "followup_terms": len(touched),
                "followup_claims": claim_count,
                "followup_records": len(records),
                "new_cohort_summaries": {name: data[name]["summary"] for name in FOLLOWUPS},
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
    for name, module in FOLLOWUPS.items():
        require(module.build(root) == data[name], "native follow-up does not reproduce")
    result, rows = project(data, plan, pin)
    records, _ = progress.current_records(root, data["census"])
    prior.prior.live.check_live_claims(records, result, rows)
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
            require(path.read_bytes() == body, "follow-up index does not reproduce")
        else:
            missing.append((path, body))
    for path, body in missing:
        with path.open("xb") as stream:
            stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
