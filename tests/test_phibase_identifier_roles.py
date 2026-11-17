"""Documented database roles must not become experimental gene assignments."""

import copy
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_phibase_identifier_roles as roles  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "research/2026-10-13-phibase-gene-id-types.json"
DOCS = ROOT / "research/2026-10-13-uniprot-ensemblfungi-fields.json"


def test_roles_are_database_and_field_specific_not_name_inferences():
    hits = [
        {"kind": "GENE_ANNOTATION_FIELD", "field": "orfNames", "value": "transcript-looking"},
        {"kind": "CROSS_REFERENCE_PRIMARY_ID", "database": "Other", "field": "id"},
        {"kind": "CROSS_REFERENCE_PRIMARY_ID", "database": "ensemblfungi", "field": "id"},
        {"kind": "CROSS_REFERENCE_PRIMARY_ID", "database": "EnsemblFungi", "field": "id"},
        {"kind": "TYPED_CROSS_REFERENCE_PROPERTY", "database": "EnsemblFungi", "field": "ProteinId"},
        {"kind": "TYPED_CROSS_REFERENCE_PROPERTY", "database": "EnsemblFungi", "field": "GeneId"},
    ]
    assert roles.roles_for_matches(hits) == [
        {"match_index": 3, "field": "id", "role": "TRANSCRIPT"},
        {"match_index": 4, "field": "ProteinId", "role": "PROTEIN"},
        {"match_index": 5, "field": "GeneId", "role": "GENE"},
    ]


def test_documented_report_preserves_overlap_rejections_and_missing_values():
    audit = json.loads(AUDIT.read_bytes())
    before = copy.deepcopy(audit)
    result = roles.build_report(audit, json.loads(DOCS.read_bytes()))
    assert result["summary"] == {
        "source_rows": 217, "nonempty_source_gene_ids": 95, "empty_source_gene_ids": 122,
        "documented_role_counts": {"TRANSCRIPT": 95, "PROTEIN": 8},
        "multiple_documented_roles": 8, "no_documented_role": 0,
        "rejected_source_gene_ids_preserved": 1, "experimental_identifiers_assigned": 0,
    }
    rejected, = [r for r in result["rows"] if r["current_review"]["source_gene_id_rejected"]]
    assert rejected["documented_roles"] == ["TRANSCRIPT"]
    assert rejected["current_review"]["source_gene_id_withheld"]
    assert all(not r["experimental_identity_verified"] for r in result["rows"])
    assert sum(bool(r["gene_annotation_fields"]) for r in result["rows"]) == 6
    assert audit == before
    for old, new in zip(audit["rows"], result["rows"], strict=True):
        for evidence in new["field_role_evidence"]:
            hit = old["matches"][evidence["match_index"]]
            assert hit["field"] == evidence["field"]
            assert hit["database"] == "EnsemblFungi"


@pytest.mark.parametrize("change", [
    "scope", "version", "count", "empty_count", "duplicate", "missing_value",
    "hits", "summary", "accession", "database", "rules",
])
def test_inconsistent_inputs_are_rejected(change):
    audit, docs = json.loads(AUDIT.read_bytes()), json.loads(DOCS.read_bytes())
    if change == "scope":
        audit["scope"] = "OTHER"
    elif change == "version":
        audit["schema_version"] = 2
    elif change == "count":
        audit["summary"]["nonempty_source_gene_ids"] += 1
    elif change == "empty_count":
        audit["summary"]["empty_source_gene_ids"] += 1
    elif change == "duplicate":
        audit["rows"][1] = audit["rows"][0]
    elif change == "missing_value":
        audit["rows"][0]["source_gene_id"] = ""
    elif change == "hits":
        audit["rows"][0]["matches"] = []
    elif change == "summary":
        audit["rows"][0]["match_summary"]["experimental_identity_verified"] = True
    elif change == "accession":
        accession = audit["rows"][0]["reference_accession"]
        audit["reference_entries"][accession]["accession"] = "OTHER"
    elif change == "database":
        docs["database"] = "Other"
    else:
        docs["field_roles"]["id"] = "GENE"
    with pytest.raises(ValueError):
        roles.build_report(audit, docs)


def test_output_is_exclusive(tmp_path, monkeypatch):
    path = tmp_path / "existing.json"
    path.write_text("keep")
    monkeypatch.setattr(sys, "argv", ["audit", "--audit", "missing", "--documentation", "missing",
                                     "--output", str(path)])
    with pytest.raises(SystemExit, match="2"):
        roles.main()
    assert path.read_text() == "keep"


def test_saved_report_replays_without_private_cache_or_live_corpus():
    path = ROOT / "research/2026-10-13-phibase-identifier-roles.json"
    saved = json.loads(path.read_bytes())
    regenerated = roles.build_report(json.loads(AUDIT.read_bytes()), json.loads(DOCS.read_bytes()))
    assert {k: v for k, v in saved.items() if k != "inputs"} == regenerated
    for pin in saved["inputs"].values():
        assert roles.digest((ROOT / pin["path"]).read_bytes()) == pin["sha256"]
