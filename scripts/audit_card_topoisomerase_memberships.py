"""Reconcile pinned topoisomerase reference dossiers with every current CARD claim."""

import argparse
import copy
import json
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import audit_card_reference_memberships as prior
from audit_curator_resistance_fields import owner

progress, reference = prior.progress, prior.reference
PREFIX = "research/2026-10-14-card-topoisomerase-memberships"
PLAN = Path(PREFIX + "-plan.json")
SCOPE = "CARD_REFERENCE_INDEX_WITH_TOPOISOMERASE_FOLLOWUPS_NOT_EXPERIMENTAL_GROUNDING"
REVIEWED = "REVIEWED_GENE_AND_SPECIES_REFERENCE_ONLY"
UNREVIEWED = "UNREVIEWED_GENE_AND_SPECIES_CANDIDATE_ONLY"
UNSELECTED = "NO_PROTEIN_CANDIDATE_IN_THE_FOUR_SELECTED_COHORTS"
COLUMNS = {
    prior.DIRECT: "direct_xref_claims",
    prior.CITATION: "citation_candidate_claims",
    REVIEWED: "reviewed_topoisomerase_claims",
    UNREVIEWED: "unreviewed_topoisomerase_claims",
    UNSELECTED: "unselected_candidate_claims",
}


def pointer(name, path):
    return {"input": name, "pointer": path}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_memberships(dossier, claims):
    expected = Counter(
        (c["record_identifier"], c["aro_id"]) for c in claims if c["aro_id"] in dossier["terms"]
    )
    actual = Counter((r["record_id"], r["aro_id"]) for r in dossier["memberships"])
    require(actual == expected, "follow-up assertion memberships changed")
    for tid, term in dossier["terms"].items():
        require(
            term["record_ids"] == sorted({i for i, t in expected if t == tid})
            and term["source_assertion_memberships"] == sum(n for (_, t), n in expected.items() if t == tid),
            "follow-up term memberships changed",
        )


def check_query(query, term, unreviewed=False):
    species = term["source_species_taxon_id"]
    expected = (
        f"(gene_exact:{term['source_gene_symbol']} AND taxonomy_id:{species.split(':')[1]} "
        f"AND reviewed:{'false' if unreviewed else 'true'})"
    )
    url = urlparse(query["url"])
    require(
        query["query"] == expected
        and url.scheme == "https"
        and url.netloc == "rest.uniprot.org"
        and url.path == "/uniprotkb/search"
        and parse_qs(url.query).get("query") == [expected]
        and query["status"] == 200
        and query["release"] == "2026_03"
        and query["zero_hit_is_absence"] is False
        and len(query["accessions"]) == len(set(query["accessions"])),
        "reference query identity, completeness or scope changed",
    )


def topoisomerase_identity(accession, protein, unreviewed):
    require(
        protein["protein_accession"] == f"UniProtKB:{accession}"
        and protein["species_lineage_verified"] is True
        and protein["exact_resistance_allele"] is False
        and protein["experimental_subject_assignment"] is False
        and protein["entry_type"]
        == ("UniProtKB unreviewed (TrEMBL)" if unreviewed else "UniProtKB reviewed (Swiss-Prot)"),
        "topoisomerase protein identity or evidence scope changed",
    )
    return prior.reference_identity(
        {
            **protein,
            "exact_allele_assignment": False,
            "reference_species_taxon_id": protein["source_species_taxon_id"],
        }
    )


