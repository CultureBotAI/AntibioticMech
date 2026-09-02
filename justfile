# AntibioticMech — individual chemical structures with antimicrobial activity

set positional-arguments := true

schema := "src/antibioticmech/schema/antibioticmech.yaml"
corpus := "data/antibiotics"

default:
    @just --list --unsorted

# Install package + dev tools
install:
    uv sync --extra dev --extra chemical-map

# Generate Pydantic classes from the LinkML schema
gen-schema:
    uv run gen-pydantic {{schema}} > src/antibioticmech/schema/antibioticmech_dataclasses.py

# Show what extraction would produce, without writing (free check before the real run)
extract-inventory-dry:
    uv run python scripts/extract_source_inventory.py --dry-run

# Re-extract data/raw/ from ChEBI and CARD. Only needed when those release;
# the inventories are committed, so seeding, validation and tests all run offline.
extract-inventory *args:
    uv run python scripts/extract_source_inventory.py {{args}}

# Extract reviewed MIBiG producer/BGC assertions. RDKit converts upstream
# SMILES to the Standard InChIKey used for the exact corpus join.
extract-mibig *args:
    uv run --extra chemical-map python scripts/extract_mibig_producers.py {{args}}

extract-mibig-dry *args:
    uv run --extra chemical-map python scripts/extract_mibig_producers.py --dry-run {{args}}

# Join Drugs@FDA regulatory tables to exact GSRS/UNII structures.
extract-fda *args:
    uv run --extra chemical-map python scripts/extract_fda_clinical_status.py {{args}}

extract-fda-dry *args:
    uv run --extra chemical-map python scripts/extract_fda_clinical_status.py --dry-run {{args}}

# Evaluate BindingDB's curated-only article export without writing target claims.
evaluate-bindingdb *args:
    uv run --extra chemical-map python scripts/evaluate_bindingdb_targets.py {{args}}

# Extract BindingDB-curated quantitative targets. All four pinned archives are
# explicit arguments so a release refresh cannot silently mix versions.
extract-bindingdb *args:
    uv run --extra chemical-map python scripts/extract_bindingdb_targets.py {{args}}

extract-bindingdb-dry *args:
    uv run --extra chemical-map python scripts/extract_bindingdb_targets.py --dry-run {{args}}

# Extract ChEBI-grounded PHI-base gene--antimicrobial resistance observations.
extract-phibase *args:
    uv run python scripts/extract_phibase_amr.py {{args}}

extract-phibase-dry *args:
    uv run python scripts/extract_phibase_amr.py --dry-run {{args}}

# Evaluate CRyPTIC phenotypes without attaching name-only drug codes to records.
evaluate-cryptic *args:
    uv run --extra source-ingest python scripts/evaluate_cryptic_activity.py {{args}}

# Compare AMRFinderPlus families/classes with the committed ARO resistance slice.
evaluate-amrfinder *args:
    uv run python scripts/evaluate_amrfinderplus.py {{args}}

# Find exact-ligand PDB entries that overlap established BindingDB UniProt targets.
evaluate-rcsb-pdb *args:
    uv run python scripts/evaluate_rcsb_pdb.py {{args}}

# Free check: print the PubChem URL for the first molecule needing a structure
extract-pubchem-dry:
    uv run python scripts/enrich_pubchem_structures.py --dry-run

# One real PubChem call — the canary before the batch. `just extract-pubchem-canary ARO:0000018`
extract-pubchem-canary *args:
    uv run python scripts/enrich_pubchem_structures.py --only "$@"

# Fetch structures for every ARO molecule ChEBI does not cover (~270 calls)
extract-pubchem *args:
    uv run python scripts/enrich_pubchem_structures.py {{args}}

# Dry-run the seed: harmonize the inventories and report the record counts that
# WOULD be written, per class. No files touched.
seed:
    uv run python scripts/seed_from_sources.py

# Seed exactly one record end to end and validate it — the canary to run before
# any bulk write. `just seed-canary CHEBI:48923`
seed-canary *args:
    uv run python scripts/seed_from_sources.py --apply --only "$@"

# Write every record under data/antibiotics/<class>/<slug>.yaml.
# Run `just seed` and `just seed-canary` first.
seed-apply *args:
    uv run python scripts/seed_from_sources.py --apply {{args}}

# Validate a single record against the schema
validate file:
    uv run linkml-validate -s {{schema}} --target-class AntibioticRecord {{file}}

# Validate every record. Delegates to validate-strict (closed mode: unknown
# fields are errors, not silently accepted as in linkml-validate's open mode).
validate-all *args:
    @just validate-strict {{args}}

