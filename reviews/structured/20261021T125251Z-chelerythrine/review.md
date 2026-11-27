# Chelerythrine: supported cation identity and antibacterial role with an obsolete duplicate KNApSAcK reference

- Review: 20261021T125251Z-chelerythrine
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:36:37Z
- Finished UTC: 2026-10-21T12:52:51Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native record consistently represents the isolated +1 chelerythrine cation, distinct from a chloride salt, reduced analogues and pseudobases. Public chemical graphs, including the official archived LINCS entry, agree. Primary isolation and antimicrobial experiments support the antibacterial role and plant-source context. One minor source-maintenance finding concerns an explicitly obsolete duplicate KNApSAcK identifier. MetaCyc and Reaxys could not be independently checked at exact structure depth. No missing optional mechanism or activity field is treated as a defect, and host-cell kinase, ROS and anti-inflammatory results are not transferred to antibacterial mechanism.

## Scope And Provenance

Entire native YAML: definition, two exact chemical synonyms, both broader chemical parents, antibacterial role, all chemical descriptors, eight chemical xrefs, document xref, sole ChEBI source concept and all four history events. Complete adopted ChEBI row and all eight source citation leads were read, with focused full-primary follow-up.

Selection: Queue 286. The initial thirteen captured inputs are the actual ChEBI-only owners/context; their hashes are preserved. Inspection confirmed no ARO, PubChem-enrichment, FDA or producer inventory row owns this record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:78373 | data/antibiotics/antibacterial/chelerythrine.yaml | generated | chelerythrine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:78373 | No schema issues found. |
| strict | passed | True | CHEBI:78373 | One record scanned; zero strict errors. |
| chemistry | passed | False | CHEBI:78373 | Both native encodings, element counts, separate +1 charge, masses and stable mint agree. The helper correctly compares elemental formula separately from RDKit charge notation. |
| external-structures | passed | False | CHEBI:78373 | Independent official KEGG, PubChem CAS mapping, KNApSAcK/historical PCIDB, CCD and archived LINCS encodings agree on the native full key. |
| Initial generic formula comparison | failed | False | CHEBI:78373 | The generic helper compared C21H18NO4+ with the native elemental formula C21H18NO4 despite native charge +1, causing a false failure. Initial output is retained; the charge-aware comparison above passes without changing any record. |
| Authoritative full QC | failed | True | CHEBI:78373 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:78373 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:78373 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:78373 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:78373 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:78373 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:78373 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:78373 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:78373 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact chelerythrine cation and names

identity: supported. Targets: CHEBI:78373.

Native structure, cation/alkaloid parents and systematic names are coherent. Accessible public graphs agree, including official normalized LINCS1187. Counterions, pseudobases and reduced analogues remain separate. MetaCyc/Reaxys exact structure verification is limited.

### Plant-source wording

evidence: supported. Targets: CHEBI:78373.

ChEBI directly supports the definition, and primary root-bark isolation from Z. simulans plus chromatographic confirmation in C. majus support the two named species. KNApSAcK supports broader plant occurrence as database context; no complete family-wide primary isolation audit or biosynthetic pathway is claimed.

### Antibacterial role and exact study material

scope: supported. Targets: CHEBI:78373.

The original 2014 compound 10 drawing and experiments support antibacterial activity of the named cation. Its bulk counterion is not fully characterized in the accessed report, so quantitative material scope must remain explicit. Taxon and assay reporting inconsistencies limit later numerical enrichment, not the native general role.

### All eight source PMID dispositions

evidence: supported. Targets: CHEBI:78373.

Every adopted PMID resolves and its complete abstract was read. The extraction logic intentionally keeps them as leads. One directly tests antibacterial activity; the other seven concern analytical chemistry, parasites, host-cell effects or synthetic DNA. No claim-level evidence was fabricated by seeding their citation list.

### Mechanism and activity detail

completeness: unknown. Targets: CHEBI:78373.

Optional activity/producer/target enrichment is possible after handling material and source inconsistencies. The inspected work does not justify transferring host PKC or mitochondrial ROS effects to bacteria. No requirement forces a target or causal graph onto this identity/role seed.

### Retired KNApSAcK duplicate

ownership: concern. Targets: CHEBI:78373.

C00024660 is explicitly old at its provider and its direct record no longer resolves; the active C00024634 and historical exact identity are both established. A narrow maintained-source cleanup is warranted without changing the native molecular structure.

## Findings

### F1: Retire the obsolete duplicate KNApSAcK cross-reference

minor / open / confirmed; issue key: chelerythrine-obsolete-knapsack-c00024660.

xrefs[3] retains KNApSAcK C00024660. The provider direct entry rejects it and its official Twins index labels it old. Historical PCIDB metadata maps it to the same exact cation, while native xrefs[2] C00024634 already resolves to the active exact entry. Normalize the obsolete reference through the maintained source path; preserve historical provenance if required. This is not evidence of a wrong chelerythrine structure.

## Recommended Actions And Acceptance Checks

### A1

Normalize the obsolete KNApSAcK identifier without altering chelerythrine identity.

- Confirm the provider retirement and retain C00024634 as the active exact chemical entry. Remove or qualify C00024660 through a maintained upstream mapping/filter so regeneration does not restore it as an active link.
- Preserve historical evidence of the old identifier if the repository policy retains retired mappings; do not relabel it as a different chemical structure.
- Rerun extraction/seeding through the owning path, focused schema/strict checks and exact structure validation, plus applicable corpus gates.

### A2

If enriching optional primary evidence, retain exact material, assay and biological scope.

