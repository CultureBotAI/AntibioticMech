"""Do not promote source screens or failed reference searches to exact alleles."""

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
import audit_ionophore_yeast as audit  # noqa: E402


def worksheet():
    rows = [[""] * 10 for _ in range(133)]
    rows[1][:3] = ["ORF", "standard name", "phenotype of the deletant on Val/Nig"]
    index = 2
    for category, count in audit.COUNTS.items():
        for _ in range(count):
            rows[index][:3] = [f"YAL{index:03d}W", "TEST_GENE", category]
            rows[index][5] = "Dubious ORF" if index < 17 else "annotation"
            rows[index][7] = "*" if index < 63 else ""
            index += 1
    return rows


@pytest.mark.parametrize(
    "change",
    [
        "none",
        "row_count",
        "columns",
        "header",
        "locus",
        "duplicate",
        "symbol",
        "category",
        "stability",
        "trailing",
        "dubious_count",
        "stable_count",
    ],
)
def test_source_table_boundaries(change):
    rows = worksheet()
    if change == "row_count":
        rows.pop()
    elif change == "columns":
        rows[2].pop()
    elif change == "header":
        rows[1][2] = "unspecified phenotype"
    elif change == "locus":
        rows[2][0] = "OTHER"
    elif change == "duplicate":
        rows[3][0] = rows[2][0]
    elif change == "symbol":
        rows[2][1] = ""
    elif change == "category":
        rows[2][2] = "susceptible"
    elif change == "stability":
        rows[2][7] = "?"
    elif change == "trailing":
        rows[130][0] = "YAL999W"
    elif change == "dubious_count":
        rows[2][5] = "annotation"
    elif change == "stable_count":
        rows[2][7] = ""
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_rows(rows)
        return
    result = audit.project_rows(rows)
    assert len(result) == 127
    assert sum("RESISTANT" in (r["valinomycin_label"], r["nigericin_label"]) for r in result) == 78
    assert sum("HYPERSENSITIVE" in (r["valinomycin_label"], r["nigericin_label"]) for r in result) == 49
    assert result[0]["valinomycin_label"] is None
    assert all(r["reference_status"] == "NOT_COMPLETED_QUERY_LIMIT_HOLD" for r in result)
    assert not any(r["experimental_genome_accession"] or r["experimental_allele_accession"] for r in result)


def metadata():
    name = "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)"
    entry = {
        "primaryAccession": "P32352",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 175, "sequenceVersion": 1},
        "genes": [{"geneName": {"value": "ERG2"}, "orderedLocusNames": [{"value": "YMR202W"}]}],
        "organism": {"taxonId": 559292, "scientificName": name},
        "uniProtKBCrossReferences": [{"database": "SGD", "id": "S000004815"}],
    }
    taxon = {
        "taxonId": 559292,
        "scientificName": name,
        "rank": "strain",
        "active": True,
        "lineage": [{"rank": "species", "taxonId": 4932, "scientificName": "Saccharomyces cerevisiae"}],
    }
    return entry, taxon


@pytest.mark.parametrize(
    "change",
    [
        "none",
        "accession",
        "status",
        "gene",
        "locus",
        "duplicate_gene",
        "protein_taxon",
        "taxon_id",
        "rank",
        "inactive",
        "species",
        "duplicate_species",
        "organism_name",
        "version_boolean",
        "version_zero",
        "sgd",
        "sequence",
        "features",
        "comments",
    ],
)
def test_reference_boundaries(change):
    entry, taxon = metadata()
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "status":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "ERG3"
    elif change == "locus":
        entry["genes"][0]["orderedLocusNames"][0]["value"] = "OTHER"
    elif change == "duplicate_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change == "protein_taxon":
        entry["organism"]["taxonId"] = 4932
    elif change == "taxon_id":
        taxon["taxonId"] = 4932
    elif change == "rank":
        taxon["rank"] = "species"
    elif change == "inactive":
        taxon["active"] = False
    elif change == "species":
        taxon["lineage"][0]["taxonId"] = 1
    elif change == "duplicate_species":
        taxon["lineage"].append(copy.deepcopy(taxon["lineage"][0]))
    elif change == "organism_name":
        entry["organism"]["scientificName"] = "OTHER"
    elif change == "version_boolean":
        entry["entryAudit"]["entryVersion"] = True
    elif change == "version_zero":
        entry["entryAudit"]["sequenceVersion"] = 0
    elif change == "sgd":
        entry["uniProtKBCrossReferences"][0]["id"] = "OTHER"
    elif change in {"sequence", "features", "comments"}:
        entry[change] = "NOT_EXPORTED"
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_reference(entry, taxon)
        return
    result = audit.project_reference(entry, taxon)
    assert result["reference_taxon_id"] == "NCBITaxon:559292"
    assert result["species_taxon_id"] == "NCBITaxon:4932"
    assert result["experimental_subject_assignment"] is False
    assert result["resistance_inferred_from_reference"] is False


