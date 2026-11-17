"""All-record reconciliation retains taxonomy, gene and primary-evidence scope."""

import copy
import json
import socket
import sys
from collections import Counter
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_folp_rpo_memberships as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("network forbidden in reference-index tests")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)


@pytest.fixture(scope="module")
def frozen():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    data = {}
    for name, pin in plan["inputs"].items():
        if name in {"source_inventory", "source_queue"}:
            continue
        path = audit.reference.check_pin(ROOT, pin)
        data[name] = (
            audit.progress.read_tsv(path.read_bytes())
            if path.suffix == ".tsv"
            else json.loads(path.read_bytes())
        )
    return data, plan, audit.reference.pin(ROOT, ROOT / audit.PLAN)


@pytest.fixture
def inputs(frozen):
    return copy.deepcopy(frozen)


def resolve(data, pointer):
    value = data[pointer["input"]]
    for part in pointer["pointer"].split("/")[1:]:
        part = part.replace("~1", "/").replace("~0", "~")
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def test_public_reproduction_covers_all_records_and_card_claims(frozen):
    result, rows = audit.project(*frozen)
    for suffix, payload in zip((".json", ".tsv"), audit.prior.prior.prior.render(result, rows), strict=True):
        assert (ROOT / (audit.PREFIX + suffix)).read_bytes() == payload
    summary = result["summary"]
    assert summary["corpus_records"] == len(rows) == 2939
    assert summary["card_terms"] == len(result["terms"]) == 2002
    assert summary["card_assertions"] == len(result["claims"]) == 4538
    assert summary["selected_reference_terms"] == 1244
    assert summary["selected_reference_proteins"] == 1520
    assert summary["reference_links"] == 2608
    assert summary["added_reference_terms"] == 18
    assert summary["added_reference_proteins"] == 76
    assert summary["added_reference_links"] == 104
    assert summary["folp_rpo_source_terms"] == 21 and summary["folp_rpo_source_claims"] == 53
    assert summary["term_statuses"][audit.UNSELECTED] == 758
    assert summary["claim_statuses"][audit.UNSELECTED] == 1361
    assert summary["term_statuses"][audit.REVIEWED] == 16
    assert summary["term_statuses"][audit.UNREVIEWED] == 2
    assert summary["claim_statuses"][audit.REVIEWED] == 46
    assert summary["claim_statuses"][audit.UNREVIEWED] == 3
    assert summary["records_with_selected_references"] == 216
    assert summary["unreviewed_fragment_references"] == 212
    assert summary["phi_claims_not_reassessed"] == 217
    assert summary["curator_claims_not_reassessed"] == 133
    assert summary["score_rules_not_reassessed"] == 467
    assert summary["whole_record_primary_signoffs"] == 0
    assert all(sum(row[c] for c in audit.COLUMNS.values()) == row["card_assertions"] for row in rows)
    assert all(row["whole_record_primary_review"] == "OPEN" for row in rows)


def test_every_pointer_resolves_and_old_evidence_is_preserved(frozen):
    data = frozen[0]
    result, _ = audit.project(*frozen)

    def check(value):
        if isinstance(value, dict):
            if set(value) == {"input", "pointer"}:
                resolve(data, value)
            else:
                for child in value.values():
                    check(child)
        elif isinstance(value, list):
            for child in value:
                check(child)

    check(result)
    selected = set(data["folp"]["terms"]) | set(data["rpo"]["terms"])
    for tid, term in data["base"]["terms"].items():
        if tid in selected:
            continue
        expected = audit.rebase(term, "terms", tid)
        if expected["reference_status"] == audit.prior.UNSELECTED:
            expected["reference_status"] = audit.UNSELECTED
        assert result["terms"][tid] == expected
    for accession, old in data["base"]["proteins"].items():
        assert result["proteins"][accession] == audit.rebase(old, "proteins", accession)
    for old, new in zip(data["base"]["claims"], result["claims"], strict=True):
        assert {k: v for k, v in old.items() if k != "reference_status"} == {
            k: v for k, v in new.items() if k != "reference_status"
        }
    assert result["limits"] == data["base"]["limits"]
    assert Counter(t["entity_review"] for t in result["terms"].values()) == Counter(
        t["entity_review"] for t in data["base"]["terms"].values()
    )
    for tid in selected:
        for link in result["terms"][tid]["links"]:
            assert (
                link["explicit_card_xref"]
                is link["experimental_subject_assignment"]
                is link["exact_allele_assignment"]
                is False
            )
            assert link["source_citation_ids"] == link["matched_reference_numbers"] == []
            assert resolve(data, link["source"])["protein_accession"] == link["protein_accession"]


