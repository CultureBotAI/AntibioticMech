# AntibioticMech Cycle 6 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `6`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Source Revision**: `0de923c93426655dc335c3d92c6cda77dcc55d55`
- **Single-Record Review Bundle**: `reviews/structured/20261105T153000Z-obafluorin-record-review/review.yaml` (`.claude/skills/review-yaml-record/SKILL.md`)
- **Full-Inventory Cohort Review Bundle**: `reviews/structured/20261105T153100Z-cycle6-frozen-inventory-cohort-review/review.yaml` (`.claude/skills/review-yaml-category/SKILL.md`)

## 1. Frozen Inventory & Validation Census

All **3,086** `AntibioticRecord` YAML files under `data/antibiotics/` at commit `0de923c93426655dc335c3d92c6cda77dcc55d55` were audited without modifying any scientific YAML records:

| Metric | Value |
| --- | ---: |
| Total `AntibioticRecord` files | 3,086 |
| `SEEDED` / `REVIEWED` / `PROPOSED` | 2,810 / 127 / 149 |
| `EXACT` / `MINTED` grounding | 2,759 / 327 (`240` `SEEDED` `antibioticmech:aro-*` + `87` `PROPOSED` `antibioticmech:curator-*`) |
| Records with `causal_graphs` | 83 (`82` `REVIEWED` + `1` `SEEDED`/`MINTED` ofloxacin; `84` graphs; `64/64` `GENE_OR_PROTEIN` nodes carry `121` reviewed `UniProtKB` `protein_examples` + `22` non-protein graphs held) |
| Records with `PRIMARY_LITERATURE` `molecular_targets` | 166 (`127` `REVIEWED` + `39` `PROPOSED` total across `172` target entries: `83` targets carry `152` reviewed `UniProtKB` `protein_examples`, `89` non-protein/complex targets explicitly held in `curation/uniprot_protein_examples.yaml`, `0` unaccounted) |
| `scripts/validate_strict.py --quiet --workers 4` | `0` errors across `3,086` files |
| `scripts/verify_corpus.py --summary` | `0` errors across `3,086` files (`127/127` `REVIEWED` have `EXACT` grounding + `chemical_structure`) |

### Partition by Antimicrobial Class Directory (`boundary_decisions[0]`)

| Directory | Record Count |
| --- | ---: |
| `data/antibiotics/antibacterial/` | 1,166 |
| `data/antibiotics/antifungal/` | 612 |
| `data/antibiotics/antiviral/` | 473 |
| `data/antibiotics/unspecified/` | 472 |
| `data/antibiotics/antiprotozoal/` | 254 |
| `data/antibiotics/antimycobacterial/` | 78 |
| `data/antibiotics/biocide/` | 31 |
| **Total** | **3,086** |

### Partition by Curation-Readiness Cohort (`boundary_decisions[1]`)

| Cohort | Record Count |
| --- | ---: |
| `REVIEWED` records with primary-literature `causal_graphs` | 82 |
| `REVIEWED` records awaiting primary-literature `causal_graphs` | 45 |
| `PROPOSED` records with `PRIMARY_LITERATURE` `molecular_targets` and `mode_of_action` | 39 (`8` `EXACT` + `31` `MINTED`) |
| `PROPOSED` `EXACT` Cycle 6 Stage 1 natural products ready for primary mechanism/target curation | 5 (`5` `EXACT`) |
| `PROPOSED` records awaiting primary mechanism curation | 105 (`49` `EXACT` + `56` `MINTED`) |
| `SEEDED` baseline records | 2,810 (`2,570` `EXACT` + `240` `MINTED`) |
| **Total** | **3,086** |

## 2. Single-Record Deep Review (`20261105T153000Z-obafluorin-record-review`)

- **Target**: `CHEBI:199965` (`data/antibiotics/antibacterial/obafluorin.yaml`)
- **Verdict**: `needs_curation` (`NEEDS_CURATION`)
- **Verified Support**: Exact `C17H14N2O7` chemical structure (`AINNQKIVZOTQBB-KGLIPLIRSA-N`, PubChem CID `146354`), `CURATOR` discovery and mechanism evidence (`DOI:10.1038/nchembio.2374`, `PMID:28504677`; `DOI:10.1038/ncomms15935`, `PMID:28649989`; `DOI:10.1021/acschembio.9b00590`, `PMID:31675206`), MIBiG `BGC0001437` producer `Pseudomonas fluorescens` (`NCBITaxon:294`), `biosynthesis_origin: NATURAL_PRODUCT`, `mode_of_action: PROTEIN_SYNTHESIS_INHIBITION` (`MICROBIAL_TARGET`), and `PRIMARY_LITERATURE` `molecular_targets[0]` for bacterial threonyl-tRNA synthetase (`ThrRS / ThrS`, `GO:0004829`) with 1 reviewed Swiss-Prot `UniProtKB` `protein_example` (`UniProtKB:P0A8M3`).
- **Open Finding**: `obafluorin-awaiting-reviewed-promotion` (`issue_key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`) — retains `curation_status: PROPOSED` despite meeting all `REVIEWED` gate criteria.

## 3. Stable Findings & Dispositions (`20261105T153100Z-cycle6-frozen-inventory-cohort-review`)

