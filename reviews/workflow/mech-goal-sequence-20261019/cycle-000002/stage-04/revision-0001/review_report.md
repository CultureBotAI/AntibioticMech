# AntibioticMech Cycle 2 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Source Revision**: `bfc2881eb4543729f96eade32084c147fa07acdb`
- **Single-Record Review Bundle**: `reviews/structured/20261025T081800Z-fabimycin-record-review/review.yaml` (`.claude/skills/review-yaml-record/SKILL.md`)
- **Full-Inventory Cohort Review Bundle**: `reviews/structured/20261025T082000Z-cycle2-frozen-inventory-cohort-review/review.yaml` (`.claude/skills/review-yaml-category/SKILL.md`)

## 1. Frozen Inventory & Validation Census

All **2,992** `AntibioticRecord` YAML files under `data/antibiotics/` at commit `bfc2881eb4543729f96eade32084c147fa07acdb` were audited without modifying any scientific YAML records:

| Metric | Value |
| --- | ---: |
| Total `AntibioticRecord` files | 2,992 |
| `SEEDED` / `REVIEWED` / `PROPOSED` | 2,819 / 90 / 83 |
| `EXACT` / `MINTED` grounding | 2,697 / 295 (`240` `SEEDED` `antibioticmech:aro-*` + `55` `PROPOSED` `antibioticmech:curator-*`) |
| Records with `chemical_structure` / without `chemical_structure` | 2,750 / 242 |
| Records with `causal_graphs` | 59 (`58` `REVIEWED` + `1` `SEEDED`/`MINTED` ofloxacin; `42/42` `GENE_OR_PROTEIN` nodes carry reviewed `UniProtKB` `protein_examples`) |
| Records with `PRIMARY_LITERATURE` `molecular_targets` | 108 (`90` `REVIEWED` + `17` `PROPOSED` + `1` `SEEDED` ofloxacin; `73` targets carry reviewed `UniProtKB` `protein_examples`, `25` protein/defined-complex targets explicitly held in `curation/uniprot_protein_examples.yaml`) |
| `scripts/validate_strict.py --quiet --workers 2` | `0` errors across `2,992` files |
| `scripts/verify_corpus.py` | `0` errors across `2,992` files |
| `scripts/structure_completeness_audit.py` | `0` `REVIEWED` gate violations (`90/90` `REVIEWED` have `EXACT` grounding + `chemical_structure`) |

### Partition by Antimicrobial Class Directory (`boundary_decisions[0]`)

| Directory | Record Count |
| --- | ---: |
| `data/antibiotics/antibacterial/` | 1,091 |
| `data/antibiotics/antifungal/` | 599 |
| `data/antibiotics/antiviral/` | 473 |
| `data/antibiotics/unspecified/` | 472 |
| `data/antibiotics/antiprotozoal/` | 248 |
| `data/antibiotics/antimycobacterial/` | 78 |
| `data/antibiotics/biocide/` | 31 |
| **Total** | **2,992** |

### Partition by Curation-Readiness Cohort (`boundary_decisions[1]`)

| Cohort | Record Count |
| --- | ---: |
| `REVIEWED` records with primary-literature `causal_graphs` | 58 |
| `REVIEWED` records awaiting primary-literature `causal_graphs` | 32 |
| `PROPOSED` records with `PRIMARY_LITERATURE` `molecular_targets` | 17 (`6` `EXACT` + `11` `MINTED`) |
| `PROPOSED` records awaiting primary mechanism curation | 66 (`22` `EXACT` + `44` `MINTED`) |
| `SEEDED` baseline records | 2,819 (`2,579` `EXACT` + `240` `MINTED`) |
| **Total** | **2,992** |

## 2. Single-Record Deep Review (`20261025T081800Z-fabimycin-record-review`)

- **Target**: `antibioticmech:curator-47d32d7a07` (`data/antibiotics/antibacterial/fabimycin.yaml`)
- **Verdict**: `needs_curation` (`NEEDS_CURATION`)
- **Verified Support**: Exact `C23H24N4O3` chemical structure (`ZWQNEFFHBSGFHV-HKMNZKMDSA-N`, PubChem CID `134159600`), `CURATOR` discovery evidence (`DOI:10.1021/acscentsci.2c00598`, `PMID:36035943`), `PRIMARY_LITERATURE` `molecular_targets` entry for bacterial enoyl-acyl carrier protein reductase (FabI) in *Escherichia coli* K-12 (`NCBITaxon:83333`), and reviewed `UniProtKB:P0AEK4` (`fabI`, b1288) `protein_examples`.
- **Open Finding**: `fabimycin-missing-mode-of-action-and-biosynthesis-origin` — lacks top-level `biosynthesis_origin: SYNTHETIC`, `mode_of_action: LIPID_SYNTHESIS_INHIBITION`, `mode_of_action_target_scope: MICROBIAL_TARGET`, and `CURATOR` `mode_of_action_notes`.

## 3. Stable Findings & Dispositions (`20261025T082000Z-cycle2-frozen-inventory-cohort-review`)

### Open Findings for Cycle 2 Stage 5 Grouped Remediation (3 findings, 20 records)

