"""Reconcile nomenclature and reference metadata without assigning resistant alleles."""

import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_unresolved_names as names
import audit_fungamr_references as fungal
import audit_mex_component_references as mex
from lxml import html

prior = names.prior
reference, require, read_json = prior.reference, prior.require, prior.read_json
PREFIX = "research/2026-10-15-card-name-crosswalks"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
SCOPE = "VERIFIED_NAME_CROSSWALKS_AND_REFERENCE_PROTEINS_NOT_EXPERIMENTAL_ALLELES"
QUALIFIED = "NAME_CROSSWALK_GENE_AND_SPECIES_REFERENCE_NOT_EXPERIMENTAL_ALLELE"


def normalized(node):
    return " ".join(" ".join(node.itertext()).split())


def lpsn_context(payload):
    tree = html.fromstring(payload)
    require(
        tree.xpath("//title/text()") == ["Species: Mycobacteroides abscessus"], "LPSN page identity changed"
    )
    rows = [[normalized(cell) for cell in row.xpath("./td")] for row in tree.xpath("//tr")]
    matches = [
        row
        for row in rows
        if len(row) == 2
        and row[0] == "Mycobacterium abscessus (Moore and Frerichs 1953) Kusunoki and Ezaki 1992"
        and row[1] == "homotypic synonym, validly published under the ICNP"
    ]
    require(len(matches) == 1, "specific validly published homotypic synonym not found uniquely")
    return {
        "source_name": "Mycobacterium abscessus",
        "uniprot_name": "Mycobacteroides abscessus",
        "relation": "HOMOTYPIC_SYNONYM",
        "support": "LPSN_NATIVE_SYNONYM_TABLE",
        "nomenclatural_authorship": "(Moore and Frerichs 1953) Kusunoki and Ezaki 1992",
        "genus_preference_or_experimental_subject_inferred": False,
    }


def fijiensis_context(payload):
    tree = html.fromstring(payload)
    titles = tree.xpath('//meta[@name="citation_title"]/@content')
    dois = tree.xpath('//meta[@name="citation_doi"]/@content')
    require(
        len(titles) == 1
        and dois == ["10.1371/journal.pgen.1005876"]
        and "Pseudocercospora fijiensis (Synonym Mycosphaerella fijiensis)" in titles[0]
        and any(
            "Pseudocercospora fijiensis (previously: Mycosphaerella fijiensis)" in normalized(n)
            for n in tree.xpath('//*[contains(@class,"abstract")]')
        ),
        "author-institution title, DOI or abstract name relation changed",
    )
    return {
        "source_name": "Mycosphaerella fijiensis",
        "uniprot_name": "Pseudocercospora fijiensis",
        "relation": "PUBLICATION_EXPLICIT_SYNONYM",
        "doi": dois[0],
        "support": "AUTHOR_INSTITUTION_PUBLICATION_TITLE_AND_ABSTRACT",
        "full_text_results_or_phylogeny_reviewed": False,
    }


def accept_name(payload, source_name, identity, proof):
    matches = [n for n in payload["results"] if n["taxonId"] == identity["taxonId"]]
    require(len(matches) == 1, "missing or duplicate selected native taxon")
    node = matches[0]
    require(
        node["active"] is True and prior.lineages.identity(node) == identity, "native taxon identity changed"
    )
    if proof is None:
        require(node["scientificName"] == source_name, "direct name is not native scientific name")
        require(
            [n["taxonId"] for n in payload["results"] if n["active"] and n["scientificName"] == source_name]
            == [identity["taxonId"]],
            "ambiguous active native name",
        )
        relation = "EXACT_NATIVE_NAME_RANK_PRESERVED"
    else:
        require(
            node["rank"] == "species"
            and source_name in node.get("otherNames", [])
            and proof["source_name"] == source_name
            and proof["uniprot_name"] == node["scientificName"]
            and proof["relation"]
            in {"HOMOTYPIC_SYNONYM", "PUBLICATION_EXPLICIT_SYNONYM", "FORMAL_NEW_COMBINATION"},
            "independent name crosswalk does not bind the native species",
        )
        require(
            [
                n["taxonId"]
                for n in payload["results"]
                if n["active"]
                and n["rank"] == "species"
                and n["scientificName"] == proof["uniprot_name"]
                and source_name in n.get("otherNames", [])
            ]
            == [identity["taxonId"]],
            "ambiguous native species for independent name proof",
        )
        relation = proof["relation"]
    lineage, species = prior.lineages.lineage(node)
    return {
        "identity": identity,
        "source_name": source_name,
        "relation": relation,
        "evidence": proof,
        "reference_lineage": lineage,
        "species_ancestor": species,
        "source_name_automatically_replaced_by_species_ancestor": False,
        "experimental_subject_assignment": False,
    }


