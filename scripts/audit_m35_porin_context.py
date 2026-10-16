"""Replay publication-qualified porin references without assigning resistant alleles."""

import argparse
import json
from pathlib import Path

import audit_daptomycin_locus_context as previous
import audit_outer_membrane_evidence as outer
from audit_card_protein_name_screen import protein_names

prior, aliases, mex = previous.prior, previous.aliases, previous.mex
reference, require, read_json = prior.reference, prior.require, prior.read_json
PREFIX = "research/2026-10-15-m35-porin-context"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
SCOPE = "M35_PAPER_NAME_SPECIES_REFERENCE_CONTEXT_OMP1_UNRESOLVED"
POLICY = "EXACT_NATIVE_FULL_NAME_WITH_SAME_PAPER_PMID_DOI_AND_SPECIES_NOT_A_GENE_SYMBOL"
TERMS = {"ARO:3004124": ("M35", "480"), "ARO:3004128": ("Omp1", "615")}
NAME = "Outer membrane porin M35"
PMID, DOI = "16159786", "10.1128/jb.187.18.6528-6535.2005"
QUALIFIED = "PAPER_PROTEIN_NAME_AND_SPECIES_REFERENCE_NOT_EXPERIMENTAL_ALLELE"
CONSTRAINTS = {
    "new_native_requests": 0,
    "new_protein_requests": 0,
    "new_taxonomy_requests": 0,
    "ncbi_requests": 0,
    "biological_record_writes": False,
    "experimental_allele_assignments": False,
    "issue_1040": "DEFERRED",
    "full_corpus_goal_status": "OPEN",
}


def candidate(entry, node):
    require(entry["entryType"] in previous.identifiers.ACTIVE, "inactive or unknown reference state")
    names = [n for n in protein_names(entry) if n["value"] == NAME and n["path"].endswith("/fullName")]
    publications = []
    for i, item in enumerate(entry.get("references", [])):
        refs = item.get("citation", {}).get("citationCrossReferences", [])
        if {"database": "PubMed", "id": PMID} in refs and any(
            r.get("database") == "DOI" and r.get("id", "").casefold() == DOI for r in refs
        ):
            publications.append({"native_reference_index": i, "pmid": PMID, "doi": DOI})
    taxonomy_matches = (
        node.get("active") is True
        and node["rank"] == "species"
        and str(node["taxonId"]) == str(entry["organism"]["taxonId"]) == "480"
        and node["scientificName"] == entry["organism"]["scientificName"] == "Moraxella catarrhalis"
    )
    qualified = bool(names and publications and taxonomy_matches)
    return {
        "protein_accession": "UniProtKB:" + entry["primaryAccession"],
        "exact_full_name_matches": names,
        "same_paper_identifier_matches": publications,
        "same_native_species": taxonomy_matches,
        "native_source_gene_matches": prior.prior.gene_matches(entry, "M35"),
        "qualified_reference": qualified,
        "disposition": QUALIFIED if qualified else "NAME_CITATION_OR_SPECIES_UNRESOLVED_WITHHELD",
        "gene_symbol_inferred_from_protein_name": False,
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
        "experimental_genome_assignment": None,
        "individual_paper_isolate_assignment": None,
        "reference_identity_establishes_resistance": False,
    }


def check_assessment(a):
    identity, later, hold = a["m35_identity"], a["m35_later_study"], a["omp1_archive_access"]
    require(
        a["scope"] == "SELECTED_PUBLICATION_IDENTITY_CONTEXT_NOT_EXPERIMENTAL_ALLELE_GROUNDING"
        and a["ncbi_requests"] == 0
        and a["issue_1040"] == "DEFERRED"
        and identity["pmid"] == PMID
        and identity["doi"] == DOI
        and identity["source_url"] == "https://journals.asm.org/doi/full/" + DOI
        and identity["access"] == "WEB_TOOL_PUBLISHER_HTML_READ"
        and identity["source_species"] == "Moraxella catarrhalis"
        and identity["source_protein_designation"] == "M35"
        and identity["reviewed_native_full_name"] == NAME
        and later["pmid"] == "20801781"
        and later["doi"] == "10.1093/jac/dkq312"
        and later["source_url"] == "https://academic.oup.com/jac/article-pdf/65/10/2089/2088349/dkq312.pdf"
        and later["access"] == "WEB_TOOL_PUBLISHER_PDF_TEXT_READ"
        and later["named_parent_strains"] == ["O35E", "300", "415"],
        "reviewed publication identity or scope changed",
    )
    groups = [
        (
            a,
            (
                "local_publisher_bodies_available",
                "manual_web_assessment_is_native_body_replay",
                "experimental_allele_assignments",
                "experimental_strain_or_genome_assignments",
                "numeric_ast_exported",
                "variant_specifications_exported",
                "protocols_exported",
                "whole_record_primary_signoff",
                "biological_record_writes",
            ),
        ),
        (
            identity,
            (
                "gene_symbol_inferred_from_protein_name",
                "individual_native_accession_to_paper_isolate_crosswalk_verified",
                "paper_nucleotide_to_uniprot_crosswalk_verified",
                "figures_visually_reviewed",
                "supplements_reviewed",
                "whole_paper_primary_signoff",
            ),
        ),
        (
            later,
            (
                "reference_proteins_assigned_to_later_subjects",
                "table_visually_reviewed",
                "results_reviewed_for_ast_curation",
                "supplements_reviewed",
                "whole_paper_primary_signoff",
            ),
        ),
        (
            hold,
            (
                "native_local_http_receipt_available",
                "origin_http_status_inferred",
                "primary_text_reviewed",
                "global_unavailability_or_paywall_inferred",
            ),
        ),
    ]
    require(all(d[k] is False for d, keys in groups for k in keys), "assessment overclaims evidence scope")
    require(
        hold["pmid"] == "9353750"
        and hold["source_url"] == "https://crinoidea.semicrobiologia.org/info/revista_hist/13_3.pdf"
        and hold["web_tool_result"] == "Failed to fetch: (502) Bad Gateway"
        and hold["same_route_retries"] == hold["alternate_routes_requested"] == 0
        and hold["disposition"] == "ACCESS_UNRESOLVED_NO_PRIMARY_IDENTITY_ASSIGNMENT",
        "archive access limitation changed",
    )


