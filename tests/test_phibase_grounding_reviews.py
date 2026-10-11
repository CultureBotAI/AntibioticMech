"""Reviewed reference identifiers must not become experimental isolate identity."""

import copy
import csv
import json
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import phibase_grounding_reviews as review  # noqa: E402
import seed_from_sources as seed  # noqa: E402

INVENTORY = ROOT / "data/raw/phibase_amr.tsv"
CURRENT_REVIEWED = 185
FUMIGATUS_REFERENCES = {
    "12543662": "DOI:10.1128/aac.47.2.577-581.2003",
    "12709346": "DOI:10.1128/aac.47.5.1719-1726.2003",
    "15215142": "DOI:10.1128/aac.48.7.2747-2750.2004",
    "17371828": "DOI:10.1128/aac.01092-06",
    "23226235": "DOI:10.1371/journal.pone.0050034",
}
FOLLOWUP_REFERENCES = {
    "27799210": "DOI:10.1128/aac.02101-16",
    "15504870": "DOI:10.1128/aac.48.11.4405-4413.2004",
    "12604551": "DOI:10.1128/aac.47.3.1120-1124.2003",
    "16801438": "DOI:10.1128/aac.00187-06",
    "15215099": "DOI:10.1128/aac.48.7.2490-2496.2004",
    "39464835": "DOI:10.2147/idr.s483623",
}
PRIMARY_CONTEXT_REFERENCES = {
    "10919801": "DOI:10.1128/aem.66.8.3421-3426.2000",
    "16048935": "DOI:10.1128/aac.49.8.3264-3273.2005",
    "22155829": "DOI:10.1128/aac.05502-11",
    "25441450": "DOI:10.1111/mpp.12222",
}
OA_CONTEXT_REFERENCES = {
    "26596626": "DOI:10.1038/srep16881",
    "30044782": "DOI:10.1371/journal.pgen.1007546",
    "40934067": "DOI:10.1080/21505594.2025.2555419",
    "41277790": "DOI:10.1111/mpp.70174",
    "41745253": "DOI:10.3390/jof12020111",
    "42112916": "DOI:10.1128/spectrum.02761-25",
}
REN_SUBJECTS = {"Bt6-4": "Bt6-4R1", "Bt3-4": "Bt3-4R", "Yc-6": "Yc-6R1", "Nj5-10": "Nj5-10R"}


@pytest.fixture
def inputs(tmp_path):
    inventory = tmp_path / "phibase_amr.tsv"
    inventory.write_bytes(INVENTORY.read_bytes())
    path = tmp_path / "reviews.json"
    path.write_bytes(review.DEFAULT_REVIEW.read_bytes())
    with inventory.open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    return inventory, rows, path


def decision_for(document, pmid):
    return next(d for d in document["reviews"] if d["pmid"] == pmid)


def test_reviews_have_expected_unique_source_rows(inputs):
    inventory, rows, path = inputs
    decisions = review.load_reviews(inventory, rows, path)
    matched = [r for r in rows if review.row_digest(r) in decisions]
    assert len(matched) == CURRENT_REVIEWED
    posteraro, = [r for r in matched if r["pmid"] == "12519188"]
    assert posteraro["identifier"] == "CHEBI:46081" and posteraro["strain_label"] == "BYP22"
    assert decisions[review.row_digest(posteraro)]["subject_strain"] == "BPY22.17"
    assert decisions[review.row_digest(posteraro)]["withhold"] == ["taxon_id", "protein_accession"]
    darlington = [r for r in matched if r["pmid"] == "11036010"]
    assert len(darlington) == 1 and darlington[0]["identifier"] == "CHEBI:46081"
    assert decisions[review.row_digest(darlington[0])]["subject_strain"] == "transformant 12"
    ren = [r for r in matched if r["pmid"] == "30686204"]
    assert len(ren) == 8
    assert {r["identifier"] for r in ren} == {"CHEBI:28909", "CHEBI:81763"}
    assert all(decisions[review.row_digest(r)]["subject_strain"] == REN_SUBJECTS[r["strain_label"]]
               for r in ren)
    oa = [r for r in matched if r["pmid"] in OA_CONTEXT_REFERENCES]
    assert len(oa) == 6
    assert {r["protein_accession"] for r in oa} == {
        "P53373", "I1S9X9", "W7MZ22", "I1RPK0", "A0A8E5ME34", "G2XFG4",
    }
    primary = [r for r in matched if r["pmid"] in PRIMARY_CONTEXT_REFERENCES]
    assert len(primary) == 9
    assert {r["protein_accession"] for r in primary} == {"Q9P340", "Q870D1", "A7EGE3", "A0A1D8PCT0"}
    assert all("subject_strain" not in decisions[review.row_digest(r)] for r in primary)
    followup = [r for r in matched if r["pmid"] in FOLLOWUP_REFERENCES]
    assert len(followup) == 12
    assert {r["protein_accession"] for r in followup} == {
        "Q4WNT5", "B0XYD8", "B0Y628", "E9R5G2", "Q5ALV2", "Q59X67",
    }
    assert all("subject_strain" not in decisions[review.row_digest(r)] for r in followup)
    li = [r for r in matched if r["pmid"] == "8641470"]
    assert len(li) == 1 and li[0]["identifier"] == "CHEBI:3392"
    assert decisions[review.row_digest(li[0])]["subject_strain"] == "WL167Y"
    fumigatus = [r for r in matched if r["pmid"] in FUMIGATUS_REFERENCES]
    assert len(fumigatus) == 17
    assert {r["identifier"] for r in fumigatus} == {"CHEBI:6076", "CHEBI:64355", "CHEBI:10023"}
    assert {r["protein_accession"] for r in fumigatus} == {"Q4WNT5", "Q4WDM9"}
    assert {r["strain_taxon_id"] for r in fumigatus} == {"330879"}
    assert all("subject_strain" not in decisions[review.row_digest(r)] for r in fumigatus)
    fillinger = [r for r in matched if r["pmid"] == "22912706"]
    assert len(fillinger) == 8
    assert {r["identifier"] for r in fillinger} == {"CHEBI:28909"}
    assert {r["protein_accession"] for r in fillinger} == {"A0A384J5Y1"}
    assert all("subject_strain" not in decisions[review.row_digest(r)] for r in fillinger)
    xia = [r for r in matched if r["pmid"] == "41649761"]
    assert len(xia) == 3
    assert {r["identifier"] for r in xia} == {"CHEBI:81763"}
    assert {r["strain_label"] for r in xia} == {"Unknown strain"}
    assert {r["protein_accession"]: decisions[review.row_digest(r)]["subject_strain"]
            for r in xia} == {"W7LTW3": "\u0394FvPbs2", "W7LX41": "\u0394FvSsk2",
                              "W7M468": "\u0394FvHog1"}
    followup = [r for r in matched if r["pmid"] in {"26092798", "27558019"}]
    assert len(followup) == 2
    assert {r["identifier"] for r in followup} == {"CHEBI:3405"}
    assert {r["protein_accession"] for r in followup} == {"O42772", "G4NE45"}
    assert all("subject_strain" not in decisions[review.row_digest(r)] for r in followup)
    carboxin = [r for r in matched if r["pmid"] in {"21933337", "22536383"}]
    assert len(carboxin) == 26
    assert {r["identifier"] for r in carboxin} == {"CHEBI:3405"}
    assert {r["protein_accession"] for r in carboxin} == {"O42772", "F9X9V6", "F9XH52"}
    assert sum(r["pmid"] == "21933337" for r in carboxin) == 19
    assert sum(bool(r["strain_taxon_id"]) for r in carboxin) == 9
    assert all("subject_strain" not in decisions[review.row_digest(r)] for r in carboxin)
    rybak = [r for r in matched if r["pmid"] == "28630186"]
    assert len(rybak) == 6
    assert {r["identifier"] for r in rybak} == {"CHEBI:10023", "CHEBI:46081", "CHEBI:6076"}
    assert {r["protein_accession"] for r in rybak} == {"Q59VG6", "G8B7T4"}
    assert {r["modification"] for r in rybak} == {"ERG3delta (deletion)"}
    assert all("subject_strain" not in decisions[review.row_digest(r)] for r in rybak)
    eddouzi = [r for r in matched if r["pmid"] == "23629718"]
    assert len(eddouzi) == 6
    assert {r["identifier"] for r in eddouzi} == {"CHEBI:10023", "CHEBI:46081", "CHEBI:48080"}
    assert all("subject_strain" not in decisions[review.row_digest(r)] for r in eddouzi)
    js67 = [r for r in matched if r["pmid"] == "32569396"]
    assert len(js67) == 3
    assert {r["identifier"] for r in js67} == {"CHEBI:81760", "CHEBI:8434", "CHEBI:8489"}
    assert {r["strain_label"] for r in js67} == {"JS67"}
    flavus = [r for r in matched if r["pmid"] == "18775650"]
    assert len(flavus) == 5
    assert {r["identifier"] for r in flavus} == {"CHEBI:10023"}
    assert {r["strain_label"] for r in flavus} == {"X26728"}
    assert {r["protein_accession"] for r in flavus} == {"B8N2C8", "B8NFL5"}
    assert {r["strain_taxon_id"] for r in flavus} == {"332952"}
    sts1 = [r for r in matched if r["pmid"] == "8307980"]
    assert len(sts1) == 1
    assert sts1[0]["identifier"] == "CHEBI:27641"
    assert sts1[0]["gene_id"] == "YIR011C_mRNA"
    assert sts1[0]["protein_accession"] == "P38637"
    liu = [r for r in matched if r["pmid"] == "22314539"]
    assert len(liu) == 3
    assert {r["strain_label"] for r in liu} == {"NRRL 3357"}
    assert {decisions[review.row_digest(r)]["subject_strain"] for r in liu} == {
        "AF-A", "AF-B", "AflavC-788",
    }
    balashov = [r for r in matched if r["pmid"] == "16723566"]
    assert len(balashov) == 24
    assert {r["identifier"] for r in balashov} == {"CHEBI:474180", "CHEBI:55346", "CHEBI:600520"}
    assert {r["protein_accession"] for r in balashov} == {"A0A1D8PCT0"}
    assert {r["strain_taxon_id"] for r in balashov} == {"237561"}
    assert {r["strain_label"] for r in balashov} == {"M70", "SC5314"}
    assert all("subject_strain" not in decisions[review.row_digest(r)] for r in balashov)
    flowers = [r for r in matched if r["pmid"] == "25385095"]
    assert len(flowers) == 21
    assert {r["identifier"] for r in flowers} == {"CHEBI:10023", "CHEBI:46081", "CHEBI:6076"}
    assert {r["gene_id"] for r in flowers} == {"C5_00660C_A-T"}
    assert all("subject_strain" not in decisions[review.row_digest(r)] for r in flowers)
    garcia = [r for r in matched if r["pmid"] == "18443110"]
    assert len(garcia) == 3
    assert {r["strain_label"] for r in garcia} == {"BY4742"}
    assert {decisions[review.row_digest(r)]["subject_strain"] for r in garcia} == {"BY4742-P649A"}


@pytest.mark.parametrize("change", [
    "inventory", "schema", "extra_root", "row_hash", "duplicate_row", "wrong_identifier",
    "wrong_pmid", "unsupported_field", "empty_note", "duplicate_review", "empty_locations",
    "extra_decision", "empty_rows",
])
def test_drift_or_invalid_reviews_fail_closed(inputs, change):
    inventory, rows, path = inputs
    document = json.loads(path.read_bytes())
    item = document["reviews"][0]
    if change == "inventory":
        inventory.write_bytes(inventory.read_bytes() + b"\n")
    elif change == "schema":
        document["schema_version"] = True
    elif change == "extra_root":
        document["ignore_errors"] = True
    elif change == "row_hash":
        item["source_rows"][0]["row_sha256"] = "0" * 64
    elif change == "duplicate_row":
        item["source_rows"].append(item["source_rows"][0])
    elif change == "wrong_identifier":
        item["source_rows"][0]["identifier"] = "CHEBI:1"
    elif change == "wrong_pmid":
        item["pmid"] = "1"
    elif change == "unsupported_field":
        item["withhold"] = ["alteration"]
    elif change == "empty_note":
        item["note"] = " "
    elif change == "duplicate_review":
        document["reviews"].append(copy.deepcopy(item))
    elif change == "empty_locations":
        item["locations"] = []
    elif change == "extra_decision":
        item["replace"] = {"taxon_id": "1"}
    else:
        item["source_rows"] = []
    path.write_text(json.dumps(document))
    with pytest.raises(ValueError):
        review.load_reviews(inventory, rows, path)


def test_source_rows_cannot_change_after_inventory_read(inputs):
    inventory, rows, path = inputs
    rows[0]["pmid"] = "1"
    with pytest.raises(ValueError, match="rows changed"):
        review.load_reviews(inventory, rows, path)


@pytest.mark.parametrize("values", [
    [], "gene_id", [None], ["gene_id", "gene_id"], ["taxon_id"],
    ["strain_taxon_id"], ["alteration"], ["protein_accession"],
])
def test_misassigned_identifier_decisions_are_explicit_and_bounded(inputs, values):
    inventory, rows, path = inputs
    document = json.loads(path.read_bytes())
    decision_for(document, "8307980")["misassigned"] = values
    path.write_text(json.dumps(document))
    with pytest.raises(ValueError, match="misassigned identifier"):
        review.load_reviews(inventory, rows, path)


