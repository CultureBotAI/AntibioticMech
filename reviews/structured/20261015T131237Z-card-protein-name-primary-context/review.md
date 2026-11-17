# Primary evidence scope for six CARD protein-name candidates

- Review: 20261015T131237Z-card-protein-name-primary-context
- Repository: culturebotai/AntibioticMech
- Started UTC: 2026-10-15T12:57:32Z
- Finished UTC: 2026-10-15T13:12:37Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Six reference candidates remain non-experimental. Four scoped findings require evidence qualification or further primary review; no biological records changed.

## Scope And Provenance

Only the eight CARD claims linked to six pending protein-name candidates; not whole-record review.

Selection: All six pending candidates from the pinned 720-term name screen, with all eight affected corpus records.
Coverage: partial; 8 reviewed / 2939 in the declared population.
Source: working_tree at Git base 8f0dc555d7b4b683610fae7945f22bd6e9fb5105.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:100241 | data/antibiotics/antibacterial/ciprofloxacin.yaml | generated | ciprofloxacin |
| CHEBI:59064 | data/antibiotics/antibacterial/colistin-a.yaml | generated | colistin A |
| CHEBI:59673 | data/antibiotics/antibacterial/colistin-b.yaml | generated | colistin B |
| CHEBI:42355 | data/antibiotics/antibacterial/erythromycin-a.yaml | generated | erythromycin A |
| CHEBI:8269 | data/antibiotics/antibacterial/pleuromutilin.yaml | generated | pleuromutilin |
| CHEBI:8732 | data/antibiotics/antibacterial/quinupristin.yaml | generated | quinupristin |
| antibioticmech:aro-be005cca98 | data/antibiotics/antibacterial/tunicamycin.yaml | generated | tunicamycin |
| CHEBI:28001 | data/antibiotics/antibacterial/vancomycin.yaml | generated | vancomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Collection-aware source and identity binding | passed | True | CHEBI:100241, CHEBI:59064, CHEBI:59673, CHEBI:42355, CHEBI:8269, CHEBI:8732, antibioticmech:aro-be005cca98, CHEBI:28001 | Offline replay checks 2939 record hashes, reads eight complete records, and binds eight CARD claims to source rows. |
| Full primary result and supplement coverage | unavailable | True | CHEBI:100241, CHEBI:59064, CHEBI:59673, CHEBI:42355, CHEBI:8269, CHEBI:8732, antibioticmech:aro-be005cca98, CHEBI:28001 | Coverage varies from primary text to abstracts and citation identity; figure, supplement and complete-result review is unfinished. |
| Experimental allele and genome grounding | unavailable | True | CHEBI:100241, CHEBI:59064, CHEBI:59673, CHEBI:42355, CHEBI:8269, CHEBI:8732, antibioticmech:aro-be005cca98, CHEBI:28001 | Reference UniProt/TaxID identities do not resolve experimental alleles, subjects or genomes. |
| Authoritative repository QC | unavailable | True | CHEBI:100241, CHEBI:59064, CHEBI:59673, CHEBI:42355, CHEBI:8269, CHEBI:8732, antibioticmech:aro-be005cca98, CHEBI:28001 | Not rerun: RDKit absent; locked 2026.3.5 has no Intel macOS wheel or source distribution in this lockfile. |

## Scientific And Domain Assessments

### QnrB65

grounding: unknown. Targets: CHEBI:100241.

CITATION_IDENTITY_ONLY_PRIMARY_RESULTS_UNAVAILABLE

Interpretation and pending action: research/2026-10-15-card-protein-name-evidence-assessments.json#/reviews/ARO:3002777

### msrC

grounding: concern. Targets: CHEBI:42355, CHEBI:8732.

FUNCTIONAL_ASSOCIATION_WITH_CAUSAL_AND_MECHANISM_LIMITS

Interpretation and pending action: research/2026-10-15-card-protein-name-evidence-assessments.json#/reviews/ARO:3002819

### eatAv

grounding: concern. Targets: CHEBI:8269.

FUNCTIONAL_ALLELE_CONTEXT_WITH_EXACT_COMPOUND_SCOPE_GAP

Interpretation and pending action: research/2026-10-15-card-protein-name-evidence-assessments.json#/reviews/ARO:3003761

### D-Ala-D-Ala ligase

grounding: concern. Targets: CHEBI:28001.

GENERIC_LIGASE_REFERENCE_NOT_A_TESTED_RESISTANT_ALLELE

