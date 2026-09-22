# Operating Intelligence Platform

This note defines the platform layer that sits between discovery and agent deployment.

The intent is not to build a generic Palantir clone. The intent is to build a client-specific operating intelligence layer that makes the approved parts of a company queryable, governed, and agent-ready.

## Core Idea

The platform turns Section 1 discovery into an implementation environment:

- workflows become queryable process maps.
- systems become source inventories and access paths.
- reports and spreadsheets become metric and truth-production objects.
- documents and tacit knowledge become governed knowledge assets.
- owners and controls become permission, review, and escalation rules.
- approved use cases become platform workloads.
- agents become applications on top of the governed operating layer.

The platform should start as a minimum viable foundry for one high-value workflow or domain, not as a whole-company platform.

## When Platform Build Can Start

The earliest technical point is after Step 14, when the technical implementation blueprint has enough information about systems, data, identity, access paths, canonical entities, hosting, logging, testing, and blocked paths.

The stronger operating point is after Step 17, when the implementation decision packet approves what should be built, in what order, with which owners and boundaries.

Actual client implementation still requires Step 18 handoff acceptance and separate implementation approval.

## No Proprietary Data Required Initially

The initial platform can be built without proprietary client data.

During Section 1, the platform can use:

- system names and source inventory metadata.
- owner maps and access constraints.
- workflow maps and decision maps.
- screenshots, report descriptions, and field lists when approved.
- redacted examples.
- synthetic records.
- KPI definitions and formula descriptions.
- document categories and knowledge maps.
- approved and prohibited data paths.
- future access request packages.

This creates a platform scaffold: a structured model of how the company works, without storing sensitive operational records.

## Data Access Stages

Use staged access:

1. No proprietary data: build the scaffold from discovery evidence, metadata, redacted samples, and synthetic examples.
2. Limited approved samples: test schemas, mappings, retrieval, metrics, query behavior, and evals with redacted or narrow sample data.
3. Controlled client environment: connect approved sources inside the client cloud, tenant, or approved secure environment.
4. Production operating intelligence layer: make approved company data and knowledge queryable with access control, audit, lineage, and monitoring.
5. Agent layer: deploy agents that use the governed platform for retrieval, reasoning, drafting, recommendations, or approved actions.

## Platform Layers

Minimum platform layers:

1. Source inventory and access map.
2. Data contracts and source-to-canonical mappings.
3. Canonical entity model.
4. Raw or staged landing layer, where approved.
5. Standardized data layer.
6. Semantic and truth layer for metrics, formulas, definitions, and lineage.
7. Document and knowledge layer for SOPs, policies, PDFs, emails, notes, examples, and tacit rules.
8. Permission and governance layer.
9. Query layer for business users and operators.
10. Tool/action layer for approved APIs, workflow actions, and automations.
11. Observability, audit, quality, and freshness layer.
12. Agent layer.
13. Managed AgentOps layer.

Keep these layers logically separate. Agents should not bypass the platform and directly improvise over ungoverned sources.

The ontology that defines the platform object graph lives in `../docs/operating-intelligence-platform-ontology.md`.

## Minimum Viable Foundry

The first implementation should target one domain or workflow:

- revenue operations.
- customer support.
- claims or intake.
- finance close.
- recruiting or talent operations.
- field operations.
- compliance review.
- project delivery.

The first platform wedge should include:

- one approved workflow boundary.
- one or two primary systems or source groups.
- a small canonical entity model.
- a limited semantic layer.
- a governed document/knowledge set.
- clear owners and access limits.
- queryable views over approved sources.
- traceable answers with source references.
- one or two agent-ready use cases.

## Platform Readiness Gate

Before building the platform, confirm:

- Business outcome and workflow boundary are approved.
- Required source systems are identified.
- Source owners and data owners are named.
- Access path is known or future access request is defined.
- Canonical entities and key fields are sketched.
- Metric definitions and truth-production rules are documented.
- Document and knowledge categories are identified.
- Sensitive data, prohibited data, and retention constraints are known.
- Permission model and user groups are defined.
- Hosting/environment posture is known.
- Query use cases are specific enough to test.
- Agent opportunities are downstream of the platform, not a reason to skip it.

If these are missing, continue Section 1 discovery or return to the method owner.

## Relationship To Agents

Agents should be built after the platform has enough governed structure for the agent's job.

The platform provides:

- approved sources.
- source freshness rules.
- identity and access boundaries.
- semantic definitions.
- retrieval context.
- tool contracts.
- audit traces.
- eval datasets.
- guardrail policies.
- owner and escalation paths.

The agent then becomes a controlled interface or worker on top of the platform.

## Boundary

Do not collect production credentials, broad proprietary datasets, all-email access, live API tokens, or bulk unredacted exports during discovery.

Do not use client proprietary data for model training unless explicitly approved in writing.

Do not mix data across clients.

Do not treat a metadata scaffold as a production intelligence platform.

Build the real platform only after approval, inside the approved environment, with clear ownership, data authorization, access control, audit, retention, and deletion rules.
