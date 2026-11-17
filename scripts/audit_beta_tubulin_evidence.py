"""Trace beta-tubulin reference bibliographies and a cited paper's access hold."""

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

import audit_card_beta_tubulin_references as beta
from audit_valinomycin_abcb1 import planned_source
from lxml import html

reference, require = beta.reference, beta.require
CACHE = Path("reports/resistance-grounding-2026-10-14-banno-primary")
OUTPUT = Path("research/2026-10-14-beta-tubulin-evidence-followup.json")
SCOPE = "BETA_TUBULIN_REFERENCE_BIBLIOGRAPHY_AND_BANNO_ACCESS_NOT_PRIMARY_RESISTANCE_REVIEW"
COHORT_SHA = "eb36781d5bd14155c75cd8ebae190576c7ec891ae443be649849987948452552"
PLAN_SHA = "fea37da947fff35d1377894aee96b23572f2fab8efcbd5ce038b734b85b4457e"
PMID = "18944187"
DOI = "10.1094/phyto-98-4-0397"
DOI_URL = "https://doi.org/10.1094/PHYTO-98-4-0397"
ARTICLE = "https://apsjournals.apsnet.org/doi/10.1094/PHYTO-98-4-0397"
TERMS = {"ARO:3009320", "ARO:3009324"}
BODY_SHA = {
    "doi": "97614790787544e869f13eaa3a76459a7a24184299c19291c33c6a1c5864fae7",
    "publisher": "5a28ebd8a1c379b9a6fb928435de18d7abe4a9f6d772243e48cec3b782288f47",
}


def bibliography(entry):
    """Preserve reference metadata, never sequence positions or experimental claims."""
    rows, seen = [], set()
    for ref in entry.get("references", []):
        number, citation = ref["referenceNumber"], ref["citation"]
        require(type(number) is int and number > 0 and number not in seen, "invalid reference numbering")
        seen.add(number)
        kind = citation["citationType"]
        require(kind in {"journal article", "submission"}, "unreviewed citation type")
        title = citation.get("title")
        require(title is None or isinstance(title, str) and bool(title.strip()), "invalid citation title")
        require(kind != "journal article" or title, "journal article lacks a title")
        date = citation["publicationDate"]
        require(isinstance(date, str) and bool(date.strip()), "invalid native publication date")
        identifiers, issues = [], []
        for value in citation.get("citationCrossReferences", []):
            db, identifier = value["database"], value["id"]
            require(
                isinstance(db, str) and db and isinstance(identifier, str) and identifier,
                "invalid reference identifier",
            )
            identifiers.append({"database": db, "id": identifier})
            if db == "DOI" and not re.fullmatch(r"10\.\d{4,9}/\S+", identifier):
                issues.append(
                    {
                        "database": db,
                        "native_id": identifier,
                        "status": "MALFORMED_NATIVE_DOI_NOT_CORRECTED",
                        "replacement": None,
                    }
                )
        require(
            len({(i["database"], i["id"]) for i in identifiers}) == len(identifiers),
            "duplicate reference identifiers",
        )
        strains = []
        for comment in ref.get("referenceComments", []):
            if comment.get("type") == "STRAIN":
                value = comment["value"]
                require(isinstance(value, str) and value.strip(), "invalid native strain comment")
                strains.append(value)
        rows.append(
            {
                "native_reference_number": number,
                "native_citation_id": citation.get("id"),
                "citation_type": kind,
                "title": title,
                "publication_date": date,
                "submission_database": citation.get("submissionDatabase"),
                "identifiers": identifiers,
                "identifier_issues": issues,
                "reference_strain_comments": strains,
                "strain_comment_scope": "NATIVE_REFERENCE_METADATA_NOT_TESTED_RESISTANCE_SUBJECTS",
                "primary_results_reviewed": False,
                "experimental_subject_assignment": False,
                "resistance_inferred_from_citation": False,
            }
        )
    return rows


def project_hold(receipt, body):
    headers = {k.lower(): v for k, v in receipt.get("headers", {}).items()}
    require(
        receipt.get("url") == ARTICLE
        and receipt.get("status") == 403
        and receipt.get("retry_performed") is receipt.get("redirects_followed") is False
        and headers.get("cf-mitigated") == "challenge",
        "publisher hold scope changed",
    )
    tree = html.fromstring(body)
    require(
        tree.xpath("//title/text()") == ["Just a moment..."]
        and not tree.xpath("//meta[@name='citation_title']"),
        "challenge is not inspected article text",
    )
    return {
        "reference": "PMID:" + PMID,
        "doi": DOI,
        "status": "PUBLISHER_403_CHALLENGE_HELD_NO_RETRY",
        "url": ARTICLE,
        "retrieved_at": receipt["retrieved_at"],
        "http_status": 403,
        "article_obtained": False,
        "primary_results_reviewed": False,
        "retry_or_alternate_route_performed": False,
        "negative_biological_evidence": False,
        "global_inaccessibility_inferred": False,
        "paywall_inferred": False,
        "requires_new_direction_or_user_supplied_primary": True,
    }


