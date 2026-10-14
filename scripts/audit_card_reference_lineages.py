"""Resolve the taxonomy ranks of all explicit CARD-linked UniProt references.

Offline only. Reference ancestry never assigns an experimental subject, allele,
or phenotype. Missing standalone species responses remain explicit.
"""

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

import audit_card_definition_citations as definitions
import audit_card_grounding as card
import audit_topoisomerase_references as reference
from resistance_checkpoint_records import checkpoint_path

PLAN = Path("reports/resistance-grounding-2026-10-14-card-reference-lineages/plan-v2.json")
OUTPUT = Path("research/2026-10-14-card-reference-lineages.json")
SCOPE = "REFERENCE_TAXONOMY_LINEAGES_NOT_EXPERIMENTAL_ORGANISM_OR_ALLELE_ASSIGNMENTS"


def identity(node):
    if (not isinstance(node, dict) or type(node.get("taxonId")) is not int
            or node["taxonId"] <= 0 or any(not isinstance(node.get(key), str)
                or not node[key].strip() for key in ("rank", "scientificName"))):
        raise ValueError("invalid taxonomy identity")
    return {key: node[key] for key in ("taxonId", "rank", "scientificName")}


def lineage(taxon):
    leaf = identity(taxon)
    if taxon.get("active") is not True:
        raise ValueError("reference taxonomy is inactive")
    nodes = taxon.get("lineage")
    if not isinstance(nodes, list):
        raise ValueError("missing taxonomy lineage")
    projected = [identity(node) for node in nodes] + [leaf]
    if len({node["taxonId"] for node in projected}) != len(projected):
        raise ValueError("duplicate or cyclic taxonomy lineage")
    parent = taxon.get("parent")
    if nodes and (not isinstance(parent, dict)
                  or parent.get("taxonId") != nodes[-1]["taxonId"]
                  or parent.get("scientificName") != nodes[-1]["scientificName"]):
        raise ValueError("parent differs from terminal lineage node")
    species = [node for node in projected if node["rank"] == "species"]
    if len(species) > 1:
        raise ValueError("ambiguous species lineage")
    return projected, species[0] if species else None


def label_flags(name):
    """Flag source wording, not taxonomic validity or organismal phenotype."""
    flags = []
    if name.casefold().startswith("uncultured "):
        flags.append("UNCULTURED_LABEL")
    if name.casefold().startswith("mixed culture "):
        flags.append("MIXED_CULTURE_LABEL")
    if re.search(r"\bsp\.(?:\s|$)", name):
        flags.append("UNSPECIFIED_SPECIES_LABEL")
    if re.search(r"\bbacterium\b", name, flags=re.IGNORECASE):
        flags.append("BACTERIUM_PLACEHOLDER_WORD")
    return flags


def native_taxon(root, item, taxid, release):
    receipt = json.loads(reference.check_pin(root, item["receipt"]).read_bytes())
    url = urlsplit(receipt["url"])
    if (url.scheme != "https" or url.netloc != "rest.uniprot.org"
            or url.path not in {f"/taxonomy/{taxid}", f"/taxonomy/{taxid}.json"}
            or url.query or url.fragment or receipt["status"] != 200):
        raise ValueError("native taxonomy request identity changed")
    body = (reference.check_pin(root, item["body"]).read_bytes() if item["body"] is not None
            else receipt["body"].encode())
    headers = {key.lower(): value for key, value in receipt["headers"].items()}
    if (hashlib.sha256(body).hexdigest() != receipt["sha256"]
            or headers.get("x-uniprot-release") != release or headers.get("link")):
        raise ValueError("native taxonomy checksum, release or pagination changed")
    taxon = json.loads(body)
    if identity(taxon)["taxonId"] != int(taxid):
        raise ValueError("native taxonomy identifies another taxon")
    lineage(taxon)
    return taxon, {**item, "url": receipt["url"], "body_sha256": receipt["sha256"],
                   "retrieved_at": receipt["retrieved_at"], "release": release}


def taxonomy_sources(root, plan, snapshot, release):
    taxa, sources = snapshot["taxa"], {}
    expected = {f"https://rest.uniprot.org/taxonomy/{key}" for key in taxa}
    requests = {row["url"]: row for row in snapshot["requests"]}
    if len(requests) != len(snapshot["requests"]) or set(requests) != expected:
        raise ValueError("reference taxonomy request coverage changed")
    for taxid, taxon in taxa.items():
        url = f"https://rest.uniprot.org/taxonomy/{taxid}"
        key = hashlib.sha256(json.dumps([url, None], sort_keys=True).encode()).hexdigest()
        path = root / Path(plan["inputs"]["taxonomy"]["path"]).parent / f"request-{key}.json"
        item = {"receipt": reference.pin(root, path), "body": None}
        native, sources[taxid] = native_taxon(root, item, taxid, release)
        receipt = json.loads(path.read_bytes())
        if (native != taxon or sources[taxid]["body_sha256"] != requests[url]["sha256"]
                or {key: value for key, value in receipt.items() if key != "body"} != requests[url]):
            raise ValueError("aggregate taxonomy differs from native response")
    extra, extra_sources = {}, {}
    for taxid, items in plan["reused_species_responses"].items():
        if taxid in taxa:
            raise ValueError("supplement would replace original reference taxonomy")
        extra_sources[taxid] = []
        for item in items:
            taxon, provenance = native_taxon(root, item, taxid, release)
            if taxon["rank"] != "species":
                raise ValueError("supplement is not a species node")
            signature = lineage(taxon)
            if taxid in extra and lineage(extra[taxid]) != signature:
                raise ValueError("conflicting native species responses")
            extra[taxid] = taxon
            extra_sources[taxid].append(provenance)
    return taxa, sources, extra, extra_sources


