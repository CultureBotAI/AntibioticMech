# AntibioticMech Cycle 3 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Source Revision**: `2cc3ea13020683af56460711fbff425aa2dad456`
- **Single-Record Review Bundle**: `reviews/structured/20261026T003500Z-negamycin-record-review/review.yaml` (`.claude/skills/review-yaml-record/SKILL.md`)
- **Full-Inventory Cohort Review Bundle**: `reviews/structured/20261026T003600Z-cycle3-frozen-inventory-cohort-review/review.yaml` (`.claude/skills/review-yaml-category/SKILL.md`)

## 1. Frozen Inventory & Validation Census

All **3,012** `AntibioticRecord` YAML files under `data/antibiotics/` at commit `2cc3ea13020683af56460711fbff425aa2dad456` were audited without modifying any scientific YAML records:

| Metric | Value |
| --- | ---: |
| Total `AntibioticRecord` files | 3,012 |
| `SEEDED` / `REVIEWED` / `PROPOSED` | 2,819 / 96 / 97 |
| `EXACT` / `MINTED` grounding | 2,702 / 310 (`240` `SEEDED` `antibioticmech:aro-*` + `70` `PROPOSED` `antibioticmech:curator-*`) |
| Records with `chemical_structure` / without `chemical_structure` | 2,770 / 242 |
| Records with `causal_graphs` | 64 (`63` `REVIEWED` + `1` `SEEDED`/`MINTED` ofloxacin; `65` graphs; `46/46` `GENE_OR_PROTEIN` nodes carry `82` reviewed `UniProtKB` `protein_examples` + `21` non-protein graphs held) |
| Records with `PRIMARY_LITERATURE` `molecular_targets` | 117 (`96` `REVIEWED` + `21` `PROPOSED`; `123` target entries: `59` targets carry `108` reviewed `UniProtKB` `protein_examples`, `64` non-protein/complex targets explicitly held in `curation/uniprot_protein_examples.yaml`, `0` unaccounted) |
| `scripts/validate_strict.py --quiet --workers 4` | `0` errors across `3,012` files |
| `scripts/verify_corpus.py --summary` | `0` errors across `3,012` files (`96/96` `REVIEWED` have `EXACT` grounding + `chemical_structure`) |

### Partition by Antimicrobial Class Directory (`boundary_decisions[0]`)

| Directory | Record Count |
| --- | ---: |
| `data/antibiotics/antibacterial/` | 1,108 |
| `data/antibiotics/antifungal/` | 602 |
| `data/antibiotics/antiviral/` | 473 |
| `data/antibiotics/unspecified/` | 472 |
| `data/antibiotics/antiprotozoal/` | 248 |
| `data/antibiotics/antimycobacterial/` | 78 |
| `data/antibiotics/biocide/` | 31 |
| **Total** | **3,012** |

### Partition by Curation-Readiness Cohort (`boundary_decisions[1]`)

| Cohort | Record Count |
| --- | ---: |
| `REVIEWED` records with primary-literature `causal_graphs` | 63 |
| `REVIEWED` records awaiting primary-literature `causal_graphs` | 33 |
| `PROPOSED` records with `PRIMARY_LITERATURE` `molecular_targets` and `mode_of_action` | 21 (`2` `EXACT` + `19` `MINTED`) |
| `PROPOSED` records with curated `mode_of_action` awaiting `PRIMARY_LITERATURE` `molecular_targets` | 10 (`3` `EXACT` + `7` `MINTED`) |
| `PROPOSED` records awaiting primary mechanism curation | 66 (`22` `EXACT` + `44` `MINTED`) |
| `SEEDED` baseline records | 2,819 (`2,579` `EXACT` + `240` `MINTED`) |
| **Total** | **3,012** |

## 2. Single-Record Deep Review (`20261026T003500Z-negamycin-record-review`)

- **Target**: `CHEBI:198310` (`data/antibiotics/antibacterial/negamycin.yaml`)
- **Verdict**: `needs_curation` (`NEEDS_CURATION`)
- **Verified Support**: Exact `C9H20N4O4` chemical structure (`IKHFJPZQZVMLRH-RNFRBKRXSA-N`, PubChem CID `11118411`), `CURATOR` discovery evidence (`DOI:10.1073/pnas.1414401111`, `PMID:25368144`; `DOI:10.1016/j.molcel.2014.09.021`, `PMID:25306922`), `biosynthesis_origin: NATURAL_PRODUCT`, `mode_of_action: PROTEIN_SYNTHESIS_INHIBITION` (`MICROBIAL_TARGET`), `PRIMARY_LITERATURE` `molecular_targets[0]` for bacterial 30S ribosomal subunit head domain (16S rRNA helix 34) in *Escherichia coli* (`NCBITaxon:562`), and documented `RIBOSOMAL_SUBUNIT` hold in `curation/uniprot_protein_examples.yaml`.
- **Open Finding**: `negamycin-awaiting-reviewed-promotion` (`issue_key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`) — retains `curation_status: PROPOSED` despite meeting all `REVIEWED` gate criteria.

