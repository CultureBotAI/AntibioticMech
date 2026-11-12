# (M)-viriditoxin: supported natural product with an unrepresented chiral axis

- Review: 20261021T201006Z-m-viriditoxin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:52:51Z
- Finished UTC: 2026-10-21T20:10:06Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Primary synthesis and biosynthesis support the named M atropisomer and fungal producer. Native chemical encodings preserve the two S centres but omit the stable biaryl axis; current M and P ChEBI entries serialize identically. One major representation/source-matching gap and one minor definition wording defect are retained. Published FtsZ and membrane experiments are reconciled without assigning an unsupported direct target.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 618; full native record, original thirteen input captures preserved and actual MIBiG owners appended to fifteen.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:146007 | data/antibiotics/antibacterial/m-viriditoxin.yaml | generated | (M)-viriditoxin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:146007 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:146007 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:146007 | Actual focused execution exited 0. |
| Independent native, authority and atropisomer comparison | passed | False | CHEBI:146007 | Ten encodings agree for constitution and two S centres; the M/P axis is absent and both official atropisomers have identical serializations. |
| Authoritative full QC | failed | True | CHEBI:146007 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:146007 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:146007 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:146007 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:146007 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:146007 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:146007 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:146007 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:146007 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Named atropisomer versus stored encoding

identity: concern. Targets: CHEBI:146007.

Primary drawings and ECD support the intended M product, but the stored graph cannot distinguish it from P. Two tetrahedral centres, constitution, formula and masses are consistent. A different or racemic identity is not inferred.

### Broader parent, antibacterial role and CAS boundary

grounding: supported. Targets: CHEBI:146007.

The stereo-unspecified parent is strictly broader. Named product antibacterial activity is supported. CAS is preserved as an upstream association without claiming independent licensed registry verification.

### Specific fungal producer and MIBiG matching

evidence: supported. Targets: CHEBI:146007.

The taxon is a valid synonym and primary native/heterologous studies support M production and the cluster. The existing source-quality/legacy-reference qualifications are honest. However, the matching algorithm needs an axis-aware safeguard; the key alone is insufficient.

### FtsZ evidence and membrane confounding

evidence: unknown. Targets: CHEBI:146007.

Published assays disagree under differing conditions. The record has no unsupported target assertion to correct. Optional enrichment must preserve the2003 report, negative biochemical replication, and permeability/localization effects without mislabeling viriditoxin as a demonstrated depolarizer in that assay.

### Six adopted leads and five history events

provenance: supported. Targets: CHEBI:146007.

All six adopted citations were resolved and read at stated depth. Actual source rows and maintained transformations are identified and fifteen hashes preserved. The historical review is not inherited scientific evidence or current required-field policy.

### Bounded literature and optional fields

completeness: unknown. Targets: CHEBI:146007.

Full2003/2017 assays and all raw spectra were not audited. No omission of optional MICs, resistance, clinical fields or causal graphs is scored as a defect. Current CAS and exact version4 public-source representation remain access-limited.

### Definition text quality

representation: concern. Targets: CHEBI:146007.

The duplicated words "the the" are present in both native and upstream definition. Embedded atropisomer markup is source presentation, and no malicious content or unrelated chemical claim is inferred.

## Findings

### F1: Represent the M/P distinction beyond the shared Standard InChI

major / open / confirmed; issue key: m-viriditoxin-unrepresented-atropisomer-axis.

The intended M/Ra stereoisomer and official P/Sa entry have byte-identical SMILES/InChI/key. Native aromatic linking bond10 has no axial assignment. The MIBiG row is nevertheless marked stereo_complete and used for exact-key matching. Primary drawings and ECD demonstrate stable distinct atropisomers. Preserve the supported M identity and producer evidence, but carry an explicit source-backed axial representation/identity qualification and prevent key-only joins from asserting complete atropisomer equivalence.

### F2: Remove the duplicated article in the definition

minor / open / confirmed; issue key: m-viriditoxin-definition-duplicated-article.

The definition repeats "the the" before the3/3-prime position description. Correct through source text handling while preserving stereochemical meaning.

## Recommended Actions And Acceptance Checks

### A1

Add a maintained axis-aware identity representation or explicit limitation and source-matching safeguard for this atropisomer.

- Preserve source-backed M/Ra assignment independently of the identical M/P Standard InChI. Do not flip either S tetrahedral centre or invent a distinct standard key.
- Demonstrate that M and P source concepts cannot be silently collapsed or joined solely through this shared key or RDKit tetrahedral-completeness flag.
- Keep the primary-supported P.variotii/B.spectabilis producer and exact strain/heterologous-host distinctions; do not remove a sound claim merely because its join needs strengthening.
- Regenerate the canary through maintained inputs; verify native schema/strict, chemistry, source reproduction and relevant identity cases.

