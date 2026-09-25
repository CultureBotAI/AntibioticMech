# YAML Record Review: 1-(2-hydroxy-4-methoxyphenyl)-3-(4-hydroxy-3-methoxyphenyl)propane

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antimycobacterial/1-2-hydroxy-4-methoxyphenyl-3-4-hydroxy-3-methoxyphenyl-propane.yaml`
- Started UTC: 2026-09-25T07:54:01Z
- Finished UTC: 2026-09-25T07:54:01Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/antimycobacterial/1-2-hydroxy-4-methoxyphenyl-3-4-hydroxy-3-methoxyphenyl-propane.yaml` |
| Class | `ANTIMYCOBACTERIAL` |
| ID | `CHEBI:69704` |
| Label | `1-(2-hydroxy-4-methoxyphenyl)-3-(4-hydroxy-3-methoxyphenyl)propane` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained status | Generated from `data/raw/` inventories |

The record denotes exact ChEBI-grounded
`1-(2-hydroxy-4-methoxyphenyl)-3-(4-hydroxy-3-methoxyphenyl)propane`
with InChIKey `UDWSABBWZXKLLQ-UHFFFAOYSA-N`. It has one ChEBI
source concept, one exact IUPAC synonym, one Reaxys xref, one ChEBI
`antimycobacterial drug` activity role, one broader ChEBI parent compound, and
no record evidence, no seeded `mode_of_action`, no molecular target, no
activity observation, no resistance mechanism, no producer organism, no
clinical assertion, no causal graph, no dataset, and no `Discussion`.

## Validation

