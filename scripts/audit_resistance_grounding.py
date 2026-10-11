"""Census every record and audit existing PHI-base accession grounding.

This is not a literature review or evidence of completed allele curation.
Network requests require explicit opt-in and contact UniProt only.
"""

import argparse
import csv
import hashlib
import json
import re
import subprocess
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests

from antibioticmech.activity_collections import load_record

OUT: Path | None = None
ALLOW_NETWORK = False


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def write(name, value):
    target = OUT / name
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True, default=str) + "\n")
    temporary.replace(target)


def fetch(path, params=None):
    url = "https://rest.uniprot.org/" + path
    key = digest(json.dumps([url, params], sort_keys=True).encode())
    target = OUT / ("request-" + key + ".json")
    if target.exists():
        cached = json.loads(target.read_text())
        if digest(cached["body"].encode()) != cached["sha256"]:
            raise ValueError("cache checksum mismatch")
        return cached
    if not ALLOW_NETWORK:
        raise ValueError("missing cached UniProt response; network is disabled")
    if urlparse(url).hostname != "rest.uniprot.org":
        raise ValueError("only UniProt requests are authorized")
    for attempt in range(3):
        try:
            response = requests.get(url, params=params, timeout=(10, 60), allow_redirects=False)
        except (requests.Timeout, requests.ConnectionError):
            if attempt == 2:
                raise
        else:
            if response.status_code not in (429, 500, 502, 503, 504) or attempt == 2:
                break
        time.sleep(2**attempt)
    result = {
        "url": response.url,
        "status": response.status_code,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "headers": dict(response.headers),
        "sha256": digest(response.content),
        "body": response.text,
    }
    if digest(result["body"].encode()) != result["sha256"]:
        raise ValueError("response is not UTF-8")
    if response.status_code == 200:
        write(target.name, result)
    time.sleep(0.15)
    return result


def inventory(root):
    records = []
    paths = sorted((root / "data/antibiotics").rglob("*.yaml"))
    identifiers = set()
    for index, path in enumerate(paths, 1):
        before = digest(path.read_bytes())
        doc = load_record(path)
        if before != digest(path.read_bytes()):
            raise ValueError("record changed during audit")
        if doc["identifier"] in identifiers:
            raise ValueError("duplicate record identifier")
        identifiers.add(doc["identifier"])
        mechanisms = doc.get("resistance_mechanisms", [])
        scores = doc.get("genotype_resistance_score_rules", [])
        records.append(
            {
                "identifier": doc["identifier"],
                "label": doc["label"],
                "path": str(path.relative_to(root)),
                "sha256": before,
                "standard_inchi_key": doc["chemical_structure"]["standard_inchi_key"],
                "class": doc["antimicrobial_class"],
                "resistance_mechanisms": mechanisms,
                "score_rules": scores,
                "activity_count": len(doc.get("activity_spectrum", [])),
                "research_status": "PENDING_PRIMARY_REVIEW" if mechanisms or scores else "PENDING_DISCOVERY",
            }
        )
        if index % 500 == 0:
            print("loaded", index, "/", len(paths), flush=True)
    result = {
        "root": str(root),
        "git_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
        "records": records,
        "counts": {
            "records": len(records),
            "with_resistance_mechanisms": sum(bool(r["resistance_mechanisms"]) for r in records),
            "with_score_rules": sum(bool(r["score_rules"]) for r in records),
            "resistance_assertions": sum(len(r["resistance_mechanisms"]) for r in records),
            "score_rules": sum(len(r["score_rules"]) for r in records),
            "pending_discovery": sum(r["research_status"] == "PENDING_DISCOVERY" for r in records),
        },
    }
    write("corpus.json", result)
    print(json.dumps(result["counts"]), flush=True)


