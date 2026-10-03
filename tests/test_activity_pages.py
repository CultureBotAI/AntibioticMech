"""Activity publication must bound the DOM, not truncate scientific observations."""

import copy
import gzip
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import activity_pages as activity  # noqa: E402
import render_pages  # noqa: E402
from audit_ncbi_ast_publication import (  # noqa: E402
    verify_activity_publication,
    verify_activity_table,
    verify_site_links,
)
from render_pages import TEMPLATES_DIR  # noqa: E402

from antibioticmech.activity_collections import load_record  # noqa: E402


@pytest.fixture
def env():
    return Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=select_autoescape(["html"]),
                       trim_blocks=True, lstrip_blocks=True)


@pytest.fixture
def doc():
    observations = [{
        "taxon_label": "Example bacterium", "taxon_id": "NCBITaxon:1", "strain": f"isolate {i}",
        "activity": "RESISTANT", "assay": "broth dilution", "mic_value": float(i),
        "mic_qualifier": ">", "mic_units": "mg/L", "biosample_accession": f"SAMN{i}",
        "source": "NCBI_AST", "source_observation_id": f"source-{i}",
        "evidence": [{"reference": "PMID:1", "notes": "<img src=x onerror=alert(1)>"}],
    } for i in range(201)]
    observations[-1].update(
        activity="", source="", assay="disk diffusion", mic_value=None,
        disk_diffusion_value=18.0, disk_diffusion_qualifier="<=", disk_diffusion_units="mm",
        measurement_count=1, source_export_row_count=2,
        pathogen_detection_contexts=[
            {"pathogen_detection_target_accession": "PDT1.1", "assembly_accession": "GCA_1.1",
             "bioproject_accession": "PRJNA1", "sra_accessions": ["SRR1"]},
            {"pathogen_detection_target_accession": "PDT2.1", "assembly_accession": "GCA_2.1",
             "bioproject_accession": "PRJNA2", "sra_accessions": ["SRR2"]},
        ],
    )
    return {"identifier": "CHEBI:1", "label": "example <compound>",
            "chemical_structure": {"standard_inchi_key": "AAAAAAAAAAAAAA-BBBBBBBBBB-C"},
            "activity_spectrum": observations, "evidence": [{"reference": "PMID:2"}]}


def publish(doc, tmp_path, env):
    return activity.render_activity_pages(doc, Path("antibacterial/example.yaml"), tmp_path, env, {})


def test_complete_publication_is_bounded_and_deterministic(tmp_path, env, doc):
    original = copy.deepcopy(doc)
    publication = publish(doc, tmp_path / "one", env)
    assert doc == original
    assert len(publication["preview"]) == 20
    assert len(publication["pages"]) == 3
    metrics = verify_activity_publication(doc, tmp_path / "one", publication)
    assert metrics["activity_page_count"] == 3
    directory = tmp_path / "one/antibacterial/example"
    for number, count in [(1, 100), (2, 100), (3, 1)]:
        html = (directory / f"activity-{number}.html").read_text()
        assert html.count('class="activity-evidence"') == count
        assert "example &lt;compound&gt;" in html
        assert "onerror" not in html
    last = (directory / "activity-3.html").read_text()
    assert "18.0 mm" in last and "GCA_2.1" in last and "1 measurement(s)" in last
    assert 'id="observation-201"' in last
    other = publish(doc, tmp_path / "two", env)
    first_bytes = {p.relative_to(tmp_path / "one"): p.read_bytes() for p in publication["written"]}
    other_bytes = {p.relative_to(tmp_path / "two"): p.read_bytes() for p in other["written"]}
    assert first_bytes == other_bytes
    assert set(first_bytes) == {
        p.relative_to(tmp_path / "one") for p in (tmp_path / "one").rglob("*") if p.is_file()
    }


@pytest.mark.parametrize("count,preview,pages", [(1, 1, 1), (100, 100, 1), (101, 20, 2), (200, 20, 2)])
def test_page_boundaries_and_record_preview(tmp_path, env, doc, count, preview, pages):
    doc["activity_spectrum"] = doc["activity_spectrum"][:count]
    result = publish(doc, tmp_path, env)
    assert len(result["preview"]) == preview and len(result["pages"]) == pages
    verify_activity_publication(doc, tmp_path, result)
    record = {**doc, "activity_spectrum": result["preview"], "activity": result["activity"]}
    html = env.get_template("record.html").render(r=record, root="../", stats={})
    verify_activity_table(html, result["preview"], evidence=True)
    assert 'href="example/activity-1.html"' in html
    assert f"{count} observations" in html


