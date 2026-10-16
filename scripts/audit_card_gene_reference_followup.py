"""Replay bounded species/gene searches without asserting resistant alleles."""

import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_species_gene_context as prior

reference, require, read_json = prior.reference, prior.require, prior.read_json
lineages = prior.members.prior.lineages
PREFIX = "research/2026-10-15-card-gene-reference-followup"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
CANARY, TAXON_PLAN = Path(PREFIX + "-canary.json"), Path(PREFIX + "-taxonomy-plan.json")
SCOPE = "NAMED_GENE_REFERENCE_FOLLOWUP_NOT_EXPERIMENTAL_ALLELES"
QUALIFIED = "MATCHING_SPECIES_NAMED_REFERENCE_NOT_EXPERIMENTAL_ALLELE"
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_card,lit_pubmed_id,sequence_version,version"
)


def native_matches(entry, symbol):
    matches = prior.gene_matches(entry, symbol)
    for i, gene in enumerate(entry.get("genes", [])):
        matches += [
            {"field": f"genes/{i}/orderedLocusNames/{j}", "value": value["value"]}
            for j, value in enumerate(gene.get("orderedLocusNames", []))
            if value["value"].casefold() == symbol.casefold()
        ]
    return matches


def disposition(source, target):
    if target is None:
        return "REFERENCE_WITHOUT_SPECIES_RANK_WITHHELD"
    return QUALIFIED if source == target else "DIFFERENT_SPECIES_REFERENCE_WITHHELD"


def cached_node(root, item):
    url = urlsplit(item["source"]["url"])
    require(
        url.path
        in {"/taxonomy/search", "/taxonomy/" + item["taxon_id"], "/taxonomy/" + item["taxon_id"] + ".json"},
        "not a taxonomy endpoint",
    )
    source = item["source"]
    receipt = read_json(root, source.get("wrapper") or source["receipt"])
    require(
        not {k.lower(): v for k, v in receipt["headers"].items()}.get("location")
        and receipt.get("retries", 0) == receipt.get("redirects_followed", 0) == 0,
        "taxonomy retry or redirect is not reusable",
    )
    payload, provenance = prior.members.screen.read_source(root, item["source"])
    nodes = [n for n in payload.get("results", [payload]) if str(n["taxonId"]) == item["taxon_id"]]
    require(len(nodes) == 1, "missing or duplicate selected taxonomy node")
    lineages.lineage(nodes[0])
    return nodes[0], provenance


def source_bindings(root, plan, inventory):
    result = {}
    require(inventory["ignored_files_included"] is True, "cache inventory omitted ignored files")
    names = {r["tokens"]["species"] for r in plan["terms"].values()}
    require(set(plan["source_names"]) == names, "source name coverage changed")
    for name, resolution in plan["source_names"].items():
        candidates = inventory["name_bindings"].get(name, {})
        require(resolution["candidates"] == candidates, "frozen source candidates changed")
        selected = next(iter(candidates)) if len(candidates) == 1 else None
        require(selected == resolution["selected_taxon_id"], "ambiguous source name selected")
        checked = {}
        for tid, item in candidates.items():
            node, provenance = cached_node(root, item)
            matches = prior.species_name_binding(name, node)
            require(tid == item["taxon_id"] and bool(matches), "unsupported source species name")
            checked[tid] = {
                "identity": lineages.identity(node),
                "native_name_fields": matches,
                "native_source": provenance,
            }
        result[name] = {
            "status": "EXACT_CACHED_SPECIES_NAME"
            if selected
            else "AMBIGUOUS_CACHED_SPECIES_NAMES"
            if candidates
            else "NO_EXACT_CACHED_SPECIES_NAME",
            "candidates": checked,
            "selected": checked.get(selected),
            "biological_absence_inferred": False,
            "experimental_subject_assignment": False,
        }
        require(resolution["status"] == result[name]["status"], "source resolution status changed")
    return result


