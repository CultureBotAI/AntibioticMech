"""Rpo references must retain gene, taxon and evidence scope."""

import copy
import json
import socket
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_rpo_references as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)


def node(taxid, name, rank):
    return {"taxonId": taxid, "scientificName": name, "rank": rank}


def taxonomy():
    ancestors = [node(2, "Bacteria", "domain"), node(562, "Escherichia coli", "species")]
    return {
        **node(83333, "Escherichia coli (strain K12)", "strain"),
        "active": True,
        "lineage": ancestors,
        "parent": ancestors[-1],
    }


def named():
    bacteria = node(2, "Bacteria", "domain")
    taxon = {
        **node(562, "Escherichia coli", "species"),
        "active": True,
        "lineage": [bacteria],
        "parent": bacteria,
    }
    return audit.resolve_name({"results": [taxon]}, "Escherichia coli")["selected_taxon"]


@pytest.fixture
def entry():
    return {
        "primaryAccession": "P0A8V2",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
        "organism": {"scientificName": "Escherichia coli (strain K12)", "taxonId": 83333},
        "genes": [{"geneName": {"value": "rpoB"}, "orderedLocusNames": [{"value": "b3987"}]}],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "RNA polymerase subunit beta"}}},
        "references": [
            {
                "citation": {
                    "publicationDate": "2000",
                    "citationCrossReferences": [{"database": "PubMed", "id": "12345"}],
                },
                "referencePositions": ["not exported"],
            }
        ],
    }


def test_source_label_identity():
    label = "Escherichia coli rpoB mutants conferring resistance to rifampicin"
    assert audit.source_identity("ARO:test", label, {}, {}) == ("Escherichia coli", "rpoB", "SOURCE_LABEL")


@pytest.mark.parametrize(
    "tid,label",
    [
        ("ARO:3003290", "daptomycin-resistant beta prime subunit of RNA polymerase (rpoC)"),
        ("ARO:3004995", "rifampicin resistant rpoC"),
    ],
)
def test_organism_free_terms_are_not_assigned_neighboring_species(tid, label):
    assert audit.source_identity(tid, label, {tid: ""}, {}) == (None, "rpoC", "UNRESOLVED_NO_NAME")


@pytest.mark.parametrize("change", [None, "definition", "title", "pmid"])
def test_abbreviation_bridge_needs_its_own_definition_and_cited_title(change):
    tid = "ARO:3003090"
    definitions = {tid: "Known from S. aureus."}
    bibliography = {"20837752": {"pmid": "20837752", "title": "Reported in Staphylococcus aureus."}}
    if change == "definition":
        definitions[tid] = "Known from another organism."
    elif change:
        bibliography["20837752"][change] = "different"
    if change:
        with pytest.raises(ValueError, match="abbreviation"):
            audit.source_identity(tid, "RNA polymerase (rpoB)", definitions, bibliography)
    else:
        assert audit.source_identity(tid, "RNA polymerase (rpoB)", definitions, bibliography) == (
            "Staphylococcus aureus",
            "rpoB",
            "DEFINITION_ABBREVIATION_AND_CITED_TITLE",
        )


@pytest.mark.parametrize("label", ["RNA polymerase", "rpoB and rpoC", "rpoB and rpoB"])
def test_ambiguous_gene_labels_fail_closed(label):
    with pytest.raises(ValueError):
        audit.source_identity("ARO:test", label, {}, {})


@pytest.mark.parametrize("gene", ["rpoB", "rpoC"])
@pytest.mark.parametrize("reviewed", [True, False])
def test_exact_query_scope(gene, reviewed):
    query = parse_qs(urlsplit(audit.gene_url(562, gene, reviewed)).query)
    assert query["query"] == [f"gene_exact:{gene} AND taxonomy_id:562 AND reviewed:{str(reviewed).lower()}"]
    assert not {"sequence", "ft_variant", "cc_function"}.intersection(query["fields"][0].split(","))


@pytest.mark.parametrize(
    "taxid,gene,reviewed",
    [
        (True, "rpoB", True),
        (0, "rpoC", True),
        ("562", "rpoB", True),
        (562, "rpo", True),
        (562, "rpoB OR gene:rpoC", True),
        (562, "rpoB", 1),
    ],
)
def test_invalid_query_scope(taxid, gene, reviewed):
    with pytest.raises(ValueError):
        audit.gene_url(taxid, gene, reviewed)


def test_gene_and_name_contexts_do_not_collapse():
    terms = {
        str(i): {"source_organism_name": name, "source_gene_label": gene}
        for i, (name, gene) in enumerate(
            [
                ("Escherichia coli", "rpoB"),
                ("Escherichia coli", "rpoC"),
                ("Escherichia coli", "rpoB"),
                (None, "rpoC"),
            ]
        )
    }
    contexts = audit.contexts({"terms": terms}, {"Escherichia coli": {"selected_taxon": named()}})
    assert set(contexts) == {"Escherichia coli|rpoB", "Escherichia coli|rpoC"}
    assert audit.contexts({"terms": terms}, {"Escherichia coli": {"selected_taxon": None}}) == {}


