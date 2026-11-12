# Dragmacidin F: wrong pyrrole hydrogenation, non-equivalent ChEMBL link and copied G definition

- Review: 20261021T150749Z-dragmacidin-f-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:43:54Z
- Finished UTC: 2026-10-21T15:07:49Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The stored F graph has a reduced pyrrole bond and two excess hydrogens compared with original synthetic/natural-product characterization. Its ChEMBL link separately denotes a C26 compound, and its definition describes dragmacidin G. One identity blocker and two major source defects require maintained-input correction. Natural F stereochemistry is directly supported by enantiomeric synthesis, while exact antibacterial eligibility remains a separate bounded question.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 378; one exact record. Original 13 hashes preserved within 25 expanded source/context inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-6a4094ddb2 | data/antibiotics/antibacterial/dragmacidin-f.yaml | generated | dragmacidin F |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Structured-source applicability | not_applicable | False | antibioticmech:aro-6a4094ddb2 | No native named molecular protein, gene, pathway or transcriptomic claim is present. Synthesis and phenotype context were not used to infer a bacterial molecular mechanism. |
| Focused chemistry verification | passed | False | antibioticmech:aro-6a4094ddb2 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-6a4094ddb2 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-6a4094ddb2 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-6a4094ddb2 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-6a4094ddb2 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-6a4094ddb2 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-6a4094ddb2 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-6a4094ddb2 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-6a4094ddb2 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-6a4094ddb2 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-6a4094ddb2 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-6a4094ddb2 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact natural F versus reduced native graph

identity: concern. Targets: antibioticmech:aro-6a4094ddb2.

Original synthesis drawings and final HRMS establish the aromatic pyrrole and neutral H20 parent. Native H22 has the wrong hydrogenation state. A stereochemical-looking R/S discrepancy at the bridgehead resolves after restoring the bond, so it is not counted as an independent epimer error.

### Mint and exact chemical xrefs

grounding: concern. Targets: antibioticmech:aro-6a4094ddb2.

The mint is coherent, but PubChem propagates the wrong H22 graph. ChEMBL instead supplies a C26 graph and cannot be an exact F link. Correct the named structure and every chemical equivalence coherently.

### Copied G identity and source pointer

evidence: concern. Targets: antibioticmech:aro-6a4094ddb2.

The definition and cited material belong to G/G-H, not F. This requires an exact-F rewrite with inspected provenance rather than a letter substitution.

### ANTIBACTERIAL placement versus inspected evidence

scope: unknown. Targets: antibioticmech:aro-6a4094ddb2.

The original F lead reports antiviral activity, while the adopted antibacterial experiments concern G. No F bacterial growth assay was verified at this reading depth. Reassess eligibility after identity correction; this bounded gap does not prove antibacterial inactivity or alone mandate deletion.

### Optional quantitative activity_spectrum

completeness: unknown. Targets: antibioticmech:aro-6a4094ddb2.

No such native field is populated. G MICs and F viral EC50 values must not be converted into F antibacterial rows, and synthetic antipode/TFA material must not silently be treated as neutral natural F. Optional absence is not itself a schema error.

### Mechanism, targets and resistance

completeness: unknown. Targets: antibioticmech:aro-6a4094ddb2.

No native molecular claim is populated. The synthesis papers establish chemistry and stereochemistry; antiviral family descriptions do not establish a direct bacterial protein target, resistance allele or mechanism chain.

### Producer, clinical, causal and dataset assertions

scope: not_applicable. Targets: antibioticmech:aro-6a4094ddb2.

No structured assertions in these domains occur. The G sponge source in the definition cannot be retained as F provenance. No therapeutic approval, clinical efficacy or production organism is inferred from isolation or synthesis.

### Maintained ownership and native history

provenance: supported. Targets: antibioticmech:aro-6a4094ddb2.

The source row, structure enrichment, one ARO concept and three generated events reproduce. All original captures remain preserved among actual-owner inputs. SEEDED status is retained.

### Deterministic checks and scientific scope

schema: supported. Targets: antibioticmech:aro-6a4094ddb2.

All focused checks pass; none establishes source-level exact chemical identity or detects G-to-F claim transfer.

## Findings

### F1: The stored molecule has a reduced pyrrole and two excess hydrogens

blocker / open / confirmed; issue key: dragmacidin-f-wrong-pyrrole-hydrogenation.

Native/PubChem encode a single bond between fused pyrrole atoms 7/8, introducing two CH stereocentres and C25H22BrN7O3. Actual original drawings and HRMS require the aromatic pyrrole and neutral C25H20BrN7O3. The mismatch is constitutional hydrogenation, not tautomerism, salt choice or merely missing stereochemistry. Resolve the exact natural S,S,S structure and chemical grounding before assay enrichment.

### F2: The asserted exact ChEMBL link denotes a C26 compound

major / open / confirmed; issue key: dragmacidin-f-chembl-extra-carbon.

CHEMBL4079851 resolves to C26H22BrN7O3/QHEFDEADWAFGNX-YPFXHSDDSA-N. It differs in carbon connectivity from both the native C25 graph and the primary natural F structure. Remove or replace this chemical equivalence through maintained sources after exact structure adjudication; a shared family drawing is insufficient.

