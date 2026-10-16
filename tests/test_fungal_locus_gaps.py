"""References, species-specific experiments and inaccessible sources stay distinct."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests
from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_fungal_locus_gaps as audit  # noqa: E402


def fixture(key):
    accession, locus, field, taxon, species, name, version = audit.REFERENCES[key]
    entry = {
        "primaryAccession": accession,
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": version, "sequenceVersion": 1},
        "genes": [{field: [{"value": locus}]}],
        "organism": {"taxonId": taxon, "scientificName": name + " reference"},
    }
    taxonomy = {
        "taxonId": taxon,
        "scientificName": name + " reference",
        "active": True,
        "rank": "strain",
        "lineage": [{"taxonId": species, "scientificName": name, "rank": "species"}],
    }
    return entry, taxonomy


@pytest.mark.parametrize("key", ["wm276", "h99-candidate"])
@pytest.mark.parametrize(
    "change",
    [
        "none",
        "accession",
        "reviewed",
        "sequence",
        "features",
        "locus",
        "locus_field",
        "extra_gene",
        "symbol",
        "reference_taxon",
        "taxonomic_rank",
        "inactive",
        "species_id",
        "species_name",
        "lineage",
        "version",
        "sequence_version",
        "bool_version",
    ],
)
def test_species_and_locus_projection(key, change):
    entry, taxonomy = fixture(key)
    field = audit.REFERENCES[key][2]
    if change == "accession":
        entry["primaryAccession"] = "wrong"
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif change in {"sequence", "features"}:
        entry[change] = "outside metadata scope"
    elif change == "locus":
        entry["genes"][0][field][0]["value"] += "_different"
    elif change == "locus_field":
        other = "orfNames" if field == "orderedLocusNames" else "orderedLocusNames"
        entry["genes"][0][other] = entry["genes"][0].pop(field)
    elif change == "extra_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change == "symbol":
        entry["genes"][0]["geneName"] = {"value": "URA6"}
    elif change == "reference_taxon":
        entry["organism"]["taxonId"] += 1
    elif change == "taxonomic_rank":
        taxonomy["rank"] = "species"
    elif change == "inactive":
        taxonomy["active"] = False
    elif change == "species_id":
        taxonomy["lineage"][0]["taxonId"] = 5207 if key == "wm276" else 37769
    elif change == "species_name":
        taxonomy["lineage"][0]["scientificName"] = "A different species"
    elif change == "lineage":
        taxonomy["lineage"] *= 2
    elif change == "version":
        entry["entryAudit"]["entryVersion"] += 1
    elif change == "sequence_version":
        entry["entryAudit"]["sequenceVersion"] = 2
    elif change == "bool_version":
        entry["entryAudit"]["sequenceVersion"] = True
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_reference(entry, taxonomy, key)
        return
    result = audit.project_reference(entry, taxonomy, key)
    assert result["species_matches_card_term"] == (key == "h99-candidate")
    assert result["primary_native_gene_alias_verified"] == (key == "wm276")
    assert not result["paper_resistance_context_matches_card_species"]
    assert not result["resistance_assertion_supported_by_identity_alone"]
    assert result["experimental_allele_assignment"] is result["experimental_genome_assignment"] is None


@pytest.mark.parametrize(
    "change",
    ["one_cell", "empty_cells", "colspan", "missing_group", "duplicate", "wrong_gene", "wrong_table"],
)
def test_native_table_group_scope(change):
    headings = {
        "one_cell": "<td>WM276 derived strains</td>",
        "empty_cells": "<td>WM276 derived strains</td><td/><td/>",
        "colspan": '<td colspan="2">WM276 derived strains</td><td/>',
    }
    heading = "<tr>" + headings.get(change, headings["one_cell"]) + "</tr>"
    if change == "missing_group":
        heading = ""
    gene = "URA60" if change == "wrong_gene" else "URA6"
    row = "<tr><td>study-local subject</td><td>" + gene + "</td><td>not exported</td></tr>"
    if change == "duplicate":
        row *= 2
    identifier = "other" if change == "wrong_table" else "Tab2"
    tree = etree.fromstring(
        (
            f'<article><table-wrap id="{identifier}"><table><tbody>'
            + heading
            + row
            + "</tbody></table></table-wrap></article>"
        ).encode()
    )
    if change not in {"one_cell", "empty_cells", "colspan"}:
        with pytest.raises(ValueError):
            audit.gene_table_group(tree, "Tab2", "URA6")
        return
    result = audit.gene_table_group(tree, "Tab2", "URA6")
    assert result["group"] == "WM276 derived strains"
    assert result["row_index_zero_based"] == 1
    assert "not exported" not in json.dumps(result)


@pytest.mark.parametrize("change", ["none", "doi", "pmid", "license"])
def test_primary_identity_scope(change):
    doi = "wrong" if change == "doi" else "10.1038/test"
    pmid = "wrong" if change == "pmid" else "1234"
    license_url = "missing" if change == "license" else "https://creativecommons.org/licenses/by/4.0/"
    payload = (
        f'<article><front><article-meta><article-id pub-id-type="doi">{doi}</article-id>'
        f'<article-id pub-id-type="pmid">{pmid}</article-id><permissions>{license_url}</permissions>'
        "</article-meta></front><body/></article>"
    ).encode()
    if change != "none":
        with pytest.raises(ValueError):
            audit.parse_primary(payload, "10.1038/test", "1234")
        return
    assert audit.parse_primary(payload, "10.1038/test", "1234").tag == "article"


def test_saved_findings_do_not_promote_species_or_held_sources():
    dossier = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert dossier["ura6_table_scope"]["group"] == "WM276 derived strains"
    assert dossier["ura6_references"]["wm276"]["species_taxon_id"] == "NCBITaxon:37769"
    assert dossier["ura6_references"]["h99-candidate"]["species_taxon_id"] == "NCBITaxon:5207"
    assert dossier["held_sources"]["fks1-primary"]["status"] == 500
    assert dossier["held_sources"]["h99-model-paper"]["status"] == 301
    assert not dossier["term_assessments"]["ARO:3009633"]["card_species_assertion_replaced"]
    assert not dossier["term_assessments"]["ARO:3009633"]["h99_gene_alias_native_primary_verified"]
    assert not dossier["term_assessments"]["ARO:3009287"]["primary_read"]
    assert not dossier["cyp51_reference_accession"]["uniprot_match_found"]
    assert all(dossier["queries"][k]["result_count"] == 0 for k in ("cyp51-reference", "cyp51-alias"))
    assert (
        dossier["summary"]["biological_records_changed"]
        == dossier["summary"]["whole_record_reviews_completed"]
        == 0
    )
    assert dossier["constraints"]["ncbi_requests"] == 0
    assert not dossier["constraints"]["cross_species_phenotype_transfer"]
    assert not dossier["constraints"]["numeric_ast_exported"]
    assert not dossier["constraints"]["sequences_variants_protocols_exported"]
    assert dossier["goal_status"] == "OPEN"


def test_offline_replay(monkeypatch, pre_card_qualification_root):
    if not (ROOT / audit.CACHE / "selection.json").exists():
        pytest.skip("private source cache is not committed")

    def denied(*args, **kwargs):
        raise AssertionError("network forbidden during offline replay")

    monkeypatch.setattr(socket, "socket", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    root = pre_card_qualification_root
    value = audit.build(root, root / audit.CACHE)
    assert (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode() == (
        ROOT / audit.OUTPUT
    ).read_bytes()
