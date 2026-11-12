# Tribromopyrrolylmethyl phenol: SMILES defect and qualified primary observations

- Review: 20261021T074702Z-4-3-4-5-tribromo-1h-pyrrol-2-yl-methyl-phenol
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:41:48Z
- Finished UTC: 2026-10-21T07:47:02Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One major defect is confirmed: inherited SMILES omits pyrrole NH and fails chemical parsing despite passing focused native gates. Intended compound identity is supported by valid InChI and primary data. One minor follow-up preserves exact activity/producer evidence while retaining a tenfold source dose conflict and excluding other-metabolite mechanisms.

## Scope And Provenance

Complete exact-record identity, provenance, claim-scope and scientific review.

Selection: Queue index042; exactly CHEBI:218817 in isolated batch005.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:218817 | data/antibiotics/antibacterial/4-3-4-5-tribromo-1h-pyrrol-2-yl-methyl-phenol.yaml | generated | 4-[(3,4,5-tribromo-1H-pyrrol-2-yl)methyl]phenol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema validation | passed | True | CHEBI:218817 | Actual focused native gate passed. |
| Focused strict validation | passed | True | CHEBI:218817 | Actual focused native gate passed. |
| Independent native SMILES/InChI consistency | failed | True | CHEBI:218817 | Native SMILES cannot be sanitized/kekulized; InChI and NH-corrected candidate reproduce the declared identity. |
| Structured expression-source applicability | not_applicable | False | CHEBI:218817 | The native record has no named gene, protein, regulator, pathway, stress response or dataset. The inspected compound1 evidence is chemical isolation and disk activity; other-metabolite pathway speculation is explicitly excluded. |
| Authoritative full QC | failed | True | CHEBI:218817 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:218817 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:218817 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:218817 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:218817 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:218817 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:218817 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:218817 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:218817 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Intended exact molecule

identity: supported. Targets: CHEBI:218817.

Native label, definition, InChI, key, formula, charge and masses identify the exact primary compound1. Cross-reference identity is supported within the inspected descriptors.

### Aromatic pyrrole nitrogen encoding

consistency: concern. Targets: CHEBI:218817.

The native/current-ChEBI SMILES omits required aromatic NH encoding and fails the independent parser. The declared InChI and tested correction agree exactly, narrowing the defect to SMILES representation.

### Antibacterial role and broader classes

grounding: supported. Targets: CHEBI:218817.

The role is an official assertion corroborated by exact compound1 disk activity. Both retained parents are broader valid classes. Current additional phenols parent is context, not evidence that the captured two-parent snapshot is a wrong identity.

### Qualified primary assay observations

completeness: concern. Targets: CHEBI:218817.

Exact primary compound1 positive/negative outcomes are available for bounded activity curation. Preserve the unresolved4versus40microgram/disc conflict, qualitative threshold and absent most isolate identifiers; do not invent MICs, measured zone diameters or susceptibility breakpoints.

### Cultured J010 source

completeness: concern. Targets: CHEBI:218817.

Culture and isolation directly support Pseudoalteromonas sp.J010 as producer and provide a concrete annotation opportunity. The alga is environmental origin.

### Mode and direct target

evidence: unknown. Targets: CHEBI:218817.

No exact-compound molecular mechanism is established by these phenotypic results. Korormicin quorum-sensing and TBP/BAC-A endpoints must remain separate.

### Resistance, clinical, causal graphs and datasets

scope: not_applicable. Targets: CHEBI:218817.

No native assertions in these fields require correction. The source does not justify a resistance determinant from J010 non-inhibition, a clinical claim, a transcriptomic dataset or a lethal causal graph.

### Source ownership and history

provenance: supported. Targets: CHEBI:218817.

The defect is inherited from the adopted/current ChEBI SMILES. Source concept/version and all three seed/reseed events are consistent; no native status promotion was made.

### Focused validation boundary

schema: supported. Targets: CHEBI:218817.

Both native focused validators pass; independent chemical consistency fails separately.

## Findings

### F1: Seeded pyrrole SMILES omits the aromatic NH

major / open / confirmed; issue key: chebi-218817-smiles-missing-pyrrole-nh.

The native SMILES contains pyrrole n without its hydrogen and cannot be kekulized. The declared InChI and primary molecular identity require NH. The exact NH-corrected candidate regenerates every stored chemical identifier and mass. Current ChEBI repeats the same bad SMILES, so a repeatable source correction or extraction safeguard is needed.

### F2: Preserve exact compound1 activity and producer evidence with assay conflict

minor / open / confirmed; issue key: chebi-218817-primary-compound1-observation-disposition.

