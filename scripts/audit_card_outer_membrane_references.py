"""Ground outer-membrane label references without flattening complexes or alleles."""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlencode, urlsplit

import audit_card_folp_references as shared
import audit_card_rpo_references as rpo
from audit_beta_tubulin_evidence import bibliography
from audit_card_beta_tubulin_references import protein_names
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

genes, lineages, native, reference = shared.genes, shared.lineages, shared.native, shared.reference
require, contexts = shared.require, rpo.contexts
CACHE = Path("reports/resistance-grounding-2026-10-14-card-outer-membrane")
OUTPUT = Path("research/2026-10-14-card-outer-membrane-references.json")
COHORT_SHA = "19ab849317740fadc00f86216d361e06796f1146b4f72b370565a46dd17b1e56"
SCOPE = "CARD_OUTER_MEMBRANE_LABEL_SCREEN_REFERENCE_CONTEXT_NOT_EXPERIMENTAL_RESISTANCE"
SELECT = re.compile(r"\b(?:omp\w*|opr\w*|porin|LamB|mipA|AbuO)\b", re.I)
SINGLE = re.compile(r"^([A-Z][a-z]+ [a-z]+) ((?i:omp\w*|opr\w*|LamB|mipA|AbuO))\b(.*)$")
GENES = {
    "por",
    "omp36",
    "ompf",
    "oprd",
    "ompk35",
    "ompk36",
    "ompk37",
    "omp38",
    "lamb",
    "mipa",
    "omp1",
    "abuo",
}


def source_identity(label):
    match = SINGLE.fullmatch(label)
    if match:
        require(
            not match[3]
            or re.fullmatch(
                r" (?:with mutations? conferring resistance|conferring resistance) to .+", match[3]
            ),
            "unreviewed single-protein label suffix",
        )
        return {
            "source_organism_name": match[1],
            "source_gene_label": match[2],
            "entity_scope": "ORGANISM_NAMED_SINGLE_PROTEIN_LABEL",
        }
    if label == "Neisseria gonorrhoeae porin PIB (por)":
        return {
            "source_organism_name": "Neisseria gonorrhoeae",
            "source_gene_label": "por",
            "entity_scope": "ORGANISM_NAMED_SINGLE_PROTEIN_LABEL",
        }
    if label in {"porin OmpC", "OmpA"}:
        return {
            "source_organism_name": None,
            "source_gene_label": None,
            "entity_scope": "ORGANISM_UNSPECIFIED_NO_SPECIES_QUERY",
        }
    require(re.match(r"^(?:Mex|Amr|Axy)[A-Za-z]+-Opr[A-Za-z]+\b", label), "unreviewed source-label scope")
    return {
        "source_organism_name": None,
        "source_gene_label": None,
        "entity_scope": "COMPLEX_OR_REGULATORY_CONTEXT_NOT_SINGLE_PROTEIN",
    }


def names(root, directory, cohort):
    named = {k: t for k, t in cohort["terms"].items() if t["source_organism_name"] is not None}
    return shared.names(root, directory, {**cohort, "terms": named})


def gene_url(taxid, gene, reviewed):
    require(
        type(taxid) is int
        and taxid > 0
        and type(reviewed) is bool
        and isinstance(gene, str)
        and gene.casefold() in GENES,
        "invalid outer-membrane query scope",
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
            "reviewed": key not in unreviewed,
            "queries": {
                "reviewed": value[1],
                **({"unreviewed": unreviewed[key][1]} if key in unreviewed else {}),
            },
        }
        for key, value in reviewed.items()
    }


def native_bibliography(entry):
    rows, seen = [], set()
    for ref in entry.get("references", []):
        number, citation = ref["referenceNumber"], ref["citation"]
        require(type(number) is int and number > 0 and number not in seen, "invalid native reference number")
        seen.add(number)
        if citation["citationType"] != "thesis":
            rows.extend(bibliography({"references": [ref]}))
            continue
        require(
            set(citation) == {"id", "citationType", "authors", "publicationDate", "institute"}
            and all(
                isinstance(citation[k], str) and citation[k].strip()
                for k in ("id", "publicationDate", "institute")
            )
            and isinstance(citation["authors"], list)
            and citation["authors"]
            and all(isinstance(a, str) and a.strip() for a in citation["authors"]),
            "unreviewed native thesis shape",
        )
        strains = [c["value"] for c in ref.get("referenceComments", []) if c.get("type") == "STRAIN"]
        require(all(isinstance(s, str) and s.strip() for s in strains), "invalid thesis strain comments")
        rows.append(
            {
                "native_reference_number": number,
                "native_citation_id": citation["id"],
                "citation_type": "thesis",
                "title": None,
                "publication_date": citation["publicationDate"],
                "institute": citation["institute"],
                "submission_database": None,
                "identifiers": [],
                "identifier_issues": [],
                "reference_strain_comments": strains,
                "strain_comment_scope": "NATIVE_REFERENCE_METADATA_NOT_TESTED_RESISTANCE_SUBJECTS",
                "primary_results_reviewed": False,
                "experimental_subject_assignment": False,
                "resistance_inferred_from_citation": False,
            }
        )
    return rows


