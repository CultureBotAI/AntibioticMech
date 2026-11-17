"""Keep publication context, native reference identity and resistance separate."""

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
import audit_cytochrome_b_evidence as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture
def metadata(monkeypatch):
    monkeypatch.setitem(audit.ABSTRACT_SHA, "29996698", hashlib.sha256(b"Abstract fixture").hexdigest())
    return {
        "hitCount": 1,
        "request": {"queryString": "EXT_ID:29996698 AND SRC:MED", "resultType": "CORE", "pageSize": 1},
        "resultList": {
            "result": [
                {
                    **audit.PUBLICATIONS["29996698"],
                    "id": "29996698",
                    "pmid": "29996698",
                    "source": "MED",
                    "abstractText": "Abstract fixture",
                }
            ]
        },
    }


def test_metadata_is_not_primary_or_global_access_decision(metadata):
    result = audit.project_metadata(metadata, "29996698")
    assert result["doi"] == "10.1094/phyto-04-18-0128-r"
    assert result["primary_request_performed"] is False
    assert result["abstract_is_experimental_crosswalk"] is False
    assert result["global_access_or_paywall_inferred"] is False
    assert "abstractText" not in result


@pytest.mark.parametrize("field,value", [("hitCount", True), ("hitCount", 2), ("nextCursorMark", "next")])
def test_metadata_query_must_be_complete(metadata, field, value):
    metadata[field] = value
    with pytest.raises(ValueError, match="completeness"):
        audit.project_metadata(metadata, "29996698")


@pytest.mark.parametrize(
    "field,value",
    [
        ("queryString", "EXT_ID:28201983 AND SRC:MED"),
        ("resultType", "lite"),
        ("pageSize", True),
        ("pageSize", 2),
    ],
)
def test_exact_query_required(metadata, field, value):
    metadata["request"][field] = value
    with pytest.raises(ValueError, match="query scope"):
        audit.project_metadata(metadata, "29996698")


@pytest.mark.parametrize(
    "field,value",
    [
        ("id", "28201983"),
        ("pmid", "28201983"),
        ("source", "PMC"),
        ("doi", ".1094/PHYTO-04-18-0128-R"),
        ("title", "Other"),
        ("pubYear", "2017"),
        ("pmcid", "PMC5311727"),
        ("abstractText", "Changed"),
        ("isOpenAccess", "Y"),
    ],
)
def test_publication_identity_and_inspected_abstract_required(metadata, field, value):
    metadata["resultList"]["result"][0][field] = value
    with pytest.raises(ValueError, match="publication identity"):
        audit.project_metadata(metadata, "29996698")


def test_duplicate_metadata_hit_rejected(metadata):
    metadata["resultList"]["result"] *= 2
    with pytest.raises(ValueError, match="completeness"):
        audit.project_metadata(metadata, "29996698")


@pytest.fixture
def primary(monkeypatch):
    payload = b"""<article xmlns:xlink="http://www.w3.org/1999/xlink"><front><article-meta>
    <article-id pub-id-type="pmid">28201983</article-id>
    <article-id pub-id-type="pmcid">PMC5311727</article-id>
    <article-id pub-id-type="doi">10.1186/s12864-016-3480-x</article-id>
    </article-meta></front><body><sec id="Sec9">Labels fixture</sec>
    <sec id="Sec16">Conclusion fixture</sec><sec id="FPar2">Availability fixture</sec>
    <media id="MOESM1" xlink:href="12864_2016_3480_MOESM1_ESM.xlsx"/></body></article>"""
    monkeypatch.setitem(audit.BODY_SHA, "primary-28201983", hashlib.sha256(payload).hexdigest())
    tree = etree.fromstring(payload)
    for key in audit.SECTION_SHA:
        (element,) = tree.xpath(f".//*[@id='{key}']")
        text = " ".join("".join(element.itertext()).split())
        monkeypatch.setitem(audit.SECTION_SHA, key, hashlib.sha256(text.encode()).hexdigest())
    return payload


