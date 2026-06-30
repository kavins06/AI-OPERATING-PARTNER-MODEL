---
name: agent-build-managed-agentops
description: "Run the post-18 agent build and Managed AgentOps backbone after an AI operating partner engagement has completed Step 18, the Step 17 implementation decision packet and Step 18 managed lifecycle or lifecycle_set are approved, the method-to-build handoff is accepted, and a separate implementation approval authorizes build-phase work. Consumes approved handoff artifacts and produces build, validation, pilot, launch, operation, change-control, incident, expansion, and retirement contracts without changing the Step 0-18 method."
---

# Agent Build Managed AgentOps

## Core Boundary

Use this skill only after Step 18 is complete and separately approved implementation work has begun.

Do not use this skill to create another engagement step. Step 18 remains the handoff boundary for the AI operating partner method. This skill starts a post-18 build/operate track only when the client or sponsor has approved a separate implementation phase.

Do not infer approval from a build-ready recommendation. A Step 17 packet and Step 18 lifecycle object can say what may be built; the build phase starts only when the required implementation approvers explicitly authorize it.

## Required Inputs

Start only when the following approved artifacts exist:

- Step 17 `implementation_decision_packet` or `packet_set`.
- Step 18 `managed_lifecycle_object` or `lifecycle_set`.
- Step 18 method-to-build handoff contract.
- Implementation approval naming the approved scope, owner forum, build owner, technical owner, security/risk approvers, environments, access limits, and budget/timebox.

If any input is missing, stop and request the missing approval or artifact. Do not backfill missing Step 17/18 decisions in this skill; return to the method engagement owner.

## Skill Role

Convert the approved Step 17/18 handoff into build/operate contracts for implementation teams and Managed AgentOps owners.

Use Section 2 support skills for specialized slices as they become available:

- `agent-build-intake-and-scope`: phases 1-3, covering build conversion gate, agent necessity kill test, and first behavior scope.
- `agent-architecture-and-tooling`: phases 4-5, covering architecture, tools, data, identity, permissions, audit, and revocation contracts.
- `agent-environment-and-access`: phase 6, covering environment progression, sandbox/test data, secrets, provisioning, access review, and rollback readiness.
- `agent-evals-guardrails-observability`: phases 7 and 9, covering eval design, guardrails, security/control verification, trace policy, dashboards, metrics, and alerts.
- `agent-sandbox-pilot-readiness`: phases 8, 10, and 11, covering sandbox prototype evidence, controlled pilot launch, and production readiness gate.
- `agent-release-management`: phase 12, covering release versioning, deployment notes, compatibility, and rollback package.
- `managed-agentops-operations`: phase 13, covering live operations, metrics, source freshness, incidents, access review, guidance updates, and value tracking.
- `agent-change-expansion-retirement`: phases 14-15, covering material change, expansion, rollback, remediation, retirement, and redesign decisions.

Produce contracts that preserve:

- Approved first behavior and excluded behaviors.
- Tool, data, identity, environment, security, eval, launch, monitoring, incident, revocation, expansion, and retirement boundaries.
- Evidence references and owner decisions from the handoff.
- Return-to-method triggers when build learning changes readiness, risk, truth, value, solution shape, or lifecycle assumptions.

## Operating Procedure

For each phase:

1. Load the handoff map and confirm the required Section 1 inputs are approved, versioned, and cited.
2. Confirm the phase scope is equal to or narrower than the Step 17/18 approved first behavior and lifecycle scope.
3. Use the phase support skill, checklist, template, rubric, validator rule group, and golden-path example.
4. Complete the machine-readable output contract with source inputs, owners, evidence references, blockers, and exit decision.
5. Mark every known failure mode as mitigated, accepted by an authorized owner, blocked, or returned to method.
6. Stop when a required approval, owner, source, control, trace, eval, rollback, revocation, or monitoring path is missing.
7. Route to phase 14 before implementing any material expansion.

Do not rely on prose summary alone. The output of a phase must be consumable by the next phase as structured evidence.

## Post-18 Phases

Run the phases in order. Each phase should produce a short machine-readable contract or update a consolidated build/operate contract set.

