"""Resolve names in CARD's RNA-ancestor cohort, not experimental organisms.

Only exact UniProt Taxonomy scientific names or explicit synonyms can resolve.
The source ontology's protein/RNA conflict is retained, not silently corrected.
"""

import argparse
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import audit_card_grounding as card
import audit_card_term_scope as scope
import audit_resistance_grounding as common

COHORT = "RNA_TERM_NOT_A_PROTEIN_PRODUCT"
SCOPE = "CARD_LABEL_ORGANISM_NAME_ONLY_NOT_EXPERIMENTAL_SUBJECT_GENE_OR_ALLELE_GROUNDING"
CONFLICT_ID = "ARO:3004956"
CONFLICT_DEFINITION = (
    "rpld encodes for the 50S L4 ribosomal protein, is a macrolide resistance "
    "protein identified in Neisseria gonorrhoeae."
)


def source_name(tid, label):
    if tid == CONFLICT_ID:
        if label != "Neisseria gonorrhoeae rpld":
            raise ValueError("reviewed protein/RNA conflict label changed")
        return "Neisseria gonorrhoeae", "PROTEIN_DEFINITION_CONFLICTS_WITH_RNA_ANCESTRY"
    if tid == "ARO:3004057":
        if label != "23S rRNA with mutation conferring resistance to linezolid antibiotics":
            raise ValueError("reviewed organism-free label changed")
        return None, "RNA_LABEL_NOT_PRIMARY_VALIDATION"
    if tid == "ARO:3004161":
        if label != "Propionibacteria 23S rRNA with mutation conferring resistance to macrolide antibiotics":
            raise ValueError("reviewed broad-organism label changed")
        return "Propionibacteria", "RNA_LABEL_NOT_PRIMARY_VALIDATION"
    match = re.fullmatch(r"([A-Z][a-z]+ [a-z]+) (?:16S|23[Ss]) rRNA .+", label)
    if match is None:
        raise ValueError("unreviewed label syntax; do not guess an organism")
    return match[1], "RNA_LABEL_NOT_PRIMARY_VALIDATION"


def parameters(name):
    if re.fullmatch(r"[A-Z][a-z]+ [a-z]+", name) is None:
        raise ValueError("only reviewed binomial names may be queried")
    return {"query": f'"{name}" AND rank:species', "format": "json", "size": "500"}


def cache_path(name):
    key = common.digest(json.dumps([
        "https://rest.uniprot.org/taxonomy/search", parameters(name),
    ], sort_keys=True).encode())
    return common.OUT / f"request-{key}.json"


def resolve_name(name, response):
    parsed = urlparse(response["url"])
    expected = {k: [v] for k, v in parameters(name).items()}
    if (parsed.scheme != "https" or parsed.netloc != "rest.uniprot.org"
            or parsed.path != "/taxonomy/search" or parsed.fragment
            or parse_qs(parsed.query, keep_blank_values=True) != expected):
        raise ValueError("taxonomy response request identity mismatch")
    if response["status"] != 200 or common.digest(response["body"].encode()) != response["sha256"]:
        raise ValueError("taxonomy response status or checksum mismatch")
    headers = {k.lower(): v for k, v in response["headers"].items()}
    entries = json.loads(response["body"])["results"]
    if (len(entries) != int(headers["x-total-results"]) or len(entries) > 500
            or headers.get("link")):
        raise ValueError("taxonomy search is incomplete; review a narrower canary")
    if not headers.get("x-uniprot-release"):
        raise ValueError("taxonomy response lacks release provenance")
    candidates, seen = [], set()
    for entry in entries:
        taxid = entry["taxonId"]
        if type(taxid) is not int or taxid < 1 or taxid in seen:
            raise ValueError("invalid or duplicate taxonomy identifier")
        seen.add(taxid)
        if (not isinstance(entry.get("scientificName"), str) or not entry["scientificName"]
                or not isinstance(entry.get("rank"), str) or type(entry.get("active")) is not bool
                or any(not isinstance(entry.get(key, []), list)
                       or any(not isinstance(value, str) for value in entry[key])
                       for key in ("synonyms", "otherNames") if key in entry)):
            raise ValueError("invalid taxonomy name or status fields")
        fields = (["scientificName"] if name == entry["scientificName"] else [])
        if name in entry.get("synonyms", []):
            fields.append("synonyms")
        candidates.append({
            "taxon_id": f"NCBITaxon:{taxid}", "scientific_name": entry["scientificName"],
            "rank": entry["rank"], "active": entry["active"], "exact_name_fields": fields,
            "other_name_match_only": not fields and name in entry.get("otherNames", []),
        })
    candidates.sort(key=lambda c: int(c["taxon_id"].split(":")[1]))
    accepted = [c for c in candidates if c["active"] is True and c["rank"] == "species"
                and c["exact_name_fields"]]
    return {
        "status": "EXACT_SPECIES_NAME_RESOLVED" if len(accepted) == 1 else
        "AMBIGUOUS_EXACT_SPECIES_NAMES" if accepted else "NO_EXACT_ACTIVE_SPECIES_NAME",
        "named_organism_taxon_id": accepted[0]["taxon_id"] if len(accepted) == 1 else None,
        "candidates": candidates, "release": headers["x-uniprot-release"],
        "request": {k: response[k] for k in ("url", "status", "sha256", "retrieved_at")},
    }


