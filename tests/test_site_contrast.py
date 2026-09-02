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
    """Every style rule, with `@media` blocks flattened to top level.

    The previous split-on-`}` version merged an at-rule's opener into its first
    nested selector and left the rest looking like top-level rules, so all but
    the first rule of every `@media` block was invisible to the sweep. Nothing
    colour-bearing lived there, but a responsive override would have landed in
    the gap silently.
    """
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out: list[tuple[str, str]] = []
    depth, start, header = 0, 0, ""
    i = 0
    while i < len(css):
        ch = css[i]
        if ch == "{":
            if depth == 0:
                header = css[start:i].strip()
                body_start = i + 1
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                body = css[body_start:i]
                if header.startswith("@"):
                    out.extend(_rules(body))
                else:
                    out.append((header, body))
                start = i + 1
        i += 1
    return out


COMBINATORS = re.compile(r"\s*[>+~]\s*|\s+")


def _compounds(selector: str) -> list[str]:
    return [p for p in COMBINATORS.split(selector.strip()) if p]


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


def _colour_stops(value: str | None, tokens: dict[str, str]) -> list[str]:
    """Every colour a background declaration can paint.

    One for a flat colour; each stop for a gradient. A gradient interpolates
    between its stops, so the stops bound every intermediate position — the
    masthead's `linear-gradient(135deg, #5D5641, #55514A)` was unresolvable and
    therefore unchecked, which is how 3.11:1 nav links survived the sweep.
    """
    if not value:
        return []
    flat = _resolve(value, tokens)
    if flat:
        return [flat]
    if "gradient(" not in value:
        return []
    stops = []
    for piece in re.findall(r"var\(--[\w-]+\)|#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)", value):
        resolved = _resolve(piece, tokens)
        if resolved:
            stops.append(resolved)
    return stops


def _declaration(body: str, prop: str) -> str | None:
    found = re.search(rf"(?:^|;)\s*{prop}\s*:\s*([^;]+)", body)
    return found.group(1) if found else None


def _is_token_block(selector: str) -> bool:
    """A block that only declares tokens — `:root`, or a bare theme block.

    Skipping anything merely STARTING with `:root` also skipped every
    dark-block-scoped descendant rule (`:root[data-theme="dark"] .foo`), which
    is exactly where a theme-specific colour override lives.
    """
    return len(_compounds(selector)) == 1 and selector.startswith(":root")


def _applies_in(selector: str, theme: str) -> bool:
    """A dark-block-scoped rule renders in dark mode only."""
    return theme == "dark" or not selector.startswith(DARK_BLOCKS)


def _themes():
    rules = _rules(STYLESHEET.read_text(encoding="utf-8"))
    light = _tokens(rules, {":root"})
    dark = {**light, **_tokens(rules, set(DARK_BLOCKS))}
    return rules, {"light": light, "dark": dark}


def _ancestor_backgrounds(selector: str, rules, tokens, theme: str) -> list[str]:
    """The background painted by the nearest ancestor that paints one.

    `header.site nav a` sets a colour and no background, so it was measured
    against the page — a surface it never renders on. It actually sits on
    `.wrap > header.site`, whose gradient both dark blocks override with a
    literal. That is the pattern this file exists to ban, one layer up.
    """
    ancestors = _compounds(selector)[:-1]
    for ancestor in reversed(ancestors):          # nearest ancestor wins
        hits: list[tuple[str, list[str]]] = []
        for other_sel, other_body in rules:
            parts = _compounds(other_sel)
            if not parts or parts[-1] != ancestor:
                continue
            rule_theme = "dark" if other_sel.startswith(DARK_BLOCKS) else "light"
            if rule_theme == "dark" and theme != "dark":
                continue
            stops = _colour_stops(_declaration(other_body, "background(?:-color)?"), tokens)
            if stops:
                hits.append((rule_theme, stops))
        if hits:
            # A dark-block rule overrides the base rule it restates.
            dark = [stops for rule_theme, stops in hits if rule_theme == "dark"]
            if theme == "dark" and dark:
                return dark[-1]
            return hits[-1][1]
    return []


