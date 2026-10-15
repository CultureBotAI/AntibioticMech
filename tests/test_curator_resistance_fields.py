"""Field indexing must not promote citations to experimental assignments."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_curator_resistance_fields as audit  # noqa: E402
from seed_from_sources import CARD_NOTE_MARKER, PHIBASE_NOTE_MARKER  # noqa: E402


@pytest.mark.parametrize("value,identifier", [
    ("UniProtKB:P20081", "UniProtKB:P20081"),
    ("https://www.uniprot.org/uniprotkb/P20081/entry", "UniProtKB:P20081"),
    ("https://rest.uniprot.org/uniprotkb/P20081.json", "UniProtKB:P20081"),
    ("http://www.uniprot.org/uniprot/P20081", "UniProtKB:P20081"),
    ("UniProtKB:A0A7G4P320", "UniProtKB:A0A7G4P320"),
    ("UniProtKB:P20081-2", "UniProtKB:P20081-2"),
    ("UniParc:UPI000005318F", "UniParc:UPI000005318F"),
    ("https://www.uniprot.org/uniparc/UPI000005318F", "UniParc:UPI000005318F"),
    ("https://rest.uniprot.org/taxonomy/4932", "NCBITaxon:4932"),
    ("NCBITaxon:4932", "NCBITaxon:4932"),
    ("PMID:12345", "PMID:12345"),
    ("DOI:10.1093/nar/gkn642", "DOI:10.1093/nar/gkn642"),
    ("https://doi.org/10.1093/nar/gkn642", "DOI:10.1093/nar/gkn642"),
    ("https://dx.doi.org/10.1093%2Fnar%2Fgkn642", "DOI:10.1093/nar/gkn642"),
])
def test_explicit_reference_forms(value, identifier):
    assert audit.normalize_reference(value)["identifier"] == identifier


@pytest.mark.parametrize("value", [
    "", "P20081", "See UniProtKB:P20081", "UniProtKB:UPI000005318F", "UniProtKB:P20081x",
    "NCBITaxon:0", "NCBITaxon:04932", "PMID:-1", "DOI:not-a-doi",
    "https://uniprot.org.example.com/uniprotkb/P20081/entry",
    "https://www.uniprot.org@evil.example/uniprotkb/P20081/entry",
    "https://evil.example@www.uniprot.org/uniprotkb/P20081/entry",
    "https://@www.uniprot.org/uniprotkb/P20081/entry",
    "https://www.uniprot.org:0/uniprotkb/P20081/entry",
    "https://www.uniprot.org:443/uniprotkb/P20081/entry",
    "https://www.uniprot.org/uniprotkb/P20081/entry?query=other",
    "https://www.uniprot.org/uniprotkb/P20081/entry#other",
    "https://www.uniprot.org/uniprotkb/P20081/unexpected",
    "https://www.uniprot.org/uniprotkb/P20081/entry/more",
    "ftp://www.uniprot.org/uniprotkb/P20081/entry",
    "https://[broken", "https://www.uniprot.org:bad/uniprotkb/P20081",
    "https://www.uni\nprot.org/uniprotkb/P20081/entry",
    " https://www.uniprot.org/uniprotkb/P20081/entry",
    "https://www.uniprot.org/uniprotkb/P20081/entry\x00",
])
def test_no_bare_symbol_or_lookalike_mapping(value):
    assert audit.normalize_reference(value) is None


def project(**changes):
    record = {"identifier": "CHEBI:1", "path": "data/antibiotics/test.yaml", "sha256": "a" * 64,
              "standard_inchi_key": "TEST"}
    claim = {"label": "PRIVATE CLAIM", "gene_id": "PRIVATE GENE",
             "alteration": "PRIVATE ALTERATION", "taxon_id": "NCBITaxon:4932",
             "note": "PRIVATE NOTE UniProtKB:P20081",
             "evidence": [{"reference": "https://www.uniprot.org/uniprotkb/P20081/entry"},
                          {"reference": "PRIVATE UNCLASSIFIED REFERENCE"}]}
    claim.update(changes)
    baseline = copy.deepcopy(claim)
    result = audit.project_claim(record, 3, claim)
    assert claim == baseline
    assert result["resistance_index"] == 3
    assert "PRIVATE" not in json.dumps(result)
    return result


@pytest.mark.parametrize("fields,state", [
    ({}, "GENE_ID_ONLY"),
    ({"gene_families": ["PRIVATE FAMILY"]}, "BOTH_FIELDS"),
    ({"gene_id": "", "gene_families": ["PRIVATE FAMILY"]}, "GENE_FAMILIES_ONLY"),
    ({"gene_id": ""}, "NEITHER_FIELD"),
])
def test_optional_gene_fields_are_not_missing_identity_verdicts(fields, state):
    result = project(**fields)
    assert result["gene_field_state"] == state
    assert result["protein_accession_slot"] is None
    assert result["experimental_identity_assessed_by_this_index"] is False


def test_slots_and_repeated_citations_remain_distinct():
    claim = project(protein_accession="UniProtKB:Q08986", evidence=[
        {"reference": "UniProtKB:P20081"},
        {"reference": "https://www.uniprot.org/uniprotkb/P20081/entry"},
        {"reference": "UniParc:UPI000005318F"},
    ])
    assert claim["protein_accession_slot"] == "UniProtKB:Q08986"
    assert len(claim["recognized_citations"]) == 3
    summary = audit.summarize([claim])
    assert summary["claims_citing_each_namespace"] == {"UniParc": 1, "UniProtKB": 1}
    assert summary["distinct_cited_uniprot_accessions"] == 1
    assert summary["claims_with_protein_accession_slot"] == 1


def test_notes_are_not_automatically_grounded():
    claim = project(evidence=[])
    assert claim["recognized_citations"] == []
    assert claim["unclassified_citations"] == []
    assert claim["protein_accession_slot"] is None


@pytest.mark.parametrize("value", ["PMID:12345", "UniParc:UPI000005318F", "P20081",
                                   "https://www.uniprot.org/uniprotkb/P20081/entry"])
def test_protein_slot_cannot_be_a_citation_or_other_namespace(value):
    with pytest.raises(ValueError, match="protein accession slot"):
        project(protein_accession=value)


@pytest.mark.parametrize("claim,expected", [
    ({"evidence": []}, "CURATOR"),
    ({"source": "PHIBASE"}, "PHIBASE"),
    ({"note": PHIBASE_NOTE_MARKER}, "PHIBASE"),
    ({"evidence": [{"reference": "ARO:123", "notes": CARD_NOTE_MARKER}]}, "CARD"),
    ({"evidence": [{"reference": "ARO:123"}]}, "CURATOR"),
])
def test_ownership_uses_existing_source_rules(claim, expected):
    assert audit.owner(claim) == expected


def test_unknown_owner_fails_closed():
    with pytest.raises(ValueError, match="unhandled"):
        audit.owner({"source": "NEW_SOURCE"})


def test_conflicting_ownership_is_not_silently_counted():
    with pytest.raises(ValueError, match="conflicting"):
        audit.owner({"source": "PHIBASE", "evidence": [
            {"reference": "ARO:123", "notes": CARD_NOTE_MARKER},
        ]})


def test_source_owned_claim_is_not_projected_as_curator():
    with pytest.raises(ValueError, match="not a curator"):
        project(source="PHIBASE")


def test_census_drift_fails_closed(tmp_path):
    path = tmp_path / audit.CENSUS
    path.parent.mkdir(parents=True)
    path.write_text("changed")
    with pytest.raises(ValueError, match="census changed"):
        audit.build(tmp_path)


def test_full_corpus_replay_is_offline_and_matches_checkpoint(monkeypatch, pre_card_qualification_root):
    def fail(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(socket, "create_connection", fail)
    monkeypatch.setattr(socket.socket, "connect", fail)
    monkeypatch.setattr(requests.sessions.Session, "request", fail)
    result = audit.build(pre_card_qualification_root)
    assert result == json.loads((ROOT / audit.OUTPUT).read_bytes())
    summary = result["summary"]
    assert summary["corpus_records_checked"] == 2939
    assert summary["resistance_claims_by_owner"] == {"CARD": 4538, "CURATOR": 133, "PHIBASE": 217}
    assert summary["curator_claims"] == 133
    assert summary["curator_records"] == 54
    assert summary["claims_with_protein_accession_slot"] == 6
    assert summary["gene_field_states"] == {
        "BOTH_FIELDS": 20, "GENE_FAMILIES_ONLY": 87, "GENE_ID_ONLY": 24, "NEITHER_FIELD": 2,
    }
    assert summary["claims_citing_each_namespace"]["UniProtKB"] == 56
    assert summary["distinct_cited_uniprot_accessions"] == 48
    assert summary["claims_with_taxon_id_slot"] == 123
    assert summary["claims_with_taxon_label_but_no_taxon_id"] == 0
    assert summary["claims_with_unclassified_citations"] == 18
    assert summary["claims_without_taxon_label_or_id"] == 10
    assert {c["record_identifier"] for c in result["claims"]
            if c["gene_field_state"] == "NEITHER_FIELD"} == {"CHEBI:81419"}
    assert len({(c["record_identifier"], c["resistance_index"]) for c in result["claims"]}) == 133
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert all(not c["experimental_identity_assessed_by_this_index"] for c in result["claims"])
