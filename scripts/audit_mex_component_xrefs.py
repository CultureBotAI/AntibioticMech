"""Replay five unresolved Mex component cross-references, offline and reference-only."""

import argparse
import hashlib
import json
import re
from pathlib import Path

import audit_card_definition_citations as definitions
import audit_card_grounding as card
import audit_card_reference_lineages as lineages
import audit_mex_jkvw_evidence as prior_audit
from rdflib import OWL, RDF, RDFS, BNode, Graph, URIRef

mex = prior_audit.followup.mex
reference, require = prior_audit.reference, prior_audit.require
PREFIX = "research/2026-10-15-mex-component-xrefs"
PLAN = Path(PREFIX + "-plan.json")
OUTPUT = Path(PREFIX + ".json")
SCOPE = "MEX_COMPONENT_CARD_XREFS_NOT_COMPLEX_OR_EXPERIMENTAL_IDENTITIES"
LABELS = {
    "ARO:3003030": "MexV",
    "ARO:3003031": "MexW",
    "ARO:3003682": "OpmH",
    "ARO:3003692": "MexJ",
    "ARO:3003693": "MexK",
}
BASE = definitions.ontology.BASE
SELECTED_COMPLEXES = {"ARO:3003029", "ARO:3003691", "ARO:3003694", "ARO:3009148"}
ROLE_IRIS = {BASE + "2000002", BASE + "2000004"}


def native_page(receipt, params, release, total):
    card.common.validate_cached_response(receipt, "https://rest.uniprot.org/uniprotkb/search", params)
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    require(
        headers["x-uniprot-release"] == release
        and int(headers["x-total-results"]) == total
        and not headers.get("location"),
        "native page release, total or redirect changed",
    )
    payload = json.loads(receipt["body"])
    require(set(payload) == {"results"}, "unexpected native search payload")
    entries = payload["results"]
    accessions = [e["primaryAccession"] for e in entries]
    require(
        0 < len(entries) <= int(card.PARAMS["size"])
        and len(accessions) == len(set(accessions))
        and accessions == sorted(accessions),
        "empty, duplicate, unordered or oversized native page",
    )
    require(
        all(not {"sequence", "features"} & set(e) for e in entries)
        and all(any(x["database"] == "CARD" for x in e.get("uniProtKBCrossReferences", [])) for e in entries),
        "unexpected operational fields or missing CARD cross-reference",
    )
    return entries, card.next_page(headers.get("link", ""), card.PARAMS)


def replay_proteins(root, plan, snapshot):
    require(
        snapshot["query"] == card.PARAMS
        and snapshot["release"] == mex.RELEASE
        and snapshot["total"] == 4182
        and snapshot["source_inventory_sha256"] == plan["inputs"]["source_inventory"]["sha256"]
        and len(plan["native_protein_pages"]) == len(snapshot["requests"]) == 9,
        "frozen CARD cross-reference cohort changed",
    )
    params, entries, sources = dict(card.PARAMS), {}, []
    for item, expected in zip(plan["native_protein_pages"], snapshot["requests"], strict=True):
        require(params is not None, "extra native page after terminal cursor")
        receipt = mex.read_json(root, item)
        require(card.metadata(receipt) == expected, "aggregate request differs from native page")
        page, params = native_page(receipt, params, snapshot["release"], snapshot["total"])
        for entry in page:
            accession = entry["primaryAccession"]
            require(accession not in entries, "duplicate protein across native pages")
            entries[accession] = entry
        sources.append({"receipt": item, **expected})
    require(
        params is None
        and len(entries) == snapshot["total"]
        and list(entries) == sorted(entries)
        and entries == snapshot["entries"],
        "incomplete, unordered or altered aggregate protein snapshot",
    )
    return entries, sources


def one_label(graph, node):
    values = list(graph.objects(node, RDFS.label))
    require(len(values) == 1, "ambiguous or missing ontology label")
    return str(values[0])


