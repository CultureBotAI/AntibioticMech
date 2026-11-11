# Batch review of 21 MINTED AntibioticRecord entries matching 3-star ChEBI outside the antimicrobial role slice via CAS Common Chemistry InChIKey bridging

- Review: 20261111T060500Z-cas-chebi-grounding-candidates-batch-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-11-11T06:00:00Z
- Finished UTC: 2026-11-11T06:05:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Structured batch review of the 21 MINTED AntibioticRecord files whose Standard InChIKeys match 3-star ChEBI entries outside the CHEBI:33281 antimicrobial role subtree (CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE), identified via non-redistributing CAS Common Chemistry InChIKey bridging (scripts/evaluate_cas_common_chemistry.py). Partitioned the 21 records into three deterministic cohorts: (1) 9 CURATOR_XREF_READY records in curation/curator_antibiotics.tsv (Isoorientin -&gt; CHEBI:17965, Rutin -&gt; CHEBI:28527, Fisetin -&gt; CHEBI:42567, 5-indanol -&gt; CHEBI:59311, Hispidulin -&gt; CHEBI:75902, Vitexin -&gt; CHEBI:16954, Cladribine -&gt; CHEBI:567361, Luteolin -&gt; CHEBI:15864, Orientin -&gt; CHEBI:7781); (2) 10 DECISION_NEEDS_INVENTORY_EXTRACT ARO-seeded records in curation/decisions.tsv (miconazole ARO:3007518 -&gt; CHEBI:82892, oxpoconazole ARO:3009171 -&gt; CHEBI:83837, myclobutanil ARO:3009553 -&gt; CHEBI:83729, tacrolimus ARO:3009353 -&gt; CHEBI:61049, ofloxacin ARO:3000663 -&gt; CHEBI:194135, isopyrazam ARO:3009168 -&gt; CHEBI:83128, prothioconazole ARO:3009410 -&gt; CHEBI:84008, mebendazole ARO:3009184 -&gt; CHEBI:6704, imazalil ARO:3009554 -&gt; CHEBI:83829, econazole ARO:3007519 -&gt; CHEBI:82873); and (3) 2 HOLD_CONGENER_COLLISION records (gramicidin S ARO:3000200 and gramicidin C ARO:3000224) that share PubChem:73357 (Standard InChIKey IUAYMJGZBVDSGL-XNNAEKOYSA-N, cyclic decapeptide gramicidin S CHEBI:5530) in CARD/ARO, where grounding gramicidin S alone causes seed_from_sources.py to fold linear pentadecapeptide gramicidin C into CHEBI:5530.

## Scope And Provenance

All 21 MINTED AntibioticRecord files in data/antibiotics/ evaluated as CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE by scripts/evaluate_cas_common_chemistry.py.

Selection: Complete 21-record CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE cohort from the 209 AntibioticMech CAS Common Chemistry evaluation rows.
Coverage: full; 21 reviewed / 21 in the declared population.
Source: git_commit at Git base 450f3950d68f82fbbf9951b08014a5a0442ec532.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-0734abf918 | data/antibiotics/antibacterial/gramicidin-s.yaml | maintained | gramicidin S |
| antibioticmech:aro-bf39ac682c | data/antibiotics/antibacterial/gramicidin-c.yaml | maintained | gramicidin C |
| antibioticmech:aro-11ab0a98bf | data/antibiotics/antifungal/miconazole.yaml | maintained | miconazole |
| antibioticmech:aro-1224dc3554 | data/antibiotics/antifungal/oxpoconazole.yaml | maintained | oxpoconazole |
| antibioticmech:aro-14f45eb5b3 | data/antibiotics/antifungal/myclobutanil.yaml | maintained | myclobutanil |
| antibioticmech:aro-2e3b34cc67 | data/antibiotics/unspecified/tacrolimus.yaml | maintained | tacrolimus |
| antibioticmech:aro-2eea3233f3 | data/antibiotics/antibacterial/ofloxacin.yaml | maintained | ofloxacin |
| antibioticmech:aro-5fd4e54f15 | data/antibiotics/antifungal/isopyrazam.yaml | maintained | isopyrazam |
| antibioticmech:aro-a441fc6b50 | data/antibiotics/antifungal/prothioconazole.yaml | maintained | prothioconazole |
| antibioticmech:aro-adaab5b65b | data/antibiotics/antifungal/mebendazole.yaml | maintained | mebendazole |
| antibioticmech:aro-c1dea01a87 | data/antibiotics/antibacterial/imazalil.yaml | maintained | imazalil |
| antibioticmech:aro-e05d19b916 | data/antibiotics/antifungal/econazole.yaml | maintained | econazole |
| antibioticmech:curator-35c6404d6e | data/antibiotics/antibacterial/isoorientin.yaml | maintained | Isoorientin |
| antibioticmech:curator-59edbdc708 | data/antibiotics/antibacterial/rutin.yaml | maintained | Rutin |
| antibioticmech:curator-68713b9d28 | data/antibiotics/antibacterial/fisetin.yaml | maintained | Fisetin |
| antibioticmech:curator-9412b5ca77 | data/antibiotics/antibacterial/5-indanol.yaml | maintained | 5-indanol |
| antibioticmech:curator-b453af7884 | data/antibiotics/antibacterial/hispidulin.yaml | maintained | Hispidulin |
| antibioticmech:curator-c27816fecf | data/antibiotics/antibacterial/vitexin.yaml | maintained | Vitexin |
| antibioticmech:curator-d33759f162 | data/antibiotics/antibacterial/cladribine.yaml | maintained | Cladribine |
| antibioticmech:curator-d604421a09 | data/antibiotics/antibacterial/luteolin.yaml | maintained | Luteolin |
| antibioticmech:curator-ee3df8bfee | data/antibiotics/antibacterial/orientin.yaml | maintained | Orientin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| CAS Common Chemistry evaluator and ChEBI overlay unit tests | passed | True | antibioticmech:aro-0734abf918, antibioticmech:aro-bf39ac682c, antibioticmech:aro-11ab0a98bf, antibioticmech:aro-1224dc3554, antibioticmech:aro-14f45eb5b3, antibioticmech:aro-2e3b34cc67, antibioticmech:aro-2eea3233f3, antibioticmech:aro-5fd4e54f15, antibioticmech:aro-a441fc6b50, antibioticmech:aro-adaab5b65b, antibioticmech:aro-c1dea01a87, antibioticmech:aro-e05d19b916, antibioticmech:curator-35c6404d6e, antibioticmech:curator-59edbdc708, antibioticmech:curator-68713b9d28, antibioticmech:curator-9412b5ca77, antibioticmech:curator-b453af7884, antibioticmech:curator-c27816fecf, antibioticmech:curator-d33759f162, antibioticmech:curator-d604421a09, antibioticmech:curator-ee3df8bfee | All 6 unit tests pass, verifying CC BY-NC 4.0 non-redistribution guards, 7-column curation/decisions.tsv proposal formatting, and bilateral HOLD_CONGENER_COLLISION classification for shared ChEBI target collisions. |
| Closed-schema validation and corpus seed reproduction | passed | True | antibioticmech:aro-0734abf918, antibioticmech:aro-bf39ac682c, antibioticmech:aro-11ab0a98bf, antibioticmech:aro-1224dc3554, antibioticmech:aro-14f45eb5b3, antibioticmech:aro-2e3b34cc67, antibioticmech:aro-2eea3233f3, antibioticmech:aro-5fd4e54f15, antibioticmech:aro-a441fc6b50, antibioticmech:aro-adaab5b65b, antibioticmech:aro-c1dea01a87, antibioticmech:aro-e05d19b916, antibioticmech:curator-35c6404d6e, antibioticmech:curator-59edbdc708, antibioticmech:curator-68713b9d28, antibioticmech:curator-9412b5ca77, antibioticmech:curator-b453af7884, antibioticmech:curator-c27816fecf, antibioticmech:curator-d33759f162, antibioticmech:curator-d604421a09, antibioticmech:curator-ee3df8bfee | All 3,125 AntibioticRecord files reproduce byte-for-byte from data/raw/ and curation/ overlays with 0 drift. |

