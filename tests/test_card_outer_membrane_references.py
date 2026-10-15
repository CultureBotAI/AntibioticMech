"""Outer-membrane label references must not become allele or complex assignments."""

import copy
import csv
import json
import socket
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_outer_membrane_references as audit  # noqa: E402


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
    return audit.shared.resolve_name({"results": [taxon]}, "Escherichia coli")["selected_taxon"]


@pytest.fixture
def entry():
    return {
        "primaryAccession": "P02931",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
        "organism": {"scientificName": "Escherichia coli (strain K12)", "taxonId": 83333},
        "genes": [{"geneName": {"value": "ompF"}, "orderedLocusNames": [{"value": "b0929"}]}],
        "proteinDescription": {
            "recommendedName": {"fullName": {"value": "Outer membrane porin F"}},
            "flag": "Precursor",
        },
        "references": [
            {
                "referenceNumber": 1,
                "citation": {
                    "citationType": "journal article",
                    "title": "Fixture paper",
                    "publicationDate": "2000",
                    "citationCrossReferences": [{"database": "PubMed", "id": "12345"}],
                },
                "referenceComments": [
                    {"type": "STRAIN", "value": "reference A"},
                    {"type": "STRAIN", "value": "reference B"},
                ],
                "referencePositions": ["SEQUENCE_SENTINEL"],
            }
        ],
    }


@pytest.mark.parametrize(
    "label,name,gene",
    [
        (
            "Escherichia coli ompF with mutation conferring resistance to beta-lactam antibiotics",
            "Escherichia coli",
            "ompF",
        ),
        ("Klebsiella pneumoniae OmpK35", "Klebsiella pneumoniae", "OmpK35"),
        ("Acinetobacter baumannii AbuO", "Acinetobacter baumannii", "AbuO"),
        ("Neisseria gonorrhoeae porin PIB (por)", "Neisseria gonorrhoeae", "por"),
    ],
)
def test_named_identity_preserves_literal_gene(label, name, gene):
    assert audit.source_identity(label) == {
        "source_organism_name": name,
        "source_gene_label": gene,
        "entity_scope": "ORGANISM_NAMED_SINGLE_PROTEIN_LABEL",
    }


@pytest.mark.parametrize(
    "label",
    [
        "MexAB-OprM",
        "AmrAB-OprM",
        "AxyXY-OprZ",
        "MexEF-OprN with MexT mutation conferring resistance to "
        "chloramphenicol, ciprofloxacin, and trimethoprim",
    ],
)
def test_complexes_and_regulatory_contexts_not_forced_into_one_protein(label):
    result = audit.source_identity(label)
    assert result["source_organism_name"] is result["source_gene_label"] is None
    assert result["entity_scope"] == "COMPLEX_OR_REGULATORY_CONTEXT_NOT_SINGLE_PROTEIN"


@pytest.mark.parametrize("label", ["porin OmpC", "OmpA"])
def test_unnamed_organism_not_borrowed_from_another_record(label):
    result = audit.source_identity(label)
    assert result["source_organism_name"] is result["source_gene_label"] is None
    assert result["entity_scope"] == "ORGANISM_UNSPECIFIED_NO_SPECIES_QUERY"


@pytest.mark.parametrize(
    "label", ["Unreviewed", "Escherichia coli OmpF-OmpC", "Escherichia coli OmpF and OmpC"]
)
def test_unreviewed_source_syntax_fails_closed(label):
    with pytest.raises(ValueError):
        audit.source_identity(label)


@pytest.mark.parametrize("gene", ["OmpK35", "ompF", "por", "AbuO"])
@pytest.mark.parametrize("reviewed", [True, False])
def test_query_is_exact_literal_gene_and_taxon_without_sequences(gene, reviewed):
    args = parse_qs(urlsplit(audit.gene_url(562, gene, reviewed)).query)
    assert args["query"] == [f"gene_exact:{gene} AND taxonomy_id:562 AND reviewed:{str(reviewed).lower()}"]
    assert set(args["fields"][0].split(",")) == set(audit.genes.FIELDS.split(","))
    assert not {"sequence", "ft_variant", "cc_function"}.intersection(args["fields"][0].split(","))


@pytest.mark.parametrize(
    "taxid,gene,reviewed",
    [
        (True, "ompF", True),
        (0, "ompF", True),
        ("562", "ompF", True),
        (562, "ompF OR por", True),
        (562, "porB", True),
        (562, "ompF", 1),
    ],
)
def test_unplanned_query_scope_rejected(taxid, gene, reviewed):
    with pytest.raises(ValueError):
        audit.gene_url(taxid, gene, reviewed)


