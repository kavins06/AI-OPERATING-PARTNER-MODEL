# Controlled Pilot Checklist

Use this checklist for Section 2 phase 10: `controlled_pilot`.

## Inputs

- `managed_lifecycle_object`
- `adoption_design`
- `measurement_intelligence`
- `risk_control_model`

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/pilot-launch-gate.yaml`
- `skills/agent-build-managed-agentops/assets/templates/agentops-operating-record.yaml`

Outputs:

- `pilot_launch_gate`
- `agentops_operating_record`

## Entry Checks

- Confirm sandbox exit is approved and cited.
- Confirm eval, guardrail, observability, release candidate, support, and rollback artifacts are available.
- Confirm pilot scope remains equal to or narrower than the approved handoff.
- Confirm pilot users, daily owner, support owner, security owner, business owner, and AgentOps owner are named.
- Confirm pilot launch is limited by time, users, volume, behavior, tools, sources, and environment.

## Scope Checks

- Confirm pilot scope is equal to or narrower than approved Step 17/18 scope and sandbox-tested scope.
- Confirm pilot user roster, tools, sources, data classes, outputs, volume caps, and environment are explicitly limited.
- Confirm prohibited behaviors remain visible in user communication, controls, monitoring, and stop conditions.
- Confirm any pressure to expand users, tools, sources, volume, behavior level, or output types is routed to change review or return-to-method.

## Phase-Specific Checks

- Name pilot users or roles, onboarding status, training/comms evidence, and opt-in/mandate reality.
- Define allowed behaviors, prohibited behaviors, source/tool/data limits, output limits, and daily volume caps.
- Define measurable pilot success thresholds for task success, material error, human correction, acceptance/adoption, cycle time, control violations, and untraced runs.
- Verify human review is staffed and records reviewer identity, decision, edits, reason, and timestamp.
- Verify feedback channels capture user corrections, safety concerns, workflow friction, and missing-guidance reports.
- Verify pilot dashboard and alerts are live before first user run.
- Define daily review cadence, owner, agenda, evidence location, and escalation process.
- Define stop conditions for control violation, untraced run, successful adversarial attack, material error threshold breach, support gap, or scope pressure.
- Test incident channel, feature pause, tool disablement, credential revocation, and rollback before launch.
- Define pilot exit criteria and production-readiness evidence expectations before pilot starts.

## Evidence Checks

- Attach pilot roster and user communication/training evidence.
- Attach sandbox exit approval, release candidate manifest, and rollback package.
- Attach dashboard and alert proof.
- Attach human-review workflow test.
- Attach pilot metric definitions and source systems.
- Attach support rota, incident channel, and feedback triage evidence.
- Attach stop-condition approval by business, security, and AgentOps owners.

## Exit Checks

- `pilot_launch_gate` has a go/hold/conditional decision with approvers.
- Initial `agentops_operating_record` evidence location is ready for daily pilot review.
- Pilot monitoring and feedback process is live.
- Pilot exit criteria are measurable from traces, reviews, feedback, and business-system evidence.
- Return-to-method triggers have been evaluated and recorded.

## Blocking Conditions

- Pilot audience, support model, feedback channel, daily monitoring owner, or stop condition is missing.
- Pilot success metrics cannot be measured.
- Users can trigger behavior outside approved scope.
- Human-review, incident, pause, revocation, or rollback paths are untested.
- Pilot dashboard or alert routing is not live.
- Pilot launch would use unapproved data, source, tool, permission, or environment.

## Failure Modes

- Pilot audience, support model, feedback channel, monitoring, or stop condition is missing.

## Return-To-Method Triggers

- Pilot reveals adoption, value, control, or truth assumptions were wrong.
- Pilot demand pressures the agent beyond approved behavior level, user group, tool, source, or oversight model.
