"""A ChEBI/ARO refresh cannot erase another source's provenance."""

from __future__ import annotations

import copy
import gzip
import hashlib
import os
import sys

import pytest
import yaml


@pytest.fixture
def refresh(tmp_path, monkeypatch, repo_root, request):
    sys.path.insert(0, str(repo_root / "scripts"))
    import check_provenance as checker
    import extract_source_inventory as extractor

    raw = tmp_path / "data/raw"
    raw.mkdir(parents=True)
    downloads = tmp_path / "downloads"
    downloads.mkdir()
    conf = yaml.safe_load((repo_root / "conf/sources.yaml").read_text())
    conf_path = tmp_path / "sources.yaml"
    conf_path.write_text(yaml.safe_dump(conf))
    for name in [*conf["chebi"]["files"], "aro.obo"]:
        path = downloads / name
        path.write_bytes(b"cached upstream fixture")
        os.utime(path, (1725148800, 1725148800))
    previous = yaml.safe_load((repo_root / "data/raw/MANIFEST.yaml").read_text())
    previous["sources"]["chebi"]["license"] = "outdated fixture license"
    previous["sources"]["aro"]["molecule_root"] = "outdated fixture root"
    if getattr(request, "param", None) == "gzip":
        previous["inventories"]["ncbi_ast_activity.tsv.gz"] = {
            "source": "synthetic fixture, not adopted data",
        }
    owned = {extractor.CHEBI_INVENTORY, extractor.ARO_INVENTORY,
             extractor.ARO_RESISTANCE, extractor.ARO_TARGETS, extractor.CHEBI_ROLE_NAMES}
    payload = b"column\nvalue\n"
    for name, entry in previous["inventories"].items():
        compressed = name.endswith(".gz")
        stored = gzip.compress(payload, mtime=0) if compressed else payload
        (raw / name).write_bytes(stored)
        entry.update(rows=1, bytes=len(stored), sha256=hashlib.sha256(stored).hexdigest())
        if compressed or "content_sha256" in entry:
            entry.update(encoding="gzip" if compressed else "identity",
                         content_sha256=hashlib.sha256(payload).hexdigest(), content_bytes=len(payload))
    manifest_path = raw / "MANIFEST.yaml"
    manifest_path.write_text(yaml.safe_dump(previous, sort_keys=False))
    monkeypatch.setattr(extractor, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(extractor, "CONF_PATH", conf_path)
    monkeypatch.setattr(extractor, "DOWNLOAD_DIR", downloads)
    monkeypatch.setattr(extractor, "RAW_DIR", raw)
    monkeypatch.setattr(checker, "RAW_DIR", raw)
    monkeypatch.setattr(checker, "MANIFEST_PATH", manifest_path)
    # Exercise the real refresh/write path without fetching or parsing upstream data.
    monkeypatch.setattr(extractor, "extract_aro", lambda *a, **kw: ([], [], [], {}))
    monkeypatch.setattr(extractor, "extract_chebi", lambda *a, **kw: ([], []))
    monkeypatch.setattr(sys, "argv", ["extract_source_inventory.py", "--offline"])
    return extractor, checker, raw, manifest_path, previous, owned, conf


def test_refresh_preserves_all_other_sources_and_updates_only_owned_entries(refresh):
    extractor, checker, raw, path, previous, owned, conf = refresh
    unchanged = {name: (raw / name).read_bytes() for name in previous["inventories"] if name not in owned}
    expected = copy.deepcopy(previous)
    assert extractor.main() == 0
    actual = yaml.safe_load(path.read_text())
    assert set(actual["inventories"]) == set(previous["inventories"])
    for name in unchanged:
        assert actual["inventories"][name] == expected["inventories"][name]
        assert (raw / name).read_bytes() == unchanged[name]
    for name in owned:
        assert actual["inventories"][name]["rows"] == 0
        assert actual["inventories"][name]["sha256"] == hashlib.sha256((raw / name).read_bytes()).hexdigest()
    for name in set(previous["sources"]) - {"chebi", "aro"}:
        assert actual["sources"][name] == expected["sources"][name]
    owned_downloads = {*conf["chebi"]["files"], "aro.obo"}
    for name in set(previous["downloads"]) - owned_downloads:
        assert actual["downloads"][name] == expected["downloads"][name]
    for name in owned_downloads:
        assert actual["downloads"][name]["sha256"] == hashlib.sha256(b"cached upstream fixture").hexdigest()
    assert actual["sources"]["chebi"]["license"] == conf["chebi"]["license"]
    assert actual["sources"]["aro"]["molecule_root"] == conf["aro"]["molecule_root"]
    assert actual["retrieved_on"] == "2024-09-01"
    assert checker.main() == 0
    first_bytes = path.read_bytes()
    assert extractor.main() == 0
    assert path.read_bytes() == first_bytes


@pytest.mark.parametrize("refresh", ["gzip"], indirect=True)
def test_refresh_preserves_future_compressed_inventory_metadata_without_adopting_it(refresh):
    extractor, _, raw, path, previous, _, _ = refresh
    payload = b"column\nvalue\n"
    name = "ncbi_ast_activity.tsv.gz"
    compressed = (raw / name).read_bytes()
    assert gzip.decompress(compressed) == payload
    entry = previous["inventories"][name]
    assert entry["content_sha256"] == hashlib.sha256(payload).hexdigest()
    assert entry["content_bytes"] == len(payload)
    assert entry["encoding"] == "gzip"
    assert extractor.main() == 0
    assert yaml.safe_load(path.read_text())["inventories"][name] == entry
    assert (raw / name).read_bytes() == compressed


@pytest.mark.parametrize("change", ["missing", "modified"])
def test_refresh_does_not_drop_or_rehash_invalid_independent_inventory(refresh, change, capsys):
    extractor, checker, raw, path, previous, _, _ = refresh
    inventory = raw / "cryptic_activity.tsv"
    if change == "missing":
        inventory.unlink()
    else:
        inventory.write_bytes(b"column\nchanged\n")
    assert extractor.main() == 0
    actual = yaml.safe_load(path.read_text())["inventories"][inventory.name]
    assert actual == previous["inventories"][inventory.name]
    assert checker.main() == 1
    assert inventory.name in capsys.readouterr().err


def test_refresh_does_not_invent_provenance_for_unmanifested_inventory(refresh, capsys):
    extractor, checker, raw, path, _, _, _ = refresh
    (raw / "unreviewed.tsv").write_text("column\nvalue\n")
    assert extractor.main() == 0
    assert "unreviewed.tsv" not in yaml.safe_load(path.read_text())["inventories"]
    assert checker.main() == 1
    assert "unreviewed.tsv: committed but absent from MANIFEST.yaml" in capsys.readouterr().err


def test_dry_run_does_not_change_any_inventory_or_manifest(refresh, monkeypatch):
    extractor, _, raw, _, _, _, _ = refresh
    before = {path.name: path.read_bytes() for path in raw.iterdir()}
    monkeypatch.setattr(sys, "argv", ["extract_source_inventory.py", "--offline", "--dry-run"])
    assert extractor.main() == 0
    assert {path.name: path.read_bytes() for path in raw.iterdir()} == before
