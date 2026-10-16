"""A source taxon, a project and an empty query cannot establish experimental identity."""

import builtins
import copy
import hashlib
import io
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_cdsa_cyp51_context as audit  # noqa: E402


@pytest.fixture(autouse=True)
def offline(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline scope audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def assessment():
    return json.loads((ROOT / (audit.PREFIX + "-assessment.json")).read_bytes())


@pytest.mark.parametrize(
    "key,value",
    [
        ("alternative_species_assignment", "Streptococcus oralis"),
        ("experimental_taxon_id", "NCBITaxon:28037"),
        ("paper_subject_label", "Streptococcus mitis 351"),
        ("paper_orf", "sm351_26"),
        ("source_species_is_verified_experimental_species", True),
    ],
)
def test_paper_context_does_not_silently_resolve_the_subject(key, value):
    a = assessment()
    audit.check_assessment(a)
    a["cdsa"][key] = value
    with pytest.raises(ValueError):
        audit.check_assessment(a)


@pytest.mark.parametrize(
    "key,value",
    [
        ("namespace", "Assembly"),
        ("versioned_assembly_assigned", "GCA_000000001.1"),
        ("experimental_genome_identity_verified", True),
        ("ncbi_link_followed", True),
        ("accession", "OTHER"),
    ],
)
def test_project_namespace_and_unverified_scope_are_preserved(key, value):
    a = assessment()
    a["cdsa"]["study_project"][key] = value
    with pytest.raises(ValueError, match="promoted to experimental identity"):
        audit.check_assessment(a)


@pytest.mark.parametrize(
    "group,key",
    [
        (None, "publisher_assessment_is_offline_body_replay"),
        (None, "experimental_allele_assignments"),
        (None, "biological_record_writes"),
        (None, "numeric_ast_exported"),
        (None, "variant_specifications_exported"),
        ("cdsa", "whole_paper_signoff"),
        ("cdsa", "supplements_reviewed"),
        ("cyp51", "source_definition_has_own_citation"),
        ("cyp51", "discovery_is_inherited_source_citation"),
        ("cyp51", "primary_results_reviewed"),
        ("abuo", "primary_results_reviewed"),
        ("abuo", "http_status_inferred"),
        ("abuo", "global_unavailability_inferred"),
    ],
)
def test_assessment_cannot_upgrade_evidence(group, key):
    a = assessment()
    (a if group is None else a[group])[key] = True
    with pytest.raises(ValueError, match="scope was promoted"):
        audit.check_assessment(a)


@pytest.mark.parametrize("group", ["abuo", "cyp51"])
@pytest.mark.parametrize("change", ["retry", "url"])
def test_access_holds_bind_the_specific_route_without_implicit_retries(group, change):
    a = assessment()
    a[group]["alternate_primary_routes_requested" if change == "retry" else "source_url"] = (
        1 if change == "retry" else "https://example.org/alternate"
    )
    with pytest.raises(ValueError, match="access hold"):
        audit.check_assessment(a)


@pytest.mark.parametrize("change", ["attempt", "receipt", "body", "error", "missing"])
def test_native_request_history_is_bounded(tmp_path, change):
    for key in audit.QUERIES:
        for suffix in ("attempt", "receipt", "body"):
            (tmp_path / f"{key}-{suffix}.json").write_text("{}")
    audit.check_history(tmp_path)
    if change == "missing":
        (tmp_path / "cdsa-locus-body.json").unlink()
    else:
        (tmp_path / f"extra-{change}.json").write_text("{}")
    with pytest.raises(ValueError, match="unaccounted"):
        audit.check_history(tmp_path)


def saved():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_saved_scope_and_draft_are_not_curated_grounding():
    d = saved()
    assert d["summary"]["complete_records_read"] == d["summary"]["source_claims"] == 13
    assert d["summary"]["source_terms"] == 6
    assert d["summary"]["corpus_records_hash_checked"] == 2939
    assert d["coverage"]["new_qualified_terms"] == []
    assert d["summary"]["combined_qualified_terms"] == 108
    assert d["summary"]["combined_remaining_terms"] == 70
    assert d["terms"]["ARO:3004097"]["status"] == "SOURCE_TAXONOMIC_SCOPE_CONFLICT"
    assert all(not t["qualified_reference_accessions"] for t in d["terms"].values())
    assert all(t["experimental_taxon_assignment"] is None for t in d["terms"].values())
    assert d["queries"]["cdsa-locus"]["suggestions_ignored"] == 5
    assert d["queries"]["cyp51-publication"]["suggestions_ignored"] == 3
    assert d["summary"]["new_metadata_requests"] == 2
    assert d["summary"]["new_taxonomy_requests"] == d["summary"]["ncbi_requests"] == 0
    assert d["curation_handoff"]["loader_accepted"] is True
    assert d["curation_handoff"]["projection_changes_only_note"] is True
    assert d["curation_handoff"]["source_owned_curation_applied"] is False
    assert d["curation_handoff"]["default_active_review_contains_draft"] is False
    for c in d["claims"]:
        node = d
        for part in c["term_pointer"].lstrip("/").split("/"):
            node = node[part]
        assert c["record_identifier"] in node["record_memberships"]
    audit.native.reject_operational_fields(d)


def test_historical_draft_kept_active_reviews_unchanged(pre_cdsa_qualification_root):
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    active = audit.read_json(pre_cdsa_qualification_root, plan["inputs"]["active_reviews"])
    draft = audit.read_json(ROOT, plan["inputs"]["proposed_review"])
    assert len(active["reviews"]) == 2
    r = draft["reviews"][0]
    assert r["review_id"] not in {p["review_id"] for p in active["reviews"]}
    assert len(r["source_rows"]) == 1
    assert r["source_rows"][0]["identifier"] == "CHEBI:600103"
    assert r["source_rows"][0]["standard_inchi_key"] == "DOAKLVKFURWEDJ-RWDRXURGSA-N"
    assert r["evidence"][0]["locations"] == ["Addendum in proof"]
    assert not {"protein_accession", "taxon_id", "alteration", "assay"} & set(r)


def test_discovery_identity_is_checked_without_native_cache():
    row = {
        "id": "24298976",
        "source": "MED",
        "doi": "10.1111/mpp.12106",
        "pmcid": "PMC6638911",
        "pubYear": "2014",
    }
    body = json.dumps({"resultList": {"result": [row]}})
    wrapper = {
        "status": 200,
        "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search",
        "body": body,
        "sha256": hashlib.sha256(body.encode()).hexdigest(),
    }
    assert audit.discovery_metadata(wrapper) == row
    wrong = copy.deepcopy(wrapper)
    wrong["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="provenance"):
        audit.discovery_metadata(wrong)


def test_offline_replay_is_read_only(monkeypatch, pre_cdsa_qualification_root):
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    if not (ROOT / plan["inputs"]["canary"]["path"]).exists():
        pytest.skip("ignored native cache unavailable; portable artifact checks still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not any(c in mode for c in "wax+"), "audit attempted file mutation"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == saved()


def test_cli_does_not_overwrite_and_can_create_nested_output(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    output = tmp_path / "nested" / "audit.json"
    monkeypatch.setattr(sys, "argv", ["audit", "--root", str(tmp_path), "--output", str(output)])
    audit.main()
    audit.main()
    output.write_text("{}")
    with pytest.raises(ValueError, match="differs"):
        audit.main()
    assert output.read_text() == "{}"


def test_cli_check_does_not_create_missing_output(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    output = tmp_path / "absent" / "audit.json"
    monkeypatch.setattr(sys, "argv", ["audit", "--root", str(tmp_path), "--output", str(output), "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not output.parent.exists()
