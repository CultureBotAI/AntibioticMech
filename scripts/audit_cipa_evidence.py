"""Replay cipA's held own-citation review without assigning homologs or subjects."""

import argparse
import csv
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode

import audit_card_definition_citations as definitions
import audit_card_literature_expansion as literature
import audit_card_outer_membrane_references as shared
from audit_valinomycin_abcb1 import planned_source
from lxml import html

from antibioticmech.activity_collections import load_record

reference, require = shared.reference, shared.require
CACHE = Path("reports/resistance-grounding-2026-10-15-cipa-evidence")
OUTPUT = Path("research/2026-10-15-cipa-evidence.json")
SCOPE = "CIPA_OWN_CITATION_ACCESS_HOLD_NOT_EXPERIMENTAL_OR_REFERENCE_PROTEIN_ASSIGNMENT"
TERM, PMID = "ARO:3003907", "23752511"
ARTICLE = "https://europepmc.org/articles/PMC3719738"
COHORT_SHA = "f4c3e7b8c95a33a4502a2f0f81cf97dbaf73d7efe6276e66d3354a19e405cfdc"
PLAN_SHA = {
    "metadata-plan.json": "f28736f183df821ae75d5ff8f53fbbd48b8934152c568972b1380185c9a98099",
    "primary-plan.json": "37827b3c20811111ec72eaf85856c35eb00e484d67b8ec7fb4cfe32bbf95c1c5",
}
BODY_SHA = {
    "metadata-23752511": "5e3a12d9ce2c6ffab94e6651a48f2d6b2b2dfd9d034bb95b4b8edb60672359f2",
    "primary": "b572d3f5860bcb6bf0b39b564c19a3e4667e0c458381f9c92582827e3ffa798d",
}
PUBLICATION = {
    "title": "Distinction between the Cfr methyltransferase conferring antibiotic resistance "
    "and the housekeeping RlmN methyltransferase.",
    "doi": "10.1128/aac.00448-13",
    "pmcid": "PMC3719738",
    "pubYear": "2013",
    "isOpenAccess": "N",
    "inEPMC": "Y",
}
ABSTRACT_SHA = "0b50b0f80946698eb8d32859277d345f5ce31a9a30d42f3b58e13881dd12a6cc"


def metadata_url():
    return "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode(
        {"query": "EXT_ID:" + PMID + " AND SRC:MED", "format": "json", "resultType": "core", "pageSize": 1}
    )


def project_metadata(payload):
    request, rows = payload["request"], payload["resultList"]["result"]
    require(
        type(payload["hitCount"]) is int
        and payload["hitCount"] == 1
        and len(rows) == 1
        and not payload.get("nextCursorMark")
        and request["queryString"] == "EXT_ID:" + PMID + " AND SRC:MED"
        and request["resultType"].lower() == "core"
        and type(request["pageSize"]) is int
        and request["pageSize"] == 1,
        "metadata query scope changed",
    )
    row = rows[0]
    require(
        row["id"] == row["pmid"] == PMID
        and row["source"] == "MED"
        and {k: row.get(k) for k in PUBLICATION} == PUBLICATION
        and hashlib.sha256(row["abstractText"].encode()).hexdigest() == ABSTRACT_SHA,
        "publication identity or inspected abstract changed",
    )
    links = [r for r in row["fullTextUrlList"]["fullTextUrl"] if r["url"] == ARTICLE]
    require(
        len(links) == 1 and links[0]["availability"] == "Free" and links[0]["documentStyle"] == "html",
        "metadata-advertised primary route changed",
    )
    matches = re.findall(r"\bcipa\b", row["abstractText"], re.I)
    require(not matches, "new literal cipA abstract mention requires review")
    return {
        "pmid": "PMID:" + PMID,
        **PUBLICATION,
        "abstract_sha256": ABSTRACT_SHA,
        "source_advertised_primary_link": links[0],
        "scope": "INDEXED_METADATA_NOT_PRIMARY_RESULTS",
        "abstract_context": "CFR_AND_RLMN_HOMOLOGY_DOES_NOT_ESTABLISH_SAME_RESISTANCE_FUNCTION",
        "literal_cipa_abstract_matches": len(matches),
        "literal_nonmatch_establishes_absence": False,
        "cfr_or_rlmn_assigned_as_cipa": False,
        "primary_results_reviewed": False,
        "non_oa_flag_is_global_access_denial": False,
    }


