"""Replay paper-reported loci without assigning reference proteins as resistant alleles."""

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

import audit_vmlr2_structure_context as previous

identifiers, prior, aliases, mex = (
    previous.identifiers,
    previous.prior,
    previous.aliases,
    previous.mex,
)
reference, require, read_json = prior.reference, prior.require, prior.read_json
PREFIX = "research/2026-10-15-daptomycin-locus"
PLAN, OUTPUT = Path(PREFIX + "-audit-plan.json"), Path(PREFIX + ".json")
SCOPE = "PAPER_LOCUS_SEPARATOR_CROSSWALK_NOT_EXPERIMENTAL_ALLELE"
TERMS = {"ARO:3003797": "YybT", "ARO:3003800": "gdpD", "ARO:3003813": "drmA", "ARO:3003815": "YvlB"}
LOCI = {"drma-locus": ("ARO:3003813", "EF1797"), "yvlb-locus": ("ARO:3003815", "EF1753")}
POLICY = "EF_FOUR_DIGITS_WITH_OPTIONAL_SINGLE_NAMESPACE_UNDERSCORE_IN_V583_REFERENCE_CONTEXT"
QUALIFIED = "PAPER_LOCUS_SEPARATOR_AND_SPECIES_REFERENCE_NOT_EXPERIMENTAL_ALLELE"


def ordered_locus_matches(entry, source_locus):
    require(re.fullmatch(r"EF[0-9]{4}", source_locus) is not None, "unsupported source locus grammar")
    matches = []
    for i, gene in enumerate(entry.get("genes", [])):
        for j, value in enumerate(gene.get("orderedLocusNames", [])):
            native = value["value"]
            if native in {source_locus, "EF_" + source_locus[2:]}:
                matches.append(
                    {
                        "field": f"genes/{i}/orderedLocusNames/{j}",
                        "value": native,
                        "literal_equality": native == source_locus,
                        "normalization": "NONE" if native == source_locus else "SINGLE_NAMESPACE_SEPARATOR",
                    }
                )
    return matches


def candidate(entry, lead, species, native_species, node):
    require(entry["entryType"] in identifiers.ACTIVE, "inactive or unknown reference state")
    matches = ordered_locus_matches(entry, lead["paper_reference_locus"])
    same_species = species is not None and species == native_species
    strain = prior.lineages.identity(node)
    v583 = (
        str(entry["organism"]["taxonId"]) == str(node["taxonId"]) == "226185"
        and node["rank"] == "strain"
        and any("V583" in s.get("synonyms", []) for s in node.get("strains", []))
    )
    supplied_strain = lead["paper_reference_strain"]
    require(supplied_strain in {None, "V583"}, "unreviewed paper strain")
    qualified = bool(matches) and same_species and v583
    return {
        "protein_accession": "UniProtKB:" + entry["primaryAccession"],
        "paper_reference_locus": lead["paper_reference_locus"],
        "native_ordered_locus_matches": matches,
        "native_source_gene_matches": prior.prior.gene_matches(entry, lead["source_gene"]),
        "source_gene": lead["source_gene"],
        "reference_strain": strain,
        "same_reference_species": same_species,
        "native_v583_reference_context": v583,
        "paper_reference_strain": supplied_strain,
        "paper_reference_strain_matches_native": v583 if supplied_strain else None,
        "disposition": QUALIFIED if qualified else "LOCUS_OR_REFERENCE_TAXONOMY_UNRESOLVED_WITHHELD",
        "qualified_reference": qualified,
        "official_gene_rename_verified": False,
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
        "experimental_genome_assignment": None,
        "primary_resistance_validation": False,
    }


