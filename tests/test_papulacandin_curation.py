"""Keep compound, species and reference-protein scope distinct in curated claims."""

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


def read(name):
    return json.loads((ROOT / "research" / name).read_text())


@pytest.fixture(scope="module")
def dossier():
    return read("2026-10-09-papulacandin-curation.json")


@pytest.fixture(scope="module")
def grounding():
    return read("2026-10-09-glucan-inhibitor-grounding.json")


@pytest.fixture(params=["papulacandin-b", "papulacandin-d"])
def record(request):
    path = ROOT / "data/antibiotics/antifungal" / (request.param + ".yaml")
    return path, load_record(path)


def test_exact_compound_and_species_claims(record, dossier):
    path, doc = record
    item = next(r for r in dossier["records"] if r["identifier"] == doc["identifier"])
    assert doc["resistance_mechanisms"] == item["claims"]
    expected = {
        "papulacandin-b": ("CHEBI:569624", "UJLFRJFJTPPIOK-RZGJRGQUSA-N", {"4932", "4896"}),
        "papulacandin-d": ("CHEBI:72630", "XKSZJTQIZHUMGA-HPZFVNCBSA-N", {"4896"}),
    }
    identifier, key, taxids = expected[path.stem]
    assert doc["identifier"] == identifier
    assert doc["chemical_structure"]["standard_inchi_key"] == key
    assert {c["taxon_id"].removeprefix("NCBITaxon:") for c in item["claims"]} == taxids
    assert len(item["claims"]) == len(taxids)
    assert doc["curation_status"] == "SEEDED"


def test_qualitative_scope_and_reference_only_proteins(record):
    _, doc = record
    for claim in doc["resistance_mechanisms"]:
        budding = claim["taxon_id"] == "NCBITaxon:4932"
        assert claim["gene_id"] == ("PBR1" if budding else "pbr1")
        assert claim["gene_families"] == (["FKS1"] if budding else ["bgs4"])
        assert claim["taxon_label"] == (
            "Saccharomyces cerevisiae" if budding else "Schizosaccharomyces pombe")
        assert claim["mechanism_type"] == "OTHER"
        assert claim["phenotype_label"] == "Author-reported " + doc["label"] + " resistance"
        assert "not resistance inferred from gene presence" in claim["note"]
        assert "not a tested allele or protein assignment" in claim["note"]
        assert "Figures were not independently reanalyzed" in claim["note"]
        assert "no numeric AST or clinical category is inferred" in claim["note"]
        assert ("X2180-1A" if budding else "972") in claim["note"]
        assert ("UniProtKB:P38631" if budding else "UniProtKB:O74475") in claim["note"]
        assert ("NCBITaxon:559292" if budding else "NCBITaxon:284812") in claim["note"]
        assert claim["evidence"][0]["reference"] == "PMID:7592316"
        assert not {
            "alteration", "protein_accession", "strain", "strain_taxon_id", "phenotype_id",
            "source", "source_version", "biosample_accession", "assembly_accession",
        }.intersection(claim)
        if budding:
            assert "non-resistant comparison at this locus" in claim["note"]
        else:
            assert "PomBase explicitly aliases pbr1 to bgs4" in claim["note"]
            assert "UniProt synonym list omits pbr1" in claim["note"]
    assert not doc.get("activity_spectrum")


