# Evernimicin: misplaced livestock-use claim and constitutionally different ChEMBL link

- Review: 20261021T160624Z-evernimicin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:38:18Z
- Finished UTC: 2026-10-21T16:06:24Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The record is internally coherent and reproduces its PubChem source, but its definition transfers avilamycin livestock-feed use to evernimicin and its ChEMBL cross-reference denotes a different aromatic substituent. Primary ribosome and EmtA evidence supports the named antibiotic within experimental scope. Conflicting original evernitrose anomeric drawings prevent a definitive full-stereochemistry sign-off; they are preserved without an automatic native epimer correction.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 423; one generated exact record. Original thirteen input hashes preserved within 24 expanded inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-985189abb0 | data/antibiotics/antibacterial/evernimicin.yaml | generated | evernimicin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Structured source query before open protein follow-up | passed | False | antibioticmech:aro-985189abb0 | Actual command succeeded; the emtA homonym was not adopted as resistance evidence. |
| Structured source query before open protein follow-up | passed | False | antibioticmech:aro-985189abb0 | Actual command succeeded; the emtA homonym was not adopted as resistance evidence. |
| Focused chemistry verification | passed | False | antibioticmech:aro-985189abb0 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-985189abb0 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-985189abb0 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-985189abb0 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-985189abb0 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-985189abb0 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-985189abb0 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-985189abb0 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-985189abb0 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-985189abb0 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-985189abb0 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-985189abb0 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Constitution and unresolved anomeric source conflict

identity: unknown. Targets: antibioticmech:aro-985189abb0.

The native graph is coherent and matches its current PubChem source. Its terminal aromatic constitution agrees with primary figures. One evernitrose anomeric assignment differs across primary drawings and CCD; full natural-product stereochemical sign-off remains unresolved. No physical racemate or mixture is inferred.

### Same-structure chemical cross-references

grounding: concern. Targets: antibioticmech:aro-985189abb0.

ARO resolves and PubChem reproduces the native graph. ChEMBL5283245 has a different aromatic substituent and formula, violating the explicit same-structure xrefs contract. This is independent of the anomeric source conflict.

### Veterinary and livestock-feed use

evidence: concern. Targets: antibioticmech:aro-985189abb0.

The adopted original distinguishes avilamycin feed use from evernimicin human clinical development. The native definition assigns the former use to the latter compound. The finding does not assert that no veterinary study of evernimicin has ever existed.

### Antibacterial orthosomycin scope

scope: supported. Targets: antibioticmech:aro-985189abb0.

The named antibiotic has direct antibacterial and ribosomal evidence and the native class is structurally coherent. Whole-cell Gram-negative breadth must remain organism-specific; cell-free E. coli translation inhibition is not a Gram-negative susceptibility panel. Exact full-stereo mapping remains qualified separately.

### Sole EmtA imported assertion

evidence: supported. Targets: antibioticmech:aro-985189abb0.

The native assertion is explicitly database-level and correctly typed as target alteration. The original abstract provides enterococcal cloned-gene and rRNA-methylation support. The precise methylated atom is not established by the inspected evidence, and the E. coli homonym is excluded.

### Optional molecular targets, mode and activity_spectrum

completeness: unknown. Targets: antibioticmech:aro-985189abb0.

Primary 50S binding, H89/H91/L16 interaction and tRNA-accommodation evidence is available for bounded enrichment after material identity adjudication. These absent optional fields are not required-schema defects. No numeric activity observation or causal graph is automatically created.

### Producer, clinical product and collection assertions

scope: not_applicable. Targets: antibioticmech:aro-985189abb0.

No producer, FDA product or activity-collection assertion is present. Micromonospora family or everninomicin D biosynthesis cannot be silently transferred to this exact native graph.

### Generated source ownership and history

provenance: supported. Targets: antibioticmech:aro-985189abb0.

All three seeded/reseeded events and actual ARO/PubChem owners were inspected. Original thirteen hashes remain unchanged; source fidelity does not establish correctness of the copied definition or chemical xref.

### Focused native checks

schema: supported. Targets: antibioticmech:aro-985189abb0.

Schema, strict validation, independent native chemistry and source-mint checks pass; source-level scientific findings remain.

## Findings

### F1: The definition transfers avilamycin feed use to evernimicin

major / open / confirmed; issue key: evernimicin-definition-avilamycin-feed-use-transfer.

The cited PMID:27330110 explicitly distinguishes avilamycin as the livestock growth promoter and evernimicin as the former human clinical candidate. The native veterinary/feed statement is therefore not supported by its adopted source. Correct that narrow compound attribution while retaining the supported orthosomycin and antibacterial description.

### F2: The ChEMBL xref denotes a different aromatic constitution

major / open / confirmed; issue key: evernimicin-chembl-aromatic-methyl-hydroxyl-mismatch.

CHEMBL5283245 replaces the terminal nonchlorinated aromatic methyl with hydroxyl, changing C70H97Cl2NO38 to C69H95Cl2NO39. A single scratch atom substitution reproduces its exact key. The native PubChem graph and inspected primary figures retain the methylated ring; remove or correctly remap the incompatible exact xref without replacing the native constitution with the ChEMBL analog.

## Recommended Actions And Acceptance Checks

### A1

Correct the exact compound-use attribution in the maintained ARO-derived definition.

- Distinguish avilamycin livestock growth-promoter use from evernimicin clinical-development history using the adopted original.
- Preserve supported orthosomycin/antibacterial context without turning cell-free E. coli inhibition into broad Gram-negative growth susceptibility.
- Regenerate and run schema, strict, provenance and corpus checks.

### A2

Resolve the constitutionally incompatible ChEMBL chemical xref at its maintained source.