def test_gene_withholding_cannot_be_implicitly_reference_only(inputs):
    inventory, rows, path = inputs
    document = json.loads(path.read_bytes())
    del decision_for(document, "8307980")["misassigned"]
    path.write_text(json.dumps(document))
    with pytest.raises(ValueError, match="misassigned identifier"):
        review.load_reviews(inventory, rows, path)


def test_misassigned_identifier_must_be_withheld(inputs):
    inventory, rows, path = inputs
    document = json.loads(path.read_bytes())
    decision_for(document, "8307980")["withhold"].remove("gene_id")
    path.write_text(json.dumps(document))
    with pytest.raises(ValueError, match="misassigned identifier"):
        review.load_reviews(inventory, rows, path)


def test_seeding_preserves_claims_and_unreviewed_identifiers(inputs):
    inventory, rows, path = inputs
    before = {r["identifier"]: {
        "identifier": r["identifier"],
        "chemical_structure": {"standard_inchi_key": r["standard_inchi_key"]},
        "curation_history": [],
    } for r in rows}
    after = copy.deepcopy(before)
    baseline = seed.attach_phibase_resistance(before, grounding_review=None)
    current = seed.attach_phibase_resistance(after, grounding_review=path)
    assert baseline["matched_associations"] == current["matched_associations"] == 217
    assert current["reviewed_identifier_context"] == CURRENT_REVIEWED
    changed = []
    for identifier in before:
        for old, new in zip(before[identifier]["resistance_mechanisms"],
                            after[identifier]["resistance_mechanisms"], strict=True):
            if old == new:
                continue
            changed.append(identifier)
            withheld = {"strain_taxon_id", "protein_accession"}
            if (old["evidence"][0]["reference"] in {
                    "PMID:10919801", "PMID:22155829", "PMID:26596626", "PMID:41745253",
                    "PMID:27644008", "PMID:34490974"}
                    or (identifier == "CHEBI:3405" and old["protein_accession"] == "UniProtKB:O42772")):
                withheld = {"protein_accession"}
            elif old["evidence"][0]["reference"] == "PMID:23629718":
                withheld = {"protein_accession"}
                if old["protein_accession"] == "UniProtKB:Q5A4G2":
                    withheld.add("strain_taxon_id")
            elif identifier == "CHEBI:27641":
                withheld.add("gene_id")
            elif old["evidence"][0]["reference"] == "PMID:32569396":
                withheld.add("taxon_id")
            elif (old["evidence"][0]["reference"] == "PMID:12519188"
                  or (old["evidence"][0]["reference"] == "PMID:30732567" and old["strain"] == "HC30")):
                withheld = {"taxon_id", "protein_accession"}
            subject_changed = {"strain"} if new.get("strain") != old["strain"] else set()
            species_changed = {"taxon_label"} if new["taxon_label"] != old["taxon_label"] else set()
            assert {k for k in old if old.get(k) != new.get(k)} == {
                *withheld, *subject_changed, *species_changed, "note", "evidence",
            }
            for field in withheld:
                if not (species_changed and field == "taxon_id"):
                    assert field not in new
                assert old[field] in new["note"]
            pmid = old["evidence"][0]["reference"].removeprefix("PMID:")
            if pmid == "12519188":
                assert old["strain"] == "BYP22" and new["strain"] == "BPY22.17"
                assert new["taxon_label"] == old["taxon_label"] == "Cryptococcus neoformans"
                assert new["alteration"] == old["alteration"]
                assert not {"taxon_id", "protein_accession", "strain_taxon_id", "gene_id"} & new.keys()
                assert "Original source background label: BYP22." in new["note"]
                assert "modern species crosswalk is unresolved" in new["note"]
                reference = "DOI:10.1046/j.1365-2958.2003.03281.x"
            elif pmid == "34490974":
                assert "strain" not in new and "strain_taxon_id" not in new
                assert old["strain"] in {"IPO323", "37-16"}
                assert f"Original source background label: {old['strain']}." in new["note"]
                assert "ST1/MBC" in new["note"] and "No representative derivative is selected" in new["note"]
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:1047171"
                assert new["alteration"] == old["alteration"]
                reference = "DOI:10.1111/1462-2920.15760"
            elif pmid == "30732567":
                assert new["strain"] == old["strain"] + "M"
                assert new["alteration"] == old["alteration"]
                assert "gene_id" not in new and "strain_taxon_id" not in new
                assert new["taxon_id"] == (
                    "NCBITaxon:948311" if old["strain"] == "HC30" else "NCBITaxon:117187"
                )
                assert new["taxon_label"] == (
                    "Fusarium proliferatum" if old["strain"] == "HC30" else "Fusarium verticillioides"
                )
                reference = "DOI:10.1186/s12864-019-5479-6"
            elif pmid == "21138346":
                assert old["strain"] == "PH-1" and new["strain"] == "YM1"
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:5518"
                assert "gene_id" not in new and "strain_taxon_id" not in new
                assert new["alteration"] == old["alteration"]
                assert subject_changed == {"strain"}
                assert "Original source background label: PH-1." in new["note"]
                assert "not asserted equivalent" in new["note"]
                reference = "DOI:10.1094/MPMI-10-10-0233"
            elif pmid == "39403939":
                assert new["strain"] == old["strain"] == "SC5314"
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:5476"
                assert "gene_id" not in new and "strain_taxon_id" not in new
                assert (
                    "aliases of SDH8 reference locus C2_02620W_A, primary CGDID CAL0000192813" in new["note"]
                )
                assert "not an experimental allele" in new["note"]
                reference = "DOI:10.1080/21505594.2024.2405000"
            elif pmid == "17073308":
                assert new["strain"] == old["strain"] == "IPO323"
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:1047171"
                assert new["gene_id"] == old["gene_id"] == "Mycgr3T76502"
                assert "grouped set of three derivatives" in new["note"]
                assert "Not assayed flag remains unchanged" in new["note"]
                reference = "DOI:10.1094/mpmi-19-1262"
            elif pmid == "18992352":
                assert new["strain"] == old["strain"] == "RIB40" and not subject_changed
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:5062"
                assert new["alteration"] == old["alteration"]
                assert "gene_id" not in new and "strain_taxon_id" not in new
                assert "parent background" in new["note"]
                assert "2009 full text remains unavailable" in new["note"]
                reference = "DOI:10.1271/bbb.100687"
            elif pmid == "27644008":
                assert new["strain"] == old["strain"] == "DK05" and not subject_changed
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:112498"
                assert new["alteration"] == old["alteration"]
                assert "gene_id" not in new and "strain_taxon_id" not in new
                assert "parent background" in new["note"]
                reference = "DOI:10.1002/ps.4442"
            elif pmid == "30497711":
                assert new["strain"] == old["strain"] and new["strain"] in {"2021", "BM50", "BM6"}
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:5518"
                assert new["gene_id"] == old["gene_id"] == "FGRAMPH1_01T14465"
                assert new["alteration"] == old["alteration"]
                assert "parental backgrounds" in new["note"] and not subject_changed
                reference = "DOI:10.1016/j.pestbp.2018.08.011"
            elif pmid == "11600353":
                assert old["strain"] == new["strain"] == "ATCC 2001"
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:5478"
                assert new["gene_id"] == old["gene_id"] == "CAGL0E04334g-T"
                assert new["alteration"] == old["alteration"]
                assert "background/comparator label" in new["note"] and not subject_changed
                reference = "DOI:10.1128/aac.45.11.3037-3045.2001"
            elif pmid == "11036010":
                assert old["strain"] == "CAI4" and new["strain"] == "transformant 12"
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:5476"
                assert new["gene_id"] == old["gene_id"] == "C5_00660C_A-T"
                assert new["alteration"] == old["alteration"] and "[Not assayed]" in new["alteration"]
                assert "Original source background label: CAI4." in new["note"]
                reference = "DOI:10.1128/aac.44.11.2985-2990.2000"
            elif pmid == "30686204":
                assert new["strain"] == REN_SUBJECTS[old["strain"]]
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:40559"
                assert "gene_id" not in new and subject_changed == {"strain"}
                assert "Original source background label: " + old["strain"] in new["note"]
                assert "Association is not causation" in new["note"]
                reference = "DOI:10.1094/pdis-11-15-1290-re"
            elif pmid in OA_CONTEXT_REFERENCES:
                assert new["strain"] == old["strain"] and new["taxon_id"] == old["taxon_id"]
                assert new.get("gene_id") == old.get("gene_id") and not subject_changed
                reference = OA_CONTEXT_REFERENCES[pmid]
            elif pmid in PRIMARY_CONTEXT_REFERENCES:
                assert new["strain"] == old["strain"] and new["taxon_id"] == old["taxon_id"]
                assert "gene_id" not in new and not subject_changed
                reference = PRIMARY_CONTEXT_REFERENCES[pmid]
            elif pmid in FOLLOWUP_REFERENCES:
                assert new["strain"] == old["strain"] and not subject_changed
                assert new["taxon_id"] == old["taxon_id"]
                assert new.get("gene_id") == old.get("gene_id")
                assert "parent background" in new["note"] and "reference" in new["note"]
                assert "remain unresolved" in new["note"]
                reference = FOLLOWUP_REFERENCES[pmid]
            elif pmid == "8641470":
                assert new["strain"] == "WL167Y" and old["strain"] == "W303-1A"
                assert subject_changed == {"strain"}
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:4932"
                assert new["gene_id"] == old["gene_id"] == "YFL037W_mRNA"
                assert "does not resolve a unique clone" in new["note"]
                assert "IC50, not MIC" in new["note"]
                assert "Original source background label: W303-1A." in new["note"]
                reference = "DOI:10.1016/0014-5793(96)00334-1"
            elif pmid in FUMIGATUS_REFERENCES:
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:746128"
                assert new["strain"] == old["strain"] and not subject_changed
                assert new.get("gene_id") == old.get("gene_id")
                assert new["alteration"] == old["alteration"]
                assert "parent background" in new["note"] and "Af293 reference" in new["note"]
                assert "remain unresolved" in new["note"]
                reference = FUMIGATUS_REFERENCES[pmid]
            elif identifier == "CHEBI:3405":
                assert new["strain"] == old["strain"]
                assert new["taxon_id"] == old["taxon_id"]
                assert new["taxon_id"] in {"NCBITaxon:1047171", "NCBITaxon:318829"}
                assert new["alteration"] == old["alteration"]
                assert "gene_id" not in new and not subject_changed
                assert "parent background" in new["note"]
                reference = {"PMID:21933337": "DOI:10.1111/j.1364-3703.2011.00746.x",
                             "PMID:22536383": "DOI:10.1371/journal.pone.0035429",
                             "PMID:26092798": "DOI:10.1016/j.fgb.2015.03.018",
                             "PMID:27558019": "DOI:10.1186/s13568-016-0232-x"}[
                                 old["evidence"][0]["reference"]]
            elif identifier == "CHEBI:28909":
                assert old["evidence"][0]["reference"] == "PMID:22912706"
                assert new["strain"] == old["strain"] == "B05.10"
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:40559"
                assert "parent background" in new["note"]
                assert "not subject accessions" in new["note"]
                reference = "DOI:10.1371/journal.pone.0042520"
            elif identifier == "CHEBI:81763":
                assert old["evidence"][0]["reference"] == "PMID:41649761"
                assert old["strain"] == "Unknown strain" and subject_changed == {"strain"}
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:117187"
                assert "not the tested derivative" in new["note"]
                assert "Original source background label: Unknown strain." in new["note"]
                reference = "DOI:10.1007/s44297-025-00052-5"
            elif old["evidence"][0]["reference"] == "PMID:28630186":
                assert new["strain"] == old["strain"]
                assert new["taxon_id"] == old["taxon_id"]
                assert new.get("gene_id") == old.get("gene_id")
                assert new["alteration"] == old["alteration"] == "ERG3delta (deletion)"
                assert "Grounding review rybak-2017-" in new["note"]
                reference = "DOI:10.1128/aac.00651-17"
            elif old["evidence"][0]["reference"] == "PMID:23629718":
                assert new["strain"] == old["strain"]
                assert new["taxon_id"] == old["taxon_id"]
                assert new.get("gene_id") == old.get("gene_id")
                assert new["alteration"] == old["alteration"]
                assert "Grounding review eddouzi-2013-" in new["note"]
                reference = "DOI:10.1128/aac.00555-13"
            elif old["evidence"][0]["reference"] == "PMID:25385095":
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:5476"
                assert new["strain"] == old["strain"] == "SC5314"
                assert new["gene_id"] == old["gene_id"] == "C5_00660C_A-T"
                assert "not either tested replicate or a clinical donor" in new["note"]
                assert "reference ERG11 locus" in new["note"]
                reference = "DOI:10.1128/aac.03470-14"
            elif old["evidence"][0]["reference"] == "PMID:18443110":
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:4932"
                assert old["strain"] == "BY4742" and new["strain"] == "BY4742-P649A"
                assert new["gene_id"] == old["gene_id"] == "YLR342W_mRNA"
                assert new["alteration"] == old["alteration"]
                assert "discrepancy is preserved, not normalized" in new["note"]
                assert "AAC48981.1" in new["note"]
                reference = "DOI:10.1128/aac.00262-08"
            elif identifier == "CHEBI:10023" and subject_changed:
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:5059"
                assert new["strain"] in {"AF-A", "AF-B", "AflavC-788"}
                assert old["strain"] == "NRRL 3357"
                assert "Original source background label: NRRL 3357." in new["note"]
                assert "not clinical isolate BMU29791" in new["note"]
                assert new["gene_id"] == old["gene_id"]
                assert new["alteration"] == old["alteration"]
                reference = "DOI:10.1128/aac.05477-11"
            elif identifier == "CHEBI:10023":
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:5059"
                assert new["taxon_label"] == "Aspergillus flavus"
                assert new["strain"] == "X26728"
                assert "susceptible parent" in new["note"]
                assert "source coordinates remain unnormalized" in new["note"]
                reference = "DOI:10.1016/j.ijantimicag.2008.06.018"
            elif identifier == "CHEBI:27641":
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:4932"
                assert new["taxon_label"] == "Saccharomyces cerevisiae"
                assert new["strain"] == "YPH501"
                assert new["alteration"] == "STS1+ (wild type) [Overexpression]"
                assert "Historical STS1 denotes PDR5" in new["note"]
                assert "UniProtKB:P33302 / YOR153W" in new["note"]
                reference = "DOI:10.1016/S0021-9258(17)41760-1"
                reference_only, rejected = new["note"].split(
                    "Reference-only source identifiers: ", 1
                )[1].split(" Rejected misassigned source identifiers: ", 1)
                assert reference_only == "strain_taxon_id=NCBITaxon:559292."
                assert rejected == "protein_accession=UniProtKB:P38637; gene_id=YIR011C_mRNA."
            elif identifier in {"CHEBI:474180", "CHEBI:55346", "CHEBI:600520"}:
                assert new["taxon_id"] == old["taxon_id"] == "NCBITaxon:5476"
                assert new["strain"] == old["strain"]
                assert "parent background" in new["note"]
                assert "AF027295 / AAC49870.1" in new["note"]
                assert "UniProtKB:O13383" in new["note"]
                assert "not an experimental allele" in new["note"]
                assert "gene_id" not in new and not subject_changed
                reference = "DOI:10.1128/aac.01653-05"
            else:
                assert new["taxon_label"] == "Colletotrichum gloeosporioides"
                assert new["strain"] == "JS67"
                reference = "DOI:10.1002/ps.5964"
            assert new["mechanism_type"] == "UNKNOWN"
            assert new["evidence"][:-1] == old["evidence"]
            assert new["evidence"][-1]["reference"] == reference
    assert sorted(changed) == sorted(
        ["CHEBI:10023"] * 18 + ["CHEBI:46081"] * 30 + ["CHEBI:6076"] * 19 + ["CHEBI:48080"]
        + ["CHEBI:81784"] * 2 + ["CHEBI:81972"] * 2 + ["CHEBI:474180"] * 2
        + ["CHEBI:9448"] * 3
        + ["CHEBI:64355"] * 5 + ["CHEBI:3392"] * 4
        + ["CHEBI:16240"] * 3 + ["CHEBI:40909"] * 3 + ["CHEBI:136340"] * 2
        + ["CHEBI:3405"] * 34
        + ["CHEBI:28909"] * 13 + ["CHEBI:81763"] * 8
        + ["CHEBI:27641", "CHEBI:81760", "CHEBI:8434", "CHEBI:8489"]
        + ["CHEBI:81760"] * 3 + ["CHEBI:8434"] * 2
        + [i for i in ("CHEBI:474180", "CHEBI:55346", "CHEBI:600520") for _ in range(9)]
    )


