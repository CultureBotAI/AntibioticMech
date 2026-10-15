"""Reconcile complete CYP51/ERG11 and FKS/FSK reference cohorts offline."""

import argparse
import copy
import json
from collections import Counter, defaultdict
from pathlib import Path

import audit_card_demethylase_references as demethylase
import audit_card_demethylase_taxa as taxa
import audit_card_glucan_references as glucan
import audit_card_topoisomerase_memberships as prior

progress, reference = prior.progress, prior.reference
PREFIX = "research/2026-10-14-card-fungal-memberships"
PLAN = Path(PREFIX + "-plan.json")
SCOPE = "CARD_REFERENCE_INDEX_WITH_TWO_COMPLETE_FUNGAL_COHORTS_NOT_EXPERIMENTAL_GROUNDING"
REVIEWED = "REVIEWED_FUNGAL_GENE_AND_SPECIES_REFERENCE_ONLY"
UNREVIEWED = "UNREVIEWED_FUNGAL_GENE_AND_SPECIES_CANDIDATE_ONLY"
UNSELECTED = "NO_PROTEIN_CANDIDATE_IN_THE_SIX_SELECTED_COHORTS"
UNRESOLVED = "SOURCE_NAME_UNRESOLVED_NO_PROTEIN_QUERY"
ZERO = "NO_EXACT_GENE_RESULTS_NOT_ABSENCE"
COLUMNS = {
    **{k: v for k, v in prior.COLUMNS.items() if k != prior.UNSELECTED},
    REVIEWED: "reviewed_fungal_claims",
    UNREVIEWED: "unreviewed_fungal_claims",
    UNSELECTED: "unselected_candidate_claims",
}
COHORTS = {
    "demethylase": (taxa.GENE, taxa.source_identity, demethylase.query_signature),
    "glucan": (glucan.SELECT, glucan.source_identity, glucan.query_signature),
}
require = prior.require


def pointer(name, *parts):
    return prior.pointer(name, "/" + "/".join(str(p).replace("~", "~0").replace("/", "~1") for p in parts))


def rebase(value, *path):
    """Keep inherited pointers scoped to their immutable owner, not our new inputs."""
    if isinstance(value, dict):
        if set(value) == {"input", "pointer"}:
            return pointer("base", *path)
        return {k: rebase(v, *path, k) for k, v in value.items()}
    if isinstance(value, list):
        return [rebase(v, *path, i) for i, v in enumerate(value)]
    return value


def read_inputs(root, plan_path=PLAN):
    data, plan, pin = prior.read_inputs(root, plan_path)
    data["base_rows"] = progress.read_tsv(reference.check_pin(root, plan["inputs"]["base_rows"]).read_bytes())
    return data, plan, pin


def check_checkpoint(data, plan, name):
    dossier, receipt = data[name], data[name + "_verification"]
    require(
        plan["inputs"][name] in receipt["files"]
        and receipt["summary"] == dossier["summary"]
        and receipt["biological_records_changed"] == 0
        and receipt["whole_record_primary_signoffs"] == 0
        and receipt["full_corpus_goal_status"] == "OPEN",
        "checkpoint receipt or scope changed",
    )


def check_query(query, gene, species, reviewed, signature):
    accessions = query["accessions"]
    require(
        signature(query["source"]["url"]) == (gene, species, reviewed)
        and query.get("gene_query_key", query.get("gene")) == gene
        and type(query["species_id"]) is int
        and query["species_id"] == species
        and query["reviewed_subset"] is reviewed
        and query["complete_for_query"] is True
        and query["zero_hit_is_biological_absence"] is False
        and query["source"]["status"] == 200
        and query["source"]["release"] == "2026_03"
        and type(query["result_count"]) is int
        and query["result_count"] == len(accessions) == len(set(accessions))
        and all(isinstance(a, str) and a and not a.startswith("UniProtKB:") for a in accessions)
        and query.get("suggestions_followed", False) is False,
        "query identity, completeness or evidence scope changed",
    )


