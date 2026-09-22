# Dashboard And KPI Standards For Business AI-Agent Products

Traceability anchors: dashboard sources (`0_n6qtnjrs`, `1_8nlrdrtj`, `1_mvkxpvok`, `1_s0v3fwb6`, `25_dashboard_design_principle`, `dashboard_building_principles`), BI/reporting transcripts (`0_n6qtnjrs`, `1_8nlrdrtj`, `1_bjyscj13`, `1_pciyc4os`, `1_s0v3fwb6`), statistics (`1_x12ywfi6`, `review_of_statistics_1`).

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