def request_context(root, directory, cohort):
    for suffix in ("-attempt.json", "-receipt.json", "-response.bin"):
        require(
            {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} == {"doi", "publisher"},
            "unexpected request or alternate route",
        )
    plans = {
        name: json.loads((directory / name).read_bytes()) for name in ("doi-plan.json", "publisher-plan.json")
    }
    for name, plan in plans.items():
        key = "doi" if name == "doi-plan.json" else "publisher"
        require(
            plan["cohort"] == reference.pin(root, directory / "cohort.json")
            and set(plan["requests"]) == {key}
            and plan["canary_request"] == key
            and plan["automatic_redirects"] is plan["retry_performed"] is False
            and plan["ncbi_requests"] == 0,
            "bounded access plan changed",
        )
    require(
        plans["doi-plan.json"]["allowed_manual_redirect_host"] == "apsjournals.apsnet.org"
        and plans["publisher-plan.json"]["manual_redirect"] is True,
        "manual redirect policy changed",
    )
    sources = {
        key: planned_source(root, directory, key, filename, url, (status,))
        for key, filename, url, status in (
            ("doi", "doi-plan.json", DOI_URL, 302),
            ("publisher", "publisher-plan.json", ARTICLE, 403),
        )
    }
    receipts, attempts = {}, {}
    for key, source in sources.items():
        require(source["body"]["sha256"] == BODY_SHA[key], "inspected response bytes changed")
        receipts[key] = json.loads(reference.check_pin(root, source["receipt"]).read_bytes())
        attempts[key] = json.loads(reference.check_pin(root, source["attempt"]).read_bytes())
        require(
            datetime.fromisoformat(attempts[key]["started_at"])
            <= datetime.fromisoformat(receipts[key]["retrieved_at"]),
            "request timestamps reversed",
        )
    destination = [v for k, v in receipts["doi"]["headers"].items() if k.lower() == "location"]
    require(
        destination == [ARTICLE]
        and plans["publisher-plan.json"]["observed_redirect"] == sources["doi"]["receipt"]
        and datetime.fromisoformat(receipts["doi"]["retrieved_at"])
        <= datetime.fromisoformat(attempts["publisher"]["started_at"]),
        "publisher request lacks observed DOI route",
    )
    hold = project_hold(
        receipts["publisher"], reference.check_pin(root, sources["publisher"]["body"]).read_bytes()
    )
    return sources, hold


def check_scope(root, directory, cohort):
    for key in (
        "prior",
        "prior_verification",
        "census",
        "source_queue",
        "source_inventory",
        "definition_citations",
        "bibliography_source",
        "protected",
        "snapshots",
        "access_inventory",
    ):
        reference.check_pin(root, cohort[key])
    prior = json.loads((root / cohort["prior"]["path"]).read_bytes())
    receipt = json.loads((root / cohort["prior_verification"]["path"]).read_bytes())
    require(
        cohort["prior"] in receipt["files"] and receipt["summary"] == prior["summary"], "prior proof changed"
    )
    require(beta.build(root) == prior, "full native beta-tubulin dossier or current records changed")
    require(
        cohort["terms"] == {t: prior["terms"][t] for t in TERMS}
        and all(t["definition_citation_ids"] == ["PMID:" + PMID] for t in cohort["terms"].values())
        and cohort["reference_protein"] == prior["proteins"]["UniProtKB:P53373"],
        "Banno term scope changed",
    )
    ids = {i for t in cohort["terms"].values() for i in t["record_memberships"]}
    require(
        ids == {"CHEBI:3392", "CHEBI:4520"}
        and cohort["records"] == [r for r in prior["records"] if r["identifier"] in ids]
        and cohort["claims"] == [c for c in prior["claims"] if c["aro_id"] in TERMS],
        "Banno claim membership changed",
    )
    for row in cohort["records"]:
        snapshot = directory / (row["identifier"].replace(":", "-") + "-before.yaml")
        require(
            reference.digest(snapshot) == row["record_sha256"]
            and beta.load_record(root / row["path"]) == beta.load_record(snapshot),
            "Banno complete snapshot changed",
        )
    wrapper = json.loads((root / cohort["bibliography_source"]["path"]).read_bytes())
    require(
        wrapper["status"] == 200
        and hashlib.sha256(wrapper["body"].encode()).hexdigest() == wrapper["sha256"],
        "cached bibliography payload changed",
    )
    rows = [
        r
        for r in json.loads(wrapper["body"])["resultList"]["result"]
        if r.get("id") == PMID and r.get("source") == "MED"
    ]
    require(
        len(rows) == 1
        and {k: rows[0].get(k) for k in cohort["bibliography"]} == cohort["bibliography"]
        and rows[0]["doi"].lower() == DOI,
        "Banno bibliographic identity changed",
    )
    query = cohort["prior_citation_query"]
    _, provenance = beta.native.read_source(root, query)
    payload = json.loads(reference.check_pin(root, query["body"]).read_bytes())
    require(
        payload["results"] == [] and "lit_pubmed%3A18944187" in query["url"], "prior citation query changed"
    )
    return prior, {
        "source": provenance,
        "result_count": 0,
        "suggestions_followed": False,
        "zero_result_is_biological_absence": False,
        "paper_invalidated_by_zero_result": False,
    }