## Scientific And Domain Assessments

### 19 MINTED AntibioticRecord entries have exact 3-star ChEBI Standard InChIKey matches outside the CHEBI:33281 antimicrobial subtree

grounding: concern. Targets: antibioticmech:curator-35c6404d6e, antibioticmech:curator-59edbdc708, antibioticmech:curator-68713b9d28, antibioticmech:curator-9412b5ca77, antibioticmech:curator-b453af7884, antibioticmech:curator-c27816fecf, antibioticmech:curator-d33759f162, antibioticmech:curator-d604421a09, antibioticmech:curator-ee3df8bfee, antibioticmech:aro-11ab0a98bf, antibioticmech:aro-1224dc3554, antibioticmech:aro-14f45eb5b3, antibioticmech:aro-2e3b34cc67, antibioticmech:aro-2eea3233f3, antibioticmech:aro-5fd4e54f15, antibioticmech:aro-a441fc6b50, antibioticmech:aro-adaab5b65b, antibioticmech:aro-c1dea01a87, antibioticmech:aro-e05d19b916.

All 19 non-colliding records (9 CURATOR_XREF_READY and 10 DECISION_NEEDS_INVENTORY_EXTRACT) have exact Standard InChIKey agreement between their PubChem-seeded corpus structure, CAS Common Chemistry, and 3-star ChEBI (CC BY 4.0). Promoting their primary identifiers from antibioticmech:aro-* / antibioticmech:curator-* to CHEBI:* requires a coordinated inventory refresh (extract_source_inventory.py) plus a reversible identifier/path transition fixture in tests/conftest.py and synchronized CURIE updates across curation/cryptic_drug_map.tsv, curation/ncbi_ast_drug_map.tsv, curation/card_evidence_reviews.json, curation/causal_graphs.yaml, and curation/uniprot_protein_examples.yaml.

### Bilateral HOLD_CONGENER_COLLISION on gramicidin S (ARO:3000200) and gramicidin C (ARO:3000224) sharing PubChem:73357 (IUAYMJGZBVDSGL-XNNAEKOYSA-N)

identity: concern. Targets: antibioticmech:aro-0734abf918, antibioticmech:aro-bf39ac682c.

Gramicidin S (cyclic decapeptide, CHEBI:5530) and gramicidin C (linear pentadecapeptide in the gramicidin A/B/C Dubos complex) both carry PubChem:73357 (IUAYMJGZBVDSGL-XNNAEKOYSA-N) in upstream CARD/ARO. Grounding gramicidin S (ARO:3000200) to CHEBI:5530 while gramicidin C (ARO:3000224) retains PubChem:73357 causes seed_from_sources.py merge() to fold gramicidin C into CHEBI:5530. Both records must remain held until gramicidin C's upstream PubChem:73357 xref is suppressed or overridden.

## Findings

### nineteen-minted-records-ready-for-chebi-3star-inventory-transition: 19 MINTED AntibioticRecord entries have verified 3-star ChEBI groundings outside CHEBI:33281 awaiting coordinated inventory refresh and conftest transition

minor / open / confirmed; issue key: nineteen-minted-records-ready-for-chebi-3star-inventory-transition.

9 curator-seeded records (Isoorientin CHEBI:17965, Rutin CHEBI:28527, Fisetin CHEBI:42567, 5-indanol CHEBI:59311, Hispidulin CHEBI:75902, Vitexin CHEBI:16954, Cladribine CHEBI:567361, Luteolin CHEBI:15864, Orientin CHEBI:7781) and 10 ARO-seeded records (miconazole CHEBI:82892, oxpoconazole CHEBI:83837, myclobutanil CHEBI:83729, tacrolimus CHEBI:61049, ofloxacin CHEBI:194135, isopyrazam CHEBI:83128, prothioconazole CHEBI:84008, mebendazole CHEBI:6704, imazalil CHEBI:83829, econazole CHEBI:82873) have exact 3-star ChEBI Standard InChIKey matches outside the CHEBI:33281 antimicrobial role slice and are ready for promotion during the next data/raw/chebi_antimicrobials.tsv extraction and historical-fixture transition.

