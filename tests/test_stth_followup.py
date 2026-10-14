"""Shared species, gene symbols and publications are not allele identity."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_stth_followup as audit  # noqa: E402


@pytest.fixture
def reference_input():
    rows = []
    for accession, versions in audit.VERSIONS.items():
        entry = {
            "primaryAccession": accession,
            "entryType": "UniProtKB reviewed (Swiss-Prot)"
            if accession in audit.GENES
            else "UniProtKB unreviewed (TrEMBL)",
            "entryAudit": dict(zip(("entryVersion", "sequenceVersion"), versions, strict=True)),
            "organism": {"taxonId": 1971, "scientificName": "Streptomyces noursei"},
            "proteinDescription": {"recommendedName": {"fullName": {"value": "Streptothricin hydrolase"}}},
            "references": [
                {
                    "citation": {
                        "citationCrossReferences": [
                            {"database": "PubMed", "id": "19897889"},
                            {"database": "DOI", "id": audit.DOI.upper()},
                        ]
                    },
                    "referencePositions": ["NOT FOR EXPORT"],
                }
            ],
        }
        if accession in audit.GENES:
            entry["genes"] = [{"geneName": {"value": "sttH"}}]
            if accession == "C5NU54":
                entry["genes"][0]["synonyms"] = [{"value": "sttH-sn"}]
        rows.append(entry)
    taxon = {
        "taxonId": 1971,
        "scientificName": "Streptomyces noursei",
        "rank": "species",
        "active": True,
        "synonyms": ["Streptomyces albulus"],
        "lineage": [],
    }
    return {"results": rows}, {"X-UniProt-Release": "2026_03", "X-Total-Results": "9"}, taxon


def test_same_symbol_and_species_do_not_merge_reference_accessions(reference_input):
    result = audit.project_references(*reference_input)
    assert [r["protein_accession"] for r in result["selected_references"]] == [
        "UniProtKB:C5NU54",
        "UniProtKB:Q1MW86",
    ]
    assert [r["gene_names"] for r in result["selected_references"]] == [["sttH", "sttH-sn"], ["sttH"]]
    for row in result["selected_references"]:
        assert row["reference_species_taxon_id"] == "NCBITaxon:1971"
        assert row["exact_resistance_allele"] is False
        assert row["experimental_subject_assignment"] is False
        assert row["primary_results_reviewed"] is False
    assert result["same_symbol_or_species_establishes_same_locus_or_allele"] is False
    assert result["reference_accessions_merged"] is False
    assert result["shared_citation_is_causality"] is False
    assert len(result["other_citation_entries"]) == 7
    assert all(r["resistance_absence_inferred"] is False for r in result["other_citation_entries"])
    assert "NOT FOR EXPORT" not in json.dumps(result)


def test_reference_projection_is_order_independent(reference_input):
    expected = audit.project_references(*reference_input)
    reference_input[0]["results"].reverse()
    assert audit.project_references(*reference_input) == expected


def test_shared_gene_symbol_does_not_promote_other_cited_protein(reference_input):
    reference_input[0]["results"][-1]["genes"] = [{"geneName": {"value": "sttH"}}]
    result = audit.project_references(*reference_input)
    assert len(result["selected_references"]) == 2
    (row,) = [r for r in result["other_citation_entries"] if r["accession"] == "UniProtKB:C5NU53"]
    assert row["role"] == "SHARED_CITATION_NOT_SELECTED_AS_RESISTANCE_DETERMINANT"


@pytest.mark.parametrize(
    "change",
    [
        "null",
        "nonlist",
        "nonobject",
        "missing",
        "duplicate",
        "accession",
        "pagination",
        "count",
        "release",
        "version",
        "sequence_version",
        "boolean_version",
        "version_null",
        "reference_taxon",
        "organism_null",
        "organism_name",
        "reviewed",
        "gene",
        "alias",
        "ambiguous_gene",
        "protein_name",
        "pmid",
        "doi",
        "split_citation",
        "sequence",
        "features",
        "comments",
        "other_sequence",
        "other_pmid",
        "other_reviewed",
        "taxonomy_id",
        "taxonomy_rank",
        "taxonomy_name",
        "inactive",
        "synonym",
    ],
)
def test_publication_reference_guards(reference_input, change):
    data, headers, taxon = reference_input
    entry = data["results"][1]
    if change == "null":
        data = None
    elif change == "nonlist":
        data["results"] = {}
    elif change == "nonobject":
        data["results"][0] = None
    elif change == "missing":
        data["results"].pop()
    elif change == "duplicate":
        data["results"][-1] = copy.deepcopy(entry)
    elif change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change in {"pagination", "count", "release"}:
        headers[
            {"pagination": "Link", "count": "X-Total-Results", "release": "X-UniProt-Release"}[change]
        ] = "OTHER"
    elif change in {"version", "sequence_version", "boolean_version"}:
        key = "sequenceVersion" if change == "sequence_version" else "entryVersion"
        entry["entryAudit"][key] = True if change == "boolean_version" else 999
    elif change == "version_null":
        entry["entryAudit"] = None
    elif change == "reference_taxon":
        entry["organism"]["taxonId"] = 1972
    elif change == "organism_null":
        entry["organism"] = None
    elif change == "organism_name":
        entry["organism"]["scientificName"] = "OTHER"
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "OTHER"
    elif change == "alias":
        entry["genes"][0]["synonyms"] = []
    elif change == "ambiguous_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change == "protein_name":
        entry["proteinDescription"]["recommendedName"]["fullName"]["value"] = "OTHER"
    elif change in {"pmid", "doi", "other_pmid"}:
        if change == "other_pmid":
            entry = data["results"][-1]
        entry["references"][0]["citation"]["citationCrossReferences"][1 if change == "doi" else 0]["id"] = (
            "OTHER"
        )
    elif change == "split_citation":
        refs = entry["references"][0]["citation"]["citationCrossReferences"]
        entry["references"] = [{"citation": {"citationCrossReferences": [ref]}} for ref in refs]
    elif change == "other_sequence":
        data["results"][-1]["sequence"] = {}
    elif change == "other_reviewed":
        data["results"][-1]["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif change.startswith("taxonomy_"):
        taxon[
            {"taxonomy_id": "taxonId", "taxonomy_rank": "rank", "taxonomy_name": "scientificName"}[change]
        ] = "OTHER"
    elif change == "inactive":
        taxon["active"] = False
    elif change == "synonym":
        taxon["synonyms"] = []
        taxon["commonName"] = "Streptomyces albulus"
    else:
        entry[change] = []
    with pytest.raises(ValueError):
        audit.project_references(data, headers, taxon)


@pytest.mark.parametrize("change", ["missing_receipt", "missing_attempt", "unresolved_attempt"])
def test_incomplete_request_coverage_fails_closed(tmp_path, change):
    directory = tmp_path / "cache"
    directory.mkdir()
    for key in ("reference-2009", "primary-doi", "primary-publisher"):
        for suffix in ("receipt", "attempt"):
            (directory / f"{key}-{suffix}.json").touch()
    if change == "unresolved_attempt":
        (directory / "unreported-attempt.json").touch()
    else:
        (directory / f"primary-publisher-{change.removeprefix('missing_')}.json").unlink()
    with pytest.raises(ValueError, match="research request coverage"):
        audit.build(tmp_path, Path("cache"))


def test_public_checkpoint_preserves_holds_and_subject_boundaries():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["corpus_records_hash_checked_at_preflight"] == 2939
    assert len(result["records"]) == 3
    assert result["reference_comparison"]["shared_reference_projection_identical"] is True
    assert (
        result["reference_comparison"]["additional_reference_relative_to_prior_checkpoint"]
        == "UniProtKB:C5NU54"
    )
    assert result["reference_comparison"]["experimental_subjects_equated"] is False
    assert result["primary_access"]["disposition"] == "ACCESS_HOLD"
    assert result["primary_access"]["terminal_status"] == 403
    assert result["primary_access"]["primary_results_reviewed"] is False
    assert result["primary_access"]["distinct_study_not_alternate_copy_of_held_2006_paper"] is True
    assert result["curation_decision"] == "NO_NEW_RESISTANCE_ASSERTION_OR_EXPERIMENTAL_IDENTIFIER"
    assert result["limits"]["scientific_http_attempts"] == 3
    assert result["limits"]["held_2006_and_2017_primary_studies_not_retried"] is True
    assert result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"


@pytest.mark.parametrize("change", ["none", "manual_flag", "binding", "shared_reference"])
def test_offline_replay_preserves_prior_reference_and_manual_redirect(monkeypatch, change):
    if not (ROOT / audit.CACHE / "primary-publisher-receipt.json").exists():
        pytest.skip("private source cache is not distributed")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    original_open, original_loads = Path.open, json.loads
    original_projection = audit.project_references

    def guarded(path, *args, **kwargs):
        assert not path.resolve().is_relative_to(ROOT / "data/antibiotics")
        return original_open(path, *args, **kwargs)

    def altered_loads(*args, **kwargs):
        value = original_loads(*args, **kwargs)
        if (
            isinstance(value, dict)
            and "redirect_receipt" in value
            and "stth-followup" in value["redirect_receipt"]["path"]
        ):
            if change == "manual_flag":
                value["manual_redirect_reviewed"] = False
            elif change == "binding":
                value["redirect_receipt"]["sha256"] = "0" * 64
        return value

    def altered_projection(*args, **kwargs):
        value = original_projection(*args, **kwargs)
        if change == "shared_reference":
            (row,) = [r for r in value["selected_references"] if r["protein_accession"] == "UniProtKB:Q1MW86"]
            row["entry_version"] += 1
        return value

    monkeypatch.setattr(Path, "open", guarded)
    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(json, "loads", altered_loads)
    monkeypatch.setattr(audit, "project_references", altered_projection)
    if change == "none":
        assert audit.build(ROOT) == original_loads((ROOT / audit.OUTPUT).read_bytes())
    else:
        message = "shared protein reference" if change == "shared_reference" else "manual publisher redirect"
        with pytest.raises(ValueError, match=message):
            audit.build(ROOT)
