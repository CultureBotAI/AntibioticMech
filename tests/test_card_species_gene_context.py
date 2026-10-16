"""Literal genes, citation ownership and verified species jointly constrain references."""

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
import audit_card_species_gene_context as audit  # noqa: E402


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
    "label",
    [
        "acrR",
        "AcrAB-TolC",
        "Escherichia coli 16S rRNA",
        "Escherichia coli acrR-like",
        "Escherichia coli acrR extra",
    ],
)
def test_label_grammar_does_not_guess_unhandled_entity_shapes(label):
    assert audit.parse_label(label) is None


def test_label_grammar_is_only_tokens_not_an_asserted_species_identity():
    assert audit.parse_label("Ethambutol resistant iniC") == {
        "species": "Ethambutol resistant",
        "gene": "iniC",
    }
    row = result()["terms"]["ARO:3003450"]
    assert row["source_species_binding"] is None
    assert not row["qualified_reference_accessions"]
    assert row["citation_scope"] == "NO_OWN_DEFINITION_CITATIONS_DISCOVERY_REMAINS_OPEN"


@pytest.mark.parametrize(
    "symbol,match",
    [("acrR", True), ("AcrR", True), ("acr", False), ("acrR1", False), ("acr-R", False), ("acrR ", False)],
)
def test_whole_native_gene_symbols_only(symbol, match):
    entry = {"genes": [{"geneName": {"value": "acrR"}}]}
    assert bool(audit.gene_matches(entry, symbol)) is match


def test_native_synonyms_are_allowed_but_locus_and_protein_names_are_not():
    entry = {
        "genes": [
            {
                "synonyms": [{"value": "yybT"}],
                "orderedLocusNames": [{"value": "foo"}],
                "orfNames": [{"value": "bar"}],
            }
        ],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "baz"}}},
    }
    assert audit.gene_matches(entry, "YybT") == [{"field": "genes/0/synonyms/0", "value": "yybT"}]
    assert all(not audit.gene_matches(entry, s) for s in ("foo", "bar", "baz"))


def test_species_binding_uses_verified_species_names_and_explicit_synonyms_only():
    species = {
        "active": True,
        "rank": "species",
        "scientificName": "Klebsiella aerogenes",
        "synonyms": ["Enterobacter aerogenes"],
        "otherNames": ["Other organism"],
        "strains": [{"name": "Unrelated label"}],
    }
    assert audit.species_name_binding("Enterobacter aerogenes", species) == [
        {"field": "synonyms/0", "value": "Enterobacter aerogenes"}
    ]
    assert audit.species_name_binding("Klebsiella aerogenes", species)
    for name in ("Other organism", "Unrelated label", "Enterobacter cloacae", "Klebsiella aerogenes "):
        assert audit.species_name_binding(name, species) == []
    for key, value in (("rank", "strain"), ("active", False)):
        with pytest.raises(ValueError):
            audit.species_name_binding("Klebsiella aerogenes", {**species, key: value})


def test_lineage_species_must_agree_as_an_identity_not_just_a_name():
    species = {"taxonId": 573, "rank": "species", "scientificName": "Klebsiella pneumoniae"}
    assert audit.disposition(species, copy.deepcopy(species)) == audit.QUALIFIED
    for key, value in (("taxonId", 548), ("rank", "strain"), ("scientificName", "Another name")):
        assert audit.disposition(species, {**species, key: value}) == audit.MISMATCH
    assert audit.disposition(species, None) == "REFERENCE_WITHOUT_SPECIES_RANK_WITHHELD"


