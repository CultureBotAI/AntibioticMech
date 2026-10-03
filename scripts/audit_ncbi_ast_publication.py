#!/usr/bin/env python3
"""Exercise AST record writes and page rendering outside the published corpus."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import tempfile
import time
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from activity_pages import FORMAT, INDEX_FORMAT, PAGE_SIZE, render_activity_pages, search_row
from jinja2 import Environment, FileSystemLoader, select_autoescape
from ncbi_ast_assays import DEFAULT_REVIEW_MAP
from ncbi_ast_biosamples import DEFAULT_REVIEW
from ncbi_ast_isolates import file_sha256
from render_pages import TEMPLATES_DIR, build_record
from render_pages import build as build_site
from seed_from_sources import (
    CORPUS_DIR,
    REPO_ROOT,
    is_ncbi_ast_sourced_activity,
    merge_with_existing,
    ncbi_ast_sourced_activity_view,
    read_lockfile_paths,
)
from verify_corpus import rebuild

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic


def normalized(text: str) -> str:
    return " ".join(text.split())


class ActivityTable(HTMLParser):
    """Read the rendered cells, not just search the HTML for expected strings."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.rows = []
        self.table = False
        self.active = False
        self.caption = None
        self.cell = None
        self.row = []
        self.matches = 0
        self.anchors = []
        self.details = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "a":
            self.links.append(attributes)
        if tag == "table":
            if self.table:
                raise ValueError("unexpected nested table")
            self.table = True
        elif tag == "caption" and self.table:
            self.caption = []
        elif tag == "tr" and self.active:
            self.row = []
            self.anchors.append(attributes.get("id"))
        elif tag == "td" and self.active:
            self.cell = []
        elif tag == "br" and self.cell is not None:
            self.cell.append(" ")
        elif tag == "details" and self.active:
            self.details.append(attributes)

    def handle_data(self, data):
        if self.caption is not None:
            self.caption.append(data)
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if tag == "caption" and self.caption is not None:
            self.active = normalized("".join(self.caption)) == "Activity observations"
            self.matches += int(self.active)
            self.caption = None
        elif tag == "td" and self.cell is not None:
            self.row.append(normalized("".join(self.cell)))
            self.cell = None
        elif tag == "tr" and self.active and self.row:
            self.rows.append(self.row)
            self.row = []
        elif tag == "table":
            self.table = self.active = False


def displayed_cells(observation: dict) -> list[str]:
    missing = "\u2014"

    def measurement(prefix):
        value = observation.get(prefix + "_value")
        if value is None:
            return missing
        return (
            f"{observation.get(prefix + '_qualifier') or ''}{value} "
            f"{observation.get(prefix + '_units') or ''}"
        )

    genome = []

    def accession(label, field, context=observation):
        if context.get(field):
            genome.append(f"{label} {context[field]}")

    accession("BioSample", "biosample_accession")
    accession("BioProject", "bioproject_accession")
    accession("Pathogen Detection", "pathogen_detection_target_accession")
    accession("Assembly", "assembly_accession")
    genome.extend(f"SRA {value}" for value in observation.get("sra_accessions", []))
    for context in observation.get("pathogen_detection_contexts", []):
        accession("Pathogen Detection", "pathogen_detection_target_accession", context)
        accession("Assembly", "assembly_accession", context)
        accession("BioProject", "bioproject_accession", context)
        accession("Source created", "source_create_date", context)
        genome.extend(f"SRA {value}" for value in context.get("sra_accessions", []))
    if observation.get("pathogen_detection_contexts") and observation.get("source_export_row_count"):
        genome.append(
            f"{observation['measurement_count']} measurement(s); "
            f"{observation['source_export_row_count']} source export rows"
        )
    return [
        normalized(value)
        for value in [
            f"{observation['taxon_label']} {observation.get('taxon_id') or ''}",
            observation.get("activity") or missing,
            measurement("mic"),
            measurement("disk_diffusion"),
            observation.get("assay") or missing,
            observation.get("strain") or missing,
            " ".join(genome) or missing,
        ]
    ]