def source_evidence(root, plan, inputs):
    directory = root / plan["cache_directory"]
    request_plan = inputs["source_request_plan"]
    plan_sha = plan["inputs"]["source_request_plan"]["sha256"]
    require(
        inputs["source_canary"]["plan_sha256"] == plan_sha
        and inputs["source_canary"]["approved_for_remaining_sources"] is True
        and inputs["source_canary"]["receipt"] == plan["source_receipts"]["lpsn"]
        and set(plan["source_receipts"])
        == set(request_plan["requests"])
        == {"lpsn", "fijiensis", "oculimacula"},
        "source retrieval plan or inspected canary changed",
    )
    bodies, sources = {}, {}
    for key, pin in plan["source_receipts"].items():
        receipt = read_json(root, pin)
        attempt_path = directory / (key + "-attempt.json")
        attempt = json.loads(attempt_path.read_bytes())
        require(
            receipt["url"] == attempt["url"] == request_plan["requests"][key]["url"]
            and receipt["plan_sha256"] == attempt["plan_sha256"] == plan_sha
            and receipt["key"] == attempt["key"] == key
            and all(
                d[k] == 0 for d in (request_plan, receipt, attempt) for k in ("retries", "redirects_followed")
            ),
            "unaccounted or changed nomenclature request",
        )
        body = reference.check_pin(root, receipt["body"]).read_bytes()
        headers = {k.lower(): v for k, v in receipt["headers"].items()}
        require(
            len(body) == receipt["bytes"] <= request_plan["requests"][key]["max_bytes"], "source size changed"
        )
        require(receipt["status"] == (302 if key == "oculimacula" else 200), "source response status changed")
        if key != "oculimacula":
            require(
                "text/html" in headers.get("content-type", "") and not headers.get("location"),
                "source is not native HTML",
            )
        else:
            require(
                headers.get("location")
                == "https://openresearch-repository.anu.edu.au/server/api/core/bitstreams/19d99f6c-7319-40a4-b52d-799fbba03c1c/content",
                "redirect destination changed",
            )
        bodies[key] = body
        sources[key] = {
            "receipt": pin,
            "body": receipt["body"],
            "attempt": reference.pin(root, attempt_path),
            "url": receipt["url"],
            "status": receipt["status"],
            "retrieved_at": receipt["retrieved_at"],
        }
    require(
        {p.name for p in directory.glob("*-error.json")} == {"oculimacula-error.json"}
        and {p.name for p in directory.glob("*-attempt.json") if not p.name.startswith("protein-")}
        == {key + "-attempt.json" for key in request_plan["requests"]},
        "unaccounted source attempt or error",
    )
    for suffix in ("receipt.json", "response.bin"):
        require(
            {p.name for p in directory.glob("*-" + suffix) if not p.name.startswith("protein-")}
            == {key + "-" + suffix for key in request_plan["requests"]},
            "orphan nomenclature artifact",
        )
    error_path = directory / "oculimacula-error.json"
    error = json.loads(error_path.read_bytes())
    require(
        error["retry_performed"] is False and error["url"] == sources["oculimacula"]["url"],
        "hold was retried",
    )
    hold = {
        "source": sources["oculimacula"],
        "error": reference.pin(root, error_path),
        "status": "HTTP_302_NOT_FOLLOWED_UNDER_FROZEN_NO_REDIRECT_PLAN",
        "full_text_retrieved": False,
        "primary_nomenclature_verified": False,
        "retry_or_alternate_route_used": False,
        "permanent_unavailability_inferred": False,
        "affected_source_names": ["Tapesia acuformis", "Tapesia yallundae"],
    }
    return (
        {
            "Mycobacterium abscessus": {**lpsn_context(bodies["lpsn"]), "source": sources["lpsn"]},
            "Mycosphaerella fijiensis": {
                **fijiensis_context(bodies["fijiensis"]),
                "source": sources["fijiensis"],
            },
        },
        sources,
        hold,
    )