def project(entry, taxon, source_taxon, gene, reviewed):
    require(gene.casefold() in GENES, "unsupported reference gene")
    genes.validate_entries([entry], gene.casefold(), reviewed)
    nodes, species = lineages.lineage(taxon)
    source_id = int(source_taxon["taxon_id"].split(":")[1])
    require(
        species and any(n["taxonId"] == 2 for n in nodes) and any(n["taxonId"] == source_id for n in nodes),
        "candidate outside named bacterial scope",
    )
    end = next(i for i, n in enumerate(nodes) if n["taxonId"] == source_id)
    require(
        nodes[: end + 1] == source_taxon["lineage"] and species == source_taxon["species_ancestor"],
        "candidate lineage conflicts with resolved source name",
    )
    require(
        entry["proteinDescription"].get("flag") in (None, "Fragment", "Precursor"), "unreviewed protein flag"
    )
    result = reference.project_reference(entry, gene.casefold(), species["taxonId"], taxon, reviewed=reviewed)
    blocks, matches = genes.gene_identity(entry, gene.casefold())
    result.update(
        {
            "genes": blocks,
            "native_protein_flag": entry["proteinDescription"].get("flag"),
            "complete_native_bibliography": native_bibliography(entry),
            "unflagged_means_complete": False,
            "precursor_or_fragment_coordinates_inferred": False,
            "experimental_genome_assignment": None,
            "database_review_status_is_primary_results_review": False,
            "resistance_inferred_from_reference": False,
            "porin_function_inferred_from_source_label": False,
            "reference_organism_label_matches_taxonomy": entry["organism"]["scientificName"]
            == taxon["scientificName"],
        }
    )
    result["reference_species_taxon_id"] = result.pop("source_species_taxon_id")
    return result, matches


def partition_candidates(term, entries):
    """The native por symbol does not distinguish the source's PIB subtype."""
    if term["source_label"] != "Neisseria gonorrhoeae porin PIB (por)":
        return entries, []
    eligible, unresolved = [], []
    for entry in entries:
        names = protein_names(entry)
        values = {n["value"] for n in names}
        pib = bool(values & {"Major outer membrane protein P.IB", "Outer membrane protein PIB"})
        pia = bool(values & {"Outer membrane protein IA", "Porin IA protein"})
        hybrid = any("hybrid" in value.casefold() for value in values)
        if pib and not pia and not hybrid:
            eligible.append(entry)
            continue
        status = (
            "NATIVE_HYBRID_NOT_PURE_PIB"
            if hybrid
            else "CONFLICTING_NATIVE_SUBTYPE_NAMES"
            if pib and pia
            else "NATIVE_IA_NOT_SOURCE_PIB"
            if pia
            else "NO_EXPLICIT_NATIVE_PIB_SUBTYPE_NOT_ABSENCE"
        )
        unresolved.append(
            {
                "protein_accession": "UniProtKB:" + entry["primaryAccession"],
                "native_protein_names": names,
                "reason": status,
                "resistance_or_susceptibility_inferred": False,
            }
        )
    return eligible, unresolved


def candidate_status(term, chosen, candidates, unresolved):
    if not term["source_organism_name"]:
        return term["entity_scope"]
    if chosen is None:
        return "SOURCE_NAME_UNRESOLVED_NO_PROTEIN_QUERY"
    if not candidates:
        return (
            "NO_SUBTYPE_ELIGIBLE_REFERENCE_CANDIDATES" if unresolved else "NO_EXACT_GENE_RESULTS_NOT_ABSENCE"
        )
    if len(candidates) > 1:
        return "MULTIPLE_CANDIDATES_NO_SELECTION"
    return "REVIEWED_REFERENCE" if chosen["reviewed"] else "UNREVIEWED_CANDIDATE"


