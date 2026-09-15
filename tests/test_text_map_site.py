"""Publication requires an explicit switch and current validated full inputs."""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest
from jinja2 import Environment, FileSystemLoader

from antibioticmech import text_map_site as site


def configure(root: Path, value="false"):
    config = root / "conf" / "text_map.yaml"
    config.parent.mkdir(parents=True, exist_ok=True)
    config.write_text(f"enabled: {value}\n")


def fake_pipeline():
    calls = []
    profile = {
        "model": "BAAI/bge-large-en-v1.5",
        "revision": "d4aa6901d3a41ba39fb536a557fa166f842b0e09",
        "dimension": 1024,
    }
    manifest = {"encoder": profile, "projection": {"implementation": "pacmap.PaCMAP"}}

    def validate(bundle, *, input_path):
        assert json.loads(input_path.read_text()) == {"test": "fresh full inputs"}
        calls.append(("validate", bundle, input_path))
        return manifest

    def stage(output, published_dir, *, input_path):
        assert json.loads(input_path.read_text()) == {"test": "fresh full inputs"}
        calls.append(("stage", output, published_dir))
        return manifest

    pipeline = SimpleNamespace(
        MODEL=profile["model"],
        MODEL_REVISION=profile["revision"],
        MODEL_DIMENSION=1024,
        current_bundle=lambda output: output / "fixture-bundle",
        validate_bundle=validate,
        stage_map=stage,
    )
    return pipeline, calls, manifest


def enable_fixture(root, monkeypatch):
    configure(root, "true")
    source = root / "data" / "text_map"
    source.mkdir(parents=True)
    (source / "current.json").write_text("{}")
    pipeline, calls, manifest = fake_pipeline()
    monkeypatch.setattr(site, "load_pipeline", lambda _root: pipeline)

    def export(actual_root, output, **kwargs):
        assert actual_root == root
        assert not kwargs, "publication cannot request a canary or limited input set"
        output.write_text(json.dumps({"test": "fresh full inputs"}))
        return {"scope": "full"}

    monkeypatch.setattr(site, "export_inputs", export)
    return pipeline, calls, manifest


def test_disabled_map_requires_no_runtime_or_artifact(tmp_path, monkeypatch):
    configure(tmp_path)
    monkeypatch.setattr(site, "load_pipeline", lambda _root: pytest.fail("disabled map loaded runtime"))
    with site.prepare_text_map(tmp_path) as ready:
        assert ready is None


def test_enabled_map_missing_bundle_fails(tmp_path):
    configure(tmp_path, "true")
    with pytest.raises(ValueError, match="current.json"), site.prepare_text_map(tmp_path):
        pass


def test_enabled_map_missing_shared_runtime_fails(tmp_path):
    configure(tmp_path, "true")
    source = tmp_path / "data" / "text_map"
    source.mkdir(parents=True)
    (source / "current.json").write_text("{}")
    with pytest.raises(ValueError, match="CLAW-governed"), site.prepare_text_map(tmp_path):
        pass


@pytest.mark.parametrize("value", ["1", "'true'", "null", "[]"])
def test_enablement_requires_an_actual_boolean(tmp_path, value):
    configure(tmp_path, value)
    with pytest.raises(ValueError, match="enabled boolean"), site.prepare_text_map(tmp_path):
        pass


def test_enabled_map_uses_fresh_full_inputs_and_canonical_stage(tmp_path, monkeypatch):
    _, calls, _ = enable_fixture(tmp_path, monkeypatch)
    with site.prepare_text_map(tmp_path) as ready:
        inputs = ready.inputs
        ready.stage(tmp_path / "published")
        assert calls[-1] == ("stage", tmp_path / "data" / "text_map", tmp_path / "published" / "text-map")
    assert not inputs.exists()
    assert calls[0][0] == "validate"


def test_legacy_encoder_cannot_be_published_as_the_common_space(tmp_path, monkeypatch):
    _, _, manifest = enable_fixture(tmp_path, monkeypatch)
    manifest["encoder"] = {"model": "MiniLM", "revision": "0" * 40, "dimension": 384}
    with pytest.raises(ValueError, match="pinned fleet BGE"), site.prepare_text_map(tmp_path):
        pass


