"""Reconcile cytochrome-b and outer-membrane references across all CARD claims."""

import argparse
import copy
import json
from collections import Counter, defaultdict
from pathlib import Path

import audit_card_beta_tubulin_memberships as prior
import audit_card_cytochrome_b_references as cytb
import audit_card_outer_membrane_references as outer
import audit_cytochrome_b_evidence as cytb_evidence
import audit_outer_membrane_evidence as outer_evidence

reference, require, registry = prior.reference, prior.require, prior.registry
progress, pointer, rebase = prior.progress, prior.pointer, prior.rebase
PREFIX = "research/2026-10-14-card-cytb-outer-memberships"
PLAN = Path(PREFIX + "-plan.json")
SCOPE = "ELEVEN_COHORT_CARD_REFERENCE_INDEX_NOT_EXPERIMENTAL_GROUNDING"
CYTB = "UNREVIEWED_CYTOCHROME_B_PROTEIN_NAME_REFERENCE_ONLY"
OUTER_REVIEWED = "REVIEWED_OUTER_LABEL_GENE_TAXON_REFERENCE_ONLY"
OUTER_UNREVIEWED = "UNREVIEWED_OUTER_LABEL_GENE_TAXON_CANDIDATE_ONLY"
MIXED = "MULTIPLE_REFERENCE_EVIDENCE_KINDS_NOT_EXPERIMENTAL_SELECTION"
UNSELECTED = "NO_PROTEIN_CANDIDATE_IN_THE_ELEVEN_SELECTED_COHORTS"
COLUMNS = {
    **{k: v for k, v in prior.COLUMNS.items() if k != prior.UNSELECTED},
    CYTB: "cytb_reference_claims",
    OUTER_REVIEWED: "reviewed_outer_reference_claims",
    OUTER_UNREVIEWED: "unreviewed_outer_reference_claims",
    MIXED: "mixed_reference_evidence_claims",
    UNSELECTED: "unselected_candidate_claims",
}
COHORTS = {"cytb": cytb, "outer": outer}
EVIDENCE = {"cytb_evidence": cytb_evidence, "outer_evidence": outer_evidence}


def selected_query(name, term):
    queries = term["queries"]
    if not term["source_organism_name"]:
        require(
            name == "outer" and not queries and not term["reference_candidates"],
            "unnamed or complex term acquired a single-protein query",
        )
        return None
    require(set(queries) in ({"reviewed"}, {"reviewed", "unreviewed"}), "query coverage changed")
    taxid = int(term["named_reference_taxon_id"].split(":")[1])
    eligible = {}
    for kind, query in queries.items():
        reviewed = kind == "reviewed"
        url = (
            cytb.query_url(taxid, reviewed)
            if name == "cytb"
            else outer.gene_url(taxid, term["source_gene_label"], reviewed)
        )
        require(
            query["source"]["url"] == url
            and query["source"]["status"] == 200
            and query["source"]["release"] == "2026_03"
            and query["source_taxon_id"] == taxid
            and query["reviewed_subset"] is reviewed
            and query["complete_for_query"] is True
            and query["zero_hit_is_biological_absence"] is query["suggestions_followed"] is False,
            "query provenance or evidence scope changed",
        )
        if name == "cytb":
            hits, accepted = query["all_result_accessions"], query["candidate_accessions"]
            excluded = [
                r["protein_accession"].removeprefix("UniProtKB:") for r in query["excluded_candidates"]
            ]
            require(
                query["query_type"] == "PROTEIN_NAME_NOT_GENE_SYMBOL"
                and query["candidate_count"] == len(accepted),
                "protein-name candidate count changed",
            )
        else:
            hits = query["accessions"]
            excluded = (
                [
                    r["protein_accession"].removeprefix("UniProtKB:")
                    for r in term["query_hits_not_assigned_to_source_subtype"]
                ]
                if kind == "unreviewed"
                else []
            )
            accepted = [a for a in hits if a not in excluded]
            require(query["gene"] == term["source_gene_label"], "gene query identity changed")
        require(
            type(query["result_count"]) is int
            and query["result_count"] == len(hits)
            and len(hits) == len(set(hits))
            and len(accepted) == len(set(accepted))
            and len(excluded) == len(set(excluded))
            and not set(accepted) & set(excluded)
            and sorted(hits) == sorted(accepted + excluded),
            "complete query-hit accounting changed",
        )
        eligible[kind] = accepted
    kind = "reviewed" if eligible["reviewed"] else "unreviewed"
    require(("unreviewed" in queries) is (not eligible["reviewed"]), "reviewed-first fallback changed")
    candidates = [c["protein_accession"] for c in term["reference_candidates"]]
    require(
        sorted(candidates) == sorted("UniProtKB:" + a for a in eligible[kind]),
        "complete candidate membership changed",
    )
    expected = (
        "MULTIPLE_CANDIDATES_NO_SELECTION"
        if len(candidates) > 1
        else "REVIEWED_REFERENCE"
        if candidates and kind == "reviewed"
        else "UNREVIEWED_CANDIDATE"
        if candidates
        else "NO_EXACT_GENE_RESULTS_NOT_ABSENCE"
    )
    require(term["reference_status"] == expected, "reference disposition changed")
    return kind


