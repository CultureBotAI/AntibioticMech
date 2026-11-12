# Review of CHEBI:140434 (cis-indolyl vinyl isonitrile)

- Review: 20261021T073949Z-chebi-140434-cis-indolyl-vinyl-isonitrile-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:34:21Z
- Finished UTC: 2026-10-21T07:39:49Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One major structure-encoding defect is confirmed: the stored SMILES omits indole [nH] and fails chemical parsing. The official ChEBI Molfile, stored InChI and MIBiG structure converge on the same valid Z entity, allowing a precise source-level repair candidate. One minor evidence-completeness finding identifies original activity and biosynthetic context. MIBiG inherited producer provenance is accurately qualified; neither biosynthetic enzymes nor diffusion assays establish an antimicrobial target.

## Scope And Provenance

Entire record, ChEBI and MIBiG maintained input ownership, all structure/ontology/producer identifiers and existing citation, independent molecular checks, original 1976 diffusion study and 2014/2015 biosynthetic/activity literature.

Selection: Path-ordered unreviewed queue index 040; exactly one record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:140434 | data/antibiotics/antibacterial/3-z-2-isocyanovinyl-indole.yaml | generated | 3-[(Z)-2-isocyanovinyl]indole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:140434 | Exit 0; No issues found. |
| Documented per-record closed-schema validation | passed | True | CHEBI:140434 | Exit 0; one file, zero ERROR rows. |
| Independent structure and minted-identifier comparison | failed | False | CHEBI:140434 | Expected exit 0; exit 1 because the stored SMILES cannot be kekulized. InChI, official Molfile, MIBiG SMILES and [nH] repair candidate agree exactly. |
| Current source term, parent, role and structure comparison | passed | False | CHEBI:140434 | Source IDs, broader parent, role, taxon and adopted MIBiG row provenance assertions pass. Invalid source SMILES are explicitly preserved as a separate failed chemistry check. |
| Structured dataset discovery initial attempt | failed | False | CHEBI:140434 | Exit 2 from sandbox DNS resolution failure; later public-network retry succeeded. |
| Structured dataset discovery public-network retry | passed | False | CHEBI:140434 | Exit 0. Catalog has no Hapalosiphon dataset; a Synechococcus dataset is not a strain-equivalent substitute. No gene/module inference was made for the generic Pseudomonas isolation statement. |
| Authoritative full QC | failed | True | CHEBI:140434 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:140434 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:140434 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:140434 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:140434 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:140434 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:140434 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:140434 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:140434 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Intended cis isonitrile versus broken SMILES

identity: concern. Targets: CHEBI:140434.

The Z identity is supported by InChI, Molfile and primary structure drawing, but the stored SMILES lacks indole [nH] and cannot represent that molecule under normal aromatic parsing. This is not evidence for an E isomer or nitrile replacement.

### Broader parent, aliases and source identity

grounding: supported. Targets: CHEBI:140434.

The geometry-unspecified indolyl vinyl isonitrile parent is strictly broader. Exact ChEBI concept and source mint reproduce, and names fit the supported Z identity.

### Exact external chemical xrefs

grounding: unknown. Targets: CHEBI:140434.

ChEBI confirms inherited CAS61168-06-7 and MetaCycCPD-20769 provenance, but target structure/form content was unavailable directly. No mismatched xref is asserted as established.

### Antibacterial classification and assay scope

evidence: supported. Targets: CHEBI:140434.

Both original B371 diffusion and later compound-resolved disc diffusion support antibacterial activity. They do not supply a standard broth MIC, clinical susceptibility or a direct target.

### MIBiG inheritance and independent biosynthetic support

evidence: supported. Targets: CHEBI:140434.

Adopted taxon/cluster/version and inherited methods are faithfully represented. The source note accurately describes where MIBiG attaches its citation; independently inspected2014 experiments support organism-derived gene function in E.coli. Native free-metabolite accumulation is a narrower unanswered question.

### Primary activity and biosynthetic evidence placement

completeness: concern. Targets: CHEBI:140434.

Concrete source material can enrich evidence/discussion with correct endpoint and production scope. This is not an error merely because optional annotations are empty.

### Biosynthesis versus antimicrobial mode

scope: unknown. Targets: CHEBI:140434.

No molecular antimicrobial target was established in inspected material. The vinyl-isonitrile pharmacophore proposal is an inference; synthases and prenyltransferases make or modify the compound. Both structural consistency and unresolved mode prevent native REVIEWED sign-off.

### Resistance, clinical, graph and dataset fields

representation: not_applicable. Targets: CHEBI:140434.

No such claims are asserted. Relative diffusion response and broad family bioactivity do not justify inventing resistance or clinical annotations.

### Reproducible defect and source-owned producer slice

ownership: supported. Targets: CHEBI:140434.

The structure defect is present in the adopted ChEBI source; the producer object matches maintained MIBiG input and its explicit caveat. Six history events are retained. Future fixes must update their actual maintained owner and regenerate.

### Schema pass versus chemical failure

schema: concern. Targets: CHEBI:140434.

Schema and closed-shape validation pass, while independent molecular parsing fails. The failed expected-zero check is retained, not described as unavailable.

## Findings

### F1: Source-derived SMILES omits indole [nH] and cannot be parsed