- Use original PMID 24824737 compound 10 and preserve MIC versus MBC, strains, medium, inoculum and incubation. Reconcile the S. aureus strain discrepancy and B. subtilis MBC discrepancy before adding those exact observations.
- Do not transfer extract/mixture potency, reduced-analogue results, chloride bulk mass conventions or host-cell kinase/ROS responses into unqualified cation-specific antibacterial claims.
- Keep synthetic-DNA binding and nonbacteriolytic OD behavior separate from a demonstrated whole-cell molecular target. Absence of an established target in the inspected sources does not establish universal absence of a mechanism.
- Resolve MetaCyc/Reaxys structures when freely available before claiming every external identity independently verified; no paid access is necessary for the bounded current review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/chelerythrine.yaml; Entire YAML, all source and history entries. | supports | SEEDED, EXACT and ANTIBACTERIAL. Formula C21H18NO4, separate charge +1, one molecular component, key LLEJIEBFSOEYIV-UHFFFAOYSA-N. The record asserts no molecular target, mode, resistance determinant, transcriptomic dataset, clinical status, causal graph or numeric activity observation. Optional absence is not automatically a defect. |
| source | data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Entire row 2012; ChEBI extraction, role filtering, build_concepts, resolve_identity and record assembly/xref classification. | supports | The three-star CHEBI:78373 row is the sole source. Definition, two nonlabel synonyms, two chemical parents, antibacterial role and all xrefs are faithfully emitted. Eight source PMIDs are deliberately retained as curator leads rather than automatically attached as antimicrobial evidence. Wikipedia is intentionally placed in document_xrefs. No relevant mechanism_role_ids are present in the adopted row. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:78373; https://www.ebi.ac.uk/chebi/CHEBI:25697; https://www.ebi.ac.uk/chebi/CHEBI:38517; https://www.ebi.ac.uk/chebi/CHEBI:33282; Complete molecule entry and relevant parent/role definitions and outgoing relationships. | supports | Current ChEBI reproduces the exact cation structure, formula, charge, masses, names and plant-source definition. CHEBI:25697 is organic cation; CHEBI:38517 is benzophenanthridine alkaloid; CHEBI:33282 is antibacterial agent, whose definition allows an active part of a substance. External PKC-inhibitor and antineoplastic roles are not native antibacterial target claims. Both exact synonyms name the charged phenanthridinium skeleton. |
| chemical-identifiers | https://rest.kegg.jp/get/C12227; https://www.knapsackfamily.com/knapsack_core/information.php?word=C00024634; https://files.rcsb.org/ligands/download/CTI.cif; https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/34316-15-9/property/InChI,InChIKey,MolecularFormula,SMILES/JSON; Complete official chemical responses and independent molecular parses. | supports | KEGG C12227, active KNApSAcK C00024634, PDB CCD CTI and the CAS 34316-15-9 PubChem mapping all resolve to the exact native +1 cation and full key. CCD CTI is a chemical component identifier; its occurrence in a protein structure does not itself establish an antibacterial target. Paid CAS registry access was not used. |
| lincs | https://lincs.hms.harvard.edu/_static/db/prod-20200624/small_molecules.sdf; Official 2020-06-24 snapshot, exact LSM-1187/HMSL10186 entry; independently parsed SMILES and InChI. | supports | The archived LINCS chemical entry explicitly stores chelerythrine cation, PubChem 2703, formula C21H18NO4 and native key LLEJIEBFSOEYIV-UHFFFAOYSA-N. Its salt_id 102 and a chloride reagent label in a published screen do not negate the explicitly normalized stored cation graph. No salt-mismatch finding is warranted. The former detail URL serves a public archive index, from which this exact entry was obtained. |
| retired-knapsack | https://www.knapsackfamily.com/knapsack_core/information.php?word=C00024660; https://www.knapsackfamily.com/Twins/top.php?kword=C00032434&amp;mode=list1&amp;sword=50; https://www.genome.jp/db/pcidb/kna_cpds/24660; Official entry response and Twins table row; historical PCIDB entry identity fields. | partial | The direct C00024660 entry rejects the identifier, and the official Twins index explicitly marks it as old. PCIDB preserves its historical chelerythrine cation InChI, independently matching native. Thus this is an obsolete duplicate reference rather than a wrong chemical identity. Native C00024634 already provides the active exact entry. |
| restricted-identifiers | MetaCyc CPD-16782; Reaxys 3915260; wikipedia.en:Chelerythrine; Current ChEBI attribution, attempted official MetaCyc page and getxml endpoint, and resolved Wikipedia document. | partial | MetaCyc page and structured endpoint both returned an account requirement, not compound text. Reaxys was not consulted behind paid access. Their identifiers are currently attested by ChEBI but exact external structures remain unverified. Wikipedia resolves as the intended topical document and correctly occupies document_xrefs; its narrative is not primary scientific evidence. |
| plant-simulans | DOI:10.1016/S0031-9422(00)90870-7; https://www.sciencedirect.com/science/article/pii/S0031942200908707; Complete original publisher abstract exposed in indexed result; direct publisher page returned 403. | supports | The 1993 original Alkaloids from Zanthoxylum simulans reports chelerythrine among the compounds isolated and spectrally characterized from root bark. This supports the corresponding part of the native plant-source definition, without claiming full original experimental or spectral inspection. |
| plant-majus | PMID:31336994; DOI:10.3390/toxins11070406; https://pmc.ncbi.nlm.nih.gov/articles/PMC6669454/; Original full XML: plant materials, chromatographic identification/standards Methods and relevant root/aerial-part Results; activity discussion inspected as context. | supports | The study detects chelerythrine in C. majus root and aerial-part extracts using retention time and DAD spectrum comparison with standards, with collected fractions checked by mass spectrometry. This supports plant occurrence rather than an invented biosynthetic pathway. Individually tested chelerythrine was a purchased standard of at least 90 percent purity, so its antibacterial assay is not automatically a purified isolate from those plants. Mixture tests remain separate. |
| antibacterial-primary | PMID:24824737; DOI:10.1371/journal.pone.0097000; https://pmc.ncbi.nlm.nih.gov/articles/PMC4019524/; Full main narrative, Methods and Tables 1–3; Figure 1 and Tables 2/3 visually inspected. | supports | Exact chelerythrine is compound 10, drawn as the quaternary cation and distinguished from reduced/oxygenated analogues. It was isolated as 120 mg crystals from Z. rhoifolium stem bark and identified using authentic TLC comparison and reported NMR data. Table 2 reports MIC 1.5 micrograms/mL for six tested bacteria, with distinct MBCs. Broth microdilution uses 1e5 CFU/mL, casein soy broth and 24 h at 37 C for bacteria; subculture assesses bactericidal activity. This directly supports the role without requiring a chloride counterion to be added to the native active-moiety graph. |
| assay-boundaries | PMID:24824737, Methods, Tables 2/3 and Results/Discussion; Same inspected original main text and table images. | context_only | The Methods list S. aureus ATCC 25923 while the tables identify ATCC 6538. B. subtilis MBC is 50 micrograms/mL in Table 2 but 6.25 in Table 3; MIC is 1.5 in both. The abstract blanket statement should not replace the different organism-specific values in Table 3. Optical-density kinetics merely suggest a nonbacteriolytic effect; they do not prove a molecular target. Erythrocyte TBARS/AOPP and hemolysis are host-cell endpoints, not microbial ROS or universal safety. No disputed numeric value is asserted in the native seed. |
| adopted-antibacterial | PMID:24824737; DOI:10.1371/journal.pone.0097000; Complete original indexed abstract followed by original full-main-text review above. | supports | This is the one adopted paper directly testing exact chelerythrine antibacterial activity. Keep organism, material, endpoint and source inconsistencies explicit; the other seven leads are not equivalent antibacterial evidence. |
| adopted-analysis | PMID:23390024; DOI:10.1093/chromsci/bmt003; Complete original indexed abstract. | context_only | HPLC fluorescence method for chelerythrine/nitidine in Z. nitidum. Supports analytical and that plant context, not the different Z. simulans source assertion or an antimicrobial mechanism. |
| adopted-parasite | PMID:24295957; DOI:10.1016/j.vetpar.2013.10.021; Complete original indexed abstract. | context_only | Isolated chelerythrine and chloroxylonine from Toddalia asiatica tested against the fish ciliate Ichthyophthirius multifiliis. This is exact-compound antiparasitic context with a separate fish-toxicity endpoint, not a bacterial MIC or evidence for the named native plants. |
| adopted-host | PMID:23900672; DOI:10.1007/s13277-013-1016-4; PMID:24300194; DOI:10.1016/j.cbi.2013.11.011; PMID:24928629; DOI:10.1007/s10753-014-9929-7; PMID:24948079; DOI:10.1016/j.pharep.2014.03.013; Complete original indexed abstracts for all four primary studies. | context_only | 23900672 concerns mitochondrial ROS and apoptosis in murine lymphoma cells. 24300194 concerns ethanol-induced gastric injury and inflammatory responses in mice. 24928629 concerns LPS-induced endotoxic shock and host cytokine/NF-kappaB responses, not clearance of live bacteria. 24948079 evaluates mania-like behavior in mice. None establishes an antibacterial PKC target, microbial ROS mechanism or clinical approval. |
| adopted-DNA | PMID:25010289; DOI:10.1016/j.jphotobiol.2014.06.005; Complete original indexed abstract. | context_only | Spectroscopy and calorimetry establish interaction with synthetic sequence-defined polynucleotides, including intercalative behavior. This is direct biophysical binding context but not proof that bacterial DNA engagement explains whole-cell killing. No bacterial taxon-specific target or causal chain follows from these experiments alone. |
| search | 286-inclusive-hits.txt; bounded exact-name/identifier and plant-source searches; Hidden and ignored files included. Official identifiers and original literature at documented depth. | context_only | Exact local hits comprise native record, ChEBI row, readiness queue, PATHS and generated embeddings; no matching curator decision/overlay was found in the stated scope. No record-native gene, protein, regulator, pathway, stress response or transcriptomic dataset triggers the structured adapter. A chemical LINCS identifier is not itself a native transcriptomic dataset assertion. External host-cell literature was not promoted to native target claims. |
| validation | 286-schema.log; 286-strict.log; 286-strict.tsv; 286-chemistry-initial.json; 286-chemistry.json; 286-xref-chemistry.json; Actual focused outputs and native/external independent molecular parses. | supports | Schema and strict exit 0. Initial generic chemistry helper exit 1 reflected only RDKit appended-charge formula notation; the corrected scratch helper compares elemental formula separately and verifies charge +1, key, masses and mint, exiting 0. External representations agree. An initial external helper incorrectly treated the CCD InChIKey metadata line as SMILES; its failed log is retained as 286-xref-check-initial.log, and descriptor selection was corrected without modifying any chemical input. No native input was changed to obtain these passes. |