def candidate_identity(name, term, candidate, protein, kind):
    accession = candidate["protein_accession"]
    require(
        protein["protein_accession"] == accession
        and protein["entry_type"]
        == ("UniProtKB reviewed (Swiss-Prot)" if kind == "reviewed" else "UniProtKB unreviewed (TrEMBL)")
        and protein["reference_species_taxon_id"] == term["named_reference_taxon_id"]
        and protein["species_lineage_verified"] is True
        and protein["exact_resistance_allele"] is protein["experimental_subject_assignment"] is False
        and protein["experimental_genome_assignment"] is None
        and protein["database_review_status_is_primary_results_review"]
        is protein["resistance_inferred_from_reference"]
        is False
        and protein["unflagged_means_complete"] is False
        and protein["native_protein_flag"] in (None, "Fragment", "Precursor")
        and candidate["exact_resistant_allele"] is candidate["experimental_subject_assignment"] is False,
        "reference identity or experimental scope changed",
    )
    if name == "cytb":
        matches = [n for n in protein["native_protein_names"] if cytb.NATIVE_NAME.fullmatch(n["value"])]
        require(
            kind == "unreviewed"
            and matches
            and matches
            == protein["native_cytochrome_b_name_matches"]
            == candidate["native_cytochrome_b_name_matches"]
            and protein["source_gene_symbol_assignment"] is term["source_gene_symbol"] is None,
            "cytochrome-b native name or gene assignment changed",
        )
    else:
        matches = [
            {"gene_index": i, "field": field, "value": value}
            for i, block in enumerate(protein["genes"])
            for field in ("geneName", "synonyms")
            for value in block[field]
            if value.casefold() == term["source_gene_label"].casefold()
        ]
        require(matches and matches == candidate["native_gene_field_matches"], "native gene matches changed")
        if term["source_gene_label"] == "por":
            values = {n["value"] for n in protein["protein_names"]}
            require(
                values & {"Major outer membrane protein P.IB", "Outer membrane protein PIB"}
                and not values & {"Outer membrane protein IA", "Porin IA protein"}
                and not any("hybrid" in v.casefold() for v in values),
                "PIB subtype identity changed",
            )
    return registry.reference_identity({**protein, "exact_allele_assignment": False})


def merge_link(target, link):
    matches = [old for old in target["links"] if old["protein_accession"] == link["protein_accession"]]
    require(len(matches) <= 1, "duplicate prior term-protein link")
    if matches:
        evidence = matches[0].setdefault("additional_reference_evidence", [])
        require(link not in evidence, "duplicate new reference evidence")
        evidence.append(link)
    else:
        target["links"].append(link)
    kinds = {row["kind"] for row in target["links"]}
    kinds.update(e["kind"] for row in target["links"] for e in row.get("additional_reference_evidence", []))
    target["reference_status"] = next(iter(kinds)) if len(kinds) == 1 else MIXED


