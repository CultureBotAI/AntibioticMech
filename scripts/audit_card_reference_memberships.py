"""Bind two reference cohorts to every live CARD assertion, without assigning alleles."""

import argparse
import csv
import io
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import audit_topoisomerase_references as reference
import summarize_resistance_progress as progress
from audit_curator_resistance_fields import owner

PREFIX = "research/2026-10-14-card-reference-memberships"
PLAN = Path(PREFIX + "-plan.json")
SCOPE = "LIVE_CARD_MEMBERSHIPS_OF_TWO_REFERENCE_COHORTS_NOT_EXPERIMENTAL_GROUNDING"
DIRECT = "EXPLICIT_CARD_XREF_REFERENCE_ONLY"
CITATION = "CITATION_AND_LITERAL_GENE_CANDIDATE_ONLY"
UNSELECTED = "NO_CANDIDATE_IN_THE_TWO_SELECTED_COHORTS"


def checksum(value):
    return progress.digest(json.dumps(value, sort_keys=True, ensure_ascii=True).encode())


def reference_identity(row, literature=False):
    if (
        row.get("experimental_subject_assignment") is not False
        or row.get("exact_allele_assignment") is not False
    ):
        raise ValueError("reference promoted to experimental identity")
    species = row.get("reference_species_lineage") if literature else None
    if literature and (
        row.get("taxonomy_identity_verified") is not True
        or not species
        or species.get("rank") != "species"
        or species.get("experimental_subject_assignment") is not False
    ):
        raise ValueError("literature reference taxonomy scope changed")
    result = {
        key: row[key] for key in ("entry_type", "entry_version", "sequence_version", "reference_taxon_id")
    }
    result["reference_taxon_rank"] = row["taxonomy_rank" if literature else "reference_taxon_rank"]
    result["reference_species_taxon_id"] = (
        species["taxon_id"] if literature else row["reference_species_taxon_id"]
    )
    if (
        any(type(result[k]) is not int or result[k] <= 0 for k in ("entry_version", "sequence_version"))
        or result["entry_type"] not in {"UniProtKB reviewed (Swiss-Prot)", "UniProtKB unreviewed (TrEMBL)"}
        or not result["reference_taxon_rank"]
        or any(
            not re.fullmatch(r"NCBITaxon:[1-9][0-9]*", result[k])
            for k in ("reference_taxon_id", "reference_species_taxon_id")
        )
    ):
        raise ValueError("invalid reference version, type or taxonomy")
    return result


def reconcile_proteins(direct, literature):
    proteins = {}
    for name, cohort in (("direct", direct), ("literature", literature)):
        for accession, row in sorted(cohort["proteins"].items()):
            identity = reference_identity(row, literature=name == "literature")
            if not accession.startswith("UniProtKB:") or (
                name == "literature" and row["accession"] != accession
            ):
                raise ValueError("reference accession key mismatch")
            if accession in proteins and proteins[accession]["identity"] != identity:
                raise ValueError("cross-cohort reference identity conflict")
            item = proteins.setdefault(
                accession,
                {
                    "identity": identity,
                    "sources": [],
                    "experimental_subject_assignment": False,
                    "exact_allele_assignment": False,
                },
            )
            item["sources"].append({"input": name, "pointer": f"/proteins/{accession}"})
    return dict(sorted(proteins.items()))