def test_projection_retains_reference_precursor_and_one_to_many_bibliography(entry):
    protein, matches = audit.project(entry, taxonomy(), named(), "ompF", True)
    assert matches == [{"gene_index": 0, "field": "geneName", "value": "ompF"}]
    assert protein["reference_taxon_id"] == "NCBITaxon:83333"
    assert protein["reference_species_taxon_id"] == "NCBITaxon:562"
    assert protein["native_protein_flag"] == "Precursor"
    assert protein["precursor_or_fragment_coordinates_inferred"] is False
    assert protein["experimental_subject_assignment"] is protein["exact_resistance_allele"] is False
    assert protein["experimental_genome_assignment"] is None
    assert (
        protein["porin_function_inferred_from_source_label"]
        is protein["resistance_inferred_from_reference"]
        is False
    )
    assert protein["complete_native_bibliography"][0]["reference_strain_comments"] == [
        "reference A",
        "reference B",
    ]
    assert "SEQUENCE_SENTINEL" not in json.dumps(protein)


@pytest.mark.parametrize(
    "change",
    [
        "wrong_gene",
        "locus_only",
        "orf_only",
        "duplicate_blocks",
        "wrong_taxon",
        "lineage_conflict",
        "review_status",
        "zero_version",
        "bool_version",
        "sequence",
        "features",
        "comments",
        "unknown_flag",
    ],
)
def test_reference_projection_guards(entry, change):
    taxon = taxonomy()
    if change in {"wrong_gene", "locus_only", "orf_only"}:
        entry["genes"][0]["geneName"]["value"] = "ompC"
        if change != "wrong_gene":
            field = "orderedLocusNames" if change == "locus_only" else "orfNames"
            entry["genes"][0][field] = [{"value": "ompF"}]
    elif change == "duplicate_blocks":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change == "wrong_taxon":
        entry["organism"]["taxonId"] = 1
    elif change == "lineage_conflict":
        taxon["lineage"][-1]["scientificName"] = "Other"
    elif change == "review_status":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change.endswith("version"):
        entry["entryAudit"]["entryVersion"] = True if change == "bool_version" else 0
    elif change == "unknown_flag":
        entry["proteinDescription"]["flag"] = "Other"
    else:
        entry[change] = []
    with pytest.raises(ValueError):
        audit.project(entry, taxon, named(), "ompF", True)


def test_native_synonym_matches_without_inventing_alias(entry):
    entry["genes"][0]["geneName"]["value"] = "ompC"
    entry["genes"][0]["synonyms"] = [{"value": "ompK36"}]
    result, matches = audit.project(entry, taxonomy(), named(), "OmpK36", True)
    assert matches == [{"gene_index": 0, "field": "synonyms", "value": "ompK36"}]
    assert result["gene_names"] == ["ompC", "ompK36"]
    entry["genes"][0]["synonyms"] = []
    with pytest.raises(ValueError):
        audit.project(entry, taxonomy(), named(), "OmpK36", True)


@pytest.mark.parametrize("flag", [None, "Fragment", "Precursor"])
def test_unreviewed_flags_are_not_coordinate_or_completeness_claims(entry, flag):
    entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    if flag:
        entry["proteinDescription"]["flag"] = flag
    else:
        del entry["proteinDescription"]["flag"]
    result, _ = audit.project(entry, taxonomy(), named(), "ompF", False)
    assert result["native_protein_flag"] == flag
    assert result["unflagged_means_complete"] is result["precursor_or_fragment_coordinates_inferred"] is False


def test_empty_query_and_suggestions_not_biological_absence(monkeypatch):
    monkeypatch.setattr(audit.native, "read_source", lambda *args: ({"results": [], "suggestions": [{}]}, {}))
    entries, query = audit.read_gene(ROOT, {"url": audit.gene_url(562, "ompF", True)}, 562, "ompF", True)
    assert entries == [] and query["complete_for_query"] is True
    assert query["zero_hit_is_biological_absence"] is query["suggestions_followed"] is False
    assert query["suggestions_ignored"] == 1


def test_wrong_gene_query_url_rejected_before_source_read(monkeypatch):
    def forbidden(*args):
        raise AssertionError("wrong query was read")

    monkeypatch.setattr(audit.native, "read_source", forbidden)
    with pytest.raises(ValueError, match="query identity"):
        audit.read_gene(ROOT, {"url": audit.gene_url(573, "ompF", True)}, 562, "ompF", True)


