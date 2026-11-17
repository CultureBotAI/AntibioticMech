"""Regressions for published-site issue reports #1051–#1065."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import render_pages as site  # noqa: E402


def environment():
    return Environment(loader=FileSystemLoader(site.TEMPLATES_DIR),
                       autoescape=select_autoescape(["html"]))


def test_classification_uses_snapshot_labels_and_an_explicit_unknown_fallback():
    role = site.resolve_curie("CHEBI:33282", {}, "../")
    parent = site.resolve_curie("ARO:0000016", {}, "../")
    unknown = site.resolve_curie("CHEBI:999999999", {}, "../")
    macro = environment().get_template("macros.html").module.labeled_term
    assert role["label"] == "antibacterial agent"
    assert parent["label"] == "aminoglycoside antibiotic"
    for term in (role, parent, unknown):
        html = str(macro(term))
        assert html.count(f'>{term["id"]}<') == 1
    assert "Label unavailable" in str(macro(unknown))


def test_supported_sources_link_and_unsafe_or_unresolved_values_stay_text():
    link = environment().get_template("macros.html").module.reference_link
    cases = [
        ("PMID:123", "", "https://pubmed.ncbi.nlm.nih.gov/123"),
        ("doi:10.1000/example", "", "https://doi.org/10.1000/example"),
        ("NCBITaxon:562", "", "wwwtax.cgi?id=562"),
        ("BGC0000115", "MIBiG", "/go/BGC0000115"),
        ("GO:0008150", "", "/GO:0008150"),
        ("SAMN123", "BioSample", "/biosample/SAMN123"),
    ]
    for value, namespace, destination in cases:
        assert destination in str(link(value, namespace))
    assert "<a " not in str(link("javascript:alert(1)"))
    assert "<a " not in str(link("unknown:123"))
    assert "&lt;script&gt;" in str(link("<script>"))


def test_activity_inline_evidence_and_taxa_are_navigable():
    table = environment().get_template("activity_table.html").module.activity_table
    html = str(table([{"taxon_label": "Escherichia coli", "taxon_id": "NCBITaxon:562",
                       "evidence": [{"reference": "PMID:123", "snippet": "<raw>"}]}]))
    assert 'wwwtax.cgi?id=562' in html
    assert 'href="https://pubmed.ncbi.nlm.nih.gov/123"' in html
    assert "&lt;raw&gt;" in html


def test_dynamic_evidence_and_membership_resolvers_are_safe():
    script = site.TEMPLATES_DIR / "activity_browser.js"
    program = f"""
      const {{referenceURL}} = require({json.dumps(str(script))});
      const assert = require('node:assert/strict');
      assert.equal(referenceURL('SRR123', 'run_accession'), 'https://www.ncbi.nlm.nih.gov/sra/?term=SRR123');
      assert.equal(referenceURL('PRJEB123', 'bioproject_accession'), 'https://www.ncbi.nlm.nih.gov/bioproject/PRJEB123');
      assert.equal(referenceURL('SAMN123', 'biosample_accession'), 'https://www.ncbi.nlm.nih.gov/biosample/SAMN123');
      assert.equal(referenceURL('PMID:123', 'reference'), 'https://pubmed.ncbi.nlm.nih.gov/123');
      assert.equal(referenceURL('javascript:alert(1)', 'reference'), null);
      assert.equal(referenceURL('<script>', 'snippet'), null);
    """
    subprocess.run(["node", "-e", program], check=True)


def test_not_found_uses_absolute_site_navigation_for_unknown_nested_routes():
    html = environment().get_template("not_found.html").render(root=site.SITE_BASE, stats={})
    assert f'href="{site.SITE_BASE}index.html"' in html
    assert f'href="{site.SITE_BASE}browse.html"' in html


def test_map_has_one_main_landmark_and_reachable_search_pagination():
    html = environment().get_template("chemical_map.html").render(
        root="", stats={"total": 25}, quality={"trustworthiness_at_10": .9,
        "neighbor_overlap_at_10": .8}, model_version="fixture")
    assert html.count("<main") == 1
    assert 'id="map-show-more"' in html
    assert 'id="map-search-count"' in html


def test_landing_explains_workflow_status_without_asserting_human_review():
    html = environment().get_template("index.html").render(
        stats={"total": 10, "seeded": 8, "reviewed": 2, "seeded_pct": 80},
        classes=[], groundings=[], mechanism=[], root="")
    assert "have had no human review" not in html
    assert "do not establish human review" in html
    assert "agent-assisted" in html
    assert "by antimicrobial class" in html
