"""Replay Kpn paper-locus reference matches without experimental identity assignments."""

import argparse
import json
from pathlib import Path

import audit_card_complex_members as members

reference, require = members.reference, members.require
read_json = members.prior.mex.read_json
PREFIX = "research/2026-10-15-kpn-locus"
PLAN = Path(PREFIX + "-plan.json")
NATIVE = Path(PREFIX + "-native-plan.json")
OUTPUT = Path(PREFIX + ".json")
SCOPE = "KPN_PAPER_LOCUS_REFERENCE_GROUNDING_NOT_EXPERIMENTAL_ALLELE_OR_AST_ASSIGNMENT"
TERMS = {"ARO:3004585": "Klebsiella pneumoniae KpnEF", "ARO:3004598": "Klebsiella pneumoniae KpnGH-TolC"}
LOCI = {"KP1_2583": "A0ACD7U1E6", "KP1_2584": "A0ACD7U1G2"}
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_card,lit_pubmed_id,sequence_version,version,xref_embl,xref_refseq"
)
SPECIES = {"taxonId": 573, "rank": "species", "scientificName": "Klebsiella pneumoniae"}
REFERENCE_NAME = "Klebsiella pneumoniae subsp. pneumoniae NTUH-K2044"


def parameters(locus):
    require(locus in LOCI, "unplanned locus")
    return {
        "query": f"gene_exact:{locus} AND taxonomy_id:573",
        "format": "json",
        "size": 100,
        "sort": "accession asc",
        "fields": FIELDS,
    }


def validate_assessment(notes):
    require(
        notes["scope"] == SCOPE
        and notes["doi"] == "10.1128/aac.02284-12"
        and notes["pmid"] == "23836167"
        and notes["source_url"] == "https://journals.asm.org/doi/10.1128/aac.02284-12"
        and notes["source_kind"] == "PUBLISHER_HTML_PRIMARY_TEXT_NOT_VISUAL_PDF_REVIEW"
        and notes["paper_species_name"] == SPECIES["scientificName"]
        and notes["paper_reference_background"] == "NTUH-K2044"
        and notes["paper_comparison_background"] == "MGH78578"
        and notes["paper_locus_pair"] == list(LOCI)
        and notes["pair_label"] == "kpnEF"
        and notes["reference_genome_label"] == "NC_012731"
        and notes["reference_genome_namespace"] == "RefSeq"
        and notes["native_and_heterologous_backgrounds_separate"] is True,
        "primary identity or reference scope changed",
    )
    require(
        all(
            notes[key] is False
            for key in (
                "individual_locus_to_kpnE_or_kpnF_assignment",
                "reference_genome_version_reported_in_selected_text",
                "reference_genome_independently_verified",
                "reference_genome_is_experimental_derivative",
                "loss_of_function_sensitivity_is_new_resistant_allele",
                "numerical_ast_review_completed",
                "exact_assay_compound_mapping_completed",
                "figures_and_supplements_visually_reviewed",
                "whole_paper_signoff",
                "sequence_variant_primer_coordinate_construct_protocol_exports",
                "ncbi_links_followed",
                "manual_reading_independently_reproduced_by_code",
            )
        ),
        "primary assessment promoted beyond inspected evidence",
    )


def query_entry(receipt, locus):
    members.prior.card.common.validate_cached_response(
        receipt, "https://rest.uniprot.org/uniprotkb/search", parameters(locus)
    )
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    entries = json.loads(receipt["body"])["results"]
    require(
        len(entries) == int(headers["x-total-results"]) == 1
        and not headers.get("link")
        and headers["x-uniprot-release"] == "2026_03"
        and receipt["bytes"] == len(receipt["body"].encode())
        and receipt["retries"] == receipt["redirects_followed"] == 0,
        "incomplete, paginated or changed native query",
    )
    (entry,) = entries
    require(entry["primaryAccession"] == LOCI[locus], "locus query returned another reference")
    return entry


