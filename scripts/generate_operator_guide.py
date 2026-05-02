from __future__ import annotations

from pathlib import Path
from typing import Iterable

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
PDF_PATH = OUT_DIR / "ai-operating-partner-operator-guide.pdf"
MD_PATH = OUT_DIR / "ai-operating-partner-operator-guide.md"
PREVIEW_DIR = OUT_DIR / "previews" / "operator-guide"

PAGE_WIDTH, PAGE_HEIGHT = letter
LEFT_MARGIN = RIGHT_MARGIN = 0.58 * inch
TOP_MARGIN = 0.62 * inch
BOTTOM_MARGIN = 0.58 * inch
CONTENT_WIDTH = PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN

COLORS = {
    "ink": colors.HexColor("#1E2933"),
    "muted": colors.HexColor("#5B6773"),
    "navy": colors.HexColor("#243B53"),
    "blue": colors.HexColor("#2F80ED"),
    "teal": colors.HexColor("#0F766E"),
    "green": colors.HexColor("#2F855A"),
    "amber": colors.HexColor("#A86E12"),
    "red": colors.HexColor("#B83232"),
    "line": colors.HexColor("#C7D0DA"),
    "soft": colors.HexColor("#F6F8FB"),
    "soft_teal": colors.HexColor("#E6FFFA"),
    "soft_amber": colors.HexColor("#FFF8E1"),
    "soft_red": colors.HexColor("#FFF1F2"),
}


def clean(value: str) -> str:
    return " ".join(value.strip().split())


