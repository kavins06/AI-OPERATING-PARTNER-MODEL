from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parents[1]
TEXT_DIR = OUT / "source_text"
REPORT_DIR = OUT / "reports"
SUMMARY_DIR = OUT / "summaries"
ARTIFACT_DIR = OUT / "artifacts"


STOPWORDS = {
    "about", "above", "after", "again", "against", "also", "because", "been", "before",
    "being", "between", "business", "course", "could", "data", "each", "from", "have",
    "into", "more", "most", "other", "page", "should", "some", "such", "than", "that",
    "their", "there", "these", "they", "this", "through", "using", "very", "were",
    "what", "when", "where", "which", "while", "will", "with", "would", "your",
    "the", "and", "for", "are", "can", "not", "you", "all", "any", "our", "its",
    "has", "had", "was", "one", "two", "may", "use", "used", "pdf", "docx", "pptx",
    "classification", "extraction",
}


GLOSSARY = [
    ("Analytics", "Systematic use of data, models, and reasoning to describe, predict, or prescribe decisions.", "Frames every business agent as a decision system, not just a chat interface."),
    ("Business intelligence", "Processes, data stores, dashboards, and tools that turn operational data into decision-ready information.", "Core layer for portfolio, brokerage, property management, and investor reporting agents."),
    ("Big data", "High-volume, high-velocity, high-variety data that exceeds simple spreadsheet or single-system handling.", "Applies to listings, rent rolls, documents, tenant interactions, maintenance logs, and external market feeds."),
    ("Data warehouse", "Integrated, historical, query-optimized repository for reporting and analysis.", "Backbone for NOI, occupancy, leasing, rent collection, and performance dashboards."),
    ("Data mart", "A subject-specific analytical store, often derived from a warehouse.", "Useful for property management, brokerage pipeline, investor reporting, or asset management views."),
    ("ETL", "Extract, transform, and load pipeline that moves data from source systems into analytical structures.", "Needed to clean CRM, MLS, accounting, property management, and document metadata."),
    ("ELT", "Extract, load, then transform inside a warehouse or lakehouse.", "Often simpler for cloud analytics stacks with raw source retention."),
    ("Data lake", "Low-cost storage for raw structured, semi-structured, and unstructured data.", "Good landing zone for leases, PDFs, emails, listings, images, and logs before refinement."),
    ("Lakehouse", "Architecture combining lake storage flexibility with warehouse-style governance and analytics.", "Best target pattern for firms mixing databases, documents, and AI retrieval."),
    ("Metadata", "Data about data, including definitions, lineage, ownership, freshness, and quality.", "Prevents agents from using ambiguous fields like rent, occupancy, lead, or renewal inconsistently."),
    ("Data dictionary", "Controlled definitions for fields, metrics, tables, and business terms.", "Essential for agent reliability and client trust."),
    ("Lineage", "Trace of where data came from and how it changed.", "Lets a reporting or analysis agent justify numbers back to source systems."),
    ("Data governance", "Decision rights, policies, standards, roles, and controls around data.", "Required before AI agents touch client, tenant, investor, and transaction data."),
    ("Data stewardship", "Operational responsibility for maintaining quality and meaning of data domains.", "Assign stewards for properties, tenants, leases, deals, vendors, and financials."),
    ("Data quality", "Fitness of data for use, often measured by accuracy, completeness, consistency, timeliness, validity, and uniqueness.", "Agent answers should degrade or escalate when source quality is weak."),
    ("Master data", "Authoritative core entities shared across systems.", "Property, unit, tenant, owner, contact, broker, vendor, and market identities."),
    ("MDM", "Master data management, the discipline of reconciling shared entities across systems.", "Prevents duplicate properties, contacts, and leases from corrupting analysis."),
    ("Dimensional model", "Warehouse design using facts and dimensions for analytical queries.", "Natural fit for rent roll, occupancy, leasing, maintenance, and financial reporting."),
    ("Fact table", "Table of measurable events or balances.", "Examples: rent payments, work orders, leasing activities, valuation snapshots."),
    ("Dimension table", "Descriptive context used to filter and group facts.", "Examples: property, unit, tenant, market, date, asset class."),
    ("Star schema", "Dimensional design with central fact tables connected to dimensions.", "Keeps business dashboards fast and understandable."),
    ("OLAP", "Analytical processing optimized for slicing, dicing, aggregating, and comparing data.", "Supports portfolio drilldowns from region to property to unit."),
    ("KPI", "Key performance indicator tied to a decision or objective.", "Agent dashboards should prioritize KPIs tied to action, not decorative metrics."),
    ("Dashboard", "Visual interface for monitoring metrics, trends, exceptions, and decisions.", "Primary surface for executives, asset managers, brokers, and property managers."),
    ("Visual analytics", "Use of interactive visualization to support analysis and insight discovery.", "Lets users ask follow-up questions from charts and maps."),
    ("Descriptive analytics", "Explains what happened.", "Examples: last month's occupancy, leasing velocity, maintenance backlog."),
    ("Diagnostic analytics", "Explains why it happened.", "Examples: NOI variance drivers, lead conversion bottlenecks, delinquency causes."),
    ("Predictive analytics", "Estimates what is likely to happen.", "Examples: churn risk, rent delinquency risk, lead close probability."),
    ("Prescriptive analytics", "Recommends actions under constraints.", "Examples: next-best follow-up, staffing allocation, pricing adjustment workflow."),
    ("Data mining", "Discovery of patterns, relationships, and segments in data.", "Useful for tenant segmentation, lead scoring, anomaly detection, and vendor performance."),
    ("Classification", "Predictive task assigning records to categories.", "Examples: qualified lead, at-risk tenant, urgent maintenance issue."),
    ("Regression", "Predictive task estimating a numeric value.", "Examples: rent, days on market, expected maintenance cost."),
    ("Clustering", "Unsupervised grouping of similar records.", "Examples: tenant segments, property peer groups, investor profiles."),
    ("Association rules", "Pattern mining for items or events that co-occur.", "Examples: maintenance issue combinations, lead behavior patterns."),
    ("Anomaly detection", "Identification of unusual observations.", "Examples: abnormal expense spikes, duplicate invoices, suspicious rent roll changes."),
    ("Sampling", "Selecting a subset to infer patterns about a population.", "Important when analyzing surveys, market comps, or inspection samples."),
    ("Population", "The full group being studied.", "Could mean all units, tenants, listings, leads, or transactions."),
    ("Parameter", "Numeric characteristic of a population.", "Example: true average rent across a portfolio."),
    ("Statistic", "Numeric characteristic of a sample.", "Example: average rent from a selected comp set."),
    ("Probability", "Quantified uncertainty.", "Needed for risk-aware agent recommendations."),
    ("Hypothesis testing", "Statistical method for assessing whether evidence supports a claim.", "Useful for campaign tests, operational changes, and pricing experiments."),
    ("Confidence interval", "Range of plausible values for an estimated quantity.", "Prevents agents from presenting comp estimates with false precision."),
    ("Correlation", "Measure of association between variables.", "Helpful but not causal; agents must avoid overclaiming."),
    ("Causation", "A relationship where one factor produces change in another.", "Requires design or evidence stronger than dashboard correlation."),
    ("R", "Statistical programming environment used for analysis and modeling.", "Relevant for deeper analytical prototypes, though production may use Python/SQL."),
    ("Hadoop", "Distributed storage and processing ecosystem for large datasets.", "Historical big-data foundation; concepts matter even if modern stacks differ."),
    ("MapReduce", "Distributed processing pattern that maps work across data partitions and reduces results.", "Conceptual base for scalable analytics jobs."),
    ("Cloud analytics", "Analytics services delivered through cloud compute, storage, and managed data platforms.", "Likely operating model for multi-client AI-agent deployments."),
    ("Serverless query", "Query service where infrastructure management is abstracted away.", "Useful for ad hoc analysis over data lakes and client exports."),
    ("Streaming data", "Continuously arriving data processed near real time.", "Useful for lead events, IoT/property sensors, portal activity, and agent logs."),
    ("Batch processing", "Scheduled processing of accumulated data.", "Works for daily rent roll, accounting, CRM, and investor reporting loads."),
    ("Semantic layer", "Business-friendly metric and entity layer between raw data and users/tools.", "Keeps agents from inventing metric definitions."),
    ("Feature store", "Managed repository of model-ready variables.", "Useful for churn, lead scoring, delinquency, and pricing models."),
    ("Vector store", "Database optimized for semantic embeddings.", "Needed for lease retrieval, policy search, knowledge-base agents, and document Q&A."),
    ("Retrieval augmented generation", "LLM pattern that grounds answers in retrieved source material.", "Mandatory for lease, policy, reporting, and client-specific agents."),
    ("Agent", "AI system that uses models, tools, memory, retrieval, and workflows to complete tasks.", "The business product: managed agents that act on business data under controls."),
    ("Tool use", "Agent capability to call APIs, databases, documents, or workflow systems.", "Turns a chat assistant into an operational business worker."),
    ("Human in the loop", "Required human review or approval for sensitive or high-impact actions.", "Use for Fair Housing-sensitive, financial, legal, pricing, and client communication decisions."),
    ("Audit log", "Record of data access, reasoning context, tool calls, outputs, and approvals.", "Required to manage agent risk and client accountability."),
    ("Model drift", "Performance degradation when input patterns change.", "Monitor as markets, tenant behavior, and client operations shift."),
    ("Fair Housing", "US anti-discrimination framework affecting housing-related decisions and communications.", "Any leasing, tenant, or lead agent needs explicit safeguards and legal review."),
]