### gramicidin-s-and-c-shared-pubchem-73357-congener-collision: Gramicidin S (ARO:3000200) and gramicidin C (ARO:3000224) share upstream PubChem:73357 (IUAYMJGZBVDSGL-XNNAEKOYSA-N), blocking unilateral CHEBI:5530 grounding

minor / open / confirmed; issue key: gramicidin-s-and-c-shared-pubchem-73357-congener-collision.

In CARD/ARO, both gramicidin S (ARO:3000200, cyclic decapeptide) and gramicidin C (ARO:3000224, linear pentadecapeptide) carry PubChem:73357 (Standard InChIKey IUAYMJGZBVDSGL-XNNAEKOYSA-N, which is cyclic gramicidin S CHEBI:5530). Grounding ARO:3000200 to CHEBI:5530 without first decoupling ARO:3000224's erroneous PubChem:73357 xref causes seed_from_sources.py merge() to fold gramicidin C into CHEBI:5530.

## Recommended Actions And Acceptance Checks

### promote-19-non-colliding-chebi-3star-groundings-on-next-inventory-refresh

During the next scheduled data/raw/chebi_antimicrobials.tsv extraction (extract_source_inventory.py), apply the 10 curation/decisions.tsv rows and 9 curation/curator_antibiotics.tsv CHEBI:* xrefs emitted by scripts/evaluate_cas_common_chemistry.py --emit-overlay-proposals, update CURIE references for ofloxacin/miconazole/tacrolimus in curation/ overlays, and record the reversible identifier transition in tests/conftest.py.

- python scripts/extract_source_inventory.py refreshes data/raw/chebi_antimicrobials.tsv and data/raw/MANIFEST.yaml with all 19 3-star ChEBI IDs
- python scripts/seed_from_sources.py --apply promotes the 19 records from MINTED to EXACT with 0 congener fold regressions
- python scripts/run_qc.py passes all 12 quality gates including historical corpus SHA-256 verification

### decouple-gramicidin-c-erroneous-pubchem-73357-before-grounding-gramicidin-s

Suppress or override the erroneous upstream CARD/ARO PubChem:73357 xref on gramicidin C (ARO:3000224) in scripts/seed_from_sources.py before grounding gramicidin S (ARO:3000200) to CHEBI:5530 in curation/decisions.tsv.

- gramicidin C (ARO:3000224) remains a distinct AntibioticRecord after grounding gramicidin S (ARO:3000200) to CHEBI:5530
- python scripts/verify_corpus.py and pytest pass with 0 structure-collision fold regressions

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| cas-evaluator-script | scripts/evaluate_cas_common_chemistry.py; evaluate_cas_rows() and build_overlay_proposals() | supports | Evaluates 209 AntibioticMech CAS Common Chemistry hits against data/raw/chebi_antimicrobials.tsv and full 3-star ChEBI without writing CC BY-NC 4.0 fields to the repository; identifies 19 non-colliding 3-star ChEBI exact InChIKey matches and holds both gramicidin S and gramicidin C on shared CHEBI:5530 target collision. |
| extract-inventory-script | scripts/extract_source_inventory.py; load_curation_chebi_ids() and extract_chebi() | supports | extract_chebi() includes explicit CHEBI:* IDs from curation/decisions.tsv and curation/curator_antibiotics.tsv alongside the CHEBI:33281 antimicrobial role subtree so 3-star ChEBI structures outside CHEBI:33281 are extracted into data/raw/chebi_antimicrobials.tsv on the next inventory refresh. |
| seed-from-sources-script | scripts/seed_from_sources.py; merge() InChIKey structure fold and flag_structure_collisions() | supports | When two MINTED records share a Standard InChIKey (gramicidin S ARO:3000200 and gramicidin C ARO:3000224 sharing PubChem:73357 IUAYMJGZBVDSGL-XNNAEKOYSA-N), flag_structure_collisions() keeps them separate with structure-collision discussions; grounding gramicidin S alone to EXACT CHEBI:5530 causes merge() to fold gramicidin C into CHEBI:5530 unless gramicidin C's upstream PubChem:73357 assignment is decoupled first. |
| reconciled-corpus-manifest | research/2026-10-15-card-reference-reconciled.json; 2,939 SHA-256-pinned historical AntibioticRecord paths and identifiers | supports | All 21 candidate records are among the 2,939 records whose antibioticmech:aro-* and antibioticmech:curator-* identifiers and pre-remediation SHA-256 digests are verified by tests/conftest.py and tests/test_salmonella_qualification_checkpoint.py, and 3 ARO records (ofloxacin antibioticmech:aro-2eea3233f3, miconazole antibioticmech:aro-11ab0a98bf, tacrolimus antibioticmech:aro-2e3b34cc67) are additionally referenced by CURIE in curation/cryptic_drug_map.tsv, curation/ncbi_ast_drug_map.tsv, curation/card_evidence_reviews.json, curation/causal_graphs.yaml, and curation/uniprot_protein_examples.yaml. |

## Limits And Additional Notes

- CAS Common Chemistry (CC BY-NC 4.0) was used strictly as an external lookup bridge to verify Standard InChIKey agreement with 3-star ChEBI (CC BY 4.0); no CAS Registry Numbers or CAS-derived structures are written to corpus records or curation overlays.
- scripts/evaluate_cas_common_chemistry.py now classifies both sides of any shared ChEBI target collision (chebi_target_counts[chebi_id] &gt; 1) as HOLD_CONGENER_COLLISION and emits exact 7-column curation/decisions.tsv proposals with zero CAS-derived tokens.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261111T060500Z-cas-chebi-grounding-candidates-batch-review
kind: batch
repository: CultureBotAI/AntibioticMech
title: Batch review of 21 MINTED AntibioticRecord entries matching 3-star ChEBI outside
  the antimicrobial role slice via CAS Common Chemistry InChIKey bridging