### A2

Correct the duplicated article through maintained definition handling.

- Reseeding yields a single article and preserves the full M/Ra and3S/3-primeS meaning.

### A3

Use the inspected originals for optional, explicitly qualified mechanism/activity enrichment.

- Keep assay-specific lack of GTPase inhibition, PI permeability, unchanged short-timescale membrane-potential readout and MinD localization separate.
- Preserve strain, compound material, assay conditions and numeric units; recover original figure/table mappings before adding MICs.
- Do not turn docking, morphology or biosynthesis enzymes into proven antibacterial binding targets.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/m-viriditoxin.yaml; Entire native record, including definition, both aliases, parent, role, structure, CAS, source concept, producer and five history events. | supports | SEEDED/EXACT CHEBI:146007 explicitly names the M/Ra atropisomer with two S tetrahedral centres. The MIBiG producer is database-qualified, source quality questionable, with a first-legacy-reference limitation. No molecular target, numeric activity, resistance, clinical status or causal graph is asserted. |
| owners | data/raw/chebi_antimicrobials.tsv:2693; data/raw/mibig_producers.tsv:735; scripts/extract_mibig_producers.py; scripts/seed_from_sources.py; Exact rows and extraction structure_fields, primary-reference selection, and attach_mibig_producers branches read. | supports | The MIBiG row has stereo_complete=true from RDKit potential-stereo enumeration and joins by exact Standard InChIKey. The source contains one named compound, producing COMPOUND_SPECIFIC scope; this field does not itself adjudicate axial stereochemistry. The first-reference qualification is intentional and preserved. |
| search | Local ignored-inclusive identity/context search; Europe PMC viriditoxin search; Initial path inventory, exact source rows, supplementary ignored-inclusive CHEBI:146016/full-key search, all 28 returned publication titles, and historical 20260923 review read. | context_only | The bounded local full-key search finds native M, its ChEBI inventory and MIBiG row. The historical review is a lead only; its optional mechanism-completeness finding is not adopted as a defect. Snake-venom viriditoxin reports and derivative studies are distinct contexts. |
| chebi | CHEBI:146007; CHEBI:146016; CHEBI:146015; CHEBI:33282; Complete current M/P/parent entries and role definition; native and authority strings independently parsed. | supports | Official M and P definitions distinguish Ra versus Sa while their SMILES, Standard InChI and key are identical. The broader parent leaves both tetrahedral centres unspecified and is appropriate. The antibacterial role is supported by exact-name experiments. Current CAS association agrees with the import, but the CAS public shell supplies no independently inspected registry graph. |
| chemistry | 618-compare.py; 618-authority-chemistry.json; Ten encodings: native, M ChEBI, P ChEBI, PubChem and MIBiG, each SMILES/InChI; parent and axis checks. | refutes | All ten yield C34H30O14, neutral charge, key GMCZVCXZGZGZPX-HOTGVXAUSA-N and two S centres. Native aromatic linking bond10 between atoms10/11 is STEREONONE. Both official atropisomers serialize identically. Formula, masses and source mint pass. This is a demonstrated representational collision, not evidence that the named product is P or a mixture. |
| biosynthesis | PMID:31304040; DOI:10.1186/s40694-019-0072-y; PMC6600887; Full original main text and Methods, actual Figures1/6 viewed; official SI TableS3 p3 viewed. | supports | P. variotii CBS101075/CBS144490 and A. viridinutans FRR0576 are examined. Knockouts and chemical analysis identify the pathway; wild type favors M whereas vdtD deletion favors P. Actual drawings and ECD distinguish the two stable atropisomers, with two S centres retained. The commercial M standard anchors axial assignment; NMR/HMBC and ECD characterize the isolated product. This is biosynthesis evidence, not an antibacterial target experiment. |
| heterologous | PMID:31045362; DOI:10.1021/jacs.9b03354; DOI:10.1021/jacs.9b03354.s001; Complete original indexed abstract; official SI material/heterologous-expression/characterization ppS6–S7 and actual FigureS1 pS31 viewed. | supports | The original explicitly reports M with trace P from P. variotii. SI identifies CBS101075 as donor and A. nidulans LO7890 as expression host; CYA cultures at30C for14days yield metabolites. Heterologous VdtA–F and ECD compared with the M standard support the specific producer/BGC connection. Abstract ratios VdtB alone1:2 versus VdtB/VdtD20:1 concern M:P products. Full main remained403; unrelated SI experiments and all spectra were not audited. |
| mibig | BGC0001866; NCBITaxon:264951; Adopted version4 row, accessible official go/BGC0001866/1 page and public older-schema MIBiG JSON; current ENA taxonomy entry. | supports | The public entry corroborates Byssochlamys spectabilis, the named cluster, heterologous expression and both 2019 papers. ENA264951 currently prefers Paecilomyces variotii and lists B. spectabilis as a synonym; this is not a wrong taxon. The public JSON changelog ends3.1 and is not claimed as a fresh version4 snapshot. Native source version/quality/legacy-reference scope remain explicit. |
| synthesis | PMID:21413107 DOI:10.1002/anie.201007298; PMID:23049144 DOI:10.1055/s-0031-1289651; 2011 original main synthetic discussion/conclusion and note59; complete2012 indexed abstract. | supports | The synthesis establishes a 6,6-linked binaphthopyranone, unlike an older8,8-linkage assignment. Intermediate15 has X-ray-based stereochemistry; final material agrees with reported NMR. Note59 reports lower optical rotations than the historical value and qualifies purity evidence. The 2012 abstract describes a streamlined stereoselective synthesis. Neither paper title alone establishes direct FtsZ binding; no historical linkage defect is present in native chemistry. |
| original-target | PMID:12952956; DOI:10.1074/jbc.M307625200; Complete original indexed abstract. | supports | The2003 original reports fluorescent polymerization and GTPase inhibition plus morphology, macromolecular synthesis and FtsZ-expression experiments. Full assay conditions and original primary tables were not inspected here. Later experiments below constrain generalization of its target interpretation; abstract potency values are not transferred into native observations. |
| target-recheck | PMID:22958099; DOI:10.1021/cb300340j; PMC3514448; Original exact-viriditoxin Results, relevant protein/material/GTPase Methods, assay replication and discussion. | supports | Synthetic material identity was compared with fungal isolate. No FtsZ GTPase inhibition occurred up to200microM under standard E.coli/B.subtilis conditions or up to128microM in an approximate original-buffer repeat. The latter retained a different phosphate-readout assay and low basal activity; the authors do not rule out all condition-specific effects. Chemical instability is reported. Totarol aggregation findings are not transferred automatically to viriditoxin. |
| membrane | PMID:23539337; DOI:10.1039/c2md20127e; PMC3607388; Original exact-compound Results and susceptibility, flow-cytometry, microscopy and analysis Methods. | supports | Compound6 is synthetic viriditoxin. In B.subtilis168 it increased PI permeability at1xMIC but did not measurably lower DiOC2 membrane-potential ratio on the tested timescale. GFP-MinD localization was assessed in B.subtilisDS4294; this is distinct from the168 susceptibility assay. Membrane perturbation can confound localization-based FtsZ inference. E.coli MinD experiments used compounds1/2, not viriditoxin. No direct protein-binding conclusion follows. |
| remaining-leads | PMID:29037949 DOI:10.1016/j.bmcl.2017.10.015; PMID:25231051 DOI:10.3892/ijo.2014.2659; Both complete indexed original abstracts. | supports | The2017 original supports jellyfish-derived P.variotii and antibacterial effects against S.iniae/S.parauberis; morphology and S.aureus FtsZ docking are not direct target proof. The2014 paper concerns prostate-cancer apoptosis/autophagy and microtubules; host effects do not establish antibacterial mechanism. Exact strain/MIC/purity details were not recovered from these abstract-only reads. |
| adapter | iModulonDB via kg-microbe-sources; Dataset catalog and exact FtsZ searches before open-ended mechanism follow-up. | context_only | No fungal dataset matches the producer. E.coli precise1k/b0095 and B.subtilis modulome/BSU_15290 identify FtsZ genes with no component hits. An initial unsupported b_subtilis/precise query returned no hits and was corrected to the catalog key; that empty result is not evidence of absence. Gene membership does not prove viriditoxin binding. |