def check_assessment(assessment):
    require(
        assessment["citation"] == {"pmid": "23959318", "doi": "10.1128/aac.01473-13"}
        and assessment["source_url"] == "https://journals.asm.org/doi/full/10.1128/aac.01473-13"
        and assessment["source_access"] == "READ_THROUGH_WEB_TOOL"
        and assessment["selected_html_results_reviewed"] is True
        and assessment["figures_visually_reviewed"] == [],
        "scoped primary source changed",
    )
    require(
        all(
            assessment[k] is False
            for k in (
                "native_local_http_receipt_available",
                "native_http_status_inferred",
                "experimental_allele_assignments",
                "experimental_strain_or_genome_assignments",
                "numeric_ast_exported",
                "variant_specifications_exported",
                "protocols_exported",
                "whole_record_primary_signoff",
                "biological_record_writes",
            )
        ),
        "primary review overclaims experimental identity or inspected evidence",
    )
    correction, hold = assessment["correction"], assessment["earlier_study_access"]
    require(
        correction["doi"] == "10.1128/aac.02297-13"
        and correction["notice_text_reviewed"] is True
        and correction["replacement_image_visually_reviewed"] is False
        and correction["supplements_reviewed"] is False
        and correction["publication_chronology_resolved"] is False
        and hold["web_result"] == "403 Forbidden"
        and hold["canonical_article_http_status_inferred"] is False
        and hold["alternate_routes_requested_after_denial"] == 0,
        "correction or linkout access limitation changed",
    )
    require(set(assessment["reference_leads"]) == {v[0] for v in LOCI.values()}, "paper lead set changed")
    for term, locus in LOCI.values():
        lead = assessment["reference_leads"][term]
        require(
            lead["source_gene"] == TERMS[term]
            and lead["paper_reference_locus"] == locus
            and lead["earlier_study_independently_reviewed"] is False,
            "paper locus or evidence scope changed",
        )


def check_history(directory):
    for suffix in ("attempt", "receipt", "body"):
        require(
            set(directory.glob(f"*-{suffix}.json")) == {directory / f"{k}-{suffix}.json" for k in LOCI},
            "unaccounted or missing request artifact",
        )
    require(not list(directory.glob("*-error.json")), "unaccounted request failure")


