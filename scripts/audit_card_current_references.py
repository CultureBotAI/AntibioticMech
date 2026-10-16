"""Reconcile verified reference dossiers against every current corpus record."""

import argparse
import copy
import csv
import io
import json
from collections import Counter, defaultdict
from pathlib import Path

import audit_card_reference_memberships as registry
import summarize_resistance_progress as progress
from audit_curator_resistance_fields import owner

reference = registry.reference
PREFIX = "research/2026-10-15-card-current-references"
PLAN = Path(PREFIX + "-plan.json")
SCOPE = "CURRENT_CORPUS_REFERENCE_RECONCILIATION_NOT_EXPERIMENTAL_GROUNDING"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def pointer(name, *parts):
    return {
        "input": name,
        "pointer": "/" + "/".join(str(p).replace("~", "~0").replace("/", "~1") for p in parts),
    }


def contains_pin(value, pin):
    if isinstance(value, dict):
        return value == pin or any(contains_pin(v, pin) for v in value.values())
    return isinstance(value, list) and any(contains_pin(v, pin) for v in value)


def read_inputs(root):
    plan = json.loads((root / PLAN).read_bytes())
    data = {}
    for key, pin in plan["inputs"].items():
        raw = reference.check_pin(root, pin).read_bytes()
        data[key] = progress.read_tsv(raw) if pin["path"].endswith(".tsv") else json.loads(raw)
    require(plan["scope"] == SCOPE, "unexpected reconciliation scope")
    require(
        plan["constraints"]
        == {
            "network_requests": 0,
            "ncbi_requests": 0,
            "biological_record_writes": False,
            "experimental_identifiers_assigned": False,
            "new_primary_reviews": 0,
            "issue_1040": "DEFERRED",
            "full_investigation_complete": False,
        },
        "reconciliation cannot promote research scope",
    )
    names = plan["qualified_dossiers"] + plan["context_only_dossiers"]
    require(len(set(names)) == len(names), "duplicate dossier scope")
    for name in ["base", *names]:
        require(
            contains_pin(data[name + "_verification"], plan["inputs"][name]), "dossier not bound by receipt"
        )
    require(
        plan["inputs"]["active_reviews"]["sha256"] == data["cdsa_transition"]["review_file"]["after_sha256"],
        "active qualification checkpoint changed",
    )
    return plan, data


def current_census(census, transitions):
    rows = copy.deepcopy(census)
    by_path = progress.index_unique(rows, "path", "census path")
    for transition in transitions:
        paths = set()
        for delta in transition["record_deltas"]:
            path = delta["path"]
            require(path not in paths and path in by_path, "duplicate or unknown transition path")
            paths.add(path)
            row = by_path[path]
            require(
                row["record_sha256"] == delta["before_sha256"] and row["identifier"] == delta["identifier"],
                "discontinuous corpus transition",
            )
            require(all(c["changed_fields"] == ["note"] for c in delta["claims"]), "non-note transition")
            row["record_sha256"] = delta["after_sha256"]
    return rows


def original_claim(claim, identifier, index, transitions):
    result = copy.deepcopy(claim)
    for transition in reversed(transitions):
        for delta in transition["record_deltas"]:
            if delta["identifier"] != identifier:
                continue
            for change in delta["claims"]:
                if change["index"] != index:
                    continue
                require(change["aro_id"] == result.get("aro_id"), "qualification claim identity changed")
                if "after_note" in change:
                    require(result.get("note") == change["after_note"], "qualification note drift")
                require("note" in result, "qualified claim lost its note")
                if change.get("before_note") is None:
                    result.pop("note")
                else:
                    result["note"] = change["before_note"]
    return result


def view_identity(view):
    taxon = view["reference_taxonomy"]
    species = taxon.get("species")
    native = view["native_protein_taxonomy"]
    require(
        taxon.get("active") is True
        and species
        and species["rank"] == "species"
        and taxon["taxon_id"] == "NCBITaxon:" + str(native["taxonId"])
        and taxon["scientific_name"] == native["scientificName"]
        and taxon["lineage"][-1]["taxonId"] == native["taxonId"]
        and taxon["lineage_species_is_experimental_subject"] is False,
        "reference taxonomy not verified at its native rank",
    )
    return registry.reference_identity(
        {
            "entry_type": view["entry_type"],
            "entry_version": view["entry_audit"]["entryVersion"],
            "sequence_version": view["entry_audit"]["sequenceVersion"],
            "reference_taxon_id": taxon["taxon_id"],
            "reference_taxon_rank": taxon["native_rank"],
            "reference_species_taxon_id": "NCBITaxon:" + str(species["taxonId"]),
            "experimental_subject_assignment": view["experimental_subject_assignment"],
            "exact_allele_assignment": view["exact_allele_assignment"],
        }
    )