def test_injected_projector_cannot_reach_the_site_build(tmp_path, monkeypatch):
    _, _, manifest = enable_fixture(tmp_path, monkeypatch)
    manifest["projection"]["implementation"] = "injected-projector"
    with pytest.raises(ValueError, match="actual PaCMAP"), site.prepare_text_map(tmp_path):
        pass


def test_subset_receipt_cannot_reach_publication(tmp_path, monkeypatch):
    enable_fixture(tmp_path, monkeypatch)
    monkeypatch.setattr(site, "export_inputs", lambda _root, _output: {"scope": "subset"})
    with pytest.raises(ValueError, match="full-corpus"), site.prepare_text_map(tmp_path):
        pass


def test_navigation_is_conditional_and_uses_relative_site_root():
    templates = Path(__file__).resolve().parents[1] / "src" / "antibioticmech" / "templates"
    env = Environment(loader=FileSystemLoader(str(templates)))
    template = env.get_template("base.html")
    context = {"root": "../../", "stats": {"extracted_at": "fixture"}}
    assert "Semantic text map" not in template.render(text_map_enabled=False, **context)
    assert 'href="../../text-map/"' in template.render(text_map_enabled=True, **context)


def test_invalid_map_preflight_preserves_existing_published_pages(tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(Path(__file__).resolve().parents[1] / "scripts"))
    from scripts import render_pages

    configure(tmp_path, "true")
    published = tmp_path / "published"
    published.mkdir()
    old = published / "index.html"
    old.write_text("existing published site")
    monkeypatch.setattr(render_pages, "REPO_ROOT", tmp_path)
    with pytest.raises(ValueError, match="current.json"):
        render_pages.build(published)
    assert old.read_text() == "existing published site"


def test_real_renderer_keeps_staged_map_and_links_from_record_pages(tmp_path, monkeypatch):
    """The renderer's pruning/rebuild must preserve all canonical staged files."""
    import yaml

    from scripts import render_pages

    path = next(iter(sorted(render_pages.CORPUS_DIR.rglob("*.yaml"))))
    record = yaml.safe_load(path.read_text())
    monkeypatch.setattr(render_pages, "load_records", lambda: [(path, record)])
    chemical_map = json.loads(render_pages.CHEMICAL_MAP_ARTIFACT.read_text())
    monkeypatch.setattr(render_pages, "load_chemical_map", lambda _ids: chemical_map)

    class Prepared:
        def stage(self, output):
            destination = output / "text-map"
            destination.mkdir()
            for name in ("index.html", "points.json", "manifest.json"):
                (destination / name).write_text("verified fixture " + name)

    output = tmp_path / "site"
    render_pages._build(output, Prepared())
    for name in ("index.html", "points.json", "manifest.json"):
        assert (output / "text-map" / name).read_text() == "verified fixture " + name
    page = (output / path.parent.name / (path.stem + ".html")).read_text()
    assert 'href="../text-map/">Semantic text map</a>' in page
    assert (output / "chemical-map.html").is_file()


def test_current_semantic_navigation_precedes_the_labeled_legacy_view():
    templates = Path(__file__).resolve().parents[1] / "src" / "antibioticmech" / "templates"
    env = Environment(loader=FileSystemLoader(str(templates)))
    context = {"root": "", "stats": {"extracted_at": "fixture"}}
    enabled = env.get_template("base.html").render(text_map_enabled=True, **context)
    assert enabled.index("Semantic text map") < enabled.index("Legacy description map")
    legacy = env.get_template("map.html").render(
        text_map_enabled=True,
        map={"n": 3, "model": "legacy BGE", "method": "pacmap", "classes": []},
        map_json="{}",
        **context,
    )
    assert "saved model revision and" in legacy
    assert "complete input fingerprint are unavailable" in legacy
    assert "Open the current semantic text map" in legacy
