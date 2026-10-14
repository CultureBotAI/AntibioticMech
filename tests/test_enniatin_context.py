"""Reject congener transfer, fuzzy locus mapping and experimental identity inflation."""

import copy
import hashlib
import json
import re
import socket
import sys
from pathlib import Path

import pytest
import requests
from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_enniatin_context as audit  # noqa: E402


@pytest.fixture
def article():
    root = etree.Element("article", {"article-type": "research-article"})
    meta = etree.SubElement(etree.SubElement(root, "front"), "article-meta")
    for kind, identifier in (("pmid", "42506285"), ("pmcid", "PMC13412724"), ("doi", audit.DOI)):
        etree.SubElement(meta, "article-id", {"pub-id-type": kind}).text = identifier
    for xpath, marker in audit.LOCATIONS.values():
        node = root
        for part in xpath.split("/")[2:]:
            match = re.fullmatch(r"([a-z-]+)(?:\[(\d+)\])?", part)
            assert match is not None
            tag, index = match.group(1), int(match.group(2) or "1")
            while len(node.findall(tag)) < index:
                etree.SubElement(node, tag)
            node = node.findall(tag)[index - 1]
        node.text = "Synthetic fixture: " + marker
    return root


def project_article(root, monkeypatch):
    payload = etree.tostring(root)
    monkeypatch.setattr(audit, "ARTICLE_SHA", hashlib.sha256(payload).hexdigest())
    return audit.primary_context(payload)


def test_primary_context_does_not_transfer_congeners_hosts_or_endpoints(article, monkeypatch):
    result = project_article(article, monkeypatch)
    chemical = result["chemical_context"]
    observations = result["observations"]
    assert chemical["enniatin_A1_equated_to_enniatin_A"] is False
    assert chemical["enniatin_B1_equated_to_enniatin_B"] is False
    assert chemical["yeast_growth_results_and_caption_name"] == "enniatin B1"
    assert chemical["yeast_growth_methods_name"] == "enniatin B"
    assert chemical["yeast_growth_B_B1_discrepancy_resolved"] is False
    assert chemical["mixed_F_avenaceum_extract_induction_is_exact_compound_resistance"] is False
    assert observations["native_B_negative_comparison_is_positive_resistant_allele_evidence"] is False
    assert observations["heterologous_yeast_assay_is_native_fungal_resistance"] is False
    assert observations["export_signal_establishes_growth_resistance_or_direct_transport_kinetics"] is False
    assert observations["endpoint_is_MIC"] is False
    assert observations["earlier_cited_MICs_assigned_to_current_assays"] is False
    assert result["discordant_label_silently_corrected"] is False
    assert result["figures_visually_reviewed"] is False
    assert result["supplements_reviewed"] is False
    assert len(result["locations"]) == 15
    assert "Synthetic fixture" not in json.dumps(result)


def test_primary_checksum_change_requires_new_review():
    with pytest.raises(ValueError, match="reviewed primary article"):
        audit.primary_context(b"<article/>")


@pytest.mark.parametrize("change", ["pmid", "pmcid", "doi", "article_type", "missing", "duplicate", "marker"])
def test_primary_identity_and_location_guards(article, monkeypatch, change):
    if change in {"pmid", "pmcid", "doi"}:
        article.xpath(f'./front/article-meta/article-id[@pub-id-type="{change}"]')[0].text = "OTHER"
    elif change == "article_type":
        article.set("article-type", "review-article")
    else:
        node = article.xpath(audit.LOCATIONS["native_growth"][0])[0]
        if change == "missing":
            node.getparent().remove(node)
        elif change == "duplicate":
            node.getparent().append(copy.deepcopy(node))
        else:
            node.text = "OTHER"
    with pytest.raises(ValueError):
        project_article(article, monkeypatch)


