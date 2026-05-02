---
name: data-governance-discovery
description: "Discover and document Step 8 object-driven governance requirements including official sources, de facto trusted sources, truth production chains, source access paths, owners, stewards, definitions, data quality, access rights, retention, lineage, baseline release rules, lifecycle implications, and agent permission boundaries."
---

# Data Governance Discovery

## Core Rule

No trusted analytics or AI agent exists without clear ownership, definitions, truth production, quality rules, access boundaries, and escalation paths.

Inside the AI operating partner engagement, use this skill as an embedded Step 8 helper, not as a separate broad discovery cycle. Governance questions should be object-driven: start from information objects, source access profiles, truth production profiles, sources, systems, decisions, sensitive fields, and permission gaps already found in the Step 6 `workflow_intelligence_object` and Step 7 diagnostic.

## Engagement Role

Step 8 resolves controlled validation, governance, source access, truth production, and baseline-release decisions. It produces structured validation events and source/truth decisions that can update Step 6, re-score Step 7, revise Step 2, or seed the Organizational Intelligence Baseline.

Use these canonical method templates when formal output is needed:

- `../ai-operating-partner-engagement/assets/templates/07-source-inventory.csv`
- `../ai-operating-partner-engagement/assets/templates/07-validation-event.yaml`
- `../ai-operating-partner-engagement/assets/templates/07-controlled-validation-call-view.md`
- `../ai-operating-partner-engagement/assets/templates/07-organizational-intelligence-baseline.yaml`
- `../ai-operating-partner-engagement/assets/templates/07-baseline-release-contract.yaml`

Do not resolve governance by asking for broad data-room access. Use the smallest authorized owner group and the narrowest planning evidence needed for each unresolved object.

Useful references:

- `../../mastery-reference/information-management/operator-toolkit/data-governance-discovery-form.md`
- `../../mastery-reference/analytics/artifacts/governance_privacy_checklist.md`
- `../../mastery-reference/information-management/concept-library/concepts.md`

## Governance Areas

Capture:

- Official source.
- De facto trusted source.
- Truth production chain.
- Embedded formulas, macros, manual adjustments, reconciliations, or expert-memory rules.
- Reproducibility and auditability.
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
- Agent-safe truth usage.

## How To Get Inputs

Start from the organizational intelligence object:

- AI workflow specification.
- Organizational intelligence diagnostic.
- Validation events.
- Planning-evidence follow-up results.
- Source inventory.
- Information object and source access profile register.
- Truth production profile register.
- Existing access matrices, policies, redacted system exports, data dictionaries, schema/field lists, API/vendor docs, or issue logs if approved as planning evidence.

Do not reinterview multiple layers by default. Route each unresolved object to the smallest authorized resolver group:

- Business owner for official-source, de facto-source, truth-production, definition, exception, and approval decisions.
- Steward or operator only when actual correction, quality, truth production, or shadow-tracker behavior is still unknown.
- IT/data/security for system, integration, access, export, logging, retention, and permission reality.
- Risk/legal/compliance only for sensitive data, external sharing, contractual, regulatory, or reputational boundaries.

Use AI-led follow-up only when the object cannot be resolved from current evidence or an authorized owner needs a narrow decision prompt.

## Discovery Questions

Ask:

- Which system or document is official?
- Which source, report, spreadsheet, macro, or person is de facto trusted?
- How is the final number, status, report, or decision produced?
- Which formulas, macros, manual adjustments, reconciliations, or expert-memory rules matter?
- Is the truth chain documented, versioned, owned, reproducible, and auditable?
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

| Source ID | Linked Information Objects | Linked Workflow Objects | Linked Truth Profiles | Source | Location/System | Module/Report/Path | Lookup Keys | Official Source Status | De Facto Source Status | Truth Status | Owner | Steward | Sensitive Data | Quality Issues | Truth Production Issues | Retention/Handling | Allowed AI Actions | Prohibited AI Actions | Validation Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | authoritative / disputed / not_authoritative | | | | | | read / summarize / compare / draft | send_external / write_back | pending / resolved / disputed |

## Governance Outputs

Deliver:

- Official/de facto source map.
- Truth production profile map.
- Source access profile confirmations.
- Stewardship assignments.
- Data dictionary needs.
- Metric definition needs.
- Access matrix.
- Data-quality rules.
- Reproducibility and auditability gaps.
- Retention and audit requirements.
- Agent permission boundaries.
- Open governance decisions.
- Structured governance resolution events linked to workflow-spec object IDs.
- Future implementation access requirements, when live access or credentials will be needed after Step 18.

## Stop Conditions

Do not move to implementation-ready status when:

- No official source or de facto trusted source can be identified.
- Material truth is shadow-derived, manually adjusted, person-dependent, disputed, missing, or not reproducible without a safe-use limitation or remediation route.
- Practical access path is unknown for a source the agent must rely on.
- No owner can approve definitions.
- Sensitive data lacks handling rules.
- Quality issues are known but unowned.
- Agent permissions would inherit broad user access by default.
- The engagement would require credentials, broad live access, or bulk unredacted data before Step 18 approval.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

