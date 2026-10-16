"""Replay unresolved source identities and a separate, scoped AIF1 primary review."""

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_source_aliases as aliases
import audit_mex_component_references as mex
from rdflib import Literal, URIRef

prior = aliases.prior
reference, require, read_json = prior.reference, prior.require, prior.read_json
PREFIX = "research/2026-10-15-card-name-holds"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
SCOPE = "UNRESOLVED_NAMES_SOURCE_CONFLICTS_AND_SEPARATE_AIF1_PRIMARY_CONTEXT"
DOI = "10.15698/mic2014.01.119"
PDF_URL = "https://microbialcell.com/wp-content/uploads/2014/01/2014A-Chin-Microbial_Cell.pdf"
CGD_BASE = "https://www.candidagenome.org/download/chromosomal_feature_files/C_albicans_SC5314/"


def source_gene_conflict(label_gene, definition):
    if label_gene.casefold() == "mdr3" and definition.startswith("The Mdr2 gene is responsible for "):
        return {
            "status": "LABEL_DEFINITION_GENE_CONFLICT_WITHHELD",
            "label_gene": label_gene,
            "definition_gene": "Mdr2",
            "definition_sha256": hashlib.sha256(definition.encode()).hexdigest(),
            "correct_gene_inferred": False,
        }
    return None


def cgd_loci(mapping, features):
    expected_urls = [
        CGD_BASE + "ORF19_Assembly22_mapping.tab",
        CGD_BASE + "C_albicans_SC5314_version_A22-s08-m01-r37_chromosomal_feature.tab",
    ]
    for wrapper, url in zip((mapping, features), expected_urls, strict=True):
        require(
            wrapper["url"] == url
            and wrapper["status"] == 200
            and hashlib.sha256(wrapper["body"].encode()).hexdigest() == wrapper["sha256"]
            and len(wrapper["body"].encode()) == wrapper["bytes"],
            "CGD native source identity changed",
        )
    mapped = list(csv.DictReader(io.StringIO(mapping["body"]), delimiter="\t"))
    require(
        mapped and set(mapped[0]) == {"ORF19_ID", "ASSEMBLY22_ID", "GENE_NAME"}, "CGD mapping header changed"
    )
    require("! Genome version: A22-s08-m01-r37\n" in features["body"], "CGD assembly version changed")
    rows = [
        r for r in csv.reader(io.StringIO(features["body"]), delimiter="\t") if r and not r[0].startswith("!")
    ]
    result = {}
    for locus, expected_feature, expected_id in (
        ("orf19.3362", "C4_03350C_A", "CAL0000191273"),
        ("orf19.9721", "C2_08100W_A", "CAL0000195769"),
    ):
        links = [r for r in mapped if r["ORF19_ID"] == locus]
        matched = [r for r in rows if len(r) > 10 and r[0] == expected_feature]
        require(len(links) == len(matched) == 1, "missing or ambiguous CGD locus")
        link, row = links[0], matched[0]
        require(
            link["ASSEMBLY22_ID"] == row[0] and row[8] == expected_id and locus in row[2].split("|"),
            "CGD locus-feature join changed",
        )
        result[locus] = {
            "feature": row[0],
            "cgd_id": row[8],
            "mapping_gene_name": link["GENE_NAME"] or None,
            "feature_primary_gene_name": row[1] or None,
            "feature_aliases": row[2].split("|"),
            "feature_type": row[3],
        }
    require(
        result["orf19.3362"]["feature_primary_gene_name"] == "AIF1"
        and result["orf19.3362"]["mapping_gene_name"] == "AIF1"
        and result["orf19.9721"]["feature_primary_gene_name"] is None
        and result["orf19.9721"]["mapping_gene_name"] is None
        and "AIF1" in result["orf19.9721"]["feature_aliases"],
        "CGD gene-name ambiguity changed",
    )
    return result


