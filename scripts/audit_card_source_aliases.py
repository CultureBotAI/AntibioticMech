"""Replay explicit ontology aliases against cached reference metadata, offline."""

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

import audit_card_definition_citations as definitions
import audit_card_gene_reference_followup as prior
import audit_card_literature_expansion as literature
from rdflib import Graph, Literal, URIRef

reference, require, read_json = prior.reference, prior.require, prior.read_json
PREFIX = "research/2026-10-15-card-source-aliases"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
SCOPE = "EXPLICIT_ONTOLOGY_ALIAS_REFERENCE_CONTEXT_NOT_EXPERIMENTAL_IDENTITY"
EXACT = URIRef(definitions.ontology.NS["oboInOwl"] + "hasExactSynonym")
SYNONYMS = [
    URIRef(definitions.ontology.NS["oboInOwl"] + "has" + kind + "Synonym")
    for kind in ("Exact", "Related", "Broad", "Narrow")
]
QUALIFIED = "EXPLICIT_ALIAS_AND_SPECIES_REFERENCE_NOT_EXPERIMENTAL_ALLELE"


def ontology_graph(root, dossier):
    cached = read_json(root, dossier["inputs"]["ontology_cache"])
    body = cached["body"].encode()
    require(
        cached["status"] == 200
        and len(body) == cached["bytes"]
        and hashlib.sha256(body).hexdigest() == cached["sha256"]
        and all(cached[k] == dossier["ontology"][k] for k in ("url", "sha256", "retrieved_at"))
        and re.fullmatch(
            r"https://raw\.githubusercontent\.com/arpcard/aro/[a-f0-9]{40}/aro\.owl", cached["url"]
        ),
        "ontology cache identity changed",
    )
    return Graph().parse(data=body, format="xml")


def annotation_context(graph, selected, dossier, aliases):
    labels = {t: r["source_label"] for t, r in selected.items()}
    projected = definitions.project_annotations(graph, labels)
    require(set(aliases) <= set(selected), "alias outside unresolved cohort")
    result = {}
    for term, row in selected.items():
        node = URIRef(definitions.ontology.BASE + term.removeprefix("ARO:"))
        frozen = dossier["terms"][term]
        require(
            all(frozen[k] == v for k, v in projected[term].items())
            and frozen["record_memberships"] == row["record_memberships"]
            and frozen["definition_citation_ids"] == row["definition_citations"],
            "source definition, citation or membership binding changed",
        )
        accepted = []
        for alias in aliases.get(term, []):
            require(
                set(alias) == {"kind", "value"}
                and alias["kind"] in {"GENE_SYMBOL", "ORDERED_LOCUS", "ACCESSION_LIKE_SYNONYM"}
                and (node, EXACT, Literal(alias["value"])) in graph,
                "alias lacks the exact plain-literal source assertion",
            )
            accepted.append(
                {
                    **alias,
                    "predicate": str(EXACT),
                    "target": definitions.rdf_identity(Literal(alias["value"])),
                }
            )
        require(len({a["value"] for a in accepted}) == len(accepted), "duplicate source alias")
        annotations = [
            {"predicate": str(predicate), "target": definitions.rdf_identity(value)}
            for predicate in SYNONYMS
            for value in graph.objects(node, predicate)
        ]
        text = [str(v) for v in graph.objects(node, definitions.DEFINITION)]
        flags = []
        # This is a scoped source inconsistency, not an automatic gene correction.
        if row["tokens"]["gene"] in {"MDR2", "MDR4"} and any(v.startswith("MDR1 encodes ") for v in text):
            flags.append(
                {
                    "status": "LABEL_DEFINITION_GENE_CONFLICT_WITHHELD",
                    "label_gene": row["tokens"]["gene"],
                    "definition_gene": "MDR1",
                    "correct_gene_inferred": False,
                    "definition_hashes": [
                        definitions.text_hash(v) for v in text if v.startswith("MDR1 encodes ")
                    ],
                }
            )
        result[term] = {
            "definition_annotation": projected[term],
            "synonym_annotations": sorted(annotations, key=lambda v: json.dumps(v, sort_keys=True)),
            "selected_alias_leads": accepted,
            "source_flags": flags,
            "unselected_synonyms_are_gene_aliases": False,
            "unselected_synonyms_disposition": "NOT_PROMOTED_FROM_ONTOLOGY_SYNONYM_TO_GENE_IDENTITY",
        }
    return result


