"""Audit source definition bibliography offline, without asserting biological support.

OWL axiom annotations are bound to exact RDF triples. Synonym/class xrefs are
kept separate, and arbitrary annotation text is hashed rather than exported.
"""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import audit_card_term_scope as ontology
import audit_topoisomerase_references as reference
from rdflib import OWL, RDF, RDFS, Graph, Literal, URIRef
from seed_from_sources import is_card_sourced

from antibioticmech.activity_collections import load_record

DEFAULT_COHORT = Path("reports/resistance-grounding-2026-10-09-salmonella-scope/cohort.json")
DEFAULT_OUTPUT = Path("research/2026-10-09-card-definition-citations.json")
DEFINITION = URIRef("http://purl.obolibrary.org/obo/IAO_0000115")
XREF = URIRef(ontology.NS["oboInOwl"] + "hasDbXref")
SCOPE = "SOURCE_DEFINITION_BIBLIOGRAPHY_NOT_VERIFIED_GENE_ALLELE_OR_PHENOTYPE_EVIDENCE"


def text_hash(value):
    return hashlib.sha256(str(value).encode()).hexdigest()


def rdf_identity(value):
    if isinstance(value, Literal):
        return {"kind": "literal", "sha256": text_hash(value), "language": value.language,
                "datatype": str(value.datatype) if value.datatype else None}
    if isinstance(value, URIRef):
        return {"kind": "iri", "sha256": text_hash(value)}
    raise ValueError("unsupported anonymous annotation value")


def bibliography(values):
    accepted, other = set(), set()
    for value in values:
        raw = str(value)
        if isinstance(value, Literal) and (
            re.fullmatch(r"PMID:[1-9][0-9]*", raw)
            or re.fullmatch(r"DOI:10\.[0-9]{4,9}/[^\s]+", raw)
        ):
            accepted.add(raw)
        else:
            other.add(json.dumps(rdf_identity(value), sort_keys=True))
    return {"identifiers": sorted(accepted), "other_xrefs": [json.loads(row) for row in sorted(other)]}


def project_annotations(graph, labels):
    """Validate the exact annotated triple, including language and datatype."""
    result = {}
    for tid, label in sorted(labels.items()):
        node = URIRef(ontology.BASE + tid.removeprefix("ARO:"))
        names = list(graph.objects(node, RDFS.label))
        if ((node, RDF.type, OWL.Class) not in graph or len(names) != 1
                or str(names[0]) != label):
            raise ValueError("source class identity or label differs from ontology")
        if any(str(v).lower() in {"true", "1"} for v in graph.objects(node, OWL.deprecated)):
            raise ValueError("selected source class is deprecated")
        definitions = [rdf_identity(v) for v in graph.objects(node, DEFINITION)]
        result[tid] = {
            "label_sha256": text_hash(label),
            "definitions": sorted(definitions, key=lambda x: json.dumps(x, sort_keys=True)),
            "definition_axioms": [], "other_axioms": [],
            "class_xrefs": bibliography(graph.objects(node, XREF)),
        }
    for axiom in graph.subjects(RDF.type, OWL.Axiom):
        sources = list(graph.objects(axiom, OWL.annotatedSource))
        if not any(ontology.curie(str(node)) in labels for node in sources):
            continue
        properties = list(graph.objects(axiom, OWL.annotatedProperty))
        targets = list(graph.objects(axiom, OWL.annotatedTarget))
        if len(sources) != 1 or len(properties) != 1 or len(targets) != 1:
            raise ValueError("ambiguous or missing axiom binding")
        source, predicate, target = sources[0], properties[0], targets[0]
        if not isinstance(predicate, URIRef) or (source, predicate, target) not in graph:
            raise ValueError("annotated triple is not asserted in the ontology")
        row = {"predicate": str(predicate), "target": rdf_identity(target),
               **bibliography(graph.objects(axiom, XREF))}
        key = "definition_axioms" if predicate == DEFINITION else "other_axioms"
        result[ontology.curie(str(source))][key].append(row)
    for row in result.values():
        for key in ("definition_axioms", "other_axioms"):
            row[key].sort(key=lambda x: json.dumps(x, sort_keys=True))
        row["definition_citation_ids"] = sorted({v for a in row["definition_axioms"]
                                                for v in a["identifiers"]})
        row["definition_citation_status"] = (
            "CITATIONS_PRESENT_PRIMARY_SUPPORT_UNREVIEWED" if row["definition_citation_ids"]
            else "NO_ALLOWLISTED_DEFINITION_CITATION_IN_PINNED_ONTOLOGY"
        )
        row["biological_support_inferred"] = False
    return result


def read_corpus(root, census_path):
    with census_path.open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (not census or len({r["identifier"] for r in census}) != len(census)
            or len({r["path"] for r in census}) != len(census)
            or {r["path"] for r in census} != {
                str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}):
        raise ValueError("census does not uniquely cover every current record")
    labels, memberships, records = {}, defaultdict(list), []
    for row in census:
        path = reference.check_pin(root, {"path": row["path"], "sha256": row["record_sha256"]})
        record = load_record(path)
        if (record["identifier"] != row["identifier"]
                or record["chemical_structure"]["standard_inchi_key"] != row["standard_inchi_key"]):
            raise ValueError("current compound identity differs from census")
        claims = [c for c in record.get("resistance_mechanisms", []) if is_card_sourced(c)]
        if not claims:
            continue
        records.append({"identifier": row["identifier"], "path": row["path"],
                        "sha256": row["record_sha256"], "standard_inchi_key": row["standard_inchi_key"]})
        for claim in claims:
            tid = claim["aro_id"]
            if tid in labels and labels[tid] != claim["label"]:
                raise ValueError("source term has conflicting labels")
            labels[tid] = claim["label"]
            memberships[tid].append(row["identifier"])
    return census, labels, memberships, records


