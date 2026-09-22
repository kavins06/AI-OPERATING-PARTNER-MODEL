---
name: managed-agent-lifecycle
description: "Create Step 18 machine-readable managed_lifecycle_object or lifecycle_set artifacts for future AI capabilities, remediation paths, or no-automation review cadences, covering ownership, approval, launch gates, validation, monitoring, feedback, truth governance, source freshness, access review, incident response, revocation, guidance updates, adoption/change management, expansion, retirement, and method-to-build handoff."
---

# Managed Agent Lifecycle

## Core Rule

Manage agents as living information systems, not one-time automations.

Inside the AI operating partner engagement, this skill produces the Step 18 future operating, remediation, no-automation, and adoption-change model only. Do not build, deploy, monitor, connect, or operate a client agent during the engagement.

The canonical artifact is a structured lifecycle object, not a narrative SOP. Markdown SOPs are generated views.

## Engagement Role

Step 18 consumes the Step 17 implementation decision packet or packet_set, Step 16 readiness object, Step 15 risk/control model, Step 14 technical blueprint, Step 13 solution/adoption design, Step 12 value case, Step 11 measurement intelligence, Step 10 guidance/evals, and Step 8 baseline/source/truth decisions.

Use these canonical method templates:

- `../ai-operating-partner-engagement/assets/templates/16-managed-lifecycle-object.yaml`
- `../ai-operating-partner-engagement/assets/templates/16-lifecycle-set.yaml`
- `../ai-operating-partner-engagement/assets/templates/16-lifecycle-variant-contracts.yaml`
- `../ai-operating-partner-engagement/assets/templates/16-managed-lifecycle-sop-view.md`
- `../ai-operating-partner-engagement/assets/templates/18-method-to-build-handoff-contract.md`

If Step 17 produced a packet_set, produce a lifecycle_set with one lifecycle per packet and cross-variant relationships. The lifecycle path must match the Step 17 packet type: build-ready packets get `managed_agent_lifecycle`, remediation-style packets get `remediation_lifecycle`, and do-not-automate packets get `no_automation_review_cadence`.

Useful references:

- `../../mastery-reference/information-management/operator-toolkit/agent-lifecycle-sop.md`
- `../../mastery-reference/combined-operating-model.md`
- `../../mastery-reference/combined-operating-model.md`

## Lifecycle Inputs

Start the lifecycle only after the operating partner has gathered:

- Validated workflow map.
- Business owner and success metric.
- Source inventory and governance model.
- Truth production profiles and truth governance model.
- Knowledge map and review criteria.
- Risk register.
- Zero-trust permission boundary.
- Step 16 readiness object with hard gates, behavior-level readiness, blockers, minimum safe first behavior, and Step 17 path.
- Step 17 machine-readable implementation decision packet with build scope or remediation path, future component contracts, access requests, normalization, tests, controls, owners, sequence, confidence, revision triggers, and stop conditions.
- Step 13 adoption design: target users, opt-in/mandate reality, incentives, training, feedback channels, workflow sunsetting, and adoption-failure triggers.
- Baseline metrics.
- Truth production status for baseline metrics and AI inputs.
- Human approval model.
- Monitoring requirements.
- Future access request package for agents, MCPs, connectors, normalization pipelines, and email/data access.

If the build team lacks these inputs, return to discovery, governance, knowledge capture, or risk design before deployment planning.

## Lifecycle Paths

Use one of three paths:

- `managed_agent_lifecycle`: the opportunity is build-ready or conditionally build-ready and needs a future operating contract.
- `remediation_lifecycle`: the opportunity is not build-ready and needs owned remediation, evidence, review cadence, and return to Step 16.
- `no_automation_review_cadence`: the opportunity should not be automated now and needs revisit conditions or an alternative operating recommendation.

## Lifecycle Stages