def alias_matches(entry, alias):
    value, kind = alias["value"], alias["kind"]
    if kind == "GENE_SYMBOL":
        return prior.prior.gene_matches(entry, value)
    if kind == "ORDERED_LOCUS":
        return [m for m in prior.native_matches(entry, value) if "/orderedLocusNames/" in m["field"]]
    require(kind == "ACCESSION_LIKE_SYNONYM", "unknown alias namespace")
    return [
        {"field": field, "value": accession}
        for field, accession in [("primaryAccession", entry["primaryAccession"])]
        + [(f"secondaryAccessions/{i}", v) for i, v in enumerate(entry.get("secondaryAccessions", []))]
        if accession == value
    ]


def read_queries(root, plan, selected):
    frozen = read_json(root, plan["own_citation_plan"])
    own = {c.removeprefix("PMID:") for t in plan["aliases"] for c in selected[t]["definition_citations"]}
    require(all(re.fullmatch(r"[1-9][0-9]*", p) for p in own), "unhandled citation namespace")
    directories = dict(plan["cached_candidate_queries"])
    for pmid in own:
        directory = frozen["queries"][pmid]["directory"]
        require(pmid not in directories or directories[pmid] == directory, "conflicting query cache")
        directories[pmid] = directory
    entries, queries, pools = {}, {}, {}
    for pmid, directory in sorted(directories.items()):
        found, provenance = literature.read_query(root, root / directory, pmid)
        require(
            provenance["complete_for_query"] and provenance["release"] == "2026_03",
            "incomplete or changed query release",
        )
        if pmid in own:
            require(provenance == frozen["queries"][pmid]["query"], "own-citation query drift")
        queries[pmid] = {"directory": directory, "provenance": provenance, "result_count": len(found)}
        pools[pmid] = set(found)
        for accession, entry in found.items():
            require(not {"sequence", "features", "comments"} & set(entry), "operational metadata rejected")
            if not any(alias_matches(entry, a) for aa in plan["aliases"].values() for a in aa):
                continue
            require(accession not in entries or entries[accession] == entry, "conflicting native reference")
            entries[accession] = entry
    return entries, queries, pools


