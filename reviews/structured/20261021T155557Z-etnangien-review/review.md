# Etnangien: exact free-acid identity and antibacterial scope supported

- Review: 20261021T155557Z-etnangien-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:30:53Z
- Finished UTC: 2026-10-21T15:55:57Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native encodings and current official molfile agree on the exact etnangien free acid. All twelve stereocentres match an independent mapping of the original total-synthesis supplement drawing, and the literature distinguishes this natural product from its methyl ester and simplified analogues. The Gram-positive activity and Sorangium origin are supported. No confirmed defect was found; unavailable primary main texts and the inaccessible Reaxys substance record remain explicit limits. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 420; one entire native record. All thirteen initial source-input hashes were verified before judgment and retained. Exact source-row inspection confirmed the existing ChEBI extractor/seeder ownership; no additional maintained input was needed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65868 | data/antibiotics/antibacterial/etnangien.yaml | generated | etnangien |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:65868 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:65868 | Actual focused execution exited 0. |
| Focused chemistry verification | passed | False | CHEBI:65868 | Actual focused execution exited 0. |
| authority-map | passed | False | CHEBI:65868 | Native SMILES, native InChI, official ChEBI molfile and NP Atlas InChI independently agree on the complete key, formula, charge and twelve assigned stereocentres. |
| primary-stereo | passed | False | CHEBI:65868 | The twelve wedge/dash directions transcribed from original 2009 SI page S48 were assigned independently on native connectivity after removing native chiral tags; all twelve CIP assignments agree. |
| adapter-catalog | passed | False | CHEBI:65868 | The complete public catalog was inspected before mechanism follow-up. Native names no gene, protein or transcriptomics experiment; Sorangium is not a covered organism. No expression module was substituted for experimental activity or enzyme inhibition. |
| Authoritative full QC | failed | True | CHEBI:65868 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65868 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65868 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65868 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65868 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65868 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65868 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65868 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65868 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact natural free acid, stereochemistry and names

identity: supported. Targets: CHEBI:65868.

The graph, systematic name, official structure and original mapped total-synthesis drawing agree. The free acid is distinct from the methyl ester, truncated analogues and the older patent assignment.

### Antibacterial classification and Gram-positive definition

evidence: supported. Targets: CHEBI:65868.

The exact-parent discovery abstract and separately identified acid column in original patent Table2 support the native class and roles. The assay values remain strain/material-specific and are not clinical breakpoints.

### Sorangium culture-broth origin

evidence: supported. Targets: CHEBI:65868.

Original isolation names So ce750 and So ce1045; the patents provide fermentation/isolation context. These support the qualitative native producer statement. Synthetic ester formation and heterologous biosynthetic examples are not substituted for natural acid production.

### Chemical xref versus document scope

provenance: unknown. Targets: CHEBI:65868.

The four patent references are relevant documents and are correctly separated from chemical equivalence. Reaxys18923823 is reproduced by current ChEBI but its underlying exact substance record remains unverified at this free-source depth.

### Optional mechanism, targets and other biology

completeness: supported. Targets: CHEBI:65868.

Primary leads support polymerase-inhibition follow-up, but the SEEDED record makes no unsupported specific binding or whole-cell causal assertion. Optional mode, target, activity, producer, dataset and graph enrichment is not a confirmed defect. No REVIEWED promotion is implied.

### Source ownership, citation disposition and history

provenance: supported. Targets: CHEBI:65868.

