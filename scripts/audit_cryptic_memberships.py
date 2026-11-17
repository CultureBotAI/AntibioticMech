#!/usr/bin/env python3
"""Audit the complete adopted membership cohort against inventories and optional raw Parquet."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from audit_ncbi_ast_publication import verify_activity_publication, verify_activity_table
from cryptic_membership_inventory import ISOLATES, MEMBERSHIPS, SOURCE, load_adopted
from evaluate_cryptic_activity import verify_release_file
from seed_from_sources import (
    CRYPTIC_ACTIVITY_INVENTORY,
    RAW_DIR,
    REPO_ROOT,
    load_cryptic_activity_inventory,
    read_lockfile_paths,
)

from antibioticmech.activity_collections import load_record
from antibioticmech.activity_memberships import read_memberships

# A separate raw-value join avoids relying on the extractor's group-ID helper.
RAW_FIELDS = {
    "DST_MEASUREMENTS": ("source", "method_1", "method_2", "method_3", "method_cc",
                         "method_mic", "phenotype", "quality"),
    "UKMYC_PHENOTYPES": ("platedesign", "belongs_gpi", "phenotype_quality", "readingday",
                         "primary_method", "phenotype_description", "mic", "log2mic", "binary_phenotype"),
}


def raw_audit(rows, actual, release):
    import duckdb

    paths = [release / (name + ".parquet") for name in RAW_FIELDS]
    paths.append(release / "dedupe" / "WGS_SAMPLES.parquet")
    for path in paths:
        verify_release_file(path)
    with (REPO_ROOT / "curation/cryptic_drug_map.tsv").open() as handle:
        exact = {row["source_record_id"] for row in csv.DictReader(handle, delimiter="\t")
                 if row["mapping_status"] == "EXACT"}
    by_values = {}
    for row in rows:
        table = row["source_table"]
        key = (table, row["drug_code"], *(row[field] for field in RAW_FIELDS[table]))
        if key in by_values:
            raise ValueError("duplicate raw-value CRyPTIC observation key")
        by_values[key] = row["activity_group_id"]
    remaining = dict(actual)
    checked = 0
    with duckdb.connect() as connection:
        wgs = {row[0]: dict(zip(("biosample_accession", "bioproject_accession", "run_accession"),
                                row[1:], strict=True))
               for row in connection.execute(
                   "SELECT UNIQUEID, sample_accession, study_accession, run_accession FROM read_parquet(?)",
                   [str(paths[-1])]).fetchall()}
        for table, fields in RAW_FIELDS.items():
            names = ", ".join(["DRUG", *fields, "UNIQUEID"])
            cursor = connection.execute(
                f"SELECT {names}, count(*) FROM read_parquet(?) GROUP BY {names}",
                [str(release / (table + ".parquet"))])
            while batch := cursor.fetchmany(10000):
                for row in batch:
                    if row[0] not in exact:
                        continue
                    values = tuple("" if value is None or str(value).lower() == "nan" else (
                        str(value).lower() if isinstance(value, bool) else str(value)
                    ) for value in row[:-2])
                    group_id = by_values[(table, *values)]
                    source_id, count = row[-2:]
                    member = remaining.pop((group_id, source_id), None)
                    if member != (count, wgs.get(source_id)):
                        raise ValueError(f"raw CRyPTIC membership differs: {group_id} / {source_id}")
                    checked += 1
    if remaining:
        raise ValueError("membership artifact contains pairs absent from raw CRyPTIC")
    return checked


def audit(*, pages=None, raw_release=None):
    rows = load_cryptic_activity_inventory(CRYPTIC_ACTIVITY_INVENTORY)
    identities = {row["activity_group_id"]: (row["identifier"], row["standard_inchi_key"]) for row in rows}
    expected_groups, metadata = load_adopted(rows)
    if metadata is None:
        raise ValueError("CRyPTIC memberships are not adopted")
    paths = read_lockfile_paths()
    actual, subjects, artifacts = {}, {}, []
    page_count = 0
    for identifier in sorted({row["identifier"] for row in rows}):
        path = paths[identifier]
        doc = load_record(path)
        refs = [(ref, data) for ref, data in read_memberships(doc, path) if ref["source"] == SOURCE]
        if len(refs) != 1:
            raise ValueError(f"expected one CRyPTIC membership collection: {identifier}")
        reference, data = refs[0]
        if any(reference[key] != value for key, value in metadata.items()):
            raise ValueError("record membership provenance differs from adopted manifest")
        artifacts.append({"identifier": identifier, **reference})
        for group in data["groups"]:
            group_id = group["source_observation_id"]
            if identities.get(group_id) != (identifier, doc["chemical_structure"]["standard_inchi_key"]):
                raise ValueError("membership group is attached to a different exact structure")
            for member in group["members"]:
                subject = data["subjects"][member["subject_index"]]
                source_id = subject["source_isolate_id"]
                key = group_id, source_id
                if key in actual:
                    raise ValueError("duplicate group/source ID across records")
                context = subject["sequencing_context"]
                if source_id in subjects and subjects[source_id] != context:
                    raise ValueError("sequencing context changed across compounds")
                subjects[source_id] = context
                actual[key] = (member["measurement_count"], context)
        if pages is not None:
            relative = Path(path.parent.name) / path.stem
            directory = pages / relative
            total = len(doc["activity_spectrum"])
            activity_pages = [relative / f"activity-{i}.html" for i in range(1, (total + 99) // 100 + 1)]
            download = list(directory.glob("record-*.json.gz"))
            index = list(directory.glob("search-*.json.gz"))
            if len(download) != 1 or len(index) != 1:
                raise ValueError("missing or stale complete-record/search artifacts")
            publication = {"pages": [*activity_pages, relative / "memberships.html"],
                           "written": set(directory.iterdir()),
                           "activity": {"download": download[0].name, "index": index[0].name}}
            verify_activity_publication(doc, pages, publication)
            from audit_membership_publication import audit_membership_publication

            links = audit_membership_publication(doc, directory)["links"]
            preview = doc["activity_spectrum"][:20] if total > 100 else doc["activity_spectrum"]
            verify_activity_table((pages / relative.with_suffix(".html")).read_text(), preview,
                                  evidence=True, memberships=links)
            page_count += len(publication["pages"])
    expected = {
        (group_id, member["source_isolate_id"]): (member["measurement_count"], member["sequencing_context"])
        for group_id, members in expected_groups.items() for member in members
    }
    if actual != expected:
        raise ValueError("complete membership corpus differs from the normalized inventories")
    linked = [context for context in subjects.values() if context is not None]
    result = {
        "compounds": len(artifacts), "groups": len(expected_groups), "memberships": len(actual),
        "measurements": sum(member[0] for member in actual.values()), "source_isolate_ids": len(subjects),
        "source_isolate_ids_without_wgs": len(subjects) - len(linked),
        "biosamples": len({context["biosample_accession"] for context in linked}),
        "bioprojects": len({context["bioproject_accession"] for context in linked}),
        "sequencing_runs": len({context["run_accession"] for context in linked}),
        "publication_pages": page_count, "artifacts": artifacts,
        "inventories": [str(RAW_DIR / name) for name in (ISOLATES, MEMBERSHIPS)],
    }
    if raw_release is not None:
        result["raw_memberships_checked"] = raw_audit(rows, actual, raw_release)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pages", type=Path)
    parser.add_argument("--raw-release", type=Path)
    args = parser.parse_args()
    print(json.dumps(audit(pages=args.pages, raw_release=args.raw_release), indent=2))


if __name__ == "__main__":
    main()
