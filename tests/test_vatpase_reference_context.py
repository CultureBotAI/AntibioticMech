"""Protect historical reference grounding without requiring ignored source caches."""

import copy
import csv
import hashlib
import io
import json
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import audit_vatpase_references as audit  # noqa: E402


@pytest.fixture
def dossier():
    return json.loads((ROOT / "research/2026-10-13-vatpase-reference-context.json").read_bytes())


def pinned_bytes(pin):
    raw = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == pin["sha256"]
    return raw


def test_historical_compounds_and_folimycin_alias(dossier, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    census = list(csv.DictReader(io.StringIO(pinned_bytes(dossier["inputs"]["census"]).decode()),
                                delimiter="\t"))
    assert len(census) == 2939 and set(dossier["records"]) == set(audit.TARGETS)
    for identifier, key in audit.TARGETS.items():
        record = dossier["records"][identifier]
        row, = [r for r in census if r["identifier"] == identifier]
        assert record["sha256"] == row["record_sha256"]
        assert record["standard_inchi_key"] == row["standard_inchi_key"] == key
        assert record["path"] == row["path"] and row["resistance_assertions"] == "0"
        assert record["whole_record_review"] == "OPEN" and not record["resistance_assertions_added"]
    discovery = json.loads(pinned_bytes(dossier["inputs"]["discovery"]))
    row, = [r for r in discovery["records"] if r["identifier"] == "CHEBI:73167"]
    alias, = [n for n in row["names"] if n["text"] == "folimycin"]
    assert not alias["shared_with_record_ids"]
    assert alias["origins"] == [{"kind": "SYNONYM", "index": 1, "source": "chebi",
                                  "synonym_type": "EXACT_SYNONYM"}]
    grounding = dossier["compound_name_grounding"]
    assert grounding["folimycin"]["identifier"] == "CHEBI:73167"
    assert grounding["folimycin"]["synonym"] == {
        "synonym_text": "folimycin", "synonym_type": "EXACT_SYNONYM", "source": "chebi"}
    assert not grounding["findings_transferred_between_compounds"]
    assert not grounding["tested_preparations_independently_reidentified"]


@pytest.mark.parametrize("gene,accession,version,loci,orfs", [
    ("vma-3", "P31413", 161, [], ["12F11.130", "NCU01332"]),
    ("VMA3", "P25515", 217, ["YEL027W"], []),
    ("VMA11", "P32842", 215, ["YPL234C"], ["P1064"]),
    ("VMA16", "P23968", 205, ["YHR026W"], []),
])
def test_distinct_versioned_subunits_not_experimental_subjects(
    dossier, gene, accession, version, loci, orfs,
):
    protein = dossier["reference_proteins"][gene]
    taxid, species, subunit = audit.REFERENCES[gene]
    assert protein["protein_accession"] == "UniProtKB:" + accession
    assert protein["entry_version"] == version and protein["sequence_version"] == 1
    assert protein["reference_gene"] == gene and gene in protein["gene_names"]
    assert protein["subunit"] == subunit
    assert protein["protein_name"] == "V-type proton ATPase subunit " + subunit
    assert protein["ordered_locus_names"] == loci and protein["gene_orf_names"] == orfs
    assert protein["reference_taxon_id"] == f"NCBITaxon:{taxid}"
    assert protein["source_species_taxon_id"] == f"NCBITaxon:{species}"
    assert protein["reference_taxon_rank"] == "strain" and protein["species_lineage_verified"]
    assert protein["role"] == "REFERENCE_PROTEOLIPID_NOT_EXPERIMENTAL_ALLELE"
    for key in ("exact_resistance_allele", "experimental_subject_assignment",
                "compound_specific_resistance_established", "focal_bibliography_matches"):
        assert not protein[key]
    assert all(not b["primary_results_reviewed"] for b in protein["bibliography"])
    ids = {i["id"].lower() for b in protein["bibliography"] for i in b["identifiers"]}
    assert not ids.intersection(audit.ACCESS)
    assert not ids.intersection(p["doi"] for p in audit.ACCESS.values())


def test_access_holds_not_promoted_to_primary_evidence(dossier):
    assert set(dossier["primary_leads"]) == set(audit.ACCESS)
    for pmid, expected in audit.ACCESS.items():
        paper = dossier["primary_leads"][pmid]
        assert all(paper[k] == v for k, v in expected.items())
        assert paper["pmid"] == pmid
        assert paper["observation_basis"].startswith("MANUAL_TOOL_OBSERVATION")
        for key in ("primary_results_verified", "native_figures_visually_inspected",
                    "local_primary_text_saved", "retry_or_alternate_transport"):
            assert not paper[key]
    assert dossier["primary_leads"]["16912037"]["outcome"] == "REQUEST_MADE_BUT_ACCESS_RESULT_NOT_RETAINED"


def test_bounded_uniprot_requests_and_taxonomy_reuse(dossier):
    assert set(dossier["uniprot_requests"]) == set(audit.QUERIES)
    for key, request in dossier["uniprot_requests"].items():
        url = urlparse(request["url"])
        assert url.scheme == "https" and url.netloc == "rest.uniprot.org"
        assert url.path == "/uniprotkb/search"
        assert parse_qs(url.query) == {"query": [audit.QUERIES[key]], "format": ["json"],
                                       "size": ["500"], "fields": [audit.reference.FIELDS]}
        assert request["status"] == 200 and request["release"] == "2026_03"
        assert request["results"] == (1 if key == "neurospora-c" else 3)
        assert request["complete_for_query"] and not request["all_strains_or_unreviewed_entries_searched"]
    neuro, yeast = [json.loads(pinned_bytes(p)) for p in dossier["inputs"]["taxonomy_dossiers"]]
    prior = {"367110": next(t["request"] for t in neuro["taxonomy"] if t["taxon_id"] == 367110),
             "559292": yeast["taxonomy_request"]}
    for taxid, old in prior.items():
        reused = dossier["taxonomy_reuse"][taxid]
        assert all(reused[k] == v for k, v in old.items())
        assert reused["reused_byte_identically"] and not reused["new_request"]


@pytest.fixture
def reference_entry():
    return {
        "entryType": "UniProtKB reviewed (Swiss-Prot)", "primaryAccession": "P31413",
        "entryAudit": {"entryVersion": 161, "sequenceVersion": 1},
        "organism": {"taxonId": 367110, "scientificName": "Neurospora crassa"},
        "genes": [{"geneName": {"value": "vma-3"}, "orfNames": [{"value": "NCU01332"}]}],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "V-type proton ATPase subunit c"}}},
    }


