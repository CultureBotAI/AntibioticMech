"""Audit every current Erm term against native names without inferring alleles."""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_complex_members as members

mex = members.prior.mex
reference, require, read_json = members.reference, members.require, mex.read_json
PREFIX = "research/2026-10-15-erm-name-context"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
SCOPE = "ALL_ERM_NATIVE_NAMES_NOT_EXPERIMENTAL_ALLELES_OR_PHENOTYPES"
ERM_C = "ARO:3000250"
PMID, DOI = "3091582", "10.1128/jb.167.3.888-892.1986"
FALSE_FIELDS = (
    "gene_symbol_mismatch_is_automatically_an_error",
    "normalized_names_establish_alleles",
    "matching_symbols_merge_taxa_or_references",
    "missing_gene_field_establishes_gene_absence",
    "previous_unselected_candidates_silently_promoted",
    "all_family_members_enumerated",
    "experimental_genomes_assigned",
    "exact_chemical_forms_verified",
    "clinical_resistance_calls_assigned",
    "numeric_ast_exported",
    "operational_details_exported",
    "figures_visually_reviewed",
    "whole_record_primary_signoffs",
    "biological_curation_completed",
    "manual_primary_reading_independently_verified_by_code",
)


def validate_assessment(notes):
    require(
        notes["scope"] == SCOPE
        and notes["selected_term"] == ERM_C
        and notes["selected_term_label"] == "ErmC",
        "primary context scope changed",
    )
    require(all(notes[k] is False for k in FALSE_FIELDS), "evidence scope promoted")
    paper = notes["primary_paper"]
    require(
        paper["pmid"] == PMID
        and paper["doi"] == DOI
        and paper["publisher_url"] == "https://journals.asm.org/doi/" + DOI
        and paper["pdf_url"] == "https://journals.asm.org/doi/pdf/" + DOI + "?download=true"
        and paper["source_gene_label"] == "ermM"
        and paper["comparison_gene_label"] == "ermC"
        and paper["source_species"] == "Staphylococcus epidermidis"
        and paper["comparison_species"] == "Staphylococcus aureus"
        and paper["reference_accession"] == "UniProtKB:P06572"
        and paper["classification"] == "PRIMARY_PDF_TEXT_CONTEXT_NOT_WHOLE_PAPER_SIGNOFF"
        and bool(paper["locations"]),
        "primary source identity changed",
    )
    require(
        all(
            paper[k] is False
            for k in (
                "reference_gene_name_rewritten",
                "source_regulatory_contexts_interchangeable",
                "all_record_structures_tested",
                "experimental_allele_identity_established",
            )
        ),
        "primary source scope promoted",
    )
    require(
        notes["access"]
        == {
            "web_search_queries": 8,
            "web_reader_open_operations": 1,
            "web_reader_click_operations": 1,
            "web_reader_screenshot_operations": 2,
            "screenshot_images_exposed_for_visual_inspection": False,
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


def cohort(root, source, index):
    with reference.check_pin(root, source).open() as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    names = {}
    for row in rows:
        term, label = row["determinant_id"], row["determinant_name"]
        require(term not in names or names[term] == label, "source term has conflicting labels")
        names[term] = label
    require(set(index["terms"]) <= set(names), "current term lacks a source label")
    return {
        t: name
        for t, name in sorted(names.items())
        if t in index["terms"] and name.casefold().startswith("erm")
    }


def native_followup(root, old):
    entries, provenance = {}, {}
    for key, search in old["searches"].items():
        request = old["requests"][key]
        receipt = read_json(root, request["receipt"])
        body = reference.check_pin(root, request["cache"]).read_bytes()
        headers = {k.lower(): v for k, v in receipt["headers"].items()}
        url = urlsplit(receipt["url"])
        params = parse_qs(url.query)
        require(
            url.scheme == "https"
            and url.netloc == "rest.uniprot.org"
            and url.path == "/uniprotkb/search"
            and receipt["url"] == request["url"]
            and not url.fragment
            and receipt["status"] == request["status"] == 200
            and receipt["cache_path"] == request["cache"]["path"]
            and receipt["bytes"] == request["bytes"] == len(body)
            and receipt["sha256"] == request["sha256"] == hashlib.sha256(body).hexdigest()
            and headers["x-uniprot-release"] == "2026_03"
            and not headers.get("link")
            and not headers.get("location")
            and params["query"] == [search["query"]]
            and params["size"] == ["500"]
            and params["format"] == ["json"]
            and "sequence" not in params["fields"][0].split(","),
            "cached follow-up query changed",
        )
        payload = json.loads(body)["results"]
        accessions = [e["primaryAccession"] for e in payload]
        require(
            len(payload) == len(set(accessions)) == int(headers["x-total-results"]) == search["result_count"]
            and set(accessions) == set(search["accessions"]),
            "follow-up query coverage changed",
        )
        for entry in payload:
            accession = entry["primaryAccession"]
            require(not {"sequence", "features"} & set(entry), "unexpected operational fields")
            require(
                accession not in entries or entries[accession] == entry, "conflicting repeated native entry"
            )
            entries[accession] = entry
        provenance[key] = request
    require(set(entries) == set(old["proteins"]) and len(entries) == 8, "previous candidate coverage changed")
    for accession, entry in entries.items():
        previous = old["proteins"][accession]
        require(
            entry.get("genes", []) == previous["gene_annotations"]
            and entry["entryAudit"] == previous["entry_audit"]
            and entry["organism"]["taxonId"] == previous["organism"]["taxonId"],
            "previous native candidate projection changed",
        )
    return entries, provenance


def lexical_relation(label, entry):
    genes = entry.get("genes", [])
    symbols = sorted({g["geneName"]["value"] for g in genes if "geneName" in g})
    synonyms = sorted({s["value"] for g in genes for s in g.get("synonyms", [])})
    normalized = label.casefold()
    if normalized in {s.casefold() for s in symbols}:
        status = "CASEFOLDED_NATIVE_SYMBOL_MATCH_NOT_ALLELE_IDENTITY"
    elif normalized in {s.casefold() for s in synonyms}:
        status = "CASEFOLDED_NATIVE_SYNONYM_MATCH_NOT_ALLELE_IDENTITY"
    elif symbols or synonyms:
        # This only flags typography for human review, never equates biological entities.
        stripped = re.sub(r"[()_\-]", "", normalized)
        punctuation = {re.sub(r"[()_\-]", "", s.casefold()) for s in symbols + synonyms}
        status = (
            "PUNCTUATION_ONLY_SIMILARITY_NOT_ALIAS_PROOF"
            if stripped in punctuation
            else "DIFFERENT_NATIVE_NAME_REQUIRES_CONTEXT_NOT_AUTOMATIC_ERROR"
        )
    else:
        status = "NO_NATIVE_SYMBOL_LOCUS_FIELDS_ONLY" if genes else "GENE_FIELD_ABSENT_NOT_GENE_ABSENCE"
    return {
        "status": status,
        "native_gene_symbols": symbols,
        "native_gene_synonyms": synonyms,
        "biological_equivalence_inferred": False,
    }


def reference_views(root, entries, lineage_data, old):
    views, sources = {}, {}
    for accession, entry in sorted(entries.items()):
        taxid = str(entry["organism"]["taxonId"])
        if taxid in lineage_data["taxa"]:
            source = lineage_data["taxa"][taxid]["native_source"]
        else:
            cached = old["requests"]["tax-" + taxid]
            source = {"receipt": cached["receipt"], "body": cached["cache"]}
        taxon, provenance = members.prior.lineages.native_taxon(root, source, taxid, "2026_03")
        views["UniProtKB:" + accession] = members.member_reference(entry, taxon)
        sources[taxid] = provenance
    return views, sources


def terms_and_claims(labels, index, definitions, old, entries, views, claims):
    terms = {}
    for term, label in labels.items():
        current = index["terms"][term]
        label_hash = hashlib.sha256(label.encode()).hexdigest()
        require(
            label_hash == current["source_label_sha256"] == definitions["terms"][term]["label_sha256"],
            "source label fingerprint changed",
        )
        selected = [link["protein_accession"] for link in current["links"]]
        previous = old["candidates"].get(term)
        earlier = ["UniProtKB:" + a for a in previous["accessions"]] if previous else []
        all_candidates = sorted(set(selected) | set(earlier))
        terms[term] = {
            "source_label": label,
            "source_label_sha256": label_hash,
            "definition_citation_ids": definitions["terms"][term]["definition_citation_ids"],
            "record_memberships": current["record_memberships"],
            "selected_index_links": current["links"],
            "earlier_candidate_context": previous,
            "prior_candidates_not_in_selected_index": sorted(set(earlier) - set(selected)),
            "native_name_relations": {
                a: lexical_relation(label, entries[a.split(":")[1]]) for a in all_candidates
            },
            "reference_taxa": sorted({views[a]["reference_taxonomy"]["taxon_id"] for a in all_candidates}),
            "reference_species": sorted(
                {
                    "NCBITaxon:" + str(views[a]["reference_taxonomy"]["species"]["taxonId"])
                    for a in all_candidates
                    if views[a]["reference_taxonomy"]["species"]
                }
            ),
            "no_reference_is_biological_absence": False,
            "primary_review": "OPEN",
        }
    dispositions = [
        {
            "aro_id": c["aro_id"],
            "record_identifier": c["record_identifier"],
            "claim_sha256": c["claim_sha256"],
            "standard_inchi_key": c["standard_inchi_key"],
            "term_context_pointer": "/terms/" + c["aro_id"],
            "selected_primary_context": "NATIVE_ERMM_REFERENCE_NOT_INTERCHANGEABLE_ERMC_EXPERIMENT"
            if c["aro_id"] == ERM_C
            else None,
            "exact_allele_assigned": False,
            "source_claim_removed": False,
            "whole_claim_primary_signoff": False,
            "disposition": "PRESERVE_SOURCE_ASSERTION_REFERENCE_METADATA_ONLY",
        }
        for c in claims
    ]
    require(
        len(dispositions) == 562 and sum(c["aro_id"] == ERM_C for c in claims) == 24,
        "selected claim coverage changed",
    )
    return terms, dispositions


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["selection"] == "ALL_CURRENT_SOURCE_LABELS_WITH_CASEFOLDED_ERM_PREFIX"
        and plan["new_uniprot_requests"] == plan["ncbi_requests"] == 0
        and plan["biological_record_writes"] is plan["reuse_terms_review_resumed"] is False
        and plan["issue_1040"] == "DEFERRED",
        "research scope changed",
    )
    notes = read_json(root, plan["assessment"])
    validate_assessment(notes)
    index, update = [read_json(root, plan["inputs"][k]) for k in ("index", "corpus_update")]
    require(
        plan["source_inventory"] == index["inputs"]["source_inventory"]
        and plan["definition_citations"] == index["inputs"]["definition_citations"],
        "source ownership changed",
    )
    labels = cohort(root, plan["source_inventory"], index)
    require(len(labels) == 47, "complete Erm cohort changed")
    records, claims = members.current_context(root, index, update, set(labels), labels)
    source_plan, snapshot = [read_json(root, plan[k]) for k in ("source_plan", "protein_snapshot")]
    native, native_pages = members.prior.replay_proteins(root, source_plan, snapshot)
    old = read_json(root, plan["prior_erm"])
    extra, queries = native_followup(root, old)
    require(not set(native) & set(extra), "separate native exports overlap; inspect before selecting one")
    selected = {
        link["protein_accession"].split(":")[1] for term in labels for link in index["terms"][term]["links"]
    }
    entries = {a: e for a, e in {**native, **extra}.items() if a in selected or a in extra}
    require(
        selected <= set(entries) and len(selected) == 44 and len(entries) == 49, "reference coverage changed"
    )
    lineages = read_json(root, plan["lineages"])
    views, tax_sources = reference_views(root, entries, lineages, old)
    for accession in selected:
        identity = index["proteins"]["UniProtKB:" + accession]["identity"]
        view = views["UniProtKB:" + accession]
        require(
            view["entry_type"] == identity["entry_type"]
            and view["entry_audit"]
            == {"entryVersion": identity["entry_version"], "sequenceVersion": identity["sequence_version"]}
            and view["reference_taxonomy"]["taxon_id"] == identity["reference_taxon_id"],
            "selected reference identity changed",
        )
    definitions = read_json(root, plan["definition_citations"])
    terms, dispositions = terms_and_claims(labels, index, definitions, old, entries, views, claims)
    rows = [
        r
        for r in entries["P06572"]["references"]
        if {"database": "PubMed", "id": PMID} in r["citation"].get("citationCrossReferences", [])
    ]
    require(
        len(rows) == 1
        and views["UniProtKB:P06572"]["gene_symbols"] == ["ermM"]
        and views["UniProtKB:P06572"]["reference_taxonomy"]["taxon_id"] == "NCBITaxon:1282"
        and {"database": "DOI", "id": DOI} in rows[0]["citation"]["citationCrossReferences"],
        "primary reference binding changed",
    )
    require(
        "PMID:" + PMID not in definitions["terms"][ERM_C]["definition_citation_ids"],
        "reference bibliography is now an own definition citation",
    )
    held = read_json(root, plan["erm36_hold"])
    read_json(root, plan["erm55_curation"])
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "assessment": plan["assessment"],
        "inputs": plan["inputs"],
        "prior_erm": plan["prior_erm"],
        "records": records,
        "claims": claims,
        "terms": terms,
        "claim_dispositions": dispositions,
        "reference_views": views,
        "native_protein_pages": native_pages,
        "reused_followup_queries": queries,
        "taxonomy_sources": tax_sources,
        "prior_identity_limits": old["identity_limits"],
        "prior_primary_contexts": old["primary_papers"],
        "preserved_erm36_hold": held,
        "preserved_erm55_curation": plan["erm55_curation"],
        "ermc_reference_citation": {
            "identifiers": rows[0]["citation"]["citationCrossReferences"],
            "reference_number": rows[0]["referenceNumber"],
            "native_reference_sha256": members.screen.checksum(rows[0]),
            "own_definition_citation": False,
            "experimental_subject_assignment": False,
        },
        "summary": {
            "complete_selected_records_read": len(records),
            "source_terms": len(terms),
            "source_claims": len(claims),
            "selected_index_reference_entries": len(selected),
            "additional_preserved_candidates": len(set(entries) - selected),
            "native_reference_entries": len(views),
            "native_reference_taxa": len(tax_sources),
            "terms_without_selected_index_reference": sum(
                not r["selected_index_links"] for r in terms.values()
            ),
            "terms_without_any_candidate_in_these_inputs": sum(
                not r["native_name_relations"] for r in terms.values()
            ),
            "native_name_relation_counts": dict(
                sorted(
                    Counter(
                        v["status"] for r in terms.values() for v in r["native_name_relations"].values()
                    ).items()
                )
            ),
            "new_primary_text_contexts_reviewed": 1,
            "claims_with_selected_primary_context": 24,
            "new_reference_accessions": 0,
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
            "native_name_match_proves_allele": False,
        },
        "attribution": "CARD/ARO and UniProt CC BY 4.0; selected primary PDF text separately cited.",
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
