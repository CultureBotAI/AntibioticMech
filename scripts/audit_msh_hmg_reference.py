"""Replay MSH2/Hmg1 references without turning mutator context into MIC or target claims."""

import argparse
import hashlib
import json
from pathlib import Path

import audit_bla_primary_identifiers as native
import audit_card_gene_reference_followup as cached
import audit_card_literature_expansion as literature
import audit_card_reference_lineages as taxonomy
import audit_card_reference_memberships as memberships
import audit_sal_reference_context as sal
import audit_topoisomerase_references as reference
from audit_curator_resistance_fields import owner

from antibioticmech.activity_collections import load_record

require = native.require
PREFIX = "research/2026-10-15-msh-hmg-reference"
PLAN = Path(PREFIX + "-audit-plan.json")
OUTPUT = Path(PREFIX + ".json")
TERMS = {"msh": "ARO:3009134", "hmg": "ARO:3007670"}
QUERY = "gene_exact:MSH2 AND organism_id:284593"
IDENTITIES = {
    "msh": ("Q6FQA9", "MSH2", "CAGL0I07733g", 284593, 5478, False),
    "hmg": ("Q4WHZ1", "hmg1", "AFUA_2G03700", 330879, 746128, True),
}


def read(root, pin):
    return json.loads(reference.check_pin(root, pin).read_bytes())


def paper_ids(entry):
    return {
        (x["database"], x["id"])
        for r in entry.get("references", [])
        for x in r["citation"].get("citationCrossReferences", [])
    }


def select_reference(key, entries, taxon, species, paper):
    sal.metadata_only(entries)
    accession, symbol, locus, taxid, species_id, reviewed = IDENTITIES[key]
    require(
        len(entries) == 1 and entries[0]["primaryAccession"] == accession, "ambiguous reference candidate"
    )
    entry = entries[0]
    locus_field = "orderedLocusNames" if key == "msh" else "orfNames"
    locus_matches = [
        {"field": f"genes/{i}/{locus_field}/{j}", "value": row["value"]}
        for i, gene in enumerate(entry.get("genes", []))
        for j, row in enumerate(gene.get(locus_field, []))
        if row["value"] == locus
    ]
    require(
        len(entry.get("genes", [])) == 1 and cached.native_matches(entry, symbol) and len(locus_matches) == 1,
        "gene/locus mismatch",
    )
    _, ancestor = taxonomy.lineage(taxon)
    taxonomy.lineage(species)
    require(
        taxon["taxonId"] == taxid
        and taxon["rank"] == "strain"
        and entry["organism"]["scientificName"] == taxon["scientificName"]
        and species["taxonId"] == species_id
        and species["rank"] == "species"
        and ancestor == taxonomy.identity(species),
        "reference lineage changed",
    )
    source_context = sal.species_context([species], paper["source_species"])
    projected = reference.project_reference(entry, symbol, species_id, taxon, reviewed=reviewed)
    own = {("PubMed", paper["pmid"]), ("DOI", paper["doi"])}
    matching_citations = [
        r
        for r in entry.get("references", [])
        if own <= {(x["database"], x["id"]) for x in r["citation"].get("citationCrossReferences", [])}
    ]
    require(len(matching_citations) == (1 if key == "hmg" else 0), "ambiguous own primary citation")
    own_present = bool(matching_citations)
    require(own_present == (key == "hmg"), "own primary citation needs reassessment")
    return {
        "accession": "UniProtKB:" + accession,
        "native_reference": projected,
        "native_gene_matches": cached.native_matches(entry, symbol),
        "native_locus_matches": locus_matches,
        "source_species_context": source_context,
        "own_primary_citation_present_in_uniprot": own_present,
        "reference_basis": "SOURCE_GENE_LOCUS_AND_REFERENCE_STRAIN_MATCH"
        if key == "msh"
        else "SOURCE_GENE_OWN_CITATION_AND_REFERENCE_STRAIN_MATCH",
        "scope": "ONE_SOURCE_SPECIES_GENE_REFERENCE_NOT_FAMILY_WIDE_OR_EXPERIMENTAL_ALLELE",
        "experimental_protein_assignment": None,
        "experimental_allele_assignment": None,
        "experimental_strain_taxon_assignment": None,
        "experimental_genome_assignment": None,
        "direct_drug_target_inferred": False,
        "resistance_phenotype_from_protein_annotation": False,
    }


