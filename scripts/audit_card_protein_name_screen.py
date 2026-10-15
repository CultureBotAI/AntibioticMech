"""Replay literal protein-name candidates without selecting experimental identities."""

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

import audit_card_literature_expansion as literature
from audit_card_reference_lineages import lineage
from audit_card_reference_memberships import checksum
from audit_curator_resistance_fields import owner
from audit_fungamr_cohort import read_source
from audit_vgb_evidence import reference, require

from antibioticmech.activity_collections import load_record

PREFIX = "research/2026-10-15-card-protein-name-screen"
PLAN = Path(PREFIX + "-plan.json")
OUTPUT = Path(PREFIX + ".json")
SCOPE = "UNLINKED_CARD_LITERAL_PROTEIN_NAME_DISCOVERY_NOT_EXPERIMENTAL_GROUNDING"
SELECTION = {
    "only_unlinked_in_pinned_index": True,
    "name_blocks": ["recommendedName", "alternativeNames", "submissionNames"],
    "name_fields": ["fullName", "shortNames"],
    "literal_case_insensitive": True,
    "left_boundary": "(?<![A-Za-z0-9])",
    "right_boundary": "(?![A-Za-z0-9'-])",
    "punctuation_normalized": False,
    "gene_fields_screened": False,
}
CONSTRAINTS = {
    "network_requests": 0,
    "biological_writes": False,
    "experimental_assignments": False,
    "issue_1040": "DEFERRED",
    "reuse_terms_review_resumed": False,
}
PENDING = "NAME_CITATION_TAXON_REFERENCE_CANDIDATE_PRIMARY_REVIEW_PENDING"
COMPLEX = "WITHHELD_COMPLEX_LABEL_MATCHES_ONLY_A_SUBUNIT_NAME"
ALLELES = "WITHHELD_MULTIPLE_ALLELE_NAMES_SHARE_ONE_REFERENCE_ENTRY"
EXPECTED = {
    "ARO:3000772": ("Q24LT6", COMPLEX),
    "ARO:3000877": ("P62593", ALLELES),
    "ARO:3000880": ("P62593", ALLELES),
    "ARO:3000887": ("P62593", ALLELES),
    "ARO:3002777": ("R4NN96", PENDING),
    "ARO:3002819": ("Q9APB1", PENDING),
    "ARO:3003761": ("S5FUH0", PENDING),
    "ARO:3003970": ("Q47755", PENDING),
    "ARO:3004285": ("P12921", PENDING),
    "ARO:3004695": ("A0A2I6AXF4", PENDING),
}
NOTES = {
    "ARO:3000772": (
        "AdeK is a named subunit, not an identity for the entire AdeIJK complex; "
        "conflicting submission names remain native annotations."
    ),
    "ARO:3000877": (
        "The same reference entry carries TEM-5, TEM-8 and TEM-16 alternative names; "
        "none identifies an exact experimental allele."
    ),
    "ARO:3000880": (
        "The same reference entry carries TEM-5, TEM-8 and TEM-16 alternative names; "
        "none identifies an exact experimental allele."
    ),
    "ARO:3000887": (
        "The same reference entry carries TEM-5, TEM-8 and TEM-16 alternative names; "
        "none identifies an exact experimental allele."
    ),
    "ARO:3002777": (
        "Native protein name supplies a discovery lead; the native gene field is absent "
        "and is not inferred from that name."
    ),
    "ARO:3002819": (
        "Native protein name supplies a discovery lead; the native gene field is absent "
        "and is not inferred from that name."
    ),
    "ARO:3003761": (
        "Native protein name supplies a discovery lead; the native gene field is absent "
        "and does not identify a tested variant."
    ),
    "ARO:3003970": (
        "A generic ligase name and ddl gene symbol do not establish a resistance effect "
        "or a particular resistant allele."
    ),
    "ARO:3004285": (
        "The entry is already indexed through a different CARD term. Its tmrB cross-reference "
        "is not an explicit cross-reference to this generic source term; "
        "strain and species ranks remain distinct."
    ),
    "ARO:3004695": (
        "The native gene symbol mcr-4 differs in granularity from the protein name; "
        "no gene renaming or experimental allele assignment is made."
    ),
}


