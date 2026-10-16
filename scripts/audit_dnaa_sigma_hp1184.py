"""Replay gene/locus references while preserving comparator and experimental scope."""

import argparse
import json
from pathlib import Path

import audit_card_reference_lineages as lineages
import audit_card_reference_memberships as memberships
import audit_topoisomerase_references as reference
from audit_bla_primary_identifiers import read_json, require, validate_response
from audit_card_gene_reference_followup import cached_node, native_matches
from audit_curator_resistance_fields import owner
from audit_sal_reference_context import metadata_only

from antibioticmech.activity_collections import load_record

PREFIX = "research/2026-10-15-dnaa-sigma-hp1184"
PLAN = Path(PREFIX + "-audit-plan.json")
OUTPUT = Path(PREFIX + ".json")
TERMS = {"dnaA": "ARO:3000248", "sigma": "ARO:3000261", "hp1184": "ARO:3003965"}
QUERIES = {
    "dnaA": "gene_exact:dnaA AND organism_id:83333 AND reviewed:true",
    "sigma": "(gene_exact:rpoD OR gene_exact:rpoH) AND organism_id:83333 AND reviewed:true",
    "hp1184": "(gene_exact:HP_1184 OR gene_exact:HP1184) AND organism_id:85962",
}
IDENTITIES = {
    "dnaA": {"dnaA": "P03004"},
    "sigma": {"rpoH": "P0AGB3", "rpoD": "P00579"},
    "hp1184": {"HP_1184": "O25796"},
}


def protein_names(entry):
    description = entry["proteinDescription"]
    names = []
    if "recommendedName" in description:
        names.append(description["recommendedName"]["fullName"]["value"])
    for name in description.get("alternativeNames", []):
        names.append(name["fullName"]["value"])
    return names


