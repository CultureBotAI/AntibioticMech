"""Compare definition citations with pinned UniProt bibliography, offline only.

A shared paper can concern unrelated genes. Citation overlap is retained as a
review lead, never used to assign a protein, allele, organism or phenotype.
"""

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import audit_card_definition_citations as citations
import audit_card_grounding as card
import audit_topoisomerase_references as reference

DEFAULT_DIRECTORY = Path("reports/resistance-grounding-2026-10-09-card-citation-concordance")
DEFAULT_OUTPUT = Path("research/2026-10-09-card-citation-concordance.json")
SCOPE = "REFERENCE_BIBLIOGRAPHY_CONCORDANCE_NOT_EXPERIMENTAL_IDENTITY_OR_CAUSAL_EVIDENCE"


def citation_id(database, value):
    if database == "PubMed" and re.fullmatch(r"[1-9][0-9]*", value):
        return "PMID:" + value
    if database == "DOI" and re.fullmatch(r"10\.[0-9]{4,9}/[^\s]+", value):
        return "DOI:" + value.lower()
    if database in {"PubMed", "DOI"}:
        raise ValueError("malformed bibliography identifier")
    return None


def source_ids(values):
    return {citation_id({"PMID": "PubMed", "DOI": "DOI"}[v.split(":", 1)[0]], v.split(":", 1)[1])
            for v in values}


def entry_bibliography(entry):
    result, seen = [], set()
    for row in entry.get("references", []):
        number = row["referenceNumber"]
        if type(number) is not int or number < 1 or number in seen:
            raise ValueError("ambiguous reference numbering")
        seen.add(number)
        ids, unresolved = set(), []
        for xref in row.get("citation", {}).get("citationCrossReferences", []):
            try:
                identifier = citation_id(xref["database"], xref["id"])
            except ValueError:
                unresolved.append({"database": xref["database"],
                                   "value_sha256": citations.text_hash(xref["id"]),
                                   "status": "MALFORMED_IDENTIFIER_NOT_REPAIRED_OR_JOINED"})
            else:
                if identifier is not None:
                    ids.add(identifier)
        if ids or unresolved:
            result.append({"reference_number": number, "identifiers": sorted(ids),
                           "unresolved_identifiers": sorted(unresolved,
                               key=lambda x: json.dumps(x, sort_keys=True))})
    return sorted(result, key=lambda row: row["reference_number"])


def gene_names(entry):
    result = set()
    for block in entry.get("genes", []):
        names = ([block["geneName"]] if "geneName" in block else []) + block.get("synonyms", [])
        for name in names:
            value = name["value"]
            if not isinstance(value, str) or not value.strip():
                raise ValueError("empty gene name")
            result.add(value)
    return sorted(result)


def project_entry(entry, taxon):
    taxid = entry["organism"]["taxonId"]
    if ("sequence" in entry or type(taxid) is not int or taxid < 1
            or taxon["taxonId"] != taxid or taxon.get("active") is not True):
        raise ValueError("sequence-bearing entry or inactive/mismatched reference taxonomy")
    audit = entry["entryAudit"]
    if any(type(audit.get(k)) is not int or audit[k] < 1 for k in ("entryVersion", "sequenceVersion")):
        raise ValueError("missing protein entry versions")
    if entry["entryType"] not in {"UniProtKB reviewed (Swiss-Prot)", "UniProtKB unreviewed (TrEMBL)"}:
        raise ValueError("unsupported protein review status")
    return {
        "accession": "UniProtKB:" + entry["primaryAccession"], "entry_type": entry["entryType"],
        "entry_version": audit["entryVersion"], "sequence_version": audit["sequenceVersion"],
        "gene_names_and_synonyms": gene_names(entry),
        "description_flag": entry.get("proteinDescription", {}).get("flag"),
        "reference_taxon_id": f"NCBITaxon:{taxid}",
        "reference_organism_name": entry["organism"]["scientificName"],
        "taxonomy_scientific_name": taxon["scientificName"], "taxonomy_rank": taxon["rank"],
        "taxonomy_identity_verified": True, "bibliography": entry_bibliography(entry),
        "experimental_subject_assignment": False, "exact_allele_assignment": False,
    }


