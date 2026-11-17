"""Do not collapse human donor proteins, yeast hosts, and drug-specific endpoints."""

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
import audit_valinomycin_abcb1 as audit  # noqa: E402


def donor_fixture():
    entry = {
        "primaryAccession": "P08183", "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 258, "sequenceVersion": 3},
        "organism": {"taxonId": 9606, "scientificName": "Homo sapiens"},
        "genes": [{"geneName": {"value": "ABCB1"},
                   "synonyms": [{"value": "MDR1"}, {"value": "PGY1"}]}],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference protein"}}},
        "references": [{"citation": {"citationCrossReferences": [{"database": "PubMed", "id": "1"}]},
                        "referencePositions": ["UNEXPORTED ROLE"]}],
    }
    tax = {"taxonId": 9606, "rank": "species", "scientificName": "Homo sapiens",
           "active": True, "lineage": []}
    return entry, tax


def test_donor_reference_is_not_an_experimental_allele_or_yeast_gene():
    result = audit.project_donor(*donor_fixture())
    assert result["reference_taxon_id"] == "NCBITaxon:9606"
    assert result["protein_accession"] == "UniProtKB:P08183"
    assert result["exact_resistance_allele"] is False
    assert result["experimental_subject_assignment"] is False
    assert result["study_reference_allele_equated_to_current_uniprot_sequence"] is False
    assert result["citation_absence_disproves_paper_gene_relationship"] is False
    assert "UNEXPORTED ROLE" not in json.dumps(result)


@pytest.mark.parametrize("change", ["accession", "gene", "ambiguous_gene", "organism", "organism_name",
                                    "taxon", "species_name", "rank", "inactive", "version",
                                    "boolean_version", "sequence_version", "reviewed", "citation",
                                    "sequence", "features", "comments"])
def test_donor_identity_guards(change):
    entry, tax = donor_fixture()
    if change == "accession":
        entry["primaryAccession"] = "P38934"
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "ABCB2"
    elif change == "ambiguous_gene":
        entry["genes"] *= 2
    elif change == "organism":
        entry["organism"]["taxonId"] = 4932
    elif change == "organism_name":
        entry["organism"]["scientificName"] = "Saccharomyces cerevisiae"
    elif change == "taxon":
        tax["taxonId"] = 4932
    elif change == "species_name":
        tax["scientificName"] = "Other"
    elif change == "rank":
        tax["rank"] = "strain"
    elif change == "inactive":
        tax["active"] = False
    elif change == "version":
        entry["entryAudit"]["entryVersion"] += 1
    elif change == "boolean_version":
        entry["entryAudit"]["entryVersion"] = True
    elif change == "sequence_version":
        entry["entryAudit"]["sequenceVersion"] += 1
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change == "citation":
        entry["references"][0]["citation"]["citationCrossReferences"][0]["id"] = "17352537"
    else:
        entry[change] = []
    with pytest.raises(ValueError):
        audit.project_donor(entry, tax)


@pytest.mark.parametrize("change", ["none", "strain_taxon", "inactive", "rank", "species_taxon",
                                    "species_name", "duplicate_species"])
def test_host_species_does_not_assign_reference_strain(change):
    tax = {"taxonId": 559292, "rank": "strain", "active": True,
           "lineage": [{"taxonId": 4932, "rank": "species", "scientificName": "Saccharomyces cerevisiae"}]}
    if change == "strain_taxon":
        tax["taxonId"] = 9606
    elif change == "inactive":
        tax["active"] = False
    elif change == "rank":
        tax["rank"] = "species"
    elif change == "species_taxon":
        tax["lineage"][0]["taxonId"] = 9606
    elif change == "species_name":
        tax["lineage"][0]["scientificName"] = "Homo sapiens"
    elif change == "duplicate_species":
        tax["lineage"] *= 2
    if change == "none":
        result = audit.host_species(tax)
        assert result["species_taxon_id"] == "NCBITaxon:4932"
        assert result["reference_strain_taxon_assigned_to_assay_host"] is False
        assert result["experimental_genome_assignment"] is None
    else:
        with pytest.raises(ValueError):
            audit.host_species(tax)


