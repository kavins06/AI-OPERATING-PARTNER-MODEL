# AI Operating Partner System

This repo is the canonical package for the AI operating partner skill system.
It contains the operating skills, the master V2 engagement orchestrator, reusable templates, scoring scripts, and generated mastery references.

The original installed Codex copies can stay in `C:\Users\kavin\.codex\skills` for day-to-day use, but this repo should be the clean place to maintain, version, and move the system.

## Contents

- `skills/` - all Codex-ready skill folders.
- `skills/ai-operating-partner-engagement/` - the master orchestration skill with templates, prompts, examples, scoring scripts, and engagement references.
- `mastery-reference/` - generated mastery artifacts and reference material copied from the combined mastery folder.
- `docs/` - practical operating notes for sequence, installation, and maintenance.
- `scripts/` - helper scripts for installing and validating the skills.

The 79 original source documents, raw OCR cache, extracted source-text dumps, and chunk files are not included here by default. They remain outside this repo so the repository stays focused on the operating system and skills.

## Skill Set

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
17. `ai-operating-partner-engagement`

## Practical Order

Use `ai-operating-partner-engagement` first when you want the full process. V2 is a pre-build organizational intelligence, use-case selection, adoption, and implementation-blueprint process with Step 0 plus 18 operating steps. It does not build agents, MCPs, connectors, live integrations, normalization pipelines, email ingestion, or production automations during the engagement. It also does not assume a clean source of truth exists; it captures how business truth is actually produced through official systems, de facto trusted artifacts, spreadsheets/macros, manual adjustments, reconciliations, and expert judgment.

0. Engagement tiering and vertical extension
1. Executive opportunity terrain mapping
2. Opportunity terrain synthesis and candidate use-case shortlist
3. Role-aware AI-led interviews
4. Variation mapping for fragmented operating models
5. Planning-evidence follow-up
6. AI-native workflow intelligence object
7. Organizational intelligence diagnostic
8. Controlled validation, governance/source access/truth production resolution, and Organizational Intelligence Baseline v1
9. AI knowledge and guideline requirements map
10. AI guidance pack: structured spec, skill-style view, and test/eval cases
11. Measurement intelligence and AI-capability metric design
12. Business value case and portfolio comparison
13. Solution shape and end-user adoption design
14. Technical/vendor implementation blueprint
15. Risk and control model
16. AI-agent readiness score
17. Machine-readable implementation decision packet
18. Machine-readable managed lifecycle and adoption-change object

Implementation starts only after Step 18 is complete, the decision packet and lifecycle object are approved, and the client starts a separate build phase.

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
```

## Maintenance Rule

Edit skills in this repo first. Then run the install script to copy the updated skills into Codex.
