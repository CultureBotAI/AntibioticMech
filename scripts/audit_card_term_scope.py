"""Classify existing CARD term scope from pinned ontology metadata, offline only.

Named subclass paths are not experimental evidence or exact allele assignments.
OWL restrictions are checked against source edges, never followed as ancestry.
"""

import argparse
import csv
import json
import re
from collections import Counter, defaultdict, deque
from pathlib import Path

import audit_card_grounding as card
import audit_resistance_grounding as common
from rdflib import OWL, RDF, RDFS, Graph, URIRef

NS = {
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "oboInOwl": "http://www.geneontology.org/formats/oboInOwl#",
}
BASE = "http://purl.obolibrary.org/obo/ARO_"
ANCHORS = {
    "ARO:3000328": "rRNA with mutation conferring antibiotic resistance",
    "ARO:0000010": "antibiotic resistance gene cluster, cassette, or operon",
    "ARO:3000159": "efflux pump complex or subunit conferring antibiotic resistance",
    "ARO:0000031": "antibiotic resistance gene variant or mutant",
    "ARO:3000000": "determinant of antibiotic resistance",
}
ENTITY_SCOPES = {
    "ARO:3000328": "RNA_TERM_NOT_A_PROTEIN_PRODUCT",
    "ARO:0000010": "GENE_CLUSTER_NOT_ONE_PROTEIN",
    "ARO:3000159": "EFFLUX_COMPLEX_OR_SUBUNIT_GRANULARITY_UNRESOLVED",
}
SCOPE = "ONTOLOGY_TERM_SCOPE_ONLY_NOT_EXPERIMENTAL_GENE_ALLELE_OR_ORGANISM_GROUNDING"


def curie(iri):
    if re.fullmatch(re.escape(BASE) + r"[0-9]{7}", iri or ""):
        return "ARO:" + iri.removeprefix(BASE)
    return None


def parse_ontology(body):
    graph = Graph().parse(data=body, format="xml")
    terms, edges = {}, set()
    for node in graph.subjects(RDF.type, OWL.Class):
        tid = curie(str(node))
        if tid is None:
            continue
        labels = [str(label) for label in graph.objects(node, RDFS.label)]
        if tid in terms or len(labels) != 1 or not labels[0]:
            raise ValueError("duplicate or unlabeled named ARO class")
        parents, external = [], []
        restrictions = 0
        for sub in graph.objects(node, RDFS.subClassOf):
            if isinstance(sub, URIRef):
                parent = curie(str(sub))
                if parent is None:
                    external.append(str(sub))
                else:
                    parents.append(parent)
                continue
            if (sub, RDF.type, OWL.Restriction) not in graph:
                raise ValueError("unsupported anonymous subclass expression")
            restrictions += 1
            properties = list(graph.objects(sub, OWL.onProperty))
            targets = list(graph.objects(sub, OWL.someValuesFrom))
            if len(properties) != 1 or len(targets) != 1:
                raise ValueError("unsupported or ambiguous restriction")
            relation_labels = list(graph.objects(properties[0], RDFS.label))
            destination = curie(str(targets[0]))
            if len(relation_labels) == 1 and destination:
                edges.add((tid, str(relation_labels[0]), destination))
        deprecated = str(graph.value(node, OWL.deprecated) or "false")
        terms[tid] = {"label": labels[0], "parents": sorted(set(parents)),
                      "external_parents": sorted(set(external)),
                      "restriction_count": restrictions, "deprecated": deprecated in {"true", "1"}}
    for term in terms.values():
        if any(parent not in terms for parent in term["parents"]):
            raise ValueError("named parent missing from ontology")
    metadata = list(graph.subjects(RDF.type, OWL.Ontology))
    if len(metadata) != 1:
        raise ValueError("missing ontology metadata")
    date = graph.value(metadata[0], URIRef(NS["oboInOwl"] + "date"))
    return terms, edges, str(date) if date is not None else None


def shortest_path(terms, start, target):
    todo, seen = deque([(start,)]), set()
    while todo:
        path = todo.popleft()
        node = path[-1]
        if node == target:
            return list(path)
        if node in seen:
            continue
        seen.add(node)
        todo.extend((*path, parent) for parent in terms[node]["parents"])
    return None