started_at: '2026-11-11T06:00:00Z'
finished_at: '2026-11-11T06:05:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Structured LBNL chemical grounding review executed prior to
    adversarial PR review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: STAGED_FOR_INVENTORY_EXTRACTION_AND_CONGENER_HOLD
scientific_review: true
summary: 'Structured batch review of the 21 MINTED AntibioticRecord files whose Standard
  InChIKeys match 3-star ChEBI entries outside the CHEBI:33281 antimicrobial role
  subtree (CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE), identified via non-redistributing
  CAS Common Chemistry InChIKey bridging (scripts/evaluate_cas_common_chemistry.py).
  Partitioned the 21 records into three deterministic cohorts: (1) 9 CURATOR_XREF_READY
  records in curation/curator_antibiotics.tsv (Isoorientin -> CHEBI:17965, Rutin ->
  CHEBI:28527, Fisetin -> CHEBI:42567, 5-indanol -> CHEBI:59311, Hispidulin -> CHEBI:75902,
  Vitexin -> CHEBI:16954, Cladribine -> CHEBI:567361, Luteolin -> CHEBI:15864, Orientin
  -> CHEBI:7781); (2) 10 DECISION_NEEDS_INVENTORY_EXTRACT ARO-seeded records in curation/decisions.tsv
  (miconazole ARO:3007518 -> CHEBI:82892, oxpoconazole ARO:3009171 -> CHEBI:83837,
  myclobutanil ARO:3009553 -> CHEBI:83729, tacrolimus ARO:3009353 -> CHEBI:61049,
  ofloxacin ARO:3000663 -> CHEBI:194135, isopyrazam ARO:3009168 -> CHEBI:83128, prothioconazole
  ARO:3009410 -> CHEBI:84008, mebendazole ARO:3009184 -> CHEBI:6704, imazalil ARO:3009554
  -> CHEBI:83829, econazole ARO:3007519 -> CHEBI:82873); and (3) 2 HOLD_CONGENER_COLLISION
  records (gramicidin S ARO:3000200 and gramicidin C ARO:3000224) that share PubChem:73357
  (Standard InChIKey IUAYMJGZBVDSGL-XNNAEKOYSA-N, cyclic decapeptide gramicidin S
  CHEBI:5530) in CARD/ARO, where grounding gramicidin S alone causes seed_from_sources.py
  to fold linear pentadecapeptide gramicidin C into CHEBI:5530.'
source:
  git_revision: 450f3950d68f82fbbf9951b08014a5a0442ec532
  state: git_commit
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: cae7471ab358d3d8a4529198dd8d99206176e53cd94ba05e5f458b69a634a45d
    role: context
  - path: curation/decisions.tsv
    sha256: a5834b44307b0449b0df9362c551b7fcd707f3ae51f73d429d37d51f5a169d61
    role: context
  - path: data/antibiotics/antibacterial/5-indanol.yaml
    sha256: 02dfb2ef76084a0a5bc42b0c86777974a7715099f6c56e5704d6d662620d96b6
    role: target
  - path: data/antibiotics/antibacterial/cladribine.yaml
    sha256: a024d4e03191b0ac456e759527642619e9ee88a55a5f11516cd013c29d111e24
    role: target
  - path: data/antibiotics/antibacterial/fisetin.yaml
    sha256: dda0eaf619ee7624c6daf65bd4436477d19f63c4de6f5bbd3e83f810c86f4d4b
    role: target
  - path: data/antibiotics/antibacterial/gramicidin-c.yaml
    sha256: 2d6f2a226f80e692f51313152f18929496e2c7ffd5de864926dfe1c1dd79140f
    role: target
  - path: data/antibiotics/antibacterial/gramicidin-s.yaml
    sha256: d5b5bc269bda12fdcbc671ee93c42b9bdebacf4865201c912b843830da4cb917
    role: target
  - path: data/antibiotics/antibacterial/hispidulin.yaml
    sha256: fee5ef69c7a6535effc03ddae7059a5a62fc0b155f6f181effed9e6290d5070a
    role: target
  - path: data/antibiotics/antibacterial/imazalil.yaml
    sha256: a21f68711db34df975cc2383bbd03647202e3dff3f84bbd9b89c53b771bc9552
    role: target
  - path: data/antibiotics/antibacterial/isoorientin.yaml
    sha256: d45ae3678a02078f741ceeb2e82c0d9c2f5fed355e0c35be8150419110e6b68b
    role: target
  - path: data/antibiotics/antibacterial/luteolin.yaml
    sha256: 6fe7525ed8e5f9b076e201f7d2b43100f93f487bf017c761ad0439b6a6da7e90
    role: target
  - path: data/antibiotics/antibacterial/ofloxacin.yaml
    sha256: 01d084821fb0417288a6c93686a2222d44809e2e2767c67b055c212bc3c62e0d
    role: target
  - path: data/antibiotics/antibacterial/orientin.yaml
    sha256: 30300e7803460fec5206dc4620cc73b34b2a87cb3c69d5be7fc91bd3541c6987
    role: target
  - path: data/antibiotics/antibacterial/rutin.yaml
    sha256: d20795efff6e6b127a8000dad083ae786188d3aa8bc50f8f67af4e13b5e09640
    role: target
  - path: data/antibiotics/antibacterial/vitexin.yaml
    sha256: 17d510e1ad6938432c01a7a159af96439ebc3c6b510423b6a7aee1212c57d484
    role: target
  - path: data/antibiotics/antifungal/econazole.yaml
    sha256: 85a69c0a4373f95039bc4b3942493fb1dbd93ffce7c316cfbb42b724e5110b7b
    role: target
  - path: data/antibiotics/antifungal/isopyrazam.yaml
    sha256: e39dc672c1c63b7f81f357bb0f1363f596c4dd08b1a4d982d8b5f066158b35ba
    role: target
  - path: data/antibiotics/antifungal/mebendazole.yaml
    sha256: 4640c0b58afb044b261ce978abfc59e7dc8481863d0c896946b14c4df392e98f
    role: target
  - path: data/antibiotics/antifungal/miconazole.yaml
    sha256: 663c997eb1d5da9ea97d4679e9c3fd9c2fccdc1e468245af3addb0980ce62612
    role: target
  - path: data/antibiotics/antifungal/myclobutanil.yaml
    sha256: ff87ebb22992641e74b44de7c8b57cd1c70dfbf780937b47b4f8db92b639b480
    role: target
  - path: data/antibiotics/antifungal/oxpoconazole.yaml
    sha256: 5b97baa954f25ba2dee1ff0fffbf55209c898bf84ecce5be51eb879c5bb85ea1
    role: target
  - path: data/antibiotics/antifungal/prothioconazole.yaml
    sha256: 3b9cc481f83e005316e132e8b5c778eb7d61541a36efb3b303028cabb57b7634
    role: target
  - path: data/antibiotics/unspecified/tacrolimus.yaml
    sha256: c78b76727b23e17eb186b45746e63a146fc21e4e1608b6c09591822e21154e08
    role: target
  - path: research/2026-10-15-card-reference-reconciled.json
    sha256: d0a4b181ff5f2c42900f49e30498089f38aeb9499a4dd02f1b0f95f03beeab4b
    role: context
  - path: scripts/extract_source_inventory.py
    sha256: 27f9f0542a328ab64c0c9b2a3c532104b64f1ad97d9996129b9305f4760cee9e
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 53cf79eb1417ff7758a94f2d18ac1ce47b0f8c91c8961023363cf37698d4a056
    role: context
  - path: tests/conftest.py
    sha256: 2535208ec1858164cd6b1d56088f7c240bfb1b7eec79a62f5cfdcafe70a5ec4a
    role: context
