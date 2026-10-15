"""Exact gene aliases and native taxonomic ranks remain reference-only."""

import copy
import json
import socket
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_folp_references as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("network forbidden in reference tests")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)


def node(taxid, name, rank):
    return {"taxonId": taxid, "scientificName": name, "rank": rank}


def taxon(taxid=83333, name="Escherichia coli (strain K12)", rank="strain", ancestors=None):
    ancestors = ancestors or [node(2, "Bacteria", "domain"), node(562, "Escherichia coli", "species")]
    return {**node(taxid, name, rank), "active": True, "lineage": ancestors, "parent": ancestors[-1]}


def named_source():
    t = taxon(562, "Escherichia coli", "species", [node(2, "Bacteria", "domain")])
    return audit.resolve_name({"results": [t]}, "Escherichia coli")["selected_taxon"]


@pytest.fixture
def entry():
    return {
        "primaryAccession": "P0AC13",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 147, "sequenceVersion": 1},
        "organism": {"scientificName": "Escherichia coli (strain K12)", "taxonId": 83333},
        "genes": [
            {
                "geneName": {"value": "folP"},
                "synonyms": [{"value": "dhpS"}],
                "orderedLocusNames": [{"value": "b3177"}],
                "orfNames": [],
            }
        ],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Dihydropteroate synthase"}}},
        "references": [
            {
                "citation": {
                    "publicationDate": "2000",
                    "citationCrossReferences": [{"database": "PubMed", "id": "12345"}],
                },
                "referencePositions": ["not exported"],
            }
        ],
    }


def test_exact_name_preserves_below_species_rank():
    ancestors = [node(2, "Bacteria", "domain"), node(28901, "Salmonella enterica", "species")]
    named = taxon(594, "Salmonella gallinarum", "no rank", ancestors)
    other = taxon(
        550538,
        "Salmonella gallinarum (strain 287/91)",
        "strain",
        ancestors + [node(594, "Salmonella gallinarum", "no rank")],
    )
    result = audit.resolve_name({"results": [other, named]}, "Salmonella gallinarum")
    assert result["selected_taxon"]["taxon_id"] == "NCBITaxon:594"
    assert result["selected_taxon"]["rank"] == "no rank"
    assert result["selected_taxon"]["species_ancestor"]["taxonId"] == 28901
    assert result["selected_taxon"]["experimental_subject_assignment"] is False


@pytest.mark.parametrize("field", ["scientificName", "synonyms", "otherNames"])
def test_only_explicit_native_names_resolve(field):
    t = taxon(562, "Escherichia coli", "species", [node(2, "Bacteria", "domain")])
    name = "Source name"
    t[field] = name if field == "scientificName" else [name]
    result = audit.resolve_name({"results": [t]}, name)
    assert bool(result["selected_taxon"]) is (field != "otherNames")


@pytest.mark.parametrize("change", ["inactive", "ambiguous", "duplicate", "bad_parent", "no_species"])
def test_taxonomy_guards(change):
    t = taxon()
    payload = {"results": [t]}
    name = t["scientificName"]
    if change == "inactive":
        t["active"] = False
        assert audit.resolve_name(payload, name)["selected_taxon"] is None
    elif change == "ambiguous":
        other = copy.deepcopy(t)
        other["taxonId"] = 83334
        payload["results"].append(other)
        assert audit.resolve_name(payload, name)["status"] == "AMBIGUOUS_NATIVE_NAME"
    else:
        if change == "duplicate":
            payload["results"].append(copy.deepcopy(t))
        elif change == "bad_parent":
            t["parent"] = {"taxonId": 999, "scientificName": "wrong"}
        else:
            t["lineage"] = [node(2, "Bacteria", "domain")]
            t["parent"] = t["lineage"][-1]
        with pytest.raises(ValueError):
            audit.resolve_name(payload, name)


