---
name: analytics-maturity-assessment
description: "Assess an organization's analytics maturity across reporting, data integration, governance, semantic definitions, predictive capability, dashboards, and agent readiness. Use when Codex needs to score current state, identify gaps, recommend an upgrade path, or decide what analytics foundation is needed before AI."
---

# Analytics Maturity Assessment

## Core Rule

Assess whether decisions are supported by trusted, governed, measurable analytics before recommending predictive models or agents.

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

Gather evidence from:

- Executive goals and decision pain.
- Manager reports and dashboard needs.
- Operator/admin manual reporting work and spreadsheet workarounds.
- IT/data/system inventory.
- Current reports, dashboards, KPI lists, extracts, and data dictionaries.
- Analytics backlog, model documentation, data-quality logs, and user correction history.

Use interviews to identify trust, adoption, and actionability; use artifacts to verify whether the analytics layer actually exists.

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

## Output

Deliver:

- Current maturity level.
- Dimension-by-dimension scores.
- Evidence for each score.
- Major blockers.
- Upgrade path.
- First three improvements.
- Suitable agent scope at current maturity.

## Quality Bar

Do not over-score maturity because tools exist. Score by decision reliability, governance, data quality, and adoption.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

