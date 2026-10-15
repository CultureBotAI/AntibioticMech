"""Complete bounded yeast reference queries without assigning experimental alleles."""

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlencode

import audit_card_reference_lineages as lineages
import audit_ionophore_yeast as prior_audit
import audit_topoisomerase_references as reference
from audit_beauvericin_references import complete_query
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-ionophore-reference-successor")
OUTPUT = Path("research/2026-10-14-ionophore-reference-successor.json")
COHORT_SHA = "194b9633887b8e2d8faa0deace0ca539379b602f3bf78733a1ed555a0c4f412b"
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,xref_sgd,sequence_version,version"
)
TAXON_NAME = "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)"
REUSED = "locus:YMR202W"
ROLES = ("geneName", "synonyms", "orderedLocusNames", "orfNames")
NO_HIT = "NO_REFERENCE_HIT_IN_COMPLETE_QUERY_NOT_GENE_ABSENCE"


def select_entities(prior):
    rows = prior["source_rows"]
    if len(rows) != 127 or Counter(r["source_category"] for r in rows) != prior_audit.COUNTS:
        raise ValueError("source cohort changed")
    if prior["reconstruction_figure"] != prior_audit.project_figure(rows):
        raise ValueError("source reconstruction contexts changed")
    result = {}
    for index, row in enumerate(rows):
        locus = row["source_locus"]
        key = "locus:" + locus
        if key in result or not re.fullmatch(r"Y[A-P][LR]\d{3}[CW](?:-[A-Z])?", locus):
            raise ValueError("duplicate or malformed source locus")
        result[key] = {
            "query_token": locus,
            "kind": "LOCUS",
            "source_row": index,
            "source_gene_label": row["source_gene_label"],
            "figure_rows": [],
        }
    for index, row in enumerate(prior["reconstruction_figure"]):
        matches = [k for k, v in result.items() if v["source_gene_label"] == row["gene"]]
        if len(matches) > 1:
            raise ValueError("ambiguous figure-to-table gene join")
        if not matches:
            key = "symbol:" + row["gene"]
            result[key] = {
                "query_token": row["gene"],
                "kind": "SYMBOL",
                "source_row": None,
                "source_gene_label": row["gene"],
                "figure_rows": [],
            }
        else:
            (key,) = matches
        result[key]["figure_rows"].append(index)
    if len(result) != 130 or {k for k in result if k.startswith("symbol:")} != {
        "symbol:ERG28",
        "symbol:ERG4",
        "symbol:ERG5",
    }:
        raise ValueError("full table and figure coverage changed")
    return dict(sorted(result.items()))


def request_spec(keys, entities):
    if not 1 <= len(keys) <= 50 or len(keys) != len(set(keys)):
        raise ValueError("invalid bounded query membership")
    tokens = [entities[k]["query_token"] for k in keys]
    if any(not re.fullmatch(r"[A-Z0-9-]+", token) for token in tokens):
        raise ValueError("invalid exact gene query token")
    query = "organism_id:559292 AND (" + " OR ".join("gene_exact:" + t for t in tokens) + ")"
    return query, "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {
            "query": query,
            "format": "json",
            "fields": FIELDS,
            "size": 500,
        }
    )


def validate_plan(plan, entities):
    pending = sorted(set(entities) - {REUSED})
    requests = plan["requests"]
    if (
        len(entities) != 130
        or REUSED not in entities
        or list(requests) != ["references-001", "references-002", "references-003"]
    ):
        raise ValueError("successor query coverage changed")
    for index, item in enumerate(requests.values()):
        keys = pending[index * 50 : (index + 1) * 50]
        query, url = request_spec(keys, entities)
        if (
            item["entity_keys"] != keys
            or item["query"] != query
            or item["url"] != url
            or item["canary"] is not (index == 0)
            or item["maximum_gene_clauses"] != 50
        ):
            raise ValueError("successor query identity, bounds or coverage changed")
    flags = {
        "automatic_redirects": False,
        "retry_performed": False,
        "corrected_query_size": True,
        "original_failed_attempt_preserved": True,
        "primary_paper_or_access_hold_revisited": False,
        "canary_required_before_remaining_requests": True,
    }
    if any(plan.get(k) is not v for k, v in flags.items()) or plan.get("ncbi_requests") != 0:
        raise ValueError("request policy changed")


def gene_fields(gene):
    result = {}
    for role in ROLES:
        values = ([gene[role]] if role == "geneName" else gene[role]) if role in gene else []
        if not isinstance(values, list) or any(
            not isinstance(v, dict) or not isinstance(v.get("value"), str) or not v["value"] for v in values
        ):
            raise ValueError("malformed gene identity field")
        result[role] = [v["value"] for v in values]
    return result