### F3: The definition and adopted evidence describe G under the F label

major / open / confirmed; issue key: dragmacidin-f-definition-is-dragmacidin-g.

The copied definition explicitly names G, including its sulfur side chain and MRSA/tuberculosis/Plasmodium/cancer-cell results. The adopted originals concern G or G/H. Rewrite with exact F evidence; replacing the letter G with F would preserve false claims.

## Recommended Actions And Acceptance Checks

### A1

Resolve and regenerate the exact natural dragmacidin F graph and chemical grounding.

- Reconcile the aromatic pyrrole, neutral C25H20BrN7O3 and measured natural S,S,S stereochemistry against actual original drawings and characterization.
- Treat the scratch repaired key as a diagnostic candidate requiring independent full-structure review, including neutral versus TFA/counterion scope.
- Update all structure fields and non-equivalent PubChem references coherently through maintained inputs.
- Run focused chemistry/schema/strict, source provenance and corpus regeneration checks.

### A2

Correct the non-equivalent ChEMBL cross-reference.

- Any retained exact link independently resolves to the adjudicated C25 natural F graph and stereochemistry.
- Do not retain CHEMBL4079851 as an exact chemical equivalent merely because it resembles the scaffold.

### A3

Replace G claims with an exact F definition and evidence scope.

- Every retained identity, isolation and biological statement is supported for exact F material.
- Do not transfer G antibacterial results or reinterpret viral assays as bacterial growth endpoints.
- Reassess exact antibacterial eligibility as a separate question after identity correction, recording unresolved evidence without claiming inactivity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/dragmacidin-f.yaml; Complete native record: definition/citation, parent/class, graph, three xrefs, source concept and three history events | supports | The MINTED/SEEDED F record contains the G definition and has neutral C25H22BrN7O3. Its graph has three assigned and two unassigned carbon centres. No synonym, role list, mode, target, resistance, activity_spectrum, clinical product, structured producer, graph or dataset assertion occurs. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; ARO row 546; PubChem row 239; extractor, enrichment and seeder | supports | The exact ARO row supplies the G definition, citations PMID38206835 and PMID28085024, and F-labelled chemical links. The PubChem row supplies the H22 graph. These are inherited source defects. Initial hashes are preserved and actual ARO/PubChem ownership was captured before assessment. |
| chemistry | RDKit2026.03.5 using batch 019 interpreter against batch 038 cwd; 378-chemistry.json | supports | Both native encodings reproduce IIJUQWOGZFHFTN-FHUFSZDOSA-N, neutral C25H22BrN7O3, masses and source mint. Native SMILES atoms 1/2/4 are S/R/S and atoms 7/8 are unassigned stereogenic CH centres. Internal agreement does not establish the named natural identity. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007778; Current ARO:3007778 term and exact links | supports | Current ARO repeats the F label, G description, adopted citations and chemical links. This establishes propagation, not scientific support for the wrong-compound definition or chemical equivalences. |
| parent | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007773; ARO:3007773 broader bis-indole alkaloid class | supports | The broad source class resolves. Its antibiotic label is not an exact F antibacterial experiment and cannot justify importing another dragmacidin activity. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/459934/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; Current CID459934 full properties | supports | Current PubChem repeats native C25H22BrN7O3 and IIJUQWOGZFHFTN-FHUFSZDOSA-N. The reduced pyrrole and extra hydrogens are therefore inherited from the adopted chemical mapping, rather than a native encoding inconsistency. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL4079851.json; Current CHEMBL4079851 complete structure and independently parsed graph | supports | This ChEMBL entry has C26H22BrN7O3 and QHEFDEADWAFGNX-YPFXHSDDSA-N, including an additional carbon in the bridged scaffold. It is not the native C25 graph or the primary F parent. This is a constitutional equivalence mismatch, not a counterion or stereochemistry-only difference. |
| adopted2024 | https://doi.org/10.1021/acs.orglett.3c04039; PMID38206835 original title/abstract; material scope | context_only | This paper synthesizes G and H and reports antibacterial testing of those compounds and analogues against S. aureus and efflux-deficient Salmonella Typhimurium. No F experiment is established by its abstract. Publisher full text returned 403, so uninspected supplementary assays are not claimed. |
| adopted2017 | https://doi.org/10.3390/md15010016; PMID28085024/PMC5295236; original abstract, Results, isolation and antibacterial Methods | supports | This original is the source of the copied G definition. Its purified material and MRSA, tuberculosis, Plasmodium and pancreatic-cell results concern G, with F only in family background. The measured experimental material is not F. |
| g-figure | https://pub.mdpi-res.com/marinedrugs/marinedrugs-15-00016/article_deploy/html/images/marinedrugs-15-00016-g001.png; Actual Figure 1, compound 1 | supports | G has two brominated indoles, a pyrazine and sulfur-containing mercaptoethylguanidine side chain. F has a different bridged pyrrole/imidazole/pyrazinone architecture and one bromine. The definition is not a permissible synonym or derivative description of F. |
| synthesis2004 | https://doi.org/10.1021/ja046695b; PMID15291554; full two-page original, actual Schemes 1/4 and identity paragraph | supports | The first synthesis produced the positive-rotation antipode, with NMR/IR/UV/HPLC matching authentic natural F but opposite rotation. The authors establish natural F as (4-double-prime S,6-double-prime S,6-triple-prime S), natural rotation minus 159 versus synthetic plus 146 under the stated methanol conditions. Actual drawings show an aromatic pyrrole, not the two-CH reduced ring encoded natively. |
| synthesis2004-si | https://stoltz2.caltech.edu/publications/39-s-2004.pdf; Supporting Information S21–S24, final product preparation/HRMS and natural-versus-synthetic comparisons; actual S22/S24 viewed | supports | Final synthetic F gives [M+H]+ calculated as C25H21BrN7O3, m/z 546.0889, observed 546.0883. The neutral parent is therefore C25H20BrN7O3, not native H22. S24 identifies synthetic counterion TFA and natural counterion unknown; reversed-phase purification used TFA. Counterion differences and neutral-parent normalization cannot explain a reduced pyrrole bond or two excess parent hydrogens. |
| synthesis2005 | https://doi.org/10.1021/ja050586v; PMID15839697; printed page 5975 actual Figure 2/absolute-stereochemistry section and page 5978 natural-enantiomer completion | supports | The follow-up prepared both antipodes. Its final negative-rotation synthetic material matches natural F spectroscopically and in rotation sign; the natural configuration is S,S,S. Figure 2 explicitly separates experimentally established F from biosynthetic proposals for D/E. No new antibacterial assay panel is reported; the Conclusion says further biological testing was underway. |
| synthesis2005-si | https://stoltz2.caltech.edu/publications/45-s-2005.pdf; Supporting Information S35–S36; actual natural-enantiomer drawing and rotation viewed | supports | The final product is labelled negative natural dragmacidin F. Its measured rotation is minus 148.33 at 29 degrees C, c 0.20 in methanol; natural comparison is minus 159 at 25 degrees C, c 0.40. The preparation follows the earlier sequence, with final characterization cross-referenced. No neutral free-base antibacterial experiment is inferred from this isolated synthetic material. |
| atom-map | Scratch bond-order diagnostic; no native edits; 377378-xref-atommap.json; zero-based native SMILES atom map | supports | The fused pyrrole is N11-C7-C8-C9-C10-N11; native atoms 7/8 are CH connected by a single bond. Changing only that bond to double restores aromaticity, removes two hydrogens/unassigned centres and gives C25H20BrN7O3, DCPFQRFLBCNBTP-IZFSOPRVSA-N, with atoms 1/2/4 all S. Atom 2 changes R-to-S CIP because bond priorities change, without physical inversion. These centres correspond to methyl-bearing 6-triple-prime, bridged 4-double-prime and hydroxy 6-double-prime. This is a diagnostic candidate requiring ordinary independent full-structure adjudication before adoption. |
| isolation-lead | https://www.researchgate.net/publication/224777300_Dragmacidin_F_A_New_Antiviral_Bromoindole_Alkaloid_from_the_Mediterranean_Sponge_Halicortex_sp; Cutignano et al. 2000 original abstract, ResearchGate lines 56–58; full-text unavailability at lines 68–75 | partial | The original isolation is identified as F from Mediterranean Halicortex sp. The retrieved original abstract describes antiviral HSV-1/HIV-1 activity, and the synthesis originals cite it for the natural sample. Original full-text publisher routes failed 403/429. Exact viral assay protocols and material counterion were not independently verified here, and those antiviral results are not F bacterial growth experiments. |
| search | Ignored-inclusive local reference search and bounded free primary discovery; 377378-all-local-paths.txt;378-discovery.json;378-antibacterial-discovery.json;378-chebi-search.json | context_only | Exact F discovery recovered the stereochemical synthesis originals and the original isolation lead. No exact F antibacterial experiment was verified in the inspected sources. The official ChEBI exact-name query returned zero terms. These are bounded results, not proof of universal absence or inactivity. |
| gates | Focused chemistry, schema and strict checks; 378-focused-results.json | supports | All focused executions pass despite the wrong named molecular structure, non-equivalent chemical xref and copied G claims. Native gates used batch 038 and chemistry used batch 019 RDKit against batch 038 cwd. |

