---
name: zero-trust-agent-controls
description: "Design zero-trust control models for AI agents, automation, analytics tools, and data workflows, including least privilege, scoped credentials, identity, device, application, data, network, automation, visibility, approval gates, logging, and revocation. Use before granting agents access or action rights."
---

# Zero Trust Agent Controls

## Core Rule

Do not let agents inherit broad human access by default. Grant scoped, task-specific, observable, revocable permissions.

Inside the AI operating partner engagement, this skill designs the Step 13 zero-trust portion of the future risk and control model only. Do not provision credentials, service accounts, live API tokens, MCP access, connectors, email ingestion, monitoring, or write access during the 16-step engagement.

Useful references:

- `../../mastery-reference/information-management/concept-library/frameworks.md`
- `../../mastery-reference/information-management/operator-toolkit/privacy-security-risk-register.md`
- `../../mastery-reference/information-management/operator-toolkit/privacy-security-risk-register.md`

## Control Domains

Design controls across:

- User: identity, role, approval authority.
- Device: endpoint posture when relevant.
- Application/workload: agent, tools, APIs, jobs.
- Data: classification, row/field/document access, retention.
- Truth production: allowed uses of shadow-derived, manually adjusted, person-dependent, disputed, missing, or not-reproducible truth.
- Network/environment: allowed systems, boundaries, segmentation.
- Automation/orchestration: tool calls, write actions, approval gates.
- Visibility/analytics: logs, alerts, monitoring, review.

## How To Get Inputs

Collect:

- Proposed agent capabilities and tool calls.
- Proposed MCPs, connectors, normalization jobs, email connectors, and integration paths from the architecture blueprint.
- Users, roles, and approval authority.
- Source systems, APIs, documents, and data classifications.
- Allowed and forbidden actions from workflow owners.
- Sensitive-data handling from risk/security stakeholders.
- Logging, monitoring, retention, and incident requirements.
- Validation-call decisions about what should never be automated.
- Planning evidence access boundaries and future implementation access requests.
- Step 9 guidance packs with forbidden behaviors and output contracts.
- Step 10 metric trust and agent-safe metric usage.
- Truth production profiles, fragile truth statuses, and AI-safe truth usage.
- Step 13 risk register and data classification.

Derive controls from actual agent behavior, not generic access roles.

## Permission Model

Define for each agent:

- Allowed users.
- Allowed sources.
- Allowed records or scopes.
- Field-level restrictions.
- Document-level restrictions.
- Allowed actions: read, summarize, draft, calculate, route, write, send.
- Allowed truth behaviors: summarize, compare, flag uncertainty, draft question, escalate, calculate, cite, recommend, decide.
- Forbidden actions.
- Human approval thresholds.
- Credential owner.
- Audit fields.
- Monitoring and alert conditions.
- Revocation process.
- Incident path.

## Agent Control Matrix

| Capability | Allowed? | Scope | Approval | Log Required | Owner |
|---|---|---|---|---|---|
| Read data | | | | | |
| Retrieve documents | | | | | |
| Run calculations | | | | | |
| Draft output | | | | | |
| Send externally | | | | | |
| Write to system | | | | | |
| Trigger workflow | | | | | |

## Output Controls

Define:

- Allowed outputs.
- Prohibited outputs.
- Citation or evidence requirements.
- Confidence requirements.
- Uncertainty language.
- External-send approval requirements.
- Prohibited claims, instructions, or recommendations.

## Revocation And Incident Controls

Define:

- Who can revoke access.
- Revocation triggers.
- Expected time to revoke.
- Scope revoked: user, role, source, tool, service account, connector, or workflow.
- Incident owner.
- Escalation path.
- Containment actions.
- Restoration conditions.

## Stop Conditions

Stop or redesign when:

- Agent uses full user account permissions.
- Sensitive data is not classified.
- External output lacks approval.
- Writes are silent.
- Logs omit source, tool, action, or approval.
- There is no revocation or incident path.
- Output controls do not prevent prohibited claims, sends, approvals, or write actions.
- Fragile truth would be used for final decisions, autonomous action, or unqualified recommendations.

## Output

Deliver:

- Permission boundary.
- Control matrix.
- Data-access and field/document restrictions.
- Tool-level permission matrix.
- Output controls.
- Approval model.
- Audit-log requirements.
- Monitoring and alert requirements.
- Incident response path.
- Revocation plan.
- Monitoring plan.
- Open security decisions.
- Future provisioning prerequisites.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

