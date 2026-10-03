"""Taxonomic scope is explicit, complete, and never inferred from label strings."""

import copy
import io
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_ncbi_ast_overlap as audit  # noqa: E402
import ncbi_ast_taxonomy as taxonomy  # noqa: E402
import seed_from_sources as seed  # noqa: E402

ROOT = [("131567", "cellular organisms"), ("2", "Bacteria")]
MYCO = [*ROOT, ("1763", "Mycobacterium")]


def xml_tree():
    root = ET.Element("TaxaSet")
    for taxid, name, lineage in [
        ("562", "Escherichia coli", [*ROOT, ("561", "Escherichia")]),
        (taxonomy.SCOPE_TAXID, taxonomy.SCOPE_NAME, MYCO),
    ]:
        node = ET.SubElement(root, "Taxon")
        values = {"TaxId": taxid, "ScientificName": name,
                  "ParentTaxId": lineage[-1][0], "Lineage": "; ".join(n for _, n in lineage)}
        for tag, value in values.items():
            ET.SubElement(node, tag).text = value
        expanded = ET.SubElement(node, "LineageEx")
        for ancestor, ancestor_name in lineage:
            entry = ET.SubElement(expanded, "Taxon")
            ET.SubElement(entry, "TaxId").text = ancestor
            ET.SubElement(entry, "ScientificName").text = ancestor_name
    return root


def records():
    return taxonomy.parse_taxonomy(ET.tostring(xml_tree()), ["562", taxonomy.SCOPE_TAXID])


def row(taxid="562", sample="SAMN1", count="1"):
    return {"taxon_id": "NCBITaxon:" + taxid if taxid else "",
            "taxon_label": taxonomy.SCOPE_NAME if taxid == taxonomy.SCOPE_TAXID else "Escherichia coli",
            "biosample_accession": sample, "ast_row_count": count}


def test_requested_taxids_use_identifiers_not_names():
    assert taxonomy.requested_taxids([row(), row(), row("")]) == ["562", taxonomy.SCOPE_TAXID]
    with pytest.raises(ValueError, match="invalid AST taxon_id"):
        taxonomy.requested_taxids([{"taxon_id": "Escherichia coli"}])


def test_relationship_distinguishes_complex_descendants_ancestors_and_unknowns():
    data = records()
    data["1773"] = dict(taxid="1773", scientific_name="Mycobacterium tuberculosis",
                        lineage_taxids=[*(t for t, _ in MYCO), taxonomy.SCOPE_TAXID])
    data["1763"] = dict(taxid="1763", scientific_name="Mycobacterium", lineage_taxids=[t for t, _ in ROOT])
    assert taxonomy.relationship("562", data) == "OUTSIDE_SCOPE"
    assert taxonomy.relationship(taxonomy.SCOPE_TAXID, data) == "WITHIN_SCOPE"
    assert taxonomy.relationship("1773", data) == "WITHIN_SCOPE"
    assert taxonomy.relationship("1763", data) == "ANCESTOR_OF_SCOPE"
    assert taxonomy.relationship("999", data) == "UNRESOLVED"
    data["562"]["lineage_taxids"] = ["561"]
    assert taxonomy.relationship("562", data) == "UNRESOLVED"
    data[taxonomy.SCOPE_TAXID]["scientific_name"] = "a different scope"
    with pytest.raises(ValueError, match="complex identity"):
        taxonomy.relationship("562", data)


@pytest.mark.parametrize("mutation", [
    lambda r: r[0].remove(r[0].find("LineageEx")),
    lambda r: setattr(r[0].find("ParentTaxId"), "text", "999"),
    lambda r: setattr(r[0].find("Lineage"), "text", "different lineage"),
    lambda r: setattr(r[0].find("TaxId"), "text", "merged-away-id"),
    lambda r: setattr(r[0].find("ScientificName"), "text", ""),
    lambda r: r.append(copy.deepcopy(r[0])),
    lambda r: r.remove(r[0]),
    lambda r: ET.SubElement(r, "ERROR"),
    lambda r: r[0].find("LineageEx").append(copy.deepcopy(r[0].find("LineageEx/Taxon"))),
    lambda r: r[0].append(copy.deepcopy(r[0].find("TaxId"))),
])
def test_incomplete_or_contradictory_taxonomy_is_rejected(mutation):
    root = xml_tree()
    mutation(root)
    with pytest.raises(ValueError):
        taxonomy.parse_taxonomy(ET.tostring(root), ["562", taxonomy.SCOPE_TAXID])


def test_shared_ancestor_paths_must_agree():
    root = xml_tree()
    root[0].find("LineageEx/Taxon/ScientificName").text = "different root"
    root[0].find("Lineage").text = "different root; Bacteria; Escherichia"
    with pytest.raises(ValueError, match="inconsistent lineage"):
        taxonomy.parse_taxonomy(ET.tostring(root), ["562", taxonomy.SCOPE_TAXID])


