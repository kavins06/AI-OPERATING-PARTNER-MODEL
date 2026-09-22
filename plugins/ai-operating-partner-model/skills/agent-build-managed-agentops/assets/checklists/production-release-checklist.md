# Production Release Checklist

Use this checklist for Section 2 phase 12: `production_release`.

## Inputs

- `technical_blueprint`
- `managed_lifecycle_object`
- `risk_control_model`

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/release-version-manifest.yaml`

Outputs:

- `release_version_manifest`

## Entry Checks

- Confirm production readiness gate is approved or non-production target gate is approved.
- Confirm release owner, technical owner, business owner, security owner, AgentOps owner, support owner, and rollback owner are named.
- Confirm release target, release window, release type, semantic version, and owner coverage.
- Confirm every release condition and waiver has evidence and approver.
- Confirm release packaging remains within approved runtime, behavior, tool, source, permission, and lifecycle scope.

## Scope Checks

- Confirm release artifacts match the approved production readiness scope and target environment.
- Confirm no unapproved permission, source, tool, user group, output type, model/runtime, prompt behavior, or workflow step is packaged.
- Confirm material changes are classified correctly and routed to change review before release.
- Confirm release notes, monitoring, rollback, and support coverage reflect the actual shipped scope.

## Phase-Specific Checks

- Version every runtime-changing artifact: code, prompts, system instructions, model config, retrieval corpus/index, tool contracts, permissions, schemas, eval sets, guardrails, trace spec, dashboards, feature flags, and runbooks.
- Classify the release as initial, patch, minor, major, hotfix, or rollback and document why.
- Confirm major/material changes have completed change review before release.
- Attach blocking eval, regression, adversarial, guardrail, and trace results for this exact release candidate.
- Verify compatibility across schema versions, tool contracts, data contracts, model runtime, client environment, and migrations.
- Define deployment method, target, release window, rollout strategy, feature flags, config/secrets changes, smoke tests, and post-deploy checks.
- Define rollback triggers, previous stable version, rollback package, rollback owner, expected restore time, validation checks, and communications.
- Confirm monitoring handoff for first 24 hours, first week, alerts, dashboards, stop conditions, and owner coverage.
- Confirm release notes list user-visible changes, operator-visible changes, known risks, support contacts, and rollback contact.
- Evaluate return-to-method triggers for any packaging change that alters scope, access, risk, behavior, or lifecycle obligations.

## Evidence Checks

- Attach immutable artifact references for every included artifact.
- Attach eval/control/trace result refs for the release candidate.
- Attach deployment plan and smoke-test definitions.
- Attach rollback package and validation evidence.
- Attach monitoring handoff and support coverage evidence.
- Attach release notes and communications.
- Attach approvals and waivers.

## Exit Checks

- `release_version_manifest` is complete, approved, and tied to a production readiness gate or target-environment gate.
- Smoke tests and post-deploy checks are ready to execute.
- Rollback package can restore previous stable behavior within the required recovery window.
- First-production monitoring has live owners and alert channels.
- Return-to-method triggers have been evaluated and recorded.

## Blocking Conditions

- Release lacks versioned prompts, models, tools, schemas, eval sets, permissions, release notes, or rollback package.
- Any behavior-affecting artifact is unversioned or mutable.
- Release includes unapproved permissions, sources, tools, user groups, output types, model configs, or behavior levels.
- Blocking eval, guardrail, trace, smoke, or rollback checks are missing or failed.
- Rollback owner, previous stable version, expected restore time, or validation checks are missing.
- Monitoring owner coverage or alert routing is missing for the release window.

## Failure Modes

- Release lacks versioned prompts, models, tools, schemas, eval sets, permissions, release notes, or rollback package.

## Return-To-Method Triggers

- Release packaging changes approved runtime, tool, source, or behavior scope.
- Release packaging changes risk acceptance, lifecycle obligations, monitoring burden, owner model, or production support assumptions.
