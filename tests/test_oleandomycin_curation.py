"""Biochemical routes must not become experimentally grounded resistance alleles."""

import copy
import csv
import hashlib
import json
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import emit_antibiotic_yaml, validate_antibiotic

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from seed_from_sources import is_card_sourced, merge_with_existing  # noqa: E402

PATH = ROOT / "data/antibiotics/antibacterial/oleandomycin.yaml"


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-oleandomycin-curation.json").read_bytes())


@pytest.fixture(scope="module")
def record():
    return load_record(PATH)


def test_two_biochemical_assertions_preserve_thirty_card_items(record, dossier):
    assert record["identifier"] == dossier["identifier"] == "CHEBI:16869"
    assert record["chemical_structure"]["standard_inchi_key"] == "RZPAKFUAFGMUPI-QESOVKLGSA-N"
    assert dossier["status"] == "CURATED_QUALITATIVE_BIOCHEMICAL_ROUTES"
    assert len(record["resistance_mechanisms"]) == 32
    original, added = record["resistance_mechanisms"][:30], record["resistance_mechanisms"][30:]
    assert all(is_card_sourced(c) for c in original)
    assert not any(is_card_sourced(c) for c in added)
    assert added == dossier["claims"]
    assert (
        hashlib.sha256(json.dumps(original, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        == (dossier["source_assertions_sha256"])
    )
    assert record["curation_status"] == "SEEDED"


@pytest.mark.parametrize(
    "gene,proteins",
    [
        ("oleI", {"UniProtKB:O68841", "UniProtKB:Q3HTL7"}),
        ("oleD", {"UniProtKB:Q53685", "UniProtKB:Q3HTL6"}),
    ],
)
def test_reference_context_stays_out_of_experimental_subject_slots(dossier, gene, proteins):
    (claim,) = [c for c in dossier["claims"] if c["gene_families"] == [gene]]
    assert claim["mechanism_type"] == "ANTIBIOTIC_INACTIVATION"
    assert {e["reference"] for e in claim["evidence"]} == proteins | {"PMID:9680207", "PMID:17376874"}
    assert (
        not {
            "taxon_id",
            "taxon_label",
            "strain",
            "strain_taxon_id",
            "protein_accession",
            "gene_id",
            "alteration",
            "phenotype_id",
            "phenotype_label",
            "assay",
            "source",
        }
        & claim.keys()
    )
    for text in (
        "not a measured whole-cell resistance",
        "reference NCBITaxon:1890, species rank",
        "distinct from",
        "Reference-only protein entries",
        "No class-wide substrate claim",
    ):
        assert text in claim["note"]
    assert all(
        "Reference identity only" in e["notes"] for e in claim["evidence"] if e["reference"] in proteins
    )


@pytest.mark.parametrize(
    "accession,gene,entry,seq,archive,protein",
    [
        ("O68841", "oleI", 77, 1, "AF055579", "AAC12648.1"),
        ("Q3HTL7", "oleI", 79, 2, "DQ195535", "ABA42118.2"),
        ("Q53685", "oleD", 100, 1, "Z22577", "CAA80301.1"),
        ("Q3HTL6", "oleD", 69, 2, "DQ195536", "ABA42119.2"),
    ],
)
def test_distinct_versioned_deposits_are_not_collapsed(
    dossier, accession, gene, entry, seq, archive, protein
):
    p = dossier["reference_proteins"][accession]
    assert p["accession"] == "UniProtKB:" + accession and p["gene_symbols"] == [gene]
    assert (p["entry_version"], p["sequence_version"]) == (entry, seq)
    assert p["archive_cross_references"] == [{"database": "EMBL", "id": archive, "protein_id": protein}]
    assert p["taxon_id"] == "NCBITaxon:1890" and p["taxon_label"] == "Streptomyces antibioticus"
    assert p["scope"] == "DATABASE_REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE_ASSIGNMENT"
    decision = dossier["reference_decisions"][gene]
    assert (
        decision["collapse_deposits"] is False and decision["same_experimental_allele_established"] is False
    )


def test_primary_archive_join_and_negative_context(dossier):
    first, second = dossier["primary_contexts"]
    assert first["reference"] == "PMID:9680207" and first["year"] == 1998
    assert first["paper_reported_deposit"] == "AF055579" and first["deposit_reference"] == "UniProtKB:O68841"
    assert first["donor"] == "Streptomyces antibioticus ATCC 11891"
    assert first["figures_visually_inspected"] is False
    assert first["access_mode"] == "PUBLISHER_INDEXED_TEXT"
    assert first["results_text_inspected"] is True and first["supplements_inspected"] is False
    for gene, accession in (("oleR", "O68843"), ("oleN2", "O68842")):
        decision = dossier["reference_decisions"][gene]
        assert decision["reference"] == "UniProtKB:" + accession
        assert decision["positive_resistance_assertion"] is False
        assert all(c["gene_families"] != [gene] for c in dossier["claims"])
    assert second["reference"] == "PMID:17376874"
    assert second["pdf_pages_visually_inspected"] == [2, 3, 5]
    correction = second["correction"]
    assert correction["doi"] == "10.1073/pnas.0704090104" and correction["content_inspected"] is True
    assert correction["pdf_page"] == 7 and correction["section"] == "BIOCHEMISTRY"
    assert correction["disposition"].startswith("AUTHOR_CONTRIBUTION_CREDIT")


def test_curator_slice_survives_reseeding_and_round_trip(record, dossier):
    seeded = copy.deepcopy(record)
    seeded["resistance_mechanisms"] = seeded["resistance_mechanisms"][:30]
    seeded["curation_history"] = seeded["curation_history"][:-1]
    assert merge_with_existing(seeded, record) == record
    assert emit_antibiotic_yaml(record) == PATH.read_text()
    assert not validate_antibiotic(record, record_path=PATH)
    assert record["curation_history"][-1] == dossier["curation_event"]
    assert dossier["history_events_added"] == 1
    assert not record.get("activity_spectrum")


def test_appended_claims_do_not_change_bounded_embedding_document(record):
    from embed_records import build_document, role_names

    before = copy.deepcopy(record)
    before["resistance_mechanisms"] = before["resistance_mechanisms"][:30]
    names = role_names()
    assert build_document(before, names) == build_document(record, names)
    assert "biochemical glycosylation of oleandomycin" not in build_document(record, names)


def test_versioned_receipts_do_not_confuse_blocked_access_with_results(dossier):
    expected = {"lit_pubmed:9680207": 3, "gene_exact:oleD AND taxonomy_id:1890": 2, "accession:Q3HTL7": 1}
    assert {r["query"]: r["result_count"] for r in dossier["uniprot_requests"]} == expected
    for r in dossier["uniprot_requests"]:
        assert urlsplit(r["url"]).hostname == "rest.uniprot.org"
        assert parse_qs(urlsplit(r["url"]).query)["query"] == [r["query"]]
        assert r["complete_for_query"] is True and r["release"] == "2026_03" and r["status"] == 200
        assert len(r["sha256"]) == len(r["cache"]["sha256"]) == 64
    receipts = {urlsplit(r["url"]).hostname: r for r in dossier["primary_access_receipts"]}
    assert receipts["onlinelibrary.wiley.com"]["status"] == 403
    assert receipts["europepmc.org"]["status"] == 403
    assert receipts["users.ox.ac.uk"]["status"] == receipts["ftp.forest.sr.unh.edu"]["status"] == 200
    taxon = dossier["taxonomy"]["1890"]
    assert taxon["active"] is True and taxon["rank"] == "species"
    assert dossier["taxonomy_scope"] == "REFERENCE_SPECIES_NOT_EXPERIMENTAL_RESISTANT_ORGANISM"


def test_public_pins_and_only_one_ledger_row_changed(dossier):
    checkpoint = json.loads(
        (ROOT / "research/2026-10-09-oleandomycin-checkpoint-reconciliation.json").read_bytes()
    )
    for pin in [
        dossier["parent_structural_audit"],
        dossier["record"],
        *[checkpoint[k] for k in ("curation_dossier", "previous_ledger", "current_ledger")],
    ]:
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]

    def rows(pin):
        with (ROOT / pin["path"]).open(newline="") as stream:
            result = list(csv.DictReader(stream, delimiter="\t"))
        assert len(result) == 2939
        return {r["identifier"]: r for r in result}

    old, new = rows(checkpoint["previous_ledger"]), rows(checkpoint["current_ledger"])
    assert old.keys() == new.keys()
    assert [key for key in old if old[key] != new[key]] == ["CHEBI:16869"]
    assert new["CHEBI:16869"]["resistance_assertions"] == "32"
    assert new["CHEBI:16869"]["research_status"] == "PENDING_PRIMARY_REVIEW"
    assert sum(int(r["resistance_assertions"]) for r in new.values()) == 4792
    assert checkpoint["curator_claims"] == 37 and checkpoint["curator_records"] == 24
    assert checkpoint["ignored_files_included"] is True
    assert checkpoint["records_byte_identical"] == 2938


def test_no_completed_record_or_new_operational_details(dossier):
    assert (
        dossier["whole_record_review_complete"] is False
        and dossier["experimental_alleles_validated"] is False
    )
    assert dossier["scope"]["whole_records_completed_by_this_review"] == 0
    assert dossier["scope"]["full_corpus_primary_review"] == "OPEN"

    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {
        "sequence",
        "features",
        "variants",
        "alteration",
        "mic",
        "measurement_value",
        "protocol",
        "primers",
        "coordinates",
    }
    assert "No NCBI request" in " ".join(dossier["limitations"])
