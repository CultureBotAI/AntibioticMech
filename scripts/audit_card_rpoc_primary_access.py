"""Preserve primary-access evidence without resolving rpoC resistance causality."""

import argparse
import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_rpo_references as prior
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

reference, require = prior.reference, prior.require
CACHE = Path("reports/resistance-grounding-2026-10-14-rpoc-primary")
OUTPUT = Path("research/2026-10-14-card-rpoc-primary-access.json")
COHORT_SHA = "7ddcae8ab222331573f0ad7a0382c16326ead4be42634b3ee24356ab4da96cd9"
SCOPE = "RPOC_PRIMARY_ACCESS_AND_UNRESOLVED_CLAIM_SCOPE_NOT_CAUSAL_REVIEW"
ARTICLE = "https://www.nature.com/articles/s41598-018-33731-1"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3553702/fullTextXML"
COOKIE = (
    "https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri="
    "https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41598-018-33731-1"
)
TERMS = {"ARO:3004994", "ARO:3004995"}


def location(headers):
    values = [v for k, v in headers.items() if k.casefold() == "location"]
    require(len(values) == 1 and isinstance(values[0], str), "missing or ambiguous redirect location")
    return values[0]


def redirect_context(receipt):
    require(
        receipt["status"] == 302
        and receipt["redirects_followed"] is False
        and receipt["manual_redirect_continuation"] is True
        and receipt["credentials_supplied"] is False,
        "publisher redirect state changed",
    )
    target = urlsplit(location(receipt["headers"]))
    parameters = parse_qs(target.query, keep_blank_values=True)
    require(
        target.scheme == "https"
        and target.netloc == "idp.nature.com"
        and target.path == "/transit"
        and not target.fragment
        and set(parameters) == {"redirect_uri", "code"}
        and parameters["redirect_uri"] == [ARTICLE]
        and len(parameters["code"]) == 1
        and bool(parameters["code"][0]),
        "unexpected publisher continuation identity",
    )
    return {
        "status": "UNRESOLVED_PUBLISHER_REDIRECT_FLOW",
        "observed_status_chain": [303, 302],
        "followed_destination_host": "idp.nature.com",
        "followed_destination_path": "/authorize",
        "unfollowed_destination_host": target.netloc,
        "unfollowed_destination_path": target.path,
        "unfollowed_query_keys": sorted(parameters),
        "unfollowed_redirect_uri_matches_article": True,
        "authorization_code_or_cookie_values_exported": False,
        "article_obtained": False,
        "access_denial_or_paywall_inferred": False,
        "credentials_supplied": False,
        "automatic_redirects": 0,
        "manual_redirect_requests": 1,
        "final_article_request_performed": False,
        "primary_results_reviewed": False,
    }