## Limits And Additional Notes

- The 2004 two-page original was read in full, with actual structural schemes and SI final-product/HRMS/counterion pages. The 2005 original was read at absolute-stereochemistry and final natural-enantiomer scope with actual Figure 2 and SI S35–S36, not every unrelated synthetic-intermediate experiment. Raw spectra were not independently reprocessed.
- The original 2000 isolation full text was unavailable through publisher 403/429 routes; its abstract and the synthesis originals establish the lead scope, but exact viral assay conditions and natural counterion remain unverified.
- Adopted 2024 G/H evidence was available at original-abstract depth after publisher 403. Adopted 2017 G was inspected at full experimental/material scope with the actual structure figure. Neither was treated as an F antibacterial assay.
- The diagnostic one-bond repair identifies the hydrogenation defect and reproduces three S centres, but it is not a saved or independently finalized replacement structure. Exact neutral natural F antibacterial eligibility remains unresolved; no inactivity or racemate inference is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native/source/status/history was edited. Optional links, tags and notes were checked specifically against dragmacidin F.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T150749Z-dragmacidin-f-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Dragmacidin F: wrong pyrrole hydrogenation, non-equivalent ChEMBL link and
  copied G definition'
started_at: '2026-10-21T14:43:54Z'
finished_at: '2026-10-21T15:07:49Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent whole-record and actual ARO/PubChem-row audit after
    input capture, live chemical xref comparison, original synthesis and supporting-characterization
    reading, actual structural/MS pages and diagnostic atom/bond mapping without native
    editing.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The stored F graph has a reduced pyrrole bond and two excess hydrogens compared
  with original synthetic/natural-product characterization. Its ChEMBL link separately
  denotes a C26 compound, and its definition describes dragmacidin G. One identity
  blocker and two major source defects require maintained-input correction. Natural
  F stereochemistry is directly supported by enantiomeric synthesis, while exact antibacterial
  eligibility remains a separate bounded question.
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
  - path: data/antibiotics/antibacterial/dragmacidin-f.yaml
    sha256: 56e67cebe73d874348f97c91a623bbb83d28dcf6343e82fbb23eee6a20fbe48c
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
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-6a4094ddb2
  path: data/antibiotics/antibacterial/dragmacidin-f.yaml
  label: dragmacidin F
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO identity, definition and citation owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Minted molecular graph and chemical xref owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure retrieval
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 378; one exact record. Original 13 hashes preserved within
    25 expanded source/context inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-6a4094ddb2