The adopted primary full text contains exact compound1 disk outcomes and direct J010 culture/isolation evidence that can support qualified annotations. A concrete curator disposition should preserve these observations and the source-internal dose discrepancy. This is not a blanket finding about optional fields or a reason to infer a molecular mechanism.

## Recommended Actions And Acceptance Checks

### A1

Correct the exact source-owned SMILES through an auditable upstream/extractor path and regenerate the target.

- Use the declared valid InChI and exact primary/PubChem identity to adjudicate Oc1ccc(Cc2[nH]c(Br)c(Br)c2Br)cc1; do not apply an indiscriminate n-to-[nH] rewrite.
- Require parsing and equality to WFENRQKTALRFAD-UHFFFAOYSA-N, C11H8Br3NO, charge0 and recorded masses.
- Retain provenance and manifest consistency for any adopted inventory correction; regenerate only the authorized target using documented canary workflow before a broader change.
- Pass focused schema/strict validation plus explicit chemical cross-encoding consistency, provenance, corpus reproducibility and required QC.

### A2

After structure correction, adjudicate claim-level producer and disk activity annotations from the exact compound1 primary source.

- Use PMID:24828288 sections2.2,3.2,3.3 and Table4 at the relevant observation, with the exact compound1 column.
- Retain both40microgram/disc in Table4 and the calculated4microgram/disc from20microlitre of200microgram/mL in Methods until resolved; a qualified qualitative observation may preserve the conflict without choosing a dose.
- Preserve source medium, temperature,24h incubation and positive-zone threshold&gt;10mm; do not invent numeric zones, MICs, breakpoints or unreported isolate accessions.
- Verify NCBITaxon:998465 and its exact label for the J010 producer; do not substitute the algal host or infer a BGC.
- Do not transfer TBP/BAC-A antiprotozoal/antifungal effects, TBP coral morphogenesis or korormicin quorum-sensing speculation to compound1.
- Use native validated writer/history; retain SEEDED until scientific sign-off criteria pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/4-3-4-5-tribromo-1h-pyrrol-2-yl-methyl-phenol.yaml; Entire native YAML | supports | The ChEBI-only record is ANTIBACTERIAL, SEEDED and EXACT. All identity, definition, synonym, two parents, antibacterial role, structure, ChemSpider xref, source concept and three history events were inspected. No mechanism, target, structured activity, resistance, producer, clinical, dataset or causal graph assertions are present. |
| owner | data/raw/chebi_antimicrobials.tsv; CHEBI:218817 row2885; data/antibiotics/PATHS.tsv row523; configuration, MANIFEST, extractor and seeder | supports | The adopted raw row reproduces the same defective SMILES and otherwise matching identity. It cites PMID:24828288, source version2026-08-30 and minted identifier antibioticmech:chebi-33d078838b. No target-specific curator override was found within the ignored-inclusive curation/conf search. Identity corrections belong to the source/extractor/seeder path; scientific observations are curator-owned. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:218817; Official visible identity, structure, roles, parents, names, xref and metabolite species | partial | Current ChEBI repeats Oc1ccc(Cc2nc(Br)c(Br)c2Br)cc1 while giving the native hydrogen-containing InChI, key WFENRQKTALRFAD-UHFFFAOYSA-N, C11H8Br3NO, charge0 and masses. The defect is upstream-reproduced, not an isolated native edit. It also verifies the antibacterial role, pyrroles/organobromine classes, ChemSpider32675069 and Pseudoalteromonas sp.J010 NCBITaxon:998465 with the adopted PMID. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/129850874; PUG-View computed descriptors | supports | PubChem gives the exact same Standard InChI/key, formula and charge and a chemically valid Kekule SMILES C1=CC(=CC=C1CC2=C(C(=C(N2)Br)Br)Br)O, consistent with a pyrrole NH. This is independent structure context, not a new native xref. |
| chemspider | https://www.chemspider.com/Chemical-Structure.32675069.html; Visible official record name, formula, masses and identifier | supports | The native xref resolves to the exact named tribromopyrrolylmethyl phenol, formula C11H8Br3NO, average mass409.903 and exact mass406.815600. The visible page did not expose the full InChIKey; its name/formula/mass agreement complements the independent complete PubChem match. |
| parent-26455 | https://www.ebi.ac.uk/chebi/CHEBI:26455; Official class definition | supports | The parent resolves to pyrroles, a class broader than the intended individual molecule. |
| parent-37141 | https://www.ebi.ac.uk/chebi/CHEBI:37141; Official class definition | supports | The parent resolves to organobromine compound, a class broader than the intended individual molecule. |
| chemistry | RDKit independent structure parsing; Native SMILES and InChI parsed separately; candidate NH encoding; scratch042-chemistry.json | refutes | Native SMILES returns no molecule and reports inability to kekulize. Native InChI parses and regenerates Oc1ccc(Cc2[nH]c(Br)c(Br)c2Br)cc1. That candidate parses and reproduces the native complete InChIKey, formula C11H8Br3NO, charge0, average mass409.903 and exact mass406.815600176. The separate assertion-based sanity command exited1 because native SMILES was unparseable. No native field was changed. |
| primary-identity | PMID:24828288; DOI10.3390/md12052802; https://pmc.ncbi.nlm.nih.gov/articles/PMC4052317/ ; full XML sections2.1,3.2.1 and Table1 | supports | Compound1 is exactly 4-prime-((3,4,5-tribromo-1H-pyrrol-2-yl)methyl)phenol. Spectroscopic elucidation establishes C11H8ONBr3, a para-hydroxybenzyl group and tribrominated pyrrole; it is distinct from TBP, BAC-A and korormicins2-6. The full source supports the intended NH-containing identity without independently re-elucidating all spectra. |
| primary-producer | PMID:24828288; Same primary full XML Introduction, section3.2 and Conclusions | supports | A stock culture of Pseudoalteromonas strainJ010 was grown on marine agar for48h at28C. Ethanol extraction of harvested bacterial colonies and chromatography yielded compound1, reported18.3mg. The coralline alga Neogoniolithon fosliei is the original isolation substrate; it is not the directly cultured producer. This supports a strain-specific producer annotation. |
| primary-activity | PMID:24828288; Same primary full XML section2.2, Table4 column1 and section3.3 | supports | The compound1 column reports positive disk inhibition against the listed Pseudoalteromonas haloplanctis, P.piscicida, P.undina, Pseudomonas aeruginosa, four Vibrio labels, Shewanella aquimarina and Staphylococcus aureus; J010 and Candida albicans are negative. Results are source-specific binary growth-inhibition observations, with media/temperatures in the table and24h incubation plus clearance diameter&gt;10mm threshold in Methods. The table does not give measured zone diameters, MICs or most isolate accessions. J010 non-inhibition is not proof of a resistance mechanism. |
| dose-conflict | PMID:24828288; Same primary full XML Table4 caption versus section3.3 | context_only | Table4 labels the bacterial/fungal assay40microgram per diffusion disc. Methods say compound1 was dissolved in methanol at200microgram/mL and20microlitre evaporated on each6mm disc, which calculates to4microgram/disc. The source therefore has an unresolved tenfold dose discrepancy. Preserve both source statements; do not silently choose one dose or turn the qualitative assay into an MIC. |
| mechanism-boundary | PMID:24828288; Same primary full XML section2.2 and Conclusions | context_only | Quorum-sensing discussion concerns korormicins and is speculative. Protozoan cyst formation/lysis and broad antifungal activity concern TBP or BAC-A, not compound1. Coral metamorphosis in the introduction concerns TBP. Ecological protection of the algal host remains a hypothesis requiring in-vivo evidence. None establishes this compound1 molecular antibacterial target or causal chain. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=998465&amp;mode=Info; Official name/rank information | supports | NCBITaxon:998465 resolves to Pseudoalteromonas sp.J010, a species-ranked unclassified-Pseudoalteromonas taxon. This confirms the source isolate label; it does not establish a formal named species or a BGC. |
| search | CultureBotAI/AntibioticMech; Ignored-inclusive local searches; free primary-source discovery | context_only | The adopted raw row and PATHS are consistent. No existing exact-target curated assertion or override was found in the stated local scopes. Search results about other metabolites or whole-strain extracts were treated only as leads, not compound1 evidence. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Structure, claim-level evidence, activity and producer requirements | supports | Structure encodings must denote the same molecule. Optional fields are not universally required, but inspected exact-compound primary observations create a concrete annotation opportunity. Phenotypic disk inhibition cannot be promoted to a direct target or resistance mechanism. |
| validation | just validate; just validate-strict; Actual batch005 focused runs; scratch042-validation.tsv | supports | Both focused gates exited0: LinkML found no issues and strict scanned one target with zero ERROR rows. These successes do not detect the independent chemical parsing failure. |

