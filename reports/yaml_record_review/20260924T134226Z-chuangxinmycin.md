# YAML Record Review: (−)-chuangxinmycin

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antibacterial/chuangxinmycin.yaml`
- Started UTC: 2026-09-24T13:42:26Z
- Finished UTC: 2026-09-24T13:42:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/antibacterial/chuangxinmycin.yaml` |
| Class | `ANTIBACTERIAL` |
| ID | `CHEBI:79391` |
| Label | `(−)-chuangxinmycin` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained status | Generated from `data/raw/` inventories |

`chuangxinmycin.yaml` is a generated exact ChEBI record for `CHEBI:79391`.
ChEBI contributes the individual neutral `(−)-chuangxinmycin` structure, the
antimicrobial-agent and antibacterial-agent roles `CHEBI:33281` and
`CHEBI:33282`, the `CHEBI:25384`, `CHEBI:38958`, and `CHEBI:79393`
parents, two registry xrefs, nine source literature leads, and no
curator-owned `mode_of_action`, target scope, record-level evidence, molecular
target, activity observation, resistance mechanism, producer organism, clinical
assertion, dataset, discussion, or causal graph.

## Validation

| Command | Result |
|---|---|
| `rg --no-ignore --hidden -n -e 'CHEBI:79391' -e '79391' -e 'chuangxinmycin' data/antibiotics data/raw curation reports/yaml_record_review .claude docs README.md conf src scripts tests /tmp/antibioticmech-review-queue.tsv /tmp/antibioticmech-worklist.tsv` | Passed with ignored and hidden files included; it found the generated `CHEBI:79391` YAML, `PATHS.tsv` lock row, exact ChEBI inventory row, current review-queue rows, and current worklist rows, but no prior exact `CHEBI:79391` review report. |
| `! rg --no-ignore --hidden -n -e 'CHEBI:79391' -e 'chuangxinmycin' data/raw/aro_antibiotics.tsv data/raw/aro_resistance_edges.tsv data/raw/aro_target_edges.tsv data/raw/bindingdb_target_measurements.tsv data/raw/fda_clinical_status.tsv data/raw/mibig_producers.tsv data/raw/phibase_amr.tsv curation/decisions.tsv` | Passed with ignored and hidden files included; no exact adopted ARO, BindingDB, Drugs@FDA, MIBiG, PHI-base, or grounding-decision row exists for `CHEBI:79391` or exact `(−)-chuangxinmycin`. |
| `! rg --no-ignore --hidden -n -e 'CHEBI:79392' curation conf src scripts tests data/raw/chebi_antimicrobials.tsv data/antibiotics/antibacterial/chuangxinmycin.yaml` | Passed with ignored and hidden files included; the current repository has no ChEBI tryptophanyl-tRNA ligase inhibitor role mapping, no extracted `CHEBI:79392` mechanism role, and no generated chuangxinmycin `mode_of_action`. |
| `just validate data/antibiotics/antibacterial/chuangxinmycin.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/chuangxinmycin.yaml --out /tmp/chuangxinmycin-validate-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Passed with the known unrelated CARD iclaprim/CHEBI:31724 xref refusal; all 2,939 expected records were on disk, with no missing records, no unexpected records, no drifted fields, and no `PATHS.tsv` issues. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` | Passed; exact `CHEBI:79391` appears in the `mechanism` queue and the derived `review-readiness` queue. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed; exact `CHEBI:79391` is row 146 with `MECHANISM_REVIEW`, 9 committed source-literature leads, 0 record evidence items, and 0 targets. |
| Live OLS4 lookup for `CHEBI:79391` | Passed; OLS resolved one non-obsolete ChEBI class with `obo_id` `CHEBI:79391`, label `(-)-chuangxinmycin`, the generated formula, SMILES, Standard InChI, Standard InChIKey, CAS and Reaxys xrefs, and all nine PubMed xrefs. |
| Live ChEBI page lookup for `CHEBI:79391` | Passed; current ChEBI agreed with the generated Unicode label, ASCII label, definition, formula, charge, average mass, monoisotopic mass, SMILES, InChI, InChIKey, CAS xref, Reaxys xref, three `is_a` parents, and nine PubMed citations. ChEBI also asserts the `CHEBI:79392` tryptophanyl-tRNA ligase inhibitor role, which is not present in the committed extracted row. |
| OLS4 `parents` and `has_role` lookups for `CHEBI:79391` | Passed; OLS confirmed exactly three direct parents and four `has_role` values: antibacterial agent `CHEBI:33282`, antimicrobial agent `CHEBI:33281`, bacterial metabolite `CHEBI:76969`, and EC 6.1.1.2 tryptophan--tRNA ligase inhibitor `CHEBI:79392`. |
| PubMed esummary/efetch for ChEBI's nine cited PMIDs | Passed; all nine PMIDs resolved. `PMID:327539` is the 1977 discovery and antibacterial-activity lead, `PMID:12372526` is the direct bacterial tryptophanyl-tRNA synthetase inhibition lead, `PMID:2800539`, `PMID:6226412`, and `PMID:6242357` are biosynthesis leads, `PMID:11558613`, `PMID:3445758`, and `PMID:3677223` are synthesis/stereochemistry leads, and `PMID:22500807` is a C. elegans toxin-response lead. |