1. Build Conversion Gate: Confirm Step 17/18 approval, separate implementation authorization, funding/timebox, named owners, permitted environments, and exact handoff version.
2. Agent Necessity Check: Reconfirm that an agent is necessary; prefer a simpler workflow, report, rule, automation, or human process when it satisfies the approved outcome with less risk.
3. First Behavior Scope: Lock the smallest approved behavior level, user group, workflow slice, source set, output contract, human review path, non-goals, and prohibited behaviors.
4. Agent Architecture Spec: Translate the approved solution shape into runtime, orchestration, retrieval, state, queue, model abstraction, logging, observability, fallback, and failure-behavior contracts.
5. Tool/Data/Identity Contracts: Define each tool, connector, MCP, retrieval index, normalization job, document/email scope, identity mapping, permission, input/output schema, allowed action, prohibited action, and audit requirement.
6. Environment And Access Setup: Define dev, sandbox, staging, pilot, and production environments; provisioning owners; secrets handling; data minimization; approved test data; network boundaries; and access review.
7. Eval And Guardrail Design: Convert Step 10 evals and Step 15 controls into build-phase tests, regression suites, permission tests, output-quality checks, source-grounding checks, abuse cases, and release thresholds.
8. Sandbox Prototype: Build only inside approved sandbox boundaries using approved synthetic, redacted, or historical data; record deviations, missing contracts, failing evals, and required method re-entry.
9. Security And Control Review: Verify identity, data handling, tool permissions, audit logs, human approval, output controls, incident paths, revocation, vendor/cloud posture, and residual-risk acceptance.
10. Controlled Pilot: Release to the approved pilot audience and workflow slice with monitoring, support, feedback capture, human review, rollback, stop conditions, and sponsor review cadence.
11. Production Readiness Gate: Confirm eval pass rates, pilot evidence, risk acceptance, support readiness, monitoring thresholds, cost envelope, source freshness, owner coverage, incident rehearsal, and revocation readiness.
12. Production Release: Release only the approved behavior, users, sources, tools, and environments; record version, approvals, runbook, rollback plan, training state, and launch communication.
13. Managed AgentOps: Operate the released capability through quality, business, risk, security, cost, adoption, source freshness, truth-production, feedback, incident, access-review, guidance-update, and model/runtime review loops.
14. Expansion/Change-Control Gate: Require explicit approval, readiness reassessment, updated contracts, and Step 17/18 alignment before adding users, sources, tools, write/send actions, behavior levels, workflows, models, or environments.
15. Retirement Or Redesign Loop: Retire, pause, redesign, or return to the method when value, usage, correction rate, source reliability, controls, risk, ownership, or strategic fit no longer supports operation.

## Resource Map

Read these references when needed:

- `references/source-grounded-research.md`: standards, governance, identity, risk, and legal-routing source map.
- `references/agent-engineering-quality-bar.md`: engineering requirements for architecture, tools, evals, traces, guardrails, release, and rollback.
- `references/behavior-level-launch-bars.md`: launch bars by behavior level.
- `references/phase-cadence-guide.md`: default timeboxes, review cadence, and exit evidence for the 15 post-18 phases.
- `assets/mappings/section1-to-section2-handoff-map.yaml`: machine-readable map from Section 1 collected/approved data to Section 2 contracts.
- `../../02-implementation-managed-agentops/section2-build-spec.yaml`: automation spec for target support skills, phase assets, rubrics, checklists, validator rules, examples, and failure handling.

Use these canonical assets:

- `assets/templates/TEMPLATE_INDEX.md`
- `assets/schemas/agentops-object-schemas.yaml`
- `assets/mappings/section1-to-section2-handoff-map.yaml`
- `assets/templates/build-intake-contract.yaml`
- `assets/templates/agent-necessity-kill-test.yaml`
- `assets/templates/agent-build-plan.yaml`
- `assets/templates/agent-architecture-record.yaml`
- `assets/templates/tool-contract-registry.yaml`
- `assets/templates/eval-and-validation-plan.yaml`
- `assets/templates/guardrail-control-matrix.yaml`
- `assets/templates/trace-observability-spec.yaml`
- `assets/templates/environment-progression-gate.yaml`
- `assets/templates/release-version-manifest.yaml`
- `assets/templates/pilot-launch-gate.yaml`
- `assets/templates/production-readiness-gate.yaml`
- `assets/templates/agentops-operating-record.yaml`
- `assets/templates/incident-revocation-runbook.md`
- `assets/templates/internal-operator-run-card.md`
- `assets/templates/change-expansion-retirement-review.yaml`

