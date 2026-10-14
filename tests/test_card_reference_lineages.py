"""Taxonomy reference ancestry must not become an experimental assignment."""

import copy
import csv
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_reference_lineages as audit  # noqa: E402
from resistance_checkpoint_records import checkpoint_path  # noqa: E402


def taxon():
    return {"taxonId": 20, "rank": "strain", "scientificName": "Reference strain", "active": True,
            "parent": {"taxonId": 10, "scientificName": "Reference species"},
            "lineage": [{"taxonId": 1, "rank": "genus", "scientificName": "Reference"},
                        {"taxonId": 10, "rank": "species", "scientificName": "Reference species"}]}


def species():
    return {"taxonId": 10, "rank": "species", "scientificName": "Reference species", "active": True,
            "parent": {"taxonId": 1, "scientificName": "Reference"},
            "lineage": [{"taxonId": 1, "rank": "genus", "scientificName": "Reference"}]}


@pytest.mark.parametrize("change", ["inactive", "boolean_id", "blank_name", "duplicate", "cycle",
                                    "parent_id", "parent_name", "missing_lineage", "two_species"])
def test_corrupt_or_ambiguous_taxonomy_fails_closed(change):
    source = taxon()
    if change == "inactive":
        source["active"] = False
    elif change == "boolean_id":
        source["taxonId"] = True
    elif change == "blank_name":
        source["scientificName"] = " "
    elif change == "duplicate":
        source["lineage"].insert(0, copy.deepcopy(source["lineage"][0]))
    elif change == "cycle":
        source["lineage"][0]["taxonId"] = 20
    elif change == "parent_id":
        source["parent"]["taxonId"] = 11
    elif change == "parent_name":
        source["parent"]["scientificName"] = "Wrong"
    elif change == "missing_lineage":
        del source["lineage"]
    else:
        source["lineage"][0]["rank"] = "species"
    with pytest.raises(ValueError):
        audit.lineage(source)


def test_species_rank_is_self_and_strain_ancestry_is_not_an_experimental_subject():
    nodes, ancestor = audit.lineage(taxon())
    assert ancestor["taxonId"] == 10 and nodes[-1]["taxonId"] == 20
    taxa, parents = audit.project_taxa({"20": taxon()}, {"20": {"receipt": "example"}}, {}, {})
    assert taxa["20"]["species_relation"] == "ANCESTOR"
    assert taxa["20"]["species_taxon_id"] == "NCBITaxon:10"
    assert not taxa["20"]["experimental_subject_assignment"]
    assert not parents["10"]["standalone_active_verified"]
    assert parents["10"]["native_sources"] == []
    taxa, parents = audit.project_taxa(
        {"20": taxon(), "10": species()}, {"20": {}, "10": {}}, {}, {})
    assert taxa["10"]["species_relation"] == "SELF"
    assert parents["10"]["standalone_active_verified"]


def test_separately_cached_species_and_lineage_only_nodes_remain_distinct():
    _, parents = audit.project_taxa({"20": taxon()}, {"20": {}}, {"10": species()}, {"10": [{}]})
    assert parents["10"]["standalone_node_status"] == "ACTIVE_NATIVE_RESPONSE_VERIFIED"
    assert parents["10"]["native_sources"] == [{}]
    conflicting = species()
    conflicting["scientificName"] = "Different name"
    with pytest.raises(ValueError, match="disagrees"):
        audit.project_taxa({"20": taxon()}, {"20": {}}, {"10": conflicting}, {"10": [{}]})


def test_missing_species_is_not_invented_from_a_genus_or_name():
    source = taxon()
    source["lineage"][-1]["rank"] = "no rank"
    taxa, parents = audit.project_taxa({"20": source}, {"20": {}}, {}, {})
    assert parents == {} and taxa["20"]["species_taxon_id"] is None
    assert taxa["20"]["species_relation"] == "NO_SPECIES_RANK_IN_SELECTED_LINEAGE"


@pytest.mark.parametrize(("name", "expected"), [
    ("Streptomyces sp.", ["UNSPECIFIED_SPECIES_LABEL"]),
    ("uncultured bacterium A", ["UNCULTURED_LABEL", "BACTERIUM_PLACEHOLDER_WORD"]),
    ("mixed culture bacterium B", ["MIXED_CULTURE_LABEL", "BACTERIUM_PLACEHOLDER_WORD"]),
    ("Bifidobacterium longum", []), ("Mycobacterium smegmatis", []),
])
def test_literal_label_flags_do_not_match_genus_substrings(name, expected):
    assert audit.label_flags(name) == expected


@pytest.mark.parametrize("suffix", ["", ".json"])
def test_native_cache_accepts_both_taxonomy_endpoint_encodings(tmp_path, suffix):
    body = json.dumps(species()).encode()
    value = {"url": f"https://rest.uniprot.org/taxonomy/10{suffix}", "status": 200,
             "sha256": hashlib.sha256(body).hexdigest(), "body": body.decode(),
             "headers": {"X-UniProt-Release": "2026_03"}, "retrieved_at": "2026-10-14"}
    path = tmp_path / "request.json"
    path.write_text(json.dumps(value))
    item = {"receipt": audit.reference.pin(tmp_path, path), "body": None}
    result, _ = audit.native_taxon(tmp_path, item, "10", "2026_03")
    assert result == species()


