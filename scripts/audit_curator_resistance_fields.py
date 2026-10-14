"""Index resistance-claim fields offline without inferring biological identity."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

from seed_from_sources import is_card_sourced, is_phibase_sourced_resistance
from summarize_resistance_progress import current_records, digest, read_tsv

CENSUS = Path("research/2026-10-14-platen-archive-resistance-grounding.tsv")
CENSUS_SHA = "e9857e73bb7849b4752f21c768c706f67b6e977f5f3275e71a2976b75d5d4864"
OUTPUT = Path("research/2026-10-14-platen-archive-curator-resistance-fields.json")
SCOPE = "FIELD_AND_CITATION_INDEX_NOT_PRIMARY_REVIEW_OR_ALLELE_GROUNDING"
PATTERNS = {
    "UniProtKB": (r"(?:[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})"
                  r"(?:-[1-9][0-9]*)?"),
    "UniParc": r"UPI[0-9A-F]{10}",
    "NCBITaxon": r"[1-9][0-9]*",
    "PMID": r"[1-9][0-9]*",
    "DOI": r"10\.[0-9]{4,9}/\S+",
}


def normalize_reference(value):
    """Recognize explicit identifiers only; never dereference a URL or parse notes."""
    if any(character.isspace() or ord(character) < 32 for character in value):
        return None
    namespace, separator, identifier = value.partition(":")
    if separator and namespace in PATTERNS:
        if re.fullmatch(PATTERNS[namespace], identifier):
            return {"namespace": namespace, "identifier": f"{namespace}:{identifier}"}
        return None
    try:
        url = urlsplit(value)
        if (url.scheme not in {"https", "http"} or url.username is not None or url.password is not None
                or url.port is not None or url.query or url.fragment):
            return None
    except ValueError:
        return None
    parts = unquote(url.path).strip("/").split("/")
    namespace = None
    identifier = ""
    if url.hostname in {"doi.org", "dx.doi.org"}:
        namespace, identifier = "DOI", unquote(url.path).removeprefix("/")
    elif (url.hostname in {"www.uniprot.org", "uniprot.org", "rest.uniprot.org"}
          and len(parts) in {2, 3} and (len(parts) == 2 or parts[2] == "entry")):
        namespace = {"uniprotkb": "UniProtKB", "uniprot": "UniProtKB",
                     "uniparc": "UniParc", "taxonomy": "NCBITaxon"}.get(parts[0])
        identifier = parts[1].removesuffix(".json")
    if namespace and re.fullmatch(PATTERNS[namespace], identifier):
        return {"namespace": namespace, "identifier": f"{namespace}:{identifier}"}
    return None


def owner(claim):
    card, phi = is_card_sourced(claim), is_phibase_sourced_resistance(claim)
    if card and phi:
        raise ValueError("conflicting resistance ownership")
    if claim.get("source") not in {None, "PHIBASE"}:
        raise ValueError("unhandled resistance source")
    return "CARD" if card else "PHIBASE" if phi else "CURATOR"


def project_claim(record, index, claim):
    if owner(claim) != "CURATOR":
        raise ValueError("not a curator claim")
    citations = []
    unclassified = []
    for position, evidence in enumerate(claim.get("evidence", [])):
        value = evidence["reference"]
        parsed = normalize_reference(value)
        item = {"evidence_index": position, "reference_sha256": digest(value.encode())}
        if parsed:
            citations.append({**item, **parsed})
        else:
            unclassified.append(item)
    families, gene = bool(claim.get("gene_families")), bool(claim.get("gene_id"))
    state = ("BOTH_FIELDS" if families and gene else "GENE_ID_ONLY" if gene
             else "GENE_FAMILIES_ONLY" if families else "NEITHER_FIELD")
    protein = claim.get("protein_accession")
    if protein:
        parsed = normalize_reference(protein)
        if not parsed or parsed["namespace"] != "UniProtKB" or parsed["identifier"] != protein:
            raise ValueError("unrecognized protein accession slot")
    return {
        "record_identifier": record["identifier"], "record_path": record["path"],
        "record_sha256": record["sha256"], "standard_inchi_key": record["standard_inchi_key"],
        "resistance_index": index,
        "claim_sha256": digest(json.dumps(claim, sort_keys=True, ensure_ascii=True).encode()),
        "owner": "CURATOR", "gene_field_state": state,
        "gene_family_label_count": len(claim.get("gene_families", [])),
        "protein_accession_slot": protein,
        "taxon_id_slot": claim.get("taxon_id"),
        "strain_taxon_id_slot": claim.get("strain_taxon_id"),
        "taxon_label_present": bool(claim.get("taxon_label")),
        "strain_label_present": bool(claim.get("strain")),
        "alteration_present": bool(claim.get("alteration")),
        "evidence_count": len(claim.get("evidence", [])),
        "recognized_citations": citations, "unclassified_citations": unclassified,
        "experimental_identity_assessed_by_this_index": False,
    }


def summarize(claims):
    namespaces = Counter()
    accessions = set()
    for claim in claims:
        namespaces.update({r["namespace"] for r in claim["recognized_citations"]})
        accessions.update(r["identifier"] for r in claim["recognized_citations"]
                          if r["namespace"] == "UniProtKB")
    return {
        "curator_claims": len(claims),
        "curator_records": len({r["record_identifier"] for r in claims}),
        "gene_field_states": dict(sorted(Counter(r["gene_field_state"] for r in claims).items())),
        "claims_with_protein_accession_slot": sum(bool(r["protein_accession_slot"]) for r in claims),
        "claims_with_taxon_id_slot": sum(bool(r["taxon_id_slot"]) for r in claims),
        "claims_with_strain_taxon_id_slot": sum(bool(r["strain_taxon_id_slot"]) for r in claims),
        "claims_with_taxon_label_but_no_taxon_id": sum(
            r["taxon_label_present"] and not r["taxon_id_slot"] for r in claims),
        "claims_without_taxon_label_or_id": sum(
            not r["taxon_label_present"] and not r["taxon_id_slot"] for r in claims),
        "claims_citing_each_namespace": dict(sorted(namespaces.items())),
        "distinct_cited_uniprot_accessions": len(accessions),
        "claims_with_unclassified_citations": sum(bool(r["unclassified_citations"]) for r in claims),
    }


def build(root):
    payload = (root / CENSUS).read_bytes()
    if digest(payload) != CENSUS_SHA:
        raise ValueError("census changed; create a successor checkpoint")
    records, _ = current_records(root, read_tsv(payload))
    ownership, claims = Counter(), []
    for identifier in sorted(records):
        record = records[identifier]
        for index, claim in enumerate(record["resistance_mechanisms"]):
            source = owner(claim)
            ownership[source] += 1
            if source == "CURATOR":
                claims.append(project_claim(record, index, claim))
    return {
        "schema_version": 1, "scope": SCOPE,
        "census": {"path": str(CENSUS), "sha256": CENSUS_SHA},
        "generator": {"path": "scripts/audit_curator_resistance_fields.py",
                      "sha256": digest(Path(__file__).read_bytes())},
        "summary": {"corpus_records_checked": len(records),
                    "resistance_claims_by_owner": dict(sorted(ownership.items())),
                    **summarize(claims)},
        "claims": claims,
        "limits": {
            "network_requests": 0, "ncbi_requests": 0, "issue_1040": "DEFERRED",
            "biological_record_changes": 0, "new_primary_reviews": 0,
            "experimental_allele_assignments": 0, "experimental_genome_assignments": 0,
            "numeric_AST_or_variant_specifications_exported": False,
            "gene_values_and_claim_prose_exported": False,
            "notes_mined_for_identifiers": False,
        },
        "interpretation": [
            "Gene identifiers and gene-family labels are distinct optional fields, not completeness gates.",
            "Neither field may be appropriate for operon-level or unresolved historical claims.",
            "A recognized citation is syntactic indexing, not verified gene, allele or subject grounding.",
            "UniParc references remain separate from UniProtKB protein accessions.",
            "Protein and taxon slots are reported as stored, not endorsed as experimental identities.",
            "Citation counts are per claim; repeated references are not independent experiments.",
            "No citation does not mean no reference grounding: notes and external dossiers are not mined.",
            "Primary citation presence does not establish primary-evidence review or chemical identity.",
            "Taxon absence may reflect biochemical or route-level scope; inspect evidence before filling it.",
            "Existing paper dossiers and unresolved holds remain authoritative; no source is retried.",
            "No whole-record primary signoff or claim of exhaustive biological coverage is made.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    result = build(args.root)
    path = args.root / args.output
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if path.exists() and path.read_bytes() != payload:
        raise ValueError("refusing to replace a historical checkpoint")
    if not path.exists():
        path.write_bytes(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