def test_projection_retains_reference_only_status(entry):
    protein, matches = audit.project(entry, taxonomy(), named(), "rpoB", True)
    assert matches == [{"gene_index": 0, "field": "geneName", "value": "rpoB"}]
    assert protein["reference_species_taxon_id"] == "NCBITaxon:562"
    assert protein["reference_taxon_id"] == "NCBITaxon:83333"
    assert protein["experimental_subject_assignment"] is protein["exact_resistance_allele"] is False
    assert protein["experimental_genome_assignment"] is None
    assert protein["resistance_inferred_from_reference"] is False
    assert protein["database_review_status_is_primary_results_review"] is False
    assert protein["unflagged_means_complete"] is False
    assert "not exported" not in json.dumps(protein)
    assert all(c["primary_results_reviewed"] is False for c in protein["bibliography"])


@pytest.mark.parametrize(
    "change",
    [
        "wrong_gene",
        "locus_only",
        "orf_only",
        "ambiguous_blocks",
        "wrong_taxon",
        "lineage_conflict",
        "review_status",
        "zero_version",
        "bool_version",
        "sequence",
        "features",
        "comments",
    ],
)
def test_projection_scope_guards(entry, change):
    taxon = taxonomy()
    if change in {"wrong_gene", "locus_only", "orf_only"}:
        entry["genes"][0]["geneName"]["value"] = "rpoC"
        if change != "wrong_gene":
            field = "orderedLocusNames" if change == "locus_only" else "orfNames"
            entry["genes"][0][field] = [{"value": "rpoB"}]
    elif change == "ambiguous_blocks":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change == "wrong_taxon":
        entry["organism"]["taxonId"] = 1
    elif change == "lineage_conflict":
        taxon["lineage"][-1]["scientificName"] = "Different name"
    elif change == "review_status":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change.endswith("version"):
        entry["entryAudit"]["entryVersion"] = True if change == "bool_version" else 0
    else:
        entry[change] = []
    with pytest.raises(ValueError):
        audit.project(entry, taxon, named(), "rpoB", True)


def test_native_synonym_is_not_an_invented_gene_crosswalk(entry):
    entry["genes"][0]["geneName"]["value"] = "rpoBC"
    entry["genes"][0]["synonyms"] = [{"value": "rpoB"}]
    protein, matches = audit.project(entry, taxonomy(), named(), "rpoB", True)
    assert protein["gene_names"] == ["rpoB", "rpoBC"]
    assert matches[0]["field"] == "synonyms"
    entry["genes"][0]["synonyms"] = []
    with pytest.raises(ValueError):
        audit.project(entry, taxonomy(), named(), "rpoB", True)


@pytest.mark.parametrize("fragment", [True, False])
def test_unreviewed_fusion_metadata_and_fragment_are_preserved(entry, fragment):
    entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    entry["proteinDescription"] = {
        "recommendedName": {"fullName": {"value": "Multifunctional fusion protein"}},
        "includes": [
            {
                "recommendedName": {"fullName": {"value": "Subunit beta"}},
                "alternativeNames": [{"fullName": {"value": "Alternative beta name"}}],
            },
            {"recommendedName": {"fullName": {"value": "Subunit beta prime"}}},
        ],
    }
    if fragment:
        entry["proteinDescription"]["flag"] = "Fragment"
    protein, _ = audit.project(entry, taxonomy(), named(), "rpoB", False)
    assert protein["native_protein_flag"] == ("Fragment" if fragment else None)
    assert protein["unflagged_means_complete"] is False
    assert protein["native_included_protein_names"] == [
        {"component_index": 0, "kind": "recommendedName", "value": "Subunit beta"},
        {"component_index": 0, "kind": "alternativeNames", "value": "Alternative beta name"},
        {"component_index": 1, "kind": "recommendedName", "value": "Subunit beta prime"},
    ]


@pytest.mark.parametrize("results", [[], ["entry"]])
def test_complete_results_do_not_imply_alleles_or_absence(entry, monkeypatch, results):
    entries = [entry] if results else []
    monkeypatch.setattr(
        audit.native,
        "read_source",
        lambda *args: ({"results": entries, "suggestions": [{}]}, {"release": "2026_03"}),
    )
    value, query = audit.read_gene(ROOT, {"url": audit.gene_url(562, "rpoB", True)}, 562, "rpoB", True)
    assert value == entries
    assert query["complete_for_query"] is True
    assert query["zero_hit_is_biological_absence"] is query["suggestions_followed"] is False
    assert query["suggestions_ignored"] == 1