def reference_status(source_species, reference_species):
    if reference_species is None:
        return "REFERENCE_TAXONOMY_UNRESOLVED_WITHHELD"
    return QUALIFIED if source_species == reference_species else "DIFFERENT_SPECIES_REFERENCE_WITHHELD"


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["constraints"]
        == {
            "network_requests": 0,
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "biological_record_writes": False,
            "experimental_identity_assignments": False,
            "operational_details_exported": False,
            "new_primary_reviews": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "reference-only constraints changed",
    )
    for pin in plan["inputs"].values():
        reference.check_pin(root, pin)
    inputs = {k: read_json(root, v) for k, v in plan["inputs"].items() if k != "source_queue"}
    checkpoint = inputs["prior"]
    require(
        inputs["prior_verification"]["artifacts"]["dossier"] == plan["inputs"]["prior"],
        "prior verification mismatch",
    )
    selected = {t: r for t, r in checkpoint["terms"].items() if not r["qualified_reference_accessions"]}
    require(len(selected) == 42, "remaining cohort changed")
    records, claims = prior.prior.members.current_context(
        root,
        inputs["index"],
        inputs["corpus_update"],
        set(selected),
        {t: r["source_label"] for t, r in selected.items()},
    )
    graph = ontology_graph(root, inputs["definitions"])
    annotations = annotation_context(graph, selected, inputs["definitions"], plan["aliases"])
    entries, queries, pools = read_queries(root, plan, selected)
    registry = inputs["taxonomy_inventory"]["registry"]
    views, taxonomy_sources = {}, {}
    for accession, entry in sorted(entries.items()):
        tid = str(entry["organism"]["taxonId"])
        if tid in registry:
            node, provenance = prior.cached_node(root, registry[tid])
            views[accession] = prior.prior.members.member_reference(entry, node)
            taxonomy_sources[tid] = provenance
        else:
            views[accession] = {
                "protein_accession": "UniProtKB:" + accession,
                "entry_type": entry["entryType"],
                "entry_audit": entry["entryAudit"],
                "native_organism": entry["organism"],
                "reference_taxonomy": {"species": None},
                "status": "NO_NODE_IN_PINNED_TAXONOMY_INVENTORY_NOT_ABSENCE_FROM_UNIPROT",
                "experimental_subject_assignment": False,
            }
    bindings = {}
    for name in sorted({selected[t]["tokens"]["species"] for t in plan["aliases"]}):
        binding = checkpoint["source_bindings"][name]
        node, _ = prior.cached_node(
            root, {"taxon_id": str(binding["identity"]["taxonId"]), "source": binding["native_source"]}
        )
        require(
            prior.lineages.identity(node) == binding["identity"]
            and prior.prior.species_name_binding(name, node) == binding["native_name_fields"],
            "source species name changed",
        )
        bindings[name] = binding
    terms = {}
    for term, row in selected.items():
        candidates = []
        for accession, entry in sorted(entries.items()):
            matched = [
                {"source_alias": alias, "native_fields": fields}
                for alias in annotations[term]["selected_alias_leads"]
                if (fields := alias_matches(entry, alias))
            ]
            if not matched:
                continue
            status = reference_status(
                bindings[row["tokens"]["species"]]["identity"],
                views[accession]["reference_taxonomy"]["species"],
            )
            citations = ["PMID:" + p for p, pool in pools.items() if accession in pool]
            candidates.append(
                {
                    "protein_accession": "UniProtKB:" + accession,
                    "alias_matches": matched,
                    "cached_citation_query_memberships": citations,
                    "own_definition_citation_query_overlap": sorted(
                        set(citations) & set(row["definition_citations"])
                    ),
                    "disposition": status,
                    "qualified_reference": status == QUALIFIED,
                    "primary_resistance_validation": False,
                    "experimental_subject_assignment": False,
                    "exact_allele_assignment": False,
                }
            )
        terms[term] = {
            "source_label": row["source_label"],
            "tokens": row["tokens"],
            "record_memberships": row["record_memberships"],
            **annotations[term],
            "reference_candidates": candidates,
            "qualified_reference_accessions": [
                c["protein_accession"] for c in candidates if c["qualified_reference"]
            ],
            "whole_record_primary_review": "OPEN",
            "biological_absence_inferred": False,
        }
    qualified = {t for t, r in terms.items() if r["qualified_reference_accessions"]}
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "inputs": plan["inputs"],
        "ontology": inputs["definitions"]["ontology"],
        "ontology_cache": inputs["definitions"]["inputs"]["ontology_cache"],
        "records": records,
        "claims": claims,
        "terms": terms,
        "queries": queries,
        "source_bindings": bindings,
        "reference_views": {"UniProtKB:" + a: v for a, v in views.items()},
        "taxonomy_sources": taxonomy_sources,
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(records),
            "source_claims": len(claims),
            "selected_terms": len(terms),
            "synonym_annotations": sum(len(r["synonym_annotations"]) for r in terms.values()),
            "terms_with_selected_alias_leads": len(plan["aliases"]),
            "selected_alias_leads": sum(len(a) for a in plan["aliases"].values()),
            "source_conflict_terms": sum(bool(r["source_flags"]) for r in terms.values()),
            "complete_cached_queries": len(queries),
            "cached_query_result_occurrences": sum(q["result_count"] for q in queries.values()),
            "native_reference_candidates": len(entries),
            "cached_reference_taxa": len(taxonomy_sources),
            "candidate_dispositions": dict(
                sorted(
                    Counter(
                        c["disposition"] for r in terms.values() for c in r["reference_candidates"]
                    ).items()
                )
            ),
            "qualified_reference_terms": len(qualified),
            "qualified_reference_links": sum(
                len(r["qualified_reference_accessions"]) for r in terms.values()
            ),
            "qualified_reference_claim_memberships": sum(
                len(terms[t]["record_memberships"]) for t in qualified
            ),
            "qualified_reference_records": len(
                {rid for t in qualified for rid in terms[t]["record_memberships"]}
            ),
            "unresolved_terms_in_selected_cohort": len(terms) - len(qualified),
            "network_requests": 0,
            "biological_record_writes": 0,
            "whole_record_primary_signoffs": 0,
        },
        "attribution": {"CARD_ARO": inputs["definitions"]["attribution"], "UniProt": "CC BY 4.0"},
        "limits": [
            "Ontology synonyms are discovery leads, not experimental alleles or functional validation.",
            "Only four inspected identity aliases were selected; "
            "other synonyms are not inferred gene aliases.",
            "Case-sensitive cache discovery is bounded and not an exhaustive UniProt alias search.",
            "Reference species agreement does not identify the tested subject, allele or genome.",
            "Label-definition conflicts remain unresolved; source-owned assertions are unchanged.",
            "No sequences, variants, protocols or numerical AST are exported.",
            "No network, NCBI access, outreach, source adoption or GitHub mutation; #1040 remains deferred.",
            "The full corpus investigation and primary-evidence review remain OPEN.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    output = args.root / args.output
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.check or output.exists():
        require(output.read_text() == payload, "saved alias audit differs from offline replay")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
