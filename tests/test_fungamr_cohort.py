"""A database citation and reference identity cannot establish a tested allele."""

import copy
import hashlib
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_fungamr_cohort as audit  # noqa: E402


def metadata():
    entry = {
        "primaryAccession": "P43071",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 115, "sequenceVersion": 1},
        "genes": [{"geneName": {"value": "CDR1"}}],
        "organism": {"taxonId": 5476, "scientificName": "Candida albicans"},
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference protein"}}},
    }
    tax = {
        "taxonId": 5476,
        "rank": "species",
        "active": True,
        "scientificName": "Candida albicans",
        "lineage": [],
    }
    chosen = {"accession": "P43071", "gene": "CDR1", "species_id": 5476, "reference_taxon_id": 5476}
    return entry, tax, chosen


@pytest.mark.parametrize(
    "change",
    [
        "none",
        "accession",
        "taxon",
        "species",
        "name",
        "gene",
        "paralog",
        "duplicate_gene",
        "unreviewed",
        "inactive",
        "rank",
        "version",
    ],
)
def test_reference_identity_boundaries(change):
    entry, tax, chosen = metadata()
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "taxon":
        entry["organism"]["taxonId"] = 5482
    elif change == "species":
        chosen["species_id"] = 5482
    elif change == "name":
        tax["scientificName"] = "Candida tropicalis"
    elif change in {"gene", "paralog"}:
        entry["genes"][0]["geneName"]["value"] = "CDR2" if change == "paralog" else "OTHER"
    elif change == "duplicate_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change == "unreviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change == "inactive":
        tax["active"] = False
    elif change == "rank":
        tax["rank"] = "subspecies"
        tax["lineage"] = [{"rank": "species", "taxonId": 5476, "scientificName": "Candida albicans"}]
    elif change == "version":
        entry["entryAudit"]["sequenceVersion"] = True
    if change != "none":
        with pytest.raises(ValueError):
            audit.project(entry, tax, chosen, "Candida albicans")
        return
    result = audit.project(entry, tax, chosen, "Candida albicans")
    assert result["protein_accession"] == "UniProtKB:P43071"
    assert result["source_species_taxon_id"] == "NCBITaxon:5476"
    for key in (
        "exact_resistance_allele",
        "experimental_subject_assignment",
        "exact_card_term_mapping_asserted",
        "exact_fungamr_row_crosswalk_verified",
        "database_paper_in_bibliography",
    ):
        assert result[key] is False
    assert result["experimental_genome_assignment"] is None


def test_projection_excludes_operational_fields_even_in_old_cache():
    entry, tax, chosen = metadata()
    entry.update(
        {
            "sequence": {"value": "PRIVATE"},
            "features": [{"description": "PRIVATE"}],
            "comments": [{"text": "PRIVATE"}],
            "uniProtKBCrossReferences": [{"id": "PRIVATE"}],
        }
    )
    result = audit.project(entry, tax, chosen, "Candida albicans")
    assert "PRIVATE" not in json.dumps(result)


@pytest.mark.parametrize("wrapper", [True, False])
@pytest.mark.parametrize(
    "change", ["none", "payload", "status", "url", "host", "release", "pagination", "total", "bytes"]
)
def test_cached_transport_integrity(tmp_path, wrapper, change):
    payload = json.dumps({"results": [{"primaryAccession": "P43071"}]}).encode()
    url = "https://rest.uniprot.org/uniprotkb/search?query=lit_pubmed%3A7614555"
    receipt = {
        "url": url,
        "status": 200,
        "sha256": hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "retrieved_at": "2026-10-13T12:39:52Z",
        "headers": {"X-UniProt-Release": "2026_03", "X-Total-Results": "1"},
    }
    if change == "payload":
        receipt["sha256"] = "0" * 64
    elif change == "status":
        receipt["status"] = 403
    elif change == "url":
        receipt["url"] += "x"
    elif change == "host":
        url = receipt["url"] = url.replace("rest.uniprot.org", "example.org")
    elif change == "release":
        receipt["headers"]["X-UniProt-Release"] = "OTHER"
    elif change == "pagination":
        receipt["headers"]["Link"] = "next"
    elif change == "total":
        receipt["headers"]["X-Total-Results"] = "2"
    elif change == "bytes":
        receipt["bytes"] += 1
    if wrapper:
        receipt["body"] = payload.decode()
        path = tmp_path / "wrapper.json"
        path.write_text(json.dumps(receipt))
        source = {"wrapper": audit.reference.pin(tmp_path, path), "url": url}
    else:
        path, receipt_path = tmp_path / "response.bin", tmp_path / "receipt.json"
        path.write_bytes(payload)
        receipt_path.write_text(json.dumps(receipt))
        source = {
            "body": audit.reference.pin(tmp_path, path),
            "receipt": audit.reference.pin(tmp_path, receipt_path),
            "url": url,
        }
    if change != "none":
        with pytest.raises(ValueError):
            audit.read_source(tmp_path, source)
        return
    body, provenance = audit.read_source(tmp_path, source)
    assert len(body["results"]) == 1 and provenance["release"] == "2026_03"


@pytest.mark.parametrize("change", ["none", "duplicate", "missing", "gene", "label_hash", "relation"])
def test_source_term_membership(change):
    rows, definitions = [], {}
    for term, gene in audit.GENES.items():
        label = f"Genus species {gene} reference context"
        rows.append(
            {
                "determinant_id": term,
                "determinant_name": label,
                "antibiotic_id": "ARO:1",
                "antibiotic_name": "compound",
                "relation": "confers_resistance_to_antibiotic",
            }
        )
        definitions[term] = {
            "label_sha256": hashlib.sha256(label.encode()).hexdigest(),
            "definition_citation_ids": [audit.PMID],
            "record_memberships": ["CHEBI:1"],
        }
    if change == "duplicate":
        rows.append(copy.deepcopy(rows[0]))
    elif change == "missing":
        rows.pop()
    elif change == "gene":
        rows[0]["determinant_name"] = "Genus species WRONG context"
    elif change == "label_hash":
        definitions[rows[0]["determinant_id"]]["label_sha256"] = "0" * 64
    elif change == "relation":
        rows[0]["relation"] = "unrelated"
    if change != "none":
        with pytest.raises(ValueError):
            audit.source_terms(rows, definitions)
        return
    result = audit.source_terms(rows, definitions)
    assert len(result) == 19
    assert all(
        r["exact_allele_assignment"] is None and not r["new_resistance_assertion"] for r in result.values()
    )


def test_saved_checkpoint_has_no_subject_or_allele_promotion():
    context = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert len(context["records"]) == 10 and len(context["terms"]) == 19
    assert context["summary"]["reference_contexts_reconciled"] == 6
    assert context["summary"]["terms_without_reference_resolution_here"] == 13
    assert context["new_network_requests"] == 0
    assert all(
        t["exact_allele_assignment"] is None
        and t["experimental_subject_assignment"] is None
        and not t["whole_record_review_complete"]
        for t in context["terms"].values()
    )
    references = {
        k: t["reference"]["protein_accession"].split(":", 1)[1]
        for k, t in context["terms"].items()
        if "reference" in t
    }
    assert references == audit.SELECTED
    finding = context["review_findings"][0]
    assert finding["label_drug"] != finding["edge_drug"]
    assert finding["status"] == "OPEN_SOURCE_CONTEXT_REQUIRED"
