"""Reconcile three verified follow-ups while retaining every historical evidence binding."""

import argparse
import copy
import json
from collections import Counter
from pathlib import Path

import audit_card_reference_successor as prior_audit

previous = prior_audit.previous
reference = prior_audit.reference
require = prior_audit.require
pointer = prior_audit.pointer
PREFIX = "research/2026-10-15-card-reference-reconciled"
PLAN = Path(PREFIX + "-plan.json")
SCOPE = "RECONCILED_CURRENT_CORPUS_REFERENCES_NOT_EXPERIMENTAL_GROUNDING"
PRIOR = "prior_successor_index"
QUALIFIED = ["rifampin-inactivation-context", "msh-hmg-reference"]
CONTEXT = ["bla-recent-identifiers"]
SELECTED = {
    "ARO:3000390": ("rifampin-inactivation-context", "UniProtKB:A0QRS5"),
    "ARO:3009134": ("msh-hmg-reference", "UniProtKB:Q6FQA9"),
    "ARO:3007670": ("msh-hmg-reference", "UniProtKB:Q4WHZ1"),
}
CONSTRAINTS = dict(prior_audit.CONSTRAINTS)


def read_inputs(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["constraints"] == CONSTRAINTS
        and plan["qualified_dossiers"] == QUALIFIED
        and plan["context_only_dossiers"] == CONTEXT,
        "reconciliation scope changed",
    )
    data = {}
    for name, pin in plan["inputs"].items():
        body = reference.check_pin(root, pin).read_bytes()
        data[name] = previous.progress.read_tsv(body) if pin["path"].endswith(".tsv") else json.loads(body)
    prior = data[PRIOR]
    require(prior["scope"] == prior_audit.SCOPE, "wrong predecessor")
    require(
        all(plan["inputs"].get(k) == v for k, v in prior["inputs"].items()),
        "inherited evidence pointer rebound",
    )
    require(
        set(plan["inputs"]) - set(prior["inputs"])
        == {k for name in [PRIOR, *QUALIFIED, *CONTEXT] for k in (name, name + "_verification")},
        "unexpected reconciliation inputs",
    )
    for name in [PRIOR, *QUALIFIED, *CONTEXT]:
        require(
            previous.contains_pin(data[name + "_verification"], plan["inputs"][name]), "dossier not verified"
        )
    return plan, data