def reconcile(base, reviewed, unreviewed, salmonella):
    require(base["scope"] == prior.SCOPE, "base reference index scope changed")
    require(
        reviewed["scope"] == "REVIEWED_REFERENCE_PROTEINS_NOT_EXPERIMENTAL_RESISTANCE_ALLELES"
        and unreviewed["scope"]
        == "UNREVIEWED_IDENTIFIER_CANDIDATES_NOT_RESISTANCE_ALLELES_OR_EXPERIMENTAL_GENOMES",
        "topoisomerase dossier scope changed",
    )
    require(set(reviewed["terms"]) <= set(base["terms"]), "unknown follow-up term")
    check_memberships(reviewed, base["claims"])
    check_memberships(unreviewed, base["claims"])
    no_hit = {
        t for t, r in reviewed["terms"].items() if r["reference_query"] and not r["reference_candidates"]
    }
    unresolved = {t for t, r in reviewed["terms"].items() if not r["reference_query"]}
    require(set(unreviewed["terms"]) == no_hit, "unreviewed follow-up does not cover reviewed no-hit terms")
    require(set(salmonella["terms"]) == unresolved, "qualified Salmonella successor coverage changed")
    terms, proteins = {}, {}
    # Old source pointers remain resolvable through the immutable prior index.
    for accession, protein in base["proteins"].items():
        identity = prior.reference_identity(
            {
                **protein["identity"],
                **{k: protein[k] for k in ("experimental_subject_assignment", "exact_allele_assignment")},
            }
        )
        proteins[accession] = {
            "identity": identity,
            "sources": [pointer("base", f"/proteins/{accession}")],
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
    for tid, term in base["terms"].items():
        require(
            term["experimental_subject_assignment"] is False
            and term["whole_record_primary_review"] == "OPEN",
            "base term scope changed",
        )
        result = copy.deepcopy(term)
        for field in ("ontology_scope_source", "entity_review_source"):
            result[field] = pointer("base", f"/terms/{tid}/{field}") if term[field] else None
        for index, link in enumerate(result["links"]):
            require(
                link["kind"] in (prior.DIRECT, prior.CITATION) and link["protein_accession"] in proteins,
                "base reference link changed",
            )
            link["source"] = pointer("base", f"/terms/{tid}/links/{index}")
        require(
            term["reference_status"] == (term["links"][0]["kind"] if term["links"] else prior.UNSELECTED),
            "base reference status inconsistent",
        )
        if not term["links"]:
            result["reference_status"] = UNSELECTED
        result["topoisomerase_followup"] = None
        result["qualified_scope_followup"] = None
        terms[tid] = result

    used_queries = {"reviewed": set(), "unreviewed": set()}
    used_proteins = {"reviewed": set(), "unreviewed": set()}
    for tid, term in reviewed["terms"].items():
        target = terms[tid]
        require(
            not target["links"]
            and target["source_label_sha256"] == term["source_label_sha256"]
            and target["record_memberships"] == term["record_ids"]
            and term["exact_allele_assignment"] is False
            and term["experimental_assignment"] is False
            and term["primary_review_status"] == "OPEN",
            "reviewed follow-up term identity or scope changed",
        )
        target["topoisomerase_followup"] = pointer("reviewed", f"/terms/{tid}")
        if tid in unresolved:
            successor = salmonella["terms"][tid]
            require(
                term["source_species_taxon_id"] is None
                and not term["reference_candidates"]
                and successor["record_ids"] == term["record_ids"]
                and successor["source_assertion_memberships"] == term["source_assertion_memberships"]
                and successor["gene"] == term["source_gene_symbol"]
                and successor["source_organism_name"] == term["source_organism_name"]
                and successor["exact_allele_assignment"] is False
                and successor["experimental_protein_accession"] is None
                and successor["experimental_subject_taxon_id"] is None,
                "unresolved source scope or qualified successor changed",
            )
            target["qualified_scope_followup"] = pointer("salmonella", f"/terms/{tid}")
            continue
        species = term["source_species_taxon_id"]
        taxonomy = reviewed["source_name_taxonomy"][term["source_organism_name"]]
        require(
            term["source_name_status"] == taxonomy["status"] == "EXACT_SPECIES_NAME_RESOLVED"
            and taxonomy["named_organism_taxon_id"] == species
            and taxonomy["release"] == "2026_03"
            and len(taxonomy["exact_candidates"]) == 1
            and taxonomy["exact_candidates"][0]["taxon_id"] == species
            and taxonomy["exact_candidates"][0]["rank"] == "species"
            and taxonomy["exact_candidates"][0]["active"] is True
            and taxonomy["exact_candidates"][0]["other_name_match_only"] is False,
            "source species identity changed",
        )
        query = reviewed["queries"][term["reference_query"]]
        check_query(query, term)
        used_queries["reviewed"].add(term["reference_query"])
        require(term["reference_candidates"] == query["accessions"], "reviewed candidate coverage changed")
        cohort, selected, query_key = "reviewed", term["reference_candidates"], term["reference_query"]
        if tid in no_hit:
            follow = unreviewed["terms"][tid]
            require(
                all(
                    follow[k] == term[k]
                    for k in (
                        "record_ids",
                        "source_assertion_memberships",
                        "source_gene_symbol",
                        "source_label_sha256",
                        "source_organism_name",
                        "source_species_taxon_id",
                    )
                )
                and follow["reviewed_candidates"] == []
                and follow["exact_allele_assignment"] is False
                and follow["experimental_subject_assignment"] is False
                and follow["primary_review_status"] == "OPEN",
                "unreviewed term identity or scope changed",
            )
            cohort, selected, query_key = "unreviewed", follow["unreviewed_candidates"], follow["query"]
            query = unreviewed["queries"][query_key]
            check_query(query, follow, unreviewed=True)
            require(
                query["prior_reviewed_query"] == term["reference_query"]
                and query["accessions"] == selected
                and bool(selected),
                "unreviewed query coverage changed",
            )
            used_queries[cohort].add(query_key)
            target["topoisomerase_followup"] = pointer(cohort, f"/terms/{tid}")
        source = unreviewed if cohort == "unreviewed" else reviewed
        protein_key = "unreviewed_proteins" if cohort == "unreviewed" else "reference_proteins"
        status = UNREVIEWED if cohort == "unreviewed" else REVIEWED
        for index, accession in enumerate(selected):
            protein = source[protein_key][accession]
            identity = topoisomerase_identity(accession, protein, cohort == "unreviewed")
            require(
                term["source_gene_symbol"] in protein["gene_names"]
                and protein["source_species_taxon_id"] == species,
                "gene/species reference mismatch",
            )
            key = protein["protein_accession"]
            item = proteins.setdefault(
                key,
                {
                    "identity": identity,
                    "sources": [],
                    "experimental_subject_assignment": False,
                    "exact_allele_assignment": False,
                },
            )
            require(item["identity"] == identity, "conflicting cross-cohort protein identity")
            provenance = pointer(cohort, f"/{protein_key}/{accession}")
            if provenance not in item["sources"]:
                item["sources"].append(provenance)
            if cohort == "unreviewed":
                require(
                    protein["unflagged_means_complete"] is False
                    and protein["protein_description_flag"] in (None, "Fragment"),
                    "fragment scope changed",
                )
                item["protein_description_flag"] = protein["protein_description_flag"]
                item["unflagged_means_complete"] = False
                item["proteome_context"] = pointer(cohort, f"/{protein_key}/{accession}/proteome_links")
                for link in protein["proteome_links"]:
                    proteome = unreviewed["reference_proteomes"][link["proteome_id"]]
                    require(
                        link["experimental_genome_assignment"] is False
                        and proteome["experimental_genome_assignment"] is False
                        and link["reference_taxon_matches"] is True
                        and link["reported_components_match"] is True
                        and link["reference_assembly_id"] == proteome["reference_assembly_id"]
                        and protein["reference_taxon_id"] == proteome["reference_taxon_id"],
                        "reference proteome context changed",
                    )
            candidate_key = "unreviewed_candidates" if cohort == "unreviewed" else "reference_candidates"
            target["links"].append(
                {
                    "protein_accession": key,
                    "kind": status,
                    "explicit_card_xref": False,
                    "source_citation_ids": [],
                    "matched_reference_numbers": [],
                    "source": pointer(cohort, f"/terms/{tid}/{candidate_key}/{index}"),
                    "query": pointer(cohort, f"/queries/{query_key}"),
                    "experimental_subject_assignment": False,
                    "exact_allele_assignment": False,
                }
            )
            used_proteins[cohort].add(accession)
        target["reference_status"] = status
    for name, dossier, key in (
        ("reviewed", reviewed, "reference_proteins"),
        ("unreviewed", unreviewed, "unreviewed_proteins"),
    ):
        require(used_queries[name] == set(dossier["queries"]), "unbound follow-up query")
        require(used_proteins[name] == set(dossier[key]), "unbound follow-up protein")
    return dict(sorted(terms.items())), dict(sorted(proteins.items()))


def project(data, plan, plan_pin):
    base, reviewed, unreviewed = [data[k] for k in ("base", "reviewed", "unreviewed")]
    inputs = plan["inputs"]
    require(
        plan["selection"] == "ALL_CARD_MEMBERSHIPS_WITH_PINNED_TOPOISOMERASE_SUCCESSORS"
        and plan["constraints"]
        == {
            "network_requests": 0,
            "biological_writes": False,
            "experimental_assignments": False,
            "issue_1040": "DEFERRED",
        },
        "successor plan scope changed",
    )
    require(
        all(
            base["inputs"][k] == inputs[k]
            for k in ("direct_candidates", "ledger", "source_inventory", "source_queue")
        )
        and reviewed["inputs"]["source_reference_audit"] == inputs["direct_candidates"]
        and reviewed["inputs"]["source_named_taxa"] == base["inputs"]["named_taxa"]
        and unreviewed["inputs"]["prior_dossier"] == inputs["reviewed"]
        and data["curator"]["census"] == inputs["census"],
        "checkpoint provenance changed",
    )
    terms, proteins = reconcile(base, reviewed, unreviewed, data["salmonella"])
    census = progress.index_unique(data["census"], "identifier", "census record")
    expected = Counter((r["identifier"], r["aro_id"]) for r in data["ledger"])
    require(
        Counter((c["record_identifier"], c["aro_id"]) for c in base["claims"]) == expected,
        "base claim memberships differ from source ledger",
    )
    claims, by_record, memberships, indexes = [], defaultdict(list), defaultdict(set), set()
    for claim in base["claims"]:
        identifier, tid = claim["record_identifier"], claim["aro_id"]
        record = census[identifier]
        require(
            claim["experimental_subject_assignment"] is False
            and claim["record_path"] == record["path"]
            and claim["standard_inchi_key"] == record["standard_inchi_key"]
            and type(claim["resistance_index"]) is int
            and claim["resistance_index"] >= 0
            and (identifier, claim["resistance_index"]) not in indexes,
            "base claim identity changed",
        )
        indexes.add((identifier, claim["resistance_index"]))
        item = {
            **claim,
            "record_sha256": record["record_sha256"],
            "reference_status": terms[tid]["reference_status"],
        }
        claims.append(item)
        by_record[identifier].append(item)
        memberships[tid].add(identifier)
    require(set(memberships) == set(terms), "source term coverage changed")
    for tid, term in terms.items():
        require(sorted(memberships[tid]) == term["record_memberships"], "base term memberships changed")
    curated = Counter(c["record_identifier"] for c in data["curator"]["claims"])
    require(set(curated) <= set(census), "unknown curated record")
    rows = []
    for identifier, record in sorted(census.items()):
        subset = by_record[identifier]
        statuses = Counter(c["reference_status"] for c in subset)
        links = {link["protein_accession"] for c in subset for link in terms[c["aro_id"]]["links"]}
        phi = int(record["resistance_assertions"]) - len(subset) - curated[identifier]
        require(phi >= 0, "negative unreviewed source count")
        rows.append(
            {
                **{k: record[k] for k in ("identifier", "path", "record_sha256", "standard_inchi_key")},
                "card_assertions": len(subset),
                **{column: statuses[kind] for kind, column in COLUMNS.items()},
                "selected_reference_accessions": "|".join(sorted(links)),
                "phi_claims_not_reassessed": phi,
                "curator_claims_not_reassessed": curated[identifier],
                "score_rules_not_reassessed": int(record["score_rules"]),
                "whole_record_primary_review": "OPEN",
            }
        )
    summary = {
        "corpus_records": len(rows),
        "card_assertions": len(claims),
        "card_terms": len(terms),
        "selected_reference_terms": sum(bool(t["links"]) for t in terms.values()),
        "selected_reference_proteins": len(proteins),
        "reference_links": sum(len(t["links"]) for t in terms.values()),
        "term_statuses": dict(sorted(Counter(t["reference_status"] for t in terms.values()).items())),
        "claim_statuses": dict(sorted(Counter(c["reference_status"] for c in claims).items())),
        "records_with_selected_references": sum(bool(r["selected_reference_accessions"]) for r in rows),
        "records_without_card_assertions": sum(not r["card_assertions"] for r in rows),
        "phi_claims_not_reassessed": sum(r["phi_claims_not_reassessed"] for r in rows),
        "curator_claims_not_reassessed": sum(curated.values()),
        "score_rules_not_reassessed": sum(r["score_rules_not_reassessed"] for r in rows),
        "added_reference_proteins": len(set(proteins) - set(base["proteins"])),
        "added_reference_terms": sum(bool(terms[t]["links"]) for t in reviewed["terms"]),
        "added_reference_links": sum(len(terms[t]["links"]) for t in reviewed["terms"]),
        "unreviewed_fragment_references": sum(
            p.get("protein_description_flag") == "Fragment" for p in proteins.values()
        ),
        "qualified_salmonella_terms_without_selected_protein": len(data["salmonella"]["terms"]),
        "whole_record_primary_signoffs": 0,
    }
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": plan_pin,
        "inputs": inputs,
        "terms": terms,
        "proteins": proteins,
        "claims": claims,
        "summary": summary,
        "limits": {**base["limits"], "outreach": 0, "reuse_terms_review_resumed": False},
        "interpretation": [
            "This index extends two pinned reference cohorts with two topoisomerase follow-ups; "
            "other dossiers remain separate.",
            "Reference gene/species matches are not exact resistance alleles, experimental subjects, "
            "genomes or phenotype evidence.",
            "Explicit CARD cross-references and citation/name candidates "
            "retain distinct term-specific scopes.",
            "Unreviewed entries, fragments and multiple same-symbol proteome entries "
            "are retained, not selected as unique loci.",
            "No selected protein is not gene absence or an unsearched term; "
            "four Salmonella terms link to their later qualified review.",
            "Current claims are byte-hash checked; repeated assertion memberships "
            "are not independent biological replicates.",
            "Primary review, curated claims, PHI-base and HIVDB are not reassessed here. "
            "All whole-record reviews remain open.",
        ],
        "shared_symbol_reference_context": pointer("unreviewed", "/shared_symbol_in_same_proteome"),
        "salmonella_taxonomy_context": pointer("salmonella", "/taxonomy_context"),
        "salmonella_primary_review": pointer("salmonella", "/primary_review"),
        "attribution": {k: data[k]["attribution"] for k in ("base", "reviewed", "unreviewed")},
    }, rows


