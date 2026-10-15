"""Reference names, citation ownership and taxa cannot establish resistant alleles."""

import builtins
import copy
import hashlib
import io
import json
import socket
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_pbp_reference_context as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def assessment():
    return audit.read_json(ROOT, result()["assessment"])


def cli_fixture(monkeypatch, root, *, check=False):
    payload = {"summary": {"terms": 0}}
    monkeypatch.setattr(audit, "build", lambda _: payload)
    args = ["audit", "--root", str(root), "--output", "nested/audit.json"]
    monkeypatch.setattr(sys, "argv", args + (["--check"] if check else []))
    return payload, root / "nested/audit.json"


def test_cli_creates_nested_output_only_in_write_mode(tmp_path, monkeypatch):
    payload, target = cli_fixture(monkeypatch, tmp_path)
    audit.main()
    assert target.read_bytes() == (json.dumps(payload, sort_keys=True, indent=2) + "\n").encode()
    before = target.stat().st_mtime_ns
    audit.main()
    assert target.stat().st_mtime_ns == before


def test_cli_check_does_not_create_missing_output_directories(tmp_path, monkeypatch):
    _, target = cli_fixture(monkeypatch, tmp_path, check=True)
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not target.parent.exists()


@pytest.mark.parametrize("check", [False, True])
def test_cli_never_overwrites_a_different_existing_output(tmp_path, monkeypatch, check):
    _, target = cli_fixture(monkeypatch, tmp_path, check=check)
    target.parent.mkdir()
    target.write_bytes(b"historical output\n")
    with pytest.raises(ValueError, match="preserve prior output"):
        audit.main()
    assert target.read_bytes() == b"historical output\n"


@pytest.mark.parametrize(
    "name,label,matched",
    [
        ("PBP-2X", "PBP2x", True),
        ("Penicillin-binding protein 1A", "PBP1a", True),
        ("PBP2a activator MacP", "PBP2a", False),
        ("Penicillin-binding protein 2a activator MacP", "PBP2a", False),
        ("Guiding PBP1-shuttling protein", "PBP1", False),
        ("PBP", "PBP4", False),
        ("Phosphate-binding protein PstS", "PBP4", False),
        ("PBP2a", "PBP2", False),
        ("PBP2", "PBP2a", False),
        ("PBP3 mutant", "PBP3", False),
        ("PBP3", "pbp3", True),
    ],
)
def test_complete_native_names_not_substrings_or_homonyms(name, label, matched):
    entry = {"proteinDescription": {"alternativeNames": [{"fullName": {"value": name}}]}}
    assert bool(audit.name_matches(entry, label)) is matched


def test_included_domains_and_gene_symbols_do_not_substitute_for_protein_identity():
    name = {"recommendedName": {"fullName": {"value": "PBP4"}}}
    entry = {"genes": [{"geneName": {"value": "pbp4"}}], "proteinDescription": {"includes": [name]}}
    assert audit.name_matches(entry, "PBP4") == []


@pytest.mark.parametrize("label", ["PBP", "PBP2a variant", "PBP2/3", "pbp2a1"])
def test_unsupported_source_labels_are_rejected(label):
    with pytest.raises(ValueError, match="unsupported"):
        audit.name_matches({}, label)


def test_species_and_unresolved_names_are_not_interchangeable():
    species = {"taxonId": 727, "rank": "species", "scientificName": "Haemophilus influenzae"}
    assert audit.reference_disposition(species, copy.deepcopy(species)).startswith("SAME_SPECIES_")
    assert audit.reference_disposition(None, species).startswith("SOURCE_NAME_UNRESOLVED_")
    for key, value in (("taxonId", 485), ("rank", "strain"), ("scientificName", "Another species")):
        other = {**species, key: value}
        assert audit.reference_disposition(species, other).startswith("DIFFERENT_SPECIES_")


