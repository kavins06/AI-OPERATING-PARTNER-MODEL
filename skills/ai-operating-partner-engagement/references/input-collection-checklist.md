# Input Collection Checklist

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

Do not ask executives to identify where AI agents fit, what exact tasks should be automated, or how lower-level workflows happen. Use the executive conversation to map the terrain and collect only the relevant org structure needed for interview coverage, then use manager, operator, admin, customer-facing, and IT/data/security interviews to discover workflow truth.

## Opportunity Terrain Synthesis

This is primarily the operating partner's work after the executive conversation. The client confirms priorities, people, access, and constraints.

Produce:

- Strategic context summary.
- Operating leverage themes.
- Full opportunity terrain.
- Sequenced discovery tiers.
- Rationale for tiering.
- Interview plan.
- Org coverage matrix.
- Artifact request plan.
- Sponsor confirmation questions.

Discovery zones are areas where important information, judgment, coordination, visibility, consistency, or trust-sensitive work appears to concentrate. Map the full terrain first, then sequence the investigation. Do not imply that lower-priority zones are unimportant.

Use tiering:

- Tier 1: investigate now with deep discovery.
- Tier 2: investigate next or after Tier 1 dependencies are clearer.
- Foundation/dependency: cross-cutting data, governance, knowledge, analytics, architecture, or access issues.
- Watchlist: potentially important areas needing more evidence.

Do not recommend automation from this step. Candidate agent uses are hypotheses only.

Use the org structure to create a stratified coverage plan. Start with representative deep interviews across hierarchy, function, portfolio, region, or workflow variation. Expand only when interviews reveal meaningful variation, unresolved conflicts, low quality coverage, high-risk workflows, or rollout/change-management needs.

## Documents and Examples

Ask for examples, not everything. During AI-led interviews, do not ask participants to upload documents live. Log evidence needs silently, then let the operating partner curate a consolidated planning-evidence follow-up request after interviews.

No direct company data access is required for early discovery. Prefer planning evidence: redacted examples, screenshots, reports, trackers, templates, walkthroughs, sample exports, schema/field lists, API/vendor documentation, access-control screenshots, architecture notes, and data dictionaries when tied to specific workflow objects.

Do not ask for broad system access, employee credentials, production credentials, unapproved API tokens, live integrations, MCP/server access, connector access, all-email access, write access, data-room access, or bulk document dumps during the 16-step engagement. Those belong in the post-Step-16 implementation phase if the blueprint is approved.

Every planning-evidence request must name:

- Purpose.
- Workflow, claim, edge case, source conflict, metric, or approval gate it validates.
- Likely owner.
- Sensitivity.
- Redaction needed.
- Access scope.
- Retention or handling rule.
- Priority.

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

## Planning Evidence Access Boundary

Allowed during the 16-step engagement:

- Redacted report samples.
- Redacted record examples.
- Screenshots.
- Read-only walkthroughs led by the client.
- Sample exports.
- Schema, field lists, report definitions, or data dictionaries.
- API, vendor, or integration documentation.
- Access matrix or role-permission screenshots.
- Redacted email or document examples tied to a specific workflow object.

Prohibited during the 16-step engagement:

- Employee passwords or personal credentials.
- Production credentials or service accounts.
- Broad live system access.
- Unapproved API tokens.
- Live MCP, connector, ETL, or normalization builds.
- All-email ingestion.
- Write-back access.
- Bulk unredacted exports.
- Automation of client workflows.

Step 12-16 should define any future access request package needed for implementation, including purpose, scope, owner approvals, security controls, credential handling, testing approach, and revocation plan.

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
- Is any part sensitive or approval-bound?

Do not ask for passwords, credentials, unrestricted system access, or live uploads. If a screenshot, walkthrough, export, or redacted example would help later, log a silent evidence need for operating partner review.

## Controlled Validation and Governance Resolution

Finish source, ownership, sensitivity, access, retention, and permitted-AI-action decisions during controlled validation instead of starting another broad governance discovery round.

Use the AI workflow specification and diagnostic to prefill:

- Systems and sources mentioned.
- Information objects and source access profiles.
- Source-of-record candidates and conflicts.
- Practical access paths, lookup keys, required fields, and alternate locations.
- Likely owners and stewards.
- Known quality issues.
- Sensitive data signals.
- Access/export constraints.
- Candidate AI actions and forbidden behaviors.

Route only unresolved or high-risk objects to the smallest authorized resolver group. Ask object-specific decision questions:

- Is this the authoritative source for this workflow object?
- Is this the correct practical access path for the information object?
- Who owns the definition or source?
- Who stewards quality and correction?
- Which fields or content classes are sensitive?
- What retention, export, or handling rule applies?
- Can AI read, summarize, compare, draft from, export, send, or write this?
- Which action is prohibited until risk or zero-trust controls are designed?

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
