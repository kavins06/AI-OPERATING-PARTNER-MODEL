# Input Collection Checklist

## Engagement Tiering And Vertical Extension

Before Step 1, decide the engagement depth and vertical obligations.

Capture:

- Engagement tier: lite / standard / deep.
- Target duration and decision deadline.
- Organization size, geography, business units, and operating model.
- Whether the operating model is centralized, federated, franchised, multi-region, independent-contractor, or mixed.
- Whether regulated-domain templates apply.
- Which vertical extension is needed, if any.
- Maximum candidate use cases to deep-discover.
- Maximum opportunities to advance after portfolio comparison.
- Explicit non-goals.

For real estate, decide whether the RE extension applies: Fair Housing, TCPA, RESPA where referrals are involved, MLS/IDX/VOW data rules, state advertising/licensure rules, and broker-agent independent-contractor adoption dynamics.

## Executive Opportunity Terrain Mapping

Ask the sponsor for leadership-level context, not low-level task mechanics or AI ideas.

- Business goals.
- Growth, change, or complexity drivers.
- High-leverage functions.
- Information-intensive work areas.
- Judgment-heavy work areas.
- Coordination-heavy work areas.
- Areas where consistency, visibility, speed, review, or scale would create leverage.
- Trust-critical areas: external communication, sensitive data, regulated work, reputational risk, or approval-heavy decisions.
- Strategic constraints.
- Sponsor decision rights.
- Relevant org chart or team structure for the operating areas being discussed.
- Roles, reporting lines, portfolio/function scope, decision owners, approval owners, and known system/data owners.
- People who can explain how the work actually happens.
- Definition of success.

Triangulate informant nomination:

- Sponsor-nominated people.
- Org-chart sample across layers, portfolios, regions, or functions.
- At least two non-sponsor answers to: "Who do people go to when this work breaks or the answer is unclear?"
- Known system/data/risk owners, even if sponsor did not name them.

Do not ask executives to identify where AI agents fit, what exact tasks should be automated, or how lower-level workflows happen. Use the executive conversation to map the terrain and collect only the relevant org structure needed for interview coverage, then use manager, operator, admin, customer-facing, and IT/data/security interviews to discover workflow truth.

## Opportunity Terrain Synthesis

This is primarily the operating partner's work after the executive conversation. The client confirms priorities, people, access, and constraints.

Produce:

- Strategic context summary.
- Operating leverage themes.
- Full opportunity terrain.
- Sequenced discovery tiers.
- Candidate use-case shortlist.
- Rationale for tiering.
- Interview plan.
- Org coverage matrix.
- Artifact request plan.
- Sponsor confirmation questions.

Each candidate use case must include:

- One-line hypothesis.
- Target user group.
- Workflow boundary.
- Business outcome.
- Value hypothesis.
- Truth production dependencies.
- Source access dependencies.
- Adoption dependencies.
- Regulated-domain dependencies.
- Current confidence.
- Disqualification criteria.
- Minimum safe behavior hypothesis.

Discovery zones are areas where important information, judgment, coordination, visibility, consistency, or trust-sensitive work appears to concentrate. Map the full terrain first, then sequence the investigation. Do not imply that lower-priority zones are unimportant.

Use tiering:

- Tier 1: investigate now with deep discovery.
- Tier 2: investigate next or after Tier 1 dependencies are clearer.
- Foundation/dependency: cross-cutting data, governance, knowledge, analytics, architecture, or access issues.
- Watchlist: potentially important areas needing more evidence.

Do not recommend implementation from this step. Candidate AI uses are hypotheses only, but the shortlist is a required artifact and must be versioned/reaffirmed at diagnostic, value/portfolio, and readiness points.

Use the org structure to create a stratified coverage plan. Start with representative deep interviews across hierarchy, function, portfolio, region, or workflow variation. Expand only when interviews reveal meaningful variation, unresolved conflicts, low quality coverage, high-risk workflows, or rollout/change-management needs.

## AI Interview Protocol Requirements

Before AI-led interviews, define:

- Consent language.
- Whether the interview is recorded or transcribed.
- Retention and deletion expectations.
- PII/sensitive data instructions.
- No-live-upload boundary.
- No-asserted-org-facts rule: the AI interviewer may ask questions but must not assert unvalidated facts about the organization.
- Hallucination protocol: if the AI makes an unsupported assumption, the participant can correct it; the operating partner reviews and marks the item as invalid.
- Operating-partner intervention rules: when to interrupt, clarify, stop, or route to human follow-up.
- Participation-bias monitoring.

For fragmented orgs, do not aim for saturation against one canonical workflow until variation is tested. Use variation mapping for independent contractors, franchises, multi-region operations, or multiple valid workflows.

## Documents and Examples

Ask for examples, not everything. During AI-led interviews, do not ask participants to upload documents live. Log evidence needs silently, then let the operating partner curate a consolidated planning-evidence follow-up request after interviews.

No direct company data access is required for early discovery. Prefer planning evidence: redacted examples, screenshots, reports, trackers, templates, walkthroughs, sample exports, schema/field lists, API/vendor documentation, access-control screenshots, architecture notes, and data dictionaries when tied to specific workflow objects.

Do not ask for broad system access, employee credentials, production credentials, unapproved API tokens, live integrations, MCP/server access, connector access, all-email access, write access, data-room access, or bulk document dumps during the V2 engagement. Those belong in the post-Step-18 implementation phase if the decision packet and lifecycle object are approved.

Every planning-evidence request must name:

- Purpose.
- Workflow, claim, edge case, source conflict, metric, or approval gate it validates.
- Likely owner.
- Sensitivity.
- Redaction needed.
- Access scope.
- Retention or handling rule.
- Priority.
- SLA or due date.
- Escalation path if unavailable.
- Acceptable substitute hierarchy.

- SOPs.
- Current reports.
- Dashboards.
- Spreadsheets.
- Forms.
- Templates.
- Policies.
- Sample tickets/tasks/cases.
- Redacted exports.
- Screenshots or walkthrough videos.
- Schema or field lists.
- API or vendor documentation.
- Access-control screenshots.
- Integration notes.

Acceptable substitute hierarchy when redaction is too costly:

1. Redacted file or screenshot.
2. Screen-share or walkthrough recording with sensitive fields masked.
3. Sample export with dummy or synthetic values.
4. Schema/field list or report definition.
5. Verbal walkthrough captured by the operating partner with evidence confidence marked lower.

## Planning Evidence Access Boundary

Allowed during the V2 engagement:

- Redacted report samples.
- Redacted record examples.
- Screenshots.
- Read-only walkthroughs led by the client.
- Sample exports.
- Formula extracts or screenshots.
- Macro walkthroughs.
- Reconciliation notes.
- Redacted final reporting or decision packets.
- Schema, field lists, report definitions, or data dictionaries.
- API, vendor, or integration documentation.
- Access matrix or role-permission screenshots.
- Redacted email or document examples tied to a specific workflow object.

Prohibited during the V2 engagement:

- Employee passwords or personal credentials.
- Production credentials or service accounts.
- Broad live system access.
- Unapproved API tokens.
- Live MCP, connector, ETL, or normalization builds.
- All-email ingestion.
- Write-back access.
- Bulk unredacted exports.
- Automation of client workflows.

Steps 14-18 should define any future access request package needed for implementation, including purpose, scope, owner approvals, security controls, credential handling, testing approach, and revocation plan.

## Systems Inventory

Capture:

- System name.
- Purpose.
- Owner.
- Users.
- Data inside.
- Export/API access.
- Sensitive data.
- Known quality issues.

## Source Access Intelligence

Capture source access intelligence for every information object that matters to a workflow input, output, decision, approval, edge case, or candidate AI assist. Do not try to inventory every data point in the company upfront.

An information object can be a data point, document, report, dashboard, spreadsheet, email, system record, image, approval, policy, metric, or message.

During interviews, when someone names a report, system, document, field, dashboard, tracker, email, or data point, ask lightweight access-path probes:

- What exactly is the information object called?
- What do you use it for in this workflow?
- Where do you access it: system, module, report, dashboard, folder, inbox, portal, tracker, or person?
- How do you find it: search path, filters, lookup keys, property, tenant, vendor, date, invoice, work order, deal, or account?
- Which fields or attributes are required?
- What do you compare it against?
- Who can access it today?
- What happens when it is missing, stale, duplicated, wrong, or stored somewhere else?
- Is the source official, practical, or disputed?
- If people treat this as true, what official source is supposed to be authoritative?
- What de facto source, artifact, report, spreadsheet, macro, or person do people actually trust?
- What export, formula, macro, manual adjustment, reconciliation, or judgment step produces the final answer?
- Who owns the truth and who understands the production chain?
- Is the chain documented, versioned, reproducible, and auditable?
- Is any part sensitive or approval-bound?

Do not ask for passwords, credentials, unrestricted system access, or live uploads. If a screenshot, walkthrough, export, or redacted example would help later, log a silent evidence need for operating partner review.

## Controlled Validation and Governance Resolution

Finish source, ownership, sensitivity, access, retention, and permitted-AI-action decisions during controlled validation instead of starting another broad governance discovery round.

Use the AI workflow specification and diagnostic to prefill:

- Systems and sources mentioned.
- Information objects and source access profiles.
- Official source candidates, de facto trusted sources, and source conflicts.
- Truth production profiles: official source, de facto trusted source, production chain, embedded rules/macros/manual adjustments, owner, reproducibility, auditability, and AI-safe usage.
- Practical access paths, lookup keys, required fields, and alternate locations.
- Likely owners and stewards.
- Known quality issues.
- Sensitive data signals.
- Access/export constraints.
- Candidate AI actions and forbidden behaviors.

Route only unresolved or high-risk objects to the smallest authorized resolver group. Ask object-specific decision questions:

- What is the official source for this workflow object?
- What source or artifact is de facto trusted when work must get done?
- How is the final truth produced from raw source to final report, status, or decision?
- Which formulas, macros, manual adjustments, reconciliations, or expert-memory rules matter?
- Is the truth chain owned, reproducible, and auditable?
- Is this the correct practical access path for the information object?
- Who owns the definition or source?
- Who stewards quality and correction?
- Which fields or content classes are sensitive?
- What retention, export, or handling rule applies?
- Can AI read, summarize, compare, draft from, export, send, or write this?
- Which action is prohibited until risk or zero-trust controls are designed?
- Which AI use is prohibited until truth production is remediated or limited to summarize, compare, flag uncertainty, draft question, or escalate?

## Metrics

Ask for:

- Volume.
- Cycle time.
- Response time.
- Error rate.
- Rework.
- Cost.
- Revenue impact.
- Customer impact.
- Risk impact.

## Trust and Boundary Inputs

Ask in an executive-safe way:

- Which areas involve sensitive data, external communication, regulated decisions, or reputational risk?
- Where is human judgment especially important?
- Where would stronger review, approval, or auditability be valuable before introducing automation?
- What decisions or communications require named approval?
- Which current laws, policies, standards, contracts, or client expectations must be respected?
