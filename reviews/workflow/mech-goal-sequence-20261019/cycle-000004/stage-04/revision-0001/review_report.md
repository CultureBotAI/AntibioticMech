# AntibioticMech Cycle 4 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `4`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Source Revision**: `fd66617286f55b8f9bf6802bf44d24bcee32959c`
- **Single-Record Review Bundle**: `reviews/structured/20261103T053500Z-squalestatin-s1-record-review/review.yaml` (`.claude/skills/review-yaml-record/SKILL.md`)
- **Full-Inventory Cohort Review Bundle**: `reviews/structured/20261103T053600Z-cycle4-frozen-inventory-cohort-review/review.yaml` (`.claude/skills/review-yaml-category/SKILL.md`)

## 1. Frozen Inventory & Validation Census

All **3,042** `AntibioticRecord` YAML files under `data/antibiotics/` at commit `fd66617286f55b8f9bf6802bf44d24bcee32959c` were audited without modifying any scientific YAML records:

| Metric | Value |
| --- | ---: |
| Total `AntibioticRecord` files | 3,042 |
| `SEEDED` / `REVIEWED` / `PROPOSED` | 2,819 / 101 / 122 |
| `EXACT` / `MINTED` grounding | 2,721 / 321 (`240` `SEEDED` `antibioticmech:aro-*` + `81` `PROPOSED` `antibioticmech:curator-*`) |
| Records with `chemical_structure` / without `chemical_structure` | 2,800 / 242 |
| Records with `causal_graphs` | 69 (`68` `REVIEWED` + `1` `SEEDED`/`MINTED` ofloxacin; `70` graphs; `50/50` `GENE_OR_PROTEIN` nodes carry `75` reviewed `UniProtKB` `protein_examples` + `22` non-protein graphs held) |
| Records with `PRIMARY_LITERATURE` `molecular_targets` | 129 (`101` `REVIEWED` + `28` `PROPOSED` total across `135` target entries: `64` targets carry `99` reviewed `UniProtKB` `protein_examples`, `71` non-protein/complex targets explicitly held in `curation/uniprot_protein_examples.yaml`, `0` unaccounted) |
| `scripts/validate_strict.py --quiet --workers 4` | `0` errors across `3,042` files |
| `scripts/verify_corpus.py --summary` | `0` errors across `3,042` files (`101/101` `REVIEWED` have `EXACT` grounding + `chemical_structure`) |

### Partition by Antimicrobial Class Directory (`boundary_decisions[0]`)

| Directory | Record Count |
| --- | ---: |
| `data/antibiotics/antibacterial/` | 1,134 |
| `data/antibiotics/antifungal/` | 604 |
| `data/antibiotics/antiviral/` | 474 |
| `data/antibiotics/unspecified/` | 472 |
| `data/antibiotics/antiprotozoal/` | 249 |
| `data/antibiotics/antimycobacterial/` | 78 |
| `data/antibiotics/biocide/` | 31 |
| **Total** | **3,042** |

### Partition by Curation-Readiness Cohort (`boundary_decisions[1]`)

| Cohort | Record Count |
| --- | ---: |
| `REVIEWED` records with primary-literature `causal_graphs` | 68 |
| `REVIEWED` records awaiting primary-literature `causal_graphs` | 33 |
| `PROPOSED` records with `PRIMARY_LITERATURE` `molecular_targets` and `mode_of_action` | 28 (`1` `EXACT` + `27` `MINTED`) |
| `PROPOSED` `EXACT` Cycle 4 Stage 1 natural products ready for primary mechanism/target curation | 6 (`6` `EXACT`) |
| `PROPOSED` records awaiting primary mechanism curation | 88 (`34` `EXACT` + `54` `MINTED`) |
| `SEEDED` baseline records | 2,819 (`2,579` `EXACT` + `240` `MINTED`) |
| **Total** | **3,042** |

## 2. Single-Record Deep Review (`20261103T053500Z-squalestatin-s1-record-review`)

- **Target**: `CHEBI:220211` (`data/antibiotics/antifungal/squalestatin-s1.yaml`)
- **Verdict**: `needs_curation` (`NEEDS_CURATION`)
- **Verified Support**: Exact `C35H46O13` chemical structure (`KKQOCSPYLTUDES-KVBVMKTNSA-N`, PubChem CID `139586329`), `CURATOR` discovery and mechanism evidence (`DOI:10.1039/c6cc02130a`, `PMID:27032439`; `DOI:10.7164/antibiotics.45.639`, `PMID:1624366`; `DOI:10.1073/pnas.90.1.80`, `PMID:8419946`), `biosynthesis_origin: NATURAL_PRODUCT`, `mode_of_action: ERGOSTEROL_PATHWAY_INHIBITION` (`HOST_SHARED_TARGET`), and `PRIMARY_LITERATURE` `molecular_targets[0]` for fungal squalene synthase (`Erg9`, `GO:0051996`) with 3 reviewed Swiss-Prot `UniProtKB` `protein_examples` (`UniProtKB:P78589`, `UniProtKB:A0A1D8PI71`, `UniProtKB:P29704`).
- **Open Finding**: `squalestatin-s1-awaiting-reviewed-promotion` (`issue_key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`) — retains `curation_status: PROPOSED` despite meeting all `REVIEWED` gate criteria.

