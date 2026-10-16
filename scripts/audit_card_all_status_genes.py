"""Replay complete reviewed/unreviewed gene searches as reference metadata only."""

import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlsplit

import audit_card_gene_reference_followup as prior
import audit_card_grounding as card

reference, require, read_json = prior.reference, prior.require, prior.read_json
PREFIX = "research/2026-10-15-card-all-status-gene-references"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
CANARY = Path(PREFIX + "-canary.json")
SCOPE = "ALL_ENTRY_STATUS_NAMED_REFERENCES_NOT_EXPERIMENTAL_ALLELES"
ENTRY_TYPES = {"UniProtKB reviewed (Swiss-Prot)", "UniProtKB unreviewed (TrEMBL)"}


def page_url(item, parameters, page):
    return item["url"] if page == 1 else "https://rest.uniprot.org/uniprotkb/search?" + urlencode(parameters)


def read_page(root, plan, key, page, parameters, seen_count, total, last_accession):
    item = plan["requests"][key]
    prefix = root / plan["cache_directory"] / f"{key}-page-{page:04d}"
    attempt_path, receipt_path = [Path(str(prefix) + f"-{kind}.json") for kind in ("attempt", "receipt")]
    attempt, receipt = [json.loads(p.read_bytes()) for p in (attempt_path, receipt_path)]
    url = page_url(item, parameters, page)
    parsed = urlsplit(url)
    require(
        parsed.scheme == "https"
        and parsed.netloc == "rest.uniprot.org"
        and parsed.path == "/uniprotkb/search"
        and not parsed.fragment
        and parse_qs(parsed.query, keep_blank_values=True) == {k: [v] for k, v in parameters.items()}
        and attempt["plan"] == reference.pin(root, root / PLAN)
        and attempt["key"] == key
        and attempt["page"] == page
        and attempt["url"] == receipt["url"] == url
        and all(d[k] == 0 for d in (attempt, receipt) for k in ("retries", "redirects_followed"))
        and receipt["status"] == 200,
        "page request identity or status differs from plan",
    )
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    count = int(headers["x-total-results"])
    require(
        headers["x-uniprot-release"] == plan["release"] == "2026_03"
        and not headers.get("location")
        and 0 <= count <= plan["max_results_per_query"]
        and (total is None or total == count),
        "page release, size limit, redirect or total changed",
    )
    body = reference.check_pin(root, receipt["body"])
    require(
        body == Path(str(prefix) + "-body.json")
        and body.stat().st_size == receipt["bytes"] <= plan["max_response_bytes"],
        "page body identity or length changed",
    )
    rows = json.loads(body.read_bytes())["results"]
    require(
        isinstance(rows, list) and len(rows) == min(plan["page_size"], max(count - seen_count, 0)),
        "page cardinality differs from query total",
    )
    for entry in rows:
        accession = entry["primaryAccession"]
        require(
            isinstance(accession, str)
            and bool(accession)
            and (last_accession is None or accession > last_accession)
            and entry["entryType"] in ENTRY_TYPES
            and not {"sequence", "features", "comments"} & set(entry),
            "duplicate, unordered, untyped or operational protein entry",
        )
        last_accession = accession
    next_parameters = card.next_page(headers.get("link", ""), item["parameters"])
    require(
        (next_parameters is None) == (seen_count + len(rows) == count),
        "pagination termination differs from query total",
    )
    return (
        rows,
        next_parameters,
        count,
        {
            "page": page,
            "attempt": reference.pin(root, attempt_path),
            "receipt": reference.pin(root, receipt_path),
            "body": receipt["body"],
            "url": url,
            "retrieved_at": receipt["retrieved_at"],
            "status": 200,
        },
    )


