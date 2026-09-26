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


def test_record_page_renders_activity_sample_accessions():
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
            "source_concepts": [],
            "activity_spectrum": [{
                "taxon_label": "Escherichia coli",
                "taxon_id": "NCBITaxon:562",
                "activity": "RESISTANT",
                "mic_value": 32.0,
                "mic_qualifier": ">",
                "mic_units": "mg/L",
                "disk_diffusion_value": 18.0,
                "disk_diffusion_qualifier": ">=",
                "disk_diffusion_units": "mm",
                "assay": "broth microdilution",
                "strain": "AR-0001",
                "biosample_accession": "SAMN11953777",
                "bioproject_accession": "PRJNA123456",
                "assembly_accession": "GCF_000005845.2",
                "sra_accessions": ["SRR123456"],
            }, {
                "taxon_label": "Staphylococcus aureus",
                "activity": "SUSCEPTIBLE",
                "mic_value": 1.0,
                "mic_units": "mg/L",
                "assay": "broth microdilution",
            }, {
                "taxon_label": "Pseudomonas aeruginosa",
                "activity": "RESISTANT",
                "disk_diffusion_value": 12.0,
                "disk_diffusion_units": "mm",
                "assay": "Kirby-Bauer disk diffusion",
            }],
        },
        root="../",
        stats={},
    )

    assert '<th scope="col">Sample/genome</th>' in html
    assert '<th scope="col">Disk diffusion</th>' in html
    assert "&gt;=18.0 mm" in html
    assert "1.0 mg/L</td>\n    <td class=\"num\">—</td>" in html
    assert "<td class=\"num\">—</td>\n    <td class=\"num\">12.0 mm</td>" in html
    assert "BioSample" in html
    assert "SAMN11953777" in html
    assert "BioProject" in html
    assert "PRJNA123456" in html
    assert "Assembly" in html
    assert "GCF_000005845.2" in html
    assert "SRR123456" in html