def request_context(root, directory, cohort):
    expected = {"article-23208709", "publisher-30337678", "publisher-cookie-flow"}
    for suffix in ("-attempt.json", "-receipt.json", "-response.bin"):
        require(
            {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} == expected,
            "request inventory changed or an unrequested route was used",
        )
    plans = {
        name: json.loads((directory / name).read_bytes())
        for name in ("primary-plan.json", "publisher-plan.json", "publisher-redirect-plan.json")
    }
    cohort_pin = reference.pin(root, directory / "cohort.json")
    require(all(p["cohort"] == cohort_pin for p in plans.values()), "request plan cohort changed")
    primary = plans["primary-plan.json"]
    require(
        set(primary["requests"]) == {"article-23208709", "article-30337678"}
        and primary["canary_request"] == "article-23208709"
        and primary["canary_required_before_batch"] is True,
        "primary canary scope changed",
    )
    for pmid, paper in cohort["bibliography"].items():
        item = primary["requests"]["article-" + pmid]
        require(
            all(item[k] == paper[k] for k in ("pmid", "pmcid", "doi"))
            and item["url"]
            == "https://www.ebi.ac.uk/europepmc/webservices/rest/" + paper["pmcid"] + "/fullTextXML",
            "planned primary publication changed",
        )
    sources = {
        "article-23208709": planned_source(
            root, directory, "article-23208709", "primary-plan.json", EPMC, (500,)
        ),
        "publisher-30337678": planned_source(
            root, directory, "publisher-30337678", "publisher-plan.json", ARTICLE, (303,)
        ),
        "publisher-cookie-flow": planned_source(
            root, directory, "publisher-cookie-flow", "publisher-redirect-plan.json", COOKIE, (302,)
        ),
    }
    stop_path = directory / "primary-canary-stop.json"
    stop = json.loads(stop_path.read_bytes())
    require(
        stop["plan"] == sources["article-23208709"]["plan"]
        and stop["receipt"] == sources["article-23208709"]["receipt"]
        and stop["held_pmid"] == "23208709"
        and stop["unrequested_pmid"] == "30337678"
        and stop["unrequested_route"] == "EUROPE_PMC_FULLTEXT"
        and stop["status"] == "HTTP_500_TECHNICAL_HOLD_NO_RETRY"
        and stop["primary_results_reviewed"] is stop["biological_absence_inferred"] is False,
        "failed primary canary stop changed",
    )
    require(
        plans["publisher-plan.json"]["prior_canary_stop"] == reference.pin(root, stop_path)
        and set(plans["publisher-plan.json"]["requests"]) == {"publisher-30337678"}
        and plans["publisher-plan.json"]["held_first_paper_retried"] is False,
        "independent publisher request scope changed",
    )
    redirect_plan = plans["publisher-redirect-plan.json"]
    require(
        redirect_plan["observed_redirect_receipt"] == sources["publisher-30337678"]["receipt"]
        and set(redirect_plan["requests"]) == {"publisher-cookie-flow", "publisher-article-flow"}
        and redirect_plan["requests"]["publisher-article-flow"]["url"] == ARTICLE
        and redirect_plan["max_requests"] == 2
        and redirect_plan["held_pmid_23208709_retried"] is False
        and redirect_plan["credentials_supplied"] is False,
        "bounded publisher continuation changed",
    )
    receipts = {
        key: json.loads(reference.check_pin(root, source["receipt"]).read_bytes())
        for key, source in sources.items()
    }
    times = [datetime.fromisoformat(receipts[key]["retrieved_at"]) for key in sources]
    require(times == sorted(times) and len(set(times)) == 3, "request chronology changed")
    error = json.loads(reference.check_pin(root, sources["article-23208709"]["body"]).read_bytes())
    require(
        error.get("status") == 500
        and error.get("error") == "Internal Server Error"
        and error.get("path") == "/europepmc/webservices/rest/PMC3553702/fullTextXML",
        "technical error payload changed",
    )
    require(
        location(receipts["publisher-30337678"]["headers"]) == COOKIE, "observed publisher redirect changed"
    )
    require(
        reference.check_pin(root, sources["publisher-cookie-flow"]["body"]).read_bytes() == b"",
        "redirect body changed",
    )
    return sources, {
        "PMID:23208709": {
            "status": "TECHNICAL_HTTP_500_HOLD",
            "http_status": 500,
            "article_obtained": False,
            "primary_results_reviewed": False,
            "retry_or_alternate_route_performed": False,
            "negative_biological_evidence": False,
        },
        "PMID:30337678": redirect_context(receipts["publisher-cookie-flow"]),
    }