def proteins(root):
    with (root / "data/raw/phibase_amr.tsv").open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    accessions = sorted({row["protein_accession"] for row in rows})
    entries, evidence = {}, []
    for offset in range(0, len(accessions), 15):
        batch = accessions[offset : offset + 15]
        response = fetch(
            "uniprotkb/search",
            {
                "query": " OR ".join("accession:" + acc for acc in batch),
                "format": "json",
                "size": 500,
            },
        )
        if response["status"] != 200:
            raise ValueError(response)
        payload = json.loads(response["body"])
        headers = {k.lower(): v for k, v in response["headers"].items()}
        if 'rel="next"' in headers.get("link", ""):
            raise ValueError("unexpected extra page")
        if int(headers["x-total-results"]) != len(payload["results"]):
            raise ValueError("incomplete search response")
        evidence.append({k: v for k, v in response.items() if k != "body"})
        for entry in payload["results"]:
            aliases = {entry["primaryAccession"], *entry.get("secondaryAccessions", [])}
            for acc in set(batch) & aliases:
                if acc in entries and entries[acc] != entry:
                    raise ValueError("ambiguous accession mapping")
                entries[acc] = entry
        print("protein batch", offset + len(batch), "/", len(accessions), flush=True)
    taxids = {str(entry["organism"]["taxonId"]) for entry in entries.values()}
    taxids |= {row[key] for row in rows for key in ("taxon_id", "strain_taxon_id") if row[key]}
    taxa = {}
    for index, taxid in enumerate(sorted(taxids, key=int), 1):
        response = fetch("taxonomy/" + taxid)
        evidence.append({k: v for k, v in response.items() if k != "body"})
        taxa[taxid] = (
            json.loads(response["body"])
            if response["status"] == 200
            else {"unresolved_status": response["status"]}
        )
        if index % 10 == 0:
            print("taxonomy", index, "/", len(taxids), flush=True)
    write(
        "uniprot-grounding.json",
        {
            "requested_accessions": accessions,
            "entries": entries,
            "taxa": taxa,
            "unresolved_accessions": sorted(set(accessions) - set(entries)),
            "source_inventory_sha256": digest((root / "data/raw/phibase_amr.tsv").read_bytes()),
            "requests": evidence,
        },
    )
    print("saved grounding:", len(entries), "proteins;", len(taxa), "taxa", flush=True)


def normalized(value):
    return " ".join(value.casefold().split())


