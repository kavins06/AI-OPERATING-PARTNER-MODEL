from __future__ import annotations

from pathlib import Path
from textwrap import dedent

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output" / "pdf"
PDF_PATH = OUT_DIR / "ai-operating-partner-process-guide.pdf"
MD_PATH = OUT_DIR / "ai-operating-partner-process-guide.md"

PAGE_WIDTH, PAGE_HEIGHT = letter
LEFT_MARGIN = RIGHT_MARGIN = 0.62 * inch
TOP_MARGIN = 0.65 * inch
BOTTOM_MARGIN = 0.62 * inch
CONTENT_WIDTH = PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN

COLORS = {
    "ink": colors.HexColor("#17202A"),
    "muted": colors.HexColor("#566573"),
    "navy": colors.HexColor("#243B53"),
    "blue": colors.HexColor("#2F80ED"),
    "teal": colors.HexColor("#0F766E"),
    "green": colors.HexColor("#2F855A"),
    "amber": colors.HexColor("#B7791F"),
    "red": colors.HexColor("#C53030"),
    "line": colors.HexColor("#CBD5E0"),
    "soft": colors.HexColor("#F6F8FB"),
    "soft_teal": colors.HexColor("#E6FFFA"),
    "soft_amber": colors.HexColor("#FFF8E1"),
}