def ensure_dirs() -> None:
    for d in (SUMMARY_DIR, ARTIFACT_DIR, REPORT_DIR):
        d.mkdir(parents=True, exist_ok=True)


def load_records() -> list[dict]:
    path = REPORT_DIR / "source_inventory.json"
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}. Run ingest_corpus.py first.")
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(source_id: str) -> str:
    path = TEXT_DIR / f"{source_id}.md"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def words(text: str) -> list[str]:
    return [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9_-]{2,}", text) if w.lower() not in STOPWORDS]


def top_terms(text: str, n: int = 10) -> list[str]:
    counts = Counter(words(text))
    return [term for term, _ in counts.most_common(n)]


def interesting_lines(text: str, n: int = 8) -> list[str]:
    candidates = []
    for line in text.splitlines():
        line = re.sub(r"\s+", " ", line.strip())
        if not line or line.startswith("#") or line.startswith("---"):
            continue
        if line.lower().startswith(("classification:", "extraction:")):
            continue
        if len(line) < 25 or len(line) > 180:
            continue
        if re.search(r"\d{2}:\d{2}:\d{2}", line):
            continue
        score = 0
        if re.search(r"\b(data|analytics|warehouse|dashboard|governance|statistics|cloud|model|architecture|business intelligence|big data)\b", line.lower()):
            score += 2
        if line[:1].isupper():
            score += 1
        if len(line.split()) <= 14:
            score += 1
        candidates.append((score, line))
    seen = set()
    result = []
    for _, line in sorted(candidates, key=lambda x: (-x[0], x[1])):
        key = line.lower()
        if key in seen:
            continue
        seen.add(key)
        result.append(line)
        if len(result) >= n:
            break
    return result


