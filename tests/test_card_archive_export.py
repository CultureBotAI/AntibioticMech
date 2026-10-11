"""Archive identity must retain each UniProt candidate and its reference scope."""

import json
from collections import defaultdict
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def export():
    return json.loads((ROOT / "research/2026-10-09-card-archive-groups.json").read_bytes())


def test_archive_export_retains_complete_candidate_membership_and_versions(export):
    audit = json.loads((ROOT / "research/2026-10-07-card-reference-grounding.json").read_bytes())
    candidates = {c["accession"]: c for d in audit["determinants"].values() for c in d["candidates"]}
    assert set(export["proteins"]) == set(candidates)
    for accession, candidate in candidates.items():
        protein = export["proteins"][accession]
        assert protein["entry_audit"] == candidate["entry_audit"]
        assert protein["reference_taxon_id"] == candidate["reference_taxon_id"]
    for key in ("source_inventory_sha256", "corpus_sha256", "protein_snapshot_sha256"):
        assert export[key] == audit[key]
    assert export["multiple_candidate_determinants"] == {
        aro: sorted(c["accession"] for c in row["candidates"])
        for aro, row in audit["determinants"].items() if len(row["candidates"]) > 1
    }


def test_archive_groups_are_exact_partitions_not_representative_selections(export):
    groups = defaultdict(list)
    absent = []
    for accession, protein in export["proteins"].items():
        if protein["uniparc_id"] is None:
            absent.append(accession)
        else:
            groups[protein["uniparc_id"]].append(accession)
    assert dict(groups) == export["archive_groups"]
    assert absent == export["proteins_without_archive_id"] == []
    assert export["summary"] == {
        "reference_proteins": 979, "archive_identifiers": 977, "shared_archive_identifiers": 2,
        "proteins_with_shared_archive_id": 4, "proteins_without_archive_id": 0,
    }


def test_both_ambiguous_pairs_share_archive_ids_but_keep_all_accessions(export):
    shared = {k: v for k, v in export["archive_groups"].items() if len(v) > 1}
    assert shared == {
        "UPI000162A5BF": ["UniProtKB:A0A1B1M202", "UniProtKB:A9Y8T8"],
        "UPI0000551E0C": ["UniProtKB:A0ACM8Q8E3", "UniProtKB:Q461P1"],
    }
    assert set(shared["UPI000162A5BF"]) == set(export["multiple_candidate_determinants"]["ARO:3002881"])
    assert set(shared["UPI0000551E0C"]) == set(export["multiple_candidate_determinants"]["ARO:3002709"])


def test_archive_export_cannot_be_mistaken_for_experimental_grounding(export):
    assert export["scope"] == "DATABASE_ARCHIVE_IDENTITY_ONLY_NOT_EXPERIMENTAL_ALLELE_GROUNDING"
    assert export["release"] == "2026_03"
    assert all(set(p) == {"uniparc_id", "entry_audit", "reference_taxon_id"}
               for p in export["proteins"].values())
    text = " ".join(export["limitations"])
    assert "no representative is chosen" in text
    assert "No sequence was fetched or compared" in text
    assert "not a tested allele or genomic locus" in text
