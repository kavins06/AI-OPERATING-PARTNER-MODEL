# Voice Interview Discovery Playbook

Purpose: discover how a business firm actually works day to day, then turn recorded interviews into workflow maps, knowledge maps, governance requirements, risk controls, and AI-agent opportunities.

Core principle: do not enter with a pre-assumed workflow. Start from lived work, repeated decisions, exceptions, information handoffs, and pain. Let workflows emerge from what people actually do.

## 1. Interview Operating Model

Use voice interviews as the first discovery layer.

Interview formats:
- AI-led voice interview: best for scalable intake across many roles.
- Founder/consultant-led Zoom interview: best for executives, high-context operators, and sensitive workflows.
- Recorded working-session walkthrough: best when the person can screen-share how they actually process work.
- Follow-up clarification interview: best after transcript synthesis reveals gaps or contradictions.

Recommended first interview set:
- One executive or owner: business goals, constraints, risk tolerance.
- One operations leader: repeated workflows, bottlenecks, systems, accountability.
- Two front-line operators: actual day-to-day work and exceptions.
- One admin/support role: data entry, document handling, reporting, coordination.
- One IT/compliance/security stakeholder if available.

Recording and transcription:
- Record through Zoom, Granola, or an approved notetaker.
- Tell participants the call is recorded for process discovery and AI-readiness analysis.
- Do not ask for passwords, credentials, personal financial details, medical details, or unnecessary sensitive data.
- If sensitive examples arise, capture the pattern and redact the unnecessary personal details.

## 2. AI Interviewer Instructions

The interviewer should behave like an ethnographer, not a salesperson.

Instruction:
> Your job is to understand how this person actually works. Do not pitch automation. Do not assume workflows. Ask about recent real examples, tools used, decisions made, handoffs, exceptions, delays, duplicate work, trust issues, sensitive data, and undocumented judgment. Keep asking "what happens next?" until the work is clear enough to map.

Interview rules:
- Ask for real recent examples, not abstract opinions.
- Follow the timeline of the work from trigger to outcome.
- Ask where information comes from, where it goes, and who trusts it.
- Ask what happens when things go wrong.
- Ask what only experienced people know.
- Ask what should never be automated.
- Ask what must be approved by a human.
- Ask what would make the work 10x easier.

Avoid:
- Leading questions like "Would an AI agent help with maintenance?"
- Tool-first language before understanding the work.
- Assuming the source of truth.
- Treating one person's description as organizational truth without validation.

## 3. Core Interview Flow

Opening:
- What is your role and what are you responsible for day to day?
- Walk me through yesterday or the last normal workday. What did you actually do?
- Which tasks repeat every day, every week, or every month?
- Which tasks create the most delays, rework, or stress?

Workflow discovery:
- Pick one recent task that took too long. What triggered it?
- What information did you need?
- Where did you look first?
- Which systems, documents, spreadsheets, emails, calls, or people were involved?
- What did you decide, route, approve, create, send, or update?
- What happened next?
- Who else touched the work?
- Where did the final output go?

Information trust:
- Which source do you trust most for this work?
- Which source is usually incomplete, stale, duplicated, or wrong?
- What do you check manually because the system cannot be trusted?
- What definitions or fields mean different things to different people?
- What data do people keep in personal spreadsheets or inboxes?

Tacit knowledge:
- What would a new hire get wrong here?
- What are the edge cases?
- What are the red flags?
- What do you know from experience that is not written anywhere?
- What examples show a good decision and a bad decision?

Risk and governance:
- What information here is sensitive?
- Who should be allowed to see it?
- What should require approval before it is sent or acted on?
- What mistakes would be expensive, embarrassing, illegal, or damaging?
- What needs to be logged or traceable?

Value:
- If this workflow improved, what would change?
- Would it save time, reduce risk, improve conversion, reduce vacancy, speed diligence, improve reporting, or improve client service?
- How would we measure the improvement?

Closing:
- What did I not ask that matters?
- Who else should I interview to understand the real work?
- What document, report, spreadsheet, or example would help explain this?

## 4. Transcript Extraction Schema

After every interview, convert the transcript into structured discovery notes.

Use this schema:

| Field | Description |
|---|---|
| Participant | Role, team, seniority, relationship to workflow |
| Work episodes | Specific examples of real tasks described |
| Trigger | What starts the work |
| Steps | Actual sequence from trigger to outcome |
| Decisions | Decisions made during the workflow |
| Inputs | Data, documents, systems, emails, calls, people, external sources |
| Outputs | Reports, messages, updates, approvals, decisions, records |
| Handoffs | People or teams involved |
| Systems | Software, spreadsheets, shared drives, portals, email, notetakers |
| Source of truth candidates | Sources people appear to trust |
| Trust problems | Stale, missing, duplicated, inconsistent, ambiguous, or unverified information |
| Tacit knowledge | Judgment, rules of thumb, exceptions, red flags |
| Explicit knowledge | SOPs, templates, checklists, documents, policies |
| Sensitive data | Personal, financial, confidential, legal, tenant, buyer, seller, investor, employee, or deal data |
| Approval gates | Human review, escalation, sign-off, compliance check |
| Pain points | Delay, rework, manual lookup, errors, unclear ownership |
| Value levers | Time, cost, risk, revenue, conversion, vacancy, diligence speed, reporting quality |
| Candidate agent assists | Possible AI help, phrased as hypotheses only |
| Do-not-automate areas | Work requiring human judgment, legal review, relationship handling, or high-risk decisions |
| Follow-up questions | Gaps, contradictions, or missing evidence |

