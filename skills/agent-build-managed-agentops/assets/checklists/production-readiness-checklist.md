# Production Readiness Gate Checklist

Use this checklist for Section 2 phase 11: `production_readiness_gate`.

## Inputs

- `managed_lifecycle_object`
- `measurement_intelligence`
- `risk_control_model`
- `technical_blueprint`

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/production-readiness-gate.yaml`

Outputs:

- `production_readiness_gate`

## Entry Checks

- Confirm pilot is complete or has enough approved evidence for production decision.
- Confirm production scope is no wider than approved handoff and pilot-tested behavior unless change review approved it.
- Confirm production owners, support, security, data, risk, AgentOps, revocation, and release owners are named.
- Confirm eval, guardrail, trace, release, pilot, support, incident, access-review, and rollback evidence is attached.
- Confirm every open issue has severity, owner, due date, production impact, and decision.

## Scope Checks

- Confirm production scope is equal to or narrower than approved Step 17/18 scope and pilot-tested scope.
- Confirm production users, workflow boundaries, sources, tools, data classes, environments, behavior level, outputs, and scale limits are explicit.
- Confirm first-month expansion freeze or change-control rule is documented.
- Confirm any production scope increase has approved change review before the gate is passed.

## Phase-Specific Checks

- Summarize pilot evidence: total runs, active users, success rate, material error rate, correction rate, adoption signal, incidents, defects, control violations, and untraced runs.
- Verify all blocking eval, adversarial, regression, control, trace, and pilot thresholds pass after remediation.
- Verify residual risk acceptance is explicit, conditioned, dated, and approved by authorized owners.
- Verify production support model, operator run card, escalation path, incident channel, and owner rota are live.
- Verify trace completeness and dashboards cover quality, safety, reliability, adoption, value, cost, source freshness, access, and incidents.
- Verify first-30-day monitoring cadence, review agenda, thresholds, stop conditions, and owners.
- Verify access review, credential revocation, source freshness checks, and truth-production controls are scheduled.
- Rehearse incident response: detect, alert, pause, revoke, rollback, preserve evidence, communicate, remediate, approve restart.
- Verify release candidate manifest, smoke tests, feature flags, config/secrets changes, and rollback package are ready for phase 12.
- Evaluate return-to-method triggers for scope, owner, risk, truth, value, adoption, or lifecycle changes.

## Evidence Checks

- Attach pilot metric summary and daily review records.
- Attach eval/regression/adversarial rerun results after pilot defects.
- Attach trace completeness and dashboard proof.
- Attach access review and permission-boundary evidence.
- Attach incident rehearsal evidence with measured time to detect, pause, revoke, and restore.
- Attach residual risk acceptance and owner signoffs.
- Attach release candidate and rollback evidence.

## Exit Checks

- `production_readiness_gate` includes a go/conditional/hold/return-to-method decision.
- Production scope, scale limits, first-month expansion freeze, stop conditions, and monitoring cadence are explicit.
- Required owners have accepted production responsibilities.
- Phase 12 release dependencies are explicit.
- Return-to-method triggers have been evaluated and recorded.

## Blocking Conditions

- Pilot evidence is missing, incomplete, or fails blocking thresholds without remediation and retest.
- Production launch lacks owner signoff, residual-risk acceptance, incident rehearsal, revocation readiness, or rollback evidence.
- Any production run or tool call could be untraced.
- Any control, access review, source freshness, support, or monitoring owner is unnamed.
- Production scope exceeds approved/pilot-tested behavior without change review.
- Incident rehearsal fails pause, revoke, rollback, evidence capture, communication, or restart approval.

## Failure Modes

- Production launch lacks pilot evidence, owner signoff, incident rehearsal, revocation readiness, or accepted residual risk.

## Return-To-Method Triggers

- Production readiness requires scope, owner, risk, or lifecycle changes.
- Production evidence invalidates value, adoption, source truth, oversight, or operational assumptions.