def analyze(root, cohort_path, only=None):
    cohort = json.loads(cohort_path.read_bytes())
    inputs = {key: cohort[key] for key in ("current_census", "source_scope", "ontology_cache",
                                          "source_inventory", "prior_checkpoint")}
    paths = {key: reference.check_pin(root, value) for key, value in inputs.items()}
    source_scope = json.loads(paths["source_scope"].read_bytes())
    if any(source_scope[key] != inputs[key] for key in ("ontology_cache", "source_inventory")):
        raise ValueError("source scope pins differ from cohort")
    cached = json.loads(paths["ontology_cache"].read_bytes())
    body = cached["body"].encode()
    match = re.fullmatch(r"https://raw\.githubusercontent\.com/arpcard/aro/([0-9a-f]{40})/aro\.owl",
                         cached["url"])
    if (cached["status"] != 200 or hashlib.sha256(body).hexdigest() != cached["sha256"]
            or len(body) != cached["bytes"] or match is None):
        raise ValueError("ontology cache identity or digest mismatch")
    census, labels, memberships, records = read_corpus(root, paths["current_census"])
    if set(labels) != set(source_scope["terms"]):
        raise ValueError("current CARD cohort differs from the full source-term scope")
    with paths["source_inventory"].open(newline="") as stream:
        inventory = list(csv.DictReader(stream, delimiter="\t"))
    names = defaultdict(set)
    for row in inventory:
        names[row["determinant_id"]].add(row["determinant_name"])
    if any(names[tid] != {label} for tid, label in labels.items()):
        raise ValueError("source inventory term identity mismatch")
    selected = set(labels) if only is None else set(only)
    if not selected or not selected <= set(labels):
        raise ValueError("invalid term selection")
    graph = Graph().parse(data=body, format="xml")
    terms = project_annotations(graph, {tid: labels[tid] for tid in selected})
    for tid, row in terms.items():
        row["record_memberships"] = sorted(memberships[tid])
    selected_ids = {record_id for tid in selected for record_id in memberships[tid]}
    selected_records = [row for row in records if row["identifier"] in selected_ids]
    definition_ids = {value for row in terms.values() for value in row["definition_citation_ids"]}
    cited = {tid for tid, row in terms.items() if row["definition_citation_ids"]}
    result = {
        "scope": SCOPE, "selection": "ALL_EXISTING_CARD_TERMS" if only is None else "CANARY_ONLY",
        "inputs": {**inputs, "cohort": reference.pin(root, cohort_path)},
        "ontology": {key: cached[key] for key in ("url", "sha256", "retrieved_at")},
        "attribution": {"source": "CARD Antibiotic Resistance Ontology",
                        "license_url": f"https://github.com/arpcard/aro/blob/{match[1]}/LICENSE"},
        "terms": terms, "records": selected_records,
        "summary": {
            "corpus_records_checked": len(census), "terms": len(terms),
            "source_assertion_memberships": sum(len(memberships[t]) for t in selected),
            "compound_records": len(selected_records), "terms_with_definition_citations": len(cited),
            "terms_without_allowlisted_definition_citations": len(terms) - len(cited),
            "assertion_memberships_with_definition_citations": sum(len(memberships[t]) for t in cited),
            "unique_definition_citation_ids": len(definition_ids),
            "definition_identifier_namespaces": dict(sorted(Counter(v.split(":")[0]
                                                                   for v in definition_ids).items())),
            "definition_axioms": sum(len(r["definition_axioms"]) for r in terms.values()),
            "other_axioms": sum(len(r["other_axioms"]) for r in terms.values()),
            "biological_records_changed": 0, "whole_record_reviews_completed": 0,
        },
        "limits": [
            "Bibliography membership does not verify a causal effect, allele, organism or assay.",
            "Missing definition citations in this snapshot is not absence of biological evidence.",
            "Class, synonym and other annotation xrefs are not definition citations.",
            "No sequences, variants, protocols or numerical AST are exported.",
            "No network requests, NCBI endpoint use, source adoption or GitHub mutation.",
            "Whole-corpus primary review remains OPEN; source labels and definitions are hashed only.",
        ],
    }
    for item in inputs.values():
        reference.check_pin(root, item)
    for row in census:
        reference.check_pin(root, {"path": row["path"], "sha256": row["record_sha256"]})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--cohort", type=Path, default=DEFAULT_COHORT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--only", action="append")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = analyze(args.root, args.root / args.cohort, args.only)
    body = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    output = args.root / args.output
    if args.check:
        if output.read_bytes() != body:
            raise ValueError("citation dossier does not reproduce")
    else:
        with output.open("xb") as stream:
            stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
