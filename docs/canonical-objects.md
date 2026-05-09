# Canonical Objects

The future webapp should treat the method artifacts as domain objects, not as static documents. The canonical schema lives at `skills/ai-operating-partner-engagement/assets/schemas/canonical-object-schemas.yaml`.

## Object Chain

| Stage | Object | Purpose |
|---|---|---|
| Step 2 | `candidate_use_case_shortlist` | Names candidate opportunities, hypotheses, dependencies, success-pattern fit, sponsor fit, confidence, and disqualification criteria. |
| Step 4 | `variation_map` | Captures whether one workflow is canonical or fragmented across roles, regions, systems, portfolios, or local practice. |
| Step 6 | `workflow_intelligence_object` | Describes the work: roles, steps, decisions, information objects, source access, truth production, edge cases, evidence, and completeness. |
| Step 7 | `organizational_intelligence_diagnostic` | Classifies blockers, invisible costs, resistance sources, sponsor mechanics, root-cause hypotheses, affected behavior levels, and required routes. |
| Step 8 | `organizational_intelligence_baseline` | Releases a validated baseline with audience views and downstream payloads. |
| Step 9 | `knowledge_requirements_map` | Defines knowledge, guideline, tacit judgment, and expertise gaps. |
| Step 10 | `ai_guidance_pack` | Converts knowledge into rules, examples, output contracts, source hierarchy, forbidden behaviors, and eval suites. |
| Step 11 | `measurement_intelligence` | Classifies existing metrics and designs AI capability metrics, value-breadth metrics, governance metrics, drift signals, costs, and kill criteria. |
| Step 13 | `solution_shape` | Specifies future solution posture, UX surface, oversight model, agent topology, model class, adoption design, and risk loop status. |
| Step 14 | `technical_blueprint` | Defines future architecture, systems, data-access plan, model abstraction/routing, access paths, component contracts, normalization, truth remediation, and build sequence. |
| Step 15 | `risk_control_model` | Defines data classification, shadow AI risk, security enablement, risks, controls, tool permissions, output controls, stop conditions, and redesign loops. |
| Step 16 | `readiness_object` | Scores hard gates, sponsor behavior, process documentation, resistance, recoverable-error fit, model/orchestration, security enablement, behavior levels, blockers, minimum safe first behavior, and recommended Step 17 path. |
| Step 17 | `implementation_decision_packet` or `packet_set` | Produces the build, remediation, risk, technical, knowledge, governance, or do-not-automate decision. |
| Step 18 | `managed_lifecycle_object` or `lifecycle_set` | Defines future operation, remediation, or no-automation review cadence plus handoff requirements. |

## Post-18 Build/Operate Contracts

Post-18 contracts are implementation artifacts, not new method objects and not another numbered method step. They may be created only after Step 18 approval, accepted method-to-build handoff, and separate implementation approval.

The `agent-build-managed-agentops` skill consumes approved Step 17/18 objects and can produce a build/operate contract set:

- `agent_build_contract`
- `agent_necessity_kill_test`
- `agent_build_plan`
- `agent_architecture_record`
- `tool_contract_registry`
- `eval_harness_spec`
- `guardrail_control_matrix`
- `trace_observability_spec`
- `environment_progression_gate`
- `release_version_manifest`
- `pilot_launch_gate`
- `production_readiness_gate`
- `agentops_operating_record`
- `change_expansion_retirement_review`

The human-readable `incident-revocation-runbook.md` and `internal-operator-run-card.md` support those machine-readable contracts with incident triage, pause, revoke, rollback, communication, recovery, daily checks, stop conditions, and escalation procedures.

These contracts must preserve evidence references, owner decisions, approved behavior scope, prohibited behaviors, access limits, control obligations, lifecycle rules, and return-to-method triggers from the Step 17/18 handoff.

The required crosswalk is maintained in `section1-to-section2-data-map.md` and `skills/agent-build-managed-agentops/assets/mappings/section1-to-section2-handoff-map.yaml`. Section 2 contracts should cite Section 1 source artifacts through `source_inputs` or evidence references rather than rediscovering or re-deciding approved method facts.

## Cross-Object Rules

- Every material claim should carry evidence references and confidence.
- Source access profiles attach practical access paths to information objects.
- Truth production profiles attach official sources, de facto trusted sources, manual adjustments, reproducibility, auditability, and safe AI usage.
- Candidate use cases can be disqualified at discovery, economic, or readiness events.
- Sponsor mechanics, resistance profile, prior-failure learning, and oversight model should be carried forward as structured fields, not left as narrative notes.
- Step 8 validation changes loop back into Step 6 and Step 7 when they alter workflow, source, truth, or blocker facts.
- Step 15 risk findings can force a return to Step 13 when controls require different topology, behavior level, UX, retrieval, or adoption design.
- Step 16 readiness selects the Step 17 packet path; hard gates override average scores.
- Step 17 packet sets create Step 18 lifecycle sets when multiple packet paths apply.

## App Domain Model Implications

A future app should store these objects as versioned, evidence-linked records. It should support:

- Draft, partial validation, validated, blocked, approved, and superseded states.
- Object diffs across validation cycles.
- Owner assignment and review state per blocker, source, truth profile, control, and packet.
- Source/evidence privacy metadata and redaction status.
- Behavior-level authorization, not just use-case authorization.
- Exportable machine-readable payloads for build teams.
- Post-18 build/operate contracts linked to approved handoff versions and separate implementation approvals.

The app should not flatten the method into a survey. The value is in preserving relationships among work, truth, risk, measurement, adoption, and lifecycle.
