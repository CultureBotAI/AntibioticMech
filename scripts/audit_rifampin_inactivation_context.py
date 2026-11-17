"""Replay rifampin-inactivation reference identities without assigning resistant alleles."""

import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_bla_primary_identifiers as native
import audit_card_gene_reference_followup as cached
import audit_card_reference_lineages as taxonomy
import audit_card_reference_memberships as memberships
import audit_sal_reference_context as sal
from audit_curator_resistance_fields import owner

from antibioticmech.activity_collections import load_record

reference = native.reference
require = native.require
PREFIX = "research/2026-10-15-rifampin-inactivation-context"
PLAN = Path(PREFIX + "-audit-plan.json")
OUTPUT = Path(PREFIX + ".json")
TERMS = {"rgt1438": "ARO:3002883", "arr": "ARO:3000390", "rphB": "ARO:3003992"}
QUERIES = {
    "rgt1438": "xref:embl-JX028276",
    "rphB": "gene_exact:rphB AND organism_id:1120679",
    "rgt-taxonomy": "WAC1438",
}


def read(root, pin):
    return json.loads(reference.check_pin(root, pin).read_bytes())


def pdb_response(plan, receipt, attempt, body):
    item = plan["requests"]["pdb-arr"]
    parsed = urlsplit(item["url"])
    require(
        parsed.scheme == "https"
        and parsed.netloc == "data.rcsb.org"
        and parsed.path == "/graphql"
        and not parsed.fragment
        and parse_qs(parsed.query) == {"query": [item["query"]]}
        and 'entries(entry_ids:["2HW2"])' in item["query"],
        "PDB request scope changed",
    )
    require(
        all(
            r["url"] == item["url"] and r["key"] == "pdb-arr" and r["retries"] == r["redirects_followed"] == 0
            for r in (receipt, attempt)
        )
        and all(receipt[k] == v for k, v in attempt.items()),
        "PDB request history changed",
    )
    require(
        receipt["status"] == 200
        and "application/json" in receipt["headers"].get("content-type", "")
        and not receipt["headers"].get("location")
        and not receipt["headers"].get("link")
        and len(body) == receipt["bytes"] <= plan["max_bytes"]
        and hashlib.sha256(body).hexdigest() == receipt["body"]["sha256"],
        "PDB response changed",
    )
    payload = json.loads(body)
    sal.metadata_only(payload)
    require(not payload.get("errors"), "PDB GraphQL error")
    entries = payload["data"]["entries"]
    require(len(entries) == 1 and entries[0]["rcsb_id"] == "2HW2", "wrong structure entry")
    return entries[0]


def citation_entry(receipt, body):
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    parsed = urlsplit(receipt["url"])
    require(
        parsed.scheme == "https"
        and parsed.netloc == "rest.uniprot.org"
        and parsed.path == "/uniprotkb/search"
        and not parsed.fragment
        and parse_qs(parsed.query)
        == {
            "query": ["lit_pubmed:18349144"],
            "format": ["json"],
            "size": ["500"],
            "sort": ["accession asc"],
            "fields": [
                "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
                "xref_card,lit_pubmed_id,sequence_version,version"
            ],
        },
        "cached citation query changed",
    )
    require(
        receipt["status"] == 200
        and receipt["query"] == "lit_pubmed:18349144"
        and receipt["sha256"] == hashlib.sha256(body).hexdigest()
        and receipt["bytes"] == len(body)
        and headers["x-uniprot-release"] == "2026_03"
        and not headers.get("link")
        and not headers.get("location"),
        "cached citation response changed",
    )
    entries = json.loads(body)["results"]
    sal.metadata_only(entries)
    require(len(entries) == int(headers["x-total-results"]) == 1, "citation result coverage changed")
    return entries[0]


