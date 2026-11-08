# AntibioticMech Cycle 7 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `7`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Source Revision**: `9d3d0205b298bbb5ef04218fb8245ccb4e471ca7`
- **Single-Record Review Bundle**: `reviews/structured/20261108T210000Z-neocarzinostatin-record-review/review.yaml` (`.claude/skills/review-yaml-record/SKILL.md`)
- **Full-Inventory Cohort Review Bundle**: `reviews/structured/20261108T210100Z-cycle7-frozen-inventory-cohort-review/review.yaml` (`.claude/skills/review-yaml-category/SKILL.md`)

## 1. Frozen Inventory & Validation Census

All **3,105** `AntibioticRecord` YAML files under `data/antibiotics/` at commit `9d3d0205b298bbb5ef04218fb8245ccb4e471ca7` were audited without modifying any scientific YAML records:

| Metric | Value |
| --- | ---: |
| Total `AntibioticRecord` files | 3,105 |
| `SEEDED` / `REVIEWED` / `PROPOSED` | 2,805 / 145 / 155 |
| `EXACT` / `MINTED` grounding | 2,767 / 338 (`240` `SEEDED` `antibioticmech:aro-*` + `98` `PROPOSED` `antibioticmech:curator-*`) |
| Records with `causal_graphs` | 91 (`90` `REVIEWED` + `1` `SEEDED`/`MINTED` ofloxacin; `92` graphs; `72/72` `GENE_OR_PROTEIN` nodes carry `131` reviewed `UniProtKB` `protein_examples` across `70` protein-node graphs + `22` non-protein graphs held) |
| Records with `PRIMARY_LITERATURE` `molecular_targets` | 183 (`145` `REVIEWED` + `38` `PROPOSED` total across `189` target entries: `91` targets carry `162` reviewed `UniProtKB` `protein_examples`, `98` non-protein/complex targets explicitly held in `curation/uniprot_protein_examples.yaml`, `0` unaccounted) |
| `scripts/validate_strict.py --quiet --workers 4` | `0` errors across `3,105` files |
| `scripts/verify_corpus.py --summary` | `0` errors across `3,105` files (`145/145` `REVIEWED` have `EXACT` grounding + `chemical_structure`) |

### Partition by Antimicrobial Class Directory (`boundary_decisions[0]`)

| Directory | Record Count |
| --- | ---: |
| `data/antibiotics/antibacterial/` | 1,182 |
| `data/antibiotics/antifungal/` | 613 |
| `data/antibiotics/antiviral/` | 473 |
| `data/antibiotics/unspecified/` | 472 |
| `data/antibiotics/antiprotozoal/` | 256 |
| `data/antibiotics/antimycobacterial/` | 78 |
| `data/antibiotics/biocide/` | 31 |
| **Total** | **3,105** |

### Partition by Curation-Readiness Cohort (`boundary_decisions[1]`)

| Cohort | Record Count |
| --- | ---: |
| `REVIEWED` records with primary-literature `causal_graphs` | 90 |
| `REVIEWED` records awaiting primary-literature `causal_graphs` | 55 |
| `PROPOSED` records with `PRIMARY_LITERATURE` `molecular_targets` and `mode_of_action` | 38 (`3` `EXACT` + `35` `MINTED`) |
| `PROPOSED` `EXACT` Cycle 7 Stage 1 natural products ready for primary mechanism/target curation | 5 (`5` `EXACT`) |
| `PROPOSED` records awaiting primary mechanism curation | 112 (`49` `EXACT` + `63` `MINTED`) |
| `SEEDED` baseline records | 2,805 (`2,565` `EXACT` + `240` `MINTED`) |
| **Total** | **3,105** |

## 2. Single-Record Deep Review (`20261108T210000Z-neocarzinostatin-record-review`)

- **Target**: `CHEBI:29655` (`data/antibiotics/antibacterial/neocarzinostatin.yaml`)
- **Verdict**: `needs_curation` (`NEEDS_CURATION`)
- **Verified Support**: Exact `C35H33NO12` chemical structure (`QZGIWPZCWHMVQL-UIYAJPBUSA-N`, PubChem CID `447545`), `CURATOR` discovery and mechanism evidence (`DOI:10.1016/j.chembiol.2004.12.013`, `PMID:15797213`; `DOI:10.7164/antibiotics.28.229`, `PMID:123897`), MIBiG `BGC0000112` producer `Streptomyces carzinostaticus subsp. neocarzinostaticus` (`NCBITaxon:167636`), `biosynthesis_origin: NATURAL_PRODUCT`, `mode_of_action: NUCLEIC_ACID_SYNTHESIS_INHIBITION` (`MICROBIAL_TARGET`), and `PRIMARY_LITERATURE` `molecular_targets[0]` for bacterial duplex DNA (`CHEBI:16991`, `NUCLEIC_ACID`, `DIRECT_BINDING_TARGET`) explicitly accounted in `curation/uniprot_protein_examples.yaml` (`held_targets`).
- **Open Finding**: `neocarzinostatin-awaiting-reviewed-promotion` (`issue_key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`) — retains `curation_status: PROPOSED` despite meeting all `REVIEWED` gate criteria.

## 3. Stable Findings & Dispositions (`20261108T210100Z-cycle7-frozen-inventory-cohort-review`)

### Open Findings for Cycle 7 Stage 5 Grouped Remediation (3 findings, 14 records)

