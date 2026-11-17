#!/usr/bin/env python3
"""Build and save the structured batch review for the 21 AntibioticMech MINTED records
matching 3-star ChEBI outside the antimicrobial role subtree via CAS Common Chemistry
InChIKey bridging.

Purpose:
  Produces and saves `reviews/structured/20261111T060500Z-cas-chebi-grounding-candidates-batch-review`
  using `scripts/record_review.py` (`save_review`). Documents:
    1. The 19 non-colliding MINTED records (`9` `CURATOR_XREF_READY` in `curation/curator_antibiotics.tsv`
       and `10` `DECISION_NEEDS_INVENTORY_EXTRACT` in `curation/decisions.tsv`) verified to match
       3-star ChEBI (`CC BY 4.0`) by exact Standard InChIKey agreement
       (`corpus_inchikey == cas_inchikey == chebi_inchikey`).
    2. The 2 shared-InChIKey congener collision records (`gramicidin S` `ARO:3000200` and
       `gramicidin C` `ARO:3000224`, both carrying `PubChem:73357` `IUAYMJGZBVDSGL-XNNAEKOYSA-N`)
       classified as `HOLD_CONGENER_COLLISION` because grounding `gramicidin S` to `CHEBI:5530`
       causes `seed_from_sources.py` to fold `gramicidin C` (linear pentadecapeptide) into
       `CHEBI:5530` (cyclic decapeptide) until `gramicidin C`'s upstream `PubChem:73357`
       collision is resolved.
    3. Why promotion of the 19 `MINTED` records to `EXACT` (`CHEBI:*`) is staged for the
       next `extract_source_inventory.py` + `seed_from_sources.py` + historical-fixture-transition
       cycle (`research/2026-10-15-card-reference-reconciled.json` and `tests/conftest.py`
       pin the current `antibioticmech:aro-*` / `antibioticmech:curator-*` identifiers and
       file SHA-256 digests).

Inputs:
  - `data/antibiotics/PATHS.tsv` and the 21 target YAML files
  - `scripts/evaluate_cas_common_chemistry.py`
  - `scripts/extract_source_inventory.py`
  - `scripts/seed_from_sources.py`
  - `curation/decisions.tsv`
  - `curation/curator_antibiotics.tsv`
  - `research/2026-10-15-card-reference-reconciled.json`

Outputs:
  - `reviews/structured/20261111T060500Z-cas-chebi-grounding-candidates-batch-review/review.yaml`
  - `reviews/structured/20261111T060500Z-cas-chebi-grounding-candidates-batch-review/review.md`

Date: 2026-11-11
"""

from __future__ import annotations

import csv
import os
import sys
from pathlib import Path

os.environ.setdefault("PYSTOW_HOME", "/tmp/pystow")

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import record_review  # noqa: E402

