"""Ontology ancestry must not manufacture protein, allele or organism mappings."""

import csv
import hashlib
import json
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_term_scope as scope  # noqa: E402


def tag(prefix, name):
    return "{" + scope.NS[prefix] + "}" + name


def iri(identifier):
    return scope.BASE + identifier.removeprefix("ARO:") if identifier.startswith("ARO:") else identifier


def document(classes, *, restrictions=(), split_labels=False):
    root = ET.Element(tag("rdf", "RDF"))
    meta = ET.SubElement(root, tag("owl", "Ontology"), {tag("rdf", "about"): "https://example.org/test"})
    ET.SubElement(meta, tag("oboInOwl", "date")).text = "fixture"
    for tid, parents in classes.items():
        node = ET.SubElement(root, tag("owl", "Class"), {tag("rdf", "about"): iri(tid)})
        for parent in parents:
            ET.SubElement(node, tag("rdfs", "subClassOf"), {tag("rdf", "resource"): iri(parent)})
        for subject, relation, target in restrictions:
            if subject == tid:
                sub = ET.SubElement(node, tag("rdfs", "subClassOf"))
                restriction = ET.SubElement(sub, tag("owl", "Restriction"))
                ET.SubElement(restriction, tag("owl", "onProperty"),
                              {tag("rdf", "resource"): iri(relation)})
                ET.SubElement(restriction, tag("owl", "someValuesFrom"),
                              {tag("rdf", "resource"): iri(target)})
        label_node = (ET.SubElement(root, tag("rdf", "Description"), {tag("rdf", "about"): iri(tid)})
                      if split_labels else node)
        ET.SubElement(label_node, tag("rdfs", "label")).text = scope.ANCHORS.get(tid, tid)
    for _, relation, _ in restrictions:
        node = ET.SubElement(root, tag("owl", "ObjectProperty"), {tag("rdf", "about"): iri(relation)})
        ET.SubElement(node, tag("rdfs", "label")).text = "confers_resistance_to_antibiotic"
    return ET.tostring(root)


def test_rdf_description_labels_join_their_class_statements():
    terms, _, date = scope.parse_ontology(document({"ARO:3000328": []}, split_labels=True))
    assert terms["ARO:3000328"]["label"] == scope.ANCHORS["ARO:3000328"]
    assert date == "fixture"


def test_restriction_target_is_not_an_is_a_parent():
    terms, edges, _ = scope.parse_ontology(document(
        {"ARO:3003402": [], "ARO:3000328": []},
        restrictions=[("ARO:3003402", "ARO:2000000", "ARO:3000328")],
    ))
    assert edges == {("ARO:3003402", "confers_resistance_to_antibiotic", "ARO:3000328")}
    assert terms["ARO:3003402"]["restriction_count"] == 1
    assert scope.shortest_path(terms, "ARO:3003402", "ARO:3000328") is None
    assert scope.term_scope(terms, "ARO:3003402", 0)["entity_scope"] == (
        "OTHER_TERM_ENTITY_GRANULARITY_UNRESOLVED")


def test_named_transitive_path_and_rna_scope():
    terms, _, _ = scope.parse_ontology(document({
        "ARO:3003402": ["ARO:3003211"], "ARO:3003211": ["ARO:3000328"], "ARO:3000328": [],
    }))
    result = scope.term_scope(terms, "ARO:3003402", 0)
    assert result["entity_scope"] == "RNA_TERM_NOT_A_PROTEIN_PRODUCT"
    assert result["anchor_paths"]["ARO:3000328"] == ["ARO:3003402", "ARO:3003211", "ARO:3000328"]
    assert scope.shortest_path(terms, "ARO:3000328", "ARO:3000328") == ["ARO:3000328"]


def test_rna_word_in_a_protein_label_is_not_rna_ancestry():
    terms, _, _ = scope.parse_ontology(document({"ARO:3005099": []}))
    terms["ARO:3005099"]["label"] = "23S rRNA methyltransferase"
    assert scope.term_scope(terms, "ARO:3005099", 0)["entity_scope"] == (
        "OTHER_TERM_ENTITY_GRANULARITY_UNRESOLVED")


def test_cycles_terminate_and_shortest_path_is_deterministic():
    terms, _, _ = scope.parse_ontology(document({
        "ARO:3000001": ["ARO:3000003", "ARO:3000002"],
        "ARO:3000002": ["ARO:3000001", "ARO:3000328"],
        "ARO:3000003": ["ARO:3000328"], "ARO:3000328": [],
    }))
    assert scope.shortest_path(terms, "ARO:3000001", "ARO:3000328") == [
        "ARO:3000001", "ARO:3000002", "ARO:3000328",
    ]
    assert scope.shortest_path(terms, "ARO:3000001", "ARO:9999999") is None


