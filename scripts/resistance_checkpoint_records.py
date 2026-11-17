"""Resolve explicit historical research inputs, never the live corpus census."""

import json

import audit_topoisomerase_references as reference

FLUCYTOSINE_PATH = "data/antibiotics/antifungal/flucytosine.yaml"
FLUCYTOSINE_FIXTURE = "tests/fixtures/flucytosine-before-2026-10-13.yaml"
FLUCYTOSINE_SHA256 = "4ffd0f50d00448664a2aec8b152d62231ec7c6fabc5e91a67fc42c27a3ed7ada"
CLOTRIMAZOLE_PATH = "data/antibiotics/antifungal/clotrimazole.yaml"
CLOTRIMAZOLE_FIXTURE = "tests/fixtures/clotrimazole-before-2026-10-13.yaml"
HISTORICAL_RECORDS = {
    "081fcfdb19f92cb018d6300bbdb1f141ab81659a14b132c8687ddba9d6b795da": (
        "CHEBI:15353", "data/antibiotics/antifungal/blasticidin-s.yaml",
        "tests/fixtures/blasticidin-s-before-deaminase-2026-10-13.yaml",
    ),
    "d08fcf405a7209c76c0f33749e3aa7a609504eff8c6de91737cc5f8e05c5b15c": (
        "CHEBI:16842", "data/antibiotics/biocide/formaldehyde.yaml",
        "tests/fixtures/formaldehyde-before-2026-10-14.yaml",
    ),
    "ac88ec7d91f9fe520740a84623e1024bfce36c338d16da4c63398a5f2079466e": (
        "CHEBI:172943", "data/antibiotics/antiviral/bictegravir.yaml",
        "tests/fixtures/bictegravir-before-2026-10-14.yaml",
    ),
    "2894f5b4c56f5716b102720362a56e69279661421faff7dcc5c30a0954f01566": (
        "CHEBI:65484", "data/antibiotics/antiviral/bevirimat.yaml",
        "tests/fixtures/bevirimat-before-2026-10-14.yaml",
    ),
    "264f89429273999ddda4f850bf45929897b8b5f33ef0ae6a01433811a9a8ee58": (
        "CHEBI:78661", "data/antibiotics/antifungal/borrelidin.yaml",
        "tests/fixtures/borrelidin-before-2026-10-14.yaml",
    ),
    "5bdf0cc6feda78dd54eee8f5a7bbf37b7c8515344790fc01cb833c20953580b7": (
        "CHEBI:68241", "data/antibiotics/antibacterial/platencin.yaml",
        "tests/fixtures/platencin-before-2026-10-14.yaml",
    ),
    "f75a55971c4629c13895681a48dc43f5b43143e380431503d6a28c1e16576a84": (
        "CHEBI:68236", "data/antibiotics/antibacterial/platensimycin.yaml",
        "tests/fixtures/platensimycin-before-2026-10-14.yaml",
    ),
    "36014dc9ddbd32288e27e051c676ad82bcb6ba8bfb24c793800fcc673fdabe4c": (
        "CHEBI:168396", "data/antibiotics/antiviral/mycophenolic-acid.yaml",
        "tests/fixtures/mycophenolic-acid-before-2026-10-14.yaml",
    ),
    FLUCYTOSINE_SHA256: ("CHEBI:5100", FLUCYTOSINE_PATH, FLUCYTOSINE_FIXTURE),
    "a20523175943481166351a5178707948ef52441c2a907cf1a286695f66ad95a6": (
        "CHEBI:3764", CLOTRIMAZOLE_PATH, CLOTRIMAZOLE_FIXTURE,
    ),
    "1731a6718d89e95494d9d8b1c9c621ef538e9a4fd1993f6b952f11d7d0cd96bc": (
        "CHEBI:77762", "data/antibiotics/antifungal/syringomycin-e.yaml",
        "tests/fixtures/syringomycin-e-before-2026-10-13.yaml",
    ),
}

