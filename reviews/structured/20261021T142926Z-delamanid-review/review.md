# Review of delamanid

- Review: 20261021T142926Z-delamanid-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:11:36Z
- Finished UTC: 2026-10-21T14:29:26Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact R delamanid parent is supported by independent authority structures and the original OPC-67683 paper. Its mycolic-acid/combination-treatment description is supported within appropriate source and regimen boundaries. All 250 CRyPTIC observations and the 47,650-member collection reproduce from maintained inputs. The sole confirmed correction is to type Deltyba as a brand rather than an exact chemical synonym. The five CARD resistance assertions remain database-qualified; their target-alteration category must not be mistaken for direct inhibition of the activation proteins.

## Scope And Provenance

Entire SEEDED, EXACT record: definition, sole alias, parent/class, complete chemical structure and four xrefs, source concept, all five resistance entries, all 250 grouped activities, complete membership reference and five history events. All eleven adopted ARO/ChEBI PMID leads checked separately.

Selection: Queue 352 in isolated batch 036; thirteen original hashes preserved and twelve actual-owner hashes appended before detailed assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:134742 | data/antibiotics/antibacterial/delamanid.yaml | generated | delamanid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | CHEBI:134742 | Exit 0. |
| Documented strict validation | passed | True | CHEBI:134742 | Exit 0; no ERROR rows. |
| Native molecular consistency | passed | False | CHEBI:134742 | Native SMILES/InChI, key, formula, charge and masses agree. |
| Independent exact stereochemical mapping | passed | False | CHEBI:134742 | Eight native/current authority representations agree by reciprocal chirality-aware atom mappings; sole configured center is R. |
| Initial structured dataset discovery | failed | False | CHEBI:134742 | Actual child command exit 2 from sandbox DNS failure. Five subsequent gene searches in the same initial ledger also exited 2; no absence inference. |
| Structured network retry | passed | False | CHEBI:134742 | Dataset discovery and all five exact-gene searches exit 0 on network-enabled retry; catalog matches remain context only. |
| Exact CRyPTIC collection reconstruction | passed | False | CHEBI:134742 | All 250 groups reconstruct the exact compressed payload and complete reference; native membership validation passes. |
| Whole source/activity/history audit | passed | False | CHEBI:134742 | Twenty-five unchanged hashes, five resistance edges, all 250 activity fields, eleven adopted identifiers and five history events reconcile. |
| Authoritative full QC | failed | True | CHEBI:134742 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:134742 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:134742 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:134742 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:134742 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:134742 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:134742 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:134742 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:134742 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact R delamanid parent

identity: supported. Targets: CHEBI:134742.

Independent atom mappings, original compound assignment and source projections agree.

### Product alias typing

representation: concern. Targets: CHEBI:134742.

Deltyba is a medicinal-product brand; native EXACT_SYNONYM loses that distinction.

### Mycolic-acid and combination-treatment description

evidence: supported. Targets: CHEBI:134742.

Pathway inhibition and bounded combination-treatment context are supported; neither a specific terminal protein target nor universal regimen superiority follows.

### Five database resistance claims

evidence: supported. Targets: CHEBI:134742.

All five claims match current CARD and remain explicitly database-cited. Activation/cofactor biology must be kept separate from literal direct-target inhibition.

### Activation pathway versus terminal binding target

completeness: unknown. Targets: CHEBI:134742.

The record has no direct-binding edge. Exact terminal target identity and variant-level causal sufficiency are not established by inherited CARD categories or catalog membership.

### All 250 grouped activity observations and sidecar

evidence: supported. Targets: CHEBI:134742.

Every field reproduces and quantitative/categorical projections independently reconcile; exact collection bytes and reference validate. Source ECOFF classifications, methods, quality and missingness remain bounded.

### All adopted leads, history and maintained ownership

provenance: supported. Targets: CHEBI:134742.

Eleven adopted identifiers have explicit dispositions; 25 hashes and five events remain unchanged. External source-access limitations are not called biological negatives.

## Findings

### F1: Deltyba is typed as an exact chemical synonym

minor / open / confirmed; issue key: delamanid-deltyba-brand-typed-exact-synonym.

The sole native alias deltyba is EXACT_SYNONYM. Official EMA product information identifies Deltyba tablets containing delamanid, so the supported representation is BRAND_NAME. The current blanket ARO alias typing reproduces the error.

## Recommended Actions And Acceptance Checks

### A1

During separately authorized curation, retain deltyba but emit BRAND_NAME through a reproducible narrow maintained alias-type correction. The current ARO seeder supplies only blanket EXACT_SYNONYM, so add and validate an explicit source/alias-specific type override or typed extraction support rather than claiming an existing override key. Regenerate and verify the resulting native synonym.

