---
name: managed-agentops-operations
description: "Operate live agents through metrics, source freshness, incidents, access review, guidance updates, and value tracking. Use after approved Step 18 handoff and separate implementation approval as part of the Section 2 build and Managed AgentOps backbone."
---

# Managed AgentOps Operations

## Boundary

Use this skill only for Section 2 Phase 13 after Step 18 handoff approval, production readiness approval, and separate implementation approval. This skill operates a live or limited-pilot agent; it does not approve new scope, repair missing Section 1 decisions, or silently convert a pilot learning into a new capability.

Stop and return to the `agent-build-managed-agentops` orchestrator when the requested work belongs to build, architecture, evals, access setup, pilot, production readiness, or release management. Stop and return to the Section 1 method owner when operational evidence invalidates the approved value case, readiness score, risk posture, owner model, source-of-truth assumptions, or managed lifecycle decision.

Phase 13 is allowed to keep the current release healthy, pause or revoke unsafe operation, record incidents, update operating evidence, and recommend change, expansion, retirement, or redesign review. It is not allowed to widen users, tools, sources, workflow boundaries, write/send permissions, model autonomy, or behavior level.

## Required Inputs

Use the Section 1 to Section 2 handoff map before producing outputs:

- `../agent-build-managed-agentops/assets/mappings/section1-to-section2-handoff-map.yaml`

Required Section 1 inputs for Phase 13:

- `managed_lifecycle_object`
- `measurement_intelligence`
- `ai_guidance_pack`
- `organizational_intelligence_baseline`
- `risk_control_model`

Required Section 2 operating inputs:

- `agent_build_contract`
- `release_version_manifest`
- `production_readiness_gate`
- `trace_observability_spec`
- `guardrail_control_matrix`
- `tool_contract_registry`
- `eval_harness_spec`
- `incident-revocation-runbook.md`
- `internal-operator-run-card.md`

## Owned Phases

- Phase 13: Managed AgentOps.

### Phase 13: Managed AgentOps

Purpose: operate the approved agent release while preserving the Step 17/18 scope and detecting the moment the agent should pause, enter change control, return to method, retire, or be redesigned.

Section 1 inputs:

- `managed_lifecycle_object`
- `measurement_intelligence`
- `ai_guidance_pack`
- `organizational_intelligence_baseline`
- `risk_control_model`

Section 2 outputs:

- `agentops_operating_record`

Templates:

- `skills/agent-build-managed-agentops/assets/templates/agentops-operating-record.yaml`
- `skills/agent-build-managed-agentops/assets/templates/internal-operator-run-card.md`

Execution requirements:

- Confirm the release version, environment, authorized behavior level, live users, workflow boundaries, allowed sources, enabled tools, scale limits, and explicit exclusions before reviewing health.
- Confirm named owner coverage for business, technical, security, data, support, AgentOps, and revocation responsibilities. Add backup coverage for vacations, weekends, critical incidents, and client holidays.
- Review quality, safety, reliability, adoption, value, cost, latency, source freshness, and support metrics against target, warning, and blocking thresholds.
- Verify source freshness for every authoritative source used by the agent. If a source is stale beyond SLA, missing owner attestation, or contradicted by a newer source, pause affected output paths or force human review.
- Perform access review for user entitlements, service accounts, tool credentials, connectors, secrets, groups, and break-glass permissions. Revoke orphaned, overbroad, unused, or unapproved access.
- Review incidents, near misses, user corrections, manual overrides, and control alerts. Open an incident if evidence shows unsafe output, missing traces, unauthorized scope, or material business impact.
- Rehearse or verify pause, rollback, and revocation mechanisms on the required cadence. Evidence must include who can act, what is revoked, how queued work is stopped, and how restoration is approved.
- Track business value against the measurement baseline. If value cannot be measured, is below minimum viable threshold for two review cycles, or is offset by operating burden, open retirement or redesign review.
- Record guidance updates, source updates, prompt/model/runtime changes, and runbook changes. Material changes must go to Phase 14 before production use.
- Complete the phase checklist and apply the phase rubric before marking the operating cycle passed.

Stop conditions:

- Any unauthorized write, send, deletion, permission change, workflow progression, user expansion, source use, tool call, or behavior-level escalation.
- Any critical or high severity incident, privacy/security exposure, untraced run, audit-log gap for a tool call, or control bypass.
- Source freshness SLA missed for a source used in user-visible output without a safe fallback.
- Required owner coverage is absent for an active operating window or revocation owner cannot be reached within the response SLA.
- Quality, safety, reliability, or value metric crosses a blocking threshold.
- The agent depends on a source, tool, model, workflow, or approval path that no longer matches the approved handoff.
- Sponsor, business owner, security owner, or risk owner requests pause.

Return-to-method triggers:

- Value metrics show the original business value case is no longer credible.
- Adoption, correction, or support patterns show the workflow diagnosis or organizational readiness assumptions were wrong.
- New user groups, sources, data classes, tools, or autonomy are needed to make the agent useful.
- The source-of-truth model has changed, is disputed, or cannot be governed by the current owner model.
- Incident history reveals a risk scenario not covered by the approved risk control model.
- The accountable owner model is no longer viable.

Implementation example:

- A revenue intake draft-and-flag agent has a weekly target of `draft_acceptance_rate >= 0.90`, `control_violation_count = 0`, `untraced_run_count = 0`, and source freshness for CRM field definitions within 7 days. If the CRM field definition source is 13 days old and the data owner cannot attest to it, the operator pauses drafts that cite those fields, routes records to manual review, opens an operating issue, and schedules a Phase 14 review if the source model changed.

## Resource Map

- Local phase packs: `assets/phase-packs`
- `../agent-build-managed-agentops/assets/schemas/agentops-object-schemas.yaml`
- `../agent-build-managed-agentops/assets/templates/agentops-operating-record.yaml`
- `../agent-build-managed-agentops/assets/templates/internal-operator-run-card.md`
- `../agent-build-managed-agentops/assets/templates/incident-revocation-runbook.md`
- `../agent-build-managed-agentops/assets/checklists/agentops-weekly-review-checklist.md`
- `../agent-build-managed-agentops/assets/rubrics/agentops-operating-health-rubric.yaml`
- `../agent-build-managed-agentops/assets/validator-rules/managed_agentops.yaml`
- `../agent-build-managed-agentops/assets/examples/golden-path/13-agentops-operating-record.yaml`
- `../agent-build-managed-agentops/assets/examples/golden-path-revenue-intake.yaml`

## Workflow

1. Confirm the approved handoff, current release manifest, production readiness gate, operating record, and run card all reference the same agent, environment, behavior level, and owner model.
2. Check stop conditions first. If any stop condition is met, pause or revoke before continuing the routine review.
3. Review owner coverage and escalation readiness. Record named primary and backup owners plus any coverage gaps.
4. Review operating metrics against target, warning, and blocking thresholds. Attach dashboard, trace, incident, user feedback, and finance evidence.
5. Review source freshness and guidance currency. Mark stale sources, changed policy, stale prompts, or missing owner attestations as blockers when they affect output.
6. Review access and tool permissions. Remove unused or unapproved access and log every permission change.
7. Review incidents, near misses, control alerts, manual overrides, and support themes. Link each to a decision: monitor, remediate, pause, change review, retirement review, or return to method.
8. Review value realization, adoption, operating cost, and human workload. Compare against the Section 1 measurement baseline and decision threshold.
9. Update the `agentops_operating_record`, run card, incident log, open action register, and next review date.
10. Apply the rubric. Do not mark the review healthy unless all required criteria pass with evidence or an authorized waiver.

## Output Contracts

- `agentops_operating_record`: source-of-truth record for current release health, owner coverage, live scope, metric thresholds, source freshness, access review, incidents, revocation readiness, value tracking, guidance updates, open actions, decisions, and next review.
- `internal_operator_run_card`: human-readable on-call card derived from the operating record. It must be current enough that a backup operator can pause, revoke, escalate, or route to manual fallback without reconstructing the full build packet.

## Quality Bar

Do not widen approved scope. Do not operate without named owner coverage, traceability, current sources, reviewed access, measurable value, incident response path, and tested revocation path. Treat missing evidence as a blocker. Treat convenience-driven expansion as a defect. Treat a live agent with no clear stop condition as unmanaged software, not Managed AgentOps.