## Limits And Additional Notes

- The primary paper contradicts itself on disc dose:40microgram/disc in Table4 versus4microgram/disc calculated from Methods. No exact MIC or measured inhibition-zone diameter is provided by that table.
- Most tested bacterial labels lack isolate accession details in the inspected source. J010 non-inhibition is phenotype context, not an established biochemical resistance route.
- The primary text and structure descriptors were inspected; the blocked publisher image route did not permit an additional visual inspection of Figure1. No independent spectral re-elucidation is claimed.
- ChemSpider visible identity/formula/mass were inspected, while the full key comparison uses independent PubChem and native InChI. Bounded discovery does not establish absence of additional exact-compound research.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Initial capture preceded assessment; all20 captured input hashes were rechecked.
- Current ChEBI repeating the defective encoding does not make it chemically consistent. The correction candidate was tested only in scratch.
- No native record content or scientific status was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T074702Z-4-3-4-5-tribromo-1h-pyrrol-2-yl-methyl-phenol
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Tribromopyrrolylmethyl phenol: SMILES defect and qualified primary observations'
started_at: '2026-10-21T07:41:48Z'
finished_at: '2026-10-21T07:47:02Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not create the seed; entire record, primary full
    text, official identities and independent chemistry were inspected.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'One major defect is confirmed: inherited SMILES omits pyrrole NH and fails
  chemical parsing despite passing focused native gates. Intended compound identity
  is supported by valid InChI and primary data. One minor follow-up preserves exact
  activity/producer evidence while retaining a tenfold source dose conflict and excluding
  other-metabolite mechanisms.'
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
  - path: data/antibiotics/antibacterial/4-3-4-5-tribromo-1h-pyrrol-2-yl-methyl-phenol.yaml
    sha256: c35f32c092b9e9ac74f58e3dd45455216efc1933357870b6c002323f42da9eb9
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
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: data/antibiotics/PATHS.tsv
    sha256: 3b1d82d007878e4aca2c28f4001a468776b325b726da2e48abb76a3dc551cc38
    role: context