- Remove the incompatible same-structure link or independently verify an exact replacement.
- Compare formula, full graph and stereochemistry; do not overwrite the native methylated ring to match the incorrect link.
- Regenerate and rerun structure/xref checks, schema/strict and corpus validation.

### A3

Adjudicate the evernitrose anomeric source conflict before full natural-product identity sign-off or exact primary assay transfer.

- Retain the explicit C1/InChI 39 map, native/PubChem S, 2000/2016/CCD R and 2010 S counterevidence.
- Inspect original final-product chemical stereochemical evidence, distinguishing SCH27899/Ziracin from everninomicin D and nucleotide-sugar analogs.
- Do not resolve the conflict by majority vote among databases or copied drawings; any future change must remain reproducible and evidence-backed.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/evernimicin.yaml; Entire native YAML, including all three history events | supports | The complete generated record, MINTED identifier, PubChem graph, alternate spelling, orthosomycin class, adopted definition, all three xrefs and sole explicitly qualified EmtA database assertion were read. |
| owners | 423425-raw-rows.json; Exact ARO antibiotic row, ARO resistance edge and PubChem structure row | supports | The actual ARO row owns the definition/classification and imported ChEMBL link. PubChem enrichment owns the native structure. The generic initial ChEBI inventory remains preserved as captured context, but is not claimed as a structural owner. |
| search | 423425-all-local-paths.txt; Ignored- and hidden-inclusive local identifier/name search | context_only | The search covered data, curation, conf, scripts, src, reports and reviews. No exact curator override or additional native activity collection was identified in that scope. External absence is not inferred. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007167; Current ARO:3007167 record and adopted definition | partial | The identifier and label resolve. The current ARO definition reproduces the veterinary/feed wording; reproduction identifies its source owner but does not independently validate its scientific scope. |
| class | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007166; ARO:3007166 orthosomycin antibiotic | supports | The parent and structural-class identifier resolve to orthosomycin antibiotic, coherent with the orthoester-containing oligosaccharide constitution. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6917933/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; Current PubChem CID 6917933 exact property export | supports | Formula C70H97Cl2NO38, neutral charge and key UPADRKHAIMTUCC-OWALTSPQSA-N agree with the native graph, including all 35 specified tetrahedral centres. This is authority agreement, not independent experimental adjudication of the anomeric source conflict. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL5283245.json; Current CHEMBL5283245 molecule graph | refutes | The named ChEMBL entry instead has C69H95Cl2NO39 and key OWWMQNCXYRQWSD-IJBKMQQTSA-N. Its terminal nonchlorinated aromatic methyl is replaced by hydroxyl. It is not the same constitution as the native PubChem graph. |
| chemistry | 423-chemistry.json; 423425-xref-chemistry.json; Independent RDKit 2026.03.5 chemistry with batch 019 interpreter against batch 043 cwd | supports | Native SMILES/InChI, formula, charge, masses and source mint agree. Replacing only native SMILES atom 69, the terminal nonchlorinated aromatic methyl carbon, with hydroxyl oxygen in scratch exactly reproduces the ChEMBL key. A trial on the other aromatic methyl does not. No native edit was made. |
| adopted-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27330110%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; PMID:27330110 / DOI10.1073/pnas.1604790113, original abstract and bibliographic identity | supports | The sole adopted PMID resolves to the 2016 original ribosome study, not a veterinary-use experiment. Its complete original abstract was read. |
| primary2016 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4941455/?pdf=render; PMID:27330110; Introduction, Figure 1, ribosome-binding/accommodation results, EmtA discussion and relevant Methods | partial | The original explicitly assigns livestock growth-promoter use to avilamycin, while evernimicin/SCH27899/Ziracin was a human clinical candidate discontinued in 2000. E. coli ribosome cryo-EM and smFRET support an H89/H91/L16-associated site and interference with late aminoacyl-tRNA accommodation. These are primary mechanism findings; the 3.9-A EVN reconstruction is not a de novo determination of every molecular stereocentre. |
| primary2016-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/67a4/4941455/5f510fe782f4/pnas.1604790113fig01.jpg; Actual original Figure 1B viewed; terminal ringI and evernitrose ringA-prime | partial | RingI visibly has a methyl and two hydroxyl groups, supporting the native aromatic constitution over the ChEMBL alternative. The depicted A-prime anomeric bond gives R by explicit atom mapping, conflicting with native/PubChem S. This drawing conflict is retained separately from the confirmed terminal-substituent mismatch. |
| primary2000 | https://pmc.ncbi.nlm.nih.gov/articles/PMC89832/?pdf=render; PMID:10770739 / DOI10.1128/AAC.44.5.1121-1126.2000; Figure 1, Materials, binding methods and translation results | supports | Schering-Plough evernimicin was studied with E. coli A19 and S. aureus RN450 ribosomes using radioligand binding and cell-free translation. Wild-type E. coli growth insensitivity differs from susceptible modified strain HS227-5 and from cell-free inhibition. These experiments support direct 50S binding and translation inhibition, not broad Gram-negative whole-cell susceptibility. Exact numerical endpoints are not imported into the native record. |
| primary2000-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/ee90/89832/324e23341cf5/ac0500657001.jpg; Actual original Figure 1 viewed, with separately retained magnified anomeric crop | partial | The original structure depicts the same terminal methylated aromatic group. The evernitrose anomeric solid wedge, with the ring rotated relative to the 2016 drawing, maps to R and agrees with that drawing. It is not treated as a new absolute-structure experiment. |
| emta-authority | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3004669; ARO:3004669 identity | supports | The authority identifies the enterococcal EmtA rRNA methyltransferase, consistent with ANTIBIOTIC_TARGET_ALTERATION. The native evidence is correctly labeled a database assertion. |
| emta-primary | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3AEmtA&amp;format=json&amp;resultType=core&amp;pageSize=100; PMID:11580839 / DOI10.1046/j.1365-2958.2001.02602.x, complete original abstract | supports | The original study reports animal-origin E. faecium 9631355, cloned plasmid-borne emtA, impaired evernimicin binding and methylation near G2470. Purified EmtA methylates susceptible 50S subunits more efficiently than resistant ones. This supports target alteration; it does not establish a specific modified atom of G2470. Unrelated mammalian emtA search hits are excluded. |
| emta-access | https://onlinelibrary.wiley.com/doi/10.1046/j.1365-2958.2001.02602.x; Attempted original Wiley full text | context_only | The original publisher returned HTTP 403. Full experimental methods were not inspected; the abstract and 2016 structural discussion provide the bounded retained support. |
| pdb-ligand | https://www.ebi.ac.uk/pdbe/api/pdb/entry/ligand_monomers/5kcs; PDB 5KCS ligand listing | partial | The cited 2016 structure deposits ligand EVN and names its 2,4-dihydroxy-6-methylbenzoyl moiety. This supports the aromatic constitution but does not make the complete ligand graph identical to PubChem. |
| ccd-conflict | https://data.rcsb.org/rest/v1/core/chemcomp/EVN; RCSB EVN chemical component InChI and descriptors | partial | The component has the native formula/connectivity but /t39- rather than native /t39+, yielding UPADRKHAIMTUCC-LRNXXXSBSA-N. It specifies the evernitrose anomeric carbon as R instead of S. A PDB dictionary is not silently substituted for the native graph. |
| primary2010 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2964426/?pdf=render; PMID:20866105 / DOI10.1021/bi101336u; abstract, Introduction, Figure 1 and substrate scope | context_only | This original biosynthesis paper explicitly identifies Figure 1 compound 1 as Ziracin. Its experiments concern ORF36 and TDP-sugar analogs; they do not experimentally redetermine the final antibiotic anomeric centre. That distinction limits the weight of its conflicting structure drawing. |
| primary2010-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8264/2964426/e4a27ef35dab/nihms-241121-f0001.jpg; Actual original Figure 1 evernitrose ring viewed | partial | The anomeric solid wedge at the top of the depicted ring maps to S and agrees with native/PubChem, while conflicting with the 2000/2016 drawings. This counterevidence is retained; no definitive native epimer finding is asserted. |
| primary2016-alt | https://pmc.ncbi.nlm.nih.gov/articles/PMC5098648/?pdf=render; PMID:27791159 / DOI10.1073/pnas.1614297113; Introduction, Figure 1, comparison and model-building methods | partial | The independent D. radiodurans 50S study likewise separates avilamycin feed use from human-directed evernimicin development. It reports 3.58-A EVN structural analysis and describes generation of starting chemical models from prior structures. It does not remove the conflict with the 2010 drawing. |
| primary2016-alt-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8a34/5098648/da39ef48bb52/pnas.1614297113fig01.jpg; Actual original Figure 1A; ringA1 numbered C63 | partial | The numbered evernitrose anomeric C63 maps to InChI atom 39. Its dashed glycosidic bond indicates R, agreeing with the other 2016 figure and CCD. |
| related2018 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/6eef/7231510/c26fb90bbb0d/nihms-1583818-f0001.jpg; PMID:30525509 / DOI10.1021/acs.biochem.8b00836; actual Figure 1A and corresponding full-text caption | context_only | The figure depicts everninomicin D, with a different terminal substitution pattern. Its evernitrose drawing is additional context, not exact-compound evidence for Ziracin and not a transferred producer or antibacterial assay. |
| anomer-map | 423-anomer-map.json; 423-anomer-map.py; Explicit InChI atom 39 mapping and original figure-coordinate interpretation | partial | The centre connects to InChI atoms 19,96 and99. Glycosidic O99 outranks ring O96. The 2000 and two 2016 drawings map to R; the 2010 drawing maps to S. Only this centre differs between native/PubChem and EVN CCD. This is a genuine source conflict requiring original chemical-structure adjudication, not an automatic blocker conclusion. |
| adapter | iModulonDB; 423425-adapter-results.json and exact pre-web catalog/emtA query | context_only | Catalog retrieval and e_coli/precise1k emtA search succeeded. The hit b1193 is lytic murein transglycosylase E, a homonym unrelated to enterococcal EmtA resistance methyltransferase; no iModulon component was returned. No matching Enterococcus or Micromonospora dataset was present. These results are not negative resistance evidence. |
| gates | 423-focused-results.json; Actual schema, strict and independent chemistry executions | supports | All focused checks pass; they do not detect an external constitutional mismatch, misplaced source prose or contradictory published stereodrawings. |

