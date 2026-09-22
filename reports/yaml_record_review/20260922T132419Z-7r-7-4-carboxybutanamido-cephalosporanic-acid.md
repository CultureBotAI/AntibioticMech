# YAML Record Review: (7R)-7-(4-carboxybutanamido)cephalosporanic acid

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/unspecified/7r-7-4-carboxybutanamido-cephalosporanic-acid.yaml`
- Started UTC: 2026-09-22T13:24:19Z
- Finished UTC: 2026-09-22T13:24:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:41425` |
| Label | `(7R)-7-(4-carboxybutanamido)cephalosporanic acid` |
| Path | `data/antibiotics/unspecified/7r-7-4-carboxybutanamido-cephalosporanic-acid.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:41425`, version `2026-08-30`, minted key `antibioticmech:chebi-fe620cfd4f` |
| Source role | `CHEBI:33281` antimicrobial agent |
| Parent compound | `CHEBI:23066` cephalosporin |
| Structure | `IXUSDMGLUJZNFO-BXUZGUMPSA-N`; formula `C15H18N2O8S`; charge `0` |
| Xrefs | `beilstein:1183847`; `cas:27920-90-7`; `kegg.compound:C15666`; `pdb-ccd:CEN` |
| Source literature leads | None |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded record for neutral
glutaryl-7-aminocephalosporanic acid. The YAML has exact ChEBI grounding, seven
exact ChEBI synonyms, one strictly broader ChEBI parent, four xrefs, the broad
ChEBI antimicrobial-agent role, structure, and source-concept metadata. It has
no generated or curator-owned mode of action, molecular target, activity
observation, resistance mechanism, producer, dataset, discussion, causal graph,
or claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/7r-7-4-carboxybutanamido-cephalosporanic-acid.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/7r-7-4-carboxybutanamido-cephalosporanic-acid.yaml --out /tmp/antibioticmech-chebi-41425-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-41425.tsv` | Pass: the full worklist TSV was written. `CHEBI:41425` appears on `mechanism` and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 65` | Pass: `CHEBI:41425` is queued with `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:41425` resolves in official OLS as a current, non-obsolete ChEBI term
with label `(7R)-7-(4-carboxybutanamido)cephalosporanic acid`, no text
definition, the exact Standard InChIKey `IXUSDMGLUJZNFO-BXUZGUMPSA-N`, the
exact formula `C15H18N2O8S`, the exact CAS cross-reference `27920-90-7`, and
the exact `beilstein:1183847`, `kegg.compound:C15666`, and `pdb-ccd:CEN` xrefs
stored by this record.

The live OLS term exposes the same exact synonyms stored in the YAML. The
IUPAC-name synonym is duplicated upstream in the OLS term JSON, but the
generated YAML stores it once, which is the correct local representation.

The live OLS graph gives `CHEBI:41425` one direct `subClassOf` edge:
`CHEBI:23066` `cephalosporin`. That is exactly the generated
`parent_compounds` value. The graph also exposes a `has functional parent` edge
to `CHEBI:23064` `cephalosporanic acid` and a protonation edge to
`CHEBI:58693` `(7R)-7-(4-carboxylatobutanamido)cephalosporanate`; those are not
strict subclass parentage and are correctly absent from `parent_compounds`.

The committed ChEBI inventory row carries role `CHEBI:33281` `antimicrobial
agent`; `data/raw/chebi_role_names.tsv` marks that role as a broad `scope`
role; and `conf/sources.yaml` maps it to the generated
`ANTIMICROBIAL_UNSPECIFIED` filing class. That role is generic, but it is the
only ChEBI antimicrobial role on this source row, so the record was filed under
the lowest-priority generic class without erasing source role provenance.

