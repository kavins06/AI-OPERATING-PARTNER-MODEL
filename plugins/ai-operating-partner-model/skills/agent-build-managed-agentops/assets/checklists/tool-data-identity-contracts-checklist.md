# Tool/Data/Identity Contracts Checklist

Use this checklist for Section 2 phase 5: `tool_data_identity_contracts`.

## Inputs

- `technical_blueprint`
- `organizational_intelligence_baseline`
- `risk_control_model`
- `implementation_decision_packet`
- Current `agent_architecture_record`.

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/tool-contract-registry.yaml`

Outputs:

- `tool_contract_registry`

## Entry Checks

- Confirm Step 18 handoff and separate implementation approval are present, approved, versioned, and cited.
- Confirm the architecture record is current and no tool dependency exceeds the approved architecture.
- Confirm system owner, technical owner, data owner, security owner, AgentOps owner, support owner, and revocation owner for every tool candidate.
- Confirm approved behavior level, user groups, workflow boundary, sources, environments, prohibited actions, and approval conditions.
- Confirm open blockers and assumptions are listed with owner and decision date.

## Scope Checks

- Confirm every registered tool traces to an approved source, component, or data/system path.
- Confirm unregistered tools are disabled and unknown tool names are blocked and logged.
- Confirm least privilege: each permission is narrowly scoped by environment, action, endpoint, data class, and identity.
- Confirm no write, send, create, update, delete, execute, or workflow action is present without explicit approval, human approval policy, audit event, idempotency, and rollback or compensation behavior.
- Confirm tool use is equal to or narrower than the approved handoff and architecture record.

## Evidence Checks

- Attach evidence references for owner approval, source-of-truth validation, permission scope, data classification, and access request.
- Attach sandbox fixture, permission test, negative test, audit-log test, revocation drill, and rollback or compensation test evidence where applicable.
- Record missing evidence as a blocker instead of approximating the contract.
- Confirm every data field exposed to the agent has classification, validation, freshness, retention, redaction, and prohibited-use rules.
- Confirm every side effect has reconciliation evidence or is blocked.

## Phase-Specific Checks

- Register every API, MCP tool, connector, database, document store, workflow action, notification system, and human handoff tool.
- Define approved use cases, prohibited use cases, environments, endpoints/actions, input schema, output schema, side effects, and downstream use.
- Define identity model: agent identity, runtime service account, end-user delegation, impersonation prohibition, credential storage, token rotation, access review, break-glass policy, and emergency revocation SLA.
- Define invocation policy: allowed/prohibited conditions, rate limits, concurrency limits, timeout, retry, idempotency key, human approval requirement, and approval policy reference.
- Define failure behavior for validation error, permission error, unavailable service, stale data, partial success, duplicate invocation, unexpected side effect, and downstream policy rejection.
- Define audit fields for every tool call, including run ID, actor ID, release version, environment, permission scope, approval reference, latency, status, and error code.
- Confirm secrets never appear in source control, local files, plaintext logs, prompts, traces, or exported payloads.
- Confirm production enablement is blocked until the environment progression gate approves that tool in that environment.

## Phase Specific Checks

This compatibility heading intentionally mirrors `## Phase-Specific Checks` for automated validators that normalize hyphens differently. The authoritative checklist items are in `## Phase-Specific Checks`.

## Blocking Conditions

- A tool lacks owner, purpose, approved use case, permission scope, audit event, failure behavior, or revocation path.
- Identity mapping is ambiguous or allows unapproved impersonation/delegation.
- Any write/send/execute/delete action lacks explicit approval, human approval policy, idempotency, reconciliation, and rollback or compensation plan.
- Data contract lacks authoritative source, field classification, freshness, retention, redaction, validation, or prohibited field rules.
- A side effect can occur without auditability, alerting, or operator recovery.
- Required least-privilege access cannot be provisioned by the system owner.

## Exit Checks

- `tool_contract_registry` is complete enough for implementation, security review, data owner approval, and environment provisioning.
- Every tool has owner, environments, permissions, identity model, input/output contract, data contract, audit fields, failure behavior, revocation path, test evidence, and approval status.
- Registry policy denies unregistered tools and blocks production enablement until environment gate approval.
- Rubric criteria are passed, waived by an authorized owner, or marked blocked.
- Return-to-method triggers have been evaluated and documented.
- Phase 6 dependencies for access, secrets, network, data, and environment setup are explicit.

## Failure Modes

- Tool lacks owner, permission scope, audit logging, failure behavior, or revocation path.
- Identity mapping is ambiguous.
- Write/send action appears without explicit approval.
- Data contract lacks source-of-truth, classification, freshness, retention, validation, or prohibited-field rules.
- Tool output can drive user-visible or system side effects without a reconciliation path.

## Return-To-Method Triggers

- Tool requires access not approved in Step 17/18.
- Required system owner refuses or cannot provide least-privilege access.
- The approved outcome cannot be delivered without a new source, user group, workflow action, or identity assumption.
