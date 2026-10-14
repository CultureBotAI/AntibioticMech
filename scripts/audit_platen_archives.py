"""Resolve deposited donor genes through ENA and historical UniParc metadata."""

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.parse import urlencode

import audit_card_reference_lineages as lineages
import audit_topoisomerase_references as reference
from audit_enniatin_context import complete_query
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-platen-archive")
OUTPUT = Path("research/2026-10-14-platen-archive-context.json")
COHORT_SHA = "e949f35cb582fc0dab3728db0b12d490fb3664d847425ca1b15c88bf8f743837"
ARCHIVE_FIELDS = (
    "accession,parent_accession,protein_id,gene,product,scientific_name,tax_id,strain,"
    "sequence_version,first_public,last_updated"
)
PARENT_FIELDS = (
    "accession,sequence_version,description,tax_id,scientific_name,strain,first_public,last_updated"
)
KB_FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,xref_embl,"
    "lit_pubmed_id,sequence_version,version"
)
PARC_FIELDS = "upi,accession,organism_id,organism,first_seen,last_seen"
GENES = {
    "fabF": (
        "KF543053",
        "AHA90851",
        "UPI0003C98D16",
        "V5NR11",
        "3-oxoacyl-[acyl-carrier-protein] synthase 2",
    ),
    "fabH": (
        "KF543054",
        "AHA90852",
        "UPI0003C9A5B9",
        "V5NT21",
        "Beta-ketoacyl-[acyl-carrier-protein] synthase III",
    ),
}
STRUCTURES = {"CHEBI:68236": "CSOMAHTTWTVBFL-OFBLZTNGSA-N", "CHEBI:68241": "DWUHGPPFFABTIY-RLWZQHMASA-N"}
TAXONOMY = {
    "receipt": {
        "path": "reports/resistance-grounding-2026-10-09-platen/taxonomy-58346-receipt.json",
        "sha256": "05d7d9b586fbef87bf049e96e93b798d579877ccd095ab18c6bb05a9b06b5b5d",
    },
    "body": {
        "path": "reports/resistance-grounding-2026-10-09-platen/taxonomy-58346-response.bin",
        "sha256": "ab7abb38ffb50e87d620121334288ca12ee51dc76b1f29df56a62f13c38b5b36",
    },
}


def urls():
    ena = "https://www.ebi.ac.uk/ena/portal/api/"
    result = {
        "ena-results": ("configuration-plan.json", ena + "results?format=tsv"),
        "coding-return-fields": ("fields-plan.json", ena + "returnFields?result=coding&format=tsv"),
        "coding-search-fields": ("fields-plan.json", ena + "searchFields?result=coding&format=tsv"),
        "parent-archives": (
            "parent-plan.json",
            ena
            + "search?"
            + urlencode(
                {
                    "result": "sequence",
                    "query": '(accession="KF543053" OR accession="KF543054")',
                    "fields": PARENT_FIELDS,
                    "format": "json",
                    "limit": "0",
                }
            ),
        ),
        "uniprot-protein-ids": (
            "protein-plan.json",
            "https://rest.uniprot.org/uniprotkb/search?"
            + urlencode(
                {
                    "query": '("AHA90851.1" OR "AHA90852.1")',
                    "format": "json",
                    "size": "500",
                    "fields": KB_FIELDS,
                }
            ),
        ),
        "uniparc-search-fields": (
            "uniparc-configuration-plan.json",
            "https://rest.uniprot.org/configure/uniparc/search-fields",
        ),
        "uniparc-protein-ids": (
            "uniparc-plan.json",
            "https://rest.uniprot.org/uniparc/search?"
            + urlencode(
                {
                    "query": "(dbid:AHA90851 OR dbid:AHA90852) AND database:embl-cds",
                    "format": "json",
                    "size": "500",
                    "fields": PARC_FIELDS,
                }
            ),
        ),
    }
    for gene, (parent, _, upi, _, _) in GENES.items():
        result["archive-" + gene] = (
            "archive-plan.json",
            ena
            + "search?"
            + urlencode(
                {
                    "result": "coding",
                    "query": 'parent_accession="' + parent + '"',
                    "fields": ARCHIVE_FIELDS,
                    "format": "json",
                    "limit": "0",
                }
            ),
        )
        result["uniparc-" + upi] = (
            "uniparc-crossrefs-plan.json",
            "https://rest.uniprot.org/uniparc/" + upi + "/databases?format=json&size=100",
        )
    return result


