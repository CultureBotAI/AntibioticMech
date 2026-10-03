"""Shared minimum assay-context gate; not a certification of submitted methods."""

import re

# Generic vessels and local/unknown method labels cannot identify an assay.
UNINFORMATIVE_CONTEXT = frozenset({
    "", "0", "na", "none", "null", "missing", "unknown", "unspecified",
    "notapplicable", "notavailable", "notcollected", "notprovided", "notreported",
    "other", "inhouse", "96wellplate",
})


def has_informative_assay_context(*values: str) -> bool:
    return any(
        re.sub(r"[^a-z0-9]", "", value.casefold()) not in UNINFORMATIVE_CONTEXT
        for value in values
    )