major / open / confirmed; issue key: chebi-140434-invalid-smiles-missing-indole-hydrogen.

The stored aromatic n has no hydrogen in a neutral indole ring, causing RDKit kekulization failure. Stored InChI and current official Molfile instead encode the valid NH indole with Z geometry; the separately adopted MIBiG structure agrees. Schema passes do not resolve this conflict. Native REVIEWED structure consistency is blocked.

### F2: Available primary evidence can preserve activity and biosynthesis scope

minor / open / confirmed; issue key: chebi-140434-primary-activity-producer-evidence-completeness.

The seed contains a broad antibacterial definition and qualified database producer object but no activity-level primary evidence. Inspected studies support narrow diffusion observations and organism-derived biosynthetic function. These can be represented without converting diffusion concentrations to MIC or biosynthetic enzymes to antimicrobial targets.

## Recommended Actions And Acceptance Checks

### A1

Repair the maintained source representation and regenerate the record. Candidate valid SMILES: [C-]#[N+]/C=C\c1c[nH]c2ccccc12. The official Molfile, stored InChI and MIBiG encoding all support it.

- Preserve Z geometry and the charge-separated isonitrile; represent indole nitrogen as [nH]. Require a sanitized molecular parse and exact agreement with JQMYMZZLIOIXEO-SREVYHEPSA-N, C11H8N2 and charge0.
- Repair the maintained ChEBI extraction/input policy so reseeding preserves the valid encoding; do not silently replace only the generated YAML or adopt the defective OLS SMILES.
- Recompute dependent structural fields consistently if necessary; do not change the already agreeing InChI/key/formula merely to match the invalid input. Regenerate affected products only in an authorized curation/code pass.
- Run the meaningful chemical consistency check, just validate, just validate-strict, just verify-corpus --summary and just qc; retain a curation history event and leave REVIEWED unset until all native criteria pass.

### A2

Curate narrow primary activity and biosynthesis evidence after resolving the structure defect, retaining the accurate MIBiG source-attachment caveat.