def match_fields(entry, entity):
    if entity["kind"] not in {"LOCUS", "SYMBOL"}:
        raise ValueError("unknown source identity kind")
    roles = ("orderedLocusNames", "orfNames") if entity["kind"] == "LOCUS" else ROLES[:2]
    matches = []
    for index, gene in enumerate(entry.get("genes", [])):
        fields = gene_fields(gene)
        for role in roles:
            if entity["query_token"] in fields[role]:
                matches.append({"gene_index": index, "field": role, "value": entity["query_token"]})
    if len({match["gene_index"] for match in matches}) > 1:
        raise ValueError("reference token matches multiple native gene blocks")
    return matches


def project_reference(entry):
    accession = entry.get("primaryAccession")
    audit = entry.get("entryAudit", {})
    organism = entry.get("organism", {})
    if (
        not isinstance(accession, str)
        or not re.fullmatch(r"[A-Z0-9]{6}(?:[A-Z0-9]{4})?", accession)
        or entry.get("entryType") not in {"UniProtKB reviewed (Swiss-Prot)", "UniProtKB unreviewed (TrEMBL)"}
        or any(type(audit.get(k)) is not int or audit[k] < 1 for k in ("entryVersion", "sequenceVersion"))
        or organism.get("taxonId") != 559292
        or organism.get("scientificName") != TAXON_NAME
        or not isinstance(entry.get("genes"), list)
        or not entry["genes"]
        or {"sequence", "features", "comments"}.intersection(entry)
    ):
        raise ValueError("reference identity, version, taxon or payload scope changed")
    genes = [gene_fields(g) for g in entry["genes"]]
    description = entry.get("proteinDescription", {})
    names = []
    for kind in ("recommendedName", "submissionNames", "alternativeNames"):
        items = (
            ([description[kind]] if kind == "recommendedName" else description[kind])
            if kind in description
            else []
        )
        for item in items:
            value = item.get("fullName", {}).get("value")
            if not isinstance(value, str) or not value:
                raise ValueError("missing protein full name")
            names.append({"kind": kind, "value": value})
    if not names:
        raise ValueError("missing protein identity name")
    sgd = [x["id"] for x in entry.get("uniProtKBCrossReferences", []) if x.get("database") == "SGD"]
    if len(sgd) != len(set(sgd)) or any(not re.fullmatch(r"S\d{9}", x) for x in sgd):
        raise ValueError("invalid or duplicate SGD cross-reference")
    flag = description.get("flag")
    if flag not in {None, "Precursor", "Fragment", "Fragments"}:
        raise ValueError("unhandled native protein flag")
    return {
        "protein_accession": "UniProtKB:" + accession,
        "entry_type": entry["entryType"],
        "entry_version": audit["entryVersion"],
        "sequence_version": audit["sequenceVersion"],
        "genes": genes,
        "sgd_ids": sorted("SGD:" + x for x in sgd),
        "protein_names": names,
        "native_protein_flag": flag,
        "fragment_annotation": flag in {"Fragment", "Fragments"},
        "absence_of_fragment_flag_proves_completeness": False,
        "reference_taxon_id": "NCBITaxon:559292",
        "reference_taxon_rank": "strain",
        "reference_taxon_label": TAXON_NAME,
        "reference_species_taxon_id": "NCBITaxon:4932",
        "reference_species_taxon_rank": "species",
        "reference_species_taxon_label": "Saccharomyces cerevisiae",
        "experimental_subject_assignment": False,
        "experimental_allele_accession": None,
        "experimental_genome_accession": None,
        "resistance_inferred_from_reference": False,
        "database_review_status_is_primary_results_review": False,
    }


def read_batch(root, directory, key, plan, entities):
    directory = root / directory
    validate_plan(plan, entities)
    item = plan["requests"][key]
    source = planned_source(root, directory, key, "request-plan.json", item["url"])
    receipt = json.loads(reference.check_pin(root, source["receipt"]).read_bytes())
    payload = json.loads(reference.check_pin(root, source["body"]).read_bytes())
    count = len(payload.get("results", []))
    entries = complete_query(payload, receipt["headers"], count)
    if count > 500 or len({e["primaryAccession"] for e in entries}) != count:
        raise ValueError("duplicate or excessive native entries")
    for entry in entries:
        project_reference(entry)
        if not any(match_fields(entry, entities[k]) for k in item["entity_keys"]):
            raise ValueError("reference is not bound to a planned locus or symbol field")
    return entries, source


