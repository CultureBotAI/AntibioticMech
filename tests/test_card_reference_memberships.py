"""Reference links retain per-term provenance and cannot promote experimental scope."""

import copy
import json
import socket
import sys
from collections import Counter, defaultdict
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_reference_memberships as audit  # noqa: E402

CURATOR_PIN = {
    "path": "research/2026-10-14-antiviral-taxa-curator-resistance-fields.json",
    "sha256": "0a15457ee90614e9c202dae5b2c54a356b748533c4d0a0618cf4147563de6460",
}


def assert_public_projection(result, rows, census, ledger, curator):
    assert curator["census"] == result["inputs"]["census"]
    assert len(census) == len({r["identifier"] for r in census})
    assert len(rows) == len(census) == len({r["identifier"] for r in rows})
    by_record = defaultdict(list)
    for claim in ledger:
        by_record[claim["identifier"]].append(claim["aro_id"])
    curated = Counter(c["record_identifier"] for c in curator["claims"])
    expected = []
    for record in sorted(census, key=lambda r: r["identifier"]):
        identifier = record["identifier"]
        terms = [result["terms"][tid] for tid in by_record[identifier]]
        statuses = Counter(t["reference_status"] for t in terms)
        references = {link["protein_accession"] for t in terms for link in t["links"]}
        phi = int(record["resistance_assertions"]) - len(terms) - curated[identifier]
        assert phi >= 0
        expected.append({
            **{k: record[k] for k in ("identifier", "path", "record_sha256", "standard_inchi_key")},
            "card_assertions": str(len(terms)),
            "direct_xref_claims": str(statuses[audit.DIRECT]),
            "citation_candidate_claims": str(statuses[audit.CITATION]),
            "unselected_candidate_claims": str(statuses[audit.UNSELECTED]),
            "selected_reference_accessions": "|".join(sorted(references)),
            "phi_claims_not_reassessed": str(phi),
            "curator_claims_not_reassessed": str(curated[identifier]),
            "score_rules_not_reassessed": record["score_rules"],
            "whole_record_primary_review": "OPEN",
        })
    assert rows == expected
    terms, proteins = result["terms"], result["proteins"]
    assert result["summary"] == {
        "corpus_records": len(census),
        "card_assertions": len(ledger),
        "card_terms": len(terms),
        "selected_reference_terms": sum(bool(t["links"]) for t in terms.values()),
        "selected_reference_proteins": len(proteins),
        "reference_links": sum(len(t["links"]) for t in terms.values()),
        "accessions_shared_between_cohorts": sum(len(p["sources"]) == 2 for p in proteins.values()),
        "term_statuses": dict(Counter(t["reference_status"] for t in terms.values())),
        "claim_statuses": dict(Counter(terms[r["aro_id"]]["reference_status"] for r in ledger)),
        "records_with_selected_references": sum(bool(r["selected_reference_accessions"]) for r in expected),
        "records_without_card_assertions": sum(r["card_assertions"] == "0" for r in expected),
        "other_source_claims_not_reassessed": sum(
            int(r["phi_claims_not_reassessed"]) + int(r["curator_claims_not_reassessed"]) for r in expected),
        "score_rules_not_reassessed": sum(int(r["score_rules"]) for r in census),
        "whole_record_primary_signoffs": 0,
    }


@pytest.fixture
def public_projection():
    result = json.loads((ROOT / (audit.PREFIX + ".json")).read_bytes())
    rows = audit.progress.read_tsv((ROOT / (audit.PREFIX + ".tsv")).read_bytes())
    census, ledger = [audit.progress.read_tsv(
        audit.reference.check_pin(ROOT, result["inputs"][key]).read_bytes()) for key in ("census", "ledger")]
    curator = json.loads(audit.reference.check_pin(ROOT, CURATOR_PIN).read_bytes())
    return result, rows, census, ledger, curator


@pytest.mark.parametrize("field", [
    "path", "standard_inchi_key", "record_sha256", "card_assertions", "direct_xref_claims",
    "citation_candidate_claims", "unselected_candidate_claims", "selected_reference_accessions",
    "phi_claims_not_reassessed", "curator_claims_not_reassessed", "score_rules_not_reassessed",
    "whole_record_primary_review", "summary", "duplicate_row", "extra_protein",
])
def test_public_projection_rejects_mutated_fields(public_projection, field):
    result, rows, *_ = public_projection
    assert_public_projection(*public_projection)
    if field == "summary":
        result["summary"]["card_assertions"] += 1
    elif field == "duplicate_row":
        rows[0] = copy.deepcopy(rows[1])
    elif field == "extra_protein":
        result["proteins"]["UniProtKB:UNEXPECTED"] = {"sources": []}
    else:
        rows[0][field] = "CORRUPTED"
    with pytest.raises(AssertionError):
        assert_public_projection(*public_projection)