- Keep1976 cup-plate minimum zone-detection concentrations distinct from standard MIC. Keep2015 zones at0.25 µmol/disc distinct from potency concentrations; obtain strain/medium details from accessible supplemental methods before fully specified observations.
- Use the2014 paper for heterologous production by organism-derived welI1-3 genes, not proof of high free-intermediate production in native culture. Do not overwrite imported MIBiG citation-attachment semantics with a broader curator interpretation.
- Retain antimicrobial mechanism as unresolved; no Wel/Amb biosynthetic enzyme or SAR pharmacophore becomes a directly supported molecular target.
- Verify CAS and MetaCyc target-form equivalence when authoritative data become accessible. No xref removal or substitution is justified solely by the access failure.
- Use validated writer/history and appropriate native gates; additional optional fields should be filled only where exact-claim evidence warrants them.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/3-z-2-isocyanovinyl-indole.yaml; Entire generated record | supports | Read label/definition, six aliases, one broader parent, antibacterial role, full structure, two xrefs, source concept, MIBiG producer object and six history events. The producer explicitly marks cluster-inherited methods, questionable quality and a structure-attached reference. No target, mode, activity observation, resistance, clinical, graph or dataset object is asserted. |
| inventory | data/raw/chebi_antimicrobials.tsv; Complete CHEBI:140434 row, roles and manifest; data/raw/mibig_producers.tsv BGC0000668 compound12 row | supports | The invalid SMILES is copied from the adopted ChEBI row, which also supplies matching InChI/key and six citation leads. The MIBiG row independently has a valid Z structure and identical key. Its v5, questionable quality, 12-compound cluster and structure-reference basis reproduce the producer object. |
| ownership | scripts/extract_source_inventory.py; Default ChEBI structure extraction; scripts/seed_from_sources.py structure_from_chebi, attach_mibig_producers, MIBIG_REFERENCE_BASIS and merge; scripts/extract_mibig_producers.py | supports | ChEBI source extraction/maintained inventory and seeding own the invalid imported SMILES. MIBiG producer data have their own extractor/inventory owner; exact-key matching and inherited-method/reference scope are intentional. Do not hand-edit generated identity or relabel a source-attached structure citation as a MIBiG producer-link citation. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:140434; 040-chebi.html, 040-ols.json | partial | The current native entry retains the same missing-[nH] SMILES defect; OLS additionally omits the reverse alkene slash. Both retain the correct InChI/key. Name, aliases, neutral formula/masses and both source xrefs agree with the seed. Matching a defective source string does not establish molecular consistency. |
| molfile | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/140434; Official ChEBI Molfile; 040-molfile.mol | supports | The official Molfile parses successfully and produces the stored InChIKey and Z alkene. Its canonical aromatic serialization includes [nH] and matches the independently valid MIBiG structure and stored InChI. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_140434; 040-ols.json, 040-parents.json and 040-has_role.json | supports | The target is current/non-obsolete. CHEBI:144370 resolves to the geometry-unspecified 3-(2-isocyanovinyl)indole broader class; antibacterial-agent role resolves. Synonym strings correspond to the Z chemical identity supported by the InChI/Molfile. |
| mibig | https://zenodo.org/records/14835872/files/mibig_json_4.0.tar.gz?download=1; Read-only original-checkout cached archive; member BGC0000668.json copied only to scratch as 040-mibig4.json; archive SHA256 d02a387c7d62f8e54d7bcdc03984301e513ce56c1782ecbc9ce957a76039444f | supports | The adopted release member is active version5, questionable quality, Hapalosiphon welwitschii UTEX B1830 taxon1433842, and 12 compounds. Its cis intermediate matches the record key. Locus methods are enzymatic assays and heterologous expression with no linked references; the intermediate citation is under mass-spectrometric structure evidence. This verifies the record note and inherited scope. |
| taxon | https://www.ebi.ac.uk/ols4/api/ontologies/ncbitaxon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FNCBITaxon_1433842; 040-ncbitaxon.json | supports | The non-obsolete strain taxon resolves to Hapalosiphon welwitschii UTEX B 1830, matching the record species label plus separate strain. No taxon mismatch is found. |
| primary1976 | PMID:993124; DOI:10.7164/antibiotics.29.850; full 040-primary1976.pdf, pp.850-852, Table1 and original structure drawing visually inspected | supports | B371 was isolated from Pseudomonas sp. NCIB11237. Spectroscopy supports the cis indole isonitrile. Table1 uses nutrient-agar cup-plate diffusion at 37 C for18 h and reports the lowest applied concentration with a detectable zone, not broth MIC: S. aureus Oxford H strain VI8 µg/mL; E.coli NCIB9482 62; E.coli GlaxoC1343 16; Pseudomonas pyocyanea NCTC8203 &gt;500. These historical organism labels and endpoint must be preserved. |
| primary2014 | DOI:10.1002/cbic.201300794; PMID:24677572; inspected full PMC source text at https://pmc.ncbi.nlm.nih.gov/articles/PMC4382313/; Figure3 and associated Results | supports | The wel cluster was sequenced from H. welwitschii UTEX B1830. Expressing welI1-3 in E.coli generated intermediate10 matching the synthetic cis standard, with no E-isomer observed. This independently supports biosynthetic competence of the organism-derived genes, while not demonstrating abundant free intermediate accumulation in its native culture. It is a biosynthesis result, not antimicrobial target evidence. |
| primary2015 | PMID:29861925; DOI:10.1039/c5sc02919h; full 040-primary2015.xml, Results and Table1 | supports | Parent cis compound1a and halo analogues were tested separately. At0.25 µmol per disc, parent1a gave zone diameters19,38 and29 mm against V.cholerae, E.coli and B.subtilis, respectively. This is disc diffusion, not MIC. The proposed isonitrile pharmacophore is an SAR inference; neither these growth data nor AmbI/WelI biosynthesis establishes a molecular antibacterial target. |
| citation-metadata | Europe PMC core metadata; 040-citations.json; six source-row PMID leads | context_only | All six citation leads resolve. Besides the1976 discovery and2015 analogue study, the other titles concern biosynthetic Cope rearrangement, prenylation, allosteric control and vinyl-isocyanide assembly. Their metadata were checked; their complete texts were not all inspected and their enzymes were not promoted to antimicrobial targets. |
| chemistry | RDKit and hashlib calculations; 040-chemistry.py and 040-chemistry.json | refutes | Stored SMILES fails kekulization. Stored InChI, official ChEBI Molfile, MIBiG SMILES and the minimal [nH] repair all yield JQMYMZZLIOIXEO-SREVYHEPSA-N, C11H8N2, charge0, mass168.199/exact168.068748256 and Z geometry. The minted identifier reproduces. Independent chemical consistency check therefore exits1 as a true failure. |
| source-check | Focused official-source and MIBiG assertions; 040-source-check.py and 040-source-check.json | supports | Parent/role, aliases, InChI/key, taxon and exact adopted MIBiG provenance assertions pass. This check intentionally reports defective source SMILES and does not claim they parse. Direct xref-target content remains inaccessible. |
| validation | just validate; just validate-strict; Actual isolated batch-004 executions; 040-strict.tsv | supports | Both documented per-record schema validators exited0; strict scanned one record with zero ERROR rows. Their success does not catch the independently demonstrated chemical encoding failure. |
| adapter | https://imodulondb.org/api/datasets; Existing kg-microbe-sources runner; 040-imodulondb-datasets.json contains Markdown catalog output despite its filename | context_only | Initial sandbox attempt exited2 on DNS. Public-network retry exited0 before open-ended research and listed no Hapalosiphon dataset. No neighbouring cyanobacterial or generic Pseudomonas dataset was treated as equivalent to the record producer. |
| search | Ignored-inclusive local and bounded free web discovery; 040-local-hits.txt; maintained owner searches, chemical identities, exact DOI and biosynthetic/activity searches | context_only | The original1976 paper and2015 study support antibacterial activity; the record-cited2014 study was read independently for its actual producer scope. CAS/MetaCyc targets could not be directly resolved: Common Chemistry returned an app shell without compound data and MetaCyc a login/subscription page. |

## Limits And Additional Notes

