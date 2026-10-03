"""Bounded static activity views with lossless, content-addressed downloads."""

from __future__ import annotations

import gzip
import hashlib
import io
import json
import unicodedata
from pathlib import Path

PAGE_SIZE = 100
PREVIEW_SIZE = 20
MAX_BROWSER_BYTES = 16 * 1024 * 1024
FORMAT = "antibioticmech-activity-page-v1"
INDEX_FORMAT = "antibioticmech-activity-index-v1"


def search_row(number: int, observation: dict) -> list:
    """Index every accession, including paired contexts, without flattening evidence."""
    fields = (
        "biosample_accession", "bioproject_accession", "assembly_accession",
        "pathogen_detection_target_accession",
    )
    accessions = []
    for context in [observation, *observation.get("pathogen_detection_contexts", [])]:
        accessions.extend(context[field] for field in fields if context.get(field))
        accessions.extend(context.get("sra_accessions", []))
    values = [str(observation.get(field) or "") for field in (
        "taxon_label", "taxon_id", "strain", "activity", "source",
    )]
    values.append(" ".join(dict.fromkeys(accessions)))
    query = " ".join([*values, observation.get("assay") or "",
                      observation.get("source_observation_id") or ""])
    return [number, *values, unicodedata.normalize("NFKC", query).lower()]


def write_json(directory: Path, prefix: str, value: dict, *, browser: bool = True) -> str:
    raw = (json.dumps(value, ensure_ascii=False, allow_nan=False, separators=(",", ":"))
           + "\n").encode("utf-8")
    buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=buffer, mode="wb", filename="", mtime=0) as stream:
        stream.write(raw)
    payload = buffer.getvalue()
    if browser and max(len(raw), len(payload)) > MAX_BROWSER_BYTES:
        raise ValueError(f"{prefix} exceeds the browser payload bound")
    name = f"{prefix}-{hashlib.sha256(payload).hexdigest()}.json.gz"
    (directory / name).write_bytes(payload)
    return name


def render_activity_pages(doc: dict, record_path: Path, out_dir: Path, env, stats: dict) -> dict:
    """Write all pages/assets; return record-preview context and pruning ownership."""
    observations = doc.get("activity_spectrum") or []
    if not observations:
        return {"written": set(), "pages": []}
    if doc.get("activity_collections"):
        raise ValueError("activity publication requires a fully expanded record")
    relative = Path(record_path.parent.name) / record_path.stem
    directory = out_dir / relative
    directory.mkdir(parents=True, exist_ok=True)
    written = set()

    def asset(prefix, value, *, browser=True):
        name = write_json(directory, prefix, value, browser=browser)
        written.add(directory / name)
        return name

    identity = {
        "identifier": doc["identifier"],
        "standard_inchi_key": doc["chemical_structure"]["standard_inchi_key"],
        "total": len(observations),
    }
    download = asset("record", doc, browser=False)
    index_rows = [search_row(i, row) for i, row in enumerate(observations, 1)]
    index = asset("search", {"format": INDEX_FORMAT, **identity, "rows": index_rows})
    common = {
        **identity, "label": doc["label"], "download": download, "index": index,
        "page_size": PAGE_SIZE, "page_count": (len(observations) + PAGE_SIZE - 1) // PAGE_SIZE,
        "activities": sorted({row[4] for row in index_rows}),
        "sources": sorted({row[5] for row in index_rows}),
    }
    pages = []
    first_data = None
    for offset in range(0, len(observations), PAGE_SIZE):
        rows = observations[offset:offset + PAGE_SIZE]
        number = offset // PAGE_SIZE + 1
        data = asset(f"activity-{number}", {
            "format": FORMAT, **identity, "offset": offset, "observations": rows,
        })
        if first_data is None:
            first_data = data
        page = directory / f"activity-{number}.html"
        page.write_text(env.get_template("activity.html").render(
            activity={**common, "number": number, "offset": offset, "data": data},
            observations=rows, record_href=f"../{record_path.stem}.html#activity",
            root="../../", stats=stats,
        ), encoding="utf-8")
        written.add(page)
        pages.append(page.relative_to(out_dir).as_posix())
    preview = observations[:PREVIEW_SIZE] if len(observations) > PAGE_SIZE else observations
    return {
        "written": written, "pages": pages, "preview": preview,
        "activity": {
            **common, "offset": 0, "data": f"{record_path.stem}/{first_data}",
            "download": f"{record_path.stem}/{download}",
            "home": f"{record_path.stem}/activity-1.html",
        },
    }
