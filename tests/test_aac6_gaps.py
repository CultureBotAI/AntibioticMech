"""Reject overbroad AAC6 allele and native-isolate interpretations."""

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
import audit_aac6_gaps as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def taxon(taxid, name, parentid, parentname):
    return {
        "taxonId": taxid,
        "scientificName": name,
        "rank": "species",
        "active": True,
        "parent": {"taxonId": parentid, "scientificName": parentname},
        "lineage": [
            {"taxonId": 2, "scientificName": "Bacteria", "rank": "domain"},
            {"taxonId": parentid, "scientificName": parentname, "rank": "genus"},
        ],
    }


def entry_fixture(accession):
    expected = audit.SELECTED[accession]
    kinds = [k for k, n in expected["citations"].items() for _ in range(n)]
    references = [
        {"referenceNumber": i + 1, "citation": {"citationType": k, "title": "Other source"}}
        for i, k in enumerate(kinds)
    ]
    references[0]["citation"].update(
        {
            "title": "Characterization in Pseudomonas aeruginosa",
            "citationCrossReferences": [
                {"database": "PubMed", "id": "11158753"},
                {"database": "DOI", "id": audit.DOI},
            ],
        }
    )
    return {
        "primaryAccession": accession,
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": expected["version"], "sequenceVersion": 1},
        "genes": [{"geneName": {"value": expected["gene"]}}],
        "organism": {"taxonId": 287, "scientificName": "Pseudomonas aeruginosa"},
        "proteinDescription": {
            "submissionNames": [
                {"fullName": {"value": "Aminoglycoside acetyltransferase " + expected["label"]}}
            ]
        },
        "uniProtKBCrossReferences": [],
        "references": references,
    }, taxon(287, "Pseudomonas aeruginosa", 286, "Pseudomonas")


@pytest.mark.parametrize("accession", audit.SELECTED)
def test_distinct_native_references_are_not_tested_alleles(accession):
    args = entry_fixture(accession)
    before = copy.deepcopy(args)
    result = audit.project_reference(*args)
    assert args == before
    assert result["accession"] == "UniProtKB:" + accession
    assert result["gene_symbols"] == [audit.SELECTED[accession]["gene"]]
    assert result["reference_taxon_id"] == "NCBITaxon:287"
    assert result["exact_allele_assignment"] is result["experimental_subject_assignment"] is False
    assert result["primary_results_reviewed"] is result["submission_name_is_expert_review"] is False
    assert result["experimental_allele_assignment"] is result["experimental_genome_assignment"] is None
    assert result["scope"] == audit.REFERENCE


@pytest.mark.parametrize("accession", audit.SELECTED)
@pytest.mark.parametrize(
    "change",
    [
        "gene",
        "name",
        "version",
        "boolean_version",
        "reviewed",
        "taxon",
        "rank",
        "inactive",
        "parent",
        "xref",
        "flag",
        "sequence",
        "citation",
        "doi",
        "count",
    ],
)
def test_reference_identity_guards(accession, change):
    entry, taxonomy = entry_fixture(accession)
    if change == "gene":
        entry["genes"][0]["geneName"]["value"] = "aacA29"
    elif change == "name":
        entry["proteinDescription"]["submissionNames"][0]["fullName"]["value"] += "-other"
    elif change == "version":
        entry["entryAudit"]["entryVersion"] += 1
    elif change == "boolean_version":
        entry["entryAudit"]["sequenceVersion"] = True
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif change == "taxon":
        entry["organism"]["taxonId"] = 562
    elif change == "rank":
        taxonomy["rank"] = "strain"
    elif change == "inactive":
        taxonomy["active"] = False
    elif change == "parent":
        taxonomy["parent"]["scientificName"] = "Other"
    elif change == "xref":
        entry["uniProtKBCrossReferences"] = [{"database": "CARD", "id": "other"}]
    elif change == "flag":
        entry["proteinDescription"]["flag"] = "Fragment"
    elif change == "sequence":
        entry["sequence"] = {}
    elif change == "citation":
        entry["references"][0]["citation"]["citationCrossReferences"][0]["id"] = "1"
    elif change == "doi":
        entry["references"][0]["citation"]["citationCrossReferences"][1]["id"] = "10.1000/other"
    else:
        entry["references"].pop()
    with pytest.raises(ValueError):
        audit.project_reference(entry, taxonomy)


