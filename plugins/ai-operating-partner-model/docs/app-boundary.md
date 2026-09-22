# App Boundary

This repo is the method backbone for a future enterprise modernization webapp. The webapp should live in a separate product repository and consume this system as method, schema, and workflow guidance.

## The App May Build

- Guided engagement setup, tiering, and vertical-extension selection.
- Client touchpoint workspaces for the strategy, workflow interview, evidence/data, governance validation, and decision/handoff bundles.
- Interview planning, AI interviewer flows, transcript handling, evidence logs, and redaction workflows.
- Structured editors for canonical objects and templates.
- Review flows for sponsors, business owners, data owners, IT, security, risk, compliance, and remediation owners.
- Source, system, truth-production, and ownership inventories.
- Sponsor mechanics, prior-failure learning, resistance-source, oversight-model, and headcount/capacity outcome capture.
- Readiness scoring, risk scoring, analytics maturity scoring, and portfolio comparison.
- Packet generation, lifecycle generation, exports, and build-phase handoff packages.
- Dashboards for gate status, blockers, owner commitments, evidence gaps, and lifecycle readiness.

## The App Must Preserve

- Step 0-18 sequencing and explicit loopbacks.
- The batched client-touchpoint model: the app may simplify the client experience, but it must still preserve the full internal method.
- Evidence references, confidence, validation status, and redaction status.
- Behavior-level readiness and authorization.
- Hard-gate overrides.
- Source access profiles and truth production profiles.
- Sponsor behavior, resistance mapping, security enablement, model/orchestration, and recoverable-error fit as first-class readiness inputs.
- Vertical-extension rules and regulated-domain obligations.
- Stop boundaries that prevent accidental implementation during the pre-build engagement.
- Approved Step 18 handoff contracts plus separate implementation approval before any implementation phase begins.

## The App Must Not Do By Default

- Request passwords, broad credentials, unrestricted production access, all-email ingestion, or unapproved API tokens during pre-build.
- Turn every internal step into a separate client prompt or create repeated evidence drip requests when a consolidated request and targeted blocker follow-up would suffice.
- Start agent, connector, MCP, normalization, live integration, or production automation work before Step 18 approval and separate implementation authorization.
- Collapse disputed or fragile truth into a single "source of truth" field.
- Treat high average scores as build-ready when a hard gate fails.
- Hide evidence quality, confidence, redaction status, or unresolved ownership from reviewers.
- Present build recommendations without adoption, risk, lifecycle, and revocation design.

## Product Architecture Implication

The app should have a method engine, not just forms:

- A step engine that knows prerequisites, loopbacks, and halt states.
- A touchpoint engine that batches client work into the five input, validation, and approval bundles while preserving internal step state.
- An object engine that stores versioned canonical objects.
- An evidence engine that links claims to approved evidence.
- A gate engine that evaluates readiness, risk, validation, and handoff status.
- A review engine that routes owner decisions and records approvals.
- A deployment-calibration engine that tracks sponsor behavior, staff-function blockers, shadow AI risk, oversight model, value-realization path, and failure-learning loops.
- An export engine that generates human-readable views and machine-readable payloads from the same objects.

That product architecture lets the app feel simple to users while preserving the full method underneath.

## Post-18 Build Boundary

Step 18 remains the method-to-build handoff boundary. The future app must not introduce another numbered method step or treat build work as an implicit continuation of the engagement.

After Step 18, a separate implementation approval may authorize a build/operate track. That track may use `agent-build-managed-agentops` to convert approved Step 17/18 artifacts into build/operate contracts for an agent necessity kill test, first behavior scope, architecture, tool/data/identity boundaries, environment access, evals, security review, sandbox prototype, pilot, production readiness scoring, production release, Managed AgentOps, change control, and retirement or redesign.

The app should preserve a clean state transition: pre-build method engagement, approved handoff, separate implementation approval, then post-18 build/operate execution.
