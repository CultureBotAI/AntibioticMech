"""An empty deposition lookup is not protein absence or an experimental identity."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_qnr_unresolved as audit  # noqa: E402


@pytest.fixture(autouse=True)
def offline(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("Qnr evidence replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "getaddrinfo", denied)


@pytest.fixture(scope="module")
def frozen():
    config = json.loads((ROOT / audit.AUDIT).read_bytes())
    return {k: audit.read(ROOT, pin) for k, pin in config["inputs"].items()}


def test_full_public_replay(frozen):
    dossier = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert audit.build(ROOT) == dossier
    assert len(dossier["claims"]) == len(dossier["reviews"]) == 7
    assert len(dossier["records"]) == 1
    assert dossier["summary"]["corpus_records_hash_checked"] == 2939
    assert dossier["summary"]["new_reference_selections"] == 0
    for row in dossier["reviews"].values():
        assert row["selected_reference_accessions"] == []
        assert row["whole_record_primary_review"] == "OPEN"
    for row in dossier["deposition_contexts"].values():
        assert row["query_result_count"] == 0
        assert row["service_suggestions_not_followed"]
        assert all(v is None for k, v in row.items() if k.startswith("experimental_"))


def test_optional_native_replay(frozen, require_native_inputs):
    require_native_inputs(frozen["projection"])
    assert audit.capture(ROOT) == frozen["projection"]


@pytest.mark.parametrize(
    "change",
    [
        "query",
        "deposition",
        "assembly",
        "taxon",
        "rank",
        "inactive",
        "lineage",
        "host",
        "phenotype_transfer",
        "isolate",
        "citation",
        "coverage",
        "canary",
        "release",
        "truncated",
        "body",
        "plan",
    ],
)
def test_independent_scope_and_identity_failures(frozen, change):
    plan, projection, notes = [
        copy.deepcopy(frozen[k]) for k in ("request_plan", "projection", "assessments")
    ]
    source = notes["sources"]["qnrvc2"]
    node = projection["taxa"]["qnrvc2"]["node"]
    query = projection["queries"]["qnre1"]
    if change == "query":
        plan["requests"]["qnre1"]["query"] = "gene:qnrE1"
    elif change == "deposition":
        source["deposition_accession"] = "EU436855"
    elif change == "assembly":
        source["deposition_is_genome_assembly"] = True
    elif change == "taxon":
        node["taxonId"] = 573
    elif change == "rank":
        node["rank"] = "strain"
    elif change == "inactive":
        node["active"] = False
    elif change == "lineage":
        node["lineage"].append(node["lineage"][0])
    elif change == "host":
        notes["sources"]["qnre1"]["heterologous_host_results_are_separate"] = False
    elif change == "phenotype_transfer":
        source["qnrvc1_phenotype_transfer_allowed"] = True
    elif change == "isolate":
        source["source_isolate_label"] = "VC627"
    elif change == "citation":
        source["reference"] = "PMID:28193666"
    elif change == "coverage":
        del notes["reviews"]["ARO:3002802"]
    elif change == "canary":
        projection["canary_review"]["approved_remaining_queries"] = False
    elif change == "release":
        query["receipt"]["headers"]["x-uniprot-release"] = "different"
    elif change == "truncated":
        query["receipt"]["headers"]["link"] = "next"
    elif change == "body":
        query["response_body"] += " "
    else:
        query["receipt"]["plan_sha256"] = "0" * 64
    with pytest.raises(ValueError):
        audit.validate(plan, projection, notes)


@pytest.mark.parametrize(
    "key",
    [
        "experimental_identifiers_assigned",
        "new_reference_selection",
        "biological_record_writes",
        "whole_record_primary_signoff",
        "all_primary_results_reviewed",
        "biological_absence_inferred",
        "reuse_terms_review_resumed",
        "numeric_ast_exported",
        "sequences_exported",
    ],
)
def test_no_evidence_promotion(frozen, key):
    notes = copy.deepcopy(frozen["assessments"])
    notes["limits"][key] = True
    with pytest.raises(ValueError):
        audit.validate(frozen["request_plan"], frozen["projection"], notes)


def test_canary_review_must_bind_actual_receipt(frozen):
    projection = copy.deepcopy(frozen["projection"])
    projection["canary_review"]["receipt"]["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="canary receipt"):
        audit.validate(frozen["request_plan"], projection, frozen["assessments"])


@pytest.mark.parametrize("change", ["path", "bytes", "structured_receipt"])
def test_canary_receipt_cannot_be_substituted(frozen, change):
    projection = copy.deepcopy(frozen["projection"])
    if change == "path":
        projection["canary_review"]["receipt"]["path"] = "reports/other-receipt.json"
    elif change == "bytes":
        projection["canary_receipt_body"] += " "
    else:
        projection["queries"]["qnre1"]["receipt"]["headers"]["irrelevant"] = "different"
    with pytest.raises(ValueError, match="canary receipt"):
        audit.validate(frozen["request_plan"], projection, frozen["assessments"])


def test_scope_flag_must_not_disappear(frozen):
    notes = copy.deepcopy(frozen["assessments"])
    del notes["limits"]["biological_absence_inferred"]
    with pytest.raises(ValueError, match="research scope"):
        audit.validate(frozen["request_plan"], frozen["projection"], notes)
