"""Replay unlinked APH/ANT/aad/mph label contexts without experimental assignments."""

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

import audit_card_literature_expansion as literature
from audit_aac6_gaps import name_matches, protein_names
from audit_card_reference_memberships import checksum
from audit_fungamr_cohort import read_source
from audit_vgb_evidence import project_taxon, reference, require

from antibioticmech.activity_collections import load_record

PREFIX = "research/2026-10-15-aph-ant-aad-mph-gaps"
PLAN = Path(PREFIX + "-plan.json")
OUTPUT = Path(PREFIX + ".json")
PREFIXES = ("aph", "ant(", "aad", "mph")
SCOPE = "UNLINKED_APH_ANT_AAD_MPH_LABEL_COHORT_REFERENCE_METADATA_NOT_EXPERIMENTAL_IDENTITY"
QUALIFIED = "HISTORICAL_NOMENCLATURE_AND_UNREVIEWED_CITATION_TAXON_REFERENCE_ONLY"
EMPTY = "COMPLETE_CITATION_QUERIES_EMPTY_NOT_BIOLOGICAL_ABSENCE"
UNMATCHED = "CITATION_ENTRIES_WITHOUT_EXACT_LABEL_MATCH_NO_SELECTION"
TERM = "ARO:3002637"
ACCESSION = "UniProtKB:O68183"


def select_terms(index, direct):
    require(set(index["terms"]) == set(direct["determinants"]), "source term universe changed")
    result = {}
    for tid, row in index["terms"].items():
        labels = direct["determinants"][tid]["labels"]
        if not row["links"] and any(label.casefold().startswith(PREFIXES) for label in labels):
            require(len(labels) == 1, "multiple source labels require review")
            result[tid] = labels[0]
    return result


def public_context(root, plan):
    require(
        plan["scope"] == SCOPE
        and plan["selection"]
        == {
            "casefolded_label_prefixes": list(PREFIXES),
            "only_unlinked_in_pinned_index": True,
            "enzyme_family_membership_inferred_from_prefix": False,
        }
        and plan["constraints"]
        == {
            "network_requests": 0,
            "biological_writes": False,
            "experimental_assignments": False,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
        },
        "cohort selection or scope changed",
    )
    paths = {k: reference.check_pin(root, p) for k, p in plan["inputs"].items()}
    data = {k: json.loads(p.read_bytes()) for k, p in paths.items() if p.suffix == ".json"}
    index, definitions = data["index"], data["definition_citations"]["terms"]
    require(
        plan["inputs"]["index"] in data["index_verification"]["files"]
        and index["summary"] == data["index_verification"]["summary"]
        and plan["inputs"]["nomenclature"] in data["nomenclature_verification"]["artifacts"]
        and select_terms(index, data["direct_candidates"]) == plan["terms"]
        and len(plan["terms"]) == 14,
        "checkpoint or complete cohort changed",
    )
    for key in ("direct_candidates", "definition_citations", "census", "source_inventory", "source_queue"):
        require(index["inputs"][key] == plan["inputs"][key], "input owner differs from index")
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
    expected = [c for c in index["claims"] if c["aro_id"] in plan["terms"]]
    actual = []
    for row in records:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "complete record identity changed",
        )
        for i, claim in enumerate(doc.get("resistance_mechanisms", [])):
            tid = claim.get("aro_id")
            if tid in plan["terms"]:
                require(claim["label"] == plan["terms"][tid], "source claim label changed")
                actual.append((row["identifier"], i, tid, checksum(claim)))
    require(
        sorted(actual)
        == sorted(
            (c["record_identifier"], c["resistance_index"], c["aro_id"], c["claim_sha256"]) for c in expected
        )
        and len(actual) == 38,
        "live claim membership changed",
    )
    for tid, label in plan["terms"].items():
        require(
            definitions[tid]["label_sha256"] == literature.definitions.text_hash(label)
            and sorted({c[0] for c in actual if c[2] == tid}) == index["terms"][tid]["record_memberships"],
            "term identity or membership differs",
        )
    pmids = {
        p.removeprefix("PMID:") for tid in plan["terms"] for p in definitions[tid]["definition_citation_ids"]
    }
    require(set(plan["queries"]) == pmids and len(pmids) == 14, "citation query coverage changed")
    return data, records, expected