### Open Findings for Cycle 6 Stage 5 Grouped Remediation (3 findings, 18 records)

1. **`proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`** (`major`, `open`, `8` targets: `CHEBI:199044` `berninamycin A`, `CHEBI:205987` `berninamycin B`, `CHEBI:222785` `empedopeptin`, `CHEBI:219296` `laterocidine`, `CHEBI:199965` `obafluorin`, `CHEBI:227666` `salinamide A`, `CHEBI:200517` `salinamide B`, `CHEBI:80106` `rimocidin`):
   - Have `grounding_status: EXACT`, complete single-molecule `chemical_structure`, curated `biosynthesis_origin: NATURAL_PRODUCT`, curated `mode_of_action` (`PROTEIN_SYNTHESIS_INHIBITION` on `berninamycin A`, `berninamycin B`, and `obafluorin`; `CELL_WALL_SYNTHESIS_INHIBITION` on `empedopeptin`; `MEMBRANE_DISRUPTION` on `laterocidine` and `rimocidin`; `NUCLEIC_ACID_SYNTHESIS_INHIBITION` on `salinamide A` and `salinamide B`), and `PRIMARY_LITERATURE` `molecular_targets` with complete `UniProtKB` accounting, yet remain `curation_status: PROPOSED`.
2. **`cycle6-stage1-proposed-exact-natural-products-missing-mechanism-and-targets`** (`major`, `open`, `5` targets: `CHEBI:225841` `kendomycin B`, `CHEBI:201881` `marinopyrrole C`, `CHEBI:206310` `marinopyrrole D`, `CHEBI:199931` `marinopyrrole E`, `CHEBI:223870` `amipurimycin`):
   - All 5 `PROPOSED`/`EXACT` natural-product records seeded in Cycle 6 Stage 1 have complete `chemical_structure`, curated `biosynthesis_origin: NATURAL_PRODUCT`, and primary-literature discovery/biosynthetic citations (`Chen et al. 2021 PMID:34940672` / `Zhang et al. 2019 PMID:30843714` for `kendomycin B`; `Hughes et al. 2010 PMID:20405892` / `Yamanaka et al. 2012 PMID:22800473` for `marinopyrrole C`, `marinopyrrole D`, and `marinopyrrole E`; `Kang et al. 2019 PMID:30990701` / `Harada et al. 1977 PMID:838626` for `amipurimycin`), but lack `mode_of_action`, structured `PRIMARY_LITERATURE` `molecular_targets` (with `UniProtKB` accounting), and `REVIEWED` promotion.
3. **`seeded-exact-sulfonamides-with-card-only-targets-awaiting-primary-literature-promotion`** (`major`, `open`, `5` targets: `CHEBI:63845` `sulfacetamide`, `CHEBI:102265` `sulfamethazine`, `CHEBI:9331` `sulfamethizole`, `CHEBI:9332` `sulfamethoxazole`, `CHEBI:9328` `sulfadiazine`):
   - All 5 `SEEDED`/`EXACT` sulfonamide records have complete ChEBI `chemical_structure` and `CARD_ARO` target assertions (`PRIMARY_EVIDENCE_NEEDED`) but lack `biosynthesis_origin: SYNTHETIC`, curator-reviewed `mode_of_action_notes` (`MICROBIAL_TARGET`), structured `PRIMARY_LITERATURE` `molecular_targets` (with reviewed `UniProtKB` `protein_examples`), and `REVIEWED` promotion.

### Deferred Findings Carried Forward with Explicit Dispositions (8 findings)

1. **`mcr43-context`** (`2` targets: `CHEBI:59064`, `CHEBI:59673`; `carried_from: mcr43-context`, Issue `#1140`) — `deferred`.
2. **`eatav-compound`** (`1` target: `CHEBI:8269`; `carried_from: eatav-compound`, Issue `#1141`) — `deferred`.
3. **`msrc-evidence`** (`2` targets: `CHEBI:42355`, `CHEBI:8732`; `carried_from: msrc-evidence`, Issue `#1143`) — `deferred`.
4. **`ddl-scope`** (`1` target: `CHEBI:28001`; `carried_from: ddl-scope`, Issue `#1144`) — `deferred`.
5. **`mexjk-role-conflict`** (`4` targets: `CHEBI:42355`, `CHEBI:27902`, `CHEBI:164200`, `antibioticmech:aro-1fe0873afd`; `carried_from: mexjk-role-conflict`, Issue `#1142`) — `deferred`.
6. **`reviewed-records-awaiting-causal-graphs`** (`46` targets: `45` `REVIEWED` records + `antibioticmech:aro-2eea3233f3` ofloxacin; `carried_from: reviewed-records-awaiting-causal-graphs`, Issue `#1257`) — `deferred`.
7. **`proposed-antibacterial-records-awaiting-grounding-and-mechanism`** (`105` targets; `carried_from: proposed-antibacterial-records-awaiting-grounding-and-mechanism`, Issue `#1258`) — `deferred`.
8. **`minted-aro-records-without-exact-chebi-structure`** (`240` targets; `carried_from: minted-aro-records-without-exact-chebi-structure`, Issue `#1259`) — `deferred`.
