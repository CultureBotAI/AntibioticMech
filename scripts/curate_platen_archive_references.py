"""Append bounded donor-archive context, never an experimental protein assignment."""

import copy
import json

import audit_platen_archives as archives
import audit_topoisomerase_references as reference
from audit_curator_resistance_fields import normalize_reference, owner
from resistance_reference_citations import claim_digest, digest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import emit_antibiotic_yaml

DOSSIER = {
    "path": "research/2026-10-14-platen-archive-context.json",
    "sha256": "3d4de3b458ec34ce3e98e12e056ccd63b577d0d650687a4fed3c16033f4419cc",
}
PLAN = "research/2026-10-14-platen-archive-curation-plan.json"
RECEIPT = "research/2026-10-14-platen-archive-curation.json"
NOTE = (
    " Donor-archive update (2026-10-14): the accepted manuscript's accession statement "
    "links MA7327 fabF to KF543053. Sequence-free ENA metadata explicitly links "
    "EMBL:KF543053.1 to EMBL:AHA90851.1; the parent record supplies Streptomyces platensis "
    "MA7327 and species NCBITaxon:58346. UniParc:UPI0003C98D16 links that EMBL protein "
    "to historical UniProtKB:V5NR11 (UniProtKB/TrEMBL cross-reference version 1, "
    "inactive in UniProt release 2026_03). This updates the preceding unresolved "
    "reference-search statement, not the experimental identity. No active current "
    "UniProtKB mapping is established. The donor reference is not the tested host "
    "Streptomyces albidoflavus SB12013, an exact tested allele, or a genome; no protein "
    "accession, strain TaxID or genome is assigned. The original phenotype, mechanism "
    "and primary-review limitations remain unchanged. Archive membership is not "
    "independent resistance evidence."
)


def evidence():
    urls = archives.urls()
    return [
        {
            "reference": urls["archive-fabF"][1],
            "notes": (
                "EMBL-EBI ENA coding metadata, retrieved 2026-10-14: the explicit "
                "parent KF543053 has protein AHA90851.1, product FabF, strain MA7327. "
                "The coding row's gene, scientific_name and tax_id fields are blank; "
                "gene identity follows the primary accession statement, not a filled-in "
                "coding annotation. Donor reference only, not tested-allele identity."
            ),
        },
        {
            "reference": urls["parent-archives"][1],
            "notes": (
                "EMBL-EBI ENA parent metadata, retrieved 2026-10-14: the KF543053 "
                "row (sequence version 1) names Streptomyces platensis MA7327, TaxID "
                "58346; last updated 2014-05-15. Joined by the coding row's explicit "
                "parent_accession, not name similarity. KF543054 is the separate FabH "
                "comparison, not evidence for a positive FabF claim. A gene archive "
                "is not a whole genome or a strain TaxID."
            ),
        },
        {
            "reference": urls["uniparc-UPI0003C98D16"][1],
            "notes": (
                "UniProt Consortium, CC BY 4.0; release 2026_03, retrieved 2026-10-14. "
                "UniParc:UPI0003C98D16 has explicit EMBL AHA90851 version 1 (active) "
                "and UniProtKB/TrEMBL V5NR11 version 1 (inactive) cross-references, "
                "both with species NCBITaxon:58346. The historical UniProtKB row's "
                "lastUpdated 2026-01-28 is not asserted to be its inactivation date. "
                "This is a donor archive crosswalk, not an active UniProtKB entry, "
                "experimental allele assignment, or independent phenotype evidence."
            ),
        },
    ]


def make_plan(root):
    dossier = json.loads(reference.check_pin(root, DOSSIER).read_bytes())
    if archives.build(root) != dossier:
        raise ValueError("native archive evidence does not reproduce")
    rows = []
    for row in dossier["records"]:
        doc = load_record(reference.check_pin(root, row["snapshot"]))
        rows.append(
            {
                "identifier": row["identifier"],
                "standard_inchi_key": row["standard_inchi_key"],
                "before": row["record"],
                "snapshot": row["snapshot"],
                "resistance_index": 1,
                "before_claim_sha256": claim_digest(doc["resistance_mechanisms"][1]),
            }
        )
    return {"scope": "DONOR_ARCHIVE_REFERENCE_ONLY", "dossier": DOSSIER, "records": rows}


def add_reference(record, plan):
    identifier = record.get("identifier")
    if (
        identifier not in archives.STRUCTURES
        or plan["identifier"] != identifier
        or record["chemical_structure"]["standard_inchi_key"] != archives.STRUCTURES[identifier]
        or plan["standard_inchi_key"] != archives.STRUCTURES[identifier]
    ):
        raise ValueError("record identity changed")
    if digest(emit_antibiotic_yaml(record).encode()) != plan["before"]["sha256"]:
        raise ValueError("record baseline changed")
    if type(plan["resistance_index"]) is not int or plan["resistance_index"] != 1:
        raise ValueError("unplanned resistance index")
    claim = record["resistance_mechanisms"][1]
    if (
        claim_digest(claim) != plan["before_claim_sha256"]
        or owner(claim) != "CURATOR"
        or claim.get("gene_families") != ["fabF"]
        or claim.get("taxon_id") != "NCBITaxon:1886"
        or claim.get("taxon_label") != "Streptomyces albidoflavus"
        or claim.get("strain") != "SB12013"
        or claim.get("protein_accession")
        or claim.get("strain_taxon_id")
        or not isinstance(claim.get("note"), str)
        or not claim["note"]
    ):
        raise ValueError("claim content, ownership or subject context changed")
    refs = {e["reference"] for e in claim["evidence"]}
    parsed = [normalize_reference(value) for value in refs]
    if (
        "PMID:24560608" not in refs
        or any(e["reference"] in refs for e in evidence())
        or any(p and p["identifier"] in {"UniParc:UPI0003C98D16", "UniProtKB:V5NR11"} for p in parsed)
        or NOTE in claim["note"]
    ):
        raise ValueError("primary citation missing or archive reference already present")
    after = copy.deepcopy(record)
    after["resistance_mechanisms"][1]["note"] += NOTE
    after["resistance_mechanisms"][1]["evidence"].extend(evidence())
    return after


def restore_before(record, receipt):
    if digest(emit_antibiotic_yaml(record).encode()) != receipt["after"]["sha256"]:
        raise ValueError("historical replay requires pinned successor")
    before = copy.deepcopy(record)
    if before["curation_history"][-1] != receipt["curation_event"]:
        raise ValueError("historical curation event changed")
    before["curation_history"].pop()
    claim = before["resistance_mechanisms"][1]
    if not claim["note"].endswith(NOTE) or claim["evidence"][-3:] != evidence():
        raise ValueError("historical archive delta changed")
    claim["note"] = claim["note"][: -len(NOTE)]
    del claim["evidence"][-3:]
    if (
        claim_digest(claim) != receipt["before_claim_sha256"]
        or digest(emit_antibiotic_yaml(before).encode()) != receipt["before"]["sha256"]
    ):
        raise ValueError("historical record checksum changed")
    return before