def test_query_scope_has_no_automatic_rank_or_gene_rewrite():
    assert parse_qs(urlsplit(audit.name_url("Salmonella gallinarum")).query)["query"] == [
        '"Salmonella gallinarum"'
    ]
    assert parse_qs(urlsplit(audit.gene_url(594, True)).query)["query"] == [
        "gene_exact:folP AND taxonomy_id:594 AND reviewed:true"
    ]


@pytest.mark.parametrize(
    ("taxid", "reviewed"), [(True, True), (0, True), (-1, False), ("562", True), (562, 1), (562, "true")]
)
def test_query_scope_rejects_invalid_types(taxid, reviewed):
    with pytest.raises(ValueError):
        audit.gene_url(taxid, reviewed)


def test_native_alias_and_reference_only_projection(entry):
    entry["genes"][0]["geneName"]["value"] = "folP1"
    entry["genes"][0]["synonyms"] = [{"value": "folP"}]
    protein, matches = audit.project(entry, taxon(), named_source(), True)
    assert matches == [{"gene_index": 0, "field": "synonyms", "value": "folP"}]
    assert protein["gene_names"] == ["folP", "folP1"]
    assert protein["reference_species_taxon_id"] == "NCBITaxon:562"
    assert protein["exact_resistance_allele"] is protein["experimental_subject_assignment"] is False
    assert protein["experimental_genome_assignment"] is None
    assert protein["resistance_inferred_from_reference"] is False
    assert protein["unflagged_means_complete"] is False
    assert "not exported" not in json.dumps(protein)
    assert all(c["primary_results_reviewed"] is False for c in protein["bibliography"])


def test_named_subspecies_scope_does_not_expand_to_whole_species(entry):
    ancestors = [node(2, "Bacteria", "domain"), node(28901, "Salmonella enterica", "species")]
    named = taxon(594, "Salmonella gallinarum", "no rank", ancestors)
    source = audit.resolve_name({"results": [named]}, "Salmonella gallinarum")["selected_taxon"]
    leaf = taxon(
        550538, "Salmonella strain", "strain", ancestors + [node(594, "Salmonella gallinarum", "no rank")]
    )
    entry["organism"] = {"taxonId": 550538, "scientificName": "Salmonella strain"}
    protein, _ = audit.project(entry, leaf, source, True)
    assert protein["reference_species_taxon_id"] == "NCBITaxon:28901"
    leaf["lineage"][-1] = node(595, "Different lineage", "no rank")
    leaf["parent"] = leaf["lineage"][-1]
    with pytest.raises(ValueError, match="outside the named taxon"):
        audit.project(entry, leaf, source, True)


@pytest.mark.parametrize(
    "change",
    [
        "missing_alias",
        "orf_only",
        "locus_only",
        "ambiguous",
        "wrong_taxon",
        "wrong_review",
        "missing_version",
        "sequence",
    ],
)
def test_protein_scope_guards(entry, change):
    if change in {"missing_alias", "orf_only", "locus_only"}:
        entry["genes"][0]["geneName"]["value"] = "folP1"
        entry["genes"][0]["synonyms"] = []
        if change == "orf_only":
            entry["genes"][0]["orfNames"] = [{"value": "folP"}]
        if change == "locus_only":
            entry["genes"][0]["orderedLocusNames"] = [{"value": "folP"}]
    elif change == "ambiguous":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change == "wrong_taxon":
        entry["organism"]["taxonId"] = 999
    elif change == "wrong_review":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change == "missing_version":
        entry["entryAudit"]["entryVersion"] = 0
    else:
        entry["sequence"] = {"value": "not admitted"}
    with pytest.raises(ValueError):
        audit.project(entry, taxon(), named_source(), True)