def combined_coverage(old, added):
    qualified, remaining = old["qualified_terms"], old["remaining_terms"]
    require(
        old["cohort_terms"] == 178
        and len(qualified) == len(set(qualified))
        and len(remaining) == len(set(remaining))
        and not set(qualified) & set(remaining)
        and len(qualified) + len(remaining) == 178
        and set(TERMS) <= set(remaining)
        and set(added) <= set(TERMS)
        and len(added) == len(set(added)),
        "coverage overlap, duplicate or unreviewed source term",
    )
    return {
        "cohort_terms": 178,
        "previous_qualified_count": len(qualified),
        "new_qualified_terms": sorted(added),
        "qualified_terms": sorted(set(qualified) | set(added)),
        "remaining_terms": sorted(set(remaining) - set(added)),
        "whole_corpus_completion": False,
    }


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["reviewed_name_policy"] == POLICY
        and plan["constraints"] == CONSTRAINTS,
        "audit constraints changed",
    )
    for pin in plan["inputs"].values():
        reference.check_pin(root, pin)
    inputs = {k: read_json(root, p) for k, p in plan["inputs"].items() if k != "source_queue"}
    require(
        inputs["previous_verification"]["artifacts"]["dossier"] == plan["inputs"]["prior"],
        "previous verification binding changed",
    )
    assessment = inputs["assessment"]
    check_assessment(assessment)
    rows = {t: inputs["all_status"]["terms"][t] for t in TERMS}
    require(rows == plan["source_context"], "source term contexts changed")
    records, claims = prior.prior.members.current_context(
        root,
        inputs["index"],
        inputs["corpus_update"],
        set(TERMS),
        {t: r["source_label"] for t, r in rows.items()},
    )
    require(records == plan["records"] and claims == plan["claims"], "complete source cohort changed")
    annotations = aliases.annotation_context(
        aliases.ontology_graph(root, inputs["definitions"]), rows, inputs["definitions"], {}
    )
    nodes, taxonomy, species, gene_queries = {}, {}, {}, {}
    for term, (gene, tid) in TERMS.items():
        nodes[tid], taxonomy[tid] = prior.cached_node(root, inputs["taxonomy_inventory"]["registry"][tid])
        require(
            prior.prior.species_name_binding(rows[term]["tokens"]["species"], nodes[tid]),
            "source species lacks native taxonomy binding",
        )
        species[term] = prior.lineages.identity(nodes[tid])
        old = inputs["all_status"]["queries"]["proteins-" + tid]
        query = f"(gene_exact:{gene.lower()}) AND taxonomy_id:{tid}"
        require(
            old["complete_for_query"] is True and len(old["pages"]) == 1 and old["query"] == query,
            "old exact-gene query changed or incomplete",
        )
        entries, source = mex.native_query(
            root,
            old["pages"][0]["receipt"],
            {
                "query": [query],
                "format": ["json"],
                "size": ["500"],
                "sort": ["accession asc"],
                "fields": [prior.FIELDS],
            },
        )
        require(len(entries) == old["result_count"] == 0, "old exact-gene query no longer empty")
        gene_queries[term] = {"source": source, "result_count": len(entries), "biological_absence": False}
    queries, pools = {}, {}
    for pmid in (PMID, "20801781", "25856195", "9353750"):
        own = inputs["citation_queries"]["queries"][pmid]
        entries, source = aliases.literature.read_query(root, root / own["directory"], pmid)
        require(
            source == own["query"] and source["complete_for_query"] is True,
            "own-citation query changed or incomplete",
        )
        pools[pmid], queries[pmid] = entries, source
    require(
        set(pools[PMID]) == {"Q3MK85", "Q3MK87"}
        and pools["20801781"] == pools["9353750"] == {}
        and set(pools["25856195"]) == {"A0A0J9X1Q5"},
        "inspected citation candidates changed",
    )
    candidates, views = {}, {}
    for accession, entry in sorted(pools[PMID].items()):
        candidates[accession] = candidate(entry, nodes["480"])
        require(
            candidates[accession]["qualified_reference"]
            and not candidates[accession]["native_source_gene_matches"],
            "M35 reference qualification or gene-field absence changed",
        )
        views[accession] = prior.prior.members.member_reference(entry, nodes["480"])
    old_outer = inputs["outer_membrane"]
    pub = old_outer["publications"]["9353750"]
    for pin in (pub["source"][k] for k in ("body", "receipt", "attempt", "plan")):
        reference.check_pin(root, pin)
    body = read_json(root, pub["source"]["body"])
    metadata = outer.project_metadata(body, "9353750")
    require({**metadata, "source": pub["source"]} == pub, "prior indexed publication changed")
    types = body["resultList"]["result"][0]["pubTypeList"]["pubType"]
    require(types == ["Review", "Journal Article"], "indexed publication types changed")
    primary = old_outer["primary_context"]
    payload = reference.check_pin(root, primary["source"]["body"]).read_bytes()
    require(
        {**outer.project_primary(payload), "source": primary["source"]} == primary,
        "prior scoped Omp1 primary assessment changed",
    )
    nonmatch = outer.project_nonmatch(pools["25856195"]["A0A0J9X1Q5"])
    terms = {}
    for term, row in sorted(rows.items()):
        qualified = [c["protein_accession"] for c in candidates.values()] if term == "ARO:3004124" else []
        terms[term] = {
            "source_label": row["source_label"],
            "record_memberships": row["record_memberships"],
            "definition_citations": row["definition_citations"],
            "source_species": species[term],
            "qualified_reference_accessions": qualified,
            "status": QUALIFIED if qualified else "OMP1_IDENTITY_UNRESOLVED_NOT_BIOLOGICAL_ABSENCE",
            "whole_record_primary_review": "OPEN",
        }
    added = [t for t, r in terms.items() if r["qualified_reference_accessions"]]
    coverage = combined_coverage(inputs["prior"]["coverage"], added)
    result = {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "inputs": plan["inputs"],
        "records": records,
        "claims": claims,
        "source_annotations": annotations,
        "terms": terms,
        "reference_candidates": candidates,
        "reference_views": views,
        "taxonomy_sources": taxonomy,
        "citation_queries": queries,
        "reused_gene_queries": gene_queries,
        "primary_assessment": assessment,
        "omp1_context": {
            "prior_indexed_metadata": pub,
            "native_publication_types": types,
            "prior_primary_context": primary,
            "unassigned_citation_hit": nonmatch,
            "new_archive_web_attempt": assessment["omp1_archive_access"],
            "omp2_or_omp3_comparison_is_omp1_alias": False,
        },
        "coverage": coverage,
        "constraints": CONSTRAINTS,
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(records),
            "source_claims": len(claims),
            "qualified_reference_entries": len(candidates),
            "new_qualified_source_terms": len(added),
            "combined_qualified_terms": len(coverage["qualified_terms"]),
            "combined_remaining_terms": len(coverage["remaining_terms"]),
            "reused_complete_queries": len(queries) + len(gene_queries),
            "reused_taxonomy_nodes": len(taxonomy),
            "new_protein_metadata_requests": 0,
            "new_taxonomy_requests": 0,
            "biological_record_writes": 0,
            "experimental_allele_assignments": 0,
            "ncbi_requests": 0,
        },
        "limits": [
            "A protein full name is not a native gene symbol; native ORF names remain separate.",
            "The two entries are separate references, "
            "not interchangeable alleles or uniquely identified study isolates.",
            "The later study's subjects are not assigned to the earlier protein references.",
            "Web-reviewed publisher context has no local body replay; "
            "figures and supplements remain unreviewed.",
            "A failed archive fetch and metadata publication types "
            "do not establish global inaccessibility or primary results.",
            "Prior Omp1 context is retained, "
            "including the excluded PigE hit and unresolved FS14 species scope.",
            "Claim reference_status retains the input-index checkpoint; "
            "term_pointer resolves this assessment.",
            "No sequences, variant specifications, protocols, numeric AST "
            "or experimental genome assignments are exported.",
            "No biological records or source inputs changed; "
            "the full-corpus investigation remains OPEN and #1040 deferred.",
        ],
        "attribution": {
            "CARD_ARO": "CC BY 4.0",
            "UniProt": "CC BY 4.0",
            "primary_papers": "Cited reference only; no source adoption",
        },
    }
    previous.previous.reject_operational_fields(result)
    return result


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
        require(output.read_text() == payload, "saved porin audit differs from offline replay")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
