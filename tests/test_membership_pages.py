"""Published source IDs must remain paired, searchable, and bound to their assays."""

import gzip
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from activity_pages import render_activity_pages, write_json  # noqa: E402
from audit_ncbi_ast_publication import verify_activity_publication, verify_activity_table  # noqa: E402
from render_pages import TEMPLATES_DIR  # noqa: E402
from test_activity_memberships import prepared  # noqa: E402

from antibioticmech.activity_memberships import FIELD  # noqa: E402
from antibioticmech.validation.write_validated import write_validated_antibiotic  # noqa: E402


@pytest.fixture
def published(tmp_path):
    doc, ref, artifacts = prepared()
    source = tmp_path / "records/antibacterial/example.yaml"
    write_validated_antibiotic(doc, source, membership_artifacts=artifacts)
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=select_autoescape(["html"]))
    output = tmp_path / "pages"
    result = render_activity_pages(doc, source, output, env, {})
    return doc, ref, result, output, env


def test_bounded_publication_exposes_lossless_downloads_and_indexed_members(published):
    doc, ref, result, output, env = published
    before = json.loads(json.dumps(doc))
    verify_activity_publication(doc, output, result)
    directory = output / "antibacterial/example"
    assert len(result["pages"]) == 2
    assert (directory / "memberships.html").stat().st_size < 20000
    assert "SAMEA123" not in (directory / "memberships.html").read_text()
    download_path = directory / Path(result["activity"]["download"]).name
    download = json.loads(gzip.decompress(download_path.read_bytes()))
    assert download == doc == before
    assert (directory / download[FIELD][0]["path"]).exists()
    search = json.loads(gzip.decompress((directory / result["activity"]["index"]).read_bytes()))
    assert search["memberships"] == [
        ["first prjeb123 samea123 err123", [1]], ["second prjeb123 samea123 err456", [1]], ["unmatched", [1]],
    ]
    assert search["rows"][0][6] == "3 source isolates"
    assert ref["unlinked_subject_count"] == 1
    record = {**doc, "activity": result["activity"]}
    html = env.get_template("record.html").render(r=record, root="../", stats={})
    verify_activity_table(html, doc["activity_spectrum"], evidence=True,
                          memberships=result["activity"]["memberships"])
    assert 'href="example/memberships.html?' in html


@pytest.mark.parametrize("fault", ["download", "index", "search", "link", "browser", "binding"])
def test_membership_audit_rejects_missing_and_misbound_assets(published, fault):
    doc, ref, result, output, _ = published
    directory = output / "antibacterial/example"
    page = directory / "memberships.html"
    if fault == "download":
        (directory / ref["path"]).unlink()
    elif fault == "index":
        index = next(directory.glob("membership-index-*.gz"))
        value = json.loads(gzip.decompress(index.read_bytes()))
        value["groups"][0]["observation"]["mic_value"] = 100.0
        replacement = write_json(directory, "membership-index", value)
        page.write_text(page.read_text().replace(index.name, replacement))
    elif fault == "search":
        path = directory / result["activity"]["index"]
        value = json.loads(gzip.decompress(path.read_bytes()))
        value["memberships"].pop()
        result["activity"]["index"] = write_json(directory, "search", value)
    elif fault == "link":
        page = directory / "activity-1.html"
        page.write_text(page.read_text().replace("memberships.html?", "wrong.html?"))
    elif fault == "browser":
        page.write_text(page.read_text().replace('id="membership-browser"', 'id="wrong"'))
    else:
        page.write_text(page.read_text().replace('data-total="1"', 'data-total="2"'))
    with pytest.raises((ValueError, OSError)):
        verify_activity_publication(doc, output, result)


@pytest.mark.skipif(not shutil.which("node"), reason="Node is needed for browser-logic regression checks")
def test_membership_browser_logic(published):
    _, _, _, output, _ = published
    index = next((output / "antibacterial/example").glob("membership-index-*.gz"))
    subprocess.run(["node", str(Path(__file__).with_name("membership_browser.test.cjs")),
                    str(TEMPLATES_DIR), str(index)], check=True, capture_output=True, text=True)