## 3. Stable Findings & Dispositions (`20261103T053600Z-cycle4-frozen-inventory-cohort-review`)

### Open Findings for Cycle 4 Stage 5 Grouped Remediation (3 findings, 11 records)

1. **`proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`** (`major`, `open`, `1` target: `CHEBI:220211` `squalestatin S1`):
   - Has `grounding_status: EXACT`, complete single-molecule `chemical_structure`, curated `biosynthesis_origin: NATURAL_PRODUCT`, curated `mode_of_action: ERGOSTEROL_PATHWAY_INHIBITION` (`HOST_SHARED_TARGET`), `PRIMARY_LITERATURE` `molecular_targets` (`GO:0051996`), and 3 reviewed `UniProtKB` `protein_examples` (`P78589`, `A0A1D8PI71`, `P29704`), yet remains `curation_status: PROPOSED`.
2. **`cycle4-stage1-proposed-exact-natural-products-missing-mechanism-and-targets`** (`major`, `open`, `6` targets: `CHEBI:199753` `diazaquinomycin H`, `CHEBI:225769` `diazaquinomycin J`, `CHEBI:221686` `jessenipeptin`, `CHEBI:224130` `minimycin`, `CHEBI:219230` `pamamycin-621A`, `CHEBI:198952` `pamamycin-649B`):
   - All 6 `PROPOSED`/`EXACT` natural-product records seeded in Cycle 4 Stage 1 have complete `chemical_structure`, curated `biosynthesis_origin: NATURAL_PRODUCT`, and primary-literature mechanism characterization, but lack `mode_of_action`, structured `PRIMARY_LITERATURE` `molecular_targets` (with `UniProtKB` accounting), and `REVIEWED` promotion.
3. **`seeded-exact-fluoroquinolones-with-card-only-targets-awaiting-primary-literature-promotion`** (`major`, `open`, `4` targets: `CHEBI:157175` `enoxacin`, `CHEBI:31810` `fleroxacin`, `CHEBI:5280` `gatifloxacin`, `CHEBI:9763` `trovafloxacin`):
   - All 4 `SEEDED`/`EXACT` fluoroquinolone records have complete ChEBI `chemical_structure` and `CARD_ARO` target assertions (`PRIMARY_EVIDENCE_NEEDED`) but lack `biosynthesis_origin: SYNTHETIC`, curator-reviewed `mode_of_action_notes` (`MICROBIAL_TARGET`), structured `PRIMARY_LITERATURE` `molecular_targets` (with reviewed `UniProtKB` `protein_examples`), and `REVIEWED` promotion.

### Deferred Findings Carried Forward with Explicit Dispositions (8 findings)

1. **`mcr43-context`** (`2` targets: `CHEBI:59064`, `CHEBI:59673`; `carried_from: mcr43-context`, Issue `#1140`) — `deferred`.
2. **`eatav-compound`** (`1` target: `CHEBI:8269`; `carried_from: eatav-compound`, Issue `#1141`) — `deferred`.
3. **`msrc-evidence`** (`2` targets: `CHEBI:42355`, `CHEBI:8732`; `carried_from: msrc-evidence`, Issue `#1143`) — `deferred`.
4. **`ddl-scope`** (`1` target: `CHEBI:28001`; `carried_from: ddl-scope`, Issue `#1144`) — `deferred`.
5. **`mexjk-role-conflict`** (`4` targets: `CHEBI:42355`, `CHEBI:27902`, `CHEBI:164200`, `antibioticmech:aro-1fe0873afd`; `carried_from: mexjk-role-conflict`, Issue `#1142`) — `deferred`.
6. **`reviewed-records-awaiting-causal-graphs`** (`34` targets: `33` `REVIEWED` records + `antibioticmech:aro-2eea3233f3` ofloxacin; `carried_from: reviewed-records-awaiting-causal-graphs`, Issue `#1257`) — `deferred`.
7. **`proposed-antibacterial-records-awaiting-grounding-and-mechanism`** (`88` targets; `carried_from: proposed-antibacterial-records-awaiting-grounding-and-mechanism`, Issue `#1258`) — `deferred`.
8. **`minted-aro-records-without-exact-chebi-structure`** (`240` targets; `carried_from: minted-aro-records-without-exact-chebi-structure`, Issue `#1259`) — `deferred`.