@pytest.mark.parametrize("reviewed", [True, False])
def test_complete_query_results_are_not_allele_assignments(entry, monkeypatch, reviewed):
    if not reviewed:
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
        entry["proteinDescription"]["flag"] = "Fragment"
    monkeypatch.setattr(
        audit.native,
        "read_source",
        lambda *args: ({"results": [entry], "suggestions": [{}]}, {"release": "2026_03"}),
    )
    entries, result = audit.read_gene(ROOT, {"url": audit.gene_url(562, reviewed)}, 562, reviewed)
    assert entries == [entry] and result["accessions"] == ["P0AC13"]
    assert result["complete_for_query"] is True and result["zero_hit_is_biological_absence"] is False
    assert result["suggestions_ignored"] == 1 and result["suggestions_followed"] is False
    protein, _ = audit.project(entry, taxon(), named_source(), reviewed)
    assert protein["native_protein_flag"] == (None if reviewed else "Fragment")
    assert protein["unflagged_means_complete"] is False


def test_duplicate_native_results_rejected(entry, monkeypatch):
    monkeypatch.setattr(audit.native, "read_source", lambda *args: ({"results": [entry, entry]}, {}))
    with pytest.raises(ValueError):
        audit.read_gene(ROOT, {"url": audit.gene_url(562, True)}, 562, True)


def test_empty_query_is_not_gene_absence(monkeypatch):
    monkeypatch.setattr(audit.native, "read_source", lambda *args: ({"results": []}, {}))
    entries, result = audit.read_gene(ROOT, {"url": audit.gene_url(562, True)}, 562, True)
    assert not entries and not result["accessions"] and result["zero_hit_is_biological_absence"] is False


def test_query_identity_mismatch_is_rejected():
    with pytest.raises(ValueError, match="query identity"):
        audit.read_gene(ROOT, {"url": audit.gene_url(28901, True)}, 594, True)


@pytest.mark.parametrize("change", ["rank", "name", "species", "ancestry", "flag"])
def test_independent_source_lineage_agreement(entry, change):
    source = named_source()
    if change == "flag":
        entry["proteinDescription"]["flag"] = "unknown"
    elif change == "species":
        source["species_ancestor"]["scientificName"] = "Different species"
    elif change == "ancestry":
        source["lineage"].insert(0, node(1, "different root", "no rank"))
    else:
        source["lineage"][-1]["rank" if change == "rank" else "scientificName"] = "different"
    with pytest.raises(ValueError):
        audit.project(entry, taxon(), source, True)


@pytest.fixture
def query_plan(tmp_path, monkeypatch):
    (tmp_path / "cohort.json").write_text("{}\n")
    pin = audit.reference.pin(tmp_path, tmp_path / "cohort.json")
    name = "Escherichia coli"
    plan = {
        "cohort": pin,
        "queries": {name: {"request_key": "one", "source_taxon_id": 562, "gene": "folP", "reviewed": True}},
        "requests": {"one": {"name": name, "source_taxon_id": 562, "reviewed": True}},
    }
    names = {name: {"selected_taxon": {"taxon_id": "NCBITaxon:562"}}}
    monkeypatch.setattr(audit, "planned_source", lambda *args: {"url": args[-1]})
    monkeypatch.setattr(audit, "read_gene", lambda *args: ([], {"accessions": []}))
    return tmp_path, plan, names


@pytest.mark.parametrize(
    "change",
    [
        "none",
        "cohort",
        "missing_query",
        "extra_request",
        "query_taxon",
        "request_taxon",
        "request_name",
        "query_review",
        "request_review",
        "gene",
    ],
)
def test_planned_query_guards(query_plan, change):
    directory, plan, names = query_plan
    query = plan["queries"]["Escherichia coli"]
    request = plan["requests"]["one"]
    if change == "cohort":
        plan["cohort"]["sha256"] = "wrong"
    elif change == "missing_query":
        plan["queries"] = {}
    elif change == "extra_request":
        plan["requests"]["extra"] = copy.deepcopy(request)
    elif change.endswith("taxon"):
        (query if change.startswith("query") else request)["source_taxon_id"] = 28901
    elif change.endswith("review"):
        (query if change.startswith("query") else request)["reviewed"] = 1
    elif change == "request_name":
        request["name"] = "Different species"
    elif change == "gene":
        query["gene"] = "folP1"
    (directory / "reviewed-plan.json").write_text(json.dumps(plan))
    if change == "none":
        assert audit.read_queries(directory, directory, names, True) == {
            "Escherichia coli": ([], {"accessions": []})
        }
    else:
        with pytest.raises(ValueError):
            audit.read_queries(directory, directory, names, True)


