"""The public context index retains annotations without assigning experimental identity."""

import hashlib
import json
from collections import Counter
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def context():
    return json.loads((ROOT / "research/2026-10-09-card-citation-context.json").read_bytes())


def test_complete_candidate_coverage_and_snapshot_binding(context):
    path = ROOT / "research/2026-10-07-card-reference-grounding.json"
    audit = json.loads(path.read_bytes())
    assert context["candidate_audit_sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()
    for key in ("corpus_sha256", "protein_snapshot_sha256", "source_inventory_sha256", "attribution"):
        assert context[key] == audit[key]
    candidates = {c["accession"]: c for d in audit["determinants"].values() for c in d["candidates"]}
    assert set(candidates) == set(context["proteins"])
    for accession, candidate in candidates.items():
        protein = context["proteins"][accession]
        assert protein["entry_audit"] == candidate["entry_audit"]
        assert protein["reference_taxon_id"] == candidate["reference_taxon_id"]
        assert protein["primary_review_status"] == "PENDING"
        pmids = {x["id"] for r in protein["reference_contexts"]
                 for x in r["citation"]["citationCrossReferences"] if x["database"] == "PubMed"}
        assert pmids == set(candidate["pubmed_ids"])


def test_annotation_counts_are_not_independent_studies_or_isolates(context):
    proteins = context["proteins"]
    references = [r for p in proteins.values() for r in p["reference_contexts"]]
    assert len(proteins) == context["summary"]["reference_proteins"] == 979
    assert len(references) == context["summary"]["citation_contexts"] == 1686
    assert Counter(r["citation"]["citationType"] for r in references) == context["summary"]["citation_types"]
    assert sum(len(r["strain_annotations"]) for r in references) == 1277
    assert sum(bool(r["strain_annotations"]) for r in references) == 1159
    with_strains = sum(any(r["strain_annotations"] for r in p["reference_contexts"])
                       for p in proteins.values())
    assert with_strains == 810
    assert "not independent experiments or unique isolates" in " ".join(context["limitations"])


def test_qnr_reference_submissions_remain_separate_from_primary_citation(context):
    refs = context["proteins"]["UniProtKB:Q461P1"]["reference_contexts"]
    assert [r["citation"]["id"] for r in refs] == ["16048974", "CI-CQOT5CJ962UUJ", "CI-89A2BM06EPSTH"]
    assert [r["citation"]["citationType"] for r in refs] == ["journal article", "submission", "submission"]
    assert [[s["value"] for s in r["strain_annotations"]] for r in refs] == [["KB1"], ["QC39"], ["TUM17379"]]
    other = context["proteins"]["UniProtKB:A0ACM8Q8E3"]["reference_contexts"]
    assert [[s["value"] for s in r["strain_annotations"]] for r in other] == [["NCTC10738"]]
    assert all(r["citation"]["citationType"] == "submission" for r in other)


def test_ambiguous_links_remain_present_and_out_of_scope_example_stays_out(context):
    for aro, expected in (
        ("ARO:3002709", {"UniProtKB:Q461P1", "UniProtKB:A0ACM8Q8E3"}),
        ("ARO:3002881", {"UniProtKB:A9Y8T8", "UniProtKB:A0A1B1M202"}),
    ):
        assert {acc for acc, p in context["proteins"].items()
                if any(m["aro_id"] == aro for m in p["corpus_memberships"])} == expected
    assert not any(m["aro_id"] == "ARO:3001560" for p in context["proteins"].values()
                   for m in p["corpus_memberships"])


def test_export_has_no_biological_measurement_or_allele_assignments(context):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert context["scope"] == "DATABASE_CITATION_CONTEXT_ONLY_NOT_EXPERIMENTAL_SUBJECT_OR_ALLELE_GROUNDING"
    assert not set(keys(context)) & {
        "sequence", "features", "variants", "alteration", "resistance_mechanisms", "title",
        "activity_spectrum", "mic", "measurement_value", "protocol", "primers", "referencePositions",
        "strain_taxon_id", "assembly_accession", "biosample_accession",
    }
    assert all(s["type"] == "STRAIN" for p in context["proteins"].values()
               for r in p["reference_contexts"] for s in r["strain_annotations"])
