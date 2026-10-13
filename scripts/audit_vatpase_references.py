"""Replay pinned V-ATPase reference metadata, never experimental resistance calls."""

import argparse
import csv
import json
from pathlib import Path

import audit_topoisomerase_references as reference
from audit_resistance_grounding import validate_cached_response

from antibioticmech.activity_collections import load_record

DEFAULT_CACHE = Path("reports/resistance-grounding-2026-10-13-vatpase")
DEFAULT_OUTPUT = Path("research/2026-10-13-vatpase-reference-context.json")
QUERIES = {
    "neurospora-c": "gene_exact:vma-3 AND organism_id:367110 AND reviewed:true",
    "yeast-proteolipids": (
        "(gene_exact:VMA3 OR gene_exact:VMA11 OR gene_exact:VMA16) "
        "AND organism_id:559292 AND reviewed:true"
    ),
}
REFERENCES = {
    "vma-3": (367110, 5141, "c"),
    "VMA3": (559292, 4932, "c"),
    "VMA11": (559292, 4932, "c'"),
    "VMA16": (559292, 4932, "c''"),
}
TARGETS = {
    "CHEBI:22689": "XDHNQDDQEHDUTM-JQWOJBOSSA-N",
    "CHEBI:73167": "DJZCTUVALDDONK-HQMSUKCRSA-N",
}
# These are observed access outcomes, not primary-text evidence or HTTP receipts.
ACCESS = {
    "11724795": {
        "doi": "10.1074/jbc.m109756200",
        "requested_url": "https://www.jbc.org/article/S0021925820874997/pdf",
        "outcome": "TOOL_REPORTED_URL_INACCESSIBLE",
    },
    "15180988": {
        "doi": "10.1074/jbc.m404638200",
        "requested_url": "https://www.sciencedirect.com/science/article/pii/S0021925820773722",
        "outcome": "TOOL_REPORTED_HTTP_403",
    },
    "16912037": {
        "doi": "10.1074/jbc.m605532200",
        "requested_url": "https://www.sciencedirect.com/science/article/pii/S0021925819841030",
        "outcome": "REQUEST_MADE_BUT_ACCESS_RESULT_NOT_RETAINED",
    },
}


def project_proteolipid(entry, gene, taxonomy):
    taxid, species, subunit = REFERENCES[gene]
    if entry["organism"]["taxonId"] != taxid or "features" in entry:
        raise ValueError("wrong reference organism or unexpected feature export")
    result = reference.project_reference(entry, gene, species, taxonomy)
    if result["protein_name"] != "V-type proton ATPase subunit " + subunit:
        raise ValueError("reference subunit identity differs from the selected gene")
    identifiers = {i["id"].lower() for b in result["bibliography"] for i in b["identifiers"]}
    result.update({
        "reference_gene": gene,
        "subunit": subunit,
        "gene_orf_names": sorted({v["value"] for g in entry.get("genes", [])
                                  for v in g.get("orfNames", [])}),
        "role": "REFERENCE_PROTEOLIPID_NOT_EXPERIMENTAL_ALLELE",
        "focal_bibliography_matches": sorted(pmid for pmid, paper in ACCESS.items()
                                             if pmid in identifiers or paper["doi"] in identifiers),
        "compound_specific_resistance_established": False,
    })
    return result