def test_projection_does_not_read_files_after_loading_public_snapshots(frozen, monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("filesystem access forbidden during projection")

    monkeypatch.setattr(Path, "read_bytes", forbidden)
    monkeypatch.setattr(Path, "read_text", forbidden)
    result, rows = audit.project(*frozen)
    assert len(rows) == 2939 and len(result["claims"]) == 4538


def test_rank_alias_fusion_fragments_and_access_states_survive(frozen):
    data = frozen[0]
    result, _ = audit.project(*frozen)
    gallinarum = result["terms"]["ARO:3007749"]
    assert gallinarum["named_organism_taxon_reference_only"] == "NCBITaxon:594"
    assert gallinarum["named_taxon_rank_reference_only"] == "no rank"
    assert gallinarum["species_ancestor_reference_only"]["taxonId"] == 28901
    assert gallinarum["folp_rpo_query_disposition"] == audit.prior.ZERO and gallinarum["links"] == []
    for tid in ("ARO:3003290", "ARO:3004995"):
        assert result["terms"][tid]["named_organism_taxon_reference_only"] is None
        assert not result["terms"][tid]["links"]
    alias = result["terms"]["ARO:3003389"]["links"][0]
    assert resolve(data, alias["source"])["native_gene_field_matches"] == [
        {"gene_index": 0, "field": "synonyms", "value": "folP"}
    ]
    fusion = result["proteins"]["UniProtKB:B5Z8J3"]
    assert len(fusion["native_included_protein_names"]) == 6
    assert fusion["unflagged_means_complete"] is False
    for accession in ("UniProtKB:P0C1T4", "UniProtKB:Q9KJE4"):
        assert result["proteins"][accession]["protein_description_flag"] == "Fragment"
    assert (
        resolve(data, result["rpo_primary_access_context"])["PMID:23208709"]["primary_results_reviewed"]
        is False
    )
    generic = resolve(data, result["terms"]["ARO:3004995"]["primary_access_followup"])
    assert generic["named_reference_taxon_id"] is None and generic["definition_citation_ids"] == []


@pytest.mark.parametrize("cohort", audit.COHORTS)
@pytest.mark.parametrize(
    "field,value",
    [
        ("source_label", "different"),
        ("source_label_sha256", "different"),
        ("source_gene_label", "different"),
        ("source_organism_name", "Different species"),
        ("record_memberships", []),
        ("definition_citation_ids", []),
        ("named_reference_taxon_id", "NCBITaxon:1"),
        ("named_reference_taxon_rank", "genus"),
        ("source_species_ancestor", None),
        ("reference_candidates", []),
        ("exact_allele_assignment", True),
        ("experimental_subject_assignment", True),
        ("experimental_genome_assignment", "GCA_000001"),
        ("primary_review_status", "COMPLETE"),
        ("reference_status", "REVIEWED_REFERENCE"),
    ],
)
def test_term_scope_guards(inputs, cohort, field, value):
    term = next(t for t in inputs[0][cohort]["terms"].values() if len(t["reference_candidates"]) > 1)
    term[field] = value
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize(
    "change",
    ["missing_term", "missing_record", "missing_claim", "duplicate_claim", "wrong_position", "extra_protein"],
)
def test_full_cohort_coverage_guards(inputs, change):
    dossier = inputs[0]["folp"]
    if change == "missing_term":
        dossier["terms"].pop(next(iter(dossier["terms"])))
    elif change == "missing_record":
        dossier["records"].pop()
    elif change == "missing_claim":
        dossier["claims"].pop()
    elif change == "duplicate_claim":
        dossier["claims"].append(copy.deepcopy(dossier["claims"][0]))
    elif change == "wrong_position":
        dossier["claims"][0]["position"] += 1
    else:
        dossier["proteins"]["UniProtKB:UNUSED"] = copy.deepcopy(next(iter(dossier["proteins"].values())))
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize(
    "field,value",
    [
        ("url", "https://rest.uniprot.org/uniprotkb/search?query=wrong"),
        ("gene", "rpoC"),
        ("source_taxon_id", True),
        ("reviewed_subset", False),
        ("complete_for_query", False),
        ("zero_hit_is_biological_absence", True),
        ("suggestions_followed", True),
        ("result_count", 0),
        ("accessions", []),
        ("release", "different"),
    ],
)
def test_query_guards(inputs, field, value):
    query = inputs[0]["folp"]["terms"]["ARO:3003386"]["queries"]["reviewed"]
    if field in {"url", "release"}:
        query["source"][field] = value
    else:
        query[field] = value
    with pytest.raises(ValueError):
        audit.project(*inputs)


def test_fallback_cannot_replace_nonempty_reviewed_results(inputs):
    term = inputs[0]["folp"]["terms"]["ARO:3003386"]
    term["queries"]["unreviewed"] = copy.deepcopy(term["queries"]["reviewed"])
    with pytest.raises(ValueError, match="fallback"):
        audit.project(*inputs)


@pytest.mark.parametrize(
    "change", ["rank", "parent", "experimental", "other_name_only", "provenance", "duplicate_candidate"]
)
def test_native_name_guards(inputs, change):
    row = inputs[0]["folp"]["names"]["Salmonella gallinarum"]
    if change == "rank":
        row["selected_taxon"]["rank"] = "species"
    elif change == "parent":
        row["selected_taxon"]["species_ancestor"]["taxonId"] = 999
    elif change == "experimental":
        row["experimental_subject_assignment"] = True
    elif change == "other_name_only":
        row["selected_taxon"]["other_name_match_only"] = True
    elif change == "provenance":
        row["source"]["url"] = "https://other.example/taxonomy/594"
    else:
        row["candidates"].append(copy.deepcopy(row["candidates"][0]))
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize(
    "change", ["version", "species", "experimental", "allele", "fragment", "ambiguous_gene", "invented_alias"]
)
def test_protein_guards(inputs, change):
    protein = inputs[0]["folp"]["proteins"]["UniProtKB:P0C0X1"]
    if change == "version":
        protein["entry_version"] = True
    elif change == "species":
        protein["reference_species_taxon_id"] = "NCBITaxon:1"
    elif change == "experimental":
        protein["experimental_subject_assignment"] = True
    elif change == "allele":
        protein["exact_resistance_allele"] = True
    elif change == "fragment":
        protein["native_protein_flag"] = "Complete"
    elif change == "ambiguous_gene":
        protein["genes"].append(copy.deepcopy(protein["genes"][0]))
    else:
        protein["genes"][0]["synonyms"] = []
    with pytest.raises(ValueError):
        audit.project(*inputs)


def test_conflicting_cross_cohort_identity_fails(inputs):
    accession = "UniProtKB:P0C0X1"
    protein = inputs[0]["folp"]["proteins"][accession]
    identity = audit.prior.prior.prior.reference_identity({**protein, "exact_allele_assignment": False})
    identity["entry_version"] += 1
    inputs[0]["base"]["proteins"][accession] = {
        "identity": identity,
        "sources": [],
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
    }
    with pytest.raises(ValueError, match="conflicting cross-cohort"):
        audit.project(*inputs)


@pytest.mark.parametrize("change", ["bridge_title", "bridge_citation", "generic_organism", "shared_query"])
def test_rpo_specific_identity_boundaries(inputs, change):
    rpo = inputs[0]["rpo"]
    if change == "bridge_title":
        rpo["bibliographic_identity_context"]["20837752"]["title"] = "A different organism"
    elif change == "bridge_citation":
        inputs[0]["definition_citations"]["terms"]["ARO:3003090"]["definition_citation_ids"] = []
    elif change == "generic_organism":
        rpo["terms"]["ARO:3004995"]["source_organism_name"] = "Mycobacterium tuberculosis"
    else:
        rpo["terms"]["ARO:3003285"]["queries"]["reviewed"]["source"]["retrieved_at"] = "different"
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize(
    "change",
    ["primary_complete", "article_obtained", "paywall_inferred", "negative_biology", "generic_citation"],
)
def test_primary_access_does_not_become_biological_signoff(inputs, change):
    access = inputs[0]["rpo_primary_access"]
    if change == "primary_complete":
        access["access_states"]["PMID:23208709"]["primary_results_reviewed"] = True
    elif change == "article_obtained":
        access["access_states"]["PMID:30337678"]["article_obtained"] = True
    elif change == "paywall_inferred":
        access["access_states"]["PMID:30337678"]["access_denial_or_paywall_inferred"] = True
    elif change == "negative_biology":
        access["access_states"]["PMID:23208709"]["negative_biological_evidence"] = True
    else:
        access["term_contexts"]["ARO:3004995"]["definition_citation_ids"] = ["PMID:23208709"]
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize(
    "change",
    [
        "missing_row",
        "row_count",
        "phi",
        "curator",
        "score",
        "primary",
        "accessions",
        "claim_hash",
        "claim_position",
    ],
)
def test_all_record_accounting_guards(inputs, change):
    data = inputs[0]
    row = data["base_rows"][0]
    if change == "missing_row":
        data["base_rows"].pop()
    elif change in {"row_count", "phi", "curator", "score", "primary", "accessions"}:
        field = {
            "row_count": "card_assertions",
            "phi": "phi_claims_not_reassessed",
            "curator": "curator_claims_not_reassessed",
            "score": "score_rules_not_reassessed",
            "primary": "whole_record_primary_review",
            "accessions": "selected_reference_accessions",
        }[change]
        row[field] = (
            "COMPLETE" if change == "primary" else "UniProtKB:WRONG" if change == "accessions" else "999999"
        )
    elif change == "claim_hash":
        claim = next(c for c in data["base"]["claims"] if c["aro_id"] in data["folp"]["terms"])
        claim["claim_sha256"] = "different"
    else:
        data["base"]["claims"][0]["resistance_index"] = -1
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize("check", [False, True])
def test_cli_validates_both_outputs_before_writing_either(tmp_path, monkeypatch, check):
    prefix = str(tmp_path / "index")
    Path(prefix + ".tsv").write_bytes(b"historical tsv\n")
    monkeypatch.setattr(audit, "PREFIX", prefix)
    monkeypatch.setattr(audit, "build", lambda root: ({"summary": {}}, []))
    monkeypatch.setattr(audit.prior.prior.prior, "render", lambda *args: (b"new json", b"new tsv"))
    monkeypatch.setattr(sys, "argv", ["audit"] + (["--check"] if check else []))
    with pytest.raises((ValueError, FileNotFoundError)):
        audit.main()
    assert not Path(prefix + ".json").exists()
    assert Path(prefix + ".tsv").read_bytes() == b"historical tsv\n"
