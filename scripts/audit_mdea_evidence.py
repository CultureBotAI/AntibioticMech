"""Replay mdeA citation, species-name and empty protein queries without allele assignment."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode

import audit_card_grounding as card
import audit_card_literature_expansion as literature
import audit_card_named_taxa as named
import audit_card_protein_name_screen as screen
import audit_mex_component_references as common
from audit_mex_jkvw_evidence import project_metadata

from antibioticmech.activity_collections import load_record

reference, require = literature.reference, common.require
PREFIX = "research/2026-10-15-mdea-evidence"
PLAN = Path(PREFIX + "-native-plan.json")
OUTPUT = Path(PREFIX + ".json")
SCOPE = "MDEA_OWN_CITATION_REFERENCE_IDENTITY_NOT_EXPERIMENTAL_ALLELES"
TERM, PMID, NAME = "ARO:3007011", "23462018", "Streptococcus mutans"
DOI = "https://doi.org/10.4014/jmb.1301.01028"
PUBLISHER = "https://www.jmb.or.kr/journal/viewJournal.html?year=2013&vol=23&num=3&page=430"
KEYS = {"metadata-23462018", "doi-23462018", "taxonomy-name", "protein-reviewed", "protein-unreviewed"}


def current_context(root, plan):
    require(
        plan["scope"] == SCOPE and plan["term_id"] == TERM and plan["pmid"] == PMID, "selected cohort changed"
    )
    paths = {k: reference.check_pin(root, p) for k, p in plan["inputs"].items()}
    index = json.loads(paths["index"].read_bytes())
    screened = json.loads(paths["screen"].read_bytes())["terms"][TERM]
    require(
        screened == plan["term"]
        and screened["source_label"] == plan["source_label"] == "mdeA"
        and screened["definition_citation_ids"] == ["PMID:" + PMID]
        and not index["terms"][TERM]["links"],
        "source identity or reference status changed",
    )
    definitions = json.loads(paths["definition_citations"].read_bytes())["terms"][TERM]
    require(
        screen.checksum(definitions) == screened["definition_annotation_sha256"],
        "source definition annotation changed",
    )
    update = json.loads(paths["corpus_update"].read_bytes())
    deltas = {r["path"]: r for r in update["record_deltas"]}
    require(len(deltas) == len(update["record_deltas"]) == 3, "qualification deltas changed")
    with paths["census"].open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    paths_now = {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
    require(
        len(census) == len(paths_now) == len({r["identifier"] for r in census}) == 2939
        and {r["path"] for r in census} == paths_now
        and set(deltas) <= paths_now,
        "corpus membership changed",
    )
    for row in census:
        expected = row["record_sha256"]
        if row["path"] in deltas:
            delta = deltas[row["path"]]
            require(
                delta["identifier"] == row["identifier"] and delta["before_sha256"] == expected,
                "qualification delta binding changed",
            )
            expected = delta["after_sha256"]
        require(reference.digest(root / row["path"]) == expected, "current corpus bytes changed")
        row["record_sha256"] = expected
    records = [r for r in census if r["identifier"] in screened["record_memberships"]]
    claims = [c for c in index["claims"] if c["aro_id"] == TERM]
    actual = []
    for row in records:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "complete record identity changed",
        )
        for i, claim in screen.selected_claims(doc, {TERM}):
            require(claim["label"] == "mdeA", "claim label changed")
            actual.append((row["identifier"], i, screen.checksum(claim)))
    require(
        len(records) == len(claims) == len(actual) == 7
        and records == plan["records"]
        and claims == plan["claims"]
        and sorted(actual)
        == sorted((c["record_identifier"], c["resistance_index"], c["claim_sha256"]) for c in claims),
        "selected claim membership changed",
    )
    return records, claims


def native_http(root, native, key, url, status):
    receipt = common.read_json(root, native["requests"][key])
    attempt = common.read_json(root, native["attempts"][key])
    require(
        receipt["url"] == attempt["url"] == url
        and receipt["status"] == status
        and receipt["retries"] == receipt["redirects_followed"] == 0
        and attempt["retries"] == attempt["redirects_followed"] == attempt["ncbi_requests"] == 0,
        "native request identity, status or constraints changed",
    )
    path = reference.check_pin(root, receipt["body"])
    require(path.stat().st_size == receipt["bytes"], "native response size changed")
    return path.read_bytes(), {
        "receipt": native["requests"][key],
        "attempt": native["attempts"][key],
        **receipt,
    }


def failure_disposition(error):
    require(error == {"error_type": "ConnectionError", "retried": False}, "transport error changed")
    return {
        "status": "TRANSPORT_FAILURE_NO_HTTP_RESPONSE_NOT_AN_ACCESS_DENIAL",
        "http_status": None,
        "access_denial_established": False,
        "global_unavailability_inferred": False,
        "paywall_inferred": False,
        "fulltext_inspected": False,
        "retry_performed": False,
        "alternate_fulltext_route_requested": False,
    }


def protein_url(reviewed):
    return "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {
            "query": "gene_exact:mdeA AND taxonomy_id:1309 AND reviewed:" + str(reviewed).lower(),
            "format": "json",
            "size": "500",
            "sort": "accession asc",
            "fields": card.FIELDS,
        }
    )


def empty_query(body, source):
    headers = source["headers"]
    require(
        headers.get("x-uniprot-release") == "2026_03"
        and headers.get("x-total-results") == "0"
        and not headers.get("link")
        and not headers.get("location")
        and json.loads(body) == {"results": []},
        "new, incomplete or changed protein query requires review",
    )
    return {
        "source": source,
        "result_count": 0,
        "complete_for_exact_query": True,
        "establishes_biological_absence": False,
        "accession_assigned": None,
    }


def build(root):
    native = json.loads((root / PLAN).read_bytes())
    plan = common.read_json(root, native["plan"])
    records, claims = current_context(root, plan)
    require(
        set(native["requests"]) == KEYS and set(native["attempts"]) == KEYS | {"publisher-23462018"},
        "request coverage changed",
    )
    request_plans = {k: common.read_json(root, p) for k, p in native["request_plans"].items()}
    screen_plan = common.read_json(root, native["screen_plan"])
    prior = native["own_citation_query"]
    require(prior == screen_plan["queries"][PMID], "cached citation selection changed")
    entries, citation = literature.read_query(root, root / prior["directory"], PMID)
    require(
        not entries and citation == prior["query"] and citation["release"] == "2026_03",
        "own-citation query changed",
    )
    metadata_url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode(
        {"query": "EXT_ID:" + PMID + " AND SRC:MED", "format": "json", "resultType": "core", "pageSize": 1}
    )
    require(plan["metadata_url"] == metadata_url, "metadata route changed")
    metadata_body, metadata_source = native_http(root, native, "metadata-23462018", metadata_url, 200)
    metadata = project_metadata(json.loads(metadata_body), PMID, native["metadata_identity"])
    require(
        metadata["doi"] == DOI.removeprefix("https://doi.org/")
        and metadata["title"]
        == "Gene cloning and characterization of MdeA, a novel multidrug efflux pump in Streptococcus mutans."
        and metadata["pmcid"] is None
        and request_plans["doi"]["metadata"] == metadata_source["body"],
        "paper identity changed",
    )
    require(DOI in {r["url"] for r in metadata["indexed_fulltext_links"]}, "DOI missing from native metadata")
    _, doi_source = native_http(root, native, "doi-23462018", DOI, 302)
    require(
        request_plans["doi"]["url"] == DOI
        and doi_source["headers"]["location"] == PUBLISHER.replace("https://", "http://", 1)
        and request_plans["publisher"]["doi_receipt"] == native["requests"]["doi-23462018"]
        and request_plans["publisher"]["url"] == PUBLISHER
        and request_plans["publisher"]["transport_upgrade_to_https_before_first_publisher_request"] is True,
        "publisher route or transport upgrade changed",
    )
    failed = common.read_json(root, native["attempts"]["publisher-23462018"])
    require(
        failed["url"] == PUBLISHER and failed["retries"] == failed["redirects_followed"] == 0,
        "publisher attempt changed",
    )
    cache = (root / native["publisher_error"]["path"]).parent
    require(
        {p.name.removesuffix("-receipt.json") for p in cache.glob("*-receipt.json")} == KEYS
        and {p.name.removesuffix("-response.bin") for p in cache.glob("*-response.bin")} == KEYS
        and {p.name.removesuffix("-attempt.json") for p in cache.glob("*-attempt.json")}
        == KEYS | {"publisher-23462018"},
        "unexpected request, response or alternate route",
    )
    failure = failure_disposition(common.read_json(root, native["publisher_error"]))
    tax_url = "https://rest.uniprot.org/taxonomy/search?" + urlencode(named.parameters(NAME))
    tax_body, tax_source = native_http(root, native, "taxonomy-name", tax_url, 200)
    require(
        request_plans["taxonomy"]["url"] == tax_url
        and request_plans["taxonomy"]["metadata"] == metadata_source["body"],
        "taxon query owner changed",
    )
    resolved = named.resolve_name(
        NAME, {**tax_source, "body": tax_body.decode(), "sha256": hashlib.sha256(tax_body).hexdigest()}
    )
    require(
        resolved["status"] == "EXACT_SPECIES_NAME_RESOLVED"
        and resolved["named_organism_taxon_id"] == "NCBITaxon:1309"
        and resolved["release"] == "2026_03"
        and len(resolved["candidates"]) == 4,
        "species-name resolution changed",
    )
    queries = {}
    for kind in ("reviewed", "unreviewed"):
        query_plan = request_plans[kind]
        url = protein_url(kind == "reviewed")
        require(
            query_plan["url"] == url
            and query_plan["taxonomy"] == native["requests"]["taxonomy-name"]
            and query_plan["name_crosswalk"] == resolved,
            "protein query taxonomy binding changed",
        )
        body, source = native_http(root, native, "protein-" + kind, url, 200)
        queries[kind] = empty_query(body, source)
    require(
        request_plans["unreviewed"]["prior_reviewed_canary"] == native["requests"]["protein-reviewed"],
        "unreviewed fallback lacks reviewed canary",
    )
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": native["plan"],
        "native_plan": reference.pin(root, root / PLAN),
        "inputs": plan["inputs"],
        "term_id": TERM,
        "term": plan["term"],
        "records": records,
        "claims": claims,
        "metadata": {**metadata, "source": metadata_source},
        "cached_own_citation_query": citation,
        "publisher_attempt": {
            **failure,
            "doi": doi_source,
            "attempt": native["attempts"]["publisher-23462018"],
            "error": native["publisher_error"],
            "url": PUBLISHER,
            "http_to_https_upgrade_before_request": True,
        },
        "species_name_crosswalk": {
            **resolved,
            "source": tax_source,
            "evidence_scope": "INDEXED_STUDY_ORGANISM_NAME_NOT_EXPERIMENTAL_SUBJECT_IDENTITY",
            "experimental_organism_assignment": False,
            "strain_or_genome_assigned": False,
        },
        "protein_queries": queries,
        "reference_candidates": {},
        "study_context": {
            "indexed_donor_organism_name": NAME,
            "heterologous_test_context_reported": True,
            "native_organism_resistance_inferred": False,
            "primary_results_reviewed": False,
        },
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": 7,
            "source_claims": 7,
            "source_terms": 1,
            "exact_species_name_crosswalks": 1,
            "taxonomy_candidates_screened": 4,
            "new_reference_proteins": 0,
            "complete_empty_protein_queries": 2,
            "new_native_request_attempts": 6,
            "native_http_responses": 5,
            "publisher_transport_failures_without_http_status": 1,
            "new_confirmed_access_denials": 0,
        },
        "web_tools": native["web_tools"],
        "limits": {
            **common.LIMITS,
            "new_taxonomy_requests": 1,
            "new_uniprot_protein_requests": 2,
            "primary_fulltext_inspected": False,
            "exact_variant_or_operational_exports": False,
            "protein_absence_inferred": False,
            "name_match_to_another_species_accepted": False,
        },
        "attribution": (
            "CARD/ARO and UniProt2026_03, CC BY 4.0; Europe PMC metadata; primary text not redistributed."
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