def old_zero_queries(root, inputs):
    result = {}
    for source_key, term, gene, tid in (
        ("fungamr", "ARO:3009390", "Cdc6", "5478"),
        ("folp", "ARO:3007749", "folP", "594"),
    ):
        saved = inputs[source_key]["terms"][term]["queries"]
        if source_key == "folp":
            require(
                isinstance(saved, dict) and set(saved) == {"reviewed", "unreviewed"},
                "old folP query map changed",
            )
            rows = [("folp-" + key, row) for key, row in saved.items()]
        else:
            require(isinstance(saved, list), "old fungal query list changed")
            rows = [(row["key"], row) for row in saved]
        require(len(rows) == 2, "old entry-status partition changed")
        statuses = set()
        for key, row in rows:
            source = row["source"]
            for field in ("attempt", "plan"):
                if field in source:
                    reference.check_pin(root, source[field])
            payload, provenance = prior.prior.members.screen.read_source(root, source)
            params = parse_qs(urlsplit(source["url"]).query)
            reviewed = row["reviewed_subset"]
            statuses.add(reviewed)
            require(
                type(reviewed) is bool
                and params["query"]
                == [f"gene_exact:{gene} AND taxonomy_id:{tid} AND reviewed:{str(reviewed).lower()}"]
                and payload["results"] == []
                and row["result_count"] == 0,
                "old complete zero query differs from the preserved scope",
            )
            require(key not in result, "duplicate old query key")
            result[key] = {
                "term": term,
                "gene": gene,
                "source": source,
                "validated_provenance": provenance,
                "result_count": 0,
                "reused": True,
                "biological_absence_inferred": False,
            }
        require(statuses == {True, False}, "old status partition incomplete")
    return result


