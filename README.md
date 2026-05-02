# AI Operating Partner System

This repo is the method backbone for an AI operating partner workbench. It defines the principles, engagement sequence, canonical objects, templates, rubrics, schemas, scoring helpers, and handoff contracts for enterprise modernization work.

It is not the enterprise modernization webapp. The future app should live elsewhere and operationalize this method through guided workflows, structured object editing, evidence management, validation, scoring, review, packet generation, lifecycle planning, and build-phase handoff.

## What This Repo Is For

- Maintaining the operating method.
- Maintaining Codex-ready skills that execute the method.
- Defining machine-readable artifact contracts for a future app.
- Preserving the pre-build boundary before any implementation work starts.
- Supporting vertical extensions, with real estate as the first worked example.
- Generating operator, sponsor, and visual guides as derived artifacts.

## What This Repo Is Not For

- App UI code.
- Production agents.
- MCP servers, connectors, or live integrations.
- Credential collection or broad production data access.
- Normalization pipelines or production automations.
- Build-phase implementation work before Step 18 approval.

## Read First

- [docs/README.md](docs/README.md): method-workbench documentation map.
- [docs/principles.md](docs/principles.md): non-negotiables and modernization thesis.
- [docs/method-backbone.md](docs/method-backbone.md): system shape and artifact flow.
- [docs/engagement-steps.md](docs/engagement-steps.md): canonical Step 0-18 process.
- [docs/canonical-objects.md](docs/canonical-objects.md): object model for future product design.
- [docs/quality-gates.md](docs/quality-gates.md): readiness, risk, validation, and handoff gates.
- [docs/app-boundary.md](docs/app-boundary.md): what the future app may build and must preserve.
- [docs/vertical-extension-guide.md](docs/vertical-extension-guide.md): how to extend the method by domain.

## Repo Structure

- `docs/`: method backbone, product boundary, quality gates, and install notes.
- `skills/`: Codex-ready skill package.
- `skills/ai-operating-partner-engagement/`: master orchestration skill with templates, schemas, references, examples, and scoring helpers.
- `mastery-reference/`: generated mastery/reference material copied from the broader mastery folder.
- `scripts/`: install, validation, guide-generation, and maintenance helpers.
- `output/`: generated guide PDFs, markdown, and preview images.

## Method Summary

The engagement is a pre-build organizational intelligence, use-case selection, adoption, and implementation-blueprint process. It has Step 0 plus 18 operating steps.

The method discovers how business truth is actually produced: official systems, de facto trusted sources, exports, formulas, spreadsheets/macros, manual adjustments, reconciliations, expert judgment, ownership, reproducibility, auditability, and AI-safe usage. Fragile truth becomes a readiness blocker unless the proposed AI behavior is limited to safe actions such as summarize, compare, flag uncertainty, draft clarification questions, or escalate.

Implementation starts only after Step 18 is complete, the decision packet and lifecycle object are approved, the method-to-build handoff is accepted, and the client starts a separate build phase.

## Skill Set

The bundle contains 16 supporting skills plus 1 orchestrator.

Supporting skills:

1. `information-ecology-diagnostic`
2. `source-grounded-consulting`
3. `voice-interview-discovery`
4. `workflow-mapping`
5. `ai-agent-readiness-assessment`
6. `data-strategy-workshop`
7. `data-governance-discovery`
8. `knowledge-map-capture`
9. `tacit-to-explicit-knowledge-capture`
10. `privacy-security-risk-register`
11. `zero-trust-agent-controls`
12. `data-monetization-canvas`
13. `analytics-maturity-assessment`
14. `warehouse-lakehouse-blueprint`
15. `dashboard-kpi-design`
16. `managed-agent-lifecycle`

Orchestrator:

17. `ai-operating-partner-engagement`

## Reference Platform

Codex is the reference runtime for this skill set. The methodology is platform-agnostic: schemas, contracts, rubrics, and protocols can run on any harness. Operators using a different harness should preserve the schemas, rubrics, and step-numbered artifacts and substitute equivalent mechanics for skill loading and orchestration.

The original installed Codex copies live at `C:\Users\kavin\.codex\skills`. This repo is the clean place to maintain, version, and move the system.

## Source Corpus

The 79 original source documents, raw OCR cache, extracted source-text dumps, and chunk files are not included here by default. They remain outside this repo so the repository stays focused on the operating system and skills. The corpus is available on request from the maintainer for IP-defensibility purposes.

## Install Into Codex

From this repo:

```powershell
.\scripts\install-codex-skills.ps1
```

To overwrite existing installed copies:

```powershell
.\scripts\install-codex-skills.ps1 -Force
```

## Validate

```powershell
.\scripts\validate-codex-skills.ps1
python .\scripts\validate-method-contracts.py
```

## Maintenance Rule

Edit the method and skills in this repo first. Then run the install script to copy updated skills into Codex. Treat installed Codex copies and generated guide output as derived artifacts unless you explicitly decide to publish a snapshot.
