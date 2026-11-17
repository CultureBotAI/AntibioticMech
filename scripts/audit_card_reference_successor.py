"""Integrate five verified dossiers without rewriting their historical index."""

import argparse
import copy
import json
from collections import Counter
from pathlib import Path

import audit_card_current_references as previous
import audit_card_reference_lineages as taxonomy

reference = previous.reference
require = previous.require
pointer = previous.pointer
PREFIX = "research/2026-10-15-card-reference-successor"
PLAN = Path(PREFIX + "-plan.json")
SCOPE = "CURRENT_CORPUS_REFERENCE_SUCCESSOR_NOT_EXPERIMENTAL_GROUNDING"
QUALIFIED = ["sal-reference-context", "dnaa-sigma-hp1184"]
CONTEXT = ["bla-primary-identifiers", "aph-mph-primary", "pjm-amz-primary"]
SELECTED = {
    "ARO:3007028": "UniProtKB:A0ABQ0Y1N0",
    "ARO:3000248": "UniProtKB:P03004",
    "ARO:3000261": "UniProtKB:P0AGB3",
    "ARO:3003965": "UniProtKB:O25796",
}
CONSTRAINTS = {
    "network_requests": 0,
    "ncbi_requests": 0,
    "biological_record_writes": False,
    "experimental_identifiers_assigned": False,
    "new_primary_reviews": 0,
    "issue_1040": "DEFERRED",
    "full_investigation_complete": False,
}


def read_inputs(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["constraints"] == CONSTRAINTS
        and plan["qualified_dossiers"] == QUALIFIED
        and plan["context_only_dossiers"] == CONTEXT,
        "successor scope changed",
    )
    data = {}
    for name, pin in plan["inputs"].items():
        body = reference.check_pin(root, pin).read_bytes()
        data[name] = previous.progress.read_tsv(body) if pin["path"].endswith(".tsv") else json.loads(body)
    prior = data["prior_index"]
    require(prior["scope"] == previous.SCOPE, "unexpected predecessor")
    require(
        all(plan["inputs"].get(k) == v for k, v in prior["inputs"].items()),
        "inherited evidence pointer rebound",
    )
    require(
        set(plan["inputs"]) - set(prior["inputs"])
        == {k for name in ["prior_index", *QUALIFIED, *CONTEXT] for k in (name, name + "_verification")},
        "unexpected successor inputs",
    )
    for name in ["prior_index", *QUALIFIED, *CONTEXT]:
        require(
            previous.contains_pin(data[name + "_verification"], plan["inputs"][name]),
            "dossier not bound by verification receipt",
        )
    return plan, data


def bind_dossier(prior, dossier):
    terms = set(dossier["terms"])
    require(terms and terms <= set(prior["terms"]), "dossier terms outside corpus")
    expected_claims = [c for c in prior["claims"] if c["aro_id"] in terms]
    expected_records = [r for r in prior["records"] if terms.intersection(r["card_terms"])]
    require(dossier["claims"] == expected_claims, "dossier claim binding drift")
    require(dossier["records"] == expected_records, "dossier record binding drift")
    for term, row in dossier["terms"].items():
        require(
            row["record_memberships"] == prior["terms"][term]["record_memberships"]
            and row["whole_record_primary_review"] == "OPEN"
            and "experimental_allele_assignment" in row
            and all(v is None for k, v in row.items() if k.startswith("experimental_")),
            "dossier membership or experimental scope changed",
        )


