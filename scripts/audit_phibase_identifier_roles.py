"""Apply documented field roles to a frozen PHI identifier-field audit, offline."""

import argparse
import json
from collections import Counter
from pathlib import Path

from audit_phibase_gene_ids import SCOPE, digest, identifier_matches, match_summary

ROLE_SCOPE = "DOCUMENTED_FIELD_ROLES_NOT_EXPERIMENTAL_IDENTIFIERS"
# This convention is database-specific; never infer object types from ID spelling.
DATABASE = "EnsemblFungi"
FIELD_ROLES = {"id": "TRANSCRIPT", "ProteinId": "PROTEIN", "GeneId": "GENE"}


def roles_for_matches(matches):
    return [{"match_index": index, "field": hit["field"],
             "role": FIELD_ROLES[hit["field"]]}
            for index, hit in enumerate(matches)
            if hit.get("database") == DATABASE and hit["field"] in FIELD_ROLES
            and ((hit["kind"] == "CROSS_REFERENCE_PRIMARY_ID" and hit["field"] == "id")
                 or (hit["kind"] == "TYPED_CROSS_REFERENCE_PROPERTY" and hit["field"] != "id"))]


def build_report(audit, documentation):
    if audit["scope"] != SCOPE or audit["schema_version"] != 1:
        raise ValueError("unsupported identifier audit")
    if documentation["database"] != DATABASE or documentation["field_roles"] != FIELD_ROLES:
        raise ValueError("unsupported documented field convention")
    source_summary = audit["summary"]
    rows = audit["rows"]
    if (len(rows) != source_summary["nonempty_source_gene_ids"]
            or len(rows) + source_summary["empty_source_gene_ids"] != source_summary["source_rows"]
            or len({r["source_row_sha256"] for r in rows}) != len(rows)):
        raise ValueError("inconsistent source-row accounting")
    output = []
    for row in rows:
        value = row["source_gene_id"]
        if not value:
            raise ValueError("empty value in nonempty audit rows")
        reference = audit["reference_entries"][row["reference_accession"]]
        if reference["accession"] != row["reference_accession"]:
            raise ValueError("reference accession mismatch")
        hits = identifier_matches(value, reference)
        if hits != row["matches"] or match_summary(value, hits) != row["match_summary"]:
            raise ValueError("identifier-field evidence drift")
        evidence = roles_for_matches(hits)
        output.append({"source_row_sha256": row["source_row_sha256"],
                       "source_gene_id": value, "reference_accession": row["reference_accession"],
                       "documented_roles": sorted({e["role"] for e in evidence}),
                       "field_role_evidence": evidence,
                       "gene_annotation_fields": row["match_summary"]["gene_annotation_fields"],
                       "current_review": row["current_review"],
                       "experimental_identity_verified": False})
    return {
        "schema_version": 1, "scope": ROLE_SCOPE, "documentation": documentation,
        "reference_releases": audit["reference_releases"], "snapshot_summary": source_summary,
        "summary": {
            "source_rows": source_summary["source_rows"],
            "nonempty_source_gene_ids": len(output),
            "empty_source_gene_ids": source_summary["empty_source_gene_ids"],
            "documented_role_counts": dict(Counter(role for r in output for role in r["documented_roles"])),
            "multiple_documented_roles": sum(len(r["documented_roles"]) > 1 for r in output),
            "no_documented_role": sum(not r["documented_roles"] for r in output),
            "rejected_source_gene_ids_preserved": sum(r["current_review"]["source_gene_id_rejected"]
                                                       for r in output),
            "experimental_identifiers_assigned": 0,
        },
        "rows": output,
        "limitations": [
            "Roles describe fields in the pinned UniProt reference, not verified experimental subjects.",
            "Current documentation is applied to historical metadata; no live Ensembl object lookup "
            "or current-release validation of the 23 references is claimed.",
            "Roles can overlap for the same string. Gene annotation membership is retained separately.",
            "No identifier spelling, version, namespace or source-owned review is changed.",
            "Rejected references remain rejected, including when their field roles are known.",
            "No new gene, allele, genome, sequence, variant, phenotype or measurement is assigned.",
            "Empty source values remain empty; none are filled from related reference properties.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--documentation", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("refusing to overwrite an existing research artifact")
    payloads = {k: getattr(args, k).read_bytes() for k in ("audit", "documentation")}
    report = build_report(*(json.loads(payloads[k]) for k in ("audit", "documentation")))
    report["inputs"] = {key: {"path": str(getattr(args, key)), "sha256": digest(value)}
                        for key, value in payloads.items()}
    with args.output.open("x") as stream:
        stream.write(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
