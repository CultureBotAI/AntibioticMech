"""Resolve explicit historical research inputs, never the live corpus census."""

import audit_topoisomerase_references as reference

FLUCYTOSINE_PATH = "data/antibiotics/antifungal/flucytosine.yaml"
FLUCYTOSINE_FIXTURE = "tests/fixtures/flucytosine-before-2026-10-13.yaml"
FLUCYTOSINE_SHA256 = "4ffd0f50d00448664a2aec8b152d62231ec7c6fabc5e91a67fc42c27a3ed7ada"


def checkpoint_path(root, item):
    """Allow only the registered identity/path/hash tuple to use a fixture."""
    hashes = [item[key] for key in ("sha256", "record_sha256") if key in item]
    if not hashes or len(set(hashes)) != 1:
        raise ValueError("missing or conflicting historical record checksum")
    checksum = hashes[0]
    path = item["path"]
    if checksum == FLUCYTOSINE_SHA256:
        if (item["identifier"], path) != ("CHEBI:5100", FLUCYTOSINE_PATH):
            raise ValueError("historical flucytosine identity or path changed")
        path = FLUCYTOSINE_FIXTURE
    return reference.check_pin(root, {"path": path, "sha256": checksum})