def test_selected_primary_context_preserves_qualification_and_gaps(primary):
    result = audit.project_primary(primary)
    assert result["primary_xml_obtained"] is True
    assert result["status"].endswith("NOT_FULL_PAPER_SIGNOFF")
    groups = result["source_isolate_groups"]
    assert sum(len(g["source_isolate_labels"]) for g in groups) == 9
    (siamense,) = [g for g in groups if g["source_organism_label"] == "C. siamense s.l."]
    assert len(siamense["source_isolate_labels"]) == 6
    for group in groups:
        assert group["experimental_subject_taxon_id"] is group["resistant_allele_assignment"] is None
        assert group["experimental_genome_accessions"] == []
    assert result["supplement"]["retrieved"] is result["supplement"]["reviewed"] is False
    for field in (
        "siamense_sensu_lato_collapsed_to_current_species",
        "figures_visually_reviewed",
        "selected_text_establishes_drug_specific_resistance",
        "full_paper_signoff",
        "off_target_figure_accessions_used",
        "numeric_AST_exported",
        "absence_of_resistance_words_is_susceptibility",
    ):
        assert result[field] is False


def test_primary_bytes_pinned(primary):
    with pytest.raises(ValueError, match="XML changed"):
        audit.project_primary(primary + b" ")


@pytest.mark.parametrize(
    "old,new",
    [
        (b"28201983", b"29996698"),
        (b"PMC5311727", b"PMC1"),
        (b"s12864-016-3480-x", b"other"),
        (b"Sec9", b"Sec99"),
        (b"Labels fixture", b"Different"),
        (b"_ESM.xlsx", b"_OTHER.xlsx"),
    ],
)
def test_primary_identity_locations_and_native_asset_required(primary, monkeypatch, old, new):
    changed = primary.replace(old, new)
    monkeypatch.setitem(audit.BODY_SHA, "primary-28201983", hashlib.sha256(changed).hexdigest())
    with pytest.raises(ValueError):
        audit.project_primary(changed)


@pytest.fixture
def receipt():
    return {
        "url": audit.ARTICLE,
        "status": 403,
        "retry_performed": False,
        "redirects_followed": False,
        "headers": {"Cf-Mitigated": "challenge"},
        "retrieved_at": "2026-10-15T05:37:48+00:00",
    }


def test_supplement_discovery_hold_does_not_erase_obtained_xml(receipt):
    hold = audit.project_hold(receipt, b"<html><title>Just a moment...</title></html>")
    assert hold["primary_xml_obtained_before_hold"] is True
    assert hold["supplement_retrieved"] is False
    for key in (
        "retry_or_alternate_route_performed",
        "paywall_inferred",
        "global_inaccessibility_inferred",
        "negative_biological_evidence",
    ):
        assert hold[key] is False


@pytest.mark.parametrize(
    "field,value",
    [
        ("url", "https://example.org"),
        ("status", 200),
        ("retry_performed", True),
        ("redirects_followed", True),
        ("headers", {}),
    ],
)
def test_hold_requires_exact_challenge_receipt(receipt, field, value):
    receipt[field] = value
    with pytest.raises(ValueError, match="hold changed"):
        audit.project_hold(receipt, b"<html><title>Just a moment...</title></html>")


@pytest.mark.parametrize(
    "body",
    [
        b"<html><title>Article</title></html>",
        b'<html><title>Just a moment...</title><meta name="citation_title"/></html>',
    ],
)
def test_hold_body_not_confused_with_primary(receipt, body):
    with pytest.raises(ValueError, match="challenge"):
        audit.project_hold(receipt, body)


def read_output():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_cache_independent_full_checkpoint():
    result = read_output()
    old = json.loads((ROOT / audit.prior.OUTPUT).read_bytes())
    assert result["scope"] == audit.SCOPE
    assert result["records"] == old["records"] and result["claims"] == old["claims"]
    assert set(result["terms"]) == set(old["terms"]) and len(result["terms"]) == 6
    assert set(result["proteins"]) == set(old["proteins"]) and len(result["proteins"]) == 7
    assert result["inputs"]["prior"] == audit.reference.pin(ROOT, ROOT / audit.prior.OUTPUT)
    for tid, term in result["terms"].items():
        assert term["source_definition_citations"] == []
        assert term["record_memberships"] == old["terms"][tid]["record_memberships"]
        assert term["reference_proteins"] == [
            c["protein_accession"] for c in old["terms"][tid]["reference_candidates"]
        ]
        assert term["reference_citations_adopted_as_primary_support"] is False
        assert term["primary_review_status"] == "OPEN"
    rows = [r for p in result["proteins"].values() for r in p["reference_rows"]]
    assert len(rows) == 11
    assert sum(r["citation_type"] == "submission" for r in rows) == 6
    assert sum(len(r["reference_strain_comments"]) for r in rows) == 22
    assert sum(not r["identifiers"] for r in rows) == 6
    assert len(result["reference_comment_paper_label_matches"]) == 7
    for p in result["proteins"].values():
        assert p["exact_resistant_allele_assignment"] is p["experimental_genome_assignment"] is None
        assert p["experimental_subject_assignment"] is False
    assert result["summary"]["new_verified_resistance_results"] == 0
    assert result["constraints"]["ncbi_requests"] == 0
    assert result["constraints"]["issue_1040"] == "DEFERRED"
    assert result["constraints"]["full_corpus_goal_status"] == "OPEN"
    assert "referencePositions" not in json.dumps(result)


