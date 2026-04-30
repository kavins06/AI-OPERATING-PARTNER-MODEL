---
name: ai-operating-partner-engagement
description: "Orchestrate a complete AI operating partner engagement from executive intake through AI-led interviews, workflow mapping, data/knowledge/governance/risk discovery, readiness scoring, and managed-agent operating design. Use when Codex needs to run the full pre-build client process or coordinate the 16 supporting mastery skills."
---

# AI Operating Partner Engagement

## Core Rule

Run the engagement as a structured, evidence-based pipeline. Use AI for heavy interviewing, extraction, synthesis, drafting, and scoring. Use the human operating partner for scope, judgment, prioritization, client trust, and final recommendations. Use the client for truth, examples, approvals, and ownership decisions.

This skill orchestrates the 16 supporting skills:

1. `source-grounded-consulting`
2. `data-strategy-workshop`
3. `voice-interview-discovery`
4. `workflow-mapping`
5. `information-ecology-diagnostic`
6. validation call
7. `data-governance-discovery`
8. `knowledge-map-capture`
9. `tacit-to-explicit-knowledge-capture`
10. `analytics-maturity-assessment`
11. `dashboard-kpi-design`
12. `data-monetization-canvas`
13. `warehouse-lakehouse-blueprint`
14. `privacy-security-risk-register`
15. `zero-trust-agent-controls`
16. `ai-agent-readiness-assessment`
17. `managed-agent-lifecycle`

## Practical Engagement Flow

1. Start with executive intake and business goals.
2. Use AI-led adaptive interviews across organizational layers.
3. Collect documents and examples, not a giant undifferentiated data dump.
4. Map workflows from trigger to outcome.
5. Diagnose people, process, data, knowledge, governance, analytics, and risk gaps.
6. Validate the map and findings with the client.
7. Define data governance and knowledge capture requirements.
8. Assess analytics maturity and KPI needs.
9. Build value case and data monetization canvas.
10. Design architecture only as deeply as needed.
11. Create risk register and zero-trust control model.
12. Score AI-agent readiness.
13. Produce a build-ready agent brief or a gap-remediation plan.
14. If ready, define managed lifecycle for build, validation, deployment, monitoring, and improvement.

## Resource Map

Read these when needed:

- `references/engagement-sequence.md`: full order, roles, and decision gates.
- `references/role-interview-prompts.md`: adaptive AI interviewer prompts by org layer.
- `references/input-collection-checklist.md`: what to collect and how to ask for it.
- `references/output-standards.md`: deliverable standards and build-ready packet definition.

Use these templates:

- `assets/templates/01-executive-intake.md`
- `assets/templates/02-role-interview-guide.md`
- `assets/templates/03-workflow-map.md`
- `assets/templates/04-source-inventory.csv`
- `assets/templates/05-knowledge-map.md`
- `assets/templates/06-kpi-dictionary.csv`
- `assets/templates/07-risk-register.csv`
- `assets/templates/08-readiness-scorecard.csv`
- `assets/templates/09-build-ready-agent-brief.md`
- `assets/templates/10-managed-agent-lifecycle-sop.md`
- `assets/templates/11-ai-interviewer-system-prompt.md`
- `assets/templates/12-validation-call.md`

Use scripts:

- `scripts/score_readiness.py`
- `scripts/score_analytics_maturity.py`
- `scripts/score_risk.py`
- `scripts/transcript_extract.py`

## Output Modes

If the user asks to start an engagement, produce:

- Intake request.
- Interview plan.
- Document request list.
- Timeline.
- Roles and responsibilities.

If the user gives transcripts or notes, produce:

- Extracted work episodes.
- Workflow map.
- Source and system map.
- Pain points.
- Knowledge gaps.
- Risk signals.
- Follow-up questions.

If the user asks whether to build, produce:

- Readiness score.
- Build/fix/do-not-automate decision.
- Required fixes.
- First safe agent behavior.
- Build-ready agent brief or remediation plan.

## Quality Bar

Do not recommend building an agent until the workflow is validated, sources and owners are known, knowledge gaps are named, sensitive data and approval gates are controlled, value is measurable, and readiness is scored with evidence.