1. **`proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`** (`major`, `open`, `3` targets: `CHEBI:29655` `neocarzinostatin`, `CHEBI:67576` `streptothricin E`, `CHEBI:42265` `epoxomicin`):
   - Have `grounding_status: EXACT`, complete single-molecule `chemical_structure`, curated `biosynthesis_origin: NATURAL_PRODUCT`, curated `mode_of_action` (`NUCLEIC_ACID_SYNTHESIS_INHIBITION` on `neocarzinostatin`; `PROTEIN_SYNTHESIS_INHIBITION` on `streptothricin E`; `OTHER` / `HOST_SHARED_TARGET` on `epoxomicin`), and `PRIMARY_LITERATURE` `molecular_targets` with complete `UniProtKB` `held_targets` accounting, yet remain `curation_status: PROPOSED` (and `streptothricin E` / `epoxomicin` can additionally be enriched with canonical GO `target_id` terms `GO:0015935` and `GO:0005839`).
2. **`cycle7-stage1-proposed-exact-natural-products-missing-mechanism-and-targets`** (`major`, `open`, `5` targets: `CHEBI:226154` `benastatin A`, `CHEBI:200324` `benastatin B`, `CHEBI:204430` `tetarimycin A`, `CHEBI:215258` `9-methylstreptimidone`, `CHEBI:198890` `7-deoxypactamycin`):
   - All 5 `PROPOSED`/`EXACT` natural-product records seeded in Cycle 7 Stage 1 have complete `chemical_structure`, curated `biosynthesis_origin: NATURAL_PRODUCT`, and primary-literature discovery/biosynthetic citations (`Kawahara et al. 2024 PMID:38664572` / `Xu et al. 2009 PMID:19047004` / `BGC0000203` for `benastatin A` and `benastatin B`; `Kallifidas et al. 2012 PMID:23157252` / `BGC0000274` for `tetarimycin A`; `Wang et al. 2013 PMID:23438151` / `Song et al. 2025 PMID:41162067` / `BGC0000171` for `9-methylstreptimidone`; `Lu et al. 2011 PMID:21513878` / `Kudo et al. 2007 PMID:17827660` / `Masaki et al. 2026 PMID:42265342` / `BGC0000711` for `7-deoxypactamycin`), but lack `mode_of_action`, structured `PRIMARY_LITERATURE` `molecular_targets` (with `UniProtKB` accounting), and `REVIEWED` promotion.
3. **`seeded-exact-folate-inhibitors-with-card-only-targets-awaiting-primary-literature-promotion`** (`major`, `open`, `6` targets: `CHEBI:9329` `sulfadoxine`, `CHEBI:9334` `sulfasalazine`, `CHEBI:102484` `sulfisoxazole`, `CHEBI:4325` `dapsone`, `CHEBI:131726` `brodimoprim`, `CHEBI:135420` `tetroxoprim`):
   - All 6 `SEEDED`/`EXACT` folate-pathway inhibitor records have complete ChEBI `chemical_structure` and `CARD_ARO` target assertions (`PRIMARY_EVIDENCE_NEEDED`: `ARO:3000744` dihydropteroate synthase on `sulfadoxine`, `sulfasalazine`, `sulfisoxazole`, and `dapsone`; `ARO:3000745` dihydrofolate reductase on `brodimoprim` and `tetroxoprim`) but lack `biosynthesis_origin: SYNTHETIC`, curator-reviewed `mode_of_action` (`FOLATE_PATHWAY_INHIBITION` with `MICROBIAL_TARGET`; `brodimoprim` carries ChEBI-seeded `FOLATE_PATHWAY_INHIBITION` / `HOST_SHARED_TARGET` while the other 5 lack `mode_of_action`) and `mode_of_action_notes`, structured `PRIMARY_LITERATURE` `molecular_targets` (`GO:0004156` dihydropteroate synthase activity or `GO:0004146` dihydrofolate reductase activity with reviewed `UniProtKB` `protein_examples`), and `REVIEWED` promotion.

### Deferred Findings Carried Forward with Explicit Dispositions (8 findings)

1. **`mcr43-context`** (`2` targets: `CHEBI:59064`, `CHEBI:59673`; `carried_from: mcr43-context`, Issue `#1140`) — `deferred`.
2. **`eatav-compound`** (`1` target: `CHEBI:8269`; `carried_from: eatav-compound`, Issue `#1141`) — `deferred`.
3. **`msrc-evidence`** (`2` targets: `CHEBI:42355`, `CHEBI:8732`; `carried_from: msrc-evidence`, Issue `#1143`) — `deferred`.
4. **`ddl-scope`** (`1` target: `CHEBI:28001`; `carried_from: ddl-scope`, Issue `#1144`) — `deferred`.
5. **`mexjk-role-conflict`** (`4` targets: `CHEBI:42355`, `CHEBI:27902`, `CHEBI:164200`, `antibioticmech:aro-1fe0873afd`; `carried_from: mexjk-role-conflict`, Issue `#1142`) — `deferred`.
6. **`reviewed-records-awaiting-causal-graphs`** (`56` targets: `55` `REVIEWED` records + `antibioticmech:aro-2eea3233f3` ofloxacin; `carried_from: reviewed-records-awaiting-causal-graphs`, Issue `#1257`) — `deferred`.
7. **`proposed-antibacterial-records-awaiting-grounding-and-mechanism`** (`112` targets; `carried_from: proposed-antibacterial-records-awaiting-grounding-and-mechanism`, Issue `#1258`) — `deferred`.
8. **`minted-aro-records-without-exact-chebi-structure`** (`240` targets; `carried_from: minted-aro-records-without-exact-chebi-structure`, Issue `#1259`) — `deferred`.
