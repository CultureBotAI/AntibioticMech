"""Grounding is not a completed allele review or an isolate identification."""

import csv
import json
import sys
from pathlib import Path
from types import SimpleNamespace
from urllib.parse import urlencode

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_resistance_grounding as audit  # noqa: E402


@pytest.fixture
def snapshot(tmp_path, monkeypatch):
    output = tmp_path / "output"
    output.mkdir()
    monkeypatch.setattr(audit, "OUT", output)
    raw = tmp_path / "data/raw"
    raw.mkdir(parents=True)
    row = {
        "protein_accession": "PTEST",
        "taxon_id": "1",
        "taxon_label": "Source species",
        "strain_taxon_id": "2",
        "strain_label": "Experimental alias",
        "gene_id": "locus_transcript",
        "pmid": "123",
        "modification": "GENE(P2A) (amino acid mutation)",
        "identifier": "CHEBI:1",
    }
    path = raw / "phibase_amr.tsv"
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=row, delimiter="\t")
        writer.writeheader()
        writer.writerow(row)
    grounding = {
        "source_inventory_sha256": audit.digest(path.read_bytes()),
        "entries": {
            "PTEST": {
                "primaryAccession": "PTEST",
                "entryAudit": {"sequenceVersion": 2},
                "organism": {"taxonId": 2},
                "sequence": {"value": "MPAAAA"},
                "genes": [{"geneName": {"value": "GENE"}}],
                "uniProtKBCrossReferences": [{"id": "locus_transcript", "database": "EnsemblFungi"}],
            }
        },
        "taxa": {
            "1": {"taxonId": 1, "scientificName": "Current species", "synonyms": ["Source species"]},
            "2": {
                "taxonId": 2,
                "scientificName": "Reference strain",
                "lineage": [{"taxonId": 1}],
                "strains": [{"name": "Reference strain", "synonyms": ["Experimental alias"]}],
            },
        },
    }
    return tmp_path, grounding


def run(snapshot):
    root, grounding = snapshot
    audit.write("uniprot-grounding.json", grounding)
    audit.analyze(root)
    return json.loads((audit.OUT / "phibase-audit.json").read_text())["rows"][0]


def test_synonyms_and_strain_aliases_are_not_falsely_rejected(snapshot):
    row = run(snapshot)
    assert row["organism_status"] == "SOURCE_TAXON_IN_PROTEIN_LINEAGE"
    assert row["taxon_label_status"] == "LABEL_RECOGNIZED"
    assert row["strain_status"] == "STRAIN_ALIAS_RECOGNIZED_NOT_ISOLATE_PROOF"
    assert row["gene_id_status"] == "EXACT_IDENTIFIER_RECOGNIZED"
    assert row["candidate_coordinate_checks"][0]["coordinate_check"] == "MATCH"
    assert row["allele_evidence_status"] == "PRIMARY_PAPER_REVIEW_REQUIRED"
    assert row["source_paper_in_uniprot"] is False


def test_reference_species_does_not_verify_unlisted_experimental_strain(snapshot):
    snapshot[1]["taxa"]["2"]["strains"] = []
    assert run(snapshot)["strain_status"] == "STRAIN_REVIEW_REQUIRED"


def test_wrong_residue_is_a_review_flag_not_a_rewritten_allele(snapshot):
    snapshot[1]["entries"]["PTEST"]["sequence"]["value"] = "MAAAAA"
    row = run(snapshot)
    assert row["candidate_coordinate_checks"][0]["coordinate_check"] == "REVIEW_REQUIRED"
    assert row["source"]["modification"] == "GENE(P2A) (amino acid mutation)"


def test_fragment_requires_coordinate_review_even_when_residue_matches(snapshot):
    snapshot[1]["entries"]["PTEST"]["proteinDescription"] = {"flag": "Fragment"}
    row = run(snapshot)
    assert row["reference_is_fragment"] is True
    assert row["candidate_coordinate_checks"][0]["reference_residue"] == "P"
    assert row["candidate_coordinate_checks"][0]["coordinate_check"] == "REVIEW_REQUIRED"


def test_unresolved_accession_is_not_verified(snapshot):
    snapshot[1]["entries"] = {}
    row = run(snapshot)
    assert row["protein_status"] == "UNRESOLVED_ACCESSION"
    assert "primary_accession" not in row


def test_gene_symbol_does_not_replace_exact_source_locus(snapshot):
    snapshot[1]["entries"]["PTEST"]["uniProtKBCrossReferences"] = []
    assert run(snapshot)["gene_id_status"] == "GENE_ID_REVIEW_REQUIRED"


def test_incompatible_taxon_is_not_grounded(snapshot):
    snapshot[1]["taxa"]["2"]["lineage"] = [{"taxonId": 99}]
    assert run(snapshot)["organism_status"] == "LINEAGE_REVIEW_REQUIRED"


def test_source_drift_refuses_old_grounding(snapshot):
    snapshot[1]["source_inventory_sha256"] = "old"
    with pytest.raises(ValueError, match="inventory drift"):
        run(snapshot)