def test_contexts_do_not_merge_different_organisms_or_genes():
    terms = {
        str(i): {"source_organism_name": name, "source_gene_label": gene}
        for i, (name, gene) in enumerate(
            [
                ("Escherichia coli", "ompF"),
                ("Escherichia coli", "LamB"),
                (None, None),
                ("Escherichia coli", "ompF"),
            ]
        )
    }
    result = audit.contexts({"terms": terms}, {"Escherichia coli": {"selected_taxon": named()}})
    assert set(result) == {"Escherichia coli|ompF", "Escherichia coli|LamB"}
    assert audit.contexts({"terms": terms}, {"Escherichia coli": {"selected_taxon": None}}) == {}


def test_public_checkpoint_covers_complete_screen_independent_of_private_cache():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    index = json.loads((ROOT / result["inputs"]["index"]["path"]).read_bytes())
    labels = {
        r["determinant_id"]: r["determinant_name"]
        for r in csv.DictReader((ROOT / "data/raw/aro_resistance_edges.tsv").open(), delimiter="\t")
    }
    expected = {tid for tid in index["terms"] if audit.SELECT.search(labels[tid])}
    assert set(result["terms"]) == expected and len(expected) == 29
    assert result["scope"] == audit.SCOPE
    assert len(result["records"]) == 46 and len(result["claims"]) == 117
    assert len(result["names"]) == 8
    counts = Counter()
    used = set()
    for tid, term in result["terms"].items():
        assert term["source_label"] == labels[tid]
        identity = audit.source_identity(labels[tid])
        assert all(term[k] == v for k, v in identity.items())
        counts[identity["entity_scope"]] += 1
        assert term["record_memberships"] == index["terms"][tid]["record_memberships"]
        assert term["prior_reference_links"] == index["terms"][tid]["links"]
        if not term["source_organism_name"]:
            assert term["queries"] == {} and term["reference_candidates"] == []
            assert term["named_reference_taxon_id"] is None
        for candidate in term["reference_candidates"]:
            assert (
                candidate["experimental_subject_assignment"] is candidate["exact_resistant_allele"] is False
            )
            used.add(candidate["protein_accession"])
        assert term["primary_review_status"] == "OPEN"
    assert counts == {
        "ORGANISM_NAMED_SINGLE_PROTEIN_LABEL": 14,
        "COMPLEX_OR_REGULATORY_CONTEXT_NOT_SINGLE_PROTEIN": 13,
        "ORGANISM_UNSPECIFIED_NO_SPECIES_QUERY": 2,
    }
    assert used == set(result["proteins"])
    assert result["constraints"]["ncbi_requests"] == 0
    assert result["constraints"]["full_corpus_goal_status"] == "OPEN"
    assert "referencePositions" not in json.dumps(result)