def project(entry):
    taxonomy = {"taxonId": 367110, "active": True, "rank": "strain",
                "scientificName": "Neurospora crassa reference strain",
                "lineage": [{"rank": "species", "taxonId": 5141}]}
    return audit.project_proteolipid(entry, "vma-3", taxonomy)


def test_orf_field_preserved_without_locus_upgrade(reference_entry):
    result = project(reference_entry)
    assert result["gene_orf_names"] == ["NCU01332"]
    assert result["ordered_locus_names"] == []
    assert not result["experimental_subject_assignment"]


@pytest.mark.parametrize("mutation", ["species", "subunit", "gene", "sequence", "features"])
def test_reference_projection_rejects_unsafe_conflations(reference_entry, mutation):
    entry = copy.deepcopy(reference_entry)
    if mutation == "species":
        entry["organism"]["taxonId"] = 559292
    elif mutation == "subunit":
        entry["proteinDescription"]["recommendedName"]["fullName"]["value"] += "'"
    elif mutation == "gene":
        entry["genes"][0]["geneName"]["value"] = "vma-1"
    else:
        entry[mutation] = []
    with pytest.raises(ValueError):
        project(entry)


def test_no_experimental_payload_or_completion_claims(dossier):
    counts = dossier["summary"]
    assert counts["selected_records"] == 2 and counts["reference_proteins"] == 4
    assert counts["corpus_records_in_scope"] == 2939
    for key in ("new_taxonomy_requests", "biological_records_changed", "new_phi_decisions",
                "experimental_accessions_assigned", "whole_records_completed"):
        assert counts[key] == 0
    previous = json.loads(pinned_bytes(dossier["inputs"]["prior_progress"]))
    assert previous["summary"]["phi_identifier_scoped_associations"] == 190
    assert previous["summary"]["phi_identifier_review_pending"] == 27
    forbidden = {"sequence", "features", "alteration", "variants", "mic", "construct", "protocol"}

    def check(value):
        if isinstance(value, dict):
            assert not forbidden.intersection(value)
            for child in value.values():
                check(child)
        elif isinstance(value, list):
            for child in value:
                check(child)

    check(dossier)
