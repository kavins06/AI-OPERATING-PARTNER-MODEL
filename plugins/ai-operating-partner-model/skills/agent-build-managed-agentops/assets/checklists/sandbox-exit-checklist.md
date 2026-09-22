# Sandbox Prototype Checklist

Use this checklist for Section 2 phase 8: `sandbox_prototype`.

## Inputs

- `technical_blueprint`
- `ai_guidance_pack`
- `risk_control_model`
- `method_to_build_handoff_contract`

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/environment-progression-gate.yaml`
- `skills/agent-build-managed-agentops/assets/templates/release-version-manifest.yaml`

Outputs:

- `environment_progression_gate`
- `release_version_manifest`

## Entry Checks

- Confirm sandbox environment, test data, secrets, identity, and tool access are isolated from production.
- Confirm Step 18 handoff, separate implementation approval, and sandbox scope are still valid.
- Confirm eval, guardrail, trace, tool, and architecture artifacts are available for sandbox testing.
- Confirm phase owner, technical reviewer, security reviewer, AgentOps owner, and evidence location.
- Confirm production access, live customer action, external send, write action, and expansion remain prohibited unless explicitly approved.

## Scope Checks

- Confirm sandbox run scope is equal to or narrower than the approved first behavior and lifecycle scope.
- Confirm sandbox tools, sources, users, test data, environments, and outputs match the approved sandbox boundary.
- Confirm production credentials, live writes, external sends, and customer-facing outputs are absent unless explicitly approved.
- Confirm any prototype deviation that changes scope is blocked pending owner decision and return-to-method assessment.

## Phase-Specific Checks

- Record sandbox build version, code refs, prompt/model/tool versions, retrieval corpus, schemas, and config.
- Prove test data provenance, redaction, synthetic/live-data status, and allowed environments.
- Run golden, edge, adversarial, permission-boundary, source-truth, and regression eval suites in sandbox or offline as required.
- Capture representative run traces for successful, failed, blocked, escalated, and human-reviewed cases.
- Test registered tool success paths and denied paths for unregistered, write/send, export, unauthorized identity, and environment mismatch.
- Record prototype deviations from architecture, tool contracts, eval plans, controls, or handoff assumptions.
- Attach defect log with severity, owner, remediation, retest evidence, and pilot impact.
- Test pause, feature disablement, credential/tool revocation, and rollback to previous sandbox build.
- Confirm sandbox success is framed as evidence for pilot readiness, not production readiness.
- Evaluate return-to-method triggers for changed scope, risk, truth, value, or feasibility assumptions.

## Evidence Checks

- Attach sandbox run report with counts by scenario, suite, and outcome.
- Attach eval/adversarial/control result references.
- Attach trace samples and trace completeness report.
- Attach tool invocation and tool denial logs.
- Attach deviation and defect logs.
- Attach rollback and revocation validation evidence.
- Attach owner decision for sandbox exit or blocker.

## Exit Checks

- `environment_progression_gate` records sandbox outcome and next-gate decision.
- `release_version_manifest` captures the sandbox release candidate and rollback package.
- All blocking eval/control/trace/tool tests pass or are blocked with named remediation.
- Pilot dependencies, user roster needs, monitoring needs, and unresolved risks are explicit.
- Return-to-method triggers have been evaluated and recorded.

## Blocking Conditions

- Sandbox uses unapproved data, unapproved access, production secrets, or unregistered tools.
- Any blocking eval, adversarial, permission, control, trace, or rollback test fails without remediation and retest.
- Prototype deviations are undocumented or lack owner decision.
- Defects lack severity, owner, due date, or pilot impact.
- Runs cannot be traced by version, source, tool call, control decision, and output.
- Sandbox evidence is used to imply production readiness.

## Failure Modes

- Sandbox uses unapproved data or access.
- Prototype deviations are not recorded.
- Sandbox success is treated as production readiness.

## Return-To-Method Triggers

- Sandbox learning changes approved scope, risk, truth, or value assumptions.
- Sandbox feasibility requires different behavior level, source, tool, access, oversight, or lifecycle model.