def analyze(root):
    grounding = json.loads((OUT / "uniprot-grounding.json").read_text())
    with (root / "data/raw/phibase_amr.tsv").open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if digest((root / "data/raw/phibase_amr.tsv").read_bytes()) != grounding["source_inventory_sha256"]:
        raise ValueError("source inventory drift")
    results = []
    for row_number, row in enumerate(rows, 2):
        result = {
            "source_row": row_number,
            "source": row,
            "allele_evidence_status": "PRIMARY_PAPER_REVIEW_REQUIRED",
        }
        entry = grounding["entries"].get(row["protein_accession"])
        if not entry:
            result["protein_status"] = "UNRESOLVED_ACCESSION"
            results.append(result)
            continue
        result["protein_status"] = (
            "PRIMARY_ACCESSION"
            if entry["primaryAccession"] == row["protein_accession"]
            else "SECONDARY_ACCESSION"
        )
        result["primary_accession"] = entry["primaryAccession"]
        result["entry_audit"] = entry["entryAudit"]
        result["reference_is_fragment"] = entry.get("proteinDescription", {}).get("flag") == "Fragment"
        result["protein_taxon"] = entry["organism"]
        taxonomy = grounding["taxa"][str(entry["organism"]["taxonId"])]
        lineage = {str(t["taxonId"]) for t in taxonomy.get("lineage", [])}
        lineage.add(str(taxonomy.get("taxonId", "")))
        result["organism_status"] = (
            "SOURCE_TAXON_IN_PROTEIN_LINEAGE" if row["taxon_id"] in lineage else "LINEAGE_REVIEW_REQUIRED"
        )
        source_taxon = grounding["taxa"][row["taxon_id"]]
        names = [
            source_taxon.get("scientificName", ""),
            *source_taxon.get("synonyms", []),
            *source_taxon.get("otherNames", []),
        ]
        result["taxon_label_status"] = (
            "LABEL_RECOGNIZED"
            if normalized(row["taxon_label"]) in {normalized(n) for n in names}
            else "LABEL_REVIEW_REQUIRED"
        )
        if row["strain_taxon_id"]:
            strain_taxon = grounding["taxa"][row["strain_taxon_id"]]
            strain_names = [
                strain_taxon.get("scientificName", ""),
                *strain_taxon.get("synonyms", []),
                *strain_taxon.get("otherNames", []),
            ]
            for strain in strain_taxon.get("strains", []):
                strain_names.extend([strain["name"], *strain.get("synonyms", [])])
            tokens = {normalized(n) for n in strain_names}
            tokens.update(normalized(part) for name in strain_names for part in name.split(" / "))
            result["strain_status"] = (
                "STRAIN_ALIAS_RECOGNIZED_NOT_ISOLATE_PROOF"
                if normalized(row["strain_label"]) in tokens
                else "STRAIN_REVIEW_REQUIRED"
            )
            result["strain_taxon_name"] = strain_taxon.get("scientificName")
        else:
            result["strain_status"] = "NO_SOURCE_STRAIN_TAXID"
        result["genes"] = entry.get("genes", [])
        gene_ids = {
            v["value"]
            for gene in entry.get("genes", [])
            for key in ("synonyms", "orderedLocusNames", "orfNames")
            for v in gene.get(key, [])
        }
        gene_ids.update(gene["geneName"]["value"] for gene in entry.get("genes", []) if "geneName" in gene)
        for crossref in entry.get("uniProtKBCrossReferences", []):
            gene_ids.add(crossref["id"])
            gene_ids.update(
                prop["value"]
                for prop in crossref.get("properties", [])
                if prop["key"] in ("GeneId", "ProteinId", "TranscriptId")
            )
        result["gene_id_status"] = (
            "NO_SOURCE_GENE_ID"
            if not row["gene_id"]
            else "EXACT_IDENTIFIER_RECOGNIZED"
            if row["gene_id"] in gene_ids
            else "GENE_ID_REVIEW_REQUIRED"
        )
        ref_pmids = {
            x["id"]
            for ref in entry.get("references", [])
            for x in ref.get("citation", {}).get("citationCrossReferences", [])
            if x.get("database") == "PubMed"
        }
        result["source_paper_in_uniprot"] = row["pmid"] in ref_pmids
        # A residue match checks the proposed coordinate, not its phenotype or causality.
        variants = []
        if "(amino acid mutation)" in row["modification"]:
            sequence = entry["sequence"]["value"]
            for match in re.finditer(
                r"(?<![A-Za-z0-9])([ACDEFGHIKLMNPQRSTVWY])([1-9][0-9]*)([ACDEFGHIKLMNPQRSTVWY])(?=[,\s)]|$)",
                row["modification"],
            ):
                reference, position, alternate = match.groups()
                index = int(position) - 1
                actual = sequence[index] if index < len(sequence) else None
                variants.append(
                    {
                        "source_token": match.group(),
                        "reference_residue": actual,
                        "coordinate_check": (
                            "MATCH"
                            if actual == reference and not result["reference_is_fragment"]
                            else "REVIEW_REQUIRED"
                        ),
                    }
                )
        result["candidate_coordinate_checks"] = variants
        results.append(result)
    summary = {
        key: dict(Counter(r.get(key, "NOT_CHECKED") for r in results))
        for key in (
            "protein_status",
            "organism_status",
            "taxon_label_status",
            "strain_status",
            "gene_id_status",
            "source_paper_in_uniprot",
        )
    }
    summary["coordinate_checks"] = dict(
        Counter(v["coordinate_check"] for r in results for v in r.get("candidate_coordinate_checks", []))
    )
    write(
        "phibase-audit.json",
        {
            "summary": summary,
            "rows": results,
            "source_inventory_sha256": grounding["source_inventory_sha256"],
            "grounding_sha256": digest((OUT / "uniprot-grounding.json").read_bytes()),
        },
    )
    print(json.dumps(summary, indent=2), flush=True)