## Limits And Additional Notes

- The2019 Fungal Biology and Biotechnology main text was read in full, with Figures1/6 and SI TableS3 visually inspected. All raw spectra and supplementary experimental results were not reprocessed.
- The2019 ACS main remained403; its complete abstract and official SI ppS6–S7, S11/S12 contextual tables and actual FigureS1 atS31 were inspected. The remaining SI was not read in full.
- The2011 synthesis was read in main synthetic discussion/conclusion and note59; original crystal coordinates and all synthetic SI were not audited. The2012 synthesis was read only at complete-abstract depth.
- The2003 discovery,2017 fish-pathogen and2014 host-cancer studies remain complete-abstract-depth assessments here. No exact numeric MIC or direct binding assertion is imported from them.
- The2012 biochemical and2013 cellular studies were inspected in exact-compound Results and relevant Methods. Whole unrelated-compound datasets and raw images were not reanalyzed; the2013 MIC table contains structure images not independently mapped here.
- The public CAS page was an application shell; current licensed registry chemistry is unverified. Accessible MIBiG public page/JSON are older-version representations, distinct from the adopted version4 row.
- Some200-status figure/PDF responses were HTML challenge/viewer pages and were excluded. Correct official CDN figures and publisher SI were subsequently retrieved and inspected.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Original thirteen input hashes were preserved and actual MIBiG owners expanded the set to fifteen. All retrieval manifests retain real timestamps, response outcomes and file hashes.
- The auxiliary PubChem lookup and P ChEBI comparison are diagnostic comparators, not additional asserted native xrefs.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T201006Z-m-viriditoxin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: '(M)-viriditoxin: supported natural product with an unrepresented chiral axis'
started_at: '2026-10-21T19:52:51Z'
finished_at: '2026-10-21T20:10:06Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire record
    and maintained source were read, independent chemistry calculated, asserted chemical
    groundings checked and exact-compound primary literature assessed with explicit
    access boundaries.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Primary synthesis and biosynthesis support the named M atropisomer and fungal
  producer. Native chemical encodings preserve the two S centres but omit the stable
  biaryl axis; current M and P ChEBI entries serialize identically. One major representation/source-matching
  gap and one minor definition wording defect are retained. Published FtsZ and membrane
  experiments are reconciled without assigning an unsupported direct target.
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
  - path: data/antibiotics/antibacterial/m-viriditoxin.yaml
    sha256: 0f88e011c939a9a2a33b4edf68164e85e7fd90682c0c8773f718f1d8de8e84d4
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
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
    role: context
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
    role: context