@pytest.mark.parametrize("target", [
    "cell", "anchor", "evidence", "previous", "next", "download", "checksum", "index", "page",
])
def test_audit_rejects_missing_or_changed_publication(tmp_path, env, doc, target):
    result = publish(doc, tmp_path, env)
    directory = tmp_path / "antibacterial/example"
    if target in {"checksum", "index"}:
        path = next(directory.glob("search-*.gz"))
        if target == "checksum":
            path.write_bytes(path.read_bytes()[:-1])
        else:
            wrong = json.loads(gzip.decompress(path.read_bytes()))
            wrong["rows"].pop()
            result["activity"]["index"] = activity.write_json(directory, "search", wrong)
    elif target == "page":
        result["pages"].pop()
    else:
        path = directory / "activity-2.html"
        before, after = {
            "cell": ("SAMN100", "SAMNwrong"),
            "anchor": ('id="observation-101"', 'id="observation-1"'),
            "evidence": ('data-row="0"', 'data-row="1"'),
            "previous": ('rel="prev"', 'rel="lost"'),
            "next": ('rel="next"', 'rel="lost"'),
            "download": (' download>Complete record', '>Complete record'),
        }[target]
        html = path.read_text()
        assert before in html
        path.write_text(html.replace(before, after))
    with pytest.raises(ValueError):
        verify_activity_publication(doc, tmp_path, result)


def test_complete_download_cannot_silently_drop_nonactivity_fields(tmp_path, env, doc):
    result = publish(doc, tmp_path, env)
    changed = copy.deepcopy(doc)
    changed.pop("evidence")
    directory = tmp_path / "antibacterial/example"
    result["activity"]["download"] = activity.write_json(directory, "record", changed, browser=False)
    with pytest.raises(ValueError, match="complete record download"):
        verify_activity_publication(doc, tmp_path, result)


def test_browser_limits_and_expanded_input_are_enforced(tmp_path, env, doc, monkeypatch):
    doc["activity_collections"] = [{"path": "not-expanded"}]
    with pytest.raises(ValueError, match="expanded"):
        publish(doc, tmp_path, env)
    doc.pop("activity_collections")
    monkeypatch.setattr(activity, "MAX_BROWSER_BYTES", 10)
    with pytest.raises(ValueError, match="browser payload"):
        publish(doc, tmp_path, env)
    assert publish({**doc, "activity_spectrum": []}, tmp_path, env) == {"written": set(), "pages": []}


def test_search_includes_both_paired_contexts_and_unknown_filters(doc):
    row = activity.search_row(201, doc["activity_spectrum"][-1])
    assert row[:6] == [201, "Example bacterium", "NCBITaxon:1", "isolate 200", "", ""]
    for value in ["SAMN200", "PDT1.1", "PDT2.1", "GCA_1.1", "GCA_2.1", "PRJNA1", "PRJNA2", "SRR1", "SRR2"]:
        assert value in row[6] and value.lower() in row[7]


def test_full_site_link_check_rejects_broken_and_escaping_targets(tmp_path):
    (tmp_path / "asset.js").write_text("test")
    page = tmp_path / "index.html"
    page.write_text('<script src="asset.js"></script><a href="https://example.org/">external</a>')
    assert verify_site_links(tmp_path) == 1
    for target in ["missing.html", "../index.html", "missing.json.gz"]:
        page.write_text(f'<a href="{target}">missing</a>')
        with pytest.raises(ValueError, match="broken local site link"):
            verify_site_links(tmp_path)


def test_site_owns_prunes_and_lists_all_activity_artifacts(tmp_path, doc, monkeypatch):
    path = render_pages.CORPUS_DIR / "antibacterial/tetracycline.yaml"
    record = load_record(path)
    record["activity_spectrum"] = doc["activity_spectrum"]
    chemical_map = json.loads(render_pages.CHEMICAL_MAP_ARTIFACT.read_text())
    monkeypatch.setattr(render_pages, "load_chemical_map", lambda identifiers: chemical_map)
    render_pages.build(tmp_path, records=[(path, record)])
    directory = tmp_path / "antibacterial/tetracycline"
    before = {p.name for p in directory.glob("*.gz")}
    sitemap = (tmp_path / "sitemap.xml").read_text()
    assert "antibacterial/tetracycline/activity-3.html" in sitemap
    record["activity_spectrum"] = record["activity_spectrum"][:1]
    render_pages.build(tmp_path, records=[(path, record)])
    assert not before.intersection({p.name for p in directory.glob("*.gz")})
    assert not (directory / "activity-2.html").exists()
    assert "activity-3.html" not in (tmp_path / "sitemap.xml").read_text()
    record["activity_spectrum"] = []
    render_pages.build(tmp_path, records=[(path, record)])
    assert not directory.exists()


@pytest.mark.skipif(not shutil.which("node"), reason="Node is needed for browser-logic regression checks")
def test_browser_logic(tmp_path, env, doc):
    result = publish(doc, tmp_path, env)
    script = Path(__file__).parent / "activity_browser.test.cjs"
    subprocess.run(["node", str(script), str(TEMPLATES_DIR / "activity_browser.js"),
                    str(tmp_path / "antibacterial/example" / result["activity"]["index"])],
                   check=True, capture_output=True, text=True)
