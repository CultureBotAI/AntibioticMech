"""Claim assessments are typed, backward-compatible and never defaulted."""

from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "src/antibioticmech/schema/antibioticmech.yaml"
CLASSES = ["EvidenceItem"]
SUPPORT = {"SUPPORT", "REFUTE", "PARTIAL", "NO_EVIDENCE", "WRONG_STATEMENT"}
SOURCES = {
    "FIELD_STUDY",
    "MESOCOSM",
    "LABORATORY",
    "IN_VITRO",
    "IN_VIVO",
    "COMPUTATIONAL",
    "META_ANALYSIS",
    "REVIEW",
    "REMOTE_SENSING",
    "LONG_TERM_MONITORING",
    "EXPERT_OPINION",
    "DATABASE",
    "OTHER",
}
REQUIRED = {"EvidenceItem": {"supports": False, "evidence_source": False}}


@pytest.fixture(scope="module")
def assessment_view():
    return SchemaView(str(SCHEMA))


@pytest.fixture(scope="module")
def assessment_validator():
    return Validator(str(SCHEMA), validation_plugins=[JsonschemaValidationPlugin(closed=True)])


def baseline(view, cls):
    values = {
        "reference": "PMID:12345678",
        "snippet": "A verbatim test fixture passage.",
        "explanation": "Fixture assessment, not a curated scientific assertion.",
        "source": "fixture",
        "supports": "SUPPORT",
        "evidence_source": "IN_VITRO",
    }
    result = {}
    for slot in view.class_induced_slots(cls):
        if slot.required:
            if slot.name in values:
                result[slot.name] = values[slot.name]
            elif slot.range in view.all_enums():
                result[slot.name] = next(iter(view.get_enum(slot.range).permissible_values))
            else:
                raise AssertionError(f"Add an explicit fixture for {cls}.{slot.name}")
    return result


@pytest.mark.parametrize("cls", CLASSES)
def test_assessments_preserve_legacy_requiredness_and_have_no_default(
    assessment_view, assessment_validator, cls
):
    for name in ("supports", "evidence_source"):
        slot = assessment_view.induced_slot(name, cls)
        assert bool(slot.required) == REQUIRED[cls][name]
        assert slot.ifabsent is None
        expected = SUPPORT if name == "supports" else SOURCES
        assert set(assessment_view.get_enum(slot.range).permissible_values) == expected
    old = baseline(assessment_view, cls)
    assert not list(assessment_validator.iter_results(old, target_class=cls))


@pytest.mark.parametrize("cls", CLASSES)
@pytest.mark.parametrize("support", sorted(SUPPORT))
def test_all_support_assessments_validate(assessment_view, assessment_validator, cls, support):
    data = {**baseline(assessment_view, cls), "supports": support, "evidence_source": "DATABASE"}
    assert not list(assessment_validator.iter_results(data, target_class=cls))


@pytest.mark.parametrize("cls", CLASSES)
@pytest.mark.parametrize("source", sorted(SOURCES))
def test_study_types_validate_without_changing_support(assessment_view, assessment_validator, cls, source):
    data = {**baseline(assessment_view, cls), "supports": "REFUTE", "evidence_source": source}
    assert not list(assessment_validator.iter_results(data, target_class=cls))
    assert data["supports"] == "REFUTE"


@pytest.mark.parametrize("cls", CLASSES)
@pytest.mark.parametrize(
    "field,value",
    [
        ("supports", "HIGH_CONFIDENCE"),
        ("supports", "support"),
        ("evidence_source", "abstract"),
        ("evidence_source", "LLM_ASSISTED"),
        ("evidence_source", "PMID:123"),
    ],
)
def test_rejects_conflating_assessment_source_and_curation(
    assessment_view, assessment_validator, cls, field, value
):
    valid = {**baseline(assessment_view, cls), "supports": "PARTIAL", "evidence_source": "LABORATORY"}
    assert not list(assessment_validator.iter_results(valid, target_class=cls))  # positive control
    invalid = {**valid, field: value}
    assert list(assessment_validator.iter_results(invalid, target_class=cls))


