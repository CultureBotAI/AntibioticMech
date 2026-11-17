"""Shared gene names are insufficient for a paper or experimental-subject join."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_bcmfs1_reference as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline Bcmfs1 audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)


def entry():
    return {
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "primaryAccession": "REFERENCE",
        "entryAudit": {"entryVersion": 88, "sequenceVersion": 2},
        "organism": {"taxonId": 40559, "scientificName": "Botrytis cinerea"},
        "proteinDescription": {"submissionNames": [{"fullName": {"value": "DHA14-like major facilitator"}}]},
        "genes": [{"geneName": {"value": "Bcmfs1"}}],
        "references": [
            {
                "citation": {
                    "citationCrossReferences": [
                        {"database": "PubMed", "id": audit.PMID},
                        {"database": "DOI", "id": audit.DOI.lower()},
                    ]
                },
                "referenceComments": [{"type": "STRAIN", "value": "SAS56"}],
            }
        ],
    }


def node():
    return {"taxonId": 40559, "rank": "species", "scientificName": "Botrytis cinerea", "active": True}


def test_same_paper_is_reference_not_experimental_identity():
    result = audit.candidate(entry(), node())
    assert result["qualified_reference"] is True
    assert result["disposition"] == audit.QUALIFIED
    assert result["bibliography_strain_comments_not_subject_identity"] == ["SAS56"]
    assert result["experimental_subject_assignment"] is result["exact_resistance_allele"] is False
    assert result["canonical_locus_selected"] is result["reference_identity_establishes_resistance"] is False
    assert result["experimental_genome_assignment"] is result["tested_derivative_assignment"] is None


@pytest.mark.parametrize("change", ["missing", "wrong_pmid", "wrong_doi", "split", "namespace"])
def test_gene_species_or_separate_citations_cannot_supply_paper_identity(change):
    e = entry()
    refs = e["references"][0]["citation"]["citationCrossReferences"]
    if change == "missing":
        e["references"] = []
    elif change == "wrong_pmid":
        refs[0]["id"] = "11374155"
    elif change == "wrong_doi":
        refs[1]["id"] = "10.1002/ps.309"
    elif change == "split":
        e["references"].append({"citation": {"citationCrossReferences": [refs.pop()]}})
    else:
        refs[0]["database"] = "Other"
    result = audit.candidate(e, node())
    assert not result["qualified_reference"]
    assert result["disposition"] == "GENE_ONLY_REFERENCE_LOCUS_UNRESOLVED"


@pytest.mark.parametrize(
    "change",
    [
        "gene",
        "gene_missing",
        "orf_only",
        "duplicate_gene",
        "wrong_species",
        "inactive_taxon",
        "wrong_label",
        "missing_version",
        "boolean_version",
        "inactive_entry",
        "sequence",
        "features",
        "comments",
    ],
)
def test_invalid_native_identity_is_rejected(change):
    e, n = entry(), node()
    if change == "gene":
        e["genes"][0]["geneName"]["value"] = "MFS1"
    elif change == "gene_missing":
        e["genes"] = []
    elif change == "orf_only":
        e["genes"] = [{"orfNames": [{"value": "Bcmfs1"}]}]
    elif change == "duplicate_gene":
        e["genes"].append(copy.deepcopy(e["genes"][0]))
    elif change == "wrong_species":
        n["taxonId"] = e["organism"]["taxonId"] = 999
    elif change == "inactive_taxon":
        n["active"] = False
    elif change == "wrong_label":
        e["organism"]["scientificName"] = "Different organism"
    elif change == "missing_version":
        e["entryAudit"].pop("sequenceVersion")
    elif change == "boolean_version":
        e["entryAudit"]["sequenceVersion"] = True
    elif change == "inactive_entry":
        e["entryType"] = "Inactive"
    else:
        e[change] = []
    with pytest.raises(ValueError):
        audit.candidate(e, n)


def test_strain_stays_strain_not_experimental_derivative():
    e, n = entry(), node()
    e["references"] = []
    n.update(
        {
            "taxonId": 332648,
            "scientificName": "Botrytis cinerea (strain B05.10)",
            "rank": "strain",
            "lineage": [node()],
        }
    )
    e["organism"] = {"taxonId": n["taxonId"], "scientificName": n["scientificName"]}
    e["genes"][0]["orfNames"] = [{"value": "REFERENCE_LOCUS"}]
    result = audit.candidate(e, n)
    assert result["reference_taxon_rank"] == "strain"
    assert result["source_species_taxon_id"] == "NCBITaxon:40559"
    assert result["gene_orf_names"] == ["REFERENCE_LOCUS"]
    assert not result["qualified_reference"]
    assert result["tested_derivative_assignment"] is None


def test_public_cohort_accounting_and_limits():
    doc = json.loads((ROOT / audit.OUTPUT).read_bytes())
    plan = audit.read_json(ROOT, doc["plan"])
    for pin in plan["inputs"].values():
        if not pin["path"].startswith("reports/"):
            audit.reference.check_pin(ROOT, pin)
    assessment = audit.read_json(ROOT, doc["assessment"])
    assert not assessment["publication"]["abstract_is_full_primary_results_review"]
    assert not assessment["publication"]["tested_chemical_form_verified"]
    assert not assessment["biological_record_writes"]
    assert assessment["access_accounting"][0]["reported_http_status"] == 403
    assert not assessment["access_accounting"][0]["retry_or_alternate_after_denial"]
    assert doc["summary"]["corpus_records_hash_checked"] == 2939
    assert doc["summary"]["native_gene_candidates"] == 9
    assert doc["summary"]["publication_qualified_references"] == 1
    qualified = [c for c in doc["candidates"] if c["qualified_reference"]]
    assert [c["protein_accession"] for c in qualified] == ["UniProtKB:Q9P8L8"]
    assert qualified[0]["entry_version"] == 88
    assert qualified[0]["sequence_version"] == 2
    assert len({tuple(c["gene_orf_names"]) for c in doc["candidates"] if not c["qualified_reference"]}) == 8
    assert doc["terms"][audit.ARO]["qualified_reference_accessions"] == []
    assert doc["terms"][audit.ARO]["publication_reference_leads"] == ["UniProtKB:Q9P8L8"]
    assert not doc["terms"][audit.ARO]["source_gene_alias_verified"]
    coverage = doc["coverage"]
    assert coverage["previous_qualified_count"] == 108
    assert coverage["new_qualified_terms"] == []
    assert len(coverage["qualified_terms"]) == 108
    assert len(coverage["remaining_terms"]) == 70
    assert not set(coverage["qualified_terms"]) & set(coverage["remaining_terms"])
    assert (
        len(set(coverage["qualified_terms"] + coverage["remaining_terms"])) == coverage["cohort_terms"] == 178
    )
    for candidate in doc["candidates"]:
        assert not candidate["experimental_subject_assignment"]
        assert not candidate["exact_resistance_allele"]
        assert not candidate["reference_identity_establishes_resistance"]
    assert doc["constraints"]["issue_1040"] == "DEFERRED"
    assert not doc["constraints"]["full_investigation_complete"]


@pytest.mark.parametrize(
    "change",
    [
        None,
        "pagination",
        "redirect",
        "release",
        "incomplete",
        "duplicate",
        "body",
        "endpoint",
        "fields",
        "history",
        "media",
        "status",
    ],
)
def test_native_query_provenance_completeness_and_duplicates(tmp_path, change):
    request = json.loads((ROOT / (audit.PREFIX + "-plan.json")).read_bytes())
    item = request["requests"]["gene"]
    payload = {"results": [entry()], "suggestions": [{"not_a_result": True}]}
    if change == "duplicate":
        payload["results"].append(entry())
    body = json.dumps(payload).encode()
    (tmp_path / "body.json").write_bytes(body)
    attempt = {
        "key": "gene",
        "url": item["url"],
        "plan_sha256": "PLAN",
        "retries": 0,
        "redirects_followed": 0,
    }
    receipt = {
        **attempt,
        "status": 200,
        "retrieved_at": "TEST",
        "bytes": len(body),
        "body": {"path": "body.json", "sha256": hashlib.sha256(body).hexdigest()},
        "headers": {
            "x-uniprot-release": "2026_03",
            "content-type": "application/json",
            "x-total-results": str(len(payload["results"])),
        },
    }
    plan = {"inputs": {"request_plan": {"sha256": "PLAN"}, "gene_receipt": {}, "gene_attempt": {}}}
    inputs = {"request_plan": request, "gene_receipt": receipt, "gene_attempt": attempt}
    if change == "pagination":
        receipt["headers"]["link"] = "next"
    elif change == "redirect":
        receipt["headers"]["location"] = "elsewhere"
    elif change == "release":
        receipt["headers"]["x-uniprot-release"] = "other"
    elif change == "incomplete":
        receipt["headers"]["x-total-results"] = "2"
    elif change == "body":
        (tmp_path / "body.json").write_text("{}")
    elif change == "endpoint":
        item["url"] = item["url"].replace("rest.uniprot.org", "example.org")
    elif change == "fields":
        item["url"] += ",sequence"
    elif change == "history":
        attempt["retries"] = 1
    elif change == "media":
        receipt["headers"]["content-type"] = "text/html"
    elif change == "status":
        receipt["status"] = 403
    if change is None:
        results, provenance = audit.query_results(tmp_path, plan, inputs, "gene")
        assert results == [entry()]
        assert provenance["complete_for_query"]
        assert provenance["suggestion_count"] == 1
        assert not provenance["suggestions_selected"]
    else:
        with pytest.raises(ValueError):
            audit.query_results(tmp_path, plan, inputs, "gene")