def test_scope_counts_measurements_without_mutating_rows_or_hiding_conflicts():
    rows = [row(count="3"), row(sample="SAMN2", count="4"), row(taxonomy.SCOPE_TAXID), row("")]
    original = copy.deepcopy(rows)
    result = audit.taxonomy_scope(rows, records(), {"all_samples": {"SAMN2"}})
    assert rows == original
    assert result["conclusion"] == "REVIEW_REQUIRED"
    assert result["counts"]["OUTSIDE_SCOPE"] == {"groups": 1, "measurements": 3}
    assert result["counts"]["TAXON_SAMPLE_CONFLICT"] == {"groups": 1, "measurements": 4}
    assert result["counts"]["WITHIN_SCOPE"]["groups"] == 1
    assert result["counts"]["UNRESOLVED"]["groups"] == 1
    outside = audit.taxonomy_scope([row()], records(), {"all_samples": set()})
    assert outside["conclusion"] == "DISJOINT_BY_REPORTED_TAXONOMY"
    assert audit.taxonomy_scope([], records(), {"all_samples": set()})["conclusion"] == "REVIEW_REQUIRED"


def test_new_cryptic_release_requires_scope_review(monkeypatch):
    monkeypatch.setattr(audit.cryptic, "VERSION", "new")
    with pytest.raises(ValueError, match="release scope"):
        audit.taxonomy_scope([row()], records(), {"all_samples": set()})


def test_taxid_name_disagreement_cannot_establish_disjointness():
    candidate = {**row(), "taxon_label": taxonomy.SCOPE_NAME}
    result = audit.taxonomy_scope([candidate], records(), {"all_samples": set()})
    assert result["conclusion"] == "REVIEW_REQUIRED"
    assert result["counts"]["TAXON_LABEL_REVIEW"]["groups"] == 1
    assert result["counts"]["OUTSIDE_SCOPE"]["groups"] == 0
    assert result["taxa"][0]["source_taxon_labels"] == [taxonomy.SCOPE_NAME]
    assert result["taxa"][0]["scientific_name"] == "Escherichia coli"


def fake_snapshot(tmp_path, monkeypatch):
    report = tmp_path / "activity.tsv"
    report.write_text("test report")
    monkeypatch.setattr(seed, "load_ncbi_ast_activity_inventory", lambda _: [row()])
    requests = []

    def retrieve(request, timeout):
        requests.append(request)
        return io.BytesIO(ET.tostring(xml_tree()))

    monkeypatch.setattr(taxonomy, "urlopen", retrieve)
    directory = tmp_path / "snapshot"
    taxonomy.fetch_snapshot(report, directory)
    assert requests[0].get_method() == "POST"
    assert b"db=taxonomy" in requests[0].data
    return report, directory


def test_snapshot_roundtrip_and_no_overwrite(tmp_path, monkeypatch):
    report, directory = fake_snapshot(tmp_path, monkeypatch)
    assert taxonomy.load_snapshot(directory, report, [row()]) == records()
    before = (directory / "snapshot.json").read_bytes()
    with pytest.raises(ValueError, match="already exists"):
        taxonomy.fetch_snapshot(report, directory)
    assert (directory / "snapshot.json").read_bytes() == before


@pytest.mark.parametrize("field,value", [
    ("source", "other"), ("endpoint", "https://example.org"), ("file", "../taxonomy.xml"),
    ("source_retrieved_on", "not a date"), ("requested_taxids", ["562"]),
    ("sha256", "0" * 64), ("bytes", 0), ("activity_report_sha256", "0" * 64),
])
def test_snapshot_metadata_drift_is_rejected(tmp_path, monkeypatch, field, value):
    report, directory = fake_snapshot(tmp_path, monkeypatch)
    path = directory / "snapshot.json"
    metadata = json.loads(path.read_text())
    metadata[field] = value
    path.write_text(json.dumps(metadata))
    with pytest.raises(ValueError):
        taxonomy.load_snapshot(directory, report, [row()])


def test_partial_response_never_publishes_snapshot(tmp_path, monkeypatch):
    report = tmp_path / "activity.tsv"
    report.write_text("test report")
    monkeypatch.setattr(seed, "load_ncbi_ast_activity_inventory", lambda _: [row()])
    monkeypatch.setattr(taxonomy, "urlopen", lambda *a, **kw: io.BytesIO(b"<TaxaSet/>"))
    directory = tmp_path / "snapshot"
    with pytest.raises(ValueError, match="exact requested TaxIDs"):
        taxonomy.fetch_snapshot(report, directory)
    assert not directory.exists()
