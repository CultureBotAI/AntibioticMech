#!/usr/bin/env python3
"""Exercise AST record writes and page rendering outside the published corpus."""

from __future__ import annotations

import argparse
import json
import tempfile
import time
from html.parser import HTMLParser
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from ncbi_ast_assays import DEFAULT_REVIEW_MAP
from ncbi_ast_biosamples import DEFAULT_REVIEW
from ncbi_ast_isolates import file_sha256
from render_pages import TEMPLATES_DIR, build_record
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

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            if self.table:
                raise ValueError("unexpected nested table")
            self.table = True
        elif tag == "caption" and self.table:
            self.caption = []
        elif tag == "tr" and self.active:
            self.row = []
        elif tag == "td" and self.active:
            self.cell = []
        elif tag == "br" and self.cell is not None:
            self.cell.append(" ")

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


def verify_activity_table(html: str, observations: list[dict]) -> None:
    parser = ActivityTable()
    parser.feed(html)
    parser.close()
    if parser.table or parser.cell is not None or parser.matches != int(bool(observations)):
        raise ValueError("missing, duplicated, or incomplete activity table")
    expected = [displayed_cells(observation) for observation in observations]
    if parser.rows != expected:
        raise ValueError("rendered activity rows differ from serialized observations")


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
    html = template.render(r=build_record(path, reloaded, index, root="../"), root="../", stats={})
    verify_activity_table(html, reloaded.get("activity_spectrum", []))
    html_path = directory / "pages" / relative.with_suffix(".html")
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html, encoding="utf-8")
    observations = ncbi_ast_sourced_activity_view(reloaded)
    physical = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    collections = physical.get("activity_collections", [])
    return {
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


def audit(inventory: Path, output: Path) -> dict:
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
            )
        }
        result["elapsed_seconds"] = round(time.monotonic() - started, 3)
        result["scope"] = (
            "Production record merge, closed-schema write, YAML round trip, reseed idempotence, "
            "and complete record-template activity cells. No source adoption, independent phenotype "
            "verification, full-site navigation test, or browser usability claim."
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
    args = parser.parse_args()
    result = audit(args.activity_report, args.output_directory)
    print(json.dumps(result["totals"], indent=2))


if __name__ == "__main__":
    main()