def hmg_candidates(entries):
    require(set(entries) == {"Q4WHZ1", "B0YA65"}, "citation pool changed")
    sal.metadata_only(entries)
    for entry in entries.values():
        require(("PubMed", "30940706") in paper_ids(entry), "own citation absent from pool")
    other = entries["B0YA65"]
    require(
        cached.native_matches(other, "erg10B") and not cached.native_matches(other, "hmg1"),
        "same-paper comparator identity changed",
    )
    return [entries["Q4WHZ1"]], {
        "accession": "UniProtKB:B0YA65",
        "native_gene": "erg10B",
        "reason": "SAME_CITATION_DIFFERENT_GENE_NOT_HMG1",
        "eligible_as_hmg1_reference": False,
        "experimental_identifiers_assigned": False,
    }


def validate_assessment(assessment):
    papers = assessment["terms"]
    require(set(papers) == set(TERMS), "assessment cohort changed")
    for key, term in TERMS.items():
        accession, gene, locus, taxid, species_id, _ = IDENTITIES[key]
        paper = papers[key]
        require(
            paper["aro_id"] == term
            and paper["source_gene"] == gene
            and paper["reference_taxon_id"] == taxid
            and paper["reference_species_taxon_id"] == species_id
            and paper["direct_drug_target_established"] is False,
            "source/reference scope changed",
        )
        if key == "msh":
            require(
                paper["source_locus"] == locus
                and paper["query"] == QUERY
                and paper["endpoint_is_mic"] is False
                and paper["single_identity_for_whole_msh_family"] is False
                and paper["later_primary"]["cohorts_pooled"] is False,
                "MSH evidence types conflated",
            )
        else:
            require(
                paper["reference_candidate"] == "UniProtKB:" + accession
                and paper["native_reference_locus"] == locus
                and paper["all_aspergillus_species_grounded"] is False
                and paper["experimental_background_is_af293"] is False,
                "Hmg reference and experimental scope conflated",
            )
    limits = assessment["constraints"]
    require(
        limits
        == {
            "primary_access": "SELECTED_PUBLISHER_WEB_TEXT_AND_ENDPOINT_HEADINGS",
            "native_primary_bodies_replayed": False,
            "whole_papers_reviewed": False,
            "figure_pixels_reviewed": False,
            "supplements_reviewed": False,
            "sequences_variants_constructs_protocols_or_numeric_ast_exported": False,
            "biological_record_writes": False,
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "full_investigation_complete": False,
        },
        "review limits changed",
    )
    return papers


def bind_current(root, index):
    expected = {r["path"]: r["record_sha256"] for r in index["records"]}
    actual = {
        str(p.relative_to(root)): reference.digest(p) for p in (root / "data/antibiotics").rglob("*.yaml")
    }
    require(len(expected) == 2939 and actual == expected, "current corpus changed")
    terms = set(TERMS.values())
    records = [r for r in index["records"] if terms.intersection(r["card_terms"])]
    claims = [c for c in index["claims"] if c["aro_id"] in terms]
    keys = {(c["record_identifier"], c["resistance_index"]): c for c in claims}
    require(len(records) == 8 and len(claims) == len(keys) == 9, "cohort coverage changed")
    for term in terms:
        require(
            index["terms"][term]["record_memberships"]
            == sorted({c["record_identifier"] for c in claims if c["aro_id"] == term}),
            "term membership changed",
        )
    seen = set()
    for row in records:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "compound identity changed",
        )
        for i, claim in enumerate(doc.get("resistance_mechanisms", [])):
            if claim.get("aro_id") not in terms:
                continue
            key = (doc["identifier"], i)
            require(
                key in keys
                and owner(claim) == "CARD"
                and memberships.checksum(claim) == keys[key]["claim_sha256"],
                "source claim changed",
            )
            require(
                hashlib.sha256(claim["label"].encode()).hexdigest()
                == index["terms"][claim["aro_id"]]["source_label_sha256"],
                "source label changed",
            )
            seen.add(key)
    require(seen == set(keys), "unread claim membership")
    return records, claims