## 3. Stable Findings & Dispositions (`20261026T003600Z-cycle3-frozen-inventory-cohort-review`)

### Open Findings for Cycle 3 Stage 5 Grouped Remediation (3 findings, 12 records)

1. **`proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`** (`major`, `open`, `2` targets: `CHEBI:138579` `bactobolin A`, `CHEBI:198310` `negamycin`; `carried_from: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`):
   - Both records have `grounding_status: EXACT`, complete single-molecule `chemical_structure`, curated `biosynthesis_origin: NATURAL_PRODUCT`, curated `mode_of_action: PROTEIN_SYNTHESIS_INHIBITION` (`MICROBIAL_TARGET`), `PRIMARY_LITERATURE` `molecular_targets`, and complete `UniProtKB` accounting (`bactobolin A` carries reviewed `UniProtKB:P42919` and `UniProtKB:P60405` `protein_examples` on uL2 / RplB, while `negamycin` carries a documented `RIBOSOMAL_SUBUNIT` hold in `curation/uniprot_protein_examples.yaml`), yet remain `curation_status: PROPOSED`.
2. **`proposed-exact-quinolones-with-moa-missing-primary-targets-and-reviewed-promotion`** (`major`, `open`, `3` targets: `CHEBI:135622` `besifloxacin`, `CHEBI:136050` `ozenoxacin`, `CHEBI:94700` `pazufloxacin`):
   - All 3 records have `grounding_status: EXACT`, complete `chemical_structure`, and curated `mode_of_action: NUCLEIC_ACID_SYNTHESIS_INHIBITION` (`MICROBIAL_TARGET`) with primary target citations in `mode_of_action_notes`/`provenance`, but lack structured `PRIMARY_LITERATURE` `molecular_targets` (with reviewed `UniProtKB` `protein_examples`) and remain `PROPOSED`.
3. **`proposed-minted-records-with-moa-missing-primary-targets`** (`major`, `open`, `7` targets: `antibioticmech:curator-975acd7c4d` `cadazolid`, `antibioticmech:curator-a739fc0555` `radezolid`, `antibioticmech:curator-f56d459cee` `sutezolid`, `antibioticmech:curator-daae3d88a3` `sanfetrinem`, `antibioticmech:curator-e14f58e6dc` `tomopenem`, `antibioticmech:curator-6bdee75cea` `albaconazole`, `antibioticmech:curator-217ed2935e` `quilseconazole`):
   - All 7 `PROPOSED`/`MINTED` records have curated `mode_of_action` and primary target citations in `mode_of_action_notes`/`provenance` but lack structured `PRIMARY_LITERATURE` `molecular_targets` and `UniProtKB` accounting.

### Deferred Findings Carried Forward with Explicit Dispositions (8 findings)

1. **`mcr43-context`** (`2` targets: `CHEBI:59064`, `CHEBI:59673`; `carried_from: mcr43-context`, Issue `#1140`) — `deferred`.
2. **`eatav-compound`** (`1` target: `CHEBI:8269`; `carried_from: eatav-compound`, Issue `#1141`) — `deferred`.
3. **`msrc-evidence`** (`2` targets: `CHEBI:42355`, `CHEBI:8732`; `carried_from: msrc-evidence`, Issue `#1143`) — `deferred`.
4. **`ddl-scope`** (`1` target: `CHEBI:28001`; `carried_from: ddl-scope`, Issue `#1144`) — `deferred`.
5. **`mexjk-role-conflict`** (`4` targets: `CHEBI:42355`, `CHEBI:27902`, `CHEBI:164200`, `antibioticmech:aro-1fe0873afd`; `carried_from: mexjk-role-conflict`, Issue `#1142`) — `deferred`.
6. **`reviewed-records-awaiting-causal-graphs`** (`34` targets: `33` `REVIEWED` records + `antibioticmech:aro-2eea3233f3` ofloxacin; `carried_from: reviewed-records-awaiting-causal-graphs`, Issue `#1257`) — `deferred`.
7. **`proposed-antibacterial-records-awaiting-grounding-and-mechanism`** (`66` targets; `carried_from: proposed-antibacterial-records-awaiting-grounding-and-mechanism`, Issue `#1258`) — `deferred`.
8. **`minted-aro-records-without-exact-chebi-structure`** (`240` targets; `carried_from: minted-aro-records-without-exact-chebi-structure`, Issue `#1259`) — `deferred`.