## Limits And Additional Notes

- MetaCyc CPD-16782 returned an account requirement from both page and structured endpoint; Reaxys 3915260 was not inspected behind paid access. They are attested by ChEBI, not independently verified at exact graph depth.
- The original 1993 Z. simulans isolation paper was accessible at complete publisher-abstract depth only. C. majus occurrence was checked in the original 2019 relevant methods/results; a full primary audit of every Papaveraceae occurrence was not attempted.
- All eight adopted abstracts were read; PMID 24824737 received full main-text and selected visual follow-up. The seven other adopted papers were not inspected as complete articles and are not used to establish an antibacterial target.
- The 2014 primary paper inconsistently reports S. aureus strains and B. subtilis MBC values, and does not fully specify the bulk counterion of isolated compound 10. Figure 1 and Tables 2/3 were visually checked, but complete original spectra and additional images were not independently reanalyzed.
- The native record has no structured-adapter trigger. No external expression-module membership, host-cell response, protein-bound CCD occurrence or chemical-library membership is treated as antimicrobial causal proof.
- Scientific completion remains partial. No paid access, external contact or provider-credit research was used. Deterministic validation does not constitute native REVIEWED sign-off.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Root read the entire native record and scientific draft, verified thirteen captured hashes, checked explicit provider retirement and visually inspected original compound10 Figure1 before ordered persistence.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T125251Z-chelerythrine
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Chelerythrine: supported cation identity and antibacterial role with an obsolete
  duplicate KNApSAcK reference'
