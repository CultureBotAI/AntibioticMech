"""CARD audit test collection must not depend on earlier modules' imports."""

import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("filename", [
    "test_card_book_citations.py", "test_card_literature_expansion.py",
])
def test_card_audit_collects_in_fresh_process(filename):
    env = os.environ.copy()
    # Keep dependency paths in overlay environments, but remove the path under test.
    env["PYTHONPATH"] = os.pathsep.join(
        part for part in env.get("PYTHONPATH", "").split(os.pathsep)
        if part and Path(part).resolve() != ROOT / "scripts"
    )
    env.pop("PYTEST_ADDOPTS", None)
    env.pop("PYTEST_PLUGINS", None)
    completed = subprocess.run(
        [sys.executable, "-m", "pytest", "--collect-only", "-q", "tests/" + filename],
        cwd=ROOT, env=env, capture_output=True, text=True, timeout=60, check=False,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