- The exact Deltyba alias is BRAND_NAME and the neutral R structure remains unchanged.
- Re-extraction/reseeding preserves the typed correction and does not change unrelated ARO aliases.
- All 250 grouped activities, membership payload and resistance provenance remain intact; run required native/corpus checks after curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/delamanid.yaml; Entire native YAML; 352-native-nonactivity.yaml and all activity fields reconciled in 352-source-audit.json | supports | The record retains delamanid exact parent identity, database-qualified resistance and source-labelled grouped phenotypes. Its only alias is deltyba with EXACT_SYNONYM typing; no native direct-binding target, clinical-status object or causal graph is asserted. |
| chemistry | CHEBI:134742; CAS:681492-22-8; PubChem CID6480466; ChEMBL CHEMBL218650; 352-chebi.json/.mol;352-pubchem.json;352-chembl.json;352-authority-chemistry.json | supports | Official authorities agree on neutral C25H25F3N4O6 and XDAOLTSRNUSPPH-XMMPIXPASA-N. Eight encodings share reciprocal chirality-aware mappings, zero charge and compatible masses, with one configured R center. ChEBI/CARD corroborate the exact CAS. Original 2006 Figure1 names the R compound; no racemate or product-excipient structure is inferred. |
| card | ARO:3004490; ARO:3004115; 352-card.html;352-card-class.html;352-raw-rows.json | supports | Current CARD and frozen inventory agree on the nitroimidazole class, parent, definition, deltyba alias and adopted definition review. ChEBI grants the exact structure while the ARO source supplies class/definition; the two-star ChEBI row has no independent adopted antimicrobial role. |
| brand | EMA Deltyba Summary of Product Characteristics; 352-ema-product.pdf sections1–2 and4.1, printed p2;352-ema.html product details | refutes | The official document names Deltyba 50 mg film-coated tablets and specifies delamanid as their active substance. Thus Deltyba is a product brand and should use BRAND_NAME. The combination-regimen indication supports bounded use context; it does not turn the tablet/excipients into the chemical parent or establish efficacy of every regimen. |
| leads | Eleven adopted ARO/ChEBI MED identifiers; 352-adopted-core.json;352-adopted-abstracts.txt;352-lead-dispositions.json | context_only | All eleven exact MED records resolve. Ten complete abstracts were read; the 2009 review has no indexed abstract. Original OPC-67683 work, historical reviews, PA-824 analogues, polar nitroimidazooxazoles, leishmaniasis candidates and unrelated nitroheterocyclic classes receive separate dispositions. Their analogue results are not silently transferred to delamanid. |
| definition-review | PMID:25210407; DOI:10.4103/0976-500x.136121; 352-definition-review.xml, complete main text | supports | The adopted 2014 review explicitly describes delamanid as a prodrug activated by Rv3547 and links it to methoxy/keto-mycolic acid suppression and combination treatment. Its optimistic historical safety/no-interaction language and conditional-approval date are not adopted as modern clinical claims. |
| original | PMID:17132069; DOI:10.1371/journal.pmed.0030466; 352-original.xml: Figure1 identity; material/MIC/mycolic-acid/metabolism/intracellular and mouse-combination methods/results; discussion | supports | Otsuka synthesized R-OPC-67683. Agar-growth assays support antimycobacterial activity; BCG lipid labelling shows methoxy/keto-mycolic-acid suppression, a pathway endpoint rather than direct binding. Susceptible BCG metabolized the drug, whereas a resistant strain did not; the Rv3547 mutation observation is described as unpublished data. Intracellular and mouse-regimen effects remain preclinical. Neither the desnitro end product nor every combination is declared the active antibacterial agent. |
| resistance | ARO:3007661; ARO:3007849; ARO:3009339; ARO:3009340; ARO:3009341; 352-card-ddn.html;352-card-fgd1.html;352-card-fbiA.html;352-card-fbiB.html;352-card-fbiC.html;352-card-leads-core.json | supports | All five exact CARD nodes assert delamanid resistance and currently classify it as antibiotic target alteration. The native evidence honestly labels this database provenance. Current sources describe Ddn activation and F420 cofactor biology, not direct drug inhibition of each protein. PMID36409105 concerns ddn Trp20Stop in a specific clinical lineage; PMID32361756 is a systematic mutation review; the Fbi entries cite the WHO 2023 mutation catalogue. These do not establish that every mutation in each gene confers resistance. |
| adapter | iModulonDB m_tuberculosis/modulome; 352-adapter-results.json and 352-adapter-retry-results.json | context_only | Initial dataset/gene calls failed with DNS errors. The network retry maps ddn to Rv3547, fgd1 to Rv0407, fbiA to Rv3261, fbiB to Rv3262 and fbiC to Rv1173, with no iModulon hits. Catalog membership supports gene context only; it is neither binding evidence nor proof of a resistance variant. |
| cryptic | CRyPTIC3.4.0; DOI:10.5281/zenodo.15680920; 352-cryptic-table.txt;352-source-audit.json;352-membership-audit.json; exact native membership sidecar | supports | All 250 groups reproduce exactly: 79 DST and 171 UKMYC groups, 210 quantitative rows with 155 uncensored, 31 &lt;= and 24 &gt; qualifiers. Source calls comprise 136 susceptible, 74 resistant,one intermediate and 39 unspecified groups. The exact sidecar reconstructs 47,650 memberships across 25,038 subjects, including 7,059 unlinked subjects. Counts do not imply unique patients, independent experiments or prevalence. Assay, quality, censoring and missing outcomes remain explicit. |
| cryptic-primary | PMID:35944069; DOI:10.1371/journal.pbio.3001721; 352-cryptic-primary.xml, sample collection, Plate assay and Binary phenotype classification methods | context_only | The original compendium describes resistance-enriched collection, Otsuka-supplied DLM in UKMYC microdilution plates and ECOFF-derived binary phenotypes. This supports assay/interpretation context without identifying all current release 3.4.0 rows with the older study cohort or treating source resistance calls as independently reassessed clinical breakpoints. |
| owners | Maintained ChEBI/CARD/CRyPTIC inputs and seeding; 352-inspect.json;352-owner-append.json;352-source-audit.json;conf/sources.yaml aro_mechanism_map; seeder ARO synonym projection | supports | All 25 captured input hashes and five ordered histories reconcile. The seeder currently assigns every ARO alias EXACT_SYNONYM, explaining the brand defect. Its resistance type follows CARD ancestry through the maintained mechanism map; generated fields require maintained source/owner changes rather than a YAML-only patch. |
| validation | Actual focused checks; 352-focused-results.json;352-focused-run.log;352-strict.tsv;352-chemistry-authorities.log;352-ledger.log;352-membership-check.log | supports | Native chemistry, independent authority mapping, schema, strict, source ledger and exact membership reconstruction all exit 0. Initial adapter failures and successful retry are separately preserved. |
| search | Exact identifier, adopted publication and source-release searches; 352-local-hits.txt includes ignored files;352-fetch manifests; exact CARD/EMA/PMC retrievals on 2026-10-21 | context_only | Zenodo metadata and landing page returned 403, so release contents were checked through adopted source inventories and exact membership reconstruction. The2009 review and 2015 analogue full texts returned XML 500/browser challenges; the current ddn clinical paper and mutation review returned XML 500. Abstract or bibliographic scope is explicitly retained. |