## 5. Synthesis After 3-5 Interviews

Do not jump from one interview to an agent build.

After the first 3-5 interviews:
1. Cluster repeated work episodes into candidate workflows.
2. Map each workflow from trigger to outcome.
3. Identify sources, systems, documents, and informal knowledge.
4. Mark trust problems and source-of-truth conflicts.
5. Mark sensitive data and approval needs.
6. Extract tacit knowledge that needs codification.
7. Identify workflow owners and decision owners.
8. Create a first AI-agent opportunity backlog.
9. Validate the map with the people interviewed.

Output artifacts:
- Workflow map.
- Source inventory.
- Knowledge map.
- Trust-gap list.
- Governance questions.
- Risk register.
- AI-agent opportunity backlog.
- Follow-up interview list.

## 6. Validation Call

Run a short validation call before proposing any AI agent.

Validation questions:
- Did we map the workflow correctly?
- What did we misunderstand?
- Which steps are rare exceptions versus normal work?
- Which source is actually authoritative?
- Which parts are too sensitive or judgment-heavy to automate?
- Which improvement would matter most to the business?
- Who owns this workflow?
- What would make a pilot safe?

Decision rule:
- If the client disagrees on the workflow, sources, owner, or risk controls, keep discovering.
- If the workflow is clear, valuable, and governable, move to readiness scoring.

## 7. What To Do After Discovery

Use this sequence:

1. Workflow definition:
   Name the workflow, trigger, outcome, owner, users, and success metric.

2. Readiness assessment:
   Score business value, workflow clarity, data quality, knowledge availability, privacy/security risk, integration feasibility, human oversight, and measurement.

3. Source inventory:
   Identify systems of record, shadow sources, documents, spreadsheets, inboxes, reports, and external sources.

4. Knowledge capture:
   Convert tacit judgment into rules, examples, escalation criteria, approved language, and SOPs.

5. Governance design:
   Define owners, access rights, definitions, quality checks, retention rules, approval gates, and audit needs.

6. Risk register:
   Capture privacy, security, legal, operational, reputational, and output-quality risks.

7. Agent opportunity selection:
   Prioritize use cases by value, readiness, risk, and effort.

8. Pilot design:
   Start with assistive, source-grounded, human-reviewed agent behavior before autonomous action.

9. Measurement:
   Establish baseline and target metrics before implementation.

10. Managed operation:
   Monitor outputs, exceptions, source drift, user feedback, and risk events.

## 8. AI-Agent Opportunity Types

Discovery may reveal several opportunity types:

| Opportunity Type | Good First Use | Risk Level |
|---|---|---|
| Retrieval assistant | Answer questions from approved documents with citations | Low-medium |
| Drafting assistant | Draft emails, reports, summaries, updates for human review | Medium |
| Triage assistant | Classify urgency, route work, suggest next step | Medium |
| Data-quality assistant | Detect missing, stale, duplicated, inconsistent records | Low-medium |
| Workflow coordinator | Track open items, reminders, handoffs, approvals | Medium |
| Decision-support assistant | Compare options, surface evidence, recommend review path | Medium-high |
| Autonomous action agent | Send, update, approve, or trigger actions without review | High |

Default first pilot:
- Retrieval, drafting, triage, data-quality, or coordination.
- Human review required.
- Scoped access.
- Strong logging.
- Clear success metric.

## 9. Quality Checks

Before proposing a build:
- At least three roles have been interviewed, unless the firm is very small.
- The workflow has been validated by the actual operators.
- The source of truth is named or the conflict is documented.
- Sensitive data is classified.
- Tacit knowledge has examples, not just labels.
- Human approval gates are clear.
- The value metric is measurable.
- The first agent behavior is assistive before autonomous.
- Legal, privacy, security, and compliance claims are verified before client-facing use.

## 10. The Service Offer

Position the service like this:

> We interview your team to understand how work actually happens, map the information and knowledge behind it, identify where data and process risk block automation, then build and manage AI agents only where the workflow is clear, valuable, and governable.

The offer is not "we install AI agents."

The offer is:
- Discover the real work.
- Structure the information system.
- Govern the risk.
- Capture the expertise.
- Build the agent.
- Manage and improve it over time.