def read_chain(root, plan, key):
    parameters = plan["requests"][key]["parameters"]
    entries, pages, visited = {}, [], set()
    total, last = None, None
    while parameters is not None:
        page = len(pages) + 1
        fingerprint = json.dumps(parameters, sort_keys=True)
        require(
            page <= plan["max_pages_per_query"] and fingerprint not in visited, "page limit or cursor cycle"
        )
        visited.add(fingerprint)
        rows, parameters, total, provenance = read_page(
            root, plan, key, page, parameters, len(entries), total, last
        )
        for row in rows:
            entries[row["primaryAccession"]] = row
            last = row["primaryAccession"]
        pages.append(provenance)
    directory = root / plan["cache_directory"]
    used = {root / p[k]["path"] for p in pages for k in ("attempt", "receipt", "body")}
    require(
        set(directory.glob(f"{key}-page-*.json")) == used and not list(directory.glob(f"{key}-error.json")),
        "orphaned page or failed query",
    )
    return entries, {
        "query": plan["requests"][key]["parameters"]["query"],
        "pages": pages,
        "result_count": total,
        "release": plan["release"],
        "complete_for_query": True,
        "entry_type_counts": dict(sorted(Counter(e["entryType"] for e in entries.values()).items())),
        "empty_result_means_biological_absence": False,
    }


def current_selection(root, plan):
    checkpoint = read_json(root, plan["prior"])
    names = read_json(root, plan["name_followup"])
    require(names["prior"] == plan["prior"], "name follow-up belongs to another checkpoint")
    for pin in plan["prior_verifications"]:
        read_json(root, pin)
    selected, held, bindings = {}, {}, {}
    for term, row in checkpoint["terms"].items():
        if row["qualified_reference_accessions"]:
            continue
        name = row["tokens"]["species"]
        source = checkpoint["source_names"][name]["selected"]
        if source:
            identity, provenance = source["identity"], source["native_source"]
            fields = source["native_name_fields"]
        else:
            resolved = names["names"][name]["selected_reference_species"]
            if not resolved:
                held[term] = {
                    "source_label": row["source_label"],
                    "tokens": row["tokens"],
                    "reason": names["names"][name]["status"],
                    "record_memberships": row["record_memberships"],
                }
                continue
            identity, provenance = resolved["identity"], names["native_sources"][name]
            fields = resolved["exact_name_fields"]
        selected[term] = row
        bindings[name] = {"identity": identity, "native_source": provenance, "native_name_fields": fields}
    require(
        selected == plan["terms"]
        and held == plan["name_unresolved_terms"]
        and bindings == plan["source_bindings"]
        and len(selected) == 54
        and len(held) == 36,
        "complete remaining-term partition changed",
    )
    for name, binding in bindings.items():
        node, _ = prior.cached_node(
            root, {"taxon_id": str(binding["identity"]["taxonId"]), "source": binding["native_source"]}
        )
        require(
            prior.lineages.identity(node) == binding["identity"]
            and prior.prior.species_name_binding(name, node) == binding["native_name_fields"],
            "source name is not supported by native taxonomy",
        )
    ancestor = read_json(root, checkpoint["prior"])
    index, update = [read_json(root, ancestor["inputs"][k]) for k in ("index", "corpus_update")]
    records, claims = prior.prior.members.current_context(
        root, index, update, set(selected), {t: r["source_label"] for t, r in selected.items()}
    )
    require(records == plan["records"] and claims == plan["claims"], "current claim bindings changed")
    return selected, held, records, claims