def focus_for(record: dict, text: str) -> tuple[list[str], list[str]]:
    name = record["file_name"].lower()
    classification = record["classification"].lower()
    core: list[str] = []
    business: list[str] = []
    if "statistics" in classification or "statistics" in name:
        core = [
            "Statistical foundations: populations, samples, descriptive measures, probability, inference, and model-aware thinking.",
            "Practical analysis skill: use statistical reasoning to separate signal from noise before trusting dashboards or model outputs.",
        ]
        business = [
            "Use for lead scoring, tenant churn, rent and comp estimation, A/B tests, and confidence-aware agent recommendations.",
            "Require agents to communicate uncertainty and avoid treating sample-based estimates as facts.",
        ]
    elif "dashboard" in classification or "dashboard" in name:
        core = [
            "Dashboard design: audience-first KPI selection, visual hierarchy, context, comparison, simplicity, and actionability.",
            "Visual analytics: dashboards should support decisions, not just display available metrics.",
        ]
        business = [
            "Create executive, property manager, brokerage, asset management, and investor dashboards with role-specific KPIs.",
            "Agents should explain dashboard exceptions and recommend next investigative steps.",
        ]
    elif "governance" in classification or "governance" in name:
        core = [
            "Data governance: ownership, stewardship, definitions, quality, lineage, access, policy, and organizational accountability.",
            "Big data increases the need for governance because variety and velocity make unmanaged data riskier.",
        ]
        business = [
            "Define owners for property, tenant, lease, investor, vendor, and financial data before deploying agents.",
            "Use governance controls for PII, Fair Housing-sensitive workflows, lease documents, and auditability.",
        ]
    elif "warehousing" in classification or "warehousing" in name:
        core = [
            "Data warehousing: integrated historical data, dimensional modeling, ETL/ELT, subject orientation, and analytical access.",
            "Warehouse architecture converts fragmented source systems into trusted reporting and analysis layers.",
        ]
        business = [
            "Build fact/dimension models for rent roll, leasing, occupancy, maintenance, financials, valuation, and agent activity.",
            "Ground agents in governed warehouse metrics before allowing operational action.",
        ]
    elif "cloud" in classification or "aws" in name or "google" in name:
        core = [
            "Cloud analytics: managed storage, query, processing, BI, streaming, and machine-learning services.",
            "Service choice should follow workload needs: batch, streaming, ad hoc SQL, warehouse, BI, or model workflows.",
        ]
        business = [
            "Use cloud primitives to support multi-client ingestion, secure storage, scalable analytics, and agent tool APIs.",
            "Keep service comparisons capability-based and validate current product names/pricing before client proposals.",
        ]
    elif "textbook" in classification:
        core = [
            "Managerial BI/analytics perspective: decision support, data warehousing, visualization, data mining, big data, analytics strategy, and organizational adoption.",
            "Connects technical analytics methods to business value, managerial decision-making, and implementation discipline.",
        ]
        business = [
            "Use as the backbone for the full operating model: data foundation, analytics use cases, dashboards, predictive models, governance, and adoption.",
            "Translate each analytics capability into business workflows with measurable business decisions.",
        ]
    elif "video transcript" in classification:
        terms = set(top_terms(text, 20))
        topic = "BI and analytics"
        if terms & {"warehouse", "warehousing", "etl"}:
            topic = "data warehousing"
        elif terms & {"governance", "dictionary", "quality"}:
            topic = "data governance"
        elif terms & {"hadoop", "cloud", "architecture"}:
            topic = "big data architecture"
        elif terms & {"dashboard", "visual", "reporting"}:
            topic = "reporting and visual analytics"
        elif terms & {"mining", "predictive", "model"}:
            topic = "data mining and analytics"
        core = [
            f"Course lecture transcript focused on {topic}.",
            "Useful for managerial framing, practical examples, and instructor emphasis around implementation choices.",
        ]
        business = [
            "Convert the lecture emphasis into client discovery questions and operational agent requirements.",
            "Use examples as prompts for scenario tests and explainers.",
        ]
    else:
        core = [
            "Supporting source for the BI, big data, analytics, and implementation corpus.",
            "Contributes terminology, examples, or external references for architecture and delivery.",
        ]
        business = [
            "Use as supporting context when designing business data systems and agent playbooks.",
            "Map any external references to modern equivalents before client use.",
        ]
    return core, business