- The full1976 PDF and2015 XML were inspected. The1976 structure drawing and Table1 were checked visually. Publisher retrieval of the2015 PDF and supplement returned403; strain/medium details beyond the inspected main text were not inferred.
- The record-cited2014 complete PMC text was accessible through the web reader; its EPMC XML returned500 and direct HTML download was a challenge page. The latter file is not used as a primary-source snapshot.
- The current MIBiG web entry/JSON URLs failed; the official GitHub copy was an older schema and used only as context. The adopted v4 archive was located by an ignored-inclusive search in the original checkout and read without alteration; its version5 member was independently compared with maintained input.
- Common Chemistry returned an application shell without this compound data, MetaCyc returned login/subscription HTML and direct J-GLOBAL retrieval returned503. The inherited exact external xrefs remain unverified at their target authority.
- Other ChEBI bibliography leads were metadata-checked, not all read in full. Bounded searching did not establish an antimicrobial molecular target. Structural consistency is demonstrably failed, rather than unavailable.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch review artifacts were written. No native record, maintained input, generated artifact or curation history was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T073949Z-chebi-140434-cis-indolyl-vinyl-isonitrile-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of CHEBI:140434 (cis-indolyl vinyl isonitrile)
started_at: '2026-10-21T07:34:21Z'
finished_at: '2026-10-21T07:39:49Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Major invalid source-derived SMILES blocks native REVIEWED structural
  consistency; identity from InChI/Molfile and antibacterial role supported
scientific_review: true
summary: 'One major structure-encoding defect is confirmed: the stored SMILES omits
  indole [nH] and fails chemical parsing. The official ChEBI Molfile, stored InChI
  and MIBiG structure converge on the same valid Z entity, allowing a precise source-level
  repair candidate. One minor evidence-completeness finding identifies original activity
  and biosynthetic context. MIBiG inherited producer provenance is accurately qualified;
  neither biosynthetic enzymes nor diffusion assays establish an antimicrobial target.'
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
  - path: data/antibiotics/antibacterial/3-z-2-isocyanovinyl-indole.yaml
    sha256: 77842cb1f39e34f0cdf2e0f36c40d4dfb140c3fed3dea569bc0ecf24c1165b39
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
scope:
  description: Entire record, ChEBI and MIBiG maintained input ownership, all structure/ontology/producer
    identifiers and existing citation, independent molecular checks, original 1976
    diffusion study and 2014/2015 biosynthetic/activity literature.
  selection: Path-ordered unreviewed queue index 040; exactly one record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:140434
targets:
- target_id: CHEBI:140434
  path: data/antibiotics/antibacterial/3-z-2-isocyanovinyl-indole.yaml
  label: 3-[(Z)-2-isocyanovinyl]indole
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
    role: Adopted producer/BGC claim inventory
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: MIBiG source extraction and exact structure producer matching
checks:
- check_id: schema
  name: Documented per-record LinkML validation
  status: passed
  required: true
  summary: Exit 0; No issues found.
  target_ids:
  - CHEBI:140434
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/3-z-2-isocyanovinyl-indole.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented per-record closed-schema validation
  status: passed
  required: true
  summary: Exit 0; one file, zero ERROR rows.
  target_ids:
  - CHEBI:140434
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/3-z-2-isocyanovinyl-indole.yaml --out /private/tmp/am-review-session/040-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Independent structure and minted-identifier comparison
  status: failed
  required: false
  summary: Expected exit 0; exit 1 because the stored SMILES cannot be kekulized.
    InChI, official Molfile, MIBiG SMILES and [nH] repair candidate agree exactly.
  target_ids:
  - CHEBI:140434
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/040-chemistry.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-check
  name: Current source term, parent, role and structure comparison
  status: passed
  required: false
  summary: Source IDs, broader parent, role, taxon and adopted MIBiG row provenance
    assertions pass. Invalid source SMILES are explicitly preserved as a separate
    failed chemistry check.
  target_ids:
  - CHEBI:140434
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/040-source-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ontology
  - source-check
- check_id: imodulondb-first-attempt
  name: Structured dataset discovery initial attempt
  status: failed
  required: false
  summary: Exit 2 from sandbox DNS resolution failure; later public-network retry
    succeeded.
  target_ids:
  - CHEBI:140434
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run --project
    /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 2
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: imodulondb-datasets
  name: Structured dataset discovery public-network retry
  status: passed
  required: false
  summary: Exit 0. Catalog has no Hapalosiphon dataset; a Synechococcus dataset is
    not a strain-equivalent substitute. No gene/module inference was made for the
    generic Pseudomonas isolation statement.
  target_ids:
  - CHEBI:140434
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 datasets > /private/tmp/am-review-session/040-imodulondb-datasets.json
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:140434
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
  - CHEBI:140434
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
  - CHEBI:140434
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
  - CHEBI:140434
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
  - CHEBI:140434
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
  - CHEBI:140434
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
  - CHEBI:140434
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
  - CHEBI:140434
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
  - CHEBI:140434
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/3-z-2-isocyanovinyl-indole.yaml
  locator: Entire generated record
  accessed_at: '2026-10-21T07:39:09Z'
  support: supports
  summary: Read label/definition, six aliases, one broader parent, antibacterial role,
    full structure, two xrefs, source concept, MIBiG producer object and six history
    events. The producer explicitly marks cluster-inherited methods, questionable
    quality and a structure-attached reference. No target, mode, activity observation,
    resistance, clinical, graph or dataset object is asserted.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Complete CHEBI:140434 row, roles and manifest; data/raw/mibig_producers.tsv
    BGC0000668 compound12 row
  accessed_at: '2026-10-21T07:39:09Z'
  support: supports
  summary: The invalid SMILES is copied from the adopted ChEBI row, which also supplies
    matching InChI/key and six citation leads. The MIBiG row independently has a valid
    Z structure and identical key. Its v5, questionable quality, 12-compound cluster
    and structure-reference basis reproduce the producer object.
