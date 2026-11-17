# YAML Record Review: 10α-hydroperoxy-guaia-1,11-diene

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antiprotozoal/10α-hydroperoxy-guaia-1-11-diene.yaml`
- Started UTC: 2026-09-25T16:23:03Z
- Finished UTC: 2026-09-25T16:23:03Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:66472` |
| Label | `10α-hydroperoxy-guaia-1,11-diene` |
| Class | `ANTIPROTOZOAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained path | `data/raw/chebi_antimicrobials.tsv` plus the ChEBI extractor for seeded identity, synonyms, structure, parent terms, role terms, and xrefs |
| Generated record | `data/antibiotics/antiprotozoal/10α-hydroperoxy-guaia-1-11-diene.yaml`, locked by `data/antibiotics/PATHS.tsv` |

The reviewed YAML is the generated ChEBI seed for `CHEBI:66472`. It contains one ChEBI source concept with `role_terms: [CHEBI:36335]`, the ChEBI definition, one ChEBI IUPAC synonym, two ChEBI parents, a ChEBI-sourced structure, and one `reaxys` xref.

The record has no record-level `evidence`, `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`, `molecular_targets`, `activity_spectrum`, `resistance_mechanisms`, `producer_organisms`, `causal_graph`, `datasets`, `clinical_status`, or `discussions`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiprotozoal/10α-hydroperoxy-guaia-1-11-diene.yaml` | Passed. |
| `just validate-strict data/antibiotics/antiprotozoal/10α-hydroperoxy-guaia-1-11-diene.yaml --out /tmp/antibioticmech-chebi-66472-strict.tsv` | Passed; 1 file, 0 errors. |
| `just verify-corpus --summary` | Passed; 2,939 records on disk exactly reproduce from `data/raw/` plus curator inputs. The only diagnostic was the known unrelated CARD `iclaprim` self-contradictory cross-reference refusal. |
| `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi66472.tsv` | Passed. The exact `CHEBI:66472` rows were the `mechanism` queue row, with 0 CARD targets and 0 resistance edges to build on; the `producer-candidate` row for `Pogostemon cablin`, marked `SOURCE only`; and the `review-readiness` row with 1 source literature lead, 0 record evidence items, and 0 targets. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-next-review-queue.tsv` | Passed; wrote 2,859 review-readiness rows. `CHEBI:66472` is queued as `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| Live OLS4 `CHEBI:66472` term, parent, and `has_role` lookups | Passed; the term is current and non-obsolete, the identity annotations match the YAML formula, SMILES, Standard InChI, InChIKey, mass values, Reaxys and PubMed xrefs, the direct parents are `CHEBI:35924` and `CHEBI:36744`, and its imported antimicrobial role is `CHEBI:36335`. |
| Live OLS4 `CHEBI:36335` role lookup | Passed; the source ChEBI role resolves to current, non-obsolete `trypanocidal drug`. |
| PubChem InChIKey lookup for `WVEJIBNZNZLFEF-SFDCQRBFSA-N` | Passed; the lookup returned CID 11736507, and its PubChem formula, Standard InChI, InChIKey, exact mass, and charge match the record identity. |
| PubMed ESummary and EFetch for `PMID:15577255` | Passed; the PMID resolves to Kiuchi et al. 2004, with DOI `10.1248/cpb.52.1495`, and its abstract describes trypanocidal hydroperoxides isolated from `Pogostemon cablin`. |
| J-STAGE article and PDF for `DOI:10.1248/cpb.52.1495` | Passed; the publisher page resolved and the downloaded PDF text was inspectable. |
| `scripts/search_publications.py` PubMed/Semantic Scholar search for the label, InChIKey, and mechanism terms | Partially passed; PubMed returned 0 candidates and Semantic Scholar returned HTTP 429 under its unauthenticated rate limit, so the bounded search did not find additional mechanism papers. |

## Identity and Grounding