scope:
  description: All 21 MINTED AntibioticRecord files in data/antibiotics/ evaluated
    as CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE by scripts/evaluate_cas_common_chemistry.py.
  selection: Complete 21-record CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE cohort from
    the 209 AntibioticMech CAS Common Chemistry evaluation rows.
  coverage: full
  population_size: 21
  reviewed_target_ids:
  - antibioticmech:aro-0734abf918
  - antibioticmech:aro-bf39ac682c
  - antibioticmech:aro-11ab0a98bf
  - antibioticmech:aro-1224dc3554
  - antibioticmech:aro-14f45eb5b3
  - antibioticmech:aro-2e3b34cc67
  - antibioticmech:aro-2eea3233f3
  - antibioticmech:aro-5fd4e54f15
  - antibioticmech:aro-a441fc6b50
  - antibioticmech:aro-adaab5b65b
  - antibioticmech:aro-c1dea01a87
  - antibioticmech:aro-e05d19b916
  - antibioticmech:curator-35c6404d6e
  - antibioticmech:curator-59edbdc708
  - antibioticmech:curator-68713b9d28
  - antibioticmech:curator-9412b5ca77
  - antibioticmech:curator-b453af7884
  - antibioticmech:curator-c27816fecf
  - antibioticmech:curator-d33759f162
  - antibioticmech:curator-d604421a09
  - antibioticmech:curator-ee3df8bfee
targets:
- target_id: antibioticmech:aro-0734abf918
  path: data/antibiotics/antibacterial/gramicidin-s.yaml
  label: gramicidin S
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/gramicidin-s.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:aro-bf39ac682c
  path: data/antibiotics/antibacterial/gramicidin-c.yaml
  label: gramicidin C
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/gramicidin-c.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:aro-11ab0a98bf
  path: data/antibiotics/antifungal/miconazole.yaml
  label: miconazole
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/miconazole.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:aro-1224dc3554
  path: data/antibiotics/antifungal/oxpoconazole.yaml
  label: oxpoconazole
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/oxpoconazole.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:aro-14f45eb5b3
  path: data/antibiotics/antifungal/myclobutanil.yaml
  label: myclobutanil
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/myclobutanil.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:aro-2e3b34cc67
  path: data/antibiotics/unspecified/tacrolimus.yaml
  label: tacrolimus
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/unspecified/tacrolimus.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:aro-2eea3233f3
  path: data/antibiotics/antibacterial/ofloxacin.yaml
  label: ofloxacin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/ofloxacin.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:aro-5fd4e54f15
  path: data/antibiotics/antifungal/isopyrazam.yaml
  label: isopyrazam
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/isopyrazam.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:aro-a441fc6b50
  path: data/antibiotics/antifungal/prothioconazole.yaml
  label: prothioconazole
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/prothioconazole.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:aro-adaab5b65b
  path: data/antibiotics/antifungal/mebendazole.yaml
  label: mebendazole
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/mebendazole.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:aro-c1dea01a87
  path: data/antibiotics/antibacterial/imazalil.yaml
  label: imazalil
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/imazalil.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:aro-e05d19b916
  path: data/antibiotics/antifungal/econazole.yaml
  label: econazole
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/econazole.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:curator-35c6404d6e
  path: data/antibiotics/antibacterial/isoorientin.yaml
  label: Isoorientin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/isoorientin.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:curator-59edbdc708
  path: data/antibiotics/antibacterial/rutin.yaml
  label: Rutin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/rutin.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:curator-68713b9d28
  path: data/antibiotics/antibacterial/fisetin.yaml
  label: Fisetin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/fisetin.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:curator-9412b5ca77
  path: data/antibiotics/antibacterial/5-indanol.yaml
  label: 5-indanol
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5-indanol.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:curator-b453af7884
  path: data/antibiotics/antibacterial/hispidulin.yaml
  label: Hispidulin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/hispidulin.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:curator-c27816fecf
  path: data/antibiotics/antibacterial/vitexin.yaml
  label: Vitexin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/vitexin.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:curator-d33759f162
  path: data/antibiotics/antibacterial/cladribine.yaml
  label: Cladribine
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cladribine.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:curator-d604421a09
  path: data/antibiotics/antibacterial/luteolin.yaml
  label: Luteolin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/luteolin.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
- target_id: antibioticmech:curator-ee3df8bfee
  path: data/antibiotics/antibacterial/orientin.yaml
  label: Orientin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/orientin.yaml
    role: Seeded MINTED AntibioticRecord evaluated for 3-star ChEBI grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator grounding overlay consumed by extract_source_inventory.py and seed_from_sources.py
