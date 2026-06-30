from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output" / "pdf"
PDF_PATH = OUT_DIR / "ai-operating-partner-ceo-overview.pdf"
MD_PATH = OUT_DIR / "ai-operating-partner-ceo-overview.md"
PREVIEW_DIR = OUT_DIR / "previews" / "ceo-process-overview"

PAGE_W, PAGE_H = LETTER
MARGIN = 54
TEXT_W = PAGE_W - (MARGIN * 2)

NAVY = colors.HexColor("#23384d")
INK = colors.HexColor("#202833")
MUTED = colors.HexColor("#5f6b76")
LINE = colors.HexColor("#d8dee5")
FILL = colors.HexColor("#f4f7f9")
ACCENT = colors.HexColor("#4f7f73")
GOLD = colors.HexColor("#b8924a")


def clean(text: str) -> str:
    return " ".join(text.strip().split())


def draw_wrapped(
    c: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    font: str = "Helvetica",
    size: int = 10,
    leading: int = 14,
    color=INK,
) -> float:
    c.setFont(font, size)
    c.setFillColor(color)
    max_chars = max(24, int(width / (size * 0.48)))
    for line in wrap(clean(text), width=max_chars):
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_bullets(c: canvas.Canvas, items: list[str], x: float, y: float, width: float, size: int = 9.5) -> float:
    for item in items:
        c.setFillColor(ACCENT)
        c.circle(x + 3, y + 4, 2, fill=1, stroke=0)
        y = draw_wrapped(c, item, x + 14, y, width - 14, size=size, leading=13)
        y -= 3
    return y


def header(c: canvas.Canvas, page_num: int, title: str) -> None:
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(MARGIN, PAGE_H - 34, "AI Operating Partner")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawRightString(PAGE_W - MARGIN, PAGE_H - 34, f"{title}  |  {page_num}/5")
    c.setStrokeColor(LINE)
    c.line(MARGIN, PAGE_H - 44, PAGE_W - MARGIN, PAGE_H - 44)


def footer(c: canvas.Canvas) -> None:
    c.setStrokeColor(LINE)
    c.line(MARGIN, 42, PAGE_W - MARGIN, 42)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 7.5)
    c.drawString(MARGIN, 28, "Confidential discussion material")
    c.drawRightString(PAGE_W - MARGIN, 28, "Pre-build organizational intelligence and AI implementation decision system")


def box(c: canvas.Canvas, x: float, y: float, w: float, h: float, fill=FILL, stroke=LINE) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.roundRect(x, y - h, w, h, 6, fill=1, stroke=1)


def section_title(c: canvas.Canvas, text: str, x: float, y: float, color=ACCENT) -> float:
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(x, y, text.upper())
    return y - 18


def page_one(c: canvas.Canvas) -> None:
    header(c, 1, "CEO overview")
    y = PAGE_H - 96
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 25)
    c.drawString(MARGIN, y, "How The AI Operating Partner")
    c.drawString(MARGIN, y - 31, "Process Works")
    y -= 78
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 12)
    c.drawString(MARGIN, y, "A five-page CEO overview of the operating system")
    y -= 42

    box(c, MARGIN, y, TEXT_W, 126, fill=colors.white)
    y2 = y - 22
    y2 = section_title(c, "Core idea", MARGIN + 20, y2)
    y2 = draw_wrapped(
        c,
        "Most companies do not know where AI agents fit because they do not yet have a structured model of how work, decisions, data, knowledge, ownership, and business truth actually operate. The process creates that model first, then decides what AI should or should not do.",
        MARGIN + 20,
        y2,
        TEXT_W - 40,
        size=10.5,
        leading=15,
    )

    y -= 158
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(MARGIN, y, "What this gives the CEO")
    y -= 22
    y = draw_bullets(
        c,
        [
            "A clear view of where the company has leverage, friction, hidden dependency, and AI opportunity.",
            "A machine-readable Organizational Intelligence Baseline by Step 8.",
            "A disciplined way to separate AI opportunities from data, governance, adoption, and truth-production problems.",
            "A final build, fix-first, or do-not-automate decision by Step 18, before credentials or live integrations are requested.",
        ],
        MARGIN,
        y,
        TEXT_W,
    )

    y -= 12
    box(c, MARGIN, y, TEXT_W, 92, fill=colors.HexColor("#f8f5ef"), stroke=colors.HexColor("#e1d7c2"))
    y2 = y - 20
    y2 = section_title(c, "CEO expectation", MARGIN + 20, y2, color=GOLD)
    draw_wrapped(
        c,
        "The CEO is not asked to know where AI fits. The CEO supplies strategic terrain, priorities, risk boundaries, and access to people who understand the work. The operating partner and AI system infer candidate opportunities from evidence.",
        MARGIN + 20,
        y2,
        TEXT_W - 40,
        size=10,
        leading=14,
    )
    footer(c)


