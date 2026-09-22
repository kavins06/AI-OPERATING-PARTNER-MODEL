---
name: agent-change-expansion-retirement
description: "Review material changes, expansion, rollback, remediation, retirement, and redesign loops. Use after approved Step 18 handoff and separate implementation approval as part of the Section 2 build and Managed AgentOps backbone."
---

# Agent Change Expansion Retirement

## Boundary

Use this skill only for Section 2 Phases 14 and 15 after Step 18 handoff approval, separate implementation approval, and an existing build or operating record. This skill governs lifecycle decisions after a release exists or a release change is requested.

Do not use this skill to sneak in unapproved expansion. Any new user group, workflow boundary, source, data class, tool, write/send action, model autonomy, behavior level, production environment, or operating owner model must be treated as material until proven otherwise.

Stop and return to the `agent-build-managed-agentops` orchestrator when the work requires build, architecture, eval, release, pilot, or production readiness rework. Stop and return to the Section 1 method owner when the requested change or redesign invalidates readiness, risk, value, workflow diagnosis, source-of-truth, adoption, or lifecycle assumptions from the approved method packet.

## Required Inputs

Use the Section 1 to Section 2 handoff map before producing outputs:

- `../agent-build-managed-agentops/assets/mappings/section1-to-section2-handoff-map.yaml`

Required Section 1 inputs for the owned phases:

- `implementation_decision_packet`
- `managed_lifecycle_object`
- `measurement_intelligence`
- `method_to_build_handoff_contract`
- `organizational_intelligence_diagnostic`
- `readiness_object`
- `risk_control_model`

Required Section 2 lifecycle inputs:

- `agentops_operating_record`
- `release_version_manifest`
- `production_readiness_gate`
- `tool_contract_registry`
- `eval_harness_spec`
- `guardrail_control_matrix`
- `trace_observability_spec`
- `incident and near-miss evidence`
- `support, adoption, value, cost, and correction evidence`

## Owned Phases

- Phase 14: Expansion/Change-Control Gate.
- Phase 15: Retirement Or Redesign Loop.

### Phase 14: Expansion/Change-Control Gate

Purpose: decide whether a requested material change, expansion, remediation, rollback, or release alteration is approved, limited, held, rolled back, or returned to method.

Section 1 inputs:

- `managed_lifecycle_object`
- `readiness_object`
- `implementation_decision_packet`
- `method_to_build_handoff_contract`

Section 2 outputs:

- `change_expansion_retirement_review`

Templates:

- `skills/agent-build-managed-agentops/assets/templates/change-expansion-retirement-review.yaml`

Material change examples:

- Add a new user group, region, department, client, workflow, business process, system, connector, source, retrieval corpus, data class, or output channel.
- Move from read-only, draft-and-flag, or recommendation support into human-approved action or autonomous action.
- Add write, send, delete, approve, schedule, route, payment, account, or permission-changing capability.
- Change the model class, model routing, prompt/instruction hierarchy, guardrail threshold, eval dataset, source authority, service account, access group, runtime, or release packaging in a way that changes risk or output behavior.
- Expand volume, operating hours, business criticality, or downstream decision reliance beyond the approved lifecycle object.

Stop conditions:

- Requested change would create an unapproved write/send/autonomous action.
- Required Section 1 source inputs are missing, stale, contradicted, or not approved.
- Requested source, tool, data class, or user group lacks named owner and access review.
- Existing incidents or control violations are unresolved and relevant to the requested change.
- Evals, guardrails, traceability, rollback, or revocation path cannot cover the changed behavior.
- The change materially changes value, risk, readiness, lifecycle, adoption, or source-of-truth assumptions.

Return-to-method triggers:

- Expansion requires new discovery, workflow mapping, readiness scoring, risk controls, value case, or lifecycle decision.
- The requested behavior is outside the approved first behavior or approved operating model.
- The business sponsor is requesting a different outcome than the approved use case.
- The change depends on an organizational policy, source-of-truth, or owner model that Section 1 did not validate.

Implementation example:

- A draft-and-flag revenue intake agent requests CRM write access to set a `missing_info_requested` field. This is a new write action and a new downstream system effect. Phase 14 must hold the change until a revised tool contract, eval suite, human approval control, rollback package, access review, and Section 1 risk/value reassessment are approved.

### Phase 15: Retirement Or Redesign Loop

Purpose: decide whether an agent should continue unchanged, pause, remediate, redesign, retire, or return to method when operating evidence shows low value, high correction burden, source drift, owner gaps, unacceptable risk, or misfit with the real workflow.

Section 1 inputs:

- `managed_lifecycle_object`
- `measurement_intelligence`
- `risk_control_model`
- `organizational_intelligence_diagnostic`