def locus_reference(entry, taxon, locus):
    projected = members.member_reference(entry, taxon)
    require(
        entry["primaryAccession"] == LOCI[locus]
        and locus in projected["ordered_locus_names"] + projected["orf_names"]
        and entry["organism"]["scientificName"] == taxon["scientificName"] == REFERENCE_NAME
        and taxon["taxonId"] == 484021
        and taxon["rank"] == "strain"
        and projected["reference_taxonomy"]["species"] == SPECIES,
        "exact native locus or reference taxonomy changed",
    )
    xrefs = entry.get("uniProtKBCrossReferences", [])
    refseq = [x for x in xrefs if x["database"] == "RefSeq"]
    embl = [x for x in xrefs if x["database"] == "EMBL"]
    require(len(refseq) == len(embl) == 1, "ambiguous native reference cross-references")
    require(
        refseq[0]["properties"] == [{"key": "NucleotideSequenceId", "value": "NC_012731.1"}]
        and refseq[0]["id"].startswith("WP_")
        and embl[0]["id"] == "AP006725",
        "native reference nucleotide context changed",
    )
    bibliography = [
        {
            "reference_number": r["referenceNumber"],
            "reference_positions": r.get("referencePositions", []),
            "strain_comments": [c["value"] for c in r.get("referenceComments", []) if c["type"] == "STRAIN"],
            "complete_native_reference_sha256": members.screen.checksum(r),
        }
        for r in entry["references"]
    ]
    require(
        len(bibliography) == 1 and bibliography[0]["strain_comments"] == ["NTUH-K2044"],
        "reference bibliography background changed",
    )
    return {
        "paper_locus": locus,
        "reference": projected,
        "native_gene_synonyms": sorted(
            {s["value"] for g in entry.get("genes", []) for s in g.get("synonyms", [])}
        ),
        "native_reference_cross_references": refseq + embl,
        "reference_bibliography_context": bibliography,
        "join_basis": "EXACT_PAPER_LOCUS_IN_NATIVE_ORF_OR_ORDERED_LOCUS_FIELD_AND_REFERENCE_BACKGROUND",
        "individual_kpn_component_alias_assigned": False,
        "genome_context": {
            "paper_reference_label": "NC_012731",
            "uniprot_nucleotide_cross_reference": "NC_012731.1",
            "paper_label_matches_unversioned_reference": True,
            "paper_reports_selected_version": False,
            "native_nucleotide_provider_independently_verified": False,
            "nucleotide_cross_reference_is_assembly_identifier": False,
            "experimental_derivative_genome_assigned": False,
        },
    }


def compare_member_reference(projected):
    species = projected["reference_taxonomy"]["species"]
    require(species is not None, "reference species unresolved")
    same_species = species == SPECIES
    return {
        "source_species": SPECIES,
        "reference_species": species,
        "species_comparison": "SAME_SPECIES_NOT_EXPERIMENTAL_IDENTITY"
        if same_species
        else "DIFFERENT_REFERENCE_SPECIES_WITHHOLD_EXPERIMENTAL_JOIN",
        "paper_reference_taxon_match": projected["reference_taxonomy"]["taxon_id"] == "NCBITaxon:484021",
        "exact_paper_locus_present": bool(
            set(LOCI) & set(projected["ordered_locus_names"] + projected["orf_names"])
        ),
        "native_card_annotation_removed": False,
        "experimental_subject_assigned": False,
    }


def request_accounting(root, plan, native):
    frozen = read_json(root, native["taxonomy_plan"])
    accepted = read_json(root, native["canary"])
    require(
        native["plan"] == frozen["plan"] == reference.pin(root, root / PLAN)
        and native["new_uniprot_requests"] == 3
        and set(native["queries"]) == set(LOCI)
        and set(native["native_taxonomy"]) == {"484021"}
        and frozen["native_taxonomy"] == {}
        and frozen["missing"] == {"484021": "https://rest.uniprot.org/taxonomy/484021.json"},
        "frozen request scope changed",
    )
    receipts = {**native["queries"], "tax-484021": native["native_taxonomy"]["484021"]["receipt"]}
    require(set(native["attempts"]) == set(receipts), "attempt coverage changed")
    cache = (root / native["taxonomy_plan"]["path"]).parent
    require(
        set(cache.glob("*-attempt.json")) == {root / p["path"] for p in native["attempts"].values()}
        and not list(cache.glob("*-error.json")),
        "unaccounted request attempt or error",
    )
    for key, pin in receipts.items():
        receipt, attempt = read_json(root, pin), read_json(root, native["attempts"][key])
        expected = plan["queries"][key]["url"] if key in LOCI else frozen["missing"]["484021"]
        require(
            receipt["url"] == attempt["url"] == expected
            and receipt["status"] == 200
            and attempt["ncbi_requests"] == 0
            and receipt["bytes"] == len(receipt["body"].encode())
            and all(item[k] == 0 for item in (receipt, attempt) for k in ("redirects_followed", "retries")),
            "native request differs from plan",
        )
    require(
        plan["canary"] == accepted["locus"] == "KP1_2583"
        and accepted["accepted"] is accepted["reference_only"] is True
        and accepted["accession"] == LOCI["KP1_2583"]
        and accepted["receipt"] == native["queries"]["KP1_2583"],
        "canary binding changed",
    )