targets:
- target_id: CHEBI:146007
  path: data/antibiotics/antibacterial/m-viriditoxin.yaml
  label: (M)-viriditoxin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/mibig_producers.tsv
    role: Actual maintained source or source-handling owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: Actual maintained source or source-handling owner
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 618; full native record, original thirteen input captures
    preserved and actual MIBiG owners appended to fifteen.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:146007
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:146007
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    618
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:146007
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/m-viriditoxin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:146007
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/m-viriditoxin.yaml --out /private/tmp/am-review-session/618-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-comparison
  name: Independent native, authority and atropisomer comparison
  status: passed
  required: false
  summary: Ten encodings agree for constitution and two S centres; the M/P axis is
    absent and both official atropisomers have identical serializations.
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/618-compare.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:146007
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:146007
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
  - CHEBI:146007
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
  - CHEBI:146007
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
  - CHEBI:146007
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
  - CHEBI:146007
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
  - CHEBI:146007
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
  - CHEBI:146007
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
  - CHEBI:146007
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
  - CHEBI:146007
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/m-viriditoxin.yaml
  locator: Entire native record, including definition, both aliases, parent, role,
    structure, CAS, source concept, producer and five history events.
  accessed_at: '2026-10-21T20:01:45Z'
  support: supports
  summary: SEEDED/EXACT CHEBI:146007 explicitly names the M/Ra atropisomer with two
    S tetrahedral centres. The MIBiG producer is database-qualified, source quality
    questionable, with a first-legacy-reference limitation. No molecular target, numeric
    activity, resistance, clinical status or causal graph is asserted.
  snapshot_sha256: 9a12a3b763de2ef0917329e25328758d477168f2b49d8fb8236b8b91ce169bd3
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:2693; data/raw/mibig_producers.tsv:735;
    scripts/extract_mibig_producers.py; scripts/seed_from_sources.py
  locator: Exact rows and extraction structure_fields, primary-reference selection,
    and attach_mibig_producers branches read.
  accessed_at: '2026-10-21T20:01:45Z'
  support: supports
  summary: The MIBiG row has stereo_complete=true from RDKit potential-stereo enumeration
    and joins by exact Standard InChIKey. The source contains one named compound,
    producing COMPOUND_SPECIFIC scope; this field does not itself adjudicate axial
    stereochemistry. The first-reference qualification is intentional and preserved.
  snapshot_sha256: 06a120d4a69851c61e5cf5b99fb694df498fb756a5565af0a312c4d32d241b48