## Limits And Additional Notes

- All eleven adopted PMID records were checked; ten abstracts were available. PMID19075046 lacked an abstract and attempted full text failed. Other analogue papers were assessed at abstract level except the inspected original 2006 study; their data are not transferred to delamanid.
- The original 2006 relevant methods/results and discussion were inspected, not all raw spectra, supplementary animal data or every plotted point. Its Rv3547 mutation statement explicitly refers to unpublished data and is not treated as a fully reported allelic-exchange experiment.
- Current CARD resistance classification is preserved as database provenance. It does not demonstrate direct drug binding to Ddn/Fgd1/Fbi proteins, that all variants are causal, or a shared resistance genotype for grouped activity observations. The current ddn paper was available at abstract level only.
- CRyPTIC 3.4.0 remote Zenodo access returned 403. Every maintained group and collection byte was checked, but source raw susceptibility experiments and original archived release files were not independently remeasured or downloaded.
- CRyPTIC groups include missing MICs, uncategorized calls, lower-quality observations and repeated subjects across methods/tables. No population resistance percentage, unique-patient total or universal clinical-breakpoint interpretation is inferred.
- Historical review clinical optimism is not a contemporary superiority/safety assertion. The EMA label supports product identity and bounded combination use, not efficacy of every regimen.
- Focused native checks passed; shared corpus gates remain separate. No scientific-status promotion or native change is part of this review.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Optional future primary-evidence enrichment should describe prodrug activation separately from the downstream mycolic-acid phenotype and avoid equating the inactive desnitro end product with the active intermediate.
- Current CARD classification semantics warrant careful qualification; the record already labels the five edges as database assertions, so this review does not delete supported resistance relationships solely because the imported mechanism category is broad.
- Native records, maintained inputs and history remain unchanged. Native checks used batch 036 and standalone chemistry the recorded batch 019 interpreter.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T142926Z-delamanid-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of delamanid
started_at: '2026-10-21T14:11:36Z'
finished_at: '2026-10-21T14:29:26Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Independent whole-record source reconciliation, chirality-aware
    chemical comparisons, original discovery methods/results, current EMA material/indication
    evidence, exact CARD assertions, all adopted publication leads, and complete CRyPTIC
    projection/membership reconstruction.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Minor brand-name typing correction; exact R parent, database resistance
  provenance and grouped activity projections otherwise reconcile