targets:
- target_id: CHEBI:218817
  path: data/antibiotics/antibacterial/4-3-4-5-tribromo-1h-pyrrol-2-yl-methyl-phenol.yaml
  label: 4-[(3,4,5-tribromo-1H-pyrrol-2-yl)methyl]phenol
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
  description: Complete exact-record identity, provenance, claim-scope and scientific
    review.
  selection: Queue index042; exactly CHEBI:218817 in isolated batch005.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:218817
  exclusions:
  - target: Tetrabromopyrrole, bromoalterochromide A and korormicins
    reason: Co-isolated compounds are identity/assay boundary context; their mechanisms
      and activities are not transferred.
checks:
- check_id: schema
  name: Focused schema validation
  status: passed
  required: true
  summary: Actual focused native gate passed.
  target_ids:
  - CHEBI:218817
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/4-3-4-5-tribromo-1h-pyrrol-2-yl-methyl-phenol.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Focused strict validation
  status: passed
  required: true
  summary: Actual focused native gate passed.
  target_ids:
  - CHEBI:218817
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/4-3-4-5-tribromo-1h-pyrrol-2-yl-methyl-phenol.yaml
    --out /private/tmp/am-review-session/042-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemical-consistency
  name: Independent native SMILES/InChI consistency
  status: failed
  required: true
  summary: Native SMILES cannot be sanitized/kekulized; InChI and NH-corrected candidate
    reproduce the declared identity.
  target_ids:
  - CHEBI:218817
  command: '.venv/bin/python - <<''PY''

    from pathlib import Path

    import yaml

    from rdkit import Chem

    p=Path(''data/antibiotics/antibacterial/4-3-4-5-tribromo-1h-pyrrol-2-yl-methyl-phenol.yaml'');s=yaml.safe_load(p.read_text())[''chemical_structure''];m=Chem.MolFromSmiles(s[''smiles'']);assert
    m is not None, ''Native SMILES cannot be sanitized/kekulized''

    assert Chem.MolToInchiKey(m)==s[''standard_inchi_key'']

    PY'
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: structured-adapter
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  summary: The native record has no named gene, protein, regulator, pathway, stress
    response or dataset. The inspected compound1 evidence is chemical isolation and
    disk activity; other-metabolite pathway speculation is explicitly excluded.
  target_ids:
  - CHEBI:218817
  evidence_ids:
  - record
  - mechanism-boundary
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:218817
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
  - CHEBI:218817
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
  - CHEBI:218817
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
  - CHEBI:218817
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
  - CHEBI:218817
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
  - CHEBI:218817
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
  - CHEBI:218817
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
  - CHEBI:218817
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
  - CHEBI:218817
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/4-3-4-5-tribromo-1h-pyrrol-2-yl-methyl-phenol.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T07:44:45Z'
  support: supports
  summary: The ChEBI-only record is ANTIBACTERIAL, SEEDED and EXACT. All identity,
    definition, synonym, two parents, antibacterial role, structure, ChemSpider xref,
    source concept and three history events were inspected. No mechanism, target,
    structured activity, resistance, producer, clinical, dataset or causal graph assertions
    are present.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI:218817 row2885; data/antibiotics/PATHS.tsv row523; configuration,
    MANIFEST, extractor and seeder
  accessed_at: '2026-10-21T07:44:45Z'
  support: supports
  summary: The adopted raw row reproduces the same defective SMILES and otherwise
    matching identity. It cites PMID:24828288, source version2026-08-30 and minted
    identifier antibioticmech:chebi-33d078838b. No target-specific curator override
    was found within the ignored-inclusive curation/conf search. Identity corrections
    belong to the source/extractor/seeder path; scientific observations are curator-owned.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:218817
  locator: Official visible identity, structure, roles, parents, names, xref and metabolite
    species
  accessed_at: '2026-10-21T07:42:10Z'
  support: partial
  summary: Current ChEBI repeats Oc1ccc(Cc2nc(Br)c(Br)c2Br)cc1 while giving the native
    hydrogen-containing InChI, key WFENRQKTALRFAD-UHFFFAOYSA-N, C11H8Br3NO, charge0
    and masses. The defect is upstream-reproduced, not an isolated native edit. It
    also verifies the antibacterial role, pyrroles/organobromine classes, ChemSpider32675069
    and Pseudoalteromonas sp.J010 NCBITaxon:998465 with the adopted PMID.
  snapshot_sha256: 81b1a2a5020dcf5941cdf926586bfb871723da78633311e2bb2131cd9f6bc5fb
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/129850874
  locator: PUG-View computed descriptors
  accessed_at: '2026-10-21T07:42:29Z'
  support: supports
  summary: PubChem gives the exact same Standard InChI/key, formula and charge and
    a chemically valid Kekule SMILES C1=CC(=CC=C1CC2=C(C(=C(N2)Br)Br)Br)O, consistent
    with a pyrrole NH. This is independent structure context, not a new native xref.
  snapshot_sha256: 9527c98d035fea81f51a397763137b222afb0b9d275b5ac5f9a7a8f49452081e
