from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import shorten

from PIL import Image, ImageDraw
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output" / "pdf"
PDF_PATH = OUT_DIR / "ai-operating-partner-visual-process-guide.pdf"
PREVIEW_DIR = OUT_DIR / "previews" / "visual-process-guide"

PAGE_W, PAGE_H = landscape(letter)
M = 0.34 * inch
TOP = PAGE_H - M

COLORS = {
    "ink": colors.HexColor("#1D2733"),
    "muted": colors.HexColor("#667085"),
    "line": colors.HexColor("#CBD5E1"),
    "soft": colors.HexColor("#F7F9FC"),
    "navy": colors.HexColor("#1F3A5F"),
    "blue": colors.HexColor("#2F80ED"),
    "teal": colors.HexColor("#0F766E"),
    "green": colors.HexColor("#2F855A"),
    "amber": colors.HexColor("#A86E12"),
    "red": colors.HexColor("#B83232"),
    "purple": colors.HexColor("#6B46C1"),
    "sky": colors.HexColor("#E8F2FF"),
    "mint": colors.HexColor("#E6FFFA"),
    "sand": colors.HexColor("#FFF8E1"),
    "rose": colors.HexColor("#FFF1F2"),
    "lav": colors.HexColor("#F3E8FF"),
    "white": colors.white,
}

PHASES = [
    ("Frame", "0-2", COLORS["blue"]),
    ("Discover", "3-5", COLORS["teal"]),
    ("Intelligence", "6-8", COLORS["green"]),
    ("Reasoning", "9-10", COLORS["purple"]),
    ("Value", "11-12", COLORS["amber"]),
    ("Shape", "13-15", COLORS["navy"]),
    ("Decide", "16-18", COLORS["red"]),
]


@dataclass(frozen=True)
class Step:
    n: int
    title: str
    phase: str
    purpose: str
    inputs: list[str]
    client: list[str]
    ai: list[str]
    partner: list[str]
    outputs: list[str]
    gate: str
    templates: list[str]
    watchouts: list[str]
    loop: str


