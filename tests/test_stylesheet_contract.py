"""The stylesheet resolves, and resolves the same way in both dark declarations.

CSS never reports a failure. An undefined token falls back to its literal, a
duplicated selector quietly overrides the earlier one, and a dark value present
in one of the two dark blocks but not the other themes correctly by toggle and
incorrectly by OS preference. Every one of those renders, passes `--check`, and
passes a page-level site contract, so "it rendered" says almost nothing about
whether it rendered correctly. See issue #116.
"""

from __future__ import annotations

import re

STYLESHEET = "src/antibioticmech/templates/style.css"

# Declared twice on purpose: the pastel overrides layer onto the base rules for
# the same selector, and the map palette re-opens :root. A new name appearing
# here is a merge that appended a stylesheet instead of folding it in.
ALLOWED_DUPLICATE_SELECTORS = {":root", "th", ".card"}

TOKEN_DECL = re.compile(r"^\s*(--[\w-]+)\s*:", re.M)
RULE_SELECTOR = re.compile(r"(?m)^([^\s@/}][^{]*)\{")
VAR_WITH_FALLBACK = re.compile(r"var\(\s*(--[\w-]+)\s*,\s*([^)]+)\)")
COLOUR_LITERAL = re.compile(
    r"(?m)^\s*(?:color|background|background-color)\s*:\s*"
    # rgb()/hsl() too. Matching only hex is how `.map-tooltip` kept a literal
    # `background: rgb(23 32 42 / .94)` beside a tokenised `color: var(--bg)` —
    # the exact 1.01:1 pairing this test's docstring describes, surviving the
    # test that describes it.
    r"(#[0-9a-fA-F]{3,8}|white|black|rgba?\([^;]*\)|hsla?\([^;]*\))\s*;"
)


def _text(repo_root):
    return (repo_root / STYLESHEET).read_text(encoding="utf-8")


def _token_block(text, header):
    """The declarations of the first rule whose selector line is `header`."""
    start = text.index(header)
    body = text[start + len(header) : text.index("}", start)]
    return dict(re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", body))


def test_no_var_falls_back_to_a_token_the_stylesheet_never_defines(repo_root):
    """A fallback for a token that exists is a default. A fallback for one that
    does not is a silent substitution -- which is how main's chemical-map rules
    would have painted near-white text onto the dark ground.
    """
    text = _text(repo_root)
    defined = set(TOKEN_DECL.findall(text))
    missing = sorted(
        {(name, fb.strip()) for name, fb in VAR_WITH_FALLBACK.findall(text)
         if name not in defined}
    )
    assert not missing, (
        "var() names a token this stylesheet never defines, so the literal "
        f"fallback is what actually paints: {missing}"
    )


def test_no_selector_is_declared_twice_outside_the_override_set(repo_root):
    """Appending one stylesheet to another produces a file that renders and is
    wrong: whichever copy lands last wins, including its palette.
    """
    text = _text(repo_root)
    seen: dict[str, int] = {}
    for selector in RULE_SELECTOR.findall(text):
        key = selector.strip()
        seen[key] = seen.get(key, 0) + 1
    duplicated = sorted(
        s for s, n in seen.items() if n > 1 and s not in ALLOWED_DUPLICATE_SELECTORS
    )
    assert not duplicated, (
        "selector declared more than once; the later copy silently overrides "
        f"the earlier: {duplicated}"
    )


def test_colours_come_from_tokens_so_they_can_respond_to_the_theme(repo_root):
    """A literal in a color/background declaration cannot change with the theme.
    One such pair -- a literal background beside a tokenised color -- measured
    1.01:1 in dark mode, an invisible button label.
    """
    text = _text(repo_root)
    literals = COLOUR_LITERAL.findall(text)
    assert not literals, (
        "colour literal outside the token blocks; it cannot respond to the "
        f"theme: {sorted(set(literals))}"
    )


def test_both_dark_blocks_declare_the_same_tokens(repo_root):
    """Dark values are declared twice by design -- once for OS preference, once
    for the toggle. A token added to one and not the other yields a page that
    themes correctly one way and not the other, which no page-level check sees.
    """
    text = _text(repo_root)
    by_preference = _token_block(text, ':root:not([data-theme="light"]) {')
    by_toggle = _token_block(text, ':root[data-theme="dark"] {')
    assert by_preference and by_toggle, "expected both dark declarations"
    only_pref = sorted(set(by_preference) - set(by_toggle))
    only_toggle = sorted(set(by_toggle) - set(by_preference))
    assert not only_pref and not only_toggle, (
        f"only under prefers-color-scheme: {only_pref}; "
        f"only under data-theme: {only_toggle}"
    )
    differing = sorted(
        name for name in by_preference
        if by_preference[name].strip() != by_toggle[name].strip()
    )
    assert not differing, f"same token, different dark value: {differing}"