def synthetic_source(root, mutation=None):
    directory = root / audit.CACHE
    directory.mkdir(parents=True)
    params = audit.parameters("999")
    url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(params)
    entry = {"primaryAccession": "TEST1", "entryType": "UniProtKB reviewed (Swiss-Prot)"}
    entries = [entry]
    headers = {"X-UniProt-Release": "2026_03", "X-Total-Results": "1"}
    if mutation == "sequence":
        entry["sequence"] = {}
    elif mutation == "unreviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif mutation == "duplicate":
        entries.append(copy.deepcopy(entry))
        headers["X-Total-Results"] = "2"
    elif mutation == "pagination":
        headers["Link"] = "<https://rest.uniprot.org/next>; rel=next"
    elif mutation == "release":
        headers["X-UniProt-Release"] = "2026_04"
    elif mutation == "count":
        headers["X-Total-Results"] = "2"

    def save(path, value):
        path.write_text(json.dumps(value))
        return audit.reference.pin(root, path)

    body = save(directory / "q-body.json", {"results": entries})
    plan = save(
        root / "query-plan.json",
        {
            "requests": {"q": {"url": url, "parameters": params}},
            "max_response_bytes": 10000,
        },
    )
    receipt = {
        "url": url,
        "status": 200,
        "headers": headers,
        "sha256": body["sha256"],
        "bytes": (root / body["path"]).stat().st_size,
        "retry_performed": False,
        "redirects_followed": False,
    }
    attempt = {"url": url, "plan_sha256": plan["sha256"], "retry_performed": False}
    if mutation == "url":
        receipt["url"] = url.replace("rest.uniprot.org", "example.org")
    elif mutation == "status":
        receipt["status"] = 403
    elif mutation == "checksum":
        receipt["sha256"] = "0" * 64
    elif mutation == "size":
        receipt["bytes"] += 1
    elif mutation == "redirect":
        receipt["redirects_followed"] = True
    elif mutation == "retry":
        receipt["retry_performed"] = True
    elif mutation == "plan":
        attempt["plan_sha256"] = "0" * 64
    save(directory / "q-receipt.json", receipt)
    save(directory / "q-attempt.json", attempt)
    return audit.source_for(root, "q", "query-plan.json")


def test_complete_metadata_query_replays(tmp_path):
    entries = audit.read_query(tmp_path, synthetic_source(tmp_path), "999")
    assert [e["primaryAccession"] for e in entries] == ["TEST1"]


@pytest.mark.parametrize(
    "mutation",
    [
        "sequence",
        "unreviewed",
        "duplicate",
        "pagination",
        "release",
        "count",
        "url",
        "status",
        "checksum",
        "size",
        "redirect",
        "retry",
        "plan",
    ],
)
def test_native_query_drift_fails_closed(tmp_path, mutation):
    with pytest.raises(ValueError):
        audit.read_query(tmp_path, synthetic_source(tmp_path, mutation), "999")


@pytest.mark.parametrize(
    "key",
    [
        "all_14_terms_primary_reviewed",
        "figures_visually_reviewed",
        "supplements_reviewed",
        "numeric_ast_exported",
        "operational_details_exported",
        "all_gene_or_allele_references_enumerated",
        "biological_curation_completed",
        "whole_record_primary_signoffs",
        "manual_primary_reading_independently_verified_by_code",
    ],
)
def test_assessment_scope_cannot_be_promoted(key):
    notes = assessment()
    notes[key] = True
    with pytest.raises(ValueError, match="promoted"):
        audit.validate_assessment(notes)


@pytest.mark.parametrize(
    "mutation", ["gene", "species", "prodrug", "genome", "causality", "ncbi", "neisseria", "correction"]
)
def test_primary_boundaries_are_retained(mutation):
    notes = assessment()
    h, n = [notes["primary_contexts"][k] for k in ("29352811", "16940068")]
    if mutation == "gene":
        h["gene"] = "another"
    elif mutation == "species":
        h["species"] = "Haemophilus haemolyticus"
    elif mutation == "prodrug":
        h["chemical_qualification"]["same_structure_established"] = True
    elif mutation == "genome":
        h["reference_genome_assigned_to_tested_isolates"] = True
    elif mutation == "causality":
        h["independent_causality_assigned"] = True
    elif mutation == "ncbi":
        notes["access"]["ncbi_requests"] = 1
    elif mutation == "neisseria":
        n["primary_experimental_species"] = "Neisseria meningitidis"
    else:
        n["source_label_silently_corrected"] = True
    with pytest.raises(ValueError):
        audit.validate_assessment(notes)


