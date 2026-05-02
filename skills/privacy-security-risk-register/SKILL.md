---
name: privacy-security-risk-register
description: "Create the Step 15 implementation-grade risk_control_model for privacy, security, compliance, operational, vendor, output-quality, data-handling, truth-production, regulated-domain, adoption, and AI-agent risks before implementation."
---

# Privacy Security Risk Register

## Core Rule

Make risk visible, owned, and testable before deployment. Current legal, regulatory, privacy, cybersecurity, and vendor claims must be verified against current official sources before client-facing use.

Inside the AI operating partner engagement, this is part of Step 15: the risk and control model. It is not only a risk register. It must translate workflow, data, guidance, measurement, value, adoption, regulated-domain, and technical blueprint evidence into concrete protocols for future permissions, outputs, approvals, logging, monitoring, incident response, revocation, and stop conditions. It does not provision access, deploy monitoring, or implement controls.

## Engagement Role

Step 15 produces the `risk_control_model`, risk register, data classification, tool permission matrix, output controls, stop conditions, and Step 15-to-Step 13 loop decision. Risk can force solution-shape redesign before readiness scoring.

Use these canonical templates:

- `../ai-operating-partner-engagement/assets/templates/13-risk-control-model.yaml`
- `../ai-operating-partner-engagement/assets/templates/13-risk-register.csv`

When a regulated-domain extension applies, load the extension requirements and name the specific owner-confirmed rules, prohibited AI behaviors, required human review, required evidence, and lifecycle implications.

Useful references:

- `../../mastery-reference/information-management/operator-toolkit/privacy-security-risk-register.md`
- `../../mastery-reference/analytics/artifacts/governance_privacy_checklist.md`
- `../../mastery-reference/information-management/concept-library/frameworks.md`
- `../../mastery-reference/information-management/operator-toolkit/privacy-security-risk-register.md`

## Risk Categories

Consider:

- Overbroad access.
- Sensitive data in prompts, logs, exports, or training sets.
- Unauthorized sharing.
- Missing retention/deletion rules.
- Hallucinated policy, contract, or factual claims.
- Incorrect external communication.
- Missing audit trail.
- Vendor or integration risk.
- Model or tool outage.
- Data-quality failure.
- Spreadsheet, macro, or shadow-reporting risk.
- Key-person truth dependency.
- Undocumented transformation or manual-adjustment risk.
- Low auditability or not-reproducible truth production.
- Legal, regulatory, or compliance exposure.
- Named regulated-domain exposure such as Fair Housing, TCPA, RESPA/referrals, MLS/IDX/VOW data-use rules, and state advertising/licensure rules for real estate when applicable.
- Adoption, incentive, or end-user misuse risk.
- Security incident response gaps.
- Missing revocation path.
- Tool permission mismatch.
- Output without citation, confidence, or uncertainty language.
- Broad user-account inheritance.

## How To Get Inputs

In the AI operating partner engagement, use prior outputs first:

- Step 6 workflow actions, decisions, approval gates, edge cases, and failure modes.
- Step 7 diagnostic findings and automation blockers.
- Step 8 sensitive fields, source constraints, retention/export limits, permitted AI actions, and governance decisions.
- Step 10 AI guidance packs, forbidden behaviors, escalation triggers, output contracts, and test/evaluation cases.
- Step 11 trusted/disputed measurements, AI-capability metrics, and agent-safe metric usage.
- Truth production profiles and fragile truth statuses.
- Step 12 business value case and risk tolerance implied by the value case.
- Step 13 solution shape and adoption design.
- Step 14 technical implementation blueprint: systems, access paths, future tools/MCPs/connectors, document/email scope, credential/secrets approach, audit/logging, test strategy, blocked paths, and build sequence.
- Regulated-domain extension, if applicable.
- Existing policies: access, retention, incident response, data processing, acceptable use.
- Targeted confirmations from risk, security, legal, compliance, IT/data, and business owners.

Use current official sources for unstable legal, regulatory, privacy, security-standard, and vendor claims.

## Protocol Derivation

Derive controls from evidence:

- Future AI behavior implies tool/action permissions.
- Sensitive data implies classification, redaction, retention, export, and logging rules.
- Forbidden behavior implies prohibited tool actions and output controls.
- Disputed or conditionally trusted measurements imply human review or uncertainty language.
- Shadow-derived, manually adjusted, person-dependent, disputed, missing, or not-reproducible truth implies safe-use limitation, remediation, or stop condition.
- External communication implies approval gates, content restrictions, audit trail, and incident path.
- Write-back implies stronger approval, rollback, logging, and revocation controls.
- Broad access implies narrowing scope or redesign.
- No audit logging, no revocation path, or no owner implies an implementation stop condition.

## Risk Register Template

| Risk ID | Category | Linked Object | Linked Tool/Source/Truth Profile | Impact | Likelihood | Severity | Control | Owner | Status | Verification Needed | Residual Risk | Blocks Readiness |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

## Control Prompts

Ask:

- What sensitive data is involved?
- Who should access it?
- What should be redacted?
- What must be logged?
- What external outputs require approval?
- What data can be retained and for how long?
- What vendor or model receives the data?
- What happens when a tool, model, or source fails?
- What current laws, policies, standards, or contracts must be checked?
- What spreadsheet, macro, manual adjustment, reconciliation, or person-dependent truth chain could create risk?
- Can the truth be reproduced and audited before AI relies on it?
- Which future tool action does this risk affect?
- What output must be prohibited or approval-gated?
- What must be logged and reviewed?
- Who can revoke access and how fast?

## Output

Deliver:

- Risk and control model.
- Data classification matrix.
- Risk register.
- Truth production controls.
- Tool-level permission matrix.
- Output controls.
- Human approval gates.
- Logging and monitoring requirements.
- Incident response path.
- Revocation model.
- Critical stop conditions.
- Required controls.
- Owners.
- Current verification list.
- Residual risk after controls.
- Recommended go/no-go posture.

## Quality Bar

Do not bury high-impact risks in prose. Put them in the model with owner, control, verification status, residual risk, and stop-condition status.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

