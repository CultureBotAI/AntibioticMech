"""Semantic input contracts run without a model or a complete corpus."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest
import yaml

from antibioticmech import text_map_inputs as adapter


def write_record(root: Path, name: str, **extra) -> Path:
    path = root / "data" / adapter.CORPUS / "example" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {"identifier": "ENVO:1", "label": "Test entity", adapter.CATEGORY_FIELD: "OTHER"}
    record.update(extra)
    path.write_text(yaml.safe_dump(record), encoding="utf-8")
    return path


def test_jsonl_contract_and_no_input_mutation(tmp_path):
    path = write_record(tmp_path, "one.yaml")
    before = path.read_bytes()
    preview = adapter.export_inputs(tmp_path, None)
    output = tmp_path / "inputs.jsonl"
    exported = adapter.export_inputs(tmp_path, output)
    row = json.loads(output.read_text())
    assert set(row) == {
        "identifier",
        "label",
        "category",
        "page",
        "source_path",
        "text",
        "text_sha256",
        "adapter_version",
    }
    assert row["text"]
    assert row["text_sha256"] == hashlib.sha256(row["text"].encode()).hexdigest()
    assert row["source_path"] == path.relative_to(tmp_path).as_posix()
    assert preview["scope"] == exported["scope"] == "full"
    assert preview["records"] == exported["records"] == 1
    assert preview["jsonl_sha256"] == exported["jsonl_sha256"]
    assert path.read_bytes() == before


def test_duplicate_identifier_refuses_partial_output(tmp_path):
    write_record(tmp_path, "a.yaml")
    write_record(tmp_path, "b.yaml")
    output = tmp_path / "inputs.jsonl"
    output.write_text("preserve me\n")
    with pytest.raises(ValueError, match="duplicate record identifier"):
        adapter.export_inputs(tmp_path, output)
    assert output.read_text() == "preserve me\n"
    assert not list(tmp_path.glob(".text-map-*"))


def test_selecting_path_outside_corpus_is_refused(tmp_path):
    write_record(tmp_path, "a.yaml")
    elsewhere = tmp_path / "elsewhere.yaml"
    elsewhere.write_text("identifier: ENVO:1\nlabel: elsewhere\n")
    with pytest.raises(ValueError, match="leaves the corpus"):
        list(adapter.iter_inputs(tmp_path, records=["elsewhere.yaml"]))


def test_symlink_records_are_refused(tmp_path):
    real = write_record(tmp_path, "a.yaml")
    (real.parent / "linked.yaml").symlink_to(real)
    with pytest.raises(ValueError, match="symlink"):
        list(adapter.iter_inputs(tmp_path))


def test_subset_is_explicit_and_order_is_stable(tmp_path):
    first = write_record(tmp_path, "a.yaml")
    write_record(tmp_path, "z.yaml", identifier="ENVO:2")
    output = tmp_path / "canary.jsonl"
    receipt = adapter.export_inputs(tmp_path, output, limit=1)
    assert receipt["scope"] == "subset"
    assert receipt["records"] == 1
    assert json.loads(output.read_text())["source_path"] == first.relative_to(tmp_path).as_posix()
    assert (
        adapter.export_inputs(tmp_path, None, records=[first.relative_to(tmp_path).as_posix()])["scope"]
        == "subset"
    )


def test_output_suffix_and_invalid_limit_are_refused(tmp_path):
    source = write_record(tmp_path, "a.yaml")
    with pytest.raises(ValueError, match=".jsonl"):
        adapter.export_inputs(tmp_path, source)
    with pytest.raises(ValueError, match="positive"):
        adapter.export_inputs(tmp_path, None, limit=0)


def test_nonsemantic_history_edits_do_not_change_text_but_definition_edits_do(tmp_path):
    path = write_record(tmp_path, "a.yaml", definition="Original biological definition.")
    before = list(adapter.iter_inputs(tmp_path))[0]
    record = yaml.safe_load(path.read_text())
    record["curation_history"] = [{"changes": "PRIVATE PROCESS SENTINEL"}]
    record["curation_status"] = "PROCESS SENTINEL"
    path.write_text(yaml.safe_dump(record))
    history_only = list(adapter.iter_inputs(tmp_path))[0]
    assert history_only["text_sha256"] == before["text_sha256"]
    assert "SENTINEL" not in history_only["text"]
    record["definition"] = "A new biological meaning."
    path.write_text(yaml.safe_dump(record))
    assert list(adapter.iter_inputs(tmp_path))[0]["text_sha256"] != before["text_sha256"]


def test_full_and_selected_record_documents_match(tmp_path):
    first = write_record(tmp_path, "a.yaml")
    write_record(tmp_path, "z.yaml", identifier="ENVO:2")
    full = list(adapter.iter_inputs(tmp_path))
    chosen = list(adapter.iter_inputs(tmp_path, records=[first.relative_to(tmp_path).as_posix()]))
    assert chosen == full[:1]


def test_cli_canary_is_explicit_and_empty_corpus_refuses(tmp_path, capsys):
    write_record(tmp_path, "a.yaml")
    assert adapter.main(["--root", str(tmp_path), "--limit", "1"]) == 0
    receipt = json.loads(capsys.readouterr().out)
    assert receipt["mode"] == "preview" and receipt["scope"] == "subset"
    assert receipt["records"] == 1
    for path in (tmp_path / "data" / adapter.CORPUS).rglob("*.yaml"):
        path.unlink()
    with pytest.raises(ValueError, match="no corpus records"):
        adapter.export_inputs(tmp_path, None)


def test_duplicate_selected_paths_and_missing_record_fail(tmp_path):
    path = write_record(tmp_path, "a.yaml").relative_to(tmp_path).as_posix()
    with pytest.raises(ValueError, match="duplicate selected path"):
        list(adapter.iter_inputs(tmp_path, records=[path, path]))
    with pytest.raises(ValueError, match="not a corpus YAML"):
        list(adapter.iter_inputs(tmp_path, records=[path.replace("a.yaml", "missing.yaml")]))


def test_exact_existing_antibiotic_text_keeps_roles_and_excludes_structure(tmp_path):
    context_dir = tmp_path / "data" / "raw"
    context_dir.mkdir(parents=True)
    (context_dir / "chebi_role_names.tsv").write_text("role_id\tname\nCHEBI:1\tprotein inhibitor\n")
    record = {
        "identifier": "CHEBI:2",
        "label": "widgetmycin",
        "antimicrobial_class": "ANTIBACTERIAL",
        "definition": "An antimicrobial.",
        "activity_roles": ["CHEBI:1"],
        "producer_organisms": [{"taxon_label": "Streptomyces example", "strain": "EXCLUDED_STRAIN"}],
        "chemical_structure": {"smiles": "EXCLUDED_SMILES"},
        "mode_of_action_notes": "EXCLUDED_NOTES",
    }
    context = adapter.build_context(tmp_path)
    text = adapter.semantic_text(record, context)
    assert text == context["builder"](record, context["names"])
    assert "widgetmycin" in text and "Streptomyces example" in text
    assert "EXCLUDED" not in text
    assert adapter.page_target(record, "data/antibiotics/antibacterial/special-slug.yaml") == (
        "antibacterial/special-slug.html"
    )
