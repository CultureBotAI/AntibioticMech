#!/usr/bin/env python3
"""Audit BioSample overlap with CRyPTIC and existing corpus evidence, without seeding.

Rebuild both inventories before comparing sample/drug membership. A shared
sample is a review lead, not proof that two assays are the same observation.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import evaluate_cryptic_activity as cryptic
import evaluate_ncbi_ast as ast
from ncbi_ast_assays import apply_assay_review, read_assay_review
from ncbi_ast_isolates import file_sha256, load_isolate_snapshot
from ncbi_ast_taxonomy import SCOPE_NAME, SCOPE_REFERENCE, SCOPE_TAXID, load_snapshot, relationship
from seed_from_sources import load_cryptic_activity_inventory

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


def corpus_input_hashes(directory: Path) -> dict[str, str]:
    records = sorted(directory.rglob("*.yaml"))
    if not records:
        raise ValueError("empty existing corpus cannot establish overlap coverage")
    paths = {*records, *directory.rglob("activity-*.jsonl.gz")}
    lock = directory / "PATHS.tsv"
    if lock.exists() or lock.is_symlink():
        paths.add(lock)
    if any(path.is_symlink() or not path.is_file() for path in paths):
        raise ValueError("existing corpus inputs must be regular files")
    return {str(path): file_sha256(path) for path in sorted(paths)}


def require_same_corpus(directory: Path, inputs: dict[str, str]) -> None:
    if corpus_input_hashes(directory) != inputs:
        raise ValueError("existing corpus changed during overlap audit")


def corpus_membership(directory: Path) -> dict:
    """Index tested samples, not species-level resistance or project exclusions."""
    inputs = corpus_input_hashes(directory)
    by_sample: dict[str, list[dict]] = defaultdict(list)
    projects: set[str] = set()
    counts: Counter = Counter()
    for name in inputs:
        path = Path(name)
        if path.suffix != ".yaml":
            continue
        doc = load_record(path)
        identifier = doc.get("identifier")
        key = doc.get("chemical_structure", {}).get("standard_inchi_key")
        if not isinstance(identifier, str) or not identifier or not isinstance(key, str) or not re.fullmatch(
            r"[A-Z]{14}-[A-Z]{10}-[A-Z]", key,
        ):
            raise ValueError(f"existing corpus record requires exact chemical identity: {path}")
        counts["records"] += 1
        for number, row in enumerate(doc.get("activity_spectrum", []), 1):
            if row.get("source") == "NCBI_AST":
                counts["ast_observations_excluded"] += 1
                continue
            counts["observations"] += 1
            contexts = [row, *row.get("pathogen_detection_contexts", [])]
            samples = {context["biosample_accession"] for context in contexts
                       if context.get("biosample_accession")}
            row_projects = {context["bioproject_accession"] for context in contexts
                            if context.get("bioproject_accession")}
            if any(not isinstance(value, str) or not re.fullmatch(r"SAM(N|D|EA)[0-9]+", value)
                   for value in samples):
                raise ValueError(f"existing corpus has invalid BioSample: {path}")
            if any(not isinstance(value, str) or not re.fullmatch(r"PRJ(NA|EB|DB)[0-9]+", value)
                   for value in row_projects):
                raise ValueError(f"existing corpus has invalid BioProject: {path}")
            projects.update(row_projects)
            counts["observations_with_biosample" if samples else "observations_without_biosample"] += 1
            reference = {"record": str(path), "identifier": identifier, "standard_inchi_key": key,
                         "activity_observation_number": number, "source": row.get("source"),
                         "source_observation_id": row.get("source_observation_id"),
                         "evidence": row.get("evidence", [])}
            for sample in sorted(samples):
                by_sample[sample].append(reference)
    require_same_corpus(directory, inputs)
    return {
        "by_sample": by_sample, "projects": projects, "inputs": inputs,
        "counts": {name: counts[name] for name in (
            "records", "observations", "observations_with_biosample",
            "observations_without_biosample", "ast_observations_excluded",
        )} | {"biosamples": len(by_sample), "bioprojects": len(projects)},
    }


def corpus_overlap_summary(rows, membership: dict, *, raw: bool, mappings: dict) -> dict:
    counts: Counter = Counter()
    shared: dict[str, dict] = {}
    for row in rows:
        if raw:
            sample = ast.first_value(row, ast.BIOSAMPLE_ALIASES)
            project = ast.first_value(row, ast.BIOPROJECT_ALIASES)
            drug = ast.first_value(row, ast.ANTIBIOTIC_ALIASES)
            mapping = mappings.get(ast.normalize(drug), {})
            exact = mapping.get("mapping_status") == "EXACT"
            identifier, key = ((mapping.get("identifier"), mapping.get("standard_inchi_key"))
                               if exact else (None, None))
            count = 1
        else:
            sample, project, drug = (
                row["biosample_accession"], row["bioproject_accession"], row["source_name"],
            )
            identifier, key = row["identifier"], row["standard_inchi_key"]
            count = int(row["ast_row_count"])
        counts["groups_or_rows"] += 1
        counts["export_rows"] += count
        if project in membership["projects"]:
            counts["shared_project_export_rows"] += count
        references = membership["by_sample"].get(sample, [])
        if not references:
            continue
        counts["shared_sample_export_rows"] += count
        exact_match = any(ref["identifier"] == identifier and ref["standard_inchi_key"] == key
                          for ref in references)
        if exact_match:
            counts["shared_sample_and_compound_export_rows"] += count
        lead = shared.setdefault(sample, {
            "biosample_accession": sample, "source_names": set(),
            "exact_matched_identifiers": set(), "existing_observations": references,
        })
        lead["source_names"].add(drug)
        if exact_match:
            lead["exact_matched_identifiers"].add(identifier)
    for lead in shared.values():
        for field in ("source_names", "exact_matched_identifiers"):
            lead[field] = sorted(lead[field])
    return {name: counts[name] for name in (
        "groups_or_rows", "export_rows", "shared_sample_export_rows",
        "shared_sample_and_compound_export_rows", "shared_project_export_rows",
    )} | {"sample_review_leads": [shared[key] for key in sorted(shared)]}


def require_same_inventory(adopted: list[dict], rebuilt: list[dict]) -> None:
    actual = {row["activity_group_id"]: row for row in adopted}
    expected = {row["activity_group_id"]: row for row in rebuilt}
    if actual != expected or len(actual) != len(adopted) or len(expected) != len(rebuilt):
        raise ValueError("CRyPTIC rebuilt evidence does not match the adopted inventory")


def cryptic_membership(connection, dst: Path, ukmyc: Path, wgs: Path, mappings: dict) -> dict:
    """Use only exact-mapped phenotype members, not every sequenced sample."""
    drugs_by_id: dict[str, set[str]] = defaultdict(set)
    for unique_id, code in connection.execute(
        "SELECT DISTINCT UNIQUEID, DRUG FROM read_parquet(?) "
        "UNION SELECT DISTINCT UNIQUEID, DRUG FROM read_parquet(?)", [str(dst), str(ukmyc)],
    ).fetchall():
        mapping = mappings[code]
        if mapping["mapping_status"] == cryptic.EXACT_MAPPING_STATUS:
            if not unique_id:
                raise ValueError("CRyPTIC exact phenotype has no UNIQUEID")
            drugs_by_id[unique_id].add(mapping["identifier"])

    all_samples, projects, represented_ids, seen_ids = set(), set(), set(), set()
    drugs_by_sample: dict[str, set[str]] = defaultdict(set)
    for unique_id, sample, project in connection.execute(
        "SELECT UNIQUEID, sample_accession, study_accession FROM read_parquet(?)", [str(wgs)],
    ).fetchall():
        if not unique_id or unique_id in seen_ids:
            raise ValueError("CRyPTIC WGS mapping requires unique nonempty UNIQUEIDs")
        seen_ids.add(unique_id)
        if not isinstance(sample, str) or not re.fullmatch(r"SAM(N|D|EA)[0-9]+", sample):
            raise ValueError(f"CRyPTIC WGS mapping has invalid BioSample {sample!r}")
        if not isinstance(project, str) or not re.fullmatch(r"PRJ(NA|EB|DB)[0-9]+", project):
            raise ValueError(f"CRyPTIC WGS mapping has invalid BioProject {project!r}")
        all_samples.add(sample)
        if unique_id in drugs_by_id:
            represented_ids.add(unique_id)
            projects.add(project)
            drugs_by_sample[sample].update(drugs_by_id[unique_id])
    return {
        "all_samples": all_samples, "projects": projects, "drugs_by_sample": drugs_by_sample,
        "counts": {
            "wgs_rows": len(seen_ids), "wgs_biosamples": len(all_samples),
            "adopted_phenotype_uniqueids": len(drugs_by_id),
            "adopted_phenotype_uniqueids_with_wgs": len(represented_ids),
            "adopted_phenotype_uniqueids_without_wgs": len(set(drugs_by_id) - represented_ids),
            "adopted_biosamples": len(drugs_by_sample), "adopted_bioprojects": len(projects),
        },
    }


def overlap_summary(rows, membership: dict, *, raw: bool, mappings: dict) -> dict:
    counts: Counter = Counter()
    samples, adopted_samples = set(), set()
    for row in rows:
        if raw:
            sample = ast.first_value(row, ast.BIOSAMPLE_ALIASES)
            project = ast.first_value(row, ast.BIOPROJECT_ALIASES)
            mapping = mappings.get(ast.normalize(ast.first_value(row, ast.ANTIBIOTIC_ALIASES)), {})
            identifier = mapping.get("identifier", "")
            count = 1
        else:
            sample, project, identifier = (
                row["biosample_accession"], row["bioproject_accession"], row["identifier"],
            )
            count = int(row["ast_row_count"])
        counts["groups_or_rows"] += 1
        counts["measurements"] += count
        if sample in membership["all_samples"]:
            counts["shared_wgs_sample_measurements"] += count
            samples.add(sample)
        if sample in membership["drugs_by_sample"]:
            counts["shared_adopted_sample_measurements"] += count
            adopted_samples.add(sample)
            if identifier in membership["drugs_by_sample"][sample]:
                counts["shared_adopted_sample_and_drug_measurements"] += count
        if project in membership["projects"]:
            counts["shared_adopted_project_measurements"] += count
    return {
        key: counts[key] for key in (
            "groups_or_rows", "measurements", "shared_wgs_sample_measurements",
            "shared_adopted_sample_measurements", "shared_adopted_sample_and_drug_measurements",
            "shared_adopted_project_measurements",
        )
    } | {"shared_wgs_biosamples": sorted(samples), "shared_adopted_biosamples": sorted(adopted_samples)}


def assay_contexts(rows: list[dict]) -> list[dict]:
    counts: Counter = Counter()
    for row in rows:
        kind = "+".join(name for name, field in (
            ("MIC", "mic_value"), ("DISK", "disk_diffusion_value"),
        ) if row[field])
        counts[(row["method"], row["platform"], row["reagent"], kind)] += int(row["ast_row_count"])
    return [
        dict(zip(("method", "platform", "reagent", "measurement"), key, strict=True), count=count)
        for key, count in sorted(counts.items())
    ]


def taxonomy_scope(rows: list[dict], records: dict, membership: dict) -> dict:
    if cryptic.VERSION != "3.4.0":
        raise ValueError("CRyPTIC release scope must be reviewed for the new version")
    counts: Counter = Counter()
    taxa: dict[str, dict] = {}
    for row in rows:
        curie = row["taxon_id"]
        taxid = curie.removeprefix("NCBITaxon:")
        status = relationship(taxid, records)
        if status == "OUTSIDE_SCOPE" and row["biosample_accession"] in membership["all_samples"]:
            status = "TAXON_SAMPLE_CONFLICT"
        elif taxid in records and row["taxon_label"] != records[taxid]["scientific_name"]:
            status = "TAXON_LABEL_REVIEW"
        counts[(status, "groups")] += 1
        counts[(status, "measurements")] += int(row["ast_row_count"])
        entry = taxa.setdefault(curie, {
            "taxon_id": curie, "scientific_name": records.get(taxid, {}).get("scientific_name", ""),
            "lineage_taxids": records.get(taxid, {}).get("lineage_taxids", []),
            "groups": 0, "measurements": 0, "statuses": set(), "source_taxon_labels": set(),
        })
        entry["groups"] += 1
        entry["measurements"] += int(row["ast_row_count"])
        entry["statuses"].add(status)
        entry["source_taxon_labels"].add(row["taxon_label"])
    for entry in taxa.values():
        entry["statuses"] = sorted(entry["statuses"])
        entry["source_taxon_labels"] = sorted(entry["source_taxon_labels"])
    statuses = ["OUTSIDE_SCOPE", "WITHIN_SCOPE", "ANCESTOR_OF_SCOPE", "UNRESOLVED",
                "TAXON_SAMPLE_CONFLICT", "TAXON_LABEL_REVIEW"]
    return {
        "scope_taxon_id": "NCBITaxon:" + SCOPE_TAXID, "scope_name": SCOPE_NAME,
        "scope_reference": SCOPE_REFERENCE,
        "conclusion": ("DISJOINT_BY_REPORTED_TAXONOMY" if rows and
                       counts[("OUTSIDE_SCOPE", "groups")] == len(rows) else "REVIEW_REQUIRED"),
        "counts": {status: {kind: counts[(status, kind)] for kind in ("groups", "measurements")}
                   for status in statuses},
        "taxa": [taxa[key] for key in sorted(taxa)],
        "limitations": [
            "Conditional on source TaxIDs and CRyPTIC's published complex-wide scope, "
            "including pDST-only isolates.",
            "Does not resolve aliases or independently re-identify isolates; "
            "conflicting sample IDs require review.",
            "TaxID/name disagreements require review, including legitimate scientific-name changes.",
            "Does not establish within-source uniqueness, drug identity, assay validity, or source adoption.",
        ],
    }


def audit(args) -> dict:
    import duckdb

    corpus = corpus_membership(args.corpus_directory)
    release = args.cryptic_directory
    dst, ukmyc, codes = [release / name for name in (
        "DST_MEASUREMENTS.parquet", "UKMYC_PHENOTYPES.parquet", "DRUG_CODES.csv.gz",
    )]
    for path in (dst, ukmyc, codes, args.wgs):
        cryptic.verify_release_file(path)
    drug_codes = cryptic.read_drug_codes(codes)
    cryptic_mappings = cryptic.validated_drug_mappings(args.cryptic_drug_map, drug_codes)
    adopted = load_cryptic_activity_inventory(args.cryptic_inventory)
    with duckdb.connect() as connection:
        rebuilt = cryptic.activity_inventory(connection, dst, ukmyc, drug_codes, cryptic_mappings)
        require_same_inventory(adopted, rebuilt)
        membership = cryptic_membership(connection, dst, ukmyc, args.wgs, cryptic_mappings)

    version = "ast-browser-sha256:" + file_sha256(args.ast)
    _, structure_keys = ast.corpus_name_candidates()
    mappings = ast.read_drug_map(args.drug_map, structure_keys, version)
    report = ast.read_activity_report(args.activity_report, structure_keys, version)
    if not report:
        raise ValueError("empty AST candidate report cannot establish overlap coverage")
    raw = ast.read_table(args.ast)
    snapshot = load_isolate_snapshot(args.isolate_snapshot)
    enriched = ast.enrich_isolate_identity(raw, snapshot)
    dedupe = ast.read_project_dedupe_map(args.project_dedupe_map) if args.project_dedupe_map else {}
    current = ast.exact_activity_rows(
        enriched, mappings, source_version=version,
        source_retrieved_on=report[0]["source_retrieved_on"], isolate_snapshot=snapshot,
        project_dedupe=dedupe,
    )
    if args.assay_review:
        current, _ = apply_assay_review(current, read_assay_review(args.assay_review))
    ast.require_activity_report_matches_current(report, current, args.activity_report)
    input_paths = {
        "ast": args.ast, "activity_report": args.activity_report, "drug_map": args.drug_map,
        "isolates": args.isolate_snapshot / "isolates.json",
        "isolate_manifest": args.isolate_snapshot / "snapshot.json",
        "cryptic_inventory": args.cryptic_inventory, "cryptic_drug_map": args.cryptic_drug_map,
        "cryptic_dst": dst, "cryptic_ukmyc": ukmyc, "cryptic_drug_codes": codes, "cryptic_wgs": args.wgs,
    }
    if args.project_dedupe_map:
        input_paths["project_dedupe_map"] = args.project_dedupe_map
    if args.assay_review:
        input_paths["assay_review"] = args.assay_review
    taxonomy = None
    if args.taxonomy_snapshot:
        taxonomy = taxonomy_scope(
            report, load_snapshot(args.taxonomy_snapshot, args.activity_report, report), membership,
        )
        input_paths["taxonomy"] = args.taxonomy_snapshot / "taxonomy.xml"
        input_paths["taxonomy_manifest"] = args.taxonomy_snapshot / "snapshot.json"
    corpus_overlap = {
        "membership": corpus["counts"], "inputs": corpus["inputs"],
        "raw_ast": corpus_overlap_summary(raw, corpus, raw=True, mappings=mappings),
        "eligible_ast": corpus_overlap_summary(report, corpus, raw=False, mappings=mappings),
    }
    require_same_corpus(args.corpus_directory, corpus["inputs"])
    return {
        "scope": "Exact accession overlap; review leads only, not automatic duplicate exclusions.",
        "limitations": [
            "Different BioSample accessions may identify the same isolate; aliases are unresolved.",
            "Phenotype-only CRyPTIC samples without a WGS accession link cannot be accession-matched.",
            "Existing corpus observations without BioSample accessions cannot be accession-matched.",
            "A shared sample/drug does not prove duplicate measurements or justify project-wide exclusion.",
            "Assay signatures retain submitted values; informative text does not certify field consistency.",
        ],
        "source_version": version, "cryptic_version": cryptic.VERSION,
        "inputs": {key: {"path": str(path), "sha256": file_sha256(path)}
                   for key, path in input_paths.items()},
        "cryptic_membership": membership["counts"],
        "existing_corpus": corpus_overlap,
        "raw_ast": overlap_summary(raw, membership, raw=True, mappings=mappings),
        "eligible_ast": overlap_summary(report, membership, raw=False, mappings=mappings),
        "eligible_assay_contexts": assay_contexts(report),
        "taxonomy_scope": taxonomy,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("ast", "activity-report", "isolate-snapshot", "wgs", "report"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--drug-map", type=Path, default=ROOT / "curation/ncbi_ast_drug_map.tsv")
    parser.add_argument("--project-dedupe-map", type=Path)
    parser.add_argument("--assay-review", type=Path)
    parser.add_argument("--taxonomy-snapshot", type=Path)
    parser.add_argument("--corpus-directory", type=Path, default=ROOT / "data/antibiotics")
    parser.add_argument("--cryptic-directory", type=Path, default=ROOT / "downloads/cryptic_3.4.0")
    parser.add_argument("--cryptic-drug-map", type=Path, default=cryptic.DEFAULT_DRUG_MAP)
    parser.add_argument("--cryptic-inventory", type=Path, default=ROOT / "data/raw/cryptic_activity.tsv")
    args = parser.parse_args()
    if args.report.exists():
        parser.error(f"refusing to overwrite {args.report}")
    result = audit(args)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(f"Overlap audit: {args.report}")
    for section in ("cryptic_membership", "raw_ast", "eligible_ast"):
        print(section, {key: len(value) if isinstance(value, list) else value
                        for key, value in result[section].items()})


if __name__ == "__main__":
    main()
