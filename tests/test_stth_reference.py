"""Publication membership and reference names do not establish tested alleles."""

import copy
import json
import socket
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_stth_reference as audit  # noqa: E402


@pytest.fixture
def reference_input():
    rows = []
    for accession, versions in audit.VERSIONS.items():
        rows.append(
            {
                "primaryAccession": accession,
                "entryType": "UniProtKB reviewed (Swiss-Prot)"
                if accession == "Q1MW86"
                else "UniProtKB unreviewed (TrEMBL)",
                "entryAudit": dict(zip(("entryVersion", "sequenceVersion"), versions, strict=True)),
                "organism": {"taxonId": 1971, "scientificName": "Streptomyces noursei"},
                "genes": [{"geneName": {"value": "sttH"}}] if accession == "Q1MW86" else [],
                "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference protein"}}},
                "references": [
                    {
                        "citation": {
                            "citationCrossReferences": [
                                {"database": "PubMed", "id": "16641084"},
                                {"database": "DOI", "id": audit.DOI.upper()},
                            ]
                        },
                        "referencePositions": ["NOT FOR EXPORT"],
                    }
                ],
            }
        )
    taxon = {
        "taxonId": 1971,
        "scientificName": "Streptomyces noursei",
        "active": True,
        "rank": "species",
        "synonyms": ["Streptomyces albulus"],
        "lineage": [],
    }
    return {"results": rows}, {"X-UniProt-Release": "2026_03", "X-Total-Results": "7"}, taxon


def test_reference_selection_does_not_promote_shared_citations(reference_input):
    result = audit.project_references(*reference_input)
    selected = result["selected_reference"]
    assert selected["protein_accession"] == "UniProtKB:Q1MW86"
    assert selected["reference_species_taxon_id"] == "NCBITaxon:1971"
    assert selected["exact_resistance_allele"] is False
    assert selected["experimental_subject_assignment"] is False
    assert selected["primary_results_reviewed"] is False
    assert result["shared_citation_is_causality"] is False
    assert len(result["other_citation_entries"]) == 6
    for entry in result["other_citation_entries"]:
        assert entry["role"] == "SHARED_CITATION_NOT_SELECTED_AS_RESISTANCE_DETERMINANT"
        assert entry["resistance_absence_inferred"] is False
    assert "NOT FOR EXPORT" not in json.dumps(result)


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
        "reference_taxon",
        "organism_name",
        "reviewed",
        "gene",
        "ambiguous_gene",
        "pmid",
        "doi",
        "split_citation",
        "sequence",
        "features",
        "comments",
        "other_sequence",
        "other_pmid",
    ],
)
def test_reference_guards(reference_input, change):
    data, headers, taxon = reference_input
    entry = data["results"][0]
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
    elif change == "reference_taxon":
        entry["organism"]["taxonId"] = 1972
    elif change == "organism_name":
        entry["organism"]["scientificName"] = "OTHER"
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "OTHER"
    elif change == "ambiguous_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
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
    else:
        entry[change] = []
    with pytest.raises(ValueError):
        audit.project_references(data, headers, taxon)


@pytest.mark.parametrize(
    "change", ["taxid", "inactive", "rank", "name", "common_name", "other_names", "string", "missing"]
)
def test_taxonomy_requires_explicit_species_synonym(reference_input, change):
    taxon = reference_input[2]
    if change == "taxid":
        taxon["taxonId"] = "1971"
    elif change == "inactive":
        taxon["active"] = False
    elif change == "rank":
        taxon["rank"] = "strain"
    elif change == "name":
        taxon["scientificName"] = "OTHER"
    else:
        taxon.pop("synonyms")
        if change == "common_name":
            taxon["commonName"] = "Streptomyces albulus"
        elif change == "other_names":
            taxon["otherNames"] = ["Streptomyces albulus"]
        elif change == "string":
            taxon["synonyms"] = "Streptomyces albulus"
    with pytest.raises(ValueError):
        audit.synonym_scope(taxon)