@pytest.mark.parametrize(
    "name,match",
    [
        ("Aminoglycoside acetyltransferase AAC(6')-29a", True),
        ("aac(6')-29a", True),
        ("AAC(6')-29ab", False),
        ("AAC(6')-29a-cr", False),
        ("AAC(6')-29b", False),
        ("aacA29a", False),
        ("AAC(6\u2032)-29a", False),
        ("xAAC(6')-29a", False),
        ("AAC(6')-29a'", False),
    ],
)
def test_protein_names_are_specific_not_generic_aliases(name, match):
    entry = {"proteinDescription": {"submissionNames": [{"fullName": {"value": name}}]}}
    assert bool(audit.name_matches(entry, "AAC(6')-29a")) is match
    assert audit.name_matches({"genes": [{"geneName": {"value": "AAC(6')-29a"}}]}, "AAC(6')-29a") == []


@pytest.fixture
def challenge():
    body = b"<html><head><title>Just a moment...</title></head></html>"
    receipt = {
        "url": audit.PRIMARY_URL,
        "status": 403,
        "sha256": hashlib.sha256(body).hexdigest(),
        "bytes": len(body),
        "headers": {"cf-mitigated": "challenge"},
        "retry_performed": False,
        "redirects_followed": False,
    }
    return body, receipt


def test_primary_403_is_a_hold_not_a_pdf_or_biological_negative(challenge):
    result = audit.primary_hold(*challenge)
    assert result["pdf_retrieved"] is result["primary_results_reviewed"] is False
    assert result["biological_absence_inferred"] is result["permanent_unavailability_inferred"] is False
    assert result["revisit_requires"] == "USER_SUPPLIED_PRIMARY_COPY_OR_NEW_EXPLICIT_DIRECTION"


@pytest.mark.parametrize(
    "field,value",
    [
        ("url", "https://example.org/other"),
        ("status", 200),
        ("sha256", "other"),
        ("bytes", 0),
        ("retry_performed", True),
        ("redirects_followed", True),
        ("headers", {}),
    ],
)
def test_challenge_identity_guards(challenge, field, value):
    body, receipt = challenge
    receipt[field] = value
    with pytest.raises(ValueError):
        audit.primary_hold(body, receipt)


@pytest.fixture
def lc231():
    columns = [
        "Resistance Determinant",
        "Name",
        "Antibiotic class",
        "Antibiotic",
        "MIC (\u03bcg ml\u22121)",
        "Empty vector control MIC (\u03bcg ml\u22121)",
    ]
    cells = ["Kanamycin acetyltransferase", "aac(6\u2032)-34", "Aminoglycoside", "Kanamycin", ">128", "8"]
    payload = (
        "<article><front><article-meta><article-id pub-id-type='pmid'>27929110</article-id>"
        "<article-id pub-id-type='doi'>10.1038/ncomms13803</article-id></article-meta></front>"
        "<body><sec id='sec2'><title>Paenibacillus sp. LC231 is multi-drug resistant</title></sec>"
        "<table-wrap id='t1'><caption>MICs of antibiotic resistance determinants "
        "heterologously expressed in E. coli.</caption>"
        "<table><thead><tr>"
        + "".join("<th>" + c + "</th>" for c in columns)
        + "</tr></thead><tbody><tr>"
        + "".join("<td>" + c + "</td>" for c in cells)
        + "</tr></tbody></table></table-wrap></body></article>"
    ).encode()
    donor = taxon(1120679, "Paenibacillus sp. (strain LC231)", 185978, "unclassified Paenibacillus")
    host = taxon(562, "Escherichia coli", 561, "Escherichia")
    return payload, donor, host