def make_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    styles: dict[str, ParagraphStyle] = {}

    styles["title"] = ParagraphStyle(
        "Title",
        parent=base["Title"],
        fontName="Helvetica-Bold",
        fontSize=27,
        leading=32,
        textColor=COLORS["navy"],
        alignment=TA_CENTER,
        spaceAfter=12,
    )
    styles["subtitle"] = ParagraphStyle(
        "Subtitle",
        parent=base["BodyText"],
        fontName="Helvetica",
        fontSize=12.5,
        leading=17,
        textColor=COLORS["muted"],
        alignment=TA_CENTER,
        spaceAfter=18,
    )
    styles["h1"] = ParagraphStyle(
        "Heading1",
        parent=base["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        textColor=COLORS["navy"],
        spaceBefore=14,
        spaceAfter=7,
    )
    styles["h2"] = ParagraphStyle(
        "Heading2",
        parent=base["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13.5,
        leading=17,
        textColor=COLORS["teal"],
        spaceBefore=10,
        spaceAfter=5,
    )
    styles["h3"] = ParagraphStyle(
        "Heading3",
        parent=base["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=11.5,
        leading=14,
        textColor=COLORS["navy"],
        spaceBefore=7,
        spaceAfter=4,
    )
    styles["body"] = ParagraphStyle(
        "Body",
        parent=base["BodyText"],
        fontName="Helvetica",
        fontSize=9.6,
        leading=13.2,
        textColor=COLORS["ink"],
        spaceAfter=5,
    )
    styles["small"] = ParagraphStyle(
        "Small",
        parent=styles["body"],
        fontSize=8.4,
        leading=11.2,
        textColor=COLORS["muted"],
        spaceAfter=3,
    )
    styles["callout"] = ParagraphStyle(
        "Callout",
        parent=styles["body"],
        fontName="Helvetica-Bold",
        fontSize=9.4,
        leading=12.8,
        textColor=COLORS["navy"],
        leftIndent=7,
        rightIndent=7,
        spaceBefore=4,
        spaceAfter=4,
    )
    styles["table_header"] = ParagraphStyle(
        "TableHeader",
        parent=styles["body"],
        fontName="Helvetica-Bold",
        fontSize=8.2,
        leading=10,
        textColor=colors.white,
        alignment=TA_LEFT,
    )
    styles["table"] = ParagraphStyle(
        "Table",
        parent=styles["body"],
        fontSize=7.75,
        leading=9.6,
        spaceAfter=0,
    )
    styles["toc"] = ParagraphStyle(
        "TOC",
        parent=styles["body"],
        fontSize=9.2,
        leading=12.2,
        leftIndent=10,
        firstLineIndent=-10,
    )
    return styles


STEPS = [
    {
        "no": "1",
        "name": "Executive Opportunity Terrain Mapping",
        "purpose": "Understand strategy, operating context, leverage areas, trust boundaries, and who can explain how work actually happens.",
        "inputs": "Sponsor/executive conversation, strategic priorities, business model context, high-level org shape, known constraints.",
        "work": "Operating partner leads the conversation. AI structures themes and possible discovery zones. Client executives give context and name who understands the work.",
        "output": "Executive terrain map, trust boundaries, candidate opportunity zones, roles to interview, early evidence hypotheses.",
        "stop": "Stop when the opportunity landscape is understood well enough to design discovery, without asking executives about low-level task mechanics.",
    },
    {
        "no": "2",
        "name": "Opportunity Terrain Synthesis And Discovery Sequencing",
        "purpose": "Turn executive terrain into a sequenced discovery plan that finds AI opportunity without asking the client to self-diagnose automation potential.",
        "inputs": "Step 1 terrain, org structure, sponsor priorities, business-unit boundaries, suspected leverage zones.",
        "work": "AI drafts the opportunity map and discovery zones. Operating partner applies judgment and chooses sequence. Client confirms priorities and access.",
        "output": "Opportunity terrain synthesis, discovery-zone sequence, interview coverage matrix, preliminary planning-evidence list.",
        "stop": "Stop when the next interviews are targeted by organizational zone, role layer, portfolio variation, and likely knowledge density.",
    },
    {
        "no": "3",
        "name": "Role-Aware AI-Led Interviews",
        "purpose": "Capture how work actually happens across layers without making participants defend problems or upload files during the interview.",
        "inputs": "Interview plan, role list, discovery zones, AI interviewer prompt, role-specific interview guide.",
        "work": "Participants talk to the AI interviewer. AI captures work episodes, edge cases, sources, source access paths, truth production, approvals, and silent evidence needs. Operating partner monitors coverage and quality.",
        "output": "Interview notes/transcripts, edge case register, source access register, truth production signals, silent evidence need log.",
        "stop": "Stop when the role sample has enough saturation to model the workflow and variation, or when gaps are clear enough to target additional interviews.",
    },
    {
        "no": "4",
        "name": "Planning-Evidence Follow-Up",
        "purpose": "Request only the smallest useful evidence needed to validate important claims, source conflicts, access paths, and truth production chains.",
        "inputs": "Silent evidence needs from Step 3, disputed objects, fragile truth signals, source access unknowns, edge cases.",
        "work": "AI consolidates evidence needs. Operating partner curates the request. Client provides approved redacted examples, screenshots, walkthroughs, reports, formulas, macro walkthroughs, sample exports, or data dictionaries.",
        "output": "Curated planning-evidence request and evidence log tied to workflow objects and truth profiles.",
        "stop": "Stop when evidence needs are specific, owner-grouped, redaction-aware, and do not request credentials, broad live access, or uploads during interviews.",
    },
    {
        "no": "5",
        "name": "AI-Native Workflow Intelligence Object",
        "purpose": "Convert interviews and evidence into structured organizational intelligence that an AI system can understand, not a prose report for a human to read.",
        "inputs": "Steps 1-4, interviews, planning evidence, edge cases, source registers, role coverage, truth production signals.",
        "work": "AI builds a machine-readable workflow object. Operating partner checks realism and scope. Client is not asked to review the whole object.",
        "output": "Structured workflow intelligence with roles, actors, steps, decisions, edge cases, information objects, source access profiles, truth production profiles, approvals, sensitive data signals, evidence, confidence, and unknowns.",
        "stop": "Stop when the workflow graph exists and incomplete source/truth/owner/sensitivity/access/permission fields are routed to Step 7.",
    },
    {
        "no": "6",
        "name": "Organizational Intelligence Diagnostic",
        "purpose": "Attach findings to the workflow object and explain what patterns matter before deciding whether AI belongs anywhere.",
        "inputs": "Step 5 workflow intelligence object, interview variation, edge cases, source conflicts, truth production gaps.",
        "work": "AI drafts object-linked findings. Operating partner separates symptoms from likely root causes and decides which findings matter.",
        "output": "Diagnostic findings across process, people, knowledge, data, governance, systems, risk, measurement, and architecture.",
        "stop": "Stop when findings are linked to objects, have evidence and confidence, and route to the correct later step.",
    },
    {
        "no": "7",
        "name": "Controlled Validation And Governance Resolution",
        "purpose": "Validate the model and resolve object-specific governance questions without handing the whole organizational intelligence object to everyone.",
        "inputs": "Step 5 object, Step 6 diagnostic, source access profiles, truth production profiles, unresolved governance fields.",
        "work": "AI pre-fills controlled views. Operating partner routes each unresolved item to the smallest authorized resolver group. Client resolvers confirm official sources, de facto trusted sources, truth chains, owners, access paths, sensitivity, retention, and permitted AI actions.",
        "output": "Validation event, corrections, disputed items, source inventory enrichment, confirmed or unresolved truth production decisions.",
        "stop": "Stop when critical objects are validated or explicitly disputed/blocked, with remaining gaps routed instead of re-interviewing the whole organization.",
    },
    {
        "no": "8",
        "name": "AI Knowledge And Guideline Requirements Map",
        "purpose": "Identify what knowledge, examples, and future AI guidelines are required before the AI can reason safely.",
        "inputs": "Workflow object, diagnostic, edge cases, validation events, truth profiles, approval gates, decisions, planning evidence.",
        "work": "AI infers knowledge requirements and likely experts. Operating partner prioritizes what matters. Client confirms only targeted high-risk or low-confidence items.",
        "output": "Knowledge requirement map with linked decisions, likely owners, where knowledge lives, evidence, examples needed, AI relevance, and next route.",
        "stop": "Stop when required knowledge is mapped. Do not write final agent rules yet.",
    },
    {
        "no": "9",
        "name": "AI Guidance Pack",
        "purpose": "Turn prioritized knowledge requirements into structured guidance, rules, examples, output contracts, and eval cases for future implementation.",
        "inputs": "Step 8 requirements, validated workflow objects, truth profiles, source hierarchy, risk/sensitivity signals.",
        "work": "AI drafts a machine-readable guidance spec, readable view, and test cases. Operating partner checks usefulness. Subject-matter owners validate rules and examples.",
        "output": "Canonical guidance spec plus readable guide and eval cases covering good, bad, edge, source conflict, fragile truth, and escalation scenarios.",
        "stop": "Stop when guidance is structured enough for future prompts, tool policies, product controls, and evals. It is not a deployed agent.",
    },
    {
        "no": "10",
        "name": "Measurement Intelligence And Analytics Readiness",
        "purpose": "Define which measurements future AI can trust, conditionally use, dispute, avoid, or route for remediation.",
        "inputs": "Workflow decisions, metrics, reports, KPI needs, truth profiles, current dashboards, spreadsheets, manual reports.",
        "work": "AI drafts decision-to-metric maps and trust classifications. Operating partner decides which metrics matter. Client confirms formulas, owners, sources, freshness, quality checks, reproducibility, auditability, and allowed AI usage.",
        "output": "Measurement intelligence object, KPI dictionary needs, metric trust classification, reporting gaps, agent-safe metric usage.",
        "stop": "Stop when every material metric has trust status and AI-safe usage. Do not build dashboards or pipelines.",
    },
    {
        "no": "11",
        "name": "Business Value Case",
        "purpose": "Decide whether the opportunity is economically credible enough to carry forward.",
        "inputs": "Workflow strain, metric trust, value signals, risk reduction, cycle time, rework, capacity, revenue, client priorities.",
        "work": "AI drafts evidence-linked value hypotheses and ranges. Operating partner judges credibility and strategic fit. Client confirms volumes, cost assumptions, risk tolerance, and what leadership values.",
        "output": "Business value case with assumptions, confidence, dependencies, recommendation, and carry-forward or remediation path.",
        "stop": "Stop when value is credible enough to justify technical/risk blueprinting or when the opportunity is deprioritized. Fragile metrics cannot be used as reliable baseline evidence unless the value case is about fixing measurement/truth infrastructure.",
    },
    {
        "no": "12",
        "name": "Technical Implementation Blueprint",
        "purpose": "Define what would need to be built later, without building anything during the 16-step engagement.",
        "inputs": "Surviving opportunity, workflow object, guidance, measurement, value case, source access profiles, truth remediation needs, client stack constraints.",
        "work": "AI drafts future architecture, runtime, hosting, access, MCP/tool, connector, normalization, identity, truth-rule extraction, test, and credential/secrets requirements. IT/data/security confirm feasibility as a plan.",
        "output": "Technical blueprint with future access paths, blocked paths, component contracts, normalization plan, truth remediation plan, hosting/environment requirements, and build sequence.",
        "stop": "Stop when a future build team could understand the technical path and constraints without live access or credentials.",
    },
    {
        "no": "13",
        "name": "Risk And Control Model",
        "purpose": "Design the future controls that would make the AI safe enough to test and operate after approval.",
        "inputs": "Steps 5-12, sensitive fields, future tools, outputs, approval gates, truth risks, access paths, credential/secrets plan.",
        "work": "AI derives risk register, data classification, zero-trust controls, tool permissions, output controls, stop conditions, and incident paths. Operating partner judges materiality. Client risk/security/legal/compliance and system owners confirm protocols.",
        "output": "Risk register, control model, permission matrix, output controls, logging/monitoring/revocation plan, stop conditions.",
        "stop": "Stop when risks are owned and controls are testable. Do not provision access or deploy monitoring.",
    },
    {
        "no": "14",
        "name": "AI-Agent Readiness Score",
        "purpose": "Make the build/fix/do-not-automate decision evidence-based and behavior-specific.",
        "inputs": "Steps 5-13, value case, guidance, measurement intelligence, technical blueprint, risk/control model, truth profiles.",
        "work": "AI scores hard gates and dimensions. Operating partner challenges the score and chooses minimum safe first behavior. Client confirms only unresolved priority, source, owner, feasibility, risk, and approval facts.",
        "output": "Readiness object with hard gates, truth production gate, behavior-level readiness, dependency map, blockers, minimum safe first behavior, prohibited behaviors, and Step 15 path.",
        "stop": "Stop when every candidate opportunity has a readiness object. Do not start implementation from a score alone.",
    },
    {
        "no": "15",
        "name": "Implementation Decision Packet",
        "purpose": "Create the canonical implementation decision packet: build-ready brief, remediation plan, or do-not-automate recommendation.",
        "inputs": "Steps 1-14, especially readiness object, technical blueprint, risk/control model, guidance, measurement, value case, workflow object, validation events.",
        "work": "AI assembles the packet and controlled audience views. Operating partner narrows scope and makes the recommendation. Client sponsor decides whether to continue toward implementation after Step 16.",
        "output": "Machine-readable packet with scope, behavior contract, systems, future access requests, runtime/hosting requirements, component contracts, normalization/truth remediation, tests, controls, owners, sequence, and stop conditions.",
        "stop": "Stop when a future decision can be made from the packet. If material truth is fragile, route to remediation unless selected behavior is safe-limited.",
    },
    {
        "no": "16",
        "name": "Managed Lifecycle Object",
        "purpose": "Define how the future AI capability, remediation plan, or no-automation decision will be owned and governed after approval.",
        "inputs": "Step 15 packet, readiness, risk controls, technical blueprint, value case, measurement, guidance, truth governance needs, workflow object.",
        "work": "AI drafts the lifecycle object. Operating partner tests whether ownership and cadence are realistic. Client confirms approval forum, owners, monitoring, incident, revocation, feedback, source freshness, and governance cadence as a plan.",
        "output": "Managed lifecycle, remediation lifecycle, or no-automation review cadence with launch gates, validation, monitoring, truth governance, feedback, incidents, revocation, updates, expansion, and retirement.",
        "stop": "Stop when the future operating model can answer who owns it, what proves it works, what pauses it, how truth/source changes are handled, and when it retires. Implementation starts only after separate approval.",
    },
]


TRUTH_STATUSES = [
    ("authoritative", "Official and de facto source align; owner, derivation, quality checks, reproducibility, and auditability are sufficient."),
    ("conditionally_reliable", "Usable only with explicit caveats, timing rules, human review, source hierarchy, or limited behavior."),
    ("shadow_derived", "Trusted output comes from a spreadsheet, tracker, report, shared-drive file, macro, email thread, or local artifact outside governed systems."),
    ("manually_adjusted", "Material truth depends on manual edits, adjustments, copy/paste steps, or semi-documented corrections."),
    ("person_dependent", "Only one person or a small group knows how to produce or interpret the truth."),
    ("disputed", "Official source, de facto source, formula, owner, or decision use conflicts across teams."),
    ("missing", "No credible source or production chain has been identified."),
    ("not_reproducible", "The output cannot be recreated from known inputs, rules, and evidence."),
    ("unknown", "The engagement has not yet resolved the truth status."),
]


PHASES = [
    ("1. Orient", "Steps 1-2", "Understand business terrain, sequence discovery, and choose where to look first."),
    ("2. Discover", "Steps 3-4", "Interview across layers and request targeted planning evidence only after interviews."),
    ("3. Structure", "Steps 5-7", "Build AI-native organizational intelligence, diagnose patterns, and validate the model through controlled views."),
    ("4. Enrich", "Steps 8-13", "Add knowledge, guidance, measurement, value, technical blueprint, and risk/control design."),
    ("5. Decide", "Steps 14-16", "Score readiness, create the implementation decision packet, and define the future lifecycle."),
]


def para(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"), style)


def rich_para(text: str, style: ParagraphStyle) -> Paragraph:
    safe = (
        text.replace("&", "&amp;")
        .replace("<b>", "<b>")
        .replace("</b>", "</b>")
        .replace("<i>", "<i>")
        .replace("</i>", "</i>")
        .replace("<br/>", "<br/>")
    )
    return Paragraph(safe, style)


def bullets(items: list[str], styles: dict[str, ParagraphStyle], level: str = "body") -> ListFlowable:
    return ListFlowable(
        [ListItem(para(item, styles[level]), bulletColor=COLORS["teal"]) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=14,
        bulletFontSize=6,
        spaceAfter=4,
    )


def table_cell(text: str, styles: dict[str, ParagraphStyle]) -> Paragraph:
    return para(text, styles["table"])


def data_table(
    rows: list[list[str]],
    styles: dict[str, ParagraphStyle],
    widths: list[float],
    header_color=COLORS["navy"],
) -> Table:
    data = []
    for idx, row in enumerate(rows):
        row_style = styles["table_header"] if idx == 0 else styles["table"]
        data.append([para(cell, row_style) for cell in row])
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), header_color),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.35, COLORS["line"]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, COLORS["soft"]]),
            ]
        )
    )
    return table