- `CHEBI:66472` is the correct grounding for the exact sesquiterpene hydroperoxide named by the record. Live OLS4 reports the term as current and non-obsolete, and the ChEBI term, committed raw ChEBI row, generated YAML, and PubChem CID 11736507 agree on Standard InChIKey `WVEJIBNZNZLFEF-SFDCQRBFSA-N`, formula `C15H24O2`, charge `0`, and exact mass near 236.17763.
- The direct ChEBI parents are current, non-obsolete `CHEBI:35924` `peroxol` and `CHEBI:36744` `guaiane sesquiterpenoid`, and both are strictly broader than the exact compound.
- `activity_roles: [CHEBI:36335]` preserves ChEBI's `trypanocidal drug` role and correctly files the record as `ANTIPROTOZOAL`. OLS4 reports that ChEBI also asserts the generic `metabolite` role for `CHEBI:66472`; the seeder correctly omits that non-antimicrobial role.
- The ChEBI exact IUPAC synonym in the YAML matches the committed raw ChEBI inventory row. PubChem uses a different but compatible IUPAC rendering for the same Standard InChIKey.
- The local ignored-inclusive exact search covered `reports`, `curation`, `data/raw`, `data/antibiotics`, and `.git` refs/logs. It found only the target YAML, raw ChEBI row, lockfile row, review-queue row, and active local branch/log entries; it found no prior exact review report, and GitHub plus `origin` had no stale remote branch ref before this branch was published.

## Evidence

The record currently inherits the ChEBI database assertion and exact Reaxys xref but has no primary-paper activity, mechanism, target, resistance, producer, or causal-graph evidence in the YAML.

| Lead | Supports the antiprotozoal record? | Review |
|---|---|---|
| `PMID:15577255` / `DOI:10.1248/cpb.52.1495` | Exact identity, plant source, and trypanocidal activity support for compound 1. | The full two-page paper reports activity-guided isolation of three hydroperoxides from `Pogostemon cablin`, concludes that compound 1 is `10a-hydroperoxy-guaia-1,11-diene`, reports compound 1 with formula `C15H24O2`, and measures a `Trypanosoma cruzi` epimastigote minimum lethal concentration of 0.84 micromolar. |
| ChEBI `CHEBI:66472` | Exact seeded identity and upstream role assertion. | Live OLS4 repeats the same formula, Standard InChI, InChIKey, SMILES, Reaxys xref, and PubMed xref as the generated YAML, and asserts the imported `trypanocidal drug` role. |
| PubChem CID 11736507 | Secondary structure cross-check. | PubChem resolves the record's InChIKey to one CID with the same Standard InChI, formula, charge, and exact mass; this verifies identifier consistency but is not source evidence for the trypanocidal assay. |
| Exact PubMed/Semantic Scholar search for label, InChIKey, and mechanism terms | No new inspected mechanism evidence. | The repository search adapter wrote 0 candidates: PubMed returned no matching mechanism candidate and Semantic Scholar was rate-limited. The source paper establishes activity but does not claim a molecular target or mode of action. |

## Completeness

