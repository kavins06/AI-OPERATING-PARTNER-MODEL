# Build Conversion Gate Checklist

Use this checklist for Section 2 phase 1: `build_conversion_gate`.

## Inputs

- `implementation_decision_packet`
- `managed_lifecycle_object`
- `method_to_build_handoff_contract`
- `separate_implementation_approval`

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/build-intake-contract.yaml`

Outputs:

- `agent_build_contract`

## Entry Checks

- [ ] Confirm the Step 17 `implementation_decision_packet` is approved, versioned, and explicitly build-ready.
- [ ] Confirm the Step 18 `managed_lifecycle_object` is approved and authorizes the behavior level being carried into Section 2.
- [ ] Confirm the `method_to_build_handoff_contract` is accepted and includes entry criteria, non-transfer items, owner acceptance, and return-to-method triggers.
- [ ] Confirm `separate_implementation_approval` exists with authorizing body, approval date, budget/timebox, build owner, technical owner, security/risk approvers, and permitted environments.
- [ ] Confirm every required artifact has an evidence reference and none are only described from memory.
- [ ] Confirm unresolved handoff questions are listed as blockers or conditional items before any build work proceeds.

## Phase-Specific Checks

- [ ] Populate `agent_build_contract.source_inputs` with object IDs, handoff version, approved behavior level, approved environments, and evidence refs.
- [ ] Populate `source_input_usage` for all four required inputs and mark completeness status for each.
- [ ] Set `authorization.build_authorized` to true only when Step 18 approval and separate implementation approval are both explicit and current.
- [ ] Record `authorization.budget_timebox`, `authorized_scope_summary`, `authorized_environments`, and `explicit_out_of_scope`.
- [ ] Normalize Section 1 owner roles into business, product, technical, security, data, risk/compliance, AgentOps, support, and revocation owners.
- [ ] Confirm owner coverage checks are true or list each gap as a blocker with owner and due date.
- [ ] Carry forward the narrowest approved workflow boundary, user groups, systems, data domains, tools/actions, and minimum safe first behavior.
- [ ] Preserve prohibited use cases, excluded user groups, systems out of scope, and prohibited tools/actions without softening language.
- [ ] Complete `gate_decisions.build_conversion_gate` with required evidence, pass/fail basis, failure handling, owner signoffs, and return-to-method review.
- [ ] Confirm the contract does not authorize pilot, production, new user groups, new sources, write/send actions, or behavior-level expansion.

## Scope Checks

- [ ] Confirm target users, excluded users, workflow boundary, systems, data domains, and tools/actions match approved Step 17/18 scope.
- [ ] Confirm approved behavior level is not higher than the Step 18 lifecycle authorization.
- [ ] Confirm permitted environments do not imply pilot or production authorization.
- [ ] Confirm every prohibited use case, excluded system, and prohibited action remains explicit.
- [ ] Confirm any requested expansion is removed or routed to return-to-method/change review before exit.

## Evidence Checks

- [ ] Attach evidence refs for authorization, scope, owner model, approved environments, budget/timebox, and lifecycle path.
- [ ] Cite Section 1 paths used for every material field in the contract.
- [ ] Record missing evidence in `open_handoff_questions`; do not fill unknown fields by inference.
- [ ] Confirm approval conditions are either satisfied, assigned, or blocking.
- [ ] Confirm failure-handling instructions are actionable for missing approval, scope ambiguity, owner gaps, and evidence gaps.

## Output Completeness

- [ ] `source_inputs` is complete for required phase inputs.
- [ ] `authorization` has decision state, authorizing body, date, budget/timebox, authorized scope, and out-of-scope terms.
- [ ] `owners` has required accountable owners or explicit blockers.
- [ ] `build_scope` has users, workflow boundary, allowed/prohibited systems, data, actions, and first behavior.
- [ ] `acceptance_contract` lists Phase 1 exit artifacts and launch blockers.
- [ ] `change_control` defines material change and requires `change_expansion_retirement_review`.
- [ ] `contract_signoff` lists required roles and current approval status.

## Exit Checks

- [ ] Rubric result is pass, conditional, blocked, or return-to-method with rationale.
- [ ] Validator rule group `build_conversion_gate` has no error-level failures.
- [ ] Required owner signoffs are captured or explicitly blocking.
- [ ] Return-to-method triggers are evaluated and recorded, including handoff version and incomplete Step 17/18 artifacts.
- [ ] Phase 2 dependencies are explicit.

## Blocking Conditions

- Step 18 approval is missing, expired, contradicted, or cannot be tied to a versioned lifecycle object.
- Separate implementation approval is missing, lacks budget/timebox, or does not authorize the requested environment.
- Required owner model is incomplete, especially business, technical, security, data, AgentOps, support, or revocation owner.
- Scope, budget, timebox, behavior level, permitted environment, or first behavior is ambiguous.
- Any Section 2 scope exceeds the approved Step 17/18 handoff without change review.
- Evidence refs are missing for authorization, owner model, or scope.
- A required return-to-method trigger is active and unresolved.

## Failure Modes

- Step 18 approval missing.
- Separate implementation approval missing.
- Owner model incomplete.
- Scope or budget/timebox ambiguous.

## Return-To-Method Triggers

- Handoff version cannot be identified.
- Required Step 17/18 artifact is incomplete.
- Approved behavior level, workflow boundary, source, owner model, risk posture, or lifecycle assumption is contradicted.