def paper_locus_assignment(reference_loci, paper_locus, features):
    require(paper_locus in features, "paper locus lacks independent CGD mapping")
    source_feature = features[paper_locus]["feature"]
    matched_features = {features[locus]["feature"] for locus in reference_loci if locus in features}
    return {
        "paper_locus": paper_locus,
        "reference_loci": reference_loci,
        "paper_cgd_feature": source_feature,
        "reference_cgd_features": sorted(matched_features),
        "status": "DISTINCT_CGD_FEATURES_WITHHELD"
        if matched_features and source_feature not in matched_features
        else "EXPERIMENTAL_LOCUS_ASSIGNMENT_UNRESOLVED",
        "gene_name_match_overrides_locus_disagreement": False,
        "experimental_protein_assignment": False,
    }


def primary_review(root, plan, inputs):
    assessment = inputs["primary_assessment"]
    require(
        assessment["citation"] == {"doi": DOI, "pmid": "28357223", "authors_year": "Chin et al. 2014"}
        and assessment["visually_inspected_printed_pages"] == list(range(58, 64))
        and assessment["figures_visually_inspected"] == [1, 2]
        and assessment["results_and_discussion_reviewed"] is True
        and assessment["evidence_type"] == "QUALITATIVE_RELATIVE_GROWTH_AND_CELL_DEATH_CONTEXT"
        and assessment["formulation_disposition"] == "FORMULATION_NOT_RESOLVED_TO_CORPUS_STRUCTURE"
        and assessment["aneuploidy_validation"] == "NOT_ESTABLISHED_BY_REVIEWED_STUDY"
        and all(
            assessment[k] is False
            for k in (
                "numeric_ast_exported",
                "exact_structure_match_to_neutral_record",
                "source_spelling_correction_inferred",
                "experimental_reference_protein_assignment",
                "experimental_allele_assignment",
                "experimental_strain_taxon_or_genome_assignment",
                "whole_record_primary_signoff",
                "negative_control_inferred_globally_ineffective",
            )
        ),
        "primary review scope changed",
    )
    receipt = read_json(root, assessment["source"])
    network = inputs["network_enabled_plan"]
    require(network["original_plan"] == plan["inputs"]["source_plan"], "source plan history changed")
    attempt, error = [read_json(root, network[k]) for k in ("prior_attempt", "prior_error")]
    require(
        attempt["url"] == error["url"] == network["url"] == receipt["url"] == PDF_URL
        and "NameResolutionError" in error["error"]
        and attempt["plan_sha256"] == plan["inputs"]["source_plan"]["sha256"]
        and network["local_attempts_including_this_one"] == 2
        and network["previous_local_dns_failure_retried"] is True
        and receipt["prior_local_dns_failure_retried"] is True
        and receipt["plan_sha256"] == plan["inputs"]["network_enabled_plan"]["sha256"],
        "local DNS failure or separately approved attempt history changed",
    )
    directory = root / plan["cache_directory"]
    second_path = directory / "chin-primary-network-enabled-attempt.json"
    second = json.loads(second_path.read_bytes())
    require(all(receipt[k] == v for k, v in second.items()), "second attempt differs from receipt")
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    pdf = reference.check_pin(root, receipt["body"]).read_bytes()
    require(
        receipt["status"] == 200
        and pdf.startswith(b"%PDF-")
        and len(pdf) == receipt["bytes"] <= network["max_bytes"]
        and "application/pdf" in headers.get("content-type", "")
        and not headers.get("location")
        and receipt["retries"] == receipt["redirects_followed"] == 0
        and {p.name for p in directory.glob("*-error.json")} == {"chin-primary-error.json"}
        and not (directory / "chin-primary-receipt.json").exists(),
        "native PDF response or attempt accounting changed",
    )
    inspection = read_json(root, assessment["inspection"])
    require(inspection["source"] == receipt["body"], "inspected PDF differs from retrieved source")
    require([p["printed_page"] for p in inspection["pages"]] == list(range(58, 64)), "page coverage changed")
    texts = []
    for i, page in enumerate(inspection["pages"]):
        require(page["zero_based_page"] == i, "page order changed")
        reference.check_pin(root, page["image"])
        texts.append(reference.check_pin(root, page["text"]).read_text())
    require(
        DOI in texts[0]
        and "FIGURE 1:" in texts[1]
        and "FIGURE 2:" in texts[2]
        and "orf19.3362" in texts[3]
        and "Cancidas" in texts[3]
        and "RBY1132" in texts[3]
        and "W303-1A" in texts[3],
        "primary identity or inspected evidence location changed",
    )
    return {
        **assessment,
        "native_response": receipt,
        "page_artifacts": inspection,
        "network_enabled_attempt": reference.pin(root, second_path),
        "local_attempts": 2,
        "successful_http_responses": 1,
        "local_dns_failure_retried": True,
        "source_http_denial_bypassed": False,
    }