@pytest.fixture
def cohorts():
    protein = {
        "entry_type": "UniProtKB reviewed (Swiss-Prot)", "entry_version": 2, "sequence_version": 1,
        "reference_taxon_id": "NCBITaxon:20", "reference_taxon_rank": "strain",
        "reference_species_taxon_id": "NCBITaxon:10", "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
    }
    context = {"reference_number": 1, "citation_identifiers": ["PMID:1"],
               "experimental_subject_assignment": False, "primary_review_completed_by_this_audit": False}
    literature_protein = {
        **protein, "accession": "UniProtKB:P00001", "taxonomy_identity_verified": True,
        "taxonomy_rank": "strain", "reference_species_lineage": {
            "taxon_id": "NCBITaxon:10", "rank": "species", "experimental_subject_assignment": False},
        "reference_contexts": [context], "gene_names_and_synonyms": ["example"],
    }
    candidate = {
        "protein_accession": "UniProtKB:P00001", "source_citation_ids": ["PMID:1"],
        "literal_gene_matches": [{"field": "geneName", "value": "example"}],
        "matched_study_contexts": [copy.deepcopy(context)], "explicit_card_xref": False,
        "experimental_subject_assignment": False, "exact_allele_assignment": False,
        "primary_review_completed_by_this_audit": False,
    }
    base = {"determinants": {
        "ARO:1": {"labels": ["example"], "candidates": [{
            "accession": "UniProtKB:P00001", "card_cross_reference": {"database": "CARD", "id": "ARO:1"},
            "evidence_scope": "EXPLICIT_REFERENCE_LINK_NOT_EXPERIMENTAL_ALLELE_GROUNDING",
            "entry_audit": {"entryVersion": 2, "sequenceVersion": 1},
            "reference_taxon_id": "NCBITaxon:20", "taxonomy_rank": "strain",
            "entry_type": protein["entry_type"],
        }]},
        "ARO:2": {"labels": ["example"], "candidates": []},
        "ARO:3": {"labels": ["unselected"], "candidates": []},
    }}
    direct = {"proteins": {"UniProtKB:P00001": protein}, "terms": {"ARO:1": {
        "source_label_sha256": audit.progress.digest(b"example"), "experimental_subject_assignment": False,
        "record_memberships": ["CHEBI:1"], "reference_accessions": ["UniProtKB:P00001"],
    }}}
    literature = {"proteins": {"UniProtKB:P00001": literature_protein}, "terms": {"ARO:2": {
        "source_label": "example", "definition_citation_ids": ["PMID:1"],
        "record_memberships": ["CHEBI:1"], "reference_candidates": [candidate],
        "whole_record_primary_review": "OPEN",
    }}}
    scopes = {"terms": {tid: {"entity_scope": "UNRESOLVED"} for tid in base["determinants"]}}
    return base, direct, literature, scopes, {"terms": {}}


def test_shared_accession_does_not_transfer_cross_reference_to_another_term(cohorts):
    _, direct, literature, _, _ = cohorts
    proteins = audit.reconcile_proteins(direct, literature)
    terms = audit.reconcile_terms(*cohorts)
    assert len(proteins) == 1 and len(proteins["UniProtKB:P00001"]["sources"]) == 2
    assert terms["ARO:1"]["links"][0]["kind"] == audit.DIRECT
    assert terms["ARO:2"]["links"][0]["kind"] == audit.CITATION
    assert terms["ARO:3"]["reference_status"] == audit.UNSELECTED
    assert terms["ARO:1"]["links"][0]["source"]["pointer"] == "/determinants/ARO:1/candidates/0"
    assert terms["ARO:2"]["links"][0]["source"]["pointer"] == "/terms/ARO:2/reference_candidates/0"
    assert all(t["experimental_subject_assignment"] is False for t in terms.values())


@pytest.mark.parametrize(("key", "value"), [
    ("entry_version", 3), ("sequence_version", 2), ("entry_version", True),
    ("entry_type", "UniProtKB unreviewed (TrEMBL)"), ("reference_taxon_id", "NCBITaxon:21"),
    ("taxonomy_rank", "species"), ("reference_taxon_id", "NCBITaxon:0"),
    ("experimental_subject_assignment", True), ("exact_allele_assignment", True),
    ("taxonomy_identity_verified", False), ("accession", "UniProtKB:P00002"),
])
def test_shared_identity_and_scope_conflicts_fail(cohorts, key, value):
    _, direct, literature, _, _ = cohorts
    literature["proteins"]["UniProtKB:P00001"][key] = value
    with pytest.raises(ValueError):
        audit.reconcile_proteins(direct, literature)