Every native field and all three adopted leads were assessed. The four source events and current SEEDED status are preserved. The maintained extractor keeps citations as leads, so absence of record-level copied references is intentional rather than a lost-evidence defect.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/etnangien.yaml; Entire native YAML. | supports | The SEEDED, EXACT CHEBI65868 record contains one stereospecific systematic synonym, two broader parents, antimicrobial and antibacterial roles, the neutral C49H76O11 structure, one Reaxys chemical xref, four patent document xrefs, one ChEBI source concept and four seed/reseed events. It asserts no molecular target, mode, numerical assay, resistance determinant, clinical status, structured producer, expression dataset or causal graph. The definition names culture-broth origin in Sorangium cellulosum and Gram-positive activity. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml; Complete exact row 1340 and applicable source extraction, classification, citation and xref-routing logic. | supports | ChEBI supplies every native scientific field and the three adopted literature leads. Extraction selects reviewed in-scope roles and retains citations as leads rather than asserting record-level experimental evidence. The seeder deliberately moves patent references into document_xrefs, where they do not assert exact chemical equivalence. No exact ARO, FDA, PubChem or MIBiG row matches the inspected source IDs or full key. Original input hashes and the source version 2026-08-30 were preserved. |
| chebi | CHEBI:65868; https://www.ebi.ac.uk/chebi/CHEBI:65868; Complete current official entry, systematic name, properties, relationships, registry entry and document links. | supports | Current ChEBI agrees with the native neutral free acid and systematic stereochemical name. CHEBI25105 is the broader macrolide-antibiotic class and CHEBI35868 is hydroxy monocarboxylic acid; CHEBI33281 and CHEBI33282 mean antimicrobial and antibacterial agent. The displayed metabolite role is outside the imported antimicrobial-role slice and is not a required missing role. ChEBI repeats Reaxys18923823, but the underlying Reaxys substance page was not inspected. All four patent identifiers resolve as documents after using the B1 publication for EP2014655; the initially attempted A1 route returned 404. |
| graphs | 420-xref-chemistry.json; https://www.ebi.ac.uk/chebi/backend/api/public/molfile/65868; https://www.npatlas.org/explore/compounds/NPA008563; Independent native and authority graph parsing; complete NP Atlas identity/revision page read. | supports | Both native encodings, the official molfile and NP Atlas InChI reproduce VHPBIOVAVQXSJO-DLGDGFEOSA-N, neutral C49H76O11 and monoisotopic mass 840.538763252. Twelve tetrahedral centres and nine alkene geometries are assigned. NP Atlas explicitly links the original planar assignment to PMID17547459 and the later stereochemical revision to PMID18826315. Database agreement is corroboration, not a replacement for the original structure drawing. |
| original-discovery | PMID:17547459; DOI:10.1021/np070115h; Complete indexed original abstract; main article retrieval attempted but unavailable. | supports | The original publication identifies etnangien compound 1 from Sorangium cellulosum strains So ce750 and So ce1045, describes a macrocyclic lactone with a C21 carboxylic-acid side chain and all-E hexaene, reports Gram-positive activity and initial bacterial/viral nucleic-acid-polymerase inhibition. This supports the qualitative native definition. No precise MIC, direct binding site, subunit assignment or whole-cell causal chain is inferred from the abstract. |
| stereochemistry | PMID:19645468; DOI:10.1021/ja9056163; DOI:10.1021/ja9056163.s001; https://acs.figshare.com/articles/journal_contribution/Total_Synthesis_of_Etnangien/2832724; Complete original indexed abstract; official supplement pages S44–S49 read, S46 and S48 drawings visually inspected, complete S48–S49 comparison table read. | supports | The supplement separately prepares etnangien methyl ester and then converts it with porcine liver esterase to etnangien. The free acid has C49H76O11, measured negative-ion HRMS matching its formula, positive optical rotation and an explicit comparison with authentic natural material. The S48 drawing has C6S, C20R, C21R, C22S, C24R, C28S, C35S, C36R, C37S, C38S, C39R and C40R; independent wedge/dash assignment matches every native centre. The seven side-chain alkenes are E and the macrocyclic diene is 30Z,32E, matching the native name/graph. This is a mapped published assignment, not an independent re-elucidation of raw spectra. |
| earlier-stereo | PMID:18826315; DOI:10.1021/ja804194c; DOI:10.1021/ja804194c.s001; Complete indexed/publisher abstract and official supplementary pages S1–S3 read. | supports | The 2008 study assigns relative and absolute stereochemistry using NMR, derivatization, modeling and biosynthetic analysis. Its supplement identifies the more stable methyl ester as compound 2 and supplies its NMR table. These ester measurements are not silently treated as a direct assay of the free acid. The main article and the remainder of the 21-page supplement were not fully reviewed. |
| synthesis-followup | PMID:20334428; DOI:10.1021/jo100201f; https://www.researchgate.net/publication/42540624_Stereoselective_Total_Synthesis_of_Etnangien_and_Etnangien_Methyl_Ester; Author-deposited full text accessed through the web tool; Introduction, final coupling/deprotection discussion, Conclusions and final methyl-ester/free-acid experimental entries read. | supports | The 2010 full account confirms that ester hydrolysis yields etnangien identical to authentic material by NMR, HRMS, chromatographic behavior and optical rotation. It distinguishes the labile free acid from the more stable methyl ester and describes translactonization/isomerization problems during synthesis. Only the stated selected sections were assessed; the full synthetic route and all spectra were not independently reconstructed. |
| patent-activity | patent:EP2014655; EP2014655B1; https://patents.google.com/patent/EP2014655B1/en; Complete description and examples read; original PDF pages 3 and 7 visually inspected, including full Table 2 and units. | supports | Formula I distinguishes etnangien acid 1 with R=H from ester 2. Table 2 reports separate acid/ester MIC columns. The acid column includes S. aureus 1.0 µg/mL, a rifampicin-resistant S. aureus isolate 0.62 µg/mL, C. glutamicum DSM20300 0.03 µg/mL and M. luteus 0.06 µg/mL. Testing uses serial dilution with the reported peptone/meat-extract/yeast-extract growth medium at pH7; detailed standardized clinical breakpoints are not supplied. The PDF glyph is µg/mL despite text extraction rendering mg/mL. This independently supports bacterial activity, without transferring the methyl-ester values, proving clinical efficacy or assigning a resistance mechanism. |
| patent-scope | patent:DE19630980; patent:WO2008142046; patent:EP2247740; https://patents.google.com/patent/DE19630980A1/en; https://patents.google.com/patent/WO2008142046A1/en; https://patents.google.com/patent/EP2247740A1/en; DE19630980 description read in the supplied English translation; WO2008142046 identity, isolation and activity sections; EP2247740 description and experimental examples. | supports | The early DE document reports production by So ce750/DSM11028 and an older structural assignment. The later derivative patents explicitly discuss a corrected C38 hydroxyl assignment and distinguish acid from ester. EP2247740 concerns biosynthetic coding sequences and production experiments in Sorangium, not an antimicrobial target. These documents are scientifically relevant historical/production references; native correctly treats them as document_xrefs rather than chemical equivalents. Proposed pharmaceutical use in a patent is not regulatory approval. Sequence listings and all patent figures were not reanalysed. |
| mechanism-scope | EP2014655B1 examples 3–4; PMID:17547459; Original patent assay description and discovery abstract. | supports | The patent describes biochemical inhibition assays for E. coli RNA polymerase, E. coli DNA polymerase and retroviral reverse transcriptases, while whole E. coli cells remain poorly susceptible under its reported conditions. The text explicitly presents RNA-polymerase mediation of antibacterial activity as an assumption. Enzyme inhibition is a defensible follow-up lead, but it does not establish a specific subunit-binding site or a unique whole-cell mechanism. No such target is currently asserted in native. Biosynthetic Etn proteins are separate from antimicrobial targets. |
| adopted-leads | PMID:17547459; PMID:19645468; PMID:22832317; All three adopted bibliographic records and complete indexed abstracts. | context_only | PMID17547459 is the original isolation/activity paper; PMID19645468 is the total synthesis with publicly retrieved supplementary identity evidence; PMID22832317, DOI10.1016/j.bmcl.2012.06.070, tests designed simplified side chains and is an analogue study rather than standalone exact-parent assay proof. The latter full paper was not obtained: the advertised author-repository URL returned a DSpace application shell through curl, not a PDF. Additional biosynthetic and gladiolin search hits were treated as context and were not transferred to native etnangien claims. |
| adapter | iModulonDB public dataset catalog; Complete actual catalog inspected before primary mechanism follow-up. | context_only | There is no native target gene, locus or expression dataset to resolve, and the named Sorangium producer is outside the catalog. No computational component membership was used to prove production, antibacterial activity or polymerase binding. |
| search | 420-inclusive-hits.txt; 420-fetch-results.json through 420-fetch5-results.json; Hidden- and ignored-inclusive local search plus bounded public primary/official routes. | context_only | The local search covered data, curation, conf, scripts, src, docs, .claude, reviews and reports using exact identifiers, name, full-key prefix and four patent IDs. It located the readiness queue and no exact curator override or earlier retained review in that bounded surface. Public routes included the three adopted PMIDs, original stereochemistry/synthesis follow-up, official ChEBI, NP Atlas and all four patent identifiers. Publisher main-text requests returned 403; public Figshare supplements succeeded. Reaxys was not accessed through a paid service. |
| checks | 420-focused-results.json; 420-chemistry.json; 420-xref-chemistry.json; 420-primary-stereo-map.json; Actual focused gates, independent graph and primary-drawing calculations, final captured-input hash recheck. | supports | Schema, strict validation and independent chemistry pass. The source-concept minted alias reproduces exactly. All native input hashes remain unchanged; no field or curation-history mutation was made. |

