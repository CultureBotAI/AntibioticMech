"""Bind a shared primary paper's table scope to current Mex claims, offline."""

import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_mex_host_context as host

members, mex = host.members, host.mex
reference, require, read_json = host.reference, host.require, host.read_json
PREFIX = "research/2026-10-15-mex-substrate-context"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
SCOPE = "MEX_SHARED_PRIMARY_TABLE_SCOPE_NOT_EXPERIMENTAL_ALLELE_ASSIGNMENT"
PMID, DOI = "11083635", "10.1128/aac.44.12.3322-3327.2000"
TERMS = {**host.TERMS, "ARO:3003032": "MexXY-OprM"}
COMPONENTS = {
    **host.COMPONENTS,
    "ARO:3003032": {"mexX": "UniProtKB:G3XD21", "mexY": "UniProtKB:G3XCW2", "oprM": "UniProtKB:Q51487"},
}
TABLE_SCOPE = {
    "CHEBI:2637": ("amikacin", 2, "amikacin"),
    "CHEBI:28971": ("ampicillin", None, None),
    "CHEBI:2955": ("azithromycin", None, None),
    "CHEBI:161680": ("aztreonam", 3, "aztreonam"),
    "CHEBI:3508": ("ceftazidime", 3, "ceftazidime"),
    "CHEBI:29007": ("ceftriaxone", 3, "ceftriaxone"),
    "CHEBI:17698": ("chloramphenicol", 2, "chloramphenicol"),
    "CHEBI:100241": ("ciprofloxacin", 2, "ciprofloxacin"),
    "CHEBI:59064": ("colistin A", None, None),
    "CHEBI:59673": ("colistin B", None, None),
    "CHEBI:42355": ("erythromycin A", 2, "erythromycin"),
    "antibioticmech:aro-6407ce57f1": ("gentamicin C", 2, "gentamicin"),
    "CHEBI:43968": ("meropenem", 3, "meropenem"),
    "CHEBI:100246": ("norfloxacin", 2, "norfloxacin"),
    "CHEBI:28368": ("novobiocin", 2, "novobiocin"),
    "antibioticmech:aro-2eea3233f3": ("ofloxacin", 2, "ofloxacin"),
    "CHEBI:7911": ("panipenem", None, None),
    "CHEBI:27902": ("tetracycline", 2, "tetracycline"),
    "CHEBI:28864": ("tobramycin", 2, "tobramycin"),
    "CHEBI:45924": ("trimethoprim", None, None),
    "antibioticmech:aro-1fe0873afd": ("acriflavine", None, None),
}
NEGATIVE = ("ARO:3000797", "antibioticmech:aro-6407ce57f1")
NO_INCREASE = "NO_RESISTANCE_INCREASE_IN_SELECTED_COMPARISON_NOT_GLOBAL_ABSENCE"
FALSE_FIELDS = (
    "figure_images_visually_reviewed",
    "typeset_tables_visually_verified",
    "all_backgrounds_interchangeable",
    "numeric_ast_exported",
    "clinical_resistance_calls_assigned",
    "exact_chemical_forms_verified",
    "experimental_alleles_assigned",
    "experimental_genomes_assigned",
    "whole_claim_primary_signoff",
    "biological_curation_completed",
    "operational_details_exported",
    "manual_primary_reading_independently_verified_by_code",
)
BIBLIOGRAPHY = {
    "G3XCW2": ("mexY", "PA2018", 3, ["FUNCTION"]),
    "G3XD21": ("mexX", "PA2019", 3, ["FUNCTION", "SUBCELLULAR LOCATION"]),
    "Q51487": ("oprM", "PA0427", 12, ["FUNCTION"]),
}


