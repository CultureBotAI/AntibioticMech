"""Append reference-only citations without changing resistance subject identity.

All inputs are local, pinned research snapshots. Historical replay removes only
the exact append-only citation delta and verifies the complete original bytes.
"""

import copy
import datetime
import hashlib
import json

from audit_curator_resistance_fields import normalize_reference, owner

from antibioticmech.validation.write_validated import emit_antibiotic_yaml


def digest(value):
    return hashlib.sha256(value).hexdigest()


def claim_digest(claim):
    return digest(json.dumps(claim, sort_keys=True, ensure_ascii=True).encode())


def reference_metadata(receipt, expected, gene, accession):
    """Require a complete, versioned response and a unique exact gene match."""
    if any(receipt.get(key) != expected[key] for key in ("url", "sha256", "retrieved_at", "status")):
        raise ValueError("reference receipt identity changed")
    if receipt["status"] != 200 or digest(receipt["body"].encode()) != receipt["sha256"]:
        raise ValueError("reference response status or body checksum changed")
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    release = headers.get("x-uniprot-release")
    if release != "2026_03" or headers.get("link"):
        raise ValueError("reference release changed or query incomplete")
    body = json.loads(receipt["body"])
    if not isinstance(body, dict) or not isinstance(body.get("results"), list):
        raise ValueError("reference results must be an array")
    results = body["results"]
    if not all(isinstance(entry, dict) for entry in results):
        raise ValueError("reference results must contain objects")
    if str(len(results)) != headers.get("x-total-results"):
        raise ValueError("reference result count changed")
    matches = [entry for entry in results if entry.get("primaryAccession") == accession]
    if len(matches) != 1:
        raise ValueError("reference accession missing or ambiguous")
    entry = matches[0]
    if any(key in entry for key in ("sequence", "features", "comments")):
        raise ValueError("unexpected operational annotation in reference response")
    genes = [g.get("geneName", {}).get("value") for g in entry.get("genes", [])]
    if genes != [gene]:
        raise ValueError("reference gene identity changed")
    versions = entry["entryAudit"]
    if any(type(versions.get(k)) is not int or versions[k] < 1 for k in ("entryVersion", "sequenceVersion")):
        raise ValueError("invalid reference versions")
    if entry["entryType"] not in {"UniProtKB reviewed (Swiss-Prot)", "UniProtKB unreviewed (TrEMBL)"}:
        raise ValueError("invalid reference review status")
    taxon = entry["organism"]["taxonId"]
    if type(taxon) is not int or taxon < 1:
        raise ValueError("invalid reference taxon")
    return {
        "accession": f"UniProtKB:{accession}",
        "gene": gene,
        "entry_type": entry["entryType"],
        "entry_version": versions["entryVersion"],
        "sequence_version": versions["sequenceVersion"],
        "reference_taxon_id": f"NCBITaxon:{taxon}",
        "release": release,
        "retrieved_on": receipt["retrieved_at"][:10],
        "scope": "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE",
    }


