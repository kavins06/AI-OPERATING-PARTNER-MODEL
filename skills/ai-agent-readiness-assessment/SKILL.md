---
name: ai-agent-readiness-assessment
description: "Create implementation-grade AI-agent readiness objects for candidate opportunities by evaluating hard gates, behavior-level readiness, business value, workflow clarity, source access, data quality, truth production, knowledge/guidance, measurement, architecture, risk controls, human oversight, lifecycle readiness, dependencies, blockers, and Step 15 path. Use after discovery and before implementation."
---

# AI Agent Readiness Assessment

## Core Rule

Readiness scoring comes after enough discovery to score with evidence. Scores without evidence are guesses.

Inside the AI operating partner engagement, readiness scoring does not authorize implementation by itself. Implementation starts only after Step 16 is complete and the client approves the separate implementation phase.

Step 14 is not a generic percentage score. It produces an implementation-grade readiness object for each candidate AI opportunity. The object must say which AI behavior level is ready, which behavior levels are blocked, which dependencies matter, which gates override the score, and what Step 15 should become.

Useful references:

- `../../mastery-reference/operator-system/readiness-scorecard.md`
- `../../mastery-reference/information-management/operator-toolkit/ai-agent-readiness-assessment.md`
- `../../mastery-reference/analytics/artifacts/client_analytics_maturity_model.md`
- `../../mastery-reference/combined-operating-model.md`

## Required Input Package

Before scoring, gather or explicitly mark missing:

- Candidate opportunity ID, linked workflow IDs, proposed users, and business outcome.
- Validated AI workflow intelligence object from Step 5.
- Organizational diagnostic findings and automation blockers from Step 6.
- Controlled validation/governance decisions from Step 7: official source, de facto trusted source, truth production, owner/steward, source access path, sensitive fields, retention, permission boundaries, and permitted AI actions.
- Truth production profiles: truth status, owner/knower, reproducibility, auditability, AI-safe usage, and remediation route.
- Knowledge requirements from Step 8.
- AI guidance pack, forbidden behaviors, escalation triggers, output contract, and test cases from Step 9.
- Measurement intelligence, metric trust classifications, KPI definitions, and agent-safe metric usage from Step 10.
- Business value case with assumptions, confidence, and recommendation from Step 11.
- Technical implementation blueprint from Step 12: systems, sources, future access paths, runtime/orchestration requirements, hosting/environment requirements, tool/MCP/connector contracts, normalization, identity resolution, test strategy, credentials/secrets approach, audit/logging, blocked paths, and build sequence.
- Risk and control model from Step 13: data classification, tool permissions, output controls, approval gates, logging, monitoring, incident response, revocation, residual risk, and stop conditions.
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

- `business_value_gate`: credible value and owner exist.
- `workflow_clarity_gate`: workflow, roles, decisions, and edge cases are clear enough.
- `source_access_gate`: required sources, official/de facto source status, access path, and owner are known or explicitly scoped out.
- `data_quality_gate`: required data quality is adequate for the proposed AI behavior level.
- `truth_production_gate`: material truth production is known, owned, reproducible enough, auditable enough, and safe for the proposed behavior level.
- `knowledge_guidance_gate`: guidance pack, examples, forbidden behaviors, and escalation rules are sufficient.
- `measurement_gate`: value and success measurements are trusted or conditionally trusted.
- `technical_feasibility_gate`: future architecture, runtime/orchestration requirements, hosting/environment requirements, access, identity, normalization, tool contracts, test strategy, and blocked paths are known.
- `risk_control_gate`: data handling, permissions, approval gates, output controls, logging, monitoring, incident response, and revocation are defined.
- `human_oversight_gate`: accountable owner, reviewer, escalation path, and approval authority exist.
- `lifecycle_gate`: future validation, rollout, monitoring, improvement, and decommission ownership can be assigned.

Gate statuses: `pass`, `conditional`, `fail`, `blocked`, or `unknown`.

## Dimensions

Score 1-5 and record evidence confidence for each dimension:

- Business value.
- Workflow clarity.
- Source access readiness.
- Data quality.
- Truth production readiness.
- Knowledge/guidance readiness.
- Measurement readiness.
- Architecture feasibility.
- Risk/control readiness.
- Human oversight readiness.
- Change/lifecycle readiness.

## Scoring Anchors

1 means weak, unclear, risky, or unsupported.
3 means usable but with named gaps.
5 means clear, governed, measurable, and ready to be included in a post-Step-16 implementation plan.

Do not average away a critical stop condition. A single failed hard gate, severe Step 13 stop condition, missing source access path, missing owner, fragile truth dependency, prohibited action, or unresolved credential/logging/revocation issue can block build even if the total score is high.

## Assessment Workflow

1. Name the candidate opportunity, workflow, owner, users, outcome, and proposed first AI behavior.
2. Pull evidence from Steps 5-13 before asking for anything new.
3. Evaluate hard gates and identify any override conditions.
4. Score each dimension with evidence references, confidence, gap/fix, owner, and blocking status.
5. Score readiness by behavior level: ready, conditional, not ready, or prohibited.
6. Map dependencies across systems, data sources, truth production profiles, guidance packs, metrics, controls, owners, access paths, normalization, tools/MCPs/connectors, tests, credentials/secrets, logging, and lifecycle.
7. Name blockers, required fixes, owner, target resolution path, and whether the blocker changes the Step 15 path.
8. Define minimum safe first behavior and explicitly list not-ready or prohibited behaviors.
9. Recommend the Step 15 path.

## Output Object

Use `../ai-operating-partner-engagement/assets/templates/14-ai-agent-readiness-score.yaml` as the canonical artifact. The older CSV scorecard can be used only as a compact view.

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
- Step 15 path.
- Readiness decision.
- Owner confirmations still required.
- Stop boundary confirming no implementation starts before Step 16 approval.

## Decision Guide

- `ready_for_step_15_build_brief`: all hard gates pass or have non-blocking conditions, score is strong, evidence confidence is sufficient, and the first behavior level is safe.
- `fix_gaps_first`: value exists, but one or more fixable blockers prevent a build-ready brief.
- `governance_or_data_readiness_first`: source, truth production, permission, quality, owner, retention, or measurement issues are blocking.
- `knowledge_capture_first`: tacit rules, examples, escalation criteria, or output contract are not mature enough.
- `technical_feasibility_first`: API/export/vendor/test/credential/logging/normalization feasibility is unresolved.
- `risk_control_first`: sensitive data, approval, output, monitoring, incident, or revocation controls are not acceptable.
- `deprioritize`: opportunity is not important enough relative to effort or risk.
- `do_not_automate_yet`: behavior is unsafe, prohibited, unowned, unmeasurable, or unsupported.

Step 15 should become either a build-ready implementation brief or a specific remediation plan based on this decision.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