scientific_review: true
summary: The exact R delamanid parent is supported by independent authority structures
  and the original OPC-67683 paper. Its mycolic-acid/combination-treatment description
  is supported within appropriate source and regimen boundaries. All 250 CRyPTIC observations
  and the 47,650-member collection reproduce from maintained inputs. The sole confirmed
  correction is to type Deltyba as a brand rather than an exact chemical synonym.
  The five CARD resistance assertions remain database-qualified; their target-alteration
  category must not be mistaken for direct inhibition of the activation proteins.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: conf/sources.yaml
    sha256: 4a2dcd7a3a88953b6cb35b51a48ed77b626c3af2cbb542b0d38ba10540ed7df9
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: 224cbb7261add427184b2762a29c2ff3e85c85e0a06cf22b144545346487247b
    role: context
  - path: curation/decisions.tsv
    sha256: a5834b44307b0449b0df9362c551b7fcd707f3ae51f73d429d37d51f5a169d61
    role: context
  - path: data/antibiotics/antibacterial/delamanid.yaml
    sha256: c532d157179c1393d757f63226613e07175dc26683f798c1f6a44b827257e780
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/chebi_antimicrobials.tsv
    sha256: 4c33e56c3c342be657309f720f5b5cb9cad1fae13bec202ef99e449503c32004
    role: context
  - path: data/raw/chebi_role_names.tsv
    sha256: 5c476c0aacd7c98d7241d2343a6fc41ee9eb9338077404c5b011a04bf40c6ac5
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/extract_source_inventory.py
    sha256: bb1606fd07cd8187640b5200a21ec090bb06683397d691e87ddd6884ea768860
    role: context
  - path: scripts/seed_from_sources.py
    sha256: be66eca74d22a3daa9ac6ff73d437c6c56e8d85b97f6877fdf3de77e2ab64680
    role: context
  - path: src/antibioticmech/schema/antibioticmech.yaml
    sha256: de62be2dd2dd55f141a0c14ff666eaa00efc6f3b431d651d0196ebcfddfbb301
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/cryptic_activity.tsv
    sha256: fa2fe5e5258328f10f9fe5724e4b74f354a98f5355bac68108ab28ffb17c7987
    role: context
  - path: curation/cryptic_drug_map.tsv
    sha256: 69643f9b5e6dfc91761a4541317de63c5dca565131f6a07a3193878d7f863a54
    role: context
  - path: data/raw/cryptic_memberships.tsv.gz
    sha256: f121fc3ac48a44a89931366d908877d833bd846d9690257583c5dbbdb8bd2601
    role: context
  - path: data/raw/cryptic_isolates.tsv.gz
    sha256: 7d51bf3032e295a56e2543f52f12e59d6a8589ad6f2208e2314a154e6e8cf2c5
    role: context
  - path: scripts/extract_cryptic_memberships.py
    sha256: d944260859c29ff3af55137c311e14be45b6c3219b5283c4cbd1b794d49fe952
    role: context
  - path: scripts/cryptic_membership_inventory.py
    sha256: b0d8ae24cac64dfb2813bfa5a5ef590e3330e3c5ace82e25f3528b025147d6cc
    role: context
  - path: src/antibioticmech/activity_memberships.py
    sha256: 22849043b741d7a48a708dfade09524a11ac46afa7efb08d350ec7422ec2e146
    role: context
  - path: data/antibiotics/antibacterial/membership-29e0cdcf46f7d35b980a75dc4050bf07074066420039bd506863dea353970d97.json.gz
    sha256: 29e0cdcf46f7d35b980a75dc4050bf07074066420039bd506863dea353970d97
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
scope:
  description: 'Entire SEEDED, EXACT record: definition, sole alias, parent/class,
    complete chemical structure and four xrefs, source concept, all five resistance
    entries, all 250 grouped activities, complete membership reference and five history
    events. All eleven adopted ARO/ChEBI PMID leads checked separately.'
  selection: Queue 352 in isolated batch 036; thirteen original hashes preserved and
    twelve actual-owner hashes appended before detailed assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:134742
targets:
- target_id: CHEBI:134742
  path: data/antibiotics/antibacterial/delamanid.yaml
  label: delamanid
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI and CARD/ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted CARD identity, definition, class and alias
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Five adopted CARD resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_activity.tsv
    role: Adopted250 CRyPTIC grouped observations
  - repository: CultureBotAI/AntibioticMech
    path: curation/cryptic_drug_map.tsv
    role: Exact delamanid drug mapping
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_memberships.tsv.gz
    role: Adopted CRyPTIC observation membership
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_isolates.tsv.gz
    role: Adopted CRyPTIC subject metadata
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_cryptic_memberships.py
    role: CRyPTIC membership extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/cryptic_membership_inventory.py
    role: Membership loading and validation
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/activity_memberships.py
    role: Native membership collections
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/membership-29e0cdcf46f7d35b980a75dc4050bf07074066420039bd506863dea353970d97.json.gz
    role: Exact delamanid membership sidecar
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: CARD evidence qualification context
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: CARD evidence qualification extraction
checks:
- check_id: schema
  name: Documented schema validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/delamanid.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/delamanid.yaml --out /private/tmp/am-review-session/352-strict.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Native molecular consistency
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    352
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Native SMILES/InChI, key, formula, charge and masses agree.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - chemistry
  - validation
- check_id: authority-chemistry
  name: Independent exact stereochemical mapping
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/352-chemistry-authorities.py
    > /private/tmp/am-review-session/352-chemistry-authorities.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Eight native/current authority representations agree by reciprocal chirality-aware
    atom mappings; sole configured center is R.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - chemistry
- check_id: adapter-initial
  name: Initial structured dataset discovery
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  status: failed
  required: false
  exit_code: 2
  expected_exit_code: 0
  summary: Actual child command exit 2 from sandbox DNS failure. Five subsequent gene
    searches in the same initial ledger also exited 2; no absence inference.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - adapter