- evidence_id: chemspider
  kind: database
  reference: https://www.chemspider.com/Chemical-Structure.32675069.html
  locator: Visible official record name, formula, masses and identifier
  accessed_at: '2026-10-21T07:42:13Z'
  support: supports
  summary: The native xref resolves to the exact named tribromopyrrolylmethyl phenol,
    formula C11H8Br3NO, average mass409.903 and exact mass406.815600. The visible
    page did not expose the full InChIKey; its name/formula/mass agreement complements
    the independent complete PubChem match.
  snapshot_sha256: cd7c2717fb6d8950f0784a2aa3a53cf4393e327292f332b47c142c66c6a875c8
- evidence_id: parent-26455
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:26455
  locator: Official class definition
  accessed_at: '2026-10-21T07:42:31Z'
  support: supports
  summary: The parent resolves to pyrroles, a class broader than the intended individual
    molecule.
  snapshot_sha256: 2f3fa8b09dfdb7c63362a844bc19543190c0b3df71d21c4e4086a6827eabe07b
- evidence_id: parent-37141
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:37141
  locator: Official class definition
  accessed_at: '2026-10-21T07:42:33Z'
  support: supports
  summary: The parent resolves to organobromine compound, a class broader than the
    intended individual molecule.
  snapshot_sha256: a0a8a6bfb21b42a90d643a0314d0f4246047fcfc1b6c0425af9cc481bab21384
- evidence_id: chemistry
  kind: validation
  reference: RDKit independent structure parsing
  locator: Native SMILES and InChI parsed separately; candidate NH encoding; scratch042-chemistry.json
  accessed_at: '2026-10-21T07:42:09Z'
  support: refutes
  summary: Native SMILES returns no molecule and reports inability to kekulize. Native
    InChI parses and regenerates Oc1ccc(Cc2[nH]c(Br)c(Br)c2Br)cc1. That candidate
    parses and reproduces the native complete InChIKey, formula C11H8Br3NO, charge0,
    average mass409.903 and exact mass406.815600176. The separate assertion-based
    sanity command exited1 because native SMILES was unparseable. No native field
    was changed.
  snapshot_sha256: 87b61acc25785a78d007e62b8fcf7b6916e21d1c84531de2eea40c6f833926ed
- evidence_id: primary-identity
  kind: primary_source
  reference: PMID:24828288
  locator: DOI10.3390/md12052802; https://pmc.ncbi.nlm.nih.gov/articles/PMC4052317/
    ; full XML sections2.1,3.2.1 and Table1
  accessed_at: '2026-10-21T07:42:28Z'
  support: supports
  summary: Compound1 is exactly 4-prime-((3,4,5-tribromo-1H-pyrrol-2-yl)methyl)phenol.
    Spectroscopic elucidation establishes C11H8ONBr3, a para-hydroxybenzyl group and
    tribrominated pyrrole; it is distinct from TBP, BAC-A and korormicins2-6. The
    full source supports the intended NH-containing identity without independently
    re-elucidating all spectra.
  snapshot_sha256: 2f646294ba7b7801904519b5d474533b893e88b2fc9d6d749daaa4b9e79374ff
