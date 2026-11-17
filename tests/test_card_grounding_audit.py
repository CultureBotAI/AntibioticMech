"""Explicit reference links never establish tested isolate or allele identity."""

import copy
import csv
import json
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_card_grounding as card  # noqa: E402


def entry(accession="P1", aro="ARO:1", taxid=1):
    return {
        "primaryAccession": accession, "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"sequenceVersion": 1},
        "organism": {"taxonId": taxid, "scientificName": "Reference organism"},
        "genes": [{"geneName": {"value": "geneA"}}],
        "uniProtKBCrossReferences": [{"database": "CARD", "id": aro,
                                      "properties": [{"key": "CARD short name", "value": "geneB"}]}],
    }


def link(cursor="next", **overrides):
    params = {**card.PARAMS, "cursor": cursor, **overrides}
    return '<https://rest.uniprot.org/uniprotkb/search?' + urlencode(params) + '>; rel="next"'


def response(entries, total=2, release="release-1", next_link=""):
    return {"status": 200, "headers": {"x-total-results": str(total),
                                       "x-uniprot-release": release, "link": next_link},
            "body": json.dumps({"results": entries})}


def search(monkeypatch, responses):
    iterator = iter(responses)
    monkeypatch.setattr(card.common, "fetch", lambda *args, **kwargs: next(iterator))
    return card.search_proteins()


def test_complete_pagination_retains_every_protein(monkeypatch):
    result = search(monkeypatch, [response([entry()], next_link=link()), response([entry("P2")])])
    assert set(result["entries"]) == {"P1", "P2"}
    assert result["total"] == 2
    assert len(result["requests"]) == 2


def test_truncated_search_is_not_a_complete_cohort(monkeypatch):
    with pytest.raises(ValueError, match="incomplete"):
        search(monkeypatch, [response([entry()])])


@pytest.mark.parametrize("change", [{"total": 3}, {"release": "release-2"}])
def test_release_or_count_drift_is_refused(monkeypatch, change):
    with pytest.raises(ValueError, match="changed during pagination"):
        search(monkeypatch, [response([entry()], next_link=link()), response([entry("P2")], **change)])


def test_duplicate_proteins_are_not_silently_collapsed(monkeypatch):
    with pytest.raises(ValueError, match="duplicate protein"):
        search(monkeypatch, [response([entry()], next_link=link()), response([entry()])])


@pytest.mark.parametrize("url", [
    link().replace("https://rest.uniprot.org", "https://example.org"),
    link().replace("https://", "http://"),
    link(query="organism_id:1"),
    link().replace("/uniprotkb/search?", "/taxonomy/search?"),
])
def test_pagination_cannot_change_host_or_query(url):
    with pytest.raises(ValueError, match="approved UniProt endpoint|query drift"):
        card.next_page(url, card.PARAMS)


def test_matching_gene_name_is_not_a_cross_reference():
    protein = entry()
    protein["uniProtKBCrossReferences"] = [{"database": "Other", "id": "ARO:1"}]
    assert dict(card.reference_index({"P1": protein}, {"ARO:1"})) == {}


def test_one_to_many_reference_candidates_are_preserved():
    result = card.reference_index({"P1": entry(), "P2": entry("P2")}, {"ARO:1"})
    assert len(result["ARO:1"]) == 2


def test_inconsistent_duplicate_card_crossrefs_are_refused():
    protein = entry()
    protein["uniProtKBCrossReferences"] *= 2
    with pytest.raises(ValueError, match="duplicate CARD"):
        card.reference_index({"P1": protein}, {"ARO:1"})


def test_reference_taxonomy_and_gene_names_do_not_ground_an_allele():
    protein = entry()
    row = card.candidate(protein, protein["uniProtKBCrossReferences"][0], {
        "1": {"active": True, "rank": "species", "scientificName": "Reference organism"},
    })
    assert row["reference_taxon_id"] == "NCBITaxon:1"
    assert row["gene_name_comparison"] == "NAMES_DIFFER_REVIEW_REQUIRED"
    assert row["evidence_scope"] == "EXPLICIT_REFERENCE_LINK_NOT_EXPERIMENTAL_ALLELE_GROUNDING"
    assert "strain" not in row
    assert "alteration" not in row


