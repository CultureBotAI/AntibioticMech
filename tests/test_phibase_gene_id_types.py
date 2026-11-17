"""Reference cross-reference presence is neither a gene type nor subject proof."""

import copy
import csv
import io
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_phibase_gene_ids as audit  # noqa: E402


@pytest.fixture
def reference():
    return {
        "primaryAccession": "P12345", "entryAudit": {"entryVersion": 9, "sequenceVersion": 2},
        "organism": {"taxonId": 1, "scientificName": "Reference organism"},
        "genes": [{"geneName": {"value": "GENE"}, "synonyms": [{"value": "ALIAS"}],
                   "orderedLocusNames": [{"value": "LOCUS"}], "orfNames": [{"value": "TRANSCRIPT"}]}],
        "uniProtKBCrossReferences": [
            {"database": "EnsemblFungi", "id": "TRANSCRIPT", "properties": [
                {"key": "GeneId", "value": "LOCUS"}, {"key": "ProteinId", "value": "PROTEIN"}]},
            {"database": "EnsemblFungi", "id": "PROTEIN", "properties": [
                {"key": "GeneId", "value": "OTHER_LOCUS"}, {"key": "ProteinId", "value": "PROTEIN"}]},
            {"database": "Other", "id": "GENERIC", "properties": []},
            {"database": "Other", "id": "OTHER", "properties": [
                {"key": "TranscriptId", "value": "EXPLICIT_TRANSCRIPT"},
                {"key": "GeneId", "value": "MIXED"}, {"key": "ProteinId", "value": "MIXED"}]},
        ],
        "sequence": {"value": "DO_NOT_EXPORT"}, "features": [{"type": "Variant", "value": "SECRET"}],
        "comments": [{"text": "Do not copy biological annotations"}],
    }


@pytest.mark.parametrize("value,genes,types,primary", [
    ("GENE", ["geneName"], [], False), ("ALIAS", ["synonyms"], [], False),
    ("LOCUS", ["orderedLocusNames"], ["GeneId"], False),
    ("TRANSCRIPT", ["orfNames"], [], True), ("PROTEIN", [], ["ProteinId"], True),
    ("EXPLICIT_TRANSCRIPT", [], ["TranscriptId"], False),
    ("MIXED", [], ["GeneId", "ProteinId"], False), ("GENERIC", [], [], True),
    ("", [], [], False), ("protein", [], [], False), ("PROTEIN.1", [], [], False),
    ("LOCUS-T", [], [], False),
])
def test_field_types_remain_separate_and_matching_is_exact(reference, value, genes, types, primary):
    projected = audit.reference_projection(reference)
    hits = audit.identifier_matches(value, projected)
    summary = audit.match_summary(value, hits)
    assert summary["gene_annotation_fields"] == genes
    assert summary["typed_cross_reference_properties"] == types
    assert summary["primary_cross_reference_id_match"] is primary
    assert not summary["experimental_identity_verified"]
    assert reference["sequence"]["value"] == "DO_NOT_EXPORT"
    assert "DO_NOT_EXPORT" not in json.dumps(projected)
    assert "SECRET" not in json.dumps(projected)


@pytest.fixture
def inputs(reference):
    rows = [{"identifier": "CHEBI:1", "pmid": "1", "protein_accession": "P12345", "gene_id": value}
            for value in ("PROTEIN", "TRANSCRIPT", "", "GENERIC")]
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t")
    writer.writeheader()
    writer.writerows(rows)
    inventory = stream.getvalue().encode()
    grounding = json.dumps({"source_inventory_sha256": audit.digest(inventory),
        "entries": {"P12345": reference},
        "requests": [{"headers": {"X-UniProt-Release": "test_release"}}]}).encode()
    historical = json.dumps({"source_inventory_sha256": audit.digest(inventory),
        "grounding_sha256": audit.digest(grounding), "rows": [{"source": r} for r in rows]}).encode()
    reviews = {audit.row_digest(rows[0]): {"review_id": "rejected-reference", "withhold": ["gene_id"],
                                         "misassigned": ["gene_id"]}}
    return inventory, grounding, historical, rows, reviews


def test_complete_accounting_retains_rejected_reference_and_missing_values(inputs):
    report = audit.build_report(*inputs)
    assert report["summary"] == {
        "source_rows": 4, "empty_source_gene_ids": 1, "nonempty_source_gene_ids": 3,
        "reference_entries": 1, "distinct_identifier_reference_pairs": 3,
        "gene_annotation_field_matches": 1, "typed_property_matches": {"ProteinId": 1},
        "primary_id_only_matches": 1, "unmatched_source_values": 0,
        "already_rejected_source_gene_ids": 1, "experimental_identifiers_assigned": 0,
    }
    rejected = report["rows"][0]
    assert rejected["current_review"]["source_gene_id_rejected"]
    assert not rejected["match_summary"]["experimental_identity_verified"]
    assert report["reference_releases"] == ["test_release"]
    assert all("alteration" not in r and "strain" not in r for r in report["rows"])