- evidence_id: ownership
  kind: record_content
  reference: scripts/extract_source_inventory.py
  locator: Default ChEBI structure extraction; scripts/seed_from_sources.py structure_from_chebi,
    attach_mibig_producers, MIBIG_REFERENCE_BASIS and merge; scripts/extract_mibig_producers.py
  accessed_at: '2026-10-21T07:39:09Z'
  support: supports
  summary: ChEBI source extraction/maintained inventory and seeding own the invalid
    imported SMILES. MIBiG producer data have their own extractor/inventory owner;
    exact-key matching and inherited-method/reference scope are intentional. Do not
    hand-edit generated identity or relabel a source-attached structure citation as
    a MIBiG producer-link citation.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:140434
  locator: 040-chebi.html, 040-ols.json
  accessed_at: '2026-10-21T07:39:09Z'
  support: partial
  summary: The current native entry retains the same missing-[nH] SMILES defect; OLS
    additionally omits the reverse alkene slash. Both retain the correct InChI/key.
    Name, aliases, neutral formula/masses and both source xrefs agree with the seed.
    Matching a defective source string does not establish molecular consistency.
  snapshot_sha256: 3645f6ec3f863bebc3fc0fc55f04177d776954c617e190f3cb3525666fa3aff9
- evidence_id: molfile
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/140434
  locator: Official ChEBI Molfile; 040-molfile.mol
  accessed_at: '2026-10-21T07:39:09Z'
  support: supports
  summary: The official Molfile parses successfully and produces the stored InChIKey
    and Z alkene. Its canonical aromatic serialization includes [nH] and matches the
    independently valid MIBiG structure and stored InChI.
  snapshot_sha256: 583e7a876d11695ed6b8fc617a9559319c8037af9e011e53fc67af7997000aa7
- evidence_id: ontology
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_140434
  locator: 040-ols.json, 040-parents.json and 040-has_role.json
  accessed_at: '2026-10-21T07:39:09Z'
  support: supports
  summary: The target is current/non-obsolete. CHEBI:144370 resolves to the geometry-unspecified
    3-(2-isocyanovinyl)indole broader class; antibacterial-agent role resolves. Synonym
    strings correspond to the Z chemical identity supported by the InChI/Molfile.
  snapshot_sha256: 4a39e00e10270564cf8b7252d99f462c55ac715c42009810941f32a96efc13bd
- evidence_id: mibig
  kind: database
  reference: https://zenodo.org/records/14835872/files/mibig_json_4.0.tar.gz?download=1
  locator: Read-only original-checkout cached archive; member BGC0000668.json copied
    only to scratch as 040-mibig4.json; archive SHA256 d02a387c7d62f8e54d7bcdc03984301e513ce56c1782ecbc9ce957a76039444f
  accessed_at: '2026-10-21T07:39:09Z'
  support: supports
  summary: The adopted release member is active version5, questionable quality, Hapalosiphon
    welwitschii UTEX B1830 taxon1433842, and 12 compounds. Its cis intermediate matches
    the record key. Locus methods are enzymatic assays and heterologous expression
    with no linked references; the intermediate citation is under mass-spectrometric
    structure evidence. This verifies the record note and inherited scope.
  snapshot_sha256: cebbf3a80dd3eb5699df94e3ac7d461c046e4dd91b75d258e7fb85518edfdb54
- evidence_id: taxon
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/ncbitaxon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FNCBITaxon_1433842
  locator: 040-ncbitaxon.json
  accessed_at: '2026-10-21T07:39:09Z'
  support: supports
  summary: The non-obsolete strain taxon resolves to Hapalosiphon welwitschii UTEX
    B 1830, matching the record species label plus separate strain. No taxon mismatch
    is found.
  snapshot_sha256: b6ab308f702618661497da623f4f85f750a76be9a3525fb079024f66e492676f
- evidence_id: primary1976
  kind: primary_source
  reference: PMID:993124
  locator: DOI:10.7164/antibiotics.29.850; full 040-primary1976.pdf, pp.850-852, Table1
    and original structure drawing visually inspected
  accessed_at: '2026-10-21T07:39:09Z'
  support: supports
  summary: 'B371 was isolated from Pseudomonas sp. NCIB11237. Spectroscopy supports
    the cis indole isonitrile. Table1 uses nutrient-agar cup-plate diffusion at 37
    C for18 h and reports the lowest applied concentration with a detectable zone,
    not broth MIC: S. aureus Oxford H strain VI8 µg/mL; E.coli NCIB9482 62; E.coli
    GlaxoC1343 16; Pseudomonas pyocyanea NCTC8203 >500. These historical organism
    labels and endpoint must be preserved.'
  snapshot_sha256: cf365f8032a11e0d8491fd97eb2242cf842c2da8340ee863f0ee834fa6892e05
