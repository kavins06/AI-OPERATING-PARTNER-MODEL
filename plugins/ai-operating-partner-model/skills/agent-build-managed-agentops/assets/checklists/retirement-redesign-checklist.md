# Retirement Or Redesign Loop Checklist

Use this checklist for Section 2 Phase 15: `retirement_or_redesign_loop`. Run it when operating evidence suggests the agent should pause, remediate, retire, redesign, or return to method.

## Inputs

- `managed_lifecycle_object`
- `measurement_intelligence`
- `risk_control_model`
- `organizational_intelligence_diagnostic`
- `agentops_operating_record`
- `release_version_manifest`
- incident, support, correction, adoption, value, cost, source freshness, access, and owner coverage evidence

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/change-expansion-retirement-review.yaml`
- `skills/agent-build-managed-agentops/assets/templates/incident-revocation-runbook.md`

Outputs:

- `change_expansion_retirement_review`
- decommission, redesign, remediation, or return-to-method action register

## Entry Checks

- Confirm the trigger: low value, high correction burden, high risk, source drift, access failure, owner coverage gap, low adoption, operational cost, incident pattern, simpler alternative, or sponsor request.
- Confirm required Section 1 source artifacts are approved, current, versioned, and cited.
- Confirm current release, operating record, incidents, metrics, support logs, user feedback, access reviews, and source freshness evidence are available.
- Confirm whether the agent should be paused immediately before the review continues.
- Confirm user and downstream process dependencies before retiring or changing operation.

## Scope Checks

- Confirm the current retirement or redesign discussion starts from approved live scope, not from aspirational future scope.
- Confirm any proposed redesign deltas across users, workflows, tools, sources, data classes, outputs, behavior level, environment, or owner model are listed.
- Confirm retirement removes or disables only approved current scope unless a separate change decision covers broader decommissioning.
- Confirm any redesign that changes method assumptions is routed back to Section 1 rather than handled as an internal patch.

## Phase-Specific Checks

- Value evidence: compare realized value, net time saved, quality improvement, revenue or cost impact, and human correction burden against the measurement baseline and minimum viable value threshold.
- Risk evidence: review incidents, near misses, control violations, privacy/security findings, audit gaps, residual risk, and accepted waivers.
- Source evidence: review freshness failures, disputed authority, missing source owner, stale guidance, source model changes, and unresolved data quality issues.
- Access evidence: review unused access, overbroad access, orphaned credentials, missing service account owner, revocation failures, and user entitlement drift.
- Owner coverage: verify business, technical, AgentOps, support, security, data, risk, and revocation ownership remains viable.
- Adoption evidence: review active users, opt-outs, manual workarounds, support tickets, training gaps, incentive conflicts, and workflow mismatch.
- Operating burden: compare monitoring, support, correction, incident, model, source, and access review burden to realized value.
- Alternative paths: evaluate simpler process, SOP, dashboard, template, workflow automation, report, or retirement without replacement.
- Redesign fit: identify whether redesign stays inside approved lifecycle or requires new discovery, readiness scoring, risk controls, value case, and build approval.
- Transition plan: define user communications, manual fallback, data retention, queued work closure, access revocation, tool disablement, dashboard retirement, and archive evidence.

## Blocking Conditions

- High or critical incident remains unresolved and the agent is still active.
- Agent cannot operate with current sources, controls, traces, access, and named owner coverage.
- Users are relying on outputs that no longer have current source or control evidence.
- Value is below minimum viable threshold for two consecutive review cycles and no owner-approved remediation plan exists.
- Human correction, support, or monitoring burden exceeds realized value and no redesign owner is assigned.
- Retirement would strand users, queued actions, records, reports, downstream processes, or compliance evidence without a transition plan.
- Redesign changes user group, workflow, source, data class, tool, behavior level, owner model, or business outcome without return-to-method routing.
- Required business, security, risk, technical, data, or support owner refuses to continue operation.

## Evidence Checks

- Attach metric, incident, trace, support, user feedback, value, source, access, cost, and owner coverage evidence.
- Record missing evidence as a blocker.
- Confirm every proposed remediation has owner, due date, validation method, and stop condition.
- Confirm retirement/decommission actions include actor, timestamp, target, validation check, and evidence location.
- Confirm redesign recommendations identify which Section 1 artifacts must be reopened.

## Exit Checks

- `change_expansion_retirement_review` is complete.
- Decision outcome is one of: continue with conditions, pause and remediate, rollback, retire, redesign, or return to method.
- If continuing, conditions, thresholds, owner coverage, and next review are documented.
- If retiring, user communications, fallback process, access revocation, tool disablement, data retention, evidence archive, and monitoring shutdown are documented.
- If redesigning, method-return scope and required Section 1 artifacts are listed.
- Operating record and run card are updated.
- Rubric criteria are passed, waived by authorized owner with expiry, or marked blocked.

## Realistic Examples

- Retire: a pilot agent has 8 percent active use, misses its value threshold for two cycles, and duplicates a dashboard now used by the team. Retire, revoke access, archive evidence, and update users to the dashboard path.
- Redesign: a draft agent is useful only when it can update CRM status after human approval. That adds a write action and changes risk; pause expansion and return to method for a new lifecycle decision.
- Remediate: a source owner missed one attestation but source content is unchanged and human fallback exists. Hold expansion, require source attestation within 3 business days, and continue limited operation if no blocker remains.

## Failure Modes

- Low value, high correction rate, source drift, ownership gap, or unacceptable risk continues without pause, redesign, or retirement.

## Return-To-Method Triggers

- Redesign requires new discovery, readiness scoring, or lifecycle decision.