Interpretation and pending action: research/2026-10-15-card-protein-name-evidence-assessments.json#/reviews/ARO:3003970

### tunicamycin resistance protein

grounding: unknown. Targets: antibioticmech:aro-be005cca98.

ABSTRACT_ONLY_REFERENCE_CONTEXT_PRIMARY_RESULTS_PENDING

Interpretation and pending action: research/2026-10-15-card-protein-name-evidence-assessments.json#/reviews/ARO:3004285

### MCR-4.3

grounding: concern. Targets: CHEBI:59064, CHEBI:59673.

CONTEXT_SPECIFIC_NEGATIVE_EVIDENCE_REQUIRES_QUALIFICATION

Interpretation and pending action: research/2026-10-15-card-protein-name-evidence-assessments.json#/reviews/ARO:3004695

## Findings

### mcr43-context: Negative functional evidence requires a scoped qualification

major / open / confirmed; issue key: card-protein-name-mcr43-context.

The MCR-4.3 source edges lack the context-specific negative-evidence qualification documented in the dossier. Neither universal inactivity nor component-specific resistance is established.

### eatav-compound: Tested derivative does not ground the parent compound

major / open / confirmed; issue key: card-protein-name-eatav-compound.

The inspected eatAv experiment does not supply an exact-compound crosswalk for this source edge. Class membership cannot replace structure-specific evidence.

### msrc-evidence: Early association does not establish the current mechanistic classification

minor / open / confirmed; issue key: card-protein-name-msrc-evidence.

The early cited study is insufficient to prove exclusive causality or the current target-protection classification. This does not establish that CARD's classification is wrong.

### ddl-scope: Generic enzyme identity leaves the tested alteration unresolved

minor / open / confirmed; issue key: card-protein-name-ddl-scope.

The generic ligase reference does not resolve the alteration-dependent source context. Abstract-only review cannot support an experimental allele assignment.

## Recommended Actions And Acceptance Checks

### review-mcr43-context

Review remaining later functional reports before a source-owned qualification; preserve contrasting contexts, original provenance, and the separation of colistin A and B.

- Resolve the scoped evidence gap without inferring an experimental accession or transferring a reference taxon.
- Preserve source ownership, exact compound identity, contradictory evidence and unchanged unrelated claims.
- Any biological change must reproduce from a maintained source-owned input, use the validated writer and curation event, and pass authoritative QC.

### review-eatav-compound

Resolve exact compound evidence and the experimental accession crosswalk before promoting this reference or curating an activity observation.

- Resolve the scoped evidence gap without inferring an experimental accession or transferring a reference taxon.
- Preserve source ownership, exact compound identity, contradictory evidence and unchanged unrelated claims.
- Any biological change must reproduce from a maintained source-owned input, use the validated writer and curation event, and pass authoritative QC.

### review-msrc-evidence

Check later mechanistic evidence and compound form before a source-owned qualification; do not invent the missing native gene field.

- Resolve the scoped evidence gap without inferring an experimental accession or transferring a reference taxon.
- Preserve source ownership, exact compound identity, contradictory evidence and unchanged unrelated claims.
- Any biological change must reproduce from a maintained source-owned input, use the validated writer and curation event, and pass authoritative QC.

### review-ddl-scope

Review primary results and the source term's entity scope before assigning any experimental allele.

