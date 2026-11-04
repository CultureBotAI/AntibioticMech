# AntibioticMech Cycle 5 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `5`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Source Revision**: `47746980c7f56e7d9a37ebb7eb4d475d3a7ea6e5`
- **Single-Record Review Bundle**: `reviews/structured/20261104T152500Z-rustmicin-record-review/review.yaml` (`.claude/skills/review-yaml-record/SKILL.md`)
- **Full-Inventory Cohort Review Bundle**: `reviews/structured/20261104T152600Z-cycle5-frozen-inventory-cohort-review/review.yaml` (`.claude/skills/review-yaml-category/SKILL.md`)

## 1. Frozen Inventory & Validation Census

All **3,064** `AntibioticRecord` YAML files under `data/antibiotics/` at commit `47746980c7f56e7d9a37ebb7eb4d475d3a7ea6e5` were audited without modifying any scientific YAML records:

| Metric | Value |
| --- | ---: |
| Total `AntibioticRecord` files | 3,064 |
| `SEEDED` / `REVIEWED` / `PROPOSED` | 2,815 / 112 / 137 |
| `EXACT` / `MINTED` grounding | 2,740 / 324 (`240` `SEEDED` `antibioticmech:aro-*` + `84` `PROPOSED` `antibioticmech:curator-*`) |
| Records with `causal_graphs` | 75 (`74` `REVIEWED` + `1` `SEEDED`/`MINTED` ofloxacin; `76` graphs; `56/56` `GENE_OR_PROTEIN` nodes carry `96` reviewed `UniProtKB` `protein_examples` + `22` non-protein graphs held) |
| Records with `PRIMARY_LITERATURE` `molecular_targets` | 145 (`112` `REVIEWED` + `33` `PROPOSED` total across `151` target entries: `73` targets carry `124` reviewed `UniProtKB` `protein_examples`, `78` non-protein/complex targets explicitly held in `curation/uniprot_protein_examples.yaml`, `0` unaccounted) |
| `scripts/validate_strict.py --quiet --workers 4` | `0` errors across `3,064` files |
| `scripts/verify_corpus.py --summary` | `0` errors across `3,064` files (`112/112` `REVIEWED` have `EXACT` grounding + `chemical_structure`) |

### Partition by Antimicrobial Class Directory (`boundary_decisions[0]`)

| Directory | Record Count |
| --- | ---: |
| `data/antibiotics/antibacterial/` | 1,147 |
| `data/antibiotics/antifungal/` | 609 |
| `data/antibiotics/antiviral/` | 473 |
| `data/antibiotics/unspecified/` | 472 |
| `data/antibiotics/antiprotozoal/` | 254 |
| `data/antibiotics/antimycobacterial/` | 78 |
| `data/antibiotics/biocide/` | 31 |
| **Total** | **3,064** |

### Partition by Curation-Readiness Cohort (`boundary_decisions[1]`)

| Cohort | Record Count |
| --- | ---: |
| `REVIEWED` records with primary-literature `causal_graphs` | 74 |
| `REVIEWED` records awaiting primary-literature `causal_graphs` | 38 |
| `PROPOSED` records with `PRIMARY_LITERATURE` `molecular_targets` and `mode_of_action` | 33 (`5` `EXACT` + `28` `MINTED`) |
| `PROPOSED` `EXACT` Cycle 5 Stage 1 natural products ready for primary mechanism/target curation | 5 (`5` `EXACT`) |
| `PROPOSED` records awaiting primary mechanism curation | 99 (`43` `EXACT` + `56` `MINTED`) |
| `SEEDED` baseline records | 2,815 (`2,575` `EXACT` + `240` `MINTED`) |
| **Total** | **3,064** |

## 2. Single-Record Deep Review (`20261104T152500Z-rustmicin-record-review`)

- **Target**: `CHEBI:206910` (`data/antibiotics/antifungal/rustmicin.yaml`)
- **Verdict**: `needs_curation` (`NEEDS_CURATION`)
- **Verified Support**: Exact `C21H34O6` chemical structure (`WZROUGNDADCPAJ-VOCSLKHZSA-N`, PubChem CID `10063700`), `CURATOR` discovery and mechanism evidence (`DOI:10.1074/jbc.273.24.14942`, `PMID:9614099`; `DOI:10.7164/antibiotics.51.837`, `PMID:9820234`; `DOI:10.1016/j.chembiol.2013.11.014`, `PMID:24361047`), `biosynthesis_origin: NATURAL_PRODUCT`, `mode_of_action: LIPID_BIOSYNTHESIS_INHIBITION` (`MICROBIAL_TARGET`), and `PRIMARY_LITERATURE` `molecular_targets[0]` for fungal inositol phosphorylceramide synthase (`Aur1 / Ipc1`, `GO:0052645`) with 2 reviewed Swiss-Prot `UniProtKB` `protein_examples` (`UniProtKB:P36107`, `UniProtKB:O13332`).
- **Open Finding**: `rustmicin-awaiting-reviewed-promotion` (`issue_key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`) — retains `curation_status: PROPOSED` despite meeting all `REVIEWED` gate criteria.

