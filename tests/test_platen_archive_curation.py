"""An inactive donor reference cannot become a tested-allele assignment."""

import copy
import json
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.curate.curation_event import record_curation_event
from antibioticmech.validation.write_validated import emit_antibiotic_yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import curate_platen_archive_references as audit  # noqa: E402


def repin(record, plan):
    plan["before"]["sha256"] = audit.digest(emit_antibiotic_yaml(record).encode())
    plan["before_claim_sha256"] = audit.claim_digest(record["resistance_mechanisms"][1])


@pytest.fixture
def inputs():
    record = {
        "identifier": "CHEBI:68236",
        "chemical_structure": {"standard_inchi_key": audit.archives.STRUCTURES["CHEBI:68236"]},
        "curation_history": [{"action": "EXISTING"}],
        "resistance_mechanisms": [
            {"unchanged": True},
            {
                "gene_families": ["fabF"],
                "taxon_id": "NCBITaxon:1886",
                "taxon_label": "Streptomyces albidoflavus",
                "strain": "SB12013",
                "note": "Existing interpretation and limitations.",
                "evidence": [{"reference": "PMID:24560608"}],
            },
        ],
    }
    plan = {
        "identifier": record["identifier"],
        "standard_inchi_key": record["chemical_structure"]["standard_inchi_key"],
        "before": {},
        "resistance_index": 1,
    }
    repin(record, plan)
    return record, plan


def test_only_appends_note_and_qualified_references(inputs):
    record, plan = inputs
    original = copy.deepcopy(record)
    after = audit.add_reference(record, plan)
    assert record == original
    claim = after["resistance_mechanisms"][1]
    assert claim["note"].endswith(audit.NOTE)
    assert claim["evidence"][-3:] == audit.evidence()
    assert "inactive" in claim["evidence"][-1]["notes"]
    assert "not an active UniProtKB entry" in claim["evidence"][-1]["notes"]
    claim["note"] = claim["note"][: -len(audit.NOTE)]
    del claim["evidence"][-3:]
    assert after == original


@pytest.mark.parametrize(
    "change",
    [
        "identifier",
        "structure",
        "plan_structure",
        "baseline",
        "claim_hash",
        "gene",
        "owner",
        "protein",
        "strain_taxon",
        "taxon",
        "taxon_label",
        "strain",
        "primary",
        "index_zero",
        "index_bool",
        "note_missing",
        "note_empty",
        "already_noted",
        "existing_url",
        "existing_curie",
        "existing_kb_curie",
        "existing_entry_url",
    ],
)
def test_rejects_drift_or_duplicate_context(inputs, change):
    record, plan = inputs
    claim = record["resistance_mechanisms"][1]
    fields = {
        "gene": ("gene_families", ["fabH"]),
        "owner": ("source", "PHIBASE"),
        "protein": ("protein_accession", "UniProtKB:V5NR11"),
        "strain_taxon": ("strain_taxon_id", "NCBITaxon:58346"),
        "taxon": ("taxon_id", "NCBITaxon:58346"),
        "taxon_label": ("taxon_label", "Streptomyces platensis"),
        "strain": ("strain", "MA7327"),
        "primary": ("evidence", []),
        "note_missing": ("note", None),
        "note_empty": ("note", ""),
        "already_noted": ("note", claim["note"] + audit.NOTE),
    }
    aliases = {
        "existing_url": audit.evidence()[-1]["reference"],
        "existing_curie": "UniParc:UPI0003C98D16",
        "existing_kb_curie": "UniProtKB:V5NR11",
        "existing_entry_url": "https://www.uniprot.org/uniparc/UPI0003C98D16/entry",
    }
    if change in fields:
        key, value = fields[change]
        claim[key] = value
    elif change in aliases:
        claim["evidence"].append({"reference": aliases[change]})
    elif change == "identifier":
        record["identifier"] = "CHEBI:1"
    elif change == "structure":
        record["chemical_structure"]["standard_inchi_key"] = "WRONG"
    elif change == "plan_structure":
        plan["standard_inchi_key"] = "WRONG"
    elif change.startswith("index"):
        plan["resistance_index"] = 0 if change == "index_zero" else True
    repin(record, plan)
    if change == "baseline":
        plan["before"]["sha256"] = "0" * 64
    if change == "claim_hash":
        plan["before_claim_sha256"] = "0" * 64
    with pytest.raises(ValueError):
        audit.add_reference(record, plan)


@pytest.mark.parametrize("change", ["none", "successor", "event", "note", "evidence", "before"])
def test_exact_historical_restoration(inputs, change):
    record, plan = inputs
    after = audit.add_reference(record, plan)
    event = record_curation_event(after, curator="test", action="ARCHIVE_REFERENCE")
    receipt = {
        **plan,
        "curation_event": copy.deepcopy(event),
        "after": {"sha256": audit.digest(emit_antibiotic_yaml(after).encode())},
    }
    if change == "none":
        assert audit.restore_before(after, receipt) == record
        return
    if change == "successor":
        after["identifier"] = "CHEBI:1"
    elif change == "event":
        after["curation_history"][-1]["action"] = "OTHER"
    elif change == "note":
        after["resistance_mechanisms"][1]["note"] += " drift"
    elif change == "evidence":
        after["resistance_mechanisms"][1]["evidence"][-1]["notes"] += " drift"
    else:
        receipt["before"]["sha256"] = "0" * 64
    if change != "successor":
        receipt["after"]["sha256"] = audit.digest(emit_antibiotic_yaml(after).encode())
    with pytest.raises(ValueError):
        audit.restore_before(after, receipt)


def test_published_records_replay_exact_delta():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    receipt = json.loads((ROOT / audit.RECEIPT).read_bytes())
    assert len(plan["records"]) == len(receipt["records"]) == 2
    for planned, row in zip(plan["records"], receipt["records"], strict=True):
        doc = load_record(ROOT / row["after"]["path"])
        before = audit.restore_before(doc, row)
        after = audit.add_reference(before, planned)
        after["curation_history"].append(row["curation_event"])
        assert after == doc
        assert doc["resistance_mechanisms"][0] == before["resistance_mechanisms"][0]
        assert not doc["resistance_mechanisms"][1].get("protein_accession")
        if row["identifier"] == "CHEBI:68241":
            assert "partial resistance" in doc["resistance_mechanisms"][1]["phenotype_label"]
