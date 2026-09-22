# AI Operating Partner System

## Install the AI Operating Partner plugin

In **Add from marketplace**, paste **https://github.com/kavins06/AI-OPERATING-PARTNER-MODEL**. Select **AI Operating Partner** from **Quoin Operating Partner**, install, and start a new conversation.

Try: **Help me find the best AI opportunity in my business.**

This repository includes the complete [plugin package](plugins/ai-operating-partner-model/) with 27 skills and method assets. See the [user guide](plugins/ai-operating-partner-model/docs/plugin-guide.md) and [acceptance scenarios](plugins/ai-operating-partner-model/docs/plugin-test-cases.md). GitHub marketplace installation requires a supporting host and workspace permission.

The packaged method is independent of the older method files below. Rebuild it from the method-development checkout; do not mix these versions.

This repo is the source-of-truth package for the AI operating partner skill system.
It contains the 16 operating skills, the master engagement orchestrator, reusable templates, scoring scripts, and generated mastery references.

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

Use `ai-operating-partner-engagement` first when you want the full process. It coordinates the other skills in this order:

1. Source-grounded consulting
2. Data strategy workshop
3. AI-led interview discovery
4. Workflow mapping
5. Information ecology diagnostic
6. Validation call
7. Data governance discovery
8. Knowledge map capture
9. Tacit-to-explicit knowledge capture
10. Analytics maturity assessment
11. Dashboard and KPI design
12. Data monetization canvas
13. Warehouse/lakehouse blueprint
14. Agent data preparation and knowledge structuring
15. Privacy/security risk register
16. Zero-trust agent controls
17. AI-agent readiness assessment
18. Managed agent lifecycle

Step 14 is handled through the orchestration skill and the knowledge, governance, architecture, KPI, and readiness skills rather than as a separate standalone skill.

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