def map_entity(entity, entries):
    candidates = []
    for entry in entries:
        matches = match_fields(entry, entity)
        if not matches:
            continue
        label = entity["source_gene_label"]
        matched_gene_indexes = {m["gene_index"] for m in matches}
        names = {
            v
            for i in matched_gene_indexes
            for role in ROLES[:2]
            for v in gene_fields(entry["genes"][i])[role]
        }
        candidates.append(
            {
                "protein_accession": "UniProtKB:" + entry["primaryAccession"],
                "matches": matches,
                "source_gene_label_status": "NOT_SUPPLIED"
                if label is None
                else (
                    "MATCHED_CURRENT_NAME_OR_SYNONYM"
                    if label in names
                    else "SOURCE_LABEL_DIFFERS_FROM_CURRENT_GENE_NAMES"
                ),
            }
        )
    candidates.sort(key=lambda r: r["protein_accession"])
    if len({r["protein_accession"] for r in candidates}) != len(candidates):
        raise ValueError("duplicate candidate accession")
    return {
        **entity,
        "reference_candidates": candidates,
        "status": "REFERENCE_ONLY_MULTIPLE_CANDIDATES"
        if len(candidates) > 1
        else ("REFERENCE_ONLY_FIELD_MATCH" if candidates else NO_HIT),
        "experimental_allele_accession": None,
        "experimental_genome_accession": None,
        "experimental_subject_assignment": False,
        "resistance_inferred_from_reference": False,
    }