@pytest.mark.parametrize("change", ["none", "url", "plan", "status", "digest", "retry",
                                    "attempt_retry", "redirect"])
def test_source_plan_and_native_response_are_bound(tmp_path, change):
    url = audit.ARTICLE
    path = tmp_path / "plan.json"
    path.write_text(json.dumps({"requests": {"article": {"url": url}}}))
    attempt = {"url": url, "plan_sha256": audit.reference.digest(path), "retry_performed": False}
    body = b"test"
    receipt = {"url": url, "status": 200, "sha256": hashlib.sha256(body).hexdigest(),
               "bytes": len(body), "retrieved_at": "2026-10-14", "retry_performed": False,
               "redirects_followed": False}
    if change == "url":
        receipt["url"] = "https://example.org/"
    elif change == "plan":
        attempt["plan_sha256"] = "0" * 64
    elif change == "status":
        receipt["status"] = 403
    elif change == "digest":
        receipt["sha256"] = "0" * 64
    elif change == "retry":
        receipt["retry_performed"] = True
    elif change == "attempt_retry":
        attempt["retry_performed"] = True
    elif change == "redirect":
        receipt["redirects_followed"] = True
    (tmp_path / "article-attempt.json").write_text(json.dumps(attempt))
    (tmp_path / "article-receipt.json").write_text(json.dumps(receipt))
    (tmp_path / "article-response.bin").write_bytes(body)
    if change == "none":
        assert audit.planned_source(tmp_path, tmp_path, "article", "plan.json", url)["status"] == 200
    else:
        with pytest.raises(ValueError):
            audit.planned_source(tmp_path, tmp_path, "article", "plan.json", url)


def test_primary_scope_and_holds_in_public_checkpoint():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    p = result["primary"]
    assert p["endpoint"] == "EC30" and p["source_units"] == "micromolar"
    assert p["endpoint_is_MIC"] is p["converted_to_MIC"] is False
    assert p["supplement_tables_reviewed"] is p["per_allele_signoff"] is False
    assert p["species_wide_or_clinical_resistance_inferred"] is False
    assert p["effect_transferred_across_drugs"] is False
    assert p["actinomycin_host_transferred_to_valinomycin"] is False
    assert result["curation"]["whole_record_primary_review"] == "OPEN"
    assert result["limits"]["ncbi_requests"] == result["limits"]["biological_changes"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["donor_reference"]["reference_taxon_id"] == "NCBITaxon:9606"
    assert result["host_species_context"]["species_taxon_id"] == "NCBITaxon:4932"
    assert all("X-Goog" not in v.get("url", "") for v in result["sources"].values())


def test_changed_article_rejected():
    with pytest.raises(ValueError, match="reviewed article changed"):
        audit.primary_context(b"different article")


def test_offline_native_replay_uses_dated_baseline(monkeypatch):
    if not (ROOT / audit.CACHE / "cohort.json").exists():
        pytest.skip("optional native research cache not available")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network access")

    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(Path, "open", guarded)
    monkeypatch.chdir(ROOT)
    monkeypatch.setattr(sys, "argv", ["audit_valinomycin_abcb1.py", "--check"])
    audit.main()


def test_study_reference_is_not_assigned_even_when_gene_synonym_is_used():
    entry, tax = donor_fixture()
    reordered = copy.deepcopy(entry)
    reordered["genes"][0]["geneName"]["value"] = "MDR1"
    reordered["genes"][0]["synonyms"][0]["value"] = "ABCB1"
    assert audit.project_donor(entry, tax) == audit.project_donor(reordered, tax)


@pytest.mark.parametrize("field", ["identifier", "standard_inchi_key"])
def test_cohort_cannot_relabel_the_pinned_baseline(monkeypatch, field):
    path = ROOT / audit.CACHE / "cohort.json"
    if not path.exists():
        pytest.skip("optional native research cache not available")
    cohort = json.loads(path.read_bytes())
    cohort["record"][field] = "Different"
    original = Path.read_bytes

    def replaced(self):
        return json.dumps(cohort).encode() if self == path else original(self)

    monkeypatch.setattr(Path, "read_bytes", replaced)
    with pytest.raises(ValueError, match="cohort label differs"):
        audit.build(ROOT)