def concordance(entries, definitions, direct, labels):
    index = defaultdict(set)
    bibliographies = {}
    for accession, entry in sorted(entries.items()):
        if accession != entry["primaryAccession"] or "sequence" in entry:
            raise ValueError("protein key mismatch or unexpected sequence")
        bibliographies[accession] = entry_bibliography(entry)
        for row in bibliographies[accession]:
            for identifier in row["identifiers"]:
                index[identifier].add(accession)
    result = {}
    for tid, row in sorted(definitions.items()):
        ids = source_ids(row["definition_citation_ids"])
        candidates = sorted({acc for identifier in ids for acc in index[identifier]})
        direct_ids = sorted(e["primaryAccession"] for e, _ in direct.get(tid, []))
        leads = []
        for accession in candidates:
            names = gene_names(entries[accession])
            matching = [name for name in names if name.casefold() == labels[tid].casefold()]
            shared = sorted(ids & {x for ref in bibliographies[accession] for x in ref["identifiers"]})
            leads.append({
                "protein_accession": "UniProtKB:" + accession, "shared_citation_ids": shared,
                "reference_numbers": [r["reference_number"] for r in bibliographies[accession]
                                      if ids.intersection(r["identifiers"])],
                "explicit_card_link": accession in direct_ids,
                "literal_source_label_gene_matches": matching,
                "identity_status": "LITERATURE_OVERLAP_NOT_A_PROTEIN_OR_ALLELE_ASSIGNMENT",
            })
        result[tid] = {
            "source_label_sha256": citations.text_hash(labels[tid]),
            "definition_citation_ids": sorted(ids),
            "explicit_reference_candidates": ["UniProtKB:" + acc for acc in direct_ids],
            "citation_overlap_leads": leads,
            "record_memberships": row["record_memberships"],
            "primary_support_status": "NOT_ESTABLISHED_BY_CITATION_CONCORDANCE",
        }
    return result


