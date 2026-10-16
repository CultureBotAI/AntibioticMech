"""Replay a deposited locus and archive-ID crosswalk without assigning an allele."""

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_explicit_identifiers as identifiers

prior, aliases, mex = identifiers.prior, identifiers.aliases, identifiers.mex
reference, require, read_json = prior.reference, prior.require, prior.read_json
PREFIX = "research/2026-10-15-vmlr2-structure"
PLAN, OUTPUT = Path(PREFIX + "-audit-plan.json"), Path(PREFIX + ".json")
SCOPE = "PDB_LOCUS_AND_ARCHIVE_REFERENCE_NOT_ENGINEERED_OR_RESISTANT_ALLELE"
FIELDS = prior.FIELDS + ",xref_pdb"
QUERY = "(accession:W1SM44 OR sec_acc:W1SM44 OR (gene_exact:BAVI_03309 AND taxonomy_id:220686))"
QUALIFIED = "PDB_LOCUS_ARCHIVE_AND_SPECIES_REFERENCE_NOT_EXPERIMENTAL_ALLELE"
FORBIDDEN = {
    "sequence",
    "features",
    "comments",
    "pdbx_seq_one_letter_code",
    "pdbx_seq_one_letter_code_can",
    "pdbx_mutation",
    "pdbx_gene_src_variant",
    "pdbx_host_org_vector",
    "pdbx_host_org_variant",
}


def reject_operational_fields(value):
    if isinstance(value, dict):
        require(not FORBIDDEN & set(value), "unexpected sequence, variant or construction payload")
        for item in value.values():
            reject_operational_fields(item)
    elif isinstance(value, list):
        for item in value:
            reject_operational_fields(item)


def select_entity(payload, source_taxon, expected_pmid, expected_doi):
    reject_operational_fields(payload)
    require(
        not payload.get("errors") and len(payload["data"]["entries"]) == 1,
        "GraphQL error or entry count changed",
    )
    entry = payload["data"]["entries"][0]
    require(
        entry["rcsb_id"] == "8BUU" and entry["struct"]["title"] == "ARE-ABCF VmlR2 bound to a 70S ribosome",
        "structure title or identity changed",
    )
    citation = entry["rcsb_primary_citation"]
    require(
        str(citation["pdbx_database_id_PubMed"]) == expected_pmid
        and citation["pdbx_database_id_DOI"].casefold() == expected_doi.casefold(),
        "structure citation differs from source",
    )
    entities = entry["polymer_entities"]
    ids = [e["rcsb_id"] for e in entities]
    require(
        len(ids) == len(set(ids)) and all(re.fullmatch(r"8BUU_[1-9][0-9]*", i) for i in ids),
        "duplicate or foreign entity",
    )
    selected = [
        e
        for e in entities
        if any(str(o["ncbi_taxonomy_id"]) == source_taxon for o in (e["rcsb_entity_source_organism"] or []))
    ]
    require(len(selected) == 1, "missing or ambiguous source-organism entity")
    entity = selected[0]
    organisms = entity["rcsb_entity_source_organism"]
    require(
        len(organisms) == 1 and organisms[0]["scientific_name"] == "Neobacillus vireti",
        "mixed or renamed entity source",
    )
    source = entity["entity_src_gen"]
    require(
        len(source) == 1
        and source[0]["pdbx_gene_src_ncbi_taxonomy_id"] == source_taxon
        and source[0]["pdbx_gene_src_scientific_name"] == organisms[0]["scientific_name"],
        "entity source fields disagree",
    )
    count = entity["entity_poly"]["rcsb_mutation_count"]
    require(type(count) is int and count >= 0, "missing or invalid engineered-mutation flag")
    return entry, entity


