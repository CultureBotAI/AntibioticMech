"""Replay explicit identifier leads without promoting references to tested alleles."""

import argparse
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_name_holds as holds

aliases, prior, mex = holds.aliases, holds.prior, holds.mex
reference, require, read_json = holds.reference, holds.require, holds.read_json
PREFIX = "research/2026-10-15-card-explicit-identifiers"
PLAN, OUTPUT = Path(PREFIX + "-audit-plan.json"), Path(PREFIX + ".json")
SCOPE = "EXPLICIT_IDENTIFIER_REFERENCE_AUDIT_NOT_EXPERIMENTAL_ALLELES"
ACTIVE = {"UniProtKB reviewed (Swiss-Prot)", "UniProtKB unreviewed (TrEMBL)"}
TERMS = {"ARO:3004578", "ARO:3004977"}
FIELDS = prior.FIELDS + ",xref_cgd"


def inactive_reference(entry):
    require(entry["entryType"] == "Inactive", "entry is not inactive")
    require(not {"sequence", "features", "comments"} & set(entry), "unexpected operational data")
    return {
        "protein_accession": "UniProtKB:" + entry["primaryAccession"],
        "entry_type": entry["entryType"],
        "native_inactive_reason": entry.get("inactiveReason"),
        "native_secondary_accessions": entry.get("secondaryAccessions", []),
        "status": "INACTIVE_ACCESSION_WITHHELD_FROM_ACTIVE_REFERENCE_ASSIGNMENT",
        "qualified_reference": False,
        "organism_inferred_from_source_label": False,
        "replacement_accession_inferred": False,
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
        "biological_absence_inferred": False,
    }


def locus_alias_matches(entry, values):
    result = []
    # ORF labels remain a distinct namespace, not silently renamed gene symbols.
    for value in values:
        native = prior.native_matches(entry, value)
        native += [
            {"field": f"genes/{i}/orfNames/{j}", "value": field["value"]}
            for i, gene in enumerate(entry.get("genes", []))
            for j, field in enumerate(gene.get("orfNames", []))
            if field["value"].casefold() == value.casefold()
        ]
        if native:
            result.append({"source_alias": value, "native_fields": native})
    return result


def source_candidate(entry, leads, source_species, reference_species, source_gene):
    require(entry["entryType"] in ACTIVE | {"Inactive"}, "unknown entry state")
    matches = [
        {"source_alias": a, "native_fields": fields}
        for a in leads
        if (fields := aliases.alias_matches(entry, a))
    ]
    if entry["entryType"] == "Inactive":
        status = "INACTIVE_ACCESSION_WITHHELD"
    elif not matches:
        status = "QUERY_MEMBERSHIP_WITHOUT_NATIVE_IDENTIFIER_MATCH_WITHHELD"
    else:
        status = aliases.reference_status(source_species, reference_species)
    return {
        "protein_accession": "UniProtKB:" + entry["primaryAccession"],
        "alias_matches": matches,
        "native_source_gene_name_matches": prior.prior.gene_matches(entry, source_gene),
        "disposition": status,
        "qualified_reference": status == aliases.QUALIFIED,
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
        "primary_resistance_validation": False,
    }


def cgd_candidate(entry, feature, species, expected_species, values):
    require(entry["entryType"] in ACTIVE, "inactive entry cannot be a CGD protein reference")
    matches = locus_alias_matches(entry, values)
    cgd = [x for x in entry.get("uniProtKBCrossReferences", []) if x["database"] == "CGD"]
    ids = {x["id"] for x in cgd}
    same_species = species == expected_species
    if not same_species:
        status = "SPECIES_UNRESOLVED_OR_DIFFERENT_WITHHELD"
    elif not matches:
        status = "NO_EXACT_NATIVE_ALIAS_WITHHELD"
    elif ids and ids != {feature["cgd_id"]}:
        status = "CONFLICTING_CGD_FEATURE_WITHHELD"
    elif ids == {feature["cgd_id"]}:
        status = "SAME_CGD_FEATURE_REFERENCE_NOT_EXPERIMENTAL_HAPLOTYPE"
    else:
        status = "CGD_ALIAS_ONLY_REFERENCE_NOT_PAPER_SUBJECT"
    return {
        "protein_accession": "UniProtKB:" + entry["primaryAccession"],
        "native_alias_matches": matches,
        "native_cgd_cross_references": cgd,
        "same_species": same_species,
        "status": status,
        "same_cgd_feature_verified": status == "SAME_CGD_FEATURE_REFERENCE_NOT_EXPERIMENTAL_HAPLOTYPE",
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
        "experimental_haplotype_assignment": False,
        "experimental_genome_assignment": None,
        "primary_resistance_validation": False,
    }


