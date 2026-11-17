"""Bind QnrC's deposited-gene reference without making the Qnr family one protein."""

import argparse
import copy
import hashlib
import json
from pathlib import Path

import audit_bla_primary_identifiers as native
import audit_card_literature_proteins as literature
import audit_card_reference_lineages as taxonomy
import audit_card_reference_memberships as registry
import audit_card_source_aliases as aliases
import audit_sal_reference_context as safety
from audit_curator_resistance_fields import owner
from rdflib import RDFS, URIRef

from antibioticmech.activity_collections import load_record

reference, require = native.reference, native.require
PREFIX = "research/2026-10-16-qnr-identity-context"
PLAN, AUDIT_PLAN = Path(PREFIX + "-plan.json"), Path(PREFIX + "-audit-plan.json")
NATIVE, OUTPUT = Path(PREFIX + "-native.json"), Path(PREFIX + ".json")
CACHE = Path("reports/qnr-parent-followup-2026-10-16")
PARENT, CHILD, ACCESSION = "ARO:3000419", "ARO:3002787", "UniProtKB:C0J7J6"
TERMS = {PARENT, CHILD}
SCOPE = "QNR_FAMILY_MEMBER_AND_QNRC_DEPOSIT_CONTEXT_NOT_EXPERIMENTAL_GROUNDING"


def read(root, pin):
    return json.loads(reference.check_pin(root, pin).read_bytes())


def inputs(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["constraints"]
        == {
            "planned_new_requests": 1,
            "ncbi_requests": 0,
            "retries": 0,
            "redirects_followed": 0,
            "issue_1040": "DEFERRED",
            "biological_record_writes": False,
            "experimental_identifiers_assigned": False,
            "new_reference_selection": False,
            "full_investigation_complete": False,
        },
        "research scope changed",
    )
    for pin in plan["inputs"].values():
        reference.check_pin(root, pin)
    data = {k: read(root, p) for k, p in plan["inputs"].items() if p["path"].endswith(".json")}
    require(
        data["current_verification"]["artifacts"]["dossier"] == plan["inputs"]["current_index"],
        "unverified predecessor index",
    )
    return plan, data


def project_entry(entry):
    safety.metadata_only(entry)
    return {
        "accession": "UniProtKB:" + entry["primaryAccession"],
        "entry_type": entry["entryType"],
        "versions": entry["entryAudit"],
        "gene_names": [g["geneName"]["value"] for g in entry.get("genes", []) if "geneName" in g],
        "organism": {k: entry["organism"][k] for k in ("taxonId", "scientificName")},
        "embl": [x for x in entry.get("uniProtKBCrossReferences", []) if x["database"] == "EMBL"],
        "citations": [
            {
                "reference_number": r["referenceNumber"],
                "identifiers": r["citation"].get("citationCrossReferences", []),
                "source_strains": [
                    c["value"] for c in r.get("referenceComments", []) if c["type"] == "STRAIN"
                ],
            }
            for r in entry.get("references", [])
            if r["citation"]["citationType"] == "journal article"
        ],
    }


