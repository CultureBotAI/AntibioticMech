"""Source-name resolution preserves rank, ambiguity and non-taxonomic strings."""

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
import audit_card_unresolved_names as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def node(tid=1, name="Example species"):
    parent = {"taxonId": 100, "rank": "genus", "scientificName": "Example"}
    return {
        "taxonId": tid,
        "scientificName": name,
        "rank": "species",
        "active": True,
        "parent": parent,
        "lineage": [parent],
    }


def result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


@pytest.mark.parametrize(
    "name,accepted",
    [
        ("Example species", True),
        ("EXAMPLE SPECIES", True),
        ("Example specie", False),
        ("Example species ", False),
    ],
)
def test_exact_full_name_only(name, accepted):
    resolved = audit.resolve({"results": [node()]}, name)
    assert (resolved["selected_reference_species"] is not None) is accepted


def test_other_names_are_not_silently_treated_as_synonyms():
    taxon = {**node(), "otherNames": ["Historical name"], "synonyms": ["Explicit alias"]}
    resolved = audit.resolve({"results": [taxon]}, "Historical name")
    assert resolved["selected_reference_species"] is None
    assert resolved["candidates"][0]["other_name_fields"] == [
        {"field": "otherNames/0", "value": "Historical name"}
    ]
    resolved = audit.resolve({"results": [taxon]}, "Explicit alias")
    assert resolved["selected_reference_species"]["exact_name_fields"] == [
        {"field": "synonyms/0", "value": "Explicit alias"}
    ]


@pytest.mark.parametrize("rank", ["strain", "species group", "genus", "subspecies", "no rank"])
def test_matching_name_at_other_rank_does_not_resolve_species(rank):
    resolved = audit.resolve({"results": [{**node(), "rank": rank}]}, "Example species")
    assert resolved["selected_reference_species"] is None
    assert resolved["candidates"][0]["exact_name_fields"]


def test_ambiguous_active_names_are_all_retained_without_a_representative():
    resolved = audit.resolve({"results": [node(), node(2)]}, "Example species")
    assert resolved["status"] == "AMBIGUOUS_EXACT_ACTIVE_SPECIES_NAMES"
    assert resolved["selected_reference_species"] is None and len(resolved["candidates"]) == 2


def test_inactive_candidate_does_not_mask_active_exact_match():
    resolved = audit.resolve({"results": [{**node(), "active": False}, node(2)]}, "Example species")
    assert resolved["selected_reference_species"]["identity"]["taxonId"] == 2
    assert len(resolved["candidates"]) == 2


@pytest.mark.parametrize("mutation", ["duplicate", "taxid", "activity", "synonyms", "otherNames", "lineage"])
def test_invalid_native_taxonomy_fails_closed(mutation):
    entry = node()
    payload = {"results": [entry]}
    if mutation == "duplicate":
        payload["results"].append(copy.deepcopy(entry))
    elif mutation == "taxid":
        entry["taxonId"] = True
    elif mutation == "activity":
        entry["active"] = "true"
    elif mutation in ("synonyms", "otherNames"):
        entry[mutation] = "not a list"
    else:
        entry["lineage"] = []
        entry["parent"] = {"taxonId": 1}
        entry["lineage"].append(copy.deepcopy(entry))
    with pytest.raises(ValueError):
        audit.resolve(payload, "Example species")


