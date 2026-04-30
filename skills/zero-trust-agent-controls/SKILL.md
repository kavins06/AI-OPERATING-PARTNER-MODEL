---
name: zero-trust-agent-controls
description: "Design zero-trust control models for AI agents, automation, analytics tools, and data workflows, including least privilege, scoped credentials, identity, device, application, data, network, automation, visibility, approval gates, logging, and revocation. Use before granting agents access or action rights."
---

# Zero Trust Agent Controls

## Core Rule

Do not let agents inherit broad human access by default. Grant scoped, task-specific, observable, revocable permissions.

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
- Network/environment: allowed systems, boundaries, segmentation.
- Automation/orchestration: tool calls, write actions, approval gates.
- Visibility/analytics: logs, alerts, monitoring, review.

## How To Get Inputs

Collect:

- Proposed agent capabilities and tool calls.
- Users, roles, and approval authority.
- Source systems, APIs, documents, and data classifications.
- Allowed and forbidden actions from workflow owners.
- Sensitive-data handling from risk/security stakeholders.
- Logging, monitoring, retention, and incident requirements.
- Validation-call decisions about what should never be automated.

Derive controls from actual agent behavior, not generic access roles.

## Permission Model

Define for each agent:

- Allowed users.
- Allowed sources.
- Allowed records or scopes.
- Allowed actions: read, summarize, draft, calculate, route, write, send.
- Forbidden actions.
- Human approval thresholds.
- Credential owner.
- Audit fields.
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

## Stop Conditions

Stop or redesign when:

- Agent uses full user account permissions.
- Sensitive data is not classified.
- External output lacks approval.
- Writes are silent.
- Logs omit source, tool, action, or approval.
- There is no revocation or incident path.

## Output

Deliver:

- Permission boundary.
- Control matrix.
- Approval model.
- Audit-log requirements.
- Revocation plan.
- Monitoring plan.
- Open security decisions.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

