#!/usr/bin/env python3
"""Check every PathwayMech link against the committed index without network access."""

from pathlib import Path

import yaml

from antibioticmech.pathway_links import check_links, load_index

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    commit, index = load_index(ROOT)
    errors = []
    for path in sorted((ROOT / "data/antibiotics").rglob("*.yaml")):
        record = yaml.safe_load(path.read_text())
        errors.extend(f"{path.relative_to(ROOT)}: {error}"
                      for error in check_links(record, commit, index))
    for error in errors:
        print(error)
    print(f"PathwayMech links: {len(errors)} errors; pinned at {commit}")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
