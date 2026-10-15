"""Reconcile complete folP and RNA-polymerase references with every CARD claim."""

import argparse
import copy
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit

import audit_card_folp_references as folp
import audit_card_fungal_memberships as prior
import audit_card_rpo_references as rpo

progress, reference = prior.progress, prior.reference
require, pointer, rebase = prior.require, prior.pointer, prior.rebase
PREFIX = "research/2026-10-14-card-folp-rpo-memberships"
PLAN = Path(PREFIX + "-plan.json")
SCOPE = "CARD_REFERENCE_INDEX_WITH_COMPLETE_FOLP_AND_RPO_COHORTS_NOT_EXPERIMENTAL_GROUNDING"
REVIEWED = "REVIEWED_FOLP_RPO_GENE_AND_TAXON_REFERENCE_ONLY"
UNREVIEWED = "UNREVIEWED_FOLP_RPO_GENE_AND_TAXON_CANDIDATE_ONLY"
UNSELECTED = "NO_PROTEIN_CANDIDATE_IN_THE_EIGHT_SELECTED_COHORTS"
COLUMNS = {
    **{k: v for k, v in prior.COLUMNS.items() if k != prior.UNSELECTED},
    REVIEWED: "reviewed_folp_rpo_claims",
    UNREVIEWED: "unreviewed_folp_rpo_claims",
    UNSELECTED: "unselected_candidate_claims",
}
COHORTS = {"folp": folp, "rpo": rpo}


def source_identity(cohort, tid, label, dossier, citations):
    if cohort == "folp":
        match = re.fullmatch(r"([A-Z][a-z]+ [a-z]+) (folP) (.+)", label)
        require(match, "invalid folP source label")
        return {
            "source_organism_name": match[1],
            "source_gene_label": match[2],
            "source_claim_wording": match[3],
        }
    match = re.match(r"([A-Z][a-z]+ [a-z]+) (rpo[BC])\b", label)
    genes = re.findall(r"\brpo[BC]\b", label)
    require(len(genes) == 1, "ambiguous rpo source gene")
    name, basis = (match[1], "SOURCE_LABEL") if match else (None, "UNRESOLVED_NO_NAME")
    if tid == "ARO:3003090":
        paper = dossier["bibliographic_identity_context"]["20837752"]
        require(
            paper["pmid"] == "20837752"
            and paper["source"] == "MED"
            and "Staphylococcus aureus" in paper["title"]
            and citations[tid]["definition_citation_ids"] == ["PMID:20837752"],
            "verified abbreviation context changed",
        )
        name, basis = "Staphylococcus aureus", "DEFINITION_ABBREVIATION_AND_CITED_TITLE"
    return {"source_organism_name": name, "source_gene_label": genes[0], "name_evidence": basis}


def named_taxon(row, name):
    url = urlsplit(row["source"]["url"])
    require(
        row["source_name"] == name
        and row["experimental_subject_assignment"] is False
        and row["unresolved_name_is_absence"] is False
        and row["source"]["status"] == 200
        and row["source"]["release"] == "2026_03",
        "source-name evidence scope changed",
    )
    require(
        url.scheme == "https"
        and url.netloc == "rest.uniprot.org"
        and url.path.startswith("/taxonomy/")
        and not url.fragment
        and len({c["taxon_id"] for c in row["candidates"]}) == len(row["candidates"]),
        "native taxonomy provenance or candidate identity changed",
    )
    selected = row["selected_taxon"]
    positives = [c for c in row["candidates"] if c["active"] is True and c["matching_fields"]]
    if selected is None:
        require(
            len(positives) != 1 and row["status"] in ("AMBIGUOUS_NATIVE_NAME", "NO_EXACT_ACTIVE_NATIVE_NAME"),
            "unresolved name disposition changed",
        )
        return None
    require(
        len(positives) == 1
        and all(selected[k] == v for k, v in positives[0].items())
        and selected["active"] is True
        and selected["experimental_subject_assignment"] is False
        and selected["other_name_match_only"] is False
        and set(selected["matching_fields"]) <= {"scientificName", "synonyms"}
        and row["status"] == "EXACT_NATIVE_NAME_REFERENCE",
        "selected native name identity changed",
    )
    nodes = selected["lineage"]
    require(nodes and len({n["taxonId"] for n in nodes}) == len(nodes), "invalid named lineage")
    require(
        all(folp.lineages.identity(n) == n for n in nodes)
        and selected["taxon_id"] == f"NCBITaxon:{nodes[-1]['taxonId']}"
        and selected["rank"] == nodes[-1]["rank"]
        and selected["scientific_name"] == nodes[-1]["scientificName"]
        and [n for n in nodes if n["rank"] == "species"] == [selected["species_ancestor"]]
        and any(n["taxonId"] == 2 for n in nodes),
        "named rank or species ancestry changed",
    )
    return selected


