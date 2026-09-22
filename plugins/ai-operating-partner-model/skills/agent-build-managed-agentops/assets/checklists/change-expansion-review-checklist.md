# Expansion/Change-Control Gate Checklist

Use this checklist for Section 2 Phase 14: `expansion_change_control_gate`. Treat every requested change as material until the review proves it stays inside approved scope with no change to value, risk, readiness, source ownership, access, operating model, or behavior level.

## Inputs

- `managed_lifecycle_object`
- `readiness_object`
- `implementation_decision_packet`
- `method_to_build_handoff_contract`
- `agentops_operating_record`
- `release_version_manifest`
- `tool_contract_registry`
- `eval_harness_spec`
- `guardrail_control_matrix`
- `trace_observability_spec`
- incident, source, access, value, support, and adoption evidence

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/change-expansion-retirement-review.yaml`

Outputs:

- `change_expansion_retirement_review`

## Entry Checks

- Confirm the requested change has a named requester, business reason, affected release, desired effective date, and accountable sponsor.
- Confirm required Section 1 source artifacts are approved, current, versioned, and cited.
- Confirm the current operating record, release manifest, production gate, tool registry, eval harness, guardrail matrix, and trace spec are available.
- Confirm open incidents, unresolved waivers, source freshness issues, access exceptions, and owner coverage gaps are listed.
- Confirm the current approved scope is frozen before comparing requested deltas.

## Scope Checks

- Compare requested users, workflows, systems, tools, sources, data classes, outputs, environments, scale limits, model/runtime, support model, and behavior level to the current approved scope.
- Confirm approved scope and denied scope will both be documented in the decision record.
- Confirm any new write/send/autonomous action, new source-of-truth, or new workflow outcome is treated as material and routed to required approval or return to method.
- Confirm no implementation work begins before decision, owner coverage, rollback, and revocation conditions are accepted.

## Phase-Specific Checks

- Classification: classify request as non-material change, material change, expansion, remediation, rollback, retirement candidate, redesign candidate, or return-to-method candidate.
- Scope delta: enumerate deltas for users, workflows, systems, tools, sources, data classes, outputs, environment, scale, model/runtime, prompt/guidance, access, support model, and behavior level.
- Behavior level: verify no movement into write, send, delete, approve, schedule, route, payment, account, permission, human-approved action, or autonomous action without explicit approval and updated controls.
- Source freshness: verify every new or changed source has authoritative owner, freshness SLA, last verification, attestation, conflict handling, and stale-source action.
- Access review: verify every new or changed user group, service account, tool credential, connector, secret, group, or permission has owner, minimum scope, revocation path, and audit evidence.
- Value reassessment: compare requested change to measurement baseline, expected incremental value, support burden, operating cost, and adoption evidence.
- Risk and readiness reassessment: identify new risk scenarios, changed likelihood or impact, readiness gaps, human oversight burden, and residual risk owners.
- Evals and controls: require updated evals, guardrails, trace events, alerts, smoke tests, rollback tests, and human review controls for the changed behavior.
- Owner coverage: confirm business, technical, security, data, support, AgentOps, and revocation coverage for rollout and steady state.
- Rollout plan: define limited population, timebox, monitoring cadence, stop conditions, user communications, manual fallback, rollback package, and revocation targets.
- Contract updates: identify required updates to build contract, release manifest, tool registry, eval harness, guardrail matrix, trace spec, operating record, run card, and incident runbook.

## Blocking Conditions

- Requested change adds an unapproved write, send, delete, approval, scheduling, routing, permission-changing, payment, account, or autonomous action.
- Requested change adds a user group, workflow, source, data class, tool, system, environment, output channel, behavior level, model route, or operating model outside approved handoff without return-to-method decision.
- Required Section 1 input is missing, stale, contradicted, or not approved.
- Any affected source, tool, data class, access path, support path, or revocation path lacks a named owner.
- Existing high or critical incident, unresolved control violation, or unresolved access exception affects the requested change.
- Updated evals, guardrails, traceability, rollback, revocation, or manual fallback cannot cover the changed behavior.
- Business value cannot be stated, measured, or tied to the original value case.
- Owner coverage is not available during rollout or steady-state operation.
- Required approver refuses, is absent, or adds conditions that are not incorporated.

## Evidence Checks

- Attach evidence for current scope, requested delta, metric baseline, expected value, source review, access review, risk review, readiness review, eval results, control tests, rollout plan, rollback test, and owner approvals.
- Record missing evidence as a blocker rather than an assumption.
- Confirm all waivers have owner, rationale, expiry, and compensating control.
- Confirm denied scope is explicit enough to prevent accidental expansion later.

## Exit Checks

- `change_expansion_retirement_review` is complete.
- Decision outcome is one of: approve, approve with conditions, hold, rollback, retire, redesign, or return to method.
- Approved and denied scope are both documented.
- Required actions have owner, due date, blocker status, and evidence target.
- Stop conditions, rollback trigger, revocation targets, and next review date are recorded.
- Operating record and run card update requirements are listed.
- Rubric criteria are passed, waived by authorized owner with expiry, or marked blocked.

## Realistic Examples

- Limited expansion: add two additional intake coordinators in the same workflow and same read-only tools. Still requires user entitlement review, owner coverage, monitoring limit, and Phase 14 approval.
- Blocked expansion: add CRM write access to mark `missing_info_requested`. This is a new write action; hold until revised tool contract, controls, evals, access review, rollback, and method risk/value review are approved.
- Return to method: expand from revenue intake to customer renewal risk scoring. This is a different workflow and business outcome; route back to Section 1 discovery and lifecycle decision.

## Failure Modes

- New user, source, tool, workflow, behavior level, model, or write/send action is added without approval.

## Return-To-Method Triggers

- Expansion changes readiness, risk, value, or lifecycle assumptions.