def make_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    styles: dict[str, ParagraphStyle] = {}
    styles["title"] = ParagraphStyle(
        "Title",
        parent=base["Title"],
        fontName="Helvetica-Bold",
        fontSize=25,
        leading=30,
        textColor=COLORS["navy"],
        alignment=TA_CENTER,
        spaceAfter=10,
    )
    styles["subtitle"] = ParagraphStyle(
        "Subtitle",
        parent=base["BodyText"],
        fontName="Helvetica",
        fontSize=11.5,
        leading=16,
        textColor=COLORS["muted"],
        alignment=TA_CENTER,
        spaceAfter=18,
    )
    styles["h1"] = ParagraphStyle(
        "Heading1",
        parent=base["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=17,
        leading=21,
        textColor=COLORS["navy"],
        spaceBefore=13,
        spaceAfter=6,
    )
    styles["h2"] = ParagraphStyle(
        "Heading2",
        parent=base["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        textColor=COLORS["teal"],
        spaceBefore=10,
        spaceAfter=5,
    )
    styles["h3"] = ParagraphStyle(
        "Heading3",
        parent=base["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=10.8,
        leading=13.5,
        textColor=COLORS["navy"],
        spaceBefore=7,
        spaceAfter=3,
    )
    styles["body"] = ParagraphStyle(
        "Body",
        parent=base["BodyText"],
        fontName="Helvetica",
        fontSize=9.25,
        leading=12.4,
        textColor=COLORS["ink"],
        spaceAfter=4,
    )
    styles["small"] = ParagraphStyle(
        "Small",
        parent=styles["body"],
        fontSize=7.9,
        leading=10.3,
        textColor=COLORS["muted"],
        spaceAfter=2.5,
    )
    styles["table_header"] = ParagraphStyle(
        "TableHeader",
        parent=styles["body"],
        fontName="Helvetica-Bold",
        fontSize=7.7,
        leading=9.5,
        textColor=colors.white,
        alignment=TA_LEFT,
    )
    styles["table"] = ParagraphStyle(
        "Table",
        parent=styles["body"],
        fontSize=7.35,
        leading=9.4,
        spaceAfter=0,
    )
    styles["callout"] = ParagraphStyle(
        "Callout",
        parent=styles["body"],
        fontName="Helvetica-Bold",
        fontSize=8.9,
        leading=12,
        textColor=COLORS["navy"],
        leftIndent=5,
        rightIndent=5,
        spaceBefore=3,
        spaceAfter=3,
    )
    styles["mono"] = ParagraphStyle(
        "Mono",
        parent=styles["body"],
        fontName="Courier",
        fontSize=7.4,
        leading=9.3,
        textColor=COLORS["ink"],
        spaceAfter=0,
    )
    return styles


def para(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(clean(text), style)


def code_para(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(text.replace(" ", "&nbsp;"), style)


def bullets(items: Iterable[str], styles: dict[str, ParagraphStyle]) -> ListFlowable:
    return ListFlowable(
        [ListItem(para(item, styles["body"]), bulletColor=COLORS["teal"]) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=14,
        bulletFontSize=6,
        spaceAfter=4,
    )


def table(
    rows: list[list[str]],
    styles: dict[str, ParagraphStyle],
    col_widths: list[float],
    header_color=COLORS["navy"],
) -> Table:
    data = []
    for row_index, row in enumerate(rows):
        row_style = styles["table_header"] if row_index == 0 else styles["table"]
        data.append([para(cell, row_style) for cell in row])
    t = Table(data, colWidths=col_widths, hAlign="LEFT", repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), header_color),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.35, COLORS["line"]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return t


def callout(
    text: str,
    styles: dict[str, ParagraphStyle],
    fill=COLORS["soft_teal"],
    border=COLORS["line"],
) -> Table:
    t = Table([[para(text, styles["callout"])]], colWidths=[CONTENT_WIDTH])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), fill),
                ("BOX", (0, 0), (-1, -1), 0.6, border),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return t


UMBRELLAS = [
    {
        "name": "Frame And Hypothesize",
        "steps": "0-2",
        "meaning": "Set the engagement boundary, understand executive terrain, and create candidate AI use-case hypotheses. These are not final build decisions.",
    },
    {
        "name": "Discover Reality",
        "steps": "3-5",
        "meaning": "Use role-aware interviews, variation mapping, and targeted evidence follow-up to understand work as it really happens.",
    },
    {
        "name": "Build And Validate The Intelligence Layer",
        "steps": "6-8",
        "meaning": "Create the machine-readable workflow object, diagnose blockers, validate key governance and truth questions, and release Organizational Intelligence Baseline.",
    },
    {
        "name": "Define AI Reasoning Requirements",
        "steps": "9-10",
        "meaning": "Map what the AI must know, then convert high-priority knowledge into guidance, rules, output contracts, and evaluation cases.",
    },
    {
        "name": "Prove Measurement And Value",
        "steps": "11-12",
        "meaning": "Classify which metrics can be trusted, design future AI success metrics, model value and AI-side cost, and select the right opportunities to advance.",
    },
    {
        "name": "Shape The Future Solution",
        "steps": "13-15",
        "meaning": "Decide solution and adoption shape, document technical/vendor blueprint, and design risk and zero-trust controls.",
    },
    {
        "name": "Decide And Govern",
        "steps": "16-18",
        "meaning": "Score readiness, generate the implementation decision packet, and define managed lifecycle and adoption-change obligations.",
    },
]


STEPS = [
    {
        "no": "0",
        "name": "Engagement Tiering And Vertical Extension",
        "purpose": "Decide how deep the engagement should be before discovery starts. This prevents a 60-person company, a 200-agent brokerage, and a 10,000-employee REIT from being forced through the same depth.",
        "question": "What are we scoping, how deep are we going, what domain rules matter, and what is inside or outside the pre-build boundary?",
        "inputs": "Client size, timeline, budget, functions in scope, business model, regulated domain, geographic footprint, sponsor goals, known constraints, and appetite for offline proof points.",
        "op_work": "Choose lite, standard, or deep depth; define scope controls; decide whether a vertical extension applies; explain the no-build boundary; decide whether cheap offline proof points are allowed.",
        "ai_work": "Draft a tier recommendation, likely discovery coverage, vertical/regulatory checklist, artifact plan, and scope-risk warnings.",
        "client_work": "Confirm budget, time, functions in scope, vertical context, legal/security review expectations, and decision forum.",
        "output": "Engagement tiering object, vertical extension object, timeline, scope boundary, offline-proof boundary, and initial responsibility model.",
        "gate": "The process cannot start until depth, scope, domain extension, and build boundary are explicit.",
        "feeds": "Step 1 uses the tier and vertical extension to frame the executive conversation and avoid overcollecting or undercollecting.",
        "example": "For a multifamily REIT, Step 0 decides whether the work covers only maintenance invoice review, the full asset-management operating model, or a cross-functional portfolio view including property management, accounting, leasing, and capex.",
        "watchout": "Do not let a client buy a lite engagement while expecting deep implementation-grade blueprinting across every business unit.",
    },
    {
        "no": "1",
        "name": "Executive Opportunity Terrain Mapping",
        "purpose": "Learn the strategic and operating terrain without asking executives to describe low-level daily tasks they do not personally perform.",
        "question": "Where does leadership believe leverage, complexity, growth, risk, trust boundaries, and operating pressure exist?",
        "inputs": "Sponsor interview, strategy context, org chart sample, portfolio/business-unit map, known initiatives, known constraints, and initial role nominations.",
        "op_work": "Lead the sponsor conversation, listen for strategic terrain, ask who people go to when work breaks, and triangulate nominations beyond loyalist names.",
        "ai_work": "Structure the terrain into opportunity zones, trust boundaries, likely workflows, likely informants, and early assumptions.",
        "client_work": "Provide business direction, constraints, known leverage areas, names of operators, and permission to approach role groups.",
        "output": "Executive opportunity terrain map, named opportunity zones, trust boundaries, org-structure capture, and informant map.",
        "gate": "Enough strategic terrain exists to synthesize discovery zones without pretending executives know every task detail.",
        "feeds": "Step 2 converts the terrain into candidate use-case hypotheses and a discovery sequence.",
        "example": "A REIT CEO might say asset managers spend too much time reconciling property manager updates and board reporting. Step 1 records this as terrain, not as a confirmed AI use case.",
        "watchout": "Do not ask the sponsor for a list of tasks to automate. Ask for operating terrain, not self-diagnosis.",
    },
    {
        "no": "2",
        "name": "Opportunity Terrain Synthesis And Candidate Use-Case Shortlist",
        "purpose": "Convert executive terrain into candidate AI opportunities, hypotheses, dependencies, and disqualification criteria.",
        "question": "What are the 5-10 candidate use cases worth investigating, and what would disqualify each one before deeper discovery?",
        "inputs": "Step 0 scope, Step 1 terrain, org chart, opportunity zones, trust boundaries, vertical extension, and sponsor priorities.",
        "op_work": "Interpret terrain, choose candidates worth discovery, remove weak or sponsor-bias-only ideas, sequence discovery, and define disqualification criteria.",
        "ai_work": "Draft candidate use cases with target users, workflow boundaries, value hypotheses, truth dependencies, source dependencies, adoption dependencies, regulated-domain dependencies, confidence, and discovery plan.",
        "client_work": "Confirm whether the candidates are strategically relevant and whether the operating partner can access the right people. The client does not need to know where AI fits.",
        "output": "Candidate use-case shortlist, discovery-zone sequence, interview coverage matrix, and versioned disqualification criteria.",
        "gate": "Every active candidate has a target user, workflow boundary, value hypothesis, trust/adoption/regulatory dependencies, confidence, and disqualification route.",
        "feeds": "Step 3 interviews are targeted against these candidates. Steps 6, 12, and 16 re-affirm, narrow, or disqualify them.",
        "example": "Candidate use cases might include maintenance invoice review, lease abstract variance detection, delinquency escalation drafting, capex project status summarization, and board packet variance explanation.",
        "watchout": "Step 2 does not decide what to build. It decides what is worth learning about and what evidence could kill the idea.",
    },
    {
        "no": "3",
        "name": "Role-Aware AI-Led Interviews",
        "purpose": "Capture how work actually happens across role layers, with AI doing scalable neutral interviewing under clear protocol.",
        "question": "What do people actually do, decide, check, trust, adjust, escalate, and worry about in recent real work episodes?",
        "inputs": "Candidate shortlist, interview coverage matrix, role guide, AI interviewer system prompt, consent/recording/retention language, no-live-upload boundary, and intervention rules.",
        "op_work": "Select participants, monitor interview quality, intervene only when protocol or trust requires it, and protect the no-upload and no-asserted-facts boundaries.",
        "ai_work": "Ask adaptive questions without asserting facts about the organization; capture work episodes, decisions, edge cases, source access paths, truth production signals, tacit rules, approvals, adoption signals, and silent evidence needs.",
        "client_work": "Participants answer from real examples and explain how work happens. They do not upload artifacts during the interview.",
        "output": "Interview transcripts or summaries, work episodes, edge case register, source access register, silent evidence need log, participation-quality notes, and truth production signals.",
        "gate": "Coverage is sufficient to model the workflow or the gaps are clear enough to target more interviews or variation mapping.",
        "feeds": "Step 4 uses variation signals. Step 5 uses silent evidence needs to request targeted artifacts.",
        "example": "An assistant asset manager explains that the property management system shows invoice details, but the final review depends on a monthly Excel tracker and a director's memory of vendor exceptions.",
        "watchout": "The AI interviewer must never say, 'Your company uses X this way.' It can only ask and confirm what the participant says.",
    },
    {
        "no": "4",
        "name": "Variation Mapping",
        "purpose": "Handle fragmented operating models instead of forcing one fake canonical workflow.",
        "question": "Is there one workflow, or are there meaningful variants by region, portfolio, property type, seniority, system, franchise, contractor model, or local practice?",
        "inputs": "Interview variation signals, role coverage, org structure, candidate use cases, known portfolio differences, participation skew, and executive terrain.",
        "op_work": "Decide whether one canonical workflow is valid, whether variants need separate modeling, and whether participation skew is material.",
        "ai_work": "Enumerate variants, map where they were observed, describe de facto patterns, identify best-practice candidates, and flag variants with different truth, risk, or adoption implications.",
        "client_work": "Confirm whether variation is real, provide representative participants, and identify where a variant is mandatory versus local habit.",
        "output": "Variation map with variant IDs, variation dimensions, observed locations, separate-modeling flags, adoption implications, truth implications, and coverage gaps.",
        "gate": "No workflow proceeds as if canonical when material variation has not been mapped or explicitly ruled out.",
        "feeds": "Step 5 evidence follow-up and Step 6 workflow intelligence use the variants as first-class objects.",
        "example": "One region uses AppFolio reports, another uses Yardi exports, and a third runs a shared-drive workbook for maintenance exceptions. These become variants, not noise.",
        "watchout": "Saturation is the wrong goal in fragmented orgs. The goal is variation enumeration and explicit coverage confidence.",
    },
    {
        "no": "5",
        "name": "Planning-Evidence Follow-Up",
        "purpose": "Request the smallest approved evidence needed to validate important claims, source conflicts, access paths, edge cases, and truth production chains.",
        "question": "What targeted artifacts would let us confirm or challenge the most important parts of the model without asking for credentials or live system access?",
        "inputs": "Silent evidence need log, source access register, edge cases, variation map, disputed claims, fragile truth signals, and candidate dependencies.",
        "op_work": "Consolidate requests, remove nice-to-have asks, set SLA and escalation, define acceptable substitutes, and make the request owner-grouped and redaction-aware.",
        "ai_work": "Cluster duplicate evidence needs, connect each request to workflow objects, generate the follow-up request, and identify substitute options.",
        "client_work": "Provide approved redacted reports, screenshots, walkthroughs, formula or macro walkthroughs, sample exports, schema or field lists, vendor docs, or explain why unavailable.",
        "output": "Curated planning-evidence request, evidence log, artifact substitute decisions, redaction and retention rules, and unresolved evidence routes.",
        "gate": "Requests are specific, minimal, SLA-bound, sensitivity-aware, and do not request passwords, broad live access, all-email ingestion, or bulk unredacted data.",
        "feeds": "Step 6 uses evidence to build the initial workflow intelligence object and assign evidence references and confidence.",
        "example": "Instead of asking for full accounting access, request a redacted invoice packet, a screenshot of the approval screen, a sample export layout, and a walkthrough of the director's adjustment workbook.",
        "watchout": "Evidence follow-up often stalls. Use a 5-business-day default SLA, sponsor escalation, and substitute hierarchy.",
    },
    {
        "no": "6",
        "name": "AI-Native Workflow Intelligence Object",
        "purpose": "Turn discovery into a structured machine-readable model of the organization, not a slide deck or narrative report.",
        "question": "Can an AI system understand the workflow, roles, steps, decisions, information objects, systems, sources, truth production, approvals, variation, edge cases, evidence, and unknowns?",
        "inputs": "Steps 0-5, interviews, evidence, source access register, edge case register, variation map, candidate shortlist, and vertical extension.",
        "op_work": "Challenge realism, scope, confidence, missing roles, missing variants, missing truth profiles, and whether the object can support later decisioning.",
        "ai_work": "Build the structured workflow intelligence object with stable IDs for roles, people if allowed, teams, workflows, variants, steps, decisions, sources, systems, information objects, access profiles, truth profiles, approvals, edge cases, and evidence.",
        "client_work": "The client is not asked to review the entire object. They will later validate controlled slices.",
        "output": "AI-native workflow intelligence object, completeness flags, unresolved governance fields, unresolved truth fields, and downstream enrichment routes.",
        "gate": "Every material workflow, decision, source, information object, source access path, truth production profile, and edge case is either captured or explicitly routed as unknown.",
        "feeds": "Step 7 diagnoses the object. Step 8 validates and enriches controlled slices.",
        "example": "The invoice review workflow contains IDs for the maintenance invoice, work order, budget line, vendor contract, property manager note, approval gate, accounting system, Excel exception tracker, and director review decision.",
        "watchout": "Do not make a human-readable report the source of truth. The structured object is the source of truth; human views are projections.",
    },
    {
        "no": "7",
        "name": "Organizational Intelligence Diagnostic",
        "purpose": "Interpret the workflow object and classify what matters before more design work happens.",
        "question": "Which findings are symptoms, which are root causes, and which ones block, narrow, or reshape AI opportunity?",
        "inputs": "Step 6 workflow object, evidence confidence, source conflicts, truth profiles, variation map, adoption signals, risk signals, and candidate shortlist.",
        "op_work": "Judge materiality, classify blockers, decide whether candidates continue, pause, narrow, or disqualify, and avoid overreacting to weak evidence.",
        "ai_work": "Attach findings to workflow objects, separate symptoms from root-cause hypotheses, confidence-score findings, classify blockers, and route each finding.",
        "client_work": "Clarify disputed facts only when necessary and confirm whether findings align with known operating reality.",
        "output": "Object-linked organizational intelligence diagnostic with blocker classifications: fatal-for-use-case, requires-remediation-before-build, acceptable-with-controls, or informational.",
        "gate": "Fatal findings pause or disqualify affected candidates instead of silently drifting downstream.",
        "feeds": "Step 8 validation resolves material objects and loops back to Step 6 and Step 7 if corrections change the model.",
        "example": "If every asset manager computes repair variance differently, the diagnostic may classify recommendation support as requires-remediation-before-build while allowing summarization.",
        "watchout": "Do not treat all findings equally. A single truth or governance blocker can override high apparent business value.",
    },
    {
        "no": "8",
        "name": "Controlled Validation, Governance Resolution, And Baseline Release",
        "purpose": "Validate the most important parts of the model with the smallest authorized resolver groups and release Organizational Intelligence Baseline.",
        "question": "What is confirmed, corrected, disputed, blocked, or unknown, and what structured baseline can now power client product views and downstream steps?",
        "inputs": "Step 6 workflow object, Step 7 diagnostic, source inventory, source access profiles, truth production profiles, unresolved owner/access/sensitivity/retention/permission fields, and validation views.",
        "op_work": "Choose validators, route each unresolved question to the smallest authorized resolver group, protect sensitive internal model content, decide back-edges, and decide baseline release status.",
        "ai_work": "Prefill controlled views, generate validation prompts, update structured validation events, update source and truth profiles, produce the Organizational Intelligence Baseline payload, and identify downstream seeds.",
        "client_work": "Correct role-relevant slices and make binding decisions about owners, sources, access paths, truth chains, sensitive fields, retention, and permitted AI actions.",
        "output": "Validation events, updated source inventory, governance decisions, back-edge decisions, and Organizational Intelligence Baseline with graph nodes, graph edges, candidate AI portfolio, truth registry, validation state, product-view contract, and downstream payloads.",
        "gate": "Material corrections loop back to Step 6 object update and Step 7 diagnostic re-score before continuing.",
        "feeds": "Step 9 starts from a validated baseline instead of raw interview notes. Separate client-facing product views can also be generated from the baseline.",
        "example": "The VP validates hierarchy, accounting validates source constraints, IT validates system/access paths, and directors validate de facto truth production for invoice review. The full internal object is not broadcast.",
        "watchout": "Step 8 is not handing over all organizational intelligence. It releases controlled product-ready views and machine-readable downstream seeds.",
    },
    {
        "no": "9",
        "name": "AI Knowledge And Guideline Requirements Map",
        "purpose": "Identify what knowledge the future AI would need before it can reason safely.",
        "question": "What rules, examples, tacit judgments, regulated-domain obligations, adoption knowledge, truth-production rules, and escalation criteria need to exist?",
        "inputs": "Step 8 baseline, workflow decisions, edge cases, truth profiles, approval gates, source hierarchy signals, adoption signals, regulated-domain extension, and unresolved knowledge gaps.",
        "op_work": "Prioritize which knowledge matters, decide which gaps must be captured, and avoid asking experts to explain everything when only a few rules are material.",
        "ai_work": "Infer knowledge requirements from prior steps, link them to decisions and truth profiles, identify likely experts, classify where knowledge lives, and route gaps.",
        "client_work": "Confirm targeted high-value, high-risk, low-confidence, or fragile-truth knowledge ownership and availability.",
        "output": "Knowledge and guideline requirements map with requirement IDs, linked workflow objects, likely owners, evidence, confidence, examples needed, knowledge location, AI relevance, and next route.",
        "gate": "Every material AI behavior has required knowledge mapped or an explicit no-agent-use-yet gap.",
        "feeds": "Step 10 turns selected requirements into guidance and eval cases.",
        "example": "The AI needs rules for when an invoice can be summarized, when a variance is suspicious, what Fair Housing or resident-sensitive language must be avoided, and when an asset manager must escalate.",
        "watchout": "This is not the skill/guidance file yet. Step 9 says what guidance must exist; Step 10 writes it.",
    },
    {
        "no": "10",
        "name": "AI Guidance Pack",
        "purpose": "Codify prioritized AI reasoning rules in a platform-agnostic, machine-readable form.",
        "question": "What exact behavior, source hierarchy, rules, examples, forbidden actions, output contract, escalation triggers, and eval cases should a future AI follow?",
        "inputs": "Step 9 requirements, validated workflow objects, truth profiles, source hierarchy, regulated-domain requirements, examples, and subject-matter review.",
        "op_work": "Select which requirements deserve guidance, challenge vague rules, require examples, define acceptable confidence language, and ensure the guidance is implementation-grade.",
        "ai_work": "Draft canonical guidance spec, readable guide, behavioral evals, output-quality evals, regulated-domain evals, source-conflict cases, fragile-truth cases, and escalation cases.",
        "client_work": "Subject-matter owners validate rules, examples, review criteria, source hierarchy, forbidden behavior, escalation triggers, and update ownership.",
        "output": "Machine-readable AI guidance spec, readable guide view, test/eval cases, output contract, owners, validation status, and update cadence.",
        "gate": "Guidance is specific enough to become future prompts, policies, product controls, tool behavior, and eval suites, but no agent is deployed.",
        "feeds": "Step 11 uses guidance to define AI performance metrics. Step 15 uses it for control design. Step 16 uses it for readiness.",
        "example": "For invoice review, the guidance may require the AI to cite invoice amount, work order, budget line, approval status, and truth confidence, while forbidding payment approval or accounting write-back.",
        "watchout": "Do not make this Codex-specific. It is a canonical guidance spec with generated views for whatever implementation platform is later chosen.",
    },
    {
        "no": "11",
        "name": "Measurement Intelligence And AI-Capability Metric Design",
        "purpose": "Separate trusted measurement from fragile measurement, then design the future AI capability metrics before implementation.",
        "question": "Which existing metrics can be trusted, and how will the future AI capability be measured, monitored, killed, or expanded?",
        "inputs": "Step 8 baseline, truth profiles, reports, KPIs, dashboards, shadow trackers, Step 10 guidance, candidate use cases, and value hypotheses.",
        "op_work": "Decide which metrics matter, challenge fragile baselines, and define what evidence is acceptable for value and readiness.",
        "ai_work": "Classify metric trust and truth status, map formulas, owners, grains, refresh cadence, quality checks, AI-safe metric usage, and design AI success/drift/error/override/adoption/cost/kill metrics.",
        "client_work": "Confirm formulas, owners, quality checks, manual adjustments, freshness, permitted AI use, and whether metrics are disputed or fragile.",
        "output": "Measurement intelligence object, KPI dictionary, existing metric trust classification, AI-capability metric design, kill criteria, and unresolved metric routes.",
        "gate": "No value case uses fragile metrics as reliable baseline evidence unless the value case is explicitly about fixing measurement or truth infrastructure.",
        "feeds": "Step 12 uses trusted or conditional metrics for value. Step 16 uses AI metrics and kill criteria for readiness.",
        "example": "NOI variance may be disputed between finance and asset management; the future AI may flag and compare both but cannot use either as ground truth until reconciled.",
        "watchout": "This step includes both existing metrics and future AI metrics. Do not stop at current KPI cleanup.",
    },
    {
        "no": "12",
        "name": "Business Value Case And Portfolio Comparison",
        "purpose": "Decide which opportunities are worth advancing, fixing first, deprioritizing, or stopping.",
        "question": "Which candidate use cases have enough value, confidence, feasibility, adoption realism, and manageable risk to move forward?",
        "inputs": "Candidate shortlist, Step 8 baseline, guidance requirements, measurement intelligence, metric trust, volume/cost assumptions, risk signals, and sponsor priorities.",
        "op_work": "Judge credibility, compare opportunities, choose 1-N to advance, and prevent every interesting idea from moving into architecture.",
        "ai_work": "Draft value cases, AI-side cost model, dependency map, confidence ranges, sensitivity analysis, and portfolio comparison.",
        "client_work": "Confirm volumes, costs, priorities, budget/capacity, value preference, and whether selected opportunities fit leadership appetite.",
        "output": "Business value case, portfolio comparison, selected opportunities, deprioritized opportunities, remediation routes, and advancement rationale.",
        "gate": "Only the right 1-N opportunities move to solution shape. Weak, fragile, or low-value candidates are paused or routed.",
        "feeds": "Step 13 designs solution/adoption only for surviving opportunities.",
        "example": "The REIT may advance maintenance invoice review as a safe-limited assistant, pause autonomous capex approval, and route NOI reconciliation to measurement/truth remediation.",
        "watchout": "Model, tool-call, retrieval, observability, eval, support, and maintenance cost must be included. Do not treat AI as free.",
    },
    {
        "no": "13",
        "name": "Solution Shape And Adoption Design",
        "purpose": "Choose the future solution pattern and adoption path before writing the technical blueprint.",
        "question": "Should this be build, buy, leverage-vendor, hybrid, no-agent workflow, assistant, workflow-with-LLM-steps, tool-using agent, multi-agent system, or deferred?",
        "inputs": "Surviving opportunity, value/portfolio decision, Step 8 baseline, guidance, metrics, adoption signals, end-user realities, client stack, and vertical constraints.",
        "op_work": "Decide solution shape, agent topology, model class, UX surface, adoption realism, opt-in versus mandate limits, and rollout philosophy.",
        "ai_work": "Draft solution-shape options, adoption design, model-selection class, UX surface, retrieval/context pattern, eval/observability shape, training plan, feedback channels, and adoption-failure triggers.",
        "client_work": "Business owners and end-user owners confirm adoption feasibility, incentives, rollout, training, support model, and whether users can be mandated.",
        "output": "Solution shape decision and adoption design: build/buy/leverage path, topology, model class, UX surface, adoption plan, and failure triggers.",
        "gate": "No technical blueprint is written until the future solution shape and adoption path are explicit.",
        "feeds": "Step 14 turns the selected shape into technical/vendor blueprint details.",
        "example": "Instead of a standalone AI app, invoice review may be shaped as a draft-and-flag assistant embedded in the existing asset-management workflow, with manager approval before any system action.",
        "watchout": "Architecture follows adoption reality. A brilliant separate interface fails if users live in another system.",
    },
    {
        "no": "14",
        "name": "Technical/Vendor Implementation Blueprint",
        "purpose": "Document the future build plan in enough detail that an implementation team can execute later, without building anything now.",
        "question": "What systems, access paths, APIs, connectors, MCPs, normalization, identity resolution, truth remediation, runtime, hosting, tests, credentials, and build sequence would be needed after approval?",
        "inputs": "Step 13 solution shape, Step 8 baseline, systems/sources, source access profiles, truth profiles, guidance/eval packs, measurement needs, client IT/security constraints, vendor documentation, and evidence artifacts.",
        "op_work": "Ensure the blueprint is implementation-grade but still pre-build, identify blocked paths, and require enough specificity to avoid rediscovery later.",
        "ai_work": "Draft architecture, system/source table, future access request package, tool/MCP/connector contracts, normalization mappings, canonical entities, identity resolution, truth remediation, sandbox/test plan, secrets plan, audit/logging, hosting/environment, and build sequence.",
        "client_work": "IT, data, security, system owners, and vendor owners confirm feasibility as a plan: APIs, exports, permissions, sandboxes, audit logging, data quality, vendor limits, and approval process.",
        "output": "Technical/vendor blueprint with future access paths, fallback paths, blocked paths, component contracts, normalization plan, truth remediation plan, test strategy, credential/secrets plan, and build sequence.",
        "gate": "A future build team can understand what to build, what to request, what to avoid, and what must be remediated first, without needing live credentials during the engagement.",
        "feeds": "Step 15 controls attach to technical components. Step 16 readiness evaluates feasibility and dependencies.",
        "example": "The blueprint may specify Yardi read-only API if available, manual export fallback, document OCR for invoice packets, canonical vendor/property/work-order entities, and a future MCP contract that can only read approved fields.",
        "watchout": "This is where legacy systems and future access are planned. It is not where credentials are requested or connectors are built.",
    },
    {
        "no": "15",
        "name": "Risk And Control Model",
        "purpose": "Define the controls that would make the selected future AI behavior safe enough to test and operate.",
        "question": "What can the future AI see, say, calculate, recommend, draft, send, write, escalate, log, and stop, and who owns every risk?",
        "inputs": "Technical blueprint, guidance pack, measurement intelligence, truth profiles, sensitive fields, approval gates, future tool contracts, regulated-domain extension, access paths, and adoption design.",
        "op_work": "Judge materiality, require named owners, force regulatory risks to be explicit, and decide stop conditions.",
        "ai_work": "Draft data classification, risk register, zero-trust controls, tool permission matrix, output controls, approval gates, logging/monitoring, incident response, revocation, residual risk, and stop conditions.",
        "client_work": "Risk, security, legal, compliance, IT, system owners, and business owners confirm controls, owners, residual risks, and forbidden actions.",
        "output": "Risk/control model with named risks, controls, owners, tool permissions, output controls, logging, monitoring, incident response, revocation, and stop conditions.",
        "gate": "Risks are owned, controls are testable, and regulated-domain risks are named rather than hidden under generic compliance.",
        "feeds": "Step 16 readiness uses controls as hard gates and behavior-level limits.",
        "example": "For real estate, Fair Housing, TCPA, RESPA, MLS/IDX/VOW restrictions, state license rules, resident PII, vendor payment risk, and accounting write-back risk are explicit risk objects.",
        "watchout": "Do not make controls abstract. Each future tool and output type needs allowed actions, prohibited actions, approval rules, logs, and stop conditions.",
    },
    {
        "no": "16",
        "name": "AI-Agent Readiness Score",
        "purpose": "Convert the full evidence base into a behavior-specific readiness decision.",
        "question": "For each surviving opportunity, what behavior level is safe now, what is blocked, what must be fixed, and what path should Step 17 take?",
        "inputs": "Steps 0-15, especially value case, solution shape, technical blueprint, risk/control model, guidance pack, measurement intelligence, truth profiles, adoption design, and lifecycle assumptions.",
        "op_work": "Challenge AI scoring, interpret hard gates, choose minimum safe first behavior, and prevent score averages from hiding fatal blockers.",
        "ai_work": "Apply hard gates, score dimensions, map dependencies, identify blockers, classify behavior-level readiness, propose minimum safe first behavior, and recommend Step 17 path.",
        "client_work": "Confirm unresolved priority, owner, source, truth, adoption, feasibility, risk, and approval facts if needed.",
        "output": "Readiness object with hard gates, dimension scores, behavior-level readiness, dependency map, blockers, minimum safe first behavior, prohibited behaviors, and recommended Step 17 path.",
        "gate": "Readiness is behavior-specific. Read-only summary can pass while recommendation support, human-approved action, or autonomous action fails.",
        "feeds": "Step 17 turns the readiness decision into a decision packet.",
        "example": "The invoice assistant may be ready for summarize/compare/flag, conditional for draft recommendation with human review, and failed for approval or accounting write-back.",
        "watchout": "Truth production gate is hard. Fragile truth blocks non-safe behavior unless remediated or tightly controlled.",
    },
    {
        "no": "17",
        "name": "Implementation Decision Packet",
        "purpose": "Assemble the canonical machine-readable recommendation packet for build-ready, fix-first, or do-not-automate decisions.",
        "question": "What exactly should happen next, why, under what confidence, with what scope, owners, future access requests, controls, tests, and revision triggers?",
        "inputs": "Step 16 readiness object, Step 14 blueprint, Step 15 controls, Step 13 solution/adoption design, Step 12 value/portfolio decision, Step 11 metrics, Step 10 guidance, Step 8 baseline, and Step 6 workflow object.",
        "op_work": "Make the recommendation, narrow first-build or remediation scope, define confidence and revision triggers, and ensure audience views are consistent with the canonical packet.",
        "ai_work": "Assemble machine-readable packet, sponsor/business/technical/risk/remediation views, future access request package, component contracts, normalization and truth remediation plan, tests, controls, sequence, owner matrix, and stop boundary.",
        "client_work": "Sponsor and decision owners review the packet and decide whether to approve a separate implementation phase after Step 18.",
        "output": "Implementation decision packet: build-ready brief, gap-remediation plan, governance/data readiness plan, knowledge capture plan, technical feasibility plan, risk/control plan, or do-not-automate recommendation.",
        "gate": "The packet includes recommendation confidence, conditional-revision triggers, scope, owners, future access requests, controls, build sequence, and no-build boundary.",
        "feeds": "Step 18 defines the lifecycle/adoption-change operating contract for whatever path the packet recommends.",
        "example": "If truth is fragile, the packet may become a governance/data readiness plan instead of a build-ready brief. If safe-limited behavior is valuable, it can recommend a first build limited to summarization and uncertainty flagging.",
        "watchout": "Do not let a conditional pass become vague build approval. The packet must route unresolved blockers to named remediation paths.",
    },
    {
        "no": "18",
        "name": "Managed Lifecycle And Adoption-Change Object",
        "purpose": "Define how the future capability, remediation plan, or no-automation decision will be owned, governed, adopted, monitored, changed, paused, expanded, or retired.",
        "question": "If the client proceeds, who owns the future system, what proves it works, what changes it, what pauses it, what trains users, and what happens when truth, systems, or rules drift?",
        "inputs": "Step 17 packet, readiness object, risk/control model, technical blueprint, adoption design, guidance/evals, metrics, truth governance needs, and owner model.",
        "op_work": "Test whether ownership and cadence are realistic, define approval forum, and make adoption/change management explicit.",
        "ai_work": "Draft lifecycle object with stages, launch gates, validation, monitoring, truth governance, feedback/correction loops, adoption/change plan, access review, incidents, revocation, guidance/source/model updates, expansion, retirement, remediation cadence, and no-automation review cadence.",
        "client_work": "Confirm owners, approval forum, training, support, monitoring, incident expectations, adoption metrics, review cadence, and implementation authorization conditions.",
        "output": "Managed lifecycle/adoption-change object, remediation lifecycle, or no-automation review cadence with final approval status and implementation conditions.",
        "gate": "No implementation begins until Step 18 approval and separate build authorization exist.",
        "feeds": "After the engagement, a separate implementation phase may begin using the decision packet and lifecycle object.",
        "example": "The lifecycle defines who reviews invoice assistant outputs, what correction rate triggers pause, how source drift is checked, when the tracker is retired, and how training changes if asset managers do not adopt it.",
        "watchout": "Lifecycle is not just governance. It includes adoption, incentives, training, feedback, workflow sunsetting, and failure triggers.",
    },
]


TRUTH_STATUSES = [
    ("authoritative", "Official and de facto sources align, with owner, derivation, reproducibility, and auditability strong enough for the proposed AI behavior."),
    ("conditionally_reliable", "Usable with caveats, timing rules, human review, source hierarchy, or limited AI behavior."),
    ("shadow_derived", "Trusted output comes from a spreadsheet, tracker, shared-drive file, local report, email thread, or other unmanaged artifact."),
    ("manually_adjusted", "Final truth depends on manual edits, overrides, copy/paste, reconciliations, or judgment steps."),
    ("person_dependent", "A person or small group knows how to produce or interpret the truth, but the rule is not documented enough."),
    ("disputed", "Teams disagree about source, number, formula, owner, or valid decision use."),
    ("missing", "No credible source or production chain has been found."),
    ("not_reproducible", "The output cannot be recreated from known inputs, rules, and artifacts."),
]


KEY_OBJECTS = [
    ("candidate_use_case_shortlist", "Step 2", "Hypotheses about where AI may fit, with target users, workflow boundary, value hypothesis, dependencies, confidence, and disqualification criteria."),
    ("variation_map", "Step 4", "Workflow variants by region, portfolio, system, role seniority, local practice, contractor model, or other variation dimension."),
    ("source_access_profile", "Steps 3, 6, 8, 14", "Where information can practically be found, how it is accessed, which roles can access it, lookup keys, fields needed, and access failure modes."),
    ("truth_production_profile", "Steps 3-18", "Official source, de facto trusted source, production chain, manual adjustments, macros, expert memory, owner, reproducibility, auditability, and AI-safe usage."),
    ("workflow_intelligence_object", "Step 6", "Machine-readable graph of workflows, roles, people IDs if allowed, teams, steps, decisions, systems, sources, information objects, approvals, edge cases, evidence, and confidence."),
    ("organizational_intelligence_baseline", "Step 8", "Validated product-ready data substrate with graph nodes, graph edges, candidate portfolio, truth registry, validation state, product-view contract, and downstream seeds."),
    ("knowledge_requirements_map", "Step 9", "What knowledge, tacit rules, examples, regulated-domain obligations, adoption knowledge, and truth-production rules future AI needs."),
    ("ai_guidance_pack", "Step 10", "Machine-readable guidance spec, readable view, eval cases, source hierarchy, forbidden behaviors, escalation triggers, output contract, owners, and update cadence."),
    ("measurement_intelligence", "Step 11", "Metric trust classification, formulas, owners, grains, quality checks, AI-safe metric usage, AI success metrics, drift/error/override/adoption/cost metrics, and kill criteria."),
    ("solution_shape", "Step 13", "Build/buy/leverage path, topology, model class, UX surface, retrieval/context shape, eval/observability shape, and adoption design."),
    ("technical_blueprint", "Step 14", "Future architecture, access options, MCP/tool/connector contracts, normalization, identity resolution, truth remediation, hosting, testing, secrets, and build sequence."),
    ("risk_control_model", "Step 15", "Named risks, data classification, zero-trust controls, tool permissions, output controls, approval gates, monitoring, incidents, revocation, and stop conditions."),
    ("readiness_object", "Step 16", "Hard gates, dimension scores, behavior-level readiness, dependency map, blockers, minimum safe first behavior, and Step 17 path."),
    ("implementation_decision_packet", "Step 17", "Build-ready, fix-first, governance/data readiness, knowledge capture, technical feasibility, risk/control, or do-not-automate packet."),
    ("managed_lifecycle_object", "Step 18", "Future ownership, launch gates, validation, monitoring, truth governance, adoption/change, incidents, revocation, updates, expansion, retirement, and review cadence."),
]


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica-Bold", 7.6)
    canvas.setFillColor(COLORS["navy"])
    canvas.drawString(LEFT_MARGIN, PAGE_HEIGHT - 0.38 * inch, "AI Operating Partner Operator Guide")
    canvas.setFont("Helvetica", 7.4)
    canvas.setFillColor(COLORS["muted"])
    canvas.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, PAGE_HEIGHT - 0.38 * inch, f"Page {doc.page}")
    canvas.setStrokeColor(COLORS["line"])
    canvas.line(LEFT_MARGIN, PAGE_HEIGHT - 0.45 * inch, PAGE_WIDTH - RIGHT_MARGIN, PAGE_HEIGHT - 0.45 * inch)
    canvas.line(LEFT_MARGIN, 0.42 * inch, PAGE_WIDTH - RIGHT_MARGIN, 0.42 * inch)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(COLORS["muted"])
    canvas.drawString(LEFT_MARGIN, 0.27 * inch, "Pre-build organizational intelligence and implementation planning system")
    canvas.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, 0.27 * inch, "Confidential operator manual")
    canvas.restoreState()


def add_title(story, styles):
    story.append(Spacer(1, 0.58 * inch))
    story.append(para("AI Operating Partner", styles["title"]))
    story.append(para("Operator Guide: Step 0 To Step 18", styles["title"]))
    story.append(
        para(
            "A detailed explanation of what happens in every step, who does the work, what gets produced, how the artifacts connect, and why the process stays pre-build until final approval.",
            styles["subtitle"],
        )
    )
    story.append(HRFlowable(width="78%", color=COLORS["line"], thickness=1, spaceBefore=12, spaceAfter=18))
    story.append(
        callout(
            "Read this as the operating manual behind the framework. The goal is that after reading it, you can explain the logic of the whole engagement, know what each step produces, and understand how the system moves from vague AI opportunity to a precise build, fix-first, safe-limited, or do-not-automate decision.",
            styles,
        )
    )
    story.append(Spacer(1, 0.24 * inch))
    story.append(para("Core promise", styles["h2"]))
    story.append(
        para(
            "The process discovers where AI agents fit by first building structured organizational intelligence: how work happens, who does it, what decisions are made, which sources are trusted, how business truth is produced, what knowledge is tacit, where adoption will fail, what metrics can be believed, and what controls are needed.",
            styles["body"],
        )
    )
    story.append(para("Core boundary", styles["h2"]))
    story.append(
        para(
            "The engagement is pre-build. It does not build agents, MCPs, connectors, live integrations, normalization pipelines, email ingestion, write-back automation, or production tools. It can define exactly what those future builds need after Step 18 approval.",
            styles["body"],
        )
    )
    story.append(PageBreak())


def add_overview(story, styles):
    story.append(para("1. The Process In One Page", styles["h1"]))
    story.append(
        para(
            "The framework exists because most companies do not know what cannot be automated, what should not be automated, and where AI agents actually fit. The answer is rarely inside an executive's head. It is distributed across workflows, systems, reports, spreadsheets, tacit judgment, access constraints, incentives, regulatory rules, and the hidden ways the organization produces truth.",
            styles["body"],
        )
    )
    story.append(
        para(
            "The process therefore does not start by asking the client, 'What should we automate?' It starts by mapping strategic terrain, forming candidate hypotheses, interviewing the people closest to the work, discovering truth production, and converting the result into a machine-readable Organizational Intelligence Layer. Only then does it design AI behavior, measurement, architecture, controls, readiness, decision packet, and lifecycle.",
            styles["body"],
        )
    )
    story.append(para("The responsibility split", styles["h2"]))
    story.append(
        table(
            [
                ["Actor", "Owns"],
                ["Human operating partner", "Scope, trust, interpretation, prioritization, judgment, client relationship, recommendations, and when to stop, narrow, or route to remediation."],
                ["AI", "Interviewing, extraction, mapping, synthesis, completeness checks, draft artifacts, scoring, cross-checking, and turning unstructured discovery into structured objects."],
                ["Client", "Truth, examples, approval, system facts, ownership decisions, constraints, access feasibility, adoption reality, and final decisions."],
            ],
            styles,
            [1.65 * inch, 5.6 * inch],
        )
    )
    story.append(Spacer(1, 0.1 * inch))
    story.append(
        callout(
            "Important: The sponsor is not expected to know where AI can add value. The sponsor gives terrain and priorities. The operating partner and AI infer candidate opportunities from evidence.",
            styles,
            fill=COLORS["soft_amber"],
        )
    )
    story.append(para("Umbrella view", styles["h2"]))
    story.append(
        table(
            [["Umbrella", "Steps", "What It Means"]]
            + [[u["name"], u["steps"], u["meaning"]] for u in UMBRELLAS],
            styles,
            [2.0 * inch, 0.65 * inch, 4.6 * inch],
            header_color=COLORS["teal"],
        )
    )
    story.append(PageBreak())


def add_operating_model(story, styles):
    story.append(para("2. What The Organizational Intelligence Layer Means", styles["h1"]))
    story.append(
        para(
            "An Organizational Intelligence Layer is a structured, queryable model of how the organization operates. It is not a report, not a slide deck, and not just process documentation. It is a machine-readable representation of roles, workflows, decisions, sources, knowledge, metrics, risks, owners, truth production, adoption realities, and AI-fit boundaries.",
            styles["body"],
        )
    )
    story.append(para("The layer has three maturity states in this process", styles["h2"]))
    story.append(
        table(
            [
                ["State", "When", "Meaning"],
                ["Initial intelligence", "After Step 6", "The workflow graph exists with evidence, confidence, unknowns, and routes. Useful internally, but not yet fully validated."],
                ["Diagnostic intelligence", "After Step 7", "Object-linked findings and blocker classifications explain what matters and what might block AI."],
                ["Organizational Intelligence Baseline", "After Step 8", "Validated enough to power controlled client product views and downstream Steps 9-18."],
            ],
            styles,
            [1.55 * inch, 1.1 * inch, 4.6 * inch],
        )
    )
    story.append(para("What the baseline can power", styles["h2"]))
    story.append(
        bullets(
            [
                "Executive intelligence view: operating insights, candidate AI portfolio, major truth risks, major blockers, and safe versus unsafe AI patterns.",
                "Operating intelligence view: workflows, variants, handoffs, edge cases, hidden dependencies, owner gaps, and standardization opportunities.",
                "Data governance view: systems, sources, source access profiles, truth production profiles, sensitive fields, retention gaps, and steward gaps.",
                "AI-fit boundary view: safe-now behaviors, unsafe-now behaviors, fix-first routes, prohibited behaviors, and next recommended steps.",
            ],
            styles,
        )
    )
    story.append(
        callout(
            "This is why Step 8 can be a valuable client product moment. The client can receive intelligence they likely never had before, while the operating partner keeps the machine-readable substrate needed for the rest of the process.",
            styles,
        )
    )
    story.append(para("Key machine-readable objects", styles["h2"]))
    story.append(
        table(
            [["Object", "Primary Step", "What It Carries"]]
            + [[obj, step, meaning] for obj, step, meaning in KEY_OBJECTS],
            styles,
            [1.75 * inch, 0.9 * inch, 4.6 * inch],
            header_color=COLORS["navy"],
        )
    )
    story.append(PageBreak())


def add_truth_layer(story, styles):
    story.append(para("3. The Truth Production Layer", styles["h1"]))
    story.append(
        para(
            "The framework never assumes a clean source of truth. Many enterprises have official systems, but the number or decision people actually trust may come from an old workbook, a macro, a manual reconciliation, a finance analyst's report, a director's memory, or a board-packet adjustment. The framework treats those artifacts as intelligence assets, not embarrassing exceptions.",
            styles["body"],
        )
    )
    story.append(para("The four-way classification", styles["h2"]))
    story.append(
        table(
            [
                ["Element", "Meaning"],
                ["official_source", "What policy, system design, or leadership says is authoritative."],
                ["de_facto_source", "What people actually trust when work has to get done."],
                ["truth_production_chain", "The exports, formulas, macros, manual adjustments, reconciliations, judgment, and reporting steps that produce final truth."],
                ["truth_status", "The reliability class that determines what AI can safely do with that truth."],
            ],
            styles,
            [1.75 * inch, 5.5 * inch],
            header_color=COLORS["teal"],
        )
    )
    story.append(para("Truth status taxonomy", styles["h2"]))
    story.append(
        table(
            [["Status", "Meaning"]] + [[status, definition] for status, definition in TRUTH_STATUSES],
            styles,
            [1.65 * inch, 5.6 * inch],
            header_color=COLORS["teal"],
        )
    )
    story.append(
        callout(
            "Fragile truth rule: if material truth is shadow_derived, manually_adjusted, person_dependent, disputed, missing, or not_reproducible, non-safe AI behavior must fail or become conditional unless the behavior is limited to summarize, compare, flag uncertainty, draft clarification questions, or escalate.",
            styles,
            fill=COLORS["soft_amber"],
            border=COLORS["amber"],
        )
    )
    story.append(para("Where truth production is captured and used", styles["h2"]))
    story.append(
        table(
            [
                ["Steps", "Use"],
                ["3", "Interview prompts ask how final numbers, statuses, reports, and decisions are actually produced and trusted."],
                ["5", "Evidence follow-up may request redacted reports, formula walkthroughs, macro walkthroughs, sample exports, reconciliation notes, or screenshots."],
                ["6", "Workflow intelligence object stores truth_production_profiles linked to information objects, metrics, decisions, reports, and sources."],
                ["8", "Validation resolves official source, de facto source, owner, reproducibility, auditability, and permitted AI usage."],
                ["9-11", "Macros, manual adjustments, expert memory, and fragile metrics become knowledge and measurement requirements."],
                ["12-15", "Value, solution, technical blueprint, and controls account for truth remediation and fragile-truth limits."],
                ["16-18", "Truth production is a readiness gate, decision-packet routing rule, and lifecycle governance obligation."],
            ],
            styles,
            [0.85 * inch, 6.4 * inch],
        )
    )
    story.append(PageBreak())


def step_block(step, styles) -> KeepTogether:
    pieces = [
        para(f"Step {step['no']}: {step['name']}", styles["h2"]),
        para(step["purpose"], styles["body"]),
        table(
            [
                ["Question Answered", step["question"]],
                ["Inputs", step["inputs"]],
                ["Operating Partner Work", step["op_work"]],
                ["AI Work", step["ai_work"]],
                ["Client Work", step["client_work"]],
                ["Output", step["output"]],
                ["Gate", step["gate"]],
                ["Feeds Next", step["feeds"]],
                ["Practical Example", step["example"]],
                ["Watchout", step["watchout"]],
            ],
            styles,
            [1.55 * inch, 5.7 * inch],
            header_color=COLORS["teal"],
        ),
        Spacer(1, 0.08 * inch),
    ]
    return KeepTogether(pieces)


def add_steps(story, styles):
    story.append(para("4. Step-By-Step Operating Guide", styles["h1"]))
    story.append(
        para(
            "This section is the heart of the guide. For each step, the question answered and gate matter as much as the output. The gate tells you when the step is done and prevents the engagement from sliding into build work too early.",
            styles["body"],
        )
    )
    for step in STEPS:
        if step["no"] in {"6", "11", "16"}:
            story.append(PageBreak())
        story.append(step_block(step, styles))


def add_back_edges_and_data(story, styles):
    story.append(PageBreak())
    story.append(para("5. Iteration Loops, Data Access, And Implementation Boundary", styles["h1"]))
    story.append(
        para(
            "The sequence is linear enough to run, but it has explicit back-edges. Back-edges prevent false progress. If a validation, value, readiness, or technical finding changes the earlier model, the process updates the upstream object instead of pretending nothing changed.",
            styles["body"],
        )
    )
    story.append(para("Named back-edges", styles["h2"]))
    story.append(
        table(
            [
                ["Back-edge", "Trigger", "What Happens"],
                ["Step 8 to Step 6", "Validation materially corrects workflow, role, source, truth, or decision objects.", "Update the workflow intelligence object and evidence/confidence fields."],
                ["Step 8 to Step 7", "Validation changes blocker classification or diagnostic conclusion.", "Re-score the diagnostic and update candidate status."],
                ["Step 12 to Step 2", "Value/portfolio work deprioritizes or disqualifies candidates.", "Update the candidate shortlist and portfolio status."],
                ["Step 16 to Step 14", "Readiness exposes technical infeasibility or missing future component contract.", "Revise technical blueprint before decision packet."],
                ["Step 16 to Step 15", "Readiness exposes missing control, owner, approval, or stop condition.", "Revise risk/control model before decision packet."],
            ],
            styles,
            [1.35 * inch, 2.4 * inch, 3.5 * inch],
        )
    )
    story.append(para("Where legacy systems, access, MCPs, and normalization are handled", styles["h2"]))
    story.append(
        table(
            [
                ["Topic", "Captured During", "Planned During", "Not Done During Engagement"],
                ["Legacy systems", "Steps 3, 5, 6, 8", "Step 14", "No live integration or production system connection."],
                ["API, MCP, connector access", "Steps 3, 5, 8", "Steps 14, 17", "No token, credential, service account, MCP server, connector, or write-back build."],
                ["Email/document access", "Steps 3, 5, 8", "Step 14", "No all-email ingestion or broad mailbox access."],
                ["Normalization", "Steps 6, 8, 11", "Step 14", "No ETL, ELT, semantic layer, vector index, or normalization pipeline build."],
                ["Credentials/secrets", "Not collected", "Steps 14, 17, 18", "No employee credentials, broad production access, or unapproved secrets."],
            ],
            styles,
            [1.45 * inch, 1.45 * inch, 1.45 * inch, 2.9 * inch],
        )
    )
    story.append(
        callout(
            "By the end of Step 18, you should know exactly what future access, APIs, MCPs, connectors, data normalization, truth remediation, tests, controls, owners, and build sequence are required. The actual implementation still starts in a separate phase.",
            styles,
            fill=COLORS["soft_amber"],
        )
    )


def add_examples(story, styles):
    story.append(PageBreak())
    story.append(para("6. Practical Example: Multifamily REIT", styles["h1"]))
    story.append(
        para(
            "Assume a multifamily REIT wants to understand where AI can help asset management, property operations, maintenance, accounting, and portfolio reporting. The sponsor suspects manual work is high but does not know which agent should be built.",
            styles["body"],
        )
    )
    story.append(para("How the first eight steps create sticky value", styles["h2"]))
    story.append(
        table(
            [
                ["Steps", "What Happens", "Client-Visible Value"],
                ["0-2", "Scope the engagement, map executive terrain, and form hypotheses like invoice review, delinquency escalation, board packet variance explanation, leasing exception handling, and maintenance dispatch triage.", "The CEO sees a structured opportunity portfolio instead of a generic AI brainstorm."],
                ["3-5", "Interview VPs, directors, asset managers, assistant asset managers, property managers, accounting, and operations; map variants; request targeted evidence like redacted invoice packets and sample reports.", "The client sees that the process understands lived work without demanding broad data access."],
                ["6", "Build workflow intelligence for selected workflows, with IDs for roles, steps, decisions, sources, systems, truth profiles, and edge cases.", "The operating partner now has a machine-readable model of how the org works."],
                ["7", "Classify blockers such as disputed NOI, property manager system variation, undocumented invoice adjustment rules, or adoption resistance.", "Leadership sees which problems block AI versus which can be controlled."],
                ["8", "Validate key slices and release Organizational Intelligence Baseline with views for executives, operators, data governance, and AI fit boundaries.", "The client receives a new management asset: a structured view of work, truth, and AI fit they did not previously have."],
            ],
            styles,
            [0.65 * inch, 3.65 * inch, 2.95 * inch],
        )
    )
    story.append(para("A concrete candidate: maintenance invoice review", styles["h2"]))
    story.append(
        bullets(
            [
                "Safe now: summarize invoice packet, compare invoice to work order and budget line, flag missing approvals, flag conflicting amounts, draft clarification questions.",
                "Unsafe now: approve invoice, reject invoice, update accounting system, recommend payment if truth is disputed, or override property manager notes.",
                "Truth issue: the official source may be the accounting/property system, but the de facto trusted review may be a director's Excel exception tracker.",
                "Step 14 implication: recommendation support fails until the truth chain is documented, reproducible, controlled, or explicitly limited with human review.",
                "Step 17 implication: route to safe-limited build brief or governance/data readiness plan depending on value and controls.",
            ],
            styles,
        )
    )
    story.append(para("Interview approach for a layered asset-management team", styles["h2"]))
    story.append(
        para(
            "If the asset management team has a VP, 3 Directors, 6 Asset Managers, and 20 Assistant Asset Managers, do not interview all 30 by default. Interview the VP for terrain, the Directors for portfolio variation and authority, a stratified sample of Asset Managers by portfolio/property/system variation, and enough Assistant Asset Managers to capture execution details and edge cases. Expand only when variation, confidence, or risk requires it.",
            styles["body"],
        )
    )


def add_final_quality_bar(story, styles):
    story.append(PageBreak())
    story.append(para("7. What You Should Understand After Reading This", styles["h1"]))
    story.append(
        table(
            [
                ["You Should Be Able To Explain", "Short Answer"],
                ["Why the process starts with terrain, not automation ideas", "Executives supply strategic context; the system discovers AI fit from evidence."],
                ["What Step 2 decides", "Candidate use-case hypotheses, dependencies, and disqualification criteria, not final build decisions."],
                ["What exists by Step 8", "A validated Organizational Intelligence Baseline and product-view contract, plus downstream seeds for Steps 9-18."],
                ["Why truth production is central", "AI safety depends on how final business truth is actually produced, not what a system label says."],
                ["Where data access and MCPs are handled", "Planned in Steps 14, 17, and 18; not built or provisioned during the engagement."],
                ["Where normalization is handled", "Requirements are identified in Steps 6, 8, 11, and specified in Step 14; no pipeline is built during the engagement."],
                ["Why Step 13 exists", "Solution shape and adoption design are decisions that must precede technical blueprinting."],
                ["What Step 16 decides", "Behavior-level readiness: what is safe now, what is blocked, what must be fixed, and the Step 17 path."],
                ["What Step 18 adds", "The future operating contract for ownership, validation, monitoring, truth governance, adoption, incident response, expansion, and retirement."],
            ],
            styles,
            [2.3 * inch, 4.95 * inch],
            header_color=COLORS["teal"],
        )
    )
    story.append(Spacer(1, 0.1 * inch))
    story.append(
        callout(
            "Definition of done for the whole engagement: a future build team can understand scope, behavior, systems, source access, truth production, runtime pattern, hosting requirements, access requests, normalization, remediation, tests, controls, owners, sequence, adoption plan, lifecycle, and stop conditions without rediscovering the organization.",
            styles,
        )
    )


def add_appendix_machine_readable(story, styles):
    story.append(PageBreak())
    story.append(para("Appendix: Example Machine-Readable Baseline Fragment", styles["h1"]))
    story.append(
        para(
            "This fragment is illustrative. It shows the kind of logic the process is designed to produce by Step 8 and enrich through Steps 9-18.",
            styles["body"],
        )
    )
    lines = [
        "organizational_intelligence_baseline:",
        "  baseline_id: oib.multifamily_reit.asset_management.current",
        "  graph_nodes:",
        "    workflows:",
        "      - workflow_id: wf.maintenance_invoice_review",
        "        validation_status: partially_validated",
        "    information_objects:",
        "      - information_object_id: io.invoice_packet",
        "        source_access_profile_ids: [sap.accounting_invoice_view]",
        "        truth_production_profile_ids: [tp.invoice_review_truth]",
        "    truth_production_profiles:",
        "      - truth_profile_id: tp.invoice_review_truth",
        "        official_source: property_management_or_accounting_system",
        "        de_facto_trusted_source: director_excel_exception_tracker",
        "        truth_status: manually_adjusted",
        "        reproducibility: low",
        "        auditability: medium",
        "        ai_safe_usage:",
        "          allowed_uses: [summarize, compare_sources, flag_uncertainty]",
        "          prohibited_uses: [approve_invoice, reject_invoice, update_accounting]",
        "  candidate_ai_portfolio:",
        "    - candidate_use_case_id: uc.maintenance_invoice_review",
        "      status: alive_with_conditions",
        "      ai_fit_boundary:",
        "        safe_now: [summarize_packet, compare_amounts, flag_missing_approval]",
        "        fix_first: [document_adjustment_rules, assign_truth_owner]",
        "        prohibited: [autonomous_approval, accounting_write_back]",
    ]
    rows = [[code_para(line, styles["mono"])] for line in lines]
    t = Table(rows, colWidths=[CONTENT_WIDTH])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), COLORS["soft"]),
                ("BOX", (0, 0), (-1, -1), 0.45, COLORS["line"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    story.append(t)


def markdown() -> str:
    lines: list[str] = []
    lines.append("# AI Operating Partner Operator Guide: Step 0 To Step 18")
    lines.append("")
    lines.append("This is a detailed operator-facing explanation of the process. It is not a CEO overview. It explains what happens in every step, who does the work, what gets produced, and how the artifacts connect.")
    lines.append("")
    lines.append("## Core Promise")
    lines.append("")
    lines.append("The process discovers where AI agents fit by first building structured organizational intelligence: how work happens, who does it, what decisions are made, which sources are trusted, how business truth is produced, what knowledge is tacit, where adoption will fail, what metrics can be believed, and what controls are needed.")
    lines.append("")
    lines.append("## Core Boundary")
    lines.append("")
    lines.append("The engagement is pre-build. It does not build agents, MCPs, connectors, live integrations, normalization pipelines, email ingestion, write-back automation, or production tools. It defines what those future builds need after Step 18 approval.")
    lines.append("")
    lines.append("## Umbrella View")
    lines.append("")
    for u in UMBRELLAS:
        lines.append(f"- **{u['name']} (Steps {u['steps']}):** {u['meaning']}")
    lines.append("")
    lines.append("## Key Machine-Readable Objects")
    lines.append("")
    for obj, step, meaning in KEY_OBJECTS:
        lines.append(f"- `{obj}` ({step}): {meaning}")
    lines.append("")
    lines.append("## Truth Production Layer")
    lines.append("")
    lines.append("The framework never assumes a clean source of truth. It discovers official sources, de facto trusted sources, truth production chains, and truth status.")
    lines.append("")
    for status, definition in TRUTH_STATUSES:
        lines.append(f"- `{status}`: {definition}")
    lines.append("")
    lines.append("**Fragile truth rule:** if material truth is `shadow_derived`, `manually_adjusted`, `person_dependent`, `disputed`, `missing`, or `not_reproducible`, non-safe AI behavior must fail or become conditional unless the behavior is limited to summarize, compare, flag uncertainty, draft clarification questions, or escalate.")
    lines.append("")
    lines.append("## Step-By-Step Operating Guide")
    lines.append("")
    for step in STEPS:
        lines.append(f"### Step {step['no']}: {step['name']}")
        lines.append("")
        lines.append(f"**Purpose:** {step['purpose']}")
        lines.append("")
        lines.append(f"**Question answered:** {step['question']}")
        lines.append("")
        lines.append(f"**Inputs:** {step['inputs']}")
        lines.append("")
        lines.append(f"**Operating partner work:** {step['op_work']}")
        lines.append("")
        lines.append(f"**AI work:** {step['ai_work']}")
        lines.append("")
        lines.append(f"**Client work:** {step['client_work']}")
        lines.append("")
        lines.append(f"**Output:** {step['output']}")
        lines.append("")
        lines.append(f"**Gate:** {step['gate']}")
        lines.append("")
        lines.append(f"**Feeds next:** {step['feeds']}")
        lines.append("")
        lines.append(f"**Practical example:** {step['example']}")
        lines.append("")
        lines.append(f"**Watchout:** {step['watchout']}")
        lines.append("")
    lines.append("## Iteration Loops")
    lines.append("")
    lines.append("- Step 8 to Step 6: validation materially corrects workflow, role, source, truth, or decision objects.")
    lines.append("- Step 8 to Step 7: validation changes blocker classification or diagnostic conclusion.")
    lines.append("- Step 12 to Step 2: value/portfolio work deprioritizes or disqualifies candidates.")
    lines.append("- Step 16 to Step 14: readiness exposes technical infeasibility or missing future component contract.")
    lines.append("- Step 16 to Step 15: readiness exposes missing control, owner, approval, or stop condition.")
    lines.append("")
    lines.append("## Data Access, MCPs, Connectors, And Normalization")
    lines.append("")
    lines.append("Legacy systems, source access, APIs, MCPs, connectors, email/document scope, credentials, and normalization are planned inside the process but not built during the engagement. The future access and build package is specified in Steps 14, 17, and 18.")
    lines.append("")
    lines.append("## Multifamily REIT Example")
    lines.append("")
    lines.append("A multifamily REIT may start with vague terrain such as asset managers spending too much time reconciling property manager updates, invoice packets, board reporting, and accounting variances. By Step 8, the process can produce a validated baseline of workflows, variants, truth risks, candidate AI portfolio, and safe versus unsafe AI boundaries. For maintenance invoice review, safe-now behaviors may include summarizing invoice packets, comparing sources, flagging missing approvals, and drafting clarification questions. Unsafe behaviors may include invoice approval, rejection, accounting write-back, or reliance on disputed manually adjusted truth.")
    lines.append("")
    lines.append("## Definition Of Done")
    lines.append("")
    lines.append("A future build team can understand scope, behavior, systems, source access, truth production, runtime pattern, hosting requirements, access requests, normalization, remediation, tests, controls, owners, sequence, adoption plan, lifecycle, and stop conditions without rediscovering the organization.")
    lines.append("")
    return "\n".join(lines)


def build_markdown() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    MD_PATH.write_text(markdown(), encoding="utf-8")


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
        title="AI Operating Partner Operator Guide",
        author="AI Operating Partner System",
        subject="Detailed step-by-step guide to the AI Operating Partner process",
        creator="AI Operating Partner System",
    )
    story = []
    add_title(story, styles)
    add_overview(story, styles)
    add_operating_model(story, styles)
    add_truth_layer(story, styles)
    add_steps(story, styles)
    add_back_edges_and_data(story, styles)
    add_examples(story, styles)
    add_final_quality_bar(story, styles)
    add_appendix_machine_readable(story, styles)
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)