def check_definition(body):
    root = ET.fromstring(body)
    about = "{" + scope.NS["rdf"] + "}about"
    tag = "{http://purl.obolibrary.org/obo/}IAO_0000115"
    definitions = [child.text for node in root.iter()
                   if node.get(about) == scope.BASE + CONFLICT_ID.split(":")[1]
                   for child in node if child.tag == tag]
    if definitions != [CONFLICT_DEFINITION]:
        raise ValueError("reviewed protein/RNA conflict definition changed")
    return common.digest(CONFLICT_DEFINITION.encode())


def analyze(root, scope_path, only=None):
    source_bytes = scope_path.read_bytes()
    source = json.loads(source_bytes)
    inputs = [source[key] for key in ("ontology_cache", "reference_audit", "reference_ledger",
                                     "source_inventory", "current_corpus")]
    ontology_cache = root / source["ontology_cache"]["path"]
    audit_path = root / source["reference_audit"]["path"]
    ledger_path = root / source["reference_ledger"]["path"]
    # Reproduce the full prior audit before interpreting its selected ancestry cohort.
    if scope.analyze(root, ontology_cache, audit_path, ledger_path) != source:
        raise ValueError("prior term-scope audit does not reproduce")
    definition_hash = check_definition(json.loads(ontology_cache.read_bytes())["body"])
    audit = json.loads(audit_path.read_bytes())
    cohort = {tid for tid, row in source["terms"].items() if row["entity_scope"] == COHORT}
    selected = cohort if only is None else set(only)
    if not selected or not selected <= cohort:
        raise ValueError("selection is outside the reviewed ancestry cohort")
    terms, names = {}, {}
    for tid in sorted(selected):
        labels = audit["determinants"][tid]["labels"]
        if len(labels) != 1:
            raise ValueError("ambiguous determinant label")
        name, entity_review = source_name(tid, labels[0])
        if name is None:
            status, taxid = "SOURCE_LABEL_HAS_NO_ORGANISM", None
        elif name == "Propionibacteria":
            status, taxid = "BROAD_SOURCE_NAME_UNRESOLVED", None
        else:
            if name not in names:
                response = common.fetch("taxonomy/search", parameters(name))
                names[name] = resolve_name(name, response)
                if json.loads(cache_path(name).read_bytes()) != response:
                    raise ValueError("taxonomy cache differs from reviewed response")
                names[name]["cache"] = scope.pin(root, cache_path(name))
            status = names[name]["status"]
            taxid = names[name]["named_organism_taxon_id"]
        terms[tid] = {
            "source_label_sha256": common.digest(labels[0].encode()),
            "source_organism_label": name, "name_resolution": status,
            "named_organism_taxon_id": taxid, "entity_review": entity_review,
            "rna_ancestor_path": source["terms"][tid]["anchor_paths"]["ARO:3000328"],
            "primary_review_status": audit["determinants"][tid]["primary_review_status"],
        }
    releases = {row["release"] for row in names.values()}
    if len(releases) > 1:
        raise ValueError("taxonomy release changed across selected names")
    records = card.current_corpus(root)
    claims = [(r, c) for r, c in card.claims_from(records) if c["aro_id"] in selected]
    for tid, row in terms.items():
        row["record_ids"] = sorted({r["identifier"] for r, c in claims if c["aro_id"] == tid})
        row["assertion_count"] = sum(c["aro_id"] == tid for _, c in claims)
    if scope_path.read_bytes() != source_bytes:
        raise ValueError("prior audit changed during name review")
    for pin in inputs:
        if common.digest((root / pin["path"]).read_bytes()) != pin["sha256"]:
            raise ValueError("source input changed during name review")
    for row in names.values():
        path = root / row["cache"]["path"]
        if common.digest(path.read_bytes()) != row["cache"]["sha256"]:
            raise ValueError("taxonomy cache changed during name review")
    return {
        "scope": SCOPE, "selection": "ALL_RNA_ANCESTOR_TERMS" if only is None else "CANARY_ONLY",
        "source_term_scope": scope.pin(root, scope_path), "ontology": source["ontology"],
        "source_inventory": source["source_inventory"], "current_corpus": source["current_corpus"],
        "names": names, "terms": terms,
        "source_conflicts": ({CONFLICT_ID: {
            "status": "PROTEIN_DEFINITION_CONFLICTS_WITH_RNA_ANCESTRY",
            "definition_predicate": "http://purl.obolibrary.org/obo/IAO_0000115",
            "definition_sha256": definition_hash,
            "note": "The ontology definition names a 50S L4 ribosomal protein; "
                    "the named subclass path leads to the rRNA determinant anchor. "
                    "No RNA identity or exact protein accession is assigned by this audit.",
        }} if CONFLICT_ID in selected else {}),
        "summary": {
            "corpus_records": len(records), "selected_terms": len(terms),
            "selected_assertions": len(claims),
            "selected_records": len({r["identifier"] for r, _ in claims}),
            "queried_names": len(names), "taxonomy_release": next(iter(releases), None),
            "name_resolution_counts": dict(Counter(row["name_resolution"] for row in terms.values())),
            "entity_review_counts": dict(Counter(row["entity_review"] for row in terms.values())),
            "distinct_named_organism_taxa": len({row["named_organism_taxon_id"] for row in terms.values()
                                                if row["named_organism_taxon_id"] is not None}),
        },
        "attribution": {"sources": ["CARD curation team, Antibiotic Resistance Ontology",
                                     "UniProt Consortium, UniProt Taxonomy"],
                        "license": "CC-BY-4.0"},
        "limitations": [
            "Names are from CARD term labels, not independently identified experimental organisms.",
            "Only exact scientific names or explicit synonyms of active species entries resolve; "
            "otherNames, lineage names, substrings and homology are not accepted matches.",
            "The prior 88-term RNA category is ontology ancestry, not proof all terms denote RNA; "
            "the protein-definition conflict is preserved separately.",
            "The generic organism-free term and broad Propionibacteria label remain unresolved.",
            "No experimental strain, isolate, genome, gene locus, allele or UniProtKB protein is assigned.",
            "A TaxID match neither validates the source resistance claim "
            "nor establishes species-wide resistance.",
            "Taxonomy requests use UniProt only, not NCBI. "
            "No source is adopted or biological record changed.",
        ],
    }


def write_once(path, result):
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if path.exists():
        if path.read_bytes() != payload:
            raise ValueError("output already exists with different content")
    else:
        with path.open("xb") as handle:
            handle.write(payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--scope-audit", type=Path, default=Path("research/2026-10-09-card-term-scope.json"))
    parser.add_argument("--only", action="append")
    parser.add_argument("--allow-network", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    common.OUT = root / "reports/resistance-grounding-2026-10-07"
    common.ALLOW_NETWORK = args.allow_network
    result = analyze(root, root / args.scope_audit, args.only)
    write_once(root / args.output, result)
    print(json.dumps(result["summary"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