def source_refs(records: list[dict], patterns: list[str]) -> str:
    hits = []
    for r in records:
        hay = f"{r['file_name']} {r['classification']} {load_text(r['source_id'])[:3000]}".lower()
        if any(p.lower() in hay for p in patterns):
            hits.append(r["source_id"])
    if not hits:
        return "supporting sources across corpus"
    return ", ".join(f"`{h}`" for h in hits[:10])


def write_source_summaries(records: list[dict]) -> None:
    lines = ["# Source-by-Source Mastery Summaries\n"]
    lines.append("Each source below includes a traceability tag matching files in `mastery_base/source_text/` and `mastery_base/chunks/`.\n")
    for r in records:
        text = load_text(r["source_id"])
        terms = top_terms(text)
        signals = interesting_lines(text)
        core, business = focus_for(r, text)
        lines.append(f"## `{r['source_id']}`")
        lines.append(f"- File: `{r['file_name']}`")
        lines.append(f"- Type: {r['classification']}; extraction: {r['extraction_method']} ({r['extraction_status']}); chunks: {r['chunks']}")
        lines.append(f"- Top extracted terms: {', '.join(terms) if terms else 'not enough extracted text'}")
        lines.append("- What I learned from it:")
        lines.extend(f"  - {item}" for item in core)
        if signals:
            lines.append("- Extracted signals:")
            lines.extend(f"  - {s}" for s in signals[:5])
        lines.append("- Business AI-agent leverage:")
        lines.extend(f"  - {item}" for item in business)
        lines.append("")
    (SUMMARY_DIR / "source_summaries.md").write_text("\n".join(lines), encoding="utf-8")


def write_concept_map(records: list[dict]) -> None:
    sections = [
        ("1. Decision Support And BI Value", "BI exists to improve managerial decisions by turning operational facts into trusted, timely, role-specific insight. In business, that means agents should answer questions in the language of owners, brokers, property managers, investors, and operators.", ["business intelligence", "decision", "managerial", "value"]),
        ("2. Data Foundation", "Operational systems feed analytics through ingestion, integration, metadata, data quality checks, and shared definitions. Without this layer, agents will confidently answer from fragmented or contradictory data.", ["etl", "integration", "metadata", "dictionary", "quality"]),
        ("3. Warehouse/Lakehouse Core", "Historical, governed analytical data should be modeled around facts and dimensions, with raw document and event data retained for AI retrieval and future use.", ["warehouse", "warehousing", "etl", "data mart"]),
        ("4. Governance And Trust", "Governance defines owners, stewards, definitions, quality thresholds, security, lineage, privacy, and escalation rules. It is the trust system for every agent output.", ["governance", "steward", "quality", "privacy"]),
        ("5. Cloud Analytics Platform", "Cloud services provide storage, SQL, batch, streaming, BI, and ML capabilities. The right architecture is workload-driven, not vendor-driven.", ["aws", "google", "cloud", "athena", "redshift", "bigquery"]),
        ("6. Statistics And Modeling", "Statistics supplies the discipline for uncertainty, sampling, inference, relationships, and model evaluation. It prevents dashboards and AI outputs from becoming confident guesswork.", ["statistics", "probability", "sample", "regression", "hypothesis"]),
        ("7. Data Mining And Predictive Analytics", "Pattern discovery and predictive modeling convert historical data into forecasts, segments, risk scores, and recommended actions.", ["mining", "classification", "predictive", "model", "cluster"]),
        ("8. Dashboards And Visual Analytics", "Dashboards should be designed around audience, KPI purpose, context, comparison, and action. Agents can make dashboards conversational and investigative.", ["dashboard", "visual", "reporting", "kpi"]),
        ("9. Agentic Business Operating Layer", "AI agents sit above governed data, retrieval, analytics, dashboards, and workflow tools. They must cite sources, use approved tools, log actions, and escalate sensitive decisions.", ["agent", "ai", "analytics", "governance"]),
    ]
    lines = ["# Cross-Corpus Concept Map\n"]
    for title, body, pats in sections:
        lines.append(f"## {title}")
        lines.append(body)
        lines.append(f"Supporting source tags: {source_refs(records, pats)}")
        lines.append("")
    lines.append("## Operating Flow")
    lines.append("Source systems -> ingestion -> raw store -> quality and metadata -> warehouse/lakehouse -> semantic metrics -> dashboards and models -> AI agents -> audited actions and feedback.")
    (SUMMARY_DIR / "concept_map.md").write_text("\n".join(lines), encoding="utf-8")


