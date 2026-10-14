"""Verify standalone species responses for the remaining CARD reference ancestors.

This offline successor leaves the earlier lineage-only checkpoint intact and
does not assign experimental organisms, resistance proteins, or alleles.
"""

import argparse
import json
from datetime import datetime
from pathlib import Path

import audit_card_definition_citations as definitions
import audit_card_reference_lineages as lineages
import audit_topoisomerase_references as reference
from resistance_checkpoint_records import checkpoint_path

CACHE = Path("reports/resistance-grounding-2026-10-14-card-species-nodes")
OUTPUT = Path("research/2026-10-14-card-species-nodes.json")
SCOPE = "STANDALONE_REFERENCE_SPECIES_VERIFICATION_NOT_EXPERIMENTAL_IDENTITY"


def species_projection(expected, native):
    nodes, species = lineages.lineage(native)
    wanted = {"taxonId": int(expected["taxon_id"].split(":")[1]), "rank": "species",
              "scientificName": expected["scientific_name"]}
    if (expected["taxon_id"] != f"NCBITaxon:{wanted['taxonId']}"
            or lineages.identity(native) != wanted or species != wanted):
        raise ValueError("standalone species differs from the pinned lineage identity")
    return {"taxon_id": expected["taxon_id"], "scientific_name": native["scientificName"],
            "rank": "species", "active": True,
            "previous_status": "LINEAGE_ANNOTATION_ONLY_NO_STANDALONE_RESPONSE_SELECTED",
            "status": "ACTIVE_NATIVE_RESPONSE_VERIFIED", "lineage": nodes,
            "experimental_subject_assignment": False, "exact_allele_assignment": False}


def read_request(root, directory, taxid, cohort):
    key = "species-" + taxid
    paths = {kind: directory / f"{key}-{kind}.{suffix}"
             for kind, suffix in (("plan", "json"), ("attempt", "json"),
                                  ("response", "bin"), ("receipt", "json"))}
    plan, attempt, receipt = [json.loads(paths[k].read_bytes()) for k in ("plan", "attempt", "receipt")]
    url = cohort["species"][taxid]["url"]
    if (any(row["url"] != url for row in (plan, attempt, receipt))
            or plan["redirects_followed"] is not False or plan["max_bytes"] != 500_000
            or receipt["retry_performed"] is not False
            or receipt["bytes"] != paths["response"].stat().st_size
            or receipt["bytes"] > plan["max_bytes"]
            or datetime.fromisoformat(attempt["started_at"])
            > datetime.fromisoformat(receipt["retrieved_at"])):
        raise ValueError("native request identity, timing or single-attempt scope changed")
    item = {"receipt": reference.pin(root, paths["receipt"]),
            "body": reference.pin(root, paths["response"])}
    native, provenance = lineages.native_taxon(root, item, taxid, cohort["release"])
    return native, {**provenance, "request_plan": reference.pin(root, paths["plan"]),
                    "request_attempt": reference.pin(root, paths["attempt"]), "retry_performed": False}


def ancestor_concordance(reference_taxon, species):
    nodes, ancestor = lineages.lineage(reference_taxon)
    expected = {"taxonId": int(species["taxon_id"].split(":")[1]), "rank": "species",
                "scientificName": species["scientific_name"]}
    if ancestor != expected or nodes[:nodes.index(ancestor) + 1] != species["lineage"]:
        raise ValueError("standalone species ancestry differs from reference lineage")
    return True