def render_previews() -> None:
    try:
        import fitz  # type: ignore
        from PIL import Image, ImageDraw  # type: ignore
    except Exception:
        return

    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(PDF_PATH))
    image_paths = []
    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=fitz.Matrix(1.35, 1.35), alpha=False)
        path = PREVIEW_DIR / f"page-{i:02d}.png"
        pix.save(str(path))
        image_paths.append(path)
    doc.close()

    thumbs = []
    for path in image_paths:
        img = Image.open(path).convert("RGB")
        img.thumbnail((190, 245))
        thumbs.append((path.name, img.copy()))
        img.close()
    if not thumbs:
        return
    cols = 4
    rows = (len(thumbs) + cols - 1) // cols
    sheet_w = cols * 220
    sheet_h = rows * 285
    sheet = Image.new("RGB", (sheet_w, sheet_h), "white")
    draw = ImageDraw.Draw(sheet)
    for idx, (name, img) in enumerate(thumbs):
        x = (idx % cols) * 220 + 15
        y = (idx // cols) * 285 + 22
        sheet.paste(img, (x, y))
        draw.text((x, y - 16), name, fill=(35, 56, 77))
    sheet.save(PREVIEW_DIR / "contact-sheet.png")


def main() -> None:
    build_markdown()
    build_pdf()
    render_previews()
    print(PDF_PATH)
    print(MD_PATH)
    print(PREVIEW_DIR)


if __name__ == "__main__":
    main()