## Limits And Additional Notes

- The sole adopted PMID was resolved and its full original paper was inspected for the named claims, structure figure, mechanism and relevant methods. The 2001 EmtA paper was available at abstract depth only; its publisher returned HTTP 403.
- Original Figure 1 drawings from 2000, 2010 and both 2016 studies were viewed and explicitly mapped. Their anomeric conflict remains unresolved; original final-product chemical stereochemical experiments were not independently recovered and reanalyzed.
- The 2018 biosynthetic figure is everninomicin D and is not exact Ziracin evidence. The 2010 enzyme experiments use nucleotide-sugar analogs, so its final-product drawing cannot alone settle the conflict.
- No exact MIC observation, producer or clinical-use assertion is added. Literature discovery was bounded; the large search result sets were not exhaustively read and do not justify claims of global evidence absence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Native files, maintained inputs and immutable reviews were not edited. Every original input hash was preserved; actual owners were appended and rechecked. Optional links, tags and notes were checked against evernimicin.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T160624Z-evernimicin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Evernimicin: misplaced livestock-use claim and constitutionally different
  ChEMBL link'
started_at: '2026-10-21T15:38:18Z'
finished_at: '2026-10-21T16:06:24Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
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
summary: The record is internally coherent and reproduces its PubChem source, but
  its definition transfers avilamycin livestock-feed use to evernimicin and its ChEMBL
  cross-reference denotes a different aromatic substituent. Primary ribosome and EmtA
  evidence supports the named antibiotic within experimental scope. Conflicting original
  evernitrose anomeric drawings prevent a definitive full-stereochemistry sign-off;
  they are preserved without an automatic native epimer correction.
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
  - path: data/antibiotics/antibacterial/evernimicin.yaml
    sha256: 80c1ec671299a546920c2af0684f95122c8e3602ac9757b348c595890b8e6be5
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
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
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
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-985189abb0
  path: data/antibiotics/antibacterial/evernimicin.yaml
  label: evernimicin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Actual ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO definition, classification, names and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Actual imported resistance assertion
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual PubChem structural grounding
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual PubChem enrichment extractor
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 423; one generated exact record. Original thirteen input
    hashes preserved within 24 expanded inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-985189abb0