started_at: '2026-10-21T12:36:37Z'
finished_at: '2026-10-21T12:52:51Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author this seed. Independently read the whole native
    record, actual ChEBI row, source selection and emission logic, official chemical
    identities and all eight adopted literature abstracts. Original primary antibacterial
    evidence was inspected in full main text and selected images. Initial provenance
    capture preceded judgment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The native record consistently represents the isolated +1 chelerythrine cation,
  distinct from a chloride salt, reduced analogues and pseudobases. Public chemical
  graphs, including the official archived LINCS entry, agree. Primary isolation and
  antimicrobial experiments support the antibacterial role and plant-source context.
  One minor source-maintenance finding concerns an explicitly obsolete duplicate KNApSAcK
  identifier. MetaCyc and Reaxys could not be independently checked at exact structure
  depth. No missing optional mechanism or activity field is treated as a defect, and
  host-cell kinase, ROS and anti-inflammatory results are not transferred to antibacterial
  mechanism.
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
  - path: data/antibiotics/antibacterial/chelerythrine.yaml
    sha256: 75e8dd21a3c03007983e3841b8f795693547481ca4f73f3c6d834e36959c79ef
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
- target_id: CHEBI:78373
  path: data/antibiotics/antibacterial/chelerythrine.yaml
  label: chelerythrine
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
  description: 'Entire native YAML: definition, two exact chemical synonyms, both
    broader chemical parents, antibacterial role, all chemical descriptors, eight
    chemical xrefs, document xref, sole ChEBI source concept and all four history
    events. Complete adopted ChEBI row and all eight source citation leads were read,
    with focused full-primary follow-up.'
  selection: Queue 286. The initial thirteen captured inputs are the actual ChEBI-only
    owners/context; their hashes are preserved. Inspection confirmed no ARO, PubChem-enrichment,
    FDA or producer inventory row owns this record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:78373
  exclusions:
  - target: Chelerythrine chloride, dihydrochelerythrine, hydroxydihydro derivatives
      and plant mixtures
    reason: Bulk salt, adjacent chemical structures and mixtures are distinct from
      the selected cation. Reported experimental material is preserved rather than
      silently collapsed.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: No schema issues found.
  target_ids:
  - CHEBI:78373
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/chelerythrine.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: One record scanned; zero strict errors.
  target_ids:
  - CHEBI:78373
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/chelerythrine.yaml --out /private/tmp/am-review-session/286-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Both native encodings, element counts, separate +1 charge, masses and stable
    mint agree. The helper correctly compares elemental formula separately from RDKit
    charge notation.
  target_ids:
  - CHEBI:78373
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/286-chemistry-check.py 286
  exit_code: 0
  expected_exit_code: 0
- check_id: external-structures
  name: external-structures
  status: passed
  required: false
  summary: Independent official KEGG, PubChem CAS mapping, KNApSAcK/historical PCIDB,
    CCD and archived LINCS encodings agree on the native full key.
  target_ids:
  - CHEBI:78373
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/286-xref-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: initial-chemistry-helper
  name: Initial generic formula comparison
  status: failed
  required: false
  summary: The generic helper compared C21H18NO4+ with the native elemental formula
    C21H18NO4 despite native charge +1, causing a false failure. Initial output is
    retained; the charge-aware comparison above passes without changing any record.
  target_ids:
  - CHEBI:78373
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 286
  exit_code: 1
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
  - CHEBI:78373
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
  - CHEBI:78373
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
  - CHEBI:78373
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
  - CHEBI:78373
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
  - CHEBI:78373
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
  - CHEBI:78373
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
  - CHEBI:78373
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
  - CHEBI:78373
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
  - CHEBI:78373
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/chelerythrine.yaml
  locator: Entire YAML, all source and history entries.
  accessed_at: '2026-10-21T12:52:08Z'
  support: supports
  summary: SEEDED, EXACT and ANTIBACTERIAL. Formula C21H18NO4, separate charge +1,
    one molecular component, key LLEJIEBFSOEYIV-UHFFFAOYSA-N. The record asserts no
    molecular target, mode, resistance determinant, transcriptomic dataset, clinical
    status, causal graph or numeric activity observation. Optional absence is not
    automatically a defect.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Entire row 2012; ChEBI extraction, role filtering, build_concepts, resolve_identity
    and record assembly/xref classification.
  accessed_at: '2026-10-21T12:52:08Z'
  support: supports
  summary: The three-star CHEBI:78373 row is the sole source. Definition, two nonlabel
    synonyms, two chemical parents, antibacterial role and all xrefs are faithfully
    emitted. Eight source PMIDs are deliberately retained as curator leads rather
    than automatically attached as antimicrobial evidence. Wikipedia is intentionally
    placed in document_xrefs. No relevant mechanism_role_ids are present in the adopted
    row.
  snapshot_sha256: d6cc5204d7df8e27f0d37e5858eb32500a1aefa34fc650f10aeeaff05b60a036
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:78373; https://www.ebi.ac.uk/chebi/CHEBI:25697;
    https://www.ebi.ac.uk/chebi/CHEBI:38517; https://www.ebi.ac.uk/chebi/CHEBI:33282
  locator: Complete molecule entry and relevant parent/role definitions and outgoing
    relationships.
  accessed_at: '2026-10-21T12:46:32Z'
  support: supports
  summary: Current ChEBI reproduces the exact cation structure, formula, charge, masses,
    names and plant-source definition. CHEBI:25697 is organic cation; CHEBI:38517
    is benzophenanthridine alkaloid; CHEBI:33282 is antibacterial agent, whose definition
    allows an active part of a substance. External PKC-inhibitor and antineoplastic
    roles are not native antibacterial target claims. Both exact synonyms name the
    charged phenanthridinium skeleton.
  snapshot_sha256: 96d2874e46b61859069ea81404ece5f5d12425461c72702b42a16ceb77529619
