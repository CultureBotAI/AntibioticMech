"""Bind cached literature candidates to citation-specific reference context."""

import argparse
import copy
import json
from collections import Counter
from pathlib import Path

import audit_card_citation_concordance as concordance
import audit_card_definition_citations as definitions
import audit_card_grounding as card
import audit_card_literature_proteins as literature
import audit_topoisomerase_references as reference

CACHE = Path("reports/resistance-grounding-2026-10-13-bmr-context")
OUTPUT = Path("research/2026-10-13-card-study-context.json")
SCOPE = "CITATION_SCOPED_DATABASE_CONTEXT_NOT_EXPERIMENTAL_IDENTITY_OR_PRIMARY_REVIEW"
ROLES = (
    "NUCLEOTIDE SEQUENCE", "PROTEIN SEQUENCE", "FUNCTION", "CATALYTIC ACTIVITY",
    "ACTIVITY REGULATION", "SUBCELLULAR LOCATION", "CHARACTERIZATION",
    "X-RAY CRYSTALLOGRAPHY", "PROBABLE ACTIVE SITE", "DISRUPTION PHENOTYPE",
    "MUTAGENESIS", "SEQUENCE REVISION", "SUBUNIT", "INDUCTION", "BIOPHYSICOCHEMICAL PROPERTIES",
)


def study_contexts(entry):
    contexts = card.reference_contexts(entry)
    sources = {r["referenceNumber"]: r for r in entry.get("references", [])}
    bibliography = {r["reference_number"]: r for r in concordance.entry_bibliography(entry)}
    for row in contexts:
        source = sources[row["reference_number"]]
        positions = source.get("referencePositions", [])
        if not isinstance(positions, list) or any(not isinstance(p, str) or not p.strip() for p in positions):
            raise ValueError("invalid citation role annotation")
        roles = []
        for value in positions:
            matches = [role for role in ROLES if value == role or value.startswith(role + " ")]
            if len(matches) > 1:
                raise ValueError("ambiguous role category")
            roles.append({"category": matches[0] if matches else "OTHER_HASH_ONLY",
                          "source_annotation_sha256": definitions.text_hash(value)})
        title = source["citation"].get("title")
        if title is not None and (not isinstance(title, str) or not title.strip()):
            raise ValueError("invalid citation title")
        row.update({"citation_identifiers": bibliography.get(row["reference_number"], {}).get(
                        "identifiers", []),
                    "role_annotations": roles,
                    "title_sha256": definitions.text_hash(title) if title else None,
                    "title_mentions_susceptibility": bool(title and "susceptib" in title.casefold()),
                    "raw_role_annotations_exported": False,
                    "strain_values_split_or_normalized": False,
                    "experimental_subject_assignment": False,
                    "primary_review_completed_by_this_audit": False})
    return contexts


def reference_lineage(taxon):
    if (taxon.get("active") is not True or type(taxon.get("taxonId")) is not int
            or taxon["taxonId"] < 1):
        raise ValueError("inactive reference taxonomy")
    species = [t for t in taxon.get("lineage", []) if t["rank"] == "species"]
    if taxon["rank"] == "species":
        species.append(taxon)
    if len(species) > 1:
        raise ValueError("ambiguous reference species lineage")
    if any(type(t.get("taxonId")) is not int or t["taxonId"] < 1
           or not isinstance(t.get("scientificName"), str) or not t["scientificName"].strip()
           for t in species):
        raise ValueError("invalid species lineage identity")
    return ({"taxon_id": "NCBITaxon:" + str(species[0]["taxonId"]),
             "scientific_name": species[0]["scientificName"], "rank": "species",
             "experimental_subject_assignment": False} if species else None)


def select_contexts(entry, citation_ids):
    contexts = [r for r in study_contexts(entry) if set(r["citation_identifiers"]) & set(citation_ids)]
    matched = {c for r in contexts for c in r["citation_identifiers"]} & set(citation_ids)
    if not citation_ids or matched != set(citation_ids):
        raise ValueError("source citation context missing from candidate")
    return contexts


def reused_taxonomy(root, expansion):
    pins = [*expansion["taxonomy_sources"],
            *(p for r in expansion["taxonomy_requests"].values() for p in (r["cache"], r["receipt"]))]
    taxa = {}
    for pin in pins:
        value = json.loads(reference.check_pin(root, pin).read_bytes())
        rows = value.get("taxa", {}).values() if "taxa" in value else [value] if "taxonId" in value else []
        for taxon in rows:
            key = str(taxon["taxonId"])
            if key in taxa and taxa[key] != taxon:
                raise ValueError("conflicting reused taxonomy")
            taxa[key] = taxon
    return taxa, pins


