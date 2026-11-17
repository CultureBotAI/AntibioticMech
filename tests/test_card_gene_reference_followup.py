"""Reviewed reference identity never substitutes for experimental allele evidence."""

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
import audit_card_gene_reference_followup as audit  # noqa: E402


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


@pytest.mark.parametrize(
    "symbol,expected", [("foo", True), ("FOO", True), ("fo", False), ("foo1", False), ("foo ", False)]
)
def test_exact_case_insensitive_native_field_match(symbol, expected):
    assert bool(audit.native_matches({"genes": [{"geneName": {"value": "foo"}}]}, symbol)) is expected


def test_locus_field_is_preserved_without_gene_or_orf_inference():
    entry = {
        "genes": [
            {
                "synonyms": [{"value": "alias"}],
                "orderedLocusNames": [{"value": "locus1"}],
                "orfNames": [{"value": "orf1"}],
            }
        ],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "name1"}}},
    }
    assert audit.native_matches(entry, "LOCUS1") == [
        {"field": "genes/0/orderedLocusNames/0", "value": "locus1"}
    ]
    assert not audit.prior.gene_matches(entry, "locus1")
    assert audit.native_matches(entry, "ALIAS") == [{"field": "genes/0/synonyms/0", "value": "alias"}]
    assert not audit.native_matches(entry, "orf1") and not audit.native_matches(entry, "name1")


def test_species_identity_not_name_or_identifier_alone():
    species = {"taxonId": 1, "scientificName": "Example species", "rank": "species"}
    assert audit.disposition(species, copy.deepcopy(species)) == audit.QUALIFIED
    for field, value in (("taxonId", 2), ("scientificName", "Another name"), ("rank", "strain")):
        assert audit.disposition(species, {**species, field: value}) != audit.QUALIFIED
    assert audit.disposition(species, None) != audit.QUALIFIED


def save(root, path, value):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value))
    return audit.reference.pin(root, target)


def query_fixture(root, mutation=None):
    params = audit.prior.members.prior.mex.parameters(["foo"], "1", True)
    params = {k: v[0] for k, v in params.items()}
    params["fields"] = audit.FIELDS
    url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(params)
    item = {
        "source_name": "Example species",
        "taxon_id": "1",
        "symbols": ["foo"],
        "parameters": params,
        "url": url,
    }
    plan = {
        "cache_directory": "cache",
        "canary": "proteins-1",
        "max_response_bytes": 100000,
        "terms": {"term": {"tokens": {"species": "Example species", "gene": "foo"}}},
        "source_names": {"Example species": {"selected_taxon_id": "1"}},
        "requests": {"proteins-1": item},
    }
    if mutation == "symbols":
        item["symbols"] = ["bar"]
    elif mutation == "fields":
        params["fields"] += ",cc_subunit"
    elif mutation == "missing_query":
        plan["requests"] = {}
    elif mutation == "missing_canary":
        plan["canary"] = "proteins-2"
    plan_pin = save(root, audit.PLAN, plan)
    entry = {
        "primaryAccession": "P00001",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "organism": {"taxonId": 10},
        "genes": [{"geneName": {"value": "foo"}}],
    }
    if mutation == "unreviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif mutation == "comments":
        entry["comments"] = []
    body = {"results": [entry]}
    if mutation == "duplicate":
        body["results"].append(copy.deepcopy(entry))
    body_pin = save(root, "cache/proteins-1-body.json", body)
    receipt = {
        "url": url,
        "status": 200,
        "retries": 0,
        "redirects_followed": 0,
        "headers": {"x-uniprot-release": "2026_03", "x-total-results": str(len(body["results"]))},
        "body": body_pin,
        "bytes": (root / body_pin["path"]).stat().st_size,
    }
    if mutation == "release":
        receipt["headers"]["x-uniprot-release"] = "2026_04"
    elif mutation == "pagination":
        receipt["headers"]["link"] = "next"
    elif mutation == "location":
        receipt["headers"]["location"] = "https://example.org"
    elif mutation == "count":
        receipt["headers"]["x-total-results"] = "2"
    elif mutation == "retry":
        receipt["retries"] = 1
    elif mutation == "redirect":
        receipt["redirects_followed"] = 1
    elif mutation == "status":
        receipt["status"] = 503
    elif mutation == "bytes":
        receipt["bytes"] += 1
    elif mutation == "wrong_host":
        receipt["url"] = url.replace("rest.uniprot.org", "example.org")
    receipt_pin = save(root, "cache/proteins-1-receipt.json", receipt)
    attempt = {"key": "proteins-1", "plan": plan_pin, "url": url, "retries": 0, "redirects_followed": 0}
    if mutation == "attempt":
        attempt["url"] = "https://example.org"
    save(root, "cache/proteins-1-attempt.json", attempt)
    if mutation == "extra_attempt":
        save(root, "cache/proteins-2-attempt.json", attempt)
    elif mutation == "error":
        save(root, "cache/proteins-1-error.json", {"error": "failure"})
    inspection = {
        "plan": plan_pin,
        "approved_for_remaining_metadata_queries": True,
        "experimental_subjects_or_resistant_alleles_assigned": False,
        "source": receipt_pin,
        "inspected_count": 1,
    }
    if mutation == "unapproved":
        inspection["approved_for_remaining_metadata_queries"] = False
    elif mutation == "experimental":
        inspection["experimental_subjects_or_resistant_alleles_assigned"] = True
    save(root, audit.CANARY, inspection)
    return plan