## Limits And Additional Notes

- The original 2007 discovery, 2008 stereochemistry and 2009 synthesis main articles were not obtained in full; their complete abstracts were read. The 2008 supplement was assessed only on S1–S3, and the 164-page 2009 supplement only on the stated final-product and comparison pages. No complete raw-spectral re-elucidation is claimed.
- The 2010 author-deposited full text was read only in the specified identity/endgame and final experimental sections. Its whole synthetic route was not audited. The 2012 simplified-side-chain study remained at complete-abstract depth.
- The underlying Reaxys18923823 substance page was not independently accessed. Current ChEBI supplies its provenance but does not replace exact registry verification.
- The older DE patent translation has OCR/translation limitations and an earlier structure assignment. The later original PDF table was visually checked for µg/mL and material columns; no numerical object was constructed from ambiguous OCR.
- Original patent descriptions do not by themselves demonstrate clinical efficacy, approval, a direct binding site or a uniquely causal antibacterial target. Optional mechanism curation should inspect the exact enzyme and cellular assay protocols before making stronger claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No confirmed finding or corrective action is proposed. The maintained inputs remain unchanged, and the review does not promote native SEEDED status.
- The primary stereo diagnostic compares twelve original wedge/dash assignments after removing native chiral tags. It uses native connectivity as the mapped scaffold; agreement is not presented as a fresh structure elucidation from spectra.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T155557Z-etnangien-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Etnangien: exact free-acid identity and antibacterial scope supported'
started_at: '2026-10-21T15:30:53Z'
finished_at: '2026-10-21T15:55:57Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire record
    and maintained source were read, independent chemistry calculated, asserted chemical
    groundings checked and exact-compound primary literature assessed with explicit
    access boundaries.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The native encodings and current official molfile agree on the exact etnangien
  free acid. All twelve stereocentres match an independent mapping of the original
  total-synthesis supplement drawing, and the literature distinguishes this natural
  product from its methyl ester and simplified analogues. The Gram-positive activity
  and Sorangium origin are supported. No confirmed defect was found; unavailable primary
  main texts and the inaccessible Reaxys substance record remain explicit limits.
  Scientific assessment retains the stated evidence limits; full verification is blocked
  by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/etnangien.yaml
    sha256: dff97583db1092529409c2fb3b72d6d590a925a34104fbebc0c4aa46b250cdde
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
targets:
- target_id: CHEBI:65868
  path: data/antibiotics/antibacterial/etnangien.yaml
  label: etnangien
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
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 420; one entire native record. All thirteen initial source-input
    hashes were verified before judgment and retained. Exact source-row inspection
    confirmed the existing ChEBI extractor/seeder ownership; no additional maintained
    input was needed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65868
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65868
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/etnangien.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65868
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/etnangien.yaml --out /private/tmp/am-review-session/420-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65868
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 420
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-map
  name: authority-map
  status: passed
  required: false
  summary: Native SMILES, native InChI, official ChEBI molfile and NP Atlas InChI
    independently agree on the complete key, formula, charge and twelve assigned stereocentres.
  target_ids:
  - CHEBI:65868
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/420-xref-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: primary-stereo
  name: primary-stereo
  status: passed
  required: false
  summary: The twelve wedge/dash directions transcribed from original 2009 SI page
    S48 were assigned independently on native connectivity after removing native chiral
    tags; all twelve CIP assignments agree.
  target_ids:
  - CHEBI:65868
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/420-stereo-map.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-catalog
  name: adapter-catalog
  status: passed
  required: false
  summary: The complete public catalog was inspected before mechanism follow-up. Native
    names no gene, protein or transcriptomics experiment; Sorangium is not a covered
    organism. No expression module was substituted for experimental activity or enzyme
    inhibition.
  target_ids:
  - CHEBI:65868
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:65868
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
  - CHEBI:65868
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
  - CHEBI:65868
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
  - CHEBI:65868
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
  - CHEBI:65868
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
  - CHEBI:65868
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
  - CHEBI:65868
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
  - CHEBI:65868
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
  - CHEBI:65868
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/etnangien.yaml
  locator: Entire native YAML.
  accessed_at: '2026-10-21T15:54:25Z'
  support: supports
  summary: The SEEDED, EXACT CHEBI65868 record contains one stereospecific systematic
    synonym, two broader parents, antimicrobial and antibacterial roles, the neutral
    C49H76O11 structure, one Reaxys chemical xref, four patent document xrefs, one
    ChEBI source concept and four seed/reseed events. It asserts no molecular target,
    mode, numerical assay, resistance determinant, clinical status, structured producer,
    expression dataset or causal graph. The definition names culture-broth origin
    in Sorangium cellulosum and Gram-positive activity.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py; conf/sources.yaml
  locator: Complete exact row 1340 and applicable source extraction, classification,
    citation and xref-routing logic.
  accessed_at: '2026-10-21T15:54:25Z'
  support: supports
  summary: ChEBI supplies every native scientific field and the three adopted literature
    leads. Extraction selects reviewed in-scope roles and retains citations as leads
    rather than asserting record-level experimental evidence. The seeder deliberately
    moves patent references into document_xrefs, where they do not assert exact chemical
    equivalence. No exact ARO, FDA, PubChem or MIBiG row matches the inspected source
    IDs or full key. Original input hashes and the source version 2026-08-30 were
    preserved.
  snapshot_sha256: c140bc8dd9ed4aaa55a15b661aa59384b5b6582791cac90f40956c9aece34427
