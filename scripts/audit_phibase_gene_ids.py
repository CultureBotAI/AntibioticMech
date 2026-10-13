"""Offline identifier-field audit, not experimental gene or allele assignment."""

import argparse
import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path

from phibase_grounding_reviews import load_reviews, row_digest

SCOPE = "SOURCE_IDENTIFIER_FIELDS_NOT_EXPERIMENTAL_GROUNDING"
GENE_FIELDS = ("geneName", "synonyms", "orderedLocusNames", "orfNames")
TYPED_PROPERTIES = {"GeneId", "ProteinId", "TranscriptId"}


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def reference_projection(entry):
    """Retain identity metadata only; never copy sequence or variant annotations."""
    return {
        "accession": entry["primaryAccession"],
        "entry_version": entry["entryAudit"]["entryVersion"],
        "sequence_version": entry["entryAudit"]["sequenceVersion"],
        "reference_taxon_id": entry["organism"]["taxonId"],
        "reference_name": entry["organism"]["scientificName"],
        "genes": [{key: ([gene[key]["value"]] if key == "geneName" else
                          [item["value"] for item in gene[key]])
                   for key in GENE_FIELDS if key in gene}
                  for gene in entry.get("genes", [])],
        "cross_references": [
            {"database": item["database"], "id": item["id"],
             "properties": [{"key": prop["key"], "value": prop["value"]}
                            for prop in item.get("properties", [])
                            if prop["key"] in TYPED_PROPERTIES]}
            for item in entry.get("uniProtKBCrossReferences", [])],
    }


def identifier_matches(value, reference):
    if not value:
        return []
    hits = []
    for index, gene in enumerate(reference["genes"]):
        for field in GENE_FIELDS:
            if value in gene.get(field, []):
                hits.append({"kind": "GENE_ANNOTATION_FIELD", "gene_index": index,
                             "field": field, "value": value})
    for index, crossref in enumerate(reference["cross_references"]):
        properties = crossref["properties"]
        typed = sorted({p["key"] for p in properties if p["value"] == value})
        if crossref["id"] == value:
            hits.append({"kind": "CROSS_REFERENCE_PRIMARY_ID", "cross_reference_index": index,
                         "database": crossref["database"], "field": "id", "value": value,
                         "same_value_property_types": typed})
        for prop in properties:
            if prop["value"] == value:
                hits.append({"kind": "TYPED_CROSS_REFERENCE_PROPERTY", "cross_reference_index": index,
                             "database": crossref["database"], "field": prop["key"], "value": value})
    return hits


def match_summary(value, hits):
    """Field membership and identifier type are separate, nonexclusive facts."""
    return {
        "has_source_value": bool(value),
        "exact_reference_match": bool(hits),
        "gene_annotation_fields": sorted({h["field"] for h in hits
                                          if h["kind"] == "GENE_ANNOTATION_FIELD"}),
        "typed_cross_reference_properties": sorted({h["field"] for h in hits
                                                    if h["kind"] == "TYPED_CROSS_REFERENCE_PROPERTY"}),
        "primary_cross_reference_id_match": any(h["kind"] == "CROSS_REFERENCE_PRIMARY_ID" for h in hits),
        "experimental_identity_verified": False,
    }


