"""Replay the complete CARD folP cohort without assigning tested resistance alleles."""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlencode, urlsplit

import audit_card_demethylase_references as genes
import audit_card_reference_lineages as lineages
import audit_fungamr_cohort as native
import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-card-folp")
OUTPUT = Path("research/2026-10-14-card-folp-references.json")
COHORT_SHA = "b4b711435a627de83976e52189c3c3c5fa238ed44806dbca7ac497f6d614a885"
SCOPE = "ALL_CARD_FOLP_REFERENCE_CONTEXTS_NOT_EXPERIMENTAL_ALLELES_OR_PHENOTYPES"
SELECT = re.compile(r"\bfolP\d*\b|dihydropteroate", re.I)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def name_url(name):
    require(re.fullmatch(r"[A-Z][a-z]+ [a-z]+", name), "unsupported source-name syntax")
    return "https://rest.uniprot.org/taxonomy/search?" + urlencode(
        {"query": '"' + name + '"', "format": "json", "size": 500}
    )


def gene_url(taxid, reviewed):
    require(type(taxid) is int and taxid > 0 and type(reviewed) is bool, "invalid gene query scope")
    return "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {
            "query": f"gene_exact:folP AND taxonomy_id:{taxid} AND reviewed:{str(reviewed).lower()}",
            "format": "json",
            "size": 500,
            "fields": genes.FIELDS,
        }
    )


def resolve_name(payload, name):
    candidates, selected, seen = [], [], set()
    for taxon in payload.get("results", [payload]):
        identity = lineages.identity(taxon)
        require(
            identity["taxonId"] not in seen and type(taxon.get("active")) is bool, "invalid name response"
        )
        seen.add(identity["taxonId"])
        for field in ("synonyms", "otherNames"):
            require(
                isinstance(taxon.get(field, []), list)
                and all(isinstance(v, str) for v in taxon.get(field, [])),
                "invalid native names",
            )
        fields = ["scientificName"] if taxon["scientificName"] == name else []
        if name in taxon.get("synonyms", []):
            fields.append("synonyms")
        row = {
            "taxon_id": f"NCBITaxon:{identity['taxonId']}",
            "scientific_name": identity["scientificName"],
            "rank": identity["rank"],
            "active": taxon["active"],
            "matching_fields": fields,
            "other_name_match_only": not fields and name in taxon.get("otherNames", []),
        }
        candidates.append(row)
        if fields and taxon["active"] is True:
            nodes, species = lineages.lineage(taxon)
            require(
                species and any(n["taxonId"] == 2 for n in nodes),
                "source name lacks bacterial species ancestry",
            )
            selected.append(
                {
                    **row,
                    "lineage": nodes,
                    "species_ancestor": species,
                    "experimental_subject_assignment": False,
                }
            )
    return {
        "source_name": name,
        "candidates": candidates,
        "selected_taxon": selected[0] if len(selected) == 1 else None,
        "status": "EXACT_NATIVE_NAME_REFERENCE"
        if len(selected) == 1
        else "AMBIGUOUS_NATIVE_NAME"
        if selected
        else "NO_EXACT_ACTIVE_NATIVE_NAME",
        "experimental_subject_assignment": False,
        "unresolved_name_is_absence": False,
    }


def names(root, directory, cohort):
    plan = json.loads((directory / "names-plan.json").read_bytes())
    require(plan["cohort"] == reference.pin(root, directory / "cohort.json"), "name plan cohort changed")
    expected = {t["source_organism_name"] for t in cohort["terms"].values()}
    require(set(cohort["names"]) == expected, "source name coverage changed")
    result, used = {}, set()
    for name, item in cohort["names"].items():
        if item["kind"] == "REUSED_EXACT_NATIVE_NAME":
            source = item["source"]
        else:
            require(item["kind"] == "NEW_EXACT_NAME_ALL_RANKS", "unknown name retrieval kind")
            key = item["request_key"]
            require(plan["requests"][key]["name"] == name, "planned name changed")
            source = planned_source(root, directory, key, "names-plan.json", name_url(name))
            used.add(key)
        require(urlsplit(source["url"]).path.startswith("/taxonomy/"), "name source is not native taxonomy")
        body, provenance = native.read_source(root, source)
        resolved = resolve_name(body, name)
        require(
            item["kind"] != "REUSED_EXACT_NATIVE_NAME" or resolved["selected_taxon"],
            "reused positive name no longer resolves",
        )
        result[name] = {**resolved, "source": provenance, "retrieval_kind": item["kind"]}
    require(used == set(plan["requests"]), "name request coverage changed")
    return result