checks:
- check_id: adapter-catalog
  name: Structured source query before open protein follow-up
  status: passed
  required: false
  target_ids:
  - antibioticmech:aro-985189abb0
  evidence_ids:
  - adapter
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
  summary: Actual command succeeded; the emtA homonym was not adopted as resistance
    evidence.
- check_id: adapter-emtA
  name: Structured source query before open protein follow-up
  status: passed
  required: false
  target_ids:
  - antibioticmech:aro-985189abb0
  evidence_ids:
  - adapter
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query emtA
  exit_code: 0
  expected_exit_code: 0
  summary: Actual command succeeded; the emtA homonym was not adopted as resistance
    evidence.
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-985189abb0
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/423425-focused.py
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-985189abb0
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/evernimicin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-985189abb0
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/evernimicin.yaml --out /private/tmp/am-review-session/423-strict.tsv
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
  - antibioticmech:aro-985189abb0
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
  - antibioticmech:aro-985189abb0
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
  - antibioticmech:aro-985189abb0
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
  - antibioticmech:aro-985189abb0
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
  - antibioticmech:aro-985189abb0
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
  - antibioticmech:aro-985189abb0
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
  - antibioticmech:aro-985189abb0
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
  - antibioticmech:aro-985189abb0
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
  - antibioticmech:aro-985189abb0
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/evernimicin.yaml
  locator: Entire native YAML, including all three history events
  accessed_at: '2026-10-21T16:05:00Z'
  support: supports
  summary: The complete generated record, MINTED identifier, PubChem graph, alternate
    spelling, orthosomycin class, adopted definition, all three xrefs and sole explicitly
    qualified EmtA database assertion were read.
- evidence_id: owners
  kind: record_content
  reference: 423425-raw-rows.json
  locator: Exact ARO antibiotic row, ARO resistance edge and PubChem structure row
  accessed_at: '2026-10-21T16:05:00Z'
  support: supports
  summary: The actual ARO row owns the definition/classification and imported ChEMBL
    link. PubChem enrichment owns the native structure. The generic initial ChEBI
    inventory remains preserved as captured context, but is not claimed as a structural
    owner.
  snapshot_sha256: 17546d8870410b46645ee7a3caced63be3383d6062cd2167b9a1007fabc163d9
- evidence_id: search
  kind: search
  reference: 423425-all-local-paths.txt
  locator: Ignored- and hidden-inclusive local identifier/name search
  accessed_at: '2026-10-21T16:05:00Z'
  support: context_only
  summary: The search covered data, curation, conf, scripts, src, reports and reviews.
    No exact curator override or additional native activity collection was identified
    in that scope. External absence is not inferred.
  search_scope: rg --no-ignore --hidden -il 'evernimicin|faropenem|ARO:3007167|ARO:3003707|CHEBI:51788|aro-985189abb0'
    data curation conf scripts src reports reviews
  snapshot_sha256: fa3428d9be5b95909e513cc172724911f65611bd1507ceb736c919bbfffecc37
- evidence_id: aro
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007167
  locator: Current ARO:3007167 record and adopted definition
  accessed_at: '2026-10-21T15:54:16.959032Z'
  support: partial
  summary: The identifier and label resolve. The current ARO definition reproduces
    the veterinary/feed wording; reproduction identifies its source owner but does
    not independently validate its scientific scope.
  snapshot_sha256: 7d914b2949abda2b6efed19c19fd9fd69a524d4271495fc69193539ce8ade3c7
- evidence_id: class
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007166
  locator: ARO:3007166 orthosomycin antibiotic
  accessed_at: '2026-10-21T15:54:16.959990Z'
  support: supports
  summary: The parent and structural-class identifier resolve to orthosomycin antibiotic,
    coherent with the orthoester-containing oligosaccharide constitution.
  snapshot_sha256: 8ec00f3362cb04c855eb6a1ea2cdd5931a0f0016203b7411b8f9478fe88d4984
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6917933/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: Current PubChem CID 6917933 exact property export
  accessed_at: '2026-10-21T15:54:17.666359Z'
  support: supports
  summary: Formula C70H97Cl2NO38, neutral charge and key UPADRKHAIMTUCC-OWALTSPQSA-N
    agree with the native graph, including all 35 specified tetrahedral centres. This
    is authority agreement, not independent experimental adjudication of the anomeric
    source conflict.
  snapshot_sha256: 404b80c59fe5e2f5b16d1d96a98f4dc175b4a80d37c22df120fd8e9beec0b3e2