def project_taxa(taxa, sources, extra, extra_sources):
    known = {**taxa, **extra}
    result, species = {}, {}
    for taxid, taxon in sorted(taxa.items(), key=lambda row: int(row[0])):
        nodes, ancestor = lineage(taxon)
        if str(taxon["taxonId"]) != taxid:
            raise ValueError("taxonomy dictionary identity mismatch")
        for node in nodes:
            if str(node["taxonId"]) in known and identity(known[str(node["taxonId"])]) != node:
                raise ValueError("lineage disagrees with independently cached node")
        species_id = str(ancestor["taxonId"]) if ancestor else None
        if ancestor is not None:
            direct = known.get(species_id)
            item = {
                "taxon_id": f"NCBITaxon:{species_id}", "scientific_name": ancestor["scientificName"],
                "rank": "species", "label_flags": label_flags(ancestor["scientificName"]),
                "standalone_node_status": "ACTIVE_NATIVE_RESPONSE_VERIFIED" if direct else
                    "LINEAGE_ANNOTATION_ONLY_NO_STANDALONE_RESPONSE_SELECTED",
                "standalone_active_verified": direct is not None,
                "native_sources": [sources[species_id]] if species_id in sources
                    else extra_sources.get(species_id, []),
                "experimental_subject_assignment": False,
            }
            if direct is not None and direct.get("active") is not True:
                raise ValueError("standalone species is inactive")
            if species_id in species and species[species_id] != item:
                raise ValueError("conflicting species projections")
            species[species_id] = item
        result[taxid] = {
            "reference_taxon_id": f"NCBITaxon:{taxid}", "reference_rank": taxon["rank"],
            "reference_scientific_name": taxon["scientificName"], "reference_active": True,
            "species_taxon_id": f"NCBITaxon:{species_id}" if species_id else None,
            "species_relation": "SELF" if taxon["rank"] == "species" else
                "ANCESTOR" if ancestor else "NO_SPECIES_RANK_IN_SELECTED_LINEAGE",
            "species_to_reference_path": nodes[nodes.index(ancestor):] if ancestor else [],
            "native_source": sources[taxid], "experimental_subject_assignment": False,
        }
    return result, dict(sorted(species.items(), key=lambda row: int(row[0])))


