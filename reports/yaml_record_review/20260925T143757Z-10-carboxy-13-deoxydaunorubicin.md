# YAML Record Review: 10-carboxy-13-deoxydaunorubicin

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/unspecified/10-carboxy-13-deoxydaunorubicin.yaml`
- Started UTC: 2026-09-25T14:34:00Z
- Finished UTC: 2026-09-25T14:37:57Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:77195` |
| Label | `10-carboxy-13-deoxydaunorubicin` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained path | `data/raw/chebi_antimicrobials.tsv` plus the ChEBI extractor for seeded identity, structure, parents, role terms, and xrefs |
| Generated record | `data/antibiotics/unspecified/10-carboxy-13-deoxydaunorubicin.yaml`, locked by `data/antibiotics/PATHS.tsv` |

The reviewed YAML is the generated ChEBI seed for `CHEBI:77195`. It contains one ChEBI source concept with `role_terms: [CHEBI:33281]`, a ChEBI definition, one ChEBI IUPAC synonym, six ChEBI parents, a ChEBI-sourced structure, and one database xref, `metacyc.compound:CPD-15740`.

The record has no record-level `evidence`, `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`, `molecular_targets`, `activity_spectrum`, `resistance_mechanisms`, `producer_organisms`, `causal_graph`, `datasets`, `clinical_status`, or `discussions`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/10-carboxy-13-deoxydaunorubicin.yaml` | Passed. |
| `just validate-strict data/antibiotics/unspecified/10-carboxy-13-deoxydaunorubicin.yaml --out /tmp/antibioticmech-chebi-77195-strict.tsv` | Passed; 1 file, 0 errors. |
| `just verify-corpus --summary` | Passed; 2,939 records on disk exactly reproduce from `data/raw/` plus curator inputs. The only diagnostic was the known unrelated CARD `iclaprim` self-contradictory cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-next-worklist.tsv` | Passed. The exact `CHEBI:77195` rows were the `mechanism` queue row, with 0 CARD targets and 0 resistance edges to build on, and the `review-readiness` row with 0 source literature leads, 0 record evidence items, and 0 targets. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-77195-review-queue.tsv` | Passed; wrote 2,859 review-readiness rows. `CHEBI:77195` remains queued as `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| Live OLS4 label lookup | Passed; `CHEBI:77195`, all six parent CURIEs, and `CHEBI:33281` resolve with the labels expected from the seed. |
| Live OLS4 `CHEBI:77195` term and parent lookups | Passed; the term is current and non-obsolete, and its direct parents are `CHEBI:25830`, `CHEBI:35315`, `CHEBI:35868`, `CHEBI:47779`, `CHEBI:49322`, and `CHEBI:63367`. |
| PubChem InChIKey lookup for `ROYGEIBVSIXOBH-QWWLYEKJSA-N` | Passed; the lookup returned two same-Standard-InChI PubChem CIDs, 13591572 and 72715827, matching the record formula and InChIKey. |
| PubMed exact-name search for the label and InChIKey | Passed; returned 0 PMIDs. |
| Semantic Scholar exact-label check | Not checked: the public API returned HTTP 429. |

## Identity and Grounding

- `CHEBI:77195` is the correct grounding for the exact structure named by the record. Live OLS4 reports the term as current and non-obsolete, and the ChEBI term, committed raw ChEBI row, generated YAML, and PubChem InChIKey lookup agree on Standard InChIKey `ROYGEIBVSIXOBH-QWWLYEKJSA-N` and formula `C28H31NO11`.
- The six `parent_compounds` are current direct ChEBI parents: `p-quinones`, `deoxy hexoside`, `hydroxy monocarboxylic acid`, `aminoglycoside`, `anthracycline antibiotic`, and `monosaccharide derivative`. All are broader chemical classes rather than exact xrefs.
- `activity_roles: [CHEBI:33281]` preserves ChEBI's `antimicrobial agent` role and explains why the record is in scope while filed under `ANTIMICROBIAL_UNSPECIFIED`.
- The exact sibling `CHEBI:31047` differs by demethylation at the tetracene ring and has a different formula, Standard InChI, Standard InChIKey, and MetaCyc xref. It is not a duplicate of `CHEBI:77195`.
- The PubChem InChIKey lookup resolves both a neutral CID and a zwitterionic CID because Standard InChI collapses those protonation representations. AntibioticMech does not assert either CID as an exact xref, so this is not a record-level conflict.
- The local ignored-inclusive exact search covered `data/raw`, `curation`, `data/antibiotics`, `reports/yaml_record_review`, and `.git` refs/logs. It found only the target YAML, raw ChEBI row, lockfile row, and review-queue row; it found no prior exact review report and no stale local or remote branch ref.

