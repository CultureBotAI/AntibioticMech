# AntibioticMech Cycle 8 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `8`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Source Revision**: `defe41100737cee8dc1e4722a2930e9752e6bee8`
- **Single-Record Review Bundle**: `reviews/structured/20261109T120000Z-andrimid-record-review/review.yaml` (`.claude/skills/review-yaml-record/SKILL.md`)
- **Full-Inventory Cohort Review Bundle**: `reviews/structured/20261109T120100Z-cycle8-frozen-inventory-cohort-review/review.yaml` (`.claude/skills/review-yaml-category/SKILL.md`)

## 1. Frozen Inventory & Validation Census

All **3,125** `AntibioticRecord` YAML files under `data/antibiotics/` at commit `defe41100737cee8dc1e4722a2930e9752e6bee8` were audited without modifying any scientific YAML records:

| Metric | Value |
| --- | ---: |
| Total `AntibioticRecord` files | 3,125 |
| `SEEDED` / `REVIEWED` / `PROPOSED` | 2,799 / 159 / 167 |
| `EXACT` / `MINTED` grounding | 2,782 / 343 (`240` `SEEDED` `antibioticmech:aro-*` + `103` `PROPOSED` `antibioticmech:curator-*`) |
| Records with `causal_graphs` | 97 (`96` `REVIEWED` + `1` `SEEDED`/`MINTED` ofloxacin; `98` graphs; `78/78` `GENE_OR_PROTEIN` nodes carry `137` reviewed `UniProtKB` `protein_examples` across `76` protein-node graphs + `22` non-protein graphs held) |
| Records with `PRIMARY_LITERATURE` `molecular_targets` | 202 (`159` `REVIEWED` + `43` `PROPOSED` total across `208` target entries: `99` targets carry `172` reviewed `UniProtKB` `protein_examples`, `109` non-protein/complex targets explicitly held in `curation/uniprot_protein_examples.yaml`, `0` unaccounted) |
| `scripts/validate_strict.py --quiet --workers 4` | `0` errors across `3,125` files |
| `scripts/verify_corpus.py --summary` | `0` errors across `3,125` files (`159/159` `REVIEWED` have `EXACT` grounding + `chemical_structure`) |

### Partition by Antimicrobial Class Directory (`boundary_decisions[0]`)

| Directory | Record Count |
| --- | ---: |
| `data/antibiotics/antibacterial/` | 1,196 |
| `data/antibiotics/antifungal/` | 617 |
| `data/antibiotics/antiviral/` | 473 |
| `data/antibiotics/unspecified/` | 472 |
| `data/antibiotics/antiprotozoal/` | 258 |
| `data/antibiotics/antimycobacterial/` | 78 |
| `data/antibiotics/biocide/` | 31 |
| **Total** | **3,125** |

### Partition by Curation-Readiness Cohort (`boundary_decisions[1]`)

| Cohort | Record Count |
| --- | ---: |
| `REVIEWED` records with primary-literature `causal_graphs` | 96 |
| `REVIEWED` records awaiting primary-literature `causal_graphs` | 63 |
| `PROPOSED` records with `PRIMARY_LITERATURE` `molecular_targets` and `mode_of_action` | 43 (`6` `EXACT` + `37` `MINTED`) |
| `PROPOSED` `EXACT` Cycle 8 Stage 1 natural products ready for primary mechanism/target curation | 4 (`4` `EXACT`) |
| `PROPOSED` records awaiting primary mechanism curation | 120 (`54` `EXACT` + `66` `MINTED`) |
| `SEEDED` baseline records | 2,799 (`2,559` `EXACT` + `240` `MINTED`) |
| **Total** | **3,125** |

## 2. Single-Record Deep Review (`20261109T120000Z-andrimid-record-review`)

