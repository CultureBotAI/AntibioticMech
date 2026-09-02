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

EVERY LATER MISTAKE HERE WAS THE SAME ONE: a number that describes no state the
page can actually be in. Measuring text against the page when it sits on an
ancestor. Measuring against a gradient's absence instead of its stops. Reading a
rule's theme off its selector when the theme lived in an `@media` condition.
And, last, printing a condition beside a ratio without ever requiring the
surface's condition and the text's condition to be compatible — which pairs
wide-viewport text with a narrow-viewport background, two things never on screen
together.

So this does not pair declarations. It enumerates the STATES the page can be in
— each theme crossed with each viewport width where a breakpoint changes
something — resolves the cascade within one state down to a single colour and a
single background per selector, and checks that pair. Cross-state pairs cannot be
constructed, rather than being filtered out afterwards. The theme axis is not a
special case: `prefers-color-scheme` is one condition among the others.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import NamedTuple

REPO_ROOT = Path(__file__).resolve().parent.parent
STYLESHEET = REPO_ROOT / "src" / "antibioticmech" / "templates" / "style.css"
RENDERED = REPO_ROOT / "pages" / "style.css"

AA_BODY_TEXT = 4.5

DARK_BLOCKS = (':root:not([data-theme="light"])', ':root[data-theme="dark"]')
WIDEST = 1440


class Rule(NamedTuple):
    """A style rule plus the `@media` conditions it is nested inside."""

    selector: str
    body: str
    media: tuple[str, ...] = ()


class State(NamedTuple):
    """One way the page can actually be on screen.

    THE THEME IS TWO INDEPENDENT INPUTS, not one. The OS preference drives
    `@media (prefers-color-scheme: dark)`; the toggle writes `data-theme` and
    drives the `:root[...]` blocks. Collapsing them into a single "dark" hid a
    real drift: a token altered inside the media block was overridden by the
    toggle block declared later, so the OS-preference reader — who never touches
    the toggle — saw the broken value while the check saw the good one.

    It also makes the fourth combination visible. OS dark with the toggle set to
    light is exactly what `:root:not([data-theme="light"])` exists to exclude.
    """

    os_dark: bool
    toggle: str | None
    width: int

    def __str__(self) -> str:
        return (f"os={'dark' if self.os_dark else 'light'} "
                f"toggle={self.toggle or 'unset'} @{self.width}px")


