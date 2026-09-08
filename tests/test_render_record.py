from __future__ import annotations

import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from render_pages import TEMPLATES_DIR  # noqa: E402


def test_record_page_renders_source_concept_evidence():
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(["html", "xml"]),
    )

    html = env.get_template("record.html").render(
        r={
            "identifier": "antibioticmech:curator-widget",
            "label": "widgetmycin",
            "class_slug": "antibacterial",
            "antimicrobial_class": "ANTIBACTERIAL",
            "grounding_status": "MINTED",
            "curation_status": "PROPOSED",
            "source_concepts": [{
                "source": "CURATOR",
                "source_id": "DOI:10.1000/widget#compound-1",
                "source_label": "widgetmycin",
                "minted_identifier": "antibioticmech:curator-widget",
                "source_version": "2026-09-07",
                "evidence": [{
                    "reference": "DOI:10.1000/widget",
                    "snippet": "Compound 1 inhibited Bacillus subtilis.",
                    "notes": "Table 1 reports the exact structure and activity.",
                }],
            }],
        },
        root="../",
        stats={},
    )

    assert '<th scope="col">Evidence</th>' in html
    assert "DOI:10.1000/widget" in html
    assert "Compound 1 inhibited Bacillus subtilis." in html