def protein_queries(root, plan, inputs):
    frozen = inputs["protein_plan"]
    require(
        frozen["primary_source"] == inputs["primary_assessment"]["source"]
        and frozen["pdf_inspection_artifacts"] == inputs["primary_assessment"]["inspection"]
        and frozen["visually_inspected_printed_pages"]
        == inputs["primary_assessment"]["visually_inspected_printed_pages"],
        "reference query plan differs from inspected primary context",
    )
    expected_queries = {
        "yeast-aif1": "gene_exact:AIF1 AND taxonomy_id:4932 AND reviewed:true",
        "candida-paper-locus": "gene_exact:orf19.3362 AND taxonomy_id:5476",
    }
    require(
        set(frozen["requests"]) == set(plan["protein_receipts"]) == set(expected_queries),
        "query scope changed",
    )
    preflight = read_json(root, frozen["preflight"])
    require(
        preflight["ignored_files_included"] is True and preflight["matching_query_history"] == [],
        "query preflight changed",
    )
    entries, sources, pools = {}, {}, {}
    for key, query in expected_queries.items():
        expected = {
            "query": [query],
            "format": ["json"],
            "size": ["500"],
            "sort": ["accession asc"],
            "fields": [prior.FIELDS],
        }
        item = frozen["requests"][key]
        require(
            item["parameters"] == {k: v[0] for k, v in expected.items()}, "planned protein fields changed"
        )
        path = root / plan["cache_directory"] / (key + "-attempt.json")
        attempt = json.loads(path.read_bytes())
        require(
            attempt["plan_sha256"] == plan["inputs"]["protein_plan"]["sha256"]
            and attempt["key"] == key
            and attempt["url"] == item["url"]
            and attempt["retries"] == attempt["redirects_followed"] == 0,
            "query attempt changed",
        )
        found, source = mex.native_query(root, plan["protein_receipts"][key], expected)
        require(
            source["url"] == item["url"] and source["bytes"] <= frozen["max_bytes"], "query source changed"
        )
        require(
            all(not {"sequence", "features", "comments"} & set(e) for e in found.values()),
            "operational fields",
        )
        require(not set(found) & set(entries), "cross-query accession needs explicit review")
        if key == "yeast-aif1":
            require(
                all(e["entryType"] == "UniProtKB reviewed (Swiss-Prot)" for e in found.values()),
                "entry status",
            )
        entries.update(found)
        pools[key] = sorted(found)
        sources[key] = {
            "native_source": source,
            "attempt": reference.pin(root, path),
            "result_count": len(found),
        }
    canary = inputs["protein_canary"]
    require(
        canary["plan_sha256"] == plan["inputs"]["protein_plan"]["sha256"]
        and canary["source"] == plan["protein_receipts"]["yeast-aif1"]
        and canary["accessions"] == pools["yeast-aif1"]
        and canary["approved_for_remaining_query"] is True,
        "canary binding changed",
    )
    require(
        len(pools["yeast-aif1"]) == 1 and pools["candida-paper-locus"] == [],
        "inspected query results changed",
    )
    directory = root / plan["cache_directory"]
    successful = {"chin-primary-network-enabled", *expected_queries}
    require(
        {p.name for p in directory.glob("*-attempt.json")}
        == {key + "-attempt.json" for key in successful | {"chin-primary"}}
        and {p.name for p in directory.glob("*-receipt.json")}
        == {key + "-receipt.json" for key in successful},
        "unaccounted request attempt or response",
    )
    old = inputs["gene_checkpoint"]["queries"]["proteins-5476"]["native_source"]
    found, source = mex.native_query(root, old["receipt"], parse_qs(urlsplit(old["url"]).query))
    require(source == old, "cached Candida query provenance changed")
    candida = "A0A1D8PI22"
    require(prior.native_matches(found[candida], "AIF1"), "cached gene-name reference changed")
    entries[candida] = found[candida]
    sources["cached-candida-name"] = {
        "native_source": source,
        "reused": True,
        "result_count": len(found),
        "selected_name_reference": candida,
    }
    return entries, sources


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["constraints"]
        == {
            "biological_record_writes": 0,
            "experimental_identity_assignments": 0,
            "ncbi_requests": 0,
            "new_taxonomy_requests": 0,
            "issue_1040": "DEFERRED",
            "source_spelling_corrections": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "scope changed",
    )
    for pin in plan["inputs"].values():
        reference.check_pin(root, pin)
    inputs = {k: read_json(root, p) for k, p in plan["inputs"].items() if k != "source_queue"}
    require(
        inputs["prior_verification"]["artifacts"]["dossier"] == plan["inputs"]["prior"],
        "prior binding changed",
    )
    selected = {t: r for t, r in inputs["prior"]["terms"].items() if r["reference_name_context"] is None}
    require(
        len(selected) == 31 and plan["additional_primary_context_term"] == "ARO:3009378", "cohort changed"
    )
    extra = inputs["gene_checkpoint"]["terms"]["ARO:3009378"]
    context = {**selected, "ARO:3009378": extra}
    records, claims = prior.prior.members.current_context(
        root,
        inputs["index"],
        inputs["corpus_update"],
        set(context),
        {t: r["source_label"] for t, r in context.items()},
    )
    graph = aliases.ontology_graph(root, inputs["definitions"])
    annotations = aliases.annotation_context(graph, selected, inputs["definitions"], {})
    terms, flagged = {}, []
    for term, row in selected.items():
        node = URIRef(aliases.definitions.ontology.BASE + term.removeprefix("ARO:"))
        conflicts = []
        for value in graph.objects(node, aliases.definitions.DEFINITION):
            require(
                isinstance(value, Literal) and value.language is None and value.datatype is None,
                "uninspected definition literal type",
            )
            conflict = source_gene_conflict(row["tokens"]["gene"], str(value))
            if conflict:
                conflicts.append(conflict)
        if conflicts:
            flagged.append(term)
        terms[term] = {
            "prior_assessment": row,
            "source_annotations": annotations[term],
            "source_gene_conflicts": conflicts,
            "name_disposition": "UNRESOLVED_NO_CORRECTION_INFERRED",
            "new_qualified_reference_accessions": [],
            "experimental_subject_assignment": False,
        }
    require(sorted(flagged) == plan["source_gene_conflicts"], "inspected source conflict cohort changed")
    review = primary_review(root, plan, inputs)
    frozen = inputs["protein_plan"]
    features = cgd_loci(read_json(root, frozen["cg_mapping"]), read_json(root, frozen["cg_features"]))
    entries, sources = protein_queries(root, plan, inputs)
    registry = inputs["taxonomy_inventory"]["registry"]
    species, taxonomy, views = {}, {}, {}
    for name, tid in plan["paper_species"].items():
        node, provenance = prior.cached_node(root, registry[tid])
        require(
            node["scientificName"] == name and node["rank"] == "species", "paper species identity changed"
        )
        species[name] = {"identity": prior.lineages.identity(node), "experimental_strain_assignment": False}
        taxonomy[tid] = provenance
    require(
        set(species) == {r["species"] for r in review["reported_species_contexts"]}, "paper species scope"
    )
    for accession, entry in entries.items():
        tid = str(entry["organism"]["taxonId"])
        node, provenance = prior.cached_node(root, registry[tid])
        view = prior.prior.members.member_reference(entry, node)
        expected = "Saccharomyces cerevisiae" if accession == "P52923" else "Candida albicans"
        require(
            prior.native_matches(entry, "AIF1")
            and view["reference_taxonomy"]["species"] == species[expected]["identity"],
            "reference gene or independently checked species differs",
        )
        views["UniProtKB:" + accession] = view
        taxonomy[tid] = provenance
    require(set(views) == {"UniProtKB:P52923", "UniProtKB:A0A1D8PI22"}, "reference candidate set changed")
    disagreement = paper_locus_assignment(
        views["UniProtKB:A0A1D8PI22"]["ordered_locus_names"], "orf19.3362", features
    )
    require(disagreement["status"] == "DISTINCT_CGD_FEATURES_WITHHELD", "locus discrepancy changed")
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "inputs": plan["inputs"],
        "records": records,
        "claims": claims,
        "terms": terms,
        "additional_primary_context_term": {"term": "ARO:3009378", "prior_assessment": extra},
        "primary_review": review,
        "paper_species_contexts": species,
        "reference_views": views,
        "reference_queries": sources,
        "taxonomy_sources": taxonomy,
        "cgd_sources": {k: frozen[k] for k in ("cg_mapping", "cg_features")},
        "cgd_features": features,
        "candida_locus_disagreement": disagreement,
        "retained_nomenclature_access_hold": inputs["prior"]["nomenclature_access_hold"],
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(records),
            "source_claims": len(claims),
            "remaining_name_unresolved_terms": len(terms),
            "source_gene_conflict_terms": len(flagged),
            "source_gene_conflict_claims": sum(len(selected[t]["record_memberships"]) for t in flagged),
            "primary_papers_reviewed": 1,
            "primary_pages_visually_reviewed": 6,
            "primary_figures_reviewed": 2,
            "paper_species_grounded": len(species),
            "new_complete_protein_queries": 2,
            "reused_complete_protein_queries": 1,
            "new_reference_entries": 1,
            "reused_name_references": 1,
            "paper_locus_queries_with_zero_results": 1,
            "cached_taxonomy_nodes": len(taxonomy),
            "distinct_cgd_features": len(features),
            "experimental_locus_assignments_withheld": 1,
            "new_qualified_source_term_references": 0,
            "biological_record_writes": 0,
            "whole_record_primary_signoffs": 0,
            "ncbi_requests": 0,
        },
        "limits": [
            "The paper's species context is distinct from correction of the misspelled CARD source name.",
            "A gene-name reference cannot override the paper-locus/CGD discrepancy.",
            "The empty exact-locus query is not an exhaustive alias search or biological absence finding.",
            "Reference strains and proteins are not assigned to "
            "experimental derivatives, alleles or genomes.",
            "Formulation identity, source-name correction and primary claims remain separate curation gates.",
            "No numeric AST, sequences, construction details or genotype specifications are exported.",
            "#1040 remains deferred; no NCBI endpoint, outreach, "
            "source adoption or GitHub mutation occurred.",
            "The full-corpus goal remains OPEN; "
            "the preceding 103-of-178 qualified reference count is unchanged.",
        ],
        "attribution": {
            "CARD_ARO": "CC BY 4.0",
            "UniProt": "CC BY 4.0",
            "CGD": "Reused cited reference crosswalk only; no new source adoption",
            "primary_article": "Cited evidence only; native NC-ND article and renders stay in ignored cache",
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
        require(output.read_text() == payload, "saved name-hold audit differs from offline replay")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