def selected_query(context, gene, species, signature):
    queries, candidates = context["queries"], context["reference_candidates"]
    if species is None:
        require(
            not queries and not candidates and context["status"] == UNRESOLVED,
            "unresolved name acquired candidates",
        )
        return None, None
    require(set(queries) in ({"reviewed"}, {"reviewed", "unreviewed"}), "reviewed-first query policy changed")
    check_query(queries["reviewed"], gene, species, True, signature)
    reviewed = bool(queries["reviewed"]["accessions"])
    require(("unreviewed" in queries) is (not reviewed), "unreviewed fallback without reviewed zero hits")
    kind = "reviewed" if reviewed else "unreviewed"
    query = queries[kind]
    if not reviewed:
        check_query(query, gene, species, False, signature)
    selected = [c["protein_accession"] for c in candidates]
    require(
        sorted(selected) == sorted("UniProtKB:" + a for a in query["accessions"]),
        "query candidate coverage changed",
    )
    status = (
        ZERO
        if not selected
        else "MULTIPLE_CANDIDATES_NO_SELECTION"
        if len(selected) > 1
        else "REVIEWED_REFERENCE"
        if reviewed
        else "UNREVIEWED_CANDIDATE"
    )
    require(context["status"] == status, "query disposition changed")
    return kind, query


def protein_identity(accession, protein, candidate, gene, species, reviewed):
    require(
        protein["protein_accession"] == accession
        and protein["entry_type"]
        == ("UniProtKB reviewed (Swiss-Prot)" if reviewed else "UniProtKB unreviewed (TrEMBL)")
        and protein["species_lineage_verified"] is True
        and protein["reference_species_taxon_id"] == f"NCBITaxon:{species}"
        and protein["exact_resistance_allele"] is False
        and protein["experimental_subject_assignment"] is False
        and protein["experimental_genome_assignment"] is None
        and protein["database_review_status_is_primary_results_review"] is False
        and protein["resistance_inferred_from_reference"] is False
        and protein["native_protein_flag"] in (None, "Fragment")
        and protein.get("protein_description_flag", protein["native_protein_flag"])
        == protein["native_protein_flag"]
        and protein["unflagged_means_complete"] is False
        and candidate["experimental_subject_assignment"] is False
        and candidate["exact_resistant_allele"] is False,
        "protein identity or evidence scope changed",
    )
    matches = [
        {"gene_index": i, "field": field, "value": value}
        for i, block in enumerate(protein["genes"])
        for field in ("geneName", "synonyms")
        for value in block[field]
        if value.casefold() == gene
    ]
    require(
        len({m["gene_index"] for m in matches}) == 1 and matches == candidate["native_gene_field_matches"],
        "native gene-name match absent, ambiguous or changed",
    )
    return prior.prior.reference_identity({**protein, "exact_allele_assignment": False})


