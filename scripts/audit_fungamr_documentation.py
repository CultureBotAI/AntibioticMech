"""Replay the documentation gate, not FungAMR rows or experimental assignments."""

import argparse
import base64
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import audit_caspofungin_context as context
import audit_fungamr_cohort as cohort_audit
import audit_topoisomerase_references as reference
from resistance_checkpoint_records import checkpoint_path

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-13-fungamr-source-crosswalk")
OUTPUT = Path("research/2026-10-13-fungamr-documentation.json")
URLS = {
    "repository-metadata": "https://api.github.com/repos/Landrylab/FungAMR",
    "repository-readme": "https://api.github.com/repos/Landrylab/FungAMR/readme",
    "tool-readme": "https://api.github.com/repos/nmquijada/ChroQueTas/readme",
    "publisher": "https://www.nature.com/articles/s41564-025-02084-7",
}
BLOBS = {
    "repository-readme": "7d9bff7b3b3ee7582bead1da972206588b8fbb9f",
    "tool-readme": "5280e917fa27bc337b2bbe2c61a40c1fa87ea9ad",
}
METHODS = {
    "1": "SAME_SPECIES_FUNCTIONAL_TEST",
    "2": "HETEROLOGOUS_FUNCTIONAL_TEST",
    "3": "POOLED_MEASUREMENT",
    "4": "EXPERIMENTAL_EVOLUTION_ASSOCIATION",
    "5": "GENE_DELETION_EFFECT",
    "6": "EXPRESSION_OR_COPY_NUMBER_EFFECT",
    "7": "POPULATION_ASSOCIATION",
    "8": "NATURAL_ISOLATE_COOCCURRENCE",
    "Negative scores (-)": "NEGATIVE_RESULT_FOR_CORRESPONDING_METHOD",
}


def decode_readme(payload, repository, expected_blob):
    """Verify both the API envelope and Git's identity for the decoded file."""
    if (
        payload.get("encoding") != "base64"
        or payload.get("path") != "README.md"
        or payload.get("name") != "README.md"
        or payload.get("type") != "file"
        or type(payload.get("size")) is not int
        or payload.get("sha") != expected_blob
        or not payload.get("html_url", "").startswith(f"https://github.com/{repository}/blob/")
    ):
        raise ValueError("README identity or encoding changed")
    data = base64.b64decode("".join(payload["content"].split()), validate=True)
    blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    if len(data) != payload["size"] or blob != expected_blob:
        raise ValueError("README byte count or Git blob changed")
    return data.decode("utf-8")


def project_methods(text):
    rows = {}
    for line_number, line in enumerate(text.splitlines(), 1):
        if not line.startswith("| "):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells[0] == "Confidence Score":
            continue
        if len(cells) != 2 or cells[0] not in METHODS or cells[0] in rows or not cells[1]:
            raise ValueError("confidence table has unknown, duplicate or malformed rows")
        rows[cells[0]] = {
            "method": METHODS[cells[0]],
            "source_line": line_number,
            "source_row_sha256": hashlib.sha256(line.encode()).hexdigest(),
        }
    if set(rows) != set(METHODS):
        raise ValueError("confidence table is incomplete")
    return {
        "categories": rows,
        "numeric_probability": False,
        "antibiotic_measurement": False,
        "mic_conversion_permitted": False,
        "assigned_to_any_selected_term": False,
        "negative_result_is_species_wide_susceptibility": False,
    }


