"""Ground explicit CARD members without assigning a protein to a complex or an experimental allele."""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import audit_card_protein_name_screen as screen
import audit_mex_component_xrefs as prior
from rdflib import OWL, RDF, RDFS, BNode, Graph, URIRef

from antibioticmech.activity_collections import load_record

reference, require = prior.reference, prior.require
PREFIX = "research/2026-10-15-card-complex-members"
PLAN = Path(PREFIX + "-plan.json")
OUTPUT = Path(PREFIX + ".json")
BASE = prior.BASE
SCOPE = "EXPLICIT_ONTOLOGY_MEMBER_REFERENCE_GROUNDING_NOT_COMPLEX_OR_EXPERIMENTAL_IDENTITY"
PART_OF = "http://purl.obolibrary.org/obo/BFO_0000050"
RELATIONS = {
    PART_OF: "part_of",
    BASE + "2000002": "inner_membrane_protein_of",
    BASE + "2000003": "outer_membrane_protein_of",
    BASE + "2000004": "periplasmic_adaptor_protein_of",
}


def source_members(graph, targets):
    """Only direct, explicitly typed membership restrictions; never subclass or regulator propagation."""
    members, excluded = [], Counter()
    for node, restriction in graph.subject_objects(RDFS.subClassOf):
        if not isinstance(node, URIRef) or not isinstance(restriction, BNode):
            continue
        if (restriction, RDF.type, OWL.Restriction) not in graph:
            continue
        properties = list(graph.objects(restriction, OWL.onProperty))
        objects = list(graph.objects(restriction, OWL.someValuesFrom))
        selected = [
            obj
            for obj in objects
            if isinstance(obj, URIRef)
            and str(obj).startswith(BASE)
            and "ARO:" + str(obj)[len(BASE) :] in targets
        ]
        if not selected:
            continue
        require(len(properties) == len(objects) == 1, "ambiguous source restriction")
        prop, target = str(properties[0]), "ARO:" + str(selected[0])[len(BASE) :]
        if prop not in RELATIONS:
            excluded[prop] += 1
            continue
        require(
            str(node).startswith(BASE)
            and isinstance(properties[0], URIRef)
            and set(graph.objects(restriction, RDF.type)) == {OWL.Restriction}
            and set(graph.predicates(restriction)) == {RDF.type, OWL.onProperty, OWL.someValuesFrom}
            and prior.one_label(graph, properties[0]) == RELATIONS[prop],
            "unsupported membership restriction or property label changed",
        )
        require(prior.one_label(graph, selected[0]) == targets[target], "source parent identity changed")
        members.append(
            {
                "member_aro": "ARO:" + str(node)[len(BASE) :],
                "member_label": prior.one_label(graph, node),
                "parent_aro": target,
                "property_iri": prop,
                "property_label": RELATIONS[prop],
                "assertion_kind": "DIRECT_RDFS_SUBCLASS_OF_OWL_SOME_VALUES_FROM",
                "biological_composition_independently_verified": False,
            }
        )
    keys = [(r["parent_aro"], r["member_aro"], r["property_iri"]) for r in members]
    require(len(keys) == len(set(keys)), "duplicate membership assertion")
    return sorted(members, key=lambda r: (r["parent_aro"], r["member_aro"], r["property_iri"])), dict(
        sorted(excluded.items())
    )


def current_context(root, index, update, selected, labels):
    census_path = reference.check_pin(root, index["inputs"]["census"])
    with census_path.open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    deltas = {r["path"]: r for r in update["record_deltas"]}
    require(len(deltas) == len(update["record_deltas"]) == 3, "qualification delta coverage changed")
    paths = {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
    require(
        len(census) == len({r["identifier"] for r in census}) == len(paths) == 2939
        and paths == {r["path"] for r in census}
        and set(deltas) <= paths,
        "corpus membership drift",
    )
    records = []
    ids = {rid for tid in selected for rid in index["terms"][tid]["record_memberships"]}
    claims = [c for c in index["claims"] if c["aro_id"] in selected]
    actual = []
    for row in census:
        expected = row["record_sha256"]
        if row["path"] in deltas:
            delta = deltas[row["path"]]
            require(
                delta["before_sha256"] == expected and delta["identifier"] == row["identifier"],
                "qualification record binding changed",
            )
            expected = delta["after_sha256"]
        require(reference.digest(root / row["path"]) == expected, "current corpus bytes changed")
        if row["identifier"] not in ids:
            continue
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "complete record identity changed",
        )
        records.append({**row, "record_sha256": expected})
        for position, claim in screen.selected_claims(doc, selected):
            require(claim["label"] == labels[claim["aro_id"]], "source claim label drift")
            actual.append((row["identifier"], position, claim["aro_id"], screen.checksum(claim)))
    require(
        sorted(actual)
        == sorted(
            (c["record_identifier"], c["resistance_index"], c["aro_id"], c["claim_sha256"]) for c in claims
        ),
        "source claim drift",
    )
    for tid in selected:
        require(
            sorted({rid for rid, _, term, _ in actual if term == tid})
            == index["terms"][tid]["record_memberships"],
            "parent record membership changed",
        )
    hashes = {r["identifier"]: r["record_sha256"] for r in records}
    return records, [{**c, "record_sha256": hashes[c["record_identifier"]]} for c in claims]