@pytest.mark.parametrize(("key", "value"), [
    ("taxon_id", "NCBITaxon:11"), ("rank", "genus"), ("experimental_subject_assignment", True),
])
def test_species_conflicts_fail(cohorts, key, value):
    _, direct, literature, _, _ = cohorts
    literature["proteins"]["UniProtKB:P00001"]["reference_species_lineage"][key] = value
    with pytest.raises(ValueError):
        audit.reconcile_proteins(direct, literature)


@pytest.mark.parametrize("change", [
    "xref", "experimental", "allele", "primary", "optional_flag", "citation", "duplicate_citation",
    "context", "context_number", "duplicate_context", "duplicate_available", "missing_context",
    "gene", "gene_field", "gene_label", "missing_gene", "missing_subject_flag",
])
def test_citation_name_context_and_scope_guards(cohorts, change):
    _, _, literature, _, _ = cohorts
    term = literature["terms"]["ARO:2"]
    candidate = term["reference_candidates"][0]
    protein = literature["proteins"]["UniProtKB:P00001"]
    flags = {"xref": "explicit_card_xref", "experimental": "experimental_subject_assignment",
             "allele": "exact_allele_assignment", "primary": "primary_review_completed_by_this_audit",
             "optional_flag": "experimental_identity_assigned"}
    if change in flags:
        candidate[flags[change]] = True
    elif change == "citation":
        candidate["source_citation_ids"] = ["PMID:2"]
    elif change == "duplicate_citation":
        candidate["source_citation_ids"] *= 2
    elif change == "context":
        candidate["matched_study_contexts"][0]["citation_identifiers"] = ["PMID:2"]
    elif change == "context_number":
        candidate["matched_study_contexts"][0]["reference_number"] = 2
    elif change == "duplicate_context":
        candidate["matched_study_contexts"] *= 2
    elif change == "duplicate_available":
        protein["reference_contexts"] *= 2
    elif change == "missing_context":
        candidate["matched_study_contexts"] = []
    elif change == "gene":
        protein["gene_names_and_synonyms"] = ["different"]
    elif change == "gene_field":
        candidate["literal_gene_matches"][0]["field"] = "orderedLocusNames"
    elif change == "gene_label":
        term["source_label"] = "different"
    elif change == "missing_gene":
        candidate["literal_gene_matches"] = []
    else:
        del candidate["experimental_subject_assignment"]
    with pytest.raises(ValueError):
        audit.citation_link(candidate, term, protein)


@pytest.mark.parametrize("change", ["duplicate_link", "duplicate_membership", "empty_membership",
                                    "xref_term", "direct_version", "label", "scope_coverage", "overlap"])
def test_term_coverage_and_provenance_guards(cohorts, change):
    base, direct, literature, scopes, _ = cohorts
    if change == "duplicate_link":
        literature["terms"]["ARO:2"]["reference_candidates"] *= 2
    elif change == "duplicate_membership":
        direct["terms"]["ARO:1"]["record_memberships"] *= 2
    elif change == "empty_membership":
        direct["terms"]["ARO:1"]["record_memberships"] = []
    elif change == "xref_term":
        base["determinants"]["ARO:1"]["candidates"][0]["card_cross_reference"]["id"] = "ARO:2"
    elif change == "direct_version":
        base["determinants"]["ARO:1"]["candidates"][0]["entry_audit"]["entryVersion"] = 9
    elif change == "label":
        direct["terms"]["ARO:1"]["source_label_sha256"] = "changed"
    elif change == "scope_coverage":
        del scopes["terms"]["ARO:3"]
    else:
        literature["terms"]["ARO:1"] = literature["terms"]["ARO:2"]
    with pytest.raises(ValueError):
        audit.reconcile_terms(*cohorts)


def records():
    claims = [{"aro_id": tid, "label": "unselected" if tid == "ARO:3" else "example",
               "evidence": [{"reference": tid, "notes": "CARD/ARO asserts example"}]}
              for tid in ("ARO:1", "ARO:1", "ARO:2", "ARO:3")]
    claims += [{"source": "PHIBASE"}, {"aro_id": "ARO:1", "label": "curator-owned"}]
    row = {"path": "data/antibiotics/example.yaml", "sha256": "0" * 64,
           "standard_inchi_key": "EXAMPLE", "resistance_mechanisms": claims, "score_rules": [{}, {}]}
    return {"CHEBI:1": row, "CHEBI:2": {**row, "path": "data/antibiotics/empty.yaml",
                                          "resistance_mechanisms": [], "score_rules": []}}