def selected_view(dossier, accession):
    matches = [
        (v, ("reference_views", key))
        for key, v in dossier.get("reference_views", {}).items()
        if v.get("accession") == accession
    ]
    if dossier.get("reference_view", {}).get("accession") == accession:
        matches.append((dossier["reference_view"], ("reference_view",)))
    require(len(matches) == 1, "qualified reference view missing or ambiguous")
    return matches[0]


def selected_candidate(dossier, term, accession):
    found = []
    for field in ("literal_gene_candidates", "reference_candidates", "name_matched_candidates"):
        found.extend(
            (c, ("terms", term, field, i))
            for i, c in enumerate(dossier["terms"][term].get(field, []))
            if c.get("protein_accession") == accession and c.get("qualified_reference") is True
        )
    for field in ("reference_candidate", "reference_link"):
        candidate = dossier["terms"][term].get(field, {})
        if (
            candidate
            and candidate.get("protein_accession") == accession
            and candidate.get("qualified_reference") is True
        ):
            found.append((candidate, ("terms", term, field)))
    if dossier["scope"] == "M35_PAPER_NAME_SPECIES_REFERENCE_CONTEXT_OMP1_UNRESOLVED":
        require(term == "ARO:3004124", "porin candidate moved to another term")
        for key, candidate in dossier["reference_candidates"].items():
            if candidate["protein_accession"] == accession and candidate["qualified_reference"] is True:
                found.append((candidate, ("reference_candidates", key)))
    require(len(found) == 1, "qualified term candidate missing or ambiguous")
    candidate, path = found[0]
    require(
        candidate.get("exact_allele_assignment", candidate.get("experimental_allele_assigned")) is False
        and candidate.get(
            "experimental_subject_assignment", dossier["terms"][term].get("experimental_subject_assigned")
        )
        is False
        and candidate.get("primary_resistance_validation", False) is False,
        "reference candidate promoted to experimental identity",
    )
    return candidate, path


