---
name: ai-agent-readiness-assessment
description: "Score whether a workflow is ready for AI-agent design or build by evaluating business value, workflow clarity, data quality, knowledge availability, analytics maturity, architecture feasibility, privacy/security controls, human oversight, and measurement. Use after discovery and before implementation."
---

# AI Agent Readiness Assessment

## Core Rule

Readiness scoring comes after enough discovery to score with evidence. Scores without evidence are guesses.

Useful references:

- `../../mastery-reference/operator-system/readiness-scorecard.md`
- `../../mastery-reference/information-management/operator-toolkit/ai-agent-readiness-assessment.md`
- `../../mastery-reference/analytics/artifacts/client_analytics_maturity_model.md`
- `../../mastery-reference/combined-operating-model.md`

## Required Input Package

Before scoring, gather or explicitly mark missing:

- Intake goals and success definition.
- AI-led interview synthesis across organizational layers.
- Workflow map.
- Source/system inventory.
- Governance discovery.
- Knowledge map and tacit knowledge capture.
- Analytics maturity evidence.
- Dashboard/KPI definitions if relevant.
- Privacy/security risk register.
- Zero-trust permission model.
- Baseline metrics.
- Validation-call corrections.

If several inputs are missing, score readiness as "discovery incomplete" instead of pretending precision.

## Dimensions

Score 1-5:

- Business value.
- Workflow clarity.
- Data quality.
- Knowledge availability.
- Analytics maturity.
- Architecture feasibility.
- Privacy/security control.
- Human oversight.
- Measurement.

## Scoring Anchors

1 means weak, unclear, risky, or unsupported.
3 means usable but with named gaps.
5 means clear, governed, measurable, and ready for scoped pilot design.

Do not average away a critical stop condition. A single severe risk can block build even if the total score is high.

## Assessment Workflow

1. Name the workflow, owner, users, and outcome.
2. Gather evidence from interviews, maps, sources, governance, knowledge, analytics, and risk work.
3. Score each dimension.
4. Write evidence for every score.
5. Identify blockers and required fixes.
6. Recommend: build-ready, fix gaps first, discovery/governance first, or do not automate.
7. Define first safe agent behavior if build-ready.

## Output Template

| Dimension | Score | Evidence | Gap/Fix |
|---|---:|---|---|
| Business value | | | |
| Workflow clarity | | | |
| Data quality | | | |
| Knowledge availability | | | |
| Analytics maturity | | | |
| Architecture feasibility | | | |
| Privacy/security control | | | |
| Human oversight | | | |
| Measurement | | | |

Then provide:

- Total score.
- Decision.
- Required fixes.
- Recommended first agent behavior.
- Success metric.
- Review cadence.

## Decision Guide

- Strong: proceed to pilot design.
- Medium: fix named gaps first.
- Low: discovery, governance, data-quality, or knowledge-capture project first.
- Severe risk: do not automate yet.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