def reconcile_cohort(name, data, labels, terms, proteins):
    dossier, base = data[name], data["base"]
    require(
        dossier["scope"]
        == (
            "ALL_CARD_CYP51_ERG11_REFERENCE_CONTEXTS_NOT_EXPERIMENTAL_ALLELES_OR_PHENOTYPES"
            if name == "demethylase"
            else "ALL_CARD_FKS_FSK_REFERENCE_CONTEXTS_NOT_RESISTANCE_ALLELES"
        )
        and dossier["release"] == "2026_03",
        "fungal dossier scope changed",
    )
    selector, parse_label, signature = COHORTS[name]
    require(
        set(dossier["terms"]) == {tid for tid in base["terms"] if selector.search(labels[tid])},
        "full fungal cohort coverage changed",
    )
    expected_claims = [
        {
            "record_identifier": c["record_identifier"],
            "position": c["resistance_index"],
            "aro_id": c["aro_id"],
            "claim_sha256": c["claim_sha256"],
        }
        for c in base["claims"]
        if c["aro_id"] in dossier["terms"]
    ]
    require(
        Counter(map(prior.prior.checksum, expected_claims))
        == Counter(map(prior.prior.checksum, dossier["claims"])),
        "fungal claim position or content changed",
    )
    census = progress.index_unique(data["census"], "identifier", "census record")
    record_ids = {c["record_identifier"] for c in expected_claims}
    require(
        len(dossier["records"]) == len(record_ids)
        and {r["identifier"] for r in dossier["records"]} == record_ids
        and all(r == census[r["identifier"]] for r in dossier["records"]),
        "fungal record identity changed",
    )
    context_key = "gene_contexts" if name == "demethylase" else "source_contexts"
    term_context_key = "gene_context" if name == "demethylase" else "source_context"
    contexts = dossier[context_key]
    names = data["demethylase_taxa"]["names"] if name == "demethylase" else dossier["names"]
    seen, used_proteins, used_queries = set(), set(), set()
    for key, context in contexts.items():
        source_name = context["source_name"]
        gene = context.get("casefold_gene_query_key", context.get("gene_query_key"))
        require(json.loads(key) == [source_name, gene], "source context key changed")
        name_row = names[source_name]
        selected_taxon = name_row["selected_taxon"]
        taxid = selected_taxon["taxon_id"] if selected_taxon else None
        species = int(taxid.split(":")[1]) if taxid else None
        require(name_row["experimental_subject_assignment"] is False, "source name became experimental")
        if selected_taxon:
            require(
                selected_taxon["active"] is True
                and selected_taxon["rank"] == "species"
                and selected_taxon["experimental_subject_assignment"] is False
                and selected_taxon["accepted_name_and_rank"] is True
                and selected_taxon["other_name_match_only"] is False,
                "source name is not an accepted species reference",
            )
        if name == "demethylase":
            require(
                context["named_reference_taxon_id"] == taxid and context["experimental_assignments"] is False,
                "demethylase context scope changed",
            )
            query_context, query_path = context, (context_key, key)
        else:
            require(
                context["species_id"] == species and context["source_spelling_corrected"] is False,
                "glucan context scope changed",
            )
            query_key = context["query_key"]
            require(json.loads(query_key) == [gene, species], "shared query key changed")
            query_context = dossier["query_contexts"][query_key]
            require(
                query_context["gene"] == gene
                and query_context["species_id"] == species
                and query_context["source_spelling_corrected"] is False
                and query_context["reference_candidates"] == context["reference_candidates"]
                and query_context["status"] == context["reference_status"],
                "shared query binding changed",
            )
            query_path = ("query_contexts", query_key)
            used_queries.add(query_key)
        kind, _ = selected_query(query_context, gene, species, signature)
        status = query_context["status"]
        candidates = query_context["reference_candidates"]
        accessions = [c["protein_accession"] for c in candidates]
        source_gene_labels = set()
        require(bool(context["terms"]), "orphan fungal context")
        for tid in context["terms"]:
            term, original = dossier["terms"][tid], base["terms"][tid]
            require(
                tid not in seen
                and not original["links"]
                and original["reference_status"] == prior.UNSELECTED,
                "duplicate or previously linked fungal term",
            )
            seen.add(tid)
            identity = parse_label(labels[tid])
            require(
                all(term[k] == v for k, v in identity.items())
                and term["source_label"] == labels[tid]
                and term["source_label_sha256"]
                == original["source_label_sha256"]
                == progress.digest(labels[tid].encode())
                and term["record_memberships"] == original["record_memberships"]
                and term[term_context_key] == key
                and term["source_organism_name"] == source_name
                and term["source_gene_label"].casefold() == gene
                and term["named_reference_taxon_id"] == taxid
                and term["reference_candidates"] == accessions
                and term["reference_status"] == status
                and term["exact_allele_assignment"] is False
                and term["experimental_subject_assignment"] is False
                and term.get("experimental_genome_assignment") is None
                and term["primary_review_status"] == "OPEN",
                "fungal term identity, membership or scope changed",
            )
            source_gene_labels.add(term["source_gene_label"])
            target = terms[tid]
            target["fungal_followup"] = pointer(name, "terms", tid)
            target["fungal_query_disposition"] = status
            target["named_organism_taxon_reference_only"] = taxid
            target["fungal_name_context"] = pointer(
                "demethylase_taxa" if name == "demethylase" else name, "names", source_name
            )
            for i, candidate in enumerate(candidates):
                accession = candidate["protein_accession"]
                protein = dossier["proteins"][accession]
                identity = protein_identity(accession, protein, candidate, gene, species, kind == "reviewed")
                item = proteins.setdefault(
                    accession,
                    {
                        "identity": identity,
                        "sources": [],
                        "experimental_subject_assignment": False,
                        "exact_allele_assignment": False,
                    },
                )
                require(item["identity"] == identity, "conflicting cross-cohort protein identity")
                provenance = pointer(name, "proteins", accession)
                if provenance not in item["sources"]:
                    item["sources"].append(provenance)
                require(
                    item.get("protein_description_flag", protein["native_protein_flag"])
                    == protein["native_protein_flag"],
                    "conflicting protein fragment status",
                )
                item["protein_description_flag"] = protein["native_protein_flag"]
                item["unflagged_means_complete"] = False
                link_kind = REVIEWED if kind == "reviewed" else UNREVIEWED
                target["links"].append(
                    {
                        "protein_accession": accession,
                        "kind": link_kind,
                        "explicit_card_xref": False,
                        "source_citation_ids": [],
                        "matched_reference_numbers": [],
                        "source": pointer(name, *query_path, "reference_candidates", i),
                        "query": pointer(name, *query_path, "queries", kind),
                        "experimental_subject_assignment": False,
                        "exact_allele_assignment": False,
                    }
                )
                target["reference_status"] = link_kind
                used_proteins.add(accession)
        require(
            Counter(source_gene_labels) == Counter(context["source_gene_labels"]),
            "source paralog labels changed",
        )
    require(
        seen == set(dossier["terms"]) and used_proteins == set(dossier["proteins"]),
        "unbound fungal terms or proteins",
    )
    if name == "glucan":
        require(used_queries == set(dossier["query_contexts"]), "unbound fungal query")


