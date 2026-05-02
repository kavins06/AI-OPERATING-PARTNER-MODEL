# AI Operating Partner Template Index

Use this index to keep artifacts aligned to the engagement. Machine-readable YAML or CSV artifacts are canonical unless a file name explicitly says `view`. The current method keeps the Step 0-18 process and adds operating contracts, schemas, rubrics, and handoff rules.

> **File-numbering note.** Physical filenames retain legacy numeric prefixes (e.g., `06-blocker-classification-rubric.md` belongs to Step 7; `07-baseline-release-contract.yaml` belongs to Step 8). The Step column in the table below is authoritative; the prefix is historical. New artifacts use the current step number; existing artifacts are not renamed in order to preserve git history and avoid breaking inbound references.

| Step | Canonical Templates | Generated Or Supporting Views |
|---|---|---|
| Cross-step contracts | `halt-taxonomy.yaml`, `offline-proof-catalog.yaml` | `../schemas/canonical-object-schemas.yaml` |
| 0. Engagement tiering and vertical extension | `00-engagement-tiering.yaml`, `00-tier-matrix.yaml`, `regulated-domain-extension.yaml`, `vertical-extension.schema.yaml`, `regulated-domain-extension-real-estate.yaml` |  |
| 1. Executive opportunity terrain mapping | `01-executive-opportunity-terrain.md`, `01-org-structure-capture.csv` |  |
| 2. Opportunity terrain synthesis and candidate use-case shortlist | `02-opportunity-terrain-synthesis.md`, `02-candidate-use-case-shortlist.yaml`, `02-interview-coverage-matrix.csv` |  |
| 3. Role-aware AI-led interviews | `03-role-interview-guide.md`, `03-ai-interviewer-protocol.md`, `03-edge-case-register.csv`, `03-interview-evidence-need-log.csv`, `03-source-access-register.csv` | `03-ai-interviewer-system-prompt.md` |
| 4. Variation mapping | `04-variation-map.yaml` |  |
| 5. Planning-evidence follow-up | `04-artifact-follow-up-request.md`, `04-artifact-follow-up-request.csv` |  |
| 6. AI-native workflow intelligence object | `05-ai-workflow-spec.yaml` |  |
| 7. Organizational intelligence diagnostic | `06-organizational-intelligence-diagnostic.yaml`, `06-blocker-classification-rubric.md` |  |
| 8. Controlled validation, governance resolution, and organizational intelligence baseline | `07-source-inventory.csv`, `07-validation-event.yaml`, `07-organizational-intelligence-baseline.yaml`, `07-baseline-release-contract.yaml` | `07-controlled-validation-call-view.md` |
| 9. AI knowledge and guideline requirements map | `08-knowledge-map.md` |  |
| 10. AI guidance pack | `09-ai-guidance-spec.yaml`, `09-ai-guidance-test-cases.yaml` | `09-ai-guidance-skill.md` |
| 11. Measurement intelligence and AI-capability metric design | `10-measurement-intelligence.yaml`, `10-kpi-dictionary.csv` |  |
| 12. Business value case and portfolio comparison | `11-business-value-case.yaml`, `11-portfolio-comparison.yaml` |  |
| 13. Solution shape and adoption design | `12-solution-shape.yaml`, `13-adoption-design.yaml` |  |
| 14. Technical/vendor implementation blueprint | `12-technical-implementation-blueprint.yaml` |  |
| 15. Risk and control model | `13-risk-control-model.yaml`, `13-risk-register.csv` |  |
| 16. AI-agent readiness score | `14-ai-agent-readiness-score.yaml`, `14-hard-gates-readiness-rubric.yaml`, `14-readiness-scorecard.csv` |  |
| 17. Machine-readable implementation decision packet | `15-implementation-decision-packet.yaml`, `15-implementation-decision-packet-set.yaml`, `15-decision-packet-contracts.yaml` | `15-build-ready-implementation-brief-view.md` |
| 18. Machine-readable managed lifecycle and adoption-change object | `16-managed-lifecycle-object.yaml`, `16-lifecycle-set.yaml`, `16-lifecycle-variant-contracts.yaml`, `18-method-to-build-handoff-contract.md` | `16-managed-lifecycle-sop-view.md` |

Cleanup rules:

- Keep step numbers tied to the file series where the artifact is maintained; legacy file names may remain when the artifact moves in .
- Treat `view` files as generated human-readable projections, not canonical planning records.
- Do not add build-phase templates here unless they remain explicitly pre-build planning artifacts.
- Use `regulated-domain-extension.yaml` as a cross-cutting extension, not as a single isolated risk artifact.
- Treat `assets/schemas/canonical-object-schemas.yaml` as the compatibility contract for machine-readable product and downstream automation objects.
