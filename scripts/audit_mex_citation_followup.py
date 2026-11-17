"""Replay Mex citation candidates, scoped nonmatches and a publisher access hold."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_literature_expansion as literature
import audit_mex_component_references as mex
import audit_topoisomerase_references as reference

PREFIX = "research/2026-10-15-mex-citation-followup"
PLAN = Path(PREFIX + "-native-plan.json")
OUTPUT = Path(PREFIX + ".json")
SCOPE = "MEX_CITATION_AND_SPECIES_REFERENCE_FOLLOWUP_NOT_EXPERIMENTAL_GROUNDING"
DOI = "10.1111/j.1348-0421.2005.tb03696.x"
PUBLISHER = "https://onlinelibrary.wiley.com/doi/" + DOI
EXPECTED = {
    "G3XCL7": "opmE",
    "Q4LDT6": "mexQ",
    "Q4LDT7": "mexP",
    "Q4LDT8": "mexN",
    "Q4LDT9": "mexM",
    "I0IYR4": "oprA",
    "I0IYR5": "oprA",
}
require = mex.require


def native_http(root, source, url, status):
    receipt = mex.read_json(root, source)
    path = reference.check_pin(root, receipt["body"])
    require(
        receipt["url"] == url
        and receipt["status"] == status
        and receipt["redirects_followed"] == receipt["retries"] == 0
        and path.stat().st_size == receipt["bytes"],
        "native HTTP identity or status changed",
    )
    return path.read_bytes(), {"receipt": source, **receipt}


def project_metadata(payload):
    require(
        payload["hitCount"] == 1
        and len(payload["resultList"]["result"]) == 1
        and not payload.get("nextCursorMark")
        and payload["request"]["queryString"] == "EXT_ID:16301811 AND SRC:MED"
        and payload["request"]["resultType"] == "CORE"
        and payload["request"]["pageSize"] == 1,
        "publication query scope changed",
    )
    (row,) = payload["resultList"]["result"]
    require(
        row["id"] == row["pmid"] == "16301811"
        and row["source"] == "MED"
        and row["doi"] == DOI
        and row["isOpenAccess"] == row["inEPMC"] == "N"
        and row["title"]
        == "Gene cloning and properties of the RND-type multidrug efflux pumps "
        "MexPQ-OpmE and MexMN-OprM from Pseudomonas aeruginosa."
        and "https://doi.org/" + DOI in {r["url"] for r in row["fullTextUrlList"]["fullTextUrl"]}
        and all(name in row["abstractText"] for name in ("MexPQ-OpmE", "MexMN-OprM")),
        "publication identity or indexed access metadata changed",
    )
    return {
        "pmid": "PMID:16301811",
        "doi": DOI,
        "title": row["title"],
        "isOpenAccess": row["isOpenAccess"],
        "inEPMC": row["inEPMC"],
        "abstract_sha256": hashlib.sha256(row["abstractText"].encode()).hexdigest(),
        "evidence_scope": "INDEXED_ABSTRACT_NOT_FULL_TEXT_OR_EXPERIMENTAL_ACCESSION_CROSSWALK",
        "abstract_names_both_complexes": True,
        "quantitative_phenotype_or_experimental_identity_exported": False,
        "index_access_flags_are_not_global_access_or_reuse_decisions": True,
    }


def project_term(term, pools, entries, adjacent=None):
    own = term["definition_citation_ids"]
    require(adjacent is None or adjacent not in own, "adjacent citation mislabeled as own citation")
    citations = own + ([adjacent] if adjacent else [])
    candidates = []
    for gene in term["component_search_symbols"]:
        for accession, entry in sorted(entries.items()):
            genes = [g["geneName"]["value"] for g in entry.get("genes", []) if "geneName" in g]
            source_ids = [p for p in citations if accession in pools[p.removeprefix("PMID:")]]
            if gene in genes and source_ids:
                candidates.append(
                    {
                        "gene_symbol": gene,
                        "accession": "UniProtKB:" + accession,
                        "own_definition_citations": [p for p in source_ids if p in own],
                        "adjacent_followup_citations": [p for p in source_ids if p not in own],
                        "status": "SYMBOL_AND_BIBLIOGRAPHY_CANDIDATE_NOT_VERIFIED_COMPLEX_OR_ALLELE",
                        "experimental_subject_assignment": False,
                        "complex_membership_proven": False,
                    }
                )
    return {
        k: term[k]
        for k in (
            "source_label",
            "complex_label",
            "component_search_symbols",
            "definition_citation_ids",
            "record_memberships",
        )
    } | {
        "component_candidates": candidates,
        "adjacent_citation_lead": adjacent,
        "whole_record_primary_review": "OPEN",
        "exact_experimental_complex_assignment": False,
        "reference_candidates_replace_existing_claims": False,
    }


def build(root):
    native = json.loads((root / PLAN).read_bytes())
    plan = mex.read_json(root, native["plan"])
    require(
        plan["scope"] == SCOPE and plan["new_gene_symbols"] == ["mexJ", "mexK", "mexV", "mexW"],
        "follow-up scope changed",
    )
    prior = mex.read_json(root, plan["prior"])
    require(mex.build(root) == prior, "prior Mex current-corpus replay changed")
    prior_verification = mex.read_json(root, plan["prior_verification"])
    require(plan["prior"] in prior_verification["files"], "prior checkpoint not verified")
    selected = {
        t: r for t, r in prior["terms"].items() if not r["all_label_components_have_native_annotations"]
    }
    require(
        sorted(selected) == plan["selected_terms"] and len(selected) == 9, "selected term coverage changed"
    )
    registry = mex.read_json(root, plan["query_registry"])
    pmids = sorted(
        {p[5:] for t in selected.values() for p in t["definition_citation_ids"] if p.startswith("PMID:")}
    )
    require(pmids == plan["cached_citation_queries"], "own citation coverage changed")
    pools, entries, citation_queries = {}, {}, {}
    for pmid in pmids:
        registered = registry["queries"][pmid]
        pool, query = literature.read_query(root, root / registered["directory"], pmid)
        require(
            query == registered["query"] and query["complete_for_query"] and query["release"] == mex.RELEASE,
            "cached query provenance changed",
        )
        pools[pmid], citation_queries[pmid] = pool, query
        for accession, entry in pool.items():
            require(
                not {"sequence", "features"} & set(entry)
                and (accession not in entries or entries[accession] == entry),
                "citation entry conflict",
            )
            entries[accession] = entry
    require(set(entries) == set(EXPECTED) | {"I0IYR3"}, "citation candidate pool requires fresh review")
    require(
        native["adjacent_citation_leads"] == {"ARO:3003703": "PMID:16301811"}
        and native["adjacent_citation_is_not_own_definition_citation"] is True,
        "adjacent citation interpretation changed",
    )
    terms = {
        tid: project_term(term, pools, entries, native["adjacent_citation_leads"].get(tid))
        for tid, term in sorted(selected.items())
    }
    linked = {
        r["accession"].removeprefix("UniProtKB:") for t in terms.values() for r in t["component_candidates"]
    }
    require(linked == set(EXPECTED), "symbol/citation selection changed")
    taxon, taxonomy_source = mex.native_taxon(root, native["taxonomy"], "287", mex.RELEASE)
    references = {}
    for accession in sorted(linked):
        projected = mex.project_reference(entries[accession], taxon)
        require(
            projected["gene_symbols"] == [EXPECTED[accession]]
            and projected["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
            and projected["reference_taxonomy"]["native_rank"] == "species",
            "candidate identity changed",
        )
        key = projected["accession"]
        projected["already_in_prior_mex_dossier"] = key in prior["reference_candidates"]
        if projected["already_in_prior_mex_dossier"]:
            for field in ("entry_type", "entry_audit", "gene_symbols", "protein_names", "reference_taxonomy"):
                require(
                    projected[field] == prior["reference_candidates"][key][field],
                    "prior reference identity differs",
                )
        references[key] = projected
    sources, empty_queries = {}, {}
    for key, symbols in (("mexj-canary", ["mexJ"]), ("remaining-symbols", ["mexK", "mexV", "mexW"])):
        pool, source = mex.native_query(root, native["requests"][key], mex.parameters(symbols, 287, False))
        require(not pool and source["url"] == plan["urls"][key], "new symbol match requires review")
        body = mex.read_json(root, source["body"])
        empty_queries[key] = {
            "symbols": symbols,
            "complete_for_exact_query": True,
            "result_count": 0,
            "native_suggestion_count": len(body.get("suggestions", [])),
            "suggestions_followed": False,
            "biological_absence_inferred": False,
            "source": source,
        }
    canary = mex.read_json(root, native["canary_inspected"])
    require(
        canary["accepted"] is True
        and canary["suggestions_followed"] is False
        and canary["response"] == empty_queries["mexj-canary"]["source"]["body"],
        "canary not inspected",
    )
    prior_opmh = mex.read_json(root, plan["reused_opmh_no_hit"])
    old_source = prior_opmh["sources"]["opmh-species-reference"]
    for field in ("body", "receipt", "attempt", "plan"):
        reference.check_pin(root, old_source[field])
    url = urlsplit(old_source["url"])
    parameters = parse_qs(url.query)
    require(parameters["query"] == ["gene_exact:opmH AND taxonomy_id:287"], "OpmH query scope changed")
    old_body, old_provenance = reference.read_response(
        root,
        (root / old_source["body"]["path"]).parent,
        "opmh-species-reference",
        "/uniprotkb/search",
        parameters,
    )
    require(
        old_body["results"] == [] and old_provenance["release"] == mex.RELEASE,
        "OpmH candidate requires review",
    )
    metadata_body, sources["metadata"] = native_http(
        root, native["requests"]["metadata-16301811"], plan["urls"]["metadata-16301811"], 200
    )
    publication = project_metadata(json.loads(metadata_body))
    _, sources["doi"] = native_http(root, native["requests"]["doi"], "https://doi.org/" + DOI, 302)
    require(sources["doi"]["headers"]["location"] == PUBLISHER, "DOI redirect target changed")
    _, sources["publisher"] = native_http(root, native["requests"]["publisher"], PUBLISHER, 403)
    require(not sources["publisher"]["headers"].get("location"), "unexpected publisher redirect")
    primary_plan = mex.read_json(root, native["primary_plan"])
    publisher_plan = mex.read_json(root, native["publisher_plan"])
    require(
        primary_plan["metadata"] == sources["metadata"]["body"]
        and primary_plan["url"] == "https://doi.org/" + DOI
        and publisher_plan["observed_redirect"] == native["requests"]["doi"]
        and publisher_plan["url"] == PUBLISHER,
        "primary access plan changed",
    )
    publication["access"] = {
        "status": "PUBLISHER_HTTP403_HELD_NO_RETRY_OR_ALTERNATE_ROUTE",
        "fulltext_inspected": False,
        "manual_doi_redirects_followed": 1,
        "sources": sources,
        "revisit_requires_new_direction_or_supplied_copy": True,
    }
    claims = [c for c in prior["claims"] if c["aro_id"] in terms]
    records = [r for r in prior["records"] if r["identifier"] in {c["record_identifier"] for c in claims}]
    return {
        "date": "2026-10-15",
        "scope": SCOPE,
        "native_plan": reference.pin(root, root / PLAN),
        "plan": native["plan"],
        "prior": plan["prior"],
        "records": records,
        "claims": claims,
        "terms": terms,
        "reference_candidates": references,
        "cached_citation_queries": citation_queries,
        "taxonomy_source": taxonomy_source,
        "new_empty_symbol_queries": empty_queries,
        "reused_opmh_query": {
            "source": old_provenance,
            "result_count": 0,
            "complete_for_query": True,
            "biological_absence_inferred": False,
        },
        "excluded_citation_entry": {
            "accession": "UniProtKB:I0IYR3",
            "native_gene_symbol": "mexZ",
            "entry_sha256": mex.checksum(entries["I0IYR3"]),
            "reason": "REGULATOR_NAME_IS_NOT_A_LABEL_NAMED_MEXXY_OPRA_COMPONENT",
        },
        "publication": publication,
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read_in_prior_replay": 27,
            "selected_records": len(records),
            "selected_claims": len(claims),
            "selected_terms": len(terms),
            "cached_citation_queries_replayed": len(citation_queries),
            "citation_pool_entries": len(entries),
            "reference_candidates": len(references),
            "new_reference_candidates": sum(
                not r["already_in_prior_mex_dossier"] for r in references.values()
            ),
            "new_native_http_requests": 5,
            "new_taxonomy_requests": 0,
            "new_primary_access_holds": 1,
            "web_search_calls": 2,
            "underlying_web_http_request_count_known": False,
        },
        "limits": {
            **mex.LIMITS,
            "new_complex_membership_assignments": 0,
            "all_Mex_family_aliases_or_strains_searched": False,
        },
        "attribution": (
            "CARD/ARO and UniProt release 2026_03, CC BY 4.0; no primary article text redistributed."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build(args.root)
    if args.output:
        with args.output.open("x") as stream:
            stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