- evidence_id: chebi
  kind: authority
  reference: CHEBI:65868; https://www.ebi.ac.uk/chebi/CHEBI:65868
  locator: Complete current official entry, systematic name, properties, relationships,
    registry entry and document links.
  accessed_at: '2026-10-21T15:49:11Z'
  support: supports
  summary: Current ChEBI agrees with the native neutral free acid and systematic stereochemical
    name. CHEBI25105 is the broader macrolide-antibiotic class and CHEBI35868 is hydroxy
    monocarboxylic acid; CHEBI33281 and CHEBI33282 mean antimicrobial and antibacterial
    agent. The displayed metabolite role is outside the imported antimicrobial-role
    slice and is not a required missing role. ChEBI repeats Reaxys18923823, but the
    underlying Reaxys substance page was not inspected. All four patent identifiers
    resolve as documents after using the B1 publication for EP2014655; the initially
    attempted A1 route returned 404.
  snapshot_sha256: ab46664476cb9353e9396d950c86376c8d5c7f93bf63661769e5699dbad20c4b
- evidence_id: graphs
  kind: validation
  reference: 420-xref-chemistry.json; https://www.ebi.ac.uk/chebi/backend/api/public/molfile/65868;
    https://www.npatlas.org/explore/compounds/NPA008563
  locator: Independent native and authority graph parsing; complete NP Atlas identity/revision
    page read.
  accessed_at: '2026-10-21T15:54:25Z'
  support: supports
  summary: Both native encodings, the official molfile and NP Atlas InChI reproduce
    VHPBIOVAVQXSJO-DLGDGFEOSA-N, neutral C49H76O11 and monoisotopic mass 840.538763252.
    Twelve tetrahedral centres and nine alkene geometries are assigned. NP Atlas explicitly
    links the original planar assignment to PMID17547459 and the later stereochemical
    revision to PMID18826315. Database agreement is corroboration, not a replacement
    for the original structure drawing.
  snapshot_sha256: 561db5905f864f4579234c7bcaa8889e9214b958b6f867413ac11d5988203505
