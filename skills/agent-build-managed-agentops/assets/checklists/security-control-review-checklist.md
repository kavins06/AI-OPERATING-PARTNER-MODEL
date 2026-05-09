# Security And Control Review Checklist

Use this checklist for Section 2 phase 9: `security_and_control_review`.

## Inputs

- `risk_control_model`
- `technical_blueprint`
- `managed_lifecycle_object`

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/guardrail-control-matrix.yaml`
- `skills/agent-build-managed-agentops/assets/templates/trace-observability-spec.yaml`

Outputs:

- `guardrail_control_matrix`
- `trace_observability_spec`

## Entry Checks

- Confirm required Section 1 inputs and Section 2 architecture/tool/eval artifacts are approved and cited.
- Confirm the security reviewer, risk owner, data owner, technical owner, AgentOps owner, and revocation owner are named.
- Confirm scope remains equal to or narrower than Step 17/18 approval.
- Confirm every residual risk has a proposed control, owner, and approval path.
- Confirm current implementation can emit trace and audit data in the target environments.

## Scope Checks

- Confirm security controls enforce only the approved behavior level, user groups, workflow boundaries, sources, tools, environments, data classes, and outputs.
- Confirm no unapproved write, send, export, privileged action, model/runtime, or data path is reachable.
- Confirm human review, revocation, logging, and incident controls match the approved lifecycle and oversight model.
- Confirm any security-required architecture, tool, source, or access change is routed to change review or return-to-method.

## Phase-Specific Checks

- Verify every risk maps to one or more implemented controls with owner, test method, pass criteria, fail behavior, and evidence.
- Verify default-deny behavior for unregistered tools, unauthorized users, unsupported actions, unknown intent, missing source, stale source, and trace failure.
- Test permission boundaries for every registered tool, identity, environment, data class, action type, and role.
- Test adversarial controls for prompt injection, hidden instruction disclosure, data exfiltration, policy conflict, and social-pressure escalation.
- Confirm human-review gates cannot be bypassed, reused after expiry, or approved by unauthorized reviewers.
- Confirm sensitive data minimization and log redaction apply to prompts, outputs, traces, tool inputs, and incident evidence.
- Confirm trace events exist for run start, input, retrieval, model call, tool call, control decision, output, human review, alert, incident, and completion.
- Confirm alert routes, response SLAs, dashboard metrics, and owner notifications are live or blocked.
- Rehearse pause, revoke access, disable tool/feature flag, rollback release, preserve evidence, notify owners, and restart approval.
- Confirm residual risk acceptance is explicit, dated, conditioned, and approved by authorized owners.

## Evidence Checks

- Attach permission-boundary test results.
- Attach adversarial and data-exfiltration test results.
- Attach tool denial and human-review bypass test results.
- Attach trace completeness report and representative audit-log samples.
- Attach dashboard and alert-routing proof.
- Attach incident rehearsal notes and remediation evidence.
- Attach residual-risk approval or blocker record.

## Exit Checks

- `guardrail_control_matrix` reflects implemented and tested controls.
- `trace_observability_spec` lists required fields, metrics, alerts, dashboards, retention, redaction, and access roles.
- Control failure, trace failure, and incident handling fail closed.
- Revocation and rollback paths have named owners and measured time-to-pause/time-to-restore targets.
- Return-to-method triggers have been evaluated and recorded.

## Blocking Conditions

- Residual risk lacks authorized owner approval.
- Any control lacks owner, evidence, pass criteria, fail behavior, or test result.
- Any tool call or production run can occur without required trace fields.
- Any unapproved write, send, export, privileged action, or data source is reachable.
- Human approval can be bypassed or cannot be audited.
- Sensitive data is logged or exposed without approved redaction and retention controls.
- Incident rehearsal fails pause, revoke, rollback, evidence capture, owner notification, or restart approval.

## Failure Modes

- Residual risk is accepted without owner approval.
- Audit, revocation, or incident evidence is missing.

## Return-To-Method Triggers

- Security control requires different architecture, behavior, or data path.
- Security review changes approved scope, source, access, oversight, lifecycle, or risk assumptions.