STEPS = [
    Step(
        0,
        "Engagement Tiering And Vertical Extension",
        "Frame",
        "Choose the depth, vertical rules, timeline, proof boundary, and no-build rules before discovery starts.",
        ["Sponsor goals", "Org size", "Budget/timeline", "Vertical", "Risk sensitivity"],
        ["Confirms tier", "Names sponsor", "Accepts pre-build boundary"],
        ["Drafts tier fit", "Flags vertical/regulatory needs", "Prepares scope controls"],
        ["Selects lite/standard/deep", "Loads vertical extension", "Sets offline-proof boundary"],
        ["Engagement tier", "Vertical extension", "Scope controls", "Proof boundary"],
        "Tier and vertical extension are explicit. No one-size-fits-all engagement starts.",
        ["00-engagement-tiering.yaml", "00-tier-matrix.yaml", "vertical-extension.schema.yaml"],
        ["Do not run every client at the same depth.", "Do not start any build work here."],
        "If the client scope changes materially, return here before expanding the engagement.",
    ),
    Step(
        1,
        "Executive Opportunity Terrain Mapping",
        "Frame",
        "Understand where the company is, what leadership cares about, and who can explain how work really happens.",
        ["Strategy", "Org chart", "Operating model", "Trust boundaries", "Sponsor narrative"],
        ["Shares priorities", "Names informants", "Explains decision rights"],
        ["Structures terrain", "Finds nomination bias", "Drafts opportunity zones"],
        ["Triangulates informants", "Avoids asking executives for task lists", "Frames zones without ego threat"],
        ["Terrain map", "Named zones", "Initial informant list", "Trust boundaries"],
        "There is enough context to form discovery zones without forcing the sponsor to self-diagnose AI use cases.",
        ["01-executive-opportunity-terrain.md", "01-org-structure-capture.csv"],
        ["Sponsors over-nominate loyalists.", "Ask who people call when something breaks."],
        "If informants are biased or thin, expand nomination before Step 2.",
    ),
    Step(
        2,
        "Opportunity Terrain Synthesis And Candidate Shortlist",
        "Frame",
        "Turn terrain into candidate use cases with hypotheses, dependencies, confidence, and disqualification rules.",
        ["Step 1 terrain", "Org sample", "Strategic priorities", "Known systems", "Risk clues"],
        ["Reviews priorities", "Confirms constraints", "Does not need to know where AI fits"],
        ["Drafts candidates", "Names assumptions", "Creates discovery sequencing"],
        ["Chooses which candidates deserve discovery", "Sets disqualification rules", "Versions the shortlist"],
        ["Candidate AI portfolio", "Discovery plan", "Disqualification events"],
        "Each candidate has target user, workflow boundary, value hypothesis, dependencies, and kill/disqualify criteria.",
        ["02-candidate-use-case-shortlist.yaml", "02-interview-coverage-matrix.csv"],
        ["This is hypothesis selection, not final AI selection.", "Sponsors provide priorities, not all answers."],
        "Step 7 can discovery-disqualify, Step 12 can economic-disqualify, Step 16 can readiness-disqualify.",
    ),
    Step(
        3,
        "Role-Aware AI-Led Interviews",
        "Discover",
        "Capture work episodes, edge cases, source access, truth production, approvals, and adoption realities at scale.",
        ["Candidate list", "Interview matrix", "AI interviewer protocol", "Consent rules"],
        ["Participants answer with examples", "No uploads during interview", "Can refuse AI path"],
        ["Asks adaptive questions", "Does not assert org facts", "Captures edge cases and evidence needs"],
        ["Monitors quality", "Intervenes on protocol breaks", "Protects consent and retention rules"],
        ["Interview notes", "Edge case register", "Evidence need log", "Source access clues"],
        "Enough role coverage exists to model actual work, including exceptions and truth-production clues.",
        ["03-ai-interviewer-protocol.md", "03-role-interview-guide.md", "03-edge-case-register.csv"],
        ["AI interviewer can ask, not claim.", "Participation skew matters in fragmented orgs."],
        "If interviews reveal major workflow variation, trigger Step 4 instead of forcing a fake canonical workflow.",
    ),
    Step(
        4,
        "Variation Mapping",
        "Discover",
        "Map operating variants when the company is multi-region, franchised, independent-contractor, multi-system, or portfolio-driven.",
        ["Interview variance", "Region/portfolio spread", "System differences", "Role differences"],
        ["Confirms whether variation is real", "Supplies representative variants"],
        ["Clusters variants", "Detects sampling bias", "Highlights split-model needs"],
        ["Decides whether one workflow model is valid", "Names variant-specific paths"],
        ["Variation map", "Canonical workflow assertion or split", "Revisit triggers"],
        "Either variation is modeled, or a single-canonical-workflow assertion is justified with evidence.",
        ["04-variation-map.yaml"],
        ["Do not average fragmented work into one clean process.", "Variation can change use-case economics."],
        "If new variants appear later, update Step 6 and re-score Step 7.",
    ),
    Step(
        5,
        "Planning-Evidence Follow-Up",
        "Discover",
        "Request the smallest useful planning evidence after interviews, without asking for credentials or live access.",
        ["Evidence need log", "Source conflicts", "Truth-production gaps", "Screens/report needs"],
        ["Provides redacted/substitute evidence", "Explains unavailable artifacts"],
        ["Clusters requests", "Drafts owner-grouped follow-up", "Tracks SLA and substitutes"],
        ["Approves request scope", "Escalates stalls", "Keeps boundary tight"],
        ["Evidence request", "Evidence status", "Substitute evidence", "Open gaps"],
        "Evidence requests are justified, minimal, SLA-bound, and do not cross into build access.",
        ["04-artifact-follow-up-request.md", "04-artifact-follow-up-request.csv"],
        ["No uploads during interview.", "A walkthrough or screenshot can substitute for a file."],
        "Missing evidence routes to confidence gaps in Step 6 and validation items in Step 8.",
    ),
    Step(
        6,
        "AI-Native Workflow Intelligence Object",
        "Intelligence",
        "Build the machine-readable model of work: roles, decisions, information objects, truth, sources, risks, variation, and confidence.",
        ["Interview data", "Evidence", "Variation map", "Source clues", "Truth signals"],
        ["Does not review the full raw object", "Corrects targeted views later"],
        ["Extracts structured objects", "Links evidence", "Flags completeness gaps"],
        ["Challenges structure", "Keeps object schema-governed", "Defines enrichment routes"],
        ["Workflow intelligence object", "Information objects", "Source profiles", "Truth profiles"],
        "The object conforms to the canonical schema and is complete enough for diagnostic and validation.",
        ["05-ai-workflow-spec.yaml", "canonical-object-schemas.yaml"],
        ["This is not a report.", "Every decision/input should have owner, evidence, and confidence where possible."],
        "Material validation changes from Step 8 loop back here and can trigger Step 7 re-score.",
    ),
    Step(
        7,
        "Organizational Intelligence Diagnostic",
        "Intelligence",
        "Classify what the workflow object means for AI: blockers, root causes, remediation paths, and safe boundaries.",
        ["Workflow object", "Variation", "Truth profiles", "Source access profiles", "Evidence confidence"],
        ["Confirms routed facts only", "Does not review the full raw object"],
        ["Finds patterns", "Separates symptoms/root causes", "Classifies blockers"],
        ["Applies judgment", "Routes fatal/remediation/control findings", "Updates candidate status"],
        ["Diagnostic", "Blocker classifications", "Intervention routes", "Candidate updates"],
        "Findings are object-linked, evidence-backed, confidence-scored, and classified by the current blocker rubric.",
        ["06-organizational-intelligence-diagnostic.yaml", "06-blocker-classification-rubric.md"],
        ["Fatal findings should not drift downstream.", "One blocker can limit one behavior but not another."],
        "Fatal-for-use-case findings can send candidates back to Step 2 as discovery disqualifications.",
    ),
    Step(
        8,
        "Controlled Validation And Baseline Release",
        "Intelligence",
        "Validate unresolved governance/truth/source objects with the smallest authorized resolver group, then release Organizational Intelligence Baseline.",
        ["Workflow object", "Diagnostic", "Validation items", "Resolver groups"],
        ["Confirms ownership, authority, source/truth decisions", "Only sees controlled views"],
        ["Pre-fills validation views", "Tracks disputes", "Generates baseline seeds"],
        ["Routes questions", "Updates object", "Decides baseline release state"],
        ["Organizational Intelligence Baseline", "Downstream seeds", "Validation state"],
        "Organizational Intelligence Baseline is released, partially released, or blocked using the baseline release contract.",
        ["07-validation-event.yaml", "07-organizational-intelligence-baseline.yaml", "07-baseline-release-contract.yaml"],
        ["Do not hand over the raw object.", "Baseline is product substrate and downstream machine input."],
        "Material corrections loop back to Step 6 and Step 7 before continuing.",
    ),
    Step(
        9,
        "AI Knowledge And Guideline Requirements Map",
        "Reasoning",
        "Name what the future AI would need to know before it can reason safely in the workflow.",
        ["Baseline", "Decisions", "Exceptions", "Truth profiles", "Domain obligations"],
        ["Experts confirm what knowledge exists and who owns it"],
        ["Maps requirements", "Finds tacit knowledge", "Flags regulated-domain rules"],
        ["Prioritizes knowledge gaps", "Chooses capture route", "Avoids writing final rules too early"],
        ["Knowledge requirements map", "Tacit capture routes", "Regulated-domain knowledge list"],
        "Every material AI decision has required knowledge, owner, source, validation status, and gap route.",
        ["08-knowledge-map.md"],
        ["A macro, spreadsheet, or expert habit can be knowledge.", "This maps requirements, not final guidance."],
        "Uncaptured tacit knowledge routes to Step 10 guidance gaps or Step 17 knowledge capture plan.",
    ),
    Step(
        10,
        "AI Guidance Pack",
        "Reasoning",
        "Convert prioritized requirements into machine-readable rules, examples, output contracts, and eval cases.",
        ["Knowledge map", "Truth profiles", "Output needs", "Domain rules", "Edge cases"],
        ["Subject experts validate examples, rules, forbidden behavior"],
        ["Drafts rules", "Builds eval cases", "Splits behavioral/output-quality tests"],
        ["Chooses rule priority", "Sets confidence language", "Approves escalation policy"],
        ["Guidance spec", "Readable view", "Eval suite", "Output contract"],
        "Guidance includes minimum eval counts, methodology, regression versioning, and drift/revalidation rules.",
        ["09-ai-guidance-spec.yaml", "09-ai-guidance-test-cases.yaml", "09-ai-guidance-skill.md"],
        ["A skill-style view is not Codex-specific.", "Source conflict and fragile truth rules are required."],
        "Weak eval coverage can block readiness at Step 16.",
    ),
    Step(
        11,
        "Measurement Intelligence And AI Metrics",
        "Value",
        "Classify existing metrics for trust, then define the metrics the future AI capability itself will need.",
        ["Reports", "KPIs", "Metric formulas", "Truth production", "Value hypotheses"],
        ["Metric owners confirm formulas, quality, usage limits"],
        ["Classifies trust", "Designs AI performance metrics", "Flags fragile baselines"],
        ["Decides which metrics can be used", "Sets kill criteria and caveats"],
        ["Metric trust map", "AI metrics", "Kill criteria", "Measurement gaps"],
        "Existing metrics are trust-classified and future AI success, drift, cost, adoption, and error metrics are defined.",
        ["10-measurement-intelligence.yaml", "10-kpi-dictionary.csv"],
        ["Fragile metrics cannot prove ROI unless the use case is measurement remediation.", "AI metrics are pre-build design."],
        "Disputed or fragile metrics constrain Step 12 value case and Step 16 readiness.",
    ),
    Step(
        12,
        "Business Value Case And Portfolio Comparison",
        "Value",
        "Compare surviving opportunities, including AI-side costs, fragile-truth caveats, and portfolio priority.",
        ["Candidate portfolio", "Metric trust", "Costs", "Risk posture", "Adoption constraints"],
        ["Confirms volumes, costs, priorities, budget/capacity"],
        ["Models value ranges", "Calculates AI-side cost", "Ranks portfolio"],
        ["Chooses 1-N opportunities to advance", "Deprioritizes weak cases"],
        ["Value case", "Portfolio rank", "Economic disqualifications", "Advance list"],
        "Only credible, prioritized opportunities advance to solution shape.",
        ["11-business-value-case.yaml", "11-portfolio-comparison.yaml"],
        ["Do not let every candidate reach readiness.", "Include model/tool/eval/observability costs."],
        "Economic disqualification updates Step 2 shortlist state.",
    ),
    Step(
        13,
        "Solution Shape And Adoption Design",
        "Shape",
        "Decide the future solution posture and the human adoption path before detailed technical blueprinting.",
        ["Advance list", "Value case", "Guidance", "Adoption signals", "System realities"],
        ["End users and managers confirm adoption reality"],
        ["Drafts topology, UX, build/buy/leverage options, adoption plan"],
        ["Selects minimum solution shape", "Challenges incentives", "Sets rollout failure triggers"],
        ["Solution shape", "Adoption design", "Offline proof recommendation"],
        "Build/buy/leverage path, topology, UX surface, model class, adoption path, and failure triggers are explicit.",
        ["12-solution-shape.yaml", "13-adoption-design.yaml"],
        ["Architecture follows adoption reality.", "Risk findings in Step 15 can force a shape revision."],
        "Step 15 can loop back here if controls require a different topology, behavior, or UX.",
    ),
    Step(
        14,
        "Technical And Vendor Implementation Blueprint",
        "Shape",
        "Document what a future build would require: systems, access paths, tools, normalization, runtime, hosting, tests, and secrets.",
        ["Solution shape", "Source profiles", "Truth profiles", "Guidance/evals", "Risk constraints"],
        ["IT/data/security/vendor owners confirm feasibility as a plan"],
        ["Drafts architecture", "Maps future tool contracts", "Names access options"],
        ["Avoids vendor defaulting", "Defines preferred/fallback/blocked paths"],
        ["Technical blueprint", "Future access package", "Build sequence", "Blocked paths"],
        "A future build team can see the required architecture without any credentials or implementation work starting.",
        ["12-technical-implementation-blueprint.yaml"],
        ["This defines MCP/tool/connector contracts; it does not build them.", "No production credentials here."],
        "Technical infeasibility can route to Step 17 technical feasibility plan.",
    ),
    Step(
        15,
        "Risk And Control Model",
        "Shape",
        "Define controls for privacy, security, output quality, truth, tools, regulated-domain risk, approvals, logging, and revocation.",
        ["Technical blueprint", "Guidance pack", "Sensitive data", "Regulated-domain extension"],
        ["Risk/legal/security owners confirm named controls"],
        ["Drafts risk register", "Maps permissions", "Names stop conditions"],
        ["Judges materiality", "Sets residual risk stance", "Loops back if shape must change"],
        ["Risk register", "Zero-trust controls", "Stop conditions", "Residual risk"],
        "Material risks have controls, owners, verification needs, residual risk, and stop/revoke conditions.",
        ["13-risk-control-model.yaml", "13-risk-register.csv"],
        ["Compliance is named, not generic.", "Controls can shrink the AI behavior level."],
        "If controls force topology, UX, retrieval, or adoption changes, return to Step 13.",
    ),
    Step(
        16,
        "AI-Agent Readiness Score",
        "Decide",
        "Convert all upstream evidence into behavior-level readiness: safe first behavior, blockers, gates, and Step 17 path.",
        ["Steps 0-15", "Hard-gate rubric", "Evidence confidence", "Candidate scope"],
        ["Confirms unresolved facts and owner commitments"],
        ["Applies gates", "Scores dimensions", "Maps blockers/dependencies"],
        ["Challenges score", "Chooses minimum safe behavior", "Names prohibited behaviors"],
        ["Readiness object", "Readiness decision", "Minimum safe first behavior", "Step 17 path"],
        "Hard gates override averages. Behavior levels are separately ready, conditional, failed, or blocked.",
        ["14-ai-agent-readiness-score.yaml", "14-hard-gates-readiness-rubric.yaml"],
        ["Average score cannot hide a failed hard gate.", "Fragile truth only passes for safe-limited behavior."],
        "Readiness disqualification updates the candidate portfolio and Step 17 recommendation path.",
    ),
    Step(
        17,
        "Implementation Decision Packet",
        "Decide",
        "Produce the canonical machine-readable recommendation: build-ready, remediate, feasibility, risk plan, or do not automate.",
        ["Readiness object", "Blueprint", "Risk model", "Value case", "Guidance/evals"],
        ["Sponsor decides whether to approve separate implementation after Step 18"],
        ["Assembles packet", "Creates audience views", "Links evidence and owners"],
        ["Writes final recommendation", "States confidence", "Names revision triggers"],
        ["Decision packet", "Packet set if needed", "Future access request package"],
        "Packet type matches contract and includes no-build boundary, owners, confidence, and conditional revision triggers.",
        ["15-implementation-decision-packet.yaml", "15-implementation-decision-packet-set.yaml", "15-decision-packet-contracts.yaml"],
        ["One workflow can produce multiple packets.", "A build-ready packet still does not authorize build by itself."],
        "Multiple packet types create a packet_set that Step 18 turns into a lifecycle_set.",
    ),
    Step(
        18,
        "Managed Lifecycle And Adoption-Change Object",
        "Decide",
        "Define how the future capability, remediation, or no-automation decision will be owned, monitored, changed, paused, and handed off.",
        ["Step 17 packet", "Controls", "Adoption design", "Owners", "Handoff terms"],
        ["Approves owners, forum, cadence, handoff, implementation conditions"],
        ["Drafts lifecycle", "Maps monitoring, truth governance, incidents, adoption"],
        ["Tests realism", "Defines return-to-method triggers", "Closes pre-build engagement"],
        ["Lifecycle object", "Lifecycle set if needed", "method-to-build handoff"],
        "Lifecycle variant and handoff are approved before any implementation phase begins.",
        ["16-managed-lifecycle-object.yaml", "16-lifecycle-set.yaml", "18-method-to-build-handoff-contract.md"],
        ["Lifecycle is also adoption/change management.", "No agent is operated during the engagement."],
        "Material vendor, truth, regulatory, or kill-trigger changes return to the method.",
    ),
]