@pytest.mark.parametrize(
    "change",
    [
        "none",
        "title",
        "missing",
        "duplicate",
        "syntax",
        "host",
        "http",
        "paper",
        "path",
        "fragment",
        "duplicate_key",
        "empty_key",
        "duplicate_redirect",
        "extra_parameter",
    ],
)
def test_html_200_locator_is_only_an_exact_manual_redirect(change):
    params = [("Redirect", f"https://jbc.org/retrieve/pii/{audit.PII}"), ("key", "opaque")]
    if change == "paper":
        params[0] = ("Redirect", "https://jbc.org/retrieve/pii/OTHER")
    elif change in {"duplicate_key", "duplicate_redirect"}:
        params.append(params[1 if change == "duplicate_key" else 0])
    elif change == "empty_key":
        params[1] = ("key", "")
    elif change == "extra_parameter":
        params.append(("other", "1"))
    destination = "/retrieve/articleSelectPrefsTemp?" + urlencode(params)
    if change == "host":
        destination = "https://www.ncbi.nlm.nih.gov" + destination
    elif change == "http":
        destination = "http://linkinghub.elsevier.com" + destination
    elif change == "path":
        destination = destination.replace("articleSelectPrefsTemp", "OTHER")
    elif change == "fragment":
        destination += "#other"
    content = f"0;url='{destination}'" if change != "syntax" else "invalid"
    meta = f'<meta http-equiv="Refresh" content="{content}">'
    if change == "missing":
        meta = ""
    elif change == "duplicate":
        meta *= 2
    title = "Redirecting" if change != "title" else "Article"
    payload = f"<html><head><title>{title}</title>{meta}</head></html>".encode()
    base = f"https://linkinghub.elsevier.com/retrieve/pii/{audit.PII}"
    if change == "none":
        assert audit.locator_destination(payload, base) == "https://linkinghub.elsevier.com" + destination
    else:
        with pytest.raises(ValueError):
            audit.locator_destination(payload, base)


@pytest.mark.parametrize("change", ["missing_receipt", "missing_attempt", "unresolved_attempt"])
def test_incomplete_attempt_accounting_fails_closed(tmp_path, change):
    directory = tmp_path / "cache"
    directory.mkdir()
    keys = {"reference-2006", "primary-doi", "primary-publisher", "primary-locator", "primary-jbc"}
    for key in keys:
        for suffix in ("receipt", "attempt"):
            (directory / f"{key}-{suffix}.json").touch()
    if change == "unresolved_attempt":
        (directory / "unreported-attempt.json").touch()
    else:
        (directory / f"primary-jbc-{change.removeprefix('missing_')}.json").unlink()
    with pytest.raises(ValueError, match="research request coverage"):
        audit.build(tmp_path, Path("cache"))


def test_public_checkpoint_keeps_primary_access_and_subject_identity_unresolved():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["corpus_records_hash_checked_at_preflight"] == 2939
    assert len(result["records"]) == 3
    assert result["primary_access"]["terminal_status"] == 403
    assert result["primary_access"]["disposition"] == "ACCESS_HOLD"
    assert result["primary_access"]["locator_http_200_is_primary_text"] is False
    assert result["primary_access"]["primary_results_reviewed"] is False
    assert result["reference_context"]["name_resolution"]["experimental_strain_or_genome_resolved"] is False
    assert result["curation_decision"] == "NO_NEW_RESISTANCE_ASSERTION_OR_EXPERIMENTAL_IDENTIFIER"
    assert result["limits"]["scientific_http_attempts"] == 5
    assert result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"
    assert "?" not in result["sources"]["primary-locator"]["url"]
    assert "referencePositions" not in json.dumps(result)


@pytest.mark.parametrize("change", ["none", "manual_flag", "binding"])
def test_cache_replay_is_offline_and_requires_manual_html_review(monkeypatch, change):
    if not (ROOT / audit.CACHE / "primary-jbc-receipt.json").exists():
        pytest.skip("private source cache is not distributed")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    original_open, original_loads = Path.open, json.loads

    def guarded(path, *args, **kwargs):
        assert not path.resolve().is_relative_to(ROOT / "data/antibiotics")
        return original_open(path, *args, **kwargs)

    def altered_loads(*args, **kwargs):
        value = original_loads(*args, **kwargs)
        if isinstance(value, dict) and "html_redirect_source" in value:
            if change == "manual_flag":
                value["manual_redirect_reviewed"] = False
            elif change == "binding":
                value["html_redirect_source"]["body"]["sha256"] = "0" * 64
        return value

    monkeypatch.setattr(Path, "open", guarded)
    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(json, "loads", altered_loads)
    if change == "none":
        assert audit.build(ROOT) == original_loads((ROOT / audit.OUTPUT).read_bytes())
    else:
        with pytest.raises(ValueError, match="manual HTML redirect provenance"):
            audit.build(ROOT)