def ledger(root):
    corpus = json.loads((OUT / "corpus.json").read_text())
    current_paths = {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
    if current_paths != {r["path"] for r in corpus["records"]}:
        raise ValueError("corpus membership drift; rerun inventory")
    audit = json.loads((OUT / "phibase-audit.json").read_text())
    if digest((root / "data/raw/phibase_amr.tsv").read_bytes()) != audit["source_inventory_sha256"]:
        raise ValueError("source inventory drift; rerun grounding and analysis")
    if digest((OUT / "uniprot-grounding.json").read_bytes()) != audit["grounding_sha256"]:
        raise ValueError("grounding snapshot drift; rerun analysis")
    by_record = {}
    for row in audit["rows"]:
        by_record.setdefault(row["source"]["identifier"], []).append(row)
    fields = [
        "identifier",
        "label",
        "standard_inchi_key",
        "path",
        "record_sha256",
        "research_status",
        "resistance_assertions",
        "score_rules",
        "activity_observations",
        "verified_reference_accessions",
        "lineage_checked_taxids",
        "primary_papers_pending",
        "taxon_label_flags",
        "strain_flags",
        "coordinate_flags",
    ]
    rows = []
    for record in corpus["records"]:
        if digest((root / record["path"]).read_bytes()) != record["sha256"]:
            raise ValueError("corpus snapshot drift; rerun inventory")
        claims = by_record.get(record["identifier"], [])
        rows.append(
            {
                "identifier": record["identifier"],
                "label": record["label"],
                "standard_inchi_key": record["standard_inchi_key"],
                "path": record["path"],
                "record_sha256": record["sha256"],
                "research_status": record["research_status"],
                "resistance_assertions": len(record["resistance_mechanisms"]),
                "score_rules": len(record["score_rules"]),
                "activity_observations": record["activity_count"],
                "verified_reference_accessions": "|".join(
                    sorted(
                        {
                            "UniProtKB:" + claim["primary_accession"]
                            for claim in claims
                            if "primary_accession" in claim
                        }
                    )
                ),
                "lineage_checked_taxids": "|".join(
                    sorted(
                        {
                            "NCBITaxon:" + claim["source"]["taxon_id"]
                            for claim in claims
                            if claim.get("organism_status") == "SOURCE_TAXON_IN_PROTEIN_LINEAGE"
                        }
                    )
                ),
                "primary_papers_pending": "|".join(
                    sorted(
                        {
                            item["reference"]
                            for mechanism in record["resistance_mechanisms"]
                            for item in mechanism.get("evidence", [])
                            if item["reference"].startswith(("PMID:", "DOI:"))
                        }
                    )
                ),
                "taxon_label_flags": sum(
                    c.get("taxon_label_status") == "LABEL_REVIEW_REQUIRED" for c in claims
                ),
                "strain_flags": sum(c.get("strain_status") == "STRAIN_REVIEW_REQUIRED" for c in claims),
                "coordinate_flags": sum(
                    v["coordinate_check"] != "MATCH"
                    for c in claims
                    for v in c.get("candidate_coordinate_checks", [])
                ),
            }
        )
    with (OUT / "records.tsv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print("ledger:", len(rows), "records; all primary reviews remain open", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=["inventory", "proteins", "analyze", "ledger"])
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--allow-network", action="store_true")
    args = parser.parse_args()
    ALLOW_NETWORK = args.allow_network
    OUT = args.output_dir.resolve()
    OUT.mkdir(parents=True, exist_ok=True)
    globals()[args.stage](args.root.resolve())
