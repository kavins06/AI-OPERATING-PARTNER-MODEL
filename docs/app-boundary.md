# App Boundary

This repo is the method backbone for a future enterprise modernization webapp. The webapp should live in a separate product repository and consume this system as method, schema, and workflow guidance.

## The App May Build

- Guided engagement setup, tiering, and vertical-extension selection.
- Interview planning, AI interviewer flows, transcript handling, evidence logs, and redaction workflows.
- Structured editors for canonical objects and templates.
- Review flows for sponsors, business owners, data owners, IT, security, risk, compliance, and remediation owners.
- Source, system, truth-production, and ownership inventories.
- Readiness scoring, risk scoring, analytics maturity scoring, and portfolio comparison.
- Packet generation, lifecycle generation, exports, and build-phase handoff packages.
- Dashboards for gate status, blockers, owner commitments, evidence gaps, and lifecycle readiness.

## The App Must Preserve

- Step 0-18 sequencing and explicit loopbacks.
- Evidence references, confidence, validation status, and redaction status.
- Behavior-level readiness and authorization.
- Hard-gate overrides.
- Source access profiles and truth production profiles.
- Vertical-extension rules and regulated-domain obligations.
- Stop boundaries that prevent accidental implementation during the pre-build engagement.
- Approved handoff contracts before any implementation phase begins.

## The App Must Not Do By Default

- Request passwords, broad credentials, unrestricted production access, all-email ingestion, or unapproved API tokens during pre-build.
- Start agent, connector, MCP, normalization, live integration, or production automation work before Step 18 approval.
- Collapse disputed or fragile truth into a single "source of truth" field.
- Treat high average scores as build-ready when a hard gate fails.
- Hide evidence quality, confidence, redaction status, or unresolved ownership from reviewers.
- Present build recommendations without adoption, risk, lifecycle, and revocation design.

## Product Architecture Implication

The app should have a method engine, not just forms:

- A step engine that knows prerequisites, loopbacks, and halt states.
- An object engine that stores versioned canonical objects.
- An evidence engine that links claims to approved evidence.
- A gate engine that evaluates readiness, risk, validation, and handoff status.
- A review engine that routes owner decisions and records approvals.
- An export engine that generates human-readable views and machine-readable payloads from the same objects.

That product architecture lets the app feel simple to users while preserving the full method underneath.
