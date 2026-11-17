"""Reconcile three bla-labeled gene references without assigning experimental alleles."""

import argparse
import copy
import json
from collections import Counter, defaultdict
from pathlib import Path

import audit_card_bla_alias_screen as alias
import audit_card_followup_memberships as prior
import audit_card_literature_expansion as literature
import audit_sco1_evidence as sco1
from audit_card_reference_lineages import lineage
from audit_card_topoisomerase_memberships import check_live_claims
from audit_fungamr_cohort import read_source
from audit_vgb_evidence import project_protein

reference, require, registry = prior.reference, prior.require, prior.registry
progress, pointer, rebase, shared = prior.progress, prior.pointer, prior.rebase, prior.shared
PREFIX = "research/2026-10-15-card-bla-memberships"
PLAN = Path(PREFIX + "-plan.json")
SCOPE = "CARD_REFERENCE_INDEX_WITH_NATIVE_BLA_CITATIONS_NOT_EXPERIMENTAL_ALLELES"
QUALIFIED = "UNREVIEWED_BLA_GENE_CITATION_TAXON_REFERENCE_ONLY"
UNSELECTED = prior.UNSELECTED
COLUMNS = {**prior.COLUMNS, QUALIFIED: "unreviewed_bla_citation_reference_claims"}
SELECTED = {
    "Q0GA57": {
        "term": "ARO:3001917",
        "label": "CTX-M-55",
        "pmid": "17449211",
        "doi": "10.1016/j.diagmicrobio.2007.02.005",
        "version": 150,
        "synonyms": ["bla", "blaCTX-M-15", "blaCTX-M-3", "CTX-M-57"],
        "citations": {"journal article": 10, "submission": 27},
    },
    "G3K399": {
        "term": "ARO:3000467",
        "label": "NDM-5",
        "pmid": "21930874",
        "doi": "10.1128/aac.05108-11",
        "version": 95,
        "synonyms": ["blaNDM"],
        "citations": {"journal article": 7, "submission": 13},
    },
}
TERMS = {sco1.TERM, *(r["term"] for r in SELECTED.values())}


def project_reference(entry, taxon):
    accession = entry["primaryAccession"]
    require(accession in SELECTED, "unselected native reference")
    expected = SELECTED[accession]
    nodes, species = lineage(taxon)
    symbols = [g["geneName"]["value"] for g in entry.get("genes", []) if "geneName" in g]
    synonyms = [s["value"] for g in entry.get("genes", []) for s in g.get("synonyms", [])]
    require(
        not {"sequence", "features"} & set(entry)
        and symbols == ["bla" + expected["label"]]
        and synonyms == expected["synonyms"]
        and entry["entryType"] == "UniProtKB unreviewed (TrEMBL)"
        and entry["entryAudit"] == {"entryVersion": expected["version"], "sequenceVersion": 1}
        and all(type(v) is int for v in entry["entryAudit"].values())
        and entry["uniProtKBCrossReferences"] == []
        and entry.get("proteinDescription", {}).get("flag") is None
        and entry["organism"]["taxonId"] == taxon["taxonId"] == 562
        and entry["organism"]["scientificName"] == taxon["scientificName"] == "Escherichia coli"
        and taxon["rank"] == "species"
        and taxon["active"] is True
        and species == nodes[-1],
        "native gene, synonyms, version or taxonomy changed",
    )
    bibliography, focal = [], []
    for item in entry["references"]:
        citation = item["citation"]
        ids = citation.get("citationCrossReferences", [])
        row = {
            "reference_number": item["referenceNumber"],
            "citation_type": citation["citationType"],
            "native_citation_sha256": registry.checksum(citation),
            "focal_source_citation": any(
                i["database"] == "PubMed" and i["id"] == expected["pmid"] for i in ids
            ),
        }
        if row["focal_source_citation"]:
            pmids = [i["id"] for i in ids if i["database"] == "PubMed"]
            dois = [i["id"].lower() for i in ids if i["database"] == "DOI"]
            require(
                pmids == [expected["pmid"]]
                and dois == [expected["doi"]]
                and citation["citationType"] == "journal article"
                and expected["label"] in citation["title"],
                "focal native bibliography changed",
            )
            focal.append(
                {
                    "reference_number": item["referenceNumber"],
                    "pmid": "PMID:" + expected["pmid"],
                    "doi": "DOI:" + expected["doi"],
                    "native_title": citation["title"],
                }
            )
        bibliography.append(row)
    require(
        len(focal) == 1
        and focal[0]["reference_number"] == 1
        and [r["reference_number"] for r in bibliography] == list(range(1, len(bibliography) + 1))
        and dict(Counter(r["citation_type"] for r in bibliography)) == expected["citations"],
        "native bibliography coverage changed",
    )
    return {
        **project_protein(entry),
        "source_term_id": expected["term"],
        "source_label": expected["label"],
        "native_reference_taxon_rank": "species",
        "native_synonyms": synonyms,
        "synonyms_establish_equivalent_alleles": False,
        "different_allele_style_synonyms_present": accession == "Q0GA57",
        "all_native_citations_accounted": bibliography,
        "matched_source_bibliography": focal,
        "nonfocal_citations_are_independent_primary_reviews": False,
        "explicit_card_xref": False,
        "global_bla_prefix_normalization_enabled": False,
        "native_protein_flag": None,
        "unflagged_means_complete": False,
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
        "experimental_genome_assignment": None,
        "primary_results_reviewed": False,
        "scope": QUALIFIED,
    }