def validate_assessment(notes):
    require(notes["scope"] == SCOPE, "assessment scope changed")
    require(all(notes[k] is False for k in FALSE_FIELDS), "evidence scope promoted")
    citation = notes["citation"]
    require(
        citation["pmid"] == PMID
        and citation["doi"] == DOI
        and citation["url"] == "https://journals.asm.org/doi/" + DOI
        and citation["classification"] == "PRIMARY_TEXT_CONTEXT_REVIEW_NOT_WHOLE_PAPER_SIGNOFF"
        and citation["relationship_to_card_definitions"]
        == "ADJACENT_PRIMARY_EVIDENCE_NOT_OWN_DEFINITION_CITATION"
        and bool(citation["locations"]),
        "citation identity or ownership changed",
    )
    require(
        notes["assay_species"] == "Pseudomonas aeruginosa"
        and notes["parental_background_label"] == "PAO1"
        and notes["subject_scope"] == "DISTINCT_EXPERIMENTAL_DERIVATIVES_NOT_ONE_REFERENCE_ACCESSION"
        and notes["endpoint"] == "MIC"
        and notes["source_units"] == "ug/mL"
        and notes["standard_units"] == "mg/L"
        and notes["unit_conversion_factor"] == 1,
        "subject or measurement context changed",
    )
    require(
        notes["record_table_scope"]
        == {k: {"table": t, "source_label": s} for k, (_, t, s) in TABLE_SCOPE.items()}
        and notes["non_supporting_selected_comparisons"]
        == [
            {
                "aro_id": NEGATIVE[0],
                "record_identifier": NEGATIVE[1],
                "table": 2,
                "status": NO_INCREASE,
            }
        ]
        and notes["rejected_label_substitutions"]
        == {
            "CHEBI:28971": "amoxicillin",
            "CHEBI:59064": "polymyxin B",
            "CHEBI:59673": "polymyxin B",
            "CHEBI:7911": "S-4661",
        },
        "selected table scope or negative comparison changed",
    )
    require(
        notes["cross_study_qualification"]
        == "CURRENT_TABLE_CONTEXT_DOES_NOT_SUPERSEDE_PRIOR_STUDY_SPECIFIC_LIMITS",
        "cross-study limit lost",
    )
    require(
        notes["access"]
        == {
            "web_search_queries": 0,
            "web_reader_open_operations": 5,
            "web_reader_find_operations": 0,
            "web_service_upstream_http_request_count_known": False,
            "new_native_publisher_requests": 0,
            "new_uniprot_requests": 0,
            "ncbi_requests": 0,
            "access_holds_retried": False,
            "outreach": False,
            "reuse_terms_review_resumed": False,
        },
        "access accounting changed",
    )


def citation_owners(definitions):
    return sorted(
        t for t, row in definitions["terms"].items() if "PMID:" + PMID in row["definition_citation_ids"]
    )


def bibliography_bindings(entries, views):
    result = {}
    for accession, entry in entries.items():
        rows = [
            r
            for r in entry["references"]
            if {"database": "PubMed", "id": PMID} in r["citation"].get("citationCrossReferences", [])
        ]
        if not rows:
            continue
        require(accession in BIBLIOGRAPHY and len(rows) == 1, "selected bibliography coverage changed")
        gene, locus, number, positions = BIBLIOGRAPHY[accession]
        row, view = rows[0], views["UniProtKB:" + accession]
        require(
            row["referenceNumber"] == number
            and row["referencePositions"] == positions
            and not row.get("referenceComments")
            and {"database": "DOI", "id": DOI} in row["citation"]["citationCrossReferences"]
            and row["citation"]["citationType"] == "journal article"
            and view["gene_symbols"] == [gene]
            and view["ordered_locus_names"] == [locus],
            "selected bibliography or native gene identity changed",
        )
        result["UniProtKB:" + accession] = {
            "reference_number": number,
            "identifiers": row["citation"]["citationCrossReferences"],
            "reference_positions": positions,
            "reference_comments": row.get("referenceComments", []),
            "citation_sha256": members.screen.checksum(row["citation"]),
            "complete_native_reference_sha256": members.screen.checksum(row),
            "independent_experiment_per_protein": False,
            "experimental_subject_assignment": False,
        }
    require(set(result) == {"UniProtKB:" + a for a in BIBLIOGRAPHY}, "selected bibliography coverage changed")
    require(len({r["citation_sha256"] for r in result.values()}) == 1, "shared citation identity changed")
    return result


