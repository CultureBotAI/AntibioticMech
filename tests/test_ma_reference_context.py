"""Reference scope must not imply experimental identity or phenotype verification."""

import copy
import csv
import hashlib
import json
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import embed_records as embed  # noqa: E402
import phibase_grounding_reviews as review  # noqa: E402
import seed_from_sources as seed  # noqa: E402

CONTEXT = ROOT / "research/2026-10-12-ma-reference-context.json"
TARGETS = {"CHEBI:28909": "iprodione", "CHEBI:81763": "fludioxonil"}


def test_context_pins_reference_scope_and_access_limits():
    doc = json.loads(CONTEXT.read_bytes())
    inventory = ROOT / doc["source_inventory"]["path"]
    assert hashlib.sha256(inventory.read_bytes()).hexdigest() == doc["source_inventory"]["sha256"]
    assert doc["scope"] == "LIMITED_REFERENCE_IDENTITY_REVIEW_NOT_EXPERIMENTAL_ALLELE_GROUNDING"
    assert set(doc["record_ids"]) == set(TARGETS)
    assert doc["source_associations"] == 4
    assert doc["primary_evidence"]["main_text_status"] == "ACCESS_LIMITED_NOT_FULLY_INSPECTED"
    assert doc["primary_evidence"]["license"] == "CC BY-NC 4.0"
    assert doc["primary_evidence"]["raw_artifacts"] == "LOCAL_IGNORED_CACHE_ONLY_NOT_ADOPTED_OR_REDISTRIBUTED"
    assert doc["decision"]["whole_record_review"] == doc["decision"]["primary_phenotype_review"] == "OPEN"
    assert doc["decision"]["new_measurements"] == 0
    assert doc["decision"]["new_genome_or_experimental_protein_ids"] == 0
    versions = {r["accession"]: (r["entry_version"], r["sequence_version"])
                for r in doc["reference_proteins"]}
    assert versions == {
        "UniProtKB:A7EQI8": (111, 1), "UniProtKB:A7F519": (97, 1),
    }
    assert all(not r["reviewed"] and r["taxon_id"] == "NCBITaxon:665079"
               and r["scope"] == "REFERENCE_ONLY_NOT_EXPERIMENTAL_SUBJECT"
               for r in doc["reference_proteins"])
    assert {r["taxon_id"]: r["rank"] for r in doc["taxonomy"]} == {
        "NCBITaxon:5180": "species", "NCBITaxon:665079": "strain",
    }


def test_owner_targets_only_four_pinned_rows():
    inventory = ROOT / "data/raw/phibase_amr.tsv"
    rows = list(csv.DictReader(inventory.open(), delimiter="\t"))
    decisions = review.load_reviews(inventory, rows)
    selected = [r for r in rows if r["pmid"] == "38374637"]
    assert len(selected) == 4
    assert {r["identifier"] for r in selected} == set(TARGETS)
    assert {r["strain_label"] for r in selected} == {"Scl02-05"}
    for row in selected:
        item = decisions[review.row_digest(row)]
        assert item["review_id"] == "ma-2024-reference-context"
        assert item["withhold"] == ["strain_taxon_id", "protein_accession"]
        assert item["reference"] == "DOI:10.1021/acs.jafc.3c08093.s001"
        assert not {"subject_strain", "subject_taxon", "withhold_strain", "misassigned"} & item.keys()


@pytest.mark.parametrize("identifier", TARGETS)
def test_live_claims_have_reference_provenance_not_subject_accessions(identifier):
    path = ROOT / f"data/antibiotics/antifungal/{TARGETS[identifier]}.yaml"
    doc = load_record(path)
    claims = [c for c in doc["resistance_mechanisms"]
              if c.get("source") == "PHIBASE" and c["evidence"][0]["reference"] == "PMID:38374637"]
    assert len(claims) == 2
    for claim in claims:
        assert not {"strain_taxon_id", "protein_accession", "gene_id"} & claim.keys()
        assert claim["taxon_id"] == "NCBITaxon:5180"
        assert claim["strain"] == "Scl02-05"
        assert claim["mechanism_type"] == "UNKNOWN"
        assert "not independently validated" in claim["note"]
        assert "Reference-only source identifiers:" in claim["note"]
        assert "strain_taxon_id=NCBITaxon:665079" in claim["note"]
        assert claim["evidence"][-1]["reference"] == "DOI:10.1021/acs.jafc.3c08093.s001"


def test_reseed_changes_only_identifier_scope_and_review_checksums(tmp_path):
    inventory = ROOT / "data/raw/phibase_amr.tsv"
    rows = list(csv.DictReader(inventory.open(), delimiter="\t"))
    old_review = json.loads(review.DEFAULT_REVIEW.read_bytes())
    old_review["reviews"] = [r for r in old_review["reviews"]
                             if r["review_id"] != "ma-2024-reference-context"]
    old_path = tmp_path / "old-review.json"
    old_path.write_text(json.dumps(old_review))
    fixture = {r["identifier"]: {"identifier": r["identifier"],
                               "chemical_structure": {"standard_inchi_key": r["standard_inchi_key"]}}
               for r in rows}
    before, after = copy.deepcopy(fixture), copy.deepcopy(fixture)
    previous_counts = seed.attach_phibase_resistance(before, grounding_review=old_path)
    assert previous_counts["reviewed_identifier_context"] == 185
    assert seed.attach_phibase_resistance(after)["reviewed_identifier_context"] == 189
    changed = refreshed = 0
    for identifier, old in before.items():
        new = after[identifier]
        assert embed.build_document(old, {}) == embed.build_document(new, {})
        for a, b in zip(old["resistance_mechanisms"], new["resistance_mechanisms"], strict=True):
            if a == b:
                continue
            fields = {k for k in a.keys() | b.keys() if a.get(k) != b.get(k)}
            if a["evidence"][0]["reference"] == "PMID:38374637":
                assert fields == {"strain_taxon_id", "protein_accession", "note", "evidence"}
                assert b["evidence"][:-1] == a["evidence"]
                changed += 1
            else:
                assert fields == {"evidence"}
                assert a["evidence"][:-1] == b["evidence"][:-1]
                assert a["evidence"][-1]["reference"] == b["evidence"][-1]["reference"]
                assert a["evidence"][-1]["notes"].split("SHA-256 ")[0] == (
                    b["evidence"][-1]["notes"].split("SHA-256 ")[0])
                refreshed += 1
    assert (changed, refreshed) == (4, 185)
