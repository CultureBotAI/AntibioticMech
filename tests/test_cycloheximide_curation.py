"""Dated yeast evidence must not become an exact allele or causal pathway."""
import copy
import csv
import hashlib
import json
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic
from scripts.embed_records import build_document, role_names

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-13-cycloheximide"


def read(suffix):
    return json.loads(Path(str(PREFIX) + suffix).read_bytes())


def assert_pin(pin):
    payload = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
    return payload


def ordered(value, keys):
    # Sorted JSON receipts need the original YAML field order for byte replay.
    assert set(value) == set(keys)
    return {key: copy.deepcopy(value[key]) for key in keys}


def replay(context, receipt, tmp_path):
    assert hashlib.sha256(assert_pin(receipt["fixture"])).hexdigest() == receipt["before"]["sha256"]
    assert receipt["before"] == context["record_before"]
    assert receipt["record"]["path"] == receipt["before"]["path"]
    before = load_record(ROOT / receipt["fixture"]["path"])
    after = copy.deepcopy(before)
    assert before["identifier"] == "CHEBI:27641"
    assert before["chemical_structure"]["standard_inchi_key"] == "YPHMISFOHDHNIV-FSZOTQKASA-N"
    additions = [ordered(c, ("mechanism_type", "label", "gene_families", "taxon_id", "taxon_label",
                             "phenotype_label", "assay", "note", "evidence")) for c in receipt["claims"]]
    for claim in additions:
        claim["evidence"] = [ordered(e, ("reference", "notes")) for e in claim["evidence"]]
    after["resistance_mechanisms"].extend(additions)
    after["curation_history"].append(ordered(receipt["curation_event"], (
        "timestamp", "curator", "action", "changes", "llm_assisted")))
    output = tmp_path / "after.yaml"
    write_validated_antibiotic(after, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == receipt["record"]["sha256"]
    assert after["resistance_mechanisms"][:3] == before["resistance_mechanisms"]
    assert after["curation_history"][:-1] == before["curation_history"]
    unchanged = set(before) - {"resistance_mechanisms", "curation_history"}
    assert {k: before[k] for k in unchanged} == {k: after[k] for k in unchanged}
    assert build_document(before, role_names()) != build_document(after, role_names())
    assert receipt["history_events_added"] == receipt["records_changed"] == 1
    assert receipt["new_resistance_claims"] == 2 and receipt["existing_claims_preserved"] == 3


def test_dated_replay_preserves_source_slices(tmp_path):
    replay(read("-context.json"), read("-curation.json"), tmp_path)


def test_replay_does_not_freeze_live_record(tmp_path, monkeypatch):
    receipt = read("-curation.json")
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert path != ROOT / receipt["record"]["path"]
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    replay(read("-context.json"), receipt, tmp_path)


@pytest.mark.parametrize("field", ["claim", "event", "before_hash", "after_hash"])
def test_replay_rejects_tampering(tmp_path, field):
    receipt = read("-curation.json")
    if field == "claim":
        receipt["claims"][1]["mechanism_type"] = "ANTIBIOTIC_EFFLUX"
    elif field == "event":
        receipt["curation_event"]["changes"] += " Unsupported edit."
    else:
        receipt["before" if field == "before_hash" else "record"]["sha256"] = "0" * 64
    with pytest.raises(AssertionError):
        replay(read("-context.json"), receipt, tmp_path)


def test_historical_alias_is_not_modern_rpl29():
    refs = read("-context.json")["reference_proteins"]
    for name in ("CYH2", "RPL28"):
        row = refs[name]
        assert row["protein_accession"] == "UniProtKB:P02406"
        assert row["canonical_gene"] == "RPL28" and "CYH2" in row["aliases"]
        assert row["ordered_locus_names"] == ["YGL103W"]
        assert row["sgd_ids"] == ["SGD:S000003071"]
        assert (row["entry_version"], row["sequence_version"]) == (210, 3)
    modern = refs["RPL29"]
    assert modern["protein_accession"] == "UniProtKB:P05747"
    assert modern["ordered_locus_names"] == ["YFR032C-A"]
    assert modern["canonical_gene"] == "RPL29" and "CYH2" not in modern["aliases"]
    assert refs["CYH2"]["request"]["body_sha256"] == refs["RPL28"]["request"]["body_sha256"]
    for row in refs.values():
        assert row["reference_taxon_id"] == "NCBITaxon:559292"
        assert row["reviewed"] and not row["experimental_resistance_assignment"]
        assert row["request"]["pagination_complete"] and row["request"]["total_results"] == 1
        assert row["request"]["release"] == "2026_03"
        assert "results" not in row["request"]


def assert_no_experimental_assignment(claims):
    forbidden = {"alteration", "protein_accession", "strain", "strain_taxon_id", "gene_id",
                 "assembly_accession", "biosample_accession", "bioproject_accession", "sra_accessions",
                 "sequence", "variant", "mic", "mic_value", "phenotype"}
    assert all(not forbidden.intersection(claim) for claim in claims)


def test_qualified_claims_and_causal_limits():
    receipt = read("-curation.json")
    rpl28, agp2 = receipt["claims"]
    assert rpl28["gene_families"] == ["RPL28"]
    assert rpl28["mechanism_type"] == "ANTIBIOTIC_TARGET_ALTERATION"
    assert "not modern RPL29" in rpl28["note"]
    assert "does not establish direct drug binding" in rpl28["note"]
    assert agp2["gene_families"] == ["AGP2"] and agp2["mechanism_type"] == "UNKNOWN"
    assert "were not established" in agp2["note"] and "units conflict" in agp2["note"]
    assert_no_experimental_assignment(receipt["claims"])
    for claim, accession in zip(receipt["claims"], ("P02406", "P38090"), strict=True):
        assert claim["taxon_id"] == "NCBITaxon:4932"
        assert claim["taxon_label"] == "Saccharomyces cerevisiae"
        assert claim["evidence"][1]["reference"] == "UniProtKB:" + accession
        assert "Reference identity only" in claim["evidence"][1]["notes"]
        assert "not an experimental strain assignment" in claim["evidence"][1]["notes"]
    assert receipt["numerical_ast_added"] == receipt["experimental_proteins_or_genomes_assigned"] == 0
    assert not receipt["whole_record_review_complete"]


@pytest.mark.parametrize("field", ["alteration", "protein_accession", "strain_taxon_id", "assembly_accession",
                                  "biosample_accession", "mic", "phenotype"])
def test_unsupported_fields_are_rejected(field):
    claims = read("-curation.json")["claims"]
    claims[0][field] = "unsupported"
    with pytest.raises(AssertionError):
        assert_no_experimental_assignment(claims)


def test_source_scope_taxonomy_and_deferral():
    context = read("-context.json")
    assert context["taxonomy"] == json.loads(assert_pin(context["taxonomy_predecessor"]))["taxonomy"]
    old, new = context["primary"]
    assert old["reference"] == "PMID:6304624" and not old["native_figures_inspected"]
    assert new["native_figures_inspected"] == [1, 8, 10] and new["pdf"]["pages"] == 26
    assert all(not p["whole_paper_review_complete"] for p in context["primary"])
    assert not context["disposition"]["PDR5_mediation_proven"]
    assert not context["disposition"]["modern_RPL29_promoted"]
    assert context["limits"]["issue_1040"] == "DEFERRED"
    assert all(not v for k, v in context["limits"].items() if k != "issue_1040")


def test_census_has_two_additions_without_more_resistant_records():
    receipt = read("-curation.json")
    reconciliation = read("-reconciliation.json")
    maps = []
    for key in ("previous_census", "current_census"):
        rows = list(csv.DictReader(assert_pin(reconciliation[key]).decode().splitlines(), delimiter="\t"))
        mapping = {r["identifier"]: r for r in rows}
        assert len(rows) == len(mapping) == 2939
        maps.append(mapping)
    before, after = maps
    assert set(before) == set(after)
    assert [i for i in before if before[i] != after[i]] == ["CHEBI:27641"]
    assert before["CHEBI:27641"]["resistance_assertions"] == "3"
    assert after["CHEBI:27641"] == {**before["CHEBI:27641"],
        "record_sha256": receipt["record"]["sha256"], "resistance_assertions": "5",
        "research_status": "PENDING_PRIMARY_REVIEW"}
    assert sum(int(r["resistance_assertions"]) for r in after.values()) == 4855
    assert sum(int(r["resistance_assertions"]) > 0 for r in after.values()) == 311
    assert reconciliation["curator_claims"] == 100 and reconciliation["curator_records"] == 44
    assert reconciliation["whole_record_reviews_completed"] == 0