- evidence_id: original-discovery
  kind: primary_source
  reference: PMID:17547459; DOI:10.1021/np070115h
  locator: Complete indexed original abstract; main article retrieval attempted but
    unavailable.
  accessed_at: '2026-10-21T15:49:11Z'
  support: supports
  summary: The original publication identifies etnangien compound 1 from Sorangium
    cellulosum strains So ce750 and So ce1045, describes a macrocyclic lactone with
    a C21 carboxylic-acid side chain and all-E hexaene, reports Gram-positive activity
    and initial bacterial/viral nucleic-acid-polymerase inhibition. This supports
    the qualitative native definition. No precise MIC, direct binding site, subunit
    assignment or whole-cell causal chain is inferred from the abstract.
  snapshot_sha256: 0311f31ed6f9e8b8acc853df933690025e7b9501d5cc890439f1f55bec8b3b3e
- evidence_id: stereochemistry
  kind: primary_source
  reference: PMID:19645468; DOI:10.1021/ja9056163; DOI:10.1021/ja9056163.s001; https://acs.figshare.com/articles/journal_contribution/Total_Synthesis_of_Etnangien/2832724
  locator: Complete original indexed abstract; official supplement pages S44–S49 read,
    S46 and S48 drawings visually inspected, complete S48–S49 comparison table read.
  accessed_at: '2026-10-21T15:51:43Z'
  support: supports
  summary: The supplement separately prepares etnangien methyl ester and then converts
    it with porcine liver esterase to etnangien. The free acid has C49H76O11, measured
    negative-ion HRMS matching its formula, positive optical rotation and an explicit
    comparison with authentic natural material. The S48 drawing has C6S, C20R, C21R,
    C22S, C24R, C28S, C35S, C36R, C37S, C38S, C39R and C40R; independent wedge/dash
    assignment matches every native centre. The seven side-chain alkenes are E and
    the macrocyclic diene is 30Z,32E, matching the native name/graph. This is a mapped
    published assignment, not an independent re-elucidation of raw spectra.
  snapshot_sha256: 774eda6db1e98a8df2ddbba5c9bf6812f835778e2bb90ded10aca901be6c6ded