def test_overlapping_entity_anchors_require_review():
    terms, _, _ = scope.parse_ontology(document({
        "ARO:3000001": ["ARO:3000328", "ARO:0000010"], "ARO:3000328": [], "ARO:0000010": [],
    }))
    assert scope.term_scope(terms, "ARO:3000001", 0)["entity_scope"] == (
        "MULTIPLE_ENTITY_SCOPES_REQUIRE_REVIEW")


def test_external_parents_are_retained_without_fetching_and_block_selected_ancestry():
    terms, _, _ = scope.parse_ontology(document({"ARO:3000001": ["https://example.org/external"]}))
    assert terms["ARO:3000001"]["external_parents"] == ["https://example.org/external"]
    with pytest.raises(ValueError, match="leaves the supported ARO graph"):
        scope.term_scope(terms, "ARO:3000001", 0)


def test_missing_named_parent_fails_closed():
    with pytest.raises(ValueError, match="named parent missing"):
        scope.parse_ontology(document({"ARO:3000001": ["ARO:3000002"]}))


def test_conflicting_class_labels_fail_closed():
    root = ET.fromstring(document({"ARO:3000001": []}))
    node = root.find(tag("owl", "Class"))
    ET.SubElement(node, tag("rdfs", "label")).text = "conflicting label"
    with pytest.raises(ValueError, match="duplicate or unlabeled"):
        scope.parse_ontology(ET.tostring(root))


@pytest.fixture
def audit_input(tmp_path, monkeypatch):
    source = tmp_path / scope.card.SOURCE
    source.parent.mkdir(parents=True)
    row = {"determinant_id": "ARO:3003402", "determinant_name": "ARO:3003402",
           "relation": "confers_resistance_to_antibiotic", "antibiotic_id": "ARO:0000005"}
    with source.open("w") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(row), delimiter="\t")
        writer.writeheader()
        writer.writerow(row)
    record_path = tmp_path / "data/antibiotics/fixture.yaml"
    record_path.parent.mkdir(parents=True)
    record_path.write_text("fixture\n")
    claim = {"aro_id": "ARO:3003402", "label": "ARO:3003402", "evidence": [
        {"reference": "ARO:3003402", "notes": "CARD/ARO asserts fixture"},
    ]}
    corpus = {"records": [{"identifier": "CHEBI:1", "path": "data/antibiotics/fixture.yaml",
                           "sha256": scope.common.digest(record_path.read_bytes()),
                           "resistance_mechanisms": [claim]}]}
    (tmp_path / "corpus.json").write_text(json.dumps(corpus))
    monkeypatch.setattr(scope.common, "OUT", tmp_path)
    audit = tmp_path / "audit.json"
    audit.write_text(json.dumps({
        "source_inventory_sha256": scope.common.digest(source.read_bytes()), "summary": {"release": "test"},
        "determinants": {"ARO:3003402": {"labels": ["ARO:3003402"], "candidates": [],
                                        "status": "NO_EXPLICIT_LINK_IN_THIS_RELEASE",
                                        "primary_review_status": "PENDING"}},
    }))
    ledger = tmp_path / "ledger.tsv"
    ledger.write_text("identifier\taro_id\tdeterminant_label\nCHEBI:1\tARO:3003402\tARO:3003402\n")
    classes = {**{t: [] for t in scope.ANCHORS}, "ARO:3003402": ["ARO:3000328"], "ARO:0000005": []}
    body = document(classes, restrictions=[("ARO:3003402", "ARO:2000000", "ARO:0000005")]).decode()
    cache = tmp_path / "cache.json"
    cache.write_text(json.dumps({
        "url": "https://raw.githubusercontent.com/arpcard/aro/" + "a" * 40 + "/aro.owl",
        "status": 200, "body": body, "bytes": len(body.encode()),
        "sha256": scope.common.digest(body.encode()), "retrieved_at": "fixture",
    }))
    return tmp_path, cache, audit, ledger


def test_full_analysis_preserves_scope_and_binds_license_to_the_actual_commit(audit_input):
    result = scope.analyze(*audit_input)
    assert result["summary"]["selected_terms"] == result["summary"]["selected_card_assertions"] == 1
    assert result["summary"]["source_inventory_edges_verified"] == 1
    assert result["attribution"]["ontology_license_url"] == (
        "https://github.com/arpcard/aro/blob/" + "a" * 40 + "/LICENSE")


@pytest.mark.parametrize("field,value", [
    ("sha256", "incorrect"), ("status", 403), ("bytes", 0),
    ("url", "https://example.org/not-the-approved-ontology.owl"),
])
def test_cache_identity_and_digest_fail_closed(audit_input, field, value):
    cache = audit_input[1]
    raw = json.loads(cache.read_bytes())
    raw[field] = value
    cache.write_text(json.dumps(raw))
    with pytest.raises(ValueError, match="cache identity or checksum"):
        scope.analyze(*audit_input)