def build(root, directory):
    plan_path = directory / "cohort.json"
    plan = json.loads(plan_path.read_bytes())
    if plan["queries"] != QUERIES or plan["fields"] != reference.FIELDS:
        raise ValueError("bounded request plan changed")
    canary_path = directory / "canary-reviewed.json"
    canary = json.loads(canary_path.read_bytes())
    if canary["manually_reviewed"] is not True:
        raise ValueError("canary review missing")
    for pin in (canary["response"], canary["receipt"]):
        reference.check_pin(root, pin)
    with reference.check_pin(root, plan["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if len(census) != 2939 or set(plan["records"]) != set(TARGETS):
        raise ValueError("selected historical cohort changed")
    records = {}
    for identifier, pin in plan["records"].items():
        record = load_record(reference.check_pin(root, pin))
        row, = [r for r in census if r["identifier"] == identifier]
        if (record["identifier"] != identifier or record.get("resistance_mechanisms")
                or record["chemical_structure"]["standard_inchi_key"] != TARGETS[identifier]
                or row["record_sha256"] != pin["sha256"]):
            raise ValueError("record identity or evidence changed")
        records[identifier] = {**pin, "whole_record_review": "OPEN", "resistance_assertions_added": []}
        if identifier == "CHEBI:73167":
            alias, = [s for s in record["synonyms"] if s["synonym_text"] == "folimycin"]
            if alias["source"] != "chebi" or alias["synonym_type"] != "EXACT_SYNONYM":
                raise ValueError("folimycin identity is not an exact source synonym")
    discovery = json.loads(reference.check_pin(root, plan["discovery"]).read_bytes())
    discovery_records = {r["identifier"]: r for r in discovery["records"] if r["identifier"] in TARGETS}
    candidates = {c["pmid"]: c for r in discovery_records.values() for q in r["queries"]
                  for c in q["candidates"] if c.get("pmid") in ACCESS}
    primary = {}
    for pmid, observed in ACCESS.items():
        if candidates[pmid]["doi"].lower() != observed["doi"]:
            raise ValueError("primary lead DOI/PMID mismatch")
        primary[pmid] = {
            **observed, "pmid": pmid, "checked_on": "2026-10-13",
            "metadata_source": plan["discovery"], "primary_results_verified": False,
            "native_figures_visually_inspected": False, "local_primary_text_saved": False,
            "retry_or_alternate_transport": False,
            "observation_basis": "MANUAL_TOOL_OBSERVATION_NOT_REPLAYABLE_FROM_LOCAL_PRIMARY_BYTES",
        }
    tax_dossiers = [json.loads(reference.check_pin(root, p).read_bytes())
                    for p in plan["taxonomy_dossiers"]]
    neuro, yeast = tax_dossiers
    source_tax, = [t for t in neuro["taxonomy"] if t["taxon_id"] == 367110]
    old = source_tax["request"]
    cache = json.loads(reference.check_pin(root, old["cache"]).read_bytes())
    validate_cached_response(cache, "https://rest.uniprot.org/taxonomy/367110", None)
    tax_neuro = json.loads(cache["body"])
    release = {k.lower(): v for k, v in cache["headers"].items()}["x-uniprot-release"]
    if old["body_sha256"] != cache["sha256"] or old["url"] != cache["url"]:
        raise ValueError("reused Neurospora metadata identity changed")
    yeast_request = yeast["taxonomy_request"]
    for pin in (yeast_request["cache"], yeast_request["receipt"]):
        reference.check_pin(root, pin)
    tax_yeast, checked = reference.read_response(
        root, (root / yeast_request["cache"]["path"]).parent, "tax-559292", "/taxonomy/559292")
    if checked != yeast_request or checked["release"] != release:
        raise ValueError("taxonomy reuse or release mismatch")
    taxonomy = {367110: tax_neuro, 559292: tax_yeast}
    requests, proteins = {}, {}
    for key, query in QUERIES.items():
        params = {"query": [query], "format": ["json"], "size": ["500"], "fields": [reference.FIELDS]}
        body, request = reference.read_response(root, directory, key, "/uniprotkb/search", params)
        if request["release"] != release:
            raise ValueError("reference and taxonomy releases differ")
        expected = {"vma-3"} if key == "neurospora-c" else {"VMA3", "VMA11", "VMA16"}
        returned = set()
        for entry in body["results"]:
            gene, = [g["geneName"]["value"] for g in entry["genes"]]
            if gene not in expected or gene in returned:
                raise ValueError("unexpected or duplicate reference gene")
            returned.add(gene)
            proteins[gene] = project_proteolipid(entry, gene, taxonomy[REFERENCES[gene][0]])
        if returned != expected:
            raise ValueError("reference query did not resolve the selected genes")
        requests[key] = {**request, "results": len(returned), "complete_for_query": True,
                         "all_strains_or_unreviewed_entries_searched": False}
    reference.check_pin(root, plan["prior_progress"])
    return {
        "date": "2026-10-13", "scope": "REFERENCE_METADATA_ONLY_PRIMARY_RESISTANCE_REVIEW_UNRESOLVED",
        "inputs": {"plan": reference.pin(root, plan_path), "canary": reference.pin(root, canary_path),
                   **{k: plan[k] for k in ("census", "discovery", "taxonomy_dossiers", "prior_progress")}},
        "records": records, "primary_leads": primary,
        "reference_proteins": proteins, "uniprot_requests": requests,
        "taxonomy_reuse": {
            "367110": {**old, "release": release, "reused_byte_identically": True, "new_request": False},
            "559292": {**checked, "reused_byte_identically": True, "new_request": False},
        },
        "compound_name_grounding": {
            "folimycin": {"identifier": "CHEBI:73167", "basis": "EXACT_CHEBI_SYNONYM", "synonym": alias},
            "tested_preparations_independently_reidentified": False,
            "findings_transferred_between_compounds": False,
        },
        "summary": {"corpus_records_in_scope": 2939, "selected_records": 2, "reference_proteins": 4,
                    "complete_uniprot_queries": 2, "new_taxonomy_requests": 0,
                    "biological_records_changed": 0, "new_phi_decisions": 0,
                    "experimental_accessions_assigned": 0, "whole_records_completed": 0},
        "limits": [
            "Access outcomes are manual observations; offline replay verifies metadata, not primary results.",
            "Search-result snippets and article titles do not establish a verified resistance claim.",
            "Missing focal citations in returned bibliographies do not disprove the primary studies.",
            "Reference strain and species lineage identify database entries, "
            "not tested derivatives or isolates.",
            "Exact experimental allele, strain, genome and sample links remain unresolved, "
            "not asserted absent.",
            "ORF names remain source ORF names, not upgraded to ordered-locus identifiers.",
            "Subunits c, c-prime and c-double-prime are distinct; similar names do not transfer phenotypes.",
            "Biochemical inhibition is not MIC or organismal resistance; "
            "compound-specific effects remain unverified.",
            "No sequences, variant specifications, constructs, protocols or numeric AST are exported.",
            "No NCBI request/contact, reuse-terms review, source adoption or GitHub mutation; "
            "issue 1040 stays deferred.",
        ],
        "attribution": {"source": "UniProt Consortium", "license": "CC BY 4.0",
                        "license_url": "https://www.uniprot.org/help/license"},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    root = Path.cwd()
    result = build(root, root / args.cache)
    with args.output.open("x") as stream:
        stream.write(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n")
    print(json.dumps(result["summary"]))


if __name__ == "__main__":
    main()
