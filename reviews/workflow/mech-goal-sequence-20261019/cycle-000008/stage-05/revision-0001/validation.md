# Stage 5 Validation Report (`mech-goal-sequence-20261019`, Cycle 8, Stage 5)

## Executed Validation Gates and Command Provenance

1. **Native Writer Remediation and Transition Manifest Generation**
   - Curated `mode_of_action` and `PRIMARY_LITERATURE` `molecular_targets` on the 4 Cycle 8 Stage 1 natural products (`#1360`) and 5 `EXACT` rifamycins and elfamycins (`#1361`), updated [`curation/uniprot_protein_examples.yaml`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/uniprot_protein_examples.yaml) (`records=102`, `held_targets=135`, `sha256=c39f5eee35d652d2a0a409632a21fe87ca4e68e7dcebc7348df0a2206bd0c016`) and [`curation/uniprot_protein_examples_transition.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/uniprot_protein_examples_transition.json) (`sha256=48b5f467ca7c684032866839bef7455e84310640b52abee9b25da865df312fcc`), promoted all 15 `EXACT` ChEBI records (`alanylclavam`, `amicetin`, `andrimid`, `bottromycin-a2`, `planosporicin`, `ajudazol-a`, `tp-1161`, `2-formyloxymethylclavam`, `2-hydroxymethylclavam`, `clavam-2-carboxylate`, `rifabutin`, `rifaximin`, `rifapentine`, `ge2270a`, `pulvomycin`) to `curation_status: REVIEWED` via `record_curation_event` and `write_validated_antibiotic`, updated [`curation/causal_graphs.yaml`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/causal_graphs.yaml) (`held_records` `count=78`, `sha256=064a5bdaac1b593d4c898ba55c016bd0dc9aa2e3a0d93ec726279bbcaf89eac4`), and recorded [`curation/cycle8_stage5_review_remediation_transition.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/cycle8_stage5_review_remediation_transition.json) (`sha256=0f1488849ca06efc4025adcec18cc514d4d6deddb980a2ebac7e43479ff8e11a`) (`BypassSandbox: true`, exit code `0`).

2. **Closed LinkML Schema and OAK Ontology Label Validation ([`scripts/validate_strict.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/validate_strict.py))**
   - Command (`BypassSandbox: true`): `.venv/bin/python scripts/validate_strict.py --out .temp/validate_strict_c8s5.tsv`
   - Exit Code: `0`
   - Literal Summary Output:
     ```text
     === validate-strict summary ===
       files scanned:      3125
       files with ERROR:   0
       total ERROR rows:   0
       TSV:                .temp/validate_strict_c8s5.tsv
     ```

3. **Full Corpus Seed Reproduction Check ([`scripts/verify_corpus.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/verify_corpus.py))**
   - Command (`BypassSandbox: false`): `.venv/bin/python scripts/verify_corpus.py`
   - Exit Code: `0`
   - Literal Output:
     ```text
       1 CARD cross-reference(s) refused as self-contradictory (see `just worklist --queue crossref-conflict`)
         ARO:3000337: CARD links ARO:3000337 (iclaprim) to CHEBI:31724 (Isoaminile citrate), but the names differ and the CAS numbers disagree (192314-93-5 vs 28416-66-2). Cross-reference not trusted for roles, structure or identity.
     records expected: 3125   on disk: 3125
     missing: 0   unexpected: 0   drifted fields: 0
     identifiers absent from PATHS.tsv: 0   stale lockfile rows: 0

     corpus reproduces exactly from data/raw/ plus curator inputs.
     ```

4. **Review-Readiness Queue Refresh ([`scripts/curation_worklist.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/curation_worklist.py))**
   - Refreshed [`curation/record_review_queue.tsv`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/record_review_queue.tsv) (`sha256=91aa57f1cd2dec3cb751555e31a077f8e783291bc293073976ff33db87093f19`): `2,951` unsigned items (`REVIEWED` count increased from `159` to `174`; `PROPOSED` count decreased from `167` to `157`; `SEEDED` count decreased from `2,799` to `2,794`).

5. **Chemical Structure Map and PaCMAP Corpus Map Refresh ([`data/embeddings/chemical-structure-map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/chemical-structure-map.json), [`data/embeddings/corpus_map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/corpus_map.json))**
   - Refreshed [`data/embeddings/chemical-structure-map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/chemical-structure-map.json) (`input_hash=09220d43649a951cea06e703e2ce0611617e85b5f14b2b9a40cc38c70fc4bc1e`) and [`data/embeddings/corpus_map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/corpus_map.json) (`corpus_fingerprint=78548d09bc150603`).
   - Embeddings, Corpus Integrity, and Docs Test Suites (`BypassSandbox: false`):
     - Command: `.venv/bin/python -m pytest -q tests/test_embeddings.py tests/test_corpus_integrity.py tests/test_docs.py`
     - Exit Code: `0` (`52 passed`).

6. **README Statistics and Static Site Pages Synchronization ([`scripts/check_docs.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/check_docs.py), [`scripts/render_pages.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/render_pages.py), [`NEXT_TASKS.md`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/NEXT_TASKS.md))**
   - Updated [`NEXT_TASKS.md`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/NEXT_TASKS.md) (`518` records with target or resistance evidence; `104` populated `PRIMARY_LITERATURE` `MolecularTarget` entries across `102` records in `curation/uniprot_protein_examples.yaml` and `135` `held_targets`; `190` reviewed Swiss-Prot `UniProtKB` `protein_examples` across the corpus).
   - Refresh Run (`BypassSandbox: true`):
     - Command: `.venv/bin/python scripts/check_docs.py --write` and `.venv/bin/python scripts/render_pages.py`
     - Exit Code: `0`
     - Literal Output:
       ```text
       README statistics refreshed.
       rendered 3125 compound pages, 7 classes, pruned 0 stale -> /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/pages
       ```

7. **Native Structured Review Bundle Save, Validate, and Append-Only Check ([`scripts/record_review.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/record_review.py))**
   - Save and Check Bundle (`BypassSandbox: true`):
     - Command: `.venv/bin/python scripts/record_review.py save --content .temp/cycle8_stage5_remediated_review_input.yaml && .venv/bin/python scripts/record_review.py check --base main`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"review": "/Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/reviews/structured/20261109T155000Z-cycle8-stage5-remediated-records-review/review.yaml", "markdown": "/Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/reviews/structured/20261109T155000Z-cycle8-stage5-remediated-records-review/review.md"}
       topClass is deprecated - use top_class
       {
         "repository": "culturebotai/AntibioticMech",
         "valid_reviews": 27,
         "coverage": "declared_scopes_only"
       }
       ```

8. **Pytest and Ruff Validation Suites**
   - UniProt Protein Examples & Causal Graphs Curation Suites (`BypassSandbox: false`):
     - Command: `.venv/bin/python -m pytest -q tests/test_causal_graphs_curation.py tests/test_uniprot_protein_examples.py`
     - Exit Code: `0` (`201 passed`).
   - Record Review Contract Suite (`BypassSandbox: true`):
     - Command: `.venv/bin/python -m pytest -q tests/test_record_review_contract.py`
     - Exit Code: `0` (`4 passed`).
   - Ruff Linter Check (`BypassSandbox: false`):
     - Command: `.venv/bin/python -m ruff check --no-cache .`
     - Exit Code: `0` (`All checks passed!`).
