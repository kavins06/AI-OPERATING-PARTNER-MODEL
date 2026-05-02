---
name: analytics-maturity-assessment
description: "Assess an organization's analytics maturity and measurement intelligence across reporting, data integration, metric trust, governance, semantic definitions, predictive capability, dashboards, and agent readiness. Use when Codex needs to score current state, classify trusted measurements, identify gaps, recommend an upgrade path, or decide what analytics foundation is needed before AI."
---

# Analytics Maturity Assessment

## Core Rule

Assess whether decisions are supported by trusted, governed, measurable analytics before recommending predictive models or agents.

Inside the AI operating partner engagement, this is part of Step 11: measurement intelligence and AI-capability metric design. AI does the heavy first pass, the operating partner decides which measurements matter, and the client confirms official source, de facto trusted source, truth production, and ownership. Do not build dashboards, models, pipelines, semantic layers, MCPs, connectors, live integrations, or production automations in this step.

Useful references:

- `../../mastery-reference/analytics/artifacts/client_analytics_maturity_model.md`
- `../../mastery-reference/analytics/summaries/concept_map.md`
- `../../mastery-reference/analytics/summaries/glossary.md`
- `../../mastery-reference/analytics/artifacts/dashboard_kpi_standards.md`

## Maturity Levels

Use this scale (1-5, aligned with the V3 readiness rubric `scoring_scale`):

| Level | State | Symptoms (in canonical-schema terms) | Suitable behavior_level |
|---|---|---|---|
| 1 | Spreadsheet chaos | Most material `truth_production_profile`s have `truth_status` of shadow_derived, manually_adjusted, person_dependent, or not_reproducible. Owners often unknown. | `read_only_summary` only, with explicit uncertainty language |
| 2 | Basic reporting | Some authoritative system reports exist; many KPIs still pass through Excel macros and manual adjustment. `de_facto_trusted_source` typically diverges from `official_source`. | `read_only_summary`; selective `draft_and_flag` |
| 3 | Governed analytics | Material `truth_production_profile`s are conditionally_reliable or authoritative, with `owner_role` named, `reproducibility` medium-or-better, and `auditability` medium-or-better. | `draft_and_flag`; selective `recommendation_support` for behaviors with adequate guidance/eval coverage |
| 4 | Predictive operations | Model outputs are governed, monitored, and tied to AI-capability metrics. Truth production is mostly authoritative. | `recommendation_support`; selective `human_approved_action` |
| 5 | Agentic operations | Tool-using agents with approval gates, audit logging, kill criteria, and monitored override/error/drift signals. | `human_approved_action`; selective `autonomous_action` for low-regulated-domain-risk behaviors |

## Assessment Dimensions

Score 1-5. Each dimension is grounded in canonical-schema fields rather than generic rubric language.

- Business question clarity: each candidate AI behavior maps to a `decision_id` or `workflow_step_id` in the workflow_intelligence_object.
- Source integration: material `information_object`s have at least one `source_access_profile` with a known `practical_access_path` and `access_method`.
- Data quality: information objects have `known_quality_or_access_issues` triaged with controls or routes.
- Metric definitions: KPIs in scope have grain, formula, owner, and a linked `truth_production_profile`.
- Dashboard usefulness: dashboards drive named decisions and AI behavior on dashboards is constrained by `ai_safe_usage`.
- Governance and stewardship: every material truth_production_profile has `owner_role` and `steward_or_knower_role` confirmed.
- Truth production readiness: distribution of `truth_status` values across material profiles - higher percentage of `authoritative` and `conditionally_reliable` raises the score; presence of `shadow_derived`, `manually_adjusted`, `person_dependent`, `not_reproducible`, or `disputed` reduces it.
- Security/access control: `current_access_roles` and `access_failure_modes` are documented; tool permissions and output controls are designed.
- Statistical/modeling discipline: when models are in scope, evaluation methodology and regression-suite versioning exist (per the Step 10 `09-ai-guidance-test-cases.yaml` coverage_requirements).
- Feedback and monitoring: AI-capability metrics (success, override_rate, error_rate, drift signals, cost, adoption, kill criteria) are defined and monitored.
- Change adoption: adoption-failure triggers are defined and monitored per Step 13 adoption_design.
- AI-capability metric design: success, override, error, drift, adoption, cost, and kill criteria are defined per the canonical `measurement_intelligence` schema.

