"""Mixtures, salts and reference taxa must not become exact resistant subjects."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_streptothricin_context as audit  # noqa: E402


@pytest.fixture
def reference_input():
    entry = {
        "primaryAccession": "P37506",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 136, "sequenceVersion": 1},
        "organism": {"taxonId": 224308, "scientificName": "Bacillus subtilis (strain 168)"},
        "genes": [
            {
                "geneName": {"value": "satA"},
                "synonyms": [{"value": "yyaR"}],
                "orderedLocusNames": [{"value": "BSU40740"}],
            }
        ],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference enzyme"}}},
        "references": [
            {
                "citation": {
                    "citationCrossReferences": [
                        {"database": "PubMed", "id": "28842538"},
                        {"database": "DOI", "id": "10.1128/aem.01590-17"},
                    ]
                },
                "referencePositions": ["NOT FOR EXPORT"],
            }
        ],
    }
    taxonomy = {
        "taxonId": 224308,
        "scientificName": "Bacillus subtilis (strain 168)",
        "active": True,
        "rank": "strain",
        "lineage": [{"taxonId": 1423, "rank": "species", "scientificName": "Bacillus subtilis"}],
    }
    return {"results": [entry]}, {"X-UniProt-Release": "2026_03", "X-Total-Results": "1"}, taxonomy


def test_publication_reference_remains_non_experimental(reference_input):
    result = audit.project_sata(*reference_input)
    assert result["protein_accession"] == "UniProtKB:P37506"
    assert result["reference_species_taxon_id"] == "NCBITaxon:1423"
    assert result["exact_resistance_allele"] is False
    assert result["experimental_subject_assignment"] is False
    assert result["primary_results_reviewed"] is False
    assert "NOT FOR EXPORT" not in json.dumps(result)


@pytest.mark.parametrize(
    "change",
    [
        "empty",
        "null",
        "nonobject",
        "duplicate",
        "partial",
        "count",
        "release",
        "accession",
        "gene",
        "alias",
        "locus",
        "reference_taxon",
        "organism_name",
        "shared_wrong_name",
        "taxon",
        "inactive",
        "rank",
        "species",
        "version",
        "sequence_version",
        "boolean_version",
        "unreviewed",
        "pmid",
        "doi",
        "sequence",
        "features",
        "comments",
    ],
)
def test_publication_reference_guards(reference_input, change):
    data, headers, tax = reference_input
    entry = data["results"][0]
    if change == "empty":
        data["results"] = []
    elif change == "null":
        data["results"] = None
    elif change == "nonobject":
        data["results"] = [None]
    elif change == "duplicate":
        data["results"].append(copy.deepcopy(entry))
        headers["X-Total-Results"] = "2"
    elif change == "partial":
        headers["Link"] = "next"
    elif change == "count":
        headers["X-Total-Results"] = "2"
    elif change == "release":
        headers["X-UniProt-Release"] = "OTHER"
    elif change == "accession":
        entry["primaryAccession"] = "B7JE95"
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "different"
    elif change == "alias":
        entry["genes"][0]["synonyms"] = []
    elif change == "locus":
        entry["genes"][0]["orderedLocusNames"][0]["value"] = "OTHER"
    elif change == "reference_taxon":
        entry["organism"]["taxonId"] = 405535
    elif change in {"organism_name", "shared_wrong_name"}:
        entry["organism"]["scientificName"] = "OTHER"
        if change == "shared_wrong_name":
            tax["scientificName"] = "OTHER"
    elif change == "taxon":
        tax["taxonId"] = 405535
    elif change == "inactive":
        tax["active"] = False
    elif change == "rank":
        tax["rank"] = "no rank"
    elif change == "species":
        tax["lineage"][0]["taxonId"] = 1396
    elif change == "version":
        entry["entryAudit"]["entryVersion"] += 1
    elif change == "sequence_version":
        entry["entryAudit"]["sequenceVersion"] += 1
    elif change == "boolean_version":
        entry["entryAudit"]["entryVersion"] = True
    elif change == "unreviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change in {"pmid", "doi"}:
        entry["references"][0]["citation"]["citationCrossReferences"][0 if change == "pmid" else 1]["id"] = (
            "OTHER"
        )
    else:
        entry[change] = []
    with pytest.raises(ValueError):
        audit.project_sata(data, headers, tax)


def test_article_changed_bytes_cannot_reuse_manual_review():
    with pytest.raises(ValueError, match="reviewed primary article"):
        audit.primary_context(b"<article>Different source</article>")


def test_public_checkpoint_preserves_all_scope_boundaries():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert {r["identifier"] for r in result["records"]} == set(audit.RECORDS)
    assert result["corpus_records_hash_checked_at_preflight"] == 2939
    assert result["reference_interpretation"] == {
        "same_reference_species": False,
        "interchangeable_accessions": False,
        "source_term_candidate_replaced": False,
        "source_assertion_proven_false": False,
    }
    assert result["prior_card_reference"]["accession"] == "UniProtKB:B7JE95"
    assert result["publication_reference"]["protein_accession"] == "UniProtKB:P37506"
    for form in result["chemical_forms"].values():
        assert form["reported_material"] == "SULFATE_HYDRATE"
        assert form["exact_match_to_neutral_record"] is False
        assert form["exact_match_to_bare_trication_record"] is False
        assert form["active_moiety_equivalence_used_for_curation"] is False
        assert form["pages_visually_reviewed"] == 1
    assert result["primary_2017_hold"]["primary_results_reviewed"] is False
    assert result["primary_2017_hold"]["status"] == 403
    assert result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["new_experimental_identifiers"] == 0
    assert result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"
    assert result["primary_2023"]["rna_scope"]["protein_accession_applicable_to_rna"] is False
    assert "X-Goog-Signature" not in json.dumps(result)


@pytest.mark.parametrize("change", ["none", "destination", "binding", "automatic", "pdf", "page"])
def test_chemical_pdf_redirect_and_visual_review_are_pinned(tmp_path, monkeypatch, change):
    expected = audit.SUPPLEMENTS["chemical-f"]
    public_url = f"https://journals.plos.org/plosbiology/article/file?id={audit.DOI}.s014&type=supplementary"
    destination = (
        f"https://storage.googleapis.com/plos-corpus-prod/{audit.DOI}/1/pbio.3002091.s014.pdf?test=1"
    )
    if change == "destination":
        destination = destination.replace("s014.pdf", "s015.pdf")
    directory = tmp_path / "cache"
    directory.mkdir()
    payload = b"%PDF synthetic"
    page = b"synthetic reviewed page"
    monkeypatch.setitem(expected, "sha256", hashlib.sha256(payload).hexdigest())
    monkeypatch.setitem(expected, "page_sha256", hashlib.sha256(page).hexdigest())

    def request(key, url, body, status, plan, headers):
        path = directory / plan
        config = {"requests": {key: {"url": url}}}
        if key.endswith("-pdf"):
            config.update(
                {
                    "manual_redirect_reviewed": True,
                    "redirect_receipt": audit.reference.pin(tmp_path, directory / "chemical-f-receipt.json"),
                }
            )
            if change == "binding":
                config["redirect_receipt"]["sha256"] = "0" * 64
        path.write_text(json.dumps(config))
        (directory / (key + "-attempt.json")).write_text(
            json.dumps({"url": url, "plan_sha256": audit.reference.digest(path), "retry_performed": False})
        )
        (directory / (key + "-response.bin")).write_bytes(body)
        (directory / (key + "-receipt.json")).write_text(
            json.dumps(
                {
                    "url": url,
                    "status": status,
                    "headers": headers,
                    "bytes": len(body),
                    "sha256": hashlib.sha256(body).hexdigest(),
                    "retry_performed": False,
                    "redirects_followed": change == "automatic",
                    "retrieved_at": "2026-10-14T00:00:00Z",
                }
            )
        )

    request("chemical-f", public_url, b"", 302, "chemical-supplements-plan.json", {"Location": destination})
    request(
        "chemical-f-pdf",
        destination,
        payload if change != "pdf" else b"other",
        200,
        "chemical-f-redirect-plan.json",
        {},
    )
    (directory / "chemical-f-page-1.png").write_bytes(page if change != "page" else b"other")
    if change == "none":
        result = audit.chemical_source(tmp_path, directory, "chemical-f")
        assert result["reported_material"] == "SULFATE_HYDRATE"
        assert "url" not in result["pdf"]
    else:
        with pytest.raises(ValueError):
            audit.chemical_source(tmp_path, directory, "chemical-f")


@pytest.mark.parametrize("change", ["missing_receipt", "missing_attempt", "unresolved_attempt"])
def test_missing_or_unreported_attempts_fail_closed(tmp_path, change):
    keys = {
        "primary-2023",
        "primary-2017",
        "references-2017",
        "chemical-f",
        "chemical-f-pdf",
        "chemical-d",
        "chemical-d-pdf",
    }
    for key in keys:
        for suffix in ("-receipt.json", "-attempt.json"):
            (tmp_path / (key + suffix)).write_text("{}")
    if change == "missing_receipt":
        (tmp_path / "chemical-f-receipt.json").unlink()
    elif change == "missing_attempt":
        (tmp_path / "chemical-f-attempt.json").unlink()
    else:
        (tmp_path / "unexpected-attempt.json").write_text("{}")
    with pytest.raises(ValueError, match="research request coverage"):
        audit.build(tmp_path, Path("."))


def test_cache_replay_is_offline_and_uses_historical_records(monkeypatch):
    if not (ROOT / audit.CACHE / "chemical-d-pdf-response.bin").exists():
        pytest.skip("private source cache is not distributed")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.resolve().is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    assert audit.build(ROOT) == json.loads((ROOT / audit.OUTPUT).read_bytes())