No separate single-record term, reference, or history validator is documented in
the local `justfile`. The full `just qc` gate is left for the PR-level check
because this review made no generated YAML mutation.

## Identity and Grounding

| Claim | Assessment |
|---|---|
| Identifier and label | Supported. `PATHS.tsv`, the generated YAML, the committed ChEBI row, OLS, and current ChEBI all resolve `CHEBI:79391` to exact `(−)-chuangxinmycin` / `(-)-chuangxinmycin`. |
| Structure | Supported. The generated SMILES, Standard InChI, Standard InChIKey `DKHFLDXCKWDVMF-UPONEAKYSA-N`, formula `C12H11NO2S`, charge `0`, average mass, and monoisotopic mass match `data/raw/chebi_antimicrobials.tsv`, OLS, and current ChEBI for exact `CHEBI:79391`. |
| Stereochemistry | Supported. The record denotes the `(2R,3S)` diastereoisomer, using the same chiral SMILES and Standard InChI stereochemical layer as the ChEBI source. |
| Parent compounds | Supported. Current ChEBI and OLS both keep exact `(−)-chuangxinmycin` under `CHEBI:25384` monocarboxylic acid, `CHEBI:38958` indole alkaloid, and `CHEBI:79393` thiinoindole, matching the generated `parent_compounds`. |
| Xrefs | Supported as exact same-structure rows by ChEBI for the bounded review. OLS and current ChEBI still list CAS `63339-68-4` and Reaxys `7796054`. |
| Source concept | Supported. The only exact source concept is ChEBI `CHEBI:79391` at version `2026-08-30`, with minted key `antibioticmech:chebi-a9f211116d`; exact ignored/hidden-inclusive searches found no adopted external inventory or local curator decision that changes this record's identity. |

## Evidence