def protein_names(entry):
    result = []
    description = entry.get("proteinDescription", {})
    for field in SELECTION["name_blocks"]:
        blocks = description.get(field, [])
        if field == "recommendedName":
            blocks = [blocks] if blocks else []
        for i, block in enumerate(blocks):
            if "fullName" in block:
                result.append({"path": f"{field}/{i}/fullName", "value": block["fullName"]["value"]})
            result.extend(
                {"path": f"{field}/{i}/shortNames/{j}", "value": short["value"]}
                for j, short in enumerate(block.get("shortNames", []))
            )
    return result


def name_matches(entry, label):
    require(isinstance(label, str) and bool(label.strip()), "empty source label")
    pattern = re.compile(SELECTION["left_boundary"] + re.escape(label) + SELECTION["right_boundary"], re.I)
    return [name for name in protein_names(entry) if pattern.search(name["value"])]


def select_terms(index, direct):
    require(set(index["terms"]) == set(direct["determinants"]), "source term universe changed")
    result = {}
    for tid, row in index["terms"].items():
        if not row["links"]:
            labels = direct["determinants"][tid]["labels"]
            require(len(labels) == 1, "multiple source labels require review")
            result[tid] = labels[0]
    return result


def selected_claims(document, terms):
    return [
        (i, c)
        for i, c in enumerate(document.get("resistance_mechanisms", []))
        if owner(c) == "CARD" and c.get("aro_id") in terms
    ]


def public_context(root, plan):
    require(
        plan["scope"] == SCOPE and plan["selection"] == SELECTION and plan["constraints"] == CONSTRAINTS,
        "scope or selection changed",
    )
    paths = {k: reference.check_pin(root, p) for k, p in plan["inputs"].items()}
    data = {k: json.loads(p.read_bytes()) for k, p in paths.items() if p.suffix == ".json"}
    index = data["index"]
    require(
        plan["inputs"]["index"] in data["index_verification"]["files"]
        and index["summary"] == data["index_verification"]["summary"]
        and select_terms(index, data["direct_candidates"]) == plan["terms"]
        and len(plan["terms"]) == 720,
        "complete cohort or checkpoint changed",
    )
    for key in ("direct_candidates", "definition_citations", "census", "source_inventory", "source_queue"):
        require(plan["inputs"][key] == index["inputs"][key], "input owner differs from index")
    with paths["census"].open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    require(
        len(census) == len({r["identifier"] for r in census}) == 2939
        and {r["path"] for r in census}
        == {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        and all(reference.digest(root / r["path"]) == r["record_sha256"] for r in census),
        "corpus membership or bytes changed",
    )
    ids = {rid for tid in plan["terms"] for rid in index["terms"][tid]["record_memberships"]}
    records = [r for r in census if r["identifier"] in ids]
    claims = [c for c in index["claims"] if c["aro_id"] in plan["terms"]]
    actual = []
    for row in records:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "complete record identity changed",
        )
        for i, claim in selected_claims(doc, plan["terms"]):
            tid = claim["aro_id"]
            require(claim["label"] == plan["terms"][tid], "source claim label changed")
            actual.append((row["identifier"], i, tid, checksum(claim)))
    require(
        sorted(actual)
        == sorted(
            (c["record_identifier"], c["resistance_index"], c["aro_id"], c["claim_sha256"]) for c in claims
        )
        and len(actual) == 1277
        and len(records) == 203,
        "live claim membership changed",
    )
    definitions = data["definition_citations"]["terms"]
    for tid, label in plan["terms"].items():
        require(
            definitions[tid]["label_sha256"] == literature.definitions.text_hash(label)
            and sorted({c[0] for c in actual if c[2] == tid}) == index["terms"][tid]["record_memberships"],
            "term identity or membership differs",
        )
    pmids = {
        c.removeprefix("PMID:")
        for tid in plan["terms"]
        for c in definitions[tid]["definition_citation_ids"]
        if c.startswith("PMID:")
    }
    require(set(plan["queries"]) == pmids and len(pmids) == 643, "citation query coverage changed")
    for pmid, query in plan["queries"].items():
        require(
            query == {k: data["prior_queries"]["queries"][pmid][k] for k in ("directory", "query")},
            "cached query provenance differs",
        )
    return data, records, claims


