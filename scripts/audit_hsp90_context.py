"""Replay conditional Hsp90 evidence context without asserting single-drug resistance."""

import argparse
import csv
import json
import zipfile
from pathlib import Path
from urllib.parse import parse_qs, urlsplit, urlunsplit
from xml.etree import ElementTree

import audit_topoisomerase_references as reference

from antibioticmech.activity_collections import load_record

DEFAULT_CACHE = Path("reports/resistance-grounding-2026-10-13-hsp90")
DEFAULT_OUTPUT = Path("research/2026-10-13-hsp90-context.json")
DOI = "10.1371/journal.pgen.1003390"
ARTICLE = "https://journals.plos.org/plosgenetics/article?id=" + DOI
TARGETS = {"CHEBI:5292": "QTQAWLPCGQOSGP-KSRBKZBZSA-N",
           "CHEBI:556075": "WYZWZEOGROVVHK-GTMNPGAYSA-N"}
REFERENCES = {"hsc82": ("HSC82", 559292, 4932), "hsp82": ("HSP82", 559292, 4932),
              "ca-hsp90": ("HSP90", 237561, 5476)}
QUERIES = {key: f"gene_exact:{gene} AND organism_id:{taxid} AND reviewed:true"
           for key, (gene, taxid, _) in REFERENCES.items()}
SUBJECTS = {"Sc-G-12": ("ScLC1539", "S. cerevisiae", "hsc82"),
            "Sc-G-14": ("ScLC1541", "S. cerevisiae", "hsc82"),
            "Ca-G-10": ("CaLC1486", "C. albicans", "ca-hsp90")}
ASSETS = {"figure2": "g002", "figure4": "g004", "table-s1": "s003", "table-s5": "s007"}


def read_table(path):
    with zipfile.ZipFile(path) as archive:
        document = ElementTree.fromstring(archive.read("word/document.xml"))
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    table, = document.findall(".//w:tbl", ns)
    return [["".join(cell.itertext()).strip() for cell in row.findall("w:tc", ns)]
            for row in table.findall("w:tr", ns)]


def project_subjects(strains, coverage):
    if (strains[0] != ["Strain name", "Strain number", "Species", "Genotype", "Source"]
            or coverage[0] != ["Strain", "Mean Coverage"]):
        raise ValueError("supplement identity or headers changed")
    sequenced = [row[0] for row in coverage[1:]]
    if len(sequenced) != 8 or len(set(sequenced)) != 8:
        raise ValueError("coverage table membership changed")
    subjects = {}
    for label, (number, species, ref) in SUBJECTS.items():
        matches = [r for r in strains[1:] if r[0] == label]
        if len(matches) != 1:
            raise ValueError("source lineage is absent or ambiguous")
        row, = matches
        if len(row) != 5 or (row[1], row[2], row[4]) != (number, species, "This study"):
            raise ValueError("source lineage identity changed")
        if label in sequenced:
            raise ValueError("selected lineage unexpectedly appears in the WGS coverage table")
        subjects[label] = {
            "source_lineage": label, "source_laboratory_id": number, "source_species": species,
            "species_taxon_id": f"NCBITaxon:{REFERENCES[ref][2]}",
            "species_grounding_basis": "PRIMARY_SPECIES_NAME_AND_UNIPROT_REFERENCE_LINEAGE",
            "reference_key": ref, "listed_in_table_s1_wgs_coverage": False,
            "strain_taxon_id_assigned": False, "exact_experimental_protein_assigned": False,
            "sample_or_genome_accession_assigned": False,
            "table_s5_locator": {"row": strains.index(row) + 1, "count_includes_header": True},
        }
    return subjects, sequenced


def project_protein(entry, key, taxonomy):
    gene, taxid, species = REFERENCES[key]
    if entry["organism"]["taxonId"] != taxid or "features" in entry:
        raise ValueError("wrong reference strain or unexpected feature payload")
    result = reference.project_reference(entry, gene, species, taxonomy)
    primary, = [g["geneName"]["value"] for g in entry["genes"]]
    if primary != gene:
        raise ValueError("reference primary gene is not the selected gene")
    identifiers = {i["id"].lower() for b in result["bibliography"] for i in b["identifiers"]}
    result.update({
        "primary_gene_name": gene,
        "gene_orf_names": sorted({v["value"] for g in entry["genes"] for v in g.get("orfNames", [])}),
        "role": "ISOFORM_HYPOTHESIS_ONLY" if key == "hsp82" else "REFERENCE_FOR_CONDITIONAL_FINDING",
        "focal_paper_in_bibliography": "23593013" in identifiers or DOI in identifiers,
        "single_drug_resistance_established": False,
    })
    return result


