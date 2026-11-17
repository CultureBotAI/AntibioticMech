"""Replay bounded Mex reference metadata without assigning experimental identities."""

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

from audit_card_protein_name_screen import project_reference, selected_claims
from audit_card_reference_lineages import native_taxon
from audit_card_reference_memberships import checksum
from audit_topoisomerase_references import check_pin, digest, pin
from audit_vgb_evidence import require

from antibioticmech.activity_collections import load_record

PREFIX = "research/2026-10-15-mex-component-references"
PLAN = Path(PREFIX + "-native-plan.json")
OUTPUT = Path(PREFIX + ".json")
SCOPE = "MEX_COMPONENT_REFERENCE_EXAMPLES_NOT_SINGLE_PROTEIN_COMPLEX_OR_EXPERIMENTAL_ALLELES"
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_card,lit_pubmed_id,sequence_version,version,cc_subunit"
)
RELEASE = "2026_03"
LIMITS = {
    "biological_records_changed": 0,
    "experimental_identity_assignments": 0,
    "exact_allele_assignments": 0,
    "new_primary_results_reviews": 0,
    "curated_ast_observations": 0,
    "whole_record_primary_signoffs": 0,
    "ncbi_requests": 0,
    "source_adoptions": 0,
    "outreach": 0,
    "github_mutations": 0,
    "issue_1040": "DEFERRED",
    "reuse_terms_review_resumed": False,
    "broad_reference_index_updated": False,
    "exhaustive_gene_alias_strain_or_allele_search": False,
    "single_protein_complex_assignments": 0,
    "full_corpus_goal_status": "OPEN",
}


def read_json(root, item):
    return json.loads(check_pin(root, item).read_bytes())


def parameters(symbols, taxid, reviewed):
    query = "(" + " OR ".join("gene_exact:" + g for g in symbols) + ")"
    query += f" AND taxonomy_id:{taxid} AND reviewed:{str(reviewed).lower()}"
    return {
        "query": [query],
        "format": ["json"],
        "size": ["500"],
        "sort": ["accession asc"],
        "fields": [FIELDS],
    }


def native_query(root, source, expected):
    receipt = read_json(root, source)
    url = urlsplit(receipt["url"])
    headers = receipt["headers"]
    require(
        url.scheme == "https"
        and url.netloc == "rest.uniprot.org"
        and url.path == "/uniprotkb/search"
        and not url.fragment
        and parse_qs(url.query, keep_blank_values=True) == expected
        and receipt["status"] == 200
        and receipt["redirects_followed"] == receipt["retries"] == 0
        and headers.get("x-uniprot-release") == RELEASE
        and not headers.get("link")
        and not headers.get("location"),
        "native query identity, status or pagination changed",
    )
    path = check_pin(root, receipt["body"])
    require(path.stat().st_size == receipt["bytes"], "native response size changed")
    entries = json.loads(path.read_bytes())["results"]
    accessions = [e["primaryAccession"] for e in entries]
    require(
        len(entries) == int(headers["x-total-results"]) <= 500
        and len(accessions) == len(set(accessions))
        and accessions == sorted(accessions),
        "native result count, duplicate accession or ordering changed",
    )
    require(
        all(not {"sequence", "features"} & set(e) for e in entries), "unexpected sequence or variant data"
    )
    return {e["primaryAccession"]: e for e in entries}, {
        "receipt": source,
        **receipt,
        "complete_for_exact_query": True,
        "empty_result_means_biological_absence": False,
    }