def check_scope(root, directory, cohort):
    for key in (
        "prior",
        "prior_verification",
        "census",
        "source_queue",
        "bibliography_archive",
        "source_inventory",
        "definition_citations",
        "protected",
        "snapshots",
        "access_inventory",
    ):
        reference.check_pin(root, cohort[key])
    previous = json.loads((root / cohort["prior"]["path"]).read_bytes())
    receipt = json.loads((root / cohort["prior_verification"]["path"]).read_bytes())
    require(
        cohort["prior"] in receipt["files"] and receipt["summary"] == previous["summary"],
        "prior reference proof changed",
    )
    require(
        cohort["terms"] == {tid: previous["terms"][tid] for tid in TERMS}, "selected term context changed"
    )
    require(
        set(cohort["bibliography"]) == {"23208709", "30337678"}
        and cohort["terms"]["ARO:3004994"]["definition_citation_ids"] == ["PMID:23208709", "PMID:30337678"]
        and cohort["terms"]["ARO:3004995"]["definition_citation_ids"] == []
        and cohort["terms"]["ARO:3004995"]["source_organism_name"] is None,
        "definition citation or unresolved-organism scope changed",
    )
    with (root / cohort["census"]["path"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    require(
        len(census) == len({r["identifier"] for r in census}) == 2939
        and {r["path"] for r in census}
        == {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        and all(reference.digest(root / r["path"]) == r["record_sha256"] for r in census),
        "complete corpus census changed",
    )
    ids = {rid for term in cohort["terms"].values() for rid in term["record_memberships"]}
    require(ids == {"CHEBI:28077", "CHEBI:45367"}, "compound membership changed")
    require([r for r in census if r["identifier"] in ids] == cohort["records"], "record identities changed")
    claims = []
    for row in cohort["records"]:
        document = load_record(root / row["path"])
        snapshot = directory / (row["identifier"].replace(":", "-") + "-before.yaml")
        require(
            document == load_record(snapshot)
            and reference.digest(snapshot) == row["record_sha256"]
            and document["identifier"] == row["identifier"]
            and document["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "complete selected record changed",
        )
        for position, claim in enumerate(document.get("resistance_mechanisms", [])):
            if claim.get("aro_id") in TERMS:
                claims.append(
                    {
                        "record_identifier": row["identifier"],
                        "position": position,
                        "aro_id": claim["aro_id"],
                        "claim_sha256": hashlib.sha256(
                            json.dumps(claim, sort_keys=True, ensure_ascii=True).encode()
                        ).hexdigest(),
                    }
                )
    require(claims == cohort["claims"] and len(claims) == 4, "claim content or positions changed")
    return previous


def build(root, directory=CACHE):
    directory = root / directory
    require(reference.digest(directory / "cohort.json") == COHORT_SHA, "frozen primary review scope changed")
    cohort = json.loads((directory / "cohort.json").read_bytes())
    previous = check_scope(root, directory, cohort)
    sources, access = request_context(root, directory, cohort)
    return {
        "date": "2026-10-14",
        "scope": SCOPE,
        "inputs": {
            k: cohort[k]
            for k in (
                "prior",
                "prior_verification",
                "census",
                "source_inventory",
                "source_queue",
                "definition_citations",
                "bibliography_archive",
                "access_inventory",
            )
        },
        "cohort": reference.pin(root, directory / "cohort.json"),
        "request_sources": sources,
        "bibliographic_metadata_not_primary_results": cohort["bibliography"],
        "access_states": access,
        "records": cohort["records"],
        "claims": cohort["claims"],
        "term_contexts": {
            tid: {
                "source_label": term["source_label"],
                "definition_citation_ids": term["definition_citation_ids"],
                "record_memberships": term["record_memberships"],
                "named_reference_taxon_id": term["named_reference_taxon_id"],
                "reference_protein_candidates": [
                    c["protein_accession"] for c in term["reference_candidates"]
                ],
                "primary_review_status": "OPEN",
                "source_claim_corrected": False,
                "experimental_subject_assignment": False,
                "exact_resistant_allele": None,
                "experimental_genome_assignment": None,
            }
            for tid, term in cohort["terms"].items()
        },
        "prior_causal_review_flag": previous["primary_review_flags"]["ARO:3004994"],
        "pending_review_requirements": [
            "Inspect both cited primary results and relevant supplements "
            "before adjudicating the source claim.",
            "Distinguish compensation, co-occurrence and direct resistance causality.",
            "Verify exact compound scope separately for rifampicin and rifabutin; "
            "class membership is not evidence.",
            "Do not assign the unnamed generic term an organism or borrow the named term's citations.",
            "Keep reference proteins and taxa separate from tested alleles, isolates and genomes.",
        ],
        "summary": {
            "corpus_records_hash_checked": 2939,
            "source_terms": 2,
            "source_assertions": 4,
            "source_records": 2,
            "cited_publications": 2,
            "primary_articles_obtained": 0,
            "new_primary_result_reviews": 0,
            "http_status_counts": {"500": 1, "303": 1, "302": 1},
            "manual_redirect_requests": 1,
            "automatic_redirects": 0,
            "biological_records_changed": 0,
            "whole_record_primary_signoffs": 0,
        },
        "constraints": {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "prior_primary_holds_preserved": True,
            "held_first_paper_retried": False,
            "publisher_article_return_and_Europe_PMC_second_route_unrequested": True,
            "error_or_redirect_is_negative_biological_evidence": False,
            "source_adoptions": 0,
            "github_mutations": 0,
            "outreach": 0,
            "sequences_variants_protocols_or_numeric_AST_exported": False,
            "authorization_codes_or_cookie_values_exported": False,
            "full_corpus_goal_status": "OPEN",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        require(OUTPUT.read_bytes() == payload, "primary-access checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