def primary_hold(root, directory, earlier_pin):
    receipt_path, body = directory / "primary-receipt.json", directory / "primary-response.bin"
    receipt = json.loads(receipt_path.read_bytes())
    attempt_path = directory / "primary-attempt.json"
    attempt = json.loads(attempt_path.read_bytes())
    url = "https://europepmc.org/articles/PMC178954?pdf=render"
    if (receipt["status"] != 403 or receipt["url"] != url or attempt["url"] != url
            or receipt["sha256"] != reference.digest(body) or receipt["bytes"] != body.stat().st_size
            or receipt["retry_performed"] is not False or body.read_bytes().startswith(b"%PDF")):
        raise ValueError("primary access-hold receipt changed")
    earlier = json.loads(reference.check_pin(root, earlier_pin).read_bytes())[
        "additional_primary_access_hold"]
    if earlier["source_pmid"] != "1675788" or earlier["reported_http_status"] != 403:
        raise ValueError("earlier primary hold changed")
    return {"doi": "10.1128/jb.179.7.2189-2193.1997", "pmid": "9079903", "source_url": url,
            "http_status": 403, "retrieved_at": receipt["retrieved_at"],
            "attempt": reference.pin(root, attempt_path), "receipt": reference.pin(root, receipt_path),
            "response": reference.pin(root, body), "full_text_received": False,
            "primary_results_reviewed": False, "alternate_route_attempted": False,
            "prior_distinct_paper_hold": earlier,
            "absence_or_global_unavailability_inferred": False}


