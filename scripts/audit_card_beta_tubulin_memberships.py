"""Reconcile complete beta-tubulin references with every current CARD claim."""

import argparse
import copy
import json
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit

import audit_beta_tubulin_evidence as evidence
import audit_card_beta_tubulin_references as beta
import audit_card_folp_rpo_memberships as prior
import audit_card_reference_memberships as registry
import audit_card_topoisomerase_memberships as live

progress, reference, require = prior.progress, prior.reference, prior.require
pointer, rebase = prior.pointer, prior.rebase
PREFIX = "research/2026-10-14-card-beta-tubulin-memberships"
PLAN = Path(PREFIX + "-plan.json")
SCOPE = "CARD_REFERENCE_INDEX_WITH_COMPLETE_BETA_TUBULIN_COHORT_NOT_EXPERIMENTAL_GROUNDING"
REVIEWED = "REVIEWED_BETA_TUBULIN_PROTEIN_NAME_REFERENCE_ONLY"
UNREVIEWED = "UNREVIEWED_BETA_TUBULIN_PROTEIN_NAME_CANDIDATE_ONLY"
UNSELECTED = "NO_PROTEIN_CANDIDATE_IN_THE_NINE_SELECTED_COHORTS"
COLUMNS = {
    **{k: v for k, v in prior.COLUMNS.items() if k != prior.UNSELECTED},
    REVIEWED: "reviewed_beta_tubulin_claims",
    UNREVIEWED: "unreviewed_beta_tubulin_claims",
    UNSELECTED: "unselected_candidate_claims",
}


def named_taxon(row, name):
    source, selected = row["source"], row["selected_taxon"]
    url = urlsplit(source["url"])
    require(
        row["source_name"] == name
        and row["source_name_kind"] == "BINOMIAL"
        and row["status"] == "EXACT_NATIVE_NAME_REFERENCE"
        and row["experimental_subject_assignment"] is False
        and row["unresolved_name_is_biological_absence"] is False
        and row["protein_or_allele_assignment"] is None
        and source["status"] == 200
        and source["release"] == "2026_03"
        and url.scheme == "https"
        and url.netloc == "rest.uniprot.org"
        and url.path.startswith("/taxonomy/")
        and not url.fragment,
        "native source-name context changed",
    )
    positives = [c for c in row["candidates"] if c["active"] is True and c["matching_fields"]]
    require(
        selected
        and len(positives) == row["exact_match_count"] == 1
        and len({c["taxon_id"] for c in row["candidates"]}) == len(row["candidates"])
        and all(selected[k] == v for k, v in positives[0].items())
        and selected["rank"] == "species"
        and selected["accepted_name_and_rank"] is True
        and selected["experimental_subject_assignment"] is selected["other_name_match_only"] is False
        and set(selected["matching_fields"]) <= {"scientificName", "synonyms"},
        "named species selection changed",
    )
    nodes = selected["lineage"]
    require(
        nodes
        and len({n["taxonId"] for n in nodes}) == len(nodes)
        and all(beta.lineages.identity(n) == n for n in nodes)
        and nodes[-1] == selected["species_ancestor"]
        and [n for n in nodes if n["rank"] == "species"] == [nodes[-1]]
        and selected["taxon_id"] == f"NCBITaxon:{nodes[-1]['taxonId']}"
        and selected["scientific_name"] == nodes[-1]["scientificName"]
        and any(n["taxonId"] == 4751 and n["rank"] == "kingdom" for n in nodes),
        "named fungal lineage changed",
    )
    return selected


