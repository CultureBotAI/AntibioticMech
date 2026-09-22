# YAML Record Review: (5R)-5-hydroxy-7-(4''-hydroxy-3''-methoxyphenyl)-1-phenyl-3-heptanone

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antiviral/5r-5-hydroxy-7-4-hydroxy-3-methoxyphenyl-1-phenyl-3-heptanone.yaml`
- Started UTC: 2026-09-22T12:10:28Z
- Finished UTC: 2026-09-22T12:15:08Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:66027` |
| Label | `(5R)-5-hydroxy-7-(4''-hydroxy-3''-methoxyphenyl)-1-phenyl-3-heptanone` |
| Path | `data/antibiotics/antiviral/5r-5-hydroxy-7-4-hydroxy-3-methoxyphenyl-1-phenyl-3-heptanone.yaml` |
| Class | `ANTIVIRAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:66027`, version `2026-08-30`, minted key `antibioticmech:chebi-d457318742` |
| Source roles | `CHEBI:52425` EC 3.2.1.18 (exo-alpha-sialidase) inhibitor |
| Parent compounds | `CHEBI:134251`, `CHEBI:55380` |
| Structure | `JHJPDDBIHSFERA-GOSISDBHSA-N`; formula `C20H24O4`; charge `0` |
| Xrefs | `cas:68622-73-1`; `reaxys:5761856` |
| Source literature leads | `PMID:20091245`, `PMID:731398` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded antiviral record. The YAML has
source-derived exact ChEBI grounding, a ChEBI definition, one exact ChEBI
synonym, two strictly broader ChEBI parents, two xrefs, an EC 3.2.1.18
inhibitor role, source-seeded viral-release mode-of-action fields, structure,
and source-concept metadata. It has no generated or curator-owned molecular
target, activity observation, resistance mechanism, producer, discussion,
dataset, causal graph, or claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiviral/5r-5-hydroxy-7-4-hydroxy-3-methoxyphenyl-1-phenyl-3-heptanone.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antiviral/5r-5-hydroxy-7-4-hydroxy-3-methoxyphenyl-1-phenyl-3-heptanone.yaml --out /tmp/antibioticmech-chebi-66027-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-66027.tsv` | Pass: the full worklist TSV was written. `CHEBI:66027` appears on `mechanism`, `producer-candidate`, `activity-candidate`, and `review-readiness`. |
| `just review-queue --limit 60` | Pass: `CHEBI:66027` is queued with `MECHANISM_REVIEW: mechanism is source-seeded and not curator-checked; 2 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:66027` resolves in official OLS as a current, non-obsolete ChEBI term
with label `(5R)-5-hydroxy-7-(4''-hydroxy-3''-methoxyphenyl)-1-phenyl-3-heptanone`,
the same text definition as the generated record, the exact Standard InChIKey
`JHJPDDBIHSFERA-GOSISDBHSA-N`, the exact formula `C20H24O4`, the exact CAS
cross-reference `68622-73-1`, and the exact IUPAC synonym stored by this
record.

The live OLS graph gives `CHEBI:66027` two `subClassOf` edges: `CHEBI:134251`
`guaiacols` and `CHEBI:55380` `beta-hydroxy ketone`. Those are exactly the
generated `parent_compounds` values, and both parent IDs resolve as current,
non-obsolete ChEBI classes.

The live OLS graph gives `CHEBI:66027` direct `has role` edges to `CHEBI:52425`
`EC 3.2.1.18 (exo-alpha-sialidase) inhibitor` and `CHEBI:76924` `plant
metabolite`. Live OLS resolves `CHEBI:52425` as a current, non-obsolete ChEBI
class; `data/raw/chebi_role_names.tsv` marks it as a `class,mode_of_action`
role; and `conf/sources.yaml` maps it to `ANTIVIRAL`,
`VIRAL_RELEASE_INHIBITION`, and `HOST_SHARED_TARGET`. The generated record
does not store the `plant metabolite` role in `activity_roles`, which is
correct because this corpus imports ChEBI antimicrobial roles there, not
generic chemical roles.

Before this report was created, an ignored-inclusive exact search for
`CHEBI:66027`, the exact label, filename stem, exact Standard InChIKey, exact
CAS, and source PMIDs across `data/antibiotics`, `data/raw`, `curation`, and
`reports/yaml_record_review` found only the expected `PATHS.tsv` row, the
generated YAML, and the raw ChEBI row. No prior dedicated review report,
curation decision, generated activity observation, molecular target,
resistance, producer, dataset, or causal-graph claim resolving `CHEBI:66027`
was present.

## Evidence

The record's antiviral classification and source-seeded release mechanism are
inherited from ChEBI role `CHEBI:52425`, `EC 3.2.1.18 (exo-alpha-sialidase)
inhibitor`. That role is sufficient for the generator to file the record under
`ANTIVIRAL` and infer `VIRAL_RELEASE_INHIBITION` with
`HOST_SHARED_TARGET`; it is not compound-specific primary evidence for a
particular viral neuraminidase, a particular influenza isolate, a measured
assay, or a causal graph edge.

OLS exposes ChEBI PubMed cross-references to `PMID:20091245` and
`PMID:731398`, matching the raw ChEBI source row. `PMID:20091245` is a 2010
Journal of Natural Medicines paper on in-vitro anti-influenza A activity of
ten diarylheptanoids isolated from `Alpinia officinarum`; its PubMed abstract
reports that all ten diarylheptanoids had potential anti-influenza activity and
that compounds 3 and 8 were especially active, but the abstract does not name
exact `CHEBI:66027`, its IUPAC synonym, `68622-73-1`, or neuraminidase.
`PMID:731398` is a 1978 Yakugaku Zasshi chemistry article about the pungent
principle of `Alpinia officinarum`; PubMed has no abstract for it, so it is an
isolation and structure lead rather than inspected claim-level support for a
producer or antiviral assay row.

A bounded PubMed helper search for `Alpinia officinarum diarylheptanoids
neuraminidase` found `PMID:33309269`, a 2020 Bioorganic Chemistry paper on
neuraminidase-inhibitory diarylheptanoids from `Alpinia officinarum`. Its
abstract reports virtual screening, 30 diarylheptanoids, stable binding in NA
for 10 of them, and potent in-vitro NA inhibition by five of them. The abstract
does not name exact `CHEBI:66027`, so this is a future full-text curation lead
for the seeded role, not evidence that can be attached to this exact compound.

Bounded PubMed helper and direct PubMed eSearch queries for the exact Standard
InChIKey `JHJPDDBIHSFERA-GOSISDBHSA-N`, exact CAS `68622-73-1`, exact ChEBI
label, and exact IUPAC synonym returned zero indexed candidates. The bounded
checks therefore identified source-level ChEBI PubMed leads and one
neuraminidase-specific `Alpinia officinarum` lead, but no source that could be
verified from an indexed abstract as an exact activity, molecular-target, or
producer claim for `CHEBI:66027`.

No NCBI Taxonomy verification was needed for this pass because the review did
not add source-organism or susceptible-organism rows. The available snippets
only supplied lead-level `Alpinia officinarum` and influenza contexts that
still require primary-paper curation before any plant producer or viral taxon
can be grounded.

## Completeness

The record is incomplete as a reviewed influenza neuraminidase-inhibitor
record. It has exact ChEBI identity, structure, two xrefs, strictly broader
ChEBI parents, ChEBI EC 3.2.1.18 inhibitor classification, and a generated
mechanism mapping, but no primary-paper evidence, no `activity_spectrum`, no
molecular target, no producer, no dataset, and no causal graph.

The empty molecular target and causal graph slots are correct for the current
seed. ChEBI states a broad EC 3.2.1.18 inhibitor role, and the generated note
correctly warns that this role is also a host-shared target family, but exact
viral-neuraminidase target curation still needs a primary-paper claim for
exact `CHEBI:66027` rather than role text alone.

The empty `activity_spectrum` and producer slots are preferable to over-scoped
filler. `PMID:20091245` is a credible lead for influenza activity, and ChEBI's
definition says the compound was isolated from `Alpinia officinarum`; neither
abstract-level check resolves which named or numbered compound is exact
`CHEBI:66027` with a measured value or proves the plant-source claim from
inspected text.

The empty `resistance_mechanisms`, `clinical_status_assertions`, `datasets`,
and `discussions` slots are also acceptable. No measured resistance edge,
clinical assertion, public dataset accession, or discussion-worthy conflict
with exact `CHEBI:66027` claim-level evidence was identified in the bounded
checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:66027` has source-level ChEBI neuraminidase-inhibitor classification and a generated viral-release mechanism, but no curator-owned primary evidence for exact activity, a molecular target, the `Alpinia officinarum` producer candidate, or a causal graph. | The generated record has two source literature leads, zero record evidence items, zero `activity_spectrum` rows, zero targets, no producer, and no causal graph; OLS supports the ChEBI `has role` assertion, while `PMID:20091245`, `PMID:731398`, and `PMID:33309269` are lead-level abstracts that do not name exact `CHEBI:66027`. | Future curator-owned fields on `data/antibiotics/antiviral/5r-5-hydroxy-7-4-hydroxy-3-methoxyphenyl-1-phenyl-3-heptanone.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI later changes this term's roles, xrefs, parents, or citations, the ChEBI inventory extractor owns that refresh. |

No blocker identity, structure, schema, xref, class, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Inspect `PMID:20091245` and map its compound numbers to exact ChEBI
   structures before adding `activity_spectrum` rows. Require virus or strain,
   assay, measured value, unit, and assertion-level evidence for exact
   `CHEBI:66027`.
2. Inspect `PMID:33309269` before upgrading the broad source-seeded EC 3.2.1.18
   inhibitor role into a reviewed viral-neuraminidase `MolecularTarget` or
   causal graph edge. Require exact compound identity, the assayed
   neuraminidase or virus, assay, and measured value.
3. Inspect `PMID:731398` or a later structure paper before adding
   `Alpinia officinarum` as a producer. Keep the worklist
   `producer-candidate` row unresolved until the source text confirms that
   exact `CHEBI:66027`, rather than only a related diarylheptanoid, was
   isolated from that plant.
4. Add `resistance_mechanisms` only from primary papers that test exact
   `CHEBI:66027` against a stated viral neuraminidase mutant or resistance
   genotype; do not import resistance claims from unrelated neuraminidase
   inhibitors.
5. Continue treating the direct ChEBI `plant metabolite` role as out of scope
   for `activity_roles` unless the source importer gains support for generic
   chemical roles.

## Follow-up Checks

After any exact-term curation or source refresh, rerun:

1. `just validate data/antibiotics/antiviral/5r-5-hydroxy-7-4-hydroxy-3-methoxyphenyl-1-phenyl-3-heptanone.yaml`
2. `just validate-strict data/antibiotics/antiviral/5r-5-hydroxy-7-4-hydroxy-3-methoxyphenyl-1-phenyl-3-heptanone.yaml --out /tmp/antibioticmech-chebi-66027-validation.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-66027.tsv`
5. `just review-queue --limit 60`
6. `just qc`

Manually compare any future activity, mechanism, target, resistance, dataset,
producer, or causal-graph assertion against exact `CHEBI:66027` identity.
Confirm that every claim-level evidence block attaches to the specific object
it supports, not only to the whole ChEBI term, broad neuraminidase-inhibitor
role, or diarylheptanoids as a chemical class.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.

`runoak` was not available in this shell, so official ChEBI term checks were
performed against the EBI OLS4 HTTPS API.
