#!/usr/bin/env python3
"""Generate or verify the committed structure-only chemical-map artifact."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from antibioticmech.chemical_embedding import (  # noqa: E402
    StructureEmbeddingError,
    build_artifact,
    load_structure_records,
    serialize_artifact,
    validate_artifact,
)

CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"
PATHS_FILE = CORPUS_DIR / "PATHS.tsv"
DEFAULT_OUTPUT = REPO_ROOT / "data" / "embeddings" / "chemical-structure-map.json"


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", dir=path.parent
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write(content)
        os.replace(temporary_name, path)
    except BaseException:
        Path(temporary_name).unlink(missing_ok=True)
        raise


def _load_artifact(path: Path) -> dict:
    try:
        artifact = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise StructureEmbeddingError(f"missing generated artifact: {path}") from None
    except json.JSONDecodeError as error:
        raise StructureEmbeddingError(f"{path}: invalid JSON: {error}") from error
    if not isinstance(artifact, dict):
        raise StructureEmbeddingError(f"{path}: root must be an object")
    return artifact


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check hashes, versions, coverage, and quality metadata without writing.",
    )
    parser.add_argument(
        "--recompute",
        action="store_true",
        help="With --check, rerun the complete model and require byte-identical output.",
    )
    args = parser.parse_args(argv)
    if args.recompute and not args.check:
        parser.error("--recompute requires --check")

    try:
        records = load_structure_records(CORPUS_DIR, PATHS_FILE)
        if args.check and not args.recompute:
            artifact = _load_artifact(args.out)
            errors = validate_artifact(artifact, records)
            if errors:
                print(f"{args.out} is stale:", file=sys.stderr)
                for error in errors:
                    print(f"  {error}", file=sys.stderr)
                print("Regenerate with `just chemical-map`.", file=sys.stderr)
                return 1
            quality = artifact["quality"]
            print(
                f"chemical map is current: {len(records)} records, "
                f"trustworthiness@10={quality['trustworthiness_at_10']:.4f}, "
                f"neighbor-overlap@10={quality['neighbor_overlap_at_10']:.4f}"
            )
            return 0

        started = time.perf_counter()
        artifact = build_artifact(records, REPO_ROOT)
        content = serialize_artifact(artifact)
        elapsed = time.perf_counter() - started
        if args.check:
            existing = args.out.read_text(encoding="utf-8")
            if existing != content:
                print(
                    f"{args.out} is not byte-identical to a complete rebuild",
                    file=sys.stderr,
                )
                return 1
            print(f"chemical map complete rebuild is byte-identical ({elapsed:.2f}s)")
            return 0
        _atomic_write(args.out, content)
        quality = artifact["quality"]
        print(
            f"generated {len(records)} chemical-map records in {elapsed:.2f}s -> {args.out}"
        )
        print(
            f"SMILES/InChI fallback: {quality['inchi_fallback_count']}; "
            f"multi-fragment: {quality['multifragment_count']}; "
            f"stereoisomer zero-distance: "
            f"{quality['zero_distance_stereoisomer_pairs']}/"
            f"{quality['stereoisomer_pair_count']}"
        )
        return 0
    except (OSError, StructureEmbeddingError) as error:
        print(f"chemical-map error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
