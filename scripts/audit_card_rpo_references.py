"""Replay all CARD rpoB/rpoC reference contexts without assigning resistance alleles."""

import argparse
import csv
import gzip
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from urllib.parse import urlencode, urlsplit

import audit_card_folp_references as shared
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

genes, lineages, native, reference = shared.genes, shared.lineages, shared.native, shared.reference
require, resolve_name = shared.require, shared.resolve_name
CACHE = Path("reports/resistance-grounding-2026-10-14-card-rpo")
OUTPUT = Path("research/2026-10-14-card-rpo-references.json")
COHORT_SHA = "7078bc16f498f0ac65d3f1d3e6c603ae814bbb14a74b940087c413b69a9385d1"
SCOPE = "ALL_CARD_RPO_REFERENCE_CONTEXTS_NOT_EXPERIMENTAL_ALLELES_OR_PHENOTYPES"
SELECT = re.compile(r"\brpo[BC]\b|RNA polymerase", re.I)


def source_identity(tid, label, definitions, bibliography):
    match = re.match(r"([A-Z][a-z]+ [a-z]+) (rpo[BC])\b", label)
    tokens = re.findall(r"\brpo[BC]\b", label)
    require(len(tokens) == 1, "ambiguous or absent source gene")
    if match:
        return match[1], tokens[0], "SOURCE_LABEL"
    if tid == "ARO:3003090":
        require(
            "Known from S. aureus." in definitions[tid]
            and bibliography["20837752"]["pmid"] == "20837752"
            and "Staphylococcus aureus" in bibliography["20837752"]["title"],
            "definition abbreviation lacks cited-title support",
        )
        return "Staphylococcus aureus", tokens[0], "DEFINITION_ABBREVIATION_AND_CITED_TITLE"
    return None, tokens[0], "UNRESOLVED_NO_NAME"


def names(root, directory, cohort):
    named = {k: t for k, t in cohort["terms"].items() if t["source_organism_name"] is not None}
    return shared.names(root, directory, {**cohort, "terms": named})


def contexts(cohort, selected_names):
    result = {}
    for term in cohort["terms"].values():
        name, gene = term["source_organism_name"], term["source_gene_label"]
        if name is None or not selected_names[name]["selected_taxon"]:
            continue
        result[f"{name}|{gene}"] = {
            "name": name,
            "gene": gene,
            "source_taxon_id": int(selected_names[name]["selected_taxon"]["taxon_id"].split(":")[1]),
        }
    return dict(sorted(result.items()))


def gene_url(taxid, gene, reviewed):
    require(
        type(taxid) is int and taxid > 0 and type(reviewed) is bool and gene in ("rpoB", "rpoC"),
        "invalid rpo query scope",
    )
    return "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {
            "query": f"gene_exact:{gene} AND taxonomy_id:{taxid} AND reviewed:{str(reviewed).lower()}",
            "format": "json",
            "size": 500,
            "fields": genes.FIELDS,
        }
    )


def read_gene(root, source, taxid, gene, reviewed):
    require(source["url"] == gene_url(taxid, gene, reviewed), "gene query identity changed")
    body, provenance = native.read_source(root, source)
    entries = body["results"]
    genes.validate_entries(entries, gene.casefold(), reviewed)
    for entry in entries:
        genes.gene_identity(entry, gene.casefold())
    return entries, {
        "source": provenance,
        "source_taxon_id": taxid,
        "gene": gene,
        "reviewed_subset": reviewed,
        "accessions": sorted(e["primaryAccession"] for e in entries),
        "result_count": len(entries),
        "complete_for_query": True,
        "zero_hit_is_biological_absence": False,
        "suggestions_followed": False,
        "suggestions_ignored": len(body.get("suggestions", [])),
    }


def read_queries(root, directory, cohort, selected_names, reviewed, prior=None):
    filename = "reviewed-plan.json" if reviewed else "unreviewed-plan.json"
    plan = json.loads((directory / filename).read_bytes())
    expected = {k: c for k, c in contexts(cohort, selected_names).items() if reviewed or not prior[k][0]}
    require(
        plan["cohort"] == reference.pin(root, directory / "cohort.json")
        and set(plan["queries"]) == set(expected),
        "gene plan coverage changed",
    )
    result, used = {}, set()
    for key, context in expected.items():
        item = plan["queries"][key]
        request_key = item["request_key"]
        request = plan["requests"][request_key]
        require(
            all(request[k] == v for k, v in context.items())
            and request["context"] == key
            and request["reviewed"] is reviewed,
            "gene request context changed",
        )
        if not reviewed:
            require(item["prior_reviewed_query"] == prior[key][1], "fallback prior evidence changed")
        args = context["source_taxon_id"], context["gene"], reviewed
        source = planned_source(root, directory, request_key, filename, gene_url(*args))
        result[key] = read_gene(root, source, *args)
        used.add(request_key)
    require(used == set(plan["requests"]), "unbound gene request")
    return result


