# Managed AgentOps Weekly Review Checklist

Use this checklist for Section 2 Phase 13: `managed_agentops`. Run it weekly for every active pilot, controlled rollout, or production agent. During the first 30 days of production, also perform daily monitoring for blocking alerts, untraced runs, control violations, critical feedback, and source freshness failures.

## Inputs

- `managed_lifecycle_object`
- `measurement_intelligence`
- `ai_guidance_pack`
- `organizational_intelligence_baseline`
- `risk_control_model`
- `agent_build_contract`
- `release_version_manifest`
- `production_readiness_gate`
- `trace_observability_spec`
- `guardrail_control_matrix`
- `tool_contract_registry`
- `eval_harness_spec`

## Templates And Outputs

Templates:

- `skills/agent-build-managed-agentops/assets/templates/agentops-operating-record.yaml`
- `skills/agent-build-managed-agentops/assets/templates/internal-operator-run-card.md`
- `skills/agent-build-managed-agentops/assets/templates/incident-revocation-runbook.md`

Outputs:

- `agentops_operating_record`
- updated internal operator run card
- incident and open action updates

## Entry Checks

- Confirm Step 18 handoff, production readiness approval, release manifest, and operating record all identify the same agent, release, behavior level, environment, and owner model.
- Confirm required source inputs are approved, versioned, and linked as evidence, not merely named.
- Confirm the review owner, backup operator, approver, evidence location, and next review date.
- Confirm prior open actions, incidents, waivers, and blockers were either closed or carried forward with owner and due date.
- Confirm no Phase 14 or Phase 15 decision is pending that should pause routine operation.

## Scope Checks

- Confirm current users, workflows, systems, tools, sources, data classes, outputs, environments, scale limits, and behavior level match the approved handoff, production readiness gate, and release manifest.
- Confirm no write/send/autonomous action appears unless explicitly approved in the build contract, tool registry, guardrail matrix, and production readiness gate.
- Confirm all explicit exclusions remain visible in the run card and operating record.
- Confirm any detected scope drift has been paused or routed to Phase 14 before continued operation.

## Phase-Specific Checks

- Owner coverage: business, technical, security, data, risk/compliance, AgentOps, support, and revocation owners are named, reachable, and backed up for the active operating window.
- Live scope: users, workflow boundaries, sources, tools, data classes, outputs, scale limits, and behavior level match the approved handoff and release manifest.
- Operating metrics: quality, safety, reliability, adoption, value, cost, latency, and support metrics are reviewed against target, warning, and blocking thresholds.
- Source freshness: every authoritative source has owner attestation, freshness SLA, last verified date, stale action, and evidence. Stale sources used in outputs are paused or routed to human review.
- Access review: user entitlements, service accounts, tool credentials, connector scopes, secrets, and break-glass access are reviewed for drift, unused access, overbroad access, and revocation evidence.
- Guidance currency: AI guidance pack, prompts, retrieval corpus, policy references, eval datasets, run card, and incident runbook are current; material changes are routed to Phase 14.
- Incident review: incidents, near misses, manual overrides, user corrections, support tickets, control alerts, and audit gaps are classified and linked to decisions.
- Revocation readiness: pause, tool revocation, credential revocation, user entitlement removal, queued work stop, rollback, and manual fallback mechanisms are documented and recently tested or attested.
- Value tracking: realized value, human correction burden, support burden, operating cost, and adoption are compared to the Section 1 measurement baseline.
- Decision logging: continue, monitor, remediate, pause, change review, retirement/redesign review, or return-to-method decision is recorded with evidence.

## Monthly Add-On Checks

- Formal access attestation completed by security, data, tool, and business owners.
- Source owners attest that authoritative sources remain current, owned, and appropriate for agent output.
- Value realization is reviewed against the minimum viable value threshold and business case.
- Owner coverage, escalation channels, and backup coverage are checked for upcoming holidays, team changes, or support rotations.
- Revocation mechanism rehearsal is completed or prior rehearsal evidence is still inside its accepted window.
- Retirement or redesign triggers are evaluated and documented.

## Evidence Checks

- Attach dashboard, trace, audit log, eval, source, access review, incident, support, finance, and user feedback references for every material claim.
- Record missing evidence as a blocker or explicit owner-accepted waiver with expiry date.
- Confirm every unresolved deviation has an owner, due date, decision date, and stop condition.
- Confirm all access changes and revocations include before state, after state, actor, timestamp, and validation evidence.

## Blocking Conditions

- Any unauthorized write, send, delete, permission change, workflow progression, user expansion, source use, tool call, output channel, or behavior-level escalation.
- Any critical or high severity incident, privacy/security exposure, control bypass, or unresolved access exception.
- Any production run without required trace, tool-call audit log, source evidence, or approval record.
- Required owner coverage is missing, or revocation owner cannot execute within the response SLA.
- Source freshness SLA is missed for a source used in output and no approved safe fallback exists.
- Quality, safety, reliability, adoption, value, cost, or support metric crosses a blocking threshold.
- Business value is below minimum viable threshold for two consecutive review cycles.
- Agent behavior, source, tool, model, access, or workflow no longer matches the approved handoff.
- Sponsor, business owner, security owner, risk owner, or data owner requests pause.

## Exit Checks

- `agentops_operating_record` and run card are updated.
- Review decision and next review date are recorded.
- All stop conditions are evaluated.
- Phase 14 or Phase 15 referrals are opened where required.
- Rubric criteria are passed, waived by authorized owner with expiry, or marked blocked.
- Required owners accepted the review outcome.

## Realistic Examples

- Source freshness: CRM field dictionary is 13 days old against a 7-day SLA. Pause drafts that cite CRM field requirements, route affected records to manual review, notify the data owner, and open Phase 14 if the source model changed.
- Access drift: a departed pilot user remains in the agent access group. Revoke access, record before and after evidence, confirm no runs occurred after departure, and review group ownership.
- Value trigger: the agent saves 3 hours per week but creates 5 hours of correction effort for two weeks. Open Phase 15 retirement or redesign review.

## Failure Modes

- Live operation lacks owner coverage, metric review, source freshness, cost review, access review, incident handling, or guidance update cadence.

## Return-To-Method Triggers

- Operating metrics show value, risk, source, ownership, or adoption assumptions are invalid.