- Resolve the scoped evidence gap without inferring an experimental accession or transferring a reference taxon.
- Preserve source ownership, exact compound identity, contradictory evidence and unchanged unrelated claims.
- Any biological change must reproduce from a maintained source-owned input, use the validated writer and curation event, and pass authoritative QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| mcr-original | https://journals.asm.org/doi/10.1128/JCM.01562-17; Letter, functional-result paragraph and concluding paragraph; HTML table interpretations only | refutes | The letter reports no independent polymyxin-resistance effect for its historical mcr-4.2 label, despite variable isolate phenotypes. |
| mcr-followup | https://journals.asm.org/doi/10.1128/aac.00649-18; Text, naming paragraph and functional-result conclusions preceding Figure 2; figures not visually reviewed | refutes | The later study identifies the renamed MCR-4.3 allele and reports negative colistin-resistance and lipid-A-modification results in its tested contexts. |
| mcr-naming | https://academic.oup.com/jac/article/73/10/2625/5055843; Indexed naming proposal; detailed naming table unavailable through the web reader | context_only | This PMID identifies the nomenclature proposal, not the separate AAC.00649-18 functional study. |
| mcr-later-context | https://journals.asm.org/doi/10.1128/aac.00133-19; Results and Discussion, initial isolate-identification subsection; supplements not inspected | context_only | A later report describes resistant Acinetobacter and susceptible Shewanella carriers; co-occurrence does not establish allele causality. |
| msrc | https://journals.asm.org/doi/10.1128/aac.45.1.263-266.2001; Results and Discussion, concluding paragraph | partial | Susceptibility changes allow a downstream-gene contribution; the proposed efflux mechanism remains a hypothesis. |
| eatav | https://journals.asm.org/doi/10.1128/aac.01030-13; Reciprocal-replacement results, Table 3 headers and Discussion; no quantitative AST extraction | partial | Functional genetic evidence supports an LSAP phenotype, but the tested pleuromutilin was tiamulin and the biochemical mechanism remained unresolved. |
| eatav-genome | https://journals.asm.org/doi/10.1128/jb.00259-12; Aus0004 reference-genome results; also matched by cached UniProt bibliography | context_only | Aus0004 supplies reference-genome context, not the tested derivative's identity. |
| ddl-primary | https://onlinelibrary.wiley.com/doi/abs/10.1110/ps.39101; Abstract; full results and figures not obtained | partial | The abstract concerns inactivated ligases in glycopeptide-dependent isolates, not generic ddl presence. |
| ddl-review | https://academic.oup.com/cid/article-abstract/42/Supplement_1/S25/275393; Abstract explicitly describing a review | context_only | This is a review article, not a second allele-specific primary experiment. |
| tmrb | https://journals.asm.org/doi/10.1128/jb.174.13.4302-4307.1992; Abstract; full paper available as advertised PDF but not inspected here | partial | The abstract supports ATP-binding and membrane association; full mechanism and experimental subject identity remain unresolved. |
| qnrb65 | https://journals.asm.org/doi/10.1128/aac.01849-13; Journal issue 58(2), letter identity; no allele-specific results obtained | unknown | Citation identity agrees, but no allele-specific primary result was obtained. |
| local-bindings | research/2026-10-15-card-protein-name-evidence.json | supports | Eight live CARD claim positions and hashes bind to eight source rows; six reference identities remain non-experimental. |

## Limits And Additional Notes

- The web reader returned internal errors, without HTTP status, for initial opens of QnrB65, msrC, eatAv, the reference-genome paper, the ddl full-text page, and the Europe PMC metadata query. These are not documented HTTP 403 responses.
- Publisher-indexed text was subsequently available for msrC, eatAv and the reference-genome paper. QnrB65 opens remained unavailable. The naming-proposal find operations also returned internal errors.
- No native primary article files were cached; primary assessments are dated human-readable web-text observations, not offline replay of article bodies.
- No figures, supplements or rendered tables were visually verified. No MIC values or resistance breakpoints were newly curated.
- The nomenclature proposal's exact PMID-to-DOI identity was checked against existing local Europe PMC discovery metadata. No NCBI request was made.
- A later clinical Acinetobacter report at https://academic.oup.com/jac/article/75/1/60/5580312 remains an unreviewed lead after a web-reader internal error; no universal MCR-4.3 activity conclusion is made.
- All inherited access holds remain in force. No held article was retried, and NCBI AST/#1040 and reuse-terms review remain deferred.
- No whole-record primary signoff, biological curation, AST import, source adoption, GitHub mutation or NCBI request.
- The full-corpus goal remains open; a validated review is not scientific status promotion.
- Evidence timestamps mark final inspection of the available source text and assessment; the web reader does not expose exact underlying fetch timestamps.
- A protected baseline was frozen before research; the source inspection rebinds the unchanged target bytes.
- Do not reinterpret the prior CARD target-protection classification as an efflux claim; the historical paper's uncertainty is retained.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
actions:
- acceptance_checks:
  - Resolve the scoped evidence gap without inferring an experimental accession or
    transferring a reference taxon.
  - Preserve source ownership, exact compound identity, contradictory evidence and
    unchanged unrelated claims.
  - Any biological change must reproduce from a maintained source-owned input, use
    the validated writer and curation event, and pass authoritative QC.
  action_id: review-mcr43-context
  description: Review remaining later functional reports before a source-owned qualification;
    preserve contrasting contexts, original provenance, and the separation of colistin
    A and B.
  finding_ids:
  - mcr43-context
  generator: scripts/seed_from_sources.py
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  target_ids:
  - CHEBI:59064
  - CHEBI:59673
