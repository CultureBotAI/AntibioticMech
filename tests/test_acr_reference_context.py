"""Acr query hits, ontology members and review articles are not experimental alleles."""

import builtins
import copy
import hashlib
import io
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_acr_reference_context as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def assessment():
    return audit.read_json(ROOT, result()["assessment"])


def test_portable_artifact_binds_entire_cohort_and_preserves_current_claims(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    d = result()
    plan = audit.read_json(ROOT, d["plan"])
    index = audit.read_json(ROOT, d["inputs"]["index"])
    update = audit.read_json(ROOT, d["inputs"]["corpus_update"])
    definitions = audit.read_json(ROOT, d["inputs"]["definition_citations"])
    explicit = audit.read_json(ROOT, d["inputs"]["members"])
    labels = audit.cohort(ROOT, index)
    assert sorted(labels) == plan["expected_terms"] and len(labels) == 11
    assert len(d["records"]) == 16 and len(d["claims"]) == 31
    notes = assessment()
    audit.validate_assessment(notes)
    assert d["terms"] == {
        t: audit.term_view(t, label, index, definitions, explicit, d["citation_queries"], notes)
        for t, label in labels.items()
    }
    deltas = {r["identifier"]: r for r in update["record_deltas"]}
    claims = copy.deepcopy([c for c in index["claims"] if c["aro_id"] in labels])
    for c in claims:
        if c["record_identifier"] in deltas:
            delta = deltas[c["record_identifier"]]
            assert c["record_sha256"] == delta["before_sha256"]
            c["record_sha256"] = delta["after_sha256"]
    assert d["claims"] == claims
    records = {r["identifier"]: r for r in d["records"]}
    for c in claims:
        assert c["record_sha256"] == records[c["record_identifier"]]["record_sha256"]
        assert c["standard_inchi_key"] == records[c["record_identifier"]]["standard_inchi_key"]
    assert all(not t["experimental_allele_assignment"] for t in d["terms"].values())
    assert all(not t["experimental_subject_or_genome_assignment"] for t in d["terms"].values())


def test_unqueried_citations_are_not_zero_hit_queries():
    queries = result()["citation_queries"]
    pending = [q for q in queries.values() if not q["complete_for_query"]]
    empty = [q for q in queries.values() if q["complete_for_query"] and q["result_count"] == 0]
    assert len(pending) == 8 and len(empty) == 7
    assert all(q["result_count"] is None and "accessions" not in q for q in pending)
    assert all(q["accessions"] == [] for q in empty)
    assert all(q["biological_absence_inferred"] is False for q in queries.values())
    assert queries["14706082"]["result_count"] == 0
    assert queries["10692383"]["accessions"] == ["UniProtKB:P24177"]


def test_cached_query_replay_keeps_missing_empty_and_nonempty_separate(tmp_path, monkeypatch):
    provenance = {"complete_for_query": True, "release": "2026_03"}
    plan = {"queries": {p: {"directory": p, "query": provenance} for p in ("1", "2")}}

    def read(root, directory, pmid):
        return ({"TEST": {"primaryAccession": "TEST"}} if pmid == "1" else {}), provenance

    monkeypatch.setattr(audit.literature, "read_query", read)
    queries, pools = audit.replay_queries(tmp_path, {"1", "2", "3"}, plan)
    assert pools == {"1": ["TEST"], "2": []}
    assert [queries[p]["result_count"] for p in ("1", "2", "3")] == [1, 0, None]
    assert queries["1"]["unselected_hits_promoted_to_references"] is False


@pytest.mark.parametrize("mutation", ["incomplete", "release", "receipt", "sequence", "features", "comments"])
def test_cached_queries_reject_drift_and_operational_payloads(tmp_path, monkeypatch, mutation):
    provenance = {"complete_for_query": True, "release": "2026_03"}
    plan = {"queries": {"1": {"directory": "cache", "query": copy.deepcopy(provenance)}}}
    entry = {"primaryAccession": "TEST"}
    if mutation == "incomplete":
        provenance["complete_for_query"] = False
    elif mutation == "release":
        provenance["release"] = "2026_04"
    elif mutation == "receipt":
        provenance["extra"] = True
    else:
        entry[mutation] = {}
    monkeypatch.setattr(audit.literature, "read_query", lambda *args: ({"TEST": entry}, provenance))
    with pytest.raises(ValueError):
        audit.replay_queries(tmp_path, {"1"}, plan)


def test_membership_does_not_make_repressors_structural_components():
    d = result()
    parent = d["terms"]["ARO:3004083"]["explicit_member_context"]
    regulator = [e for e in parent["member_edges"] if e["member_label"] == "AcrS"]
    assert len(regulator) == 1 and regulator[0]["property_label"] == "part_of"
    assert regulator[0]["reference_candidates"] == ["UniProtKB:P0ACT2"]
    assert not regulator[0]["biological_composition_independently_verified"]
    assert not parent["complete_biological_membership_established"]
    assert parent["parent_protein_accession_assignment"] is None
    assert d["terms"]["ARO:3004082"]["explicit_member_context"] is None
    assert not d["limits"]["whole_complex_composition_verified"]


def test_native_reference_taxa_and_versions_remain_separate():
    d = result()
    refs = d["reference_views"]
    assert len(refs) == 8 and len(d["taxonomy_sources"]) == 4
    assert refs["UniProtKB:P24177"]["reference_taxonomy"]["taxon_id"] == "NCBITaxon:83333"
    assert refs["UniProtKB:A0A1X3IY90"]["reference_taxonomy"]["taxon_id"] == "NCBITaxon:656447"
    assert refs["UniProtKB:Q93K41"]["reference_taxonomy"]["taxon_id"] == "NCBITaxon:573"
    assert refs["UniProtKB:A0A0H2VTA2"]["reference_taxonomy"]["taxon_id"] == "NCBITaxon:623"
    assert refs["UniProtKB:P24177"]["entry_audit"] == {"entryVersion": 176, "sequenceVersion": 3}
    assert all(not r["whole_complex_identity_assignment"] for r in refs.values())
    assert d["limits"]["new_reference_assignments"] == 0
    assert d["limits"]["unrelated_yeast_acr_loci_merged"] is False


@pytest.mark.parametrize("field", audit.FALSE_FIELDS)
def test_assessment_cannot_be_promoted_to_experimental_curation(field):
    notes = assessment()
    notes[field] = True
    with pytest.raises(ValueError, match="scope promoted"):
        audit.validate_assessment(notes)


@pytest.mark.parametrize("mutation", ["kind", "terms", "doi", "url", "join", "ncbi", "retry"])
def test_review_article_and_access_scope_are_enforced(mutation):
    notes = assessment()
    row = notes["contexts"]["14706082"]
    if mutation == "kind":
        row["kind"] = "PRIMARY_EXPERIMENT_SELECTED_TEXT_CONTEXT"
    elif mutation == "terms":
        row["terms"].append("ARO:3000491")
    elif mutation in {"doi", "url"}:
        row[mutation] = "wrong"
    elif mutation == "join":
        row["exact_structure_and_subject_join_established"] = True
    else:
        notes["access"]["ncbi_endpoint_opened" if mutation == "ncbi" else "access_holds_retried"] = True
    with pytest.raises(ValueError):
        audit.validate_assessment(notes)


def test_complex_cannot_acquire_single_protein_link():
    d = result()
    index = audit.read_json(ROOT, d["inputs"]["index"])
    definitions = audit.read_json(ROOT, d["inputs"]["definition_citations"])
    explicit = audit.read_json(ROOT, d["inputs"]["members"])
    term = "ARO:3004082"
    index["terms"][term]["links"] = [{"protein_accession": "UniProtKB:P24177"}]
    with pytest.raises(ValueError, match="complex silently"):
        audit.term_view(
            term,
            d["terms"][term]["source_label"],
            index,
            definitions,
            explicit,
            d["citation_queries"],
            assessment(),
        )


def test_exports_exclude_sequences_variants_and_numeric_ast():
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    forbidden = {"sequence", "features", "variants", "alteration", "mic_value", "primers", "protocol"}
    assert not set(keys(result())) & forbidden
    assert not set(keys(assessment())) & forbidden


def cli_fixture(monkeypatch, root, check=False):
    payload = {"summary": {"terms": 0}}
    monkeypatch.setattr(audit, "build", lambda _: payload)
    argv = ["audit", "--root", str(root), "--output", "nested/audit.json"]
    monkeypatch.setattr(sys, "argv", argv + (["--check"] if check else []))
    return payload, root / "nested/audit.json"


def test_cli_creates_parent_and_does_not_rewrite_matching_output(tmp_path, monkeypatch):
    payload, path = cli_fixture(monkeypatch, tmp_path)
    audit.main()
    assert path.read_bytes() == (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    before = path.stat().st_mtime_ns
    audit.main()
    assert path.stat().st_mtime_ns == before


def test_check_mode_does_not_create_missing_directories(tmp_path, monkeypatch):
    _, path = cli_fixture(monkeypatch, tmp_path, check=True)
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not path.parent.exists()


@pytest.mark.parametrize("check", [False, True])
def test_cli_refuses_to_overwrite_prior_output(tmp_path, monkeypatch, check):
    _, path = cli_fixture(monkeypatch, tmp_path, check=check)
    path.parent.mkdir()
    path.write_bytes(b"prior output\n")
    with pytest.raises(ValueError, match="preserve prior output"):
        audit.main()
    assert path.read_bytes() == b"prior output\n"


def test_offline_replay_is_read_only(monkeypatch, pre_cdsa_qualification_root):
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    if not (ROOT / plan["inputs"]["protein_snapshot"]["path"]).exists():
        pytest.skip("local native caches unavailable; portable assertions still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not set(mode) & set("wax+"), "audit attempted a write"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    before = hashlib.sha256((ROOT / audit.OUTPUT).read_bytes()).hexdigest()
    assert audit.build(pre_cdsa_qualification_root) == result()
    assert hashlib.sha256((ROOT / audit.OUTPUT).read_bytes()).hexdigest() == before