def test_primary_mic_preserves_comparator_host_and_compound_limit(lc231):
    result = audit.project_lc231(*lc231)
    assert result["reported_determinant_mic"] == {
        "original_value": ">128",
        "original_unit": "ug/mL",
        "comparator": ">",
        "value": 128,
        "unit": "mg/L",
        "conversion_factor": 1,
    }
    assert result["reported_control_mic"]["value"] == 8
    assert result["reported_control_mic"]["comparator"] == "="
    assert result["source_isolate_taxon_reference"] == "NCBITaxon:1120679"
    assert result["source_isolate_native_rank"] == "species"
    assert result["assay_host_species_taxon"] == "NCBITaxon:562"
    assert result["native_isolate_MIC_inferred"] is False
    assert result["exact_corpus_structure_assignment"] is result["clinical_resistance_category"] is None
    assert result["experimental_protein_assignment"] is result["experimental_genome_assignment"] is None


@pytest.mark.parametrize(
    "before,after",
    [
        ("27929110", "1"),
        ("ncomms13803", "other"),
        ("E. coli.", "Paenibacillus."),
        ("LC231 is", "LC999 is"),
        ("aac(6\u2032)-34", "aac(6\u2032)-35"),
        (">128", "128"),
        ("<td>8</td>", "<td>16</td>"),
        ("Kanamycin</td>", "Kanamycin A</td>"),
        ("\u03bcg ml\u22121", "mm"),
    ],
)
def test_table_and_units_cannot_be_silently_reinterpreted(lc231, before, after):
    body, donor, host = lc231
    with pytest.raises(ValueError):
        audit.project_lc231(body.replace(before.encode(), after.encode()), donor, host)


@pytest.mark.parametrize(
    "role,field,value", [(1, "rank", "strain"), (1, "taxonId", 1), (2, "taxonId", 287), (2, "active", False)]
)
def test_donor_and_host_taxonomy_cannot_be_swapped(lc231, role, field, value):
    lc231[role][field] = value
    with pytest.raises(ValueError):
        audit.project_lc231(*lc231)


def test_saved_public_invariants_without_request_caches():
    data = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert data["summary"] == {
        "source_terms": 15,
        "source_claims": 70,
        "cohort_records": 12,
        "corpus_records_hash_checked": 2939,
        "complete_cached_citation_queries": 12,
        "citation_query_entries": 154,
        "distinct_citation_entries": 153,
        "term_statuses": {audit.EMPTY: 5, audit.NO_CITATION: 4, audit.AMBIGUOUS: 4, audit.REFERENCE: 2},
        "new_reference_links": 2,
        "new_reference_memberships": 10,
        "new_primary_access_holds": 1,
        "cached_primary_table_context_reviews": 1,
    }
    assert all(
        not t["prior_term"]["links"]
        and not t["experimental_subject_assignment"]
        and not t["biological_absence_inferred"]
        for t in data["terms"].values()
    )
    assert all(data["terms"][tid]["status"] == audit.NO_CITATION for tid in ("ARO:3007770", "ARO:3007771"))
    assert set(data["references"]) == {"UniProtKB:Q9AIK8", "UniProtKB:Q9AIK9"}
    assert len(data["terms"]["ARO:3002567"]["related_family_context"]) == 7
    assert data["primary_access_hold"]["http_status"] == 403
    assert data["constraints"]["ncbi_requests"] == 0 and data["constraints"]["issue_1040"] == "DEFERRED"
    assert not any(data["disposition"].values())
    assert data["aac34_primary_table_context"]["exact_corpus_structure_assignment"] is None
    assert data["aac34_primary_table_context"]["reported_determinant_mic"]["comparator"] == ">"


def test_native_replay_when_caches_available(pre_card_qualification_root):
    if not (ROOT / audit.CACHE / "cohort.json").exists():
        pytest.skip("native research caches unavailable; public invariants and synthetic guards still run")
    result = audit.build(pre_card_qualification_root)
    assert (json.dumps(result, sort_keys=True, indent=2) + "\n").encode() == (
        ROOT / audit.OUTPUT
    ).read_bytes()


def test_cli_is_exclusive_and_checks_missing_output(tmp_path, monkeypatch):
    path = tmp_path / "test.json"
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    monkeypatch.setattr(sys, "argv", ["audit", "--check", "--output", str(path)])
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not path.exists()
    monkeypatch.setattr(sys, "argv", ["audit", "--output", str(path)])
    audit.main()
    audit.main()
    path.write_text("different\n")
    with pytest.raises(ValueError, match="does not reproduce"):
        audit.main()