| Claim | Assessment |
|---|---|
| Exact `CHEBI:79391` denotes neutral `(−)-chuangxinmycin`. | Supported by the committed ChEBI inventory row, OLS, and current ChEBI. |
| Exact `(−)-chuangxinmycin` has roles `CHEBI:33281` and `CHEBI:33282`. | Supported as ChEBI database assertions. The record correctly retains both activity roles and files the record under `ANTIBACTERIAL` from the antibacterial-agent role. |
| Exact `(−)-chuangxinmycin` is an inhibitor of bacterial tryptophanyl-tRNA synthetase. | Supported by `PMID:12372526`, whose PubMed abstract reports chuangxinmycin as a potent and selective inhibitor of bacterial tryptophanyl-tRNA synthetase, and by current ChEBI's `CHEBI:79392` role. The current repo does not map `CHEBI:79392`, so the extracted ChEBI row has an empty `mechanism_role_ids` value. |
| Exact `(−)-chuangxinmycin` is active against bacteria. | Supported at source-provenance level by the original discovery abstract in `PMID:327539`, which reports isolation from `Actinoplanes tsinanensis`, in vitro activity against Gram-negative and Gram-positive bacteria, and in vivo activity in mice against `Escherichia coli` and `Shigella dysenteriae` infections. The abstract does not expose exact MIC rows for the YAML's `activity_spectrum` model. |
| ChEBI's remaining source PMIDs are useful chemical, biosynthetic, and host-response leads. | `PMID:11558613`, `PMID:3445758`, and `PMID:3677223` concern chemical synthesis of chuangxinmycin or derivatives; `PMID:2800539`, `PMID:6226412`, and `PMID:6242357` concern producer-strain biosynthesis; `PMID:22500807` uses chuangxinmycin in a C. elegans study of xenobiotic defenses. These are not direct claim-level evidence for MIC, molecular target, or antibacterial causal-edge entries. |

The record makes no molecular-target, activity-observation,
resistance-mechanism, producer, clinical, dataset, or causal-edge claims, so
there are no unsupported claim-level citations in the YAML.

## Completeness