- check_id: adapter-retry
  name: Structured network retry
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/352-adapter-retry.py
    > /private/tmp/am-review-session/352-adapter-retry.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Dataset discovery and all five exact-gene searches exit 0 on network-enabled
    retry; catalog matches remain context only.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - adapter
- check_id: membership
  name: Exact CRyPTIC collection reconstruction
  command: .venv/bin/python /private/tmp/am-review-session/352-membership-check.py
    > /private/tmp/am-review-session/352-membership-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 250 groups reconstruct the exact compressed payload and complete reference;
    native membership validation passes.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - cryptic
- check_id: ledger
  name: Whole source/activity/history audit
  command: .venv/bin/python /private/tmp/am-review-session/352-ledger.py > /private/tmp/am-review-session/352-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Twenty-five unchanged hashes, five resistance edges, all 250 activity fields,
    eleven adopted identifiers and five history events reconcile.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - owners
  - cryptic
  - leads
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:134742
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just qc
  exit_code: 2
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-verify-corpus
  name: Generated corpus reproduction
  status: passed
  required: true
  summary: 2939 expected and present; zero missing, unexpected, drifted fields or
    lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic
    retained.
  target_ids:
  - CHEBI:134742
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just verify-corpus
    --summary
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-review-queue
  name: Native review-readiness inventory
  status: passed
  required: false
  summary: 2859 native unsigned readiness rows written; this status queue does not
    determine structured-review coverage.
  target_ids:
  - CHEBI:134742
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just review-queue
    --limit 0 --tsv /private/tmp/am-review-session/native-queue.tsv
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-tests-platform-partial
  name: Supplementary test suite with two unavailable modules excluded
  status: passed
  required: false
  summary: 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy
    native library were explicitly excluded; this does not replace full QC.
  target_ids:
  - CHEBI:134742
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q -ra --ignore=tests/test_chemical_embedding.py --ignore=tests/test_chemical_map_site.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-validate-all
  name: Full closed-schema validation
  status: passed
  required: true
  summary: 2939 files, zero ERROR rows.
  target_ids:
  - CHEBI:134742
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-all
    --quiet --workers 2 --out /private/tmp/am-review-session/corpus-validation.tsv
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-chemical-map-check
  name: Chemical map consistency
  status: failed
  required: false
  summary: Exited 1 on the same pinned SciPy native library import failure.
  target_ids:
  - CHEBI:134742
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just chemical-map-check
  exit_code: 1
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-render-check
  name: Generated site consistency
  status: passed
  required: false
  summary: 2939 compound pages and seven class pages current.
  target_ids:
  - CHEBI:134742
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just render-check
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-report
  name: Corpus statistics
  status: passed
  required: false
  summary: Corpus report completed successfully.
  target_ids:
  - CHEBI:134742
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just report
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-corpus-integrity
  name: Full-corpus history/evidence/reference invariants
  status: passed
  required: true
  summary: 23 full-corpus integrity tests passed, including seed history, evidence
    placement and internal references.
  target_ids:
  - CHEBI:134742
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/delamanid.yaml
  locator: Entire native YAML; 352-native-nonactivity.yaml and all activity fields
    reconciled in 352-source-audit.json
  accessed_at: '2026-10-21T14:22:43Z'
  support: supports
  summary: The record retains delamanid exact parent identity, database-qualified
    resistance and source-labelled grouped phenotypes. Its only alias is deltyba with
    EXACT_SYNONYM typing; no native direct-binding target, clinical-status object
    or causal graph is asserted.
- evidence_id: chemistry
  kind: authority
  reference: CHEBI:134742; CAS:681492-22-8; PubChem CID6480466; ChEMBL CHEMBL218650
  locator: 352-chebi.json/.mol;352-pubchem.json;352-chembl.json;352-authority-chemistry.json
  accessed_at: '2026-10-21T14:22:43Z'
  support: supports
  summary: Official authorities agree on neutral C25H25F3N4O6 and XDAOLTSRNUSPPH-XMMPIXPASA-N.
    Eight encodings share reciprocal chirality-aware mappings, zero charge and compatible
    masses, with one configured R center. ChEBI/CARD corroborate the exact CAS. Original
    2006 Figure1 names the R compound; no racemate or product-excipient structure
    is inferred.
  snapshot_sha256: b76dd10f34d209681ac25c6141a75267d6d0996487532f09aa0576d47d4d30fc
- evidence_id: card
  kind: database
  reference: ARO:3004490; ARO:3004115
  locator: 352-card.html;352-card-class.html;352-raw-rows.json
  accessed_at: '2026-10-21T14:19:45.318536Z'
  support: supports
  summary: Current CARD and frozen inventory agree on the nitroimidazole class, parent,
    definition, deltyba alias and adopted definition review. ChEBI grants the exact
    structure while the ARO source supplies class/definition; the two-star ChEBI row
    has no independent adopted antimicrobial role.
  snapshot_sha256: ed3d76cf56298ee5eb43fafa20c5f7e544b90d7d3d3eba5860eb8466d655864f
