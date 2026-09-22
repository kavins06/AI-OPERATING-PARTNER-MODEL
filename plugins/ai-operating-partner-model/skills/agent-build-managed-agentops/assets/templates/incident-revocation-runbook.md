# Incident And Revocation Runbook

## Purpose

Use this runbook when an agent, tool, model behavior, data path, source, owner coverage gap, or operating control creates material risk, degraded quality, unauthorized action, privacy or security exposure, audit failure, or business harm. The default posture is pause first, preserve evidence, and restore only after accountable owners approve recovery.

## Incident Intake

- Incident ID:
- Detected at:
- Reported by:
- Agent ID:
- Release version:
- Environment:
- Affected users or groups:
- Affected workflows:
- Affected systems, tools, sources, and data classes:
- First known bad run:
- Last known bad run:
- Evidence location:

## Severity

| Severity | Definition | Default Action | Required Owners |
|---|---|---|---|
| Critical | Unauthorized production action, sensitive data exposure, systemic incorrect output, control bypass, legal/compliance issue, or inability to revoke. | Revoke affected capability immediately, stop queued work, escalate to executive, security, risk, technical, business, and AgentOps owners. | Executive sponsor, security owner, risk owner, business owner, technical owner, revocation owner. |
| High | Repeated unsafe output, failed human review path, incorrect tool invocation, material user impact, missing production trace, or monitoring gap affecting decisions. | Pause affected workflow, tool, source, or release and start incident review. | Business owner, technical owner, AgentOps owner, security owner, revocation owner. |
| Medium | Isolated quality issue, recoverable integration failure, stale source with safe fallback, or minor scope drift. | Contain, document, remediate, and block expansion until reviewed. | AgentOps owner, support owner, source or tool owner. |
| Low | Usability issue, non-blocking telemetry gap, documentation defect, or support trend. | Track in weekly operating review and fix through normal change control if material. | AgentOps owner, support owner. |

## Blocking Conditions

Pause or revoke before investigation continues when any of these are true:

- Unauthorized write, send, delete, approval, scheduling, routing, permission, or workflow progression occurred or was attempted.
- Sensitive data was exposed to an unauthorized user, model, tool, log, prompt, output channel, or downstream system.
- A production run is missing required trace, tool-call audit log, source citation, approval record, or redaction evidence.
- A source used in output is stale beyond SLA, disputed, unavailable, or no longer governed by its named owner.
- Required owner coverage is absent and the agent remains available to users.
- A guardrail, eval, human review, revocation, or access control was bypassed.
- The agent is operating outside approved users, workflow boundaries, tools, sources, data classes, environment, scale, output channel, or behavior level.
- Business, security, risk, or sponsor owner requests pause.

## Immediate Triage

1. Assign severity, incident commander, business owner, technical owner, security owner, AgentOps owner, support owner, and revocation owner.
2. Capture run traces, prompts, instructions, model config, retrieval references, tool invocation records, approvals, output artifacts, user feedback, source versions, access records, feature flags, deployment versions, and dashboard screenshots.
3. Determine blast radius across users, records, downstream systems, reports, decisions, queued work, cached outputs, and follow-up tasks.
4. Decide whether to pause the whole agent, one release, one user group, one workflow, one output channel, one source, one tool, or one credential.
5. Notify the required owners and record notification timestamps.

## Pause Or Revoke

1. Disable the affected feature flag, deployment route, schedule, queue consumer, model route, connector credential, tool contract, service account, user group, or entitlement.
2. Confirm queued, retrying, scheduled, or in-flight actions cannot continue after revocation.
3. Switch the operating record status to `paused`, `revoked`, or `degraded_mode` and record the exact scope paused.
4. Route users to the approved manual fallback or human review path.
5. Preserve evidence under the retention and redaction policy in the trace observability spec.
6. Record revocation evidence: actor, timestamp, target, before state, after state, validation check, and restoration approvers required.

## Investigation

1. Identify whether the failure came from source freshness, source authority, prompt or instruction drift, model behavior, eval gap, guardrail gap, tool contract gap, access gap, human review failure, user workflow condition, owner coverage gap, architecture assumption, or release packaging.
2. Compare actual behavior to approved Step 17/18 scope, production readiness conditions, release manifest, tool registry, and operating record.
3. Determine whether the issue requires Phase 14 change control, Phase 15 retirement/redesign review, or return to Section 1 method.
4. Document root cause, contributing factors, blast radius, user impact, business impact, data impact, corrective actions, owners, due dates, validation evidence, and communication needs.

## Recovery

1. Produce a fix, rollback, source update, access correction, or decommission package with release notes and validation results.
2. Re-run blocking evals, control tests, smoke tests, access checks, source freshness checks, trace checks, and audit-log checks.
3. Confirm owner coverage and support readiness for the restored scope.
4. Obtain explicit approval from required owners before restoring access.
5. Restore only the approved scope and record evidence in the operating record.
6. Open Phase 14 review if any tool, source, behavior, model, user group, owner model, or release contract changed.

## Post-Incident Review

1. Complete root-cause summary and user, business, risk, source, and cost impact assessment.
2. Add or update tests, alerts, runbook steps, controls, owner coverage, source freshness checks, access review checks, and user communications.
3. Decide whether to continue, limit, remediate, roll back, retire, redesign, or return to method.
4. Schedule follow-up review and verify all open actions are closed.

## Example

A coordinator reports that a draft-and-flag agent cited an intake requirement that was removed from the CRM field dictionary 10 days ago. The dictionary freshness SLA is 7 days. The operator pauses drafts that cite that dictionary, preserves traces and source versions, routes affected records to manual review, notifies the data owner, opens a medium incident, and starts Phase 14 if the source model changed.
