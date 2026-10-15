"""Ground all CARD cytochrome-b labels without assigning experimental alleles."""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlencode, urlsplit

import audit_card_beta_tubulin_references as shared
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

reference, native, taxa = shared.reference, shared.native, shared.taxa
require, names, protein_names = shared.require, shared.names, shared.protein_names
CACHE = Path("reports/resistance-grounding-2026-10-14-card-cytochrome-b")
OUTPUT = Path("research/2026-10-14-card-cytochrome-b-references.json")
COHORT_SHA = "2ce4b4ce1f1e1684c796d02fd58a87d0447ecffa2359e4d57f441ef4bfcdc36b"
SCOPE = "ALL_CARD_CYTOCHROME_B_PROTEIN_NAME_REFERENCES_NOT_EXPERIMENTAL_ALLELES"
SELECT = re.compile(r"\bcytochrome b\b|\bcytb\b", re.I)
NATIVE_NAME = re.compile(r"cytochrome b", re.I)
FIELDS = shared.FIELDS


def source_identity(label):
    match = re.fullmatch(r"(Colletotrichum [a-z]+) (cytochrome b protein) (.+)", label)
    require(match, "unreviewed cytochrome-b source syntax")
    return {
        "source_organism_name": match[1],
        "taxonomy_query_name": match[1],
        "source_protein_label": match[2],
        "source_gene_symbol": None,
        "source_claim_wording": match[3],
    }


def query_url(taxid, reviewed):
    require(type(taxid) is int and taxid > 0 and type(reviewed) is bool, "invalid protein query scope")
    return "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {
            "query": f'protein_name:"cytochrome b" AND taxonomy_id:{taxid} '
            f"AND reviewed:{str(reviewed).lower()}",
            "format": "json",
            "size": 500,
            "fields": FIELDS,
        }
    )


def validate_entry(entry, reviewed):
    # The existing validator checks metadata; its beta-specific name result is not reused.
    shared.validate_entry(entry, reviewed)
    return [n for n in protein_names(entry) if NATIVE_NAME.fullmatch(n["value"])]


def read_query(root, source, taxid, reviewed):
    require(source["url"] == query_url(taxid, reviewed), "protein query identity changed")
    body, provenance = native.read_source(root, source)
    entries = body["results"]
    require(
        len(entries) <= 500 and len({e["primaryAccession"] for e in entries}) == len(entries),
        "duplicate accessions or incomplete bounded query",
    )
    eligible, excluded = [], []
    for entry in entries:
        if validate_entry(entry, reviewed):
            eligible.append(entry)
        else:
            excluded.append(
                {
                    "protein_accession": "UniProtKB:" + entry["primaryAccession"],
                    "native_protein_names": protein_names(entry),
                    "reason": "NO_EXACT_NATIVE_CYTOCHROME_B_NAME_NOT_BIOLOGICAL_ABSENCE",
                }
            )
    return eligible, {
        "source": provenance,
        "source_taxon_id": taxid,
        "reviewed_subset": reviewed,
        "query_type": "PROTEIN_NAME_NOT_GENE_SYMBOL",
        "result_count": len(entries),
        "all_result_accessions": sorted(e["primaryAccession"] for e in entries),
        "candidate_accessions": sorted(e["primaryAccession"] for e in eligible),
        "candidate_count": len(eligible),
        "excluded_candidates": excluded,
        "complete_for_query": True,
        "zero_hit_is_biological_absence": False,
        "suggestions_followed": False,
        "suggestions_ignored": len(body.get("suggestions", [])),
    }


def read_queries(root, directory, cohort, named, reviewed, prior=None):
    filename = "reviewed-plan.json" if reviewed else "unreviewed-plan.json"
    plan = json.loads((directory / filename).read_bytes())
    expected = {
        name: row["selected_taxon"]
        for name, row in named.items()
        if row["selected_taxon"] and (reviewed or not prior[name][0])
    }
    require(
        plan["cohort"] == reference.pin(root, directory / "cohort.json")
        and set(plan["queries"]) == set(expected),
        "complete query plan changed",
    )
    result, used = {}, set()
    for name, selected in expected.items():
        taxid = int(selected["taxon_id"].split(":")[1])
        item = plan["queries"][name]
        key = item["request_key"]
        request = plan["requests"][key]
        require(
            request["name"] == name
            and request["source_taxon_id"] == taxid
            and request["reviewed"] is reviewed,
            "protein request scope changed",
        )
        if not reviewed:
            require(item["prior_reviewed_query"] == prior[name][1], "fallback evidence changed")
        source = planned_source(root, directory, key, filename, query_url(taxid, reviewed))
        result[name] = read_query(root, source, taxid, reviewed)
        used.add(key)
    require(used == set(plan["requests"]), "unbound protein request")
    return result


