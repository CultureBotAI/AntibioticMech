"""Acceptance tests for the PHI-base resistance-association lane."""

from __future__ import annotations

import csv
import sys
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from seed_from_sources import (  # noqa: E402
    PHIBASE_RESISTANCE_SOURCE,
    merge_with_existing,
    phibase_sourced_resistance_view,
)

INVENTORY = ROOT / "data" / "raw" / "phibase_amr.tsv"


def inventory_rows() -> list[dict[str, str]]:
    with INVENTORY.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_inventory_is_the_audited_phibase_resistance_set():
    rows = inventory_rows()
    assert len(rows) == 217
    assert len({row["identifier"] for row in rows}) == 23
    assert all(row["identifier"].startswith("CHEBI:") for row in rows)
    assert all(len(row["standard_inchi_key"].split("-")) == 3 for row in rows)
    assert all(row["phenotype_label"].startswith("resistance to ") for row in rows)
    assert {row["interaction_type"] for row in rows} == {"antimicrobial_interaction"}
    assert all(row["pmid"].isdigit() for row in rows)
    assert all(row["taxon_id"].isdigit() for row in rows)
    assert {row["source_commit"] for row in rows} == {
        "62e6a87a49397cba6ceb211b254d7ac8e5d09ff8"
    }


def test_known_upstream_chemical_mismatch_is_not_imported():
    rows = inventory_rows()
    assert not any(row["identifier"] == "CHEBI:9242" for row in rows)


def test_seeded_associations_do_not_claim_a_biochemical_route(records):
    imported = [
        item
        for _, record in records
        for item in phibase_sourced_resistance_view(record)
    ]
    assert len(imported) == 217
    assert {item["mechanism_type"] for item in imported} == {"UNKNOWN"}
    assert all(item["evidence"][0]["reference"].startswith("PMID:") for item in imported)
    # The caveat is what the note is FOR. It used to also carry the organism,
    # strain, accession and phenotype, which #94 moved into slots; asserting on
    # the caveat keeps the check on the claim rather than on the prose.
    assert all("not evidence for a specific biochemical resistance mechanism" in item["note"]
               for item in imported)
    assert all(item["source"] == PHIBASE_RESISTANCE_SOURCE for item in imported)


def test_reseed_replaces_only_phibase_owned_resistance_slice(records):
    record = next(
        deepcopy(record)
        for _, record in records
        if phibase_sourced_resistance_view(record)
    )
    fresh = deepcopy(record)
    existing = deepcopy(record)
    phibase_sourced_resistance_view(existing)[0]["label"] = "stale PHI-base row"
    curator_item = {
        "mechanism_type": "UNKNOWN",
        "label": "curator resistance assertion",
        "note": "curator-owned",
        "evidence": [{"reference": "PMID:1"}],
    }
    existing.setdefault("resistance_mechanisms", []).append(curator_item)

    merged = merge_with_existing(fresh, existing)
    assert phibase_sourced_resistance_view(merged) == phibase_sourced_resistance_view(fresh)
    assert curator_item in merged["resistance_mechanisms"]