CANDIDATE_SPECS = [
    # (identifier, label, chebi_id, chebi_name, inchikey, action)
    (
        "antibioticmech:aro-0734abf918",
        "gramicidin S",
        "CHEBI:5530",
        "gramicidin S",
        "IUAYMJGZBVDSGL-XNNAEKOYSA-N",
        "HOLD_CONGENER_COLLISION",
    ),
    (
        "antibioticmech:aro-bf39ac682c",
        "gramicidin C",
        "CHEBI:5530",
        "gramicidin S",
        "IUAYMJGZBVDSGL-XNNAEKOYSA-N",
        "HOLD_CONGENER_COLLISION",
    ),
    (
        "antibioticmech:aro-11ab0a98bf",
        "miconazole",
        "CHEBI:82892",
        "1-[2-(2,4-dichlorobenzyloxy)-2-(2,4-dichlorophenyl)ethyl]imidazole",
        "BYBLEWFAAKGYCD-UHFFFAOYSA-N",
        "DECISION_NEEDS_INVENTORY_EXTRACT",
    ),
    (
        "antibioticmech:aro-1224dc3554",
        "oxpoconazole",
        "CHEBI:83837",
        "{2-[3-(4-chlorophenyl)propyl]-2,4,4-trimethyl-1,3-oxazolidin-3-yl}(imidazol-1-yl)methanone",
        "FJBGIXKIXPUXBY-UHFFFAOYSA-N",
        "DECISION_NEEDS_INVENTORY_EXTRACT",
    ),
    (
        "antibioticmech:aro-14f45eb5b3",
        "myclobutanil",
        "CHEBI:83729",
        "2-(4-chlorophenyl)-2-(1H-1,2,4-triazol-1-ylmethyl)hexanenitrile",
        "HZJKXKUJVSEEFU-UHFFFAOYSA-N",
        "DECISION_NEEDS_INVENTORY_EXTRACT",
    ),
    (
        "antibioticmech:aro-2e3b34cc67",
        "tacrolimus",
        "CHEBI:61049",
        "tacrolimus (anhydrous)",
        "QJJXYPPXXYFBGM-LFZNUXCKSA-N",
        "DECISION_NEEDS_INVENTORY_EXTRACT",
    ),
    (
        "antibioticmech:aro-2eea3233f3",
        "ofloxacin",
        "CHEBI:194135",
        (
            "9-fluoro-3-methyl-10-(4-methylpiperazin-1-yl)-7-oxo-2,3-dihydro-7H-"
            "[1,4]oxazino[2,3,4-ij]quinoline-6-carboxylic acid"
        ),
        "GSDSWSVVBLHKDQ-UHFFFAOYSA-N",
        "DECISION_NEEDS_INVENTORY_EXTRACT",
    ),
    (
        "antibioticmech:aro-5fd4e54f15",
        "isopyrazam",
        "CHEBI:83128",
        "3-(difluoromethyl)-N-(9-isopropyl-1,2,3,4-tetrahydro-1,4-methanonaphthalen-5-yl)-1-methylpyrazole-4-carboxamide",
        "XTDZGXBTXBEZDN-UHFFFAOYSA-N",
        "DECISION_NEEDS_INVENTORY_EXTRACT",
    ),
    (
        "antibioticmech:aro-a441fc6b50",
        "prothioconazole",
        "CHEBI:84008",
        "2-[2-(1-chlorocyclopropyl)-3-(2-chlorophenyl)-2-hydroxypropyl]-1,2-dihydro-1,2,4-triazole-3-thione",
        "MNHVNIJQQRJYDH-UHFFFAOYSA-N",
        "DECISION_NEEDS_INVENTORY_EXTRACT",
    ),
    (
        "antibioticmech:aro-adaab5b65b",
        "mebendazole",
        "CHEBI:6704",
        "mebendazole",
        "OPXLLQIJSORQAM-UHFFFAOYSA-N",
        "DECISION_NEEDS_INVENTORY_EXTRACT",
    ),
    (
        "antibioticmech:aro-c1dea01a87",
        "imazalil",
        "CHEBI:83829",
        "1-[2-(allyloxy)-2-(2,4-dichlorophenyl)ethyl]imidazole",
        "PZBPKYOVPCNPJY-UHFFFAOYSA-N",
        "DECISION_NEEDS_INVENTORY_EXTRACT",
    ),
    (
        "antibioticmech:aro-e05d19b916",
        "econazole",
        "CHEBI:82873",
        "1-{2-(4-chlorobenzyloxy)-2-(2,4-dichlorophenyl)ethyl}imidazole",
        "LEZWWPYKPKIXLL-UHFFFAOYSA-N",
        "DECISION_NEEDS_INVENTORY_EXTRACT",
    ),
    (
        "antibioticmech:curator-35c6404d6e",
        "Isoorientin",
        "CHEBI:17965",
        "isoorientin",
        "ODBRNZZJSYPIDI-VJXVFPJBSA-N",
        "CURATOR_XREF_READY",
    ),
    (
        "antibioticmech:curator-59edbdc708",
        "Rutin",
        "CHEBI:28527",
        "rutin",
        "IKGXIBQEEMLURG-NVPNHPEKSA-N",
        "CURATOR_XREF_READY",
    ),
    (
        "antibioticmech:curator-68713b9d28",
        "Fisetin",
        "CHEBI:42567",
        "fisetin",
        "XHEFDIBZLJXQHF-UHFFFAOYSA-N",
        "CURATOR_XREF_READY",
    ),
    (
        "antibioticmech:curator-9412b5ca77",
        "5-indanol",
        "CHEBI:59311",
        "indan-5-ol",
        "PEHSSTUGJUBZBI-UHFFFAOYSA-N",
        "CURATOR_XREF_READY",
    ),
    (
        "antibioticmech:curator-b453af7884",
        "Hispidulin",
        "CHEBI:75902",
        "hispidulin",
        "IHFBPDAQLQOCBX-UHFFFAOYSA-N",
        "CURATOR_XREF_READY",
    ),
    (
        "antibioticmech:curator-c27816fecf",
        "Vitexin",
        "CHEBI:16954",
        "vitexin",
        "SGEWCQFRYRRZDC-VPRICQMDSA-N",
        "CURATOR_XREF_READY",
    ),
    (
        "antibioticmech:curator-d33759f162",
        "Cladribine",
        "CHEBI:567361",
        "cladribine",
        "PTOAARAWEBMLNO-KVQBGUIXSA-N",
        "CURATOR_XREF_READY",
    ),
    (
        "antibioticmech:curator-d604421a09",
        "Luteolin",
        "CHEBI:15864",
        "luteolin",
        "IQPNAANSBPBGFQ-UHFFFAOYSA-N",
        "CURATOR_XREF_READY",
    ),
    (
        "antibioticmech:curator-ee3df8bfee",
        "Orientin",
        "CHEBI:7781",
        "orientin",
        "PLAPMLGJVGLZOV-VPRICQMDSA-N",
        "CURATOR_XREF_READY",
    ),
]