def native_fixture(root, mutation=None, unranked=False):
    query = '"Example species"' + ("" if unranked else " AND rank:species")
    url = "https://rest.uniprot.org/taxonomy/search?" + urlencode(
        {"query": query, "format": "json", "size": "500"}
    )
    if mutation == "query":
        url = url.replace("Example", "Another")
    elif mutation == "host":
        url = url.replace("rest.uniprot.org", "example.org")
    elif mutation == "endpoint":
        url = url.replace("taxonomy", "uniprotkb")
    body = json.dumps({"results": [node()]})
    receipt = {
        "url": url,
        "status": 200,
        "body": body,
        "sha256": hashlib.sha256(body.encode()).hexdigest(),
        "bytes": len(body.encode()),
        "retrieved_at": "2026-10-15T00:00:00Z",
        "headers": {"x-uniprot-release": "2026_03", "x-total-results": "1"},
    }
    if mutation == "checksum":
        receipt["sha256"] = "0" * 64
    elif mutation == "status":
        receipt["status"] = 503
    elif mutation == "release":
        receipt["headers"]["x-uniprot-release"] = "2026_04"
    elif mutation == "pagination":
        receipt["headers"]["link"] = "next"
    elif mutation == "count":
        receipt["headers"]["x-total-results"] = "2"
    elif mutation == "location":
        receipt["headers"]["location"] = "https://example.org"
    elif mutation == "retry":
        receipt["retries"] = 1
    elif mutation == "legacy_retry":
        receipt["retry_performed"] = True
    elif mutation == "redirect":
        receipt["redirects_followed"] = True
    path = root / "receipt.json"
    path.write_text(json.dumps(receipt))
    return {"url": url, "wrapper": audit.reference.pin(root, path)}


def test_native_query_is_complete_and_source_bound(tmp_path):
    resolved, provenance = audit.native_name(tmp_path, "Example species", native_fixture(tmp_path))
    assert resolved["status"] == "EXACT_ACTIVE_SPECIES_NAME"
    assert provenance["release"] == "2026_03"


def test_unranked_historical_query_requires_explicit_reuse(tmp_path):
    source = native_fixture(tmp_path, unranked=True)
    with pytest.raises(ValueError):
        audit.native_name(tmp_path, "Example species", source)
    resolved, _ = audit.native_name(tmp_path, "Example species", source, allow_unranked=True)
    assert resolved["selected_reference_species"]["identity"]["rank"] == "species"


@pytest.mark.parametrize(
    "mutation",
    [
        "query",
        "host",
        "endpoint",
        "checksum",
        "status",
        "release",
        "pagination",
        "count",
        "location",
        "retry",
        "legacy_retry",
        "redirect",
    ],
)
def test_native_query_rejects_changed_or_failed_evidence(tmp_path, mutation):
    with pytest.raises(ValueError):
        audit.native_name(tmp_path, "Example species", native_fixture(tmp_path, mutation))