- evidence_id: chemical-identifiers
  kind: database
  reference: https://rest.kegg.jp/get/C12227; https://www.knapsackfamily.com/knapsack_core/information.php?word=C00024634;
    https://files.rcsb.org/ligands/download/CTI.cif; https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/34316-15-9/property/InChI,InChIKey,MolecularFormula,SMILES/JSON
  locator: Complete official chemical responses and independent molecular parses.
  accessed_at: '2026-10-21T12:52:08Z'
  support: supports
  summary: KEGG C12227, active KNApSAcK C00024634, PDB CCD CTI and the CAS 34316-15-9
    PubChem mapping all resolve to the exact native +1 cation and full key. CCD CTI
    is a chemical component identifier; its occurrence in a protein structure does
    not itself establish an antibacterial target. Paid CAS registry access was not
    used.
  snapshot_sha256: d9351a7242c750c5db87fbd27c0c0b9bebdd7c1129cf60cf8f8a99e338f8c2c9
- evidence_id: lincs
  kind: database
  reference: https://lincs.hms.harvard.edu/_static/db/prod-20200624/small_molecules.sdf
  locator: Official 2020-06-24 snapshot, exact LSM-1187/HMSL10186 entry; independently
    parsed SMILES and InChI.
  accessed_at: '2026-10-21T12:48:24Z'
  support: supports
  summary: The archived LINCS chemical entry explicitly stores chelerythrine cation,
    PubChem 2703, formula C21H18NO4 and native key LLEJIEBFSOEYIV-UHFFFAOYSA-N. Its
    salt_id 102 and a chloride reagent label in a published screen do not negate the
    explicitly normalized stored cation graph. No salt-mismatch finding is warranted.
    The former detail URL serves a public archive index, from which this exact entry
    was obtained.
  snapshot_sha256: 4af9ec0b0b10272b8ff4a929d8f25f75bf68611c73b2e25bc74e750156d87274
- evidence_id: retired-knapsack
  kind: database
  reference: https://www.knapsackfamily.com/knapsack_core/information.php?word=C00024660;
    https://www.knapsackfamily.com/Twins/top.php?kword=C00032434&mode=list1&sword=50;
    https://www.genome.jp/db/pcidb/kna_cpds/24660
  locator: Official entry response and Twins table row; historical PCIDB entry identity
    fields.
  accessed_at: '2026-10-21T12:47:39Z'
  support: partial
  summary: The direct C00024660 entry rejects the identifier, and the official Twins
    index explicitly marks it as old. PCIDB preserves its historical chelerythrine
    cation InChI, independently matching native. Thus this is an obsolete duplicate
    reference rather than a wrong chemical identity. Native C00024634 already provides
    the active exact entry.
  snapshot_sha256: 507a6e68dd097e6d17a4b8a43af714aa52333f29603f1e9f0f5ec992d6948f63
- evidence_id: restricted-identifiers
  kind: database
  reference: MetaCyc CPD-16782; Reaxys 3915260; wikipedia.en:Chelerythrine
  locator: Current ChEBI attribution, attempted official MetaCyc page and getxml endpoint,
    and resolved Wikipedia document.
  accessed_at: '2026-10-21T12:46:34Z'
  support: partial
  summary: MetaCyc page and structured endpoint both returned an account requirement,
    not compound text. Reaxys was not consulted behind paid access. Their identifiers
    are currently attested by ChEBI but exact external structures remain unverified.
    Wikipedia resolves as the intended topical document and correctly occupies document_xrefs;
    its narrative is not primary scientific evidence.
  snapshot_sha256: 24b2a5abdd8d3058fe1e7712b8b3184785d0d2e8b86ff8784e1e511f2bda41da
- evidence_id: plant-simulans
  kind: primary_source
  reference: DOI:10.1016/S0031-9422(00)90870-7; https://www.sciencedirect.com/science/article/pii/S0031942200908707
  locator: Complete original publisher abstract exposed in indexed result; direct
    publisher page returned 403.
  accessed_at: '2026-10-21T12:52:08Z'
  support: supports
  summary: The 1993 original Alkaloids from Zanthoxylum simulans reports chelerythrine
    among the compounds isolated and spectrally characterized from root bark. This
    supports the corresponding part of the native plant-source definition, without
    claiming full original experimental or spectral inspection.
