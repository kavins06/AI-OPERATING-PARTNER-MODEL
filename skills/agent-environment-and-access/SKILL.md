---
name: agent-environment-and-access
description: "Control environment progression, test data, secrets, provisioning, access review, and rollback readiness. Use after approved Step 18 handoff and separate implementation approval as part of the Section 2 build and Managed AgentOps backbone."
---

# Agent Environment And Access

## Boundary

Use this skill only inside Section 2 after Step 18 handoff approval and separate implementation approval. This skill prepares the environment/access gate for the approved first behavior; it does not approve production launch, bypass security review, create permanent access without owner approval, or authorize new tools, users, data sources, behavior levels, write/send actions, or environments.

Stop and return to the `agent-build-managed-agentops` orchestrator when the requested work belongs to another Section 2 phase. Stop and return to the Section 1 method owner when the approved environment path is infeasible or requires a changed scope, source, tool, user population, operating assumption, or risk acceptance.

No production access is implied by sandbox or pilot work. Every environment promotion requires an explicit gate record, evidence, rollback path, and owner approval.

## Required Inputs

Use the Section 1 to Section 2 handoff map before producing outputs:

- `../agent-build-managed-agentops/assets/mappings/section1-to-section2-handoff-map.yaml`

Required Section 1 inputs for the owned phase:

- `managed_lifecycle_object`
- `method_to_build_handoff_contract`
- `risk_control_model`
- `technical_blueprint`

Required Section 2 inputs when available:

- `agent_build_contract`
- `agent_architecture_record`
- `tool_contract_registry`
- `eval_harness_spec`
- `guardrail_control_matrix`
- `trace_observability_spec`
- `release_version_manifest`

Evidence requirements:

- Cite approved artifact IDs, versions, approval status, approval date, and evidence references.
- Confirm the current environment, target environment, approved behavior level, allowed users, allowed data classes, allowed tools, prohibited actions, and approval conditions.
- Confirm business, technical, security, data, risk/compliance, AgentOps, support, and revocation owners for the promotion.

## Owned Phases

- Phase 6: Environment And Access Setup.

### Phase 6: Environment And Access Setup

Purpose: Produce an `environment_progression_gate` that proves the agent can move from one environment to the next with correct access, data handling, secrets, observability, rollback, and support controls.

Section 1 inputs:

- `technical_blueprint`
- `risk_control_model`
- `managed_lifecycle_object`
- `method_to_build_handoff_contract`

Section 2 outputs:

- `environment_progression_gate`

Templates:

- `skills/agent-build-managed-agentops/assets/templates/environment-progression-gate.yaml`

Execution requirements:

- Verify that the target environment is authorized by the handoff, architecture record, tool registry, and lifecycle object.
- Inventory each environment in the progression path: offline validation, sandbox, limited pilot, controlled rollout, production, and monitored operation where applicable.
- Define data policy for each environment: synthetic, masked, sampled, production, prohibited fields, retention, deletion, and approval evidence.
- Define secrets and configuration posture: vault or secret manager, runtime injection, no local/plaintext secrets, rotation cadence, owner, emergency rotation, config diff review, and secret revocation.
- Define identity and access: agent identity, service accounts, end-user roles, system roles, least-privilege permissions, provisioning workflow, access request IDs, access review cadence, break-glass conditions, and revocation SLA.
- Define network and system boundaries: allowed hosts, private endpoints, outbound restrictions, firewall or allowlist requirements, tenant/workspace isolation, and environment-specific endpoints.
- Confirm observability and audit readiness before promotion: traces, audit logs, dashboard, alert owner, log retention, redaction, and incident route.
- Confirm eval and guardrail evidence required for the target environment: quality thresholds, control tests, negative tests, permission tests, audit tests, and revocation drill.
- Define promotion criteria, no-go criteria, approval conditions, expiration date, and post-promotion monitoring window.
- Define rollback plan: trigger conditions, rollback owner, steps, data cleanup, secret revocation, user communication, validation after rollback, and maximum rollback time.

Failure modes:

- Secrets, test data, sandbox, or access review process is undefined.
- Production access is implied before readiness gate.
- Target environment has broader data, users, tools, network, or behavior than approved.
- Promotion lacks rollback, revocation, audit, support, or incident evidence.
- Access can persist after gate expiration, owner change, failed pilot, or rollback.

Return-to-method triggers:

- Approved environment path is not feasible.
- Required data cannot be safely masked, isolated, logged, or retained under the approved constraints.
- A necessary permission, system endpoint, or user population was not approved in Step 17/18.
- Risk owner requires a different control model, oversight model, or lifecycle posture.

## Resource Map

- Local phase packs: `assets/phase-packs`
- `../agent-build-managed-agentops/assets/schemas/agentops-object-schemas.yaml`
- `../agent-build-managed-agentops/assets/templates/environment-progression-gate.yaml`
- `../agent-build-managed-agentops/assets/checklists/environment-access-checklist.md`
- `../agent-build-managed-agentops/assets/rubrics/environment-access-readiness-rubric.yaml`
- `../agent-build-managed-agentops/assets/validator-rules/environment_and_access_setup.yaml`
- `../agent-build-managed-agentops/assets/examples/golden-path/06-environment-progression-gate.yaml`

## Workflow

1. Confirm approved source artifacts, versions, approvals, evidence references, and unresolved approval conditions.
2. Extract the hard boundary: current and target environments, behavior level, users, workflow, tools, data classes, prohibited actions, and material change triggers.
3. Reconcile the architecture record and tool registry with the target environment. Every tool, secret, identity, data path, and audit event must have an environment-specific implementation path.
4. Inventory environment differences, including data posture, endpoints, credentials, permissions, network access, logging, alert routing, and support coverage.
5. Complete the environment/access checklist and fill the environment progression gate.
6. Evaluate the rubric. Treat missing secrets posture, missing access owner, missing revocation path, missing rollback test, missing audit evidence, or unapproved production access as blocking.
7. Record promotion decision, conditions, expiration date, rollback plan, post-promotion monitoring, and return-to-method triggers.
8. Do not mark the gate approved until required evidence is attached and owners accept the promotion risk.

## Output Contracts

- `environment_progression_gate`

Minimum acceptance for `environment_progression_gate`:

- Source inputs and approval evidence are cited.
- Environment scope, data policy, access model, secrets posture, network boundaries, eval/control evidence, observability, support, rollback, revocation, approval, and expiration are complete.
- Target environment is equal to or narrower than the approved handoff and prior phase contracts.

## Quality Bar

Do not widen approved scope. Do not proceed when owner, evidence, control, approval, least privilege, auditability, secrets handling, access review, revocation, rollback, or return-to-method requirements are missing.

Implementation-grade means an engineer can provision it, a security/data owner can approve it, an AgentOps operator can monitor and revoke it, and a support owner can recover safely when promotion fails.
