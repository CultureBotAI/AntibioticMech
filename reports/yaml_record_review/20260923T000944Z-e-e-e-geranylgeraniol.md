# YAML Record Review: (E,E,E)-geranylgeraniol

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antiprotozoal/e-e-e-geranylgeraniol.yaml`
- Started UTC: 2026-09-23T00:04:00Z
- Finished UTC: 2026-09-23T00:09:44Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:46762` |
| Label | `(E,E,E)-geranylgeraniol` |
| Path | `data/antibiotics/antiprotozoal/e-e-e-geranylgeraniol.yaml` |
| Class | `ANTIPROTOZOAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:46762`, version `2026-08-30`, minted key `antibioticmech:chebi-5dccfe57c9` |
| Source role | `CHEBI:70868` antileishmanial agent |
| Parent compound | `CHEBI:24229` geranylgeraniol |
| Structure | `OJISWRZIEWCUBN-QIRCYJPOSA-N`; formula `C20H34O`; charge `0` |
| Source literature leads | None |
| Evidence-bearing objects | None |

This review covered one ChEBI-seeded exact `(E,E,E)-geranylgeraniol` record.
The YAML has exact ChEBI grounding, a ChEBI definition, two exact ChEBI
synonyms, one ChEBI related synonym, one broader ChEBI parent, one
antileishmanial activity role, chemical structure fields, exact ChEBI xrefs, a
ChEBI Wikipedia document xref, and source-concept metadata. It has no generated
or curator-owned activity observation, molecular target, resistance mechanism,
mode of action, producer, discussion, dataset, causal graph, or claim-level
evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiprotozoal/e-e-e-geranylgeraniol.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antiprotozoal/e-e-e-geranylgeraniol.yaml --out /tmp/antibioticmech-e-e-e-geranylgeraniol-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-e-e-e-geranylgeraniol-worklist.tsv` | Pass: the full worklist TSV was written. Exact `CHEBI:46762` appears on `mechanism` and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 86` | Pass: `CHEBI:46762` is the first queued record after the already-reviewed `(E,E)-germacrone`; its row says `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `uv run runoak -i ols:chebi labels CHEBI:46762 CHEBI:24229 CHEBI:70868` | Partial, then pass: the first OLS request resolved `CHEBI:46762` as `(E,E,E)-geranylgeraniol` and `CHEBI:24229` as `geranylgeraniol` before timing out; a focused retry resolved `CHEBI:70868` as `antileishmanial agent`. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query 'geranylgeraniol[Title/Abstract] AND (Leishmania[Title/Abstract] OR antileishmanial[Title/Abstract] OR antiprotozoal[Title/Abstract] OR protozoa[Title/Abstract] OR protozoal[Title/Abstract])' --limit 20 --output /tmp/antibioticmech-e-e-e-geranylgeraniol-antiprotozoal-pubmed.jsonl` | Pass: PubMed returned 4 bounded antiprotozoal candidates. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --provider semantic-scholar --query 'geranylgeraniol Leishmania antileishmanial antiprotozoal' --limit 20 --output /tmp/antibioticmech-e-e-e-geranylgeraniol-publications.jsonl` | Partial pass: PubMed returned 2 broader candidates; Semantic Scholar returned HTTP 429. |
| `git diff --cached --check` | Pass: no staged whitespace or path errors. |
| `just lint` | Pass: Ruff exited successfully. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`data/raw/chebi_antimicrobials.tsv` seeds `CHEBI:46762` as a 3-star ChEBI
entry in antimicrobial role scope and gives the same label, definition, SMILES,
Standard InChI, Standard InChIKey, formula, charge, masses, ChEBI parent,
synonyms, xrefs, and absence of source PMIDs that appear in or explain the
generated YAML. OAK through OLS resolved the identifier as
`(E,E,E)-geranylgeraniol`, its parent as `geranylgeraniol`, and its source role
as `antileishmanial agent`.

The generated `ANTIPROTOZOAL` filing class follows `conf/sources.yaml`:
`CHEBI:70868` maps to `ANTIPROTOZOAL` and is the only source role imported for
this ChEBI concept. The record preserves the all-trans child identity rather
than the stereochemically unspecified parent `CHEBI:24229` or the sibling
`CHEBI:18822` `(Z,Z,Z)-geranylgeraniol`. The reviewed YAML, `PATHS.tsv`, and
raw ChEBI row all use the Standard InChIKey `OJISWRZIEWCUBN-QIRCYJPOSA-N` and
the `/b18-11+,19-13+,20-15+` Standard InChI bond layer.

Ignored-inclusive searches over the raw ChEBI inventory, generated antibiotic
records, generated path map, curation directory, review queue, and ignored
`reports/yaml_record_review` directory found no previous
`(E,E,E)-geranylgeraniol` review report and no maintained curation decision,
curator-inventory row, generated activity observation, molecular target,
resistance edge, producer, dataset, or causal-graph claim resolving exact
`CHEBI:46762`.

## Evidence

The record's antiprotozoal class comes from the broad ChEBI `CHEBI:70868`
`antileishmanial agent` role. That role is sufficient for the generator to
file the record under `ANTIPROTOZOAL`, but it is not assertion-level primary
evidence for a particular `Leishmania` taxon, strain, assay, IC50 value,
molecular target, resistance mechanism, or causal graph edge.

ChEBI stores no source PMIDs on the exact all-trans `CHEBI:46762` record in
the 2026-08-30 inventory. The parent `CHEBI:24229` geranylgeraniol raw row
does carry four source PMIDs, including `PMID:23304195` and `PMID:23983115`,
but those parent-record leads do not automatically establish exact
stereochemical support for the all-trans child.

The focused PubMed query returned one direct pure-geranylgeraniol lead:
`PMID:23304195`, "Mitochondria Superoxide Anion Production Contributes to
Geranylgeraniol-Induced Death in Leishmania amazonensis." Its abstract reports
geranylgeraniol activity against `Leishmania amazonensis` promastigotes and
intracellular amastigotes with IC50 values, and electron-microscopy,
Rhodamine 123, TUNEL, and superoxide-anion experiments consistent with
mitochondrial damage and apoptosis-like cell death. That paper is the strongest
future exact-activity and mechanism lead, but its abstract does not provide the
parasite strain and does not explicitly state the `E,E,E` stereochemical form.

The remaining PubMed candidates are weaker mixture or extract leads.
`PMID:23983115` measured antileishmanial activity of essential oil from
`Bixa orellana` seeds in which geranylgeraniol was a 9.1% constituent,
`PMID:27725158` measured `Pterodon pubescens` fruit extracts and attributed
activity to a geranylgeraniol derivative, and `PMID:38852132` tested plant
extracts that GC-MS detected as containing trans-geranylgeraniol among several
candidate active substances. These abstracts should remain literature leads
unless full text reports an activity measurement for isolated exact
`(E,E,E)-geranylgeraniol`.

Semantic Scholar returned HTTP 429 for the broader repository
publication-helper search; PubMed returned the bounded search results.

## Completeness

The record is incomplete as a reviewed antileishmanial record. It has exact
ChEBI identity, structure, a broader ChEBI parent, an antileishmanial source
role, exact database xrefs, and no ChEBI source-paper leads, but no
claim-level evidence, no `activity_spectrum`, no molecular target, no
resistance mechanism, no mode of action, no dataset, and no causal graph.

The empty molecular target, mode-of-action, resistance, and causal-graph slots
are correct for the current seed. The inspected PubMed abstracts provide
antileishmanial activity and mitochondrial-damage leads, but they do not yet
support a schema-ready exact all-trans `MolecularTarget`, target scope, or
directed causal edge without full-text review.

The empty `activity_spectrum` slot should be treated as missing curation, not
as negative activity. `PMID:23304195` is a direct geranylgeraniol activity
lead, but exact stereochemistry, strain, assay, endpoint, value, unit, and
host-cell selectivity details still need full-paper extraction before any row
can be added.

The empty `producers`, `clinical_status_assertions`, `datasets`, and
`discussions` slots are acceptable for the generated record. No clinical
assertion, public dataset accession, or discussion-worthy conflict with exact
`CHEBI:46762` claim-level evidence was identified in the bounded checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:46762` has source-level ChEBI antileishmanial classification, but no curator-owned primary evidence for exact all-trans activity, no activity observation, no molecular target, no mode of action, and no causal graph. | The generated record has zero source literature leads, zero record evidence items, zero `activity_spectrum` rows, zero targets, no resistance edges, no mode-of-action fields, and no causal graph. The worklist flags exact `CHEBI:46762` for `mechanism` and `review-readiness` only. `PMID:23304195` is a direct geranylgeraniol antileishmanial lead, but exact all-trans support and schema-ready strain/assay details need full-text extraction. | Future curator-owned fields on `data/antibiotics/antiprotozoal/e-e-e-geranylgeraniol.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI later changes this term's roles, parentage, xrefs, or citations, the ChEBI inventory extractor owns that refresh. |

No blocker identity, structure, schema, parentage, class, audit-history, or
known xref-conflict findings were found.

No minor findings.

## Recommended Edits

1. Inspect `PMID:23304195` in full and add exact `ActivityObservation` rows for
   geranylgeraniol only if the paper preserves or makes inferable the
   all-trans form, `Leishmania amazonensis` strain or isolate, assay method,
   endpoint type, value, and unit.
2. Use `PMID:23304195` as a mechanism lead only after full-text review confirms
   whether the reported mitochondrial depolarization, ultrastructural damage,
   and superoxide anion production can be represented by a
   compound-specific `ModeOfActionEnum`, `MolecularTarget`, or causal graph for
   exact `(E,E,E)-geranylgeraniol`.
3. Treat `PMID:23983115` as essential-oil evidence only unless its full text
   separates an isolated geranylgeraniol assay from the `Bixa orellana` oil
   mixture.
4. Treat `PMID:27725158` as extract and derivative evidence only unless its
   full text reports isolated all-trans geranylgeraniol activity; do not use
   geranylgeraniol-derivative activity to curate exact `CHEBI:46762`.
5. Treat `PMID:38852132` as plant-extract composition evidence only unless its
   full text tests pure trans-geranylgeraniol against defined `Leishmania`
   strains.

## Follow-up Checks

After any exact-term curation or source refresh, rerun:

1. `just validate data/antibiotics/antiprotozoal/e-e-e-geranylgeraniol.yaml`
2. `just validate-strict data/antibiotics/antiprotozoal/e-e-e-geranylgeraniol.yaml --out /tmp/antibioticmech-e-e-e-geranylgeraniol-validation.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-e-e-e-geranylgeraniol-worklist.tsv`
5. `just review-queue --limit 86`
6. `just qc`

Manually compare future activity, mechanism, target, and causal-graph curation
against the full geranylgeraniol, Bixa-essential-oil, Pterodon-extract, and
Hypericum/Eryngium plant-extract papers to confirm that every curated claim is
attached to exact `(E,E,E)-geranylgeraniol` rather than the stereochemically
unspecified geranylgeraniol parent, `(Z,Z,Z)-geranylgeraniol`, an essential-oil
mixture, a plant extract, or a geranylgeraniol derivative.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, `find`, or
Git/GitHub ref listing, so they included ignored `reports/` files or otherwise
did not depend on Git's ignore filters.
