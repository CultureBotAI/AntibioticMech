"""Keep parent-term literature and child-reference links at their source scope.

Offline only. Named subclasses and shared papers never identify a parent's
experimental protein, allele, organism, or resistance phenotype.
"""

import argparse
import json
from collections import Counter
from pathlib import Path

import audit_card_citation_concordance as concordance
import audit_card_definition_citations as citations
import audit_card_grounding as card
import audit_card_literature_proteins as literature
import audit_card_term_scope as term_scope
import audit_topoisomerase_references as reference

DEFAULT_DIRECTORY = Path("reports/resistance-grounding-2026-10-10-card-parents")
DEFAULT_OUTPUT = Path("research/2026-10-10-card-parents-context.json")
SCOPE = "PARENT_TERM_REFERENCE_CONTEXT_NOT_EXPERIMENTAL_IDENTITY"


def select_terms(source, definitions, ontology, labels, memberships):
    if set(source["terms"]) != set(definitions["terms"]) or set(labels) != set(source["terms"]):
        raise ValueError("source term coverage mismatch")
    selected = {}
    for tid, row in sorted(source["terms"].items()):
        if row["reference_candidate_accessions"] or not row["named_direct_subclass_count"]:
            continue
        definition = definitions["terms"][tid]
        children = sorted(t for t, v in ontology.items() if tid in v["parents"])
        if (
            len(children) != row["named_direct_subclass_count"]
            or ontology[tid]["deprecated"]
            or ontology[tid]["label"] != labels[tid]
            or definition["label_sha256"] != citations.text_hash(labels[tid])
            or definition["record_memberships"] != sorted(memberships[tid])
        ):
            raise ValueError("parent identity, membership or named child drift")
        keys = (
            "entity_scope",
            "named_parent_ids",
            "anchor_paths",
            "named_direct_subclass_count",
            "deprecated",
        )
        if term_scope.term_scope(ontology, tid, len(children)) != {k: row[k] for k in keys}:
            raise ValueError("ontology entity scope drift")
        selected[tid] = {
            "source_label_sha256": definition["label_sha256"],
            "definition_citation_ids": definition["definition_citation_ids"],
            "record_memberships": definition["record_memberships"],
            "named_direct_subclass_ids": children,
        }
    return selected


def derive_terms(selected, entries, query_members, ontology, scopes):
    identifiers = set(selected) | {t for row in selected.values() for t in row["named_direct_subclass_ids"]}
    direct = card.reference_index(entries, identifiers)
    result = {}
    for tid, row in sorted(selected.items()):
        pmids = [value.removeprefix("PMID:") for value in row["definition_citation_ids"]]
        if any(not p.isdigit() for p in pmids):
            raise ValueError("unsupported non-PMID definition query")
        pool = {acc for pmid in pmids for acc in query_members[pmid]}
        children = []
        for child in row["named_direct_subclass_ids"]:
            children.append(
                {
                    "aro_id": child,
                    "label_sha256": citations.text_hash(ontology[child]["label"]),
                    "reference_candidates": [
                        {
                            "protein_accession": "UniProtKB:" + entry["primaryAccession"],
                            "explicit_card_xref": child,
                            "shared_parent_definition_citations": sorted(
                                "PMID:" + p for p in pmids if entry["primaryAccession"] in query_members[p]
                            ),
                            "scope": "CHILD_TERM_REFERENCE_NOT_PARENT_IDENTITY",
                        }
                        for entry, _ in direct.get(child, [])
                    ],
                }
            )
        parent = [
            {
                "protein_accession": "UniProtKB:" + entry["primaryAccession"],
                "explicit_card_xref": tid,
                "scope": "REFERENCE_NOT_EXPERIMENTAL_IDENTITY",
            }
            for entry, _ in direct.get(tid, [])
        ]
        linked = {
            c["protein_accession"].removeprefix("UniProtKB:")
            for child in children
            for c in child["reference_candidates"]
        }
        linked.update(c["protein_accession"].removeprefix("UniProtKB:") for c in parent)
        literal = []
        for acc in sorted(pool):
            names, _ = literature.match_entry(entries[acc], tid, ontology[tid]["label"])
            if names:
                literal.append(
                    {
                        "protein_accession": "UniProtKB:" + acc,
                        "source_citation_ids": sorted("PMID:" + p for p in pmids if acc in query_members[p]),
                        "matched_gene_fields": [
                            {"field": name["field"], "value_sha256": citations.text_hash(name["value"])}
                            for name in names
                        ],
                        "scope": "LITERAL_NAME_AND_CITATION_REFERENCE_NOT_ALLELE_IDENTITY",
                    }
                )
        literal_ids = {c["protein_accession"].removeprefix("UniProtKB:") for c in literal}
        result[tid] = {
            **row,
            "entity_scope": scopes[tid]["entity_scope"],
            "direct_parent_reference_candidates": parent,
            "named_direct_subclasses": children,
            "literal_label_reference_candidates": literal,
            "literature_entries": len(pool),
            "literature_entries_with_explicit_parent_or_child_link": len(pool & linked),
            "citation_only_entries": len(pool - linked - literal_ids),
            "parent_accession_assignment": None,
            "child_accession_propagation": False,
            "primary_review_status": "OPEN",
            "no_result_is_biological_absence": False,
            "disposition": "RNA_NOT_A_PROTEIN_PRODUCT"
            if scopes[tid]["entity_scope"] == "RNA_TERM_NOT_A_PROTEIN_PRODUCT"
            else "PARENT_IDENTITY_REQUIRES_PRIMARY_REVIEW",
        }
    return result