def page_two(c: canvas.Canvas) -> None:
    header(c, 2, "Steps 0-8")
    y = PAGE_H - 82
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN, y, "Steps 0-8 Build The Organizational Intelligence Baseline")
    y -= 28
    y = draw_wrapped(
        c,
        "The first part of the process is not a technology-selection exercise. It is a structured way to learn how the company actually works and turn that reality into a machine-readable asset.",
        MARGIN,
        y,
        TEXT_W,
        size=10.5,
        leading=15,
    )
    y -= 18

    rows = [
        ("0-2", "Frame", "Set scope, map executive terrain, and create candidate use-case hypotheses with disqualification criteria."),
        ("3-5", "Discover", "Run AI-led interviews, map variation, and request only targeted planning evidence after interviews."),
        ("6", "Structure", "Build the initial workflow intelligence object: roles, steps, decisions, systems, sources, truth profiles, and unknowns."),
        ("7", "Diagnose", "Attach findings to objects and classify blockers as fatal, remediation-needed, acceptable-with-controls, or informational."),
        ("8", "Validate", "Resolve key source, truth, owner, access, sensitivity, and AI-action questions with the smallest authorized resolver group."),
    ]
    for step, label, desc in rows:
        box(c, MARGIN, y, TEXT_W, 74, fill=colors.white)
        c.setFillColor(ACCENT)
        c.setFont("Helvetica-Bold", 15)
        c.drawString(MARGIN + 18, y - 28, step)
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(MARGIN + 72, y - 24, label)
        draw_wrapped(c, desc, MARGIN + 72, y - 42, TEXT_W - 96, size=9.3, leading=12)
        y -= 86

    y -= 2
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN, y, "Important distinction")
    y -= 18
    draw_wrapped(
        c,
        "Step 2 decides what is worth investigating, not what will be built. Step 8 decides what has been learned and validated well enough to power the next decision steps.",
        MARGIN,
        y,
        TEXT_W,
        size=10,
        leading=14,
    )
    footer(c)


def page_three(c: canvas.Canvas) -> None:
    header(c, 3, "Step 8 baseline")
    y = PAGE_H - 82
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN, y, "What Exists By Step 8")
    y -= 26
    y = draw_wrapped(
        c,
        "By Step 8, the company has a structured Organizational Intelligence Baseline. This is the data substrate that your separate client-facing product can render into executive, operating, governance, and AI-fit views.",
        MARGIN,
        y,
        TEXT_W,
        size=10.5,
        leading=15,
    )
    y -= 16

    left_w = (TEXT_W - 16) / 2
    cards = [
        ("Organizational graph", "Roles, teams, workflows, variants, steps, handoffs, decisions, approvals, and edge cases."),
        ("Truth production registry", "Official sources, de facto trusted artifacts, spreadsheets, macros, manual adjustments, expert memory, disputes, reproducibility, and auditability."),
        ("Candidate AI portfolio", "Each candidate use case is alive, blocked, disqualified, or needs more discovery, with evidence and AI-fit boundaries."),
        ("Validation state", "What is validated, partially validated, disputed, unknown, blocked, or routed back to earlier steps."),
    ]
    for idx, (title, desc) in enumerate(cards):
        x = MARGIN + (idx % 2) * (left_w + 16)
        if idx % 2 == 0 and idx > 0:
            y -= 112
        box(c, x, y, left_w, 96, fill=colors.white)
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(x + 14, y - 23, title)
        draw_wrapped(c, desc, x + 14, y - 43, left_w - 28, size=9, leading=12)
    y -= 124

    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN, y, "Example of the machine-readable logic")
    y -= 18
    box(c, MARGIN, y, TEXT_W, 158, fill=colors.HexColor("#f7f9fb"))
    code = [
        "candidate_ai_portfolio:",
        "  maintenance_invoice_review:",
        "    status: alive_with_conditions",
        "    safe_now: [summarize, compare, flag_missing_approval]",
        "    unsafe_now: [approve_invoice, reject_invoice, update_accounting_system]",
        "    blocker: repair_expense_truth_is_manually_adjusted",
        "truth_production_profile:",
        "  official_source: Yardi",
        "  de_facto_source: asset_management_excel_tracker",
        "  truth_status: manually_adjusted",
    ]
    c.setFont("Courier", 8.4)
    c.setFillColor(INK)
    cy = y - 18
    for line in code:
        c.drawString(MARGIN + 18, cy, line)
        cy -= 12

    footer(c)