def arr_reference(entry, structure, taxon, species):
    sal.metadata_only(entry)
    _, ancestor = taxonomy.lineage(taxon)
    taxonomy.lineage(species)
    require(
        ancestor == taxonomy.identity(species)
        and species["taxonId"] == 1772
        and species["rank"] == "species"
        and taxon["taxonId"] == 246196
        and taxon["rank"] == "strain",
        "Arr reference taxonomy changed",
    )
    require(
        entry["primaryAccession"] == "A0QRS5"
        and entry["entryType"] == "UniProtKB unreviewed (TrEMBL)"
        and entry["organism"]["taxonId"] == taxon["taxonId"]
        and entry["organism"]["scientificName"] == taxon["scientificName"]
        and cached.native_matches(entry, "MSMEG_1221"),
        "Arr reference locus changed",
    )
    papers = [
        r
        for r in entry["references"]
        if {("PubMed", "18349144"), ("DOI", "10.1073/pnas.0711939105")}
        <= {(c["database"], c["id"]) for c in r["citation"].get("citationCrossReferences", [])}
    ]
    require(
        len(papers) == 1
        and any(e.get("source") == "PDB" and e.get("id") == "2HW2" for e in papers[0].get("evidences", [])),
        "Arr own structure citation missing",
    )
    citation = structure["rcsb_primary_citation"]
    require(
        structure["rcsb_id"] == "2HW2"
        and citation["pdbx_database_id_PubMed"] == 18349144
        and citation["pdbx_database_id_DOI"] == "10.1073/pnas.0711939105",
        "Arr structure citation changed",
    )
    entities = structure["polymer_entities"]
    require(len(entities) == 1 and entities[0]["rcsb_id"] == "2HW2_1", "ambiguous Arr structure component")
    entity = entities[0]
    require(
        entity["rcsb_polymer_entity"]["pdbx_description"] == "Rifampin ADP-ribosyl transferase"
        and entity["rcsb_polymer_entity_container_identifiers"]["reference_sequence_identifiers"]
        == [{"database_name": "UniProt", "database_accession": "A0QRS5"}],
        "Arr structure crosswalk changed",
    )
    sources = entity["entity_src_gen"]
    require(
        len(sources) == 1
        and sources[0]["pdbx_gene_src_gene"] == "arr"
        and sources[0]["pdbx_gene_src_ncbi_taxonomy_id"] == "1772"
        and sources[0]["gene_src_strain"] is None
        and sources[0]["pdbx_host_org_ncbi_taxonomy_id"] == "469008"
        and entity["rcsb_entity_source_organism"]
        == [{"ncbi_taxonomy_id": 1772, "scientific_name": "Mycobacterium smegmatis"}],
        "Arr structure source or expression host changed",
    )
    name_context = sal.species_context([species], sources[0]["pdbx_gene_src_scientific_name"])
    identity = memberships.reference_identity(
        {
            "entry_type": entry["entryType"],
            "entry_version": entry["entryAudit"]["entryVersion"],
            "sequence_version": entry["entryAudit"]["sequenceVersion"],
            "reference_taxon_id": "NCBITaxon:246196",
            "reference_taxon_rank": taxon["rank"],
            "reference_species_taxon_id": "NCBITaxon:1772",
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
    )
    return {
        "accession": "UniProtKB:A0QRS5",
        "identity": identity,
        "native_locus_matches": cached.native_matches(entry, "MSMEG_1221"),
        "own_primary_citation": {
            "pmid": "18349144",
            "doi": "10.1073/pnas.0711939105",
            "native_reference_number": papers[0]["referenceNumber"],
        },
        "structure_entry": structure["rcsb_id"],
        "structure_revision": structure["rcsb_accession_info"],
        "structure_entity": entity["rcsb_id"],
        "source_species_name_context": name_context,
        "structure_source_strain_reported": None,
        "structure_expression_host_source_reported": {
            "taxon_id": "NCBITaxon:469008",
            "label": sources[0]["pdbx_host_org_scientific_name"],
            "independent_taxonomy_verification_performed": False,
            "experimental_subject_assigned": False,
        },
        "scope": "STRUCTURE_LINKED_ARR_MS_FAMILY_MEMBER_REFERENCE_NOT_EXPERIMENTAL_ALLELE",
        "single_protein_identity_for_whole_arr_family": False,
        "experimental_protein_assignment": None,
        "experimental_allele_assignment": None,
        "experimental_strain_taxon_assignment": None,
        "experimental_genome_assignment": None,
    }


def rph_primary_scope(wrapper):
    body = wrapper["body"].encode()
    require(
        wrapper["status"] == 200
        and wrapper["url"] == "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5155152/fullTextXML"
        and hashlib.sha256(body).hexdigest() == wrapper["sha256"],
        "cached Rph primary changed",
    )
    root = ET.fromstring(body)
    ids = {e.get("pub-id-type"): e.text for e in root.findall(".//front/article-meta/article-id")}
    require(ids.get("pmid") == "27929110" and ids.get("doi") == "10.1038/ncomms13803", "wrong Rph primary")
    table = root.find(".//table-wrap[@id='t1']")
    caption = "".join(table.find("caption").itertext())
    require("heterologously expressed in E. coli" in caption, "Rph host scope changed")
    rows = [
        r
        for r in table.findall(".//tbody/tr")
        if any("".join(c.itertext()) == "rphB" for c in r.findall("td"))
    ]
    require(len(rows) == 1, "Rph table row missing or ambiguous")
    cells = rows[0].findall("td")
    require(
        ["".join(c.itertext()) for c in cells[:2]] == ["Rifampin phosphotransferase", "rphB"],
        "Rph determinant label changed",
    )
    availability = root.find(".//sec[@id='sec27']")
    text = "".join(availability.itertext())
    require(
        all(x in text for x in ("JFOM00000000", "KX531043 to KX531056", "Paenibacillus sp. LC231")),
        "Rph source deposits changed",
    )
    return {
        "pmid": ids["pmid"],
        "doi": ids["doi"],
        "selected_element_sha256": {
            k: hashlib.sha256(ET.tostring(e)).hexdigest()
            for k, e in {"t1": table, "sec27": availability}.items()
        },
        "table_determinant": {
            "label": "Rifampin phosphotransferase",
            "gene": "rphB",
            "measurement_subject": "HETEROLOGOUS_E_COLI_NOT_NATIVE_LC231",
        },
        "source_wgs_accession": "JFOM00000000",
        "source_determinant_accession_range": ["KX531043", "KX531056"],
        "individual_gene_accession_assigned_from_range": False,
        "quantitative_values_exported": False,
        "whole_paper_reviewed": False,
    }


def bind_current(root, index):
    expected = {r["path"]: r["record_sha256"] for r in index["records"]}
    actual = {
        str(p.relative_to(root)): reference.digest(p) for p in (root / "data/antibiotics").rglob("*.yaml")
    }
    require(len(expected) == 2939 and actual == expected, "current corpus changed")
    cohort = set(TERMS.values())
    rows = [r for r in index["records"] if cohort.intersection(r["card_terms"])]
    claims = [c for c in index["claims"] if c["aro_id"] in cohort]
    by_key = {(c["record_identifier"], c["resistance_index"]): c for c in claims}
    require(len(by_key) == len(claims), "duplicate claim membership")
    seen = set()
    for row in rows:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "compound identity changed",
        )
        for i, claim in enumerate(doc.get("resistance_mechanisms", [])):
            if claim.get("aro_id") not in cohort:
                continue
            key = (doc["identifier"], i)
            require(
                key in by_key
                and owner(claim) == "CARD"
                and memberships.checksum(claim) == by_key[key]["claim_sha256"],
                "source claim changed",
            )
            require(
                hashlib.sha256(claim["label"].encode()).hexdigest()
                == index["terms"][claim["aro_id"]]["source_label_sha256"],
                "source label changed",
            )
            seen.add(key)
    require(seen == set(by_key) and len(rows) == 4 and len(claims) == 12, "cohort coverage changed")
    return rows, claims