- evidence_id: plant-majus
  kind: primary_source
  reference: PMID:31336994; DOI:10.3390/toxins11070406; https://pmc.ncbi.nlm.nih.gov/articles/PMC6669454/
  locator: 'Original full XML: plant materials, chromatographic identification/standards
    Methods and relevant root/aerial-part Results; activity discussion inspected as
    context.'
  accessed_at: '2026-10-21T12:47:40Z'
  support: supports
  summary: The study detects chelerythrine in C. majus root and aerial-part extracts
    using retention time and DAD spectrum comparison with standards, with collected
    fractions checked by mass spectrometry. This supports plant occurrence rather
    than an invented biosynthetic pathway. Individually tested chelerythrine was a
    purchased standard of at least 90 percent purity, so its antibacterial assay is
    not automatically a purified isolate from those plants. Mixture tests remain separate.
  snapshot_sha256: f114a1bc4e0a076de3c03bc4436553c33a2fd493a9ff25c5220ecf7ab91f04c3
- evidence_id: antibacterial-primary
  kind: primary_source
  reference: PMID:24824737; DOI:10.1371/journal.pone.0097000; https://pmc.ncbi.nlm.nih.gov/articles/PMC4019524/
  locator: Full main narrative, Methods and Tables 1–3; Figure 1 and Tables 2/3 visually
    inspected.
  accessed_at: '2026-10-21T12:47:02Z'
  support: supports
  summary: Exact chelerythrine is compound 10, drawn as the quaternary cation and
    distinguished from reduced/oxygenated analogues. It was isolated as 120 mg crystals
    from Z. rhoifolium stem bark and identified using authentic TLC comparison and
    reported NMR data. Table 2 reports MIC 1.5 micrograms/mL for six tested bacteria,
    with distinct MBCs. Broth microdilution uses 1e5 CFU/mL, casein soy broth and
    24 h at 37 C for bacteria; subculture assesses bactericidal activity. This directly
    supports the role without requiring a chloride counterion to be added to the native
    active-moiety graph.
  snapshot_sha256: 0af93a0782f00274e277f423d19514627b8fe80dbfe37619d2136718a6e09188
- evidence_id: assay-boundaries
  kind: primary_source
  reference: PMID:24824737, Methods, Tables 2/3 and Results/Discussion
  locator: Same inspected original main text and table images.
  accessed_at: '2026-10-21T12:47:02Z'
  support: context_only
  summary: The Methods list S. aureus ATCC 25923 while the tables identify ATCC 6538.
    B. subtilis MBC is 50 micrograms/mL in Table 2 but 6.25 in Table 3; MIC is 1.5
    in both. The abstract blanket statement should not replace the different organism-specific
    values in Table 3. Optical-density kinetics merely suggest a nonbacteriolytic
    effect; they do not prove a molecular target. Erythrocyte TBARS/AOPP and hemolysis
    are host-cell endpoints, not microbial ROS or universal safety. No disputed numeric
    value is asserted in the native seed.
  snapshot_sha256: 0af93a0782f00274e277f423d19514627b8fe80dbfe37619d2136718a6e09188
- evidence_id: adopted-antibacterial
  kind: primary_source
  reference: PMID:24824737; DOI:10.1371/journal.pone.0097000
  locator: Complete original indexed abstract followed by original full-main-text
    review above.
  accessed_at: '2026-10-21T12:46:34Z'
  support: supports
  summary: This is the one adopted paper directly testing exact chelerythrine antibacterial
    activity. Keep organism, material, endpoint and source inconsistencies explicit;
    the other seven leads are not equivalent antibacterial evidence.
  snapshot_sha256: a261549b4e0e052331f1c980a5598cf161de1bc62cf3773808d9e6016161ba08
- evidence_id: adopted-analysis
  kind: primary_source
  reference: PMID:23390024; DOI:10.1093/chromsci/bmt003
  locator: Complete original indexed abstract.
  accessed_at: '2026-10-21T12:46:34Z'
  support: context_only
  summary: HPLC fluorescence method for chelerythrine/nitidine in Z. nitidum. Supports
    analytical and that plant context, not the different Z. simulans source assertion
    or an antimicrobial mechanism.
  snapshot_sha256: a261549b4e0e052331f1c980a5598cf161de1bc62cf3773808d9e6016161ba08
- evidence_id: adopted-parasite
  kind: primary_source
  reference: PMID:24295957; DOI:10.1016/j.vetpar.2013.10.021
  locator: Complete original indexed abstract.
  accessed_at: '2026-10-21T12:46:34Z'
  support: context_only
  summary: Isolated chelerythrine and chloroxylonine from Toddalia asiatica tested
    against the fish ciliate Ichthyophthirius multifiliis. This is exact-compound
    antiparasitic context with a separate fish-toxicity endpoint, not a bacterial
    MIC or evidence for the named native plants.
  snapshot_sha256: a261549b4e0e052331f1c980a5598cf161de1bc62cf3773808d9e6016161ba08
