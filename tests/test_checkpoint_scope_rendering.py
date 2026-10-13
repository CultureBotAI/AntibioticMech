"""Reference-only caveats must survive both stages of the published renderer."""

import json
from html.parser import HTMLParser
from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape

from antibioticmech.activity_collections import load_record
from scripts.render_pages import TEMPLATES_DIR, build_record

ROOT = Path(__file__).resolve().parents[1]


class PageText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.excluded = None

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.excluded = tag

    def handle_endtag(self, tag):
        if tag == self.excluded:
            self.excluded = None

    def handle_data(self, data):
        if self.excluded is None:
            self.parts.append(data)


@pytest.mark.parametrize("checkpoint", ["bcr", "sulfathiazole", "cycloheximide"])
def test_checkpoint_reference_scope_survives_record_adapter_and_template(checkpoint):
    receipt = json.loads((ROOT / f"research/2026-10-13-{checkpoint}-curation.json").read_bytes())
    doc = load_record(ROOT / receipt["fixture"]["path"])
    if checkpoint == "bcr":
        target, = [t for t in doc["molecular_targets"] if t.get("source") == "PRIMARY_LITERATURE"]
        target.update(receipt["added_target_taxon"])
        target["protein_examples"] = [receipt["protein_example"]]
        target["evidence"].append(receipt["added_evidence"])
        caveats = [receipt["added_evidence"]["notes"]]
        accessions = [receipt["protein_example"]["uniprot_id"]]
    else:
        doc.setdefault("resistance_mechanisms", []).extend(receipt["claims"])
        caveats = [c["note"] for c in receipt["claims"]]
        caveats.extend(c["evidence"][1]["notes"] for c in receipt["claims"])
        accessions = [c["evidence"][1]["reference"] for c in receipt["claims"]]

    # The live path is adapter metadata only; the record comes from a dated fixture.
    record = build_record(ROOT / receipt["record"]["path"], doc, {}, "../")
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR),
                      autoescape=select_autoescape(["html", "xml"]))
    html = env.get_template("record.html").render(r=record, root="../", stats={})
    page = PageText()
    page.feed(html)
    text = " ".join(" ".join(page.parts).split())
    for caveat in caveats:
        assert " ".join(caveat.split()) in text, f"Missing rendered scope caveat: {checkpoint}"
    assert all(accession in text for accession in accessions)
