# Business Data Architecture Patterns For Managed AI Agents

Traceability anchors: warehousing (`0_ab2tn7r0`, `1_143lj4b8`, `1_5bu6bkms`, `1_69vy7x68`, `1_8nlrdrtj`, `1_bjyscj13`, `1_luz6mncn`, `aws_data_analytics_products`, `data_warehousing`), big-data architecture (`0_ab2tn7r0`, `0_dtkwnv22`, `0_kjkmxro4`, `0_ps4eqwt7`, `1_1cg0sy8s`, `1_5bu6bkms`, `1_mvkxpvok`, `1_pciyc4os`, `1_qfxdmxya`, `1_s0v3fwb6`), governance (`0_dtkwnv22`, `1_5bu6bkms`, `1_luz6mncn`, `1_mvkxpvok`, `25_dashboard_design_principle`, `big_data_governance_nov_7_2013v62docx`, `data_governance_in_small_businesses`, `review_of_statistics_1`), cloud analytics (`0_kjkmxro4`, `0_ps4eqwt7`, `1_pciyc4os`, `1_qfxdmxya`, `1_s0v3fwb6`, `aws_data_analytics_products`, `big_data_architecture_resources`, `big_data_governance_nov_7_2013v62docx`, `dashboard_building_principles`, `google_cloud_platform`).

## Pattern 1: Governed Warehouse First
Use this when the client mainly needs trusted reporting and KPI agents.

Source systems: CRM, MLS/listings, property management, accounting, leasing, maintenance, marketing, documents.

Core layers:
- Ingestion: API pulls, secure file drops, database replication, event streams where needed.
- Raw landing: immutable source extracts with timestamps and source ownership.
- Standardized layer: cleaned entities, normalized fields, identity resolution.
- Warehouse marts: leasing, rent roll, occupancy, maintenance, finance, investor reporting.
- Semantic layer: approved metric definitions and row-level security.
- Agent layer: SQL tools, retrieval tools, dashboard explainers, workflow actions, audit logs.

## Pattern 2: Lakehouse Plus Document Intelligence
Use this when leases, offering memoranda, emails, inspection reports, and policies are central.

Add:
- Object storage for PDFs, DOCX files, images, and exports.
- OCR and document parsing pipeline.
- Metadata index for document type, property, tenant, date, version, owner, and access level.
- Vector store for semantic retrieval.
- Citation-required response policy for lease, policy, and reporting agents.

## Pattern 3: Streaming Operational Agent
Use this when the agent reacts to live events.

Examples:
- New lead submitted.
- Work order created.
- Payment failed.
- Listing status changed.
- Agent tool call failed.

Design:
- Event bus or stream.
- Rules plus model scoring.
- Human-in-the-loop approval queue for sensitive actions.
- Monitoring dashboard for throughput, latency, escalations, and errors.

## Minimum Business Analytical Model
Dimensions:
- `dim_property`, `dim_unit`, `dim_tenant`, `dim_lease`, `dim_contact`, `dim_broker`, `dim_market`, `dim_vendor`, `dim_date`, `dim_document`.

Facts:
- `fact_leasing_activity`, `fact_rent_roll_snapshot`, `fact_occupancy_snapshot`, `fact_rent_payment`, `fact_work_order`, `fact_gl_transaction`, `fact_budget_variance`, `fact_listing_activity`, `fact_agent_action`.

Control tables:
- data dictionary, metric definitions, source lineage, data quality rules, access policy, agent approval rules.