checks:
- check_id: structured-adapter
  name: Structured-source applicability
  status: not_applicable
  required: false
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  summary: No native named molecular protein, gene, pathway or transcriptomic claim
    is present. Synthesis and phenotype context were not used to infer a bacterial
    molecular mechanism.
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/377378-focused.py
    (cwd /private/tmp/antibioticmech-record-reviews-038)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/dragmacidin-f.yaml (cwd /private/tmp/antibioticmech-record-reviews-038)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/dragmacidin-f.yaml --out /private/tmp/am-review-session/378-strict.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-038)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-6a4094ddb2
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
  - antibioticmech:aro-6a4094ddb2
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
  - antibioticmech:aro-6a4094ddb2
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
  - antibioticmech:aro-6a4094ddb2
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
  - antibioticmech:aro-6a4094ddb2
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
  - antibioticmech:aro-6a4094ddb2
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
  - antibioticmech:aro-6a4094ddb2
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
  - antibioticmech:aro-6a4094ddb2
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
  - antibioticmech:aro-6a4094ddb2
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/dragmacidin-f.yaml
  locator: 'Complete native record: definition/citation, parent/class, graph, three
    xrefs, source concept and three history events'
  accessed_at: '2026-10-21T14:56:53Z'
  support: supports
  summary: The MINTED/SEEDED F record contains the G definition and has neutral C25H22BrN7O3.
    Its graph has three assigned and two unassigned carbon centres. No synonym, role
    list, mode, target, resistance, activity_spectrum, clinical product, structured
    producer, graph or dataset assertion occurs.
  snapshot_sha256: c107fcd06ea87c08843077f896579f49247e5b92d04535c16ab3e8d18165ea98
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv
  locator: ARO row 546; PubChem row 239; extractor, enrichment and seeder
  accessed_at: '2026-10-21T14:56:53Z'
  support: supports
  summary: The exact ARO row supplies the G definition, citations PMID38206835 and
    PMID28085024, and F-labelled chemical links. The PubChem row supplies the H22
    graph. These are inherited source defects. Initial hashes are preserved and actual
    ARO/PubChem ownership was captured before assessment.
  snapshot_sha256: c107fcd06ea87c08843077f896579f49247e5b92d04535c16ab3e8d18165ea98
- evidence_id: chemistry
  kind: validation
  reference: RDKit2026.03.5 using batch 019 interpreter against batch 038 cwd
  locator: 378-chemistry.json
  accessed_at: '2026-10-21T14:56:53Z'
  support: supports
  summary: Both native encodings reproduce IIJUQWOGZFHFTN-FHUFSZDOSA-N, neutral C25H22BrN7O3,
    masses and source mint. Native SMILES atoms 1/2/4 are S/R/S and atoms 7/8 are
    unassigned stereogenic CH centres. Internal agreement does not establish the named
    natural identity.
  snapshot_sha256: 3904d87cd811b8d163602f7f9177a918c0f79aa8746c8ffad8ca64d1ffd44b81