def page_four(c: canvas.Canvas) -> None:
    header(c, 4, "Steps 9-18")
    y = PAGE_H - 82
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN, y, "Steps 9-18 Convert Intelligence Into An Implementation Decision")
    y -= 29
    y = draw_wrapped(
        c,
        "The second part of the process uses the Step 8 baseline to decide what AI would need to know, how success would be measured, what solution shape is appropriate, what controls are required, and whether implementation should proceed.",
        MARGIN,
        y,
        TEXT_W,
        size=10.3,
        leading=15,
    )
    y -= 18

    rows = [
        ("9-10", "AI knowledge and guidance", "Identify required knowledge, then codify source hierarchy, rules, forbidden behavior, escalation, examples, and eval cases."),
        ("11-12", "Measurement and value", "Classify existing metrics, design AI success metrics, model value, include AI-side costs, and compare opportunities as a portfolio."),
        ("13-14", "Solution and blueprint", "Decide build/buy/leverage, topology, model class, UX surface, adoption design, then document future technical and vendor blueprint."),
        ("15-16", "Controls and readiness", "Define risk, regulated-domain controls, zero-trust permissions, and behavior-level readiness with hard gates."),
        ("17-18", "Decision and lifecycle", "Produce the machine-readable implementation decision packet and managed lifecycle/adoption-change object."),
    ]
    for step, label, desc in rows:
        box(c, MARGIN, y, TEXT_W, 66, fill=colors.white)
        c.setFillColor(GOLD)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(MARGIN + 16, y - 25, step)
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(MARGIN + 76, y - 22, label)
        draw_wrapped(c, desc, MARGIN + 76, y - 39, TEXT_W - 94, size=9, leading=12)
        y -= 77

    y -= 4
    box(c, MARGIN, y, TEXT_W, 88, fill=colors.HexColor("#f8f5ef"), stroke=colors.HexColor("#e1d7c2"))
    y2 = y - 20
    y2 = section_title(c, "Pre-build boundary", MARGIN + 20, y2, color=GOLD)
    draw_wrapped(
        c,
        "The engagement does not request credentials, build MCPs or connectors, normalize live data, ingest emails, or deploy agents. It defines what would be needed later, after approval.",
        MARGIN + 20,
        y2,
        TEXT_W - 40,
        size=9.7,
        leading=13,
    )
    footer(c)