def test_independent_doi_is_not_native_metadata_repair():
    result = read_output()
    links, discrepancies = audit.followup_links(result["proteins"], result["publications"])
    assert links == result["reference_comment_paper_label_matches"]
    assert discrepancies == result["doi_discrepancies"] and len(discrepancies) == 2
    for row in discrepancies:
        assert row["native_doi"] == ".1094/PHYTO-04-18-0128-R"
        assert row["independently_reported_doi"] == "10.1094/phyto-04-18-0128-r"
        assert row["native_or_prior_artifact_corrected"] is False
        assert row["primary_resistance_result_verified"] is False


def test_unreviewed_label_crosswalk_rejected():
    result = read_output()
    result["proteins"]["UniProtKB:A0A1S6LNE2"]["reference_rows"][0]["reference_strain_comments"].append(
        "OTHER"
    )
    with pytest.raises(ValueError, match="isolate label"):
        audit.followup_links(result["proteins"], result["publications"])


def test_repaired_native_doi_rejected():
    result = read_output()
    row = result["proteins"]["UniProtKB:A0A344X8F3"]["reference_rows"][0]
    next(i for i in row["identifiers"] if i["database"] == "DOI")["id"] = "10.1094/phyto-04-18-0128-r"
    with pytest.raises(ValueError, match="malformed DOI"):
        audit.followup_links(result["proteins"], result["publications"])


@pytest.fixture
def reference_entry():
    entry = {
        "primaryAccession": "A0A1S6LNE2",
        "entryAudit": {"entryVersion": 28, "sequenceVersion": 1},
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "organism": {"taxonId": 690259},
        "references": [
            {
                "referenceNumber": 1,
                "citation": {"citationType": "submission", "publicationDate": "2021"},
                "referenceComments": [{"type": "STRAIN", "value": "A"}, {"type": "STRAIN", "value": "B"}],
                "referencePositions": ["SEQUENCE_SENTINEL"],
            }
        ],
    }
    saved = {
        "entry_version": 28,
        "sequence_version": 1,
        "entry_type": entry["entryType"],
        "reference_taxon_id": "NCBITaxon:690259",
        "reference_species_taxon_id": "NCBITaxon:690259",
        "native_protein_flag": None,
    }
    return entry, {"proteins": {"UniProtKB:A0A1S6LNE2": saved}, "terms": {}}


def test_projection_preserves_one_to_many_comments_without_sequence(reference_entry):
    entry, old = reference_entry
    proteins, _ = audit.project_bibliographies({"UniProtKB:A0A1S6LNE2": (entry, {})}, old)
    assert proteins["UniProtKB:A0A1S6LNE2"]["reference_rows"][0]["reference_strain_comments"] == ["A", "B"]
    assert "SEQUENCE_SENTINEL" not in json.dumps(proteins)


@pytest.mark.parametrize(
    "change", ["missing", "extra", "accession", "version", "sequence_version", "type", "taxon", "citations"]
)
def test_projection_requires_complete_native_reference_identity(reference_entry, change):
    entry, old = reference_entry
    entries = {"UniProtKB:A0A1S6LNE2": (entry, {})}
    if change == "missing":
        entries.clear()
    elif change == "extra":
        entries["UniProtKB:OTHER"] = (copy.deepcopy(entry), {})
    elif change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "version":
        entry["entryAudit"]["entryVersion"] += 1
    elif change == "sequence_version":
        entry["entryAudit"]["sequenceVersion"] += 1
    elif change == "type":
        entry["entryType"] = "Other"
    elif change == "taxon":
        entry["organism"]["taxonId"] = 1
    else:
        old["terms"]["ARO:3009279"] = {
            "source_label": "label",
            "record_memberships": [],
            "reference_candidates": [],
            "definition_citation_ids": ["PMID:28201983"],
        }
    with pytest.raises(ValueError):
        audit.project_bibliographies(entries, old)


