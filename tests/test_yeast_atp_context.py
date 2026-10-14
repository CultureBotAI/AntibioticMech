"""Reference subunits and conditional comparisons cannot become allele assignments."""

import copy
import csv
import hashlib
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_yeast_atp_context as audit  # noqa: E402


def source(gene):
    accession, locus, sgd, subunit = audit.GENES[gene]
    taxonomy = {"taxonId": 559292, "rank": "strain", "active": True,
                "scientificName": "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)",
                "lineage": [{"rank": "species", "taxonId": 4932,
                             "scientificName": "Saccharomyces cerevisiae"}]}
    entry = {"primaryAccession": accession, "entryType": "UniProtKB reviewed (Swiss-Prot)",
             "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
             "organism": {"taxonId": 559292, "scientificName": taxonomy["scientificName"]},
             "genes": [{"geneName": {"value": gene}, "orderedLocusNames": [{"value": locus}]}],
             "proteinDescription": {"recommendedName": {"fullName": {
                 "value": f"ATP synthase subunit {subunit}, mitochondrial"}}},
             "uniProtKBCrossReferences": [{"database": "SGD", "id": sgd,
                 "properties": [{"key": "GeneName", "value": gene}]}]}
    return entry, taxonomy


@pytest.mark.parametrize("gene", audit.GENES)
@pytest.mark.parametrize("change", ["none", "accession", "gene", "locus", "sgd", "sgd_gene",
                                   "subunit", "sequence", "features", "reviewed", "taxon",
                                   "species", "rank", "inactive", "version", "duplicate_gene"])
def test_reference_subunit_scope(gene, change):
    entry, tax = source(gene)
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "OTHER"
    elif change == "locus":
        entry["genes"][0]["orderedLocusNames"][0]["value"] = "OTHER"
    elif change == "sgd":
        entry["uniProtKBCrossReferences"][0]["id"] = "OTHER"
    elif change == "sgd_gene":
        entry["uniProtKBCrossReferences"][0]["properties"][0]["value"] = "OTHER"
    elif change == "subunit":
        entry["proteinDescription"]["recommendedName"]["fullName"]["value"] = "OTHER"
    elif change in ("sequence", "features"):
        entry[change] = "must not be exported"
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change == "taxon":
        entry["organism"]["taxonId"] = 4932
    elif change == "species":
        tax["lineage"][0]["taxonId"] = 999
    elif change == "rank":
        tax["rank"] = "no rank"
    elif change == "inactive":
        tax["active"] = False
    elif change == "version":
        entry["entryAudit"]["entryVersion"] = True
    elif change == "duplicate_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_protein(entry, gene, tax)
        return
    result = audit.project_protein(entry, gene, tax)
    assert result["reference_taxon_id"] == "NCBITaxon:559292"
    assert result["source_species_taxon_id"] == "NCBITaxon:4932"
    assert not result["exact_resistance_allele"] and not result["experimental_subject_assignment"]
    assert not result["independent_primary_in_bibliography"]


@pytest.mark.parametrize("change", ["none", "doi", "pmid", "pmcid", "license", "background",
                                   "project", "missing_section", "duplicate_section"])
def test_primary_identity_and_subject_locations(change):
    fields = {"doi": audit.DOI, "pmid": audit.PMID, "pmcid": "PMC9635649",
              "license": "https://creativecommons.org/licenses/by/4.0/",
              "background": "Saccharomyces cerevisiae BY4741 BY4742", "project": "PRJNA742704"}
    if change in fields:
        fields[change] = "OTHER"
    sections = "".join(f'<sec id="{identifier}"><p>Source context</p></sec>'
                       for identifier in ("sec27", "sec29", "sec35"))
    if change == "missing_section":
        sections = sections.replace('id="sec27"', 'id="OTHER"')
    elif change == "duplicate_section":
        sections += '<sec id="sec27"><p>Duplicate</p></sec>'
    payload = (f'<article><front><article-meta><article-id pub-id-type="doi">{fields["doi"]}</article-id>'
               f'<article-id pub-id-type="pmid">{fields["pmid"]}</article-id>'
               f'<article-id pub-id-type="pmcid">{fields["pmcid"]}</article-id>'
               f'<permissions>{fields["license"]}</permissions></article-meta></front><body>'
               f'<sec id="sec3"><p>{fields["background"]}</p></sec>{sections}'
               f'<sec id="sec40"><p>{fields["project"]}</p></sec>'
               '<fig id="jkac246-F5"><caption>Source caption</caption></fig></body></article>').encode()
    if change != "none":
        with pytest.raises(ValueError):
            audit.primary_context(payload)
        return
    result = audit.primary_context(payload)
    assert not result["reference_strain_is_exact_tested_derivative"]
    assert not result["study_accession_is_genome_assignment"]
    assert not result["experimental_protein_allele_or_genome_assignment"]


@pytest.mark.parametrize("change", ["none", "attempt", "url", "status", "retry", "hash", "bytes"])
def test_request_bindings_and_no_public_signed_query(tmp_path, change):
    url = "https://example.org/figure.jpeg?Signature=PRIVATE_LINK_PARAMETER"
    payload = b"synthetic asset"
    attempt = {"url": url}
    receipt = {"url": url, "status": 200, "retry_performed": False, "bytes": len(payload),
               "sha256": hashlib.sha256(payload).hexdigest(), "retrieved_at": "synthetic"}
    if change == "attempt":
        attempt["url"] = "OTHER"
    elif change == "url":
        receipt["url"] = "OTHER"
    elif change == "status":
        receipt["status"] = 403
    elif change == "retry":
        receipt["retry_performed"] = True
    elif change == "hash":
        receipt["sha256"] = "0" * 64
    elif change == "bytes":
        receipt["bytes"] += 1
    (tmp_path / "figure-attempt.json").write_text(json.dumps(attempt))
    (tmp_path / "figure-receipt.json").write_text(json.dumps(receipt))
    (tmp_path / "figure-response.bin").write_bytes(payload)
    if change != "none":
        with pytest.raises(ValueError):
            audit.request(tmp_path, tmp_path, "figure", url)
        return
    result = audit.request(tmp_path, tmp_path, "figure", url)
    assert "PRIVATE_LINK_PARAMETER" not in json.dumps(result)


def test_historical_dossier_scope_without_live_record_freeze():
    dossier = json.loads((ROOT / audit.OUTPUT).read_bytes())
    census = audit.reference.check_pin(ROOT, dossier["inputs"]["census"])
    rows = {r["identifier"]: r for r in csv.DictReader(census.read_text().splitlines(), delimiter="\t")}
    assert len(rows) == 2939 and len(dossier["records"]) == 10
    for record in dossier["records"]:
        assert record["record_sha256"] == rows[record["identifier"]]["record_sha256"]
    assert len(dossier["database_citation"]["terms"]) == 19
    assert {p["reference_taxon_id"] for p in dossier["reference_proteins"].values()} == {"NCBITaxon:559292"}
    primary = dossier["independent_primary"]
    assert not primary["ATP1"]["independent_allele_effect_established_here"]
    assert not primary["ATP2"]["single_mutant_growth_benefit_in_reported_comparison"]
    assert not primary["figure_5_hypothesis_edges_are_verified_causal_edges"]
    assert not primary["fungamr_row_to_independent_paper_crosswalk_verified"]
    assert dossier["summary"]["biological_records_changed"] == 0
    assert dossier["summary"]["full_corpus_goal_status"] == "OPEN"
    assert dossier["constraints"]["ncbi_requests"] == dossier["constraints"]["github_mutations"] == 0
