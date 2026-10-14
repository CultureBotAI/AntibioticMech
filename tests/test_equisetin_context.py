"""Chemical modulation, producer loci and assay subjects must stay distinct."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests
from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_equisetin_context as audit  # noqa: E402


@pytest.fixture
def article():
    root = etree.Element("article", {"article-type": "research-article"})
    meta = etree.SubElement(etree.SubElement(root, "front"), "article-meta")
    for kind, identifier in (("pmid", "34869220"), ("pmcid", "PMC8632820"), ("doi", audit.DOI)):
        etree.SubElement(meta, "article-id", {"pub-id-type": kind}).text = identifier
    body = etree.SubElement(root, "body")
    etree.SubElement(body, "sec")
    methods = etree.SubElement(body, "sec")
    for _ in range(8):
        etree.SubElement(etree.SubElement(methods, "sec"), "p")
    results = etree.SubElement(body, "sec")
    for count in (1, 2, 8):
        section = etree.SubElement(results, "sec")
        for _ in range(count):
            etree.SubElement(section, "p")
    for _ in range(2):
        etree.SubElement(etree.SubElement(etree.SubElement(section, "fig"), "caption"), "p")
    for xpath, marker in audit.LOCATIONS.values():
        (node,) = root.xpath(xpath)
        node.text = "Synthetic fixture: " + marker
    return root


def project_article(root, monkeypatch):
    payload = etree.tostring(root)
    monkeypatch.setattr(audit, "ARTICLE_SHA", hashlib.sha256(payload).hexdigest())
    return audit.primary_context(payload)


def test_primary_scope_does_not_turn_modulation_into_genetic_resistance(article, monkeypatch):
    result = project_article(article, monkeypatch)
    assert len(result["locations"]) == 12
    assert result["observations"]["antibacterial_activity_reported"] is True
    assert result["observations"]["vitamin_C_reduces_antibacterial_effect"] is True
    assert result["observations"]["modulation_is_resistant_genotype_evidence"] is False
    assert result["observations"]["zone_converted_to_MIC"] is False
    assert result["observations"]["source_MIC_units"] == "ug/mL"
    assert result["observations"]["standard_MIC_unit_if_curated"] == "mg/L"
    assert result["gene_scope"]["producer_gene_cluster_compound"] == "xanthobaccin A"
    assert result["gene_scope"]["producer_locus_is_assay_subject_resistance_gene"] is False
    assert result["gene_scope"]["comparative_gene_cluster_accessions_are_assay_genomes"] is False
    assert (
        result["gene_scope"]["HSAF_oxidative_stress_and_transcriptomic_results_transferred_to_equisetin"]
        is False
    )
    assert result["gene_scope"]["uniprot_assignment"] is None
    assert result["gene_scope"]["no_resistance_gene_exists_inferred"] is False
    assert result["figures_visually_reviewed"] is False
    assert result["supplements_reviewed"] is False
    assert "Synthetic fixture" not in json.dumps(result)


def test_changed_article_cannot_reuse_manual_review():
    with pytest.raises(ValueError, match="reviewed primary article changed"):
        audit.primary_context(b"<article>Different source</article>")


@pytest.mark.parametrize("change", ["pmid", "pmcid", "doi", "article_type", "missing", "duplicate", "marker"])
def test_primary_identity_and_reviewed_location_guards(article, monkeypatch, change):
    if change in {"pmid", "pmcid", "doi"}:
        article.xpath(f'./front/article-meta/article-id[@pub-id-type="{change}"]')[0].text = "OTHER"
    elif change == "article_type":
        article.set("article-type", "review-article")
    else:
        node = article.xpath(audit.LOCATIONS["producer_locus"][0])[0]
        if change == "missing":
            node.getparent().remove(node)
        elif change == "duplicate":
            node.getparent().append(copy.deepcopy(node))
        else:
            node.text = "OTHER"
    with pytest.raises(ValueError):
        project_article(article, monkeypatch)


@pytest.mark.parametrize("change", ["none", "id", "string_id", "rank", "name", "active"])
def test_assay_taxonomy_is_species_only(change):
    taxon = {"taxonId": 1423, "scientificName": "Bacillus subtilis", "rank": "species", "active": True}
    if change in {"id", "string_id"}:
        taxon["taxonId"] = 224308 if change == "id" else "1423"
    elif change == "rank":
        taxon["rank"] = "strain"
    elif change == "name":
        taxon["scientificName"] = "OTHER"
    elif change == "active":
        taxon["active"] = False
    if change == "none":
        result = audit.ground_assay_species(taxon)
        assert result["source_strain_label"] == "ATCC 6051"
        assert result["taxon_id"] == "NCBITaxon:1423"
        assert result["strain_taxon_id"] is None
        assert result["assembly_accession"] is None
        assert result["reference_strain_168_or_its_protein_identifiers_assigned"] is False
        assert result["species_wide_resistance_inferred"] is False
    else:
        with pytest.raises(ValueError, match="identity"):
            audit.ground_assay_species(taxon)


@pytest.fixture
def discovery():
    entries = []
    for key in sorted(audit.LEADS):
        source, identifier = key.split(":", 1)
        row = {"source": source, "id": identifier, "title": "Synthetic title"}
        if key == "MED:34869220":
            row.update({"doi": audit.DOI, "pmcid": "PMC8632820"})
        entries.append(row)
    query = {"candidates": entries, "hit_count": 8, "next_cursor": None, "request": {"status": 200}}
    return {
        "identifier": "CHEBI:142135",
        "candidate_ids": sorted(audit.LEADS),
        "queries": [query, copy.deepcopy(query)],
    }


def test_unreviewed_and_duplicate_title_leads_remain_unresolved(discovery):
    result = audit.project_discovery(discovery)
    assert result["candidate_count"] == 8
    assert result["remaining_candidates_unreviewed"] == 7
    assert result["scoped_primary_text_reviews"] == 1
    assert result["AGR_MED_same_title_is_not_a_verified_crosswalk_or_independent_replication"] is True
    assert result["TA_289_title_lead_is_not_assigned_to_equisetin"] is True
    assert len([r for r in result["leads"] if r["review_status"] == "UNREVIEWED"]) == 7


@pytest.mark.parametrize(
    "change",
    [
        "record",
        "member",
        "duplicate",
        "missing_query",
        "partial",
        "count",
        "failed",
        "missing_entry",
        "duplicate_entry",
        "mismatch",
        "paper",
    ],
)
def test_discovery_membership_and_completeness_guards(discovery, change):
    if change == "record":
        discovery["identifier"] = "OTHER"
    elif change == "member":
        discovery["candidate_ids"].pop()
    elif change == "duplicate":
        discovery["candidate_ids"].append(discovery["candidate_ids"][0])
    elif change == "missing_query":
        discovery["queries"].pop()
    else:
        query = discovery["queries"][0]
        if change == "partial":
            query["next_cursor"] = "next"
        elif change == "count":
            query["hit_count"] += 1
        elif change == "failed":
            query["request"]["status"] = 500
        elif change == "missing_entry":
            query["candidates"].pop()
        elif change == "duplicate_entry":
            query["candidates"][-1] = copy.deepcopy(query["candidates"][0])
        elif change == "mismatch":
            query["candidates"][0]["title"] = "OTHER"
        else:
            for query in discovery["queries"]:
                for entry in query["candidates"]:
                    if entry["id"] == "34869220":
                        entry["doi"] = "OTHER"
    with pytest.raises(ValueError):
        audit.project_discovery(discovery)


@pytest.mark.parametrize("change", ["missing_receipt", "missing_attempt", "unresolved_attempt"])
def test_request_coverage_fails_closed(tmp_path, change):
    directory = tmp_path / "cache"
    directory.mkdir()
    for suffix in ("receipt", "attempt"):
        (directory / f"article-2021-{suffix}.json").touch()
    if change == "unresolved_attempt":
        (directory / "unreported-attempt.json").touch()
    else:
        (directory / f"article-2021-{change.removeprefix('missing_')}.json").unlink()
    with pytest.raises(ValueError, match="research request coverage"):
        audit.build(tmp_path, Path("cache"))


def test_public_checkpoint_has_no_resistance_or_experimental_protein_assignment():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["corpus_records_hash_checked_at_preflight"] == 2939
    assert result["record"]["identifier"] == "CHEBI:142135"
    assert result["record"]["standard_inchi_key"] == "QNQBPPQLRODXET-HMHJLHGTSA-N"
    assert result["assay_species"]["taxon_id"] == "NCBITaxon:1423"
    assert result["primary_context"]["gene_scope"]["uniprot_assignment"] is None
    assert result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"
    assert result["primary_context"]["mechanism"]["seeded_antiviral_role_replaced"] is False


def test_cache_replay_is_offline_and_does_not_read_live_records(monkeypatch):
    if not (ROOT / audit.CACHE / "article-2021-receipt.json").exists():
        pytest.skip("private source cache is not distributed")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    original_open = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.resolve().is_relative_to(ROOT / "data/antibiotics")
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    assert audit.build(ROOT) == json.loads((ROOT / audit.OUTPUT).read_bytes())