- acceptance_checks:
  - Resolve the scoped evidence gap without inferring an experimental accession or
    transferring a reference taxon.
  - Preserve source ownership, exact compound identity, contradictory evidence and
    unchanged unrelated claims.
  - Any biological change must reproduce from a maintained source-owned input, use
    the validated writer and curation event, and pass authoritative QC.
  action_id: review-eatav-compound
  description: Resolve exact compound evidence and the experimental accession crosswalk
    before promoting this reference or curating an activity observation.
  finding_ids:
  - eatav-compound
  generator: scripts/seed_from_sources.py
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  target_ids:
  - CHEBI:8269
- acceptance_checks:
  - Resolve the scoped evidence gap without inferring an experimental accession or
    transferring a reference taxon.
  - Preserve source ownership, exact compound identity, contradictory evidence and
    unchanged unrelated claims.
  - Any biological change must reproduce from a maintained source-owned input, use
    the validated writer and curation event, and pass authoritative QC.
  action_id: review-msrc-evidence
  description: Check later mechanistic evidence and compound form before a source-owned
    qualification; do not invent the missing native gene field.
  finding_ids:
  - msrc-evidence
  generator: scripts/seed_from_sources.py
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  target_ids:
  - CHEBI:42355
  - CHEBI:8732
- acceptance_checks:
  - Resolve the scoped evidence gap without inferring an experimental accession or
    transferring a reference taxon.
  - Preserve source ownership, exact compound identity, contradictory evidence and
    unchanged unrelated claims.
  - Any biological change must reproduce from a maintained source-owned input, use
    the validated writer and curation event, and pass authoritative QC.
  action_id: review-ddl-scope
  description: Review primary results and the source term's entity scope before assigning
    any experimental allele.
  finding_ids:
  - ddl-scope
  generator: scripts/seed_from_sources.py
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  target_ids:
  - CHEBI:28001
assessments:
- area: grounding
  assessment_id: ARO-3002777
  details: 'Interpretation and pending action: research/2026-10-15-card-protein-name-evidence-assessments.json#/reviews/ARO:3002777'
  evidence_ids:
  - qnrb65
  - local-bindings
  outcome: unknown
  summary: CITATION_IDENTITY_ONLY_PRIMARY_RESULTS_UNAVAILABLE
  target_ids:
  - CHEBI:100241
  topic: QnrB65
- area: grounding
  assessment_id: ARO-3002819
  details: 'Interpretation and pending action: research/2026-10-15-card-protein-name-evidence-assessments.json#/reviews/ARO:3002819'
  evidence_ids:
  - msrc
  - local-bindings
  outcome: concern
  summary: FUNCTIONAL_ASSOCIATION_WITH_CAUSAL_AND_MECHANISM_LIMITS
  target_ids:
  - CHEBI:42355
  - CHEBI:8732
  topic: msrC
- area: grounding
  assessment_id: ARO-3003761
  details: 'Interpretation and pending action: research/2026-10-15-card-protein-name-evidence-assessments.json#/reviews/ARO:3003761'
  evidence_ids:
  - eatav
  - eatav-genome
  - local-bindings
  outcome: concern
  summary: FUNCTIONAL_ALLELE_CONTEXT_WITH_EXACT_COMPOUND_SCOPE_GAP
  target_ids:
  - CHEBI:8269
  topic: eatAv
- area: grounding
  assessment_id: ARO-3003970
  details: 'Interpretation and pending action: research/2026-10-15-card-protein-name-evidence-assessments.json#/reviews/ARO:3003970'
  evidence_ids:
  - ddl-primary
  - ddl-review
  - local-bindings
  outcome: concern
  summary: GENERIC_LIGASE_REFERENCE_NOT_A_TESTED_RESISTANT_ALLELE
  target_ids:
  - CHEBI:28001
  topic: D-Ala-D-Ala ligase
- area: grounding
  assessment_id: ARO-3004285
  details: 'Interpretation and pending action: research/2026-10-15-card-protein-name-evidence-assessments.json#/reviews/ARO:3004285'
  evidence_ids:
  - tmrb
  - local-bindings
  outcome: unknown
  summary: ABSTRACT_ONLY_REFERENCE_CONTEXT_PRIMARY_RESULTS_PENDING
  target_ids:
  - antibioticmech:aro-be005cca98
  topic: tunicamycin resistance protein
