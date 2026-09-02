"""Curated synonym exclusions prevent cross-isomer identity assertions."""

from __future__ import annotations


def test_oleic_acid_does_not_claim_the_trans_isomer_as_a_synonym(records):
    by_id = {record["identifier"]: record for _path, record in records}
    oleic = by_id["CHEBI:16196"]
    names = {item["synonym_text"] for item in oleic.get("synonyms") or []}
    assert "Elaidoic acid" not in names
    assert "Oleate" in names


def test_synonym_exclusion_is_scoped_to_the_offending_source_record(repo_root):
    import yaml

    conf = yaml.safe_load((repo_root / "conf" / "sources.yaml").read_text(encoding="utf-8"))
    exclusions = conf["synonym_exclusions"]
    assert exclusions == {"ARO:3003958": ["Elaidoic acid"]}
