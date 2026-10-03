"""Export versioned semantic text for the fleet map; no model inference.

The temporary SQLite path/identity index bounds memory independently of corpus
size. Full exports are the default; selected subsets are reported as subsets.
The existing domain renderer defines each document; selection changes coverage,
not the meaning or text checksum of a selected record.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sqlite3
import sys
import tempfile
from collections.abc import Iterator, Mapping
from contextlib import ExitStack
from pathlib import Path
from urllib.parse import quote

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
ADAPTER_VERSION = "antibioticmech-existing-full-text-v1"
CORPUS = "antibiotics"


def clean(value: object) -> str:
    if value is None:
        return ""
    return " ".join(str(value).split())


def _load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        record = yaml.load(handle, Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
    if not isinstance(record, dict):
        raise ValueError(f"record is not a mapping: {path}")
    for field in ("identifier", "label"):
        if not isinstance(record.get(field), str) or not clean(record[field]):
            raise ValueError(f"record has no nonempty {field}: {path}")
    return record


def _discover(directory: Path) -> Iterator[Path]:
    """Yield paths without a list of all YAML files or following symlinks."""
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_symlink():
                if entry.name.endswith(".yaml") or entry.is_dir():
                    raise ValueError(f"symlink in corpus: {entry.path}")
                continue
            if entry.is_dir(follow_symlinks=False):
                yield from _discover(Path(entry.path))
            elif entry.name.endswith(".yaml") and entry.is_file(follow_symlinks=False):
                yield Path(entry.path)


def _record_path(root: Path, relative: str) -> Path:
    if Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ValueError(f"record leaves the corpus: {relative}")
    path = root / relative
    corpus_root = root / "data" / CORPUS
    if path.suffix != ".yaml" or not path.is_file():
        raise ValueError(f"not a corpus YAML file: {relative}")
    try:
        path.resolve().relative_to(corpus_root.resolve())
        path.relative_to(corpus_root)
    except ValueError as exc:
        raise ValueError(f"record leaves the corpus: {relative}") from exc
    if any(parent.is_symlink() for parent in (path, *path.parents) if parent != root.parent):
        raise ValueError(f"symlink in record path: {relative}")
    return path


CATEGORY_FIELD = "antimicrobial_class"


def build_context(root: Path) -> Mapping:
    """Load the existing renderer without importing any embedding/model stack."""
    spec = importlib.util.spec_from_file_location(
        "_antibioticmech_legacy_text", REPO_ROOT / "scripts" / "embed_records.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROLE_NAMES = root / "data" / "raw" / "chebi_role_names.tsv"
    return {"builder": module.build_document, "names": module.role_names()}


def semantic_text(record: dict, context: Mapping) -> str:
    """Keep the existing domain-specific field selection and document order."""
    return context["builder"](record, context["names"])


def page_target(record: dict, source_path: str) -> str:
    # scripts/render_pages.py publishes the class/pathway directory and YAML stem.
    path = Path(source_path)
    return quote(path.parent.name, safe="-") + "/" + quote(path.stem, safe="-") + ".html"


def iter_inputs(
    root: Path = REPO_ROOT, *, records: list[str] | None = None, limit: int | None = None
) -> Iterator[dict]:
    """Yield the exact fleet JSONL contract, with stable order and unique IDs."""
    root = root.resolve()
    corpus_root = root / "data" / CORPUS
    if not corpus_root.is_dir() or corpus_root.is_symlink() or (root / "data").is_symlink():
        raise ValueError(f"missing real corpus directory: {corpus_root}")
    if limit is not None and limit < 1:
        raise ValueError("limit must be a positive integer")
    context = build_context(root)
    with tempfile.TemporaryDirectory(prefix="antibioticmech-map-inputs-") as directory:
        connection = sqlite3.connect(str(Path(directory) / "index.sqlite"))
        try:
            connection.execute("CREATE TABLE paths (path TEXT PRIMARY KEY)")
            connection.execute("CREATE TABLE ids (identifier TEXT PRIMARY KEY)")
            paths = (_record_path(root, path) for path in records) if records else _discover(corpus_root)
            for path in paths:
                relative = path.relative_to(root).as_posix()
                try:
                    connection.execute("INSERT INTO paths VALUES (?)", (relative,))
                except sqlite3.IntegrityError as exc:
                    raise ValueError(f"duplicate selected path: {relative}") from exc
            connection.commit()
            query = "SELECT path FROM paths ORDER BY path"
            if limit is not None:
                query += " LIMIT ?"
            for (relative,) in connection.execute(query, (limit,) if limit is not None else ()):
                record = _load(_record_path(root, relative))
                identifier = record["identifier"]
                try:
                    connection.execute("INSERT INTO ids VALUES (?)", (identifier,))
                except sqlite3.IntegrityError as exc:
                    raise ValueError(f"duplicate record identifier: {identifier}") from exc
                text = semantic_text(record, context)
                yield {
                    "identifier": identifier,
                    "label": clean(record["label"]),
                    "category": clean(record.get(CATEGORY_FIELD)) or "UNKNOWN",
                    "page": page_target(record, relative),
                    "source_path": relative,
                    "text": text,
                    "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                    "adapter_version": ADAPTER_VERSION,
                }
        finally:
            connection.close()


def export_inputs(
    root: Path, output: Path | None, *, records: list[str] | None = None, limit: int | None = None
) -> dict:
    """Validate a preview or atomically publish JSONL after all rows pass."""
    destination = output.resolve() if output is not None else None
    if destination is not None and destination.suffix != ".jsonl":
        raise ValueError("output must have a .jsonl suffix")
    temporary = None
    handle = None
    digest = hashlib.sha256()
    count = 0
    try:
        with ExitStack() as stack:
            if destination is not None:
                destination.parent.mkdir(parents=True, exist_ok=True)
                handle = stack.enter_context(
                    tempfile.NamedTemporaryFile(
                        mode="wb",
                        prefix=".text-map-",
                        dir=destination.parent,
                        delete=False,
                    )
                )
                temporary = Path(handle.name)
            for record in iter_inputs(root, records=records, limit=limit):
                payload = (json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
                digest.update(payload)
                count += 1
                if handle is not None:
                    handle.write(payload)
            if not count:
                raise ValueError("selection contains no corpus records")
            if handle is not None:
                handle.close()
                temporary.replace(destination)
            return {
                "mode": "export" if destination is not None else "preview",
                "scope": "subset" if records or limit is not None else "full",
                "records": count,
                "adapter_version": ADAPTER_VERSION,
                "jsonl_sha256": digest.hexdigest(),
                "output": str(destination) if destination is not None else None,
            }
    finally:
        if handle is not None:
            handle.close()
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="repository containing data/" + CORPUS)
    parser.add_argument("--output", type=Path, help="publish JSONL atomically; otherwise validate a preview")
    parser.add_argument(
        "--record", action="append", help="repo-relative YAML path; repeat for a canary subset"
    )
    parser.add_argument(
        "--limit", type=int, help="canary: select this many paths before parsing selected records"
    )
    args = parser.parse_args(argv)
    try:
        result = export_inputs(args.root, args.output, records=args.record, limit=args.limit)
    except (OSError, ValueError, yaml.YAMLError, sqlite3.Error) as exc:
        print(f"text-map inputs refused: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
