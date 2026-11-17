"""Keep MexXY references, primary hosts, bibliography strains and access holds distinct."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_mexxy_context as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def assessment():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    return audit.read_json(ROOT, plan["assessment"])


@pytest.mark.parametrize("group,key", [(g, k) for g, keys in audit.FALSE_FIELDS.items() for k in keys])
def test_primary_scope_cannot_be_promoted(group, key):
    notes = assessment()
    (notes[group] if group else notes)[key] = True
    with pytest.raises(ValueError, match="promoted"):
        audit.validate_assessment(notes)


@pytest.mark.parametrize(
    "change", ["donor", "host", "deposit", "paper", "hold", "strain", "regulator", "ncbi"]
)
def test_assessment_identity_and_scope_changes_rejected(change):
    notes = assessment()
    if change == "donor":
        notes["primary"]["source_species_name"] = "Escherichia coli"
    elif change == "host":
        notes["primary"]["assay_host_species_name"] = "Pseudomonas aeruginosa"
    elif change == "deposit":
        notes["primary"]["source_reported_nucleotide_deposit"] += ".1"
    elif change == "paper":
        notes["primary"]["pmid"] = "22282519"
    elif change == "hold":
        notes["held_primary"]["single_native_fulltext_request_status"] = 200
    elif change == "strain":
        notes["bibliography_scope"]["I0IYR4"]["strain_comment"] = "PA7"
    elif change == "regulator":
        notes["bibliography_scope"]["I0IYR3"]["role"] = "STRUCTURAL_COMPONENT"
    else:
        notes["access"]["ncbi_requests"] = 1
    with pytest.raises(ValueError):
        audit.validate_assessment(notes)


def native_fixture(accession):
    gene, pmid, strain, _ = audit.BIBLIOGRAPHY[accession]
    ids = [{"database": "PubMed", "id": pmid}]
    if pmid == "22282519":
        ids.append({"database": "DOI", "id": audit.HELD_DOI})
    return {
        "primaryAccession": accession,
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
        "proteinDescription": {},
        "organism": {"taxonId": 287, "scientificName": "Pseudomonas aeruginosa"},
        "genes": [{"geneName": {"value": gene}}],
        "references": [
            {
                "referenceNumber": 1,
                "citation": {"citationType": "journal article", "citationCrossReferences": ids},
                "referencePositions": ["NUCLEOTIDE SEQUENCE"],
                "referenceComments": [{"type": "STRAIN", "value": strain}],
            }
        ],
    }


def native_taxon():
    return {
        "taxonId": 287,
        "scientificName": "Pseudomonas aeruginosa",
        "rank": "species",
        "active": True,
        "parent": {"taxonId": 286, "scientificName": "Pseudomonas"},
        "lineage": [{"taxonId": 286, "scientificName": "Pseudomonas", "rank": "genus"}],
    }


@pytest.mark.parametrize("accession", audit.BIBLIOGRAPHY)
def test_native_bibliography_preserves_literal_strain_and_species(accession):
    entry = native_fixture(accession)
    before = copy.deepcopy(entry)
    result = audit.bibliography_context(entry, native_taxon())
    binding = result["primary_citation_binding"]
    assert binding["reference_strain_comments"] == [audit.BIBLIOGRAPHY[accession][2]]
    assert binding["identifiers"] == entry["references"][0]["citation"]["citationCrossReferences"]
    assert binding["missing_native_doi_filled_from_external_source"] is False
    assert binding["strain_comment_is_strain_taxonomy_assignment"] is False
    assert result["reference"]["reference_taxonomy"]["native_rank"] == "species"
    assert result["experimental_allele_assigned"] is result["experimental_host_assigned"] is False
    assert result["role"] == audit.BIBLIOGRAPHY[accession][3]
    assert entry == before


@pytest.mark.parametrize("change", ["gene", "pmid", "strain", "position", "doi", "duplicate", "taxon"])
def test_changed_native_binding_rejected(change):
    entry, taxon = native_fixture("Q9ZNG8"), native_taxon()
    row = entry["references"][0]
    if change == "gene":
        entry["genes"][0]["geneName"]["value"] = "mexZ"
    elif change == "pmid":
        row["citation"]["citationCrossReferences"][0]["id"] = "22282519"
    elif change == "strain":
        row["referenceComments"][0]["value"] = "KAM3"
    elif change == "position":
        row["referencePositions"] = ["FUNCTION"]
    elif change == "doi":
        row["citation"]["citationCrossReferences"].append({"database": "DOI", "id": "10.1128/aac.43.2.415"})
    elif change == "duplicate":
        entry["references"].append(copy.deepcopy(row))
    else:
        taxon["rank"] = "strain"
    with pytest.raises(ValueError):
        audit.bibliography_context(entry, taxon)


def hold_fixture(tmp_path, change=None):
    def save(name, value):
        path = tmp_path / name
        path.write_text(json.dumps(value))
        return audit.reference.pin(tmp_path, path)

    body = tmp_path / "primary-response.bin"
    body.write_bytes(b"Access denied")
    request = {
        "url": audit.HELD_URL,
        "pmid": "22282519",
        "doi": audit.HELD_DOI,
        "native_request_limit": 1,
        "web_reader_result": "TOOL_INACCESSIBLE_WITHOUT_HTTP_STATUS_NOT_AN_ACCESS_DENIAL",
        "ncbi_requests": 0,
        "retries": 0,
        "redirects_followed": 0,
    }
    plan = {"request_plan": save("request-plan.json", request)}
    attempt = {
        "url": audit.HELD_URL,
        "request_plan": plan["request_plan"],
        "ncbi_requests": 0,
        "retries": 0,
        "redirects_followed": 0,
    }
    receipt = {
        "url": audit.HELD_URL,
        "status": 403,
        "retries": 0,
        "redirects_followed": 0,
        "body": audit.reference.pin(tmp_path, body),
        "bytes": body.stat().st_size,
        "sha256": audit.reference.digest(body),
        "retrieved_at": "2026-10-15T18:30:38+00:00",
    }
    if change == "status":
        receipt["status"] = 200
    elif change == "url":
        receipt["url"] = "https://example.org/other-paper"
    elif change == "retry":
        attempt["retries"] = 1
    elif change == "body":
        body.write_bytes(b"Different body")
    elif change == "size":
        receipt["bytes"] += 1
    elif change == "extra":
        save("second-attempt.json", attempt)
    plan["primary_attempt"] = save("primary-attempt.json", attempt)
    plan["primary_receipt"] = save("primary-receipt.json", receipt)
    return plan


def test_access_hold_is_not_biological_absence(tmp_path):
    result = audit.access_hold(tmp_path, hold_fixture(tmp_path))
    assert result["status"] == 403 and result["native_attempts"] == 1
    assert result["primary_results_reviewed"] is result["establishes_biological_absence"] is False


@pytest.mark.parametrize("change", ["status", "url", "retry", "body", "size", "extra"])
def test_changed_access_hold_rejected(tmp_path, change):
    plan = hold_fixture(tmp_path, change)
    with pytest.raises(ValueError):
        audit.access_hold(tmp_path, plan)


def test_portable_artifact_retains_claims_references_and_citation_ownership(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    prior, mex = [audit.read_json(ROOT, result[k]) for k in ("prior_members", "prior_mex")]
    audit.read_json(ROOT, result["plan"])
    notes = audit.read_json(ROOT, result["assessment"])
    audit.validate_assessment(notes)
    assert result["claims"] == [c for c in prior["claims"] if c["aro_id"] in audit.TERMS]
    assert result["claims"] == [c for c in mex["claims"] if c["aro_id"] in audit.TERMS]
    ids = {c["record_identifier"] for c in result["claims"]}
    assert len(ids) == 12 and len(result["claims"]) == 21
    assert result["records"] == [r for r in prior["records"] if r["identifier"] in ids]
    assert result["claim_dispositions"] == audit.claim_dispositions(result["claims"], result["records"])
    for tid in audit.TERMS:
        assert result["source_terms"][tid] == mex["terms"][tid]
        assert result["source_terms"][tid]["definition_citation_ids"] == audit.CITATIONS[tid]
    for accession, row in result["component_reference_candidates"].items():
        assert row == mex["reference_candidates"][accession]
    for accession, row in result["member_reference_views"].items():
        assert row == prior["reference_proteins"][accession]
    accessions = set(result["component_reference_candidates"]) | set(result["member_reference_views"])
    assert len(accessions) == 7 and "UniProtKB:I0IYR3" not in accessions
    contexts = result["native_bibliography_contexts"]
    assert set(contexts) == set(audit.BIBLIOGRAPHY)
    for accession, (gene, pmid, strain, role) in audit.BIBLIOGRAPHY.items():
        context = contexts[accession]
        assert context["role"] == role
        assert context["reference"]["gene_symbols"] == [gene]
        assert context["reference"]["reference_taxonomy"]["taxon_id"] == "NCBITaxon:287"
        binding = context["primary_citation_binding"]
        assert binding["reference_strain_comments"] == [strain]
        assert {"database": "PubMed", "id": pmid} in binding["identifiers"]
        assert binding["missing_native_doi_filled_from_external_source"] is False
        if pmid == "9925549":
            assert not any(i["database"] == "DOI" for i in binding["identifiers"])
    assert result["primary_source_species"]["taxon_id"] == "NCBITaxon:287"
    assert result["primary_assay_host_species"]["taxon_id"] == "NCBITaxon:562"
    assert result["primary_access_hold"]["status"] == 403
    assert result["oprA_own_citation_query"]["result_count"] == 3
    assert result["limits"]["biological_records_changed"] == result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"


def test_no_operational_or_ast_values_exported():
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    forbidden = {
        "sequence",
        "features",
        "variants",
        "alteration",
        "assembly_accession",
        "biosample_accession",
        "mic_value",
        "primers",
        "coordinates",
        "protocol",
    }
    assert not set(keys(public_result())) & forbidden
    assert not set(keys(assessment())) & forbidden


def test_offline_read_only_replay_when_native_cache_available(monkeypatch, pre_cdsa_qualification_root):
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    if not (ROOT / plan["primary_receipt"]["path"]).exists():
        pytest.skip("native cache unavailable; portable checks still run")
    original = Path.open

    def read_only(path, mode="r", *args, **kwargs):
        assert not set(mode) & set("wax+"), "offline replay attempted file write"
        return original(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", read_only)
    assert audit.build(pre_cdsa_qualification_root) == public_result()