def page_five(c: canvas.Canvas) -> None:
    header(c, 5, "CEO role")
    y = PAGE_H - 82
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN, y, "What The CEO Needs To Know")
    y -= 28
    y = draw_wrapped(
        c,
        "This process is designed so the CEO can sponsor AI strategy without guessing which agents to build. The system turns strategic priorities and organizational reality into evidence-backed implementation decisions.",
        MARGIN,
        y,
        TEXT_W,
        size=10.5,
        leading=15,
    )
    y -= 18

    cols = [
        ("CEO supplies", ["Strategic priorities", "Risk boundaries", "Executive sponsorship", "Access to the right operators and owners"]),
        ("CEO receives", ["Organizational Intelligence Baseline", "AI opportunity portfolio", "Build/fix/do-not-automate decision", "Lifecycle and governance plan"]),
    ]
    col_w = (TEXT_W - 18) / 2
    start_y = y
    for i, (title, items) in enumerate(cols):
        x = MARGIN + i * (col_w + 18)
        box(c, x, start_y, col_w, 146, fill=colors.white)
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(x + 15, start_y - 24, title)
        draw_bullets(c, items, x + 15, start_y - 47, col_w - 30, size=9)
    y -= 174

    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN, y, "The final decision categories")
    y -= 19
    y = draw_bullets(
        c,
        [
            "Build-ready: the behavior is valuable, governable, measurable, adoptable, and technically feasible.",
            "Fix-then-build: the opportunity is real, but truth, data, knowledge, controls, adoption, or technical feasibility must be fixed first.",
            "Safe-limited: AI may summarize, compare, flag uncertainty, draft questions, or escalate, but cannot recommend, decide, send, or write.",
            "Do not automate: risk, value, ownership, adoption, or truth conditions make automation inappropriate.",
        ],
        MARGIN,
        y,
        TEXT_W,
    )

    y -= 12
    box(c, MARGIN, y, TEXT_W, 92, fill=colors.HexColor("#eef5f2"), stroke=colors.HexColor("#cfe0d8"))
    y2 = y - 20
    y2 = section_title(c, "Executive takeaway", MARGIN + 20, y2, color=ACCENT)
    draw_wrapped(
        c,
        "The process does not sell an AI agent first. It builds the organizational intelligence layer that tells the company which agents should exist, what they need to know, what they can safely do, and what must be fixed before implementation.",
        MARGIN + 20,
        y2,
        TEXT_W - 40,
        size=10,
        leading=14,
    )
    footer(c)


def write_markdown() -> None:
    text = """# How The AI Operating Partner Process Works

Prepared for: CEO / Executive Sponsor

## Page 1 - Executive Overview

Most companies do not know where AI agents fit because they do not yet have a structured model of how work, decisions, data, knowledge, ownership, and business truth actually operate. The process creates that model first, then decides what AI should or should not do.

The CEO is not asked to know where AI fits. The CEO supplies strategic terrain, priorities, risk boundaries, and access to people who understand the work.

## Page 2 - Steps 0-8

Steps 0-8 build the Organizational Intelligence Baseline. They frame the engagement, discover lived work, map variation, request targeted planning evidence, structure the workflow intelligence object, diagnose blockers, and validate source/truth/owner/access decisions.

## Page 3 - What Exists By Step 8

By Step 8, the company has a machine-readable baseline: organizational graph, truth production registry, candidate AI portfolio, AI-fit boundaries, validation state, product-view contract, and downstream seeds for Steps 9-18.

## Page 4 - Steps 9-18

Steps 9-18 convert the baseline into an implementation decision. They define AI knowledge, guidance, evals, measurement, value, portfolio priority, solution shape, adoption design, technical blueprint, risk controls, readiness, decision packet, and lifecycle.

## Page 5 - CEO Role

The CEO sponsors the terrain, risk boundaries, and decision authority. The CEO receives a clear build, fix-first, safe-limited, do-not-automate, or no-action recommendation. Implementation starts only after Step 18 approval and a separate build phase.
"""
    MD_PATH.write_text(text, encoding="utf-8")


def build_pdf() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(PDF_PATH), pagesize=LETTER)
    c.setTitle("AI Operating Partner CEO Overview")
    c.setAuthor("AI Operating Partner System")
    c.setCreator("AI Operating Partner System")
    c.setSubject("CEO overview of the AI Operating Partner process")
    for page in [page_one, page_two, page_three, page_four, page_five]:
        page(c)
        c.showPage()
    c.save()


def render_previews() -> None:
    try:
        import fitz  # type: ignore
    except Exception:
        return
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(PDF_PATH))
    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
        pix.save(str(PREVIEW_DIR / f"page-{i}.png"))
    doc.close()


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_markdown()
    build_pdf()
    render_previews()
    print(PDF_PATH)
    print(MD_PATH)
    print(PREVIEW_DIR)


if __name__ == "__main__":
    main()