## 3. Stable Findings & Dispositions (`20261104T152600Z-cycle5-frozen-inventory-cohort-review`)

### Open Findings for Cycle 5 Stage 5 Grouped Remediation (3 findings, 15 records)

1. **`proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`** (`major`, `open`, `5` targets: `CHEBI:70619` `pentabromopseudilin`, `CHEBI:219845` `taromycin A`, `CHEBI:198520` `pneumocandin A0`, `CHEBI:206910` `rustmicin`, `CHEBI:9200` `soraphen A`):
   - Have `grounding_status: EXACT`, complete single-molecule `chemical_structure`, curated `biosynthesis_origin: NATURAL_PRODUCT`, curated `mode_of_action`, and `PRIMARY_LITERATURE` `molecular_targets` with complete `UniProtKB` accounting, yet remain `curation_status: PROPOSED`.
2. **`cycle5-stage1-proposed-exact-natural-products-missing-mechanism-and-targets`** (`major`, `open`, `5` targets: `CHEBI:197824` `naphthomycin A`, `CHEBI:29671` `resistomycin`, `CHEBI:198957` `micacocidin`, `CHEBI:191052` `kendomycin`, `CHEBI:218214` `endophenazine A`):
   - All 5 `PROPOSED`/`EXACT` natural-product records seeded in Cycle 5 Stage 1 have complete `chemical_structure`, curated `biosynthesis_origin: NATURAL_PRODUCT`, and primary-literature mechanism characterization, but lack `mode_of_action`, structured `PRIMARY_LITERATURE` `molecular_targets` (with `UniProtKB` accounting), and `REVIEWED` promotion.
3. **`seeded-exact-fluoroquinolones-with-card-only-targets-awaiting-primary-literature-promotion`** (`major`, `open`, `5` targets: `CHEBI:3716` `cinoxacin`, `CHEBI:5543` `Grepafloxacin`, `CHEBI:63611` `moxifloxacin`, `CHEBI:9212` `sparfloxacin`, `CHEBI:116278` `lomefloxacin`):
   - All 5 `SEEDED`/`EXACT` quinolone/fluoroquinolone records have complete ChEBI `chemical_structure` and `CARD_ARO` target assertions (`PRIMARY_EVIDENCE_NEEDED`) but lack `biosynthesis_origin: SYNTHETIC`, curator-reviewed `mode_of_action_notes` (`MICROBIAL_TARGET`), structured `PRIMARY_LITERATURE` `molecular_targets` (with reviewed `UniProtKB` `protein_examples`), and `REVIEWED` promotion.

### Deferred Findings Carried Forward with Explicit Dispositions (8 findings)

1. **`mcr43-context`** (`2` targets: `CHEBI:59064`, `CHEBI:59673`; `carried_from: mcr43-context`, Issue `#1140`) — `deferred`.
2. **`eatav-compound`** (`1` target: `CHEBI:8269`; `carried_from: eatav-compound`, Issue `#1141`) — `deferred`.
3. **`msrc-evidence`** (`2` targets: `CHEBI:42355`, `CHEBI:8732`; `carried_from: msrc-evidence`, Issue `#1143`) — `deferred`.
4. **`ddl-scope`** (`1` target: `CHEBI:28001`; `carried_from: ddl-scope`, Issue `#1144`) — `deferred`.
5. **`mexjk-role-conflict`** (`4` targets: `CHEBI:42355`, `CHEBI:27902`, `CHEBI:164200`, `antibioticmech:aro-1fe0873afd`; `carried_from: mexjk-role-conflict`, Issue `#1142`) — `deferred`.
6. **`reviewed-records-awaiting-causal-graphs`** (`39` targets: `38` `REVIEWED` records + `antibioticmech:aro-2eea3233f3` ofloxacin; `carried_from: reviewed-records-awaiting-causal-graphs`, Issue `#1257`) — `deferred`.
7. **`proposed-antibacterial-records-awaiting-grounding-and-mechanism`** (`99` targets; `carried_from: proposed-antibacterial-records-awaiting-grounding-and-mechanism`, Issue `#1258`) — `deferred`.
8. **`minted-aro-records-without-exact-chebi-structure`** (`240` targets; `carried_from: minted-aro-records-without-exact-chebi-structure`, Issue `#1259`) — `deferred`.
