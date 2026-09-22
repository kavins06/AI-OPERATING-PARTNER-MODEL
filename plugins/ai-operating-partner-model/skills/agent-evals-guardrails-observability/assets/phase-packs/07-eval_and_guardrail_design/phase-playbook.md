# Phase 7: Eval And Guardrail Design

Local phase pack for `eval_and_guardrail_design`. Use this file from the owning support skill folder; use the referenced central assets as the source of truth for executable templates, rubrics, validator rules, and examples.

## Required Inputs

- `ai_guidance_pack`
- `measurement_intelligence`
- `risk_control_model`
- `readiness_object`
- `managed_lifecycle_object`

## Required Outputs

- `eval_harness_spec`
- `guardrail_control_matrix`

## Canonical Assets

Templates:

- `skills/agent-build-managed-agentops/assets/templates/eval-and-validation-plan.yaml`
- `skills/agent-build-managed-agentops/assets/templates/guardrail-control-matrix.yaml`

- Checklist: `skills/agent-build-managed-agentops/assets/checklists/eval-guardrail-design-checklist.md`
- Rubric: `skills/agent-build-managed-agentops/assets/rubrics/eval-guardrail-launch-rubric.yaml`
- Validator rule: `skills/agent-build-managed-agentops/assets/validator-rules/eval_and_guardrail_design.yaml`
- Golden-path example: `skills/agent-build-managed-agentops/assets/examples/golden-path/07-eval-harness-and-guardrails.yaml`

## Operating Steps

1. Confirm each required Section 1 input is approved, versioned, and cited by object ID.
2. Confirm the phase is still inside the approved Step 17/18 first behavior and lifecycle scope.
3. Complete the canonical template fields that this phase owns.
4. Complete the checklist and attach evidence for every material claim.
5. Apply the rubric and record pass, conditional, blocked, stop, or return-to-method.
6. Run or apply the validator rule group for this phase.
7. Record the downstream fields the next phase must consume.

## Blocking Conditions

- Required source input, approval, owner, evidence reference, or decision forum is missing.
- Scope is wider than the approved handoff and no change review has approved it.
- A required control, trace, eval, rollback, revocation, monitoring, or support path is absent.
- A high-impact, regulated, write, send, export, privileged, or autonomous action appears without explicit approval.
- The phase output cannot be consumed by the next phase without undocumented assumptions.

## Failure Modes

- Eval suite does not cover guidance, edge cases, risks, prohibited behaviors, and permissions.
- Blocking thresholds are missing.

## Return-To-Method Triggers

- Required evals reveal missing knowledge or unstable truth production.

## Exit Evidence

- Source input IDs and evidence references.
- Completed output object IDs or blocked output decision.
- Checklist result.
- Rubric result.
- Validator result.
- Owner signoff or blocker owner.
- Return-to-method assessment.
