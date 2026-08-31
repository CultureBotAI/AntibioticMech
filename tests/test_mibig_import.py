"""Acceptance tests for the strict first MIBiG producer import."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from extract_mibig_producers import reviewer_ids  # noqa: E402


def test_review_filter_ignores_the_migration_placeholder():
    entry = {
        "changelog": {
            "releases": [
                {
                    "entries": [
                        {"reviewers": ["AAAAAAAAAAAAAAAAAAAAAAAA"]},
                        {"reviewers": ["EXPERT-2", "EXPERT-1"]},
                    ]
                }
            ]
        }
    }
    assert reviewer_ids(entry, "AAAAAAAAAAAAAAAAAAAAAAAA") == ["EXPERT-1", "EXPERT-2"]


def test_committed_mibig_inventory_is_reviewed_and_carries_no_activity_claims(repo_root):
    path = repo_root / "data" / "raw" / "mibig_producers.tsv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(rows) == 43
    assert all(row["reviewed"] == "true" for row in rows)
    assert all("AAAAAAAAAAAAAAAAAAAAAAAA" not in row["reviewer_ids"] for row in rows)
    assert all(row["primary_reference"] for row in rows)
    assert "bioactivity" not in {column.lower() for column in rows[0]}
    assert "mic" not in {column.lower() for column in rows[0]}


def test_only_the_three_one_to_one_exact_matches_are_seeded(records):
    claims = {
        (record["identifier"], producer["biosynthetic_gene_cluster"])
        for _, record in records
        for producer in record.get("producer_organisms") or []
        if producer.get("source") == "MIBIG"
    }
    assert claims == {
        ("CHEBI:60821", "BGC0000432"),
        ("CHEBI:60828", "BGC0000432"),
        ("CHEBI:28001", "BGC0000455"),
    }
    # BGC0000311 balhimycin has only a connectivity-block match and must remain
    # rejected until its stereochemical identity is resolved.
    assert all(bgc != "BGC0000311" for _, bgc in claims)


def test_reseed_replaces_only_the_mibig_owned_producer_slice():
    from seed_from_sources import merge_with_existing

    old_mibig = {
        "taxon_id": "NCBITaxon:1",
        "taxon_label": "old",
        "source": "MIBIG",
        "reviewed": True,
    }
    new_mibig = {
        "taxon_id": "NCBITaxon:2",
        "taxon_label": "new",
        "source": "MIBIG",
        "reviewed": True,
    }
    curated = {
        "taxon_id": "NCBITaxon:3",
        "taxon_label": "curator assertion",
        "reference": "PMID:1",
    }
    base = {
        "identifier": "CHEBI:1",
        "label": "example",
        "antimicrobial_class": "ANTIBACTERIAL",
        "curation_status": "SEEDED",
        "grounding_status": "EXACT",
        "curation_history": [],
    }
    fresh = dict(base) | {"producer_organisms": [new_mibig]}
    existing = dict(base) | {"producer_organisms": [old_mibig, curated]}
    assert merge_with_existing(fresh, existing)["producer_organisms"] == [new_mibig, curated]