checks:
- check_id: cas-evaluation-unit-tests
  name: CAS Common Chemistry evaluator and ChEBI overlay unit tests
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_evaluate_cas_common_chemistry.py
  exit_code: 0
  summary: All 6 unit tests pass, verifying CC BY-NC 4.0 non-redistribution guards,
    7-column curation/decisions.tsv proposal formatting, and bilateral HOLD_CONGENER_COLLISION
    classification for shared ChEBI target collisions.
  target_ids:
  - antibioticmech:aro-0734abf918
  - antibioticmech:aro-bf39ac682c
  - antibioticmech:aro-11ab0a98bf
  - antibioticmech:aro-1224dc3554
  - antibioticmech:aro-14f45eb5b3
  - antibioticmech:aro-2e3b34cc67
  - antibioticmech:aro-2eea3233f3
  - antibioticmech:aro-5fd4e54f15
  - antibioticmech:aro-a441fc6b50
  - antibioticmech:aro-adaab5b65b
  - antibioticmech:aro-c1dea01a87
  - antibioticmech:aro-e05d19b916
  - antibioticmech:curator-35c6404d6e
  - antibioticmech:curator-59edbdc708
  - antibioticmech:curator-68713b9d28
  - antibioticmech:curator-9412b5ca77
  - antibioticmech:curator-b453af7884
  - antibioticmech:curator-c27816fecf
  - antibioticmech:curator-d33759f162
  - antibioticmech:curator-d604421a09
  - antibioticmech:curator-ee3df8bfee
  evidence_ids:
  - cas-evaluator-script
  - seed-from-sources-script
- check_id: strict-schema-and-corpus-reproduction
  name: Closed-schema validation and corpus seed reproduction
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  summary: All 3,125 AntibioticRecord files reproduce byte-for-byte from data/raw/
    and curation/ overlays with 0 drift.
  target_ids:
  - antibioticmech:aro-0734abf918
  - antibioticmech:aro-bf39ac682c
  - antibioticmech:aro-11ab0a98bf
  - antibioticmech:aro-1224dc3554
  - antibioticmech:aro-14f45eb5b3
  - antibioticmech:aro-2e3b34cc67
  - antibioticmech:aro-2eea3233f3
  - antibioticmech:aro-5fd4e54f15
  - antibioticmech:aro-a441fc6b50
  - antibioticmech:aro-adaab5b65b
  - antibioticmech:aro-c1dea01a87
  - antibioticmech:aro-e05d19b916
  - antibioticmech:curator-35c6404d6e
  - antibioticmech:curator-59edbdc708
  - antibioticmech:curator-68713b9d28
  - antibioticmech:curator-9412b5ca77
  - antibioticmech:curator-b453af7884
  - antibioticmech:curator-c27816fecf
  - antibioticmech:curator-d33759f162
  - antibioticmech:curator-d604421a09
  - antibioticmech:curator-ee3df8bfee
  evidence_ids:
  - reconciled-corpus-manifest
  - seed-from-sources-script
evidence:
- evidence_id: cas-evaluator-script
  kind: validation
  reference: scripts/evaluate_cas_common_chemistry.py
  locator: evaluate_cas_rows() and build_overlay_proposals()
  accessed_at: '2026-11-11T06:02:00Z'
  support: supports
  snapshot_sha256: 71e29e56eeb589819ed8848d3136d74c6c6d4dd0fcd09e5d87557b9b64188af3
  summary: Evaluates 209 AntibioticMech CAS Common Chemistry hits against data/raw/chebi_antimicrobials.tsv
    and full 3-star ChEBI without writing CC BY-NC 4.0 fields to the repository; identifies
    19 non-colliding 3-star ChEBI exact InChIKey matches and holds both gramicidin
    S and gramicidin C on shared CHEBI:5530 target collision.
- evidence_id: extract-inventory-script
  kind: validation
  reference: scripts/extract_source_inventory.py
  locator: load_curation_chebi_ids() and extract_chebi()
  accessed_at: '2026-11-11T06:02:00Z'
  support: supports
  snapshot_sha256: 27f9f0542a328ab64c0c9b2a3c532104b64f1ad97d9996129b9305f4760cee9e
  summary: extract_chebi() includes explicit CHEBI:* IDs from curation/decisions.tsv
    and curation/curator_antibiotics.tsv alongside the CHEBI:33281 antimicrobial role
    subtree so 3-star ChEBI structures outside CHEBI:33281 are extracted into data/raw/chebi_antimicrobials.tsv
    on the next inventory refresh.
- evidence_id: seed-from-sources-script
  kind: validation
  reference: scripts/seed_from_sources.py
  locator: merge() InChIKey structure fold and flag_structure_collisions()
  accessed_at: '2026-11-11T06:02:00Z'
  support: supports
  snapshot_sha256: 53cf79eb1417ff7758a94f2d18ac1ce47b0f8c91c8961023363cf37698d4a056
  summary: When two MINTED records share a Standard InChIKey (gramicidin S ARO:3000200
    and gramicidin C ARO:3000224 sharing PubChem:73357 IUAYMJGZBVDSGL-XNNAEKOYSA-N),
    flag_structure_collisions() keeps them separate with structure-collision discussions;
    grounding gramicidin S alone to EXACT CHEBI:5530 causes merge() to fold gramicidin
    C into CHEBI:5530 unless gramicidin C's upstream PubChem:73357 assignment is decoupled
    first.
- evidence_id: reconciled-corpus-manifest
  kind: validation
  reference: research/2026-10-15-card-reference-reconciled.json
  locator: 2,939 SHA-256-pinned historical AntibioticRecord paths and identifiers
  accessed_at: '2026-11-11T06:02:00Z'
  support: supports
  snapshot_sha256: d0a4b181ff5f2c42900f49e30498089f38aeb9499a4dd02f1b0f95f03beeab4b
  summary: All 21 candidate records are among the 2,939 records whose antibioticmech:aro-*
    and antibioticmech:curator-* identifiers and pre-remediation SHA-256 digests are
    verified by tests/conftest.py and tests/test_salmonella_qualification_checkpoint.py,
    and 3 ARO records (ofloxacin antibioticmech:aro-2eea3233f3, miconazole antibioticmech:aro-11ab0a98bf,
    tacrolimus antibioticmech:aro-2e3b34cc67) are additionally referenced by CURIE
    in curation/cryptic_drug_map.tsv, curation/ncbi_ast_drug_map.tsv, curation/card_evidence_reviews.json,
    curation/causal_graphs.yaml, and curation/uniprot_protein_examples.yaml.