| Command | Result |
|---|---|
| `just validate data/antibiotics/antimycobacterial/1-2-hydroxy-4-methoxyphenyl-3-4-hydroxy-3-methoxyphenyl-propane.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antimycobacterial/1-2-hydroxy-4-methoxyphenyl-3-4-hydroxy-3-methoxyphenyl-propane.yaml --out /tmp/chebi-69704-validate-strict.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2,939 expected records, 2,939 records on disk, no missing records, no unexpected records, no drifted fields, no `PATHS.tsv` issues. |
| `just worklist --limit 0 --tsv /tmp/chebi-69704-worklist.tsv` | Confirmed `CHEBI:69704` appears in `mechanism`, `producer-candidate`, and `review-readiness`; the review row reports `MECHANISM_REVIEW`, one source literature lead, zero record evidence items, and zero targets. |
| `uvx --from oaklib runoak -i ols:chebi info CHEBI:69704 CHEBI:64912 CHEBI:134251` | Resolved the compound, the retained `antimycobacterial drug` activity role, and the `guaiacols` parent term through OLS/ChEBI. |
| `curl -L 'https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:69704'` | Resolved the official ChEBI term with the same label, definition, formula, SMILES, Standard InChI, InChIKey, charge, average mass, monoisotopic mass, `pubmed:21919533` xref, `reaxys:6521737` xref, and IUPAC synonym. |
| `curl -L 'https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_69704/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FRO_0000087'` | Resolved four ChEBI `has_role` entries: `metabolite`, `antineoplastic agent`, `antimycobacterial drug`, and `plant metabolite`. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query '21919533[uid]' --limit 20 --output /tmp/chebi-69704-pmid-publications.jsonl` | Wrote one PubMed candidate, the expected `PMID:21919533` / DOI `10.1021/np200593d` paper. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query '"1-(2-hydroxy-4-methoxyphenyl)-3-(4-hydroxy-3-methoxyphenyl)propane"' --limit 20 --output /tmp/chebi-69704-exact-label-publications.jsonl` | Wrote one PubMed candidate, the same `PMID:21919533` paper. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --provider semantic-scholar --query 'UDWSABBWZXKLLQ-UHFFFAOYSA-N OR CHEBI:69704 OR "antibioticmech:chebi-20fa5cc869"' --limit 20 --output /tmp/chebi-69704-id-publications.jsonl` | PubMed wrote zero candidates; Semantic Scholar returned HTTP 429. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --provider semantic-scholar --query '"4-[3-(2-hydroxy-4-methoxyphenyl)propyl]-2-methoxyphenol" OR "Combretum griffithii"' --limit 20 --output /tmp/chebi-69704-iupac-combretum-publications.jsonl` | PubMed wrote two candidates, including `PMID:21919533`; Semantic Scholar returned HTTP 429. |

No separate single-record term, reference, or history validator is documented in
the local `justfile`. The full `just qc` gate is left for the PR-level check
because this review made no YAML mutation.

## Identity and Grounding

The generated lock row in `data/antibiotics/PATHS.tsv` maps `CHEBI:69704` to
`ANTIMYCOBACTERIAL/1-2-hydroxy-4-methoxyphenyl-3-4-hydroxy-3-methoxyphenyl-propane`,
and `source_concepts` carries only the expected ChEBI upstream identity with
minted ID `antibioticmech:chebi-20fa5cc869`.

The exact structure block matches the committed ChEBI antimicrobial inventory
row for `CHEBI:69704`: SMILES, Standard InChI, InChIKey
`UDWSABBWZXKLLQ-UHFFFAOYSA-N`, formula `C17H20O4`, charge `0`, average mass,
monoisotopic mass, the `CHEBI:64912` role term, the `CHEBI:134251` parent
compound, the IUPAC synonym, and `reaxys:6521737` all agree with
`data/raw/chebi_antimicrobials.tsv`. The official ChEBI OLS term for
`CHEBI:69704` reports the same label, definition, formula, SMILES, Standard
InChI, InChIKey, mass fields, Reaxys xref, PubMed xref, and IUPAC name.

The filing class is consistent with the retained role. OLS resolves
`CHEBI:64912` as `antimycobacterial drug`, while the other ChEBI roles are a
generic `metabolite`, a host anticancer role, and a `plant metabolite` role; the
generated record therefore retained the one in-scope antimicrobial role and did
not import host anticancer or metabolite assertions as antimicrobial activity.

The lone `parent_compounds` entry is a strict broader term. OLS resolves
`CHEBI:134251` as `guaiacols`, matching the committed parent value. No
same-structure cross-reference was found except `reaxys:6521737`.

No local grounding decision or prior review report was found for `CHEBI:69704`,
`antibioticmech:chebi-20fa5cc869`,
`UDWSABBWZXKLLQ-UHFFFAOYSA-N`, the exact label, or the exact slug in
gitignore-independent searches over `data/antibiotics`, `data/raw`, `curation`,
`reports/yaml_record_review`, `.claude`, `docs`, `README.md`, `conf`, `src`,
`scripts`, `tests`, `justfile`, and `pyproject.toml`.

## Evidence

The generated identity, label, definition, exact structure, IUPAC synonym,
Reaxys xref, parent compound, ChEBI grounding, source concept,
antimycobacterial activity role, and grounding status reproduce from the
committed ChEBI inventory with no `verify-corpus` drift.

The official ChEBI term and local raw row both carry `PMID:21919533`.
The PubMed record resolves it to Moosophon et al. 2011, "Diarylpropanes and an
arylpropyl quinone from Combretum griffithii," DOI `10.1021/np200593d`. The
PubMed abstract supports this label as a known diarylpropane isolated from a
methanol extract of *Combretum griffithii* stems and reports that compound 5
had activity against *Mycobacterium tuberculosis* with MIC `3.13 ug/mL`. That
is consistent with the upstream antimycobacterial role, but it is not
mechanism or target evidence.

The `Combretum griffithii` publication query also returned `PMID:23795891`,
another paper on compounds from the same plant. Its PubMed abstract names new
flavans, new diarylpropanes, known flavans, known diarylpropanes, and
beta-sitosterol, but it does not identify `CHEBI:69704` by exact label in the
available abstract and is therefore only a weak discovery lead for this exact
record.

The exact-label, exact PMID, identifier, and IUPAC/plant publication searches
did not return any inspected mechanism paper for `CHEBI:69704`. The record
makes no mode-of-action, molecular-target, activity, resistance, producer,
clinical, or causal-edge claims, so there are no unsupported claim-level
citations in the YAML.

## Completeness

The exact ChEBI identity, structure, ChEBI grounding, IUPAC synonym, source
concept, Reaxys xref, antimycobacterial activity role, and parent compound are
defensible.

The consequential gap is mechanism sign-off. The YAML has no `mode_of_action`,
no `mode_of_action_target_scope`, no `molecular_targets` item, no causal graph,
and no target-specific `EvidenceItem`. `just worklist --limit 0 --tsv
/tmp/chebi-69704-worklist.tsv` therefore keeps the record in the `mechanism`
and `review-readiness` queues.

The PubMed abstract for `PMID:21919533` contains an MIC value for
*M. tuberculosis*, but a complete `ActivityObservation` still needs the exact
strain or isolate, assay method, value qualifier, unit normalization, and
compound identity from the full source before curation.

No resistance assertions, clinical assertions, or public datasets are present.
The record has a `producer-candidate` row for *Combretum griffithii*, but that
candidate comes from "isolated from" ChEBI definition prose and names a plant
source rather than a microbial biosynthesis claim.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record has no antimycobacterial mechanism and cannot satisfy the `REVIEWED` gate until a curator either supports a mechanism for this exact diarylpropane or explicitly records why no mechanism should be asserted. | The target YAML has no `mode_of_action`, no `mode_of_action_target_scope`, no `record_evidence`, no `molecular_targets`, and no `causal_graphs`; `just worklist --limit 0 --tsv /tmp/chebi-69704-worklist.tsv` reports `0 CARD target(s), 0 resistance edge(s) to build on` for the `mechanism` queue and `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)` for the `review-readiness` queue. | Curator-owned evidence, molecular target, activity observation, discussion, or causal-graph additions written to `data/antibiotics/antimycobacterial/1-2-hydroxy-4-methoxyphenyl-3-4-hydroxy-3-methoxyphenyl-propane.yaml` through `write_validated_antibiotic`, if primary literature supports them. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect `PMID:21919533` in full before asserting a mechanism or activity row.
   The PubMed abstract has the exact compound label and an *M. tuberculosis*
   MIC, but not enough target or assay context to curate mechanism or
   `ActivityObservation` fields.
2. If the inspected source reports a compound-specific antimycobacterial target
   or pathway, add a curator-owned `MolecularTarget`,
   `mode_of_action`, `mode_of_action_target_scope: MICROBIAL_TARGET`, and
   claim-level primary evidence.
3. If the paper only reports whole-cell inhibition, leave mechanism fields
   empty and add either a measured `ActivityObservation` with complete strain,
   assay, qualifier, value, units, and evidence, or a `Discussion` explaining
   why the antimycobacterial role is source-supported but the mechanism remains
   unknown.
4. Do not convert the *Combretum griffithii* definition phrase into a
   `producer_organisms` item; it documents plant isolation, not a microbial
   producer.
5. If a mode of action, target, activity observation, discussion, or causal
   graph is supported, write it with a guarded mutator that asserts
   `identifier == "CHEBI:69704"`, updates only curator-owned fields, appends a
   `codex` `CurationEvent` with `llm_assisted: true`, and emits via
   `write_validated_antibiotic`.
6. Move `curation_status` to `REVIEWED` only after identity, structure, filing
   class, and any newly curator-checked mechanism satisfy the
   `docs/CURATION.md` sign-off criteria.

## Follow-up Checks

After a future mechanism or activity curation edit:

- `just validate-strict data/antibiotics/antimycobacterial/1-2-hydroxy-4-methoxyphenyl-3-4-hydroxy-3-methoxyphenyl-propane.yaml --out /tmp/chebi-69704-validate-strict.tsv`
- `just verify-corpus`
- `just qc`
- `git diff -- data/antibiotics/antimycobacterial/1-2-hydroxy-4-methoxyphenyl-3-4-hydroxy-3-methoxyphenyl-propane.yaml curation/decisions.tsv src scripts tests`
- `just review-queue --limit 0 --tsv curation/record_review_queue.tsv`

## Additional Notes

Searches used to establish absence included ignored files:

- `rg --no-ignore --hidden` over `data/antibiotics`, `data/raw`, `curation`,
  `reports/yaml_record_review`, `.claude`, `docs`, `README.md`, `conf`, `src`,
  `scripts`, `tests`, `justfile`, and `pyproject.toml` for `CHEBI:69704`,
  `UDWSABBWZXKLLQ-UHFFFAOYSA-N`, the exact label, and the exact slug.

`NCBI_EMAIL` was unset for the PubMed searches. Semantic Scholar returned HTTP
429 for both non-PubMed searches, so that provider's literature leads were not
available in this pass.

This report is read-only review output. No generated record, upstream
inventory, decision row, page, queue, or curation-history entry was edited.