def verify_activity_table(html: str, observations: list[dict], *, evidence=False, offset=0) -> None:
    parser = ActivityTable()
    parser.feed(html)
    parser.close()
    if parser.table or parser.cell is not None or parser.matches != int(bool(observations)):
        raise ValueError("missing, duplicated, or incomplete activity table")
    expected = [displayed_cells(observation) for observation in observations]
    if evidence:
        expected = [row + ["Evidence Page data (JSON.gz)"] for row in expected]
        # The header row has no anchor; every scientific row must have its full-record ordinal.
        if parser.anchors != [None, *[f"observation-{offset + i}" for i in range(1, len(observations) + 1)]]:
            raise ValueError("activity observation anchors differ")
    if parser.rows != expected:
        raise ValueError("rendered activity rows differ from serialized observations")


def verify_activity_publication(doc: dict, out_dir: Path, publication: dict) -> dict:
    """Check every bounded row, data envelope, evidence link, index and complete download."""
    observations = doc["activity_spectrum"]
    first = out_dir / publication["pages"][0]
    directory = first.parent
    identity = {
        "identifier": doc["identifier"],
        "standard_inchi_key": doc["chemical_structure"]["standard_inchi_key"],
        "total": len(observations),
    }

    def read_asset(path):
        payload = path.read_bytes()
        if not path.name.endswith(f"-{hashlib.sha256(payload).hexdigest()}.json.gz"):
            raise ValueError("activity asset checksum mismatch")
        return json.loads(gzip.decompress(payload))

    download = directory / Path(publication["activity"]["download"]).name
    if read_asset(download) != doc:
        raise ValueError("complete record download differs")
    index_path = directory / publication["activity"]["index"]
    expected_index = {"format": INDEX_FORMAT, **identity,
                      "rows": [search_row(i, row) for i, row in enumerate(observations, 1)]}
    if read_asset(index_path) != expected_index:
        raise ValueError("activity search index differs")
    expected_pages = [directory / f"activity-{i}.html"
                      for i in range(1, (len(observations) + PAGE_SIZE - 1) // PAGE_SIZE + 1)]
    if [out_dir / page for page in publication["pages"]] != expected_pages:
        raise ValueError("activity page coverage differs")
    sizes = []
    for number, page in enumerate(expected_pages, 1):
        offset = (number - 1) * PAGE_SIZE
        rows = observations[offset:offset + PAGE_SIZE]
        html = page.read_text(encoding="utf-8")
        verify_activity_table(html, rows, evidence=True, offset=offset)
        parser = ActivityTable()
        parser.feed(html)
        data_links = [link["href"] for link in parser.links if link.get("class") == "activity-data"]
        if len(data_links) != len(rows) or len(set(data_links)) != 1:
            raise ValueError("missing or inconsistent activity evidence links")
        if any(Path(link).name != link for link in data_links):
            raise ValueError("activity data link escaped page directory")
        data_path = directory / data_links[0]
        if read_asset(data_path) != {"format": FORMAT, **identity, "offset": offset, "observations": rows}:
            raise ValueError("complete activity page differs")
        expected_details = [
            {"class": "activity-evidence", "data-row": str(i), "data-offset": str(offset),
             "data-total": str(len(observations)), "data-identifier": doc["identifier"],
             "data-key": identity["standard_inchi_key"]} for i in range(len(rows))
        ]
        if parser.details != expected_details:
            raise ValueError("activity evidence bindings differ")
        for direction, target in [("prev", number - 1), ("next", number + 1)]:
            expected = [f"activity-{target}.html"] * 2 if 1 <= target <= len(expected_pages) else []
            actual = [link["href"] for link in parser.links if link.get("rel") == direction]
            if actual != expected:
                raise ValueError("activity pagination links differ")
        if not any(link.get("href") == download.name and "download" in link for link in parser.links):
            raise ValueError("complete download link missing")
        sizes.append(page.stat().st_size)
    return {
        "activity_page_count": len(sizes), "activity_html_bytes": sum(sizes),
        "max_activity_html_bytes": max(sizes), "download_bytes": download.stat().st_size,
        "browser_data_bytes": sum(path.stat().st_size for path in publication["written"]
                                  if path.suffix == ".gz" and path != download),
    }


def verify_merge(fresh: dict, existing: dict) -> dict:
    merged = merge_with_existing(fresh, existing)
    for field in set(merged) | set(existing):
        if field not in {"activity_spectrum", "curation_history"} and merged.get(field) != existing.get(
            field
        ):
            raise ValueError(f"non-AST field changed during audit: {field}")

    def keep(doc):
        return [a for a in doc.get("activity_spectrum", []) if not is_ncbi_ast_sourced_activity(a)]

    if keep(merged) != keep(existing):
        raise ValueError("non-AST activities changed during audit")
    if ncbi_ast_sourced_activity_view(merged) != ncbi_ast_sourced_activity_view(fresh):
        raise ValueError("AST source slice differs after record merge")
    history = existing.get("curation_history", [])
    if merged.get("curation_history", [])[: len(history)] != history:
        raise ValueError("existing curation history changed")
    return merged


def audit_record(fresh: dict, existing: dict, path: Path, directory: Path, template, index: dict) -> dict:
    started = time.monotonic()
    merged = verify_merge(fresh, existing)
    relative = path.relative_to(CORPUS_DIR)
    yaml_path = directory / "records" / relative
    write_validated_antibiotic(merged, yaml_path)
    write_seconds = time.monotonic() - started
    reloaded = load_record(yaml_path)
    if reloaded != merged:
        raise ValueError("YAML round trip changed the complete record")
    if merge_with_existing(fresh, reloaded) != reloaded:
        raise ValueError("unchanged reseeding duplicated or changed record content/history")
    roundtrip_seconds = time.monotonic() - started - write_seconds
    publication = render_activity_pages(reloaded, path, directory / "pages", template.environment, {})
    record = build_record(path, reloaded, index, root="../")
    record.update(activity=publication["activity"], activity_spectrum=publication["preview"])
    html = template.render(r=record, root="../", stats={})
    verify_activity_table(html, publication["preview"], evidence=True)
    page_metrics = verify_activity_publication(reloaded, directory / "pages", publication)
    html_path = directory / "pages" / relative.with_suffix(".html")
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html, encoding="utf-8")
    observations = ncbi_ast_sourced_activity_view(reloaded)
    physical = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    collections = physical.get("activity_collections", [])
    return {
        **page_metrics,
        "identifier": fresh["identifier"],
        "record": str(relative),
        "observations": len(observations),
        "measurements": sum(a["measurement_count"] for a in observations),
        "paired_context_observations": sum(bool(a.get("pathogen_detection_contexts")) for a in observations),
        "total_activity_rows": len(reloaded.get("activity_spectrum", [])),
        "yaml_bytes": yaml_path.stat().st_size,
        "collection_bytes": sum(c["byte_size"] for c in collections),
        "collection_files": len(collections),
        "html_bytes": html_path.stat().st_size,
        "yaml_sha256": file_sha256(yaml_path),
        "html_sha256": file_sha256(html_path),
        "write_seconds": round(write_seconds, 3),
        "roundtrip_seconds": round(roundtrip_seconds, 3),
        "render_verify_seconds": round(time.monotonic() - started - write_seconds - roundtrip_seconds, 3),
    }


def verify_site_links(directory: Path) -> int:
    """Check local page/download/style/script targets without requesting external URLs."""
    class Links(HTMLParser):
        def __init__(self):
            super().__init__()
            self.targets = []

        def handle_starttag(self, tag, attrs):
            field = "href" if tag in {"a", "link"} else "src" if tag in {"script", "img"} else None
            target = dict(attrs).get(field)
            if target:
                self.targets.append(target)

    directory = directory.resolve()
    checked = 0
    for path in directory.rglob("*.html"):
        parser = Links()
        parser.feed(path.read_text(encoding="utf-8"))
        for href in parser.targets:
            url = urlsplit(href)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (path.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(directory) or not target.is_file():
                raise ValueError(f"broken local site link: {path.relative_to(directory)} -> {href}")
            checked += 1
    return checked


def audit(inventory: Path, output: Path, *, full_site: bool = False) -> dict:
    # Keep evaluation artifacts in the ignored report tree, never publishable paths.
    output = output.resolve()
    reports = (REPO_ROOT / "reports").resolve()
    if output.parent != reports:
        raise ValueError("output must be a new direct child directory of reports/")
    if output.exists():
        raise ValueError(f"refusing to overwrite {output}")
    if not inventory.is_file():
        raise ValueError(f"missing activity report: {inventory}")
    paths = read_lockfile_paths()
    inputs = sorted(
        set(
            [
                inventory,
                DEFAULT_REVIEW_MAP,
                DEFAULT_REVIEW,
                *paths.values(),
                *CORPUS_DIR.rglob("activity-*.jsonl.gz"),
                *REPO_ROOT.glob("data/raw/*"),
                *REPO_ROOT.glob("conf/*"),
                *REPO_ROOT.glob("curation/*"),
                *REPO_ROOT.glob("scripts/*.py"),
                *TEMPLATES_DIR.rglob("*"),
                *REPO_ROOT.glob("src/antibioticmech/schema/*.yaml"),
                *REPO_ROOT.glob("src/antibioticmech/validation/*.py"),
                REPO_ROOT / "src/antibioticmech/activity_collections.py",
            ]
        )
    )
    hashes = {str(path): file_sha256(path) for path in inputs if path.is_file()}
    started = time.monotonic()
    records = rebuild(ncbi_ast_inventory=inventory)
    if set(records) != set(paths):
        raise ValueError("rebuilt corpus and locked record paths disagree")
    index = {
        identifier: {
            "class_dir": paths[identifier].parent.name,
            "slug": paths[identifier].stem,
            "label": record["label"],
        }
        for identifier, record in records.items()
    }
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("record.html")
    result = {"records": [], "unchanged_records": 0, "inputs": hashes}
    reports.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".ncbi-publication-", dir=reports) as temporary:
        staged = Path(temporary) / "audit"
        staged.mkdir()
        # Largest records first expose full-scale failures before processing the tail.
        ordered = sorted(records, key=lambda i: (-len(records[i].get("activity_spectrum", [])), i))
        for identifier in ordered:
            fresh, path = records[identifier], paths[identifier]
            existing = load_record(path)
            if not ncbi_ast_sourced_activity_view(fresh) and not ncbi_ast_sourced_activity_view(existing):
                if verify_merge(fresh, existing) != existing:
                    raise ValueError(f"unaffected record changed: {identifier}")
                result["unchanged_records"] += 1
                continue
            print(
                f"Auditing {identifier}: {len(ncbi_ast_sourced_activity_view(fresh))} AST observations",
                flush=True,
            )
            metrics = audit_record(fresh, existing, path, staged, template, index)
            result["records"].append(metrics)
            print(json.dumps(metrics, sort_keys=True), flush=True)
        if not result["records"]:
            raise ValueError("no AST records audited")
        if full_site:
            # Replace rebuilt candidates with the validated, merged publication records.
            for identifier, path in paths.items():
                published = staged / "records" / path.relative_to(CORPUS_DIR)
                records[identifier] = load_record(published if published.exists() else path)
            site = staged / "site"
            build_site(site, records=[(paths[i], records[i]) for i in sorted(records)])
            for asset in (staged / "pages").rglob("*.gz"):
                if asset.read_bytes() != (site / asset.relative_to(staged / "pages")).read_bytes():
                    raise ValueError("full-site evidence/download differs from audited asset")
            result["full_site"] = {"records": len(records), "local_links": verify_site_links(site)}
            print(json.dumps(result["full_site"], sort_keys=True), flush=True)
        if any(
            not Path(path).is_file() or file_sha256(Path(path)) != checksum
            for path, checksum in hashes.items()
        ):
            raise ValueError("an input or published corpus file changed during the audit")
        result["totals"] = {
            field: sum(row[field] for row in result["records"])
            for field in (
                "observations",
                "measurements",
                "paired_context_observations",
                "total_activity_rows",
                "yaml_bytes",
                "collection_bytes",
                "collection_files",
                "html_bytes",
                "activity_page_count",
                "activity_html_bytes",
                "download_bytes",
                "browser_data_bytes",
            )
        }
        result["elapsed_seconds"] = round(time.monotonic() - started, 3)
        result["scope"] = (
            "Production record merge, closed-schema write, YAML round trip, reseed idempotence, "
            "bounded record/activity-page cells, complete evidence assets, search-index coverage, "
            "and expanded-record downloads. No source adoption, independent phenotype "
            "verification or browser usability claim. Full-site rendering/local link validation "
            "is included only when the report has a full_site entry."
        )
        (staged / "audit.json").write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        if output.exists():
            raise ValueError(f"refusing to overwrite {output}")
        staged.rename(output)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--activity-report", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    parser.add_argument("--full-site", action="store_true")
    args = parser.parse_args()
    result = audit(args.activity_report, args.output_directory, full_site=args.full_site)
    print(json.dumps(result["totals"], indent=2))


if __name__ == "__main__":
    main()