def read_inputs(root, plan_path=PLAN):
    plan = json.loads((root / plan_path).read_bytes())
    paths = {key: reference.check_pin(root, pin) for key, pin in plan["inputs"].items()}
    data = {key: json.loads(path.read_bytes()) for key, path in paths.items() if path.suffix == ".json"}
    for key in ("census", "ledger"):
        data[key] = progress.read_tsv(paths[key].read_bytes())
    return data, plan, reference.pin(root, root / plan_path)


def check_live_claims(records, result, rows):
    expected = {(c["record_identifier"], c["resistance_index"]): c for c in result["claims"]}
    row_index = {r["identifier"]: r for r in rows}
    require(
        len(expected) == len(result["claims"])
        and len(row_index) == len(rows)
        and set(row_index) == set(records),
        "live record or claim coverage changed",
    )
    observed = set()
    for identifier, record in records.items():
        counts = Counter(owner(c) for c in record["resistance_mechanisms"])
        row = row_index[identifier]
        require(
            counts["PHIBASE"] == row["phi_claims_not_reassessed"]
            and counts["CURATOR"] == row["curator_claims_not_reassessed"],
            "live source counts changed",
        )
        for index, claim in enumerate(record["resistance_mechanisms"]):
            if owner(claim) != "CARD":
                continue
            key = (identifier, index)
            require(
                key in expected
                and expected[key]["aro_id"] == claim["aro_id"]
                and expected[key]["claim_sha256"] == prior.checksum(claim)
                and result["terms"][claim["aro_id"]]["source_label_sha256"]
                == progress.digest(claim["label"].encode()),
                "live CARD assertion content or position changed",
            )
            observed.add(key)
    require(observed == set(expected), "live CARD claim coverage changed")


def build(root, plan_path=PLAN):
    data, plan, plan_pin = read_inputs(root, plan_path)
    result, rows = project(data, plan, plan_pin)
    records, _ = progress.current_records(root, data["census"])
    progress.card_progress(records, data["direct_candidates"], data["ledger"])
    check_live_claims(records, result, rows)
    return result, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result, rows = build(Path.cwd())
    for suffix, body in zip((".json", ".tsv"), prior.render(result, rows), strict=True):
        path = Path(PREFIX + suffix)
        if args.check or path.exists():
            require(path.read_bytes() == body, "successor index does not reproduce")
        else:
            with path.open("xb") as stream:
                stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