def build(root, directory):
    plan_path = directory / "study-plan.json"
    plan = json.loads(plan_path.read_bytes())
    if (plan["selection"] != "ALL_REFERENCE_CANDIDATES_FROM_BOTH_UNLINKED_CARD_LITERATURE_COHORTS"
            or plan["network_required"] is not False
            or plan["record_or_source_input_mutations"] is not False):
        raise ValueError("study-context selection or scope changed")
    paths = {k: reference.check_pin(root, p) for k, p in plan["inputs"].items()}
    audits = {name: json.loads(paths[name].read_bytes()) for name in ("earlier", "expansion")}
    census, labels, memberships, records = definitions.read_corpus(root, paths["census"])
    if len(census) != 2939:
        raise ValueError("corpus coverage changed")
    taxa, taxonomy_pins = reused_taxonomy(root, audits["expansion"])
    entries, queries, query_members, proteins, terms = {}, {}, {}, {}, {}
    for audit_name, audit in audits.items():
        for tid, term in sorted(audit["terms"].items()):
            if not term["reference_candidates"]:
                continue
            if (tid in terms or sorted(memberships[tid]) != term["record_memberships"]
                    or definitions.text_hash(labels[tid]) != term["source_label_sha256"]):
                raise ValueError("source cohort identity or membership changed")
            candidates = []
            for candidate in term["reference_candidates"]:
                accession = candidate["protein_accession"]
                acc = accession.removeprefix("UniProtKB:")
                for citation in candidate["source_citation_ids"]:
                    if not citation.startswith("PMID:"):
                        raise ValueError("unsupported candidate citation namespace")
                    pmid = citation.removeprefix("PMID:")
                    key = audit_name + ":" + pmid
                    if key not in queries:
                        expected = audit["queries"][pmid]
                        source = reference.check_pin(root, expected["pages"][0]["cache"]).parent
                        rows, query = literature.read_query(root, source, pmid)
                        if query != {k: v for k, v in expected.items() if k != "status"}:
                            raise ValueError("complete query no longer matches frozen audit")
                        queries[key] = {"source_audit": audit_name, **query}
                        query_members[key] = set(rows)
                        for entry_acc, entry in rows.items():
                            if entry_acc in entries and entries[entry_acc] != entry:
                                raise ValueError("conflicting entry metadata across cached queries")
                            entries[entry_acc] = entry
                    if acc not in query_members[key]:
                        raise ValueError("candidate not found in cited query")
                entry = entries[acc]
                taxon = taxa[str(entry["organism"]["taxonId"])]
                projected = concordance.project_entry(entry, taxon)
                if projected != audit["proteins"][accession] or "features" in entry:
                    raise ValueError("reference identity or field scope changed")
                names, direct = literature.match_entry(entry, tid, labels[tid])
                if names != candidate["literal_gene_matches"] or direct != candidate["explicit_card_xref"]:
                    raise ValueError("candidate identity basis changed")
                protein = {**projected, "reference_species_lineage": reference_lineage(taxon),
                           "reference_contexts": study_contexts(entry),
                           "ordered_locus_names": sorted({v["value"] for g in entry.get("genes", [])
                                                          for v in g.get("orderedLocusNames", [])})}
                if accession in proteins and protein != proteins[accession]:
                    raise ValueError("candidate reference projections conflict")
                proteins[accession] = protein
                candidates.append({**copy.deepcopy(candidate),
                    "matched_study_contexts": select_contexts(entry, candidate["source_citation_ids"]),
                    "experimental_subject_assignment": False, "exact_allele_assignment": False,
                    "primary_review_completed_by_this_audit": False})
            linked_citations = {c for item in candidates for c in item["source_citation_ids"]}
            terms[tid] = {"source_audit": audit_name, "source_label": labels[tid],
                          "record_memberships": term["record_memberships"],
                          "definition_citation_ids": term["definition_citation_ids"],
                          "reference_candidates": candidates,
                          "source_citations_without_candidate_context": sorted(
                              set(term["definition_citation_ids"]) - linked_citations),
                          "whole_record_primary_review": "OPEN"}
    selected_ids = {identifier for t in terms.values() for identifier in t["record_memberships"]}
    record_rows = [{**r, "cohort_terms": sorted(t for t, row in terms.items()
                                               if r["identifier"] in row["record_memberships"]),
                    "whole_record_primary_review": "OPEN"}
                   for r in records if r["identifier"] in selected_ids]
    contexts = [r for p in proteins.values() for r in p["reference_contexts"]]
    matched = [r for t in terms.values() for c in t["reference_candidates"]
               for r in c["matched_study_contexts"]]
    return {"date": "2026-10-13", "scope": SCOPE, "selection": plan["selection"],
            "inputs": {**plan["inputs"], "plan": reference.pin(root, plan_path)},
            "attribution": audits["expansion"]["attribution"], "queries": queries,
            "taxonomy_pins": taxonomy_pins, "proteins": proteins, "terms": terms, "records": record_rows,
            "bmr_primary_hold": primary_hold(root, directory, plan["inputs"]["prior_access_hold"]),
            "summary": {"corpus_records_checked": len(census), "selected_terms": len(terms),
                "reference_proteins": len(proteins), "selected_records": len(record_rows),
                "reference_candidate_links": sum(len(t["reference_candidates"]) for t in terms.values()),
                "citation_contexts": len(contexts), "matched_study_context_links": len(matched),
                "matched_contexts_with_strain_annotations": sum(
                    bool(r["strain_annotations"]) for r in matched),
                "matched_contexts_with_multiple_strain_annotations": sum(
                    len(r["strain_annotations"]) > 1 for r in matched),
                "matched_contexts_with_susceptibility_title": sum(
                    r["title_mentions_susceptibility"] for r in matched),
                "reference_taxonomy_ranks": dict(sorted(Counter(
                    p["taxonomy_rank"] for p in proteins.values()).items())),
                "references_without_species_rank_in_lineage": sum(
                    p["reference_species_lineage"] is None for p in proteins.values()),
                "replayed_query_chains": len(queries), "new_protein_or_taxonomy_requests": 0,
                "biological_records_changed": 0, "experimental_subject_or_allele_assignments": 0,
                "whole_record_reviews_completed": 0, "full_corpus_goal_status": "OPEN"},
            "limitations": [
                "Study roles and strain labels are database annotations, not primary phenotype review.",
                "Counts describe metadata links, not independent studies or unique tested organisms.",
                "Study-specific labels are not assigned the reference entry taxon or a genome.",
                "Multiple and slash-separated strain labels remain intact; no representative is selected.",
                "A susceptibility-related title is a review flag, "
                "not a measured phenotype or resistance disproof.",
                "Missing strain comments or species lineage are missing metadata, not biological absence.",
                "Role categories summarize annotation labels; "
                "function annotations are not experimental signoff.",
                "Primary-paper holds are local observations; "
                "no alternate route or NCBI endpoint was requested.",
                "Earlier per-paper reviews remain authoritative at their stated scope; "
                "this audit does not reset them.",
                "Source-owned assertions, biological records, pages, embeddings and prior snapshots "
                "are unchanged.",
                "No sequences, exact variants, raw role strings, non-strain comment values, "
                "numeric AST or protocols exported."],
            "constraints": {"ncbi_requests": 0, "ncbi_contact": 0, "issue_1040": "DEFERRED",
                            "reuse_terms_review_resumed": False, "github_mutations": 0,
                            "source_adoptions": 0}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=CACHE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path.cwd()
    result = build(root, root / args.cache)
    if args.check:
        if json.loads(args.output.read_bytes()) != result:
            raise SystemExit("study-context dossier does not reproduce")
    else:
        with args.output.open("x") as stream:
            stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