def citation(reference):
    if (
        reference.get("scope") != "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE"
        or reference.get("release") != "2026_03"
    ):
        raise ValueError("reference scope or release changed")
    parsed = normalize_reference(reference["accession"])
    taxon = normalize_reference(reference["reference_taxon_id"])
    if (
        not parsed
        or parsed["namespace"] != "UniProtKB"
        or parsed["identifier"] != reference["accession"]
        or not taxon
        or taxon["namespace"] != "NCBITaxon"
        or taxon["identifier"] != reference["reference_taxon_id"]
    ):
        raise ValueError("invalid reference identifiers")
    if (
        reference.get("entry_type")
        not in {"UniProtKB reviewed (Swiss-Prot)", "UniProtKB unreviewed (TrEMBL)"}
        or any(
            type(reference.get(key)) is not int or reference[key] < 1
            for key in ("entry_version", "sequence_version")
        )
        or not isinstance(reference.get("gene"), str)
        or not reference["gene"].strip()
    ):
        raise ValueError("invalid reference metadata")
    datetime.date.fromisoformat(reference["retrieved_on"])
    accession = parsed["identifier"].split(":", 1)[1]
    return {
        "reference": f"https://www.uniprot.org/uniprotkb/{accession}/entry",
        "notes": (
            f"Reference-only {reference['accession']} ({reference['gene']}); "
            f"{reference['entry_type']}, entry version {reference['entry_version']}, "
            f"sequence version {reference['sequence_version']}, release {reference['release']}; "
            f"retrieved {reference['retrieved_on']}. Reference organism "
            f"{reference['reference_taxon_id']}, not an experimental subject assignment. "
            "Not an exact tested allele, altered protein, strain or genome identifier, "
            "and not independent phenotype or mechanism evidence. A component reference "
            "does not assign the effect of a combined genotype to that component. "
            "UniProt Consortium, CC BY 4.0."
        ),
    }


def add_citations(record, plan):
    """Return an evidence-only copy; fail closed on ownership or claim drift."""
    if (
        record["identifier"] != plan["identifier"]
        or record["chemical_structure"]["standard_inchi_key"] != plan["standard_inchi_key"]
    ):
        raise ValueError("record identity changed")
    if digest(emit_antibiotic_yaml(record).encode()) != plan["before"]["sha256"]:
        raise ValueError("record baseline changed")
    indices = [e["resistance_index"] for e in plan["edits"]]
    if not indices or len(set(indices)) != len(indices):
        raise ValueError("empty or duplicate citation edit")
    after = copy.deepcopy(record)
    for edit in plan["edits"]:
        index = edit["resistance_index"]
        if type(index) is not int or not 0 <= index < len(after["resistance_mechanisms"]):
            raise ValueError("invalid resistance index")
        claim = after["resistance_mechanisms"][index]
        if claim_digest(claim) != edit["before_claim_sha256"] or owner(claim) != "CURATOR":
            raise ValueError("claim content or ownership changed")
        if claim.get("protein_accession") or not claim.get("taxon_id"):
            raise ValueError("unexpected experimental identity context")
        refs = edit["references"]
        if not refs or len({r["accession"] for r in refs}) != len(refs):
            raise ValueError("empty or duplicate reference proteins")
        if {r["gene"] for r in refs} != set(claim.get("gene_families", [])):
            raise ValueError("reference genes do not match the bounded claim")
        existing = {e["reference"] for e in claim["evidence"]}
        if edit["primary_reference"] not in existing:
            raise ValueError("primary citation missing")
        parsed = [normalize_reference(value) for value in existing]
        if any(p and p["identifier"] in {r["accession"] for r in refs} for p in parsed):
            raise ValueError("reference citation already present")
        claim["evidence"].extend(citation(r) for r in refs)
    return after


def restore_before(record, receipt):
    """Recover an exact archival record from a pinned append-only delta."""
    if not isinstance(record, dict):
        raise ValueError("historical replay requires a record object")
    if digest(emit_antibiotic_yaml(record).encode()) != receipt["after"]["sha256"]:
        raise ValueError("historical replay requires the pinned successor record")
    before = copy.deepcopy(record)
    if before["curation_history"][-1] != receipt["curation_event"]:
        raise ValueError("historical curation event changed")
    before["curation_history"].pop()
    for edit in receipt["edits"]:
        claim = before["resistance_mechanisms"][edit["resistance_index"]]
        added = [citation(r) for r in edit["references"]]
        if not added or claim["evidence"][-len(added) :] != added:
            raise ValueError("historical citation tail changed")
        del claim["evidence"][-len(added) :]
        if claim_digest(claim) != edit["before_claim_sha256"]:
            raise ValueError("historical claim checksum changed")
    if digest(emit_antibiotic_yaml(before).encode()) != receipt["before"]["sha256"]:
        raise ValueError("historical record checksum changed")
    return before