def check_query(query, gene, taxid, reviewed, module):
    url = module.gene_url(taxid, reviewed) if module is folp else module.gene_url(taxid, gene, reviewed)
    accessions = query["accessions"]
    require(
        query["source"]["url"] == url
        and query["source"]["status"] == 200
        and query["source"]["release"] == "2026_03"
        and query["gene"] == gene
        and type(query["source_taxon_id"]) is int
        and query["source_taxon_id"] == taxid
        and query["reviewed_subset"] is reviewed
        and query["complete_for_query"] is True
        and query["zero_hit_is_biological_absence"] is False
        and query["suggestions_followed"] is False
        and type(query["result_count"]) is int
        and query["result_count"] == len(accessions) == len(set(accessions))
        and all(isinstance(a, str) and a and not a.startswith("UniProtKB:") for a in accessions),
        "gene query identity, completeness or scope changed",
    )


def selected_query(term, selected, module):
    queries, candidates = term["queries"], term["reference_candidates"]
    if selected is None:
        require(
            not queries and not candidates and term["reference_status"] == prior.UNRESOLVED,
            "unresolved name acquired a query or protein",
        )
        return None
    taxid, gene = int(selected["taxon_id"].split(":")[1]), term["source_gene_label"]
    require(set(queries) in ({"reviewed"}, {"reviewed", "unreviewed"}), "reviewed-first policy changed")
    check_query(queries["reviewed"], gene, taxid, True, module)
    reviewed = bool(queries["reviewed"]["accessions"])
    require(("unreviewed" in queries) is (not reviewed), "fallback lacks complete reviewed zero")
    kind = "reviewed" if reviewed else "unreviewed"
    if not reviewed:
        check_query(queries[kind], gene, taxid, False, module)
    require(
        sorted(c["protein_accession"] for c in candidates)
        == sorted("UniProtKB:" + a for a in queries[kind]["accessions"]),
        "query candidate coverage changed",
    )
    status = (
        prior.ZERO
        if not candidates
        else "MULTIPLE_CANDIDATES_NO_SELECTION"
        if len(candidates) > 1
        else "REVIEWED_REFERENCE"
        if reviewed
        else "UNREVIEWED_CANDIDATE"
    )
    require(term["reference_status"] == status, "query disposition changed")
    return kind