def project_reference(entry, taxon, nomenclature, structural):
    review = nomenclature["nomenclature_review"]
    require(
        review["source_name"] == "APH(2'')-Id"
        and review["revised_name"] == "APH(2'')-IVa"
        and review["reference"] == "PMID:19158087"
        and review["doi"] == "10.1074/jbc.M808148200"
        and review["decision"] == "EXPLICIT_REFERENCE_NOMENCLATURE_RELATION_VERIFIED"
        and review["review_medium"] == "PUBLISHER_INDEXED_PRIMARY_DISCUSSION_TEXT"
        and review["scope"] == "NAME_RELATION_ONLY_NOT_SEQUENCE_EQUIVALENCE_OR_EXPERIMENTAL_ALLELE_ASSIGNMENT"
        and all(
            review[k] is False
            for k in (
                "native_primary_file_cached",
                "table_5_visually_inspected",
                "figures_visually_inspected",
                "supplements_inspected",
                "whole_paper_review_complete",
            )
        ),
        "historical nomenclature evidence or its limits changed",
    )
    path = structural["links"][TERM]
    (structure,) = path["structures"]
    (entity,) = structure["entities"]
    require(
        path["source_label"] == review["revised_name"]
        and path["source_xrefs"] == ["PDB:3N4T"]
        and structure["pdb_id"] == "3N4T"
        and entity["entity_id"] == "3N4T_1"
        and entity["reference_accessions"] == [ACCESSION]
        and entity["source_organisms"]
        == [{"ncbi_taxonomy_id": 37734, "scientific_name": "Enterococcus casseliflavus"}]
        and path["experimental_assignment"] is False,
        "structural reference path changed",
    )
    taxonomy = project_taxon(taxon, 37734, "Enterococcus casseliflavus")
    genes = [g["geneName"]["value"] for g in entry.get("genes", []) if "geneName" in g]
    require(
        not {"sequence", "features"} & set(entry)
        and entry["primaryAccession"] == "O68183"
        and entry["entryType"] == "UniProtKB unreviewed (TrEMBL)"
        and entry["entryAudit"] == {"entryVersion": 113, "sequenceVersion": 1}
        and all(type(v) is int for v in entry["entryAudit"].values())
        and genes == ["aph(2'')-Id"]
        and protein_names(entry) == [{"field": "submissionNames", "index": 0, "value": "APH(2'')-Id"}]
        and entry["organism"]["taxonId"] == taxon["taxonId"]
        and entry["organism"]["scientificName"] == taxon["scientificName"]
        and entry["uniProtKBCrossReferences"] == []
        and entry["proteinDescription"].get("flag") is None,
        "native reference identity changed",
    )
    bibliography = []
    for item in entry["references"]:
        citation = item["citation"]
        bibliography.append(
            {
                "reference_number": item["referenceNumber"],
                "citation_type": citation["citationType"],
                "identifiers": citation.get("citationCrossReferences", []),
                "citation_sha256": checksum(citation),
            }
        )
    require(
        [b["reference_number"] for b in bibliography] == list(range(1, 12))
        and Counter(b["citation_type"] for b in bibliography) == {"journal article": 10, "submission": 1}
        and bibliography[0]["identifiers"] == [{"database": "PubMed", "id": "9593155"}],
        "native bibliography or focal citation changed",
    )
    old = nomenclature["proteins"]["O68183"]
    require(
        old["entry_audit"] == entry["entryAudit"]
        and old["entry_type"] == entry["entryType"]
        and old["organism"] == entry["organism"]
        and old["gene_names_with_provenance"] == entry["genes"]
        and old["experimental_assignment"] is False,
        "historical and citation-native reference identities disagree",
    )
    return {
        "accession": ACCESSION,
        "entry_type": entry["entryType"],
        "entry_audit": entry["entryAudit"],
        "gene_symbols": genes,
        "protein_names": protein_names(entry),
        "reference_taxonomy": taxonomy,
        "native_bibliography": bibliography,
        "source_citation": "PMID:9593155",
        "historical_nomenclature_review": review,
        "structural_reference": {"pdb_id": "3N4T", "entity_id": "3N4T_1", "protein_accession": ACCESSION},
        "scope": QUALIFIED,
        "explicit_card_xref": False,
        "submission_name_is_expert_review": False,
        "native_protein_flag": None,
        "unflagged_means_complete": False,
        "nomenclature_primary_text_replayed_here": False,
        "new_primary_results_review": False,
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
        "experimental_genome_assignment": None,
    }


