"""Protect text-supported gene associations without asserting tested allele identity."""

import copy
import csv
import hashlib
import json
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import emit_antibiotic_yaml, validate_antibiotic

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from seed_from_sources import merge_with_existing, record_yaml_matches  # noqa: E402

PATH = ROOT / "data/antibiotics/antifungal/gm-193663.yaml"


@pytest.fixture(scope="module")
def record():
    return load_record(PATH)


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-gm193663-curation.json").read_text())


def test_exact_derivative_and_five_distinct_gene_groups(record, dossier):
    assert record["identifier"] == dossier["identifier"] == "CHEBI:77908"
    assert record["chemical_structure"]["standard_inchi_key"] == "YIJXUKFDZCRZIC-MYOGCEHNSA-N"
    claims = record["resistance_mechanisms"]
    assert claims == dossier["claims"] and len(claims) == 5
    assert {c["gene_id"] for c in claims} == {"DPH1", "DPH2", "DPH3", "DPH4", "DPH5"}
    assert record["curation_status"] == "SEEDED"


@pytest.mark.parametrize("gene,accession,reference_name", [
    ("DPH1", "P40487", "DPH1"), ("DPH2", "P32461", "DPH2"),
    ("DPH3", "Q3E840", "KTI11"), ("DPH4", "P47138", "JJJ3"),
    ("DPH5", "P32469", "DPH5"),
])
def test_reference_only_identity_and_qualitative_scope(record, gene, accession, reference_name):
    claim = next(c for c in record["resistance_mechanisms"] if c["gene_id"] == gene)
    assert claim["gene_families"] == [gene]
    assert claim["mechanism_type"] == "OTHER"
    assert claim["taxon_id"] == "NCBITaxon:4932"
    assert claim["taxon_label"] == "Saccharomyces cerevisiae"
    assert claim["phenotype_label"].startswith("Author-reported GM193663")
    assert "BY4741-derived" in claim["note"]
    assert "not resistance inferred from gene presence" in claim["note"]
    assert "Figures and supplements were not independently reanalyzed" in claim["note"]
    assert f"UniProtKB:{accession} ({reference_name}," in claim["note"]
    assert "NCBITaxon:559292" in claim["note"]
    assert "not an experimental allele or protein assignment" in claim["note"]
    assert {e["reference"] for e in claim["evidence"]} == {"PMID:18285480", "UniProtKB:" + accession}
    assert not {"alteration", "protein_accession", "strain", "strain_taxon_id", "phenotype_id",
                "source", "source_version", "biosample_accession", "assembly_accession"}.intersection(claim)


def test_no_ast_or_additional_drug_form_claims(record, dossier):
    assert not record.get("activity_spectrum")
    assert dossier["quantitative_ast_added"] is False
    assert dossier["experimental_alleles_validated"] is False
    assert dossier["whole_record_review_complete"] is False
    assert dossier["record_paths_changed"] == [str(PATH.relative_to(ROOT))]
    assert dossier["records_unchanged"] == 2938
    assert dossier["history_events_added"] == 1


def test_curator_slice_survives_reseeding_without_history_churn(record):
    seeded = copy.deepcopy(record)
    seeded.pop("resistance_mechanisms")
    seeded["curation_history"] = seeded["curation_history"][:-1]
    merged = merge_with_existing(seeded, record)
    assert merged == record
    assert record_yaml_matches(PATH.read_text(), merged, record_path=PATH)
    assert emit_antibiotic_yaml(record) == PATH.read_text()


def test_record_passes_closed_schema_and_history_matches_dossier(record, dossier):
    assert not validate_antibiotic(record, record_path=PATH)
    assert record["curation_history"][-1] == dossier["curation_event"]
    assert record["curation_history"][-1]["action"] == "CURATED_RESISTANCE_EVIDENCE"
    assert "figure review remains pending" in record["curation_history"][-1]["changes"]


def test_checkpoint_pins_public_dossier_and_both_ledgers():
    checkpoint = json.loads(
        (ROOT / "research/2026-10-09-gm193663-checkpoint-reconciliation.json").read_text()
    )
    for field in ("curation_dossier", "previous_ledger", "current_ledger"):
        pin = checkpoint[field]
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    assert checkpoint["records_changed"] == checkpoint["history_events_added"] == 1
    assert checkpoint["records_byte_identical"] == 2938
    assert checkpoint["protected_files_unchanged"] == 6465
    assert checkpoint["ignored_files_included"] is True


def test_current_ledger_updates_only_gm193663_without_promoting_review():
    def rows(name):
        with (ROOT / "research" / name).open(newline="") as handle:
            values = list(csv.DictReader(handle, delimiter="\t"))
        assert len(values) == 2939
        return {row["identifier"]: row for row in values}

    old = rows("2026-10-09-sdh8-resistance-grounding.tsv")
    new = rows("2026-10-09-gm193663-resistance-grounding.tsv")
    assert len(old) == len(new) == 2939 and old.keys() == new.keys()
    assert [key for key in old if old[key] != new[key]] == ["CHEBI:77908"]
    row = new["CHEBI:77908"]
    assert row["resistance_assertions"] == "5"
    assert row["research_status"] == "PENDING_PRIMARY_REVIEW"
    assert row["primary_papers_pending"] == "PMID:18285480"
    assert row["verified_reference_accessions"] == row["lineage_checked_taxids"] == ""
    assert sum(int(r["resistance_assertions"]) for r in new.values()) == 4785
    assert sum(r["research_status"] == "PENDING_DISCOVERY" for r in new.values()) == 2628