- evidence_id: aro
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007778
  locator: Current ARO:3007778 term and exact links
  accessed_at: '2026-10-21T14:48:50.959914Z'
  support: supports
  summary: Current ARO repeats the F label, G description, adopted citations and chemical
    links. This establishes propagation, not scientific support for the wrong-compound
    definition or chemical equivalences.
  snapshot_sha256: d3192bd026320e4d703621015b7b0770ceb9fbf190db5339e181531ccab97f57
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007773
  locator: ARO:3007773 broader bis-indole alkaloid class
  accessed_at: '2026-10-21T14:48:50.966910Z'
  support: supports
  summary: The broad source class resolves. Its antibiotic label is not an exact F
    antibacterial experiment and cannot justify importing another dragmacidin activity.
  snapshot_sha256: 3c0907ecf40a389d370eedb2be41438c7b3ac89dc06dcc332a4bafc65bf1bbb4
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/459934/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: Current CID459934 full properties
  accessed_at: '2026-10-21T14:48:51.643356Z'
  support: supports
  summary: Current PubChem repeats native C25H22BrN7O3 and IIJUQWOGZFHFTN-FHUFSZDOSA-N.
    The reduced pyrrole and extra hydrogens are therefore inherited from the adopted
    chemical mapping, rather than a native encoding inconsistency.
  snapshot_sha256: cbd5c38cefb32fdba8f32b16e1d469d4836137a476c506d8596b945a023a8a75
- evidence_id: chembl
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL4079851.json
  locator: Current CHEMBL4079851 complete structure and independently parsed graph
  accessed_at: '2026-10-21T14:48:51.586204Z'
  support: supports
  summary: This ChEMBL entry has C26H22BrN7O3 and QHEFDEADWAFGNX-YPFXHSDDSA-N, including
    an additional carbon in the bridged scaffold. It is not the native C25 graph or
    the primary F parent. This is a constitutional equivalence mismatch, not a counterion
    or stereochemistry-only difference.
  snapshot_sha256: eedeab211e8cc8c9ff1496cbd923b75db3ce12db26a2854bc83b328ac2da7e17
- evidence_id: adopted2024
  kind: primary_source
  reference: https://doi.org/10.1021/acs.orglett.3c04039
  locator: PMID38206835 original title/abstract; material scope
  accessed_at: '2026-10-21T14:48:50.945052Z'
  support: context_only
  summary: This paper synthesizes G and H and reports antibacterial testing of those
    compounds and analogues against S. aureus and efflux-deficient Salmonella Typhimurium.
    No F experiment is established by its abstract. Publisher full text returned 403,
    so uninspected supplementary assays are not claimed.
  snapshot_sha256: 9797c9b6877a34f621452e9abe60acae6dceb4b759c82b94a9f64de1ace7274c
- evidence_id: adopted2017
  kind: primary_source
  reference: https://doi.org/10.3390/md15010016
  locator: PMID28085024/PMC5295236; original abstract, Results, isolation and antibacterial
    Methods
  accessed_at: '2026-10-21T14:49:20.301036Z'
  support: supports
  summary: This original is the source of the copied G definition. Its purified material
    and MRSA, tuberculosis, Plasmodium and pancreatic-cell results concern G, with
    F only in family background. The measured experimental material is not F.
  snapshot_sha256: 5274486045543d17a24c658a77c86d11e71359cbbd2af9cd7f769a344953c5ee
- evidence_id: g-figure
  kind: primary_source
  reference: https://pub.mdpi-res.com/marinedrugs/marinedrugs-15-00016/article_deploy/html/images/marinedrugs-15-00016-g001.png
  locator: Actual Figure 1, compound 1
  accessed_at: '2026-10-21T14:51:03.955265Z'
  support: supports
  summary: G has two brominated indoles, a pyrazine and sulfur-containing mercaptoethylguanidine
    side chain. F has a different bridged pyrrole/imidazole/pyrazinone architecture
    and one bromine. The definition is not a permissible synonym or derivative description
    of F.
  snapshot_sha256: 4375c39aa7f3564e34af4e4089eb743c3661669b6db1c9cbb2bd38506faac458
- evidence_id: synthesis2004
  kind: primary_source
  reference: https://doi.org/10.1021/ja046695b
  locator: PMID15291554; full two-page original, actual Schemes 1/4 and identity paragraph
  accessed_at: '2026-10-21T14:49:20.301538Z'
  support: supports
  summary: The first synthesis produced the positive-rotation antipode, with NMR/IR/UV/HPLC
    matching authentic natural F but opposite rotation. The authors establish natural
    F as (4-double-prime S,6-double-prime S,6-triple-prime S), natural rotation minus
    159 versus synthetic plus 146 under the stated methanol conditions. Actual drawings
    show an aromatic pyrrole, not the two-CH reduced ring encoded natively.
  snapshot_sha256: 1e85d87d0f7abd61d14ab36352b4631f757399004391a1a9a66233ca99ae1472