def reference_link(current, historical, source_gene, source_species, reference_species):
    require(
        current["entryType"] in identifiers.ACTIVE and historical["entryType"] == "Inactive",
        "reference states changed",
    )
    matches = identifiers.locus_alias_matches(current, [source_gene])
    fields = [
        m
        for row in matches
        for m in row["native_fields"]
        if "/orderedLocusNames/" in m["field"] or "/orfNames/" in m["field"]
    ]
    left = current.get("extraAttributes", {}).get("uniParcId")
    right = historical.get("extraAttributes", {}).get("uniParcId")
    archive_match = bool(left and re.fullmatch(r"UPI[0-9A-F]{10}", left) and left == right)
    species_match = source_species is not None and source_species == reference_species
    qualified = bool(fields) and archive_match and species_match
    return {
        "protein_accession": "UniProtKB:" + current["primaryAccession"],
        "historical_pdb_reference_accession": "UniProtKB:" + historical["primaryAccession"],
        "native_locus_or_orf_matches": fields,
        "current_native_uniparc_id": left,
        "historical_native_uniparc_id": right,
        "same_native_uniparc_id": archive_match,
        "same_reference_species": species_match,
        "disposition": QUALIFIED if qualified else "REFERENCE_CROSSWALK_INCOMPLETE_WITHHELD",
        "qualified_reference": qualified,
        "official_accession_replacement_asserted": False,
        "engineered_entity_equated_to_reference": False,
        "experimental_donor_strain_assignment": False,
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
        "experimental_genome_assignment": None,
        "primary_resistance_validation": False,
    }


def request_receipt(root, directory, key, item, frozen_pin, bound):
    receipt = read_json(root, item)
    attempt_path = directory / (key + "-attempt.json")
    attempt = json.loads(attempt_path.read_bytes())
    require(
        all(receipt[k] == v for k, v in attempt.items())
        and attempt["plan_sha256"] == frozen_pin["sha256"]
        and receipt["status"] == 200
        and receipt["retries"] == receipt["redirects_followed"] == 0
        and not receipt["headers"].get("location")
        and not receipt["headers"].get("link")
        and type(receipt["bytes"]) is int
        and 0 < receipt["bytes"] <= bound,
        "native request history, status or bound changed",
    )
    return receipt, reference.pin(root, attempt_path)


def check_request_history(directory):
    keys = {"pdb-metadata", "uniprot-identifiers", "taxonomy-1131730"}
    for suffix in ("attempt", "receipt"):
        require(
            set(directory.glob(f"*-{suffix}.json")) == {directory / f"{k}-{suffix}.json" for k in keys},
            "unaccounted request artifact",
        )
    require(
        not list(directory.glob("*-error.json"))
        and set(directory.glob("*-body.json"))
        == {directory / "pdb-metadata-body.json", directory / "uniprot-identifiers-body.json"},
        "unaccounted body or failure",
    )


def structure_source(root, plan, frozen, documents):
    directory = root / frozen["cache_directory"]
    receipt, attempt = request_receipt(
        root,
        directory,
        "pdb-metadata",
        plan["receipts"]["pdb-metadata"],
        plan["inputs"]["structure_plan"],
        frozen["max_bytes"],
    )
    item = frozen["requests"]["pdb-metadata"]
    url = urlsplit(receipt["url"])
    require(
        url.scheme == "https"
        and url.netloc == "data.rcsb.org"
        and url.path == "/graphql"
        and not url.fragment
        and receipt["url"] == item["url"]
        and parse_qs(url.query) == {"query": [item["query"]]},
        "structure request identity changed",
    )
    body = reference.check_pin(root, receipt["body"]).read_bytes()
    require(len(body) == receipt["bytes"], "structure body size changed")
    entry, entity = select_entity(
        json.loads(body), plan["reference_species"], "36951104", "10.1093/nar/gkad193"
    )
    require(
        entity["rcsb_id"] == plan["focal_entity"] == "8BUU_51"
        and entity["rcsb_polymer_entity"]["pdbx_description"] == "ExpZ"
        and entity["entity_src_gen"][0]["pdbx_gene_src_gene"] == plan["native_source_locus"] == "BAVI_03309"
        and entity["entity_src_gen"][0]["gene_src_strain"] is None
        and entity["entity_src_gen"][0]["pdbx_host_org_ncbi_taxonomy_id"]
        == plan["deposited_expression_host"]
        == "224308"
        and entity["entity_poly"]["rcsb_mutation_count"] > 0,
        "inspected entity context changed",
    )
    refs = entity["rcsb_polymer_entity_container_identifiers"]["reference_sequence_identifiers"]
    require(
        refs == [{"database_name": "UniProt", "database_accession": plan["historical_reference_accession"]}],
        "PDB reference crosswalk changed",
    )
    canary = documents["canary"]
    require(
        canary["plan_sha256"] == plan["inputs"]["structure_plan"]["sha256"]
        and canary["receipt"] == plan["receipts"]["pdb-metadata"]
        and canary["approved_for_locus_reference_query"] is True
        and canary["entity_equated_to_reference_or_resistant_allele"] is False
        and canary["focal_entity"] == entity["rcsb_id"]
        and canary["native_uniprot_accession"] == refs[0]["database_accession"],
        "canary inspection binding changed",
    )
    preflight = documents["preflight"]
    require(
        preflight["ignored_files_included"] is True
        and preflight["prior_matching_native_requests"] == []
        and preflight["plan_sha256"] == plan["inputs"]["structure_plan"]["sha256"],
        "request-history review changed",
    )
    return {"receipt": plan["receipts"]["pdb-metadata"], "attempt": attempt, **receipt}, {
        "entry_id": entry["rcsb_id"],
        "title": entry["struct"]["title"],
        "revision": entry["rcsb_accession_info"],
        "primary_citation": entry["rcsb_primary_citation"],
        "entity_count_inspected": len(entry["polymer_entities"]),
        "focal_entity": entity,
        "focal_entity_selection_is_documented_inference": True,
        "focal_entity_inference": plan["focal_entity_inference"],
        "engineered_entity": True,
        "native_donor_strain_supplied": False,
        "engineered_entity_is_reference_protein_or_resistant_allele": False,
    }