def expected_queries(frozen):
    accessions = frozen["source_accession_leads"]
    require(accessions == ["A0A225SC95", "Q2FD57"], "source accession leads changed")
    require(frozen["source_locus_lead"] == "Rv2783c", "source locus changed")
    return {
        "source-accessions": "("
        + " OR ".join(clause for a in accessions for clause in ("accession:" + a, "sec_acc:" + a))
        + ")",
        "source-locus": "gene_exact:Rv2783c AND taxonomy_id:1773 AND reviewed:true",
        "cgd-paper-locus-aliases": "("
        + " OR ".join("gene_exact:" + a for a in frozen["cgd_query_aliases"])
        + ") AND taxonomy_id:5476",
    }


def check_request_history(directory, query_keys):
    keys = set(query_keys) | {"taxonomy-294748"}
    for suffix in ("attempt", "receipt"):
        require(
            set(directory.glob(f"*-{suffix}.json")) == {directory / f"{key}-{suffix}.json" for key in keys},
            "unaccounted or missing request artifact",
        )
    require(
        set(directory.glob("*-body.json")) == {directory / f"{key}-body.json" for key in query_keys}
        and not list(directory.glob("*-error.json")),
        "unaccounted body or request failure",
    )


def check_entry_scope(key, entries):
    require(all(e["entryType"] in ACTIVE | {"Inactive"} for e in entries.values()), "unknown entry state")
    if key == "source-locus":
        require(
            all(e["entryType"] == "UniProtKB reviewed (Swiss-Prot)" for e in entries.values()),
            "reviewed-only query returned a non-reviewed entry",
        )


def protein_queries(root, plan, inputs):
    frozen = inputs["protein_plan"]
    require(
        frozen["scope"] == "EXPLICIT_IDENTIFIER_REFERENCE_FOLLOWUP_NOT_EXPERIMENTAL_ALLELES"
        and frozen["fields"] == FIELDS
        and frozen["release"] == "2026_03"
        and frozen["canary"] == "source-accessions"
        and frozen["constraints"]
        == {
            "biological_record_writes": False,
            "experimental_identity_assignments": False,
            "full_corpus_goal_status": "OPEN",
            "issue_1040": "DEFERRED",
            "ncbi_requests": 0,
            "new_primary_reviews": 0,
            "redirects_followed": 0,
            "retries": 0,
        },
        "protein query scope changed",
    )
    preflight = read_json(root, frozen["preflight"])
    require(
        preflight["ignored_files_included"] is True and not preflight["existing_matching_requests"],
        "request preflight changed",
    )
    directory = root / plan["cache_directory"]
    expected = expected_queries(frozen)
    require(set(expected) == set(frozen["requests"]) == set(plan["protein_receipts"]), "query set changed")
    check_request_history(directory, expected)
    pools, sources = {}, {}
    for key, query in expected.items():
        item = frozen["requests"][key]
        params = {"query": query, "format": "json", "size": "500", "sort": "accession asc", "fields": FIELDS}
        require(item["parameters"] == params and item["query"] == query, "planned query changed")
        require(
            parse_qs(urlsplit(item["url"]).query) == {k: [v] for k, v in params.items()}, "query URL changed"
        )
        attempt_path = directory / (key + "-attempt.json")
        attempt = json.loads(attempt_path.read_bytes())
        require(
            attempt["plan_sha256"] == plan["inputs"]["protein_plan"]["sha256"]
            and attempt["key"] == key
            and attempt["url"] == item["url"],
            "attempt binding changed",
        )
        found, source = mex.native_query(
            root, plan["protein_receipts"][key], {k: [v] for k, v in params.items()}
        )
        require(
            all(source[k] == v for k, v in attempt.items()) and source["bytes"] <= frozen["max_bytes"],
            "attempt differs from receipt or exceeds bound",
        )
        require(
            all(not {"sequence", "features", "comments"} & set(e) for e in found.values()),
            "unexpected operational metadata",
        )
        check_entry_scope(key, found)
        pools[key], sources[key] = (
            found,
            {
                "attempt": reference.pin(root, attempt_path),
                "native_source": source,
                "result_count": len(found),
            },
        )
    canary = inputs["protein_canary"]
    require(
        canary["plan_sha256"] == plan["inputs"]["protein_plan"]["sha256"]
        and canary["receipt"] == plan["protein_receipts"]["source-accessions"]
        and canary["approved_for_remaining_queries"] is True
        and canary["active_reference_assignments"] == canary["source_species_assignments"] == 0
        and canary["replacement_accessions_inferred"] is False,
        "canary scope changed",
    )
    require(sorted(pools["source-accessions"]) == canary["primary_accessions"], "canary entries changed")
    for entry in pools["source-accessions"].values():
        require(
            entry["entryType"] == canary["native_entry_type"] == "Inactive"
            and entry["inactiveReason"]
            == {
                "inactiveReasonType": canary["native_inactive_reason"],
                "deletedReason": canary["native_deleted_reason"],
            },
            "inspected inactive state changed",
        )
    for key in expected.keys() - {"source-accessions"}:
        require(
            sources[key]["native_source"]["started_at"]
            > sources["source-accessions"]["native_source"]["retrieved_at"],
            "remaining query preceded canary response",
        )
    old = preflight["previous_exact_candida_paper_locus_query_reused"]
    old_params = {
        "query": ["gene_exact:orf19.3362 AND taxonomy_id:5476"],
        "format": ["json"],
        "size": ["500"],
        "sort": ["accession asc"],
        "fields": [prior.FIELDS],
    }
    old_entries, old_source = mex.native_query(root, old["native_source"]["receipt"], old_params)
    require(not old_entries and old_source == old["native_source"], "reused exact-locus result changed")
    reference.check_pin(root, old["attempt"])
    return pools, sources, old