def _relative_luminance(colour: str) -> float:
    colour = colour.lstrip("#")
    channels = [int(colour[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(a: str, b: str) -> float:
    la, lb = _relative_luminance(a), _relative_luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def _rules(css: str, conditions: tuple[str, ...] = ()) -> list[Rule]:
    """Every style rule, with its enclosing `@media` conditions attached.

    The previous split-on-`}` version merged an at-rule's opener into its first
    nested selector and left the rest looking like top-level rules, so all but
    the first rule of every `@media` block was invisible — including the whole
    `prefers-color-scheme: dark` token block, which meant the OS-preference
    theme was never read at all.
    """
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out: list[Rule] = []
    depth, start, header, body_start = 0, 0, "", 0
    for i, ch in enumerate(css):
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
                    out.extend(_rules(body, conditions + (header,)))
                else:
                    out.append(Rule(header, body, conditions))
                start = i + 1
    return out


COMBINATORS = re.compile(r"\s*[>+~]\s*|\s+")
FEATURE = re.compile(r"\(\s*([\w-]+)\s*:\s*([^)]+?)\s*\)")


def _compounds(selector: str) -> list[str]:
    return [p for p in COMBINATORS.split(selector.strip()) if p]


def _px(value: str) -> float:
    return float(re.sub(r"[^0-9.]", "", value))


def _holds(rule: Rule, state: State) -> bool:
    """Does this rule render in this state?

    Conditions are evaluated, not pattern-matched. A feature this does not model
    (`prefers-reduced-motion`, say) is treated as satisfiable, so its rules are
    still checked rather than silently dropped.
    """
    for condition in rule.media:
        for feature, value in FEATURE.findall(condition):
            if feature == "prefers-color-scheme" and (value == "dark") != state.os_dark:
                return False
            if feature == "max-width" and state.width > _px(value):
                return False
            if feature == "min-width" and state.width < _px(value):
                return False
    if rule.selector.startswith(':root:not([data-theme="light"])'):
        return state.toggle != "light"
    if rule.selector.startswith(':root[data-theme="dark"]'):
        return state.toggle == "dark"
    return True


def _states(rules: list[Rule]) -> list[State]:
    """Each theme crossed with each width where a breakpoint changes something.

    Both sides of every boundary, since `max-width: 850px` includes 850 and
    excludes 851, and a stylesheet can disagree with itself across exactly that
    one pixel.
    """
    breakpoints = {
        int(_px(value))
        for rule in rules for condition in rule.media
        for feature, value in FEATURE.findall(condition)
        if feature in ("max-width", "min-width")
    }
    widths = {WIDEST}
    for edge in breakpoints:
        widths.update({edge, edge + 1, max(edge - 1, 1)})
    # Default themes first and widest first, so a failure reported once names the
    # state most readers are in rather than a corner that happens to sort first.
    themes = [(False, None), (True, None), (False, "dark"), (True, "light"),
              (True, "dark"), (False, "light")]
    return [State(os_dark, toggle, width)
            for os_dark, toggle in themes
            for width in sorted(widths, reverse=True)]


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
    return [c for c in (_resolve(piece, tokens) for piece in
                        re.findall(r"var\(--[\w-]+\)|#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)", value))
            if c]


def _declaration(body: str, prop: str) -> str | None:
    found = re.search(rf"(?:^|;)\s*{prop}\s*:\s*([^;]+)", body)
    return found.group(1) if found else None


def _key(selector: str) -> str:
    """A selector with any dark-theme scoping prefix removed.

    `:root[data-theme="dark"] .wrap > header.site` and `.wrap > header.site` are
    the same element; the first is the second's override. Collapsing them lets
    plain source order decide the cascade instead of a special case.
    """
    for prefix in DARK_BLOCKS:
        if selector.startswith(prefix):
            return selector[len(prefix):].strip()
    return selector


def _is_token_block(key: str) -> bool:
    """`:root`, or a dark block that reduced to nothing once its prefix went."""
    return key == "" or (len(_compounds(key)) == 1 and key.startswith(":root"))


def _cascade(rules: list[Rule], state: State):
    """Resolve the whole stylesheet down to what one state renders.

    One colour and one background per selector — the last applicable
    declaration, which is what source order means for equal specificity. There
    is nothing left to cross-pair.
    """
    tokens: dict[str, str] = {}
    styles: dict[str, dict[str, str]] = {}
    for rule in rules:
        if not _holds(rule, state):
            continue
        key = _key(rule.selector)
        if _is_token_block(key):
            tokens.update(dict(re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", rule.body)))
            continue
        for prop, name in (("color", "color"), ("background(?:-color)?", "background")):
            value = _declaration(rule.body, prop)
            if value:
                styles.setdefault(key, {})[name] = value
    return tokens, styles


def _surface(key: str, tokens, styles) -> list[str]:
    """What is painted behind this selector's text, within one state.

    Own background, else its base selector's, else the nearest painting
    ancestor's, else the page. `.button-link:hover` sets only `color`; its
    background comes from `.button-link`, and resolving that to the page
    invented a 1.34:1 failure that does not exist on screen. `header.site nav a`
    sets neither, and sits on the masthead gradient (#156).
    """
    own = _colour_stops(styles.get(key, {}).get("background"), tokens)
    if own:
        return own
    base = re.sub(r"::?[a-z-]+(\([^)]*\))?", "", key).strip()
    if base and base != key:
        inherited = _colour_stops(styles.get(base, {}).get("background"), tokens)
        if inherited:
            return inherited
    for ancestor in reversed(_compounds(key)[:-1]):
        painted: list[str] = []
        for other, declarations in styles.items():
            parts = _compounds(other)
            if parts and parts[-1] == ancestor:
                stops = _colour_stops(declarations.get("background"), tokens)
                if stops:
                    painted = stops
        if painted:
            return painted
    page = _resolve(tokens.get("--page") or tokens.get("--bg"), tokens)
    return [page] if page else []


def _failures():
    rules = _rules(STYLESHEET.read_text(encoding="utf-8"))
    seen, out = set(), []
    for state in _states(rules):
        tokens, styles = _cascade(rules, state)
        for key, declarations in styles.items():
            if key.startswith(("@", "body")):
                continue
            text = _resolve(declarations.get("color"), tokens)
            if not text:
                continue
            for back in _surface(key, tokens, styles):
                ratio = contrast(text, back)
                if ratio >= AA_BODY_TEXT or (key, text, back) in seen:
                    continue
                seen.add((key, text, back))
                out.append(f"{key} [{state}] {text} on {back} = {ratio:.2f}:1")
    return out


def test_every_rule_renders_readable_text_in_every_state():
    """Resolve each state's colour pair through the cascade and check the number.

    Not "is this declaration shaped correctly" — that is what the first guard
    asked, and rewriting the declaration walked straight out of it. A browser
    resolves tokens within a state; so does this.
    """
    assert _failures() == []


def _pair(selector: str, state: State):
    rules = _rules(STYLESHEET.read_text(encoding="utf-8"))
    tokens, styles = _cascade(rules, state)
    assert selector in styles, f"{selector} is gone; if it was renamed, rename it here too"
    return _resolve(styles[selector].get("color"), tokens), _surface(selector, tokens, styles)


def test_the_map_tooltip_specifically_survives_a_rewrite():
    """The reported defect, pinned to the RULE rather than to its tokens.

    Restoring `color: var(--bg)` on `.map-tooltip` reproduces 1.01:1 exactly.
    The general test above catches it, and so does this: it is named separately
    because this is the pair a user actually reported, and a future refactor
    that quietly drops the tooltip from the general sweep should still fail here.
    """
    for state in (State(False, None, WIDEST), State(True, None, WIDEST)):
        text, surfaces = _pair(".map-tooltip", state)
        assert text and surfaces, f"{state}: tooltip colours no longer resolve"
        for back in surfaces:
            ratio = contrast(text, back)
            assert ratio >= AA_BODY_TEXT, (
                f"{state}: tooltip text is {ratio:.2f}:1 on its own surface")


def test_the_masthead_nav_is_readable_on_the_surface_it_inherits():
    """Text over an ANCESTOR's background, which is a gradient, not a colour.

    Both blind spots at once, and both had to close before the pair could be
    measured: `header.site nav a` sets no background of its own, and the one it
    inherits from `.wrap > header.site` is a `linear-gradient` the dark blocks
    repaint with a fixed literal. Unmeasured, the nav read 3.11:1 (#156).

    The assertion is that the nav is NOT measured against the page — the actual
    bug — rather than that it finds exactly two stops. Pinning the count made
    the test fail on shape for any added masthead background, before computing a
    single ratio.
    """
    for state in (State(False, None, WIDEST), State(True, None, WIDEST)):
        text, surfaces = _pair("header.site nav a", state)
        tokens, _ = _cascade(_rules(STYLESHEET.read_text(encoding="utf-8")), state)
        page = _resolve(tokens.get("--page") or tokens.get("--bg"), tokens)
        assert text and surfaces, f"{state}: nav colours no longer resolve"
        assert surfaces != [page], (
            f"{state}: the nav resolved to the page background. It renders on the "
            "masthead, and measuring it against the page is the bug in #156.")
        for back in surfaces:
            ratio = contrast(text, back)
            assert ratio >= AA_BODY_TEXT, (
                f"{state}: masthead nav is {ratio:.2f}:1 on {back}")


def test_a_state_pairs_only_colours_that_render_together():
    """Conditions define states; they are not metadata printed beside a ratio.

    A responsive redesign that recolours its text under the SAME query is
    coherent and must stay green. Carrying conditions without matching them
    paired wide text with a narrow background and narrow text with a wide one —
    two things never on screen together, reported as nine failures.
    """
    css = """
    :root { --page: #ffffff; --fg: #1a1d21; }
    .masthead { background: #ffffff; }
    .masthead a { color: #1a1d21; }
    @media (max-width: 850px) {
      .masthead { background: #17150f; }
      .masthead a { color: #f0ece0; }
    }
    """
    rules = _rules(css)
    for width, text, back in ((WIDEST, "#1a1d21", "#ffffff"), (600, "#f0ece0", "#17150f")):
        tokens, styles = _cascade(rules, State(False, None, width))
        assert _resolve(styles[".masthead a"]["color"], tokens) == text
        assert _surface(".masthead a", tokens, styles) == [back]
        assert contrast(text, back) >= AA_BODY_TEXT

    broken = css.replace("      .masthead a { color: #f0ece0; }\n", "")
    tokens, styles = _cascade(_rules(broken), State(False, None, 600))
    assert contrast(_resolve(styles[".masthead a"]["color"], tokens),
                    _surface(".masthead a", tokens, styles)[0]) < AA_BODY_TEXT, (
        "recolouring the text is what makes the redesign coherent; without it "
        "the narrow state really is unreadable and must still fail")


def test_the_two_dark_paths_are_checked_separately():
    """OS-preference dark and toggle dark are different states, not one theme.

    The `:root[data-theme="dark"]` block is declared after the media block and
    restates the same tokens. Treating both as one "dark" let the later block
    override a drifted value in the earlier one — so a token broken for every
    OS-preference reader resolved to the good value here. `_states` therefore
    varies the OS preference and the toggle independently.
    """
    media = _rules(
        '@media (prefers-color-scheme: dark) {'
        ' :root:not([data-theme="light"]) { --x: #111; } }')[0]
    toggle = _rules(':root[data-theme="dark"] { --x: #222; }')[0]

    os_dark_only = State(True, None, WIDEST)
    assert _holds(media, os_dark_only) and not _holds(toggle, os_dark_only), (
        "with the toggle unset, only the media block applies — this is the state "
        "a drift inside it is visible in, and the only one")

    toggled = State(False, "dark", WIDEST)
    assert _holds(toggle, toggled) and not _holds(media, toggled)

    assert not _holds(media, State(True, "light", WIDEST)), (
        'OS dark with the toggle set to light is what :not([data-theme="light"]) '
        "is for; the media block must not apply")


def test_a_media_condition_is_evaluated_not_read_off_the_selector():
    """A rule's theme lives in its condition, not in a prefix an author may omit."""
    dark_by_condition = _rules(
        "@media (prefers-color-scheme: dark) { .card { background: #111; } }")[0]
    assert _holds(dark_by_condition, State(True, None, WIDEST))
    assert not _holds(dark_by_condition, State(False, None, WIDEST))

    narrow = _rules("@media (max-width: 850px) { .card { background: #17150f; } }")[0]
    assert _holds(narrow, State(False, None, 850)) and _holds(narrow, State(True, None, 600))
    assert not _holds(narrow, State(False, None, 851)), "a viewport query restricts width"

    plain = _rules(".card { background: #fff; }")[0]
    assert all(_holds(plain, state) for state in _states([plain]))


def test_the_rendered_stylesheet_matches_the_template():
    """A fix that never reaches pages/ leaves the live site broken while every
    other test passes, because they all read the template."""
    assert RENDERED.read_text(encoding="utf-8") == STYLESHEET.read_text(encoding="utf-8")
