from __future__ import annotations

import json
from pathlib import Path

from antibioticmech.chemical_embedding import (
    load_structure_records,
    validate_artifact,
)

REPO = Path(__file__).resolve().parent.parent
CORPUS = REPO / "data" / "antibiotics"
ARTIFACT_PATH = REPO / "data" / "embeddings" / "chemical-structure-map.json"
PUBLIC_ARTIFACT_PATH = REPO / "pages" / "data" / "chemical-structure-map.json"


def load_artifact() -> dict:
    return json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))


def test_committed_chemical_artifact_is_current_and_complete():
    records = load_structure_records(CORPUS, CORPUS / "PATHS.tsv")
    artifact = load_artifact()

    assert validate_artifact(artifact, records) == []
    assert artifact["record_count"] == len(records)
    assert artifact["quality"]["inchi_fallback_count"] >= 0
    assert artifact["quality"]["multifragment_count"] >= 0
    assert artifact["quality"]["zero_distance_stereoisomer_pairs"] == 0
    assert all(len(row["neighbors"]) == 15 for row in artifact["records"])


def test_every_map_record_and_neighbor_has_a_published_target():
    artifact = load_artifact()
    by_id = {row["identifier"]: row for row in artifact["records"]}

    for row in artifact["records"]:
        assert (REPO / "pages" / row["path"]).is_file(), row["identifier"]
        assert isinstance(row["x"], float)
        assert isinstance(row["y"], float)
        for neighbor in row["neighbors"]:
            assert neighbor["identifier"] in by_id
            assert neighbor["identifier"] != row["identifier"]
            assert 0 <= neighbor["distance"] <= 1


def test_renderer_publishes_exact_local_assets_and_accessible_fallbacks():
    page = (REPO / "pages" / "chemical-map.html").read_text(encoding="utf-8")
    script = (REPO / "pages" / "chemical-map.js").read_text(encoding="utf-8")

    assert PUBLIC_ARTIFACT_PATH.read_bytes() == ARTIFACT_PATH.read_bytes()
    assert 'src="chemical-map.js"' in page
    assert 'data-source="data/chemical-structure-map.json"' in page
    assert 'id="map-results"' in page
    assert 'aria-live="polite"' in page
    assert "<canvas" in page
    assert "https://" not in script
    assert "fetch(root.dataset.source)" in script


def test_site_navigation_and_sitemap_include_distinct_chemical_map():
    record_page = (
        REPO / "pages" / "antibacterial" / "erythromycin-a.html"
    ).read_text(encoding="utf-8")
    sitemap = (REPO / "pages" / "sitemap.xml").read_text(encoding="utf-8")

    assert '../chemical-map.html">Chemical map</a>' in record_page
    assert "/pages/chemical-map.html</loc>" in sitemap