def write_glossary() -> None:
    lines = ["# BI, Big Data, Analytics, And Business AI-Agent Glossary\n"]
    lines.append("| Term | Working definition | Business AI-agent use |")
    lines.append("|---|---|---|")
    for term, definition, use in GLOSSARY:
        lines.append(f"| {term} | {definition} | {use} |")
    (SUMMARY_DIR / "glossary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_synthesis(records: list[dict]) -> None:
    text = f"""# Cross-Source Synthesis

## The Master Operating Model
The corpus points to one practical architecture: business decisions sit at the top, trusted data sits underneath, and analytics methods connect the two. For a business AI-agent company, the agent is not the foundation. The foundation is governed data, clear definitions, quality controls, analytical models, and dashboards that already make business meaning explicit.

## What The Sources Converge On
- BI and analytics must start with business questions, not tools. Business agents should be scoped around decisions such as lead prioritization, tenant retention, maintenance triage, NOI variance, investor reporting, and market comparison.
- Warehousing and integration are the reliability layer. If property, lease, tenant, broker, vendor, and financial entities are not reconciled, an agent cannot be trusted.
- Governance is not optional. The sources on big-data governance and small-business governance both imply that ownership, definitions, stewardship, quality, and access controls must be right-sized to the organization.
- Dashboard design is a communication discipline. KPIs need context, hierarchy, and actionability; agents should explain and investigate dashboards rather than replace visual evidence.
- Statistics and data mining provide the modeling discipline. Predictive agents need uncertainty, evaluation, and a distinction between correlation and causal claims.
- Cloud analytics supplies scalable implementation options, but cloud product choices must follow workload needs and must be revalidated before modern client proposals.

## Business Translation
The business firm is a data ecosystem: CRM, MLS/listings, property management, accounting, leases, maintenance, marketing, investor reporting, external market data, and user activity logs. The AI-agent company should offer managed agents only after mapping those systems into a governed analytical architecture. The strongest product is not a generic chatbot; it is a managed decision layer that can retrieve evidence, query metrics, run approved tools, produce dashboards or explanations, and leave an audit trail.

## Traceability
This synthesis is grounded in the inventory at `mastery_base/reports/source_inventory.md`, the extracted source text under `mastery_base/source_text/`, and the chunks under `mastery_base/chunks/`.
"""
    (SUMMARY_DIR / "cross_source_synthesis.md").write_text(text, encoding="utf-8")


def write_use_case_catalog(records: list[dict]) -> None:
    text = f"""# Business AI-Agent Use Case Catalog

Traceability anchors: BI/managerial analytics ({source_refs(records, ["business intelligence", "managerial", "analytics"])}), warehousing ({source_refs(records, ["warehouse", "warehousing"])}), governance ({source_refs(records, ["governance"])}), dashboards ({source_refs(records, ["dashboard", "visual"])}), statistics/data mining ({source_refs(records, ["statistics", "mining", "predictive"])}).

## Brokerage And Leasing
| Agent | Job | Required data | Guardrails | Success metric |
|---|---|---|---|---|
| Lead qualification agent | Scores, summarizes, and routes inbound leads. | CRM, web forms, listing views, contact history, broker availability. | Fair Housing-safe language, no protected-class inference, human approval for sensitive communications. | Response time, conversion rate, qualified appointment rate. |
| Comp research agent | Retrieves comparable listings/sales/leases and drafts a comparison memo. | MLS/listing feeds, internal deals, market data, property attributes. | Cite comps, expose uncertainty, require analyst review before external use. | Time to comp packet, analyst acceptance rate. |
| Follow-up agent | Recommends next outreach and drafts context-aware messages. | CRM activities, lead status, property preferences, campaign data. | Approved templates, opt-out handling, Fair Housing review. | Follow-up completion, reply rate, meeting rate. |

## Property Management
| Agent | Job | Required data | Guardrails | Success metric |
|---|---|---|---|---|
| Work-order triage agent | Classifies maintenance requests, detects urgency, routes vendors. | Work orders, unit/property data, vendor SLAs, tenant messages. | Emergency escalation, no unauthorized vendor dispatch, audit log. | Time to triage, SLA compliance, resident satisfaction. |
| Tenant support agent | Answers policy, lease, payment, and maintenance questions from approved sources. | Lease docs, policy docs, tenant ledger, knowledge base. | Retrieval citations, privacy controls, human handoff. | Deflection rate, resolution time, escalation quality. |
| Delinquency risk agent | Flags accounts likely to miss payment or require outreach. | Ledger, payment history, lease terms, communications. | Compliance review, no discriminatory features, human approval. | Collection rate, reduced days delinquent. |

## Asset Management And Investment
| Agent | Job | Required data | Guardrails | Success metric |
|---|---|---|---|---|
| NOI variance explainer | Explains actual-to-budget variance and suggests investigation paths. | GL, budgets, rent roll, occupancy, work orders. | Source-linked calculations, finance review. | Close/reporting cycle time, analyst acceptance rate. |
| Portfolio KPI agent | Answers performance questions across properties and markets. | Warehouse metrics, semantic layer, dashboards. | Metric definitions, lineage, row-level security. | Executive self-service rate, fewer ad hoc report requests. |
| Acquisition screen agent | Summarizes deal materials and runs first-pass fit checks. | Offering memos, comps, market assumptions, investment criteria. | Human investment committee review, current-market validation. | Screen throughput, false-positive reduction. |

## Development, Lending, And Operations
| Agent | Job | Required data | Guardrails | Success metric |
|---|---|---|---|---|
| Development tracker agent | Monitors entitlement, budget, schedule, and issue logs. | Project plans, permits, budgets, vendor updates. | No legal conclusions, escalation for blockers. | Issue aging, schedule variance visibility. |
| Loan package agent | Extracts and checks rent rolls, financials, leases, and covenant data. | Loan docs, financial statements, rent roll, property data. | Underwriter approval, calculation traceability. | Package prep time, exception detection. |
| Data quality agent | Finds duplicate records, stale fields, missing definitions, and pipeline failures. | Warehouse metadata, source extracts, data dictionary. | Steward workflow, no silent overwrites. | Quality score, issue closure time. |
"""
    (ARTIFACT_DIR / "business_ai_agent_use_case_catalog.md").write_text(text, encoding="utf-8")


def write_architecture(records: list[dict]) -> None:
    text = f"""# Business Data Architecture Patterns For Managed AI Agents

Traceability anchors: warehousing ({source_refs(records, ["warehouse", "warehousing", "etl"])}), big-data architecture ({source_refs(records, ["hadoop", "architecture", "big data"])}), governance ({source_refs(records, ["governance", "quality", "dictionary"])}), cloud analytics ({source_refs(records, ["aws", "google", "cloud"])}).

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
"""
    (ARTIFACT_DIR / "data_architecture_patterns.md").write_text(text, encoding="utf-8")


def write_governance(records: list[dict]) -> None:
    text = f"""# Governance And Privacy Checklist For Business AI Agents

Traceability anchors: data governance ({source_refs(records, ["governance", "steward", "dictionary", "quality"])}), small-business governance ({source_refs(records, ["small business", "small businesses"])}), big-data governance ({source_refs(records, ["big data governance", "roadmap"])}).

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
"""
    (ARTIFACT_DIR / "governance_privacy_checklist.md").write_text(text, encoding="utf-8")


def write_dashboards(records: list[dict]) -> None:
    text = f"""# Dashboard And KPI Standards For Business AI-Agent Products

Traceability anchors: dashboard sources ({source_refs(records, ["dashboard", "visual", "kpi"])}), BI/reporting transcripts ({source_refs(records, ["reporting", "visual analytics"])}), statistics ({source_refs(records, ["statistics", "probability"])}).

## Design Rules
- Start with the audience and decision: executive, asset manager, property manager, broker, investor, or operations lead.
- Show only KPIs that drive action.
- Provide context: target, prior period, benchmark, trend, and exception threshold.
- Use consistent metric definitions from the semantic layer.
- Prefer clear comparisons over decorative charts.
- Keep labels, units, filters, and dates visible.
- Make drilldowns predictable: portfolio -> market -> property -> unit/tenant/deal.
- Let agents explain anomalies, but keep the visual evidence available.

## Core Dashboard Types
| Dashboard | Primary audience | Core KPIs | Agent role |
|---|---|---|---|
| Portfolio executive | Owners, executives | NOI, occupancy, rent collection, budget variance, delinquency, capex, leasing velocity | Explain performance, summarize exceptions, prepare investor narrative. |
| Property operations | Property managers | Work-order backlog, SLA compliance, make-ready status, delinquency, occupancy, resident issues | Triage tasks, recommend follow-up, draft updates. |
| Brokerage pipeline | Brokers, team leads | leads, appointments, conversion, days on market, listing activity, pipeline value | Prioritize leads, draft outreach, explain conversion drop-offs. |
| Asset management variance | Asset managers | actual vs budget, revenue variance, expense variance, renewal exposure, lease rollover | Identify drivers and next investigations. |
| Investor reporting | Investor relations | distributions, capital calls, performance, occupancy, major events | Draft source-linked updates and answer investor questions. |
| Agent operations | Internal AI ops | tool success, escalation rate, correction rate, latency, cost, unresolved cases | Monitor managed-agent health and client value. |

## KPI Definition Template
For every KPI, define:
- Business question.
- Formula.
- Grain.
- Source system.
- Refresh cadence.
- Owner.
- Data quality checks.
- Allowed filters.
- Thresholds.
- Agent permissions.
"""
    (ARTIFACT_DIR / "dashboard_kpi_standards.md").write_text(text, encoding="utf-8")


def write_lakehouse(records: list[dict]) -> None:
    text = f"""# Data Warehouse / Lakehouse Blueprint For Business Firms

Traceability anchors: warehousing ({source_refs(records, ["warehouse", "etl", "data mart"])}), cloud analytics ({source_refs(records, ["aws", "google", "cloud"])}), governance ({source_refs(records, ["governance", "dictionary"])}).

## Blueprint
1. Source inventory: list every CRM, property management, accounting, document, listing, marketing, and external data source.
2. Data contracts: define fields, refresh cadence, access method, owner, and expected quality.
3. Raw zone: store immutable source snapshots and files.
4. Standardized zone: clean, type, deduplicate, and reconcile core entities.
5. Analytical zone: dimensional models and marts for reporting.
6. Document intelligence zone: OCR, metadata, embeddings, and retrieval indexes.
7. Semantic layer: approved metrics and business terms.
8. Agent tools: SQL, retrieval, workflow, dashboard, and notification tools.
9. Governance and monitoring: lineage, quality, access, cost, usage, and audit logs.

## Recommended Build Order
- Week 1 equivalent: inventory and data dictionary.
- Week 2 equivalent: core property, unit, tenant, lease, date, and market dimensions.
- Week 3 equivalent: rent roll, occupancy, leasing, maintenance, and finance facts.
- Week 4 equivalent: dashboard layer and first read-only agents.
- After trust is proven: write-back workflows with approval gates.

## Non-Negotiables
- No agent uses undefined metrics.
- No agent answers from stale data without saying so.
- No agent acts without audit logging.
- No sensitive workflow launches without human approval.
"""
    (ARTIFACT_DIR / "data_warehouse_lakehouse_blueprint.md").write_text(text, encoding="utf-8")


def write_cloud(records: list[dict]) -> None:
    text = f"""# Cloud Analytics Comparison Notes For Business AI-Agent Stacks

Traceability anchors: AWS/GCP course materials ({source_refs(records, ["aws", "athena", "google cloud", "bigquery", "cloud"])}).

These notes are capability-based because cloud services, pricing, and names change. Validate current details before client proposals.

## Capability Map
| Capability | AWS-style pattern | GCP-style pattern | Business use |
|---|---|---|---|
| Object storage | S3-style storage | Cloud Storage-style storage | Raw exports, leases, offering memos, OCR outputs, logs. |
| Serverless SQL over files | Athena-style query | BigQuery/external-table-style query | Quick analysis over raw client exports. |
| Data warehouse | Redshift-style warehouse | BigQuery-style warehouse | Governed KPIs and dashboards. |
| ETL/catalog | Glue-style catalog/jobs | Dataflow/Dataproc/catalog-style services | Ingestion, transformations, metadata. |
| Stream processing | Kinesis-style streams | Pub/Sub/Dataflow-style streams | Lead events, work orders, agent telemetry. |
| BI | QuickSight-style BI | Looker-style BI | Dashboards and governed metrics. |
| ML/AI | Managed ML and model hosting | Managed ML and model hosting | Scoring, extraction, retrieval, and agent tools. |

## Selection Heuristics
- Choose based on client environment first.
- Prefer managed services for small teams.
- Keep raw data portable.
- Separate storage, compute, semantic definitions, and agent logic.
- Budget for observability and governance, not just model calls.
"""
    (ARTIFACT_DIR / "cloud_analytics_comparison_notes.md").write_text(text, encoding="utf-8")


def write_maturity(records: list[dict]) -> None:
    text = f"""# Client Analytics Maturity Model For Business AI-Agent Readiness

Traceability anchors: managerial BI/analytics ({source_refs(records, ["managerial", "business intelligence"])}), governance ({source_refs(records, ["governance"])}), warehousing ({source_refs(records, ["warehouse"])}), dashboards ({source_refs(records, ["dashboard"])}).

| Level | State | Symptoms | Suitable agent scope | Upgrade path |
|---|---|---|---|---|
| 0 | Spreadsheet chaos | Manual exports, conflicting numbers, no owners. | Narrow document Q&A or internal assistant only. | Source inventory, data dictionary, owner assignment. |
| 1 | Basic reporting | Static reports, limited trust, manual refresh. | Read-only reporting explainer. | Automate ingestion and quality checks. |
| 2 | Warehouse foundation | Integrated data marts, stable KPIs. | KPI Q&A, dashboard explainer, analyst copilot. | Add governance, semantic layer, lineage. |
| 3 | Governed analytics | Owners, stewards, quality rules, access controls. | Client-facing and workflow-support agents. | Add predictive models and feedback loops. |
| 4 | Predictive operations | Scores, forecasts, anomaly detection. | Prioritization, risk, and recommendation agents. | Add approval-based automation. |
| 5 | Agentic operations | Agents use tools, retrieve evidence, act with approvals, and are monitored. | Managed AI-agent operating layer. | Continuous improvement, drift monitoring, productization. |

## Assessment Questions
- What decisions are delayed because data is hard to trust?
- Which systems hold property, lease, tenant, deal, and financial truth?
- Who owns metric definitions?
- How fresh does each use case need to be?
- Which actions require approval?
- What data cannot leave the client environment?
- What would a wrong answer cost?
"""
    (ARTIFACT_DIR / "client_analytics_maturity_model.md").write_text(text, encoding="utf-8")


def write_readiness(records: list[dict]) -> None:
    text = f"""# Mastery Proof: Applied Readiness Scenarios

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
"""
    (ARTIFACT_DIR / "readiness_scenarios.md").write_text(text, encoding="utf-8")


def write_coverage(records: list[dict]) -> None:
    total = len(records)
    complete = sum(1 for r in records if r["extraction_status"] == "complete")
    partial = sum(1 for r in records if r["extraction_status"] == "partial")
    needs = sum(1 for r in records if r["extraction_status"] == "needs_ocr")
    chunks = sum(int(r["chunks"]) for r in records)
    lines = ["# Coverage And Traceability Report\n"]
    lines.append(f"- Sources inventoried: {total}")
    lines.append(f"- Complete extractions: {complete}")
    lines.append(f"- Partial extractions: {partial}")
    lines.append(f"- Needs OCR/unavailable: {needs}")
    lines.append(f"- Total chunks: {chunks}")
    lines.append("")
    lines.append("## Output Files")
    for p in sorted(SUMMARY_DIR.glob("*.md")) + sorted(ARTIFACT_DIR.glob("*.md")):
        lines.append(f"- `{p.relative_to(ROOT)}`")
    lines.append("")
    lines.append("## Traceability Check")
    lines.append("Every summary and artifact references source tags from `mastery_base/reports/source_inventory.md` or the extracted source corpus.")
    (REPORT_DIR / "coverage_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme(records: list[dict]) -> None:
    text = """# Mastery Base

This folder implements the AI-Agent Business BI Mastery Plan.

## Structure
- `source_text/`: extracted text and OCR text from each source.
- `chunks/`: chunked JSONL source material for retrieval or later indexing.
- `summaries/`: source summaries, glossary, concept map, and cross-source synthesis.
- `artifacts/`: business AI-agent business artifacts.
- `reports/`: inventory, coverage, and ingestion logs.
- `tools/`: reusable ingestion and artifact-generation scripts.

## Rebuild
Run:

```powershell
& "C:\\Users\\kavin\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe" "D:\\Business Intelligence Big Data & Analysis\\mastery_base\\tools\\ingest_corpus.py"
& "C:\\Users\\kavin\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe" "D:\\Business Intelligence Big Data & Analysis\\mastery_base\\tools\\build_mastery_artifacts.py"
```

## Note
Modern cloud-service details, legal requirements, and business AI market claims should be web-validated before client-facing use.
"""
    (OUT / "README.md").write_text(text, encoding="utf-8")


def main() -> int:
    ensure_dirs()
    records = load_records()
    write_source_summaries(records)
    write_concept_map(records)
    write_glossary()
    write_synthesis(records)
    write_use_case_catalog(records)
    write_architecture(records)
    write_governance(records)
    write_dashboards(records)
    write_lakehouse(records)
    write_cloud(records)
    write_maturity(records)
    write_readiness(records)
    write_coverage(records)
    write_readme(records)
    print(f"Built mastery artifacts from {len(records)} sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
