# BindingDB-curated target evaluation plan

Date: 2026-08-31  
Issue: #103

## Decision boundary

Evaluate BindingDB's explicitly curated-article TSV as a candidate target lane,
but do not write `MolecularTarget` claims until issue #93 distinguishes direct
targets from susceptibility/resistance determinants and the schema can retain
the quantitative measurement and assay context.

## Gates

1. Require the row-level `Curation/DataSource` value `Curated from the
   literature by BindingDB`, even inside the curated-only archive.
2. Match the reported full ligand InChIKey to exactly one corpus record, then
   recompute the Standard InChIKey from ligand SMILES and require equality.
3. Require an Article DOI or PMID and at least one reported Ki, IC50, Kd, or
   EC50 value.
4. Resolve the curated target-organism name against a pinned NCBI taxonomy dump
   and accept only Bacteria, Archaea, Fungi, or Viruses. Reject unresolved,
   ambiguous, metazoan, plant, and conservatively unclassified eukaryotic rows.
5. Treat organism-specific UniProt accessions only as future
   `ProteinExample` candidates, never as the taxon-agnostic target identifier.
6. Report every exclusion category and representative accepted rows before any
   corpus-write implementation is considered.

The evaluator is non-writing by construction and prints a machine-readable JSON
reconciliation report.