def taxonomy_context(root, plan, inputs, pools):
    registry = dict(inputs["taxonomy_inventory"]["registry"])
    require("294748" not in registry, "new taxonomy was already registered")
    frozen = inputs["taxonomy_plan"]
    require(
        frozen["url"] == "https://rest.uniprot.org/taxonomy/294748.json"
        and frozen["taxon_id"] == "294748"
        and frozen["single_request_is_canary"] is True
        and frozen["ncbi_requests"] == frozen["retries"] == frozen["redirects_followed"] == 0
        and frozen["protein_query_receipt"] == plan["protein_receipts"]["cgd-paper-locus-aliases"],
        "new taxonomy plan changed",
    )
    item = plan["new_taxonomy"]
    require(
        item["taxon_id"] == "294748" and item["source"]["url"] == frozen["url"], "taxonomy identity changed"
    )
    receipt = read_json(root, item["source"]["wrapper"])
    attempt_path = root / plan["cache_directory"] / "taxonomy-294748-attempt.json"
    attempt = json.loads(attempt_path.read_bytes())
    require(
        all(receipt[k] == v for k, v in attempt.items())
        and attempt["plan_sha256"] == plan["inputs"]["taxonomy_plan"]["sha256"]
        and receipt["bytes"] <= frozen["max_bytes"],
        "taxonomy attempt differs from frozen plan",
    )
    registry["294748"] = item
    tids = {"470", "1773", "5476"} | {
        str(e["organism"]["taxonId"])
        for pool in pools.values()
        for e in pool.values()
        if e["entryType"] in ACTIVE
    }
    nodes, sources = {}, {}
    for tid in sorted(tids):
        nodes[tid], sources[tid] = prior.cached_node(root, registry[tid])
    require(
        nodes["294748"]["rank"] == "strain"
        and nodes["294748"]["scientificName"] == "Candida albicans (strain WO-1)",
        "inspected new taxonomy differs",
    )
    return nodes, sources, reference.pin(root, attempt_path)