- evidence_id: chembl
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL5283245.json
  locator: Current CHEMBL5283245 molecule graph
  accessed_at: '2026-10-21T15:54:17.671346Z'
  support: refutes
  summary: The named ChEMBL entry instead has C69H95Cl2NO39 and key OWWMQNCXYRQWSD-IJBKMQQTSA-N.
    Its terminal nonchlorinated aromatic methyl is replaced by hydroxyl. It is not
    the same constitution as the native PubChem graph.
  snapshot_sha256: 0b009619e8625a509c19a051d798b1e5a9b75e68c3fee000ee02633d045c2f3b
- evidence_id: chemistry
  kind: record_content
  reference: 423-chemistry.json; 423425-xref-chemistry.json
  locator: Independent RDKit 2026.03.5 chemistry with batch 019 interpreter against
    batch 043 cwd
  accessed_at: '2026-10-21T16:05:00Z'
  support: supports
  summary: Native SMILES/InChI, formula, charge, masses and source mint agree. Replacing
    only native SMILES atom 69, the terminal nonchlorinated aromatic methyl carbon,
    with hydroxyl oxygen in scratch exactly reproduces the ChEMBL key. A trial on
    the other aromatic methyl does not. No native edit was made.
  snapshot_sha256: 8736261f0951fbe6cdf3a95ae9d2256b91453aa63ac9cc7d9d018794bd497b28
- evidence_id: adopted-metadata
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27330110%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: PMID:27330110 / DOI10.1073/pnas.1604790113, original abstract and bibliographic
    identity
  accessed_at: '2026-10-21T15:54:17.690894Z'
  support: supports
  summary: The sole adopted PMID resolves to the 2016 original ribosome study, not
    a veterinary-use experiment. Its complete original abstract was read.
  snapshot_sha256: 343c7eb6f44404171f6b246d0f80be2ed39c4ad093a3dace064f3f3e7a1f165b
- evidence_id: primary2016
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4941455/?pdf=render
  locator: PMID:27330110; Introduction, Figure 1, ribosome-binding/accommodation results,
    EmtA discussion and relevant Methods
  accessed_at: '2026-10-21T09:24:52.750251Z'
  support: partial
  summary: The original explicitly assigns livestock growth-promoter use to avilamycin,
    while evernimicin/SCH27899/Ziracin was a human clinical candidate discontinued
    in 2000. E. coli ribosome cryo-EM and smFRET support an H89/H91/L16-associated
    site and interference with late aminoacyl-tRNA accommodation. These are primary
    mechanism findings; the 3.9-A EVN reconstruction is not a de novo determination
    of every molecular stereocentre.
  snapshot_sha256: 148096b0aabbcf3de62b399077f4f9c023614adad283b74284ccbb1b94b666e9
- evidence_id: primary2016-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/67a4/4941455/5f510fe782f4/pnas.1604790113fig01.jpg
  locator: Actual original Figure 1B viewed; terminal ringI and evernitrose ringA-prime
  accessed_at: '2026-10-21T15:55:50.212288Z'
  support: partial
  summary: RingI visibly has a methyl and two hydroxyl groups, supporting the native
    aromatic constitution over the ChEMBL alternative. The depicted A-prime anomeric
    bond gives R by explicit atom mapping, conflicting with native/PubChem S. This
    drawing conflict is retained separately from the confirmed terminal-substituent
    mismatch.
  snapshot_sha256: c024ef1ed6faac6079b7254b486e76fef92d05384bb3ed68f93326fdad182a92
- evidence_id: primary2000
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC89832/?pdf=render
  locator: PMID:10770739 / DOI10.1128/AAC.44.5.1121-1126.2000; Figure 1, Materials,
    binding methods and translation results
  accessed_at: '2026-10-21T15:55:50.221146Z'
  support: supports
  summary: Schering-Plough evernimicin was studied with E. coli A19 and S. aureus
    RN450 ribosomes using radioligand binding and cell-free translation. Wild-type
    E. coli growth insensitivity differs from susceptible modified strain HS227-5
    and from cell-free inhibition. These experiments support direct 50S binding and
    translation inhibition, not broad Gram-negative whole-cell susceptibility. Exact
    numerical endpoints are not imported into the native record.
  snapshot_sha256: 176adb645fcbd293fc72d73a08ae32eb2aaf0b91d9a6d8f49a78e3a8c4690b4c
- evidence_id: primary2000-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/ee90/89832/324e23341cf5/ac0500657001.jpg
  locator: Actual original Figure 1 viewed, with separately retained magnified anomeric
    crop
  accessed_at: '2026-10-21T16:00:19.561985Z'
  support: partial
  summary: The original structure depicts the same terminal methylated aromatic group.
    The evernitrose anomeric solid wedge, with the ring rotated relative to the 2016
    drawing, maps to R and agrees with that drawing. It is not treated as a new absolute-structure
    experiment.
  snapshot_sha256: 3019da63f43bf027cc74fdeae270d4082e598164e657269bbe514653d3592a31
- evidence_id: emta-authority
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3004669
  locator: ARO:3004669 identity
  accessed_at: '2026-10-21T15:54:16.963095Z'
  support: supports
  summary: The authority identifies the enterococcal EmtA rRNA methyltransferase,
    consistent with ANTIBIOTIC_TARGET_ALTERATION. The native evidence is correctly
    labeled a database assertion.
  snapshot_sha256: b86a6e0944dfff3d6f0ecc8914f2a6ca8776e9d2487e0886f57334c418341f54
