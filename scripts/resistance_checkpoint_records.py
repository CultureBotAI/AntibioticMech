"""Resolve explicit historical research inputs, never the live corpus census."""

import audit_topoisomerase_references as reference

FLUCYTOSINE_PATH = "data/antibiotics/antifungal/flucytosine.yaml"
FLUCYTOSINE_FIXTURE = "tests/fixtures/flucytosine-before-2026-10-13.yaml"
FLUCYTOSINE_SHA256 = "4ffd0f50d00448664a2aec8b152d62231ec7c6fabc5e91a67fc42c27a3ed7ada"
CLOTRIMAZOLE_PATH = "data/antibiotics/antifungal/clotrimazole.yaml"
CLOTRIMAZOLE_FIXTURE = "tests/fixtures/clotrimazole-before-2026-10-13.yaml"
HISTORICAL_RECORDS = {
    FLUCYTOSINE_SHA256: ("CHEBI:5100", FLUCYTOSINE_PATH, FLUCYTOSINE_FIXTURE),
    "a20523175943481166351a5178707948ef52441c2a907cf1a286695f66ad95a6": (
        "CHEBI:3764", CLOTRIMAZOLE_PATH, CLOTRIMAZOLE_FIXTURE,
    ),
    "1731a6718d89e95494d9d8b1c9c621ef538e9a4fd1993f6b952f11d7d0cd96bc": (
        "CHEBI:77762", "data/antibiotics/antifungal/syringomycin-e.yaml",
        "tests/fixtures/syringomycin-e-before-2026-10-13.yaml",
    ),
}


def checkpoint_path(root, item):
    """Allow only the registered identity/path/hash tuple to use a fixture."""
    hashes = [item[key] for key in ("sha256", "record_sha256") if key in item]
    if not hashes or len(set(hashes)) != 1:
        raise ValueError("missing or conflicting historical record checksum")
    checksum = hashes[0]
    path = item["path"]
    if checksum in HISTORICAL_RECORDS:
        identifier, original, fixture = HISTORICAL_RECORDS[checksum]
        if (item["identifier"], path) != (identifier, original):
            raise ValueError("historical record identity or path changed")
        path = fixture
    return reference.check_pin(root, {"path": path, "sha256": checksum})