- **Mechanism:** incomplete. The record has no `mode_of_action`, target scope, molecular target, or causal edge, and neither the inspected ChEBI term nor Kiuchi et al. 2004 establishes an exact molecular target for the trypanocidal activity.
- **Activity:** incomplete. Kiuchi et al. 2004 reports compound 1 with a 0.84 micromolar minimum lethal concentration against `Trypanosoma cruzi` epimastigotes, but the YAML has no `ActivityObservation` encoding the organism, Tulahuen strain, assay duration, endpoint, value, qualifier, and units.
- **Producer:** incomplete. Kiuchi et al. 2004 supports the `Pogostemon cablin` source plant for the acetone extract and compound 1 isolation, but the queue correctly treats the definition phrase as a `SOURCE only` lead until a curator chooses the exact NCBI taxon and confirms whether this plant-source observation should become a structured `ProducerOrganism`.
- **Resistance:** empty and not currently a consequential gap. CARD has 0 targets and 0 resistance edges to build on for this ChEBI-only record.
- **Clinical status and datasets:** empty and not currently consequential for this natural-product antiprotozoal seed. No regulatory or dataset accession lead was present in the inspected record or source row.
- **Discussions:** empty. The missing mode of action, assay extraction, and plant producer decision are concrete follow-up tasks and would justify a `CURATION_TODO` if a future curation pass cannot resolve them from the source paper and identifier checks.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| F1 | Major | The seeded exact trypanocidal record has primary activity support but no curated mode of action, molecular target, causal graph, or structured assay evidence. | The YAML is `SEEDED` from ChEBI with role `CHEBI:36335`; it has no `evidence`, `activity_spectrum`, `mode_of_action`, `molecular_targets`, `causal_graph`, or `discussions`. The regenerated queues keep it in the `mechanism` and `review-readiness` queues with 0 targets and 0 record evidence items, while Kiuchi et al. 2004 reports a 0.84 micromolar `Trypanosoma cruzi` MLC for compound 1 but no target. | Curator-owned additions on `data/antibiotics/antiprotozoal/10α-hydroperoxy-guaia-1-11-diene.yaml`, written through `write_validated_antibiotic` with an explicit `CurationEvent`; if no mechanism is supportable, the YAML needs an explicit unresolved discussion or curated mechanism veto. |
| F2 | Minor | The plant source is a plausible producer lead but not yet a structured producer assertion. | ChEBI's definition and Kiuchi et al. 2004 both tie the exact compound to `Pogostemon cablin`; the regenerated worklist still leaves this as a `producer-candidate` row marked `SOURCE only`, and the YAML has no `producer_organisms` entry. | Curator-owned addition on the same YAML, after checking the exact NCBI taxon and deciding that a higher-plant source belongs in `ProducerOrganism` with source evidence rather than remaining a free-text definition. |

No blocker findings were found.

## Recommended Edits

1. Add an `ActivityObservation` for Kiuchi et al. 2004 only after extracting the exact assay semantics for compound 1: `Trypanosoma cruzi` epimastigotes, Tulahuen strain, minimum lethal concentration, 0.84 micromolar, 24-hour incubation, duplicate observation, solvent and endpoint notes as representable in the schema.
2. Search by compound 1's preferred label, ASCII `10a` label, InChIKey, and `Trypanosoma cruzi` terms for primary mechanism evidence; if no source establishes a molecular target or coarse mode of action, add a `CURATION_TODO` discussion or curated `UNKNOWN`/veto rather than inferring a target from the hydroperoxide functional group.
3. Curate `Pogostemon cablin` only after confirming the exact NCBI taxon and deciding whether plant natural-product isolation should be represented as a `ProducerOrganism` in this corpus; keep the existing definition text as a source lead until that decision is explicit.
4. Leave the seeded ChEBI identifier, structure, parentage, trypanocidal role, and Reaxys xref untouched unless the upstream ChEBI extractor changes them; live ChEBI, PubChem, J-STAGE, and the committed raw ChEBI identity fields agree.

## Follow-up Checks

- Rerun `just validate-strict data/antibiotics/antiprotozoal/10α-hydroperoxy-guaia-1-11-diene.yaml --out /tmp/antibioticmech-chebi-66472-strict.tsv` after any curator-owned edit.
- Rerun `just verify-corpus --summary` to confirm new curator-owned fields are accepted as maintained curation rather than generated-record drift.
- Rerun `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi66472.tsv` and confirm `CHEBI:66472` either leaves the `mechanism` and `producer-candidate` queues or carries intentional unresolved discussions.
- Manually reread the YAML after writing activity, producer, or mechanism evidence to verify each citation is attached to the narrow assay, organism, target, or causal edge it supports.

## Additional Notes

- The J-STAGE PDF text extraction used `pypdf`. Its output included font-encoding artifacts around symbols such as alpha, micro, and plus signs, but the compound numbering, structure conclusion, formula, title, authors, DOI, isolate, and assay rows were readable enough for this identity-level review.
- The PubMed ESearch endpoint returned an empty body twice for an ad hoc URL-encoded label/InChIKey query. The repository `scripts/search_publications.py` PubMed provider completed and wrote 0 candidates for the same exact label/InChIKey/mechanism intent, so the empty raw ESearch responses were ignored.
