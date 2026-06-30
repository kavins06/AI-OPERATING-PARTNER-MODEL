---
name: data-strategy-workshop
description: "Plan, run, and synthesize Step 1-2 strategy workshops that translate business goals into executive opportunity terrain, data needs, governance choices, analytics opportunities, AI-agent candidates, candidate-use-case shortlists, and measurable modernization priorities."
---

# Data Strategy Workshop

## Core Rule

Start with business outcomes and decisions, not tools, models, dashboards, or agents.

Inside the AI operating partner engagement, this skill produces inputs for Step 1 (executive opportunity terrain) and Step 2 (candidate use-case shortlist). The workshop's outputs must conform to the canonical current artifacts: opportunity terrain capture and a `candidate_use_case_shortlist` whose `candidates[]` items conform to the canonical `candidate_use_case` schema. Do not produce generic strategy outputs that cannot route to a Step 2 candidate.

## Engagement Role

Use this skill after Step 0 engagement tiering and vertical-extension applicability are known, or explicitly mark Step 0 as unresolved and route it back to the orchestrator. Step 1 captures strategy, leverage areas, risk tolerance, trust boundaries, and who can explain the real work. Step 2 converts that terrain into discovery zones and candidate use cases with value, truth, adoption, regulatory, and disqualification dependencies.

Canonical templates:

- `../ai-operating-partner-engagement/assets/templates/01-executive-opportunity-terrain.md`
- `../ai-operating-partner-engagement/assets/templates/01-org-structure-capture.csv`
- `../ai-operating-partner-engagement/assets/templates/02-opportunity-terrain-synthesis.md`
- `../ai-operating-partner-engagement/assets/templates/02-candidate-use-case-shortlist.yaml`
- `../ai-operating-partner-engagement/assets/templates/02-interview-coverage-matrix.csv`

The output is a discovery plan and candidate shortlist, not a build roadmap. Implementation decisions wait for Steps 16-18.

Useful references:

- `../../mastery-reference/information-management/operator-toolkit/client-data-strategy-workshop-sop.md`
- `../../mastery-reference/information-management/concept-library/frameworks.md`
- `../../mastery-reference/analytics/summaries/cross_source_synthesis.md`
- `../../mastery-reference/analytics/artifacts/client_analytics_maturity_model.md`

## Workshop Inputs

Collect:

- Business goals and pain points.
- Current workflows and decisions.
- Existing systems and data sources.
- Reports, dashboards, spreadsheets, and exports.
- Governance issues.
- Privacy/security constraints.
- Current analytics and automation ideas.
- Measures of success.

## How To Get Inputs

Use this sequence:

1. Executive intake for goals, economics, risk tolerance, and success definition.
2. Manager/operator AI interviews for real workflows, bottlenecks, handoffs, and exceptions.
3. Admin/support interviews for data entry, reporting, cleanup, and coordination.
4. IT/data/security interview for systems, access, integration, privacy, and constraints.
5. Document request for reports, dashboards, SOPs, spreadsheets, templates, policies, sample tasks, and redacted exports.
6. Validation call to confirm the workshop framing before roadmap decisions.

Do not ask for everything. Ask for examples that explain decisions, repeated work, data trust, and measurable pain.

## Workshop Flow

1. Establish business outcomes.
2. Identify decisions and workflows that depend on information.
3. Map source systems, documents, spreadsheets, and informal knowledge.
4. Assess the Five Vs: volume, velocity, variety, veracity, value.
5. Identify current reports, dashboards, and KPI definitions.
6. Identify governance needs: owners, definitions, quality, access, retention, escalation.
7. Identify analytics and AI opportunities.
8. Rank opportunities by value, readiness, risk, and effort.
9. Choose one pilot and one enabling data-management fix.
10. Define success metrics and owners.

## Questions To Ask

- What business outcome matters most this quarter?
- What decisions are slow, risky, inconsistent, or poorly evidenced?
- What data is needed for those decisions?
- Which source is authoritative?
- Which definitions are disputed?
- Where do people use spreadsheets or inboxes instead of systems?
- What sensitive data is involved?
- What would a wrong answer cost?
- What metric proves improvement?

## Outputs

Produce, in canonical current artifact form where applicable:

- Executive opportunity terrain capture (Step 1 artifact).
- Candidate use-case shortlist conforming to `candidate_use_case_shortlist` and `candidate_use_case` schemas, with each candidate carrying `one_line_hypothesis`, `target_user_groups`, `workflow_boundary`, `value_hypothesis`, `trust_dependencies` (truth_production / source_access / data_quality / regulated_domain), `adoption_dependencies`, `disqualification_criteria`, `current_status`, and `evidence_refs`.
- Source inventory draft (links to Step 7/8 canonical templates).
- Governance decision list (routes into Step 8 controlled validation).
- Analytics/dashboard needs (routes into Step 11 measurement intelligence).
- Pilot recommendation with proposed minimum-safe `behavior_level` per candidate.
- Success metrics with linked AI-capability metrics: success, override_rate, error_rate, drift signals, adoption metrics, cost metrics, and kill criteria.

## Quality Bar

Every proposed initiative must link:

Business outcome -> decision/workflow -> data/knowledge needed -> governance/risk controls -> measurement.

Each candidate must produce a record that conforms to the canonical `candidate_use_case` schema; initiatives that cannot fill `value_hypothesis`, `trust_dependencies`, `adoption_dependencies`, `disqualification_criteria`, `current_status`, and `evidence_refs` are not yet candidates and should be returned to discovery.

Reject tool-first ideas until they can pass that chain.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.