def reconcile_cohort(name, data, plan, labels, result):
    dossier, base, module = data[name], data["base"], COHORTS[name]
    require(
        dossier["scope"] == module.SCOPE
        and dossier["release"] == "2026_03"
        and dossier["inputs"]["index"] == plan["inputs"]["base"]
        and dossier["inputs"]["prior_verification"] == plan["inputs"]["base_verification"],
        "reference checkpoint provenance changed",
    )
    for key in ("census", "source_queue", "source_inventory", "definition_citations"):
        require(dossier["inputs"][key] == plan["inputs"][key], "cohort source pin changed")
    expected = {tid for tid in labels if module.SELECT.search(labels[tid])}
    require(set(dossier["terms"]) == expected, "complete source cohort changed")
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
        Counter(map(registry.checksum, claims)) == Counter(map(registry.checksum, dossier["claims"])),
        "source claim positions or hashes changed",
    )
    census = progress.index_unique(data["census"], "identifier", "census")
    ids = {c["record_identifier"] for c in claims}
    require(
        len(dossier["records"]) == len(ids)
        and {r["identifier"] for r in dossier["records"]} == ids
        and all(r == census[r["identifier"]] for r in dossier["records"]),
        "cohort record coverage changed",
    )
    require(
        set(dossier["names"]) == {t["source_organism_name"] for t in dossier["terms"].values()} - {None},
        "complete source-name coverage changed",
    )
    validate_name = prior.named_taxon if name == "cytb" else prior.prior.named_taxon
    names = {label: validate_name(row, label) for label, row in dossier["names"].items()}
    used = set()
    for tid, term in dossier["terms"].items():
        old, target = base["terms"][tid], result["terms"][tid]
        require(
            term["source_label"] == labels[tid]
            and all(term[k] == v for k, v in module.source_identity(labels[tid]).items())
            and term["source_label_sha256"] == old["source_label_sha256"]
            and term["record_memberships"] == old["record_memberships"]
            and term["definition_citation_ids"]
            == data["definition_citations"]["terms"][tid]["definition_citation_ids"]
            and term["experimental_subject_assignment"] is term["exact_allele_assignment"] is False
            and term["experimental_genome_assignment"] is None
            and term["primary_review_status"] == "OPEN",
            "term identity, memberships or primary scope changed",
        )
        if name == "outer":
            require(
                term["prior_reference_links"] == old["links"], "prior explicit reference lost or replaced"
            )
        target[name + "_followup"] = pointer(name, "terms", tid)
        target[name + "_reference_disposition"] = term["reference_status"]
        if term["source_organism_name"]:
            selected = names[term["source_organism_name"]]
            require(
                selected is not None and term["named_reference_taxon_id"] == selected["taxon_id"],
                "term named taxon changed",
            )
        kind = selected_query(name, term)
        for i, candidate in enumerate(term["reference_candidates"]):
            accession = candidate["protein_accession"]
            protein = dossier["proteins"][accession]
            identity = candidate_identity(name, term, candidate, protein, kind)
            item = result["proteins"].setdefault(
                accession,
                {
                    "identity": identity,
                    "sources": [],
                    "experimental_subject_assignment": False,
                    "exact_allele_assignment": False,
                },
            )
            require(item["identity"] == identity, "cross-cohort reference identity conflict")
            source = pointer(name, "proteins", accession)
            if source not in item["sources"]:
                item["sources"].append(source)
            item[name + "_native_metadata"] = source
            if "protein_description_flag" in item:
                require(
                    item["protein_description_flag"] == protein["native_protein_flag"],
                    "native protein flag conflict",
                )
            item["protein_description_flag"] = protein["native_protein_flag"]
            item["unflagged_means_complete"] = False
            status = CYTB if name == "cytb" else OUTER_REVIEWED if kind == "reviewed" else OUTER_UNREVIEWED
            link = {
                "protein_accession": accession,
                "kind": status,
                "explicit_card_xref": False,
                "source_citation_ids": [],
                "matched_reference_numbers": [],
                "source": pointer(name, "terms", tid, "reference_candidates", i),
                "query": pointer(name, "terms", tid, "queries", kind),
                "experimental_subject_assignment": False,
                "exact_allele_assignment": False,
            }
            merge_link(target, link)
            used.add(accession)
    require(used == set(dossier["proteins"]), "unbound reference protein")


