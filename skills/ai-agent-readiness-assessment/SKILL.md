---
name: ai-agent-readiness-assessment
description: "Create Step 16 implementation-grade readiness_object artifacts for candidate opportunities by evaluating hard gates, behavior-level readiness, use-case framing, business value, workflow clarity, source access, data quality, truth production, knowledge/guidance, measurement, AI-capability metrics, solution shape, regulated-domain readiness, architecture, risk controls, adoption/change, human oversight, lifecycle readiness, dependencies, blockers, and Step 17 path."
---

# AI Agent Readiness Assessment

## Core Rule

Readiness scoring comes after enough discovery to score with evidence. Scores without evidence are guesses.

Inside the AI operating partner engagement, readiness scoring does not authorize implementation by itself. Implementation starts only after Step 18 is complete and the client approves the separate implementation phase.

Step 16 is not a generic percentage score. It produces an implementation-grade readiness object for each candidate AI opportunity. The object must say which AI behavior level is ready, which behavior levels are blocked, which dependencies matter, which gates override the score, and what Step 17 should become.

## Engagement Role

Step 16 consumes evidence from Steps 0-15 and produces the `readiness_object`. It is the hard-gate decision point before Step 17 packet selection. A candidate can be ready for one behavior level and prohibited for another.

Use `../ai-operating-partner-engagement/assets/templates/14-ai-agent-readiness-score.yaml` as the canonical artifact, `../ai-operating-partner-engagement/assets/templates/14-hard-gates-readiness-rubric.yaml` as the hard-gate rubric, and `../ai-operating-partner-engagement/assets/templates/14-readiness-scorecard.csv` only as a compact view.

The Step 16 decision must select a Step 17 path: build-ready implementation brief, gap remediation plan, governance/data readiness plan, knowledge capture plan, technical feasibility plan, risk/control plan, do-not-automate recommendation, or discovery incomplete. It must not start implementation.

Useful references:

- `../../mastery-reference/operator-system/readiness-scorecard.md`
- `../../mastery-reference/information-management/operator-toolkit/ai-agent-readiness-assessment.md`
- `../../mastery-reference/analytics/artifacts/client_analytics_maturity_model.md`
- `../../mastery-reference/combined-operating-model.md`

## Required Input Package

Before scoring, gather or explicitly mark missing:

- Candidate opportunity ID, linked workflow IDs, proposed users, and business outcome.
- Candidate use-case shortlist and disqualification criteria from Step 2.
- Validated AI workflow intelligence object from Step 6.
- Organizational diagnostic findings and automation blockers from Step 7.
- Controlled validation/governance decisions from Step 8: official source, de facto trusted source, truth production, owner/steward, source access path, sensitive fields, retention, permission boundaries, and permitted AI actions.
- Truth production profiles: truth status, owner/knower, reproducibility, auditability, AI-safe usage, and remediation route.
- Knowledge requirements from Step 9.
- AI guidance pack, forbidden behaviors, escalation triggers, output contract, and test cases from Step 10.
- Measurement intelligence, metric trust classifications, AI-capability metrics, KPI definitions, and agent-safe metric usage from Step 11.
- Business value case and portfolio comparison with assumptions, AI-side costs, confidence, and recommendation from Step 12.
- Solution shape and adoption design from Step 13.
- Technical implementation blueprint from Step 14: systems, sources, future access paths, runtime/orchestration requirements, hosting/environment requirements, tool/MCP/connector contracts, normalization, identity resolution, test strategy, credentials/secrets approach, audit/logging, blocked paths, and build sequence.
- Risk and control model from Step 15: data classification, regulated-domain risks, tool permissions, output controls, approval gates, logging, monitoring, incident response, revocation, residual risk, and stop conditions.
- Any unresolved owner, feasibility, policy, vendor, data-quality, or security decisions.

If several inputs are missing, score readiness as "discovery incomplete" instead of pretending precision.

## Behavior Levels

Score readiness by behavior level. A workflow can be ready for a narrow AI behavior while blocked from a higher-risk behavior.

- `read_only_summary`: retrieve or receive scoped inputs and summarize with citations.
- `draft_and_flag`: draft outputs, flag missing items, and prepare questions for human review.
- `recommendation_support`: recommend next action with evidence, uncertainty, and human approval.
- `human_approved_action`: prepare or execute a bounded action only after explicit human approval.
- `autonomous_action`: execute bounded actions without case-by-case approval.

Early implementation plans should usually start at the lowest useful behavior level. Do not mark a higher level ready when source access, truth production, controls, approvals, logging, revocation, or measurement trust are unresolved.

## Hard Gates

Hard gates override averages. If a gate is failed or blocked, the readiness decision must route to remediation even if the numeric score is high.

Minimum gates:

- `use_case_framing_gate`: candidate use case is explicit, bounded, and has disqualification criteria.
- `business_value_gate`: credible value and owner exist.
- `workflow_clarity_gate`: workflow, roles, decisions, and edge cases are clear enough.
- `source_access_gate`: required sources, official/de facto source status, access path, and owner are known or explicitly scoped out.
- `data_quality_gate`: required data quality is adequate for the proposed AI behavior level.
- `truth_production_gate`: material truth production is known, owned, reproducible enough, auditable enough, and safe for the proposed behavior level.
- `knowledge_guidance_gate`: guidance pack, examples, forbidden behaviors, and escalation rules are sufficient.
- `measurement_gate`: value and success measurements are trusted or conditionally trusted.
- `ai_capability_metrics_gate`: future AI success, override, error, drift, adoption, cost, and kill criteria are defined.
- `regulated_domain_gate`: named regulatory/vertical constraints are captured when applicable.
- `solution_shape_gate`: build/buy/leverage, topology, model class, UX surface, retrieval/context, and observability shape are clear.
- `technical_feasibility_gate`: future architecture, runtime/orchestration requirements, hosting/environment requirements, access, identity, normalization, tool contracts, test strategy, and blocked paths are known.
- `risk_control_gate`: data handling, permissions, approval gates, output controls, logging, monitoring, incident response, and revocation are defined.
- `adoption_change_gate`: target users, adoption path, incentives, training, feedback, workflow retirement, and adoption-failure triggers are realistic.
- `human_oversight_gate`: accountable owner, reviewer, escalation path, and approval authority exist.
- `lifecycle_gate`: future validation, rollout, monitoring, improvement, and decommission ownership can be assigned.

Gate statuses: `pass`, `conditional`, `fail`, `blocked`, or `unknown`.

## Dimensions

Score 1-5 and record evidence confidence for each dimension:

- Business value.
- Use-case framing readiness.
- Workflow clarity.
- Source access readiness.
- Data quality.
- Truth production readiness.
- Knowledge/guidance readiness.
- Measurement readiness.
- AI-capability metrics readiness.
- Regulated-domain readiness.
- Solution-shape readiness.
- Architecture feasibility.
- Risk/control readiness.
- Adoption/change readiness.
- Human oversight readiness.
- Change/lifecycle readiness.

## Scoring Anchors

1 means weak, unclear, risky, or unsupported.
3 means usable but with named gaps.
5 means clear, governed, measurable, and ready to be included in a post-Step-18 implementation plan.

Do not average away a critical stop condition. A single failed hard gate, severe Step 15 stop condition, missing source access path, missing owner, fragile truth dependency, prohibited action, or unresolved credential/logging/revocation issue can block build even if the total score is high.

If material truth is shadow-derived, manually adjusted, person-dependent, disputed, missing, or not reproducible, any recommendation, write/send, action, or autonomous behavior must fail readiness unless the behavior is explicitly limited to summarize, compare, flag uncertainty, draft clarification questions, or escalate.

## Assessment Workflow

1. Name the candidate opportunity, workflow, owner, users, outcome, and proposed first AI behavior.
2. Pull evidence from Steps 2-15 before asking for anything new.
3. Evaluate hard gates and identify any override conditions.
4. Score each dimension with evidence references, confidence, gap/fix, owner, and blocking status.
5. Score readiness by behavior level: ready, conditional, not ready, or prohibited.
6. Map dependencies across systems, data sources, truth production profiles, guidance packs, metrics, controls, owners, access paths, normalization, tools/MCPs/connectors, tests, credentials/secrets, logging, and lifecycle.
7. Name blockers, required fixes, owner, target resolution path, and whether the blocker changes the Step 17 path.
8. Define minimum safe first behavior and explicitly list not-ready or prohibited behaviors.
9. Recommend the Step 17 path.

## Output Object

Use `../ai-operating-partner-engagement/assets/templates/14-ai-agent-readiness-score.yaml` as the canonical artifact. The CSV scorecard can be used only as a compact view.

The readiness object must include:

- Opportunity and workflow IDs.
- Source inputs and evidence coverage.
- Proposed first AI behavior.
- Hard gates with status, evidence, owner, blocker flag, and required fix.
- Dimension scores with evidence confidence and gap/fix.
- Behavior-level readiness.
- Dependency map.
- Truth production readiness and fragile truth blockers.
- Blockers and required fixes.
- Minimum safe first behavior.
- Not-ready and prohibited behavior levels.
- Step 17 path.
- Readiness decision.
- Owner confirmations still required.
- Stop boundary confirming no implementation starts before Step 18 approval.

## Decision Guide

- `ready_for_step_17_build_brief`: all hard gates pass or have non-blocking conditions, score is strong, evidence confidence is sufficient, and the first behavior level is safe.
- `fix_gaps_first`: value exists, but one or more fixable blockers prevent a build-ready brief.
- `governance_or_data_readiness_first`: source, truth production, permission, quality, owner, retention, or measurement issues are blocking.
- `knowledge_capture_first`: tacit rules, examples, escalation criteria, or output contract are not mature enough.
- `technical_feasibility_first`: API/export/vendor/test/credential/logging/normalization feasibility is unresolved.
- `risk_control_first`: sensitive data, approval, output, monitoring, incident, or revocation controls are not acceptable.
- `deprioritize`: opportunity is not important enough relative to effort or risk.
- `do_not_automate_yet`: behavior is unsafe, prohibited, unowned, unmeasurable, or unsupported.
- `discovery_incomplete`: required required source inputs are missing or too low-confidence to score honestly.

Step 17 should become either a build-ready implementation brief or a specific remediation plan based on this decision.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