def project_archive(gene, coding, parent, candidate, crossrefs, taxon):
    if gene not in GENES:
        raise ValueError("unplanned donor gene")
    archive, protein, upi, kb, kb_name = GENES[gene]
    product = "F" + gene[1:]
    if (
        set(coding) != set(ARCHIVE_FIELDS.split(","))
        or coding["accession"] != protein
        or coding["parent_accession"] != archive
        or coding["protein_id"] != protein + ".1"
        or coding["sequence_version"] != "1"
        or coding["product"] != product
        or coding["strain"] != "MA7327"
        or any(coding[k] != "" for k in ("gene", "tax_id", "scientific_name"))
    ):
        raise ValueError("coding record identity or scope changed")
    if (
        set(parent) != set(PARENT_FIELDS.split(","))
        or parent["accession"] != archive
        or parent["sequence_version"] != "1"
        or parent["strain"] != "MA7327"
        or parent["tax_id"] != "58346"
        or parent["scientific_name"] != "Streptomyces platensis"
        or parent["description"] != f"Streptomyces platensis strain MA7327 {product} gene, complete cds."
    ):
        raise ValueError("explicit parent archive identity changed")
    if (
        lineages.identity(taxon)
        != {"taxonId": 58346, "rank": "species", "scientificName": "Streptomyces platensis"}
        or taxon.get("active") is not True
    ):
        raise ValueError("donor species taxonomy changed")
    organism = {"taxonId": 58346, "scientificName": "Streptomyces platensis"}
    if (
        candidate.get("uniParcId") != upi
        or candidate.get("uniProtKBAccessions") != [kb + ".1"]
        or candidate.get("organisms") != [organism]
        or {"sequence", "features", "sequenceFeatures"}.intersection(candidate)
    ):
        raise ValueError("archive candidate identity or scope changed")
    if (
        len(crossrefs) != 2
        or {r.get("database") for r in crossrefs} != {"EMBL", "UniProtKB/TrEMBL"}
        or any({"sequence", "features", "sequenceFeatures"}.intersection(r) for r in crossrefs)
    ):
        raise ValueError("archive database membership changed")
    by_database = {r["database"]: r for r in crossrefs}
    embl, historical = by_database["EMBL"], by_database["UniProtKB/TrEMBL"]
    if (
        embl.get("id") != protein
        or embl.get("active") is not True
        or embl.get("proteinName") != product
        or historical.get("id") != kb
        or historical.get("active") is not False
        or historical.get("proteinName") != kb_name
        or historical.get("geneName") != ("fabH" if gene == "fabH" else None)
        or any(
            r.get("organism") != organism
            or type(r.get("version")) is not int
            or type(r.get("versionI")) is not int
            or r["version"] != 1
            or r["versionI"] != 1
            for r in crossrefs
        )
    ):
        raise ValueError("versioned archival crosswalk changed")
    for row, created, updated in (
        (embl, "2014-01-06", "2026-03-19"),
        (historical, "2014-02-19", "2026-01-28"),
    ):
        if row.get("created") != created or row.get("lastUpdated") != updated:
            raise ValueError("dated archive status changed")
    return {
        "source_publication_gene": gene,
        "source_gene_assignment_basis": "PRIMARY_ACCESSION_STATEMENT_AND_EXPLICIT_ENA_PARENT_LINK",
        "donor_parent_archive": "EMBL:" + archive + ".1",
        "donor_protein_archive": "EMBL:" + protein + ".1",
        "uniparc_id": "UniParc:" + upi,
        "historical_uniprotkb_accession": "UniProtKB:" + kb,
        "historical_uniprotkb_crossref": {
            "database": historical["database"],
            "active": False,
            "version": historical["version"],
            "versionI": historical["versionI"],
            "created": historical["created"],
            "last_updated": historical["lastUpdated"],
            "protein_name": historical["proteinName"],
            "gene_name": historical.get("geneName"),
        },
        "EMBL_crossref": {
            "active": True,
            "version": embl["version"],
            "versionI": embl["versionI"],
            "created": embl["created"],
            "last_updated": embl["lastUpdated"],
        },
        "coding_record_blank_fields_preserved": ["gene", "scientific_name", "tax_id"],
        "parent_record_dates": {k: parent[k] for k in ("first_public", "last_updated")},
        "coding_record_dates": {k: coding[k] for k in ("first_public", "last_updated")},
        "donor_species": {
            "taxon_id": "NCBITaxon:58346",
            "scientific_name": "Streptomyces platensis",
            "rank": "species",
        },
        "source_donor_strain_label": "MA7327",
        "strain_taxon_id": None,
        "gene_archives_are_whole_genomes": False,
        "experimental_genome_assignment": None,
        "reference_accessions_assigned_to_tested_host_or_allele": False,
        "active_current_uniprotkb_mapping_established": False,
        "archive_membership_is_phenotype_or_mechanism_evidence": False,
        "primary_evidence_scope": "EXISTING_FABF_ASSOCIATIONS"
        if gene == "fabF"
        else "NEGATIVE_COMPARISON_NOT_POSITIVE_RESISTANCE",
        "existing_positive_claims_in_two_records": 2 if gene == "fabF" else 0,
    }