- evidence_id: synthesis2004-si
  kind: primary_source
  reference: https://stoltz2.caltech.edu/publications/39-s-2004.pdf
  locator: Supporting Information S21–S24, final product preparation/HRMS and natural-versus-synthetic
    comparisons; actual S22/S24 viewed
  accessed_at: '2026-10-21T14:50:00.265373Z'
  support: supports
  summary: Final synthetic F gives [M+H]+ calculated as C25H21BrN7O3, m/z 546.0889,
    observed 546.0883. The neutral parent is therefore C25H20BrN7O3, not native H22.
    S24 identifies synthetic counterion TFA and natural counterion unknown; reversed-phase
    purification used TFA. Counterion differences and neutral-parent normalization
    cannot explain a reduced pyrrole bond or two excess parent hydrogens.
  snapshot_sha256: 1323183cc9c595d56520908b5fe592cd08a55b6f4351c820a96211c2779864b7
- evidence_id: synthesis2005
  kind: primary_source
  reference: https://doi.org/10.1021/ja050586v
  locator: PMID15839697; printed page 5975 actual Figure 2/absolute-stereochemistry
    section and page 5978 natural-enantiomer completion
  accessed_at: '2026-10-21T14:50:00.265809Z'
  support: supports
  summary: The follow-up prepared both antipodes. Its final negative-rotation synthetic
    material matches natural F spectroscopically and in rotation sign; the natural
    configuration is S,S,S. Figure 2 explicitly separates experimentally established
    F from biosynthetic proposals for D/E. No new antibacterial assay panel is reported;
    the Conclusion says further biological testing was underway.
  snapshot_sha256: 3106353669d0e478ee608918664b820e89e204136b0e7e16128ef556798c9c8e
- evidence_id: synthesis2005-si
  kind: primary_source
  reference: https://stoltz2.caltech.edu/publications/45-s-2005.pdf
  locator: Supporting Information S35–S36; actual natural-enantiomer drawing and rotation
    viewed
  accessed_at: '2026-10-21T14:50:00.265957Z'
  support: supports
  summary: The final product is labelled negative natural dragmacidin F. Its measured
    rotation is minus 148.33 at 29 degrees C, c 0.20 in methanol; natural comparison
    is minus 159 at 25 degrees C, c 0.40. The preparation follows the earlier sequence,
    with final characterization cross-referenced. No neutral free-base antibacterial
    experiment is inferred from this isolated synthetic material.
  snapshot_sha256: 5bdeef915300e0f905191aaa260e0fc563d6b7326693b1f941eb3760336304ac
- evidence_id: atom-map
  kind: validation
  reference: Scratch bond-order diagnostic; no native edits
  locator: 377378-xref-atommap.json; zero-based native SMILES atom map
  accessed_at: '2026-10-21T14:56:53Z'
  support: supports
  summary: The fused pyrrole is N11-C7-C8-C9-C10-N11; native atoms 7/8 are CH connected
    by a single bond. Changing only that bond to double restores aromaticity, removes
    two hydrogens/unassigned centres and gives C25H20BrN7O3, DCPFQRFLBCNBTP-IZFSOPRVSA-N,
    with atoms 1/2/4 all S. Atom 2 changes R-to-S CIP because bond priorities change,
    without physical inversion. These centres correspond to methyl-bearing 6-triple-prime,
    bridged 4-double-prime and hydroxy 6-double-prime. This is a diagnostic candidate
    requiring ordinary independent full-structure adjudication before adoption.
  snapshot_sha256: 07dd8321ce2062465e975f80506593faa055f9ce696e133114170f9dd2f4e969
- evidence_id: isolation-lead
  kind: primary_source
  reference: https://www.researchgate.net/publication/224777300_Dragmacidin_F_A_New_Antiviral_Bromoindole_Alkaloid_from_the_Mediterranean_Sponge_Halicortex_sp
  locator: Cutignano et al. 2000 original abstract, ResearchGate lines 56–58; full-text
    unavailability at lines 68–75
  accessed_at: '2026-10-21T14:54:55Z'
  support: partial
  summary: The original isolation is identified as F from Mediterranean Halicortex
    sp. The retrieved original abstract describes antiviral HSV-1/HIV-1 activity,
    and the synthesis originals cite it for the natural sample. Original full-text
    publisher routes failed 403/429. Exact viral assay protocols and material counterion
    were not independently verified here, and those antiviral results are not F bacterial
    growth experiments.
  snapshot_sha256: 6e92c78255ef485d0e4a1ecae96301c547bf633f638a9b8c676857b51ebcf8a0
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local reference search and bounded free primary discovery
  locator: 377378-all-local-paths.txt;378-discovery.json;378-antibacterial-discovery.json;378-chebi-search.json
  accessed_at: '2026-10-21T14:51:21.399073Z'
  support: context_only
  summary: Exact F discovery recovered the stereochemical synthesis originals and
    the original isolation lead. No exact F antibacterial experiment was verified
    in the inspected sources. The official ChEBI exact-name query returned zero terms.
    These are bounded results, not proof of universal absence or inactivity.
  snapshot_sha256: cc5382307c2dbb6e4da8527a92a13c8f3b337d3a69dc2bed3dd34f1c36c708e5
  search_scope: 2026-10-21; dragmacidin F, ARO:3007778, CID459934, CHEMBL4079851,
    both adopted PMIDs, exact-name antibacterial/antimicrobial/bacteria/MRSA searches
    and original synthesis/isolation leads. Local path search included hidden and
    ignored files without file-type exclusions. Official ChEBI exact-name search was
    spelling-bounded.