def selected_queries(root, directory, cohort, named):
    reviewed = read_queries(root, directory, cohort, named, True)
    unreviewed = read_queries(root, directory, cohort, named, False, reviewed)
    return {
        name: {
            "entries": unreviewed.get(name, value)[0],
            "reviewed": name not in unreviewed,
            "queries": {
                "reviewed": value[1],
                **({"unreviewed": unreviewed[name][1]} if name in unreviewed else {}),
            },
        }
        for name, value in reviewed.items()
    }


def project(entry, taxon, source_taxon, reviewed):
    matches = validate_entry(entry, reviewed)
    require(matches, "candidate lacks an exact native cytochrome-b name")
    require(
        taxon["taxonId"] == entry["organism"]["taxonId"]
        and taxon["active"] is True
        and taxon["scientificName"] == entry["organism"]["scientificName"],
        "protein organism does not match active native taxonomy",
    )
    nodes, species = shared.lineages.lineage(taxon)
    require(
        species == source_taxon["species_ancestor"]
        and source_taxon["rank"] == "species"
        and species["taxonId"] == int(source_taxon["taxon_id"].split(":")[1])
        and any(n["taxonId"] == 4751 and n["rank"] == "kingdom" for n in nodes),
        "candidate outside named fungal species",
    )
    position = next(i for i, n in enumerate(nodes) if n["taxonId"] == species["taxonId"])
    require(nodes[: position + 1] == source_taxon["lineage"], "candidate lineage conflict")
    genes = []
    for block in entry.get("genes", []):
        values = {}
        for field in ("geneName", "synonyms", "orderedLocusNames", "orfNames"):
            items = [block[field]] if field == "geneName" and field in block else block.get(field, [])
            values[field] = [v["value"] for v in items]
            require(
                all(isinstance(v, str) and v.strip() for v in values[field]), "invalid native gene metadata"
            )
        genes.append(values)
    bibliography = []
    for row in entry.get("references", []):
        citation = row.get("citation", {})
        identifiers = sorted(
            {
                (r["database"], r["id"])
                for r in citation.get("citationCrossReferences", [])
                if r["database"] in {"PubMed", "DOI"}
            }
        )
        if identifiers:
            bibliography.append(
                {
                    "identifiers": [{"database": db, "id": value} for db, value in identifiers],
                    "publication_date": citation.get("publicationDate"),
                    "identifier_issues": [
                        {
                            "database": db,
                            "native_id": value,
                            "status": "MALFORMED_NATIVE_DOI_NOT_CORRECTED",
                            "replacement": None,
                        }
                        for db, value in identifiers
                        if db == "DOI" and not re.fullmatch(r"10\.\d{4,9}/\S+", value)
                    ],
                    "primary_results_reviewed": False,
                }
            )
    return {
        "protein_accession": "UniProtKB:" + entry["primaryAccession"],
        "entry_version": entry["entryAudit"]["entryVersion"],
        "sequence_version": entry["entryAudit"]["sequenceVersion"],
        "entry_type": entry["entryType"],
        "native_protein_names": protein_names(entry),
        "native_cytochrome_b_name_matches": matches,
        "native_protein_flag": entry["proteinDescription"].get("flag"),
        "unflagged_means_complete": False,
        "native_gene_annotations": genes,
        "source_gene_symbol_assignment": None,
        "reference_organism_name": entry["organism"]["scientificName"],
        "reference_taxon_id": f"NCBITaxon:{taxon['taxonId']}",
        "reference_taxon_rank": taxon["rank"],
        "reference_species_taxon_id": f"NCBITaxon:{species['taxonId']}",
        "species_lineage_verified": True,
        "bibliography": bibliography,
        "bibliography_is_complete_reference_inventory": False,
        "experimental_subject_assignment": False,
        "exact_resistance_allele": False,
        "experimental_genome_assignment": None,
        "resistance_inferred_from_reference": False,
        "database_review_status_is_primary_results_review": False,
        "organelle_or_genomic_location_inferred_from_name": False,
        "fragment_coordinates_mapped_to_full_length": False,
    }