def _backgrounds_for(selector, body, rules, tokens, theme) -> list[str]:
    """Own background, else the base selector's, else an ancestor's, else the page.

    Returns every surface the text can land on, because a gradient is several.
    `.button-link:hover` sets only `color`; its background comes from
    `.button-link`. Resolving that to the page background invented a 1.34:1
    failure that does not exist on screen.
    """
    own = _colour_stops(_declaration(body, "background(?:-color)?"), tokens)
    if own:
        return own
    base = re.sub(r"::?[a-z-]+(\([^)]*\))?", "", selector).strip()
    if base and base != selector:
        for other_sel, other_body in rules:
            if other_sel == base:
                inherited = _colour_stops(
                    _declaration(other_body, "background(?:-color)?"), tokens)
                if inherited:
                    return inherited
    ancestral = _ancestor_backgrounds(selector, rules, tokens, theme)
    if ancestral:
        return ancestral
    page = _resolve(tokens.get("--page") or tokens.get("--bg"), tokens)
    return [page] if page else []


def test_every_rule_renders_readable_text_in_both_themes():
    """Resolve each rule's colour pair through the cascade and check the number.

    Not "is this declaration shaped correctly" — that is what the previous guard
    asked, and rewriting the declaration walked straight out of it. A browser
    resolves tokens; so does this.
    """
    rules, themes = _themes()
    failures = []
    for selector, body in rules:
        if _is_token_block(selector) or selector.startswith(("@", "body")):
            continue
        text_decl = _declaration(body, "color")
        if not text_decl:
            continue
        for theme, tokens in themes.items():
            if not _applies_in(selector, theme):
                continue
            text = _resolve(text_decl, tokens)
            if not text:
                continue
            for back in _backgrounds_for(selector, body, rules, tokens, theme):
                ratio = contrast(text, back)
                if ratio < AA_BODY_TEXT:
                    failures.append(
                        f"{selector} [{theme}] {text} on {back} = {ratio:.2f}:1")
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
        backs = _backgrounds_for(selector, body, rules, tokens, theme)
        assert text and backs, f"{theme}: tooltip colours no longer resolve"
        for back in backs:
            ratio = contrast(text, back)
            assert ratio >= AA_BODY_TEXT, (
                f"{theme}: tooltip text is {ratio:.2f}:1 on its own surface")


def test_the_masthead_nav_is_readable_on_its_gradient():
    """Text over an ANCESTOR's background, which is a gradient, not a colour.

    Both blind spots at once, and both had to close before the pair could be
    measured: `header.site nav a` sets no background of its own, and the one it
    inherits from `.wrap > header.site` is a `linear-gradient` the dark blocks
    repaint with a fixed literal. Unmeasured, the nav read 3.11:1 (#156).

    A gradient interpolates between its stops, so checking the stops bounds
    every position along it.
    """
    rules, themes = _themes()
    nav = [(s, b) for s, b in rules if s == "header.site nav a"]
    assert nav, "header.site nav a is gone; if it was renamed, rename it here too"
    selector, body = nav[0]
    for theme, tokens in themes.items():
        text = _resolve(_declaration(body, "color"), tokens)
        stops = _backgrounds_for(selector, body, rules, tokens, theme)
        assert text, f"{theme}: nav colour no longer resolves"
        assert len(stops) == 2, (
            f"{theme}: expected the masthead's two gradient stops, got {stops}. "
            "Measuring the nav against the page background is the bug in #156.")
        for stop in stops:
            ratio = contrast(text, stop)
            assert ratio >= AA_BODY_TEXT, (
                f"{theme}: masthead nav is {ratio:.2f}:1 on gradient stop {stop}")


def test_the_rendered_stylesheet_matches_the_template():
    """A fix that never reaches pages/ leaves the live site broken while every
    other test passes, because they all read the template."""
    assert RENDERED.read_text(encoding="utf-8") == STYLESHEET.read_text(encoding="utf-8")