def dispositions(claims, records, previous):
    by_id = {r["identifier"]: r for r in records}
    require(len(by_id) == len(records) and set(by_id) == set(TABLE_SCOPE), "record scope changed")
    require(all(by_id[k]["label"] == v[0] for k, v in TABLE_SCOPE.items()), "record label changed")
    keyed = {(c["aro_id"], c["record_identifier"]): c for c in claims}
    old = {(c["aro_id"], c["record_identifier"]): c for c in previous}
    require(
        len(keyed) == len(claims) == len(old) == len(previous) == 33 and set(keyed) == set(old),
        "complete claim context changed",
    )
    require(all(c["aro_id"] in TERMS for c in claims), "unknown source term")
    result = []
    for c in claims:
        rid, tid = c["record_identifier"], c["aro_id"]
        record, before = by_id[rid], old[(tid, rid)]
        require(
            before["claim_sha256"] == c["claim_sha256"]
            and before["standard_inchi_key"] == c["standard_inchi_key"] == record["standard_inchi_key"],
            "claim or chemical identity changed",
        )
        table, label = TABLE_SCOPE[rid][1:]
        relation = (
            "NOT_LISTED_IN_SELECTED_TABLES"
            if table is None
            else "SAME_LABEL_NOT_EXACT_STRUCTURE_VERIFICATION"
            if label == record["label"]
            else "GENERIC_LABEL_NOT_EXACT_RECORD_FORM"
        )
        comparison = (
            "NO_SELECTED_TABLE_COMPARISON"
            if table is None
            else NO_INCREASE
            if (tid, rid) == NEGATIVE
            else "SOURCE_CONTEXT_SUPPORTS_EFFLUX_INTERPRETATION_NOT_DIRECT_KINETICS"
        )
        result.append(
            {
                "aro_id": tid,
                "record_identifier": rid,
                "record_label": record["label"],
                "claim_sha256": c["claim_sha256"],
                "standard_inchi_key": record["standard_inchi_key"],
                "source_pmid": "PMID:" + PMID,
                "table": table,
                "source_label": label,
                "label_relation": relation,
                "comparison_status": comparison,
                "comparison_location": f"Table {table}; {TERMS[tid]} comparison and footnote"
                if table
                else None,
                "previous_study_disposition": before,
                "previous_qualification_superseded": False,
                "whole_claim_primary_signoff": False,
                "source_claim_removed": False,
                "exact_chemical_form_verified": False,
                "experimental_identity_assigned": False,
                "disposition": "KEEP_SOURCE_ASSERTION_WITHHOLD_EXPERIMENTAL_JOIN",
            }
        )
    return result


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["selected_terms"] == TERMS
        and plan["new_uniprot_requests"] == plan["ncbi_requests"] == 0
        and plan["biological_record_writes"] is plan["reuse_terms_review_resumed"] is False
        and plan["issue_1040"] == "DEFERRED",
        "research scope changed",
    )
    notes = read_json(root, plan["assessment"])
    validate_assessment(notes)
    old_mex = read_json(root, plan["prior_mex"])
    require(mex.build(root) == old_mex, "prior component audit does not reproduce")
    old = {k: read_json(root, p) for k, p in plan["prior_contexts"].items()}
    require(
        set(old) == {"host", "mexxy_definitions"}
        and all(d["inputs"] == plan["inputs"] for d in old.values()),
        "prior contexts changed",
    )
    index, update = [read_json(root, plan["inputs"][k]) for k in ("index", "corpus_update")]
    require(
        plan["definition_citations"] == index["inputs"]["definition_citations"], "definition source changed"
    )
    definitions = read_json(root, plan["definition_citations"])
    owners = citation_owners(definitions)
    require(not owners, "adjacent citation is now an own definition citation")
    records, claims = members.current_context(root, index, update, set(TERMS), TERMS)
    require(
        claims == [c for c in old_mex["claims"] if c["aro_id"] in TERMS], "component claim coverage changed"
    )
    previous_claims = [c for d in old.values() for c in d["claims"]]
    require(
        sorted(previous_claims, key=lambda c: (c["record_identifier"], c["aro_id"])) == claims,
        "previous study claim coverage changed",
    )
    reviewed = dispositions(claims, records, [c for d in old.values() for c in d["claim_dispositions"]])
    query = old_mex["queries"]["cohort"]
    expected = parse_qs(urlsplit(query["url"]).query)
    entries, query_source = mex.native_query(root, query["receipt"], expected)
    require(query_source == query, "native query provenance changed")
    taxon, tax_source = members.prior.lineages.native_taxon(
        root, old_mex["taxonomy_sources"]["208964"], "208964", "2026_03"
    )
    species, species_source = members.prior.lineages.native_taxon(
        root, old_mex["taxonomy_sources"]["287"], "287", "2026_03"
    )
    views = {}
    for tid, genes in COMPONENTS.items():
        for gene, accession in genes.items():
            entry = entries[accession.split(":")[1]]
            view = members.member_reference(entry, taxon)
            require(
                view["native_entry_sha256"]
                == old_mex["reference_candidates"][accession]["native_entry_sha256"]
                and view["gene_symbols"] == [gene]
                and view["reference_taxonomy"]["taxon_id"] == "NCBITaxon:208964"
                and view["reference_taxonomy"]["native_rank"] == "strain"
                and accession
                in old_mex["terms"][tid]["components"][gene]["native_complex_component_references"],
                "component reference identity changed",
            )
            views[accession] = view
    bindings = bibliography_bindings(entries, views)
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "assessment": plan["assessment"],
        "inputs": plan["inputs"],
        "prior_mex": plan["prior_mex"],
        "prior_contexts": plan["prior_contexts"],
        "records": records,
        "claims": claims,
        "claim_dispositions": reviewed,
        "component_bindings": COMPONENTS,
        "reference_views": views,
        "native_query_source": query_source,
        "selected_bibliography_bindings": bindings,
        "definition_citation_owners": owners,
        "preserved_definition_citations": {
            t: definitions["terms"][t]["definition_citation_ids"] for t in TERMS
        },
        "citation_relationship": notes["citation"]["relationship_to_card_definitions"],
        "paper_species_grounding": host.species_context(species, notes["assay_species"]),
        "taxonomy_sources": {"208964": tax_source, "287": species_source},
        "preserved_opra_access_hold": old["mexxy_definitions"]["preserved_opra_access_hold"],
        "summary": {
            "complete_selected_records_read": len(records),
            "source_claims": len(claims),
            "source_terms": len(TERMS),
            "new_primary_text_contexts_reviewed": 1,
            "reused_component_references": len(views),
            "bibliography_entries_sharing_one_paper": len(bindings),
            "new_reference_accessions": 0,
            "claim_label_relations": dict(sorted(Counter(r["label_relation"] for r in reviewed).items())),
            "claim_comparison_statuses": dict(
                sorted(Counter(r["comparison_status"] for r in reviewed).items())
            ),
            "new_uniprot_requests": 0,
            "new_ncbi_requests": 0,
            "corpus_records_hash_checked": 2939,
        },
        "limits": {
            **mex.LIMITS,
            "new_primary_results_reviews": 1,
            "new_review_is_text_only_not_whole_paper_signoff": True,
            "operational_exports": False,
            "numeric_ast_exports": 0,
            "same_label_establishes_exact_structure": False,
            "table_gap_establishes_global_absence": False,
        },
        "attribution": "CARD/ARO and UniProt CC BY 4.0; manual publisher-text assessment separately cited.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    payload = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
    target = args.root / args.output
    if args.check or target.exists():
        require(target.read_bytes() == payload, "audit does not reproduce; preserve prior output")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