def test_live_binding_keeps_duplicate_assertions_other_owners_and_empty_records(cohorts):
    claims, rows = audit.bind_claims(records(), audit.reconcile_terms(*cohorts))
    assert [c["resistance_index"] for c in claims] == [0, 1, 2, 3]
    assert claims[0]["claim_sha256"] == claims[1]["claim_sha256"]
    assert rows[0]["card_assertions"] == 4
    assert rows[0]["direct_xref_claims"] == 2
    assert rows[0]["citation_candidate_claims"] == rows[0]["unselected_candidate_claims"] == 1
    assert rows[0]["phi_claims_not_reassessed"] == rows[0]["curator_claims_not_reassessed"] == 1
    assert rows[0]["score_rules_not_reassessed"] == 2
    assert rows[1]["card_assertions"] == 0 and rows[1]["selected_reference_accessions"] == ""


@pytest.mark.parametrize("change", ["label", "membership", "missing_term", "conflicting_owner"])
def test_live_binding_drift_is_rejected(cohorts, change):
    terms, live = audit.reconcile_terms(*cohorts), records()
    if change == "label":
        live["CHEBI:1"]["resistance_mechanisms"][0]["label"] = "different"
    elif change == "membership":
        terms["ARO:1"]["record_memberships"] = ["CHEBI:2"]
    elif change == "missing_term":
        live["CHEBI:1"]["resistance_mechanisms"].pop(3)
    else:
        live["CHEBI:1"]["resistance_mechanisms"][0]["source"] = "PHIBASE"
    with pytest.raises(ValueError):
        audit.bind_claims(live, terms)


def test_rna_ancestry_does_not_override_definition_conflict(cohorts):
    _, _, _, scopes, named = cohorts
    scopes["terms"]["ARO:3"]["entity_scope"] = "RNA_TERM_NOT_A_PROTEIN_PRODUCT"
    named["terms"]["ARO:3"] = {
        "source_label_sha256": audit.progress.digest(b"unselected"),
        "entity_review": "PROTEIN_DEFINITION_CONFLICTS_WITH_RNA_ANCESTRY",
        "named_organism_taxon_id": "NCBITaxon:10",
    }
    term = audit.reconcile_terms(*cohorts)["ARO:3"]
    assert term["entity_review"] == "PROTEIN_DEFINITION_CONFLICTS_WITH_RNA_ANCESTRY"
    assert term["reference_status"] == audit.UNSELECTED and term["whole_record_primary_review"] == "OPEN"
    assert term["named_organism_taxon_reference_only"] == "NCBITaxon:10"


