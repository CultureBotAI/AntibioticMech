# Reviewed MIBiG producer import plan

Date: 2026-08-31  
Issue: #104

## Decision

Adopt MIBiG 4.0.1 producer/BGC assertions under CC BY 4.0, but keep the first
release deliberately narrow. An entry is eligible only when it is `active` and
at least one changelog event names a reviewer other than MIBiG's
`AAAAAAAAAAAAAAAAAAAAAAAA` migration placeholder. `active` alone is not called
reviewed: most active v4 records are legacy migrations with `quality:
questionable`.

Compound identity is an exact Standard InChIKey join. A connectivity-only match,
an unassigned potential stereocentre, or more than one corpus record for a key is
reported but never written. MIBiG bioactivity labels are ignored.

## Work packages

1. Add a pinned MIBiG source declaration and a standalone archive extractor.
   Commit the compact producer inventory and its archive/inventory hashes, not
   the downloaded archive.
2. Publish dry-run counts for matched, ambiguous, rejected, and out-of-scope
   compounds before applying the seed.
3. Extend `ProducerOrganism` with source, source version, quality, and reviewed
   provenance fields.
4. Attach MIBiG producers by exact key while preserving curator-authored
   producers. Make corpus reproduction compare only the MIBiG-owned slice.
5. Regenerate records, generated schema/site/map artifacts, and run `just qc`.

## Evidence contract

Each emitted producer claim carries the NCBI taxon, MIBiG BGC accession, MIBiG
entry version and quality, an explicit reviewed flag, and the first
compound-specific MIBiG reference or (for migrated entries) the first listed
legacy reference. The extractor records which fallback supplied that reference.

No field in `activity_spectrum`, including MIC, is populated by this import.

## Completion

Implemented 2026-08-31. The pre-write dry run yielded 3 matched, 17 ambiguous,
0 rejected, and 23 out-of-scope compound rows. The seed added producer claims to
vancomycin, streptothricin D, and streptothricin F. Review round 1 found and
fixed two provenance/robustness defects before commit: Zenodo's named `.tar.gz`
asset is currently an uncompressed tar stream, and the first draft of the dry-run
report transcribed the wrong archive SHA-256. The corrected extractor auto-detects
tar compression and the report now matches `data/raw/MANIFEST.yaml`.

Final verification: 149 tests passed; 2,923 strict schema validations passed;
corpus reproduction, provenance, source-queue policy, chemical-map quality, and
generated-site freshness all passed via `just qc`.