Before this report was created, an ignored-inclusive exact search for
`CHEBI:41425`, the exact record path, exact Standard InChIKey, exact CAS, and
all four xrefs across `data/antibiotics`, `data/raw`, `curation`, and
`reports/yaml_record_review` found only the expected generated YAML, `PATHS.tsv`
row, raw ChEBI row, and `record_review_queue.tsv` row. No prior dedicated
review report for
`data/antibiotics/unspecified/7r-7-4-carboxybutanamido-cephalosporanic-acid.yaml`
was found.

## Evidence

The record's antimicrobial classification is inherited from committed ChEBI
role `CHEBI:33281`, `antimicrobial agent`. That broad role is sufficient for
the generator to file the record under `ANTIMICROBIAL_UNSPECIFIED`; it is not
compound-specific primary evidence for an MIC, microbial target, antimicrobial
mode of action, producer, resistance mechanism, or causal graph edge.

The pinned ChEBI source row has no PubMed citations, and the generated record
has no evidence-bearing objects. Bounded direct PubMed eSearch for the exact
Standard InChIKey `IXUSDMGLUJZNFO-BXUZGUMPSA-N` and the exact ChEBI label
`(7R)-7-(4-carboxybutanamido)cephalosporanic acid` returned zero indexed
candidates.

Bounded PubMed searches for exact `Glutaryl-7-aminocephalosporanic acid`,
`Glutaryl-7-ACA`, and `Gl-7-ACA` returned 68 candidates; the exact CAS query
for `27920-90-7` returned 21 candidates; and the repository PubMed helper found
20 title/abstract candidates in a query that combined those synonyms with
antimicrobial, antibacterial, antibiotic, and MIC terms. Semantic Scholar
returned HTTP 429 for the same helper query and was not used.

Those PubMed hits are useful bibliography leads for compound handling, not
claim-level antimicrobial support for exact `CHEBI:41425`. Inspected official
abstracts centered on glutaryl-7-aminocephalosporanic acid as a substrate or
intermediate in enzymatic production of 7-aminocephalosporanic acid: D-amino
acid oxidase oxidation of cephalosporin C to GL-7-ACA, GL-7-ACA acylase or
cephalosporin acylase cleavage of GL-7-ACA to 7-ACA, structural and
site-directed mutagenesis studies of those acylases, and engineered one-pot
bioconversions from cephalosporin C to 7-ACA. The first 20 PubMed-helper
candidates included `PMID:33177298`, `PMID:30501746`, `PMID:23994688`,
`PMID:23373797`, `PMID:23417342`, `PMID:21968249`, `PMID:20572278`,
`PMID:19909828`, `PMID:18390671`, `PMID:17349708`, and `PMID:16809100`; none
of their abstracts reported a measured MIC, susceptible organism, molecular
target, resistance genotype, or biosynthetic producer for purified exact
`CHEBI:41425`.

No NCBI Taxonomy verification was needed for this pass because the review did
not add source-organism or susceptible-organism rows. The PubMed hits named
enzyme sources and recombinant expression hosts such as `Pseudomonas`,
`Bacillus subtilis`, `Escherichia coli`, `Trigonopsis variabilis`, and
`Xanthomonas campestris`, but those abstracts concern biocatalysis and enzyme
engineering rather than biosynthesis of `CHEBI:41425` as a natural product or
susceptibility of those taxa to the exact compound.

## Completeness

The record is incomplete as a reviewed antimicrobial GL-7-ACA record. It has
exact ChEBI identity, structure, a strictly broader ChEBI parent, four xrefs,
and source-level broad antimicrobial classification from the pinned inventory,
but no primary-paper antimicrobial evidence, no `activity_spectrum`, no
molecular target, no mode of action, no producer, no dataset, and no causal
graph.

The empty mechanism and target fields are correct for the current seed.
`CHEBI:33281` does not specify a mode of action, and the inspected publication
leads establish GL-7-ACA as a cephalosporin-production substrate or
intermediate rather than as a tested antimicrobial molecule with a direct
target.

