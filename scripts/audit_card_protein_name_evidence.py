"""Bind scoped primary assessments to live claims without promoting reference IDs."""

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from audit_card_reference_memberships import checksum
from audit_curator_resistance_fields import owner
from audit_vgb_evidence import reference, require

from antibioticmech.activity_collections import load_record

PREFIX = "research/2026-10-15-card-protein-name-evidence"
ASSESSMENTS = Path(PREFIX + "-assessments.json")
CITATION = Path(PREFIX + "-citation.json")
OUTPUT = Path(PREFIX + ".json")
SCREEN = {
    "path": "research/2026-10-15-card-protein-name-screen.json",
    "sha256": "9ea833b1d24f8c48189a374f13a549ccff6458185d77f782a86961aea15a8a51",
}
SCOPE = "SCOPED_PRIMARY_ASSESSMENTS_BOUND_TO_SOURCE_CLAIMS_NOT_EXPERIMENTAL_GROUNDING"


def validate_assessments(notes, screen, citation):
    selected = {t: r for t, r in screen["terms"].items() if r["status"].startswith("NAME_CITATION_TAXON")}
    require(set(notes["reviews"]) == set(selected) and len(selected) == 6, "candidate coverage changed")
    expected_refs = {c for t in selected.values() for c in t["definition_citation_ids"]}
    require(expected_refs <= {s["reference"] for s in notes["sources"].values()}, "source citation omitted")
    identity = citation["citation_identity"]
    require(
        identity["pmid"] == "30053115"
        and identity["doi"] == "10.1093/jac/dky262"
        and identity["source"] == "MED"
        and citation["primary_results_reviewed"] is False,
        "naming citation conflated with functional paper",
    )
    require(
        notes["sources"]["mcr-naming"]["doi"] == identity["doi"]
        and notes["sources"]["mcr-followup"]["reference"] == "DOI:10.1128/AAC.00649-18",
        "distinct MCR references conflated",
    )
    for tid, review in notes["reviews"].items():
        require(
            review["accession"] == selected[tid]["name_matches"][0]["protein_accession"]
            and set(review["sources"]) <= set(notes["sources"]),
            "candidate or evidence owner changed",
        )
    require(
        notes["reviews"]["ARO:3004695"]["status"]
        == "CONTEXT_SPECIFIC_NEGATIVE_EVIDENCE_REQUIRES_QUALIFICATION"
        and {"mcr-original", "mcr-followup", "mcr-naming", "mcr-later-context"}
        == set(notes["reviews"]["ARO:3004695"]["sources"]),
        "negative or contrasting MCR context omitted",
    )
    for key in (
        "experimental_subject_assignments",
        "exact_allele_assignments",
        "experimental_genome_assignments",
        "biological_records_changed",
        "curated_ast_observations",
        "whole_record_primary_signoffs",
        "ncbi_requests",
        "github_mutations",
        "source_adoptions",
        "outreach",
    ):
        require(type(notes["limits"][key]) is int and notes["limits"][key] == 0, "evidence scope promoted")
    for key in (
        "native_primary_files_cached",
        "all_primary_results_reviewed",
        "broad_reference_index_updated",
        "new_gene_symbols_inferred",
        "operational_details_exported",
        "reuse_terms_review_resumed",
    ):
        require(notes["limits"][key] is False, "review completeness or scope promoted")
    require(
        notes["limits"]["issue_1040"] == "DEFERRED" and notes["limits"]["full_corpus_goal_status"] == "OPEN",
        "deferred work or goal status changed",
    )
    return selected