- evidence_id: primary2014
  kind: primary_source
  reference: DOI:10.1002/cbic.201300794
  locator: PMID:24677572; inspected full PMC source text at https://pmc.ncbi.nlm.nih.gov/articles/PMC4382313/;
    Figure3 and associated Results
  accessed_at: '2026-10-21T07:39:09Z'
  support: supports
  summary: The wel cluster was sequenced from H. welwitschii UTEX B1830. Expressing
    welI1-3 in E.coli generated intermediate10 matching the synthetic cis standard,
    with no E-isomer observed. This independently supports biosynthetic competence
    of the organism-derived genes, while not demonstrating abundant free intermediate
    accumulation in its native culture. It is a biosynthesis result, not antimicrobial
    target evidence.
- evidence_id: primary2015
  kind: primary_source
  reference: PMID:29861925
  locator: DOI:10.1039/c5sc02919h; full 040-primary2015.xml, Results and Table1
  accessed_at: '2026-10-21T07:39:09Z'
  support: supports
  summary: Parent cis compound1a and halo analogues were tested separately. At0.25
    µmol per disc, parent1a gave zone diameters19,38 and29 mm against V.cholerae,
    E.coli and B.subtilis, respectively. This is disc diffusion, not MIC. The proposed
    isonitrile pharmacophore is an SAR inference; neither these growth data nor AmbI/WelI
    biosynthesis establishes a molecular antibacterial target.
  snapshot_sha256: 82fcb64165907e08fc2de1289f3a759d030a2862cf53f8c4ce02611befef93c8
- evidence_id: citation-metadata
  kind: primary_source
  reference: Europe PMC core metadata
  locator: 040-citations.json; six source-row PMID leads
  accessed_at: '2026-10-21T07:39:09Z'
  support: context_only
  summary: All six citation leads resolve. Besides the1976 discovery and2015 analogue
    study, the other titles concern biosynthetic Cope rearrangement, prenylation,
    allosteric control and vinyl-isocyanide assembly. Their metadata were checked;
    their complete texts were not all inspected and their enzymes were not promoted
    to antimicrobial targets.
  snapshot_sha256: 1a05a0bf31d4706a6d885ea58bf9836360e13b990b755854a9e2ee453d2ed3b5
- evidence_id: chemistry
  kind: validation
  reference: RDKit and hashlib calculations
  locator: 040-chemistry.py and 040-chemistry.json
  accessed_at: '2026-10-21T07:39:09Z'
  support: refutes
  summary: Stored SMILES fails kekulization. Stored InChI, official ChEBI Molfile,
    MIBiG SMILES and the minimal [nH] repair all yield JQMYMZZLIOIXEO-SREVYHEPSA-N,
    C11H8N2, charge0, mass168.199/exact168.068748256 and Z geometry. The minted identifier
    reproduces. Independent chemical consistency check therefore exits1 as a true
    failure.
  snapshot_sha256: 504f5ead0e37a5b616310ba0f905f6403d8f920e13fa61a604909b6767604fb6
- evidence_id: source-check
  kind: validation
  reference: Focused official-source and MIBiG assertions
  locator: 040-source-check.py and 040-source-check.json
  accessed_at: '2026-10-21T07:39:09Z'
  support: supports
  summary: Parent/role, aliases, InChI/key, taxon and exact adopted MIBiG provenance
    assertions pass. This check intentionally reports defective source SMILES and
    does not claim they parse. Direct xref-target content remains inaccessible.
  snapshot_sha256: 139d32f849bef896d055f9d1bca8efb69401537a2ecadaafafc463752c7e621f
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual isolated batch-004 executions; 040-strict.tsv
  accessed_at: '2026-10-21T07:39:09Z'
  support: supports
  summary: Both documented per-record schema validators exited0; strict scanned one
    record with zero ERROR rows. Their success does not catch the independently demonstrated
    chemical encoding failure.
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Existing kg-microbe-sources runner; 040-imodulondb-datasets.json contains
    Markdown catalog output despite its filename
  accessed_at: '2026-10-21T07:39:09Z'
  support: context_only
  summary: Initial sandbox attempt exited2 on DNS. Public-network retry exited0 before
    open-ended research and listed no Hapalosiphon dataset. No neighbouring cyanobacterial
    or generic Pseudomonas dataset was treated as equivalent to the record producer.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and bounded free web discovery
  locator: 040-local-hits.txt; maintained owner searches, chemical identities, exact
    DOI and biosynthetic/activity searches
  accessed_at: '2026-10-21T07:39:09Z'
  support: context_only
  summary: 'The original1976 paper and2015 study support antibacterial activity; the
    record-cited2014 study was read independently for its actual producer scope. CAS/MetaCyc
    targets could not be directly resolved: Common Chemistry returned an app shell
    without compound data and MetaCyc a login/subscription page.'
  search_scope: prepare.py40 searched identifier, label and slug with rg --no-ignore
    --hidden, excluding only .git and .venv. Follow-up exact-ID, minted-ID, CPD-20769
    and BGC0000668 searches examined maintained inputs/conf and legacy reviews. Ignored-inclusive
    search located the original MIBiG archive, which was read without modification.
    Free web queries included cis-indolyl vinyl isonitrile mechanism, B371 antibiotic,
    exact label/DOI, official ontology/taxonomy/MIBiG and CAS/MetaCyc. J-GLOBAL search
    results were only leads because direct retrieval returned503. No target was inferred
    from a congener or biosynthetic enzyme.
