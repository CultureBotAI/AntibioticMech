# Stage 5 Validation Report (`mech-goal-sequence-20261019`, Cycle 5, Stage 5)

## Executed Validation Gates and Command Provenance

1. **Native Writer Remediation and Transition Manifest Generation**
   - Curated `mode_of_action` and `PRIMARY_LITERATURE` `molecular_targets` on the 5 Cycle 5 Stage 1 natural products (`#1321`) and 5 `EXACT` quinolones/fluoroquinolones (`#1322`), updated [`curation/uniprot_protein_examples.yaml`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/uniprot_protein_examples.yaml) (`records=84`, `held_targets=78`, `sha256=e7552fa9302bc985a7ea2b40c4e469255f104eb9000b60cc1a3853748827a44c`) and [`curation/uniprot_protein_examples_transition.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/uniprot_protein_examples_transition.json) (`sha256=ae82243e571fd68591a17a2adf28a493267a01c3bf12f9eea9286c59eb75d584`), promoted all 15 `EXACT` ChEBI records (`pentabromopseudilin`, `taromycin-a`, `pneumocandin-a0`, `rustmicin`, `soraphen-a`, `naphthomycin-a`, `resistomycin`, `micacocidin`, `kendomycin`, `endophenazine-a`, `cinoxacin`, `Grepafloxacin`, `moxifloxacin`, `sparfloxacin`, `lomefloxacin`) to `curation_status: REVIEWED` via `record_curation_event` and `write_validated_antibiotic`, updated [`curation/causal_graphs.yaml`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/causal_graphs.yaml) (`held_records` `count=53`, `sha256=1df9c01698a7681f9524f991212b8fe12c9c4736427d85dbec433a334b2bc8e0`), and recorded [`curation/cycle5_stage5_review_remediation_transition.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/cycle5_stage5_review_remediation_transition.json) (`sha256=6278fc9de9ab3b1ceb3718f2760893b6e624f35e8fc362d65e713407c1de956b`) (`BypassSandbox: true`, exit code `0`).

2. **Closed LinkML Schema and OAK Ontology Label Validation ([`scripts/validate_strict.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/validate_strict.py))**
   - Command (`BypassSandbox: false`): `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv`
   - Exit Code: `0`
   - Literal Summary Output:
     ```text
     === validate-strict summary ===
       files scanned:      3064
       files with ERROR:   0
       total ERROR rows:   0
       TSV:                /tmp/instance_validation_failures.tsv
     ```

3. **Full Corpus Seed Reproduction Check ([`scripts/verify_corpus.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/verify_corpus.py))**
   - Command (`BypassSandbox: false`): `.venv/bin/python scripts/verify_corpus.py`
   - Exit Code: `0`
   - Literal Output:
     ```text
       1 CARD cross-reference(s) refused as self-contradictory (see `just worklist --queue crossref-conflict`)
         ARO:3000337: CARD links ARO:3000337 (iclaprim) to CHEBI:31724 (Isoaminile citrate), but the names differ and the CAS numbers disagree (192314-93-5 vs 28416-66-2). Cross-reference not trusted for roles, structure or identity.
     records expected: 3064   on disk: 3064
     missing: 0   unexpected: 0   drifted fields: 0
     identifiers absent from PATHS.tsv: 0   stale lockfile rows: 0

     corpus reproduces exactly from data/raw/ plus curator inputs.
     ```

