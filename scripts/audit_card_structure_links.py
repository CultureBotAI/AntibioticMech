"""Audit explicit ARO -> PDB -> UniProt reference paths from cached metadata.

Offline only. A reciprocal database link is not an experimental allele mapping.
"""

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_term_scope as ontology
from rdflib import OWL, RDF, RDFS, Graph, URIRef
from seed_from_sources import is_card_sourced

from antibioticmech.activity_collections import load_record

PREFIX = "research/2026-10-09-card-structure-links"
INPUTS = {
    "term_scope": "research/2026-10-09-card-term-scope.json",
    "reference_audit": "research/2026-10-07-card-reference-grounding.json",
    "reference_ledger": "research/2026-10-07-card-reference-ledger.tsv",
    "census": "research/2026-10-09-canthin-resistance-grounding.tsv",
    "source_inventory": "data/raw/aro_resistance_edges.tsv",
}
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_pdb,xref_card,lit_pubmed_id,sequence_version,version"
)
SCOPE = "DATABASE_STRUCTURE_REFERENCE_PATH_NOT_EXPERIMENTAL_ALLELE_OR_RESISTANCE_ASSIGNMENT"
REVIEWS = {
    "ARO:3000309": (
        "2GFP",
        "P31442",
        "REFERENCE_CONTEXT_ONLY",
        "The linked structure is an EmrD reference. The UniProt entry denotes K12, "
        "whereas the PDB entity source denotes the species; neither identifies a tested resistance isolate.",
    ),
    "ARO:3000866": (
        "2IYA",
        "Q3HTL7",
        "REFERENCE_CONTEXT_ONLY",
        "The explicit structural reference and UniProt gene annotation agree on oleI. "
        "This does not establish an exact experimental allele or whole-cell phenotype.",
    ),
    "ARO:3001307": (
        "2Z2P",
        "P17978",
        "INACTIVE_STRUCTURAL_REFERENCE_NOT_RESISTANCE_SUBJECT",
        "The deposition page identifies an inactive enzyme structure. Its UniProt reference "
        "uses vgb, not the ARO label vgbA. A second polymer entity has no UniProt reference "
        "and has a different source organism; it must not supply the enzyme's taxon.",
    ),
    "ARO:3002547": (
        "1V0C",
        "Q6SJ71",
        "EXACT_ALLELE_NOT_RESOLVED_BY_STRUCTURE",
        "The PDB literature abstract distinguishes the wild-type structures from the "
        "bifunctional variant model. The UniProt entry aggregates several source gene names. "
        "Neither the structural link nor those synonyms establishes the exact ARO allele.",
    ),
    "ARO:3002637": (
        "3N4T",
        "O68183",
        "NOMENCLATURE_REVIEW_REQUIRED",
        "The ARO and PDB labels use IVa, while the current UniProt gene annotation uses Id. "
        "The reciprocal accession link is verified, but this audit does not establish a "
        "nomenclature equivalence or an experimental allele.",
    ),
    "ARO:3004042": (
        "2F1M",
        "P0AE06",
        "REJECT_FOCAL_ORGANISM_ASSIGNMENT",
        "The ARO label denotes Enterobacter cloacae acrA, but the PDB entity is Escherichia coli "
        "and UniProt denotes E. coli K12. UniProt explicitly links a different CARD term, "
        "ARO:3004043. Keep the ontology structure cross-reference, but reject its use as "
        "the focal organism's protein or an exact resistance allele.",
    ),
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin(root, path):
    return {"path": str(path.relative_to(root)), "sha256": sha(path)}


def receipt(root, path, host):
    raw = json.loads(path.read_bytes())
    url = urlsplit(raw["url"])
    if (
        raw["status"] != 200
        or raw["sha256"] != hashlib.sha256(raw["body"].encode()).hexdigest()
        or url.scheme != "https"
        or url.netloc != host
        or url.fragment
    ):
        raise ValueError("cache identity or checksum mismatch")
    public = {k: raw[k] for k in ("url", "status", "sha256", "retrieved_at")}
    public["cache"] = pin(root, path)
    return raw, json.loads(raw["body"]), public


def direct_xrefs(body, selected, labels):
    graph = Graph().parse(data=body, format="xml")
    result = {}
    for term in sorted(selected):
        node = URIRef(ontology.BASE + term.removeprefix("ARO:"))
        if (node, RDF.type, OWL.Class) not in graph or sorted(
            str(v) for v in graph.objects(node, RDFS.label)
        ) != labels[term]:
            raise ValueError("ontology term identity mismatch")
        predicate = URIRef(ontology.NS["oboInOwl"] + "hasDbXref")
        result[term] = sorted(str(v) for v in graph.objects(node, predicate))
    return result


def entity_references(entry):
    """Keep each source organism attached to its own entity, including unlinked ones."""
    result, seen = [], set()
    for entity in entry["polymer_entities"]:
        eid = entity["rcsb_id"]
        if eid in seen or not eid.startswith(entry["rcsb_id"] + "_"):
            raise ValueError("duplicate or mismatched polymer entity")
        seen.add(eid)
        identifiers = entity["rcsb_polymer_entity_container_identifiers"]
        refs = identifiers["reference_sequence_identifiers"] or []
        result.append(
            {
                "entity_id": eid,
                "reference_accessions": sorted(
                    {"UniProtKB:" + r["database_accession"] for r in refs if r["database_name"] == "UniProt"}
                ),
                "other_reference_identifiers": [r for r in refs if r["database_name"] != "UniProt"],
                "source_organisms": entity["rcsb_entity_source_organism"] or [],
            }
        )
    return sorted(result, key=lambda row: row["entity_id"])


def pdb_query(identifier):
    return "{entries(entry_ids:[" + json.dumps(identifier) + """]) {
      rcsb_id
      rcsb_accession_info {major_revision minor_revision revision_date}
      rcsb_primary_citation {pdbx_database_id_PubMed pdbx_database_id_DOI year}
      polymer_entities {
        rcsb_id
        rcsb_polymer_entity_container_identifiers {
          reference_sequence_identifiers {database_name database_accession}
        }
        rcsb_entity_source_organism {ncbi_taxonomy_id scientific_name}
      }
    }}"""


def uniprot_metadata(root, cache_dir):
    proteins, taxa, requests, releases = {}, {}, [], set()
    for path in sorted(cache_dir.glob("request-*.json")):
        raw, data, public = receipt(root, path, "rest.uniprot.org")
        url = urlsplit(raw["url"])
        if url.path.startswith("/taxonomy/"):
            taxid = url.path.removeprefix("/taxonomy/")
            if url.query or taxid != str(data["taxonId"]) or data["active"] is not True or taxid in taxa:
                raise ValueError("taxonomy response identity mismatch")
            taxa[taxid] = data
            public["kind"] = "REFERENCE_TAXONOMY"
        else:
            params = parse_qs(url.query, strict_parsing=True)
            headers = {k.lower(): v for k, v in raw["headers"].items()}
            entries = data["results"]
            if (
                url.path != "/uniprotkb/search"
                or len(entries) != 1
                or headers.get("link")
                or headers["x-total-results"] != "1"
            ):
                raise ValueError("incomplete or ambiguous accession response")
            (entry,) = entries
            accession = entry["primaryAccession"]
            expected = {
                "query": ["accession:" + accession],
                "fields": [FIELDS],
                "size": ["500"],
                "format": ["json"],
            }
            if params != expected or "sequence" in entry or accession in proteins:
                raise ValueError("unexpected accession query or response")
            proteins[accession] = entry
            releases.add(headers["x-uniprot-release"])
            public.update(
                kind="EXACT_ACCESSION_METADATA",
                query=params["query"][0],
                release=headers["x-uniprot-release"],
                result_count=1,
                complete_for_query=True,
            )
        requests.append(public)
    if len(releases) != 1:
        raise ValueError("missing or mixed UniProt releases")
    return proteins, taxa, requests, releases.pop()


def reference_metadata(entry):
    return {
        "accession": "UniProtKB:" + entry["primaryAccession"],
        "entry_type": entry["entryType"],
        "entry_audit": entry["entryAudit"],
        "reference_taxon_id": "NCBITaxon:" + str(entry["organism"]["taxonId"]),
        "reference_taxon_label": entry["organism"]["scientificName"],
        "gene_symbols": [g["geneName"]["value"] for g in entry.get("genes", []) if "geneName" in g],
        "pdb_cross_reference_ids": sorted(
            r["id"] for r in entry.get("uniProtKBCrossReferences", []) if r["database"] == "PDB"
        ),
        "card_cross_reference_ids": sorted(
            r["id"] for r in entry.get("uniProtKBCrossReferences", []) if r["database"] == "CARD"
        ),
        "citation_ids": sorted(
            {
                "PMID:" + r["id"]
                for ref in entry.get("references", [])
                for r in ref["citation"].get("citationCrossReferences", [])
                if r["database"] == "PubMed"
            }
        ),
    }


def analyze(root, cache_dir, only=None):
    pins = {k: pin(root, root / p) for k, p in INPUTS.items()}
    scope = json.loads((root / INPUTS["term_scope"]).read_bytes())
    audit = json.loads((root / INPUTS["reference_audit"]).read_bytes())
    if (
        scope["reference_audit"] != pins["reference_audit"]
        or scope["source_inventory"] != pins["source_inventory"]
        or scope["reference_ledger"] != pins["reference_ledger"]
    ):
        raise ValueError("historical audit input drift")
    raw_path = root / scope["ontology_cache"]["path"]
    if pin(root, raw_path) != scope["ontology_cache"]:
        raise ValueError("ontology cache drift")
    raw = json.loads(raw_path.read_bytes())
    if (
        raw["status"] != 200
        or raw["url"] != scope["ontology"]["url"]
        or hashlib.sha256(raw["body"].encode()).hexdigest() != scope["ontology"]["sha256"]
    ):
        raise ValueError("ontology payload drift")
    unlinked = {
        t for t, r in audit["determinants"].items() if r["status"] == "NO_EXPLICIT_LINK_IN_THIS_RELEASE"
    }
    labels = {t: r["labels"] for t, r in audit["determinants"].items()}
    refs = direct_xrefs(raw["body"], unlinked, labels)
    pdb_terms = {t: values for t, values in refs.items() if any(v.startswith("PDB:") for v in values)}
    selected = set(pdb_terms) if only is None else set(only)
    if not selected or not selected <= set(pdb_terms):
        raise ValueError("invalid canary selection")
    with (root / INPUTS["census"]).open() as handle:
        census = list(csv.DictReader(handle, delimiter="\t"))
    actual_paths = {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
    if (
        len(census) != len(actual_paths)
        or {r["path"] for r in census} != actual_paths
        or any(sha(root / r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("current corpus differs from the checkpoint")
    with (root / INPUTS["reference_ledger"]).open() as handle:
        members = [r for r in csv.DictReader(handle, delimiter="\t") if r["aro_id"] in selected]
    records = []
    for rel in sorted({r["path"] for r in members}):
        path = root / rel
        before = sha(path)
        record = load_record(path)
        rows = [r for r in members if r["path"] == rel]
        claims = [c for c in record.get("resistance_mechanisms", []) if c.get("aro_id") in selected]
        if (
            Counter(c["aro_id"] for c in claims) != Counter(r["aro_id"] for r in rows)
            or any(not is_card_sourced(c) or [c["label"]] != labels[c["aro_id"]] for c in claims)
            or any(
                record["identifier"] != r["identifier"]
                or record["chemical_structure"]["standard_inchi_key"] != r["standard_inchi_key"]
                for r in rows
            )
            or sha(path) != before
        ):
            raise ValueError("current record membership or identity drift")
        records.append(
            {
                "identifier": record["identifier"],
                "label": record["label"],
                "path": rel,
                "sha256": before,
                "standard_inchi_key": record["chemical_structure"]["standard_inchi_key"],
                "aro_ids": sorted(c["aro_id"] for c in claims),
            }
        )
    proteins, taxa, requests, release = uniprot_metadata(root, cache_dir)
    links, used_proteins, used_taxa = {}, set(), set()
    for term in sorted(selected):
        structures = []
        for xref in pdb_terms[term]:
            if not xref.startswith("PDB:"):
                continue
            pdb_id = xref.removeprefix("PDB:")
            _, data, source = receipt(root, cache_dir / ("pdb-" + pdb_id + ".json"), "data.rcsb.org")
            url = urlsplit(source["url"])
            if url.path != "/graphql" or parse_qs(url.query) != {"query": [pdb_query(pdb_id)]}:
                raise ValueError("unexpected PDB query")
            if data.get("errors") or len(data["data"]["entries"]) != 1:
                raise ValueError("incomplete PDB response")
            (entry,) = data["data"]["entries"]
            if entry["rcsb_id"] != pdb_id:
                raise ValueError("PDB identity mismatch")
            entities = entity_references(entry)
            for entity in entities:
                for organism in entity["source_organisms"]:
                    used_taxa.add(str(organism["ncbi_taxonomy_id"]))
                for curie in entity["reference_accessions"]:
                    accession = curie.removeprefix("UniProtKB:")
                    metadata = reference_metadata(proteins[accession])
                    if pdb_id not in metadata["pdb_cross_reference_ids"]:
                        raise ValueError("PDB link is not reciprocal")
                    used_proteins.add(accession)
                    used_taxa.add(str(proteins[accession]["organism"]["taxonId"]))
            structures.append(
                {
                    "pdb_id": pdb_id,
                    "revision": entry["rcsb_accession_info"],
                    "primary_citation": entry["rcsb_primary_citation"],
                    "entities": entities,
                    "request": source,
                }
            )
        reviewed_pdb, reviewed_accession, decision, note = REVIEWS[term]
        if (
            len(structures) != 1
            or structures[0]["pdb_id"] != reviewed_pdb
            or {a for e in structures[0]["entities"] for a in e["reference_accessions"]}
            != {"UniProtKB:" + reviewed_accession}
        ):
            raise ValueError("manual context review no longer matches the reference path")
        links[term] = {
            "source_label": labels[term][0],
            "source_xrefs": refs[term],
            "structures": structures,
            "scope": SCOPE,
            "experimental_assignment": False,
            "primary_review_status": "PENDING",
            "context_review": {
                "decision": decision,
                "note": note,
                "source_url": "https://www.rcsb.org/structure/" + reviewed_pdb,
                "evidence_scope": "DATABASE_METADATA_AND_DEPOSITION_PAGE_NOT_PRIMARY_RESULTS",
            },
        }
    for accession in used_proteins:
        organism = proteins[accession]["organism"]
        if taxa[str(organism["taxonId"])]["scientificName"] != organism["scientificName"]:
            raise ValueError("reference taxonomy label mismatch")
    result = {
        "scope": SCOPE,
        "selection": "ALL_DIRECT_PDB_LINKS" if only is None else "CANARY_ONLY",
        "inputs": pins,
        "ontology": scope["ontology"],
        "ontology_cache": scope["ontology_cache"],
        "coverage": {
            "unlinked_terms_scanned": len(refs),
            "direct_xref_namespace_counts": dict(
                Counter(v.split(":", 1)[0] for vs in refs.values() for v in vs)
            ),
            "terms_without_direct_xrefs": sum(not vs for vs in refs.values()),
            "scan_scope": "DIRECT_HAS_DB_XREF_ON_UNLINKED_NAMED_CLASSES_ONLY_NO_ANCESTOR_INHERITANCE",
        },
        "links": links,
        "records": records,
        "proteins": {"UniProtKB:" + a: reference_metadata(proteins[a]) for a in sorted(used_proteins)},
        "taxonomy": {
            t: {k: taxa[t][k] for k in ("taxonId", "scientificName", "rank", "active", "parent", "lineage")}
            for t in sorted(used_taxa, key=int)
        },
        "uniprot_requests": requests,
        "uniprot_release": release,
        "summary": {
            "corpus_records_verified": len(census),
            "selected_terms": len(links),
            "record_memberships": len(members),
            "selected_records_loaded": len(records),
            "reference_proteins": len(used_proteins),
            "biological_record_changes": 0,
            "curation_events_added": 0,
            "whole_records_completed": 0,
            "full_corpus_primary_review": "OPEN",
            "ignored_files_included": True,
        },
        "attribution": {
            "ontology": scope["attribution"],
            "protein_metadata": "UniProt Consortium, CC BY 4.0",
            "structure_metadata": "RCSB PDB / wwPDB, CC0",
            "documentation": "https://data.rcsb.org/",
        },
        "limitations": [
            "An explicit ontology structure link and reciprocal UniProt reference identify database context, "
            "not an exact allele.",
            "Source organisms remain entity-specific; a peptide's source is not the enzyme's organism.",
            "Reference taxonomy is not the tested isolate, host, strain, genome or clinical susceptibility.",
            "PDB primary citations are discovery leads; "
            "their Results and supplements have not been reviewed in this audit.",
            "No ancestor, child, name-only or homology join is used, and no source assertion is replaced.",
            "Missing direct xrefs in this pinned snapshot do not establish absence from other resources "
            "or absence of resistance.",
            "No NCBI request, source adoption, card.json request, "
            "sequence comparison or biological curation occurred.",
            "The public export contains no sequences, variant specifications, "
            "protocols, coordinates or quantitative AST.",
            "This audit does not change the original direct UniProt CARD-cross-reference coverage counts.",
        ],
    }
    if any(pin(root, root / v["path"]) != v for v in pins.values()):
        raise ValueError("audit input changed during analysis")
    cache_pins = [
        scope["ontology_cache"],
        *(r["cache"] for r in requests),
        *(s["request"]["cache"] for link in links.values() for s in link["structures"]),
    ]
    if any(pin(root, root / v["path"]) != v for v in cache_pins):
        raise ValueError("cached metadata changed during analysis")
    if any(sha(root / r["path"]) != r["record_sha256"] for r in census):
        raise ValueError("corpus changed during analysis")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--only", action="append")
    args = parser.parse_args()
    result = analyze(args.root.resolve(), args.cache_dir.resolve(), args.only)
    payload = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
    if args.output.exists() and args.output.read_bytes() != payload:
        raise ValueError("refusing to overwrite a different historical export")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
