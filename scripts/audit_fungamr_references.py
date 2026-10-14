"""Replay fungal identity searches without upgrading them to resistance evidence."""

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlsplit

import audit_fungamr_cohort as cohort_audit
import audit_topoisomerase_references as reference
from resistance_checkpoint_records import checkpoint_path

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-13-fungamr-references")
OUTPUT = Path("research/2026-10-13-fungamr-reference-followup.json")
FIELDS = ("accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
          "lit_pubmed_id,sequence_version,version")
SELECTED = {
    "ARO:3009239": "Q59MJ1",
    "ARO:3009486": "I1RBR4",
    "ARO:3009588": "P10614",
    "ARO:3009534": "C6GJL4",
}


def exact_name(body, name):
    entries = body.get("results", [body])
    if any(
        type(e.get("taxonId")) is not int
        or e["taxonId"] < 1
        or not isinstance(e.get("scientificName"), str)
        or not e["scientificName"]
        or type(e.get("active")) is not bool
        or not isinstance(e.get("rank"), str)
        or not isinstance(e.get("synonyms", []), list)
        or any(not isinstance(s, str) for s in e.get("synonyms", []))
        for e in entries
    ):
        raise ValueError("invalid taxonomy identity fields")
    if len({e["taxonId"] for e in entries}) != len(entries):
        raise ValueError("duplicate taxon identifier")
    matches = [
        e
        for e in entries
        if e.get("active") is True
        and e.get("rank") == "species"
        and (e.get("scientificName") == name or name in e.get("synonyms", []))
    ]
    if len(matches) != 1:
        return {
            "status": "UNRESOLVED_EXACT_NAME",
            "species_id": None,
            "result_count": len(entries),
            "exact_match_count": len(matches),
        }
    entry = matches[0]
    return {
        "status": "EXACT_UNIPROT_NAME_OR_SYNONYM",
        "species_id": entry["taxonId"],
        "scientific_name": entry["scientificName"],
        "result_count": len(entries),
        "matching_field": "scientificName" if name == entry["scientificName"] else "synonyms",
    }


def validate_gene_results(body, gene, reviewed):
    if type(reviewed) is not bool:
        raise ValueError("review status must be explicit")
    expected = "UniProtKB reviewed (Swiss-Prot)" if reviewed else "UniProtKB unreviewed (TrEMBL)"
    seen = set()
    for entry in body["results"]:
        if (
            entry["entryType"] != expected
            or "sequence" in entry
            or "features" in entry
            or entry["primaryAccession"] in seen
        ):
            raise ValueError("review status, duplicate accession or sequence-free scope changed")
        seen.add(entry["primaryAccession"])
        blocks = 0
        for block in entry.get("genes", []):
            names = [block["geneName"]["value"]] if "geneName" in block else []
            names += [n["value"] for n in block.get("synonyms", [])]
            blocks += gene.casefold() in {name.casefold() for name in names}
        if blocks != 1:
            raise ValueError("gene absent or ambiguous; ORF identifiers are not aliases")
    return {
        "result_count": len(body["results"]),
        "suggestions_ignored": len(body.get("suggestions", [])),
        "zero_results_establish_absence": False,
        "reviewed_subset": reviewed,
    }


def disposition(queries):
    if any(
        type(q["reviewed_subset"]) is not bool or type(q["result_count"]) is not int or q["result_count"] < 0
        for q in queries
    ):
        raise ValueError("invalid query counts or review status")
    by_status = {q["reviewed_subset"]: q["result_count"] for q in queries}
    if len(by_status) != len(queries) or True not in by_status:
        raise ValueError("duplicate or missing reviewed-subset query")
    if by_status[True] > 0:
        if False in by_status:
            raise ValueError("unreviewed subset was not part of the reviewed-hit selection policy")
        return "REVIEWED_REFERENCE" if by_status[True] == 1 else "MULTIPLE_CANDIDATES_NO_SELECTION"
    if False not in by_status:
        raise ValueError("empty reviewed subset still needs the planned unreviewed search")
    return (
        "UNREVIEWED_CANDIDATE"
        if by_status[False] == 1
        else "MULTIPLE_CANDIDATES_NO_SELECTION"
        if by_status[False] > 1
        else "NO_EXACT_GENE_RESULTS_NOT_ABSENCE"
    )