def reconcile_cohort(name, data, labels, terms, proteins):
    dossier, base, module = data[name], data["base"], COHORTS[name]
    require(dossier["scope"] == module.SCOPE and dossier["release"] == "2026_03", "dossier scope changed")
    expected = {tid for tid in base["terms"] if module.SELECT.search(labels[tid])}
    require(set(dossier["terms"]) == expected, "complete source cohort coverage changed")
    claims = [
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
        Counter(map(prior.prior.prior.checksum, claims))
        == Counter(map(prior.prior.prior.checksum, dossier["claims"])),
        "dossier claim positions or hashes changed",
    )
    record_ids = {c["record_identifier"] for c in claims}
    census = progress.index_unique(data["census"], "identifier", "census record")
    require(
        len(dossier["records"]) == len(record_ids)
        and {r["identifier"] for r in dossier["records"]} == record_ids
        and all(r == census[r["identifier"]] for r in dossier["records"]),
        "dossier record identities changed",
    )
    require(
        set(dossier["names"]) == {t["source_organism_name"] for t in dossier["terms"].values()} - {None},
        "source-name coverage changed",
    )
    names = {n: named_taxon(row, n) for n, row in dossier["names"].items()}
    used_proteins, shared_contexts = set(), {}
    citations = data["definition_citations"]["terms"]
    for tid, term in dossier["terms"].items():
        original = base["terms"][tid]
        identity = source_identity(name, tid, labels[tid], dossier, citations)
        require(
            not original["links"]
            and original["reference_status"] == prior.UNSELECTED
            and all(term[k] == v for k, v in identity.items())
            and term["source_label"] == labels[tid]
            and term["source_label_sha256"]
            == original["source_label_sha256"]
            == progress.digest(labels[tid].encode())
            and term["record_memberships"] == original["record_memberships"]
            and term["definition_citation_ids"] == citations[tid]["definition_citation_ids"]
            and term["experimental_subject_assignment"] is term["exact_allele_assignment"] is False
            and term["experimental_genome_assignment"] is None
            and term["primary_review_status"] == "OPEN",
            "term identity, citation membership or evidence scope changed",
        )
        source_name, gene = term["source_organism_name"], term["source_gene_label"]
        selected = names[source_name] if source_name else None
        taxid = selected["taxon_id"] if selected else None
        rank = selected["rank"] if selected else None
        species = selected["species_ancestor"] if selected else None
        require(
            term["named_reference_taxon_id"] == taxid
            and term["named_reference_taxon_rank"] == rank
            and term["source_species_ancestor"] == species,
            "term taxon or rank differs from name context",
        )
        kind = selected_query(term, selected, module)
        if source_name:
            context = (source_name, gene)
            query_content = {k: term[k] for k in ("queries", "reference_candidates", "reference_status")}
            require(
                shared_contexts.setdefault(context, query_content) == query_content,
                "shared gene/name query differs between terms",
            )
        target = terms[tid]
        target.update(
            {
                "folp_rpo_cohort": name,
                "folp_rpo_followup": pointer(name, "terms", tid),
                "folp_rpo_query_disposition": term["reference_status"],
                "named_organism_taxon_reference_only": taxid,
                "named_taxon_rank_reference_only": rank,
                "species_ancestor_reference_only": species,
                "folp_rpo_name_context": pointer(name, "names", source_name) if source_name else None,
            }
        )
        for index, candidate in enumerate(term["reference_candidates"]):
            accession = candidate["protein_accession"]
            protein = dossier["proteins"][accession]
            protein_identity = prior.protein_identity(
                accession, protein, candidate, gene.casefold(), species["taxonId"], kind == "reviewed"
            )
            item = proteins.setdefault(
                accession,
                {
                    "identity": protein_identity,
                    "sources": [],
                    "experimental_subject_assignment": False,
                    "exact_allele_assignment": False,
                },
            )
            require(item["identity"] == protein_identity, "conflicting cross-cohort protein identity")
            provenance = pointer(name, "proteins", accession)
            if provenance not in item["sources"]:
                item["sources"].append(provenance)
            require(
                item.get("protein_description_flag", protein["native_protein_flag"])
                == protein["native_protein_flag"],
                "conflicting fragment metadata",
            )
            item["protein_description_flag"] = protein["native_protein_flag"]
            item["unflagged_means_complete"] = False
            if "native_included_protein_names" in protein:
                included = protein["native_included_protein_names"]
                require(
                    item.get("native_included_protein_names", included) == included,
                    "conflicting fusion metadata",
                )
                item["native_included_protein_names"] = copy.deepcopy(included)
            status = REVIEWED if kind == "reviewed" else UNREVIEWED
            target["links"].append(
                {
                    "protein_accession": accession,
                    "kind": status,
                    "explicit_card_xref": False,
                    "source_citation_ids": [],
                    "matched_reference_numbers": [],
                    "source": pointer(name, "terms", tid, "reference_candidates", index),
                    "query": pointer(name, "terms", tid, "queries", kind),
                    "experimental_subject_assignment": False,
                    "exact_allele_assignment": False,
                }
            )
            target["reference_status"] = status
            used_proteins.add(accession)
    require(used_proteins == set(dossier["proteins"]), "unbound protein reference")


