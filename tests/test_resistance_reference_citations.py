"""Reference citations cannot change subjects, alleles, effects or old evidence."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import emit_antibiotic_yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import resistance_reference_citations as audit  # noqa: E402

PLAN = Path("research/2026-10-14-reference-citation-plan.json")


@pytest.fixture
def reference():
    return {
        "accession": "UniProtKB:P00001",
        "gene": "example",
        "entry_type": "UniProtKB reviewed (Swiss-Prot)",
        "entry_version": 2,
        "sequence_version": 1,
        "reference_taxon_id": "NCBITaxon:10",
        "release": "2026_03",
        "retrieved_on": "2026-10-12",
        "scope": "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE",
    }


@pytest.fixture
def inputs(reference):
    record = {
        "identifier": "CHEBI:1",
        "chemical_structure": {"standard_inchi_key": "TEST"},
        "resistance_mechanisms": [
            {
                "gene_families": ["example"],
                "taxon_id": "NCBITaxon:20",
                "note": "Existing experimental interpretation",
                "evidence": [{"reference": "PMID:1"}],
            }
        ],
        "curation_history": [{"action": "EXISTING"}],
    }
    plan = {
        "identifier": "CHEBI:1",
        "standard_inchi_key": "TEST",
        "before": {"sha256": audit.digest(emit_antibiotic_yaml(record).encode())},
        "edits": [
            {
                "resistance_index": 0,
                "before_claim_sha256": audit.claim_digest(record["resistance_mechanisms"][0]),
                "primary_reference": "PMID:1",
                "references": [reference],
            }
        ],
    }
    return record, plan


def repin(record, plan):
    plan["before"]["sha256"] = audit.digest(emit_antibiotic_yaml(record).encode())
    plan["edits"][0]["before_claim_sha256"] = audit.claim_digest(record["resistance_mechanisms"][0])


def test_only_appends_qualified_evidence_and_does_not_mutate_inputs(inputs):
    record, plan = inputs
    baseline = copy.deepcopy(record)
    after = audit.add_citations(record, plan)
    assert record == baseline
    claim = after["resistance_mechanisms"][0]
    added = claim["evidence"].pop()
    assert "not an experimental subject assignment" in added["notes"]
    assert "not independent phenotype or mechanism evidence" in added["notes"]
    assert after == record


@pytest.mark.parametrize(
    "field,value",
    [
        ("identifier", "CHEBI:2"),
        ("standard_inchi_key", "CHANGED"),
    ],
)
def test_record_identity_drift(inputs, field, value):
    record, plan = inputs
    plan[field] = value
    with pytest.raises(ValueError, match="record identity"):
        audit.add_citations(record, plan)


@pytest.mark.parametrize(
    "change",
    [
        "baseline",
        "claim_hash",
        "source",
        "protein",
        "taxon",
        "gene",
        "primary",
        "duplicate_edit",
        "negative_index",
        "bool_index",
        "empty_edits",
        "empty_references",
        "duplicate_reference",
        "existing_reference",
    ],
)
def test_invalid_or_conflicting_context_fails_closed(inputs, change):
    record, plan = inputs
    claim = record["resistance_mechanisms"][0]
    edit = plan["edits"][0]
    if change == "source":
        claim["source"] = "PHIBASE"
    elif change == "protein":
        claim["protein_accession"] = "UniProtKB:P00001"
    elif change == "taxon":
        del claim["taxon_id"]
    elif change == "gene":
        claim["gene_families"] = ["other"]
    elif change == "primary":
        claim["evidence"] = []
    elif change == "duplicate_edit":
        plan["edits"].append(copy.deepcopy(edit))
    elif change == "negative_index":
        edit["resistance_index"] = -1
    elif change == "bool_index":
        edit["resistance_index"] = False
    elif change == "empty_edits":
        plan["edits"] = []
    elif change == "empty_references":
        edit["references"] = []
    elif change == "duplicate_reference":
        edit["references"].append(copy.deepcopy(edit["references"][0]))
    elif change == "existing_reference":
        claim["evidence"].append({"reference": "UniProtKB:P00001"})
    if plan["edits"]:
        repin(record, plan)
    if change == "baseline":
        plan["before"]["sha256"] = "0" * 64
    if change == "claim_hash":
        edit["before_claim_sha256"] = "0" * 64
    with pytest.raises(ValueError):
        audit.add_citations(record, plan)


@pytest.mark.parametrize("already_present", [False, True])
def test_url_alias_cannot_bypass_duplicate_reference_checks(inputs, already_present):
    record, plan = inputs
    reference = plan["edits"][0]["references"][0]
    alias = {**reference, "accession": "https://www.uniprot.org/uniprotkb/P00001/entry"}
    if already_present:
        record["resistance_mechanisms"][0]["evidence"].append({"reference": "UniProtKB:P00001"})
        plan["edits"][0]["references"] = [alias]
        repin(record, plan)
    else:
        plan["edits"][0]["references"].append(alias)
    before = copy.deepcopy(record)
    with pytest.raises(ValueError, match="reference identifiers"):
        audit.add_citations(record, plan)
    assert record == before


@pytest.mark.parametrize(
    "field,value",
    [
        ("scope", "EXPERIMENTAL"),
        ("release", "different"),
        ("entry_type", "unknown"),
        ("entry_version", 0),
        ("entry_version", True),
        ("sequence_version", "1"),
        ("gene", ""),
        ("reference_taxon_id", "NCBITaxon:0"),
        ("reference_taxon_id", "https://rest.uniprot.org/taxonomy/10"),
        ("accession", "P00001"),
        ("accession", "https://www.uniprot.org/uniprotkb/P00001/entry"),
        ("accession", "https://rest.uniprot.org/uniprotkb/P00001.json"),
        ("retrieved_on", "yesterday"),
    ],
)
def test_reference_metadata_must_be_explicit(reference, field, value):
    reference[field] = value
    with pytest.raises(ValueError):
        audit.citation(reference)


@pytest.fixture
def response():
    entry = {
        "primaryAccession": "P00001",
        "genes": [{"geneName": {"value": "example"}}],
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 2, "sequenceVersion": 1},
        "organism": {"taxonId": 10},
    }
    receipt = {
        "url": "https://rest.uniprot.org/uniprotkb/search?query=example",
        "status": 200,
        "retrieved_at": "2026-10-12T00:00:00Z",
        "headers": {"X-UniProt-Release": "2026_03", "X-Total-Results": "1"},
        "body": json.dumps({"results": [entry]}),
    }
    receipt["sha256"] = audit.digest(receipt["body"].encode())
    return receipt


def test_reference_response_projects_only_metadata(response, reference):
    assert audit.reference_metadata(response, response, "example", "P00001") == reference


@pytest.mark.parametrize(
    "change",
    [
        "status",
        "body_hash",
        "url",
        "release",
        "pagination",
        "count",
        "null_results",
        "false_results",
        "string_results",
        "missing_results",
        "non_object_result",
        "duplicate_accession",
        "wrong_gene",
        "duplicate_gene",
        "sequence",
        "features",
        "comments",
        "version",
        "taxon",
        "entry_type",
    ],
)
def test_reference_response_rejects_drift_and_malformed_payloads(response, change):
    expected = copy.deepcopy(response)
    body = json.loads(response["body"])
    entry = body["results"][0]
    if change == "status":
        response["status"] = 500
    elif change == "url":
        response["url"] = "https://other.example/"
    elif change == "release":
        response["headers"]["X-UniProt-Release"] = "OTHER"
    elif change == "pagination":
        response["headers"]["Link"] = "next"
    elif change == "count":
        response["headers"]["X-Total-Results"] = "2"
    elif change == "null_results":
        body["results"] = None
    elif change == "false_results":
        body["results"] = False
    elif change == "string_results":
        body["results"] = ""
    elif change == "missing_results":
        del body["results"]
    elif change == "non_object_result":
        body["results"] = [None]
    elif change == "duplicate_accession":
        body["results"].append(copy.deepcopy(entry))
        response["headers"]["X-Total-Results"] = "2"
    elif change == "wrong_gene":
        entry["genes"][0]["geneName"]["value"] = "OTHER"
    elif change == "duplicate_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change in {"sequence", "features", "comments"}:
        entry[change] = []
    elif change == "version":
        entry["entryAudit"]["entryVersion"] = True
    elif change == "taxon":
        entry["organism"]["taxonId"] = True
    elif change == "entry_type":
        entry["entryType"] = "unknown"
    response["body"] = json.dumps(body)
    if change != "body_hash":
        response["sha256"] = audit.digest(response["body"].encode())
        expected["sha256"] = response["sha256"]
    else:
        response["body"] += " "
    with pytest.raises(ValueError):
        audit.reference_metadata(response, expected, "example", "P00001")


def test_exact_inverse_is_not_a_general_rollback(inputs):
    record, plan = inputs
    after = audit.add_citations(record, plan)
    event = {"action": "REFERENCE_CITATIONS"}
    after["curation_history"].append(event)
    receipt = {
        **plan,
        "after": {"sha256": audit.digest(emit_antibiotic_yaml(after).encode())},
        "curation_event": event,
    }
    assert audit.restore_before(after, receipt) == record
    assert after["curation_history"][-1] == event
    after["resistance_mechanisms"][0]["note"] = "Later legitimate curation"
    with pytest.raises(ValueError, match="pinned successor"):
        audit.restore_before(after, receipt)


@pytest.mark.parametrize("change", ["event", "tail", "claim", "record"])
def test_inverse_checks_every_preservation_boundary(inputs, change):
    record, plan = inputs
    after = audit.add_citations(record, plan)
    event = {"action": "REFERENCE_CITATIONS"}
    after["curation_history"].append(copy.deepcopy(event))
    receipt = {**plan, "curation_event": event}
    if change == "event":
        after["curation_history"][-1]["action"] = "OTHER"
    elif change == "tail":
        after["resistance_mechanisms"][0]["evidence"][-1]["notes"] = "OTHER"
    elif change == "claim":
        after["resistance_mechanisms"][0]["note"] = "OTHER"
    else:
        after["unrelated"] = "OTHER"
    receipt["after"] = {"sha256": audit.digest(emit_antibiotic_yaml(after).encode())}
    with pytest.raises(ValueError):
        audit.restore_before(after, receipt)


def test_cached_source_replay_and_bounded_plan_are_offline(monkeypatch):
    def fail(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(socket.socket, "connect", fail)
    plan = json.loads((ROOT / PLAN).read_bytes())
    if not all((ROOT / r["snapshot"]["path"]).exists() for r in plan["records"]):
        pytest.skip("private archival records are not distributed")
    for source in plan["sources"]:
        assert audit.digest((ROOT / source["path"]).read_bytes()) == source["sha256"]
    count = 0
    for row in plan["records"]:
        record = load_record(ROOT / row["snapshot"]["path"])
        after = audit.add_citations(record, row)
        for edit in row["edits"]:
            for reference in edit["references"]:
                request = json.loads((ROOT / reference["source_receipt"]["path"]).read_bytes())
                actual = audit.reference_metadata(
                    request,
                    reference["source_request"],
                    reference["gene"],
                    reference["accession"].split(":", 1)[1],
                )
                assert all(reference[k] == value for k, value in actual.items())
                count += 1
        assert len(record["resistance_mechanisms"]) == len(after["resistance_mechanisms"])
    assert count == 9
    assert plan["summary"]["existing_claims"] == 7


@pytest.mark.parametrize("identifier", ["CHEBI:131850", "CHEBI:15353", "CHEBI:81419"])
def test_live_citation_transition_preserves_complete_historical_record(
    identifier, pre_causal_graphs_root
):
    receipt = json.loads(
        (pre_causal_graphs_root / "research/2026-10-14-reference-citation-curation.json").read_bytes()
    )
    (row,) = [r for r in receipt["records"] if r["identifier"] == identifier]
    after = load_record(pre_causal_graphs_root / row["after"]["path"])
    before = audit.restore_before(after, row)
    rebuilt = audit.add_citations(before, row)
    rebuilt["curation_history"].append(row["curation_event"])
    assert rebuilt == after
    assert audit.digest(emit_antibiotic_yaml(before).encode()) == row["before"]["sha256"]
    assert audit.digest(emit_antibiotic_yaml(after).encode()) == row["after"]["sha256"]
