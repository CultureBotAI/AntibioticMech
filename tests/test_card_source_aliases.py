"""Source aliases, native fields and reference taxonomy cannot stand in for alleles."""

import builtins
import io
import json
import socket
import sys
from pathlib import Path

import pytest
import requests
from rdflib import OWL, RDF, RDFS, Graph, Literal, URIRef

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_source_aliases as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def source_fixture(gene="foo", definition="A source definition."):
    term = "ARO:1234567"
    node = URIRef(audit.definitions.ontology.BASE + "1234567")
    label = "Example species " + gene
    graph = Graph()
    for triple in (
        (node, RDF.type, OWL.Class),
        (node, RDFS.label, Literal(label)),
        (node, audit.definitions.DEFINITION, Literal(definition)),
        (node, audit.EXACT, Literal("bar")),
    ):
        graph.add(triple)
    selected = {
        term: {
            "source_label": label,
            "tokens": {"gene": gene},
            "record_memberships": ["CHEBI:1"],
            "definition_citations": [],
        }
    }
    projected = audit.definitions.project_annotations(graph, {term: label})
    projected[term]["record_memberships"] = ["CHEBI:1"]
    return graph, node, selected, {"terms": projected}


def test_exact_source_alias_retains_rdf_binding():
    graph, _, selected, dossier = source_fixture()
    aliases = {"ARO:1234567": [{"kind": "GENE_SYMBOL", "value": "bar"}]}
    row = audit.annotation_context(graph, selected, dossier, aliases)["ARO:1234567"]
    assert row["selected_alias_leads"][0]["predicate"] == str(audit.EXACT)
    assert row["unselected_synonyms_are_gene_aliases"] is False
    assert row["source_flags"] == []


@pytest.mark.parametrize(
    "mutation",
    [
        "missing",
        "related",
        "language",
        "case",
        "duplicate",
        "kind",
        "outside",
        "membership",
        "label",
        "definition",
        "deprecated",
    ],
)
def test_source_binding_mutations_fail_closed(mutation):
    graph, node, selected, dossier = source_fixture()
    alias = {"kind": "GENE_SYMBOL", "value": "bar"}
    aliases = {"ARO:1234567": [alias]}
    if mutation in {"missing", "related", "language", "case"}:
        graph.remove((node, audit.EXACT, Literal("bar")))
    if mutation == "related":
        graph.add((node, audit.SYNONYMS[1], Literal("bar")))
    elif mutation == "language":
        graph.add((node, audit.EXACT, Literal("bar", lang="en")))
    elif mutation == "case":
        graph.add((node, audit.EXACT, Literal("BAR")))
    elif mutation == "duplicate":
        aliases["ARO:1234567"].append(alias)
    elif mutation == "kind":
        alias["kind"] = "FAMILY"
    elif mutation == "outside":
        aliases["ARO:9999999"] = [alias]
    elif mutation == "membership":
        selected["ARO:1234567"]["record_memberships"] = ["CHEBI:2"]
    elif mutation == "label":
        selected["ARO:1234567"]["source_label"] = "Different species foo"
    elif mutation == "definition":
        graph.add((node, audit.definitions.DEFINITION, Literal("New definition")))
    elif mutation == "deprecated":
        graph.add((node, OWL.deprecated, Literal(True)))
    with pytest.raises(ValueError):
        audit.annotation_context(graph, selected, dossier, aliases)


@pytest.mark.parametrize("gene,expected", [("MDR1", False), ("MDR2", True), ("MDR4", True)])
def test_label_definition_conflict_is_not_a_correction(gene, expected):
    graph, _, selected, dossier = source_fixture(gene, "MDR1 encodes an example protein.")
    row = audit.annotation_context(graph, selected, dossier, {})["ARO:1234567"]
    assert bool(row["source_flags"]) is expected
    assert all(f["correct_gene_inferred"] is False for f in row["source_flags"])
    assert row["selected_alias_leads"] == []


