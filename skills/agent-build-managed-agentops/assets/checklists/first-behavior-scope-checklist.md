# First Behavior Scope Checklist

Use this checklist for Section 2 phase 3: `first_behavior_scope`.

## Inputs

- `implementation_decision_packet`
- `readiness_object`
- `managed_lifecycle_object`
- `workflow_intelligence_object`
- `organizational_intelligence_baseline`

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/build-intake-contract.yaml`
- `skills/agent-build-managed-agentops/assets/templates/agent-build-plan.yaml`

Outputs:

- `agent_build_contract`
- `agent_build_plan`

## Entry Checks

- [ ] Confirm Phase 1 build contract exists and does not contain unresolved authorization blockers.
- [ ] Confirm Phase 2 kill test is `proceed_with_agent_build` or that the build is intentionally blocked.
- [ ] Confirm required Section 1 inputs are approved, versioned, and cited.
- [ ] Confirm the approved first build scope and minimum safe first behavior are the starting boundary.
- [ ] Confirm phase owner, reviewer, approver, and evidence location.

## Phase-Specific Checks

- [ ] Define exactly one first behavior in `agent_build_contract.first_behavior_scope.behavior_statement`.
- [ ] Confirm the first behavior is equal to or narrower than `implementation_decision_packet.first_build_scope`.
- [ ] Carry `readiness_object.minimum_safe_first_behavior`, hard gates, blockers, and prohibited behaviors into scope and blockers.
- [ ] Carry `managed_lifecycle_object.authorized_behavior_level`, lifecycle scope, launch gates, monitoring plan, and change rules into the plan.
- [ ] Carry `workflow_intelligence_object` roles, workflow start/end, decisions, edge cases, and information objects into the scope lock.
- [ ] Carry `organizational_intelligence_baseline` source owners, access profiles, sensitivity, retention, permitted AI actions, and prohibited AI actions into source limits.
- [ ] Specify approved and prohibited users, sources, systems, actions, outputs, edge cases, and environments.
- [ ] Define human review path with reviewer role, approval points, SLA, fallback, and escalation path.
- [ ] Define output contract with allowed output types, required fields, forbidden content, and traceability.
- [ ] Define stop conditions for unavailable sources, out-of-scope requests, insufficient evidence, and human review failure.
- [ ] Convert the locked first behavior into `agent_build_plan.first_behavior_scope_lock`, workstreams, milestones, dependencies, risks, and definition of done.

## Scope Checks

- [ ] Confirm the first behavior is a single narrow behavior, not multiple behaviors or a product roadmap.
- [ ] Confirm users, sources, systems, actions, outputs, environments, and behavior level are no broader than approved Step 17/18 scope.
- [ ] Confirm prohibited sources, actions, outputs, and edge cases are explicit in both contract and plan.
- [ ] Confirm workstreams, milestones, and dependencies do not imply unapproved expansion.
- [ ] Confirm any workflow boundary change triggers return-to-method before architecture or tooling work begins.

## Evidence Checks

- [ ] Evidence refs show where each allowed source, action, output, user group, and system was approved.
- [ ] Evidence refs show where each prohibited behavior or action came from.
- [ ] Evidence refs show human review capacity and authority.
- [ ] Evidence refs show source ownership, sensitivity, retention, and permitted/prohibited AI actions.
- [ ] Missing source, owner, workflow, or review evidence is recorded as a blocker.

## Output Completeness

- [ ] `agent_build_contract.first_behavior_scope` is complete.
- [ ] `agent_build_contract.gate_decisions.first_behavior_scope` is complete.
- [ ] `agent_build_plan.source_inputs` and `source_input_usage` are complete.
- [ ] `agent_build_plan.delivery_model` has build owner, delivery lead, review forums, target dates, and operating principles.
- [ ] `agent_build_plan.first_behavior_scope_lock` mirrors the contract scope.
- [ ] `agent_build_plan.phase_cadence` has decision owners and exit evidence for phases 1-3.
- [ ] `agent_build_plan.workstreams` have owners, deliverables, dependencies, and exit criteria.
- [ ] `agent_build_plan.milestones` include contract lock, necessity decision, first behavior lock, offline validation readiness, and pilot readiness.
- [ ] `agent_build_plan.definition_of_done.phase_3_complete_when` is filled.
- [ ] `agent_build_plan.return_to_method_controls` are evaluated.

## Exit Checks

- [ ] Rubric result is pass, conditional, blocked, or return-to-method with rationale.
- [ ] Validator rule group `first_behavior_scope` has no error-level failures.
- [ ] Required owner signoffs are captured or explicitly blocking.
- [ ] The next phase can build architecture without guessing behavior, source, action, output, review, or stop-condition details.
- [ ] Return-to-method triggers have been evaluated and recorded.

## Blocking Conditions

- First behavior is broader than approved Step 17/18 scope.
- Prohibited behaviors, sources, users, systems, actions, or outputs are missing or ambiguous.
- Human review path is undefined, infeasible, or missing accountable reviewer and SLA.
- Workflow boundary changes from approved Step 17/18 scope.
- Approved source ownership, access, sensitivity, retention, or permitted/prohibited action evidence is missing.
- Build plan milestones or workstreams imply broader behavior than the locked first behavior.
- Required owner signoff is missing.
- Any source, tool, write/send action, environment, or behavior-level expansion is required to implement the first behavior.

## Failure Modes

- First behavior is broader than approved handoff.
- Prohibited behaviors are not explicit.
- Human review path is undefined.

## Return-To-Method Triggers

- Workflow boundary changes from approved Step 17/18 scope.
- Minimum safe first behavior cannot be implemented using approved sources, actions, outputs, owners, or oversight.
- Organizational source/access baseline contradicts the approved build scope.