def project_reference(entry, taxon):
    accession, taxid = entry["primaryAccession"], entry["organism"]["taxonId"]
    audit = entry["entryAudit"]
    if (
        "sequence" in entry
        or type(taxid) is not int
        or taxid < 1
        or any(type(audit.get(k)) is not int or audit[k] < 1 for k in ("entryVersion", "sequenceVersion"))
        or entry["entryType"] not in {"UniProtKB reviewed (Swiss-Prot)", "UniProtKB unreviewed (TrEMBL)"}
    ):
        raise ValueError("invalid reference entry or unexpected sequence")
    if taxon is not None and (
        taxon["taxonId"] != taxid or taxon.get("active") is not True or not taxon.get("rank")
    ):
        raise ValueError("inactive, mismatched or unranked reference taxonomy")
    return {
        "accession": "UniProtKB:" + accession,
        "entry_type": entry["entryType"],
        "entry_version": audit["entryVersion"],
        "sequence_version": audit["sequenceVersion"],
        "reference_taxon_id": f"NCBITaxon:{taxid}",
        "reference_organism_name": entry["organism"]["scientificName"],
        "taxonomy_scientific_name": taxon["scientificName"] if taxon is not None else None,
        "taxonomy_rank": taxon["rank"] if taxon is not None else None,
        "taxonomy_identity_verified": taxon is not None,
        "bibliography": concordance.entry_bibliography(entry),
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
        "genome_assignment": False,
    }


def reference_accessions(terms):
    result = set()
    for row in terms.values():
        for child in row["named_direct_subclasses"]:
            result.update(
                c["protein_accession"].removeprefix("UniProtKB:") for c in child["reference_candidates"]
            )
        for key in ("direct_parent_reference_candidates", "literal_label_reference_candidates"):
            result.update(c["protein_accession"].removeprefix("UniProtKB:") for c in row[key])
    return result