- **Target**: `CHEBI:216634` (`data/antibiotics/antibacterial/andrimid.yaml`)
- **Verdict**: `needs_curation` (`NEEDS_CURATION`)
- **Verified Support**: Exact `C27H33N3O5` chemical structure (`BDHVWPFPGIGCPA-MDKDCDSJSA-N`, PubChem CID `54675763`), `CURATOR` discovery and mechanism evidence (`DOI:10.1074/jbc.m402989200`, `PMID:15166242`; `DOI:10.1021/ja063074c`, `PMID:16866529`), MIBiG `BGC0000956` producer `Pantoea agglomerans` (`NCBITaxon:549`), `biosynthesis_origin: NATURAL_PRODUCT`, `mode_of_action: FATTY_ACID_SYNTHESIS_INHIBITION` (`MICROBIAL_TARGET`), and `PRIMARY_LITERATURE` `molecular_targets[0]` for bacterial acetyl-CoA carboxylase carboxyltransferase (`GO:0003989`, `PROTEIN`, `DIRECT_BINDING_TARGET`) carrying reviewed Swiss-Prot `UniProtKB` `protein_examples` `P0ABD5` (`accA`) and `P0A9Q5` (`accD`) in *Escherichia coli* K-12 (`NCBITaxon:83333`).
- **Open Finding**: `andrimid-awaiting-reviewed-promotion` (`issue_key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`) — retains `curation_status: PROPOSED` despite meeting all `REVIEWED` gate criteria.

## 3. Stable Findings & Dispositions (`20261109T120100Z-cycle8-frozen-inventory-cohort-review`)

### Open Findings for Cycle 8 Stage 5 Grouped Remediation (3 findings, 15 records)

1. **`proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion`** (`major`, `open`, `6` targets: `CHEBI:81029` `alanylclavam`, `CHEBI:199652` `amicetin`, `CHEBI:216634` `andrimid`, `CHEBI:202006` `bottromycin A2`, `CHEBI:226796` `planosporicin`, `CHEBI:204968` `ajudazol A`):
   - Have `grounding_status: EXACT`, complete single-molecule `chemical_structure`, curated `biosynthesis_origin: NATURAL_PRODUCT`, curated `mode_of_action` (`AMINO_ACID_METABOLISM_DISRUPTION` on `alanylclavam`; `PROTEIN_SYNTHESIS_INHIBITION` on `amicetin` and `bottromycin A2`; `FATTY_ACID_SYNTHESIS_INHIBITION` on `andrimid`; `CELL_WALL_SYNTHESIS_INHIBITION` on `planosporicin`; `ELECTRON_TRANSPORT_INHIBITION` / `HOST_SHARED_TARGET` on `ajudazol A`), and `PRIMARY_LITERATURE` `molecular_targets` with complete `UniProtKB` `protein_examples` (`P0ABD5`/`P0A9Q5` on `andrimid`) or `held_targets` accounting, yet remain `curation_status: PROPOSED` (and `alanylclavam`, `amicetin`, `bottromycin A2`, and `ajudazol A` can additionally be enriched with canonical GO `target_id` terms `GO:0004413`, `GO:0015934`, and `GO:0005747`).
2. **`cycle8-stage1-proposed-exact-natural-products-missing-mechanism-and-targets`** (`major`, `open`, `4` targets: `CHEBI:217619` `TP-1161`, `CHEBI:81025` `2-formyloxymethylclavam`, `CHEBI:81026` `2-hydroxymethylclavam`, `CHEBI:81027` `clavam-2-carboxylate`):
   - All 4 `PROPOSED`/`EXACT` natural-product records seeded in Cycle 8 Stage 1 have complete `chemical_structure`, curated `biosynthesis_origin: NATURAL_PRODUCT`, and primary-literature discovery/biosynthetic citations (`Engelhardt et al. 2010 PMID:20562278` / `Morris et al. 2009 PMID:19665975` / `BGC0000615` for `TP-1161`; `Brown et al. 1979 DOI:10.1039/c39790000282` / `Pruess et al. 1983 PMID:6190822` / `Mosher et al. 1999 PMID:10223939` / `Jensen et al. 2000 PMID:10681345` / `BGC0000845` for `2-formyloxymethylclavam`, `2-hydroxymethylclavam`, and `clavam-2-carboxylate`), but lack `mode_of_action`, structured `PRIMARY_LITERATURE` `molecular_targets` (with `UniProtKB` accounting), and `REVIEWED` promotion.
