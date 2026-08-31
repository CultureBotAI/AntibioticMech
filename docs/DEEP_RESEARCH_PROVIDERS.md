# Deep-research providers

This Mech supports two first-class deep-research lanes:

- `openscientist` through `deep-research-client`;
- `codex` through the native `codex exec` contract in
  `scripts/deep_research_contract.py`.

Codex is not routed through the client's `cyberian` adapter. The native
command explicitly enables web search, runs ephemerally in a read-only sandbox,
requires a JSON-schema response, validates report length and distinct HTTP(S)
sources, and publishes atomically only after validation.

## Credentials

Codex uses the local Codex CLI login. Run `codex login status`; no API key is
stored in this repository.

OpenScientist requires `OPENSCIENTIST_API_KEY=name:secret`.
`OPENSCIENTIST_URL` is optional and defaults to
`https://www.openscientist.io`. Never commit or print either value.

## Canary sequence

Run `just deep-research-canary codex` or
`just deep-research-canary openscientist` first. These checks do not submit a
research job. The Codex canary verifies CLI authentication and required
capabilities. The OpenScientist canary validates credential shape and provider
discovery.

Then dry-run one entity runner. Pass `--apply` only for a deliberately
authorized one-record canary, inspect the report and sources, and only then
consider a bounded batch. Research artifacts are curator inputs and never
update generated or curated records automatically.

## Canonical pin

`scripts/deep_research_contract.py` is vendored byte-for-byte from the
canonical `CultureBotAI/culturebotai-claw` artifact. Fleet-governed Mechs pin
it through `scripts/.vendored_canon_ref`; repositories outside that manifest
use `scripts/.deep_research_contract_ref`.