def member_reference(entry, taxon):
    result = screen.project_reference(entry, taxon, allow_taxon_name_difference=True)
    result["ordered_locus_names"] = sorted(
        {v["value"] for g in entry.get("genes", []) for v in g.get("orderedLocusNames", [])}
    )
    result["orf_names"] = sorted({v["value"] for g in entry.get("genes", []) for v in g.get("orfNames", [])})
    result["reference_taxonomy"]["active"] = True
    result["reference_taxonomy"]["label_flags"] = prior.lineages.label_flags(taxon["scientificName"])
    if "metagenome" in taxon["scientificName"].casefold():
        result["reference_taxonomy"]["label_flags"].append("METAGENOME_LABEL_NOT_INDIVIDUAL_ORGANISM")
    result["reference_taxonomy"]["native_species_rank_establishes_individual_organism"] = False
    result["reference_taxonomy"]["lineage_species_is_experimental_subject"] = False
    result["whole_complex_identity_assignment"] = False
    return result


def request_provenance(root, plan):
    frozen = prior.mex.read_json(root, plan["request_plan"])
    inspected = prior.mex.read_json(root, plan["taxonomy_canary_inspected"])
    missing = frozen["missing_taxonomy"]
    require(
        bool(missing)
        and type(plan["new_taxonomy_requests"]) is int
        and len(missing) == len(set(missing)) == plan["new_taxonomy_requests"]
        and missing == plan["missing_taxonomy"]
        and plan["planned_taxonomy_urls"] == frozen["planned_taxonomy_urls"]
        and set(missing) == set(frozen["planned_taxonomy_urls"])
        and not set(missing) & set(frozen["native_taxonomy"])
        and set(plan["native_taxonomy"]) == set(missing) | set(frozen["native_taxonomy"])
        and plan["remaining_missing_taxonomy"] == []
        and all(plan[k] == frozen[k] == 0 for k in ("ncbi_requests", "retries", "redirects_followed")),
        "planned request accounting changed",
    )
    for taxid, item in frozen["native_taxonomy"].items():
        require(plan["native_taxonomy"][taxid] == item, "cached taxonomy replaced")
    directory = (root / plan["request_plan"]["path"]).parent
    expected_attempts = {directory / f"taxonomy-{t}-attempt.json" for t in missing}
    require(
        set(directory.glob("taxonomy-*-attempt.json")) == expected_attempts
        and not list(directory.glob("taxonomy-*-error.json")),
        "unaccounted taxonomy request or failure",
    )
    sources = {}
    for taxid in missing:
        url = f"https://rest.uniprot.org/taxonomy/{taxid}.json"
        attempt_path = directory / f"taxonomy-{taxid}-attempt.json"
        attempt = json.loads(attempt_path.read_bytes())
        item = plan["native_taxonomy"][taxid]
        receipt = prior.mex.read_json(root, item["receipt"])
        require(
            frozen["planned_taxonomy_urls"][taxid] == attempt["url"] == receipt["url"] == url
            and attempt["request_plan"] == plan["request_plan"]
            and receipt["status"] == 200
            and receipt["retries"] == receipt["redirects_followed"] == 0
            and receipt["bytes"] == len(receipt["body"].encode())
            and item["body"] is None,
            "native taxonomy request differs from plan",
        )
        sources[taxid] = {"attempt": reference.pin(root, attempt_path), "response": item}
    require(
        inspected["accepted"] is True
        and str(inspected["taxon_id"]) == missing[0]
        and inspected["source"]["receipt"] == plan["native_taxonomy"][missing[0]]["receipt"],
        "taxonomy canary binding changed",
    )
    return sources


