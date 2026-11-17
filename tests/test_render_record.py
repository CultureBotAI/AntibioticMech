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
                "pathogen_detection_target_accession": "PDT000001234.1",
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
            }, {
                "taxon_label": "Klebsiella pneumoniae",
                "activity": "NONSUSCEPTIBLE",
                "mic_value": 4.0,
                "mic_units": "mg/L",
                "assay": "NCBI Pathogen Detection AST",
                "measurement_count": 1,
                "source_export_row_count": 2,
                "pathogen_detection_contexts": [{
                    "pathogen_detection_target_accession": "PDT000000001.1",
                    "assembly_accession": "GCA_000000001.1",
                    "bioproject_accession": "PRJNA1",
                    "source_create_date": "2026-01-01",
                }, {
                    "pathogen_detection_target_accession": "PDT000000002.1",
                    "assembly_accession": "GCA_000000002.1",
                    "bioproject_accession": "PRJNA2",
                    "source_create_date": "2026-02-01",
                }],
            }, {
                "taxon_label": "Salmonella enterica",
                "activity": "SUSCEPTIBLE_DOSE_DEPENDENT",
                "mic_value": 2.0,
                "mic_units": "mg/L",
                "assay": "NCBI Pathogen Detection AST",
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
    assert '<span class="pill warn">NONSUSCEPTIBLE</span>' in html
    assert '<span class="pill warn">SUSCEPTIBLE_DOSE_DEPENDENT</span>' in html
    assert "BioProject" in html
    assert "PRJNA123456" in html
    assert "Pathogen Detection" in html
    assert "PDT000001234.1" in html
    assert "Assembly" in html
    assert "GCF_000005845.2" in html
    assert "SRR123456" in html
    assert html.count('class="genome-context"') == 2
    for accession in ("PDT000000001.1", "PDT000000002.1", "GCA_000000001.1", "GCA_000000002.1"):
        assert accession in html
    assert "1 measurement(s); 2 source export rows" in html
    assert "Source created 2026-02-01" in html


def test_resistance_summary_counts_claims_without_asserting_distinct_known_routes():
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(["html", "xml"]),
    )
    claims = [{
        "mechanism_type": "UNKNOWN",
        "label": "Author-reported gene association",
        "note": "Reference-only identity; experimental allele unresolved.",
        "evidence": [{"reference": "DOI:10.1000/widget"}],
    }, {
        "mechanism_type": "UNKNOWN",
        "label": "Second association in the same pathway",
        "evidence": [{"reference": "DOI:10.1000/widget"}],
    }]
    html = env.get_template("record.html").render(
        r={
            "identifier": "antibioticmech:curator-widget",
            "label": "widgetmycin",
            "class_slug": "antifungal",
            "antimicrobial_class": "ANTIFUNGAL",
            "grounding_status": "MINTED",
            "curation_status": "PROPOSED",
            "source_concepts": [],
            "resistance_mechanisms": claims,
            "resistance_groups": [{"mechanism_type": "UNKNOWN", "rows": claims}],
        },
        root="../",
        stats={},
    )
    assert "2 source-backed resistance determinants or associations" in html
    assert "known routes" not in html
    assert "Reference-only identity; experimental allele unresolved." in html
    assert all(claim["label"] in html for claim in claims)