def component_graph(graph):
    annotations = definitions.project_annotations(graph, LABELS)
    components = {}
    for tid, label in LABELS.items():
        node = URIRef(BASE + tid.split(":")[1])
        parents, edges = [], []
        for parent in graph.objects(node, RDFS.subClassOf):
            if isinstance(parent, URIRef):
                parents.append({"iri": str(parent), "label": one_label(graph, parent)})
                continue
            require(
                isinstance(parent, BNode) and (parent, RDF.type, OWL.Restriction) in graph,
                "unsupported anonymous superclass",
            )
            properties = list(graph.objects(parent, OWL.onProperty))
            targets = list(graph.objects(parent, OWL.someValuesFrom))
            require(
                len(properties) == len(targets) == 1
                and isinstance(properties[0], URIRef)
                and isinstance(targets[0], URIRef)
                and str(targets[0]).startswith(BASE)
                and set(graph.predicates(parent)) == {RDF.type, OWL.onProperty, OWL.someValuesFrom},
                "ambiguous or unsupported component restriction",
            )
            prop, target = properties[0], targets[0]
            target_id = "ARO:" + str(target).removeprefix(BASE)
            edges.append(
                {
                    "property_iri": str(prop),
                    "property_label": one_label(graph, prop),
                    "target_aro": target_id,
                    "target_label": one_label(graph, target),
                    "target_in_selected_record_cohort": target_id in SELECTED_COMPLEXES,
                    "assertion_kind": "RDFS_SUBCLASS_OF_OWL_SOME_VALUES_FROM_RESTRICTION",
                    "source_assertion_not_verified_biological_composition": True,
                }
            )
        components[tid] = {
            "label": label,
            "definition_annotations": annotations[tid],
            "named_superclasses": sorted(parents, key=lambda row: row["iri"]),
            "component_relations": sorted(edges, key=lambda row: (row["target_aro"], row["property_iri"])),
        }
    return components


def role_conflicts(components):
    result = []
    for tid, component in sorted(components.items()):
        edges = [
            r
            for r in component["component_relations"]
            if r["property_iri"] in ROLE_IRIS and r["target_in_selected_record_cohort"]
        ]
        if len({r["property_iri"] for r in edges}) > 1:
            result.append(
                {
                    "component_aro": tid,
                    "component_label": component["label"],
                    "relations": edges,
                    "status": "OPEN_SOURCE_ROLE_INCONSISTENCY",
                    "biological_correction_independently_established": False,
                    "propagate_a_role_across_contexts": False,
                }
            )
    return result


