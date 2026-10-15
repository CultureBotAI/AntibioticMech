"""Replay MexJK/MexVW citation context without upgrading abstract-level evidence."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_mex_citation_followup as followup

reference, require = followup.reference, followup.require
PREFIX = "research/2026-10-15-mex-jkvw-evidence"
PLAN = Path(PREFIX + "-native-plan.json")
OUTPUT = Path(PREFIX + ".json")
SCOPE = "MEXJK_MEXVW_OWN_CITATION_IDENTITY_CONTEXT_NOT_EXPERIMENTAL_ALLELE_ASSIGNMENTS"
PMIDS = ["12193619", "12951344", "15855505", "15855547"]
COMPLEXES = {"MexJK", "MexJK-OpmH", "MexJK-OprM", "MexVW-OprM"}
PRIMARY = "https://europepmc.org/articles/PMC135324"
VW_DOI = "https://doi.org/10.1093/jac/dkg390"
VW_PUBLISHER = "https://academic.oup.com/jac/article-lookup/doi/10.1093/jac/dkg390"


def project_metadata(payload, pmid, expected):
    request = payload["request"]
    require(
        type(payload["hitCount"]) is int
        and payload["hitCount"] == 1
        and len(payload["resultList"]["result"]) == 1
        and not payload.get("nextCursorMark")
        and request["queryString"] == "EXT_ID:" + pmid + " AND SRC:MED"
        and request["resultType"] == "CORE"
        and type(request["pageSize"]) is int
        and request["pageSize"] == 1,
        "publication query scope changed",
    )
    (row,) = payload["resultList"]["result"]
    require(row["id"] == row["pmid"] == pmid and row["source"] == "MED", "publication identity changed")
    projected = {k: row.get(k) for k in ("pmid", "doi", "pmcid", "title", "isOpenAccess", "inEPMC")}
    projected["abstract_sha256"] = hashlib.sha256(row["abstractText"].encode()).hexdigest()
    require(projected == expected, "inspected publication metadata or abstract changed")
    return {
        **projected,
        "indexed_fulltext_links": row["fullTextUrlList"]["fullTextUrl"],
        "evidence_scope": "INDEXED_METADATA_AND_ABSTRACT_NOT_PRIMARY_RESULTS_REVIEW",
        "exact_experimental_gene_or_protein_identity_established": False,
        "source_claims_reinterpreted_from_abstract": False,
        "index_access_flags_are_not_global_access_or_reuse_decisions": True,
    }


def access_disposition(pmid, primary_sources):
    if pmid in {"15855505", "15855547"}:
        require(pmid not in primary_sources, "unrequested paper has a primary response")
        return {
            "status": "NOT_REQUESTED_AFTER_EUROPE_PMC_PRIMARY_CANARY_DENIAL",
            "access_denial_inferred": False,
            "fulltext_inspected": False,
            "global_unavailability_inferred": False,
        }
    require(
        pmid in {"12193619", "12951344"} and primary_sources[pmid]["status"] == 403,
        "hold requires the selected paper's HTTP 403 response",
    )
    return {
        "status": "HTTP403_ACCESS_HOLD_NO_RETRY_OR_ALTERNATE_ROUTE",
        "source": primary_sources[pmid],
        "fulltext_inspected": False,
        "global_unavailability_inferred": False,
        "requires_new_direction_or_supplied_copy": True,
    }


def build(root):
    native = json.loads((root / PLAN).read_bytes())
    plan = followup.mex.read_json(root, native["plan"])
    require(plan["scope"] == SCOPE and plan["pmids"] == PMIDS, "scope changed")
    prior = followup.mex.read_json(root, native["prior_followup"])
    require(followup.build(root) == prior, "current corpus or prior native replay changed")
    component_prior = followup.mex.read_json(root, plan["prior"])
    require(prior["prior"] == plan["prior"], "reference checkpoint differs")
    selected = {t: r for t, r in prior["terms"].items() if r["complex_label"] in COMPLEXES}
    require(
        sorted(selected) == plan["terms"]
        and len(selected) == 4
        and sorted({p[5:] for t in selected.values() for p in t["definition_citation_ids"]}) == PMIDS,
        "complete selected cohort changed",
    )
    expected_requests = {"metadata-" + p for p in PMIDS} | {
        "primary-12193619",
        "primary-12951344",
        "doi-12951344",
    }
    require(
        set(native["requests"]) == expected_requests and native["primary_unrequested"] == PMIDS[2:],
        "request coverage or unrequested disposition changed",
    )
    publications, metadata_sources = {}, {}
    for pmid in PMIDS:
        url = plan["metadata_urls"][pmid]
        parsed = urlsplit(url)
        require(
            parsed.scheme == "https"
            and parsed.netloc == "www.ebi.ac.uk"
            and parsed.path == "/europepmc/webservices/rest/search"
            and not parsed.fragment
            and parse_qs(parsed.query)
            == {
                "query": ["EXT_ID:" + pmid + " AND SRC:MED"],
                "format": ["json"],
                "resultType": ["core"],
                "pageSize": ["1"],
            },
            "metadata endpoint identity changed",
        )
        body, metadata_sources[pmid] = followup.native_http(
            root, native["requests"]["metadata-" + pmid], url, 200
        )
        publications[pmid] = project_metadata(json.loads(body), pmid, native["metadata_identities"][pmid])
    canary = followup.mex.read_json(root, native["metadata_canary"])
    require(
        canary["accepted"] is True and canary["body"] == metadata_sources[PMIDS[0]]["body"],
        "metadata canary not inspected",
    )
    access_plans = {k: followup.mex.read_json(root, p) for k, p in native["access_plans"].items()}
    require(
        access_plans["primary-canary-plan.json"]["url"] == PRIMARY
        and access_plans["primary-canary-plan.json"]["metadata"] == metadata_sources["12193619"]["body"]
        and access_plans["vw-primary-plan.json"]["url"] == VW_DOI
        and access_plans["vw-primary-plan.json"]["metadata"] == metadata_sources["12951344"]["body"]
        and access_plans["vw-publisher-plan.json"]["url"] == VW_PUBLISHER
        and access_plans["vw-publisher-plan.json"]["doi_response"] == native["requests"]["doi-12951344"],
        "primary routes differ from inspected plans",
    )
    require(
        PRIMARY in {r["url"] for r in publications["12193619"]["indexed_fulltext_links"]}
        and VW_DOI in {r["url"] for r in publications["12951344"]["indexed_fulltext_links"]},
        "primary routes absent from selected publication metadata",
    )
    _, doi_source = followup.native_http(root, native["requests"]["doi-12951344"], VW_DOI, 302)
    require(doi_source["headers"]["location"] == VW_PUBLISHER, "DOI redirect target changed")
    primary_sources = {}
    for pmid, url in (("12193619", PRIMARY), ("12951344", VW_PUBLISHER)):
        _, primary_sources[pmid] = followup.native_http(root, native["requests"]["primary-" + pmid], url, 403)
        require(not primary_sources[pmid]["headers"].get("location"), "unexpected primary redirect")
    for pmid, row in publications.items():
        row["metadata_source"] = metadata_sources[pmid]
        row["access"] = access_disposition(pmid, primary_sources)
    publications["12951344"]["doi_redirect"] = doi_source
    publications["15855505"]["regulator_citation_limit"] = (
        "The indexed title concerns MexL regulation; it is not an exact OpmH or MexJ/MexK protein crosswalk."
    )
    terms = {
        tid: {
            **row,
            "publication_pointers": ["/publications/" + p[5:] for p in row["definition_citation_ids"]],
            "experimental_accession_assignment": None,
            "curation_supported_by_this_pass": False,
        }
        for tid, row in sorted(selected.items())
    }
    claims = [c for c in prior["claims"] if c["aro_id"] in terms]
    records = [r for r in prior["records"] if r["identifier"] in {c["record_identifier"] for c in claims}]
    require(len(claims) == 8 and len(records) == 5, "claim or record membership changed")
    return {
        "date": "2026-10-15",
        "scope": SCOPE,
        "plan": native["plan"],
        "native_plan": reference.pin(root, root / PLAN),
        "prior_followup": native["prior_followup"],
        "terms": terms,
        "records": records,
        "claims": claims,
        "publications": publications,
        "reference_context": {
            "prior_component_dossier": plan["prior"],
            "taxonomy_sources": component_prior["taxonomy_sources"],
            "new_reference_or_experimental_taxon_assignments": 0,
        },
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read_in_prior_replay": 27,
            "selected_terms": 4,
            "selected_claims": 8,
            "selected_records": 5,
            "own_citations_metadata_inspected": 4,
            "confirmed_primary_access_holds": 2,
            "primary_papers_not_requested": 2,
            "new_reference_candidates": 0,
            "new_native_http_requests": 7,
            "web_reader_calls": 2,
            "underlying_web_http_request_count_known": False,
        },
        "limits": {
            **followup.mex.LIMITS,
            "new_uniprot_requests": 0,
            "new_taxonomy_requests": 0,
            "manual_doi_redirects_followed": 1,
            "exact_variant_or_operational_exports": False,
            "copies_requested_from_user": True,
        },
        "attribution": (
            "CARD/ARO and UniProt release 2026_03, CC BY 4.0; primary article text not redistributed."
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