def publication_metadata(wrapper):
    require(
        wrapper["status"] == 200
        and hashlib.sha256(wrapper["body"].encode()).hexdigest() == wrapper["sha256"],
        "cached publication metadata changed",
    )
    url = urlsplit(wrapper["url"])
    require(
        url.scheme == "https" and url.netloc in {"www.ebi.ac.uk", "www.ebi.ac.uk:443"},
        "publication cache provider changed",
    )
    rows = [
        r
        for r in json.loads(wrapper["body"])["resultList"]["result"]
        if r["id"] == "36951104" and r["source"] == "MED"
    ]
    require(len(rows) == 1 and rows[0]["doi"] == "10.1093/nar/gkad193", "publication identifier mismatch")
    return {k: rows[0][k] for k in ("id", "source", "pmid", "doi", "title", "pubYear")}


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["source_term"] == "ARO:3007646"
        and plan["ncbi_requests"] == 0
        and plan["issue_1040"] == "DEFERRED"
        and plan["full_corpus_goal_status"] == "OPEN"
        and all(
            plan[k] is False
            for k in (
                "engineered_construct_is_reference_sequence",
                "current_candidate_is_official_accession_replacement",
                "paper_results_reviewed",
                "biological_record_writes",
                "experimental_allele_assignments",
            )
        ),
        "reference-only scope changed",
    )
    documents = {k: read_json(root, p) for k, p in plan["inputs"].items()}
    frozen = documents["structure_plan"]
    for pin in frozen["inputs"].values():
        reference.check_pin(root, pin)
    inputs = {k: read_json(root, p) for k, p in frozen["inputs"].items() if k != "source_queue"}
    require(
        inputs["previous_verification"]["artifacts"]["dossier"] == frozen["inputs"]["prior"],
        "previous verification binding changed",
    )
    term = plan["source_term"]
    row = inputs["all_status"]["terms"][term]
    require(
        row == frozen["source_context"]
        and row["definition_citations"] == ["PMID:36951104"]
        and not row["qualified_reference_accessions"]
        and term in inputs["prior"]["coverage"]["remaining_terms"],
        "selected source term changed",
    )
    records, claims = prior.prior.members.current_context(
        root, inputs["index"], inputs["corpus_update"], {term}, {term: row["source_label"]}
    )
    require(
        records == frozen["records"] and claims == frozen["claims"] and len(records) == len(claims) == 6,
        "source-owned cohort changed",
    )
    annotations = aliases.annotation_context(
        aliases.ontology_graph(root, inputs["definitions"]), {term: row}, inputs["definitions"], {}
    )
    directory = root / frozen["cache_directory"]
    check_request_history(directory)
    pdb_source, structure = structure_source(root, plan, frozen, documents)
    protein_plan = documents["protein_plan"]
    require(
        protein_plan["structure_plan"] == plan["inputs"]["structure_plan"]
        and protein_plan["structure_receipt"] == plan["receipts"]["pdb-metadata"]
        and protein_plan["canary_review"] == plan["inputs"]["canary"]
        and protein_plan["fields"] == FIELDS
        and protein_plan["preflight"]["ignored_files_included"] is True
        and protein_plan["preflight"]["existing_uniprot_queries_or_responses_found"] is False,
        "protein plan changed",
    )
    params = {"query": QUERY, "format": "json", "size": "500", "sort": "accession asc", "fields": FIELDS}
    require(
        protein_plan["requests"]["uniprot-identifiers"]["parameters"] == params, "identifier query changed"
    )
    entries, protein_source = mex.native_query(
        root, plan["receipts"]["uniprot-identifiers"], {k: [v] for k, v in params.items()}
    )
    receipt, protein_attempt = request_receipt(
        root,
        directory,
        "uniprot-identifiers",
        plan["receipts"]["uniprot-identifiers"],
        plan["inputs"]["protein_plan"],
        protein_plan["max_bytes"],
    )
    require(
        receipt["url"] == protein_plan["requests"]["uniprot-identifiers"]["url"]
        and receipt["started_at"] > pdb_source["retrieved_at"],
        "protein request preceded canary or differs from plan",
    )
    require(
        set(entries) == {plan["current_candidate_accession"], plan["historical_reference_accession"]},
        "inspected candidate set changed",
    )
    reject_operational_fields(entries)
    registry = dict(inputs["taxonomy_inventory"]["registry"])
    binding = frozen["source_species"]
    require(
        binding == inputs["all_status"]["source_bindings"]["Neobacillus vireti"],
        "source species binding changed",
    )
    registry["220686"] = {"taxon_id": "220686", "source": binding["native_source"]}
    tax_plan = documents["taxonomy_plan"]
    require(
        tax_plan["protein_receipt"] == plan["receipts"]["uniprot-identifiers"]
        and tax_plan["url"] == "https://rest.uniprot.org/taxonomy/1131730.json"
        and tax_plan["taxon_id"] == "1131730"
        and "1131730" not in registry,
        "new taxonomy plan changed",
    )
    tax_receipt, tax_attempt = request_receipt(
        root,
        directory,
        "taxonomy-1131730",
        plan["receipts"]["taxonomy-1131730"],
        plan["inputs"]["taxonomy_plan"],
        tax_plan["max_bytes"],
    )
    require(tax_receipt["url"] == tax_plan["url"], "taxonomy URL changed")
    registry["1131730"] = {
        "taxon_id": "1131730",
        "source": {"url": tax_plan["url"], "wrapper": plan["receipts"]["taxonomy-1131730"]},
    }
    nodes, taxonomy = {}, {}
    for tid in ("220686", "224308", "1131730"):
        nodes[tid], taxonomy[tid] = prior.cached_node(root, registry[tid])
    require(
        prior.lineages.identity(nodes["220686"]) == binding["identity"]
        and prior.prior.species_name_binding("Neobacillus vireti", nodes["220686"])
        == binding["native_name_fields"],
        "native source species differs",
    )
    current, historical = (
        entries[plan["current_candidate_accession"]],
        entries[plan["historical_reference_accession"]],
    )
    require(
        str(current["organism"]["taxonId"]) == plan["reference_strain"] == "1131730",
        "reference strain changed",
    )
    view = prior.prior.members.member_reference(current, nodes["1131730"])
    link = reference_link(
        current,
        historical,
        plan["native_source_locus"],
        binding["identity"],
        view["reference_taxonomy"]["species"],
    )
    require(
        link["current_native_uniparc_id"]
        == link["historical_native_uniparc_id"]
        == plan["shared_native_uniparc_id"],
        "inspected archive identifier changed",
    )
    old_gene = inputs["all_status"]["queries"]["proteins-220686"]
    require(
        len(old_gene["pages"]) == 1 and old_gene["complete_for_query"] is True,
        "reused gene query scope changed",
    )
    old_params = {**params, "query": "(gene_exact:vmlr2) AND taxonomy_id:220686", "fields": prior.FIELDS}
    old_entries, old_source = mex.native_query(
        root, old_gene["pages"][0]["receipt"], {k: [v] for k, v in old_params.items()}
    )
    require(not old_entries and old_gene["result_count"] == 0, "reused zero-result gene query changed")
    own = inputs["citation_queries"]["queries"]["36951104"]
    own_entries, own_source = aliases.literature.read_query(root, root / own["directory"], "36951104")
    require(not own_entries and own_source == own["query"], "reused own-citation query changed")
    access = inputs["access_review"]
    require(
        access["primary_document_review"] == "NOT_COMPLETED_ACCESS_HELD"
        and access["alternate_article_copies_requested_after_denial"] == 0
        and access["independent_metadata_is_primary_results_review"] is False,
        "primary access hold changed",
    )
    previous = inputs["prior"]["coverage"]
    added = [term] if link["qualified_reference"] else []
    combined = sorted(set(previous["qualified_terms"]) | set(added))
    remaining = sorted(set(previous["remaining_terms"]) - set(added))
    require(
        len(combined) + len(remaining) == previous["cohort_terms"] == 178
        and not set(combined) & set(remaining),
        "coverage partition changed",
    )
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "inputs": frozen["inputs"],
        "records": records,
        "claims": claims,
        "source_annotations": annotations,
        "terms": {
            term: {
                "aro_id": term,
                "source_label": row["source_label"],
                "record_memberships": row["record_memberships"],
                "definition_citations": row["definition_citations"],
                "qualified_reference_accessions": [link["protein_accession"]] if added else [],
                "reference_link": link,
                "whole_record_primary_review": "OPEN",
            }
        },
        "structure": structure,
        "structure_source": pdb_source,
        "reference_view": view,
        "historical_reference": identifiers.inactive_reference(historical),
        "native_pdb_cross_references_in_current_response": [
            x for x in current.get("uniProtKBCrossReferences", []) if x["database"] == "PDB"
        ],
        "reference_query": {"attempt": protein_attempt, "source": protein_source},
        "taxonomy_sources": taxonomy,
        "new_taxonomy_attempt": tax_attempt,
        "source_species_context": binding,
        "expression_host_taxonomy": prior.lineages.identity(nodes["224308"]),
        "publication_metadata": publication_metadata(inputs["publication_discovery"]),
        "primary_access_review": access,
        "reused_gene_query": old_source,
        "reused_own_citation_query": own_source,
        "coverage": {
            "cohort_terms": 178,
            "previous_qualified_count": len(previous["qualified_terms"]),
            "new_qualified_terms": added,
            "qualified_terms": combined,
            "remaining_terms": remaining,
            "whole_corpus_completion": False,
        },
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(records),
            "source_claims": len(claims),
            "pdb_entities_inspected": structure["entity_count_inspected"],
            "focal_entities": 1,
            "active_reference_entries": 1,
            "inactive_reference_entries": 1,
            "new_qualified_source_terms": len(added),
            "combined_qualified_terms": len(combined),
            "combined_remaining_terms": len(remaining),
            "new_pdb_metadata_requests": 1,
            "new_uniprot_metadata_requests": 1,
            "new_taxonomy_requests": 1,
            "reused_taxonomy_nodes": 2,
            "reused_complete_queries": 2,
            "new_primary_results_reviews": 0,
            "biological_record_writes": 0,
            "experimental_allele_assignments": 0,
            "ncbi_requests": 0,
        },
        "limits": [
            "Focal entity selection is an inference from the structure title, matching own citation "
            "and unique source-organism entity; the native entity name remains ExpZ.",
            "The historical PDB cross-reference is inactive; the current ORF reference shares its "
            "UniParc identifier but is not declared an official accession replacement.",
            "Shared reference archive identity does not equate the engineered deposited construct "
            "to the reference protein or a resistant allele.",
            "The reference strain is not assigned as the deposited donor strain, which is absent "
            "in the selected native fields.",
            "The deposited expression host is distinct from the donor species and is not inferred "
            "to be the organism tested in every phenotype assay.",
            "No primary results, supplements or figures were reviewed; the PDF 403 hold was not "
            "bypassed through an alternate article copy.",
            "No sequences, variant specifications, protocols, numeric AST or experimental genome "
            "assignments are exported.",
            "Claim reference_status fields preserve the input-index checkpoint, not the updated "
            "term assessment. Complete zero-result queries are not biological absence.",
            "The 178-term reference cohort is not the full corpus; #1040 remains deferred and the "
            "investigation remains OPEN.",
        ],
        "attribution": {
            "CARD_ARO": "CC BY 4.0",
            "UniProt": "CC BY 4.0",
            "PDB_metadata": "CC0; reference only, no source adoption",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    output = args.root / args.output
    if args.check or output.exists():
        require(output.read_text() == payload, "saved VmlR2 audit differs from offline replay")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
