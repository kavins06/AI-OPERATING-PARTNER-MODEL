---
name: tacit-to-explicit-knowledge-capture
description: "Convert expert tacit knowledge into explicit, reusable rules, examples, checklists, SOPs, prompts, escalation criteria, and review workflows. Use when important work depends on experience, judgment, context, undocumented exceptions, or expert pattern recognition."
---

# Tacit To Explicit Knowledge Capture

## Core Rule

Capture judgment through examples and decision criteria, not vague labels. Experts often know more than they can state directly.

Inside the AI operating partner engagement, this is Step 10. Start from the Step 9 AI knowledge and guideline requirements map. Step 9 identifies what guidance is needed; Step 10 writes the actual AI guidance pack.

The canonical Step 10 artifact is a machine-readable guidance spec, not a prose memo and not only a `SKILL.md`. A Markdown readable guide is a platform-agnostic view of the same guidance. Test/evaluation cases are a separate view used later to verify whether a future AI follows the guidance. Keep all three aligned:

- Structured guidance spec: canonical artifact.
- Markdown readable guide: human-readable, platform-agnostic view.
- Test/evaluation cases: behavior verification view.

Useful references:

- `../../mastery-reference/information-management/operator-toolkit/information-architecture-and-knowledge-map-template.md`
- `../../mastery-reference/information-management/concept-library/concepts.md`
- `../../mastery-reference/information-management/operator-toolkit/voice-interview-discovery-playbook.md`
- `../../mastery-reference/information-management/operator-toolkit/information-architecture-and-knowledge-map-template.md`

## AI Interviewer Behavior

Use an adaptive interviewer, not a rigid script. Follow examples until the tacit decision logic is visible.

When an expert gives a general rule, ask:

- Can you show a recent example?
- What made that case different?
- What did you notice first?
- What would a new person miss?
- When does that rule fail?
- What would make you escalate?
- How confident would you be, and why?
- Is this rule encoded in a spreadsheet, macro, formula, report, reconciliation, manual adjustment, or expert memory?

Stop only when the answer can be converted into rules, examples, edge cases, and review criteria.

## Capture Workflow

1. Start from a Step 9 knowledge or guideline requirement.
2. Confirm the decision or task where expertise matters.
3. Identify top performers, reviewers, and exception handlers.
4. Ask for recent concrete examples.
5. Compare good, bad, and edge-case outcomes.
6. Extract cues, rules of thumb, thresholds, and red flags.
7. Identify exceptions and escalation triggers.
8. Translate judgment into a structured guidance spec with explicit rules, source hierarchy, truth-production handling, regulated-domain handling where applicable, tacit cues, examples, allowed behaviors, forbidden behaviors, escalation logic, and output contract.
9. Generate a Markdown readable view and behavioral/output-quality test cases from the structured spec.
10. Validate with experts, reviewers, and risk owners where needed.
11. Define ownership, update cadence, and validation status.

## Elicitation Prompts

Ask:

- What would a novice miss?
- What makes you pause?
- What is an obvious red flag to you?
- What are three examples of a good decision?
- What are three examples of a bad decision?
- What exceptions break the normal rule?
- What should always be escalated?
- What language or action would be risky?
- How do you know when confidence is low?
- What rule, formula, macro, adjustment, or reconciliation would need to be extracted before AI can rely on this?

## Codification Formats

Choose the lightest useful format:

- Machine-readable guidance spec.
- Markdown readable guide.
- Test/evaluation case file.
- Checklist.
- Decision tree.
- Example library.
- SOP.
- Approved language bank.
- Escalation matrix.
- Prompt requirements.
- Review rubric.
- Training notes.

## Output Template

Produce:

- Structured guidance spec:
  - Guidance ID, workflow ID, version, status, and linked Step 9 requirement IDs.
  - Purpose, scope, and out-of-scope areas.
  - Owner roles, reviewers, update cadence, and validation status.
  - Required inputs and missing-input behavior.
- Source hierarchy, fallback sources, prohibited sources, and source-conflict handling.
- Truth production handling: allowed truth statuses, fragile truth behaviors, confidence language, and escalation rules.
  - Explicit rules.
  - Tacit cues and judgment signals.
  - Examples: good, bad, edge, low-confidence, source-conflict, fragile-truth, regulated-domain, and adoption-failure where relevant.
  - Allowed AI behaviors.
  - Forbidden AI behaviors.
  - Escalation triggers and human approval gates.
  - Sensitive-field handling.
  - Output contract.
  - Evidence references and unresolved gaps.
- Markdown readable guide:
  - When to use it.
  - Inputs.
  - Rules.
  - Examples.
  - Escalations.
  - Forbidden behaviors.
  - Output format.
- Test/evaluation cases:
  - Scenario.
  - Inputs.
  - Expected AI behavior.
  - Expected escalation or human review.
  - Pass criteria.
  - Behavioral eval family or output-quality eval family.

Minimum eval coverage before implementation planning: at least 10 good, 10 bad/forbidden, and 5 edge behavioral cases per material behavior family; at least 5 source-conflict or fragile-truth cases when material; at least 5 regulated-domain cases when a regulated extension applies; and output-quality evals for required fields, evidence/citation, confidence language, sensitive-field handling, and schema compliance.

## Quality Bar

Do not call knowledge captured until experts can recognize their judgment in the structured guidance, a novice can use the readable view to improve performance under review, and the test/evaluation cases can detect common wrong AI behaviors.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