MECHANICS: dict[int, list[tuple[str, str]]] = {
    0: [
        ("Size", "Select lite, standard, or deep based on scope, risk, timeline, and client size."),
        ("Extend", "Load the vertical extension and identify required domain/regulatory scaffolding."),
        ("Boundary", "Define no-build, no-live-access, and offline-proof limits."),
        ("Commit", "Confirm sponsor, owner forum, timeline, and minimum artifacts."),
    ],
    1: [
        ("Listen", "Capture strategy, leverage areas, operating context, and trust boundaries."),
        ("Triangulate", "Combine sponsor nominations, org-chart sample, and break-fix informants."),
        ("Terrain", "Name opportunity zones without asking executives for task-level diagnosis."),
        ("Informants", "Identify who can explain real work across layers and functions."),
    ],
    2: [
        ("Cluster", "Turn terrain into candidate zones and rough workflow boundaries."),
        ("Hypothesize", "Create 5-10 AI candidates with target user, value logic, and dependencies."),
        ("Disqualify", "Attach discovery, economic, and readiness disqualification criteria."),
        ("Sequence", "Choose interview order based on uncertainty, value, and risk."),
    ],
    3: [
        ("Consent", "Apply hosting, recording, retention, redaction, and refusal-fallback protocol."),
        ("Elicit", "Ask about real episodes, exceptions, decisions, handoffs, and hidden work."),
        ("Detect", "Capture source access, truth production, adoption, and evidence-needed signals."),
        ("Quality", "Operating partner monitors transcripts and intervenes only when protocol requires."),
    ],
    4: [
        ("Trigger", "Run only when fragmentation, region, portfolio, system, or contractor variation appears."),
        ("Enumerate", "List variants instead of forcing one canonical process."),
        ("Compare", "Map what changes: users, systems, truth, controls, incentives, timing."),
        ("Decide", "Model one workflow, split variants, or record a skip rationale."),
    ],
    5: [
        ("Consolidate", "Cluster interview evidence needs and remove duplicates."),
        ("Minimize", "Ask for the smallest redacted artifact, screenshot, walkthrough, or substitute."),
        ("Govern", "Assign owners, SLA, escalation, sensitivity, and handling rules."),
        ("Route", "Unreceived evidence becomes a known confidence gap, not a stalled mystery."),
    ],
    6: [
        ("Extract", "Convert interviews and evidence into actors, steps, decisions, objects, and edge cases."),
        ("Link", "Attach evidence refs, confidence, owners, source profiles, and truth profiles."),
        ("Check", "Run schema and completeness checks for required nested objects."),
        ("Prepare", "Create a structured substrate for diagnostic and controlled validation."),
    ],
    7: [
        ("Diagnose", "Attach findings to workflow objects and distinguish symptom from root cause."),
        ("Classify", "Mark blockers as fatal, remediation-before-build, acceptable-with-controls, or informational."),
        ("Route", "Choose intervention path by object, owner, risk, and candidate impact."),
        ("Update", "Change candidate state when findings disqualify or narrow behavior."),
    ],
    8: [
        ("Slice", "Create controlled views for the smallest authorized resolver group."),
        ("Resolve", "Confirm source, truth chain, owner, authority, access, sensitivity, and permitted AI use."),
        ("Loop", "Feed material changes back to Step 6 and Step 7 before release."),
        ("Release", "Issue Organizational Intelligence Baseline with downstream seeds and audience-specific views."),
    ],
    9: [
        ("Trace", "Start from decisions, exceptions, truth chains, and regulated-domain obligations."),
        ("Name", "List explicit, tacit, artifact-encoded, and expert-memory knowledge requirements."),
        ("Own", "Assign source, owner, validation status, and capture route."),
        ("Prioritize", "Separate must-have AI reasoning knowledge from nice-to-have context."),
    ],
    10: [
        ("Codify", "Turn requirements into rules, source hierarchy, confidence language, and output contracts."),
        ("Example", "Write good, bad, edge, source-conflict, fragile-truth, and escalation cases."),
        ("Evaluate", "Split behavioral evals from output-quality and regulated-domain evals."),
        ("Version", "Set owners, minimum counts, regression suite, drift rules, and update cadence."),
    ],
    11: [
        ("Audit", "Classify existing metrics by truth status, reproducibility, owner, and auditability."),
        ("Protect", "Do not use fragile metrics as reliable baseline proof unless fixing measurement is the case."),
        ("Design", "Define AI success, override, error, drift, adoption, cost, and kill metrics."),
        ("Gate", "Route missing/disputed measures to value caveats or readiness blockers."),
    ],
    12: [
        ("Model", "Estimate value ranges, confidence, assumptions, and sensitivity."),
        ("Cost", "Include model, tool-call, OCR, eval, observability, tuning, and maintenance costs."),
        ("Compare", "Rank surviving opportunities against one another."),
        ("Select", "Advance, remediate, deprioritize, or stop each candidate."),
    ],
    13: [
        ("Shape", "Decide assistant, workflow-with-LLM-steps, tool agent, monitoring agent, or no-agent path."),
        ("Place", "Choose UX surface: existing system, queue, email, dashboard, chat, or separate app."),
        ("Adopt", "Map users, incentives, opt-in/mandate reality, training, and rollout."),
        ("Fail", "Name adoption-failure triggers and offline proof recommendations."),
    ],
    14: [
        ("Inventory", "List systems, sources, owners, sensitive fields, access options, and blocked paths."),
        ("Normalize", "Define canonical entities, mappings, identity resolution, freshness, and quality checks."),
        ("Contract", "Specify future tools/MCPs/connectors: input, output, allowed actions, logs, permissions."),
        ("Sequence", "Plan offline, sandbox, pilot, and controlled expansion prerequisites."),
    ],
    15: [
        ("Classify", "Map data sensitivity, regulated-domain risks, truth risks, and output risks."),
        ("Control", "Define permissions, approval gates, logging, monitoring, incidents, revocation, and stop rules."),
        ("Own", "Tie each material risk to a named owner and verification need."),
        ("Revise", "Loop back to Step 13 when controls require a different solution shape."),
    ],
    16: [
        ("Gate", "Apply hard gates before scoring averages."),
        ("Score", "Rate dimensions for the proposed behavior level and evidence confidence."),
        ("Choose", "Name minimum safe first behavior and prohibited behaviors."),
        ("Route", "Send to build brief, remediation, governance, knowledge, feasibility, risk, or no-automate path."),
    ],
    17: [
        ("Assemble", "Pull Step 16 decision, value, blueprint, controls, guidance, owners, and evidence."),
        ("Type", "Choose packet type or create packet_set for mixed outcomes."),
        ("View", "Generate sponsor, technical, risk, remediation, and future-build views from one source."),
        ("Decide", "State recommendation confidence, revision triggers, owner matrix, and no-build boundary."),
    ],
    18: [
        ("Variant", "Select managed lifecycle, remediation lifecycle, or no-automation review cadence."),
        ("Govern", "Define owners, launch gates, monitoring, truth governance, incidents, access review, and adoption."),
        ("Handoff", "Name future build owner, operating partner role, and implementation approval conditions."),
        ("Return", "Define return-to-method triggers for truth, vendor, regulatory, kill, or scope changes."),
    ],
}


