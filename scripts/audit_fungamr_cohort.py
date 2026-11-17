"""Reconcile a shared database citation without promoting reference identities."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import audit_topoisomerase_references as reference
from resistance_checkpoint_records import checkpoint_path

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-13-fungamr-cohort")
OUTPUT = Path("research/2026-10-13-fungamr-cohort-context.json")
PMID = "PMID:40790106"
SELECTED = {
    "ARO:3009437": "P43071",
    "ARO:3009575": "P10613",
    "ARO:3009397": "P50859",
    "ARO:3009201": "Q4WNT5",
    "ARO:3009347": "P07251",
    "ARO:3009350": "P00830",
}
FKS1_CONTEXT = Path("research/2026-10-08-echinocandin-reference-context.json")
GENES = {
    "ARO:3009372": "MRPL11",
    "ARO:3009390": "Cdc6",
    "ARO:3009287": "Fks1",
    "ARO:3009213": "ERG11",
    "ARO:3009239": "mrr2",
    "ARO:3009396": "ERG11",
    "ARO:3009397": "ERG11",
    "ARO:3009559": "FKS1",
    "ARO:3009578": "ERG11",
    "ARO:3009588": "ERG11",
    "ARO:3009201": "cyp51a",
    "ARO:3009575": "ERG11",
    "ARO:3009347": "ATP1",
    "ARO:3009350": "ATP2",
    "ARO:3009633": "Ura6",
    "ARO:3009407": "Cyp51",
    "ARO:3009486": "Cyp51B",
    "ARO:3009534": "Cyp51",
    "ARO:3009437": "CDR1",
}


def read_source(root, source):
    """Accept both historical cache formats, validating native payload hashes."""
    if "wrapper" in source:
        path = reference.check_pin(root, source["wrapper"])
        receipt = json.loads(path.read_bytes())
        payload = receipt["body"].encode()
    else:
        path = reference.check_pin(root, source["body"])
        receipt = json.loads(reference.check_pin(root, source["receipt"]).read_bytes())
        payload = path.read_bytes()
    url = urlsplit(source["url"])
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    if (
        receipt["url"] != source["url"]
        or url.scheme != "https"
        or url.netloc != "rest.uniprot.org"
        or url.fragment
        or receipt["status"] != 200
        or receipt["sha256"] != hashlib.sha256(payload).hexdigest()
        or ("bytes" in receipt and receipt["bytes"] != len(payload))
        or headers.get("x-uniprot-release") != "2026_03"
        or headers.get("link")
    ):
        raise ValueError("native source identity, release, completeness or payload changed")
    body = json.loads(payload)
    if url.path.endswith("/search") and len(body["results"]) != int(headers["x-total-results"]):
        raise ValueError("incomplete search response")
    return body, {
        **source,
        "release": headers["x-uniprot-release"],
        "retrieved_at": receipt["retrieved_at"],
        "status": 200,
    }


def project(entry, taxonomy, selected, source_name):
    # Old caches may include sequence/features. Export only identity metadata.
    fields = (
        "primaryAccession",
        "entryType",
        "entryAudit",
        "genes",
        "organism",
        "proteinDescription",
        "references",
    )
    metadata = {key: entry[key] for key in fields if key in entry}
    result = reference.project_reference(metadata, selected["gene"], selected["species_id"], taxonomy)
    species = [r for r in taxonomy.get("lineage", []) if r["rank"] == "species"]
    if taxonomy["rank"] == "species":
        species.append(taxonomy)
    if (
        entry["primaryAccession"] != selected["accession"]
        or taxonomy["taxonId"] != selected["reference_taxon_id"]
        or taxonomy["rank"] not in {"species", "strain"}
        or len(species) != 1
        or species[0]["scientificName"].casefold() != source_name.casefold()
    ):
        raise ValueError("selected accession, reference taxon or source species name changed")
    bibliography = result.pop("bibliography")
    result.update(
        {
            "database_paper_in_bibliography": any(
                r["database"] == "PubMed" and r["id"] == "40790106"
                for c in bibliography
                for r in c["identifiers"]
            ),
            "role": "REFERENCE_IDENTITY_ONLY_NOT_TESTED_ALLELE_OR_DRUG_EVIDENCE",
            "exact_card_term_mapping_asserted": False,
            "exact_fungamr_row_crosswalk_verified": False,
            "experimental_genome_assignment": None,
        }
    )
    return result


def source_terms(rows, definitions):
    selected = {}
    for row in rows:
        term = row["determinant_id"]
        if term not in GENES:
            continue
        if term in selected:
            raise ValueError("ambiguous source edge membership")
        label = row["determinant_name"]
        tokens = label.split()
        if (
            tokens[2].casefold() != GENES[term].casefold()
            or hashlib.sha256(label.encode()).hexdigest() != definitions[term]["label_sha256"]
            or row["relation"] != "confers_resistance_to_antibiotic"
        ):
            raise ValueError("source label, gene scope or edge relation changed")
        selected[term] = {
            "source_label": label,
            "source_organism_name": " ".join(tokens[:2]),
            "source_gene": tokens[2],
            "source_antibiotic_id": row["antibiotic_id"],
            "source_antibiotic_name": row["antibiotic_name"],
            "source_relation": row["relation"],
            "source_edge_sha256": hashlib.sha256(json.dumps(row, sort_keys=True).encode()).hexdigest(),
            "definition_citation_ids": definitions[term]["definition_citation_ids"],
            "record_memberships": definitions[term]["record_memberships"],
            "reference_status": "NOT_RESOLVED_IN_THIS_CHECKPOINT_NOT_EVIDENCE_OF_ABSENCE",
            "exact_allele_assignment": None,
            "experimental_subject_assignment": None,
            "new_resistance_assertion": False,
            "whole_record_review_complete": False,
        }
    if set(selected) != set(GENES):
        raise ValueError("source cohort membership changed")
    return selected


def build(root, directory):
    selection_path = directory / "reference-selection.json"
    selection = json.loads(selection_path.read_bytes())
    cohort = json.loads(reference.check_pin(root, selection["cohort"]).read_bytes())
    for key in ("candidate_search", "legacy_explicit_xrefs"):
        reference.check_pin(root, selection[key])
    for key in ("prior_verification", "census", "definitions", "source_inventory", "protected"):
        reference.check_pin(root, cohort[key])
    all_definitions = json.loads((root / cohort["definitions"]["path"]).read_bytes())["terms"]
    definitions = {k: v for k, v in all_definitions.items() if PMID in v["definition_citation_ids"]}
    if definitions != cohort["terms"] or set(definitions) != set(GENES):
        raise ValueError("shared-citation membership changed")
    with (root / cohort["source_inventory"]["path"]).open(newline="") as stream:
        terms = source_terms(csv.DictReader(stream, delimiter="\t"), definitions)
    with (root / cohort["census"]["path"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["path"] for r in census}) != len(census)
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        or any(reference.digest(checkpoint_path(root, r)) != r["record_sha256"] for r in census)
    ):
        raise ValueError("whole-corpus record membership or bytes changed")
    for item in cohort["records"]:
        record = load_record(checkpoint_path(root, item))
        selected_claims = [c for c in record.get("resistance_mechanisms", []) if c.get("aro_id") in terms]
        claims = {c["aro_id"]: c for c in selected_claims}
        expected = {k for k, t in terms.items() if record["identifier"] in t["record_memberships"]}
        if (
            record["identifier"] != item["identifier"]
            or record["label"] != item["label"]
            or record["chemical_structure"]["standard_inchi_key"] != item["standard_inchi_key"]
            or len(selected_claims) != len(claims)
            or set(claims) != expected
            or expected != set(item["citation_terms"])
            or any(c["label"] != terms[k]["source_label"] for k, c in claims.items())
        ):
            raise ValueError("record identity or selected claim membership changed")
    if (
        len(cohort["records"]) != 10
        or len({r["identifier"] for r in cohort["records"]}) != 10
        or {r["identifier"] for r in cohort["records"]}
        != {i for t in terms.values() for i in t["record_memberships"]}
    ):
        raise ValueError("record cohort incomplete")
    prior = json.loads((root / selection["legacy_explicit_xrefs"]["path"]).read_bytes())
    if any(prior["determinants"][k]["candidates"] for k in terms):
        raise ValueError("initial explicit-xref scope changed")
    if selection["reference_only"] is not True or selection["new_requests"] != 0:
        raise ValueError("cached reference-only scope changed")
    if {k: v["accession"] for k, v in selection["selected"].items()} != SELECTED:
        raise ValueError("reviewed reference selection changed")
    for term, selected in selection["selected"].items():
        if selected["gene"].casefold() != GENES[term].casefold():
            raise ValueError("reference selection gene does not match the term")
        proteins, protein_source = read_source(root, selected["protein_source"])
        taxonomy, taxonomy_source = read_source(root, selected["taxonomy_source"])
        if (
            urlsplit(protein_source["url"]).path != "/uniprotkb/search"
            or taxonomy_source["url"] != f"https://rest.uniprot.org/taxonomy/{selected['reference_taxon_id']}"
        ):
            raise ValueError("taxonomy request identity changed")
        entries = [p for p in proteins["results"] if p["primaryAccession"] == selected["accession"]]
        if len(entries) != 1:
            raise ValueError("selected accession absent or ambiguous")
        terms[term].update(
            {
                "reference": project(entries[0], taxonomy, selected, terms[term]["source_organism_name"]),
                "protein_source": protein_source,
                "taxonomy_source": taxonomy_source,
                "reference_status": "GENE_SPECIES_REFERENCE_NOT_EXACT_RESISTANCE_MAPPING",
            }
        )
    mismatch = terms["ARO:3009486"]
    if (
        not mismatch["source_label"].endswith("resistance to voriconazole")
        or mismatch["source_antibiotic_name"] != "tebuconazole"
    ):
        raise ValueError("reviewed drug-label discrepancy changed")
    baseline = json.loads((root / cohort["protected"]["path"]).read_bytes())
    alias_pin = {"path": str(FKS1_CONTEXT), "sha256": baseline[str(FKS1_CONTEXT)]}
    alias_context = json.loads(reference.check_pin(root, alias_pin).read_bytes())
    if (
        alias_context["proteins"]["O13383"]["genes"][0]["geneName"]["value"] != "CaFKS1"
        or alias_context["proteins"]["A0A1D8PCT0"]["genes"][0]["geneName"]["value"] != "GSC1"
    ):
        raise ValueError("cached alias lead context changed")
    findings = [
        {
            "id": "fungamr-cohort-drug-label-discrepancy",
            "term": "ARO:3009486",
            "status": "OPEN_SOURCE_CONTEXT_REQUIRED",
            "label_drug": "voriconazole",
            "edge_drug": "tebuconazole",
            "action": ("Preserve the edge pending source-row and primary-evidence review; "
                       "cross-resistance is not excluded."),
        },
        {
            "id": "fungamr-cohort-reference-not-allele",
            "terms": sorted(selection["selected"]),
            "status": "SCOPE_GUARD_APPLIED",
            "action": ("Do not fill experimental protein, strain, genome or phenotype slots "
                       "from these references."),
        },
        {
            "id": "fungamr-cohort-fks1-alias",
            "term": "ARO:3009559",
            "status": "OPEN_ALIAS_AND_PRIMARY_CONTEXT",
            "action": ("Existing CaFKS1/GSC1 context is an alias lead, not a verified mapping "
                       "for this term or its drug claim."),
        },
    ]
    return {
        "scope": "SHARED_DATABASE_CITATION_REFERENCE_RECONCILIATION",
        "date": "2026-10-13",
        "database_citation": PMID,
        "database_doi": "10.1038/s41564-025-02084-7",
        "inputs": {
            "cohort": selection["cohort"],
            "selection": reference.pin(root, selection_path),
            "candidate_search": selection["candidate_search"],
            "census": cohort["census"],
            "fks1_alias_lead": alias_pin,
            "legacy_explicit_xrefs": selection["legacy_explicit_xrefs"],
        },
        "records": cohort["records"],
        "terms": terms,
        "review_findings": findings,
        "summary": {
            "corpus_records_hash_verified": len(census),
            "records_in_cohort": 10,
            "citation_terms": len(terms),
            "reference_contexts_reconciled": len(selection["selected"]),
            "terms_without_reference_resolution_here": len(terms) - len(selection["selected"]),
            "initial_explicit_card_xref_candidates": 0,
            "exact_alleles_assigned": 0,
            "new_resistance_assertions": 0,
            "biological_records_changed": 0,
            "whole_record_reviews_completed": 0,
        },
        "constraints": cohort["constraints"],
        "new_network_requests": 0,
        "limitations": [
            "Cached gene/species identity does not establish a tested allele "
            "or resistance to a particular drug.",
            "No exact FungAMR row-to-primary crosswalk is verified by this audit.",
            "Cache discovery included ignored files but was lexical and limited to JSON and response-bin "
            "files; missing candidates do not establish absence.",
            "No new primary experiments, sequences, variant specifications, numeric AST, "
            "or genome assignments are exported.",
            "This is same-agent review and offline metadata validation, not independent scientific signoff.",
            "All 2939 records remain in scope; NCBI requests and issue 1040 remain deferred.",
        ],
        "attribution": ("CARD/ARO and UniProt Consortium (release 2026_03), CC BY 4.0; "
                        "source assertions remain source-owned."),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--cache", type=Path, default=CACHE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    payload = (
        json.dumps(build(root, root / args.cache), indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    ).encode()
    output = root / args.output
    if args.check:
        if output.read_bytes() != payload:
            raise SystemExit("saved cohort context differs from pinned evidence")
    elif output.exists() and output.read_bytes() != payload:
        raise SystemExit("refusing to overwrite a different checkpoint")
    else:
        output.write_bytes(payload)
    print("Verified 19 terms, 10 records, six reference-only contexts; no record edits")


if __name__ == "__main__":
    main()