def build(root, directory=CACHE):
    directory = root / directory
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    for key in ("prior", "census", "source_queue", "protected", "prior_checkpoint"):
        reference.check_pin(root, cohort[key])
    prior = json.loads((root / cohort["prior"]["path"]).read_bytes())
    entities = select_entities(prior)
    if entities != cohort["entities"]:
        raise ValueError("cohort differs from complete prior evidence scope")
    with (root / cohort["census"]["path"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        or any(reference.digest(root / r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("complete corpus changed")
    for item in cohort["records"]:
        current = load_record(root / item["path"])
        before = directory / (item["identifier"].replace(":", "-") + "-before.yaml")
        if (
            current != load_record(before)
            or current["identifier"] != item["identifier"]
            or current["chemical_structure"]["standard_inchi_key"] != item["standard_inchi_key"]
            or reference.digest(before) != item["sha256"]
            or current.get("resistance_mechanisms")
            or current.get("genotype_resistance_score_rules")
        ):
            raise ValueError("selected record changed")
    plan = json.loads((directory / "request-plan.json").read_bytes())
    if plan["cohort"] != reference.pin(root, cohort_path):
        raise ValueError("request cohort binding changed")
    validate_plan(plan, entities)
    canary = json.loads((directory / "canary-review.json").read_bytes())
    for key, filename in (
        ("body", "references-001-response.bin"),
        ("receipt", "references-001-receipt.json"),
        ("plan", "request-plan.json"),
    ):
        if canary[key] != reference.pin(root, directory / filename):
            raise ValueError("canary binding changed")
    if (
        canary["manually_inspected"] is not True
        or canary["experimental_subject_or_allele_assignments"] is not False
    ):
        raise ValueError("canary review changed")
    taxonomy = prior["inputs"]["taxonomy"]
    reference.check_pin(root, taxonomy["taxonomy_prior_plan"])
    taxon, taxon_source = lineages.native_taxon(
        root,
        {
            "body": taxonomy["taxonomy_body"],
            "receipt": taxonomy["taxonomy_receipt"],
        },
        "559292",
        "2026_03",
    )
    _, species = lineages.lineage(taxon)
    if lineages.identity(taxon) != {
        "taxonId": 559292,
        "scientificName": TAXON_NAME,
        "rank": "strain",
    } or species != {"taxonId": 4932, "scientificName": "Saccharomyces cerevisiae", "rank": "species"}:
        raise ValueError("reference taxonomy changed")
    # Historical bytes and failure status remain immutable; this is not a retry of a held paper.
    for name in ("reference-cohort", "reference-canary"):
        for key in ("body", "receipt", "attempt"):
            reference.check_pin(root, prior["inputs"]["sources"][name][key])
    rejected = prior["inputs"]["sources"]["reference-cohort"]
    failure = json.loads((root / rejected["body"]["path"]).read_bytes())
    if rejected["status"] != 400 or failure != {
        "url": "http://rest.uniprot.org/uniprotkb/search",
        "messages": ["Too many OR conditions in query. Maximum allowed is 100."],
    }:
        raise ValueError("original query-size failure changed")
    reused = prior["inputs"]["sources"]["reference-canary"]
    old_receipt = json.loads((root / reused["receipt"]["path"]).read_bytes())
    old_payload = json.loads((root / reused["body"]["path"]).read_bytes())
    old_entries = complete_query(old_payload, old_receipt["headers"], 1)
    prior_audit.project_reference(old_entries[0], taxon)
    references = {"UniProtKB:P32352": project_reference(old_entries[0])}
    mappings = {
        REUSED: {**map_entity(entities[REUSED], old_entries), "query_source": "reused-reference-canary"}
    }
    sources = {}
    for key, item in plan["requests"].items():
        entries, sources[key] = read_batch(root, directory, key, plan, entities)
        for entry in entries:
            projected = project_reference(entry)
            accession = projected["protein_accession"]
            if accession in references and references[accession] != projected:
                raise ValueError("conflicting cross-batch reference metadata")
            references[accession] = projected
        for entity_key in item["entity_keys"]:
            mappings[entity_key] = {**map_entity(entities[entity_key], entries), "query_source": key}
    if set(mappings) != set(entities):
        raise ValueError("incomplete entity accounting")
    return {
        "scope": "COMPLETE_STUDY_REFERENCE_QUERY_SUCCESSOR_NOT_EXPERIMENTAL_ALLELE_CURATION",
        "uniprot_release": "2026_03",
        "records": cohort["records"],
        "inputs": {
            "cohort": reference.pin(root, cohort_path),
            "prior": cohort["prior"],
            "census": cohort["census"],
            "request_plan": reference.pin(root, directory / "request-plan.json"),
            "canary_review": reference.pin(root, directory / "canary-review.json"),
            "sources": sources,
            "reused_reference": reused,
            "taxonomy": taxon_source,
            "original_rejected_query": rejected,
        },
        "reference_entities": dict(sorted(mappings.items())),
        "references": dict(sorted(references.items())),
        "experimental_context": prior["experimental_context"],
        "interpretation": {
            **prior["interpretation"],
            "reference_hold": (
                "Historical HTTP 400 input-size rejection preserved. Three bounded successor queries "
                "completed this reference scope; no held primary paper was revisited."
            ),
        },
        "source_evidence": {
            "doi": "DOI:10.1371/journal.pone.0164175",
            "pmid": "PMID:27711131",
            "table_rows": "prior.source_rows (zero-based source_row indexes)",
            "figure_rows": "prior.reconstruction_figure (zero-based figure_rows indexes)",
            "historical_reference_statuses_superseded_only_for_this_successor_scope": True,
            "phenotypes_and_experimental_contexts_unchanged": True,
            "species_node_basis": "UNIPROT_REFERENCE_LINEAGE_NOT_NEW_NCBI_REQUEST",
            "source_gene_labels_preserved": True,
            "reference_locus_is_tested_deletion_identity": False,
        },
        "summary": {
            "entities": len(mappings),
            "table_loci": 127,
            "additional_figure_symbols": 3,
            "unique_reference_proteins": len(references),
            "mapped_entities": sum(bool(v["reference_candidates"]) for v in mappings.values()),
            "unmatched_entities": [k for k, v in mappings.items() if not v["reference_candidates"]],
            "multiple_candidate_entities": [
                k for k, v in mappings.items() if len(v["reference_candidates"]) > 1
            ],
            "source_label_differences": [
                k
                for k, v in mappings.items()
                if any(
                    c["source_gene_label_status"] == "SOURCE_LABEL_DIFFERS_FROM_CURRENT_GENE_NAMES"
                    for c in v["reference_candidates"]
                )
            ],
            "reused_reference_entities": 1,
            "new_requests": 3,
            "new_taxonomy_requests": 0,
            "source_resistance_labeled_mutants": 78,
            "source_hypersensitivity_labeled_mutants": 49,
            "source_dubious_orfs": 15,
            "records_unchanged": 2939,
            "experimental_allele_subject_or_genome_assignments": 0,
            "whole_record_primary_signoffs": 0,
        },
        "constraints": {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "source_adoptions": 0,
            "primary_access_holds_preserved": True,
            "primary_paper_requests": 0,
            "original_HTTP_400_is_input_validation_not_access_denial": True,
            "biological_records_changed": 0,
            "github_mutations": 0,
            "full_corpus_goal_status": "OPEN",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != encoded:
            raise ValueError("saved reference successor differs from native replay")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(encoded)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