## Evidence

The record currently inherits the ChEBI database assertion but has no source PMIDs in `data/raw/chebi_antimicrobials.tsv`, no record-level evidence, and no claim-level evidence-bearing activity, mechanism, target, resistance, producer, or causal-graph objects.

- The bounded exact PubMed query for `10-carboxy-13-deoxydaunorubicin` or `ROYGEIBVSIXOBH-QWWLYEKJSA-N` returned zero PMIDs.
- The bounded exact Europe PMC query over the same label and InChIKey returned no exact record evidence on the first result page; the visible matches were unrelated lexical hits.
- Semantic Scholar could not be checked because its public API returned HTTP 429.

## Completeness

- **Mechanism:** incomplete. The record has no `mode_of_action`, target scope, target, or causal edge, and neither ChEBI nor the exact searches found a source-supported antimicrobial mechanism.
- **Activity:** incomplete. ChEBI classifies the exact structure as an antimicrobial agent, but no exact microbial assay was found in the inspected bounded searches.
- **Producer:** empty and unresolved. The adjacent D788-1 record has Streptomyces producer leads; no exact producer lead was found for this methylated sibling.
- **Resistance:** empty and not currently a consequential gap. CARD has 0 targets and 0 resistance edges to build on for this ChEBI-only record.
- **Clinical status and datasets:** empty; the inspected ChEBI, PubMed, PubChem, and OLS leads did not surface an exact clinical product or dataset accession for this structure.
- **Discussions:** empty. The absent source literature, antimicrobial assay, and mechanism are consequential enough to justify a `CURATION_TODO` if a future curation pass cannot resolve them.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| F1 | Major | The seeded exact structure has no primary source support for exact antimicrobial activity or mechanism. | The record is `SEEDED` from ChEBI with role `CHEBI:33281`, but the raw ChEBI row has no source PMIDs and the YAML has no `evidence`, `activity_spectrum`, `mode_of_action`, `molecular_targets`, or `discussions`. Exact PubMed searching found no hits, and the regenerated worklist keeps the record only in the `mechanism` and `review-readiness` queues. | Curator-owned additions on `data/antibiotics/unspecified/10-carboxy-13-deoxydaunorubicin.yaml`, written through `write_validated_antibiotic` with an explicit `CurationEvent`; if exact antimicrobial activity cannot be found, the ChEBI source concept may need a curated exclusion or grounding discussion in `curation/decisions.tsv` or the YAML. |

No blocker or minor findings were found.

## Recommended Edits

1. Search full-text anthracycline biosynthesis literature around D788 metabolites for `10-carboxy-13-deoxydaunorubicin`, its MetaCyc accession `CPD-15740`, and exact structure identifiers. Add exact `ActivityObservation`, `ProducerOrganism`, or mechanism objects only when a paper names this exact methylated structure.
2. If no exact activity paper is found, add a `CURATION_TODO` or curated mechanism veto documenting that the record retains ChEBI's `antimicrobial agent` role but that ChEBI provides no supporting PMID and exact label/InChIKey searches did not resolve antimicrobial activity or mechanism.
3. Leave the seeded ChEBI identifier, structure, parentage, antimicrobial role, and MetaCyc xref untouched unless the upstream ChEBI extractor changes them; live ChEBI and the committed raw ChEBI identity fields agree.

## Follow-up Checks

- Rerun `just validate-strict data/antibiotics/unspecified/10-carboxy-13-deoxydaunorubicin.yaml --out /tmp/antibioticmech-chebi-77195-strict.tsv` after any curator-owned edit.
- Rerun `just verify-corpus --summary` to confirm new curator-owned fields are accepted as maintained curation rather than generated-record drift.
- Rerun `just worklist --limit 0 --tsv /tmp/antibioticmech-next-worklist.tsv` and confirm `CHEBI:77195` either leaves the `mechanism` queue or has an intentional unresolved mechanism discussion.
- Manually reread the YAML after writing evidence to verify each citation is attached to the narrow activity, producer, target, or mechanism claim it supports.

## Additional Notes

- This record is a near miss for D788-1 / `CHEBI:31047`; do not copy producer or activity evidence from `10-carboxy-13-deoxycarminomycin` without a paper or database row that distinguishes `10-carboxy-13-deoxydaunorubicin` by name or structure.