def check_sources(root, directory, cohort):
    for key in (
        "index",
        "census",
        "source_inventory",
        "source_queue",
        "definition_citations",
        "protected",
        "taxonomy_cache_inventory",
        "query_cache_inventory",
        "prior_verification",
    ):
        reference.check_pin(root, cohort[key])
    index = json.loads(reference.check_pin(root, cohort["index"]).read_bytes())
    receipt = json.loads(reference.check_pin(root, cohort["prior_verification"]).read_bytes())
    require(
        cohort["index"] in receipt["files"] and receipt["summary"] == index["summary"],
        "prior index proof changed",
    )
    citations = json.loads(reference.check_pin(root, cohort["definition_citations"]).read_bytes())["terms"]
    labels = {}
    for row in csv.DictReader(reference.check_pin(root, cohort["source_inventory"]).open(), delimiter="\t"):
        tid, label = row["determinant_id"], row["determinant_name"]
        require(labels.setdefault(tid, label) == label, "conflicting source labels")
    expected = {t for t in index["terms"] if SELECT.search(labels[t])}
    require(len(expected) == 29 and set(cohort["terms"]) == expected, "full label-screen coverage changed")
    for tid, term in cohort["terms"].items():
        require(
            all(term[k] == v for k, v in source_identity(labels[tid]).items())
            and term["source_label"] == labels[tid]
            and term["source_label_sha256"]
            == index["terms"][tid]["source_label_sha256"]
            == hashlib.sha256(labels[tid].encode()).hexdigest()
            and term["prior_reference_links"] == index["terms"][tid]["links"]
            and term["record_memberships"] == index["terms"][tid]["record_memberships"]
            and term["definition_citation_ids"] == citations[tid]["definition_citation_ids"],
            "source term identity or prior evidence changed",
        )
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    require(
        len(census) == len({r["identifier"] for r in census}) == 2939
        and {r["path"] for r in census}
        == {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        and all(reference.digest(root / r["path"]) == r["record_sha256"] for r in census),
        "complete corpus census changed",
    )
    protected = json.loads(reference.check_pin(root, cohort["protected"]).read_bytes())
    require(
        all(
            reference.digest(root / p) == checksum
            for p, checksum in protected.items()
            if p.startswith("data/")
        ),
        "source or collection bytes changed",
    )
    ids = {rid for term in cohort["terms"].values() for rid in term["record_memberships"]}
    require([r for r in census if r["identifier"] in ids] == cohort["records"], "record selection changed")
    claims = []
    for row in cohort["records"]:
        snapshot = directory / (row["identifier"].replace(":", "-") + "-before.yaml")
        require(reference.digest(snapshot) == row["record_sha256"], "raw record snapshot changed")
        record = load_record(root / row["path"])
        require(
            record["identifier"] == row["identifier"]
            and record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "complete record identity changed",
        )
        for position, claim in enumerate(record.get("resistance_mechanisms", [])):
            if claim.get("aro_id") in expected:
                require(
                    claim["label"] == cohort["terms"][claim["aro_id"]]["source_label"], "claim label changed"
                )
                claims.append(
                    {
                        "record_identifier": record["identifier"],
                        "position": position,
                        "aro_id": claim["aro_id"],
                        "claim_sha256": hashlib.sha256(
                            json.dumps(claim, sort_keys=True, ensure_ascii=True).encode()
                        ).hexdigest(),
                    }
                )
    require(claims == cohort["claims"] and len(claims) == 117 and len(ids) == 46, "source claims changed")


def candidate_taxa(root, directory, cohort, selection):
    plan = json.loads((directory / "taxonomy-plan.json").read_bytes())
    required = {str(e["organism"]["taxonId"]) for c in selection.values() for e in c["entries"]}
    require(
        set(plan["taxa"]) == required and plan["cohort"] == reference.pin(root, directory / "cohort.json"),
        "reference taxon coverage changed",
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
        require(urlsplit(source["url"]).path.startswith("/taxonomy/"), "not native taxonomy")
        body, sources[taxid] = native.read_source(root, source)
        rows = [n for n in body.get("results", [body]) if n["taxonId"] == int(taxid)]
        require(len(rows) == 1, "reference taxon identity changed")
        taxa[taxid] = rows[0]
        lineages.lineage(rows[0])
    require(used == set(plan["requests"]), "unbound taxonomy request")
    return taxa, sources


def build(root, directory=CACHE):
    directory = root / directory
    require(reference.digest(directory / "cohort.json") == COHORT_SHA, "frozen cohort changed")
    cohort = json.loads((directory / "cohort.json").read_bytes())
    check_sources(root, directory, cohort)
    plans = ("names-plan.json", "reviewed-plan.json", "unreviewed-plan.json", "taxonomy-plan.json")
    canaries = {p: genes.check_canary(root, directory, p) for p in plans}
    named = names(root, directory, cohort)
    selection = selected_queries(root, directory, cohort, named)
    taxa, taxonomy_sources = candidate_taxa(root, directory, cohort, selection)
    terms, proteins = {}, {}
    for tid, term in cohort["terms"].items():
        name, gene = term["source_organism_name"], term["source_gene_label"]
        selected_taxon = named[name]["selected_taxon"] if name else None
        chosen = selection.get(f"{name}|{gene}") if name else None
        candidates, unresolved = [], []
        if chosen:
            eligible, unresolved = partition_candidates(term, chosen["entries"])
            for entry in eligible:
                protein, matches = project(
                    entry, taxa[str(entry["organism"]["taxonId"])], selected_taxon, gene, chosen["reviewed"]
                )
                accession = protein["protein_accession"]
                require(proteins.setdefault(accession, protein) == protein, "conflicting shared candidate")
                candidates.append(
                    {
                        "protein_accession": accession,
                        "native_gene_field_matches": matches,
                        "experimental_subject_assignment": False,
                        "exact_resistant_allele": False,
                    }
                )
        status = candidate_status(term, chosen, candidates, unresolved)
        terms[tid] = {
            **term,
            "prior_reference_links_source": {"input": "index", "pointer": f"/terms/{tid}/links"},
            "prior_link_pointers_resolve_within_pinned_index": True,
            "named_reference_taxon_id": selected_taxon["taxon_id"] if selected_taxon else None,
            "reference_status": status,
            "queries": chosen["queries"] if chosen else {},
            "reference_candidates": sorted(candidates, key=lambda c: c["protein_accession"]),
            "query_hits_not_assigned_to_source_subtype": unresolved,
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
            "experimental_genome_assignment": None,
            "primary_review_status": "OPEN",
        }
    native_rows = [r for p in proteins.values() for r in p["complete_native_bibliography"]]
    return {
        "date": cohort["date"],
        "scope": SCOPE,
        "release": "2026_03",
        "inputs": {
            **{
                k: cohort[k]
                for k in (
                    "index",
                    "prior_verification",
                    "census",
                    "source_inventory",
                    "source_queue",
                    "definition_citations",
                    "taxonomy_cache_inventory",
                    "query_cache_inventory",
                )
            },
            "cohort": reference.pin(root, directory / "cohort.json"),
            "plans": {p: reference.pin(root, directory / p) for p in plans},
            "canaries": canaries,
            "taxonomy_sources": taxonomy_sources,
        },
        "terms": terms,
        "names": named,
        "proteins": dict(sorted(proteins.items())),
        "records": cohort["records"],
        "claims": cohort["claims"],
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(cohort["records"]),
            "source_terms": len(terms),
            "source_claims": len(cohort["claims"]),
            "named_single_terms": 14,
            "entity_scopes": dict(sorted(Counter(t["entity_scope"] for t in terms.values()).items())),
            "source_names": len(named),
            "resolved_source_names": sum(bool(n["selected_taxon"]) for n in named.values()),
            "gene_taxon_contexts": len(selection),
            "reference_proteins": len(proteins),
            "reference_taxa": len(taxa),
            "term_protein_links": sum(len(t["reference_candidates"]) for t in terms.values()),
            "query_hits_not_assigned_to_source_subtype": sum(
                len(t["query_hits_not_assigned_to_source_subtype"]) for t in terms.values()
            ),
            "subtype_dispositions": dict(
                sorted(
                    Counter(
                        item["reason"]
                        for t in terms.values()
                        for item in t["query_hits_not_assigned_to_source_subtype"]
                    ).items()
                )
            ),
            "native_protein_flags": dict(
                sorted(Counter(str(p["native_protein_flag"]) for p in proteins.values()).items())
            ),
            "term_statuses": dict(sorted(Counter(t["reference_status"] for t in terms.values()).items())),
            "native_bibliography_memberships": len(native_rows),
            "bibliography_types": dict(sorted(Counter(r["citation_type"] for r in native_rows).items())),
            "native_identifier_issue_memberships": sum(len(r["identifier_issues"]) for r in native_rows),
            "whole_record_primary_signoffs": 0,
            "biological_records_changed": 0,
            "experimental_assignments": 0,
        },
        "limitations": [
            "The complete lexical label screen is not an exhaustive ontology-defined set of all porins.",
            "Named single-protein labels, organism-unspecified labels and complexes remain separate.",
            "A source label or exact gene match does not establish porin function or a resistant allele.",
            "All query hits are accounted for; no representative strain or protein is selected.",
            "The por query includes IA, hybrid and unspecified proteins; only explicit native PIB names "
            "are subtype candidates, without validating resistance alleles.",
            "Existing explicit CARD references remain attributed and are not replaced by a no-hit query.",
            "Bibliography memberships and reference strain comments are not experimental subject crosswalks.",
            "Primary experimental evidence, exact tested compounds, alleles and genome joins remain open.",
        ],
        "constraints": {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "source_adoptions": 0,
            "outreach": 0,
            "github_mutations": 0,
            "held_sources_retried": False,
            "operational_sequence_variant_or_protocol_fields_exported": False,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": "CARD/ARO CC BY 4.0; UniProt Consortium release 2026_03 CC BY 4.0; "
        "reference metadata only.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        require(OUTPUT.read_bytes() == payload, "outer-membrane dossier does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