def read_inputs(root, plan_path=PLAN):
    data, plan, pin = shared.read_inputs(root, plan_path)
    data["native_taxon"], data["native_taxonomy_source"] = read_source(
        root, {"wrapper": plan["inputs"]["taxonomy"], "url": "https://rest.uniprot.org/taxonomy/562"}
    )
    data["native_queries"] = {}
    for row in SELECTED.values():
        pmid = row["pmid"]
        body = reference.check_pin(root, plan["inputs"]["query_" + pmid])
        entries, query = literature.read_query(root, body.parent, pmid)
        require(
            query["complete_for_query"] is True
            and query["release"] == "2026_03"
            and len(query["pages"]) == 1
            and query["pages"][0]["cache"] == plan["inputs"]["query_" + pmid]
            and query["pages"][0]["receipt"] == plan["inputs"]["receipt_" + pmid]
            and len(entries) == 1,
            "native query identity or completeness changed",
        )
        data["query_" + pmid] = json.loads(body.read_bytes())
        data["native_queries"][pmid] = query
    return data, plan, pin


def reconcile_rows(data, result):
    census = progress.index_unique(data["census"], "identifier", "census")
    old_rows = progress.index_unique(data["base_rows"], "identifier", "prior row")
    require(set(census) == set(old_rows), "row coverage changed")
    old_claims, new_claims = defaultdict(list), defaultdict(list)
    for old, new in zip(data["base"]["claims"], result["claims"], strict=True):
        require({**new, "reference_status": old["reference_status"]} == old, "claim identity changed")
        old_claims[old["record_identifier"]].append(old)
        new_claims[new["record_identifier"]].append(new)
    rows = []
    for rid, record in sorted(census.items()):
        old = old_rows[rid]
        counts = Counter(c["reference_status"] for c in old_claims[rid])

        def accessions(index, rid=rid):
            return "|".join(
                sorted(
                    {
                        link["protein_accession"]
                        for c in old_claims[rid]
                        for link in index["terms"][c["aro_id"]]["links"]
                    }
                )
            )

        require(
            all(old[k] == record[k] for k in ("path", "record_sha256", "standard_inchi_key"))
            and int(old["card_assertions"]) == len(old_claims[rid])
            and all(int(old[col]) == counts[status] for status, col in prior.COLUMNS.items())
            and old["selected_reference_accessions"] == accessions(data["base"])
            and old["whole_record_primary_review"] == "OPEN",
            "prior row identity or accounting changed",
        )
        numeric = {
            *prior.COLUMNS.values(),
            "card_assertions",
            "phi_claims_not_reassessed",
            "curator_claims_not_reassessed",
            "score_rules_not_reassessed",
        }
        row = {k: int(v) if k in numeric else v for k, v in old.items()}
        counts = Counter(c["reference_status"] for c in new_claims[rid])
        row.update({col: counts[status] for status, col in COLUMNS.items()})
        row["selected_reference_accessions"] = accessions(result)
        require(
            sum(row[c] for c in COLUMNS.values()) == row["card_assertions"]
            and row["card_assertions"]
            + row["phi_claims_not_reassessed"]
            + row["curator_claims_not_reassessed"]
            == int(record["resistance_assertions"])
            and row["score_rules_not_reassessed"] == int(record["score_rules"]),
            "source accounting changed",
        )
        rows.append(row)
    return rows