- area: grounding
  assessment_id: ARO-3004695
  details: 'Interpretation and pending action: research/2026-10-15-card-protein-name-evidence-assessments.json#/reviews/ARO:3004695'
  evidence_ids:
  - mcr-original
  - mcr-followup
  - mcr-naming
  - mcr-later-context
  - local-bindings
  outcome: concern
  summary: CONTEXT_SPECIFIC_NEGATIVE_EVIDENCE_REQUIRES_QUALIFICATION
  target_ids:
  - CHEBI:59064
  - CHEBI:59673
  topic: MCR-4.3
checks:
- check_id: live-bindings
  evidence_ids:
  - local-bindings
  name: Collection-aware source and identity binding
  required: true
  status: passed
  summary: Offline replay checks 2939 record hashes, reads eight complete records,
    and binds eight CARD claims to source rows.
  target_ids:
  - CHEBI:100241
  - CHEBI:59064
  - CHEBI:59673
  - CHEBI:42355
  - CHEBI:8269
  - CHEBI:8732
  - antibioticmech:aro-be005cca98
  - CHEBI:28001
- check_id: primary-coverage
  name: Full primary result and supplement coverage
  required: true
  status: unavailable
  summary: Coverage varies from primary text to abstracts and citation identity; figure,
    supplement and complete-result review is unfinished.
  target_ids:
  - CHEBI:100241
  - CHEBI:59064
  - CHEBI:59673
  - CHEBI:42355
  - CHEBI:8269
  - CHEBI:8732
  - antibioticmech:aro-be005cca98
  - CHEBI:28001
- check_id: experimental-identity
  name: Experimental allele and genome grounding
  required: true
  status: unavailable
  summary: Reference UniProt/TaxID identities do not resolve experimental alleles,
    subjects or genomes.
  target_ids:
  - CHEBI:100241
  - CHEBI:59064
  - CHEBI:59673
  - CHEBI:42355
  - CHEBI:8269
  - CHEBI:8732
  - antibioticmech:aro-be005cca98
  - CHEBI:28001
- check_id: full-qc
  name: Authoritative repository QC
  required: true
  status: unavailable
  summary: 'Not rerun: RDKit absent; locked 2026.3.5 has no Intel macOS wheel or source
    distribution in this lockfile.'
  target_ids:
  - CHEBI:100241
  - CHEBI:59064
  - CHEBI:59673
  - CHEBI:42355
  - CHEBI:8269
  - CHEBI:8732
  - antibioticmech:aro-be005cca98
  - CHEBI:28001
completion: partial
evidence:
- accessed_at: '2026-10-15T13:12:37Z'
  evidence_id: mcr-original
  kind: primary_source
  locator: Letter, functional-result paragraph and concluding paragraph; HTML table
    interpretations only
  reference: https://journals.asm.org/doi/10.1128/JCM.01562-17
  summary: The letter reports no independent polymyxin-resistance effect for its historical
    mcr-4.2 label, despite variable isolate phenotypes.
  support: refutes
- accessed_at: '2026-10-15T13:12:37Z'
  evidence_id: mcr-followup
  kind: primary_source
  locator: Text, naming paragraph and functional-result conclusions preceding Figure
    2; figures not visually reviewed
  reference: https://journals.asm.org/doi/10.1128/aac.00649-18
  summary: The later study identifies the renamed MCR-4.3 allele and reports negative
    colistin-resistance and lipid-A-modification results in its tested contexts.
  support: refutes
- accessed_at: '2026-10-15T13:12:37Z'
  evidence_id: mcr-naming
  kind: authority
  locator: Indexed naming proposal; detailed naming table unavailable through the
    web reader
  reference: https://academic.oup.com/jac/article/73/10/2625/5055843
  summary: This PMID identifies the nomenclature proposal, not the separate AAC.00649-18
    functional study.
  support: context_only
- accessed_at: '2026-10-15T13:12:37Z'
  evidence_id: mcr-later-context
  kind: primary_source
  locator: Results and Discussion, initial isolate-identification subsection; supplements
    not inspected
  reference: https://journals.asm.org/doi/10.1128/aac.00133-19
  summary: A later report describes resistant Acinetobacter and susceptible Shewanella
    carriers; co-occurrence does not establish allele causality.
  support: context_only
- accessed_at: '2026-10-15T13:12:37Z'
  evidence_id: msrc
  kind: primary_source
  locator: Results and Discussion, concluding paragraph
  reference: https://journals.asm.org/doi/10.1128/aac.45.1.263-266.2001
  summary: Susceptibility changes allow a downstream-gene contribution; the proposed
    efflux mechanism remains a hypothesis.
  support: partial