def sal_identity(row):
    require(len(row["reference_candidates"]) == 1, "ambiguous Sal reference")
    candidate = row["reference_candidates"][0]
    source = row["source_identity"]
    species = row["species_name_context"]
    node = species["native_node"]
    _, ancestor = taxonomy.lineage(node)
    require(
        source["aro_id"] == "ARO:3007028"
        and source["protein_namespace"] == "RefSeq"
        and source["protein_version_reported"] is True
        and source["source_protein"] == "WP_082039181.1"
        and any(
            r["database"] == "RefSeq" and r["id"] == source["source_protein"]
            for r in candidate["source_refseq_cross_references"]
        )
        and candidate["scope"] == "EXACT_SOURCE_REPORTED_REFSEQ_DATABASE_CROSSWALK_NOT_EXPERIMENTAL_ALLELE"
        and candidate["experimental_strain_assignment"] is None
        and candidate["organism"] == {k: node[k] for k in ("taxonId", "scientificName")}
        and ancestor == taxonomy.identity(node)
        and species["taxon_id"] == "NCBITaxon:" + str(node["taxonId"])
        and species["rank"] == node["rank"] == "species",
        "Sal crosswalk or species scope changed",
    )
    identity = previous.registry.reference_identity(
        {
            "entry_type": candidate["entry_type"],
            "entry_version": candidate["versions"]["entryVersion"],
            "sequence_version": candidate["versions"]["sequenceVersion"],
            "reference_taxon_id": species["taxon_id"],
            "reference_taxon_rank": node["rank"],
            "reference_species_taxon_id": species["taxon_id"],
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
    )
    return candidate, identity


def gene_identity(candidate, dossier):
    node = dossier["native_taxonomy"][candidate["reference_taxon_id"].split(":")[1]]
    species = dossier["native_taxonomy"][candidate["reference_species_taxon_id"].split(":")[1]]
    _, ancestor = taxonomy.lineage(node)
    taxonomy.lineage(species)
    require(
        ancestor == taxonomy.identity(species)
        and species["rank"] == "species"
        and candidate["reference_taxon_id"] == "NCBITaxon:" + str(node["taxonId"])
        and candidate["reference_taxon_rank"] == node["rank"]
        and candidate["reference_species_taxon_id"] == "NCBITaxon:" + str(species["taxonId"])
        and candidate["reference_species_name"] == species["scientificName"]
        and type(candidate["reviewed"]) is bool
        and candidate["native_gene_matches"]
        and all(m["value"] == candidate["gene_or_locus"] for m in candidate["native_gene_matches"])
        and all(
            candidate[k] is None
            for k in (
                "experimental_allele_assignment",
                "experimental_protein_assignment",
                "experimental_strain_taxon_assignment",
            )
        )
        and candidate["resistance_phenotype_from_protein_annotation"] is False,
        "gene reference identity or experimental scope changed",
    )
    return previous.registry.reference_identity(
        {
            **candidate,
            "entry_type": "UniProtKB reviewed (Swiss-Prot)"
            if candidate["reviewed"]
            else "UniProtKB unreviewed (TrEMBL)",
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
    )


def selections(name, dossier):
    selected, comparisons = {}, {}
    for term, row in dossier["terms"].items():
        candidates = []
        if name == "sal-reference-context":
            if row["reference_candidates"]:
                candidate, identity = sal_identity(row)
                candidates.append(
                    (
                        candidate["accession"],
                        identity,
                        candidate["scope"],
                        pointer(name, "terms", term, "reference_candidates", 0),
                    )
                )
        elif name == "dnaa-sigma-hp1184":
            expected = {
                "ARO:3000248": {"UniProtKB:P03004": "dnaA"},
                "ARO:3000261": {"UniProtKB:P00579": "rpoD", "UniProtKB:P0AGB3": "rpoH"},
                "ARO:3003965": {"UniProtKB:O25796": "HP_1184"},
            }
            require(
                term in expected
                and len(row["references"]) == len(expected[term])
                and {c["accession"]: c["gene_or_locus"] for c in row["references"]} == expected[term],
                "reference component missing, duplicated or substituted",
            )
            eligible, comparators = [], []
            for i, candidate in enumerate(row["references"]):
                identity = gene_identity(candidate, dossier)
                accession, role = candidate["accession"], candidate["role"]
                evidence = pointer(name, "terms", term, "references", i)
                if candidate["eligible_as_determinant_reference_context"] is True:
                    require(
                        role == "NAMED_GENE_OR_LOCUS_REFERENCE_NOT_EXPERIMENTAL_ALLELE",
                        "comparator promoted to determinant",
                    )
                    eligible.append(accession)
                    candidates.append((accession, identity, role, evidence))
                else:
                    require(
                        candidate["eligible_as_determinant_reference_context"] is False
                        and term == "ARO:3000261"
                        and accession == "UniProtKB:P00579"
                        and role == "SIGMA70_COMPARATOR_NOT_RESISTANCE_DETERMINANT",
                        "unreviewed comparator scope",
                    )
                    comparators.append(accession)
                    comparisons.setdefault(term, []).append(
                        {
                            "protein_accession": accession,
                            "evidence": evidence,
                            "included_in_determinant_reference_counts": False,
                        }
                    )
            require(
                row["reference_accessions"] == eligible and row["comparator_accessions"] == comparators,
                "gene reference or comparator selection drift",
            )
        else:
            require(
                not row.get("reference_candidates") and not row.get("reference_accessions"),
                "context-only dossier has unreviewed references",
            )
        if candidates:
            require(
                len(candidates) == 1 and candidates[0][0] == SELECTED.get(term),
                "unexpected selected reference",
            )
            selected[term] = candidates[0]
    return selected, comparisons


def reconcile(prior, dossiers):
    result = copy.deepcopy(prior)
    terms, proteins = result["terms"], result["proteins"]
    result["successor_followups"] = {}
    result["comparison_contexts"] = {}
    added = set()
    for name, dossier in dossiers.items():
        bind_dossier(prior, dossier)
        selected, comparisons = selections(name, dossier)
        require(not set(comparisons).intersection(result["comparison_contexts"]), "duplicate comparator")
        result["comparison_contexts"].update(comparisons)
        result["successor_followups"][name] = {
            "source": {"input": name, "pointer": ""},
            "aro_ids": sorted(dossier["terms"]),
            "selected_reference_terms": sorted(selected),
            "experimental_identity_assigned": False,
        }
        if not selected:
            result["context_only_followups"][name] = {
                "source": {"input": name, "pointer": ""},
                "aro_ids": sorted(dossier["terms"]),
                "promotes_component_or_lead_to_whole_determinant": False,
            }
        for term in dossier["terms"]:
            row = terms[term]
            row["followups"].append(pointer(name, "terms", term))
            if term not in selected:
                continue
            require(not row["reference_links"] and term not in added, "reference term already linked")
            accession, identity, kind, evidence = selected[term]
            previous.add_reference(proteins, accession, identity, evidence)
            row["reference_links"].append(
                {
                    "protein_accession": accession,
                    "kind": kind,
                    "evidence": evidence,
                    "experimental_subject_assignment": False,
                    "exact_allele_assignment": False,
                }
            )
            row["reference_accessions"] = [accession]
            row["reference_status"] = "REFERENCE_CONTEXT_NOT_EXPERIMENTAL_GROUNDING"
            added.add(term)
    require(added == set(SELECTED), "incomplete successor reference selections")
    result["proteins"] = dict(sorted(proteins.items()))
    result["unresolved_reference_worklist"] = [
        {**row, "followups": terms[row["aro_id"]]["followups"]}
        for row in prior["unresolved_reference_worklist"]
        if row["aro_id"] not in added
    ]
    return result


def rebind_current(root, prior, terms):
    census = [
        {
            **row,
            "resistance_assertions": sum(
                row[k]
                for k in ("card_assertions", "phi_claims_not_reassessed", "curator_claims_not_reassessed")
            ),
            "score_rules": row["score_rules_not_reassessed"],
            "activity_observations": row["activity_observations_not_reassessed"],
        }
        for row in prior["records"]
    ]
    records, _ = previous.progress.current_records(root, census)
    rows, claims = previous.bind_records(records, prior, terms, [])
    # bind_records treats its input as the oldest checkpoint; retain the real history.
    for claim, old in zip(claims, prior["claims"], strict=True):
        claim["historical_claim_sha256"] = old["historical_claim_sha256"]
        require(
            {**claim, "reference_status": old["reference_status"]} == old,
            "non-reference claim fields changed",
        )
    for row, old in zip(rows, prior["records"], strict=True):
        require(
            {**row, **{k: old[k] for k in ("reference_accessions", "unresolved_card_terms")}} == old,
            "non-reference record fields changed",
        )
    return rows, claims


def build(root):
    plan, data = read_inputs(root)
    prior = data["prior_index"]
    dossiers = {name: data[name] for name in [*QUALIFIED, *CONTEXT]}
    result = reconcile(prior, dossiers)
    rows, claims = rebind_current(root, prior, result["terms"])
    result.update(
        {
            "date": plan["date"],
            "scope": SCOPE,
            "plan": reference.pin(root, root / PLAN),
            "inputs": plan["inputs"],
            "predecessor_index": {"input": "prior_index", "pointer": ""},
            "records": rows,
            "claims": claims,
            "constraints": plan["constraints"],
        }
    )
    terms, proteins = result["terms"], result["proteins"]
    result["summary"] = {
        **prior["summary"],
        "complete_collection_aware_records_read": len(rows),
        "card_claims": len(claims),
        "card_terms": len(terms),
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
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    outputs = [args.root / (PREFIX + suffix) for suffix in (".json", ".tsv")]
    if args.write:
        require(not any(p.exists() for p in outputs), "output already exists")
    result = build(args.root)
    if args.write:
        for path, body in zip(
            outputs,
            (json.dumps(result, indent=2, sort_keys=True) + "\n", previous.render_rows(result["records"])),
            strict=True,
        ):
            with path.open("x") as stream:
                stream.write(body)
    print(json.dumps(result["summary"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
