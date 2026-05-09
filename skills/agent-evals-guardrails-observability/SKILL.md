---
name: agent-evals-guardrails-observability
description: "Design implementation-grade eval suites, guardrail controls, security-control evidence, trace policy, dashboards, alerting, and incident rehearsal for Section 2 phases 7 and 9. Use after approved Step 18 handoff and separate implementation approval as part of the Section 2 build and Managed AgentOps backbone."
---

# Agent Evals Guardrails Observability

## Boundary

Use this skill only inside Section 2 after Step 18 handoff approval and separate implementation approval. Do not backfill missing Section 1 decisions here.

Own only:

- Phase 7: Eval And Guardrail Design.
- Phase 9: Security And Control Review.

Stop and return to the `agent-build-managed-agentops` orchestrator when the request needs sandbox execution, pilot, production readiness, release packaging, operating review, change control, expansion, retirement, or other phases outside this skill.

Stop and return to the Section 1 method owner when the approved handoff is missing, contradicted, or invalidated by eval results, control design, source drift, unsupported behavior, or security findings.

## Required Inputs

Read the handoff map before producing outputs:

- `../agent-build-managed-agentops/assets/mappings/section1-to-section2-handoff-map.yaml`

Use these Section 1 inputs across the owned phases:

- `ai_guidance_pack`
- `managed_lifecycle_object`
- `measurement_intelligence`
- `readiness_object`
- `risk_control_model`
- `technical_blueprint`

Treat every input as invalid until it is approved, versioned, and cited with evidence. Record draft or missing inputs as blockers.

## Owned Phases

- Phase 7: Eval And Guardrail Design.
- Phase 9: Security And Control Review.

## Resource Map

- Local phase packs: `assets/phase-packs`
- Templates:
  - `../agent-build-managed-agentops/assets/templates/eval-and-validation-plan.yaml`
  - `../agent-build-managed-agentops/assets/templates/guardrail-control-matrix.yaml`
  - `../agent-build-managed-agentops/assets/templates/trace-observability-spec.yaml`
- Checklists:
  - `../agent-build-managed-agentops/assets/checklists/eval-guardrail-design-checklist.md`
  - `../agent-build-managed-agentops/assets/checklists/security-control-review-checklist.md`
- Rubrics:
  - `../agent-build-managed-agentops/assets/rubrics/eval-guardrail-launch-rubric.yaml`
  - `../agent-build-managed-agentops/assets/rubrics/security-control-review-rubric.yaml`
- Validator rules:
  - `../agent-build-managed-agentops/assets/validator-rules/eval_and_guardrail_design.yaml`
  - `../agent-build-managed-agentops/assets/validator-rules/security_and_control_review.yaml`
- Examples:
  - `../agent-build-managed-agentops/assets/examples/golden-path/07-eval-harness-and-guardrails.yaml`
  - `../agent-build-managed-agentops/assets/examples/golden-path/09-security-control-review.yaml`

## Workflow

1. Confirm the approved Step 17/18 scope, behavior level, authorized users, sources, tools, environments, owner model, and prohibited behaviors.
2. Build eval coverage from behavior requirements, guidance rules, source truth rules, business metrics, risk controls, tool contracts, and failure modes.
3. Define behavior-level eval sets before implementation promotion:
   - golden set for expected successful tasks.
   - edge set for ambiguous, incomplete, stale, conflicting, and exception-path inputs.
   - adversarial set for prompt injection, permission pressure, data exfiltration, unsupported action, policy conflict, and unsafe escalation.
   - regression set for every prior defect, incident, owner override, and release-blocking issue.
4. Set blocking thresholds, sample sizes, reviewer roles, calibration rules, and promotion gates for offline, sandbox, pilot, and production.
5. Map every risk to preventive, detective, corrective, revocation, and human-review controls where applicable.
6. Define trace fields, metric fields, alert thresholds, dashboard audiences, retention, redaction, and log access roles.
7. Rehearse at least one control failure and one revocation/rollback path before approving security control review.
8. Complete the phase checklist, apply the rubric, update output contracts, and record unresolved gaps as blockers or approved conditions.

## Phase 7 Output Rules

Produce or update:

- `eval_harness_spec`
- `guardrail_control_matrix`

The eval plan must include behavior-level test cases, adversarial tests, test data provenance, redaction status, reviewer calibration, automated and expert-review methods, blocking metrics, minimum sample sizes, and promotion thresholds.

The guardrail matrix must include risk-to-control traceability, fail-closed behavior, human review points, tool and permission controls, override policy, revocation controls, evidence requirements, and control-test frequency.

Block phase exit when:

- Any approved behavior lacks a golden, edge, adversarial, and regression coverage path.
- Any prohibited behavior lacks a blocking test or preventive control.
- Any write, send, external communication, data export, or privileged tool path lacks explicit approval and a fail-closed control.
- A blocking threshold, sample size, reviewer role, evidence reference, owner, or promotion criterion is missing.

Return to method when:

- Evals reveal missing guidance, unstable truth production, unowned source rules, unresolved data-quality issues, or scope/value assumptions that differ from the approved handoff.

## Phase 9 Output Rules

Produce or update:

- `guardrail_control_matrix`
- `trace_observability_spec`

The security review must prove that controls are implemented, tested, observable, reversible, and owned. Evidence must include permission-boundary tests, prompt-injection and data-exfiltration tests, tool-call denial tests, audit-log samples, dashboard screenshots or links, alert routing proof, incident rehearsal notes, access-review coverage, and residual-risk approval.

Block phase exit when:

- Residual risk lacks named owner approval.
- Trace coverage is not mandatory for every run and every tool call.
- A control failure cannot be detected, paused, escalated, and revoked within the stated SLA.
- Sensitive fields are logged without redaction or a retention/access policy.
- Incident rehearsal does not prove pause, revoke, rollback, evidence capture, and communication paths.

Return to method when:

- A required security control changes architecture, tool access, data path, behavior level, user group, oversight model, or production lifecycle assumptions.

## Output Contracts

- `eval_harness_spec`
- `guardrail_control_matrix`
- `trace_observability_spec`

Use the templates as machine-readable contracts. Preserve additional local fields if they strengthen implementation evidence and remain compatible with the shared schema.

## Quality Bar

Do not mark phases 7 or 9 passed unless required artifacts are approved, testable, observable, and traceable to owners and evidence. Treat missing thresholds, untested controls, unobserved tool calls, broad permissions, and convenience-driven scope expansion as defects.