def retain_primary_access(data, plan, terms):
    access = data["rpo_primary_access"]
    states = access["access_states"]
    require(
        access["scope"] == "RPOC_PRIMARY_ACCESS_AND_UNRESOLVED_CLAIM_SCOPE_NOT_CAUSAL_REVIEW"
        and access["inputs"]["prior"] == plan["inputs"]["rpo"]
        and access["inputs"]["prior_verification"] == plan["inputs"]["rpo_verification"]
        and access["summary"]["new_primary_result_reviews"] == 0
        and access["summary"]["primary_articles_obtained"] == 0
        and set(access["term_contexts"]) == {"ARO:3004994", "ARO:3004995"}
        and access["prior_causal_review_flag"] == data["rpo"]["primary_review_flags"]["ARO:3004994"],
        "primary access context or scope changed",
    )
    require(
        set(states) == {"PMID:23208709", "PMID:30337678"}
        and states["PMID:23208709"]["status"] == "TECHNICAL_HTTP_500_HOLD"
        and states["PMID:23208709"]["negative_biological_evidence"] is False
        and states["PMID:30337678"]["status"] == "UNRESOLVED_PUBLISHER_REDIRECT_FLOW"
        and states["PMID:30337678"]["access_denial_or_paywall_inferred"] is False
        and all(s["primary_results_reviewed"] is s["article_obtained"] is False for s in states.values())
        and access["constraints"]["full_corpus_goal_status"] == "OPEN"
        and access["constraints"]["error_or_redirect_is_negative_biological_evidence"] is False,
        "primary access state promoted to biological evidence",
    )
    expected_claims = [c for c in data["rpo"]["claims"] if c["aro_id"] in access["term_contexts"]]
    require(access["claims"] == expected_claims, "primary-access claim membership changed")
    for tid, context in access["term_contexts"].items():
        term = data["rpo"]["terms"][tid]
        require(
            all(
                context[k] == term[k]
                for k in (
                    "source_label",
                    "definition_citation_ids",
                    "record_memberships",
                    "named_reference_taxon_id",
                )
            )
            and context["reference_protein_candidates"]
            == [c["protein_accession"] for c in term["reference_candidates"]]
            and context["source_claim_corrected"] is context["experimental_subject_assignment"] is False
            and context["exact_resistant_allele"] is context["experimental_genome_assignment"] is None
            and context["primary_review_status"] == "OPEN",
            "access context promoted or differs from reference dossier",
        )
        terms[tid]["primary_access_followup"] = pointer("rpo_primary_access", "term_contexts", tid)