def test_unresolved_taxonomy_is_not_reported_as_verified():
    protein = entry()
    row = card.candidate(protein, protein["uniProtKBCrossReferences"][0], {"1": {"unresolved_status": 404}})
    assert row["taxonomy_status"] == "REFERENCE_TAXON_REVIEW_REQUIRED"
    assert row["taxonomy_name"] is None


def test_curator_upgraded_aro_claims_are_not_owned_by_card():
    records = [{"resistance_mechanisms": [
        {"aro_id": "ARO:1", "evidence": [{"reference": "PMID:1"}]},
        {"aro_id": "ARO:2", "evidence": [{"reference": "ARO:2", "notes": "CARD/ARO asserts ..."}]},
    ]}]
    assert [c["aro_id"] for _, c in card.claims_from(records)] == ["ARO:2"]


def test_census_drift_is_refused(tmp_path, monkeypatch):
    output = tmp_path / "output"
    output.mkdir()
    monkeypatch.setattr(card.common, "OUT", output)
    path = tmp_path / "data/antibiotics/antibacterial/example.yaml"
    path.parent.mkdir(parents=True)
    path.write_text("original")
    record = {"path": str(path.relative_to(tmp_path)), "identifier": "CHEBI:1",
              "sha256": card.common.digest(path.read_bytes())}
    (output / "corpus.json").write_text(json.dumps({"records": [record]}))
    path.write_text("changed")
    with pytest.raises(ValueError, match="snapshot drift"):
        card.current_corpus(tmp_path)


@pytest.fixture
def cohort(tmp_path, monkeypatch):
    output = tmp_path / "output"
    output.mkdir()
    monkeypatch.setattr(card.common, "OUT", output)
    source = tmp_path / card.SOURCE
    source.parent.mkdir(parents=True)
    source.write_text("determinant_id\nARO:1\nARO:2\n")
    path = tmp_path / "data/antibiotics/antibacterial/example.yaml"
    path.parent.mkdir(parents=True)
    path.write_text("original")
    record = {
        "identifier": "CHEBI:1", "label": "Example", "path": str(path.relative_to(tmp_path)),
        "sha256": card.common.digest(path.read_bytes()), "standard_inchi_key": "EXAMPLE",
        "resistance_mechanisms": [
            {"aro_id": aro, "label": aro,
             "evidence": [{"reference": aro, "notes": "CARD/ARO asserts ..."}]}
            for aro in ("ARO:1", "ARO:2")
        ],
    }
    card.common.write("corpus.json", {"records": [record]})
    card.common.write("card-proteins.json", {
        "entries": {"P1": entry(), "P2": entry("P2")}, "requests": [], "release": "release-1",
        "query": card.PARAMS, "total": 2,
        "source_inventory_sha256": card.common.digest(source.read_bytes()),
        "corpus_sha256": card.common.digest((output / "corpus.json").read_bytes()),
    })
    card.common.write("card-taxonomy.json", {
        "taxa": {"1": {"active": True, "rank": "species", "scientificName": "Reference"}},
        "requests": [],
        "proteins_sha256": card.common.digest((output / "card-proteins.json").read_bytes()),
    })
    return tmp_path, output, path


def test_analysis_covers_unmatched_and_one_to_many_claims_without_record_edits(cohort):
    root, output, path = cohort
    before = path.read_bytes()
    card.analyze(root)
    result = json.loads((output / "card-reference-grounding.json").read_text())
    assert result["summary"]["card_assertions"] == 2
    assert result["summary"]["card_determinants"] == 2
    assert result["summary"]["candidate_proteins"] == 2
    assert result["summary"]["candidate_links"] == 2
    assert result["determinants"]["ARO:2"]["status"] == "NO_EXPLICIT_LINK_IN_THIS_RELEASE"
    assert result["determinants"]["ARO:1"]["status"] == "MULTIPLE_REFERENCE_CANDIDATES_RETAINED"
    with (output / "card-reference-ledger.tsv").open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(rows) == 2
    assert {r["aro_id"] for r in rows} == {"ARO:1", "ARO:2"}
    assert {r["primary_review_status"] for r in rows} == {"PENDING"}
    assert all(r["record_sha256"] == card.common.digest(before) for r in rows)
    assert rows[0]["candidate_accessions"] == "UniProtKB:P1|UniProtKB:P2"
    assert rows[1]["candidate_accessions"] == ""
    assert path.read_bytes() == before


