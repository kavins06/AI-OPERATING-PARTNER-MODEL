# Eval And Guardrail Design Checklist

Use this checklist for Section 2 phase 7: `eval_and_guardrail_design`.

## Inputs

- `ai_guidance_pack`
- `measurement_intelligence`
- `risk_control_model`
- `readiness_object`
- `managed_lifecycle_object`

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/eval-and-validation-plan.yaml`
- `skills/agent-build-managed-agentops/assets/templates/guardrail-control-matrix.yaml`

Outputs:

- `eval_harness_spec`
- `guardrail_control_matrix`

## Entry Checks

- Confirm every required Section 1 input is approved, versioned, and cited.
- Confirm Step 18 handoff and separate implementation approval are still valid.
- Confirm approved first behavior, behavior level, users, workflow boundary, sources, tools, environments, and exclusions.
- Confirm phase owner, business approver, security/risk reviewer, AgentOps owner, and evidence location.
- Confirm tool/data/identity contracts are available or explicitly blocked before eval/guardrail design.

## Scope Checks

- Confirm evals and controls cover only the approved first behavior and authorized behavior level.
- Confirm user groups, workflow boundaries, sources, tools, environments, data classes, and output types match the Step 17/18 handoff.
- Confirm excluded sources, excluded users, prohibited behaviors, write/send actions, and expansion paths remain explicit.
- Confirm any requested wider coverage is routed to change review or return-to-method before being included.

## Phase-Specific Checks

- Define behavior-level eval coverage for golden, edge, adversarial, regression, source-truth, permission-boundary, and human-review cases.
- Include realistic task cases for the approved first behavior, not generic model-quality prompts.
- Include adversarial cases for prompt injection, instruction override, source manipulation, data exfiltration, unauthorized tool use, unsupported write/send action, and social-pressure escalation.
- Set minimum sample sizes, reviewer roles, scoring rubric, calibration method, and pass/fail thresholds for every eval suite.
- Mark zero-tolerance metrics as blocking: control violation, unauthorized tool call, human-review bypass, sensitive data exposure, untraced run, and successful prompt injection.
- Tie every guidance rule, prohibited behavior, risk, tool permission, data class, and source freshness rule to at least one eval or control.
- Map each material risk to preventive, detective, corrective, revocation, and human-review controls where applicable.
- Define default fail behavior for missing source, stale source, ambiguous input, unregistered tool, unknown user, trace failure, and control failure.
- Attach evidence requirements for eval datasets, redaction, automated results, expert review, failed cases, and owner approval.
- Evaluate return-to-method triggers for missing knowledge, unstable truth production, changed behavior level, or scope assumptions.

## Evidence Checks

- Attach dataset inventory with provenance, owner, redaction status, and allowed environments.
- Attach eval result references by suite, including failed-case logs and remediation decisions.
- Attach control-test evidence for each prohibited behavior and permission boundary.
- Attach reviewer calibration notes and adjudication rules for expert review.
- Record missing evidence, unresolved failures, and unowned controls as blockers.

## Exit Checks

- `eval_harness_spec` and `guardrail_control_matrix` are complete enough for sandbox implementation and security review.
- Every blocking threshold has owner approval.
- Every eval suite has a minimum sample size and evidence source.
- Every control has owner, test method, pass criteria, fail behavior, and evidence requirement.
- Promotion criteria from offline to sandbox, sandbox to pilot, and pilot to production are explicit.
- Return-to-method triggers have been evaluated and recorded.

## Blocking Conditions

- Any approved behavior lacks golden, edge, adversarial, and regression coverage.
- Any prohibited behavior lacks a blocking eval or fail-closed control.
- Any write, send, export, privileged action, or external communication path appears without explicit approval.
- Blocking thresholds, sample sizes, reviewer roles, owners, or evidence references are missing.
- Eval data provenance or redaction status is unknown.
- Any successful prompt injection, unauthorized tool call, human-review bypass, sensitive data exposure, or untraced run remains unresolved.

## Failure Modes

- Eval suite does not cover guidance, edge cases, risks, prohibited behaviors, and permissions.
- Blocking thresholds are missing.

## Return-To-Method Triggers

- Required evals reveal missing knowledge or unstable truth production.
- Eval design changes approved scope, behavior level, source truth, risk, value, or oversight assumptions.
