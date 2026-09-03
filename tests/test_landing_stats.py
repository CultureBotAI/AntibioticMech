"""Landing-page statistics navigate to the views that explain them."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from render_pages import _has_chebi_and_aro  # noqa: E402


def test_every_landing_stat_is_a_link_to_a_matching_view():
    landing = (
        ROOT / "src" / "antibioticmech" / "templates" / "index.html"
    ).read_text(encoding="utf-8")

    assert '<div class="stat">' not in landing
    for target in (
        "browse.html",
        "index.html#identity-grounding",
        "index.html#source-integration",
        "index.html#review-status",
    ):
        assert f'<a class="stat" href="{target}">' in landing
    assert "a.stat:focus-visible" in landing


def test_chebi_and_aro_stat_does_not_mean_arbitrary_multi_source():
    def record(*sources: str) -> dict:
        return {"source_concepts": [{"source": source} for source in sources]}

    assert _has_chebi_and_aro(record("CHEBI", "ARO"))
    assert _has_chebi_and_aro(record("CHEBI", "ARO", "OTHER"))
    assert not _has_chebi_and_aro(record("CHEBI", "OTHER"))
    assert not _has_chebi_and_aro(record("CHEBI", "CHEBI"))
