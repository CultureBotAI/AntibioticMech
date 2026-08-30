"""Schema-level checks: it loads, and the corpus only uses values it declares."""

from __future__ import annotations

import hashlib

from linkml_runtime.utils.schemaview import SchemaView


def _schema(schema_path):
    return SchemaView(str(schema_path))


def test_schema_loads_with_its_imports(schema_path):
    view = _schema(schema_path)
    assert "AntibioticRecord" in view.all_classes()
    # The vendored mech_shared module must resolve, or Discussion/Dataset
    # silently disappear from the record shape.
    assert "Discussion" in view.all_classes()
    assert "Dataset" in view.all_classes()


def test_antibiotic_record_is_the_only_tree_root(schema_path):
    view = _schema(schema_path)
    roots = [name for name, cls in view.all_classes().items() if cls.tree_root]
    assert roots == ["AntibioticRecord"]


def test_mech_shared_is_vendored_byte_identical(repo_root):
    """The shared module is vendored across the Mech repos and must not be
    edited in one place. Its own docstring says so; this makes it checkable here
    by pinning the sha of the copy we shipped."""
    path = repo_root / "src" / "antibioticmech" / "schema" / "mech_shared.yaml"
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    expected = "1a5e21eb2ee9f3584ff6af3a6906b1d442e18c41de405b1bf907c20f44eafa2a"
    assert digest == expected, (
        "mech_shared.yaml has been edited locally. It is vendored byte-identical "
        "across the Mech repos — change it once upstream and re-vendor everywhere, "
        "then update this pin."
    )


def _permissible(view, enum_name: str) -> set[str]:
    return set(view.get_enum(enum_name).permissible_values)


def test_corpus_uses_only_declared_enum_values(schema_path, records):
    """Per-record validation already enforces this for records written through
    the gate. This catches a hand-edited value across the whole corpus at once."""
    view = _schema(schema_path)
    checks = [
        ("antimicrobial_class", "AntimicrobialClassEnum", lambda r: [r.get("antimicrobial_class")]),
        ("curation_status", "CurationStatusEnum", lambda r: [r.get("curation_status")]),
        ("grounding_status", "GroundingStatusEnum", lambda r: [r.get("grounding_status")]),
        ("mode_of_action", "ModeOfActionEnum", lambda r: [r.get("mode_of_action")]),
        ("cidality", "CidalityEnum", lambda r: [r.get("cidality")]),
        ("clinical_status", "ClinicalStatusEnum", lambda r: [r.get("clinical_status")]),
        ("biosynthesis_origin", "BiosynthesisOriginEnum", lambda r: [r.get("biosynthesis_origin")]),
        ("resistance_mechanisms.mechanism_type", "ResistanceMechanismEnum",
         lambda r: [m.get("mechanism_type") for m in r.get("resistance_mechanisms") or []]),
        ("source_concepts.source", "SourceEnum",
         lambda r: [c.get("source") for c in r.get("source_concepts") or []]),
        ("synonyms.synonym_type", "SynonymTypeEnum",
         lambda r: [s.get("synonym_type") for s in r.get("synonyms") or []]),
    ]
    problems = []
    for field, enum_name, extract in checks:
        allowed = _permissible(view, enum_name)
        for path, record in records:
            for value in extract(record):
                if value is not None and value not in allowed:
                    problems.append(f"{path.name}: {field}={value!r}")
    assert not problems, problems[:20]
