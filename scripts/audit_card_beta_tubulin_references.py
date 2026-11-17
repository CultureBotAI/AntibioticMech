"""Replay beta-tubulin protein-name references without assigning resistance alleles."""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlencode, urlsplit

import audit_card_demethylase_references as shared
import audit_card_demethylase_taxa as taxa
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

reference, native, lineages = shared.reference, shared.native, shared.lineages
CACHE = Path("reports/resistance-grounding-2026-10-14-card-beta-tubulin")
OUTPUT = Path("research/2026-10-14-card-beta-tubulin-references.json")
COHORT_SHA = "a5a5d506aeb24faf95d9a15619f75ffec2fa7037979777cb6ae7984e6db950e7"
SCOPE = "ALL_CARD_BETA_TUBULIN_PROTEIN_NAME_REFERENCES_NOT_EXPERIMENTAL_ALLELES"
SELECT = re.compile(r"\bbeta[- ]tubulin\b", re.I)
FIELDS = shared.FIELDS
BETA_NAME = re.compile(
    r"(?:tubulin beta(?:[- ]\d+)?(?: chain)?|beta(?:[- ]\d+)?[- ]tubulin(?:[- ]\d+)?)", re.I
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def source_identity(label):
    match = re.fullmatch(r"([A-Za-z][a-z]+ [a-z]+) (beta[- ]tubulin) (.+)", label)
    require(match, "unsupported beta-tubulin source syntax")
    name = match[1]
    query_name = name[0].upper() + name[1:]
    return {
        "source_organism_name": name,
        "taxonomy_query_name": query_name,
        "name_normalization": "GENUS_INITIAL_CASE_ONLY" if name != query_name else "NONE",
        "source_protein_label": match[2],
        "source_gene_symbol": None,
        "source_claim_wording": match[3],
    }


def query_url(taxid, reviewed):
    require(type(taxid) is int and taxid > 0 and type(reviewed) is bool, "invalid protein query scope")
    return "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {
            "query": f'(protein_name:"tubulin beta" OR protein_name:"beta-tubulin") '
            f"AND taxonomy_id:{taxid} AND reviewed:{str(reviewed).lower()}",
            "format": "json",
            "size": 500,
            "fields": FIELDS,
        }
    )


def names(root, directory, cohort):
    plan = json.loads((directory / "names-plan.json").read_bytes())
    require(plan["cohort"] == reference.pin(root, directory / "cohort.json"), "name plan changed")
    require(
        set(cohort["names"]) == {t["taxonomy_query_name"] for t in cohort["terms"].values()},
        "source name coverage changed",
    )
    result, used = {}, set()
    for name, item in cohort["names"].items():
        if item["kind"] == "REUSED_EXACT_NATIVE_NAME":
            source = item["source"]
        else:
            require(item["kind"] == "NEW_EXACT_NATIVE_NAME", "unreviewed name retrieval kind")
            key = item["request_key"]
            require(plan["requests"][key]["name"] == name, "name request identity changed")
            source = planned_source(root, directory, key, "names-plan.json", taxa.query_url(name, "BINOMIAL"))
            used.add(key)
        require(urlsplit(source["url"]).path.startswith("/taxonomy/"), "not native taxonomy")
        body, provenance = native.read_source(root, source)
        resolved = taxa.resolve_name(body, name, "BINOMIAL")
        require(
            item["kind"] != "REUSED_EXACT_NATIVE_NAME" or resolved["selected_taxon"],
            "reused positive name no longer resolves",
        )
        result[name] = {**resolved, "source": provenance, "retrieval_kind": item["kind"]}
    require(used == set(plan["requests"]), "unbound name request")
    return result


def protein_names(entry):
    description = entry["proteinDescription"]
    result = []
    for kind in ("recommendedName", "alternativeNames", "submissionNames"):
        blocks = [description[kind]] if kind == "recommendedName" and kind in description else []
        if kind != "recommendedName":
            blocks = description.get(kind, [])
        for index, block in enumerate(blocks):
            name = block["fullName"]["value"]
            require(isinstance(name, str) and bool(name.strip()), "invalid native protein name")
            result.append({"kind": kind, "index": index, "value": name})
    require(result, "protein has no native name")
    return result


