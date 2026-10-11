"""Combine existing research stages without turning reference links into findings.

Offline, metadata-only output. Historical exports remain immutable. This is a
progress index, not another primary review or a replacement for paper dossiers.
"""

import argparse
import csv
import hashlib
import io
import json
from collections import Counter, defaultdict
from pathlib import Path

from discover_resistance_aliases import make_queries, record_names
from phibase_grounding_reviews import load_reviews, row_digest
from seed_from_sources import (
    is_card_sourced,
    is_hivdb_sourced_score_rule,
    is_phibase_sourced_resistance,
)

from antibioticmech.activity_collections import load_record

INPUTS = {
    "census": "research/2026-10-11-pr-integration-resistance-grounding.tsv",
    "name_plan": "research/2026-10-08-resistance-alias-discovery-plan.json",
    "initial_searches": "research/2026-10-08-resistance-alias-discovery-candidates.json",
    "expansion": "research/2026-10-09-resistance-discovery-date-sort.json",
    "expansion_plan": "research/2026-10-08-resistance-discovery-expansion-plan.json",
    "expanded_queries": "research/2026-10-09-resistance-discovery-date-sort-ledger.tsv",
    "card": "research/2026-10-07-card-reference-grounding.json",
    "card_ledger": "research/2026-10-07-card-reference-ledger.tsv",
    "card_inventory": "data/raw/aro_resistance_edges.tsv",
    "phi_inventory": "data/raw/phibase_amr.tsv",
    "phi_reviews": "curation/phibase_grounding_reviews.json",
    "hivdb": "research/2026-10-07-hivdb-reference-grounding.json",
    "hivdb_inventory": "data/raw/hivdb_algorithm_terms.tsv",
}
PREFIX = "research/2026-10-11-pr-integration-resistance-progress"
SCOPE = "PROGRESS_INDEX_NOT_PRIMARY_REVIEW_OR_EXPERIMENTAL_GROUNDING"
IDENTITY = ("identifier", "label", "path", "standard_inchi_key", "class")


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def index_unique(rows, key, context):
    result = {row[key]: row for row in rows}
    if len(result) != len(rows):
        raise ValueError(f"duplicate {context}")
    return result


def read_tsv(payload):
    return list(csv.DictReader(io.StringIO(payload.decode()), delimiter="\t"))


def same_identity(left, right, fields=IDENTITY):
    if any(left[key] != right[key] for key in fields):
        raise ValueError("record identity drift")