def project_asset(root, key, pins):
    for item in pins.values():
        reference.check_pin(root, item)
    first = json.loads((root / pins["source_receipt"]["path"]).read_bytes())
    final = json.loads((root / pins["final_receipt"]["path"]).read_bytes())
    if key == "article":
        expected_url, expected_status = ARTICLE, 200
        expected_final = expected_url
    else:
        suffix = ASSETS[key]
        endpoint = ("figure/image?download&size=large" if key.startswith("figure")
                    else "file?type=supplementary")
        expected_url = f"https://journals.plos.org/plosgenetics/article/{endpoint}&id={DOI}.{suffix}"
        expected_status = 302
        expected_final = {k.lower(): v for k, v in first["headers"].items()}["location"]
        parsed = urlsplit(expected_final)
        extension = "PNG_L" if key.startswith("figure") else "docx"
        if (parsed.scheme != "https" or parsed.netloc != "storage.googleapis.com"
                or parsed.path != f"/plos-corpus-prod/{DOI}/1/pgen.1003390.{suffix}.{extension}"):
            raise ValueError("unexpected publisher asset redirect")
        initial_body = root / first["cache_path"]
        if first["sha256"] != reference.digest(initial_body) or initial_body.read_bytes():
            raise ValueError("redirect response changed")
    if (first["url"] != expected_url or first["status"] != expected_status
            or final["url"] != expected_final or final["status"] != 200
            or final["sha256"] != pins["body"]["sha256"]
            or first["retry_performed"] or final["retry_performed"]):
        raise ValueError("primary asset provenance changed")
    parsed = urlsplit(final["url"])
    return {**pins, "source_url": expected_url, "status": 200,
            "final_url_without_query": urlunsplit((parsed.scheme, parsed.netloc, parsed.path, "", "")),
            "retrieved_at": final["retrieved_at"], "validated_redirects": int(key != "article"),
            "raw_payload_redistributed": False}


