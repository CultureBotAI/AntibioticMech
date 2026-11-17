"""Keep missing measurements, reference identities and experimental scopes separate."""

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
import audit_vgb_evidence as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture
def primary():
    return etree.fromstring(b"""<article><front><article-meta>
      <article-id pub-id-type="pmid">27929110</article-id>
      <article-id pub-id-type="doi">10.1038/ncomms13803</article-id>
      </article-meta></front><body><sec id="sec2"><p>Fixture (Vgb) context.</p></sec>
      <sec id="sec27"><p>WGS project JFOM00000000.</p></sec>
      <table-wrap id="t1"><table><tbody><tr>
      <td>Streptogramin B lyase</td><td>vgbC</td><td>Streptogramin B</td><td>Linopristin</td>
      <td>&#160;</td><td>NA<xref rid="t1-fn2"><sup>*</sup></xref></td>
      </tr></tbody></table><table-wrap-foot><fn id="t1-fn2">
      <p>*The E. coli MIC for linopristin is &gt;128 &#956;g ml&#8722;1,
      the highest soluble concentration.</p>
      </fn></table-wrap-foot></table-wrap></body></article>""")


def project(tree):
    return audit.project_primary(etree.tostring(tree))


def test_blank_and_na_keep_column_positions(primary):
    result = project(primary)
    assert result["determinant_mic_cell"] == ""
    assert result["control_mic_cell"] == "NA*"
    assert result["control_footnote_scope"] == "SOLUBILITY_LIMIT_NOT_A_VGBC_EFFECT_SIZE"
    assert result["experimental_genome_assignment"] is None
    for key in (
        "blank_or_na_imputed",
        "quantitative_vgbc_mic_effect_established",
        "native_isolate_contribution_established",
        "broad_results_statement_overrides_table",
        "wgs_project_is_versioned_assembly",
        "determinant_accession_selected_from_range",
    ):
        assert result[key] is False


@pytest.mark.parametrize(
    "position,value",
    [(1, "other"), (2, "vgbA"), (3, "other"), (4, "Quinupristin"), (5, "0"), (5, "NA*"), (6, "")],
)
def test_table_drift_requires_review(primary, position, value):
    cell = primary.xpath("//tr/td")[position - 1]
    cell.clear()
    cell.text = value
    with pytest.raises(ValueError):
        project(primary)


@pytest.mark.parametrize("kind", ["table", "row", "footnote", "paragraph", "availability"])
def test_ambiguous_primary_locations_rejected(primary, kind):
    node = primary.xpath(
        {
            "table": "//table-wrap",
            "row": "//tr",
            "footnote": "//fn",
            "paragraph": '//sec[@id="sec2"]/p',
            "availability": '//sec[@id="sec27"]/p',
        }[kind]
    )[0]
    node.getparent().append(copy.deepcopy(node))
    with pytest.raises(ValueError):
        project(primary)


@pytest.mark.parametrize("kind", ["pmid", "doi", "footnote", "footnote_link", "genome"])
def test_primary_identity_and_footnote_binding(primary, kind):
    if kind in {"pmid", "doi"}:
        primary.xpath(f'//article-id[@pub-id-type="{kind}"]')[0].text = "other"
    elif kind == "footnote_link":
        primary.xpath("//xref")[0].set("rid", "other")
    else:
        primary.xpath("//fn/p" if kind == "footnote" else '//sec[@id="sec27"]/p')[0].text = "other"
    with pytest.raises(ValueError):
        project(primary)


@pytest.fixture
def taxon():
    parent = {"taxonId": 185978, "scientificName": "unclassified Paenibacillus", "rank": "no rank"}
    return {
        "taxonId": 1120679,
        "scientificName": "Paenibacillus sp. (strain LC231)",
        "rank": "species",
        "active": True,
        "lineage": [parent],
        "parent": {k: v for k, v in parent.items() if k != "rank"},
    }


def test_strain_label_does_not_override_native_species_rank(taxon):
    result = audit.project_taxon(taxon, 1120679, "Paenibacillus sp. (strain LC231)")
    assert result["native_rank"] == "species"
    assert result["strain_label_in_name_changes_rank"] is False
    assert result["experimental_subject_assignment"] is False


@pytest.mark.parametrize(
    "key,value",
    [("rank", "strain"), ("taxonId", 29382), ("scientificName", "Staphylococcus aureus"), ("active", False)],
)
def test_taxon_identity_and_status(taxon, key, value):
    taxon[key] = value
    with pytest.raises(ValueError):
        audit.project_taxon(taxon, 1120679, "Paenibacillus sp. (strain LC231)")


def test_taxonomy_lineage_not_silently_repaired(taxon):
    taxon["lineage"].append(dict(taxon["lineage"][0]))
    with pytest.raises(ValueError):
        audit.project_taxon(taxon, 1120679, "Paenibacillus sp. (strain LC231)")


@pytest.fixture
def metadata():
    return {
        "hitCount": 1,
        "request": {"queryString": "EXT_ID:27929110 AND SRC:MED"},
        "resultList": {"result": [{**audit.PUBLICATION, "pmid": "27929110", "source": "MED"}]},
    }


def test_metadata_identity_only(metadata):
    assert audit.project_metadata(metadata) == audit.PUBLICATION


@pytest.mark.parametrize("key,value", [("hitCount", True), ("hitCount", 2), ("nextCursorMark", "next")])
def test_metadata_completeness(metadata, key, value):
    metadata[key] = value
    with pytest.raises(ValueError):
        audit.project_metadata(metadata)


@pytest.mark.parametrize("key", ["id", "doi", "pmcid", "title", "isOpenAccess", "pmid", "source"])
def test_metadata_identity_drift(metadata, key):
    metadata["resultList"]["result"][0][key] = "other"
    with pytest.raises(ValueError):
        audit.project_metadata(metadata)


def test_reference_export_excludes_operational_and_subject_details():
    entry = {
        "primaryAccession": "P17978",
        "entryType": "reviewed",
        "entryAudit": {"entryVersion": 97, "sequenceVersion": 1},
        "genes": [{"geneName": {"value": "vgb"}}],
        "organism": {"taxonId": 1280, "scientificName": "Staphylococcus aureus"},
        "sequence": "not exported",
        "features": ["not exported"],
        "references": ["not exported"],
    }
    result = audit.project_protein(entry)
    assert result["gene_symbols"] == ["vgb"]
    assert result["experimental_allele_assignment"] is None
    assert not set(result) & {"sequence", "features", "references", "strain", "assembly"}


def test_saved_dossier_keeps_reference_primary_and_compound_scopes_separate():
    saved = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert saved["scope"] == audit.SCOPE
    assert len(saved["records"]) == 9 and len(saved["claims"]) == 27
    assert {c["aro_id"] for c in saved["claims"]} == set(audit.TERMS)
    assert not any(saved["disposition"].values())
    assert saved["references"]["vgbc"]["protein_accession_assigned"] is None
    assert saved["references"]["vgbb"]["primary_results_reviewed"] is False
    assert saved["references"]["vgba"]["hold_preserved_no_retry_or_alternate"] is True
    assert saved["metadata"]["repeat_lookup_acknowledged"] is True
    assert saved["constraints"]["ncbi_requests"] == saved["constraints"]["github_mutations"] == 0
    assert saved["constraints"]["issue_1040"] == "DEFERRED"
    assert saved["constraints"]["full_corpus_goal_status"] == "OPEN"
