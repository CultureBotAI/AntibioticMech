"""Rendered scientific tables keep their data inside named keyboard scroll regions."""
import sys
from html.parser import HTMLParser
from pathlib import Path

import pytest
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from render_pages import TEMPLATES_DIR, build_record  # noqa: E402


class Tables(HTMLParser):
    def __init__(self, content):
        super().__init__()
        self.divs = []
        self.tables = []
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "div":
            self.divs.append(attrs)
        elif tag == "table":
            self.tables.append(next((d for d in reversed(self.divs)
                                     if d.get("role") == "region"), None))

    def handle_endtag(self, tag):
        if tag == "div":
            self.divs.pop()


@pytest.mark.parametrize("view", ["class", "record"])
def test_rendered_tables_have_named_keyboard_scroll_regions(view):
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR),
                      autoescape=select_autoescape(["html"]))
    if view == "record":
        path = ROOT / "data/antibiotics/antibacterial/ampicillin.yaml"
        doc = yaml.safe_load(path.read_text())
        context = {"r": build_record(path, doc, {}, "../"), "root": "../", "stats": {}}
    else:
        context = {
            "label": 'Test <compound> "table"', "total": 1, "slug": "antibacterial",
            "index_url": "../data/class-antibacterial.json", "root": "../", "stats": {},
            "records": [{"label": "Ampicillin", "slug": "ampicillin", "sources": ["ChEBI"],
                         "status": "REVIEWED", "grounding": "EXACT", "structural_class": "penam"}],
        }
    content = env.get_template(view + ".html").render(**context)
    tables = Tables(content).tables
    assert len(tables) >= (7 if view == "record" else 1)
    for region in tables:
        assert region is not None, "Table overflows the page instead of a named region"
        assert region.get("tabindex") == "0"
        assert region.get("aria-label")
        assert "table-scroll" in region.get("class", "").split()
    assert "Ampicillin" in content or "ampicillin" in content
    assert '<th scope="col">' in content
    assert "<caption>" in content
    if view == "class":
        assert tables[0]["aria-label"] == 'Test <compound> "table" compounds'
        assert '<script' not in tables[0]["aria-label"]
