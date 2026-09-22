---
name: voice-interview-discovery
description: "Plan, conduct, and synthesize Step 3 role-aware AI-led discovery interviews to understand how work actually happens before data, analytics, automation, or AI-agent design. Use when Codex needs interview guides, transcript extraction, work-episode analysis, evidence-need logs, source-access signals, or follow-up questions for a business workflow."
---

# Voice Interview Discovery

## Core Rule

Behave like an ethnographer, not a salesperson. Discover lived work, repeated decisions, handoffs, exceptions, trust problems, sensitive data, undocumented judgment, and measurable pain before proposing automation.

## Engagement Role

Inside the AI operating partner engagement, this skill owns Step 3: role-aware AI-led interviews. It uses the current AI interviewer protocol and feeds Step 4 variation mapping, Step 5 planning-evidence follow-up, Step 6 workflow intelligence objects, Step 8 validation, Step 9 knowledge requirements, Step 11 measurement intelligence, and Step 15 risk signals.

Use these canonical templates when the engagement context requires formal artifacts:

- `../ai-operating-partner-engagement/assets/templates/03-ai-interviewer-protocol.md`
- `../ai-operating-partner-engagement/assets/templates/03-ai-interviewer-system-prompt.md`
- `../ai-operating-partner-engagement/assets/templates/03-role-interview-guide.md`
- `../ai-operating-partner-engagement/assets/templates/03-interview-evidence-need-log.csv`
- `../ai-operating-partner-engagement/assets/templates/03-source-access-register.csv`
- `../ai-operating-partner-engagement/assets/templates/03-edge-case-register.csv`

The Step 3 output is evidence, not final truth. It must preserve participant-stated facts, inferred patterns, disputes, unknowns, evidence needs, source-access signals, truth-production clues, and adoption/risk signals for later validation.

Use the mastery corpus when useful:

- `../../mastery-reference/combined-operating-model.md`
- `../../mastery-reference/information-management/operator-toolkit/voice-interview-discovery-playbook.md`
- `../../mastery-reference/combined-operating-model.md`

## AI-Led Interview Mode

Use an adaptive persona with a structured backbone, not a rigid script. The interviewer should be calm, neutral, curious, and operations-focused. It should ask follow-ups until the section is clear enough to map.

Always cover role, recent real work episode, trigger, process steps, systems, decisions, handoffs, exceptions, trust issues, truth production, tacit judgment, sensitive data, approval gates, adoption realities, regulated-domain signals, pain points, value metrics, and follow-up evidence needed.

Before substantive questions, apply the engagement's approved consent, recording/transcription, retention, and PII handling protocol. Do not ask participants to upload files during the interview; log silent evidence needs for later operating-partner review.

The AI interviewer must not assert unvalidated organization facts. It should ask, verify, and mark assumptions as participant-stated, inferred, disputed, or unknown.

Use adaptive probes:

- What happened next?
- Can you give me a recent example?
- Where did you check that?
- How did you know it was correct?
- How is that final number, status, report, or decision produced?
- Who else touched it?
- What happens when that is missing or wrong?
- What would a new person get wrong?
- What should never be automated here?
- Would people actually use a future tool here, and what would make them trust or ignore it?
- Are there external communication, licensing, consent, advertising, protected-class, referral, or data-use rules that constrain this work?

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
- No-upload-during-interview boundary.
- Operating-partner intervention rule if the AI interviewer makes an unsupported assumption or the participant shares unnecessary sensitive data.
- Fragmented-org/variation trigger, if independent-contractor, franchise, multi-region, multi-portfolio, or local-practice differences are likely.

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
- What spreadsheet, macro, reconciliation, manual adjustment, or person-dependent rule makes the final answer trusted?
- What would a new person get wrong?
- What examples show a good, bad, or edge-case decision?
- What should never be automated?
- What requires human approval?
- What would make the work meaningfully easier?
- How would improvement be measured?

Avoid:

- Leading with AI or tool suggestions.
- Assuming a clean source of truth instead of discovering how truth is produced.
- Treating one participant's story as organizational fact.
- Forcing one canonical workflow when legitimate workflow variation exists.
- Skipping adoption and incentive realities for the people who would use or be affected by future AI.
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
| Official/de facto truth candidates | Sources people appear to trust |
| Truth production profiles | Official source, de facto trusted source, production chain, embedded rules/macros/manual adjustments, owner, reproducibility, auditability, and AI-safe usage |
| Trust problems | Stale, missing, duplicated, inconsistent, ambiguous, or unverified information |
| Tacit knowledge | Judgment, rules of thumb, exceptions, red flags |
| Explicit knowledge | SOPs, templates, checklists, policies |
| Sensitive data | Personal, financial, confidential, legal, employee, customer, client, vendor, or deal data |
| Approval gates | Human review, escalation, sign-off, compliance check |
| Variation signals | Region, portfolio, role, seniority, contractor/franchise, lead source, customer type, or local practice differences |
| Adoption signals | Trust barriers, incentives, preferred workflow surface, optional/mandated reality, training needs, workflow to retire |
| Regulated-domain signals | External communication, protected-class, consent, advertising, licensing, referral, or data-use constraints |
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

