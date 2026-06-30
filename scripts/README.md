# Scripts

This folder contains helper scripts for maintaining the method package.

## Core Scripts

- `install-codex-skills.ps1`: copies the repo-maintained skills into the active Codex skills folder.
- `validate-codex-skills.ps1`: checks that each skill folder has the expected Codex skill structure.
- `validate-method-contracts.py`: validates current method contract consistency.
- `validate-section2-backbone.py`: validates the Section 2 automation spec, active support skills, shared assets, templates, and target-state coverage when run with `--strict`.
- `generate-section2-backbone.py`: dry-run generator for Section 2 support-skill and asset scaffolding from `02-implementation-managed-agentops/section2-build-spec.yaml`; use `--apply` to write files.

## Skill Helper Scripts

Skill-specific scoring and extraction helpers live under `skills/ai-operating-partner-engagement/scripts/`.

## Guide Generators

The `generate_*.py` scripts produce human-readable guide artifacts under `output/`. Treat generated PDFs, previews, and markdown output as derived artifacts unless you explicitly decide to publish a snapshot.
