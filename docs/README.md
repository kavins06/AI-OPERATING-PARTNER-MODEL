# Method Workbench Docs

This folder describes the AI operating partner system as a method backbone for enterprise modernization. The future webapp should operationalize this backbone; it should not become the place where the method is invented.

## Read First

1. `principles.md`: the operating philosophy and non-negotiables.
2. `method-backbone.md`: the overall system shape and artifact flow.
3. `engagement-steps.md`: the canonical Step 0-18 process.
4. `canonical-objects.md`: the structured objects that should become the app's domain model.
5. `section1-to-section2-data-map.md`: how Step 0-18 data maps into post-18 implementation contracts.
6. `../02-implementation-managed-agentops/intelligence-platform.md`: how the operating intelligence platform makes the company queryable before deploying agents.
7. `operating-intelligence-platform-ontology.md`: ontology for the platform object graph, relationships, permissions, provenance, REIT starter model, and agent usage.
8. `reit-cto-cio-operating-intelligence-platform-brief.md`: CTO/CIO-facing explanation of the full process for a large REIT.
9. `quality-gates.md`: evidence, readiness, validation, risk, and handoff gates.
10. `app-boundary.md`: what the future product may implement and what it must preserve.
11. `vertical-extension-guide.md`: how the method extends beyond the first real-estate implementation.
12. `codex-install.md`: how to install the maintained skill package into Codex.

## Repo Roles

- `docs/` explains the method and product backbone.
- `skills/` contains Codex-ready operating skills and templates.
- `02-implementation-managed-agentops/section2-build-spec.yaml` defines the automation contract for generating and validating the post-18 backbone.
- `mastery-reference/` contains supporting generated mastery material.
- `scripts/` contains install, validation, scoring, and guide-generation helpers.
- `output/` is generated guide output and preview material.

## Core Boundary

This repository is not the enterprise modernization webapp. It is the method source of truth: principles, process, schemas, templates, rubrics, and handoff contracts. App code should live in a separate product repository and consume these contracts intentionally.
