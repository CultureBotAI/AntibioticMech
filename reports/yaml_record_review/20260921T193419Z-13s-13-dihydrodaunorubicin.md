# YAML Record Review: (13S)-13-dihydrodaunorubicin

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/unspecified/13s-13-dihydrodaunorubicin.yaml`
- Started UTC: `2026-09-21T19:34:19Z`
- Finished UTC: `2026-09-21T19:36:16Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:31031` |
| Label | `(13S)-13-dihydrodaunorubicin` |
| Path | `data/antibiotics/unspecified/13s-13-dihydrodaunorubicin.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:31031`, minted key `antibioticmech:chebi-553e66fcf5`, ChEBI release `2026-08-30` |
| Source role | `CHEBI:33281` antimicrobial agent |

This is a generated, ChEBI-seeded record. The record has one IUPAC synonym,
one broader parent, a neutral `C27H31NO10` structure with InChIKey
`HJEZFVLKJYFNQW-PRFXOSGESA-N`, three structural xrefs, one DrugCentral xref,
one ChEBI source concept, and four seed-time history entries. It has no
record-level `evidence`, `mode_of_action`, `molecular_targets`,
`activity_observations`, `resistance_mechanisms`, `producer_organisms`,
`clinical_status`, `datasets`, or `causal_graph`.

Seeder-owned identity, synonym, parent, xref, role, structure, and source fields
must not be hand-edited in the YAML. If a future review finds that the
ChEBI-sourced antimicrobial role is wrong, the maintained fix belongs in the
ChEBI extractor or in a `curation/decisions.tsv` exclusion for
`antibioticmech:chebi-553e66fcf5` followed by `just seed-apply`. Curator-owned
activity, producer, mechanism, discussion, and causal-graph additions belong in
this record through a guarded mutator that calls `record_curation_event` and
`write_validated_antibiotic`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/13s-13-dihydrodaunorubicin.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/13s-13-dihydrodaunorubicin.yaml --out /tmp/antibioticmech-dihydrodaunorubicin-31031-validation.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 error rows. |
| `just verify-corpus --summary` | Passed; 2939 records expected and on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just review-queue --limit 31` | Confirmed `CHEBI:31031` is the next review queue row after `CHEBI:138224`, with `MECHANISM_REVIEW`, 0 source literature leads, 0 record evidence items, and 0 targets. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-dihydrodaunorubicin-31031.tsv` | Wrote the full worklist. `CHEBI:31031` appears on `mechanism` and `review-readiness` only; there are no activity or producer candidate rows for this record. |
| Single-record term/reference/history validators | Not checked: no narrower term, reference, or history validator is exposed for a single ChEBI-seeded record. The documented focused checks are the single-record schema gates plus the full-corpus `verify-corpus`, `worklist`, and `review-queue` diagnostics. |

`printenv NCBI_EMAIL` was unset, so publication discovery used
`env -u NCBI_EMAIL uv run python scripts/search_publications.py ...`.

## Identity and Grounding

The exact ChEBI grounding is coherent. The official ChEBI entry for
`CHEBI:31031` matches the seeded label, ASCII label, formula `C27H31NO10`,
neutral charge, average mass `529.542`, monoisotopic mass `529.19480`, SMILES,
Standard InChI, and InChIKey `HJEZFVLKJYFNQW-PRFXOSGESA-N`.

The seeded relationships also match ChEBI:

| Seeded item | Upstream support |
|---|---|
| IUPAC synonym | ChEBI lists the same IUPAC name for this exact stereochemical form. |
| `CHEBI:31059` | ChEBI asserts `(13S)-13-dihydrodaunorubicin is a 13-dihydrodaunorubicin`. |
| `CHEBI:33281` | ChEBI lists the biological role `antimicrobial agent`. |
| `kegg.compound:C12433` | ChEBI lists the KEGG xref; KEGG `C12433` names `(13S)-13-Dihydrodaunorubicin`, `Daunorubicinol`, and `13-Dihydrodaunorubicin`, and its DBLINKS include `ChEBI: 31031` and `LIPIDMAPS: LMPK13050005`. |
| `lipidmaps:LMPK13050005` | Listed by both ChEBI and KEGG for the same entry. |
| `drugcentral:4719` | Listed by ChEBI as a manual xref. |
| `reaxys:6773803` | Listed by ChEBI as a registry number. |

The neighboring record `data/antibiotics/unspecified/13-dihydrodaunorubicin.yaml`
is a broader ChEBI concept with a different identifier. This review targeted
only the `(13S)` diastereomer in `CHEBI:31031`.

## Evidence

The ChEBI inventory row for `CHEBI:31031` carries no `PMID:` or `DOI:` leads.
That makes this a pure database-seeded stub: the current YAML inherits ChEBI's
3-star structure and antimicrobial role assertion but has no inspected
publication support on the record itself.

Targeted PubMed searches by the exact label, `13-dihydrodaunorubicin`,
`13-dihydrodaunomycin`, `daunorubicinol`, KEGG `C12433`, and
`HJEZFVLKJYFNQW` found papers in three adjacent buckets:

| Lead | Scope of support |
|---|---|
| `PMID:38658424` | Reports reducing `(13S)-13-dihydrodaunorubicin` production by deleting `dnrU` during engineered `Streptomyces peucetius` doxorubicin production. This is a producer/biosynthetic byproduct lead, not direct antimicrobial activity evidence. |
| `PMID:9864343` and `PMID:9098063` | Show Streptomyces DoxA acts on 13-dihydrodaunorubicin in daunorubicin/doxorubicin biosynthesis. The abstracts do not establish an assay organism, MIC, or antimicrobial mechanism for the `(13S)` record. |
| `PMID:8655530` | Reports doxA-mediated bioconversion of daunomycin and 13-dihydrodaunomycin to doxorubicin; useful as biosynthesis context, not antimicrobial activity support. |
| `PMID:838632` | Reports microbial reduction of daunorubicin to 13-dihydrodaunorubicin, daunorubicinol/daunomycinol. This does not establish the producing organism as a natural source of the exact ChEBI structure. |
| `PMID:8373745` and `PMID:1777431` | Report DNA-binding calculations or nucleic-acid equilibrium binding for 13-dihydrodaunomycin. These are host/toxicity or antitumor target leads, not microbe-specific antimicrobial mechanism evidence. |
| Recent daunorubicinol pharmacology hits | Mostly cover mammalian metabolism, cardiotoxicity, and anthracycline reductases; they do not support a bacterial, fungal, protozoal, or viral activity claim. |

No inspected source in the bounded searches resolved a microbial target,
antimicrobial MIC, resistance route, or causal graph for the exact `(13S)`
compound.

## Completeness

The `mechanism` queue is correct: the record has a ChEBI antimicrobial role but
no curated `mode_of_action`, `mode_of_action_target_scope`,
`molecular_targets`, or `causal_graph`.

The absence of `producer_organisms` and `activity_observations` is also
unresolved. The worklist has no producer or activity candidate for `CHEBI:31031`,
and the ChEBI page lists no species-of-metabolite entries or citations. The
engineered `S. peucetius` and DoxA papers should be inspected before any
producer claim is added, because the abstracts show the compound in a
bioconversion or doxorubicin-production context rather than as a direct natural
product assertion for this record.

The empty `resistance_mechanisms` field is expected for this ChEBI-only record:
the mechanism worklist reports 0 CARD targets and 0 CARD resistance edges to
build on. The empty `clinical_status`, `datasets`, and `molecular_targets`
fields should stay empty until a source supports exact claims.

Exhaustive local searches included ignored files where an absence mattered:

- `find reports/yaml_record_review -maxdepth 1 -name '*dihydrodaunorubicin*' -print`
  found no prior report for this record; `find` includes ignored reports.
- `rg --no-ignore --hidden` over `data/raw`, `curation`, and
  `data/antibiotics` for `CHEBI:31031`, the exact label, the filename slug,
  `HJEZFVLKJYFNQW`, `C12433`, and related xrefs found only the expected
  `PATHS.tsv` row, the ChEBI inventory row, the queue row, and the target YAML.
  It found no curated decision row, curator-owned source row, or existing local
  curation for the `(13S)` record.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| `DIHYDRODAUNORUBICIN-31031-M1` | major | `CHEBI:31031` is a ChEBI-seeded antimicrobial record with no source literature leads, no record evidence, no activity observations, no candidate activity or producer worklist rows, and no mechanism. The official identity is coherent, but this corpus still lacks inspected primary evidence that the exact `(13S)` metabolite has antimicrobial activity or a microbe-relevant mechanism. | `data/antibiotics/unspecified/13s-13-dihydrodaunorubicin.yaml` via a guarded curator mutator for literature-backed additions; if the antimicrobial role itself is unsupported, own the exclusion or role handling through `curation/decisions.tsv` or the ChEBI extractor rather than patching generated fields. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect full text for the exact-name biosynthesis hits, especially
   `PMID:38658424`, `PMID:9864343`, `PMID:9098063`, `PMID:8655530`, and
   `PMID:838632`, to determine whether any source supports a precise
   `producer_organisms` entry for the `(13S)` compound.
2. Trace the ChEBI provenance for `CHEBI:33281` on `CHEBI:31031`. If the role
   is only inherited from anthracycline drug vocabulary or antitumor use, add a
   source exclusion or extractor rule; if it is experimentally antimicrobial,
   add claim-level `activity_observations`.
3. Search backward from any paper that reports antimicrobial activity for a
   direct molecular target. Add `mode_of_action`, a taxon-agnostic
   `molecular_targets` entry, and a causal graph only if a primary source
   supports the exact `(13S)` structure and the microbe-relevant mechanism.
4. If no activity or mechanism can be verified after bounded full-text review,
   add a `CURATION_TODO` discussion documenting the unresolved ChEBI role and
   leave mechanism fields empty.

## Follow-up Checks

- Re-run
  `just validate-strict data/antibiotics/unspecified/13s-13-dihydrodaunorubicin.yaml --out /tmp/antibioticmech-dihydrodaunorubicin-31031-validation.tsv`
  after any guarded record edit.
- Re-run `just verify-corpus --summary` to prove that no seed-owned ChEBI field
  drifted and any curator-owned additions survive reseeding.
- Re-run `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-dihydrodaunorubicin-31031.tsv`
  to confirm whether `CHEBI:31031` remains on `mechanism` after the role and
  mechanism are curated.
- Re-run `just lint` and `git diff --check` before committing any future
  curation change.

## Additional Notes

KEGG `C12433` reports CAS `28008-55-1`, but ChEBI does not currently list a CAS
registry number for `CHEBI:31031`; the generated YAML therefore correctly lacks
one instead of synthesizing an xref from KEGG.

The official ChEBI page lists `metabolite` as a role in addition to
`antimicrobial agent`, but the extractor correctly preserved only
`CHEBI:33281` because `metabolite` is not an antimicrobial role term.
