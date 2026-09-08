"""Acceptance tests for the MIBiG producer import."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from extract_mibig_producers import (  # noqa: E402
    LINK_EVIDENCE_METHODS,
    link_evidence_methods,
    reviewer_ids,
)


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


def _entry(*methods, status="active"):
    return {
        "status": status,
        "loci": [{"evidence": [{"method": method} for method in methods]}],
    }


def test_only_experimental_link_methods_admit_an_entry():
    """The gate is an allow-list, so a predicted link yields no methods at all.

    Deleting the membership test would let ``Homology-based prediction`` through,
    which is the whole distinction the gate exists to draw (#203).
    """
    assert link_evidence_methods(_entry("Knock-out studies")) == ["Knock-out studies"]
    assert link_evidence_methods(_entry("Homology-based prediction")) == []
    assert link_evidence_methods(
        _entry("Synthetic-bioinformatic natural product (syn-BNP)")) == []
    assert link_evidence_methods(
        _entry("Homology-based prediction", "Enzymatic assays")) == ["Enzymatic assays"]
    assert link_evidence_methods({}) == []


def test_the_allow_list_names_no_predictive_method():
    """A method added to the tuple without reading it would land here.

    The list is the admission gate; a predicted or synthetic link is not evidence
    that the named organism makes the compound.
    """
    forbidden = {
        "Homology-based prediction",
        "Synthetic-bioinformatic natural product (syn-BNP)",
    }
    assert forbidden.isdisjoint(LINK_EVIDENCE_METHODS)
    assert len(set(LINK_EVIDENCE_METHODS)) == len(LINK_EVIDENCE_METHODS)


def test_committed_mibig_inventory_is_evidenced_and_carries_no_activity_claims(repo_root):
    path = repo_root / "data" / "raw" / "mibig_producers.tsv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(rows) == 1462
    # Every row states which experiment supports its compound-to-producer link,
    # and every stated method is one the extractor's allow-list admits.
    assert all(row["link_evidence"] for row in rows)
    assert {method for row in rows for method in row["link_evidence"].split("|")} <= set(
        LINK_EVIDENCE_METHODS)
    # The changelog reviewer is retained as provenance but is no longer the gate,
    # so most admitted rows carry no expert review -- and none carries the
    # placeholder that made the old gate look stricter than it was.
    assert any(row["expert_reviewed"] == "false" for row in rows)
    assert all("AAAAAAAAAAAAAAAAAAAAAAAA" not in row["reviewer_ids"] for row in rows)
    assert all(row["primary_reference"] for row in rows)
    assert "bioactivity" not in {column.lower() for column in rows[0]}
    assert "mic" not in {column.lower() for column in rows[0]}


def test_only_exact_one_to_one_structure_matches_are_seeded(records):
    claims = {
        (record["identifier"], producer["biosynthetic_gene_cluster"])
        for _, record in records
        for producer in record.get("producer_organisms") or []
        if producer.get("source") == "MIBIG"
    }
    # The three matches the reviewer-field gate found are still here; widening
    # the gate to MIBiG's own link evidence added the rest (#203).
    assert {
        ("CHEBI:60821", "BGC0000432"),
        ("CHEBI:60828", "BGC0000432"),
        ("CHEBI:28001", "BGC0000455"),
    } <= claims
    assert len(claims) == 66
    # BGC0000311 balhimycin has only a connectivity-block match and must remain
    # rejected until its stereochemical identity is resolved.
    assert all(bgc != "BGC0000311" for _, bgc in claims)


def test_every_seeded_producer_says_which_experiment_supports_it(records):
    """A widened gate must not widen into unevidenced claims.

    Each seeded producer carries the MIBiG methods that admitted its entry, and
    `reviewed` is asserted only where MIBiG records a real expert reviewer -- it
    is no longer a blanket true, which is what made the old flag misleading.
    """
    allowed = set(LINK_EVIDENCE_METHODS)
    problems = []
    for _, record in records:
        for producer in record.get("producer_organisms") or []:
            if producer.get("source") != "MIBIG":
                continue
            methods = producer.get("link_evidence") or []
            if not methods or not set(methods) <= allowed:
                problems.append((record["identifier"], methods))
            if "reviewed" in producer and producer["reviewed"] is not True:
                problems.append((record["identifier"], "reviewed present but not true"))
    assert problems == [], problems[:10]


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
