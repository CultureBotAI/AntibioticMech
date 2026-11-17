"""Replay bacterial Acr reference context without assigning experimental alleles."""

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

import audit_card_complex_members as members
import audit_card_literature_expansion as literature

reference, require = members.reference, members.require
read_json = members.prior.mex.read_json
PREFIX = "research/2026-10-15-acr-reference-context"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
SCOPE = "CURRENT_CARD_ACR_REFERENCE_CONTEXT_NOT_EXPERIMENTAL_ALLELES"
COMPLEXES = {"ARO:3000384", "ARO:3004082", "ARO:3004083"}
FALSE_FIELDS = (
    "all_cohort_primary_citations_reviewed",
    "figures_visually_reviewed",
    "supplements_reviewed",
    "exact_alleles_assigned",
    "experimental_subjects_or_genomes_assigned",
    "numeric_ast_exported",
    "operational_details_exported",
    "biological_records_curated",
    "whole_record_primary_signoffs",
    "manual_primary_reading_independently_verified_by_code",
)


def cohort(root, index):
    labels = {}
    with reference.check_pin(root, index["inputs"]["source_inventory"]).open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            term, label = row["determinant_id"], row["determinant_name"]
            require(term not in labels or labels[term] == label, "conflicting source labels")
            labels[term] = label
    require(set(index["terms"]) <= set(labels), "missing source labels")
    return {
        t: n for t, n in sorted(labels.items()) if t in index["terms"] and re.search(r"\bacr\w+", n, re.I)
    }


def validate_assessment(notes):
    require(
        notes["scope"] == SCOPE and all(notes[k] is False for k in FALSE_FIELDS), "assessment scope promoted"
    )
    require(set(notes["contexts"]) == {"10692383", "14706082"}, "reading coverage changed")
    expected = {
        "10692383": (
            "10.1128/jb.182.6.1754-1756.2000",
            "https://journals.asm.org/doi/",
            "PRIMARY_EXPERIMENT_SELECTED_TEXT_CONTEXT",
            ["ARO:3000491", "ARO:3004082"],
        ),
        "14706082": (
            "10.1111/j.1469-0691.2004.00763.x",
            "https://onlinelibrary.wiley.com/doi/",
            "REVIEW_ARTICLE_NOT_AN_INDEPENDENT_EXPERIMENT",
            ["ARO:3004082"],
        ),
    }
    for pmid, (doi, base, kind, terms) in expected.items():
        row = notes["contexts"][pmid]
        require(
            row["doi"] == doi
            and row["url"] == base + doi
            and row["kind"] == kind
            and row["terms"] == terms
            and bool(row["locations"])
            and row["exact_structure_and_subject_join_established"] is False,
            "citation identity or evidence type changed",
        )
    access = notes["access"]
    require(
        access
        == {
            "web_search_queries": 4,
            "web_reader_open_operations": 2,
            "web_upstream_http_request_count_known": False,
            "new_native_publisher_requests": 0,
            "new_uniprot_requests": 0,
            "ncbi_endpoint_opened": False,
            "ncbi_requests": 0,
            "search_index_incidentally_returned_ncbi_results": True,
            "ncbi_results_used_as_primary_evidence": False,
            "outreach": False,
            "access_holds_retried": False,
            "reuse_terms_review_resumed": False,
        },
        "access accounting changed",
    )


def replay_queries(root, pmids, citation_plan):
    queries, pools = {}, {}
    for pmid in sorted(pmids):
        item = citation_plan["queries"].get(pmid)
        if item is None:
            queries[pmid] = {
                "status": "NOT_QUERIED_IN_SELECTED_INPUTS",
                "complete_for_query": False,
                "result_count": None,
                "biological_absence_inferred": False,
            }
            continue
        entries, provenance = literature.read_query(root, root / item["directory"], pmid)
        require(
            provenance == item["query"]
            and provenance["complete_for_query"]
            and provenance["release"] == "2026_03",
            "cached citation query changed",
        )
        require(
            all(not {"sequence", "features", "comments"} & set(e) for e in entries.values()),
            "unexpected operational fields",
        )
        pools[pmid] = sorted(entries)
        queries[pmid] = {
            "source": item,
            "status": "COMPLETE_QUERY_NOT_PRIMARY_REVIEW",
            "complete_for_query": True,
            "result_count": len(entries),
            "accessions": ["UniProtKB:" + a for a in sorted(entries)],
            "biological_absence_inferred": False,
            "unselected_hits_promoted_to_references": False,
        }
    return queries, pools


