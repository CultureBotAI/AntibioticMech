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


ROOT_FONT_PX = 16


def _px(value: str) -> float:
    """A CSS length in pixels, or a loud failure.

    Stripping non-digits read `40rem` as 40px — a sixteenth of its real width.
    That is silent twice over: the rule is judged not to apply where a browser
    applies it, and `_states` enumerates 39/40/41 instead of either side of the
    real boundary, so the coverage simply is not there and nothing says so.
    """
    match = re.fullmatch(r"\s*([0-9.]+)\s*(px|r?em)?\s*", value)
    if not match:
        raise ValueError(f"unrecognised length in a media query: {value!r}")
    amount = float(match.group(1))
    return amount * ROOT_FONT_PX if match.group(2) in ("rem", "em") else amount


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


def _alpha(value: str | None, tokens: dict[str, str], depth: int = 0) -> float:
    """The alpha of a colour value, following var() chains. 1.0 when opaque."""
    value = (value or "").strip()
    chained = re.fullmatch(r"var\((--[\w-]+)\)", value)
    if chained and depth < 6:
        return _alpha(tokens.get(chained.group(1)), tokens, depth + 1)
    slashed = re.match(r"rgba?\([^)]*?/\s*([0-9.]+%?)\s*\)", value)
    if slashed:
        raw = slashed.group(1)
        return float(raw.rstrip("%")) / (100 if raw.endswith("%") else 1)
    commaed = re.match(r"rgba\(\s*[\d.]+\s*,\s*[\d.]+\s*,\s*[\d.]+\s*,\s*([0-9.]+)", value)
    return float(commaed.group(1)) if commaed else 1.0