def phase_color(phase: str):
    for name, _rng, color in PHASES:
        if name == phase:
            return color
    return COLORS["navy"]


def set_font(c: canvas.Canvas, name: str, size: float, color=COLORS["ink"]) -> None:
    c.setFont(name, size)
    c.setFillColor(color)


def width(text: str, font: str, size: float) -> float:
    return pdfmetrics.stringWidth(text, font, size)


def wrap(text: str, font: str, size: float, max_w: float, max_lines: int | None = None) -> list[str]:
    words = text.split()
    lines: list[str] = []
    line = ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if width(candidate, font, size) <= max_w:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        while lines and width(lines[-1] + "...", font, size) > max_w:
            lines[-1] = " ".join(lines[-1].split()[:-1])
        lines[-1] = lines[-1].rstrip(".") + "..."
    return lines


def draw_wrapped(
    c: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    w: float,
    font: str = "Helvetica",
    size: float = 8.5,
    leading: float = 10.5,
    color=COLORS["ink"],
    max_lines: int | None = None,
) -> float:
    set_font(c, font, size, color)
    for line in wrap(text, font, size, w, max_lines):
        c.drawString(x, y, line)
        y -= leading
    return y


def rounded(c: canvas.Canvas, x: float, y: float, w: float, h: float, fill, stroke=COLORS["line"], r: float = 7) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, r, fill=1, stroke=1)


