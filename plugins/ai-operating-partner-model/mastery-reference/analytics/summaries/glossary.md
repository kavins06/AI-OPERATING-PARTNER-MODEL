# BI, Big Data, Analytics, And Business AI-Agent Glossary

| Term | Working definition | Business AI-agent use |
|---|---|---|
| Analytics | Systematic use of data, models, and reasoning to describe, predict, or prescribe decisions. | Frames every business agent as a decision system, not just a chat interface. |
| Business intelligence | Processes, data stores, dashboards, and tools that turn operational data into decision-ready information. | Core layer for portfolio, brokerage, property management, and investor reporting agents. |
| Big data | High-volume, high-velocity, high-variety data that exceeds simple spreadsheet or single-system handling. | Applies to listings, rent rolls, documents, tenant interactions, maintenance logs, and external market feeds. |
| Data warehouse | Integrated, historical, query-optimized repository for reporting and analysis. | Backbone for NOI, occupancy, leasing, rent collection, and performance dashboards. |
| Data mart | A subject-specific analytical store, often derived from a warehouse. | Useful for property management, brokerage pipeline, investor reporting, or asset management views. |
| ETL | Extract, transform, and load pipeline that moves data from source systems into analytical structures. | Needed to clean CRM, MLS, accounting, property management, and document metadata. |
| ELT | Extract, load, then transform inside a warehouse or lakehouse. | Often simpler for cloud analytics stacks with raw source retention. |
| Data lake | Low-cost storage for raw structured, semi-structured, and unstructured data. | Good landing zone for leases, PDFs, emails, listings, images, and logs before refinement. |
| Lakehouse | Architecture combining lake storage flexibility with warehouse-style governance and analytics. | Best target pattern for firms mixing databases, documents, and AI retrieval. |
| Metadata | Data about data, including definitions, lineage, ownership, freshness, and quality. | Prevents agents from using ambiguous fields like rent, occupancy, lead, or renewal inconsistently. |
| Data dictionary | Controlled definitions for fields, metrics, tables, and business terms. | Essential for agent reliability and client trust. |
| Lineage | Trace of where data came from and how it changed. | Lets a reporting or analysis agent justify numbers back to source systems. |
| Data governance | Decision rights, policies, standards, roles, and controls around data. | Required before AI agents touch client, tenant, investor, and transaction data. |
| Data stewardship | Operational responsibility for maintaining quality and meaning of data domains. | Assign stewards for properties, tenants, leases, deals, vendors, and financials. |
| Data quality | Fitness of data for use, often measured by accuracy, completeness, consistency, timeliness, validity, and uniqueness. | Agent answers should degrade or escalate when source quality is weak. |
| Master data | Authoritative core entities shared across systems. | Property, unit, tenant, owner, contact, broker, vendor, and market identities. |
| MDM | Master data management, the discipline of reconciling shared entities across systems. | Prevents duplicate properties, contacts, and leases from corrupting analysis. |
| Dimensional model | Warehouse design using facts and dimensions for analytical queries. | Natural fit for rent roll, occupancy, leasing, maintenance, and financial reporting. |
| Fact table | Table of measurable events or balances. | Examples: rent payments, work orders, leasing activities, valuation snapshots. |
| Dimension table | Descriptive context used to filter and group facts. | Examples: property, unit, tenant, market, date, asset class. |
| Star schema | Dimensional design with central fact tables connected to dimensions. | Keeps business dashboards fast and understandable. |
| OLAP | Analytical processing optimized for slicing, dicing, aggregating, and comparing data. | Supports portfolio drilldowns from region to property to unit. |
| KPI | Key performance indicator tied to a decision or objective. | Agent dashboards should prioritize KPIs tied to action, not decorative metrics. |
| Dashboard | Visual interface for monitoring metrics, trends, exceptions, and decisions. | Primary surface for executives, asset managers, brokers, and property managers. |
| Visual analytics | Use of interactive visualization to support analysis and insight discovery. | Lets users ask follow-up questions from charts and maps. |
| Descriptive analytics | Explains what happened. | Examples: last month's occupancy, leasing velocity, maintenance backlog. |
| Diagnostic analytics | Explains why it happened. | Examples: NOI variance drivers, lead conversion bottlenecks, delinquency causes. |
| Predictive analytics | Estimates what is likely to happen. | Examples: churn risk, rent delinquency risk, lead close probability. |
| Prescriptive analytics | Recommends actions under constraints. | Examples: next-best follow-up, staffing allocation, pricing adjustment workflow. |
| Data mining | Discovery of patterns, relationships, and segments in data. | Useful for tenant segmentation, lead scoring, anomaly detection, and vendor performance. |
| Classification | Predictive task assigning records to categories. | Examples: qualified lead, at-risk tenant, urgent maintenance issue. |
| Regression | Predictive task estimating a numeric value. | Examples: rent, days on market, expected maintenance cost. |
| Clustering | Unsupervised grouping of similar records. | Examples: tenant segments, property peer groups, investor profiles. |
| Association rules | Pattern mining for items or events that co-occur. | Examples: maintenance issue combinations, lead behavior patterns. |
| Anomaly detection | Identification of unusual observations. | Examples: abnormal expense spikes, duplicate invoices, suspicious rent roll changes. |
| Sampling | Selecting a subset to infer patterns about a population. | Important when analyzing surveys, market comps, or inspection samples. |
| Population | The full group being studied. | Could mean all units, tenants, listings, leads, or transactions. |
| Parameter | Numeric characteristic of a population. | Example: true average rent across a portfolio. |
| Statistic | Numeric characteristic of a sample. | Example: average rent from a selected comp set. |
| Probability | Quantified uncertainty. | Needed for risk-aware agent recommendations. |
| Hypothesis testing | Statistical method for assessing whether evidence supports a claim. | Useful for campaign tests, operational changes, and pricing experiments. |
| Confidence interval | Range of plausible values for an estimated quantity. | Prevents agents from presenting comp estimates with false precision. |
| Correlation | Measure of association between variables. | Helpful but not causal; agents must avoid overclaiming. |
| Causation | A relationship where one factor produces change in another. | Requires design or evidence stronger than dashboard correlation. |
| R | Statistical programming environment used for analysis and modeling. | Relevant for deeper analytical prototypes, though production may use Python/SQL. |
| Hadoop | Distributed storage and processing ecosystem for large datasets. | Historical big-data foundation; concepts matter even if modern stacks differ. |
| MapReduce | Distributed processing pattern that maps work across data partitions and reduces results. | Conceptual base for scalable analytics jobs. |
| Cloud analytics | Analytics services delivered through cloud compute, storage, and managed data platforms. | Likely operating model for multi-client AI-agent deployments. |
| Serverless query | Query service where infrastructure management is abstracted away. | Useful for ad hoc analysis over data lakes and client exports. |
| Streaming data | Continuously arriving data processed near real time. | Useful for lead events, IoT/property sensors, portal activity, and agent logs. |
| Batch processing | Scheduled processing of accumulated data. | Works for daily rent roll, accounting, CRM, and investor reporting loads. |
| Semantic layer | Business-friendly metric and entity layer between raw data and users/tools. | Keeps agents from inventing metric definitions. |
| Feature store | Managed repository of model-ready variables. | Useful for churn, lead scoring, delinquency, and pricing models. |
| Vector store | Database optimized for semantic embeddings. | Needed for lease retrieval, policy search, knowledge-base agents, and document Q&A. |
| Retrieval augmented generation | LLM pattern that grounds answers in retrieved source material. | Mandatory for lease, policy, reporting, and client-specific agents. |
| Agent | AI system that uses models, tools, memory, retrieval, and workflows to complete tasks. | The business product: managed agents that act on business data under controls. |
| Tool use | Agent capability to call APIs, databases, documents, or workflow systems. | Turns a chat assistant into an operational business worker. |
| Human in the loop | Required human review or approval for sensitive or high-impact actions. | Use for Fair Housing-sensitive, financial, legal, pricing, and client communication decisions. |
| Audit log | Record of data access, reasoning context, tool calls, outputs, and approvals. | Required to manage agent risk and client accountability. |
| Model drift | Performance degradation when input patterns change. | Monitor as markets, tenant behavior, and client operations shift. |
| Fair Housing | US anti-discrimination framework affecting housing-related decisions and communications. | Any leasing, tenant, or lead agent needs explicit safeguards and legal review. |