def test_seeder_default_does_not_silently_ignore_an_inventory_change(inputs, monkeypatch):
    inventory, _, _ = inputs
    inventory.write_bytes(inventory.read_bytes() + b"\n")
    monkeypatch.setattr(seed, "RAW_DIR", inventory.parent)
    with pytest.raises(ValueError, match="inventory drift"):
        seed.attach_phibase_resistance({})


def test_new_review_only_refreshes_provenance_for_previous_decisions(inputs, tmp_path):
    _, rows, path = inputs
    old_document = json.loads(path.read_bytes())
    old_document["reviews"] = [r for r in old_document["reviews"]
                               if r["pmid"] not in FUMIGATUS_REFERENCES]
    old_path = tmp_path / "previous-reviews.json"
    old_path.write_text(json.dumps(old_document))
    before = {r["identifier"]: {
        "identifier": r["identifier"],
        "chemical_structure": {"standard_inchi_key": r["standard_inchi_key"]},
        "curation_history": [],
    } for r in rows}
    after = copy.deepcopy(before)
    previous = seed.attach_phibase_resistance(before, grounding_review=old_path)
    current = seed.attach_phibase_resistance(after, grounding_review=path)
    assert previous["reviewed_identifier_context"] == CURRENT_REVIEWED - 17
    assert current["reviewed_identifier_context"] == CURRENT_REVIEWED
    changed = []
    for identifier in before:
        for old, new in zip(before[identifier]["resistance_mechanisms"],
                            after[identifier]["resistance_mechanisms"], strict=True):
            if old["evidence"][0]["reference"].removeprefix("PMID:") in FUMIGATUS_REFERENCES:
                continue
            if old == new:
                continue
            changed.append(identifier)
            assert {k for k in old if old[k] != new[k]} == {"evidence"}
            assert new["evidence"][:-1] == old["evidence"][:-1]
            assert new["evidence"][-1]["reference"] == old["evidence"][-1]["reference"]
            assert new["evidence"][-1]["notes"].split("SHA-256 ")[0] == (
                old["evidence"][-1]["notes"].split("SHA-256 ")[0]
            )
    assert sorted(changed) == sorted(
        ["CHEBI:10023"] * 16 + ["CHEBI:46081"] * 30 + ["CHEBI:6076"] * 9 + ["CHEBI:48080"]
        + ["CHEBI:81784"] * 2 + ["CHEBI:81972"] * 2 + ["CHEBI:474180"] * 2
        + ["CHEBI:9448"] * 3
        + ["CHEBI:3405"] * 34 + ["CHEBI:3392"] * 4
        + ["CHEBI:16240"] * 3 + ["CHEBI:40909"] * 3 + ["CHEBI:136340"] * 2
        + ["CHEBI:28909"] * 13 + ["CHEBI:81763"] * 8
        + ["CHEBI:27641", "CHEBI:81760", "CHEBI:8434", "CHEBI:8489"]
        + ["CHEBI:81760"] * 3 + ["CHEBI:8434"] * 2
        + [i for i in ("CHEBI:474180", "CHEBI:55346", "CHEBI:600520") for _ in range(9)]
    )


def test_li_review_does_not_resolve_individual_clones_or_change_other_claims(inputs):
    _, rows, _ = inputs
    doc = load_record(ROOT / "data/antibiotics/antifungal/carbendazim.yaml")
    source = [r for r in rows if r["identifier"] == "CHEBI:3392"]
    claims = [c for c in doc["resistance_mechanisms"] if seed.is_phibase_sourced_resistance(c)]
    assert len(source) == len(claims) == 12 and len(doc["resistance_mechanisms"]) == 19
    assert doc["curation_status"] == "SEEDED" and not doc.get("activity_spectrum")
    for row, claim in zip(source, claims, strict=True):
        assert claim["alteration"] == row["modification"]
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim.get("gene_id") == (row["gene_id"] or None)
        expected_taxid = (
            "948311" if row["pmid"] == "30732567" and row["strain_label"] == "HC30" else row["taxon_id"]
        )
        assert claim["taxon_id"] == "NCBITaxon:" + expected_taxid
        assert claim["mechanism_type"] == "UNKNOWN"
        if row["pmid"] == "8641470":
            assert claim["strain"] == "WL167Y"
            assert "protein_accession" not in claim and "strain_taxon_id" not in claim
            assert "strain_taxon_id=NCBITaxon:559292" in claim["note"]
            assert "protein_accession=UniProtKB:P02557" in claim["note"]
            assert "does not resolve a unique clone" in claim["note"]
            assert "not an exact experimental allele" in claim["note"]
        elif row["pmid"] == "30732567":
            assert claim["strain"] == row["strain_label"] + "M"
            assert "protein_accession" not in claim and "strain_taxon_id" not in claim
            assert claim["taxon_label"] == (
                "Fusarium proliferatum" if row["strain_label"] == "HC30" else "Fusarium verticillioides"
            )
        elif row["pmid"] == "42112916":
            assert claim["strain"] == row["strain_label"] == "V592"
            assert "protein_accession" not in claim and "strain_taxon_id" not in claim
            assert "paper names the parent Vd592" in claim["note"]
            assert "VdLs.17" in claim["note"]
        else:
            assert claim["strain"] == row["strain_label"]
            assert claim["protein_accession"] == "UniProtKB:" + row["protein_accession"]
            assert claim.get("strain_taxon_id") == (
                "NCBITaxon:" + row["strain_taxon_id"] if row["strain_taxon_id"] else None
            )
            assert "Grounding review" not in claim["note"]
    records = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    fresh = copy.deepcopy(doc)
    fresh["resistance_mechanisms"] = [
        c for c in fresh["resistance_mechanisms"] if not seed.is_phibase_sourced_resistance(c)
    ]
    records["CHEBI:3392"] = fresh
    seed.attach_phibase_resistance(records)
    assert fresh == doc


def test_li_review_only_refreshes_prior_decision_checksums(inputs, tmp_path):
    _, rows, path = inputs
    old = json.loads(path.read_bytes())
    old["reviews"] = [d for d in old["reviews"] if d["pmid"] != "8641470"]
    old_path = tmp_path / "before-li.json"
    old_path.write_text(json.dumps(old))
    before = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    after = copy.deepcopy(before)
    assert seed.attach_phibase_resistance(before, grounding_review=old_path)[
        "reviewed_identifier_context"] == CURRENT_REVIEWED - 1
    assert seed.attach_phibase_resistance(after, grounding_review=path)[
        "reviewed_identifier_context"] == CURRENT_REVIEWED
    checksum_only = 0
    for identifier in before:
        for a, b in zip(before[identifier]["resistance_mechanisms"],
                        after[identifier]["resistance_mechanisms"], strict=True):
            if a == b or a["evidence"][0]["reference"] == "PMID:8641470":
                continue
            checksum_only += 1
            assert {k for k in a if a[k] != b[k]} == {"evidence"}
            expected = copy.deepcopy(a)
            expected["evidence"][-1]["notes"] = expected["evidence"][-1]["notes"].replace(
                review.hashlib.sha256(old_path.read_bytes()).hexdigest(),
                review.hashlib.sha256(path.read_bytes()).hexdigest())
            assert expected == b
    assert checksum_only == CURRENT_REVIEWED - 1


def test_misassigned_only_review_does_not_label_rejected_ids_reference_only(inputs):
    inventory, rows, path = inputs
    document = json.loads(path.read_bytes())
    decision = decision_for(document, "8307980")
    decision["withhold"] = decision["misassigned"]
    path.write_text(json.dumps(document))
    decisions = review.load_reviews(inventory, rows, path)
    row = next(r for r in rows if r["pmid"] == "8307980")
    item = {"protein_accession": "UniProtKB:P38637", "gene_id": "YIR011C_mRNA",
            "note": "Source association.", "evidence": []}
    assert review.apply_review(item, row, decisions)
    assert "Rejected misassigned source identifiers:" in item["note"]
    assert "Reference-only source identifiers:" not in item["note"]
    assert "gene_id" not in item and "protein_accession" not in item


@pytest.mark.parametrize("name,identifier,pmid,total,scoped", [
    ("iprodione", "CHEBI:28909", "22912706", 15, 8),
    ("fludioxonil", "CHEBI:81763", "41649761", 13, 3),
])
def test_fungicide_scope_corrections_preserve_other_claims_and_reseed(
    inputs, name, identifier, pmid, total, scoped,
):
    _, rows, _ = inputs
    doc = load_record(ROOT / f"data/antibiotics/antifungal/{name}.yaml")
    source = [r for r in rows if r["identifier"] == identifier]
    assert len(source) == len(doc["resistance_mechanisms"]) == total
    assert doc["curation_status"] == "SEEDED" and not doc.get("activity_spectrum")
    seen = 0
    for row, claim in zip(source, doc["resistance_mechanisms"], strict=True):
        assert claim["alteration"] == row["modification"]
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim["taxon_id"] == "NCBITaxon:" + row["taxon_id"]
        assert claim["mechanism_type"] == "UNKNOWN"
        if row["pmid"] == pmid:
            seen += 1
            assert not any(k in claim for k in ("protein_accession", "strain_taxon_id", "gene_id"))
            for field, prefix in (("protein_accession", "UniProtKB:"),
                                  ("strain_taxon_id", "NCBITaxon:")):
                assert field + "=" + prefix + row[field] in claim["note"]
            if name == "iprodione":
                assert claim["strain"] == "B05.10" and "JX192607-JX192631" in claim["note"]
            else:
                assert claim["strain"] == {"W7LTW3": "\u0394FvPbs2", "W7LX41": "\u0394FvSsk2",
                                           "W7M468": "\u0394FvHog1"}[row["protein_accession"]]
                assert "does not establish 7600 as the experimental parent" in claim["note"]
        elif row["pmid"] == "17073308":
            assert claim["strain"] == "IPO323" and claim["gene_id"] == "Mycgr3T76502"
            assert "protein_accession" not in claim and "strain_taxon_id" not in claim
            assert "parent background" in claim["note"]
        elif row["pmid"] == "30686204":
            assert claim["strain"] == REN_SUBJECTS[row["strain_label"]]
            assert "protein_accession" not in claim and "strain_taxon_id" not in claim
            assert "Original source background label: " + row["strain_label"] in claim["note"]
        else:
            assert claim["protein_accession"] == "UniProtKB:" + row["protein_accession"]
            assert claim["strain_taxon_id"] == "NCBITaxon:" + row["strain_taxon_id"]
            assert claim["strain"] == row["strain_label"]
            assert "Grounding review" not in claim["note"]
    assert seen == scoped
    fresh = copy.deepcopy(doc)
    fresh["resistance_mechanisms"] = []
    records = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    records[identifier] = fresh
    seed.attach_phibase_resistance(records)
    assert fresh == doc


