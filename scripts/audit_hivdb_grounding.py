"""Audit HIVDB source-region and taxonomy context, without interpreting variants.

Offline only. Source-reference sequences stay in the local cache; only their
lengths and checksums are retained in the research report, never allele calls.
"""

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

import audit_card_grounding as card
import audit_resistance_grounding as common
import yaml

from antibioticmech.hivdb_score_rules import hivdb_score_rule_id

COMMIT = "be1c11a5145fea9073fdb71801919d4a34265336"
INVENTORY = "data/raw/hivdb_algorithm_terms.tsv"
MANIFEST = "data/raw/MANIFEST.yaml"
SOURCE_FILES = ("data/genes_hiv1.json", "data/strains_hiv1.json")


def response(name, expected_url):
    item = json.loads((common.OUT / name).read_bytes())
    if (item["status"] != 200 or item["url"] != expected_url
            or common.digest(item["body"].encode()) != item["sha256"]):
        raise ValueError("invalid source response")
    return item


def source_context():
    tree = response("hivfacts-tree-response.json",
                    f"https://api.github.com/repos/hivdb/hivfacts/git/trees/{COMMIT}?recursive=1")
    payload = json.loads(tree["body"])
    if payload["truncated"]:
        raise ValueError("truncated source tree")
    entries = {r["path"]: r for r in payload["tree"]}
    data, requests = {}, [tree]
    for path in SOURCE_FILES:
        item = response(f"hivfacts-{Path(path).stem}-response.json",
                        f"https://raw.githubusercontent.com/hivdb/hivfacts/{COMMIT}/{path}")
        body = item["body"].encode()
        blob = hashlib.sha1(b"blob " + str(len(body)).encode() + b"\0" + body).hexdigest()
        if blob != entries[path]["sha"] or item["git_blob_sha1"] != blob:
            raise ValueError("source blob differs from pinned tree")
        data[path] = json.loads(body)
        requests.append(item)
    genes = {r["abstractGene"]: r for r in data[SOURCE_FILES[0]]}
    if len(genes) != len(data[SOURCE_FILES[0]]):
        raise ValueError("ambiguous reference region")
    strains = data[SOURCE_FILES[1]]
    if len(strains) != 1 or strains[0]["name"] != "HIV1" or strains[0]["displayText"] != "HIV-1":
        raise ValueError("unexpected algorithm strain context")
    for gene in genes.values():
        if gene["strain"] != "HIV1" or not gene["refSequence"]:
            raise ValueError("invalid source reference region")
    return genes, strains[0], [{k: v for k, v in r.items() if k != "body"} for r in requests]


