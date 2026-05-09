# Quality Gates

The method's quality bar is a gate system, not a best-effort checklist. A future app should make these gates visible, reviewable, and difficult to bypass.

## Gate States

Use consistent status language across artifacts:

- `pass`: sufficient evidence and ownership exist.
- `conditional`: acceptable only with explicit conditions, owners, and review timing.
- `fail`: the current scope cannot proceed as stated.
- `blocked`: required evidence, owner decision, access clarification, or risk confirmation is missing.
- `unknown`: the method has not yet gathered enough evidence to judge.

## Core Gates

1. Engagement tier and vertical extension are selected.
2. Sponsor mechanics, business/technical co-sponsorship, prior-attempt learning, and permission-to-fail posture are captured or explicitly unknown.
3. Candidate use cases are explicitly framed with disqualification criteria and success-pattern fit.
4. Material workflow variation is mapped or explicitly ruled out with evidence.
5. Workflow intelligence objects contain evidence, confidence, source access, truth production, adoption signals, resistance signals, and completeness checks.
6. Material sources, systems, owners, access paths, and source-access profiles are known or routed.
7. Truth production profiles exist for material numbers, statuses, reports, and decision inputs.
8. Regulated-domain obligations are identified and routed through the vertical-extension contract.
9. Knowledge and guideline requirements are mapped, including tacit knowledge gaps.
10. Guidance packs include rules, examples, forbidden behaviors, output contracts, eval methodology, minimum counts, and drift rules.
11. Existing measurements are trust-classified before value claims rely on them, and value-breadth metrics are considered.
12. Business value is compared across a portfolio, not asserted candidate by candidate in isolation; headcount/capacity scenarios are explicit.
13. Solution shape, adoption design, and oversight model are explicit.
14. Fragile truth is remediated or AI behavior is limited to safe uses.
15. Privacy, security, shadow AI, sensitive data, approval, monitoring, incident, and revocation controls are designed.
16. Technical blueprinting documents future access paths, data-access-over-perfection plan, model abstraction/routing, component contracts, normalization, hosting, secrets, observability, and build sequence without requesting live credentials.
17. Risk controls are strong enough for the proposed behavior level.
18. Readiness hard gates pass or are conditional only for explicit build-phase checks, including sponsor behavior, process documentation, resistance profile, recoverable-error fit, model/orchestration, and security enablement.
19. Step 17 packet type matches the Step 16 recommended path.
20. Step 18 lifecycle variant matches the Step 17 packet type and includes failure-learning, KPI refresh, model/runtime review, and role-transition monitoring.
21. method-to-build handoff is approved by the required sponsor, owner, security, risk, legal, and data stakeholders.

## Bundled Client Checkpoint Gates

These checkpoint gates organize client participation. They do not replace the core Step 0-18 gates.

1. Strategy bundle gate, end Step 2: scope, goals, constraints, decision rights, sponsor mechanics, prior-attempt learning, candidate terrain, participant coverage, and success criteria are sufficient to begin the interview sprint.
2. Workflow interview bundle gate, end Step 4: role interviews, resistance-source mapping, oversight expectations, and variation mapping are sufficient to model the workflow without assuming a false canonical path.
3. Evidence/data bundle gate, Step 5 through Step 8: one consolidated evidence request has been issued, evidence or substitutes have been received or routed, prior-attempt/process/KPI/security/shadow-AI evidence is requested only where material, and unresolved hard blockers are explicit.
4. Governance validation bundle gate, end Step 8: source, truth-production, owner, steward, access, sensitivity, retention, and permitted/prohibited AI-action decisions are confirmed, disputed, or routed by authorized resolvers.
5. Decision/handoff bundle gate, end Step 18: value, headcount/capacity outcome, solution shape, oversight model, technical feasibility, model/orchestration, risk controls, readiness, packet path, lifecycle, and method-to-build handoff are approved or routed to remediation/no-automation review.

The bundled-gate rule is to reduce repeated client interruptions, not to reduce evidence quality. Missing critical workflow, system/data, truth-production, risk, or ownership inputs must remain visible as blocked, conditional, or unresolved items.

## Halt And Loopback Logic

The method should pause, revise, disqualify, or route remediation when gates fail. The halt taxonomy in `skills/ai-operating-partner-engagement/assets/templates/halt-taxonomy.yaml` defines the formal terms.

Important loopbacks:

- Step 8 can return to Step 6 and Step 7 when validation changes material facts.
- Step 12 can stop or deprioritize economically weak candidates.
- Step 15 can return to Step 13 when controls force a different solution shape.
- Step 16 can route to remediation, governance/data readiness, knowledge capture, technical feasibility, risk/control, or do-not-automate paths.
- Step 18 defines future re-entry triggers after handoff.

## Product Requirement

A future app should treat gate bypasses as auditable exceptions. Every exception should record who approved it, what evidence was missing, what behavior levels are prohibited, and when the decision must be revisited.