- accessed_at: '2026-10-15T13:12:37Z'
  evidence_id: eatav
  kind: primary_source
  locator: Reciprocal-replacement results, Table 3 headers and Discussion; no quantitative
    AST extraction
  reference: https://journals.asm.org/doi/10.1128/aac.01030-13
  summary: Functional genetic evidence supports an LSAP phenotype, but the tested
    pleuromutilin was tiamulin and the biochemical mechanism remained unresolved.
  support: partial
- accessed_at: '2026-10-15T13:12:37Z'
  evidence_id: eatav-genome
  kind: primary_source
  locator: Aus0004 reference-genome results; also matched by cached UniProt bibliography
  reference: https://journals.asm.org/doi/10.1128/jb.00259-12
  summary: Aus0004 supplies reference-genome context, not the tested derivative's
    identity.
  support: context_only
- accessed_at: '2026-10-15T13:12:37Z'
  evidence_id: ddl-primary
  kind: primary_source
  locator: Abstract; full results and figures not obtained
  reference: https://onlinelibrary.wiley.com/doi/abs/10.1110/ps.39101
  summary: The abstract concerns inactivated ligases in glycopeptide-dependent isolates,
    not generic ddl presence.
  support: partial
- accessed_at: '2026-10-15T13:12:37Z'
  evidence_id: ddl-review
  kind: authority
  locator: Abstract explicitly describing a review
  reference: https://academic.oup.com/cid/article-abstract/42/Supplement_1/S25/275393
  summary: This is a review article, not a second allele-specific primary experiment.
  support: context_only
- accessed_at: '2026-10-15T13:12:37Z'
  evidence_id: tmrb
  kind: primary_source
  locator: Abstract; full paper available as advertised PDF but not inspected here
  reference: https://journals.asm.org/doi/10.1128/jb.174.13.4302-4307.1992
  summary: The abstract supports ATP-binding and membrane association; full mechanism
    and experimental subject identity remain unresolved.
  support: partial
- accessed_at: '2026-10-15T13:12:37Z'
  evidence_id: qnrb65
  kind: database
  locator: Journal issue 58(2), letter identity; no allele-specific results obtained
  reference: https://journals.asm.org/doi/10.1128/aac.01849-13
  summary: Citation identity agrees, but no allele-specific primary result was obtained.
  support: unknown
- accessed_at: '2026-10-15T13:12:37Z'
  evidence_id: local-bindings
  kind: record_content
  reference: research/2026-10-15-card-protein-name-evidence.json
  snapshot_sha256: 198e593d90f19a138a001996c604a9c44eedc8a9c7a64d554f8c79c5b1c3bf0f
  summary: Eight live CARD claim positions and hashes bind to eight source rows; six
    reference identities remain non-experimental.
  support: supports
findings:
- category: evidence
  certainty: confirmed
  description: The MCR-4.3 source edges lack the context-specific negative-evidence
    qualification documented in the dossier. Neither universal inactivity nor component-specific
    resistance is established.
  evidence_ids:
  - mcr-original
  - mcr-followup
  - mcr-naming
  - mcr-later-context
  - local-bindings
  field_paths:
  - resistance_mechanisms[aro_id=ARO:3004695]
  finding_id: mcr43-context
  issue_key: card-protein-name-mcr43-context
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  severity: major
  status: open
  target_ids:
  - CHEBI:59064
  - CHEBI:59673
  title: Negative functional evidence requires a scoped qualification
- category: scope
  certainty: confirmed
  description: The inspected eatAv experiment does not supply an exact-compound crosswalk
    for this source edge. Class membership cannot replace structure-specific evidence.
  evidence_ids:
  - eatav
  - eatav-genome
  - local-bindings
  field_paths:
  - resistance_mechanisms[aro_id=ARO:3003761]
  finding_id: eatav-compound
  issue_key: card-protein-name-eatav-compound
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  severity: major
  status: open
  target_ids:
  - CHEBI:8269
  title: Tested derivative does not ground the parent compound
- category: evidence
  certainty: confirmed
  description: The early cited study is insufficient to prove exclusive causality
    or the current target-protection classification. This does not establish that
    CARD's classification is wrong.
  evidence_ids:
  - msrc
  - local-bindings
  field_paths:
  - resistance_mechanisms[aro_id=ARO:3002819]
  finding_id: msrc-evidence
  issue_key: card-protein-name-msrc-evidence
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  severity: minor
  status: open
  target_ids:
  - CHEBI:42355
  - CHEBI:8732
  title: Early association does not establish the current mechanistic classification
