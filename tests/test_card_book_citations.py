"""Book identifiers preserve source scope and do not become allele evidence."""

import csv
import hashlib
import json
from pathlib import Path

import pytest
from rdflib import OWL, RDF, RDFS, XSD, BNode, Graph, Literal, URIRef

from scripts import audit_card_book_citations as audit

TID = "ARO:3000001"
NODE = URIRef(audit.citations.ontology.BASE + "3000001")
BOOK = "ISBN:978-92-4-008241-0"


def fixture(predicate=audit.citations.DEFINITION):
    graph, axiom, target = Graph(), BNode(), Literal("not exported")
    for triple in ((NODE, RDF.type, OWL.Class), (NODE, RDFS.label, Literal("fixture")),
                   (NODE, predicate, target), (axiom, RDF.type, OWL.Axiom),
                   (axiom, OWL.annotatedSource, NODE), (axiom, OWL.annotatedProperty, predicate),
                   (axiom, OWL.annotatedTarget, target), (axiom, audit.citations.XREF, Literal(BOOK))):
        graph.add(triple)
    return graph, axiom, target


@pytest.mark.parametrize("value", [BOOK, "ISBN:9789240082410"])
def test_valid_isbn13(value):
    assert audit.isbn13(Literal(value)) == "ISBN:9789240082410"


@pytest.mark.parametrize("value", ["ISBN:978-92-4-008241-1", "ISBN:1234567890128", "ISBN:9240082417",
                                   "ISBN:9789240082410 extra", "ISBN:978--9240082410", "ISBN:private"])
def test_bad_or_unsupported_isbn_is_not_repaired(value):
    assert audit.isbn13(Literal(value)) is None


def test_uri_is_not_an_isbn_literal():
    assert audit.isbn13(URIRef("ISBN:9789240082410")) is None


def test_direct_book_reference_keeps_original_identifier_and_exact_binding():
    graph, _, target = fixture()
    terms, original = audit.project(graph, {TID: "fixture"})
    row = terms[TID]
    annotation, = row["isbn_definition_annotations"]
    assert annotation["source_identifier"] == BOOK
    assert annotation["identifier"] == "ISBN:9789240082410"
    assert annotation["target"] == audit.citations.rdf_identity(target)
    assert row["bibliography_status"] == "BOOK_REFERENCE_WITHOUT_PUBMED_DOI"
    assert not row["biological_support_inferred"] and row["primary_review_status"] == "OPEN"
    assert original[TID]["definition_citation_ids"] == []
    assert len(original[TID]["definition_axioms"][0]["other_xrefs"]) == 1
    assert "not exported" not in json.dumps(terms)


def test_book_does_not_replace_paper_or_hide_bad_identifier():
    graph, axiom, _ = fixture()
    graph.add((axiom, audit.citations.XREF, Literal("PMID:12345")))
    graph.add((axiom, audit.citations.XREF, Literal("ISBN:private")))
    row = audit.project(graph, {TID: "fixture"})[0][TID]
    assert row["definition_pubmed_doi_ids"] == ["PMID:12345"]
    assert row["bibliography_status"] == "PUBMED_DOI_AND_BOOK_REFERENCES"
    assert len(row["unresolved_definition_xrefs"]) == 1
    assert "private" not in json.dumps(row)


def test_unrecognized_reference_is_not_reported_as_no_bibliography():
    graph, axiom, _ = fixture()
    graph.set((axiom, audit.citations.XREF, Literal("ISBN:private")))
    row = audit.project(graph, {TID: "fixture"})[0][TID]
    assert row["bibliography_status"] == "UNRECOGNIZED_DEFINITION_REFERENCES_REQUIRE_REVIEW"