- evidence_id: brand
  kind: authority
  reference: EMA Deltyba Summary of Product Characteristics
  locator: 352-ema-product.pdf sections1–2 and4.1, printed p2;352-ema.html product
    details
  accessed_at: '2026-10-21T14:18:12.981279Z'
  support: refutes
  summary: The official document names Deltyba 50 mg film-coated tablets and specifies
    delamanid as their active substance. Thus Deltyba is a product brand and should
    use BRAND_NAME. The combination-regimen indication supports bounded use context;
    it does not turn the tablet/excipients into the chemical parent or establish efficacy
    of every regimen.
  snapshot_sha256: 0217d4c0330d7be0e25144b70b41b7ec19c0d1a52bc5cb87e5bee11677100a00
- evidence_id: leads
  kind: database
  reference: Eleven adopted ARO/ChEBI MED identifiers
  locator: 352-adopted-core.json;352-adopted-abstracts.txt;352-lead-dispositions.json
  accessed_at: '2026-10-21T14:22:43Z'
  support: context_only
  summary: All eleven exact MED records resolve. Ten complete abstracts were read;
    the 2009 review has no indexed abstract. Original OPC-67683 work, historical reviews,
    PA-824 analogues, polar nitroimidazooxazoles, leishmaniasis candidates and unrelated
    nitroheterocyclic classes receive separate dispositions. Their analogue results
    are not silently transferred to delamanid.
  snapshot_sha256: c14b594677cdca2acffdfc13bf33edb1751b26f608e5df752c9bea2e2e8465c3
- evidence_id: definition-review
  kind: database
  reference: PMID:25210407; DOI:10.4103/0976-500x.136121
  locator: 352-definition-review.xml, complete main text
  accessed_at: '2026-10-21T14:18:54.363512Z'
  support: supports
  summary: The adopted 2014 review explicitly describes delamanid as a prodrug activated
    by Rv3547 and links it to methoxy/keto-mycolic acid suppression and combination
    treatment. Its optimistic historical safety/no-interaction language and conditional-approval
    date are not adopted as modern clinical claims.
  snapshot_sha256: 04a15213cf6e5e07a8edf886ac05577ef9d0f80704aba27b42b68f046c47239c
- evidence_id: original
  kind: primary_source
  reference: PMID:17132069; DOI:10.1371/journal.pmed.0030466
  locator: '352-original.xml: Figure1 identity; material/MIC/mycolic-acid/metabolism/intracellular
    and mouse-combination methods/results; discussion'
  accessed_at: '2026-10-21T14:18:54.363209Z'
  support: supports
  summary: Otsuka synthesized R-OPC-67683. Agar-growth assays support antimycobacterial
    activity; BCG lipid labelling shows methoxy/keto-mycolic-acid suppression, a pathway
    endpoint rather than direct binding. Susceptible BCG metabolized the drug, whereas
    a resistant strain did not; the Rv3547 mutation observation is described as unpublished
    data. Intracellular and mouse-regimen effects remain preclinical. Neither the
    desnitro end product nor every combination is declared the active antibacterial
    agent.
  snapshot_sha256: a9eb5321b0861b512465fc0e4e0c2d5ab32f41577331ecdc5f40db9bfee83977
- evidence_id: resistance
  kind: database
  reference: ARO:3007661; ARO:3007849; ARO:3009339; ARO:3009340; ARO:3009341
  locator: 352-card-ddn.html;352-card-fgd1.html;352-card-fbiA.html;352-card-fbiB.html;352-card-fbiC.html;352-card-leads-core.json
  accessed_at: '2026-10-21T14:18:54.363708Z'
  support: supports
  summary: All five exact CARD nodes assert delamanid resistance and currently classify
    it as antibiotic target alteration. The native evidence honestly labels this database
    provenance. Current sources describe Ddn activation and F420 cofactor biology,
    not direct drug inhibition of each protein. PMID36409105 concerns ddn Trp20Stop
    in a specific clinical lineage; PMID32361756 is a systematic mutation review;
    the Fbi entries cite the WHO 2023 mutation catalogue. These do not establish that
    every mutation in each gene confers resistance.
  snapshot_sha256: 91dadfa43e85898bb1428e611dd0e40d0cfc411b9846333cf0e796a7a8ccd0bc
- evidence_id: adapter
  kind: database
  reference: iModulonDB m_tuberculosis/modulome
  locator: 352-adapter-results.json and 352-adapter-retry-results.json
  accessed_at: '2026-10-21T14:22:43Z'
  support: context_only
  summary: Initial dataset/gene calls failed with DNS errors. The network retry maps
    ddn to Rv3547, fgd1 to Rv0407, fbiA to Rv3261, fbiB to Rv3262 and fbiC to Rv1173,
    with no iModulon hits. Catalog membership supports gene context only; it is neither
    binding evidence nor proof of a resistance variant.
  snapshot_sha256: de1fad02f10e0b953bb3644750aff343c370add2a4b8b68d6a83b551312b8ff6
