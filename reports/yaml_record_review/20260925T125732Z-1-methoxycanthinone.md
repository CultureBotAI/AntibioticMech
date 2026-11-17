# YAML Record Review: 1-methoxycanthinone

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antiviral/1-methoxycanthinone.yaml
- Started UTC: 2026-09-25T12:52:30Z
- Finished UTC: 2026-09-25T12:57:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | AntibioticRecord |
| Identifier | CHEBI:66700 |
| Label | 1-methoxycanthinone |
| File | data/antibiotics/antiviral/1-methoxycanthinone.yaml |
| Maintained/generated status | Generated from `data/raw/chebi_antimicrobials.tsv` |
| `curation_status` | SEEDED |
| `grounding_status` | EXACT |
| Source concept | CHEBI:66700, minted as `antibioticmech:chebi-106be79f45`, ChEBI 2026-08-30 |
| Imported activity role | CHEBI:64946, anti-HIV agent |

The record is a generated exact ChEBI seed for one canthin-6-one alkaloid. ChEBI supplies the definition, structure, two exact synonyms, three structural parents, an anti-HIV role, a Reaxys xref, three PubMed xrefs, and the exact ChEBI source concept. The YAML does not yet contain curator-owned `evidence`, `mode_of_action`, `mode_of_action_target_scope`, molecular targets, producer organisms, activity observations, resistance mechanisms, causal graphs, datasets, or discussions.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiviral/1-methoxycanthinone.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/antibiotics/antiviral/1-methoxycanthinone.yaml --out /tmp/antibioticmech-chebi-66700-strict.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just verify-corpus --summary` | Passed; 2,939 records expected and on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. The only diagnostic was the known unrelated CARD `ARO:3000337` / `CHEBI:31724` iclaprim cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-next-worklist.tsv` | Passed; regenerated the full worklist with the same unrelated CARD diagnostic. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-66700-review-queue.tsv` | Passed; wrote 2,859 `review-readiness` rows. |
| `uv run runoak -i ols:chebi labels CHEBI:66700 CHEBI:64946 CHEBI:35618 CHEBI:38163 CHEBI:38958` | Passed; live labels resolve to `1-methoxycanthinone`, `anti-HIV agent`, `aromatic ether`, `organic heterotetracyclic compound`, and `indole alkaloid`. |
| Live OLS4 term/parent/role lookups for `CHEBI:66700` | Passed; the term is current and non-obsolete, the direct parents are exactly `CHEBI:35618`, `CHEBI:38163`, and `CHEBI:38958`, and the live relationship payload includes the anti-HIV role `CHEBI:64946`. |
| PubChem lookup by InChIKey `LEPXKGXTXIACRO-UHFFFAOYSA-N` | Passed; resolved CID 483522 with matching formula `C15H10N2O2`, Standard InChI, Standard InChIKey, monoisotopic mass, charge 0, and exact ChEBI synonyms. |
| PubMed exact-label search | Passed; exact label/synonym search returned 8 PMIDs, including all three ChEBI source PMIDs. |
| Europe PMC exact-label search | Passed; exact label/synonym search returned 24 hits, including known plant natural-product papers plus later phytochemical, docking, LC-MS, review, and unrelated tokenized matches. |
| Semantic Scholar exact-label search | Not checked; the public Graph API returned HTTP 429. |

No additional focused term, reference, or history validator is exposed for one seeded record. The remaining term, reference, and history checks for this record are the live identifier checks above, direct inspection of ChEBI/PubMed/PubChem metadata, audit-field inspection, and the full-corpus `just verify-corpus --summary` drift check.

## Identity and Grounding

The record denotes the exact ChEBI structure it claims.

- The YAML `identifier`, `label`, `grounding_status`, and single source concept all denote `CHEBI:66700` / 1-methoxycanthinone.
- The live OLS4 term is non-obsolete and carries the same Standard InChI, Standard InChIKey, formula, charge, average mass, monoisotopic mass, three PubMed xrefs, and Reaxys xref imported into `data/raw/chebi_antimicrobials.tsv`.
- PubChem CID 483522 resolves from the record's exact InChIKey and returns the same Standard InChI, formula, monoisotopic mass, and charge.
- The record's `parent_compounds` are current direct ChEBI parents and are strictly broader classes.
- `CHEBI:64946` is the only in-scope antimicrobial role on the raw ChEBI row and is enough for the seed-time `ANTIVIRAL` filing.

The exhaustive local search covered ignored and non-ignored files in `data/antibiotics`, `data/raw`, `curation`, `reports/yaml_record_review`, `.claude`, `docs`, `README.md`, `conf`, `src`, `scripts`, `tests`, `justfile`, and `pyproject.toml`. It found no prior YAML review report, no grounding/exclusion decision, and no curated exact-structure activity, producer, mechanism, target, resistance, causal-graph, or dataset assertion for `CHEBI:66700`, `antibioticmech:chebi-106be79f45`, `LEPXKGXTXIACRO-UHFFFAOYSA-N`, or `reaxys:668854`.

## Evidence

The ChEBI source PMIDs are relevant discovery leads, but the existing YAML has not promoted any source-text assertion into a claim-level curated object.

| PMID | What the inspected PubMed metadata supports | Curation implication |
|---|---|---|
| PMID:11141127 | The abstract reports 1-methoxycanthinone as one of the known compounds isolated from `Leitneria floridana` and states that in vitro evaluation found compound 5 to be a potent anti-HIV agent with an EC50 and therapeutic index. | Strong exact-compound lead for anti-HIV activity and a possible `Leitneria floridana` producer row; full text is needed for cell line, viral strain, assay context, and exact taxon/part details before writing an `ActivityObservation` or `ProducerOrganism`. |
| PMID:12590453 | The abstract reports isolation of 1-methoxycanthin-6-one from `Ailanthus altissima` root extract during phytotoxicity-guided purification and states that this alkaloid was not phytotoxic in that assay. | Supports `Ailanthus altissima` as an isolation source after taxon resolution; does not support the anti-HIV role or mode of action. |
| PMID:6619885 | The abstract reports isolation of canthin-6-one and 1-methoxycanthin-6-one from `Ailanthus altissima` callus and cell-suspension cultures and compares cytotoxicity of canthinone alkaloids. | Supports production by plant cell cultures and may support a future producer claim with careful scope; does not establish antiviral mechanism. |

The regenerated worklist has three exact rows:

- `mechanism`: no `mode_of_action`, no CARD targets, and no CARD resistance edges to build on.
- `producer-candidate`: `Ailanthus altissima`, flagged as source-only because an isolation phrase needs curator confirmation.
- `review-readiness`: mechanism absent, 3 source literature leads, 0 record evidence items, 0 targets.

Europe PMC and PubMed exact-label searches surfaced additional canthinone natural-product, synthesis, and docking leads. None contradicted the ChEBI seed during this review, and none were inspected far enough to justify adding target or mode-of-action claims.

## Completeness

The generated identity and class are sound, but the record is still a seed.

- Identity, structure, parentage, xref, and antiviral role agree with current ChEBI, PubChem, the committed ChEBI inventory, and `PATHS.tsv`.
- The anti-HIV literature lead is exact enough to justify future activity curation, but the YAML has no activity observation yet.
- The `Ailanthus altissima` and `Leitneria floridana` isolation leads are exact enough to justify future producer curation after taxon resolution and full-text scope checks.
- Mechanism is absent. ChEBI assigned an anti-HIV activity role, not a viral target role, and no inspected source supplied a molecular target or causal step for the anti-HIV effect.
- Empty `molecular_targets`, `activity_spectrum`, `producer_organisms`, `resistance_mechanisms`, `causal_graphs`, `datasets`, and `discussions` are valid placeholders until exact, claim-level evidence is curated.

## Findings

### Blocker

None found.

### Major

| ID | Finding | Evidence | Maintained owner |
|---|---|---|---|
| F1 | Literature leads exist for exact 1-methoxycanthinone, but none have been curated into mechanism, activity, or producer claims. | The record is still `SEEDED` with no `mode_of_action`, no `molecular_targets`, no `activity_spectrum`, no `producer_organisms`, and no claim-level `evidence`. `PMID:11141127` is an exact anti-HIV lead; `PMID:12590453` and `PMID:6619885` are exact `Ailanthus altissima` isolation or plant-cell production leads. The regenerated worklist keeps `CHEBI:66700` on the `mechanism`, `producer-candidate`, and `review-readiness` queues. | Curator-owned additions on `data/antibiotics/antiviral/1-methoxycanthinone.yaml`, written through `write_validated_antibiotic` with an explicit `CurationEvent`; generated identity or class fixes, if ever needed, belong in the ChEBI extractor or `curation/decisions.tsv`. |

### Minor

None found.

## Recommended Edits

1. Preserve the generated ChEBI identity, structure, parents, role, Reaxys xref, PubMed xrefs, and source concept.
2. Inspect the full text for `PMID:11141127`; if it names the exact HIV assay, add an exact anti-HIV `ActivityObservation` with qualitative activity, source assay context, and claim-level evidence.
3. Resolve `Ailanthus altissima` and `Leitneria floridana` to NCBITaxon CURIEs and inspect `PMID:11141127`, `PMID:12590453`, and `PMID:6619885` far enough to add producer rows only for source organisms that truly biosynthesize this compound.
4. Search the anti-HIV follow-up literature for an exact 1-methoxycanthinone molecular target. Leave `mode_of_action` empty unless a source supports a representable target or mechanism; if no exact mechanism is recoverable after a bounded search, add a curator veto note rather than inferring a viral mechanism from the anti-HIV role.

## Follow-up Checks

| Edit | Proof |
|---|---|
| Add producer, activity, target, or mechanism evidence | Re-run `just validate-strict data/antibiotics/antiviral/1-methoxycanthinone.yaml --out /tmp/antibioticmech-chebi-66700-strict.tsv` and confirm every new claim-level object has a stable exact-compound reference. |
| Add a producer row for `Ailanthus altissima` | Re-run `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` and confirm the CHEBI:66700 `producer-candidate` row is either resolved or intentionally left with a documented reason. |
| Claim `mode_of_action` or add a mechanism veto | Re-run `just worklist --queue mechanism --limit 0 --tsv /tmp/antibioticmech-mechanism.tsv` and confirm `CHEBI:66700` no longer appears for absent mechanism review. |
| Promote to `REVIEWED` | Re-run `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`; CHEBI:66700 should leave the queue only after identity, structure, class, and at least mode of action have all been checked. |

## Additional Notes

- `PMID:11141127` is shared with the separate ChEBI seed for simalikalactone D; that is not a duplicate record because the paper reports several different compounds.
- The ChEBI exact-label literature leads after 2003 are useful follow-up for synthesis, natural-product, and docking context, but they were not needed to verify the current seed.
- No report finding requires a generated-field correction. The unresolved work is curator-owned enrichment of producer, activity, and mechanism evidence.
