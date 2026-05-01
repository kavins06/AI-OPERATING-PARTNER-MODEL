---
name: managed-agent-lifecycle
description: "Create machine-readable managed lifecycle objects for future AI capabilities, covering ownership, approval, launch gates, validation, deployment stages, monitoring, feedback, source freshness, access review, incident response, revocation, guidance updates, expansion, retirement, remediation cadence, and no-automation review cadence. Use after readiness and implementation decision planning."
---

# Managed Agent Lifecycle

## Core Rule

Manage agents as living information systems, not one-time automations.

Inside the AI operating partner engagement, this skill produces the future operating model only. Do not build, deploy, monitor, or operate a client agent during the 16-step engagement.

The source of truth is a structured lifecycle object, not a narrative SOP. Markdown SOPs are generated views.

Useful references:

- `../../mastery-reference/information-management/operator-toolkit/agent-lifecycle-sop.md`
- `../../mastery-reference/combined-operating-model.md`
- `../../mastery-reference/combined-operating-model.md`

## Lifecycle Inputs

Start the lifecycle only after the operating partner has gathered:

- Validated workflow map.
- Business owner and success metric.
- Source inventory and governance model.
- Knowledge map and review criteria.
- Risk register.
- Zero-trust permission boundary.
- Step 14 readiness object with hard gates, behavior-level readiness, blockers, minimum safe first behavior, and Step 15 path.
- Step 15 machine-readable implementation decision packet with build scope or remediation path, future component contracts, access requests, normalization, tests, controls, owners, sequence, and stop conditions.
- Baseline metrics.
- Human approval model.
- Monitoring requirements.
- Future access request package for agents, MCPs, connectors, normalization pipelines, and email/data access.

If the build team lacks these inputs, return to discovery, governance, knowledge capture, or risk design before deployment planning.

## Lifecycle Paths

Use one of three paths:

- `managed_agent_lifecycle`: the opportunity is build-ready or conditionally build-ready and needs a future operating contract.
- `remediation_lifecycle`: the opportunity is not build-ready and needs owned remediation, evidence, review cadence, and return to Step 14.
- `no_automation_review_cadence`: the opportunity should not be automated now and needs revisit conditions or an alternative operating recommendation.

## Lifecycle Stages

1. Intake: business outcome, owner, workflow, sources, risk class.
2. Readiness: hard gates, behavior-level readiness, value, workflow, source access, data quality, knowledge/guidance, measurement, risk/control, integration, oversight, and lifecycle.
3. Design: permissions, prompts, retrieval sources, tools, escalation, logs, tests.
4. Build: sandbox first, synthetic and historical examples, human review.
5. Validate: grounding, edge cases, controls, metrics, failure behavior.
6. Deploy: staged rollout, training, support, incident path.
7. Operate: monitor quality, drift, feedback, cost, source freshness, risk events.
8. Improve: refresh sources, update SOPs, tune tools, close gaps.
9. Expand: add scope only after evidence and owner approval.
10. Retire: remove unused, risky, or low-value flows.

## Required Lifecycle Object

Use `../ai-operating-partner-engagement/assets/templates/16-managed-lifecycle-object.yaml` as the canonical artifact.

The lifecycle object must include:

- Lifecycle path, operating status, and approval boundary.
- Source-input trace from Step 15, Step 14, Step 13, Step 12, Step 11, Step 10, Step 9, Step 7, and Step 5.
- Lifecycle scope: future AI behavior level, authorized and unauthorized behavior levels, target users, environments, and exclusions.
- Owner model: business, day-to-day, technical, data, security, risk/compliance, support, guidance update, measurement, source freshness, incident, revocation, future build, sponsor, and approval forum.
- Future lifecycle stages with entry criteria, exit criteria, approvals, and stop conditions.
- Launch gates: evals, controls, audit logging, human review workflow, revocation readiness, and support model.
- Validation plan.
- Monitoring plan.
- Feedback and correction loop.
- Change management and revalidation triggers.
- Access review and revocation.
- Incident response.
- Governance cadence.
- Expansion criteria.
- Retirement criteria.
- Remediation lifecycle or no-automation review cadence when applicable.
- Final approval and conditions before implementation.
- Stop boundary confirming no build or live operation during the 16-step engagement.

## Operating Controls

Every managed agent needs:

- Business owner.
- Technical owner.
- Data steward.
- Risk owner.
- Source inventory.
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
- Any major source, policy, approval-threshold, document-type, model/runtime, or tool-contract change requires revalidation.

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

Do not finish Step 16 with unnamed owners for monitoring, incident response, revocation, guidance updates, source freshness, or access review.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