def pill(c: canvas.Canvas, x: float, y: float, text: str, fill, stroke=None, color=COLORS["ink"], font="Helvetica-Bold", size=7.5) -> float:
    pad = 7
    h = 17
    w = width(text, font, size) + pad * 2
    rounded(c, x, y, w, h, fill, stroke or fill, r=8)
    set_font(c, font, size, color)
    c.drawCentredString(x + w / 2, y + 5, text)
    return w


def arrow(c: canvas.Canvas, x1: float, y1: float, x2: float, y2: float, color=COLORS["line"], lw: float = 1.4) -> None:
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(lw)
    c.line(x1, y1, x2, y2)
    if x2 >= x1:
        pts = [(x2, y2), (x2 - 7, y2 + 3.5), (x2 - 7, y2 - 3.5)]
    else:
        pts = [(x2, y2), (x2 + 7, y2 + 3.5), (x2 + 7, y2 - 3.5)]
    p = c.beginPath()
    p.moveTo(*pts[0])
    p.lineTo(*pts[1])
    p.lineTo(*pts[2])
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def header(c: canvas.Canvas, title: str, page_no: int) -> None:
    set_font(c, "Helvetica-Bold", 8.5, COLORS["muted"])
    c.drawString(M, PAGE_H - 20, "AI Operating Partner System")
    set_font(c, "Helvetica", 8, COLORS["muted"])
    c.drawCentredString(PAGE_W / 2, PAGE_H - 20, title)
    c.drawRightString(PAGE_W - M, PAGE_H - 20, f"{page_no}")
    c.setStrokeColor(COLORS["line"])
    c.setLineWidth(0.6)
    c.line(M, PAGE_H - 28, PAGE_W - M, PAGE_H - 28)


def footer(c: canvas.Canvas) -> None:
    set_font(c, "Helvetica", 6.8, COLORS["muted"])
    c.drawString(M, 14, "Pre-build only: no agent build, no MCP/connector build, no credentials, no live integrations during the engagement.")


def title_block(c: canvas.Canvas, title: str, subtitle: str | None = None) -> None:
    set_font(c, "Helvetica-Bold", 21, COLORS["navy"])
    c.drawString(M, PAGE_H - 58, title)
    if subtitle:
        draw_wrapped(c, subtitle, M, PAGE_H - 77, PAGE_W - 2 * M, "Helvetica", 9.5, 12, COLORS["muted"], 2)


def phase_ribbon(c: canvas.Canvas, y: float) -> None:
    x = M
    gap = 6
    w = (PAGE_W - 2 * M - gap * (len(PHASES) - 1)) / len(PHASES)
    for name, rng, color in PHASES:
        rounded(c, x, y, w, 42, color, color, r=9)
        set_font(c, "Helvetica-Bold", 11, colors.white)
        c.drawCentredString(x + w / 2, y + 24, name)
        set_font(c, "Helvetica", 7.8, colors.white)
        c.drawCentredString(x + w / 2, y + 11, f"Steps {rng}")
        x += w + gap


def card_title(c: canvas.Canvas, x: float, y: float, text: str, color=COLORS["navy"]) -> None:
    set_font(c, "Helvetica-Bold", 9.2, color)
    c.drawString(x, y, text)


def bullet_list(c: canvas.Canvas, items: list[str], x: float, y: float, w: float, max_items: int = 5, size: float = 7.6) -> float:
    for item in items[:max_items]:
        c.setFillColor(COLORS["teal"])
        c.circle(x + 2.5, y + 2.5, 2.2, fill=1, stroke=0)
        y = draw_wrapped(c, item, x + 9, y, w - 9, "Helvetica", size, size + 2.1, COLORS["ink"], 2)
        y -= 1.5
    return y


def draw_phase_overview(c: canvas.Canvas, page: int) -> None:
    header(c, "Seven Umbrellas", page)
    title_block(
        c,
        "The Whole System In Seven Umbrellas",
        "The client sees the umbrellas. The operator runs the 19 step mechanics underneath.",
    )
    phase_ribbon(c, PAGE_H - 145)

    y = PAGE_H - 215
    x = M
    gap = 10
    w = (PAGE_W - 2 * M - 2 * gap) / 3
    h = 86
    descriptions = [
        ("Frame And Hypothesize", "Set engagement depth, map opportunity terrain, and form candidate AI hypotheses without asking the client to know where AI fits."),
        ("Discover Reality", "Use AI-led interviews, variation mapping, and targeted evidence to understand how work actually happens."),
        ("Build Intelligence Layer", "Turn work into schema-governed organizational intelligence, diagnose blockers, validate, and release Organizational Intelligence Baseline."),
        ("Define AI Reasoning", "Name the knowledge needed, then convert it into guidance, rules, examples, output contracts, and evals."),
        ("Prove Value", "Classify metric trust, design AI metrics, model economics, and compare the portfolio."),
        ("Shape Future Solution", "Decide solution/adoption shape, technical blueprint, and controls before any build starts."),
        ("Decide And Govern", "Score readiness, issue decision packets, and define lifecycle/handoff before implementation."),
    ]
    for idx, (name, desc) in enumerate(descriptions):
        col = idx % 3
        row = idx // 3
        cx = x + col * (w + gap)
        cy = y - row * (h + 13)
        color = PHASES[min(idx, len(PHASES) - 1)][2]
        rounded(c, cx, cy, w, h, COLORS["soft"], COLORS["line"], r=9)
        pill(c, cx + 10, cy + h - 25, PHASES[idx][1], color, color, colors.white)
        card_title(c, cx + 50, cy + h - 20, name, color)
        draw_wrapped(c, desc, cx + 12, cy + h - 42, w - 24, "Helvetica", 8, 10.2, COLORS["ink"], 4)

    rounded(c, M, 52, PAGE_W - 2 * M, 55, COLORS["mint"], COLORS["teal"], r=9)
    card_title(c, M + 13, 88, "The operating logic", COLORS["teal"])
    draw_wrapped(
        c,
        "Every step produces structured evidence or a machine-readable object. Downstream steps do not rely on memory or narrative; they consume the objects created earlier.",
        M + 13,
        72,
        PAGE_W - 2 * M - 26,
        "Helvetica-Bold",
        9,
        12,
        COLORS["navy"],
        2,
    )
    footer(c)