@pytest.fixture
def discovery():
    rows = []
    for identifier, (label, inchikey, count, selected) in audit.RECORDS.items():
        entries = [{"source": "MED", "id": str(i), "title": "Synthetic title"} for i in range(count)]
        if selected:
            entries[0] = {"source": "MED", "id": "42506285", "doi": audit.DOI, "pmcid": "PMC13412724"}
        query = {"hit_count": count, "next_cursor": None, "request": {"status": 200}, "candidates": entries}
        alias = (
            copy.deepcopy(query)
            if identifier == "CHEBI:3000"
            else {"hit_count": 0, "next_cursor": None, "request": {"status": 200}, "candidates": []}
        )
        rows.append(
            {
                "identifier": identifier,
                "label": label,
                "standard_inchi_key": inchikey,
                "candidate_ids": ["MED:" + e["id"] for e in entries],
                "queries": [query, alias],
            }
        )
    return rows


def test_discovery_preserves_cross_record_lead_and_deduplication(discovery):
    result = audit.discovery_context(discovery)
    assert result["record_candidate_memberships"] == 97
    assert result["records"]["CHEBI:64649"]["selected_paper_in_initial_candidates"] is False
    assert result["records"]["CHEBI:64649"]["selected_paper_assessed_via_related_record_lead"] is True
    assert result["records"]["CHEBI:64651"]["selected_paper_in_initial_candidates"] is True
    assert result["distinct_candidate_identities"] < result["record_candidate_memberships"]
    assert result["distinct_primary_text_reviews_this_pass"] == 1


@pytest.mark.parametrize(
    "change",
    [
        "missing_record",
        "duplicate_record",
        "structure",
        "duplicate_id",
        "missing_id",
        "missing_query",
        "partial",
        "count",
        "failed",
        "duplicate_entry",
        "empty_alias_nonempty",
        "paper_doi",
        "paper_pmcid",
        "paper_membership",
        "duplicate_query_disagreement",
    ],
)
def test_discovery_fail_closed(discovery, change):
    row = discovery[0]
    query = row["queries"][0]
    if change == "missing_record":
        discovery.pop()
    elif change == "duplicate_record":
        discovery[-1] = copy.deepcopy(row)
    elif change == "structure":
        row["standard_inchi_key"] = "OTHER"
    elif change == "duplicate_id":
        row["candidate_ids"][-1] = row["candidate_ids"][0]
    elif change == "missing_id":
        row["candidate_ids"].pop()
    elif change == "missing_query":
        row["queries"].pop()
    elif change == "partial":
        query["next_cursor"] = "next"
    elif change == "count":
        query["hit_count"] += 1
    elif change == "failed":
        query["request"]["status"] = 500
    elif change == "duplicate_entry":
        query["candidates"][-1] = copy.deepcopy(query["candidates"][0])
    elif change == "empty_alias_nonempty":
        row["queries"][1]["candidates"] = [copy.deepcopy(query["candidates"][0])]
    elif change in {"paper_doi", "paper_pmcid"}:
        query["candidates"][0][change.removeprefix("paper_")] = "OTHER"
    elif change == "paper_membership":
        query["candidates"][0]["id"] = "999"
        row["candidate_ids"][0] = "MED:999"
    else:
        discovery[-1]["queries"][1]["candidates"][0]["doi"] = "OTHER"
    with pytest.raises(ValueError):
        audit.discovery_context(discovery)


@pytest.mark.parametrize("count", [0, 1])
@pytest.mark.parametrize("change", ["none", "count", "link", "release", "results_type", "missing"])
def test_queries_require_complete_native_results(count, change):
    payload = {"results": [{}] * count, "suggestions": [{"query": "a different locus"}]}
    headers = {"X-Total-Results": str(count), "X-UniProt-Release": "2026_03"}
    if change == "count":
        headers["X-Total-Results"] = str(count + 1)
    elif change == "link":
        headers["Link"] = "next"
    elif change == "release":
        headers["X-UniProt-Release"] = "OTHER"
    elif change == "results_type":
        payload["results"] = {}
    elif change == "missing":
        del payload["results"]
    if change == "none":
        assert audit.complete_query(payload, headers, count) == [{}] * count
    else:
        with pytest.raises(ValueError, match="query incomplete"):
            audit.complete_query(payload, headers, count)