def test_analysis_refuses_taxonomy_from_another_protein_snapshot(cohort):
    root, output, _ = cohort
    taxonomy = json.loads((output / "card-taxonomy.json").read_text())
    taxonomy["proteins_sha256"] = "old"
    card.common.write("card-taxonomy.json", taxonomy)
    with pytest.raises(ValueError, match="another protein snapshot"):
        card.analyze(root)


def test_analysis_refuses_changed_card_source(cohort):
    root, _, _ = cohort
    (root / card.SOURCE).write_text("determinant_id\nARO:3\n")
    with pytest.raises(ValueError, match="source inventory drift"):
        card.analyze(root)


def test_taxonomy_refuses_a_concurrent_protein_refresh(cohort, monkeypatch):
    root, output, _ = cohort
    before = (output / "card-taxonomy.json").read_bytes()

    def fetch(*args):
        proteins = json.loads((output / "card-proteins.json").read_text())
        proteins["release"] = "new-release"
        card.common.write("card-proteins.json", proteins)
        return {"status": 200, "body": json.dumps({"taxonId": 1, "active": True})}

    monkeypatch.setattr(card.common, "fetch", fetch)
    with pytest.raises(ValueError, match="changed during taxonomy retrieval"):
        card.taxonomy(root)
    assert (output / "card-taxonomy.json").read_bytes() == before


def test_analysis_refuses_a_concurrent_taxonomy_refresh(cohort, monkeypatch):
    root, output, _ = cohort
    original_candidate = card.candidate

    def candidate(*args):
        card.common.write("card-taxonomy.json", {"changed": True})
        return original_candidate(*args)

    monkeypatch.setattr(card, "candidate", candidate)
    with pytest.raises(ValueError, match="grounding inputs changed"):
        card.analyze(root)
    assert not (output / "card-reference-grounding.json").exists()