def project_reference(entry, taxon):
    require(not {"sequence", "features"} & set(entry), "unexpected sequence or variant data")
    path, species = lineage(taxon)
    require(
        entry["organism"]["taxonId"] == taxon["taxonId"]
        and entry["organism"]["scientificName"] == taxon["scientificName"]
        and all(type(v) is int and v > 0 for v in entry["entryAudit"].values())
        and set(entry["entryAudit"]) == {"entryVersion", "sequenceVersion"},
        "native identity or version changed",
    )
    bibliography = []
    anomalies = []
    for item in entry["references"]:
        citation = item["citation"]
        identifiers = citation.get("citationCrossReferences", [])
        bibliography.append(
            {
                "reference_number": item["referenceNumber"],
                "citation_type": citation["citationType"],
                "identifiers": identifiers,
                "citation_sha256": checksum(citation),
            }
        )
        for identifier in identifiers:
            if identifier["database"] == "DOI" and not re.fullmatch(r"10\.\d{4,9}/\S+", identifier["id"]):
                anomalies.append(
                    {
                        "reference_number": item["referenceNumber"],
                        "native_identifier": identifier,
                        "silently_repaired": False,
                    }
                )
    numbers = [b["reference_number"] for b in bibliography]
    require(numbers == list(range(1, len(numbers) + 1)), "native bibliography numbering changed")
    return {
        "accession": "UniProtKB:" + entry["primaryAccession"],
        "native_entry_sha256": checksum(entry),
        "entry_type": entry["entryType"],
        "entry_audit": entry["entryAudit"],
        "gene_field_present": "genes" in entry,
        "gene_symbols": [g["geneName"]["value"] for g in entry.get("genes", []) if "geneName" in g],
        "gene_symbols_inferred_from_names": False,
        "protein_names": protein_names(entry),
        "native_protein_flag": entry["proteinDescription"].get("flag"),
        "unflagged_means_complete": False,
        "native_card_cross_references": [
            x for x in entry.get("uniProtKBCrossReferences", []) if x["database"] == "CARD"
        ],
        "reference_taxonomy": {
            "taxon_id": "NCBITaxon:" + str(taxon["taxonId"]),
            "scientific_name": taxon["scientificName"],
            "native_rank": taxon["rank"],
            "parent": taxon["parent"],
            "lineage": path,
            "species": species,
            "provider": "UniProt taxonomy cached response; no NCBI request",
        },
        "native_bibliography": bibliography,
        "bibliography_counts": dict(sorted(Counter(b["citation_type"] for b in bibliography).items())),
        "native_identifier_anomalies": anomalies,
        "new_primary_results_review": False,
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
        "experimental_genome_assignment": None,
    }


def term_status(citations, pool, matches):
    if matches:
        return matches[0]["status"]
    if not citations:
        return "NO_DEFINITION_CITATIONS_NOT_QUERIED"
    if not any(c.startswith("PMID:") for c in citations):
        return "NON_PMID_CITATIONS_NOT_QUERIED"
    return "NO_LITERAL_PROTEIN_NAME_MATCH" if pool else "COMPLETE_PMID_QUERIES_EMPTY_NOT_BIOLOGICAL_ABSENCE"