@pytest.mark.parametrize("change", [
    "inventory_hash", "grounding_hash", "rows", "duplicate_rows", "unknown_review",
    "audit_rows", "missing_reference", "secondary_accession",
])
def test_drift_is_rejected_instead_of_producing_partial_success(inputs, change):
    inventory, grounding, historical, rows, reviews = copy.deepcopy(inputs)
    old, refs = json.loads(historical), json.loads(grounding)
    if change == "inventory_hash":
        old["source_inventory_sha256"] = "0" * 64
    elif change == "grounding_hash":
        old["grounding_sha256"] = "0" * 64
    elif change == "rows":
        rows.pop()
    elif change == "duplicate_rows":
        rows.append(rows[0])
    elif change == "unknown_review":
        reviews["unknown"] = {}
    elif change == "audit_rows":
        old["rows"][0]["source"]["gene_id"] = "OTHER"
    else:
        if change == "missing_reference":
            refs["entries"].clear()
        else:
            refs["entries"]["P12345"]["primaryAccession"] = "P67890"
        grounding = json.dumps(refs).encode()
        old["grounding_sha256"] = audit.digest(grounding)
    historical = json.dumps(old).encode()
    with pytest.raises(ValueError):
        audit.build_report(inventory, grounding, historical, rows, reviews)


def test_no_match_is_not_gene_absence(inputs):
    inventory, grounding, historical, rows, reviews = inputs
    refs, old = json.loads(grounding), json.loads(historical)
    refs["entries"]["P12345"]["genes"] = []
    refs["entries"]["P12345"]["uniProtKBCrossReferences"] = []
    grounding = json.dumps(refs).encode()
    old["grounding_sha256"] = audit.digest(grounding)
    report = audit.build_report(inventory, grounding, json.dumps(old).encode(), rows, reviews)
    assert report["summary"]["unmatched_source_values"] == 3
    assert report["summary"]["experimental_identifiers_assigned"] == 0


def test_existing_output_cannot_be_overwritten(tmp_path, monkeypatch):
    path = tmp_path / "existing.json"
    path.write_text("keep")
    monkeypatch.setattr(sys, "argv", ["audit", "--grounding", "missing", "--historical-audit", "missing",
                                    "--output", str(path)])
    with pytest.raises(SystemExit, match="2"):
        audit.main()
    assert path.read_text() == "keep"


def test_dated_export_replays_from_metadata_without_private_cache_or_live_records():
    root = Path(__file__).resolve().parents[1]
    saved = json.loads((root / "research/2026-10-13-phibase-gene-id-types.json").read_bytes())
    assert saved["scope"] == audit.SCOPE
    assert len(saved["rows"]) == 95
    assert len({r["source_row_sha256"] for r in saved["rows"]}) == 95
    assert len(saved["reference_entries"]) == 23
    assert saved["summary"]["source_rows"] == 217
    assert saved["summary"]["empty_source_gene_ids"] == 122
    for row in saved["rows"]:
        hits = audit.identifier_matches(
            row["source_gene_id"], saved["reference_entries"][row["reference_accession"]])
        assert hits == row["matches"]
        assert audit.match_summary(row["source_gene_id"], hits) == row["match_summary"]
    assert sum(bool(r["match_summary"]["gene_annotation_fields"]) for r in saved["rows"]) == 6
    assert sum("ProteinId" in r["match_summary"]["typed_cross_reference_properties"]
               for r in saved["rows"]) == 8
    assert sum(all(h["kind"] == "CROSS_REFERENCE_PRIMARY_ID" for h in r["matches"])
               for r in saved["rows"]) == 81
    rejected, = [r for r in saved["rows"] if r["current_review"]["source_gene_id_rejected"]]
    assert rejected["source_gene_id"] == "YIR011C_mRNA"
    assert not rejected["match_summary"]["experimental_identity_verified"]


def test_conference_dossier_does_not_complete_journal_or_experimental_review():
    root = Path(__file__).resolve().parents[1]
    dossier = json.loads((root / "research/2026-10-13-carboxin-bcpc-context.json").read_bytes())
    assert dossier["record"]["identifier"] == "CHEBI:3405"
    assert dossier["primary"]["printed_pages"] == list(range(221, 227))
    assert dossier["primary"]["pdf_pages_one_based"] == list(range(58, 64))
    assert len(dossier["primary"]["native_pages_inspected"]) == 6
    assert dossier["primary"]["conference_paper_review_complete"]
    assert not dossier["primary"]["journal_article_review_complete"]
    assert not dossier["primary"]["journal_citation"]["subject_crosswalk_resolved"]
    assert not dossier["reference"]["experimental_allele_or_subject_assigned"]
    assert not dossier["reference"]["identifier_types"]["version_suffix_removed"]
    assert not dossier["taxonomy"]["strain_or_genome_assigned"]
    assert dossier["disposition"]["status"] == "PENDING_JOURNAL_AND_EXPERIMENTAL_SUBJECT_REVIEW"
    assert dossier["disposition"]["new_biological_claims"] == 0
    assert dossier["disposition"]["source_owned_reviews_changed"] == 0
    assert dossier["disposition"]["whole_record_reviews_completed"] == 0
    audit_pin = dossier["reference"]["identifier_types"]["typed_audit"]
    assert audit.digest((root / audit_pin["path"]).read_bytes()) == audit_pin["sha256"]