def local_response(root, directory, key, url):
    attempt_path = directory / f"{key}-attempt.json"
    attempt = json.loads(attempt_path.read_bytes())
    receipt_path = directory / f"{key}-receipt.json"
    receipt = json.loads(receipt_path.read_bytes())
    if attempt["url"] != url or receipt.get("retry_performed") is not False:
        raise ValueError("planned request or single-attempt policy changed")
    body, provenance = cohort_audit.read_source(
        root,
        {
            "url": url,
            "body": reference.pin(root, directory / f"{key}-response.bin"),
            "receipt": reference.pin(root, receipt_path),
        },
    )
    return body, {**provenance, "attempt": reference.pin(root, attempt_path)}


def nomenclature(root, review, native_name_body):
    reference.check_pin(root, review["source"])
    reference.check_pin(root, review["receipt"])
    for item in review["rendered_pages"]:
        reference.check_pin(root, item)
    if (
        review["doi"] != "10.3314/mmj.22.004"
        or review["source_name"] != "Nakaseomyces glabratus"
        or review["uniprot_species_name"] != "Candida glabrata"
        or review["mycobank_id_reported_by_paper"] != "843854"
        or review["nomenclatural_synonymy_verified"] is not True
        or review["native_pages_visually_inspected"] is not True
        or review["printed_pages"] != [126, 128]
        or review["zero_based_pages"] != [7, 9]
    ):
        raise ValueError("specific primary nomenclatural assessment changed")
    matches = [t for t in native_name_body["results"] if t["taxonId"] == 5478]
    if (
        len(matches) != 1
        or matches[0]["scientificName"] != "Candida glabrata"
        or matches[0]["active"] is not True
        or matches[0]["rank"] != "species"
        or "Nakaseomyces glabratus" not in matches[0].get("otherNames", [])
    ):
        raise ValueError("primary synonym no longer agrees with the native taxonomy context")
    return {
        "status": "PRIMARY_NOMENCLATURE_PLUS_UNIPROT_TAXONOMY",
        "species_id": 5478,
        "scientific_name": "Candida glabrata",
        "source_name": "Nakaseomyces glabratus",
        "doi": review["doi"],
        "printed_pages": review["printed_pages"],
        "mycobank_id_reported_by_paper": "843854",
        "experimental_subject_assignment": False,
    }


def project(entry, taxonomy, gene, species, reviewed):
    validate_gene_results({"results": [entry]}, gene, reviewed)
    result = reference.project_reference(entry, gene, species, taxonomy, reviewed=reviewed)
    if taxonomy["rank"] not in {"species", "strain"}:
        raise ValueError("reference taxonomy rank is not species or strain")
    result.pop("bibliography")
    result["orf_names"] = sorted({v["value"] for b in entry.get("genes", []) for v in b.get("orfNames", [])})
    result.update(
        {
            "role": "REVIEWED_GENE_REFERENCE" if reviewed else "UNREVIEWED_REFERENCE_CANDIDATE",
            "canonical_reference_established": False,
            "exact_fungamr_row_crosswalk_verified": False,
            "experimental_genome_assignment": None,
            "new_resistance_assertion": False,
        }
    )
    return result


def archive_crosswalk(entry):
    links = [r for r in entry.get("uniProtKBCrossReferences", []) if r["database"] == "EMBL"]
    if entry["primaryAccession"] != "C6GJL4" or len(links) != 1 or links[0]["id"] != "FJ976683":
        raise ValueError("published archive-reference crosswalk changed")
    properties = {p["key"]: p["value"] for p in links[0]["properties"]}
    if properties != {"ProteinId": "ACS37521.1", "Status": "-", "MoleculeType": "mRNA"}:
        raise ValueError("archive protein, status or source-reported molecule type changed")
    return {
        "paper_reported_reference": "FJ976683",
        "uniprot_accession": "UniProtKB:C6GJL4",
        "archive_protein_id": "ACS37521.1",
        "source_reported_molecule_type": "mRNA",
        "role": "PAPER_REFERENCE_LOCUS_NOT_GENOME_OR_TESTED_ALLELE",
        "archive_endpoint_requested": False,
    }