def test_carboxin_reference_scope_preserves_source_rows_and_reseeding(inputs):
    _, rows, _ = inputs
    doc = load_record(ROOT / "data/antibiotics/antifungal/carboxin.yaml")
    all_rows = [r for r in rows if r["identifier"] == "CHEBI:3405"]
    assert len(all_rows) == len(doc["resistance_mechanisms"]) == 36
    assert doc["curation_status"] == "SEEDED" and not doc.get("activity_spectrum")
    scoped = 0
    for row, claim in zip(all_rows, doc["resistance_mechanisms"], strict=True):
        assert claim["alteration"] == row["modification"]
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim["strain"] == row["strain_label"]
        assert claim["taxon_id"] == "NCBITaxon:" + row["taxon_id"]
        assert claim["mechanism_type"] == "UNKNOWN"
        if row["pmid"] in {
            "21933337", "22536383", "26092798", "27558019", "25441450", "27644008", "18992352",
        }:
            scoped += 1
            assert not any(k in claim for k in ("protein_accession", "strain_taxon_id", "gene_id"))
            assert "parent background" in claim["note"]
            assert "protein_accession=UniProtKB:" + row["protein_accession"] in claim["note"]
            if row["strain_taxon_id"]:
                assert "strain_taxon_id=NCBITaxon:" + row["strain_taxon_id"] in claim["note"]
        else:
            assert claim["protein_accession"] == "UniProtKB:" + row["protein_accession"]
            assert "Grounding review" not in claim["note"]
    assert scoped == 34
    fresh = copy.deepcopy(doc)
    fresh["resistance_mechanisms"] = []
    records = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    records["CHEBI:3405"] = fresh
    seed.attach_phibase_resistance(records)
    assert fresh == doc


@pytest.mark.parametrize("pmid,reference,forbidden", [
    ("26092798", "F9XG45", "336722"),
    ("27558019", "G4NE45", "242507"),
])
def test_followup_reference_crosswalk_never_replaces_tested_subject(pmid, reference, forbidden):
    doc = load_record(ROOT / "data/antibiotics/antifungal/carboxin.yaml")
    claims = [c for c in doc["resistance_mechanisms"]
              if c["evidence"][0]["reference"] == "PMID:" + pmid]
    assert len(claims) == 1
    claim = claims[0]
    assert all(k not in claim for k in ("protein_accession", "strain_taxon_id", "gene_id"))
    assert reference in claim["note"]
    assert claim["taxon_id"] != "NCBITaxon:" + forbidden
    if pmid == "26092798":
        assert claim["strain"] == "IPO323" and "XP_003850753.1" in claim["note"]
    else:
        assert claim["strain"] == "Guy11" and "without a version" in claim["note"]
        assert "10.1186/s13568-019-0814-5" in claim["evidence"][-1]["notes"]


@pytest.mark.parametrize("name,identifier,total,activities,scoped", [
    ("itraconazole", "CHEBI:6076", 54, 0, 10),
    ("posaconazole", "CHEBI:64355", 28, 0, 5),
    ("voriconazole", "CHEBI:10023", 62, 3, 2),
])
def test_fumigatus_reference_scope_preserves_source_claims(
    inputs, name, identifier, total, activities, scoped,
):
    _, rows, _ = inputs
    doc = load_record(ROOT / f"data/antibiotics/antifungal/{name}.yaml")
    source = [r for r in rows if r["identifier"] == identifier]
    claims = [c for c in doc["resistance_mechanisms"] if c.get("source") == "PHIBASE"]
    assert len(doc["resistance_mechanisms"]) == total
    assert doc["curation_status"] == "SEEDED"
    assert len(doc.get("activity_spectrum", [])) == activities
    seen = 0
    for row, claim in zip(source, claims, strict=True):
        if row["pmid"] not in FUMIGATUS_REFERENCES:
            continue
        seen += 1
        assert claim["strain"] == row["strain_label"]
        assert claim["taxon_id"] == "NCBITaxon:746128"
        assert claim["alteration"] == row["modification"]
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim["mechanism_type"] == "UNKNOWN"
        assert "protein_accession" not in claim and "strain_taxon_id" not in claim
        assert "protein_accession=UniProtKB:" + row["protein_accession"] in claim["note"]
        assert "strain_taxon_id=NCBITaxon:330879" in claim["note"]
        assert claim["evidence"][-1]["reference"] == FUMIGATUS_REFERENCES[row["pmid"]]
        if row["protein_accession"] == "Q4WNT5":
            assert claim["gene_id"] == "Afu4g06890-T"
            assert "retained gene_id denote the Af293 reference locus" in claim["note"]
        else:
            assert row["protein_accession"] == "Q4WDM9" and "gene_id" not in claim
            assert "not either later tested replicate or the native clinical isolate" in claim["note"]
    assert seen == scoped
    fixture = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    seed.attach_phibase_resistance(fixture)
    assert fixture[identifier]["resistance_mechanisms"] == claims


@pytest.mark.parametrize("pmid,expected", [("22897872", 4)])
def test_fumigatus_pending_studies_are_not_promoted(inputs, pmid, expected):
    _, rows, _ = inputs
    selected = [r for r in rows if r["pmid"] == pmid]
    assert len(selected) == expected
    by_identifier = {r["identifier"] for r in selected}
    records = [load_record(ROOT / f"data/antibiotics/antifungal/{name}.yaml")
               for name in ("itraconazole", "posaconazole", "voriconazole", "terbinafine")]
    claims = [c for d in records if d["identifier"] in by_identifier
              for c in d["resistance_mechanisms"] if c.get("source") == "PHIBASE"
              and c["evidence"][0]["reference"] == "PMID:" + pmid]
    assert len(claims) == expected
    assert all("protein_accession" in c and "strain_taxon_id" in c for c in claims)
    assert all("Grounding review" not in c["note"] and len(c["evidence"]) == 1 for c in claims)


@pytest.mark.parametrize("name,identifier,total,activities,scoped", [
    ("itraconazole", "CHEBI:6076", 54, 0, 6),
    ("voriconazole", "CHEBI:10023", 62, 3, 1),
    ("terbinafine", "CHEBI:9448", 11, 0, 3),
    ("fluconazole", "CHEBI:46081", 77, 2, 2),
])
def test_followup_keeps_parent_labels_and_source_biology(
    inputs, name, identifier, total, activities, scoped,
):
    _, rows, _ = inputs
    doc = load_record(ROOT / f"data/antibiotics/antifungal/{name}.yaml")
    source = [r for r in rows if r["identifier"] == identifier]
    claims = [c for c in doc["resistance_mechanisms"] if c.get("source") == "PHIBASE"]
    assert len(doc["resistance_mechanisms"]) == total
    assert len(doc.get("activity_spectrum", [])) == activities
    count = 0
    for row, claim in zip(source, claims, strict=True):
        if row["pmid"] not in FOLLOWUP_REFERENCES:
            continue
        count += 1
        assert claim["strain"] == row["strain_label"]
        assert claim["taxon_id"] == "NCBITaxon:" + row["taxon_id"]
        assert claim["alteration"] == row["modification"]
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim.get("gene_id") == (row["gene_id"] or None)
        assert claim["mechanism_type"] == "UNKNOWN"
        assert "protein_accession" not in claim and "strain_taxon_id" not in claim
        assert "protein_accession=UniProtKB:" + row["protein_accession"] in claim["note"]
        assert "strain_taxon_id=NCBITaxon:" + row["strain_taxon_id"] in claim["note"]
        assert "parent background" in claim["note"] and "remain unresolved" in claim["note"]
        assert claim["evidence"][-1]["reference"] == FOLLOWUP_REFERENCES[row["pmid"]]
        if row["pmid"] == "27799210":
            assert "frequency of later colonies is distinct from baseline susceptibility" in claim["note"]
            assert "plate growth is not a broth MIC" in claim["note"]
        elif row["pmid"] == "39464835":
            assert "not converted into MICs or clinical categories" in claim["note"]
    assert count == scoped
    fixture = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    seed.attach_phibase_resistance(fixture)
    assert fixture[identifier]["resistance_mechanisms"] == claims


def test_followup_only_refreshes_other_review_checksums(inputs, tmp_path):
    _, rows, path = inputs
    old = json.loads(path.read_bytes())
    old["reviews"] = [d for d in old["reviews"] if d["pmid"] not in FOLLOWUP_REFERENCES]
    old_path = tmp_path / "before-followup.json"
    old_path.write_text(json.dumps(old))
    before = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    after = copy.deepcopy(before)
    assert seed.attach_phibase_resistance(before, grounding_review=old_path)[
        "reviewed_identifier_context"] == CURRENT_REVIEWED - 12
    assert seed.attach_phibase_resistance(after, grounding_review=path)[
        "reviewed_identifier_context"] == CURRENT_REVIEWED
    changed = 0
    for identifier in before:
        for a, b in zip(before[identifier]["resistance_mechanisms"],
                        after[identifier]["resistance_mechanisms"], strict=True):
            if a == b or a["evidence"][0]["reference"].removeprefix("PMID:") in FOLLOWUP_REFERENCES:
                continue
            changed += 1
            expected = copy.deepcopy(a)
            expected["evidence"][-1]["notes"] = expected["evidence"][-1]["notes"].replace(
                review.hashlib.sha256(old_path.read_bytes()).hexdigest(),
                review.hashlib.sha256(path.read_bytes()).hexdigest())
            assert expected == b
    assert changed == CURRENT_REVIEWED - 12


@pytest.mark.parametrize("name,identifier,total,activities,scoped", [
    ("carboxin", "CHEBI:3405", 36, 0, 1),
    ("caspofungin", "CHEBI:474180", 33, 0, 2),
    ("fluconazole", "CHEBI:46081", 77, 2, 1),
    ("voriconazole", "CHEBI:10023", 62, 3, 1),
    ("pyrifenox", "CHEBI:81972", 2, 0, 2),
    ("triflumizole", "CHEBI:81784", 2, 0, 2),
])
def test_primary_context_preserves_biology_and_annotates_compound_limit(
    inputs, name, identifier, total, activities, scoped,
):
    _, rows, _ = inputs
    doc = load_record(ROOT / f"data/antibiotics/antifungal/{name}.yaml")
    source = [r for r in rows if r["identifier"] == identifier]
    claims = [c for c in doc["resistance_mechanisms"] if c.get("source") == "PHIBASE"]
    assert len(doc["resistance_mechanisms"]) == total
    assert len(doc.get("activity_spectrum", [])) == activities
    count = 0
    for row, claim in zip(source, claims, strict=True):
        if row["pmid"] not in PRIMARY_CONTEXT_REFERENCES:
            continue
        count += 1
        assert claim["strain"] == row["strain_label"]
        assert claim["taxon_id"] == "NCBITaxon:" + row["taxon_id"]
        assert claim["alteration"] == row["modification"]
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim["mechanism_type"] == "UNKNOWN"
        assert "protein_accession" not in claim and "strain_taxon_id" not in claim
        assert "gene_id" not in claim
        assert "protein_accession=UniProtKB:" + row["protein_accession"] in claim["note"]
        if row["strain_taxon_id"]:
            assert "strain_taxon_id=NCBITaxon:" + row["strain_taxon_id"] in claim["note"]
        assert claim["evidence"][-1]["reference"] == PRIMARY_CONTEXT_REFERENCES[row["pmid"]]
        if row["pmid"] == "16048935":
            assert "Table 4 reports L-733560, not caspofungin" in claim["note"]
            assert "does not validate that source phenotype" in claim["note"]
        elif row["pmid"] == "10919801":
            assert "two source isolates" in claim["note"]
        elif row["pmid"] == "22155829":
            assert "deposit cross-reference different" in claim["note"]
    assert count == scoped
    fixture = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    seed.attach_phibase_resistance(fixture)
    assert fixture[identifier]["resistance_mechanisms"] == claims