def current_context(root, plan):
    require(plan["scope"] == SCOPE, "scope changed")
    screen = read_json(root, plan["screen"])
    index = read_json(root, plan["base_index"])
    update = read_json(root, plan["corpus_update"])
    expected_terms = {t: row for t, row in screen["terms"].items() if row["source_label"].startswith("Mex")}
    require(
        set(expected_terms) == set(plan["terms"]) and len(expected_terms) == 16, "complete Mex cohort changed"
    )
    symbols = set()
    for tid, term in plan["terms"].items():
        for key in ("source_label", "record_memberships", "definition_citation_ids"):
            require(term[key] == expected_terms[tid][key], "source term context changed")
        require(
            not index["terms"][tid]["links"] and term["label_tokens_are_queries_not_verified_composition"],
            "term selection or interpretation changed",
        )
        symbols.update(term["component_search_symbols"])
        if term["regulatory_search_symbol"]:
            symbols.add(term["regulatory_search_symbol"])
    require(
        sorted(symbols) == plan["search_symbols"] and len(symbols) == 29, "search symbol coverage changed"
    )
    for key in ("source_inventory", "source_queue", "definition_citations"):
        check_pin(root, index["inputs"][key])
    census_path = check_pin(root, index["inputs"]["census"])
    with census_path.open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    deltas = {d["path"]: d for d in update["record_deltas"]}
    require(len(deltas) == len(update["record_deltas"]) == 3, "qualification deltas changed")
    paths = {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
    require(
        len(census) == len({r["identifier"] for r in census}) == len(paths) == 2939
        and {r["path"] for r in census} == paths
        and set(deltas) <= paths,
        "corpus membership changed",
    )
    current = []
    for row in census:
        expected_hash = row["record_sha256"]
        if row["path"] in deltas:
            delta = deltas[row["path"]]
            require(
                delta["before_sha256"] == expected_hash and delta["identifier"] == row["identifier"],
                "qualification delta identity changed",
            )
            expected_hash = delta["after_sha256"]
        require(digest(root / row["path"]) == expected_hash, "current corpus bytes changed")
        current.append({**row, "record_sha256": expected_hash})
    ids = {rid for t in plan["terms"].values() for rid in t["record_memberships"]}
    records = [row for row in current if row["identifier"] in ids]
    actual = []
    claims = [c for c in index["claims"] if c["aro_id"] in plan["terms"]]
    for row in records:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "complete record identity changed",
        )
        for i, claim in selected_claims(doc, plan["terms"]):
            require(claim["label"] == plan["terms"][claim["aro_id"]]["source_label"], "claim label changed")
            actual.append((row["identifier"], i, claim["aro_id"], checksum(claim)))
    require(
        len(records) == 27
        and len(actual) == 77
        and sorted(actual)
        == sorted(
            (c["record_identifier"], c["resistance_index"], c["aro_id"], c["claim_sha256"]) for c in claims
        ),
        "claim membership or source ownership changed",
    )
    for tid, term in plan["terms"].items():
        require(
            sorted({rid for rid, _, t, _ in actual if t == tid}) == term["record_memberships"],
            "term record membership changed",
        )
    hashes = {row["identifier"]: row["record_sha256"] for row in records}
    claims = [{**c, "record_sha256": hashes[c["record_identifier"]]} for c in claims]
    return records, claims, index["inputs"]


def component_annotations(entry, assessments):
    result = []
    for row in assessments:
        require(row["pointer"] == "/comments/0/texts/0", "unreviewed annotation pointer")
        comment = entry["comments"][0]
        text = comment["texts"][0]
        require(
            comment["commentType"] == "SUBUNIT"
            and hashlib.sha256(text["value"].encode()).hexdigest() == row["text_sha256"]
            and f"Component of the {row['complex_label']} multidrug efflux complex" in text["value"]
            and all(q in text["value"] for q in row["native_relation_qualifiers"]),
            "native component annotation changed",
        )
        result.append(
            {
                **row,
                "whole_text_evidence": text.get("evidences", []),
                "evidence_scope": "WHOLE_NATIVE_TEXT_NOT_RELATION_LEVEL_PRIMARY_PROOF",
                "primary_results_independently_reviewed": False,
            }
        )
    require(len({r["complex_label"] for r in result}) == len(result), "duplicate component annotation")
    return result


def term_projection(term, references):
    components = {}
    complex_name = term["complex_label"]
    for gene in term["component_search_symbols"]:
        candidates = [a for a, p in references.items() if gene in p["gene_symbols"]]
        annotated = [
            a
            for a in candidates
            if any(c["complex_label"] == complex_name for c in references[a]["component_annotations"])
        ]
        components[gene] = {
            "symbol_query_candidates": candidates,
            "native_complex_component_references": annotated,
            "status": "NATIVE_COMPONENT_ANNOTATION_REFERENCE_ONLY"
            if annotated
            else "SYMBOL_MATCH_ONLY_COMPONENT_CONTEXT_UNRESOLVED"
            if candidates
            else "NO_MATCH_IN_BOUNDED_QUERIES_NOT_BIOLOGICAL_ABSENCE",
        }
    regulator = term["regulatory_search_symbol"]
    regulator_candidates = (
        [a for a, p in references.items() if regulator in p["gene_symbols"]] if regulator else []
    )
    complete = all(c["native_complex_component_references"] for c in components.values())
    return {
        **term,
        "components": components,
        "regulatory_subject_candidates": regulator_candidates,
        "all_label_components_have_native_annotations": complete,
        "regulatory_candidate_is_structural_component": False,
        "regulatory_alteration_or_effect_verified": False,
        "reference_species_or_strain_is_experimental_subject": False,
        "complex_has_single_protein_identity": False,
        "selected_for_broad_single_protein_index": False,
        "whole_record_primary_review": "OPEN",
    }