def read_gene(root, source, taxid, reviewed):
    require(source["url"] == gene_url(taxid, reviewed), "gene query identity changed")
    body, provenance = native.read_source(root, source)
    entries = body["results"]
    genes.validate_entries(entries, "folp", reviewed)
    for entry in entries:
        genes.gene_identity(entry, "folp")
    return entries, {
        "source": provenance,
        "source_taxon_id": taxid,
        "gene": "folP",
        "reviewed_subset": reviewed,
        "accessions": sorted(e["primaryAccession"] for e in entries),
        "result_count": len(entries),
        "complete_for_query": True,
        "zero_hit_is_biological_absence": False,
        "suggestions_followed": False,
        "suggestions_ignored": len(body.get("suggestions", [])),
    }


def read_queries(root, directory, selected_names, reviewed, prior_queries=None):
    filename = "reviewed-plan.json" if reviewed else "unreviewed-plan.json"
    plan = json.loads((directory / filename).read_bytes())
    expected = {
        name: row["selected_taxon"]
        for name, row in selected_names.items()
        if row["selected_taxon"] and (reviewed or not prior_queries[name][1]["accessions"])
    }
    require(
        plan["cohort"] == reference.pin(root, directory / "cohort.json")
        and set(plan["queries"]) == set(expected),
        "gene query plan coverage changed",
    )
    result, used = {}, set()
    for name, taxon in expected.items():
        taxid = int(taxon["taxon_id"].split(":")[1])
        item = plan["queries"][name]
        key = item["request_key"]
        require(
            item["source_taxon_id"] == taxid and item["reviewed"] is reviewed and item["gene"] == "folP",
            "planned gene identity changed",
        )
        if not reviewed:
            require(
                item["prior_reviewed_query"] == prior_queries[name][1], "fallback prior query binding changed"
            )
        request = plan["requests"][key]
        require(
            request["name"] == name
            and request["source_taxon_id"] == taxid
            and request["reviewed"] is reviewed,
            "gene request scope changed",
        )
        source = planned_source(root, directory, key, filename, gene_url(taxid, reviewed))
        result[name] = read_gene(root, source, taxid, reviewed)
        used.add(key)
    require(used == set(plan["requests"]), "unbound planned gene request")
    return result


def selected_queries(root, directory, selected_names):
    reviewed = read_queries(root, directory, selected_names, True)
    unreviewed = read_queries(root, directory, selected_names, False, reviewed)
    return {
        name: {
            "entries": unreviewed.get(name, value)[0],
            "queries": {
                "reviewed": value[1],
                **({"unreviewed": unreviewed[name][1]} if name in unreviewed else {}),
            },
            "reviewed": name not in unreviewed,
        }
        for name, value in reviewed.items()
    }


def project(entry, taxon, source_taxon, reviewed):
    genes.validate_entries([entry], "folp", reviewed)
    nodes, species = lineages.lineage(taxon)
    require(
        species
        and any(n["taxonId"] == 2 for n in nodes)
        and any(n["taxonId"] == int(source_taxon["taxon_id"].split(":")[1]) for n in nodes),
        "candidate is outside the named taxon scope",
    )
    source_id = int(source_taxon["taxon_id"].split(":")[1])
    end = next(i for i, n in enumerate(nodes) if n["taxonId"] == source_id)
    require(
        nodes[: end + 1] == source_taxon["lineage"] and species == source_taxon["species_ancestor"],
        "candidate lineage conflicts with independently resolved source name",
    )
    require(entry["proteinDescription"].get("flag") in (None, "Fragment"), "unreviewed protein flag")
    protein = reference.project_reference(entry, "folp", species["taxonId"], taxon, reviewed=reviewed)
    blocks, matches = genes.gene_identity(entry, "folp")
    protein.update(
        {
            "genes": blocks,
            "native_protein_flag": entry["proteinDescription"].get("flag"),
            "unflagged_means_complete": False,
            "experimental_genome_assignment": None,
            "database_review_status_is_primary_results_review": False,
            "resistance_inferred_from_reference": False,
            "reference_organism_label_matches_taxonomy": entry["organism"]["scientificName"]
            == taxon["scientificName"],
        }
    )
    protein["reference_species_taxon_id"] = protein.pop("source_species_taxon_id")
    return protein, matches