def _over(colour: str, backdrop: str, alpha: float) -> str:
    top = [int(colour.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    under = [int(backdrop.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    return "#" + "".join(f"{round(alpha * t + (1 - alpha) * u):02x}"
                         for t, u in zip(top, under, strict=True))


def _bound(colour: str, alpha: float) -> list[str]:
    """What a translucent surface can actually render as.

    Alpha was discarded, so `rgb(23 32 42 / .94)` — the tooltip's own background,
    over a map canvas whose pixels CSS cannot know — was measured as if opaque.
    A number that is close to the rendered one is still not it, and reporting
    those is the habit this whole file exists to break (#161).

    The backdrop is unknowable, but the result is not unbounded: it lies between
    the colour composited over white and over black. Requiring the ratio to hold
    at both ends holds it for every backdrop. Text alpha is NOT modelled — a
    translucent glyph over an unknown backdrop has no such clean bound, and
    nothing here uses one.
    """
    return [colour] if alpha >= 1 else [_over(colour, "#ffffff", alpha),
                                        _over(colour, "#000000", alpha)]


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
        return _bound(flat, _alpha(value, tokens))
    if "gradient(" not in value:
        return []
    stops = []
    for piece in re.findall(r"var\(--[\w-]+\)|#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)", value):
        resolved = _resolve(piece, tokens)
        if resolved:
            stops.extend(_bound(resolved, _alpha(piece, tokens)))
    return stops


def _declaration(body: str, prop: str) -> str | None:
    found = re.search(rf"(?:^|;)\s*{prop}\s*:\s*([^;]+)", body)
    return found.group(1) if found else None


SPECIFIC = re.compile(r"#[\w-]+|\.[\w-]+|\[[^\]]*\]|:[\w-]+")


def _specificity(selector: str) -> int:
    """How hard a selector competes, near enough for this stylesheet.

    Source order alone decides only among EQUAL specificity.
    `:root[data-theme="dark"]` beats a plain `:root` declared after it, so
    resolving by position let a later low-specificity block override a dark one.
    That direction masks: a good value in the later block hid a broken value in
    the dark block, reproducing the original tooltip defect at 1.01:1 while
    every test passed (#158).

    Ids, classes, attributes and pseudo-classes are counted together rather than
    in CSS's three tiers. Full specificity would need a real selector parser and
    would not change any verdict here.
    """
    return len(SPECIFIC.findall(re.sub(r"::[\w-]+", "", selector)))


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
    token_wins: dict[str, tuple[int, int]] = {}
    style_wins: dict[tuple[str, str], tuple[int, int]] = {}
    tokens: dict[str, str] = {}
    styles: dict[str, dict[str, str]] = {}
    for position, rule in enumerate(rules):
        if not _holds(rule, state):
            continue
        rank = (_specificity(rule.selector), position)
        key = _key(rule.selector)
        if _is_token_block(key):
            for name, value in re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", rule.body):
                if rank >= token_wins.get(name, (-1, -1)):
                    token_wins[name] = rank
                    tokens[name] = value
            continue
        for prop, name in (("color", "color"), ("background(?:-color)?", "background")):
            value = _declaration(rule.body, prop)
            if value and rank >= style_wins.get((key, name), (-1, -1)):
                style_wins[(key, name)] = rank
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


def _failures(css: str | None = None):
    rules = _rules(css if css is not None else STYLESHEET.read_text(encoding="utf-8"))
    seen, out = set(), []
    for state in _states(rules):
        tokens, styles = _cascade(rules, state)
        for key, declarations in styles.items():
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
        # Not `page not in surfaces`: the light gradient's own second stop IS
        # --page (--pastel-b is the same sand), so the nav legitimately renders
        # on that colour at one end. What must not happen is resolving to the
        # page ALONE, which is the fallback that means no ancestor was found.
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


def test_a_conditional_surface_is_credited_only_where_it_applies():
    """A `min-width` background must count in the states it covers, and only those.

    Both directions, because either alone is satisfied by a checker that simply
    DROPS min-width rules. The first is the masking shape — text whose only
    ancestor surface sits behind the query, so it falls back to the page below
    the breakpoint and is unreadable there while being fine above it. The second
    is its inverse, readable on the page and broken on the conditional surface.
    One fails narrow, one fails wide, from the same breakpoint. A checker that
    ignored the query would fail the first for the wrong reason and would not
    fail the second at all.

    The `edge - 1` width is what makes the first land on the boundary rather
    than at whatever enumerated width happens to sit below it.
    """
    css = """
    :root { --page: #E4DED3; }
    .masked .text { color: #E4DED3; }
    .inverse .text2 { color: #1a1d21; }
    @media (min-width: 900px) {
      .masked { background: #17150f; }
      .inverse { background: #17150f; }
    }
    """
    rules = _rules(css)
    assert 899 in {state.width for state in _states(rules)}, (
        "the state just inside a boundary is where a conditional surface's "
        "absence shows; enumerating only the breakpoint itself would miss it")

    def pair(selector, width):
        tokens, styles = _cascade(rules, State(False, None, width))
        text = _resolve(styles[selector]["color"], tokens)
        return contrast(text, _surface(selector, tokens, styles)[0])

    assert pair(".masked .text", 899) < AA_BODY_TEXT, "masked: falls back to the page"
    assert pair(".masked .text", 900) >= AA_BODY_TEXT, "masked: the surface applies here"
    assert pair(".inverse .text2", 899) >= AA_BODY_TEXT, "inverse: the page is fine"
    assert pair(".inverse .text2", 900) < AA_BODY_TEXT, (
        "inverse: the conditional surface must be consulted where it applies, "
        "not dropped")


def test_the_sweep_covers_body_and_selectors_that_merely_start_with_it():
    """`body` was skipped outright, and so was anything sharing its first letters.

    It is the one selector that must never be skipped: it sets the page's
    default pair, which every element inheriting from it renders in. The guard
    was also a prefix match where an exact match was meant, so `body .card`,
    `body.wide` and even `bodyguard .x` were dropped with no drop in reported
    coverage (#160).
    """
    css = """
    :root { --page: #E4DED3; --fg: #1a1d21; }
    body { background: var(--page); color: #E4DED3; }
    body .card { background: #ffffff; color: #f4f6f8; }
    body.wide { background: #ffffff; color: #fdfdfd; }
    """
    reported = " ".join(_failures(css))
    for selector in ("body", "body .card", "body.wide"):
        assert selector in reported, f"{selector} is not being swept: {reported}"


def test_specificity_outranks_source_order():
    """A later declaration wins only among EQUAL specificity.

    `:root[data-theme="dark"]` beats a plain `:root` declared after it. Resolving
    by position alone let the later block win, and that direction MASKS: a good
    value in the later block hid a broken one in the dark block, reproducing the
    original tooltip defect at 1.01:1 with every test green (#158).
    """
    css = """
    :root { --page: #ffffff; --fg: #1a1d21; }
    :root[data-theme="dark"] { --page: #17202a; --fg: #211e16; }
    :root { --fg: #f0ece0; }
    .x { color: var(--fg); }
    """
    tokens, styles = _cascade(_rules(css), State(False, "dark", WIDEST))
    text = _resolve(styles[".x"]["color"], tokens)
    assert text == "#211e16", (
        "the dark block is more specific and wins despite being declared first; "
        "taking the later value hides whatever the dark block actually renders")
    assert contrast(text, _surface(".x", tokens, styles)[0]) < AA_BODY_TEXT

    assert _specificity(':root[data-theme="dark"]') > _specificity(":root")
    assert _specificity(".a.b") > _specificity(".a")


def test_a_rem_breakpoint_is_converted_not_stripped():
    """`40rem` is 640px, not 40px.

    Stripping non-digits was silent twice: the rule was judged not to apply
    where a browser applies it, and `_states` enumerated 39/40/41 rather than
    either side of the real boundary, so the coverage was absent with nothing
    saying so (#159).
    """
    assert _px("40rem") == 640 and _px("850px") == 850 and _px("40em") == 640

    rule = _rules("@media (max-width: 40rem) { .a { color: #000; } }")[0]
    assert _holds(rule, State(False, None, 600))
    assert not _holds(rule, State(False, None, 641))
    assert {639, 640, 641} <= {state.width for state in _states([rule])}

    try:
        _px("40vw")
    except ValueError:
        return
    raise AssertionError("an unmodelled unit must fail loudly, not yield a number")


def test_a_translucent_surface_is_bounded_not_treated_as_opaque():
    """Alpha is real; discarding it reports a number the page never renders.

    The backdrop of `rgb(23 32 42 / .94)` is a map canvas CSS cannot know, but
    the composite is bounded by that colour over white and over black. Requiring
    the ratio at both ends holds it for any backdrop (#161).
    """
    assert _alpha("rgb(23 32 42 / .94)", {}) == 0.94
    assert _alpha("rgba(0, 0, 0, .12)", {}) == 0.12
    assert _alpha("#17202a", {}) == 1.0

    bounds = _colour_stops("rgb(23 32 42 / .94)", {})
    assert bounds == ["#252d37", "#161e27"], bounds
    assert bounds[0] != "#17202a", (
        "treating the translucent surface as opaque is the thing being fixed")
    assert _colour_stops("#17202a", {}) == ["#17202a"], "opaque colours stay single"

    half = _colour_stops("rgb(128 128 128 / .5)", {})
    assert contrast("#767676", half[0]) < AA_BODY_TEXT, (
        "a pair that fails over one extreme must fail, not be averaged away")


def test_the_rendered_stylesheet_matches_the_template():
    """A fix that never reaches pages/ leaves the live site broken while every
    other test passes, because they all read the template."""
    assert RENDERED.read_text(encoding="utf-8") == STYLESHEET.read_text(encoding="utf-8")