assessments:
- assessment_id: nineteen-non-colliding-3star-chebi-matches-verified
  area: grounding
  topic: 19 MINTED AntibioticRecord entries have exact 3-star ChEBI Standard InChIKey
    matches outside the CHEBI:33281 antimicrobial subtree
  outcome: concern
  summary: All 19 non-colliding records (9 CURATOR_XREF_READY and 10 DECISION_NEEDS_INVENTORY_EXTRACT)
    have exact Standard InChIKey agreement between their PubChem-seeded corpus structure,
    CAS Common Chemistry, and 3-star ChEBI (CC BY 4.0). Promoting their primary identifiers
    from antibioticmech:aro-* / antibioticmech:curator-* to CHEBI:* requires a coordinated
    inventory refresh (extract_source_inventory.py) plus a reversible identifier/path
    transition fixture in tests/conftest.py and synchronized CURIE updates across
    curation/cryptic_drug_map.tsv, curation/ncbi_ast_drug_map.tsv, curation/card_evidence_reviews.json,
    curation/causal_graphs.yaml, and curation/uniprot_protein_examples.yaml.
  target_ids:
  - antibioticmech:curator-35c6404d6e
  - antibioticmech:curator-59edbdc708
  - antibioticmech:curator-68713b9d28
  - antibioticmech:curator-9412b5ca77
  - antibioticmech:curator-b453af7884
  - antibioticmech:curator-c27816fecf
  - antibioticmech:curator-d33759f162
  - antibioticmech:curator-d604421a09
  - antibioticmech:curator-ee3df8bfee
  - antibioticmech:aro-11ab0a98bf
  - antibioticmech:aro-1224dc3554
  - antibioticmech:aro-14f45eb5b3
  - antibioticmech:aro-2e3b34cc67
  - antibioticmech:aro-2eea3233f3
  - antibioticmech:aro-5fd4e54f15
  - antibioticmech:aro-a441fc6b50
  - antibioticmech:aro-adaab5b65b
  - antibioticmech:aro-c1dea01a87
  - antibioticmech:aro-e05d19b916
  evidence_ids:
  - cas-evaluator-script
  - extract-inventory-script
  - reconciled-corpus-manifest
- assessment_id: gramicidin-s-and-c-shared-inchikey-fold-hazard
  area: identity
  topic: Bilateral HOLD_CONGENER_COLLISION on gramicidin S (ARO:3000200) and gramicidin
    C (ARO:3000224) sharing PubChem:73357 (IUAYMJGZBVDSGL-XNNAEKOYSA-N)
  outcome: concern
  summary: Gramicidin S (cyclic decapeptide, CHEBI:5530) and gramicidin C (linear
    pentadecapeptide in the gramicidin A/B/C Dubos complex) both carry PubChem:73357
    (IUAYMJGZBVDSGL-XNNAEKOYSA-N) in upstream CARD/ARO. Grounding gramicidin S (ARO:3000200)
    to CHEBI:5530 while gramicidin C (ARO:3000224) retains PubChem:73357 causes seed_from_sources.py
    merge() to fold gramicidin C into CHEBI:5530. Both records must remain held until
    gramicidin C's upstream PubChem:73357 xref is suppressed or overridden.
  target_ids:
  - antibioticmech:aro-0734abf918
  - antibioticmech:aro-bf39ac682c
  evidence_ids:
  - cas-evaluator-script
  - seed-from-sources-script
findings:
- finding_id: nineteen-minted-records-ready-for-chebi-3star-inventory-transition
  issue_key: nineteen-minted-records-ready-for-chebi-3star-inventory-transition
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: 19 MINTED AntibioticRecord entries have verified 3-star ChEBI groundings
    outside CHEBI:33281 awaiting coordinated inventory refresh and conftest transition
  description: 9 curator-seeded records (Isoorientin CHEBI:17965, Rutin CHEBI:28527,
    Fisetin CHEBI:42567, 5-indanol CHEBI:59311, Hispidulin CHEBI:75902, Vitexin CHEBI:16954,
    Cladribine CHEBI:567361, Luteolin CHEBI:15864, Orientin CHEBI:7781) and 10 ARO-seeded
    records (miconazole CHEBI:82892, oxpoconazole CHEBI:83837, myclobutanil CHEBI:83729,
    tacrolimus CHEBI:61049, ofloxacin CHEBI:194135, isopyrazam CHEBI:83128, prothioconazole
    CHEBI:84008, mebendazole CHEBI:6704, imazalil CHEBI:83829, econazole CHEBI:82873)
    have exact 3-star ChEBI Standard InChIKey matches outside the CHEBI:33281 antimicrobial
    role slice and are ready for promotion during the next data/raw/chebi_antimicrobials.tsv
    extraction and historical-fixture transition.
  target_ids:
  - antibioticmech:curator-35c6404d6e
  - antibioticmech:curator-59edbdc708
  - antibioticmech:curator-68713b9d28
  - antibioticmech:curator-9412b5ca77
  - antibioticmech:curator-b453af7884
  - antibioticmech:curator-c27816fecf
  - antibioticmech:curator-d33759f162
  - antibioticmech:curator-d604421a09
  - antibioticmech:curator-ee3df8bfee
  - antibioticmech:aro-11ab0a98bf
  - antibioticmech:aro-1224dc3554
  - antibioticmech:aro-14f45eb5b3
  - antibioticmech:aro-2e3b34cc67
  - antibioticmech:aro-2eea3233f3
  - antibioticmech:aro-5fd4e54f15
  - antibioticmech:aro-a441fc6b50
  - antibioticmech:aro-adaab5b65b
  - antibioticmech:aro-c1dea01a87
  - antibioticmech:aro-e05d19b916
  field_paths:
  - identifier
  - grounding_status
  - xrefs
  evidence_ids:
  - cas-evaluator-script
  - extract-inventory-script
  - reconciled-corpus-manifest
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: ARO-to-ChEBI grounding decisions consumed by extract_source_inventory.py
      and seed_from_sources.py
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator antibiotic xrefs consumed by extract_source_inventory.py and seed_from_sources.py
  - repository: CultureBotAI/AntibioticMech
    path: tests/conftest.py
    role: Historical corpus SHA-256 reconstruction fixtures