def project_hold(receipt, payload):
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    require(
        receipt["url"] == ARTICLE
        and receipt["status"] == 403
        and receipt["retry_performed"] is receipt["redirects_followed"] is False
        and headers.get("cf-mitigated") == "challenge"
        and hashlib.sha256(payload).hexdigest() == BODY_SHA["primary"],
        "primary access hold changed",
    )
    tree = html.fromstring(payload)
    require(
        tree.xpath("//title/text()") == ["Just a moment..."]
        and not tree.xpath('//meta[starts-with(@name,"citation_")]'),
        "response is not the inspected challenge",
    )
    return {
        "url": ARTICLE,
        "http_status": 403,
        "status": "PRIMARY_HTML_403_CHALLENGE_HELD_NO_RETRY_OR_ALTERNATE",
        "retrieved_primary_text": False,
        "challenge_treated_as_primary": False,
        "primary_results_reviewed": False,
        "retry_performed": False,
        "alternate_route_used": False,
        "hold_is_biological_negative_result": False,
        "metadata_free_flag_overrules_denial": False,
        "global_paywall_or_permanent_unavailability_inferred": False,
        "revisit_requires": "USER_SUPPLIED_PRIMARY_COPY_OR_NEW_EXPLICIT_DIRECTION",
    }


def request_context(root, directory):
    specs = [
        ("metadata-" + PMID, "metadata-plan.json", metadata_url(), 200),
        ("primary", "primary-plan.json", ARTICLE, 403),
    ]
    for suffix in ("-attempt.json", "-receipt.json", "-response.bin"):
        require(
            {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} == set(BODY_SHA),
            "unexpected request or alternate route",
        )
    for filename, sha in PLAN_SHA.items():
        require(reference.digest(directory / filename) == sha, "request plan changed")
        plan = json.loads((directory / filename).read_bytes())
        require(
            plan["cohort"] == reference.pin(root, directory / "cohort.json")
            and plan["automatic_redirects"] is plan["retry_performed"] is False
            and plan["ncbi_requests"] == 0
            and set(plan["requests"]) == {k for k, f, _, _ in specs if f == filename},
            "request constraints changed",
        )
    sources, end = {}, None
    for key, filename, url, status in specs:
        source = planned_source(root, directory, key, filename, url, (status,))
        require(source["body"]["sha256"] == BODY_SHA[key], "inspected response changed")
        attempt = json.loads(reference.check_pin(root, source["attempt"]).read_bytes())
        receipt = json.loads(reference.check_pin(root, source["receipt"]).read_bytes())
        start = datetime.fromisoformat(attempt["started_at"])
        require(end is None or end <= start, "request order changed")
        end = datetime.fromisoformat(receipt["retrieved_at"])
        require(start <= end, "request chronology changed")
        sources[key] = source
    canary = json.loads((directory / "metadata-canary-review.json").read_bytes())
    require(
        all(canary[k] == sources["metadata-" + PMID][k] for k in ("plan", "body", "receipt"))
        and canary["identity_checked"] is True
        and canary["primary_results_reviewed"] is canary["cfr_homology_is_cipa_identity"] is False,
        "metadata canary changed",
    )
    return sources


def corpus_context(root, cohort):
    for key in (
        "index",
        "previous_verification",
        "census",
        "source_inventory",
        "source_queue",
        "definition_citations",
        "ontology_cache",
        "literature",
        "protected",
        "access_inventory",
    ):
        reference.check_pin(root, cohort[key])
    index = json.loads(reference.check_pin(root, cohort["index"]).read_bytes())
    citations = json.loads(reference.check_pin(root, cohort["definition_citations"]).read_bytes())
    require(
        cohort["source_term_id"] == TERM
        and cohort["source_label"] == "cipA"
        and cohort["pmid"] == PMID
        and cohort["source_term"] == index["terms"][TERM]
        and not cohort["source_term"]["links"]
        and cohort["source_definition"] == citations["terms"][TERM]
        and cohort["source_definition"]["definition_citation_ids"] == ["PMID:" + PMID],
        "frozen term context changed",
    )
    with reference.check_pin(root, cohort["source_inventory"]).open() as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    labels = {r["determinant_id"]: r["determinant_name"] for r in rows}
    require(
        {t for t, label in labels.items() if label.casefold() == "cipa"} == {TERM}, "cipA label scope changed"
    )
    wrapper = json.loads(reference.check_pin(root, cohort["ontology_cache"]).read_bytes())
    body = wrapper["body"].encode()
    require(
        wrapper["status"] == 200
        and wrapper["bytes"] == len(body)
        and wrapper["sha256"] == hashlib.sha256(body).hexdigest(),
        "native ontology bytes changed",
    )
    projected = definitions.project_annotations(
        definitions.Graph().parse(data=body, format="xml"), {TERM: "cipA"}
    )[TERM]
    require(
        all(cohort["source_definition"][k] == v for k, v in projected.items()),
        "native source definition changed",
    )
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    require(
        len(census) == len({r["identifier"] for r in census}) == 2939
        and {r["path"] for r in census}
        == {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        and all(reference.digest(root / r["path"]) == r["record_sha256"] for r in census),
        "current corpus changed",
    )
    records = [r for r in census if r["identifier"] in cohort["source_term"]["record_memberships"]]
    claims = []
    for row in records:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "structure identity changed",
        )
        for position, claim in enumerate(doc.get("resistance_mechanisms", [])):
            if claim.get("aro_id") == TERM:
                require(claim["label"] == "cipA", "source claim label changed")
                claims.append(
                    {
                        "record_identifier": doc["identifier"],
                        "position": position,
                        "aro_id": TERM,
                        "claim_sha256": hashlib.sha256(
                            json.dumps(claim, sort_keys=True, ensure_ascii=True).encode()
                        ).hexdigest(),
                    }
                )
    require(
        records == cohort["records"] and claims == cohort["claims"] and len(records) == len(claims) == 10,
        "complete claim membership changed",
    )
    return records, claims