def check_query(query, taxid, reviewed):
    all_hits, candidates = query["all_result_accessions"], query["candidate_accessions"]
    exclusions = query["excluded_candidates"]
    excluded = [r["protein_accession"].removeprefix("UniProtKB:") for r in exclusions]
    require(
        query["source"]["url"] == beta.query_url(taxid, reviewed)
        and query["source"]["status"] == 200
        and query["source"]["release"] == "2026_03"
        and type(query["source_taxon_id"]) is int
        and query["source_taxon_id"] == taxid
        and query["reviewed_subset"] is reviewed
        and query["query_type"] == "PROTEIN_NAME_NOT_GENE_SYMBOL"
        and query["complete_for_query"] is True
        and query["zero_hit_is_biological_absence"] is query["suggestions_followed"] is False
        and type(query["result_count"]) is type(query["candidate_count"]) is int
        and query["result_count"] == len(all_hits) == len(set(all_hits))
        and query["candidate_count"] == len(candidates) == len(set(candidates))
        and len(excluded) == len(set(excluded))
        and not set(excluded) & set(candidates)
        and sorted(all_hits) == sorted(candidates + excluded),
        "protein-name query scope or complete hit accounting changed",
    )
    for row in exclusions:
        require(
            row["reason"] == "NO_TOP_LEVEL_NATIVE_BETA_TUBULIN_NAME_NOT_BIOLOGICAL_ABSENCE"
            and row["native_protein_names"]
            and all(not beta.BETA_NAME.fullmatch(n["value"]) for n in row["native_protein_names"]),
            "excluded hit has an eligible native beta name",
        )


def selected_query(term, selected):
    queries = term["queries"]
    taxid = int(selected["taxon_id"].split(":")[1])
    require(set(queries) in ({"reviewed"}, {"reviewed", "unreviewed"}), "reviewed-first policy changed")
    check_query(queries["reviewed"], taxid, True)
    reviewed = bool(queries["reviewed"]["candidate_accessions"])
    require(("unreviewed" in queries) is (not reviewed), "fallback lacks eligible reviewed zero")
    kind = "reviewed" if reviewed else "unreviewed"
    if not reviewed:
        check_query(queries[kind], taxid, False)
    accessions = [c["protein_accession"] for c in term["reference_candidates"]]
    require(
        sorted(accessions) == sorted("UniProtKB:" + a for a in queries[kind]["candidate_accessions"]),
        "complete candidate coverage changed",
    )
    status = (
        "NO_NATIVE_BETA_NAME_CANDIDATES_NOT_ABSENCE"
        if not accessions
        else "MULTIPLE_CANDIDATES_NO_SELECTION"
        if len(accessions) > 1
        else "REVIEWED_REFERENCE"
        if reviewed
        else "UNREVIEWED_CANDIDATE"
    )
    require(term["reference_status"] == status, "candidate disposition changed")
    return kind


def protein_identity(accession, protein, candidate, selected, reviewed):
    matches = [n for n in protein["native_protein_names"] if beta.BETA_NAME.fullmatch(n["value"])]
    require(
        protein["protein_accession"] == accession
        and protein["entry_type"]
        == ("UniProtKB reviewed (Swiss-Prot)" if reviewed else "UniProtKB unreviewed (TrEMBL)")
        and protein["reference_species_taxon_id"] == selected["taxon_id"]
        and protein["species_lineage_verified"] is True
        and protein["exact_resistance_allele"] is protein["experimental_subject_assignment"] is False
        and protein["experimental_genome_assignment"] is protein["source_gene_symbol_assignment"] is None
        and protein["database_review_status_is_primary_results_review"] is False
        and protein["resistance_inferred_from_reference"] is False
        and protein["native_protein_flag"] in (None, "Fragment")
        and protein["unflagged_means_complete"] is False
        and candidate["experimental_subject_assignment"] is candidate["exact_resistant_allele"] is False
        and matches
        and matches == protein["native_beta_name_matches"] == candidate["native_beta_name_matches"],
        "native beta reference identity or evidence scope changed",
    )
    for block in protein["native_gene_annotations"]:
        require(
            set(block) == {"geneName", "synonyms", "orderedLocusNames", "orfNames"}, "gene fields changed"
        )
        require(
            all(
                isinstance(values, list) and all(isinstance(v, str) and v.strip() for v in values)
                for values in block.values()
            ),
            "invalid native gene annotations",
        )
    return registry.reference_identity({**protein, "exact_allele_assignment": False})