def capture(root):
    plan, data = inputs(root)
    key = "qnr-deposit"
    receipt_path, attempt_path = [
        root / CACHE / (key + suffix) for suffix in ("-receipt.json", "-attempt.json")
    ]
    receipt, attempt = [json.loads(p.read_bytes()) for p in (receipt_path, attempt_path)]
    require(receipt["plan_sha256"] == reference.digest(root / PLAN), "request plan changed")
    body = reference.check_pin(root, receipt["body"]).read_bytes()
    entries, suggestions = native.validate_response(plan, key, receipt, attempt, body)
    require(not suggestions, "unreviewed query suggestions")
    old, query = literature.read_query(root, root / literature.DEFAULT_DIRECTORY, "19258263")
    require(query == data["literature"]["queries"]["19258263"], "historical citation query changed")
    require({e["primaryAccession"] for e in entries} == set(old), "deposit/citation membership differs")
    for entry in entries:
        prior = old[entry["primaryAccession"]]
        require(
            {k: v for k, v in entry.items() if k != "uniProtKBCrossReferences"}
            == {k: v for k, v in prior.items() if k != "uniProtKBCrossReferences"},
            "shared native metadata conflicts",
        )
    graph = aliases.ontology_graph(root, data["definitions"])

    def node(term):
        return URIRef(aliases.definitions.ontology.BASE + term.removeprefix("ARO:"))

    children = sorted(
        "ARO:" + str(n).removeprefix(aliases.definitions.ontology.BASE)
        for n in graph.subjects(RDFS.subClassOf, node(PARENT))
        if isinstance(n, URIRef) and str(n).startswith(aliases.definitions.ontology.BASE)
    )
    require(
        children == data["prior_parent_context"]["terms"][PARENT]["named_direct_subclass_ids"],
        "direct family membership changed",
    )
    require(CHILD in children and "ARO:3003035" in children, "named child edge missing")
    snapshot = read(root, plan["native_taxonomy_snapshot"])
    taxon = snapshot["taxa"]["584"]
    url = "https://rest.uniprot.org/taxonomy/584"
    key_hash = hashlib.sha256(json.dumps([url, None], sort_keys=True).encode()).hexdigest()
    tax_path = root / Path(plan["native_taxonomy_snapshot"]["path"]).parent / f"request-{key_hash}.json"
    tax_native, tax_source = taxonomy.native_taxon(
        root, {"receipt": reference.pin(root, tax_path), "body": None}, "584", plan["release"]
    )
    require(taxon == tax_native, "taxonomy aggregate differs from native response")
    return {
        "request_plan": reference.pin(root, root / PLAN),
        "query": {
            "query": plan["requests"][key]["query"],
            "url": receipt["url"],
            "release": plan["release"],
            "result_count": len(entries),
            "complete_for_query": True,
            "receipt": reference.pin(root, receipt_path),
            "attempt": reference.pin(root, attempt_path),
            "body": receipt["body"],
            "retrieved_at": receipt["retrieved_at"],
        },
        "entries": sorted([project_entry(e) for e in entries], key=lambda e: e["accession"]),
        "prior_citation_query": query,
        "ontology": {
            "source": data["definitions"]["ontology"],
            "direct_named_child_count": len(children),
            "verified_edges": [
                {"child": c, "predicate": str(RDFS.subClassOf), "parent": PARENT}
                for c in [CHILD, "ARO:3003035"]
            ],
        },
        "taxonomy_source": tax_source,
        "taxonomy": {
            k: taxon[k] for k in ("taxonId", "scientificName", "active", "rank", "parent", "lineage")
        },
    }