def project_bibliographies(entries, prior):
    require(set(entries) == set(prior["proteins"]), "full reference protein coverage changed")
    proteins = {}
    for accession, (entry, source) in sorted(entries.items()):
        old = prior["proteins"][accession]
        require(
            entry["primaryAccession"] == accession.removeprefix("UniProtKB:")
            and entry["entryAudit"]["entryVersion"] == old["entry_version"]
            and entry["entryAudit"]["sequenceVersion"] == old["sequence_version"]
            and entry["entryType"] == old["entry_type"]
            and f"NCBITaxon:{entry['organism']['taxonId']}" == old["reference_taxon_id"],
            "native reference identity differs from prior proof",
        )
        rows = bibliography(entry)
        filtered = []
        for row in rows:
            identifiers = sorted(
                {(i["database"], i["id"]) for i in row["identifiers"] if i["database"] in {"PubMed", "DOI"}}
            )
            if identifiers:
                filtered.append(
                    {
                        "identifiers": [{"database": db, "id": value} for db, value in identifiers],
                        "publication_date": row["publication_date"],
                        "primary_results_reviewed": False,
                    }
                )
        require(filtered == old["bibliography"], "identifier-bearing prior bibliography changed")
        proteins[accession] = {
            "entry_version": old["entry_version"],
            "sequence_version": old["sequence_version"],
            "reference_taxon_id": old["reference_taxon_id"],
            "reference_species_taxon_id": old["reference_species_taxon_id"],
            "source": source,
            "reference_rows": rows,
            "exact_resistant_allele_assignment": None,
            "experimental_subject_assignment": False,
            "experimental_genome_assignment": None,
        }
    terms = {}
    for tid, term in prior["terms"].items():
        accessions = [c["protein_accession"] for c in term["reference_candidates"]]
        matches = []
        for accession in accessions:
            for row in proteins[accession]["reference_rows"]:
                for identifier in row["identifiers"]:
                    curie = "PMID:" + identifier["id"] if identifier["database"] == "PubMed" else None
                    if curie in term["definition_citation_ids"]:
                        matches.append(
                            {
                                "protein_accession": accession,
                                "native_reference_number": row["native_reference_number"],
                                "source_citation": curie,
                            }
                        )
        terms[tid] = {
            "source_label": term["source_label"],
            "record_memberships": term["record_memberships"],
            "source_definition_citations": term["definition_citation_ids"],
            "reference_proteins": accessions,
            "own_citation_matches_in_reference_bibliographies": matches,
            "native_bibliography_is_experimental_crosswalk": False,
            "primary_review_status": "OPEN",
        }
    return proteins, terms