def project(data, plan, plan_pin):
    base, discovery, sco = data["base"], data["alias_screen"], data["sco1"]
    require(
        plan["selection"] == "ALL_CARD_MEMBERSHIPS_WITH_THREE_BLA_GENE_REFERENCE_TERMS"
        and plan["constraints"]
        == {
            "network_requests": 0,
            "biological_writes": False,
            "experimental_assignments": False,
            "issue_1040": "DEFERRED",
        }
        and base["scope"] == prior.SCOPE
        and base["plan"] == plan["inputs"]["base_plan"]
        and base["inputs"] == data["base_plan"]["inputs"]
        and discovery["scope"] == alias.SCOPE
        and sco["scope"] == sco1.SCOPE
        and discovery["inputs"]["index"] == plan["inputs"]["base"]
        and sco["inputs"]["index"] == plan["inputs"]["base"]
        and not any(sco["disposition"].values())
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
        "index provenance or evidence scope changed",
    )
    for key in (
        "census",
        "curator",
        "source_queue",
        "source_inventory",
        "direct_candidates",
        "ledger",
        "definition_citations",
    ):
        require(plan["inputs"][key] == base["inputs"][key], "source pin changed")
    for name in ("base", "alias_screen", "sco1"):
        shared.check_checkpoint(data, plan, name)
    claims = [c for c in base["claims"] if c["aro_id"] in TERMS]
    require(
        Counter(map(registry.checksum, claims)) == Counter(map(registry.checksum, discovery["claims"]))
        and len(claims) == 13
        and {r["identifier"] for r in discovery["records"]} == {c["record_identifier"] for c in claims}
        and all(r in data["census"] for r in discovery["records"])
        and discovery["primary_access_hold"]["http_status"] == 403
        and discovery["primary_access_hold"]["revisit_requires"]
        == "USER_SUPPLIED_PRIMARY_COPY_OR_NEW_EXPLICIT_DIRECTION",
        "complete discovery membership or access hold changed",
    )
    result = rebase(base)
    reviewed = {}
    sources, queries = {}, {}
    for accession, expected in SELECTED.items():
        pmid = expected["pmid"]
        (entry,) = data["query_" + pmid]["results"]
        require(entry["primaryAccession"] == accession, "query accession changed")
        row = project_reference(entry, data["native_taxon"])
        tid, curie = expected["term"], "UniProtKB:" + accession
        candidate = discovery["candidates"][tid + "|" + accession]
        require(
            data["definition_citations"]["terms"][tid]["definition_citation_ids"] == ["PMID:" + pmid]
            and candidate["identity"]["protein_accession"] == curie
            and candidate["identity"]["source_label"] == expected["label"]
            and candidate["native_citation_and_taxonomy_review_pending"] is True
            and candidate["previously_reviewed_reference"] is False
            and candidate["experimental_subject_assignment"] is False
            and candidate["record_memberships"] == base["terms"][tid]["record_memberships"]
            and candidate["query_pmids"] == [pmid]
            and data["native_queries"][pmid] == discovery["queries"][pmid]["query"],
            "discovery and native source context disagree",
        )
        reviewed[curie] = row
        sources[curie] = pointer("query_" + pmid, "results", 0)
        queries[curie] = pointer("alias_screen", "queries", pmid, "query")
    require(set(sco["references"]) == {"UniProtKB:" + a for a in sco1.SELECTED}, "SCO-1 coverage changed")
    for accession, row in sco["references"].items():
        require(
            row["source_term_id"] == sco1.TERM
            and row["gene_symbols"] == ["blaSCO-1"]
            and row["scope"] == "UNREVIEWED_GENE_CITATION_TAXON_REFERENCE_ONLY"
            and row["experimental_allele_assignment"] is row["experimental_genome_assignment"] is None
            and all(
                row[k] is False
                for k in (
                    "explicit_card_xref",
                    "experimental_subject_assignment",
                    "exact_allele_assignment",
                    "primary_results_reviewed",
                    "global_bla_prefix_normalization_enabled",
                )
            ),
            "SCO-1 reference scope changed",
        )
        reviewed[accession] = row
        sources[accession] = pointer("sco1", "references", accession)
        queries[accession] = pointer("sco1", "literature_queries")
    memberships = []
    for tid in TERMS:
        require(not result["terms"][tid]["links"], "prior term already has references")
    for accession, row in sorted(reviewed.items()):
        tid = row["source_term_id"]
        require(
            accession not in result["proteins"]
            and progress.digest(row["source_label"].encode()) == base["terms"][tid]["source_label_sha256"],
            "duplicate reference or source-label mismatch",
        )
        identity = registry.reference_identity(
            {
                "entry_type": row["entry_type"],
                "entry_version": row["entry_audit"]["entryVersion"],
                "sequence_version": row["entry_audit"]["sequenceVersion"],
                "reference_taxon_id": row["reference_taxon_id"],
                "reference_taxon_rank": row["native_reference_taxon_rank"],
                "reference_species_taxon_id": row["reference_taxon_id"],
                "experimental_subject_assignment": False,
                "exact_allele_assignment": False,
            }
        )
        result["proteins"][accession] = {
            "identity": identity,
            "sources": [sources[accession]],
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
        bibliography = row.get("matched_source_bibliography", row.get("bibliography"))
        result["terms"][tid]["links"].append(
            {
                "protein_accession": accession,
                "kind": QUALIFIED,
                "explicit_card_xref": False,
                "source_citation_ids": [b["pmid"] for b in bibliography],
                "matched_reference_numbers": [b["reference_number"] for b in bibliography],
                "source": sources[accession],
                "query": queries[accession],
                "experimental_subject_assignment": False,
                "exact_allele_assignment": False,
            }
        )
        result["terms"][tid]["reference_status"] = QUALIFIED
        memberships.extend(
            {
                "record_identifier": rid,
                "source_term_id": tid,
                "protein_accession": accession,
                "scope": QUALIFIED,
                "experimental_subject_assignment": False,
            }
            for rid in base["terms"][tid]["record_memberships"]
        )
    for claim in result["claims"]:
        claim["reference_status"] = result["terms"][claim["aro_id"]]["reference_status"]
    rows = reconcile_rows(data, result)
    result.update(
        {
            "date": plan["date"],
            "scope": SCOPE,
            "plan": plan_pin,
            "inputs": plan["inputs"],
            "proteins": dict(sorted(result["proteins"].items())),
            "new_native_reference_reviews": {
                a: r for a, r in reviewed.items() if a.removeprefix("UniProtKB:") in SELECTED
            },
            "new_native_taxonomy_source": data["native_taxonomy_source"],
            "new_reference_memberships": memberships,
            "sco1_reference_context": {"input": "sco1", "pointer": ""},
            "primary_access_hold": pointer("alias_screen", "primary_access_hold"),
            "prior_interpretation": pointer("base", "interpretation"),
            "interpretation": [
                "Three terms gain four unreviewed reference links across 21 existing claim memberships, "
                "not AST results.",
                "Native gene labels, source-cited bibliography and species taxonomy "
                "support reference identity only.",
                "Q0GA57 carries different allele-style synonyms; these are retained, "
                "not equated or assigned to experiments.",
                "No general bla-prefix alias normalization is enabled.",
                "Native bibliography metadata is not independent primary-results review; "
                "remaining citations are only accounted.",
                "SCO-1 primary access remains held after a 403 challenge; "
                "no alternate route or retry was used.",
                "All prior holds, non-CARD claims and no-claim records remain; "
                "candidate-free means selected-input coverage only.",
            ],
            "attribution": {
                "base": base["attribution"],
                "sco1": sco["attribution"],
                "native_references": "CARD/ARO ontology: McMaster University, CC BY 4.0. "
                "UniProt Consortium metadata, release 2026_03. No primary text exported.",
            },
            "summary": {
                **copy.deepcopy(base["summary"]),
                "selected_reference_terms": sum(bool(t["links"]) for t in result["terms"].values()),
                "selected_reference_proteins": len(result["proteins"]),
                "reference_links": sum(len(t["links"]) for t in result["terms"].values()),
                "term_statuses": dict(
                    sorted(Counter(t["reference_status"] for t in result["terms"].values()).items())
                ),
                "claim_statuses": dict(
                    sorted(Counter(c["reference_status"] for c in result["claims"]).items())
                ),
                "records_with_selected_references": sum(
                    bool(r["selected_reference_accessions"]) for r in rows
                ),
                "added_reference_terms": len(TERMS),
                "added_reference_proteins": len(reviewed),
                "added_reference_links": len(reviewed),
                "added_reference_memberships": len(memberships),
                "newly_checked_native_reference_entries": 2,
                "reconciled_prior_reference_entries": 2,
                "followup_terms": len(TERMS),
                "followup_claims": len(claims),
                "followup_records": len(discovery["records"]),
                "new_cohort_summaries": {
                    "native_citations_accounted": 57,
                    "focal_native_citations_matched": 2,
                    "new_primary_results_reviews": 0,
                    "new_taxonomy_nodes_requested": 0,
                },
            },
        }
    )
    return result, rows


def build(root, plan_path=PLAN):
    data, plan, pin = read_inputs(root, plan_path)
    base, rows = prior.build(root, Path(plan["inputs"]["base_plan"]["path"]))
    require(
        base == data["base"]
        and registry.render(base, rows)[1]
        == reference.check_pin(root, plan["inputs"]["base_rows"]).read_bytes(),
        "prior index does not reproduce",
    )
    require(alias.build(root) == data["alias_screen"], "native discovery does not reproduce")
    require(sco1.build(root) == data["sco1"], "native SCO-1 review does not reproduce")
    result, rows = project(data, plan, pin)
    records, _ = progress.current_records(root, data["census"])
    check_live_claims(records, result, rows)
    return result, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output-prefix", default=PREFIX)
    args = parser.parse_args()
    result, rows = build(Path.cwd())
    missing = []
    for suffix, body in zip((".json", ".tsv"), registry.render(result, rows), strict=True):
        path = Path(args.output_prefix + suffix)
        if args.check or path.exists():
            require(path.read_bytes() == body, "bla reference index does not reproduce")
        else:
            missing.append((path, body))
    for path, body in missing:
        with path.open("xb") as stream:
            stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