- evidence_id: earlier-stereo
  kind: primary_source
  reference: PMID:18826315; DOI:10.1021/ja804194c; DOI:10.1021/ja804194c.s001
  locator: Complete indexed/publisher abstract and official supplementary pages S1–S3
    read.
  accessed_at: '2026-10-21T15:51:43Z'
  support: supports
  summary: The 2008 study assigns relative and absolute stereochemistry using NMR,
    derivatization, modeling and biosynthetic analysis. Its supplement identifies
    the more stable methyl ester as compound 2 and supplies its NMR table. These ester
    measurements are not silently treated as a direct assay of the free acid. The
    main article and the remainder of the 21-page supplement were not fully reviewed.
  snapshot_sha256: aa53a56cd09c1db26662b084f3c6cb5205730be11ff35aa51eebdd7dda780371
- evidence_id: synthesis-followup
  kind: primary_source
  reference: PMID:20334428; DOI:10.1021/jo100201f; https://www.researchgate.net/publication/42540624_Stereoselective_Total_Synthesis_of_Etnangien_and_Etnangien_Methyl_Ester
  locator: Author-deposited full text accessed through the web tool; Introduction,
    final coupling/deprotection discussion, Conclusions and final methyl-ester/free-acid
    experimental entries read.
  accessed_at: '2026-10-21T15:54:25Z'
  support: supports
  summary: The 2010 full account confirms that ester hydrolysis yields etnangien identical
    to authentic material by NMR, HRMS, chromatographic behavior and optical rotation.
    It distinguishes the labile free acid from the more stable methyl ester and describes
    translactonization/isomerization problems during synthesis. Only the stated selected
    sections were assessed; the full synthetic route and all spectra were not independently
    reconstructed.
- evidence_id: patent-activity
  kind: primary_source
  reference: patent:EP2014655; EP2014655B1; https://patents.google.com/patent/EP2014655B1/en
  locator: Complete description and examples read; original PDF pages 3 and 7 visually
    inspected, including full Table 2 and units.
  accessed_at: '2026-10-21T15:51:23Z'
  support: supports
  summary: Formula I distinguishes etnangien acid 1 with R=H from ester 2. Table 2
    reports separate acid/ester MIC columns. The acid column includes S. aureus 1.0
    µg/mL, a rifampicin-resistant S. aureus isolate 0.62 µg/mL, C. glutamicum DSM20300
    0.03 µg/mL and M. luteus 0.06 µg/mL. Testing uses serial dilution with the reported
    peptone/meat-extract/yeast-extract growth medium at pH7; detailed standardized
    clinical breakpoints are not supplied. The PDF glyph is µg/mL despite text extraction
    rendering mg/mL. This independently supports bacterial activity, without transferring
    the methyl-ester values, proving clinical efficacy or assigning a resistance mechanism.
  snapshot_sha256: 282fe5565ee6e164c67eeebefcb8ca4ba9d38c6e8e2eff6d41b33dfab934aa69
- evidence_id: patent-scope
  kind: primary_source
  reference: patent:DE19630980; patent:WO2008142046; patent:EP2247740; https://patents.google.com/patent/DE19630980A1/en;
    https://patents.google.com/patent/WO2008142046A1/en; https://patents.google.com/patent/EP2247740A1/en
  locator: DE19630980 description read in the supplied English translation; WO2008142046
    identity, isolation and activity sections; EP2247740 description and experimental
    examples.
  accessed_at: '2026-10-21T15:49:12Z'
  support: supports
  summary: The early DE document reports production by So ce750/DSM11028 and an older
    structural assignment. The later derivative patents explicitly discuss a corrected
    C38 hydroxyl assignment and distinguish acid from ester. EP2247740 concerns biosynthetic
    coding sequences and production experiments in Sorangium, not an antimicrobial
    target. These documents are scientifically relevant historical/production references;
    native correctly treats them as document_xrefs rather than chemical equivalents.
    Proposed pharmaceutical use in a patent is not regulatory approval. Sequence listings
    and all patent figures were not reanalysed.
  snapshot_sha256: 8738bd3d539a058225ede7fe364c3df4b355e5dfdf9237d42066250cc973f8a2