def analyze(root):
    records = card.current_corpus(root)
    census_hash = common.digest((common.OUT / "corpus.json").read_bytes())
    source_bytes = (root / INVENTORY).read_bytes()
    source_hash = common.digest(source_bytes)
    manifest_bytes = (root / MANIFEST).read_bytes()
    manifest = yaml.safe_load(manifest_bytes)
    pin = manifest["inventories"][Path(INVENTORY).name]
    source_pin = manifest["sources"]["stanford-hivdb"]
    with (root / INVENTORY).open() as handle:
        source = list(csv.DictReader(handle, delimiter="\t"))
    if (pin["sha256"] != source_hash or pin["bytes"] != len(source_bytes)
            or pin["rows"] != len(source) or source_pin["version"] != COMMIT):
        raise ValueError("source inventory differs from manifest pin")
    by_id = {r["source_rule_id"]: r for r in source}
    if len(by_id) != len(source):
        raise ValueError("duplicate source rule")
    for row in source:
        if row["source_version"] != COMMIT or row["source_rule_id"] != hivdb_score_rule_id(row):
            raise ValueError("source rule digest or version differs")
        if source_pin["algorithm"] != f'{row["algorithm_name"]} {row["algorithm_version"]}':
            raise ValueError("algorithm differs from manifest pin")
    genes, strain, requests = source_context()
    taxonomy_response = common.fetch("taxonomy/11676")
    if taxonomy_response["status"] != 200:
        raise ValueError("taxonomy unavailable")
    taxonomy = json.loads(taxonomy_response["body"])
    if (taxonomy["taxonId"] != 11676 or taxonomy["active"] is not True
            or taxonomy["commonName"] != strain["displayText"]):
        raise ValueError("taxon does not match source organism")
    taxon_names = {taxonomy["scientificName"], taxonomy["commonName"], *taxonomy.get("otherNames", [])}
    results, seen, totals = [], [], Counter()
    text_fields = ("gene", "drug_class", "algorithm_name", "algorithm_version", "algorithm_date",
                   "source_record_id", "source_rule_id", "score_term", "source_version")
    number_fields = ("score_term_index", "score_assignments", "negative_score_assignments",
                     "min_score", "max_score")
    for record in records:
        if not record["score_rules"]:
            continue
        identifiers, regions = [], Counter()
        for claim in record["score_rules"]:
            key = claim["source_rule_id"]
            row = by_id.get(key)
            if row is None or any(str(claim[k]) != row[k] for k in text_fields):
                raise ValueError("corpus rule differs from source")
            if any(float(claim[k]) != float(row[k]) for k in number_fields):
                raise ValueError("corpus score metadata differs")
            if (row["identifier"] != record["identifier"]
                    or row["standard_inchi_key"] != record["standard_inchi_key"]
                    or claim["pathogen_label"] not in taxon_names
                    or claim["source"] != "HIVDB_HIVFACTS"
                    or row["mapping_status"] != "EXACT"
                    or claim["gene"] not in genes):
                raise ValueError("compound, organism or region identity differs")
            seen.append(key)
            identifiers.append(key)
            regions[claim["gene"]] += 1
            totals[claim["gene"]] += 1
        results.append({
            "identifier": record["identifier"], "label": record["label"], "path": record["path"],
            "record_sha256": record["sha256"], "standard_inchi_key": record["standard_inchi_key"],
            "source_rule_ids": identifiers, "region_rule_counts": dict(regions),
            "pathogen_taxon_id": "NCBITaxon:11676", "pathogen_taxon_label": taxonomy["scientificName"],
            "pathogen_taxon_rank": taxonomy["rank"],
            "status": "SOURCE_REGION_AND_TAXON_VERIFIED_NOT_EXPERIMENTAL_ALLELES",
            "uniprot_status": "NO_ACCESSION_SUPPLIED_BY_PINNED_REFERENCE_DEFINITION",
            "primary_review_status": "PENDING",
        })
    if Counter(seen) != Counter(by_id.keys()):
        raise ValueError("rule membership differs from full source inventory")
    if (common.digest((root / INVENTORY).read_bytes()) != source_hash
            or (root / MANIFEST).read_bytes() != manifest_bytes
            or common.digest((common.OUT / "corpus.json").read_bytes()) != census_hash):
        raise ValueError("inputs changed during audit")
    if source_context()[2] != requests:
        raise ValueError("reference inputs changed during audit")
    card.current_corpus(root)
    common.write("hivdb-reference-grounding.json", {
        "source_commit": COMMIT, "source_inventory_sha256": source_hash,
        "manifest_sha256": common.digest(manifest_bytes),
        "corpus_sha256": census_hash, "summary": {
            "records": len(results), "score_rules": len(seen), "region_rule_counts": dict(totals),
        }, "records": results, "source_strain_definition": strain,
        "reference_regions": {name: {
            "source_name": genes[name]["name"], "abstract_gene": name,
            "source_strain_label": genes[name]["strain"],
            "reference_length": len(genes[name]["refSequence"]),
            "reference_sha256": common.digest(genes[name]["refSequence"].encode()),
        } for name in sorted(totals)},
        "taxonomy": {k: taxonomy[k] for k in ("taxonId", "scientificName", "rank", "active", "parent")},
        "requests": requests + [{k: v for k, v in taxonomy_response.items() if k != "body"}],
        "limitations": [
            "Retained rules match the manifest-pinned inventory; this audit does not re-extract source XML.",
            "Source-defined HIV1 is algorithm context, not an experimental strain or isolate.",
            "No UniProt accession is supplied by these reference definitions; no HXB2 equivalence inferred.",
            "Protein-region references are not mutant-specific accessions or normalized allele coordinates.",
            "Source formula terms remain interpretation rules, not measurements or causal mechanisms.",
            "Score rules have no taxon or reference-accession slot; grounding is report-only.",
            "No source sequence, reconstructed genotype, patient assignment or phenotype is exported.",
        ],
    })
    print(f"Verified {len(seen)} source rules across {len(results)} records: {dict(totals)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    common.OUT = args.output_dir.resolve()
    common.ALLOW_NETWORK = False
    analyze(args.root.resolve())