def test_figure_keeps_discordance_and_uninterpretable_results():
    rows = [{"source_gene_label": g} for g in ("ERG2", "ERG3", "ERG6", "ERG24")]
    figure = {r["gene"]: r for r in audit.project_figure(rows)}
    assert figure["ERG28"]["EUROSCARF_library"] == "Nig resistant"
    assert set(figure["ERG28"]["reconstructed_BY_clones"].values()) == {"Val resistant"}
    assert set(figure["ERG24"]["reconstructed_BY_clones"].values()) == {"LETHAL"}
    assert set(figure["ERG5"]["reconstructed_BY_clones"].values()) == {"NOT_DONE"}
    assert (
        figure["ERG2"]["SCY325_background"] == figure["ERG3"]["SCY325_background"] == "RESPIRATION_DEFICIENT"
    )
    assert {g for g, row in figure.items() if not row["included_in_S3_Table_127"]} == {
        "ERG4",
        "ERG5",
        "ERG28",
    }


def test_public_dossier_accounting_and_payload_scope():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["summary"]["unique_source_loci_or_additional_figure_genes"] == 130
    assert result["summary"]["verified_reference_loci"] == 1
    assert result["summary"]["reference_identity_pending"] == 129
    assert result["experimental_context"]["library_background"] == "BY4741"
    assert result["experimental_context"]["strain_taxon_assignment"] is None
    assert result["experimental_context"]["reagent_catalog_or_exact_form_verified"] is False
    rows = result["source_rows"]
    assert Counter(r["source_category"] for r in rows) == audit.COUNTS
    (mapped,) = [r for r in rows if r["reference_accessions"]]
    assert (mapped["source_locus"], mapped["source_gene_label"]) == ("YMR202W", "ERG2")
    assert mapped["reference_accessions"] == ["UniProtKB:P32352"]
    assert len([r for r in rows if r["reference_status"] == "NOT_COMPLETED_QUERY_LIMIT_HOLD"]) == 126
    assert Counter(x["status"] for x in result["inputs"]["sources"].values()) == {200: 5, 302: 3, 400: 1}
    assert all(r["new_assertions_curated"] == 0 for r in result["records"])
    assert result["constraints"]["issue_1040"] == "DEFERRED"
    assert all(result["constraints"][k] == 0 for k in ("ncbi_requests", "ncbi_contact", "github_mutations"))
    public = json.dumps(result)
    assert "X-Goog" not in public
    for forbidden in ('"sequence":', '"features":', '"comments":', '"mic":', '"protocol":'):
        assert forbidden not in public


@pytest.mark.skipif(not (ROOT / audit.CACHE).exists(), reason="native source cache is local-only")
def test_cached_source_projection_is_offline(monkeypatch):
    def deny(*args, **kwargs):
        raise AssertionError("offline replay must not access the network")

    monkeypatch.setattr(socket, "socket", deny)
    monkeypatch.setattr(requests.sessions.Session, "request", deny)
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    book = json.loads(audit.reference.check_pin(ROOT, result["inputs"]["workbook"]).read_bytes())
    expected = copy.deepcopy(result["source_rows"])
    for row in expected:
        row["reference_accessions"] = []
        row["reference_status"] = "NOT_COMPLETED_QUERY_LIMIT_HOLD"
    assert audit.project_rows(book["sheets"][0]["values"]) == expected
    sources = result["inputs"]["sources"]
    metadata_path = audit.reference.check_pin(ROOT, sources["reference-canary"]["body"])
    taxon_path = audit.reference.check_pin(ROOT, result["inputs"]["taxonomy"]["taxonomy_body"])
    (entry,) = json.loads(metadata_path.read_bytes())["results"]
    assert audit.project_reference(entry, json.loads(taxon_path.read_bytes())) == result["references"][0]