- evidence_id: search
  kind: search
  reference: Local ignored-inclusive identity/context search; Europe PMC viriditoxin
    search
  locator: Initial path inventory, exact source rows, supplementary ignored-inclusive
    CHEBI:146016/full-key search, all 28 returned publication titles, and historical
    20260923 review read.
  accessed_at: '2026-10-21T20:01:45Z'
  support: context_only
  summary: The bounded local full-key search finds native M, its ChEBI inventory and
    MIBiG row. The historical review is a lead only; its optional mechanism-completeness
    finding is not adopted as a defect. Snake-venom viriditoxin reports and derivative
    studies are distinct contexts.
  search_scope: Initial hidden/ignored-inclusive label/identifier/slug search plus
    rg --no-ignore --hidden for CHEBI:146016 and full key in data/antibiotics, data/raw,
    curation and conf. Europe PMC TITLE_ABS viriditoxin returned 28 titles; six adopted
    leads and selected originals were followed. No exhaustive literature absence is
    claimed.
  snapshot_sha256: b246794d575adc211d9365411822dc1ac45afbe0f36c80ae71b2fad03ba0cc83
- evidence_id: chebi
  kind: authority
  reference: CHEBI:146007; CHEBI:146016; CHEBI:146015; CHEBI:33282
  locator: Complete current M/P/parent entries and role definition; native and authority
    strings independently parsed.
  accessed_at: '2026-10-21T20:01:45Z'
  support: supports
  summary: Official M and P definitions distinguish Ra versus Sa while their SMILES,
    Standard InChI and key are identical. The broader parent leaves both tetrahedral
    centres unspecified and is appropriate. The antibacterial role is supported by
    exact-name experiments. Current CAS association agrees with the import, but the
    CAS public shell supplies no independently inspected registry graph.
  snapshot_sha256: 8d4fecdd79b6e92a48c1336d5072d8669af33f1e303288ed01036741277aedfe
- evidence_id: chemistry
  kind: validation
  reference: 618-compare.py; 618-authority-chemistry.json
  locator: 'Ten encodings: native, M ChEBI, P ChEBI, PubChem and MIBiG, each SMILES/InChI;
    parent and axis checks.'
  accessed_at: '2026-10-21T20:01:45Z'
  support: refutes
  summary: All ten yield C34H30O14, neutral charge, key GMCZVCXZGZGZPX-HOTGVXAUSA-N
    and two S centres. Native aromatic linking bond10 between atoms10/11 is STEREONONE.
    Both official atropisomers serialize identically. Formula, masses and source mint
    pass. This is a demonstrated representational collision, not evidence that the
    named product is P or a mixture.
  snapshot_sha256: b5c6c7e85d5680dd106e5ebc9dbe91a9ab6b401dddc4eb359714ed2a31591cc1
- evidence_id: biosynthesis
  kind: primary_source
  reference: PMID:31304040; DOI:10.1186/s40694-019-0072-y; PMC6600887
  locator: Full original main text and Methods, actual Figures1/6 viewed; official
    SI TableS3 p3 viewed.
  accessed_at: '2026-10-21T20:01:45Z'
  support: supports
  summary: P. variotii CBS101075/CBS144490 and A. viridinutans FRR0576 are examined.
    Knockouts and chemical analysis identify the pathway; wild type favors M whereas
    vdtD deletion favors P. Actual drawings and ECD distinguish the two stable atropisomers,
    with two S centres retained. The commercial M standard anchors axial assignment;
    NMR/HMBC and ECD characterize the isolated product. This is biosynthesis evidence,
    not an antibacterial target experiment.
  snapshot_sha256: f4350ed8e4d2cec8f572210b9799a18e191e4c87becd5e09f8e0bfd6b5b177c4
- evidence_id: heterologous
  kind: primary_source
  reference: PMID:31045362; DOI:10.1021/jacs.9b03354; DOI:10.1021/jacs.9b03354.s001
  locator: Complete original indexed abstract; official SI material/heterologous-expression/characterization
    ppS6–S7 and actual FigureS1 pS31 viewed.
  accessed_at: '2026-10-21T20:01:45Z'
  support: supports
  summary: The original explicitly reports M with trace P from P. variotii. SI identifies
    CBS101075 as donor and A. nidulans LO7890 as expression host; CYA cultures at30C
    for14days yield metabolites. Heterologous VdtA–F and ECD compared with the M standard
    support the specific producer/BGC connection. Abstract ratios VdtB alone1:2 versus
    VdtB/VdtD20:1 concern M:P products. Full main remained403; unrelated SI experiments
    and all spectra were not audited.
  snapshot_sha256: 06eaa62cb15ff03da0d127cdc7e5fa371e4665216579e2a6bd116f0051308bf7