def analyze(root, directory, only=None):
    plan_path = directory / "plan.json"
    plan = json.loads(plan_path.read_bytes())
    paths = {k: reference.check_pin(root, p) for k, p in plan["inputs"].items()}
    source, definitions, prior = [
        json.loads(paths[k].read_bytes())
        for k in ("source_scope", "definition_citations", "prior_literature")
    ]
    if any(source[k] != plan["inputs"][k] for k in ("ontology_cache", "source_inventory", "reference_audit")):
        raise ValueError("source pins differ from parent plan")
    cached = json.loads(paths["ontology_cache"].read_bytes())
    body = cached["body"].encode()
    if (
        cached["status"] != 200
        or len(body) != cached["bytes"]
        or citations.text_hash(cached["body"]) != cached["sha256"]
    ):
        raise ValueError("ontology response identity mismatch")
    ontology, _, date = term_scope.parse_ontology(body)
    if date != plan["ontology_date"]:
        raise ValueError("ontology date mismatch")
    census, labels, memberships, records = citations.read_corpus(root, paths["current_census"])
    selected = select_terms(source, definitions, ontology, labels, memberships)
    if selected != plan["selected_terms"] or plan["fields"] != card.FIELDS or plan["page_size"] != 500:
        raise ValueError("selection or metadata request plan drift")
    pmids = sorted(
        {p.removeprefix("PMID:") for row in selected.values() for p in row["definition_citation_ids"]},
        key=int,
    )
    reused = {
        p: str(Path(prior["queries"][p]["pages"][0]["cache"]["path"]).parent)
        for p in pmids
        if p in prior["queries"]
    }
    if (
        pmids != plan["all_pmids"]
        or reused != plan["reused_queries"]
        or plan["pmids"] != [p for p in pmids if p not in reused]
    ):
        raise ValueError("incomplete or duplicated literature plan")
    reference_audit = json.loads(paths["reference_audit"].read_bytes())
    extra = {
        "protein_snapshot": {
            "path": "reports/resistance-grounding-2026-10-07/card-proteins.json",
            "sha256": reference_audit["protein_snapshot_sha256"],
        },
        "taxonomy_snapshot": {
            "path": "reports/resistance-grounding-2026-10-07/card-taxonomy.json",
            "sha256": reference_audit["taxonomy_snapshot_sha256"],
        },
    }
    snapshot, tax_snapshot = [
        json.loads(reference.check_pin(root, extra[k]).read_bytes())
        for k in ("protein_snapshot", "taxonomy_snapshot")
    ]
    if (
        snapshot["source_inventory_sha256"] != plan["inputs"]["source_inventory"]["sha256"]
        or tax_snapshot["proteins_sha256"] != extra["protein_snapshot"]["sha256"]
        or snapshot["total"] != len(snapshot["entries"])
    ):
        raise ValueError("reference snapshot provenance mismatch")
    entries, queries, members = dict(snapshot["entries"]), {}, {}
    for pmid in pmids:
        query_directory = root / reused[pmid] if pmid in reused else directory
        rows, queries[pmid] = literature.read_query(root, query_directory, pmid)
        if pmid in reused and queries[pmid] != prior["queries"][pmid]:
            raise ValueError("reused literature query changed")
        if queries[pmid]["release"] != snapshot["release"]:
            raise ValueError("reference and literature release mismatch")
        members[pmid] = set(rows)
        for acc, entry in rows.items():
            if acc in entries and entry != entries[acc]:
                raise ValueError("conflicting reference metadata across queries")
            entries[acc] = entry
    chosen = set(selected) if only is None else set(only)
    if not chosen or not chosen <= set(selected):
        raise ValueError("invalid selected parent terms")
    all_records = {v for row in selected.values() for v in row["record_memberships"]}
    if [r for r in records if r["identifier"] in all_records] != plan["records"]:
        raise ValueError("current record pins differ from preflight")
    all_terms = derive_terms(selected, entries, members, ontology, source["terms"])
    all_matched = reference_accessions(all_terms)
    taxa = dict(tax_snapshot["taxa"])
    missing = sorted(
        {
            entries[acc]["organism"]["taxonId"]
            for acc in all_matched
            if str(entries[acc]["organism"]["taxonId"]) not in taxa
        }
    )
    taxonomy_plan = {
        "source_plan": reference.pin(root, plan_path),
        "query_inputs": [
            item
            for query in queries.values()
            for page in query["pages"]
            for item in (page["cache"], page["receipt"])
        ],
        "matched_accessions": sorted(all_matched),
        "new_taxon_ids": missing,
    }
    taxonomy_path = directory / "taxonomy-plan.json"
    if json.loads(taxonomy_path.read_bytes()) != taxonomy_plan:
        raise ValueError("additional reference taxonomy plan does not reproduce")
    extra["taxonomy_plan"] = reference.pin(root, taxonomy_path)
    taxonomy_requests = {}
    for taxid in missing:
        key = "tax-" + str(taxid)
        taxa[str(taxid)], taxonomy_requests[key] = reference.read_response(
            root, directory, key, f"/taxonomy/{taxid}"
        )
        if taxonomy_requests[key]["release"] != snapshot["release"]:
            raise ValueError("reference taxonomy release differs from protein release")
    terms = {t: all_terms[t] for t in sorted(chosen)}
    matched = reference_accessions(terms)
    proteins = {
        "UniProtKB:" + acc: project_reference(
            entries[acc], taxa.get(str(entries[acc]["organism"]["taxonId"]))
        )
        for acc in sorted(matched)
    }
    ids = {v for row in terms.values() for v in row["record_memberships"]}
    return {
        "scope": SCOPE,
        "selection": plan["selection"] if only is None else "CANARY_ONLY",
        "inputs": {**plan["inputs"], **extra, "plan": reference.pin(root, plan_path)},
        "release": snapshot["release"],
        "terms": terms,
        "reference_proteins": proteins,
        "reference_taxonomy_requests": taxonomy_requests,
        "queries": queries,
        "records": [r for r in records if r["identifier"] in ids],
        "summary": {
            "corpus_record_hashes_verified": len(census),
            "selected_terms": len(terms),
            "selected_records": len(ids),
            "assertion_memberships": sum(len(row["record_memberships"]) for row in terms.values()),
            "literature_queries": len(queries),
            "new_queries": len(plan["pmids"]),
            "reused_queries": len(reused),
            "query_pages": sum(len(row["pages"]) for row in queries.values()),
            "unique_literature_entries": len(set().union(*members.values())),
            "zero_result_queries": sum(q["result_count"] == 0 for q in queries.values()),
            "terms_without_definition_citations": sum(
                not r["definition_citation_ids"] for r in terms.values()
            ),
            "terms_with_child_references": sum(
                any(c["reference_candidates"] for c in r["named_direct_subclasses"]) for r in terms.values()
            ),
            "direct_parent_reference_candidates": sum(
                len(r["direct_parent_reference_candidates"]) for r in terms.values()
            ),
            "terms_with_literal_label_references": sum(
                bool(r["literal_label_reference_candidates"]) for r in terms.values()
            ),
            "reference_proteins": len(proteins),
            "reference_taxa": len({row["reference_taxon_id"] for row in proteins.values()}),
            "unverified_reference_taxa": sorted(
                {r["reference_taxon_id"] for r in proteins.values() if not r["taxonomy_identity_verified"]}
            ),
            "entity_scopes": dict(Counter(r["entity_scope"] for r in terms.values())),
            "biological_record_writes": 0,
            "experimental_protein_assignments": 0,
            "whole_record_reviews_completed": 0,
        },
        "attribution": source["attribution"],
        "limits": [
            "Named subclass links are not same-entity or same-allele mappings.",
            "Child references are not propagated to parent claims or their compound memberships.",
            "Shared bibliography is a review lead, not primary experimental support.",
            "Reference organism identifiers do not identify experimental isolates or genomes.",
            "No matches in these bounded queries do not establish biological absence.",
            "No NCBI endpoint, card.json, sequence, variant, protocol or numerical AST retrieval.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=DEFAULT_DIRECTORY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--only", action="append")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path.cwd()
    result = analyze(root, root / args.directory, args.only)
    encoded = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.check:
        if args.output.read_bytes() != encoded:
            raise ValueError("parent reference dossier does not reproduce")
    else:
        if args.output.exists() and args.output.read_bytes() != encoded:
            raise ValueError("refusing to overwrite a different parent reference dossier")
        args.output.write_bytes(encoded)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