def test_cli_output_is_immutable_and_check_does_not_create(monkeypatch, tmp_path):
    output = tmp_path / "output.json"
    monkeypatch.setattr(audit, "OUTPUT", output)
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    monkeypatch.setattr(sys, "argv", ["audit", "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    monkeypatch.setattr(sys, "argv", ["audit"])
    audit.main()
    audit.main()
    output.write_text("changed\n")
    with pytest.raises(ValueError, match="does not reproduce"):
        audit.main()
    assert output.read_text() == "changed\n"


@pytest.mark.parametrize(
    "names,expected",
    [
        (["Major outer membrane protein P.IB", "Porin"], None),
        (["Outer membrane protein PIB"], None),
        (["Outer membrane protein IA"], "NATIVE_IA_NOT_SOURCE_PIB"),
        (["Porin IA protein", "PorB"], "NATIVE_IA_NOT_SOURCE_PIB"),
        (["Hybrid outer membrane protein IA/IB"], "NATIVE_HYBRID_NOT_PURE_PIB"),
        (["Outer membrane protein PIB", "Outer membrane protein IA"], "CONFLICTING_NATIVE_SUBTYPE_NAMES"),
        (["Outer membrane protein I"], "NO_EXPLICIT_NATIVE_PIB_SUBTYPE_NOT_ABSENCE"),
        (["Porin"], "NO_EXPLICIT_NATIVE_PIB_SUBTYPE_NOT_ABSENCE"),
        (["PorB"], "NO_EXPLICIT_NATIVE_PIB_SUBTYPE_NOT_ABSENCE"),
    ],
)
def test_literal_por_is_not_automatically_pib(entry, names, expected):
    entry["proteinDescription"] = {"submissionNames": [{"fullName": {"value": n}} for n in names]}
    term = {"source_label": "Neisseria gonorrhoeae porin PIB (por)"}
    eligible, unresolved = audit.partition_candidates(term, [entry])
    if expected is None:
        assert eligible == [entry] and unresolved == []
    else:
        assert eligible == [] and unresolved[0]["reason"] == expected
        assert unresolved[0]["resistance_or_susceptibility_inferred"] is False


@pytest.mark.parametrize(
    "candidates,unresolved,reviewed,expected",
    [
        ([], [], True, "NO_EXACT_GENE_RESULTS_NOT_ABSENCE"),
        ([], [{}], True, "NO_SUBTYPE_ELIGIBLE_REFERENCE_CANDIDATES"),
        ([{}], [{}], True, "REVIEWED_REFERENCE"),
        ([{}], [], False, "UNREVIEWED_CANDIDATE"),
        ([{}, {}], [{}], False, "MULTIPLE_CANDIDATES_NO_SELECTION"),
    ],
)
def test_nonempty_subtype_candidates_never_reported_as_no_candidates(
    candidates, unresolved, reviewed, expected
):
    term = {"source_organism_name": "Organism species"}
    assert audit.candidate_status(term, {"reviewed": reviewed}, candidates, unresolved) == expected


def test_thesis_without_title_or_identifiers_is_not_erased(entry):
    ref = copy.deepcopy(entry["references"][0])
    ref["referenceNumber"] = 2
    ref["citation"] = {
        "id": "CI-THESIS",
        "citationType": "thesis",
        "authors": ["Author A."],
        "publicationDate": "1998",
        "institute": "Native institute",
    }
    entry["references"].append(ref)
    rows = audit.native_bibliography(entry)
    assert len(rows) == 2 and rows[1]["citation_type"] == "thesis"
    assert rows[1]["title"] is None and rows[1]["identifiers"] == []
    assert rows[1]["institute"] == "Native institute"
    assert rows[1]["reference_strain_comments"] == ["reference A", "reference B"]
    assert rows[1]["primary_results_reviewed"] is False
    assert "SEQUENCE_SENTINEL" not in json.dumps(rows)
    ref["referenceNumber"] = 1
    with pytest.raises(ValueError, match="reference number"):
        audit.native_bibliography(entry)


@pytest.mark.parametrize("change", ["empty_institute", "extra_field", "empty_authors"])
def test_unreviewed_thesis_shape_rejected(entry, change):
    citation = {
        "id": "CI-THESIS",
        "citationType": "thesis",
        "authors": ["Author A."],
        "publicationDate": "1998",
        "institute": "Native institute",
    }
    if change == "empty_institute":
        citation["institute"] = ""
    elif change == "extra_field":
        citation["title"] = "Previously uninspected title"
    else:
        citation["authors"] = []
    entry["references"][0]["citation"] = citation
    with pytest.raises(ValueError, match="thesis shape"):
        audit.native_bibliography(entry)


def test_public_subtype_accounting_flags_and_prior_reference_preservation():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    pib = result["terms"]["ARO:3000464"]
    selected = {r["protein_accession"] for r in pib["reference_candidates"]}
    unresolved = {r["protein_accession"] for r in pib["query_hits_not_assigned_to_source_subtype"]}
    hits = {"UniProtKB:" + a for a in pib["queries"]["unreviewed"]["accessions"]}
    assert len(selected) == 70 and len(unresolved) == 75
    assert not selected & unresolved and selected | unresolved == hits
    assert pib["reference_status"] == "MULTIPLE_CANDIDATES_NO_SELECTION"
    assert result["summary"]["subtype_dispositions"] == {
        "NATIVE_HYBRID_NOT_PURE_PIB": 1,
        "NATIVE_IA_NOT_SOURCE_PIB": 9,
        "NO_EXPLICIT_NATIVE_PIB_SUBTYPE_NOT_ABSENCE": 65,
    }
    assert result["summary"]["native_protein_flags"] == {"Fragment": 47, "None": 50, "Precursor": 27}
    assert result["summary"]["bibliography_types"] == {"journal article": 186, "submission": 45, "thesis": 1}
    old = result["terms"]["ARO:3004123"]
    assert old["prior_reference_links"][0]["protein_accession"] == "UniProtKB:A0A069BCC8"
    assert old["reference_candidates"][0]["protein_accession"] == "UniProtKB:Q7WZL2"
    assert old["prior_reference_links_source"] == {"input": "index", "pointer": "/terms/ARO:3004123/links"}
    assert old["prior_link_pointers_resolve_within_pinned_index"] is True
    truncated = result["proteins"]["UniProtKB:A0A075BU96"]
    assert truncated["native_protein_flag"] is None and truncated["unflagged_means_complete"] is False