def validate_entry(entry, reviewed):
    expected = "UniProtKB reviewed (Swiss-Prot)" if reviewed else "UniProtKB unreviewed (TrEMBL)"
    require(type(reviewed) is bool and entry["entryType"] == expected, "review status changed")
    require(re.fullmatch(r"[A-Z0-9]+", entry["primaryAccession"]), "invalid protein accession")
    require(
        not {"sequence", "features", "comments"}.intersection(entry), "payload includes operational fields"
    )
    require(
        all(
            type(entry["entryAudit"].get(k)) is int and entry["entryAudit"][k] > 0
            for k in ("entryVersion", "sequenceVersion")
        ),
        "invalid reference versions",
    )
    require(
        type(entry["organism"]["taxonId"]) is int and entry["organism"]["taxonId"] > 0,
        "invalid reference taxon",
    )
    require(entry["proteinDescription"].get("flag") in (None, "Fragment"), "unreviewed protein flag")
    return [n for n in protein_names(entry) if BETA_NAME.fullmatch(n["value"])]


def read_query(root, source, taxid, reviewed):
    require(source["url"] == query_url(taxid, reviewed), "protein query identity changed")
    body, provenance = native.read_source(root, source)
    entries = body["results"]
    require(
        len(entries) <= 500 and len({e["primaryAccession"] for e in entries}) == len(entries),
        "query has duplicate accessions or exceeds complete bounded size",
    )
    selected, excluded = [], []
    for entry in entries:
        matches = validate_entry(entry, reviewed)
        if matches:
            selected.append(entry)
        else:
            excluded.append(
                {
                    "protein_accession": "UniProtKB:" + entry["primaryAccession"],
                    "native_protein_names": protein_names(entry),
                    "reason": "NO_TOP_LEVEL_NATIVE_BETA_TUBULIN_NAME_NOT_BIOLOGICAL_ABSENCE",
                }
            )
    return selected, {
        "source": provenance,
        "source_taxon_id": taxid,
        "reviewed_subset": reviewed,
        "query_type": "PROTEIN_NAME_NOT_GENE_SYMBOL",
        "result_count": len(entries),
        "all_result_accessions": sorted(e["primaryAccession"] for e in entries),
        "candidate_accessions": sorted(e["primaryAccession"] for e in selected),
        "candidate_count": len(selected),
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
        n: r["selected_taxon"]
        for n, r in named.items()
        if r["selected_taxon"] and (reviewed or not prior[n][0])
    }
    require(
        plan["cohort"] == reference.pin(root, directory / "cohort.json")
        and set(plan["queries"]) == set(expected),
        "protein plan coverage changed",
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
    require(matches, "candidate lacks a native beta-tubulin name")
    require(
        taxon["taxonId"] == entry["organism"]["taxonId"] and taxon["active"] is True,
        "protein does not match active native taxonomy",
    )
    nodes, species = lineages.lineage(taxon)
    require(
        species == source_taxon["species_ancestor"]
        and source_taxon["rank"] == "species"
        and species["taxonId"] == int(source_taxon["taxon_id"].split(":")[1])
        and any(n["taxonId"] == 4751 and n["rank"] == "kingdom" for n in nodes),
        "candidate is outside named fungal species scope",
    )
    position = next(i for i, n in enumerate(nodes) if n["taxonId"] == species["taxonId"])
    require(nodes[: position + 1] == source_taxon["lineage"], "candidate lineage conflicts with source name")
    blocks = []
    for block in entry.get("genes", []):
        values = {}
        for field in ("geneName", "synonyms", "orderedLocusNames", "orfNames"):
            items = [block[field]] if field == "geneName" and field in block else block.get(field, [])
            values[field] = [v["value"] for v in items]
            require(all(isinstance(v, str) and v.strip() for v in values[field]), "invalid gene metadata")
        blocks.append(values)
    citations = []
    for ref in entry.get("references", []):
        citation = ref.get("citation", {})
        identifiers = sorted(
            {
                (r["database"], r["id"])
                for r in citation.get("citationCrossReferences", [])
                if r["database"] in {"PubMed", "DOI"}
            }
        )
        if identifiers:
            citations.append(
                {
                    "identifiers": [{"database": db, "id": value} for db, value in identifiers],
                    "publication_date": citation.get("publicationDate"),
                    "primary_results_reviewed": False,
                }
            )
    return {
        "protein_accession": "UniProtKB:" + entry["primaryAccession"],
        "entry_version": entry["entryAudit"]["entryVersion"],
        "sequence_version": entry["entryAudit"]["sequenceVersion"],
        "entry_type": entry["entryType"],
        "native_protein_names": protein_names(entry),
        "native_beta_name_matches": matches,
        "native_protein_flag": entry["proteinDescription"].get("flag"),
        "unflagged_means_complete": False,
        "native_gene_annotations": blocks,
        "source_gene_symbol_assignment": None,
        "reference_organism_name": entry["organism"]["scientificName"],
        "reference_taxon_id": f"NCBITaxon:{taxon['taxonId']}",
        "reference_taxon_rank": taxon["rank"],
        "reference_taxon_scientific_name": taxon["scientificName"],
        "reference_species_taxon_id": f"NCBITaxon:{species['taxonId']}",
        "species_lineage_verified": True,
        "bibliography": citations,
        "experimental_subject_assignment": False,
        "exact_resistance_allele": False,
        "experimental_genome_assignment": None,
        "resistance_inferred_from_reference": False,
        "database_review_status_is_primary_results_review": False,
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
    citations = json.loads((root / cohort["definition_citations"]["path"]).read_bytes())["terms"]
    receipt = json.loads((root / cohort["prior_verification"]["path"]).read_bytes())
    require(
        cohort["index"] in receipt["files"] and receipt["summary"] == index["summary"],
        "prior all-record checkpoint receipt changed",
    )
    labels = {}
    for row in csv.DictReader((root / cohort["source_inventory"]["path"]).open(), delimiter="\t"):
        require(
            labels.setdefault(row["determinant_id"], row["determinant_name"]) == row["determinant_name"],
            "conflicting source labels",
        )
    expected = {t for t in index["terms"] if SELECT.search(labels[t])}
    require(set(cohort["terms"]) == expected and len(expected) == 15, "full beta-tubulin cohort changed")
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
    ids = {i for t in cohort["terms"].values() for i in t["record_memberships"]}
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
            "complete record snapshot changed",
        )
        for position, claim in enumerate(doc.get("resistance_mechanisms", [])):
            if claim.get("aro_id") in expected:
                require(
                    claim["label"] == cohort["terms"][claim["aro_id"]]["source_label"],
                    "live claim label changed",
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
    require(claims == cohort["claims"] and len(claims) == 15, "claim hashes or positions changed")
    require(
        cohort["fields"] == FIELDS
        and cohort["query_policy"]
        == "COMPLETE_REVIEWED_PROTEIN_NAME_QUERY_THEN_UNREVIEWED_IF_NO_NATIVE_BETA_MATCH",
        "query scope changed",
    )


def build(root, directory=CACHE):
    directory = root / directory
    require(reference.digest(directory / "cohort.json") == COHORT_SHA, "frozen cohort changed")
    cohort = json.loads((directory / "cohort.json").read_bytes())
    check_scope(root, directory, cohort)
    canaries = {
        p: shared.check_canary(root, directory, p)
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
        require(urlsplit(source["url"]).path.startswith("/taxonomy/"), "candidate source is not taxonomy")
        body, taxon_sources[taxid] = native.read_source(root, source)
        candidates = [n for n in body.get("results", [body]) if n["taxonId"] == int(taxid)]
        require(len(candidates) == 1, "candidate taxonomy identity changed")
        taxonomies[taxid] = candidates[0]
    require(used == set(plan["requests"]), "unbound candidate taxonomy request")
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
                require(proteins.setdefault(accession, protein) == protein, "conflicting reference identity")
                candidates.append(
                    {
                        "protein_accession": accession,
                        "native_beta_name_matches": protein["native_beta_name_matches"],
                        "experimental_subject_assignment": False,
                        "exact_resistant_allele": False,
                    }
                )
        status = (
            "SOURCE_NAME_UNRESOLVED_NO_PROTEIN_QUERY"
            if not source_taxon
            else "NO_NATIVE_BETA_NAME_CANDIDATES_NOT_ABSENCE"
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
            "named_reference_taxon_rank": source_taxon["rank"] if source_taxon else None,
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
            "complete_records_read": len(cohort["records"]),
            "source_claims": len(cohort["claims"]),
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
            "new_experimental_assignments": 0,
            "whole_record_primary_signoffs": 0,
        },
        "interpretation": [
            "Protein-name references preserve native gene annotations "
            "but do not assign a source gene symbol.",
            "All candidates in the selected query subsets are retained, including fragments; "
            "no paralog equivalence or representative selection is inferred.",
            "Reviewed status is database curation, not primary resistance evidence.",
            "The case-only normalization does not correct source spelling or alter source-owned records.",
            "Empty queries are not absence; exact resistant alleles, subjects, genomes "
            "and compound-specific causality remain open.",
            "A neighboring term's citation is not transferred to a term lacking its own definition citation.",
        ],
        "constraints": {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "primary_access_holds_preserved": True,
            "new_primary_requests": 0,
            "github_mutations": 0,
            "source_adoptions": 0,
            "outreach": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": "CARD curation team, ARO CC BY 4.0; UniProt Consortium, release 2026_03, CC BY 4.0.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        require(OUTPUT.read_bytes() == payload, "beta-tubulin checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