def analyze(root, directory, only=None):
    plan_path = directory / "plan.json"
    plan = json.loads(plan_path.read_bytes())
    paths = {k: reference.check_pin(root, value) for k, value in plan["inputs"].items()}
    source = json.loads(paths["citations"].read_bytes())
    prior = json.loads(paths["references"].read_bytes())
    snapshot = json.loads(paths["proteins"].read_bytes())
    old_taxonomy = json.loads(paths["taxonomy"].read_bytes())
    if (prior["protein_snapshot_sha256"] != plan["inputs"]["proteins"]["sha256"]
            or prior["taxonomy_snapshot_sha256"] != plan["inputs"]["taxonomy"]["sha256"]
            or old_taxonomy["proteins_sha256"] != prior["protein_snapshot_sha256"]
            or snapshot["source_inventory_sha256"] != plan["inputs"]["source_inventory"]["sha256"]
            or snapshot["release"] != prior["summary"]["release"]
            or snapshot["total"] != len(snapshot["entries"])):
        raise ValueError("reference snapshot provenance mismatch")
    if any(source["inputs"][k] != plan["inputs"][k] for k in ("current_census", "source_inventory")):
        raise ValueError("citation source inputs differ from current plan")
    census, labels, memberships, records = citations.read_corpus(root, paths["current_census"])
    if set(labels) != set(source["terms"]) or set(labels) != set(prior["determinants"]):
        raise ValueError("term coverage differs between current corpus and source audits")
    for tid, label in labels.items():
        if (citations.text_hash(label) != source["terms"][tid]["label_sha256"]
                or prior["determinants"][tid]["labels"] != [label]
                or sorted(memberships[tid]) != source["terms"][tid]["record_memberships"]):
            raise ValueError("source label or record membership drift")
    direct = card.reference_index(snapshot["entries"], labels)
    for tid, row in prior["determinants"].items():
        if [card.candidate(e, x, old_taxonomy["taxa"]) for e, x in direct[tid]] != row["candidates"]:
            raise ValueError("original explicit reference projection does not reproduce")
    selected = set(labels) if only is None else set(only)
    if not selected or not selected <= set(labels):
        raise ValueError("invalid term selection")
    terms = concordance(snapshot["entries"], {t: source["terms"][t] for t in selected}, direct, labels)
    anomalies = [{"protein_accession": "UniProtKB:" + acc,
                  "reference_number": row["reference_number"], **item}
                 for acc, entry in sorted(snapshot["entries"].items()) for row in entry_bibliography(entry)
                 for item in row["unresolved_identifiers"]]
    retained = {acc.removeprefix("UniProtKB:") for row in terms.values()
                for acc in row["explicit_reference_candidates"]}
    retained.update(x["protein_accession"].removeprefix("UniProtKB:") for row in terms.values()
                    for x in row["citation_overlap_leads"])
    taxa = dict(old_taxonomy["taxa"])
    requests = {}
    for taxid in plan["additional_taxa"]:
        key = f"tax-{taxid}"
        if str(taxid) in taxa:
            raise ValueError("additional taxonomy would replace existing context")
        taxa[str(taxid)], requests[key] = reference.read_response(root, directory, key, f"/taxonomy/{taxid}")
        if (requests[key]["release"] != snapshot["release"]
                or requests[key]["url"] != plan["metadata_urls"][key]):
            raise ValueError("taxonomy request or release differs from plan")
    proteins = {"UniProtKB:" + acc: project_entry(snapshot["entries"][acc],
                taxa[str(snapshot["entries"][acc]["organism"]["taxonId"])]) for acc in sorted(retained)}
    overlapping = {t for t, row in terms.items() if row["citation_overlap_leads"]}
    unlinked = {t for t, row in terms.items() if not row["explicit_reference_candidates"]}
    leads = [x for row in terms.values() for x in row["citation_overlap_leads"]]
    selected_records = {v for t in selected for v in memberships[t]}
    result = {
        "scope": SCOPE, "selection": "ALL_EXISTING_CARD_TERMS" if only is None else "CANARY_ONLY",
        "inputs": {**plan["inputs"], "plan": reference.pin(root, plan_path)},
        "release": snapshot["release"], "taxonomy_requests": requests,
        "terms": terms, "proteins": proteins, "snapshot_bibliography_anomalies": anomalies,
        "records": [row for row in records if row["identifier"] in selected_records],
        "summary": {
            "corpus_records_checked": len(census), "terms": len(terms),
            "source_assertion_memberships": sum(len(memberships[t]) for t in selected),
            "compound_records": len(selected_records),
            "cached_uniprot_entries_searched": len(snapshot["entries"]),
            "retained_reference_entries": len(proteins),
            "retained_reference_taxa": len({p["reference_taxon_id"] for p in proteins.values()}),
            "explicit_reference_links_reproduced": sum(len(r["explicit_reference_candidates"])
                                                        for r in terms.values()),
            "terms_with_citation_overlap": len(overlapping), "citation_overlap_links": len(leads),
            "explicit_links_with_citation_overlap": sum(x["explicit_card_link"] for x in leads),
            "unlinked_terms_with_citation_overlap": len(unlinked & overlapping),
            "unlinked_terms_without_overlap_in_this_snapshot": len(unlinked - overlapping),
            "unlinked_terms_with_literal_gene_match": sum(any(x["literal_source_label_gene_matches"]
                for x in terms[t]["citation_overlap_leads"]) for t in unlinked),
            "unlinked_literal_gene_match_links": sum(bool(x["literal_source_label_gene_matches"])
                for t in unlinked for x in terms[t]["citation_overlap_leads"]),
            "additional_taxonomy_requests": len(requests),
            "snapshot_malformed_identifiers_not_joined": len(anomalies),
            "reference_entry_types": dict(sorted(Counter(
                p["entry_type"] for p in proteins.values()).items())),
            "biological_records_changed": 0, "whole_records_completed": 0, "exact_allele_assignments": 0,
        },
        "limits": [
            "The search covers the pinned CARD-cross-referenced UniProt snapshot, not all of UniProt.",
            "A paper can concern many different genes, taxa or alleles; overlap never establishes identity.",
            "A literal gene-name match may identify a family shared by several organisms, not one allele.",
            "Absent overlap does not invalidate an explicit reference or imply absence of evidence.",
            "TaxIDs are reference contexts, including mixed or uncultured names, not experimental isolates.",
            "DOI case is normalized for comparison; reference numbers retain citation-to-entry provenance.",
            "Malformed bibliography IDs are hashed and excluded from matching, not repaired by assumption.",
            "No sequences, exact variants, protocols, coordinates or numerical AST are exported.",
            "No source adoption, NCBI requests or GitHub mutation; whole-corpus primary review remains OPEN.",
        ],
    }
    for item in plan["inputs"].values():
        reference.check_pin(root, item)
    for row in census:
        reference.check_pin(root, {"path": row["path"], "sha256": row["record_sha256"]})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--directory", type=Path, default=DEFAULT_DIRECTORY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--only", action="append")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = analyze(args.root, args.root / args.directory, args.only)
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    path = args.root / args.output
    if args.check:
        if path.read_bytes() != payload:
            raise ValueError("concordance dossier does not reproduce")
    else:
        with path.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