def test_primary_context_refreshes_only_other_review_checksums(inputs, tmp_path):
    _, rows, path = inputs
    old = json.loads(path.read_bytes())
    old["reviews"] = [d for d in old["reviews"] if d["pmid"] not in PRIMARY_CONTEXT_REFERENCES]
    old_path = tmp_path / "before-primary-context.json"
    old_path.write_text(json.dumps(old))
    before = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    after = copy.deepcopy(before)
    assert seed.attach_phibase_resistance(before, grounding_review=old_path)[
        "reviewed_identifier_context"] == CURRENT_REVIEWED - 9
    assert seed.attach_phibase_resistance(after, grounding_review=path)[
        "reviewed_identifier_context"] == CURRENT_REVIEWED
    changed = 0
    for identifier in before:
        for a, b in zip(before[identifier]["resistance_mechanisms"],
                        after[identifier]["resistance_mechanisms"], strict=True):
            if a == b or a["evidence"][0]["reference"].removeprefix("PMID:") in PRIMARY_CONTEXT_REFERENCES:
                continue
            changed += 1
            expected = copy.deepcopy(a)
            expected["evidence"][-1]["notes"] = expected["evidence"][-1]["notes"].replace(
                review.hashlib.sha256(old_path.read_bytes()).hexdigest(),
                review.hashlib.sha256(path.read_bytes()).hexdigest())
            assert expected == b
    assert changed == CURRENT_REVIEWED - 9


@pytest.mark.parametrize("category,name,identifier,total,scoped", [
    ("biocide", "hydrogen-peroxide", "CHEBI:16240", 6, 2),
    ("antifungal", "carbendazim", "CHEBI:3392", 19, 1),
    ("antifungal", "azoxystrobin", "CHEBI:40909", 11, 3),
])
def test_oa_context_preserves_source_biology_without_inventing_alleles_or_mics(
    inputs, category, name, identifier, total, scoped,
):
    _, rows, _ = inputs
    doc = load_record(ROOT / f"data/antibiotics/{category}/{name}.yaml")
    assert len(doc["resistance_mechanisms"]) == total and not doc.get("activity_spectrum")
    source = [r for r in rows if r["identifier"] == identifier]
    claims = [c for c in doc["resistance_mechanisms"] if c.get("source") == "PHIBASE"]
    count = 0
    for row, claim in zip(source, claims, strict=True):
        if row["pmid"] not in OA_CONTEXT_REFERENCES:
            continue
        count += 1
        assert claim["strain"] == row["strain_label"]
        assert claim["taxon_id"] == "NCBITaxon:" + row["taxon_id"]
        assert claim["alteration"] == row["modification"]
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim.get("gene_id") == (row["gene_id"] or None)
        assert claim["mechanism_type"] == "UNKNOWN"
        assert "protein_accession" not in claim and "strain_taxon_id" not in claim
        assert "protein_accession=UniProtKB:" + row["protein_accession"] in claim["note"]
        if row["strain_taxon_id"]:
            assert "strain_taxon_id=NCBITaxon:" + row["strain_taxon_id"] in claim["note"]
        assert claim["evidence"][-1]["reference"] == OA_CONTEXT_REFERENCES[row["pmid"]]
        if row["pmid"] == "26596626":
            assert "including the parent" in claim["note"]
            assert "does not establish an allele-specific azoxystrobin effect" in claim["note"]
        elif row["pmid"] == "30044782":
            assert "ALT_SEQ flag in UniProt does not identify the experimental alteration" in claim["note"]
        elif row["pmid"] == "42112916":
            assert "paper names the parent Vd592" in claim["note"] and "VdLs.17" in claim["note"]
    assert count == scoped
    fixture = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    seed.attach_phibase_resistance(fixture)
    assert fixture[identifier]["resistance_mechanisms"] == claims


def test_oa_review_only_refreshes_other_checksums(inputs, tmp_path):
    _, rows, path = inputs
    old = json.loads(path.read_bytes())
    old["reviews"] = [d for d in old["reviews"] if d["pmid"] not in OA_CONTEXT_REFERENCES]
    old_path = tmp_path / "before-oa.json"
    old_path.write_text(json.dumps(old))
    before = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    after = copy.deepcopy(before)
    assert seed.attach_phibase_resistance(before, grounding_review=old_path)[
        "reviewed_identifier_context"] == CURRENT_REVIEWED - 6
    assert seed.attach_phibase_resistance(after, grounding_review=path)[
        "reviewed_identifier_context"] == CURRENT_REVIEWED
    changed = 0
    for identifier in before:
        for a, b in zip(before[identifier]["resistance_mechanisms"],
                        after[identifier]["resistance_mechanisms"], strict=True):
            if a == b or a["evidence"][0]["reference"].removeprefix("PMID:") in OA_CONTEXT_REFERENCES:
                continue
            changed += 1
            expected = copy.deepcopy(a)
            expected["evidence"][-1]["notes"] = expected["evidence"][-1]["notes"].replace(
                review.hashlib.sha256(old_path.read_bytes()).hexdigest(),
                review.hashlib.sha256(path.read_bytes()).hexdigest())
            assert expected == b
    assert changed == CURRENT_REVIEWED - 6


def test_oa_dossier_is_metadata_only_and_keeps_pending_locus_reviews_separate():
    d = json.loads((ROOT / "research/2026-10-08-fungal-oa-context-grounding.json").read_bytes())
    assert d["changes"] == {"new_scoped_claims": 6, "checksum_only_claims": 150}
    assert len(d["records"]) == 21 and len(d["primary_reviews"]) == 6
    assert len(d["unchanged_lead_claims"]) == 5
    assert len(d["remaining_papers"]) == 25 and len(d["pending_associations"]) == 61
    assert len(d["proteins"]) == 6 and len(d["taxonomy"]) == 8
    assert all("sequence" not in p for p in d["proteins"].values())
    assert d["protein_scope"] == "SOURCE_REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE"
    assert len(d["literature_access"]) == 6
    assert all(p["primary_access"] == "EBI_OPEN_ACCESS_XML_CACHED_AND_IDENTITY_VERIFIED"
               for p in d["literature_access"])
    assert d["current_pending_access_counts"] == {
        "NON_OA_NO_PMC": 21, "NON_OA_WITH_PMC": 2, "OA_WITH_PMC": 2,
    }
    assert {p["reference"] for p in d["remaining_papers"]
            if p["europe_pmc_access_category"] == "OA_WITH_PMC"} == {"PMID:30732567", "PMID:39403939"}


@pytest.mark.parametrize("name,identifier,total", [
    ("iprodione", "CHEBI:28909", 15), ("fludioxonil", "CHEBI:81763", 13),
])
def test_ren_subjects_are_not_parents_or_reference_strains(inputs, name, identifier, total):
    _, rows, _ = inputs
    doc = load_record(ROOT / f"data/antibiotics/antifungal/{name}.yaml")
    source = [r for r in rows if r["identifier"] == identifier]
    assert len(doc["resistance_mechanisms"]) == total and not doc.get("activity_spectrum")
    claims = [c for c in doc["resistance_mechanisms"] if c.get("source") == "PHIBASE"]
    count = 0
    for row, claim in zip(source, claims, strict=True):
        if row["pmid"] != "30686204":
            continue
        count += 1
        assert claim["strain"] == REN_SUBJECTS[row["strain_label"]]
        assert claim["taxon_id"] == "NCBITaxon:40559"
        assert claim["alteration"] == row["modification"] and "[Not assayed]" in claim["alteration"]
        assert claim["phenotype_id"] == row["phenotype_id"] and claim["mechanism_type"] == "UNKNOWN"
        assert not any(k in claim for k in ("protein_accession", "strain_taxon_id", "gene_id"))
        assert "protein_accession=UniProtKB:A0A384J5Y1" in claim["note"]
        assert "strain_taxon_id=NCBITaxon:332648" in claim["note"]
        assert "Original source background label: " + row["strain_label"] in claim["note"]
        assert "Association is not causation" in claim["note"] and "EC50 is not MIC" in claim["note"]
        assert "publisher-indexed primary text; direct fetch unavailable" in claim["evidence"][-1]["notes"]
        assert claim["evidence"][-1]["reference"] == "DOI:10.1094/pdis-11-15-1290-re"
    assert count == 4
    fixture = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    seed.attach_phibase_resistance(fixture)
    assert fixture[identifier]["resistance_mechanisms"] == claims


def test_ren_review_only_refreshes_other_checksums(inputs, tmp_path):
    _, rows, path = inputs
    old = json.loads(path.read_bytes())
    old["reviews"] = [d for d in old["reviews"] if d["pmid"] != "30686204"]
    old_path = tmp_path / "before-ren.json"
    old_path.write_text(json.dumps(old))
    before = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    after = copy.deepcopy(before)
    assert seed.attach_phibase_resistance(before, grounding_review=old_path)[
        "reviewed_identifier_context"] == CURRENT_REVIEWED - 8
    assert seed.attach_phibase_resistance(after, grounding_review=path)[
        "reviewed_identifier_context"] == CURRENT_REVIEWED
    changed = 0
    for identifier in before:
        for a, b in zip(before[identifier]["resistance_mechanisms"],
                        after[identifier]["resistance_mechanisms"], strict=True):
            if a == b or a["evidence"][0]["reference"] == "PMID:30686204":
                continue
            changed += 1
            expected = copy.deepcopy(a)
            expected["evidence"][-1]["notes"] = expected["evidence"][-1]["notes"].replace(
                review.hashlib.sha256(old_path.read_bytes()).hexdigest(),
                review.hashlib.sha256(path.read_bytes()).hexdigest())
            assert expected == b
    assert changed == CURRENT_REVIEWED - 8


def test_ren_dossier_preserves_manual_access_limit_and_metadata_only_scope():
    d = json.loads((ROOT / "research/2026-10-08-ren-subject-context-grounding.json").read_bytes())
    assert d["changes"] == {"new_scoped_claims": 8, "checksum_only_claims": 156}
    assert len(d["records"]) == 21 and len(d["primary_reviews"]) == 4
    assert d["subject_labels"] == REN_SUBJECTS and len(d["unchanged_lead_claims"]) == 5
    assert len(d["remaining_papers"]) == 24 and len(d["pending_associations"]) == 53
    assert d["protein"]["primaryAccession"] == "A0A384J5Y1" and "sequence" not in d["protein"]
    assert d["protein_scope"] == "B05_10_REFERENCE_NOT_EXPERIMENTAL_SUBJECT"
    assert len(d["taxonomy"]) == 2 and len(d["uniprot_requests"]) == 3
    paper, = d["literature_access"]
    assert paper["primary_access"] == "PUBLISHER_INDEXED_TABLES_INSPECTED_WITH_WEB_TOOL_NOT_CACHED"
    assert "offline_verification_limit" in paper and "fulltext_request" not in paper
    discrepancy = d["unresolved_table_discrepancy"]
    assert discrepancy["row_label"] == "Sg-28"
    assert discrepancy["status"] == "INDEXED_VALUES_DISAGREE_ORIGINAL_TABLE_CHECK_REQUIRED"
    assert "No measurement imported" in discrepancy["scope"]
    assert d["current_pending_access_counts"] == {
        "NON_OA_NO_PMC": 20, "NON_OA_WITH_PMC": 2, "OA_WITH_PMC": 2,
    }


def test_nakayama_reference_is_not_an_experimental_derivative(inputs):
    inventory, rows, path = inputs
    decisions = review.load_reviews(inventory, rows, path)
    source, = [r for r in rows if r["pmid"] == "11600353"]
    decision = decisions[review.row_digest(source)]
    assert decision["withhold"] == ["strain_taxon_id", "protein_accession"]
    assert "subject_strain" not in decision and "misassigned" not in decision
    doc = load_record(ROOT / "data/antibiotics/antifungal/fluconazole.yaml")
    claims = [c for c in doc["resistance_mechanisms"] if c.get("source") == "PHIBASE"
              and c["evidence"][0]["reference"] == "PMID:11600353"]
    assert len(claims) == 1
    claim = claims[0]
    assert "protein_accession" not in claim and "strain_taxon_id" not in claim
    assert claim["strain"] == source["strain_label"] == "ATCC 2001"
    assert claim["taxon_id"] == "NCBITaxon:5478" and claim["gene_id"] == source["gene_id"]
    assert claim["alteration"] == source["modification"]
    assert claim["phenotype_id"] == source["phenotype_id"] and claim["assay"] == source["evidence_code"]
    assert claim["mechanism_type"] == "UNKNOWN"
    assert "protein_accession=UniProtKB:P50859" in claim["note"]
    assert "strain_taxon_id=NCBITaxon:284593" in claim["note"]
    assert "background/comparator label" in claim["note"]
    assert "no individual derivative, allele accession or MIC is inferred" in claim["note"]
    assert claim["evidence"][-1]["reference"] == "DOI:10.1128/aac.45.11.3037-3045.2001"
    assert "EBI fullTextXML HTTP 500" in claim["evidence"][-1]["notes"]
    assert len(doc["activity_spectrum"]) == 2 and len(doc["resistance_mechanisms"]) == 77


def test_darlington_subject_is_not_recipient_or_reference_strain(inputs):
    _, rows, _ = inputs
    source, = [r for r in rows if r["pmid"] == "11036010"]
    doc = load_record(ROOT / "data/antibiotics/antifungal/fluconazole.yaml")
    claim, = [c for c in doc["resistance_mechanisms"] if c.get("source") == "PHIBASE"
              and c["evidence"][0]["reference"] == "PMID:11036010"]
    assert claim["strain"] == "transformant 12" and source["strain_label"] == "CAI4"
    assert claim["taxon_id"] == "NCBITaxon:5476" and claim["gene_id"] == source["gene_id"]
    assert claim["alteration"] == source["modification"] and "[Not assayed]" in claim["alteration"]
    assert claim["phenotype_id"] == source["phenotype_id"] and claim["mechanism_type"] == "UNKNOWN"
    assert "protein_accession" not in claim and "strain_taxon_id" not in claim
    assert "Original source background label: CAI4." in claim["note"]
    assert "protein_accession=UniProtKB:P10613" in claim["note"]
    assert "strain_taxon_id=NCBITaxon:237561" in claim["note"]
    assert "heterologous-host comparisons remain separate" in claim["note"]
    assert claim["evidence"][-1]["reference"] == "DOI:10.1128/aac.44.11.2985-2990.2000"
    assert "direct fetch HTTP 403" in claim["evidence"][-1]["notes"]
    assert len(doc["activity_spectrum"]) == 2 and len(doc["resistance_mechanisms"]) == 77
    assert doc["curation_status"] == "SEEDED"