def draw_cover(c: canvas.Canvas, page: int) -> None:
    c.setFillColor(colors.white)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    header(c, "Visual Process Guide", page)
    set_font(c, "Helvetica-Bold", 28, COLORS["navy"])
    c.drawCentredString(PAGE_W / 2, PAGE_H - 95, "AI Operating Partner")
    set_font(c, "Helvetica-Bold", 18, COLORS["teal"])
    c.drawCentredString(PAGE_W / 2, PAGE_H - 123, "Visual Process Guide")
    draw_wrapped(
        c,
        "A visual, operator-facing guide to every step from engagement tiering through lifecycle handoff. Built for understanding the process, not for client presentation.",
        PAGE_W / 2 - 250,
        PAGE_H - 154,
        500,
        "Helvetica",
        10,
        13,
        COLORS["muted"],
        3,
    )
    phase_ribbon(c, PAGE_H - 230)

    # Central flow
    y = PAGE_H - 330
    labels = ["Terrain", "Reality", "Intelligence", "Guidance", "Value", "Blueprint", "Readiness", "Handoff"]
    x0 = M + 20
    box_w = (PAGE_W - 2 * M - 40 - 7 * 12) / 8
    for i, label in enumerate(labels):
        x = x0 + i * (box_w + 12)
        rounded(c, x, y, box_w, 58, COLORS["soft"], COLORS["line"], r=9)
        set_font(c, "Helvetica-Bold", 9.5, COLORS["navy"])
        c.drawCentredString(x + box_w / 2, y + 34, label)
        set_font(c, "Helvetica", 7.5, COLORS["muted"])
        c.drawCentredString(x + box_w / 2, y + 19, f"{i + 1}")
        if i < len(labels) - 1:
            arrow(c, x + box_w + 2, y + 29, x + box_w + 10, y + 29, COLORS["teal"], 1.5)

    rounded(c, M + 25, 88, PAGE_W - 2 * M - 50, 92, COLORS["sky"], COLORS["blue"], r=12)
    set_font(c, "Helvetica-Bold", 13, COLORS["navy"])
    c.drawString(M + 45, 151, "What makes the method different")
    bullets = [
        "It discovers truth production instead of assuming source-of-truth cleanliness.",
        "It creates Organizational Intelligence Baseline by Step 8, before any build.",
        "It separates use-case selection, guidance, metrics, adoption, technical blueprint, risk, readiness, packet, and lifecycle.",
        "It remains pre-build: no credentials, no live integrations, no MCP/connector build, no normalization build.",
    ]
    bullet_list(c, bullets, M + 47, 132, PAGE_W - 2 * M - 95, max_items=4, size=8)
    footer(c)


def draw_truth_layer(c: canvas.Canvas, page: int) -> None:
    header(c, "Truth Production Layer", page)
    title_block(c, "Truth Production Is The Spine", "The framework does not ask: where is the source of truth? It asks: how is truth actually produced?")
    x = M + 20
    y = PAGE_H - 180
    stages = [
        ("Official source", "What policy or system says is authoritative.", COLORS["blue"]),
        ("De facto source", "What people actually trust in practice.", COLORS["teal"]),
        ("Production chain", "Exports, formulas, macros, manual adjustments, judgment, reconciliation.", COLORS["amber"]),
        ("Truth status", "Authoritative, conditional, shadow, adjusted, person-dependent, disputed, missing.", COLORS["red"]),
        ("AI-safe use", "Summarize, compare, flag, draft questions, escalate, or block behavior.", COLORS["green"]),
    ]
    w = (PAGE_W - 2 * M - 40 - 4 * 14) / 5
    for i, (label, desc, color) in enumerate(stages):
        cx = x + i * (w + 14)
        rounded(c, cx, y, w, 116, COLORS["soft"], color, r=10)
        pill(c, cx + 10, y + 84, str(i + 1), color, color, colors.white)
        card_title(c, cx + 40, y + 91, label, color)
        draw_wrapped(c, desc, cx + 12, y + 65, w - 24, "Helvetica", 8, 10.2, COLORS["ink"], 5)
        if i < len(stages) - 1:
            arrow(c, cx + w + 2, y + 58, cx + w + 12, y + 58, color, 1.4)

    rounded(c, M + 25, 120, PAGE_W - 2 * M - 50, 105, COLORS["rose"], COLORS["red"], r=10)
    card_title(c, M + 45, 194, "Readiness implication", COLORS["red"])
    draw_wrapped(
        c,
        "Fragile truth becomes a readiness blocker unless the AI behavior is safe-limited. Safe-limited means the AI can summarize, compare sources, flag uncertainty, draft clarification questions, or escalate. It cannot present fragile truth as authoritative or make/execute material decisions from it.",
        M + 45,
        174,
        PAGE_W - 2 * M - 90,
        "Helvetica-Bold",
        9.4,
        12.2,
        COLORS["navy"],
        5,
    )
    footer(c)


