"""Colour pairs the two themes cannot both satisfy.

The map tooltip painted its own dark background and took its text colour from
`var(--bg)`, the PAGE background. In light mode that is white on dark and reads
fine; in dark mode it is #211e16 on #17202a — a contrast ratio of 1.01:1, which
renders as a visible box containing text nobody can see. Reported as "the popups
on hover are empty": not empty, unreadable, and only in one theme.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STYLESHEET = REPO_ROOT / "src" / "antibioticmech" / "templates" / "style.css"


def _relative_luminance(hex_colour: str) -> float:
    hex_colour = hex_colour.lstrip("#")
    if len(hex_colour) == 3:
        hex_colour = "".join(c * 2 for c in hex_colour)
    channels = [int(hex_colour[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(a: str, b: str) -> float:
    la, lb = _relative_luminance(a), _relative_luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def _rules(css: str):
    """(selector, declarations), with comments stripped.

    Stripping matters: an explanatory comment quoting the very pattern being
    banned made an earlier version of this scan report its own prose.
    """
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    return [(sel.strip(), body) for sel, body in re.findall(r"([^{}]+)\{([^}]*)\}", css)]


def test_no_component_paints_its_own_background_and_borrows_the_theme_for_text():
    """A component that sets a literal background has left the theme's colour
    system, so its text cannot come from `var(--bg)` or `var(--fg)`.

    Those variables flip between light and dark; a fixed background does not.
    One of the two themes is then guaranteed to put near-identical colours
    together, and the failure is invisible to anyone testing in the other.
    """
    offenders = []
    for selector, body in _rules(STYLESHEET.read_text(encoding="utf-8")):
        literal_bg = re.search(
            r"background(?:-color)?\s*:\s*(#[0-9a-fA-F]{3,8}|rgb\(|hsl\()", body)
        themed_text = re.search(r"color\s*:\s*var\(--(bg|fg)\)", body)
        if literal_bg and themed_text:
            offenders.append(f"{selector}: literal background with color: var(--{themed_text.group(1)})")
    assert offenders == [], offenders


def _token_block(css: str, header: str) -> dict[str, str]:
    start = css.index(header)
    body = css[start + len(header):css.index("}", start)]
    return dict(re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", body))


def test_the_map_tooltip_is_readable_in_every_theme_block():
    """The specific pair that broke, resolved through the tokens and checked as
    a NUMBER in each theme block.

    4.5:1 is the WCAG AA threshold for body text. The broken pairing scored
    1.01:1 in dark and 16.45:1 in light, so any check that looked at one theme
    would have passed — which is how it shipped.

    Reading the tokens rather than a literal also means this keeps working after
    the stylesheet contract required the colours to be tokenised, and it fails
    if a future theme block gives the tooltip a different surface.
    """
    css = STYLESHEET.read_text(encoding="utf-8")
    blocks = [":root {", ':root:not([data-theme="light"]) {', ':root[data-theme="dark"] {']
    checked = 0
    for header in blocks:
        if header not in css:
            continue
        tokens = _token_block(css, header)
        fg, bg = tokens.get("--tooltip-fg"), tokens.get("--tooltip-bg")
        assert fg and bg, f"{header} does not declare both tooltip tokens"
        # The surface is rgb() with alpha; its opaque base is what text sits on.
        rgb = re.search(r"rgb\(\s*(\d+)\s+(\d+)\s+(\d+)", bg)
        assert rgb, f"{header}: --tooltip-bg is no longer an rgb() literal"
        base = "#" + "".join(f"{int(g):02x}" for g in rgb.groups())
        ratio = contrast(fg.strip(), base)
        assert ratio >= 4.5, f"{header}: tooltip text on its own surface is {ratio:.2f}:1"
        checked += 1
    assert checked >= 2, "expected the light block and at least one dark block"
