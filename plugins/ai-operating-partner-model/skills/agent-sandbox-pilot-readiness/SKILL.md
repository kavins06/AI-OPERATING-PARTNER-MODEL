---
name: agent-sandbox-pilot-readiness
description: "Govern sandbox prototype evidence, controlled pilot launch, production readiness, incident rehearsal, revocation readiness, monitoring gates, and pilot-to-production promotion for Section 2 phases 8, 10, and 11. Use after approved Step 18 handoff and separate implementation approval as part of the Section 2 build and Managed AgentOps backbone."
---

# Agent Sandbox Pilot Readiness

## Boundary

Use this skill only inside Section 2 after Step 18 handoff approval and separate implementation approval. Do not backfill missing Section 1 decisions here.

Own only:

- Phase 8: Sandbox Prototype.
- Phase 10: Controlled Pilot.
- Phase 11: Production Readiness Gate.

Stop and return to the `agent-build-managed-agentops` orchestrator when the request requires architecture design, eval/guardrail design, security review, production release, live operations, expansion, rollback-after-release, retirement, or other phases outside this skill.

Stop and return to the Section 1 method owner when sandbox, pilot, or readiness evidence changes approved scope, risk posture, value assumptions, user group, source truth, behavior level, oversight model, or lifecycle obligations.

## Required Inputs

Read the handoff map before producing outputs:

- `../agent-build-managed-agentops/assets/mappings/section1-to-section2-handoff-map.yaml`

Use these Section 1 inputs across the owned phases:

- `adoption_design`
- `ai_guidance_pack`
- `managed_lifecycle_object`
- `measurement_intelligence`
- `method_to_build_handoff_contract`
- `risk_control_model`
- `technical_blueprint`

Require the Section 2 eval, guardrail, observability, environment, and release artifacts as evidence when promoting beyond sandbox.

## Owned Phases

- Phase 8: Sandbox Prototype.
- Phase 10: Controlled Pilot.
- Phase 11: Production Readiness Gate.

## Resource Map

- Local phase packs: `assets/phase-packs`
- Templates:
  - `../agent-build-managed-agentops/assets/templates/pilot-launch-gate.yaml`
  - `../agent-build-managed-agentops/assets/templates/production-readiness-gate.yaml`
  - `../agent-build-managed-agentops/assets/templates/release-version-manifest.yaml`
- Related templates:
  - `../agent-build-managed-agentops/assets/templates/environment-progression-gate.yaml`
  - `../agent-build-managed-agentops/assets/templates/agentops-operating-record.yaml`
- Checklists:
  - `../agent-build-managed-agentops/assets/checklists/sandbox-exit-checklist.md`
  - `../agent-build-managed-agentops/assets/checklists/pilot-readiness-checklist.md`
  - `../agent-build-managed-agentops/assets/checklists/production-readiness-checklist.md`
- Rubrics:
  - `../agent-build-managed-agentops/assets/rubrics/sandbox-exit-rubric.yaml`
  - `../agent-build-managed-agentops/assets/rubrics/pilot-readiness-rubric.yaml`
  - `../agent-build-managed-agentops/assets/rubrics/production-readiness-rubric.yaml`
- Validator rules:
  - `../agent-build-managed-agentops/assets/validator-rules/sandbox_prototype.yaml`
  - `../agent-build-managed-agentops/assets/validator-rules/controlled_pilot.yaml`
  - `../agent-build-managed-agentops/assets/validator-rules/production_readiness_gate.yaml`
- Examples:
  - `../agent-build-managed-agentops/assets/examples/golden-path/08-sandbox-prototype-evidence.yaml`
  - `../agent-build-managed-agentops/assets/examples/golden-path/10-pilot-launch-gate.yaml`
  - `../agent-build-managed-agentops/assets/examples/golden-path/11-production-readiness-gate.yaml`

## Workflow

1. Confirm the phase boundary, approved behavior level, allowed users, allowed data classes, tools, environments, owners, and evidence store.
2. Treat sandbox, pilot, and production as separate gates. Passing one gate never implies the next gate is passed.
3. Require evidence from actual runs for each environment: run traces, eval results, human review records, tool-call logs, control decisions, feedback, open defects, and stop-condition review.
4. Verify that every deviation from approved design has a severity, owner, decision, due date, and return-to-method assessment.
5. Verify support readiness: user instructions, operator run card, incident channel, daily owner, escalation path, feedback triage, and revocation owner.
6. Verify monitoring readiness: pilot dashboard, alert routing, metric thresholds, daily/weekly review cadence, source freshness checks, and cost/latency visibility.
7. Rehearse incident response before production readiness: pause, revoke access, disable feature flag, rollback release, notify owners, preserve evidence, and restart only after approval.
8. Complete the phase checklist, apply the rubric, update output contracts, and record unresolved gaps as blockers or approved conditions.

## Phase 8 Output Rules

Produce sandbox evidence through:

- `environment_progression_gate`
- `release_version_manifest`

Sandbox evidence must include test-data lineage, environment isolation, allowed tool scopes, build version, prompt/model/tool versions, eval and adversarial results, run traces, control-denial evidence, defect log, deviation log, rollback package, and owner decision.

Block phase exit when:

- Sandbox uses unapproved live data, unapproved access, unregistered tools, or production secrets.
- Prototype deviations lack owner approval and return-to-method assessment.
- Any blocking eval, control, trace, permission, or rollback test fails.
- Sandbox success is described as production readiness instead of sandbox evidence.

## Phase 10 Output Rules

Produce:

- `pilot_launch_gate`
- initial `agentops_operating_record` evidence or references

The pilot gate must include named pilot users, entry/exit dates, volume caps, allowed behaviors, prohibited behaviors, adoption and training evidence, human-review workflow, feedback channels, support rota, monitoring cadence, alert thresholds, stop conditions, value metrics, daily review owner, and rollback/revocation controls.

Block pilot launch when:

- Pilot user roster, support model, feedback channel, daily monitoring owner, stop condition, or user communication is missing.
- Pilot success metrics cannot be measured from traces, reviews, or business-system evidence.
- Users can trigger behavior outside the approved first behavior.
- Incident channel or feature pause path has not been tested.

## Phase 11 Output Rules

Produce:

- `production_readiness_gate`

Production readiness must be based on pilot evidence, not intent. Require pilot metric results, incident and defect history, residual-risk acceptance, owner signoffs, access review, trace and alert proof, support model, source freshness checks, cost/latency review, incident rehearsal, revocation readiness, rollback plan, release candidate manifest, and first-month monitoring cadence.

Block production readiness when:

- Any pilot exit threshold failed without approved remediation and retest.
- Incident rehearsal failed pause, revoke, rollback, evidence capture, or communication.
- Residual risk, access review, monitoring, revocation, support, or production owner signoff is missing.
- Production scope exceeds the pilot-approved behavior without change review.

## Output Contracts

- `agentops_operating_record`
- `environment_progression_gate`
- `pilot_launch_gate`
- `production_readiness_gate`
- `release_version_manifest`

Use the templates as machine-readable contracts. Preserve additional local fields if they strengthen implementation evidence and remain compatible with the shared schema.

## Quality Bar

Do not promote from sandbox to pilot or pilot to production unless evidence exists for real runs, controls, monitoring, owners, users, support, incident response, revocation, rollback, and value tracking. Treat vague success claims, unowned defects, untested pauses, and unmeasured adoption as blockers.
