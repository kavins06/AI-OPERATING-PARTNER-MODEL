# AI Operating Partner Template Index

Use this index to keep artifacts aligned to the 16-step engagement. Machine-readable YAML or CSV artifacts are the source of truth unless a file name explicitly says `view`.

| Step | Canonical Templates | Generated Or Supporting Views |
|---|---|---|
| 1. Executive opportunity terrain mapping | `01-executive-opportunity-terrain.md`, `01-org-structure-capture.csv` |  |
| 2. Opportunity terrain synthesis and discovery-zone sequencing | `02-opportunity-terrain-synthesis.md`, `02-interview-coverage-matrix.csv` |  |
| 3. Role-aware AI-led interviews | `03-role-interview-guide.md`, `03-edge-case-register.csv`, `03-interview-evidence-need-log.csv`, `03-source-access-register.csv` | `03-ai-interviewer-system-prompt.md` |
| 4. Planning-evidence follow-up | `04-artifact-follow-up-request.md`, `04-artifact-follow-up-request.csv` |  |
| 5. AI-native workflow intelligence object | `05-ai-workflow-spec.yaml` |  |
| 6. Organizational intelligence diagnostic | `06-organizational-intelligence-diagnostic.yaml` |  |
| 7. Controlled validation and governance resolution | `07-source-inventory.csv`, `07-validation-event.yaml` | `07-controlled-validation-call-view.md` |
| 8. AI knowledge and guideline requirements map | `08-knowledge-map.md` |  |
| 9. AI guidance pack | `09-ai-guidance-spec.yaml`, `09-ai-guidance-test-cases.yaml` | `09-ai-guidance-skill.md` |
| 10. Measurement intelligence and analytics readiness | `10-measurement-intelligence.yaml`, `10-kpi-dictionary.csv` |  |
| 11. Business value case | `11-business-value-case.yaml` |  |
| 12. Technical implementation blueprint | `12-technical-implementation-blueprint.yaml` |  |
| 13. Risk and control model | `13-risk-control-model.yaml`, `13-risk-register.csv` |  |
| 14. AI-agent readiness score | `14-ai-agent-readiness-score.yaml`, `14-readiness-scorecard.csv` |  |
| 15. Machine-readable implementation decision packet | `15-implementation-decision-packet.yaml` | `15-build-ready-implementation-brief-view.md` |
| 16. Machine-readable managed lifecycle object | `16-managed-lifecycle-object.yaml` | `16-managed-lifecycle-sop-view.md` |

Cleanup rules:

- Keep step numbers tied to the step where the artifact is created, not where it might be used later.
- Treat `view` files as generated human-readable projections, not canonical planning records.
- Do not add build-phase templates here unless they remain explicitly pre-build planning artifacts.
