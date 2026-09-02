"""Text the page renders at a contrast nobody can read.

The map tooltip painted its own dark background and took its text colour from
`var(--bg)`, the PAGE background: 16.45:1 in light mode, 1.01:1 in dark. A
visible box containing invisible text, reported as "the popups on hover are
empty".

THE FIRST FIX BROKE ITS OWN GUARD. Tokenising the background removed the literal
that the general rule keyed on, and the accompanying check read the TOKEN
DECLARATIONS rather than `.map-tooltip`'s body — so restoring `color: var(--bg)`
reproduced the original defect with 208/208 green. A guard on the shape of a
declaration cannot survive the declaration being rewritten.

So this resolves each RULE the way a browser does — through the cascade, per
theme — and checks the number. That is the only formulation the defect cannot
walk out of.
"""

from __future__ import annotations

import colorsys  # noqa: F401  (kept for future palette work)
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STYLESHEET = REPO_ROOT / "src" / "antibioticmech" / "templates" / "style.css"
RENDERED = REPO_ROOT / "pages" / "style.css"

AA_BODY_TEXT = 4.5

DARK_BLOCKS = (':root:not([data-theme="light"])', ':root[data-theme="dark"]')


def _relative_luminance(colour: str) -> float:
    colour = colour.lstrip("#")
    channels = [int(colour[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(a: str, b: str) -> float:
    la, lb = _relative_luminance(a), _relative_luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def _rules(css: str) -> list[tuple[str, str]]:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    return [(sel.strip(), body) for sel, body in re.findall(r"([^{}]+)\{([^}]*)\}", css)]


def _tokens(rules, headers) -> dict[str, str]:
    """Every declaration from EVERY matching block, in source order.

    `:root` is opened twice in this stylesheet, and reading only the first let a
    later redefinition win the cascade unseen.
    """
    out: dict[str, str] = {}
    for selector, body in rules:
        if selector in headers:
            out.update(dict(re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", body)))
    return out


def _resolve(value: str | None, tokens: dict[str, str], depth: int = 0) -> str | None:
    """A colour literal, following var() chains. None when not a plain colour."""
    value = (value or "").strip()
    chained = re.fullmatch(r"var\((--[\w-]+)\)", value)
    if chained and depth < 6:
        return _resolve(tokens.get(chained.group(1)), tokens, depth + 1)
    rgb = re.match(r"rgba?\(\s*(\d+)[\s,]+(\d+)[\s,]+(\d+)", value)
    if rgb:
        return "#" + "".join(f"{int(g):02x}" for g in rgb.groups())
    hexed = re.match(r"#([0-9a-fA-F]{3,6})\b", value)
    if hexed:
        digits = hexed.group(1)
        return "#" + ("".join(c * 2 for c in digits) if len(digits) == 3 else digits[:6])
    return None


def _declaration(body: str, prop: str) -> str | None:
    found = re.search(rf"(?:^|;)\s*{prop}\s*:\s*([^;]+)", body)
    return found.group(1) if found else None


def _themes():
    rules = _rules(STYLESHEET.read_text(encoding="utf-8"))
    light = _tokens(rules, {":root"})
    dark = {**light, **_tokens(rules, set(DARK_BLOCKS))}
    return rules, {"light": light, "dark": dark}


def _background_for(selector: str, body: str, rules, tokens) -> str | None:
    """A rule's own background, else its base selector's, else the page.

    `.button-link:hover` sets only `color`; its background comes from
    `.button-link`. Resolving that to the page background invented a 1.34:1
    failure that does not exist on screen.
    """
    own = _resolve(_declaration(body, "background(?:-color)?"), tokens)
    if own:
        return own
    base = re.sub(r"::?[a-z-]+(\([^)]*\))?", "", selector).strip()
    if base and base != selector:
        for other_sel, other_body in rules:
            if other_sel == base:
                inherited = _resolve(_declaration(other_body, "background(?:-color)?"), tokens)
                if inherited:
                    return inherited
    return _resolve(tokens.get("--page") or tokens.get("--bg"), tokens)


def test_every_rule_renders_readable_text_in_both_themes():
    """Resolve each rule's colour pair through the cascade and check the number.

    Not "is this declaration shaped correctly" — that is what the previous guard
    asked, and rewriting the declaration walked straight out of it. A browser
    resolves tokens; so does this.
    """
    rules, themes = _themes()
    failures = []
    for selector, body in rules:
        if selector.startswith((":root", "@", "body")):
            continue
        text_decl = _declaration(body, "color")
        if not text_decl:
            continue
        for theme, tokens in themes.items():
            text = _resolve(text_decl, tokens)
            back = _background_for(selector, body, rules, tokens)
            if not text or not back:
                continue
            ratio = contrast(text, back)
            if ratio < AA_BODY_TEXT:
                failures.append(f"{selector} [{theme}] {text} on {back} = {ratio:.2f}:1")
    assert failures == [], failures


def test_the_map_tooltip_specifically_survives_a_rewrite():
    """The reported defect, pinned to the RULE rather than to its tokens.

    Restoring `color: var(--bg)` on `.map-tooltip` reproduces 1.01:1 exactly.
    The general test above catches it, and so does this: it is named separately
    because this is the pair a user actually reported, and a future refactor
    that quietly drops the tooltip from the general sweep should still fail here.
    """
    rules, themes = _themes()
    tooltip = [(s, b) for s, b in rules if s == ".map-tooltip"]
    assert tooltip, ".map-tooltip is gone; if it was renamed, rename it here too"
    selector, body = tooltip[0]
    for theme, tokens in themes.items():
        text = _resolve(_declaration(body, "color"), tokens)
        back = _background_for(selector, body, rules, tokens)
        assert text and back, f"{theme}: tooltip colours no longer resolve"
        ratio = contrast(text, back)
        assert ratio >= AA_BODY_TEXT, f"{theme}: tooltip text is {ratio:.2f}:1 on its own surface"


def test_the_rendered_stylesheet_matches_the_template():
    """A fix that never reaches pages/ leaves the live site broken while every
    other test passes, because they all read the template."""
    assert RENDERED.read_text(encoding="utf-8") == STYLESHEET.read_text(encoding="utf-8")
