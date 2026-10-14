"""An archived donor protein is not an active UniProtKB or experimental allele assignment."""

import copy
import json
import socket
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_platen_archives as audit  # noqa: E402


@pytest.fixture(params=["fabF", "fabH"])
def archive(request):
    gene = request.param
    parent, protein, upi, kb, name = audit.GENES[gene]
    product = "F" + gene[1:]
    organism = {"taxonId": 58346, "scientificName": "Streptomyces platensis"}
    coding = {k: "" for k in audit.ARCHIVE_FIELDS.split(",")}
    coding.update(
        {
            "accession": protein,
            "parent_accession": parent,
            "protein_id": protein + ".1",
            "product": product,
            "strain": "MA7327",
            "sequence_version": "1",
            "first_public": "2013-11-27",
            "last_updated": "2014-05-15",
        }
    )
    parent_row = {
        "accession": parent,
        "sequence_version": "1",
        "tax_id": "58346",
        "description": f"Streptomyces platensis strain MA7327 {product} gene, complete cds.",
        "scientific_name": "Streptomyces platensis",
        "strain": "MA7327",
        "first_public": "2013-11-27",
        "last_updated": "2014-05-15",
    }
    candidate = {"uniParcId": upi, "uniProtKBAccessions": [kb + ".1"], "organisms": [organism]}
    crossrefs = [
        {
            "database": "EMBL",
            "id": protein,
            "version": 1,
            "versionI": 1,
            "active": True,
            "created": "2014-01-06",
            "lastUpdated": "2026-03-19",
            "proteinName": product,
            "organism": organism,
            "ncbiGi": "not exported",
        },
        {
            "database": "UniProtKB/TrEMBL",
            "id": kb,
            "version": 1,
            "versionI": 1,
            "active": False,
            "created": "2014-02-19",
            "lastUpdated": "2026-01-28",
            "proteinName": name,
            "organism": organism,
        },
    ]
    if gene == "fabH":
        crossrefs[1]["geneName"] = "fabH"
    return [gene, coding, parent_row, candidate, crossrefs, {**organism, "rank": "species", "active": True}]


def test_exact_archival_mapping_retains_active_status_and_scope(archive):
    gene, coding, parent, candidate, crossrefs, taxon = archive
    result = audit.project_archive(*archive)
    assert result["donor_protein_archive"] == "EMBL:" + coding["protein_id"]
    assert result["donor_parent_archive"] == "EMBL:" + parent["accession"] + ".1"
    assert result["uniparc_id"] == "UniParc:" + candidate["uniParcId"]
    assert result["historical_uniprotkb_crossref"]["active"] is False
    assert result["EMBL_crossref"]["active"] is True
    assert result["active_current_uniprotkb_mapping_established"] is False
    assert result["reference_accessions_assigned_to_tested_host_or_allele"] is False
    assert result["gene_archives_are_whole_genomes"] is False
    assert result["strain_taxon_id"] is None
    assert result["experimental_genome_assignment"] is None
    assert result["archive_membership_is_phenotype_or_mechanism_evidence"] is False
    assert result["existing_positive_claims_in_two_records"] == (2 if gene == "fabF" else 0)
    assert result["coding_record_blank_fields_preserved"] == ["gene", "scientific_name", "tax_id"]
    assert "not exported" not in json.dumps(result)
    crossrefs.reverse()
    assert audit.project_archive(gene, coding, parent, candidate, crossrefs, taxon) == result


@pytest.mark.parametrize(
    "change",
    [
        "unknown_gene",
        "coding_accession",
        "coding_parent",
        "coding_protein_version",
        "coding_version",
        "coding_product",
        "coding_strain",
        "coding_gene",
        "coding_taxon",
        "coding_name",
        "coding_sequence",
        "parent_accession",
        "parent_version",
        "parent_taxon",
        "parent_name",
        "parent_strain",
        "parent_description",
        "taxon_id",
        "taxon_rank",
        "taxon_name",
        "taxon_active",
        "candidate_upi",
        "candidate_kb",
        "candidate_organism",
        "candidate_sequence",
        "missing_crossref",
        "duplicate_crossref",
        "crossref_sequence",
        "embl_id",
        "embl_active",
        "embl_version",
        "embl_version_bool",
        "embl_internal_version",
        "embl_name",
        "embl_organism",
        "kb_id",
        "kb_active",
        "kb_name",
        "kb_gene",
        "kb_version",
        "kb_organism",
        "kb_created",
        "kb_updated",
        "embl_created",
        "embl_updated",
    ],
)
def test_mapping_rejects_identity_version_and_scope_drift(archive, change):
    _, coding, parent, candidate, crossrefs, taxon = archive
    embl, kb = crossrefs
    if change == "unknown_gene":
        archive[0] = "fabG"
    elif change.startswith("coding_"):
        key, value = {
            "accession": ("accession", "OTHER"),
            "parent": ("parent_accession", "OTHER"),
            "protein_version": ("protein_id", coding["protein_id"][:-1] + "2"),
            "version": ("sequence_version", "2"),
            "product": ("product", "OTHER"),
            "strain": ("strain", "J1074"),
            "gene": ("gene", archive[0]),
            "taxon": ("tax_id", "1886"),
            "name": ("scientific_name", "OTHER"),
            "sequence": ("sequence", "PRIVATE"),
        }[change.removeprefix("coding_")]
        coding[key] = value
    elif change.startswith("parent_"):
        key, value = {
            "accession": ("accession", "OTHER"),
            "version": ("sequence_version", "2"),
            "taxon": ("tax_id", "1886"),
            "name": ("scientific_name", "OTHER"),
            "strain": ("strain", "DSM 40041"),
            "description": ("description", "OTHER"),
        }[change.removeprefix("parent_")]
        parent[key] = value
    elif change.startswith("taxon_"):
        key, value = {
            "id": ("taxonId", "58346"),
            "rank": ("rank", "strain"),
            "name": ("scientificName", "OTHER"),
            "active": ("active", False),
        }[change.removeprefix("taxon_")]
        taxon[key] = value
    elif change.startswith("candidate_"):
        key, value = {
            "upi": ("uniParcId", "UPI_OTHER"),
            "kb": ("uniProtKBAccessions", ["OTHER.1"]),
            "organism": ("organisms", []),
            "sequence": ("sequence", {}),
        }[change.removeprefix("candidate_")]
        candidate[key] = value
    elif change == "missing_crossref":
        crossrefs.pop()
    elif change == "duplicate_crossref":
        crossrefs[1] = copy.deepcopy(embl)
    elif change == "crossref_sequence":
        embl["sequence"] = {}
    else:
        row = embl if change.startswith("embl_") else kb
        suffix = change.split("_", 1)[1]
        key, value = {
            "id": ("id", "OTHER"),
            "active": ("active", not row["active"]),
            "version": ("version", 2),
            "version_bool": ("version", True),
            "internal_version": ("versionI", 2),
            "name": ("proteinName", "OTHER"),
            "gene": ("geneName", "OTHER"),
            "organism": ("organism", {"taxonId": 1886}),
            "created": ("created", "2026-10-14"),
            "updated": ("lastUpdated", "2026-10-14"),
        }[suffix]
        row[key] = value
    with pytest.raises(ValueError):
        audit.project_archive(*archive)