def check_sources(root, directory, cohort):
    for key in (
        "index",
        "census",
        "source_inventory",
        "source_queue",
        "definition_citations",
        "prior_ecoli",
        "protected",
        "taxonomy_cache_inventory",
        "query_cache_inventory",
        "prior_verification",
    ):
        reference.check_pin(root, cohort[key])
    index = json.loads((root / cohort["index"]["path"]).read_bytes())
    citations = json.loads((root / cohort["definition_citations"]["path"]).read_bytes())
    labels = {}
    with (root / cohort["source_inventory"]["path"]).open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            tid, label = row["determinant_id"], row["determinant_name"]
            require(labels.setdefault(tid, label) == label, "conflicting source labels")
    expected = {t for t in index["terms"] if SELECT.search(labels[t])}
    require(set(cohort["terms"]) == expected, "full folP source selection changed")
    for tid, term in cohort["terms"].items():
        match = re.fullmatch(r"([A-Z][a-z]+ [a-z]+) (folP) (.+)", labels[tid])
        require(
            match
            and term["source_label"] == labels[tid]
            and [term[k] for k in ("source_organism_name", "source_gene_label", "source_claim_wording")]
            == list(match.groups())
            and term["source_label_sha256"]
            == index["terms"][tid]["source_label_sha256"]
            == hashlib.sha256(labels[tid].encode()).hexdigest()
            and term["record_memberships"] == index["terms"][tid]["record_memberships"]
            and term["definition_citation_ids"] == citations["terms"][tid]["definition_citation_ids"],
            "source term identity changed",
        )
    with (root / cohort["census"]["path"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    require(
        len(census) == len({r["identifier"] for r in census}) == 2939
        and {r["path"] for r in census}
        == {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        and all(reference.digest(root / r["path"]) == r["record_sha256"] for r in census),
        "corpus census changed",
    )
    ids = {rid for t in cohort["terms"].values() for rid in t["record_memberships"]}
    require([r for r in census if r["identifier"] in ids] == cohort["records"], "selected records changed")
    claims = []
    for row in cohort["records"]:
        doc = load_record(root / row["path"])
        snapshot = directory / (row["identifier"].replace(":", "-") + "-before.yaml")
        require(
            doc == load_record(snapshot)
            and reference.digest(snapshot) == row["record_sha256"]
            and doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "selected record identity changed",
        )
        for position, claim in enumerate(doc.get("resistance_mechanisms", [])):
            if claim.get("aro_id") in expected:
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
    require(
        claims == cohort["claims"] and len(claims) == 21 and len(ids) == 10,
        "source claim positions or content changed",
    )


def build(root, directory=CACHE):
    directory = root / directory
    cohort_path = directory / "cohort.json"
    require(reference.digest(cohort_path) == COHORT_SHA, "frozen folP cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    check_sources(root, directory, cohort)
    canaries = {
        p: genes.check_canary(root, directory, p)
        for p in ("names-plan.json", "reviewed-plan.json", "unreviewed-plan.json", "taxonomy-plan.json")
    }
    selected_names = names(root, directory, cohort)
    selection = selected_queries(root, directory, selected_names)
    plan = json.loads((directory / "taxonomy-plan.json").read_bytes())
    required = {str(e["organism"]["taxonId"]) for c in selection.values() for e in c["entries"]}
    require(
        set(plan["taxa"]) == required and plan["cohort"] == reference.pin(root, cohort_path),
        "candidate taxonomy coverage changed",
    )
    reference.check_pin(root, plan["taxonomy_cache_inventory"])
    taxa, sources, used = {}, {}, set()
    for taxid, item in plan["taxa"].items():
        if "source" in item:
            source = item["source"]
        else:
            key = item["request_key"]
            source = planned_source(
                root, directory, key, "taxonomy-plan.json", f"https://rest.uniprot.org/taxonomy/{taxid}"
            )
            used.add(key)
        require(
            urlsplit(source["url"]).path.startswith("/taxonomy/"), "candidate source is not native taxonomy"
        )
        body, sources[taxid] = native.read_source(root, source)
        candidates = [n for n in body.get("results", [body]) if n["taxonId"] == int(taxid)]
        require(len(candidates) == 1, "candidate taxonomy identity changed")
        taxa[taxid] = candidates[0]
        lineages.lineage(candidates[0])
    require(used == set(plan["requests"]), "candidate taxonomy requests changed")
    terms, proteins = {}, {}
    for tid, term in cohort["terms"].items():
        name = term["source_organism_name"]
        named = selected_names[name]["selected_taxon"]
        chosen = selection.get(name)
        candidates = []
        if chosen:
            for entry in chosen["entries"]:
                protein, matches = project(
                    entry, taxa[str(entry["organism"]["taxonId"])], named, chosen["reviewed"]
                )
                accession = protein["protein_accession"]
                require(proteins.setdefault(accession, protein) == protein, "conflicting candidate metadata")
                candidates.append(
                    {
                        "protein_accession": accession,
                        "native_gene_field_matches": matches,
                        "experimental_subject_assignment": False,
                        "exact_resistant_allele": False,
                    }
                )
        status = (
            "SOURCE_NAME_UNRESOLVED_NO_PROTEIN_QUERY"
            if chosen is None
            else "NO_EXACT_GENE_RESULTS_NOT_ABSENCE"
            if not candidates
            else "MULTIPLE_CANDIDATES_NO_SELECTION"
            if len(candidates) > 1
            else "REVIEWED_REFERENCE"
            if chosen["reviewed"]
            else "UNREVIEWED_CANDIDATE"
        )
        terms[tid] = {
            **term,
            "named_reference_taxon_id": named["taxon_id"] if named else None,
            "named_reference_taxon_rank": named["rank"] if named else None,
            "source_species_ancestor": named["species_ancestor"] if named else None,
            "reference_status": status,
            "queries": chosen["queries"] if chosen else {},
            "reference_candidates": sorted(candidates, key=lambda c: c["protein_accession"]),
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
            "experimental_genome_assignment": None,
            "primary_review_status": "OPEN",
        }
    return {
        "date": "2026-10-14",
        "scope": SCOPE,
        "release": "2026_03",
        "inputs": {
            **{
                k: cohort[k]
                for k in (
                    "index",
                    "census",
                    "source_inventory",
                    "definition_citations",
                    "prior_ecoli",
                    "taxonomy_cache_inventory",
                    "query_cache_inventory",
                )
            },
            "cohort": reference.pin(root, cohort_path),
            "plans": {p: reference.pin(root, directory / p) for p in canaries},
            "canaries": canaries,
            "taxonomy_sources": sources,
        },
        "terms": terms,
        "names": selected_names,
        "proteins": dict(sorted(proteins.items())),
        "records": cohort["records"],
        "claims": cohort["claims"],
        "summary": {
            "corpus_records_hash_checked": 2939,
            "source_terms": len(terms),
            "source_assertions": len(cohort["claims"]),
            "source_records": len(cohort["records"]),
            "source_names": len(selected_names),
            "resolved_source_names": sum(bool(n["selected_taxon"]) for n in selected_names.values()),
            "reference_proteins": len(proteins),
            "reference_taxa": len(taxa),
            "terms_with_candidates": sum(bool(t["reference_candidates"]) for t in terms.values()),
            "term_status_counts": dict(Counter(t["reference_status"] for t in terms.values())),
            "native_protein_flags": dict(Counter(str(p["native_protein_flag"]) for p in proteins.values())),
            "biological_records_changed": 0,
            "experimental_assignments": 0,
            "whole_record_primary_signoffs": 0,
        },
        "limits": [
            "The exact folP query admits native gene-name or synonym matches; "
            "no missing alias or spelling correction is inferred.",
            "Native taxon ranks are preserved; "
            "a below-species name is not broadened to its species ancestor.",
            "Reference genes, bibliography and taxonomy are not tested alleles, "
            "genomes or phenotype evidence.",
            "All candidates and empty queries are retained; zero hits do not establish biological absence.",
            "Prior E. coli primary findings remain separate; "
            "source definition citations are not newly validated.",
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
        require(OUTPUT.read_bytes() == payload, "folP checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