def publication_metadata(wrapper):
    require(
        wrapper["status"] == 200
        and hashlib.sha256(wrapper["body"].encode()).hexdigest() == wrapper["sha256"]
        and urlsplit(wrapper["url"]).netloc == "www.ebi.ac.uk",
        "publication discovery cache changed",
    )
    rows = [r for r in json.loads(wrapper["body"])["resultList"]["result"] if r["id"] == "23959318"]
    require(
        len(rows) == 1 and rows[0]["source"] == "MED" and rows[0]["doi"] == "10.1128/aac.01473-13",
        "publication identifier mismatch",
    )
    return {k: rows[0][k] for k in ("id", "source", "doi", "pubYear")}


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["reviewed_locus_policy"] == POLICY
        and plan["reference_strain_taxon"] == "226185"
        and plan["reference_species_taxon"] == "1351"
        and plan["experimental_allele_assignments"] is plan["biological_record_writes"] is False
        and plan["ncbi_requests"] == 0
        and plan["issue_1040"] == "DEFERRED"
        and plan["full_corpus_goal_status"] == "OPEN",
        "audit scope changed",
    )
    documents = {k: read_json(root, p) for k, p in plan["inputs"].items()}
    frozen = documents["source_plan"]
    for pin in frozen["inputs"].values():
        reference.check_pin(root, pin)
    inputs = {k: read_json(root, p) for k, p in frozen["inputs"].items() if k != "source_queue"}
    require(
        inputs["previous_verification"]["artifacts"]["dossier"] == frozen["inputs"]["prior"],
        "prior verification binding changed",
    )
    rows = {t: inputs["all_status"]["terms"][t] for t in TERMS}
    require(rows == frozen["source_context"], "source term contexts changed")
    records, claims = prior.prior.members.current_context(
        root,
        inputs["index"],
        inputs["corpus_update"],
        set(TERMS),
        {t: r["source_label"] for t, r in rows.items()},
    )
    require(records == frozen["records"] and claims == frozen["claims"], "source-owned cohort changed")
    annotations = aliases.annotation_context(
        aliases.ontology_graph(root, inputs["definitions"]), rows, inputs["definitions"], {}
    )
    assessment = inputs["primary_assessment"]
    check_assessment(assessment)
    require(
        set(frozen["requests"]) == set(plan["receipts"]) == set(LOCI)
        and frozen["fields"] == prior.FIELDS
        and frozen["preflight"]["ignored_files_included"] is True
        and frozen["preflight"]["native_query_matches"] == [],
        "query scope or preflight changed",
    )
    directory = root / frozen["cache_directory"]
    check_history(directory)
    nodes, taxonomy = {}, {}
    for tid in ("1351", "226185"):
        nodes[tid], taxonomy[tid] = prior.cached_node(root, inputs["taxonomy_inventory"]["registry"][tid])
    species = prior.lineages.identity(nodes["1351"])
    require(
        prior.prior.species_name_binding(assessment["source_species"], nodes["1351"]),
        "paper species name lacks native taxonomy match",
    )
    views, candidates, queries = {}, {}, {}
    for key, (term, locus) in LOCI.items():
        params = {
            "query": f"(gene_exact:{locus} OR gene_exact:EF_{locus[2:]}) AND taxonomy_id:1351",
            "format": "json",
            "size": "500",
            "sort": "accession asc",
            "fields": prior.FIELDS,
        }
        require(frozen["requests"][key]["parameters"] == params, "locus query changed")
        entries, source = mex.native_query(root, plan["receipts"][key], {k: [v] for k, v in params.items()})
        receipt, attempt = previous.request_receipt(
            root, directory, key, plan["receipts"][key], plan["inputs"]["source_plan"], frozen["max_bytes"]
        )
        require(receipt["url"] == frozen["requests"][key]["url"], "request URL changed")
        previous.reject_operational_fields(entries)
        require(set(entries) == {plan["expected_candidates"][key]}, "inspected candidate set changed")
        for accession, entry in entries.items():
            require(str(entry["organism"]["taxonId"]) == "226185", "reference strain changed")
            view = prior.prior.members.member_reference(entry, nodes["226185"])
            views[accession] = view
            candidates[term] = candidate(
                entry,
                assessment["reference_leads"][term],
                species,
                view["reference_taxonomy"]["species"],
                nodes["226185"],
            )
        queries[key] = {"source": source, "attempt": attempt, "complete_result_count": len(entries)}
    canary = documents["canary"]
    require(
        canary["plan_sha256"] == plan["inputs"]["source_plan"]["sha256"]
        and canary["receipt"] == plan["receipts"]["drma-locus"]
        and canary["approved_second_metadata_query"] is True
        and canary["accession"] == plan["expected_candidates"]["drma-locus"]
        and canary["literal_locus_equality"] is False
        and canary["experimental_allele_assignment"] is False,
        "canary binding changed",
    )
    second_attempt = read_json(root, queries["yvlb-locus"]["attempt"])
    require(
        second_attempt["started_at"] > queries["drma-locus"]["source"]["retrieved_at"],
        "second query preceded first response",
    )
    hold = documents["nomenclature_hold"]
    require(
        hold["newer_primary_results_reviewed"] is hold["official_gene_rename_verified"] is False
        and hold["web_access"]["http_status_inferred"] is False
        and hold["web_access"]["alternate_routes_requested"] == 0,
        "newer nomenclature access scope changed",
    )
    old = inputs["all_status"]["queries"]["proteins-1351"]
    require(old["complete_for_query"] is True and len(old["pages"]) == 1, "old query incomplete")
    old_entries, old_source = mex.native_query(
        root,
        old["pages"][0]["receipt"],
        {
            "query": [old["query"]],
            "format": ["json"],
            "size": ["500"],
            "sort": ["accession asc"],
            "fields": [prior.FIELDS],
        },
    )
    require(
        len(old_entries) == old["result_count"]
        and not any(
            prior.prior.gene_matches(e, gene) for e in old_entries.values() for gene in TERMS.values()
        ),
        "old query now matches one of the four unresolved source genes",
    )
    citations = {}
    for pmid in ("19901023", "23959318"):
        own = inputs["citation_queries"]["queries"][pmid]
        _, source = aliases.literature.read_query(root, root / own["directory"], pmid)
        require(source == own["query"], "own citation query changed")
        citations[pmid] = source
    previous_coverage = inputs["prior"]["coverage"]
    added = sorted(t for t, c in candidates.items() if c["qualified_reference"])
    require(set(TERMS) <= set(previous_coverage["remaining_terms"]), "term already qualified")
    combined = sorted(set(previous_coverage["qualified_terms"]) | set(added))
    remaining = sorted(set(previous_coverage["remaining_terms"]) - set(added))
    require(len(combined) + len(remaining) == 178 and not set(combined) & set(remaining), "coverage overlap")
    terms = {
        t: {
            "aro_id": t,
            "source_label": r["source_label"],
            "record_memberships": r["record_memberships"],
            "definition_citations": r["definition_citations"],
            "reference_candidate": candidates.get(t),
            "qualified_reference_accessions": [candidates[t]["protein_accession"]] if t in added else [],
            "primary_evidence_limit": assessment["evidence_limits"][t],
            "whole_record_primary_review": "OPEN",
        }
        for t, r in sorted(rows.items())
    }
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "inputs": frozen["inputs"],
        "records": records,
        "claims": claims,
        "source_annotations": annotations,
        "terms": terms,
        "reference_views": views,
        "queries": queries,
        "taxonomy_sources": taxonomy,
        "locus_separator_policy": POLICY,
        "source_species": species,
        "primary_assessment": assessment,
        "nomenclature_hold": hold,
        "publication_metadata": publication_metadata(inputs["publication_discovery"]),
        "retained_other_species_yybt_context": inputs["species_context"]["terms"]["ARO:3003797"],
        "reused_gene_query": {"source": old_source, "result_count": len(old_entries), "four_gene_matches": 0},
        "reused_citation_queries": citations,
        "coverage": {
            "cohort_terms": 178,
            "previous_qualified_count": len(previous_coverage["qualified_terms"]),
            "new_qualified_terms": added,
            "qualified_terms": combined,
            "remaining_terms": remaining,
            "whole_corpus_completion": False,
        },
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(records),
            "source_claims": len(claims),
            "qualified_reference_entries": len(added),
            "new_qualified_source_terms": len(added),
            "combined_qualified_terms": len(combined),
            "combined_remaining_terms": len(remaining),
            "new_protein_metadata_requests": len(queries),
            "new_taxonomy_requests": 0,
            "reused_taxonomy_nodes": len(taxonomy),
            "reused_complete_queries": len(citations) + 1,
            "scoped_primary_html_reviews": 1,
            "biological_record_writes": 0,
            "experimental_allele_assignments": 0,
            "ncbi_requests": 0,
        },
        "limits": [
            "Locus crosswalks explicitly normalize one EF namespace separator, "
            "not arbitrary punctuation or gene symbols.",
            "The V583 proteins are reference context, "
            "not experimental derivatives or exact resistance alleles.",
            "Native LiaX naming is retained; the newer nomenclature paper "
            "and earlier linked study remain unreviewed.",
            "Selected HTML results are reviewed; original figures, "
            "the replacement figure and supplements are not.",
            "Homologue function, same-background association and a reference locus "
            "are not independent causal proof.",
            "The old pooled gene query has one result but no exact match for these four source genes; "
            "this is not biological absence.",
            "Claim reference_status fields retain the input-index checkpoint; "
            "term_pointer resolves the new assessment.",
            "No sequences, variant specifications, protocols, numeric AST "
            "or experimental genome assignments are exported.",
            "No biological records or source inputs changed; the full-corpus investigation "
            "remains OPEN and #1040 deferred.",
        ],
        "attribution": {
            "CARD_ARO": "CC BY 4.0",
            "UniProt": "CC BY 4.0",
            "primary_papers": "Cited reference only; no source adoption",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    output = args.root / args.output
    if args.check or output.exists():
        require(output.read_text() == payload, "saved daptomycin locus audit differs from offline replay")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
