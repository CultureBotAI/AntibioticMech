"""Reconciliation preserves provenance and does not promote references to alleles."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_reference_reconciled as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline reconciliation attempted network")

    monkeypatch.setattr(socket, "getaddrinfo", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)


@pytest.fixture(scope="module")
def frozen():
    return audit.read_inputs(ROOT)


@pytest.fixture(scope="module")
def reconciled(frozen):
    _, data = frozen
    sources = {n: data[n] for n in audit.QUALIFIED + audit.CONTEXT}
    before = copy.deepcopy(sources)
    prior = copy.deepcopy(data[audit.PRIOR])
    result = audit.reconcile(prior, sources)
    assert sources == before and prior == data[audit.PRIOR]
    return result


def test_preserves_existing_links_and_deduplicates_hmg1(frozen, reconciled):
    old = frozen[1][audit.PRIOR]
    assert len(reconciled["terms"]) == 2002
    assert len(reconciled["proteins"]) == 1926
    assert len(reconciled["unresolved_reference_worklist"]) == 597
    assert sum(bool(t["reference_links"]) for t in reconciled["terms"].values()) == 1405
    assert sum(len(t["reference_links"]) for t in reconciled["terms"].values()) == 3071
    for term, row in old["terms"].items():
        current = reconciled["terms"][term]
        for key in ("record_memberships", "source_label_sha256", "base_assessment"):
            assert current[key] == row[key]
        assert current["followups"][: len(row["followups"])] == row["followups"]
        if term not in audit.SELECTED:
            assert current["reference_links"] == row["reference_links"]
    for accession, row in old["proteins"].items():
        current = reconciled["proteins"][accession]
        assert current["identity"] == row["identity"]
        if accession != "UniProtKB:Q4WHZ1":
            assert current == row
    assert set(reconciled["proteins"]) - set(old["proteins"]) == {
        "UniProtKB:A0QRS5", "UniProtKB:Q6FQA9"
    }


def test_gaps_and_comparators_are_not_determinant_mappings(frozen, reconciled):
    gaps = {r["aro_id"]: r for r in reconciled["unresolved_reference_worklist"]}
    for name in audit.QUALIFIED + audit.CONTEXT:
        for term in frozen[1][name]["terms"]:
            link = audit.pointer(name, "terms", term)
            assert link in reconciled["terms"][term]["followups"]
            if term not in audit.SELECTED:
                assert link in gaps[term]["followups"]
                assert not reconciled["terms"][term]["reference_links"]
    assert reconciled["terms"]["ARO:3007670"]["reference_accessions"] == ["UniProtKB:Q4WHZ1"]
    comparator = reconciled["comparison_contexts"]["ARO:3007670"][0]
    assert comparator["protein_accession"] == "UniProtKB:B0YA65"
    assert comparator["included_in_determinant_reference_counts"] is False
    for row in reconciled["terms"].values():
        assert row["experimental_subject_assignment"] is False
        assert row["whole_record_primary_review"] == "OPEN"


@pytest.mark.parametrize("term", audit.SELECTED)
@pytest.mark.parametrize("change", ["accession", "allele", "rank", "inactive", "version"])
def test_reference_identity_rejects_scope_drift(frozen, term, change):
    name, _ = audit.SELECTED[term]
    dossier = copy.deepcopy(frozen[1][name])
    candidate = dossier["terms"][term]["references"][0]
    raw = candidate["identity"] if term == "ARO:3000390" else candidate["native_reference"]
    if change == "accession":
        candidate["accession"] = "UniProtKB:UNSUPPORTED"
    elif change == "allele":
        candidate["experimental_allele_assignment"] = "unsupported"
    elif change == "rank":
        raw["reference_taxon_rank"] = "species"
    elif change == "version":
        raw["sequence_version"] = True
    else:
        taxid = raw["reference_taxon_id"].split(":")[1]
        dossier["native_taxonomy"][taxid]["active"] = False
    with pytest.raises(ValueError):
        audit.selected_identity(term, candidate, dossier)


def test_public_snapshot_counts_and_pointers(frozen):
    plan, data = frozen
    doc = json.loads((ROOT / (audit.PREFIX + ".json")).read_bytes())
    assert doc["inputs"] == plan["inputs"]
    assert len(doc["records"]) == 2939 and len(doc["claims"]) == 4538
    assert doc["summary"]["current_source_qualified_claims"] == 4
    assert doc["summary"]["new_followup_claims"] == 35
    assert doc["summary"]["added_claim_memberships_with_references"] == 13
    assert doc["summary"]["whole_record_primary_signoffs"] == 0
    assert (ROOT / (audit.PREFIX + ".tsv")).read_text() == audit.previous.render_rows(doc["records"])

    def visit(value):
        if isinstance(value, dict):
            if set(value) == {"input", "pointer"}:
                node = data[value["input"]]
                for key in value["pointer"].split("/")[1:]:
                    key = key.replace("~1", "/").replace("~0", "~")
                    node = node[int(key)] if isinstance(node, list) else node[key]
            else:
                for item in value.values():
                    visit(item)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(doc)
