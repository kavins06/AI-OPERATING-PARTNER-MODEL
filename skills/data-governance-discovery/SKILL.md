---
name: data-governance-discovery
description: "Discover and document data governance requirements including source of record, source access paths, owners, stewards, definitions, data quality, access rights, retention, lineage, lifecycle rules, and agent permission boundaries. Use before analytics, dashboards, integrations, automation, or AI agents rely on organizational data."
---

# Data Governance Discovery

## Core Rule

No trusted analytics or AI agent exists without clear ownership, definitions, quality rules, access boundaries, and escalation paths.

Inside the AI operating partner engagement, use this skill as an embedded Step 7 helper, not as a separate broad discovery cycle. Governance questions should be object-driven: start from information objects, source access profiles, sources, systems, decisions, sensitive fields, and permission gaps already found in the AI workflow specification and diagnostic.

Useful references:

- `../../mastery-reference/information-management/operator-toolkit/data-governance-discovery-form.md`
- `../../mastery-reference/analytics/artifacts/governance_privacy_checklist.md`
- `../../mastery-reference/information-management/concept-library/concepts.md`

## Governance Areas

Capture:

- Source of record.
- Practical source access path.
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

Start from the organizational intelligence object:

- AI workflow specification.
- Organizational intelligence diagnostic.
- Validation events.
- Planning-evidence follow-up results.
- Source inventory.
- Information object and source access profile register.
- Existing access matrices, policies, redacted system exports, data dictionaries, schema/field lists, API/vendor docs, or issue logs if approved as planning evidence.

Do not reinterview multiple layers by default. Route each unresolved object to the smallest authorized resolver group:

- Business owner for source-of-record, definition, exception, and approval decisions.
- Steward or operator only when actual correction, quality, or shadow-tracker behavior is still unknown.
- IT/data/security for system, integration, access, export, logging, retention, and permission reality.
- Risk/legal/compliance only for sensitive data, external sharing, contractual, regulatory, or reputational boundaries.

Use AI-led follow-up only when the object cannot be resolved from current evidence or an authorized owner needs a narrow decision prompt.

## Discovery Questions

Ask:

- Which system or document is authoritative?
- Which practical access path, report, module, dashboard, folder, lookup key, or required field is correct?
- Who can approve a definition?
- Who fixes missing, stale, duplicated, or contradictory data?
- What data can be read, changed, summarized, exported, or sent?
- What data must never leave the system?
- What fields are sensitive?
- What quality checks are required before output reaches another person?
- What audit trail is needed?
- Who approves exceptions?

## Source Inventory Template

| Source ID | Linked Information Objects | Linked Workflow Objects | Source | Location/System | Module/Report/Path | Lookup Keys | Source-of-Record Status | Owner | Steward | Sensitive Data | Quality Issues | Retention/Handling | Allowed AI Actions | Prohibited AI Actions | Validation Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | authoritative / disputed / not_authoritative | | | | | | read / summarize / compare / draft | send_external / write_back | pending / resolved / disputed |

## Governance Outputs

Deliver:

- Source-of-record map.
- Source access profile confirmations.
- Stewardship assignments.
- Data dictionary needs.
- Metric definition needs.
- Access matrix.
- Data-quality rules.
- Retention and audit requirements.
- Agent permission boundaries.
- Open governance decisions.
- Structured governance resolution events linked to workflow-spec object IDs.
- Future implementation access requirements, when live access or credentials will be needed after Step 16.

## Stop Conditions

Do not move to implementation-ready status when:

- No source of record exists.
- Practical access path is unknown for a source the agent must rely on.
- No owner can approve definitions.
- Sensitive data lacks handling rules.
- Quality issues are known but unowned.
- Agent permissions would inherit broad user access by default.
- The engagement would require credentials, broad live access, or bulk unredacted data before Step 16 approval.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