def test_alias_namespaces_are_distinct():
    entry = {
        "primaryAccession": "P12345",
        "secondaryAccessions": ["Q12345"],
        "genes": [
            {
                "geneName": {"value": "foo"},
                "synonyms": [{"value": "bar"}],
                "orderedLocusNames": [{"value": "LOC123"}],
                "orfNames": [{"value": "ORF1"}],
            }
        ],
    }
    assert audit.alias_matches(entry, {"kind": "GENE_SYMBOL", "value": "BAR"})
    assert audit.alias_matches(entry, {"kind": "ORDERED_LOCUS", "value": "loc123"})
    assert audit.alias_matches(entry, {"kind": "ACCESSION_LIKE_SYNONYM", "value": "Q12345"})
    for kind, values in {
        "GENE_SYMBOL": ["LOC123", "ORF1", "P12345", "fo"],
        "ORDERED_LOCUS": ["foo", "bar", "ORF1"],
        "ACCESSION_LIKE_SYNONYM": ["foo", "q12345", "LOC123"],
    }.items():
        for value in values:
            assert not audit.alias_matches(entry, {"kind": kind, "value": value})


def test_species_identity_is_not_name_only_or_taxid_only():
    species = {"taxonId": 1, "rank": "species", "scientificName": "Example species"}
    assert audit.reference_status(species, species) == audit.QUALIFIED
    for other in (
        None,
        {**species, "rank": "strain"},
        {**species, "taxonId": 2},
        {**species, "scientificName": "Changed species"},
    ):
        assert audit.reference_status(species, other) != audit.QUALIFIED


def saved():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_saved_coverage_and_reference_limits():
    d = saved()
    assert d["summary"]["selected_terms"] == 42
    assert d["summary"]["selected_alias_leads"] == 4
    assert d["summary"]["source_conflict_terms"] == 2
    assert d["summary"]["qualified_reference_terms"] == 1
    assert d["summary"]["qualified_reference_links"] == 2
    assert d["summary"]["unresolved_terms_in_selected_cohort"] == 41
    term = d["terms"]["ARO:3003737"]
    assert term["qualified_reference_accessions"] == ["UniProtKB:Q7A084", "UniProtKB:W8U3X2"]
    assert len(term["reference_candidates"]) == 6
    assert all(not c["own_definition_citation_query_overlap"] for c in term["reference_candidates"])
    assert all(not c["exact_allele_assignment"] for c in term["reference_candidates"])
    assert not d["summary"]["network_requests"]
    assert not d["summary"]["biological_record_writes"]


def test_offline_replay_is_read_only(monkeypatch, pre_cdsa_qualification_root):
    d = saved()
    if not (ROOT / d["ontology_cache"]["path"]).exists():
        pytest.skip("ignored native cache unavailable; portable checks still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not any(c in mode for c in "wax+"), "audit attempted file mutation"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == d


def test_cli_creates_nested_output_and_refuses_drift(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {"network_requests": 0}})
    output = tmp_path / "nested" / "audit.json"
    monkeypatch.setattr(sys, "argv", ["audit", "--root", str(tmp_path), "--output", str(output)])
    audit.main()
    assert output.exists()
    audit.main()
    output.write_text("{}")
    with pytest.raises(ValueError, match="differs"):
        audit.main()
    assert output.read_text() == "{}"


def test_cli_check_never_creates_output(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    output = tmp_path / "missing" / "audit.json"
    monkeypatch.setattr(sys, "argv", ["audit", "--root", str(tmp_path), "--output", str(output), "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not output.parent.exists()


@pytest.mark.parametrize(
    "mutation", ["incomplete", "release", "sequence", "features", "comments", "own_query_drift"]
)
def test_cached_queries_reject_incomplete_or_operational_results(monkeypatch, mutation):
    provenance = {"complete_for_query": True, "release": "2026_03"}
    frozen = {"queries": {"123": {"directory": "cache", "query": dict(provenance)}}}
    selected = {"ARO:1": {"definition_citations": ["PMID:123"]}}
    plan = {
        "own_citation_plan": {},
        "cached_candidate_queries": {},
        "aliases": {"ARO:1": [{"kind": "GENE_SYMBOL", "value": "bar"}]},
    }
    entry = {"primaryAccession": "P12345", "genes": []}
    if mutation == "incomplete":
        provenance["complete_for_query"] = False
    elif mutation == "release":
        provenance["release"] = "2026_04"
    elif mutation == "own_query_drift":
        provenance["changed"] = True
    else:
        entry[mutation] = []
    monkeypatch.setattr(audit, "read_json", lambda *a: frozen)
    monkeypatch.setattr(audit.literature, "read_query", lambda *a: ({"P12345": entry}, provenance))
    with pytest.raises(ValueError):
        audit.read_queries(ROOT, plan, selected)