@pytest.fixture
def taxa():
    species = {"taxonId": 5518, "rank": "species", "scientificName": "Gibberella zeae"}
    return {
        "5518": {**species, "active": True, "synonyms": ["Fusarium graminearum"]},
        "4932": {
            "taxonId": 4932,
            "rank": "species",
            "scientificName": "Saccharomyces cerevisiae",
            "active": True,
        },
        "229533": {
            "taxonId": 229533,
            "rank": "strain",
            "active": True,
            "scientificName": (
                "Gibberella zeae (strain ATCC MYA-4620 / CBS 123657 / FGSC 9075 / NRRL 31084 / PH-1)"
            ),
            "lineage": [species],
            "parent": species,
        },
    }


def test_subject_species_are_not_reference_strains(taxa):
    result = audit.organism_context(taxa)
    donor = result["native_fungus_and_gene_donor"]
    host = result["heterologous_assay_host"]
    assert donor["taxon_id"] == "NCBITaxon:5518"
    assert donor["source_background_label"] == "FgLH03"
    assert host["taxon_id"] == "NCBITaxon:4932"
    assert host["source_background_label"] == "AD12345678"
    assert host["export_methods_source_host_label"] == "AD1-8"
    assert host["exact_export_and_growth_derivative_equivalence_independently_verified"] is False
    assert all(x["strain_taxon_id"] is None and x["assembly_accession"] is None for x in (donor, host))


@pytest.mark.parametrize(
    "change", ["species_id", "rank", "name", "active", "synonym", "host_id", "host_rank"]
)
def test_species_grounding_guards(taxa, change):
    if change in {"host_id", "host_rank"}:
        taxa["4932"]["taxonId" if change == "host_id" else "rank"] = (
            559292 if change == "host_id" else "strain"
        )
    elif change == "synonym":
        taxa["5518"]["synonyms"] = []
    else:
        key, value = {
            "species_id": ("taxonId", "5518"),
            "rank": ("rank", "strain"),
            "name": ("scientificName", "OTHER"),
            "active": ("active", False),
        }[change]
        taxa["5518"][key] = value
    with pytest.raises(ValueError):
        audit.organism_context(taxa)


@pytest.fixture
def entry(taxa):
    return {
        "primaryAccession": "I1RWY3",
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": 82, "sequenceVersion": 1},
        "organism": {k: taxa["229533"][k] for k in ("taxonId", "scientificName")},
        "genes": [{"orfNames": [{"value": "FGRAMPH1_01T10921"}]}],
        "proteinDescription": {"submissionNames": [{"fullName": {"value": "Chromosome 2, complete genome"}}]},
        "uniProtKBCrossReferences": [
            {
                "database": "EMBL",
                "id": "HG970333",
                "properties": [
                    {"key": "ProteinId", "value": "CEF77263.1"},
                    {"key": "Status", "value": "-"},
                    {"key": "MoleculeType", "value": "Genomic_DNA"},
                ],
            },
            {
                "database": "VEuPathDB",
                "id": "FungiDB:FGRAMPH1_01G10921",
                "properties": [{"key": "Description", "value": "-"}],
            },
        ],
        "references": [
            {
                "citation": {"citationCrossReferences": [{"database": "PubMed", "id": p}]},
                "referencePositions": ["Private annotation not to export"],
            }
            for p in ("17823352", "20237561", "26198851")
        ],
    }


def test_explicit_crossref_not_fuzzy_transcript_conversion(entry, taxa):
    result = audit.project_reference(entry, taxa["229533"], expanded=True)
    assert result["explicit_source_locus_crosswalk"] == "FungiDB:FGRAMPH1_01G10921"
    assert result["reference_taxon_id"] == "NCBITaxon:229533"
    assert result["reference_species_taxon_id"] == "NCBITaxon:5518"
    assert result["native_crossref_gene_label_inferred_by_G_to_T_replacement"] is False
    assert result["extra_zero_source_label_equivalence_established"] is False
    assert result["reference_accessions_assigned_to_experimental_subject"] is False
    assert result["exact_resistance_allele"] is False
    assert "Private annotation" not in json.dumps(result)
    entry["uniProtKBCrossReferences"] = []
    candidate = audit.project_reference(entry, taxa["229533"], expanded=False)
    assert candidate["explicit_source_locus_crosswalk"] is None
    assert candidate["crosswalk_basis"] == "UNRESOLVED_SEARCH_HIT"
    with pytest.raises(ValueError, match="cross-reference"):
        audit.project_reference(entry, taxa["229533"], expanded=True)