def current_records(root, census):
    snapshots = index_unique(census, "identifier", "census identifier")
    paths = {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
    if (not snapshots or paths != {r["path"] for r in snapshots.values()}
            or len(paths) != len(snapshots)):
        raise ValueError("corpus membership drift")
    records, documents = {}, {}
    for identifier, record in snapshots.items():
        path = root / record["path"]
        if digest(path.read_bytes()) != record["record_sha256"]:
            raise ValueError("census record checksum drift")
        doc = load_record(path)
        live = {"identifier": doc["identifier"], "label": doc["label"], "path": record["path"],
                "class": doc["antimicrobial_class"],
                "standard_inchi_key": doc["chemical_structure"]["standard_inchi_key"],
                "sha256": record["record_sha256"],
                "resistance_mechanisms": doc.get("resistance_mechanisms", []),
                "score_rules": doc.get("genotype_resistance_score_rules", []),
                "activity_count": len(doc.get("activity_spectrum", []))}
        same_identity(record, live, IDENTITY[:-1])
        if (len(live["resistance_mechanisms"]) != int(record["resistance_assertions"])
                or len(live["score_rules"]) != int(record["score_rules"])
                or live["activity_count"] != int(record["activity_observations"])):
            raise ValueError("census evidence drift")
        records[identifier] = live
        documents[identifier] = doc
    return records, documents


def discovery_progress(records, documents, plan, initial, expanded):
    planned = index_unique(plan["records"], "identifier", "planned identifier")
    searched = index_unique(initial["records"], "identifier", "searched identifier")
    if set(planned) != set(records) or set(searched) != set(records):
        raise ValueError("discovery record membership drift")
    if initial["corpus_sha256"] != plan["corpus_sha256"]:
        raise ValueError("historical discovery census drift")
    names = {i: record_names(doc) for i, doc in documents.items()}
    owners = defaultdict(list)
    for identifier, entries in names.items():
        for name in entries:
            owners[name["text"]].append(identifier)
    for identifier, entries in names.items():
        for name in entries:
            name["shared_with_record_ids"] = sorted(i for i in owners[name["text"]] if i != identifier)
    expansion = {}
    query_states = {}
    for row in expanded:
        key = (row["identifier"], row["query_id"])
        if key in expansion:
            raise ValueError("duplicate expanded query membership")
        if (row["status"] != "CURSOR_TRAVERSAL_COMPLETE"
                or row["primary_review_status"] != "PENDING"
                or int(row["hit_count"]) != int(row["retained_citations"])
                or int(row["hit_count"]) < 0 or int(row["pages"]) < 1):
            raise ValueError("incomplete or invalid expanded query")
        state = {k: v for k, v in row.items() if k not in ("identifier", "query_id")}
        if query_states.setdefault(row["query_key"], state) != state:
            raise ValueError("shared query state differs")
        expansion[key] = row
    result, expected_expansions = {}, set()
    for identifier, record in records.items():
        old, found = planned[identifier], searched[identifier]
        same_identity(record, old)
        same_identity(old, found, (*IDENTITY, "sha256"))
        queries = make_queries(names[identifier])
        if (old["names"] != names[identifier] or old["queries"] != queries
                or found["names"] != names[identifier]
                or len(found["queries"]) != len(queries)):
            raise ValueError("query name or provenance drift")
        if (found["search_status"] != "ALL_INITIAL_NAME_QUERIES_SEARCHED"
                or found["searched_queries"] != len(queries)
                or found["primary_review_status"] != "PENDING"):
            raise ValueError("initial searches incomplete or scope changed")
        expanded_count = 0
        for query, observation in zip(queries, found["queries"], strict=True):
            if any(observation[k] != v for k, v in query.items()):
                raise ValueError("initial query identity drift")
            count = observation["hit_count"]
            if type(count) is not int or count < 0:
                raise ValueError("invalid initial query count")
            status = ("NO_HITS_IN_LIMITED_QUERY" if count == 0 else
                      "TRUNCATED_REFINEMENT_REQUIRED" if count > 100 else "CANDIDATES_REQUIRE_REVIEW")
            if observation["status"] != status:
                raise ValueError("invalid initial query status")
            if count > 100:
                key = (identifier, query["query_id"])
                expected_expansions.add(key)
                if key not in expansion or expansion[key]["query_key"] != digest(query["query"].encode()):
                    raise ValueError("missing or mismatched expanded query")
                expanded_count += 1
        result[identifier] = {
            "recorded_names_searched": len(names[identifier]),
            "initial_query_memberships": len(queries),
            "expanded_query_memberships": expanded_count,
            "name_search_status": "RECORDED_NAME_QUERIES_TRAVERSED_NOT_PRIMARY_REVIEW",
            "record_changed_since_name_search": record["sha256"] != old["sha256"],
        }
    if set(expansion) != expected_expansions:
        raise ValueError("unexpected expanded query membership")
    return result


def card_progress(records, audit, ledger):
    membership = Counter()
    for row in ledger:
        if row["identifier"] not in records:
            raise ValueError("CARD record membership drift")
        same_identity(records[row["identifier"]], row, IDENTITY[:-1])
        membership[(row["identifier"], row["aro_id"], row["determinant_label"])] += 1
    current = Counter((i, m["aro_id"], m["label"]) for i, r in records.items()
                      for m in r["resistance_mechanisms"] if is_card_sourced(m))
    if membership != current:
        raise ValueError("CARD source assertion membership drift")
    used = set()
    result = {}
    for identifier, record in records.items():
        claims = [m for m in record["resistance_mechanisms"] if is_card_sourced(m)]
        terms = {m["aro_id"] for m in claims}
        used.update(terms)
        candidates, linked = {}, 0
        for term in sorted(terms):
            if term not in audit["determinants"]:
                raise ValueError("missing CARD determinant")
            item = audit["determinants"][term]
            if item["primary_review_status"] != "PENDING":
                raise ValueError("CARD primary review scope changed")
            linked += bool(item["candidates"])
            accessions = set()
            for candidate in item["candidates"]:
                accession = candidate["accession"]
                if (accession in accessions or not accession.startswith("UniProtKB:")
                        or candidate["card_cross_reference"]["database"] != "CARD"
                        or candidate["card_cross_reference"]["id"] != term
                        or candidate["evidence_scope"] !=
                        "EXPLICIT_REFERENCE_LINK_NOT_EXPERIMENTAL_ALLELE_GROUNDING"):
                    raise ValueError("invalid explicit CARD reference link")
                accessions.add(accession)
                taxon = candidate["reference_taxon_id"]
                if not taxon.startswith("NCBITaxon:") or candidates.setdefault(accession, taxon) != taxon:
                    raise ValueError("CARD reference taxonomy conflict")
        result[identifier] = {
            "card_source_assertions": len(claims), "card_distinct_terms": len(terms),
            "card_terms_with_reference_candidates": linked,
            "card_terms_without_explicit_reference_link": len(terms) - linked,
            "card_reference_accessions": "|".join(sorted(candidates)),
            "card_reference_taxids": "|".join(sorted(set(candidates.values()))),
        }
    if used != set(audit["determinants"]):
        raise ValueError("CARD determinant membership drift")
    if sum(r["card_source_assertions"] for r in result.values()) != audit["summary"]["card_assertions"]:
        raise ValueError("CARD assertion count drift")
    return result


def phi_progress(records, source_rows, reviews):
    grouped = defaultdict(list)
    for row in source_rows:
        if row["identifier"] not in records:
            raise ValueError("PHI-base record membership drift")
        grouped[row["identifier"]].append(row)
    result = {}
    for identifier, record in records.items():
        rows = grouped[identifier]
        claims = [m for m in record["resistance_mechanisms"] if is_phibase_sourced_resistance(m)]
        if len(claims) != len(rows):
            raise ValueError("PHI-base assertion count drift")
        reviewed = [reviews[row_digest(row)] for row in rows if row_digest(row) in reviews]
        result[identifier] = {
            "phi_source_associations": len(rows), "phi_identifier_scoped_associations": len(reviewed),
            "phi_identifier_review_pending": len(rows) - len(reviewed),
            "phi_identifier_review_ids": "|".join(sorted({r["review_id"] for r in reviewed})),
            "phi_identifier_review_pending_pmids": "|".join(sorted({
                "PMID:" + row["pmid"] for row in rows if row_digest(row) not in reviews})),
        }
    return result


def hivdb_progress(records, audit):
    grounded = index_unique(audit["records"], "identifier", "HIVDB record")
    expected, result = set(), {}
    for identifier, record in records.items():
        rules = [r for r in record["score_rules"] if is_hivdb_sourced_score_rule(r)]
        row = {"hivdb_source_rules": len(rules), "hivdb_reference_taxon": ""}
        if rules:
            expected.add(identifier)
            if identifier not in grounded:
                raise ValueError("missing HIVDB source grounding")
            item = grounded[identifier]
            same_identity(record, item, IDENTITY[:-1])
            if (Counter(r["source_rule_id"] for r in rules) != Counter(item["source_rule_ids"])
                    or dict(Counter(r["gene"] for r in rules)) != item["region_rule_counts"]
                    or item["primary_review_status"] != "PENDING"
                    or item["status"] != "SOURCE_REGION_AND_TAXON_VERIFIED_NOT_EXPERIMENTAL_ALLELES"):
                raise ValueError("HIVDB rule identity or scope drift")
            row["hivdb_reference_taxon"] = item["pathogen_taxon_id"]
        result[identifier] = row
    if expected != set(grounded):
        raise ValueError("HIVDB record membership drift")
    return result


def build(root):
    payloads = {k: (root / path).read_bytes() for k, path in INPUTS.items()}
    inputs = {k: {"path": path, "sha256": digest(payloads[k])} for k, path in INPUTS.items()}
    data = {k: json.loads(v) for k, v in payloads.items() if INPUTS[k].endswith(".json")}
    for kind in ("card", "hivdb"):
        if data[kind]["source_inventory_sha256"] != inputs[kind + "_inventory"]["sha256"]:
            raise ValueError(f"{kind} source inventory drift")
    if data["initial_searches"]["plan_sha256"] != inputs["name_plan"]["sha256"]:
        raise ValueError("initial search plan checksum drift")
    if data["expansion"]["ledger"] != inputs["expanded_queries"]:
        raise ValueError("expansion ledger checksum drift")
    if (data["expansion"]["plan"] != inputs["expansion_plan"]
            or data["expansion_plan"]["alias_plan_sha256"] != inputs["name_plan"]["sha256"]
            or data["expansion_plan"]["corpus_sha256"] != data["name_plan"]["corpus_sha256"]):
        raise ValueError("expansion historical census drift")
    records, documents = current_records(root, read_tsv(payloads["census"]))
    discovery = discovery_progress(records, documents, data["name_plan"], data["initial_searches"],
                                   read_tsv(payloads["expanded_queries"]))
    card = card_progress(records, data["card"], read_tsv(payloads["card_ledger"]))
    phi_rows = read_tsv(payloads["phi_inventory"])
    reviews = load_reviews(root / INPUTS["phi_inventory"], phi_rows, root / INPUTS["phi_reviews"])
    phi = phi_progress(records, phi_rows, reviews)
    hivdb = hivdb_progress(records, data["hivdb"])
    rows = []
    for identifier in sorted(records):
        record = records[identifier]
        rows.append({
            **{k: record[k] for k in IDENTITY}, "record_sha256": record["sha256"],
            "existing_resistance_assertions": len(record["resistance_mechanisms"]),
            "existing_genotype_rules": len(record["score_rules"]),
            **discovery[identifier], **card[identifier], **phi[identifier], **hivdb[identifier],
            "whole_record_primary_review": "OPEN",
        })
    if any(digest((root / r["path"]).read_bytes()) != r["sha256"] for r in records.values()):
        raise ValueError("record changed during progress audit")
    if {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")} != {
        r["path"] for r in records.values()
    }:
        raise ValueError("corpus membership changed during progress audit")
    if any((root / INPUTS[k]).read_bytes() != payload for k, payload in payloads.items()):
        raise ValueError("input changed during progress audit")
    counts = {k: sum(row[k] for row in rows) for k in (
        "existing_resistance_assertions", "existing_genotype_rules", "recorded_names_searched",
        "initial_query_memberships", "expanded_query_memberships", "card_source_assertions",
        "phi_source_associations", "phi_identifier_scoped_associations", "phi_identifier_review_pending",
        "hivdb_source_rules", "record_changed_since_name_search",
    )}
    summary = {
        "corpus_records": len(rows), **counts,
        "card_distinct_terms": len(data["card"]["determinants"]),
        "card_terms_with_reference_candidates": sum(bool(d["candidates"])
                                                    for d in data["card"]["determinants"].values()),
        "card_terms_without_explicit_reference_link": sum(not d["candidates"]
                                                         for d in data["card"]["determinants"].values()),
        "card_records_with_reference_candidates": sum(bool(r["card_reference_accessions"]) for r in rows),
        "expanded_distinct_queries": len({r["query_key"] for r in read_tsv(payloads["expanded_queries"])}),
        "whole_record_primary_reviews_completed": 0,
    }
    descriptor = {
        "schema_version": 1, "scope": SCOPE, "inputs": inputs, "summary": summary,
        "generator": {"path": "scripts/summarize_resistance_progress.py",
                      "sha256": digest(Path(__file__).read_bytes())},
        "reference_attribution": data["card"]["attribution"],
        "card_reference_releases": sorted({
            {k.lower(): v for k, v in request["headers"].items()}["x-uniprot-release"]
            for request in data["card"]["requests"]}),
        "limitations": [
            "This offline index summarizes existing exports, not a new primary-evidence review.",
            "Names and query provenance are checked against every current collection-loaded record.",
            "Completed traversals cover recorded query names only; no biological absence is inferred.",
            "Historical record hashes remain intact; current hashes are separately reported.",
            "CARD accessions and taxids are reference candidates, "
            "never experimental subject or allele assignments.",
            "Per-record CARD term counts overlap; use the global distinct-term count for corpus totals.",
            "PHI-base counts are source-row identifier decisions, "
            "not full phenotype review or independent experiments.",
            "HIVDB source rules and reference taxonomy are not measured resistance or allele assignments.",
            "Existing claim counts do not certify the claims, and no whole-record review is complete.",
            "Individual paper dossiers and other curator/reference mappings are not indexed here; "
            "consult the main report.",
            "No sequences, variant specifications, assay values or new biological claims are exported.",
            "No network requests, NCBI contact, source adoption, record edits or curation events occur.",
        ],
    }
    return rows, descriptor


def render(rows, descriptor):
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    tsv = buffer.getvalue().encode()
    descriptor = {**descriptor, "ledger": {"path": PREFIX + ".tsv", "sha256": digest(tsv)}}
    return tsv, (json.dumps(descriptor, indent=2, sort_keys=True) + "\n").encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify existing outputs without writing")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    rows, descriptor = build(root)
    for suffix, payload in zip((".tsv", ".json"), render(rows, descriptor), strict=True):
        path = root / (PREFIX + suffix)
        if args.check:
            if path.read_bytes() != payload:
                raise ValueError(f"progress export drift: {path}")
        else:
            path.write_bytes(payload)
    print(json.dumps(descriptor["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