def test_portable_artifact_preserves_complete_selection_and_claims(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    d = result()
    plan = audit.read_json(ROOT, d["plan"])
    index = audit.read_json(ROOT, d["inputs"]["index"])
    update = audit.read_json(ROOT, d["inputs"]["corpus_update"])
    labels, excluded = audit.cohort(ROOT, index)
    assert set(labels) == set(d["terms"]) and len(labels) == 178
    assert excluded == d["grammar_excluded_unlinked_terms"] and len(excluded) == 542
    assert len(d["claims"]) == 225 and len(d["records"]) == 83
    expected = copy.deepcopy([c for c in index["claims"] if c["aro_id"] in labels])
    deltas = {r["identifier"]: r for r in update["record_deltas"]}
    for c in expected:
        if c["record_identifier"] in deltas:
            delta = deltas[c["record_identifier"]]
            assert c["record_sha256"] == delta["before_sha256"]
            c["record_sha256"] = delta["after_sha256"]
    assert expected == d["claims"]
    records = {r["identifier"]: r for r in d["records"]}
    for c in expected:
        assert c["record_sha256"] == records[c["record_identifier"]]["record_sha256"]
        assert c["standard_inchi_key"] == records[c["record_identifier"]]["standard_inchi_key"]
    assert plan["constraints"]["full_corpus_goal_status"] == "OPEN"


def test_all_qualified_links_have_native_symbol_own_citation_and_matching_species():
    d = result()
    qualified = []
    for term, row in d["terms"].items():
        assert row["whole_record_primary_review"] == "OPEN" and not row["biological_absence_inferred"]
        for c in row["literal_gene_candidates"]:
            view = d["reference_views"][c["protein_accession"]]
            assert c["own_citation_ids"] and set(c["own_citation_ids"]) <= set(row["definition_citations"])
            assert all(
                c["protein_accession"] in d["citation_queries"][p[5:]]["accessions"]
                for p in c["own_citation_ids"]
            )
            assert c["literal_gene_fields"]
            assert all(
                f["value"].casefold() == row["parsed_tokens_not_identity_by_themselves"]["gene"].casefold()
                for f in c["literal_gene_fields"]
            )
            status = audit.disposition(
                row["source_species_binding"]["identity"], view["reference_taxonomy"]["species"]
            )
            assert status == c["disposition"]
            assert c["qualified_reference"] is (status == audit.QUALIFIED)
            assert not c["exact_allele_assignment"] and not c["experimental_subject_assignment"]
            if c["qualified_reference"]:
                qualified.append((term, c["protein_accession"]))
        assert row["qualified_reference_accessions"] == [
            c["protein_accession"] for c in row["literal_gene_candidates"] if c["qualified_reference"]
        ]
    assert len(qualified) == 38 and len({t for t, a in qualified}) == 17


def test_four_cross_species_hits_are_preserved_but_withheld():
    rejected = {
        (t, c["protein_accession"])
        for t, row in result()["terms"].items()
        for c in row["literal_gene_candidates"]
        if c["disposition"] == audit.MISMATCH
    }
    assert rejected == {
        ("ARO:3003326", "UniProtKB:Q50395"),
        ("ARO:3003788", "UniProtKB:P63757"),
        ("ARO:3003797", "UniProtKB:P37484"),
        ("ARO:3004042", "UniProtKB:Q9AEG2"),
    }


def test_acr_synonym_and_reference_strain_are_not_experimental_assignments():
    d = result()
    row = d["terms"]["ARO:3003374"]
    assert row["source_species_binding"]["name_binding"] == [
        {"field": "synonyms/0", "value": "Enterobacter aerogenes"}
    ]
    assert row["qualified_reference_accessions"] == ["UniProtKB:Q9AEG3"]
    assert d["terms"]["ARO:3004042"]["qualified_reference_accessions"] == ["UniProtKB:A6XFC0"]
    assert d["terms"]["ARO:3003373"]["qualified_reference_accessions"] == ["UniProtKB:A0A0H3GKK9"]
    view = d["reference_views"]["UniProtKB:A0A0H3GKK9"]
    assert view["reference_taxonomy"]["taxon_id"] == "NCBITaxon:1125630"
    assert view["reference_taxonomy"]["species"]["taxonId"] == 573
    assert not view["experimental_subject_assignment"] and not view["exact_allele_assignment"]


def test_no_definition_citations_is_not_a_completed_zero_hit_search():
    d = result()
    absent = [row for row in d["terms"].values() if not row["definition_citations"]]
    assert len(absent) == 102
    assert all(not row["all_own_citation_queries_complete"] for row in absent)
    assert all(row["status"] == "NO_OWN_DEFINITION_CITATIONS_DISCOVERY_REMAINS_OPEN" for row in absent)
    assert all(
        row["all_own_citation_queries_complete"] for row in d["terms"].values() if row["definition_citations"]
    )
    assert len(d["citation_queries"]) == 113
    assert sum(q["query"]["result_count"] == 0 for q in d["citation_queries"].values()) == 86


def test_fragment_references_remain_multiple_not_one_exact_allele():
    d = result()
    selected = d["terms"]["ARO:3003326"]["qualified_reference_accessions"]
    assert len(selected) == 11
    assert sum(d["reference_views"][a]["native_protein_flag"] == "Fragment" for a in selected) == 10
    assert all(not d["reference_views"][a]["exact_allele_assignment"] for a in selected)
    assert all(not d["reference_views"][a]["unflagged_means_complete"] for a in selected)


def test_export_does_not_include_operational_or_numeric_ast_fields():
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


def taxonomy_fixture(root, mutation=None):
    plan_path = root / audit.PLAN
    plan_path.parent.mkdir(parents=True)
    plan = {
        "new_taxonomy_request": {
            "url": "https://rest.uniprot.org/taxonomy/1125630.json",
            "max_response_bytes": 2000000,
            "release": "2026_03",
            "retries": 0,
            "redirects_followed": 0,
            "cache_directory": "cache",
        }
    }

    def save(path, value):
        path.write_text(json.dumps(value))
        return audit.reference.pin(root, path)

    plan_pin = save(plan_path, plan)
    directory = root / "cache"
    directory.mkdir()
    url = plan["new_taxonomy_request"]["url"]
    attempt = {"plan": plan_pin, "url": url, "retries": 0, "redirects_followed": 0}
    save(directory / "taxonomy-1125630-attempt.json", attempt)
    parent = {"taxonId": 573, "scientificName": "Klebsiella pneumoniae", "rank": "species"}
    node = {
        "taxonId": 1125630,
        "scientificName": "Reference strain",
        "rank": "strain",
        "active": True,
        "lineage": [parent],
        "parent": parent,
    }
    if mutation == "taxon":
        node["taxonId"] = 99
    body = json.dumps(node)
    receipt = {
        "url": url,
        "status": 200,
        "headers": {"x-uniprot-release": "2026_03"},
        "body": body,
        "bytes": len(body.encode()),
        "sha256": hashlib.sha256(body.encode()).hexdigest(),
        "retries": 0,
        "redirects_followed": 0,
        "retrieved_at": "2026-10-15T00:00:00Z",
    }
    if mutation == "release":
        receipt["headers"]["x-uniprot-release"] = "2026_04"
    elif mutation == "location":
        receipt["headers"]["location"] = "https://example.org"
    elif mutation == "retry":
        receipt["retries"] = 1
    elif mutation == "status":
        receipt["status"] = 503
    elif mutation == "bytes":
        receipt["bytes"] += 1
    elif mutation == "extra_attempt":
        save(directory / "extra-attempt.json", attempt)
    elif mutation == "error":
        save(directory / "prior-error.json", {"error": "failure"})
    source = {"body": None, "receipt": save(directory / "taxonomy-1125630-receipt.json", receipt)}
    inspection = {
        "plan": plan_pin,
        "source": source,
        "retries": 0,
        "redirects_followed": 0,
        "accepted_for_reference_taxonomy": True,
        "accepted_for_experimental_subject_assignment": False,
        "accepted_for_exact_resistant_allele_assignment": False,
        "scientific_name": "Reference strain",
        "rank": "strain",
        "species_ancestor_taxon_id": "573",
    }
    if mutation == "experimental":
        inspection["accepted_for_experimental_subject_assignment"] = True
    save(root / audit.INSPECTION, inspection)
    return plan


def test_new_taxonomy_request_replays_immutable_metadata(tmp_path):
    source, provenance = audit.new_taxonomy_source(tmp_path, taxonomy_fixture(tmp_path))
    assert source["body"] is None and "attempt" in provenance


@pytest.mark.parametrize(
    "mutation",
    ["taxon", "release", "location", "retry", "status", "bytes", "extra_attempt", "error", "experimental"],
)
def test_new_taxonomy_request_rejects_drift(tmp_path, mutation):
    with pytest.raises(ValueError):
        audit.new_taxonomy_source(tmp_path, taxonomy_fixture(tmp_path, mutation))


def test_cli_creates_parent_but_never_overwrites_existing_output(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda _: {"summary": {}})
    argv = ["audit", "--root", str(tmp_path), "--output", "nested/output.json"]
    monkeypatch.setattr(sys, "argv", argv)
    audit.main()
    target = tmp_path / "nested/output.json"
    before = target.stat().st_mtime_ns
    audit.main()
    assert target.stat().st_mtime_ns == before
    target.write_bytes(b"prior artifact\n")
    for args in (argv, argv + ["--check"]):
        monkeypatch.setattr(sys, "argv", args)
        with pytest.raises(ValueError, match="preserve prior output"):
            audit.main()
        assert target.read_bytes() == b"prior artifact\n"


def test_cli_check_never_creates_missing_directories(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda _: {"summary": {}})
    monkeypatch.setattr(
        sys, "argv", ["audit", "--root", str(tmp_path), "--output", "missing/a.json", "--check"]
    )
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not (tmp_path / "missing").exists()


def test_offline_replay_has_no_network_or_python_file_writes(monkeypatch, pre_cdsa_qualification_root):
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    if not (ROOT / plan["new_taxonomy_request"]["cache_directory"]).exists():
        pytest.skip("native caches unavailable; portable artifact checks still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not set(mode) & set("wax+"), "audit attempted write"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == result()
