"""Pending research must retain exact compound identity and reference-only scope."""

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-08-pending-phi-identity-audit.json").read_text())


def test_pending_snapshot_has_unique_source_bindings(dossier):
    inventory = ROOT / "data/raw/phibase_amr.tsv"
    assert hashlib.sha256(inventory.read_bytes()).hexdigest() == dossier["source_inventory_sha256"]
    rows = list(csv.DictReader(inventory.open(), delimiter="\t"))
    by_digest = {
        hashlib.sha256(json.dumps(row, sort_keys=True, separators=(",", ":"),
                                  ensure_ascii=True).encode()).hexdigest(): row
        for row in rows
    }
    pending = dossier["pending_associations"]
    assert len(pending) == len({r["row_sha256"] for r in pending}) == 43
    assert len({r["reference"] for r in pending}) == 20
    for entry in pending:
        source = by_digest[entry["row_sha256"]]
        assert source["identifier"] == entry["identifier"]
        assert source["standard_inchi_key"] == entry["standard_inchi_key"]
        assert "PMID:" + source["pmid"] == entry["reference"]
        for field in ("protein_accession", "gene_id", "taxon_id", "taxon_label",
                      "strain_label", "strain_taxon_id", "phig_id"):
            assert entry["source_" + field] == (source[field] or None)
        assert entry["status"] == (
            "PENDING_IDENTIFIER_SCOPE_REVIEW_NOT_VERIFIED_EXPERIMENTAL_MAPPING"
        )


def test_compound_labels_are_derived_from_records_not_paper_titles(dossier):
    records = {}
    for entry in dossier["pending_associations"]:
        path = entry["record_path"]
        if path not in records:
            records[path] = load_record(ROOT / path)
        record = records[path]
        assert record["identifier"] == entry["identifier"]
        assert record["label"] == entry["record_label"]
        assert record["chemical_structure"]["standard_inchi_key"] == entry["standard_inchi_key"]
    assert len(records) == dossier["summary"]["pending_records"]
    groups = Counter((e["reference"], e["identifier"], e["record_label"])
                     for e in dossier["pending_associations"])
    assert groups == {(g["reference"], g["identifier"], g["record_label"]): g["associations"]
                      for g in dossier["paper_compound_groups"]}


@pytest.mark.parametrize("pmid,identifier,label,count", [
    ("1423663", "CHEBI:45979", "thiabendazole", 6),
    ("34490974", "CHEBI:136340", "fenpicoxamid", 2),
])
def test_focused_reviews_do_not_promote_abstracts(dossier, pmid, identifier, label, count):
    review, = [r for r in dossier["focused_reviews"] if r["reference"] == "PMID:" + pmid]
    assert (review["identifier"], review["record_label"], review["associations"]) == (
        identifier, label, count,
    )
    assert review["decision"] == "KEEP_PENDING_NO_BIOLOGICAL_EDIT"
    assert review["primary_access"].startswith("ABSTRACT_ONLY_")
    assert len([r for r in dossier["pending_associations"] if r["reference"] == "PMID:" + pmid]) == count


def test_reference_gene_crosswalk_does_not_resolve_g191(dossier):
    protein = dossier["proteins"]["P10653"]
    assert protein["genes"][0]["geneName"]["value"] == "benA"
    assert protein["genes"][0]["orfNames"] == [{"value": "AN1182"}]
    assert protein["entryAudit"]["entryVersion"] == 157
    assert protein["entryAudit"]["sequenceVersion"] == 1
    assert protein["organism"]["taxonId"] == 227321
    assert any(p == {"key": "ProteinId", "value": "CBF87981.1"}
               for x in protein["embl_cross_references"] for p in x["properties"])
    assert dossier["taxonomy"]["227321"]["rank"] == "strain"
    assert dossier["taxonomy"]["227321"]["parent"]["taxonId"] == 162425
    assert dossier["taxonomy"]["162425"]["rank"] == "species"
    assert {r["source_strain_label"] for r in dossier["pending_associations"]
            if r["reference"] == "PMID:1423663"} == {"G191"}


def test_cytb_submission_strain_is_not_an_experimental_subject(dossier):
    protein = dossier["proteins"]["Q6X9S4"]
    assert protein["genes"][0]["geneName"]["value"] == "cob"
    assert protein["genes"][0]["synonyms"] == [{"value": "cytB"}]
    assert protein["entryAudit"]["entryVersion"] == 84
    assert protein["entryAudit"]["sequenceVersion"] == 1
    assert protein["reference_strain_comments"] == ["ST1/MBC"]
    assert protein["organism"]["taxonId"] == 1047171
    assert dossier["taxonomy"]["1047171"]["rank"] == "species"
    assert {r["source_strain_label"] for r in dossier["pending_associations"]
            if r["reference"] == "PMID:34490974"} == {"IPO323", "37-16"}


def test_metadata_only_scope_and_provenance(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {
        "sequence", "features", "alteration", "modification", "activity_spectrum",
        "resistance_mechanisms", "experimental_protein_accession", "experimental_genome_accession",
    }
    assert dossier["preservation"] == {
        "record_hashes_verified": 2939, "biological_record_changes": 0,
        "curation_events_added": 0, "source_reviews_unchanged": True,
    }
    assert len(dossier["uniprot_requests"]) == 5
    for request in dossier["uniprot_requests"]:
        assert urlsplit(request["url"]).hostname == "rest.uniprot.org"
        assert request["status"] == 200
        assert request["release"] == "2026_03"
        assert len(request["sha256"]) == len(request["cache_file_sha256"]) == 64
    assert {c["doi"] for c in dossier["citations"].values()} == {
        "10.1002/cm.970220304", "10.1111/1462-2920.15760",
    }