def select_references(key, entries, taxon, species, paper):
    metadata_only(entries)
    require(
        len(entries) == len(IDENTITIES[key])
        and {e["primaryAccession"] for e in entries} == set(IDENTITIES[key].values()),
        "missing, duplicate or unreviewed protein candidate",
    )
    _, ancestor = lineages.lineage(taxon)
    lineages.lineage(species)
    require(
        taxon["taxonId"] == paper["reference_taxon_id"]
        and taxon["rank"] == "strain"
        and species["taxonId"] == paper["reference_species_taxon_id"]
        and species["rank"] == "species"
        and species["scientificName"] == paper["source_species"]
        and ancestor == lineages.identity(species),
        "reference taxonomy or species ancestry changed",
    )
    result = []
    for symbol, accession in IDENTITIES[key].items():
        entry = next(e for e in entries if e["primaryAccession"] == accession)
        matches = native_matches(entry, symbol)
        require(matches, "exact gene/locus identity missing")
        require(
            {s for s in IDENTITIES[key] if native_matches(entry, s)} == {symbol},
            "ambiguous gene/locus identity",
        )
        require(
            entry["organism"]["taxonId"] == taxon["taxonId"]
            and entry["organism"]["scientificName"] == taxon["scientificName"],
            "protein organism differs from native taxonomy",
        )
        reviewed = entry["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
        require(
            entry["entryType"] in {"UniProtKB reviewed (Swiss-Prot)", "UniProtKB unreviewed (TrEMBL)"}
            and (reviewed or key == "hp1184"),
            "unexpected review status",
        )
        names = protein_names(entry)
        if symbol == "rpoH":
            require(any("sigma-32" in n.lower() for n in names), "sigma32 identity missing")
        elif symbol == "rpoD":
            require(any("sigma-70" in n.lower() for n in names), "sigma70 identity missing")
        versions = entry["entryAudit"]
        require(
            all(type(versions[k]) is int and versions[k] > 0 for k in ("entryVersion", "sequenceVersion")),
            "invalid native entry versions",
        )
        pmids = {
            cross["id"]
            for ref in entry.get("references", [])
            for cross in ref.get("citation", {}).get("citationCrossReferences", [])
            if cross["database"] == "PubMed"
        }
        comparator = symbol == "rpoD"
        result.append(
            {
                "accession": "UniProtKB:" + accession,
                "gene_or_locus": symbol,
                "native_gene_matches": matches,
                "protein_names": names,
                "reviewed": reviewed,
                "entry_version": versions["entryVersion"],
                "sequence_version": versions["sequenceVersion"],
                "reference_taxon_id": "NCBITaxon:" + str(taxon["taxonId"]),
                "reference_taxon_rank": taxon["rank"],
                "reference_species_taxon_id": "NCBITaxon:" + str(species["taxonId"]),
                "reference_species_name": species["scientificName"],
                "own_primary_pmids_in_uniprot": sorted(pmids & {p["pmid"] for p in paper["papers"]}),
                "role": "SIGMA70_COMPARATOR_NOT_RESISTANCE_DETERMINANT"
                if comparator
                else "NAMED_GENE_OR_LOCUS_REFERENCE_NOT_EXPERIMENTAL_ALLELE",
                "eligible_as_determinant_reference_context": not comparator,
                "experimental_protein_assignment": None,
                "experimental_allele_assignment": None,
                "experimental_strain_taxon_assignment": None,
                "resistance_phenotype_from_protein_annotation": False,
            }
        )
    return sorted(result, key=lambda r: r["accession"])


def bind_current(root, index):
    actual = {
        str(p.relative_to(root)): reference.digest(p) for p in (root / "data/antibiotics").rglob("*.yaml")
    }
    expected = {r["path"]: r["record_sha256"] for r in index["records"]}
    require(actual == expected and len(actual) == 2939, "current corpus changed")
    terms = set(TERMS.values())
    rows = [r for r in index["records"] if terms.intersection(r["card_terms"])]
    claims = [c for c in index["claims"] if c["aro_id"] in terms]
    by_key = {(c["record_identifier"], c["resistance_index"]): c for c in claims}
    require(len(rows) == 8 and len(claims) == len(by_key) == 12, "cohort coverage changed")
    seen = set()
    for row in rows:
        record = load_record(root / row["path"])
        require(
            record["identifier"] == row["identifier"]
            and record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "compound identity changed",
        )
        for i, claim in enumerate(record.get("resistance_mechanisms", [])):
            if claim.get("aro_id") not in terms:
                continue
            key = (record["identifier"], i)
            require(key in by_key and owner(claim) == "CARD", "source ownership changed")
            require(memberships.checksum(claim) == by_key[key]["claim_sha256"], "source claim changed")
            seen.add(key)
    require(seen == set(by_key), "source membership unread")
    return rows, claims


def build(root):
    audit = json.loads((root / PLAN).read_bytes())
    inputs = audit["inputs"]
    values = {k: read_json(root, v) for k, v in inputs.items() if v["path"].endswith(".json")}
    for binding in inputs.values():
        reference.check_pin(root, binding)
    plan = values["request_plan"]
    public_pins = plan["inputs"]
    public = {k: read_json(root, v) for k, v in public_pins.items() if v["path"].endswith(".json")}
    for binding in public_pins.values():
        reference.check_pin(root, binding)
    require(
        set(plan["requests"]) == set(TERMS)
        and plan["constraints"]["ncbi_requests"] == 0
        and plan["constraints"]["issue_1040"] == "DEFERRED",
        "planned scope changed",
    )
    canary = values["canary"]
    require(
        canary["plan_sha256"] == inputs["request_plan"]["sha256"]
        and canary["receipt"] == inputs["dnaA_receipt"]
        and canary["approved_remaining_queries"] is True,
        "unreviewed canary",
    )
    taxonomy, taxonomy_sources = {}, {}
    for taxid, source in plan["taxonomy_sources"].items():
        node, provenance = cached_node(root, {"taxon_id": taxid, "source": source})
        taxonomy[taxid], taxonomy_sources[taxid] = node, provenance
    require(set(taxonomy) == {"210", "562", "83333", "85962"}, "taxonomy coverage changed")
    records, claims = bind_current(root, public["current_index"])
    terms, requests = {}, {}
    for key, term in TERMS.items():
        paper = public["assessment"]["terms"][key]
        require(
            paper["aro_id"] == term and paper["query"] == plan["requests"][key]["query"] == QUERIES[key],
            "term/query mismatch",
        )
        expected_citations = sorted("PMID:" + p["pmid"] for p in paper["papers"])
        require(
            public["definitions"]["terms"][term]["definition_citation_ids"] == expected_citations,
            "definition citation changed",
        )
        require(
            public["prior_citation_screen"]["terms"][term]["citation_pool_size"] == 0,
            "prior citation result changed",
        )
        require(
            not public["current_index"]["terms"][term]["reference_links"],
            "term already has selected reference",
        )
        receipt, attempt = values[key + "_receipt"], values[key + "_attempt"]
        require(
            receipt["plan_sha256"] == inputs["request_plan"]["sha256"]
            and receipt["body"] == inputs[key + "_body"],
            "response pin mismatch",
        )
        body = reference.check_pin(root, receipt["body"]).read_bytes()
        entries, suggestions = validate_response(plan, key, receipt, attempt, body)
        refs = select_references(
            key,
            entries,
            taxonomy[str(paper["reference_taxon_id"])],
            taxonomy[str(paper["reference_species_taxon_id"])],
            paper,
        )
        terms[term] = {
            "primary_assessment": paper,
            "references": refs,
            "reference_accessions": sorted(
                r["accession"] for r in refs if r["eligible_as_determinant_reference_context"]
            ),
            "comparator_accessions": sorted(
                r["accession"] for r in refs if not r["eligible_as_determinant_reference_context"]
            ),
            "record_memberships": public["current_index"]["terms"][term]["record_memberships"],
            "experimental_protein_assignment": None,
            "experimental_allele_assignment": None,
            "experimental_genome_assignment": None,
            "whole_record_primary_review": "OPEN",
        }
        requests[key] = {
            "query": plan["requests"][key]["query"],
            "url": receipt["url"],
            "receipt": inputs[key + "_receipt"],
            "body": receipt["body"],
            "release": receipt["headers"]["x-uniprot-release"],
            "retrieved_at": receipt["retrieved_at"],
            "complete_result_count": len(entries),
            "suggestions_not_selected": suggestions,
        }
    all_refs = [r for t in terms.values() for r in t["references"]]
    return {
        "date": "2026-10-15",
        "inputs": {**public_pins, **inputs},
        "summary": {
            "current_corpus_hashes_verified": 2939,
            "complete_records_loaded": len(records),
            "source_claims_bound": len(claims),
            "terms_investigated": len(terms),
            "reference_proteins": len(all_refs),
            "determinant_reference_contexts": sum(
                r["eligible_as_determinant_reference_context"] for r in all_refs
            ),
            "comparators_not_resistance_determinants": sum(
                not r["eligible_as_determinant_reference_context"] for r in all_refs
            ),
            "species_nodes": 2,
            "reference_strain_nodes": 2,
            "whole_record_primary_signoffs": 0,
        },
        "records": records,
        "claims": claims,
        "terms": terms,
        "requests": requests,
        "native_taxonomy": taxonomy,
        "taxonomy_provenance": taxonomy_sources,
        "primary_review": public["assessment"]["primary_review"],
        "constraints": {**plan["constraints"], "full_investigation_complete": False},
        "attribution": (
            "CARD/ARO: McMaster University, CC BY 4.0. UniProt metadata: UniProt Consortium. "
            "Primary scope: the four papers cited in the assessment; "
            "only selected publisher text was reviewed."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    if args.write:
        with (args.root / OUTPUT).open("x") as stream:
            json.dump(result, stream, indent=2, sort_keys=True)
            stream.write("\n")
    else:
        require(result == json.loads((args.root / OUTPUT).read_bytes()), "saved projection differs")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