def callout(text: str, styles: dict[str, ParagraphStyle], color=COLORS["soft_teal"]) -> Table:
    table = Table([[rich_para(text, styles["callout"])]], colWidths=[CONTENT_WIDTH])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), color),
                ("BOX", (0, 0), (-1, -1), 0.6, COLORS["line"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


def header_footer(canvas, doc):
    canvas.saveState()
    page = canvas.getPageNumber()
    if page > 1:
        canvas.setStrokeColor(COLORS["line"])
        canvas.setLineWidth(0.5)
        canvas.line(LEFT_MARGIN, PAGE_HEIGHT - 0.45 * inch, PAGE_WIDTH - RIGHT_MARGIN, PAGE_HEIGHT - 0.45 * inch)
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(COLORS["muted"])
        canvas.drawString(LEFT_MARGIN, PAGE_HEIGHT - 0.32 * inch, "AI Operating Partner 16-Step Process Guide")
        canvas.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, 0.34 * inch, f"Page {page}")
    canvas.restoreState()


def add_title_page(story, styles):
    story.append(Spacer(1, 0.6 * inch))
    story.append(para("AI Operating Partner", styles["title"]))
    story.append(para("16-Step Process Guide", styles["title"]))
    story.append(
        para(
            "A detailed operating manual for turning enterprise discovery into structured organizational intelligence, implementation decisions, and managed AI lifecycle design.",
            styles["subtitle"],
        )
    )
    story.append(Spacer(1, 0.18 * inch))
    story.append(
        callout(
            "<b>Core promise:</b> The process discovers where AI agents fit by understanding how work, decisions, data, knowledge, risk, and business truth actually operate inside the organization. It never assumes clean data or a clean source of truth.",
            styles,
        )
    )
    story.append(Spacer(1, 0.22 * inch))
    story.append(
        data_table(
            [
                ["Engagement Type", "Boundary", "Primary Deliverable"],
                [
                    "Pre-build operating partner engagement",
                    "No agents, MCPs, connectors, credentials, live integrations, normalization builds, all-email ingestion, or production automation during the 16 steps.",
                    "Structured organizational intelligence plus an implementation decision packet and lifecycle object.",
                ],
            ],
            styles,
            [1.55 * inch, 2.9 * inch, 2.8 * inch],
            header_color=COLORS["teal"],
        )
    )
    story.append(Spacer(1, 0.22 * inch))
    story.append(para("Generated from the AI operating partner system, May 2026.", styles["small"]))
    story.append(PageBreak())


def add_toc(story, styles):
    story.append(para("Contents", styles["h1"]))
    toc_items = [
        "1. What This Process Is",
        "2. Operating Model: AI, Operating Partner, Client",
        "3. The Five Process Phases",
        "4. Step-By-Step Operating Guide",
        "5. Truth Production Layer",
        "6. Data, Access, Normalization, And Legacy Systems",
        "7. Readiness And Decision Logic",
        "8. Example: Retail Real Estate Asset Management",
        "9. Final Deliverables And Quality Bar",
    ]
    for item in toc_items:
        story.append(para(item, styles["toc"]))
    story.append(PageBreak())


def add_overview(story, styles):
    story.append(para("1. What This Process Is", styles["h1"]))
    story.append(
        para(
            "The AI operating partner process is a 16-step pre-build engagement. Its purpose is to discover where AI agents, AI copilots, workflow automation, analytics improvements, or data readiness work actually belong inside an organization.",
            styles["body"],
        )
    )
    story.append(
        para(
            "The process does not begin by asking executives what can be automated. Most companies cannot answer that accurately because their work is distributed across roles, systems, spreadsheets, meetings, exceptions, approvals, informal knowledge, and hidden reconciliation habits. Instead, the process builds structured organizational intelligence from evidence.",
            styles["body"],
        )
    )
    story.append(
        callout(
            "<b>Important:</b> The system treats Excel macros, shadow trackers, manual reports, recurring reconciliations, and expert memory as intelligence assets. They are not ignored, mocked, or treated as embarrassing exceptions.",
            styles,
            COLORS["soft_amber"],
        )
    )
    story.append(para("The engagement answers six practical questions:", styles["h2"]))
    story.append(
        bullets(
            [
                "Where in the organization does AI belong, and where does it not belong yet?",
                "Which workflows, decisions, and information objects matter?",
                "How is business truth actually produced, and where is it fragile?",
                "What knowledge, rules, examples, measurements, and controls would future AI need?",
                "What technical architecture, access paths, normalization, and remediation would be required later?",
                "Is the opportunity build-ready, remediation-first, or not worth automating?",
            ],
            styles,
        )
    )
    story.append(para("2. Operating Model: AI, Operating Partner, Client", styles["h1"]))
    story.append(
        data_table(
            [
                ["Role", "Primary Job", "What They Should Not Do"],
                [
                    "AI",
                    "Interview, extract, structure, triangulate, draft, score, map dependencies, generate machine-readable artifacts, and preserve evidence links.",
                    "Make final business judgment, assume truth, request live credentials, or start implementation.",
                ],
                [
                    "Operating Partner",
                    "Own scope, interpretation, client trust, prioritization, judgment, recommendation, sequencing, and quality control.",
                    "Outsource judgment to the client or let AI-generated artifacts become unchallenged recommendations.",
                ],
                [
                    "Client",
                    "Provide goals, examples, planning evidence, ownership decisions, source/truth confirmations, constraints, and approvals.",
                    "Self-diagnose automation potential or review the entire organizational intelligence object.",
                ],
            ],
            styles,
            [1.3 * inch, 3.1 * inch, 2.85 * inch],
        )
    )


def add_phases(story, styles):
    story.append(para("3. The Five Process Phases", styles["h1"]))
    story.append(
        data_table(
            [["Phase", "Steps", "Purpose"]] + [[name, steps, purpose] for name, steps, purpose in PHASES],
            styles,
            [1.35 * inch, 1.0 * inch, 4.9 * inch],
            header_color=COLORS["teal"],
        )
    )
    story.append(Spacer(1, 0.12 * inch))
    story.append(
        callout(
            "<b>Process rule:</b> Build work starts only after Step 16 is complete, the blueprint is approved, and the client authorizes a separate implementation phase.",
            styles,
        )
    )


def add_step_guide(story, styles):
    story.append(PageBreak())
    story.append(para("4. Step-By-Step Operating Guide", styles["h1"]))
    story.append(
        para(
            "Each step has a clear purpose, input set, responsibility split, output, and stop condition. The stop condition matters because it prevents the engagement from drifting into implementation before the organization is ready.",
            styles["body"],
        )
    )
    for step in STEPS:
        story.append(Spacer(1, 0.04 * inch))
        story.append(para(f"Step {step['no']}: {step['name']}", styles["h2"]))
        story.append(para(step["purpose"], styles["body"]))
        story.append(
            data_table(
                [
                    ["Input", "Who Does The Work", "Output", "Stop Condition"],
                    [step["inputs"], step["work"], step["output"], step["stop"]],
                ],
                styles,
                [1.75 * inch, 2.1 * inch, 1.9 * inch, 1.5 * inch],
                header_color=COLORS["navy"],
            )
        )


def add_truth_layer(story, styles):
    story.append(PageBreak())
    story.append(para("5. Truth Production Layer", styles["h1"]))
    story.append(
        para(
            "A major hardening rule in this system is that source of truth is never assumed. The methodology discovers truth production: how final numbers, statuses, decisions, reports, board packets, approval packages, and operational facts are actually produced.",
            styles["body"],
        )
    )
    story.append(
        para(
            "The key object is <b>truth_production_profile</b>. It follows material truth across the process from interviews through validation, knowledge mapping, measurement, architecture, risk, readiness, decision packet, and lifecycle governance.",
            styles["body"],
        )
    )
    story.append(para("What A Truth Production Profile Captures", styles["h2"]))
    story.append(
        data_table(
            [
                ["Field", "Meaning"],
                ["official_source", "What policy, system design, or leadership says should be authoritative."],
                ["de_facto_source", "What people actually trust or use when work must get done."],
                ["truth_production_chain", "Exports, formulas, macros, manual adjustments, reconciliations, expert judgment, approvals, and final reporting steps."],
                ["embedded_business_rules", "Rules encoded in system configuration, report logic, formulas, macros, SOPs, meeting habits, or expert memory."],
                ["owner / steward / knower", "Who owns the truth, maintains it, and understands how it is produced."],
                ["reproducibility / auditability", "Whether the output can be recreated and reviewed from known inputs and rules."],
                ["ai_safe_usage", "What future AI may summarize, compare, cite, calculate, recommend, or must escalate/refuse."],
            ],
            styles,
            [2.05 * inch, 5.2 * inch],
        )
    )
    story.append(para("Truth Status Classification", styles["h2"]))
    story.append(
        data_table(
            [["Status", "Definition"]] + [[status, definition] for status, definition in TRUTH_STATUSES],
            styles,
            [1.85 * inch, 5.4 * inch],
            header_color=COLORS["teal"],
        )
    )
    story.append(Spacer(1, 0.12 * inch))
    story.append(
        callout(
            "<b>Fragile truth rule:</b> If material truth is shadow_derived, manually_adjusted, person_dependent, disputed, missing, or not_reproducible, Step 14 must fail or conditionally pass the relevant behavior level unless the proposed AI behavior is limited to summarize, compare, flag uncertainty, draft clarification questions, or escalate.",
            styles,
            COLORS["soft_amber"],
        )
    )
    story.append(para("Where Truth Production Appears", styles["h2"]))
    story.append(
        data_table(
            [
                ["Steps", "How It Is Used"],
                ["3-4", "Interviews identify hidden truth chains; evidence follow-up requests formulas, macro walkthroughs, redacted reports, screenshots, sample exports, or reconciliation notes when needed."],
                ["5-7", "Workflow intelligence stores truth profiles; validation resolves official source, de facto source, owner, reproducibility, auditability, and AI-safe use."],
                ["8-10", "Macros, manual adjustments, reconciliations, and expert memory become knowledge and measurement requirements."],
                ["11-13", "Fragile metrics are excluded from value baselines unless the value case is about fixing truth infrastructure; architecture and controls define remediation paths."],
                ["14-16", "Truth production becomes a readiness gate, decision-packet routing rule, and lifecycle governance obligation."],
            ],
            styles,
            [1.1 * inch, 6.15 * inch],
        )
    )


def add_data_access(story, styles):
    story.append(PageBreak())
    story.append(para("6. Data, Access, Normalization, And Legacy Systems", styles["h1"]))
    story.append(
        para(
            "The 16-step process produces an implementable plan, but it intentionally does not build the implementation. This distinction is especially important for legacy systems, APIs, credentials, MCPs, connectors, data normalization, and email access.",
            styles["body"],
        )
    )
    story.append(
        data_table(
            [
                ["Topic", "Where It Is Planned", "What Happens During The 16 Steps", "What Waits Until After Step 16"],
                [
                    "Legacy systems",
                    "Steps 3, 5, 7, 12",
                    "Capture system names, reports, modules, access paths, owner roles, vendor constraints, export limits, and failure modes.",
                    "No live integration, service account, credential request, connector build, or RPA build.",
                ],
                [
                    "APIs, MCPs, connectors",
                    "Steps 12, 15, 16",
                    "Define future component contracts, permission scope, input/output contract, logging, approval dependencies, and sandbox preference.",
                    "No MCP server, connector, token, production API connection, or email ingestion is built.",
                ],
                [
                    "Data normalization",
                    "Steps 10, 12, 15",
                    "Define canonical entities, field mappings, identity resolution, quality checks, freshness requirements, blockers, and owners.",
                    "No ETL/ELT, warehouse, lakehouse, vector index, semantic layer, or normalization pipeline is built.",
                ],
                [
                    "Credentials and access",
                    "Steps 12, 13, 15, 16",
                    "Create a future access request package with purpose, scope, prohibited permissions, provisioning owner, secrets handling, rotation, revocation, and audit logging.",
                    "No employee credentials, live API tokens, broad live access, all-email access, or production secrets are requested.",
                ],
                [
                    "Planning evidence",
                    "Step 4",
                    "Request targeted redacted artifacts, screenshots, formula/macro walkthroughs, sample exports, schema lists, or data dictionaries tied to specific objects.",
                    "No broad data-room access, bulk unredacted data, or live data sync.",
                ],
            ],
            styles,
            [1.2 * inch, 1.0 * inch, 2.55 * inch, 2.5 * inch],
        )
    )
    story.append(
        callout(
            "<b>Practical meaning:</b> The operating partner should know enough by the end of Step 16 to specify exactly what future access, tools, normalization, and controls are needed. But the actual build begins only after separate implementation approval.",
            styles,
        )
    )


def add_readiness(story, styles):
    story.append(para("7. Readiness And Decision Logic", styles["h1"]))
    story.append(
        para(
            "Step 14 is not a simple score. It is a gate-based readiness object. Hard gates override averages, and readiness is behavior-specific: read-only summary can be safe while recommendation support or autonomous action is blocked.",
            styles["body"],
        )
    )
    story.append(
        data_table(
            [
                ["Gate", "Question"],
                ["Business value", "Is the outcome important enough to justify the work?"],
                ["Workflow clarity", "Is the workflow known well enough to model?"],
                ["Source access", "Are required sources, access paths, lookup keys, owners, and failure modes known or scoped out?"],
                ["Data quality", "Are quality issues understood and safe for the proposed behavior?"],
                ["Truth production", "Are material truth chains known, owned, reproducible enough, auditable enough, and safe for AI use?"],
                ["Knowledge/guidance", "Are rules, examples, source hierarchy, forbidden behaviors, and escalations sufficient?"],
                ["Measurement", "Can value and performance be measured with trusted or conditionally trusted metrics?"],
                ["Technical feasibility", "Is the future access, runtime, integration, hosting, and test path feasible as a plan?"],
                ["Risk/control", "Are permissions, outputs, approvals, logging, monitoring, incident, and revocation controls defined?"],
                ["Human oversight", "Is there a named accountable reviewer and approval path?"],
                ["Lifecycle", "Will the future AI be owned, monitored, updated, paused, expanded, and retired responsibly?"],
            ],
            styles,
            [1.55 * inch, 5.7 * inch],
            header_color=COLORS["teal"],
        )
    )
    story.append(para("Step 15 Routing", styles["h2"]))
    story.append(
        bullets(
            [
                "build_ready_implementation_brief - only when gates and dependencies support a safe first build path.",
                "gap_remediation_plan - when specific blockers must be fixed before a build-ready brief.",
                "governance_data_readiness_plan - when ownership, source access, truth production, or data quality blocks progress.",
                "knowledge_capture_plan - when tacit rules, expert memory, or examples are not captured enough.",
                "technical_feasibility_plan - when APIs, exports, vendor constraints, normalization, or architecture need confirmation.",
                "risk_control_plan - when permissions, sensitive data, approval gates, or output controls are insufficient.",
                "do_not_automate_recommendation - when the work should not be automated or the risk/value tradeoff is wrong.",
            ],
            styles,
        )
    )


def add_example(story, styles):
    story.append(PageBreak())
    story.append(para("8. Example: Retail Real Estate Asset Management", styles["h1"]))
    story.append(
        para(
            "Assume a 60-person real estate asset management firm with a retail portfolio. The asset management team has four layers: 1 VP, 3 Directors, 6 Asset Managers, and 20 Assistant Asset Managers. The process does not interview all 30 people by default. It uses stratified coverage and expands only where variation or risk requires it.",
            styles["body"],
        )
    )
    story.append(
        data_table(
            [
                ["Process Area", "Example Application"],
                ["Interview strategy", "Interview the VP for terrain, all or selected Directors for portfolio/team variation, a sample of Asset Managers by portfolio type, and enough Assistant Asset Managers to capture execution variation and edge cases."],
                ["Workflow example", "Tenant renewal review: identify upcoming renewals, collect lease abstract, AR aging, tenant sales, broker feedback, strategy context, approvals, and decision criteria."],
                ["Truth production example", "Critical date report may be the de facto trigger, lease abstract may be candidate official source, and final renewal brief may include manual adjustments or expert judgment."],
                ["Safe first AI behavior", "Draft a renewal brief, summarize sources, flag missing inputs, compare conflicting dates, draft clarification questions, and route decisions to humans."],
                ["Blocked behavior", "Make renewal decision, send tenant communication, approve economics, rely on disputed NOI/AR values, or take autonomous action."],
                ["Remediation example", "If final board NOI comes from a shadow Excel macro, Step 14 blocks recommendation/autonomous behavior and Step 15 routes to truth-rule extraction, formula documentation, reconciliation tests, or owner assignment."],
            ],
            styles,
            [1.55 * inch, 5.7 * inch],
        )
    )
    story.append(para("How The Same Example Moves Through Steps", styles["h2"]))
    story.append(
        bullets(
            [
                "Steps 1-2 find retail asset management as a high-leverage discovery zone without asking executives to describe every task.",
                "Step 3 interviews capture actual renewal episodes, exceptions, reports, trackers, broker emails, approvals, and what people trust.",
                "Step 5 creates unique role and object IDs for the workflow, information objects, source access profiles, and truth profiles.",
                "Step 7 validates only controlled slices with the right owners, not the entire organizational intelligence object.",
                "Steps 8-10 convert expert rules, metrics, and fragile truth into machine-readable guidance and measurement intelligence.",
                "Steps 12-16 define the future technical, control, readiness, decision, and lifecycle plan before any build begins.",
            ],
            styles,
        )
    )


def add_final_deliverables(story, styles):
    story.append(para("9. Final Deliverables And Quality Bar", styles["h1"]))
    story.append(
        data_table(
            [
                ["Final Artifact", "What It Must Let A Future Team Understand"],
                ["Step 5 Workflow Intelligence", "Roles, people layers, workflow steps, decisions, edge cases, information objects, sources, truth production, approvals, evidence, and unknowns."],
                ["Step 9 Guidance Pack", "How future AI should reason, use sources, handle truth conflicts, escalate, format output, and pass eval cases."],
                ["Step 10 Measurement Intelligence", "Which metrics are trusted, conditional, disputed, untrusted, shadow-derived, manually adjusted, person-dependent, missing, or not reproducible."],
                ["Step 12 Technical Blueprint", "Future access paths, system constraints, runtime, hosting, tools/MCP/connectors, normalization, identity resolution, truth remediation, tests, credential/secrets approach, and build sequence."],
                ["Step 13 Risk/Control Model", "Data classification, tool permissions, output controls, approval gates, logging, monitoring, incident response, revocation, and stop conditions."],
                ["Step 14 Readiness Object", "Hard gates, behavior-level readiness, dependencies, blockers, minimum safe first behavior, and Step 15 path."],
                ["Step 15 Decision Packet", "Build-ready brief, remediation plan, or do-not-automate recommendation with owner, sequence, tests, controls, and future access request package."],
                ["Step 16 Lifecycle Object", "Ownership, launch gates, validation, monitoring, truth governance, feedback, incidents, revocation, updates, expansion, retirement, and governance cadence."],
            ],
            styles,
            [2.0 * inch, 5.25 * inch],
            header_color=COLORS["teal"],
        )
    )
    story.append(Spacer(1, 0.12 * inch))
    story.append(
        callout(
            "<b>Definition of done:</b> A future build team should be able to understand scope, behavior, systems, truth production status, runtime pattern, hosting requirements, access requests, normalization, remediation, tests, controls, owners, sequence, and stop conditions without rediscovering the organization.",
            styles,
        )
    )


def build_pdf() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    styles = make_styles()
    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=letter,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN,
        title="AI Operating Partner 16-Step Process Guide",
        author="AI Operating Partner System",
    )
    story = []
    add_title_page(story, styles)
    add_toc(story, styles)
    add_overview(story, styles)
    add_phases(story, styles)
    add_step_guide(story, styles)
    add_truth_layer(story, styles)
    add_data_access(story, styles)
    add_readiness(story, styles)
    add_example(story, styles)
    add_final_deliverables(story, styles)
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)


