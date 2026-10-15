"""Keep the source-specific SCO-1 alias separate from experimental identity."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_sco1_evidence as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture
def publication():
    pmid = "17353248"
    identity = {
        "id": pmid,
        "source": "MED",
        "title": "SCO-1 reference identity",
        "doi": audit.PUBLICATIONS[pmid][0],
        "pmcid": audit.PUBLICATIONS[pmid][1],
        "isOpenAccess": "N",
        "firstPublicationDate": "2007-03-12",
    }
    body = {
        "hitCount": 1,
        "request": {"queryString": "EXT_ID:" + pmid + " AND SRC:MED", "resultType": "core", "pageSize": 1},
        "resultList": {
            "result": [
                {
                    **identity,
                    "pmid": pmid,
                    "abstractText": "Indexed context only.",
                    "fullTextUrlList": {"fullTextUrl": []},
                }
            ]
        },
    }
    return body, pmid, identity


def reference_fixture(accession):
    taxid, name, version, pmids = audit.SELECTED[accession]
    metadata = {p: {"doi": audit.PUBLICATIONS[p][0]} for p in pmids}
    entry = {
        "primaryAccession": accession,
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": version, "sequenceVersion": 1},
        "genes": [{"geneName": {"value": "blaSCO-1"}}],
        "organism": {"taxonId": taxid, "scientificName": name},
        "uniProtKBCrossReferences": [],
        "proteinDescription": {},
        "references": [
            {
                "referenceNumber": i + 1,
                "citation": {
                    "citationType": "journal article",
                    "title": "SCO-1 reference context",
                    "citationCrossReferences": [
                        {"database": "PubMed", "id": p},
                        {"database": "DOI", "id": audit.PUBLICATIONS[p][0]},
                    ],
                },
            }
            for i, p in enumerate(pmids)
        ],
    }
    taxon = {
        "taxonId": taxid,
        "scientificName": name,
        "rank": "species",
        "active": True,
        "parent": {"taxonId": 561 if taxid == 562 else 469, "scientificName": name.split()[0]},
        "lineage": [
            {"taxonId": 2, "rank": "domain", "scientificName": "Bacteria"},
            {"taxonId": 561 if taxid == 562 else 469, "rank": "genus", "scientificName": name.split()[0]},
        ],
    }
    return entry, taxon, metadata


def test_metadata_is_not_primary_evidence(publication):
    result = audit.project_metadata(*publication)
    assert result["primary_results_reviewed"] is False
    assert result["primary_unavailability_claimed"] is False
    assert result["non_oa_metadata_is_access_denial"] is False
    assert "abstractText" not in result


def test_metadata_request_is_explicitly_scoped():
    for pmid in audit.PUBLICATIONS:
        assert audit.metadata_url(pmid).startswith("https://www.ebi.ac.uk/europepmc/webservices/rest/search?")
        assert "EXT_ID%3A" + pmid in audit.metadata_url(pmid)
    with pytest.raises(ValueError, match="unplanned PMID"):
        audit.metadata_url("20387903")


def test_taxonomy_parent_must_match_lineage():
    entry, taxon, metadata = reference_fixture("A1E3K9")
    taxon["parent"]["scientificName"] = "Other"
    with pytest.raises(ValueError, match="parent differs"):
        audit.project_reference(entry, taxon, metadata)


@pytest.mark.parametrize("change", ["query", "count", "cursor", "pmid", "doi", "pmcid", "title", "page_size"])
def test_metadata_identity_guard(publication, change):
    body, _, _ = publication
    row = body["resultList"]["result"][0]
    if change == "query":
        body["request"]["queryString"] = "SCO-1"
    elif change == "count":
        body["hitCount"] = 2
    elif change == "cursor":
        body["nextCursorMark"] = "more"
    elif change == "page_size":
        body["request"]["pageSize"] = True
    else:
        row[change] = "changed"
    with pytest.raises(ValueError):
        audit.project_metadata(*publication)


@pytest.mark.parametrize("accession", audit.SELECTED)
def test_reference_identity_only_and_no_input_mutation(accession):
    inputs = reference_fixture(accession)
    before = copy.deepcopy(inputs)
    result = audit.project_reference(*inputs)
    assert inputs == before
    assert result["accession"] == "UniProtKB:" + accession
    assert result["gene_symbols"] == ["blaSCO-1"]
    assert result["experimental_allele_assignment"] is None
    assert result["experimental_genome_assignment"] is None
    assert result["exact_allele_assignment"] is result["experimental_subject_assignment"] is False
    assert result["explicit_card_xref"] is result["primary_results_reviewed"] is False
    assert result["global_bla_prefix_normalization_enabled"] is result["unflagged_means_complete"] is False


@pytest.mark.parametrize("accession", audit.SELECTED)
@pytest.mark.parametrize(
    "change", ["gene", "version", "taxon", "rank", "reviewed", "xref", "citation", "doi"]
)
def test_reference_requires_its_native_identity(accession, change):
    entry, taxon, metadata = reference_fixture(accession)
    if change == "gene":
        entry["genes"][0]["geneName"]["value"] = "blaTEM-1"
    elif change == "version":
        entry["entryAudit"]["sequenceVersion"] = 2
    elif change == "taxon":
        taxon["scientificName"] = "Other species"
    elif change == "rank":
        taxon["rank"] = "strain"
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif change == "xref":
        entry["uniProtKBCrossReferences"] = [{"database": "CARD", "id": audit.TERM}]
    elif change == "citation":
        entry["references"].pop()
    else:
        entry["references"][0]["citation"]["citationCrossReferences"][1]["id"] = "10.1000/other"
    with pytest.raises(ValueError):
        audit.project_reference(entry, taxon, metadata)


def test_unselected_neighbor_rejected():
    entry, taxon, metadata = reference_fixture("A1E3K9")
    entry["primaryAccession"] = "A1E3L0"
    with pytest.raises(ValueError, match="unselected"):
        audit.project_reference(entry, taxon, metadata)


def test_public_dossier_preserves_scope_and_full_memberships():
    data = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert data["scope"] == audit.SCOPE
    assert len(data["records"]) == len(data["claims"]) == 8
    assert len(data["references"]) == 2
    memberships = data["reference_memberships"]
    expected = {(r["identifier"], a) for r in data["records"] for a in data["references"]}
    assert len(memberships) == len(expected) == 16
    assert {(m["record_identifier"], m["protein_accession"]) for m in memberships} == expected
    excluded = data["incidental_citation_hits_not_selected"]
    assert len(excluded) == len(set(excluded)) == 46
    assert not set(excluded) & set(data["references"])
    assert not any(data["disposition"].values())
    assert data["constraints"]["new_requests"] == 3
    assert data["constraints"]["new_primary_requests"] == data["constraints"]["ncbi_requests"] == 0
    assert data["constraints"]["membership_index_updated"] is False
    assert all(not r["primary_results_reviewed"] for r in data["metadata"].values())


def test_cli_exclusive_output_and_check(tmp_path, monkeypatch):
    output = tmp_path / "dossier.json"
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    monkeypatch.setattr(sys, "argv", ["audit", "--output", str(output), "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not output.exists()
    monkeypatch.setattr(sys, "argv", ["audit", "--output", str(output)])
    audit.main()
    audit.main()
    output.write_text("different\n")
    with pytest.raises(ValueError, match="does not reproduce"):
        audit.main()