def parent_projection(term, edges, proteins):
    accessions = sorted({a for edge in edges for a in edge["reference_candidates"]})
    taxids = sorted({proteins[a]["reference_taxonomy"]["taxon_id"] for a in accessions})
    species = sorted(
        {
            "NCBITaxon:" + str(proteins[a]["reference_taxonomy"]["species"]["taxonId"])
            for a in accessions
            if proteins[a]["reference_taxonomy"]["species"]
        }
    )
    return {
        "source_label": term["label"],
        "source_label_sha256": term["source_label_sha256"],
        "record_memberships": term["record_memberships"],
        "prior_direct_reference_status": term["reference_status"],
        "member_edges": edges,
        "reference_accessions": accessions,
        "distinct_reference_taxa": taxids,
        "distinct_reference_species_rank_nodes": species,
        "multiple_reference_taxa_not_one_experimental_background": len(taxids) > 1,
        "missing_component_reference_is_biological_absence": False,
        "all_member_terms_have_native_xref_candidates": all(e["reference_candidates"] for e in edges),
        "complete_biological_membership_established": False,
        "reference_candidates_are_independently_validated_components": False,
        "parent_protein_accession_assignment": None,
        "experimental_taxon_assignment": None,
        "exact_allele_assignment": False,
        "primary_review": "OPEN",
    }


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["relations"] == RELATIONS
        and plan["selection"] == "ALL_2002_SOURCE_DETERMINANTS_EXPLICIT_INCOMING_MEMBERSHIP",
        "audit scope changed",
    )
    requests = request_provenance(root, plan)
    source_plan = prior.mex.read_json(root, plan["native_source_plan"])
    index = prior.mex.read_json(root, plan["inputs"]["index"])
    require(plan["inputs"]["index"] == source_plan["inputs"]["broad_index"], "broad index differs")
    inventory = reference.check_pin(root, index["inputs"]["source_inventory"])
    reference.check_pin(root, index["inputs"]["source_queue"])
    with inventory.open() as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    label_sets = defaultdict(set)
    for row in rows:
        label_sets[row["determinant_id"]].add(row["determinant_name"])
    require(all(len(names) == 1 for names in label_sets.values()), "source determinant label ambiguity")
    labels = {tid: next(iter(label_sets[tid])) for tid in index["terms"]}
    require(
        len(labels) == 2002
        and all(
            hashlib.sha256(labels[t].encode()).hexdigest() == r["source_label_sha256"]
            for t, r in index["terms"].items()
        ),
        "determinant identity changed",
    )
    cached = prior.mex.read_json(root, source_plan["inputs"]["ontology"])
    body = cached["body"].encode()
    require(
        cached["status"] == 200
        and hashlib.sha256(body).hexdigest() == cached["sha256"]
        and len(body) == cached["bytes"]
        and re.fullmatch(
            r"https://raw\.githubusercontent\.com/arpcard/aro/[0-9a-f]{40}/aro\.owl", cached["url"]
        ),
        "ontology content or identity changed",
    )
    graph = Graph().parse(data=body, format="xml")
    edges, excluded = source_members(graph, labels)
    member_labels = {e["member_aro"]: e["member_label"] for e in edges}
    selected = {e["parent_aro"] for e in edges}
    require(
        sorted(selected) == plan["parent_terms"] and member_labels == plan["member_terms"],
        "complete parent or member selection changed",
    )
    annotations = prior.definitions.project_annotations(
        graph, {**member_labels, **{t: labels[t] for t in selected}}
    )
    snapshot = prior.mex.read_json(root, source_plan["inputs"]["proteins"])
    entries, native_pages = prior.replay_proteins(root, source_plan, snapshot)
    matches = prior.card.reference_index(entries, member_labels)
    accessions = {e["primaryAccession"] for candidates in matches.values() for e, _ in candidates}
    taxids = {str(entries[a]["organism"]["taxonId"]) for a in accessions}
    require(taxids == set(plan["native_taxonomy"]), "reference taxonomy coverage changed")
    taxa, tax_sources = {}, {}
    for taxid, item in sorted(plan["native_taxonomy"].items()):
        taxa[taxid], tax_sources[taxid] = prior.lineages.native_taxon(root, item, taxid, snapshot["release"])
    prior.lineages.project_taxa(taxa, tax_sources, {}, {})
    proteins = {
        "UniProtKB:" + a: member_reference(entries[a], taxa[str(entries[a]["organism"]["taxonId"])])
        for a in sorted(accessions)
    }
    by_parent = defaultdict(list)
    for edge in edges:
        tid = edge["member_aro"]
        xrefs = [
            {"accession": "UniProtKB:" + entry["primaryAccession"], "native_cross_reference": xref}
            for entry, xref in matches.get(tid, [])
        ]
        by_parent[edge["parent_aro"]].append(
            {
                **edge,
                "native_xref_bindings": xrefs,
                "reference_candidates": sorted({x["accession"] for x in xrefs}),
                "experimental_identity_assigned": False,
            }
        )
    parents = {
        tid: parent_projection({"label": labels[tid], **index["terms"][tid]}, by_parent[tid], proteins)
        for tid in sorted(selected)
    }
    update = prior.mex.read_json(root, plan["inputs"]["corpus_update"])
    records, claims = current_context(root, index, update, selected, labels)
    variations = {}
    for member in member_labels:
        role_edges = [e for e in edges if e["member_aro"] == member and e["property_iri"] != PART_OF]
        if len({e["property_iri"] for e in role_edges}) > 1:
            variations[member] = {
                "source_role_edges": role_edges,
                "biological_error_independently_proven": False,
                "propagate_one_role_across_contexts": False,
            }
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "inputs": plan["inputs"],
        "native_source_plan": plan["native_source_plan"],
        "ontology_source": {k: cached[k] for k in ("url", "sha256", "retrieved_at")},
        "native_protein_pages": native_pages,
        "release": snapshot["release"],
        "taxonomy_sources": tax_sources,
        "new_taxonomy_requests": requests,
        "annotations": annotations,
        "parents": parents,
        "reference_proteins": proteins,
        "source_role_variations": variations,
        "excluded_relation_counts": excluded,
        "records": records,
        "claims": claims,
        "coverage": {
            t: {"explicit_member_edges": len(by_parent.get(t, [])), "no_edges_is_biological_absence": False}
            for t in sorted(labels)
        },
        "summary": {
            "source_determinants_screened": len(labels),
            "parent_terms": len(parents),
            "member_terms": len(member_labels),
            "direct_member_edges": len(edges),
            "native_member_reference_proteins": len(proteins),
            "reference_taxa": len(taxa),
            "reference_taxa_with_metagenome_labels": sum(
                "metagenome" in t["scientificName"].casefold() for t in taxa.values()
            ),
            "reference_proteins_with_taxonomy_name_disagreement": sum(
                p["taxonomy_name_comparison"] != "EXACT_NATIVE_SCIENTIFIC_NAME_AGREEMENT"
                for p in proteins.values()
            ),
            "reference_proteins_not_in_broad_index": len(set(proteins) - set(index["proteins"])),
            "members_with_native_reference_candidates": len(matches),
            "parents_with_all_members_matched": sum(
                p["all_member_terms_have_native_xref_candidates"] for p in parents.values()
            ),
            "parents_with_multiple_reference_taxa": sum(
                p["multiple_reference_taxa_not_one_experimental_background"] for p in parents.values()
            ),
            "source_role_variations": len(variations),
            "source_claims": len(claims),
            "complete_records_read": len(records),
            "corpus_records_hash_checked": 2939,
            "native_protein_entries_replayed": len(entries),
            "native_protein_pages_replayed": len(native_pages),
            "new_network_requests": plan["new_taxonomy_requests"],
        },
        "limits": {
            **prior.mex.LIMITS,
            "new_taxonomy_requests": plan["new_taxonomy_requests"],
            "component_reference_grounding_is_not_whole_complex_grounding": True,
            "regulators_inhibitors_variants_and_subclasses_propagated_as_members": False,
            "primary_access_holds_preserved": True,
            "sequences_or_operational_details_exported": False,
        },
        "attribution": (
            "CARD/ARO and UniProt2026_03 metadata, CC BY 4.0; source assertions, not primary experiments."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    output = args.root / args.output
    if args.check or output.exists():
        require(
            output.read_bytes() == payload, "member audit does not reproduce; preserve the historical output"
        )
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