- evidence_id: mechanism-scope
  kind: primary_source
  reference: EP2014655B1 examples 3–4; PMID:17547459
  locator: Original patent assay description and discovery abstract.
  accessed_at: '2026-10-21T15:49:53Z'
  support: supports
  summary: The patent describes biochemical inhibition assays for E. coli RNA polymerase,
    E. coli DNA polymerase and retroviral reverse transcriptases, while whole E. coli
    cells remain poorly susceptible under its reported conditions. The text explicitly
    presents RNA-polymerase mediation of antibacterial activity as an assumption.
    Enzyme inhibition is a defensible follow-up lead, but it does not establish a
    specific subunit-binding site or a unique whole-cell mechanism. No such target
    is currently asserted in native. Biosynthetic Etn proteins are separate from antimicrobial
    targets.
  snapshot_sha256: 5486270795605f0a0aa6b32379d71affd31313d8cd1af3d46ad3ad44d140f406
- evidence_id: adopted-leads
  kind: database
  reference: PMID:17547459; PMID:19645468; PMID:22832317
  locator: All three adopted bibliographic records and complete indexed abstracts.
  accessed_at: '2026-10-21T15:49:11Z'
  support: context_only
  summary: 'PMID17547459 is the original isolation/activity paper; PMID19645468 is
    the total synthesis with publicly retrieved supplementary identity evidence; PMID22832317,
    DOI10.1016/j.bmcl.2012.06.070, tests designed simplified side chains and is an
    analogue study rather than standalone exact-parent assay proof. The latter full
    paper was not obtained: the advertised author-repository URL returned a DSpace
    application shell through curl, not a PDF. Additional biosynthetic and gladiolin
    search hits were treated as context and were not transferred to native etnangien
    claims.'
  snapshot_sha256: 0311f31ed6f9e8b8acc853df933690025e7b9501d5cc890439f1f55bec8b3b3e
- evidence_id: adapter
  kind: database
  reference: iModulonDB public dataset catalog
  locator: Complete actual catalog inspected before primary mechanism follow-up.
  accessed_at: '2026-10-21T15:54:25Z'
  support: context_only
  summary: There is no native target gene, locus or expression dataset to resolve,
    and the named Sorangium producer is outside the catalog. No computational component
    membership was used to prove production, antibacterial activity or polymerase
    binding.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: 420-inclusive-hits.txt; 420-fetch-results.json through 420-fetch5-results.json
  locator: Hidden- and ignored-inclusive local search plus bounded public primary/official
    routes.
  accessed_at: '2026-10-21T15:54:25Z'
  support: context_only
  summary: The local search covered data, curation, conf, scripts, src, docs, .claude,
    reviews and reports using exact identifiers, name, full-key prefix and four patent
    IDs. It located the readiness queue and no exact curator override or earlier retained
    review in that bounded surface. Public routes included the three adopted PMIDs,
    original stereochemistry/synthesis follow-up, official ChEBI, NP Atlas and all
    four patent identifiers. Publisher main-text requests returned 403; public Figshare
    supplements succeeded. Reaxys was not accessed through a paid service.
  search_scope: '2026-10-21: rg --no-ignore --hidden for CHEBI:65868, etnangien, VHPBIOVAVQXSJO,
    DE19630980, EP2014655, EP2247740 and WO2008142046 across the stated paths. Europe
    PMC query combined the three adopted PMID identifiers with TITLE_ABS:etnangien.
    Focused web queries used exact etnangien DOI/title combinations and author-repository
    routes; no search snippet was used as experimental proof.'
  snapshot_sha256: 39550979fc0c2bc027b283bd69cf215818b438ef2376b8833471041cd208c079
- evidence_id: checks
  kind: validation
  reference: 420-focused-results.json; 420-chemistry.json; 420-xref-chemistry.json;
    420-primary-stereo-map.json
  locator: Actual focused gates, independent graph and primary-drawing calculations,
    final captured-input hash recheck.
  accessed_at: '2026-10-21T15:54:25Z'
  support: supports
  summary: Schema, strict validation and independent chemistry pass. The source-concept
    minted alias reproduces exactly. All native input hashes remain unchanged; no
    field or curation-history mutation was made.
  snapshot_sha256: 67bda2c44f420adb361ce4609e48d91aa3ee8d2c24a86f2a4649dc8ef0bea06e