def build(root, plan_path=PLAN):
    plan = json.loads((root / plan_path).read_bytes())
    data, records, claims = public_context(root, plan)
    pools, queries, union = {}, {}, {}
    for pmid, item in plan["queries"].items():
        entries, query = literature.read_query(root, root / item["directory"], pmid)
        require(
            query == item["query"]
            and query["complete_for_query"]
            and query["release"] == "2026_03"
            and sorted(entries) == item["accessions"],
            "cached citation query changed",
        )
        pools[pmid], queries[pmid] = entries, query
        for accession, entry in entries.items():
            require(accession not in union or union[accession] == entry, "cross-query entry conflict")
            require(not {"sequence", "features"} & set(entry), "unexpected sequence or variant data")
            union[accession] = entry
    taxon, tax_source = read_source(root, plan["reference_taxonomy"])
    protein = project_reference(union["O68183"], taxon, data["nomenclature"], data["structural"])
    require(
        [g["geneName"]["value"] for g in union["Q9AF71"]["genes"] if "geneName" in g] == ["aph"]
        and {
            g["geneName"]["value"]
            for e in pools["29317655"].values()
            for g in e.get("genes", [])
            if "geneName" in g
        }
        == {"mphB", "mphH", "mphK", "mphC"}
        and len(pools["17526756"]) == 16,
        "ambiguity-note evidence changed",
    )
    terms = {}
    for tid, label in sorted(plan["terms"].items()):
        definition = data["definition_citations"]["terms"][tid]
        pmids = [p.removeprefix("PMID:") for p in definition["definition_citation_ids"]]
        accessions = sorted({a for p in pmids for a in pools[p]})
        exact = [
            a
            for a in accessions
            if name_matches(union[a], label) or any(literature.literature.match_entry(union[a], tid, label))
        ]
        require(exact == [], "new literal name or CARD match requires review")
        if tid == TERM:
            require(accessions == ["O68183"], "qualified citation pool changed")
        status = QUALIFIED if tid == TERM else UNMATCHED if accessions else EMPTY
        terms[tid] = {
            "source_label": label,
            "definition_citation_ids": definition["definition_citation_ids"],
            "definition_annotation_sha256": checksum(definition),
            "status": status,
            "record_memberships": data["index"]["terms"][tid]["record_memberships"],
            "complete_citation_query_accessions": ["UniProtKB:" + a for a in accessions],
            "reference_candidates": [ACCESSION] if tid == TERM else [],
            "other_citation_hits_not_selected": ["UniProtKB:" + a for a in accessions if tid != TERM],
            "literal_name_match_found": False,
            "experimental_subject_assignment": False,
            "biological_absence_inferred": False,
        }
    memberships = [
        {
            "record_identifier": rid,
            "source_term_id": TERM,
            "protein_accession": ACCESSION,
            "scope": QUALIFIED,
            "experimental_subject_assignment": False,
        }
        for rid in terms[TERM]["record_memberships"]
    ]
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / plan_path),
        "inputs": plan["inputs"],
        "terms": terms,
        "records": records,
        "claims": claims,
        "references": {ACCESSION: protein},
        "reference_memberships": memberships,
        "reference_taxonomy_source": tax_source,
        "citation_queries": queries,
        "unselected_citation_entry_metadata": {
            "UniProtKB:" + a: {
                "entry_sha256": checksum(e),
                "entry_type": e["entryType"],
                "entry_audit": e["entryAudit"],
                "native_taxon_id": e["organism"]["taxonId"],
                "native_taxonomy_independently_reviewed_here": False,
            }
            for a, e in sorted(union.items())
            if a != "O68183"
        },
        "ambiguity_notes": {
            "ARO:3004675": (
                "Q9AF71 carries the generic gene label aph, not an explicit aphA15 alias; "
                "no exact assignment."
            ),
            "mph_label_cohort": (
                "The shared citation returns entries named mphB, mphH, mphK and mphC, not the five focal "
                "source labels; no substitution of family members."
            ),
            "ARO:3002602": (
                "The 16 citation hits do not identify aadA2 by the selected literal gene/protein name "
                "or CARD fields."
            ),
            "prefix_scope": (
                "Label-prefix selection is not an enzyme-family assertion; aadT is retained without "
                "inferring an enzymatic role."
            ),
        },
        "inherited_access_limitations": data["nomenclature"]["access_limitations"],
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(records),
            "source_terms": len(terms),
            "source_claims": len(claims),
            "complete_cached_citation_queries": len(queries),
            "citation_query_entries": sum(len(e) for e in pools.values()),
            "distinct_citation_entries": len(union),
            "term_statuses": dict(sorted(Counter(t["status"] for t in terms.values()).items())),
            "qualified_reference_terms": 1,
            "qualified_reference_proteins": 1,
            "qualified_reference_memberships": len(memberships),
        },
        "limits": {
            "network_requests": 0,
            "ncbi_requests": 0,
            "biological_records_changed": 0,
            "new_primary_results_reviews": 0,
            "experimental_assignments": 0,
            "curated_ast_observations": 0,
            "primary_access_holds_retried": 0,
            "source_adoptions": 0,
            "outreach": 0,
            "github_mutations": 0,
            "all_aliases_or_sources_searched": False,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "whole_record_primary_signoffs": 0,
            "broad_index_updated": False,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": (
            "CARD/ARO ontology and UniProt release 2026_03, CC BY 4.0; RCSB/wwPDB metadata CC0. "
            "Historical primary nomenclature assessment retained with its limits; "
            "no article text redistributed."
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