@pytest.mark.parametrize(
    "change",
    [
        "accession",
        "reviewed",
        "entry_version",
        "sequence_version",
        "sequence",
        "features",
        "comments",
        "organism_id",
        "organism_name",
        "taxon_rank",
        "taxon_active",
        "species_lineage",
        "orf",
        "duplicate_gene",
        "gene_name",
        "submission_name",
        "extra_zero_crossref",
        "wrong_database",
        "missing_crossref",
        "duplicate_crossref",
        "protein_id",
        "selected_pmid",
    ],
)
def test_reference_mapping_guards(entry, taxa, change):
    taxon = taxa["229533"]
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif change in {"entry_version", "sequence_version"}:
        entry["entryAudit"]["entryVersion" if change == "entry_version" else "sequenceVersion"] += 1
    elif change in {"sequence", "features", "comments"}:
        entry[change] = {}
    elif change in {"organism_id", "organism_name"}:
        entry["organism"]["taxonId" if change == "organism_id" else "scientificName"] = "OTHER"
    elif change == "taxon_rank":
        taxon["rank"] = "species"
    elif change == "taxon_active":
        taxon["active"] = False
    elif change == "species_lineage":
        taxon["lineage"][0]["taxonId"] = 5519
    elif change == "orf":
        entry["genes"][0]["orfNames"][0]["value"] = "FGRAMPH1_01G10921"
    elif change == "duplicate_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change == "gene_name":
        entry["genes"][0]["geneName"] = {"value": "FgABCB8"}
    elif change == "submission_name":
        entry["proteinDescription"]["submissionNames"][0]["fullName"]["value"] = "OTHER"
    elif change == "extra_zero_crossref":
        entry["uniProtKBCrossReferences"][1]["id"] = "FungiDB:FGRAMPH1_01G010921"
    elif change == "wrong_database":
        entry["uniProtKBCrossReferences"][1]["database"] = "EnsemblFungi"
    elif change == "missing_crossref":
        entry["uniProtKBCrossReferences"].pop()
    elif change == "duplicate_crossref":
        entry["uniProtKBCrossReferences"].append(copy.deepcopy(entry["uniProtKBCrossReferences"][1]))
    elif change == "protein_id":
        entry["uniProtKBCrossReferences"][0]["properties"][0]["value"] = "OTHER"
    else:
        entry["references"][0]["citation"]["citationCrossReferences"][0]["id"] = "42506285"
    with pytest.raises(ValueError):
        audit.project_reference(entry, taxon, expanded=True)


@pytest.mark.parametrize("change", ["missing_attempt", "missing_receipt", "unresolved_attempt"])
def test_request_coverage_fails_closed(tmp_path, change):
    directory = tmp_path / "cache"
    directory.mkdir()
    for key in {"article-2026"} | set(audit.QUERIES):
        for suffix in ("receipt", "attempt"):
            (directory / f"{key}-{suffix}.json").touch()
    if change == "unresolved_attempt":
        (directory / "extra-attempt.json").touch()
    else:
        (directory / f"article-2026-{change.removeprefix('missing_')}.json").unlink()
    with pytest.raises(ValueError, match="research request coverage"):
        audit.build(tmp_path, Path("cache"))


def test_public_checkpoint_scope():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["corpus_records_hash_checked_at_preflight"] == 2939
    assert result["discovery"]["distinct_candidate_identities"] == 76
    assert result["discovery"]["initial_candidates_without_primary_text_review_this_pass"] == 75
    assert result["limits"]["new_resistance_assertions"] == 0
    assert result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["reference_mappings_grounded"] == 1
    assert result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"
    assert result["query_interpretation"]["provider_spelling_suggestions_followed"] is False


def test_cache_replay_is_offline_and_does_not_load_live_records(monkeypatch):
    if not (ROOT / audit.CACHE / "article-2026-receipt.json").exists():
        pytest.skip("private source cache is not distributed")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    original_open = Path.open

    def guarded_open(path, *args, **kwargs):
        if path.is_relative_to(ROOT / "data/antibiotics"):
            raise AssertionError("historical replay read a live record")
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(Path, "open", guarded_open)
    assert audit.build(ROOT) == json.loads((ROOT / audit.OUTPUT).read_bytes())
