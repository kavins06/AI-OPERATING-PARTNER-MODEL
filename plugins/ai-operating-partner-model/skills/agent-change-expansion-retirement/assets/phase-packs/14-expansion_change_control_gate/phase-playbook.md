# Phase 14: Expansion/Change-Control Gate

Local phase pack for `expansion_change_control_gate`. Use this file from the owning support skill folder; use the referenced central assets as the source of truth for executable templates, rubrics, validator rules, and examples.

## Required Inputs

- `managed_lifecycle_object`
- `readiness_object`
- `implementation_decision_packet`
- `method_to_build_handoff_contract`

## Required Outputs

- `change_expansion_retirement_review`

## Canonical Assets

Templates:

- `skills/agent-build-managed-agentops/assets/templates/change-expansion-retirement-review.yaml`

- Checklist: `skills/agent-build-managed-agentops/assets/checklists/change-expansion-review-checklist.md`
- Rubric: `skills/agent-build-managed-agentops/assets/rubrics/change-control-rubric.yaml`
- Validator rule: `skills/agent-build-managed-agentops/assets/validator-rules/expansion_change_control_gate.yaml`
- Golden-path example: `skills/agent-build-managed-agentops/assets/examples/golden-path/14-change-expansion-review.yaml`

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

- New user, source, tool, workflow, behavior level, model, or write/send action is added without approval.

## Return-To-Method Triggers

- Expansion changes readiness, risk, value, or lifecycle assumptions.

## Exit Evidence

- Source input IDs and evidence references.
- Completed output object IDs or blocked output decision.
- Checklist result.
- Rubric result.
- Validator result.
- Owner signoff or blocker owner.
- Return-to-method assessment.