def reused_query(root, item):
    params = item["native_parameters"]
    require(
        item["taxon_id"] == "5478"
        and item["symbols"] == ["yor1"]
        and item["source_name"] == "Candida glabrata"
        and item["scope"] == "COMPLETE_CACHED_QUERY_SUPERSET_INCLUDING_YOR1_AND_AN_ORDERED_LOCUS"
        and params
        == {
            "query": "(gene_exact:YOR1 OR gene_exact:CAGL0G00242g) AND taxonomy_id:5478",
            "format": "json",
            "size": "500",
            "sort": "accession asc",
            "fields": prior.FIELDS.replace("xref_card", "xref_card,xref_embl"),
        }
        and parse_qs(urlsplit(item["source"]["url"]).query) == {k: [v] for k, v in params.items()},
        "cached query is not the inspected full superset",
    )
    receipt = read_json(root, item["source"]["receipt"])
    require(
        not {k.lower(): v for k, v in receipt["headers"].items()}.get("location")
        and receipt.get("retries", 0) == 0
        and not receipt.get("retry_performed", False)
        and not receipt.get("redirects_followed", False),
        "cached query retry or redirect",
    )
    payload, provenance = prior.prior.members.screen.read_source(root, item["source"])
    entries = payload["results"]
    require(
        len(entries) == 1
        and entries[0]["primaryAccession"] == "Q6FTR9"
        and entries[0]["entryType"] in ENTRY_TYPES
        and not {"sequence", "features", "comments"} & set(entries[0]),
        "cached reference metadata changed",
    )
    return {e["primaryAccession"]: e for e in entries}, {
        "native_source": provenance,
        "result_count": len(entries),
        "complete_for_query": True,
        "reused": True,
    }


def query_results(root, plan):
    require(
        not set(plan["requests"]) & set(plan["reused_queries"])
        and len(plan["requests"]) == 31
        and set(plan["reused_queries"]) == {"proteins-5478"},
        "new and reused query partition changed",
    )
    all_queries = {**plan["requests"], **plan["reused_queries"]}
    require(
        len(all_queries) == len(plan["source_bindings"]) == 32
        and {q["source_name"] for q in all_queries.values()} == set(plan["source_bindings"]),
        "species query coverage changed",
    )
    preflight = read_json(root, plan["prior_query_preflight"])
    require(
        preflight["ignored_files_included"] is True
        and not preflight["failed_or_unresolved_attempts_retried"]
        and not preflight["all_status_queries_repeated"],
        "prior source holds not preserved",
    )
    history = preflight["related_query_history"]
    success = {r["url"] for r in history if r["status"] == 200}
    for row in history:
        reference.check_pin(root, row["file"])
        require(
            row["status"] == 200 or (row["status"] is None and row["url"] in success),
            "unresolved prior source request",
        )
    inspection = json.loads((root / CANARY).read_bytes())
    require(
        plan["canary"] in plan["requests"]
        and inspection["plan"] == reference.pin(root, root / PLAN)
        and inspection["approved_for_remaining_queries"] is True
        and inspection["experimental_identity_assignments"] is False,
        "missing or changed canary approval",
    )
    entries, pools, queries = {}, {}, {}
    for key, item in sorted(all_queries.items()):
        name, tid = item["source_name"], item["taxon_id"]
        symbols = sorted(
            {r["tokens"]["gene"].casefold() for r in plan["terms"].values() if r["tokens"]["species"] == name}
        )
        params = {
            "query": "(" + " OR ".join("gene_exact:" + s for s in symbols) + ") AND taxonomy_id:" + tid,
            "format": "json",
            "size": "500",
            "sort": "accession asc",
            "fields": prior.FIELDS,
        }
        require(
            item["symbols"] == symbols
            and key == "proteins-" + tid
            and int(tid) == plan["source_bindings"][name]["identity"]["taxonId"]
            and item["parameters"] == params,
            "query symbol, species or status scope changed",
        )
        if key in plan["requests"]:
            found, queries[key] = read_chain(root, plan, key)
        else:
            found, queries[key] = reused_query(root, item)
        if key == plan["canary"]:
            require(inspection["query"] == queries[key], "canary chain changed")
        pools[name] = sorted(found)
        for accession, entry in found.items():
            require(accession not in entries or entries[accession] == entry, "conflicting reference metadata")
            entries[accession] = entry
    used = {
        root / p[k]["path"]
        for key, q in queries.items()
        if key in plan["requests"]
        for p in q["pages"]
        for k in ("attempt", "receipt", "body")
    }
    directory = root / plan["cache_directory"]
    require(
        set(directory.glob("proteins-*-page-*.json")) == used and not list(directory.glob("*-error.json")),
        "unaccounted or failed query",
    )
    return entries, pools, queries