@pytest.fixture
def configurations():
    return {
        "ena-results": b"resultId\tdescription\tprimaryAccessionType\ncoding\tCoding sequences\taccession\n",
        "coding-return-fields": ("columnId\n" + "\n".join(audit.ARCHIVE_FIELDS.split(",")) + "\n").encode(),
        "coding-search-fields": b"columnId\nparent_accession\n",
        "uniparc-search-fields": json.dumps(
            [
                {"term": "dbid", "label": "Database ID"},
                {"term": "database", "values": [{"name": "EMBL CDS", "value": "embl-cds"}]},
            ]
        ).encode(),
    }


def test_documented_metadata_fields(configurations):
    audit.validate_configurations(configurations)


@pytest.mark.parametrize(
    "change", ["result", "duplicate_result", "return_field", "search_field", "dbid", "database"]
)
def test_configuration_drift_fails_closed(configurations, change):
    if change == "result":
        configurations["ena-results"] = configurations["ena-results"].replace(b"Coding sequences", b"OTHER")
    elif change == "duplicate_result":
        configurations["ena-results"] += b"coding\tCoding sequences\taccession\n"
    elif change == "return_field":
        configurations["coding-return-fields"] = configurations["coding-return-fields"].replace(
            b"protein_id\n", b""
        )
    elif change == "search_field":
        configurations["coding-search-fields"] = b"columnId\nOTHER\n"
    else:
        rows = json.loads(configurations["uniparc-search-fields"])
        if change == "dbid":
            rows[0]["term"] = "OTHER"
        else:
            rows[1]["values"] = []
        configurations["uniparc-search-fields"] = json.dumps(rows).encode()
    with pytest.raises(ValueError):
        audit.validate_configurations(configurations)


def test_planned_urls_are_metadata_only_and_not_ncbi():
    urls = audit.urls()
    assert len(urls) == 11
    for _, url in urls.values():
        parts = urlsplit(url)
        assert parts.hostname in {"www.ebi.ac.uk", "rest.uniprot.org"}
        fields = parse_qs(parts.query).get("fields", [""])[0].split(",")
        assert not {"sequence", "translation", "alteration", "features"} & set(fields)
    assert parse_qs(urlsplit(urls["archive-fabF"][1]).query)["query"] == ['parent_accession="KF543053"']
    assert parse_qs(urlsplit(urls["uniparc-protein-ids"][1]).query)["query"] == [
        "(dbid:AHA90851 OR dbid:AHA90852) AND database:embl-cds"
    ]


@pytest.mark.parametrize("change", ["missing_attempt", "missing_receipt", "unresolved_attempt"])
def test_request_coverage_fails_closed(tmp_path, change):
    directory = tmp_path / "cache"
    directory.mkdir()
    for key in audit.urls():
        for suffix in ("receipt", "attempt"):
            (directory / f"{key}-{suffix}.json").touch()
    if change == "unresolved_attempt":
        (directory / "extra-attempt.json").touch()
    else:
        (directory / f"ena-results-{change.removeprefix('missing_')}.json").unlink()
    with pytest.raises(ValueError, match="request coverage"):
        audit.build(tmp_path, Path("cache"))


def test_public_checkpoint_separates_current_and_archival_grounding():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["corpus_records_hash_checked_at_preflight"] == 2939
    assert len(result["donor_references"]) == 2
    assert result["query_interpretation"]["current_uniprotkb_exact_protein_id_query_results"] == 0
    assert result["query_interpretation"]["historical_UniProtKB_crossrefs_inactive"] == 2
    assert result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["experimental_allele_assignments"] == 0
    assert result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"
    assert result["preserved_claim_scope"]["host_species_taxon_id"] == "NCBITaxon:1886"


def test_private_cache_replay_is_offline_and_does_not_load_live_records(monkeypatch):
    if not (ROOT / audit.CACHE / "ena-results-receipt.json").exists():
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