The empty `activity_spectrum` and producer slots are preferable to over-scoped
filler. The candidate abstracts name enzymes that make, bind, or hydrolyze
GL-7-ACA; they do not report an antimicrobial phenotype for exact
`CHEBI:41425`, and they do not show de novo biosynthesis by a producing taxon.

The empty `resistance_mechanisms`, `clinical_status_assertions`, `datasets`,
and `discussions` slots are also acceptable. No measured resistance edge,
clinical assertion, public dataset accession, or discussion-worthy conflict
with exact `CHEBI:41425` claim-level evidence was identified in the bounded
checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:41425` has only generic ChEBI antimicrobial-agent classification and no curator-owned exact-compound assay, producer, mechanism, target, or causal-graph claim. | The generated record has no source PubMed leads, zero record evidence items, zero `activity_spectrum` rows, zero targets, no producer, and no `mode_of_action`. Bounded exact-name and exact-CAS publication searches identify GL-7-ACA enzyme-substrate and cephalosporin-manufacturing leads, but not claim-level antimicrobial support for purified exact `CHEBI:41425`. | Future curator-owned fields on `data/antibiotics/unspecified/7r-7-4-carboxybutanamido-cephalosporanic-acid.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI's generic role is only a cephalosporin-class inheritance artifact with no exact molecule support, the ChEBI inventory extractor or a `curation/decisions.tsv` exclusion row owns that source-level correction. |

No blocker identity, structure, schema, xref, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Trace why the pinned ChEBI source row assigns `CHEBI:33281` to exact
   `CHEBI:41425`, and inspect the next ChEBI refresh diff for the same role.
   If the role has exact-compound antimicrobial assay provenance, curate that
   primary paper through the record's `activity_spectrum`; if it is only
   inherited from the `CHEBI:23066` cephalosporin class without an exact assay,
   consider a scoped source exclusion in `curation/decisions.tsv`.
2. Inspect the exact `Glutaryl-7-aminocephalosporanic acid`,
   `Glutaryl-7-ACA`, `Gl-7-ACA`, and `27920-90-7` PubMed candidates only for
   exact antimicrobial assays. Require purified exact `CHEBI:41425`, a
   susceptible organism or strain, assay method, measured value, and unit
   before adding an `ActivityObservation`.
3. Do not curate GL-7-ACA acylase, cephalosporin acylase, or D-amino acid
   oxidase as antimicrobial molecular targets for this record. The inspected
   abstracts use those enzymes as production catalysts, not microbial targets
   inhibited by `CHEBI:41425`.
4. Add a producer only from primary literature or MIBiG evidence that a named
   taxon biosynthesizes exact `CHEBI:41425`. Recombinant `E. coli` expression
   hosts or isolated acylase source organisms are insufficient.
5. Add resistance mechanisms only from primary papers that test exact
   `CHEBI:41425` against a stated microbial resistance genotype or route; do
   not infer resistance from cephalosporin-class membership or from
   GL-7-ACA-bioconversion enzyme activity.

## Follow-up Checks

After any exact-term curation, exclusion, or source refresh, rerun:

1. `just validate data/antibiotics/unspecified/7r-7-4-carboxybutanamido-cephalosporanic-acid.yaml`
2. `just validate-strict data/antibiotics/unspecified/7r-7-4-carboxybutanamido-cephalosporanic-acid.yaml --out /tmp/antibioticmech-chebi-41425-validation.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-41425.tsv`
5. `just review-queue --limit 65`
6. `just qc`

Manually compare any future activity, mechanism, target, producer, resistance,
dataset, or causal-graph assertion against exact `CHEBI:41425` identity.
Confirm that every claim-level evidence block attaches to the specific object
it supports, not only to the whole ChEBI term, the broader cephalosporin class,
or production enzymes that act on GL-7-ACA.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.

`runoak` was not available in this shell, so official ChEBI term checks were
performed against the EBI OLS4 HTTPS API.
