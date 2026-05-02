---
name: data-monetization-canvas
description: "Create business value cases for data, analytics, and AI opportunities through internal efficiency, customer experience, decision quality, data products, partnerships, risk reduction, revenue, leakage prevention, or retention. Use when Codex needs an evidence-linked value case, data monetization canvas, ROI framing, value hypothesis, or pilot metric design."
---

# Data Monetization Canvas

## Core Rule

Data monetization is broader than selling data. Count internal efficiency, better decisions, risk reduction, customer experience, revenue protection, leakage prevention, and reusable data products.

Inside the AI operating partner engagement, this is Step 12: the business value case and portfolio comparison. It is the economic and sequencing filter before solution shape, architecture, risk, readiness, and future implementation planning. It does not authorize build work.

AI drafts the first-pass value case from prior evidence. The operating partner judges credibility, priority, and strategic fit. The client confirms business reality: volumes, costs, acceptable assumptions, risk tolerance, and which value matters to leadership.

Useful references:

- `../../mastery-reference/information-management/operator-toolkit/data-monetization-opportunity-canvas.md`
- `../../mastery-reference/information-management/concept-library/concepts.md`
- `../../mastery-reference/information-management/operator-toolkit/data-monetization-opportunity-canvas.md`
- `../../mastery-reference/information-management/concept-library/frameworks.md`

## Value Lenses

Assess:

- Internal efficiency: labor, rework, cycle time, leakage, cost.
- Customer experience: response, accuracy, personalization, transparency.
- Decision quality: speed, confidence, evidence, consistency.
- Data product: reusable governed dataset, metric, API, report, or insight service.
- Risk reduction: compliance, operational, security, reputation, quality.
- Revenue: conversion, retention, pricing, service expansion, partnerships.
- Revenue protection and leakage prevention: missed billing, slow collections, avoidable spend, wrong classification, recoverability misses.

## How To Get Inputs

Collect:

- Executive goals, revenue priorities, cost pressures, and risk concerns.
- Manager/operator pain around repeated work, delays, rework, and service gaps.
- Current volumes, cycle times, error rates, costs, and revenue impact.
- Customer-facing feedback or service quality evidence when available.
- Data assets, reports, dashboards, and source inventories.
- Legal/privacy/security constraints on data use.

Ask for examples and baseline numbers. If baseline metrics are missing, make baseline measurement the first recommendation.

Inside the AI operating partner engagement, use prior outputs first:

- Executive opportunity terrain and strategic priorities.
- AI workflow specification and operating strain/value signals.
- Organizational intelligence diagnostic.
- Source access/governance decisions.
- Step 9 knowledge/guideline requirements.
- Step 10 guidance packs.
- Step 11 measurement intelligence, AI-capability metric design, and metric trust classifications.
- Truth production profiles and fragile-truth dependencies.
- Planning evidence such as volumes, cycle times, cost ranges, error/rework examples, leakage examples, risk incidents, service feedback, reports, and financial/operational summaries.

Do not treat disputed, untrusted, unknown, shadow-derived, manually adjusted, person-dependent, missing, or not-reproducible metrics as reliable baseline evidence unless the recommendation is explicitly to fix measurement or truth infrastructure first.

## Canvas Template

The Trust / Truth Status column uses the canonical `truth_status` enum (authoritative | conditionally_reliable | shadow_derived | manually_adjusted | person_dependent | disputed | missing | not_reproducible | unknown). The Proposed AI behavior_level column uses the canonical `behavior_level` enum (read_only_summary | draft_and_flag | recommendation_support | human_approved_action | autonomous_action). A value case proposing `recommendation_support` or higher backed only by `shadow_derived`/`manually_adjusted`/`person_dependent`/`disputed`/`missing`/`not_reproducible` baseline metrics is a measurement/truth-infrastructure-fix recommendation, not a value case.

| Lens | Questions | Notes | Metric | Truth status (canonical enum) | Proposed AI behavior_level | evidence_refs | confidence |
|---|---|---|---|---|---|---|---|
| Internal efficiency | What work, delay, or rework falls? | | | | | | |
| Customer experience | What experience improves? | | | | | | |
| Decision quality | What decision gets better evidenced? | | | | | | |
| Data product | What reusable asset can be created? | | | | | | |
| Risk reduction | What risk falls? | | | | | | |
| Revenue/leakage | What growth, retention, or leakage prevention improves? | | | | | | |

## Evaluation Workflow

1. Name the opportunity.
2. Name the user and decision.
3. Identify data rights and constraints.
4. Identify required data and knowledge.
5. Identify governance and quality prerequisites.
6. Link value levers to Step 11 baseline metrics and trust status.
7. Estimate conservative/base/upside ranges only when evidence supports them.
8. Estimate AI-side costs: model/tool calls, retrieval/storage, eval/observability, support, maintenance, human review, and vendor costs.
9. List assumptions, confidence, and client-confirmation needs.
10. Compare surviving opportunities as a portfolio and select 1-N to advance.
11. Define pilot metric and measurement window.
12. Identify risks and current verification needs.
13. Recommend: carry forward to solution shape/readiness, fix measurement first, fix truth production first, fix governance/knowledge first, deprioritize, or do not pursue.

## Output

Deliver:

- Business value case.
- Value hypotheses by lens.
- Baseline metrics and trust status.
- Evidence references.
- Conservative/base/upside estimates where supported.
- AI-side cost model.
- Portfolio comparison and sequencing recommendation.
- Assumptions and confidence.
- Dependencies across measurement, truth production, governance, source access, knowledge/guidance, architecture, risk, and change management.
- Client confirmation needs.
- Recommendation and next route.

## Quality Bar

Reject vague value claims. Every opportunity needs:

- A user.
- A decision or workflow.
- A measurable value lever.
- Required data.
- Rights/privacy constraints.
- Trusted or conditionally trusted baseline evidence, or an explicit measurement/truth-infrastructure fix recommendation.
- A pilot metric or value-capture metric.

Do not call an opportunity valuable only because it is automatable. Do not pretend ROI precision when evidence only supports a directional case.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