def test_inventory_edge_must_exist_in_the_ontology(audit_input):
    root, _, audit, _ = audit_input
    source = root / scope.card.SOURCE
    source.write_text(source.read_text().replace("confers_resistance_to_antibiotic", "unasserted_relation"))
    raw = json.loads(audit.read_bytes())
    raw["source_inventory_sha256"] = scope.common.digest(source.read_bytes())
    audit.write_text(json.dumps(raw))
    with pytest.raises(ValueError, match="source resistance edge missing"):
        scope.analyze(*audit_input)


def test_current_membership_cannot_be_replaced_by_a_partial_ledger(audit_input):
    ledger = audit_input[3]
    ledger.write_text("identifier\taro_id\tdeterminant_label\n")
    with pytest.raises(ValueError, match="membership differs"):
        scope.analyze(*audit_input)


def test_unknown_canary_selection_fails_closed(audit_input):
    with pytest.raises(ValueError, match="invalid term selection"):
        scope.analyze(*audit_input, only=["ARO:9999999"])


def test_input_change_during_analysis_is_rejected(audit_input, monkeypatch):
    audit = audit_input[2]
    original = scope.term_scope

    def mutate(*args):
        result = original(*args)
        audit.write_text(audit.read_text() + "\n")
        return result

    monkeypatch.setattr(scope, "term_scope", mutate)
    with pytest.raises(ValueError, match="grounding input changed"):
        scope.analyze(*audit_input)


@pytest.fixture(scope="module")
def export():
    return json.loads((ROOT / "research/2026-10-09-card-term-scope.json").read_bytes())


def test_export_preserves_every_original_candidate_and_review_status(export):
    pin = export["reference_audit"]
    payload = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
    audit = json.loads(payload)
    assert set(export["terms"]) == set(audit["determinants"])
    for tid, term in export["terms"].items():
        prior = audit["determinants"][tid]
        assert term["reference_link_status"] == prior["status"]
        assert term["primary_review_status"] == prior["primary_review_status"] == "PENDING"
        assert term["reference_candidate_accessions"] == sorted(c["accession"] for c in prior["candidates"])


def test_export_keeps_nonprotein_unlinked_scopes_separate(export):
    unlinked = {t: d for t, d in export["terms"].items()
                if d["reference_link_status"] == "NO_EXPLICIT_LINK_IN_THIS_RELEASE"}
    assert len(unlinked) == export["summary"]["unlinked_terms"] == 1024
    counts = Counter(d["entity_scope"] for d in unlinked.values())
    assert dict(counts) == export["summary"]["unlinked_entity_scope_counts"]
    assert counts["RNA_TERM_NOT_A_PROTEIN_PRODUCT"] == 88
    assert counts["GENE_CLUSTER_NOT_ONE_PROTEIN"] == 14
    assert counts["EFFLUX_COMPLEX_OR_SUBUNIT_GRANULARITY_UNRESOLVED"] == 147
    assert counts["OTHER_TERM_ENTITY_GRANULARITY_UNRESOLVED"] == 775
    assert all(d["reference_candidate_accessions"] == [] for d in unlinked.values())


def test_export_scope_and_path_witnesses_do_not_claim_primary_completion(export):
    assert export["scope"] == scope.SCOPE
    assert export["selection"] == "ALL_EXISTING_CARD_TERMS"
    assert export["summary"]["corpus_records"] == 2939
    assert export["summary"]["selected_card_assertions"] == 4538
    assert export["summary"]["selected_card_records"] == 273
    assert export["summary"]["selected_terms"] == 2002
    for tid, term in export["terms"].items():
        for anchor, path in term["anchor_paths"].items():
            if path is not None:
                assert path[0] == tid and path[-1] == anchor
                assert len(path) == len(set(path))
    assert "no representative is selected" in " ".join(export["limitations"])
    assert "does not complete" in " ".join(export["limitations"])


def test_outside_ancestry_is_a_review_flag_not_a_claim_removal(export):
    expected = ["ARO:3009269", "ARO:3009270", "ARO:3009638"]
    assert export["summary"]["outside_determinant_ancestry"] == expected
    assert all(t in export["terms"] for t in expected)
    assert "not evidence that resistance is absent" in " ".join(export["limitations"])


def test_export_contains_no_new_biological_or_operational_fields(export):
    permitted = {
        "entity_scope", "named_parent_ids", "anchor_paths", "named_direct_subclass_count",
        "deprecated", "reference_link_status", "reference_candidate_accessions", "primary_review_status",
    }
    assert all(set(term) == permitted for term in export["terms"].values())
    assert export["reference_release"] == "2026_03"
    assert export["attribution"]["ontology_license"] == "CC-BY-4.0"
    assert "No NCBI request" in " ".join(export["limitations"])