def citation_link(candidate, term, protein):
    for key in (
        "explicit_card_xref",
        "experimental_subject_assignment",
        "exact_allele_assignment",
        "primary_review_completed_by_this_audit",
    ):
        if candidate.get(key) is not False:
            raise ValueError("citation candidate evidence scope changed")
    # The earlier cohort predates this redundant flag; the two required flags above do not.
    if (
        "experimental_identity_assigned" in candidate
        and candidate["experimental_identity_assigned"] is not False
    ):
        raise ValueError("citation candidate identity scope changed")
    citations = candidate["source_citation_ids"]
    contexts = candidate["matched_study_contexts"]
    available = {c["reference_number"]: c for c in protein["reference_contexts"]}
    if len(available) != len(protein["reference_contexts"]):
        raise ValueError("duplicate reference context number")
    if (
        not citations
        or len(set(citations)) != len(citations)
        or not set(citations) <= set(term["definition_citation_ids"])
        or not candidate["literal_gene_matches"]
        or not contexts
        or len({c["reference_number"] for c in contexts}) != len(contexts)
    ):
        raise ValueError("missing, duplicate or unbound candidate citation")
    for match in candidate["literal_gene_matches"]:
        if (
            match["field"] not in {"geneName", "synonyms"}
            or match["value"] not in protein["gene_names_and_synonyms"]
            or match["value"].casefold() != term["source_label"].casefold()
        ):
            raise ValueError("literal gene match differs from term or protein")
    matched = set()
    for context in contexts:
        if (
            available.get(context["reference_number"]) != context
            or context.get("experimental_subject_assignment") is not False
            or context.get("primary_review_completed_by_this_audit") is not False
            or not set(context["citation_identifiers"]) & set(citations)
        ):
            raise ValueError("candidate context differs from protein bibliography")
        matched.update(set(context["citation_identifiers"]) & set(citations))
    if matched != set(citations):
        raise ValueError("candidate citation has no matching context")
    return {
        "protein_accession": candidate["protein_accession"],
        "kind": CITATION,
        "source_citation_ids": citations,
        "matched_reference_numbers": [c["reference_number"] for c in contexts],
    }