def draw_artifact_stack(c: canvas.Canvas, page: int) -> None:
    header(c, "Artifact Stack", page)
    title_block(c, "How The Objects Build On Each Other", "The method is not a sequence of meeting notes. Each layer feeds the next layer.")
    x = M + 25
    y = PAGE_H - 130
    layers = [
        ("0-2", "Candidate AI Portfolio", "Hypotheses, dependencies, disqualification rules"),
        ("3-5", "Reality Capture", "Interviews, variation, evidence needs, source clues"),
        ("6", "Workflow Intelligence Object", "Machine-readable model of work and truth"),
        ("7", "Diagnostic", "Blockers, root causes, intervention routes"),
        ("8", "Organizational Intelligence Baseline", "Validated organizational intelligence product substrate"),
        ("9-10", "Reasoning Requirements", "Knowledge map, guidance, output contracts, evals"),
        ("11-12", "Measurement And Value", "Metric trust, AI metrics, value, portfolio rank"),
        ("13-15", "Future Solution Plan", "Adoption, blueprint, risk/control model"),
        ("16-18", "Decision And Governance", "Readiness, packet or packet_set, lifecycle or lifecycle_set"),
    ]
    h = 38
    for i, (step, name, desc) in enumerate(layers):
        cy = y - i * (h + 7)
        color = PHASES[min(i // 2, len(PHASES) - 1)][2]
        rounded(c, x + i * 13, cy, PAGE_W - 2 * M - 50 - i * 26, h, COLORS["soft"], color, r=8)
        pill(c, x + i * 13 + 8, cy + 10, step, color, color, colors.white, size=7)
        card_title(c, x + i * 13 + 70, cy + 22, name, color)
        draw_wrapped(c, desc, x + i * 13 + 70, cy + 10, PAGE_W - 2 * M - 135 - i * 26, "Helvetica", 7.6, 9, COLORS["muted"], 1)
        if i < len(layers) - 1:
            arrow(c, x + i * 13 + 22, cy - 2, x + (i + 1) * 13 + 22, cy - 7, COLORS["line"], 1)
    footer(c)


def draw_step_page(c: canvas.Canvas, step: Step, page: int) -> None:
    color = phase_color(step.phase)
    header(c, f"Step {step.n}: {step.title}", page)

    # Title and phase pill
    pill(c, M, PAGE_H - 68, f"STEP {step.n}", color, color, colors.white, size=8.8)
    set_font(c, "Helvetica-Bold", 18, COLORS["navy"])
    c.drawString(M + 72, PAGE_H - 63, step.title)
    pill(c, PAGE_W - M - 84, PAGE_H - 68, step.phase, COLORS["soft"], color, color, size=8.2)
    draw_wrapped(c, step.purpose, M, PAGE_H - 88, PAGE_W - 2 * M, "Helvetica", 8.8, 11.2, COLORS["muted"], 2)

    # Top process pipeline
    lane_y = PAGE_H - 168
    labels = [
        ("Inputs", step.inputs, COLORS["sky"], COLORS["blue"]),
        ("AI work", step.ai, COLORS["lav"], COLORS["purple"]),
        ("Your judgment", step.partner, COLORS["mint"], COLORS["teal"]),
        ("Client confirms", step.client, COLORS["sand"], COLORS["amber"]),
        ("Output/Gate", step.outputs, COLORS["soft"], color),
    ]
    gap = 8
    bw = (PAGE_W - 2 * M - gap * 4) / 5
    for i, (label, items, fill, stroke) in enumerate(labels):
        x = M + i * (bw + gap)
        rounded(c, x, lane_y, bw, 86, fill, stroke, r=9)
        card_title(c, x + 9, lane_y + 66, label, stroke)
        bullet_list(c, items, x + 10, lane_y + 51, bw - 20, max_items=3, size=6.9)
        if i < 4:
            arrow(c, x + bw + 1, lane_y + 43, x + bw + gap - 1, lane_y + 43, COLORS["line"], 1.2)

    # Gate strip
    rounded(c, M, PAGE_H - 223, PAGE_W - 2 * M, 40, COLORS["soft"], color, r=8)
    card_title(c, M + 12, PAGE_H - 198, "Gate", color)
    draw_wrapped(c, step.gate, M + 62, PAGE_H - 198, PAGE_W - 2 * M - 74, "Helvetica-Bold", 8.2, 10.2, COLORS["ink"], 2)

    # Mechanics diagram
    mid_y = 220
    mid_h = 126
    rounded(c, M, mid_y, PAGE_W - 2 * M, mid_h, colors.white, COLORS["line"], r=9)
    card_title(c, M + 12, mid_y + mid_h - 20, "Inside the step", color)
    mech = MECHANICS.get(step.n, [])
    inner_x = M + 13
    inner_y = mid_y + 15
    inner_h = 80
    gap2 = 9
    inner_w = (PAGE_W - 2 * M - 26 - gap2 * 3) / 4
    for i, (label, desc) in enumerate(mech[:4]):
        cx = inner_x + i * (inner_w + gap2)
        rounded(c, cx, inner_y, inner_w, inner_h, COLORS["soft"], color, r=8)
        pill(c, cx + 8, inner_y + inner_h - 24, label, color, color, colors.white, size=7.1)
        draw_wrapped(c, desc, cx + 10, inner_y + inner_h - 39, inner_w - 20, "Helvetica", 7.15, 9.1, COLORS["ink"], 4)
        if i < min(len(mech), 4) - 1:
            arrow(c, cx + inner_w + 1, inner_y + inner_h / 2, cx + inner_w + gap2 - 1, inner_y + inner_h / 2, COLORS["line"], 1)

    # Bottom cards
    y = 68
    h = 120
    w1 = (PAGE_W - 2 * M - 18) * 0.42
    w2 = (PAGE_W - 2 * M - 18) * 0.31
    w3 = (PAGE_W - 2 * M - 18) - w1 - w2
    rounded(c, M, y, w1, h, COLORS["soft"], COLORS["line"], r=9)
    rounded(c, M + w1 + 9, y, w2, h, COLORS["soft"], COLORS["line"], r=9)
    rounded(c, M + w1 + w2 + 18, y, w3, h, COLORS["soft"], COLORS["line"], r=9)
    card_title(c, M + 12, y + h - 21, "Canonical artifacts", COLORS["navy"])
    bullet_list(c, step.templates, M + 14, y + h - 38, w1 - 25, max_items=5, size=7.1)
    card_title(c, M + w1 + 21, y + h - 21, "Watchouts", COLORS["red"])
    bullet_list(c, step.watchouts, M + w1 + 23, y + h - 38, w2 - 25, max_items=4, size=7.1)
    card_title(c, M + w1 + w2 + 30, y + h - 21, "Loop or implication", COLORS["teal"])
    draw_wrapped(c, step.loop, M + w1 + w2 + 30, y + h - 41, w3 - 24, "Helvetica-Bold", 7.8, 10, COLORS["ink"], 7)

    footer(c)


def draw_halt_taxonomy(c: canvas.Canvas, page: int) -> None:
    header(c, "Halt Taxonomy", page)
    title_block(c, "Pause, Revise, Disqualify, Kill, Revoke, Retire", "The current method separates planning stops from operating stops so the team knows what each decision means.")
    items = [
        ("Pause", "Temporary hold. Missing owner/evidence/decision. Resume when the named condition is met.", COLORS["amber"]),
        ("Revise", "Change scope, behavior level, solution shape, evidence, controls, or packet before advancing.", COLORS["blue"]),
        ("Disqualify", "Candidate does not continue for discovery, economics, or readiness reasons.", COLORS["red"]),
        ("Kill", "Future pilot or operation must stop because a threshold or control failed.", COLORS["red"]),
        ("Revoke", "Access, tool, permission, or approval is removed.", COLORS["purple"]),
        ("Retire", "Capability or remediation path is intentionally sunset.", COLORS["teal"]),
    ]
    x = M + 25
    y = PAGE_H - 155
    w = (PAGE_W - 2 * M - 50 - 2 * 14) / 3
    h = 95
    for i, (name, desc, color) in enumerate(items):
        col = i % 3
        row = i // 3
        cx = x + col * (w + 14)
        cy = y - row * (h + 18)
        rounded(c, cx, cy, w, h, COLORS["soft"], color, r=10)
        pill(c, cx + 10, cy + h - 28, name, color, color, colors.white, size=8.2)
        draw_wrapped(c, desc, cx + 12, cy + h - 47, w - 24, "Helvetica", 8.1, 10.5, COLORS["ink"], 4)
    rounded(c, M + 25, 70, PAGE_W - 2 * M - 50, 58, COLORS["mint"], COLORS["teal"], r=9)
    card_title(c, M + 42, 107, "Operator rule", COLORS["teal"])
    draw_wrapped(c, "Every halt has a type, owner, reason, re-entry condition, and evidence trail. Otherwise the process slowly becomes a pile of vague maybes.", M + 42, 90, PAGE_W - 2 * M - 84, "Helvetica-Bold", 9, 12, COLORS["navy"], 2)
    footer(c)


def draw_build_boundary(c: canvas.Canvas, page: int) -> None:
    header(c, "Pre-Build Boundary", page)
    title_block(c, "What  Plans Versus What  Does Not Build", "The engagement creates an implementable plan inch by inch. It does not secretly become implementation.")
    left_x = M + 28
    right_x = PAGE_W / 2 + 12
    y = PAGE_H - 160
    w = PAGE_W / 2 - M - 40
    h = 260
    rounded(c, left_x, y - h, w, h, COLORS["mint"], COLORS["teal"], r=12)
    rounded(c, right_x, y - h, w, h, COLORS["rose"], COLORS["red"], r=12)
    card_title(c, left_x + 16, y - 26, "The method defines", COLORS["teal"])
    bullet_list(
        c,
        [
            "Future tool, MCP, and connector contracts",
            "Future access request packages",
            "Normalization requirements and entity rules",
            "Credential/secrets handling plan",
            "Sandbox/test strategy and offline proof options",
            "Build sequence and implementation prerequisites",
            "Lifecycle, monitoring, adoption, and handoff rules",
        ],
        left_x + 18,
        y - 48,
        w - 36,
        max_items=7,
        size=8,
    )
    card_title(c, right_x + 16, y - 26, "The method does not execute", COLORS["red"])
    bullet_list(
        c,
        [
            "No agent build or deployment",
            "No MCP, connector, or tool build",
            "No live API tokens or credentials",
            "No broad production access",
            "No all-email ingestion",
            "No normalization pipeline build",
            "No write-back automation",
        ],
        right_x + 18,
        y - 48,
        w - 36,
        max_items=7,
        size=8,
    )
    arrow(c, PAGE_W / 2 - 35, 85, PAGE_W / 2 + 35, 85, COLORS["navy"], 1.6)
    set_font(c, "Helvetica-Bold", 9.4, COLORS["navy"])
    c.drawCentredString(PAGE_W / 2, 105, "After Step 18 approval")
    c.drawCentredString(PAGE_W / 2, 70, "Separate implementation phase")
    footer(c)


def draw_final_navigation(c: canvas.Canvas, page: int) -> None:
    header(c, "How To Use The Guide", page)
    title_block(c, "Operator Navigation", "Use this as a process map while running the engagement. The artifact names tell you what to fill.")
    cols = [
        ("When starting", ["Read pages 1-5", "Confirm Step 0 tier", "Use Step 1-2 to frame candidates", "Do not ask client to know AI use cases"]),
        ("During discovery", ["Use Step 3 protocol", "Trigger Step 4 for variation", "Ask for Step 5 evidence only after interviews", "Capture truth production signals"]),
        ("By Step 8", ["Release Organizational Intelligence Baseline", "Keep raw object controlled", "Use downstream seed payloads", "Create client product view separately"]),
        ("Before build", ["Finish Steps 9-18", "Pass hard gates", "Issue packet/lifecycle", "Handoff before implementation"]),
    ]
    x = M + 20
    y = PAGE_H - 170
    w = (PAGE_W - 2 * M - 40 - 3 * 12) / 4
    for i, (title, items) in enumerate(cols):
        cx = x + i * (w + 12)
        rounded(c, cx, y - 210, w, 210, COLORS["soft"], PHASES[min(i * 2, 6)][2], r=11)
        card_title(c, cx + 12, y - 26, title, PHASES[min(i * 2, 6)][2])
        bullet_list(c, items, cx + 14, y - 52, w - 28, max_items=4, size=8.1)

    rounded(c, M + 40, 58, PAGE_W - 2 * M - 80, 64, COLORS["sky"], COLORS["blue"], r=10)
    card_title(c, M + 58, 99, "The one-line mental model", COLORS["blue"])
    draw_wrapped(c, " turns uncertain organizational reality into validated, machine-readable organizational intelligence, then decides exactly what AI behavior is safe, valuable, adoptable, buildable, and governable.", M + 58, 81, PAGE_W - 2 * M - 116, "Helvetica-Bold", 9.2, 12, COLORS["navy"], 3)
    footer(c)


def build_pdf() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(PDF_PATH), pagesize=landscape(letter))
    pages = 0

    def show(draw_fn, *args):
        nonlocal pages
        pages += 1
        draw_fn(c, *args, pages)
        c.showPage()

    show(draw_cover)
    show(draw_phase_overview)
    show(draw_truth_layer)
    show(draw_artifact_stack)
    show(draw_build_boundary)
    for step in STEPS:
        show(draw_step_page, step)
    show(draw_halt_taxonomy)
    show(draw_final_navigation)
    c.save()


def render_previews() -> None:
    import fitz  # type: ignore

    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(PDF_PATH))
    paths: list[Path] = []
    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=fitz.Matrix(1.18, 1.18), alpha=False)
        path = PREVIEW_DIR / f"page-{i:02d}.png"
        pix.save(str(path))
        paths.append(path)

    thumbs: list[Image.Image] = []
    for path in paths:
        img = Image.open(path).convert("RGB")
        img.thumbnail((260, 200))
        thumbs.append(img.copy())
    if not thumbs:
        return
    cols = 4
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 300, rows * 240), "white")
    draw = ImageDraw.Draw(sheet)
    for idx, img in enumerate(thumbs):
        col = idx % cols
        row = idx // cols
        x = col * 300 + 20
        y = row * 240 + 28
        sheet.paste(img, (x, y))
        draw.text((x, y - 18), f"Page {idx + 1}", fill=(60, 70, 80))
    sheet.save(PREVIEW_DIR / "contact-sheet.png")


def main() -> None:
    build_pdf()
    render_previews()
    print(PDF_PATH)
    print(PREVIEW_DIR)


if __name__ == "__main__":
    main()