1. **`proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`** (`major`, `open`, `6` targets: `CHEBI:28429` `(2R,3R)-dihydromyricetin`, `CHEBI:228412` `6-methylflavone`, `CHEBI:48480` `thermorubin A`, `CHEBI:10100` `zafirlukast`, `CHEBI:34825` `luliconazole`, `CHEBI:188153` `oteseconazole`):
   - All 6 records have `grounding_status: EXACT`, complete single-molecule `chemical_structure`, curated `biosynthesis_origin`, curated `mode_of_action` + `mode_of_action_target_scope: MICROBIAL_TARGET` + `CURATOR` `mode_of_action_notes`, and `source: PRIMARY_LITERATURE` (`evidence_status: PRIMARY_EVIDENCE`) `molecular_targets` (with reviewed `UniProtKB` `protein_examples` on all 4 protein-targeted records), yet remain `curation_status: PROPOSED`.
2. **`proposed-minted-records-with-primary-targets-missing-mode-of-action`** (`major`, `open`, `11` targets: `antibioticmech:curator-cb71d1e3b5` `enterololin`, `antibioticmech:curator-47d32d7a07` `fabimycin`, `antibioticmech:curator-172bfdd938` `ganfeborole`, `antibioticmech:curator-1db8575797` `lolamicin`, `antibioticmech:curator-607ce000f8` `macozinone`, `antibioticmech:curator-88af230f5d` `quabodepistat`, `antibioticmech:curator-0106724e5f` `sorfequiline`, `antibioticmech:curator-17023fe654` `telacebec`, `antibioticmech:curator-fd1c955758` `ibrexafungerp`, `antibioticmech:curator-4a1156c964` `manogepix`, `antibioticmech:curator-18f8e84826` `olorofim`):
   - All 11 `PROPOSED`/`MINTED` records received curated `PRIMARY_LITERATURE` `molecular_targets` (and reviewed `UniProtKB` `protein_examples` on 8 of them) in Cycle 2 Stage 3 (`PR #1266`), but still lack top-level `biosynthesis_origin`, `mode_of_action`, `mode_of_action_target_scope`, and `CURATOR` `mode_of_action_notes`.
3. **`unreviewed-seeded-pdb-structural-observations`** (`minor`, `open`, `3` targets: `CHEBI:138488` `alsterpaullone` `PDB:1Q3W`, `CHEBI:28971` `ampicillin` `PDB:1H8S`, `CHEBI:44499` `methyl nonanoate` `PDB:1CLY`; `carried_from: unreviewed-seeded-pdb-structural-observations`):
   - Unblocked by Cycle 1 Stage 6 (`PR #1261`), which updated `scripts/seed_from_sources.py` to preserve curator-reviewed `structural_observations` across reseeding when `relevance` is not `UNREVIEWED`.

### Deferred Findings Carried Forward with Explicit Dispositions (8 findings)

1. **`mcr43-context`** (`2` targets: `CHEBI:59064`, `CHEBI:59673`; `carried_from: mcr43-context`, Issue `#1140`) — `deferred`: component-specific experimental testing for MCR-4.3 requires external experimental data not in local cached sources.
2. **`eatav-compound`** (`1` target: `CHEBI:8269`; `carried_from: eatav-compound`, Issue `#1141`) — `deferred`: `PMID:23751969` tested tiamulin rather than parent pleuromutilin; qualified via `curation/card_evidence_reviews.json`.
3. **`msrc-evidence`** (`2` targets: `CHEBI:42355`, `CHEBI:8732`; `carried_from: msrc-evidence`, Issue `#1143`) — `deferred`: awaits primary mechanistic causality evidence and native gene-field representation.
4. **`ddl-scope`** (`1` target: `CHEBI:28001`; `carried_from: ddl-scope`, Issue `#1144`) — `deferred`: `PMID:11266628` full text remains under publisher HTTP 403 hold.
5. **`mexjk-role-conflict`** (`4` targets: `CHEBI:42355`, `CHEBI:27902`, `CHEBI:164200`, `antibioticmech:aro-1fe0873afd`; `carried_from: mexjk-role-conflict`, Issue `#1142`) — `deferred`: `PMID:12193619`/`PMID:12951344` remain under publisher HTTP 403 hold.
6. **`reviewed-records-awaiting-causal-graphs`** (`33` targets: `32` `REVIEWED` records + `antibioticmech:aro-2eea3233f3` ofloxacin; `carried_from: reviewed-records-awaiting-causal-graphs`, Issue `#1257`) — `deferred`: reduced from 40 to 33 targets after Cycle 2 Stage 2 curated 7 additional causal graphs; remaining multi-compound causal-graph curation is a multi-cycle expansion task.
7. **`proposed-antibacterial-records-awaiting-grounding-and-mechanism`** (`66` targets; `carried_from: proposed-antibacterial-records-awaiting-grounding-and-mechanism`, Issue `#1258`) — `deferred`: awaits compound-by-compound primary mechanism literature retrieval in future expansion cycles.
8. **`minted-aro-records-without-exact-chebi-structure`** (`240` targets; `carried_from: minted-aro-records-without-exact-chebi-structure`, Issue `#1259`) — `deferred`: `REVIEWED` promotion intentionally gated by `docs/HARMONIZATION.md` and `scripts/verify_corpus.py` until exact single-molecule ChEBI structures exist.