- evidence_id: gates
  kind: validation
  reference: Focused chemistry, schema and strict checks
  locator: 378-focused-results.json
  accessed_at: '2026-10-21T14:56:53Z'
  support: supports
  summary: All focused executions pass despite the wrong named molecular structure,
    non-equivalent chemical xref and copied G claims. Native gates used batch 038
    and chemistry used batch 019 RDKit against batch 038 cwd.
  snapshot_sha256: f3bb35ab936a40e12cf5cd44d91b7833479d3114be1dd3e10d9d977e431096bb
assessments:
- assessment_id: identity
  area: identity
  topic: Exact natural F versus reduced native graph
  outcome: concern
  summary: Original synthesis drawings and final HRMS establish the aromatic pyrrole
    and neutral H20 parent. Native H22 has the wrong hydrogenation state. A stereochemical-looking
    R/S discrepancy at the bridgehead resolves after restoring the bond, so it is
    not counted as an independent epimer error.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  evidence_ids:
  - synthesis2004
  - synthesis2004-si
  - synthesis2005
  - synthesis2005-si
  - atom-map
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Mint and exact chemical xrefs
  outcome: concern
  summary: The mint is coherent, but PubChem propagates the wrong H22 graph. ChEMBL
    instead supplies a C26 graph and cannot be an exact F link. Correct the named
    structure and every chemical equivalence coherently.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  evidence_ids:
  - chemistry
  - aro
  - pubchem
  - chembl
  - synthesis2004-si
- assessment_id: definition
  area: evidence
  topic: Copied G identity and source pointer
  outcome: concern
  summary: The definition and cited material belong to G/G-H, not F. This requires
    an exact-F rewrite with inspected provenance rather than a letter substitution.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  evidence_ids:
  - native
  - owners
  - adopted2024
  - adopted2017
  - g-figure
- assessment_id: eligibility
  area: scope
  topic: ANTIBACTERIAL placement versus inspected evidence
  outcome: unknown
  summary: The original F lead reports antiviral activity, while the adopted antibacterial
    experiments concern G. No F bacterial growth assay was verified at this reading
    depth. Reassess eligibility after identity correction; this bounded gap does not
    prove antibacterial inactivity or alone mandate deletion.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  evidence_ids:
  - isolation-lead
  - adopted2017
  - adopted2024
  - search
  - synthesis2005
- assessment_id: activity
  area: completeness
  topic: Optional quantitative activity_spectrum
  outcome: unknown
  summary: No such native field is populated. G MICs and F viral EC50 values must
    not be converted into F antibacterial rows, and synthetic antipode/TFA material
    must not silently be treated as neutral natural F. Optional absence is not itself
    a schema error.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  evidence_ids:
  - native
  - adopted2017
  - synthesis2004-si
  - isolation-lead
- assessment_id: mode
  area: completeness
  topic: Mechanism, targets and resistance
  outcome: unknown
  summary: No native molecular claim is populated. The synthesis papers establish
    chemistry and stereochemistry; antiviral family descriptions do not establish
    a direct bacterial protein target, resistance allele or mechanism chain.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  evidence_ids:
  - native
  - synthesis2004
  - synthesis2005
- assessment_id: other
  area: scope
  topic: Producer, clinical, causal and dataset assertions
  outcome: not_applicable
  summary: No structured assertions in these domains occur. The G sponge source in
    the definition cannot be retained as F provenance. No therapeutic approval, clinical
    efficacy or production organism is inferred from isolation or synthesis.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  evidence_ids:
  - native
  - adopted2017
  - isolation-lead
- assessment_id: provenance
  area: provenance
  topic: Maintained ownership and native history
  outcome: supported
  summary: The source row, structure enrichment, one ARO concept and three generated
    events reproduce. All original captures remain preserved among actual-owner inputs.
    SEEDED status is retained.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  evidence_ids:
  - owners
  - aro
  - chemistry
- assessment_id: schema
  area: schema
  topic: Deterministic checks and scientific scope
  outcome: supported
  summary: All focused checks pass; none establishes source-level exact chemical identity
    or detects G-to-F claim transfer.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  evidence_ids:
  - gates
  - atom-map
  - adopted2017
findings:
- finding_id: F1
  issue_key: dragmacidin-f-wrong-pyrrole-hydrogenation
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The stored molecule has a reduced pyrrole and two excess hydrogens
  description: Native/PubChem encode a single bond between fused pyrrole atoms 7/8,
    introducing two CH stereocentres and C25H22BrN7O3. Actual original drawings and
    HRMS require the aromatic pyrrole and neutral C25H20BrN7O3. The mismatch is constitutional
    hydrogenation, not tautomerism, salt choice or merely missing stereochemistry.
    Resolve the exact natural S,S,S structure and chemical grounding before assay
    enrichment.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  - chemical_structure.molecular_formula
  - chemical_structure.average_mass
  - chemical_structure.monoisotopic_mass
  - xrefs[2]
  evidence_ids:
  - native
  - pubchem
  - synthesis2004
  - synthesis2004-si
  - synthesis2005
  - atom-map
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Exact PubChem mapping
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Inherited wrong hydrogenation graph/formula/masses
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure retrieval
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible record generation
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Publication-backed exact structure route if needed
  rule_id: review-checklist:Identity/Structure
  native_severity: blocker
  normalization_reason: The native rubric defines a wrong chemical identity as blocker
    even when deterministic checks pass.
