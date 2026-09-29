"""Acceptance tests for the PHI-base resistance-association lane."""

from __future__ import annotations

import csv
import sys
from copy import deepcopy
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import seed_from_sources  # noqa: E402
from seed_from_sources import (  # noqa: E402
    PHIBASE_RESISTANCE_SOURCE,
    merge_with_existing,
    phibase_sourced_resistance_view,
)

INVENTORY = ROOT / "data" / "raw" / "phibase_amr.tsv"
PHIBASE_COLUMNS = [
    "identifier",
    "standard_inchi_key",
    "phig_id",
    "protein_accession",
    "gene_id",
    "taxon_id",
    "taxon_label",
    "strain_taxon_id",
    "strain_label",
    "modification",
    "phenotype_id",
    "phenotype_label",
    "evidence_code",
    "interaction_type",
    "pmid",
    "source_commit",
    "source_retrieved_on",
]


def phibase_row(**overrides: str) -> dict[str, str]:
    row = {
        "identifier": "CHEBI:1",
        "standard_inchi_key": "AAAAAAAAAAAAAA-AAAAAAAAAA-A",
        "phig_id": "PHIG:1",
        "protein_accession": "P1",
        "gene_id": "gene-1",
        "taxon_id": "6029",
        "taxon_label": "Aspergillus flavus",
        "strain_taxon_id": "",
        "strain_label": "",
        "modification": "erg11delta (deletion)",
        "phenotype_id": "PHIPO:1",
        "phenotype_label": "resistance to widgetmycin",
        "evidence_code": "Cell growth assay",
        "interaction_type": "antimicrobial_interaction",
        "pmid": "1",
        "source_commit": "test",
        "source_retrieved_on": "2026-09-28",
    }
    row.update(overrides)
    return row


def write_phibase_inventory(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=PHIBASE_COLUMNS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


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


def test_phibase_refuses_container_taxa(tmp_path, monkeypatch):
    row = phibase_row(
        taxon_id="12908",
        taxon_label="Aspergillus flavus",
    )
    path = tmp_path / "phibase_amr.tsv"
    write_phibase_inventory(path, [row])
    monkeypatch.setattr(seed_from_sources, "RAW_DIR", tmp_path)
    records = {
        "CHEBI:1": {
            "identifier": "CHEBI:1",
            "chemical_structure": {"standard_inchi_key": row["standard_inchi_key"]},
            "curation_history": [],
        },
    }

    counts = seed_from_sources.attach_phibase_resistance(records)

    assert counts["refused_non_organism_taxon"] == 1
    assert counts["matched_associations"] == 0
    assert "resistance_mechanisms" not in records["CHEBI:1"]


@pytest.mark.parametrize(
    ("row_overrides", "records", "message"),
    [
        (
            {},
            {
                "CHEBI:1": {
                    "identifier": "CHEBI:1",
                    "chemical_structure": {"standard_inchi_key": "STALE"},
                },
            },
            "mapped InChIKey AAAAAAAAAAAAAA-AAAAAAAAAA-A does not match CHEBI:1",
        ),
        (
            {"identifier": "CHEBI:999999", "standard_inchi_key": "STALE"},
            {},
            "mapped identifier CHEBI:999999 is not in the corpus",
        ),
    ],
)
def test_phibase_rejects_identity_drift(
    tmp_path,
    monkeypatch,
    row_overrides,
    records,
    message,
):
    path = tmp_path / "phibase_amr.tsv"
    write_phibase_inventory(path, [phibase_row(**row_overrides)])
    monkeypatch.setattr(seed_from_sources, "RAW_DIR", tmp_path)

    with pytest.raises(ValueError, match=message):
        seed_from_sources.attach_phibase_resistance(records)


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