def build(root):
    audit = json.loads((root / PLAN).read_bytes())
    data = {k: read(root, p) for k, p in audit["inputs"].items() if p["path"].endswith(".json")}
    for p in audit["inputs"].values():
        reference.check_pin(root, p)
    plan, tax_plan = data["plan"], data["taxonomy_plan"]
    for pin in plan["inputs"].values():
        reference.check_pin(root, pin)
    public = {k: read(root, p) for k, p in plan["inputs"].items() if p["path"].endswith(".json")}
    require(
        set(plan["requests"]) == {"rgt1438", "rphB", "pdb-arr"}
        and set(tax_plan["requests"]) == {"rgt-taxonomy"},
        "request coverage changed",
    )
    require(
        data["canary"]["approved_remaining_queries"] is True
        and data["canary"]["plan_sha256"] == audit["inputs"]["plan"]["sha256"]
        and data["canary"]["receipt"] == audit["inputs"]["rgt1438_receipt"],
        "unreviewed canary",
    )
    require(
        all(
            p["constraints"]["ncbi_requests"] == 0 and p["constraints"]["issue_1040"] == "DEFERRED"
            for p in (plan, tax_plan)
        ),
        "NCBI deferral changed",
    )
    responses, queries = {}, {}
    for key in ("rgt1438", "rphB", "pdb-arr", "rgt-taxonomy"):
        selected_plan = tax_plan if key == "rgt-taxonomy" else plan
        pin = audit["inputs"]["taxonomy_plan" if key == "rgt-taxonomy" else "plan"]
        receipt, attempt = data[key + "_receipt"], data[key + "_attempt"]
        body = reference.check_pin(root, audit["inputs"][key + "_response"]).read_bytes()
        require(
            attempt["plan_sha256"] == pin["sha256"] and receipt["body"] == audit["inputs"][key + "_response"],
            "request plan or body pin changed",
        )
        if key == "pdb-arr":
            responses[key] = pdb_response(plan, receipt, attempt, body)
            suggestions = []
        else:
            require(selected_plan["requests"][key]["query"] == QUERIES[key], "query identity changed")
            responses[key], suggestions = native.validate_response(
                selected_plan, key, receipt, attempt, body, taxonomy=key == "rgt-taxonomy"
            )
            sal.metadata_only(responses[key])
        queries[key] = {
            "query": selected_plan["requests"][key]["query"],
            "receipt": audit["inputs"][key + "_receipt"],
            "result_count": 1 if key == "pdb-arr" else len(responses[key]),
            "suggestions_not_selected": suggestions,
        }
    require(not responses["rgt1438"] and not responses["rphB"], "new protein results require review")
    require(
        len(responses["rgt-taxonomy"]) == 1 and responses["rgt-taxonomy"][0]["taxonId"] == 2203204,
        "WAC1438 taxonomy needs reassessment",
    )
    taxonomy.lineage(responses["rgt-taxonomy"][0])
    taxa, tax_provenance = {}, {}
    for key, item in plan["reused_taxonomy"].items():
        taxa[key], tax_provenance[key] = cached.cached_node(root, item)
    entry = citation_entry(
        public["arr_citation_receipt"],
        reference.check_pin(root, plan["inputs"]["arr_citation_body"]).read_bytes(),
    )
    arr = arr_reference(entry, responses["pdb-arr"], taxa["246196"], taxa["1772"])
    rph = rph_primary_scope(public["rph_primary"])
    index, papers = public["current_index"], public["assessment"]["terms"]
    require(set(papers) == set(TERMS), "assessment cohort changed")
    rows, claims = bind_current(root, index)
    contexts = {
        "rgt1438": sal.species_context(responses["rgt-taxonomy"], papers["rgt1438"]["source_organism"]),
        "arr": arr["source_species_name_context"],
        "rphB": sal.species_context([taxa["1120679"]], papers["rphB"]["source_organism"]),
    }
    terms = {}
    for key, term in TERMS.items():
        paper = papers[key]
        require(
            paper["aro_id"] == term
            and not index["terms"][term]["reference_links"]
            and public["definitions"]["terms"][term]["definition_citation_ids"]
            == ["PMID:" + p for p in paper["pmids"]],
            "definition citation or prior reference scope changed",
        )
        require(
            public["prior_name_screen"]["terms"][term]["citation_pool_size"] == (1 if key == "arr" else 0),
            "prior citation pool changed",
        )
        terms[term] = {
            "primary_assessment": paper,
            "source_taxonomy_context": contexts[key],
            "record_memberships": index["terms"][term]["record_memberships"],
            "references": [arr] if key == "arr" else [],
            "reference_accessions": [arr["accession"]] if key == "arr" else [],
            "status": "FAMILY_MEMBER_REFERENCE_NOT_SINGLE_ARR_IDENTITY"
            if key == "arr"
            else "EXPLICIT_QUERY_EMPTY_NOT_BIOLOGICAL_ABSENCE",
            "experimental_protein_assignment": None,
            "experimental_allele_assignment": None,
            "experimental_strain_taxon_assignment": None,
            "experimental_genome_assignment": None,
            "whole_record_primary_review": "OPEN",
        }
    return {
        "date": "2026-10-15",
        "inputs": audit["inputs"],
        "scope": "RIFAMPIN_INACTIVATION_REFERENCE_CONTEXT_NOT_EXPERIMENTAL_ALLELE_GROUNDING",
        "records": rows,
        "claims": claims,
        "terms": terms,
        "queries": queries,
        "native_structure_metadata": responses["pdb-arr"],
        "native_taxonomy": taxa,
        "reused_taxonomy_provenance": tax_provenance,
        "rph_primary_scope": rph,
        "summary": {
            "current_corpus_hashes_verified": 2939,
            "complete_records_loaded": len(rows),
            "source_claims_bound": len(claims),
            "terms_investigated": len(terms),
            "selected_family_member_references": 1,
            "unresolved_protein_queries": 2,
            "source_species_name_contexts": 3,
            "new_native_taxonomy_nodes": 1,
            "reused_native_taxonomy_nodes": 3,
            "new_native_requests": len(queries),
            "whole_record_primary_signoffs": 0,
        },
        "constraints": {
            **plan["constraints"],
            "broad_index_rewritten": False,
            "experimental_identifiers_assigned": False,
        },
        "attribution": "CARD/ARO, UniProt and RCSB identity metadata retained with native provenance; "
        "primary references and source-specific limitations retained in the assessment.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    output = args.root / OUTPUT
    if args.check:
        require(output.read_bytes() == encoded, "dossier drift")
    else:
        with output.open("xb") as stream:
            stream.write(encoded)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