def build(root):
    audit = json.loads((root / PLAN).read_bytes())
    for pin in audit["inputs"].values():
        reference.check_pin(root, pin)
    data = {k: read(root, p) for k, p in audit["inputs"].items() if p["path"].endswith(".json")}
    plan = data["plan"]
    for pin in plan["inputs"].values():
        reference.check_pin(root, pin)
    public = {k: read(root, p) for k, p in plan["inputs"].items() if p["path"].endswith(".json")}
    papers = validate_assessment(public["assessment"])
    require(
        set(plan["requests"]) == {"msh"}
        and plan["canary"] == "msh"
        and plan["requests"]["msh"]["query"] == QUERY,
        "request scope changed",
    )
    require(
        plan["constraints"]
        == {
            **public["assessment"]["constraints"],
            "retries": 0,
            "redirects_followed": 0,
            "source_adoption": False,
        },
        "plan limits changed",
    )
    require(
        data["canary"]["plan_sha256"] == audit["inputs"]["plan"]["sha256"]
        and data["canary"]["receipt"] == audit["inputs"]["msh_receipt"]
        and data["canary"]["remaining_native_requests"] == 0,
        "canary review changed",
    )
    receipt, attempt = data["msh_receipt"], data["msh_attempt"]
    require(
        receipt["plan_sha256"] == audit["inputs"]["plan"]["sha256"]
        and receipt["body"] == audit["inputs"]["msh_response"],
        "request pins changed",
    )
    body = reference.check_pin(root, receipt["body"]).read_bytes()
    msh, suggestions = native.validate_response(plan, "msh", receipt, attempt, body)
    require(not suggestions, "unreviewed suggestions")
    entries, hmg_query = literature.read_query(root, root / literature.DIRECTORY, "30940706")
    require(
        hmg_query["complete_for_query"]
        and hmg_query["release"] == "2026_03"
        and hmg_query["result_count"] == 2
        and len(hmg_query["pages"]) == 1
        and hmg_query["pages"][0]["cache"] == plan["inputs"]["hmg_body"]
        and hmg_query["pages"][0]["receipt"] == plan["inputs"]["hmg_receipt"],
        "cached citation response changed",
    )
    hmg, excluded = hmg_candidates(entries)
    require(set(plan["reused_taxonomy"]) == {"330879", "746128", "284593", "5478"}, "taxonomy scope changed")
    nodes, provenance = {}, {}
    for key, item in plan["reused_taxonomy"].items():
        nodes[key], provenance[key] = cached.cached_node(root, item)
    index = public["current_index"]
    records, claims = bind_current(root, index)
    terms = {}
    for key, term in TERMS.items():
        paper = papers[key]
        require(
            not index["terms"][term]["reference_links"]
            and public["definitions"]["terms"][term]["definition_citation_ids"] == ["PMID:" + paper["pmid"]]
            and public["prior_name_screen"]["terms"][term]["citation_pool_size"]
            == (0 if key == "msh" else 2),
            "own citation or previous context changed",
        )
        ref = select_reference(
            key,
            msh if key == "msh" else hmg,
            nodes[str(paper["reference_taxon_id"])],
            nodes[str(paper["reference_species_taxon_id"])],
            paper,
        )
        terms[term] = {
            "primary_assessment": paper,
            "references": [ref],
            "reference_accessions": [ref["accession"]],
            "record_memberships": index["terms"][term]["record_memberships"],
            "status": "SOURCE_SPECIFIC_REFERENCE_NOT_EXPERIMENTAL_ALLELE_OR_FAMILY_WIDE_IDENTITY",
            "experimental_protein_assignment": None,
            "experimental_allele_assignment": None,
            "experimental_strain_taxon_assignment": None,
            "experimental_genome_assignment": None,
            "whole_record_primary_review": "OPEN",
        }
    previous_accessions = {a for row in index["terms"].values() for a in row["reference_accessions"]}
    selected = {a for row in terms.values() for a in row["reference_accessions"]}
    return {
        "date": "2026-10-15",
        "scope": public["assessment"]["scope"],
        "inputs": audit["inputs"],
        "records": records,
        "claims": claims,
        "terms": terms,
        "excluded_same_citation_candidate": excluded,
        "cached_hmg_query": hmg_query,
        "msh_query": {
            "query": QUERY,
            "receipt": audit["inputs"]["msh_receipt"],
            "complete_result_count": len(msh),
            "release": receipt["headers"]["x-uniprot-release"],
        },
        "native_taxonomy": nodes,
        "taxonomy_provenance": provenance,
        "new_unique_reference_accessions": sorted(selected - previous_accessions),
        "previously_selected_reference_accessions": sorted(selected & previous_accessions),
        "summary": {
            "current_corpus_hashes_verified": 2939,
            "complete_records_loaded": len(records),
            "source_claims_bound": len(claims),
            "terms_investigated": 2,
            "selected_references": len(selected),
            "new_unique_reference_proteins": len(selected - previous_accessions),
            "previously_selected_reference_proteins": len(selected & previous_accessions),
            "new_term_reference_links": 2,
            "excluded_same_citation_candidates": 1,
            "reused_native_taxonomy_nodes": 4,
            "new_native_requests": 1,
            "whole_record_primary_signoffs": 0,
        },
        "constraints": {
            **plan["constraints"],
            "broad_index_rewritten": False,
            "experimental_identifiers_assigned": False,
        },
        "attribution": "UniProt and CARD/ARO metadata retained with native provenance. "
        "Primary literature interpreted only at the explicitly reviewed source and subject scope.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    result = build(root)
    if args.write:
        with (root / OUTPUT).open("x") as stream:
            json.dump(result, stream, indent=2, sort_keys=True)
            stream.write("\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
