"""Guard congener, subject, reference and phenotype boundaries in yeast curation."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_syringomycin_context as audit  # noqa: E402

from antibioticmech.activity_collections import load_record  # noqa: E402
from antibioticmech.curate.curation_event import record_curation_event  # noqa: E402
from antibioticmech.validation.write_validated import write_validated_antibiotic  # noqa: E402


def metadata(gene):
    accession, canonical, locus, sgd = audit.REFERENCES[gene]
    name = "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)"
    block = {"geneName": {"value": canonical}, "orderedLocusNames": [{"value": locus}]}
    if gene != canonical:
        block["synonyms"] = [{"value": gene}]
    entry = {
        "primaryAccession": accession,
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
        "genes": [block],
        "organism": {"taxonId": 559292, "scientificName": name},
        "proteinDescription": {"recommendedName": {"fullName": {"value": "TEST REFERENCE"}}},
        "uniProtKBCrossReferences": [{"database": "SGD", "id": sgd}],
    }
    taxonomy = {
        "taxonId": 559292,
        "scientificName": name,
        "rank": "strain",
        "active": True,
        "lineage": [{"taxonId": 4932, "scientificName": "Saccharomyces cerevisiae", "rank": "species"}],
    }
    return entry, taxonomy


@pytest.mark.parametrize("gene", list(audit.REFERENCES))
@pytest.mark.parametrize(
    "change",
    [
        "none",
        "accession",
        "locus",
        "canonical",
        "sgd",
        "taxon",
        "version",
        "sequence",
        "features",
        "comments",
    ],
)
def test_reference_identity_is_not_an_experimental_assignment(gene, change):
    entry, taxonomy = metadata(gene)
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "locus":
        entry["genes"][0]["orderedLocusNames"][0]["value"] = "OTHER"
    elif change == "canonical":
        entry["genes"][0]["geneName"]["value"] = "OTHER"
    elif change == "sgd":
        entry["uniProtKBCrossReferences"][0]["id"] = "OTHER"
    elif change == "taxon":
        entry["organism"]["taxonId"] = 4932
    elif change == "version":
        entry["entryAudit"]["entryVersion"] = True
    elif change in {"sequence", "features", "comments"}:
        entry[change] = "NOT_EXPORTED"
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_protein(entry, gene, taxonomy)
        return
    result = audit.project_protein(entry, gene, taxonomy)
    assert result["experimental_subject_assignment"] is False
    assert result["exact_resistance_allele"] is False
    assert result["source_species_taxon_id"] == "NCBITaxon:4932"
    assert result["reference_taxon_id"] == "NCBITaxon:559292"


@pytest.mark.parametrize("gene", ["SYR2", "FAH1"])
def test_source_alias_is_required(gene):
    entry, taxonomy = metadata(gene)
    entry["genes"][0].pop("synonyms")
    with pytest.raises(ValueError, match="gene name"):
        audit.project_protein(entry, gene, taxonomy)


def context():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_source_scope_and_skn1_hold():
    data = context()
    assert len(data["candidate_accounting"]) == 12
    assert data["sources"]["primary-2000"]["status"] == 500
    rows = {r["source_gene"]: r for r in data["primary"]["source_rows"]}
    assert len(rows) == 7
    assert {gene for gene, row in rows.items() if row["curation_supported"]} == set(audit.BACKGROUND)
    assert rows["SKN1"]["parental_background"] is None
    assert rows["SKN1"]["figure_1B_present"] is False
    assert rows["SKN1"]["methods_resistance_label_present"] is False
    assert rows["IPT1"]["parental_background"] == "W303C"
    assert rows["ELO2"]["parental_background"] == "W303C"
    assert rows["FAH1"]["parental_background"] == "BY4741"
    assert rows["ERG3"]["parental_background"] == "8A-1B"
    assert data["summary"]["skn1_reference_does_not_authorize_curation"] is True
    assert len(data["references"]) == 4
    assert data["references"]["SYR2"]["canonical_gene"] == "SUR2"
    assert data["references"]["FAH1"]["canonical_gene"] == "SCS7"


def test_qualitative_claims_have_no_experimental_id_promotion_or_numeric_ast():
    claims = audit.claims(context())
    assert len(claims) == 6
    assert {r["gene_families"][0] for r in claims} == set(audit.BACKGROUND)
    assert {r["mechanism_type"] for r in claims} == {"UNKNOWN"}
    for row in claims:
        gene = row["gene_families"][0]
        assert row["taxon_id"] == "NCBITaxon:4932"
        assert audit.BACKGROUND[gene] + "-derived" in row["note"]
        assert row["evidence"][0]["reference"] == "PMID:22046175"
        assert "Figure 1B SRE" in row["evidence"][0]["notes"]
        assert not set(row).intersection(
            {"protein_accession", "gene_id", "strain", "strain_taxon_id", "alteration", "mic"}
        )
        refs = [e for e in row["evidence"] if e["reference"].startswith("UniProtKB:")]
        assert len(refs) == (1 if gene in {"SYR2", "IPT1", "FAH1"} else 0)
        if refs:
            assert "Reference identity only" in refs[0]["notes"]


@pytest.mark.parametrize("change", [
    "empty", "primary", "record", "source", "duplicate", "missing_row", "unsupported",
    "background", "figure", "methods", "reference", "experimental_assignment",
])
def test_claims_require_the_reviewed_context(change):
    data = context()
    if change == "empty":
        data = {"references": {}}
    elif change == "primary":
        del data["primary"]
    elif change == "record":
        data["record_before"]["identifier"] = "OTHER"
    elif change == "source":
        data["sources"]["primary-2011"]["body"]["sha256"] = "0" * 64
    elif change == "duplicate":
        data["primary"]["source_rows"].append(copy.deepcopy(data["primary"]["source_rows"][0]))
    elif change == "missing_row":
        data["primary"]["source_rows"].pop()
    elif change in {"unsupported", "background", "figure", "methods"}:
        key, value = {
            "unsupported": ("curation_supported", False),
            "background": ("parental_background", "OTHER"),
            "figure": ("figure_1B_present", False),
            "methods": ("methods_resistance_label_present", False),
        }[change]
        data["primary"]["source_rows"][0][key] = value
    elif change == "reference":
        data["references"]["SYR2"]["protein_accession"] = "UniProtKB:OTHER"
    else:
        data["references"]["SYR2"]["experimental_subject_assignment"] = True
    with pytest.raises(ValueError, match="complete reviewed"):
        audit.claims(data)


def test_saved_curation_preserves_source_record_and_history(tmp_path):
    receipt = json.loads((ROOT / "research/2026-10-13-syringomycin-curation.json").read_bytes())
    before = load_record(ROOT / audit.FIXTURE)
    after = copy.deepcopy(before)
    record_curation_event(after, **receipt["curation_event"])
    after["resistance_mechanisms"] = audit.claims(context())
    target = tmp_path / "syringomycin-e.yaml"
    write_validated_antibiotic(after, target)
    assert audit.reference.digest(target) == receipt["record"]["sha256"]
    assert audit.reference.digest(ROOT / audit.FIXTURE) == audit.RECORD_SHA
    assert after["resistance_mechanisms"] == receipt["claims"] == audit.claims(context())
    assert after["curation_history"][:-1] == before["curation_history"]
    restored = copy.deepcopy(after)
    restored.pop("resistance_mechanisms")
    restored["curation_history"] = restored["curation_history"][:-1]
    assert restored == before


@pytest.mark.skipif(not (ROOT / audit.CACHE).exists(), reason="native source cache is local-only")
def test_cached_source_projection_stays_offline(monkeypatch):
    def deny(*args, **kwargs):
        raise AssertionError("offline projection must not request the network")

    monkeypatch.setattr(socket, "socket", deny)
    monkeypatch.setattr(requests.sessions.Session, "request", deny)
    data = context()
    payload = audit.reference.check_pin(ROOT, data["sources"]["primary-2011"]["body"]).read_bytes()
    assert audit.primary_context(payload) == data["primary"]
    taxonomy = json.loads(audit.reference.check_pin(ROOT, data["taxonomy"]["body"]).read_bytes())
    for key, genes in (("syr2-reference", ["SYR2"]), ("other-references", ["IPT1", "FAH1", "SKN1"])):
        entries = json.loads(audit.reference.check_pin(ROOT, data["sources"][key]["body"]).read_bytes())[
            "results"
        ]
        for gene in genes:
            (entry,) = [e for e in entries if e["primaryAccession"] == audit.REFERENCES[gene][0]]
            assert audit.project_protein(entry, gene, taxonomy) == data["references"][gene]
