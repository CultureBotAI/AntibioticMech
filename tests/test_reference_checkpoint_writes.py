"""Dated research checkpoints must not be silently replaced on replay."""

import importlib
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
MODULES = (
    "audit_card_demethylase_taxa",
    "audit_card_demethylase_references",
    "audit_card_glucan_references",
    "audit_ionophore_reference_successor",
)


@pytest.fixture(params=MODULES)
def cli(request, monkeypatch, tmp_path):
    module = importlib.import_module(request.param)
    result = {"summary": {"fixture": True}}
    output = tmp_path / "checkpoint.json"
    monkeypatch.setattr(module, "OUTPUT", output)
    monkeypatch.setattr(module, "build", lambda root: result)
    monkeypatch.setattr(sys, "argv", [request.param])
    return module, output, json.dumps(result, indent=2, sort_keys=True) + "\n"


def test_default_creates_missing_checkpoint(cli):
    module, output, expected = cli
    module.main()
    assert output.read_text() == expected


@pytest.mark.parametrize("check", [False, True])
def test_existing_equal_checkpoint_is_not_rewritten(cli, monkeypatch, check):
    module, output, expected = cli
    output.write_text(expected)
    if check:
        monkeypatch.setattr(sys, "argv", [module.__name__, "--check"])
    original_open = Path.open

    def read_only(path, mode="r", *args, **kwargs):
        if path == output and any(flag in mode for flag in "wax+"):
            raise AssertionError("existing checkpoint must not be opened for writing")
        return original_open(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", read_only)
    module.main()
    assert output.read_text() == expected


@pytest.mark.parametrize("check", [False, True])
def test_differing_checkpoint_fails_without_replacement(cli, monkeypatch, check):
    module, output, _ = cli
    original = '{"historical": true}\n'
    output.write_text(original)
    if check:
        monkeypatch.setattr(sys, "argv", [module.__name__, "--check"])
    with pytest.raises(ValueError, match="differs from native replay"):
        module.main()
    assert output.read_text() == original


def test_check_never_creates_missing_checkpoint(cli, monkeypatch):
    module, output, _ = cli
    monkeypatch.setattr(sys, "argv", [module.__name__, "--check"])
    with pytest.raises(FileNotFoundError):
        module.main()
    assert not output.exists()


def test_concurrent_creation_is_not_overwritten(cli, monkeypatch):
    module, output, _ = cli
    original = '{"concurrent": true}\n'
    output.write_text(original)
    original_exists = Path.exists
    monkeypatch.setattr(Path, "exists", lambda path: False if path == output else original_exists(path))
    with pytest.raises(FileExistsError):
        module.main()
    assert output.read_text() == original