@pytest.mark.parametrize("pmid,new_scopes", [
    ("11036010", 1), ("11600353", 1), ("30497711", 5), ("27644008", 3),
])
def test_subject_review_only_refreshes_other_checksums(inputs, tmp_path, pmid, new_scopes):
    _, rows, path = inputs
    old = json.loads(path.read_bytes())
    old["reviews"] = [d for d in old["reviews"] if d["pmid"] != pmid]
    old_path = tmp_path / "before-subject-review.json"
    old_path.write_text(json.dumps(old))
    before = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    after = copy.deepcopy(before)
    assert seed.attach_phibase_resistance(before, grounding_review=old_path)[
        "reviewed_identifier_context"] == CURRENT_REVIEWED - new_scopes
    assert seed.attach_phibase_resistance(after, grounding_review=path)[
        "reviewed_identifier_context"] == CURRENT_REVIEWED
    changed = 0
    for identifier in before:
        for a, b in zip(before[identifier]["resistance_mechanisms"],
                        after[identifier]["resistance_mechanisms"], strict=True):
            if a == b or a["evidence"][0]["reference"] == "PMID:" + pmid:
                continue
            changed += 1
            expected = copy.deepcopy(a)
            expected["evidence"][-1]["notes"] = expected["evidence"][-1]["notes"].replace(
                review.hashlib.sha256(old_path.read_bytes()).hexdigest(),
                review.hashlib.sha256(path.read_bytes()).hexdigest())
            assert expected == b
    assert changed == CURRENT_REVIEWED - new_scopes


@pytest.mark.parametrize("name,identifier,count", [
    ("difenoconazole", "CHEBI:81760", 3), ("prochloraz", "CHEBI:8434", 2),
])
def test_duan_parent_labels_do_not_assign_ph1_to_experimental_derivatives(
    inputs, name, identifier, count,
):
    _, rows, _ = inputs
    doc = load_record(ROOT / f"data/antibiotics/antifungal/{name}.yaml")
    claims = [c for c in doc["resistance_mechanisms"]
              if c["evidence"][0]["reference"] == "PMID:30497711"]
    source = [r for r in rows if r["identifier"] == identifier and r["pmid"] == "30497711"]
    assert len(claims) == len(source) == count
    for claim, row in zip(claims, source, strict=True):
        assert claim["strain"] == row["strain_label"]
        assert claim["taxon_id"] == "NCBITaxon:5518"
        assert claim["gene_id"] == row["gene_id"] == "FGRAMPH1_01T14465"
        assert claim["alteration"] == row["modification"]
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim["assay"] == row["evidence_code"] and claim["mechanism_type"] == "UNKNOWN"
        assert "protein_accession" not in claim and "strain_taxon_id" not in claim
        assert "parental backgrounds, not exact resistant derivatives" in claim["note"]
        assert "retained gene locus are reference context" in claim["note"]
        assert "protein_accession=UniProtKB:I1RJR2" in claim["note"]
        assert "strain_taxon_id=NCBITaxon:229533" in claim["note"]
        assert "complete Results unavailable" in claim["evidence"][-1]["notes"]
    assert not doc.get("activity_spectrum") and doc["curation_status"] == "SEEDED"
    fresh = copy.deepcopy(doc)
    fresh["resistance_mechanisms"] = [c for c in fresh["resistance_mechanisms"]
                                     if not seed.is_phibase_sourced_resistance(c)]
    fixture = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    fixture[identifier] = fresh
    seed.attach_phibase_resistance(fixture)
    assert fresh == doc


def test_piotrowska_parent_references_do_not_become_descendant_accessions(inputs):
    _, rows, _ = inputs
    doc = load_record(ROOT / "data/antibiotics/antifungal/carboxin.yaml")
    claims = [c for c in doc["resistance_mechanisms"]
              if c["evidence"][0]["reference"] == "PMID:27644008"]
    source = [r for r in rows if r["pmid"] == "27644008"]
    assert len(claims) == len(source) == 3
    for claim, row in zip(claims, source, strict=True):
        assert claim["strain"] == row["strain_label"] == "DK05"
        assert claim["taxon_id"] == "NCBITaxon:112498"
        assert claim["alteration"] == row["modification"]
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim["assay"] == row["evidence_code"] and claim["mechanism_type"] == "UNKNOWN"
        assert "gene_id" not in claim and "strain_taxon_id" not in claim
        assert "protein_accession" not in claim
        assert "protein_accession=UniProtKB:" + row["protein_accession"] in claim["note"]
        assert "parent background, not the tested descendants" in claim["note"]
        assert "EC50-based resistance factors are not MICs" in claim["note"]
        assert claim["evidence"][-1]["reference"] == "DOI:10.1002/ps.4442"
    assert not doc.get("activity_spectrum") and doc["curation_status"] == "SEEDED"
    assert len(doc["resistance_mechanisms"]) == 36
    fixture = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    seed.attach_phibase_resistance(fixture)
    assert fixture["CHEBI:3405"]["resistance_mechanisms"] == doc["resistance_mechanisms"]


def test_piotrowska_dossier_separates_parent_metadata_and_experimental_identifiers():
    d = json.loads((ROOT / "research/2026-10-08-piotrowska-reference-grounding.json").read_bytes())
    assert d["changes"] == {"new_scoped_claims": 3, "checksum_only_claims": 171}
    assert d["corpus_phi_scope"] == {"retained": 217, "identifier_scoped": 174,
                                     "pending_associations": 43, "pending_papers": 20}
    proteins = {p["accession"]: p for p in d["proteins"]}
    assert set(proteins) == {"A0A1S6KZ79", "A0A1S6KZ87"}
    assert proteins["A0A1S6KZ79"]["entry_version"] == 35
    assert proteins["A0A1S6KZ87"]["entry_version"] == 22
    for protein in proteins.values():
        assert protein["scope"] == "PARENT_REFERENCE_NOT_EXPERIMENTAL_ALLELE"
        assert protein["source_strain_comments"] == ["DK 05 Rcc 001 ss2"]
        assert protein["taxon_id"] == 112498 and protein["sequence_version"] == 1
        assert not protein["reviewed"] and "sequence" not in protein
    assert d["taxonomy"]["rank"] == "species"
    assert d["subjects"]["source_background_label"] == "DK05"
    assert d["subjects"]["primary_parent_label"] == "DK05Rcc001ss2"
    assert all(v is None for k, v in d["subjects"].items() if k.startswith("experimental_"))
    access = d["primary_access"]
    assert access["review_scope"] == "ACCEPTED_MANUSCRIPT_IDENTITY_AND_ENDPOINT_CONTEXT"
    assert access["cached_manuscript"]["status"] == 200
    assert access["cached_manuscript"]["sha256"] == (
        "4cf3a99c7ce59efec6db73d092e01cfcfe71758572b898773fb774b4c12d856b")
    assert "not the manual scientific reading" in access["offline_verification_limit"]
    assert d["preservation"]["new_measurements"] == 0


def test_duan_dossier_preserves_reference_scope_and_partial_primary_access():
    d = json.loads((ROOT / "research/2026-10-08-duan-reference-grounding.json").read_bytes())
    assert d["changes"] == {"new_scoped_claims": 5, "checksum_only_claims": 166}
    assert d["corpus_phi_scope"] == {"retained": 217, "identifier_scoped": 171,
                                     "pending_associations": 46, "pending_papers": 21}
    assert d["protein"]["primaryAccession"] == "I1RJR2"
    assert d["protein"]["entryAudit"] == {"entryVersion": 82, "sequenceVersion": 1}
    assert d["protein"]["organism"]["taxonId"] == 229533
    assert d["taxonomy"]["229533"]["parent"]["taxonId"] == 5518
    assert d["subjects"]["source_background_labels"] == ["2021", "BM50", "BM6"]
    assert all(value is None for key, value in d["subjects"].items() if key.startswith("experimental_"))
    assert d["primary_access"]["review_scope"] == (
        "MANUAL_INDEXED_PRIMARY_SECTION_SNIPPETS_NOT_COMPLETE_RESULTS"
    )
    assert d["preservation"]["new_measurements"] == 0 and "sequence" not in d["protein"]


def test_nakayama_dossier_preserves_unresolved_measurement_and_reference_scope():
    d = json.loads((ROOT / "research/2026-10-08-nakayama-reference-grounding.json").read_bytes())
    assert d["changes"] == {"new_scoped_claims": 1, "checksum_only_claims": 165}
    assert d["corpus_phi_scope"] == {"retained": 217, "identifier_scoped": 166,
                                     "pending_associations": 51, "pending_papers": 22}
    assert len(d["records"]) == 21 and d["preservation"]["record_files_byte_identical"] == 2918
    assert d["preservation"]["new_measurements"] == 0
    assert d["protein"]["primaryAccession"] == "P50859" and "sequence" not in d["protein"]
    assert d["protein"]["source_gene_cross_reference"]["id"] == "CAGL0E04334g-T"
    assert d["protein_scope"] == "ATCC_2001_REFERENCE_NOT_EXPERIMENTAL_DERIVATIVE"
    assert d["subject"]["experimental_allele_accession"] is None
    assert d["subject"]["experimental_protein_accession"] is None
    assert d["subject"]["experimental_strain_taxon_id"] is None
    assert d["subject"]["experimental_genome_accession"] is None
    assert d["taxonomy"]["284593"]["rank"] == "strain"
    assert d["taxonomy"]["284593"]["parent"]["taxonId"] == 5478
    assert d["taxonomy"]["5478"]["rank"] == "species"
    assert len(d["uniprot_requests"]) == 3
    assert d["primary_access"]["failed_fulltext_request"]["status"] == 500
    assert d["primary_access"]["review_scope"] == (
        "PUBLISHER_INDEXED_PRIMARY_RESULTS_INSPECTED_WITH_WEB_TOOL_NOT_CACHED")
    assert "offline_verification_limit" in d["primary_access"]
    discrepancy = d["unresolved_table_discrepancy"]
    assert discrepancy["status"] == "CONDITION_LABEL_CONFLICT_ORIGINAL_LAYOUT_CHECK_REQUIRED"
    assert "IC50 is not MIC" in discrepancy["scope"] and "No values imported" in discrepancy["scope"]


def test_darlington_dossier_keeps_primary_access_and_reference_scope_explicit():
    d = json.loads((ROOT / "research/2026-10-08-darlington-subject-grounding.json").read_bytes())
    assert d["changes"] == {"new_scoped_claims": 1, "checksum_only_claims": 164}
    assert d["corpus_phi_scope"] == {"retained": 217, "identifier_scoped": 165,
                                     "pending_associations": 52, "pending_papers": 23}
    assert len(d["records"]) == 21 and len(d["pending_associations"]) == 52
    assert d["subject"]["primary_subject"] == "transformant 12"
    assert d["subject"]["experimental_protein_accession"] is None
    assert d["subject"]["experimental_allele_accession"] is None
    assert d["protein"]["primaryAccession"] == "P10613" and "sequence" not in d["protein"]
    assert d["protein_scope"] == "SC5314_REFERENCE_NOT_EXPERIMENTAL_SUBJECT"
    assert len(d["taxonomy"]) == 2 and len(d["uniprot_requests"]) == 3
    access = d["primary_access"]
    assert access["review_scope"] == "MANUAL_PUBLISHER_FULL_TEXT_REVIEW_WITH_WEB_TOOL"
    assert access["direct_request_failure"]["status"] == 403
    assert "offline_verification_limit" in access


def test_primary_context_dossier_does_not_promote_shared_deposits_or_missing_gene_names():
    d = json.loads((ROOT / "research/2026-10-08-fungal-primary-context-grounding.json").read_bytes())
    assert d["changes"] == {"new_scoped_claims": 9, "checksum_only_claims": 141}
    assert len(d["records"]) == 19 and len(d["primary_reviews"]) == 4
    assert len(d["unchanged_lead_claims"]) == 2 and len(d["remaining_papers"]) == 31
    assert len(d["pending_associations"]) == 67
    assert len(d["proteins"]) == 6 and len(d["taxonomy"]) == 8
    assert "genes" not in d["proteins"]["Q870D1"]
    assert all("sequence" not in p for p in d["proteins"].values())
    x = next(x for x in d["reference_crosswalks"] if x["uniprot_accession"] == "Q9P340")
    assert {v["id"] for v in x["cross_references"] if v["database"] == "EMBL"} == {"AB030178", "AB030179"}
    assert x["scope"] == "SOURCE_REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE"
    manual = [p for p in d["literature_access"] if p["status"] == "IDENTIFIER_SCOPE_CURATED"]
    assert len(manual) == 4 and all("offline_verification_limit" in p for p in manual)
    assert d["current_pending_access_counts"] == {
        "NON_OA_NO_PMC": 21, "NON_OA_WITH_PMC": 2, "OA_WITH_PMC": 8,
    }


