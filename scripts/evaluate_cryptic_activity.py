#!/usr/bin/env python3
"""Evaluate CRyPTIC release 3.4 activity data without writing corpus claims.

CRyPTIC's release tables carry drug codes and names but no structures or stable
chemical identifiers.  This evaluator quantifies usable phenotypes and reports
name-only corpus candidates, while treating every one as identity-unresolved.
That distinction is deliberate: a plausible name match cannot attach an assay
to this repository's individual-structure records.
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


def evaluate(dst: Path, ukmyc: Path, drug_codes: Path) -> dict:
    try:
        import duckdb
    except ImportError as error:  # pragma: no cover - command gives installation path
        raise SystemExit("duckdb is required; run through `just evaluate-cryptic`") from error

    for path in (dst, ukmyc, drug_codes):
        verify_release_file(path)
    codes = read_drug_codes(drug_codes)
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
        matches = sorted(names.get(normalize(source_name), set()))
        drug_rows.append({
            "code": code,
            "name": source_name,
            "dst_rows": dst_rows,
            "ukmyc_rows": ukmyc_rows,
            "mic_rows": mic_rows,
            "name_only_candidates": matches,
            "eligible_rows": 0,
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
    args = parser.parse_args()
    missing = [str(path) for path in (args.dst, args.ukmyc, args.drug_codes) if not path.exists()]
    if missing:
        raise SystemExit(f"missing pinned CRyPTIC input(s): {', '.join(missing)}")
    result = evaluate(args.dst, args.ukmyc, args.drug_codes)
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
    print(f"  name-only corpus candidates={len(candidates)}; structure-grounded drugs=0")
    for row in candidates:
        print(
            f"    {row['code']} {row['name']}: "
            f"{','.join(row['name_only_candidates'])}; "
            f"rows={row['dst_rows'] + row['ukmyc_rows']} MIC={row['mic_rows']}; NOT ELIGIBLE"
        )
    print("--dry-run: 0 observations eligible; nothing written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
