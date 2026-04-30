---
name: privacy-security-risk-register
description: "Create privacy, security, compliance, operational, vendor, output-quality, and data-handling risk registers for data, analytics, automation, or AI-agent workflows. Use when Codex needs to identify risks, controls, owners, likelihood, impact, status, verification needs, and stop conditions before implementation."
---

# Privacy Security Risk Register

## Core Rule

Make risk visible, owned, and testable before deployment. Current legal, regulatory, privacy, cybersecurity, and vendor claims must be verified against current official sources before client-facing use.

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
- Legal, regulatory, or compliance exposure.
- Security incident response gaps.

## How To Get Inputs

Gather from:

- Workflow map and data/source inventory.
- IT/data/security interview.
- Executive risk tolerance and regulatory exposure.
- Operator examples of sensitive data and external outputs.
- Vendor/tool list and integration architecture.
- Existing policies: access, retention, incident response, data processing, acceptable use.
- AI interview notes about what mistake would be expensive, embarrassing, illegal, or damaging.

Use current official sources for unstable legal, regulatory, privacy, security-standard, and vendor claims.

## Risk Register Template

| Risk | Data/Workflow | Impact | Likelihood | Control | Owner | Status | Verification Needed |
|---|---|---:|---:|---|---|---|---|
| | | | | | | | |

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

## Output

Deliver:

- Risk register.
- Critical stop conditions.
- Required controls.
- Owners.
- Current verification list.
- Residual risk after controls.
- Recommended go/no-go posture.

## Quality Bar

Do not bury high-impact risks in prose. Put them in the register with owner, control, and status.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

