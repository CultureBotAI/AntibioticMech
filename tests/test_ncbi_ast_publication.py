"""Publication audits must exercise the real writer and fail on lost source context."""

import copy
import json
import sys
from pathlib import Path

import pytest
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_ncbi_ast_publication as publication  # noqa: E402
import seed_from_sources as seed  # noqa: E402
from ncbi_ast_biosamples import activity_observations  # noqa: E402
from test_ncbi_ast_biosamples import convert, pair, review_file, sample  # noqa: E402

from antibioticmech import activity_collections  # noqa: E402


@pytest.fixture
def template():
    return Environment(
        loader=FileSystemLoader(publication.TEMPLATES_DIR),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    ).get_template("record.html")


def render(template, observations):
    return template.render(r={"label": "test", "activity_spectrum": observations}, root="../", stats={})


def test_every_displayed_cell_and_paired_context_is_checked(tmp_path, template):
    rows = pair()
    inventory, review = review_file(tmp_path, rows, sample([rows[0]]))
    observation = list(activity_observations(rows, inventory, convert, review))[0][1]
    observation["strain"] = "A < B & C"
    second = convert(pair(mic_value="2")[0])
    observations = [observation, second]
    html = render(template, observations)
    publication.verify_activity_table(html, observations)
    for text in ("GCA_000000001.1", "PRJNA2", "Source created", "1 measurement(s)", "RESISTANT", "2.0"):
        assert text in html
        with pytest.raises(ValueError, match="rendered activity"):
            publication.verify_activity_table(html.replace(text, "lost"), observations)
    with pytest.raises(ValueError, match="rendered activity"):
        publication.verify_activity_table(html, observations[::-1])
    with pytest.raises(ValueError, match="duplicated"):
        publication.verify_activity_table(html + html, observations)
    with pytest.raises(ValueError, match="missing"):
        publication.verify_activity_table("", observations)


def test_disk_only_and_missing_fields_do_not_invent_mic(template):
    observation = {
        "taxon_label": "Example",
        "assay": "disk diffusion",
        "disk_diffusion_value": 18.0,
        "disk_diffusion_units": "mm",
        "disk_diffusion_qualifier": ">=",
    }
    publication.verify_activity_table(render(template, [observation]), [observation])
    publication.verify_activity_table(render(template, []), [])


def record_fixture():
    path = seed.read_lockfile_paths()["CHEBI:478164"]
    existing = activity_collections.load_record(path)
    fresh = copy.deepcopy(existing)
    fresh["activity_spectrum"] = [
        a for a in fresh.get("activity_spectrum", []) if seed.is_cryptic_sourced_activity(a)
    ] + [convert(pair()[0])]
    return path, existing, fresh


def test_real_record_write_roundtrip_and_reseed(tmp_path, template):
    path, existing, fresh = record_fixture()
    before = copy.deepcopy(existing)
    metrics = publication.audit_record(fresh, existing, path, tmp_path, template, {})
    assert existing == before
    assert metrics["observations"] == 1
    assert metrics["yaml_bytes"] > 0 and metrics["html_bytes"] > 0
    loaded = activity_collections.load_record(tmp_path / "records" / metrics["record"])
    assert seed.ncbi_ast_sourced_activity_view(loaded) == seed.ncbi_ast_sourced_activity_view(fresh)
    assert seed.merge_with_existing(fresh, loaded) == loaded


def test_publication_audit_resolves_and_counts_all_artifacts(tmp_path, template, monkeypatch):
    monkeypatch.setattr(activity_collections, "COLLECTION_SIZE", 3)
    path, existing, fresh = record_fixture()
    original = copy.deepcopy(fresh["activity_spectrum"][-1])
    for number in range(1, 7):
        fresh["activity_spectrum"].append({**original, "source_observation_id": f"fixture-{number}"})
    metrics = publication.audit_record(fresh, existing, path, tmp_path, template, {})
    written = tmp_path / "records" / metrics["record"]
    loaded = activity_collections.load_record(written)
    assert metrics["observations"] == 7
    assert metrics["collection_files"] == 3
    assert metrics["collection_bytes"] == sum(p.stat().st_size for p in written.parent.glob("*.jsonl.gz"))
    assert seed.ncbi_ast_sourced_activity_view(loaded) == seed.ncbi_ast_sourced_activity_view(fresh)
    html = (tmp_path / "pages" / Path(metrics["record"]).with_suffix(".html")).read_text()
    publication.verify_activity_table(html, loaded["activity_spectrum"])