def test_reference_versions_and_source_specific_aliases(grounding):
    proteins = {r["accession"]: r for r in grounding["reference_proteins"]}
    assert set(proteins) == {"UniProtKB:P38631", "UniProtKB:O74475"}
    fks1, bgs4 = proteins["UniProtKB:P38631"], proteins["UniProtKB:O74475"]
    assert (fks1["entry_version"], fks1["sequence_version"]) == (209, 2)
    assert (bgs4["entry_version"], bgs4["sequence_version"]) == (158, 1)
    assert "PBR1" in fks1["uniprot_synonyms"]
    assert "pbr1" not in bgs4["uniprot_synonyms"]
    assert grounding["pombase_alias_review"]["alias"] == "pbr1"
    assert grounding["pombase_alias_review"]["uniprot_cross_reference"] == "O74475"
    for row in proteins.values():
        assert row["request"]["release"] == "2026_03"
        assert row["role"] == "REFERENCE_LOCUS_NOT_EXACT_TESTED_ALLELE"
    taxa = {r["taxonId"]: r for r in grounding["taxonomy"]}
    for species, strain in ((4932, 559292), (4896, 284812)):
        assert taxa[species]["rank"] == "species"
        assert taxa[strain]["rank"] == "strain"
        assert taxa[strain]["parent"]["taxonId"] == species


def test_other_compounds_and_research_limits_preserved(grounding, dossier):
    for item in grounding["records"]:
        if item["identifier"] in {"CHEBI:72611", "antibioticmech:aro-de2f58b0cc"}:
            path = ROOT / item["path"]
            assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]
            assert not load_record(path).get("resistance_mechanisms")
    assert dossier["claims_added"] == 3
    assert dossier["records_changed"] == dossier["history_events_added"] == 2
    assert dossier["other_records_unchanged"] == 2937
    assert dossier["experimental_alleles_validated"] is False
    assert dossier["quantitative_ast_added"] is False
    assert dossier["whole_record_review_complete"] is False
    assert dossier["corpus_research_complete"] is False


def test_schema_and_reseeding_preserve_curator_slice_without_churn(record, dossier):
    path, doc = record
    assert not validate_antibiotic(doc, record_path=path)
    seeded = copy.deepcopy(doc)
    seeded.pop("resistance_mechanisms")
    seeded["curation_history"] = seeded["curation_history"][:-1]
    merged = merge_with_existing(seeded, doc)
    assert merged == doc
    assert emit_antibiotic_yaml(doc) == path.read_text()
    assert record_yaml_matches(path.read_text(), merged, record_path=path)
    item = next(r for r in dossier["records"] if r["identifier"] == doc["identifier"])
    assert doc["curation_history"][-1] == item["curation_event"]
    assert doc["curation_history"][-1]["action"] == "CURATED_RESISTANCE_EVIDENCE"


def test_ledger_updates_only_two_records_and_retains_review_status():
    def rows(name):
        with (ROOT / "research" / name).open(newline="") as stream:
            values = list(csv.DictReader(stream, delimiter="\t"))
        assert len(values) == 2939
        return {r["identifier"]: r for r in values}

    old = rows("2026-10-09-gm193663-resistance-grounding.tsv")
    new = rows("2026-10-09-papulacandin-resistance-grounding.tsv")
    assert old.keys() == new.keys()
    assert {key for key in old if old[key] != new[key]} == {"CHEBI:569624", "CHEBI:72630"}
    for key, count in (("CHEBI:569624", "2"), ("CHEBI:72630", "1")):
        assert new[key]["resistance_assertions"] == count
        assert new[key]["research_status"] == "PENDING_PRIMARY_REVIEW"
        assert new[key]["primary_papers_pending"] == "PMID:7592316"
        assert new[key]["verified_reference_accessions"] == new[key]["lineage_checked_taxids"] == ""
    assert sum(int(r["resistance_assertions"]) for r in new.values()) == 4788
    assert sum(r["research_status"] == "PENDING_DISCOVERY" for r in new.values()) == 2626


def test_reconciliation_pins_and_preservation():
    checkpoint = read("2026-10-09-papulacandin-checkpoint-reconciliation.json")
    for field in ("curation_dossier", "previous_ledger", "current_ledger"):
        pin = checkpoint[field]
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    assert checkpoint["records_changed"] == checkpoint["history_events_added"] == 2
    assert checkpoint["records_byte_identical"] == 2937
    assert checkpoint["ignored_files_included"] is True
    assert checkpoint["non_resistance_fields_preserved"] is True