def build_report(inventory_bytes, grounding_bytes, audit_bytes, rows, reviews):
    grounding, previous = json.loads(grounding_bytes), json.loads(audit_bytes)
    if digest(grounding_bytes) != previous["grounding_sha256"]:
        raise ValueError("historical UniProt snapshot checksum drift")
    if not (digest(inventory_bytes) == previous["source_inventory_sha256"]
            == grounding["source_inventory_sha256"]):
        raise ValueError("source inventory checksum drift")
    parsed = list(csv.DictReader(io.StringIO(inventory_bytes.decode()), delimiter="\t"))
    if rows != parsed:
        raise ValueError("source rows differ from pinned inventory")
    hashes = [row_digest(r) for r in rows]
    if len(set(hashes)) != len(rows) or set(reviews) - set(hashes):
        raise ValueError("duplicate source rows or unknown review rows")
    if len(previous["rows"]) != len(rows) or any(
        old["source"] != row for old, row in zip(previous["rows"], rows, strict=True)
    ):
        raise ValueError("historical audit source-row drift")
    references, output = {}, []
    for row, key in zip(rows, hashes, strict=True):
        value = row["gene_id"]
        if not value:
            continue
        accession = row["protein_accession"]
        entry = grounding["entries"].get(accession)
        if entry is None:
            raise ValueError(f"missing pinned reference: {accession}")
        reference = reference_projection(entry)
        if reference["accession"] != accession:
            raise ValueError("source accession is not the pinned primary accession")
        references[accession] = reference
        hits = identifier_matches(value, reference)
        review = reviews.get(key)
        disposition = {
            "review_id": review["review_id"] if review else None,
            "source_gene_id_withheld": bool(review and "gene_id" in review["withhold"]),
            "source_gene_id_rejected": bool(review and "gene_id" in review.get("misassigned", [])),
        }
        output.append({"source_row_sha256": key, "identifier": row["identifier"],
                       "reference": "PMID:" + row["pmid"], "source_gene_id": value,
                       "reference_accession": accession, "matches": hits,
                       "match_summary": match_summary(value, hits), "current_review": disposition})
    releases = sorted({v for req in grounding["requests"] for k, v in req["headers"].items()
                       if k.lower() == "x-uniprot-release"})
    summary = {
        "source_rows": len(rows), "empty_source_gene_ids": len(rows) - len(output),
        "nonempty_source_gene_ids": len(output), "reference_entries": len(references),
        "distinct_identifier_reference_pairs": len({
            (r["source_gene_id"], r["reference_accession"]) for r in output}),
        "gene_annotation_field_matches": sum(
            bool(r["match_summary"]["gene_annotation_fields"]) for r in output),
        "typed_property_matches": dict(Counter(
            p for r in output for p in r["match_summary"]["typed_cross_reference_properties"])),
        "primary_id_only_matches": sum(
            bool(r["matches"]) and all(h["kind"] == "CROSS_REFERENCE_PRIMARY_ID" for h in r["matches"])
            for r in output),
        "unmatched_source_values": sum(not r["matches"] for r in output),
        "already_rejected_source_gene_ids": sum(
            r["current_review"]["source_gene_id_rejected"] for r in output),
        "experimental_identifiers_assigned": 0,
    }
    return {
        "schema_version": 1, "scope": SCOPE, "summary": summary,
        "reference_releases": releases, "reference_entries": references, "rows": output,
        "attribution": {"source": "UniProt Consortium, UniProtKB metadata", "license": "CC BY 4.0",
                        "license_url": "https://www.uniprot.org/help/license"},
        "limitations": [
            "Exact string matching is case- and version-sensitive; "
            "no prefixes, suffixes or versions are removed.",
            "Gene-annotation field membership does not establish a database object's type "
            "or an experimental gene identity.",
            "Primary cross-reference IDs are not automatically gene IDs; "
            "untyped primary IDs remain untyped here.",
            "Typed properties and gene annotations can overlap; their counts are not exclusive categories.",
            "A rejected source reference is not rehabilitated by an identifier-field match.",
            "No source gene value, subject, allele, sequence, phenotype, measurement "
            "or curation decision is changed.",
            "This is a pinned-reference audit, not fresh primary review "
            "or current-release revalidation of all entries.",
            "No network, NCBI request, source adoption or GitHub mutation occurs in this audit.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grounding", type=Path, required=True)
    parser.add_argument("--historical-audit", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, default=Path("data/raw/phibase_amr.tsv"))
    parser.add_argument("--reviews", type=Path, default=Path("curation/phibase_grounding_reviews.json"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("refusing to overwrite an existing research artifact")
    payloads = {key: getattr(args, key).read_bytes() for key in
                ("grounding", "historical_audit", "inventory", "reviews")}
    rows = list(csv.DictReader(io.StringIO(payloads["inventory"].decode()), delimiter="\t"))
    reviews = load_reviews(args.inventory, rows, args.reviews)
    report = build_report(
        payloads["inventory"], payloads["grounding"], payloads["historical_audit"], rows, reviews)
    report["inputs"] = {key: {"path": str(getattr(args, key)), "sha256": digest(value)}
                        for key, value in payloads.items()}
    with args.output.open("x") as stream:
        stream.write(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
