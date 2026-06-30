---
name: agent-release-management
description: "Version, package, approve, release, monitor, and roll back approved agent artifacts for Section 2 phase 12, including prompts, models, tools, schemas, eval sets, guardrails, trace specs, permissions, release notes, smoke tests, feature flags, deployment evidence, rollback package, and production monitoring handoff. Use after approved Step 18 handoff and separate implementation approval as part of the Section 2 build and Managed AgentOps backbone."
---

# Agent Release Management

## Boundary

Use this skill only inside Section 2 after Step 18 handoff approval and separate implementation approval. Do not backfill missing Section 1 decisions here.

Own only:

- Phase 12: Production Release.

Stop and return to the `agent-build-managed-agentops` orchestrator when the request requires earlier phase artifacts, live operations, change expansion, incident response outside release, retirement, or other phases outside this skill.

Stop and return to the Section 1 method owner when release packaging changes the approved runtime, model posture, tool access, data path, behavior level, user group, output type, oversight model, or lifecycle obligations.

## Required Inputs

Read the handoff map before producing outputs:

- `../agent-build-managed-agentops/assets/mappings/section1-to-section2-handoff-map.yaml`

Use these Section 1 inputs:

- `managed_lifecycle_object`
- `risk_control_model`
- `technical_blueprint`

Require these Section 2 artifacts before release approval:

- `agent_build_contract`
- `agent_architecture_record`
- `tool_contract_registry`
- `eval_harness_spec`
- `guardrail_control_matrix`
- `trace_observability_spec`
- `pilot_launch_gate`
- `production_readiness_gate`

## Owned Phases

- Phase 12: Production Release.

## Resource Map

- Local phase packs: `assets/phase-packs`
- Template:
  - `../agent-build-managed-agentops/assets/templates/release-version-manifest.yaml`
- Checklist:
  - `../agent-build-managed-agentops/assets/checklists/production-release-checklist.md`
- Rubric:
  - `../agent-build-managed-agentops/assets/rubrics/release-management-rubric.yaml`
- Validator rules:
  - `../agent-build-managed-agentops/assets/validator-rules/production_release.yaml`
- Example:
  - `../agent-build-managed-agentops/assets/examples/golden-path/12-release-version-manifest.yaml`

## Workflow

1. Confirm the production readiness gate is approved and that every release condition has evidence or an owner-approved waiver.
2. Assign a semantic release version and classify release type: initial, patch, minor, major, hotfix, or rollback.
3. Package immutable artifact references: code commit, prompt/instruction versions, model configuration, retrieval corpus, tool contracts, schemas, eval sets, eval results, guardrail matrix, trace spec, runbooks, and operator/user communications.
4. Confirm compatibility: schema versions, tool contract versions, data contracts, environment requirements, feature flags, migrations, and known incompatibilities.
5. Define deployment plan: target environment, release window, rollout strategy, flags, config/secrets changes, smoke tests, post-deploy checks, monitoring window, and owner coverage.
6. Define rollback package: previous stable version, rollback trigger thresholds, rollback steps, owner, expected restore time, validation checks, data/state handling, and communications.
7. Confirm release controls: no unversioned artifact, no unapproved permission, no untested smoke check, no missing rollback path, no missing monitoring handoff.
8. Produce or update `release_version_manifest`, complete the checklist, apply the rubric, and record go/no-go decision with approvals.

## Release Manifest Rules

The manifest must version or cite every artifact that can change runtime behavior:

- runtime code
- prompts and system instructions
- model/provider configuration
- retrieval corpora and indexes
- tool contracts and permissions
- schemas and parsers
- eval datasets and thresholds
- guardrails and control policy
- trace and dashboard configuration
- feature flags and environment config
- runbooks, communications, and training artifacts

Block release when:

- Any behavior-affecting artifact is missing an immutable reference or version.
- Production deployment contains a permission, tool, data source, user group, output type, model, prompt, or behavior not approved by prior gates.
- Rollback cannot restore previous stable behavior within the required recovery window.
- Smoke tests, post-deploy checks, monitoring alerts, or owner coverage are missing.
- Release notes omit known risks, conditions, support contacts, or material changes.

Return to method when:

- Packaging introduces a material change to approved scope, runtime posture, tool/data/identity contracts, risk acceptance, or lifecycle obligations.

## Output Contracts

- `release_version_manifest`

Use the template as a machine-readable contract. Preserve additional local fields if they strengthen release evidence and remain compatible with the shared schema.

## Quality Bar

Do not approve release until every runtime-changing artifact is versioned, every control and eval result is attached, every permission is traced to approval, rollback is tested, smoke tests are named, and first-production monitoring has a live owner.
