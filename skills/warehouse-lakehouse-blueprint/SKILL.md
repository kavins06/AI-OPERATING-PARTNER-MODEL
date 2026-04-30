---
name: warehouse-lakehouse-blueprint
description: "Design a governed warehouse, lakehouse, semantic layer, document intelligence, and retrieval architecture for analytics, dashboards, data products, and AI agents. Use when Codex needs source-to-dashboard architecture, dimensional models, data zones, quality controls, or build-order recommendations."
---

# Warehouse Lakehouse Blueprint

## Core Rule

Design from workload and governance needs. Keep raw data, standardized data, semantic definitions, documents, retrieval, and agent tools logically separated.

Useful references:

- `../../mastery-reference/analytics/artifacts/data_warehouse_lakehouse_blueprint.md`
- `../../mastery-reference/analytics/artifacts/data_architecture_patterns.md`
- `../../mastery-reference/analytics/artifacts/data_warehouse_lakehouse_blueprint.md`
- `../../mastery-reference/analytics/artifacts/cloud_analytics_comparison_notes.md`

## Architecture Layers

Design:

1. Source inventory.
2. Data contracts.
3. Raw landing zone.
4. Standardized zone.
5. Analytical zone.
6. Document intelligence zone.
7. Semantic layer.
8. Dashboard and BI layer.
9. Retrieval and tool layer.
10. Governance and monitoring.

## Pattern Selection

Choose:

- Governed warehouse first: when trusted reporting and KPIs are primary.
- Lakehouse plus document intelligence: when documents, emails, PDFs, or unstructured content are central.
- Streaming/event architecture: when the workflow reacts to live events.
- Hybrid: when structured metrics and unstructured evidence both matter.

## How To Get Inputs

Collect:

- Source inventory from IT/data teams.
- Workflow and decision needs from managers/operators.
- Current reports, dashboards, and extracts from business users.
- Data-quality issues from admins and stewards.
- Document and unstructured content examples.
- Privacy/security constraints and access boundaries.
- Refresh/freshness requirements.
- Expected agent/tool behaviors.

Do not design architecture from a vendor menu. Design it from decisions, sources, quality needs, governance, and workload.

## Model Design

For any domain, identify:

- Core entities.
- Fact events.
- Dimensions.
- Documents.
- Metric definitions.
- Access policies.
- Data-quality rules.
- Lineage.
- Agent tool boundaries.

Avoid hard-coding one industry model unless the user gives the domain.

## Build Order

Recommend:

1. Inventory and data dictionary.
2. Core entity reconciliation.
3. Key fact tables or analytical datasets.
4. Semantic metrics.
5. Dashboards.
6. Retrieval over approved documents.
7. Read-only agents.
8. Approval-gated write-back only after trust is proven.

## Output Template

Deliver:

- Business workloads.
- Source inventory.
- Target architecture.
- Data zones.
- Entity/fact/dimension sketch.
- Semantic layer needs.
- Document/retrieval design.
- Governance controls.
- Build sequence.
- Risks and open decisions.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