def protein_queries(root, plan, inputs):
    frozen = inputs["protein_plan"]
    directory = root / frozen["cache_directory"]
    require(
        set(frozen["requests"]) == set(plan["new_protein_receipts"]) == {"fur1", "atpe", "cyp51a"},
        "protein cohort changed",
    )
    require(
        frozen["entry_status_filter"] is None and frozen["fields"] == prior.FIELDS,
        "protein fields or status scope changed",
    )
    require(
        frozen["source_inputs"]["name_checkpoint"] == plan["inputs"]["name_checkpoint"]
        and frozen["source_inputs"]["cached_nomenclature"] == plan["inputs"]["nomenclature_review"]
        and all(
            frozen["source_inputs"][key] == plan["source_receipts"][key] for key in ("lpsn", "fijiensis")
        ),
        "protein query plan is not grounded in the inspected name sources",
    )
    entries, queries, pools = {}, {}, {}
    for key, item in frozen["requests"].items():
        expected = {
            "query": [f"(gene_exact:{item['gene']}) AND taxonomy_id:{item['taxon_id']}"],
            "format": ["json"],
            "size": ["500"],
            "sort": ["accession asc"],
            "fields": [prior.FIELDS],
        }
        require(item["parameters"] == {k: v[0] for k, v in expected.items()}, "native protein query changed")
        attempt_path = directory / ("protein-" + key + "-attempt.json")
        attempt = json.loads(attempt_path.read_bytes())
        require(
            attempt["plan"] == plan["inputs"]["protein_plan"]
            and attempt["key"] == key
            and attempt["url"] == item["url"]
            and attempt["retries"] == attempt["redirects_followed"] == 0,
            "protein request differs from frozen plan",
        )
        found, provenance = mex.native_query(root, plan["new_protein_receipts"][key], expected)
        require(
            provenance["bytes"] <= frozen["max_bytes"] and provenance["url"] == item["url"],
            "protein body bound or URL changed",
        )
        for accession, entry in found.items():
            require(
                entry["entryType"] in {"UniProtKB reviewed (Swiss-Prot)", "UniProtKB unreviewed (TrEMBL)"}
                and not {"sequence", "features", "comments"} & set(entry),
                "untyped or operational metadata",
            )
            require(accession not in entries or entries[accession] == entry, "conflicting reference metadata")
            entries[accession] = entry
        pools[key] = sorted(found)
        queries[key] = {
            "source": provenance,
            "attempt": reference.pin(root, attempt_path),
            "source_name": item["source_name"],
            "gene": item["gene"],
            "result_count": len(found),
            "reused": False,
        }
    canary = inputs["protein_canary"]
    require(
        canary["plan"] == plan["inputs"]["protein_plan"]
        and canary["approved_for_remaining_queries"] is True
        and canary["source"] == plan["new_protein_receipts"]["fur1"]
        and canary["accessions"] == pools["fur1"],
        "protein canary binding changed",
    )
    require(
        {p.name for p in directory.glob("protein-*-attempt.json")}
        == {"protein-" + k + "-attempt.json" for k in frozen["requests"]}
        and not list(directory.glob("protein-*-error.json")),
        "unaccounted or failed protein query",
    )
    for suffix in ("receipt", "body"):
        require(
            {p.name for p in directory.glob("protein-*-" + suffix + ".json")}
            == {"protein-" + key + "-" + suffix + ".json" for key in frozen["requests"]},
            "orphan protein query artifact",
        )
    return entries, pools, queries


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["constraints"]
        == {
            "new_nomenclature_requests": 3,
            "new_uniprot_protein_requests": 3,
            "new_uniprot_taxonomy_requests": 0,
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "biological_record_writes": False,
            "experimental_identity_assignments": False,
            "new_primary_resistance_reviews": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "planned reference-only scope changed",
    )
    for pin in plan["inputs"].values():
        reference.check_pin(root, pin)
    inputs = {k: read_json(root, v) for k, v in plan["inputs"].items() if k != "source_queue"}
    checkpoint = inputs["name_checkpoint"]
    selected = {t: r for t, r in checkpoint["terms"].items() if r["reference_species"] is None}
    require(len(selected) == 36, "remaining source-name cohort changed")
    records, claims = prior.prior.members.current_context(
        root,
        inputs["index"],
        inputs["corpus_update"],
        set(selected),
        {t: r["source_label"] for t, r in selected.items()},
    )
    proofs, source_snapshots, hold = source_evidence(root, plan, inputs)
    name_views, payloads = {}, {}
    for name in sorted({r["tokens"]["species"] for r in selected.values()}):
        if name in names.CONTEXTS:
            name_views[name] = checkpoint["names"][name]
            continue
        source = checkpoint["native_sources"][name]
        assessment, _ = names.native_name(root, name, source, allow_unranked=name == "Salmonella gallinarum")
        require(assessment == checkpoint["names"][name], "frozen source-name result changed")
        payloads[name], _ = prior.prior.members.screen.read_source(root, source)
        name_views[name] = assessment
    review = inputs["nomenclature_review"]
    reused = fungal.nomenclature(root, review, payloads["Nakaseomyces glabratus"])
    require(inputs["fungamr"]["nomenclature_assessment"] == review, "old nomenclature assessment differs")
    proofs["Nakaseomyces glabratus"] = {
        "source_name": reused["source_name"],
        "uniprot_name": reused["scientific_name"],
        "relation": "FORMAL_NEW_COMBINATION",
        "doi": reused["doi"],
        "support": "REUSED_PRIMARY_NOMENCLATURE_REVIEW",
        "review": plan["inputs"]["nomenclature_review"],
        "printed_pages": review["printed_pages"],
        "new_primary_review_claimed": False,
    }
    resolved = {}
    for name, identity in plan["reference_name_targets"].items():
        resolved[name] = {
            **accept_name(payloads[name], name, identity, proofs.get(name)),
            "native_source": checkpoint["native_sources"][name],
        }
    require(set(resolved) == set(proofs) | {"Salmonella gallinarum"}, "unexplained name resolution")
    for item in inputs["protein_plan"]["requests"].values():
        require(
            item["taxon_id"] == str(resolved[item["source_name"]]["identity"]["taxonId"])
            and any(
                r["tokens"] == {"species": item["source_name"], "gene": item["gene"]}
                for r in selected.values()
            ),
            "protein query is not bound to the resolved source term",
        )
    entries, pools, queries = protein_queries(root, plan, inputs)
    reused_queries = old_zero_queries(root, inputs)
    registry = inputs["taxonomy_inventory"]["registry"]
    views, taxonomy_sources = {}, {}
    for accession, entry in sorted(entries.items()):
        tid = str(entry["organism"]["taxonId"])
        require(tid in registry, "reference lacks independent cached taxonomy")
        node, source = prior.cached_node(root, registry[tid])
        views["UniProtKB:" + accession] = prior.prior.members.member_reference(entry, node)
        taxonomy_sources[tid] = source
    terms = {}
    for term, row in selected.items():
        name, gene = row["tokens"]["species"], row["tokens"]["gene"]
        candidates = []
        keys = [k for k, q in queries.items() if q["source_name"] == name and q["gene"] == gene]
        for key in keys:
            require(
                resolved[name]["identity"]["rank"] == "species",
                "non-species reference query must retain narrower taxon",
            )
            for accession in pools[key]:
                matches = prior.native_matches(entries[accession], gene)
                if not matches:
                    continue
                view = views["UniProtKB:" + accession]
                agrees = resolved[name]["identity"] == view["reference_taxonomy"]["species"]
                bibliography = {
                    "PMID:" + i["id"]
                    for b in view["native_bibliography"]
                    for i in b["identifiers"]
                    if i["database"] == "PubMed"
                }
                candidates.append(
                    {
                        "protein_accession": "UniProtKB:" + accession,
                        "native_gene_fields": matches,
                        "disposition": QUALIFIED if agrees else "REFERENCE_SPECIES_MISMATCH_WITHHELD",
                        "qualified_reference": agrees,
                        "own_definition_citation_overlap": sorted(
                            bibliography & set(row["definition_citations"])
                        ),
                        "primary_resistance_validation": False,
                        "experimental_subject_assignment": False,
                        "exact_allele_assignment": False,
                    }
                )
        reused_keys = [k for k, q in reused_queries.items() if q["term"] == term]
        qualified_accessions = [c["protein_accession"] for c in candidates if c["qualified_reference"]]
        if qualified_accessions:
            protein_status = "QUALIFIED_REFERENCE_CONTEXT_NOT_EXPERIMENTAL_ALLELE"
        elif keys or reused_keys:
            result_count = sum(queries[k]["result_count"] for k in keys) + sum(
                reused_queries[k]["result_count"] for k in reused_keys
            )
            protein_status = (
                "COMPLETE_QUERY_ZERO_RESULTS"
                if result_count == 0
                else "COMPLETE_QUERY_NO_QUALIFIED_REFERENCE"
            )
        else:
            protein_status = "NOT_QUERIED_BY_THIS_CROSSWALK_AUDIT"
        terms[term] = {
            "prior_name_assessment": row,
            "source_label": row["source_label"],
            "tokens": row["tokens"],
            "definition_citations": row["definition_citations"],
            "record_memberships": row["record_memberships"],
            "name_status": "RESOLVED_REFERENCE_NAME_RANK_PRESERVED"
            if name in resolved
            else row["name_status"],
            "protein_reference_status": protein_status,
            "reference_name_context": resolved.get(name),
            "new_query_keys": keys,
            "reused_query_keys": reused_keys,
            "reference_candidates": candidates,
            "qualified_reference_accessions": qualified_accessions,
            "exact_allele_assignment": False,
            "experimental_subject_assignment": False,
            "primary_resistance_validation": False,
            "whole_record_primary_review": "OPEN",
            "biological_absence_inferred": False,
        }
    qualified = {t for t, r in terms.items() if r["qualified_reference_accessions"]}
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "inputs": plan["inputs"],
        "records": records,
        "claims": claims,
        "terms": terms,
        "prior_name_assessments": name_views,
        "resolved_reference_names": resolved,
        "source_snapshots": source_snapshots,
        "nomenclature_access_hold": hold,
        "queries": queries,
        "reused_queries": reused_queries,
        "reference_views": views,
        "taxonomy_sources": taxonomy_sources,
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(records),
            "source_claims": len(claims),
            "selected_terms": len(terms),
            "source_name_contexts": len(name_views),
            "resolved_reference_name_contexts": len(resolved),
            "resolved_species_name_contexts": sum(
                v["identity"]["rank"] == "species" for v in resolved.values()
            ),
            "resolved_non_species_name_contexts": sum(
                v["identity"]["rank"] != "species" for v in resolved.values()
            ),
            "terms_with_resolved_reference_names": sum(
                r["reference_name_context"] is not None for r in terms.values()
            ),
            "remaining_name_unresolved_terms": sum(
                r["reference_name_context"] is None for r in terms.values()
            ),
            "new_complete_protein_queries": len(queries),
            "reused_complete_status_queries": len(reused_queries),
            "new_native_reference_entries": len(entries),
            "cached_reference_taxa": len(taxonomy_sources),
            "entry_type_counts": dict(sorted(Counter(e["entryType"] for e in entries.values()).items())),
            "qualified_reference_terms": len(qualified),
            "qualified_reference_links": sum(
                len(r["qualified_reference_accessions"]) for r in terms.values()
            ),
            "qualified_reference_claim_memberships": sum(
                len(terms[t]["record_memberships"]) for t in qualified
            ),
            "qualified_reference_records": len(
                {rid for t in qualified for rid in terms[t]["record_memberships"]}
            ),
            "selected_terms_without_qualified_references": len(terms) - len(qualified),
            "biological_record_writes": 0,
            "new_primary_resistance_reviews": 0,
            "whole_record_primary_signoffs": 0,
            "ncbi_requests": 0,
        },
        "limits": [
            "Name synonymy is independent of resistance, allele, strain, isolate and genome identity.",
            "Unranked Salmonella gallinarum stays unranked; "
            "its species ancestor is not substituted as the named subject.",
            "Other-name matches require explicit independent nomenclature evidence, not spelling similarity.",
            "The two Tapesia contexts retain the HTTP 302 hold; "
            "no full text, redirect or alternate route was used.",
            "Zero native query results and unresolved source names do not establish biological absence.",
            "No sequences, variants, protocols or numeric AST are exported; #1040 remains deferred.",
            "The full corpus investigation remains OPEN; "
            "no biological records, source adoption or GitHub state changed.",
        ],
        "attribution": {
            "CARD_ARO": "CC BY 4.0",
            "UniProt": "CC BY 4.0",
            "other_sources": "Cited nomenclatural evidence only; "
            "native pages retained in ignored cache, no bulk adoption.",
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
        require(output.read_text() == payload, "saved name-crosswalk audit differs from offline replay")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