- evidence_id: emta-primary
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3AEmtA&format=json&resultType=core&pageSize=100
  locator: PMID:11580839 / DOI10.1046/j.1365-2958.2001.02602.x, complete original
    abstract
  accessed_at: '2026-10-21T15:54:18.873883Z'
  support: supports
  summary: The original study reports animal-origin E. faecium 9631355, cloned plasmid-borne
    emtA, impaired evernimicin binding and methylation near G2470. Purified EmtA methylates
    susceptible 50S subunits more efficiently than resistant ones. This supports target
    alteration; it does not establish a specific modified atom of G2470. Unrelated
    mammalian emtA search hits are excluded.
  snapshot_sha256: 50f435c5f8e81c703c6062dac7e6e70d1b5e1d150bdba10778724b32069de01f
- evidence_id: emta-access
  kind: search
  reference: https://onlinelibrary.wiley.com/doi/10.1046/j.1365-2958.2001.02602.x
  locator: Attempted original Wiley full text
  accessed_at: '2026-10-21T15:55:50.220921Z'
  support: context_only
  summary: The original publisher returned HTTP 403. Full experimental methods were
    not inspected; the abstract and 2016 structural discussion provide the bounded
    retained support.
  snapshot_sha256: d1b711f77a30201e4ea4a475c08efffa3c824ae8cadd938bff56908055f78f20
  search_scope: Exact DOI publisher retrieval following the original EmtA abstract;
    no paid access.
- evidence_id: pdb-ligand
  kind: authority
  reference: https://www.ebi.ac.uk/pdbe/api/pdb/entry/ligand_monomers/5kcs
  locator: PDB 5KCS ligand listing
  accessed_at: '2026-10-21T15:55:50.217751Z'
  support: partial
  summary: The cited 2016 structure deposits ligand EVN and names its 2,4-dihydroxy-6-methylbenzoyl
    moiety. This supports the aromatic constitution but does not make the complete
    ligand graph identical to PubChem.
  snapshot_sha256: d323c4106fa0588de1e2655690250742006abde04cb14a067c765028688c13a2
- evidence_id: ccd-conflict
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/chemcomp/EVN
  locator: RCSB EVN chemical component InChI and descriptors
  accessed_at: '2026-10-21T15:59:16.622145Z'
  support: partial
  summary: The component has the native formula/connectivity but /t39- rather than
    native /t39+, yielding UPADRKHAIMTUCC-LRNXXXSBSA-N. It specifies the evernitrose
    anomeric carbon as R instead of S. A PDB dictionary is not silently substituted
    for the native graph.
  snapshot_sha256: 0e06c0ab772a9cdf47b68e9ae7c51e58c61c62ec7491b42968fc9e02668afb33
- evidence_id: primary2010
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2964426/?pdf=render
  locator: PMID:20866105 / DOI10.1021/bi101336u; abstract, Introduction, Figure 1
    and substrate scope
  accessed_at: '2026-10-21T16:01:18.999044Z'
  support: context_only
  summary: This original biosynthesis paper explicitly identifies Figure 1 compound
    1 as Ziracin. Its experiments concern ORF36 and TDP-sugar analogs; they do not
    experimentally redetermine the final antibiotic anomeric centre. That distinction
    limits the weight of its conflicting structure drawing.
  snapshot_sha256: e175d382a7dab4e8358370c004558be7394b942a8800174738c6fa76b0585a83
- evidence_id: primary2010-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8264/2964426/e4a27ef35dab/nihms-241121-f0001.jpg
  locator: Actual original Figure 1 evernitrose ring viewed
  accessed_at: '2026-10-21T16:01:51.637268Z'
  support: partial
  summary: The anomeric solid wedge at the top of the depicted ring maps to S and
    agrees with native/PubChem, while conflicting with the 2000/2016 drawings. This
    counterevidence is retained; no definitive native epimer finding is asserted.
  snapshot_sha256: b4c00f021eb86755aa6f28e3cbb57defafd20acfcf40b3068903500ad4b7b459
- evidence_id: primary2016-alt
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5098648/?pdf=render
  locator: PMID:27791159 / DOI10.1073/pnas.1614297113; Introduction, Figure 1, comparison
    and model-building methods
  accessed_at: '2026-10-21T16:01:19.000613Z'
  support: partial
  summary: The independent D. radiodurans 50S study likewise separates avilamycin
    feed use from human-directed evernimicin development. It reports 3.58-A EVN structural
    analysis and describes generation of starting chemical models from prior structures.
    It does not remove the conflict with the 2010 drawing.
  snapshot_sha256: fb7452672609c6a8b971b0b79037fd79c0c7642edb3f9ad8f5c2759797052a0e
- evidence_id: primary2016-alt-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8a34/5098648/da39ef48bb52/pnas.1614297113fig01.jpg
  locator: Actual original Figure 1A; ringA1 numbered C63
  accessed_at: '2026-10-21T16:01:51.639129Z'
  support: partial
  summary: The numbered evernitrose anomeric C63 maps to InChI atom 39. Its dashed
    glycosidic bond indicates R, agreeing with the other 2016 figure and CCD.
  snapshot_sha256: 2a19886fea84d4421f0d84d2113ef63773587976f6ba9e698dd884dab7b1a319
- evidence_id: related2018
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/6eef/7231510/c26fb90bbb0d/nihms-1583818-f0001.jpg
  locator: PMID:30525509 / DOI10.1021/acs.biochem.8b00836; actual Figure 1A and corresponding
    full-text caption
  accessed_at: '2026-10-21T16:01:51.634874Z'
  support: context_only
  summary: The figure depicts everninomicin D, with a different terminal substitution
    pattern. Its evernitrose drawing is additional context, not exact-compound evidence
    for Ziracin and not a transferred producer or antibacterial assay.
  snapshot_sha256: 999d050265d71ff3af867f0976214a4ff0c6a478e29a0b1c4408931c223e2922