def build(root):
    native_plan = json.loads((root / PLAN).read_bytes())
    plan = read_json(root, native_plan["discovery_plan"])
    followup = read_json(root, native_plan["followup_plan"])
    require(followup["prior_plan"] == native_plan["discovery_plan"], "follow-up plan mismatch")
    records, claims, inputs = current_context(root, plan)
    require(
        set(native_plan["queries"]) == {"canary", "cohort", "pao1-unreviewed", "opra-unreviewed"},
        "query coverage changed",
    )
    canary, canary_source = native_query(
        root, native_plan["queries"]["canary"], parameters(["mexA"], 287, True)
    )
    proof = read_json(root, native_plan["canary_inspected"])
    require(
        set(canary) == {"P52477"}
        and proof["accepted"] is True
        and proof["response"] == canary_source["body"],
        "canary not inspected",
    )
    entries, cohort_source = native_query(
        root, native_plan["queries"]["cohort"], parameters(plan["search_symbols"], 287, True)
    )
    require(
        len(entries) == 13
        and all(e["entryType"] == "UniProtKB reviewed (Swiss-Prot)" for e in entries.values())
        and all(entries[a] == e for a, e in canary.items())
        and followup["reviewed_response"] == cohort_source["body"],
        "reviewed cohort or canary differs",
    )
    found = {g["geneName"]["value"] for e in entries.values() for g in e.get("genes", []) if "geneName" in g}
    missing = sorted(set(plan["search_symbols"]) - found)
    require(missing == followup["missing_symbols"], "follow-up symbols changed")
    queries = {"canary": canary_source, "cohort": cohort_source}
    for key, symbols, taxid in (
        ("pao1-unreviewed", [g for g in missing if g != "oprA"], 208964),
        ("opra-unreviewed", ["oprA"], 287),
    ):
        additional, queries[key] = native_query(
            root, native_plan["queries"][key], parameters(symbols, taxid, False)
        )
        require(
            queries[key]["url"] == followup["urls"][key] and not set(additional) & set(entries),
            "follow-up query changed or duplicates earlier cohort",
        )
        require(
            all(
                e["entryType"] == "UniProtKB unreviewed (TrEMBL)" and e["organism"]["taxonId"] == taxid
                for e in additional.values()
            ),
            "unreviewed reference context changed",
        )
        entries.update(additional)
    taxa, taxonomy_sources = {}, {}
    require(
        set(native_plan["taxonomy"]) == {str(e["organism"]["taxonId"]) for e in entries.values()},
        "taxonomy coverage differs",
    )
    for taxid, source in native_plan["taxonomy"].items():
        taxa[taxid], taxonomy_sources[taxid] = native_taxon(root, source, taxid, RELEASE)
    references = {}
    assessments = native_plan["component_assessments"]
    require(set(assessments) <= set(entries), "unknown component reference")
    for accession, entry in sorted(entries.items()):
        projected = project_reference(entry, taxa[str(entry["organism"]["taxonId"])])
        require(
            projected["reference_taxonomy"]["species"]["taxonId"] == 287
            and set(projected["gene_symbols"]) <= set(plan["search_symbols"]),
            "unexpected reference species or gene symbol",
        )
        projected["component_annotations"] = component_annotations(entry, assessments.get(accession, []))
        projected["gene_match_alone_proves_component_membership"] = False
        references[projected["accession"]] = projected
    terms = {tid: term_projection(term, references) for tid, term in sorted(plan["terms"].items())}
    with_annotations = {
        tid for tid, term in terms.items() if term["all_label_components_have_native_annotations"]
    }
    symbols_found = {g for r in references.values() for g in r["gene_symbols"]}
    return {
        "date": "2026-10-15",
        "scope": SCOPE,
        "plan": pin(root, root / PLAN),
        "discovery_plan": native_plan["discovery_plan"],
        "followup_plan": native_plan["followup_plan"],
        "historical_index": plan["base_index"],
        "explicit_corpus_update": plan["corpus_update"],
        "inputs": {
            k: inputs[k] for k in ("census", "source_inventory", "source_queue", "definition_citations")
        },
        "records": records,
        "claims": claims,
        "terms": terms,
        "reference_candidates": references,
        "queries": queries,
        "taxonomy_sources": taxonomy_sources,
        "unmatched_symbols": sorted(set(plan["search_symbols"]) - symbols_found),
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(records),
            "source_terms": len(terms),
            "source_claims": len(claims),
            "queried_symbols": 29,
            "matched_symbols": len(symbols_found),
            "reference_entries": len(references),
            "reference_entry_types": dict(
                sorted(Counter(r["entry_type"] for r in references.values()).items())
            ),
            "reference_taxa": len(taxa),
            "new_taxonomy_requests": 0,
            "new_uniprot_searches": len(queries),
            "native_component_annotations": sum(len(r["component_annotations"]) for r in references.values()),
            "terms_with_all_label_components_annotated": len(with_annotations),
            "claims_with_all_label_components_annotated": sum(
                c["aro_id"] in with_annotations for c in claims
            ),
        },
        "limits": LIMITS,
        "attribution": (
            "CARD/ARO and UniProt release 2026_03, CC BY 4.0; no primary article text redistributed."
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
            stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