@pytest.mark.parametrize(
    "change",
    [
        None,
        "missing_context",
        "extra_request",
        "wrong_gene",
        "wrong_taxon",
        "wrong_name",
        "wrong_context",
        "wrong_review",
        "nonempty_prior",
        "stale_prior",
    ],
)
def test_fallback_is_bound_to_exact_complete_reviewed_zero(tmp_path, monkeypatch, change):
    cohort = {
        "terms": {"ARO:test": {"source_organism_name": "Escherichia coli", "source_gene_label": "rpoB"}}
    }
    (tmp_path / "cohort.json").write_text(json.dumps(cohort))
    key = "Escherichia coli|rpoB"
    selected_names = {"Escherichia coli": {"selected_taxon": named()}}
    prior = {key: ([], {"accessions": [], "complete_for_query": True})}
    request = {
        "name": "Escherichia coli",
        "gene": "rpoB",
        "source_taxon_id": 562,
        "context": key,
        "reviewed": False,
        "url": audit.gene_url(562, "rpoB", False),
    }
    plan = {
        "cohort": audit.reference.pin(tmp_path, tmp_path / "cohort.json"),
        "queries": {key: {"request_key": "fallback", "prior_reviewed_query": copy.deepcopy(prior[key][1])}},
        "requests": {"fallback": request},
    }
    if change == "missing_context":
        plan["queries"] = {}
    elif change == "extra_request":
        plan["requests"]["extra"] = copy.deepcopy(request)
    elif change and change.startswith("wrong_"):
        field = {
            "wrong_gene": "gene",
            "wrong_taxon": "source_taxon_id",
            "wrong_name": "name",
            "wrong_context": "context",
            "wrong_review": "reviewed",
        }[change]
        request[field] = True if field == "reviewed" else 999 if field == "source_taxon_id" else "different"
    elif change == "nonempty_prior":
        prior[key] = ([{"primaryAccession": "P0A8V2"}], prior[key][1])
    elif change == "stale_prior":
        plan["queries"][key]["prior_reviewed_query"]["complete_for_query"] = False
    (tmp_path / "unreviewed-plan.json").write_text(json.dumps(plan))
    monkeypatch.setattr(audit, "planned_source", lambda *args: {"url": args[-1]})
    monkeypatch.setattr(audit, "read_gene", lambda *args: ([], {"accessions": []}))
    if change:
        with pytest.raises(ValueError):
            audit.read_queries(tmp_path, tmp_path, cohort, selected_names, False, prior)
    else:
        result = audit.read_queries(tmp_path, tmp_path, cohort, selected_names, False, prior)
        assert set(result) == {key} and result[key][0] == []


@pytest.mark.parametrize("existing,check", [(False, False), (True, False), (True, True)])
def test_cli_preserves_existing_checkpoint(tmp_path, monkeypatch, existing, check):
    output = tmp_path / "checkpoint.json"
    result = {"summary": {"source_terms": 16}}
    monkeypatch.setattr(audit, "OUTPUT", output)
    monkeypatch.setattr(audit, "build", lambda root: result)
    monkeypatch.setattr(sys, "argv", ["audit"] + (["--check"] if check else []))
    if existing:
        output.write_bytes(b"historical checkpoint\n")
        with pytest.raises(ValueError, match="does not reproduce"):
            audit.main()
        assert output.read_bytes() == b"historical checkpoint\n"
    else:
        audit.main()
        assert json.loads(output.read_bytes()) == result


def test_public_checkpoint_retains_full_cohort_and_open_claims():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["summary"]["source_terms"] == 16
    assert len(result["claims"]) == 32 and len(result["records"]) == 7
    assert result["summary"]["source_names"] == 9 and result["summary"]["gene_contexts"] == 12
    for term in result["terms"].values():
        assert term["primary_review_status"] == "OPEN"
        assert term["experimental_subject_assignment"] is term["exact_allele_assignment"] is False
        assert term["experimental_genome_assignment"] is None
    for tid in ("ARO:3003290", "ARO:3004995"):
        term = result["terms"][tid]
        assert term["source_organism_name"] is term["named_reference_taxon_id"] is None
        assert not term["reference_candidates"] and not term["queries"]
    assert result["constraints"]["ncbi_requests"] == 0
    assert result["constraints"]["full_corpus_goal_status"] == "OPEN"
    assert result["primary_review_flags"]["ARO:3004994"]["source_claim_corrected"] is False


@pytest.mark.skipif(not (ROOT / audit.CACHE / "cohort.json").exists(), reason="private native cache absent")
def test_native_replay_is_byte_identical_and_offline():
    result = audit.build(ROOT)
    assert (json.dumps(result, indent=2, sort_keys=True) + "\n").encode() == (
        ROOT / audit.OUTPUT
    ).read_bytes()