def build(root, directory):
    plan_path, inspection_path = directory / "cohort.json", directory / "inspection.json"
    plan, inspection = [json.loads(p.read_bytes()) for p in (plan_path, inspection_path)]
    if (plan["fields"] != reference.FIELDS
            or set(plan["queries"]) != set(QUERIES) | {"hsp90-2009", "hsp90-2011"}
            or any(plan["queries"][k] != q for k, q in QUERIES.items())):
        raise ValueError("query plan changed")
    if plan["primary"] != {"doi": DOI, "pmid": "23593013", "url": ARTICLE}:
        raise ValueError("primary paper identity changed")
    discovery = json.loads(reference.check_pin(root, plan["discovery"]).read_bytes())
    papers = {(c.get("pmid"), c.get("doi", "").lower()) for r in discovery["records"]
              if r["identifier"] in TARGETS for q in r["queries"] for c in q["candidates"]}
    expected_papers = {("23593013", DOI), ("19236053", "10.1021/cb9000316"),
                       ("21778327", "10.1096/fj.11-188821"), ("20138026", "10.1016/j.bcp.2010.01.031")}
    if not expected_papers <= papers:
        raise ValueError("selected discovery DOI/PMID metadata changed")
    for key in ("prior_progress", "prior_checkpoint", "taxonomy_reuse_dossier"):
        reference.check_pin(root, plan[key])
    with reference.check_pin(root, plan["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if len(census) != 2939 or {p["identifier"] for p in plan["records"]} != set(TARGETS):
        raise ValueError("historical cohort changed")
    for pin in plan["records"]:
        record = load_record(reference.check_pin(root, pin))
        row, = [r for r in census if r["identifier"] == pin["identifier"]]
        if (record["identifier"] != row["identifier"] or row["record_sha256"] != pin["sha256"]
                or record.get("resistance_mechanisms")
                or record["chemical_structure"]["standard_inchi_key"] != TARGETS[record["identifier"]]):
            raise ValueError("compound identity or evidence changed")
    invalid = json.loads(reference.check_pin(root, inspection["query_disposition"]).read_bytes())
    failed = json.loads(reference.check_pin(root, invalid["response"]).read_bytes())
    failed_receipt = json.loads(reference.check_pin(root, invalid["receipt"]).read_bytes())
    failed_url = urlsplit(failed_receipt["url"])
    expected_parameters = {"query": ["lit_pubmed_id:19236053"], "format": ["json"],
                           "size": ["500"], "fields": [reference.FIELDS]}
    if (failed_url.scheme != "https" or failed_url.netloc != "rest.uniprot.org"
            or failed_url.path != "/uniprotkb/search" or failed_url.fragment
            or parse_qs(failed_url.query) != expected_parameters
            or failed_receipt["status"] != 400 or invalid["status"] != 400
            or failed_receipt["sha256"] != invalid["response"]["sha256"]
            or failed["messages"] != ["'lit_pubmed_id' is not a valid search field"]
            or invalid["protein_absence_inferred"] or invalid["publication_query_retried"]
            or (directory / "hsp90-2011-receipt.json").exists()):
        raise ValueError("invalid query disposition changed")
    yeast_dossier = json.loads(reference.check_pin(root, plan["taxonomy_reuse_dossier"]).read_bytes())
    yeast = yeast_dossier["taxonomy_request"]
    yeast_tax, yeast_request = reference.read_response(
        root, (root / yeast["cache"]["path"]).parent, "tax-559292", "/taxonomy/559292")
    if any(yeast_request[k] != yeast[k] for k in yeast_request):
        raise ValueError("yeast taxonomy reuse changed")
    candida = json.loads(reference.check_pin(root, inspection["candida_taxonomy_dossier"]).read_bytes())
    old = candida["taxonomy"]["237561"]["request"]
    ca_tax, ca_request = reference.read_response(
        root, (root / old["cache_path"]).parent, "taxonomy-237561", "/taxonomy/237561.json")
    if ca_request["cache"]["sha256"] != old["sha256"] or ca_request["url"] != old["url"]:
        raise ValueError("Candida taxonomy reuse changed")
    taxonomy = {559292: yeast_tax, 237561: ca_tax}
    if ca_request["release"] != yeast_request["release"]:
        raise ValueError("mixed taxonomy releases")
    canary = json.loads(reference.check_pin(root, inspection["reference_canary"]).read_bytes())
    for field, suffix in (("response", "response.bin"), ("receipt", "receipt.json")):
        if canary[field] != reference.pin(root, directory / f"hsc82-{suffix}"):
            raise ValueError("reference canary is not bound to HSC82")
    if canary["manually_reviewed"] is not True:
        raise ValueError("reference canary review missing")
    proteins, requests = {}, {}
    for key, query in QUERIES.items():
        body, request = reference.read_response(root, directory, key, "/uniprotkb/search", {
            "query": [query], "format": ["json"], "size": ["500"], "fields": [reference.FIELDS]})
        entry, = body["results"]
        if request["release"] != yeast_request["release"]:
            raise ValueError("mixed UniProt releases")
        proteins[key] = project_protein(entry, key, taxonomy[REFERENCES[key][1]])
        requests[key] = {**request, "results": 1, "complete_for_query": True,
                         "all_strains_and_unreviewed_entries_searched": False}
    assets = {key: project_asset(root, key, pins) for key, pins in inspection["assets"].items()}
    if set(assets) != {"article", *ASSETS}:
        raise ValueError("selected primary asset inventory changed")
    primary_canary = json.loads(reference.check_pin(root, inspection["primary_canary"]).read_bytes())
    if (primary_canary["manually_reviewed"] is not True or primary_canary["asset"] != "figure4"
            or primary_canary["response"] != assets["figure4"]["body"]
            or primary_canary["receipt"] != assets["figure4"]["final_receipt"]):
        raise ValueError("primary visual canary is not bound to Figure 4")
    for rendering in inspection["renders"].values():
        for pin in (rendering["pdf"], *rendering["pages"]):
            reference.check_pin(root, pin)
    subjects, sequenced = project_subjects(
        read_table(root / assets["table-s5"]["body"]["path"]),
        read_table(root / assets["table-s1"]["body"]["path"]))
    access = json.loads(reference.check_pin(root, inspection["access_observations"]).read_bytes())
    reference.check_pin(root, inspection["resume"])
    return {
        "date": "2026-10-13", "scope": "CONDITIONAL_COMBINATION_EVIDENCE_NOT_SINGLE_DRUG_RESISTANCE",
        "inputs": {"plan": reference.pin(root, plan_path), "inspection": reference.pin(root, inspection_path),
                   "census": plan["census"], "prior_progress": plan["prior_progress"],
                   "prior_checkpoint": plan["prior_checkpoint"], "resume": inspection["resume"]},
        "records": [{**p, "whole_record_review": "OPEN", "assertions_added": []} for p in plan["records"]],
        "primary": {**plan["primary"], "assets": assets, "renders": inspection["renders"],
                    "manual_review": inspection["manual_primary_review"]},
        "subjects": subjects, "reference_proteins": proteins, "uniprot_requests": requests,
        "taxonomy_reuse": {"559292": {"request": yeast_request, "source": plan["taxonomy_reuse_dossier"]},
                           "237561": {"request": ca_request,
                                      "source": inspection["candida_taxonomy_dossier"]}},
        "query_validation_error": invalid,
        "conditional_findings": [
            {"lineage": "Sc-G-14", "gene": "HSC82", "geldanamycin_plus_fluconazole": "FUNCTIONAL_SUPPORT",
             "radicicol_plus_fluconazole": "LINEAGE_CROSS_RESISTANCE_NOT_INDEPENDENT_ALLELE_TEST",
             "locations": ["Results HSP90 subsection", "Figure 2C", "Figure 4A-B", "Table S5"]},
            {"lineage": "Sc-G-12", "gene": "HSC82",
             "geldanamycin_plus_fluconazole": "FUNCTIONAL_PHENOCOPY_SUPPORT",
             "radicicol_plus_fluconazole": "LINEAGE_CROSS_RESISTANCE_NOT_INDEPENDENT_ALLELE_TEST",
             "locations": ["Results HSP90 subsection", "Figure 2D", "Figure 4A,C", "Table S5"]},
            {"lineage": "Ca-G-10", "gene": "HSP90", "geldanamycin_plus_fluconazole": "FUNCTIONAL_SUPPORT",
             "radicicol_plus_fluconazole": "NO_INCREASED_CROSS_RESISTANCE_REPORTED_IN_TESTED_CONTEXT",
             "locations": ["Results HSP90 subsection", "Figure 2E", "Figure 4D-E", "Table S5"]},
        ],
        "hsp82_disposition": "COMPENSATORY_ROLE_SUGGESTED_IN_DISCUSSION_NOT_EXPERIMENTALLY_ESTABLISHED",
        "assay_scope": {"source_method": "MIC-labelled relative-growth assays "
                                         "with fixed fluconazole co-exposure",
                        "quantitative_mic_imported": False, "clinical_category_assigned": False,
                        "single_agent_controls": "Reported non-inhibitory only at tested conditions "
                                                 "in Figure 1 caption",
                        "curation_decision": "HOLD_UNCONDITIONAL_SINGLE_DRUG_ASSERTIONS"},
        "genome_context": {"source_archive_accession": "SRA065341",
                           "archive_role": "SOURCE_REPORTED_SEQUENCE_ARCHIVE_ONLY",
                           "reference_genomes": [
                               "S. cerevisiae S288c 2010 / SGD reference as of February 2011",
                               "C. albicans SC5314 / CGD assembly 21"],
                           "reference_assembly_labels_are_experimental_accessions": False,
                           "table_s1_wgs_lineages": sequenced, "selected_lineages_in_table_s1": [],
                           "no_genome_anywhere_inferred": False, "archive_endpoint_requested": False},
        "remaining_primary_leads": access["observations"] + [
            {"pmid": "21778327", "doi": "10.1096/fj.11-188821", "primary_request_status": "NOT_REQUESTED",
             "protein_or_allele_assigned": False},
            {"pmid": "20138026", "doi": "10.1016/j.bcp.2010.01.031",
             "primary_request_status": "NOT_REQUESTED",
             "human_protein_in_yeast_is_native_yeast_protein": False},
        ],
        "summary": {"corpus_records_in_scope": 2939, "selected_records": 2, "reference_proteins": 3,
                    "source_lineages": 3, "complete_uniprot_queries": 3, "invalid_queries": 1,
                    "skipped_publication_queries": 1, "new_taxonomy_requests": 0,
                    "biological_records_changed": 0, "experimental_alleles_assigned": 0,
                    "genome_accessions_assigned": 0, "whole_records_completed": 0},
        "limitations": [
            "Reference proteins and reference-strain TaxIDs are not the tested alleles "
            "or laboratory subjects.",
            "Combination findings do not establish single-drug resistance or species-wide susceptibility.",
            "Different laboratory backgrounds and negative cross-resistance comparisons remain distinct.",
            "An archive accession and an alignment reference are not a sample-to-genome crosswalk.",
            "Absence from Table S1 is bounded to that table, not absence of sequencing data everywhere.",
            "No focal citation in returned UniProt bibliographies does not negate inspected primary results.",
            "PDR1 and other determinants in the study require their own assessment; "
            "the whole paper remains open.",
            "Drug analogues and findings from other papers are not transferred to these exact structures.",
            "Offline replay verifies metadata and source bytes, "
            "not the truth of the manual scientific interpretation.",
            "No sequences, variant specifications, constructs, protocols or numerical AST are exported.",
        ],
        "constraints": {"ncbi_requests": 0, "ncbi_contact": 0, "source_adoptions": 0,
                        "github_mutations_this_checkpoint": 0, "reuse_terms_review_resumed": False,
                        "issue_1040": "DEFERRED"},
        "attribution": [{"source": "Hill, Ammar, Torti, Nislow and Cowen (2013), PLOS Genetics",
                         "doi": DOI, "license": "Creative Commons Attribution (as stated by publisher)"},
                        {"source": "UniProt Consortium", "license": "CC BY 4.0",
                         "license_url": "https://www.uniprot.org/help/license"}],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path.cwd()
    result = build(root, root / args.cache)
    payload = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    if args.check:
        if args.output.read_text() != payload:
            raise ValueError("dossier does not reproduce")
    else:
        with args.output.open("x") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