- evidence_id: primary-producer
  kind: primary_source
  reference: PMID:24828288
  locator: Same primary full XML Introduction, section3.2 and Conclusions
  accessed_at: '2026-10-21T07:42:28Z'
  support: supports
  summary: A stock culture of Pseudoalteromonas strainJ010 was grown on marine agar
    for48h at28C. Ethanol extraction of harvested bacterial colonies and chromatography
    yielded compound1, reported18.3mg. The coralline alga Neogoniolithon fosliei is
    the original isolation substrate; it is not the directly cultured producer. This
    supports a strain-specific producer annotation.
  snapshot_sha256: 2f646294ba7b7801904519b5d474533b893e88b2fc9d6d749daaa4b9e79374ff
- evidence_id: primary-activity
  kind: primary_source
  reference: PMID:24828288
  locator: Same primary full XML section2.2, Table4 column1 and section3.3
  accessed_at: '2026-10-21T07:42:28Z'
  support: supports
  summary: The compound1 column reports positive disk inhibition against the listed
    Pseudoalteromonas haloplanctis, P.piscicida, P.undina, Pseudomonas aeruginosa,
    four Vibrio labels, Shewanella aquimarina and Staphylococcus aureus; J010 and
    Candida albicans are negative. Results are source-specific binary growth-inhibition
    observations, with media/temperatures in the table and24h incubation plus clearance
    diameter>10mm threshold in Methods. The table does not give measured zone diameters,
    MICs or most isolate accessions. J010 non-inhibition is not proof of a resistance
    mechanism.
  snapshot_sha256: 2f646294ba7b7801904519b5d474533b893e88b2fc9d6d749daaa4b9e79374ff
- evidence_id: dose-conflict
  kind: primary_source
  reference: PMID:24828288
  locator: Same primary full XML Table4 caption versus section3.3
  accessed_at: '2026-10-21T07:42:28Z'
  support: context_only
  summary: Table4 labels the bacterial/fungal assay40microgram per diffusion disc.
    Methods say compound1 was dissolved in methanol at200microgram/mL and20microlitre
    evaporated on each6mm disc, which calculates to4microgram/disc. The source therefore
    has an unresolved tenfold dose discrepancy. Preserve both source statements; do
    not silently choose one dose or turn the qualitative assay into an MIC.
  snapshot_sha256: 2f646294ba7b7801904519b5d474533b893e88b2fc9d6d749daaa4b9e79374ff
- evidence_id: mechanism-boundary
  kind: primary_source
  reference: PMID:24828288
  locator: Same primary full XML section2.2 and Conclusions
  accessed_at: '2026-10-21T07:42:28Z'
  support: context_only
  summary: Quorum-sensing discussion concerns korormicins and is speculative. Protozoan
    cyst formation/lysis and broad antifungal activity concern TBP or BAC-A, not compound1.
    Coral metamorphosis in the introduction concerns TBP. Ecological protection of
    the algal host remains a hypothesis requiring in-vivo evidence. None establishes
    this compound1 molecular antibacterial target or causal chain.
  snapshot_sha256: 2f646294ba7b7801904519b5d474533b893e88b2fc9d6d749daaa4b9e79374ff
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=998465&mode=Info
  locator: Official name/rank information
  accessed_at: '2026-10-21T07:43:04Z'
  support: supports
  summary: NCBITaxon:998465 resolves to Pseudoalteromonas sp.J010, a species-ranked
    unclassified-Pseudoalteromonas taxon. This confirms the source isolate label;
    it does not establish a formal named species or a BGC.
  snapshot_sha256: 95d67804bf88b1b1209348a753394578779532b97553a8ee59e8569a5024db22
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive local searches; free primary-source discovery
  accessed_at: '2026-10-21T07:44:45Z'
  support: context_only
  summary: The adopted raw row and PATHS are consistent. No existing exact-target
    curated assertion or override was found in the stated local scopes. Search results
    about other metabolites or whole-strain extracts were treated only as leads, not
    compound1 evidence.
  search_scope: prepare.py42 searched batch005 with rg --no-ignore --hidden excluding
    .git/.venv. Follow-up covered raw, curation, conf, scripts, reviews, reports and
    data/antibiotics/PATHS.tsv for218817,the exact key,minted identifier,tribromopyrrole
    name andJ010. Numeric matches to FDA application218817 were unrelated and excluded.
    Public queries combined Pseudoalteromonas,J010,tribromo,phenol and the adopted
    PMID; EPMC full XML was inspected. Hidden and ignored files were included.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Structure, claim-level evidence, activity and producer requirements
  accessed_at: '2026-10-21T07:44:45Z'
  support: supports
  summary: Structure encodings must denote the same molecule. Optional fields are
    not universally required, but inspected exact-compound primary observations create
    a concrete annotation opportunity. Phenotypic disk inhibition cannot be promoted
    to a direct target or resistance mechanism.
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual batch005 focused runs; scratch042-validation.tsv
  accessed_at: '2026-10-21T07:42:05Z'
  support: supports
  summary: 'Both focused gates exited0: LinkML found no issues and strict scanned
    one target with zero ERROR rows. These successes do not detect the independent
    chemical parsing failure.'
  snapshot_sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
