# Environment And Access Setup Checklist

Use this checklist for Section 2 phase 6: `environment_and_access_setup`.

## Inputs

- `technical_blueprint`
- `risk_control_model`
- `managed_lifecycle_object`
- `method_to_build_handoff_contract`
- Current `agent_architecture_record` and `tool_contract_registry`, when available.

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/environment-progression-gate.yaml`

Outputs:

- `environment_progression_gate`

## Entry Checks

- Confirm Step 18 handoff and separate implementation approval are present, approved, versioned, and cited.
- Confirm the current and target environments are authorized by the handoff, lifecycle object, architecture record, and tool registry.
- Confirm phase owner, environment owner, security owner, data owner, technical owner, AgentOps owner, support owner, and revocation owner.
- Confirm allowed users, behavior level, workflow boundary, tools, data classes, prohibited actions, and approval conditions.
- Confirm prior phase contracts are current, or record unavailable inputs as blockers.

## Scope Checks

- Confirm target environment is equal to or narrower than approved handoff and prior phase contracts.
- Confirm no production access is implied by offline validation, sandbox, pilot, or controlled rollout work.
- Confirm user groups, service accounts, roles, endpoints, data, tools, and network paths are environment-specific.
- Confirm any access expiration, promotion expiration, and post-promotion review date are explicit.
- Confirm every material change from current to target environment is documented.

## Evidence Checks

- Attach evidence for eval results, guardrail/control tests, audit-log tests, permission tests, revocation drill, access request, data owner approval, and support readiness.
- Attach evidence for secret manager configuration, runtime injection pattern, rotation cadence, emergency rotation owner, and config diff review.
- Attach evidence for data masking/synthesis, retention, deletion, prohibited fields, and cleanup on rollback.
- Attach evidence for trace dashboard, alert route, log retention, redaction, and incident route.
- Record missing evidence as a blocker, not a conditional pass.

## Phase-Specific Checks

- Define environment path across offline validation, sandbox, limited pilot, controlled rollout, production, and monitored operation as applicable.
- Define data policy: synthetic, masked, sampled, production, prohibited fields, retention, deletion, and approval evidence.
- Define secrets and configuration: vault or secret manager, runtime injection, no plaintext/local/source-control secrets, rotation, emergency rotation, config owner, and config diff review.
- Define identity and access: agent identity, service accounts, end-user roles, system roles, provisioning request IDs, least-privilege permissions, access review cadence, break-glass policy, expiration, and revocation SLA.
- Define network boundaries: allowed/prohibited hosts, private endpoints, outbound restrictions, inbound restrictions, firewall/allowlist references, tenant isolation, and environment-specific endpoints.
- Confirm observability and support readiness: traces, audit logs, dashboard, alert owner, retention, redaction, incident route, support hours, and operator runbook.
- Confirm eval and control evidence for the target environment: quality thresholds, safety thresholds, negative tests, permission tests, audit-log tests, and revocation drill.
- Define rollback: trigger conditions, owner, maximum rollback time, access revocation, secret rotation, data cleanup, user communication, validation after rollback, and fallback operating mode.

## Phase Specific Checks

This compatibility heading intentionally mirrors `## Phase-Specific Checks` for automated validators that normalize hyphens differently. The authoritative checklist items are in `## Phase-Specific Checks`.

## Blocking Conditions

- Target environment includes unapproved data, users, tools, actions, behavior level, network path, or source system.
- Secrets, test data, sandbox, access review, observability, support route, or rollback process is undefined.
- Production access is implied before production readiness gate.
- Access can persist after gate expiration, owner change, failed pilot, revocation, or rollback.
- Data cannot be safely masked, isolated, logged, retained, deleted, or cleaned up under approved constraints.
- Required owner refuses approval or requires a changed risk/control model.

## Exit Checks

- `environment_progression_gate` is complete enough for provisioning, approval, promotion, monitoring, rollback, and revocation.
- Entry criteria are marked passed, waived by authorized owner, or blocked with owner and date.
- Promotion decision, conditions, expiration, no-go conditions, post-promotion review, and monitoring window are explicit.
- Access, secrets, network, data, observability, support, rollback, and revocation plans are implementation-ready.
- Rubric criteria are passed, waived by an authorized owner, or marked blocked.
- Return-to-method triggers have been evaluated and documented.
- Next phase dependencies for eval, guardrail, sandbox, pilot, and release management are explicit.

## Failure Modes

- Secrets, test data, sandbox, or access review process is undefined.
- Production access is implied before readiness gate.
- Target environment has broader data, users, tools, network, or behavior than approved.
- Promotion lacks rollback, revocation, audit, support, or incident evidence.
- Access can persist after gate expiration, owner change, failed pilot, or rollback.

## Return-To-Method Triggers

- Approved environment path is not feasible.
- Required data cannot be safely masked, isolated, logged, or retained under the approved constraints.
- A necessary permission, system endpoint, or user population was not approved in Step 17/18.
- Risk owner requires a different control model, oversight model, or lifecycle posture.
