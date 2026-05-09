---
name: agent-build-intake-and-scope
description: "Gate implementation approval and lock the first safe agent behavior. Use after approved Step 18 handoff and separate implementation approval as part of the Section 2 build and Managed AgentOps backbone."
---

# Agent Build Intake And Scope

## Boundary

Use this skill only after Step 17/18 artifacts and separate implementation approval are approved. Section 2 may carry forward approved Section 1 facts, but it must not backfill, reinterpret, or expand missing Section 1 decisions.

Return to `agent-build-managed-agentops` for phases outside 1-3. Return to the Section 1 method owner when source approval, scope, owner model, risk posture, business value, workflow boundary, or lifecycle assumptions are missing or invalidated.

## Required Inputs

Read `../agent-build-managed-agentops/assets/mappings/section1-to-section2-handoff-map.yaml` before producing outputs.

Required Section 1 inputs across owned phases:

- `business_value_case`
- `candidate_use_case_shortlist`
- `implementation_decision_packet`
- `managed_lifecycle_object`
- `method_to_build_handoff_contract`
- `organizational_intelligence_baseline`
- `readiness_object`
- `separate_implementation_approval`
- `solution_shape`
- `workflow_intelligence_object`

## Owned Phases

- Phase 1: `build_conversion_gate` produces `agent_build_contract`.
- Phase 2: `agent_necessity_check` produces `agent_necessity_kill_test`.
- Phase 3: `first_behavior_scope` updates `agent_build_contract` and produces `agent_build_plan`.

## Resource Map

- Local phase packs: `assets/phase-packs`
- Templates: `../agent-build-managed-agentops/assets/templates/build-intake-contract.yaml`, `../agent-build-managed-agentops/assets/templates/agent-necessity-kill-test.yaml`, `../agent-build-managed-agentops/assets/templates/agent-build-plan.yaml`
- Checklists: `../agent-build-managed-agentops/assets/checklists/build-conversion-gate-checklist.md`, `../agent-build-managed-agentops/assets/checklists/agent-necessity-kill-test-checklist.md`, `../agent-build-managed-agentops/assets/checklists/first-behavior-scope-checklist.md`
- Rubrics: `../agent-build-managed-agentops/assets/rubrics/build-conversion-gate-rubric.yaml`, `../agent-build-managed-agentops/assets/rubrics/agent-necessity-kill-test-rubric.yaml`, `../agent-build-managed-agentops/assets/rubrics/first-behavior-scope-rubric.yaml`
- Validator rules: `../agent-build-managed-agentops/assets/validator-rules/build_conversion_gate.yaml`, `../agent-build-managed-agentops/assets/validator-rules/agent_necessity_check.yaml`, `../agent-build-managed-agentops/assets/validator-rules/first_behavior_scope.yaml`
- Golden-path examples: `../agent-build-managed-agentops/assets/examples/golden-path/01-agent-build-contract.yaml`, `../agent-build-managed-agentops/assets/examples/golden-path/02-agent-necessity-kill-test.yaml`, `../agent-build-managed-agentops/assets/examples/golden-path/03-agent-build-plan.yaml`

## Workflow

1. Confirm every required Section 1 source artifact is approved, versioned, cited, and still valid.
2. Complete the phase checklist and output template without widening the approved handoff.
3. Apply the phase rubric and validator rule group.
4. Record pass, conditional pass, blocked, or return-to-method decision with owner signoff.
5. Stop the phase when required evidence, approval, owner coverage, human review, or failure handling is incomplete.

## Output Contracts

- `agent_build_contract`
- `agent_necessity_kill_test`
- `agent_build_plan`

## Quality Bar

Phases 1-3 are not discovery. They are conversion gates. Passing means the approved Section 1 handoff is traceably converted into buildable, owned, constrained Section 2 contracts with explicit evidence, pass/fail criteria, failure handling, return-to-method triggers, and signoff.
