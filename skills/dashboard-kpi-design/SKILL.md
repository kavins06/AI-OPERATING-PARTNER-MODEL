---
name: dashboard-kpi-design
description: "Design decision-ready dashboards and KPI standards with audience, business question, formulas, grain, official sources, de facto trusted sources, truth production chains, context, thresholds, filters, owners, and quality checks. Use when Codex needs dashboard specs, KPI dictionaries, metric governance, or agent-safe analytics definitions."
---

# Dashboard KPI Design

## Core Rule

Start with the audience and decision. A KPI is useful only if it supports action, comparison, accountability, or learning.

Inside the AI operating partner engagement, KPI design supports Step 11 measurement intelligence and AI-capability metric design. It defines decision-linked metrics, agent-safe usage, success metrics, override/error/drift/adoption/cost metrics, and kill criteria; it does not build dashboards or analytics pipelines.

Useful references:

- `../../mastery-reference/analytics/artifacts/dashboard_kpi_standards.md`
- `../../mastery-reference/analytics/summaries/glossary.md`
- `../../mastery-reference/analytics/artifacts/dashboard_kpi_standards.md`
- `../../mastery-reference/analytics/summaries/concept_map.md`

## Design Workflow

Each step references the canonical V3 schema. KPI definitions are downstream consumers of `truth_production_profile` and `source_access_profile`; do not invent new structures.

1. Name the audience.
2. Name the `decision_id` or `workflow_step_id` the KPI supports (from the workflow_intelligence_object).
3. Identify the workflow and outcome.
4. Select KPIs that drive action.
5. Define formulas and grain.
6. Identify or link the canonical `truth_production_profile`: `official_source`, `de_facto_trusted_source`, `production_chain_summary`, `embedded_rules_or_macros`, `manual_adjustments_or_reconciliations`, `owner_role`, `steward_or_knower_role`, `reproducibility`, `auditability`, and `truth_status`.
7. Classify metric `truth_status` per the canonical enum (authoritative | conditionally_reliable | shadow_derived | manually_adjusted | person_dependent | disputed | missing | not_reproducible | unknown).
8. Identify or link the `source_access_profile`: `practical_access_path`, `access_method`, `lookup_keys`, `required_fields_or_attributes`, `current_access_roles`, `access_failure_modes`.
9. Add context: target, prior period, benchmark, trend, threshold.
10. Define allowed filters and drilldowns.
11. Define owners and quality checks.
12. Define `ai_safe_usage` per the canonical schema: `allowed_uses`, `prohibited_uses`, `required_human_review_when`. Constrain the maximum permitted `behavior_level` per Step 16 `behavior_level_rules` - KPIs with fragile `truth_status` cannot support `recommendation_support` or higher.

## How To Get Inputs

In the AI operating partner engagement, prefill from the workflow intelligence object, source access profiles, validation events, Step 9 knowledge requirements, Step 10 guidance packs, and planning evidence before asking new questions.

Interview and collect targeted confirmation from:

- Executives: target outcomes and accountability metrics.
- Managers: operational decisions and thresholds.
- Operators: what they check daily and what signals action.
- Admin/reporting staff: current report production and metric pain.
- Data owners: formulas, source systems, quality issues.
- Report owners and operators: formulas, spreadsheet macros, manual adjustments, reconciliations, and de facto trusted artifacts.
- Current dashboards, reports, spreadsheets, and board packs.

Use adaptive AI interviews to ask "What decision does this number change?" for every proposed KPI.

Do not ask for live system access, credentials, or build access. Use approved planning evidence such as redacted dashboards, board reports, KPI lists, budget variance reports, accounting exports, property management reports, Excel trackers, and data dictionaries.

## KPI Definition Template

| Field | Definition |
|---|---|
| KPI name | |
| Business question | |
| Formula | |
| Grain | |
| Unit | |
| Official source | |
| De facto trusted source | |
| Truth production chain | |
| Truth status | |
| Manual adjustment / macro / reconciliation status | |
| Reproducibility | |
| Auditability | |
| Operational working source | |
| Source access profile | |
| Refresh cadence | |
| Freshness required | |
| Owner | |
| Steward | |
| Quality checks | |
| Allowed filters | |
| Drilldowns | |
| Thresholds | |
| Trust status | |
| Trust evidence | |
| Decision/action | |
| Agent allowed uses | |
| Agent prohibited uses | |
| Human review triggers | |
| AI success / override / error / drift / adoption / cost metrics | |
| Kill criteria | |
| Linked truth_production_profile id | |
| Linked source_access_profile id | |
| Maximum permitted behavior_level | |
| Owner confirmation status | |

## Dashboard Rules

Use:

- Clear hierarchy.
- Visible date, filters, units, and definitions.
- Comparisons over decoration.
- Drilldowns that follow how users think.
- Exception thresholds.
- Consistent metric definitions.
- Visual evidence available even when an agent summarizes it.

Avoid:

- Decorative metrics.
- Undefined KPIs.
- Too many visuals.
- Hidden filters.
- Mismatched date ranges.
- Agent explanations that cannot trace to chart or source data.

## Output

Deliver:

- Dashboard purpose.
- Audience.
- KPI dictionary.
- Layout sections.
- Filters and drilldowns.
- Data sources.
- Truth production profiles.
- Metric trust status.
- Agent-safe metric usage.
- Quality checks.
- Agent role.
- Open governance questions.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

