"""Keep conditional gene associations distinct from exact allele assignments."""

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

PATH = ROOT / "data/antibiotics/antimycobacterial/canthin-6-one.yaml"


@pytest.fixture(scope="module")
def record():
    return load_record(PATH)


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-canthin-curation.json").read_bytes())


def test_exact_compound_and_two_associations_from_one_study(record, dossier):
    assert record["identifier"] == dossier["identifier"] == "CHEBI:3363"
    assert record["chemical_structure"]["standard_inchi_key"] == "ZERVJPYNQLONEK-UHFFFAOYSA-N"
    assert record["resistance_mechanisms"] == dossier["claims"]
    assert [c["gene_id"] for c in dossier["claims"]] == ["YAP1", "FLR1"]
    assert dossier["independent_studies"] == 1
    assert record["curation_status"] == "SEEDED"


@pytest.mark.parametrize("gene,accession,locus,version", [
    ("YAP1", "P19880", "YML007W", "entry version 230, sequence version 2"),
    ("FLR1", "P38124", "YBR008C", "entry version 171, sequence version 1"),
])
def test_species_grounding_and_reference_only_proteins(record, gene, accession, locus, version):
    claim = next(c for c in record["resistance_mechanisms"] if c["gene_id"] == gene)
    assert claim["mechanism_type"] == "OTHER" and claim["gene_families"] == [gene]
    assert claim["taxon_id"] == "NCBITaxon:4932"
    assert claim["taxon_label"] == "Saccharomyces cerevisiae"
    assert claim["phenotype_label"] == "Author-reported canthin-6-one tolerance"
    assert "Conditional gene associations" in claim["note"]
    assert f"UniProtKB:{accession} ({gene}, {locus}; NCBITaxon:559292)" in claim["note"]
    assert "not an experimental allele or protein assignment" in claim["note"]
    assert "Reference identity only" in claim["evidence"][1]["notes"]
    assert version in claim["evidence"][1]["notes"]
    assert {e["reference"] for e in claim["evidence"]} == {"PMID:23912082", "UniProtKB:" + accession}
    assert not {"alteration", "protein_accession", "strain", "strain_taxon_id", "source",
                "source_version", "phenotype_id", "assembly_accession", "biosample_accession"} & claim.keys()


def test_backgrounds_negative_comparisons_and_conflict_are_retained(record, dossier):
    yap, flr = record["resistance_mechanisms"]
    for claim in (yap, flr):
        for text in ("G175-W303", "BY4742 / EUROSCARF Y10000", "YPH250",
                     "not one experimental strain", "YCF1 was a negative comparison",
                     "not establish a direct drug target", "No MIC or clinical resistance category"):
            assert text in claim["note"]
    assert "Impaired growth without drug" in yap["note"]
    assert "basal FLR1-loss comparison did not increase sensitivity" in flr["note"]
    assert "YRR008C" in flr["note"] and "no new alias" in flr["note"]
    assert dossier["primary_context"]["figures_visually_inspected"] == [1, 3, 4, 5]
    ycf1, = [r for r in dossier["reference_proteins"] if r["gene_symbol"] == "YCF1"]
    assert ycf1["role"] == "NEGATIVE_COMPARISON_REFERENCE"
    assert ycf1["experimental_assignment"] is False


def test_no_ast_target_or_completed_review_inferred(record, dossier):
    assert not record.get("activity_spectrum") and not record.get("molecular_targets")
    assert dossier["quantitative_ast_added"] is False
    assert dossier["whole_record_review_complete"] is False
    assert dossier["experimental_alleles_validated"] is False
    assert dossier["history_events_added"] == 1 and dossier["records_unchanged"] == 2938
    assert dossier["record_paths_changed"] == [str(PATH.relative_to(ROOT))]


def test_curator_slice_survives_reseeding_without_history_churn(record, dossier):
    seeded = copy.deepcopy(record)
    seeded.pop("resistance_mechanisms")
    seeded["curation_history"] = seeded["curation_history"][:-1]
    merged = merge_with_existing(seeded, record)
    assert merged == record
    assert record_yaml_matches(PATH.read_text(), merged, record_path=PATH)
    assert emit_antibiotic_yaml(record) == PATH.read_text()
    assert not validate_antibiotic(record, record_path=PATH)
    assert record["curation_history"][-1] == dossier["curation_event"]


def test_public_pins_and_single_record_ledger_transition(dossier):
    checkpoint = json.loads(
        (ROOT / "research/2026-10-09-canthin-checkpoint-reconciliation.json").read_bytes())
    for pin in [dossier["reference_grounding"], dossier["record"], *[
            checkpoint[k] for k in ("curation_dossier", "previous_ledger", "current_ledger")]]:
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]

    def rows(pin):
        with (ROOT / pin["path"]).open(newline="") as stream:
            result = list(csv.DictReader(stream, delimiter="\t"))
        assert len(result) == 2939
        return {row["identifier"]: row for row in result}

    old, new = rows(checkpoint["previous_ledger"]), rows(checkpoint["current_ledger"])
    assert old.keys() == new.keys()
    assert [key for key in old if old[key] != new[key]] == ["CHEBI:3363"]
    assert new["CHEBI:3363"]["resistance_assertions"] == "2"
    assert new["CHEBI:3363"]["research_status"] == "PENDING_PRIMARY_REVIEW"
    assert new["CHEBI:3363"]["verified_reference_accessions"] == ""
    assert sum(int(r["resistance_assertions"]) for r in new.values()) == 4790
    assert checkpoint["curator_claims"] == 35 and checkpoint["curator_records"] == 23
    assert checkpoint["ignored_files_included"] is True