def selected_queries(root, directory, cohort, selected_names):
    reviewed = read_queries(root, directory, cohort, selected_names, True)
    unreviewed = read_queries(root, directory, cohort, selected_names, False, reviewed)
    return {
        key: {
            "entries": unreviewed.get(key, value)[0],
            "queries": {
                "reviewed": value[1],
                **({"unreviewed": unreviewed[key][1]} if key in unreviewed else {}),
            },
            "reviewed": key not in unreviewed,
        }
        for key, value in reviewed.items()
    }


def project(entry, taxon, source_taxon, gene, reviewed):
    require(gene in ("rpoB", "rpoC"), "unsupported reference gene")
    genes.validate_entries([entry], gene.casefold(), reviewed)
    nodes, species = lineages.lineage(taxon)
    source_id = int(source_taxon["taxon_id"].split(":")[1])
    require(
        species and any(n["taxonId"] == 2 for n in nodes) and any(n["taxonId"] == source_id for n in nodes),
        "candidate is outside the named taxon scope",
    )
    end = next(i for i, n in enumerate(nodes) if n["taxonId"] == source_id)
    require(
        nodes[: end + 1] == source_taxon["lineage"] and species == source_taxon["species_ancestor"],
        "candidate lineage conflicts with independently resolved source name",
    )
    require(entry["proteinDescription"].get("flag") in (None, "Fragment"), "unreviewed protein flag")
    protein = reference.project_reference(
        entry, gene.casefold(), species["taxonId"], taxon, reviewed=reviewed
    )
    blocks, matches = genes.gene_identity(entry, gene.casefold())
    included_names = []
    for index, component in enumerate(entry["proteinDescription"].get("includes", [])):
        for kind in ("recommendedName", "alternativeNames", "submissionNames"):
            values = [component[kind]] if kind == "recommendedName" and kind in component else []
            if kind != "recommendedName":
                values = component.get(kind, [])
            for value in values:
                name = value["fullName"]["value"]
                require(isinstance(name, str) and bool(name.strip()), "invalid included protein name")
                included_names.append({"component_index": index, "kind": kind, "value": name})
    protein.update(
        {
            "genes": blocks,
            "native_included_protein_names": included_names,
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
        "ontology_cache",
        "bibliography_archive",
        "protected",
        "taxonomy_cache_inventory",
        "query_cache_inventory",
        "prior_verification",
    ):
        reference.check_pin(root, cohort[key])
    index = json.loads((root / cohort["index"]["path"]).read_bytes())
    citations = json.loads((root / cohort["definition_citations"]["path"]).read_bytes())["terms"]
    labels = {}
    with (root / cohort["source_inventory"]["path"]).open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            tid, label = row["determinant_id"], row["determinant_name"]
            require(labels.setdefault(tid, label) == label, "conflicting source labels")
    expected = {t for t in index["terms"] if SELECT.search(labels[t])}
    require(len(expected) == 16 and set(cohort["terms"]) == expected, "full rpo source selection changed")
    wrapper = json.loads((root / cohort["ontology_cache"]["path"]).read_bytes())
    definitions = {}
    for cls in ET.fromstring(wrapper["body"]).iter("{http://www.w3.org/2002/07/owl#}Class"):
        tid = (
            cls.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "")
            .rsplit("/", 1)[-1]
            .replace("_", ":")
        )
        if tid in expected:
            values = [n.text for n in cls.findall("{http://purl.obolibrary.org/obo/}IAO_0000115")]
            require(len(values) == 1, "definition identity changed")
            definitions[tid] = values[0]
            require(
                hashlib.sha256(values[0].encode()).hexdigest() == citations[tid]["definitions"][0]["sha256"],
                "definition text hash changed",
            )
    require(set(definitions) == expected, "definition coverage changed")
    with gzip.open(root / cohort["bibliography_archive"]["path"], "rt") as stream:
        archive = json.load(stream)
    bibliography = {}
    for query in archive["queries"]:
        for candidate in query["candidates"]:
            pmid = candidate.get("id")
            if candidate.get("source") == "MED" and pmid in cohort["bibliography"]:
                row = {k: candidate.get(k) for k in cohort["bibliography"][pmid]}
                require(bibliography.setdefault(pmid, row) == row, "conflicting publication identity")
    require(bibliography == cohort["bibliography"], "cited-title metadata changed")
    require(
        "PMID:20837752" in citations["ARO:3003090"]["definition_citation_ids"],
        "abbreviation citation changed",
    )
    for tid, term in cohort["terms"].items():
        identity = source_identity(tid, labels[tid], definitions, bibliography)
        require(
            tuple(term[k] for k in ("source_organism_name", "source_gene_label", "name_evidence")) == identity
            and term["source_label"] == labels[tid]
            and term["source_label_sha256"]
            == index["terms"][tid]["source_label_sha256"]
            == hashlib.sha256(labels[tid].encode()).hexdigest()
            and term["record_memberships"] == index["terms"][tid]["record_memberships"]
            and term["definition_citation_ids"] == citations[tid]["definition_citation_ids"],
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
    ids = {rid for term in cohort["terms"].values() for rid in term["record_memberships"]}
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
            "selected complete record changed",
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
    require(claims == cohort["claims"] and len(claims) == 32 and len(ids) == 7, "claim scope changed")


def candidate_taxa(root, directory, selection):
    plan = json.loads((directory / "taxonomy-plan.json").read_bytes())
    required = {str(e["organism"]["taxonId"]) for c in selection.values() for e in c["entries"]}
    require(
        set(plan["taxa"]) == required and plan["cohort"] == reference.pin(root, directory / "cohort.json"),
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
        matches = [n for n in body.get("results", [body]) if n["taxonId"] == int(taxid)]
        require(len(matches) == 1, "candidate taxonomy identity changed")
        taxa[taxid] = matches[0]
        lineages.lineage(matches[0])
    require(used == set(plan["requests"]), "candidate taxonomy requests changed")
    return taxa, sources


def build(root, directory=CACHE):
    directory = root / directory
    require(reference.digest(directory / "cohort.json") == COHORT_SHA, "frozen rpo cohort changed")
    cohort = json.loads((directory / "cohort.json").read_bytes())
    check_sources(root, directory, cohort)
    canaries = {
        p: genes.check_canary(root, directory, p)
        for p in ("names-plan.json", "reviewed-plan.json", "unreviewed-plan.json", "taxonomy-plan.json")
    }
    selected_names = names(root, directory, cohort)
    selection = selected_queries(root, directory, cohort, selected_names)
    taxa, sources = candidate_taxa(root, directory, selection)
    terms, proteins = {}, {}
    for tid, term in cohort["terms"].items():
        name, gene = term["source_organism_name"], term["source_gene_label"]
        named = selected_names[name]["selected_taxon"] if name else None
        chosen = selection.get(f"{name}|{gene}")
        candidates = []
        if chosen:
            for entry in chosen["entries"]:
                protein, matches = project(
                    entry, taxa[str(entry["organism"]["taxonId"])], named, gene, chosen["reviewed"]
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
                    "source_queue",
                    "definition_citations",
                    "ontology_cache",
                    "bibliography_archive",
                    "taxonomy_cache_inventory",
                    "query_cache_inventory",
                )
            },
            "cohort": reference.pin(root, directory / "cohort.json"),
            "plans": {p: reference.pin(root, directory / p) for p in canaries},
            "canaries": canaries,
            "taxonomy_sources": sources,
        },
        "bibliographic_identity_context": cohort["bibliography"],
        "bibliographic_sources": cohort["bibliographic_sources"],
        "primary_review_flags": {
            "ARO:3004994": {
                "citation": "PMID:23208709",
                "basis": "CACHED_PUBLICATION_TITLE_ONLY_NOT_RESULTS_REVIEW",
                "status": "REVIEW_COMPENSATION_VERSUS_DIRECT_RESISTANCE_CAUSALITY",
                "source_claim_corrected": False,
            }
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
            "gene_contexts": len(selection),
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
            "Native gene names and explicit synonyms identify reference context, not a tested allele.",
            "Two organism-free terms remain unresolved; a related term cannot supply their subject.",
            "The S. aureus abbreviation bridge uses its own definition and cited publication title, "
            "not experimental results.",
            "Compensatory fitness effects, association and direct resistance "
            "must be distinguished in primary review.",
            "Reference bibliography and taxonomic lineages do not establish "
            "compound-specific phenotypes or genomes.",
            "All candidates and empty queries are retained; zero hits do not establish biological absence.",
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
        "attribution": "CARD curation team, ARO CC BY 4.0; UniProt Consortium, "
        "release 2026_03, CC BY 4.0; Europe PMC bibliographic metadata.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        require(OUTPUT.read_bytes() == payload, "rpo checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
