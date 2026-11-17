"""Advance corpus bindings through the note-only Salmonella qualification."""

import argparse
import copy
import json
from pathlib import Path

import audit_card_reference_reconciled as prior_audit

previous = prior_audit.previous
reference, require = previous.reference, previous.require
PREFIX = "research/2026-10-16-card-qualified-current"
PLAN = Path(PREFIX + "-plan.json")
PRIOR = "pre_salmonella_index"
FOLLOWUP = "salmonella_evidence_scope"
SCOPE = "CURRENT_CORPUS_AFTER_NOTE_QUALIFICATION_NOT_EXPERIMENTAL_GROUNDING"


def read_inputs(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(plan["scope"] == SCOPE and plan["constraints"] == prior_audit.CONSTRAINTS, "scope changed")
    data = {}
    for name, pin in plan["inputs"].items():
        body = reference.check_pin(root, pin).read_bytes()
        data[name] = previous.progress.read_tsv(body) if pin["path"].endswith(".tsv") else json.loads(body)
    prior = data[PRIOR]
    require(prior["scope"] == prior_audit.SCOPE, "unexpected prior index")
    transition = data["salmonella_transition"]
    old_review = prior["inputs"]["active_reviews"]
    archive = transition["historical_review_fixture"]
    require(
        old_review["sha256"] == archive["sha256"] == transition["review_file"]["before_sha256"]
        and plan["inputs"]["active_reviews"] == archive
        and plan["inputs"]["salmonella_active_reviews"]["sha256"] == transition["review_file"]["after_sha256"]
        and plan["relocated_historical_inputs"] == {"active_reviews": {"from": old_review, "to": archive}},
        "historical review relocation or current review pin changed",
    )
    require(
        all(plan["inputs"].get(k) == v for k, v in prior["inputs"].items() if k != "active_reviews")
        and set(plan["inputs"]) - set(prior["inputs"])
        == {PRIOR, FOLLOWUP, "salmonella_transition", "salmonella_active_reviews"},
        "inherited evidence bindings changed",
    )
    prior_audit.prior_audit.bind_dossier(prior, data[FOLLOWUP])
    old = copy.deepcopy(data["active_reviews"])
    added = data["salmonella_active_reviews"]["reviews"][-1]
    draft = json.loads(reference.check_pin(root, transition["proposed_review"]).read_bytes())
    require(draft["reviews"] == [added], "active qualification differs from reviewed draft")
    old["reviews"] += [added]
    require(old == data["salmonella_active_reviews"], "unreviewed active review change")
    require(
        len(transition["record_deltas"]) == 17
        and transition["new_evidence_qualification_claims"] == 13
        and transition["existing_note_provenance_updates"] == 4
        and transition["experimental_identifiers_assigned"] == transition["ncbi_requests"] == 0
        and transition["issue_1040"] == "DEFERRED",
        "qualification scope changed",
    )
    return plan, data


def bind_current(root, prior, transition, terms):
    census = [{
        **row,
        "resistance_assertions": sum(row[k] for k in (
            "card_assertions", "phi_claims_not_reassessed", "curator_claims_not_reassessed"
        )),
        "score_rules": row["score_rules_not_reassessed"],
        "activity_observations": row["activity_observations_not_reassessed"],
    } for row in prior["records"]]
    current = previous.current_census(census, [transition])
    records, _ = previous.progress.current_records(root, current)
    rows, claims = previous.bind_records(records, prior, terms, [transition])
    for claim, old in zip(claims, prior["claims"], strict=True):
        claim["historical_claim_sha256"] = old["historical_claim_sha256"]
        require(
            {**claim, **{k: old[k] for k in ("claim_sha256", "record_sha256")}} == old,
            "claim changed beyond the documented qualification",
        )
    for row, old in zip(rows, prior["records"], strict=True):
        require({**row, "record_sha256": old["record_sha256"]} == old, "record membership changed")
    changed_claims = sum(
        c["claim_sha256"] != o["claim_sha256"] for c, o in zip(claims, prior["claims"], strict=True)
    )
    changed_records = sum(
        r["record_sha256"] != o["record_sha256"] for r, o in zip(rows, prior["records"], strict=True)
    )
    require(changed_claims == changed_records == 17, "qualification delta count changed")
    return rows, claims


def build(root):
    plan, data = read_inputs(root)
    prior, transition = data[PRIOR], data["salmonella_transition"]
    result = copy.deepcopy(prior)
    terms = result["terms"]
    require(set(data[FOLLOWUP]["terms"]) == {"ARO:3003307", "ARO:3003317"}, "follow-up term scope changed")
    for term in data[FOLLOWUP]["terms"]:
        terms[term]["followups"].append(previous.pointer(FOLLOWUP, "terms", term))
    result["unresolved_reference_worklist"] = [
        {**row, "followups": terms[row["aro_id"]]["followups"]}
        for row in prior["unresolved_reference_worklist"]
    ]
    result["context_only_followups"][FOLLOWUP] = {
        "source": {"input": FOLLOWUP, "pointer": ""},
        "aro_ids": sorted(data[FOLLOWUP]["terms"]),
        "promotes_component_or_lead_to_whole_determinant": False,
    }
    rows, claims = bind_current(root, prior, transition, terms)
    result.update({
        "date": "2026-10-16", "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN), "inputs": plan["inputs"],
        "constraints": plan["constraints"], "records": rows, "claims": claims,
        "relocated_historical_inputs": plan["relocated_historical_inputs"],
        "current_qualification": {
            "transition": plan["inputs"]["salmonella_transition"],
            "active_reviews": plan["inputs"]["salmonella_active_reviews"],
            "source_qualified_claims": 17, "new_notes": 13, "existing_note_provenance_updates": 4,
            "experimental_identifiers_assigned": False,
        },
    })
    result["summary"].update({
        "current_source_qualified_claims": 17,
        "context_only_dossiers": len(result["context_only_followups"]),
        "added_reference_terms": 0, "added_reference_links": 0,
        "added_reference_proteins": 0, "added_claim_memberships_with_references": 0,
        "new_followup_claims": 26, "new_followup_dossiers": 1,
        "new_followup_records": 13, "new_followup_terms": 2,
    })
    result["qualification_update_summary"] = {
        "records_checked": len(rows), "card_claims_checked": len(claims),
        "records_with_note_history_changes": 17, "unchanged_records": len(rows) - 17,
        "new_reference_terms": 0, "new_reference_proteins": 0,
        "selected_reference_terms": 1405, "unresolved_reference_terms": 597,
        "experimental_assignments": 0, "whole_record_primary_signoffs": 0,
    }
    require(result["proteins"] == prior["proteins"], "reference protein registry changed")
    require(
        len(rows) == 2939 and len(claims) == 4538 and len(terms) == 2002
        and sum(bool(t["reference_links"]) for t in terms.values()) == 1405
        and len(result["unresolved_reference_worklist"]) == 597,
        "full corpus accounting changed",
    )
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true", help="write research exports only")
    args = parser.parse_args()
    result = build(args.root)
    for suffix, text in (
        (".json", json.dumps(result, indent=2, sort_keys=True) + "\n"),
        (".tsv", previous.render_rows(result["records"])),
    ):
        path = args.root / (PREFIX + suffix)
        if args.write:
            path.write_text(text)
        else:
            require(path.read_text() == text, f"export drift: {path}")
    print(json.dumps(result["qualification_update_summary"], sort_keys=True))


if __name__ == "__main__":
    main()
