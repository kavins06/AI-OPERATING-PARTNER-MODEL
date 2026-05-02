---
name: workflow-mapping
description: "Convert interviews, notes, transcripts, SOPs, reports, or observed work into AI-native workflow specifications. Use when Codex needs structured organizational workflow intelligence: roles, hierarchy, actors, steps, decisions, handoffs, exceptions, information objects, source access profiles, truth production profiles, inputs, outputs, controls, evidence, confidence, unknowns, and automation candidates."
---

# Workflow Mapping

## Core Rule

Model what people actually do, not what the org chart or system diagram claims happens. Keep the AI workflow specification factual, evidence-referenced, confidence-scored, validated where possible, and separate from recommendations.

Useful references:

- `../../mastery-reference/combined-operating-model.md`
- `../../mastery-reference/combined-operating-model.md`
- `../../mastery-reference/information-management/operator-toolkit/voice-interview-discovery-playbook.md`

## Inputs

Use any available:

- Interview transcript or notes.
- Relevant org structure, roles, reporting lines, and interview coverage.
- Screen-share walkthrough notes.
- SOPs, checklists, forms, policies.
- System exports or screenshots.
- Reports, dashboards, tickets, emails, or handoff examples.
- Information object and source access profiles for workflow-relevant data points, documents, reports, dashboards, trackers, emails, system records, policies, approvals, and messages.
- Truth production evidence for workflow-relevant numbers, statuses, reports, macros, reconciliations, manual adjustments, and expert-memory rules.

If evidence conflicts, preserve the conflict instead of smoothing it away.

## How To Get Inputs

As an AI operating partner, collect inputs through a staged process:

1. Executive opportunity terrain map for strategy, leverage areas, trust boundaries, candidate discovery zones, and success definition.
2. Operating partner synthesis to map the full terrain and sequence discovery zones.
3. AI-led adaptive interviews across organizational layers.
4. Evidence need consolidation and curated planning-evidence follow-up. Request only the smallest useful set of redacted examples, screenshots, reports, trackers, templates, formulas, macro walkthroughs, reconciliation notes, walkthroughs, sample exports, schema/field lists, API/vendor documentation, access-control screenshots, or data dictionaries needed to validate the AI workflow specification.
5. Client-led read-only screen-share walkthroughs of real work when approved and scoped.
6. Systems inventory with owners, users, data held, export/API access, and known issues.
7. Controlled validation and object-driven governance resolution using role-specific validation views and targeted source/truth/owner/permission decision views to ask, "What did we misunderstand?", "What is official?", "What is actually trusted?", and "What is allowed?"

Do not rely only on executives. Leaders often describe what should happen; operators reveal what actually happens.

No direct company data access is required to start mapping. During the V2 engagement, do not request production credentials, employee credentials, broad live system access, unapproved API tokens, all-email ingestion, write access, live MCP/connector access, or bulk unredacted data. If future implementation needs those, capture them as blueprint requirements for Steps 14-18.

## AI-Native Workflow Specification

Step 6 produces an `organizational_workflow_intelligence` object, not a human-readable report. Human summaries are views generated from this object.

Build the spec by:

1. Naming the workflow and defining business purpose, trigger, outcome, validation status, and confidence.
2. Encoding lightweight org context: teams, roles, reporting structure, relevant people, and interview coverage.
3. Creating stable IDs for roles, people, actors, steps, decisions, edge cases, information objects, source access profiles, truth production profiles, sources, systems, approval gates, evidence, unknowns, and candidate assists.
4. Listing normal-path steps from trigger to outcome.
5. Adding decision points, approval gates, handoffs, inputs, outputs, information object references, and source references for every step.
6. Adding source access profiles for important workflow information objects: system/location, module/report/path, lookup keys, required fields, access roles, alternate locations, compared-against sources, and known access failure modes.
7. Adding source trust signals, official/de facto source conflicts, and truth production profiles for material numbers, statuses, reports, and decisions.
8. Adding edge cases, exceptions, rework loops, delays, and failure points.
9. Adding role variation analysis: shared patterns, observed variations, conflicts, best-practice candidates, and standardization opportunities.
10. Marking sensitive data signals and human boundaries.
11. Marking candidate assists as hypotheses only.
12. Separating facts, assumptions, inferences, unknowns, validation needs, and later-step enrichment routes.
13. Adding evidence references, validation status, and confidence to every important object.

## Stop Boundary

Step 6 should complete:

- Workflow identity, business purpose, trigger, outcome.
- Known org context, roles, people, hierarchy, and interview coverage.
- Known actors, steps, handoffs, decisions, approval gates, edge cases, information objects, source access profiles, truth production profiles, sources/systems mentioned, source trust signals, sensitive data signals, human boundaries, operating strain/value signals, candidate assist hypotheses, evidence, confidence, validation status, unknowns, and enrichment routes.

Step 6 should not complete official source authority, final truth authority, data owner/steward, full data dictionary, metric formulas, data quality rules, retention rules, access matrix, agent permissions, risk scores, zero-trust controls, architecture design, readiness score, or build recommendation. Route source/truth/owner/sensitivity/access/permission fields to Step 8 controlled validation and governance resolution, and route risk, metric, architecture, adoption, and readiness fields to later enrichment steps.

## Automation Readiness Signals

Good signs:

- Stable trigger and outcome.
- Named owner.
- Repeatable steps.
- Trusted sources.
- Documented rules or examples.
- Clear escalation path.
- Measurable baseline.

Bad signs:

- Disputed process.
- Unclear official/de facto source or truth production chain.
- Shadow-derived, manually adjusted, person-dependent, disputed, missing, or not-reproducible truth production.
- Undocumented judgment.
- Sensitive outputs without approval.
- No owner.
- No measurable result.

## Output Standard

Deliver:

- An AI-native workflow specification.
- Stable IDs and relationships across workflow, roles, people, actors, steps, decisions, information objects, source access profiles, truth production profiles, sources, edge cases, approvals, evidence, unknowns, and candidate assists.
- Evidence, validation status, and confidence for every important object.
- Known role variations and coverage gaps.
- Known disagreements or uncertainty.
- A list of questions for validation.
- A next-step routing list: controlled validation/governance resolution, knowledge mapping, analytics/KPI design, architecture, risk register, zero-trust controls, or readiness scoring.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