def test_native_query_replays_with_order_independent_parameters(tmp_path):
    plan = query_fixture(tmp_path)
    # A serialized plan sorts parameter keys, unlike the original request URL.
    plan["requests"]["proteins-1"]["parameters"] = dict(
        sorted(plan["requests"]["proteins-1"]["parameters"].items())
    )
    entries, pools, sources = audit.query_results(tmp_path, plan)
    assert list(entries) == ["P00001"] and pools == {"Example species": ["P00001"]}
    assert sources["proteins-1"]["native_source"]["complete_for_exact_query"]


@pytest.mark.parametrize(
    "mutation",
    [
        "symbols",
        "fields",
        "missing_query",
        "missing_canary",
        "unreviewed",
        "comments",
        "duplicate",
        "release",
        "pagination",
        "location",
        "count",
        "retry",
        "redirect",
        "status",
        "bytes",
        "wrong_host",
        "attempt",
        "extra_attempt",
        "error",
        "unapproved",
        "experimental",
    ],
)
def test_query_rejects_unaccounted_or_changed_evidence(tmp_path, mutation):
    with pytest.raises(ValueError):
        audit.query_results(tmp_path, query_fixture(tmp_path, mutation))


def taxonomy_fixture(root, mutation=None):
    node = {
        "taxonId": 1,
        "scientificName": "Example species",
        "rank": "species",
        "active": True,
        "parent": {"taxonId": 2, "scientificName": "Example"},
        "lineage": [{"taxonId": 2, "scientificName": "Example", "rank": "genus"}],
    }
    if mutation == "inactive":
        node["active"] = False
    nodes = [node, node] if mutation == "duplicate" else [node]
    body = json.dumps({"results": nodes})
    url = "https://rest.uniprot.org/taxonomy/search?query=example"
    if mutation == "endpoint":
        url = url.replace("taxonomy", "uniprotkb")
    elif mutation == "wrong_get_id":
        url = "https://rest.uniprot.org/taxonomy/2.json"
    receipt = {
        "url": url,
        "status": 200,
        "body": body,
        "sha256": hashlib.sha256(body.encode()).hexdigest(),
        "headers": {"x-uniprot-release": "2026_03", "x-total-results": str(len(nodes))},
        "retrieved_at": "2026-10-15T00:00:00Z",
        "bytes": len(body.encode()),
    }
    if mutation == "location":
        receipt["headers"]["location"] = "https://example.org"
    elif mutation == "retry":
        receipt["retries"] = 1
    source = {"url": url, "wrapper": save(root, "cache/taxonomy.json", receipt)}
    return {"taxon_id": "999" if mutation == "identity" else "1", "source": source}


def test_cached_search_can_supply_a_native_taxonomy_node(tmp_path):
    node, source = audit.cached_node(tmp_path, taxonomy_fixture(tmp_path))
    assert node["taxonId"] == 1 and source["release"] == "2026_03"


@pytest.mark.parametrize(
    "mutation", ["inactive", "duplicate", "endpoint", "identity", "wrong_get_id", "location", "retry"]
)
def test_cached_taxonomy_fails_closed(tmp_path, mutation):
    with pytest.raises(ValueError):
        audit.cached_node(tmp_path, taxonomy_fixture(tmp_path, mutation))