@pytest.mark.parametrize("cls", CLASSES)
def test_unknown_fields_still_fail_closed_validation(assessment_view, assessment_validator, cls):
    data = {**baseline(assessment_view, cls), "invented_evidence_field": "not allowed"}
    assert list(assessment_validator.iter_results(data, target_class=cls))


def test_shared_reference_location_keeps_its_legacy_meaning(assessment_validator):
    data = {"reference": "PMID:12345678", "supports": "PARTIAL", "evidence_source": "abstract"}
    assert not list(assessment_validator.iter_results(data, target_class="SupportingReference"))


def test_causal_edge_spec_preserves_and_validates_optional_assessments():
    from jinja2 import Environment, FileSystemLoader

    from antibioticmech.causal_graphs_curation import (
        ALLOWED_EVIDENCE_SOURCES,
        ALLOWED_SUPPORT_LEVELS,
        EVIDENCE_ITEM_KEYS,
        validate_causal_edge_spec,
    )

    expected_keys = {
        "reference",
        "snippet",
        "notes",
        "supports",
        "evidence_source",
    }
    assert expected_keys == EVIDENCE_ITEM_KEYS
    assert ALLOWED_SUPPORT_LEVELS == SUPPORT
    assert ALLOWED_EVIDENCE_SOURCES == SOURCES

    base_edge = {
        "subject": "n1",
        "predicate": "inhibits",
        "predicate_id": "RO:0002408",
        "object": "n2",
        "description": "Direct enzymatic inhibition.",
        "evidence": [
            {
                "reference": "PMID:12345678",
                "snippet": "Verbatim passage.",
            }
        ],
    }
    norm_plain = validate_causal_edge_spec(
        base_edge, node_ids={"n1", "n2"}, context="test"
    )
    assert norm_plain["evidence"] == [
        {"reference": "PMID:12345678", "snippet": "Verbatim passage."}
    ]

    assessed_edge = {
        **base_edge,
        "evidence": [
            {
                "reference": "PMID:12345678",
                "supports": "SUPPORT",
                "evidence_source": "IN_VITRO",
                "snippet": "Verbatim passage.",
                "notes": "Purified enzyme assay.",
            }
        ],
    }
    norm_assessed = validate_causal_edge_spec(
        assessed_edge, node_ids={"n1", "n2"}, context="test"
    )
    assert norm_assessed["evidence"] == [
        {
            "reference": "PMID:12345678",
            "supports": "SUPPORT",
            "evidence_source": "IN_VITRO",
            "snippet": "Verbatim passage.",
            "notes": "Purified enzyme assay.",
        }
    ]

    for bad_field, bad_val in (
        ("supports", "HIGH_CONFIDENCE"),
        ("supports", ""),
        ("evidence_source", "abstract"),
        ("evidence_source", ""),
    ):
        bad_edge = {
            **base_edge,
            "evidence": [
                {
                    "reference": "PMID:12345678",
                    "snippet": "Verbatim passage.",
                    bad_field: bad_val,
                }
            ],
        }
        with pytest.raises(ValueError, match=f"invalid {bad_field}"):
            validate_causal_edge_spec(bad_edge, node_ids={"n1", "n2"}, context="test")

    env = Environment(
        loader=FileSystemLoader(str(ROOT / "src/antibioticmech/templates")),
        autoescape=True,
    )
    tmpl = env.from_string(
        '{% from "macros.html" import evidence_list %}{{ evidence_list(items) }}'
    )
    plain_html = tmpl.render(items=norm_plain["evidence"])
    expected_href = "https://pubmed.ncbi.nlm.nih.gov/12345678"
    assert (
        plain_html.strip()
        == '<ul class="plain evidence">\n'
        "  \n"
        f'  <li><span class="meta"><a href="{expected_href}">PMID:12345678</a></span>'
        " — &#34;Verbatim passage.&#34;</li>\n"
        "  \n"
        "</ul>"
    )
    assessed_html = tmpl.render(items=norm_assessed["evidence"])
    assert "[SUPPORT]" in assessed_html
    assert "[IN_VITRO]" in assessed_html