| Area | Assessment |
|---|---|
| Identity and structure | Complete enough for read-only review. Exact `CHEBI:79391`, the generated record, OLS, current ChEBI, `data/raw/chebi_antimicrobials.tsv`, and `PATHS.tsv` agree. |
| Filing class and activity roles | Complete enough for source-seeded filing. The `ANTIBACTERIAL` directory and `CHEBI:33281` plus `CHEBI:33282` activity roles faithfully reproduce the antimicrobial activity assertions imported from ChEBI. |
| Mode of action | Incomplete. Current ChEBI asserts exact chuangxinmycin has role `CHEBI:79392`, an EC 6.1.1.2 tryptophan--tRNA ligase inhibitor, and `PMID:12372526` directly supports a bacterial tryptophanyl-tRNA synthetase mechanism. The repo has not mapped that role into `role_to_mode_of_action`, so the generated record has no source-seeded or curator-reviewed mode. |
| Molecular targets and causal graphs | Incomplete. The source PMIDs include a direct bacterial tryptophanyl-tRNA synthetase mechanism lead, but the generated record has no `molecular_targets` and no `causal_graphs`. A future curation pass should inspect full text before selecting a target organism and building a directed mechanism graph. |
| Activity observations | Incomplete. The original discovery abstract supports antibacterial activity but not an exact MIC, MBC, IC50, or comparable activity measurement that should be copied into `activity_spectrum` without full-text curation. |
| Resistance mechanisms | Complete as empty for the adopted sources. Exact ignored/hidden-inclusive searches found no CARD or PHI-base row for `CHEBI:79391`. |
| Producers and clinical status | Complete as empty for the adopted sources, but not biologically complete. Current ChEBI lists `Actinoplanes tsinanensis` as a compound origin from `PMID:327539`, but exact ignored/hidden-inclusive searches found no adopted MIBiG producer row or Drugs@FDA status row for `(−)-chuangxinmycin`. |
| Datasets and discussions | Complete as empty for the bounded review. The inspected sources did not expose a public exact `(−)-chuangxinmycin` dataset accession or a concrete unresolved identity conflict that needs a `Discussion` before mechanism curation. |

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record cannot satisfy the `REVIEWED` gate because it has no curator-owned antimicrobial mode of action. | `data/antibiotics/antibacterial/chuangxinmycin.yaml` has no `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, or `causal_graphs`; `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` keeps exact `CHEBI:79391` on the `mechanism` queue. | Future curator-owned mechanism, target, discussion, and causal-graph additions on `data/antibiotics/antibacterial/chuangxinmycin.yaml`, written with `record_curation_event` and `write_validated_antibiotic`. |
| Major | ChEBI already has an exact tryptophanyl-tRNA ligase inhibitor role, but the extractor ignores it. | Current OLS and ChEBI both assert `CHEBI:79391` `has role` `CHEBI:79392`, EC 6.1.1.2 tryptophan--tRNA ligase inhibitor. `data/raw/chebi_antimicrobials.tsv` has a blank `mechanism_role_ids` field for `CHEBI:79391`, and ignored/hidden-inclusive `rg` found no `CHEBI:79392` mapping under `conf/`, `src/`, `scripts/`, `tests/`, `curation/`, or the exact chuangxinmycin YAML. | `conf/sources.yaml` role mapping, source-inventory extraction, and future reseeded `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/antibacterial/chuangxinmycin.yaml`. |
| Minor | Exact producer evidence exists outside the adopted MIBiG source path. | Current ChEBI lists `Actinoplanes tsinanensis` as a compound origin from `PMID:327539`, and the discovery abstract reports production by the same species, but `producer_organisms` is empty and exact ignored/hidden-inclusive searches found no MIBiG row for chuangxinmycin. | Future curator-owned producer additions on `data/antibiotics/antibacterial/chuangxinmycin.yaml`, written with `record_curation_event` and `write_validated_antibiotic`. |

No blocker findings.

## Recommended Edits

1. Map `CHEBI:79392` in `conf/sources.yaml` so exact ChEBI
   tryptophanyl-tRNA synthetase inhibitor assertions seed
   `PROTEIN_SYNTHESIS_INHIBITION`.

   The corresponding `role_target_scope` should be `HOST_SHARED_TARGET`,
   because EC 6.1.1.2 names tryptophan--tRNA ligase generically rather than a
   bacteria-only enzyme.

   Maintained owner: ChEBI mechanism role integration in `conf/sources.yaml`,
   `scripts/extract_source_inventory.py`, generated
   `data/raw/chebi_antimicrobials.tsv`, and reseeded generated YAML.

2. Add curator-owned molecular-target and causal-graph entries for the bacterial
   tryptophanyl-tRNA synthetase mechanism only after checking full text from
   `PMID:12372526` or another exact primary source.

   Maintained owner: future curator-owned fields on
   `data/antibiotics/antibacterial/chuangxinmycin.yaml`.

3. Add `Actinoplanes tsinanensis` as a producer organism only after checking
   full text from `PMID:327539` or another exact primary source.

   Maintained owner: future curator-owned fields on
   `data/antibiotics/antibacterial/chuangxinmycin.yaml`.

## Follow-up Checks

- Rerun `just validate data/antibiotics/antibacterial/chuangxinmycin.yaml`.
- Rerun `just validate-strict data/antibiotics/antibacterial/chuangxinmycin.yaml --out /tmp/chuangxinmycin-validate-strict.tsv`.
- Rerun `just verify-corpus`.
- Rerun `just worklist --limit 0 --tsv /tmp/chuangxinmycin-worklist.tsv` and
  confirm exact `CHEBI:79391` leaves `mechanism` only after a
  curator-reviewed mechanism is present.
- Rerun `just review-queue --limit 0 --tsv /tmp/chuangxinmycin-review-queue.tsv`
  and confirm exact `CHEBI:79391` advances past `MECHANISM_REVIEW` only after a
  supported mechanism is present.
- Repeat an ignored/hidden-inclusive exact search for `CHEBI:79391`,
  `antibioticmech:chebi-a9f211116d`, `DKHFLDXCKWDVMF-UPONEAKYSA-N`,
  `63339-68-4`, `CHEBI:79392`, and any PMID/DOI cited in future claim-level
  evidence.
- Manually recheck current ChEBI for `CHEBI:79391`, `CHEBI:79392`, and
  `NCBITaxon:2039464` so future curation preserves the exact compound,
  role, and producer boundaries.

## Additional Notes

- Searches used to establish local absence included ignored files.
- Current ChEBI's bacterial-metabolite role `CHEBI:76969` is a useful producer
  clue, not an `activity_roles` or `mode_of_action` value.
- This report is read-only review output. No generated record, upstream
  inventory, decision row, page, queue, or curation-history entry was edited.