def project(data, plan, plan_pin):
    base, inputs = data["base"], plan["inputs"]
    require(
        plan["selection"] == "ALL_CARD_MEMBERSHIPS_WITH_COMPLETE_CYP51_ERG11_AND_FKS_FSK_COHORTS"
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
        )
        and data["demethylase"]["inputs"]["prior"] == inputs["demethylase_taxa"]
        and data["demethylase_taxa"]["inputs"]["index"] == inputs["base"]
        and data["glucan"]["inputs"]["index"] == inputs["base"],
        "index plan or checkpoint provenance changed",
    )
    for name in ("base", *COHORTS):
        check_checkpoint(data, plan, name)
    for name in COHORTS:
        require(
            all(data[name]["inputs"][k] == inputs[k] for k in ("census", "source_inventory")),
            "fungal source provenance changed",
        )
    require(
        not set(data["demethylase"]["terms"]) & set(data["glucan"]["terms"]),
        "overlapping fungal source terms",
    )
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
        prior.prior.reference_identity(
            {
                **protein["identity"],
                **{k: protein[k] for k in ("experimental_subject_assignment", "exact_allele_assignment")},
            }
        )
    for term in terms.values():
        require(
            term["experimental_subject_assignment"] is False
            and term["whole_record_primary_review"] == "OPEN",
            "base term scope changed",
        )
        if term["reference_status"] == prior.UNSELECTED:
            term["reference_status"] = UNSELECTED
    for name in COHORTS:
        reconcile_cohort(name, data, labels, terms, proteins)
    claims, by_record, memberships = copy.deepcopy(base["claims"]), defaultdict(list), defaultdict(set)
    require(
        Counter((c["record_identifier"], c["aro_id"]) for c in claims)
        == Counter((r["identifier"], r["aro_id"]) for r in data["ledger"]),
        "source ledger membership changed",
    )
    census = progress.index_unique(data["census"], "identifier", "census record")
    indexes = set()
    for claim in claims:
        identifier, tid = claim["record_identifier"], claim["aro_id"]
        record = census[identifier]
        key = (identifier, claim["resistance_index"])
        require(
            type(claim["resistance_index"]) is int
            and claim["resistance_index"] >= 0
            and key not in indexes
            and claim["experimental_subject_assignment"] is False
            and all(
                claim[k] == record[r]
                for k, r in (
                    ("record_path", "path"),
                    ("record_sha256", "record_sha256"),
                    ("standard_inchi_key", "standard_inchi_key"),
                )
            ),
            "base claim identity changed",
        )
        indexes.add(key)
        claim["reference_status"] = terms[tid]["reference_status"]
        by_record[identifier].append(claim)
        memberships[tid].add(identifier)
    require(
        set(memberships) == set(terms)
        and all(sorted(memberships[t]) == r["record_memberships"] for t, r in terms.items()),
        "base term memberships changed",
    )
    old_rows = progress.index_unique(data["base_rows"], "identifier", "base row")
    require(set(old_rows) == set(census), "base census coverage changed")
    curated = Counter(c["record_identifier"] for c in data["curator"]["claims"])
    require(
        data["curator"]["census"] == inputs["census"] and set(curated) <= set(census),
        "curator checkpoint changed",
    )
    rows = []
    for identifier, record in sorted(census.items()):
        old, subset = old_rows[identifier], by_record[identifier]
        require(
            all(old[k] == record[k] for k in ("path", "record_sha256", "standard_inchi_key"))
            and int(old["card_assertions"]) == len(subset),
            "base row identity changed",
        )
        statuses = Counter(c["reference_status"] for c in subset)
        require(
            int(old["curator_claims_not_reassessed"]) == curated[identifier]
            and int(old["phi_claims_not_reassessed"])
            == int(record["resistance_assertions"]) - len(subset) - curated[identifier]
            and int(old["phi_claims_not_reassessed"]) >= 0
            and int(old["score_rules_not_reassessed"]) == int(record["score_rules"])
            and old["whole_record_primary_review"] == "OPEN",
            "unreassessed source counts or primary scope changed",
        )
        links = {link["protein_accession"] for c in subset for link in terms[c["aro_id"]]["links"]}
        rows.append(
            {
                **{k: old[k] for k in ("identifier", "path", "record_sha256", "standard_inchi_key")},
                "card_assertions": len(subset),
                **{column: statuses[kind] for kind, column in COLUMNS.items()},
                "selected_reference_accessions": "|".join(sorted(links)),
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
    fungal_terms = set(data["demethylase"]["terms"]) | set(data["glucan"]["terms"])
    summary = {
        **base["summary"],
        "corpus_records": len(rows),
        "card_assertions": len(claims),
        "card_terms": len(terms),
        "selected_reference_terms": sum(bool(t["links"]) for t in terms.values()),
        "selected_reference_proteins": len(proteins),
        "reference_links": sum(len(t["links"]) for t in terms.values()),
        "term_statuses": dict(sorted(Counter(t["reference_status"] for t in terms.values()).items())),
        "claim_statuses": dict(sorted(Counter(c["reference_status"] for c in claims).items())),
        "records_with_selected_references": sum(bool(r["selected_reference_accessions"]) for r in rows),
        "added_reference_proteins": len(set(proteins) - set(base["proteins"])),
        "added_reference_terms": sum(bool(terms[t]["links"]) for t in fungal_terms),
        "added_reference_links": sum(len(terms[t]["links"]) for t in fungal_terms),
        "fungal_source_terms": len(fungal_terms),
        "fungal_source_claims": sum(c["aro_id"] in fungal_terms for c in claims),
        "fungal_followup_dispositions": dict(
            sorted(Counter(terms[t]["fungal_query_disposition"] for t in fungal_terms).items())
        ),
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
            "Two complete fungal cohorts extend the four-cohort reference index; "
            "other dossiers remain separate.",
            "Gene/species reference candidates are not tested resistance alleles, "
            "experimental subjects, genomes or phenotypes.",
            "All query candidates, source paralog spellings, fragment flags "
            "and unresolved contexts are retained.",
            "Zero exact-query hits do not establish biological absence; "
            "reviewed zero hits alone allow unreviewed fallback.",
            "Inherited RNA, qualified Salmonella, proteome and primary-access "
            "context remains in pinned owners.",
            "Primary results, PHI-base, curator claims and HIVDB score rules are not reassessed; "
            "whole-record reviews remain open.",
        ],
        **{
            key: pointer("base", key)
            for key in (
                "shared_symbol_reference_context",
                "salmonella_taxonomy_context",
                "salmonella_primary_review",
            )
        },
        "attribution": {k: data[k]["attribution"] for k in ("base", *COHORTS)},
    }, rows


def build(root, plan_path=PLAN):
    data, plan, pin = read_inputs(root, plan_path)
    inventory = progress.read_tsv(reference.check_pin(root, plan["inputs"]["source_inventory"]).read_bytes())
    labels = defaultdict(set)
    for row in inventory:
        labels[row["determinant_id"]].add(row["determinant_name"])
    require(
        all(
            labels[tid] == set(row["labels"])
            for tid, row in data["direct_candidates"]["determinants"].items()
        ),
        "current source labels differ from the frozen public checkpoint",
    )
    result, rows = project(data, plan, pin)
    records, _ = progress.current_records(root, data["census"])
    progress.card_progress(records, data["direct_candidates"], data["ledger"])
    prior.check_live_claims(records, result, rows)
    return result, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result, rows = build(Path.cwd())
    for suffix, body in zip((".json", ".tsv"), prior.prior.render(result, rows), strict=True):
        path = Path(PREFIX + suffix)
        if args.check or path.exists():
            require(path.read_bytes() == body, "fungal successor index does not reproduce")
        else:
            with path.open("xb") as stream:
                stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
