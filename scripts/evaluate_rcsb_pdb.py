#!/usr/bin/env python3
"""Evaluate exact-ligand RCSB PDB overlap with established target examples.

The evaluator requires both an exact Standard InChIKey and a UniProt accession
already present on a BindingDB target assertion.  A hit remains a candidate:
entry-level ligand/protein co-occurrence does not by itself prove atomic contact
or antimicrobial mechanism, so this command writes no corpus claims.
"""

from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"
GRAPHQL_URL = "https://data.rcsb.org/graphql"


def post_json(url: str, payload: dict) -> dict:
    request = urllib.request.Request(  # noqa: S310 - pinned HTTPS API
        url,
        data=json.dumps(payload, separators=(",", ":")).encode(),
        headers={"Content-Type": "application/json", "User-Agent": "AntibioticMech/0.1"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:  # noqa: S310
            body = response.read()
    except urllib.error.HTTPError as error:
        if error.code == 204:
            return {}
        raise
    return json.loads(body) if body else {}


def bindingdb_targets() -> list[dict]:
    targets = []
    for path in sorted((REPO_ROOT / "data" / "antibiotics").rglob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        for target in record.get("molecular_targets") or []:
            if target.get("source") != "BINDINGDB":
                continue
            accessions = sorted({
                item["uniprot_id"].removeprefix("UniProtKB:")
                for item in (target.get("protein_examples") or [])
            })
            if accessions:
                targets.append({
                    "identifier": record["identifier"],
                    "standard_inchi_key": record["chemical_structure"]["standard_inchi_key"],
                    "target_label": target["target_label"],
                    "taxon_id": target.get("taxon_id", ""),
                    "accessions": accessions,
                })
    return targets


def search_entries(inchi_key: str, accessions: list[str]) -> list[str]:
    payload = {
        "query": {
            "type": "group",
            "logical_operator": "and",
            "nodes": [
                {
                    "type": "terminal",
                    "service": "text_chem",
                    "parameters": {
                        "attribute": "rcsb_chem_comp_descriptor.InChIKey",
                        "operator": "exact_match",
                        "value": inchi_key,
                    },
                },
                {
                    "type": "terminal",
                    "service": "text",
                    "parameters": {
                        "attribute": (
                            "rcsb_polymer_entity_container_identifiers."
                            "reference_sequence_identifiers.database_accession"
                        ),
                        "operator": "in",
                        "value": accessions,
                    },
                },
                {
                    "type": "terminal",
                    "service": "text",
                    "parameters": {
                        "attribute": (
                            "rcsb_polymer_entity_container_identifiers."
                            "reference_sequence_identifiers.database_name"
                        ),
                        "operator": "exact_match",
                        "value": "UniProt",
                    },
                },
            ],
        },
        "return_type": "entry",
        "request_options": {"return_all_hits": True},
    }
    response = post_json(SEARCH_URL, payload)
    return sorted(item["identifier"] for item in response.get("result_set", []))


def entry_metadata(entry_ids: list[str]) -> dict[str, dict]:
    if not entry_ids:
        return {}
    query = """
      query Entries($ids: [String!]!) {
        entries(entry_ids: $ids) {
          rcsb_id
          polymer_entities {
            rcsb_polymer_entity_container_identifiers {
              reference_sequence_identifiers { database_name database_accession }
            }
          }
          citation { pdbx_database_id_PubMed pdbx_database_id_DOI title }
        }
      }
    """
    output = {}
    for start in range(0, len(entry_ids), 100):
        response = post_json(
            GRAPHQL_URL,
            {"query": query, "variables": {"ids": entry_ids[start:start + 100]}},
        )
        if response.get("errors"):
            raise ValueError(f"RCSB GraphQL errors: {response['errors']}")
        for entry in response.get("data", {}).get("entries", []):
            accessions = set()
            for entity in entry.get("polymer_entities") or []:
                identifiers = (
                    entity.get("rcsb_polymer_entity_container_identifiers") or {}
                ).get("reference_sequence_identifiers") or []
                accessions.update(
                    item["database_accession"]
                    for item in identifiers
                    if item.get("database_name") == "UniProt"
                )
            citations = entry.get("citation") or []
            output[entry["rcsb_id"]] = {"accessions": accessions, "citations": citations}
    return output


def evaluate() -> tuple[list[dict], dict]:
    targets = bindingdb_targets()
    by_compound: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for target in targets:
        by_compound[(target["identifier"], target["standard_inchi_key"])].append(target)

    candidate_entries: dict[tuple[str, str], list[str]] = {}
    all_entries = set()
    for compound, compound_targets in sorted(by_compound.items()):
        accessions = sorted({a for target in compound_targets for a in target["accessions"]})
        entries = search_entries(compound[1], accessions)
        candidate_entries[compound] = entries
        all_entries.update(entries)
    metadata = entry_metadata(sorted(all_entries))

    rows = []
    for compound, entries in sorted(candidate_entries.items()):
        for target in by_compound[compound]:
            wanted = set(target["accessions"])
            for pdb_id in entries:
                common = sorted(wanted & metadata[pdb_id]["accessions"])
                if not common:
                    continue
                citations = metadata[pdb_id]["citations"]
                citation = citations[0] if citations else {}
                rows.append({
                    "identifier": compound[0],
                    "standard_inchi_key": compound[1],
                    "target_label": target["target_label"],
                    "uniprot_accessions": common,
                    "pdb_id": pdb_id,
                    "pmid": citation.get("pdbx_database_id_PubMed"),
                    "doi": citation.get("pdbx_database_id_DOI"),
                    "title": citation.get("title"),
                })
    counts = {
        "bindingdb_targets_with_uniprot": len(targets),
        "compounds_queried": len(by_compound),
        "candidate_entries": len(all_entries),
        "candidate_target_pairs": len(rows),
        "candidate_records": len({row["identifier"] for row in rows}),
    }
    return rows, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="Write candidate audit rows to this path")
    args = parser.parse_args()
    rows, counts = evaluate()
    print("RCSB PDB exact-ligand + established-UniProt audit")
    for name, count in counts.items():
        print(f"  {name}: {count}")
    for row in rows:
        reference = f"PMID:{row['pmid']}" if row["pmid"] else row["doi"] or "no citation"
        print(
            f"  {row['identifier']} {row['target_label']} -> PDB:{row['pdb_id']} "
            f"({','.join(row['uniprot_accessions'])}; {reference})"
        )
    if args.json:
        args.json.write_text(json.dumps({"counts": counts, "rows": rows}, indent=2) + "\n")
        print(f"wrote {args.json}")
    print("--audit: no rows seeded; atom-level ligand--protein contact is not yet verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
