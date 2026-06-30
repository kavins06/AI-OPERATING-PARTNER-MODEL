# Internal Operator Run Card

Use one card per live or pilot agent release. Keep it current enough that a backup operator can assess health, pause, revoke, escalate, route to manual fallback, and record evidence without reading the full contract set first.

## Agent

- Agent ID:
- Agent name:
- Current release version:
- Environment:
- Authorized behavior level:
- Live workflow boundary:
- Current status:
- Operating record:
- Release manifest:
- Production readiness gate:

## Approved Scope

- Approved user groups:
- Approved sources:
- Approved systems:
- Approved tools:
- Approved data classes:
- Approved output channels:
- Scale or volume limits:
- Explicitly prohibited:
- Material change rule: Any new user, source, tool, workflow, data class, output channel, write/send action, model autonomy, or behavior level requires Phase 14 review before use.

## Owners

- Executive sponsor:
- Business owner:
- Product owner:
- Technical owner:
- AgentOps owner:
- Support owner:
- Security/risk owner:
- Data owner:
- Revocation owner:
- Primary escalation channel:
- Backup owner coverage:
- Coverage gaps:

## Daily Checks

- Blocking alerts:
- Critical or high incidents:
- Untraced runs:
- Unauthorized tool/source/user/action attempts:
- Quality metric status:
- Control/guardrail status:
- Trace and audit-log status:
- Source freshness status:
- Cost/latency status:
- User feedback or correction status:
- Open incidents:

## Weekly Review

- Owner coverage confirmed:
- Quality, safety, reliability, adoption, value, and cost metrics reviewed:
- Source freshness and owner attestation reviewed:
- Access, service account, connector, and tool credential changes reviewed:
- Guidance, prompt, model, runtime, eval, and runbook changes reviewed:
- Incidents, near misses, manual overrides, and support themes reviewed:
- Value realization compared to baseline:
- Stop conditions evaluated:
- Next actions and owners assigned:

## Monthly Review

- Formal access attestation completed:
- Source owners attested current authoritative sources:
- Value realization, support burden, and operating cost reviewed:
- Owner coverage and backup coverage reviewed:
- Revocation mechanism rehearsal or evidence reviewed:
- Retirement or redesign triggers evaluated:
- Open Phase 14 or Phase 15 reviews reconciled:

## Blocking Conditions

- Unauthorized write, send, delete, permission change, workflow progression, user expansion, source use, tool call, or behavior-level escalation.
- Critical or high severity incident.
- Any production run without required trace or audit-log evidence.
- Source freshness SLA missed for source used in output without safe fallback.
- Required owner or revocation owner unavailable for active operating window.
- Control violation, privacy/security concern, or unresolved access exception.
- Quality, safety, reliability, or value metric crosses blocking threshold.
- Sponsor, business owner, security owner, or risk owner requests pause.

## Immediate Actions

- Pause mechanism:
- Tool or credential revocation mechanism:
- User entitlement revocation mechanism:
- Feature flag or route disablement:
- Queued work stop method:
- Rollback release:
- Human review fallback:
- Manual process fallback:
- User communication owner:
- Incident record path:
- Evidence retention path:

## Incident Severity Short Form

- Critical: Unauthorized production action, sensitive data exposure, systemic incorrect output, control bypass, or legal/compliance issue. Revoke affected capability immediately.
- High: Repeated unsafe output, failed human review path, incorrect tool invocation, material user impact, or monitoring gap. Pause affected workflow or tool.
- Medium: Isolated quality issue, recoverable integration failure, stale source with safe fallback, or minor scope drift. Contain and remediate before expansion.
- Low: Usability issue, non-blocking telemetry gap, documentation defect, or support theme. Track in weekly review.

## Review Cadence

- First-month review cadence:
- Stabilized review cadence:
- Daily monitoring owner:
- Weekly review owner:
- Monthly access review owner:
- Source freshness cadence:
- Eval refresh cadence:
- Model/prompt/runtime review cadence:
- Revocation rehearsal cadence:
- Next scheduled review:

## Example Stop Decision

If a draft-and-flag revenue intake agent uses a CRM field dictionary that is 13 days old against a 7-day freshness SLA, pause drafts that depend on that dictionary, route those records to manual review, notify the data owner and AgentOps owner, attach trace and source evidence, and open Phase 14 review if the source model changed.