def build(root):
    screen = json.loads(reference.check_pin(root, SCREEN).read_bytes())
    notes = json.loads((root / ASSESSMENTS).read_bytes())
    citation = json.loads((root / CITATION).read_bytes())
    selected = validate_assessments(notes, screen, citation)
    inputs = {
        "screen": SCREEN,
        "assessments": reference.pin(root, root / ASSESSMENTS),
        "citation_identity": reference.pin(root, root / CITATION),
        **{k: screen["inputs"][k] for k in ("source_inventory", "source_queue", "census")},
    }
    paths = {k: reference.check_pin(root, p) for k, p in inputs.items()}
    with paths["census"].open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    require(
        len(census) == len({r["identifier"] for r in census}) == 2939
        and {r["path"] for r in census}
        == {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        and all(reference.digest(root / r["path"]) == r["record_sha256"] for r in census),
        "corpus bytes or membership changed",
    )
    with paths["source_inventory"].open() as stream:
        inventory = list(csv.DictReader(stream, delimiter="\t"))
    source_rows = [r for r in inventory if r["determinant_id"] in selected]
    require(len(source_rows) == 8, "source row coverage changed")
    ids = {rid for t in selected.values() for rid in t["record_memberships"]}
    records = [r for r in census if r["identifier"] in ids]
    claims = [c for c in screen["claims"] if c["aro_id"] in selected]
    actual, labels = [], {}
    for row in records:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "record chemical identity changed",
        )
        labels[row["identifier"]] = doc["label"]
        source_ids = {s["source_id"] for s in doc["source_concepts"] if s["source"] == "ARO"}
        for i, claim in enumerate(doc.get("resistance_mechanisms", [])):
            if owner(claim) != "CARD" or claim.get("aro_id") not in selected:
                continue
            tid = claim["aro_id"]
            matches = [
                r for r in source_rows if r["determinant_id"] == tid and r["antibiotic_id"] in source_ids
            ]
            require(
                len(matches) == 1
                and matches[0]["determinant_name"] == claim["label"]
                and matches[0]["mechanism"] == claim["mechanism_type"],
                "source ownership binding changed",
            )
            actual.append((row["identifier"], i, tid, checksum(claim)))
    require(
        sorted(actual)
        == sorted(
            (c["record_identifier"], c["resistance_index"], c["aro_id"], c["claim_sha256"]) for c in claims
        )
        and len(actual) == len(records) == 8,
        "live claim coverage changed",
    )
    reviews = {}
    for tid, term in selected.items():
        assessment = notes["reviews"][tid]
        protein = screen["reference_candidates"][assessment["accession"]]
        reviews[tid] = {
            "source_label": term["source_label"],
            "record_memberships": term["record_memberships"],
            "source_citation_ids": term["definition_citation_ids"],
            "status": assessment["status"],
            "assessment_pointer": {"input": "assessments", "pointer": "/reviews/" + tid},
            "reference_accession": assessment["accession"],
            "reference_identity": {
                k: protein[k]
                for k in (
                    "entry_type",
                    "entry_audit",
                    "gene_field_present",
                    "gene_symbols",
                    "reference_taxonomy",
                )
            },
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
            "experimental_genome_assignment": None,
            "selected_for_broad_index": False,
        }
    return {
        "date": notes["date"],
        "scope": SCOPE,
        "inputs": inputs,
        "reviews": reviews,
        "records": [{**r, "label": labels[r["identifier"]]} for r in records],
        "claims": claims,
        "source_rows": [
            {
                "row_sha256": checksum(r),
                **{
                    k: r[k]
                    for k in (
                        "determinant_id",
                        "determinant_name",
                        "antibiotic_id",
                        "antibiotic_name",
                        "mechanism",
                        "relation",
                    )
                },
            }
            for r in source_rows
        ],
        "summary": {
            "corpus_record_hashes_checked": 2939,
            "complete_records_read": len(records),
            "source_terms": len(reviews),
            "live_card_claims": len(claims),
            "source_rows": len(source_rows),
            "reference_proteins": len(reviews),
            "reviewed_source_contexts": len(notes["sources"]),
            "review_media": dict(sorted(Counter(s["medium"] for s in notes["sources"].values()).items())),
        },
        "limits": notes["limits"],
        "attribution": (
            "CARD/ARO and UniProt reference metadata, CC BY 4.0. "
            "Primary evidence is cited in assessments; no article text is reproduced."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build(args.root)
    if args.output:
        with args.output.open("x") as stream:
            stream.write(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