- finding_id: gramicidin-s-and-c-shared-pubchem-73357-congener-collision
  issue_key: gramicidin-s-and-c-shared-pubchem-73357-congener-collision
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Gramicidin S (ARO:3000200) and gramicidin C (ARO:3000224) share upstream
    PubChem:73357 (IUAYMJGZBVDSGL-XNNAEKOYSA-N), blocking unilateral CHEBI:5530 grounding
  description: In CARD/ARO, both gramicidin S (ARO:3000200, cyclic decapeptide) and
    gramicidin C (ARO:3000224, linear pentadecapeptide) carry PubChem:73357 (Standard
    InChIKey IUAYMJGZBVDSGL-XNNAEKOYSA-N, which is cyclic gramicidin S CHEBI:5530).
    Grounding ARO:3000200 to CHEBI:5530 without first decoupling ARO:3000224's erroneous
    PubChem:73357 xref causes seed_from_sources.py merge() to fold gramicidin C into
    CHEBI:5530.
  target_ids:
  - antibioticmech:aro-0734abf918
  - antibioticmech:aro-bf39ac682c
  field_paths:
  - identifier
  - grounding_status
  - xrefs
  - discussions
  evidence_ids:
  - cas-evaluator-script
  - seed-from-sources-script
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Upstream PubChem xref override and structure-collision handling
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decision table for ARO:3000200 and ARO:3000224
actions:
- action_id: promote-19-non-colliding-chebi-3star-groundings-on-next-inventory-refresh
  description: During the next scheduled data/raw/chebi_antimicrobials.tsv extraction
    (extract_source_inventory.py), apply the 10 curation/decisions.tsv rows and 9
    curation/curator_antibiotics.tsv CHEBI:* xrefs emitted by scripts/evaluate_cas_common_chemistry.py
    --emit-overlay-proposals, update CURIE references for ofloxacin/miconazole/tacrolimus
    in curation/ overlays, and record the reversible identifier transition in tests/conftest.py.
  finding_ids:
  - nineteen-minted-records-ready-for-chebi-3star-inventory-transition
  target_ids:
  - antibioticmech:curator-35c6404d6e
  - antibioticmech:curator-59edbdc708
  - antibioticmech:curator-68713b9d28
  - antibioticmech:curator-9412b5ca77
  - antibioticmech:curator-b453af7884
  - antibioticmech:curator-c27816fecf
  - antibioticmech:curator-d33759f162
  - antibioticmech:curator-d604421a09
  - antibioticmech:curator-ee3df8bfee
  - antibioticmech:aro-11ab0a98bf
  - antibioticmech:aro-1224dc3554
  - antibioticmech:aro-14f45eb5b3
  - antibioticmech:aro-2e3b34cc67
  - antibioticmech:aro-2eea3233f3
  - antibioticmech:aro-5fd4e54f15
  - antibioticmech:aro-a441fc6b50
  - antibioticmech:aro-adaab5b65b
  - antibioticmech:aro-c1dea01a87
  - antibioticmech:aro-e05d19b916
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: ARO-to-ChEBI grounding overlay
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator antibiotic xrefs overlay
  - repository: CultureBotAI/AntibioticMech
    path: tests/conftest.py
    role: Reversible historical corpus reconstruction fixture
  acceptance_checks:
  - python scripts/extract_source_inventory.py refreshes data/raw/chebi_antimicrobials.tsv
    and data/raw/MANIFEST.yaml with all 19 3-star ChEBI IDs
  - python scripts/seed_from_sources.py --apply promotes the 19 records from MINTED
    to EXACT with 0 congener fold regressions
  - python scripts/run_qc.py passes all 12 quality gates including historical corpus
    SHA-256 verification
- action_id: decouple-gramicidin-c-erroneous-pubchem-73357-before-grounding-gramicidin-s
  description: Suppress or override the erroneous upstream CARD/ARO PubChem:73357
    xref on gramicidin C (ARO:3000224) in scripts/seed_from_sources.py before grounding
    gramicidin S (ARO:3000200) to CHEBI:5530 in curation/decisions.tsv.
  finding_ids:
  - gramicidin-s-and-c-shared-pubchem-73357-congener-collision
  target_ids:
  - antibioticmech:aro-0734abf918
  - antibioticmech:aro-bf39ac682c
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Upstream xref suppression before structure-based merge()
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: ARO:3000200 -> CHEBI:5530 grounding decision
  acceptance_checks:
  - gramicidin C (ARO:3000224) remains a distinct AntibioticRecord after grounding
    gramicidin S (ARO:3000200) to CHEBI:5530
  - python scripts/verify_corpus.py and pytest pass with 0 structure-collision fold
    regressions
limitations:
- CAS Common Chemistry (CC BY-NC 4.0) was used strictly as an external lookup bridge
  to verify Standard InChIKey agreement with 3-star ChEBI (CC BY 4.0); no CAS Registry
  Numbers or CAS-derived structures are written to corpus records or curation overlays.
notes:
- scripts/evaluate_cas_common_chemistry.py now classifies both sides of any shared
  ChEBI target collision (chebi_target_counts[chebi_id] > 1) as HOLD_CONGENER_COLLISION
  and emits exact 7-column curation/decisions.tsv proposals with zero CAS-derived
  tokens.
tags:
- batch-review
- lbnl-library-services
- cas-common-chemistry
- chebi-grounding
```