assessments:
- assessment_id: identity
  area: identity
  topic: Intended cis isonitrile versus broken SMILES
  outcome: concern
  summary: The Z identity is supported by InChI, Molfile and primary structure drawing,
    but the stored SMILES lacks indole [nH] and cannot represent that molecule under
    normal aromatic parsing. This is not evidence for an E isomer or nitrile replacement.
  target_ids:
  - CHEBI:140434
  evidence_ids:
  - record
  - molfile
  - chemistry
  - primary1976
- assessment_id: grounding
  area: grounding
  topic: Broader parent, aliases and source identity
  outcome: supported
  summary: The geometry-unspecified indolyl vinyl isonitrile parent is strictly broader.
    Exact ChEBI concept and source mint reproduce, and names fit the supported Z identity.
  target_ids:
  - CHEBI:140434
  evidence_ids:
  - ontology
  - inventory
  - chemistry
- assessment_id: xref
  area: grounding
  topic: Exact external chemical xrefs
  outcome: unknown
  summary: ChEBI confirms inherited CAS61168-06-7 and MetaCycCPD-20769 provenance,
    but target structure/form content was unavailable directly. No mismatched xref
    is asserted as established.
  target_ids:
  - CHEBI:140434
  evidence_ids:
  - record
  - chebi
  - search
- assessment_id: classification
  area: evidence
  topic: Antibacterial classification and assay scope
  outcome: supported
  summary: Both original B371 diffusion and later compound-resolved disc diffusion
    support antibacterial activity. They do not supply a standard broth MIC, clinical
    susceptibility or a direct target.
  target_ids:
  - CHEBI:140434
  evidence_ids:
  - primary1976
  - primary2015
- assessment_id: producer
  area: evidence
  topic: MIBiG inheritance and independent biosynthetic support
  outcome: supported
  summary: Adopted taxon/cluster/version and inherited methods are faithfully represented.
    The source note accurately describes where MIBiG attaches its citation; independently
    inspected2014 experiments support organism-derived gene function in E.coli. Native
    free-metabolite accumulation is a narrower unanswered question.
  target_ids:
  - CHEBI:140434
  evidence_ids:
  - mibig
  - taxon
  - primary2014
  - record
- assessment_id: activity
  area: completeness
  topic: Primary activity and biosynthetic evidence placement
  outcome: concern
  summary: Concrete source material can enrich evidence/discussion with correct endpoint
    and production scope. This is not an error merely because optional annotations
    are empty.
  target_ids:
  - CHEBI:140434
  evidence_ids:
  - record
  - primary1976
  - primary2014
  - primary2015
- assessment_id: mechanism
  area: scope
  topic: Biosynthesis versus antimicrobial mode
  outcome: unknown
  summary: No molecular antimicrobial target was established in inspected material.
    The vinyl-isonitrile pharmacophore proposal is an inference; synthases and prenyltransferases
    make or modify the compound. Both structural consistency and unresolved mode prevent
    native REVIEWED sign-off.
  target_ids:
  - CHEBI:140434
  evidence_ids:
  - primary2014
  - primary2015
  - citation-metadata
  - chemistry
- assessment_id: optional
  area: representation
  topic: Resistance, clinical, graph and dataset fields
  outcome: not_applicable
  summary: No such claims are asserted. Relative diffusion response and broad family
    bioactivity do not justify inventing resistance or clinical annotations.
  target_ids:
  - CHEBI:140434
  evidence_ids:
  - record
  - primary1976
  - primary2015
- assessment_id: provenance
  area: ownership
  topic: Reproducible defect and source-owned producer slice
  outcome: supported
  summary: The structure defect is present in the adopted ChEBI source; the producer
    object matches maintained MIBiG input and its explicit caveat. Six history events
    are retained. Future fixes must update their actual maintained owner and regenerate.
  target_ids:
  - CHEBI:140434
  evidence_ids:
  - inventory
  - ownership
  - mibig
- assessment_id: schema-assessment
  area: schema
  topic: Schema pass versus chemical failure
  outcome: concern
  summary: Schema and closed-shape validation pass, while independent molecular parsing
    fails. The failed expected-zero check is retained, not described as unavailable.
  target_ids:
  - CHEBI:140434
  evidence_ids:
  - validation
  - chemistry
  - source-check