- evidence_id: anomer-map
  kind: record_content
  reference: 423-anomer-map.json; 423-anomer-map.py
  locator: Explicit InChI atom 39 mapping and original figure-coordinate interpretation
  accessed_at: '2026-10-21T16:05:00Z'
  support: partial
  summary: The centre connects to InChI atoms 19,96 and99. Glycosidic O99 outranks
    ring O96. The 2000 and two 2016 drawings map to R; the 2010 drawing maps to S.
    Only this centre differs between native/PubChem and EVN CCD. This is a genuine
    source conflict requiring original chemical-structure adjudication, not an automatic
    blocker conclusion.
  snapshot_sha256: 0ebdca9a9dbf0ed1e75e0f0453fafa4beeb6fb91f4e770f5d4b95ba298103a22
- evidence_id: adapter
  kind: database
  reference: iModulonDB
  locator: 423425-adapter-results.json and exact pre-web catalog/emtA query
  accessed_at: '2026-10-21T16:05:00Z'
  support: context_only
  summary: Catalog retrieval and e_coli/precise1k emtA search succeeded. The hit b1193
    is lytic murein transglycosylase E, a homonym unrelated to enterococcal EmtA resistance
    methyltransferase; no iModulon component was returned. No matching Enterococcus
    or Micromonospora dataset was present. These results are not negative resistance
    evidence.
  snapshot_sha256: 31734dc364216aa27efa03d6fb4824dfabe84451dfea14c48ebb791c37774af0
- evidence_id: gates
  kind: record_content
  reference: 423-focused-results.json
  locator: Actual schema, strict and independent chemistry executions
  accessed_at: '2026-10-21T16:05:00Z'
  support: supports
  summary: All focused checks pass; they do not detect an external constitutional
    mismatch, misplaced source prose or contradictory published stereodrawings.
  snapshot_sha256: cdfcb0c0a112953453af6770e5eaede375de786706db93793d474a938d7784b7
assessments:
- assessment_id: identity
  area: identity
  topic: Constitution and unresolved anomeric source conflict
  outcome: unknown
  summary: The native graph is coherent and matches its current PubChem source. Its
    terminal aromatic constitution agrees with primary figures. One evernitrose anomeric
    assignment differs across primary drawings and CCD; full natural-product stereochemical
    sign-off remains unresolved. No physical racemate or mixture is inferred.
  target_ids:
  - antibioticmech:aro-985189abb0
  evidence_ids:
  - native
  - pubchem
  - chemistry
  - primary2016-figure
  - primary2000-figure
  - primary2010-figure
  - ccd-conflict
  - anomer-map
- assessment_id: grounding
  area: grounding
  topic: Same-structure chemical cross-references
  outcome: concern
  summary: ARO resolves and PubChem reproduces the native graph. ChEMBL5283245 has
    a different aromatic substituent and formula, violating the explicit same-structure
    xrefs contract. This is independent of the anomeric source conflict.
  target_ids:
  - antibioticmech:aro-985189abb0
  evidence_ids:
  - native
  - aro
  - pubchem
  - chembl
  - chemistry
- assessment_id: definition
  area: evidence
  topic: Veterinary and livestock-feed use
  outcome: concern
  summary: The adopted original distinguishes avilamycin feed use from evernimicin
    human clinical development. The native definition assigns the former use to the
    latter compound. The finding does not assert that no veterinary study of evernimicin
    has ever existed.
  target_ids:
  - antibioticmech:aro-985189abb0
  evidence_ids:
  - native
  - aro
  - primary2016
  - primary2016-alt
  - emta-primary
- assessment_id: classification
  area: scope
  topic: Antibacterial orthosomycin scope
  outcome: supported
  summary: The named antibiotic has direct antibacterial and ribosomal evidence and
    the native class is structurally coherent. Whole-cell Gram-negative breadth must
    remain organism-specific; cell-free E. coli translation inhibition is not a Gram-negative
    susceptibility panel. Exact full-stereo mapping remains qualified separately.
  target_ids:
  - antibioticmech:aro-985189abb0
  evidence_ids:
  - class
  - primary2000
  - primary2016
  - chemistry
- assessment_id: resistance
  area: evidence
  topic: Sole EmtA imported assertion
  outcome: supported
  summary: The native assertion is explicitly database-level and correctly typed as
    target alteration. The original abstract provides enterococcal cloned-gene and
    rRNA-methylation support. The precise methylated atom is not established by the
    inspected evidence, and the E. coli homonym is excluded.
  target_ids:
  - antibioticmech:aro-985189abb0
  evidence_ids:
  - native
  - owners
  - emta-authority
  - emta-primary
  - primary2016
  - adapter
- assessment_id: completeness
  area: completeness
  topic: Optional molecular targets, mode and activity_spectrum
  outcome: unknown
  summary: Primary 50S binding, H89/H91/L16 interaction and tRNA-accommodation evidence
    is available for bounded enrichment after material identity adjudication. These
    absent optional fields are not required-schema defects. No numeric activity observation
    or causal graph is automatically created.
  target_ids:
  - antibioticmech:aro-985189abb0
  evidence_ids:
  - native
  - search
  - primary2000
  - primary2016
  - anomer-map
- assessment_id: other-domains
  area: scope
  topic: Producer, clinical product and collection assertions
  outcome: not_applicable
  summary: No producer, FDA product or activity-collection assertion is present. Micromonospora
    family or everninomicin D biosynthesis cannot be silently transferred to this
    exact native graph.
  target_ids:
  - antibioticmech:aro-985189abb0
  evidence_ids:
  - native
  - search
  - related2018
  - primary2010