- finding_id: F2
  issue_key: dragmacidin-f-chembl-extra-carbon
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The asserted exact ChEMBL link denotes a C26 compound
  description: CHEMBL4079851 resolves to C26H22BrN7O3/QHEFDEADWAFGNX-YPFXHSDDSA-N.
    It differs in carbon connectivity from both the native C25 graph and the primary
    natural F structure. Remove or replace this chemical equivalence through maintained
    sources after exact structure adjudication; a shared family drawing is insufficient.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  field_paths:
  - xrefs[1]
  evidence_ids:
  - chembl
  - atom-map
  - synthesis2004-si
  - native
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Wrong exact ChEMBL link
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO chemical-xref extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Xref regeneration
  rule_id: review-checklist:Equivalence
  native_severity: major
  normalization_reason: Confirmed wrong exact chemical cross-reference, separately
    actionable from the stored-graph blocker.
- finding_id: F3
  issue_key: dragmacidin-f-definition-is-dragmacidin-g
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The definition and adopted evidence describe G under the F label
  description: The copied definition explicitly names G, including its sulfur side
    chain and MRSA/tuberculosis/Plasmodium/cancer-cell results. The adopted originals
    concern G or G/H. Rewrite with exact F evidence; replacing the letter G with F
    would preserve false claims.
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - native
  - owners
  - aro
  - adopted2024
  - adopted2017
  - g-figure
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: G definition and citations under F
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Definition/source-pointer generation
  rule_id: review-checklist:Evidence/Identity
  native_severity: major
  normalization_reason: Scientific cross-compound claim transfer, not a cosmetic wording
    problem.
actions:
- action_id: A1
  description: Resolve and regenerate the exact natural dragmacidin F graph and chemical
    grounding.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Exact PubChem mapping
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Inherited wrong hydrogenation graph/formula/masses
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure retrieval
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible record generation
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Publication-backed exact structure route if needed
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Reconcile the aromatic pyrrole, neutral C25H20BrN7O3 and measured natural S,S,S
    stereochemistry against actual original drawings and characterization.
  - Treat the scratch repaired key as a diagnostic candidate requiring independent
    full-structure review, including neutral versus TFA/counterion scope.
  - Update all structure fields and non-equivalent PubChem references coherently through
    maintained inputs.
  - Run focused chemistry/schema/strict, source provenance and corpus regeneration
    checks.
- action_id: A2
  description: Correct the non-equivalent ChEMBL cross-reference.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Wrong exact ChEMBL link
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO chemical-xref extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Xref regeneration
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Any retained exact link independently resolves to the adjudicated C25 natural
    F graph and stereochemistry.
  - Do not retain CHEMBL4079851 as an exact chemical equivalent merely because it
    resembles the scaffold.
- action_id: A3
  description: Replace G claims with an exact F definition and evidence scope.
  finding_ids:
  - F3
  target_ids:
  - antibioticmech:aro-6a4094ddb2
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: G definition and citations under F
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Definition/source-pointer generation
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Every retained identity, isolation and biological statement is supported for exact
    F material.
  - Do not transfer G antibacterial results or reinterpret viral assays as bacterial
    growth endpoints.
  - Reassess exact antibacterial eligibility as a separate question after identity
    correction, recording unresolved evidence without claiming inactivity.
limitations:
- The 2004 two-page original was read in full, with actual structural schemes and
  SI final-product/HRMS/counterion pages. The 2005 original was read at absolute-stereochemistry
  and final natural-enantiomer scope with actual Figure 2 and SI S35–S36, not every
  unrelated synthetic-intermediate experiment. Raw spectra were not independently
  reprocessed.
- The original 2000 isolation full text was unavailable through publisher 403/429
  routes; its abstract and the synthesis originals establish the lead scope, but exact
  viral assay conditions and natural counterion remain unverified.
- Adopted 2024 G/H evidence was available at original-abstract depth after publisher
  403. Adopted 2017 G was inspected at full experimental/material scope with the actual
  structure figure. Neither was treated as an F antibacterial assay.
- The diagnostic one-bond repair identifies the hydrogenation defect and reproduces
  three S centres, but it is not a saved or independently finalized replacement structure.
  Exact neutral natural F antibacterial eligibility remains unresolved; no inactivity
  or racemate inference is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native/source/status/history was edited. Optional links, tags and notes were
  checked specifically against dragmacidin F.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://card.mcmaster.ca/ontology/3007778
- https://pubchem.ncbi.nlm.nih.gov/compound/459934
- https://doi.org/10.1021/ja046695b
- https://doi.org/10.1021/ja050586v
tags:
- dragmacidin-f
- chemical-identity
- pyrrole-hydrogenation
- source-conflation
```