def select_member(projection, assessment):
    require(
        assessment["new_ncbi_requests"] == 0
        and assessment["issue_1040"] == "DEFERRED"
        and all(
            assessment[k] is False
            for k in (
                "experimental_identifiers_assigned",
                "numeric_ast_exported",
                "sequences_exported",
                "variant_specifications_exported",
                "constructs_or_protocols_exported",
            )
        ),
        "assessment scope changed",
    )
    primary = assessment["primary"]
    require(
        primary["gene"] == "qnrC"
        and primary["source_reported_nucleotide_accession"] == "EU917444"
        and primary["reference"] == "PMID:19258263"
        and primary["doi"] == "DOI:10.1128/AAC.01400-08"
        and primary["source_organism"] == "Proteus mirabilis"
        and primary["source_isolate"] == "06-489"
        and primary["source_quinolone_category"] == "SUSCEPTIBLE",
        "primary identity or category changed",
    )
    require(
        all(
            primary[k] is True
            for k in (
                "native_carriage_is_not_resistant_taxon_evidence",
                "heterologous_host_results_are_separate",
                "qnrC_is_named_member_not_whole_family_identity",
            )
        )
        and all(
            primary[k] is False
            for k in (
                "all_inherited_compounds_verified",
                "native_body_cached",
                "tables_reviewed",
                "figures_reviewed",
                "supplements_reviewed",
                "whole_paper_signoff",
            )
        ),
        "primary evidence scope promoted",
    )
    taxon = projection["taxonomy"]
    _, species = taxonomy.lineage(taxon)
    require(
        species == taxonomy.identity(taxon)
        and taxon["taxonId"] == 584
        and taxon["rank"] == "species"
        and taxon["scientificName"] == primary["source_organism"],
        "species context changed",
    )
    entries = projection["entries"]
    require(
        len(entries) == len({e["accession"] for e in entries}) == projection["query"]["result_count"] == 4
        and {e["accession"] for e in entries}
        == {"UniProtKB:C0J7J4", "UniProtKB:C0J7J5", ACCESSION, "UniProtKB:C0J7J7"}
        and projection["query"]["complete_for_query"] is True
        and projection["query"]["query"] == "xref:embl-EU917444"
        and projection["query"]["release"] == "2026_03",
        "deposit query coverage changed",
    )
    candidates = [e for e in entries if primary["gene"] in e["gene_names"]]
    require(
        len(candidates) == 1
        and candidates[0]["accession"] == ACCESSION
        and candidates[0]["gene_names"] == [primary["gene"]],
        "ambiguous gene reference",
    )
    entry = candidates[0]
    require(
        entry["organism"] == {k: taxon[k] for k in ("taxonId", "scientificName")},
        "reference organism mismatch",
    )
    require(
        entry["embl"]
        == [
            {
                "database": "EMBL",
                "id": "EU917444",
                "properties": [
                    {"key": "ProteinId", "value": "ACK75961.1"},
                    {"key": "Status", "value": "-"},
                    {"key": "MoleculeType", "value": "Genomic_DNA"},
                ],
            }
        ],
        "deposition protein crosswalk changed",
    )
    papers = [
        r
        for r in entry["citations"]
        if {("PubMed", "19258263"), ("DOI", "10.1128/AAC.01400-08")}
        <= {(x["database"], x["id"]) for x in r["identifiers"]}
    ]
    require(
        len(papers) == 1 and papers[0]["source_strains"] == [primary["source_isolate"]],
        "own-citation strain mismatch",
    )
    require(
        projection["ontology"]["direct_named_child_count"] == 110
        and {"child": CHILD, "predicate": str(RDFS.subClassOf), "parent": PARENT}
        in projection["ontology"]["verified_edges"],
        "explicit family-member edge missing",
    )
    identity = registry.reference_identity(
        {
            "entry_type": entry["entry_type"],
            "entry_version": entry["versions"]["entryVersion"],
            "sequence_version": entry["versions"]["sequenceVersion"],
            "reference_taxon_id": "NCBITaxon:584",
            "reference_species_taxon_id": "NCBITaxon:584",
            "reference_taxon_rank": "species",
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
        }
    )
    return {
        "accession": ACCESSION,
        "identity": identity,
        "gene": "qnrC",
        "member_aro_id": CHILD,
        "scope": "PRIMARY_NAMED_QNRC_MEMBER_REFERENCE_NOT_WHOLE_QNR_FAMILY_OR_TESTED_ALLELE",
        "source_nucleotide_cross_reference": "EU917444",
        "source_protein_cross_reference": "ACK75961.1",
        "own_citation": papers[0],
        "source_isolate_label": primary["source_isolate"],
        "single_protein_identity_for_whole_family": False,
        "native_isolate_resistance_inferred": False,
        "new_whole_corpus_reference_selection": False,
        "experimental_protein_assignment": None,
        "experimental_allele_assignment": None,
        "experimental_strain_taxon_assignment": None,
        "experimental_genome_assignment": None,
    }


