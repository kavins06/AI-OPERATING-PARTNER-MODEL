# Section 2: Implementation / Managed AgentOps

This section starts only after the Step 18 handoff is approved and a separate implementation approval authorizes build-phase work. It converts the approved handoff into an implementation backbone for the operating intelligence platform, controlled agent build, pilot, production release, operation, change-control, incident-response, expansion, and retirement.

This is a separate post-18 build/operate track, not an extension of the discovery step sequence.

## Primary Skill

- `../skills/agent-build-managed-agentops`

## Operating Intelligence Platform

The implementation model includes a governed operating intelligence platform before or alongside agent deployment. The platform makes the approved parts of a company queryable through source inventory, canonical entities, semantic/truth definitions, document intelligence, permissions, query interfaces, audit, and monitoring.

Start with a minimum viable foundry for one workflow or domain. Do not attempt a whole-company platform on day one. The initial platform can be built as a metadata and synthetic-data scaffold during discovery, then connected to approved client data only after implementation approval.

See `intelligence-platform.md`.

## Automation

- `section2-build-spec.yaml`: source-of-truth automation spec for all 15 Section 2 phases, target support skills, required assets, checklists, rubrics, validator rules, examples, and failure/return-to-method requirements.
- `../scripts/generate-section2-backbone.py`: dry-run by default; scaffolds target support skills, checklists, rubrics, and validator-rule stubs from the spec when run with `--apply`.
- `../scripts/validate-section2-backbone.py`: validates the current Section 2 backbone. Use `--strict` to enforce the full target-state backbone and implementation-grade asset depth.

The generator is only the deterministic rebuild path. The implementation-grade backbone also requires the support skills, templates, checklists, rubrics, validator rules, examples, and docs to preserve Section 1 inputs, explicit evidence, blocking conditions, phase decisions, return-to-method triggers, and owner acceptance.

## Supporting Skills

- `../skills/agent-build-intake-and-scope`: build conversion gate, handoff freeze, agent necessity kill test, and first behavior scope.
- `../skills/agent-architecture-and-tooling`: architecture, runtime, tools, data, identity, permissions, and revocation contracts.
- `../skills/agent-environment-and-access`: environment progression, sandbox/test data, secrets, provisioning, and access review.
- `../skills/agent-evals-guardrails-observability`: evals, guardrails, control verification, trace policy, metrics, dashboards, and alerts.
- `../skills/agent-sandbox-pilot-readiness`: sandbox evidence, controlled pilot launch, and production readiness gates.
- `../skills/agent-release-management`: release versioning, deployment record, compatibility, and rollback package.
- `../skills/managed-agentops-operations`: live operating record, metrics review, source freshness, incidents, access review, and value tracking.
- `../skills/agent-change-expansion-retirement`: material change, expansion, remediation, rollback, retirement, and redesign decisions.

## What It Contains

- Operating intelligence platform concept.
- Platform readiness gate.
- Minimum viable foundry scope.
- Build conversion gate.
- Agent necessity kill test.
- First behavior scope.
- Agent architecture record.
- Tool, data, and identity contracts.
- Environment and access progression.
- Eval harness and guardrail design.
- Sandbox prototype controls.
- Security and control review.
- Controlled pilot.
- Production readiness gate and readiness scoring.
- Production release manifest.
- Managed AgentOps operating record.
- Expansion/change-control review.
- Retirement or redesign loop.

## Key Outputs

- `agent_build_contract`
- `agent_necessity_kill_test`
- `agent_build_plan`
- `agent_architecture_record`
- `tool_contract_registry`
- `eval_harness_spec`
- `guardrail_control_matrix`
- `trace_observability_spec`
- `environment_progression_gate`
- `release_version_manifest`
- `pilot_launch_gate`
- `production_readiness_gate`
- `agentops_operating_record`
- `change_expansion_retirement_review`

Human-readable support files:

- `incident-revocation-runbook.md`
- `internal-operator-run-card.md`

## Key Files

- `../skills/agent-build-managed-agentops/SKILL.md`
- `section2-build-spec.yaml`
- `../skills/agent-build-managed-agentops/assets/templates`
- `../skills/agent-build-managed-agentops/assets/schemas/agentops-object-schemas.yaml`
- `../skills/agent-build-managed-agentops/assets/mappings/section1-to-section2-handoff-map.yaml`
- `../skills/agent-build-managed-agentops/assets/examples/golden-path-revenue-intake.yaml`
- `../skills/agent-build-managed-agentops/references/phase-cadence-guide.md`
- `../docs/section1-to-section2-data-map.md`
- `../skills/agent-build-managed-agentops/scripts/validate_agentops_contracts.py`
- `../skills/agent-build-managed-agentops/scripts/score_agentops_readiness.py`

## Required Inputs

- Approved Step 17 implementation decision packet or packet set.
- Approved Step 18 managed lifecycle object or lifecycle set.
- Step 18 method-to-build handoff contract.
- Separate implementation approval naming scope, owners, environments, access limits, budget, and timebox.

## Implementation-Grade Standard

Each Section 2 phase must be usable by a delivery operator without undocumented context. That means every phase asset must specify:

- Approved Section 1 inputs by source object and evidence reference.
- Scope limits and non-goals carried forward from Step 17/18.
- Required output contracts and downstream consumers.
- Phase-specific checks, blocking conditions, and exit decision.
- Rubric criteria with evidence requirements and pass conditions.
- Validator-rule checks for source input coverage, scope preservation, owners, evidence, blockers, output completeness, and return-to-method triggers.
- Golden-path examples showing what a complete handoff looks like.

No phase should pass because a demo works. It passes only when the evidence package can survive independent review.