def test_redirects_are_not_followed_or_cached(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "OUT", tmp_path)
    monkeypatch.setattr(audit, "ALLOW_NETWORK", True)
    monkeypatch.setattr(audit.time, "sleep", lambda _: None)

    def get(url, **kwargs):
        assert url == "https://rest.uniprot.org/taxonomy/1"
        assert kwargs["allow_redirects"] is False
        return SimpleNamespace(url=url, status_code=302, text="", content=b"", headers={})

    monkeypatch.setattr(audit.requests, "get", get)
    assert audit.fetch("taxonomy/1")["status"] == 302
    assert not list(tmp_path.iterdir())


def test_missing_cache_does_not_enable_network(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "OUT", tmp_path)
    monkeypatch.setattr(audit, "ALLOW_NETWORK", False)
    with pytest.raises(ValueError, match="network is disabled"):
        audit.fetch("taxonomy/1")


@pytest.mark.parametrize("change", ["endpoint", "query", "duplicate", "origin", "fragment", "status", "body"])
def test_cached_response_must_match_the_requested_identity(tmp_path, monkeypatch, change):
    monkeypatch.setattr(audit, "OUT", tmp_path)
    monkeypatch.setattr(audit, "ALLOW_NETWORK", False)
    url = "https://rest.uniprot.org/uniprotkb/search"
    parameters = {"query": "accession:PTEST", "format": "json"}
    receipt = {"url": url + "?" + urlencode(parameters), "status": 200,
               "body": "{}", "sha256": audit.digest(b"{}"), "headers": {}}
    if change == "endpoint":
        receipt["url"] = receipt["url"].replace("uniprotkb/search", "taxonomy/search")
    elif change == "query":
        receipt["url"] = receipt["url"].replace("PTEST", "OTHER")
    elif change == "duplicate":
        receipt["url"] += "&format=json"
    elif change == "origin":
        receipt["url"] = receipt["url"].replace("rest.uniprot.org", "example.org")
    elif change == "fragment":
        receipt["url"] += "#unverified"
    elif change == "status":
        receipt["status"] = 404
    else:
        receipt["body"] = '{"changed":true}'
    key = audit.digest(json.dumps([url, parameters], sort_keys=True).encode())
    audit.write("request-" + key + ".json", receipt)
    with pytest.raises(ValueError, match="cache"):
        audit.fetch("uniprotkb/search", parameters)


def test_cache_accepts_equivalent_query_encoding_and_order(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "OUT", tmp_path)
    monkeypatch.setattr(audit, "ALLOW_NETWORK", False)
    url = "https://rest.uniprot.org/uniprotkb/search"
    parameters = {"query": "gene name", "format": "json"}
    receipt = {"url": url + "?format=json&query=gene%20name", "status": 200,
               "body": "{}", "sha256": audit.digest(b"{}"), "headers": {}}
    key = audit.digest(json.dumps([url, parameters], sort_keys=True).encode())
    audit.write("request-" + key + ".json", receipt)
    assert audit.fetch("uniprotkb/search", parameters) == receipt


def test_mismatched_successful_response_is_not_cached(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "OUT", tmp_path)
    monkeypatch.setattr(audit, "ALLOW_NETWORK", True)

    def get(url, **kwargs):
        assert url == "https://rest.uniprot.org/taxonomy/1"
        assert kwargs["allow_redirects"] is False
        return SimpleNamespace(url="https://rest.uniprot.org/taxonomy/2", status_code=200,
                               text="{}", content=b"{}", headers={})

    monkeypatch.setattr(audit.requests, "get", get)
    with pytest.raises(ValueError, match="cache response"):
        audit.fetch("taxonomy/1")
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("failure", [audit.requests.Timeout, audit.requests.ConnectionError])
def test_transient_network_failure_retries_and_caches_success(tmp_path, monkeypatch, failure):
    monkeypatch.setattr(audit, "OUT", tmp_path)
    monkeypatch.setattr(audit, "ALLOW_NETWORK", True)
    sleeps, calls = [], []
    monkeypatch.setattr(audit.time, "sleep", sleeps.append)

    def get(url, **kwargs):
        calls.append((url, kwargs))
        if len(calls) < 3:
            raise failure("temporary failure")
        return SimpleNamespace(url=url, status_code=200, text="{}", content=b"{}", headers={})

    monkeypatch.setattr(audit.requests, "get", get)
    assert audit.fetch("taxonomy/1")["status"] == 200
    assert len(calls) == 3
    assert sleeps == [1, 2, 0.15]
    assert len(list(tmp_path.glob("request-*.json"))) == 1
    assert audit.fetch("taxonomy/1")["status"] == 200
    assert len(calls) == 3


@pytest.mark.parametrize("failure", [audit.requests.Timeout, audit.requests.ConnectionError])
def test_persistent_network_failure_is_bounded_and_not_cached(tmp_path, monkeypatch, failure):
    monkeypatch.setattr(audit, "OUT", tmp_path)
    monkeypatch.setattr(audit, "ALLOW_NETWORK", True)
    sleeps, calls = [], []
    monkeypatch.setattr(audit.time, "sleep", sleeps.append)

    def get(url, **kwargs):
        calls.append(url)
        raise failure("persistent failure")

    monkeypatch.setattr(audit.requests, "get", get)
    with pytest.raises(failure, match="persistent failure"):
        audit.fetch("taxonomy/1")
    assert len(calls) == 3
    assert sleeps == [1, 2]
    assert not list(tmp_path.iterdir())
