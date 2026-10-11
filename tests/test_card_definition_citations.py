"""A citation's presence and scope cannot substitute for primary evidence."""

import csv
import json
import sys
from pathlib import Path

import pytest
from rdflib import OWL, RDF, RDFS, XSD, BNode, Graph, Literal, URIRef

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_definition_citations as audit  # noqa: E402

TID = "ARO:3003307"
NODE = URIRef(audit.ontology.BASE + "3003307")
SYNONYM = URIRef(audit.ontology.NS["oboInOwl"] + "hasExactSynonym")


def fixture(*, predicate=audit.DEFINITION, target=None):
    graph = Graph()
    graph.add((NODE, RDF.type, OWL.Class))
    graph.add((NODE, RDFS.label, Literal("fixture")))
    target = Literal("private content") if target is None else target
    graph.add((NODE, predicate, target))
    axiom = BNode()
    for key, value in ((RDF.type, OWL.Axiom), (OWL.annotatedSource, NODE),
                       (OWL.annotatedProperty, predicate), (OWL.annotatedTarget, target),
                       (audit.XREF, Literal("PMID:12345"))):
        graph.add((axiom, key, value))
    return graph, axiom, target


def project(graph):
    return audit.project_annotations(graph, {TID: "fixture"})[TID]


def test_exact_definition_binding_and_no_text_or_support_export():
    graph, _, _ = fixture()
    result = project(graph)
    assert result["definition_citation_ids"] == ["PMID:12345"]
    assert result["definition_citation_status"] == "CITATIONS_PRESENT_PRIMARY_SUPPORT_UNREVIEWED"
    assert result["biological_support_inferred"] is False
    assert "private content" not in json.dumps(result)
    assert "fixture" not in json.dumps(result)


def test_synonym_and_class_xrefs_are_not_definition_support():
    graph, _, _ = fixture(predicate=SYNONYM)
    graph.add((NODE, audit.XREF, Literal("PMID:67890")))
    result = project(graph)
    assert result["definition_citation_ids"] == []
    assert result["definition_axioms"] == []
    assert result["other_axioms"][0]["identifiers"] == ["PMID:12345"]
    assert result["class_xrefs"]["identifiers"] == ["PMID:67890"]
    assert result["definition_citation_status"] == "NO_ALLOWLISTED_DEFINITION_CITATION_IN_PINNED_ONTOLOGY"


@pytest.mark.parametrize("key", [OWL.annotatedSource, OWL.annotatedProperty, OWL.annotatedTarget])
def test_multiple_binding_values_fail_closed(key):
    graph, axiom, _ = fixture()
    graph.add((axiom, key, URIRef("https://example.org/other")))
    with pytest.raises(ValueError, match="ambiguous or missing"):
        project(graph)


@pytest.mark.parametrize("key", [OWL.annotatedProperty, OWL.annotatedTarget])
def test_missing_selected_axiom_binding_fails_closed(key):
    graph, axiom, _ = fixture()
    graph.remove((axiom, key, None))
    with pytest.raises(ValueError, match="ambiguous or missing"):
        project(graph)


@pytest.mark.parametrize("replacement", [Literal("different"), Literal("private content", lang="en"),
                                          Literal("private content", datatype=XSD.string)])
def test_unasserted_or_different_rdf_literal_cannot_supply_citation(replacement):
    graph, axiom, _ = fixture()
    graph.set((axiom, OWL.annotatedTarget, replacement))
    with pytest.raises(ValueError, match="triple is not asserted"):
        project(graph)


def test_language_and_datatype_are_preserved_in_identity():
    graph, _, _ = fixture(target=Literal("private content", lang="en"))
    assert project(graph)["definition_axioms"][0]["target"]["language"] == "en"
    graph, _, _ = fixture(target=Literal("private content", datatype=XSD.string))
    assert project(graph)["definitions"][0]["datatype"] == str(XSD.string)


def test_ancestor_citations_are_not_inherited():
    graph, axiom, target = fixture()
    parent = URIRef(audit.ontology.BASE + "3000000")
    graph.set((axiom, OWL.annotatedSource, parent))
    graph.add((parent, audit.DEFINITION, target))
    graph.add((NODE, RDFS.subClassOf, parent))
    assert project(graph)["definition_citation_ids"] == []