def reconcile_rows(data, result):
    census = progress.index_unique(data["census"], "identifier", "census")
    old_rows = progress.index_unique(data["base_rows"], "identifier", "prior row")
    require(set(old_rows) == set(census), "all-record coverage changed")
    old_claims, claims = defaultdict(list), defaultdict(list)
    for old, claim in zip(data["base"]["claims"], result["claims"], strict=True):
        require({**claim, "reference_status": old["reference_status"]} == old, "claim identity changed")
        old_claims[old["record_identifier"]].append(old)
        claims[claim["record_identifier"]].append(claim)
    require(set(claims) <= set(census), "claim outside census")
    rows = []
    for identifier, record in sorted(census.items()):
        old = old_rows[identifier]
        counts, previous = (
            Counter(c["reference_status"] for c in claims[identifier]),
            Counter(c["reference_status"] for c in old_claims[identifier]),
        )
        require(
            all(old[k] == record[k] for k in ("path", "record_sha256", "standard_inchi_key"))
            and int(old["card_assertions"]) == len(claims[identifier])
            and all(int(old[col]) == previous[status] for status, col in prior.COLUMNS.items())
            and old["whole_record_primary_review"] == "OPEN",
            "prior record identity or counts changed",
        )
        old_accessions = {
            link["protein_accession"]
            for claim in claims[identifier]
            for link in data["base"]["terms"][claim["aro_id"]]["links"]
        }
        require(
            old["selected_reference_accessions"] == "|".join(sorted(old_accessions)),
            "prior record reference accessions changed",
        )
        accessions = {
            link["protein_accession"]
            for c in claims[identifier]
            for link in result["terms"][c["aro_id"]]["links"]
        }
        row = {
            **{k: old[k] for k in ("identifier", "path", "record_sha256", "standard_inchi_key")},
            "card_assertions": len(claims[identifier]),
            **{col: counts[status] for status, col in COLUMNS.items()},
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
            sum(counts.values()) == sum(row[col] for col in COLUMNS.values())
            and row["card_assertions"]
            + row["phi_claims_not_reassessed"]
            + row["curator_claims_not_reassessed"]
            == int(record["resistance_assertions"])
            and row["score_rules_not_reassessed"] == int(record["score_rules"]),
            "source-owned accounting changed",
        )
        rows.append(row)
    return rows