- category: evidence
  certainty: confirmed
  description: The generic ligase reference does not resolve the alteration-dependent
    source context. Abstract-only review cannot support an experimental allele assignment.
  evidence_ids:
  - ddl-primary
  - ddl-review
  - local-bindings
  field_paths:
  - resistance_mechanisms[aro_id=ARO:3003970]
  finding_id: ddl-scope
  issue_key: card-protein-name-ddl-scope
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  severity: minor
  status: open
  target_ids:
  - CHEBI:28001
  title: Generic enzyme identity leaves the tested alteration unresolved
finished_at: '2026-10-15T13:12:37Z'
kind: batch
limitations:
- The web reader returned internal errors, without HTTP status, for initial opens
  of QnrB65, msrC, eatAv, the reference-genome paper, the ddl full-text page, and
  the Europe PMC metadata query. These are not documented HTTP 403 responses.
- Publisher-indexed text was subsequently available for msrC, eatAv and the reference-genome
  paper. QnrB65 opens remained unavailable. The naming-proposal find operations also
  returned internal errors.
- No native primary article files were cached; primary assessments are dated human-readable
  web-text observations, not offline replay of article bodies.
- No figures, supplements or rendered tables were visually verified. No MIC values
  or resistance breakpoints were newly curated.
- The nomenclature proposal's exact PMID-to-DOI identity was checked against existing
  local Europe PMC discovery metadata. No NCBI request was made.
- A later clinical Acinetobacter report at https://academic.oup.com/jac/article/75/1/60/5580312
  remains an unreviewed lead after a web-reader internal error; no universal MCR-4.3
  activity conclusion is made.
- All inherited access holds remain in force. No held article was retried, and NCBI
  AST/#1040 and reuse-terms review remain deferred.
- No whole-record primary signoff, biological curation, AST import, source adoption,
  GitHub mutation or NCBI request.
- The full-corpus goal remains open; a validated review is not scientific status promotion.
- Evidence timestamps mark final inspection of the available source text and assessment;
  the web reader does not expose exact underlying fetch timestamps.
links:
- research/2026-10-15-card-protein-name-evidence.json
- research/2026-10-15-card-protein-name-evidence-assessments.json
notes:
- A protected baseline was frozen before research; the source inspection rebinds the
  unchanged target bytes.
- Do not reinterpret the prior CARD target-protection classification as an efflux
  claim; the historical paper's uncertainty is retained.
repository: culturebotai/AntibioticMech
review_id: 20261015T131237Z-card-protein-name-primary-context
reviewer:
  identity: Codex
  independence: self_review
  independence_basis: Same agent performed the discovery follow-up and this scoped
    review; not an independent review.
  kind: agent
schema_version: 1.0.0
scientific_review: true
scope:
  coverage: partial
  description: Only the eight CARD claims linked to six pending protein-name candidates;
    not whole-record review.
  exclusions:
  - reason: Not reassessed in this bounded primary-evidence follow-up.
    target: Other claims in the eight records and the remaining 2931 records
  population_size: 2939
  reviewed_target_ids:
  - CHEBI:100241
  - CHEBI:59064
  - CHEBI:59673
  - CHEBI:42355
  - CHEBI:8269
  - CHEBI:8732
  - antibioticmech:aro-be005cca98
  - CHEBI:28001
  selection: All six pending candidates from the pinned 720-term name screen, with
    all eight affected corpus records.
