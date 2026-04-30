# Governance And Privacy Checklist For Business AI Agents

Traceability anchors: data governance (`0_dtkwnv22`, `1_5bu6bkms`, `1_luz6mncn`, `1_mvkxpvok`, `25_dashboard_design_principle`, `big_data_governance_nov_7_2013v62docx`, `data_governance_in_small_businesses`, `review_of_statistics_1`), small-business governance (`data_governance_in_small_businesses`), big-data governance (`1_mvkxpvok`, `big_data_governance_nov_7_2013v62docx`).

## Before Any Agent Goes Live
- Assign data owners for property, tenant, lease, investor, contact, financial, vendor, and document domains.
- Assign data stewards who can resolve definitions, duplicates, missing values, and quality exceptions.
- Create a data dictionary for every field an agent can use in a decision or client-facing answer.
- Define approved metrics: occupancy, NOI, rent collection, delinquency, lead conversion, leasing velocity, maintenance SLA, budget variance.
- Classify sensitive data: PII, tenant ledger, lease terms, investor data, financial statements, communications, credentials.
- Implement least-privilege access and row-level security by client, property, role, and user.
- Require retrieval citations for lease, policy, investor, and financial answers.
- Log prompts, retrieved sources, tool calls, calculations, outputs, approvals, and user edits.
- Add human approval for Fair Housing-sensitive, legal, financial, pricing, vendor-dispatch, and external-communication workflows.
- Define retention rules for source files, embeddings, logs, model outputs, and client exports.

## Data Quality Controls
- Completeness: required fields populated for property, unit, tenant, lease, payment, and work-order records.
- Consistency: metric definitions match across dashboards, agent tools, and reports.
- Timeliness: freshness thresholds by source and use case.
- Accuracy: reconciliation against source systems or finance-approved reports.
- Uniqueness: duplicate detection for properties, contacts, tenants, leases, and vendors.
- Validity: field values within expected types, ranges, and controlled vocabularies.

## Agent Risk Controls
- No protected-class inference or targeting.
- No legal, tax, investment, lending, or Fair Housing conclusions without approved wording and review.
- No silent writes to production systems.
- No ungrounded claims when source data is missing, stale, or contradictory.
- Escalate low-confidence outputs and expose uncertainty.
- Monitor drift, user corrections, escalation rates, and repeated retrieval failures.
