# YAML Record Review: 10-deoxymethymycin

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/unspecified/10-deoxymethymycin.yaml`
- Started UTC: 2026-09-25T15:05:00Z
- Finished UTC: 2026-09-25T15:09:29Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:29706` |
| Label | `10-deoxymethymycin` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained path | `data/raw/chebi_antimicrobials.tsv` plus the ChEBI extractor for seeded identity, synonyms, structure, parents, role terms, and xrefs |
| Generated record | `data/antibiotics/unspecified/10-deoxymethymycin.yaml`, locked by `data/antibiotics/PATHS.tsv` |

The reviewed YAML is the generated ChEBI seed for `CHEBI:29706`. It contains one ChEBI source concept with `role_terms: [CHEBI:33281]`, a ChEBI definition, three ChEBI synonyms, three ChEBI parents, a ChEBI-sourced structure, and four database xrefs: `cas:11091-33-1`, `kegg.compound:C11994`, `lipidmaps:LMPK04000035`, and `reaxys:8085280`.

The record has no record-level `evidence`, `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`, `molecular_targets`, `activity_spectrum`, `resistance_mechanisms`, `producer_organisms`, `causal_graph`, `datasets`, `clinical_status`, or `discussions`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/10-deoxymethymycin.yaml` | Passed. |
| `just validate-strict data/antibiotics/unspecified/10-deoxymethymycin.yaml --out /tmp/antibioticmech-chebi-29706-strict.tsv` | Passed; 1 file, 0 errors. |
| `just verify-corpus --summary` | Passed; 2,939 records on disk exactly reproduce from `data/raw/` plus curator inputs. The only diagnostic was the known unrelated CARD `iclaprim` self-contradictory cross-reference refusal. |
| `just worklist --tsv /tmp/antibioticmech-next-worklist.tsv` | Passed. The exact `CHEBI:29706` rows were the `mechanism` queue row, with 0 CARD targets and 0 resistance edges to build on, and the `review-readiness` row with 3 source literature leads, 0 record evidence items, and 0 targets. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-next-review-queue.tsv` | Passed; wrote 2,859 review-readiness rows. `CHEBI:29706` is queued as `MECHANISM_REVIEW: mechanism is absent; 3 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| Live OLS4 `CHEBI:29706` term and parent lookups | Passed; the term is current and non-obsolete, the identity annotations match the YAML formula, SMILES, Standard InChI, InChIKey, mass values, and xrefs, and the direct parents are `CHEBI:24400`, `CHEBI:25105`, and `CHEBI:63367`. |
| Live OLS4 `CHEBI:33281` role lookup | Passed; the source ChEBI role resolves to `antimicrobial agent`. |
| PubChem InChIKey lookup for `DZGHWPQKGWXOHD-NHLONWFASA-N` | Passed; the lookup returned CID 5282032, and its PubChem formula, InChI, InChIKey, and exact mass match the record identity. |
| PubMed ESummary for `PMID:17049185`, `PMID:18548476`, and `PMID:20695498` | Passed; all three ChEBI PMID xrefs resolve. |
| PubMed title/abstract search for `10-deoxymethymycin`, `Antibiotic YC 17`, `YC-17`, and the InChIKey | Passed; returned 12 `YC-17` hits, with no exact `10-deoxymethymycin` or InChIKey hit. |
| Europe PMC title/abstract search for `10-deoxymethymycin`, `Antibiotic YC 17`, `YC-17`, and the InChIKey | Passed; returned 13 visible `YC-17` or related macrolide biosynthesis and biocatalysis hits. |

## Identity and Grounding

- `CHEBI:29706` is the correct grounding for the exact structure named by the record. Live OLS4 reports the term as current and non-obsolete, and the ChEBI term, committed raw ChEBI row, generated YAML, and PubChem CID 5282032 agree on Standard InChIKey `DZGHWPQKGWXOHD-NHLONWFASA-N` and formula `C25H43NO6`.
- The three `parent_compounds` are current direct ChEBI parents: `glycoside`, `macrolide antibiotic`, and `monosaccharide derivative`. All are broader chemical classes rather than exact xrefs.
- `activity_roles: [CHEBI:33281]` preserves ChEBI's `antimicrobial agent` role and explains why the record is in scope while filed under `ANTIMICROBIAL_UNSPECIFIED`.
- The ChEBI synonyms `Antibiotic YC 17` and `YC-17` explain the PubMed and Europe PMC exact-title/abstract hits that do not use the preferred label.
- The local ignored-inclusive exact search covered `data/raw`, `curation`, `data/antibiotics`, `reports/yaml_record_review`, and `.git` refs/logs. It found only the target YAML, raw ChEBI row, lockfile row, and review-queue row; it found no prior exact review report and no stale local or remote branch ref.

## Evidence

The record currently inherits the ChEBI database assertion but has no primary-paper activity, mechanism, target, resistance, producer, or causal-graph evidence.

| Lead | Supports the antimicrobial record? | Review |
|---|---|---|
| `PMID:17049185` | Biosynthetic lead only from PubMed metadata. | Resolves to a functional analysis of DesVIII homologues involved in glycosylation of macrolide antibiotics by interspecies complementation. It is a discovery lead for YC-17/methymycin-picromycin biosynthesis, not a claim-level mechanism or activity citation already inspected for exact 10-deoxymethymycin. |
| `PMID:18548476` | Biosynthetic lead only from PubMed metadata. | Resolves to a study of macrolide glycosyltransferase DesVII/DesVIII glycosylation of aglycone substrates. It supports follow-up around 10-deoxymethymycin biosynthesis, not a curated antimicrobial assay or mode of action by itself. |
| `PMID:20695498` | Biosynthetic lead only from PubMed metadata. | Resolves to characterization of glycosyltransferase DesVII and DesVIII in the methymycin/picromycin pathway. It should be inspected in full text before adding a precise producer or pathway claim. |
| `PMID:23770075` | Activity lead from exact-title search. | Europe PMC and PubMed title/abstract search found this paper on combinatorial biosynthesis and antibacterial evaluation of YC-17 glycosylated derivatives. A future pass should inspect the full text to decide whether it measures parent YC-17/10-deoxymethymycin itself or only derivatives. |
| `PMID:9831532`, `PMID:9873687`, `PMID:16825192`, `PMID:19124459`, and later `YC-17` hits | Biosynthetic or biocatalysis leads from exact-title search. | The titles tie YC-17 to PikC/PicK macrolide hydroxylation and engineered macrolide biosynthesis. They do not, at metadata level, support an antimicrobial mode of action or activity observation for this exact record. |

PubMed exact-name and Europe PMC title/abstract searches found `YC-17` biosynthetic, antibacterial-derivative, and enzymology leads but no curated molecular target, resistance mechanism, or exact antimicrobial mechanism for parent 10-deoxymethymycin in the inspected metadata.

## Completeness

- **Mechanism:** incomplete. The record has no `mode_of_action`, target scope, target, or causal edge, and neither CARD nor the inspected ChEBI/PubMed/Europe PMC metadata supplied an antimicrobial mechanism for this exact structure.
- **Activity:** incomplete. ChEBI classifies the exact structure as an antimicrobial agent; the title of `PMID:23770075` is an antibacterial-evaluation lead for YC-17 derivatives, but the record has no exact `ActivityObservation`.
- **Producer:** likely incomplete. The ChEBI source PMIDs and exact `YC-17` search results are biosynthesis leads that should be inspected in full text for exact source organism and strain context before adding `ProducerOrganism` objects.
- **Resistance:** empty and not currently a consequential gap. CARD has 0 targets and 0 resistance edges to build on for this ChEBI-only record.
- **Clinical status and datasets:** empty; the inspected ChEBI, PubMed, PubChem, Europe PMC, and OLS leads did not surface an exact clinical product or dataset accession for parent 10-deoxymethymycin.
- **Discussions:** empty. The absent antimicrobial assay and absent mechanism are consequential enough to justify a `CURATION_TODO` if a future curation pass cannot resolve them.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| F1 | Major | The seeded exact structure has no curated exact antimicrobial activity or mechanism evidence. | The record is `SEEDED` from ChEBI with role `CHEBI:33281`, but has no `evidence`, `activity_spectrum`, `mode_of_action`, `molecular_targets`, or `discussions`. Regenerated worklists keep it in the `mechanism` and `review-readiness` queues with 0 targets and 0 record evidence items. The bounded PubMed and Europe PMC title/abstract searches found `YC-17` biosynthesis, biocatalysis, and antibacterial-derivative leads, but no already-curated exact antimicrobial observation or mechanism for parent 10-deoxymethymycin. | Curator-owned additions on `data/antibiotics/unspecified/10-deoxymethymycin.yaml`, written through `write_validated_antibiotic` with an explicit `CurationEvent`; if full-text inspection cannot support exact antimicrobial activity, the YAML needs an explicit unresolved discussion or curated mechanism veto. |
| F2 | Minor | Exact YC-17 producer and activity leads are present but not curated. | `PMID:23770075` is a PubMed/Europe PMC exact-title hit for antibacterial evaluation of YC-17 glycosylated derivatives, and the ChEBI PMIDs plus older exact-title hits point at YC-17 glycosylation and hydroxylation in the methymycin/picromycin biosynthetic pathway. The YAML has no `activity_spectrum` or `producer_organisms`. | Curator-owned additions on `data/antibiotics/unspecified/10-deoxymethymycin.yaml`, after the full papers establish exact parent-compound activity, producer taxon, and strain context. |

No blocker findings were found.

## Recommended Edits

1. Inspect the full text of `PMID:23770075` and the exact `YC-17` PikC/PicK biosynthesis papers for a parent 10-deoxymethymycin antimicrobial assay. If no exact parent-compound assay exists, add a `CURATION_TODO` or curated mechanism veto documenting that the ChEBI role was retained but no primary antimicrobial activity/mechanism support was found.
2. Inspect `PMID:17049185`, `PMID:18548476`, and `PMID:20695498` for exact 10-deoxymethymycin biosynthesis or conversion claims, and add narrowly scoped `ProducerOrganism` or pathway notes only when the full text names the exact compound form and organism or strain.
3. Keep YC-17 derivative assays separate from parent 10-deoxymethymycin. Add `ActivityObservation` objects only for measurements where the exact tested molecule is YC-17/10-deoxymethymycin, not a glycosylated or hydroxylated derivative.
4. Leave the seeded ChEBI identifier, structure, parentage, role, and xrefs untouched unless the upstream ChEBI extractor changes them; the live ChEBI and committed raw ChEBI identity fields agree.

## Follow-up Checks

- Rerun `just validate-strict data/antibiotics/unspecified/10-deoxymethymycin.yaml --out /tmp/antibioticmech-chebi-29706-strict.tsv` after any curator-owned edit.
- Rerun `just verify-corpus --summary` to confirm new curator-owned fields are accepted as maintained curation rather than generated-record drift.
- Rerun `just worklist --tsv /tmp/antibioticmech-next-worklist.tsv` and confirm `CHEBI:29706` either leaves the `mechanism` queue or has an intentional unresolved mechanism discussion.
- Manually reread the YAML after writing producer or activity evidence to verify each citation is attached to the narrow organism, strain, activity, or biosynthetic claim it supports.

## Additional Notes

- `10-deoxymethymycin`, `Antibiotic YC 17`, and `YC-17` denote the same seeded ChEBI structure in this record. The source literature is easier to find under `YC-17`, but the synonym also introduces near-miss derivative papers that must not be promoted to parent-compound activity without exact full-text support.
