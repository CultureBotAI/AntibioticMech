"""Integrity tests for the BindingDB-curated quantitative target lane."""

from __future__ import annotations

import csv
import sys
from collections import Counter
from copy import deepcopy
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from evaluate_bindingdb_targets import CURATED_MARKER  # noqa: E402
from extract_bindingdb_targets import parse_measurement  # noqa: E402
from seed_from_sources import (  # noqa: E402
    attach_bindingdb_targets,
    bindingdb_sourced_target_view,
    merge_with_existing,
)

INVENTORY = ROOT / "data" / "raw" / "bindingdb_target_measurements.tsv"


def inventory_rows() -> list[dict[str, str]]:
    with INVENTORY.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_measurement_parser_preserves_closed_qualifier_semantics():
    assert parse_measurement("<50") == ("LT", 50.0)
    assert parse_measurement(">=7.1e+3") == ("GE", 7100.0)
    assert parse_measurement("~0.25") == ("APPROX", 0.25)
    assert parse_measurement("5 to 10") is None


def test_inventory_is_the_audited_bindingdb_curated_set():
    rows = inventory_rows()
    assert len(rows) == 177
    assert len({row["identifier"] for row in rows}) == 45
    assert len({
        (row["identifier"], row["target_name"], row["taxon_id"], row["target_relation"])
        for row in rows
    }) == 95
    assert {row["curation_source"] for row in rows} == {CURATED_MARKER}
    assert not any("ChEMBL" in row["curation_source"] for row in rows)


def test_inventory_retains_identity_taxonomy_assay_and_primary_citation():
    rows = inventory_rows()
    assert all(len(row["standard_inchi_key"].split("-")) == 3 for row in rows)
    assert all(row["taxon_id"].isdigit() and row["taxon_label"] for row in rows)
    assert Counter(row["microbial_root"] for row in rows) == {
        "Viruses": 149,
        "Bacteria": 23,
        "Fungi": 5,
    }
    assert all(row["assay_name"] and row["assay_description"] for row in rows)
    assert all("_" in row["bindingdb_entry_assay_id"] for row in rows)
    assert all(row["reference"].startswith(("PMID:", "DOI:")) for row in rows)
    assert {row["source_version"] for row in rows} == {"2026-09"}
    assert {row["source_retrieved_on"] for row in rows} == {"2026-08-31"}


def test_only_kd_is_promoted_to_direct_binding():
    rows = inventory_rows()
    direct = [row for row in rows if row["target_relation"] == "DIRECT_BINDING_TARGET"]
    assert [(row["identifier"], row["measurement_type"], row["original_value"]) for row in direct] == [
        ("CHEBI:17642", "KD", "<50")
    ]
    assert all(
        row["target_relation"] == "MEASURED_TARGET_ASSOCIATION"
        for row in rows
        if row["measurement_type"] in {"KI", "IC50", "EC50"}
    )


def test_attached_targets_keep_uniprot_as_examples_not_target_identity():
    path = ROOT / "data" / "antibiotics" / "antibacterial" / "ciprofloxacin.yaml"
    record = yaml.safe_load(path.read_text(encoding="utf-8"))
    record["molecular_targets"] = [
        target
        for target in record.get("molecular_targets") or []
        if target.get("source") != "BINDINGDB"
    ]
    records = {record["identifier"]: record}
    counts = attach_bindingdb_targets(records)
    targets = bindingdb_sourced_target_view(record)
    assert counts["matched_measurements"] == 1
    assert len(targets) == 1
    target = targets[0]
    assert "target_id" not in target
    assert target["target_relation"] == "MEASURED_TARGET_ASSOCIATION"
    assert target["target_type"] == "PROTEIN_COMPLEX"
    assert [protein["uniprot_id"] for protein in target["protein_examples"]] == [
        "UniProtKB:Q45066",
        "UniProtKB:Q59192",
    ]
    assert target["measurements"][0]["assay_name"] == "DNA Topoisomerase IV Assay"
    assert target["evidence_status"] == "PRIMARY_EVIDENCE"


def test_reseed_replaces_only_bindingdb_owned_target_slice():
    path = ROOT / "data" / "antibiotics" / "antibacterial" / "ciprofloxacin.yaml"
    fresh = yaml.safe_load(path.read_text(encoding="utf-8"))
    existing = deepcopy(fresh)
    bindingdb_sourced_target_view(existing)[0]["measurements"][0]["original_value"] = "stale"
    existing["molecular_targets"].append({
        "target_label": "curator target",
        "target_type": "OTHER",
        "target_relation": "MEASURED_TARGET_ASSOCIATION",
        "experimental_context": "curator-owned test assertion",
        "evidence_status": "PRIMARY_EVIDENCE",
        "source": "CURATOR",
        "source_version": "test",
        "source_retrieved_on": "2026-08-31",
        "evidence": [{"reference": "PMID:1"}],
    })

    merged = merge_with_existing(fresh, existing)
    assert bindingdb_sourced_target_view(merged) == bindingdb_sourced_target_view(fresh)
    assert any(target.get("target_label") == "curator target" for target in merged["molecular_targets"])
