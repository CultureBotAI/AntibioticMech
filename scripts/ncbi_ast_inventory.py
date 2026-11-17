"""Lossless NCBI AST TSV containers; review hashes always cover expanded bytes."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import shutil
import tempfile
from contextlib import contextmanager
from pathlib import Path

from ncbi_ast_isolates import file_sha256

ROOT = Path(__file__).resolve().parents[1]
MAX_CONTENT_BYTES = 256 * 1024 * 1024
CHUNK_BYTES = 1024 * 1024


def inventory_candidates(plain: Path) -> tuple[Path, Path]:
    return plain, plain.with_suffix(plain.suffix + ".gz")


def resolve_inventory(plain: Path) -> Path:
    present = [p for p in inventory_candidates(plain) if p.exists() or p.is_symlink()]
    if len(present) > 1:
        raise ValueError(f"ambiguous NCBI AST inventories: {present}")
    if present and not present[0].is_file():
        raise ValueError(f"NCBI AST inventory is not a file: {present[0]}")
    return present[0] if present else plain


class _BoundedReader(io.RawIOBase):
    def __init__(self, handle, limit: int):
        self.handle = handle
        self.remaining = limit

    def readable(self):
        return True

    def readinto(self, buffer):
        payload = self.handle.read(min(len(buffer), self.remaining + 1))
        if len(payload) > self.remaining:
            raise ValueError("NCBI AST inventory exceeds expanded-byte limit")
        self.remaining -= len(payload)
        buffer[:len(payload)] = payload
        return len(payload)


@contextmanager
def open_activity_bytes(path: Path):
    opener = gzip.open if path.suffix == ".gz" else open
    with (
        opener(path, "rb") as handle,
        io.BufferedReader(_BoundedReader(handle, MAX_CONTENT_BYTES)) as bounded,
    ):
        yield bounded


@contextmanager
def open_activity_text(path: Path):
    with (
        open_activity_bytes(path) as handle,
        io.TextIOWrapper(handle, encoding="utf-8", newline="") as text,
    ):
        yield text


@contextmanager
def write_activity_text(path: Path):
    with path.open("wb") as raw:
        if path.suffix == ".gz":
            with (
                gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as zipped,
                io.TextIOWrapper(zipped, encoding="utf-8", newline="") as text,
            ):
                yield text
        else:
            with io.TextIOWrapper(raw, encoding="utf-8", newline="") as text:
                yield text


def content_fingerprint(path: Path) -> tuple[str, int]:
    digest, size = hashlib.sha256(), 0
    with open_activity_bytes(path) as handle:
        while payload := handle.read(CHUNK_BYTES):
            digest.update(payload)
            size += len(payload)
    return digest.hexdigest(), size


def activity_report_sha256(path: Path) -> str:
    return content_fingerprint(path)[0]


def inventory_metadata(path: Path) -> dict:
    container_hash = file_sha256(path)
    content_hash, content_bytes = content_fingerprint(path)
    if file_sha256(path) != container_hash:
        raise ValueError("NCBI AST inventory changed while fingerprinting")
    return {
        "encoding": "gzip" if path.suffix == ".gz" else "identity",
        "sha256": container_hash,
        "bytes": path.stat().st_size,
        "content_sha256": content_hash,
        "content_bytes": content_bytes,
    }


def pack_inventory(source: Path, output: Path) -> dict:
    """Stage a validated byte-preserving container outside production inputs."""
    from seed_from_sources import load_ncbi_ast_activity_inventory

    output = output.resolve()
    if not output.is_relative_to((ROOT / "reports").resolve()):
        raise ValueError("compressed inventory staging must be under reports/")
    if output.exists():
        raise ValueError(f"refusing to overwrite {output}")
    before = inventory_metadata(source)
    rows = load_ncbi_ast_activity_inventory(source)
    row_count = len(rows)
    del rows
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".ncbi-inventory-", dir=output.parent) as temporary:
        staged = Path(temporary) / "inventory"
        staged.mkdir()
        target = staged / "activity.tsv.gz"
        with (
            open_activity_bytes(source) as handle,
            target.open("wb") as raw,
            gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as zipped,
        ):
            shutil.copyfileobj(handle, zipped, CHUNK_BYTES)
        after = inventory_metadata(target)
        if any(before[k] != after[k] for k in ("content_sha256", "content_bytes")):
            raise ValueError("compressed inventory changed the activity report bytes")
        if inventory_metadata(source) != before:
            raise ValueError("activity report changed during compression")
        result = {
            "source": {"path": str(source), **before},
            "inventory": {"file": target.name, **after},
            "source_groups": row_count,
            "scope": "Lossless container only; no source adoption or new evidence review.",
        }
        (staged / "inventory.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        if output.exists():
            raise ValueError(f"refusing to overwrite {output}")
        staged.rename(output)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--activity-report", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(pack_inventory(args.activity_report, args.output_directory), indent=2))


if __name__ == "__main__":
    main()
