# Agent Architecture Spec Checklist

Use this checklist for Section 2 phase 4: `agent_architecture_spec`.

## Inputs

- `solution_shape`
- `technical_blueprint`
- `risk_control_model`
- `implementation_decision_packet`
- Current `agent_build_contract` and `agent_build_plan`, when available.

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/agent-architecture-record.yaml`

Outputs:

- `agent_architecture_record`

## Entry Checks

- Confirm Step 18 handoff and separate implementation approval are present, approved, versioned, and cited.
- Confirm all required Section 1 inputs are approved, not merely drafted.
- Confirm the phase owner, technical reviewer, security reviewer, data owner, business approver, AgentOps owner, support owner, and revocation owner.
- Confirm the approved first behavior, behavior level, workflow boundary, target users, environments, sources, prohibited behaviors, prohibited actions, and approval conditions.
- Confirm previous Section 2 objects are current or explicitly unavailable with a blocker.

## Scope Checks

- Confirm the proposed architecture is equal to or narrower than the approved handoff.
- Confirm no new user group, source, tool, workflow boundary, environment, model class, output type, or behavior level has been added.
- Confirm no write, send, execute, delete, or autonomous action appears unless explicitly approved.
- Confirm empty write paths are documented as intentional controls, not omitted accidentally.
- Confirm every exception, unresolved condition, and assumption has an owner and decision date.

## Evidence Checks

- Attach evidence references for every material architectural claim.
- Cite the approved source artifact and version for every component, data path, tool dependency, and model/runtime constraint.
- Record missing evidence as a blocker; do not infer from convenience or implementation preference.
- Confirm privacy, latency, cost, data residency, retention, and audit constraints are backed by source evidence.
- Confirm security, data, risk/compliance, and AgentOps reviewers have accepted the evidence package or named explicit blockers.

## Phase-Specific Checks

- Map the approved behavior level to topology, orchestration, tool posture, human oversight, and environment posture.
- Document runtime, model gateway, orchestration, retrieval, tool adapter, human review, audit/trace, and operator-control components.
- Document read, write, retrieval, event, logging, secret, and human approval paths.
- Define model posture, including allowed/prohibited model classes, routing, fallback, context minimization, output constraints, and uncertainty behavior.
- Define identity posture, including agent identity, runtime service account, end-user delegation, impersonation prohibition, break-glass stance, review cadence, and revocation SLA.
- Define auditability, including required events, correlation IDs, redaction, retention, dashboard, and alert route.
- Define resilience behavior for invalid input, missing source data, unavailable tools, permission errors, model uncertainty, malformed output, partial success, latency breach, control violation, and cost spike.
- Record architectural decisions with options considered, rationale, rejected options, consequences, approver, date, and evidence.

## Phase Specific Checks

This compatibility heading intentionally mirrors `## Phase-Specific Checks` for automated validators that normalize hyphens differently. The authoritative checklist items are in `## Phase-Specific Checks`.

## Blocking Conditions

- Required handoff, approval, source input, owner, or evidence reference is missing.
- Architecture widens approved behavior level, users, sources, tools, actions, environments, or workflow boundary.
- Tool, data, identity, model, audit, secret, revocation, support, or rollback posture is undefined.
- Any write/send/execute/delete/autonomous path appears without explicit approval and human oversight policy.
- Failure behavior is ambiguous for a user-visible output, system side effect, policy violation, or partial success.
- The architecture cannot be implemented without returning to Section 1 for changed scope, risk, value, or oversight assumptions.

## Exit Checks

- `agent_architecture_record` is complete enough for engineering, security, data, and AgentOps review.
- Every architecture component has owner, purpose, environments, dependencies, interfaces, data classes, and audit events.
- Every data/system path has source, owner, classification, validation, environment, retention, and failure behavior.
- Rollback dependencies, stop conditions, human escalation, incident route, and material change triggers are explicit.
- Rubric criteria are passed, waived by an authorized owner, or marked blocked.
- Return-to-method triggers have been evaluated and documented.
- Next phase dependencies for tool contracts and environment access are explicit.

## Failure Modes

- Runtime topology does not match approved behavior level.
- Fallback and failure behavior are undefined.
- Model/runtime posture ignores privacy, latency, cost, data residency, or audit constraints.
- Component ownership, revocation, or support responsibility is ambiguous.
- Architecture requires a tool, source, write action, identity model, or environment not approved in the handoff.

## Return-To-Method Triggers

- Architecture requires a different behavior level, source, user group, workflow boundary, oversight model, or business process assumption.
- The only feasible architecture needs write/send capability that was not approved.
- Required source or owner evidence from Section 1 cannot be reconciled.