@pytest.mark.parametrize("change", ["none", "positive_reviewed", "stale_prior"])
def test_fallback_only_after_bound_complete_reviewed_zero_hit(query_plan, change):
    directory, plan, names = query_plan
    name = "Escherichia coli"
    prior = {name: ([], {"accessions": [], "complete_for_query": True})}
    plan["queries"][name].update({"reviewed": False, "prior_reviewed_query": copy.deepcopy(prior[name][1])})
    plan["requests"]["one"]["reviewed"] = False
    if change == "positive_reviewed":
        prior[name][1]["accessions"] = ["P0AC13"]
    elif change == "stale_prior":
        plan["queries"][name]["prior_reviewed_query"] = {}
    (directory / "unreviewed-plan.json").write_text(json.dumps(plan))
    if change == "none":
        assert audit.read_queries(directory, directory, names, False, prior)
    else:
        with pytest.raises(ValueError):
            audit.read_queries(directory, directory, names, False, prior)


def test_public_snapshot_covers_entire_source_cohort_without_mutable_records():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    index = json.loads(audit.reference.check_pin(ROOT, result["inputs"]["index"]).read_bytes())
    labels = json.loads(audit.reference.check_pin(ROOT, index["inputs"]["direct_candidates"]).read_bytes())[
        "determinants"
    ]
    expected = {tid for tid, t in labels.items() if audit.SELECT.search(t["labels"][0])}
    assert set(result["terms"]) == expected and len(expected) == 5
    assert len(result["records"]) == 10 and len(result["claims"]) == 21
    assert Counter(
        (c["record_identifier"], c["position"], c["aro_id"], c["claim_sha256"]) for c in result["claims"]
    ) == Counter(
        (c["record_identifier"], c["resistance_index"], c["aro_id"], c["claim_sha256"])
        for c in index["claims"]
        if c["aro_id"] in expected
    )
    used = set()
    for tid, term in result["terms"].items():
        assert term["record_memberships"] == index["terms"][tid]["record_memberships"]
        assert term["source_label_sha256"] == index["terms"][tid]["source_label_sha256"]
        assert term["exact_allele_assignment"] is term["experimental_subject_assignment"] is False
        assert term["experimental_genome_assignment"] is None and term["primary_review_status"] == "OPEN"
        q = term["queries"]
        selected = q.get("unreviewed", q["reviewed"])
        if "unreviewed" in q:
            assert q["reviewed"]["accessions"] == []
        assert {c["protein_accession"] for c in term["reference_candidates"]} == {
            "UniProtKB:" + a for a in selected["accessions"]
        }
        used.update(c["protein_accession"] for c in term["reference_candidates"])
    assert used == set(result["proteins"])
    gallinarum = result["terms"]["ARO:3007749"]
    assert gallinarum["named_reference_taxon_id"] == "NCBITaxon:594"
    assert gallinarum["named_reference_taxon_rank"] == "no rank"
    assert gallinarum["reference_status"] == "NO_EXACT_GENE_RESULTS_NOT_ABSENCE"
    leprae = result["terms"]["ARO:3003389"]
    assert leprae["reference_candidates"][0]["native_gene_field_matches"] == [
        {"gene_index": 0, "field": "synonyms", "value": "folP"}
    ]
    assert result["summary"]["reference_proteins"] == 10
    assert result["summary"]["terms_with_candidates"] == 4
    assert (
        result["summary"]["experimental_assignments"] == result["summary"]["biological_records_changed"] == 0
    )