assessments:
- assessment_id: identity
  area: identity
  topic: Intended exact molecule
  outcome: supported
  summary: Native label, definition, InChI, key, formula, charge and masses identify
    the exact primary compound1. Cross-reference identity is supported within the
    inspected descriptors.
  target_ids:
  - CHEBI:218817
  evidence_ids:
  - record
  - chebi
  - pubchem
  - chemspider
  - primary-identity
- assessment_id: structure
  area: consistency
  topic: Aromatic pyrrole nitrogen encoding
  outcome: concern
  summary: The native/current-ChEBI SMILES omits required aromatic NH encoding and
    fails the independent parser. The declared InChI and tested correction agree exactly,
    narrowing the defect to SMILES representation.
  target_ids:
  - CHEBI:218817
  evidence_ids:
  - record
  - chebi
  - chemistry
  - pubchem
- assessment_id: classification
  area: grounding
  topic: Antibacterial role and broader classes
  outcome: supported
  summary: The role is an official assertion corroborated by exact compound1 disk
    activity. Both retained parents are broader valid classes. Current additional
    phenols parent is context, not evidence that the captured two-parent snapshot
    is a wrong identity.
  target_ids:
  - CHEBI:218817
  evidence_ids:
  - chebi
  - parent-26455
  - parent-37141
  - primary-activity
- assessment_id: activity
  area: completeness
  topic: Qualified primary assay observations
  outcome: concern
  summary: Exact primary compound1 positive/negative outcomes are available for bounded
    activity curation. Preserve the unresolved4versus40microgram/disc conflict, qualitative
    threshold and absent most isolate identifiers; do not invent MICs, measured zone
    diameters or susceptibility breakpoints.
  target_ids:
  - CHEBI:218817
  evidence_ids:
  - primary-activity
  - dose-conflict
  - rubric
- assessment_id: producer
  area: completeness
  topic: Cultured J010 source
  outcome: concern
  summary: Culture and isolation directly support Pseudoalteromonas sp.J010 as producer
    and provide a concrete annotation opportunity. The alga is environmental origin.
  target_ids:
  - CHEBI:218817
  evidence_ids:
  - primary-producer
  - taxon
  - rubric
- assessment_id: mechanism
  area: evidence
  topic: Mode and direct target
  outcome: unknown
  summary: No exact-compound molecular mechanism is established by these phenotypic
    results. Korormicin quorum-sensing and TBP/BAC-A endpoints must remain separate.
  target_ids:
  - CHEBI:218817
  evidence_ids:
  - record
  - mechanism-boundary
- assessment_id: other
  area: scope
  topic: Resistance, clinical, causal graphs and datasets
  outcome: not_applicable
  summary: No native assertions in these fields require correction. The source does
    not justify a resistance determinant from J010 non-inhibition, a clinical claim,
    a transcriptomic dataset or a lethal causal graph.
  target_ids:
  - CHEBI:218817
  evidence_ids:
  - record
  - primary-activity
  - mechanism-boundary
- assessment_id: provenance
  area: provenance
  topic: Source ownership and history
  outcome: supported
  summary: The defect is inherited from the adopted/current ChEBI SMILES. Source concept/version
    and all three seed/reseed events are consistent; no native status promotion was
    made.
  target_ids:
  - CHEBI:218817
  evidence_ids:
  - record
  - owner
  - chebi
