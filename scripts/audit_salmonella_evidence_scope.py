"""Bind a primary-evidence qualification draft to unchanged CARD source claims."""

import argparse
import copy
import csv
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory

import audit_card_literature_expansion as literature
import audit_card_reference_memberships as registry
import audit_sal_reference_context as metadata
import audit_topoisomerase_references as reference
import card_evidence_reviews as reviews

from antibioticmech.activity_collections import load_record

PREFIX = "research/2026-10-16-salmonella-evidence-scope"
PLAN = Path(PREFIX + "-plan.json")
TERMS = {"ARO:3003307": "gyrB", "ARO:3003317": "parE"}
PARE = "ARO:3003317"
REVIEW_ID = "2026-10-16-salmonella-pare-evidence-scope"
SCOPE = "SALMONELLA_SOURCE_QUALIFICATION_DRAFT_NOT_EXPERIMENTAL_GROUNDING"
require = metadata.require


def read_inputs(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["new_network_requests_by_replay"] == 0
        and plan["active_curation_changed"] is False
        and plan["issue_1040"] == "DEFERRED",
        "audit scope changed",
    )
    data = {}
    for name, pin in plan["inputs"].items():
        body = reference.check_pin(root, pin).read_bytes()
        data[name] = body if pin["path"].endswith(".tsv") else json.loads(body)
    return plan, data


def check_assessment(a):
    require(
        a["scope"] == "SELECTED_PRIMARY_TABLE_AND_NARRATIVE_REVIEW_NOT_EXPERIMENTAL_IDENTITY"
        and a["reference"] == "PMID:19104017"
        and a["doi"] == "DOI:10.1128/aac.01005-08"
        and a["source_url"] == "https://journals.asm.org/doi/10.1128/aac.01005-08"
        and a["access"] == "PUBLISHER_HTML_READ_WITH_WEB_TOOL"
        and a["tables_text_reviewed"] == [1, 3]
        and a["new_ncbi_requests"] == 0
        and a["issue_1040"] == "DEFERRED",
        "primary source identity or inspection scope changed",
    )
    require(
        a["assessment"] == {
            "source_organism_scope": "Salmonella serovars",
            "paper_organism_scope": "Salmonella enterica serovar Enteritidis",
            "table_1_compound_labels": ["nalidixic acid", "ciprofloxacin"],
            "pare_result": "NO_INDEPENDENT_EFFECT_IN_TESTED_BACKGROUND",
            "indirect_pare_role": "UNRESOLVED_NOT_EXCLUDED",
            "universal_pare_inactivity_inferred": False,
            "gyrb_result": "REPORTED_FUNCTIONAL_CONTRIBUTION_IN_TESTED_CONTEXT",
            "all_serovars_or_inherited_compounds_verified": False,
            "table_3_supplies_pare_specific_comparison": False,
        },
        "negative result or organism/compound scope changed",
    )
    require(
        all(a[k] is False for k in (
            "native_publisher_body_cached", "offline_primary_body_replay",
            "tables_visually_verified", "figures_reviewed", "supplements_reviewed",
            "whole_paper_signoff", "experimental_identifiers_assigned",
            "numeric_ast_exported", "variant_specifications_exported", "protocols_exported",
        )),
        "review scope promoted beyond inspected evidence",
    )


def bind_claims(records, claims, docs):
    require(len(records) == len(docs) == 13 and len(claims) == 26, "cohort count changed")
    by_id = {r["identifier"]: r for r in records}
    require(len(by_id) == 13 and set(by_id) == set(docs), "record identity set changed")
    expected = {(r["identifier"], t) for r in records for t in TERMS}
    require(
        {(c["record_identifier"], c["aro_id"]) for c in claims} == expected,
        "missing or duplicated claim membership",
    )
    for c in claims:
        doc = docs[c["record_identifier"]]
        record = by_id[c["record_identifier"]]
        claim = doc["resistance_mechanisms"][c["resistance_index"]]
        require(
            doc["identifier"] == c["record_identifier"]
            and doc["chemical_structure"]["standard_inchi_key"]
            == c["standard_inchi_key"] == record["standard_inchi_key"]
            and c["record_path"] == record["path"]
            and c["record_sha256"] == record["record_sha256"]
            and claim["aro_id"] == c["aro_id"]
            and registry.checksum(claim) == c["claim_sha256"]
            and c["experimental_subject_assignment"] is False,
            "live claim or chemical identity drift",
        )