def selected_identity(term, candidate, dossier):
    require(
        candidate["accession"] == SELECTED[term][1]
        and all(v is None for k, v in candidate.items() if k.startswith("experimental_")),
        "reference accession or experimental scope changed",
    )
    if term == "ARO:3000390":
        require(
            candidate["single_protein_identity_for_whole_arr_family"] is False
            and candidate["scope"]
            == "STRUCTURE_LINKED_ARR_MS_FAMILY_MEMBER_REFERENCE_NOT_EXPERIMENTAL_ALLELE"
            and candidate["structure_entity"] == "2HW2_1",
            "Arr family member scope changed",
        )
        raw = {
            **candidate["identity"],
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
    else:
        native = candidate["native_reference"]
        require(
            candidate["scope"] == "ONE_SOURCE_SPECIES_GENE_REFERENCE_NOT_FAMILY_WIDE_OR_EXPERIMENTAL_ALLELE"
            and candidate["direct_drug_target_inferred"] is False
            and candidate["resistance_phenotype_from_protein_annotation"] is False
            and native["experimental_subject_assignment"] is False
            and native["exact_resistance_allele"] is False
            and candidate["native_gene_matches"]
            and candidate["native_locus_matches"],
            "fungal gene reference scope changed",
        )
        raw = {
            **native,
            "reference_species_taxon_id": native["source_species_taxon_id"],
            "exact_allele_assignment": False,
        }
    identity = previous.registry.reference_identity(raw)
    expected = {
        "ARO:3000390": ("NCBITaxon:246196", "NCBITaxon:1772"),
        "ARO:3009134": ("NCBITaxon:284593", "NCBITaxon:5478"),
        "ARO:3007670": ("NCBITaxon:330879", "NCBITaxon:746128"),
    }[term]
    require(
        (identity["reference_taxon_id"], identity["reference_species_taxon_id"]) == expected
        and identity["reference_taxon_rank"] == "strain",
        "source reference taxonomy changed",
    )
    node = dossier["native_taxonomy"][expected[0].split(":")[1]]
    species = dossier["native_taxonomy"][expected[1].split(":")[1]]
    _, ancestor = prior_audit.taxonomy.lineage(node)
    prior_audit.taxonomy.lineage(species)
    require(ancestor == prior_audit.taxonomy.identity(species), "reference species lineage changed")
    return identity


def reconcile(prior, dossiers):
    require(set(dossiers) == set(QUALIFIED + CONTEXT), "dossier cohort changed")
    result = copy.deepcopy(prior)
    terms, proteins = result["terms"], result["proteins"]
    added = set()
    result["reconciled_followups"] = {}
    for name, dossier in dossiers.items():
        prior_audit.bind_dossier(prior, dossier)
        result["reconciled_followups"][name] = {
            "source": {"input": name, "pointer": ""},
            "aro_ids": sorted(dossier["terms"]),
            "experimental_identity_assigned": False,
        }
        if name in CONTEXT:
            result["context_only_followups"][name] = {
                "source": {"input": name, "pointer": ""},
                "aro_ids": sorted(dossier["terms"]),
                "promotes_component_or_lead_to_whole_determinant": False,
            }
        for term, row in dossier["terms"].items():
            terms[term]["followups"].append(pointer(name, "terms", term))
            if term not in SELECTED:
                require(
                    not row["reference_accessions"] and not row["references"],
                    "unreviewed reference in context-only term",
                )
                continue
            expected_name, accession = SELECTED[term]
            require(
                name == expected_name
                and len(row["references"]) == 1
                and row["reference_accessions"] == [accession]
                and not terms[term]["reference_links"]
                and term not in added,
                "missing, duplicate or already-linked reference",
            )
            candidate = row["references"][0]
            identity = selected_identity(term, candidate, dossier)
            evidence = pointer(name, "terms", term, "references", 0)
            previous.add_reference(proteins, accession, identity, evidence)
            terms[term]["reference_accessions"] = [accession]
            terms[term]["reference_status"] = "REFERENCE_CONTEXT_NOT_EXPERIMENTAL_GROUNDING"
            terms[term]["reference_links"].append(
                {
                    "protein_accession": accession,
                    "kind": candidate["scope"],
                    "evidence": evidence,
                    "experimental_subject_assignment": False,
                    "exact_allele_assignment": False,
                }
            )
            added.add(term)
    require(added == set(SELECTED), "incomplete reference integration")
    excluded = dossiers["msh-hmg-reference"]["excluded_same_citation_candidate"]
    require(
        excluded["accession"] == "UniProtKB:B0YA65"
        and excluded["native_gene"] == "erg10B"
        and excluded["eligible_as_hmg1_reference"] is False,
        "same-citation comparator promoted",
    )
    require("ARO:3007670" not in result["comparison_contexts"], "comparator context already exists")
    result["comparison_contexts"]["ARO:3007670"] = [
        {
            "protein_accession": excluded["accession"],
            "evidence": pointer("msh-hmg-reference", "excluded_same_citation_candidate"),
            "included_in_determinant_reference_counts": False,
        }
    ]
    result["proteins"] = dict(sorted(proteins.items()))
    result["unresolved_reference_worklist"] = [
        {**row, "followups": terms[row["aro_id"]]["followups"]}
        for row in prior["unresolved_reference_worklist"]
        if row["aro_id"] not in added
    ]
    return result


def build(root):
    plan, data = read_inputs(root)
    prior = data[PRIOR]
    dossiers = {name: data[name] for name in QUALIFIED + CONTEXT}
    result = reconcile(prior, dossiers)
    rows, claims = prior_audit.rebind_current(root, prior, result["terms"])
    result.update(
        {
            "date": plan["date"],
            "scope": SCOPE,
            "plan": reference.pin(root, root / PLAN),
            "inputs": plan["inputs"],
            "predecessor_index": {"input": PRIOR, "pointer": ""},
            "records": rows,
            "claims": claims,
            "constraints": CONSTRAINTS,
        }
    )
    terms, proteins = result["terms"], result["proteins"]
    result["summary"] = {
        **prior["summary"],
        "complete_collection_aware_records_read": len(rows),
        "selected_reference_terms": sum(bool(t["reference_links"]) for t in terms.values()),
        "unresolved_reference_terms": len(result["unresolved_reference_worklist"]),
        "selected_reference_proteins": len(proteins),
        "reference_links": sum(len(t["reference_links"]) for t in terms.values()),
        "added_reference_terms": len(SELECTED),
        "added_reference_links": len(SELECTED),
        "added_reference_proteins": len(set(proteins) - set(prior["proteins"])),
        "added_claim_memberships_with_references": sum(len(terms[t]["record_memberships"]) for t in SELECTED),
        "records_with_reference_context": sum(bool(r["reference_accessions"]) for r in rows),
        "qualified_followup_dossiers": prior["summary"]["qualified_followup_dossiers"] + len(QUALIFIED),
        "context_only_dossiers": len(result["context_only_followups"]),
        "new_followup_dossiers": len(dossiers),
        "new_followup_terms": len({t for d in dossiers.values() for t in d["terms"]}),
        "new_followup_claims": sum(len(d["claims"]) for d in dossiers.values()),
        "new_followup_records": len({r["identifier"] for d in dossiers.values() for r in d["records"]}),
        "comparators_excluded_from_reference_counts": sum(
            len(v) for v in result["comparison_contexts"].values()
        ),
        "current_source_qualified_claims": sum(
            c["claim_sha256"] != c["historical_claim_sha256"] for c in claims
        ),
        "unresolved_reference_scope_counts": dict(
            sorted(Counter(r["source_scope"] for r in result["unresolved_reference_worklist"]).items())
        ),
    }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    result = build(root)
    if args.write:
        for suffix, body in (
            (".json", json.dumps(result, indent=2, sort_keys=True) + "\n"),
            (".tsv", previous.render_rows(result["records"])),
        ):
            with (root / (PREFIX + suffix)).open("x") as stream:
                stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