def build(root, directory=CACHE):
    directory = root / directory
    require(reference.digest(directory / "cohort.json") == COHORT_SHA, "frozen cohort changed")
    cohort = json.loads((directory / "cohort.json").read_bytes())
    records, claims = corpus_context(root, cohort)
    entries, query = literature.read_query(root, root / literature.DIRECTORY, PMID)
    require(
        not entries
        and query["complete_for_query"]
        and query["release"] == "2026_03"
        and json.loads(reference.check_pin(root, cohort["literature"]).read_bytes())
        == {"entries": entries, "query": query},
        "cached own-citation query changed",
    )
    sources = request_context(root, directory)
    metadata = project_metadata(json.loads((directory / ("metadata-" + PMID + "-response.bin")).read_bytes()))
    hold = project_hold(
        json.loads((directory / "primary-receipt.json").read_bytes()),
        (directory / "primary-response.bin").read_bytes(),
    )
    canary = json.loads((directory / "metadata-canary-review.json").read_bytes())
    require(
        metadata["source_advertised_primary_link"] == canary["source_advertised_primary_link"],
        "advertised route changed",
    )
    return {
        "date": cohort["date"],
        "scope": SCOPE,
        "inputs": {
            **{
                k: cohort[k]
                for k in (
                    "index",
                    "previous_verification",
                    "census",
                    "source_inventory",
                    "source_queue",
                    "definition_citations",
                    "ontology_cache",
                    "literature",
                )
            },
            "cohort": reference.pin(root, directory / "cohort.json"),
        },
        "source_term_id": TERM,
        "source_label": "cipA",
        "source_term": cohort["source_term"],
        "source_definition": cohort["source_definition"],
        "records": records,
        "claims": claims,
        "reused_literature_query": query,
        "publication": {**metadata, "source": sources["metadata-" + PMID]},
        "primary_access_hold": {**hold, "source": sources["primary"]},
        "request_sources": sources,
        "disposition": {
            "status": "CIPA_IDENTITY_UNRESOLVED_PRIMARY_ACCESS_HELD",
            "protein_accession_assigned": None,
            "taxon_id_assigned": None,
            "strain_taxon_id_assigned": None,
            "experimental_allele_assigned": None,
            "experimental_genome_assigned": None,
            "cfr_like_definition_is_exact_cfr_identity": False,
            "homologous_housekeeping_protein_substituted": False,
            "gene_query_without_resolved_source_organism_performed": False,
        },
        "summary": {
            "source_terms": 1,
            "source_claims": len(claims),
            "cohort_records": len(records),
            "corpus_records_hash_checked": 2939,
            "complete_collection_aware_records_read": len(records),
            "native_ontology_definition_replayed": True,
            "reused_complete_literature_queries": 1,
            "reference_candidates": 0,
            "primary_context_reviews": 0,
            "metadata_only_papers": 1,
            "new_verified_resistance_results": 0,
            "experimental_gene_allele_assignments": 0,
            "biological_records_changed": 0,
        },
        "constraints": {
            "network_requests": 2,
            "new_uniprot_requests": 0,
            "ncbi_requests": 0,
            "new_access_holds": 1,
            "retry_performed": False,
            "redirects_followed": False,
            "alternate_routes_used": False,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "source_adoptions": 0,
            "outreach": 0,
            "github_mutations": 0,
            "sequence_variant_protocol_exported": False,
            "full_corpus_goal_status": "OPEN",
        },
        "limitations": [
            "The own citation remains metadata-only; challenge content is not primary scientific evidence.",
            "Empty citation-query results and an abstract literal nonmatch "
            "do not establish biological absence.",
            "The Cfr-like source definition is not an exact gene, protein, organism "
            "or experimental-subject crosswalk.",
            "The citation's distinction between homologous enzyme classes "
            "precludes automatic function transfer.",
            "Primary Results, figures, tables, supplements, exact assays "
            "and whole-record signoffs remain open.",
        ],
        "attribution": "CARD/ARO ontology: McMaster University, CC BY 4.0. "
        "UniProt metadata: UniProt Consortium. "
        "Bibliographic metadata: Europe PMC at EBI. No primary article text redistributed or source adopted.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = (json.dumps(build(Path.cwd()), indent=2, sort_keys=True) + "\n").encode()
    if args.check or args.output.exists():
        require(args.output.read_bytes() == payload, "saved dossier does not reproduce")
    else:
        with args.output.open("xb") as stream:
            stream.write(payload)


if __name__ == "__main__":
    main()