def check_bibliography(data, plan):
    dossier, followup = data["beta"], data["bibliography"]
    require(
        followup["scope"] == evidence.SCOPE
        and followup["inputs"]["prior"] == plan["inputs"]["beta"]
        and followup["inputs"]["prior_verification"] == plan["inputs"]["beta_verification"]
        and followup["records"] == dossier["records"]
        and followup["claims"] == dossier["claims"]
        and set(followup["proteins"]) == set(dossier["proteins"]),
        "bibliography provenance or full cohort changed",
    )
    sources = {}
    for term in dossier["terms"].values():
        selected = term["queries"].get("unreviewed", term["queries"]["reviewed"])
        for candidate in term["reference_candidates"]:
            accession = candidate["protein_accession"]
            require(sources.setdefault(accession, selected["source"]) == selected["source"], "query conflict")
    entries = {}
    for accession, row in followup["proteins"].items():
        require(row["source"] == sources[accession], "bibliography query source changed")
        references = []
        for item in row["reference_rows"]:
            references.append(
                {
                    "referenceNumber": item["native_reference_number"],
                    "citation": {
                        "id": item["native_citation_id"],
                        "citationType": item["citation_type"],
                        "title": item["title"],
                        "publicationDate": item["publication_date"],
                        "submissionDatabase": item["submission_database"],
                        "citationCrossReferences": item["identifiers"],
                    },
                    "referenceComments": [
                        {"type": "STRAIN", "value": value} for value in item["reference_strain_comments"]
                    ],
                }
            )
        entries[accession] = (
            {
                "primaryAccession": accession.removeprefix("UniProtKB:"),
                "entryAudit": {
                    "entryVersion": row["entry_version"],
                    "sequenceVersion": row["sequence_version"],
                },
                "entryType": dossier["proteins"][accession]["entry_type"],
                "organism": {"taxonId": int(row["reference_taxon_id"].split(":")[1])},
                "references": references,
            },
            row["source"],
        )
    proteins, terms = evidence.project_bibliographies(entries, dossier)
    require(
        proteins == followup["proteins"] and terms == followup["terms"], "bibliography projection changed"
    )
    references = [row for protein in proteins.values() for row in protein["reference_rows"]]
    summary = {
        "corpus_records_hash_checked": len(data["census"]),
        "complete_records_read": len(dossier["records"]),
        "source_terms": len(terms),
        "source_claims": len(dossier["claims"]),
        "reference_proteins": len(proteins),
        "native_reference_memberships": len(references),
        "reference_types": dict(sorted(Counter(row["citation_type"] for row in references).items())),
        "references_without_identifiers": sum(not row["identifiers"] for row in references),
        "journal_references_without_identifiers": sum(
            not row["identifiers"] and row["citation_type"] == "journal article" for row in references
        ),
        "native_identifier_issues": sum(len(row["identifier_issues"]) for row in references),
        "terms_with_own_source_citation_matches": sum(
            bool(term["own_citation_matches_in_reference_bibliographies"]) for term in terms.values()
        ),
        "primary_access_terms": 2,
        "new_network_requests": 2,
        "new_primary_access_holds": 1,
        "new_primary_result_reviews": 0,
        "whole_record_primary_signoffs": 0,
    }
    require(followup["summary"] == summary, "bibliography summary does not match its memberships")
    banno = followup["banno_followup"]
    hold = banno["access_hold"]
    query = banno["prior_uniprot_citation_query"]
    require(
        set(banno["terms"]) == evidence.TERMS
        and banno["claims"] == [c for c in dossier["claims"] if c["aro_id"] in evidence.TERMS]
        and all(
            dossier["terms"][tid]["definition_citation_ids"] == ["PMID:" + evidence.PMID]
            for tid in evidence.TERMS
        )
        and banno["reference_protein"] == "UniProtKB:P53373"
        and banno["reference_taxon_id"] == "NCBITaxon:40559"
        and banno["source_claims_corrected"] is False
        and banno["exact_allele_assignment"] is None
        and banno["primary_review_status"] == "OPEN"
        and banno["metadata"]["pmid"] == evidence.PMID
        and banno["metadata"]["doi"].lower() == evidence.DOI
        and query["result_count"] == 0
        and query["suggestions_followed"] is query["zero_result_is_biological_absence"] is False
        and query["paper_invalidated_by_zero_result"] is False
        and "lit_pubmed%3A18944187" in query["source"]["url"]
        and hold["reference"] == "PMID:" + evidence.PMID
        and hold["doi"] == evidence.DOI
        and hold["url"] == evidence.ARTICLE
        and hold["http_status"] == 403
        and hold["status"] == "PUBLISHER_403_CHALLENGE_HELD_NO_RETRY"
        and all(
            hold[k] is False
            for k in (
                "article_obtained",
                "primary_results_reviewed",
                "retry_or_alternate_route_performed",
                "negative_biological_evidence",
                "global_inaccessibility_inferred",
                "paywall_inferred",
            )
        )
        and followup["constraints"]["full_corpus_goal_status"] == "OPEN",
        "access hold or unresolved experimental scope changed",
    )