## How To Get Inputs

In the AI operating partner engagement, use prior outputs first:

- Executive opportunity terrain and business outcomes.
- AI workflow specification.
- Organizational intelligence diagnostic.
- Controlled validation and governance events.
- Information objects and source access profiles.
- Step 9 knowledge/guideline requirements.
- Step 10 guidance packs.
- Planning evidence such as dashboards, board reports, KPI lists, Excel trackers, budget variance reports, accounting exports, property management reports, invoice aging reports, and data dictionaries.
- Truth production profiles, macro/formula walkthroughs, reconciliation notes, and manual adjustment evidence when available.

Outside the operating partner engagement, gather evidence from:

- Executive goals and decision pain.
- Manager reports and dashboard needs.
- Operator/admin manual reporting work and spreadsheet workarounds.
- IT/data/system inventory.
- Current reports, dashboards, KPI lists, extracts, and data dictionaries.
- Analytics backlog, model documentation, data-quality logs, and user correction history.

Use interviews to identify trust, adoption, and actionability; use artifacts to verify whether the analytics layer actually exists.

## Measurement Trust Classification

AI may propose trust status, but the authorized client owner must confirm or correct it. Use the canonical-schema `truth_status` enum rather than ad-hoc labels.

Map metric trust to `truth_status`:

- `authoritative`: official source confirmed, clear formula, known grain, named owner/steward, sufficient freshness, reproducible chain, adequate auditability, quality checks, and real decision use.
- `conditionally_reliable`: usable with caveats such as timing lag, manual refresh, source-hierarchy rule, documented manual adjustment, or human review. Suitable for `recommendation_support` only when the caveats are encoded in guidance.
- `shadow_derived`: a system export passes through a spreadsheet, macro, or shadow tracker before becoming the trusted number.
- `manually_adjusted`: the final number is produced by manual adjustment of a system value.
- `person_dependent`: the rules or judgments live in one person's head.
- `disputed`: sources, formulas, ownership, or decision usage conflict.
- `missing`: required truth chain or owner cannot be located.
- `not_reproducible`: the chain is too complex or undocumented to reproduce.
- `unknown`: not enough evidence yet.

Per the Step 16 `behavior_level_rules`, `recommendation_support`, `human_approved_action`, and `autonomous_action` cannot pass with fragile truth (shadow_derived, manually_adjusted, person_dependent, disputed, missing, not_reproducible). `read_only_summary` and `draft_and_flag` may pass with fragile truth provided the AI surfaces uncertainty and avoids final recommendations.

Trust criteria:

- Official source and de facto trusted source.
- Truth production chain and truth status.
- Formula.
- Grain.
- Owner and steward.
- Freshness relative to the decision.
- Reconciliation status.
- Manual adjustment status, reproducibility, auditability, and version/change-control status.
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
- Which source is official, and which source or artifact is actually trusted?
- What exports, formulas, macros, manual adjustments, reconciliations, or expert-memory rules produce the final metric?
- Is this metric current enough for the decision?
- Can future AI calculate, cite, compare, summarize, flag, or only escalate this metric?

## Output

Deliver:

- Measurement intelligence object.
- Decision-to-metric map.
- Metric trust classifications with evidence.
- Truth production status for each material metric.
- Agent-safe metric usage and prohibited metric usage.
- Current maturity level.
- Dimension-by-dimension scores.
- Evidence for each score.
- Major blockers.
- Upgrade path.
- First three improvements.
- Suitable agent scope at current maturity.
- Unresolved metric questions routed to governance, architecture/normalization, readiness, or do-not-use-yet.
- Fragile truth questions routed to knowledge capture, architecture/normalization, readiness, or do-not-use-yet.

## Quality Bar

Do not over-score maturity because tools exist. Score by decision reliability, governance, data quality, and adoption.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

