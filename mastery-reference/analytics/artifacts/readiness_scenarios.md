# Mastery Proof: Applied Readiness Scenarios

Each scenario answers the readiness question: "How would we build and manage this AI agent for a business firm?"

## 1. Lead Routing Agent
- Decision: which lead should be contacted, by whom, and when.
- Data: CRM, web forms, listing interactions, broker availability, historical outcomes.
- Analytics: descriptive funnel metrics, predictive conversion score, segmentation.
- Architecture: CRM ingestion, lead activity fact table, contact dimension, approved outreach templates.
- Governance: Fair Housing-safe language, opt-out handling, no protected-class inference, audit log.
- Dashboard: response time, conversion, appointment rate, agent recommendations accepted.

## 2. Tenant Churn / Renewal Risk Agent
- Decision: which tenants need proactive retention action.
- Data: lease terms, payment history, service requests, communications, renewal history.
- Analytics: classification risk score, driver explanation, confidence band.
- Architecture: tenant and lease dimensions, rent payment and work-order facts, retrieval for lease clauses.
- Governance: PII protection, human review, no discriminatory variables.
- Dashboard: renewal rate, risk bucket movement, intervention outcomes.

## 3. Portfolio Reporting Agent
- Decision: what changed in portfolio performance and why.
- Data: GL, budgets, rent roll, occupancy, leasing, maintenance, capex.
- Analytics: variance analysis, trend comparison, anomaly detection.
- Architecture: finance and occupancy marts, semantic KPI layer, dashboard explainer tool.
- Governance: finance-approved definitions, lineage, row-level security.
- Dashboard: NOI, occupancy, rent collection, budget variance, exceptions.

## 4. Market Comping Agent
- Decision: which comps are relevant and what they imply.
- Data: listing feeds, internal transactions, property attributes, market geography.
- Analytics: filtering, similarity scoring, statistical summary, uncertainty communication.
- Architecture: comp warehouse, property dimension, geospatial attributes, document memo generation.
- Governance: cite every comp, analyst approval, current-market validation.
- Dashboard: comp set quality, confidence, analyst edits.

## 5. Lease Abstraction Agent
- Decision: what obligations, dates, clauses, and financial terms matter.
- Data: leases, amendments, rent schedules, policy documents.
- Analytics: OCR, extraction, retrieval, validation against structured fields.
- Architecture: document lake, metadata index, vector store, lease term table.
- Governance: citations, legal review, no uncited clause claims.
- Dashboard: extraction confidence, missing fields, review backlog.

## 6. Maintenance Triage Agent
- Decision: how to route and prioritize a request.
- Data: work orders, property/unit data, vendor history, SLA policies, tenant messages.
- Analytics: classification, urgency detection, vendor performance.
- Architecture: streaming/event workflow, work-order fact table, vendor dimension.
- Governance: emergency escalation, human approval for dispatch rules, audit log.
- Dashboard: backlog, SLA compliance, repeat issue rate, triage accuracy.
