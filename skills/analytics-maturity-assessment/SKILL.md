---
name: analytics-maturity-assessment
description: "Assess an organization's analytics maturity and measurement intelligence across reporting, data integration, metric trust, governance, semantic definitions, predictive capability, dashboards, and agent readiness. Use when Codex needs to score current state, classify trusted measurements, identify gaps, recommend an upgrade path, or decide what analytics foundation is needed before AI."
---

# Analytics Maturity Assessment

## Core Rule

Assess whether decisions are supported by trusted, governed, measurable analytics before recommending predictive models or agents.

Inside the AI operating partner engagement, this is part of Step 10: measurement intelligence and analytics readiness. AI does the heavy first pass, the operating partner decides which measurements matter, and the client confirms source authority and ownership. Do not build dashboards, models, pipelines, semantic layers, MCPs, connectors, live integrations, or production automations in this step.

Useful references:

- `../../mastery-reference/analytics/artifacts/client_analytics_maturity_model.md`
- `../../mastery-reference/analytics/summaries/concept_map.md`
- `../../mastery-reference/analytics/summaries/glossary.md`
- `../../mastery-reference/analytics/artifacts/dashboard_kpi_standards.md`

## Maturity Levels

Use this scale:

| Level | State | Symptoms | Suitable Scope |
|---|---|---|---|
| 0 | Spreadsheet chaos | Manual exports, conflicting numbers, no owners | Narrow read-only help only |
| 1 | Basic reporting | Static reports, manual refresh, limited trust | Reporting explainer |
| 2 | Warehouse foundation | Integrated marts, stable KPIs | KPI Q&A, dashboard support |
| 3 | Governed analytics | Owners, stewards, quality rules, access controls | Workflow-support agents |
| 4 | Predictive operations | Scores, forecasts, anomaly detection | Prioritization and recommendations |
| 5 | Agentic operations | Tool-using agents, approvals, monitoring | Managed agent operating layer |

## Assessment Dimensions

Score 0-5:

- Business question clarity.
- Source integration.
- Data quality.
- Metric definitions.
- Dashboard usefulness.
- Governance and stewardship.
- Security/access control.
- Statistical/modeling discipline.
- Feedback and monitoring.
- Change adoption.

## How To Get Inputs

In the AI operating partner engagement, use prior outputs first:

- Executive opportunity terrain and business outcomes.
- AI workflow specification.
- Organizational intelligence diagnostic.
- Controlled validation and governance events.
- Information objects and source access profiles.
- Step 8 knowledge/guideline requirements.
- Step 9 guidance packs.
- Planning evidence such as dashboards, board reports, KPI lists, Excel trackers, budget variance reports, accounting exports, property management reports, invoice aging reports, and data dictionaries.

Outside the operating partner engagement, gather evidence from:

- Executive goals and decision pain.
- Manager reports and dashboard needs.
- Operator/admin manual reporting work and spreadsheet workarounds.
- IT/data/system inventory.
- Current reports, dashboards, KPI lists, extracts, and data dictionaries.
- Analytics backlog, model documentation, data-quality logs, and user correction history.

Use interviews to identify trust, adoption, and actionability; use artifacts to verify whether the analytics layer actually exists.

## Measurement Trust Classification

AI may propose trust status, but the authorized client owner must confirm or correct it.

Classify each important metric:

- `trusted`: authoritative source, clear formula, known grain, named owner/steward, sufficient freshness, quality checks, and real decision use.
- `conditionally_trusted`: usable with caveats such as timing lag, manual refresh, source hierarchy rule, or human review.
- `disputed`: sources, formulas, ownership, or decision usage conflict.
- `untrusted`: no reliable owner, unclear formula, poor quality, stale data, or known misuse.
- `unknown`: not enough evidence yet.

Trust criteria:

- Source of record.
- Formula.
- Grain.
- Owner and steward.
- Freshness relative to the decision.
- Reconciliation status.
- Quality checks.
- Access boundary.
- Actual decision use.
- Allowed AI usage.

## Questions

Ask:

- Which decisions depend on analytics?
- Which reports are trusted?
- Which numbers conflict?
- Who owns metric definitions?
- How fresh does each use case need to be?
- What quality checks exist?
- What dashboards drive action?
- Are models evaluated and monitored?
- What would a wrong recommendation cost?
- Which source is authoritative for this metric?
- Is this metric current enough for the decision?
- Can future AI calculate, cite, compare, summarize, flag, or only escalate this metric?

## Output

Deliver:

- Measurement intelligence object.
- Decision-to-metric map.
- Metric trust classifications with evidence.
- Agent-safe metric usage and prohibited metric usage.
- Current maturity level.
- Dimension-by-dimension scores.
- Evidence for each score.
- Major blockers.
- Upgrade path.
- First three improvements.
- Suitable agent scope at current maturity.
- Unresolved metric questions routed to governance, architecture/normalization, readiness, or do-not-use-yet.

## Quality Bar

Do not over-score maturity because tools exist. Score by decision reliability, governance, data quality, and adoption.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