def coverage(root, plan, terms):
    sources = {k: read_json(root, p) for k, p in plan["coverage_inputs"].items()}
    cohort = set(sources["card-species-gene-context"]["terms"])
    previous = set()
    for dossier in sources.values():
        qualified = {t for t, row in dossier["terms"].items() if row["qualified_reference_accessions"]}
        require(qualified <= cohort and not previous & qualified, "overlapping or out-of-cohort baseline")
        previous |= qualified
    added = {t for t, row in terms.items() if row["qualified_reference_accessions"]}
    require(
        len(cohort) == 178 and len(previous) == 103 and not added & previous and added <= cohort,
        "prior coverage or increment changed",
    )
    return {
        "cohort_terms": len(cohort),
        "previous_qualified_terms": sorted(previous),
        "new_qualified_terms": sorted(added),
        "qualified_terms": sorted(previous | added),
        "remaining_terms": sorted(cohort - previous - added),
        "whole_corpus_completion": False,
    }


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["constraints"]
        == {
            "biological_record_writes": False,
            "experimental_identity_assignments": False,
            "new_primary_reviews": 0,
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "full_corpus_goal_status": "OPEN",
        },
        "audit scope changed",
    )
    for item in plan["inputs"].values():
        reference.check_pin(root, item)
    inputs = {k: read_json(root, p) for k, p in plan["inputs"].items() if k != "source_queue"}
    require(
        inputs["previous_verification"]["artifacts"]["dossier"] == plan["inputs"]["name_holds"],
        "previous verification binding changed",
    )
    old = inputs["source_aliases"]
    selected = {
        t: {
            **old["terms"][t],
            "definition_citations": old["terms"][t]["definition_annotation"]["definition_citation_ids"],
        }
        for t in TERMS
    }
    require(
        all(not r["qualified_reference_accessions"] for r in selected.values()),
        "selected term already qualified",
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
    leads = {
        t: [{k: a[k] for k in ("kind", "value")} for a in r["selected_alias_leads"]]
        for t, r in selected.items()
    }
    annotations = aliases.annotation_context(graph, selected, inputs["definitions"], leads)
    frozen = inputs["protein_plan"]
    require(
        leads
        == {
            "ARO:3004578": [
                {"kind": "ACCESSION_LIKE_SYNONYM", "value": a} for a in frozen["source_accession_leads"]
            ],
            "ARO:3004977": [{"kind": "ORDERED_LOCUS", "value": frozen["source_locus_lead"]}],
        },
        "source leads changed",
    )
    prior_holds = inputs["name_holds"]
    cgd_sources = prior_holds["cgd_sources"]
    features = holds.cgd_loci(
        read_json(root, cgd_sources["cg_mapping"]), read_json(root, cgd_sources["cg_features"])
    )
    feature = features["orf19.3362"]
    values = sorted(
        ({feature["feature"]} | set(feature["feature_aliases"])) - {"orf19.3362", "AIF1", "orf19.9721"}
    )
    require(
        frozen["cgd_feature"] == feature
        and frozen["cgd_query_aliases"] == values
        and frozen["cgd_allelic_aliases_do_not_assign_haplotype"] is True,
        "CGD alias scope changed",
    )
    pools, queries, reused = protein_queries(root, plan, inputs)
    nodes, tax_sources, tax_attempt = taxonomy_context(root, plan, inputs, pools)
    bindings = {}
    for row in selected.values():
        name = row["tokens"]["species"]
        binding = old["source_bindings"][name]
        node = nodes[str(binding["identity"]["taxonId"])]
        require(
            prior.lineages.identity(node) == binding["identity"]
            and prior.prior.species_name_binding(name, node) == binding["native_name_fields"],
            "source species changed",
        )
        bindings[name] = binding
    views, inactive = {}, {}
    for pool in pools.values():
        for accession, entry in pool.items():
            if entry["entryType"] == "Inactive":
                inactive[accession] = inactive_reference(entry)
            else:
                view = prior.prior.members.member_reference(entry, nodes[str(entry["organism"]["taxonId"])])
                require(accession not in views or views[accession] == view, "conflicting reference entry")
                views[accession] = view
    terms = {}
    for term, row in sorted(selected.items()):
        key = "source-accessions" if term == "ARO:3004578" else "source-locus"
        candidates = []
        for accession, entry in pools[key].items():
            species = views[accession]["reference_taxonomy"]["species"] if accession in views else None
            candidates.append(
                source_candidate(
                    entry,
                    annotations[term]["selected_alias_leads"],
                    bindings[row["tokens"]["species"]]["identity"],
                    species,
                    row["tokens"]["gene"],
                )
            )
        terms[term] = {
            "source_label": row["source_label"],
            "tokens": row["tokens"],
            "record_memberships": row["record_memberships"],
            "source_annotations": annotations[term],
            "query_key": key,
            "reference_candidates": candidates,
            "qualified_reference_accessions": [
                r["protein_accession"] for r in candidates if r["qualified_reference"]
            ],
            "biological_absence_inferred": False,
            "whole_record_primary_review": "OPEN",
        }
    expected_species = prior.lineages.identity(nodes["5476"])
    require(
        expected_species["rank"] == "species" and expected_species["scientificName"] == "Candida albicans",
        "Candida species changed",
    )
    candida = [
        cgd_candidate(e, feature, views[a]["reference_taxonomy"]["species"], expected_species, values)
        for a, e in pools["cgd-paper-locus-aliases"].items()
    ]
    disagreement = holds.paper_locus_assignment(
        prior_holds["reference_views"]["UniProtKB:A0A1D8PI22"]["ordered_locus_names"], "orf19.3362", features
    )
    require(disagreement == prior_holds["candida_locus_disagreement"], "prior locus conflict changed")
    combined = coverage(root, plan, terms)
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "inputs": plan["inputs"],
        "records": records,
        "claims": claims,
        "terms": terms,
        "source_bindings": bindings,
        "reference_queries": queries,
        "reused_exact_locus_query": reused,
        "reference_views": views,
        "inactive_accessions": inactive,
        "taxonomy_sources": tax_sources,
        "new_taxonomy_attempt": tax_attempt,
        "cgd_sources": cgd_sources,
        "cgd_features": features,
        "cgd_alias_candidates": candida,
        "retained_name_only_reference_disagreement": disagreement,
        "additional_context_term": {
            "term": "ARO:3009378",
            "prior_reference_accessions": extra["qualified_reference_accessions"],
            "additional_qualified_card_terms": 0,
            "experimental_protein_assignment": False,
        },
        "coverage": combined,
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(records),
            "source_claims": len(claims),
            "source_terms_followed": len(terms),
            "new_complete_protein_queries": len(queries),
            "reused_complete_queries": 1,
            "inactive_accessions": len(inactive),
            "active_reference_entries": len(views),
            "new_qualified_source_terms": len(combined["new_qualified_terms"]),
            "same_cgd_feature_references": sum(c["same_cgd_feature_verified"] for c in candida),
            "cgd_alias_only_references": sum(
                c["status"] == "CGD_ALIAS_ONLY_REFERENCE_NOT_PAPER_SUBJECT" for c in candida
            ),
            "taxonomy_nodes": len(nodes),
            "new_taxonomy_queries": 1,
            "combined_qualified_terms": len(combined["qualified_terms"]),
            "combined_remaining_terms": len(combined["remaining_terms"]),
            "new_primary_reviews": 0,
            "biological_record_writes": 0,
            "experimental_identity_assignments": 0,
            "ncbi_requests": 0,
        },
        "limits": [
            "Deleted accessions are not active reference assignments, "
            "proof of biological absence or inferred replacement identifiers.",
            "The source-locus query is reviewed-only; its pnp gene label "
            "does not silently rename source gpsI or validate a resistant allele.",
            "CGD feature identity supports reference context only; "
            "allelic and cross-strain aliases do not assign experimental haplotypes.",
            "The earlier same-name protein remains a distinct CGD feature, "
            "not an interchangeable paper-locus reference.",
            "The primary paper's formulation, experimental strain and allele limits "
            "remain unchanged; no new primary review was performed.",
            "No sequences, variant specifications, numeric AST or construction details are exported.",
            "No NCBI endpoint, outreach, source adoption or GitHub mutation; #1040 remains deferred.",
            "The 178-term cohort is not the full corpus; the active investigation remains OPEN.",
        ],
        "attribution": {
            "CARD_ARO": "CC BY 4.0",
            "UniProt": "CC BY 4.0",
            "CGD": "Cited reference crosswalk only; no new source adoption",
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
        require(output.read_text() == payload, "saved explicit identifier audit differs from offline replay")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