def test_portable_claim_and_reference_coverage(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    d = result()
    p = audit.read_json(ROOT, d["plan"])
    index = audit.read_json(ROOT, p["inputs"]["index"])
    labels = audit.selected_cohort(ROOT, p, index)
    audit.validate_assessment(assessment())
    assert len(labels) == len(d["terms"]) == 14
    assert len(d["records"]) == 12 and len(d["claims"]) == len(d["claim_dispositions"]) == 25
    update = audit.read_json(ROOT, p["inputs"]["corpus_update"])
    deltas = {r["identifier"]: r for r in update["record_deltas"]}
    expected = copy.deepcopy([c for c in index["claims"] if c["aro_id"] in labels])
    for claim in expected:
        if claim["record_identifier"] in deltas:
            delta = deltas[claim["record_identifier"]]
            assert claim["record_sha256"] == delta["before_sha256"]
            claim["record_sha256"] = delta["after_sha256"]
    assert d["claims"] == expected
    assert len(d["reference_views"]) == 20 and len(d["reference_taxonomy_sources"]) == 8
    qualified = set()
    for term, row in d["terms"].items():
        assert row["record_memberships"] == index["terms"][term]["record_memberships"]
        assert row["source_label_sha256"] == hashlib.sha256(labels[term].encode()).hexdigest()
        for candidate in row["name_matched_candidates"]:
            view = d["reference_views"][candidate["protein_accession"]]
            expected = audit.reference_disposition(
                row["source_species_reference"], view["reference_taxonomy"]["species"]
            )
            assert candidate["disposition"] == expected
            assert candidate["qualified_reference"] is expected.startswith("SAME_SPECIES_")
        qualified.update(row["qualified_reference_accessions"])
    assert len(qualified) == 13
    assert sum(bool(t["qualified_reference_accessions"]) for t in d["terms"].values()) == 8
    assert sum(bool(c["qualified_reference_accessions"]) for c in d["claim_dispositions"]) == 16
    assert all(
        not v["exact_allele_assignment"] and not v["experimental_subject_assignment"]
        for v in d["reference_views"].values()
    )


def test_unreviewed_citation_matches_stay_separate_and_reference_only():
    d = result()
    for term in ("ARO:3009660", "ARO:3009661"):
        assert d["terms"][term]["qualified_reference_accessions"] == ["UniProtKB:A0A0H2WY27"]
    staph = d["reference_views"]["UniProtKB:A0A0H2WY27"]
    assert staph["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
    assert staph["reference_taxonomy"]["taxon_id"] == "NCBITaxon:93062"
    assert len(d["terms"]["ARO:3004832"]["qualified_reference_accessions"]) == 2
    rejected = d["terms"]["ARO:3003937"]
    assert rejected["qualified_reference_accessions"] == [] and rejected["source_species_reference"] is None
    assert len(rejected["name_matched_candidates"]) == 7
    assert all(not c["qualified_reference"] for c in rejected["name_matched_candidates"])


def test_qualifications_do_not_rewrite_or_upgrade_claims():
    d = result()
    assert sum(bool(c["qualifications"]) for c in d["claim_dispositions"]) == 9
    for claim, disposition in zip(d["claims"], d["claim_dispositions"], strict=True):
        assert all(disposition[k] == v for k, v in claim.items())
        assert disposition["source_claim_preserved"] and not disposition["whole_claim_primary_signoff"]
    parent = [
        c
        for c in d["claim_dispositions"]
        if c["aro_id"] == "ARO:3004446" and c["record_identifier"] == "CHEBI:59343"
    ]
    assert (
        len(parent) == 1
        and "PAPER_CAPTION_NAMES_PRODRUG_NOT_VERIFIED_PARENT_STRUCTURE" in parent[0]["qualifications"]
    )
    assert all(
        "AMPICILLIN" in c["qualifications"][0]
        for c in d["claim_dispositions"]
        if c["aro_id"] == "ARO:3004446"
    )
    assert d["limits"]["full_corpus_goal_status"] == "OPEN"


def test_exports_contain_no_operational_or_numerical_ast_fields():
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    forbidden = {
        "sequence",
        "features",
        "variants",
        "alteration",
        "mic_value",
        "primers",
        "coordinates",
        "protocol",
    }
    assert not set(keys(result())) & forbidden
    assert not set(keys(assessment())) & forbidden


def test_offline_replay_has_no_network_or_python_file_writes(monkeypatch):
    if not (ROOT / audit.CACHE / "taxonomy-373153-body.json").exists():
        pytest.skip("native cache unavailable; portable tests still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not set(mode) & set("wax+"), "offline replay attempted write"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(ROOT) == result()