def build_markdown() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# AI Operating Partner 16-Step Process Guide\n")
    lines.append(
        "A detailed operating manual for turning enterprise discovery into structured organizational intelligence, implementation decisions, and managed AI lifecycle design.\n"
    )
    lines.append(
        "**Core promise:** The process discovers where AI agents fit by understanding how work, decisions, data, knowledge, risk, and business truth actually operate inside the organization. It never assumes clean data or a clean source of truth.\n"
    )
    lines.append("## Process Boundary\n")
    lines.append(
        "The 16-step engagement is pre-build. It does not build agents, MCPs, connectors, live integrations, normalization pipelines, email ingestion, production automations, or request credentials during the engagement.\n"
    )
    lines.append("## Step-By-Step Guide\n")
    for step in STEPS:
        lines.append(f"### Step {step['no']}: {step['name']}\n")
        lines.append(f"**Purpose:** {step['purpose']}\n")
        lines.append(f"**Input:** {step['inputs']}\n")
        lines.append(f"**Who does the work:** {step['work']}\n")
        lines.append(f"**Output:** {step['output']}\n")
        lines.append(f"**Stop condition:** {step['stop']}\n")
    lines.append("## Truth Production Layer\n")
    lines.append(
        "The key cross-step object is `truth_production_profile`, which captures official source, de facto trusted source, production chain, embedded rules, owner/steward/knower, truth status, reproducibility, auditability, AI-safe usage, and required fix.\n"
    )
    for status, definition in TRUTH_STATUSES:
        lines.append(f"- `{status}`: {definition}\n")
    lines.append("\n**Fragile truth rule:** If material truth is shadow-derived, manually adjusted, person-dependent, disputed, missing, or not reproducible, Step 14 must fail or conditionally pass the relevant behavior level unless AI behavior is limited to summarize, compare, flag uncertainty, draft clarification questions, or escalate.\n")
    MD_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    build_markdown()
    build_pdf()
    print(PDF_PATH)
    print(MD_PATH)


if __name__ == "__main__":
    main()