- evidence_id: cryptic
  kind: validation
  reference: CRyPTIC3.4.0; DOI:10.5281/zenodo.15680920
  locator: 352-cryptic-table.txt;352-source-audit.json;352-membership-audit.json;
    exact native membership sidecar
  accessed_at: '2026-10-21T14:22:43Z'
  support: supports
  summary: 'All 250 groups reproduce exactly: 79 DST and 171 UKMYC groups, 210 quantitative
    rows with 155 uncensored, 31 <= and 24 > qualifiers. Source calls comprise 136
    susceptible, 74 resistant,one intermediate and 39 unspecified groups. The exact
    sidecar reconstructs 47,650 memberships across 25,038 subjects, including 7,059
    unlinked subjects. Counts do not imply unique patients, independent experiments
    or prevalence. Assay, quality, censoring and missing outcomes remain explicit.'
  snapshot_sha256: e29e3849df68b8bc9297582e150887e184bc59c4f92cf0eeec141b620fb76cc9
- evidence_id: cryptic-primary
  kind: primary_source
  reference: PMID:35944069; DOI:10.1371/journal.pbio.3001721
  locator: 352-cryptic-primary.xml, sample collection, Plate assay and Binary phenotype
    classification methods
  accessed_at: '2026-10-21T14:20:23.239820Z'
  support: context_only
  summary: The original compendium describes resistance-enriched collection, Otsuka-supplied
    DLM in UKMYC microdilution plates and ECOFF-derived binary phenotypes. This supports
    assay/interpretation context without identifying all current release 3.4.0 rows
    with the older study cohort or treating source resistance calls as independently
    reassessed clinical breakpoints.
  snapshot_sha256: 1196104e72e2e3df7daa109a76c157fd810e394f8a15b2c080603e12c5f9480d
- evidence_id: owners
  kind: database
  reference: Maintained ChEBI/CARD/CRyPTIC inputs and seeding
  locator: 352-inspect.json;352-owner-append.json;352-source-audit.json;conf/sources.yaml
    aro_mechanism_map; seeder ARO synonym projection
  accessed_at: '2026-10-21T14:22:43Z'
  support: supports
  summary: All 25 captured input hashes and five ordered histories reconcile. The
    seeder currently assigns every ARO alias EXACT_SYNONYM, explaining the brand defect.
    Its resistance type follows CARD ancestry through the maintained mechanism map;
    generated fields require maintained source/owner changes rather than a YAML-only
    patch.
  snapshot_sha256: e29e3849df68b8bc9297582e150887e184bc59c4f92cf0eeec141b620fb76cc9
- evidence_id: validation
  kind: validation
  reference: Actual focused checks
  locator: 352-focused-results.json;352-focused-run.log;352-strict.tsv;352-chemistry-authorities.log;352-ledger.log;352-membership-check.log
  accessed_at: '2026-10-21T14:22:43Z'
  support: supports
  summary: Native chemistry, independent authority mapping, schema, strict, source
    ledger and exact membership reconstruction all exit 0. Initial adapter failures
    and successful retry are separately preserved.
  snapshot_sha256: 8225dc642c68725360ccab822159569accbe40e1e9fb62aa78d2efdd220ddcc2
- evidence_id: search
  kind: search
  reference: Exact identifier, adopted publication and source-release searches
  locator: 352-local-hits.txt includes ignored files;352-fetch manifests; exact CARD/EMA/PMC
    retrievals on 2026-10-21
  accessed_at: '2026-10-21T14:22:43Z'
  support: context_only
  summary: Zenodo metadata and landing page returned 403, so release contents were
    checked through adopted source inventories and exact membership reconstruction.
    The2009 review and 2015 analogue full texts returned XML 500/browser challenges;
    the current ddn clinical paper and mutation review returned XML 500. Abstract
    or bibliographic scope is explicitly retained.
  snapshot_sha256: 581a8d3610541fdca6211652689a170cb0b0f13063e8a2bcc5ecedc0c3c9f503
  search_scope: 352-local-hits.txt includes ignored files;352-fetch manifests; exact
    CARD/EMA/PMC retrievals on 2026-10-21
assessments:
- assessment_id: identity
  area: identity
  topic: Exact R delamanid parent
  outcome: supported
  summary: Independent atom mappings, original compound assignment and source projections
    agree.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - chemistry
  - original
  - owners
- assessment_id: brand
  area: representation
  topic: Product alias typing
  outcome: concern
  summary: Deltyba is a medicinal-product brand; native EXACT_SYNONYM loses that distinction.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - record
  - brand
  - owners
- assessment_id: definition
  area: evidence
  topic: Mycolic-acid and combination-treatment description
  outcome: supported
  summary: Pathway inhibition and bounded combination-treatment context are supported;
    neither a specific terminal protein target nor universal regimen superiority follows.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - original
  - definition-review
  - brand
- assessment_id: resistance
  area: evidence
  topic: Five database resistance claims
  outcome: supported
  summary: All five claims match current CARD and remain explicitly database-cited.
    Activation/cofactor biology must be kept separate from literal direct-target inhibition.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - resistance
  - original
  - adapter