Use `scripts/validate_agentops_contracts.py` to check the post-18 templates, schema, examples, and golden-path packet. Use `../../scripts/validate-section2-backbone.py` to check the Section 2 automation spec. Use `scripts/score_agentops_readiness.py` to score a production readiness gate or golden-path packet before launch approval.

Validation expectation:

- `../../scripts/validate-section2-backbone.py --strict` confirms support skills, phase assets, examples, and implementation-grade asset depth.
- `scripts/validate_agentops_contracts.py` confirms templates, schemas, examples, handoff map, phase assets, rubrics, and validator rules.
- `scripts/score_agentops_readiness.py` is a readiness signal, not an approval substitute.

## Output Contracts

Produce a build/operate contract set. Use YAML or JSON when the user does not specify a format.

Include:

- `agent_build_contract`: Step 17/18 handoff IDs, separate implementation approval, owners, scope, exclusions, acceptance contract, and change-control triggers.
- `agent_necessity_kill_test`: explicit proof that an agent is still the narrowest justified implementation path, with simpler alternatives rejected or selected.
- `agent_build_plan`: delivery model, workstreams, milestones, dependencies, risks, and definition of done.
- `agent_architecture_record`: topology, model/runtime posture, retrieval/context, state/memory, fallback, and architectural decisions.
- `tool_contract_registry`: per-tool schema, permission, identity, auth, data, audit, failure, rollback, and revocation contract.
- `eval_harness_spec`: golden, synthetic, adversarial, regression, pilot, and production-derived eval suites with pass thresholds.
- `guardrail_control_matrix`: preventive, detective, corrective, approval, and revocation controls mapped to risks.
- `trace_observability_spec`: run traces, event taxonomy, redaction, retention, dashboards, alerts, cost, latency, and audit evidence.
- `environment_progression_gate`: offline, sandbox, pilot, production, rollback, and expansion promotion evidence.
- `release_version_manifest`: versioned prompts, models, tools, schemas, retrieval corpus, eval set, runtime config, permissions, release notes, and rollback package.
- `pilot_launch_gate`: pilot audience, launch criteria, support model, monitoring, feedback, stop conditions, and decision cadence.
- `production_readiness_gate`: release gates, signoffs, residual risks, support readiness, owner coverage, monitoring, incident rehearsal, and revocation readiness.
- `agentops_operating_record`: live operating record for quality, value, risk, security, cost, adoption, source freshness, incidents, access review, and change history.
- `incident-revocation-runbook.md`: human-readable incident triage, pause, revoke, rollback, communication, recovery, and post-incident process.
- `internal-operator-run-card.md`: one-page operator view of current release, owners, checks, stop conditions, and escalation path.
- `change_expansion_retirement_review`: expansion, material change, rollback, remediation, retirement, or redesign decision record.

## Return-To-Method Triggers

Return to the AI operating partner method owner instead of pushing through implementation when build learning changes or invalidates:

- The approved first behavior, behavior level, workflow boundary, user group, or value case.
- Source, truth-production, data quality, identity-resolution, or access assumptions.
- Risk/control posture, regulated-domain interpretation, approval model, or security architecture.
- Guidance/eval requirements, output contract, or human oversight model.
- Lifecycle owners, operating cadence, expansion rules, retirement criteria, or revocation path.

## Quality Bar

Do not let implementation convenience widen scope. Every new source, tool, user group, action type, output type, model/runtime, environment, or workflow step requires change-control approval and contract updates.

Do not ship without named owners for monitoring, incident response, revocation, source freshness, guidance updates, feedback triage, access review, security review, support, adoption, and value tracking.

Do not treat sandbox success as production readiness. Production release requires pilot evidence, owner signoff, control verification, support readiness, revocation readiness, and accepted residual risk.