def discover_candidates() -> list[dict[str, str]]:
    """Resolve the 21 candidate records directly via `data/antibiotics/PATHS.tsv`."""
    with (REPO_ROOT / "data/antibiotics/PATHS.tsv").open(encoding="utf-8", newline="") as fh:
        slug_by_id = {row["identifier"]: row["slug"] for row in csv.DictReader(fh, delimiter="\t")}

    out: list[dict[str, str]] = []
    for identifier, label, chebi_id, chebi_name, inchikey, action in CANDIDATE_SPECS:
        slug = slug_by_id[identifier]
        matches = sorted((REPO_ROOT / "data/antibiotics").glob(f"*/{slug}.yaml"))
        if not matches:
            raise FileNotFoundError(f"No YAML file for {identifier} ({slug})")
        rel = matches[0].relative_to(REPO_ROOT).as_posix()
        out.append(
            {
                "identifier": identifier,
                "path": rel,
                "label": label,
                "chebi_id": chebi_id,
                "chebi_name": chebi_name,
                "inchikey": inchikey,
                "action": action,
            }
        )
    return out


def build_review_dict() -> dict:
    candidates = discover_candidates()
    targets = [
        {
            "target_id": c["identifier"],
            "path": c["path"],
            "label": c["label"],
            "record_class": "AntibioticRecord",
            "kind": "maintained",
            "owner_paths": [
                {
                    "repository": "CultureBotAI/AntibioticMech",
                    "path": c["path"],
                    "role": "Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding",
                },
                {
                    "repository": "CultureBotAI/AntibioticMech",
                    "path": (
                        "curation/curator_antibiotics.tsv"
                        if c["action"] == "CURATOR_XREF_READY"
                        else "curation/decisions.tsv"
                    ),
                    "role": (
                        "Curator grounding overlay consumed by extract_source_inventory.py "
                        "and seed_from_sources.py"
                    ),
                },
            ],
        }
        for c in candidates
    ]
    extra_inputs = [
        ".claude/skills/review-yaml-record/SKILL.md",
        "curation/curator_antibiotics.tsv",
        "curation/decisions.tsv",
        "research/2026-10-15-card-reference-reconciled.json",
        "scripts/extract_source_inventory.py",
        "scripts/seed_from_sources.py",
        "tests/conftest.py",
    ]
    inspected = record_review.inspect_source(REPO_ROOT, targets, extra_inputs)
    inspected["source"]["state"] = "git_commit"

    all_ids = [c["identifier"] for c in candidates]
    ready_curator_ids = [c["identifier"] for c in candidates if c["action"] == "CURATOR_XREF_READY"]
    ready_aro_ids = [
        c["identifier"] for c in candidates if c["action"] == "DECISION_NEEDS_INVENTORY_EXTRACT"
    ]
    held_ids = [c["identifier"] for c in candidates if c["action"] == "HOLD_CONGENER_COLLISION"]

    eval_sha = record_review.file_sha256(REPO_ROOT, "scripts/evaluate_cas_common_chemistry.py")
    extract_sha = record_review.file_sha256(REPO_ROOT, "scripts/extract_source_inventory.py")
    seed_sha = record_review.file_sha256(REPO_ROOT, "scripts/seed_from_sources.py")
    reconciled_sha = record_review.file_sha256(
        REPO_ROOT, "research/2026-10-15-card-reference-reconciled.json"
    )

    review = {
        "schema_version": "1.0.0",
        "review_id": "20261111T060500Z-cas-chebi-grounding-candidates-batch-review",
        "kind": "batch",
        "repository": inspected["repository"],
        "title": (
            "Batch review of 21 MINTED AntibioticRecord entries matching 3-star ChEBI "
            "outside the antimicrobial role slice via CAS Common Chemistry InChIKey bridging"
        ),
        "started_at": "2026-11-11T06:00:00Z",
        "finished_at": "2026-11-11T06:05:00Z",
        "reviewer": {
            "identity": "Antigravity",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": (
                "Structured LBNL chemical grounding review executed prior to adversarial PR review."
            ),
        },
        "skill": ".claude/skills/review-yaml-record/SKILL.md",
        "completion": "completed",
        "verdict": "needs_curation",
        "native_verdict": "STAGED_FOR_INVENTORY_EXTRACTION_AND_CONGENER_HOLD",
        "scientific_review": True,
        "summary": (
            "Structured batch review of the 21 MINTED AntibioticRecord files whose Standard "
            "InChIKeys match 3-star ChEBI entries outside the CHEBI:33281 antimicrobial role "
            "subtree (CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE), identified via non-redistributing "
            "CAS Common Chemistry InChIKey bridging (scripts/evaluate_cas_common_chemistry.py). "
            "Partitioned the 21 records into three deterministic cohorts: (1) 9 CURATOR_XREF_READY "
            "records in curation/curator_antibiotics.tsv (Isoorientin -> CHEBI:17965, Rutin -> "
            "CHEBI:28527, Fisetin -> CHEBI:42567, 5-indanol -> CHEBI:59311, Hispidulin -> "
            "CHEBI:75902, Vitexin -> CHEBI:16954, Cladribine -> CHEBI:567361, Luteolin -> "
            "CHEBI:15864, Orientin -> CHEBI:7781); (2) 10 DECISION_NEEDS_INVENTORY_EXTRACT "
            "ARO-seeded records in curation/decisions.tsv (miconazole ARO:3007518 -> CHEBI:82892, "
            "oxpoconazole ARO:3009171 -> CHEBI:83837, myclobutanil ARO:3009553 -> CHEBI:83729, "
            "tacrolimus ARO:3009353 -> CHEBI:61049, ofloxacin ARO:3000663 -> CHEBI:194135, "
            "isopyrazam ARO:3009168 -> CHEBI:83128, prothioconazole ARO:3009410 -> CHEBI:84008, "
            "mebendazole ARO:3009184 -> CHEBI:6704, imazalil ARO:3009554 -> CHEBI:83829, "
            "econazole ARO:3007519 -> CHEBI:82873); and (3) 2 HOLD_CONGENER_COLLISION records "
            "(gramicidin S ARO:3000200 and gramicidin C ARO:3000224) that share PubChem:73357 "
            "(Standard InChIKey IUAYMJGZBVDSGL-XNNAEKOYSA-N, cyclic decapeptide gramicidin S "
            "CHEBI:5530) in CARD/ARO, where grounding gramicidin S alone causes seed_from_sources.py "
            "to fold linear pentadecapeptide gramicidin C into CHEBI:5530."
        ),
        "source": inspected["source"],
        "scope": {
            "description": (
                "All 21 MINTED AntibioticRecord files in data/antibiotics/ evaluated as "
                "CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE by scripts/evaluate_cas_common_chemistry.py."
            ),
            "selection": (
                "Complete 21-record CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE cohort from the "
                "209 AntibioticMech CAS Common Chemistry evaluation rows."
            ),
            "coverage": "full",
            "population_size": 21,
            "reviewed_target_ids": all_ids,
        },
        "targets": targets,
        "checks": [
            {
                "check_id": "cas-evaluation-unit-tests",
                "name": "CAS Common Chemistry evaluator and ChEBI overlay unit tests",
                "status": "passed",
                "required": True,
                "command": ".venv/bin/python -m pytest tests/test_evaluate_cas_common_chemistry.py",
                "exit_code": 0,
                "summary": (
                    "All 6 unit tests pass, verifying CC BY-NC 4.0 non-redistribution guards, "
                    "7-column curation/decisions.tsv proposal formatting, and bilateral "
                    "HOLD_CONGENER_COLLISION classification for shared ChEBI target collisions."
                ),
                "target_ids": all_ids,
                "evidence_ids": ["cas-evaluator-script", "seed-from-sources-script"],
            },
            {
                "check_id": "strict-schema-and-corpus-reproduction",
                "name": "Closed-schema validation and corpus seed reproduction",
                "status": "passed",
                "required": True,
                "command": ".venv/bin/python scripts/verify_corpus.py",
                "exit_code": 0,
                "summary": (
                    "All 3,125 AntibioticRecord files reproduce byte-for-byte from data/raw/ "
                    "and curation/ overlays with 0 drift."
                ),
                "target_ids": all_ids,
                "evidence_ids": ["reconciled-corpus-manifest", "seed-from-sources-script"],
            },
        ],
        "evidence": [
            {
                "evidence_id": "cas-evaluator-script",
                "kind": "validation",
                "reference": "scripts/evaluate_cas_common_chemistry.py",
                "locator": "evaluate_cas_rows() and build_overlay_proposals()",
                "accessed_at": "2026-11-11T06:02:00Z",
                "support": "supports",
                "snapshot_sha256": eval_sha,
                "summary": (
                    "Evaluates 209 AntibioticMech CAS Common Chemistry hits against data/raw/"
                    "chebi_antimicrobials.tsv and full 3-star ChEBI without writing CC BY-NC 4.0 "
                    "fields to the repository; identifies 19 non-colliding 3-star ChEBI exact "
                    "InChIKey matches and holds both gramicidin S and gramicidin C on shared "
                    "CHEBI:5530 target collision."
                ),
            },
            {
                "evidence_id": "extract-inventory-script",
                "kind": "validation",
                "reference": "scripts/extract_source_inventory.py",
                "locator": "load_curation_chebi_ids() and extract_chebi()",
                "accessed_at": "2026-11-11T06:02:00Z",
                "support": "supports",
                "snapshot_sha256": extract_sha,
                "summary": (
                    "extract_chebi() includes explicit CHEBI:* IDs from curation/decisions.tsv "
                    "and curation/curator_antibiotics.tsv alongside the CHEBI:33281 antimicrobial "
                    "role subtree so 3-star ChEBI structures outside CHEBI:33281 are extracted "
                    "into data/raw/chebi_antimicrobials.tsv on the next inventory refresh."
                ),
            },
            {
                "evidence_id": "seed-from-sources-script",
                "kind": "validation",
                "reference": "scripts/seed_from_sources.py",
                "locator": "merge() InChIKey structure fold and flag_structure_collisions()",
                "accessed_at": "2026-11-11T06:02:00Z",
                "support": "supports",
                "snapshot_sha256": seed_sha,
                "summary": (
                    "When two MINTED records share a Standard InChIKey (gramicidin S ARO:3000200 "
                    "and gramicidin C ARO:3000224 sharing PubChem:73357 IUAYMJGZBVDSGL-XNNAEKOYSA-N), "
                    "flag_structure_collisions() keeps them separate with structure-collision "
                    "discussions; grounding gramicidin S alone to EXACT CHEBI:5530 causes merge() "
                    "to fold gramicidin C into CHEBI:5530 unless gramicidin C's upstream "
                    "PubChem:73357 assignment is decoupled first."
                ),
            },
            {
                "evidence_id": "reconciled-corpus-manifest",
                "kind": "validation",
                "reference": "research/2026-10-15-card-reference-reconciled.json",
                "locator": "2,939 SHA-256-pinned historical AntibioticRecord paths and identifiers",
                "accessed_at": "2026-11-11T06:02:00Z",
                "support": "supports",
                "snapshot_sha256": reconciled_sha,
                "summary": (
                    "All 21 candidate records are among the 2,939 records whose antibioticmech:aro-* "
                    "and antibioticmech:curator-* identifiers and pre-remediation SHA-256 digests "
                    "are verified by tests/conftest.py and "
                    "tests/test_salmonella_qualification_checkpoint.py, "
                    "and 3 ARO records (ofloxacin antibioticmech:aro-2eea3233f3, miconazole "
                    "antibioticmech:aro-11ab0a98bf, tacrolimus antibioticmech:aro-2e3b34cc67) are "
                    "additionally referenced by CURIE in curation/cryptic_drug_map.tsv, "
                    "curation/ncbi_ast_drug_map.tsv, curation/card_evidence_reviews.json, "
                    "curation/causal_graphs.yaml, and curation/uniprot_protein_examples.yaml."
                ),
            },
        ],
        "assessments": [
            {
                "assessment_id": "nineteen-non-colliding-3star-chebi-matches-verified",
                "area": "grounding",
                "topic": (
                    "19 MINTED AntibioticRecord entries have exact 3-star ChEBI Standard InChIKey "
                    "matches outside the CHEBI:33281 antimicrobial subtree"
                ),
                "outcome": "concern",
                "summary": (
                    "All 19 non-colliding records (9 CURATOR_XREF_READY and 10 "
                    "DECISION_NEEDS_INVENTORY_EXTRACT) have exact Standard InChIKey agreement "
                    "between their PubChem-seeded corpus structure, CAS Common Chemistry, and "
                    "3-star ChEBI (CC BY 4.0). Promoting their primary identifiers from "
                    "antibioticmech:aro-* / antibioticmech:curator-* to CHEBI:* requires a "
                    "coordinated inventory refresh (extract_source_inventory.py) plus a "
                    "reversible identifier/path transition fixture in tests/conftest.py and "
                    "synchronized CURIE updates across curation/cryptic_drug_map.tsv, "
                    "curation/ncbi_ast_drug_map.tsv, curation/card_evidence_reviews.json, "
                    "curation/causal_graphs.yaml, and curation/uniprot_protein_examples.yaml."
                ),
                "target_ids": ready_curator_ids + ready_aro_ids,
                "evidence_ids": [
                    "cas-evaluator-script",
                    "extract-inventory-script",
                    "reconciled-corpus-manifest",
                ],
            },
            {
                "assessment_id": "gramicidin-s-and-c-shared-inchikey-fold-hazard",
                "area": "identity",
                "topic": (
                    "Bilateral HOLD_CONGENER_COLLISION on gramicidin S (ARO:3000200) and "
                    "gramicidin C (ARO:3000224) sharing PubChem:73357 (IUAYMJGZBVDSGL-XNNAEKOYSA-N)"
                ),
                "outcome": "concern",
                "summary": (
                    "Gramicidin S (cyclic decapeptide, CHEBI:5530) and gramicidin C (linear "
                    "pentadecapeptide in the gramicidin A/B/C Dubos complex) both carry "
                    "PubChem:73357 (IUAYMJGZBVDSGL-XNNAEKOYSA-N) in upstream CARD/ARO. "
                    "Grounding gramicidin S (ARO:3000200) to CHEBI:5530 while gramicidin C "
                    "(ARO:3000224) retains PubChem:73357 causes seed_from_sources.py merge() "
                    "to fold gramicidin C into CHEBI:5530. Both records must remain held until "
                    "gramicidin C's upstream PubChem:73357 xref is suppressed or overridden."
                ),
                "target_ids": held_ids,
                "evidence_ids": ["cas-evaluator-script", "seed-from-sources-script"],
            },
        ],
        "findings": [
            {
                "finding_id": "nineteen-minted-records-ready-for-chebi-3star-inventory-transition",
                "issue_key": "nineteen-minted-records-ready-for-chebi-3star-inventory-transition",
                "category": "grounding",
                "severity": "minor",
                "status": "open",
                "certainty": "confirmed",
                "title": (
                    "19 MINTED AntibioticRecord entries have verified 3-star ChEBI groundings "
                    "outside CHEBI:33281 awaiting coordinated inventory refresh and conftest transition"
                ),
                "description": (
                    "9 curator-seeded records (Isoorientin CHEBI:17965, Rutin CHEBI:28527, "
                    "Fisetin CHEBI:42567, 5-indanol CHEBI:59311, Hispidulin CHEBI:75902, "
                    "Vitexin CHEBI:16954, Cladribine CHEBI:567361, Luteolin CHEBI:15864, "
                    "Orientin CHEBI:7781) and 10 ARO-seeded records (miconazole CHEBI:82892, "
                    "oxpoconazole CHEBI:83837, myclobutanil CHEBI:83729, tacrolimus CHEBI:61049, "
                    "ofloxacin CHEBI:194135, isopyrazam CHEBI:83128, prothioconazole CHEBI:84008, "
                    "mebendazole CHEBI:6704, imazalil CHEBI:83829, econazole CHEBI:82873) "
                    "have exact 3-star ChEBI Standard InChIKey matches outside the CHEBI:33281 "
                    "antimicrobial role slice and are ready for promotion during the next "
                    "data/raw/chebi_antimicrobials.tsv extraction and historical-fixture transition."
                ),
                "target_ids": ready_curator_ids + ready_aro_ids,
                "field_paths": ["identifier", "grounding_status", "xrefs"],
                "evidence_ids": [
                    "cas-evaluator-script",
                    "extract-inventory-script",
                    "reconciled-corpus-manifest",
                ],
                "owner_paths": [
                    {
                        "repository": "CultureBotAI/AntibioticMech",
                        "path": "curation/decisions.tsv",
                        "role": (
                            "ARO-to-ChEBI grounding decisions consumed by "
                            "extract_source_inventory.py and seed_from_sources.py"
                        ),
                    },
                    {
                        "repository": "CultureBotAI/AntibioticMech",
                        "path": "curation/curator_antibiotics.tsv",
                        "role": (
                            "Curator antibiotic xrefs consumed by "
                            "extract_source_inventory.py and seed_from_sources.py"
                        ),
                    },
                    {
                        "repository": "CultureBotAI/AntibioticMech",
                        "path": "tests/conftest.py",
                        "role": "Historical corpus SHA-256 reconstruction fixtures",
                    },
                ],
            },
            {
                "finding_id": "gramicidin-s-and-c-shared-pubchem-73357-congener-collision",
                "issue_key": "gramicidin-s-and-c-shared-pubchem-73357-congener-collision",
                "category": "identity",
                "severity": "minor",
                "status": "open",
                "certainty": "confirmed",
                "title": (
                    "Gramicidin S (ARO:3000200) and gramicidin C (ARO:3000224) share upstream "
                    "PubChem:73357 (IUAYMJGZBVDSGL-XNNAEKOYSA-N), blocking unilateral CHEBI:5530 grounding"
                ),
                "description": (
                    "In CARD/ARO, both gramicidin S (ARO:3000200, cyclic decapeptide) and "
                    "gramicidin C (ARO:3000224, linear pentadecapeptide) carry PubChem:73357 "
                    "(Standard InChIKey IUAYMJGZBVDSGL-XNNAEKOYSA-N, which is cyclic gramicidin S "
                    "CHEBI:5530). Grounding ARO:3000200 to CHEBI:5530 without first decoupling "
                    "ARO:3000224's erroneous PubChem:73357 xref causes seed_from_sources.py "
                    "merge() to fold gramicidin C into CHEBI:5530."
                ),
                "target_ids": held_ids,
                "field_paths": ["identifier", "grounding_status", "xrefs", "discussions"],
                "evidence_ids": ["cas-evaluator-script", "seed-from-sources-script"],
                "owner_paths": [
                    {
                        "repository": "CultureBotAI/AntibioticMech",
                        "path": "scripts/seed_from_sources.py",
                        "role": "Upstream PubChem xref override and structure-collision handling",
                    },
                    {
                        "repository": "CultureBotAI/AntibioticMech",
                        "path": "curation/decisions.tsv",
                        "role": "Grounding decision table for ARO:3000200 and ARO:3000224",
                    },
                ],
            },
        ],
        "actions": [
            {
                "action_id": "promote-19-non-colliding-chebi-3star-groundings-on-next-inventory-refresh",
                "description": (
                    "During the next scheduled data/raw/chebi_antimicrobials.tsv extraction "
                    "(extract_source_inventory.py), apply the 10 curation/decisions.tsv rows and "
                    "9 curation/curator_antibiotics.tsv CHEBI:* xrefs emitted by "
                    "scripts/evaluate_cas_common_chemistry.py --emit-overlay-proposals, update "
                    "CURIE references for ofloxacin/miconazole/tacrolimus in curation/ overlays, "
                    "and record the reversible identifier transition in tests/conftest.py."
                ),
                "finding_ids": ["nineteen-minted-records-ready-for-chebi-3star-inventory-transition"],
                "target_ids": ready_curator_ids + ready_aro_ids,
                "owner_paths": [
                    {
                        "repository": "CultureBotAI/AntibioticMech",
                        "path": "curation/decisions.tsv",
                        "role": "ARO-to-ChEBI grounding overlay",
                    },
                    {
                        "repository": "CultureBotAI/AntibioticMech",
                        "path": "curation/curator_antibiotics.tsv",
                        "role": "Curator antibiotic xrefs overlay",
                    },
                    {
                        "repository": "CultureBotAI/AntibioticMech",
                        "path": "tests/conftest.py",
                        "role": "Reversible historical corpus reconstruction fixture",
                    },
                ],
                "acceptance_checks": [
                    (
                        "python scripts/extract_source_inventory.py refreshes "
                        "data/raw/chebi_antimicrobials.tsv and data/raw/MANIFEST.yaml "
                        "with all 19 3-star ChEBI IDs"
                    ),
                    (
                        "python scripts/seed_from_sources.py --apply promotes the 19 "
                        "records from MINTED to EXACT with 0 congener fold regressions"
                    ),
                    (
                        "python scripts/run_qc.py passes all 12 quality gates including "
                        "historical corpus SHA-256 verification"
                    ),
                ],
            },
            {
                "action_id": "decouple-gramicidin-c-erroneous-pubchem-73357-before-grounding-gramicidin-s",
                "description": (
                    "Suppress or override the erroneous upstream CARD/ARO PubChem:73357 xref on "
                    "gramicidin C (ARO:3000224) in scripts/seed_from_sources.py before grounding "
                    "gramicidin S (ARO:3000200) to CHEBI:5530 in curation/decisions.tsv."
                ),
                "finding_ids": ["gramicidin-s-and-c-shared-pubchem-73357-congener-collision"],
                "target_ids": held_ids,
                "owner_paths": [
                    {
                        "repository": "CultureBotAI/AntibioticMech",
                        "path": "scripts/seed_from_sources.py",
                        "role": "Upstream xref suppression before structure-based merge()",
                    },
                    {
                        "repository": "CultureBotAI/AntibioticMech",
                        "path": "curation/decisions.tsv",
                        "role": "ARO:3000200 -> CHEBI:5530 grounding decision",
                    },
                ],
                "acceptance_checks": [
                    (
                        "gramicidin C (ARO:3000224) remains a distinct AntibioticRecord "
                        "after grounding gramicidin S (ARO:3000200) to CHEBI:5530"
                    ),
                    (
                        "python scripts/verify_corpus.py and pytest pass with 0 "
                        "structure-collision fold regressions"
                    ),
                ],
            },
        ],
        "limitations": [
            (
                "CAS Common Chemistry (CC BY-NC 4.0) was used strictly as an external lookup "
                "bridge to verify Standard InChIKey agreement with 3-star ChEBI (CC BY 4.0); "
                "no CAS Registry Numbers or CAS-derived structures are written to corpus records "
                "or curation overlays."
            ),
        ],
        "notes": [
            (
                "scripts/evaluate_cas_common_chemistry.py now classifies both sides of any "
                "shared ChEBI target collision (chebi_target_counts[chebi_id] > 1) as "
                "HOLD_CONGENER_COLLISION and emits exact 7-column curation/decisions.tsv "
                "proposals with zero CAS-derived tokens."
            ),
        ],
        "tags": [
            "batch-review",
            "lbnl-library-services",
            "cas-common-chemistry",
            "chebi-grounding",
        ],
    }
    return review


def main() -> int:
    review = build_review_dict()
    saved_path = record_review.save_review(REPO_ROOT, review)
    print(f"Saved structured review: {saved_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