- evidence_id: mibig
  kind: database
  reference: BGC0001866; NCBITaxon:264951
  locator: Adopted version4 row, accessible official go/BGC0001866/1 page and public
    older-schema MIBiG JSON; current ENA taxonomy entry.
  accessed_at: '2026-10-21T20:01:45Z'
  support: supports
  summary: The public entry corroborates Byssochlamys spectabilis, the named cluster,
    heterologous expression and both 2019 papers. ENA264951 currently prefers Paecilomyces
    variotii and lists B. spectabilis as a synonym; this is not a wrong taxon. The
    public JSON changelog ends3.1 and is not claimed as a fresh version4 snapshot.
    Native source version/quality/legacy-reference scope remain explicit.
  snapshot_sha256: 96f1e4a4a4d1c2e27e5376b06e896a4a0790b2ac3bf3d600ab6383c1254d1302
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:21413107 DOI:10.1002/anie.201007298; PMID:23049144 DOI:10.1055/s-0031-1289651
  locator: 2011 original main synthetic discussion/conclusion and note59; complete2012
    indexed abstract.
  accessed_at: '2026-10-21T20:01:45Z'
  support: supports
  summary: The synthesis establishes a 6,6-linked binaphthopyranone, unlike an older8,8-linkage
    assignment. Intermediate15 has X-ray-based stereochemistry; final material agrees
    with reported NMR. Note59 reports lower optical rotations than the historical
    value and qualifies purity evidence. The 2012 abstract describes a streamlined
    stereoselective synthesis. Neither paper title alone establishes direct FtsZ binding;
    no historical linkage defect is present in native chemistry.
  snapshot_sha256: 004b4f7bf2c94c43a2a8bddc78cfee45bf730b4b69a64605db79b3ee03411119
- evidence_id: original-target
  kind: primary_source
  reference: PMID:12952956; DOI:10.1074/jbc.M307625200
  locator: Complete original indexed abstract.
  accessed_at: '2026-10-21T20:01:45Z'
  support: supports
  summary: The2003 original reports fluorescent polymerization and GTPase inhibition
    plus morphology, macromolecular synthesis and FtsZ-expression experiments. Full
    assay conditions and original primary tables were not inspected here. Later experiments
    below constrain generalization of its target interpretation; abstract potency
    values are not transferred into native observations.
  snapshot_sha256: 1243a1b5f8c3f0b8ad568ddc6cf489feb1baa8d968fa81a13cdc1d13ff8b66af
- evidence_id: target-recheck
  kind: primary_source
  reference: PMID:22958099; DOI:10.1021/cb300340j; PMC3514448
  locator: Original exact-viriditoxin Results, relevant protein/material/GTPase Methods,
    assay replication and discussion.
  accessed_at: '2026-10-21T20:01:45Z'
  support: supports
  summary: Synthetic material identity was compared with fungal isolate. No FtsZ GTPase
    inhibition occurred up to200microM under standard E.coli/B.subtilis conditions
    or up to128microM in an approximate original-buffer repeat. The latter retained
    a different phosphate-readout assay and low basal activity; the authors do not
    rule out all condition-specific effects. Chemical instability is reported. Totarol
    aggregation findings are not transferred automatically to viriditoxin.
  snapshot_sha256: 517fe1f82097d152ba695943af8d7e32d7d4e4f01065a95fc022af98c795d85f
- evidence_id: membrane
  kind: primary_source
  reference: PMID:23539337; DOI:10.1039/c2md20127e; PMC3607388
  locator: Original exact-compound Results and susceptibility, flow-cytometry, microscopy
    and analysis Methods.
  accessed_at: '2026-10-21T20:01:45Z'
  support: supports
  summary: Compound6 is synthetic viriditoxin. In B.subtilis168 it increased PI permeability
    at1xMIC but did not measurably lower DiOC2 membrane-potential ratio on the tested
    timescale. GFP-MinD localization was assessed in B.subtilisDS4294; this is distinct
    from the168 susceptibility assay. Membrane perturbation can confound localization-based
    FtsZ inference. E.coli MinD experiments used compounds1/2, not viriditoxin. No
    direct protein-binding conclusion follows.
  snapshot_sha256: 594e1db57263151a892b4dc52e507e8245f7ae1acd22167ea42a32bd14ee3baa
- evidence_id: remaining-leads
  kind: primary_source
  reference: PMID:29037949 DOI:10.1016/j.bmcl.2017.10.015; PMID:25231051 DOI:10.3892/ijo.2014.2659
  locator: Both complete indexed original abstracts.
  accessed_at: '2026-10-21T20:01:45Z'
  support: supports
  summary: The2017 original supports jellyfish-derived P.variotii and antibacterial
    effects against S.iniae/S.parauberis; morphology and S.aureus FtsZ docking are
    not direct target proof. The2014 paper concerns prostate-cancer apoptosis/autophagy
    and microtubules; host effects do not establish antibacterial mechanism. Exact
    strain/MIC/purity details were not recovered from these abstract-only reads.
  snapshot_sha256: 0fdf1d249c17d68b77784a9f6f187ab2a7cadab2ab197acfa8f5e7d0d210b7e3