def build(root, directory=CACHE, *, record_resolver=None):
    directory = root / directory
    cohort_path = directory / "cohort.json"
    cohort = json.loads(cohort_path.read_bytes())
    if (cohort["selection"] != "ALL_LINEAGE_ONLY_SPECIES_FROM_DIRECT_CARD_REFERENCES"
            or cohort["constraints"]["ncbi_requests"] != 0
            or cohort["constraints"]["biological_writes"] is not False):
        raise ValueError("reference-only cohort scope changed")
    pins = {key: cohort[key] for key in ("prior", "prior_checkpoint", "census", "source_queue")}
    paths = {key: reference.check_pin(root, pin) for key, pin in pins.items()}
    prior = json.loads(paths["prior"].read_bytes())
    expected = {key: node for key, node in prior["species"].items() if not node["standalone_active_verified"]}
    if set(expected) != set(cohort["species"]) or prior["release"] != cohort["release"]:
        raise ValueError("lineage-only species cohort changed")
    received = {path.name.removeprefix("species-").removesuffix("-receipt.json")
                for path in directory.glob("species-*-receipt.json")}
    if received != set(expected):
        raise ValueError("unexpected or missing native species receipts")
    terminal_path = directory / "batch-terminal.json"
    terminal = json.loads(terminal_path.read_bytes())
    if terminal != {"status": "COMPLETE", "species_responses": len(expected),
                    "retry_performed": False, "ncbi_requests": 0}:
        raise ValueError("species request batch is incomplete")
    canary_path = directory / "canary-reviewed.json"
    canary = json.loads(canary_path.read_bytes())
    if (canary["approved_for_remaining_metadata_requests"] is not True
            or canary["approved_for_experimental_or_biological_assignments"] is not False
            or set(canary["remaining_species"]) != set(expected) - {cohort["canary"]}):
        raise ValueError("canary approval or selection changed")
    census, labels, memberships, records = definitions.read_corpus(
        root, paths["census"], record_resolver=record_resolver)
    for tid, row in prior["terms"].items():
        if (definitions.text_hash(labels[tid]) != row["source_label_sha256"]
                or sorted(memberships[tid]) != row["record_memberships"]):
            raise ValueError("source term identity or record memberships changed")
    species, requests = {}, {}
    for taxid in sorted(expected, key=int):
        native, requests[taxid] = read_request(root, directory, taxid, cohort)
        species[taxid] = species_projection(expected[taxid], native)
        if cohort["species"][taxid]["scientific_name"] != species[taxid]["scientific_name"]:
            raise ValueError("planned species name differs from prior checkpoint")
    key = cohort["canary"]
    if (canary["canary"]["receipt"] != requests[key]["receipt"]
            or canary["canary"]["body"] != requests[key]["body"]):
        raise ValueError("canary response changed after review")
    reference_taxa = {}
    for taxid, taxon in prior["taxa"].items():
        species_id = taxon["species_taxon_id"].split(":")[1]
        if species_id not in species:
            continue
        native, _ = lineages.native_taxon(root, taxon["native_source"], taxid, cohort["release"])
        reference_taxa[taxid] = {
            "reference_taxon_id": taxon["reference_taxon_id"], "species_taxon_id": taxon["species_taxon_id"],
            "ancestor_lineage_concordant": ancestor_concordance(native, species[species_id]),
            "experimental_subject_assignment": False,
        }
    proteins = {accession: row for accession, row in prior["proteins"].items()
                if row["reference_species_taxon_id"].split(":")[1] in species}
    terms = {tid: row for tid, row in prior["terms"].items()
             if set(row["reference_accessions"]) & set(proteins)}
    identifiers = {identifier for row in terms.values() for identifier in row["record_memberships"]}
    record_rows = [{**row, "whole_record_primary_review": "OPEN"}
                   for row in records if row["identifier"] in identifiers]
    return {
        "date": "2026-10-14", "scope": SCOPE, "release": cohort["release"],
        "inputs": {**pins, "cohort": reference.pin(root, cohort_path),
                   "canary": reference.pin(root, canary_path),
                   "batch_terminal": reference.pin(root, terminal_path)},
        "attribution": prior["attribution"], "species": species, "requests": requests,
        "reference_taxa": reference_taxa, "proteins": proteins, "terms": terms, "records": record_rows,
        "summary": {"corpus_records_checked": len(census), "card_terms_checked": len(labels),
                    "new_species_responses": len(species), "reference_taxa_checked": len(reference_taxa),
                    "reference_proteins_with_new_species_evidence": len(proteins),
                    "reference_terms_with_new_species_evidence": len(terms),
                    "compound_records": len(record_rows),
                    "total_direct_reference_proteins": len(prior["proteins"]),
                    "total_species_nodes": len(prior["species"]),
                    "species_with_standalone_responses_after": sum(
                        row["standalone_active_verified"] for row in prior["species"].values()
                    ) + len(species),
                    "remaining_lineage_only_species": len(expected) - len(species),
                    "label_warning_nodes_retained": sum(
                        bool(row["label_flags"]) for row in prior["species"].values()),
                    "biological_record_changes": 0, "experimental_assignments": 0,
                    "whole_record_signoffs": 0},
        "limitations": [
            "Standalone species evidence closes only the selected reference-taxonomy metadata gap.",
            "All original gene, allele, primary-evidence, exact-compound "
            "and experimental-subject gaps remain.",
            "The prior lineage-only dossier is preserved as its historical snapshot; this is its successor.",
            "Species status does not assign a resistant isolate or prove a species-wide phenotype.",
            "All candidate protein accessions, versions and citation-context pointers are unchanged.",
            "Source aliases, strain lists and statistics from species responses "
            "are not experimental mappings.",
            "No protein, sequence, variant, assay, sample or genome query or biological write occurred.",
        ],
        "constraints": {"ncbi_requests": 0, "issue_1040": "DEFERRED", "source_adoptions": 0,
                        "github_mutations": 0, "held_source_retries": 0, "new_network_requests": len(species),
                        "full_corpus_goal_status": "OPEN", "new_primary_reviews": 0},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=CACHE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--historical-records", action="store_true",
                        help="Replay registered identifier/path/hash fixtures, not the live census.")
    args = parser.parse_args()
    result = build(Path.cwd(), args.cache,
                   record_resolver=checkpoint_path if args.historical_records else None)
    if args.check:
        if result != json.loads(args.output.read_bytes()):
            raise SystemExit("standalone species dossier does not reproduce")
    else:
        with args.output.open("x") as stream:
            stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