def build(root):
    plan, data = inputs(root)
    audit = json.loads((root / AUDIT_PLAN).read_bytes())
    require(audit["request_plan"] == reference.pin(root, root / PLAN), "audit/request plan mismatch")
    projection = read(root, audit["projection"])
    require(projection["request_plan"] == audit["request_plan"], "projection plan mismatch")
    member = select_member(projection, data["assessment"])
    index = data["current_index"]
    require(
        member["identity"] == index["proteins"][ACCESSION]["identity"],
        "deposition crosswalk disagrees with existing reference identity",
    )
    expected = {r["path"]: r["record_sha256"] for r in index["records"]}
    actual = {
        p.relative_to(root).as_posix(): reference.digest(p)
        for p in (root / "data/antibiotics").rglob("*.yaml")
    }
    require(len(actual) == 2939 and actual == expected, "current corpus changed")
    rows = [r for r in index["records"] if TERMS.intersection(r["card_terms"])]
    claims = [c for c in index["claims"] if c["aro_id"] in TERMS]
    docs = {r["identifier"]: load_record(root / r["path"]) for r in rows}
    require(len(rows) == 7 and len(claims) == 8, "source cohort changed")
    for claim in claims:
        doc = docs[claim["record_identifier"]]
        item = doc["resistance_mechanisms"][claim["resistance_index"]]
        require(
            owner(item) == "CARD"
            and item["aro_id"] == claim["aro_id"]
            and registry.checksum(item) == claim["claim_sha256"]
            and doc["chemical_structure"]["standard_inchi_key"] == claim["standard_inchi_key"],
            "claim identity changed",
        )
    terms = {}
    for term in sorted(TERMS):
        old = index["terms"][term]
        require(
            data["definitions"]["terms"][term]["label_sha256"] == old["source_label_sha256"],
            "source label changed",
        )
        require(
            old["record_memberships"] == data["definitions"]["terms"][term]["record_memberships"],
            "membership changed",
        )
        require(
            old["reference_accessions"] == ([] if term == PARENT else [ACCESSION]),
            "preexisting reference changed",
        )
        terms[term] = {
            "record_memberships": old["record_memberships"],
            "prior_reference_accessions": old["reference_accessions"],
            "named_member_reference": copy.deepcopy(member),
            "whole_record_primary_review": "OPEN",
            "experimental_allele_assignment": None,
            "experimental_protein_assignment": None,
            "experimental_taxon_assignment": None,
            "experimental_genome_assignment": None,
        }
    result = {
        "scope": SCOPE,
        "date": "2026-10-16",
        "inputs": plan["inputs"],
        "audit_plan": reference.pin(root, root / AUDIT_PLAN),
        "projection": audit["projection"],
        "records": rows,
        "claims": claims,
        "terms": terms,
        "primary_assessment": data["assessment"],
        "native_taxonomy": {"584": projection["taxonomy"]},
        "excluded_same_deposit_entries": [e for e in projection["entries"] if e["accession"] != ACCESSION],
        "exclusion_scope": "OTHER_DEPOSIT_PROTEINS_NOT_QNRC_IDENTITY_NOT_GLOBAL_FUNCTIONAL_ABSENCE",
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_loaded": 7,
            "source_claims_bound": 8,
            "named_member_crosswalks_verified": 1,
            "other_deposit_proteins_excluded": 3,
            "new_uniprot_requests": 1,
            "new_taxonomy_requests": 0,
            "new_reference_selections": 0,
            "experimental_identifiers_assigned": 0,
            "whole_record_primary_signoffs": 0,
            "current_selected_reference_terms": 1405,
            "current_unresolved_reference_terms": 597,
        },
        "constraints": plan["constraints"],
    }
    safety.metadata_only(result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture", action="store_true", help="project existing local caches, no network")
    parser.add_argument("--write", action="store_true", help="write research output only")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = capture(args.root) if args.capture else build(args.root)
    path = args.root / (NATIVE if args.capture else OUTPUT)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.write:
        with path.open("x") as stream:
            stream.write(text)
    else:
        require(path.read_text() == text, "research export drift")
    print(json.dumps({"path": str(path), "sha256": reference.digest(path), "summary": result.get("summary")}))


if __name__ == "__main__":
    main()