findings:
- finding_id: F1
  issue_key: chebi-140434-invalid-smiles-missing-indole-hydrogen
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Source-derived SMILES omits indole [nH] and cannot be parsed
  description: The stored aromatic n has no hydrogen in a neutral indole ring, causing
    RDKit kekulization failure. Stored InChI and current official Molfile instead
    encode the valid NH indole with Z geometry; the separately adopted MIBiG structure
    agrees. Schema passes do not resolve this conflict. Native REVIEWED structure
    consistency is blocked.
  target_ids:
  - CHEBI:140434
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - record
  - inventory
  - chebi
  - molfile
  - chemistry
  rule_id: 'review-checklist: Structure and REVIEWED gate criteria1-2'
  native_severity: major molecular-encoding inconsistency and native REVIEWED blocker
  normalization_reason: A core structural field is chemically invalid and inconsistent
    with the supported exact entity. The defect is consequential despite passing schema
    checks; there is no evidence the other encodings or Z identity need changing.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI structure input for CHEBI:140434
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI extraction/default-structure transform
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproduce corrected source structure in generated record
- finding_id: F2
  issue_key: chebi-140434-primary-activity-producer-evidence-completeness
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Available primary evidence can preserve activity and biosynthesis scope
  description: The seed contains a broad antibacterial definition and qualified database
    producer object but no activity-level primary evidence. Inspected studies support
    narrow diffusion observations and organism-derived biosynthetic function. These
    can be represented without converting diffusion concentrations to MIC or biosynthetic
    enzymes to antimicrobial targets.
  target_ids:
  - CHEBI:140434
  field_paths:
  - evidence
  - activity_spectrum
  - discussions
  - mode_of_action_notes
  evidence_ids:
  - record
  - primary1976
  - primary2014
  - primary2015
  rule_id: 'review-checklist: Evidence standard, Activity, Producer and Mode of action'
  native_severity: minor actionable primary-evidence completeness gap
  normalization_reason: Concrete sources support useful enrichment. The existing MIBiG
    scope caveat is accurate and is not classified as a false producer citation.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-z-2-isocyanovinyl-indole.yaml
    role: Curator-owned claim evidence, activity context and discussion through validated
      writer/history; imported MIBiG source slice retains its documented owner
actions:
- action_id: A1
  description: 'Repair the maintained source representation and regenerate the record.
    Candidate valid SMILES: [C-]#[N+]/C=C\c1c[nH]c2ccccc12. The official Molfile,
    stored InChI and MIBiG encoding all support it.'
  finding_ids:
  - F1
  target_ids:
  - CHEBI:140434
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI structure input for CHEBI:140434
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI extraction/default-structure transform
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproduce corrected source structure in generated record
  acceptance_checks:
  - Preserve Z geometry and the charge-separated isonitrile; represent indole nitrogen
    as [nH]. Require a sanitized molecular parse and exact agreement with JQMYMZZLIOIXEO-SREVYHEPSA-N,
    C11H8N2 and charge0.
  - Repair the maintained ChEBI extraction/input policy so reseeding preserves the
    valid encoding; do not silently replace only the generated YAML or adopt the defective
    OLS SMILES.
  - Recompute dependent structural fields consistently if necessary; do not change
    the already agreeing InChI/key/formula merely to match the invalid input. Regenerate
    affected products only in an authorized curation/code pass.
  - Run the meaningful chemical consistency check, just validate, just validate-strict,
    just verify-corpus --summary and just qc; retain a curation history event and
    leave REVIEWED unset until all native criteria pass.
- action_id: A2
  description: Curate narrow primary activity and biosynthesis evidence after resolving
    the structure defect, retaining the accurate MIBiG source-attachment caveat.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:140434
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-z-2-isocyanovinyl-indole.yaml
    role: Curator-owned claim evidence, activity context and discussion through validated
      writer/history; imported MIBiG source slice retains its documented owner
  acceptance_checks:
  - Keep1976 cup-plate minimum zone-detection concentrations distinct from standard
    MIC. Keep2015 zones at0.25 µmol/disc distinct from potency concentrations; obtain
    strain/medium details from accessible supplemental methods before fully specified
    observations.
  - Use the2014 paper for heterologous production by organism-derived welI1-3 genes,
    not proof of high free-intermediate production in native culture. Do not overwrite
    imported MIBiG citation-attachment semantics with a broader curator interpretation.
  - Retain antimicrobial mechanism as unresolved; no Wel/Amb biosynthetic enzyme or
    SAR pharmacophore becomes a directly supported molecular target.
  - Verify CAS and MetaCyc target-form equivalence when authoritative data become
    accessible. No xref removal or substitution is justified solely by the access
    failure.
  - Use validated writer/history and appropriate native gates; additional optional
    fields should be filled only where exact-claim evidence warrants them.
limitations:
- The full1976 PDF and2015 XML were inspected. The1976 structure drawing and Table1
  were checked visually. Publisher retrieval of the2015 PDF and supplement returned403;
  strain/medium details beyond the inspected main text were not inferred.
- The record-cited2014 complete PMC text was accessible through the web reader; its
  EPMC XML returned500 and direct HTML download was a challenge page. The latter file
  is not used as a primary-source snapshot.
- The current MIBiG web entry/JSON URLs failed; the official GitHub copy was an older
  schema and used only as context. The adopted v4 archive was located by an ignored-inclusive
  search in the original checkout and read without alteration; its version5 member
  was independently compared with maintained input.
- Common Chemistry returned an application shell without this compound data, MetaCyc
  returned login/subscription HTML and direct J-GLOBAL retrieval returned503. The
  inherited exact external xrefs remain unverified at their target authority.
- Other ChEBI bibliography leads were metadata-checked, not all read in full. Bounded
  searching did not establish an antimicrobial molecular target. Structural consistency
  is demonstrably failed, rather than unavailable.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Only scratch review artifacts were written. No native record, maintained input,
  generated artifact or curation history was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:140434
- https://www.ebi.ac.uk/chebi/backend/api/public/molfile/140434
- https://doi.org/10.7164/antibiotics.29.850
- https://doi.org/10.1002/cbic.201300794
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4382313/
- https://doi.org/10.1039/c5sc02919h
- https://zenodo.org/records/14835872
tags:
- record-review
- invalid-smiles
- cis-isonitrile
- producer-evidence-scope
- biosynthesis-versus-target
```
