# Section 1 To Section 2 Data Map

This map defines how data collected and approved during the Step 0-18 discovery/pre-build method becomes directly usable during post-18 implementation and Managed AgentOps.

The machine-readable source of truth is:

- `skills/agent-build-managed-agentops/assets/mappings/section1-to-section2-handoff-map.yaml`

## Boundary

Section 2 starts only after:

- Step 17 `implementation_decision_packet` or `packet_set` is approved.
- Step 18 `managed_lifecycle_object` or `lifecycle_set` is approved.
- The Step 18 method-to-build handoff contract is accepted.
- A separate implementation approval authorizes build-phase work.

Section 2 may carry forward approved Section 1 data. It must not invent missing Section 1 decisions.

## Main Handoff Carriers

| Section 1 Source | Primary Section 2 Use |
|---|---|
| Step 2 `candidate_use_case_shortlist` | Opportunity ID, target users, value hypothesis, disqualification criteria, agent necessity check. |
| Step 6 `workflow_intelligence_object` | Roles, workflow steps, decisions, information objects, edge cases, and workflow boundary. |
| Step 8 `organizational_intelligence_baseline` | Validated sources, owners, access paths, sensitivity, retention, permitted/prohibited AI actions. |
| Step 10 `ai_guidance_pack` | Rules, examples, output contracts, eval cases, source hierarchy, forbidden behaviors. |
| Step 11 `measurement_intelligence` | Success metrics, AI capability metrics, drift signals, costs, kill criteria. |
| Step 12 `business_value_case` | Business outcome, value range, assumptions, confidence, AI-side costs, value risks. |
| Step 13 `solution_shape` and `adoption_design` | Agent topology, UX surface, model posture, oversight model, target users, rollout, incentives, feedback. |
| Step 14 `technical_blueprint` | Architecture, runtime, hosting, access paths, identity, component contracts, test strategy, audit/logging. |
| Step 15 `risk_control_model` | Risks, controls, tool permissions, output controls, incident response, revocation, stop conditions. |
| Step 16 `readiness_object` | Hard gates, behavior readiness, blockers, minimum safe first behavior, prohibited behaviors. |
| Step 17 `implementation_decision_packet` | Build decision, first build scope, behavior contract, systems/sources, owner matrix, future access requests. |
| Step 18 `managed_lifecycle_object` | Authorized lifecycle, owners, launch gates, validation plan, monitoring plan, change/incident/retirement rules. |
| Step 18 `method_to_build_handoff_contract` | What transfers, what does not transfer, entry criteria, owner acceptance, return-to-method triggers. |
| Separate implementation approval | Build authorization, budget/timebox, owner forum, implementation scope, permitted environments. |

## Section 2 Consumption

| Section 2 Phase | Consumes From Section 1 | Produces |
|---|---|---|
| 1. Build Conversion Gate | Step 17 packet, Step 18 lifecycle, handoff contract, separate implementation approval | `agent_build_contract` |
| 2. Agent Necessity Check | Candidate shortlist, value case, solution shape, readiness object, Step 17 packet | `agent_necessity_kill_test` |
| 3. First Behavior Scope | Step 17 first scope, Step 16 minimum safe behavior, Step 18 lifecycle scope, workflow/baseline objects | `agent_build_contract`, `agent_build_plan` |
| 4. Agent Architecture Spec | Solution shape, technical blueprint, risk/control model, Step 17 runtime requirements | `agent_architecture_record` |
| 5. Tool/Data/Identity Contracts | Technical blueprint, baseline source/access decisions, risk controls, future access requests | `tool_contract_registry` |
| 6. Environment And Access Setup | Hosting/environment requirements, lifecycle environments, handoff entry criteria | `environment_progression_gate` |
| 7. Eval And Guardrail Design | Guidance pack, measurement intelligence, readiness object, risk/control model, lifecycle launch gates | `eval_harness_spec`, `guardrail_control_matrix` |
| 8. Sandbox Prototype | Blueprint, guidance pack, controls, handoff boundary | Updated gates and release evidence |
| 9. Security And Control Review | Risk/control model, blueprint observability, lifecycle incident/revocation requirements | `guardrail_control_matrix`, `trace_observability_spec` |
| 10. Controlled Pilot | Lifecycle pilot stage, adoption design, metrics, stop conditions | `pilot_launch_gate`, `agentops_operating_record` |
| 11. Production Readiness Gate | Lifecycle launch gates, controls, metrics, blueprint, pilot evidence | `production_readiness_gate` |
| 12. Production Release | Blueprint build sequence, lifecycle release rules, controls | `release_version_manifest` |
| 13. Managed AgentOps | Lifecycle monitoring, metrics, guidance update rules, baseline source owners, controls | `agentops_operating_record` |
| 14. Expansion/Change-Control Gate | Lifecycle change rules, readiness object, Step 17 boundaries, handoff triggers | `change_expansion_retirement_review` |
| 15. Retirement Or Redesign Loop | Lifecycle retirement criteria, metrics, risk events, diagnostic signals | `change_expansion_retirement_review` |

## Non-Negotiable Mapping Rules

- Every Section 2 object must cite Section 1 source artifacts through `source_inputs` or equivalent evidence references.
- `agent_build_contract.authorization.build_authorized` requires Step 18 approval and separate implementation approval.
- Section 2 scope must be equal to or narrower than approved Section 1 first build scope unless `change_expansion_retirement_review` approves a material change.
- Section 1 owners must normalize into Section 2 owner fields before pilot or production.
- Section 1 risk, incident, revocation, audit, and monitoring requirements must map into guardrails, trace/observability, production readiness, and operating records.
- If build learning invalidates approved workflow, truth, value, risk, technical, owner, or lifecycle assumptions, return to the method owner instead of forcing implementation through.

## Anti-Loss Checks

Use these checks before any Section 2 phase exits:

- No orphan output: every Section 2 object has `source_inputs` that point to approved Section 1 object IDs or a documented Section 2 predecessor object.
- No silent transformation: every derived field has a mapping rule, not just a copied phrase.
- No owner drop: business, technical, data/source, security/risk, support, AgentOps, and revocation ownership survives the handoff.
- No control drop: every Step 15 risk/control, incident, revocation, stop condition, and monitoring requirement appears in at least one guardrail, trace, readiness, runbook, or operating record.
- No metric drop: Step 11 value, quality, cost, drift, and kill metrics appear in evals, readiness gates, or Managed AgentOps metrics.
- No source drop: Step 8 source owners, access paths, sensitivity, retention, permitted actions, prohibited actions, and freshness rules appear in tool, retrieval, trace, and operating records.
- No guidance drop: Step 10 rules, examples, output contract, prohibited behaviors, and revalidation triggers appear in eval, guardrail, release, and operating records.
- No scope creep: any new user group, workflow step, source, tool, model/runtime, environment, output type, action authority, or autonomy level starts Section 2 phase 14 before implementation.

## Validation

Run:

```powershell
python .\skills\agent-build-managed-agentops\scripts\validate_agentops_contracts.py
```

The validator checks that the mapping file exists, parses, covers all required Section 2 objects, includes required handoff artifacts, and includes the required mapping types.