@pytest.mark.parametrize("placement", ["synonym", "class", "parent"])
def test_nondirect_reference_is_not_inherited(placement):
    synonym = URIRef(audit.citations.ontology.NS["oboInOwl"] + "hasExactSynonym")
    graph, axiom, target = fixture(synonym if placement == "synonym" else audit.citations.DEFINITION)
    if placement == "class":
        graph.remove((axiom, audit.citations.XREF, None))
        graph.add((NODE, audit.citations.XREF, Literal(BOOK)))
    elif placement == "parent":
        parent = URIRef(audit.citations.ontology.BASE + "3000000")
        graph.set((axiom, OWL.annotatedSource, parent))
        graph.add((parent, audit.citations.DEFINITION, target))
        graph.add((NODE, RDFS.subClassOf, parent))
    row = audit.project(graph, {TID: "fixture"})[0][TID]
    assert not row["definition_isbn13_ids"]
    assert row["bibliography_status"] == "NO_DEFINITION_BIBLIOGRAPHY_IN_PINNED_SOURCE"


@pytest.mark.parametrize("target", [Literal("different"), Literal("not exported", lang="en"),
                                     Literal("not exported", datatype=XSD.string)])
def test_wrong_definition_target_fails_closed(target):
    graph, axiom, _ = fixture()
    graph.set((axiom, OWL.annotatedTarget, target))
    with pytest.raises(ValueError, match="not asserted"):
        audit.project(graph, {TID: "fixture"})


def test_record_rows_preserve_duplicate_assertions_and_unaffected_records():
    census = [{"identifier": i, "path": i, "record_sha256": "hash", "standard_inchi_key": "key"}
              for i in ("one", "two")]
    terms = {TID: {"record_memberships": ["one", "one"], "definition_isbn13_ids": [BOOK]}}
    rows = audit.record_rows(census, terms)
    assert rows[0]["book_citing_terms"] == [TID]
    assert rows[0]["book_reference_assertion_memberships"] == 2
    assert rows[1]["book_citing_terms"] == []
    assert {r["whole_record_primary_review"] for r in rows} == {"OPEN"}
    with pytest.raises(ValueError, match="duplicate"):
        audit.record_rows(census + census, terms)
    with pytest.raises(ValueError, match="outside"):
        audit.record_rows(census[1:], terms)


def test_public_successor_keeps_historical_bindings_without_freezing_live_corpus(monkeypatch):
    root = Path(__file__).resolve().parents[1]
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(root / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    public = json.loads((root / audit.OUTPUT).read_bytes())
    inputs = {}
    for key in ("prior", "expansion", "current_census"):
        pin = public["inputs"][key]
        raw = (root / pin["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == pin["sha256"]
        inputs[key] = (list(csv.DictReader(raw.decode().splitlines(), delimiter="\t"))
                       if key == "current_census" else json.loads(raw))
    assert len(public["terms"]) == 2002 and set(public["terms"]) == set(inputs["prior"]["terms"])
    for tid, row in public["terms"].items():
        old = inputs["prior"]["terms"][tid]
        assert row["definition_pubmed_doi_ids"] == old["definition_citation_ids"]
        assert row["record_memberships"] == old["record_memberships"]
        assert row["label_sha256"] == old["label_sha256"]
        assert not row["biological_support_inferred"] and row["primary_review_status"] == "OPEN"
        for annotation in row["isbn_definition_annotations"]:
            assert annotation["identifier"] == audit.isbn13(Literal(annotation["source_identifier"]))
            assert annotation["source_identifier_sha256"] == audit.citations.text_hash(
                annotation["source_identifier"])
            assert any(a["target"] == annotation["target"] and any(
                x["sha256"] == annotation["source_identifier_sha256"] for x in a["other_xrefs"])
                for a in old["definition_axioms"])
    assert public["records"] == audit.record_rows(inputs["current_census"], public["terms"])
    assert len(public["records"]) == 2939
    books = {t for t, r in public["terms"].items() if r["definition_isbn13_ids"]}
    uncited = {t for t, r in inputs["expansion"]["terms"].items() if not r["definition_citation_ids"]}
    assert len(books) == 36 and len(books & uncited) == 14 and len(uncited - books) == 308
    assert public["summary"]["whole_records_completed"] == 0
