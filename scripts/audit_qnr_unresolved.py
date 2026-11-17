"""Replay seven unresolved Qnr members without converting reference context to AST."""

import argparse
import hashlib
import json
from pathlib import Path

import audit_bla_primary_identifiers as native
import audit_card_reference_lineages as taxonomy
import audit_card_reference_memberships as registry
import audit_sal_reference_context as safety
from audit_curator_resistance_fields import owner

from antibioticmech.activity_collections import load_record

reference, require = native.reference, native.require
PREFIX = "research/2026-10-16-qnr-unresolved"
PLAN = Path(PREFIX + "-plan.json")
AUDIT = Path(PREFIX + "-audit-plan.json")
NATIVE = Path(PREFIX + "-native.json")
OUTPUT = Path(PREFIX + ".json")
CACHE = Path("reports/qnr-unresolved-2026-10-16")
TERMS = {
    "ARO:3002719": ("QnrB5", "16804843"),
    "ARO:3002777": ("QnrB65", "24247140"),
    "ARO:3002802": ("QnrVC5", "23800600"),
    "ARO:3002803": ("QnrVC6", "23800600"),
    "ARO:3004625": ("QnrS12", "29415140"),
    "ARO:3004636": ("qnrE1", "28193666"),
    "ARO:3005007": ("QnrVC2", "18598639"),
}
DEPOSITS = {"qnre1": "KY073238", "qnrvc2": "AB200915"}
SPECIES = {"qnre1": (573, "Klebsiella pneumoniae"), "qnrvc2": (666, "Vibrio cholerae")}
FALSE_LIMITS = {
    "experimental_identifiers_assigned",
    "new_reference_selection",
    "biological_record_writes",
    "native_primary_files_cached",
    "whole_record_primary_signoff",
    "all_primary_results_reviewed",
    "numeric_ast_exported",
    "sequences_exported",
    "variant_specifications_exported",
    "constructs_or_protocols_exported",
    "biological_absence_inferred",
    "reuse_terms_review_resumed",
}
TAXONOMY = {
    "path": "reports/resistance-grounding-2026-10-07/card-taxonomy.json",
    "sha256": "d75a09d19145527c20d59928f4e3a44b0e827e7fae1e3220b8a6546ce5be6e6a",
}


def read(root, pin):
    return json.loads(reference.check_pin(root, pin).read_bytes())


def capture(root):
    """Project already captured native responses; never make network requests."""
    plan = json.loads((root / PLAN).read_bytes())
    queries = {}
    for key in DEPOSITS:
        receipt, attempt = [
            json.loads((root / CACHE / (key + suffix)).read_bytes())
            for suffix in ("-receipt.json", "-attempt.json")
        ]
        body = reference.check_pin(root, receipt["body"]).read_bytes()
        native.validate_response(plan, key, receipt, attempt, body)
        queries[key] = {"receipt": receipt, "attempt": attempt, "response_body": body.decode()}
    snapshot = read(root, TAXONOMY)
    taxa = {}
    for key, (tid, _) in SPECIES.items():
        url = f"https://rest.uniprot.org/taxonomy/{tid}"
        digest = hashlib.sha256(json.dumps([url, None], sort_keys=True).encode()).hexdigest()
        path = root / Path(TAXONOMY["path"]).parent / f"request-{digest}.json"
        node, provenance = taxonomy.native_taxon(
            root, {"receipt": reference.pin(root, path), "body": None}, str(tid), plan["release"]
        )
        require(node == snapshot["taxa"][str(tid)], "taxonomy aggregate changed")
        taxa[key] = {
            "source": provenance,
            "node": {
                k: node[k] for k in ("taxonId", "scientificName", "rank", "active", "parent", "lineage")
            },
        }
    return {
        "request_plan": reference.pin(root, root / PLAN),
        "queries": queries,
        "canary_review": json.loads((root / CACHE / "canary-review.json").read_bytes()),
        "canary_receipt_body": (root / CACHE / "qnre1-receipt.json").read_text(),
        "native_taxonomy_snapshot": TAXONOMY,
        "taxa": taxa,
    }


