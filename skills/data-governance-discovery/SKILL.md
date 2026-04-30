---
name: data-governance-discovery
description: "Discover and document data governance requirements including source of record, owners, stewards, definitions, data quality, access rights, retention, lineage, lifecycle rules, and agent permission boundaries. Use before analytics, dashboards, integrations, automation, or AI agents rely on organizational data."
---

# Data Governance Discovery

## Core Rule

No trusted analytics or AI agent exists without clear ownership, definitions, quality rules, access boundaries, and escalation paths.

Useful references:

- `../../mastery-reference/information-management/operator-toolkit/data-governance-discovery-form.md`
- `../../mastery-reference/analytics/artifacts/governance_privacy_checklist.md`
- `../../mastery-reference/information-management/concept-library/concepts.md`

## Governance Areas

Capture:

- Source of record.
- Data owner.
- Data steward.
- Users and roles.
- Update frequency.
- Sensitive data.
- Data-quality issues.
- Metric and field definitions.
- Access rights.
- Retention and deletion rules.
- Lineage and transformation steps.
- Exception and approval rights.
- Agent read/write/summarize/send permissions.

## How To Get Inputs

Collect governance inputs from multiple layers:

- Executive: data risk tolerance, regulatory exposure, decision rights.
- Manager: operational ownership and escalation paths.
- Operator/admin: actual data entry, corrections, duplicates, shadow spreadsheets.
- IT/data/security: systems, integrations, permissions, logs, retention, export/API access.
- Documents: data dictionaries, reports, access matrices, policies, system exports, issue logs.

Use AI-led interviews adaptively: drill down whenever someone says "the system," "the spreadsheet," "usually," "I just know," or "we check manually."

## Discovery Questions

Ask:

- Which system or document is authoritative?
- Who can approve a definition?
- Who fixes missing, stale, duplicated, or contradictory data?
- What data can be read, changed, summarized, exported, or sent?
- What data must never leave the system?
- What fields are sensitive?
- What quality checks are required before output reaches another person?
- What audit trail is needed?
- Who approves exceptions?

## Source Inventory Template

| Source | Location/System | Owner | Steward | Users | Refresh | Sensitive Data | Quality Issues | Agent Permissions |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## Governance Outputs

Deliver:

- Source-of-record map.
- Stewardship assignments.
- Data dictionary needs.
- Metric definition needs.
- Access matrix.
- Data-quality rules.
- Retention and audit requirements.
- Agent permission boundaries.
- Open governance decisions.

## Stop Conditions

Do not move to build-ready status when:

- No source of record exists.
- No owner can approve definitions.
- Sensitive data lacks handling rules.
- Quality issues are known but unowned.
- Agent permissions would inherit broad user access by default.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