def test_portable_output_accounts_for_entire_unresolved_cohort(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    d = result()
    prior = audit.read_json(ROOT, d["prior"])
    assert set(d["terms"]) == {
        t for t, r in prior["terms"].items() if not r["qualified_reference_accessions"]
    }
    assert len(d["terms"]) == 161 and len(d["claims"]) == 201 and len(d["records"]) == 79
    selected = set(d["terms"])
    assert d["claims"] == [c for c in prior["claims"] if c["aro_id"] in selected]
    for term, row in d["terms"].items():
        assert row["record_memberships"] == sorted(
            {c["record_identifier"] for c in d["claims"] if c["aro_id"] == term}
        )
        assert row["whole_record_primary_review"] == "OPEN" and not row["biological_absence_inferred"]


def test_qualified_references_have_exact_fields_and_verified_species():
    d = result()
    for row in d["terms"].values():
        source = d["source_names"][row["tokens"]["species"]]["selected"]
        for candidate in row["reference_candidates"]:
            view = d["reference_views"][candidate["protein_accession"]]
            assert candidate["literal_native_fields"]
            assert all(
                m["value"].casefold() == row["tokens"]["gene"].casefold()
                for m in candidate["literal_native_fields"]
            )
            assert candidate["disposition"] == audit.disposition(
                source["identity"], view["reference_taxonomy"]["species"]
            )
            assert candidate["qualified_reference"] is (candidate["disposition"] == audit.QUALIFIED)
            assert (
                not candidate["exact_allele_assignment"] and not candidate["experimental_subject_assignment"]
            )
            assert not candidate["citation_overlap_is_primary_validation"]
            assert set(candidate["own_definition_citation_overlap"]) <= set(row["definition_citations"])
        assert row["qualified_reference_accessions"] == [
            c["protein_accession"] for c in row["reference_candidates"] if c["qualified_reference"]
        ]


def test_unresolved_names_are_not_silently_corrected_or_queried():
    d = result()
    unresolved = {n for n, r in d["source_names"].items() if not r["selected"]}
    assert len(unresolved) == 18
    assert {"Ethambutol resistant", "Saccharomyces cerevasiae", "Trychophyton rubrum"} <= unresolved
    assert not unresolved & {q["source_name"] for q in d["queries"].values()}
    for row in d["terms"].values():
        if row["tokens"]["species"] in unresolved:
            assert row["status"] == "SOURCE_NAME_UNRESOLVED_NOT_QUERIED"
            assert not row["reference_candidates"]


def test_reference_metadata_has_no_experimental_or_operational_assignments():
    d = result()
    for view in d["reference_views"].values():
        assert view["entry_type"] == "UniProtKB reviewed (Swiss-Prot)"
        assert not view["experimental_subject_assignment"] and not view["exact_allele_assignment"]
        assert view["experimental_genome_assignment"] is None and not view["new_primary_results_review"]
    assert d["limits"]["full_corpus_goal_status"] == "OPEN"
    assert d["limits"]["ncbi_requests"] == 0 and d["limits"]["issue_1040"] == "DEFERRED"

    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(d)) & {"sequence", "features", "comments", "variants", "alteration", "mic", "primers"}


def test_bounded_counts_locus_scope_and_multiple_references():
    d = result()
    assert len(d["reference_views"]) == 167 and len(d["taxonomy_sources"]) == 59
    qualified = [
        c for r in d["terms"].values() for c in r["reference_candidates"] if c["qualified_reference"]
    ]
    assert len(qualified) == d["summary"]["qualified_reference_links"] == 185
    assert sum(bool(r["qualified_reference_accessions"]) for r in d["terms"].values()) == 71
    assert sum(len(r["qualified_reference_accessions"]) > 1 for r in d["terms"].values()) == 31
    assert sum(not q["accessions"] for q in d["queries"].values()) == 19
    assert not any(c["own_definition_citation_overlap"] for c in qualified)
    loci = [
        (t, c)
        for t, r in d["terms"].items()
        for c in r["reference_candidates"]
        if c["match_kind"] == "ORDERED_LOCUS_REFERENCE_NOT_GENE_RENAMING"
    ]
    assert {t for t, _ in loci} == {"ARO:3007674", "ARO:3007852"}
    assert all(c["protein_accession"] == "UniProtKB:I6Y8F7" for _, c in loci)


def test_cli_creates_parent_and_preserves_existing_output(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda _: {"summary": {}})
    argv = ["audit", "--root", str(tmp_path), "--output", "nested/output.json"]
    monkeypatch.setattr(sys, "argv", argv)
    audit.main()
    path = tmp_path / "nested/output.json"
    before = path.stat().st_mtime_ns
    audit.main()
    assert path.stat().st_mtime_ns == before
    path.write_bytes(b"older artifact\n")
    for args in (argv, argv + ["--check"]):
        monkeypatch.setattr(sys, "argv", args)
        with pytest.raises(ValueError, match="preserve prior output"):
            audit.main()
        assert path.read_bytes() == b"older artifact\n"


def test_offline_replay_is_read_only(monkeypatch, pre_cdsa_qualification_root):
    d = result()
    required = [q["native_source"]["receipt"]["path"] for q in d["queries"].values()]
    if not all((ROOT / p).exists() for p in required):
        pytest.skip("ignored native receipts unavailable; portable output tests still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not any(c in mode for c in "wax+"), "audit attempted file mutation"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == d