def validate(plan, projection, notes):
    require(set(plan["requests"]) == set(DEPOSITS) == set(projection["queries"]), "query cohort changed")
    require(set(notes["reviews"]) == set(TERMS), "review cohort changed")
    require(
        set(notes["limits"])
        == FALSE_LIMITS | {"ncbi_requests", "new_taxonomy_requests", "issue_1040", "full_corpus_goal_status"}
        and all(notes["limits"][k] is False for k in FALSE_LIMITS)
        and notes["limits"]["ncbi_requests"] == notes["limits"]["new_taxonomy_requests"] == 0
        and notes["limits"]["issue_1040"] == "DEFERRED"
        and notes["limits"]["full_corpus_goal_status"] == "OPEN",
        "research scope promoted",
    )
    require(
        plan["constraints"]
        == {
            "planned_new_requests": 2,
            "ncbi_requests": 0,
            "retries": 0,
            "redirects_followed": 0,
            "issue_1040": "DEFERRED",
            "biological_record_writes": False,
            "experimental_identifiers_assigned": False,
            "new_reference_selection": False,
            "full_investigation_complete": False,
        },
        "request scope promoted",
    )
    contexts = {}
    for key, deposit in DEPOSITS.items():
        q = projection["queries"][key]
        require(plan["requests"][key]["query"] == "xref:embl-" + deposit, "deposition query changed")
        require(q["receipt"]["plan_sha256"] == projection["request_plan"]["sha256"], "request plan changed")
        entries, suggestions = native.validate_response(
            plan, key, q["receipt"], q["attempt"], q["response_body"].encode()
        )
        require(not entries, "new query results require explicit review")
        source = notes["sources"][key]
        require(
            source["deposition_accession"] == deposit and source["deposition_is_genome_assembly"] is False,
            "deposition identity or scope changed",
        )
        node = projection["taxa"][key]["node"]
        tid, name = SPECIES[key]
        _, species = taxonomy.lineage(node)
        require(
            node["taxonId"] == tid
            and node["scientificName"] == source["source_organism"] == name
            and node["rank"] == "species"
            and species == taxonomy.identity(node),
            "species context changed",
        )
        contexts[key] = {
            "deposition_accession": deposit,
            "query_result_count": len(entries),
            "service_suggestions_not_followed": suggestions,
            "query_status": "COMPLETE_EMPTY_EXACT_QUERY_NOT_BIOLOGICAL_ABSENCE",
            "species_name_context": taxonomy.identity(node),
            "species_scope": "NAME_CONTEXT_NOT_RESISTANT_SPECIES_OR_EXPERIMENTAL_ISOLATE_ID",
            "source_isolate_label": source["source_isolate_label"],
            "experimental_protein_assignment": None,
            "experimental_taxon_assignment": None,
            "experimental_strain_taxon_assignment": None,
            "experimental_genome_assignment": None,
        }
    review = projection["canary_review"]
    receipt_body = projection["canary_receipt_body"]
    require(
        review["receipt"]
        == {
            "path": str(CACHE / "qnre1-receipt.json"),
            "sha256": hashlib.sha256(receipt_body.encode()).hexdigest(),
        }
        and json.loads(receipt_body) == projection["queries"]["qnre1"]["receipt"],
        "canary receipt does not match reviewed response",
    )
    require(
        plan["canary"] == "qnre1"
        and review["approved_remaining_queries"] is True
        and review["plan_sha256"] == projection["request_plan"]["sha256"],
        "canary not reviewed",
    )
    require(
        notes["sources"]["qnre1"]["heterologous_host_results_are_separate"] is True
        and notes["sources"]["qnre1"]["source_isolate_label"] == "Q1130"
        and notes["sources"]["qnrvc2"]["qnrvc1_phenotype_transfer_allowed"] is False
        and notes["sources"]["qnrvc2"]["source_isolate_label"] is None,
        "source subjects conflated",
    )
    for term, (_, pmid) in TERMS.items():
        require(
            notes["sources"][notes["reviews"][term]["source"]]["reference"] == "PMID:" + pmid,
            "own citation changed",
        )
    safety.metadata_only(contexts)
    return contexts