def build(root, plan_path=PLAN):
    plan = json.loads((root / plan_path).read_bytes())
    data, records, claims = public_context(root, plan)
    pools, union, queries = {}, {}, {}
    for pmid, item in plan["queries"].items():
        entries, query = literature.read_query(root, root / item["directory"], pmid)
        require(
            query == item["query"] and query["complete_for_query"] and query["release"] == "2026_03",
            "cached citation query changed",
        )
        pools[pmid], queries[pmid] = entries, query
        for accession, entry in entries.items():
            require(not {"sequence", "features"} & set(entry), "unexpected sequence or variant data")
            require(accession not in union or union[accession] == entry, "cross-query entry conflict")
            union[accession] = entry
    terms, observed = {}, {}
    for tid, label in sorted(plan["terms"].items()):
        definition = data["definition_citations"]["terms"][tid]
        citations = definition["definition_citation_ids"]
        pmids = [c.removeprefix("PMID:") for c in citations if c.startswith("PMID:")]
        pool = {a for p in pmids for a in pools[p]}
        matches = []
        for accession in sorted(pool):
            names = name_matches(union[accession], label)
            if not names:
                continue
            require(tid in EXPECTED and accession == EXPECTED[tid][0], "new name match requires review")
            observed[tid] = accession
            matches.append(
                {
                    "protein_accession": "UniProtKB:" + accession,
                    "name_matches": names,
                    "source_citation_ids": ["PMID:" + p for p in pmids if accession in pools[p]],
                    "status": EXPECTED[tid][1],
                    "review_note": NOTES[tid],
                    "explicit_card_xref_to_source_term": any(
                        x["database"] == "CARD" and x["id"] == tid
                        for x in union[accession].get("uniProtKBCrossReferences", [])
                    ),
                    "selected_for_broad_index": False,
                    "experimental_subject_assignment": False,
                }
            )
        terms[tid] = {
            "source_label": label,
            "definition_citation_ids": citations,
            "definition_annotation_sha256": checksum(definition),
            "record_memberships": data["index"]["terms"][tid]["record_memberships"],
            "ontology_scope_hint": data["index"]["terms"][tid]["ontology_scope_hint"],
            "citation_pool_size": len(pool),
            "name_matches": matches,
            "status": term_status(citations, pool, matches),
            "other_citations_not_queried": [c for c in citations if not c.startswith("PMID:")],
            "biological_absence_inferred": False,
            "whole_record_primary_review": "OPEN",
        }
    require(observed == {t: pair[0] for t, pair in EXPECTED.items()}, "reviewed match set changed")
    taxons, tax_sources = {}, {}
    for tid, source in plan["taxonomy"].items():
        taxons[tid], tax_sources[tid] = read_source(root, source)
        require(taxons[tid]["taxonId"] == int(tid), "taxonomy request identity changed")
    matched_entries = {a: union[a] for a in set(observed.values())}
    require(
        {str(e["organism"]["taxonId"]) for e in matched_entries.values()} == set(taxons),
        "taxonomy coverage changed",
    )
    references = {
        "UniProtKB:" + a: project_reference(e, taxons[str(e["organism"]["taxonId"])])
        for a, e in sorted(matched_entries.items())
    }
    for accession, item in references.items():
        item["already_in_base_index"] = accession in data["index"]["proteins"]
        if item["already_in_base_index"]:
            identity = data["index"]["proteins"][accession]["identity"]
            require(
                identity
                == {
                    "entry_type": item["entry_type"],
                    "entry_version": item["entry_audit"]["entryVersion"],
                    "sequence_version": item["entry_audit"]["sequenceVersion"],
                    "reference_taxon_id": item["reference_taxonomy"]["taxon_id"],
                    "reference_taxon_rank": item["reference_taxonomy"]["native_rank"],
                    "reference_species_taxon_id": "NCBITaxon:"
                    + str(item["reference_taxonomy"]["species"]["taxonId"]),
                },
                "existing indexed reference identity differs",
            )
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / plan_path),
        "inputs": plan["inputs"],
        "terms": terms,
        "records": records,
        "claims": claims,
        "reference_candidates": references,
        "citation_queries": queries,
        "taxonomy_sources": tax_sources,
        "citation_entry_digests": {"UniProtKB:" + a: checksum(e) for a, e in sorted(union.items())},
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(records),
            "source_terms": len(terms),
            "source_claims": len(claims),
            "complete_cached_citation_queries": len(queries),
            "citation_query_entry_appearances": sum(len(e) for e in pools.values()),
            "distinct_citation_entries": len(union),
            "matched_terms": len(observed),
            "matched_proteins": len(references),
            "reference_taxa": len(taxons),
            "term_statuses": dict(sorted(Counter(t["status"] for t in terms.values()).items())),
        },
        "limits": {
            **CONSTRAINTS,
            "ncbi_requests": 0,
            "new_primary_results_reviews": 0,
            "biological_records_changed": 0,
            "curated_ast_observations": 0,
            "primary_access_holds_retried": 0,
            "github_mutations": 0,
            "source_adoptions": 0,
            "outreach": 0,
            "whole_record_primary_signoffs": 0,
            "broad_index_updated": False,
            "all_aliases_or_sources_searched": False,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": (
            "CARD/ARO ontology and UniProt release 2026_03, CC BY 4.0; no primary article text redistributed."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build(args.root)
    if args.output:
        with args.output.open("x") as stream:
            stream.write(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