- assessment_id: mechanism-scope
  area: completeness
  topic: Activation pathway versus terminal binding target
  outcome: unknown
  summary: The record has no direct-binding edge. Exact terminal target identity and
    variant-level causal sufficiency are not established by inherited CARD categories
    or catalog membership.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - record
  - original
  - resistance
- assessment_id: activity
  area: evidence
  topic: All 250 grouped activity observations and sidecar
  outcome: supported
  summary: Every field reproduces and quantitative/categorical projections independently
    reconcile; exact collection bytes and reference validate. Source ECOFF classifications,
    methods, quality and missingness remain bounded.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - cryptic
  - cryptic-primary
  - owners
- assessment_id: provenance
  area: provenance
  topic: All adopted leads, history and maintained ownership
  outcome: supported
  summary: Eleven adopted identifiers have explicit dispositions; 25 hashes and five
    events remain unchanged. External source-access limitations are not called biological
    negatives.
  target_ids:
  - CHEBI:134742
  evidence_ids:
  - leads
  - owners
  - search
  - validation
findings:
- finding_id: F1
  issue_key: delamanid-deltyba-brand-typed-exact-synonym
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Deltyba is typed as an exact chemical synonym
  description: The sole native alias deltyba is EXACT_SYNONYM. Official EMA product
    information identifies Deltyba tablets containing delamanid, so the supported
    representation is BRAND_NAME. The current blanket ARO alias typing reproduces
    the error.
  target_ids:
  - CHEBI:134742
  field_paths:
  - synonyms[0].synonym_type
  evidence_ids:
  - record
  - brand
  - owners
  rule_id: 'review-checklist: Identity and synonym scope'
  native_severity: Minor product-versus-chemical alias typing defect
  normalization_reason: Exact chemical identity and activity evidence remain supported;
    the correction preserves the useful brand alias.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO alias text
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-specific correction configuration; add narrow typed override
      if needed
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: ARO alias typing and generated synonym owner
actions:
- action_id: A1
  description: During separately authorized curation, retain deltyba but emit BRAND_NAME
    through a reproducible narrow maintained alias-type correction. The current ARO
    seeder supplies only blanket EXACT_SYNONYM, so add and validate an explicit source/alias-specific
    type override or typed extraction support rather than claiming an existing override
    key. Regenerate and verify the resulting native synonym.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:134742
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO alias text
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-specific correction configuration; add narrow typed override
      if needed
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: ARO alias typing and generated synonym owner
  acceptance_checks:
  - The exact Deltyba alias is BRAND_NAME and the neutral R structure remains unchanged.
  - Re-extraction/reseeding preserves the typed correction and does not change unrelated
    ARO aliases.
  - All 250 grouped activities, membership payload and resistance provenance remain
    intact; run required native/corpus checks after curation.
limitations:
- All eleven adopted PMID records were checked; ten abstracts were available. PMID19075046
  lacked an abstract and attempted full text failed. Other analogue papers were assessed
  at abstract level except the inspected original 2006 study; their data are not transferred
  to delamanid.
- The original 2006 relevant methods/results and discussion were inspected, not all
  raw spectra, supplementary animal data or every plotted point. Its Rv3547 mutation
  statement explicitly refers to unpublished data and is not treated as a fully reported
  allelic-exchange experiment.
- Current CARD resistance classification is preserved as database provenance. It does
  not demonstrate direct drug binding to Ddn/Fgd1/Fbi proteins, that all variants
  are causal, or a shared resistance genotype for grouped activity observations. The
  current ddn paper was available at abstract level only.
- CRyPTIC 3.4.0 remote Zenodo access returned 403. Every maintained group and collection
  byte was checked, but source raw susceptibility experiments and original archived
  release files were not independently remeasured or downloaded.
- CRyPTIC groups include missing MICs, uncategorized calls, lower-quality observations
  and repeated subjects across methods/tables. No population resistance percentage,
  unique-patient total or universal clinical-breakpoint interpretation is inferred.
- Historical review clinical optimism is not a contemporary superiority/safety assertion.
  The EMA label supports product identity and bounded combination use, not efficacy
  of every regimen.
- Focused native checks passed; shared corpus gates remain separate. No scientific-status
  promotion or native change is part of this review.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Optional future primary-evidence enrichment should describe prodrug activation separately
  from the downstream mycolic-acid phenotype and avoid equating the inactive desnitro
  end product with the active intermediate.
- Current CARD classification semantics warrant careful qualification; the record
  already labels the five edges as database assertions, so this review does not delete
  supported resistance relationships solely because the imported mechanism category
  is broad.
- Native records, maintained inputs and history remain unchanged. Native checks used
  batch 036 and standalone chemistry the recorded batch 019 interpreter.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:134742
- https://card.mcmaster.ca/ontology/41931
- https://www.ema.europa.eu/en/medicines/human/EPAR/deltyba
- https://doi.org/10.1371/journal.pmed.0030466
tags:
- record-review
- delamanid
- cryptic-source-scope
- brand-name
```
