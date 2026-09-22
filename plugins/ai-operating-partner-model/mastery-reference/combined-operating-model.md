# Combined Operating Model

## The Stack

The combined system joins two disciplines:

- Data analytics: trusted data, warehouses/lakehouses, dashboards, statistics, models, KPIs, cloud infrastructure, and BI decision support.
- Information management: information ecology, sensemaking, knowledge capture, governance, privacy, security, data monetization, and organizational decision quality.

Together they produce one operating principle:

> Build agents only after the organization knows what decision is being supported, what information is trusted, who owns it, what knowledge constrains it, what risks apply, and how success will be measured.

## Layer 1: Business Outcome

Name the business result before naming an AI feature.

Business examples:

- Improve lead response speed.
- Shorten review cycles.
- Improve executive reporting quality.
- Reduce operational triage delays.
- Improve revenue and cash-flow visibility.
- Reduce reporting rework.
- Increase decision consistency.

## Layer 2: Workflow Discovery

Map the real work from trigger to outcome.

Capture:

- Trigger.
- Inputs.
- Steps.
- Decisions.
- Handoffs.
- Exceptions.
- Systems used.
- Shadow spreadsheets and inboxes.
- Human approvals.
- Sensitive data.
- Failure points.
- Success metric.

## Layer 3: Information Ecology

Diagnose the whole environment, not just the software.

Map:

- People.
- Process.
- Culture.
- Incentives.
- Politics.
- Informal workarounds.
- Tools.
- Data flows.
- Documents.
- Decision rights.

Failure pattern: treating a workflow breakdown as a chatbot opportunity when the real issue is ownership, definitions, trust, or incentives.

## Layer 4: Data Foundation

Before analytics or agents, establish:

- Source inventory.
- Source of record.
- Data dictionary.
- Core entities.
- Field definitions.
- Refresh cadence.
- Quality rules.
- Lineage.
- Access rules.

Common business entities:

- Contact.
- Customer.
- Account.
- Product.
- Contract.
- Order.
- Transaction.
- Vendor.
- Market.
- Document.
- Date.

## Layer 5: Knowledge Foundation

Agents need explicit knowledge and captured tacit judgment.

Capture:

- SOPs.
- Policies.
- Scripts.
- Examples.
- Edge cases.
- Escalation rules.
- Expert judgment.
- Approved language.
- Do-not-automate zones.

Common tacit knowledge:

- What a top operator notices in a request.
- What a manager treats as urgent.
- What an analyst checks before trusting a variance.
- What a reviewer sees as a red flag.
- What language creates legal, privacy, compliance, or reputational risk.

## Layer 6: Analytics and BI

Use analytics to make decisions visible and measurable.

Required layers:

- Raw source landing.
- Standardized data.
- Warehouse or lakehouse.
- Dimensional marts.
- Semantic layer.
- KPI definitions.
- Dashboards.
- Statistical and predictive models where justified.

The agent should explain, investigate, and coordinate around analytics. It should not replace the evidence layer.

## Layer 7: Governance, Privacy, Security, and Risk

Define controls before connecting agents to systems.

Controls:

- Data owners.
- Data stewards.
- Least privilege.
- Row-level security.
- Retention rules.
- Audit logging.
- Human approval.
- Incident path.
- Vendor review.
- Sensitive-data handling.
- Zero-trust access assumptions.

Stop conditions:

- No source of record.
- Undefined metric.
- Unclear owner.
- Sensitive data without access rules.
- Client-facing output without review.
- Legal/privacy/security claims not verified against current official sources.

## Layer 8: Agent Design

Design agent behavior around controlled capabilities.

Agent patterns:

- Retrieval assistant.
- Drafting assistant.
- Triage assistant.
- Data-quality assistant.
- Dashboard explainer.
- Workflow coordinator.
- Decision-support assistant.
- Approval-gated action agent.

Default first pilot:

- Assistive.
- Read-only or human-reviewed.
- Source-grounded.
- Narrowly scoped.
- Logged.
- Measurable.

## Layer 9: Managed Operation

Treat agents as living systems.

Monitor:

- Output quality.
- Source freshness.
- Retrieval failures.
- Tool failures.
- User corrections.
- Escalation rate.
- Approval rate.
- Cycle-time improvement.
- Cost.
- Risk events.
- Model or workflow drift.

Improve:

- Refresh sources.
- Update SOPs.
- Expand after evidence.
- Retire unused flows.
- Feed user corrections into knowledge and data-quality backlogs.