- assessment_id: schema
  area: schema
  topic: Focused validation boundary
  outcome: supported
  summary: Both native focused validators pass; independent chemical consistency fails
    separately.
  target_ids:
  - CHEBI:218817
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-218817-smiles-missing-pyrrole-nh
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Seeded pyrrole SMILES omits the aromatic NH
  description: The native SMILES contains pyrrole n without its hydrogen and cannot
    be kekulized. The declared InChI and primary molecular identity require NH. The
    exact NH-corrected candidate regenerates every stored chemical identifier and
    mass. Current ChEBI repeats the same bad SMILES, so a repeatable source correction
    or extraction safeguard is needed.
  target_ids:
  - CHEBI:218817
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - record
  - owner
  - chebi
  - chemistry
  - pubchem
  - primary-identity
  rule_id: native-review-checklist:Structure;docs/HARMONIZATION.md
  native_severity: major structure consistency defect
  normalization_reason: One structure encoding is chemically invalid despite schema
    success; the intended exact molecule remains recoverable from the valid InChI
    and key, so this is not evidence for a different compound identity.
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
- finding_id: F2
  issue_key: chebi-218817-primary-compound1-observation-disposition
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve exact compound1 activity and producer evidence with assay conflict
  description: The adopted primary full text contains exact compound1 disk outcomes
    and direct J010 culture/isolation evidence that can support qualified annotations.
    A concrete curator disposition should preserve these observations and the source-internal
    dose discrepancy. This is not a blanket finding about optional fields or a reason
    to infer a molecular mechanism.
  target_ids:
  - CHEBI:218817
  field_paths:
  - activity_spectrum
  - producer_organisms
  evidence_ids:
  - primary-producer
  - primary-activity
  - dose-conflict
  - taxon
  - rubric
  rule_id: native-review-checklist:Activity and Producer
  native_severity: minor source-specific annotation opportunity
  normalization_reason: Existing seed assertions are not contradicted; the paper supports
    limited new annotations if dose and source scopes are retained.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/4-3-4-5-tribromo-1h-pyrrol-2-yl-methyl-phenol.yaml
    role: Curator-owned scientific annotations through the validated writer and curation
      history
actions:
- action_id: A1
  description: Correct the exact source-owned SMILES through an auditable upstream/extractor
    path and regenerate the target.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:218817
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
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - Use the declared valid InChI and exact primary/PubChem identity to adjudicate
    Oc1ccc(Cc2[nH]c(Br)c(Br)c2Br)cc1; do not apply an indiscriminate n-to-[nH] rewrite.
  - Require parsing and equality to WFENRQKTALRFAD-UHFFFAOYSA-N, C11H8Br3NO, charge0
    and recorded masses.
  - Retain provenance and manifest consistency for any adopted inventory correction;
    regenerate only the authorized target using documented canary workflow before
    a broader change.
  - Pass focused schema/strict validation plus explicit chemical cross-encoding consistency,
    provenance, corpus reproducibility and required QC.
- action_id: A2
  description: After structure correction, adjudicate claim-level producer and disk
    activity annotations from the exact compound1 primary source.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:218817
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/4-3-4-5-tribromo-1h-pyrrol-2-yl-methyl-phenol.yaml
    role: Curator-owned scientific annotations through the validated writer and curation
      history
  depends_on:
  - A1
  acceptance_checks:
  - Use PMID:24828288 sections2.2,3.2,3.3 and Table4 at the relevant observation,
    with the exact compound1 column.
  - Retain both40microgram/disc in Table4 and the calculated4microgram/disc from20microlitre
    of200microgram/mL in Methods until resolved; a qualified qualitative observation
    may preserve the conflict without choosing a dose.
  - Preserve source medium, temperature,24h incubation and positive-zone threshold>10mm;
    do not invent numeric zones, MICs, breakpoints or unreported isolate accessions.
  - Verify NCBITaxon:998465 and its exact label for the J010 producer; do not substitute
    the algal host or infer a BGC.
  - Do not transfer TBP/BAC-A antiprotozoal/antifungal effects, TBP coral morphogenesis
    or korormicin quorum-sensing speculation to compound1.
  - Use native validated writer/history; retain SEEDED until scientific sign-off criteria
    pass.
limitations:
- The primary paper contradicts itself on disc dose:40microgram/disc in Table4 versus4microgram/disc
  calculated from Methods. No exact MIC or measured inhibition-zone diameter is provided
  by that table.
- Most tested bacterial labels lack isolate accession details in the inspected source.
  J010 non-inhibition is phenotype context, not an established biochemical resistance
  route.
- The primary text and structure descriptors were inspected; the blocked publisher
  image route did not permit an additional visual inspection of Figure1. No independent
  spectral re-elucidation is claimed.
- ChemSpider visible identity/formula/mass were inspected, while the full key comparison
  uses independent PubChem and native InChI. Bounded discovery does not establish
  absence of additional exact-compound research.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Initial capture preceded assessment; all20 captured input hashes were rechecked.
- Current ChEBI repeating the defective encoding does not make it chemically consistent.
  The correction candidate was tested only in scratch.
- No native record content or scientific status was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:218817
- https://pubchem.ncbi.nlm.nih.gov/compound/129850874
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4052317/
tags:
- antibacterial
- smiles
- pyrrole
- source-defect
- primary-assay
- producer
```