@pytest.mark.parametrize("change", ["ncbi_host", "different_id", "query", "failed_status",
                                    "body_digest", "release", "pagination", "inactive"])
def test_native_response_identity_and_integrity_guards(tmp_path, change):
    source = species()
    if change == "inactive":
        source["active"] = False
    body = json.dumps(source).encode()
    value = {"url": "https://rest.uniprot.org/taxonomy/10", "status": 200,
             "sha256": hashlib.sha256(body).hexdigest(), "body": body.decode(),
             "headers": {"X-UniProt-Release": "2026_03"}, "retrieved_at": "2026-10-14"}
    if change == "ncbi_host":
        value["url"] = "https://www.ncbi.nlm.nih.gov/taxonomy/10"
    elif change == "different_id":
        value["url"] = "https://rest.uniprot.org/taxonomy/11"
    elif change == "query":
        value["url"] += "?query=unplanned"
    elif change == "failed_status":
        value["status"] = 403
    elif change == "body_digest":
        value["sha256"] = "0" * 64
    elif change == "release":
        value["headers"]["X-UniProt-Release"] = "different"
    elif change == "pagination":
        value["headers"]["Link"] = "unexpected"
    path = tmp_path / "request.json"
    path.write_text(json.dumps(value))
    item = {"receipt": audit.reference.pin(tmp_path, path), "body": None}
    with pytest.raises(ValueError):
        audit.native_taxon(tmp_path, item, "10", "2026_03")


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_public_export_covers_every_explicit_reference_without_selecting_representatives(dossier):
    prior = json.loads(audit.reference.check_pin(ROOT, dossier["inputs"]["references"]).read_bytes())
    expected = {tid: row for tid, row in prior["determinants"].items() if row["candidates"]}
    assert set(dossier["terms"]) == set(expected) and len(expected) == 978
    accessions = set()
    for tid, row in expected.items():
        actual = dossier["terms"][tid]
        assert actual["reference_accessions"] == [c["accession"] for c in row["candidates"]]
        assert not actual["experimental_subject_assignment"]
        accessions.update(actual["reference_accessions"])
    assert accessions == set(dossier["proteins"]) and len(accessions) == 979
    assert sum(len(t["reference_accessions"]) > 1 for t in dossier["terms"].values()) == 2


def test_public_species_references_bind_to_dated_native_sources_without_live_freeze(dossier, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    census_text = audit.reference.check_pin(ROOT, dossier["inputs"]["census"]).read_text()
    census = {r["identifier"]: r for r in csv.DictReader(
        census_text.splitlines(), delimiter="\t")}
    assert len(census) == 2939 and len(dossier["records"]) == 169
    for record in dossier["records"]:
        assert record["sha256"] == census[record["identifier"]]["record_sha256"]
        assert record["whole_record_primary_review"] == "OPEN"
    for protein in dossier["proteins"].values():
        taxon = dossier["taxa"][protein["reference_taxon_id"].split(":")[1]]
        assert protein["reference_taxon_rank"] == taxon["reference_rank"]
        assert protein["reference_species_taxon_id"] == taxon["species_taxon_id"]
        assert not protein["experimental_subject_assignment"] and not protein["exact_allele_assignment"]
    summary = dossier["summary"]
    assert summary["reference_taxa"] == len(dossier["taxa"]) == 360
    assert summary["species_lineage_nodes"] == len(dossier["species"]) == 288
    assert summary["species_nodes_with_standalone_response"] == 254
    assert summary["species_nodes_lineage_only"] == 34
    assert summary["additional_cached_species_nodes"] == 6
    for node in dossier["species"].values():
        assert node["standalone_active_verified"] == bool(node["native_sources"])


def test_mixed_and_uncultured_nodes_remain_ranked_but_not_identified_experimental_species(dossier):
    for taxid, flag in (("663178", "MIXED_CULTURE_LABEL"), ("155900", "UNCULTURED_LABEL"),
                        ("1931", "UNSPECIFIED_SPECIES_LABEL")):
        node = dossier["species"][taxid]
        assert node["rank"] == "species" and flag in node["label_flags"]
        assert not node["experimental_subject_assignment"]


def test_offline_native_replay(dossier, monkeypatch):
    if not (ROOT / audit.PLAN).exists():
        pytest.skip("optional native research cache not available")

    def denied(*args, **kwargs):
        raise AssertionError("offline taxonomy audit attempted network access")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    assert audit.build(ROOT, record_resolver=checkpoint_path) == dossier


def test_no_operational_or_experimental_values_are_exported(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {"sequence", "features", "alteration", "genes", "gene_id", "variants",
                                   "strain_taxon_id", "assembly_accession", "biosample_accession", "mic"}
    assert dossier["constraints"]["issue_1040"] == "DEFERRED"
    assert dossier["constraints"]["full_corpus_goal_status"] == "OPEN"
    assert dossier["summary"]["new_network_requests"] == dossier["summary"]["biological_record_changes"] == 0