def term_view(term, label, index, definitions, explicit, queries, notes):
    citations = definitions["terms"][term]["definition_citation_ids"]
    parent = explicit["parents"].get(term)
    links = index["terms"][term]["links"]
    require(
        hashlib.sha256(label.encode()).hexdigest() == index["terms"][term]["source_label_sha256"],
        "source label changed",
    )
    require(
        not parent
        or (
            term in COMPLEXES
            and parent["source_label"] == label
            and parent["record_memberships"] == index["terms"][term]["record_memberships"]
        ),
        "member dossier parent binding changed",
    )
    require(term not in COMPLEXES or not links, "complex silently assigned a single protein")
    contexts = [p for p, row in notes["contexts"].items() if term in row["terms"]]
    require(all("PMID:" + p in citations for p in contexts), "reading is not an own citation")
    return {
        "source_label": label,
        "source_label_sha256": index["terms"][term]["source_label_sha256"],
        "record_memberships": index["terms"][term]["record_memberships"],
        "definition_citations": citations,
        "selected_index_links": links,
        "entity_scope": "NAMED_COMPLEX_NOT_ONE_PROTEIN" if term in COMPLEXES else "INDIVIDUAL_GENE_TERM",
        "explicit_member_context": parent,
        "explicit_member_context_status": "SELECTED_DIRECT_ONTOLOGY_EDGES_NOT_VERIFIED_COMPOSITION"
        if parent
        else "NO_SELECTED_DIRECT_MEMBER_CONTEXT_NOT_BIOLOGICAL_ABSENCE",
        "citation_query_status": {
            p.removeprefix("PMID:"): queries[p.removeprefix("PMID:")]["status"] for p in citations
        },
        "inspected_citation_contexts": contexts,
        "experimental_allele_assignment": False,
        "experimental_subject_or_genome_assignment": False,
        "whole_record_primary_signoff": False,
    }


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["constraints"]
        == {
            "issue_1040": "DEFERRED",
            "ncbi_requests": 0,
            "new_uniprot_requests": 0,
            "outreach": False,
            "reuse_terms_review_resumed": False,
            "biological_record_writes": False,
            "exact_alleles_assigned": False,
            "experimental_subjects_or_genomes_assigned": False,
            "operational_details_or_numeric_ast_exported": False,
            "whole_record_primary_signoffs": False,
        },
        "planned scope changed",
    )
    inputs = {k: read_json(root, pin) for k, pin in plan["inputs"].items()}
    assessment = reference.pin(root, root / (PREFIX + "-assessment.json"))
    notes = read_json(root, assessment)
    validate_assessment(notes)
    canary_pin = reference.pin(root, root / (PREFIX + "-canary.json"))
    canary = read_json(root, canary_pin)
    require(
        canary["plan"] == str(PLAN)
        and canary["primary_citation"] == "PMID:10692383"
        and canary["url"] == notes["contexts"]["10692383"]["url"]
        and canary["accepted_for_remaining_planned_primary_lookup"] is True
        and canary["accepted_for_biological_record_mutation"] is False
        and canary["accepted_for_experimental_identifier_assignment"] is False,
        "canary scope changed",
    )
    index, explicit = inputs["index"], inputs["members"]
    labels = cohort(root, index)
    require(sorted(labels) == plan["expected_terms"] and len(labels) == 11, "complete cohort changed")
    records, claims = members.current_context(root, index, inputs["corpus_update"], set(labels), labels)
    require(
        len(records) == plan["expected_records"] == 16 and len(claims) == plan["expected_claims"] == 31,
        "current claim coverage changed",
    )
    definitions = inputs["definition_citations"]
    citations = {p for t in labels for p in definitions["terms"][t]["definition_citation_ids"]}
    require(
        len(citations) == 19 and all(re.fullmatch(r"PMID:[1-9][0-9]*", p) for p in citations),
        "own citation set changed",
    )
    queries, pools = replay_queries(root, {p[5:] for p in citations}, inputs["citation_plan"])
    require(len(pools) == 11 and sum(not p for p in pools.values()) == 7, "cached query coverage changed")
    terms = {
        t: term_view(t, label, index, definitions, explicit, queries, notes) for t, label in labels.items()
    }
    native, native_pages = members.prior.replay_proteins(
        root, inputs["source_plan"], inputs["protein_snapshot"]
    )
    selected = {link["protein_accession"] for row in terms.values() for link in row["selected_index_links"]}
    member_refs = {
        a
        for row in terms.values()
        if row["explicit_member_context"]
        for a in row["explicit_member_context"]["reference_accessions"]
    }
    require(
        len(selected) == 4 and len(member_refs) == 5 and len(selected | member_refs) == 8,
        "selected reference coverage changed",
    )
    views, tax_sources = {}, {}
    for identifier in sorted(selected | member_refs):
        entry = native[identifier.split(":")[1]]
        tid = str(entry["organism"]["taxonId"])
        source = (
            inputs["lineages"]["taxa"].get(tid, {}).get("native_source") or explicit["taxonomy_sources"][tid]
        )
        taxon, provenance = members.prior.lineages.native_taxon(root, source, tid, "2026_03")
        view = members.member_reference(entry, taxon)
        if identifier in selected:
            identity = index["proteins"][identifier]["identity"]
            require(
                view["entry_type"] == identity["entry_type"]
                and view["entry_audit"]
                == {
                    "entryVersion": identity["entry_version"],
                    "sequenceVersion": identity["sequence_version"],
                }
                and view["reference_taxonomy"]["taxon_id"] == identity["reference_taxon_id"],
                "selected native identity changed",
            )
        if identifier in member_refs:
            require(view == explicit["reference_proteins"][identifier], "member reference projection changed")
        views[identifier], tax_sources[tid] = view, provenance
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "assessment": assessment,
        "canary": canary_pin,
        "inputs": plan["inputs"],
        "records": records,
        "claims": claims,
        "terms": terms,
        "reference_views": views,
        "citation_queries": queries,
        "native_protein_pages": native_pages,
        "taxonomy_sources": tax_sources,
        "summary": {
            "terms": len(terms),
            "claims": len(claims),
            "complete_records_read": len(records),
            "corpus_records_hash_checked": 2939,
            "named_complex_terms": len(COMPLEXES),
            "direct_reference_terms": sum(bool(t["selected_index_links"]) for t in terms.values()),
            "distinct_direct_references": len(selected),
            "distinct_member_references": len(member_refs),
            "distinct_reference_entries": len(views),
            "distinct_reference_taxa": len(tax_sources),
            "own_definition_citations": len(citations),
            "replayed_citation_queries": len(pools),
            "empty_complete_queries": sum(not p for p in pools.values()),
            "not_queried_in_selected_inputs": len(queries) - len(pools),
            "distinct_citation_query_hits_not_automatically_selected": len(
                {a for p in pools.values() for a in p}
            ),
            "new_primary_text_contexts": 1,
            "review_article_contexts_not_primary_experiments": 1,
            "new_uniprot_requests": 0,
            "new_ncbi_requests": 0,
            "biological_record_writes": 0,
        },
        "limits": {
            **plan["constraints"],
            "all_citations_queried": False,
            "all_terms_primary_reviewed": False,
            "whole_complex_composition_verified": False,
            "unrelated_yeast_acr_loci_merged": False,
            "new_reference_assignments": 0,
        },
        "attribution": "CARD/ARO and UniProt CC BY 4.0; publisher reading separately cited in assessment.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    payload = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
    target = args.root / args.output
    if args.check or target.exists():
        require(target.read_bytes() == payload, "audit does not reproduce; preserve prior output")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