- evidence_id: adopted-host
  kind: primary_source
  reference: PMID:23900672; DOI:10.1007/s13277-013-1016-4; PMID:24300194; DOI:10.1016/j.cbi.2013.11.011;
    PMID:24928629; DOI:10.1007/s10753-014-9929-7; PMID:24948079; DOI:10.1016/j.pharep.2014.03.013
  locator: Complete original indexed abstracts for all four primary studies.
  accessed_at: '2026-10-21T12:46:34Z'
  support: context_only
  summary: 23900672 concerns mitochondrial ROS and apoptosis in murine lymphoma cells.
    24300194 concerns ethanol-induced gastric injury and inflammatory responses in
    mice. 24928629 concerns LPS-induced endotoxic shock and host cytokine/NF-kappaB
    responses, not clearance of live bacteria. 24948079 evaluates mania-like behavior
    in mice. None establishes an antibacterial PKC target, microbial ROS mechanism
    or clinical approval.
  snapshot_sha256: a261549b4e0e052331f1c980a5598cf161de1bc62cf3773808d9e6016161ba08
- evidence_id: adopted-DNA
  kind: primary_source
  reference: PMID:25010289; DOI:10.1016/j.jphotobiol.2014.06.005
  locator: Complete original indexed abstract.
  accessed_at: '2026-10-21T12:46:34Z'
  support: context_only
  summary: Spectroscopy and calorimetry establish interaction with synthetic sequence-defined
    polynucleotides, including intercalative behavior. This is direct biophysical
    binding context but not proof that bacterial DNA engagement explains whole-cell
    killing. No bacterial taxon-specific target or causal chain follows from these
    experiments alone.
  snapshot_sha256: a261549b4e0e052331f1c980a5598cf161de1bc62cf3773808d9e6016161ba08
- evidence_id: search
  kind: search
  reference: 286-inclusive-hits.txt; bounded exact-name/identifier and plant-source
    searches
  locator: Hidden and ignored files included. Official identifiers and original literature
    at documented depth.
  accessed_at: '2026-10-21T12:52:08Z'
  support: context_only
  summary: Exact local hits comprise native record, ChEBI row, readiness queue, PATHS
    and generated embeddings; no matching curator decision/overlay was found in the
    stated scope. No record-native gene, protein, regulator, pathway, stress response
    or transcriptomic dataset triggers the structured adapter. A chemical LINCS identifier
    is not itself a native transcriptomic dataset assertion. External host-cell literature
    was not promoted to native target claims.
  snapshot_sha256: 5cd0a94bd4a1f0badcad7b40365039a99203918d7dc78cb1ddd2c74bceeaaa89
  search_scope: rg --no-ignore --hidden -n -F for CHEBI:78373, chelerythrine, LLEJIEBFSOEYIV-UHFFFAOYSA-N
    and antibioticmech:chebi-cd1a4e7da7 across data, curation, conf, scripts, src,
    docs, .claude, reviews and reports; bounded public exact identifiers and Z. simulans/C.
    majus primary-source queries on 2026-10-21.
- evidence_id: validation
  kind: validation
  reference: 286-schema.log; 286-strict.log; 286-strict.tsv; 286-chemistry-initial.json;
    286-chemistry.json; 286-xref-chemistry.json
  locator: Actual focused outputs and native/external independent molecular parses.
  accessed_at: '2026-10-21T12:52:08Z'
  support: supports
  summary: Schema and strict exit 0. Initial generic chemistry helper exit 1 reflected
    only RDKit appended-charge formula notation; the corrected scratch helper compares
    elemental formula separately and verifies charge +1, key, masses and mint, exiting
    0. External representations agree. An initial external helper incorrectly treated
    the CCD InChIKey metadata line as SMILES; its failed log is retained as 286-xref-check-initial.log,
    and descriptor selection was corrected without modifying any chemical input. No
    native input was changed to obtain these passes.
  snapshot_sha256: 37170a6f009f677b2f9f899a9b81a8367423dd23e5513bcb25059c7f99904d01
assessments:
- assessment_id: identity
  area: identity
  topic: Exact chelerythrine cation and names
  outcome: supported
  summary: Native structure, cation/alkaloid parents and systematic names are coherent.
    Accessible public graphs agree, including official normalized LINCS1187. Counterions,
    pseudobases and reduced analogues remain separate. MetaCyc/Reaxys exact structure
    verification is limited.
  target_ids:
  - CHEBI:78373
  evidence_ids:
  - record
  - chebi
  - chemical-identifiers
  - lincs
  - restricted-identifiers
  - validation
- assessment_id: definition
  area: evidence
  topic: Plant-source wording
  outcome: supported
  summary: ChEBI directly supports the definition, and primary root-bark isolation
    from Z. simulans plus chromatographic confirmation in C. majus support the two
    named species. KNApSAcK supports broader plant occurrence as database context;
    no complete family-wide primary isolation audit or biosynthetic pathway is claimed.
  target_ids:
  - CHEBI:78373
  evidence_ids:
  - chebi
  - plant-simulans
  - plant-majus
  - chemical-identifiers
- assessment_id: scope
  area: scope
  topic: Antibacterial role and exact study material
  outcome: supported
  summary: The original 2014 compound 10 drawing and experiments support antibacterial
    activity of the named cation. Its bulk counterion is not fully characterized in
    the accessed report, so quantitative material scope must remain explicit. Taxon
    and assay reporting inconsistencies limit later numerical enrichment, not the
    native general role.
  target_ids:
  - CHEBI:78373
  evidence_ids:
  - antibacterial-primary
  - assay-boundaries
  - chebi
- assessment_id: bibliography
  area: evidence
  topic: All eight source PMID dispositions
  outcome: supported
  summary: Every adopted PMID resolves and its complete abstract was read. The extraction
    logic intentionally keeps them as leads. One directly tests antibacterial activity;
    the other seven concern analytical chemistry, parasites, host-cell effects or
    synthetic DNA. No claim-level evidence was fabricated by seeding their citation
    list.
  target_ids:
  - CHEBI:78373
  evidence_ids:
  - source
  - adopted-antibacterial
  - adopted-analysis
  - adopted-parasite
  - adopted-host
  - adopted-DNA