def reconcile_terms(base, direct, literature, scopes, named_taxa):
    expected_direct = {tid for tid, row in base["determinants"].items() if row["candidates"]}
    if (
        set(direct["terms"]) != expected_direct
        or set(scopes["terms"]) != set(base["determinants"])
        or not set(literature["terms"]) <= set(base["determinants"])
        or set(direct["terms"]) & set(literature["terms"])
    ):
        raise ValueError("selected term cohorts or direct/citation partition changed")
    rna_terms = {
        tid for tid, row in scopes["terms"].items() if row["entity_scope"] == "RNA_TERM_NOT_A_PROTEIN_PRODUCT"
    }
    if set(named_taxa["terms"]) != rna_terms:
        raise ValueError("RNA ancestry review coverage changed")
    terms = {}
    for tid, source in sorted(base["determinants"].items()):
        if len(source["labels"]) != 1:
            raise ValueError("ambiguous source term label")
        label_hash = progress.digest(source["labels"][0].encode())
        links, membership = [], None
        if tid in direct["terms"]:
            term = direct["terms"][tid]
            if (
                term["source_label_sha256"] != label_hash
                or term["experimental_subject_assignment"] is not False
                or term["reference_accessions"] != [c["accession"] for c in source["candidates"]]
            ):
                raise ValueError("direct term identity or candidate coverage changed")
            membership = term["record_memberships"]
            for index, candidate in enumerate(source["candidates"]):
                accession = candidate["accession"]
                protein = reference_identity(direct["proteins"][accession])
                if (
                    candidate["card_cross_reference"]["database"] != "CARD"
                    or candidate["card_cross_reference"]["id"] != tid
                    or candidate["evidence_scope"]
                    != "EXPLICIT_REFERENCE_LINK_NOT_EXPERIMENTAL_ALLELE_GROUNDING"
                    or candidate["entry_audit"]
                    != {
                        "entryVersion": protein["entry_version"],
                        "sequenceVersion": protein["sequence_version"],
                    }
                    or candidate["reference_taxon_id"] != protein["reference_taxon_id"]
                    or candidate["taxonomy_rank"] != protein["reference_taxon_rank"]
                    or candidate["entry_type"] != protein["entry_type"]
                ):
                    raise ValueError("direct protein cross-reference or identity changed")
                links.append(
                    {
                        "protein_accession": accession,
                        "kind": DIRECT,
                        "source_citation_ids": [],
                        "matched_reference_numbers": [],
                        "source": {
                            "input": "direct_candidates",
                            "pointer": f"/determinants/{tid}/candidates/{index}",
                        },
                    }
                )
        elif tid in literature["terms"]:
            term = literature["terms"][tid]
            if term["source_label"] != source["labels"][0] or term["whole_record_primary_review"] != "OPEN":
                raise ValueError("citation term label or review status changed")
            membership = term["record_memberships"]
            for index, candidate in enumerate(term["reference_candidates"]):
                accession = candidate["protein_accession"]
                link = citation_link(candidate, term, literature["proteins"][accession])
                link["source"] = {
                    "input": "literature",
                    "pointer": f"/terms/{tid}/reference_candidates/{index}",
                }
                links.append(link)
            if not links:
                raise ValueError("empty selected citation cohort")
        if len({link["protein_accession"] for link in links}) != len(links):
            raise ValueError("duplicate term candidate")
        if membership is not None and (not membership or len(set(membership)) != len(membership)):
            raise ValueError("empty or duplicate source record membership")
        named = named_taxa["terms"].get(tid)
        if named and named["source_label_sha256"] != label_hash:
            raise ValueError("named-organism term identity changed")
        terms[tid] = {
            "source_label_sha256": label_hash,
            "links": links,
            "reference_status": links[0]["kind"] if links else UNSELECTED,
            "record_memberships": sorted(membership) if membership is not None else None,
            "ontology_scope_hint": scopes["terms"][tid]["entity_scope"],
            "ontology_scope_source": {"input": "term_scope", "pointer": f"/terms/{tid}"},
            "entity_review": named["entity_review"] if named else "NOT_REASSESSED_BY_THIS_RECONCILIATION",
            "entity_review_source": {"input": "named_taxa", "pointer": f"/terms/{tid}"} if named else None,
            "named_organism_taxon_reference_only": named["named_organism_taxon_id"] if named else None,
            "experimental_subject_assignment": False,
            "whole_record_primary_review": "OPEN",
        }
    selected = {link["protein_accession"] for term in terms.values() for link in term["links"]}
    if selected != set(direct["proteins"]) | set(literature["proteins"]):
        raise ValueError("unlinked or missing cohort protein")
    return terms


def bind_claims(records, terms):
    memberships, claims, rows = defaultdict(set), [], []
    for identifier, record in sorted(records.items()):
        counts, linked = Counter(), set()
        for index, claim in enumerate(record["resistance_mechanisms"]):
            source = owner(claim)
            counts[source] += 1
            if source != "CARD":
                continue
            tid = claim["aro_id"]
            if (
                tid not in terms
                or progress.digest(claim["label"].encode()) != terms[tid]["source_label_sha256"]
            ):
                raise ValueError("live source term identity changed")
            term = terms[tid]
            memberships[tid].add(identifier)
            counts[term["reference_status"]] += 1
            linked.update(link["protein_accession"] for link in term["links"])
            claims.append(
                {
                    "record_identifier": identifier,
                    "record_path": record["path"],
                    "record_sha256": record["sha256"],
                    "standard_inchi_key": record["standard_inchi_key"],
                    "resistance_index": index,
                    "claim_sha256": checksum(claim),
                    "aro_id": tid,
                    "term_pointer": f"/terms/{tid}",
                    "reference_status": term["reference_status"],
                    "experimental_subject_assignment": False,
                }
            )
        rows.append(
            {
                "identifier": identifier,
                "path": record["path"],
                "record_sha256": record["sha256"],
                "standard_inchi_key": record["standard_inchi_key"],
                "card_assertions": counts["CARD"],
                "direct_xref_claims": counts[DIRECT],
                "citation_candidate_claims": counts[CITATION],
                "unselected_candidate_claims": counts[UNSELECTED],
                "selected_reference_accessions": "|".join(sorted(linked)),
                "phi_claims_not_reassessed": counts["PHIBASE"],
                "curator_claims_not_reassessed": counts["CURATOR"],
                "score_rules_not_reassessed": len(record["score_rules"]),
                "whole_record_primary_review": "OPEN",
            }
        )
    if set(memberships) != set(terms):
        raise ValueError("live CARD term coverage differs from source cohorts")
    for tid, term in terms.items():
        actual = sorted(memberships[tid])
        if term["record_memberships"] is not None and term["record_memberships"] != actual:
            raise ValueError("source-to-live record membership changed")
        term["record_memberships"] = actual
    return claims, rows


