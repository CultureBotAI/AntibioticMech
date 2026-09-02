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


def test_the_map_tooltip_is_readable_in_both_themes():
    """The specific pair that broke, checked as a number rather than a rule.

    4.5:1 is the WCAG AA threshold for body text. The broken pairing scored
    1.01:1 in dark mode and 16.45:1 in light, so a rule-shaped test that only
    looked at one theme would have passed.
    """
    css = STYLESHEET.read_text(encoding="utf-8")
    tooltip = next(body for sel, body in _rules(css) if sel == ".map-tooltip")
    text = re.search(r"color\s*:\s*(#[0-9a-fA-F]{3,8})", tooltip)
    assert text, "the tooltip's text colour is no longer a literal; re-check both themes"
    # Its background is an rgb() with alpha over the page; the opaque base is
    # what the text sits on.
    assert contrast(text.group(1), "#17202a") >= 4.5, contrast(text.group(1), "#17202a")