def reconcile_rows(data, terms, claims):
    base, census = data["base"], progress.index_unique(data["census"], "identifier", "census record")
    old_rows = progress.index_unique(data["base_rows"], "identifier", "base row")
    require(set(old_rows) == set(census), "all-record row coverage changed")
    old_by_record, by_record = defaultdict(list), defaultdict(list)
    for old, claim in zip(base["claims"], claims, strict=True):
        require({**claim, "reference_status": old["reference_status"]} == old, "claim identity changed")
        require(
            old["reference_status"] == base["terms"][old["aro_id"]]["reference_status"], "claim status drift"
        )
        old_by_record[old["record_identifier"]].append(old)
        by_record[claim["record_identifier"]].append(claim)
    require(set(by_record) <= set(census), "claim lies outside the census")
    rows = []
    for identifier, record in sorted(census.items()):
        old, subset = old_rows[identifier], by_record[identifier]
        old_status = Counter(c["reference_status"] for c in old_by_record[identifier])
        counts = Counter(c["reference_status"] for c in subset)
        old_accessions = {
            link["protein_accession"] for c in subset for link in base["terms"][c["aro_id"]]["links"]
        }
        require(
            all(old[k] == record[k] for k in ("path", "record_sha256", "standard_inchi_key"))
            and int(old["card_assertions"]) == len(subset)
            and all(int(old[column]) == old_status[kind] for kind, column in prior.COLUMNS.items())
            and old["selected_reference_accessions"] == "|".join(sorted(old_accessions))
            and old["whole_record_primary_review"] == "OPEN",
            "base record identity, reference counts or review status changed",
        )
        accessions = {link["protein_accession"] for c in subset for link in terms[c["aro_id"]]["links"]}
        row = {
            **{k: old[k] for k in ("identifier", "path", "record_sha256", "standard_inchi_key")},
            "card_assertions": len(subset),
            **{column: counts[kind] for kind, column in COLUMNS.items()},
            "selected_reference_accessions": "|".join(sorted(accessions)),
            **{
                k: int(old[k])
                for k in (
                    "phi_claims_not_reassessed",
                    "curator_claims_not_reassessed",
                    "score_rules_not_reassessed",
                )
            },
            "whole_record_primary_review": "OPEN",
        }
        require(
            row["card_assertions"] + row["phi_claims_not_reassessed"] + row["curator_claims_not_reassessed"]
            == int(record["resistance_assertions"])
            and row["score_rules_not_reassessed"] == int(record["score_rules"]),
            "source-owned accounting changed",
        )
        rows.append(row)
    return rows