def test_cli_never_overwrites_or_silently_creates_in_check_mode(monkeypatch, tmp_path):
    target = tmp_path / "output.json"
    monkeypatch.setattr(audit, "OUTPUT", target)
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    monkeypatch.setattr(sys, "argv", ["audit", "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    monkeypatch.setattr(sys, "argv", ["audit"])
    audit.main()
    audit.main()
    target.write_text("changed\n")
    with pytest.raises(ValueError, match="does not reproduce"):
        audit.main()
    assert target.read_text() == "changed\n"


@pytest.fixture
def request_cache(tmp_path, monkeypatch):
    def save(name, value):
        path = tmp_path / name
        path.write_text(json.dumps(value, sort_keys=True) + "\n")
        return audit.reference.pin(tmp_path, path)

    cohort = save("cohort.json", {})
    specs = [
        ("metadata-28201983", "metadata-plan.json", audit.metadata_url("28201983"), 200),
        ("metadata-29996698", "metadata-plan.json", audit.metadata_url("29996698"), 200),
        ("primary-28201983", "primary-plan.json", audit.XML_URL, 200),
        ("article-page", "asset-discovery-plan.json", audit.ARTICLE, 403),
    ]
    for filename in audit.PLAN_SHA:
        plan = {"cohort": cohort, "requests": {k: {"url": u} for k, f, u, _ in specs if f == filename}}
        checksum = save(filename, plan)["sha256"]
        monkeypatch.setitem(audit.PLAN_SHA, filename, checksum)
    for i, (key, filename, url, status) in enumerate(specs):
        body = b"<html><title>Just a moment...</title></html>" if key == "article-page" else key.encode()
        body_path = tmp_path / (key + "-response.bin")
        body_path.write_bytes(body)
        monkeypatch.setitem(audit.BODY_SHA, key, hashlib.sha256(body).hexdigest())
        save(
            key + "-attempt.json",
            {
                "url": url,
                "retry_performed": False,
                "plan_sha256": audit.PLAN_SHA[filename],
                "started_at": f"2026-10-15T05:3{i}:00+00:00",
            },
        )
        save(
            key + "-receipt.json",
            {
                "url": url,
                "status": status,
                "retry_performed": False,
                "redirects_followed": False,
                "sha256": audit.BODY_SHA[key],
                "bytes": len(body),
                "headers": {"Cf-Mitigated": "challenge"},
                "retrieved_at": f"2026-10-15T05:3{i}:10+00:00",
            },
        )
    save(
        "metadata-canary-review.json",
        {
            "body": audit.reference.pin(tmp_path, tmp_path / "metadata-28201983-response.bin"),
            "receipt": audit.reference.pin(tmp_path, tmp_path / "metadata-28201983-receipt.json"),
            "plan": audit.reference.pin(tmp_path, tmp_path / "metadata-plan.json"),
            "manually_inspected": True,
            "publication_identity_verified": True,
            "primary_results_reviewed": False,
            "abstract_is_experimental_allele_assignment": False,
        },
    )
    return tmp_path


def test_all_four_planned_requests_replay_offline(request_cache):
    sources, hold = audit.request_context(request_cache, request_cache)
    assert set(sources) == set(audit.BODY_SHA)
    assert sources["primary-28201983"]["status"] == 200
    assert sources["article-page"]["status"] == 403
    assert hold["primary_xml_obtained_before_hold"] is True


@pytest.mark.parametrize(
    "change",
    [
        "extra",
        "missing",
        "plan",
        "body",
        "url",
        "bytes",
        "retry",
        "redirect",
        "chronology",
        "order",
        "canary",
    ],
)
def test_request_scope_integrity_and_no_retry_guards(request_cache, change):
    root = request_cache
    if change == "extra":
        (root / "extra-attempt.json").write_text("{}")
    elif change == "missing":
        (root / "article-page-response.bin").unlink()
    elif change == "plan":
        (root / "asset-discovery-plan.json").write_text("{}")
    elif change == "body":
        (root / "primary-28201983-response.bin").write_bytes(b"changed")
    else:
        filename = "metadata-canary-review.json" if change == "canary" else "primary-28201983-receipt.json"
        path = root / filename
        row = json.loads(path.read_bytes())
        if change == "url":
            row["url"] = "https://example.org"
        elif change == "bytes":
            row["bytes"] += 1
        elif change == "retry":
            row["retry_performed"] = True
        elif change == "redirect":
            row["redirects_followed"] = True
        elif change == "chronology":
            row["retrieved_at"] = "2026-10-14T00:00:00+00:00"
        elif change == "order":
            row["retrieved_at"] = "2026-10-16T00:00:00+00:00"
        elif change == "canary":
            row["manually_inspected"] = False
        path.write_text(json.dumps(row))
    with pytest.raises(ValueError):
        audit.request_context(root, root)
