"""Shared Stanford HIVDB score-rule report contract."""

from __future__ import annotations

import hashlib
from collections.abc import Mapping

HIVDB_SCORE_RULE_ID_VERSION = "hivdb_score_rule_v1"
HIVDB_SCORE_RULE_GENE_BY_DRUG_CLASS = {
    "NRTI": "RT",
    "NNRTI": "RT",
    "PI": "PR",
    "INSTI": "IN",
    "CAI": "CA",
}
HIVDB_SCORE_RULE_ID_COLUMNS = [
    "source_version",
    "algorithm_name",
    "algorithm_version",
    "algorithm_date",
    "source_record_id",
    "score_term_index",
    "score_term",
]
HIVDB_SCORE_RULE_COLUMNS = [
    "source_rule_id",
    "source_version",
    "algorithm_name",
    "algorithm_version",
    "algorithm_date",
    "source_record_id",
    "source_name",
    "algorithm_full_name",
    "full_name_matches",
    "drug_class",
    "gene",
    "mapping_status",
    "identifier",
    "standard_inchi_key",
    "score_term_index",
    "score_term",
    "score_assignments",
    "negative_score_assignments",
    "min_score",
    "max_score",
]


def hivdb_score_rule_id(row: Mapping[str, str]) -> str:
    """Stable digest for one HIVDB drug-specific algorithm formula term."""
    digest = hashlib.sha256()
    digest.update(HIVDB_SCORE_RULE_ID_VERSION.encode("utf-8"))
    digest.update(b"\0")
    for column in HIVDB_SCORE_RULE_ID_COLUMNS:
        digest.update(str(row[column]).encode("utf-8"))
        digest.update(b"\0")
    return f"hivdb_hivfacts:{digest.hexdigest()[:16]}"