def test_unknown_or_malformed_xrefs_remain_hashed():
    result = audit.bibliography([Literal("ISBN:private"), Literal("PMID:0"), Literal("PMID:12 prose"),
                                 URIRef("https://example.org/PMID:12"), Literal("DOI:10.1234/example"),
                                 Literal("PMID:12345"), Literal("PMID:12345")])
    assert result["identifiers"] == ["DOI:10.1234/example", "PMID:12345"]
    assert len(result["other_xrefs"]) == 4
    assert "private" not in json.dumps(result)


@pytest.mark.parametrize("mutation", ["label", "class", "deprecated"])
def test_source_class_identity_fails_closed(mutation):
    graph, _, _ = fixture()
    if mutation == "label":
        graph.add((NODE, RDFS.label, Literal("other")))
    elif mutation == "class":
        graph.remove((NODE, RDF.type, OWL.Class))
    else:
        graph.add((NODE, OWL.deprecated, Literal(True)))
    with pytest.raises(ValueError, match="identity|deprecated"):
        project(graph)


def test_blank_annotation_value_fails_closed():
    with pytest.raises(ValueError, match="anonymous"):
        audit.bibliography([BNode()])


@pytest.fixture
def corpus(tmp_path, monkeypatch):
    path = tmp_path / "data/antibiotics/fixture.yaml"
    path.parent.mkdir(parents=True)
    path.write_text("fixture\n")
    census = tmp_path / "census.tsv"
    row = {"identifier": "CHEBI:1", "path": str(path.relative_to(tmp_path)),
           "record_sha256": audit.reference.digest(path), "standard_inchi_key": "FIXTURE"}
    with census.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(row), delimiter="\t")
        writer.writeheader()
        writer.writerow(row)
    record = {"identifier": "CHEBI:1", "chemical_structure": {"standard_inchi_key": "FIXTURE"},
              "resistance_mechanisms": [{"aro_id": TID, "label": "fixture", "evidence": [
                  {"reference": TID, "notes": "CARD/ARO asserts fixture"}]}]}
    monkeypatch.setattr(audit, "load_record", lambda _: record)
    return tmp_path, census, path, record


def test_only_source_owned_claims_are_citation_audit_members(corpus):
    root, census, _, record = corpus
    record["resistance_mechanisms"].append({"aro_id": TID, "label": "curated", "evidence": [
        {"reference": "PMID:12345", "notes": "curator evidence"}]})
    rows, labels, memberships, records = audit.read_corpus(root, census)
    assert len(rows) == len(records) == 1
    assert labels == {TID: "fixture"}
    assert memberships == {TID: ["CHEBI:1"]}


@pytest.mark.parametrize("mutation", ["hash", "identifier", "structure", "ignored_extra", "duplicate"])
def test_whole_corpus_census_guard(corpus, mutation):
    root, census, path, record = corpus
    if mutation == "hash":
        path.write_text("changed\n")
    elif mutation == "identifier":
        record["identifier"] = "CHEBI:2"
    elif mutation == "structure":
        record["chemical_structure"]["standard_inchi_key"] = "OTHER"
    elif mutation == "ignored_extra":
        (root / ".gitignore").write_text("**/extra.yaml\n")
        path.with_name("extra.yaml").write_text("extra\n")
    else:
        with census.open("a") as stream:
            stream.write(census.read_text().splitlines()[1] + "\n")
    with pytest.raises(ValueError, match="checksum|identity|uniquely cover"):
        audit.read_corpus(root, census)


def test_published_audit_keeps_full_scope_and_no_biological_promotion():
    result = json.loads((ROOT / audit.DEFAULT_OUTPUT).read_bytes())
    assert result["scope"] == audit.SCOPE
    assert result["selection"] == "ALL_EXISTING_CARD_TERMS"
    assert result["summary"]["corpus_records_checked"] == 2939
    assert result["summary"]["terms"] == len(result["terms"]) == 2002
    assert result["summary"]["source_assertion_memberships"] == 4538
    assert sum(len(r["record_memberships"]) for r in result["terms"].values()) == 4538
    assert result["summary"]["biological_records_changed"] == 0
    assert result["summary"]["whole_record_reviews_completed"] == 0
    assert all(r["biological_support_inferred"] is False for r in result["terms"].values())
    expected = {"ARO:3003307": "PMID:19104017", "ARO:3003317": "PMID:19104017",
                "ARO:3007751": "PMID:37627729", "ARO:3007752": "PMID:37627729"}
    assert all(result["terms"][tid]["definition_citation_ids"] == [pmid] for tid, pmid in expected.items())
