#!/usr/bin/env python3
"""Evaluate CRyPTIC release 3.4 activity data without writing corpus claims.

CRyPTIC's release tables carry drug codes and names but no structures or stable
chemical identifiers. This evaluator quantifies usable phenotypes and reports
candidate corpus records by lexical name while keeping those matches separate
from the versioned curation crosswalk in ``curation/cryptic_drug_map.tsv``.
Only crosswalked drug codes are eligible for future ActivityObservation rows.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import re
from collections import defaultdict
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
VERSION = "3.4.0"
ZENODO_RECORD = "15680920"
DEFAULT_DRUG_MAP = REPO_ROOT / "curation" / "cryptic_drug_map.tsv"
DRUG_MAP_COLUMNS = [
    "source_version",
    "source_record_id",
    "source_name",
    "mapping_status",
    "identifier",
    "standard_inchi_key",
    "mapping_basis",
    "notes",
]
EXACT_MAPPING_STATUS = "EXACT"
MAPPING_STATUSES = {
    EXACT_MAPPING_STATUS,
    "AMBIGUOUS_STEREOCHEMISTRY",
    "COMBINATION",
    "DRUG_CLASS",
    "MISSING_CORPUS_RECORD",
    "MIXTURE",
}
EXPECTED_MD5 = {
    "DRUG_CODES.csv.gz": "923d3a193df21698bd6a00f857ab337e",
    "DST_MEASUREMENTS.parquet": "45b4501ea7c3925af565dbbc6188dec0",
    "UKMYC_PHENOTYPES.parquet": "020b6c0af6c05e19610a59f5ef97b832",
}


def md5_of(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)  # noqa: S324 - upstream integrity checksum
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_release_file(path: Path) -> None:
    expected = EXPECTED_MD5.get(path.name)
    if expected is None:
        raise ValueError(f"unrecognized CRyPTIC release file: {path.name}")
    actual = md5_of(path)
    if actual != expected:
        raise ValueError(f"{path.name} md5 {actual} != pinned release checksum {expected}")


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def read_drug_codes(path: Path) -> dict[str, str]:
    with gzip.open(path, "rt", newline="", encoding="utf-8") as handle:
        return {
            row["DRUG_3_LETTER_CODE"].strip(): row["DRUG_NAME"].strip()
            for row in csv.DictReader(handle)
        }


def corpus_name_candidates() -> dict[str, set[str]]:
    candidates: dict[str, set[str]] = defaultdict(set)
    for path in sorted((REPO_ROOT / "data" / "antibiotics").rglob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        names = {record["label"]}
        names.update(
            synonym["synonym_text"]
            for synonym in (record.get("synonyms") or [])
            if synonym.get("synonym_text")
        )
        for name in names:
            candidates[normalize(name)].add(record["identifier"])
    return candidates


def corpus_structure_keys() -> dict[str, str]:
    keys = {}
    for path in sorted((REPO_ROOT / "data" / "antibiotics").rglob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        keys[record["identifier"]] = record["chemical_structure"]["standard_inchi_key"]
    return keys


def read_drug_map(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != DRUG_MAP_COLUMNS:
            raise ValueError(f"unexpected CRyPTIC drug map columns: {reader.fieldnames}")
        rows = {}
        for row in reader:
            code = row["source_record_id"]
            if code in rows:
                raise ValueError(f"duplicate CRyPTIC drug map code: {code}")
            if row["source_version"] != VERSION:
                raise ValueError(f"{code}: source_version {row['source_version']!r} != {VERSION!r}")
            if row["mapping_status"] not in MAPPING_STATUSES:
                raise ValueError(f"{code}: unknown mapping_status {row['mapping_status']!r}")
            has_mapping = bool(row["identifier"] or row["standard_inchi_key"])
            if row["mapping_status"] == EXACT_MAPPING_STATUS:
                if not row["identifier"] or not row["standard_inchi_key"]:
                    raise ValueError(f"{code}: EXACT mapping needs identifier and standard_inchi_key")
            elif has_mapping:
                raise ValueError(f"{code}: non-EXACT mapping must not carry structure fields")
            rows[code] = row
        return rows


def validated_drug_mappings(path: Path, drug_codes: dict[str, str]) -> dict[str, dict[str, str]]:
    mappings = read_drug_map(path)
    missing = set(drug_codes) - set(mappings)
    extra = set(mappings) - set(drug_codes)
    if missing or extra:
        raise ValueError(
            "CRyPTIC drug map/code mismatch: "
            f"missing={sorted(missing)} extra={sorted(extra)}"
        )

    structure_keys = corpus_structure_keys()
    for code, source_name in drug_codes.items():
        mapping = mappings[code]
        if mapping["source_name"] != source_name:
            raise ValueError(
                f"{code}: mapped source_name {mapping['source_name']!r} != "
                f"DRUG_CODES name {source_name!r}"
            )
        if mapping["mapping_status"] != EXACT_MAPPING_STATUS:
            continue
        identifier = mapping["identifier"]
        expected = structure_keys.get(identifier)
        if expected is None:
            raise ValueError(f"{code}: mapped identifier {identifier} is not in the corpus")
        if mapping["standard_inchi_key"] != expected:
            raise ValueError(
                f"{code}: mapped InChIKey {mapping['standard_inchi_key']} "
                f"does not match {identifier} ({expected})"
            )
    return mappings


def evaluate(dst: Path, ukmyc: Path, drug_codes: Path, drug_map: Path) -> dict:
    try:
        import duckdb
    except ImportError as error:  # pragma: no cover - command gives installation path
        raise SystemExit("duckdb is required; run through `just evaluate-cryptic`") from error

    for path in (dst, ukmyc, drug_codes):
        verify_release_file(path)
    codes = read_drug_codes(drug_codes)
    mappings = validated_drug_mappings(drug_map, codes)
    names = corpus_name_candidates()
    connection = duckdb.connect()
    dst_summary = connection.execute(
        """
        SELECT count(*), count(DISTINCT UNIQUEID), count(DISTINCT DRUG),
               count(*) FILTER (WHERE PHENOTYPE IN ('S', 'R', 'I')),
               count(*) FILTER (WHERE QUALITY = 'HIGH')
        FROM read_parquet(?)
        """,
        [str(dst)],
    ).fetchone()
    ukmyc_summary = connection.execute(
        """
        SELECT count(*), count(DISTINCT UNIQUEID), count(DISTINCT DRUG),
               count(*) FILTER (WHERE nullif(trim(MIC), '') IS NOT NULL),
               count(*) FILTER (WHERE BINARY_PHENOTYPE IN ('S', 'R', 'I'))
        FROM read_parquet(?)
        """,
        [str(ukmyc)],
    ).fetchone()
    per_drug = connection.execute(
        """
        SELECT DRUG, sum(dst_rows), sum(ukmyc_rows), sum(mic_rows)
        FROM (
          SELECT DRUG, count(*) AS dst_rows, 0 AS ukmyc_rows, 0 AS mic_rows
          FROM read_parquet(?) GROUP BY DRUG
          UNION ALL
          SELECT DRUG, 0, count(*),
                 count(*) FILTER (WHERE nullif(trim(MIC), '') IS NOT NULL)
          FROM read_parquet(?) GROUP BY DRUG
        ) GROUP BY DRUG ORDER BY DRUG
        """,
        [str(dst), str(ukmyc)],
    ).fetchall()
    drug_rows = []
    for code, dst_rows, ukmyc_rows, mic_rows in per_drug:
        source_name = codes.get(code, "")
        mapping = mappings[code]
        matches = sorted(names.get(normalize(source_name), set()))
        eligible_rows = dst_rows + ukmyc_rows if mapping["mapping_status"] == EXACT_MAPPING_STATUS else 0
        drug_rows.append({
            "code": code,
            "name": source_name,
            "mapping_status": mapping["mapping_status"],
            "identifier": mapping["identifier"],
            "standard_inchi_key": mapping["standard_inchi_key"],
            "dst_rows": dst_rows,
            "ukmyc_rows": ukmyc_rows,
            "mic_rows": mic_rows,
            "name_only_candidates": matches,
            "eligible_rows": eligible_rows,
        })
    return {
        "dst": dst_summary,
        "ukmyc": ukmyc_summary,
        "drugs": drug_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dst", type=Path, required=True)
    parser.add_argument("--ukmyc", type=Path, required=True)
    parser.add_argument("--drug-codes", type=Path, required=True)
    parser.add_argument("--drug-map", type=Path, default=DEFAULT_DRUG_MAP)
    args = parser.parse_args()
    missing = [
        str(path)
        for path in (args.dst, args.ukmyc, args.drug_codes, args.drug_map)
        if not path.exists()
    ]
    if missing:
        raise SystemExit(f"missing pinned CRyPTIC input(s): {', '.join(missing)}")
    result = evaluate(args.dst, args.ukmyc, args.drug_codes, args.drug_map)
    dst_rows, dst_isolates, dst_drugs, classified, high_quality = result["dst"]
    uk_rows, uk_isolates, uk_drugs, mic_rows, uk_classified = result["ukmyc"]
    print(f"CRyPTIC {VERSION} (Zenodo {ZENODO_RECORD})")
    print(
        f"  DST: rows={dst_rows} isolates={dst_isolates} drugs={dst_drugs} "
        f"S/R/I={classified} high_quality={high_quality}"
    )
    print(
        f"  UKMYC: rows={uk_rows} isolates={uk_isolates} drugs={uk_drugs} "
        f"MIC={mic_rows} S/R/I={uk_classified}"
    )
    candidates = [row for row in result["drugs"] if row["name_only_candidates"]]
    grounded = [row for row in result["drugs"] if row["eligible_rows"]]
    eligible_rows = sum(row["eligible_rows"] for row in grounded)
    print(
        f"  name-only corpus candidates={len(candidates)}; "
        f"structure-grounded drugs={len(grounded)}; eligible rows={eligible_rows}"
    )
    reported = [row for row in result["drugs"] if row["name_only_candidates"] or row["eligible_rows"]]
    for row in reported:
        if row["mapping_status"] == EXACT_MAPPING_STATUS:
            suffix = f"ELIGIBLE {row['identifier']}"
        else:
            suffix = f"NOT ELIGIBLE {row['mapping_status']}"
        print(
            f"    {row['code']} {row['name']}: "
            f"{','.join(row['name_only_candidates']) or '-'}; "
            f"rows={row['dst_rows'] + row['ukmyc_rows']} MIC={row['mic_rows']}; "
            f"{suffix}"
        )
    print(f"--dry-run: {eligible_rows} observations eligible; nothing written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
