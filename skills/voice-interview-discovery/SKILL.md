---
name: voice-interview-discovery
description: "Plan, conduct, and synthesize discovery interviews to understand how work actually happens before data, analytics, automation, or AI-agent design. Use when Codex needs interview guides, transcript extraction, work-episode analysis, discovery notes, or follow-up questions for any business workflow."
---

# Voice Interview Discovery

## Core Rule

Behave like an ethnographer, not a salesperson. Discover lived work, repeated decisions, handoffs, exceptions, trust problems, sensitive data, undocumented judgment, and measurable pain before proposing automation.

Use the mastery corpus when useful:

- `../../mastery-reference/combined-operating-model.md`
- `../../mastery-reference/information-management/operator-toolkit/voice-interview-discovery-playbook.md`
- `../../mastery-reference/combined-operating-model.md`

## AI-Led Interview Mode

Use an adaptive persona with a structured backbone, not a rigid script. The interviewer should be calm, neutral, curious, and operations-focused. It should ask follow-ups until the section is clear enough to map.

Always cover role, recent real work episode, trigger, process steps, systems, decisions, handoffs, exceptions, trust issues, tacit judgment, sensitive data, approval gates, pain points, value metrics, and follow-up evidence needed.

Use adaptive probes:

- What happened next?
- Can you give me a recent example?
- Where did you check that?
- How did you know it was correct?
- Who else touched it?
- What happens when that is missing or wrong?
- What would a new person get wrong?
- What should never be automated here?

## Layered Interview Coverage

Interview different layers because each layer sees a different truth:

- Executive or owner: goals, risk tolerance, strategy, economics.
- Manager or operations lead: workflows, bottlenecks, accountability, handoffs.
- Front-line operator: actual work, exceptions, workarounds.
- Admin or support: data entry, documents, reporting, coordination, cleanup.
- IT, data, or security: systems, access, integrations, privacy/security limits.
- Customer-facing role when relevant: communication gaps and service quality.

Use the gap between leadership's intended process and operators' lived process as a primary discovery signal.

## Interview Setup

Define:

- Interview objective.
- Participant role and workflow relationship.
- Recording/transcription plan.
- Sensitive topics to avoid.
- Consent language for process discovery.
- Documents, reports, or screen-share examples requested.

Recommended participant mix:

- Executive or owner for goals and risk tolerance.
- Operations leader for repeated workflows and accountability.
- Front-line operators for real work and exceptions.
- Admin/support role for data entry, coordination, and reporting.
- IT, security, compliance, or data owner when systems or sensitive data are involved.

## Question Flow

Start broad, then follow one real recent work episode.

Ask:

- What are you responsible for day to day?
- Walk through a recent task from start to finish.
- What triggered it?
- What information did you need?
- Where did you look first?
- Which systems, documents, spreadsheets, emails, calls, or people were involved?
- What did you decide, create, route, approve, send, or update?
- What happened next?
- What usually goes wrong?
- What do you check manually because the system cannot be trusted?
- What would a new person get wrong?
- What examples show a good, bad, or edge-case decision?
- What should never be automated?
- What requires human approval?
- What would make the work meaningfully easier?
- How would improvement be measured?

Avoid:

- Leading with AI or tool suggestions.
- Assuming the source of truth.
- Treating one participant's story as organizational fact.
- Asking for passwords, credentials, unnecessary personal details, or confidential specifics that are not needed.

## Transcript Extraction

Convert notes or transcripts into this structure:

| Field | Notes |
|---|---|
| Participant | Role, team, seniority, workflow relationship |
| Work episodes | Specific recent tasks described |
| Trigger | What starts the work |
| Steps | Actual sequence from trigger to outcome |
| Decisions | Decisions made during the workflow |
| Inputs | Data, documents, systems, messages, people |
| Outputs | Reports, messages, updates, approvals, records |
| Handoffs | People or teams involved |
| Systems | Software, spreadsheets, drives, portals, email |
| Source of truth candidates | Sources people appear to trust |
| Trust problems | Stale, missing, duplicated, inconsistent, ambiguous, or unverified information |
| Tacit knowledge | Judgment, rules of thumb, exceptions, red flags |
| Explicit knowledge | SOPs, templates, checklists, policies |
| Sensitive data | Personal, financial, confidential, legal, employee, customer, client, vendor, or deal data |
| Approval gates | Human review, escalation, sign-off, compliance check |
| Pain points | Delay, rework, errors, unclear ownership |
| Value levers | Time, cost, risk, revenue, quality, service |
| Candidate agent assists | Hypotheses only, not recommendations yet |
| Do-not-automate areas | High-risk judgment, legal review, relationship handling, sensitive decisions |
| Follow-up questions | Gaps, contradictions, missing evidence |

## Synthesis After Interviews

After 3-5 interviews, produce:

- Workflow candidates.
- Repeated work episodes.
- Source inventory draft.
- Knowledge map draft.
- Trust-gap list.
- Governance questions.
- Risk signals.
- Candidate automation backlog.
- Follow-up interview list.

Validate the synthesis with participants before readiness scoring or solution design.

## Output Standard

End with:

- What is known.
- What is uncertain.
- What needs validation.
- What evidence supports each candidate workflow.
- Which workflow should be mapped next.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