def test_portable_cohort_preserves_every_unresolved_term_and_claim(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    d = result()
    prior = audit.read_json(ROOT, d["prior"])
    selected = {t for t, r in prior["terms"].items() if r["status"] == "SOURCE_NAME_UNRESOLVED_NOT_QUERIED"}
    assert set(d["terms"]) == selected and len(selected) == 43
    assert d["claims"] == [c for c in prior["claims"] if c["aro_id"] in selected]
    assert len(d["claims"]) == 50 and len(d["records"]) == 31 and len(d["names"]) == 18
    for term, row in d["terms"].items():
        assert row["record_memberships"] == sorted(
            {c["record_identifier"] for c in d["claims"] if c["aro_id"] == term}
        )
        assert row["source_label"] == prior["terms"][term]["source_label"]
        assert not row["experimental_subject_assignment"] and not row["exact_allele_assignment"]
        assert row["whole_record_primary_review"] == "OPEN"


def test_canary_search_noise_is_not_an_identity_join():
    row = result()["names"]["Streptococcus mitis"]
    assert row["result_count"] == 4 and row["exact_species_match_count"] == 1
    assert row["selected_reference_species"]["identity"] == {
        "taxonId": 28037,
        "rank": "species",
        "scientificName": "Streptococcus mitis",
    }
    assert any(c["identity"]["rank"] == "species group" for c in row["candidates"])
    assert any("phage" in c["identity"]["scientificName"] for c in row["candidates"])


def test_non_individual_strings_remain_unqueried_context():
    d = result()
    for name, status in audit.CONTEXTS.items():
        assert name not in d["native_sources"]
        row = d["names"][name]
        assert row["status"] == status and row["result_count"] is None
        assert row["selected_reference_species"] is None and not row["biological_absence_inferred"]


def test_cached_other_name_matches_do_not_gain_identity_by_repetition():
    d = result()
    for name in [
        "Nakaseomyces glabratus",
        "Mycosphaerella fijiensis",
        "Tapesia acuformis",
        "Tapesia yallundae",
        "Phakospora pachyrhizi",
    ]:
        row = d["names"][name]
        assert row["selected_reference_species"] is None
        assert any(c["other_name_fields"] for c in row["candidates"])
        assert not any(c["accepted_species_name"] for c in row["candidates"])


def test_exact_synonym_and_species_neighbours_are_not_silently_rewritten():
    d = result()
    dermatophyte = d["names"]["Microsporum canis"]["selected_reference_species"]
    assert dermatophyte["identity"] == {
        "taxonId": 63405,
        "scientificName": "Arthroderma otae",
        "rank": "species",
    }
    assert dermatophyte["exact_name_fields"] == [{"field": "synonyms/0", "value": "Microsporum canis"}]
    mucor = d["names"]["Mucor circinelloides"]
    assert mucor["result_count"] == 4 and mucor["selected_reference_species"]["identity"]["taxonId"] == 36080
    neighbour = next(c for c in mucor["candidates"] if c["identity"]["taxonId"] == 29924)
    assert neighbour["identity"]["rank"] == "species" and not neighbour["accepted_species_name"]


def test_canary_inspection_is_bound_to_the_actual_selected_identity(tmp_path):
    source = native_fixture(tmp_path)
    key = "name-example-species"
    plan = {
        "cache_directory": "cache",
        "max_response_bytes": 100000,
        "canary": key,
        "requests": {
            key: {
                "name": "Example species",
                "url": source["url"],
                "parameters": {
                    "query": '"Example species" AND rank:species',
                    "format": "json",
                    "size": "500",
                },
            }
        },
    }
    (tmp_path / audit.PLAN).parent.mkdir(parents=True)
    (tmp_path / audit.PLAN).write_text(json.dumps(plan))
    plan_pin = audit.reference.pin(tmp_path, tmp_path / audit.PLAN)
    cache = tmp_path / "cache"
    cache.mkdir()
    receipt_path = cache / (key + "-receipt.json")
    receipt_path.write_bytes((tmp_path / "receipt.json").read_bytes())
    (cache / (key + "-attempt.json")).write_text(
        json.dumps(
            {"key": key, "plan": plan_pin, "url": source["url"], "retries": 0, "redirects_followed": 0}
        )
    )
    original = {
        "plan": plan_pin,
        "approved_for_remaining_queries": True,
        "experimental_identity_assignments": False,
        "result_count": 1,
        "exact_species_match_count": 1,
        "selected_reference_taxon_id": "1",
        "selected_reference_scientific_name": "Example species",
        "receipt": audit.reference.pin(tmp_path, receipt_path),
    }
    (tmp_path / audit.CANARY).write_text(json.dumps(original))
    assert audit.requests(tmp_path, plan)[0]["Example species"]["status"] == "EXACT_ACTIVE_SPECIES_NAME"
    for key, value in (
        ("selected_reference_taxon_id", "999"),
        ("selected_reference_scientific_name", "Another name"),
        ("exact_species_match_count", 0),
    ):
        (tmp_path / audit.CANARY).write_text(json.dumps({**original, key: value}))
        with pytest.raises(ValueError, match="canary native response changed"):
            audit.requests(tmp_path, plan)


def test_cli_preserves_existing_output_and_creates_parent(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda _: {"summary": {}})
    argv = ["audit", "--root", str(tmp_path), "--output", "nested/output.json"]
    monkeypatch.setattr(sys, "argv", argv)
    audit.main()
    path = tmp_path / "nested/output.json"
    before = path.stat().st_mtime_ns
    audit.main()
    assert path.stat().st_mtime_ns == before
    path.write_bytes(b"prior artifact\n")
    for args in (argv, argv + ["--check"]):
        monkeypatch.setattr(sys, "argv", args)
        with pytest.raises(ValueError, match="preserve prior output"):
            audit.main()
        assert path.read_bytes() == b"prior artifact\n"


def test_offline_replay_is_read_only(monkeypatch, pre_cdsa_qualification_root):
    d = result()
    required = [s.get("wrapper", s.get("receipt"))["path"] for s in d["native_sources"].values()]
    if not all((ROOT / p).exists() for p in required):
        pytest.skip("ignored native sources unavailable; portable tests still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not any(c in mode for c in "wax+"), "audit attempted file mutation"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == d