# Strict in-process validation in closed mode. Emits
# reports/instance_validation_failures.tsv and exits 1 on any ERROR.
validate-strict *args:
    uv run python scripts/validate_strict.py {{args}}

# Verify data/antibiotics/ is exactly what data/raw/ produces. Schema validation
# checks each record's shape but not its content; without this a hand-edited or
# drifted record passes every other check.
verify-corpus *args:
    uv run python scripts/verify_corpus.py {{args}}

# The curation backlog: source concepts with no structure, records with no
# mechanism, and minted identities that still need a grounding decision.
worklist *args:
    uv run python scripts/curation_worklist.py {{args}}

# Every unsigned record, ordered by its next evidence-review gate. The TSV is
# a restartable checkpoint; literature references in it are discovery leads.
review-queue *args:
    uv run python scripts/curation_worklist.py --queue review-readiness {{args}}

# The prioritized data-source queue: what to adopt next, and what is still
# unverified about it. `.claude/skills/source-queue` triages it.
source-queue:
    uv run python scripts/check_source_queue.py

# Corpus report: records per class, structure coverage, source corroboration,
# and the mechanism/resistance coverage that curation is filling in.
report *args:
    uv run python scripts/antibiotic_report.py {{args}}

# Render the browsable site under pages/ from the corpus. Committed and served
# from the branch root, so it can go stale exactly as records can; `--check` fails when it has.
render *args:
    uv run python scripts/render_pages.py {{args}}

# Fail if pages/ is out of step with the corpus
render-check:
    uv run python scripts/render_pages.py --check

# Recompute the exact structure-only chemical embedding, then publish it.
chemical-map:
    uv run --extra chemical-map python scripts/generate_chemical_map.py
    uv run python scripts/render_pages.py

# Fast deterministic staleness, coverage, and scientific-quality check.
chemical-map-check:
    uv run --extra chemical-map python scripts/generate_chemical_map.py --check

# Expensive local reproducibility audit: rerun fingerprints, distances, and UMAP.
chemical-map-recompute-check:
    uv run --extra chemical-map python scripts/generate_chemical_map.py --check --recompute

# Verify every committed inventory is covered by MANIFEST.yaml and matches it
provenance-check:
    uv run python scripts/check_provenance.py

# Refresh the generated current-corpus block in README.md
docs-stats:
    uv run python scripts/check_docs.py --write

# Fail if README.md's current-corpus block is out of step with the corpus
docs-check:
    uv run python scripts/check_docs.py --check

# Run the test suite
test *args:
    uv run pytest {{args}}

# Deep research for one compound. Dry-run by default; pass --apply for one
# real canary after `just deep-research-canary <provider>`.
research-antibiotic provider target *args="":
    uv run python scripts/research_antibiotic.py \
      --provider {{provider}} --target {{target}} {{args}}

research-entity provider target *args="":
    @just research-antibiotic {{provider}} {{target}} {{args}}

# Search publication APIs for candidate reports of newly discovered antibiotics.
# PubMed and Semantic Scholar work without keys at their public limits;
# Google Scholar uses SerpAPI and requires SERPAPI_API_KEY.
search-publications *args:
    uv run python scripts/search_publications.py {{args}}

# Non-billing configuration/capability checks.
deep-research-canary provider="all" *args="":
    uv run python scripts/deep_research_contract.py {{provider}} \
      --client-command "uvx --python 3.12 --prerelease=allow --from deep-research-client[cyberian] deep-research-client" \
      {{args}}

# Lint
lint *args:
    uv run ruff check {{args}} .

# Auto-fix lint findings
lint-fix:
    uv run ruff check --fix .

# Show the documents that WOULD be embedded, and their size distribution. Free.
embed-dry:
    python3 scripts/embed_records.py --dry-run

# Embed ONE small batch end to end — the canary before the full run.
embed-canary *args:
    python3 scripts/embed_records.py --limit 20 {{args}}

# Text-embed every record with a local model (needs the `embed` extra and runs
# on system python, so torch stays out of the core install). ~2 min for the
# corpus on Apple-Silicon MPS. Writes data/embeddings/ (vectors gitignored).
embed *args:
    python3 scripts/embed_records.py {{args}}

# Project the embeddings to 2-D -> data/embeddings/corpus_map.json (committed).
# Run `just render` afterwards to rebuild pages/map.html from it.
embed-map *args:
    python3 scripts/embed_map.py {{args}}

# The authoritative quality gate used both locally and in CI.
qc:
    uv run --extra chemical-map python scripts/run_qc.py
