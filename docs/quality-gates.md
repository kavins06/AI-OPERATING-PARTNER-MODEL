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
2. Candidate use cases are explicitly framed with disqualification criteria.
3. Material workflow variation is mapped or explicitly ruled out with evidence.
4. Workflow intelligence objects contain evidence, confidence, source access, truth production, and completeness checks.
5. Material sources, systems, owners, access paths, and source-access profiles are known or routed.
6. Truth production profiles exist for material numbers, statuses, reports, and decision inputs.
7. Regulated-domain obligations are identified and routed through the vertical-extension contract.
8. Knowledge and guideline requirements are mapped, including tacit knowledge gaps.
9. Guidance packs include rules, examples, forbidden behaviors, output contracts, eval methodology, minimum counts, and drift rules.
10. Existing measurements are trust-classified before value claims rely on them.
11. Business value is compared across a portfolio, not asserted candidate by candidate in isolation.
12. Solution shape and adoption design are explicit.
13. Fragile truth is remediated or AI behavior is limited to safe uses.
14. Privacy, security, sensitive data, approval, monitoring, incident, and revocation controls are designed.
15. Technical blueprinting documents future access paths, component contracts, normalization, hosting, secrets, observability, and build sequence without requesting live credentials.
16. Risk controls are strong enough for the proposed behavior level.
17. Readiness hard gates pass or are conditional only for explicit build-phase checks.
18. Step 17 packet type matches the Step 16 recommended path.
19. Step 18 lifecycle variant matches the Step 17 packet type.
20. method-to-build handoff is approved by the required sponsor, owner, security, risk, legal, and data stakeholders.

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