- evidence_id: adapter
  kind: database
  reference: iModulonDB via kg-microbe-sources
  locator: Dataset catalog and exact FtsZ searches before open-ended mechanism follow-up.
  accessed_at: '2026-10-21T20:01:45Z'
  support: context_only
  summary: No fungal dataset matches the producer. E.coli precise1k/b0095 and B.subtilis
    modulome/BSU_15290 identify FtsZ genes with no component hits. An initial unsupported
    b_subtilis/precise query returned no hits and was corrected to the catalog key;
    that empty result is not evidence of absence. Gene membership does not prove viriditoxin
    binding.
  snapshot_sha256: 680df807f6294c2c3364bf5448e7d4a59f172d9ba91d18f27e4bf4e73a6f5bd5
assessments:
- assessment_id: identity
  area: identity
  topic: Named atropisomer versus stored encoding
  outcome: concern
  summary: Primary drawings and ECD support the intended M product, but the stored
    graph cannot distinguish it from P. Two tetrahedral centres, constitution, formula
    and masses are consistent. A different or racemic identity is not inferred.
  target_ids:
  - CHEBI:146007
  evidence_ids:
  - native
  - chemistry
  - biosynthesis
  - heterologous
  - synthesis
- assessment_id: parents
  area: grounding
  topic: Broader parent, antibacterial role and CAS boundary
  outcome: supported
  summary: The stereo-unspecified parent is strictly broader. Named product antibacterial
    activity is supported. CAS is preserved as an upstream association without claiming
    independent licensed registry verification.
  target_ids:
  - CHEBI:146007
  evidence_ids:
  - chebi
  - chemistry
  - membrane
  - remaining-leads
- assessment_id: producer
  area: evidence
  topic: Specific fungal producer and MIBiG matching
  outcome: supported
  summary: The taxon is a valid synonym and primary native/heterologous studies support
    M production and the cluster. The existing source-quality/legacy-reference qualifications
    are honest. However, the matching algorithm needs an axis-aware safeguard; the
    key alone is insufficient.
  target_ids:
  - CHEBI:146007
  evidence_ids:
  - biosynthesis
  - heterologous
  - mibig
  - owners
  - chemistry
- assessment_id: mechanism
  area: evidence
  topic: FtsZ evidence and membrane confounding
  outcome: unknown
  summary: Published assays disagree under differing conditions. The record has no
    unsupported target assertion to correct. Optional enrichment must preserve the2003
    report, negative biochemical replication, and permeability/localization effects
    without mislabeling viriditoxin as a demonstrated depolarizer in that assay.
  target_ids:
  - CHEBI:146007
  evidence_ids:
  - original-target
  - target-recheck
  - membrane
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Six adopted leads and five history events
  outcome: supported
  summary: All six adopted citations were resolved and read at stated depth. Actual
    source rows and maintained transformations are identified and fifteen hashes preserved.
    The historical review is not inherited scientific evidence or current required-field
    policy.
  target_ids:
  - CHEBI:146007
  evidence_ids:
  - native
  - owners
  - search
  - synthesis
  - biosynthesis
  - heterologous
  - remaining-leads
- assessment_id: completeness
  area: completeness
  topic: Bounded literature and optional fields
  outcome: unknown
  summary: Full2003/2017 assays and all raw spectra were not audited. No omission
    of optional MICs, resistance, clinical fields or causal graphs is scored as a
    defect. Current CAS and exact version4 public-source representation remain access-limited.
  target_ids:
  - CHEBI:146007
  evidence_ids:
  - search
  - mibig
  - remaining-leads
  - original-target
- assessment_id: wording
  area: representation
  topic: Definition text quality
  outcome: concern
  summary: The duplicated words "the the" are present in both native and upstream
    definition. Embedded atropisomer markup is source presentation, and no malicious
    content or unrelated chemical claim is inferred.
  target_ids:
  - CHEBI:146007
  evidence_ids:
  - native
  - chebi