def build(root, plan_path=PLAN, *, record_resolver=None):
    plan_path = root / plan_path
    plan = json.loads(plan_path.read_bytes())
    if (plan["selection"] != "ALL_EXPLICIT_CARD_REFERENCE_CANDIDATES"
            or plan["network_required"] is not False or plan["biological_record_writes"] is not False):
        raise ValueError("offline reference-only scope changed")
    paths = {key: reference.check_pin(root, pin) for key, pin in plan["inputs"].items()}
    prior, snapshot, taxonomy, contexts = [json.loads(paths[key].read_bytes())
                                         for key in ("references", "proteins", "taxonomy", "contexts")]
    if (prior["protein_snapshot_sha256"] != plan["inputs"]["proteins"]["sha256"]
            or prior["taxonomy_snapshot_sha256"] != plan["inputs"]["taxonomy"]["sha256"]
            or taxonomy["proteins_sha256"] != prior["protein_snapshot_sha256"]
            or snapshot["source_inventory_sha256"] != plan["inputs"]["source_inventory"]["sha256"]
            or snapshot["release"] != prior["summary"]["release"]
            or contexts["protein_snapshot_sha256"] != prior["protein_snapshot_sha256"]
            or contexts["candidate_audit_sha256"] != plan["inputs"]["references"]["sha256"]):
        raise ValueError("reference snapshot provenance mismatch")
    census, labels, memberships, records = definitions.read_corpus(
        root, paths["census"], record_resolver=record_resolver)
    if set(labels) != set(prior["determinants"]):
        raise ValueError("source term coverage changed")
    index = card.reference_index(snapshot["entries"], labels)
    taxa, sources, extra, extra_sources = taxonomy_sources(root, plan, taxonomy, snapshot["release"])
    projected, species = project_taxa(taxa, sources, extra, extra_sources)
    missing = {str(node["taxon_id"].split(":")[1]) for node in species.values()} - set(taxa)
    if (set(plan["species_outside_original_taxonomy"]) != missing
            or set(plan["reused_species_responses"]) != missing):
        raise ValueError("supplement species selection drift")
    proteins, terms = {}, {}
    for tid, expected in sorted(prior["determinants"].items()):
        candidates = index.get(tid, [])
        if (expected["labels"] != [labels[tid]]
                or [card.candidate(e, x, taxa) for e, x in candidates] != expected["candidates"]):
            raise ValueError("explicit reference candidate projection changed")
        if not candidates:
            continue
        links = []
        for entry, _ in candidates:
            if "sequence" in entry or "features" in entry:
                raise ValueError("unexpected sequence or feature payload")
            accession, taxid = "UniProtKB:" + entry["primaryAccession"], str(entry["organism"]["taxonId"])
            old = contexts["proteins"][accession]
            if (old["reference_taxon_id"] != f"NCBITaxon:{taxid}"
                    or old["entry_audit"] != entry["entryAudit"]
                    or old["reference_contexts"] != card.reference_contexts(entry)):
                raise ValueError("prior citation context no longer reproduces")
            proteins[accession] = {
                "entry_version": entry["entryAudit"]["entryVersion"],
                "sequence_version": entry["entryAudit"]["sequenceVersion"],
                "entry_type": entry["entryType"], "reference_taxon_id": f"NCBITaxon:{taxid}",
                "reference_taxon_rank": projected[taxid]["reference_rank"],
                "reference_species_taxon_id": projected[taxid]["species_taxon_id"],
                "citation_context_pointer": f"/proteins/{accession}",
                "citation_context_input": "contexts", "experimental_subject_assignment": False,
                "exact_allele_assignment": False,
            }
            links.append(accession)
        terms[tid] = {"source_label_sha256": definitions.text_hash(labels[tid]),
                      "reference_accessions": links, "record_memberships": sorted(memberships[tid]),
                      "experimental_subject_assignment": False}
    if set(proteins) != set(contexts["proteins"]):
        raise ValueError("explicit protein coverage differs from prior context audit")
    selected_ids = {rid for term in terms.values() for rid in term["record_memberships"]}
    selected_records = [{**row, "whole_record_primary_review": "OPEN"}
                        for row in records if row["identifier"] in selected_ids]
    summary = {
        "corpus_records_checked": len(census), "card_terms_checked": len(labels),
        "reference_terms": len(terms), "reference_links": sum(
            len(row["reference_accessions"]) for row in terms.values()),
        "reference_proteins": len(proteins), "record_memberships": len(selected_records),
        "reference_taxa": len(projected), "reference_taxonomy_ranks": dict(sorted(Counter(
            row["reference_rank"] for row in projected.values()).items())),
        "species_lineage_nodes": len(species), "reference_taxa_without_species_rank": sum(
            row["species_taxon_id"] is None for row in projected.values()),
        "species_nodes_with_standalone_response": sum(
            row["standalone_active_verified"] for row in species.values()),
        "species_nodes_lineage_only": sum(not row["standalone_active_verified"] for row in species.values()),
        "species_nodes_with_label_flags": sum(bool(row["label_flags"]) for row in species.values()),
        "additional_cached_species_nodes": len(extra),
        "biological_record_changes": 0, "new_network_requests": 0, "whole_record_reviews_completed": 0,
    }
    return {"date": plan["date"], "scope": SCOPE, "release": snapshot["release"],
            "inputs": {**plan["inputs"], "plan": reference.pin(root, plan_path)},
            "attribution": prior["attribution"], "taxa": projected, "species": species,
            "proteins": proteins, "terms": terms, "records": selected_records, "summary": summary,
            "limitations": [
                "Taxonomy ranks and lineages identify database references, not tested subjects or alleles.",
                "A species-rank node may still have an uncultured, mixed-culture or unspecified name.",
                "Label flags are literal wording alerts, not taxonomic corrections or biological absence.",
                "Lineage-only nodes are not claimed to have independently verified active status.",
                "Standalone-response coverage is limited to the frozen local cache search, "
                "including ignored files.",
                "Multiple reference candidates and original citation-specific strain labels are preserved.",
                "No primary result, exact compound phenotype or gene-to-isolate join is established here.",
                "Earlier primary assessments and source holds remain unchanged; "
                "all 2939 records stay in scope.",
                "No sequence, variant specification, numeric AST, protocol, "
                "gene value or new allele is exported.",
            ],
            "constraints": {"ncbi_requests": 0, "issue_1040": "DEFERRED", "source_adoptions": 0,
                            "github_mutations": 0, "experimental_assignments": 0,
                            "full_corpus_goal_status": "OPEN"}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=PLAN)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--historical-records", action="store_true",
                        help="Replay registered identifier/path/hash fixtures, not the live census.")
    args = parser.parse_args()
    result = build(Path.cwd(), args.plan,
                   record_resolver=checkpoint_path if args.historical_records else None)
    if args.check:
        if json.loads(args.output.read_bytes()) != result:
            raise SystemExit("reference lineage dossier does not reproduce")
    else:
        with args.output.open("x") as stream:
            stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