def build(root, plan_path=PLAN):
    plan = json.loads((root / plan_path).read_bytes())
    if plan["selection"] != "ALL_CURRENT_RECORDS_ALL_CARD_ASSERTIONS_TWO_PINNED_REFERENCE_COHORTS" or plan[
        "constraints"
    ] != {
        "network_requests": 0,
        "biological_writes": False,
        "experimental_assignments": False,
        "issue_1040": "DEFERRED",
    }:
        raise ValueError("reconciliation scope changed")
    paths = {key: reference.check_pin(root, pin) for key, pin in plan["inputs"].items()}
    data = {key: json.loads(path.read_bytes()) for key, path in paths.items() if path.suffix == ".json"}
    direct, literature, base = [data[k] for k in ("direct", "literature", "direct_candidates")]
    if (
        direct["release"] != base["summary"]["release"]
        or direct["release"] != "2026_03"
        or direct["inputs"]["references"] != plan["inputs"]["direct_candidates"]
        or direct["inputs"]["contexts"] != plan["inputs"]["direct_contexts"]
        or direct["inputs"]["source_inventory"] != plan["inputs"]["source_inventory"]
    ):
        raise ValueError("direct source provenance changed")
    if (
        direct["scope"] != "REFERENCE_TAXONOMY_LINEAGES_NOT_EXPERIMENTAL_ORGANISM_OR_ALLELE_ASSIGNMENTS"
        or literature["scope"]
        != "CITATION_SCOPED_DATABASE_CONTEXT_NOT_EXPERIMENTAL_IDENTITY_OR_PRIMARY_REVIEW"
        or not literature["queries"]
        or {q["release"] for q in literature["queries"].values()} != {direct["release"]}
    ):
        raise ValueError("reference cohort scope or release changed")
    successor = data["species_successor"]
    missing = {key for key, node in direct["species"].items() if not node["standalone_active_verified"]}
    if (
        successor["inputs"]["prior"] != plan["inputs"]["direct"]
        or successor["release"] != direct["release"]
        or set(successor["species"]) != missing
    ):
        raise ValueError("species successor cohort changed")
    for key, node in successor["species"].items():
        if (
            node["taxon_id"] != direct["species"][key]["taxon_id"]
            or node["scientific_name"] != direct["species"][key]["scientific_name"]
            or node["rank"] != "species"
            or node["active"] is not True
            or node["experimental_subject_assignment"] is not False
        ):
            raise ValueError("species successor identity changed")
    proteins = reconcile_proteins(direct, literature)
    for accession, source in direct["proteins"].items():
        context = data["direct_contexts"]["proteins"][accession]
        if context["reference_taxon_id"] != source["reference_taxon_id"] or context["entry_audit"] != {
            "entryVersion": source["entry_version"],
            "sequenceVersion": source["sequence_version"],
        }:
            raise ValueError("direct citation context identity changed")
        species_id = source["reference_species_taxon_id"].split(":")[1]
        taxon = direct["taxa"][source["reference_taxon_id"].split(":")[1]]
        node = direct["species"][species_id]
        if (
            taxon["reference_taxon_id"] != source["reference_taxon_id"]
            or taxon["reference_rank"] != source["reference_taxon_rank"]
            or taxon["species_taxon_id"] != source["reference_species_taxon_id"]
            or taxon["reference_active"] is not True
            or taxon["experimental_subject_assignment"] is not False
            or node["taxon_id"] != source["reference_species_taxon_id"]
            or node["rank"] != "species"
            or node["experimental_subject_assignment"] is not False
        ):
            raise ValueError("direct reference lineage identity changed")
        proteins[accession]["species_label_flags"] = node["label_flags"]
        proteins[accession]["species_evidence"] = {
            "input": "species_successor" if species_id in missing else "direct",
            "pointer": f"/species/{species_id}",
            "scope": "STANDALONE_REFERENCE_SPECIES_ONLY",
        }
        proteins[accession]["citation_context"] = {
            "input": "direct_contexts",
            "pointer": f"/proteins/{accession}",
        }
    terms = reconcile_terms(base, direct, literature, data["term_scope"], data["named_taxa"])
    records, _ = progress.current_records(root, progress.read_tsv(paths["census"].read_bytes()))
    progress.card_progress(records, base, progress.read_tsv(paths["ledger"].read_bytes()))
    claims, rows = bind_claims(records, terms)
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / plan_path),
        "inputs": plan["inputs"],
        "proteins": proteins,
        "terms": terms,
        "claims": claims,
        "summary": {
            "corpus_records": len(rows),
            "card_assertions": len(claims),
            "card_terms": len(terms),
            "selected_reference_terms": sum(bool(t["links"]) for t in terms.values()),
            "selected_reference_proteins": len(proteins),
            "reference_links": sum(len(t["links"]) for t in terms.values()),
            "accessions_shared_between_cohorts": sum(len(p["sources"]) == 2 for p in proteins.values()),
            "term_statuses": dict(sorted(Counter(t["reference_status"] for t in terms.values()).items())),
            "claim_statuses": dict(sorted(Counter(c["reference_status"] for c in claims).items())),
            "records_with_selected_references": sum(bool(r["selected_reference_accessions"]) for r in rows),
            "records_without_card_assertions": sum(not r["card_assertions"] for r in rows),
            "other_source_claims_not_reassessed": sum(
                r["phi_claims_not_reassessed"] + r["curator_claims_not_reassessed"] for r in rows
            ),
            "score_rules_not_reassessed": sum(r["score_rules_not_reassessed"] for r in rows),
            "whole_record_primary_signoffs": 0,
        },
        "limits": {
            "network_requests": 0,
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "biological_record_changes": 0,
            "experimental_allele_or_genome_assignments": 0,
            "full_corpus_goal_status": "OPEN",
            "source_adoptions": 0,
            "github_mutations": 0,
        },
        "interpretation": [
            "These are two dated reference cohorts, not all scientific groundings or primary reviews.",
            "A protein shared across cohorts does not transfer its CARD cross-reference to another term.",
            "No candidate in these cohorts is not protein absence, resistance absence or an unsearched gene.",
            "RNA ancestry, the protein-definition conflict, clusters and complexes need separate review.",
            "Manual follow-ups, named-organism references, curated claims, "
            "PHI-base and HIVDB remain separate.",
            "Species evidence describes database references, not resistant subjects or whole species.",
            "No gene/allele values, sequences, protocols, new AST or strain annotations are exported here.",
        ],
        "attribution": {"direct": direct["attribution"], "literature": literature["attribution"]},
    }, rows


def render(result, rows):
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return (json.dumps(result, indent=2, sort_keys=True) + "\n").encode(), stream.getvalue().encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result, rows = build(Path.cwd())
    for suffix, body in zip((".json", ".tsv"), render(result, rows), strict=True):
        path = Path(PREFIX + suffix)
        if args.check or path.exists():
            if path.read_bytes() != body:
                raise SystemExit("reference membership checkpoint does not reproduce")
        else:
            with path.open("xb") as stream:
                stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