- assessment_id: provenance
  area: provenance
  topic: Generated source ownership and history
  outcome: supported
  summary: All three seeded/reseeded events and actual ARO/PubChem owners were inspected.
    Original thirteen hashes remain unchanged; source fidelity does not establish
    correctness of the copied definition or chemical xref.
  target_ids:
  - antibioticmech:aro-985189abb0
  evidence_ids:
  - native
  - owners
  - gates
- assessment_id: validation
  area: schema
  topic: Focused native checks
  outcome: supported
  summary: Schema, strict validation, independent native chemistry and source-mint
    checks pass; source-level scientific findings remain.
  target_ids:
  - antibioticmech:aro-985189abb0
  evidence_ids:
  - gates
  - chemistry
findings:
- finding_id: F1
  issue_key: evernimicin-definition-avilamycin-feed-use-transfer
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The definition transfers avilamycin feed use to evernimicin
  description: The cited PMID:27330110 explicitly distinguishes avilamycin as the
    livestock growth promoter and evernimicin as the former human clinical candidate.
    The native veterinary/feed statement is therefore not supported by its adopted
    source. Correct that narrow compound attribution while retaining the supported
    orthosomycin and antibacterial description.
  target_ids:
  - antibioticmech:aro-985189abb0
  field_paths:
  - definition
  evidence_ids:
  - native
  - aro
  - primary2016
  - primary2016-alt
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Actual ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO definition, classification, names and citation leads
  rule_id: review-checklist:Evidence/Scope
  native_severity: major
  normalization_reason: An adopted definition makes a material compound-specific use
    claim belonging to its comparator.
- finding_id: F2
  issue_key: evernimicin-chembl-aromatic-methyl-hydroxyl-mismatch
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The ChEMBL xref denotes a different aromatic constitution
  description: CHEMBL5283245 replaces the terminal nonchlorinated aromatic methyl
    with hydroxyl, changing C70H97Cl2NO38 to C69H95Cl2NO39. A single scratch atom
    substitution reproduces its exact key. The native PubChem graph and inspected
    primary figures retain the methylated ring; remove or correctly remap the incompatible
    exact xref without replacing the native constitution with the ChEMBL analog.
  target_ids:
  - antibioticmech:aro-985189abb0
  field_paths:
  - xrefs[1]
  evidence_ids:
  - native
  - chembl
  - pubchem
  - chemistry
  - primary2016-figure
  - primary2000-figure
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Actual ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO definition, classification, names and citation leads
  rule_id: review-checklist:Identity/Grounding
  native_severity: major
  normalization_reason: The xrefs field explicitly denotes the same structure, but
    this accession has different atomic composition and connectivity.
actions:
- action_id: A1
  description: Correct the exact compound-use attribution in the maintained ARO-derived
    definition.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-985189abb0
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Actual ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO definition, classification, names and citation leads
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Distinguish avilamycin livestock growth-promoter use from evernimicin clinical-development
    history using the adopted original.
  - Preserve supported orthosomycin/antibacterial context without turning cell-free
    E. coli inhibition into broad Gram-negative growth susceptibility.
  - Regenerate and run schema, strict, provenance and corpus checks.
- action_id: A2
  description: Resolve the constitutionally incompatible ChEMBL chemical xref at its
    maintained source.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-985189abb0
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Actual ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO definition, classification, names and citation leads
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Remove the incompatible same-structure link or independently verify an exact replacement.
  - Compare formula, full graph and stereochemistry; do not overwrite the native methylated
    ring to match the incorrect link.
  - Regenerate and rerun structure/xref checks, schema/strict and corpus validation.
- action_id: A3
  description: Adjudicate the evernitrose anomeric source conflict before full natural-product
    identity sign-off or exact primary assay transfer.
  target_ids:
  - antibioticmech:aro-985189abb0
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual PubChem structural grounding
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual PubChem enrichment extractor
  acceptance_checks:
  - Retain the explicit C1/InChI 39 map, native/PubChem S, 2000/2016/CCD R and 2010
    S counterevidence.
  - Inspect original final-product chemical stereochemical evidence, distinguishing
    SCH27899/Ziracin from everninomicin D and nucleotide-sugar analogs.
  - Do not resolve the conflict by majority vote among databases or copied drawings;
    any future change must remain reproducible and evidence-backed.
  finding_ids: []
limitations:
- The sole adopted PMID was resolved and its full original paper was inspected for
  the named claims, structure figure, mechanism and relevant methods. The 2001 EmtA
  paper was available at abstract depth only; its publisher returned HTTP 403.
- Original Figure 1 drawings from 2000, 2010 and both 2016 studies were viewed and
  explicitly mapped. Their anomeric conflict remains unresolved; original final-product
  chemical stereochemical experiments were not independently recovered and reanalyzed.
- The 2018 biosynthetic figure is everninomicin D and is not exact Ziracin evidence.
  The 2010 enzyme experiments use nucleotide-sugar analogs, so its final-product drawing
  cannot alone settle the conflict.
- No exact MIC observation, producer or clinical-use assertion is added. Literature
  discovery was bounded; the large search result sets were not exhaustively read and
  do not justify claims of global evidence absence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Native files, maintained inputs and immutable reviews were not edited. Every original
  input hash was preserved; actual owners were appended and rechecked. Optional links,
  tags and notes were checked against evernimicin.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.1073/pnas.1604790113
- https://doi.org/10.1128/AAC.44.5.1121-1126.2000
- https://doi.org/10.1021/bi101336u
tags:
- evernimicin
- orthosomycin
- chemical-xref
- primary-source-conflict
```