CITATION_BASELINES = {
    "272ab62a133779fb068f84c97fbeba1dfd1d3e101d7342d8994b2a632d6224bd": (
        "CHEBI:131850",
        "data/antibiotics/antibacterial/pr-39.yaml",
    ),
    "4886e113f1e70381dd401f1346c9058c687ea5c7f192fbbd12db7bedbc4cc3f4": (
        "CHEBI:15353",
        "data/antibiotics/antifungal/blasticidin-s.yaml",
    ),
    "7a1fb4d516dcc4337524ad052655d47fe2ff98e4dfe0b53f1c3b4c981518fd37": (
        "CHEBI:81419",
        "data/antibiotics/antifungal/kasugamycin.yaml",
    ),
}
CITATION_RECEIPT = {
    "path": "research/2026-10-14-reference-citation-curation.json",
    "sha256": "d7b0c8c624cd2c1eb0c6a35cb5591e8a94910230c6421ace8b592e5c2275002c",
}
ARCHIVE_BASELINES = {
    "d28d043dfb2adcb9d6cb3f9c86d17f0e5da4c8b6a580f5baa2617eb9f8bfdc7f": (
        "CHEBI:68241", "data/antibiotics/antibacterial/platencin.yaml",
    ),
    "8baffa64e37818f750df4ab55b5ed0d16783b1158c5f4a6845b85536e979839a": (
        "CHEBI:68236", "data/antibiotics/antibacterial/platensimycin.yaml",
    ),
}
ARCHIVE_RECEIPT = {
    "path": "research/2026-10-14-platen-archive-curation.json",
    "sha256": "0800102f30608f3444487fcc675273c8403a155d3f0ae9ccdbba185907d497e0",
}


def citation_snapshot(root, item, checksum):
    """Replay a pinned citation-only delta without redistributing full records."""
    from resistance_reference_citations import restore_before

    return reference_snapshot(root, item, checksum, CITATION_BASELINES, CITATION_RECEIPT, restore_before)


def reference_snapshot(root, item, checksum, baselines, receipt_pin, restore_before):
    """Restore only an explicitly registered, checksum-pinned reference delta."""
    from antibioticmech.activity_collections import load_record
    from antibioticmech.validation.write_validated import write_validated_antibiotic

    if (item["identifier"], item["path"]) != baselines[checksum]:
        raise ValueError("historical citation record identity or path changed")
    receipt = json.loads(reference.check_pin(root, receipt_pin).read_bytes())
    rows = [r for r in receipt["records"] if r["before"]["sha256"] == checksum]
    if len(rows) != 1 or (rows[0]["identifier"], rows[0]["before"]["path"]) != baselines[checksum]:
        raise ValueError("historical citation receipt binding changed")
    snapshot = root / "reports/resistance-reference-checkpoints" / f"{checksum}.yaml"
    if not snapshot.exists():
        from pathlib import Path

        source_path = root / item["path"]
        record = load_record(source_path)
        repo_root = Path(__file__).resolve().parents[1]
        cg_receipt_path = root / "curation/causal_graphs_transition.json"
        if not cg_receipt_path.is_file():
            cg_receipt_path = repo_root / "curation/causal_graphs_transition.json"
        if cg_receipt_path.is_file() and isinstance(record, dict):
            cg_receipt = json.loads(cg_receipt_path.read_bytes())
            for delta in cg_receipt.get("record_deltas") or []:
                if (
                    delta.get("path") == item["path"]
                    and record.get("causal_graphs") == delta.get("after_causal_graphs")
                    and delta.get("added_history_event") in (record.get("curation_history") or [])
                ):
                    record["curation_history"].remove(delta["added_history_event"])
                    if delta.get("before_causal_graphs") is not None:
                        record["causal_graphs"] = delta["before_causal_graphs"]
                    else:
                        record.pop("causal_graphs", None)
                    break
        before = restore_before(record, rows[0])
        write_validated_antibiotic(before, snapshot)
    return reference.check_pin(root, {"path": str(snapshot.relative_to(root)), "sha256": checksum})


def checkpoint_path(root, item):
    """Allow only the registered identity/path/hash tuple to use a fixture."""
    hashes = [item[key] for key in ("sha256", "record_sha256") if key in item]
    if not hashes or len(set(hashes)) != 1:
        raise ValueError("missing or conflicting historical record checksum")
    checksum = hashes[0]
    path = item["path"]
    if checksum in CITATION_BASELINES:
        return citation_snapshot(root, item, checksum)
    if checksum in ARCHIVE_BASELINES:
        from curate_platen_archive_references import restore_before

        return reference_snapshot(root, item, checksum, ARCHIVE_BASELINES, ARCHIVE_RECEIPT, restore_before)
    if checksum in HISTORICAL_RECORDS:
        identifier, original, fixture = HISTORICAL_RECORDS[checksum]
        if (item["identifier"], path) != (identifier, original):
            raise ValueError("historical record identity or path changed")
        path = fixture
    return reference.check_pin(root, {"path": path, "sha256": checksum})