assessments:
- assessment_id: identity
  area: identity
  topic: Exact natural free acid, stereochemistry and names
  outcome: supported
  summary: The graph, systematic name, official structure and original mapped total-synthesis
    drawing agree. The free acid is distinct from the methyl ester, truncated analogues
    and the older patent assignment.
  target_ids:
  - CHEBI:65868
  evidence_ids:
  - native
  - chebi
  - graphs
  - stereochemistry
  - earlier-stereo
  - synthesis-followup
- assessment_id: activity
  area: evidence
  topic: Antibacterial classification and Gram-positive definition
  outcome: supported
  summary: The exact-parent discovery abstract and separately identified acid column
    in original patent Table2 support the native class and roles. The assay values
    remain strain/material-specific and are not clinical breakpoints.
  target_ids:
  - CHEBI:65868
  evidence_ids:
  - original-discovery
  - patent-activity
  - chebi
- assessment_id: producer
  area: evidence
  topic: Sorangium culture-broth origin
  outcome: supported
  summary: Original isolation names So ce750 and So ce1045; the patents provide fermentation/isolation
    context. These support the qualitative native producer statement. Synthetic ester
    formation and heterologous biosynthetic examples are not substituted for natural
    acid production.
  target_ids:
  - CHEBI:65868
  evidence_ids:
  - original-discovery
  - patent-scope
  - patent-activity
- assessment_id: documents
  area: provenance
  topic: Chemical xref versus document scope
  outcome: unknown
  summary: The four patent references are relevant documents and are correctly separated
    from chemical equivalence. Reaxys18923823 is reproduced by current ChEBI but its
    underlying exact substance record remains unverified at this free-source depth.
  target_ids:
  - CHEBI:65868
  evidence_ids:
  - chebi
  - owners
  - patent-scope
- assessment_id: mechanism
  area: completeness
  topic: Optional mechanism, targets and other biology
  outcome: supported
  summary: Primary leads support polymerase-inhibition follow-up, but the SEEDED record
    makes no unsupported specific binding or whole-cell causal assertion. Optional
    mode, target, activity, producer, dataset and graph enrichment is not a confirmed
    defect. No REVIEWED promotion is implied.
  target_ids:
  - CHEBI:65868
  evidence_ids:
  - native
  - mechanism-scope
  - adopted-leads
  - adapter
- assessment_id: audit
  area: provenance
  topic: Source ownership, citation disposition and history
  outcome: supported
  summary: Every native field and all three adopted leads were assessed. The four
    source events and current SEEDED status are preserved. The maintained extractor
    keeps citations as leads, so absence of record-level copied references is intentional
    rather than a lost-evidence defect.
  target_ids:
  - CHEBI:65868
  evidence_ids:
  - owners
  - native
  - adopted-leads
  - search
  - checks
findings: []
actions: []
limitations:
- The original 2007 discovery, 2008 stereochemistry and 2009 synthesis main articles
  were not obtained in full; their complete abstracts were read. The 2008 supplement
  was assessed only on S1–S3, and the 164-page 2009 supplement only on the stated
  final-product and comparison pages. No complete raw-spectral re-elucidation is claimed.
- The 2010 author-deposited full text was read only in the specified identity/endgame
  and final experimental sections. Its whole synthetic route was not audited. The
  2012 simplified-side-chain study remained at complete-abstract depth.
- The underlying Reaxys18923823 substance page was not independently accessed. Current
  ChEBI supplies its provenance but does not replace exact registry verification.
- The older DE patent translation has OCR/translation limitations and an earlier structure
  assignment. The later original PDF table was visually checked for µg/mL and material
  columns; no numerical object was constructed from ambiguous OCR.
- Original patent descriptions do not by themselves demonstrate clinical efficacy,
  approval, a direct binding site or a uniquely causal antibacterial target. Optional
  mechanism curation should inspect the exact enzyme and cellular assay protocols
  before making stronger claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No confirmed finding or corrective action is proposed. The maintained inputs remain
  unchanged, and the review does not promote native SEEDED status.
- The primary stereo diagnostic compares twelve original wedge/dash assignments after
  removing native chiral tags. It uses native connectivity as the mapped scaffold;
  agreement is not presented as a fresh structure elucidation from spectra.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
