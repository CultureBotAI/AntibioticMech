# Corpus-wide resistance gene and allele investigation

Date: 2026-10-07. Latest checkpoint: 2026-10-09 UTC.
Status: **in progress, not a completed corpus review**.
The maintainer requested investigation of every record, UniProtKB and NCBITaxon
grounding where possible, and curation of verified findings. NCBI contact and
new NCBI endpoint requests remain deferred, as does #1040.
The source queue now puts this current direction before its historical
2026-10-04 review. Its `BLOCKED`, `REFERENCE`, `UNVERIFIED` fields and historical
verification date remain unchanged; no source-terms reassessment was performed.

## Scope and baseline

The collection-aware loader inspected all 2,939 records at baseline commit
`d6c98be44bd706a2e31c8ebeea4de225decfc5a9`, including activity and membership
validation. This is a census, not evidence that every compound has been
searched in the literature. Every record remains on the research ledger.

| Existing evidence | Records | Assertions |
| --- | ---: | ---: |
| Resistance mechanisms/associations | 295 | 4,770 |
| HIVDB genotype interpretation rules | 16 | 467 |
| PHI-base organism/protein associations | 23 | 217 |
| No resistance mechanism or genotype rule yet | 2,631 | 0 |

These categories overlap. Absence of an existing field is not evidence that a
resistance determinant is unknown or does not exist. CARD assertions, HIVDB
rules, primary experimental results, and measured phenotypes remain separate.
No compound, isolate, allele, or resistance category is inferred by name alone.
The CARD slice contains 4,538 assertions across 273 records and 2,002 distinct
ARO identifiers. At baseline, fourteen records carried 15 curator-authored resistance claims.
These remain within the requested scope, not just the 23 PHI-base records.

The latest curated corpus contains **4,800 resistance assertions across 306
records**, including **45 curator-authored claims across 29 records**. There
are still 2,620 records without resistance assertions or genotype rules. These
are coverage counts, not completed primary reviews or independent experiments.

The [combined progress ledger](2026-10-09-bacteriocin-resistance-progress.tsv) now places
all 2,939 records on one current-hash index, with separate name-search, CARD
reference-candidate, PHI-base identifier-review and HIVDB source-rule columns.
Its [provenance and limitations](2026-10-09-bacteriocin-resistance-progress.json) distinguish
this stage summary from primary review. Individual paper dossiers and other
curator/reference mappings remain in this report, not in that index.

The latest [CARD structural-reference audit](2026-10-09-card-structure-links.json)
checks direct ontology cross-references for all 1,024 terms without an explicit
UniProt CARD link. Six PDB paths lead to reciprocal UniProt references across
17 records, with species, entity and allele caveats retained. These are not new
experimental assignments; the original direct-link counts and curation totals
remain unchanged by that structural-reference audit.

The earlier [bacteriocin identity and reference review](2026-10-09-bacteriocin-primary-context.json)
adds ten versioned UniProt reference candidates across five records, without
biological edits. Microcin B17 and J25 have chemical-graph conflicts; the other
records retain explicit congener or primary-evidence holds. These reference
findings do not change coverage totals or complete any whole-record review.

The subsequent [bacteriocin curation](2026-10-09-bacteriocin-curation.json) adds
three qualified claims across epidermin and microcin C. The
[follow-up dossier](2026-10-09-bacteriocin-followup-context.json) documents primary
text review and an explicit ENA secondary-accession crosswalk. No exact
experimental proteins or genomes are assigned. The nisin congener hold and
the two microcin chemical-graph conflicts remain open.

The earlier biological [platensimycin/platencin curation](2026-10-09-platen-curation.json)
adds four qualitative primary-backed claims, retaining the partial platencin
response and author-interpretation limits on the coarse routes. One donor
UniProt reference is resolved by archive accession; seven wrong-strain
name matches are not substituted for experimental proteins.

The earlier [borrelidin curation](2026-10-09-borrelidin-curation.json) adds one
qualified primary-author report of borO-associated resistance, explicitly
retaining its data-not-shown limitation. The proposed mechanism remains UNKNOWN;
donor UniProt and taxonomy references are not experimental allele assignments.
The conflicting J1074 strain-name candidates remain unresolved.

The earlier [oleandomycin curation](2026-10-09-oleandomycin-curation.json)
adds two qualitative biochemical routes for OleI and OleD, preserving all 30
CARD assertions. Original and later UniProt deposits remain separate references;
donor NCBITaxon:1890 is not an experimental resistance-subject assignment.

The latest canthin-6-one curation adds two conditional gene-level associations
from one primary study, retaining negative comparisons and distinct experimental
backgrounds. Species grounding uses NCBITaxon:4932; YAP1/P19880 and FLR1/P38124
remain reference-only protein mappings, not tested-allele assignments.

The latest PHI-base checkpoint has **185 of 217 associations reviewed for
identifier scope**, with **32 associations across 13 papers pending**. This
is not full phenotype validation or whole-record signoff.

The latest PHI-base curation identifies **BPY22.17** as the subject of the
Posteraro study, preserving the source spelling and separating the UniProt
reference from the experiment. Exact experimental protein and modern species
identity remain unresolved; no new allele or phenotype interpretation was added.

An earlier PHI-base curation resolves the **SDH8 reference-locus alias** between the
primary paper and UniProt using explicit CGD mappings and a shared stable CGD
identifier. Experimental identifiers remain unassigned; protein and strain
TaxID stay in reference-only provenance.

A subsequent cordycepin follow-up grounds **two yeast reference proteins** but
holds biological curation: indexed primary Results were available, while direct
PDF access failed and figure/subject verification remains incomplete. That
metadata-only checkpoint changed no biological records or coverage totals.

A subsequent sordarin-family review distinguishes **GM193663**, neutral sordarin,
and the sodium salt used in another study. It grounds seven DPH reference
proteins, retaining three current UniProt gene-name aliases. A subsequent
text-supported curation adds **five primary author-reported GM193663 gene
associations**, DPH1 through DPH5, to **CHEBI:77908**. Species grounding uses
**NCBITaxon:4932**; UniProt proteins and S288c taxonomy remain reference-only.
The earlier blanket hold is superseded only for those qualitative associations.
Allele validation, figure/supplement review, other assays and the sodium-salt
study remain pending. No whole-record review total increased.

The latest papulacandin follow-up adds **three qualitative gene associations
across papulacandins B and D**, grounded to species and reference-only UniProt
entries. Papulacandin A is not substituted for those congeners. Arborcandin C
remains an unresolved primary-study lead because the inspected text has
conflicting subject labels. Exact alleles, experimental protein assignments and
numeric AST remain uncurated; no whole-record review total increased.

The latest reference-only follow-up investigates the **three fungal CARD terms
outside determinant ancestry**. It retains their explicit source resistance
edges, documents two UniProt reference entries, and resolves three primary-paper
species names through UniProt taxonomy. The source spelling `Trychophyton rubrum`
and an `otherNames`-only match remain unresolved under the exact-name gate.
Neither protein becomes an experimental-allele or exact CARD-term assignment;
biological records and coverage totals are unchanged.

A recent metadata-only follow-up supports **rplD protein-product identity**
despite conflicting ARO ancestry and records two distinct UniProt reference
entries with strain TaxIDs. It assigns neither entry to an experimental allele
or existing clinical activity, and changes no biological records or review totals.

A metadata-only follow-up preserves citation-specific reference-strain
context for all **979 CARD-linked candidate proteins across 169 records**.
It adds no experimental assignments or completed primary reviews. A preceding
follow-up records a thesis/reference lead for two pending journal associations,
without promoting either to reviewed. A prior
metadata-only follow-up independently checks **87 clinical-isolate
BioSample links** from a new primary-study supplement and grounds its reference
protein through UniProt. It added no experimental allele assignments or corpus
claims. The subsequent HDF1 and fenpicoxamid subject-context corrections account
for the latest PHI-base count above; none constitutes whole-record phenotype validation.

The latest citation-discovery checkpoint expanded queries for **384 records**.
All **611 distinct previously truncated query traversals are complete**, covering
612 query-record memberships. Five fresh whole-query traversals replace the
remaining conflicted prefixes. The selected index contains **241,143 distinct
citation identities**, not independent studies or verified resistance findings.
All primary-review statuses remain pending. Discovery made no biological changes;
the separate FUR1 curations are documented below.

The latest primary-evidence follow-up reviews **three additional hygromycin B
yeast studies**, retaining **seven UniProt reference-gene mappings**, condition-specific
negative results, and source-qualified experimental subjects. These are sensitivity
comparisons, not new resistance-conferring allele assignments. A cited original
strain table corroborates SKY252 but does not resolve the later SKY242 alias
conflict. No biological record or PHI-base review count changed.

## First grounding pass

All 63 distinct PHI-base protein accessions resolve as current primary UniProtKB
accessions in release `2026_03`. All 217 source organism TaxIDs occur in the
corresponding protein taxonomy lineages. This verifies identifier presence and
broad lineage compatibility, **not assignment to the experimentally tested gene,
allele, isolate, or causal resistance claim**. All 95 nonempty source gene identifiers occur explicitly in
the associated UniProt records; 122 observations have no source gene identifier.

The [PHI-base database paper](https://doi.org/10.1093/nar/gkz904), in its
"Migration to reference sequence UniProt IDs" section, describes moving linked
UniProt identifiers to reference-strain entries. This resource convention is
another reason not to treat a linked protein automatically as the tested allele.
It does not independently justify changing an individual association; those
decisions still require claim-specific primary evidence. This contextual section
was inspected through the publisher web text, not a locally replayable snapshot.

Taxonomy was obtained from UniProt, not from NCBI endpoints. UniProt uses
[NCBI-assigned taxonomic identifiers](https://www.uniprot.org/help/taxonomic_identifier)
and supplements taxonomy with organism names and strain information. Its
[database license](https://www.uniprot.org/help/license) is CC BY 4.0 for
copyrightable content. This bounded research does not adopt a new bulk source.

### Verified correction

PHIG:2858 on carbendazim (`CHEBI:3392`) used a strain-qualified reference name
as the label of species `NCBITaxon:5141`.
[UniProt taxonomy 5141](https://rest.uniprot.org/taxonomy/5141) identifies
**Neurospora crassa** at species rank. The extractor now removes an explicitly
delimited reference-strain suffix from the source's species-name field.
Re-extraction from the original, checksum-verified PHI-base and PHIPO files
changes exactly this one label in the 217-row inventory.

The experimental designation `74-OR31-14a`, source strain TaxID, protein
accession, alteration text, and publication remain unchanged. Their
experimental-strain and allele correspondence is still under review; correcting
the species label does not validate those other fields.
The [publisher's primary-study summary](https://link.springer.com/article/10.1007/BF00351701)
supports a beta-tubulin substitution in the N. crassa F914 background and its
carbendazim phenotype, but does not expose the source export's complete
experimental-strain crosswalk. No numeric MIC or additional allele claim was
curated from the abstract.

### Curator-owned grounding

Pyrisoxazole (`CHEBI:83823`) now separates the existing study groups and grounds
one supported protein/taxon crosswalk. The
[primary Results and tables](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2020.01396/full)
were inspected; the record retains coordinate and isolate-name caveats.
The [UniProt cross-reference snapshot](2026-10-07-pyrisoxazole-protein-crosswalk.json)
preserves the four candidate entries, citation-specific strain annotations,
sequence versions, retrieval timestamps, release, and response digest.
Only `UniProtKB:A0A7G4P320` was assigned to an individual resistance claim;
the other candidates were not promoted automatically. The accession identifies
the deposited protein, not independent validation of causality or a normalized
allele representation. No genome or strain TaxID was inferred.

This curator-owned change used the collection-aware loader, closed-schema
validated writer, and curation-event helper. Source-owned slices and activities
were unchanged. Splitting the existing aggregate adds one assertion, so the
post-curation corpus has 4,771 resistance assertions, not a new independent
experimental result. The corpus-wide investigation remains open.

### Cerulenin primary-evidence curation

Cerulenin (`CHEBI:171741`, InChIKey `GVEZIHKRYBHEFX-NQQPLRFYSA-N`) now
contains two separate, strain-scoped `fabF` claims from the inspected
[2014 primary Results and Tables 2, 4 and 5](https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.12785).
The GS77 `fabF1` and GS76 `fabF3` claims retain the source protein notation and
JH642 background. Expression regulation also contributes in GS77. No assay
from a heterologous host was relabeled as a native-strain measurement.

The [grounding dossier](2026-10-07-cerulenin-grounding.json) records species
`NCBITaxon:1423`, resolved through UniProt Taxonomy. Only GS77 receives
`UniProtKB:O34340`, supported by its explicit GS77 annotation and PDB crosswalk.
This is a canonical reference protein, not a mutant-specific accession.
The source's residue 108 and UniProt's residue 109 remain explicitly distinct;
no coordinate conversion was inferred. GS76 protein grounding remains open.
The reference strain's TaxID was not assigned to either experimental strain,
and no genome accession was inferred.

Reported MICs are retained in the research dossier with original units and
equivalent `mg/L` values. The MIC assay method and clinical breakpoint were not
established, so no `ActivityObservation` or clinical interpretation was added.
Both claims used the validated writer and curation-event helper; replay was
byte-identical and added no history event. The record remains `SEEDED` because
these findings do not constitute whole-record signoff.

After this curation, the corpus has **4,773 resistance assertions across 296
records**, with **2,630** records lacking both resistance assertions and genotype
rules. These current counts supersede the intermediate pyrisoxazole count,
not the historical baseline table.

### Narlaprevir taxon-only curation

The existing narlaprevir (`CHEBI:173104`) clinical association now has
`NCBITaxon:3052230`, **Orthohepacivirus hominis**. The
[UniProt taxonomy response](https://rest.uniprot.org/taxonomy/3052230) identifies
an active species and explicitly lists `Hepatitis C virus` as an alias, matching
the organism in the [published study metadata](https://repub.eur.nl/pub/41170).
The original association, gene-family label, and primary citation are retained.
No new allele, patient-specific accession, strain TaxID, genome, or measurement
was added. Counts remain 4,773 assertions across 296 records.

The [grounding dossier](2026-10-07-narlaprevir-grounding.json) distinguishes the
2012 submitted manuscript in the author's thesis from the final 2013 paper.
The versions differ in one long-term frequency, so no quantitative claim was
updated. The submitted manuscript names H77 reference accession `AF009606`;
UniProt explicitly links it to both `P27958` (genome polyprotein, containing NS3)
and `P0C045` (F protein). A reference accession alone is neither a unique protein
product nor a patient-virus identity. Neither protein was assigned to the
clinical claim. Final-publication Results and exact allele grounding remain
open. The validated write was idempotent on replay, with no extra history event.

### Raltegravir model grounding

The [primary Results and Figure 3](https://www.researchgate.net/publication/47621681_Molecular_mechanisms_of_retroviral_integrase_inhibition_and_the_evolution_of_viral_resistance)
support two separate PFV biochemical-model observations, not direct HIV-1
measurements. The existing aggregate claim is now separated accordingly.
[UniProt P14350](https://www.uniprot.org/uniprotkb/P14350/entry) identifies the
reference Pro-Pol polyprotein via the study's PDB links; it is not a
mutant-specific accession. [Taxon 11963](https://rest.uniprot.org/taxonomy/11963)
is active with rank `no rank`, not a species-level assignment.

The [dossier](2026-10-08-raltegravir-model-grounding.json) preserves the original
claim and source numbering. No MIC, whole-virus phenotype, genome, or clinical
resistance call was added. All 35 raltegravir HIVDB rules are unchanged. The
corpus at that checkpoint had **4,774 resistance assertions across 296 records**, including
**19 curator-authored claims across 15 records**; 2,630 records still lack
resistance assertions and genotype rules. Splitting the aggregate is not a new
independent experiment, and does not finish raltegravir's literature review.

### HCV compound-form reviews

The initial [dasabuvir identity lead](2026-10-08-dasabuvir-identity-lead.json)
retains the pre-warning hashes of three distinct structures. The
[primary paper's Compound section](https://journals.asm.org/doi/pdf/10.1128/aac.04619-14)
names a sodium form. The current resistance claim is on neutral dasabuvir
(`CHEBI:85182`); sodium (`CHEBI:85179`) and hydrate (`CHEBI:85178`) are separate
structures. Hydration and exact claim placement remain unresolved.

Paritaprevir (`CHEBI:85188`) has a similar open question: its
[primary Compound section](https://journals.asm.org/doi/pdf/10.1128/aac.04227-14)
names a hydrate, while the record formula contains no water. Neither paper's
Figure 1 was visually inspected. No form equivalence or stereochemical
correction was inferred from names alone.

Both records now carry a claim-level warning and an open `CURATION_TODO`.
The [review dossier](2026-10-08-hcv-compound-form-reviews.json) pins the original
and updated records. Chemical identities, existing claims and citations are
otherwise unchanged; the prior `REVIEWED` status is retained, not renewed.
No claim was copied to a salt/hydrate record, and no additional organism,
protein or allele grounding was assigned. Both related dasabuvir records
remain byte-identical to the initial snapshot.

### Elbasvir taxon and reference scope

Elbasvir's existing aggregate claim now has `NCBITaxon:3052230`, using the
verified HCV alias in [UniProt taxonomy](https://rest.uniprot.org/taxonomy/3052230).
The [primary Results](https://journals.asm.org/doi/pdf/10.1128/aac.01390-15)
distinguish genotype-specific replicon susceptibility from clinical sequencing.
Neither context identifies one exact allele for the aggregate claim.

The [grounding dossier](2026-10-08-elbasvir-grounding.json) retains explicit
reference crosswalks: `AJ238799` to [Q9WMX2](https://www.uniprot.org/uniprotkb/Q9WMX2/entry)
and `GU814263` to [D6P444](https://www.uniprot.org/uniprotkb/D6P444/entry).
These are Con1 and S52 reference polyproteins, not patient or mutant assignments.
Their active reference taxa fall within the verified species lineage; neither
reference TaxID is assigned to the aggregate claim. The literal
`xref:refseq-NC_004102` query returned zero entries, which is an unresolved
crosswalk, not proof of protein absence. No sequence, coordinate conversion,
new variant, quantitative endpoint or clinical interpretation was added.
The claim count at that checkpoint remained 4,774 across 296 records.

### PR-39 species and gene context

The existing PR-39 claim (`CHEBI:131850`) now grounds the source gene symbol
`sbmA` and species **Salmonella enterica**, `NCBITaxon:28901`. The
[primary Results](https://journals.asm.org/doi/10.1128/aac.00205-08) identify
LT2-derived mutants, not a single experimental allele. The unresolved uptake
route and existing phenotype summary remain unchanged; no new measurement was
added.

The [grounding dossier](2026-10-08-pr39-grounding.json) retains
[UniProtKB:Q8ZRF5](https://www.uniprot.org/uniprotkb/Q8ZRF5/entry), an unreviewed
LT2 reference protein (entry version 106, sequence version 1), and locus
`STM0376`. UniProt links `NP_459371.1` to `NC_003197.2`; the paper's reference
is unversioned `NC_003197`. Version and coordinate equivalence were not inferred.
Neither this reference protein nor LT2 strain TaxID `99287` was assigned to
the aggregate mutant claim. Mutant-specific proteins, strain TaxIDs and genomes
remain unresolved.

### Daclatasvir clinical and reference context

The existing daclatasvir claim (`CHEBI:82977`) now has species
`NCBITaxon:3052230`, **Orthohepacivirus hominis**. The
[primary Results and Discussion](https://journals.asm.org/doi/10.1128/aac.02494-12)
distinguish patient sequencing from phenotyping in H77c and Con1 reference
replicons. The claim note now preserves that distinction and limits the
six-month persistence statement to variant populations rather than every
individual substitution.

The [dossier](2026-10-08-daclatasvir-grounding.json) assigns no patient-specific
protein, strain TaxID, genome or normalized allele. The administered compound
form was not newly established; this taxonomic update does not transfer or
revalidate exact-form placement. No quantitative endpoint was added. Both this
update and PR-39 used the validated writer and replayed without extra events.
Their existing `REVIEWED` statuses are retained, not renewed. Corpus totals
at that checkpoint remained 4,774 resistance assertions across 296 records.

Primary Results for boceprevir (PMID:18201776) and vaniprevir (PMID:23747481)
were not retrieved in this pass. DOI opens failed in the browsing tool, and the
boceprevir publisher article request returned HTTP 403. Their claims were left unchanged;
the available bibliographic or abstract information is not full primary review.

### Open grounding flags

- Nine simple substitution-coordinate checks fail across seven observations
  on voriconazole and azoxystrobin. This is not nine independent resistance
  discoveries. Current reference versions and the source coordinate systems
  need primary-paper review; source allele strings remain unchanged.
- [A0A089QDC9](https://www.uniprot.org/uniprotkb/A0A089QDC9/entry) is a fragment.
  A matching residue in a fragment would not establish full-length numbering.
  [B8NFL5](https://www.uniprot.org/uniprotkb/B8NFL5/entry) is sequence version 3,
  while [B8N2C8](https://www.uniprot.org/uniprotkb/B8N2C8/entry) is version 1.
  Neither version history nor a coordinate discrepancy alone resolves an allele.
- Three observations on difenoconazole, prochloraz, and propiconazole pair
  `Colletotrichum gloeosporioides` with `NCBITaxon:690256`, which UniProt identifies
  as [Colletotrichum fructicola](https://rest.uniprot.org/taxonomy/690256).
  This is a flag in the unchanged source inventory. The primary-source review
  below now withholds those identifiers from experimental-subject fields;
  it does not re-identify the experimental organism.
- 102 observations have no exact experimental-strain alias match in the
  supplied strain TaxID entry; 41 lack a source strain TaxID. These are review
  queues, not 143 proven errors. The remaining 74 have an explicit alias match,
  which still does not prove isolate or genome identity.
- The earlier S. cerevisiae BY4742 example needs a qualification:
  [UniProt taxonomy 559292](https://rest.uniprot.org/taxonomy/559292) explicitly
  lists BY4742 under its S288c entry. The reference-strain name alone therefore
  does not establish an erroneous TaxID. The paper's P647A/P649A discrepancy
  remains unresolved; no MICs were added from that example.

Only 35 observations cite a paper also listed in their UniProt entry. Citation
absence in UniProt does not invalidate the source study. Conversely, citation
presence and reference-residue agreement do not complete the experimental review.

The [azoxystrobin follow-up](2026-10-08-azoxystrobin-cytb-lead.json) pins two
PHIG:9043 rows and the fragment entry above. The
[2003 publisher page](https://link.springer.com/article/10.1007/s00294-002-0356-1)
exposes only an abstract; its PDF was inaccessible through the browsing tool.
One direct publisher HEAD request returned HTTP 303 to Springer's authorization
route; it was not followed and does not establish full-text availability or absence.
The entry cites a different 2015 paper. That warrants reference-scope review,
not an automatic accession replacement or coordinate conversion. The record
remains unchanged, and no full-text request or other outreach was sent.

### Reviewed reference boundaries

The [author-provided article](https://www.researchgate.net/publication/342367490_Mutations_at_sterol_14a-demethylases_CYP51AB_confer_the_DMI_resistance_in_Colletotrichum_gloeosporioides_from_grape)
distinguishes JS67 experimental background from Nara gc5 reference material
(Table 1 and Section 2.5). The [identity-scope dossier](2026-10-08-js67-reference-context.json)
retains `UniProtKB:L2FD62`, `UniProtKB:L2FQR9`, and reference TaxIDs with their
verified database provenance. These are not established subject identifiers.
Literal `JS67` searches returned no taxonomy or protein entries in UniProt
release `2026_03`; different-name suggestions were not followed. This limited
index result does not establish biological absence.

All three PHI-base associations remain, including their original organism,
strain, alteration, phenotype, and citation. The subject `taxon_id`,
`strain_taxon_id`, and `protein_accession` fields are withheld, with the original
IDs retained as reference-only provenance. No replacement ID, genome, variant,
mechanism or measurement was inferred. EC50 is not relabeled as MIC.

The [review input](../curation/phibase_grounding_reviews.json) pins the complete
adopted inventory and the three individual JS67 rows. Seeding applies the review;
the raw inventory is unchanged. Unknown decisions, source drift, duplicate or
missing rows, and attempts to remove biological claim fields fail closed. A
validated canary preceded the other two writes, and replay produced no record
changes or new history. The records remain `SEEDED`. At the JS67 checkpoint the
corpus had 4,773 resistance assertions across 296 records. This identifier-scope review
does not complete the experimental or whole-record review.

### Voriconazole reference-context correction

The [publisher-indexed primary Results and Table 1](https://www.sciencedirect.com/science/article/abs/pii/S0924857908002823)
distinguish X26728 parent background from NRRL 3357 reference material.
The indexed Results and Discussion were inspected; a direct publisher open
returned HTTP 403. This access limitation is retained in the
[new scope dossier](2026-10-08-flavus-reference-context.json).

Five existing PHI-base claims now withhold `protein_accession` and
`strain_taxon_id`. Source associations, gene identifiers, coordinates and species
`NCBITaxon:5059` remain unchanged. The source strain label is explicitly qualified
as parent context, not exact resistant-isolate identity. No new allele, genome,
measurement or biochemical route was assigned.

Cached UniProt release `2026_03` places both reference proteins under strain
`NCBITaxon:332952`: `B8NFL5` entry 92/sequence 3 and `B8N2C8` entry 90/sequence 1.
The species and strain ranks were independently checked against cached taxonomy
responses. A new metadata-only literal `X26728` query returned zero entries;
different-name suggestions were ignored. This is not biological absence.

That source-owned checkpoint pinned eight associations across four records. Adding
the review changed the whole-file checksum carried by three earlier JS67
records; those updates are provenance-only, with biological fields unchanged.
The earlier JS67 dossier remains a labeled historical snapshot. A validated and
inspected canary preceded the remaining writes, and replay made no writes or
history events. All four records remain `SEEDED`; all 217 PHI-base associations
and the raw inventory are preserved. Exact subject grounding remains unresolved.

### Cycloheximide gene-name correction

The [1994 primary paper](https://www.researchgate.net/publication/14891280_Molecular_cloning_and_expression_of_the_Saccharomyces_cerevisiae_STS1_gene_product_A_yeast_ABC_transporter_conferring_mycotoxin_resistance)
identifies its historical `STS1` as allelic with `PDR5`.
[UniProt P33302](https://www.uniprot.org/uniprotkb/P33302/entry) supports the
`PDR5` / `YOR153W` reference crosswalk and explicitly cites that paper.
[P38637](https://www.uniprot.org/uniprotkb/P38637/entry) instead represents
the modern `STS1` / `YIR011C` proteasome-tether gene. This is a wrong-gene
assignment, not merely an unresolved reference strain.

PHIG:1805 on cycloheximide (`CHEBI:27641`) now rejects the imported protein and
locus identifiers as misassigned. They remain in explicitly labeled provenance.
The S288c strain TaxID is withheld as reference-only; species `NCBITaxon:4932`,
source strain label, alteration, phenotype and `UNKNOWN` mechanism are retained.
`P33302` is not assigned as the exact experimental protein. Its citation-specific
AB320 sequence context remains separate from its canonical S288c entry.
No allele, genome, coordinate conversion or quantitative measurement was added.

The [dossier](2026-10-08-cycloheximide-sts1-grounding.json) pins the source row,
four cached UniProt responses and five before/after records. Only cycloheximide
has an identifier correction; the four earlier reviewed records receive review-file
checksum updates only. Earlier dossiers retain their historical pins and link
forward. That checkpoint covered nine associations across five records;
all 217 PHI-base associations remain. The validated canary and replay succeeded.

### Voriconazole tested subjects and clinical MIC

The inspected [2012 primary Results and Tables 2-3](https://journals.asm.org/doi/10.1128/aac.05477-11)
distinguish clinical isolate BMU29791 from the tested derivatives. The three
imported associations now carry their source-supported subject labels:
PHIG:336 / AF-B, PHIG:337 / AflavC-788, and PHIG:338 / AF-A. The review is
pinned to complete rows and PMID:22314539, not to reused PHIG identifiers alone.
NRRL 3357 remains background provenance, not the tested subject's identity.

The [new dossier](2026-10-08-voriconazole-subject-grounding.json) verifies the
three reference-locus crosswalks against cached UniProt release `2026_03`:
`B8NFL5`, `B8NUK6`, and `B8N2C8`. The reference proteins and parent TaxID are
withheld from exact-subject identifier slots but retained explicitly in notes.
The existing source gene IDs remain reference-locus identifiers. `B8NUK6`
also contains the exact primary-paper feature citation; `B8NFL5` sequence
version 3 changed in 2026 and is not asserted equivalent to the historical
experimental sequence. No coordinates, whole genotypes or genome IDs were inferred.

One independent clinical observation now records BMU29791's MIC of **8 mg/L**
(source: 8 ug/mL), CLSI M38-A2 assay, and historically qualified source resistance
call. It is curator-owned and is not a second numeric Etest observation. The
derivative claims are not assigned to the clinical isolate. Species grounding is
`NCBITaxon:5059`, checked through cached UniProt Taxonomy without NCBI requests.

That checkpoint covered **12 associations across five records**, retaining
all 217 PHI-base associations and all 61 voriconazole claims. The other four
reviewed records change only review-file checksums. The canary was inspected,
replay made no writes or history events, and all 48 identifier-review tests passed.
The previous cycloheximide dossier is now a labeled historical snapshot whose
pins match the new before-images. Whole-record review remains incomplete.

### Echinocandin FKS1 reference context

The [2006 primary Results and Table 3](https://journals.asm.org/doi/10.1128/aac.01653-05)
support the three-drug scope of 24 imported associations across caspofungin,
micafungin and anidulafungin. The strain labels describe parent backgrounds,
not uniquely resolved resistant derivatives. Zygosity and grouped measurements
must not be collapsed into individual-isolate observations.

The paper's declared `AF027295` reference cross-references explicitly to
[UniProtKB:O13383](https://www.uniprot.org/uniprotkb/O13383/entry), sequence version
1, entry 50, via `AAC49870.1`. Its CAI4 sequence-source context differs from the
imported genome-reference `A0A1D8PCT0` and the tested derivatives. The
[pinned dossier](2026-10-08-echinocandin-reference-context.json) records this
positive reference grounding without assigning an experimental protein accession.

The review withholds reference-only protein and strain IDs in 24 associations;
species `NCBITaxon:5476`, parent labels, source alterations and phenotypes remain.
No MIC or unit correction was inferred. All 217 PHI-base associations remain;
**36 then had identifier-scope decisions across eight records**, leaving 181
without such a decision at that checkpoint. Five previous records received checksum-only refreshes.
The validated canary, independent before/after verification, four cached UniProt
responses and idempotent replay passed. All 32 offline checkpoint stages passed.
The earlier voriconazole dossier retains historical pins checked against the new
before-images. These are scoped corrections, not completed whole-record reviews.

### ERG11 deposited-protein lead

The [Flowers primary paper](https://journals.asm.org/doi/10.1128/aac.03470-14)
separates clinical isolates from tested laboratory derivatives. Its imported
scope is drug-specific: 18 fluconazole, two voriconazole and one itraconazole
association. Clinical resistance without an ERG11 amino-acid alteration and
additional resistance mechanisms are reported; genotype presence alone is not
the phenotype or its complete explanation.

The [non-curating lead](2026-10-08-flowers-erg11-lead.json) verifies all 19
paper-declared deposited accessions against 18 cached UniProt entries. One
entry covers two deposits, and other entries have additional publication
contexts. This is not a one-accession/one-experimental-isolate relationship.
The accession-source strain labels still need an explicit join to the paper's
numbered clinical isolates and tested derivatives. No phenotype, MIC or allele
is transferred through this unresolved join. No new network request was needed
for these crosswalks, and no biological record change was made for this paper
at that checkpoint. Its original record pins are now historical; the following
review addresses reference scope without resolving the clinical joins.

### ERG11 and yeast FKS1 subject context

The [paired review](2026-10-08-azole-yeast-subject-grounding.json) scopes another
24 imported associations: 21 ERG11 associations across three azoles and three
yeast FKS1 associations across the echinocandins. All source alterations,
phenotypes, species, gene IDs and existing activity observations are retained.
Reference protein and strain identifiers are preserved in notes instead of
being presented as exact experimental-subject identifiers.

For the [ERG11 paper](https://journals.asm.org/doi/10.1128/aac.03470-14), Table 1
lists two independent laboratory replicates per genotype. The imported rows do
not distinguish these replicates. SC5314 remains explicitly the susceptible
parent, not a uniquely resolved derivative or clinical donor. UniProtKB:P10613
(entry 179, sequence version 2) explicitly cross-references the retained
`C5_00660C_A-T` reference locus. The deposited clinical proteins remain separate
leads, with no allele or MIC transferred through an unresolved isolate join.

For the [yeast FKS1 paper](https://journals.asm.org/doi/10.1128/aac.00262-08),
the subject label is the exact Table 1 label `BY4742-P649A`; Results and the
imported alteration instead use `P647A`. The discrepancy is explicit, not
normalized. Figure 1's declared `AAC48981` reference crosswalks through
`U12893 / AAC48981.1` to UniProtKB:P38631 (entry 209, sequence version 2).
Its retained `YLR342W_mRNA` gene ID is reference-locus grounding, not evidence
for the exact derivative sequence. Whole-cell MIC geometric means and enzyme
inhibition arithmetic means remain distinct; no new measurements are curated.

The species TaxIDs `5476` and `4932` and reference-strain TaxIDs `237561` and
`559292` are checked against existing UniProt Taxonomy responses, without NCBI
requests. At that checkpoint, all 217 PHI-base associations remained: **60 had identifier-scope
decisions across ten records**, and 157 had no such decision. The 36 previously
reviewed claims receive checksum-only refreshes. Both curation canaries,
independent verification and idempotent replay passed; all 33 offline checkpoint
stages passed. Whole-record reviews remain pending.

### Clinical MICs and deposited-source grounding

The [clinical review](2026-10-08-eddouzi-clinical-grounding.json) scopes six
imported associations from the
[2013 primary study](https://journals.asm.org/doi/10.1128/aac.00555-13).
Reference loci, clinical donors and tested derivatives remain distinct.
The imported subject label `1909` remains unresolved, not reassigned to a donor.
Sixty older claims receive only the updated review-file checksum.

Four clinical observations retain Table 3's RPMI 1640 condition and EUCAST
method; original ug/mL values are numerically equivalent in mg/L:

| Compound | Clinical isolate | Species TaxID | MIC, mg/L | Interpretation |
| --- | --- | --- | --- | --- |
| Fluconazole | JEY355 | 5476 | 8 | Source R |
| Fluconazole | JEY162 | 5482 | >128 | Source R |
| Voriconazole | JEY355 | 5476 | <0.0078 | No categorical call inferred |
| Voriconazole | JEY162 | 5482 | >16 | Source R |

These are four drug/isolate observations, not four isolates. R calls retain
historical source interpretation, not a new breakpoint assessment. Existing
voriconazole clinical evidence is unchanged. No laboratory or additional-medium
MIC, plate-assay conversion, genome or strain TaxID is added.

Two clinical ERG3 associations link the same-isolate findings to
[UniProtKB:N0A5G3](https://www.uniprot.org/uniprotkb/N0A5G3/entry), entry 42,
sequence version 1. Its `KC676662 / AGK44786.1` cross-reference has
protein-specific JEY162 evidence. The incomplete bibliography lacks a PMID;
the link instead uses the paper-declared deposit and source-strain evidence.
Neither an entry-wide strain label nor sequence-coordinate equivalence is
assumed. Combined-genotype effects are not attributed independently to ERG3.

The [earlier deposit lead](2026-10-08-eddouzi-deposit-lead.json) retains four
crosswalks from seven declared deposits; unmatched deposits are not biological
absence claims. It and the paired azole/yeast review retain historical record
pins checked against this batch's frozen before-images. This checkpoint retained
all 217 PHI-base associations, with 66 identifier-scope decisions across 11
records and 151 not reviewed at that scope. Its record pins now remain historical
before the following reference-scope correction.

### ERG3 reference-context correction

The [2017 ERG3 study](https://journals.asm.org/doi/10.1128/aac.00651-17),
PMID:28630186, supports the new
[six-association scope review](2026-10-08-rybak-reference-grounding.json) across
fluconazole, itraconazole and voriconazole. Primary Results and strain rows
distinguish clinical isolates, reference backgrounds and laboratory subjects.
The imported deletion claims are not reassigned to the native clinical variant.

UniProt release `2026_03` grounds `Q59VG6` (entry 109, sequence 1) and
`G8B7T4` (entry 50, sequence 1) as reference ERG3 loci in SC5314 and CDC 317.
The source protein and strain TaxIDs now remain explicitly reference-only in
provenance. Species identifiers, source background labels, the existing gene
identifier, alterations and phenotypes are unchanged. No individual derivative
or genome is inferred. Sixty-six older claims receive only the shared review
checksum refresh; all existing clinical observations and curator claims remain.

The declared clinical deposit `KT277771` returned no explicit UniProt EMBL
cross-reference. This is an unresolved mapping, not biological absence.
`PRJNA361149` remains source-reported study-level WGS provenance, not an
individual genome or sample join. Exact-DOI Europe PMC metadata was verified
through EMBL-EBI; no NCBI endpoint was contacted. Publisher-indexed primary text
was available, but direct full text and the public author PDF could not be
retrieved. Numeric Table 1 column alignment remains unresolved, so no MIC or
clinical category was added.

This checkpoint retained all 217 associations, with 72 scoped associations across
11 records and 145 not reviewed at that scope. Its record pins now remain
historical before the following carboxin correction.

### Carboxin reference-context correction

Carboxin (`CHEBI:3405`, `GYSSRZJIHXQEHQ-UHFFFAOYSA-N`) contains 26 imported
associations from PMID:21933337 and PMID:22536383. The
[Fraaije study's Results and Tables 3-4](https://bsppjournals.onlinelibrary.wiley.com/doi/10.1111/j.1364-3703.2011.00746.x)
separate parent backgrounds from tested derivatives and report grouped EC50
ranges. The [Scalliet Results](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0035429)
distinguish whole-cell and mitochondrial inhibition, with IC50-derived resistance
factors. Neither endpoint is an MIC; grouped ranges must not be assigned to
individual isolates.

The [26-association review](2026-10-08-carboxin-reference-grounding.json) now
retains the source protein identifiers in reference-only provenance, not as
tested-allele identifiers. `O42772` (SDH2/SdhB) has unresolved reference-strain
scope. `F9X9V6` (SDH4/SdhD), `F9XH52` (SDH3/SdhC) and TaxID `336722` identify
IPO323 reference context, not IRE30 or experimental derivatives. Species TaxID
`1047171`, background labels, alterations, phenotypes and all 36 carboxin
associations are preserved. No experimental subject, sequence or genome is
inferred. These are identifier-scope corrections, not full mechanism reviews.

Cached UniProt release `2026_03` independently grounds 18 declared deposits
through 11 protein entries and six field backgrounds. Every link has exact
protein-specific strain evidence under the matching primary citation. These
metadata-only crosswalks remain research evidence, not resistant-derivative
identities or new phenotype claims. Unrelated deposits in the same entries are
excluded. Current `ActivityObservation` fields cannot faithfully represent
native EC50/IC50 ranges; no values were coerced into MIC fields.

That checkpoint reached 98 scoped associations and is retained as historical.
Its 72 older claims received only the shared review-checksum refresh.

### Carboxin follow-up reference scope

The [two-association follow-up](2026-10-08-carboxin-followup-grounding.json)
adds primary-verified identifier corrections for
[Kilaru 2015](https://www.sciencedirect.com/science/article/pii/S1087184515000614)
and [Guo 2016](https://link.springer.com/article/10.1186/s13568-016-0232-x).
Their Results distinguish parent backgrounds from tested laboratory derivatives.
The source `IPO323` and `Guy11` labels, species TaxIDs, alterations, categorical
phenotypes and assay wording remain unchanged; no exact derivative is inferred.

Kilaru's versioned reference `XP_003850753.1` and protein ID `74146` crosswalk to
[UniProtKB:F9XG45](https://www.uniprot.org/uniprotkb/F9XG45/entry), entry 75,
sequence version 1, locus `MYCGRDRAFT_74146`, in IPO323. This is reference-only
research grounding, not a replacement experimental accession. The inherited
`O42772` reference has unresolved strain scope and is withheld from the claim's
experimental-protein field.

[UniProtKB:G4NE45](https://www.uniprot.org/uniprotkb/G4NE45/entry), entry 73,
sequence version 1, locus `MGG_00167`, and TaxID `242507` identify reference
strain 70-15, not Guy11 or its derivatives. They now remain only in provenance.
Guo reports `XP_003718958` without a version; UniProt links `XP_003718958.1`.
The [2019 correction](https://link.springer.com/article/10.1186/s13568-019-0814-5)
replaces a Figure 4b image and is recorded alongside the original study.

At that checkpoint, eight other carboxin associations remained unchanged.
Primary access or subject joins were incomplete for Piotrowska, Shima, Wang,
Skinner and Broomfield. Later identifier reviews below address Wang and Piotrowska.
Citation metadata, partial publisher views and donor-deposit labels do not
resolve an experimental protein or justify a strain alias. In particular,
Europe PMC inclusion does not itself establish open-access reuse permission.
The dossier retains eight citation responses, three primary-text response pins,
three reference proteins and four taxonomy records, without exporting methods
or sequences. No growth endpoint or selection condition was converted to MIC.

That historical checkpoint retained all 217 associations, with **100 scoped
associations across 12 records** and **117 not reviewed at that scope**.
Carboxin then had 28 scoped associations out of 36. This follow-up changed two
identifier interpretations and refreshed only the shared checksum on 98 older
claims. Existing clinical activities and curator claims are unchanged.
Whole-record and corpus-wide primary reviews remain pending. No NCBI endpoint
was contacted.

### Iprodione and fludioxonil subject scope

The [new dossier](2026-10-08-iprodione-fludioxonil-grounding.json) records
11 primary-verified identifier-scope corrections, without new resistance
phenotypes, allele calls or activity measurements.

- **Iprodione (`CHEBI:28909`)**: [Fillinger 2012 Results and Table 3](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0042520)
  distinguish eight imported comparisons from both the B05.10 parent and
  the original isolates in Table 1. `UniProtKB:A0A384J5Y1` / `BCIN_01g06260`
  and TaxID `332648` now remain reference-only provenance. The B05.10 parent
  label and species `NCBITaxon:40559` remain; exact tested clones and proteins
  are unresolved. Original deposits `JX192607-JX192631` crosswalk to 21
  UniProt entries, but cannot be transferred onto the later subjects.
- **Fludioxonil (`CHEBI:81763`)**: [Xia 2025 Results and Figure 5](https://link.springer.com/article/10.1007/s44297-025-00052-5)
  resolve three reported experimental subject labels. The species
  `NCBITaxon:117187` is retained, including the source name
  *Fusarium verticillioides* and UniProt's *Gibberella moniliformis* synonym
  context. `W7LTW3`, `W7LX41` and `W7M468` ground reference loci
  `FVEG_01970`, `FVEG_00869` and `FVEG_04168`, respectively. Those accessions
  and TaxID `334819` identify M3125 / FGSC 7600, not the tested derivatives.
  The inspected full text does not establish that reference strain as the
  experimental parent. Individual clones, parent lineage and genomes remain
  unresolved despite the supported subject labels.

The dossier preserves one-to-many protein cross-references and deposit-specific
strain evidence without selecting an experimental isoform. Twenty of the 21
original-isolate entries carry a Fragment flag; absence of the flag on the
remaining entry is not independent completeness proof. A versioned EMBL-xref
query returned no hit for the paper's unversioned historical `BAB69486`
reference. This narrow query is not proof of absence or equivalence to the
current reference protein.

All 28 existing associations in these two records remain. Seventeen await
completed primary-results review across Ren, Mehrabi, Ma and the two other
Fusarium studies; citation metadata and partial publisher views are not
sufficient subject joins. Access restrictions were not bypassed. EC50,
categorical growth and growth-inhibition rates remain distinct from MIC;
source assay flags and `UNKNOWN` mechanism classifications are unchanged.

At that checkpoint the PHI-base slice had **111 identifier-scoped associations across
14 records**, with **106 of 217 pending at this scope**. The 100 previously
reviewed associations received only the shared review-checksum refresh.
Existing curator claims and clinical activities remain unchanged. Whole-record
and corpus-wide primary reviews remain pending. No NCBI requests, source
adoption, outreach or GitHub mutations were made.

### A. fumigatus reference-context review

The [follow-up dossier](2026-10-08-fumigatus-reference-grounding.json) records
**17 additional identifier-scope corrections** across itraconazole (10),
posaconazole (5), and voriconazole (2). Five pinned primary reviews distinguish
parent backgrounds and tested subjects from Af293 reference identity:

| Study | Associations | Identity distinction |
| --- | ---: | --- |
| [Mann 2003](https://journals.asm.org/doi/10.1128/aac.47.2.577-581.2003) | 6 | Original parent, later recipient, and clinical isolates are separate contexts. |
| [Nascimento 2003](https://journals.asm.org/doi/10.1128/aac.47.5.1719-1726.2003) | 3 | Parent background does not identify an individual tested derivative. |
| [Mellado 2004](https://journals.asm.org/doi/10.1128/aac.48.7.2747-2750.2004) | 3 | Clinical donor identity is not later recipient identity. |
| [Mellado 2007](https://journals.asm.org/doi/10.1128/aac.01092-06) | 2 | Separate subject groups must not be collapsed into the parent. |
| [Camps 2012](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0050034) | 3 | Native clinical isolates, reference genomes, and later experimental groups are distinct. |

UniProt release `2026_03` grounds `Q4WNT5` (entry 146, sequence version 1)
and `Q4WDM9` (entry 125, sequence version 1) to the Af293 reference strain.
Their explicit reference loci are `AFUA_4G06890` and `AFUA_6G05300`;
the former also explicitly cross-references the retained source transcript
`Afu4g06890-T`. These reference links do not resolve the exact experimental
proteins. The source species TaxID `746128` remains; reference strain TaxID
`330879` and both protein accessions are retained only in labeled provenance.
Taxonomy was checked through cached UniProt responses, not NCBI requests.

The Camps paper reports sequencing project `ERP001097` for its clinical study.
The dossier retains that study-level accession separately: it is not assigned
to a later experimental subject, individual isolate, sample, or assembly.
No new MIC, breakpoint, subject label, allele sequence, or genome was curated.

Four publisher Results were inspected through the web tool and were not cached;
the offline verifier checks their citation identities and UniProt metadata,
not those publisher texts. The Camps primary text is separately cached and
checksum-pinned. Europe PMC's `isOpenAccess=N` flag was not treated as proof
that a publisher's Results were unreadable. Nine cohort associations remain
pending: four from Natesan 2012 lack a completed primary review; five from
[Wei 2016](https://journals.asm.org/doi/10.1128/aac.02101-16) require careful
separation of baseline susceptibility, later colony frequency, plate growth,
and broth endpoints. These partial reviews did not authorize source changes.

That checkpoint held **128 identifier-scoped associations across
15 records**, with **89 of 217 pending across 42 papers**. The 111 older
associations received only the shared review-checksum refresh. Curator claims,
existing clinical observations, source wording and mechanism classifications
are unchanged. This is identifier review, not complete phenotype validation or
whole-record review. The broader all-record investigation remains incomplete.

### Yeast subject-group review and fungal identity leads

The [next dossier](2026-10-08-li-yeast-reference-grounding.json) curates one
carbendazim identity correction and retains 21 unresolved associations from
the seven-paper, 22-association cohort. In the
[Li 1996 primary Results](https://febs.onlinelibrary.wiley.com/doi/pdf/10.1016/0014-5793(96)00334-1),
`WL167Y` denotes two tested isolates, while `W303-1A` is their parent background.
The group label is now retained with an explicit non-unique-clone caveat.
The paper's endpoint is IC50, not MIC; no measurement was added.

UniProtKB:P02557 (entry 224, sequence version 2) and strain TaxID `559292`
identify the S288c reference, not the tested group. They remain reference-only
provenance, absent from subject identifier fields. Species TaxID `4932` is
retained; `YFL037W_mRNA` remains explicitly a reference-locus identifier, not
an experimental allele accession. The protein and both taxonomy records are
pinned to UniProt release `2026_03`; no NCBI endpoint was contacted.

All 19 carbendazim claims are preserved: 12 PHI-base associations and seven
CARD assertions. Only one receives a new identity-scope decision. The 128
earlier decisions receive only their shared review-file checksum refresh;
16 records are affected in total. Source alterations, phenotype labels,
assays, mechanism classifications, clinical observations and curator claims
remain unchanged. That checkpoint contained **129 identifier-scoped
associations**, with **88 of 217 pending across 41 papers**.

| Pending study at that checkpoint | Associations | Evidence limit |
| --- | ---: | --- |
| Jung 1992, PMID:1423663 | 6 | Citation and abstract reviewed; primary Results unavailable. |
| Qiu 2010, PMID:21077124 | 5 | Primary Results and paralog crosswalk unresolved. |
| Duan 2018, PMID:30497711 | 5 | Publisher Results snippets, not a full primary review. |
| Xu 2019, PMID:30732567 | 2 | Cached primary context inspected; reference-locus crosswalk unresolved. |
| Chen 2009, PMID:19900007 | 2 | Citation-linked deposits do not resolve the experimental subject; Results unavailable. |
| Fujimura 1992, PMID:1388107 | 1 | Subscription preview only. |

Possible fungal paralog conflicts remain leads, not corrected assignments.
Two narrowly scoped UniProt locus queries returned zero hits; a reference-strain
tubulin metadata query returned seven entries. Neither gene symbols nor those
no-hit results establish exact allele identity or gene absence. No replacement
protein, gene, strain TaxID, or genome was inferred for the unresolved studies.

Seven EMBL-EBI citation responses and the Xu primary XML are checksum-pinned.
The Li publisher PDF text was inspected through the web tool, but a direct
download returned HTTP 403. No local PDF or successful image rendering is
claimed; its primary-text review remains manual, not offline replayable.
No protocols, sequences, primers, constructs or enhancement designs are
exported. Identifier review does not complete the broader all-record primary
investigation.

### Fungal identity follow-up and remaining-paper inventory

The [follow-up dossier](2026-10-08-fungal-identity-followup-grounding.json)
records **12 additional identifier-scope corrections** from six studies across
itraconazole, voriconazole, terbinafine and fluconazole. Reference proteins and
strain TaxIDs remain in provenance but are withheld from tested-subject fields.
Parent-background labels, species TaxIDs and source-reported biological fields
are preserved. Existing gene IDs are reference-locus context, not verified
experimental allele accessions. No new allele, genome or activity was added.

The primary identity reviews cover
[Wei 2016](https://journals.asm.org/doi/10.1128/aac.02101-16),
[Ferreira 2004](https://journals.asm.org/doi/10.1128/aac.48.11.4405-4413.2004),
[Diaz-Guerra 2003](https://journals.asm.org/doi/10.1128/aac.47.3.1120-1124.2003),
the [2006](https://journals.asm.org/doi/10.1128/aac.00187-06) and
[2004](https://journals.asm.org/doi/10.1128/aac.48.7.2490-2496.2004)
terbinafine studies, and the
[2024 Candida study](https://doi.org/10.2147/IDR.S483623).
These reviews distinguish parents, reference strains and experimental groups;
they do not validate every imported phenotype interpretation. In particular,
later colony frequency is not baseline susceptibility, and plate growth is not
broth MIC or a clinical resistance category. No endpoint was converted.

The dossier pins six reference proteins and five taxonomy records through
UniProt release `2026_03`. Five ASM primary-text reviews remain manual and
uncached. The Candida primary XML was retrieved from EMBL-EBI and checksum-pinned.
Offline metadata replay does not substitute for those manual primary reviews.
The 129 earlier reviewed claims received only their shared review-file checksum
refresh. In total, 17 records changed; that checkpoint had **141 of 217
associations identifier-scoped**, leaving **76 across 35 papers pending**.

Citation metadata is now pinned for all 41 papers pending at the preceding
checkpoint. Their access flags were 21 non-OA without PMC, 11 non-OA with PMC,
and nine OA with PMC. After this curation, the 35 remaining papers comprise
21, six and eight in those groups, respectively. These are source metadata,
not redistribution decisions or claims that every publisher text is inaccessible.

A second cached primary text, the
[2024 SDH8 study](https://doi.org/10.1080/21505594.2024.2405000), was unresolved
at that historical checkpoint. Its reported locus `orf19.1588` had not been explicitly crosswalked to the
`orf19.9161` annotation on UniProtKB:A0A1D8PGP5. A targeted UniProt query returned
that one entry but did not establish the alias relationship or an experimental
allele. Quantitative susceptibility wording also requires primary-table
reconciliation. No replacement identifier or measurement was curated.
The later direct CGD accession-page request returned HTTP 301 to `/`, not a
locus summary. Its response is retained in local cache
`sdh8-cgd-summary.json`; the redirect was not followed. This access outcome
does not resolve the locus relationship or establish that an alias is absent.

No protocols, sequences, primers, constructs or enhancement designs were
exported. No NCBI endpoint, deferred reuse-terms work, source adoption or GitHub
mutation was used. The broader all-record primary investigation is incomplete.

### Further primary-paper subject and compound context

The [next dossier](2026-10-08-fungal-primary-context-grounding.json) curates
**nine identifier-scope corrections from four papers**, while two other paper
reviews remain incomplete. The affected associations are on carboxin,
caspofungin, fluconazole, voriconazole, pyrifenox and triflumizole. No source
alteration, phenotype, assay, mechanism classification or parent label changes;
no new subject identifier, allele, genome or measurement is inferred.

| Primary study | Associations | Identity-review result |
| --- | ---: | --- |
| [Hamamoto 2000](https://journals.asm.org/doi/10.1128/aem.66.8.3421-3426.2000) | 4 | PD5 is parental context; one protein entry links two source-isolate deposits and does not resolve a unique experimental allele. |
| [Park 2005](https://journals.asm.org/doi/10.1128/aac.49.8.3264-3273.2005) | 2 | Parent or recipient backgrounds are distinct from tested derivatives; SC5314 reference identifiers are withheld. |
| [Sionov 2012](https://journals.asm.org/doi/10.1128/aac.05502-11) | 2 | H99, the clinical isolate and later derivatives are distinct; the imported accession's deposit cross-reference does not resolve the paper's tested allele. |
| [Wang 2015](https://bsppjournals.onlinelibrary.wiley.com/doi/10.1111/mpp.12222) | 1 | JK19 parental context is distinct from tested derivatives and the ATCC 18683 / 1980 / Ss-1 reference. |

Park Table 4 explicitly concerns **L-733560, not caspofungin**. The existing
T1FOA-associated source interpretation therefore needs further compound-context
review; it was not validated or turned into a caspofungin measurement. That
warning is retained in the source-owned claim note. EC50, MIC and biochemical
endpoints likewise remain separate. Identifier review is not phenotype signoff.

The [Kakeya 2000](https://journals.asm.org/doi/10.1128/aac.44.11.2985-2990.2000)
and [Nakayama 2001](https://journals.asm.org/doi/10.1128/aac.45.11.3037-3045.2001)
reviews retain indexed primary snippets and reference metadata, but full Results
could not be retrieved reliably through the web tool. Their two existing claims
are unchanged. No whole-paper review or exact subject crosswalk is claimed.

All four completed primary identity reviews remain manual and uncached.
Six reference proteins, including two for the uncurated leads, and eight
taxonomy records are pinned through cached UniProt release `2026_03` responses.
An entry lacking a gene-name field is not evidence that the gene is absent.
The dossier verifies all 35 preceding pending-paper citation responses and
retains a 31-paper queue: 21 non-OA without PMC, two non-OA with PMC, and eight
OA with PMC. Access flags are metadata, not source-adoption or reuse decisions.

The 141 earlier reviewed claims receive only the shared review checksum refresh;
19 records changed in total. At that checkpoint, **150 of 217 associations were
identifier-scoped, with 67 across 31 papers pending.** No NCBI request, outreach, source adoption,
GitHub mutation, protocol or sequence export was used. The all-record primary
investigation remains incomplete.

### Six open-access parent/reference reviews

The [next identity-scope dossier](2026-10-08-fungal-oa-context-grounding.json)
records six more source-pinned corrections, affecting hydrogen peroxide,
carbendazim and azoxystrobin. Primary XML was retrieved through EMBL-EBI
Europe PMC, checked against each article's PMID and DOI, and retained with
response checksums. No NCBI endpoint was used.

| Primary paper | Identity finding | Endpoint limitation |
| --- | --- | --- |
| [PMID:26596626](https://doi.org/10.1038/srep16881) | NJ11 parent and tested derivatives are distinct; P53373 is reference context. | Azoxystrobin resistance occurs in the parent and other phenotype groups; co-occurrence does not establish an allele-specific effect. EC50 is not MIC. |
| [PMID:30044782](https://doi.org/10.1371/journal.pgen.1007546) | I1S9X9, the retained gene ID and TaxID 229533 describe PH-1 reference context, not a uniquely identified derivative. | Growth comparisons are not MICs. UniProt ALT_SEQ does not identify the experimental alteration. |
| [PMID:40934067](https://doi.org/10.1080/21505594.2025.2555419) | W7MZ22 and TaxID 334819 identify M3125 reference context, not an exact derivative. | Table 1 reports EC50, not MIC. |
| [PMID:41277790](https://doi.org/10.1111/mpp.70174) | I1RPK0 and TaxID 229533 identify PH-1 reference context, not the separately tested derivatives. | Figure 5 growth-inhibition comparisons are not clinical resistance categories or MICs. |
| [PMID:41745253](https://doi.org/10.3390/jof12020111) | P1 is the parent; A0A8E5ME34 has species-level taxonomy and does not resolve an exact experimental allele. | Table 1 reports IC50, not MIC. |
| [PMID:42112916](https://doi.org/10.1128/spectrum.02761-25) | Source V592 is retained; the paper names Vd592. G2XFG4 and TaxID 498257 instead describe the VdLs.17 reference. | Growth-inhibition and zone observations are not converted into MIC. |

The correction withholds six structured protein assignments and four
strain-TaxID assignments while retaining them in reference-only provenance.
Species IDs, source strain labels, the one source gene ID, source alterations,
phenotypes, assays, claim order and existing activities are unchanged. No new
experimental allele, genome, sample, TaxID or measurement is assigned.
The identity review does not independently certify the source biological claims.

The prior 150 reviewed claims receive only the shared review checksum refresh.
Twenty-one records change; the other 2,918 record files remain byte-identical.
The prior primary-context dossier is now explicitly historical and retains its
original evidence and record pins. Five unresolved lead claims from three
papers remain unchanged, including both OA locus-crosswalk leads.

At that checkpoint, identifier-review coverage was **156/217 associations**, leaving **61
across 25 papers**: 21 with Europe PMC `NON_OA_NO_PMC` metadata, two
`NON_OA_WITH_PMC`, and two `OA_WITH_PMC`. These access categories do not establish
reuse permission or publisher availability. No new source adoption, NCBI
contact, GitHub mutation, protocol, sequence or enhancement-design export occurred.
This is another bounded identity review, not completion of the corpus-wide goal.

### Ren parent/descendant identity review

The [new subject dossier](2026-10-08-ren-subject-context-grounding.json) corrects
eight fludioxonil/iprodione associations using the
[Ren primary paper](https://apsjournals.apsnet.org/doi/10.1094/PDIS-11-15-1290-RE).
Its publisher-indexed Results and Tables 2, 3 and 5 distinguish the parental
comparators from the tested descendants. The four source labels are corrected
to the documented subjects, with parents retained in provenance. EC50 is not
converted into MIC, and fludioxonil-specific categories are not generalized.

UniProt `A0A384J5Y1` (entry 36, sequence version 1, release `2026_03`) and
TaxID `332648` describe **B05.10 reference context**, not these subjects.
They remain in provenance instead of exact-subject fields. Species TaxID
`40559` is preserved. Source alterations, phenotype and assay fields, including
`Not assayed` annotations, are unchanged. No experimental protein, gene,
allele sequence, genome, sample, TaxID or measurement is assigned; association
is not promoted to causation.

**Primary-access limitation:** the direct publisher fetch failed. The table
review used indexed publisher content and is manual, not locally cached or
independently replayed by the offline checks. Checksums verify the citation,
UniProt records, source rows and exact record diff, not that manual reading.
The indexed Sg-28 row disagrees across Tables 2 and 3; an original-table check
is required before measurement curation. This may be an indexing/extraction
error, not an established error in the article. No values are imported.

The prior 156 reviewed claims receive only a shared review-checksum refresh.
There are 21 changed records and 2,918 byte-identical records. Prior decisions,
source biology and activities are preserved. The preceding OA dossier remains
a historical snapshot, and five unresolved lead claims are unchanged.

Other leads did not meet the curation threshold: PMID:1388107 remains a
subscription preview; PMID:1423663 was inaccessible; the inspected
PMID:34490974 page did not expose Results/subject context. Restricted database
index searches for the two remaining OA locus crosswalks did not supply
authoritative mappings. These are bounded access/search outcomes, not evidence
of protein or alias absence, and no corresponding claim was changed.

At that checkpoint, coverage was **164/217 identifier-scoped associations**, with **53
across 24 papers pending**. Europe PMC metadata describes 20 as
`NON_OA_NO_PMC`, two as `NON_OA_WITH_PMC`, and two as `OA_WITH_PMC`;
these categories do not establish publisher availability or reuse permission.
No NCBI request, outreach, source adoption or GitHub mutation was made.
The all-record primary investigation remains incomplete.

### Darlington subject/reference correction

The [Darlington dossier](2026-10-08-darlington-subject-grounding.json) uses the
[primary Results and Figure 3 caption](https://journals.asm.org/doi/full/10.1128/aac.44.11.2985-2990.2000)
to correct fluconazole's PHIG:1132 subject from recipient background `CAI4` to
`transformant 12`. Donor and heterologous-host comparisons remain separate.
Reviewed UniProt `P10613` (entry 179, sequence 2, release `2026_03`) and TaxID
`237561` identify SC5314 reference context, now retained only in provenance.
Species `NCBITaxon:5476` and the source reference-gene ID remain unchanged.
No exact experimental allele, protein, genome or strain TaxID is assigned.

The source alteration, `[Not assayed]` qualifier, phenotype and assay remain
unchanged; no MIC or activity was added. The review does not certify those
source biological fields. Primary text was read through the web tool; the
direct publisher request returned HTTP 403. Its cached failure and the
bibliographic/UniProt responses are auditable, but do not independently replay
the manual primary reading. At that checkpoint PMID:11600353 remained pending
identifier review and its claim was unchanged. A follow-up search exposed its
[publisher-indexed Table 1](https://journals.asm.org/doi/10.1128/aac.45.11.3037-3045.2001),
which distinguishes the ATCC 2001 parent from several derivatives through ACG4.
The full-page request timed out; partial indexed context was not promoted to
an exact experimental-subject or phenotype assignment.

A validated fluconazole canary preceded the other writes. One association has
new identifier-scope decisions; 164 earlier associations have checksum-only
provenance updates. Across the corpus, 21 record files changed and 2,918 are
byte-identical. All 217 PHI-base claims, previous decisions, source inventory,
other-source claims and activities are preserved. The independent diff audit
verified those boundaries against the frozen pre-curation records.

Coverage at that checkpoint was **165/217 identifier-scoped associations**, with **52 across
23 papers pending**. This is not whole-record signoff or completion of the
corpus-wide investigation. NCBI, #1040 and reuse-terms work remain deferred;
no source adoption or GitHub mutation occurred.

### Nakayama Reference/Subject Follow-Up

The [new dossier](2026-10-08-nakayama-reference-grounding.json) resolves the
identifier scope of PHIG:3694 on fluconazole (`CHEBI:46081`). The
[publisher-indexed primary Results and Figure 5 caption](https://journals.asm.org/doi/10.1128/aac.45.11.3037-3045.2001)
distinguish ATCC 2001 background/comparator context from tested derivatives.
The source row does not identify a unique derivative. Its background label,
gene, alteration, phenotype and assay remain unchanged; no individual derivative
or experimental accession is assigned.

UniProt release `2026_03` grounds reference `P50859` to **ERG11**, synonym
**CYP51**, locus **CAGL0E04334g**, with the exact source transcript cross-reference
**CAGL0E04334g-T** (entry 162, sequence version 1). Its strain taxonomy
**284593** has species parent **5478**. These are reference-context identifiers,
not identifiers for the experimental derivatives; the protein and strain IDs
now remain explicitly in provenance rather than structured subject slots.
The species ID and source gene ID are retained. Taxonomy was read from cached
UniProt responses, not NCBI.

The indexed Table 4 condition labels conflict with surrounding prose and its
footnote. That discrepancy requires checking the original layout; it was not
silently repaired or converted into measurements. **IC50 is not MIC.** No new
activity observation or clinical category was added. EBI full-text retrieval
returned HTTP 500, and direct publisher HTML/PDF access was unavailable. The
manual indexed-primary reading is identified as such, not claimed to be an
offline-replayable full-text review.

A validated canary and independent preservation audit establish one new
identifier-scope correction, 165 checksum-only claim updates, 21 changed record
files and 2,918 byte-identical files. All 217 PHI-base claims, earlier review
decisions and existing activities are preserved. Coverage is now **166/217**,
with **51 associations across 22 papers pending identifier review**. This
remains narrower than phenotype validation or corpus-wide primary review.

The largest remaining paper group is the six **thiabendazole** associations
(`CHEBI:45979`, InChIKey `WJCNZQLZVWNLKY-UHFFFAOYSA-N`) from PMID:1423663.
The paper title refers to benomyl, but the pinned source rows and complete
compound record identify thiabendazole; the earlier report wording conflated
these scopes. The [publisher abstract](https://onlinelibrary.wiley.com/doi/abs/10.1002/cm.970220304)
reports 18 mutant alleles, not a six-subject crosswalk. Direct full-text access
was unavailable. Cached UniProt `P10653` identifies reference **benA** / **AN1182**
in FGSC A4 (TaxID **227321**, entry 157, sequence version 1), not those individual
experimental subjects. The six source associations remain pending; complete
primary subject/allele context is needed before interpreting them as distinct
isolates or assigning exact reference identifiers. No new variant details were
exported from that abstract.

### Duan: Parent and Reference Context

The [Duan dossier](2026-10-08-duan-reference-grounding.json) corrects identifier
scope for five PHIG:7751 associations on difenoconazole (`CHEBI:81760`) and
prochloraz (`CHEBI:8434`). The
[publisher-indexed primary sections](https://www.sciencedirect.com/science/article/abs/pii/S0048357518303225)
distinguish BM6, BM50 and 2021 parental backgrounds from their descendants.
Those source labels remain, explicitly qualified as backgrounds rather than
exact resistant-subject identities. Complete Results and the individual
subject crosswalk were unavailable; no derivative designation is invented.

[UniProt I1RJR2](https://www.uniprot.org/uniprotkb/I1RJR2/entry), reviewed entry
82 / sequence version 1 in release `2026_03`, identifies PH-1 CYP51A with
reference locus `FGRAMPH1_01T14465`. UniProt Taxonomy verifies strain **229533**
under species **5518**. The protein and strain TaxID are retained in provenance,
not assigned as experimental identifiers. The source gene locus remains with
an explicit reference-context qualification; species grounding is preserved.

This correction preserves source alterations, phenotypes, assays, earlier
reviews and all other-source claims. It does not certify compound-form scope,
new causal effects or individual alleles. No measurements were added. Direct
publisher retrieval returned HTTP 403; the manual indexed-section reading is
not represented as a cached full-text review. The separate PMID:21077124 and
PMID:38374637 leads remain pending; the inspected publisher/Supporting
Information access routes did not establish complete subject crosswalks.

An independent audit verifies five scoped corrections and 166 checksum-only
updates, 21 changed record files and 2,918 byte-identical files. Coverage at that checkpoint was
**171/217 identifier-scoped associations**, with **46 across 21 papers pending**.
Corpus-wide primary review remains incomplete.

### Piotrowska: Parent Reference Scope

The [Piotrowska dossier](2026-10-08-piotrowska-reference-grounding.json) scopes
three existing carboxin associations (`CHEBI:3405`, PHIG:3434/3435).
The [accepted manuscript](https://www.pure.ed.ac.uk/ws/portalfiles/portal/29148098/Characterisation_of_Ramularia_collo_cygni_laboratory_mutants_resistant_to_Succinate_Dehydrogenase_Inhibitors.pdf)
identifies DK05 as the parent and distinguishes the tested descendants. Its
carboxin comparisons use EC50-based resistance factors, not MICs.
This resolves the earlier access-limited parent-label question without assigning
any descendant a reference genome or allele accession.

UniProt release `2026_03` entries
[A0A1S6KZ79](https://www.uniprot.org/uniprotkb/A0A1S6KZ79/entry) and
[A0A1S6KZ87](https://www.uniprot.org/uniprotkb/A0A1S6KZ87/entry)
ground SdhB/SdhC parent references, with entry versions 35/22 and sequence
versions 1. Their strain comments name `DK 05 Rcc 001 ss2`.
Species TaxID **112498** remains; parent proteins are preserved only in
provenance, not as experimental allele identifiers. Source biology is unchanged.

The working university archive response is cached and checksum-pinned.
Publisher full text/supplement and the other university download route returned
HTTP 403. No sequence, new variant, protocol or activity measurement was added.
This is identifier-scope curation, not full phenotype or compound-form signoff.

### Pending Compound Identity and Access Audit

The [pending identity audit](2026-10-08-pending-phi-identity-audit.json) binds
all **43 then-pending associations across 20 papers and 10 records** to source-row
digests and exact record labels/InChIKeys. Labels come from collection-aware
record reads, not publication titles. This is a metadata audit, not new
identifier-scope curation; the reviewed count at that checkpoint was **174/217**.

For the six Jung associations, the exact compound is **thiabendazole**, not
benomyl. [UniProt P10653](https://www.uniprot.org/uniprotkb/P10653/entry)
verifies reference `benA` / `AN1182` and the source identifier's versioned EMBL
cross-reference `CBF87981.1`. TaxID **227321** is the FGSC A4 reference strain,
under species **162425**. These facts do not establish a G191 experimental
allele or make six source associations into six distinct tested isolates.
Additional title/DOI and author/institutional searches did not yield accessible
primary Results in this pass. The complete subject crosswalk remains pending.

The two Fouche associations belong to **fenpicoxamid** (`CHEBI:136340`,
InChIKey `QGTOTYJSCYHYFK-RBODFLQRSA-N`).
[UniProt Q6X9S4](https://www.uniprot.org/uniprotkb/Q6X9S4/entry) identifies
reference `cob` / `cytB`, entry 84 / sequence version 1, species **1047171**,
with the sequence-submission strain comment `ST1/MBC`. This does not verify
the source labels `IPO323` or `37-16` as accession-specific experimental subjects.
The [institutional manuscript link](https://hal.inrae.fr/hal-03357067v1/file/accepted.pdf)
returned access-denied HTML; the
[publisher full-text route](https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1462-2920.15760)
redirected to its abstract. Neither is represented as an inspected full text.

Both focused groups remain unresolved. No biological record, source review,
measurement, experimental accession or curation event changed in this pass.
All reference metadata came from checksum-verified existing UniProt caches;
no new NCBI requests, outreach or terms reassessment occurred.

### Xu: Tested Subjects and Species Correction

The [Xu dossier](2026-10-08-xu-subject-species-grounding.json) scopes two existing
carbendazim associations (`CHEBI:3392`, InChIKey
`TWFZGCMQGLPBSX-UHFFFAOYSA-N`). The
[primary paper](https://link.springer.com/article/10.1186/s12864-019-5479-6)
distinguishes tested **SJ51M** and **HC30M** from parents SJ51 and HC30 in
Results, Figure 2 and Table 1. Its abstract identifies HC30M as
**F. proliferatum**, not the source export's F. fujikuroi. These subject labels
are corrected; original parent and organism labels remain in provenance.
The reported measurements are EC50, not MIC; no measurements were added.

[UniProt Taxonomy 948311](https://www.uniprot.org/taxonomy/948311) is a species
entry named **Gibberella intermedia**, with **Fusarium proliferatum** as a
synonym. This grounds the paper-reported name, not an independent taxonomic
reidentification. SJ51M retains species TaxID **117187**.

[W7M0I3](https://www.uniprot.org/uniprotkb/W7M0I3/entry) identifies the M3125 /
FGSC 7600 reference, TaxID **334819**, locus `FVEG_05512`, entry 62 / sequence
version 1. Its protein and strain TaxID are retained only in provenance.
[P53374](https://www.uniprot.org/uniprotkb/P53374/entry), entry 110 / sequence
version 1, identifies F. fujikuroi TUB2, TaxID **5127**, with strain comment
`A 102`; it is explicitly rejected for HC30M rather than transferred across
species. Neither tested subject receives a protein accession, strain TaxID
or genome identifier.

A bounded reference-locus name query returned
[A0A1L7VSA4](https://www.uniprot.org/uniprotkb/A0A1L7VSA4/entry) for
`FPRO_07779` in reference strain ET1, TaxID **1227346**, entry 21 / sequence
version 1. Its predicted protein name conflicts with the paper's terminology.
It remains a reference-locus lead, not HC30M identity or functional validation.
The query did not return `FVER_09254`; that is not evidence of gene absence.

The guarded review loader now supports paired species replacement only when
the source TaxID is explicitly rejected and every conflicting source identifier
is withheld. All 19 carbendazim claims, source allele wording, phenotypes,
assays and other-source assertions are preserved. The two corrections plus
174 shared-checksum updates affect 21 files; **2,918 records are byte-identical**.
No sequence, new variant, protocol or activity was added. At this checkpoint,
identifier review reached **176/217**, with **41 associations across 19 papers pending**; exact
experimental proteins and corpus-wide primary review remain incomplete.

### Shima: Parent-Reference Context

The [Shima dossier](2026-10-08-shima-parent-reference-grounding.json) scopes two
existing carboxin associations (`CHEBI:3405`, InChIKey
`GYSSRZJIHXQEHQ-UHFFFAOYSA-N`). The authors' final published
[2011 primary follow-up](https://www.jstage.jst.go.jp/article/bbb/75/1/75_100687/_pdf/-char/en)
distinguishes wild-type **RIB40** from earlier-study subjects on p. 181 and
in Table 1 on p. 182; reference 15 on p. 184 identifies the original 2009 paper.
Those three pages were visually inspected from a checksum-pinned local PDF.
Earlier donor deposits do not identify later transformants. RIB40 remains the
parent-background label, not a unique tested-subject identifier.

UniProt release `2026_03` identifies [Q2TWM0](https://www.uniprot.org/uniprotkb/Q2TWM0/entry)
(entry 127, locus `AO090010000505`) and
[Q2U3V9](https://www.uniprot.org/uniprotkb/Q2U3V9/entry)
(entry 98, locus `AO090020000596`) as RIB40 reference proteins, both sequence
version 1. Their reference strain TaxID **510516** is under *A. oryzae* species
**5062**, verified using cached UniProt Taxonomy responses. The protein
accessions and strain TaxID are retained in provenance only; species 5062 and
the source phenotype, assay and alteration wording remain unchanged.

The **2009 full text remains unavailable**. This is a follow-up-supported
identity correction, not complete validation of its experimental claims.
Whole-cell growth and biochemical activity are distinct endpoints, and neither
was converted to MIC. No new variant, sequence, construct, protocol, numeric
measurement, experimental accession or genome was added. All 36 carboxin claims
are retained. The two corrections and 176 checksum-only updates affect 21
record files; 2,918 records remain byte-identical. At this checkpoint, identifier review reached
**178/217**, with **39 associations across 18 papers pending**.

### Mehrabi: Parent and Reference-Locus Context

The [Mehrabi dossier](2026-10-08-mehrabi-parent-reference-grounding.json) scopes
one existing association each on iprodione (`CHEBI:28909`, InChIKey
`ONUFESLQCSAYKA-UHFFFAOYSA-N`) and fludioxonil (`CHEBI:81763`, InChIKey
`MUJOIMFVNIBMKC-UHFFFAOYSA-N`). The
[published primary paper](https://doi.org/10.1094/mpmi-19-1262), accessible as
an [author-uploaded copy](https://www.researchgate.net/profile/Gert-Kema/publication/6723668_MgHog1_Regulates_Dimorphism_and_Pathogenicity_in_the_Fungal_Wheat_Pathogen_Mycosphaerella_graminicola/links/5724f92a08aee491cb3a9d74/MgHog1-Regulates-Dimorphism-and-Pathogenicity-in-the-Fungal-Wheat-Pathogen-Mycosphaerella-graminicola.pdf),
separates three grouped derivatives from wild-type and ectopic controls in
Table 2 (p. 1266). Page 1267 identifies **IPO323** as the parent background.
Neither source row is assigned to an individual clone.

[UniProt Q1KTF2](https://www.uniprot.org/uniprotkb/Q1KTF2/entry), reviewed entry
108 / sequence version 2 in release `2026_03`, identifies IPO323 reference
**Hog1 / MYCGRDRAFT_76502**. Its source-paper citation, strain comment and
`DQ432031 / ABD92790.2` cross-reference connect the paper's reference deposit,
not an experimental derivative accession. The source `Mycgr3T76502` identifier
is retained as an explicitly qualified reference locus. Reference strain TaxID
**336722** is under species **1047171**, verified through cached UniProt
Taxonomy; the protein and strain TaxID are confined to provenance.

Primary PDF text was inspected through the web tool. Direct download returned
**HTTP 403**; no local PDF, visually inspected pages or offline primary-text
replay is claimed. The source **Not assayed** flag is preserved and remains
unresolved against the grouped primary comparison. No numeric measurement,
new variant, sequence, construct, protocol, experimental accession or genome
was added. All 15 iprodione and 13 fludioxonil claims are retained. Identifier
review at this checkpoint reached **180/217**, with **37 associations across 17 papers pending**;
this is not whole-record phenotype validation.

### Huang: Parent Context and Unresolved Locus Alias

The [Huang dossier](2026-10-08-huang-parent-reference-grounding.json) scopes
one existing fluconazole association (`CHEBI:46081`, InChIKey
`RFHAOTPXVQNOHP-UHFFFAOYSA-N`). The
[2024 primary study](https://doi.org/10.1080/21505594.2024.2405000) distinguishes
the wild-type **SC5314** parent from the laboratory derivative in Table 1;
Table 2 and Results distinguish their tested observations. Clinical subjects
remain separate. The review used the previously cached primary XML from
EMBL-EBI Europe PMC, not an NCBI endpoint.

[UniProt A0A1D8PGP5](https://www.uniprot.org/uniprotkb/A0A1D8PGP5/entry) is an
unreviewed SC5314 reference entry, version 35 / sequence version 1 in release
`2026_03`, with gene name **SDH8** and loci **orf19.9161 / CAALFM_C202620WA**.
Its four GO annotations cite this paper, but that does not make it an
experimental allele accession. The paper instead names **orf19.1588**. The
authoritative historical-locus alias was unresolved at this checkpoint; the
subsequent CGD crosswalk below resolves reference nomenclature only. The source's
empty `gene_id` is not filled by a name match. Cached UniProt Taxonomy places strain
**237561** under species **5476**. Protein and strain identifiers now remain
in provenance, while SC5314 is explicitly retained as parent background.

The earlier CGD locus response redirected to its homepage; the current web
tool could not open the locus page, and the homepage and publisher full text
returned HTTP 403. No blocked route was retried. Cached XML supports the
identity review, not visual figure inspection or complete phenotype validation.
Quantitative wording in the Results needs separate reconciliation before any
measurement curation. No new variant, construct, sequence, protocol, numeric
measurement, exact experimental accession or genome was added. All **77
resistance claims, two activities and 118 clinical-status assertions** are
preserved. Identifier review reaches **181/217**, with **36 associations across
16 papers pending** at that historical checkpoint; exact experimental grounding
remains open after the reference-alias follow-up.

### SDH8: Verified Reference-Locus Alias

The [CGD crosswalk dossier](2026-10-09-sdh8-locus-crosswalk.json) resolves the
reference-name discrepancy using the primary database's explicit metadata.
The [Assembly 19-to-22 mapping](https://www.candidagenome.org/download/chromosomal_feature_files/C_albicans_SC5314/ORF19_Assembly22_mapping.tab)
contains separate rows mapping **orf19.1588** and **orf19.9161** to
**C2_02620W_A / SDH8**. The
[versioned feature file](https://www.candidagenome.org/download/chromosomal_feature_files/C_albicans_SC5314/C_albicans_SC5314_version_A22-s08-m01-r37_chromosomal_feature.tab)
lists both aliases on the same feature with primary CGD identifier
**CAL0000192813**. That identifier exactly matches the CGD cross-reference on
[UniProt A0A1D8PGP5](https://www.uniprot.org/uniprotkb/A0A1D8PGP5/entry).
No string-normalization assumption or sequence comparison was used.

The CGD files were retrieved on 2026-10-09 and report modification on
2026-10-04. Feature version **A22-s08-m01-r37** is pinned explicitly; it was
not substituted with the directory's separately listed `current` link.
The old CGI locus route still redirects to the homepage. Public download
metadata was accessible through direct requests despite the web tool's access
failure. Redirects and access failures are not evidence of missing genes.

The source-owned PHI-base review now records the resolved reference alias and
the two CGD source digests. **UniProt remains unreviewed**, and this finding
does not identify the tested derivative or allele. The source's empty `gene_id`
stays empty; protein and strain TaxID remain reference-only provenance, with
SC5314 retained as parent background. Species TaxID **5476**, source alteration,
phenotype, assay and all clinical/activity observations are unchanged.

One note correction and **183 shared-checksum-only claim updates** change
22 records, each through the validated writer with one appended history event.
The other 2,917 records are byte-identical. Coverage remains **184/217
identifier-scoped associations**, with **33 across 14 papers pending**: resolving
this reference alias is not an additional primary resistance review.
The earlier Huang dossier and other historical audits remain unchanged.
Only selected identity metadata is exported; no CGD bulk source was adopted,
and no sequences, coordinates, variants, protocols or measurements were added.
No NCBI request, outreach or GitHub mutation occurred.

### HDF1: Tested Subject Versus Parent Reference

The [HDF1 dossier](2026-10-09-hdf1-subject-reference-grounding.json) scopes
PHIG:8901 on hydrogen peroxide (`CHEBI:16240`, exact existing InChIKey
`MHAJPDPJQMAIIY-UHFFFAOYSA-N`). The
[published paper in the author-affiliated USDA archive](https://www.ars.usda.gov/ARSUserFiles/3041/2011%20Li%20mpmi-10-10-0233.pdf)
identifies **YM1** as the tested subject, distinct from parent **PH-1** and
comparator **YM11**. Results on printed p. 488, Table 1 on p. 489 and Figure 9C
on p. 492 were checked in extracted text and visually rendered pages.
The claim now uses YM1; PH-1 remains original-background provenance.

[UniProt I1RCN2](https://www.uniprot.org/uniprotkb/I1RCN2/entry) is an
unreviewed PH-1 reference entry, not an experimental-subject accession.
Its source accession and `NCBITaxon:229533` are retained only in provenance.
[UniProt Taxonomy 5518](https://rest.uniprot.org/taxonomy/5518) identifies
the species and explicitly lists *Fusarium graminearum* as a synonym;
the [PH-1 strain node](https://rest.uniprot.org/taxonomy/229533) has that
species as parent. No NCBI endpoint was requested.

The paper's historical locus `FGSG_01353` and UniProt's current locus
`FGRAMPH1_01T03337` remain **an unresolved alias crosswalk**. A bounded
UniProt exact gene query returned no results; suggestions were not adopted,
and this is not evidence of gene absence. The previously empty `gene_id`
remains empty. No experimental protein accession, genome, sequence, new
variant, protocol or numerical measurement was added. Source alteration,
phenotype and assay fields are unchanged; the growth comparison was not
converted to MIC or clinical resistance. Identifier-scope review reaches
**182/217**, leaving **35 associations across 15 papers pending**.

A later metadata-only lookup on 2026-10-09 did not resolve this alias.
The Ensembl Genomes REST taxonomy request failed TLS hostname validation;
certificate checks were not disabled and no response was accepted as evidence.
The Rothamsted/Grassroots catalogue `package_show` request for dataset
`a5bd7322-068d-49a8-9d3f-fb2b29890c66` returned HTTP 404. Its response is cached
as `hdf1-rothamsted-catalogue-2026-10-09.json` with body SHA-256
`2ea1eeeaea8817938de86ddf25078110d2dc9468d3e414f166b4ea09f9dc92b6`.
The [reference-annotation paper](https://doi.org/10.1186/s12864-015-1756-1)
describes historical naming changes, but the inspected text does not establish
this specific locus pair. The Fusarium mapping page cited by the
[PHI-base database paper](https://doi.org/10.1093/nar/gkz904),
`https://scabusa.org/FgMutantDb`, also returned HTTP 404. Its response is cached
as `hdf1-scabusa-landing-2026-10-09.json` with body SHA-256
`63197fde41b74429c94982cdd42e0f4fe8fbb574431cdf86f2bfe45a92947dc7`.
Access failures are not evidence of gene absence; no additional identifier or
biological record was changed.

### Fenpicoxamid: Parent Cohorts Versus Reference Protein

The [HAL accepted manuscript](https://hal.inrae.fr/hal-03357067/file/accepted.pdf)
for PMID `34490974`, DOI `10.1111/1462-2920.15760`, distinguishes ancestral
backgrounds `IPO323` and `37-16` from the derived subjects represented by the
two adopted PHI-base associations. The journal DOI and accepted status appear
on PDF p. 2; Results pp. 9-10, Table 4 on p. 36, and Figure 3 on pp. 39/43
support the subject-context correction. These identity pages were visually
inspected. This is an accepted manuscript, not the publisher's Version of Record.

[UniProtKB Q6X9S4](https://www.uniprot.org/uniprotkb/Q6X9S4/entry), entry 84,
sequence version 1 in release `2026_03`, is a reviewed `cob` / `cytB` reference
entry whose sequence citation names **ST1/MBC**. It does not establish an
experimental accession for either cohort. [UniProt Taxonomy 1047171](https://rest.uniprot.org/taxonomy/1047171)
supports the retained species **Zymoseptoria tritici**, not a strain assignment.

Both source background labels and the protein accession now remain in provenance
only. The original two associations, species, source alteration, phenotype and
assay are preserved. Individual row-to-subject mapping remains unresolved,
including a label discrepancy between Table 4 and Figure 3; no representative
derivative is selected. The source assay qualifier is not reinterpreted.
No new variant, sequence, protocol, numeric measurement or genome was added.
The [metadata dossier](2026-10-09-fouche-subject-reference-grounding.json)
retains the source-row and evidence pins. This brings identifier-scope review
to **184/217**; it is not allele validation or whole-record signoff.

### Nguyen: Thesis Reference Lead, Journal Subjects Pending

The [metadata-only lead](2026-10-09-nguyen-reference-lead.json) retains two
pending associations under PMID:22591226. The
[author's 2013 dissertation](https://ediss.sub.uni-hamburg.de/handle/ediss/4850)
names PH1 as wild-type background and `FGSG_09612` as the locus, and cites the
2012 paper. Printed pages 15, 53 and 143 were visually checked for these
identity and bibliographic statements. The dissertation is **not the final
journal article**, and a subject-by-subject crosswalk between them is not
established. The publisher PDF request returned 403; this is an access limit,
not evidence that the paper or crosswalk does not exist.

[UniProt P0C431](https://www.uniprot.org/uniprotkb/P0C431/entry), reviewed entry
110 / sequence version 1 in cached release `2026_03`, explicitly carries
`FGSG_09612` and the source's EnsemblFungi cross-reference `FGRAMPH1_01T26671`.
That cross-reference's `GeneId` property is separately `FGRAMPH1_01G26671`;
the two identifiers were not silently substituted. Species `NCBITaxon:5518`
and reference-strain `NCBITaxon:229533` are grounded through cached UniProt
Taxonomy, not new NCBI requests. This verifies **reference metadata**, not the
experimental protein, allele, isolate or genome.

No corpus claim or curation event changed, and the two journal associations
remain pending. Restricted text and page images stay in ignored local caches;
no sequences, variants, protocols, new measurements or bulk source content
were exported. Identifier-scope review remains **182/217**, with **35
associations across 15 papers pending**.

### DKAG124: Clinical Samples Versus Reference Identifiers

The [metadata dossier](2026-10-09-dkag124-cohort-reference-grounding.json)
reviews the [2026 primary study](https://doi.org/10.1093/jac/dkag124) by
Gomez Londono, Oliveira Souza et al. Its cohort was selected for decreased
susceptibility to at least one triazole, not resistance to every tested drug.
[Supplementary Table S1](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/jac/81/5/10.1093_jac_dkag124/1/dkag124_supplementary_data.docx)
contains 87 unique isolate/BioSample pairs: 35 under `PRJNA985736` and 52 under
`PRJNA1301956`. These are sample/project links, not per-isolate assemblies.
The native embedded worksheet was read structurally, not visually inspected.

The paper's modelling reference resolves to
[UniProt Q4WNT5](https://www.uniprot.org/uniprotkb/Q4WNT5/entry), reviewed entry
146 / sequence version 1 in release `2026_03`, gene **cyp51A / AFUA_4G06890**.
Cached UniProt Taxonomy places reference strain **Af293 / 330879** under
species **Aspergillus fumigatus / 746128**. Neither the protein nor the strain
TaxID is assigned to the clinical isolates. The paper's read-mapping reference
`GCA_000150145.1` and laboratory background `PyrG+` are also kept separate;
their strain crosswalk is not independently resolved.

Voriconazole, isavuconazole, itraconazole and posaconazole remain name-level
leads against four InChIKey-pinned records, not verified tested-form mappings.
The publisher displays **CC BY-NC 4.0**: raw text and table rows remain in
ignored local caches, with no bulk table redistribution, source adoption or
reuse clarification. No new variant, sequence, construct, protocol or numeric
resistance measurement is exported. The three older Natesan subject labels
were not found in this HTML or S1 identifier cells; this does not resolve those
four pending associations or establish biological non-overlap.

### Oligomycin: Reference Grounding and Compound-Scope Limit

The [reference dossier](2026-10-08-oligomycin-reference-grounding.json) verifies
two reviewed UniProt entries from release `2026_03`, without assigning either to
an experimental resistance allele:

| Reference gene / locus | UniProt | Entry / sequence version | Reference taxon |
| --- | --- | --- | --- |
| OLI1 (ATP9) / Q0130 | [P61829](https://www.uniprot.org/uniprotkb/P61829/entry) | 171 / 1 | S288c, 559292 |
| ATP6 (OLI2) / Q0085 | [P00854](https://www.uniprot.org/uniprotkb/P00854/entry) | 196 / 2 | S288c, 559292 |

UniProt Taxonomy places reference strain **559292** under *S. cerevisiae*
species **4932**. [RCSB entry 4F4S](https://www.rcsb.org/structure/4F4S) explicitly
links its subunit-9 entity to P61829; UniProt reciprocally links the structure.
The deposited entity reports species 4932 and zero mutations, not a resistant
S288c experimental subject. Its EFO ligand matches oligomycin A (`CHEBI:28285`)
by InChIKey **MNULEGDCPYONBU-AWJDAWNUSA-N**.

The [2012 primary paper](https://www.pnas.org/doi/10.1073/pnas.1207912109), however,
reports an **oligomycin A/B/C mixture** in its Results, Figure 2 caption and
Methods. Modeling the ligand as A does not establish a pure-A resistance
phenotype. The paper cites older functional genetics; its structural experiment
does not independently validate those resistance claims.

Three cited primary abstracts were inspected: PMID:2932333 and PMID:2867935
provide OLI1/subunit-9 context; PMID:2876917 provides ATP6/OLI2 context.
PMID:159820 remains citation-only. Their exact DOI/PMID identities are verified
in cached EBI responses, but full primary Results, exact congener and
experimental-subject crosswalks remain unresolved. These are gene-component
leads, not verified experimental protein or allele accessions.

The 2012 publisher text was read manually; the failed EBI XML retrieval is not
an offline full-text cache. The 2018 paper (PMID:29650704,
DOI:10.1126/science.aas9699) remains citation-only because primary text was
unavailable. No new interpretation is assigned to it. All four separately
identified oligomycin A/B/C/D records remain unchanged, with no resistance
claim added. No variants, sequences, new measurements or experimental protocols
were exported, and no mixture result was copied to an individual congener.

## CARD reference-link pass

The complete UniProt `database:card` query returned 4,182 metadata-only entries
in nine pages from release `2026_03`. Exact explicit CARD cross-references,
not gene-name similarity, were compared with all 2,002 determinants in the
current corpus. The [determinant audit](2026-10-07-card-reference-grounding.json)
and [4,538-assertion ledger](2026-10-07-card-reference-ledger.tsv) retain both
matched and unmatched assertions across all 273 CARD-bearing records.

| Explicit UniProt link status | Determinants | Corpus assertions |
| --- | ---: | ---: |
| One reference candidate, primary review pending | 976 | 2,545 |
| Multiple reference candidates, all retained | 2 | 4 |
| No explicit link in this release | 1,024 | 1,989 |

There are 980 determinant-to-protein links to 979 distinct proteins: 189
Swiss-Prot reviewed and 790 TrEMBL unreviewed entries. These links cover 169
compound records. All 360 reference TaxIDs resolve as active identifiers
through UniProt Taxonomy. **None of this establishes the experimental allele,
tested isolate, genome, AST result, or causal effect.** A reference taxon is not
the organism of an unreviewed compound-specific resistance experiment, and
missing explicit links are not evidence that a biological mapping is absent.

The two one-to-many determinants are `ARO:3002881` and `ARO:3002709`.
The audit keeps both candidates for each. Across the 980 links, 151 gene symbols
literally equal the CARD short name, 593 differ, and 236 lack a primary gene
symbol. This is a case-sensitive text check, not 593 established annotation
errors or an allele-validation test. Prefixes, capitalization, nomenclature,
and actual annotation disagreements all require review. For an in-scope example,
`UniProtKB:A0ACM8Q8E3` pairs gene annotation `pipB2` with an explicit
`ARO:3002709` cross-reference named `QnrA3`; the audit does not resolve that
disagreement or reject either candidate automatically. The earlier `OXA-374`
example was present in the broader UniProt query but outside the 2,002
CARD-owned determinants being counted, so it did not illustrate the in-scope links.

This is a UniProt research crosswalk, attributed under its
[CC BY 4.0 database license](https://rest.uniprot.org/help/license), not adoption
of another source or import of CARD's restricted `card.json`. The adopted
ontology inventory was not refreshed. No record was changed by this pass.
The retained artifacts pin source, corpus, protein, taxonomy, and response
digests. Independent verification compared every candidate with cached raw
responses and checked all 2,939 current record hashes and all 4,538 ledger rows.

### Citation-Specific Reference Context

The separate [citation-context index](2026-10-09-card-citation-context.json)
retains **1,686 citation contexts** across all **979 candidate proteins**:
1,098 journal-article annotations, 586 database submissions, one book and one
unpublished-observation annotation. These are citation occurrences, not counts
of distinct publications or independently validated experiments. **1,277 strain
annotation occurrences** remain attached to their own 1,159 citation contexts
on 810 proteins. Composite strain labels are preserved without splitting them
into inferred individual isolates or collection-equivalence mappings.

For example, cached [UniProt Q461P1](https://www.uniprot.org/uniprotkb/Q461P1/entry)
attaches KB1 to PMID:16048974, but QC39 and TUM17379 to separate database
submissions. The other retained QnrA3 candidate,
[A0ACM8Q8E3](https://www.uniprot.org/uniprotkb/A0ACM8Q8E3/entry), has a separate
NCTC10738 submission annotation. None of those labels is promoted to the
ciprofloxacin record's experimental subject. Both candidates remain retained;
the gene-name conflict and their biological equivalence require primary review.
The two LmrC candidates likewise remain separate.

The index is reconstructed entirely from the existing nine UniProt protein
responses, retaining per-reference citation IDs, dates and evidence pointers.
No new endpoint request, restricted CARD download, sequence comparison or
experimental allele assignment was made. Non-strain comment values, citation
titles and experimental reference-position text are omitted from this metadata
export. The original candidate audit, assertion ledger, source inventories and
all biological records remain unchanged. Missing or uninspected citation
context is not evidence that a gene, strain or relevant study does not exist.

### LmrC: Primary Context, Allele Assignment Pending

The [LmrC review dossier](2026-10-09-lmrc-primary-context.json) traces
`ARO:3002881` across the lincomycin, clindamycin and celesticetin records.
The inspected evidence is the **published 2021 mBio article** included in a
[Charles University appendix bundle](https://dspace.cuni.cz/bitstream/handle/20.500.11956/197887/140129614.pdf?isAllowed=y&sequence=4),
not an inferred equivalence between thesis prose and a final journal article.
The title/license page, Figure 1 and adjacent Results were visually inspected;
Materials and Methods were inspected as extracted text. The article identifies
itself as DOI:10.1128/mbio.01731-21, PMID:34488446, under CC BY 4.0. That license
is not assumed to cover other material in the bundle.

Figure 1b/c and Results distinguish the native producer, **S. lincolnensis
ATCC 25466**, from the laboratory host, **S. coelicolor M1154**. LmrC is not
a major native self-protection contributor in the tested background; the
laboratory-host resistance result must not be generalized to that background.
The article also distinguishes regulatory function from self-protection.
Figure 1d's celesticetin production comparison does not validate the existing
celesticetin LmrC resistance assertion. These conclusions are qualitative and
limited to the inspected article locations, not an export of experimental
methods or resistance measurements.

Both UniProt candidates remain reference-only: `A9Y8T8` cites the 2008 paper
naming ATCC 25466, whereas `A0A1B1M202` has a distinct 2016 submission annotated
NRRL 2936 and locus `SLINC_0260`. Their cached metadata share UniParc identifier
`UPI000162A5BF`; this is not a tested-subject, genomic-locus or experimental
allele crosswalk. No sequence comparison was performed. Species-name matches
are retained as `NCBITaxon:1915` and `NCBITaxon:1902` through UniProt Taxonomy;
neither is a strain identifier, and the separate A3(2)/M145 reference node
`NCBITaxon:100226` was not assigned to M1154.

**No biological record was changed.** Exact tested material forms and the
experimental-allele crosswalk remain unresolved; supplementary Table S2 was not
inspected. The three original CARD assertions, clindamycin's pre-existing
activity observations and all other record fields remain unchanged. The
candidate audit stays pending because this limited primary-context review
does not finish allele grounding or compound coverage.

### Archive Identity Versus Experimental Identity

The separate [archive-ID index](2026-10-09-card-archive-groups.json) covers all
**979 UniProt reference candidates**, retaining their individual accession,
entry versions and reference TaxID. They map to **977 UniParc identifiers**;
none lacks an archive ID in this pinned response. Only two groups contain
multiple candidate accessions: `UPI000162A5BF` contains the two LmrC candidates,
and `UPI0000551E0C` contains the two QnrA3 candidates. Both pairs remain intact.

[UniProt's archive documentation](https://www.uniprot.org/help/uniparc) defines
archive identity by protein sequence. That database identity does not establish
a shared genomic locus, tested strain, experimental allele or resistance effect.
[UniProt's gene-name guidance](https://www.uniprot.org/help/gene_name) also notes
that distinct genes can encode identical proteins. No sequence was downloaded
or compared in this audit, and no representative accession was selected.
In particular, QnrA3's `qnrA3` versus `pipB2` annotation disagreement and its
separate citation-specific strain contexts remain unresolved. No source-owned
claim, candidate audit or citation-context entry was rewritten by this pass.

### Ontology Term Scope

The [term-scope audit](2026-10-09-card-term-scope.json) classifies all **2,002
existing CARD terms**, covering **4,538 assertions across 273 records**, without
changing their candidate accessions or primary-review statuses. It uses the
[ARO ontology at commit 0225daaf](https://github.com/arpcard/aro/blob/0225daaf01b1336fc6e866989b4835b89afa40d8/aro.owl),
whose embedded date is `12:08:2026 11:14`, under its
[CC BY 4.0 license](https://github.com/arpcard/aro/blob/0225daaf01b1336fc6e866989b4835b89afa40d8/LICENSE).
This is an ontology-only research projection, not a refresh of the source
inventories or import of restricted `card.json`.

The OWL serialization is separately checksum-pinned; it is not claimed to be
byte-identical to the historical OBO download. All **4,555 source-inventory
resistance edges** and their determinant labels were reconciled against its
asserted restrictions. All 2,002 current determinant labels match. Classification
uses only explicit named ARO `rdfs:subClassOf` paths, which are retained as
witnesses. Restriction targets, including antibiotics, are not ancestry edges.
No imported ontology is fetched, and a selected term reaching an external
named parent would fail classification.

The **1,024 terms without explicit UniProt links** divide as follows:

| Ontology Scope | Terms | Grounding Limit |
| --- | ---: | --- |
| rRNA-ancestor term | 88 | Ontology ancestry only: 87 RNA labels and one protein-definition conflict, reviewed below. |
| Gene cluster, cassette or operon | 14 | A whole cluster is not one protein accession. |
| Efflux complex or subunit | 147 | This broad ancestor does not distinguish the complex from its components. |
| Other unresolved entity scope | 775 | A protein or exact allele mapping still requires evidence. |

Across linked and unlinked terms, the first two categories cover 107 and 20
existing assertions respectively. Their absence of protein links is not evidence
that the resistance observation is missing or false. Actual RNA loci and clusters
need appropriate locus/component and organism grounding. Ancestry alone does
not establish entity identity; this audit does not complete primary review.

Among unlinked terms, **43 have named direct subclasses** and **603 have
variant-category ancestry**. These are overlapping flags, not additional terms
in the table. A child protein must not be assigned automatically to its ancestor,
and a canonical reference does not identify a tested variant. No descendant
accession was propagated or representative selected.

Three existing terms, `ARO:3009269`, `ARO:3009270` and `ARO:3009638`, have no
named subclass path to the determinant root in this snapshot. Their source
resistance edges remain present. This discrepancy is retained for ontology
review; it does not establish that resistance is absent and caused no claim
deletion. All prior candidate links, reference taxonomy, source records and
curation history remain unchanged.

A bounded title/DOI and author-copy recheck for PMIDs `22897872`, `24903410`,
`38056173` and `38374637` did not complete their primary subject crosswalks.
The inspected routes yielded bibliographic or abstract material, inaccessible
publisher text, or incomplete supporting context. No outreach or paid access
was attempted, and the **35 pending PHI-base associations remain pending**.

### Named Organism Crosswalk

The [name crosswalk](2026-10-09-card-named-taxa.json) follows up all **88 terms
with the rRNA ancestor**, covering **107 source assertions across 33 records**.
It retains the previous audit unchanged and reproduces its ontology/source
checks before resolving names. The source label is not an experimentally tested
organism: no `ResistanceMechanism.taxon_id`, strain, genome, gene locus, allele
or protein accession was assigned by this pass.

**86 term labels resolve to 33 distinct active species TaxIDs** in UniProt
Taxonomy release `2026_03`. The 34 binomial-name searches retain their full
candidate metadata and raw-response pins. Only exact scientific names or
explicit synonyms at species rank are accepted; matching a lineage, substring,
`otherNames` entry or search rank is insufficient. All searches are complete
within their declared response counts. The Borreliella canary was inspected
before the remaining queries; later replay requires no network.

Six names resolve through explicit synonyms rather than current scientific names:

| CARD Source Name | UniProt Scientific Name | Named Organism TaxID |
| --- | --- | --- |
| Chlamydophila psittaci | Chlamydia psittaci | NCBITaxon:83554 |
| Halobacterium halobium | Halobacterium salinarum | NCBITaxon:2242 |
| Mycoplasma gallisepticum | Mycoplasmoides gallisepticum | NCBITaxon:2096 |
| Mycoplasma genitalium | Mycoplasmoides genitalium | NCBITaxon:2097 |
| Mycoplasma hominis | Metamycoplasma hominis | NCBITaxon:2098 |
| Mycoplasma pneumoniae | Mycoplasmoides pneumoniae | NCBITaxon:2104 |

Both Halobacterium names denote the same species in these responses; this is
why 34 resolved names yield 33 TaxIDs. `ARO:3004057` names no organism and
`ARO:3004161` uses the broad label "Propionibacteria"; both remain unresolved.
The latter was not silently narrowed to Cutibacterium acnes. An organism-name
match also does not identify the genomic compartment of an RNA locus, including
the two Chlamydomonas terms.

**Correction to the biological reading of the ancestry category:** the pinned
ontology definition of `ARO:3004956` (Neisseria gonorrhoeae rpld) describes a
50S L4 ribosomal protein, while its named subclass path reaches the rRNA
determinant anchor. Thus the earlier 88-term category must not be read as
88 independently verified RNA determinants. The crosswalk flags this source
conflict separately from the 87 RNA-named terms; none is primary allele
validation. The source assertion and missing protein link are preserved,
not replaced with a guessed protein accession.

[UniProt documents](https://www.uniprot.org/help/taxonomic_identifier) its use
of NCBI-assigned TaxIDs, including identifiers not necessarily visible in the
NCBI interface. This pass used only UniProt Taxonomy endpoints, not NCBI.
No source was adopted, no restricted CARD model data imported, and no
source-owned biological record or curation history was changed.

### rplD: Protein Identity Versus Resistance Allele

The [identity dossier](2026-10-09-rpld-reference-grounding.json) follows up
`ARO:3004956` on azithromycin (`CHEBI:2955`, InChIKey
`MQTOSJVFKKJCRP-BICOPXKESA-N`). The pinned ontology definition describes L4
protein, despite the named ancestry through `ARO:3000328`. The Introduction
of [Mauffrey et al. (2024)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0306695),
paragraph `article1.body1.sec1.p2`, distinguishes rplD-encoded L4 protein from
rrl-encoded ribosomal RNA. This is **gene-product identity context only**:
tables, supplements, exact alleles and resistance effects were not validated
in this pass. The upstream ontology and historical ancestry audit are unchanged;
their RNA-ancestor category must not be interpreted as a biological assignment.

The metadata-only query `gene_exact:rplD AND organism_id:485 AND reviewed:true`
returned zero entries; the strain-inclusive `taxonomy_id:485` query returned
two. Both responses are complete for their exact queries in release `2026_03`.
The first result is not evidence of gene absence. Both returned entries identify
L4 and explicitly name rplD, but neither supplies a CARD cross-reference in
the selected metadata. These are new reference leads, not replacements for
the frozen CARD-linked candidate totals.

| UniProt Reference | Locus | Reference Strain | Strain TaxID | Entry / Sequence Version |
| --- | --- | --- | --- | --- |
| [B4RQX9](https://www.uniprot.org/uniprotkb/B4RQX9/entry) | NGK_2437 | NCCP11945 | 521006 | 89 / 1 |
| [Q5F5S8](https://www.uniprot.org/uniprotkb/Q5F5S8/entry) | NGO_1837 | ATCC 700825 / FA 1090 | 242231 | 104 / 1 |

UniProt Taxonomy confirms active strain nodes
[521006](https://rest.uniprot.org/taxonomy/521006) and
[242231](https://rest.uniprot.org/taxonomy/242231), both under species 485.
The citation-specific strain annotations agree with those reference contexts.
The genome-paper citation on B4RQX9 and submission citation on Q5F5S8 were
inspected as UniProt metadata, not independently reviewed primary references.
Both entries are reviewed, but their gene/product annotations include HAMAP
rule evidence; reviewed status is not experimental resistance evidence.

Both entries report UniParc `UPI00004CE837`. They remain separate: a shared
archive identifier does not identify an experimental allele, genomic locus or
clinical subject. No sequence was requested or compared. Neither reference is
joined to the existing clinical isolate or another activity by species matching.
The source-owned CARD claim remains intact, with no newly assigned protein,
gene, strain or TaxID. Primary resistance review remains pending, as does the
whole-corpus investigation. No NCBI endpoint, restricted CARD model data,
source adoption, outreach or GitHub mutation was involved.

## HIVDB reference-context pass

All **467 interpretation rules across 16 records** match the adopted,
manifest-pinned inventory: 231 RT, 192 IN, and 44 PR terms. The
[reference-context audit](2026-10-07-hivdb-reference-grounding.json) retains
every source rule ID, exact compound identifier, record checksum, source version,
and score metadata. It is not a fresh extraction of the algorithm XML.

The gene and strain definitions were inspected at the exact adopted
[hivfacts commit](https://github.com/hivdb/hivfacts/tree/be1c11a5145fea9073fdb71801919d4a34265336).
Their cached SHA-256 digests and Git blob IDs agree with the pinned repository
tree. The source defines PR, RT, and IN reference regions but supplies no
UniProt accession in those definitions. Only reference lengths and digests,
not sequences or transformed variants, are exported to the research artifact.
Neither HXB2 equivalence nor a patient allele was inferred.

[UniProt taxonomy 11676](https://rest.uniprot.org/taxonomy/11676) is active and
explicitly recognizes the corpus's organism label, `Human immunodeficiency
virus 1`. Its scientific name is `Human immunodeficiency virus type 1` and its
rank is **no rank**, not species. `HIV1` in the source definition is algorithm
context, not an experimental isolate designation. The existing score-rule
schema has no taxon or reference-accession slot, so this grounding remains in
the report. Rules were not converted into resistance mechanisms or AST results.
Primary evidence and exact allele grounding remain pending.

## Bounded citation discovery

The initial discovery cohort contained all 2,631 records with neither a
resistance assertion nor a genotype rule. A class-balanced, citation-only
Europe PMC search queried canonical labels in titles/abstracts alongside
resistance and genetics terms. Three inspected canaries preceded a bounded
250-query batch. The [initial plan](2026-10-07-resistance-discovery-plan.json),
[initial candidate index](2026-10-07-resistance-discovery-candidates.json), and
[initial ledger](2026-10-07-resistance-discovery-ledger.tsv) preserve that
pre-cerulenin checkpoint:

| Initial query outcome | Records |
| --- | ---: |
| No hits in this limited query | 202 |
| Citation candidates requiring review | 41 |
| More than 100 hits; refinement required | 10 |
| Not searched yet | 2,378 |

These are **253 citation searches, not 253 completed biological reviews or 51
verified resistance findings**. Canonical labels often differ from literature
names; synonyms and historical aliases were outside that initial pass. Phrase matching
does not establish exact chemical identity, and co-occurrence may involve
another drug, non-microbial systems, or an unrelated experiment. Patent,
preprint, and other source IDs retain their namespaces rather than becoming
PMIDs. No-hit results do not establish biological absence. The first 100
provider-ranked citations are retained, with truncation explicitly flagged.

The initial artifacts pin the historical census archived locally as
`corpus-before-cerulenin.json`. Cerulenin subsequently left the no-claim cohort
through the primary-evidence curation above; it was not silently discarded.
After the later FUR1 cohort curation, the current canonical-only plan covers the
remaining 2,629 records. 5-Fluorouracil remains in the all-record investigation;
it was not silently dropped when it gained curator-owned associations.

A second bounded batch completed 500 additional canonical-label queries,
followed by the final 1,878 queries for this canonical-label pass.
The [current plan](2026-10-07-resistance-discovery-current-plan.json),
[current candidate index](2026-10-07-resistance-discovery-current-candidates.json),
and [current ledger](2026-10-07-resistance-discovery-current-ledger.tsv) pin the
post-curation census. **All 2,629 current no-claim records have a cached search
response**, independently checked against the exact query and each retained
citation:

| Current query outcome | Records |
| --- | ---: |
| No hits in this limited query | 1,537 |
| Citation candidates requiring review | 972 |
| More than 100 hits; refinement required | 120 |
| Not searched by canonical label | 0 |

Including cerulenin's earlier search, all 2,631 records in the initial discovery
cohort have reached citation discovery. **This completes the canonical-label
pass, not the biological investigation.** Aliases, historical names, exact
structure matching, and primary experimental review remain open. An empty query
result does not establish that resistance or a gene association is absent.

Aculeacin A is another [unresolved discovery lead](2026-10-07-aculeacin-a-lead.json).
Its canonical query returned eight citations, but the 1991 primary paper's
publisher fetch failed and the EMBL-EBI full-text endpoint returned HTTP 500.
UniProt returned zero citation-linked entries for three exact study PMIDs in
release `2026_03`; suggestions containing different PMIDs were not followed.
Neither inaccessible Results nor empty citation indexing establishes biological
absence. The previously curated aculeacin A record was left unchanged.

## All-record name discovery

A separate [all-record plan](2026-10-08-resistance-alias-discovery-plan.json)
now covers **all 2,939 records**, including those with existing resistance
assertions or interpretation rules. Its 16,030 distinct record-name pairs retain
all 2,939 canonical-label origins, 13,064 synonym origins and 3,224 source-label
origins. Identical text within a record shares one query name without losing its
origins. Names shared between records remain separate: 166 name entries across
137 records carry explicit cross-record ambiguity flags. Case, stereochemical
notation, related synonyms and source provenance are preserved.

An inspected cerulenin alias canary preceded 500 new Europe PMC responses,
followed by two bounded batches of 1,000 and a final batch of 2,334. Earlier
checkpoints covered 3,135, 4,135 and 5,135 query memberships. The
[candidate index](2026-10-08-resistance-alias-discovery-candidates.json) and
[2,939-record ledger](2026-10-08-resistance-alias-discovery-ledger.tsv) now cover
all 7,469 planned query memberships. An identical lexical query may serve
multiple record memberships without merging those records.

| Query outcome | Canonical | Alias groups | Total |
| --- | ---: | ---: | ---: |
| No hits in this limited query | 1,558 | 3,153 | 4,711 |
| Citation candidates requiring review | 1,103 | 1,043 | 2,146 |
| More than 100 hits; refinement required | 278 | 334 | 612 |
| Not searched | 0 | 0 | 0 |

All canonical labels now have cached searches, including the existing-claim
records excluded from the earlier no-claim cohort. All initially planned name
queries have run for all 2,939 records; none remain partial. **Completed initial
searches do not mean primary review is complete.** All 2,939 primary-review statuses remain
pending in this discovery ledger, independently of the separately documented
claim-level curations.

Alias queries retain 24,785 additional record-citation memberships across 756
records relative to each canonical query's retained first page. These are not
24,785 distinct publications or verified findings, nor proof that a citation was
absent from a truncated canonical result set. Each OR-query keeps its complete
name group; no individual matching name is inferred from a returned citation.

Spot checks illustrate why identity and primary evidence still need review:

- `CHEBI:140779` has aliases `TTD` and `TATD`; its alias group returned 87
  citations, including titles about a TatD-like nuclease and human cancer.
  These metadata hits do not establish resistance to the compound.
- The two mefloquine stereoisomer records, `CHEBI:63684` and `CHEBI:63687`,
  produced equal hit counts (335) and identical retained citation identities
  from their different alias queries. This is not stereochemical equivalence
  or evidence that either precise form was tested.
- Cerulenin's canary returned 94 citations and no added identities relative to
  its retained canonical page. PMID:39363718 was already in that canonical
  result. The [2024 primary publisher page](https://onlinelibrary.wiley.com/doi/10.1002/anie.202414941)
  exposes an abstract and data-availability statement, not inspected full
  Results. The author-manuscript and publisher-supplement requests returned
  HTTP 403. This self-resistance research lead remains unresolved; it supplied
  no new curated determinant, allele, protein, genome or AST measurement.

Names not yet present in the records remain a separate historical-name gap.
The first 100 citations per query remain a discovery bound, not an exhaustive
literature review. Citation discovery never writes biological records; the
PR-39, daclatasvir and PHI-base scope curations were applied separately after
their respective batches ended.
The refreshed discovery artifacts pin their post-curation record hashes.

### Truncated-query expansion

The 612 truncated record-query memberships represent **611 distinct queries
across 384 records**. A new [expansion plan](2026-10-08-resistance-discovery-expansion-plan.json)
retains every membership and its name provenance. The historical first-page
artifacts above remain unchanged. Queries and chemical identities are not
merged, narrowed or reinterpreted to make searches smaller.

A spectinomycin (`CHEBI:9215`) canary retrieved two pages totaling 1,060 unique
citations. Independent inspection verified the raw response hashes, origin,
request echoes, cursor handoff, page lengths and source-qualified citation
identities before a class-balanced batch of 50 additional pages. Two subsequent
bounded batches each retrieved 150 more pages. The initial 52-page checkpoint is
preserved under `reports/resistance-grounding-2026-10-07/expansion-first-checkpoint/`.
The intermediate 202-page checkpoint is preserved in `expansion-second-checkpoint/`
and the 352-page checkpoint in `expansion-third-checkpoint/` under the same local
cache. A further bounded batch retrieved exactly 260 pages; that 612-page
checkpoint is preserved in `expansion-fourth-checkpoint/`. After two guarded
stops and recovery canaries, a conflict-aware batch retrieved 269 new responses
under a 468-response cap. The historical pre-restart
[checkpoint](2026-10-08-resistance-discovery-expansion.json),
[compressed candidate index](2026-10-08-resistance-discovery-expansion-candidates.json.gz), and
[612-membership ledger](2026-10-08-resistance-discovery-expansion-ledger.tsv)
retain the result:

| Cursor-expansion state | Distinct queries |
| --- | ---: |
| Complete traversal; primary review still pending | 520 |
| Conflicted traversal; separate restart required | 91 |
| Partial traversal without a detected conflict | 0 |
| Expansion not started | 0 |

The **795 accepted cursor pages**, plus **91 separately pinned rejected pages**,
cover 384 records across all seven filing classes. Accepted pages retain
465,621 query-citation memberships representing 166,001 distinct source-qualified
citations. Comparison with **all original queries for each record**, rather
than only its canonical page, yields **278,062 added record-citation memberships
across 383 records**. None is automatically an independent experiment, exact
compound match, protein/allele grounding, taxon assignment or measured phenotype.
No hit-count drift relative to the historical queries was observed in accepted
chains. There are 183 more accepted pages and 61 more completed traversals than
at the preserved 612-page checkpoint.

The candidate export is lossless gzip: **38,082,158 stored bytes** expand to
**203,884,217 exact JSON bytes**. The checkpoint's `compressed_artifacts` records
both SHA-256 digests and sizes. Read it with `gzip.open(path, "rt")` and a JSON
parser, or decompress it with `gzip -dc`. Compression omits filename and time
headers; repeated canary exports were byte-identical. The prior uncompressed
352-page export was preserved and checksum-verified before removing the stale
public copy. Local cache snapshots are ignored by git, not committed archives.

Completion means distinct retained rows equal the provider's reported count in
a consistent cursor chain. It does not prove an atomic provider-index snapshot,
exhaustive literature coverage or completed primary review. All 611 query
primary-review statuses remain pending. The **91 conflicted queries across 64
records remained incomplete at that checkpoint**, despite there being no ordinary partial traversal
left. The checkpoint's `query_conflicts` and candidate index retain each rejected
response's request metadata, body hash, cache-file hash, row count, and failure reason. Fifty
are classified as cross-page publication overlap and 41 as page-length mismatch;
88 of the 91 also contain a citation already present in their accepted prefix.
No rows from a rejected page were salvaged by deduplication. Resume skips these
chains; they need separately cached fresh traversals, not an unchanged retry or
an overwrite of historical pages. The cause of the provider inconsistencies is
not established. Historical-name and biological-review gaps also remain.
Discovery changed no biological record, source inventory, claim or curation
event. Its refreshed exports pin all 2,939 current post-Nakayama-curation
record hashes; all 7,466 original query caches remain unchanged. The separately
verified FUR1, Darlington and Nakayama curations are not attributed to citation metadata.
The preceding 795-page export and census are preserved under
`reports/resistance-grounding-2026-10-07/nakayama-before-research/`; the hash
refresh adds no citation or completed primary review. NCBI and #1040 remain deferred.

### Fresh Retrieval Cohort (Historical)

The [fresh-cohort checkpoint](2026-10-09-resistance-discovery-restart.json)
preserves all historical responses and retains the 520 completed query chains
without refetching them. All 91 previously conflicted queries restart at the
initial cursor in a separate cache namespace, with unchanged query terms,
parameters, record identities and name provenance. A two-page nevirapine canary
completed first; the subsequent bounded batch retrieved 207 additional pages
under a 500-page cap. **18 queries recovered complete traversals; 73 conflicted
again.** The selected combined index at that checkpoint had **538/611 complete traversals**,
covering the same 612 query-record memberships across 384 records.

The [combined ledger](2026-10-09-resistance-discovery-restart-ledger.tsv) covers
every original membership. The [compressed retry delta](2026-10-09-resistance-discovery-restart-candidates.json.gz)
contains only the 91 restarted query chains; the descriptor identifies the 520
unchanged chains in the pinned historical index. No old prefix is spliced into
a new chain. The selected index contains 796 accepted pages and 73 rejected
pages, retaining 457,027 query-citation memberships and 169,129 distinct citation
identities. Eight fresh query counts differ from their historical first pages.

Some fresh conflicted chains retain fewer citations than their historical valid
prefixes. Both histories remain available; the descriptor separately accounts
for their citation union, which is discovery evidence rather than a validated
single cursor traversal. Across the two indices, that union is **175,437 distinct
citations**: 9,436 appear only in the selected retry index and 6,308 only in the
historical index. The original 7,466 name-query responses and all 886
historical expansion responses remain unchanged. No citation is discarded from
the historical archive because a newer attempt failed earlier.

A separate amikacin ordering canary completed three tightly sequenced pages
under both the default order and the documented `P_PDATE_D desc` order, each
retaining 2,503 unique citations. It remains separate from the batch's conflicted
amikacin chain. Both outcomes succeeded, so this comparison does **not** establish
the cause of the conflict or demonstrate that sorting caused recovery. The
checkpoint identified query-local traversal in another pinned cohort as the
next retrieval test, preserving these results and unchanged lexical queries.
All primary-review statuses
remain pending; no biological record, source inventory or curation event changed.

### Query-Local Retrieval (Historical)

The [third-cohort checkpoint](2026-10-09-resistance-discovery-query-local.json)
reuses the preceding 538 complete chains and the separately verified complete
default-order amikacin canary. The other 72 failed queries start from their
initial cursors in a new namespace, with unchanged query terms and parameters.
The optional `--traversal-order query-local` finishes each eligible query before
advancing; the existing breadth-first default is unchanged.

The bounded run finished after **337 new responses** under a 500-response cap.
**67 of 72 fresh traversals completed**; together with the reused canary, this
recovers 68 of the preceding 73 conflicts. The selected index at that checkpoint contains
**606/611 complete traversals and five conflicts**, covering all 612 planned
query-record memberships across 384 records. Retrieval recovery does not
establish its cause or guarantee a consistent live-index snapshot.

The [combined ledger](2026-10-09-resistance-discovery-query-local-ledger.tsv)
retains every membership. The [compressed delta](2026-10-09-resistance-discovery-query-local-candidates.json.gz)
contains only the 73 replacement chains, with the canary's reuse explicitly
identified; the 538 unchanged chains remain in the pinned parent index.
There are 1,039 accepted pages and five fully rejected pages, retaining
666,278 query-citation memberships and **218,994 distinct citation identities**.
All 175,437 identities in the union of the preceding two indices occur in this
selected index, with **43,557 additional identities**. This global identity
comparison does not merge query chains, establish chemical relevance, or turn
the three retrieval histories into one atomic snapshot.

| Record | Query | Retained / Reported Citations | Rejection |
| --- | --- | --- | --- |
| Ampicillin (`CHEBI:28971`) | 0 | 3,000 / 6,611 | Cross-page overlap |
| Penicillin O (`CHEBI:51207`) | 2 | 2,000 / 5,671 | Cross-page overlap |
| Polysulfur (`CHEBI:17909`) | 1 | 31,000 / 65,775 | Cross-page overlap |
| Tioguanine (`CHEBI:9555`) | 1 | 2,000 / 2,946 | Page-length mismatch, also overlapping |
| Methicillin (`CHEBI:6827`) | 2 | 7,000 / 9,836 | Cross-page overlap |

Each rejected page contains one previously accepted citation identity; none
was repaired by salvaging its other rows. The polysulfur query includes the
source aliases `S`, `Sn`, `Sulfur` and `sulphur`. Its large reported count is
not polysulfur-specific resistance evidence. The checkpoint explicitly flags
this ambiguity without changing source aliases or estimating relevant hits.
Refinement must remain separate from the preserved original query.
All query primary-review statuses remain pending. No biological claim,
identifier assignment, source inventory or curation event changed in this pass.

### Date-Sorted Retrieval

The [fourth-cohort checkpoint](2026-10-09-resistance-discovery-date-sort.json)
retains the 606 complete parent chains and replaces only the five conflicted
queries above with fresh, isolated traversals. Query text, source aliases,
record memberships, `resultType=lite` and `synonym=false` are unchanged. Only
the request's ordering changes to `sort=P_PDATE_D desc`, documented by the
[Europe PMC REST service](https://europepmc.org/RestfulWebService). No pages
from different attempts are joined into a single chain.

An ampicillin canary independently completed both default-order and date-sorted
traversals: seven pages and 6,611 unique citation identifiers each. Their
identifier sets agree, although their order differs. Both attempts succeeded;
this does **not** establish that sorting caused recovery or explain earlier
conflicts. The remaining four date-sorted traversals completed within the
100-page batch cap, using 85 newly cached responses. Including both canary
orders, 99 new cached responses were verified. This stored-response count does
not count transient failed HTTP attempts.

| Record | Query | Unique Citations | Pages |
| --- | --- | --- | --- |
| Ampicillin (`CHEBI:28971`) | 0 | 6,611 | 7 |
| Penicillin O (`CHEBI:51207`) | 2 | 5,671 | 6 |
| Polysulfur (`CHEBI:17909`) | 1 | 65,775 | 66 |
| Tioguanine (`CHEBI:9555`) | 1 | 2,946 | 3 |
| Methicillin (`CHEBI:6827`) | 2 | 9,836 | 10 |

The [combined ledger](2026-10-09-resistance-discovery-date-sort-ledger.tsv)
retains all 612 query-record memberships across 384 records. The
[compressed delta](2026-10-09-resistance-discovery-date-sort-candidates.json.gz)
contains only the five replacement chains. Together with the 606 complete
parent chains, the selected index has **611/611 complete traversals**, 1,086
accepted pages, no selected rejected pages, and **712,117 query-citation
memberships**. Its **241,143 distinct citation identities** include every
identity in the preceding selected index plus **22,149 additional identities**.
Each fresh chain also retains every identifier in its own previous valid prefix.
These comparisons do not merge attempts or count unique studies or experiments.
The earlier rejected pages and all four retrieval histories remain preserved.

A separate current-name comparison rebuilt the inventory using the
collection-aware loader: all **2,939 records, 16,030 names and 7,469 query
memberships** retain their historical compound identities, names and queries.
Twenty-two record hashes changed during the preceding SDH8 curation; those
historical pins are not rewritten. The comparison binds the unchanged discovery
scope to the latest SDH8 corpus census without treating curation changes as
new searches.

Search completion is limited to these planned queries and their cached API
counts, not an atomic live-index snapshot, exact chemical relevance, or complete
organism/gene/allele coverage. In particular, the polysulfur `S`/`Sn` aliases
remain ambiguous. All primary-review statuses remain pending and all 2,939
records remain in scope. No biological record, source inventory, identifier
assignment or curation event changed in this retrieval pass.

## Hygromycin B Modifier Review

The [research dossier](2026-10-08-hygromycin-yeast-modifier-grounding.json)
reviews three primary studies for hygromycin B (`CHEBI:16976`,
`GRRNUXAQVGOGFE-NZSRVPFOSA-N`):
[UBC6/UBC7](https://www.micropublication.org/journals/biology/micropub-biology-001276/),
[CUE1](https://www.micropublication.org/journals/biology/micropub-biology-002032/)
and [UFD2](https://www.micropublication.org/journals/biology/micropub-biology-002152/).
Their primary XML Results/Description, figure captions and reagent tables were
inspected. The original text-only dossier is preserved. A separate
[figure and comparator follow-up](2026-10-08-hygromycin-yeast-figure-followup.json)
now records manual full-resolution review of all three publisher-linked PNG
figures: ten labeled panels, comprising seven growth panels and three schematics.
The qualitative growth comparisons agree with the retained sensitization
direction, but effects vary by displayed condition. Schematics are not direct
binding or biochemical evidence. No quantitative effect size was inferred.

All four genes have reviewed UniProt reference entries in release `2026_03`:

| Gene | Reference Protein | Systematic Locus | Entry / Sequence Version |
| --- | --- | --- | --- |
| UBC6 | [P33296](https://www.uniprot.org/uniprotkb/P33296/entry) | YER100W | 197 / 1 |
| UBC7 | [Q02159](https://www.uniprot.org/uniprotkb/Q02159/entry) | YMR022W | 208 / 1 |
| CUE1 | [P38428](https://www.uniprot.org/uniprotkb/P38428/entry) | YMR264W | 175 / 2 |
| UFD2 | [P54860](https://www.uniprot.org/uniprotkb/P54860/entry) | YDL190C | 190 / 3 |

Four additional comparator genes have reviewed references in the same release:

| Source Gene | Reference Protein | Systematic Locus | Entry / Sequence Version |
| --- | --- | --- | --- |
| HRD1 | [Q08109](https://www.uniprot.org/uniprotkb/Q08109/entry) | YOL013C | 190 / 1 |
| DOA10 (UniProt preferred name: SSM4) | [P40318](https://www.uniprot.org/uniprotkb/P40318/entry) | YIL030C | 205 / 1 |
| ASI1 | [P54074](https://www.uniprot.org/uniprotkb/P54074/entry) | YMR119W | 161 / 1 |
| ASI3 | [P53983](https://www.uniprot.org/uniprotkb/P53983/entry) | YNL008C | 154 / 2 |

`DOA10` is an explicit synonym on the `SSM4` entry, not a second gene mapping.
Combined-loss comparator phenotypes do not establish an individual effect for
each gene. These four crosswalks are not four additional causal resistance claims.

These identify S288c reference proteins, not the tested gene-loss derivatives.
Species `NCBITaxon:4932` is supported through cached UniProt taxonomy; reference
strain `NCBITaxon:559292` is not assigned to experimental derivatives. The follow-up
retains 26 source-qualified plotted subject memberships: ten focal, seven
multi-gene comparator, three additional UBC7 comparator and six wild-type
memberships. These are not 26 distinct isolates. MHY500 and BY4741 comparators
remain distinct; repeated subjects across papers are not independent replicates.

The source tables disagree on one alias: the UBC6/UBC7 paper calls `VJY305`
`SKY252`, whereas the UFD2 paper calls it `SKY242`. Both cite Habeck et al. (2015).
`HYGROMYCIN-VJY305-SKY-ALIAS-CONFLICT` remains unresolved: the shared citation
and gene combination do not justify choosing an alias, merging subjects,
asserting distinct isolates, or assigning an experimental strain/genome ID.

The observed direction is **loss-associated sensitization**, retained as
qualitative growth comparison, not a resistance-conferring allele or clinical
resistance call. No MIC or zone diameter is inferred. CUE1 includes reported
complementation; UFD2 describes it as additional confirmation, not a reported
result. The UBC6/UBC7 paper cites an earlier discordant result. At the original
checkpoint, Europe PMC metadata confirmed PMID `16118187`, PMCID `PMC1456077`
and DOI `10.1534/genetics.105.046888`, but its EBI full-text XML route returned
HTTP 500 and its PDF route returned HTTP 403 with a non-PDF body. Those failed
responses remain preserved.

The [discordance follow-up](2026-10-09-hygromycin-discordance-followup.json)
now records manual review of the older paper's
[author-uploaded text transcription](https://www.researchgate.net/publication/7642934_Saccharomyces_cerevisiae_Ub-Conjugating_Enzyme_Ubc4_Binds_the_Proteasome_in_the_Presence_of_Translationally_Damaged_Proteins).
Its Results report negative UBC6/UBC7 single-loss comparisons under the tested
conditions, and an unshown combined-loss comparison. UBC4 loss sensitized;
UBC5 loss alone did not impair growth. The experimental background remains
unresolved. This was text review, not PDF or visual figure review; the separate
direct fetch returned HTTP 403 and is not a successful full-text cache.

Two additional reviewed UniProt references were verified in release `2026_03`:
UBC4 [P15731](https://www.uniprot.org/uniprotkb/P15731/entry), locus `YBR082C`,
entry/sequence version `228/1`; and UBC5
[P15732](https://www.uniprot.org/uniprotkb/P15732/entry), locus `YDR059C`,
version `207/1`. Both remain S288c references, not tested alleles or strains.
The studies' disagreement and the VJY305 alias conflict remain unresolved.
The newer authors' proposed exposure difference is a hypothesis, not a verified
explanation. No biological record changed and no NCBI endpoint was contacted.

These findings remain susceptibility-modifier research. The five existing CARD
assertions are unchanged; no exact experimental allele, protein, genome,
drug-target or antibiotic-inactivation assignment was added. This focused
review does not complete the hygromycin B record or the all-record investigation.

### Additional Primary Studies

The [additional primary dossier](2026-10-09-hygromycin-additional-primary-grounding.json)
reviews publisher JATS Description, reagent tables and every Figure 1 panel in
three further studies. It preserves 26 source-qualified reagent-table memberships
and 13 comparison groups; neither count represents independent studies or
biological replicates. Repeated strain labels are not silently merged across papers.

| Primary Study | Focal Findings and Scope |
| --- | --- |
| [Niekamp et al., 2019](https://www.micropublication.org/journals/biology/micropub-biology-000193/) | TOM1 loss comparisons show sensitization in two independently sourced subjects. BY4741 and BY4742 comparators remain distinct. |
| [Woodruff et al., 2021](https://www.micropublication.org/journals/biology/micropub-biology-000403/) | ASI1 and ASI3 comparisons show sensitization. ASI2 comparisons, including independently generated subjects, do not show the same disadvantage. HUL5 comparisons are negative in two backgrounds under the tested conditions. |
| [Daraghmi et al., 2023](https://www.micropublication.org/journals/biology/micropub-biology-000738/) | Independent ATG39 and ATG40 comparisons show sensitization. The joint comparison is retained separately, without assigning its additional effect to either gene alone. |

These are qualitative growth findings, not MICs, clinical categories, or proof
of a direct antibiotic target. Negative findings are restricted to the reported
comparisons. The authors' broader protein-quality-control interpretations do
not establish a specific biochemical resistance route. Source material is named
hygromycin B; no independent lot or structure analysis is asserted.

Seven reviewed UniProt entries were verified in release `2026_03`:

| Gene | Reference Protein | Systematic Locus | Entry / Sequence Version |
| --- | --- | --- | --- |
| TOM1 | [Q03280](https://www.uniprot.org/uniprotkb/Q03280/entry) | YDR457W | 209 / 1 |
| ASI1 | [P54074](https://www.uniprot.org/uniprotkb/P54074/entry) | YMR119W | 161 / 1 |
| ASI2 | [P53895](https://www.uniprot.org/uniprotkb/P53895/entry) | YNL159C | 146 / 1 |
| ASI3 | [P53983](https://www.uniprot.org/uniprotkb/P53983/entry) | YNL008C | 154 / 2 |
| HUL5 | [P53119](https://www.uniprot.org/uniprotkb/P53119/entry) | YGL141W | 183 / 1 |
| ATG39 | [Q06159](https://www.uniprot.org/uniprotkb/Q06159/entry) | YLR312C | 132 / 1 |
| ATG40 | [Q99325](https://www.uniprot.org/uniprotkb/Q99325/entry) | YOR152C | 142 / 1 |

Each entry has an explicit SGD cross-reference. These are **S288c reference
proteins**, with reference strain `NCBITaxon:559292`; experimental species
`NCBITaxon:4932` remains separate. Both taxonomy responses were reused from pinned
UniProt caches. No reference accession or strain TaxID was assigned to a tested
derivative, and no allele, genome or sample accession was invented.

The source cited for VJY305 is
[Habeck et al., 2015](https://rupress.org/jcb/article/209/2/261/46118/The-yeast-ERAD-C-ubiquitin-ligase-Doa10-recognizes).
Its supplementary Table S2, printed page S6, explicitly lists **SKY252** in the
S288C-background group. The downloaded PDF and rendered table were inspected;
the 2019 and 2023 reagent tables likewise explicitly connect VJY305 to SKY252.
This corroborates SKY252 but does not prove that the later SKY242 label is a
typographical error. The conflict remains open and source aliases are unchanged.
The older UBC6/UBC7 discordance and its original-figure review gap also remain open.

No resistance assertion or curation event was added. The seven-gene reference
cohort is not an exhaustive list of all genes mentioned in these papers, and
this review does not complete the hygromycin B record or the 2,939-record goal.

## 5-Fluorouracil Grounding

At the first checkpoint, `CHEBI:46345` (`GHASVSINZRGABV-UHFFFAOYSA-N`) had no
resistance assertion. Its historical [FUR1 research snapshot](2026-10-07-5-fluorouracil-fur1-lead.json)
retains reviewed [UniProtKB:P18562](https://www.uniprot.org/uniprotkb/P18562/entry),
gene `FUR1`, locus `YHR128W`, sequence version 2, and four database annotations
citing two primary papers. This is a discovery lead, not new record curation.

The [1991 publisher summary](https://link.springer.com/article/10.1007/BF00309592)
numbers the `fur1-5` substitution at residue 134, whereas UniProt annotates
residue 99. The full Results were unavailable; no coordinate conversion was
verified. UniProt flags earlier sequences for an extended N-terminus, which
is a review lead rather than proof of the offset. Its 1990 citation identifies
FL100; the canonical protein's S288c TaxID `559292` was not assigned to that
experimental background. Species `NCBITaxon:4932` resolves through UniProt.
No genome, mutant-specific protein accession, linked quantitative AST, or
clinical resistance category was established. The 1970 historical study's
Europe PMC full-text request returned HTTP 500, and its publisher returned 403;
neither was treated as inspected primary Results. NCBI was not contacted.

A later [primary study](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1011002)
supports two FUR1-associated cohorts derived from LL13-040 and NC-02. Results
and Figures 2/4C link gene-level observations to relative colony growth with
5-fluorouracil. These are not parental-strain resistance claims or exact-allele
causal assignments. Two qualified associations were curated; no MIC conversion
or clinical category was inferred. The [curation dossier](2026-10-08-fur1-cohort-grounding.json)
pins cached primary text and preserves the older allele questions as unresolved.

UniProtKB:P18562 (entry 192, sequence 2; S288c, TaxID 559292; locus YHR128W)
remains reference-only. Species TaxID 4932 is grounded through UniProt. The
literal experimental-background query returned zero entries; this is not an
absence claim. No experimental protein accession, strain TaxID, sample or genome
was assigned. Review removed descriptive cohort labels from the `strain` slots;
the context remains in claim labels. Curation and scope correction each append
one event. At that checkpoint, all unrelated fields and 2,938 other records
remained unchanged; this is not whole-record signoff.

## Flucytosine Grounding

Flucytosine (`CHEBI:5100`, `XRECTZIEBJDKEO-UHFFFAOYSA-N`) was reviewed as a
separate structure. Its exact synonyms include 5-FC and 5-Fluorocytosine. Direct
5-FC Results and Figures 2/4C in the
[primary study](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1011002)
support two FUR1-associated cohorts; this is not a transfer of 5-fluorouracil
evidence. These are compound-specific claims from the same study cohorts, not
additional independent experiments. The eight CARD-owned route assertions remain
unchanged. Two qualified
curator associations were appended. A subsequent serialization review restored
the original YAML key order without changing biological values; both writes have
their own curation events.

The [compound-specific dossier](2026-10-08-flucytosine-fur1-grounding.json)
pins the record before/after hashes, original CARD slice, primary sections and
shared UniProt responses. Species TaxID 4932 is grounded; P18562, YHR128W and
S288c TaxID 559292 remain reference-only. Cohort background names are in labels,
not synthetic strain fields. The claims do not cover every screened derivative
or establish individual-allele causality. Growth AUC was not converted to MIC;
no clinical category, experimental protein, sample or genome was assigned.

The other 2,938 records, including the earlier 5-fluorouracil curation, are
unchanged from this follow-up's before-image. Replaying the curation made no
write or additional history event. The record remains `SEEDED`, and its broader
primary and exact-allele investigation remains open.

## Artifacts and reproducibility

The original local, non-publishing evidence cache is
`reports/resistance-grounding-2026-10-07/`. It contains raw UniProt responses with
request URLs, timestamps, release headers, SHA-256 digests, parsed protein and
taxonomy entries, the complete record census, and claim-level review flags.
Its `records.tsv` is a historical per-record ledger. Existing primary references remain
pending until their actual results and experimental identities are checked.
The review snapshots are also retained as
[the earlier 2,939-record ledger](2026-10-07-resistance-grounding.tsv) and
[the 217-observation PHI-base audit](2026-10-07-phibase-grounding.json).
The ledger's `verified_reference_accessions` and `lineage_checked_taxids`
columns currently describe the PHI-base pass only; curator-owned grounding is
documented separately above. Its hashes describe the earlier HDF1 checkpoint,
not the current post-fenpicoxamid corpus.
The [current 2,939-record ledger](2026-10-09-resistance-grounding.tsv) is generated
from the new `reports/resistance-grounding-2026-10-09-fouche/` census. The
[checkpoint reconciliation](2026-10-09-fouche-checkpoint-reconciliation.json)
links the 22 changed record hashes while retaining prior candidate audits and
their historical snapshots unchanged. No candidate or whole-record research
status is promoted by this reconciliation.
Those reference columns can include IDs withheld from experimental-subject
fields by a primary-source identity review; they are not a list of verified
experimental alleles or isolate accessions.
`publications.json` resolves all 77 unique primary PMIDs cited by the initial
resistance assertions through Europe PMC at EMBL-EBI, in four batches of at most
20 identifiers. It retains returned bibliographic metadata and request
provenance, not reviewed experimental conclusions or copied full abstracts.
An exact-PMID UniProt search found 101 protein candidates citing 27 of those
papers, including 88 accessions outside the existing PHI-base protein set.
The [citation candidate index](2026-10-07-resistance-citation-candidates.json)
records both hits and empty results. These are paper-to-protein leads, not
automatic compound-to-allele assignments; a paper may discuss several proteins
or reference and experimental strains. The other 50 papers are not thereby
evidence of absent protein mappings.

```bash
just audit-resistance-grounding inventory --output-dir reports/resistance-grounding-2026-10-07
just audit-resistance-grounding proteins --output-dir reports/resistance-grounding-2026-10-07
just audit-resistance-grounding analyze --output-dir reports/resistance-grounding-2026-10-07
just audit-resistance-grounding ledger --output-dir reports/resistance-grounding-2026-10-07
just audit-card-grounding proteins --output-dir reports/resistance-grounding-2026-10-07
just audit-card-grounding taxonomy --output-dir reports/resistance-grounding-2026-10-07
just audit-card-grounding analyze --output-dir reports/resistance-grounding-2026-10-07
just audit-card-grounding contexts --output-dir reports/resistance-grounding-2026-10-07
just audit-card-grounding archives --output-dir reports/resistance-grounding-2026-10-07
just audit-hivdb-grounding --output-dir reports/resistance-grounding-2026-10-07
just discover-resistance-literature plan --output-dir reports/resistance-grounding-2026-10-07
just discover-resistance-literature analyze --output-dir reports/resistance-grounding-2026-10-07
just discover-resistance-aliases plan --output-dir reports/resistance-grounding-2026-10-07
just discover-resistance-aliases analyze --output-dir reports/resistance-grounding-2026-10-07
```

The commands above document the earlier checkpoint; use a new output directory
for subsequent inventories rather than overwriting pinned historical snapshots.
They default to offline execution. On a new machine the protein stage
requires either the captured cache or explicit `--allow-network` after a
reviewed canary. The CARD protein and taxonomy stages follow the same opt-in
rule. Requests are confined to UniProt and redirects are not followed. Successful
responses are cached; transient failures get at most three attempts. Pagination
checks release, count, unique accessions, cursor progress, and unchanged query
parameters. Taxonomy and analysis refuse concurrent snapshot replacement.
No genotype-analysis pipeline or paid research service is run.
The HIVDB audit is offline-only and requires the cached, pinned GitHub
gene/strain definitions and UniProt taxon response. It checks inventory rows,
size, checksum, version and algorithm against the adopted manifest.

Citation discovery uses only EMBL-EBI Europe PMC, never an NCBI endpoint. Resume
it with `just discover-resistance-literature search --output-dir
reports/resistance-grounding-2026-10-07 --max-new-requests 500 --allow-network`.
Successful cached queries do not consume the new-query bound. The client checks
response origin, echoed query, checksum, count and source-qualified IDs, rejects
redirects, and bounds transient retries. Planning and analysis refuse stale
record/census hashes. The empty-cohort case still writes a header-only ledger.
A pooled HTTP session is reused and closed for each bounded batch; a canary and
regression tests verified this change before resuming the final batch.

Resume the broader all-record pass with `just discover-resistance-aliases search
--output-dir reports/resistance-grounding-2026-10-07 --max-new-requests 500
--allow-network`, then run its `analyze` stage. It uses the same citation-only
client and preserves existing single-label cache keys. Alias groups contain at
most four names within a client-side encoded-URL bound; no name is silently
dropped. Query rounds visit one group per record, with class-balanced record
order. Planning reads complete records through the collection-aware loader;
search and analysis reproduce that name inventory and reject stale or altered
plans. These commands write discovery artifacts, never biological records.

Truncated-query expansion uses `just expand-resistance-discovery plan
--output-dir reports/resistance-grounding-2026-10-07`, followed by `search` with
explicit `--allow-network --max-new-pages 50`, then the offline `analyze` stage.
The page bound permits at most three HTTP attempts per new page, including
retries. `--only CHEBI:9215` selects the inspected two-page canary record.
The original 100-citation caches remain unchanged; new pages use distinct
1,000-row cache keys and preserve the exact lexical queries. This follows
[Europe PMC's cursor/page-size interface](https://europepmc.org/docs/EBI_Europe_PMC_Web_Service_Reference.pdf)
and [citation-only `lite` result type](https://europepmc.org/RestfulWebService).
Shared queries retain all record/name memberships. After filtering for
truncation, queries are rebalanced across classes; resume visits the shallowest
incomplete chains first. Count/version drift within a chain, cursor cycles,
duplicate citation identities, altered query echoes, stale inputs and corrupt
caches fail closed. A changed hit count relative to the historical first page
is reported rather than mixing old and new pages. Matching counts and versions
do not prove an atomic snapshot of the live provider index. No truncated query
is called a completed primary review.

The original source files are `phibase_amr_export.csv` and `phipo.csv`; their
checksums and URLs remain in `data/raw/MANIFEST.yaml`. The corrected inventory
is reproducible through `scripts/extract_phibase_amr.py`. Record changes use
the normal seeder, validated writer, and curation-event path.

## Verification checkpoint

Verification sections below are dated historical checkpoints unless explicitly
identified as the current checkpoint. Later runtime findings supersede earlier
environment limitations, not the historical evidence or preservation results.

### Posteraro Subject Context (Current Curation Checkpoint)

The [identifier-scope dossier](2026-10-09-posteraro-subject-reference-grounding.json)
reviews the single `PHIG:8831` association on fluconazole, `CHEBI:46081`.
[Posteraro et al. (2003)](https://onlinelibrary.wiley.com/doi/full/10.1046/j.1365-2958.2003.03281.x)
names **BPY22.17** in primary Results and the Figure 1 caption, separately from
the parent **BPY22**. PHI-base's spelling **BYP22** remains in provenance, not
as an assumed synonym. Only the experimentally supported subject label and
identifier scope are corrected; the inherited alteration, phenotype, assay and
`UNKNOWN` mechanism type are preserved.

Current UniProt **Q8X0Z3** is an unreviewed AFR1 reference with the same paper
citation, entry version **116**, sequence version **1**, release **2026_03**.
It names **CR 22.17** and archive **AJ318062 / CAC59691.2**, whereas the paper
names genomic deposit **AJ428201**. Citation agreement alone does not prove
these deposits or strain labels equivalent. The accession is therefore
reference-only, not assigned to the experimental subject. The bounded UniProt
`AJ428201` query returned no results; this does not establish biological absence.

The paper's serotype-D qualification also prevents automatic assignment of
the source TaxID **5207**. Current UniProt taxonomy includes that qualified
historical name only under `otherNames` for **40410**, not an exact scientific
name or explicit synonym. Neither TaxID is assigned to the experiment. The
source organism label is retained, and the unresolved modern species mapping
is explicit. No NCBI endpoint was requested.

The text review used indexed publisher full text and captions, not visual
figure inspection or a locally cached native primary file. No new sequences,
variant specifications, constructs, protocols, coordinates, experimental
genomes or numerical resistance measurements were exported. This is not full
phenotype validation or whole-record completion.

The canary and guarded bulk write changed **one identifier-scoped claim** and
refreshed **184 prior review checksums** across **22 records**, with one
meaningful curation event per changed record. **2,917 records** remain
byte-identical. The source inventory is unchanged. An offline replay made zero
writes. PHI-base identifier review now covers **185/217 associations**; **32
associations across 13 papers** remain pending.

The [current all-record ledger](2026-10-09-posteraro-resistance-grounding.tsv)
and [publication reconciliation](2026-10-09-posteraro-checkpoint-reconciliation.json)
retain all **2,939 records**, their current hashes and open research statuses.
Counts remain **4,788 resistance assertions across 300 records**, including
**33 curator-authored claims across 22 records**. The ledger's reference columns
remain PHI-base metadata, not experimental assignments. Earlier dossiers retain
their historical hashes rather than being rewritten to match the new corpus.

Adversarial review dispositions:

- **Subject conflation:** corrected the subject slot from primary Results;
  preserved the original source spelling without claiming synonymy.
- **Reference conflation:** withheld the experimental protein assignment;
  explicit archive and strain-label disagreements remain unresolved.
- **Taxonomic overreach:** retained the source label and withheld a modern
  species assignment through an `otherNames`-only lead.
- **Coverage overstatement:** counted an identifier-scope review, not a new
  measured phenotype, exact allele or completed record.
- **Stale test expectations:** the first focused run had **204 passed, 13
  failed**; the next had **127 passed, one failed**. Failures exposed stale
  coverage expectations and a narrow no-TaxID exception. Exact new expectations and
  citation-specific assertions replace them; no production gate was relaxed.

The first full authoritative run completed its test stage with **2,198 passed,
five failed, three skipped and one existing warning**. All five failures were
live-corpus assertions expecting 184 rather than 185 identifier-scoped
associations. An ignored-file-inclusive search located the five assertions;
their historical-dossier counts were left unchanged. All **44 focused
regression tests passed** after the five one-value fixes.

The [final preservation reconciliation](2026-10-09-posteraro-final-reconciliation.json)
retains the earlier publication audit and verifies exactly those additional test
edits. Against the original checkpoint snapshot, **6,633 protected files**,
including **138 earlier research artifacts**, remain byte-identical. All **2,939 current
record hashes** still match the ledger. Publication changed only **24 HTML
pages** and replaced **two record downloads**; decompressed downloads equal
the collection-aware records and retain their activities. The rendered subject
cell carries BPY22.17 without the withheld reference IDs. Embedding documents,
map artifacts, site index and sitemap are unchanged. No browser visual review
was performed.

The [final verification record](2026-10-09-posteraro-verification.json) pins the
successful terminal run of all **11 authoritative QC gates**: **2,203 tests
passed**, three known empty command-frontmatter parameter sets were skipped,
and the existing SSSOM/LinkML deprecation warning remained. Strict validation
reported **zero errors across 2,939 records**. Corpus reproduction found no
missing or unexpected records, field drift or lockfile drift. The chemical map
and generated site are current. No gate, dependency or production behavior was
changed to obtain this result.

The post-QC preservation replay passed with the same artifact hashes. Earlier
failed runs and their scoped fixes remain recorded rather than being replaced
by the successful log. No NCBI request, source adoption, outreach or GitHub
mutation occurred. The complete 2,939-record investigation remains open; this
checkpoint does not complete experimental-allele or whole-record review.

### Fungal CARD Reference Follow-up (Previous Research Checkpoint)

The [reference dossier](2026-10-09-card-fungal-reference-grounding.json)
investigates `ARO:3009269`, `ARO:3009270`, and `ARO:3009638`, represented by
three existing assertions on terbinafine and fluconazole. The pinned ontology
and adopted inventory agree on explicit `confers_resistance_to_antibiotic`
edges. Missing named ancestry is therefore a review flag, not grounds for
deleting those assertions. No source assertion was replaced or reclassified.

| Reference | Grounding | Limit |
| --- | --- | --- |
| SQLE, UniProtKB:F2STB6 | Explicit EGD89476.1 cross-reference; TERG_05717; reference strain NCBITaxon:559305, species NCBITaxon:5551 | Unreviewed reference protein, not a tested resistance allele |
| UPC2, UniProtKB:Q59QC7 | Reviewed reference; CGD:CAL0000191743; reference strain NCBITaxon:237561, species NCBITaxon:5476 | SC5314 reference context, not the paper's SGY-243 derivatives or a unique generic CARD-term mapping |

[Yamada et al. (2017)](https://journals.asm.org/doi/full/10.1128/aac.00115-17)
distinguishes clinical Trichophyton observations from experiments in a separate
host. [MacPherson et al. (2005)](https://journals.asm.org/doi/10.1128/aac.49.5.1745-1752.2005)
supports context-dependent UPC2 susceptibility, not resistance inferred from
gene presence. Review used indexed primary publisher text; figures were not
visually inspected and no native primary file was cached in this follow-up.
Chemical-form and experimental-identity questions remain unresolved.

UniProt release `2026_03` resolves the separately queried paper names
Trichophyton rubrum, Trichophyton interdigitale, and Candida albicans to species
TaxIDs `5551`, `101480`, and `5476`. CARD's literal `Trychophyton rubrum` query
returned no hit. `Arthroderma vanbreuseghemii` matched only an `otherNames` entry
under Trichophyton mentagrophytes, so the strict scientific-name/synonym resolver
does not assign a TaxID. Source spellings and unresolved outcomes are retained.

The `EZF33561` and `gene_exact:orf19.391` protein queries returned zero results;
these are query-specific results, not claims of biological absence. A separately
recorded species/gene query finds Q59QC7 and its `CaO19.391` reference label.
That reference context is not an exact experimental crosswalk.

The adversarial review records five local findings with dispositions. Four
interpretation hazards are addressed by retaining source edges, separating name
queries and reference contexts, and bounding negative searches. The
`antifungal susceptible Upc2` source-label/context ambiguity remains open;
neither resistance nor susceptibility of an unspecified allele is inferred.
No GitHub issue or upstream contact was made.

Verification: **139 focused tests passed**, including the new reference-only
regressions and the existing CARD taxonomy, term-scope and grounding suites.
Ruff and `git diff --check` passed. Offline dossier reconstruction verifies
all **2,939 record hashes** and **6,550 pre-existing protected files**, including
ignored files, against the checkpoint snapshot. Biological changes and new
curation events are both zero. The full QC suite was not rerun for this
research-only addition. At that checkpoint, the latest completed
biological/publication QC was the papulacandin checkpoint below. Whole-record
review totals did not increase.

### Papulacandin Qualitative Curation (Previous Biological Checkpoint)

The publisher PDF text of [Castro et al. (1995)](https://journals.asm.org/doi/pdf/10.1128/jb.177.20.5732-5739.1995?download=true)
supports author-reported qualitative resistance associations in experimental
yeast derivatives. Methods identify the distinct tested compounds; the Results
on physiological characterization support the following limited curation:

| Exact Compound | Species | Source Gene | Reference-Only Mapping |
| --- | --- | --- | --- |
| Papulacandin B, CHEBI:569624 | Saccharomyces cerevisiae, NCBITaxon:4932 | PBR1 | FKS1, UniProtKB:P38631, YLR342W |
| Papulacandin B, CHEBI:569624 | Schizosaccharomyces pombe, NCBITaxon:4896 | pbr1 | bgs4, UniProtKB:O74475, SPCC1840.02c |
| Papulacandin D, CHEBI:72630 | Schizosaccharomyces pombe, NCBITaxon:4896 | pbr1 | bgs4, UniProtKB:O74475, SPCC1840.02c |

These are not species-wide resistance assertions, predictions from gene
presence or assignments to the parental strains. The budding-yeast claim
retains the paper's non-resistant comparison at the same locus. The
fission-yeast papulacandin D result is not transferred to budding yeast.
Growth susceptibility and biochemical observations remain distinct; no
numeric measurement or clinical interpretation was added.

The [reference dossier](2026-10-09-glucan-inhibitor-grounding.json) preserves
the pre-curation state and the source-specific identity chain. The paper
explicitly equates budding-yeast PBR1 with FKS1. Current reviewed UniProt
**P38631** includes PBR1 as a synonym, entry version **209**, sequence version
**2**. Fission-yeast pbr1 is an explicit alias of bgs4 on the official
[PomBase gene page](https://www.pombase.org/gene/SPCC1840.02c), which links
**O74475**. UniProt's own inspected synonym list omits pbr1; entry version
**158**, sequence version **1**. Both UniProt responses report release
**2026_03**. The PomBase page was inspected through indexed official text,
not retained as a native snapshot; its displayed release was **2026-09-15**.

UniProt taxonomy verifies species **4932/4896** and reference strains
**559292/284812**, including their ranks and parents. The strain TaxIDs and
protein accessions appear only as reference provenance, not as identifiers
of the tested derivatives. Cached budding-yeast taxonomy was reused; no NCBI
endpoint was contacted. No sequences, variants, constructs, protocols,
coordinates or numerical resistance measurements were newly exported.

The text was inspectable through the publisher PDF reader, but direct local
download returned HTTP 403 and visual figure review was unavailable. The
claims explicitly retain that limitation. The [curation dossier](2026-10-09-papulacandin-curation.json)
pins both canaries, three claims and two history events. Both records retain
`SEEDED` status and remain `PENDING_PRIMARY_REVIEW` in the
[current all-record ledger](2026-10-09-papulacandin-resistance-grounding.tsv).
The ledger's reference-accession and lineage columns still have PHI-base-only
scope; these non-PHI reference mappings remain in the linked dossiers.

The [pre-publication reconciliation](2026-10-09-papulacandin-checkpoint-reconciliation.json)
verifies all **2,939** current record paths and hashes. Only the two intended
records and ledger rows changed; **2,937 biological records** remain
byte-identical. All non-resistance fields and existing history prefixes of the
changed records were preserved. An ignored-file-inclusive manifest verifies
**6,472 of 6,474** protected existing files unchanged before publication.
Validated-writer canaries and offline pre-publication replays passed.

Other findings remain leads, not curated claims:

- **Papulacandin A:** the 1995 study is not evidence for this congener.
  [Martins et al. (2011)](https://doi.org/10.1074/jbc.M110.174300) remains a
  bibliography/database lead: EMBL-EBI full-text retrieval returned HTTP 500
  and publisher access was denied or inconsistent. Full Results review is
  incomplete; a search hit does not establish the tested congener.
- **Arborcandin C:** [Ohyama et al. (2004)](https://journals.asm.org/doi/10.1128/aac.48.1.319-322.2004)
  supplies a gene-level FKS1 lead, but the inspected publisher text alternates
  YPH250/YHP250 and ACR79-5/ACR75-5. Those subject labels remain unresolved,
  without silent normalization or an experimental allele assignment.
- [Berzaghi et al. (2019)](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.01692/full)
  reuses historical resistant backgrounds for other compounds; it does not
  replace the original papulacandin evidence. No new compounds were imported.

The [publication audit](2026-10-09-papulacandin-publication.json) verifies
**two freshly encoded documents**, **2,937 byte-identical reused vector rows**,
and a full PaCMAP projection. Sixteen unchanged controls match within
`0.000030517578125` maximum absolute float16 difference. The current document
fingerprint is **`0c15de9fbfd527d9`**. The existing offline model revision,
runtime, embedding code and projection settings were retained. All **2,939**
map links resolve, and its embedded payload matches the artifact. Publication
changed nine expected files out of **6,479 protected existing files**; it
changed no biological records, curation inputs, IDs, record metadata or chemical
map. README statistics and the backlog now report **404** records with target
or resistance evidence. The sitemap is unchanged because its URLs are unchanged.

An additional adversarial check found two publication defects, documented in
the [map-wording review](2026-10-09-papulacandin-map-wording.json): the map's
fixed **86%** class-neighborhood claim was stale, and the claim that the model
had not been told the classes contradicted the embedded class field. A
diagnostic on this artifact measures **87.7101%** same-class neighbors in the
published rounded 2-D projection, **83.4025%** in the embeddings, and a
**22.6156%** random-other-record baseline. The dossier records distance metrics,
ten-neighbor/self-exclusion rules and artifact pins. These diagnostics are not
biological validation or a claim that projection quality improved.
The unbound numerical paragraph was removed from the map template, and the
harmonization document now explains the supplied class information. The
follow-up changes only the template, documentation, regression tests and map
page, preserving all biological and embedding artifacts. Its map-page checksum
supersedes the initial publication audit's page checksum, not its vector proof.

The initial focused suite finished with **115 passed and two failures** in new
test assertions about merged dictionary order. The normal seeder's no-op check
and byte-identical emission of the loaded record are now tested separately;
all **10 papulacandin tests pass**. This corrected a test assumption without
changing the emitter or reducing production gates. Full QC's first run was
deliberately interrupted after the map-wording findings, not treated as passed.
The clean authoritative rerun **passed all 11 gates**, with **2,181 passed,
3 skipped and one warning** in its test stage (**1,852.34 seconds**). The
three skips are empty command-frontmatter parameter sets, confirmed separately;
the warning is the existing `sssom_schema` LinkML dataclass-extension
deprecation. Both map-wording regression checks also pass. Strict validation
scanned **2,939 records with zero errors**; reproduction found **zero missing,
unexpected or drifted records and zero lockfile mismatches**. The chemical-map
check passed, and all **2,939 generated compound pages across seven classes**
match current inputs.

The [final verification manifest](2026-10-09-papulacandin-verification.json)
pins the terminal QC log, focused test results, current census and ledger,
curation and publication dossiers, and the separate map-wording correction.
Every current record hash was checked again. CUA reports no enabled browsers
or apps, so live visual inspection remains unavailable. These artifacts remain
local to the working branch: no commit, push, GitHub mutation or deployment
was performed. No NCBI endpoint was contacted. Passing the curation and
publication gates does not complete exact-allele or corpus-wide primary review.

### GM193663 Qualitative Curation (Previous Checkpoint)

Reinspection of the primary Methods and the Results section on diphthamide
synthesis in [Botet et al. (2008)](https://journals.asm.org/doi/10.1128/aac.01603-07)
supports five author-reported gene-level growth-resistance associations for
**GM193663**, **CHEBI:77908**, InChIKey **YIJXUKFDZCRZIC-MYOGCEHNSA-N**.
The DPH3 follow-up is distinguished from the principal screening collection.
The record now carries five curator-owned claims with species **NCBITaxon:4932**,
the primary citation **PMID:18285480**, and reference-only UniProt provenance:

| Source Gene | Reference Protein | Current UniProt Symbol |
| --- | --- | --- |
| DPH1 | P40487 | DPH1 |
| DPH2 | P32461 | DPH2 |
| DPH3 | Q3E840 | KTI11 |
| DPH4 | P47138 | JJJ3 |
| DPH5 | P32469 | DPH5 |

The [curation dossier](2026-10-09-gm193663-curation.json) pins the exact record,
canary, curation event, reference responses and cached taxonomy. The source
findings concern experimental laboratory subjects in a BY4741-derived
background, not resistance of the parent or species, and not prediction from
gene presence. The exported findings omit sequences, variant specifications,
constructs, protocols and numeric measurements. No structured tested-protein,
allele, strain, strain TaxID, assembly or BioSample assignment was added.
S288c **NCBITaxon:559292** describes the reference entries only.

This is a deliberately narrower decision than complete primary review:
explicit qualitative Results support these author-reported associations, while
figure panels and supplements have not been independently reanalyzed. Every
claim retains that limitation. The earlier hold remains for allele-specific or
quantitative curation, DPH6/DPH7, broader screen findings and other assay types.
Neither neutral sordarin nor the sodium-salt exposure from the 2013 study was
curated. `curation_status` remains `SEEDED`.

The [current ledger](2026-10-09-gm193663-resistance-grounding.tsv) retains all
**2,939 records**. Only GM193663 changes: its record hash, assertion count,
pending citation and status now reflect this curation; it remains
`PENDING_PRIMARY_REVIEW`. The reference-accession and lineage columns retain
their earlier PHI-base-only meaning, so these new non-PHI mappings are in the
linked dossier rather than silently broadening those columns.
The [reconciliation](2026-10-09-gm193663-checkpoint-reconciliation.json)
checks every current record path and hash against the fresh collection-aware
census. It finds **2,938 records byte-identical**, one added history event and
all other fields of the changed record preserved. An ignored-file-inclusive
manifest verifies **6,465 of 6,468 existing protected files unchanged**: only
GM193663 YAML, its rendered page and the site index differ. README statistics
were regenerated separately. This reconciliation predates the publication
refresh below; its old semantic-map pin remains historical. Earlier research
dossiers remain unchanged.

Verification: **99 focused tests passed**, including eleven new curation and
ledger tests, the publication-wording regression test and the semantic-map tests.
The two documentation-count tests also pass after correcting the backlog's
target-or-resistance coverage figure from 401 to 402. Strict validation passed
for **all 2,939 records**, and corpus reproduction reported **zero missing,
unexpected or drifted records**. The validated-writer canary and pre-render
replay passed.

### Semantic Map and Publication Refresh

The [publication audit](2026-10-09-gm193663-publication.json) records a genuine
incremental BGE refresh and complete PaCMAP projection, not a fingerprint-only
correction. The cached document baseline reconstructs exactly from commit
`d6c98be44bd706a2e31c8ebeea4de225decfc5a9`, including all 2,939 paths and the
original row order. **Five changed documents** were re-encoded with the cached
`BAAI/bge-large-en-v1.5` model; **2,934 unchanged vector rows remain
byte-identical**. Sixteen unchanged control documents were independently
re-encoded, matching within a maximum absolute float16 difference of
`0.000030517578125`. All vectors are finite and normalized.

The existing PaCMAP pipeline then projected the complete matrix with 15 neighbors
and seed 42. The published map contains **2,939 points** and current document
fingerprint **`8eb46854614f7c55`**. Record identifiers, labels, classes and normalized
coordinate bounds were checked. Semantic proximity describes record text; it
is not chemical similarity, allele homology or phenotype prediction.
The rendered map's embedded JSON exactly matches the artifact, and all 2,939
record links resolve. Live browser/pixel verification was not available: the
browser connector reported no enabled browser, and the active Python and Node
environments could not resolve Playwright. Static rendering and data checks do
not replace visual inspection.

This used an isolated Python 3.12 runtime without changing `pyproject.toml`,
`uv.lock`, the embedding scripts or the QC runner. A minimal Annoy probe
reproduced the one-neighbor behavior reported in
[the upstream issue](https://github.com/spotify/annoy/issues/682).
Rebuilding Annoy 1.17.3 with unsafe floating-point optimizations disabled via
its [documented compiler override](https://github.com/spotify/annoy/blob/v1.17.3/setup.py)
fixed that probe and allowed the existing projection to complete. Package,
compiler, model-revision and artifact pins are in the publication audit. Model
loading and inference were offline; no NCBI endpoint was contacted.

The shared record template now counts **source-backed resistance determinants
or associations**, rather than calling every entry a distinct known route.
All **298 affected record pages** match precisely that paragraph-only change.
The dedicated map page and three embedding artifacts account for the remaining
publication changes: **302 of 6,471 protected existing files changed**, with
**6,169 unchanged**. All **2,939 biological records** and all curation inputs are
unchanged during this publication step. The index is unchanged at this step.

The first full QC run finished with **2,164 passed, 3 skipped and 3 failed**
(2,238.21 seconds). Its failures were the two stale documentation-count checks
and the stale map fingerprint. The counts and map are now corrected, and the
focused checks pass. The authoritative full QC rerun completed successfully:
**2,170 tests passed, 3 skipped and 1 deprecation warning** (1,759.19 seconds
for the test stage), followed by successful strict schema validation, corpus
reproduction, chemical-map, generated-site and corpus-report gates. All eleven
QC stages passed. Strict validation found **zero errors across 2,939 records**;
reproduction found **zero missing, unexpected or drifted records**.
The [final verification manifest](2026-10-09-gm193663-verification.json) pins
both QC logs, the focused test results, current census and ledger, and the
curation/publication dossiers. It independently rechecks all 2,939 current
record paths and hashes. This verifies the curation and publication checkpoint,
not completion of corpus-wide primary review or experimental allele validation.
The three skips are empty command-frontmatter parameter sets, independently
confirmed with `tests/test_skill_frontmatter.py -q -rs` (38 passed, 3 skipped).
The warning comes from the existing LinkML dataclass extension in `sssom_schema`.

### Sordarin Compound Scope (Pre-Curation Checkpoint)

Methods inspection changes the appropriate destination of this literature lead:
[Botet et al. (2008)](https://journals.asm.org/doi/10.1128/aac.01603-07),
PMID:18285480, used the derivative **GM193663** in the growth screen and DPH
follow-up. That compound is **CHEBI:77908**, not neutral sordarin
**CHEBI:52549**. The separately described radioligand assay is not automatically
assigned the derivative's identity.

[Uthman et al. (2013)](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1003334)
explicitly used **sordarin sodium salt**. Its publisher XML was retrieved and
the methods, relevant Results, and Figure 3A caption inspected. That exposure
does not become a neutral-sordarin or GM193663 observation. An ignored-file-inclusive
name search in `data/antibiotics` and `curation` found no explicit sodium- or
potassium-sordarin name match; this is not an exhaustive structural-alias claim.

UniProtKB release **2026_03** grounds these reviewed reference identities:

| Paper Gene | UniProt Primary Symbol | Reference Protein | Reference Locus |
| --- | --- | --- | --- |
| DPH1 | DPH1 | P40487 | YIL103W |
| DPH2 | DPH2 | P32461 | YKL191W |
| DPH3 | KTI11 | Q3E840 | YBL071W-A |
| DPH4 | JJJ3 | P47138 | YJR097W |
| DPH5 | DPH5 | P32469 | YLR172C |
| DPH6 | DPH6 | Q12429 | YLR143W |
| DPH7 | RRT2 | P38332 | YBR246W |

These are reference-only mappings, not experimental allele assignments. The
[scope dossier](2026-10-09-sordarin-compound-scope.json) retains SGD identifiers,
entry and sequence versions, response pins, and the explicit synonym mappings.
Cached taxonomy separates experimental species **NCBITaxon:4932** from reference
S288c **NCBITaxon:559292**. BY4741-derived subjects receive no strain TaxID or
genome assignment. Other assay types and eEF2 comparison backgrounds remain separate.

The 2008 primary text supports qualitative leads, but publisher PDF retrieval
returned 403, the university archive redirect returned 404, and EMBL-EBI XML
retrieval returned 500. No figure panels or supplements were visually verified.
At this checkpoint, both studies retained explicit curation holds; the subsequent
GM193663 section above supersedes that hold only for text-supported qualitative
gene associations. No MIC, clinical category, sequence, variant specification or
experimental protocol was exported. All 2,939 records and 6,322 protected data,
curation and page files were unchanged at this pre-curation checkpoint.

Verification: **88 focused tests passed**, including 12 new compound-scope and
alias tests. Ruff, whitespace checks, byte-identical dossier replay, and an
independent comparison of all current record paths and hashes against the latest
corpus census passed. Full QC was not rerun; its earlier red result remains
authoritative. This checkpoint changes research metadata only.

### Cordycepin Reference Lead

The parent compound **CHEBI:29014** and its triphosphate metabolite
**CHEBI:52316** remain distinct. Neither record was changed.
[Holbein et al. (2009)](https://rnajournal.cshlp.org/content/15/5/837.full.pdf),
PMID:19324962, DOI:10.1261/rna.1458909, provides a qualitative ADO1/ADK1
growth-response lead in *Saccharomyces cerevisiae*. Indexed Results on printed
page 838 were inspected, but the figure panels and strain provenance were not
verified. Publisher and Europe PMC direct PDF requests both returned HTTP 403.
This is an incomplete primary review, not a new curated resistance assertion.

Sequence-free UniProtKB release **2026_03** metadata resolves two reviewed
reference entries:

| Gene | Reference Protein | Reference Locus | SGD | Entry / Sequence Version |
| --- | --- | --- | --- | --- |
| ADO1 | [P47143](https://www.uniprot.org/uniprotkb/P47143/entry) | YJR105W | S000003866 | 200 / 1 |
| ADK1 | [P07170](https://www.uniprot.org/uniprotkb/P07170/entry) | YDR226W | S000002634 | 237 / 2 |

ADO1 is adenosine kinase; ADK1 is adenylate kinase. Neither returned reference
entry cites the 2009 paper in this response, so these are gene-identity mappings,
not a citation-specific experimental protein crosswalk. Cached UniProt Taxonomy
supports species **NCBITaxon:4932** and reference S288c **NCBITaxon:559292**;
the latter is not assigned to a tested subject. No allele, genome, BioSample,
MIC, clinical category, or triphosphate exposure claim was inferred.

The [reference-lead dossier](2026-10-09-cordycepin-reference-lead.json) pins the
UniProt response and reused taxonomy caches, records the access limitations, and
preserves an explicit curation hold. An ignored-file-inclusive hash manifest
verified **6,322 existing data, curation, and page files unchanged**, including
all **2,939 records**. This metadata-only checkpoint does not supersede the
latest full-QC failure or the pending corpus-wide primary review.

Verification: **76 focused tests passed**, including seven new cordycepin
boundary tests. Repository test and helper Ruff checks, `git diff --check`, and
byte-identical offline dossier replay passed. The full QC suite was not rerun;
the earlier red full-QC checkpoint remains authoritative.

### Additional Yeast Primary Review

The TOM1 article/reference canary passed before retrieving the remaining two
primary studies and five focal reference entries. A separate HUL5 query followed
inspection of the negative-control result. All retrieval replayed offline from
the existing caches. The public dossier contains identity metadata and
qualitative interpretations, not sequences, variant specifications, constructs,
protocols or quantitative resistance measurements.

An independent parser checked the three primary XML responses, **nine Description
paragraph anchors**, three captions, all **26 source-qualified reagent rows**,
seven reference mappings from three complete UniProt queries, and two reused
taxonomy responses. The three inspected figures and the original strain-table
PDF/render are checksum-pinned. Local PDF rendering used PDFKit after Poppler
was unavailable. These checks verify source identity and preservation, not
automatic correctness of biological interpretation.

The verifier checked every current record path/hash, with ignored files included,
and **6,462 protected files**, plus the previous discovery checkpoint and its
new artifacts. The counts overlap. All **2,939 biological records** remain unchanged;
the five existing hygromycin B CARD assertions and all PHI-base decisions are preserved.

The **413 distinct metadata/research tests passed in 16.08 seconds**, with no
failures, errors or skips. This includes 16 new tests; the earlier 16-case run
overlaps the total. JUnit results are in
`reports/resistance-grounding-2026-10-07/hygromycin-additional-primary-tests.xml`,
SHA-256 `aee8b849ecd2b7f3bda9b2f5edb7c06f08bb494bb03a72369ab6fa08e742406a`.
The dossier SHA-256 is
`637418925374bfda1893854750b1dbcd1112248856b549b05afc582b3cc0aeaf`;
the independent verifier SHA-256 is
`357d483816bdb0001ef1fc32e7467f7686c22af0b3624e8ab1de0ed5a012b669`.
Its frozen proof is
`reports/resistance-grounding-2026-10-07/hygromycin-additional-20261009/independent-proof.json`.

No NCBI endpoint, outreach, source adoption or GitHub mutation was used.
Full authoritative QC was not rerun. The latest curation checkpoint remains
**not QC-green** because the semantic text map still needs a genuine rebuild.

### Date-Sorted Retrieval (Latest Discovery)

An independent parser verified all **99 new raw cached responses**, including
the two canary orders, against their request parameters, endpoint, echoed
query/cursor/sort, API version, page lengths, counts and checksums. It checked
for cross-page duplicate identities and reconstructed the eight-field citation
projection without importing the retrieval implementation. All five new chains
passed. The lossless gzip export has a deterministic header and checksum.
The parser also checked **6,462 protected files** and every current record
path/hash, with ignored files included. These overlapping preservation counts
are not additive. No biological or rendered files changed.

The **397 distinct metadata/discovery tests passed in 22.27 seconds**, with no
failures, errors or skips. This includes the 12 new date-sort cases; the earlier
12-case run overlaps this total. JUnit results are in
`reports/resistance-grounding-2026-10-07/date-sort-metadata-tests.xml`, SHA-256
`5d3b00930071ace7bfa3829c5b44e1e288c15e7363128cde4684ffb62a4d94d9`.
The checkpoint descriptor SHA-256 is
`e3e545520420d8109c8b0bd2ac07ea8c3c248ab5c829b29ba1eb2a2112436846`;
the independent verifier SHA-256 is
`215e70f29ef48c6a46f4644c69949e4e4a1cfadd67e7b1cc6b82133e6b494b7e`.
The frozen proof is
`reports/resistance-grounding-2026-10-07/expansion-date-sort-20261009/date-sort-independent-proof.json`.
Offline producer replay reproduced all six canary/batch chains with zero fresh
responses, and independent replay reproduced the public artifacts and frozen
proof byte-for-byte. Repository Ruff, `git diff --check`, and explicit whitespace
checks of the new untracked text artifacts passed.

This metadata-only checkpoint does not replace the latest curation validation
below. Full authoritative QC was not rerun and is **not green**: the semantic
text map still requires a genuine rebuild. No NCBI request, outreach, source
adoption or GitHub mutation occurred.

### SDH8 Reference Alias (Latest Curation)

The guarded canary passed readback and the three Huang tests. The combined
SDH8/Huang suite then passed **12 tests in 3.20 seconds**; these runs overlap.
Repeated curation made no writes or history events. The independent
pre-publication verifier reconstructed the one note correction and 183
checksum-only updates without importing the production review transformer.
It checked **6,436 other protected files** and all 2,939 record paths/hashes,
with ignored files included. Its frozen proof is
`sdh8-alias-prepublication-proof.json`; the dossier SHA-256 is
`e9500844909e483eb0c6784fe58d307de1674f722c7c10ff6b608885f0d74e7c`.

After rendering, the [checkpoint reconciliation](2026-10-09-sdh8-checkpoint-reconciliation.json)
verified **24 changed HTML files**, two replaced complete-record downloads,
**116 preserved historical research artifacts** and **6,410 protected files**.
The counts overlap and are not additive. Activity/membership/search datasets,
index and sitemap are unchanged. The corrected fluconazole row keeps reference
identifiers in provenance, not experimental-subject cells. All 22 changed records
produce unchanged semantic-embedding input text; the existing map was not edited.
The [new full-corpus ledger](2026-10-09-sdh8-resistance-grounding.tsv) binds all
2,939 current record hashes while earlier ledgers retain their historical pins.

The reconciliation SHA-256 is
`f2e69a1829ef7c3d5817a5fe2c65f7350ffe805c5249102a5f7cfe6fafc09ba5`.
The frozen pre-publication verifier is
`63d9b5c332da25aedba77000c78e42410fea5a9d33f2c0360dfd0923a19f3e24`;
the publication reconciliation verifier is
`80aa2502f21ed41fb1450faf342c24457475f571f973e8321fad1d290b6cc202`.
Proofs and logs are in `reports/resistance-grounding-2026-10-07/`.
All **11 downstream stages passed**: strict validation of all 2,939 files,
exact corpus reproduction, rendering freshness, checkpoint reconciliation,
documentation statistics, raw provenance, source queue, chemical-map freshness,
corpus report, Ruff and whitespace checks. The log `sdh8-offline-checks.log`
has SHA-256 `3b7eb596bcf606308619d2e59c1b256904c255309071ef73d88ea1331ba39008`.
Publication reconciliation replayed again without changing its frozen proof.

The initial broad curation suite had **343 passes and two failures**: two
assertions still expected the historical unresolved SDH8 alias wording.
They now require the explicit reference crosswalk while retaining the ban on
experimental allele assignments. The corrected assertions with SDH8/Huang
coverage passed **14 tests in 4.41 seconds**; this overlaps the earlier 12 tests.
The original failure log is preserved as `sdh8-focused-checks.log`, SHA-256
`a1b58d3ca02acb9695664ab62e4123c2306cf50f4583883e46c9979095d7c969`.
The broader focused recheck passed **345 curation/publication tests in 518.98
seconds** and **385 metadata/discovery tests in 12.77 seconds**. Parsed JUnit XML
confirms **730 distinct cases**, with no failures, errors or skips; the earlier
14 cases overlap this total. The recheck log SHA-256 is
`73807d98d4f058423d1f40866b35462f9f0e9deb8db7610e4c5d7037a8860364`.
The curation XML SHA-256 is
`5d54cb52d779ad8bbb97fd84c76cdb13bb4f3636ca02d00d4560cdeee9ae6456`;
the metadata XML SHA-256 is
`b55b2deb87975c138bc267c79d585aa69ed9132e892ccc3828a1dd57f5e9a5a7`.

Authoritative QC completed with **2,108 passed, three skipped, three failed and
one warning**, in 2,044.55 seconds for pytest (2,123.57 seconds for the runner).
It passed the lint, documentation, provenance, source-queue and curator-structure
stages, then stopped at tests. The downstream stages were independently checked
above; that does not turn the authoritative run green.

The failures were the existing semantic-map freshness assertion and the two
pre-correction SDH8 assertions in `test_phibase_grounding_reviews.py`. This
process collected the old tests before the corrections, so its result is not
a post-correction full run. Both repaired assertions pass in the 730-case
focused recheck; those cases overlap the full suite. The remaining known defect
is the unchanged map fingerprint `089fe6e5f5af1d42` versus current document
fingerprint `a132d1276c49dc07`. The SDH8 curation leaves embedding input text
unchanged, and neither the map nor its fingerprint was patched. A genuine
embedding/map rebuild is still needed. The warning is the existing LinkML
dataclass-extension deprecation.

The full log `sdh8-qc-checks.log` has SHA-256
`55ff707897a2be6afb2ea88bdb9b364339ffef110df8266f029a68bf0e5fa6e4`.
**This checkpoint is not QC-green**, and no post-correction full-QC pass is
claimed. No GitHub mutation or NCBI request occurred.

The current source-owned review SHA-256 is
`47e4c1aba10bd711a318ffbc0ff5a66cd94acedb9e9967194688f66a421f08c9`;
the current ledger SHA-256 is
`cf5908cc0a3e8447f8239fcb354977cc90294c7f950b7f40d9fe15ef3a9cc99a`;
the current census SHA-256 is
`659b758cba122d3b571f55fb26ad4f61473ce4a4ba81fbceb015c89fd65fdcaf`.

### rplD Reference Identity (Historical)

The metadata/discovery suite passed **385 tests in 22.58 seconds**, including
the **10 new rplD cases**. The earlier 10-test run overlaps this total.
Tests cover exact query scope, separate loci and citation-specific strain
contexts, the retained ontology conflict, metadata-only export, source-owned
claim preservation, and the distinction between identity and resistance review.
Results are in `reports/resistance-grounding-2026-10-07/rpld-metadata-tests.xml`.
Repository Ruff, documentation-statistics freshness and `git diff --check`
passed. The new untracked dossier and test file also passed explicit whitespace
and ASCII checks; the XML contains 385 distinct test cases with no failures.

Offline replay reproduced the dossier byte-for-byte. A separate verifier
compared both complete UniProt query responses, both projected protein entries,
their citation-specific strain annotations, and strain taxonomy against the
cached responses. It checked the publisher paragraph digest and every source
pin, then verified **all 2,939 current record hashes and 6,458 protected files**,
including the earlier research artifacts. Record-path enumeration includes
ignored files. These counts overlap and are not additive. No biological record,
curation history, source inventory, source queue or rendered page changed.

The dossier SHA-256 is
`803fb2091d65211f9e399c5a9e28899afa42c34af96484585229428f0fc2b56c`.
The cached proof `rpld-reference-independent-proof.json` pins the generator
`776aee148a423541ee7d4b185c516d9536c69024a15491834fd3daa94c1bf7fb`
and independent verifier
`0afe644945032a0692d63376c364566f92811ec8e488402233a9cadf3f832bfd`.
All source responses and the proof are under
`reports/resistance-grounding-2026-10-07/`; they replay without network access.

This metadata-only checkpoint does **not** rerun authoritative full QC or
declare it green. The latest full run remains the fenpicoxamid checkpoint
below, with the pre-existing stale semantic-map failure. The latest biological
curation remains that checkpoint as well: **184/217 PHI-base associations
identifier-scoped**, with **33 across 14 papers pending**. The rplD identity
finding does not change those counts or complete primary resistance review.

### Fenpicoxamid Subject Context (Historical)

The guarded canary and subsequent source-owned update retain both original
associations. All **19 focused tests** passed, including fail-closed background
withholding, source drift, source-row separation and dossier scope. The earlier
17- and 18-test runs overlap this total. A repeated curation run made no writes
or history events. The **336-test curation/publication suite** passed in 454.67
seconds, including those 19 tests, and the separate **375-test metadata/discovery
suite** passed in 14.44 seconds: **711 distinct focused tests** in total.
Strict schema validation found zero errors across **2,939 records**. Corpus
reproduction found zero missing, unexpected or drifted records. Render freshness,
documentation statistics, raw-data provenance, source-queue checks, the current
structure-only chemical map, the corpus report, repository Ruff and
`git diff --check` all passed. All **12 offline checkpoint stages** completed.

The authoritative `scripts/run_qc.py` run completed its test stage with
**2,091 passed, three skipped, one failed and one warning in 1,899.76 seconds**.
It used the inspected temporary Python 3.13.16 runtime with the pinned RDKit
`2026.03.5`; repository dependency pins were not changed. Full QC is **not
green**: its only failure is
`tests/test_embeddings.py::test_the_committed_map_is_not_stale_against_the_corpus`.
The stored semantic-map fingerprint remains `089fe6e5f5af1d42`, while the current
document fingerprint is `a132d1276c49dc07`, the same pre-existing mismatch
reported before this curation. The previous documentation-count failure did
not recur. The warning concerns the deprecated LinkML dataclass extension.
The runner stopped at the failed test stage; downstream gates were exercised
separately by the successful offline stages above, not bypassed within QC.
The full log is `fouche-authoritative-qc.log`; focused test results are in
`fouche-curation-tests.xml` and `fouche-metadata-tests.xml`. Their cases overlap
the full run and must not be added to its totals.

Before publication, the independent verifier reconstructed the two scope edits
and **182 checksum-only claim updates** without importing the production review
transformation. Exactly **22 records** changed, each with one appended history
event; **2,917 records** were byte-identical. It checked 6,408 other protected
files at that pre-publication stage. The dossier SHA-256 is
`949c9c84dd2d2679b39df9f4bc32dd6f9c257820c8daa36402073662e86b2ff0`;
`fouche-context-proof.json` pins the frozen pre-publication verifier
`e769bd3d431c6ae67d1e222e23d311aa188468dc3cc906b7071bcbd9b8d1b710`.

After rendering, the independent reconciliation checked **24 changed HTML
files**: 22 record pages and the two activity pages whose full-record download
links changed. Exactly two content-addressed complete-record downloads were
replaced; both decode to the current records, and their previous hashes were
independently reproduced from the frozen pre-curation records. Activity,
membership and search datasets, HTML page paths, index and sitemap are unchanged.
The fenpicoxamid table retains two rows and species context, with background
labels and reference protein confined to provenance rather than subject cells.

The reconciliation verifies **112 earlier research artifacts**, **20,122
earlier protected files**, and **6,406 post-publication protected files** with
ignored files included. These inventories overlap and are not additive.
It binds all 2,939 current record hashes to a new census and ledger while leaving
earlier audit snapshots unchanged. All 22 changed records generate identical
semantic-embedding input text to their pre-curation versions; no map artifact
was rewritten. The reconciliation SHA-256 is
`0326863f0a8f100853cefa3527569e4998441a3407f79f48406cebccda31acfc`;
`fouche-reconciliation-proof.json` pins its independent verifier
`eec0947bcf17960a69eea2708abb1adff3508c711fd613764acde1bae8ff5a48`.
Both proofs and check logs are in `reports/resistance-grounding-2026-10-07/`.

Identifier-scope review is **184/217**, with **33 associations across 14 papers
pending**. The manuscript is cached for review, not re-exported or adopted as
a bulk source. No new sequences, variants, numeric measurements or genomes
were added, and no NCBI request, outreach, reuse-terms review or GitHub mutation
occurred. The corpus-wide investigation remains incomplete.

### CARD Named Taxa (Historical)

The metadata/discovery suite passed **375 tests in 18.14 seconds**, including
**45 new cases** for exact name/synonym matching, ambiguous and missing matches,
rank/activity checks, malformed responses, duplicate IDs, incomplete searches,
source-label drift, the protein/RNA conflict and public-export preservation.
The earlier focused 37- and 39-test runs overlap this total and preceded the
last six malformed-field cases. Results are in `card-named-taxa-audit-tests.xml`
under `reports/resistance-grounding-2026-10-07/`.

The independent verifier reconstructed all **34 name searches** from raw cached
responses, all **88 term projections** and **107 assertion memberships**, and
checked the conflict definition and named ancestry witnesses in the pinned RDF.
It verified **20,145 protected file digests**, all **2,939 current record hashes**,
and the complete record-path set with ignored files included. The previous
term-scope audit and hygromycin follow-up are byte-identical. This checks name
metadata and preservation, not primary experimental identity or causality.

The export SHA-256 is
`9aec094dbd14d5e6b913477e1bee57acec8c5b5fd672c16dde5a513a282e2b91`.
The proof is `card-named-taxa-independent-proof.json`; it pins the generator and
the frozen independent verifier
`f2971ea31ecc13a7bce1767c4b202b0bea629ba745342996ac496697c207617d`.
Production replay reproduced the export byte-for-byte, offline:

```bash
.venv/bin/python scripts/audit_card_named_taxa.py \
  --output research/2026-10-09-card-named-taxa.json
```

Adversarial review caught the earlier prose's overinterpretation of RNA
ancestry. The report now distinguishes 87 RNA labels from the protein-definition
conflict without changing the pinned ancestry artifact or source assertions.
Additional checks reject malformed taxonomy names/status fields and input/cache
drift. Repository Ruff, documentation statistics, `git diff --check`, and explicit
whitespace checks for all four new or updated public files passed. Species-name
matches alone did not meet the biological curation threshold.
No biological record, source inventory, generated page or history event changed;
PHI-base identifier scope remains **182/217**, with **35 associations across
15 papers pending**. New taxonomy requests went only to UniProt. No source
adoption, outreach, restricted CARD download or GitHub mutation occurred.
Full QC was not rerun and the semantic-map mismatch remains unresolved. The
all-record investigation is not complete.

### CARD Term Scope (Historical)

The metadata/discovery suite passed **330 tests in 21.64 seconds**, including
**23 new cases** for ontology parsing, scope classification, input integrity and
the public export. The focused 23-test run overlaps this total. Results are in
`card-term-scope-audit-tests.xml` under `reports/resistance-grounding-2026-10-07/`.
The canary was inspected before the full export. RDF statements split across
class declarations and descriptions are resolved through RDFLib; restrictions
are kept separate from named subclass ancestry.

Independent verification reconstructed all **2,002 term classifications** from
the pinned RDF graph, checked every ancestry witness and its shortest-path
length, reconciled all **4,555 source edges** and **4,538 current assertion
memberships**, and retained all reference candidates. It verified **20,145
protected file digests**, all **2,939 current record hashes**, and the exact
record-path set with ignored files included. The preceding hygromycin dossier
also remains byte-identical. These are ontology and preservation checks, not
completed primary-paper or experimental-allele validation.

The export SHA-256 is
`4de3f3c046e5f6822d0ed738906baf20089c712edaf493e32fff5551af040acd`.
The proof is `card-term-scope-independent-proof.json`, which pins both the
generator and independent verifier. Production replay reproduced the export
byte-for-byte and refuses to replace a different existing audit.
With the captured cache, the offline replay command is:

```bash
.venv/bin/python scripts/audit_card_term_scope.py \
  --ontology-cache reports/resistance-grounding-2026-10-07/aro-term-scope-aro.owl-0225daaf01b1336fc6e866989b4835b89afa40d8.json \
  --output research/2026-10-09-card-term-scope.json
```

Repository Ruff and documentation-statistics checks passed. No biological
record, source inventory, reference taxonomy, generated page or curation event
changed. No NCBI request, outreach, restricted CARD download, source adoption
or GitHub mutation occurred. Full QC was not rerun; the known semantic-map
mismatch remains unresolved. PHI-base identifier scope remains **182/217**,
with 35 associations across 15 papers pending. The full-corpus investigation
is still incomplete.

### Hygromycin Discordance (Historical)

The metadata/discovery suite passed **307 tests in 29.08 seconds**, including
**nine new cases** for the qualitative follow-up. The focused nine-test run
overlaps this total. Results are in `hygromycin-discordance-audit-tests.xml`
under `reports/resistance-grounding-2026-10-07/`.

Independent metadata checks reconciled five cached responses: one containing
both reference proteins, two taxonomy responses, the later paper's JATS, and
the failed direct author-copy fetch. The latter is failure evidence, not cached
primary text. The checker verified **20,145 protected file digests**, including
all **2,939 record hashes** and the exact record-path set with ignored files
included. These checks do not independently validate the manual scientific
interpretation or substitute for the outstanding older-figure inspection.

The dossier SHA-256 is
`7239211b2cfdd81ad68c8aa7fc90f0d0a9eeaeb18e0d7d0f2c8dc70cc1735583`.
The proof is `hygromycin-discordance-independent-proof.json`; it pins the
verifier and preserved-file manifest and replayed byte-identically. Historical dossiers and failed access
responses remain unchanged. No biological record or curation event changed;
canonical reference proteins were not assigned to experimental alleles.

Repository Ruff and documentation-statistics checks passed. Full QC was not
rerun; the known semantic-map mismatch
remains unresolved. PHI-base identifier scope remains **182/217**, with 35
associations across 15 papers pending. The corpus-wide investigation is still
incomplete. No NCBI request, outreach, source adoption or GitHub mutation occurred.

### Query-Local Retrieval (Historical)

The metadata/discovery suite passed **298 tests in 12.74 seconds**, including
**15 new cases**: seven scheduler/bound/resume cases and eight public-export
cases. The preceding 119-test discovery and 290-test pre-export runs overlap
this total; they are not additional distinct tests. The final JUnit result is
`query-local-audit-tests.xml` under `reports/resistance-grounding-2026-10-07/`.

Independent replay reconstructed **1,044 raw expansion responses**: 704 pages
from completed parent chains, three from the complete default-order canary,
and 337 fresh responses. It checked query echoes, cursor handoffs, counts,
versions, overlaps, rejection reasons, every candidate projection, all 612
ledger memberships, and the observed order of all 72 fresh query chains.
It verified **20,145 protected file digests**, including **2,939 current record
hashes** and the exact record-path set with ignored files included.
Both earlier retrieval cohorts remain unchanged.

The descriptor SHA-256 is
`45596e2d5842620ddca8f66f39dc477491635d02b0e10239597a0de5810a098a`.
Its 73-query delta compresses 130,446,197 exact JSON bytes to 24,355,547 bytes,
with separate stored and expanded digests. The frozen proof is
`expansion-query-local-20261009/query-local-independent-proof.json`.
Replaying the independent checker reproduces all new exports byte-for-byte.
These are metadata and preservation checks, not completed primary-paper review.

Repository Ruff, documentation statistics and source-queue checks passed.
No biological record, generated page, source adoption, GitHub state or curation
event changed. No NCBI request or outreach occurred. Full QC was not rerun;
the known semantic-map mismatch remains unresolved. PHI-base identifier scope
remains **182/217**, with 35 associations across 15 papers pending, and the
broader corpus-wide gene/allele investigation is still incomplete.

### Retrieval Restart and Archive IDs (Historical)

The metadata/discovery suite passed **283 tests in 10.84 seconds**, including
**28 new cases**: 15 archive-projection/stage cases, four archive-export cases
and nine retrieval-restart cases. The 79-test archive-focused and 112-test
discovery runs overlap this total; they are not additional distinct tests.
JUnit reports are `restart-and-archive-audit-tests.xml`,
`card-archive-regression-tests.xml` and `expansion-restart-regression-tests.xml`
under `reports/resistance-grounding-2026-10-07/`.

Independent reconstruction verified **869 expansion responses** (660 retained
historical pages and 209 fresh responses including the first canary), plus the
six separate ordering-canary responses. It checked query echoes, cursor
handoffs, counts, versions, duplicate identities, rejection reasons, all 612
ledger memberships and **11,791 protected file digests**, including all
**2,939 current records** and their exact paths with ignored files included.
The original 7,466 name-query caches and 886 expansion responses remain
unchanged. Both valid-prefix histories remain accessible; the selected index
and historical/retry union are explicitly different evidence views.

The retrieval descriptor SHA-256 is
`86a041f3208d80b447a166d7b05137ece1bb253504256ad741e538a104ad6934`.
Its 91-query delta compresses 55,548,318 JSON bytes to 10,468,778 bytes, with
both digests recorded. The proof is
`expansion-restart-20261009/restart-independent-proof.json`. Frozen publication
refuses to overwrite a different existing export. The batch recovered 18
traversals but left 73 conflicted; the separately complete amikacin canaries
were not silently substituted into its batch chain or counted as primary review.

The independent archive verifier reconstructed all 4,182 cached protein entries
from nine responses and checked every retained candidate's archive ID, versions
and reference TaxID. Its 979 candidates form 977 archive groups; both shared-ID
pairs remain separate entries with their existing annotations. The export is
257,950 bytes, SHA-256
`0275d0944d18f8a95ad57efb2b6bf73eb998baa27eda719350c650dcf30e8496`.
Production replay is byte-identical; `card-archive-independent-proof.json`
verifies 3,428 protected files and all record hashes.

Repository Ruff, documentation statistics and source-queue checks passed.
No biological claim, curation event, generated page, source adoption or GitHub
state changed. No NCBI request or outreach occurred. Full QC was not rerun;
the known semantic-map mismatch and corpus-wide primary/allele review backlog
remain unresolved. PHI-base identifier scope remains **182/217**, with 35
associations across 15 papers pending.

### LmrC Primary Context (Historical)

The new qualitative dossier preserves all **2,939 record hashes** and
**3,428 protected file digests**, including the candidate audit, citation-context
index, source inventories, PHI-base decisions, source queue and semantic map.
The exact record-path set was checked with ignored files included. Its SHA-256
is `195350c4637194c8586c25a2b8c5d119aca9e41ab859086a54e9b5a8af26152d`
(14,596 bytes). The exporter refuses to replace an existing different output.

An independent checker reconciles all nine cached protein responses, the two
candidate projections, three taxonomy projections, citation metadata, PDF and
page-image digests, and the three source-assertion memberships. It checks
**13 JSON responses** and confirms all **12 referenced cache files** are
gitignored. The current proof is `lmrc-context-independent-proof-v2.json`;
the earlier proof is retained separately after a helper-only line-length fix.
These are metadata and preservation checks, not a second scientific review.

The broader metadata/discovery suite passed **255 tests in 6.85 seconds**,
including **11 new cases** covering native versus host context, citation-specific
strain annotations, shared archive-ID limits, taxonomic rank, compound scope
and unchanged source assertions. The focused 11-test run passed in 0.25 seconds
and is included in that total, not additional coverage. JUnit results are
`lmrc-context-tests.xml` and `lmrc-context-audit-tests.xml`. Exporter replay is
byte-identical. Repository Ruff, explicit whitespace checks, documentation
statistics and the source-queue check passed.
No biological curation event was added, and the PHI-base scope count remains
**182/217**. Full QC was not rerun; the previously identified semantic-map
mismatch and corpus-wide review backlog
remain open. No NCBI request, outreach, source adoption or GitHub mutation
occurred.

### CARD Citation Context (Historical)

The broader metadata/discovery suite passed **244 tests in 5.64 seconds**,
including **28 new cases** covering the context extractor and its public export.
The focused 49-test run is included in that total, not additional coverage.
The JUnit results are `card-context-audit-tests.xml` and
`card-context-regression-tests.xml` under `reports/resistance-grounding-2026-10-07/`.

The independent verifier reconstructed every retained context directly from
the nine checksum-verified UniProt responses, without calling the production
extractor. It reconciled all **1,686 contexts on 979 proteins**, their
source-assertion memberships, citation-specific strain annotations and evidence
pointers. It also verified **3,426 protected file digests**, including all
**2,939 record hashes** and the exact record-path set with ignored files included.
The candidate audit, assertion ledger, source inventory, PHI-base decisions,
source queue, semantic map and cached responses are unchanged.

A manually inspected Q461P1 canary preceded the full offline export. Replay
is byte-identical: **2,019,148 bytes**, SHA-256
`2bf1c102685080c1a130af31be4cf9a8c9d81c64bf7b2774bf9fd0afa19bd07e`.
The local proof is `card-context-independent-proof.json`; the protected-input
manifest is `card-context-before.json`. These checks validate database metadata
and preservation, not biological interpretation or primary-paper Results.
No experimental identifier, biological claim or curation event was added.

Repository Ruff and whitespace checks passed. No new UniProt or NCBI endpoint
request, restricted bulk retrieval, source adoption or GitHub mutation occurred
for this export. Earlier bounded primary-access searches in this checkpoint
did not resolve the remaining PHI-base subjects, whose review count stays
**182/217**, with **35 associations across 15 papers pending**. Full QC was not
rerun for this metadata-only change; the previously reported semantic-map
mismatch and broader primary-review backlog remain unresolved.

### Nguyen Reference Lead (Historical)

The metadata/discovery audit suite passed **216 tests in 9.54 seconds**,
including **eight new lead-specific tests** and the existing 208 cases.
These overlap the preceding checkpoint, not 216 additional distinct tests.
The JUnit result is `nguyen-audit-tests.xml` under
`reports/resistance-grounding-2026-10-07/`.

The frozen lead SHA-256 is
`c6e6569d383ed7aee7d4b0456f904472dabf821ad580ff3b9a59b8210c3f85f2`.
Replaying its verifier is byte-identical. A separate checker, without importing
the generator, verifies **2,947 protected files**, including all **2,939
record hashes** and the exact record-path set with ignored files included.
Source inventory, review decisions, queue, semantic map and census remain
unchanged. Six cached responses have matching metadata and body digests;
the PDF, extracted text and three visually inspected page images are pinned.
All 14 referenced local cache files are confirmed gitignored. The local proofs
are `nguyen-reference-lead-proof.json` and
`nguyen-reference-independent-proof.json`; these replay evidence and preservation,
not an independent scientific interpretation.

Repository Ruff, the separate checker lint, whitespace and documentation
statistics checks passed. No biological record, generated page, curation event
or review count changed. Full QC was not rerun for this metadata-only addition;
the previously reported semantic-map mismatch remains unresolved. No NCBI
request, outreach, source adoption or GitHub mutation occurred.

### HDF1 Subject Correction (Historical)

The curation/publication suite passed **317 tests in 462.55 seconds**;
the disjoint discovery/audit suite passed **208 tests in 12.27 seconds**:
**525 distinct tests total**, including four new HDF1 cases. The initial run
had two stale regression expectations and 315 passes; the missing HDF1 branch
and reviewed-claim counts were corrected, then the complete suite was rerun.
The original failure log is retained as `hdf1-checkpoint.log`; the successful
35-stage run is `hdf1-checkpoint-corrected.log`, both under
`reports/resistance-grounding-2026-10-07/`.

Canary-before-bulk curation used the validated writer and curation-event helper.
Replay made **no writes or history events**. Independent reconstruction checks
all **2,939 record hashes**: one new identifier-scope correction, **181
checksum-only claim updates**, **21 changed record files**, and **2,918
byte-identical records**. Each changed record has one new event; earlier history,
other-source assertions, source alteration/phenotype/assay fields, activities
and clinical-status assertions are preserved. The source inventory and source
queue are unchanged. The metadata-only dossier SHA-256 is
`f9abf4b33f459b233abe55fd002805bc21a8b7a09d729f259c0970181c920211`.
The independent proof is `hdf1-context-proof.json` in the same local directory.
It checks cached primary PDF, text and rendered-page digests, citation metadata,
four UniProt responses and the deliberately unresolved locus alias. Automated
replay verifies the cached locations; it does not repeat scientific interpretation.

The independent `hdf1-discovery-refresh-proof.json` checks **18 archived research
exports plus the separately preserved census**, all current record hashes,
**886 unchanged expansion responses**, identical candidates and statuses for
**611 queries**, and a byte-identical expansion ledger. Only **27 record-hash
memberships across 18 records** and their parent checksum bindings changed.
All **7,466 original citation-cache files** remain unchanged. Earlier dossiers
retain their historical scope. The current census SHA-256 is
`ba828f06017d67183a8335e2933656b9970ac13ce57e764f518a92faccac8610`.

**All 35 offline checkpoint stages passed.** Strict validation covered 2,939
records with zero errors; the corpus reproduces exactly from source-owned
inputs. Documentation statistics, raw-data provenance, source queue, repository
and helper Ruff, whitespace and render-consistency checks passed. The published
hydrogen-peroxide table retains all six claims, displays YM1 as subject, and
keeps PH-1 reference accessions outside the subject cell. The unresolved-alias
warning, zero activities and one clinical-status assertion are preserved.
Rendering pruned two stale managed outputs; no tracked files were deleted.

The prior blanket RDKit limitation is **superseded**. An existing temporary
conda runtime supplies Python 3.13.16 and RDKit **2026.03.5**, equivalent to the
repository's `2026.3.5` pin. Eight exact locked scientific wheels were installed
only in a new temporary directory, with repository dependencies layered read-only.
The project environment, `pyproject.toml`, `uv.lock`, QC runner and embedding
artifacts were not modified. Version/origin checks and the curator-structure
gate passed. The separate **chemical-structure map check passed for all 2,939
records**. Projection generation was not tested: the locked `numba==0.67.0`
has no usable wheel in this environment, and an earlier unconstrained transitive
`llvmlite` build failed for missing LLVM. No dependency pin was relaxed.

**Full QC has not passed.** The combined chemistry/embedding subset had **24
passes and one failure in 303.09 seconds**: the existing semantic corpus map
still records fingerprint `089fe6e5f5af1d42`, while current embedded documents
hash to `a132d1276c49dc07`. Both stored vectors' metadata and the semantic map
carry the old fingerprint. `hdf1-embedding-scope-proof.json` independently
verifies that this HDF1 checkpoint changes **none of the embedded documents**;
the mismatch predates this checkpoint, not necessarily the broader research
branch. No fingerprint-only patch or projection substitution was made.
The BGE model files are present in the local cache, but the project, system Python and five existing
temporary embedding environments checked lack the text-embedding stack.
The existing BGE/PaCMAP pipeline needs a genuine rebuild in a compatible runtime.

The authoritative `scripts/run_qc.py` run completed with **1,904 passed, three
skipped and two failed tests in 1,749.87 seconds**; the runner exited 1 after
1,812.18 seconds. Its first five gates passed, then it stopped at the test gate.
The complete log is `hdf1-authoritative-qc.log`. Besides semantic-map staleness,
it found a stale **399-record** target-or-resistance-evidence count in
`NEXT_TASKS.md`. That count is now **401**, derived from the current corpus and
registered against its own metric in `tests/test_docs.py`, not merely accepted
because it equals some other corpus quantity. The backlog's outdated direction
to proceed with NCBI AST was also replaced with the existing explicit deferral;
source status and historical verification date remain unchanged.

After these documentation corrections, **28 focused tests passed in 91.27
seconds**, covering both numeric-claim guards and the source-queue/deferral
assertions; these overlap earlier counts and are not additional distinct tests.
The JUnit result is `hdf1-docs-followup.xml`. The full suite was not rerun after
this documentation-only correction; the known remaining failure is the stale
semantic map. Post-suite verification again confirms all 2,939 record hashes,
the exact record-path set including ignored files, the unchanged source queue,
and the published subject/reference distinction. No scientific record was
changed by the documentation fix, and no full-QC pass is claimed.

Identifier-scope review is **182/217**, with **35 associations across 15 papers
pending**. Exact experimental accessions, unresolved aliases, phenotype
validation and corpus-wide primary review remain open. No NCBI endpoint request,
outreach, reuse clarification, source adoption or GitHub mutation occurred.

### DKAG124 Metadata Follow-Up (Historical)

**208 tests passed in 8.52 seconds**: 11 new metadata-grounding regression
cases plus the existing 197 discovery/audit tests. This overlaps the preceding
Huang coverage and is not an additional 208 distinct corpus tests.
The JUnit result is `reports/resistance-grounding-2026-10-07/dkag124-tests.xml`.

The native XML audit verifies Table S1's DOCX-to-XLSX relationship, worksheet
identity, headers, identifier cell range, absence of formulas in those cells,
uniqueness and project counts. An independent **openpyxl** read reproduces all
87 tuples, preserving numeric-looking labels as strings and case. No visual
worksheet or figure review is claimed. Four cache files and their response
bodies are checksum-verified, including the primary HTML and three UniProt
responses. The original HTML cache remains unchanged; its Latin-1 decoding is
reversed to recover bytes before parsing the declared UTF-8 encoding.

The collection-aware audit reloads all **2,939 records** and **26 membership
collections**, with zero exact matches to these BioSample IDs. File enumeration
includes ignored and hidden files within `data/antibiotics`; this is not a
search of every raw dataset or research file and does not establish biological
non-overlap. Independent verification preserves **2,989 protected files**,
including every record and corpus artifact, **18 existing research exports**,
the census, source inventory, review decisions and source queue. No corpus
artifact was added or removed, and no curation event was added.

The dossier SHA-256 is
`bacce3929557d76e9735d4416832d3a3306caa2e74d79dea423e3536d27e8b81`.
The local proofs are `dkag124-metadata-proof.json` and
`dkag124-independent-proof.json` in the same report directory. Restricted
source caches and extracted identifier rows are confirmed gitignored. Prior
biological-curation results below retain their original scope; full QC had
not passed at this checkpoint because of the then-unresolved RDKit environment.
Documentation statistics, raw-data provenance, source-queue validation,
repository Ruff, the independent verifier's Ruff check and whitespace checks
passed. The whitespace scan explicitly included the new untracked research
and test files; `git diff --check` alone does not cover those files.

### Huang Parent-Reference Correction (Historical)

The curation/publication suite passed **313 tests in 453.55 seconds**;
the disjoint discovery/audit suite passed **197 tests in 6.67 seconds**:
**510 distinct tests total**, including three new Huang cases. The earlier
156-test focused run overlaps this coverage and is not counted again.

Curator replay made **no writes or history events**. Independent before/after
reconstruction verifies one new identifier-scope correction, 180 checksum-only
updates, one event per changed record, **21 changed record files and 2,918
byte-identical records**. The source inventory, source alteration/phenotype/assay
fields, other-source assertions, activities, clinical-status assertions and
prior history entries are preserved. The metadata-only dossier SHA-256 is
`16a1c9652528a29aba690d0b2f076c54801f43d468a898a244739ef1987d59f7`.
The proof is `huang-context-proof.json` in
`reports/resistance-grounding-2026-10-07/`. Checksums verify the primary XML,
three UniProt responses and the earlier CGD redirect response. Structural
checks recheck the parent row and locus strings in the cached XML; they do not
replay scientific interpretation, resolve the locus alias or inspect figures.

The independent `huang-discovery-refresh-proof.json` verifies **18 archived
research exports plus the separately preserved census**, all 2,939 current
record hashes, **886 unchanged expansion responses**, identical candidates and
statuses for **611 queries**, and a byte-identical expansion ledger. Only **27
record-hash memberships across 18 records** and their parent checksum bindings
changed. All 7,466 original citation-cache files remain unchanged. Prior exports
are preserved in `huang-before-research/`; earlier dossiers retain their
historical scope. The corpus SHA-256 at this checkpoint is
`f9c3484231d5d98874ced45e0c7b129084ac7c9f15e9f6e796a58503dbf63aac`.

**All 35 offline checkpoint stages passed**, recorded in `huang-checkpoint.log`.
Strict validation covered **2,939 records with zero errors**, and the corpus
reproduces exactly from its source-owned inputs. Documentation statistics,
provenance, source queue, render consistency, repository/helper Ruff and
whitespace checks passed. The publication audit retains all **77 fluconazole
claims**, verifies parent context with reference identifiers confined to
provenance, and preserves the unresolved locus-alias warning. The two existing
activities and 118 clinical-status assertions are unchanged. Rendering pruned
two stale untracked managed-output files; no tracked files were deleted.

**Full QC has not passed.** A read-only environment check confirms that RDKit
is absent under Python 3.13.12/macOS x86_64. The unchanged locked
`rdkit==2026.3.5` incompatibility was not retried or bypassed. No NCBI endpoint
request, outreach, reuse-terms review, source adoption or GitHub mutation
occurred. Identifier review is **181/217**, with **36 associations across 16
papers pending**. Historical locus aliases, exact experimental accessions,
whole-record phenotype validation and the corpus-wide investigation remain open.

### Mehrabi Parent-Reference Correction (Historical)

The curation/publication suite passed **310 tests in 344.88 seconds**;
the disjoint discovery/audit suite passed **197 tests in 5.63 seconds**:
**507 distinct tests total**, including four new Mehrabi cases. The earlier
153-test focused run overlaps this coverage and is not counted again.

Curator replay made **no writes or history events**. Independent before/after
reconstruction verifies two new identifier-scope corrections, 178 checksum-only
updates, one event per changed record, **21 changed record files and 2,918
byte-identical records**. The source inventory, source alteration/phenotype/assay
fields, other-source assertions, activities and prior history entries are
preserved. The metadata-only dossier SHA-256 is
`0aebc5d1186ae1afcd23ca3c1a82aab70243c633f465b3ee7e7865afcb12bde6`.
The final proof is `mehrabi-context-proof-v2.json` in
`reports/resistance-grounding-2026-10-07/`. Checksums verify three UniProt
responses and the citation cache, not the primary PDF text. The primary review
used web-extracted PDF text; direct download returned HTTP 403. No local PDF,
visual page inspection or offline primary-text replay is claimed.

The independent `mehrabi-discovery-refresh-proof.json` verifies **18 archived
research exports plus the separately preserved census**, all 2,939 current
record hashes, **886 unchanged expansion responses**, identical candidates and
statuses for **611 queries**, and a byte-identical expansion ledger. Only **27
record-hash memberships across 18 records** and their parent checksum bindings
changed. All 7,466 original citation-cache files remain unchanged. Prior exports
are preserved in `mehrabi-before-research/`; earlier dossiers retain their
historical scope. The corpus SHA-256 at this checkpoint was
`bfdc75dad0f08962602640abe431a0d8edf18d4e05ebc25fd0084e903926f381`.

**All 35 offline checkpoint stages passed**, recorded in
`mehrabi-checkpoint.log`. Strict validation covered **2,939 records with zero
errors**, and the corpus reproduces exactly from its source-owned inputs.
Documentation statistics, provenance, source queue, render consistency,
repository/helper Ruff and whitespace checks passed. The publication audit
retains all **15 iprodione and 13 fludioxonil claims**, preserves the source
flags and reference-locus link, and verifies both parent-only subject cells
with reference protein and strain identifiers confined to provenance.
Rendering pruned two stale untracked managed-output files; no tracked files
were deleted.

**Full QC has not passed.** The unchanged Python 3.13.12/macOS x86_64 environment
still lacks the locked `rdkit==2026.3.5` build; the incompatibility was not retried
or bypassed. No NCBI endpoint request, outreach, reuse-terms review, source
adoption or GitHub mutation occurred. Identifier review at this checkpoint was **180/217**, with
**37 associations across 17 papers pending**. Exact experimental accessions,
whole-record phenotype validation and the corpus-wide investigation remain open.

### Shima Parent-Reference Correction (Historical)

**503 distinct tests pass across the initial run and targeted rerun.** The
initial curation/publication run finished with 305 passes and one stale carboxin
test expectation failing (393.65 seconds). That expectation was corrected to
include the two newly reviewed associations; no production code changed.
All **149 PHI-base tests** then passed (16.23 seconds), including four new
Shima cases. The 157 other passing cases remain valid and were not rerun.
The disjoint discovery/audit suite passed **197 tests** (6.36 seconds).
Overlapping focused runs are not counted again.

Curator replay made **no writes or history events**. Independent before/after
reconstruction verifies two new identifier-scope corrections, 176 checksum-only
updates, one event per changed record, **21 changed record files and 2,918
byte-identical records**. The source inventory, source alteration/phenotype/assay
fields, other-source assertions, activities and prior history entries are
preserved. The metadata-only dossier SHA-256 is
`197ba7f47a07445799e1e881f7765e4ad160b53ddb332e05b731aef5371f994e`.
The proof is `shima-context-proof.json` in
`reports/resistance-grounding-2026-10-07/`. Checksums verify the final published
follow-up PDF, original-study citation cache and three UniProt responses;
they preserve the evidence snapshot, not an automated replay of scientific reading.

The independent `shima-discovery-refresh-proof.json` verifies **18 archived
research exports plus the separately preserved census**, all 2,939 current
record hashes, **886 unchanged expansion responses**, identical candidates and
statuses for **611 queries**, and a byte-identical expansion ledger. Only **27
record-hash memberships across 18 records** and their parent checksum bindings
changed. All 7,466 original citation-cache files remain unchanged. Prior exports
are preserved in `shima-before-research/`; earlier dossiers retain their
historical scope. The corpus SHA-256 at this checkpoint was
`2b012e0174e22e7a062f8808462c679eb6030e71da03f7a0ef7691fe496f0719`.

**All 35 stages in the rerun offline checkpoint passed**, recorded in
`shima-checkpoint-rerun.log`; the initial failure remains in
`shima-checkpoint.log`. Strict validation covered **2,939 records with zero
errors**, and the corpus reproduces exactly from its source-owned inputs.
Documentation statistics, provenance, source queue, render consistency,
repository/helper Ruff and whitespace checks passed. The publication audit
retains all 36 carboxin claims and verifies both parent-only subject cells with
reference identifiers confined to provenance. Rendering pruned two stale
untracked managed-output files; no tracked files were deleted.

**Full QC has not passed.** The unchanged Python 3.13.12/macOS x86_64 environment
still lacks the locked `rdkit==2026.3.5` build; the incompatibility was not retried
or bypassed. No NCBI endpoint request, outreach, reuse-terms review, source
adoption or GitHub mutation occurred. Identifier review at this checkpoint was **178/217**, with
**39 associations across 18 papers pending**. Exact experimental accessions,
whole-record phenotype validation and the corpus-wide investigation remain open.

### Xu Subject and Species Correction (Historical)

The curation/publication suite passed **302 tests in 401.22 seconds**;
the disjoint discovery/audit suite passed **197 tests in 5.02 seconds**:
**499 tests total**. This includes 28 species-correction tests for malformed
decisions, cross-species identifier retention, atomic rejection of source drift,
the persisted dossier and the live carbendazim subject contexts. Earlier
focused test runs overlap this coverage and are not counted again.

Curator replay made **no writes or history events**. Independent reconstruction
verifies two subject corrections, 174 checksum-only updates, one new event per
changed record, **21 changed files and 2,918 byte-identical files**. All source
alterations, phenotypes, assays, earlier decisions and other-source claims are
preserved. The dossier SHA-256 is
`d6d6eabf92faffa41978b18ac0a938fb47a97af587127e71b3e64c11972aad3f`;
the proof is `xu-context-proof.json` in
`reports/resistance-grounding-2026-10-07/`. The primary XML and seven UniProt
responses are checksum-verified; this preserves the evidence snapshot, not
an automated replay of the scientific reading.

The independent `xu-discovery-refresh-proof.json` verifies **18 archived research
artifacts plus the separately preserved census**, all 2,939 current record
hashes, **886 unchanged expansion responses**, identical candidates and statuses
for **611 queries**, and a byte-identical expansion ledger. Only **27 record-hash
memberships across 18 records** and their parent checksum bindings changed.
The original 7,466 citation-cache files are also unchanged. Prior exports remain
in `xu-before-research/`; earlier dossiers retain their historical scope.
The corpus SHA-256 at this checkpoint was
`2fc65c9c5d27cacc921ac6c670c3c9a62db94c1f7425c8cd1de21540beb901d7`.

**All 35 offline checkpoint stages passed**, recorded in `xu-checkpoint.log`.
Strict validation covered **2,939 records with zero errors**, and the corpus
reproduces exactly from its source-owned inputs. Documentation statistics,
provenance, source queue, render consistency, repository/helper Ruff and
whitespace checks passed. The publication audit retains all 19 carbendazim
claims and verifies both corrected subject cells while keeping rejected or
reference-only identifiers in provenance. Rendering reported two untracked
files pruned from its managed output directory; no tracked files were deleted.

**Full QC has not passed.** The unchanged Python 3.13.12/macOS x86_64 environment
still lacks the locked `rdkit==2026.3.5` build. The previously established
incompatibility was not retried or bypassed by changing the pin. No NCBI
endpoint request, outreach, reuse-terms review, source adoption or GitHub
mutation occurred. Identifier review at this checkpoint was **176/217**, with **41 associations
across 19 papers pending**. Whole-record phenotype validation and the all-record
investigation remain incomplete.

### Pending Identity Audit

Seven focused regression tests passed, covering all 43 source-row bindings,
compound identity, the two reference protein contexts, taxonomy rank, and
metadata-only scope. The offline replay verified all **2,939
record hashes unchanged**, the source inventory and review pins, and seven
cached responses. The dossier SHA-256 is
`54fb4296401c7f93de1ed8140d799f5223cbbd4143492801e5333e4fa8216f86`.
The combined pending-identity, discovery, grounding-audit and source-queue
suite passed **197 tests in 4.69 seconds**. Repository whitespace checks and
Ruff on the new tests and private audit helper passed. The documentation
checker confirmed that README statistics are current.
These checks do not replay inaccessible primary text or constitute full QC;
the previously documented RDKit limitation is unchanged.

### Piotrowska Parent-Reference Correction

The curation/publication suite passed **274 tests in 477.41 seconds**;
the disjoint discovery/audit suite passed **190 tests in 6.00 seconds**:
**464 tests total**. The initial run exposed two outdated carboxin expectations;
both were updated for the three newly scoped claims, and the entire suite was
rerun successfully. No production behavior or source biology was changed to
satisfy those tests. The initial log is preserved separately.

Curator replay made **no writes or history events**. Independent reconstruction
verifies three new scopes, 171 checksum-only updates, one history event per
changed record, 21 changed files and **2,918 byte-identical files**. The dossier
SHA-256 is
`6693ca217386c46d90be20fc3ce030f5f6552363e9b9d3d0160831cfe854f5fd`;
the proof is `piotrowska-context-proof.json` in
`reports/resistance-grounding-2026-10-07/`.

The accepted manuscript response and UniProt metadata are checksum-verified.
That preserves provenance, not an automated replay of the scientific reading.
The separately inspected Broomfield publisher page still provides only a
[subscription preview](https://link.springer.com/article/10.1007/BF00351470);
its subject/allele crosswalk remains pending and was not curated.

**All 34 offline checkpoint stages passed**, recorded in
`piotrowska-checkpoint.log`. Strict validation covered **2,939 records with
zero errors**, and the corpus reproduced exactly. Documentation statistics,
provenance, source queue, render consistency, repository/helper Ruff and
whitespace checks passed. The rendered-page audit retained all 36 carboxin
claims and verified the three corrected provenance/subject distinctions.

The additional `piotrowska-discovery-refresh-proof.json` checks **19 archived
artifacts**, **886 unchanged expansion response files**, identical candidate
sets and statuses for **611 queries**, and a byte-identical expansion ledger.
Only **27 record-hash memberships across 18 records** changed, together with
their parent checksum bindings. All 2,939 current record hashes were checked;
the prior exports remain in `piotrowska-before-research/`.

**Full QC has not passed.** The read-only environment check still finds no
RDKit under Python 3.13.12/macOS x86_64; the known incompatible locked build
was not retried or changed. No NCBI endpoint request, outreach, reuse-terms
review, source adoption or GitHub mutation occurred. Identifier review at that checkpoint was
**174/217**, with **43 associations across 20 papers pending**. Whole-record
phenotype validation and the all-record investigation remain incomplete.

### Duan Reference-Scope Correction

**All 34 offline checkpoint stages passed**, followed by an independent
archived/current discovery comparison. The log is `duan-checkpoint.log` under
`reports/resistance-grounding-2026-10-07/`. The curation/publication suite passed
**271 tests in 347.44 seconds**; the disjoint discovery/audit suite passed
**190 tests in 4.02 seconds**, for **461 tests total**. Earlier focused runs
overlap this coverage and are not counted again. Two initially failing new
tests had an incomplete reseeding fixture; the fixture was corrected without
changing or weakening production behavior.

Strict schema validation passed for all **2,939 records with zero errors**.
Exact corpus reproduction found no missing records, unexpected records,
drifted fields or path-lock inconsistencies. Documentation, provenance,
source queue, render consistency, repository/helper Ruff and whitespace
checks passed. The publication audit retains all 14 claims across the two
affected records and checks that the five corrected associations retain
their source text while excluding PH-1 identifiers from subject links.

Curator replay made **no writes or history events**. The independent audit
reconstructed five scoped corrections and 166 checksum-only updates, verified
21 changed files with one event each and 2,918 byte-identical files, and
reproduced the dossier byte-for-byte. Its SHA-256 is
`b625d75d006609f21d3c29e85c50005a901ede4b17a5fe729895d2a457f78283`;
the proof is `duan-context-proof.json` in the report directory.

The additional `duan-discovery-refresh-proof.json` verifies **19 archived
research artifacts**, all 2,939 current record hashes, and **886 unchanged
response files**. All 611 query candidate sets and statuses are identical;
the expansion ledger is byte-identical. Only **27 record-hash memberships
across 18 records** changed in the discovery exports, plus their parent
checksum bindings. Prior exports remain in `duan-before-research/`; earlier
dossiers and checkpoint statements retain their historical snapshot scope.
The refreshed census still has 4,780 resistance assertions and 467 score rules.

**Full QC has not passed.** A fresh read-only check confirms that RDKit is
absent under Python 3.13.12/macOS x86_64. The unchanged `rdkit==2026.3.5` lock
has 20 wheels, zero compatible wheels and no source distribution. No install
retry or dependency-pin change was made. No NCBI endpoint request, outreach,
reuse-terms review, source adoption or GitHub mutation occurred. Identifier
review at that checkpoint was **171/217**, with **46 associations across 21 papers pending**;
corpus-wide primary review remains incomplete.

### Oligomycin Reference-Only Follow-Up

The focused oligomycin, curated-grounding, grounding-audit and source-queue
suite passed **91 tests in 4.00 seconds**, including seven new oligomycin checks.
These guard exact congener identity, reference versus experimental subject
scope, unresolved functional-paper links, full-text access status and the
metadata-only export boundary. This overlaps earlier suites; it is not added
to the prior 450-test checkpoint total.

Both retrieval stages replayed from existing caches with network access
disabled. The independent verifier reproduced the dossier and its proof
byte-for-byte, checking two reference proteins, two taxa, six citations and
the reciprocal PDB/UniProt ligand crosswalk. Dossier SHA-256:
`cc18b04738b286622dd942094e02b93d833f3f7806b1c73445693765a25c06d4`.
The proof is `oligomycin-reference-proof.json` under
`reports/resistance-grounding-2026-10-07/`. Manual publisher interpretation is
explicitly outside the offline full-text replay claim.

All **2,939 record hashes and file membership** match the current census.
Source reviews, the PHI-base inventory and current discovery exports are
unchanged. This follow-up added **zero biological record changes, curation
events, measurements or experimental allele assignments**. The documentation
statistics check passed. Full schema, reproduction and publication checks were
not rerun for this metadata-only checkpoint; their preceding results below
retain their original scope. Full QC remains limited by the known RDKit
environment incompatibility. NCBI access, outreach and #1040 remain deferred;
there were no GitHub mutations. All-record primary review remains incomplete.

### Nakayama Reference-Scope Correction

**All 34 offline checkpoint stages passed**, followed by an independent
archived/current discovery comparison. The log is `nakayama-checkpoint.log`
under `reports/resistance-grounding-2026-10-07/`. The curation/publication suite
passed **260 tests** (503.04 seconds), and the disjoint discovery/audit suite
passed **190 tests** (5.46 seconds): **450 tests** total. The earlier 110-test
focused run overlaps this coverage and is not counted again.

Strict schema validation passed for all **2,939 records with zero errors**.
Exact corpus reproduction reported no missing records, unexpected records,
drifted fields or path-lock inconsistencies. Provenance, source queue, README
statistics, rendered-page consistency, repository/helper Ruff and whitespace
checks passed. The publication check retains all 77 fluconazole claims and two
activities, preserves the source background label with its scope note, and
keeps `P50859` and `284593` out of experimental-subject identifier links.

Curator replay made **no writes or history events**. The independent audit
reconstructed the new correction and all 165 checksum-only updates, verified
21 changed files with one event each and 2,918 byte-identical files, and
reproduced the dossier byte-for-byte. Its SHA-256 is
`097ef6f014aa6716e2fa2895e3c54c2c1a4cc908686cc9aee0a3935cd12d6c3e`;
the proof is `nakayama-context-proof.json` in the report directory.

The additional `nakayama-discovery-refresh-proof.json` verifies **19 archived
research artifacts**, all 2,939 current record hashes, and **886 unchanged
accepted/rejected response files**. All 611 query candidate sets and statuses
are identical; the expansion ledger is byte-identical. Only **27 record-hash
memberships across 18 records** changed in the plan/candidate exports, together
with their parent checksum bindings. The prior exports and census remain in
`nakayama-before-research/`. Earlier dossiers, proofs and checkpoint statements
retain their historical snapshot scope; they were not rewritten to claim the
post-Nakayama hashes.

**Full QC has not passed.** A fresh read-only check confirms that RDKit is still
absent under Python 3.13.12/macOS x86_64. The unchanged lockfile pins
`rdkit==2026.3.5`, with 20 wheels, zero compatible with this interpreter/platform,
and no locked source distribution. No install retry or pin relaxation was made.
No NCBI endpoint request, outreach, reuse-terms review, source adoption or GitHub
mutation occurred. Identifier-scope coverage is **166/217 PHI-base associations**;
all-record primary review remains incomplete.

### Darlington Subject Correction

All **34 offline checkpoint stages passed after correcting a publication-check
column assertion**, followed by an additional independent discovery-preservation
check. The qualifier and complete source alteration were already present in the
rendered claim-text column; the initial helper incorrectly checked the
mechanism-type column. No record or renderer change was needed for that failure.
The original failed log remains `darlington-checkpoint.log`; the resumed stages
are in `darlington-checkpoint-continuation.log`, both under
`reports/resistance-grounding-2026-10-07/`.

The PHI-base, organismal-context, curated-grounding, activity-page and publication
suite passed **258 tests** (513.64 seconds). The separate discovery, grounding
audit, CARD, HIVDB and source-queue suite passed **190 tests** (5.75 seconds):
**448 tests across disjoint test files**. Earlier focused runs overlap these
suites and are not additional coverage. Strict schema validation passed for all
**2,939 records with zero errors**; exact corpus reproduction reported no
missing records, unexpected records or drifted fields. Documentation statistics,
provenance, source-queue, rendered-page consistency, repository/helper Ruff and
whitespace checks also passed.

The independent curation audit reconstructed the one new subject correction and
**164 checksum-only claim updates**, verified all 217 retained PHI-base claims,
and confirmed **21 changed record files and 2,918 byte-identical files**. Each
changed file has exactly one new curation event; unchanged files have none.
Curator replay made no writes or history events, and the independent dossier
reproduced byte-for-byte. The publication check retained all 77 fluconazole
claims and two activities, placed the tested subject in the organism column,
and kept withheld reference identifiers in provenance rather than subject links.
The independent proof is `darlington-context-proof.json` in the report directory.

The additional `darlington-discovery-refresh-proof.json` verifies **19 archived
research artifacts**, all 2,939 current record hashes and **886 unchanged
accepted/rejected response files**. All 611 expansion queries retain identical
candidate identities and statuses; the expansion ledger is byte-identical.
Only **27 record-hash memberships across 18 records** changed in the refreshed
expansion plan/candidate exports, together with their parent checksum bindings.
The previous census and exports remain in `darlington-before-research/`.
Earlier checkpoint claims about unchanged or current hashes refer to their
then-current snapshots, not the post-Darlington corpus; their original dossiers
and proofs have not been rewritten.

Coverage is **165/217 identifier-scoped PHI-base associations**, not completed
corpus-wide primary review. All 611 discovery query primary-review statuses
remain pending. **Full QC has not passed**: the pinned `rdkit==2026.3.5` remains
unavailable for the documented Python 3.13.12/macOS x86_64 environment. No
unchanged installation retry, relaxed dependency pin, NCBI request, outreach,
reuse-terms review, source adoption or GitHub mutation occurred.

### Cursor Conflict Recovery

**All seven offline checkpoint stages passed**, including Ruff, documentation
statistics and whitespace checks.
The focused discovery, grounding-audit, CARD, HIVDB and source-queue suite passed
**190 tests** (11.58 seconds). The separate 90-test discovery run overlaps this
suite and is not additional distinct coverage. New cases preserve complete valid
prefixes, reject an entire overlapping page, count rejected responses against
the request cap, resume other queries, and detect changes to rejection caches.
End-to-end cases cover changed counts, versions and short pages. Provenance,
query-echo, identifier, within-page duplicate and abstract guards remain strict;
the shared fetcher retains intact cursor conflicts only with explicit opt-in.

The initial 474-response attempt accepted two pages before detecting a repeated
`PPR:PPR552787` in the amikacin query. Its response was preserved. A one-page
`CHEBI:2676` continuation canary passed independent checks. A subsequent
469-response attempt stopped before accepting a new page because the next page
length was inconsistent; that failed response body was not retained by the
then-current fetcher. After adding explicit conflict retention, a one-response
amphotericin B diagnostic preserved a page with **180 rows where 179 were
expected**, including an overlap with the accepted first page. This diagnostic
is a new response, not a reconstruction of the discarded body. The entire page
was excluded. The final 468-response batch stopped normally after 269 responses
because every remaining chain was complete or explicitly conflicted.

Independent reconstruction checked all **795 accepted and 91 rejected pages**,
611 query identities, 612 record-query memberships, candidate identities,
summaries and ledger rows. It verified all **7,466 original query caches** and
all **2,939 current record hashes** unchanged. The preservation audit verified
all 612 earlier page files and candidate prefixes, all 459 earlier completed
query results, the unchanged plan and census, and lossless gzip round-trip bytes.
The independent proof also pins the discovery code and regression-test hashes.

The checkpoint log is `expansion-conflict-checkpoint.log` under
`reports/resistance-grounding-2026-10-07/`. Its independent proof is
`expansion-conflict-proof-8e0f2f3f127b38bef86d60121f375a0379ce036bed356d50bdb521dbe767c334.json`
under that directory. This checkpoint made **zero biological record changes**
and no new protein, allele, taxon or measurement assignments. All 611 query
primary-review statuses remain pending. No NCBI request, outreach, reuse-terms
review, source adoption or GitHub mutation occurred. **Full QC remains
incomplete** because of the previously documented RDKit environment limitation.

### Hygromycin B Figure Follow-Up

The independent offline follow-up audit verified **four additional reference-gene
crosswalks, three publisher-linked figure files and 26 source-qualified subject
memberships**, including all comparator rows. It checked body/cache hashes,
publisher HTML-to-PNG links, PNG dimensions, primary XML tables, source symbols
versus UniProt preferred names/synonyms, loci, SGD identifiers, database release
and entry/sequence versions. It also checked both conflicting VJY305 labels
against their respective tables and preserved the two older-study access failures.

Manual visual review covered all ten labeled panels; the automated audit verifies
source integrity and structured mappings, not growth significance or phenotype
interpretation. The original four-gene, ten-focal-row dossier and its independent
proof were rechecked unchanged. Together the dossiers retain eight reference
genes, not eight independent causal resistance findings. All **2,939 current
record hashes remain unchanged**; this follow-up made zero biological edits.

The focused curated-grounding, grounding-audit and source-queue suite passed
**84 tests** (8.62 seconds). Ruff passed for the four follow-up helpers; README
statistics and whitespace checks passed. Offline regeneration reproduced the
new dossier byte-for-byte, and the independent proof also reproduced unchanged.
The comparator-gene lookup replay used only existing caches, preserving the
explicit `DOA10` synonym match rather than requiring a preferred-name match.

The new dossier SHA-256 is
`ae84c2b65f383008dc7b2377df370ab0c0497816ce87e9e29ed7732a9d5c4d39`.
Its independent proof is `hygromycin-yeast-visual-proof.json` under
`reports/resistance-grounding-2026-10-07/`. No NCBI request, outreach, source
adoption, genome-analysis pipeline or GitHub mutation occurred. Full QC remains
incomplete because of the previously documented RDKit environment limitation.

### Earlier Hygromycin B Text-Only Checkpoint

The offline source audit verified **four reference-gene crosswalks, three
primary XML bodies, two taxonomy entries and ten focal subject-table rows**.
It checked request origins, body and cache hashes, database release, exact gene
and locus names, SGD cross-references, entry/sequence versions, primary DOI and
publication dates, subject names, figure panels and comparator-table membership.
The source Results support the retained phenotype direction and the distinct
complementation and discordance caveats. Automated source checks do not replace
manual interpretation. Figure-pixel review was unperformed at that checkpoint
and is now documented in the separate follow-up above.

All **2,939 current record hashes remain unchanged**, including hygromycin B
and the earlier curations. The selected studies were not promoted to complete
query reviews or to new resistance assertions. The exported dossier pins the
same corpus census as the 612-page citation checkpoint. The independent proof
is `hygromycin-yeast-reviewed-proof.json` under
`reports/resistance-grounding-2026-10-07/`. No NCBI request, outreach, source
adoption, new genome pipeline or GitHub mutation occurred. Full QC remains
incomplete because of the previously documented RDKit environment limitation.
The earlier draft proof is retained separately; final review narrowed the UFD2
wording from an assertion about experiments performed to what the paper reports.

### Citation Expansion and Storage

**All seven offline checkpoint stages passed.** The discovery, grounding-audit,
CARD, HIVDB and source-queue suite passed **161 tests** (4.89 seconds), including
five new compression regressions. The separate 36-test expansion run overlaps
this suite and is not additional distinct coverage. Compression tests check
lossless and repeatable bytes, separate checksums, source-overwrite refusal,
source-change detection, failed round trips and corrupt temporary-file handling.
Failed publication preserves the previous target. Ruff, documentation statistics
and whitespace checks passed.

Independent verification reconstructed all 612 pages, 611 queries, 612
record-query memberships, citation identities and ledger rows. It checked all
7,466 unchanged original query caches and all 2,939 current record hashes. The
separate storage audit verified the previous 352 page files and their candidate
prefixes, all 278 previously complete query results, the unchanged expansion
plan, the archived census and the exact decompressed export. This checkpoint
made **zero biological record changes**; earlier curations remain intact.

Two primary-paper follow-ups remain pending. The
[Jung 1992 publisher PDF](https://onlinelibrary.wiley.com/doi/pdf/10.1002/cm.970220304)
did not provide accessible Results in this attempt. For the
[2024 SDH8 paper](https://doi.org/10.1080/21505594.2024.2405000), cached primary
XML and UniProt metadata still leave the `orf19.1588` / `orf19.9161` relationship
unresolved. The public CGD locus page could not be retrieved through the
available tools; this is an access limitation, not evidence that an alias is
absent. A shared paper citation was not promoted to an exact locus or allele
crosswalk. No new claim, identifier or measurement was curated from either lead.

The log is `expansion-storage-checkpoint.log`; the independent proof is
`expansion-storage-checkpoint-proof.json`, both under
`reports/resistance-grounding-2026-10-07/`. At that checkpoint, the 53 pending
PHI-base associations across 24 papers, 152 partial cursor traversals and
all-record primary review remained open. **Full QC has not passed** because of
the previously documented RDKit environment limitation. No unchanged installation retry, NCBI request,
outreach, reuse-terms work, source adoption or GitHub mutation occurred.

### Flucytosine Follow-Up

**All 32 offline checkpoint stages passed.** The combined curator-grounding and
publication suite passed **88 tests** (15.25 seconds), including five new
flucytosine regressions. The discovery, grounding-audit, CARD, HIVDB and
source-queue suite passed **156 tests** (5.53 seconds). The earlier pre-correction
run is preserved but is not counted as a passing checkpoint or additional
distinct test coverage.

The validated-writer dry run, independent exact-delta audit and idempotent replay
passed. Exactly one record gained two associations and two history events; eight
CARD claims, unrelated biological fields and the other 2,938 records are
unchanged. Diff review caught key-order churn caused by reconstructing a record
from a sorted JSON snapshot. The helper now uses the live loader's ordering;
the corrective validated write preserved all biological values and earlier
history. Removing only the new claims and events reproduces the original YAML
byte-for-byte, checked independently and by regression. The original and
intermediate snapshots remain in the cache.

All 2,939 records passed strict validation with zero errors and reproduced
exactly from source and curator inputs, with zero missing records or field drift.
Documentation, provenance, source gates, rendering and render comparison,
repository-wide Ruff and whitespace checks passed. The publication audit checked
all ten flucytosine rows: eight source assertions and two cohort associations.
Reference-only identifiers and parental backgrounds remain outside tested-organism
cells. Earlier FUR1, clinical-table, evidence, browser-binding, download and
reference-scope publication checks also passed.

The independent citation audit reproduced all 352 cached pages, 611 queries,
612 record-query memberships and exported citations against the current census.
It verified all 2,939 record hashes and 7,466 unchanged original query caches.
The previous 202-page exports are preserved in `expansion-second-checkpoint/`.
The latest bounded network batch completed exactly 150 additional citation pages
using only EMBL-EBI Europe PMC. These citations are not automatically reviewed
primary findings or biological assignments.

The log is `flucytosine-fur1-checkpoint.log` and the byte-level proof is
`flucytosine-fur1-independent-proof.json`, under
`reports/resistance-grounding-2026-10-07/`. **Full QC has not passed**: the locked
RDKit dependency remains unavailable in the documented macOS x86_64 environment.
No installation retry or dependency-pin change was attempted. No NCBI request,
outreach, reuse-terms work, source adoption or GitHub mutation occurred. The
53 pending PHI-base associations across 24 papers, 333 incomplete cursor
expansions and all-record primary review remain open.

### Earlier FUR1 Checkpoint

The FUR1 cohort checkpoint passed **206 resistance and organism-context tests**
(584.33 seconds), including four new regressions for cohort scope, reference-only
identifiers, non-MIC phenotype evidence and reseeding preservation. The separate
discovery, grounding-audit, CARD, HIVDB and source-queue suite passed **156 tests**
(5.27 seconds). The four-test FUR1 rerun is included in the 206-test suite, not
four additional distinct cases.

At that checkpoint, independent comparison verified exactly two new gene-level
associations and two curation events on 5-fluorouracil; all unrelated fields and
the other 2,938 records were unchanged from the FUR1 before-image. Scope review removed synthetic
cohort descriptions from structured strain fields while preserving them in claim
labels. Primary text, four UniProt responses, reference versions and the empty
literal background query are checksum-pinned. Replay made no further record
write or curation event. The older exact-allele questions remain unresolved.

**All 49 offline checkpoint stages passed.** All 2,939 records passed strict
schema validation with zero errors and reproduced exactly from their inputs,
with no missing records or field drift. Documentation statistics, provenance,
source gates, full-site rendering and render comparison, repository-wide Ruff,
and whitespace checks passed. The actual-publication audit verified both FUR1
rows, their assays and citations, and kept reference-only P18562, YHR128W and
TaxID 559292 out of tested-organism cells. Earlier clinical-table, evidence,
browser-binding, download and reference-scope publication checks also passed.
`test_activity_pages.py` and `test_publication_search.py` passed **44 tests**
(7.01 seconds).

The independent citation verifier reproduced all 202 cached pages and current
exports, including all 611 queries, 612 record-query memberships, 2,939 current
record hashes and 7,466 unchanged original caches. The separate 150-page network
batch completed within its request bound. Current record pins include the FUR1
curation; they do not claim that record is unchanged from the earlier citation
checkpoint. The original 52-page exports remain in `expansion-first-checkpoint/`.

The successful run is recorded in `fur1-cohort-checkpoint.log`; the complete
record comparison is `fur1-cohort-independent-proof.json`, both under
`reports/resistance-grounding-2026-10-07/`. An earlier run was deliberately
stopped for the strain-scope correction and is not counted as a passing run.
**Full QC has not passed**: the locked RDKit dependency remains unavailable in
the Python 3.13.12/macOS x86_64 environment. Read-only architecture checks did
not establish an alternative runtime; no dependency pin was relaxed or failed
installation repeated. No NCBI request, outreach, reuse-terms work, source
adoption or GitHub mutation occurred. The 53 pending PHI-base associations across
24 papers and the broader all-record primary investigation remain open.

The earlier 52-page citation-expansion checkpoint passed **156 focused discovery, grounding-audit,
HIVDB, CARD and source-queue tests** (9.88 seconds), repository-wide Ruff, and
`git diff --check`. The independent offline verifier reproduced every expanded
query, page, exported citation, summary and ledger row from raw response caches,
including all record/name memberships and source-qualified deduplication.
All **2,939 live records and 7,466 original query caches are byte-identical**
to their pre-expansion pins. The two-page canary and 50-page batch completed
within their bounds. Offline replay of the completed canary produced zero new
pages; the final raw-cache audit confirmed unchanged evidence. Review fixes
added post-filter class balancing and
same-byte parse/hash plus pre-export page-cache checks. No new biological
curation was inferred from citation metadata. Full QC was not rerun for this
citation-only checkpoint; the previously documented RDKit limitation remains.

The earlier Ren subject checkpoint passed its validated-writer canary and independent
exact-diff audit. **All 45 offline checkpoint stages passed.** The
resistance/context suite passed **202 tests** (401.10 seconds), and
`test_activity_pages.py` plus `test_publication_search.py` passed **44 tests**
(7.63 seconds). The manual-access/discrepancy regression also passed a separate
focused rerun; it is not an additional distinct case.

All 2,939 records passed strict schema validation with zero errors and reproduced
exactly from source and curator inputs, with zero field drift. Eight subject
corrections and 156 checksum-only changes are pinned across 21 records;
2,918 others are byte-identical. Every refreshed census hash matches the live
record. Earlier decisions, source alterations, phenotype and assay fields,
claim order, curator claims and activities are preserved. Replay made no further
writes or history events. Historical dossiers retain their evidence and pins.

The metadata audit checks one reference protein, two taxa, three UniProt
responses and all 25 prior pending-paper citation responses. Five unresolved
lead claims are unchanged. The primary table review remains **manual and
uncached**; offline verification does not replay that inspection. The indexed
Sg-28 discrepancy requires an original-table check and is not treated as a
verified error in the article. No measurement, exact experimental protein,
subject TaxID, genome or sample was assigned.

Documentation, provenance, source gates, rendering, lint and whitespace checks
passed. The actual-publication audit preserves all 15 iprodione and 13
fludioxonil claims. Four tested descendants are displayed for each compound,
with their parents and B05.10 identifiers retained in provenance rather than
tested-subject cells. All earlier publication checks passed, including the two
fluconazole and three voriconazole clinical tables, evidence, browser bindings
and full-record downloads. Auxiliary helper lint passed.

The log is `ren-subject-context-checkpoint.log` under
`reports/resistance-grounding-2026-10-07/`; the complete byte comparison is
`ren-subject-context-census-proof.json` in that cache. **Full QC has not passed**:
Python 3.13.12 on macOS x86_64 still lacks the locked RDKit dependency. Its
installation was not retried and its pin was not relaxed. No NCBI request,
outreach, terms reassessment, source adoption or GitHub mutation occurred.
**53 PHI-base associations across 24 papers** remain pending identifier review;
the broader all-record primary investigation is incomplete.

### Previous checkpoints

The six-paper OA checkpoint passed its validated-writer canary and independent
exact-diff audit. **All 44 offline checkpoint stages passed.** The
resistance/context suite passed **198 tests** (359.74 seconds), and
`test_activity_pages.py` plus `test_publication_search.py` passed **44 tests**
(12.03 seconds). The earlier 96-test run overlaps the expanded suite and is not
an additional set of distinct cases.

All 2,939 records passed strict schema validation with zero errors and reproduced
exactly from source and curator inputs, with zero field drift. Six new identity
corrections and 150 checksum-only claim updates are pinned across 21 records;
the other 2,918 are byte-identical. Every refreshed census hash matches the live
record. Previous decisions, source biological fields, claim order, curator
claims and activities are preserved. Replay made no further writes or history
events. Historical dossiers retain their original evidence and record pins.

The evidence audit checks six reference proteins, eight taxonomy records,
12 UniProt responses, all 31 prior pending-paper citation responses and six
cached primary XML texts. Citation request metadata, primary PMID/DOI identity,
release metadata and body checksums replay. Five unresolved lead claims from
three papers are unchanged. No exact experimental allele, subject TaxID,
genome, sample or activity measurement was inferred.

Documentation, provenance, source gates, rendering, lint and whitespace checks
passed. The actual-publication audit preserves all six hydrogen-peroxide,
19 carbendazim and 11 azoxystrobin claims. The six reference identifier sets
remain in provenance and are absent from tested-subject cells; the retained
source gene ID remains displayed. The azoxystrobin co-occurrence warning is
visible. All earlier publication checks passed, including the two fluconazole
and three voriconazole clinical tables, evidence, browser bindings and complete
downloads. Auxiliary helper lint passed.

The log is `fungal-oa-context-checkpoint.log` under
`reports/resistance-grounding-2026-10-07/`; the complete byte comparison is
`fungal-oa-context-census-proof.json` in that cache. **Full QC has not passed**:
the pinned Python 3.13.12/macOS x86_64 environment still lacks RDKit. Its
installation was not retried and the dependency pin was not changed.
No NCBI request, outreach, terms reassessment, source adoption or GitHub mutation
was performed. At that checkpoint, **61 PHI-base associations across 25 papers** remained pending
identifier review, and the broader all-record primary investigation is incomplete.

The primary-context checkpoint passed its validated-writer canary and independent
exact-diff/evidence audit. **All 43 offline checkpoint stages passed.** The
resistance/context suite passed **193 tests** (508.11 seconds), and
`test_activity_pages.py` plus `test_publication_search.py` passed **44 tests**
(8.26 seconds). The focused 96-test review-module run is included in the 193,
not additional distinct cases.

All 2,939 records passed strict schema validation with zero errors and reproduced
exactly from source and curator inputs. Nine new scope corrections and 141
checksum-only claim updates are pinned across 19 records; the other 2,920
records are byte-identical to the preceding checkpoint. Every refreshed census
hash matches the live record. Source biological fields, claim order, existing
curator claims, clinical activities and history are preserved. Replay made no
additional writes or history events. Both incompletely reviewed lead claims
remain unchanged. Historical dossiers retain their original evidence and pins.

The independent evidence audit checks six reference proteins, eight taxonomy
records, 11 UniProt responses and all 35 prior pending-paper citation responses.
All four new primary identity reviews are manual and uncached; their Results
are not replayed by the offline metadata checks. No exact experimental allele,
genome, subject TaxID or measurement was inferred.

Documentation, provenance, source gates, rendering, lint and whitespace checks
passed. The actual-publication audit preserves all 36 carboxin, 33 caspofungin,
77 fluconazole, 62 voriconazole, two pyrifenox and two triflumizole claims.
The nine new identifier sets remain in provenance, absent from tested-subject
cells. The caspofungin analogue warning is displayed in the claim notes. All
earlier publication checks passed, including the two fluconazole and three
voriconazole clinical tables, evidence, browser bindings and complete downloads.
The prior carboxin checks now explicitly include the 29th reviewed association.
Auxiliary helper lint passed.

The log is `fungal-primary-context-checkpoint.log` under
`reports/resistance-grounding-2026-10-07/`; the complete byte comparison is
`fungal-primary-context-census-proof.json` in that cache. **Full QC has not
passed**: Python 3.13.12 on macOS x86_64 still lacks the locked RDKit dependency.
Its installation was not retried or its pin relaxed. No NCBI request, outreach,
source adoption or GitHub mutation was made. At that checkpoint, **67 PHI-base associations across
31 papers** remained pending identifier review; the broader all-record primary
investigation remains incomplete.

The fungal-identity follow-up passed its validated-writer canary and independent
exact-diff/evidence audit. **All 42 offline checkpoint stages passed.** The
resistance/context suite passed **184 tests** (339.23 seconds), and
`test_activity_pages.py` plus `test_publication_search.py` passed **44 tests**
(7.11 seconds). The focused 87-test review-module run is included in the 184,
not additional distinct cases.

All 2,939 records passed strict schema validation with zero errors and
reproduced exactly from source and curator inputs. Twelve new identity-scope
corrections and 129 checksum-only claim updates are pinned across 17 records;
the other 2,922 records are byte-identical to the preceding checkpoint. The
refreshed census matches every live record hash. Existing claim order, source
biological fields, curator claims, clinical activities and history are preserved.
Replay made no further writes or history events. Historical dossiers verify
without replacing their original record or review pins.

The evidence audit verifies six reference proteins, five taxonomy records,
nine UniProt responses, all 41 prior pending-paper citation responses and two
cached primary texts. Five ASM primary-text reviews remain explicitly manual
and uncached; offline citation verification does not replay those Results.
The separate SDH8 locus review was unresolved at that historical checkpoint
and made no biological change then; the later CGD follow-up above resolves
reference nomenclature only.

Documentation, provenance, source gates, rendering, lint and whitespace checks
passed. The actual-publication audit preserved all 54 itraconazole, 62
voriconazole, 11 terbinafine and 77 fluconazole claims. The 12 newly scoped
identifier sets remain in provenance and are absent from tested-subject cells.
All earlier publication checks passed, including the two fluconazole and three
voriconazole clinical tables, evidence, browser bindings and complete downloads.
Auxiliary helper lint passed.

The log is `fungal-identity-followup-checkpoint.log` under
`reports/resistance-grounding-2026-10-07/`; the complete byte comparison is
`fungal-identity-followup-census-proof.json` in that cache. **Full QC has not
passed**: Python 3.13.12 on macOS x86_64 still lacks the locked RDKit dependency.
Its installation was not retried or its pin relaxed. No NCBI requests, source
adoption, outreach or GitHub mutations were made. That left **76 PHI-base
associations across 35 papers** pending identifier review; the broader
all-record primary investigation remains incomplete.

The yeast-reference checkpoint passed its validated-writer canary and
independent exact-diff/evidence audit. **All 41 offline checkpoint stages
passed.** The resistance/context suite passed **178 tests** (374.38 seconds),
and `test_activity_pages.py` plus `test_publication_search.py` passed
**44 tests** (6.78 seconds). The separate 81-test review-module run is included
in the 178, not additional distinct cases.

All 2,939 records passed strict schema validation with zero errors and
reproduced exactly from source and curator inputs. One new identity correction
and 128 checksum-only claim updates are pinned across 16 records; the other
2,923 records are byte-identical to the preceding checkpoint. The refreshed
census matches every live hash. Existing claim order, source biological fields,
curator claims, clinical activities and history are preserved. Replay made no
further writes or history events. Historical dossiers verify without replacing
their original record or review pins.

The evidence audit verifies one reference protein, two taxonomy records,
six UniProt responses, seven citation responses and one cached primary text.
The Li publisher PDF text inspection remains explicitly manual: its direct
download returned 403, and no successful local PDF rendering is asserted.
Twenty-one associations in this seven-paper cohort remain unresolved.

Documentation, provenance, source gates, rendering, lint and whitespace checks
passed. The actual-publication audit preserved all 19 carbendazim claims and
confirmed that the tested group is displayed separately from reference and
parent identities. All earlier carboxin, iprodione, fludioxonil and azole
publication checks passed, including the two fluconazole and three voriconazole
clinical tables, evidence, browser bindings and complete downloads. Auxiliary
helper lint passed.

The log is `li-reference-checkpoint.log` under
`reports/resistance-grounding-2026-10-07/`; the complete byte comparison is
`li-reference-census-proof.json` in that cache. **Full QC has not passed**:
the Python 3.13.12 macOS x86_64 environment still lacks the locked RDKit
dependency. Its installation was not retried or its pin relaxed. No NCBI
requests, source adoption, outreach or GitHub mutations were made. That left
**88 PHI-base associations across 41 papers** pending identifier review;
subsequent progress is recorded above.

The A. fumigatus checkpoint passed its validated-writer canary and independent
exact-diff/evidence audit. **All 40 offline checkpoint stages passed.** The
resistance/context suite passed **176 tests** (370.92 seconds), and the separate
activity-publication suite passed **29 tests** (13.54 seconds). The updated
review module also passed its separate 79-test run; those tests are included
in the 176, not additional distinct cases.

All 2,939 records passed strict schema validation with zero errors and reproduced
exactly from source and curator inputs. Seventeen new scope corrections and
111 checksum-only updates are pinned across 15 records; the other 2,924 records
are byte-identical to the preceding checkpoint. The refreshed census matches
every live record hash. Source wording, claim order, curator claims, clinical
activities and existing history were preserved. Idempotent replay made no
further writes or history events. The historical checkpoint chain verifies
without replacing its original record or review pins.

The independent evidence audit checks two reference proteins, two taxonomy
records, three UniProt responses, seven citation responses, and one cached
primary text. Four other publisher Results reviews remain explicitly manual
and uncached; offline citation verification is not primary-text replay.
The exported dossier contains identifier metadata, not experimental methods
or sequences.

Documentation, provenance, source gates, rendering, lint and whitespace checks
passed. The actual-publication audit preserved all 54 itraconazole, 28
posaconazole and 62 voriconazole claims. The 17 newly scoped identifier sets
remain in provenance and are absent from tested-subject cells. Earlier
iprodione, fludioxonil and carboxin publication checks passed, as did the two
fluconazole and three voriconazole clinical tables, evidence, browser bindings
and complete downloads. Auxiliary helper lint passed.

The log is `fumigatus-reference-checkpoint.log` under
`reports/resistance-grounding-2026-10-07/`; the all-record byte comparison is
`fumigatus-reference-census-proof.json` in the same cache. **Full QC has not
passed**: the current Python 3.13.12 macOS x86_64 environment still lacks the
locked RDKit dependency. Its installation was not retried or its pin relaxed.
No NCBI requests, source adoption, outreach or GitHub mutations were made.
That checkpoint left **89 PHI-base associations across 42 papers** pending
identifier review; subsequent progress is recorded above.

The iprodione/fludioxonil checkpoint passed its validated-writer canary,
independent exact before/after comparison and idempotent replay. The independent
audit checks 14 record pins, four reference proteins, 25 original deposits
across 21 additional entries, four taxonomy records, eight successful UniProt
grounding responses, one narrowly scoped no-hit response, seven citations and
two primary full-text responses. Only metadata is exported; experimental
methods and sequences remain outside the research artifact.

**All 39 offline checkpoint stages passed.** The checkpoint's resistance/context
suite passed **167 tests** (465.15 seconds). Three additional crosswalk regression
cases passed separately, and the fully updated review module passed **73 tests**
(8.60 seconds), giving 170 distinct resistance/context tests. The separate
activity-publication suite passed **29 tests** (11.15 seconds).

All 2,939 records passed strict schema validation with zero errors and reproduced
exactly from source and curator inputs. The refreshed census matches every live
record hash: exactly 14 records changed and 2,925 remained byte-identical to the
preceding checkpoint. Eleven associations received scope corrections; 100 older
associations received only the review-file checksum refresh. Claim order,
source alterations, phenotypes, assay flags and unrelated curator fields were
preserved. The historical checkpoint chain still verifies against its original
record pins.

Documentation, provenance, source gates, rendering, lint and whitespace checks
passed. The actual-publication audit verified all 15 iprodione and 13 fludioxonil
rows, including the three resolved subject labels; the 11 reference-only
identifier sets remain in provenance rather than tested-organism cells.
All 36 carboxin rows and its 28 scoped identifier sets remain correctly displayed.
The earlier two fluconazole and three voriconazole clinical observations retain
their tables, evidence, browser bindings and complete downloads. Idempotent
replay made no writes or extra history events. Auxiliary helper lint passed.

The log is `iprodione-fludioxonil-checkpoint.log` under
`reports/resistance-grounding-2026-10-07/`; the complete byte comparison is
`iprodione-fludioxonil-census-proof.json` in the same cache. **Full QC has not
passed**: Python 3.13.12 on macOS x86_64 still lacks the locked RDKit dependency.
The failed installation was not retried or its pin relaxed. No NCBI requests,
source adoption, outreach or GitHub mutations were made. At that checkpoint,
106 PHI-base associations across 47 papers remained unreviewed at this scope;
the broader corpus-wide primary investigation was not complete.

The Kilaru/Guo carboxin follow-up passed its validated-writer canary, independent
before/after comparison and idempotent replay. Exactly 12 pinned records changed;
2,927 remained byte-identical to the prior census. Two associations received
identifier-scope corrections, and 98 older claims received only the shared
review-checksum refresh. All biological source wording, claim order, curator
claims and clinical activities were preserved. The retained historical
checkpoint chain still verifies without rewriting its record pins.

**165 resistance/context tests passed** (495.14 seconds), and **29
activity-publication tests passed** (13.75 seconds). All 2,939 records passed
strict schema validation with zero errors and reproduced exactly from source
and curator inputs. The refreshed census matches all live record hashes.
Independent evidence verification checked three reference proteins, four taxa,
seven UniProt responses, eight citation responses and three primary-text
responses. Missing primary access remains explicit for eight carboxin
associations; no abstract-only mapping was promoted to a curated subject.

**All 38 offline checkpoint stages passed**, including refreshed audits and
historical pins, all-record validation and reproduction, documentation,
provenance, source gates, rendering, lint and whitespace. The actual-publication
audit also passed: all 36 carboxin source rows are present, and 28 reviewed
identifier sets remain in provenance rather than tested-organism cells. Existing
clinical tables, evidence, browser bindings and complete downloads are preserved.
The log is `carboxin-followup-checkpoint.log` under
`reports/resistance-grounding-2026-10-07/`. Auxiliary helper lint passed too.
Full QC has not passed: the current Python 3.13.12 macOS x86_64 environment still
lacks the locked RDKit dependency. No NCBI requests, source adoption, outreach
or GitHub mutations were made.

The preceding carboxin reference-context batch passed its record canary, independent
before/after verification and idempotent replay. A complete byte comparison
against the pre-change census confirmed exactly the 12 pinned records changed;
2,927 remained untouched. Twenty-six associations received scope corrections,
and 72 received checksum-only updates. All existing activities, curator claims,
source allele wording and claim order were preserved. Independent verification
also checked five cached responses, three reference proteins, two taxonomy
entries, and 18 field deposits through 11 proteins and six backgrounds.

**66 identifier-review tests passed** (4.84 seconds), as did **29
activity-publication tests** (8.21 seconds). The initial broad run had **155
passes and one failure** (418.09 seconds): a prose-only guard allowed reviewed
subject names but not reviewed parent-background explanations. The corrected
guard permits only exact pinned text for the matching compound, citation, strain,
allele and phenotype; seven
negative cases reject mismatched identities and unreviewed extra prose.
The complete corrected resistance/context rerun passed **163 tests** (350.98
seconds). **All 37 offline checkpoint stages passed**, including strict schema
validation and exact reproduction of all 2,939 records, refreshed audits,
historical pins, documentation, provenance, source gates, rendering, lint and
whitespace. Its census matched all 2,939 then-current record hashes.

The separate actual-publication audit passed for all 36 carboxin rows: 26 scoped
reference identifier sets remain in provenance rather than tested-organism
cells. Existing clinical tables, evidence, browser bindings and full downloads
are unchanged. Auxiliary verifier lint also passed. The initial and corrected
logs are retained separately as
`carboxin-reference-checkpoint.log` and `carboxin-reference-checkpoint-final.log`
under `reports/resistance-grounding-2026-10-07/`.
Full QC remains unavailable for the separate dependency reason below.

The preceding Rybak reference-context batch passed its record canary, independent
before/after verification, and idempotent replay. A complete byte comparison
against the pre-change census confirmed only the 11 pinned records changed;
2,928 remained untouched. Six associations received scope corrections, and 66
received checksum-only updates. Existing activities, curator claims and source
claim order were preserved.

**155 resistance/context tests passed** (345.33 seconds), including three new
on-disk regression cases; **29 activity-publication tests passed** (12.96 seconds).
**All 36 offline checkpoint stages passed**, including all-record schema
validation, exact reproduction, refreshed discovery/grounding audits, historical
record pins, source gates, documentation, rendering, lint and whitespace.
The log is `reports/resistance-grounding-2026-10-07/rybak-reference-checkpoint.log`.
The separate actual-publication audit verified all six rendered resistance rows:
reference identifiers remain in notes, not tested-organism identifier cells.
Both existing clinical pages retain exact tables, evidence, search-index bindings
and complete record downloads. No full-QC success is claimed.

The preceding clinical batch passed two record canaries, independent verification of
11 before/after record pins and six cached UniProt responses, and idempotent
replay. Five new regression cases check the source scopes, clinical observations
and reseeding. **152 resistance/context tests passed** (452.31 seconds), as did
**29 activity-publication tests** (10.64 seconds). **All 35 offline checkpoint
stages passed**, including schema validation and exact reproduction of all 2,939
records, refreshed audits, historical provenance, documentation, source gates,
rendering, lint and whitespace. The log is
`reports/resistance-grounding-2026-10-07/eddouzi-clinical-checkpoint.log`.
The separate actual-publication audit also passed: both clinical pages match
their full observations, evidence bindings, search indexes and record downloads.
No full-QC success is claimed.

The preceding paired ERG11/yeast subject review passed both record canaries,
independent before/after verification and idempotent replay. Its expanded
regression passed **147 tests** (328.22 seconds); pre-write review tests also
passed (45, with 12 on-disk tests deselected). **All 33 offline checkpoint stages
passed**, including all-record schema validation, reproduction, refreshed
audits, historical provenance checks, documentation, source provenance and
queue, rendering, lint and whitespace. The log is
`reports/resistance-grounding-2026-10-07/azole-yeast-checkpoint.log`.
The additional metadata-only deposit-lead verifier also passed. Auxiliary
verifier line-length findings were corrected; lint and all four affected
independent verifiers passed again with unchanged exported findings.

The previous **32 offline checkpoint stages passed** after the FKS1 reference-context
corrections and five checksum-only record refreshes. The preceding **30 offline
checkpoint stages passed** after the voriconazole subject
corrections, one clinical MIC, and four provenance-only refreshes. The preceding
27-stage checkpoint passed after the cycloheximide correction and final alias batch.
These checkpoints include refreshed
audits, independent export verification, full-corpus schema and reproduction
checks, documentation, provenance, source queue, rendering, lint and whitespace.
This is not a substitute for the unavailable full-QC gate below.

- Closed-schema validation: all 2,939 records, zero errors after curation.
- Corpus reproduction: 2,939 expected and present, no drift or stale paths.
- The previous regression run covered 141 tests across PHI-base reviews/import,
  organismal context and curator grounding: **138 passed and three failed**
  (383.37 seconds). All three failures were in the newly added reseeding test
  fixture, which omitted the other required source-record identities. The
  corrected fixture retains the seeder's fail-closed corpus identity guard.
  All **51 identifier-review tests then passed** (3.31 seconds), including
  the three new on-disk and reseeding cases. Logs are retained separately as
  `balashov-checkpoint.log` and `balashov-checkpoint-final.log` under the local
  research cache. No production gate or scientific assertion was weakened.
- The preceding focused regression covered 138 tests across PHI-base reviews/import,
  organismal context and curator grounding. The initial run had **137 pass and
  one fail** (540.16 seconds): the old prose-only invariant rejected a tested
  strain's name repeated in its explicit review explanation. The check now
  allows only exact pinned subject-review text with matching subject, compound
  and primary citation; arbitrary identity prose remains disallowed. That
  corrected test passed against the full corpus (46.50 seconds). Separately,
  all **48 identifier-review tests passed** (4.11 seconds). The initial failure
  and successful rerun are retained in separate checkpoint logs.
- Previous checkpoint's pre-write regression: **193 tests passed** (737.32 seconds) across
  PHI-base identifier reviews/import, organismal context, curator grounding,
  canonical and alias discovery, and source-queue checks. Only the new on-disk
  cycloheximide regression was deselected before the record write.
  After the canary and checksum refreshes, **all 34 identifier-review tests
  passed** (2.81 seconds), including that on-disk case and three additional
  checks that source mismatches cannot partially mutate a claim.
- Earlier focused regression: **165 tests passed** across PHI-base import and identifier
  reviews, PHI/CARD/HIVDB grounding audits, citation discovery, curator grounding,
  and organismal context after raltegravir model grounding (499.13 seconds).
  After the HCV updates, **27 curator-grounding tests passed** (3.48 seconds),
  including 11 new cases for form warnings, unchanged related structures,
  reference-only crosswalks, taxon scope and reseeding preservation.
  The combined curator-grounding and source-queue suite then passed **53 tests**
  (4.76 seconds on the final rerun), including a new current-deferral versus historical-review check.
  The pyrisoxazole, cerulenin, narlaprevir, three JS67, and raltegravir updates
  were idempotent on replay, with no extra history event. The new dasabuvir,
  paritaprevir and elbasvir updates also replay without writes or history events.
  Full-repository lint and whitespace checks pass.
- Site: regenerated all 2,939 pages; independent `render_pages.py --check`
  confirms the committed-page working tree is in step with the records.
  The new voriconazole activity page and compressed evidence payload preserve
  the clinical isolate, MIC units, assay and historical-interpretation caveat.
  At the preceding checkpoint, its regenerated full-record download independently
  matched the then-current YAML, while the clinical activity payload remained unchanged.
  All six newly reviewed azole/echinocandin pages contain their review notes.
  The latest clinical rebuild regenerated 2,939 pages across seven classes and
  pruned three obsolete artifacts. Independent checks confirm the fluconazole
  and voriconazole tables, qualifiers, unknown categorical call, evidence and
  downloads exactly match the current records. All three Eddouzi-reviewed
  compound pages retain their source-scope explanations.
- Ledger: exact current record membership, unique identifiers, and matching
  SHA-256 digests for all 2,939 records. The 217-row PHI-base audit matches the
  current source inventory. Retained protein crosswalks match the checksummed
  UniProt response.
- PHI-base identifier review: all 217 associations remain; 151 now have no
  identifier-scope decision. The expanded tests cover pinned-source drift, invalid
  decisions, row identity, read races, unchanged unreviewed associations,
  reference-only versus misassigned identifiers, and unchanged claims on a
  source mismatch, explicit tested-subject labels, independent clinical MIC,
  and preservation through reseeding. Independent verification checks three
  subject corrections, one MIC, five current record pins and three cached
  UniProt responses at the preceding checkpoint. The historical FKS1
  verification covers 24 associations, eight retained record pins, one explicit
  deposited-reference crosswalk, and four cached UniProt responses. The historical
  paired verifier covers 24 additional reviews, 36 checksum-only claim refreshes,
  ten record pins, two reference-locus crosswalks and five cached UniProt
  responses. The latest clinical verifier checks six new scopes, 60 checksum-only
  claims, four MICs, two associations, 11 record pins and six cached responses.
  Replay is idempotent. All previous source-review dossiers retain historical pins checked
  against subsequent frozen before-images. Exact tested-derivative protein identifiers
  remain unresolved. Separately, the ERG11 lead verifies 19 deposited-accession
  crosswalks to 18 proteins without inventing a genotype/phenotype subject join.
- Raltegravir: five new regression tests preserve distinct model observations,
  reference-only protein scope, taxonomic rank, biochemical endpoint scope,
  source numbering, and all 35 HIVDB rules through reseeding. Independent
  verification checks the original record, unchanged non-resistance fields,
  the retained original claim, current record digest, and both cached UniProt
  response bodies.
- HCV updates: independent verification checks all three pre-curation git blobs,
  current record digests, unchanged claim fields and history prefixes. All six
  cached UniProt responses reproduce the two reference crosswalks, three taxonomy
  entries and one unresolved reference query. Compound-form warnings do not
  validate or transfer the existing claims.
- PR-39 and daclatasvir: eight new regression cases preserve species rank,
  reference-only protein/strain context, source gene identity, separate clinical
  and reference observations, unchanged unrelated fields and history, and source
  reseeding. Independent verification checks both original git blobs, the exact
  scoped changes, all four cached UniProt responses and current corpus hashes.
  Both updates are idempotent: replay adds no write or curation event.
- CARD audit: snapshot-race tests pass. The refreshed research artifacts
  independently reproduce all 4,182
  raw protein entries, 360 raw taxon entries, 2,002 determinants, and 4,538
  assertion rows. This is reference-link verification, not primary-paper review.
- HIVDB audit: 17 regression tests cover rule/identity drift, inactive taxonomy,
  source-cache corruption, truncated trees, and manifest pins. Independent
  verification checks all 467 rule memberships, 16 record mappings, source
  reference metadata, cached response digests, and current corpus hashes before
  exporting the report. No score rules were changed.
- Discovery: tests cover empty cohorts, offline cache replay, bounded retries,
  response origin, stale census, invalid echoes, truncation, duplicate IDs,
  request bounds, and preservation of all planned record IDs. Independent
  verification checks both historical and current cohorts against their pinned
  censuses and raw cached responses, including each retained citation and every
  ledger row. The main ledger again matches all 2,939 current record hashes.
- All-record name discovery and curation: **108 focused tests passed** (3.23 seconds),
  covering the new name-discovery workflow, the existing canonical client,
  curator grounding and source-queue checks. Added cases preserve all origins,
  existing-claim records, case/stereochemistry, query bounds, source-qualified
  citations, offline behavior and resumable coverage; altered plans and read
  races fail closed. The TSV now exposes canonical-query status so an unknown
  comparison cannot be mistaken for zero added citations. An independent
  verifier reconstructed every live record's names and origins, all shared-name
  flags, query coverage and syntax, cached response digests and echoes, every
  retained citation, summaries and ledger row before export. Verification matched
  all 2,939 post-curation record hashes. The cache-compatibility regression
  pins the pre-alias query text independently of the new shared helper.
- The earlier authoritative `scripts/run_qc.py` passed lint, documentation statistics,
  raw-data provenance, and source-queue checks. It stopped at the curator
  structure gate because `rdkit` is not installed. An isolated locked install
  of `--extra dev --extra chemical-map` failed because pinned `rdkit==2026.3.5`
  has no macOS x86_64 wheel or source distribution. Dependencies and QC gates
  were not loosened. A read-only Docker probe did not return and was stopped;
  no working alternative runtime was established at that historical checkpoint.
  The HDF1 checkpoint above now establishes a temporary runtime with the exact
  RDKit version and passes curator-structure and chemical-map checks without
  changing project pins. Semantic-map staleness remains a separate failure.

**Full QC had not passed at this historical checkpoint.** Passing schema and
reproduction checks did not override the then-failing semantic-map regression. The current
checkpoint above records the latest test and runtime evidence.
No commit, push, GitHub issue, PR, merge, or branch deletion was performed for
this research checkpoint.

## Producer Gene Reference Leads (2026-10-09)

The next bounded review covers valanimycin (`CHEBI:133621`), zorbamycin
(`CHEBI:67811`) and efrotomycin (`antibioticmech:aro-5d5ecfee72`). All 2,939
records remain in scope. This is reference and citation triage, not completed
primary review or new biological curation. The
[identifier dossier](2026-10-09-producer-gene-reference-grounding.json)
pins the exact structures, sequence-free UniProt receipts and access limits.

- **Valanimycin:** `UniProtKB:Q9LA76` cites `PMID:10708373` and retains the
  reference strain label `MG456-hf10`, but its gene-symbol field is empty.
  The exact `vlmF` search returned no entries; the broader compound search
  found this candidate. Its `AY116644/AAN10244.1` cross-reference does not
  establish equivalence to the paper's `AF148322` deposit. Keep the producer
  separate from the laboratory hosts and the proposed efflux interpretation
  separate from directly demonstrated mechanism. Only the publisher abstract
  and accession note were inspected; the free full-text endpoint returned 403.
  [Primary publisher](https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-146-2-345).
- **Zorbamycin:** `UniProtKB:B9UIZ4` explicitly cites `PMID:26512730` and links
  `EU670723/ACG60763.1`. Its current species reference is `NCBITaxon:28893`,
  *Streptomyces pilosus*. The paper's *S. flavoviridis* appears under UniProt
  `otherNames`, not `synonyms`; neither this name association nor the citation
  assigns an experimental strain or allele. Primary Results remain unreviewed:
  the EMBL-EBI full-text request returned 500.
  [Primary citation](https://pubs.acs.org/doi/10.1021/acs.biochem.5b01008).
- **Efrotomycin:** `PMID:36445346` concerns distinct congeners and describes
  `efrT` as putative. Its production context does not establish resistance to
  this record's exact structure. Exact-gene and compound-keyword UniProt
  searches both returned no entries, not evidence of biological absence.
  Full Results were not inspected; the congener join remains open.
  [Primary abstract](https://pubs.acs.org/doi/10.1021/acs.jnatprod.2c00986).

Eight successful UniProt metadata requests are pinned to release `2026_03`;
all six protein-search result sets fit in one page. Only the two focal
reference candidates are exported. No new sequences, variant specifications,
protocols or numerical resistance measurements are included. The preservation
audit includes ignored files and checks every record against the prior census;
there are no record edits or curation events in this batch. NCBI and #1040
remain deferred. The latest full authoritative QC is still the Posteraro
checkpoint; this research-only review does not claim a new full-QC run.

Verification: **144 focused tests passed**, covering the new producer-reference
regressions plus the Posteraro and shared PHI review tests. The offline export
replay validates cached response digests, pagination totals, reference citations
and taxonomic name fields. It reproduced the dossier byte-for-byte, verified
all **2,939 record hashes**, and preserved **6,704 pre-existing files** across
the protected roots; this report is the sole allowed pre-existing edit.

## Producer Primary Context Follow-up (2026-10-09)

The [follow-up dossier](2026-10-09-producer-primary-context.json) advances the
preceding reference checkpoint without overwriting it. RCSB PDB entries
`4IAG` and `5CJ3` explicitly map their protein entity to `UniProtKB:B9UIZ4`.
The `5CJ3` component `52G` has the exact zorbamycin record InChIKey. RCSB's
source-organism metadata retains *Streptomyces flavoviridis* with TaxID 28893,
while the current UniProt name is *S. pilosus*. This verifies a structural
reference and ligand-component join, not a whole-cell resistance assignment.
[PDB 5CJ3](https://www.rcsb.org/structure/5CJ3),
[PDB 4IAG](https://www.rcsb.org/structure/4IAG).

Primary Results from `PMID:25299801` are now reviewed through publisher-indexed
text. The dossier separates biochemical findings, compound forms and
producer-derived subjects across zorbamycin, bleomycin B2 and phleomycin D1;
figure and supplement review remain pending.
[Primary paper](https://pubs.acs.org/doi/10.1021/bi501121e).
The exact `tlmB` UniProt symbol hit belongs to a different donor and citation;
it is rejected for this paper. `UniProtKB:Q53796` is an older donor-matched
reference lead, not an established 2014 experimental accession. Generic
same-species and other-species hits remain unassigned.

The Rice manuscript request returned a challenge, and CiteSeerX's explicit
archive redirect returned 404. No access control was bypassed. The 2015 full
Results and valanimycin primary Results remain unresolved. No biological
records changed; no NCBI request or source adoption occurred. All 2,939
records remain in the ongoing investigation.

Verification: **54 focused tests passed** across this dossier, the preceding
producer references, LmrC context and Posteraro grounding. Ruff and
`git diff --check` passed. Offline replay reproduced the export byte-for-byte,
verified every record hash, and preserved **6,706 pre-existing protected files**
with ignored files included. This report is the sole pre-existing edit in
this batch. Full authoritative QC was not rerun for these research-only changes.

## Combined Progress Index (2026-10-09)

`scripts/summarize_resistance_progress.py` reconciles existing research exports
against all 2,939 collection-loaded current records, without network requests
or biological edits. The [initial TSV](2026-10-09-resistance-progress.tsv) and
[descriptor](2026-10-09-resistance-progress.json) preserve historical
exports rather than replacing their hashes or retroactively changing statuses.
In particular, the old census's `PENDING_DISCOVERY` means no existing resistance
assertion or genotype rule; it is not used to describe the current search stage.

The index confirms 16,030 recorded names and 7,469 initial query memberships.
All 612 expanded query-record memberships, representing 611 distinct query
traversals, are complete in the pinned selected ledger. These are search
operations, not verified findings. Twenty-five current record hashes differ
from the historical name-search plan, but identities, names, name provenance,
shared-name ownership and query text still match. Historical hashes are retained.

The source layers remain separate: 4,538 CARD assertions across 2,002 distinct
terms, with reference candidates for 978 terms and no explicit link for 1,024;
217 PHI-base associations, with 185 identifier-scoped decisions and 32 pending;
and 467 HIVDB source rules. CARD candidates occur on 169 records. Reference
accessions and taxonomy are not experimental allele or organism assignments.
Per-record CARD term counts overlap and must not be summed as unique terms.
At that checkpoint, corpus totals were 4,788 resistance assertions and 467 genotype rules.
All whole-record primary-review statuses remain `OPEN`.

At this checkpoint the generator used the public Posteraro census ledger, not
an ignored cache; the later canthin checkpoint advances that input and retains
these initial outputs unchanged.
It checks source inventory pins, source-row review decisions,
assertion membership, exact rule identities, query memberships and both initial
and final record hashes. Its filesystem census includes ignored and hidden
YAML files. It exports only stage counts, identifiers and provenance, not
sequences, variant specifications, assay values or new biological claims.
Offline reproduction of the latest checkpoint is available with:

```bash
.venv/bin/python scripts/summarize_resistance_progress.py --check
```

Verification: **251 focused tests passed**, including the 36 new progress-index
tests and the alias-discovery, CARD, HIVDB and PHI-base review suites. The live
integration test reproduced both exports byte-for-byte with HTTP requests
disabled. All 13 pinned inputs are outside gitignore. Adversarial cases cover
missing or duplicate memberships, changed names and provenance, mismatched
reference links, incomplete cursors, rule identity drift, review promotion,
and ignored/hidden YAML additions. Ruff and `git diff --check` passed.
No biological record changed; the preceding protected-file snapshot still
matches 6,706 pre-existing files, with this report the sole pre-existing edit.
Full authoritative QC was not rerun for this metadata-only checkpoint.

## Transport-Related Primary Context (2026-10-09)

The [new dossier](2026-10-09-transport-primary-context.json) examines three
records and four publications, retaining five reference proteins from UniProt
release `2026_03`: FLR1/P38124, YAP1/P19880, YCF1/P39109, RTA1/P53047 and
bmrA/O06967. UniProt taxonomy verifies the species and reference-strain contexts,
not experimental allele identity. No NCBI endpoint was contacted.

For **canthin-6-one**, the author's university thesis contains the primary
paper. Table 1 and Figures 1, 3, 4 and 5 were visually inspected. The
Yap1/Flr1 association is ready for qualitative curation, retaining negative
comparisons and the baseline-growth caveat. Table 2's conflicting FLR1 locus
label is not promoted to an alias. The S288c reference is not substituted for
the distinct experimental backgrounds.
[Dejos et al.](https://doi.org/10.1016/j.febslet.2013.07.040)

For **7-aminocholesterol**, the 1996 abstract's deposit identifier joins to
P53047, but UniProt associates that citation with FL100 rather than its current
S288c entry context. The 2012 primary Results and Figures 2 and 7 were inspected;
subject/form questions remain, and RTA1 is not curated as a proven drug-efflux
mechanism. [Soustre et al.](https://doi.org/10.1007/s002940050110),
[Kolaczkowska et al.](https://doi.org/10.1111/j.1567-1364.2011.00768.x)

For **cervimycin C**, indexed primary Results distinguish experimental
derivatives from the parent and reference genome. The unpublished producer
aside is excluded. Direct PDF retrieval failed, leaving figure/supplement
review open. [Krugel et al.](https://doi.org/10.1111/j.1574-6968.2010.02143.x)

Five other discovery citations remain pending, not rejected by title. This
research checkpoint changes no biological records and completes no whole-record
review. The canthin curation decision is a next action, not an applied change.

Verification: 89 focused tests passed across transport context, producer context,
producer grounding and the progress index. Offline replay reproduced this
research checkpoint and verified all record hashes. The following curation is
a separate checkpoint; it does not rewrite this historical research disposition.

## Canthin Gene Associations (2026-10-09)

The [curation dossier](2026-10-09-canthin-curation.json) applies the two
qualitative associations supported by the preceding primary review to
CHEBI:3363, retaining its exact InChIKey. YAP1 and FLR1 share one study;
the two assertions are not independent study replications or evidence of species-wide resistance.
YCF1 remains a negative comparison. Baseline growth complicates the YAP1-loss
comparison, and the basal FLR1-loss comparison was negative in its tested context.
The conflicting Table 2 locus label remains provenance, not a new gene alias.

Species is grounded to NCBITaxon:4932. UniProtKB:P19880 and UniProtKB:P38124
and reference-strain NCBITaxon:559292 appear only as reference context;
no exact experimental allele, protein accession, strain TaxID, genome, numeric
AST, clinical category or direct drug target was assigned. The existing source
identity and curator status are unchanged. One curation event records the edit.

The [reconciliation](2026-10-09-canthin-checkpoint-reconciliation.json) confirms
that only canthin-6-one changed among all 2,939 biological records. Its
[new census ledger](2026-10-09-canthin-resistance-grounding.tsv) changes one row
and retains all historical exports. The refreshed combined progress index now
has 26 records changed since the original name-search plan; names, identities
and query memberships remain unchanged. All whole-record review statuses stay
open. The coarse census column `primary_papers_pending` is not a claim that the
documented qualitative canthin review never occurred.

The [verification checkpoint](2026-10-09-canthin-verification.json) records
**63 focused tests passed** and **all 11 authoritative QC gates passed**, including
**2,299 tests passed, 3 skipped and 1 warning** in the full suite. The skips are
empty command-frontmatter parameter sets; the warning is the existing LinkML
dataclass-extension deprecation. Closed-schema validation and corpus reproduction
passed for all 2,939 records, with no missing records or field drift. Source
provenance, source gates, chemical-map and generated-site checks also passed.

The semantic map was genuinely refreshed: one changed document was re-encoded
locally, 2,938 unchanged vector rows were retained byte-for-byte, and 16 control
documents matched within tolerance. A complete PaCMAP projection now carries
fingerprint `6ef789f99f7de573`. The rendered payload and all 2,939 record links
were checked offline; no live-browser verification is claimed. The protection
audit includes ignored files and confirms 6,660 pre-existing files unchanged,
excluding this report and the eight expected record/publication/generator edits.
All other biological records and curation inputs remain unchanged. NCBI was not
contacted; no source adoption or GitHub mutation occurred. This verifies the
curation checkpoint, not exact experimental alleles or completed corpus research.

A bounded follow-up of PMID:41108078 inspected the primary publisher's indexed
abstract and screening/Introduction context, which identify canthin-6-one as N1
in ERAP1-focused cancer research. This establishes a compound-name match but
does not establish a microbial resistance observation from the inspected text.
Direct publisher and Uniupo landing-page retrieval returned HTTP 403; the
Sapienza repository lists its accepted manuscript under embargo until
2026-10-17. No embargo or access restriction was bypassed. The citation remains
pending for full relevance review, not rejected from its title; no ERAP1
resistance assertion or target was curated.
[Publisher](https://www.sciencedirect.com/science/article/pii/S1525001625008573),
[repository status](https://iris.uniroma1.it/handle/11573/1753522).

The worklist also retains three ChEBI-linked citations outside the two name-query
hits. A primary-publisher abstract-level triage on 2026-10-09 distinguishes their
scope without declaring full reviews or adding resistance claims:

| Citation | Inspected scope and disposition |
| --- | --- |
| PMID:19325221, [Tada et al.](https://www.jstage.jst.go.jp/article/shokueishi/50/1/50_1_16/_article/-char/en) | Constituent identification in commercial bittering extracts; compound occurrence is not resistance evidence. |
| PMID:21134431, [Ferreira et al.](https://www.sciencedirect.com/science/article/pii/S0378874110008172) | Antiparasitic activity context. Keep leaf-extract and purified-compound evidence distinct; no resistance-gene link established from the inspected abstract. |
| PMID:21236329, [Almeida et al.](https://www.sciencedirect.com/science/article/pii/S0378874111000109) | Gastroprotective pharmacology; neither the abstract nor the indexed context inspected establishes microbial resistance. |

These are bounded relevance observations, not claims that a full article or
all supplementary material contains no relevant evidence. No new taxon, protein,
allele, assay value or clinical interpretation was assigned from these leads.

A closer read of the cached 7-aminocholesterol primary HTML separates JD52
purification/fractionation work (Methods and Figure 1) from the FY-background
growth assays explicitly named in Figure 2's caption. Their proximity in the
Results does not by itself establish an author error or make the subjects
interchangeable. The earlier subject-label caveat is therefore a warning against
joining distinct assays, not a proven typo. Exact experimental identity and
stereospecific compound-form questions remain open; no record or historical
dossier was rewritten from this clarification.
[Kolaczkowska et al.](https://academic.oup.com/femsyr/article/12/3/279/592505)

## CARD Structural References (2026-10-09)

The [metadata export](2026-10-09-card-structure-links.json) and
[offline audit](../scripts/audit_card_structure_links.py) inspect the pinned
ARO OWL serialization's direct `hasDbXref` statements on all **1,024** terms
without an explicit UniProt CARD cross-reference. This scan includes the
ignored ontology cache. Exactly six terms have direct cross-references, all
to PDB; the remaining **1,018** have none in that specific field and snapshot.
This is not an absence claim about definition citations, ancestors, other
resources, possible proteins or biological resistance.

The six references occur in **20 existing CARD assertions across 17 records**.
All 17 complete records were loaded through the collection-aware loader;
chemical identities, source ownership and term membership were checked.
RCSB GraphQL requests selected only entity identifiers, source organisms,
reference accessions, revisions and bibliography. UniProt metadata-only
queries verified all six reciprocal PDB links in release **2026_03**.
Their gene names and taxonomy remain database reference context.

| ARO term | PDB entity | UniProt reference | Reference taxon | Disposition |
| --- | --- | --- | --- | --- |
| ARO:3000309, emrD | 2GFP_1 | P31442 | NCBITaxon:83333, E. coli K12 | Gene-level structural reference only; the PDB entity reports species 562. |
| ARO:3000866, oleI | 2IYA_1 | Q3HTL7 | NCBITaxon:1890, S. antibioticus | Explicit structural reference, not an experimental allele or phenotype. |
| ARO:3001307, vgbA | 2Z2P_1 | P17978 | NCBITaxon:1280, S. aureus | Inactive structural reference; UniProt uses vgb. |
| ARO:3002547 | 1V0C_1 | Q6SJ71 | NCBITaxon:562, E. coli | Exact allele unresolved; a structural reference is not the variant assignment. |
| ARO:3002637 | 3N4T_1 | O68183 | NCBITaxon:37734, E. casseliflavus | ARO/PDB IVa versus UniProt Id nomenclature requires primary review. |
| ARO:3004042, E. cloacae acrA | 2F1M_1 | P0AE06 | NCBITaxon:83333, E. coli K12 | Reject assignment to the focal organism; retain the source cross-reference. |

The organism mismatch in the last row is explicit in the deposition metadata;
UniProt also points to the different CARD identifier `ARO:3004043`. This does
not establish that the ontology's structural cross-reference is erroneous:
it establishes that it cannot identify the named E. cloacae protein.
[RCSB 2F1M](https://www.rcsb.org/structure/2F1M)

`2Z2P_2` is a separate polymer entity with no UniProt reference. Its source
TaxID 68212 resolves through UniProt taxonomy to Streptomyces graminofaciens;
the PDB source spelling is retained separately. That entity's organism must
not be transferred to the enzyme in `2Z2P_1`. The deposition identifies the
enzyme structure as inactive, so neither a resistance phenotype nor an exact
active allele follows from its protein reference.
[RCSB 2Z2P](https://www.rcsb.org/structure/2Z2P)

The 1V0C literature abstract distinguishes the wild-type structures from the
variant model. Q6SJ71 aggregates source gene-name annotations; those names
do not settle which exact experimental allele a CARD term denotes.
[RCSB 1V0C](https://www.rcsb.org/structure/1V0C)
Likewise, the IVa/Id naming difference remains explicitly unresolved here,
not silently normalized or interpreted as a functional difference.
[RCSB 3N4T](https://www.rcsb.org/structure/3N4T)

PDB citations remain bibliography, not completed primary reviews. In particular,
2GFP cites PMID:16675700, while that PMID is absent from the selected P31442
reference metadata. The two citation lists are retained independently; this
is not evidence of retraction, disagreement or biological absence.
[RCSB 2GFP](https://www.rcsb.org/structure/2GFP)
The oleI reference similarly remains scoped to its explicit database link.
[RCSB 2IYA](https://www.rcsb.org/structure/2IYA)

All **2,939** biological record hashes still match the canthin checkpoint.
No biological record, source inventory, curation event, page or embedding was
changed. The original 978/1,024 direct UniProt CARD-link split is unchanged;
these indirect structural paths must not inflate that count. No whole-record
primary review was completed, and no NCBI request or source-terms work occurred.
The public export excludes sequences, variant specifications, protocols,
coordinates and numerical susceptibility measurements.

Verification: the canary preceded the complete export; **159 focused tests**
passed, including an offline replay and entity/taxon-separation regressions.
Repository-wide Ruff and the README-statistics check passed. Full authoritative
QC was not rerun for this research-only change; the prior canthin QC result
remains a historical curation checkpoint, not a new full-suite result.
The [verification receipt](2026-10-09-card-structure-verification.json) pins
the export, script, tests and preservation check.

## Oleandomycin Biochemical Curation (2026-10-09)

Follow-up of ARO:3000866 / PDB:2IYA resolves primary biochemical evidence for
the existing oleandomycin structure, CHEBI:16869, Standard InChIKey
`RZPAKFUAFGMUPI-QESOVKLGSA-N`. The [curation dossier](2026-10-09-oleandomycin-curation.json)
retains six versioned UniProt references and three complete metadata-query receipts.

The [1998 primary paper](https://onlinelibrary.wiley.com/doi/full/10.1046/j.1365-2958.1998.00880.x)
reports OleI/OleD biochemical glycosylation and reduced activity of the modified
product in a cell-free assay. Its negative host comparison and the opposite
OleR reactivation direction are retained. Donor and heterologous host are not
interchangeable. Relevant Results and figure legends were inspected through
publisher-indexed text; the figures themselves were not visually inspected.
The paper's AF055579 deposit maps through UniProt to O68841 for OleI.
OleN2's biosynthetic annotation is not a positive resistance finding.

The [author-hosted 2007 paper](https://users.ox.ac.uk/~dplb0149/publication/pub83.pdf)
provides wild-type biochemical activity in Tables 1 and 3. Those tables and
Figures 1 and 2 were visually inspected; numerical results and engineering
details are not exported. Its published correction was read and visually
checked on journal page 9911, BIOCHEMISTRY section, in a
[university-hosted journal copy](https://ftp.forest.sr.unh.edu/Ollinger/PapersforFranklin/Bala%20et%20al.%202007%20PNAS_Albedo.pdf).
That notice changes author-contribution credit, not the biochemical results.
Supplementary material was not inspected and is not a basis for these claims.

| Gene | Earlier reference | Later reference | Disposition |
| --- | --- | --- | --- |
| oleI | O68841, AF055579 / AAC12648.1 | Q3HTL7, DQ195535 / ABA42118.2 | Distinct reference deposits; no exact experimental allele assignment |
| oleD | Q53685, Z22577 / CAA80301.1 | Q3HTL6, DQ195536 / ABA42119.2 | Distinct reference deposits; no representative chosen |
| oleR | O68843 | Not selected | Reactivation, not another inactivation determinant |
| oleN2 | O68842 | Not selected | Biosynthetic annotation, not demonstrated resistance |

The earlier OleD study, PMID:8244027, remains a UniProt bibliographic lead;
its DOI route was unavailable through the web tool in this pass. No primary
finding from that uninspected paper was added.

Two curator-owned `ANTIBIOTIC_INACTIVATION` assertions were added through a
validated canary and a single curation event. All 30 CARD-owned assertions and
other record fields were preserved. UniProt accessions and the active species
NCBITaxon:1890 are reference-only context, not experimental subject fields.
No allele, strain TaxID, genome, BioSample, whole-cell phenotype or numerical
AST was assigned. Source routes for OleB and OleC were not reinterpreted.

The [checkpoint reconciliation](2026-10-09-oleandomycin-checkpoint-reconciliation.json)
checks all 2,939 current record paths and hashes, including ignored files:
one record changed and 2,938 remained byte-identical. This narrow curation does
not complete oleandomycin's other source assertions or any whole-record review.
All 2,939 embedding documents are unchanged: the existing builder takes only
the first six resistance labels, so the appended curator assertions are outside
its projection. Vectors, metadata and semantic map retain their verified bytes
and fingerprint `6ef789f99f7de573`; no re-encoding or fingerprint rewrite occurred.
The generated record page, not the semantic projection, carries the new claims.
Verification: **78 focused tests passed, one skipped**. All **11 authoritative
QC stages passed**, including **2,334 tests passed, four skipped, one warning**,
strict validation of all 2,939 records, exact corpus reproduction, chemical-map
consistency and generated-site agreement. One skip is the historical structural
audit replay after the corpus changed; its public invariants still run. The
other three are empty skill-path parameter sets. The warning is the existing
LinkML dataclass-extension deprecation. The
[verification receipt](2026-10-09-oleandomycin-verification.json) records the
preservation, rendering and embedding checks. No live browser QA is claimed.

## Structural Reference Follow-Up (2026-10-09)

The [identity follow-up](2026-10-09-structure-primary-context.json) covers the
five remaining paths from the structural audit: **19 CARD assertions across
16 records**. Fresh identifier-only UniProt queries returned all five requested
entries in release `2026_03`. Their reference organisms and archive identifiers
remain separate from experimental subjects and exact alleles.

| Reference path | Follow-up disposition |
| --- | --- |
| `emrD` / `P31442` | Europe PMC lists an erratum in Science 317:1682 (2007). Its content and the original Results remain unreviewed; no retraction or biological consequence is inferred. |
| `vgbA` / `P17978` | Retain the inactive structural entity and its separate enzyme taxon. A named quinupristin lead does not validate every streptogramin congener. |
| `AAC(6')-Ib-cr1` / `Q6SJ71` | The wild-type structural reference is not an exact cr1 assignment. Preserve all 27 archive links, including two proteins on one archive accession; later-deposit citation comments are not original assay subjects. |
| `APH(2'')-IVa` / `O68183` | The historical Id-to-IVa name relation is verified from the primary nomenclature Discussion. Compound-specific assay and experimental-identity review remain open. |
| E. cloacae `acrA` / `P0AE06` | Retain the rejected cross-species mapping: this is an E. coli reference, not an E. cloacae assignment. |

The nomenclature finding comes from the final Discussion paragraph of
[Toth et al. (2009), PMID:19158087](https://www.sciencedirect.com/science/article/pii/S0021925820325497),
which explicitly renames Id to IVa. Publisher-indexed primary text was inspected;
Table 5 was not visually inspected, and no complete paper, figure or supplement
review is claimed. UniProt's NC95 citation context remains attached to the
earlier reference, not silently transferred to the structural paper's assay.

Primary publisher access was unavailable for the five structural papers. A
Europe PMC HTML canary returned a challenge; no remaining HTML batch or bypass
was attempted. EMBL-EBI bibliographic metadata was retrieved, but the OA XML API
was not used because these records are outside its indicated OA slice. This is
an access limit, not evidence that the biological claims are false. Author
bibliographies did not supply a reviewed full-text copy through the inspected
links; their NCBI links were not followed.

No biological claims or curation events were added in this follow-up. Generic
gentamicin was not mapped to exact gentamycin A, and the existing patricin A/B
structure-collision questions remain open. All 2,939 record hashes still match
the oleandomycin checkpoint. The dossier records per-assertion dispositions but
does not change the combined stage-progress ledger or complete any whole-record
review. Source inputs, rendered pages and embeddings are unchanged.

Verification: **94 focused tests passed, one historical replay skipped**;
repository lint, generated documentation statistics and whitespace checks passed.
The [verification receipt](2026-10-09-structure-primary-verification.json) pins
the new artifacts and preservation checks. Full authoritative QC was not rerun
for this research-only addition; the last biological curation's full QC remains
the oleandomycin checkpoint above. No live browser verification is claimed.

## Transport Lead Follow-Up (2026-10-09)

The [primary-context dossier](2026-10-09-transport-followup-context.json) follows
four pending papers across **19 records**: 7-aminocholesterol, seven cervimycins
and eleven tunicamycin records. This is bounded evidence review, not completion
of those records or the full 2,939-record investigation.

| Context | Finding and curation limit |
| --- | --- |
| RTA1 / 7-aminocholesterol | The primary locus `CNAG_03091` maps to reference `UniProtKB:J9VUL5`, H99 `NCBITaxon:235443`. Active material, control and derivatives remain distinct; exact chemical and experimental-allele assignment is held. |
| RTA2 / 7-aminocholesterol and tunicamycin | `UniProtKB:Q59Q40`, SC5314 `NCBITaxon:237561`, is a name-based reference candidate. The paper tests both compounds, but has conflicting strain labels. Commercial tunicamycin is not congener-resolved. |
| Cervimycin C/D | Source-reported SG511 reference genome `NZ_CP076660.1` and study `PRJNA852436` have different scopes. Neither identifies every tested isolate. No C/D finding is propagated to the other five congeners. |

Relevant primary text was inspected in the
[RTA1 paper](https://www.mdpi.com/2076-0817/11/11/1239),
[RTA2 paper](https://academic.oup.com/femsyr/article/15/8/fov095/2467771),
[2022 cervimycin paper](https://journals.asm.org/doi/10.1128/spectrum.02567-22)
and [2024 follow-up](https://journals.asm.org/doi/10.1128/msphere.00764-23).
RTA1 Figures 3/4 and supplement Figure S8/Table S2, and RTA2 Figure 2, were
visually inspected. The imine supplement's conflicting formula fields are
retained, not repaired. Cervimycin figures and the 2022 supplement PDF were not
visually inspected; its earlier indexed Table S2 text is explicitly distinguished.
Later reopening and screenshot attempts failed. No access restriction was bypassed.

RTA2's MIC80 endpoint in micromolar units is not converted to mass concentration
for an unresolved mixture. Growth images are not MIC values. Cervimycin's
negative comparisons and reused 2022 data remain separate from new evidence;
susceptibility modifiers are not automatically direct drug targets. The two
complete SG511/archive UniProt queries returned no hits, which does not prove
protein absence. No other strain's reference was substituted.

No biological assertions or curation events were added. All 2,939 record hashes,
source inputs, pages and embeddings remain unchanged. No NCBI endpoint requests,
outreach, #1040 work or reuse-terms reassessment occurred. Exact experimental
alleles, chemical identities and the broader primary review remain open; the
combined stage ledger is unchanged.

Verification: **96 focused tests passed**; repository lint, documentation
statistics and whitespace checks passed. The
[verification receipt](2026-10-09-transport-followup-verification.json) records
source-cache agreement and preservation checks. Full authoritative QC was not
rerun for this research-only addition; the last biological checkpoint remains
oleandomycin. No live browser verification is claimed.

## Borrelidin Primary Context and Curation (2026-10-09)

The [primary-context dossier](2026-10-09-borrelidin-primary-context.json) reviews
bounded sections of four primary papers and grounds **six UniProt references**.
The exact compound is borrelidin, **CHEBI:78661**, neutral acid, with existing
Standard InChIKey `OJCKRNPLOZHAOU-JTHVHBRGSA-N`. Its previously curated
Phytophthora sojae molecular target is preserved without modification.

| Primary context | Finding and curation limit |
| --- | --- |
| Olano 2004, PMID:15112998 | The paper reports borO-associated resistance in a laboratory host derived from S. albus J1074, with **data not shown**. Target replacement and native self-resistance are proposed, not directly demonstrated. One qualified UNKNOWN-route assertion was curated. |
| Ruan 2005, PMID:15507440 | The archaeal enzyme comparison contains both relatively insensitive and inhibited references. It does not support domain-wide or whole-cell resistance. Five publication-linked UniProt entries remain references, not experimental allele assignments. |
| Qiao 2024, PMID:39014102 | A borrelidin-specific biochemical section is relevant despite the obafluorin-focused Introduction. ObaO and BorO are distinct; biochemical susceptibility is not a clinical or whole-cell phenotype. |
| Liu 2026, PMID:41773311 | Subject and assay-scope review shows that the listed MIC panel tests seven other antibiotics, not borrelidin. A reference chromosome and study project do not identify every derivative genome or establish an isolated causal effect. |

The [2004 institutional PDF](https://digibuo.uniovi.es/dspace/bitstream/handle/10651/41688/1-s2.0-S1074552103002977-main.pdf?sequence=1)
was inspected at the relevant Results, Figure 1, Table 1 and accession statement;
Figure 1, Table 1 and Results page 92 were visually checked. The
[2005 author-uploaded primary text](https://www.researchgate.net/publication/8210679_A_Unique_Hydrophobic_Cluster_Near_the_Active_Site_Contributes_to_Differences_in_Borrelidin_Inhibition_among_Threonyl-tRNA_Synthetases)
was read without a successful native PDF download or visual figure review.
The [2024](https://doi.org/10.1038/s42003-024-06559-x) and
[2026](https://doi.org/10.1093/g3journal/jkag046) papers were inspected through
licensed EMBL-EBI OA XML. No supplement review or complete-paper review is claimed.
The 2004 bibliographic comment listing is not labelled an erratum or retraction;
its content remains uninspected.

Donor **UniProtKB:Q70HZ0**, entry 112/sequence 1, links borO to archive
`AJ580915` / `CAE45679.1` and source strain Tu4055. Donor **NCBITaxon:146923**
is not the tested host. **NCBITaxon:1888** is retained only as a species-name
reference; all three J1074 taxonomy candidates remain separate, with no chosen
experimental strain or genome. Table 1 homology hits are not BorO accessions.
The five biochemical references retain entry/sequence versions and archive
flags, including two `ALT_INIT` flags. Halobacterium NRC-1's no-rank TaxID has
a strain-ranked parent; its species ancestor is not inferred from that parent.

The validated canary and production write preserve source ownership, existing
target/chemical fields and all prior history, adding one meaningful event.
Fresh-seed merging preserves the entire curated record. The first private
canary check incorrectly supplied an already curated record as its seed; that
test setup was corrected before the production write, without changing merge code.
The private staging snapshot also sorted YAML keys. A validated serialization
correction restored the original field order without changing the claim or
adding another event; the original record bytes are preserved as a prefix.
The [census reconciliation](2026-10-09-borrelidin-checkpoint-reconciliation.json)
verifies all **2,939 records**, with **2,938 byte-identical** to the prior checkpoint.

Fourteen discovery papers still need primary review, and the existing target
paper was not rereviewed for resistance. All whole-record reviews remain open.
No sequences, variant specifications, constructs, protocols, numerical AST or
combination designs were exported. No NCBI endpoint request, outreach, #1040
work, reuse-terms reassessment, new source adoption or GitHub mutation occurred.
Verification: **173 focused tests passed**. All **11 authoritative QC gates
passed**, including **2,376 tests**, strict validation of all 2,939 records with
zero errors, exact source reproduction, chemical-map consistency and generated
site checks. Four tests were skipped: one historical-cache replay after corpus
change and three empty skill-path parameter sets. One dependency deprecation
warning remains; no test failure was suppressed.

The changed borrelidin search document was genuinely re-encoded with the local
pinned BGE model, with 16 control rows checked. All **2,938 other vector rows**
remain byte-identical. The full PaCMAP projection was rebuilt with seed 42;
that checkpoint's semantic fingerprint is `9abdb4c539712d79`. The
[verification receipt](2026-10-09-borrelidin-verification.json) binds the
curation, full census, research context, test outputs and preservation checks.
The rendered map payload and all 2,939 record links were checked. No live
browser verification or independent external review is claimed.

## Platensimycin and Platencin (2026-10-09)

The [primary-context dossier](2026-10-09-platen-primary-context.json) covers
12 discovery candidates for two existing neutral-acid records: platensimycin,
**CHEBI:68236**, `CSOMAHTTWTVBFL-OFBLZTNGSA-N`, and platencin,
**CHEBI:68241**, `DWUHGPPFFABTIY-RLWZQHMASA-N`. Eleven candidates have fresh
MED bibliographic metadata; `CBA:662853` remains a separate unreviewed candidate,
not a failed or silently discarded MED lookup. Two papers received bounded
primary review, not complete paper or supplement review.

The [2014 accepted author manuscript](https://artefacts-discovery.researcher.life/full_text/DA-2/3f/3ff1fecd75a737289fc93d1193afee9f/full_text/2d1c5caefbe881a219fe0969de0b5e10.pdf)
was read at the relevant Results, Discussion and accession statement. Its title
page, Figures 1 and 2, and Table 1 were visually inspected. The original
publisher endpoint returned 403; no access restriction was bypassed. The copy
is explicitly an unedited accepted manuscript, not the final publisher version;
no article text, figures or supplementary content is republished.

Four qualitative claims retain the source-reported laboratory subjects and
separate them from their donor and host background. The fabF-associated
platencin response remains **partial resistance / reduced susceptibility**.
The coarse routes are the authors' interpretation, not independent kinetic
validation or exact-allele grounding. Negative native-gene comparisons are not
promoted to positive claims; a multi-gene native deletion is not treated as
single-gene necessity, and PtnP3 is not substituted for tested PtmP3.

**UniProtKB:D8L2W8**, entry 45/sequence 1, has no gene-name annotation in the
selected metadata. It nevertheless matches the paper's `ACS13710` reference
through `FJ655920` / `ACS13710.1`; its earlier citation identifies MA7327.
This is donor-reference grounding, not an experimental protein assignment.
The earlier cited paper was not independently reviewed. The separate donor
gene archives are not genomes. Seven current fabF/fabH name matches belong to
DSM 40041, not MA7327, and remain unselected. All five UniProt searches were
complete for their exact query; zero gene-name or citation hits did not prove
protein absence.

**NCBITaxon:58346** is a donor species reference. **NCBITaxon:1888** and the
three conflicting J1074 taxonomy candidates are reused from the pinned prior
checkpoint; no strain representative, derivative TaxID or genome was selected.
The [2015 publisher paper](https://journals.asm.org/doi/10.1128/aac.04179-14)
has distinct laboratory subject and FabH contexts. Its cerulenin negative
comparison is condition-specific and does not negate existing B. subtilis
evidence. Indexed subject-to-alteration labels need visual adjudication before
any exact allele join. The cerulenin record is unchanged. No thiolactomycin
record was found in the filename/content search of `data/antibiotics`, including
hidden and ignored files; none was added.

Both canaries passed the validated writer, exact round-trip, fresh-seed merge
and original-byte-prefix checks before production writes. Existing MIBiG
producer evidence, chemical fields, source slices and prior history are
preserved; each record receives one meaningful event and remains SEEDED.
The [census reconciliation](2026-10-09-platen-checkpoint-reconciliation.json)
checks all **2,939 records**, with **2,937 byte-identical** to the prior checkpoint.
Nine MED candidates and one CBA candidate still need primary review. All
whole-record reviews remain open. No sequence, variant specification, construct,
protocol, numerical AST or combination design was exported. No NCBI endpoint
request, outreach, #1040 work, terms reassessment, source adoption or GitHub
mutation occurred.

Verification: **155 focused tests passed**, including the eight new regression
tests. The first full run detected a stale handwritten count in `NEXT_TASKS.md`:
405 records with target or resistance evidence became 407. The count was
corrected without changing the original test. The task-owned failed worker was
terminated and that incomplete attempt retained separately; its failure was
identified from collected test order and progress, not a completed traceback or
JUnit report. The corrected regression passed in isolation and in a fresh full
run of all gates.

All **11 authoritative QC gates passed** in the fresh run: **2,384 tests passed**,
four were skipped, and one dependency deprecation warning remains. The skips
are one historical CARD-cache replay after corpus change and three empty
skill-path parameter sets. Strict schema validation reported zero errors for
all 2,939 records, source reproduction was exact, and chemical-map and
generated-site checks passed.

Both changed search documents were genuinely re-encoded with the pinned local
BGE model. All **2,937 other vector rows** are byte-identical, with 16 control
rows agreeing within `0.0001`. The complete PaCMAP projection was rebuilt with
seed 42; the current semantic fingerprint is `d3ad62728785d526`. The rendered
map payload, all 2,939 local record links, and the rendered identity caveats were
checked. The [verification receipt](2026-10-09-platen-verification.json) binds
these results, current record hashes, source-cache pins and preservation checks.
No live browser verification or independent external review is claimed. Earlier
checkpoint receipts remain historical; passing QC does not complete primary
review of either compound or of the whole corpus.

## Bacteriocin Identity and References (2026-10-09)

The [dossier](2026-10-09-bacteriocin-primary-context.json) covers nisin,
epidermin, microcin B17, microcin C and microcin J25. All five remain open.
It retains ten UniProt references from release `2026_03`, with entry/sequence
versions, archive links and citation-specific donor context. None is assigned
as an exact experimental protein, allele or genome.

| Record | Verified reference finding or hold |
| --- | --- |
| Nisin, CHEBI:71629 | P42708 is a NisI reference from NIZO R5/6F3, not a verified NZ9700 experimental allele. Two primary studies name commercial nisin; the exact congener-to-record match remains unresolved. |
| Epidermin, CHEBI:71659 | EpiF/Q54002, EpiE/Q54003 and EpiG/Q54004 explicitly cite PMID:8550476 and donor Tue3298. Its tested S. carnosus host is distinct. Primary Results remain pending. |
| Microcin B17, CHEBI:64624 | The stored unmodified peptide graph lacks the maturation heterocycles described in PMID:8183941's abstract. Current ChEBI repeats that graph; matching identifiers do not resolve it. |
| Microcin C, CHEBI:82754 | Six MccE/MccF references remain separate candidates. Intact material, processed intracellular material and analogues are not interchangeable assay substrates. |
| Microcin J25, antibioticmech:aro-0a1c492c45 | The stored head-to-tail backbone graph conflicts with the lasso linkage described by three 2003 primary abstracts. CHEBI:203056 repeats the stored key. The inherited YojI assertion is preserved, not independently revalidated. |

RDKit `2026.03.5` reproduces J25's stored key from its SMILES and finds a
63-atom ring without specified atom stereochemistry. B17's stored and current
ChEBI SMILES fail strict parsing. Its Standard InChI does parse and reproduces
the stored key, with only one five-membered ring and no aromatic oxygen or sulfur.
These graph checks support identity holds, not a source-owned identity repair.

Licensed EMBL-EBI XML supplied relevant primary Results and identity text for
PMID:25014359 and PMID:25176038. The reported growth endpoint is IC50, not MIC
or a clinical resistance category. The NisI result supports a pore-formation
effect; direct Lipid II shielding remains a proposed explanation. Figures and
supplements have not been visually reviewed. UniProt taxonomy names
NCBITaxon:746361 as the NZ9000 background; the separate MG1363 result and the
current cremoris parent are retained. This is not a derivative-strain or donor
TaxID assignment. NisI's reference TaxID 1360 is subspecies rank.

The broader NisI query returned 64 hits, including nickel-silicide false positives;
biological refinement retained 47 candidates, not 47 verified findings.
These supplemental searches do not replace the already-complete 611 expanded
corpus query traversals. Publisher access to the selected PNAS and ASM papers
returned 403; their primary Results were not obtained. Microcin C's selected
papers remain abstract-level leads. The GdmH abstract reports gallidermin,
so its title is not used to establish epidermin resistance.

All 2,939 biological records and their histories remain unchanged. No new
sequences, variant specifications, protocols or numerical susceptibility data
are exported. Full authoritative QC was not rerun for this research-only
checkpoint; the platensimycin/platencin receipt remains the last biological QC
result. Curation stays authorized once each evidence hold is resolved.

The [verification receipt](2026-10-09-bacteriocin-verification.json) records
103 passing related regression tests and a repeat of all 14 focused tests on
the final artifact. The existing full-corpus progress index reproduces exactly;
lint and whitespace checks pass. This is an adversarial self-review, not an
independent external review or a new full-QC run.

## Bacteriocin Qualitative Curation

The [follow-up dossier](2026-10-09-bacteriocin-followup-context.json) supersedes
only the two primary-text holds needed for the
[three curated claims](2026-10-09-bacteriocin-curation.json). The earlier
five-record dossier remains an immutable historical checkpoint.

Relevant Results were inspected in public author-uploaded text for
[Peschel and Goetz 1996](https://www.researchgate.net/publication/14649002_Analysis_of_the_Staphylococcus_epidermidis_genes_epiF_-E_and_-G_involved_in_epidermin_immunity),
[Tikhonov et al. 2010](https://www.researchgate.net/publication/46578673_The_Mechanism_of_Microcin_C_Resistance_Provided_by_the_MccF_Peptidase), and
[Novikova et al. 2010](https://www.researchgate.net/publication/41451765_MccE_Provides_Resistance_to_Protein_Synthesis_Inhibitor_Microcin_C_by_Acetylating_the_Processed_Form_of_the_Antibiotic).
No native primary files were obtained; figures were not visually adjudicated
and supplements remain unreviewed. Direct Europe PMC and author-page canaries
returned 403; the batches stopped. Public indexed text, not those failed
downloads, supports this checkpoint. No access-control bypass occurred.

[ENA's U77778 summary](https://www.ebi.ac.uk/ena/browser/api/summary/U77778)
explicitly lists U29130 as a secondary accession. This resolves the archive
identifier discrepancy, not experimental allele identity. The empty response
for the older accession is not biological absence. The six-hit UniProt archive
query retains three donor references and three unselected neighboring proteins;
the latter are not promoted to resistance determinants. The tested host species
is grounded through [UniProt taxonomy 1281](https://rest.uniprot.org/taxonomy/1281.json),
not donor species 1282. No exact laboratory-derivative TaxID is assigned.

The six microcin C reference candidates remain separate. The curated notes
retain the intact/processed/analogue distinctions and the reference-versus-
experimental identity limitations. No numerical susceptibility observations,
sequences, exact variants or experimental designs are added.

The [full-corpus reconciliation](2026-10-09-bacteriocin-checkpoint-reconciliation.json)
verifies two changed records, two meaningful history events, and 2,937
byte-identical records. Source-owned inputs, chemical identities and prior
history are preserved. All whole-record primary reviews remain open.
The genuine embedding refresh and site regeneration are published. Both changed
documents were re-encoded; 2,937 vector rows remain byte-identical, and the
16 control rows agree within the established tolerance. All 176 focused
regression tests pass. All 11 authoritative QC gates also pass, including
**2,405 tests passed, four skipped and one dependency-deprecation warning**,
zero strict-schema errors across all 2,939 records, exact corpus reproduction,
and chemical-map and generated-site checks. The skips are one historical
checkpoint comparison and three empty skill parameter sets; current public
invariants still run.

The [curation verification receipt](2026-10-09-bacteriocin-curation-verification.json)
binds the final artifacts, all current record hashes, protected-file checks,
embedding reuse and terminal QC logs. This was an adversarial self-review,
not an independent external review. Exact experimental alleles, genomes,
uninspected figures and supplements, the three remaining identity holds,
and broader whole-record evidence coverage remain open. No NCBI request,
source adoption or GitHub mutation occurred.

## Peptide Reference Follow-Up

The [four-record dossier](2026-10-09-peptide-reference-followup.json) adds six
UniProt reference candidates and reuses the previously verified NisI reference.
It does not assign experimental alleles or change biological records.

| Record | Disposition |
| --- | --- |
| Nisin | Historical nisin A evidence does not resolve the later commercial congener; the representation hold remains. |
| Mersacidin | Five reference proteins are retained separately; the current MrsG reference revision postdates the experiment. Exact material scope remains open. |
| Cinnamycin | Key susceptibility tests used duramycin. The selected UniProt citation and immunity paper also name different strains. |
| Lugdunin | A paper-linked background chromosome is verified, but experimental derivative and protein mappings remain open. |

The [cinnamycin primary study](https://doi.org/10.1007/s10295-016-1869-9)
cannot support relabeling duramycin assays as direct cinnamycin AST.
[ENA CP063143](https://www.ebi.ac.uk/ena/browser/api/summary/CP063143) supplies
reference chromosome version 1, BioSample SAMN16428309 and BioProject
PRJNA669000; these are not derivative-genome assignments.

Current ChEBI keys match all four records. RDKit diagnostics flag nisin and
lugdunin SMILES parsing and partially specified stereochemistry in three
records; these checks alone neither prove misidentification nor establish
tested-material equivalence. Source-owned structures remain unchanged.

The dossier distinguishes inspected primary text, selected native-page visual
review, and an abstract-only lead. Supplements and whole-record reviews remain
open. Gene-name collisions and no-hit queries are not biological assignments
or evidence of absence. No NCBI requests, source adoption or GitHub mutations
occurred. Full QC was not rerun for this research-only pass; the previous
biological checkpoint remains authoritative.

A [bounded vocabulary audit](2026-10-09-peptide-discovery-vocabulary-gap.json)
confirms two missed known papers under the production API settings: the v1
genetics clause excludes PMID:33106269, recovered by `gene*`; the phenotype
clause excludes PMID:27858169, recovered by `immun*`/`sensitiv*`. These are
counterexamples, not a corpus recall estimate. Historical snapshots and search
code remain unchanged. A separately versioned complementary search is needed
before interpreting completed v1 traversals as adequate discovery coverage.

The [verification receipt](2026-10-09-peptide-followup-verification.json) records
153 passing related tests, a final 16-test focused pass, unchanged hashes for
all 2,939 records, and preserved pre-existing report text. Lint, whitespace,
README statistics and the existing corpus progress index pass. This is an
adversarial self-review, not an independent external review.

## Broader Discovery Vocabulary

The [versioned v2 discovery checkpoint](2026-10-09-resistance-vocabulary-discovery.json)
addresses the two preceding vocabulary counterexamples. It adds `gene*`,
`immun*` and `sensitiv*` without subtracting live v1 results. All 2,939 records
and 16,030 recorded names were searched, including the 319 records with
existing resistance assertions or interpretation rules. Both known-paper
canaries recovered their expected references, PMID:27858169 and PMID:33106269.
This does not resolve the biological identity and evidence holds above.

| Discovery Measure | Result |
| --- | --- |
| Distinct initial queries | 7,466, representing 7,469 query-record memberships |
| Queries with no hits under these filters | 4,199 |
| Queries with complete initial-page candidate sets | 2,408 |
| Truncated queries requiring separate expansion | 859 across 536 records; 860 query-record memberships |
| Distinct citations retained in v2 initial pages | 72,142 |
| Distinct citations absent from all pinned earlier exports | 38,491 |
| Distinct citations in the historical-plus-v2 union | 286,114 |

The [per-record ledger](2026-10-09-resistance-vocabulary-discovery-ledger.tsv),
[candidate index](2026-10-09-resistance-vocabulary-discovery-candidates.json.gz)
and [citation union](2026-10-09-resistance-vocabulary-discovery-union.json.gz)
retain source-qualified identities and separate record memberships. All
247,623 historical citation identities and 500,533 historical record-citation
memberships survive; no rejected-page rows are recovered as accepted results.
There are additional citation leads for 1,634 records. These are not counts of
relevant studies, independent biological replicates or verified resistance findings.
Live-index changes and first-page ranking also affect differences, so additions
cannot all be attributed to the broader vocabulary.

The existing v1 CLI default and all 7,469 historical query strings remain
byte-compatible. V2 uses `--vocabulary immunity-v2` with separate plans and
exports. The 611 completed cursor traversals described earlier apply to v1
only: they do not complete the 859 truncated v2 queries. Their expansion needs
a separately identified, profile-aware plan. The union preserves discovery
history; it is not one validated cursor chain or a completed primary review.

All 11 authoritative QC gates passed for the frozen implementation, including
**2,461 tests passed, four skipped and one dependency-deprecation warning**.
The subsequent 175-test publication check and offline union reproduction also
passed. The [verification receipt](2026-10-09-resistance-vocabulary-discovery-verification.json)
binds the exports, terminal QC results, unchanged hashes for all 2,939 records,
and the ignored-file-inclusive preservation check. All pre-existing report text
is preserved. This was an adversarial self-review, not an independent external review.

No biological record, curation history, source inventory, embedding or generated
page changed in this pass. No NCBI request, outreach, source adoption or GitHub
mutation occurred. Full-corpus gene/allele evaluation, primary evidence review,
UniProt and taxon grounding, and curation of further verified findings remain open.

## Duramycin Primary Curation

The recovered cinnamycin paper tested **duramycin**, an existing exact ChEBI
synonym on lancovutide, **CHEBI:77834**. Relevant primary Results and native
Figures 3-5 were inspected. Two qualitative susceptibility associations are now
curator-owned on that record: a context-dependent Cinorf10 association in
laboratory derivatives of *Streptomyces lividans*, and separate native-host
perturbations implicating cinorf10/CinKR in protection. These are not resistant
allele assignments, individual-gene sufficiency, clinical interpretations or
direct cinnamycin AST. The route remains `UNKNOWN`.
[Primary study](https://link.springer.com/article/10.1007/s10295-016-1869-9).

The [reference-context dossier](2026-10-09-duramycin-reference-context.json)
retains UniProt Q83VX7, Q83VX8 and Q83VX9 separately from experimental alleles.
Their DSM 40005/JCM 4633 reference contexts do not resolve the study's DSM 40646
material. Q83VX9 also carries an unrelated-organism citation, flagged rather
than used as evidence. Species crosswalks use NCBITaxon:1916 and
NCBITaxon:53446; NCBITaxon:1200984 is background-only, not a derivative identity.
A bare collection-number search returned an unrelated plant TaxID, which was
rejected; a zero-result exact-phrase query is not evidence of biological absence.
No experimental genome or exact protein allele was assigned.

The named-compound match preserves ChEBI's existing identity and source fields.
Current/local structures retain one unassigned tetrahedral center; this is not
physical-sample or complete stereochemical re-identification. Both heterologous
comparators are laboratory derivatives, including the vector control. Negative
and expression-context-dependent findings remain visible. Production-indicator
results are not resistance evidence for the indicator organism, and regulatory
inference is not direct ligand-binding evidence. Whole-paper review and
supplement review remain open.

The [curation artifact](2026-10-09-duramycin-curation.json) records the validated
canary, fresh-seed merge check and single meaningful history event. Original
record bytes remain a complete prefix; all other fields and all **2,938** other
records are preserved. The [new census](2026-10-09-duramycin-resistance-grounding.tsv)
and [reconciliation](2026-10-09-duramycin-checkpoint-reconciliation.json) account
for all **2,939 records**, **4,802 resistance assertions across 307 records**,
**47 curator claims across 30 records**, and **467 unchanged interpretation
rules**. The `PENDING_DISCOVERY` label on 2,619 rows denotes no existing claims,
not an absence of previous searches. Every whole-record primary review is open.
The refreshed progress index retains its historical v1 discovery inputs; it
does not complete the separately documented 859 truncated v2 queries.

The changed document was genuinely encoded offline with the pinned BGE model.
All 2,938 unaffected vector rows are byte-identical; 16 re-encoded controls have
maximum absolute difference 0.000030517578125, below the 0.0001 gate. The entire
2,939-point PaCMAP projection and generated site were rebuilt. The fingerprint
is `6bdf987c4e89966b`; this is not a fingerprint-only refresh.

The focused suite passes **69 tests**. All **11 authoritative QC gates passed**,
including **2,471 tests passed, four skipped and one dependency-deprecation
warning**. The [verification receipt](2026-10-09-duramycin-curation-verification.json)
binds terminal results, source-field preservation, all current record hashes,
real encoding and rendered evidence. Its preservation search includes ignored
files. This is an adversarial self-review, not an independent review; no live
browser verification is claimed. No NCBI requests, outreach, source adoption,
GitHub mutations, sequences, exact variants, experimental designs or numerical
AST were added in this checkpoint. Corpus-wide investigation remains open.

## V2 Cursor Expansion

The [v2 expansion checkpoint](2026-10-09-resistance-vocabulary-expansion.json)
completes the **859 previously truncated immunity-v2 queries**, representing
860 query-record memberships across 536 records. It does not reuse historical
v1 completion as v2 evidence. The unchanged query-name projection was checked
against all **2,939 current records**, 16,030 names and 7,469 query memberships,
including ignored files. The duramycin record is the sole record whose hash
differs from the historical v2 plan; that historical hash was not rewritten.

A three-response canary checked pagination and the shared geneticin/G418 query
without merging its distinct chemical records. The bounded batch then stored
2,013 additional responses. All **2,016 cached pages** were rebuilt offline:
859 complete cursor traversals, no rejected pages, no cursor conflicts and no
hit-count drift relative to the initial v2 searches. Requests ran from
2026-10-09T22:39:17Z through 2026-10-10T01:38:31Z. Date ordering and consistent
counts still do not establish an atomic Europe PMC index snapshot.

The expansion retains 1,488,394 query-citation memberships and 636,253 distinct
citation identities. Its [all-record union](2026-10-09-resistance-vocabulary-expansion-union.json.gz)
now contains **645,070 distinct citations and 1,093,332 record-citation
memberships**. All previous 286,114 distinct citations and 547,953 memberships
survive; 358,956 citation identities are new to that historical union, and
533 records gain leads. These are not relevance estimates or experimentally
verified compound matches. Ambiguous aliases, including the large polysulfur
query, remain explicitly unresolved. Every primary-review status remains pending.

The full candidate gzip was 117,944,432 bytes, exceeding
[GitHub's regular-file limit](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).
The [candidate manifest](2026-10-09-resistance-vocabulary-expansion-candidates-parts.json)
therefore lists four ordered byte parts, each at most 32 MiB. Verify their
individual sizes and checksums, concatenate in manifest order, verify the
combined checksum, then gzip-decompress and verify the uncompressed checksum.
Individual parts are not standalone gzip or JSON files. Both compressed and
expanded bytes match the original export exactly; the original single-file
export remains private. Missing, reordered, duplicated, corrupted and
size-mismatched parts were rejected in packaging checks. No GitHub or LFS
mutation was performed.

### Lugdunin Reference Follow-up

The [supplement follow-up](2026-10-09-lugdunin-reference-followup.json) checks
five source-reported protein identifiers against UniProt release 2026_03.
The paper's Results call the accession table Table S3; the inspected supplement
labels it **Table S1 on page 1**. Both labels are retained with that discrepancy.
Three exact versioned RefSeq cross-references resolve to UniProt reference
entries, all annotated to **SL13**, not the study's **IVK28** background. Two
identifiers have no match in the exact or accession-base queries; that is not
evidence of biological absence. Species-level NCBITaxon:28035 and the earlier
background chromosome context remain separate from experimental derivatives.
No exact experimental allele or genome is assigned. The chemical-representation
and experimental-mapping hold remains, and the lugdunin record is unchanged.

### Verification

The frozen implementation passed 214 focused tests and all 11 authoritative
QC gates: **2,497 tests passed, four skipped, one dependency-deprecation
warning**. The skips cover one historical checkpoint mismatch and three empty
optional skill parameter sets; current public invariants still ran.
The [post-publication verification](2026-10-09-resistance-vocabulary-expansion-verification.json)
checks the cached chains, multipart payload, historical union, all current
record hashes, prior report bytes and protected files including ignored files.
This is adversarial self-review, not an independent review. No biological
record, curation event, raw source inventory, rendered page or embedding changed
in this checkpoint. No NCBI requests, outreach, source adoption, exact variants,
sequences, protocols or numerical AST were added. The all-record investigation
remains open; completed searches do not complete gene/allele grounding.

## Translation-Inhibitor Reference Follow-up

The [reference dossier](2026-10-09-translation-reference-followup.json) reviews
kirromycin, GE2270A, pulvomycin and thiostrepton without adding biological claims.
It preserves all 2,939 current record hashes and the historical citation union.
These four records and the corpus-wide primary review remain open.

### Primary Scope and Reference Identity

Relevant Results and Discussion text in
[Olsthoorn-Tieleman et al. (2007)](https://journals.asm.org/doi/10.1128/jb.01810-06)
distinguishes biochemical EF-Tu3 resistance from native-producer protection.
Kirromycin sensitivity persisted with the sensitive EF-Tu1 present; the paper
does not establish EF-Tu3-mediated protection of the native producer. The
coelicolor pulvomycin response was ambiguous. GE2270A growth observations used
laboratory derivatives and crude material, not an unchanged reference strain.
Thiostrepton served as a selection marker, not the focal resistance outcome.
Native figures were not visually inspected and this is not a completed review
of every result in the paper.

Three release-pinned UniProt references were followed up, without assigning
them as exact experimental alleles or linking them to a measured isolate:

| Reference | Source identity | Limit |
| --- | --- | --- |
| [P29544](https://www.uniprot.org/uniprotkb/P29544/entry) | ramocissimus `tuf3`; species TaxID 1925; entry 110, sequence version 1 | Reference identity, not an exact experimental allele assignment. |
| [P40175](https://www.uniprot.org/uniprotkb/P40175/entry) | coelicolor `tuf3`/`SCO1321`; reference-strain TaxID 100226; entry 156, sequence version 2 | The M145/A3(2) reference does not identify the tested J1501-derived backgrounds. |
| [P18644](https://www.uniprot.org/uniprotkb/P18644/entry) | azureus `tsnR`, alias `tsr`; species TaxID 146537; entry 105, sequence version 1 | The linked archive deposit has a conflicting taxon assertion. |

For P18644, [ENA X02392.1](https://www.ebi.ac.uk/ena/browser/view/X02392.1)
describes an azureus gene but reports TaxID 1904, which
[UniProt taxonomy](https://www.uniprot.org/taxonomy/1904) labels *Streptomyces
cyaneus*. UniProt's protein entry instead reports *S. azureus*, TaxID 146537.
Both source assertions are retained. No synonym equivalence, source correction
or experimental-organism assignment is inferred. The three inspected ENA
gene deposits are not genome assemblies.

### Chemical and Access Holds

The kirromycin record's Standard InChIKey is
`HMSYAPGFKGSXAJ-GFNGQHCCSA-N`; current
[ChEBI:190786](https://www.ebi.ac.uk/chebi/CHEBI:190786), labelled Mocimycin,
reports `HMSYAPGFKGSXAJ-PAHGNTJYSA-N`. RDKit 2026.03.5 reproduces both keys from
their respective InChIs: connectivity and tetrahedral stereochemistry agree,
but double-bond stereochemistry differs. ChEBI's current SMILES also fails
strict parsing. Neither representation is declared wrong or automatically
corrected. The all-record search, including ignored files, finds no other
record with that current ChEBI key. GE2270A leaves six of six tetrahedral
centers unspecified, and pulvomycin eight of thirteen. These diagnostics do
not establish the identity of the material tested in the paper.

Thiostrepton references PMID:6806287 and PMID:25086036 are retained as
supplemental leads absent from this record's historical citation union, not
new biological assignments or a corpus-recall estimate. Their relevant Results
remain unreviewed. Two Europe PMC full-text requests returned HTTP 500; the
publisher reader returned 403. Other web-tool access limits are recorded in
the dossier. Requests were stopped without retry or bypass; access failures
are not biological negative evidence.

### Checkpoint Verification

The [verification receipt](2026-10-09-translation-followup-verification.json)
checks cached response pins, source-to-reference projections, historical
citation memberships and preservation of the complete current record census.
The focused suite passed **56 tests**, including 14 new scope-regression tests;
lint, documentation consistency and whitespace checks passed. Full authoritative
QC was not rerun for this research-only checkpoint; the preceding production
QC remains historical. No biological record, curation event, raw source
inventory, rendered page or embedding changed. No NCBI requests, outreach,
source adoption, GitHub mutation, sequences, exact variants, protocols or
numerical AST were added. This is adversarial self-review, not an independent
review, and does not complete the all-record investigation.

## Aminocoumarin Reference Follow-up

The [aminocoumarin dossier](2026-10-09-aminocoumarin-reference-followup.json)
adds nine explicitly reference-only protein entries for novobiocin, coumermycin
A1 and clorobiocin. It investigates four existing assertion memberships for
`ARO:3002522` and `ARO:3003318`, without rewriting the ontology's assertions
or treating literature-derived candidates as explicit ARO cross-references.
All three records and the 2,939-record investigation remain open.

### Resolved and Conflicting Links

ENA explicitly marks [AF205853](https://www.ebi.ac.uk/ena/browser/view/AF205853)
as suppressed in favor of
[AF235050](https://www.ebi.ac.uk/ena/browser/view/AF235050), whose secondary
accession list points back to AF205853. This resolves the deposit link to
UniProt Q83WB9 and Q83WB8. It does not establish exact experimental allele
equivalence: the current archive record is version 4 and both proteins have
sequence version 2. The referenced nucleotide contig is not assigned as the
experimental genome.

| Reference context | Disposition |
| --- | --- |
| P50074 / Z17304 | UniProt reports *Streptomyces niveus*, TaxID 193462; ENA reports TaxID 2893586, currently *Actinoalloteichus cyanogriseus*. Retain the disagreement and the later paper's separately attributed organism hypothesis. |
| Q83WB7 / AF205854 | Current reference taxonomy differs from the paper's spheroides donor label. No experimental re-identification. |
| Q9L9G7 / AF170880 | The reference reports NCIMB 9219, whereas the focal paper names NCIMB 11891. Species synonymy does not establish strain equivalence. |
| Q83VW7 and Q83VW6 / AY136281 | TaxID 149682 is a subspecies; TaxID 1352936 is its DS 12.976 strain child. Different ranks are not an identity conflict. |
| P50075 | Sensitive reference comparator, not a resistance determinant. |
| Q9F8T3 | CouR5 reference context; no exact experimental allele assignment. |

The dossier pins UniProt release 2026_03, entry and sequence versions, six ENA
metadata records, and five UniProt taxonomy responses. Thirty-one other
publication-query hits remain in the private response, not a resistance list.
No sequence retrieval or NCBI endpoint request was made.

### Primary Scope

The inspected [2003 Results](https://journals.asm.org/doi/10.1128/aac.47.3.869-877.2003)
concern laboratory-host susceptibility to novobiocin and coumermycin A1.
Donor identity is separate; clorobiocin susceptibility, direct efflux and an
induced point mutant were not established by this review. The
[2004 biochemical follow-up](https://www.microbiologyresearch.org/content/journal/micro/10.1099/mic.0.26867-0)
was inspected only at abstract level: its linked full text returned 403 and
was not retried or bypassed. Native figures, exact tested chemical forms and
experimental allele identity remain pending. No biological claim was added.

### Verification

The [verification receipt](2026-10-09-aminocoumarin-followup-verification.json)
checks source projections, accession succession, citation memberships and all
current record hashes, including ignored files. **43 focused tests passed**,
including 13 new scope-regression tests; lint, documentation consistency and
whitespace checks passed. Full authoritative QC was not rerun for this
research-only checkpoint. All prior report bytes and biological records,
source inventories, pages and embeddings are preserved. This is adversarial
self-review, not independent review or completed corpus grounding.

## Aminocoumarin Primary Curation

The [primary context](2026-10-09-aminocoumarin-primary-context.json) and
[curation receipt](2026-10-09-aminocoumarin-primary-curation.json) add one
qualitative ParYR-associated host-susceptibility claim each to novobiocin
(`CHEBI:28368`) and coumermycin A1 (`CHEBI:3907`). The claims follow the
previously inspected [2003 Results](https://journals.asm.org/doi/10.1128/aac.47.3.869-877.2003)
and the now visually inspected native chemical Figure 1A. The subsequent
article request returned 403 and was stopped without retry or bypass.
Native Table 2 and whole-paper review remain open; no measurements are added.

### Identity and Scope

The observed host is *Streptomyces lividans*, `NCBITaxon:1916`.
TK24's `NCBITaxon:457428` is background context, not an identifier for a
laboratory derivative. The donor is separately reported as *S. rishiriensis*
DSM 40489. UniProt Q83WB8 remains a reference entry (entry version 120,
sequence version 2), not an exact experimental protein assignment. Archive
succession does not resolve the historical allele. The 2003 paper's unresolved
ParY function is retained as `UNKNOWN`, without importing conclusions from
the separately reviewed 2004 abstract.

Local InChI checks reproduce all three aminocoumarin record keys. Coumermycin
A1's stored SMILES fails strict RDKit parsing, but its InChI is valid. A limited
imidic-to-amide representation check retains the key and eight assigned
tetrahedral centers and visually agrees with Figure 1A. This is consistent
with [Standard InChI tautomer normalization](https://www.inchi-trust.org/technical-faq/),
not independent identification of the tested preparation. An unrestricted
tautomer-enumeration attempt was not accepted. No source-owned chemistry was
changed; the SMILES issue still needs source-level review.

Clorobiocin is unchanged: this review did not establish a focal susceptibility
result for it. Existing CARD assertions, prior curator content, compound
identity and all other record fields are preserved. No exact variants,
sequences, constructs, protocols, numerical AST or experimental genomes are
exported. No NCBI request, source adoption or GitHub mutation was made.

### Corpus and Verification

The [current census](2026-10-09-aminocoumarin-primary-resistance-grounding.tsv)
contains all **2,939 records**, **4,804 resistance assertions**, and **467
genotype rules**. There are **49 curator claims across 32 records**. Only two
record hashes and their assertion counts change relative to the previous
census; historical discovery artifacts remain immutable. The progress summary
retains its v1 query scope and must not be mistaken for the separate v2
expansion summary. All whole-record primary reviews remain open.

Both biological canaries passed closed-schema, roundtrip, fresh-seed merge
and field-preservation checks. **35 focused tests passed**, including eight
new regression cases. The existing embedding builder retains only six
resistance labels: coumermycin A1's model text changes, while novobiocin's
new claim falls outside that cap. The local model therefore re-encodes one
changed document, with 16 unchanged controls; it does not merely repin a
fingerprint. **All 11 authoritative QC gates passed: 2,532 tests passed,
four skipped, and one dependency deprecation warning.** The skips concern a
superseded historical checkpoint and three empty skill-parameter sets.
The [final verification receipt](2026-10-09-aminocoumarin-primary-verification.json)
records the protected-file audit, current record hashes, preserved source
slices, and projection/rendering checks. This is adversarial self-review,
not an independent review or completed corpus-wide investigation.

## Unlinked Erm Reference Follow-Up

The [Erm reference dossier](2026-10-09-erm-reference-followup.json) covers all
six terms without explicit UniProt candidates among the pinned audit's 47
Erm-prefixed labels. These terms occur in **80 existing assertions across 24
records**. Every record was read through the collection-aware loader and
checked against the current 2,939-record census. This cohort does not narrow
the whole-corpus goal or constitute completed primary review.

Nine bounded, sequence-free UniProt queries return **eight reference
candidates**, in release `2026_03`. Fourteen ENA summaries and eight UniProt
taxonomy responses retain accession versions, source bibliography and species
rank. All 31 metadata responses are hash-pinned. The searches cover recorded
gene names, explicit source aliases and selected publication-linked deposits;
they are not an exhaustive enumeration of either family or allele diversity.

| Source term | Reference candidates | Disposition |
| --- | --- | --- |
| ErmQ | Q46194 | Original JIR100 citation and later SC4-C13 submission remain separate. |
| ErmX | Q7BBX6, Q9AG96, Q9AG93, J7Q2T4, Q46484 | Multiple organisms and source contexts; no representative is selected. |
| Erm(36) | Q8VQ13 | Current `ermML` / `erm36` annotations; source definition conflict retained. |
| Erm(O)-lrm | Q54386 | TK21 reference; shared deposit is not a unique gene identifier. |
| erm(56) | No hit for the recorded queries | Published ENA deposit OQ326498 remains a verified reference lead. |
| erm(55) | No hit for the recorded queries | Published ENA deposits OQ656455, OQ656456 and OQ656457 remain separate. |

### Evidence Boundaries

- The pinned ontology labels `ARO:3000605` as Erm(36), but its definition
  names ErmD. This is flagged, not converted into an alias or silently corrected.
  The [2002 primary abstract](https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-148-8-2479)
  connects Erm(36), MAW843 and AF462611; primary Results remain uninspected.
- J7Q2T4 derives from the partial type-strain deposit HE586307. The
  [2012 Results](https://link.springer.com/article/10.1186/1471-2180-12-52)
  report that type strain as susceptible to the tested antibiotics except
  cefotaxime. Its gene annotation is not a macrolide-resistance assignment.
- UniProt and ENA associate Q9AG96 / AF338705 with CJ21, and Q9AG93 /
  AF338706 with CJ12. The [2001 figure caption](https://journals.asm.org/doi/10.1128/aac.45.7.1982-1989.2001)
  lists strains and accessions in opposite order without explicit per-item
  pairing. The database mappings remain attributed; positional matching is
  not used to assign experimental alleles.
- Q46484's historical citation names *Corynebacterium xerosis*, while the
  current reference and ENA metadata name *C. striatum*. Historical
  reidentification is not yet verified, so the names are not treated as
  species synonyms. In contrast, UniProt taxonomy explicitly lists
  *Mycobacterium chelonae* as a synonym of *Mycobacteroides chelonae*,
  `NCBITaxon:1774`; this does not identify a clinical isolate.
- The [Erm(55) study](https://journals.asm.org/doi/10.1128/jcm.00428-23)
  distinguishes clinical isolates and several deposits. The
  [Erm(56) study](https://journals.asm.org/doi/10.1128/msphere.00239-23)
  distinguishes host-dependent outcomes, including an inconclusive
  pristinamycin IA comparison in *E. coli*. Neither a class label nor a
  database no-hit justifies propagating or rejecting a phenotype.

The lrm publisher request returned 403 and was stopped without retry or
bypass. The Erm(36) full-text link returned a tool internal error without
an HTTP status; no denial status or full-text inspection is inferred.
Other candidate bibliography remains pending primary review. Exact tested
chemical forms, subject crosswalks and native tables still need review
before further biological curation. No new sequences, exact variants,
constructs, protocols, numerical AST or experimental genome assignments are
exported. NCBI remains deferred; no endpoint request or outreach was made.

**72 focused tests passed**, including 14 new scope-regression cases.
Lint, documentation consistency and protected-file checks are recorded in
the [verification receipt](2026-10-09-erm-followup-verification.json).
All 2,939 biological records, source inputs, pages and embeddings are
unchanged in this pass. The 49 previously curated claims remain in place.
Full authoritative QC was not rerun for this research-only checkpoint.
This is adversarial self-review, not independent review, and the corpus-wide
investigation remains open.

## Corrected Erm(55) Clinical Associations

The [primary-context dossier](2026-10-09-erm55-primary-context.json) and
[curation receipt](2026-10-09-erm55-primary-curation.json) document ten
qualitative clinical-isolate associations added to clarithromycin
(`CHEBI:3732`). The [2023 study](https://journals.asm.org/doi/10.1128/jcm.00428-23)
and its [2024 erratum](https://journals.asm.org/doi/10.1128/jcm.00415-24)
are both cited at claim level. The erratum replaces Table 2 because genotype
columns were misaligned; its heading and footnote corrections to Table 3
are also recorded. Europe PMC bibliography independently confirms the
study-to-erratum relationship in both directions.

These are source-reported gene-family and phenotype co-occurrences, not
functional proof, exact-allele assignments or species-wide resistance claims.
The corrected table does not make every resistant isolate positive for one
subtype-specific assay. Its susceptible comparator and intermediate isolates
are not promoted to resistance claims. Exact source isolate labels remain
separate. No UniProt accession, exact allele, strain TaxID or experimental
genome is assigned: the recorded UniProt queries returned no hit, which is
not evidence that the gene or protein is absent.

The source name *Mycobacterium chelonae* is an explicit synonym of
*Mycobacteroides chelonae* in the pinned UniProt taxonomy response,
`NCBITaxon:1774`, at species rank. That grounding does not identify an isolate.
The paper names clarithromycin in broth microdilution panels, but the tested
preparation was not independently re-identified. The local SMILES and InChI
agree with the stored Standard InChIKey; all 18 tetrahedral centers are assigned.
No chemical identity fields changed, and the curation remains a named-compound
qualitative join rather than an exact tested-preparation assertion.

Selected publisher Methods and Results and the corrected Table 2 text were
inspected. Native PDF visual inspection was not completed: the publisher PDF
link returned a tool internal error without an HTTP status, and the subsequent
Europe PMC PDF request returned 403. Access attempts stopped without retry or
bypass. No whole-paper review, complete table redistribution, sequences, exact
variants, constructs, protocols or numerical AST export is claimed.

The validated canary preserved all 44 prior resistance claims, activity
membership bindings, source-owned slices and other fields. Applying it added
ten claims and one curation-history event; all 2,938 other records remain
byte-identical. The [current census](2026-10-09-erm55-primary-resistance-grounding.tsv)
now contains 4,814 resistance assertions, including 59 curator claims across
33 records. The [progress checkpoint](2026-10-09-erm55-primary-resistance-progress.json)
keeps the 611 completed v1 query traversals distinct from v2 retrieval history;
neither query completion nor these limited claims completes primary review.

**75 focused tests passed**, including 17 new regression cases. Full
authoritative QC passed all 11 gates: **2,563 tests passed, 4 skipped, one
existing dependency deprecation warning**, zero schema errors and zero corpus
reproduction drift. All 2,939 embedding documents are unchanged because these
appended claims fall outside the existing first-six-label input; embedding
artifacts and their fingerprint remain byte-identical, with no re-encoding or
fingerprint-only update. The generated site and replacement content-addressed
clarithromycin download match the current record. The
[verification receipt](2026-10-09-erm55-primary-verification.json) records the
checks, preserved history, exact artifact hashes and skip details.

This is adversarial self-review, not independent review. NCBI endpoint requests,
outreach, source adoptions and GitHub mutations remain zero. All 2,939 records
remain in scope; whole-record primary-review completion remains zero and the
corpus-wide investigation remains **OPEN**.

## Topoisomerase Reference Grounding

The [reference dossier](2026-10-09-topoisomerase-reference-followup.json)
covers all 57 single-label `gyrA`, `gyrB`, `parC` and `parE` terms lacking
candidates in the pinned original CARD reference audit. These terms account
for 332 existing source-assertion memberships across 21 current compound
records. This is a defined follow-up cohort, not an exhaustive inventory of
all topoisomerase alleles or all resistance mechanisms. The
[offline exporter](../scripts/audit_topoisomerase_references.py) reads all
2,939 current records through the collection-aware loader and checks their
hashes, so an omitted source membership cannot be hidden by a selected-record
plan. Source assertions are preserved, not reclassified as primary findings.

| Evidence scope | Result |
| --- | --- |
| Source organism names | 24 of 26 resolve to exact active species names or explicit synonyms. |
| Source terms with species grounding | 53 of 57; this identifies the source-named species, not an experimental subject. |
| Complete reviewed-protein queries | 45, with 16 returning no reviewed hit. |
| Terms with reviewed reference candidates | 37 of 57. |
| Distinct reference proteins | 68, retaining entry and sequence versions. |
| Reference-organism taxonomy checks | 27, with source-species ancestry verified. |

The checkpoint combines 25 source-name taxonomy responses, including 13
reused responses, with 45 cached protein searches and 27 reference-organism
taxonomy responses. All retain request identity, retrieval time, response
hash and UniProt release `2026_03`. Pagination and result counts are checked;
only explicit gene names or synonyms and matching species ancestry support
a reference candidate. Locus names alone, matching organism text, inactive
taxa and cross-species references cannot satisfy those checks. Species,
strain and `no rank` reference entries retain their actual taxonomy rank.
Multiple candidates remain separate; no representative experimental allele
is selected.

Four terms remain without species grounding: the source label
`Salmonella serovars` is too broad, while the recorded `Salmonella isangi`
query has no exact active-species match. Neither is silently renamed or
assigned a species. The 16 protein no-hits apply only to the recorded
reviewed-entry queries; they do not show gene absence. Unreviewed entries,
additional aliases and primary experimental crosswalks remain open work.

These are ordinary reference candidates, not verified resistance alleles,
tested isolates or compound-specific phenotype evidence. Database-linked
bibliography is retained as identifiers and dates, but primary Results were
not reviewed in this pass. Reference positions and comments, sequences,
exact variants, constructs, protocols, coordinates and numerical AST are
not exported. No new biological curation is justified by these matches alone.
The existing 59 curator claims across 33 records remain unchanged.

**188 focused tests passed**, including 25 new regression cases. Repository
lint, documentation consistency, full-corpus offline export reproduction and
diff checks passed. Self-review also tightened the exporter to verify every
current record's cohort membership and match protein responses against the
frozen preparation, not just their own receipts. All 2,939 biological records,
source inputs, pages and embeddings remain byte-identical; prior report text
is preserved. The [verification receipt](2026-10-09-topoisomerase-followup-verification.json)
pins the checks and artifacts. Full authoritative QC was not rerun for this
research-only pass; the preceding biological checkpoint's passing QC remains
historical evidence for the unchanged corpus, not a new full test run.

This is adversarial self-review, not independent review. No NCBI endpoint
request, outreach, source adoption or GitHub mutation was made. The complete
2,939-record objective remains **OPEN**, with no additional whole-record
primary review declared complete.

## Unreviewed Topoisomerase Context

The [unreviewed follow-up](2026-10-09-topoisomerase-unreviewed-followup.json)
investigates all 16 reviewed-protein no-hit queries from the preceding
checkpoint. They represent 16 source terms, 112 existing source-assertion
memberships and 15 compound records. Changing only the query's review-status
filter returns **82 unreviewed UniProtKB entries**, including **42 explicitly
flagged fragments**. All 16 searches are complete at the recorded query scope,
with response counts, request identity, versions and release `2026_03` pinned.
Neither this search nor the earlier reviewed-only search exhausts all aliases
or establishes an experimental resistance allele.

The export preserves gene names and explicit synonyms, submission and other
protein names, fragment flags, ordered locus names and ORF names. A missing
fragment flag is not treated as proof of completeness. A `recommendedName`
field does not change an entry's unreviewed status. Conversely, unreviewed
status is not evidence that no experiment exists: the status wording now
explicitly says that **this audit has not established experimental identity**.
The wording refinement was checked to leave all identifiers and metadata
relationships unchanged.

Thirty-four reference-organism taxonomy responses verify the source-species
relationships. Eighteen reported proteomes were also inspected through
UniProt's metadata API. Twenty-six protein entries have matching proteome
TaxIDs and component names, supporting **18 distinct versioned reference
assembly identifiers**. These are database reference contexts, not genome
assignments to the source's tested resistant isolates. Proteome membership
does not itself establish manual review or experimental evidence; UniProt
documents that proteomes can contain reviewed and unreviewed entries and that
one TaxID can have multiple proteomes. See
[UniProt's proteome documentation](https://www.uniprot.org/help/proteome).
No assembly sequence was fetched and no NCBI link was followed.

One same-symbol, same-proteome group contains two separate entries with
distinct ORF identifiers. Both are retained. No representative is selected,
and the shared symbol does not establish one unique locus, a duplicate
experimental observation or an exact resistance allele. Entries without a
reported proteome link are not assigned an assembly by matching species alone.

Together, the two checkpoints contain 68 reviewed and 82 unreviewed reference
candidates for 53 of the defined 57 source terms. The four terms with
unresolved organism scope remain unresolved. This is reference-candidate
coverage, not 150 validated resistance alleles or completion of primary
review. Bibliography remains database-linked discovery evidence. No primary
resistance Results were reviewed, phenotype inferred, or biological record
changed in this pass. Sequences, exact variants, constructs, reference
positions, coordinates and numerical AST remain outside the export.

**212 focused tests passed**, including 24 new cases. Repository lint,
documentation consistency, full-corpus offline reproduction and diff checks
passed. The [exporter](../scripts/audit_unreviewed_topoisomerase.py) first
reproduces the prior reviewed dossier over all 2,939 records. Its shared
projection helper requires explicit Boolean opt-in for unreviewed entries;
the default reviewed-only output remains unchanged. The
[verification receipt](2026-10-09-topoisomerase-unreviewed-verification.json)
pins the final checks, wording-only comparison and protected-file audit.
All biological records, source inputs, pages and embeddings remain
byte-identical. Full authoritative QC was not rerun for this research-only
change; the 59 previously curated claims across 33 records are preserved.

This is adversarial self-review, not independent review. NCBI requests,
outreach, source adoptions and GitHub mutations remain zero. The entire
2,939-record objective remains **OPEN**, with no additional whole-record
primary review declared complete.

## CARD Definition Citations and Salmonella Scope

The [definition-citation audit](2026-10-09-card-definition-citations.json)
checks all **2,939 current records**, read through the collection-aware loader,
and all **4,538 CARD-owned assertion memberships** across **273 records** and
**2,002 terms**. The earlier class-only inspection missed references attached
to OWL definition axioms. This audit validates each annotation against its exact
asserted RDF triple, including literal language and datatype. It does not inherit
parent citations or treat synonym and class xrefs as definition citations.

| Definition bibliography in the pinned ontology | Count |
| --- | ---: |
| Terms with allowlisted definition citations | 1,580 |
| Terms without allowlisted definition citations | 422 |
| Source assertion memberships with definition citations | 4,031 |
| Unique PMID identifiers | 1,780 |
| Unique DOI identifiers | 1 |
| Definition axiom annotations checked | 1,594 |
| Other axiom annotations kept separate | 1,615 |

Of the original 1,024 terms without an explicit reference-protein link,
**702 have definition citations** and 322 do not in this snapshot. These are
literature-review leads, not newly verified biological effects. The historical
978 linked / 1,024 unlinked reference audit is unchanged. An absent ontology
citation is not evidence that primary research does not exist. Source definitions,
labels and unrecognized xrefs are hashed rather than exported as raw text.

The [Salmonella scope dossier](2026-10-09-salmonella-source-scope.json)
retains four terms, 30 source assertion memberships and 13 compound records.
Both broad serovar terms cite PMID:19104017; both Isangi terms cite
PMID:37627729. EMBL-EBI bibliography responses independently verify the two DOI
identities. Their titles do not establish experimental gene or allele identity.

UniProt release **2026_03** supplies genus context `NCBITaxon:590` for the broad
source name, not a species assignment. Its Isangi candidate `NCBITaxon:1386015`
has rank **no rank**, with the source spelling in **otherNames**, not synonyms.
The candidate's lineage includes species `NCBITaxon:28901` and subspecies
`NCBITaxon:59201`; those ancestors are not assignments to experimental subjects.
Three strain candidates retain historical Enteritidis names as ambiguity, with
none selected. [LPSN's nomenclatural record](https://lpsn.dsmz.de/species/salmonella-isangi)
reports the species name as not validly published; that status alone does not
prove a serovar crosswalk.

Selected narrative Results and Discussion in the
[2009 primary paper](https://journals.asm.org/doi/10.1128/aac.01005-08)
describe an Enteritidis background and a negative parE test. The authors leave
an indirect contribution unresolved. This does not independently demonstrate
causal resistance for `ARO:3003317`, nor prove absence of a role in all backgrounds.
The review does not extend that result to every inherited compound membership.
Tables, supplements and whole-paper review remain open. The
[Isangi publisher page](https://www.mdpi.com/2079-6382/12/8/1309) returned **HTTP 429**;
access stopped without retry or bypass, and primary Results remain unreviewed.

The four-term canary reproduced in the full audit. **242 focused tests passed**,
including **30 new cases**, followed by repository lint, documentation checks,
offline citation and Salmonella-context reproduction, and diff checks. Tests use
public artifacts and fixtures; ignored response caches are required only for the
explicit local reproduction checks. The
[verification receipt](2026-10-09-card-definition-citations-verification.json)
pins these checks and the protected-file comparison. This is adversarial
self-review, not independent review; full authoritative QC was not rerun for
this research-only change.

All **2,939 biological records**, source inputs, pages and embeddings remain
byte-identical. No new experimental protein, exact allele or taxon assignment
was made. Source-owned claims were not replaced from this limited review.
NCBI endpoint requests, outreach, source adoption and GitHub mutations remain
zero; #1040 remains deferred. Whole-corpus primary review remains **OPEN**, with
no whole record declared complete.

## CARD Citation Concordance and TlrB Context

The [citation-concordance audit](2026-10-09-card-citation-concordance.json)
compares all **2,002 current CARD terms** against **4,182 entries** in the pinned
UniProt CARD-cross-reference snapshot, release **2026_03**. It rechecks all
**2,939 records** through the collection-aware loader and reproduces the original
**980 explicit reference links**, without changing their status. This is not a
search of all UniProt and does not replace the wider discovery work.

| Citation comparison | Count |
| --- | ---: |
| Terms with a shared source-definition / UniProt citation | 554 |
| Term-to-protein citation-overlap links | 1,109 |
| Existing explicit links with citation overlap | 415 |
| Previously unlinked terms with literature-overlap leads | 59 |
| Previously unlinked terms without overlap in this snapshot | 965 |
| Previously unlinked terms with a literal gene-name match | 2 |
| Literal gene-name matching links for those two terms | 9 |
| Distinct retained reference proteins | 1,099 |
| Reference TaxIDs checked | 366 |

The 59 terms are leads, not newly grounded resistance alleles. A unique shared
paper can still refer to a different gene: the `aadA23` lead is a reference to
`dfrA15b`. Likewise, eight matching `cat` names remain distinct family references,
not one chosen representative. Lack of citation overlap does not invalidate an
existing explicit link. The original 978 linked / 1,024 unlinked source-term
classification remains unchanged.

Six additional TaxIDs were retrieved through UniProt after a successful canary.
All are active, but their species, serotype and strain ranks are preserved;
mixed-culture and uncultured names are not silently converted to identified
experimental isolates. The canary also exposed **18 malformed DOI annotations**
in the cached protein snapshot, all lacking the leading `10`. They are hashed
and retained as unresolved metadata, not repaired or matched by assumption.
Valid PMID annotations in the same references remain usable. DOI case is
normalized only for comparison, and citation-specific reference numbers remain
attached to their protein entries.

The [TlrB primary-context dossier](2026-10-09-tlrb-primary-context.json) retains
the `tlrB` synonym lead to **UniProtKB:Q9S1M6** and two independently verified
EMBL-EBI bibliography identities. UniProt's explicit CARD xref is `ARO:3004592`
(`erm(32)`), not the `tlrB` term `ARO:3001299`; the evidence here neither merges
those ontology terms nor declares that xref erroneous. Citation-specific strain
annotations remain separate.

Selected [primary Results and Discussion](https://onlinelibrary.wiley.com/doi/full/10.1046/j.1365-2958.2000.02046.x)
distinguish the donor **Streptomyces fradiae** (`NCBITaxon:1906`) from the assay
host **Streptomyces lividans** (`NCBITaxon:1916`). They retain RNA-modification
evidence, a negative drug-inactivation result and an explicitly qualified causal
interpretation. The native reference is not assigned as the experimental protein
form. The [earlier publisher abstract](https://www.jstage.jst.go.jp/article/antibiotics1968/52/3/52_3_288/_article/-char/en)
is not treated as a completed primary-results review. Figure inspection, exact
experimental protein identity, tested preparation identity and broader primary
review remain open. No new biological claim was curated from this scoped review.

The canary's three terms reproduce in the full audit. **275 focused tests passed**,
including **33 new cases**, with repository lint, documentation checks, offline
audit/context reproduction and diff checks. The
[verification receipt](2026-10-09-card-citation-concordance-verification.json)
pins the scoped checks and the protected-file comparison. Full authoritative QC
was not rerun for this research-only change; this is adversarial self-review,
not independent review.

All biological records, source inputs, pages and embeddings remain byte-identical.
No source adoption, NCBI endpoint request, outreach or GitHub mutation occurred;
#1040 remains deferred. All **2,939 records** remain in scope and whole-corpus
primary review remains **OPEN**, with no whole record declared complete.

## Literature-Constrained UniProt References

The [literature-protein dossier](2026-10-09-card-literature-proteins.json)
follows all **111 definition PMIDs** for the **59 previously unlinked terms**
with citation-overlap leads. The source cohort covers **152 assertion
memberships across 64 compound records**. All **2,939 current records** were
read with the collection-aware loader and checked against the current census.
The UniProt searches use no CARD-database or reviewed-entry filter.

All **134 response pages** reproduce under release **2026_03**, including the
four complete pagination chains. Their combined metadata contains **13,412
distinct entries**; this is database inspection, not primary-paper review.
Twenty-four queries return zero entries, which does not establish biological
absence. Query identity, counts, releases, ordering, requested citation
membership and terminal cursors are checked before a search is called complete.

Literal gene-name or synonym matches retain **32 reference proteins for 12
terms**, covering **16 source memberships in 11 compound records**. Of these
proteins, **23** were outside the earlier CARD-filtered snapshot; **15** are
reviewed and **17** unreviewed. Their **27 reference TaxIDs** retain their
verified ranks. The four additional taxonomy checks resolve a species, a
serotype, a subspecies and a strain, not four interchangeable species labels.
The other **47 terms** have no qualifying match in these queries; that is not
evidence that their genes or literature are absent.

The canary retains `aadA23` / `UniProtKB:Q6A150` as a reference candidate tied
to `PMID:15761062` and reference `NCBITaxon:58095` (rank **no rank**). Two
different-gene entries citing that paper are not assigned to this term.
The broad `cat` match retains **20 entries** without choosing an allele;
`cmlA1` retains two synonym matches. All candidate links in this follow-up are
name-based, not newly verified explicit CARD cross-references. Prior explicit
link status remains unchanged.

All **303 focused tests passed**, including **28 new cases**. The
[verification receipt](2026-10-09-card-literature-proteins-verification.json)
pins those tests, repository lint, documentation checks, offline dossier
reproduction and the protected-file comparison. The canary term and protein
reproduce in the full export. This is adversarial self-review, not independent
review; full authoritative QC is not rerun for this research-only change.

No new primary experimental claim is established by these metadata lookups,
so no biological record is changed. Source inputs, pages and embeddings remain
byte-identical. No sequences, exact variants, experimental procedures or
numerical AST are exported. No NCBI endpoint request, source adoption, outreach
or GitHub mutation occurred; #1040 remains deferred. All **2,939 records**
remain in scope, and whole-corpus primary review remains **OPEN**.

## Literature Primary and Archive Context

The [primary-context dossier](2026-10-09-literature-primary-context.json)
follows three source terms across **six memberships in five compound records**.
Four bibliography identities and three sequence-free UniProt-to-ENA reference
links are verified. Existing reference TaxIDs retain their distinct **no rank**,
**subspecies** and **strain** ranks; they are not all species identifiers.

The [aadA23 publisher abstract](https://academic.oup.com/jac/article/55/5/776/691293)
distinguishes isolate 231 from the other isolate in the study. Its reference
link agrees with the citation-specific strain annotation, but the full results
remain unreviewed. A shared paper does not justify a shared-isolate assignment.

Selected [ant(6)-Ib results and Table 2](https://journals.asm.org/doi/full/10.1128/aac.00304-10)
support a gene-dependent streptomycin phenotype. The enzyme-family assignment
is homology-based, not a direct biochemical measurement in the inspected
results. The paper's donor `IMD523-06`, assay host `1516477`, and reference
annotation `IMD 523` remain distinct. The shared archive accession verifies a
source link, not independent equivalence of those strain labels.

The open-access [HelD study](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8655204/fullTextXML)
names `SVEN_6029`, matching the HelR reference locus. Its resistance discussion
cites the same Surette study already used by the source term, so it is not
counted as an independent phenotype experiment. Selected results, conclusions
and captions were read, not the figure images or the whole paper. The two
publisher requests returned 403 and were not retried or bypassed; the earlier
study's explicitly open-access repository XML was available through EMBL-EBI.
The 2022 HelR primary results remain unreviewed.

HelR's `FR845719.1`, `SAMEA3138410` and `PRJNA62209` provide complete-genome
sequence, sample and project **reference context**. The archive cites the
genome publication, not the source resistance paper. No assembly accession or
experimental-genome assignment is inferred from this sequence record.

All **315 focused tests passed**, including **12 new cases**. The
[verification receipt](2026-10-09-literature-primary-context-verification.json)
records those tests, lint, documentation checks, offline dossier reproduction
and protected-file comparison. This is adversarial self-review, not independent
review; full authoritative QC is not rerun for this research-only increment.
Exact tested preparations and experimental protein identities remain unresolved,
so biological records, source inputs, pages and embeddings are unchanged.
No sequences, exact variants, constructs, protocols or numerical AST are
exported. All **2,939 records** remain in scope and whole-corpus primary review
remains **OPEN**. No NCBI endpoint requests, source adoption, outreach or GitHub
mutation occurred; #1040 remains deferred.

## nimB Clinical Associations

Primary [Table 2 and selected Methods/Results](https://journals.asm.org/doi/10.1128/jcm.38.9.3209-3213.2000)
support five qualitative `nimB`-type/metronidazole clinical co-occurrences.
Four isolates are *Bacteroides fragilis* (`NCBITaxon:817`); one is
*Bacteroides thetaiotaomicron* (`NCBITaxon:818`). The curation preserves the
separate control, `nimE` distinctions and assay-negative comparators. Gene-type
association is not exact-allele causation or demonstrated biochemical activity.
No numerical AST or new breakpoint interpretation is exported.

The prior UniProt snapshot supplies `UniProtKB:Q45146` as reference context only
(unreviewed, entry 68, sequence version 1, release `2026_03`, citing
`PMID:8067736`). It is not assigned to these clinical isolates. Species taxonomy
is reused from the pinned local snapshot; no strain TaxID or genome is inferred.
The metronidazole record's InChIKey reproduces from both stored structure
representations. The study's named-compound join does not independently identify
its tested preparation and is not extended to a salt or ester.

The validated canary adds five claims and one history event, preserving all
18 prior resistance claims and every other record field. The census now has
4,819 resistance assertions, including 64 curator claims across 34 records.
All 2,939 embedding documents and existing embedding artifacts remain unchanged.
The default virtual environment lacks RDKit; the existing scientific environment
completed the chemistry check on the same canary without creating another event.
All eleven authoritative QC gates passed: 2,729 tests passed, four were skipped,
and the existing LinkML deprecation warning remained. The focused suite passed
346 tests. All 2,939 records passed strict schema validation and the corpus
reproduced exactly from its source and curator inputs. The chemical map and
generated site are current. Whole-record and whole-corpus primary reviews remain
**OPEN**. No NCBI endpoint, source adoption or GitHub mutation was used.

Artifacts: [primary context](2026-10-09-nimb-primary-context.json),
[curation](2026-10-09-nimb-primary-curation.json),
[census reconciliation](2026-10-09-nimb-primary-checkpoint-reconciliation.json),
[current progress](2026-10-09-nimb-primary-resistance-progress.json),
[verification](2026-10-09-nimb-primary-verification.json).

## Native Isolates and Reference Hosts

The [azithromycin study's native Epi0082 row](https://academic.oup.com/jac/article/76/1/48/5942709)
supports one qualitative `mef(F)`/`msr(G)` co-occurrence with reduced
susceptibility. It does not isolate either gene's causal contribution in the
native organism. The separate comparator and expression-host experiment remain
distinct. The source name *Macrococcus canis* matches `otherNames`, not a formal
synonym field, in the cached UniProt taxonomy record for *Macrococcoides canis*
(`NCBITaxon:1855823`). No clinical breakpoint interpretation is added.

ENA metadata independently resolves the five source-reported genome components
`CP046363.1` through `CP046367.1` to Epi0082, `SAMN13342681` and `PRJNA590936`.
These are components, not assembly accessions or newly generated gene calls.
The `mef(F)` reference `UniProtKB:A0A7S4U594` instead belongs to
*Macrococcoides caseolyticum* (`NCBITaxon:69966`), strain `5459_5_49`; it is not
assigned to the native isolate. The bounded native-archive UniProt query returned
no hits, which is not evidence of gene absence. No exact protein or allele was
curated. Azithromycin's stored structure identity reproduces; the named assay
does not independently identify the tested preparation.

The four Qnr reference entries also require context-specific joins:
`Q2PT28` (`qnrB3`), `E1A0W6` (`qnrB27`), `G1FE71` (`qnrB34`) and `G1FE80`
(`qnrB38`). One `qnrB27` entry links three named isolates through distinct
archive protein evidence. `qnrB38` has separate original-isolate and later
dataset references. Some ENA queries return parent contig sets, not the requested
contigs; their versions and BioSamples are not assigned to the 2011 isolate.
Unbound strain comments are not propagated to every protein cross-reference.

Selected labels in the [2011 primary figure](https://journals.asm.org/doi/10.1128/aac.05187-11)
were visually checked. Its accession statement prints `JN173059` for both
`qnrB37` and `qnrB38`; the conflict is retained while UniProt/ENA support
`JN173060.2` for the latter. This is not a silently corrected primary source.
The Korean study remains abstract-only. No Qnr carrier is assigned clinical
resistance from gene presence, and no later dataset is treated as another
replicate of the original isolate.

The validated canary adds one claim and one history event, retaining all 54 prior
azithromycin resistance claims, both activity observations and their membership
collection. The census now contains 4,820 resistance assertions, including 65
curator claims across 35 records. All 2,939 embedding inputs and existing
embedding artifacts are unchanged. All eleven authoritative QC gates passed:
2,748 tests passed, with the same four skips and existing LinkML deprecation
warning as the previous checkpoint. The focused suite passed 365 tests. Strict
schema validation passed for all 2,939 records, the corpus reproduced with no
field drift, and the chemical map and generated site are current. A separate
self-review rechecked all five protein and 16 archive projections against their
27 cached request receipts; it was not an independent review.
Whole-record and whole-corpus primary reviews remain **OPEN**. No NCBI endpoint,
outreach, source adoption or GitHub mutation occurred; #1040 remains deferred.

Artifacts: [reference and primary context](2026-10-09-literature-hosts-context.json),
[curation](2026-10-09-literature-hosts-curation.json),
[census reconciliation](2026-10-09-literature-hosts-checkpoint-reconciliation.json),
[current progress](2026-10-09-literature-hosts-resistance-progress.json),
[verification](2026-10-09-literature-hosts-verification.json).

## Chloramphenicol Reference and Native Context

The [SOF-1 primary study](https://journals.asm.org/doi/10.1128/aac.45.6.1615-1620.2001)
reports native *Pseudomonas aeruginosa* chloramphenicol resistance by disk
diffusion and identifies CMLA6 in that isolate. The phenotype is explicitly
reported as data not shown. One qualitative same-isolate association is curated,
with `NCBITaxon:287`; it does not establish CMLA6-specific causation. The paper's
beta-lactam MIC table is not a chloramphenicol measurement. No zone diameter,
clinical breakpoint interpretation, exact allele, experimental protein or genome
is assigned. The source deposit `AF294653.1` is an archive record, not an assembly.

The reference audit retains all 20 `cat` candidates and the two literal `cmlA1`
synonym candidates, then follows two unsuffixed `cmlA` leads from the original
citation searches. These 24 proteins are reference identities, not 24 verified
experimental alleles. `Q8GGX1` includes a `cmlA1-variant` annotation and separate
ILT-3, D-03 and NF808096 source contexts. `Q933G9` combines CmlA6/cmlA1 names from
different publications and later deposits. Neither is silently promoted to the
canonical prototype. `P32482` has a revision citation and sequence version 2;
`Q9R8B8` is a fragment. Repeated citations are not independent observations.
The linked [comment and reply](https://journals.asm.org/doi/10.1128/aac.46.6.2058-2059.2002)
do not constitute a chloramphenicol allele erratum.

All 35 linked archive records were checked through ENA summary metadata.
`X51450` is laboratory material with a different taxon from the UniProt source
organism. Other archive/protein taxonomy differences remain explicit rather than
being forced into species-level agreement. The 17 UniProt reference TaxIDs retain their
species, subspecies, strain, serotype or no-rank status. Archive versions, protein
versions and UniProt entry versions stay separate; reference BioSamples and
projects are not assigned to SOF-1. The absence of an EMBL link on `P20074` is not
evidence of gene or deposit absence.

The [Bacillus clausii CAT paper](https://academic.oup.com/femsle/article/296/2/185/604333)
remains an abstract-only lead. Its PDF route resolves to a purchase/abstract page;
primary per-isolate results were not inspected. The source name matches
`otherNames` for *Shouchella clausii*, not a strain identifier. No new native CAT
phenotype is curated from that abstract.

The validated canary preserves all 87 previous chloramphenicol resistance
assertions, both activity observations, prior history and the existing `REVIEWED`
status. It adds one claim and one curation event. The census now contains 4,821
resistance assertions, including 66 curator claims across 36 records. All 2,939
embedding inputs and existing embedding artifacts remain unchanged. All eleven
authoritative QC gates passed: 2,765 tests passed, with the same four skips and
existing LinkML deprecation warning as the prior checkpoint. The focused suite
passed 171 tests. Strict validation passed for all 2,939 records, the corpus
reproduced with no field drift, and the chemical map and generated site are
current. A separate self-review checked all 95 cached response/receipt pairs and
the protein, archive, taxonomy and bibliography projections; it was not an
independent review.

All **2,939 records** remain in scope; whole-record and whole-corpus primary
reviews remain **OPEN**. No NCBI requests, outreach, source adoption or GitHub
mutation occurred. #1040 remains deferred.

Artifacts: [reference and primary context](2026-10-10-chloramphenicol-references-context.json),
[curation](2026-10-10-chloramphenicol-references-curation.json),
[census reconciliation](2026-10-10-chloramphenicol-references-checkpoint-reconciliation.json),
[current progress](2026-10-10-chloramphenicol-references-resistance-progress.json),
[verification](2026-10-10-chloramphenicol-references-verification.json).

## Glycopeptide Whole-Cluster Reference Audit

All thirteen glycopeptide whole-cluster terms were followed across their eighteen
existing memberships in vancomycin and teicoplanin. The unrelated `almEFG`
cluster remains outside this cohort, not outside the overall investigation.
Twenty cached UniProt citation queries were reused and six missing queries were
completed. The twenty-six publications are bibliography, not twenty-six verified
native genotype/phenotype links. The audit retains seventeen selected protein
references, twenty-seven ENA archive lookups, nine taxonomy entries and
eighty-two new frozen metadata response/receipt pairs. It does not enumerate
complete genetic architectures or assign a protein to an entire cluster.

Name searches expose two different failure modes. Most entries linked to the
[VanO paper](https://journals.asm.org/doi/10.1128/aac.01880-13)
lack `van` gene symbols; the ligase lead `V5KW92` is annotated `ddl`. Conversely,
literal `vanB`, `vanI` and `vanP` searches return unrelated vanillate-metabolism,
quorum-sensing or porin annotations. Ten homonyms were excluded. Two additional
VanI-labelled ligases remain unverified leads, not Y51 experimental subjects.
The VanP citation query has no hits; the name query supplies no supported
resistance-ligase mapping. Neither result establishes biological absence.
The [VanP publication](https://www.eurosurveillance.org/content/10.2807/1560-7917.ES.2021.26.36.2100767)
returned HTTP 403, without bypass. Its indexed abstract concerns borderline
susceptibility, not an automatically resistant clinical category.

The [Y51 primary results](https://journals.asm.org/doi/10.1128/aac.01408-08)
distinguish the resistance-associated `DSY3690` reference (`Q24R63`) from the
`DSY1579` comparator (`Q24X74`), although both UniProt entries use `ddl`.
Native vancomycin resistance and separate biochemical evidence support a scoped
curation handoff, not assignment of either accession to a modified experimental
protein. Species `NCBITaxon:49338` and strain `NCBITaxon:138119` remain distinct.
The [VanM study](https://journals.asm.org/doi/10.1128/aac.01710-09)
links native Efm-HS0661 to vancomycin resistance. `B8XGS3` binds that source
context to `FJ349556.1`; its separate `CP039730.1`/ZY2 context and BioSample must
not become the original isolate's genome. Discordant teicoplanin findings among
VanM carriers prevent phenotype propagation from cluster identity alone.

Other identity limits remain explicit. `Q06893` is a V583-associated reference,
not the BM4281 subject named by a different VanB citation. `O52073` retains a
Paenibacillus `vanE` annotation and sequence version 2; historical VanF naming
requires primary reconciliation, not an enterococcal VanE merge. `Q9ZFK2` is a
second-ligase fragment, not a VanF assignment. `Q47822` and `Q9S4K1` are also
fragments. Publication `N00-410` versus UniProt `N00-0410`, and source `RE-S7B`
versus UniProt `S7B`, remain unreconciled strings. The VanO reference taxonomy
retains its current name and source-name context rather than silently relabeling
the experimental subject.

ENA answers the `JARQDZ010000002` query with contig-set `JARQDZ010000000`, not an
individual-contig summary. That distinction, archive versions, sample/project
context and taxon disagreements are preserved. None becomes an experimental
assembly assignment. Generic teicoplanin assays remain on hold because the
existing record's source structure is labelled Teicoplanin A2-5; a mixture-level
drug name is not an exact-component identity join.

This is a research-only checkpoint. No biological record, curation event,
embedding, source-owned assertion or existing phenotype is changed. Native
VanM and Y51 findings are queued for validated qualitative curation; the
remaining primary-result and identity checks stay open. Focused tests,
projection reproduction and preservation checks are recorded in the verification
artifact; full authoritative QC is not rerun or claimed for this checkpoint.
All **2,939 records** remain in scope. No NCBI request, outreach, source adoption
or GitHub mutation occurred; #1040 remains deferred.

Artifacts: [reference and primary context](2026-10-10-glycopeptide-clusters-context.json),
[verification](2026-10-10-glycopeptide-clusters-verification.json).

## Vancomycin Native Curation

Two qualitative native-organism claims are now curated in vancomycin
(`CHEBI:28001`), with taxon grounding and explicitly reference-only UniProt
context. The named-compound join does not independently identify the tested
preparation or assign an exact experimental protein, allele or genome.

For E. faecium Efm-HS0661, the source reports vancomycin resistance and native
precursor evidence supporting a VanM-cluster-associated target-alteration route,
not isolated VanM sufficiency. Species `NCBITaxon:1352` is retained.
`UniProtKB:B8XGS3` and `FJ349556.1` supply source-bound reference context;
the entry's separate `CP039730.1` context belongs to another isolate and is not
assigned to Efm-HS0661. Laboratory-recipient results remain separate.
[Primary study](https://journals.asm.org/doi/10.1128/aac.01710-09).

For D. hafniense Y51, native resistance and separate recombinant-ligase
biochemistry support the proposed `DSY3690`-associated route. This is not a
claim of isolated-locus necessity or sufficiency, nor native precursor analysis.
Species `NCBITaxon:49338` and strain `NCBITaxon:138119` remain distinct.
The locus-matched `UniProtKB:Q24R63` reference is not interchangeable with the
`DSY1579`/`UniProtKB:Q24X74` biochemical comparator. The archive and sample
remain reference context, not the assay's experimental genome.
[Primary study](https://journals.asm.org/doi/10.1128/aac.01408-08).

The validated canary and final write preserve all twenty existing source-owned
resistance claims, three CDC/FDA activity observations, prior history and other
record fields. One meaningful curation event was added; status remains
`SEEDED`. No numerical AST, exact variants or laboratory procedures were added.
Teicoplanin remains unchanged because generic assay terminology does not resolve
the existing Teicoplanin A2-5 component identity.

The reconciled corpus has **4,823 resistance assertions**, including **68 curator
claims across 37 records**. All 2,938 other biological records are byte-identical
to the preceding checkpoint. All **2,939 embedding inputs** are unchanged, so
the existing vectors and projection remain valid without reencoding.

Verification: **167 focused tests passed**; the full suite reports **2,795 passed,
four existing skips and one existing LinkML deprecation warning**. All eleven
authoritative QC gates passed, including strict schema validation, exact corpus
reproduction and generated-site checks. Self-review found no supported defect;
this is not an independent review. The final preservation audit also checks the
content-addressed download, published links and all current record hashes.

All **2,939 whole-record primary reviews remain open**. No NCBI endpoint request,
outreach, source adoption or GitHub mutation occurred; #1040 remains deferred.

Artifacts: [primary context](2026-10-10-vancomycin-native-context.json),
[curation receipt](2026-10-10-vancomycin-native-curation.json),
[current census](2026-10-10-vancomycin-native-resistance-grounding.tsv),
[progress](2026-10-10-vancomycin-native-resistance-progress.json),
[verification](2026-10-10-vancomycin-native-verification.json).

## Vancomycin Follow-Up Curation

Five further qualitative findings are curated in vancomycin (`CHEBI:28001`).
Species grounding distinguishes E. faecalis (`NCBITaxon:1351`) from E. faecium
(`NCBITaxon:1352`); no strain TaxID is invented. UniProt links remain reference
context, not assignments of exact experimental proteins, alleles or genomes.

- **BM4405 / vanE:** native precursor evidence supports a cluster-associated
  target-alteration route. `UniProtKB:Q9S4K1` is a fragment, not a complete
  experimental protein. [Primary study](https://journals.asm.org/doi/10.1128/aac.43.9.2161).
- **N00-410 / vanE:** retain same-isolate co-occurrence with an `UNKNOWN` route;
  do not borrow BM4405 precursor findings. `UniProtKB:Q93A46` retains its
  differently recorded N00-0410 label.
  [Primary study](https://journals.asm.org/doi/10.1128/aac.46.6.1977-1979.2002).
- **N06-0364 / vanL:** the source explicitly leaves functionality unproven.
  The curated co-occurrence has an `UNKNOWN` route, with `UniProtKB:A9LN35`
  as reference context. Its source-reported phenotype is not a new clinical
  breakpoint interpretation. [Primary study](https://journals.asm.org/doi/10.1128/aac.01516-07).
- **UCN71 / vanN:** native precursor evidence supports a cluster-associated
  route. `UniProtKB:G4XFK8` has separate archive contexts for UCN71 and another
  isolate; neither these contexts nor UCN71's characterization are assigned to
  UCN72. [Primary study](https://journals.asm.org/doi/10.1128/aac.00714-11).
- **10/96A / vanD:** retain native phenotype and precursor evidence separately
  from comparator and laboratory-host findings. `UniProtKB:Q9EZQ9`/`AY082011`
  supplies source-bound reference context.
  [Primary study](https://journals.asm.org/doi/10.1128/aac.47.1.7-18.2003).

The VanE archive discrepancy now has an explicit, bidirectional crosswalk:
ENA marks [AF430807](https://www.ebi.ac.uk/ena/browser/api/summary/AF430807)
as suppressed and replaced by FJ872411; the
[replacement](https://www.ebi.ac.uk/ena/browser/api/summary/FJ872411)
lists AF430807 as a secondary accession. Both cite the N00-410 study.
Archive succession does not prove unchanged sequence or exact allele identity.
The already retrieved response and receipt are reused; no new metadata request
was needed for this checkpoint.

The validated canary and final write preserve all **22 previous resistance
claims**, three CDC/FDA observations, prior history and other fields. One
curation event was added; status remains `SEEDED`. Teicoplanin is unchanged:
its exact-component ambiguity persists, and conflicting wording in the VanD
source is not silently resolved. No numerical AST or laboratory instructions
were added. VanC, VanG and historical VanF follow-up remain open.

The corpus now contains **4,828 resistance assertions**, including **73 curator
claims across 37 records**. All 2,938 other records and all 2,939 embedding
inputs are unchanged. The earlier native-curation regression test still checks
its exact claim/history prefixes while allowing later, separately tested
additions; no preservation assertion was replaced by a skip.

Verification: **168 focused tests passed**; the full suite reports **2,813
passed, four existing skips and one existing LinkML deprecation warning**.
All eleven authoritative QC gates passed. The final audit checks corpus hashes,
archive/reference projections, source-slice preservation and the regenerated
content-addressed download. Self-review found no supported defect; it was not
an independent review. All **2,939 whole-record primary reviews remain open**.
No NCBI endpoint request, outreach, source adoption or GitHub mutation occurred;
#1040 remains deferred.

Artifacts: [primary context](2026-10-10-vancomycin-followup-context.json),
[curation receipt](2026-10-10-vancomycin-followup-curation.json),
[current census](2026-10-10-vancomycin-followup-resistance-grounding.tsv),
[progress](2026-10-10-vancomycin-followup-resistance-progress.json),
[verification](2026-10-10-vancomycin-followup-verification.json).

## CARD Parent-Term Reference Audit

The complete cohort of **43 previously unlinked CARD terms with named direct
subclasses** is audited across **50 compound records and 75 assertion
memberships**. Current hashes were checked for all 2,939 records, and complete
records were read through the collection-aware loader. This is a reference-scope
audit, not a completed primary review or new biological curation.

All **46 definition-citation UniProt queries** are complete in release
`2026_03`: 13 cached queries were reused and 33 new metadata-only queries were
retrieved after a successful canary. The queries contain 126 distinct entries;
28 return no entries. Thirteen terms have no definition citations in the pinned
ontology. Neither an empty query nor a missing citation establishes biological
absence.

Eleven parent terms have explicit UniProt links to named child terms. Across
the existing CARD snapshot and the citation queries, the dossier retains
**434 distinct reference proteins**; these are not 434 newly discovered
experimental assignments. Direct child edges remain separate from parents,
and grandchildren are not silently promoted to direct children. Child labels
are hashed rather than exporting variant details. All 43 parent accession
assignments remain empty.

Two source-label matches are retained strictly as citation-bound reference
candidates: ACC-1 / [UniProtKB:Q9XB24](https://www.uniprot.org/uniprotkb/Q9XB24/entry)
and flo / [UniProtKB:Q9F0D9](https://www.uniprot.org/uniprotkb/Q9F0D9/entry).
Literal synonym agreement and shared bibliography do not establish the exact
experimental allele, tested organism, genome or compound-specific phenotype.
Seven selected terms retain unresolved efflux-complex/subunit granularity;
one is an RNA term and must not be forced into a protein accession.

The 434 proteins have validated reference taxonomy across **106 TaxIDs**, using
the existing UniProt snapshot plus two separately validated UniProt taxonomy
responses. Both additional TaxIDs are strain-ranked;
their rank and reference-only scope are preserved. No experimental strain or
species assignment is inferred from those entries. NCBI endpoints were not
contacted, #1040 remains deferred, and no source adoption or GitHub mutation
occurred.

No biological records, generated pages, embeddings, source inventories or
existing tests were changed by this audit. The previous curation total remains
**73 curator claims across 37 records**, within 4,828 resistance assertions.
All 2,939 whole-record primary reviews remain open. **250 focused tests passed**.
Offline reproduction and preservation checks are recorded in the
[verification](2026-10-10-card-parents-verification.json); the previous full QC
result remains the biological baseline, not a new full-suite run.

Artifacts: [reference dossier](2026-10-10-card-parents-context.json),
[offline audit](../scripts/audit_card_parent_references.py),
[regression tests](../tests/test_card_parent_references.py).

## CARD Parent Primary Curation

Primary follow-up covers the two literal-name leads and their **11 compound
records**. Three primary studies were inspected at the relevant result,
subject and accession locations. A fourth definition citation, PMID:15914491,
is a review and was not promoted into another experiment.

**Ten qualitative co-occurrences** were added across chloramphenicol and
florfenicol. Four named avian E. coli isolates retain separate observations;
the flo/cmlA-positive bovine subgroup remains a separate, unnamed subgroup.
All new claims use species `NCBITaxon:562`, retain `UNKNOWN` mechanism and
explicitly avoid isolated-gene causation or new clinical breakpoint calls.
No numerical AST, exact allele, experimental protein or genome was added.
See the [avian study](https://journals.asm.org/doi/10.1128/aac.44.2.421-424.2000)
and [bovine study](https://journals.asm.org/doi/10.1128/jcm.38.12.4593-4598.2000).

The bovine paper's AF252855.1 deposit links to `UniProtKB:Q9F0D9`, but that
entry also contains a later EC56 submission. Neither context is assigned to
the avian isolates, and EC56 is not substituted for the bovine subgroup.
`UniProtKB:Q9XB24` separately binds the original KUS/AJ133121 context and
other isolate submissions. The [ACC-1 study](https://journals.asm.org/doi/10.1128/aac.43.8.1924)
distinguishes native and laboratory-host findings; its nine compound records
remain unchanged rather than receiving one uniform native resistance claim.

The chemical preflight also found an explicit **cefotetan identity hold**:
its stored InChI and InChIKey agree (`SRZNHPXWXCNNDU-IXOPCIAXSA-N`), while
RDKit recomputation from its stored SMILES gives
`SRZNHPXWXCNNDU-RHBCBLIFSA-N`. No chemical correction was inferred or applied.
The [current ChEBI page](https://www.ebi.ac.uk/chebi/CHEBI:3499) displays the
same structural fields; the discrepancy was not introduced by this curation.
Both compounds selected for curation pass the InChI, SMILES and stored-key
crosscheck; tested preparations were not independently re-identified.

Validated canaries preserve all 88 previous chloramphenicol claims and all 11
previous florfenicol claims, existing activity evidence and other fields.
Two meaningful curation events were added. All 2,939 embedding inputs remain
unchanged. The corpus now has **4,838 resistance assertions**, including
**83 curator claims across 38 records**. Historical tests retain exact old
claim/history prefixes and reconstruct the prior record hashes, rather than
skipping preservation checks after an append-only curation.

All **11 authoritative QC gates passed**: the full suite completed with
**2,862 passed, four existing skips and one existing warning**. All **204
focused tests passed**. The skip identities and reasons match the previous
biological QC baseline; the warning remains the SSSOM/LinkML deprecation.
The first focused run found two literal-wording mistakes in a new test.
Those expectations were corrected without changing biological data, and the
failed run's log and test report are retained alongside the successful rerun.
The saved adversarial self-review found no supported new-claim defects; it
is not an independent review and retains the cefotetan identity hold.

All 2,939 whole-record primary reviews remain open. No NCBI endpoint request,
outreach, source adoption or GitHub mutation occurred; #1040 remains deferred.

Artifacts: [primary context](2026-10-10-card-parent-primary-context.json),
[curation receipt](2026-10-10-card-parent-primary-curation.json),
[current census](2026-10-10-card-parent-primary-resistance-grounding.tsv),
[progress](2026-10-10-card-parent-primary-resistance-progress.json),
[verification](2026-10-10-card-parent-primary-verification.json).

## Efflux Parent Reference Identity

The seven efflux-parent terms flagged by the preceding audit span **13 source
memberships across 10 records**. Their 35 parent/child ontology bindings were
checked without propagating child accessions. The entity review separates one
multi-protein complex, four gene-variant categories, and two gene-family
categories; sharing an efflux ancestor does not identify one protein or a
validated transport mechanism.

For MexEF-OprN, sequence-free UniProt metadata resolves separate reference
components: `mexE` / `Q9I0Y9`, `mexF` / `Q9I0Y8`, and `oprN` / `Q9I0Y7`, all
in reference strain `NCBITaxon:208964`, under species `NCBITaxon:287`.
The [primary source](https://journals.asm.org/doi/10.1128/jb.181.20.6300-6305.1999)
distinguishes the component proteins, regulator, and experimental backgrounds.
None of these accessions is assigned to the entire complex or to every subject.
OprN's explicit `ARO:3000805` cross-reference is retained at that term, not
relabeled as the complex parent or its different named subclasses.

The iniA, iniB and iniC searches retain **six** reviewed reference entries:
one per gene in each of `NCBITaxon:83331` and `NCBITaxon:83332`, both strain
children of species `NCBITaxon:1773`. No representative strain is selected.
The [iniB definition citation](https://journals.asm.org/doi/10.1128/aac.44.2.326-336.2000)
explicitly warns in its concluding Summary that association does not prove
causation. This qualifies a primary-evidence interpretation of the source's
stronger wording; it does not by itself authorize deletion of the retained
CARD assertion. The same paper is an independently traced context for iniA
and iniC, not an invented definition citation. Exact alleles and causal routes
remain unresolved.

Yor1 maps at reference-locus scope to unreviewed `UniProtKB:Q6FTR9`,
`CAGL0G00242g`, in `NCBITaxon:284593`, under species `NCBITaxon:5478`.
The [2010 study's annotation tables](https://journals.asm.org/doi/full/10.1128/aac.00535-10)
retain the historical name's homology context. The independently discovered
[2022 follow-up](https://journals.asm.org/doi/10.1128/mbio.03545-21) distinguishes
context-dependent gene-level susceptibility findings from direct drug transport.
Neither establishes the ontology's posaconazole-associated allele, and a
transport observation for one drug is not generalized to every azole.
The fungal MDR1 family remains without a single selected organism or protein;
its 19 named descendants are not propagated to the parent. The previous flo
reference/subject review and ten curated qualitative claims remain unchanged.

The dossier records **10 reference proteins and seven verified TaxIDs**, using
11 bounded metadata requests to UniProt and Europe PMC. These counts describe
this follow-up, not globally novel accessions. Mex and ini queries
were reviewed-entry searches, not exhaustive searches of unreviewed proteins.
All references remain distinct from experimental proteins, alleles and genomes.
No new biological record, curation event, numerical AST, sequence or variant
specification was written. NCBI access and #1040 remain deferred.

Research-only checks passed: **219 focused tests**, repository lint and
byte-identical metadata reproduction. The preservation audit verifies all
2,939 record hashes and unchanged source inputs, generated pages and embedding
artifacts, including ignored files. The saved adversarial self-review retains
the ini causal-evidence and Yor1 allele/transport scope holds; it is not an
independent review. No full QC rerun is claimed: the preceding biological
checkpoint remains the last authoritative full-suite result. All 2,939 records
remain in scope, and whole-record primary review remains open.

Artifacts: [reference dossier](2026-10-10-efflux-entities-context.json),
[regression tests](../tests/test_efflux_entity_references.py),
[verification](2026-10-10-efflux-entities-verification.json).

## FR171456 Primary Curation

On 2026-10-11 UTC, repository access was restored and the staged FR171456
evidence was revalidated before curation. The existing
[FR171456 record](../data/antibiotics/antifungal/fr171456.yaml), `CHEBI:88298`,
retains Standard InChIKey `JAHGNOXPMXOEJS-BSPLYONXSA-N`; its stored key,
SMILES-derived key and InChI-derived key agree. This checks the local chemical
representation, not the identity of the physical preparation tested in the paper.

One qualitative **ERG26-associated resistance** claim was added for laboratory
*Saccharomyces cerevisiae* derivatives, supported by selected results in
[Helliwell et al. (2015), PMID:26456460](https://www.nature.com/articles/ncomms9613).
The review inspected native Figures 2 and 3 and supplementary pages 6, 9 and 13
(Figures 6 and 9 and Table 3), not the whole paper. The claim does not imply a
clinical or species-wide phenotype. Resistant isolates without ERG26 changes
remain explicitly unexplained. Parent FR171456 is kept separate from the
paper's derivative compounds; no numerical AST or exact variant specification
was added.

Four reviewed reference entries were checked against **UniProt release 2026_03**:

| Gene | Reference UniProtKB entry | Reference locus | Entry version |
|---|---|---|---:|
| ERG26 | [P53199](https://www.uniprot.org/uniprotkb/P53199/entry) | YGL001C | 201 |
| HMG1 | [P12683](https://www.uniprot.org/uniprotkb/P12683/entry) | YML075C | 231 |
| HMG2 | [P12684](https://www.uniprot.org/uniprotkb/P12684/entry) | YLR450W | 217 |
| YOR1 | [P53049](https://www.uniprot.org/uniprotkb/P53049/entry) | YGR281W | 218 |

All four have sequence version 1 and reference-strain taxonomy
`NCBITaxon:559292` (S288c). UniProt taxonomy confirms its parent species as
`NCBITaxon:4932`; only the species identifier is assigned to the resistance
claim. These are reference identities, not experimental allele, derivative or
genome assignments, and not necessarily globally new accessions. HMG1/HMG2
modifier interpretations and YOR1 transport interpretation remain outside the
accepted claim. The primary text's `YPR090w`/`YPL090w` conflict remains a hold;
Figure 2 labels `YPR090w`, but no silent locus correction was made.

The validated canary and adversarial **self-review, not independent review**
preceded the record write and its single curation event. All other record fields
and history were preserved, and the other **2,938 records are byte-identical**.
The inventory now contains **4,839 resistance assertions**, including **84
curator claims across 39 records**; these are coverage counts, not completed
primary-review counts. The embedding refresh changed one document, reused all
2,938 unaffected vector rows byte-for-byte and rebuilt the projection with
fingerprint `47f50d3dae02f512`.

Verification passed **139 focused tests** and all **11 authoritative QC gates**:
**2,886 tests passed, 4 skipped**, with one LinkML dependency warning. Strict
validation found no errors in 2,939 records; corpus reproduction found no drift,
and the generated site and maps are current. QC caught a stale `NEXT_TASKS.md`
coverage count, corrected from 410 to 411 without weakening its test. The failed
run, isolated reproduction and successful retry remain separately recorded.
The apply-time curation snapshot is preserved; the final verification records
its subsequent QC outcome. No live-browser check is claimed.

No NCBI endpoint requests, source adoption or GitHub mutations occurred; #1040
remains deferred. All **2,939 records remain in scope**, and no whole-record
primary review was completed by this selected-evidence checkpoint.

Artifacts: [reference dossier](2026-10-11-fr171456-context.json),
[curation snapshot](2026-10-11-fr171456-curation.json),
[census](2026-10-11-fr171456-resistance-grounding.tsv),
[reconciliation](2026-10-11-fr171456-checkpoint-reconciliation.json),
[progress index](2026-10-11-fr171456-resistance-progress.json),
[regression tests](../tests/test_fr171456_curation.py),
[verification](2026-10-11-fr171456-verification.json).

## Remaining work

1. Review primary results for every existing PHI-base association, including
   donor/host context, reference numbering, strain identifiers, and negative
   or discordant findings. Resolve the flagged cases before changing them.
   In particular, reconcile the T1FOA-associated caspofungin source interpretation
   with Park Table 4's distinct analogue before treating that phenotype as verified.
   Keep PMID:26596626's azoxystrobin co-occurrence separate from allele-specific
   causation; its parent is also reported resistant. Other OA leads
   still need their unresolved authoritative locus crosswalks checked before
   further identifier curation. SDH8's reference alias is now resolved through
   CGD; its exact experimental allele remains unresolved.
   Check Ren's indexed Sg-28 discrepancy against the original tables before
   importing measurements; the subject-label review does not resolve that discrepancy.
2. Finish curator-claim review beyond the taxon and reference assignments already
   documented, including unresolved exact alleles. Review the 978 CARD
   determinants with reference candidates and investigate the 1,024 without
   explicit links. The ontology-scope audit identifies 88 rRNA-ancestor terms
   (87 RNA labels and one protein-definition conflict) and 14 whole-cluster
   terms. Do not force true RNA loci or whole clusters into single-protein
   mappings. The name crosswalk resolves 86 term labels to 33 species TaxIDs,
   not experimental organisms; resolve locus/component and tested-subject
   context before biological curation. The rplD follow-up supports protein
   identity and retains two separate reference entries; experimental allele
   and phenotype joins remain unresolved. Do not override source assertions
   or select a representative reference. Review
   efflux granularity, the 43 unlinked terms with named subclasses, and the
   three flagged determinant-ancestry gaps without propagating child accessions
   or deleting source assertions. Their fungal follow-up now verifies explicit
   source edges and two separate reference proteins, but retains source-name,
   UPC2-context and experimental-identity ambiguities. These flags and reference
   crosswalks do not finish primary review.
   The structural-reference audit now adds six explicitly scoped PDB-to-UniProt
   paths, including a rejected cross-species assignment and unresolved allele
   and experimental contexts. The APH Id-to-IVa nomenclature relation is now
   verified; this does not resolve its compound-specific assays. EmrD's listed
   erratum still needs inspection. Review their primary papers before promoting
   any structural reference to an experimental resistance claim. Oleandomycin
   now has two primary-backed biochemical routes, but exact experimental allele,
   whole-cell phenotype and broader source-assertion review remain open.
   Do not treat family-level assertions as exact protein,
   allele, or isolate assignments. Resolve dasabuvir's and paritaprevir's compound-form questions
   before expanding their resistance grounding; daclatasvir's taxonomic update
   likewise does not establish its administered form.
   The LmrC primary-context review distinguishes native and laboratory-host
   results but does not resolve tested chemical forms, exact alleles or the
   celesticetin resistance assertion; its two UniProt candidates remain separate.
3. Review HIVDB primary evidence and resolve supported reference accessions
   beyond the verified source-region/taxon context. Retain algorithm rules as
   rules rather than measured phenotypes or biochemical mechanisms.
4. Initial searches are complete for all names currently recorded. Investigate
   historical names not yet captured in records. Of 612 truncated query-record
   memberships (611 distinct queries), all **611 selected cursor traversals
   are complete** after whole-chain recovery of the final five conflicts.
   Preserve all four retrieval histories. Refine ambiguous short aliases in
   separately identified queries; the large
   polysulfur `S`/`Sn` query is not a collection of verified chemical matches.
   The complete default-order amikacin canary is explicitly reused as a whole
   chain; its sorted counterpart remains separate. The ampicillin ordering
   canary likewise preserves both attempts, selecting its date-sorted chain.
   Neither agreement nor recovery establishes the cause of earlier failures.
   Prioritize primary
   evidence behind all candidate citations, including completed traversals.
   The earlier 121 truncated no-claim canonical searches are a
   subset, not additional completed reviews. Keep curated cerulenin and
   5-fluorouracil and flucytosine in scope; their limited claims do not complete
   all possible organism/allele coverage.
   For hygromycin B, resolve the VJY305/SKY252 versus VJY305/SKY242 source-label
   conflict; the cited original Table S2 now corroborates SKY252, but does not
   establish a correction to SKY242. Inspect the older study's original figures and resolve its
   experimental identity and cross-study comparability. Its primary Results
   have now been reviewed through an author-uploaded text transcription; the
   disagreement's cause remains unknown. Figure review and canonical reference
   crosswalks do not complete the record's biological evidence review.
   The three additional yeast studies now have primary figure/text review and
   seven focal reference-gene mappings, including negative findings; their
   experimental allele, strain and genome accessions remain unresolved.
   Keep GM193663's five qualitative gene associations in scope: figure and
   supplement review, exact experimental identifiers and broader evidence
   coverage remain pending. The 2013 sordarin sodium-salt study is not a
   neutral-sordarin or GM193663 observation. Cordycepin remains a reference lead.
   Papulacandins B and D now have three qualitative gene associations; figure
   review and exact experimental identifiers remain unresolved. Papulacandin A
   and arborcandin C remain uncurated from the latest follow-up. Resolve the
   latter's conflicting subject labels before importing a genotype-phenotype join.
5. Curate supported findings through source-owned inputs; normalize MICs to
   mg/L where reported, keep EC50 and disk-diffusion measurements distinct, and
   never infer clinical resistance from a number without its source interpretation.
6. Verify full-corpus coverage and all curation/publication gates before calling
   the requested investigation complete. The BGE/PaCMAP refresh is now published
   with an exact baseline-reuse proof for the current epidermin/microcin C
   checkpoint. All authoritative QC gates passed after genuine encoding of both
   changed documents and a full projection refresh; all other 2,937 vector rows
   remain byte-identical. Earlier verification receipts remain historical and
   unchanged.
   Rerun the applicable gates after subsequent edits. Future
   embedded-field changes require a genuine vector and projection refresh,
   never a fingerprint-only correction. Passing gates does not finish primary
   evidence review of every record.
