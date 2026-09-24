# YAML Record Review: (S)-nadifloxacin

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antibacterial/s-nadifloxacin.yaml
- Started UTC: 2026-09-24T00:37:00Z
- Finished UTC: 2026-09-24T00:41:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | CHEBI:37908 |
| Label | (S)-nadifloxacin |
| Path | data/antibiotics/antibacterial/s-nadifloxacin.yaml |
| Class | ANTIBACTERIAL |
| Curation status | SEEDED |
| Grounding status | EXACT |
| Maintained owner | Generated from `data/raw/` ARO and ChEBI inventories; do not hand-edit the generated YAML |
| Source concepts | ARO / ARO:3005120 / `antibioticmech:aro-6c3d2579b5`; CHEBI / CHEBI:37908 / `antibioticmech:chebi-b0f94261f2` |

The entire target YAML was read before judging the record. The generated record contains seeded ChEBI identity, role, structure, `beilstein:7084299`, PubChem CID `9850038`, merged ARO `levonadifloxacin`, and source-concept fields only: it has no `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, `activity_spectrum`, `resistance_mechanisms`, `producer_organisms`, `causal_graphs`, `datasets`, `discussions`, or record-level `evidence`.

## Validation

| Check | Result |
|---|---|
| `rg --no-ignore --hidden --files -g AGENTS.md` | Passed; no repo-local `AGENTS.md` was found, with hidden and ignored files included. |
| `rg --no-ignore --hidden 'CHEBI:37908\|\(S\)-nadifloxacin\|s-nadifloxacin' data/antibiotics/PATHS.tsv data/raw curation reports/yaml_record_review` | Passed; resolved the target YAML, the ARO/PubChem/ChEBI raw rows, the `PATHS.tsv` row, and the `review-readiness` row. The only pre-existing report hit was a contextual `(S)-nadifloxacin` mention in the prior `(R)-nadifloxacin` report. |
| `find reports/yaml_record_review -name '*s-nadifloxacin*' -print` | Passed; no prior `s-nadifloxacin` report file was found, with ignored files included. |
| `just validate data/antibiotics/antibacterial/s-nadifloxacin.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/antibiotics/antibacterial/s-nadifloxacin.yaml --out /tmp/s-nadifloxacin-validate-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2,939 records expected and present, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just review-queue --limit 130` | Passed; regenerated the review-readiness queue and reported 2,859 unsigned records. |
| `just worklist --limit 0 --tsv /tmp/s-nadifloxacin-worklist.tsv` | Passed; wrote 8,252 rows. `CHEBI:37908` appears on the `mechanism`, `activity-candidate`, and `review-readiness` queues. |
| `just lint` | Passed; Ruff reported all checks passed. |
| Narrow single-record term/reference/history validators | Not available for plain generated ARO/ChEBI records; the repository exposes schema validation for a single record plus full-corpus generated-state and worklist checks. |

## Identity and Grounding

The record denotes the same individual ChEBI structure named by the target:

- The official EBI OLS search for `CHEBI:37908` returned one defining ChEBI term with label `(S)-nadifloxacin`.
- The official OLS term detail for `CHEBI:37908` is non-obsolete and matched the generated exact synonym, SMILES, Standard InChI, Standard InChIKey `JYJTVFIEFKZWCJ-JTQLQIEISA-N`, formula `C19H21FN2O4`, charge `0`, average mass `360.385`, monoisotopic mass `360.14854`, and `beilstein:7084299`.
- The official OLS parent lookup for `CHEBI:37908` returned `CHEBI:31889` / `nadifloxacin`; that broader parent has a Standard InChIKey without stereochemical assignment (`JYJTVFIEFKZWCJ-UHFFFAOYSA-N`), so the record's `parent_compounds: CHEBI:31889` is a broader stereochemical parent rather than an equivalent exact xref.
- The official OLS term lookups for `CHEBI:33281` and `CHEBI:36047` returned non-obsolete `antimicrobial agent` and `antibacterial drug` roles.
- The official PubChem PUG response for CID `9850038` matched the generated molecular formula `C19H21FN2O4`, Standard InChI, Standard InChIKey `JYJTVFIEFKZWCJ-JTQLQIEISA-N`, monoisotopic mass `360.14853532`, charge `0`, and isomeric SMILES stereochemistry.
- An ignored-inclusive YAML search for `standard_inchi_key: JYJTVFIEFKZWCJ-JTQLQIEISA-N` under `data/antibiotics -g '*.yaml'` found only this record, so no other curated YAML currently duplicates this exact ChEBI structure.

No grounding conflict was found. Future fixes to seeded identity, structure, class, role, parent, xref, or source-concept fields would be owned by `data/raw/aro_antibiotics.tsv`, `data/raw/pubchem_structures.tsv`, `data/raw/chebi_antimicrobials.tsv`, `curation/decisions.tsv`, the extractor, or the seeder rather than by direct record edits.

## Evidence

Existing evidence-backed claim objects are absent, so there were no claim-level citations, snippets, molecular-target assertions, resistance mechanisms, activity observations, producer claims, datasets, or causal edges to verify.

Bounded literature checks found exact-structure and exact-name leads, but not enough primary mechanism support to populate the record directly:

- `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query 'levonadifloxacin' --limit 100 --output /tmp/s-nadifloxacin-levonadifloxacin-pubmed.jsonl` returned 48 PubMed candidates.
- `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query 'nadifloxacin enantiomer' --limit 50 --output /tmp/s-nadifloxacin-enantiomer-pubmed.jsonl` returned 7 PubMed candidates.
- `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query '31920285[PMID] OR 11709337[PMID] OR 42670252[PMID]' --limit 10 --output /tmp/s-nadifloxacin-known-pmids.jsonl` returned the seeded levonadifloxacin review, a racemic nadifloxacin target-preference paper, and an exact enantioresolution lead.
- PMID:42670252 / DOI:10.1002/chir.70143 is exact for separated nadifloxacin enantiomers; its abstract reports that `(S)-nadifloxacin` is more potent than racemate and 64- to 256-fold more active than `(R)-nadifloxacin` against *Staphylococcus aureus*, *Propionibacterium acnes*, and other pathogens. That supports the enantiomer caution but is not a mechanism paper.
- PMID:31920285 / DOI:10.2147/dddt.s229882 is the seeded ARO lead for levonadifloxacin; its abstract summarizes the anti-MRSA spectrum and DNA gyrase-preference mechanism, but it is a review and should be mined for primary source papers before adding target assertions.
- PMID:11709337 / DOI:10.1128/aac.45.12.3544-3547.2001 assays racemic nadifloxacin target preference in *S. aureus* mutant strains and reports DNA gyrase preference for that stereochemically broader concept. It is a useful follow-up lead, not exact support for `CHEBI:37908`.
- `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --provider semantic-scholar --query '(S)-nadifloxacin levonadifloxacin DNA gyrase topoisomerase MIC antibacterial' --limit 20 --output /tmp/s-nadifloxacin-mech-pub.jsonl` found no PubMed candidates; Semantic Scholar returned HTTP 429.

## Completeness

The record is structurally complete enough for a generated exact ARO/ChEBI merge:

- Identity and structure are grounded to ChEBI and reproduce from `data/raw/chebi_antimicrobials.tsv`.
- CARD ARO's `levonadifloxacin` concept is merged through the same PubChem CID and exact Standard InChIKey.
- ChEBI's broader `nadifloxacin` term is retained as `parent_compounds`, not mis-modeled as an equivalent `xrefs` value.
- The one Beilstein xref and the ARO/PubChem xrefs are present.
- The ChEBI `antimicrobial agent` and `antibacterial drug` roles are retained as `activity_roles`.

Consequential gaps remain:

- No mode of action has been curated.
- No target scope has been curated.
- No DNA gyrase or topoisomerase IV target has been curated.
- No organism- or strain-scoped MIC, disk diffusion, or other `ActivityObservation` has been curated.
- No resistance phenotype, causal graph, or exact-enantiomer dataset has been curated.

The full worklist row for `CHEBI:37908` reports `mechanism	CHEBI:37908	(S)-nadifloxacin	ARO+CHEBI	fluoroquinolone antibiotic	0 CARD target(s), 0 resistance edge(s) to build on` and `review-readiness	CHEBI:37908	(S)-nadifloxacin	ARO+CHEBI	PMID:31920285	MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `CHEBI:37908` is not mechanism-reviewed: it lacks `mode_of_action`, target scope, molecular targets, resistance mechanisms, and a causal graph for exact `(S)-nadifloxacin` / levonadifloxacin. | The target YAML has no mechanism or target fields; `just worklist --limit 0 --tsv /tmp/s-nadifloxacin-worklist.tsv` lists `mechanism	CHEBI:37908	(S)-nadifloxacin	ARO+CHEBI	fluoroquinolone antibiotic	0 CARD target(s), 0 resistance edge(s) to build on`; the review-readiness row reports `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. | `data/antibiotics/antibacterial/s-nadifloxacin.yaml`, written through a validated curation mutator that calls `record_curation_event` and `write_validated_antibiotic`. |
| Blocker | None found. Identity, exact ARO/ChEBI grounding, seeded structure, xref placement, source concepts, and corpus reproduction all check out. | See `Identity and Grounding` and `Validation`. | Not applicable. |
| Minor | None found. | Not applicable. | Not applicable. |

## Recommended Edits

1. Curate levonadifloxacin mechanism evidence from exact-drug primary literature, or record a bounded `UNKNOWN`/`CURATION_TODO` discussion if the available DNA gyrase and topoisomerase literature proves review-only or racemate-scoped.
   - Maintained path: `data/antibiotics/antibacterial/s-nadifloxacin.yaml` through a guarded `/tmp` mutator using `record_curation_event(..., curator="codex", llm_assisted=True)` and `write_validated_antibiotic`.
   - Expected fields: `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets` for bacterial DNA gyrase and/or topoisomerase IV only if the inspected source supports that exact target relationship, and `causal_graphs` only after every directed edge has primary evidence.

2. Curate organism- or strain-scoped activity observations only from sources that report reference-compatible quantitative measurements for levonadifloxacin.
   - Maintained path: `data/antibiotics/antibacterial/s-nadifloxacin.yaml` through the same guarded write path.
   - Expected fields: `ActivityObservation` entries with organism or strain, assay method, CLSI/EUCAST interpretive context when present, numeric value and qualifier, units for each MIC or inhibition measurement, and claim-level `EvidenceItem` values.

## Follow-up Checks

- Use PMID:31920285 as a bibliography seed and inspect the levonadifloxacin primary studies it cites for DNA gyrase preference, topoisomerase IV inhibition, efflux behavior, low mutant-prevention concentration, and *S. aureus* resistance-suppression assays.
- Inspect full text for PMID:42670252 to decide whether the separated `(S)-nadifloxacin` antibacterial measurements are quantitative enough for `ActivityObservation` rows.
- Inspect full text for PMID:11709337 only as a stereochemically broader nadifloxacin target-preference lead; do not attach its claims to `CHEBI:37908` unless the paper identifies the exact enantiomer.
- Retry Semantic Scholar after its 429 clears with `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider semantic-scholar --query '"levonadifloxacin" DNA gyrase topoisomerase MIC' --limit 50 --output /tmp/s-nadifloxacin-followup-semscholar.jsonl`.
- After any curation edit, run `just validate-strict data/antibiotics/antibacterial/s-nadifloxacin.yaml --out /tmp/s-nadifloxacin-strict-after.tsv`.
- Run `just verify-corpus` and confirm curator-owned mechanism additions persist without drift.
- Run `just worklist --queue mechanism --limit 0 --tsv /tmp/antibioticmech-mechanism-after.tsv` and verify `CHEBI:37908` leaves the mechanism queue if a concrete mechanism is added.
- Run `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-after.tsv` and verify the row moves from `MECHANISM_REVIEW` to the next unresolved evidence gate.
- Run `just qc` before opening a curation PR.

## Additional Notes

- Search results, PubMed abstracts, OLS responses, and PubChem responses were treated as leads or identifier checks only; no generated report asserts a new biological mechanism from them.
- Publication discovery was run with `NCBI_EMAIL` unset, as required by `.claude/skills/curate-yaml-record/SKILL.md`.
- Google Scholar was not queried because it uses SerpAPI and requires explicit approval.
- No generated YAML was edited.