def test_followup_access_inventory_covers_the_entire_prior_pending_cohort():
    d = json.loads((ROOT / "research/2026-10-08-fungal-identity-followup-grounding.json").read_bytes())
    assert d["changes"] == {"new_scoped_claims": 12, "checksum_only_claims": 129}
    assert len(d["records"]) == 17 and len(d["primary_reviews"]) == 6
    prior, pending = d["prior_pending_associations"], d["pending_associations"]
    assert len(prior) == 88 and len(pending) == 76
    assert {r["reference"] for r in d["literature_access"]} == {"PMID:" + r["pmid"] for r in prior}
    assert len(d["literature_access"]) == 41 and len({r["pmid"] for r in pending}) == 35
    assert d["prior_pending_access_counts"] == {
        "NON_OA_NO_PMC": 21, "NON_OA_WITH_PMC": 11, "OA_WITH_PMC": 9,
    }
    assert d["current_pending_access_counts"] == {
        "NON_OA_NO_PMC": 21, "NON_OA_WITH_PMC": 6, "OA_WITH_PMC": 8,
    }
    assert len(d["proteins"]) == 6 and len(d["taxonomy"]) == 5
    assert all("sequence" not in p for p in d["proteins"].values())
    assert all(r["scope"] == "REFERENCE_ONLY_NOT_TESTED_SUBJECT" for r in d["reference_crosswalks"])
    manual = [p for p in d["literature_access"]
              if p.get("primary_access") == "PUBLISHER_HTML_INSPECTED_WITH_WEB_TOOL_NOT_CACHED"]
    assert len(manual) == 5
    assert all("offline_verification_limit" in p and "fulltext_request" not in p for p in manual)


def test_historical_sdh8_query_and_current_reference_alias_do_not_ground_an_allele():
    d = json.loads((ROOT / "research/2026-10-08-fungal-identity-followup-grounding.json").read_bytes())
    lead = d["unresolved_locus_review"]
    assert lead["paper_locus"] == "orf19.1588" and lead["database_locus"] == "orf19.9161"
    assert lead["hit_count"] == 1 and lead["scope"] == "NAME_QUERY_NOT_ALIAS_OR_EXACT_ALLELE_PROOF"
    assert lead["curated"] is False
    doc = load_record(ROOT / "data/antibiotics/antifungal/fluconazole.yaml")
    claims = [c for c in doc["resistance_mechanisms"] if c.get("source") == "PHIBASE"
              and c["evidence"][0]["reference"] == "PMID:39403939"]
    assert len(claims) == 1 and len(claims[0]["evidence"]) == 2
    assert not any(k in claims[0] for k in ("protein_accession", "strain_taxon_id", "gene_id"))
    assert "protein_accession=UniProtKB:A0A1D8PGP5" in claims[0]["note"]
    assert "aliases of SDH8 reference locus C2_02620W_A, primary CGDID CAL0000192813" in claims[0]["note"]
    assert "not an experimental allele" in claims[0]["note"]
    assert "Grounding review huang-2024-parent-reference-context" in claims[0]["note"]
    assert all("PMID:39403939" not in {e["reference"] for e in a["evidence"]}
               for a in doc.get("activity_spectrum", []))


def test_fumigatus_dossier_separates_reference_and_clinical_project_context():
    dossier = json.loads((ROOT / "research/2026-10-08-fumigatus-reference-grounding.json").read_bytes())
    assert dossier["changes"] == {"new_scoped_claims": 17, "checksum_only_claims": 111}
    assert len(dossier["records"]) == 15 and len(dossier["primary_reviews"]) == 5
    assert len(dossier["pending_cohort_associations"]) == 9
    crosswalks = {x["uniprot_accession"]: x for x in dossier["reference_crosswalks"]}
    assert set(crosswalks) == {"Q4WNT5", "Q4WDM9"}
    for accession, locus in (("Q4WNT5", "AFUA_4G06890"), ("Q4WDM9", "AFUA_6G05300")):
        assert crosswalks[accession]["reference_locus"] == locus
        assert crosswalks[accession]["scope"] == "REFERENCE_ONLY_NOT_TESTED_SUBJECT"
        protein = dossier["proteins"][accession]
        assert set(protein) == {"primaryAccession", "entryType", "entryAudit", "organism", "genes",
                                "entry_object_sha256"}
        assert protein["organism"]["taxonId"] == 330879
    assert dossier["taxonomy"]["330879"]["parent"]["taxonId"] == 746128
    assert dossier["taxonomy"]["746128"]["rank"] == "species"
    literature = {r["reference"]: r for r in dossier["literature_access"]}
    project = literature["PMID:23226235"]["sequence_project"]
    assert project == {"accession": "ERP001097", "reported_by": "s2b",
                       "scope": "CLINICAL_STUDY_NOT_LATER_EXPERIMENTAL_SUBJECT",
                       "assigned_to_record": False}
    for pmid in set(FUMIGATUS_REFERENCES) - {"23226235"}:
        item = literature["PMID:" + pmid]
        assert item["primary_access"] == "PUBLISHER_HTML_INSPECTED_WITH_WEB_TOOL_NOT_CACHED"
        assert item["europe_pmc_open_access_flag"] == "N"
        assert "offline_verification_limit" in item and "fulltext_request" not in item


def fungicide_dossier():
    return json.loads((ROOT / "research/2026-10-08-iprodione-fludioxonil-grounding.json").read_bytes())


def test_fungicide_reference_crosswalks_keep_all_protein_alternatives():
    dossier = fungicide_dossier()
    crosswalks = {x["uniprot_accession"]: x for x in dossier["reference_crosswalks"]}
    assert set(crosswalks) == {"A0A384J5Y1", "W7LTW3", "W7LX41", "W7M468"}
    for accession, proteins in {
        "A0A384J5Y1": {"ATZ45931.1", "ATZ45933.1", "ATZ45935.1"},
        "W7LTW3": {"EWG38885.1", "EWG38886.1"},
        "W7LX41": {"EWG37117.1"},
        "W7M468": {"EWG42323.1", "EWG42324.1"},
    }.items():
        crosswalk = crosswalks[accession]
        assert crosswalk["scope"] == "REFERENCE_ONLY_NOT_TESTED_DERIVATIVE"
        assert {p["value"] for x in crosswalk["cross_references"] if x["database"] == "EMBL"
                for p in x["properties"] if p["key"] == "ProteinId"} == proteins
    for protein in dossier["proteins"].values():
        assert set(protein) == {"primaryAccession", "entryType", "entryAudit", "organism", "genes",
                                "entry_object_sha256"}
    for child, parent in (("332648", "40559"), ("334819", "117187")):
        assert dossier["taxonomy"][child]["rank"] == "strain"
        assert str(dossier["taxonomy"][child]["parent"]["taxonId"]) == parent
        assert dossier["taxonomy"][parent]["rank"] == "species"


def test_original_deposits_remain_separate_from_later_fungicide_subjects():
    deposits = fungicide_dossier()["original_deposit_crosswalks"]
    assert len(deposits) == 25
    assert len({d["uniprot_accession"] for d in deposits}) == 21
    assert {d["embl_cross_reference"]["id"] for d in deposits} == {
        "JX" + str(i) for i in range(192607, 192632)
    }
    for deposit in deposits:
        assert deposit["scope"] == "ORIGINAL_ISOLATE_NOT_LATER_B05_10_SUBJECT"
        assert deposit["strain_evidence"]["value"] != "B05.10"
        assert deposit["fragment_flag"] == (
            None if deposit["uniprot_accession"] == "J7JZS9" else "Fragment"
        )
        assert "protein_accession" not in deposit and "strain_taxon_id" not in deposit


def test_fungicide_dossier_does_not_promote_pending_studies_or_no_hit_query():
    dossier = fungicide_dossier()
    assert dossier["changes"] == {"new_scoped_claims": 11, "checksum_only_claims": 100}
    assert len(dossier["records"]) == 14 and len(dossier["primary_reviews"]) == 4
    assert {r["pmid"] for r in dossier["primary_reviews"]} == {"22912706", "41649761"}
    assert len(dossier["pending_associations"]) == 17
    assert {r["pmid"] for r in dossier["pending_associations"]} == {
        "17073308", "30686204", "38374637", "24903410", "22591226",
    }
    unresolved = dossier["unresolved_historical_reference"]
    assert unresolved["paper_accession"] == "BAB69486"
    assert unresolved["paper_version_scope"] == "UNVERSIONED"
    assert unresolved["result"] == "NO_HITS_IN_THIS_QUERY_NOT_PROTEIN_ABSENCE"
    assert unresolved["query_scope"] == "EXACT_VERSIONED_EMBL_XREF_QUERY_ONLY"


@pytest.mark.parametrize("name,total,activity_count", [
    ("fluconazole", 77, 2), ("itraconazole", 54, 0), ("voriconazole", 62, 3),
])
def test_rybak_reference_scope_preserves_subject_uncertainty_and_clinical_evidence(
    name, total, activity_count,
):
    doc = load_record(ROOT / f"data/antibiotics/antifungal/{name}.yaml")
    claims = [c for c in doc["resistance_mechanisms"]
              if c.get("source") == "PHIBASE" and c["evidence"][0]["reference"] == "PMID:28630186"]
    assert len(claims) == 2 and len(doc["resistance_mechanisms"]) == total
    assert doc["curation_status"] == "SEEDED"
    assert len(doc.get("activity_spectrum", [])) == activity_count
    assert all(a["evidence"][0]["reference"] != "PMID:28630186"
               for a in doc.get("activity_spectrum", []))
    by_taxon = {c["taxon_id"]: c for c in claims}
    assert set(by_taxon) == {"NCBITaxon:5476", "NCBITaxon:5480"}
    albicans, parapsilosis = by_taxon["NCBITaxon:5476"], by_taxon["NCBITaxon:5480"]
    assert albicans["strain"] == "SC5314" and albicans["gene_id"] == "C1_04770C_A-T"
    assert "parent background, not the tested deletion derivative" in albicans["note"]
    assert parapsilosis["strain"] == "Unknown strain" and "gene_id" not in parapsilosis
    assert "does not uniquely resolve either tested background" in parapsilosis["note"]
    assert "not the native clinical variant" in parapsilosis["note"]
    for claim, accession, taxon in ((albicans, "Q59VG6", "237561"),
                                    (parapsilosis, "G8B7T4", "578454")):
        assert "protein_accession" not in claim and "strain_taxon_id" not in claim
        assert f"protein_accession=UniProtKB:{accession}" in claim["note"]
        assert f"strain_taxon_id=NCBITaxon:{taxon}" in claim["note"]
        assert claim["alteration"] == "ERG3delta (deletion)"
        assert claim["mechanism_type"] == "UNKNOWN"
        assert claim["phenotype_label"] == f"resistance to {name}"
        assert claim["evidence"][-1]["reference"] == "DOI:10.1128/aac.00651-17"


@pytest.mark.parametrize("field", ["strain_taxon_id", "protein_accession", "gene_id"])
def test_source_identifier_mismatch_does_not_partially_mutate_the_claim(inputs, field):
    inventory, rows, path = inputs
    decisions = review.load_reviews(inventory, rows, path)
    row = next(r for r in rows if r["pmid"] == "8307980")
    item = {"strain_taxon_id": "NCBITaxon:559292", "protein_accession": "UniProtKB:P38637",
            "gene_id": "YIR011C_mRNA", "note": "Source association.", "evidence": []}
    item[field] = "unexpected"
    original = copy.deepcopy(item)
    with pytest.raises(ValueError, match="differs from reviewed source"):
        review.apply_review(item, row, decisions)
    assert item == original


def test_current_cycloheximide_does_not_assign_the_wrong_sts1_gene():
    doc = load_record(ROOT / "data/antibiotics/antifungal/cycloheximide.yaml")
    claims = [c for c in doc["resistance_mechanisms"] if c.get("source") == "PHIBASE"]
    assert len(claims) == 1 and len(doc["resistance_mechanisms"]) == 3
    claim = claims[0]
    assert doc["curation_status"] == "REVIEWED"
    assert claim["taxon_id"] == "NCBITaxon:4932"
    assert claim["strain"] == "YPH501"
    assert claim["mechanism_type"] == "UNKNOWN"
    assert claim["alteration"] == "STS1+ (wild type) [Overexpression]"
    assert claim["evidence"][0]["reference"] == "PMID:8307980"
    assert all(k not in claim for k in ("gene_id", "protein_accession", "strain_taxon_id"))
    assert "Historical STS1 denotes PDR5" in claim["note"]
    assert "Rejected misassigned source identifiers: protein_accession=UniProtKB:P38637;" in claim["note"]


@pytest.mark.parametrize("value", [None, True, [], {}, "", " ", " AF-B", "AF-B ", "AF\nB", "NRRL 3357"])
def test_invalid_subject_strain_fails_closed(inputs, value):
    inventory, rows, path = inputs
    document = json.loads(path.read_bytes())
    decision_for(document, "22314539")["subject_strain"] = value
    path.write_text(json.dumps(document))
    with pytest.raises(ValueError, match="subject strain"):
        review.load_reviews(inventory, rows, path)