def test_merge_rejects_non_ast_source_loss():
    _, existing, fresh = record_fixture()
    existing.setdefault("activity_spectrum", []).append({"source": "CRYPTIC", "taxon_label": "sentinel"})
    with pytest.raises(ValueError, match="non-AST activities"):
        publication.verify_merge(fresh, existing)


def test_merge_preserves_curated_activity_and_replaces_stale_ast():
    _, existing, fresh = record_fixture()
    curated = {"taxon_label": "curator sentinel", "assay": "literature"}
    stale = {"source": "NCBI_AST", "source_observation_id": "stale"}
    existing.setdefault("activity_spectrum", []).extend([curated, stale])
    result = publication.verify_merge(fresh, existing)
    assert curated in result["activity_spectrum"]
    assert stale not in result["activity_spectrum"]
    assert seed.merge_with_existing(fresh, result) == result


def test_merge_rejects_unrelated_changes():
    _, existing, fresh = record_fixture()
    fresh["label"] = "changed identity"
    with pytest.raises(ValueError, match="non-AST field"):
        publication.verify_merge(fresh, existing)


def test_explicit_inventory_cannot_silently_disappear(tmp_path):
    with pytest.raises(ValueError, match="explicit NCBI AST inventory"):
        seed.attach_ncbi_ast_activity({}, inventory=tmp_path / "missing.tsv")


@pytest.mark.parametrize("target", ["data/raw", "data/antibiotics", "pages", "reports"])
def test_audit_refuses_published_or_shared_output_directories(target):
    with pytest.raises(ValueError, match="direct child"):
        publication.audit(Path("unused"), publication.REPO_ROOT / target)


def test_staged_audit_publishes_only_after_all_checks(tmp_path, monkeypatch):
    path, existing, fresh = record_fixture()
    root = tmp_path / "repo"
    corpus = root / "data/antibiotics"
    new_path = corpus / path.relative_to(seed.CORPUS_DIR)
    new_path.parent.mkdir(parents=True)
    new_path.write_text(yaml.safe_dump(existing))
    inventory = tmp_path / "activity.tsv"
    inventory.write_text("test fixture input")
    reports = root / "reports"
    target = reports / "audit"
    monkeypatch.setattr(publication, "REPO_ROOT", root)
    monkeypatch.setattr(publication, "CORPUS_DIR", corpus)
    monkeypatch.setattr(publication, "read_lockfile_paths", lambda: {fresh["identifier"]: new_path})
    def rebuild(**kwargs):
        assert kwargs == {"ncbi_ast_inventory": inventory}
        return {fresh["identifier"]: fresh}

    monkeypatch.setattr(publication, "rebuild", rebuild)
    # build_record requires a path inside the actual repository; all other paths stay staged.
    real_build = publication.build_record
    monkeypatch.setattr(publication, "build_record", lambda p, *a, **kw: real_build(path, *a, **kw))
    result = publication.audit(inventory, target)
    assert result["totals"]["observations"] == 1
    assert json.loads((target / "audit.json").read_text()) == result
    with pytest.raises(ValueError, match="refusing to overwrite"):
        publication.audit(inventory, target)
    before = new_path.read_bytes()
    label = fresh["label"]
    fresh["label"] = "bad identity"
    with pytest.raises(ValueError, match="non-AST field"):
        publication.audit(inventory, reports / "failure")
    assert not (reports / "failure").exists()
    assert new_path.read_bytes() == before
    fresh["label"] = label

    def changed_input(**kwargs):
        inventory.write_text("input changed during rebuild")
        return rebuild(**kwargs)

    monkeypatch.setattr(publication, "rebuild", changed_input)
    with pytest.raises(ValueError, match="changed during the audit"):
        publication.audit(inventory, reports / "input-drift")
    assert not (reports / "input-drift").exists()
    assert not list(reports.glob(".ncbi-publication-*"))
