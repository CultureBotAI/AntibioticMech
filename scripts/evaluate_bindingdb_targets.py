#!/usr/bin/env python3
"""Evaluate the BindingDB-curated article export without writing corpus claims.

The evaluation is deliberately non-writing: issue #93 must first give a
BindingDB measurement an assertion-level target role and experimental context.
This script proves the source lane, identity join, citation, and target-taxon
filter that a later importer can reuse.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import zipfile
from array import array
from collections import Counter, defaultdict
from pathlib import Path

import yaml
from rdkit import Chem, RDLogger
from rdkit.Chem import inchi

REPO_ROOT = Path(__file__).resolve().parents[1]
CURATED_MARKER = "Curated from the literature by BindingDB"
MEASUREMENT_FIELDS = ("Ki (nM)", "IC50 (nM)", "Kd (nM)", "EC50 (nM)")
MICROBIAL_ROOTS = {
    2: "Bacteria",
    2157: "Archaea",
    4751: "Fungi",
    10239: "Viruses",
}

RDLogger.DisableLog("rdApp.warning")


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def archive_member(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        members = [name for name in archive.namelist() if name.endswith(".tsv")]
    if len(members) != 1:
        raise ValueError(f"expected one TSV in {path}, found {members}")
    return members[0]


def corpus_keys() -> dict[str, list[str]]:
    by_key: dict[str, list[str]] = defaultdict(list)
    for path in sorted((REPO_ROOT / "data" / "antibiotics").rglob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        key = str((record.get("chemical_structure") or {}).get("standard_inchi_key") or "")
        if key:
            by_key[key].append(record["identifier"])
    return by_key


def primary_reference(row: dict[str, str]) -> str:
    pmid = row.get("PMID", "").strip()
    if pmid.isdigit():
        return f"PMID:{pmid}"
    doi = row.get("Article DOI", "").strip()
    if doi:
        return f"DOI:{doi}"
    return ""


def standard_key(smiles: str) -> str:
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        return ""
    standard_inchi = inchi.MolToInchi(molecule)
    return inchi.InchiToInchiKey(standard_inchi) if standard_inchi else ""


def compact_candidate(row: dict[str, str], identifier: str) -> dict:
    measurements = {
        field.removesuffix(" (nM)"): row.get(field, "").strip()
        for field in MEASUREMENT_FIELDS
        if row.get(field, "").strip()
    }
    proteins = []
    for chain in range(1, 21):
        for status in ("SwissProt", "TrEMBL"):
            value = row.get(f"UniProt ({status}) Primary ID of Target Chain {chain}", "")
            name_kind = "Recommended" if status == "SwissProt" else "Submitted"
            label = row.get(f"UniProt ({status}) {name_kind} Name of Target Chain {chain}", "").strip()
            for accession in (part.strip() for part in value.split(",") if part.strip()):
                proteins.append({
                    "accession": accession,
                    "label": label or row["Target Name"].strip(),
                    "entry_status": "REVIEWED" if status == "SwissProt" else "UNREVIEWED",
                    "chain": chain,
                })
    # Swiss-Prot is visited first and must win if an accession is redundantly
    # present in both source columns; a dict comprehension would let the later
    # TrEMBL row downgrade REVIEWED to UNREVIEWED.
    by_accession = {}
    for protein in proteins:
        by_accession.setdefault(protein["accession"], protein)
    proteins = sorted(
        by_accession.values(),
        key=lambda protein: (protein["chain"], protein["accession"]),
    )
    return {
        "identifier": identifier,
        "standard_inchi_key": row["Ligand InChI Key"].strip(),
        "bindingdb_reactant_set_id": row["BindingDB Reactant_set_id"].strip(),
        "bindingdb_monomer_id": row["BindingDB MonomerID"].strip(),
        "target_name": row["Target Name"].strip(),
        "organism": row["Target Source Organism According to Curator or DataSource"].strip(),
        "reference": primary_reference(row),
        "measurements": measurements,
        "protein_examples": proteins,
        "uniprot_accessions": [protein["accession"] for protein in proteins],
        "chain_count": row["Number of Protein Chains in Target (>1 implies a multichain complex)"].strip(),
        "article_doi": row.get("Article DOI", "").strip(),
        "pmid": row.get("PMID", "").strip(),
    }


def collect_candidates(archive_path: Path) -> tuple[list[dict], Counter]:
    by_key = corpus_keys()
    candidates = []
    counts: Counter = Counter()
    csv.field_size_limit(sys.maxsize)
    with zipfile.ZipFile(archive_path) as archive, archive.open(archive_member(archive_path)) as binary:
        text = (line.decode("utf-8", errors="replace") for line in binary)
        for row in csv.DictReader(text, delimiter="\t"):
            counts["rows_total"] += 1
            if row.get("Curation/DataSource", "").strip() != CURATED_MARKER:
                counts["rejected_not_bindingdb_curated"] += 1
                continue
            counts["proven_curated_rows"] += 1
            reported_key = row.get("Ligand InChI Key", "").strip()
            matches = by_key.get(reported_key, [])
            if not matches:
                counts["out_of_scope_structure"] += 1
                continue
            if len(matches) != 1:
                counts["ambiguous_corpus_structure"] += 1
                continue
            computed_key = standard_key(row.get("Ligand SMILES", "").strip())
            if not computed_key:
                counts["rejected_unparseable_structure"] += 1
                continue
            if computed_key != reported_key:
                counts["rejected_reported_computed_key_mismatch"] += 1
                continue
            if not primary_reference(row):
                counts["rejected_missing_primary_citation"] += 1
                continue
            if not any(row.get(field, "").strip() for field in MEASUREMENT_FIELDS):
                counts["rejected_missing_affinity_measurement"] += 1
                continue
            candidates.append(compact_candidate(row, matches[0]))
            counts["identity_citation_measurement_candidates"] += 1
    return candidates, counts


def normalized_taxon_name(value: str) -> str:
    return " ".join(value.casefold().split())


def resolve_taxa(
    taxdump: Path, names: set[str]
) -> tuple[dict[str, set[int]], dict[int, str], array]:
    wanted = {normalized_taxon_name(name) for name in names if name}
    resolved: dict[str, set[int]] = defaultdict(set)
    parents = array("I", [0])
    with zipfile.ZipFile(taxdump) as archive, archive.open("names.dmp") as binary:
        for raw in binary:
            parts = raw.decode("utf-8", errors="replace").split("\t|\t")
            if len(parts) < 4:
                continue
            taxid = int(parts[0].strip())
            name = normalized_taxon_name(parts[1].strip())
            name_class = parts[3].replace("\t|\n", "").strip()
            if name in wanted and name_class in {"scientific name", "synonym", "equivalent name"}:
                resolved[name].add(taxid)
    selected_taxids = {taxid for taxids in resolved.values() for taxid in taxids}
    scientific_names = {}
    with zipfile.ZipFile(taxdump) as archive, archive.open("names.dmp") as binary:
        for raw in binary:
            parts = raw.decode("utf-8", errors="replace").split("\t|\t")
            if len(parts) < 4:
                continue
            taxid = int(parts[0].strip())
            name_class = parts[3].replace("\t|\n", "").strip()
            if taxid in selected_taxids and name_class == "scientific name":
                scientific_names[taxid] = parts[1].strip()
    with zipfile.ZipFile(taxdump) as archive, archive.open("nodes.dmp") as binary:
        for raw in binary:
            parts = raw.split(b"\t|\t", 2)
            taxid = int(parts[0].strip())
            parent = int(parts[1].strip())
            if taxid >= len(parents):
                parents.extend([0] * (taxid + 1 - len(parents)))
            parents[taxid] = parent
    return resolved, scientific_names, parents


def microbial_root(taxid: int, parents: array) -> str:
    seen = set()
    while taxid and taxid < len(parents) and taxid not in seen:
        if taxid in MICROBIAL_ROOTS:
            return MICROBIAL_ROOTS[taxid]
        seen.add(taxid)
        parent = parents[taxid]
        if not parent or parent == taxid:
            break
        taxid = parent
    return ""


def classify_candidates(candidates: list[dict], taxdump: Path) -> tuple[list[dict], Counter]:
    resolved, scientific_names, parents = resolve_taxa(
        taxdump, {row["organism"] for row in candidates}
    )
    accepted = []
    counts: Counter = Counter()
    for candidate in candidates:
        taxids = resolved.get(normalized_taxon_name(candidate["organism"]), set())
        if len(taxids) != 1:
            counts["rejected_unresolved_or_ambiguous_taxon"] += 1
            continue
        taxid = next(iter(taxids))
        root = microbial_root(taxid, parents)
        if not root:
            counts["rejected_nonmicrobial_target"] += 1
            continue
        accepted.append(candidate | {
            "taxon_id": taxid,
            "taxon_label": scientific_names.get(taxid, candidate["organism"]),
            "microbial_root": root,
        })
        counts["accepted_measurement_rows"] += 1
        counts[f"accepted_root:{root}"] += 1
    return accepted, counts


def summarize(archive_path: Path, taxdump: Path) -> dict:
    candidates, initial = collect_candidates(archive_path)
    accepted, taxonomy = classify_candidates(candidates, taxdump)
    pairs = {
        (row["identifier"], row["target_name"], row["taxon_id"])
        for row in accepted
    }
    records = {row["identifier"] for row in accepted}
    measurements = Counter(
        name for row in accepted for name in row["measurements"]
    )
    examples = sorted(
        accepted,
        key=lambda row: (row["identifier"], row["target_name"], row["bindingdb_reactant_set_id"]),
    )[:20]
    return {
        "bindingdb_archive": archive_path.name,
        "bindingdb_sha256": sha256_of(archive_path),
        "taxdump_archive": taxdump.name,
        "taxdump_sha256": sha256_of(taxdump),
        "counts": dict(sorted((initial + taxonomy).items())),
        "accepted_records": len(records),
        "accepted_record_target_taxon_pairs": len(pairs),
        "accepted_measurement_types": dict(sorted(measurements.items())),
        "examples": examples,
        "write_decision": "EVALUATION_ONLY_SEE_EXTRACT_BINDINGDB_TARGETS",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--taxdump", type=Path, required=True)
    args = parser.parse_args()
    if not args.archive.exists() or not args.taxdump.exists():
        raise SystemExit("--archive and --taxdump must name existing pinned ZIP files")
    print(json.dumps(summarize(args.archive, args.taxdump), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
