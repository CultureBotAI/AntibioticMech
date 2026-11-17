"""Bibliographies and access holds must not become experimental evidence."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_beta_tubulin_evidence as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture
def entry():
    return {
        "primaryAccession": "P53373",
        "entryAudit": {"entryVersion": 113, "sequenceVersion": 1},
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "organism": {"taxonId": 40559},
        "references": [
            {
                "referenceNumber": 1,
                "citation": {
                    "id": "CI-TEST",
                    "citationType": "submission",
                    "publicationDate": "FEB-1996",
                    "submissionDatabase": "EMBL/GenBank/DDBJ databases",
                },
                "referenceComments": [{"type": "STRAIN", "value": "reference only"}],
                "referencePositions": ["OPERATIONAL_SENTINEL"],
            },
            {
                "referenceNumber": 2,
                "citation": {
                    "citationType": "journal article",
                    "title": "A native bibliography title",
                    "publicationDate": "2000",
                    "citationCrossReferences": [
                        {"database": "PubMed", "id": "12345"},
                        {"database": "DOI", "id": "10.1234/test"},
                        {"database": "AGRICOLA", "id": "IND123"},
                    ],
                },
            },
            {
                "referenceNumber": 3,
                "citation": {
                    "citationType": "journal article",
                    "title": "A journal reference without identifiers",
                    "publicationDate": "2021",
                },
            },
        ],
    }


def prior_for(entry):
    return {
        "proteins": {
            "UniProtKB:P53373": {
                "entry_version": 113,
                "sequence_version": 1,
                "entry_type": entry["entryType"],
                "reference_taxon_id": "NCBITaxon:40559",
                "reference_species_taxon_id": "NCBITaxon:40559",
                "bibliography": [
                    {
                        "identifiers": [
                            {"database": "DOI", "id": "10.1234/test"},
                            {"database": "PubMed", "id": "12345"},
                        ],
                        "publication_date": "2000",
                        "primary_results_reviewed": False,
                    }
                ],
            }
        },
        "terms": {
            "ARO:3009320": {
                "source_label": "Original source label",
                "record_memberships": ["CHEBI:3392"],
                "definition_citation_ids": ["PMID:18944187"],
                "reference_candidates": [{"protein_accession": "UniProtKB:P53373"}],
            }
        },
    }


def test_all_native_references_survive_without_experimental_assignment(entry):
    result = audit.bibliography(entry)
    assert len(result) == 3
    assert [r["citation_type"] for r in result] == ["submission", "journal article", "journal article"]
    assert result[0]["identifiers"] == result[2]["identifiers"] == []
    assert result[0]["reference_strain_comments"] == ["reference only"]
    assert result[0]["native_citation_id"] == "CI-TEST"
    assert result[0]["submission_database"] == "EMBL/GenBank/DDBJ databases"
    assert result[1]["identifiers"][-1] == {"database": "AGRICOLA", "id": "IND123"}
    assert "OPERATIONAL_SENTINEL" not in json.dumps(result)
    for row in result:
        assert row["primary_results_reviewed"] is False
        assert row["experimental_subject_assignment"] is False
        assert row["resistance_inferred_from_citation"] is False
        assert row["strain_comment_scope"] == "NATIVE_REFERENCE_METADATA_NOT_TESTED_RESISTANCE_SUBJECTS"


@pytest.mark.parametrize("identifier", [".1094/PDIS-09-17-1516-RE", "10.123/test", "10.1234/has space"])
def test_malformed_doi_is_retained_not_repaired(entry, identifier):
    entry["references"][1]["citation"]["citationCrossReferences"][1]["id"] = identifier
    row = audit.bibliography(entry)[1]
    assert row["identifiers"][1]["id"] == identifier
    assert row["identifier_issues"] == [
        {
            "database": "DOI",
            "native_id": identifier,
            "status": "MALFORMED_NATIVE_DOI_NOT_CORRECTED",
            "replacement": None,
        }
    ]


@pytest.mark.parametrize("number", [True, 0, -1, "1", 2])
def test_invalid_or_duplicate_native_reference_number_fails(entry, number):
    entry["references"][0]["referenceNumber"] = number
    with pytest.raises(ValueError, match="reference numbering"):
        audit.bibliography(entry)


@pytest.mark.parametrize(
    "field,value",
    [
        ("citationType", "unknown"),
        ("title", ""),
        ("title", 1),
        ("publicationDate", ""),
        ("publicationDate", None),
    ],
)
def test_unreviewed_citation_shape_fails(entry, field, value):
    entry["references"][1]["citation"][field] = value
    with pytest.raises(ValueError):
        audit.bibliography(entry)


def test_journal_title_is_required(entry):
    del entry["references"][1]["citation"]["title"]
    with pytest.raises(ValueError, match="lacks a title"):
        audit.bibliography(entry)


@pytest.mark.parametrize("field,value", [("database", ""), ("id", ""), ("id", None)])
def test_invalid_reference_identifier_fails(entry, field, value):
    entry["references"][1]["citation"]["citationCrossReferences"][0][field] = value
    with pytest.raises(ValueError, match="reference identifier"):
        audit.bibliography(entry)


def test_duplicate_identifier_fails(entry):
    refs = entry["references"][1]["citation"]["citationCrossReferences"]
    refs.append(copy.deepcopy(refs[0]))
    with pytest.raises(ValueError, match="duplicate"):
        audit.bibliography(entry)


def test_empty_strain_comment_fails(entry):
    entry["references"][0]["referenceComments"][0]["value"] = ""
    with pytest.raises(ValueError, match="strain comment"):
        audit.bibliography(entry)


def test_term_citations_are_not_borrowed_or_experimental_crosswalks(entry):
    prior = prior_for(entry)
    second = copy.deepcopy(prior["terms"]["ARO:3009320"])
    second["definition_citation_ids"] = ["PMID:12345"]
    prior["terms"]["ARO:3009324"] = second
    proteins, terms = audit.project_bibliographies({"UniProtKB:P53373": (entry, {})}, prior)
    assert terms["ARO:3009320"]["own_citation_matches_in_reference_bibliographies"] == []
    assert terms["ARO:3009324"]["own_citation_matches_in_reference_bibliographies"] == [
        {
            "protein_accession": "UniProtKB:P53373",
            "native_reference_number": 2,
            "source_citation": "PMID:12345",
        }
    ]
    assert all(t["primary_review_status"] == "OPEN" for t in terms.values())
    assert all(t["native_bibliography_is_experimental_crosswalk"] is False for t in terms.values())
    assert proteins["UniProtKB:P53373"]["exact_resistant_allele_assignment"] is None
    assert proteins["UniProtKB:P53373"]["experimental_genome_assignment"] is None


@pytest.mark.parametrize(
    "change", ["missing", "extra", "accession", "version", "type", "taxon", "prior_refs"]
)
def test_projection_is_bound_to_complete_prior_reference_identity(entry, change):
    prior = prior_for(entry)
    entries = {"UniProtKB:P53373": (entry, {})}
    if change == "missing":
        entries.clear()
    elif change == "extra":
        entries["UniProtKB:OTHER"] = (entry, {})
    elif change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "version":
        entry["entryAudit"]["entryVersion"] += 1
    elif change == "type":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change == "taxon":
        entry["organism"]["taxonId"] = 1
    else:
        prior["proteins"]["UniProtKB:P53373"]["bibliography"] = []
    with pytest.raises(ValueError):
        audit.project_bibliographies(entries, prior)


@pytest.fixture
def receipt():
    return {
        "url": audit.ARTICLE,
        "status": 403,
        "retry_performed": False,
        "redirects_followed": False,
        "headers": {"CF-Mitigated": "challenge"},
        "retrieved_at": "2026-10-15T03:54:28+00:00",
    }


def test_publisher_challenge_is_not_primary_text_or_global_absence(receipt):
    result = audit.project_hold(receipt, b"<html><title>Just a moment...</title></html>")
    assert result["status"] == "PUBLISHER_403_CHALLENGE_HELD_NO_RETRY"
    for key in (
        "article_obtained",
        "primary_results_reviewed",
        "retry_or_alternate_route_performed",
        "negative_biological_evidence",
        "global_inaccessibility_inferred",
        "paywall_inferred",
    ):
        assert result[key] is False


@pytest.mark.parametrize(
    "field,value",
    [
        ("status", 200),
        ("url", "https://example.org"),
        ("retry_performed", True),
        ("redirects_followed", True),
        ("headers", {}),
    ],
)
def test_hold_requires_the_inspected_request_scope(receipt, field, value):
    receipt[field] = value
    with pytest.raises(ValueError, match="scope changed"):
        audit.project_hold(receipt, b"<title>Just a moment...</title>")


@pytest.mark.parametrize(
    "body",
    [
        b"<title>An article</title>",
        b'<title>Just a moment...</title><meta name="citation_title" content="Article">',
    ],
)
def test_hold_rejects_uninspected_article_payload(receipt, body):
    with pytest.raises(ValueError, match="inspected article"):
        audit.project_hold(receipt, body)


def test_request_inventory_refuses_an_alternate_route(tmp_path):
    for key in ("doi", "publisher", "alternate"):
        (tmp_path / f"{key}-attempt.json").write_text("{}")
    with pytest.raises(ValueError, match="alternate route"):
        audit.request_context(tmp_path, tmp_path, {})


def test_cli_refuses_overwriting_a_different_checkpoint(tmp_path, monkeypatch):
    output = tmp_path / "checkpoint.json"
    output.write_bytes(b"old checkpoint\n")
    monkeypatch.setattr(audit, "OUTPUT", output)
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    monkeypatch.setattr(sys, "argv", ["audit"])
    with pytest.raises(ValueError, match="does not reproduce"):
        audit.main()
    assert output.read_bytes() == b"old checkpoint\n"


def test_public_snapshot_retains_complete_scope_and_native_gaps():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    summary = result["summary"]
    assert summary["reference_proteins"] == len(result["proteins"]) == 26
    assert summary["source_terms"] == len(result["terms"]) == 15
    assert len(result["records"]) == 7 and len(result["claims"]) == 15
    rows = [r for p in result["proteins"].values() for r in p["reference_rows"]]
    assert summary["native_reference_memberships"] == len(rows) == 81
    assert summary["reference_types"] == {"journal article": 45, "submission": 36}
    assert summary["references_without_identifiers"] == 47
    assert summary["journal_references_without_identifiers"] == 11
    assert summary["native_identifier_issues"] == 1
    assert summary["terms_with_own_source_citation_matches"] == 0
    assert all(t["primary_review_status"] == "OPEN" for t in result["terms"].values())
    assert "UniProtKB:A0ACC3ZK29" not in result["proteins"]
    botrytis = result["proteins"]["UniProtKB:P53373"]["reference_rows"]
    assert len(botrytis) == 3 and all(r["citation_type"] == "submission" for r in botrytis)
    assert [r["reference_strain_comments"] for r in botrytis] == [["SAS56"], ["91T-1"], ["ICMP 8583"]]
    issues = [i for r in rows for i in r["identifier_issues"]]
    assert issues[0]["native_id"] == ".1094/PDIS-09-17-1516-RE"
    assert issues[0]["replacement"] is None
    assert result["banno_followup"]["access_hold"]["article_obtained"] is False
    assert result["constraints"]["ncbi_requests"] == 0
    assert result["constraints"]["full_corpus_goal_status"] == "OPEN"
    assert "referencePositions" not in json.dumps(result)