findings:
- finding_id: F1
  issue_key: m-viriditoxin-unrepresented-atropisomer-axis
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Represent the M/P distinction beyond the shared Standard InChI
  description: The intended M/Ra stereoisomer and official P/Sa entry have byte-identical
    SMILES/InChI/key. Native aromatic linking bond10 has no axial assignment. The
    MIBiG row is nevertheless marked stereo_complete and used for exact-key matching.
    Primary drawings and ECD demonstrate stable distinct atropisomers. Preserve the
    supported M identity and producer evidence, but carry an explicit source-backed
    axial representation/identity qualification and prevent key-only joins from asserting
    complete atropisomer equivalence.
  target_ids:
  - CHEBI:146007
  field_paths:
  - chemical_structure
  - producer_organisms[0].note
  evidence_ids:
  - chemistry
  - chebi
  - biosynthesis
  - heterologous
  - owners
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/mibig_producers.tsv
    role: Actual maintained source or source-handling owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: Actual maintained source or source-handling owner
  rule_id: One exact structure; stereochemical completeness and exact matching
  normalization_reason: Major missing stereochemical representation and matching safeguard.
    The label/definition identify the intended supported M molecule, so this is not
    a confirmed wrong-isomer blocker.
- finding_id: F2
  issue_key: m-viriditoxin-definition-duplicated-article
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Remove the duplicated article in the definition
  description: The definition repeats "the the" before the3/3-prime position description.
    Correct through source text handling while preserving stereochemical meaning.
  target_ids:
  - CHEBI:146007
  field_paths:
  - definition
  evidence_ids:
  - native
  - chebi
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  rule_id: Clear definition wording
  normalization_reason: Bounded non-blocking prose defect.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - CHEBI:146007
  description: Add a maintained axis-aware identity representation or explicit limitation
    and source-matching safeguard for this atropisomer.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/mibig_producers.tsv
    role: Actual maintained source or source-handling owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: Actual maintained source or source-handling owner
  generator: scripts/extract_mibig_producers.py; scripts/seed_from_sources.py after
    separately authorized schema/source policy adjudication
  acceptance_checks:
  - Preserve source-backed M/Ra assignment independently of the identical M/P Standard
    InChI. Do not flip either S tetrahedral centre or invent a distinct standard key.
  - Demonstrate that M and P source concepts cannot be silently collapsed or joined
    solely through this shared key or RDKit tetrahedral-completeness flag.
  - Keep the primary-supported P.variotii/B.spectabilis producer and exact strain/heterologous-host
    distinctions; do not remove a sound claim merely because its join needs strengthening.
  - Regenerate the canary through maintained inputs; verify native schema/strict,
    chemistry, source reproduction and relevant identity cases.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - CHEBI:146007
  description: Correct the duplicated article through maintained definition handling.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  acceptance_checks:
  - Reseeding yields a single article and preserves the full M/Ra and3S/3-primeS meaning.
- action_id: A3
  finding_ids: []
  target_ids:
  - CHEBI:146007
  description: Use the inspected originals for optional, explicitly qualified mechanism/activity
    enrichment.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  acceptance_checks:
  - Keep assay-specific lack of GTPase inhibition, PI permeability, unchanged short-timescale
    membrane-potential readout and MinD localization separate.
  - Preserve strain, compound material, assay conditions and numeric units; recover
    original figure/table mappings before adding MICs.
  - Do not turn docking, morphology or biosynthesis enzymes into proven antibacterial
    binding targets.
limitations:
- The2019 Fungal Biology and Biotechnology main text was read in full, with Figures1/6
  and SI TableS3 visually inspected. All raw spectra and supplementary experimental
  results were not reprocessed.
- The2019 ACS main remained403; its complete abstract and official SI ppS6–S7, S11/S12
  contextual tables and actual FigureS1 atS31 were inspected. The remaining SI was
  not read in full.
- The2011 synthesis was read in main synthetic discussion/conclusion and note59; original
  crystal coordinates and all synthetic SI were not audited. The2012 synthesis was
  read only at complete-abstract depth.
- The2003 discovery,2017 fish-pathogen and2014 host-cancer studies remain complete-abstract-depth
  assessments here. No exact numeric MIC or direct binding assertion is imported from
  them.
- The2012 biochemical and2013 cellular studies were inspected in exact-compound Results
  and relevant Methods. Whole unrelated-compound datasets and raw images were not
  reanalyzed; the2013 MIC table contains structure images not independently mapped
  here.
- The public CAS page was an application shell; current licensed registry chemistry
  is unverified. Accessible MIBiG public page/JSON are older-version representations,
  distinct from the adopted version4 row.
- Some200-status figure/PDF responses were HTML challenge/viewer pages and were excluded.
  Correct official CDN figures and publisher SI were subsequently retrieved and inspected.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Original thirteen input hashes were preserved and actual MIBiG owners expanded the
  set to fifteen. All retrieval manifests retain real timestamps, response outcomes
  and file hashes.
- The auxiliary PubChem lookup and P ChEBI comparison are diagnostic comparators,
  not additional asserted native xrefs.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