1. Intake: business outcome, owner, workflow, sources, risk class.
2. Readiness: hard gates, behavior-level readiness, value, workflow, source access, data quality, knowledge/guidance, measurement, risk/control, integration, oversight, and lifecycle.
3. Design: permissions, prompts, retrieval sources, tools, escalation, logs, tests.
4. Build: sandbox first, synthetic and historical examples, human review.
5. Validate: grounding, edge cases, controls, metrics, failure behavior.
6. Deploy: staged rollout, training, support, incident path.
7. Operate: monitor quality, drift, feedback, cost, source freshness, truth production, risk events.
8. Improve: refresh sources, update SOPs, tune tools, close gaps.
9. Expand: add scope only after evidence and owner approval.
10. Retire: remove unused, risky, or low-value flows.

## Required Lifecycle Object

Use `../ai-operating-partner-engagement/assets/templates/16-managed-lifecycle-object.yaml` as the canonical artifact.

The lifecycle object must include:

- Lifecycle path, operating status, and approval boundary.
- Source-input trace from Step 17, Step 16, Step 15, Step 14, Step 13, Step 12, Step 11, Step 10, Step 9, Step 8, and Step 6.
- Truth production governance: source drift checks, rule-change approval, reconciliation cadence, owner review, and shadow artifact retirement.
- Lifecycle scope: future AI behavior level, authorized and unauthorized behavior levels, target users, environments, and exclusions.
- Owner model: business, day-to-day, technical, data, security, risk/compliance, support, guidance update, measurement, source freshness, incident, revocation, future build, sponsor, and approval forum.
- Future lifecycle stages with entry criteria, exit criteria, approvals, and stop conditions.
- Launch gates: evals, controls, audit logging, human review workflow, revocation readiness, and support model.
- Validation plan.
- Monitoring plan, including truth production checks.
- Feedback and correction loop.
- Adoption/change management: training, incentive alignment, opt-in/mandate reality, communication plan, workflow sunsetting, adoption metrics, adoption-failure triggers, and remedial actions.
- Change management and revalidation triggers.
- Access review and revocation.
- Incident response.
- Governance cadence.
- Expansion criteria.
- Retirement criteria.
- Remediation lifecycle or no-automation review cadence when applicable.
- Final approval and conditions before implementation.
- Stop boundary confirming no build, live access, connector/MCP build, email ingestion, normalization build, deployment, monitoring, or live operation during the engagement.

## Operating Controls

Every managed agent needs:

- Business owner.
- Technical owner.
- Data steward.
- Risk owner.
- Source inventory.
- Truth production owner.
- Permission boundary.
- Human approval rules.
- Audit log.
- Monitoring dashboard.
- Incident path.
- Improvement cadence.

## Monitoring Metrics

Monitoring must cover more than uptime. Track:

- Task volume.
- Success rate.
- Correction rate.
- Escalation rate.
- Citation/source quality.
- Tool failures.
- Latency.
- Cost.
- User satisfaction.
- Business metric movement.
- Risk events.
- Data freshness.
- Truth production drift.
- Rule or macro change events.
- Source retrieval failures.
- Unsupported recommendation attempts.
- Approval gate bypass attempts.
- Access or permission errors.
- Human override rate.
- Guidance-update backlog.

## Launch And Expansion Rules

- Do not approve launch unless every launch gate has an owner, evidence, pass criteria, and stop condition.
- Do not expand scope until current-scope value, quality, risk, source freshness, access review, and user feedback are acceptable.
- Any new user group, source, tool action, output type, write/send behavior, or workflow step requires readiness reassessment and an updated implementation packet.
- Any major source, truth production chain, formula, macro, manual adjustment rule, policy, approval-threshold, document-type, model/runtime, or tool-contract change requires revalidation.

## Output Template

Produce a machine-readable lifecycle object with:

- Lifecycle path.
- Owners.
- Launch gates.
- Validation plan.
- Deployment or remediation stages.
- Monitoring plan.
- Feedback and correction loop.
- Change-management and revalidation triggers.
- Access review and revocation.
- Incident response.
- Governance cadence.
- Expansion criteria.
- Retirement criteria.
- Final approval status.

## Quality Bar

Do not propose expansion until the agent has evidence of accuracy, usefulness, controlled access, logged behavior, source freshness, acceptable risk, owner approval, and measurable value.

Do not finish Step 18 with unnamed owners for monitoring, incident response, revocation, guidance updates, source freshness, access review, adoption support, feedback triage, or workflow sunsetting.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

