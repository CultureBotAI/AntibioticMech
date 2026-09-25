# YAML Record Review: 11α-hydroxyasiatic acid

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antibacterial/11α-hydroxyasiatic-acid.yaml`
- Started UTC: 2026-09-25T16:54:23Z
- Finished UTC: 2026-09-25T16:54:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:68380` |
| Label | `11α-hydroxyasiatic acid` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained path | `data/raw/chebi_antimicrobials.tsv` plus the ChEBI extractor for seeded identity, synonyms, structure, parents, role terms, and xrefs |
| Generated record | `data/antibiotics/antibacterial/11α-hydroxyasiatic-acid.yaml`, locked by `data/antibiotics/PATHS.tsv` |

The reviewed YAML is the generated ChEBI seed for `CHEBI:68380`. It contains one ChEBI source concept with `role_terms: [CHEBI:33282]`, the ChEBI definition, one ChEBI IUPAC synonym, two ChEBI parents, a ChEBI-sourced structure, and one `reaxys` xref.

The record has no record-level `evidence`, `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`, `molecular_targets`, `activity_spectrum`, `resistance_mechanisms`, `producer_organisms`, `causal_graph`, `datasets`, `clinical_status`, or `discussions`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/11α-hydroxyasiatic-acid.yaml` | Passed. |
| `just validate-strict data/antibiotics/antibacterial/11α-hydroxyasiatic-acid.yaml --out /tmp/antibioticmech-chebi-68380-strict.tsv` | Passed; 1 file, 0 errors. |
| `just verify-corpus --summary` | Passed; 2,939 records on disk exactly reproduce from `data/raw/` plus curator inputs. The only diagnostic was the known unrelated CARD `iclaprim` self-contradictory cross-reference refusal. |
| `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi68380.tsv` | Passed. The exact `CHEBI:68380` rows were the `mechanism` queue row, with 0 CARD targets and 0 resistance edges to build on; the `producer-candidate` row for `Symplocos lancifolia`, marked `SOURCE only`; and the `review-readiness` row with 1 source literature lead, 0 record evidence items, and 0 targets. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi68380-review-queue.tsv` | Passed; wrote 2,859 review-readiness rows. `CHEBI:68380` is queued as `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| Live OLS4 `CHEBI:68380` term and parent lookups | Passed; the term is current and non-obsolete, the identity annotations match the YAML formula, SMILES, Standard InChI, InChIKey, mass values, and xrefs, and the direct parents are `CHEBI:25872` and `CHEBI:35868`. |
| Live OLS4 `CHEBI:33282` role lookup | Passed; the source ChEBI role resolves to current, non-obsolete `antibacterial agent`. |
| PubChem InChIKey lookup for `FFPKNVKIBUBHMY-CCEBUSCFSA-N` | Passed; the lookup returned CID 51041097, and its PubChem formula, Standard InChI, InChIKey, exact mass, and charge match the record identity. |
| PubMed ESummary and EFetch for `PMID:21288041` | Passed; the PMID resolves to Acebey-Castellon et al. 2011, with DOI `10.1021/np100502y`, and the abstract identifies compound 4 as 11α-hydroxyasiatic acid. |
| ACS DOI landing page for `DOI:10.1021/np100502y` | Not checked: ACS returned a Cloudflare browser challenge in this environment, so the source table with exact organism-level activity values was not inspectable. |
| `scripts/search_publications.py` PubMed/Semantic Scholar search for the label, InChIKey, and mechanism terms | Partially passed; PubMed returned 0 candidates and Semantic Scholar returned HTTP 429 under its unauthenticated rate limit, so the bounded search did not find additional mechanism papers. |
| Europe PMC DOI, PMID, label, and InChIKey search | Passed; returned the source `PMID:21288041` plus three false-positive biomedical records. |

## Identity and Grounding

- `CHEBI:68380` is the correct grounding for the exact tetrahydroxy ursane triterpenoid named by the record. Live OLS4 reports the term as current and non-obsolete, and the ChEBI term, committed raw ChEBI row, generated YAML, and PubChem CID 51041097 agree on Standard InChIKey `FFPKNVKIBUBHMY-CCEBUSCFSA-N`, formula `C30H48O6`, charge `0`, and exact mass near 504.34509.
- The direct ChEBI parents are current, non-obsolete `CHEBI:25872` `pentacyclic triterpenoid` and `CHEBI:35868` `hydroxy monocarboxylic acid`; both are strictly broader than this exact structure.
- `activity_roles: [CHEBI:33282]` preserves ChEBI's generic `antibacterial agent` role and correctly files the record as `ANTIBACTERIAL`.
- The ChEBI exact IUPAC synonym in the YAML matches the committed raw ChEBI inventory row. PubChem uses a different systematic IUPAC rendering for the same Standard InChIKey.
- The local ignored-inclusive exact search covered `reports`, `curation`, `data/raw`, `data/antibiotics`, and `.git` refs/logs. It found only the target YAML, raw ChEBI row, lockfile row, and review-queue row; it found no prior exact review report and no stale local or remote branch ref.

## Evidence

The record currently inherits the ChEBI database assertion and exact Reaxys xref but has no primary-paper activity, mechanism, target, resistance, producer, or causal-graph evidence in the YAML.

| Lead | Supports the antibacterial record? | Review |
|---|---|---|
| `PMID:21288041` / `DOI:10.1021/np100502y` | Exact identity and plant-source support at abstract level; antibacterial support remains a full-text lead. | The PubMed abstract names the exact structure as the new ursane triterpenoid compound 4 isolated from methanolic leaf extract of `Symplocos lancifolia`. It also says the isolated triterpenoids were evaluated against `Staphylococcus aureus`, `Enterococcus faecalis`, `Escherichia coli`, and `Pseudomonas aeruginosa`, with several active against Gram-positive bacteria, but does not specify whether compound 4 itself was active. |
| ChEBI `CHEBI:68380` | Exact seeded identity and upstream role assertion. | Live OLS4 repeats the same formula, Standard InChI, InChIKey, SMILES, Reaxys xref, and PubMed xref as the generated YAML, and ChEBI asserts the imported `antibacterial agent` role. |
| PubChem CID 51041097 | Secondary structure cross-check. | PubChem resolves the record's InChIKey to one CID with the same Standard InChI, formula, charge, and exact mass; this verifies identifier consistency but is not source evidence for antibacterial activity. |
| Exact PubMed/Semantic Scholar search for label, InChIKey, and mechanism terms | No new inspected mechanism evidence. | The repository search adapter wrote 0 candidates: PubMed returned no matching mechanism candidate and Semantic Scholar was rate-limited. The source abstract does not claim a molecular target or mode of action. |

## Completeness

- **Mechanism:** incomplete. The record has no `mode_of_action`, target scope, molecular target, or causal edge, and neither the inspected ChEBI term nor the source abstract establishes an exact molecular target for antibacterial activity.
- **Activity:** incomplete. The source paper is likely the exact organism-level activity source, but the accessible abstract only summarizes that several isolated triterpenoids showed Gram-positive activity. A curator needs the ACS full text before adding `ActivityObservation` objects for compound 4.
- **Producer:** incomplete. Acebey-Castellon et al. 2011 supports isolation from `Symplocos lancifolia` leaves, but the queue correctly treats the definition phrase as a `SOURCE only` lead until a curator chooses the exact NCBI taxon and confirms whether this plant-source observation should become a structured `ProducerOrganism`.
- **Resistance:** empty and not currently a consequential gap. CARD has 0 targets and 0 resistance edges to build on for this ChEBI-only record.
- **Clinical status and datasets:** empty and not currently consequential for this plant natural-product seed. No regulatory or dataset accession lead was present in the inspected record, source row, or first-page Europe PMC results.
- **Discussions:** empty. The missing mode of action, exact activity extraction, and plant producer decision are concrete follow-up tasks and would justify a `CURATION_TODO` if a future curation pass cannot resolve them from the source paper and identifier checks.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| F1 | Major | The seeded exact antibacterial has no curated mode of action, target, causal graph, or structured assay evidence, and the exact activity rows remain unverified without the full source table. | The YAML is `SEEDED` from ChEBI with role `CHEBI:33282`; it has no `evidence`, `activity_spectrum`, `mode_of_action`, `molecular_targets`, `causal_graph`, or `discussions`. The regenerated queues keep it in the `mechanism` and `review-readiness` queues with 0 targets and 0 record evidence items. PubMed confirms that Acebey-Castellon et al. evaluated the isolated triterpenoids against four bacterial species, but the abstract does not say which organisms compound 4 inhibited. | Curator-owned additions on `data/antibiotics/antibacterial/11α-hydroxyasiatic-acid.yaml`, written through `write_validated_antibiotic` with an explicit `CurationEvent`; if no mechanism is supportable, the YAML needs an explicit unresolved discussion or curated mechanism veto. |
| F2 | Minor | The plant source is a plausible producer lead but not yet a structured producer assertion. | ChEBI's definition and Acebey-Castellon et al. 2011 both tie the exact compound to `Symplocos lancifolia`; the regenerated worklist still leaves this as a `producer-candidate` row marked `SOURCE only`, and the YAML has no `producer_organisms` entry. | Curator-owned addition on the same YAML, after checking the exact NCBI taxon and deciding that a higher-plant source belongs in `ProducerOrganism` with source evidence rather than remaining a free-text definition. |

No blocker findings were found.

## Recommended Edits

1. Inspect Acebey-Castellon et al. 2011 in full text and extract only exact compound-4 assay results into `ActivityObservation` objects, with organism, strain if reported, assay, value, qualifier, and units preserved from the table.
2. Search by `11alpha-hydroxyasiatic acid`, the IUPAC synonym, the InChIKey, and Gram-positive activity terms for primary mechanism evidence; if no source establishes a molecular target or coarse mode of action, add a `CURATION_TODO` discussion or curated `UNKNOWN`/veto rather than inferring a target from triterpenoid class membership.
3. Curate `Symplocos lancifolia` only after confirming the exact NCBI taxon and deciding whether plant natural-product isolation should be represented as a `ProducerOrganism` in this corpus; keep the existing definition text as a source lead until that decision is explicit.
4. Leave the seeded ChEBI identifier, structure, parentage, antibacterial role, and Reaxys xref untouched unless the upstream ChEBI extractor changes them; live ChEBI, PubChem, PubMed, and the committed raw ChEBI identity fields agree.

## Follow-up Checks

- Rerun `just validate-strict data/antibiotics/antibacterial/11α-hydroxyasiatic-acid.yaml --out /tmp/antibioticmech-chebi-68380-strict.tsv` after any curator-owned edit.
- Rerun `just verify-corpus --summary` to confirm new curator-owned fields are accepted as maintained curation rather than generated-record drift.
- Rerun `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi68380.tsv` and confirm `CHEBI:68380` either leaves the `mechanism` and `producer-candidate` queues or carries intentional unresolved discussions.
- Manually reread the YAML after writing activity, producer, or mechanism evidence to verify each citation is attached to the narrow assay, organism, target, or causal edge it supports.

## Additional Notes

- ACS blocked unauthenticated `curl` access to the DOI landing page with a Cloudflare challenge, so this review deliberately did not infer exact MIC or inhibition values from ChEBI's role assertion or from the PubMed abstract's statement about several active triterpenoids.