def project(data, plan, plan_pin):
    base = data["base"]
    require(
        plan["selection"] == "ALL_CARD_MEMBERSHIPS_WITH_CYTB_AND_OUTER_LABEL_COHORTS"
        and plan["constraints"]
        == {
            "network_requests": 0,
            "biological_writes": False,
            "experimental_assignments": False,
            "issue_1040": "DEFERRED",
        }
        and base["scope"] == prior.SCOPE
        and base["plan"] == plan["inputs"]["base_plan"]
        and data["base_plan"]["inputs"] == base["inputs"]
        and base["limits"]
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
        "index provenance or limits changed",
    )
    for name in ("base", *COHORTS, *EVIDENCE):
        prior.prior.prior.check_checkpoint(data, plan, name)
    for key in (
        "census",
        "curator",
        "source_queue",
        "source_inventory",
        "direct_candidates",
        "ledger",
        "definition_citations",
    ):
        require(plan["inputs"][key] == base["inputs"][key], "successor source pin changed")
    labels = {tid: r["labels"][0] for tid, r in data["direct_candidates"]["determinants"].items()}
    require(
        set(labels) == set(base["terms"])
        and data["direct_candidates"]["source_inventory_sha256"]
        == plan["inputs"]["source_inventory"]["sha256"]
        and all(len(r["labels"]) == 1 for r in data["direct_candidates"]["determinants"].values())
        and all(
            progress.digest(labels[t].encode()) == r["source_label_sha256"] for t, r in base["terms"].items()
        ),
        "complete source-label coverage changed",
    )
    result = rebase(base)
    for term in result["terms"].values():
        require(
            term["experimental_subject_assignment"] is False
            and term["whole_record_primary_review"] == "OPEN"
            and term["reference_status"] in prior.COLUMNS
            and bool(term["links"]) is (term["reference_status"] != prior.UNSELECTED)
            and len(term["links"]) == len({link["protein_accession"] for link in term["links"]})
            and all(
                link["kind"] == term["reference_status"] and link["protein_accession"] in result["proteins"]
                for link in term["links"]
            ),
            "prior term reference scope changed",
        )
        if not term["links"]:
            term["reference_status"] = UNSELECTED
    for item in result["proteins"].values():
        registry.reference_identity(
            {
                **item["identity"],
                "experimental_subject_assignment": item["experimental_subject_assignment"],
                "exact_allele_assignment": item["exact_allele_assignment"],
            }
        )
    for name in COHORTS:
        reconcile_cohort(name, data, plan, labels, result)
    for name, module in EVIDENCE.items():
        context, cohort = data[name], name.removesuffix("_evidence")
        require(
            context["scope"] == module.SCOPE
            and context["inputs"]["prior"] == plan["inputs"][cohort]
            and context["constraints"]["full_corpus_goal_status"] == "OPEN"
            and context["constraints"]["ncbi_requests"] == 0
            and set(context["terms"]) <= set(data[cohort]["terms"]),
            "evidence follow-up scope changed",
        )
        for tid in context["terms"]:
            result["terms"][tid][name] = pointer(name, "terms", tid)
        result[name + "_context"] = pointer(name, "primary_context")
    result["cytb_supplement_access_hold"] = pointer("cytb_evidence", "supplement_discovery_hold")
    for claim in result["claims"]:
        claim["reference_status"] = result["terms"][claim["aro_id"]]["reference_status"]
    rows = reconcile_rows(data, result)
    terms, proteins = result["terms"], result["proteins"]
    links = sum(len(t["links"]) for t in terms.values())
    result.update(
        {
            "date": plan["date"],
            "scope": SCOPE,
            "plan": plan_pin,
            "inputs": plan["inputs"],
            "terms": dict(sorted(terms.items())),
            "proteins": dict(sorted(proteins.items())),
            "summary": {
                **base["summary"],
                "corpus_records": len(rows),
                "card_terms": len(terms),
                "card_assertions": len(result["claims"]),
                "selected_reference_terms": sum(bool(t["links"]) for t in terms.values()),
                "selected_reference_proteins": len(proteins),
                "reference_links": links,
                "term_statuses": dict(sorted(Counter(t["reference_status"] for t in terms.values()).items())),
                "claim_statuses": dict(
                    sorted(Counter(c["reference_status"] for c in result["claims"]).items())
                ),
                "records_with_selected_references": sum(
                    bool(r["selected_reference_accessions"]) for r in rows
                ),
                "added_reference_terms": sum(
                    bool(t["links"]) and not base["terms"][tid]["links"] for tid, t in terms.items()
                ),
                "added_reference_proteins": len(set(proteins) - set(base["proteins"])),
                "added_reference_links": links - base["summary"]["reference_links"],
                "additional_evidence_for_existing_links": sum(
                    len(link.get("additional_reference_evidence", []))
                    for t in terms.values()
                    for link in t["links"]
                ),
                "new_cohort_summaries": {
                    name: copy.deepcopy(data[name]["summary"]) for name in (*COHORTS, *EVIDENCE)
                },
                "unreviewed_fragment_references": sum(
                    p.get("protein_description_flag") == "Fragment"
                    and p["identity"]["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
                    for p in proteins.values()
                ),
            },
            "prior_interpretation": pointer("base", "interpretation"),
            "interpretation": [
                "Eleven selected cohorts, not all research or primary experimental evidence.",
                "Term-protein links are unique; additional evidence for an existing link "
                "is not another candidate.",
                "Mixed reference statuses retain each evidence kind "
                "without selecting an experimental protein.",
                "Complete label screens retain complex, unnamed, zero-hit and subtype-unassigned contexts.",
                "Primary context, reported study genomes and access holds remain scoped evidence pointers.",
                "All PHI, curator, HIVDB and no-claim records remain in scope and are not reassessed here.",
            ],
            "attribution": {name: data[name]["attribution"] for name in ("base", *COHORTS, *EVIDENCE)},
        }
    )
    return result, rows


def build(root, plan_path=PLAN):
    data, plan, pin = prior.prior.prior.read_inputs(root, plan_path)
    base, rows = prior.build(root, Path(plan["inputs"]["base_plan"]["path"]))
    require(
        base == data["base"]
        and registry.render(base, rows)[1]
        == reference.check_pin(root, plan["inputs"]["base_rows"]).read_bytes(),
        "prior index does not reproduce",
    )
    result, rows = project(data, plan, pin)
    records, _ = progress.current_records(root, data["census"])
    progress.card_progress(records, data["direct_candidates"], data["ledger"])
    prior.live.check_live_claims(records, result, rows)
    return result, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result, rows = build(Path.cwd())
    outputs = [
        (Path(PREFIX + suffix), body)
        for suffix, body in zip((".json", ".tsv"), registry.render(result, rows), strict=True)
    ]
    missing = []
    for path, body in outputs:
        if args.check or path.exists():
            require(path.read_bytes() == body, "cytb/outer index does not reproduce")
        else:
            missing.append((path, body))
    for path, body in missing:
        with path.open("xb") as stream:
            stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