Section 2 outputs:

- `change_expansion_retirement_review`

Retirement or redesign triggers:

- Value misses the minimum threshold for two consecutive review cycles.
- Human correction, override, or support burden consumes the expected efficiency gain.
- Control violations, near misses, or incident severity exceed the risk appetite.
- Source freshness repeatedly fails or the source-of-truth owner cannot support the agent.
- Required owner coverage is unavailable or revocation responsibilities are unclear.
- Adoption is persistently low because the workflow, incentives, or operating model do not match the original diagnosis.
- A simpler tool, report, SOP, template, or workflow automation now meets the need with less risk.
- The agent needs a materially different behavior, population, data path, or operating model to remain useful.

Stop conditions:

- A high or critical incident remains unresolved.
- The current release cannot be operated with current sources, current controls, and named owner coverage.
- Users are relying on outputs that the agent can no longer support with evidence.
- Retirement would strand users, data, queued actions, or downstream processes without a transition plan.
- Redesign would require new discovery or readiness work but no sponsor is assigned.

Return-to-method triggers:

- Redesign requires a new use case, new business value case, new risk control model, or new lifecycle object.
- Retirement evidence shows the original workflow or organizational diagnosis was wrong.
- A replacement process changes the decision rights, source ownership, or human review model.
- The proposed future state is not an agent or is a different class of agent than the approved build.

Implementation example:

- A revenue intake agent saves 3 hours per week but creates 5 hours of coordinator correction and support effort, while the source field dictionary goes stale twice in a month. Phase 15 should pause expansion, route work to the manual fallback, revoke optional pilot access, compare retirement versus redesign, and return to method if the workflow now needs a governed CRM data cleanup rather than an agent.

## Resource Map

- Local phase packs: `assets/phase-packs`
- `../agent-build-managed-agentops/assets/schemas/agentops-object-schemas.yaml`
- `../agent-build-managed-agentops/assets/templates/change-expansion-retirement-review.yaml`
- `../agent-build-managed-agentops/assets/checklists/change-expansion-review-checklist.md`
- `../agent-build-managed-agentops/assets/checklists/retirement-redesign-checklist.md`
- `../agent-build-managed-agentops/assets/rubrics/change-control-rubric.yaml`
- `../agent-build-managed-agentops/assets/rubrics/retirement-redesign-rubric.yaml`
- `../agent-build-managed-agentops/assets/validator-rules/expansion_change_control_gate.yaml`
- `../agent-build-managed-agentops/assets/validator-rules/retirement_or_redesign_loop.yaml`
- `../agent-build-managed-agentops/assets/examples/golden-path/14-change-expansion-review.yaml`
- `../agent-build-managed-agentops/assets/examples/golden-path/15-retirement-redesign-review.yaml`
- `../agent-build-managed-agentops/assets/examples/golden-path-revenue-intake.yaml`

## Workflow

1. Classify the request as change, expansion, remediation, rollback, retirement, redesign, or return-to-method candidate.
2. Freeze the current approved scope and compare requested scope against the operating record, release manifest, production gate, handoff contract, and lifecycle object.
3. Check stop conditions first. If any automatic blocker is present, hold or pause before further analysis.
4. Confirm source inputs are approved, versioned, current, and cited. Missing or stale method evidence is a blocker.
5. Enumerate every delta across users, workflows, systems, tools, data classes, sources, outputs, behavior level, model/runtime, access, monitoring, support, and owner coverage.
6. Reassess value, quality, risk, source freshness, access, adoption, cost, incidents, support burden, and readiness against the approved baseline.
7. Identify required contract updates: build contract, release manifest, tool registry, eval harness, guardrail matrix, trace spec, run card, operating record, incident runbook, support playbook, and communications.
8. Define rollout, rollback, revocation, monitoring, owner coverage, training, and user communication requirements.
9. Decide: approve, approve with conditions, hold, remediate, rollback, retire, redesign, or return to method. Each decision must include owner, evidence, approved scope, denied scope, stop conditions, expiry, and next review.
10. Update the `change_expansion_retirement_review` and link follow-up work to the operating record.

## Output Contracts

- `change_expansion_retirement_review`: source-of-truth decision record for material changes, expansion, remediation, rollback, retirement, redesign, or return-to-method routing. It must show the baseline scope, requested delta, materiality decision, risk/value/readiness reassessment, source/access/owner review, required contract updates, stop conditions, approved and denied scope, rollout or decommission plan, and signoff.

## Quality Bar

Do not approve change or expansion because it is operationally convenient. Do not keep a low-value or unsafe agent alive because it already exists. Every lifecycle decision must preserve method integrity: either stay within the approved handoff with evidence, or explicitly return to method for a new decision.