def query_results(root, plan):
    directory = root / plan["cache_directory"]
    plan_pin = reference.pin(root, root / PLAN)
    inspection = json.loads((root / CANARY).read_bytes())
    require(
        inspection["plan"] == plan_pin
        and plan["canary"] in plan["requests"]
        and inspection["approved_for_remaining_metadata_queries"] is True
        and inspection["experimental_subjects_or_resistant_alleles_assigned"] is False,
        "canary approval changed",
    )
    for suffix in ("attempt", "receipt", "body"):
        require(
            {p.name for p in directory.glob(f"proteins-*-{suffix}.json")}
            == {f"{k}-{suffix}.json" for k in plan["requests"]},
            "unaccounted or missing protein request artifact",
        )
    require(not list(directory.glob("*-error.json")), "failed request remains unresolved")
    expected_names = {n for n, r in plan["source_names"].items() if r["selected_taxon_id"]}
    require(
        len(plan["requests"]) == len(expected_names)
        and {r["source_name"] for r in plan["requests"].values()} == expected_names,
        "query name coverage changed",
    )
    entries, pools, queries = {}, {}, {}
    for key, item in sorted(plan["requests"].items()):
        name, tid = item["source_name"], item["taxon_id"]
        symbols = {
            r["tokens"]["gene"].casefold() for r in plan["terms"].values() if r["tokens"]["species"] == name
        }
        require(
            key == "proteins-" + tid
            and tid == plan["source_names"][name]["selected_taxon_id"]
            and len(item["symbols"]) == len(symbols)
            and {s.casefold() for s in item["symbols"]} == symbols,
            "query taxon or symbol coverage changed",
        )
        params = prior.members.prior.mex.parameters(item["symbols"], tid, True)
        params["fields"] = [FIELDS]
        require(item["parameters"] == {k: v[0] for k, v in params.items()}, "query parameters changed")
        require(
            item["url"].startswith("https://rest.uniprot.org/uniprotkb/search?")
            and parse_qs(urlsplit(item["url"]).query) == params,
            "query URL changed",
        )
        attempt_path = directory / (key + "-attempt.json")
        attempt = json.loads(attempt_path.read_bytes())
        require(
            attempt["plan"] == plan_pin
            and attempt["key"] == key
            and attempt["url"] == item["url"]
            and attempt["retries"] == attempt["redirects_followed"] == 0,
            "request attempt differs from frozen plan",
        )
        receipt_pin = reference.pin(root, directory / (key + "-receipt.json"))
        found, provenance = prior.members.prior.mex.native_query(root, receipt_pin, params)
        require(provenance["url"] == item["url"], "receipt URL differs from attempted URL")
        require(provenance["bytes"] <= plan["max_response_bytes"], "oversized response")
        require(
            all(
                e["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
                and not {"sequence", "features", "comments"} & set(e)
                for e in found.values()
            ),
            "unreviewed or operational payload",
        )
        if key == plan["canary"]:
            require(
                inspection["source"] == receipt_pin and inspection["inspected_count"] == len(found),
                "canary source changed",
            )
        for accession, entry in found.items():
            require(accession not in entries or entries[accession] == entry, "conflicting entry")
            entries[accession] = entry
        pools[name] = sorted(found)
        queries[key] = {
            "source_name": name,
            "attempt": reference.pin(root, attempt_path),
            "native_source": provenance,
            "accessions": ["UniProtKB:" + a for a in sorted(found)],
        }
    return entries, pools, queries


def supplement(root, plan, inventory, needed):
    extra = json.loads((root / TAXON_PLAN).read_bytes())
    require(
        needed - set(inventory["registry"]) == {extra["taxon_id"]} == {"224326"}
        and extra["parent_plan"] == reference.pin(root, root / PLAN),
        "missing taxonomy differs from supplemental plan",
    )
    reference.check_pin(root, extra["protein_receipt"])
    directory = root / plan["cache_directory"]
    attempt_path = directory / "taxonomy-224326-attempt.json"
    receipt_path = directory / "taxonomy-224326-receipt.json"
    attempt, receipt = [json.loads(p.read_bytes()) for p in (attempt_path, receipt_path)]
    require(
        attempt["plan"] == reference.pin(root, root / TAXON_PLAN)
        and attempt["url"]
        == receipt["url"]
        == extra["url"]
        == "https://rest.uniprot.org/taxonomy/224326.json"
        and all(d[k] == 0 for d in (attempt, receipt, extra) for k in ("retries", "redirects_followed"))
        and not receipt["headers"].get("location")
        and receipt["bytes"] <= extra["max_response_bytes"]
        and {p.name for p in directory.glob("taxonomy-*-attempt.json")} == {attempt_path.name}
        and {p.name for p in directory.glob("taxonomy-*-receipt.json")} == {receipt_path.name},
        "unaccounted or changed taxonomy request",
    )
    item = {
        "taxon_id": "224326",
        "source": {"url": extra["url"], "wrapper": reference.pin(root, receipt_path)},
    }
    return item, {
        "plan": reference.pin(root, root / TAXON_PLAN),
        "attempt": reference.pin(root, attempt_path),
        "source": item["source"],
    }


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["reviewed_only"] is True
        and plan["release"] == "2026_03"
        and plan["fields"] == FIELDS
        and plan["retries"] == plan["redirects_followed"] == 0
        and plan["native_match_fields"] == ["geneName", "synonyms", "orderedLocusNames"]
        and plan["constraints"]
        == {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "outreach": False,
            "reuse_terms_review_resumed": False,
            "biological_record_writes": False,
            "experimental_alleles_subjects_or_genomes_assigned": False,
            "operational_details_or_numeric_ast_exported": False,
            "full_corpus_goal_status": "OPEN",
        },
        "planned scope changed",
    )
    checkpoint = read_json(root, plan["prior"])
    read_json(root, plan["prior_verification"])
    selected = {t: r for t, r in checkpoint["terms"].items() if not r["qualified_reference_accessions"]}
    expected = {
        t: {
            "source_label": r["source_label"],
            "tokens": r["parsed_tokens_not_identity_by_themselves"],
            "record_memberships": r["record_memberships"],
        }
        for t, r in selected.items()
    }
    require(plan["terms"] == expected and len(expected) == 161, "complete unresolved cohort changed")
    index, update = [read_json(root, checkpoint["inputs"][k]) for k in ("index", "corpus_update")]
    records, claims = prior.members.current_context(
        root, index, update, set(selected), {t: r["source_label"] for t, r in selected.items()}
    )
    require(records == plan["records"] and claims == plan["claims"], "current claim context changed")
    inventory = read_json(root, plan["taxonomy_cache_inventory"])
    names = source_bindings(root, plan, inventory)
    entries, pools, queries = query_results(root, plan)
    needed = {str(e["organism"]["taxonId"]) for e in entries.values()}
    extra, extra_provenance = supplement(root, plan, inventory, needed)
    registry = {**inventory["registry"], extra["taxon_id"]: extra}
    taxa, sources = {}, {}
    for tid in sorted(needed):
        taxa[tid], sources[tid] = cached_node(root, registry[tid])
    views = {
        "UniProtKB:" + a: prior.members.member_reference(e, taxa[str(e["organism"]["taxonId"])])
        for a, e in sorted(entries.items())
    }
    terms = {}
    for term, row in selected.items():
        tokens = row["parsed_tokens_not_identity_by_themselves"]
        name, symbol = tokens["species"], tokens["gene"]
        source = names[name]["selected"]
        candidates = []
        for accession in pools.get(name, []):
            matches = native_matches(entries[accession], symbol)
            if not matches:
                continue
            view = views["UniProtKB:" + accession]
            status = disposition(source["identity"], view["reference_taxonomy"]["species"])
            bibliography = {
                "PMID:" + i["id"]
                for b in view["native_bibliography"]
                for i in b["identifiers"]
                if i["database"] == "PubMed"
            }
            candidates.append(
                {
                    "protein_accession": "UniProtKB:" + accession,
                    "literal_native_fields": matches,
                    "match_kind": "GENE_SYMBOL_OR_SYNONYM"
                    if prior.gene_matches(entries[accession], symbol)
                    else "ORDERED_LOCUS_REFERENCE_NOT_GENE_RENAMING",
                    "own_definition_citation_overlap": sorted(
                        bibliography & set(row["definition_citations"])
                    ),
                    "citation_overlap_is_primary_validation": False,
                    "disposition": status,
                    "qualified_reference": status == QUALIFIED,
                    "experimental_subject_assignment": False,
                    "exact_allele_assignment": False,
                }
            )
        qualified = [c["protein_accession"] for c in candidates if c["qualified_reference"]]
        terms[term] = {
            **plan["terms"][term],
            "definition_citations": row["definition_citations"],
            "prior_status": row["status"],
            "reference_candidates": candidates,
            "qualified_reference_accessions": qualified,
            "status": "QUALIFIED_NAMED_REFERENCE_PRIMARY_REVIEW_OPEN"
            if qualified
            else "SOURCE_NAME_UNRESOLVED_NOT_QUERIED"
            if source is None
            else "EXACT_FIELDS_WITHHELD_FOR_TAXONOMY"
            if candidates
            else "NO_EXACT_FIELD_MATCH_IN_BOUNDED_REVIEWED_QUERY_NOT_BIOLOGICAL_ABSENCE",
            "whole_record_primary_review": "OPEN",
            "biological_absence_inferred": False,
        }
    qualified_terms = {t for t, r in terms.items() if r["qualified_reference_accessions"]}
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "prior": plan["prior"],
        "canary": reference.pin(root, root / CANARY),
        "records": records,
        "claims": claims,
        "terms": terms,
        "source_names": names,
        "queries": queries,
        "reference_views": views,
        "taxonomy_sources": sources,
        "supplemental_taxonomy_request": extra_provenance,
        "summary": {
            "selected_terms": len(terms),
            "source_claims": len(claims),
            "complete_records_read": len(records),
            "corpus_records_hash_checked": 2939,
            "source_names": len(names),
            "resolved_source_names": len(pools),
            "unresolved_source_names": len(names) - len(pools),
            "native_protein_queries": len(queries),
            "zero_hit_queries": sum(not p for p in pools.values()),
            "native_reference_entries": len(entries),
            "verified_reference_taxa": len(taxa),
            "qualified_reference_terms": len(qualified_terms),
            "qualified_reference_links": sum(
                len(r["qualified_reference_accessions"]) for r in terms.values()
            ),
            "qualified_reference_claim_memberships": sum(c["aro_id"] in qualified_terms for c in claims),
            "qualified_reference_record_memberships": len(
                {c["record_identifier"] for c in claims if c["aro_id"] in qualified_terms}
            ),
            "term_statuses": dict(sorted(Counter(r["status"] for r in terms.values()).items())),
            "new_uniprot_taxonomy_requests": 1,
            "ncbi_requests": 0,
        },
        "limits": {
            **plan["constraints"],
            "prior_index_rewritten": False,
            "new_primary_reviews": 0,
            "whole_record_primary_signoffs": 0,
            "reviewed_status_proves_resistance": False,
            "search_is_exhaustive_for_unreviewed_entries_strains_or_alleles": False,
            "ordered_locus_matches_are_gene_symbols": False,
        },
        "attribution": (
            "CARD/ARO and UniProt CC BY 4.0; database reference metadata, not new primary evidence."
        ),
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