def project(data, plan, plan_pin):
    base, dossier, inputs = data["base"], data["beta"], plan["inputs"]
    require(
        base["limits"]
        == {
            "biological_record_changes": 0,
            "experimental_allele_or_genome_assignments": 0,
            "full_corpus_goal_status": "OPEN",
            "github_mutations": 0,
            "issue_1040": "DEFERRED",
            "ncbi_requests": 0,
            "network_requests": 0,
            "outreach": 0,
            "reuse_terms_review_resumed": False,
            "source_adoptions": 0,
        },
        "prior index scope or deferred-source limits changed",
    )
    require(
        not set(dossier["proteins"]) & set(base["proteins"]),
        "unreviewed overlap with prior reference proteins",
    )
    require(
        plan["selection"] == "ALL_CARD_MEMBERSHIPS_WITH_COMPLETE_BETA_TUBULIN_COHORT"
        and plan["constraints"]
        == {
            "network_requests": 0,
            "biological_writes": False,
            "experimental_assignments": False,
            "issue_1040": "DEFERRED",
        }
        and base["scope"] == prior.SCOPE
        and base["plan"] == inputs["base_plan"]
        and data["base_plan"]["inputs"] == base["inputs"]
        and dossier["scope"] == beta.SCOPE
        and dossier["release"] == "2026_03"
        and dossier["inputs"]["index"] == inputs["base"]
        and dossier["inputs"]["prior_verification"] == inputs["base_verification"],
        "successor index or reference provenance changed",
    )
    for name in ("base", "beta", "bibliography"):
        prior.prior.check_checkpoint(data, plan, name)
        for key in ("census", "source_queue", "source_inventory", "definition_citations"):
            require(data[name]["inputs"][key] == inputs[key], "checkpoint source pin changed")
    source = data["direct_candidates"]
    labels = {tid: row["labels"][0] for tid, row in source["determinants"].items()}
    require(
        source["source_inventory_sha256"] == inputs["source_inventory"]["sha256"]
        and set(labels) == set(base["terms"])
        and all(len(r["labels"]) == 1 for r in source["determinants"].values())
        and all(
            t["source_label_sha256"] == progress.digest(labels[tid].encode())
            for tid, t in base["terms"].items()
        ),
        "source labels or full term coverage changed",
    )
    expected = {tid for tid, label in labels.items() if beta.SELECT.search(label)}
    require(set(dossier["terms"]) == expected, "complete beta-tubulin term coverage changed")
    expected_claims = [
        {
            "record_identifier": c["record_identifier"],
            "position": c["resistance_index"],
            "aro_id": c["aro_id"],
            "claim_sha256": c["claim_sha256"],
        }
        for c in base["claims"]
        if c["aro_id"] in expected
    ]
    require(
        Counter(map(registry.checksum, expected_claims))
        == Counter(map(registry.checksum, dossier["claims"])),
        "beta claim positions or content changed",
    )
    census = progress.index_unique(data["census"], "identifier", "census record")
    ids = {c["record_identifier"] for c in expected_claims}
    require(
        len(dossier["records"]) == len(ids)
        and {r["identifier"] for r in dossier["records"]} == ids
        and all(r == census[r["identifier"]] for r in dossier["records"]),
        "complete beta record scope changed",
    )
    require(
        set(dossier["names"]) == {t["taxonomy_query_name"] for t in dossier["terms"].values()},
        "source-name coverage changed",
    )
    names = {name: named_taxon(row, name) for name, row in dossier["names"].items()}
    check_bibliography(data, plan)
    result = rebase(base)
    terms, proteins = result["terms"], result["proteins"]
    for protein in proteins.values():
        registry.reference_identity(
            {
                **protein["identity"],
                **{k: protein[k] for k in ("experimental_subject_assignment", "exact_allele_assignment")},
            }
        )
    for term in terms.values():
        require(
            term["experimental_subject_assignment"] is False
            and term["whole_record_primary_review"] == "OPEN"
            and term["reference_status"] in prior.COLUMNS
            and all(
                link["kind"] == term["reference_status"] and link["protein_accession"] in proteins
                for link in term["links"]
            ),
            "base link or primary scope changed",
        )
        require(
            bool(term["links"]) is (term["reference_status"] != prior.UNSELECTED), "base disposition drift"
        )
        if term["reference_status"] == prior.UNSELECTED:
            term["reference_status"] = UNSELECTED
    used, contexts = set(), {}
    for tid, term in dossier["terms"].items():
        old, label = base["terms"][tid], labels[tid]
        require(
            all(term[k] == v for k, v in beta.source_identity(label).items())
            and term["source_label"] == label
            and term["source_label_sha256"] == old["source_label_sha256"]
            and term["record_memberships"] == old["record_memberships"]
            and term["definition_citation_ids"]
            == data["definition_citations"]["terms"][tid]["definition_citation_ids"]
            and not old["links"]
            and old["reference_status"] == prior.UNSELECTED
            and term["experimental_subject_assignment"] is term["exact_allele_assignment"] is False
            and term["experimental_genome_assignment"] is None
            and term["primary_review_status"] == "OPEN",
            "beta source identity or unresolved evidence scope changed",
        )
        name = term["taxonomy_query_name"]
        selected = names[name]
        require(
            term["named_reference_taxon_id"] == selected["taxon_id"]
            and term["named_reference_taxon_rank"] == selected["rank"],
            "term taxon changed",
        )
        kind = selected_query(term, selected)
        content = {k: term[k] for k in ("queries", "reference_candidates", "reference_status")}
        require(contexts.setdefault(name, content) == content, "shared source-name query conflict")
        target = terms[tid]
        target.update(
            {
                "beta_followup": pointer("beta", "terms", tid),
                "beta_bibliography_followup": pointer("bibliography", "terms", tid),
                "beta_query_disposition": term["reference_status"],
                "named_organism_taxon_reference_only": selected["taxon_id"],
                "named_taxon_rank_reference_only": selected["rank"],
                "species_ancestor_reference_only": selected["species_ancestor"],
                "beta_name_context": pointer("beta", "names", name),
                "source_gene_symbol_assignment": None,
            }
        )
        for index, candidate in enumerate(term["reference_candidates"]):
            accession = candidate["protein_accession"]
            protein = dossier["proteins"][accession]
            identity = protein_identity(accession, protein, candidate, selected, kind == "reviewed")
            item = proteins.setdefault(
                accession,
                {
                    "identity": identity,
                    "sources": [],
                    "experimental_subject_assignment": False,
                    "exact_allele_assignment": False,
                },
            )
            require(item["identity"] == identity, "cross-cohort protein identity conflict")
            provenance = pointer("beta", "proteins", accession)
            if provenance not in item["sources"]:
                item["sources"].append(provenance)
            item.update(
                {
                    "protein_description_flag": protein["native_protein_flag"],
                    "unflagged_means_complete": False,
                    "native_gene_annotations": copy.deepcopy(protein["native_gene_annotations"]),
                    "native_protein_names": copy.deepcopy(protein["native_protein_names"]),
                    "source_gene_symbol_assignment": None,
                    "beta_bibliography": pointer("bibliography", "proteins", accession),
                }
            )
            status = REVIEWED if kind == "reviewed" else UNREVIEWED
            target["links"].append(
                {
                    "protein_accession": accession,
                    "kind": status,
                    "explicit_card_xref": False,
                    "source_citation_ids": [],
                    "matched_reference_numbers": [],
                    "source": pointer("beta", "terms", tid, "reference_candidates", index),
                    "query": pointer("beta", "terms", tid, "queries", kind),
                    "experimental_subject_assignment": False,
                    "exact_allele_assignment": False,
                }
            )
            target["reference_status"] = status
            used.add(accession)
    require(used == set(dossier["proteins"]), "unbound beta reference protein")
    claims = result["claims"]
    for claim in claims:
        claim["reference_status"] = terms[claim["aro_id"]]["reference_status"]
    rows = reconcile_rows(data, terms, claims)
    result.update(
        {
            "date": plan["date"],
            "scope": SCOPE,
            "plan": plan_pin,
            "inputs": inputs,
            "terms": dict(sorted(terms.items())),
            "proteins": dict(sorted(proteins.items())),
            "summary": {
                **base["summary"],
                "corpus_records": len(rows),
                "card_terms": len(terms),
                "card_assertions": len(claims),
                "selected_reference_proteins": len(proteins),
                "selected_reference_terms": sum(bool(t["links"]) for t in terms.values()),
                "reference_links": sum(len(t["links"]) for t in terms.values()),
                "term_statuses": dict(sorted(Counter(t["reference_status"] for t in terms.values()).items())),
                "claim_statuses": dict(sorted(Counter(c["reference_status"] for c in claims).items())),
                "records_with_selected_references": sum(
                    bool(r["selected_reference_accessions"]) for r in rows
                ),
                "added_reference_terms": sum(bool(terms[t]["links"]) for t in expected),
                "added_reference_proteins": len(set(proteins) - set(base["proteins"])),
                "added_reference_links": sum(len(terms[t]["links"]) for t in expected),
                "beta_source_terms": len(expected),
                "beta_source_claims": len(expected_claims),
                "beta_followup_dispositions": dict(
                    sorted(Counter(t["reference_status"] for t in dossier["terms"].values()).items())
                ),
                "beta_bibliography_summary": copy.deepcopy(data["bibliography"]["summary"]),
                "unreviewed_fragment_references": sum(
                    p.get("protein_description_flag") == "Fragment"
                    and p["identity"]["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
                    for p in proteins.values()
                ),
            },
            "beta_primary_access_hold": pointer("bibliography", "banno_followup", "access_hold"),
            "prior_interpretation": pointer("base", "interpretation"),
            "interpretation": [
                "One complete protein-name cohort extends the eight-cohort index; "
                "other dossiers remain separate.",
                "Native gene annotations are retained but no source gene symbol "
                "or exact paralog is assigned.",
                "All candidates, fragments, exclusions and native name contexts "
                "remain explicit references only.",
                "Reference strains, journal leads, citation gaps and malformed identifiers "
                "do not establish tested subjects.",
                "The publisher challenge remains held; reference grounding does not finish primary review.",
                "All PHI, curator and interpretation-rule memberships remain unchanged and in scope.",
            ],
            "attribution": {name: data[name]["attribution"] for name in ("base", "beta", "bibliography")},
        }
    )
    return result, rows


def build(root, plan_path=PLAN):
    data, plan, pin = prior.prior.read_inputs(root, plan_path)
    baseline, baseline_rows = prior.build(root, Path(plan["inputs"]["base_plan"]["path"]))
    require(
        baseline == data["base"]
        and registry.render(baseline, baseline_rows)[1]
        == reference.check_pin(root, plan["inputs"]["base_rows"]).read_bytes(),
        "prior all-record index does not reproduce",
    )
    result, rows = project(data, plan, pin)
    records, _ = progress.current_records(root, data["census"])
    progress.card_progress(records, data["direct_candidates"], data["ledger"])
    live.check_live_claims(records, result, rows)
    return result, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result, rows = build(Path.cwd())
    outputs = [
        (Path(PREFIX + suffix), payload)
        for suffix, payload in zip((".json", ".tsv"), registry.render(result, rows), strict=True)
    ]
    missing = []
    for path, payload in outputs:
        if args.check or path.exists():
            require(path.read_bytes() == payload, "beta-tubulin index does not reproduce")
        else:
            missing.append((path, payload))
    if not args.check:
        for path, payload in missing:
            with path.open("xb") as stream:
                stream.write(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