def build_draft(root, plan, data, records, claims, docs):
    rows = list(csv.DictReader(io.StringIO(data["inventory"].decode()), delimiter="\t"))
    targets = []
    selected_rows = {}
    for c in claims:
        if c["aro_id"] != PARE:
            continue
        doc = docs[c["record_identifier"]]
        source_ids = {s["source_id"] for s in doc["source_concepts"] if s["source"] == "ARO"}
        candidates = [r for r in rows if r["determinant_id"] == PARE and r["antibiotic_id"] in source_ids]
        require(len(candidates) == 1, "source row ownership is ambiguous")
        row = candidates[0]
        selected_rows[c["record_identifier"]] = row
        targets.append({
            "row_sha256": reviews.row_digest(row),
            "identifier": c["record_identifier"],
            "standard_inchi_key": c["standard_inchi_key"],
        })
    a = data["assessment"]
    draft = {
        "schema_version": 1,
        "source_inventory_sha256": plan["inputs"]["inventory"]["sha256"],
        "reviews": [{
            "review_id": REVIEW_ID,
            "curator": "Codex",
            "reviewed_on": a["reviewed_on"],
            "note": a["review_note"],
            "evidence": [{
                "reference": a["doi"], "source_url": a["source_url"],
                "locations": a["locations"],
                "inspected": (
                    "publisher HTML text and selected table text; "
                    "no visual table, figure or supplement verification"
                ),
            }],
            "source_rows": sorted(targets, key=lambda t: t["identifier"]),
        }],
    }
    require(
        REVIEW_ID not in {r["review_id"] for r in data["active_reviews"]["reviews"]},
        "draft already active; record a curation transition instead of replaying the draft",
    )
    # Exercise the production loader without writing any biological record.
    with TemporaryDirectory() as directory:
        path = Path(directory) / "draft.json"
        path.write_text(json.dumps(draft, indent=2, sort_keys=True) + "\n")
        accepted = reviews.load_reviews(root / plan["inputs"]["inventory"]["path"], rows, docs, path)
    require(len(accepted) == 13, "draft source coverage changed")
    projected = []
    for c in claims:
        if c["aro_id"] != PARE:
            continue
        original = docs[c["record_identifier"]]["resistance_mechanisms"][c["resistance_index"]]
        modified = copy.deepcopy(original)
        require(
            reviews.apply_review(modified, selected_rows[c["record_identifier"]], accepted),
            "unqualified row",
        )
        require(
            set(modified) - set(original) == {"note"}
            and {k: v for k, v in modified.items() if k != "note"} == original,
            "draft changes more than a note",
        )
        projected.append({
            "identifier": c["record_identifier"], "aro_id": PARE,
            "resistance_index": c["resistance_index"], "changed_fields": ["note"],
            "original_claim_sha256": c["claim_sha256"],
            "projected_claim_sha256": registry.checksum(modified),
        })
    return draft, projected


def build(root, *, native=False):
    plan, data = read_inputs(root)
    check_assessment(data["assessment"])
    prior = data["index"]
    require(len(prior["records"]) == 2939, "corpus scope changed")
    require(
        {p.relative_to(root).as_posix() for p in (root / "data/antibiotics").rglob("*.yaml")}
        == {r["path"] for r in prior["records"]},
        "corpus file membership changed",
    )
    for r in prior["records"]:
        require(reference.digest(root / r["path"]) == r["record_sha256"], "record snapshot drift")
    records = [r for r in prior["records"] if set(r["card_terms"]) & set(TERMS)]
    claims = [c for c in prior["claims"] if c["aro_id"] in TERMS]
    docs = {r["identifier"]: load_record(root / r["path"]) for r in records}
    bind_claims(records, claims, docs)
    query = data["literature"]["queries"]["19104017"]
    require(
        query["query"] == "lit_pubmed:19104017"
        and query["release"] == "2026_03" and query["result_count"] == 0
        and query["complete_for_query"] is True
        and query["establishes_biological_absence"] is False,
        "citation query scope changed",
    )
    if native:
        entries, actual = literature.read_query(root, root / literature.DIRECTORY, "19104017")
        require(not entries and actual == query, "native query differs from public projection")
    terms = {}
    for term, gene in TERMS.items():
        row = prior["terms"][term]
        source = data["previous_scope"]["terms"][term]
        citation = data["citations"]["terms"][term]
        require(
            row["record_memberships"] == source["record_ids"] == citation["record_memberships"]
            and citation["definition_citation_ids"] == ["PMID:19104017"]
            and source["gene"] == gene and not row["reference_accessions"],
            "source citation or reference membership changed",
        )
        terms[term] = {
            "gene": gene, "record_memberships": row["record_memberships"],
            "definition_citation": "PMID:19104017",
            "reference_accessions": [], "references": [],
            "experimental_allele_assignment": None, "experimental_protein_assignment": None,
            "experimental_taxon_assignment": None, "experimental_genome_assignment": None,
            "whole_record_primary_review": "OPEN",
            "draft_qualification_proposed": term == PARE,
        }
    draft, projected = build_draft(root, plan, data, records, claims, docs)
    result = {
        "schema_version": 1, "scope": SCOPE, "inputs": plan["inputs"],
        "records": records, "claims": claims, "terms": terms,
        "primary_assessment": data["assessment"],
        "cached_citation_query": query,
        "taxonomy_context": data["previous_scope"]["taxonomy_context"],
        "taxonomy_scope": "PRIOR_NAME_CONTEXT_REUSED_NOT_EXPERIMENTAL_SUBJECT",
        "curation_handoff": {
            "review_id": REVIEW_ID, "projected_claims": projected,
            "loader_accepted": True, "projection_changes_only_note": True,
            "production_records_written": False, "active_curation_changed": False,
            "pending": ["Source-owned curation canary", "Validated write and history",
                        "Corpus reproduction and rendering", "Authoritative QC"],
        },
        "summary": {
            "corpus_records_hash_checked": len(prior["records"]),
            "complete_records_read": len(records), "source_claims": len(claims),
            "new_qualified_reference_terms": 0, "proposed_note_qualifications": len(projected),
            "experimental_identifiers_assigned": 0, "biological_records_changed": 0,
            "new_ncbi_requests": 0, "issue_1040": "DEFERRED",
            "whole_record_primary_signoffs": 0, "whole_corpus_goal_status": "OPEN",
        },
    }
    metadata.metadata_only(result)
    return result, draft


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--native", action="store_true", help="also validate optional local UniProt caches")
    parser.add_argument("--write", action="store_true", help="write research exports only")
    args = parser.parse_args()
    dossier, draft = build(args.root, native=args.native)
    for suffix, value in ((".json", dossier), ("-proposed-review.json", draft)):
        path = args.root / (PREFIX + suffix)
        rendered = json.dumps(value, indent=2, sort_keys=True) + "\n"
        if args.write:
            path.write_text(rendered)
        else:
            require(path.read_text() == rendered, f"research export drift: {path}")
    print(json.dumps(dossier["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