def validate_configurations(payloads):
    result_types = list(csv.DictReader(io.StringIO(payloads["ena-results"].decode()), delimiter="\t"))
    rows = [r for r in result_types if r["resultId"] == "coding"]
    if (
        len(rows) != 1
        or rows[0]["description"] != "Coding sequences"
        or rows[0]["primaryAccessionType"] != "accession"
    ):
        raise ValueError("ENA result type changed")
    returns = {
        r["columnId"]
        for r in csv.DictReader(io.StringIO(payloads["coding-return-fields"].decode()), delimiter="\t")
    }
    searches = {
        r["columnId"]
        for r in csv.DictReader(io.StringIO(payloads["coding-search-fields"].decode()), delimiter="\t")
    }
    if not set(ARCHIVE_FIELDS.split(",")) <= returns or "parent_accession" not in searches:
        raise ValueError("ENA metadata fields unsupported")
    fields = json.loads(payloads["uniparc-search-fields"])
    database = [r for r in fields if r.get("term") == "database"]
    if (
        len([r for r in fields if r.get("term") == "dbid" and r.get("label") == "Database ID"]) != 1
        or len(database) != 1
        or {"name": "EMBL CDS", "value": "embl-cds"} not in database[0]["values"]
    ):
        raise ValueError("UniParc exact database-ID field unsupported")