def build(root):
    audit = json.loads((root / AUDIT).read_bytes())
    data = {k: read(root, pin) for k, pin in audit["inputs"].items()}
    plan, projection, notes = data["request_plan"], data["projection"], data["assessments"]
    require(projection["request_plan"] == audit["inputs"]["request_plan"], "projection plan mismatch")
    public = {k: read(root, pin) for k, pin in plan["inputs"].items()}
    contexts = validate(plan, projection, notes)
    index = public["current_index"]
    children = data["parents"]["terms"]["ARO:3000419"]["named_direct_subclass_ids"]
    require(
        {t for t in children if t in index["terms"] and not index["terms"][t]["reference_accessions"]}
        == set(TERMS),
        "unresolved family cohort changed",
    )
    actual = {
        str(p.relative_to(root)): reference.digest(p) for p in (root / "data/antibiotics").rglob("*.yaml")
    }
    require(
        len(actual) == 2939 and actual == {r["path"]: r["record_sha256"] for r in index["records"]},
        "current corpus changed",
    )
    rows = [r for r in index["records"] if set(TERMS).intersection(r["card_terms"])]
    claims = [c for c in index["claims"] if c["aro_id"] in TERMS]
    require(
        len(rows) == 1 and len(claims) == 7 and {c["aro_id"] for c in claims} == set(TERMS),
        "source cohort changed",
    )
    doc = load_record(root / rows[0]["path"])
    require(
        doc["identifier"] == "CHEBI:100241"
        and doc["chemical_structure"]["standard_inchi_key"] == "MYSWGUAQZAJSOK-UHFFFAOYSA-N",
        "chemical identity changed",
    )
    for c in claims:
        item = doc["resistance_mechanisms"][c["resistance_index"]]
        require(
            owner(item) == "CARD"
            and item["aro_id"] == c["aro_id"]
            and registry.checksum(item) == c["claim_sha256"]
            and c["record_identifier"] == doc["identifier"]
            and c["standard_inchi_key"] == doc["chemical_structure"]["standard_inchi_key"],
            "source claim changed",
        )
    reviews = {}
    for term, (label, pmid) in TERMS.items():
        previous = data["screen"]["terms"][term]
        require(
            previous["source_label"] == label
            and public["definitions"]["terms"][term]["definition_citation_ids"] == ["PMID:" + pmid],
            "source identity changed",
        )
        reviews[term] = {
            "source_label": label,
            "source_citation": "PMID:" + pmid,
            "prior_name_screen": previous,
            "assessment": notes["reviews"][term],
            "selected_reference_accessions": [],
            "whole_record_primary_review": "OPEN",
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
    return {
        "date": notes["date"],
        "scope": plan["scope"],
        "inputs": audit["inputs"],
        "current_inputs": plan["inputs"],
        "records": rows,
        "claims": claims,
        "reviews": reviews,
        "deposition_contexts": contexts,
        "primary_assessments": notes,
        "summary": {
            "corpus_records_hash_checked": len(actual),
            "complete_records_loaded": 1,
            "source_claims_bound": len(claims),
            "unresolved_family_members_reviewed": len(reviews),
            "new_uniprot_requests": 2,
            "complete_empty_deposition_queries": 2,
            "species_name_contexts_verified": 2,
            "new_reference_selections": 0,
            "experimental_identifiers_assigned": 0,
            "whole_record_primary_signoffs": 0,
            "current_selected_reference_terms": 1405,
            "current_unresolved_reference_terms": 597,
        },
        "attribution": (
            "CARD/ARO ontology and UniProt metadata, CC BY 4.0; "
            "cited primary evidence summarized, not reproduced."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--capture", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = capture(args.root) if args.capture else build(args.root)
    path = args.root / (NATIVE if args.capture else OUTPUT)
    text = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.write:
        with path.open("x") as stream:
            stream.write(text)
    else:
        require(path.read_text() == text, "research export drift")
    print(json.dumps({"path": str(path), "sha256": reference.digest(path), "summary": result.get("summary")}))


if __name__ == "__main__":
    main()