def project_candidate(entry, crossref, taxon, component_label):
    taxid = str(entry["organism"]["taxonId"])
    require(
        taxid == str(taxon["taxonId"]) and entry["organism"]["scientificName"] == taxon["scientificName"],
        "reference protein and taxonomy disagree",
    )
    nodes, species = lineages.lineage(taxon)
    symbols = sorted({g["geneName"]["value"] for g in entry.get("genes", []) if "geneName" in g})
    props = crossref.get("properties", [])
    require(
        crossref["database"] == "CARD"
        and LABELS.get(crossref["id"]) == component_label
        and len({p["key"] for p in props}) == len(props)
        and {p["key"]: p["value"] for p in props}.get("CARD short name") == component_label,
        "ambiguous or changed native CARD short name",
    )
    compatible = species is not None and species["taxonId"] == 287
    return {
        "uniprot_id": "UniProtKB:" + entry["primaryAccession"],
        "entry_type": entry["entryType"],
        "entry_audit": entry["entryAudit"],
        "native_entry_sha256": mex.checksum(entry),
        "card_cross_reference": crossref,
        "native_gene_symbols": symbols,
        "native_ordered_locus_names": sorted(
            {v["value"] for g in entry.get("genes", []) for v in g.get("orderedLocusNames", [])}
        ),
        "native_orf_names": sorted(
            {v["value"] for g in entry.get("genes", []) for v in g.get("orfNames", [])}
        ),
        "gene_name_comparison": "NO_NATIVE_GENE_SYMBOL"
        if not symbols
        else (
            "EXACT_TEXT_MATCH_NOT_IDENTITY_PROOF"
            if component_label in symbols
            else "NATIVE_SYMBOL_DIFFERS_FROM_CARD_COMPONENT_LABEL"
        ),
        "reference_taxon_id": "NCBITaxon:" + taxid,
        "reference_taxon_name": taxon["scientificName"],
        "reference_taxon_rank": taxon["rank"],
        "reference_taxon_active": True,
        "reference_species": species,
        "species_to_reference_path": nodes[nodes.index(species) :] if species else [],
        "disposition": "REFERENCE_SPECIES_COMPATIBLE_NOT_EXPERIMENTAL_IDENTITY"
        if compatible
        else "WITHHELD_FROM_P_AERUGINOSA_CONTEXT_DIFFERENT_REFERENCE_SPECIES",
        "native_citation_contexts": card.reference_contexts(entry),
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
        "whole_complex_identity_assignment": False,
        "curation_supported_by_this_pass": False,
    }


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["component_labels"] == LABELS
        and plan["selection"] == "FIVE_UNRESOLVED_MEXJK_MEXVW_COMPONENT_SYMBOLS"
        and plan["limits"]
        == {
            "network_requests": 0,
            "biological_record_writes": False,
            "operational_exports": False,
            "issue_1040": "DEFERRED",
        },
        "selected offline scope changed",
    )
    prior = mex.read_json(root, plan["prior"])
    require(prior_audit.build(root) == prior, "prior native replay or current corpus changed")
    require(set(prior["terms"]) == SELECTED_COMPLEXES, "selected parent contexts changed")
    inputs = {
        k: mex.read_json(root, p)
        for k, p in plan["inputs"].items()
        if k not in {"source_inventory", "source_queue"}
    }
    for key in ("source_inventory", "source_queue"):
        reference.check_pin(root, plan["inputs"][key])
    cached = inputs["ontology"]
    body = cached["body"].encode()
    require(
        cached["status"] == 200
        and hashlib.sha256(body).hexdigest() == cached["sha256"]
        and len(body) == cached["bytes"]
        and re.fullmatch(
            r"https://raw\.githubusercontent\.com/arpcard/aro/[0-9a-f]{40}/aro\.owl", cached["url"]
        ),
        "ontology identity or content changed",
    )
    graph = Graph().parse(data=body, format="xml")
    components = component_graph(graph)
    dates = list(map(str, graph.objects(None, URIRef(definitions.ontology.NS["oboInOwl"] + "date"))))
    require(dates == ["12:08:2026 11:14"], "ontology release date changed")
    for tid, term in prior["terms"].items():
        require(one_label(graph, URIRef(BASE + tid[4:])) == term["complex_label"], "parent label changed")
    entries, native_pages = replay_proteins(root, plan, inputs["proteins"])
    require(
        inputs["taxonomy"]["proteins_sha256"] == plan["inputs"]["proteins"]["sha256"],
        "taxonomy snapshot bound to different proteins",
    )
    index = card.reference_index(entries, LABELS)
    taxids = {str(e["organism"]["taxonId"]) for matches in index.values() for e, _ in matches}
    require(taxids == set(plan["native_taxonomy"]), "selected reference taxonomy coverage changed")
    taxa, taxonomy_sources = {}, {}
    for taxid, pin in plan["native_taxonomy"].items():
        taxa[taxid], taxonomy_sources[taxid] = lineages.native_taxon(root, pin, taxid, mex.RELEASE)
        require(taxa[taxid] == inputs["taxonomy"]["taxa"][taxid], "aggregate taxonomy differs from native")
    candidates = {}
    for tid, component in components.items():
        component["reference_candidates"] = []
        for entry, xref in index.get(tid, []):
            projected = project_candidate(entry, xref, taxa[str(entry["organism"]["taxonId"])], LABELS[tid])
            accession = projected["uniprot_id"]
            require(
                accession not in candidates, "candidate shared across selected components; review required"
            )
            candidates[accession] = projected
            component["reference_candidates"].append(accession)
    require(
        len(candidates) == 5 and all(len(c["reference_candidates"]) == 1 for c in components.values()),
        "bounded component cross-reference coverage changed",
    )
    require(not set(candidates) & set(inputs["broad_index"]["proteins"]), "references already in broad index")
    conflicts = role_conflicts(components)
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "inputs": plan["inputs"],
        "prior": plan["prior"],
        "ontology_source": {k: cached[k] for k in ("url", "sha256", "retrieved_at")},
        "ontology_date": dates[0],
        "release": mex.RELEASE,
        "native_protein_pages": native_pages,
        "taxonomy_sources": taxonomy_sources,
        "components": components,
        "reference_candidates": candidates,
        "role_conflicts": conflicts,
        "terms": prior["terms"],
        "claims": prior["claims"],
        "records": prior["records"],
        "publication_access_status_in_prior_unchanged": True,
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read_in_prior_replay": 27,
            "selected_terms": 4,
            "selected_claims": 8,
            "selected_records": 5,
            "component_terms": len(components),
            "native_card_entries_replayed": len(entries),
            "native_pages_replayed": len(native_pages),
            "component_reference_candidates": len(candidates),
            "species_compatible_reference_candidates": sum(
                p["reference_species"]["taxonId"] == 287 for p in candidates.values()
            ),
            "different_species_candidates_withheld": sum(
                p["reference_species"]["taxonId"] != 287 for p in candidates.values()
            ),
            "component_role_conflicts": len(conflicts),
            "new_network_requests": 0,
        },
        "limits": {
            **mex.LIMITS,
            "prior_primary_access_holds_preserved": True,
            "new_taxonomy_requests": 0,
            "new_uniprot_requests": 0,
            "exact_variant_or_operational_exports": False,
            "source_role_correction_established": False,
            "component_term_is_not_parent_complex_identity": True,
        },
        "attribution": "CARD/ARO and UniProt release 2026_03, CC BY 4.0; reference metadata only.",
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