def reference(number=1, strain="Study A", pmid="101"):
    return {
        "referenceNumber": number,
        "citation": {"id": pmid, "citationType": "journal article", "publicationDate": "2008",
                     "citationCrossReferences": [{"database": "PubMed", "id": pmid}],
                     "title": "Not exported"},
        "referenceComments": [
            {"type": "STRAIN", "value": strain,
             "evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "ABC1.1"}]},
            {"type": "PLASMID", "value": "Not exported"},
        ],
        "referencePositions": ["Not exported"],
        "evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "ABC1.1"}],
    }


def test_context_preserves_each_citation_strain_binding_without_entry_assignment():
    protein = entry()
    protein["references"] = [reference(), reference(2, "Study B", "202")]
    before = copy.deepcopy(protein)
    contexts = card.reference_contexts(protein)
    assert [r["citation"]["id"] for r in contexts] == ["101", "202"]
    assert [r["strain_annotations"][0]["value"] for r in contexts] == ["Study A", "Study B"]
    assert all(r["omitted_comment_types"] == ["PLASMID"] for r in contexts)
    assert "Not exported" not in json.dumps(contexts)
    contexts[0]["strain_annotations"][0]["value"] = "changed"
    contexts[0]["evidences"][0]["id"] = "changed"
    contexts[0]["citation"]["citationCrossReferences"][0]["id"] = "changed"
    assert protein == before


def test_missing_citations_and_strains_are_not_inferred():
    assert card.reference_contexts(entry()) == []
    protein = entry()
    protein["references"] = [{"referenceNumber": 1,
                              "citation": {"id": "CI:1", "citationType": "submission"}}]
    result, = card.reference_contexts(protein)
    assert result["citation"] == {"id": "CI:1", "citationType": "submission", "citationCrossReferences": []}
    assert result["strain_annotations"] == [] and result["evidences"] == []


def test_repeated_citations_and_compound_strain_labels_are_not_split_or_collapsed():
    protein = entry()
    protein["references"] = [reference(strain="A / B, C"), reference(2, "D", "101")]
    result = card.reference_contexts(protein)
    assert len(result) == 2
    assert [r["citation"]["id"] for r in result] == ["101", "101"]
    assert [[s["value"] for s in r["strain_annotations"]] for r in result] == [["A / B, C"], ["D"]]


@pytest.mark.parametrize("change", [
    {"referenceNumber": True}, {"referenceNumber": 0}, {"referenceNumber": "1"},
    {"citation": None}, {"citation": {"id": "101"}},
    {"citation": {"id": "101", "citationType": ""}},
    {"citation": {"id": "101", "citationType": "submission", "publicationDate": None}},
    {"citation": {"id": "101", "citationType": "submission", "citationCrossReferences": None}},
    {"referenceComments": [{"type": "STRAIN", "value": ""}]},
    {"referenceComments": [{"type": "STRAIN", "value": "A", "sequence": "not metadata"}]},
    {"referenceComments": [{"type": "STRAIN", "value": "A", "evidences": None}]},
    {"evidences": [{"source": "EMBL", "id": "ABC1.1"}]},
    {"evidences": [{"evidenceCode": "ECO:0000313", "sequence": "not metadata"}]},
])
def test_malformed_reference_context_is_refused(change):
    protein = entry()
    protein["references"] = [{**reference(), **change}]
    with pytest.raises(ValueError):
        card.reference_contexts(protein)


def test_duplicate_reference_numbers_are_not_collapsed():
    protein = entry()
    protein["references"] = [reference(), reference(strain="Another study")]
    with pytest.raises(ValueError, match="duplicate"):
        card.reference_contexts(protein)


def test_context_export_preserves_audit_census_and_records(cohort):
    root, output, record = cohort
    card.analyze(root)
    protected = {p: p.read_bytes() for p in (
        record, output / "corpus.json", output / "card-reference-grounding.json",
        output / "card-reference-ledger.tsv", output / "card-proteins.json", output / "card-taxonomy.json",
    )}
    card.contexts(root)
    result = json.loads((output / "card-citation-context.json").read_bytes())
    assert result["scope"] == card.CONTEXT_SCOPE
    assert result["summary"]["reference_proteins"] == 2
    assert result["summary"]["proteins_without_citation_context"] == 2
    assert result["summary"]["citation_contexts"] == 0
    for protein in result["proteins"].values():
        assert protein["primary_review_status"] == "PENDING"
        assert protein["reference_contexts"] == []
        assert protein["corpus_memberships"] == [
            {"identifier": "CHEBI:1", "aro_id": "ARO:1", "source_assertion_count": 1},
        ]
        assert "strain_taxon_id" not in protein and "strain" not in protein
    for path, payload in protected.items():
        assert path.read_bytes() == payload
    first = (output / "card-citation-context.json").read_bytes()
    card.contexts(root)
    assert (output / "card-citation-context.json").read_bytes() == first


@pytest.mark.parametrize("kind", ["snapshot", "determinants", "candidates", "duplicate_candidates"])
def test_context_export_refuses_changed_candidate_audit(cohort, kind):
    root, output, _ = cohort
    card.analyze(root)
    path = output / "card-reference-grounding.json"
    audit = json.loads(path.read_bytes())
    if kind == "snapshot":
        audit["protein_snapshot_sha256"] = "old"
    elif kind == "determinants":
        del audit["determinants"]["ARO:2"]
    elif kind == "candidates":
        audit["determinants"]["ARO:1"]["candidates"].pop()
    else:
        audit["determinants"]["ARO:1"]["candidates"] *= 2
    path.write_text(json.dumps(audit))
    with pytest.raises(ValueError, match="snapshot|coverage drift"):
        card.contexts(root)
    assert not (output / "card-citation-context.json").exists()


def test_context_export_refuses_concurrent_source_refresh(cohort, monkeypatch):
    root, output, _ = cohort
    card.analyze(root)
    original = card.reference_contexts

    def changed(protein):
        path = output / "card-proteins.json"
        payload = json.loads(path.read_bytes())
        payload["release"] = "changed-during-analysis"
        path.write_text(json.dumps(payload))
        return original(protein)

    monkeypatch.setattr(card, "reference_contexts", changed)
    with pytest.raises(ValueError, match="changed during context analysis"):
        card.contexts(root)
    assert not (output / "card-citation-context.json").exists()


def test_archive_identity_does_not_merge_distinct_reference_taxa_or_entries():
    first, second = entry("P1", taxid=1), entry("P2", taxid=2)
    for protein in (first, second):
        protein["extraAttributes"] = {"uniParcId": "UPI0000551E0C"}
    original = copy.deepcopy({"P1": first, "P2": second})
    result = card.archive_groups(original)
    assert result["archive_groups"] == {"UPI0000551E0C": ["UniProtKB:P1", "UniProtKB:P2"]}
    assert result["proteins"]["UniProtKB:P1"]["reference_taxon_id"] == "NCBITaxon:1"
    assert result["proteins"]["UniProtKB:P2"]["reference_taxon_id"] == "NCBITaxon:2"
    assert result["summary"] == {
        "reference_proteins": 2, "archive_identifiers": 1, "shared_archive_identifiers": 1,
        "proteins_with_shared_archive_id": 2, "proteins_without_archive_id": 0,
    }
    assert original == {"P1": first, "P2": second}
    result["proteins"]["UniProtKB:P1"]["entry_audit"]["sequenceVersion"] = 9
    assert original["P1"]["entryAudit"]["sequenceVersion"] == 1
    assert "representative" not in result


def test_missing_archive_metadata_remains_an_explicit_gap():
    result = card.archive_groups({"P1": entry()})
    assert result["proteins_without_archive_id"] == ["UniProtKB:P1"]
    assert result["proteins"]["UniProtKB:P1"]["uniparc_id"] is None
    assert result["archive_groups"] == {}
    assert result["summary"]["reference_proteins"] == 1
    assert result["summary"]["proteins_without_archive_id"] == 1


def test_empty_archive_cohort_is_valid_without_invented_groups():
    result = card.archive_groups({})
    assert result["archive_groups"] == result["proteins"] == {}
    assert result["proteins_without_archive_id"] == []
    assert all(count == 0 for count in result["summary"].values())


@pytest.mark.parametrize("value", ["", "UPI123", "UPI0000551e0c", " UPI0000551E0C", {}, True])
def test_malformed_archive_identifiers_fail_closed(value):
    protein = entry()
    protein["extraAttributes"] = {"uniParcId": value}
    with pytest.raises(ValueError, match="invalid UniParc"):
        card.archive_groups({"P1": protein})


@pytest.mark.parametrize("value", [None, [], "UPI0000551E0C"])
def test_invalid_archive_attribute_container_fails_closed(value):
    protein = entry()
    protein["extraAttributes"] = value
    with pytest.raises(ValueError, match="invalid UniProt extra attributes"):
        card.archive_groups({"P1": protein})


def test_archive_projection_checks_accession_identity():
    with pytest.raises(ValueError, match="accession/key mismatch"):
        card.archive_groups({"P2": entry("P1")})


def test_archive_stage_preserves_source_records_and_reference_snapshots(cohort):
    root, output, record = cohort
    card.analyze(root)
    before = {p: p.read_bytes() for p in output.glob("*.json")}
    before[record] = record.read_bytes()
    card.archives(root)
    result = json.loads((output / "card-archive-groups.json").read_bytes())
    assert result["scope"] == card.ARCHIVE_SCOPE
    assert result["summary"]["reference_proteins"] == 2
    assert result["summary"]["proteins_without_archive_id"] == 2
    assert result["multiple_candidate_determinants"] == {"ARO:1": ["UniProtKB:P1", "UniProtKB:P2"]}
    assert all(p.read_bytes() == payload for p, payload in before.items())
    exported = (output / "card-archive-groups.json").read_bytes()
    card.archives(root)
    assert (output / "card-archive-groups.json").read_bytes() == exported


def test_archive_stage_refuses_concurrent_protein_refresh(cohort, monkeypatch):
    root, output, _ = cohort
    original = card.archive_groups

    def changed(entries):
        path = output / "card-proteins.json"
        payload = json.loads(path.read_bytes())
        payload["release"] = "changed-during-analysis"
        path.write_text(json.dumps(payload))
        return original(entries)

    monkeypatch.setattr(card, "archive_groups", changed)
    with pytest.raises(ValueError, match="changed during archive analysis"):
        card.archives(root)
    assert not (output / "card-archive-groups.json").exists()