def test_public_cohorts_replay_without_network_native_cache_or_mutable_live_records(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline public checkpoint attempted network access")

    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        assert not path.is_relative_to(ROOT / "reports")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(Path, "open", guarded)
    result = json.loads((ROOT / (audit.PREFIX + ".json")).read_bytes())
    receipt = json.loads((ROOT / (audit.PREFIX + "-verification.json")).read_bytes())
    for pin in receipt["outputs"]:
        audit.reference.check_pin(ROOT, pin)
    plan = json.loads(audit.reference.check_pin(ROOT, result["plan"]).read_bytes())
    assert result["inputs"] == plan["inputs"]
    paths = {k: audit.reference.check_pin(ROOT, v) for k, v in result["inputs"].items()}
    source = {k: json.loads(p.read_bytes()) for k, p in paths.items() if p.suffix == ".json"}
    proteins = audit.reconcile_proteins(source["direct"], source["literature"])
    assert set(result["proteins"]) == set(proteins)
    for accession, item in proteins.items():
        assert all(result["proteins"][accession][k] == v for k, v in item.items())
    assert len(proteins) == 1046
    terms = audit.reconcile_terms(*(source[k] for k in (
        "direct_candidates", "direct", "literature", "term_scope", "named_taxa")))
    ledger = audit.progress.read_tsv(paths["ledger"].read_bytes())
    memberships = defaultdict(set)
    for row in ledger:
        memberships[row["aro_id"]].add(row["identifier"])
    for tid, term in terms.items():
        if term["record_memberships"] is not None:
            assert term["record_memberships"] == sorted(memberships[tid])
        term["record_memberships"] = sorted(memberships[tid])
    assert result["terms"] == terms
    census = {r["identifier"]: r for r in audit.progress.read_tsv(paths["census"].read_bytes())}
    rows = audit.progress.read_tsv((ROOT / (audit.PREFIX + ".tsv")).read_bytes())
    curator = json.loads(audit.reference.check_pin(ROOT, CURATOR_PIN).read_bytes())
    assert_public_projection(result, rows, list(census.values()), ledger, curator)
    assert {r["identifier"] for r in rows} == set(census) and len(rows) == 2939
    for row in rows:
        assert row["record_sha256"] == census[row["identifier"]]["record_sha256"]
    assert Counter((c["record_identifier"], c["aro_id"]) for c in result["claims"]) == Counter(
        (r["identifier"], r["aro_id"]) for r in ledger)
    for claim in result["claims"]:
        row = census[claim["record_identifier"]]
        assert claim["record_sha256"] == row["record_sha256"]
        assert claim["record_path"] == row["path"]
        assert claim["standard_inchi_key"] == row["standard_inchi_key"]
        assert claim["reference_status"] == terms[claim["aro_id"]]["reference_status"]
        assert claim["experimental_subject_assignment"] is False
    assert len({(c["record_identifier"], c["resistance_index"]) for c in result["claims"]}) == 4538
    assert sum(int(r["curator_claims_not_reassessed"]) for r in rows) == 131
    assert sum(int(r["phi_claims_not_reassessed"]) for r in rows) == 217
    assert sum(int(r["score_rules_not_reassessed"]) for r in rows) == 467
    assert result["summary"]["whole_record_primary_signoffs"] == 0
    assert terms["ARO:3004956"]["entity_review"] == "PROTEIN_DEFINITION_CONFLICTS_WITH_RNA_ANCESTRY"


def test_cli_check_never_overwrites_a_checkpoint(tmp_path, monkeypatch, cohorts):
    _, rows = audit.bind_claims(records(), audit.reconcile_terms(*cohorts))
    result = {"summary": {"example": 1}}
    (tmp_path / "research").mkdir()
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(audit, "build", lambda root: (result, rows))
    monkeypatch.setattr(sys, "argv", ["audit_card_reference_memberships.py"])
    audit.main()
    monkeypatch.setattr(sys, "argv", ["audit_card_reference_memberships.py", "--check"])
    audit.main()
    path = Path(audit.PREFIX + ".tsv")
    path.write_bytes(b"changed")
    with pytest.raises(SystemExit, match="does not reproduce"):
        audit.main()
    assert path.read_bytes() == b"changed"


@pytest.mark.parametrize("change", ["plan_scope", "input_digest", "direct_scope", "literature_scope",
                                    "release", "successor", "lineage", "context"])
def test_build_rejects_changed_inputs_before_loading_live_corpus(tmp_path, monkeypatch, change):
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    data = {key: json.loads((ROOT / pin["path"]).read_bytes()) for key, pin in plan["inputs"].items()
            if pin["path"].endswith(".json")}
    if change == "plan_scope":
        plan["constraints"]["experimental_assignments"] = True
    elif change == "input_digest":
        plan["inputs"]["direct"]["sha256"] = "0" * 64
    elif change in {"direct_scope", "literature_scope"}:
        data[change.removesuffix("_scope")]["scope"] = "EXPERIMENTAL"
    elif change == "release":
        next(iter(data["literature"]["queries"].values()))["release"] = "other"
    elif change == "successor":
        next(iter(data["species_successor"]["species"].values()))["active"] = False
    elif change == "lineage":
        next(iter(data["direct"]["taxa"].values()))["reference_active"] = False
    else:
        next(iter(data["direct_contexts"]["proteins"].values()))["reference_taxon_id"] = "NCBITaxon:1"
    paths = {}
    for key, pin in plan["inputs"].items():
        path = tmp_path / Path(pin["path"]).name
        body = (json.dumps(data[key]).encode() if key in data else (ROOT / pin["path"]).read_bytes())
        path.write_bytes(body)
        paths[pin["path"]] = path
    (tmp_path / "research").mkdir()
    (tmp_path / audit.PLAN).write_text(json.dumps(plan))

    def no_live(*args, **kwargs):
        raise AssertionError("invalid input reached live-corpus loading")

    monkeypatch.setattr(audit.progress, "current_records", no_live)
    if change == "input_digest":
        # Use the real checksum validator for this case, with a wrong digest and actual bytes.
        for pin in plan["inputs"].values():
            path = tmp_path / pin["path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((ROOT / pin["path"]).read_bytes())
    else:
        monkeypatch.setattr(audit.reference, "check_pin", lambda root, pin: paths[pin["path"]])
    with pytest.raises(ValueError):
        audit.build(tmp_path)