def reference_taxonomy(root, plan, entries, queries):
    path = root / (PREFIX + "-taxonomy-plan.json")
    frozen = json.loads(path.read_bytes())
    needed = sorted({str(e["organism"]["taxonId"]) for e in entries.values()})
    inventory = read_json(root, frozen["taxonomy_cache_inventory"])
    cached = {t: inventory["registry"][t] for t in needed if t in inventory["registry"]}
    require(
        frozen["parent_plan"] == reference.pin(root, root / PLAN)
        and frozen["queries"] == queries
        and frozen["reference_accessions"] == sorted(entries)
        and frozen["reference_taxa"] == needed
        and frozen["cached_taxonomy"] == cached
        and frozen["missing_taxonomy"] == sorted(set(needed) - set(cached)) == ["1399146"],
        "taxonomy plan does not cover exact native references",
    )
    directory = root / plan["cache_directory"]
    attempt_path, receipt_path = [
        directory / f"taxonomy-1399146-{kind}.json" for kind in ("attempt", "receipt")
    ]
    attempt, receipt = [json.loads(p.read_bytes()) for p in (attempt_path, receipt_path)]
    require(
        attempt["plan"] == reference.pin(root, path)
        and attempt["url"]
        == receipt["url"]
        == frozen["requests"]["1399146"]["url"]
        == "https://rest.uniprot.org/taxonomy/1399146.json"
        and all(d[k] == 0 for d in (frozen, attempt, receipt) for k in ("retries", "redirects_followed"))
        and receipt["bytes"] <= frozen["max_response_bytes"]
        and {p.name for p in directory.glob("taxonomy-*-attempt.json")} == {attempt_path.name}
        and {p.name for p in directory.glob("taxonomy-*-receipt.json")} == {receipt_path.name},
        "unaccounted or changed taxonomy request",
    )
    source = {"url": receipt["url"], "wrapper": reference.pin(root, receipt_path)}
    registry = {**cached, "1399146": {"taxon_id": "1399146", "source": source}}
    taxa, sources = {}, {}
    for tid, item in sorted(registry.items()):
        taxa[tid], sources[tid] = prior.cached_node(root, item)
    inspection_path = root / (PREFIX + "-taxonomy-inspection.json")
    inspection = json.loads(inspection_path.read_bytes())
    _, species = prior.lineages.lineage(taxa["1399146"])
    require(
        inspection["plan"] == reference.pin(root, path)
        and inspection["source"] == source
        and inspection["accepted_for_reference_taxonomy"] is True
        and inspection["experimental_identity_assignments"] is False
        and inspection["identity"] == prior.lineages.identity(taxa["1399146"])
        and inspection["species"] == species,
        "taxonomy inspection differs from native identity",
    )
    return (
        taxa,
        sources,
        {
            "plan": reference.pin(root, path),
            "inspection": reference.pin(root, inspection_path),
            "attempt": reference.pin(root, attempt_path),
        },
    )


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["fields"] == prior.FIELDS
        and plan["entry_status_filter"] is None
        and plan["page_size"] == 500
        and plan["max_pages_per_query"] == 20
        and plan["max_results_per_query"] == 10000
        and plan["release"] == "2026_03"
        and plan["retries"] == plan["redirects_followed"] == 0
        and plan["constraints"]
        == {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "outreach": False,
            "reuse_terms_review_resumed": False,
            "biological_record_writes": False,
            "experimental_identity_assignments": False,
            "operational_details_exported": False,
            "new_primary_reviews": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "planned scope changed",
    )
    selected, held, records, claims = current_selection(root, plan)
    entries, pools, queries = query_results(root, plan)
    taxa, sources, new_taxonomy = reference_taxonomy(root, plan, entries, queries)
    views = {
        "UniProtKB:" + a: prior.prior.members.member_reference(e, taxa[str(e["organism"]["taxonId"])])
        for a, e in sorted(entries.items())
    }
    terms = {}
    for term, row in selected.items():
        name, symbol = row["tokens"]["species"], row["tokens"]["gene"]
        candidates = []
        for accession in pools[name]:
            matches = prior.native_matches(entries[accession], symbol)
            if not matches:
                continue
            view = views["UniProtKB:" + accession]
            status = prior.disposition(
                plan["source_bindings"][name]["identity"], view["reference_taxonomy"]["species"]
            )
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
                    if prior.prior.gene_matches(entries[accession], symbol)
                    else "ORDERED_LOCUS_REFERENCE_NOT_GENE_RENAMING",
                    "own_definition_citation_overlap": sorted(
                        bibliography & set(row["definition_citations"])
                    ),
                    "citation_overlap_is_primary_validation": False,
                    "disposition": status,
                    "qualified_reference": status == prior.QUALIFIED,
                    "experimental_subject_assignment": False,
                    "exact_allele_assignment": False,
                }
            )
        qualified = [c["protein_accession"] for c in candidates if c["qualified_reference"]]
        terms[term] = {
            "source_label": row["source_label"],
            "tokens": row["tokens"],
            "record_memberships": row["record_memberships"],
            "definition_citations": row["definition_citations"],
            "prior_status": row["status"],
            "reference_candidates": candidates,
            "qualified_reference_accessions": qualified,
            "status": "QUALIFIED_ALL_STATUS_REFERENCE_PRIMARY_REVIEW_OPEN"
            if qualified
            else "EXACT_FIELDS_WITHHELD_FOR_TAXONOMY"
            if candidates
            else "NO_EXACT_NATIVE_FIELD_MATCH_IN_COMPLETE_QUERY_NOT_BIOLOGICAL_ABSENCE",
            "whole_record_primary_review": "OPEN",
            "biological_absence_inferred": False,
        }
    qualified_terms = {t for t, r in terms.items() if r["qualified_reference_accessions"]}
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "prior": plan["prior"],
        "name_followup": plan["name_followup"],
        "canary": reference.pin(root, root / CANARY),
        "records": records,
        "claims": claims,
        "terms": terms,
        "name_unresolved_terms": held,
        "source_bindings": plan["source_bindings"],
        "queries": queries,
        "reference_views": views,
        "taxonomy_sources": sources,
        "new_taxonomy": new_taxonomy,
        "summary": {
            "corpus_records_hash_checked": 2939,
            "selected_terms": len(terms),
            "name_unresolved_terms": len(held),
            "complete_records_read": len(records),
            "source_claims": len(claims),
            "species_queries": len(queries),
            "new_species_queries": len(plan["requests"]),
            "reused_species_queries": len(plan["reused_queries"]),
            "new_protein_page_requests": sum(
                len(q["pages"]) for k, q in queries.items() if k in plan["requests"]
            ),
            "zero_hit_queries": sum(q["result_count"] == 0 for q in queries.values()),
            "native_reference_entries": len(entries),
            "reference_taxa": len(taxa),
            "entry_type_counts": dict(sorted(Counter(e["entryType"] for e in entries.values()).items())),
            "qualified_reference_terms": len(qualified_terms),
            "qualified_reference_links": sum(
                len(r["qualified_reference_accessions"]) for r in terms.values()
            ),
            "qualified_reference_claim_memberships": sum(c["aro_id"] in qualified_terms for c in claims),
            "qualified_reference_records": len(
                {c["record_identifier"] for c in claims if c["aro_id"] in qualified_terms}
            ),
            "term_status_counts": dict(sorted(Counter(r["status"] for r in terms.values()).items())),
            "new_uniprot_taxonomy_requests": 1,
            "ncbi_requests": 0,
        },
        "limits": {
            **plan["constraints"],
            "prior_dossiers_rewritten": False,
            "all_possible_gene_aliases_or_alleles_searched": False,
            "whole_record_primary_signoffs": 0,
            "unreviewed_annotation_proves_resistance": False,
            "ordered_locus_matches_are_gene_symbols": False,
        },
        "attribution": (
            "CARD/ARO and UniProt CC BY 4.0; reference metadata, not new primary experimental evidence."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
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