skill: antibioticmech-research-resistance-genes
source:
  git_revision: 8f0dc555d7b4b683610fae7945f22bd6e9fb5105
  inputs:
  - path: curation/source_queue.tsv
    role: context
    sha256: 32ff6b625b7787e8935d6f1ec7195d2ba61fda714a664ee1b54049ebc2bd9fdb
  - path: data/antibiotics/antibacterial/ciprofloxacin.yaml
    role: target
    sha256: de4e65076e0a69a82637f3af5a824c0bd198a1b49ee22d85a424d67ca0c9fedd
  - path: data/antibiotics/antibacterial/colistin-a.yaml
    role: target
    sha256: 185868296f91137f4154d34980a5e7d2dc54b48cfc6b00fe33b1f682ab975ec2
  - path: data/antibiotics/antibacterial/colistin-b.yaml
    role: target
    sha256: 0c6a2a63eb0235476c340f5fd8f5f0774125f4fc179fb7d24eb9ba3939945b91
  - path: data/antibiotics/antibacterial/erythromycin-a.yaml
    role: target
    sha256: 4639a9ca3005a92edabbab64b412731187bbe2a540971f251ce4a856bd6fe65f
  - path: data/antibiotics/antibacterial/pleuromutilin.yaml
    role: target
    sha256: 068be77c7f217810e535cc6c301d52cd5756d7ed72e7f1253fc61fa2bbd26ee5
  - path: data/antibiotics/antibacterial/quinupristin.yaml
    role: target
    sha256: 967ba62d716c63cbfbaae4ef73bcb94c3932d6b96177ade545bed3d47e0f83b6
  - path: data/antibiotics/antibacterial/tunicamycin.yaml
    role: target
    sha256: 44fe9a0f90d401d43e58ff9c272a178cec9b68e6c8bf33daebfa901516d18584
  - path: data/antibiotics/antibacterial/vancomycin.yaml
    role: target
    sha256: 1d053af44db16f6be6dc981827b0dbb079f41632fb4259c2803147ff99e4540f
  - path: data/raw/aro_resistance_edges.tsv
    role: context
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
  - path: docs/CURATION.md
    role: context
    sha256: a340fda17ab222a356ee9113cfdb2bd8e237e8784184195057e4189446580996
  - path: docs/HARMONIZATION.md
    role: context
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
  - path: research/2026-10-15-card-protein-name-evidence-assessments.json
    role: context
    sha256: ed5215a715ed801e290f7468e996f00d6ac7eea71a04762c29ccdaa7cff6f61c
  - path: research/2026-10-15-card-protein-name-evidence-citation.json
    role: context
    sha256: 4ada293625e06fc7292ab37ae3ce82a5a431907ae12499940069f9c1643f0af9
  - path: research/2026-10-15-card-protein-name-evidence.json
    role: context
    sha256: 198e593d90f19a138a001996c604a9c44eedc8a9c7a64d554f8c79c5b1c3bf0f
  - path: research/2026-10-15-card-protein-name-screen.json
    role: context
    sha256: 9ea833b1d24f8c48189a374f13a549ccff6458185d77f782a86961aea15a8a51
  - path: scripts/seed_from_sources.py
    role: context
    sha256: 10a1c33ce3e61ee06d1d03ad7539a95e676df97c9e3bb0062a2f26d39c99b5eb
  state: working_tree
started_at: '2026-10-15T12:57:32Z'
summary: Six reference candidates remain non-experimental. Four scoped findings require
  evidence qualification or further primary review; no biological records changed.
tags:
- card
- uniprot
- reference-only
- primary-evidence
targets:
- kind: generated
  label: ciprofloxacin
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  path: data/antibiotics/antibacterial/ciprofloxacin.yaml
  record_class: AntibioticRecord
  target_id: CHEBI:100241
- kind: generated
  label: colistin A
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  path: data/antibiotics/antibacterial/colistin-a.yaml
  record_class: AntibioticRecord
  target_id: CHEBI:59064
- kind: generated
  label: colistin B
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  path: data/antibiotics/antibacterial/colistin-b.yaml
  record_class: AntibioticRecord
  target_id: CHEBI:59673
- kind: generated
  label: erythromycin A
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  path: data/antibiotics/antibacterial/erythromycin-a.yaml
  record_class: AntibioticRecord
  target_id: CHEBI:42355
- kind: generated
  label: pleuromutilin
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  path: data/antibiotics/antibacterial/pleuromutilin.yaml
  record_class: AntibioticRecord
  target_id: CHEBI:8269
- kind: generated
  label: quinupristin
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  path: data/antibiotics/antibacterial/quinupristin.yaml
  record_class: AntibioticRecord
  target_id: CHEBI:8732
- kind: generated
  label: tunicamycin
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  path: data/antibiotics/antibacterial/tunicamycin.yaml
  record_class: AntibioticRecord
  target_id: antibioticmech:aro-be005cca98
- kind: generated
  label: vancomycin
  owner_paths:
  - path: data/raw/aro_resistance_edges.tsv
    repository: CultureBotAI/AntibioticMech
    role: Frozen source assertions; retain provenance, do not hand-edit
  - path: scripts/seed_from_sources.py
    repository: CultureBotAI/AntibioticMech
    role: Source-owned projection and future evidence qualification
  path: data/antibiotics/antibacterial/vancomycin.yaml
  record_class: AntibioticRecord
  target_id: CHEBI:28001
title: Primary evidence scope for six CARD protein-name candidates
verdict: needs_curation
```