def add_reference(proteins, accession, identity, source):
    require(accession.startswith("UniProtKB:"), "non-UniProt reference")
    if accession in proteins:
        require(proteins[accession]["identity"] == identity, "conflicting reference identity or version")
    else:
        proteins[accession] = {
            "identity": identity,
            "sources": [],
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
    if source not in proteins[accession]["sources"]:
        proteins[accession]["sources"].append(source)


def reconcile_terms(base, dossiers):
    terms, proteins = {}, {}
    for accession, row in base["proteins"].items():
        identity = registry.reference_identity(
            {**row["identity"], "experimental_subject_assignment": False, "exact_allele_assignment": False}
        )
        require(
            row["experimental_subject_assignment"] is row["exact_allele_assignment"] is False,
            "base reference scope changed",
        )
        add_reference(proteins, accession, identity, pointer("base", "proteins", accession))
    for term, row in base["terms"].items():
        terms[term] = {
            "source_label_sha256": row["source_label_sha256"],
            "record_memberships": row["record_memberships"],
            "base_assessment": pointer("base", "terms", term),
            "reference_links": [
                {
                    "protein_accession": link["protein_accession"],
                    "kind": link["kind"],
                    "evidence": pointer("base", "terms", term, "links", i),
                }
                for i, link in enumerate(row["links"])
            ],
            "followups": [],
            "experimental_subject_assignment": False,
            "whole_record_primary_review": "OPEN",
        }
    for name, dossier in dossiers.items():
        for term, row in dossier["terms"].items():
            require(term in terms, "follow-up outside base term scope")
            old = terms[term]
            require(
                progress.digest(row["source_label"].encode()) == old["source_label_sha256"]
                and row["record_memberships"] == old["record_memberships"],
                "follow-up source binding drift",
            )
            old["followups"].append(pointer(name, "terms", term))
            accessions = row.get("qualified_reference_accessions", [])
            require(len(accessions) == len(set(accessions)), "duplicate qualified reference")
            if accessions:
                require(not old["reference_links"], "unexpected overlap with an already linked term")
            for accession in accessions:
                candidate, candidate_path = selected_candidate(dossier, term, accession)
                view, view_path = selected_view(dossier, accession)
                identity = view_identity(view)
                add_reference(proteins, accession, identity, pointer(name, *view_path))
                old["reference_links"].append(
                    {
                        "protein_accession": accession,
                        "kind": candidate["disposition"],
                        "evidence": pointer(name, *candidate_path),
                        "reference_view": pointer(name, *view_path),
                        "experimental_subject_assignment": False,
                        "exact_allele_assignment": False,
                    }
                )
    for row in terms.values():
        row["reference_accessions"] = sorted({link["protein_accession"] for link in row["reference_links"]})
        row["reference_status"] = (
            "REFERENCE_CONTEXT_NOT_EXPERIMENTAL_GROUNDING"
            if row["reference_links"]
            else "UNRESOLVED_REFERENCE_IDENTITY_NOT_BIOLOGICAL_ABSENCE"
        )
    return terms, dict(sorted(proteins.items()))


def bind_records(records, base, terms, transitions):
    original = {(c["record_identifier"], c["resistance_index"]): c for c in base["claims"]}
    require(len(original) == len(base["claims"]), "duplicate base claim")
    rows, claims, memberships = [], [], defaultdict(set)
    seen = set()
    for identifier, record in sorted(records.items()):
        counts, local_terms, linked, unresolved = Counter(), set(), set(), set()
        for index, claim in enumerate(record["resistance_mechanisms"]):
            source = owner(claim)
            counts[source] += 1
            if source != "CARD":
                continue
            key = identifier, index
            require(key in original, "new or moved CARD claim")
            previous = original[key]
            term = claim["aro_id"]
            require(
                previous["aro_id"] == term
                and registry.checksum(original_claim(claim, identifier, index, transitions))
                == previous["claim_sha256"],
                "unreviewed source claim drift",
            )
            require(
                progress.digest(claim["label"].encode()) == terms[term]["source_label_sha256"],
                "source label drift",
            )
            seen.add(key)
            local_terms.add(term)
            memberships[term].add(identifier)
            linked.update(terms[term]["reference_accessions"])
            if not terms[term]["reference_accessions"]:
                unresolved.add(term)
            claims.append(
                {
                    "record_identifier": identifier,
                    "record_path": record["path"],
                    "record_sha256": record["sha256"],
                    "standard_inchi_key": record["standard_inchi_key"],
                    "resistance_index": index,
                    "aro_id": term,
                    "claim_sha256": registry.checksum(claim),
                    "historical_claim_sha256": previous["claim_sha256"],
                    "reference_status": terms[term]["reference_status"],
                    "experimental_subject_assignment": False,
                }
            )
        rows.append(
            {
                "identifier": identifier,
                "label": record["label"],
                "path": record["path"],
                "record_sha256": record["sha256"],
                "standard_inchi_key": record["standard_inchi_key"],
                "card_assertions": counts["CARD"],
                "card_terms": sorted(local_terms),
                "unresolved_card_terms": sorted(unresolved),
                "reference_accessions": sorted(linked),
                "reference_taxonomy_is_experimental_subject": False,
                "phi_claims_not_reassessed": counts["PHIBASE"],
                "curator_claims_not_reassessed": counts["CURATOR"],
                "score_rules_not_reassessed": len(record["score_rules"]),
                "activity_observations_not_reassessed": record["activity_count"],
                "whole_record_primary_review": "OPEN",
                "no_card_assertions_is_review_complete": False,
            }
        )
    require(seen == set(original) and set(memberships) == set(terms), "CARD membership coverage changed")
    require(
        all(sorted(memberships[t]) == r["record_memberships"] for t, r in terms.items()),
        "term membership drift",
    )
    return rows, claims


def build(root):
    plan, data = read_inputs(root)
    transitions = [data["first_transition"], data["cdsa_transition"]]
    census = current_census(data["census"], transitions)
    base = data["base"]
    terms, proteins = reconcile_terms(base, {name: data[name] for name in plan["qualified_dossiers"]})
    records, _ = progress.current_records(root, census)
    rows, claims = bind_records(records, base, terms, transitions)
    require(
        len(rows) == 2939 and len(terms) == 2002 and len(claims) == 4538, "full corpus accounting changed"
    )
    contexts = {}
    for name in plan["context_only_dossiers"]:
        dossier = data[name]
        selected = sorted(
            {c["aro_id"] for c in dossier.get("claims", [])}
            | set(dossier.get("terms", {}))
            | set(dossier.get("parents", {}))
        )
        require(set(selected) <= set(terms), "context outside current CARD scope")
        contexts[name] = {
            "source": {"input": name, "pointer": ""},
            "aro_ids": selected,
            "promotes_component_or_lead_to_whole_determinant": False,
        }
        for term in selected:
            terms[term]["followups"].append({"input": name, "pointer": ""})
    added_terms = sorted(t for t in terms if terms[t]["reference_links"] and not base["terms"][t]["links"])
    added_memberships = sum(len(terms[t]["record_memberships"]) for t in added_terms)
    unresolved = [
        {
            "aro_id": t,
            "record_memberships": row["record_memberships"],
            "membership_count": len(row["record_memberships"]),
            "source_scope": base["terms"][t]["ontology_scope_hint"],
            "followups": row["followups"],
            "status": row["reference_status"],
            "clinical_risk_ranking": False,
        }
        for t, row in terms.items()
        if not row["reference_links"]
    ]
    unresolved.sort(key=lambda r: (-r["membership_count"], r["aro_id"]))
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "inputs": plan["inputs"],
        "records": rows,
        "claims": claims,
        "terms": terms,
        "proteins": proteins,
        "context_only_followups": contexts,
        "active_source_qualifications": {"input": "active_reviews", "pointer": ""},
        "unresolved_reference_worklist": unresolved,
        "summary": {
            "complete_collection_aware_records_read": len(rows),
            "card_terms": len(terms),
            "card_claims": len(claims),
            "selected_reference_terms": sum(bool(t["reference_links"]) for t in terms.values()),
            "unresolved_reference_terms": len(unresolved),
            "selected_reference_proteins": len(proteins),
            "reference_links": sum(len(t["reference_links"]) for t in terms.values()),
            "added_reference_terms": len(added_terms),
            "added_reference_links": sum(len(terms[t]["reference_links"]) for t in added_terms),
            "added_reference_proteins": len(set(proteins) - set(base["proteins"])),
            "added_claim_memberships_with_references": added_memberships,
            "records_with_reference_context": sum(bool(r["reference_accessions"]) for r in rows),
            "records_without_card_assertions": sum(r["card_assertions"] == 0 for r in rows),
            "phi_claims_not_reassessed": sum(r["phi_claims_not_reassessed"] for r in rows),
            "curator_claims_not_reassessed": sum(r["curator_claims_not_reassessed"] for r in rows),
            "score_rules_not_reassessed": sum(r["score_rules_not_reassessed"] for r in rows),
            "qualified_followup_dossiers": len(plan["qualified_dossiers"]),
            "context_only_dossiers": len(contexts),
            "current_source_qualified_claims": sum(
                c["claim_sha256"] != c["historical_claim_sha256"] for c in claims
            ),
            "whole_record_primary_signoffs": 0,
        },
        "constraints": plan["constraints"],
        "attribution": "Inherited CARD/ARO and UniProt reference metadata, CC BY 4.0; "
        "original evidence scopes and citations retained by pinned pointers.",
    }


def render_rows(rows):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=sorted(rows[0]), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({k: "|".join(v) if isinstance(v, list) else v for k, v in row.items()})
    return output.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.write:
        require(
            not any(Path(PREFIX + suffix).exists() for suffix in (".json", ".tsv")), "output already exists"
        )
    result = build(Path.cwd())
    if args.write:
        for suffix, text in (
            (".json", json.dumps(result, indent=2, sort_keys=True) + "\n"),
            (".tsv", render_rows(result["records"])),
        ):
            with Path(PREFIX + suffix).open("x") as stream:
                stream.write(text)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