4. **Review-Readiness Queue Refresh ([`scripts/curation_worklist.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/curation_worklist.py))**
   - Refreshed [`curation/record_review_queue.tsv`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/record_review_queue.tsv) (`sha256=540b92c8691c08813862fc5f8495bdb9d9e8c619bca5ae04e88321c939101683`): `2,937` unsigned items (`REVIEWED` count increased from `112` to `127`; `PROPOSED` count decreased from `137` to `127`; `SEEDED` count decreased from `2,815` to `2,810`).

5. **Chemical Structure Map and PaCMAP Corpus Map Refresh ([`data/embeddings/chemical-structure-map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/chemical-structure-map.json), [`data/embeddings/corpus_map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/corpus_map.json))**
   - Refreshed [`data/embeddings/chemical-structure-map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/chemical-structure-map.json) (`input_hash=62c5527d239d67f59494297b6a82d4443ab4b12e53498b58ffbeceea487bb558`) and [`data/embeddings/corpus_map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/corpus_map.json) (`corpus_fingerprint=488fb6ad856e7056`).
   - Chemical Structure Map Check (`BypassSandbox: false`):
     - Command: `/private/tmp/antibioticmech-rdkit/bin/python scripts/generate_chemical_map.py --check`
     - Exit Code: `0`
     - Literal Output: `chemical map is current: 3064 records, trustworthiness@10=0.9695, neighbor-overlap@10=0.4922`

6. **README Statistics and Static Site Pages Synchronization ([`scripts/check_docs.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/check_docs.py), [`scripts/render_pages.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/render_pages.py), [`NEXT_TASKS.md`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/NEXT_TASKS.md))**
   - Updated [`NEXT_TASKS.md`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/NEXT_TASKS.md) (`479` records with target or resistance evidence; `84` populated `PRIMARY_LITERATURE` `MolecularTarget` entries with reviewed `UniProtKB` `protein_examples` and `78` `held_targets`).
   - Refresh Run (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError` writing to `README.md` / `pages/`):
     - Command: `.venv/bin/python scripts/check_docs.py --write` and `.venv/bin/python scripts/render_pages.py`
     - Exit Code: `0`
     - Literal Output:
       ```text
       README statistics refreshed.
       corpus_map.json: 3064 points (pacmap) -> /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/corpus_map.json
       rendered 3064 compound pages, 7 classes, pruned 1 stale -> /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/pages
       ```
   - Static Site Pages Check (`BypassSandbox: false`):
     - Command: `.venv/bin/python scripts/render_pages.py --check`
     - Exit Code: `0`
     - Literal Output: `pages/ is in step with the corpus`

7. **Native Structured Review Bundle Save, Validate, and Append-Only Check ([`scripts/record_review.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/record_review.py))**
   - Save Bundle (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'Users'` in `scripts/record_review.py:_directory`):
     - Command: `.venv/bin/python scripts/record_review.py save --content /Users/marcin/.gemini/antigravity-cli/brain/75d4a007-e80b-4cd0-a885-0beb737cc7bf/scratch/remediated_review.yaml`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"review": "/Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/reviews/structured/20261105T004500Z-cycle5-stage5-remediated-records-review/review.yaml", "markdown": "/Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/reviews/structured/20261105T004500Z-cycle5-stage5-remediated-records-review/review.md"}
       ```
   - Validate Saved Bundle (`BypassSandbox: false`):
     - Command: `.venv/bin/python scripts/record_review.py validate reviews/structured/20261105T004500Z-cycle5-stage5-remediated-records-review/review.yaml`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"valid_reviews": 1}
       ```
   - Append-Only Check Across All 18 Structured Review Bundles (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'Users'`):
     - Command: `.venv/bin/python scripts/record_review.py check --require-reviews --base main`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {
         "repository": "culturebotai/AntibioticMech",
         "valid_reviews": 18,
         "coverage": "declared_scopes_only"
       }
       ```

8. **Pytest and Ruff Validation Suites**
   - UniProt Protein Examples, Causal Graphs, Review-Readiness Queue & Embeddings Suites (`BypassSandbox: false`):
     - Command: `.venv/bin/python -m pytest -q tests/test_uniprot_protein_examples.py tests/test_causal_graphs_curation.py tests/test_review_readiness_queue.py tests/test_embeddings.py`
     - Exit Code: `0` (`175 passed`).
   - Ruff Linter Check (`BypassSandbox: false`):
     - Command: `.venv/bin/ruff check --no-cache tests/conftest.py tests/test_causal_graphs_curation.py tests/test_uniprot_protein_examples.py`
     - Exit Code: `0` (`All checks passed!`).