- assessment_id: completeness
  area: completeness
  topic: Mechanism and activity detail
  outcome: unknown
  summary: Optional activity/producer/target enrichment is possible after handling
    material and source inconsistencies. The inspected work does not justify transferring
    host PKC or mitochondrial ROS effects to bacteria. No requirement forces a target
    or causal graph onto this identity/role seed.
  target_ids:
  - CHEBI:78373
  evidence_ids:
  - record
  - assay-boundaries
  - adopted-host
  - adopted-DNA
- assessment_id: xref-maintenance
  area: ownership
  topic: Retired KNApSAcK duplicate
  outcome: concern
  summary: C00024660 is explicitly old at its provider and its direct record no longer
    resolves; the active C00024634 and historical exact identity are both established.
    A narrow maintained-source cleanup is warranted without changing the native molecular
    structure.
  target_ids:
  - CHEBI:78373
  evidence_ids:
  - source
  - retired-knapsack
  - chemical-identifiers
findings:
- finding_id: F1
  issue_key: chelerythrine-obsolete-knapsack-c00024660
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Retire the obsolete duplicate KNApSAcK cross-reference
  description: xrefs[3] retains KNApSAcK C00024660. The provider direct entry rejects
    it and its official Twins index labels it old. Historical PCIDB metadata maps
    it to the same exact cation, while native xrefs[2] C00024634 already resolves
    to the active exact entry. Normalize the obsolete reference through the maintained
    source path; preserve historical provenance if required. This is not evidence
    of a wrong chelerythrine structure.
  target_ids:
  - CHEBI:78373
  field_paths:
  - xrefs[3]
  evidence_ids:
  - source
  - chemical-identifiers
  - retired-knapsack
  rule_id: 'review-yaml-record: verify stable source accessions; native-review-checklist:
    Equivalence and provenance'
  native_severity: minor
  normalization_reason: The historical identity remains correct and an active exact
    identifier is already present. The defect is a retired redundant external reference,
    with limited provenance/usability impact rather than a chemical mismatch.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Imported obsolete KNApSAcK cross-reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source normalization
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-specific xref policy where appropriate
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Xref filtering and deterministic emission
actions:
- action_id: A1
  description: Normalize the obsolete KNApSAcK identifier without altering chelerythrine
    identity.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:78373
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Imported obsolete KNApSAcK cross-reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source normalization
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-specific xref policy where appropriate
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Xref filtering and deterministic emission
  acceptance_checks:
  - Confirm the provider retirement and retain C00024634 as the active exact chemical
    entry. Remove or qualify C00024660 through a maintained upstream mapping/filter
    so regeneration does not restore it as an active link.
  - Preserve historical evidence of the old identifier if the repository policy retains
    retired mappings; do not relabel it as a different chemical structure.
  - Rerun extraction/seeding through the owning path, focused schema/strict checks
    and exact structure validation, plus applicable corpus gates.
- action_id: A2
  description: If enriching optional primary evidence, retain exact material, assay
    and biological scope.
  finding_ids: []
  target_ids:
  - CHEBI:78373
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/chelerythrine.yaml
    role: Curator-owned primary activity, source and mechanism additions
  acceptance_checks:
  - Use original PMID 24824737 compound 10 and preserve MIC versus MBC, strains, medium,
    inoculum and incubation. Reconcile the S. aureus strain discrepancy and B. subtilis
    MBC discrepancy before adding those exact observations.
  - Do not transfer extract/mixture potency, reduced-analogue results, chloride bulk
    mass conventions or host-cell kinase/ROS responses into unqualified cation-specific
    antibacterial claims.
  - Keep synthetic-DNA binding and nonbacteriolytic OD behavior separate from a demonstrated
    whole-cell molecular target. Absence of an established target in the inspected
    sources does not establish universal absence of a mechanism.
  - Resolve MetaCyc/Reaxys structures when freely available before claiming every
    external identity independently verified; no paid access is necessary for the
    bounded current review.
limitations:
- MetaCyc CPD-16782 returned an account requirement from both page and structured
  endpoint; Reaxys 3915260 was not inspected behind paid access. They are attested
  by ChEBI, not independently verified at exact graph depth.
- The original 1993 Z. simulans isolation paper was accessible at complete publisher-abstract
  depth only. C. majus occurrence was checked in the original 2019 relevant methods/results;
  a full primary audit of every Papaveraceae occurrence was not attempted.
- All eight adopted abstracts were read; PMID 24824737 received full main-text and
  selected visual follow-up. The seven other adopted papers were not inspected as
  complete articles and are not used to establish an antibacterial target.
- The 2014 primary paper inconsistently reports S. aureus strains and B. subtilis
  MBC values, and does not fully specify the bulk counterion of isolated compound
  10. Figure 1 and Tables 2/3 were visually checked, but complete original spectra
  and additional images were not independently reanalyzed.
- The native record has no structured-adapter trigger. No external expression-module
  membership, host-cell response, protein-bound CCD occurrence or chemical-library
  membership is treated as antimicrobial causal proof.
- Scientific completion remains partial. No paid access, external contact or provider-credit
  research was used. Deterministic validation does not constitute native REVIEWED
  sign-off.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Root read the entire native record and scientific draft, verified thirteen captured
  hashes, checked explicit provider retirement and visually inspected original compound10
  Figure1 before ordered persistence.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