def check_scope(root, directory, cohort):
    for key in (
        "index",
        "census",
        "source_inventory",
        "source_queue",
        "definition_citations",
        "protected",
        "snapshot_artifacts",
        "taxonomy_cache_inventory",
        "query_cache_inventory",
        "prior_verification",
    ):
        reference.check_pin(root, cohort[key])
    index = json.loads((root / cohort["index"]["path"]).read_bytes())
    receipt = json.loads((root / cohort["prior_verification"]["path"]).read_bytes())
    require(
        cohort["index"] in receipt["files"] and receipt["summary"] == index["summary"],
        "index receipt changed",
    )
    citations = json.loads((root / cohort["definition_citations"]["path"]).read_bytes())["terms"]
    labels = {}
    for row in csv.DictReader((root / cohort["source_inventory"]["path"]).open(), delimiter="\t"):
        require(
            labels.setdefault(row["determinant_id"], row["determinant_name"]) == row["determinant_name"],
            "conflicting source labels",
        )
    expected = {tid for tid in index["terms"] if SELECT.search(labels[tid])}
    require(set(cohort["terms"]) == expected and len(expected) == 6, "complete source cohort changed")
    for tid, term in cohort["terms"].items():
        label, old = labels[tid], index["terms"][tid]
        require(
            all(term[k] == v for k, v in source_identity(label).items())
            and term["source_label"] == label
            and term["source_label_sha256"]
            == old["source_label_sha256"]
            == hashlib.sha256(label.encode()).hexdigest()
            and term["record_memberships"] == old["record_memberships"]
            and not old["links"]
            and term["definition_citation_ids"] == citations[tid]["definition_citation_ids"],
            "source identity, membership or citation changed",
        )
    census = list(csv.DictReader((root / cohort["census"]["path"]).open(), delimiter="\t"))
    require(
        len(census) == len({r["identifier"] for r in census}) == 2939
        and {r["path"] for r in census}
        == {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        and all(reference.digest(root / r["path"]) == r["record_sha256"] for r in census),
        "current corpus membership or bytes changed",
    )
    ids = {rid for t in cohort["terms"].values() for rid in t["record_memberships"]}
    require(cohort["records"] == [r for r in census if r["identifier"] in ids], "record coverage changed")
    for artifact in json.loads((root / cohort["snapshot_artifacts"]["path"]).read_bytes()):
        reference.check_pin(root, artifact["source"])
        reference.check_pin(root, artifact["snapshot"])
        require(artifact["source"]["sha256"] == artifact["snapshot"]["sha256"], "collection snapshot changed")
    claims = []
    for row in cohort["records"]:
        doc = load_record(root / row["path"])
        snapshot = directory / (row["identifier"].replace(":", "-") + "-before.yaml")
        require(
            reference.digest(snapshot) == row["record_sha256"]
            and doc == load_record(snapshot)
            and doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "complete record changed",
        )
        for position, claim in enumerate(doc.get("resistance_mechanisms", [])):
            if claim.get("aro_id") in expected:
                require(
                    claim["label"] == cohort["terms"][claim["aro_id"]]["source_label"],
                    "live source label changed",
                )
                claims.append(
                    {
                        "record_identifier": doc["identifier"],
                        "position": position,
                        "aro_id": claim["aro_id"],
                        "claim_sha256": hashlib.sha256(
                            json.dumps(claim, sort_keys=True, ensure_ascii=True).encode()
                        ).hexdigest(),
                    }
                )
    require(claims == cohort["claims"] and len(claims) == 6, "claim content or positions changed")


def build(root, directory=CACHE):
    directory = root / directory
    require(reference.digest(directory / "cohort.json") == COHORT_SHA, "frozen cohort changed")
    cohort = json.loads((directory / "cohort.json").read_bytes())
    check_scope(root, directory, cohort)
    canaries = {
        p: shared.shared.check_canary(root, directory, p)
        for p in ("names-plan.json", "reviewed-plan.json", "unreviewed-plan.json", "taxonomy-plan.json")
    }
    named = names(root, directory, cohort)
    selected = selected_queries(root, directory, cohort, named)
    plan = json.loads((directory / "taxonomy-plan.json").read_bytes())
    required = {str(e["organism"]["taxonId"]) for s in selected.values() for e in s["entries"]}
    require(
        set(plan["taxa"]) == required and plan["cohort"] == reference.pin(root, directory / "cohort.json"),
        "candidate taxonomy coverage changed",
    )
    reference.check_pin(root, plan["taxonomy_cache_inventory"])
    taxonomies, taxon_sources, used = {}, {}, set()
    for taxid, item in plan["taxa"].items():
        if "source" in item:
            source = item["source"]
        else:
            key = item["request_key"]
            source = planned_source(
                root, directory, key, "taxonomy-plan.json", f"https://rest.uniprot.org/taxonomy/{taxid}"
            )
            used.add(key)
        require(urlsplit(source["url"]).path.startswith("/taxonomy/"), "not native taxonomy")
        body, taxon_sources[taxid] = native.read_source(root, source)
        candidates = [n for n in body.get("results", [body]) if n["taxonId"] == int(taxid)]
        require(len(candidates) == 1, "candidate taxonomy identity changed")
        taxonomies[taxid] = candidates[0]
    require(used == set(plan["requests"]), "unbound taxonomy request")
    terms, proteins = {}, {}
    for tid, term in cohort["terms"].items():
        name = term["taxonomy_query_name"]
        source_taxon = named[name]["selected_taxon"]
        context = selected.get(name)
        candidates = []
        if context:
            for entry in context["entries"]:
                taxid = str(entry["organism"]["taxonId"])
                protein = project(entry, taxonomies[taxid], source_taxon, context["reviewed"])
                protein["taxonomy_source"] = taxon_sources[taxid]
                accession = protein["protein_accession"]
                require(proteins.setdefault(accession, protein) == protein, "reference identity conflict")
                candidates.append(
                    {
                        "protein_accession": accession,
                        "native_cytochrome_b_name_matches": protein["native_cytochrome_b_name_matches"],
                        "experimental_subject_assignment": False,
                        "exact_resistant_allele": False,
                    }
                )
        status = (
            "SOURCE_NAME_UNRESOLVED_NO_PROTEIN_QUERY"
            if not source_taxon
            else "NO_EXACT_NATIVE_NAME_CANDIDATES_NOT_ABSENCE"
            if not candidates
            else "MULTIPLE_CANDIDATES_NO_SELECTION"
            if len(candidates) > 1
            else "REVIEWED_REFERENCE"
            if context["reviewed"]
            else "UNREVIEWED_CANDIDATE"
        )
        terms[tid] = {
            **term,
            "named_reference_taxon_id": source_taxon["taxon_id"] if source_taxon else None,
            "queries": context["queries"] if context else {},
            "reference_candidates": candidates,
            "reference_status": status,
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
            "experimental_genome_assignment": None,
            "primary_review_status": "OPEN",
        }
    return {
        "date": cohort["date"],
        "scope": SCOPE,
        "release": "2026_03",
        "cohort": reference.pin(root, directory / "cohort.json"),
        "inputs": {
            k: cohort[k]
            for k in (
                "index",
                "census",
                "source_inventory",
                "source_queue",
                "definition_citations",
                "prior_verification",
            )
        },
        "canaries": canaries,
        "names": named,
        "terms": terms,
        "proteins": dict(sorted(proteins.items())),
        "records": cohort["records"],
        "claims": cohort["claims"],
        "summary": {
            "corpus_records_hash_checked": 2939,
            "source_terms": len(terms),
            "source_claims": len(cohort["claims"]),
            "complete_records_read": len(cohort["records"]),
            "source_name_contexts": len(named),
            "resolved_source_names": sum(bool(n["selected_taxon"]) for n in named.values()),
            "reference_proteins": len(proteins),
            "terms_with_references": sum(bool(t["reference_candidates"]) for t in terms.values()),
            "term_protein_links": sum(len(t["reference_candidates"]) for t in terms.values()),
            "reference_statuses": dict(
                sorted(Counter(t["reference_status"] for t in terms.values()).items())
            ),
            "entry_types": dict(sorted(Counter(p["entry_type"] for p in proteins.values()).items())),
            "fragment_references": sum(p["native_protein_flag"] == "Fragment" for p in proteins.values()),
            "terms_without_own_definition_citations": sum(
                not t["definition_citation_ids"] for t in terms.values()
            ),
            "bibliography_identifier_issue_memberships": sum(
                len(c["identifier_issues"]) for p in proteins.values() for c in p["bibliography"]
            ),
            "new_experimental_assignments": 0,
            "whole_record_primary_signoffs": 0,
        },
        "constraints": {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "primary_access_holds_preserved": True,
            "new_primary_requests": 0,
            "github_mutations": 0,
            "source_adoptions": 0,
            "outreach": 0,
            "biological_record_changes": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "interpretation": [
            "Protein names identify reference candidates, "
            "not exact source gene symbols or resistant alleles.",
            "All eligible candidates in the selected reviewed-first subsets are retained; "
            "zero results are not absence.",
            "Fragments are not assigned full-length coordinates; "
            "no sequence or organelle location is inferred.",
            "Bibliography identifiers are discovery metadata, "
            "not complete literature inventories or experimental evidence.",
            "No citation is borrowed from a neighboring term "
            "or from the distinct Magnaporthe PHI-base context.",
            "All records remain in the broader investigation; "
            "exact alleles, subjects, genomes and primary review remain open.",
        ],
        "attribution": "CARD curation team, ARO CC BY 4.0; UniProt Consortium, release 2026_03, CC BY 4.0.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        require(OUTPUT.read_bytes() == payload, "cytochrome-b checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
