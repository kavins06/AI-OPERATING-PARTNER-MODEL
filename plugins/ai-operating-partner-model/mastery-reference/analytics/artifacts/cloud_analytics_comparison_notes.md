# Cloud Analytics Comparison Notes For Business AI-Agent Stacks

Traceability anchors: AWS/GCP course materials (`0_kjkmxro4`, `0_ps4eqwt7`, `1_pciyc4os`, `1_qfxdmxya`, `1_s0v3fwb6`, `aws_data_analytics_products`, `big_data_architecture_resources`, `dashboard_building_principles`, `google_cloud_platform`).

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
