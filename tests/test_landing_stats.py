"""Landing-page statistics navigate to the views that explain them."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


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
