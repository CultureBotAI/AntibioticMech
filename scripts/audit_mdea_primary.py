"""Replay mdeA reference-identity follow-up without promoting transcription or search controls."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlencode

import audit_mdea_evidence as prior_audit

common, reference, require = prior_audit.common, prior_audit.reference, prior_audit.require
PREFIX = "research/2026-10-15-mdea-primary"
PLAN = Path(PREFIX + "-native-plan.json")
OUTPUT = Path(PREFIX + ".json")
SCOPE = "MDEA_PRIMARY_IDENTITY_FOLLOWUP_NOT_EXPERIMENTAL_ALLELE_ASSIGNMENT"
DOI = "10.4014/jmb.1301.01028"
CROSSREF = "https://api.crossref.org/works/10.4014%2Fjmb.1301.01028"
PDF = "https://pdf.medrang.co.kr/JMB2/2013/023/JMB023-03-20_FDOC_1.pdf"
SOURCE = (
    "https://www.researchgate.net/publication/235796115_Gene_Cloning_and_Characterization_of_"
    "MdeA_a_Novel_Multidrug_Efflux_Pump_in_Streptococcus_mutans"
)
KEYS = {"crossref", "reference", "locus", "taxonomy-control"}


def query_parameters(key):
    require(key in {"reference", "locus", "taxonomy-control"}, "unplanned query")
    queries = {
        "reference": "xref:refseq-NP_722397*",
        "locus": "gene:SMU_2109* AND taxonomy_id:1309",
        "taxonomy-control": "taxonomy_id:1309",
    }
    fields = prior_audit.card.FIELDS
    if key != "taxonomy-control":
        fields += ",xref_refseq"
    if key == "locus":
        fields += ",xref_embl"
    return {
        "query": queries[key],
        "format": "json",
        "size": "1" if key == "taxonomy-control" else "100",
        "sort": "accession asc",
        "fields": fields,
    }


def query_url(key):
    return "https://rest.uniprot.org/uniprotkb/search?" + urlencode(query_parameters(key))


def project_crossref(payload):
    require(payload["status"] == "ok" and payload["message-type"] == "work", "Crossref response changed")
    work = payload["message"]
    expected_link = {
        "URL": PDF,
        "content-type": "unspecified",
        "content-version": "vor",
        "intended-application": "similarity-checking",
    }
    require(
        work["DOI"] == DOI
        and work["title"]
        == [
            "Gene Cloning and Characterization of MdeA, a Novel Multidrug Efflux Pump in Streptococcus mutans"
        ]
        and work["resource"]["primary"]["URL"] == prior_audit.PUBLISHER.replace("https://", "http://", 1)
        and work["link"] == [expected_link],
        "registered paper identity or links changed",
    )
    return {
        "doi": work["DOI"],
        "registered_article_url": work["resource"]["primary"]["URL"],
        "registered_pdf_link": expected_link,
        "registration_is_access_or_redistribution_permission": False,
    }


def validate_assessment(notes):
    require(
        notes["source_url"] == SOURCE
        and notes["doi"] == DOI
        and notes["pmid"] == "23462018"
        and notes["source_kind"] == "AUTHOR_UPLOADED_WEB_TEXT_NOT_VISUAL_PDF_VERIFICATION"
        and notes["reference_accession"] == "NP_722397"
        and notes["reference_namespace"] == "RefSeq"
        and notes["paper_reference_locus_label"] == "SMU 2109"
        and notes["paper_gene_label"] == "mdeA"
        and notes["reference_strain_label"] == "UA159"
        and notes["paper_donor_strain_labels"] == ["KCTC 3065", "ATCC 25175"]
        and notes["paper_reports_sequence_identity_to_reference"] is True
        and notes["heterologous_test_context_kept_separate"] is True,
        "primary identity context changed",
    )
    false_keys = (
        "accession_version_reported",
        "donor_is_reference_strain",
        "sequence_comparison_independently_performed",
        "other_table_homologs_selected_as_experimental_identity",
        "exact_experimental_accession_assigned",
        "figures_visually_reviewed",
        "table_layout_visually_verified",
        "whole_paper_signoff",
        "sequence_variant_construct_protocol_exports",
        "numeric_ast_exported",
        "ncbi_links_followed",
        "author_contacted",
    )
    require(all(notes[k] is False for k in false_keys), "reference identity or review scope was promoted")
    require(
        set(notes["locations"])
        == {
            "identity",
            "reference_alias",
            "reference_accession",
            "donor_distinction",
            "heterologous_context",
        },
        "inspected location scope changed",
    )


def project_control(body, source):
    headers = source["headers"]
    payload = json.loads(body)
    require(
        headers["x-uniprot-release"] == "2026_03"
        and headers["x-total-results"] == "2451"
        and not headers.get("location")
        and set(payload) == {"results"}
        and len(payload["results"]) == 1,
        "taxonomy control identity or result count changed",
    )
    next_params = prior_audit.card.next_page(headers.get("link", ""), query_parameters("taxonomy-control"))
    require(next_params is not None, "partial control unexpectedly lacks remaining pages")
    (entry,) = payload["results"]
    require(
        not {"sequence", "features"} & set(entry)
        and entry["primaryAccession"] == "A0A090AX29"
        and entry["organism"]["taxonId"] == 1309
        and entry["organism"]["scientificName"] == "Streptococcus mutans",
        "control protein changed",
    )
    return {
        "source": source,
        "declared_result_count": 2451,
        "entries_inspected": 1,
        "complete_for_query": False,
        "pagination_followed": False,
        "control_accession": "UniProtKB:A0A090AX29",
        "selected_as_mdea_candidate": False,
        "supports_species_query_retrieval_not_target_gene_identity": True,
    }


def build(root):
    native = json.loads((root / PLAN).read_bytes())
    plan = common.read_json(root, native["plan"])
    require(
        plan["scope"] == SCOPE
        and plan["crossref_url"] == CROSSREF
        and plan["prior_failure_is_confirmed_access_denial"] is False,
        "follow-up scope changed",
    )
    prior = common.read_json(root, plan["prior"])
    require(prior_audit.build(root) == prior, "prior evidence or current corpus changed")
    require(
        set(native["requests"]) == KEYS and set(native["attempts"]) == KEYS | {"primary-pdf"},
        "request coverage changed",
    )
    plans = {k: common.read_json(root, p) for k, p in native["request_plans"].items()}
    notes = common.read_json(root, native["assessment"])
    validate_assessment(notes)
    body, crossref_source = prior_audit.native_http(root, native, "crossref", CROSSREF, 200)
    registered = project_crossref(json.loads(body))
    require(
        plans["pdf"]["crossref"] == native["requests"]["crossref"]
        and plans["pdf"]["native_link"] == registered["registered_pdf_link"]
        and plans["pdf"]["url"] == PDF,
        "PDF route differs from registered source",
    )
    failure = prior_audit.failure_disposition(common.read_json(root, native["pdf_error"]))
    failure["alternate_fulltext_route_requested"] = True
    failure["primary_identity_text_available_via_separate_author_copy"] = True
    attempt = common.read_json(root, native["attempts"]["primary-pdf"])
    require(
        attempt["url"] == PDF
        and attempt["retries"] == attempt["redirects_followed"] == attempt["ncbi_requests"] == 0,
        "PDF attempt constraints changed",
    )
    cache = (root / native["pdf_error"]["path"]).parent
    for suffix, expected in (
        ("-receipt.json", KEYS),
        ("-response.bin", KEYS),
        ("-attempt.json", KEYS | {"primary-pdf"}),
        ("-error.json", {"primary-pdf"}),
    ):
        require(
            {p.name.removesuffix(suffix) for p in cache.glob("*" + suffix)} == expected,
            "unexpected request, error or alternate native route",
        )
    queries = {}
    for key in ("reference", "locus", "taxonomy-control"):
        require(plans[key]["url"] == query_url(key), "planned query changed")
        body, source = prior_audit.native_http(root, native, key, query_url(key), 200)
        queries[key] = (
            project_control(body, source)
            if key == "taxonomy-control"
            else prior_audit.empty_query(body, source)
        )
    require(
        plans["reference"]["assessment"] == plans["locus"]["assessment"] == native["assessment"]
        and plans["locus"]["refseq_query"] == native["requests"]["reference"]
        and plans["locus"]["taxonomy_source"]
        == plans["taxonomy-control"]["taxonomy_source"]
        == plan["prior"],
        "query evidence bindings changed",
    )
    require(
        native["web_tools"]["author_text_read"] is True
        and native["web_tools"]["author_pdf_click_status"] == 404
        and native["web_tools"]["author_fulltext_native_body_cached"] is False
        and native["web_tools"]["figures_or_pdf_visually_inspected"] is False,
        "web review scope changed",
    )
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": native["plan"],
        "native_plan": reference.pin(root, root / PLAN),
        "prior": plan["prior"],
        "assessment": native["assessment"],
        "primary_identity_assessment": notes,
        "registered_source": {**registered, "source": crossref_source},
        "publisher_pdf_attempt": {
            **failure,
            "url": PDF,
            "attempt": native["attempts"]["primary-pdf"],
            "error": native["pdf_error"],
        },
        "queries": queries,
        "reference_candidates": {},
        "term": prior["term"],
        "records": prior["records"],
        "claims": prior["claims"],
        "species_name_crosswalk": prior["species_name_crosswalk"],
        "web_tools": native["web_tools"],
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read_in_prior_replay": 7,
            "source_claims": 7,
            "source_terms": 1,
            "selected_primary_identity_contexts_reviewed": 1,
            "paper_reference_accession_leads": 1,
            "paper_reference_locus_leads": 1,
            "new_reference_proteins": 0,
            "new_empty_identifier_queries": 2,
            "partial_positive_species_controls": 1,
            "new_native_request_attempts": 5,
            "native_http_responses": 4,
            "publisher_transport_failures_without_http_status": 1,
            "new_confirmed_access_denials": 0,
        },
        "limits": {
            **common.LIMITS,
            "new_primary_results_reviews": 1,
            "new_primary_results_review_scope": "SELECTED_IDENTITY_CONTEXT_NOT_AST_OR_FULL_PAPER",
            "new_taxonomy_requests": 0,
            "new_uniprot_protein_requests": 3,
            "primary_identity_review_medium": "AUTHOR_UPLOADED_WEB_TEXT_ONLY",
            "full_primary_text_or_figures_replayed_offline": False,
            "exact_variant_or_operational_exports": False,
            "copies_requested_from_user": True,
        },
        "attribution": (
            "CARD/ARO and UniProt2026_03, CC BY 4.0; Crossref metadata; primary text not redistributed."
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