def build(root, directory):
    selection_path = directory / "reference-selection.json"
    selection = json.loads(selection_path.read_bytes())
    cohort = json.loads(reference.check_pin(root, selection["cohort"]).read_bytes())
    prior = json.loads(reference.check_pin(root, cohort["prior"]).read_bytes())
    for key in ("prior_verification", "protected", "census"):
        reference.check_pin(root, cohort[key])
    plans = {k: json.loads(reference.check_pin(root, v).read_bytes()) for k, v in selection["plans"].items()}
    requests = {}
    for plan in plans.values():
        if set(requests) & set(plan["requests"]):
            raise ValueError("duplicate planned request")
        requests.update(plan["requests"])
    if len(requests) != 28 or cohort["fields"] != FIELDS:
        raise ValueError("planned search scope changed")
    pending = {k: v for k, v in prior["terms"].items() if "reference" not in v}
    if cohort["terms"] != pending or len(pending) != 13:
        raise ValueError("pending term membership changed")
    with reference.check_pin(root, cohort["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["path"] for r in census}) != len(census)
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        or any(reference.digest(checkpoint_path(root, r)) != r["record_sha256"] for r in census)
    ):
        raise ValueError("whole-corpus membership or bytes changed")
    if cohort["records"] != prior["records"] or len(cohort["records"]) != 10:
        raise ValueError("record cohort changed")
    for item in cohort["records"]:
        record = load_record(checkpoint_path(root, item))
        if (
            record["identifier"] != item["identifier"]
            or record["chemical_structure"]["standard_inchi_key"] != item["standard_inchi_key"]
        ):
            raise ValueError("record identity changed")
    bodies, sources = {}, {}
    for key, request in requests.items():
        bodies[key], sources[key] = local_response(root, directory, key, request["url"])
    names = {}
    for name, item in plans["initial"]["names"].items():
        if item["status"] == "REUSE_VERIFIED_CACHE":
            body, source = cohort_audit.read_source(root, item["source"])
        else:
            body, source = bodies[item["key"]], sources[item["key"]]
            expected = {"query": [f'"{name}" AND rank:species'], "format": ["json"], "size": ["500"]}
            if parse_qs(urlsplit(source["url"]).query) != expected:
                raise ValueError("taxonomy name query changed")
        names[name] = {**exact_name(body, name), "source": source}
    review = json.loads(reference.check_pin(root, selection["nomenclature"]).read_bytes())
    names["Nakaseomyces glabratus"].update(nomenclature(root, review, bodies["name-nakaseomyces-glabratus"]))
    if len(names) != 10 or any(n["species_id"] is None for n in names.values()):
        raise ValueError("source-name coverage is incomplete")
    terms = {}
    for term, prior_term in pending.items():
        name = prior_term["source_organism_name"]
        species = names[name]["species_id"]
        queries = []
        for key, request in requests.items():
            if request.get("term") != term:
                continue
            reviewed = request["kind"] == "reviewed_gene"
            query = (f"gene_exact:{prior_term['source_gene']} AND taxonomy_id:{species} "
                     f"AND reviewed:{str(reviewed).lower()}")
            expected = {"query": [query], "format": ["json"], "size": ["500"], "fields": [FIELDS]}
            url = urlsplit(request["url"])
            if url.path != "/uniprotkb/search" or parse_qs(url.query) != expected:
                raise ValueError("gene, taxonomy or field scope changed")
            queries.append(
                {
                    "key": key,
                    "source": sources[key],
                    **validate_gene_results(bodies[key], prior_term["source_gene"], reviewed),
                }
            )
        terms[term] = {
            "gene": prior_term["source_gene"],
            "source_organism_name": name,
            "source_species_taxon_id": f"NCBITaxon:{species}",
            "record_memberships": prior_term["record_memberships"],
            "status": disposition(queries),
            "queries": queries,
            "experimental_subject_assignment": None,
            "exact_allele_assignment": None,
            "new_resistance_assertion": False,
        }
    if {k: v["accession"] for k, v in selection["selected"].items()} != SELECTED:
        raise ValueError("reviewed singleton selections changed")
    if set(SELECTED) != {
        k for k, t in terms.items() if t["status"] in {"REVIEWED_REFERENCE", "UNREVIEWED_CANDIDATE"}
    }:
        raise ValueError("singleton selections no longer cover the query results")
    for term, selected in selection["selected"].items():
        (entry,) = bodies[selected["query_key"]]["results"]
        taxa, tax_source = cohort_audit.read_source(root, selected["taxonomy_source"])
        (taxon,) = [t for t in taxa.get("results", [taxa]) if t["taxonId"] == selected["reference_taxon_id"]]
        if entry["primaryAccession"] != selected["accession"]:
            raise ValueError("selected accession changed")
        terms[term]["reference_context"] = project(
            entry,
            taxon,
            terms[term]["gene"],
            names[terms[term]["source_organism_name"]]["species_id"],
            selected["reviewed"],
        )
        terms[term]["reference_taxonomy_source"] = tax_source
    crosswalk_plan = json.loads(reference.check_pin(root, selection["puccinia_crosswalk_plan"]).read_bytes())
    expected_url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {"query": "accession:C6GJL4", "format": "json", "size": "500", "fields": FIELDS + ",xref_embl"}
    )
    if crosswalk_plan["url"] != expected_url:
        raise ValueError("archive crosswalk request scope changed")
    expanded, expanded_source = local_response(root, directory, "puccinia-crosswalk", expected_url)
    (entry,) = expanded["results"]
    (old_entry,) = bodies["gene-3009534-unreviewed"]["results"]
    if {k: v for k, v in entry.items() if k != "uniProtKBCrossReferences"} != old_entry:
        raise ValueError("entry changed between identity and cross-reference reads")
    crosswalk = {**archive_crosswalk(entry), "source": expanded_source}
    primary = json.loads(reference.check_pin(root, selection["puccinia_primary"]).read_bytes())
    if primary["reported_archive_reference"] != crosswalk["paper_reported_reference"]:
        raise ValueError("indexed primary reference and archive mapping differ")
    counts = dict(Counter(t["status"] for t in terms.values()))
    prior_reference_count = sum("reference" in t for t in prior["terms"].values())
    return {
        "scope": "FUNGAMR_SHARED_CITATION_REFERENCE_FOLLOWUP",
        "date": "2026-10-13",
        "inputs": {
            "selection": reference.pin(root, selection_path),
            "prior": cohort["prior"],
            "prior_verification": cohort["prior_verification"],
            "census": cohort["census"],
        },
        "names": names,
        "terms": terms,
        "nomenclature_assessment": review,
        "puccinia_reference_crosswalk": crosswalk,
        "puccinia_partial_primary_context": primary,
        "summary": {
            "pending_terms_investigated": 13,
            "source_names_resolved": 10,
            "term_dispositions": counts,
            "uniprot_api_requests": 29,
            "primary_pdf_retrievals": 1,
            "web_tool_calls": selection["web_tool_calls"],
            "prior_reviewed_reference_contexts": prior_reference_count,
            "total_reviewed_reference_contexts": prior_reference_count + counts.get("REVIEWED_REFERENCE", 0),
            "additional_unreviewed_candidate_contexts": counts.get("UNREVIEWED_CANDIDATE", 0),
            "cohort_terms": len(prior["terms"]),
            "cohort_records": len(cohort["records"]),
            "corpus_records_hash_verified": 2939,
            "biological_records_changed": 0,
            "new_resistance_assertions": 0,
            "exact_alleles_assigned": 0,
            "whole_record_reviews_completed": 0,
        },
        "constraints": cohort["constraints"],
        "review_findings": [
            {
                "id": "taxonomy-near-matches",
                "status": "ADDRESSED",
                "disposition": ("Excluded hybrid, virus and otherNames-only matches; "
                                "the latter required a separate primary nomenclatural assessment."),
            },
            {
                "id": "query-suggestions",
                "status": "ADDRESSED",
                "disposition": ("Only native results count. "
                                "Suggested searches with altered taxonomy IDs were not followed."),
            },
            {
                "id": "unreviewed-not-canonical",
                "status": "SCOPE_GUARD_APPLIED",
                "disposition": ("The unreviewed singleton is a reference candidate, "
                                "not a verified canonical protein or resistant allele."),
            },
            {
                "id": "puccinia-primary-scope",
                "status": "OPEN",
                "disposition": ("The submission title and related publisher abstract do not establish "
                                "a causal resistant allele; inspect full primary results, figures and "
                                "source-row context before replacing the CARD claim."),
            },
            {
                "id": "fungamr-drug-label-discrepancy",
                "status": "OPEN",
                "disposition": ("CYP51B identity does not resolve ARO:3009486's voriconazole-label "
                                "versus tebuconazole-edge discrepancy."),
            },
        ],
        "limitations": [
            "Reference identifiers are not experimental subject or allele assignments.",
            "Multiple matches remain unselected; empty exact-gene searches do not establish "
            "gene or protein absence.",
            "The nomenclatural assessment is primary-source reading; the Puccinia phenotype context "
            "is only publisher-indexed abstract/snippet reading.",
            "No sequences, variant specifications, numeric AST, experimental protocols "
            "or inferred genome assignments are exported.",
            "The source-reported archive molecule type is retained without independent archive validation.",
            "No whole-record signoff, new source adoption, NCBI request, "
            "issue 1040 work or GitHub mutation occurred.",
        ],
        "attribution": ("UniProt Consortium, release 2026_03, CC BY 4.0; CARD/ARO; "
                        "Takashima and Sugita (2022); Stammler et al. (2009)."),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--cache", type=Path, default=CACHE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    result = build(root, root / args.cache)
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    output = root / args.output
    if args.check or output.exists():
        if output.read_bytes() != payload:
            raise SystemExit("saved reference follow-up differs from pinned evidence")
    else:
        output.write_bytes(payload)
    print(json.dumps(result["summary"]))


if __name__ == "__main__":
    main()