def build(root):
    plan, native = [json.loads((root / p).read_bytes()) for p in (PLAN, NATIVE)]
    require(
        plan["scope"] == SCOPE
        and plan["terms"] == TERMS
        and plan["loci"] == list(LOCI)
        and plan["fields"] == FIELDS
        and plan["biological_record_writes"] is False
        and plan["ncbi_requests"] == plan["retries"] == plan["redirects_followed"] == 0
        and plan["issue_1040"] == "DEFERRED"
        and plan["reuse_terms_review_resumed"] is False,
        "research scope changed",
    )
    for locus in LOCI:
        require(plan["queries"][locus]["parameters"] == parameters(locus), "query plan changed")
    notes = read_json(root, plan["assessment"])
    validate_assessment(notes)
    request_accounting(root, plan, native)
    prior, old_kpn = [read_json(root, plan[k]) for k in ("prior_members", "prior_kpn")]
    require(
        old_kpn["primary_context"]["paper_organism_name"] == SPECIES["scientificName"],
        "prior KpnGH paper organism changed",
    )
    index, update = [read_json(root, plan["inputs"][k]) for k in ("index", "corpus_update")]
    require(
        plan["inputs"] == prior["inputs"] and plan["source_plan"] == prior["native_source_plan"],
        "prior source binding changed",
    )
    for key in ("source_queue", "source_inventory"):
        reference.check_pin(root, index["inputs"][key])
    records, claims = members.current_context(root, index, update, set(TERMS), TERMS)
    require(
        len(records) == 26
        and len(claims) == 28
        and claims == [c for c in prior["claims"] if c["aro_id"] in TERMS],
        "source cohort changed",
    )
    taxon, source = members.prior.lineages.native_taxon(
        root, native["native_taxonomy"]["484021"], "484021", "2026_03"
    )
    loci = {
        locus: locus_reference(query_entry(read_json(root, native["queries"][locus]), locus), taxon, locus)
        for locus in LOCI
    }
    source_plan = read_json(root, plan["source_plan"])
    entries, pages = members.prior.replay_proteins(
        root, source_plan, read_json(root, source_plan["inputs"]["proteins"])
    )
    parents = {t: prior["parents"][t] for t in TERMS}
    selected = sorted({a for p in parents.values() for a in p["reference_accessions"]})
    require(len(selected) == 4, "prior member selection changed")
    existing = {}
    for accession in selected:
        expected = prior["reference_proteins"][accession]
        taxid = expected["reference_taxonomy"]["taxon_id"].split(":")[1]
        old_taxon, _ = members.prior.lineages.native_taxon(
            root, prior["taxonomy_sources"][taxid], taxid, "2026_03"
        )
        projected = members.member_reference(entries[accession.split(":")[1]], old_taxon)
        require(projected == expected, "prior native reference changed")
        existing[accession] = {"reference": projected, "comparison": compare_member_reference(projected)}
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "native_plan": reference.pin(root, root / NATIVE),
        "assessment": plan["assessment"],
        "prior_members": plan["prior_members"],
        "prior_kpn": plan["prior_kpn"],
        "inputs": plan["inputs"],
        "records": records,
        "claims": claims,
        "parents": parents,
        "locus_references": loci,
        "existing_member_references": existing,
        "taxonomy_source": source,
        "native_prior_protein_pages": pages,
        "disposition": "REFERENCE_GROUNDING_ONLY_WITHHOLD_EXPERIMENTAL_ALLELE_AND_AST_ASSIGNMENTS",
        "manual_reading_independently_verified_by_code": False,
        "summary": {
            "complete_records_read": len(records),
            "source_claims": len(claims),
            "source_terms": len(TERMS),
            "exact_paper_locus_reference_matches": len(loci),
            "prior_member_references_preserved": len(existing),
            "prior_members_with_different_species": sum(
                x["comparison"]["reference_species"] != SPECIES for x in existing.values()
            ),
            "native_protein_entries_replayed": len(entries),
            "native_protein_pages_replayed": len(pages),
            "corpus_records_hash_checked": 2939,
            "new_uniprot_requests": 3,
            "new_primary_text_contexts_reviewed": 1,
        },
        "limits": {
            **members.prior.mex.LIMITS,
            "new_primary_results_reviews": 1,
            "new_review_is_text_only_not_whole_paper_signoff": True,
            "operational_exports": False,
            "numeric_ast_exports": 0,
        },
        "attribution": (
            "CARD/ARO and UniProt metadata under CC BY 4.0; "
            "manual publisher-text assessment separately cited."
        ),
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
