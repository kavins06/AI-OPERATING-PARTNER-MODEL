---
name: source-grounded-consulting
description: "Create traceable, evidence-based consulting recommendations by separating facts, assumptions, inferences, and recommendations. In the AI operating partner engagement, use as the cross-step evidence discipline for Steps 0-18, sponsor-facing views, packet/lifecycle recommendations, and current law, regulation, standards, vendor, or market claims."
---

# Source Grounded Consulting

## Core Rule

Every recommendation needs a business reason, evidence, stated assumptions, risk limits, and a clear next action. Do not present unstable legal, privacy, security, vendor, or market claims as current fact without verification.

## Engagement Role

This is a cross-step  quality skill, not a standalone numbered deliverable. Use it whenever Steps 0-18 produce client-facing advice, owner decisions, risk statements, implementation packet views, lifecycle views, or claims that could affect legal, regulatory, security, vendor, financial, or market decisions.

Inside the AI operating partner engagement, source-grounding must preserve the pre-build boundary. It can recommend a Step 17 packet path, a Step 18 lifecycle condition, a remediation route, a verification need, or a future implementation request. It must not start build work, request live credentials, grant access, build connectors, create MCP servers, run production automations, or imply that Step 17/18 approval has occurred.

Canonical  outputs are embedded inside the artifact being produced: `evidence_refs`, confidence, facts, assumptions, inferences, verification_needed, owner, decision_needed, recommendation, and stop conditions.

Useful references:

- `../../mastery-reference/information-management/operator-toolkit/source-grounded-consulting-checklist.md`
- `../../mastery-reference/reference-map/source-and-artifact-map.md`
- `../../mastery-reference/reference-map/source-and-artifact-map.md`
- `../../mastery-reference/analytics/reports/source_inventory.md`

## Evidence Ladder

Prefer evidence in this order:

1. Current official sources for current law, regulation, standards, vendor terms, pricing, or market facts.
2. User-provided source documents and internal evidence.
3. Mastery source notes and extracted corpus references.
4. Generated artifacts from the mastery folder.
5. Clearly labeled inference or assumption.

Use web verification when the claim could have changed recently or affects legal, financial, security, medical, compliance, or substantial business decisions.

## Operating Partner Input Path

Before advising, identify how the input was obtained:

- Intake form: goals, pain, systems, sensitive areas, success definition.
- Documents/examples: reports, dashboards, SOPs, policies, spreadsheets, tickets, messages.
- AI-led interviews: adaptive interviews across organizational layers.
- System inventory: tools, owners, users, data, access, quality issues.
- Metrics: volume, cycle time, cost, error/rework, response time, revenue or risk impact.
- Validation call: what stakeholders corrected or confirmed.

Treat AI interview output as evidence to validate, not final truth.

## Consulting Workflow

1. Name the workflow, decision, or business question.
2. Identify the framework or concept being applied.
3. Gather local evidence from the mastery corpus or user artifacts.
4. Separate facts, assumptions, inferences, and recommendations.
5. Identify current claims that need external verification.
6. State risks, constraints, and stop conditions.
7. Tie every recommendation to a measurable business reason.
8. Give a practical next step.

## Output Structure

Use:

- Decision or workflow:
- Evidence used:
- Facts:
- Assumptions:
- Inferences:
- Risks:
- Recommendations:
- Current verification needed:
- Next actions:

For formal deliverables, include source references such as:

- `client-source/<file>.md`, page/slide/block reference.
- `analytics/artifacts/<file>.md`.
- Official current URL when web-verified.

## Do Not

- Hide uncertainty.
- Cite generated summaries as if they are original sources when source notes are available.
- Give current legal, privacy, security, vendor, or market claims from memory.
- Recommend automation without naming data, knowledge, governance, privacy/security, and measurement prerequisites.

## Quality Bar

The reader should be able to answer:

- Why this recommendation?
- What evidence supports it?
- What could make it wrong?
- What must be verified?
- Who owns the next decision?

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