def term_scope(terms, tid, child_count):
    todo, seen = [tid], set()
    while todo:
        node = todo.pop()
        if node in seen:
            continue
        seen.add(node)
        if terms[node]["external_parents"]:
            raise ValueError("selected term ancestry leaves the supported ARO graph")
        todo.extend(terms[node]["parents"])
    paths = {anchor: shortest_path(terms, tid, anchor) for anchor in ANCHORS}
    matches = [ENTITY_SCOPES[a] for a in ENTITY_SCOPES if paths[a] is not None]
    scope = (matches[0] if len(matches) == 1 else "MULTIPLE_ENTITY_SCOPES_REQUIRE_REVIEW" if matches
             else "OTHER_TERM_ENTITY_GRANULARITY_UNRESOLVED")
    return {
        "entity_scope": scope, "named_parent_ids": terms[tid]["parents"],
        "anchor_paths": paths, "named_direct_subclass_count": child_count,
        "deprecated": terms[tid]["deprecated"],
    }


def pin(root, path):
    return {"path": str(path.relative_to(root)), "sha256": common.digest(path.read_bytes())}


def analyze(root, cache, audit_path, ledger_path, only=None):
    before = cache.read_bytes()
    raw = json.loads(before)
    body = raw["body"].encode()
    source_match = re.fullmatch(
        r"https://raw\.githubusercontent\.com/arpcard/aro/([0-9a-f]{40})/aro\.owl", raw["url"])
    if (raw["status"] != 200 or common.digest(body) != raw["sha256"] or len(body) != raw["bytes"]
            or source_match is None):
        raise ValueError("ontology cache identity or checksum mismatch")
    terms, edges, ontology_date = parse_ontology(body)
    if any(terms.get(t, {}).get("label") != label for t, label in ANCHORS.items()):
        raise ValueError("ontology anchor identity drift")
    inventory_path = root / card.SOURCE
    input_paths = (audit_path, ledger_path, inventory_path, common.OUT / "corpus.json")
    inputs = {p: p.read_bytes() for p in input_paths}
    audit = json.loads(inputs[audit_path])
    if common.digest(inventory_path.read_bytes()) != audit["source_inventory_sha256"]:
        raise ValueError("source inventory differs from reference audit")
    with inventory_path.open() as handle:
        inventory = list(csv.DictReader(handle, delimiter="\t"))
    for row in inventory:
        key = (row["determinant_id"], row["relation"], row["antibiotic_id"])
        if key not in edges:
            raise ValueError(f"source resistance edge missing from ontology: {key}")
        if terms[key[0]]["label"] != row["determinant_name"]:
            raise ValueError("source determinant label differs from ontology")
    records = card.current_corpus(root)
    claims = card.claims_from(records)
    expected = Counter((r["identifier"], c["aro_id"], c["label"]) for r, c in claims)
    with ledger_path.open() as handle:
        ledger = list(csv.DictReader(handle, delimiter="\t"))
    if Counter((r["identifier"], r["aro_id"], r["determinant_label"]) for r in ledger) != expected:
        raise ValueError("current CARD membership differs from pinned ledger")
    labels = defaultdict(set)
    for _, claim in claims:
        labels[claim["aro_id"]].add(claim["label"])
    if set(labels) != set(audit["determinants"]):
        raise ValueError("reference audit determinant membership drift")
    for tid, names in labels.items():
        if (tid not in terms or sorted(names) != audit["determinants"][tid]["labels"]
                or sorted(names) != [terms[tid]["label"]] or terms[tid]["deprecated"]):
            raise ValueError("current determinant identity differs from ontology or audit")
    selected = set(labels) if only is None else set(only)
    if not selected or not selected <= set(labels):
        raise ValueError("invalid term selection")
    children = Counter(p for term in terms.values() for p in term["parents"])
    classified = {}
    for tid in sorted(selected):
        row = audit["determinants"][tid]
        classified[tid] = {
            **term_scope(terms, tid, children[tid]),
            "reference_link_status": row["status"],
            "reference_candidate_accessions": sorted(c["accession"] for c in row["candidates"]),
            "primary_review_status": row["primary_review_status"],
        }
    selected_claims = [(r, c) for r, c in claims if c["aro_id"] in selected]
    unlinked = {t: d for t, d in classified.items()
                if d["reference_link_status"] == "NO_EXPLICIT_LINK_IN_THIS_RELEASE"}
    result = {
        "scope": SCOPE, "selection": "ALL_EXISTING_CARD_TERMS" if only is None else "CANARY_ONLY",
        "ontology": {k: raw[k] for k in ("url", "status", "sha256", "bytes", "retrieved_at")},
        "ontology_cache": pin(root, cache), "ontology_date": ontology_date,
        "reference_audit": pin(root, audit_path), "reference_ledger": pin(root, ledger_path),
        "source_inventory": pin(root, inventory_path),
        "current_corpus": pin(root, common.OUT / "corpus.json"),
        "reference_release": audit["summary"]["release"], "anchors": ANCHORS, "terms": classified,
        "summary": {
            "corpus_records": len(records), "selected_terms": len(classified),
            "selected_card_assertions": len(selected_claims),
            "selected_card_records": len({r["identifier"] for r, _ in selected_claims}),
            "source_inventory_edges_verified": len(inventory),
            "entity_scope_counts": dict(Counter(d["entity_scope"] for d in classified.values())),
            "unlinked_terms": len(unlinked),
            "unlinked_entity_scope_counts": dict(Counter(d["entity_scope"] for d in unlinked.values())),
            "assertion_entity_scope_counts": dict(Counter(
                classified[c["aro_id"]]["entity_scope"] for _, c in selected_claims)),
            "unlinked_terms_with_named_subclasses": sum(d["named_direct_subclass_count"] > 0
                                                       for d in unlinked.values()),
            "unlinked_variant_ancestor_terms": sum(d["anchor_paths"]["ARO:0000031"] is not None
                                                   for d in unlinked.values()),
            "outside_determinant_ancestry": [t for t, d in classified.items()
                                             if d["anchor_paths"]["ARO:3000000"] is None],
        },
        "attribution": {"source": "CARD curation team, Antibiotic Resistance Ontology; UniProt Consortium",
                        "ontology_license": "CC-BY-4.0", "ontology_license_url":
                        f"https://github.com/arpcard/aro/blob/{source_match.group(1)}/LICENSE"},
        "limitations": [
            "Only explicit named ARO rdfs:subClassOf paths are traversed; OWL restrictions are not ancestry.",
            "External named parents are retained during parsing and rejected if reached by a selected term; "
            "no ontology import is fetched.",
            "The OWL file is a separate pinned serialization, "
            "not claimed byte-identical to the historical OBO.",
            "RNA determinants are not protein products; gene clusters are not single protein accessions.",
            "The efflux anchor includes both complexes and subunits; "
            "it does not identify which a term denotes.",
            "Named subclasses flag ontology granularity, not a verified gene family or an exact allele.",
            "No child reference accession is propagated to its ancestor, and no representative is selected.",
            "Variant-category ancestry does not identify a tested variant, "
            "protein accession or reference sequence.",
            "Missing determinant ancestry is an ontology-review flag, "
            "not evidence that resistance is absent.",
            "All prior reference candidates and pending primary-review statuses remain unchanged.",
            "Ledger record hashes are historical; "
            "current corpus hashes independently verify current records.",
            "No source adoption, source-inventory mutation, biological curation or curation event occurred.",
            "No NCBI request, card.json request, sequence, "
            "variant specification or numeric phenotype is added.",
            "This classification does not complete primary evidence review or the full-corpus investigation.",
        ],
    }
    if cache.read_bytes() != before:
        raise ValueError("ontology cache changed during analysis")
    if any(path.read_bytes() != payload for path, payload in inputs.items()):
        raise ValueError("grounding input changed during analysis")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--ontology-cache", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--only", action="append")
    args = parser.parse_args()
    root = args.root.resolve()
    common.OUT = root / "reports/resistance-grounding-2026-10-07"
    result = analyze(root, args.ontology_cache.resolve(),
                     root / "research/2026-10-07-card-reference-grounding.json",
                     root / "research/2026-10-07-card-reference-ledger.tsv", args.only)
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.output.exists():
        if args.output.read_bytes() != payload:
            raise ValueError("refusing to overwrite a different existing audit")
    else:
        args.output.write_bytes(payload)
    print(json.dumps(result["summary"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
