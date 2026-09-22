# Agent Necessity Kill Test Checklist

Use this checklist for Section 2 phase 2: `agent_necessity_check`.

## Inputs

- `candidate_use_case_shortlist`
- `business_value_case`
- `solution_shape`
- `readiness_object`
- `implementation_decision_packet`

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/agent-necessity-kill-test.yaml`

Outputs:

- `agent_necessity_kill_test`

## Entry Checks

- [ ] Confirm the candidate use case, value case, solution shape, readiness object, and implementation decision packet are approved, versioned, and cited.
- [ ] Confirm the build contract from Phase 1 exists or that missing contract evidence is listed as a blocker.
- [ ] Confirm the approved first behavior and behavior level are carried forward without expansion.
- [ ] Confirm the current status quo and requested outcome are grounded in Section 1 evidence.
- [ ] Confirm the phase owner and decision approvers are named before scoring alternatives.

## Phase-Specific Checks

- [ ] Populate `source_input_usage` for all five required Section 1 inputs with completeness status and evidence refs.
- [ ] State the requested agent outcome, status quo, lowest-risk sufficient solution, reason an agent is considered, and approved first behavior.
- [ ] Compare at least six simpler alternatives: human process, SOP/training, workflow automation, report/dashboard, search/retrieval, and template/macro.
- [ ] For each simpler alternative, record outcome fit, delivery speed, effort, risk delta, operating cost delta, value delta, evidence refs, and select/reject rationale.
- [ ] Score every agent-fit test with evidence: contextual judgment, unstructured reasoning, value vs operating burden, safe constraint, and workable human oversight.
- [ ] Explicitly include evals, monitoring, controls, incident response, support, and owner cadence in operating burden.
- [ ] Compare agent-specific risks, simpler-path risks, controls required for each path, net risk position, and evidence gaps.
- [ ] Complete `decision_gate` with pass criteria, fail criteria, automatic kill conditions, conditional-pass rules, and failure handling.
- [ ] Carry all required scope reductions into `kill_decision.required_scope_reductions`.
- [ ] Evaluate return-to-method triggers before `proceed_with_agent_build`.

## Scope Checks

- [ ] Confirm the requested agent outcome is the approved first behavior, not the broader roadmap.
- [ ] Confirm simpler alternatives are judged against the same approved outcome and user group.
- [ ] Confirm agent-fit tests do not assume unapproved sources, tools, environments, write/send actions, or behavior level.
- [ ] Confirm required scope reductions preserve or narrow the approved Step 17/18 handoff.
- [ ] Confirm any agent path that needs broader scope is marked `return_to_method`, not `proceed_with_agent_build`.

## Evidence Checks

- [ ] Evidence demonstrates why a simpler non-agent path is insufficient.
- [ ] Evidence demonstrates agent value exceeds ongoing AgentOps burden.
- [ ] Evidence demonstrates human oversight can meet expected volume and SLA.
- [ ] Evidence demonstrates the first behavior can be constrained to approved sources, users, actions, outputs, and environment.
- [ ] Any missing evidence is recorded as `hold_for_more_evidence`, not treated as a pass.

## Output Completeness

- [ ] `source_inputs` and `source_input_usage` are complete.
- [ ] `decision_summary` includes the decision forcing question and operating burden summary.
- [ ] `simpler_alternatives` includes realistic non-agent paths and selected/rejected decisions.
- [ ] `agent_fit_tests` are all scored with evidence refs.
- [ ] `risk_comparison` includes net risk position and operating burden delta.
- [ ] `decision_gate` includes pass/fail criteria and failure handling.
- [ ] `return_to_method_review` is evaluated.
- [ ] `kill_decision` has decision, rationale, required scope reductions, approvers, and date or blocker.
- [ ] `kill_test_signoff` lists required signoff roles and current approval status.

## Exit Checks

- [ ] Rubric result is pass, conditional, blocked, or return-to-method with rationale.
- [ ] Validator rule group `agent_necessity_check` has no error-level failures.
- [ ] Decision is one of `proceed_with_agent_build`, `replace_with_simpler_path`, `hold_for_more_evidence`, or `return_to_method`.
- [ ] Required owner signoffs are captured or explicitly blocking.
- [ ] Phase 3 scope reductions and dependencies are explicit.

## Blocking Conditions

- A simpler non-agent path satisfies the approved outcome with lower risk and acceptable value.
- Agent value does not justify evals, monitoring, controls, support, incident response, and ongoing AgentOps.
- Human oversight is undefined, infeasible, or lacks an accountable reviewer.
- Agent path requires unapproved source, tool, write/send action, user group, environment, or behavior-level expansion.
- Required Section 1 value, readiness, solution, or decision evidence is missing.
- The agent path changes the Step 17 implementation decision or invalidates the Step 18 lifecycle object.
- Required owner signoff is missing.

## Failure Modes

- Simpler non-agent path satisfies the approved outcome.
- Agent value does not justify operating burden.
- Human oversight is not workable.

## Return-To-Method Triggers

- Agent path changes recommended Step 17 decision.
- Lowest-risk sufficient solution is not an agent.
- Approved first behavior, value case, readiness posture, oversight model, or solution shape must change for the build to proceed.
