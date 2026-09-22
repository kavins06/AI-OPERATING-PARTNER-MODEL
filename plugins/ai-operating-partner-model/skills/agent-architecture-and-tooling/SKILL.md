---
name: agent-architecture-and-tooling
description: "Translate approved handoff artifacts into implementation-grade architecture, tool, data, and identity contracts. Use after approved Step 18 handoff and separate implementation approval as part of the Section 2 build and Managed AgentOps backbone."
---

# Agent Architecture And Tooling

## Boundary

Use this skill only inside Section 2 after Step 18 handoff approval and separate implementation approval. This skill converts approved method artifacts into buildable internal delivery contracts; it does not approve a new use case, widen the first behavior, choose a new behavior level, or add new users, systems, tools, sources, write/send actions, or environments.

Stop and return to the `agent-build-managed-agentops` orchestrator when the requested work belongs to another Section 2 phase. Stop and return to the Section 1 method owner when the approved handoff is missing, contradicted, infeasible, or made materially different by the architecture or tool needs discovered here.

Never fill a missing fact with a preferred design assumption. Record it as a blocker, identify the owner who can resolve it, and name the exact downstream phase that is blocked.

## Required Inputs

Use the Section 1 to Section 2 handoff map before producing outputs:

- `../agent-build-managed-agentops/assets/mappings/section1-to-section2-handoff-map.yaml`

Required Section 1 inputs for the owned phases:

- `implementation_decision_packet`
- `organizational_intelligence_baseline`
- `risk_control_model`
- `solution_shape`
- `technical_blueprint`

Required Section 2 inputs when available:

- `agent_build_contract`
- `agent_build_plan`
- prior version of `agent_architecture_record`
- prior version of `tool_contract_registry`

Evidence requirements:

- Cite approved artifact IDs, versions, approval status, approval date, and evidence references.
- Confirm the approved first behavior, behavior level, workflow boundary, target users, prohibited behaviors, excluded sources, excluded actions, and approval conditions before drafting contracts.
- Confirm owner model coverage for business, product, technical, security, data, risk/compliance, AgentOps, support, and revocation responsibilities.

## Owned Phases

- Phase 4: Agent Architecture Spec.
- Phase 5: Tool/Data/Identity Contracts.

### Phase 4: Agent Architecture Spec

Purpose: Produce an `agent_architecture_record` that is buildable, reviewable, and constrained to the approved Step 17/18 handoff.

Section 1 inputs:

- `solution_shape`
- `technical_blueprint`
- `risk_control_model`
- `implementation_decision_packet`

Section 2 outputs:

- `agent_architecture_record`

Templates:

- `skills/agent-build-managed-agentops/assets/templates/agent-architecture-record.yaml`

Execution requirements:

- Verify all source inputs are approved and internally consistent before designing runtime topology.
- Map the approved behavior level to runtime topology, orchestration pattern, human oversight path, tool posture, and environment posture.
- Document every material component: runtime, model gateway, orchestration, retrieval, tool adapters, identity boundary, audit/trace layer, data stores, and operator controls.
- Specify data/system paths for reads, writes, retrieval, events, logs, secrets, and human approvals. Empty write paths are an intentional control and must be represented explicitly.
- State model posture: allowed/prohibited model classes, routing policy, fallback policy, prompt and retrieval sources, context minimization, output constraints, latency and cost guardrails, and privacy constraints.
- Define identity/access posture for the agent runtime, service accounts, end-user delegation, break-glass use, revocation owner, and review cadence.
- Define auditability: required event taxonomy, correlation IDs, trace retention, sensitive data redaction, and tool-call audit fields.
- Define failure behavior for invalid input, missing source data, unavailable tools, permission failures, model refusal/uncertainty, malformed output, partial success, latency breach, control violation, and cost spike.
- Define degraded mode, stop conditions, human escalation, rollback dependencies, and material change triggers.
- Record each architectural decision with options considered, rationale, consequences, approver, and evidence reference.

Failure modes:

- Runtime topology does not match approved behavior level.
- Fallback and failure behavior are undefined.
- Model/runtime posture ignores privacy, latency, cost, data residency, or audit constraints.
- Component ownership, revocation, or support responsibility is ambiguous.
- Architecture requires a tool, source, write action, identity model, or environment not approved in the handoff.

Return-to-method triggers:

- Architecture requires a different behavior level, source, user group, workflow boundary, oversight model, or business process assumption.
- The only feasible architecture needs write/send capability that was not approved.
- Required source or owner evidence from Section 1 cannot be reconciled.

### Phase 5: Tool/Data/Identity Contracts

Purpose: Produce a `tool_contract_registry` that makes every approved tool, data path, permission, identity mapping, and failure behavior explicit enough to implement and operate.

Section 1 inputs:

- `technical_blueprint`
- `organizational_intelligence_baseline`
- `risk_control_model`
- `implementation_decision_packet`

Section 2 outputs:

- `tool_contract_registry`

Templates:

- `skills/agent-build-managed-agentops/assets/templates/tool-contract-registry.yaml`

Execution requirements:

- Start from deny-by-default: every tool is disabled until registered, scoped, tested, audited, and approved.
- Register one contract per tool or connector, including read-only tools, internal APIs, MCP tools, workflow actions, databases, document stores, notification systems, and human handoff tools.
- For each tool, define owner, system of record, approved use cases, prohibited use cases, environments allowed, data classes, endpoints/actions, input schema, output schema, side effects, idempotency, rate limits, timeout, retry, and failure behavior.
- For each tool, document least-privilege permissions with explicit allow and deny scopes. Any create/update/delete/send/execute action requires a named approval policy, human approval rule, audit event, rollback or compensation plan, and revocation path.
- Document identity and access model: service account, agent identity, end-user identity, delegation rules, impersonation prohibition, token storage, token rotation, break-glass owner, access review cadence, and emergency revocation SLA.
- Document data contracts: authoritative source, field-level classification, validation, freshness, retention, lineage, redaction, transformation, and prohibited fields.
- Document auditability: run ID, user ID, agent ID, release version, tool ID, permission scope, input hash or redacted input, output hash or redacted output, decision rationale reference, approval reference, latency, status, and error code.
- Document failure behavior for validation error, permission error, unavailable service, stale data, partial success, duplicate invocation, hallucinated tool name, unexpected side effect, and downstream policy rejection.
- Attach test contract evidence: sandbox fixture, permission test, negative test, audit-log test, revocation drill, and rollback/compensation test where applicable.

Failure modes:

- Tool lacks owner, permission scope, audit logging, failure behavior, or revocation path.
- Identity mapping is ambiguous.
- Write/send action appears without explicit approval.
- Data contract lacks source-of-truth, classification, freshness, retention, validation, or prohibited-field rules.
- Tool output can drive user-visible or system side effects without a reconciliation path.

Return-to-method triggers:

- Tool requires access not approved in Step 17/18.
- Required system owner refuses or cannot provide least-privilege access.
- The approved outcome cannot be delivered without a new source, user group, workflow action, or identity assumption.

## Resource Map

- Local phase packs: `assets/phase-packs`
- `../agent-build-managed-agentops/assets/schemas/agentops-object-schemas.yaml`
- `../agent-build-managed-agentops/assets/templates/agent-architecture-record.yaml`
- `../agent-build-managed-agentops/assets/templates/tool-contract-registry.yaml`
- `../agent-build-managed-agentops/assets/checklists/agent-architecture-review-checklist.md`
- `../agent-build-managed-agentops/assets/checklists/tool-data-identity-contracts-checklist.md`
- `../agent-build-managed-agentops/assets/rubrics/agent-architecture-readiness-rubric.yaml`
- `../agent-build-managed-agentops/assets/rubrics/tool-contract-completeness-rubric.yaml`
- `../agent-build-managed-agentops/assets/validator-rules/agent_architecture_spec.yaml`
- `../agent-build-managed-agentops/assets/validator-rules/tool_data_identity_contracts.yaml`
- `../agent-build-managed-agentops/assets/examples/golden-path/04-agent-architecture-record.yaml`
- `../agent-build-managed-agentops/assets/examples/golden-path/05-tool-contract-registry.yaml`

## Workflow

1. Confirm the approved Section 1 source artifacts, versions, approvals, evidence references, and unresolved approval conditions.
2. Extract the hard boundary: approved first behavior, behavior level, users, workflow, data sources, environments, prohibited behaviors, prohibited actions, and material change triggers.
3. Build the architecture record before the tool registry. Tool contracts must trace back to architecture components and approved data/system paths.
4. For Phase 4, complete the architecture checklist, fill the architecture template, evaluate the architecture rubric, and record blockers or return-to-method triggers.
5. For Phase 5, inventory every tool and data path from the architecture, complete the tool/data/identity checklist, fill the registry template, evaluate the tool contract rubric, and record blockers or return-to-method triggers.
6. Reconcile cross-object consistency: every tool must have an architecture component or approved dependency; every write/send/execute capability must have explicit approval; every secret and identity must have an environment/access follow-up for Phase 6.
7. Mark phase status only as `approved` when evidence, owners, least privilege, auditability, failure behavior, revocation, rollback, and next-phase dependencies are complete.

## Output Contracts

- `agent_architecture_record`
- `tool_contract_registry`

Minimum acceptance for `agent_architecture_record`:

- Source inputs and approval evidence are cited.
- Runtime topology, components, data/system paths, model posture, identity posture, auditability, failure modes, rollback dependencies, and signoff are complete.
- Architecture is equal to or narrower than approved scope.

Minimum acceptance for `tool_contract_registry`:

- All tools are registered with owner, purpose, allowed/prohibited use, environments, permission scope, identity model, input/output contract, audit fields, failure behavior, revocation path, and approval state.
- No unregistered, over-scoped, unaudited, or unrevocable tool is allowed.
- Write/send/execute actions have explicit approval, human approval policy, idempotency, reconciliation, and rollback or compensation behavior.

## Quality Bar

Do not widen approved scope. Do not proceed when owner, evidence, control, approval, least privilege, auditability, failure handling, revocation, rollback, or return-to-method requirements are missing.

Implementation-grade means an engineer, security reviewer, data owner, and AgentOps operator can independently answer: what will run, where it will run, what it can access, whose identity it uses, what it can and cannot do, how every action is audited, how failures stop safely, who can revoke it, and what must happen before it moves to the next environment.