3. **`seeded-exact-rifamycins-and-elfamycins-with-card-only-targets-awaiting-primary-literature-promotion`** (`major`, `open`, `5` targets: `CHEBI:45367` `rifabutin`, `CHEBI:75246` `rifaximin`, `CHEBI:45304` `rifapentine`, `CHEBI:29584` `GE2270A`, `CHEBI:29668` `pulvomycin`):
   - All 5 `SEEDED`/`EXACT` antibiotic records have complete ChEBI `chemical_structure` and `CARD_ARO` target assertions (`PRIMARY_EVIDENCE_NEEDED`: `ARO:3000737` rifamycin-sensitive beta-subunit of RNA polymerase `rpoB` on `rifabutin`, `rifaximin`, and `rifapentine`; `ARO:3000731` elongation factor Tu on `GE2270A` and `pulvomycin`) but lack curated `biosynthesis_origin` (`SEMISYNTHETIC` on `rifabutin`, `rifaximin`, `rifapentine`; `NATURAL_PRODUCT` on `GE2270A`, `pulvomycin`), curator-reviewed `mode_of_action` (`NUCLEIC_ACID_SYNTHESIS_INHIBITION` with `MICROBIAL_TARGET` on the three rifamycins; `PROTEIN_SYNTHESIS_INHIBITION` with `MICROBIAL_TARGET` on the two elfamycins) and `mode_of_action_notes`, structured `PRIMARY_LITERATURE` `molecular_targets` (`GO:0003899` DNA-directed 5'-3' RNA polymerase activity or `GO:0003746` translation elongation factor activity with reviewed `UniProtKB` `protein_examples`), and `REVIEWED` promotion.

### Deferred Findings Carried Forward with Explicit Dispositions (8 findings)

1. **`mcr43-context`** (`2` targets: `CHEBI:59064`, `CHEBI:59673`; `carried_from: mcr43-context`, Issue `#1140`) — `deferred`.
2. **`eatav-compound`** (`1` target: `CHEBI:8269`; `carried_from: eatav-compound`, Issue `#1141`) — `deferred`.
3. **`msrc-evidence`** (`2` targets: `CHEBI:42355`, `CHEBI:8732`; `carried_from: msrc-evidence`, Issue `#1143`) — `deferred`.
4. **`ddl-scope`** (`1` target: `CHEBI:28001`; `carried_from: ddl-scope`, Issue `#1144`) — `deferred`.
5. **`mexjk-role-conflict`** (`4` targets: `CHEBI:42355`, `CHEBI:27902`, `CHEBI:164200`, `antibioticmech:aro-1fe0873afd`; `carried_from: mexjk-role-conflict`, Issue `#1142`) — `deferred`.
6. **`reviewed-records-awaiting-causal-graphs`** (`64` targets: `63` `REVIEWED` records + `antibioticmech:aro-2eea3233f3` ofloxacin; `carried_from: reviewed-records-awaiting-causal-graphs`, Issue `#1257`) — `deferred`.
7. **`proposed-antibacterial-records-awaiting-grounding-and-mechanism`** (`120` targets; `carried_from: proposed-antibacterial-records-awaiting-grounding-and-mechanism`, Issue `#1258`) — `deferred`.
8. **`minted-aro-records-without-exact-chebi-structure`** (`240` targets; `carried_from: minted-aro-records-without-exact-chebi-structure`, Issue `#1259`) — `deferred`.