def build(root, directory):
    plan_path = directory / "native-plan.json"
    plan = json.loads(plan_path.read_bytes())
    cohort = json.loads(reference.check_pin(root, plan["cohort"]).read_bytes())
    reference.check_pin(root, plan["discovery_plan"])
    for key in ("prior_verification", "prior_cohort", "current_census", "protected"):
        reference.check_pin(root, cohort[key])
    protected = json.loads((root / cohort["protected"]["path"]).read_bytes())
    reference.check_pin(
        root,
        {"path": "curation/source_queue.tsv", "sha256": protected["curation/source_queue.tsv"]},
    )
    if {key: row["url"] for key, row in plan["requests"].items()} != URLS:
        raise ValueError("documentation-only request scope changed")
    if set(cohort["terms"]) != set(cohort_audit.GENES):
        raise ValueError("selected term set changed")
    sources = {
        key: context.native(root, directory, key, url, statuses=(303,) if key == "publisher" else (200,))
        for key, url in URLS.items()
    }
    metadata = json.loads(reference.check_pin(root, sources["repository-metadata"]["body"]).read_bytes())
    if (
        metadata["full_name"] != "Landrylab/FungAMR"
        or metadata["private"] is not False
        or metadata["license"]["spdx_id"] != "NOASSERTION"
    ):
        raise ValueError("repository metadata or license classification changed")
    canary_path = directory / "documentation-canary.json"
    canary = json.loads(canary_path.read_bytes())
    if (
        canary["source"] != sources["repository-metadata"]["body"]
        or canary["receipt"] != sources["repository-metadata"]["receipt"]
        or canary["manually_inspected"] is not True
    ):
        raise ValueError("documentation canary changed")
    readmes = {}
    for key, repository in (
        ("repository-readme", "Landrylab/FungAMR"),
        ("tool-readme", "nmquijada/ChroQueTas"),
    ):
        payload = json.loads(reference.check_pin(root, sources[key]["body"]).read_bytes())
        readmes[key] = decode_readme(payload, repository, BLOBS[key])
        sources[key]["git_blob_sha1"] = BLOBS[key]
        sources[key]["decoded_sha256"] = hashlib.sha256(readmes[key].encode()).hexdigest()
    tool_lines = readmes["tool-readme"].splitlines()
    license_line = "ChroQuetas and FungAMR are under Creative Commons "
    license_rows = [i for i, line in enumerate(tool_lines, 1) if line.startswith(license_line)]
    if len(license_rows) != 1 or "CC BY-NC-ND 4.0" not in tool_lines[license_rows[0] - 1]:
        raise ValueError("companion README license statement changed")
    publisher_receipt = json.loads(reference.check_pin(root, sources["publisher"]["receipt"]).read_bytes())
    location = {k.lower(): v for k, v in publisher_receipt["headers"].items()}.get("location", "")
    parsed = urlsplit(location)
    if parsed.scheme != "https" or parsed.netloc != "idp.nature.com" or parsed.path != "/authorize":
        raise ValueError("publisher redirect scope changed")
    with reference.check_pin(root, cohort["current_census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["path"] for r in census}) != 2939
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        or any(reference.digest(checkpoint_path(root, row)) != row["record_sha256"] for row in census)
    ):
        raise ValueError("current corpus membership or bytes changed")
    records = []
    expected_ids = {i for term in cohort["terms"].values() for i in term["record_memberships"]}
    for selected in cohort["records"]:
        record = load_record(checkpoint_path(root, selected))
        assertions = [
            a for a in record.get("resistance_mechanisms", []) if a.get("aro_id") in cohort["terms"]
        ]
        if (
            record["identifier"] != selected["identifier"]
            or record["chemical_structure"]["standard_inchi_key"] != selected["standard_inchi_key"]
            or assertions != selected["selected_card_assertions"]
            or len(record.get("resistance_mechanisms", [])) != selected["existing_resistance_assertions"]
        ):
            raise ValueError("record identity or selected source claims changed")
        records.append(
            {key: selected[key] for key in ("path", "sha256", "identifier", "label", "standard_inchi_key")}
        )
    if len(records) != 10 or {r["identifier"] for r in records} != expected_ids:
        raise ValueError("selected record membership changed")
    local_licenses = [
        reference.pin(root, root / p) for p in ("LICENSE-DATA", "ATTRIBUTION.md", "pyproject.toml")
    ]
    if "licensed [CC BY 4.0](LICENSE-DATA)" not in (root / "ATTRIBUTION.md").read_text():
        raise ValueError("repository data license changed")
    return {
        "date": "2026-10-13",
        "retrieval_date_utc": "2026-10-14",
        "scope": "DOCUMENTATION_ONLY_NO_SOURCE_ROW_CROSSWALK",
        "inputs": {
            "plan": reference.pin(root, plan_path),
            "cohort": plan["cohort"],
            "canary": reference.pin(root, canary_path),
            "local_licenses": local_licenses,
        },
        "sources": sources,
        "evidence_categories": project_methods(readmes["repository-readme"]),
        "reuse_gate": {
            "companion_readme_declared_license": "CC-BY-NC-ND-4.0",
            "source_line": license_rows[0],
            "repository_api_license": "NOASSERTION",
            "repository_api_is_permission": False,
            "destination_data_license": "CC-BY-4.0",
            "decision": "NO_DIRECT_DATABASE_IMPORT_UNDER_CURRENT_SOURCE_GATE",
            "source_queue_changed": False,
            "license_file_inspected": False,
            "scope": (
                "Companion documentation states terms for both resources; "
                "not legal advice or a row-level rights audit."
            ),
            "existing_aro_assertions_relicensed_or_removed": False,
        },
        "publisher_access": {
            "status": 303,
            "redirect_followed": False,
            "primary_full_text_read": False,
            "retry_performed": False,
        },
        "tool_limitations": {
            "source_section": "Limitations",
            "full_database_coverage": False,
            "tool_prediction_is_measured_phenotype": False,
            "installed_or_executed": False,
        },
        "records": records,
        "terms": {
            term: {
                "gene_label": row["source_gene"],
                "record_memberships": row["record_memberships"],
                "fungamr_row_id": None,
                "source_score": None,
                "primary_row_crosswalk_verified": False,
                "new_uniprot_assignment": None,
                "new_taxon_assignment": None,
                "exact_allele_assignment": None,
                "experimental_genome_assignment": None,
                "disposition": "PRIMARY_EVIDENCE_REQUIRED_NO_DATABASE_ROW_IMPORT",
            }
            for term, row in cohort["terms"].items()
        },
        "summary": {
            "corpus_records_hash_verified": 2939,
            "cohort_records": len(records),
            "cohort_terms": len(cohort["terms"]),
            "native_documentation_requests": 4,
            "database_rows_downloaded": 0,
            "new_resistance_assertions": 0,
            "biological_records_changed": 0,
            "whole_record_reviews_completed": 0,
        },
        "limitations": [
            "README blob identities are not database release versions.",
            "A shared database citation does not resolve a primary row, its method score or tested subject.",
            "Previously established reference identities remain reference-only; this checkpoint adds none.",
            "The CYP51B drug-label discrepancy and qualified URA6 species question remain open.",
            "Full corpus investigation remains incomplete; same-agent review is not independent validation.",
        ],
        "constraints": {
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "issue_1040": "DEFERRED",
            "github_mutations": 0,
            "failed_source_retries": 0,
            "source_adoptions": 0,
            "sequences_variants_protocols_exported": False,
            "numeric_ast_exported": False,
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=CACHE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    result = build(root, root / args.cache)
    encoded = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    path = root / args.output
    if path.exists() and path.read_text() != encoded:
        raise ValueError("refusing to overwrite a differing research checkpoint")
    path.write_text(encoded)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