def test_subject_change_cannot_keep_parent_strain_identifier(inputs):
    inventory, rows, path = inputs
    document = json.loads(path.read_bytes())
    decision_for(document, "22314539")["withhold"].remove("strain_taxon_id")
    path.write_text(json.dumps(document))
    with pytest.raises(ValueError, match="subject strain"):
        review.load_reviews(inventory, rows, path)


@pytest.mark.parametrize("strain", [None, "unreviewed subject"])
def test_subject_mismatch_is_atomic(inputs, strain):
    inventory, rows, path = inputs
    decisions = review.load_reviews(inventory, rows, path)
    row = next(r for r in rows if r["phig_id"] == "PHIG:336" and r["pmid"] == "22314539"
               and r["identifier"] == "CHEBI:10023")
    item = {"strain_taxon_id": "NCBITaxon:332952", "protein_accession": "UniProtKB:B8NFL5",
            "note": "Source association.", "evidence": []}
    if strain is not None:
        item["strain"] = strain
    original = copy.deepcopy(item)
    with pytest.raises(ValueError, match="strain differs"):
        review.apply_review(item, row, decisions)
    assert item == original


def test_current_voriconazole_separates_subjects_and_clinical_mic():
    doc = load_record(ROOT / "data/antibiotics/antifungal/voriconazole.yaml")
    claims = [c for c in doc["resistance_mechanisms"]
              if c["evidence"][0]["reference"] == "PMID:22314539"]
    assert len(doc["resistance_mechanisms"]) == 62 and len(claims) == 3
    assert {c["strain"] for c in claims} == {"AF-A", "AF-B", "AflavC-788"}
    assert {c["gene_id"]: c["strain"] for c in claims} == {
        "AFLA_001488_t1": "AF-A", "AFLA_005443_t1": "AF-B", "AFLA_010303_t1": "AflavC-788",
    }
    assert {c["taxon_id"] for c in claims} == {"NCBITaxon:5059"}
    assert all("protein_accession" not in c and "strain_taxon_id" not in c for c in claims)
    assert all(c["mechanism_type"] == "UNKNOWN" for c in claims)
    assert len(doc["activity_spectrum"]) == 3
    activity = doc["activity_spectrum"][0]
    assert set(activity) == {"taxon_id", "taxon_label", "strain", "activity", "mic_value",
                             "mic_units", "assay", "evidence"}
    assert activity["strain"] == "BMU29791" and activity["taxon_id"] == "NCBITaxon:5059"
    assert activity["activity"] == "RESISTANT"
    assert activity["mic_value"] == 8.0 and activity["mic_units"] == "mg/L"
    assert "CLSI M38-A2" in activity["assay"]
    assert activity["evidence"][0]["reference"] == "PMID:22314539"
    assert "historical" in activity["evidence"][0]["notes"]
    fresh = copy.deepcopy(doc)
    fresh.pop("activity_spectrum")
    fresh["resistance_mechanisms"] = [c for c in fresh["resistance_mechanisms"]
                                      if seed.is_card_sourced(c) or seed.is_phibase_sourced_resistance(c)]
    assert seed.merge_with_existing(fresh, doc) == doc


def test_current_flavus_claims_match_the_scoped_source_review():
    doc = load_record(ROOT / "data/antibiotics/antifungal/voriconazole.yaml")
    with INVENTORY.open() as handle:
        rows = [r for r in csv.DictReader(handle, delimiter="\t") if r["pmid"] == "18775650"]
    claims = [c for c in doc["resistance_mechanisms"] if c.get("source") == "PHIBASE"
              and c["evidence"][0]["reference"] == "PMID:18775650"]
    assert len(rows) == len(claims) == 5
    assert doc["curation_status"] == "SEEDED"
    for row, claim in zip(rows, claims, strict=True):
        assert claim["alteration"] == row["modification"]
        assert claim["gene_id"] == row["gene_id"]
        assert claim["strain"] == row["strain_label"]
        assert claim["taxon_id"] == "NCBITaxon:" + row["taxon_id"]
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim["mechanism_type"] == "UNKNOWN"
        assert all(k not in claim for k in ("protein_accession", "strain_taxon_id"))
        assert "susceptible parent" in claim["note"]
        assert "source coordinates remain unnormalized" in claim["note"]
        assert claim["evidence"][-1]["reference"] == "DOI:10.1016/j.ijantimicag.2008.06.018"


@pytest.mark.parametrize("slug,identifier,total", [
    ("caspofungin", "CHEBI:474180", 33),
    ("anidulafungin", "CHEBI:55346", 21),
    ("micafungin", "CHEBI:600520", 22),
])
def test_current_echinocandins_retain_parent_context_without_subject_accessions(slug, identifier, total):
    doc = load_record(ROOT / f"data/antibiotics/antifungal/{slug}.yaml")
    with INVENTORY.open() as handle:
        all_rows = list(csv.DictReader(handle, delimiter="\t"))
    rows = [r for r in all_rows if r["pmid"] == "16723566" and r["identifier"] == identifier]
    claims = [c for c in doc["resistance_mechanisms"]
              if c["evidence"][0]["reference"] == "PMID:16723566"]
    assert len(rows) == len(claims) == 8
    assert len(doc["resistance_mechanisms"]) == total
    assert doc["curation_status"] == "SEEDED" and not doc.get("activity_spectrum")
    assert [c["strain"] for c in claims].count("M70") == 5
    assert [c["strain"] for c in claims].count("SC5314") == 3
    for row, claim in zip(rows, claims, strict=True):
        assert claim["alteration"] == row["modification"]
        assert claim["strain"] == row["strain_label"]
        assert claim["taxon_id"] == "NCBITaxon:5476" and claim["taxon_label"] == "Candida albicans"
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim["mechanism_type"] == "UNKNOWN"
        assert all(k not in claim for k in ("protein_accession", "strain_taxon_id", "gene_id"))
        assert "parent background" in claim["note"]
        assert "UniProtKB:O13383 (CaFKS1; CAI4 reference), not an experimental allele" in claim["note"]
        assert "aggregated zygosity and grouped MICs" in claim["note"]
        assert claim["evidence"][-1]["reference"] == "DOI:10.1128/aac.01653-05"
    fresh = copy.deepcopy(doc)
    fresh["resistance_mechanisms"] = [c for c in fresh["resistance_mechanisms"]
                                      if not seed.is_phibase_sourced_resistance(c)]
    source_records = {r["identifier"]: {
        "identifier": r["identifier"],
        "chemical_structure": {"standard_inchi_key": r["standard_inchi_key"]},
        "curation_history": [],
    } for r in all_rows}
    source_records[identifier] = fresh
    seed.attach_phibase_resistance(source_records)
    assert fresh == doc


@pytest.mark.parametrize("slug,pmid,count,gene,taxon", [
    ("fluconazole", "25385095", 18, "C5_00660C_A-T", "5476"),
    ("itraconazole", "25385095", 1, "C5_00660C_A-T", "5476"),
    ("voriconazole", "25385095", 2, "C5_00660C_A-T", "5476"),
    ("caspofungin", "18443110", 1, "YLR342W_mRNA", "4932"),
    ("anidulafungin", "18443110", 1, "YLR342W_mRNA", "4932"),
    ("micafungin", "18443110", 1, "YLR342W_mRNA", "4932"),
])
def test_current_azole_and_yeast_claims_preserve_reference_and_subject_scope(slug, pmid, count, gene, taxon):
    doc = load_record(ROOT / f"data/antibiotics/antifungal/{slug}.yaml")
    with INVENTORY.open() as handle:
        rows = [r for r in csv.DictReader(handle, delimiter="\t")
                if r["identifier"] == doc["identifier"] and r["pmid"] == pmid]
    claims = [c for c in doc["resistance_mechanisms"] if c["evidence"][0]["reference"] == "PMID:" + pmid]
    assert len(rows) == len(claims) == count
    assert doc["curation_status"] == "SEEDED"
    for row, claim in zip(rows, claims, strict=True):
        assert claim["gene_id"] == row["gene_id"] == gene
        assert claim["taxon_id"] == "NCBITaxon:" + taxon
        assert claim["alteration"] == row["modification"]
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim["mechanism_type"] == "UNKNOWN"
        assert "protein_accession" not in claim and "strain_taxon_id" not in claim
        if pmid == "25385095":
            assert claim["strain"] == "SC5314"
            assert "reference ERG11 locus, not an exact experimental allele" in claim["note"]
            assert "combined genotype's effect to each component" in claim["note"]
        else:
            assert claim["strain"] == "BY4742-P649A"
            assert claim["alteration"] == "FKS1(P647A) (amino acid mutation) [Not assayed]"
            assert "discrepancy is preserved, not normalized" in claim["note"]
            assert "Original source background label: BY4742." in claim["note"]
            assert "whole-cell MICs and enzyme inhibition remain distinct" in claim["note"]
    if slug == "voriconazole":
        assert len(doc["activity_spectrum"]) == 3
        assert doc["activity_spectrum"][0]["strain"] == "BMU29791"
    elif slug == "fluconazole":
        assert len(doc["activity_spectrum"]) == 2
    else:
        assert not doc.get("activity_spectrum")


@pytest.mark.parametrize("name,count", [
    ("antifungal/fluconazole", 3), ("antifungal/voriconazole", 2), ("antibacterial/brefeldin-a", 1),
])
def test_current_eddouzi_source_claims_do_not_transfer_donor_identity(name, count):
    doc = load_record(ROOT / f"data/antibiotics/{name}.yaml")
    with INVENTORY.open() as handle:
        rows = [r for r in csv.DictReader(handle, delimiter="\t")
                if r["identifier"] == doc["identifier"] and r["pmid"] == "23629718"]
    claims = [c for c in doc["resistance_mechanisms"] if c.get("source") == "PHIBASE"
              and c["evidence"][0]["reference"] == "PMID:23629718"]
    assert len(rows) == len(claims) == count
    for row, claim in zip(rows, claims, strict=True):
        assert claim["strain"] == row["strain_label"]
        assert claim["taxon_id"] == "NCBITaxon:" + row["taxon_id"]
        assert claim["alteration"] == row["modification"]
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim["mechanism_type"] == "UNKNOWN"
        assert "protein_accession" not in claim and "strain_taxon_id" not in claim
        assert claim.get("gene_id", "") == row["gene_id"]
        assert "UniProtKB:" + row["protein_accession"] in claim["note"]
        assert claim["evidence"][-1]["reference"] == "DOI:10.1128/aac.00555-13"
        if row["protein_accession"] == "N0A5G3":
            assert claim["strain"] == "1909"
            assert "clinical donor JEY162" in claim["note"]
            assert "remains unresolved" in claim["note"]
    if name.endswith("brefeldin-a"):
        assert not doc.get("activity_spectrum")


@pytest.mark.parametrize("slug,values,total", [
    ("fluconazole", [(8.0, None, "RESISTANT"), (128.0, ">", "RESISTANT")], 77),
    ("voriconazole", [(0.0078, "<", None), (16.0, ">", "RESISTANT")], 62),
])
def test_current_eddouzi_clinical_observations_keep_qualifiers_and_cooccurrence(slug, values, total):
    doc = load_record(ROOT / f"data/antibiotics/antifungal/{slug}.yaml")
    observations = [a for a in doc["activity_spectrum"]
                    if a["evidence"][0]["reference"] == "PMID:23629718"]
    assert len(observations) == 2 and len(doc["resistance_mechanisms"]) == total
    assert [(a["strain"], a["taxon_id"]) for a in observations] == [
        ("JEY355", "NCBITaxon:5476"), ("JEY162", "NCBITaxon:5482"),
    ]
    for observation, (value, qualifier, call) in zip(observations, values, strict=True):
        assert observation["mic_value"] == value and observation["mic_units"] == "mg/L"
        assert observation.get("mic_qualifier") == qualifier and observation.get("activity") == call
        assert observation["assay"] == "EUCAST broth microdilution, source RPMI 1640 condition"
        assert "Table 3" in observation["evidence"][0]["notes"]
        assert "ug/mL" in observation["evidence"][0]["notes"]
        assert all(k not in observation for k in ("assembly_accession", "strain_taxon_id",
                                                  "biosample_accession", "sra_accessions"))
    claims = [c for c in doc["resistance_mechanisms"] if c.get("strain") == "JEY162"]
    assert len(claims) == 1
    claim = claims[0]
    assert claim["gene_families"] == ["ERG3"] and claim["alteration"] == "S258F"
    assert claim["protein_accession"] == "UniProtKB:N0A5G3"
    assert claim["taxon_id"] == "NCBITaxon:5482" and claim["mechanism_type"] == "UNKNOWN"
    assert all(k not in claim for k in ("source", "gene_id", "strain_taxon_id", "assembly_accession"))
    assert "not independent causality" in claim["note"] and "combined ERG3/ERG11" in claim["note"]
    assert claim["evidence"][0]["reference"] == "PMID:23629718"
    assert claim["evidence"][1]["reference"] == "UniProtKB:N0A5G3"
    assert "KC676662 / AGK44786.1" in claim["evidence"][1]["notes"]
    assert "no indexed PMID" in claim["evidence"][1]["notes"]
    fresh = copy.deepcopy(doc)
    fresh.pop("activity_spectrum")
    fresh["resistance_mechanisms"] = [c for c in fresh["resistance_mechanisms"]
                                      if seed.is_card_sourced(c) or seed.is_phibase_sourced_resistance(c)]
    assert seed.merge_with_existing(fresh, doc) == doc