def build(root, directory=CACHE):
    directory = root / directory
    require(
        reference.digest(directory / "cohort.json") == COHORT_SHA
        and reference.digest(directory / "bibliography-plan.json") == PLAN_SHA,
        "frozen scope changed",
    )
    cohort = json.loads((directory / "cohort.json").read_bytes())
    prior, citation_query = check_scope(root, directory, cohort)
    sources, hold = request_context(root, directory, cohort)
    plan = json.loads((directory / "bibliography-plan.json").read_bytes())
    require(
        plan["cohort"] == reference.pin(root, directory / "cohort.json")
        and plan["prior"] == cohort["prior"]
        and plan["prior_verification"] == cohort["prior_verification"]
        and plan["reference_accessions"] == sorted(prior["proteins"])
        and plan["terms"] == sorted(prior["terms"])
        and plan["records"] == prior["records"]
        and plan["network_requests"] == 0
        and plan["primary_results_reviewed"] is plan["experimental_assignments"] is False,
        "complete offline bibliography plan changed",
    )
    native_sources = {}
    for term in prior["terms"].values():
        query = term["queries"].get("unreviewed", term["queries"]["reviewed"])
        source = query["source"]
        require(
            native_sources.setdefault(source["url"], source) == source, "inconsistent shared native query"
        )
    require(list(native_sources.values()) == plan["native_query_sources"], "native query coverage changed")
    entries = {}
    for source in native_sources.values():
        body, provenance = beta.native.read_source(root, source)
        for entry in body["results"]:
            accession = "UniProtKB:" + entry["primaryAccession"]
            if accession in prior["proteins"]:
                require(accession not in entries, "duplicate reference accession across queries")
                entries[accession] = (entry, provenance)
    proteins, terms = project_bibliographies(entries, prior)
    rows = [r for p in proteins.values() for r in p["reference_rows"]]
    return {
        "date": cohort["date"],
        "scope": SCOPE,
        "inputs": {
            **{
                k: cohort[k]
                for k in (
                    "prior",
                    "prior_verification",
                    "census",
                    "source_inventory",
                    "source_queue",
                    "definition_citations",
                    "bibliography_source",
                )
            },
            "cohort": reference.pin(root, directory / "cohort.json"),
            "bibliography_plan": reference.pin(root, directory / "bibliography-plan.json"),
        },
        "records": prior["records"],
        "claims": prior["claims"],
        "terms": terms,
        "proteins": proteins,
        "banno_followup": {
            "terms": sorted(TERMS),
            "claims": cohort["claims"],
            "metadata": cohort["bibliography"],
            "metadata_scope": "DATED_BIBLIOGRAPHY_NOT_PRIMARY_RESULTS_OR_GLOBAL_ACCESS_DECISION",
            "prior_uniprot_citation_query": citation_query,
            "request_sources": sources,
            "access_hold": hold,
            "reference_protein": "UniProtKB:P53373",
            "reference_taxon_id": "NCBITaxon:40559",
            "source_claims_corrected": False,
            "exact_allele_assignment": None,
            "primary_review_status": "OPEN",
        },
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(prior["records"]),
            "source_terms": len(terms),
            "source_claims": len(prior["claims"]),
            "reference_proteins": len(proteins),
            "native_reference_memberships": len(rows),
            "reference_types": dict(sorted(Counter(r["citation_type"] for r in rows).items())),
            "references_without_identifiers": sum(not r["identifiers"] for r in rows),
            "journal_references_without_identifiers": sum(
                not r["identifiers"] and r["citation_type"] == "journal article" for r in rows
            ),
            "native_identifier_issues": sum(len(r["identifier_issues"]) for r in rows),
            "terms_with_own_source_citation_matches": sum(
                bool(t["own_citation_matches_in_reference_bibliographies"]) for t in terms.values()
            ),
            "primary_access_terms": 2,
            "new_network_requests": 2,
            "new_primary_access_holds": 1,
            "new_primary_result_reviews": 0,
            "whole_record_primary_signoffs": 0,
        },
        "limitations": [
            "Reference bibliography memberships are not independent experimental observations "
            "or resistance support.",
            "Identifier-free journal references are retained; missing identifiers do not establish "
            "missing literature.",
            "A malformed native DOI remains uncorrected and is not followed as an inferred replacement.",
            "Reference strain comments are not tested resistance subjects, alleles or genome identifiers.",
            "No own-definition citation matched these reference bibliographies; "
            "that does not invalidate any paper.",
            "The publisher challenge was not solved, retried or bypassed; no primary article was obtained.",
            "Source organism, exact tested paralog, compound-specific phenotype "
            "and causal interpretation remain open.",
        ],
        "constraints": {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "source_adoptions": 0,
            "github_mutations": 0,
            "outreach": 0,
            "biological_writes": False,
            "held_sources_retried": False,
            "operational_sequence_variant_or_protocol_fields_exported": False,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": "CARD curation team, ARO CC BY 4.0; UniProt Consortium, release 2026_03, CC BY 4.0; "
        "Europe PMC bibliographic metadata. Publisher response retained privately as access evidence only.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        require(OUTPUT.read_bytes() == payload, "evidence follow-up does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