def project(data, plan, plan_pin):
    base, inputs = data["base"], plan["inputs"]
    require(
        plan["selection"] == "ALL_CARD_MEMBERSHIPS_WITH_COMPLETE_FOLP_AND_RPO_COHORTS"
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
        and all(
            base["inputs"][k] == inputs[k]
            for k in ("census", "curator", "direct_candidates", "ledger", "source_inventory", "source_queue")
        ),
        "index plan or checkpoint provenance changed",
    )
    for name in ("base", *COHORTS, "rpo_primary_access"):
        prior.check_checkpoint(data, plan, name)
    for name in COHORTS:
        require(
            data[name]["inputs"]["index"] == inputs["base"]
            and all(
                data[name]["inputs"][k] == inputs[k]
                for k in ("census", "source_inventory", "definition_citations")
            ),
            "gene-cohort provenance changed",
        )
    require(not set(data["folp"]["terms"]) & set(data["rpo"]["terms"]), "overlapping source cohorts")
    source = data["direct_candidates"]
    require(
        source["source_inventory_sha256"] == inputs["source_inventory"]["sha256"]
        and set(source["determinants"]) == set(base["terms"])
        and all(len(r["labels"]) == 1 for r in source["determinants"].values()),
        "frozen source labels or provenance changed",
    )
    labels = {tid: row["labels"][0] for tid, row in source["determinants"].items()}
    require(
        all(
            t["source_label_sha256"] == progress.digest(labels[tid].encode())
            for tid, t in base["terms"].items()
        ),
        "base source label hash changed",
    )
    terms, proteins = rebase(base["terms"], "terms"), rebase(base["proteins"], "proteins")
    for protein in proteins.values():
        prior.prior.prior.reference_identity(
            {
                **protein["identity"],
                **{k: protein[k] for k in ("experimental_subject_assignment", "exact_allele_assignment")},
            }
        )
    for term in terms.values():
        require(
            term["experimental_subject_assignment"] is False
            and term["whole_record_primary_review"] == "OPEN",
            "base primary scope changed",
        )
        require(
            term["reference_status"] in prior.COLUMNS
            and all(
                link["kind"] == term["reference_status"] and link["protein_accession"] in proteins
                for link in term["links"]
            ),
            "base link disposition changed",
        )
        if term["reference_status"] == prior.UNSELECTED:
            require(not term["links"], "unselected base term has a reference")
            term["reference_status"] = UNSELECTED
        else:
            require(bool(term["links"]), "selected base term lacks references")
    for name in COHORTS:
        reconcile_cohort(name, data, labels, terms, proteins)
    retain_primary_access(data, plan, terms)
    claims, by_record, old_by_record, memberships = (
        copy.deepcopy(base["claims"]),
        defaultdict(list),
        defaultdict(list),
        defaultdict(set),
    )
    require(
        Counter((c["record_identifier"], c["aro_id"]) for c in claims)
        == Counter((r["identifier"], r["aro_id"]) for r in data["ledger"]),
        "source ledger memberships changed",
    )
    census = progress.index_unique(data["census"], "identifier", "census record")
    positions = set()
    for claim in claims:
        identifier, tid = claim["record_identifier"], claim["aro_id"]
        row, key = census[identifier], (identifier, claim["resistance_index"])
        require(
            type(claim["resistance_index"]) is int
            and claim["resistance_index"] >= 0
            and key not in positions
            and claim["experimental_subject_assignment"] is False
            and claim["reference_status"] == base["terms"][tid]["reference_status"]
            and all(
                claim[k] == row[r]
                for k, r in (
                    ("record_path", "path"),
                    ("record_sha256", "record_sha256"),
                    ("standard_inchi_key", "standard_inchi_key"),
                )
            ),
            "base claim identity or status changed",
        )
        positions.add(key)
        old_by_record[identifier].append(claim["reference_status"])
        claim["reference_status"] = terms[tid]["reference_status"]
        by_record[identifier].append(claim)
        memberships[tid].add(identifier)
    require(
        set(memberships) == set(terms)
        and all(sorted(memberships[t]) == r["record_memberships"] for t, r in terms.items()),
        "term memberships changed",
    )
    old_rows = progress.index_unique(data["base_rows"], "identifier", "base row")
    require(set(old_rows) == set(census), "all-record row coverage changed")
    curated = Counter(c["record_identifier"] for c in data["curator"]["claims"])
    require(
        data["curator"]["census"] == inputs["census"] and set(curated) <= set(census),
        "curator checkpoint changed",
    )
    rows = []
    for identifier, record in sorted(census.items()):
        old, subset = old_rows[identifier], by_record[identifier]
        statuses, old_statuses = (
            Counter(c["reference_status"] for c in subset),
            Counter(old_by_record[identifier]),
        )
        require(
            all(old[k] == record[k] for k in ("path", "record_sha256", "standard_inchi_key"))
            and int(old["card_assertions"]) == len(subset)
            and all(int(old[column]) == old_statuses[kind] for kind, column in prior.COLUMNS.items())
            and int(old["curator_claims_not_reassessed"]) == curated[identifier]
            and int(old["phi_claims_not_reassessed"])
            == int(record["resistance_assertions"]) - len(subset) - curated[identifier]
            and int(old["phi_claims_not_reassessed"]) >= 0
            and int(old["score_rules_not_reassessed"]) == int(record["score_rules"])
            and old["whole_record_primary_review"] == "OPEN",
            "base row identity, counts or primary scope changed",
        )
        accessions = {link["protein_accession"] for c in subset for link in terms[c["aro_id"]]["links"]}
        old_accessions = {
            link["protein_accession"] for c in subset for link in base["terms"][c["aro_id"]]["links"]
        }
        require(
            old["selected_reference_accessions"] == "|".join(sorted(old_accessions)),
            "base row accessions changed",
        )
        rows.append(
            {
                **{k: old[k] for k in ("identifier", "path", "record_sha256", "standard_inchi_key")},
                "card_assertions": len(subset),
                **{column: statuses[kind] for kind, column in COLUMNS.items()},
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
        )
    selected_terms = set(data["folp"]["terms"]) | set(data["rpo"]["terms"])
    summary = {
        **base["summary"],
        "corpus_records": len(rows),
        "card_terms": len(terms),
        "card_assertions": len(claims),
        "selected_reference_terms": sum(bool(t["links"]) for t in terms.values()),
        "selected_reference_proteins": len(proteins),
        "reference_links": sum(len(t["links"]) for t in terms.values()),
        "term_statuses": dict(sorted(Counter(t["reference_status"] for t in terms.values()).items())),
        "claim_statuses": dict(sorted(Counter(c["reference_status"] for c in claims).items())),
        "records_with_selected_references": sum(bool(r["selected_reference_accessions"]) for r in rows),
        "added_reference_proteins": len(set(proteins) - set(base["proteins"])),
        "added_reference_terms": sum(bool(terms[t]["links"]) for t in selected_terms),
        "added_reference_links": sum(len(terms[t]["links"]) for t in selected_terms),
        "folp_rpo_source_terms": len(selected_terms),
        "folp_rpo_source_claims": sum(c["aro_id"] in selected_terms for c in claims),
        "folp_rpo_followup_dispositions": {
            name: dict(sorted(Counter(t["reference_status"] for t in data[name]["terms"].values()).items()))
            for name in COHORTS
        },
        "unreviewed_fragment_references": sum(
            p.get("protein_description_flag") == "Fragment"
            and p["identity"]["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
            for p in proteins.values()
        ),
    }
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": plan_pin,
        "inputs": inputs,
        "terms": dict(sorted(terms.items())),
        "proteins": dict(sorted(proteins.items())),
        "claims": claims,
        "summary": summary,
        "limits": copy.deepcopy(base["limits"]),
        "interpretation": [
            "Two complete gene cohorts extend the six-cohort index; other dossiers remain separate.",
            "Reference proteins and taxonomic names are not tested alleles, isolates, genomes or phenotypes.",
            "Source names retain their native ranks; no-rank queries are not broadened "
            "to their species ancestors.",
            "Explicit native synonyms, fusion names, fragment flags, all candidates "
            "and empty queries are retained.",
            "The rpo abbreviation bridge remains tied to its own verified source context, "
            "not neighboring terms.",
            "The separate rpoC primary-access follow-up does not adjudicate causality "
            "or complete primary review.",
            "PHI-base, curator claims, HIVDB rules and other inherited review context are unchanged.",
        ],
        **{
            key: pointer("base", key)
            for key in (
                "shared_symbol_reference_context",
                "salmonella_taxonomy_context",
                "salmonella_primary_review",
            )
        },
        "rpo_primary_access_context": pointer("rpo_primary_access", "access_states"),
        "rpo_causal_review_flags": pointer("rpo", "primary_review_flags"),
        "attribution": {k: data[k]["attribution"] for k in ("base", *COHORTS)},
    }, rows


def build(root, plan_path=PLAN):
    data, plan, pin = prior.read_inputs(root, plan_path)
    inventory = progress.read_tsv(reference.check_pin(root, plan["inputs"]["source_inventory"]).read_bytes())
    labels = defaultdict(set)
    for row in inventory:
        labels[row["determinant_id"]].add(row["determinant_name"])
    require(
        all(
            labels[tid] == set(row["labels"])
            for tid, row in data["direct_candidates"]["determinants"].items()
        ),
        "current source labels differ from frozen public evidence",
    )
    result, rows = project(data, plan, pin)
    records, _ = progress.current_records(root, data["census"])
    progress.card_progress(records, data["direct_candidates"], data["ledger"])
    prior.prior.check_live_claims(records, result, rows)
    return result, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result, rows = build(Path.cwd())
    outputs = [
        (Path(PREFIX + suffix), payload)
        for suffix, payload in zip((".json", ".tsv"), prior.prior.prior.render(result, rows), strict=True)
    ]
    for path, payload in outputs:
        if args.check or path.exists():
            require(path.read_bytes() == payload, "folP/rpo index does not reproduce")
    for path, payload in outputs:
        if not path.exists():
            with path.open("xb") as stream:
                stream.write(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