def build(root, directory=CACHE):
    directory = root / directory
    requests = urls()
    if any(
        {p.name.removesuffix(s) for p in directory.glob("*" + s)} != set(requests)
        for s in ("-receipt.json", "-attempt.json")
    ):
        raise ValueError("research request coverage changed")
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen archive cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    protected = json.loads(reference.check_pin(root, cohort["protected"]).read_bytes())
    reference.check_pin(root, cohort["source_queue"])
    previous = json.loads(reference.check_pin(root, cohort["previous_context"]).read_bytes())
    paper = previous["primary_papers"]["24560608"]
    primary = reference.check_pin(root, cohort["primary_cached_copy"])
    if (
        reference.digest(primary) != paper["primary_request"]["sha256"]
        or paper["doi"] != "10.1016/j.chembiol.2014.01.005"
        or paper["document_version"] != "ACCEPTED_AUTHOR_MANUSCRIPT_NOT_FINAL_PUBLISHER_VERSION"
    ):
        raise ValueError("primary archive provenance changed")
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or any(protected.get(r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("corpus preflight changed")
    if len(cohort["records"]) != 2 or {r["identifier"] for r in cohort["records"]} != set(STRUCTURES):
        raise ValueError("record cohort changed")
    for row in cohort["records"]:
        record = load_record(reference.check_pin(root, row["snapshot"]))
        if (
            record["identifier"] != row["identifier"]
            or record["chemical_structure"]["standard_inchi_key"] != STRUCTURES[row["identifier"]]
            or row["snapshot"]["sha256"] != row["record"]["sha256"]
            or protected.get(row["record"]["path"]) != row["record"]["sha256"]
            or [c["gene_families"] for c in record["resistance_mechanisms"]] != [["ptmP3"], ["fabF"]]
            or any(c["taxon_id"] != "NCBITaxon:1886" for c in record["resistance_mechanisms"])
        ):
            raise ValueError("historical donor versus host claim context changed")
    sources, payloads, plans = {}, {}, {}
    for key, (plan_name, url) in requests.items():
        sources[key] = planned_source(root, directory, key, plan_name, url)
        payloads[key] = reference.check_pin(root, sources[key]["body"]).read_bytes()
        plans[key] = json.loads(reference.check_pin(root, sources[key]["plan"]).read_bytes())
        if plans[key].get("cohort") != reference.pin(root, cohort_path):
            raise ValueError("request cohort binding changed")
    validate_configurations(payloads)

    def source_pin(key):
        return {k: sources[key][k] for k in ("body", "receipt")}

    if (
        plans["coding-return-fields"].get("configuration_canary") != source_pin("ena-results")
        or plans["archive-fabF"].get("configurations")
        != {k: source_pin(k) for k in ("coding-return-fields", "coding-search-fields")}
        or plans["parent-archives"].get("coding_canary_and_followup")
        != {g: source_pin("archive-" + g) for g in GENES}
        or plans["uniprot-protein-ids"].get("parent_archive_review") != source_pin("parent-archives")
        or plans["uniparc-search-fields"].get("complete_empty_uniprotkb_query")
        != sources["uniprot-protein-ids"]["receipt"]
        or plans["uniparc-protein-ids"].get("search_configuration") != source_pin("uniparc-search-fields")
        or plans["uniparc-UPI0003C98D16"].get("archive_search_canary") != source_pin("uniparc-protein-ids")
    ):
        raise ValueError("reviewed canary or source binding changed")
    primary_review = plans["archive-fabF"]["primary_accession_statement"]
    if (
        primary_review.get("pdf") != cohort["primary_cached_copy"]
        or primary_review.get("pdf_page") != 1
        or primary_review.get("visually_inspected") is not True
        or primary_review.get("source_pairs") != {"fabF": "KF543053", "fabH": "KF543054"}
        or primary_review.get("donor") != "Streptomyces platensis MA7327"
        or primary_review.get("paper_version") != paper["document_version"]
    ):
        raise ValueError("primary accession statement review changed")
    reference.check_pin(root, primary_review["visual_page"])
    configuration = plans["parent-archives"]["sequence_return_fields_reused"]
    config_receipt = json.loads(reference.check_pin(root, configuration["receipt"]).read_bytes())
    config_body = reference.check_pin(root, configuration["body"]).read_bytes()
    if (
        config_receipt["status"] != 200
        or hashlib.sha256(config_body).hexdigest() != config_receipt["sha256"]
        or config_receipt["url"]
        != "https://www.ebi.ac.uk/ena/portal/api/returnFields?result=sequence&format=tsv"
        or not set(PARENT_FIELDS.split(","))
        <= {r["columnId"] for r in csv.DictReader(io.StringIO(config_body.decode()), delimiter="\t")}
    ):
        raise ValueError("reused parent metadata configuration changed")
    parc_config_pin = plans["uniparc-protein-ids"]["result_configuration_reused"]
    parc_config = json.loads(reference.check_pin(root, parc_config_pin).read_bytes())
    if (
        parc_config["status"] != 200
        or parc_config["url"] != "https://rest.uniprot.org/configure/uniparc/result-fields"
        or hashlib.sha256(parc_config["body"].encode()).hexdigest() != parc_config["sha256"]
        or not set(PARC_FIELDS.split(","))
        <= {r["name"] for g in json.loads(parc_config["body"]) for r in g.get("fields", [])}
    ):
        raise ValueError("reused archive metadata configuration changed")
    reference.check_pin(root, plans["uniparc-UPI0003C98D16"]["known_database_endpoint_example"])

    def results(key, count):
        receipt = json.loads(reference.check_pin(root, sources[key]["receipt"]).read_bytes())
        return complete_query(json.loads(payloads[key]), receipt["headers"], count)

    results("uniprot-protein-ids", 0)
    candidates = results("uniparc-protein-ids", 2)
    if len({c.get("uniParcId") for c in candidates}) != 2:
        raise ValueError("duplicate archive candidate")
    parents = json.loads(payloads["parent-archives"])
    if len(parents) != 2 or {p.get("accession") for p in parents} != {"KF543053", "KF543054"}:
        raise ValueError("parent archive result membership changed")
    taxon, taxonomy_source = lineages.native_taxon(root, TAXONOMY, "58346", "2026_03")
    grounded = {}
    for gene, (archive, _, upi, _, _) in GENES.items():
        coding = json.loads(payloads["archive-" + gene])
        if len(coding) != 1:
            raise ValueError("coding accession result is ambiguous")
        matches = [c for c in candidates if c.get("uniParcId") == upi]
        if len(matches) != 1:
            raise ValueError("archive candidate membership changed")
        grounded[gene] = project_archive(
            gene,
            coding[0],
            next(p for p in parents if p["accession"] == archive),
            matches[0],
            results("uniparc-" + upi, 2),
            taxon,
        )
    return {
        "date": "2026-10-14",
        "scope": "EXPLICIT_DONOR_ARCHIVE_CROSSWALKS_NOT_EXPERIMENTAL_ALLELES",
        "cohort": reference.pin(root, cohort_path),
        "baseline_commit": cohort["baseline_commit"],
        "census": cohort["census"],
        "corpus_records_hash_checked_at_preflight": len(census),
        "records": cohort["records"],
        "previous_context": cohort["previous_context"],
        "primary_accession_review": primary_review,
        "sources": sources,
        "donor_references": grounded,
        "taxonomy_source": taxonomy_source,
        "reused_configurations": {"ENA_sequence": configuration, "UniParc_result_fields": parc_config_pin},
        "query_interpretation": {
            "current_uniprotkb_exact_protein_id_query_results": 0,
            "uniparc_candidate_count": 2,
            "native_crossref_pages_complete": 2,
            "native_EMBL_crossrefs_active": 2,
            "historical_UniProtKB_crossrefs_inactive": 2,
            "historical_UniProtKB_inactivity_explains_all_search_behavior": False,
            "empty_current_query_proves_global_protein_absence": False,
            "query_order_or_name_similarity_used_as_mapping": False,
            "archive_membership_proves_same_strain_or_experimental_allele": False,
        },
        "curation_decision": "NO_EXPERIMENTAL_PROTEIN_OR_GENOME_ASSIGNMENT_FROM_DONOR_ARCHIVES",
        "preserved_claim_scope": {
            "host_species_taxon_id": "NCBITaxon:1886",
            "host_species": "Streptomyces albidoflavus",
            "MA7327_donor_is_not_J1074_host_or_SB12013_derivative": True,
            "platencin_partial_response_not_promoted_to_full_resistance": True,
            "fabH_negative_comparison_not_promoted_to_positive_claim": True,
            "ptmP3_reference_D8L2W8_unchanged_and_not_replaced_by_fabF": True,
            "prior_primary_supplement_and_exact_experimental_identity_limits_preserved": True,
        },
        "limits": {
            "scientific_http_attempts": 11,
            "metadata_configuration_requests": 4,
            "native_taxonomy_responses_reused": 1,
            "configuration_responses_reused": 2,
            "new_primary_article_or_figure_requests": 0,
            "biological_records_changed": 0,
            "new_resistance_assertions": 0,
            "experimental_allele_assignments": 0,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "issue_1040": "DEFERRED",
            "automatic_redirects": 0,
            "retries": 0,
            "prior_source_holds_preserved": True,
            "source_adoptions": 0,
            "reuse_terms_review_resumed": False,
            "numeric_AST_variants_sequences_constructs_or_protocols_exported": False,
            "whole_record_primary_review": "OPEN",
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": [
            {
                "source": "Peterson et al. 2014",
                "doi": "DOI:10.1016/j.chembiol.2014.01.005",
                "scope": (
                    "private cached accepted manuscript accession statement; no article assets redistributed"
                ),
            },
            {
                "source": "EMBL-EBI European Nucleotide Archive",
                "scope": "selected archive identity metadata; not source adoption",
            },
            {"source": "UniProt Consortium", "license": "CC BY 4.0", "release": "2026_03"},
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != payload:
            raise SystemExit("Platen archive checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {
                "donor_archive_crosswalks": 2,
                "inactive_UniProtKB_references": 2,
                "new_resistance_assertions": 0,
            }
        )
    )


if __name__ == "__main__":
    main()
