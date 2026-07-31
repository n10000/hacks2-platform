from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageBreak, PageTemplate, Paragraph, Spacer,
    Table, TableStyle, KeepTogether,
)

OUTPUT = "private/AI-Business-Operations-Pack-Hacks2.pdf"
INK = colors.HexColor("#11120e")
PAPER = colors.HexColor("#f1f0e7")
ACID = colors.HexColor("#d7ff36")
CYAN = colors.HexColor("#79e8f4")
MUTED = colors.HexColor("#a5a69d")


def p(text, style):
    return Paragraph(text, style)


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(INK)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.setStrokeColor(colors.Color(1, 1, 1, alpha=.17))
    canvas.line(18 * mm, 14 * mm, A4[0] - 18 * mm, 14 * mm)
    canvas.setFillColor(MUTED)
    canvas.setFont("H2SansBold", 7)
    canvas.drawString(18 * mm, 8 * mm, "HACKS2 / APPLIED AI")
    canvas.drawRightString(A4[0] - 18 * mm, 8 * mm, f"{doc.page:02d}")
    canvas.restoreState()


def build():
    pdfmetrics.registerFont(TTFont("H2Sans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("H2SansBold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("H2Mono", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"))
    doc = BaseDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=20 * mm,
        bottomMargin=22 * mm,
        title="AI Business Operations Pack - Hacks2",
        author="Hacks2",
        subject="Practical AI workflows, prompts and templates for small-business operations",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="H2", frames=[frame], onPage=on_page)])

    styles = getSampleStyleSheet()
    title = ParagraphStyle("Title", parent=styles["Normal"], fontName="H2SansBold", fontSize=33, leading=29, textColor=PAPER, alignment=TA_LEFT, spaceAfter=12)
    display = ParagraphStyle("Display", parent=styles["Normal"], fontName="H2SansBold", fontSize=24, leading=23, textColor=PAPER, alignment=TA_LEFT, spaceAfter=16)
    h2 = ParagraphStyle("H2", parent=styles["Normal"], fontName="H2SansBold", fontSize=16, leading=19, textColor=ACID, alignment=TA_LEFT, spaceBefore=12, spaceAfter=10)
    h3 = ParagraphStyle("H3", parent=styles["Normal"], fontName="H2SansBold", fontSize=10, leading=13, textColor=CYAN, alignment=TA_LEFT, spaceBefore=10, spaceAfter=5)
    body = ParagraphStyle("Body", parent=styles["Normal"], fontName="H2Sans", fontSize=9.4, leading=14, textColor=PAPER, alignment=TA_LEFT, spaceAfter=8)
    small = ParagraphStyle("Small", parent=body, fontSize=7.7, leading=10, textColor=MUTED)
    kicker = ParagraphStyle("Kicker", parent=body, fontName="H2SansBold", fontSize=7.8, leading=10, textColor=ACID, spaceAfter=12)
    prompt = ParagraphStyle("Prompt", parent=body, fontName="H2Mono", fontSize=8.1, leading=12, textColor=INK, backColor=colors.HexColor("#dfe8d4"), borderColor=ACID, borderWidth=.5, borderPadding=9, spaceBefore=7, spaceAfter=12)

    story = []
    story += [Spacer(1, 31 * mm), p("H2 / PAID FIELD GUIDE", kicker), p("AI BUSINESS<br/>OPERATIONS<br/><font color='#d7ff36'>PACK.</font>", title), p("Six repeatable systems, prompts and templates for turning useful AI experiments into calmer day-to-day operations.", ParagraphStyle("Lead", parent=body, fontSize=13, leading=19, textColor=PAPER)), Spacer(1, 20 * mm), p("For founders, operators and small teams. Built to be used on live work - not admired as theory.", small), PageBreak()]

    story += [p("START HERE", kicker), p("MAKE AI USEFUL - WITHOUT TURNING YOUR BUSINESS INTO A TOOL EXPERIMENT.", display), p("This pack is for work that repeats: incoming leads, discovery and onboarding, meeting follow-up, SOPs, support patterns and the short weekly review that keeps the useful improvements alive.", body), p("Use one system at a time. Put a human check wherever an output could affect a customer, a payment, a contract or a public claim.", body), p("The operating rule", h2), p("A workflow is useful only when it has a named owner, a clear input, a visible definition of a good output and a way to check whether it saved time without lowering quality.", body), p("Inside", h2)]
    contents = [
        ("01", "Workflow map", "Choose work that is worth improving before you automate it."),
        ("02", "Lead qualification", "Turn uneven enquiries into a reviewable next-action brief."),
        ("03", "Client onboarding", "Create a clear project start without inventing scope or commitments."),
        ("04", "Meeting to action", "Make notes useful while the context is still fresh."),
        ("05", "SOP builder", "Capture repeatable work so it does not live in one person’s head."),
        ("06", "Weekly operations review", "Keep the patterns that work and stop the ones that do not."),
    ]
    table = Table([[p(f"<font color='#d7ff36'>{n}</font>", h3), p(f"<b>{t}</b><br/><font color='#a5a69d'>{d}</font>", body)] for n,t,d in contents], colWidths=[20*mm, 145*mm])
    table.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"), ("LINEBELOW", (0,0), (-1,-1), .35, colors.Color(1,1,1,.2)), ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7)]))
    story += [table, PageBreak()]

    systems = [
        ("01 / WORKFLOW MAP", "Choose the right task first", "Start with a task that happens at least weekly, has recognisable inputs and produces a result someone can judge. Do not begin with a process that is changing every day or one where no one owns the final decision.", "For this task, define: (1) the trigger, (2) the exact inputs, (3) the useful output, (4) the person who reviews it, (5) the current time spent each month, and (6) the risk if the output is wrong. Return a compact workflow map. Do not invent missing facts."),
        ("02 / LEAD QUALIFICATION", "Make the first pass faster, not automatic", "AI can reduce the friction of reading a mixed-quality enquiry. It should extract and organise; a person should decide priority, price, promises and the reply that goes out under your name.", "Read this customer enquiry. Create: (1) likely goal, (2) confirmed requirements, (3) missing information, (4) urgency signals, (5) a suggested next action, and (6) a short response draft. Do not invent prices, deadlines, capabilities or commitments. Label uncertainty clearly."),
        ("03 / CLIENT ONBOARDING", "Create a visible project start", "A good onboarding pack separates what is agreed from what is assumed. Use the proposal, discovery notes and client messages as source material; preserve the original records beside the summary.", "Using the supplied proposal, discovery notes and emails, create an internal onboarding brief with: confirmed goals, agreed deliverables, explicit dates, responsibilities, required access, source links and unanswered questions. Do not infer scope, pricing, approvals or dates. Mark every uncertainty."),
        ("04 / MEETING TO ACTION", "Turn conversations into owned next moves", "Meeting summaries fail when they are merely shorter transcripts. The useful result is a small list of decisions, actions, owners and deadlines that participants can correct quickly.", "Turn these meeting notes into: (1) decisions made, (2) action items with owner and due date only where explicitly stated, (3) open questions, (4) risks or dependencies, and (5) a concise follow-up email. Do not assign ownership, dates or commitments that were not stated."),
        ("05 / SOP BUILDER", "Document the version that survived real work", "Do not write an SOP for an imaginary perfect process. Observe a process after several real runs, then make its inputs, decisions, hand-offs and quality checks visible.", "Draft a practical SOP from this process description. Include: purpose, trigger, inputs, step-by-step actions, decision points, exceptions, final quality check, owner and links to source materials. Flag missing details as questions instead of filling gaps."),
        ("06 / WEEKLY REVIEW", "Improve one thing and stop the noise", "A weekly review turns isolated experiments into an operating loop. Keep it short: look at one workflow, compare with the old way of working and decide the next smallest change.", "Review this week’s workflow evidence. Return: (1) what saved time or improved quality, (2) what introduced risk or friction, (3) one change to test next week, (4) what to stop doing, and (5) the single metric to record. Be specific and avoid generic recommendations."),
    ]
    for index, (label, heading, copy, prompt_text) in enumerate(systems):
        story += [p(label, kicker), p(heading.upper(), display), p(copy, body), p("Copy-ready prompt", h3), p(prompt_text, prompt), p("Implementation check", h3), p("Before using the output: compare it with the original input, confirm any customer-facing claims, and keep a named owner for the final decision.", body)]
        if index < len(systems) - 1: story += [PageBreak()]

    story += [PageBreak(), p("TEMPLATES", kicker), p("SIX SMALL<br/>TEMPLATES FOR<br/><font color='#d7ff36'>REAL WORK.</font>", display)]
    templates = [
        ("Workflow baseline", "Task | Trigger | Input | Useful output | Owner | Human check | Monthly time | Quality signal"),
        ("Lead review", "Source | Goal | Fit | Missing information | Priority | Next action | Draft reply | Reviewer"),
        ("Onboarding brief", "Client | Goals | Deliverables | Dates | Access needed | People | Risks | Open questions"),
        ("Action register", "Action | Owner | Due date | Dependency | Status | Source / context"),
        ("SOP checklist", "Purpose | Trigger | Steps | Decision points | Exceptions | Quality check | Owner | Last reviewed"),
        ("Weekly review", "Workflow | Evidence | Time saved | Quality change | Friction | Next test | Metric | Owner"),
    ]
    for title_text, fields in templates:
        story += [KeepTogether([p(title_text, h3), p(fields, prompt)])]
    story += [PageBreak(), p("30-MINUTE IMPLEMENTATION", kicker), p("PICK ONE TASK.<br/>MAKE ONE CHANGE.<br/><font color='#79e8f4'>MEASURE THE RESULT.</font>", display), p("Minutes 0-5: choose the repeated task and write its baseline. Minutes 5-15: run the relevant prompt on a real, bounded example. Minutes 15-25: compare the AI-assisted output with the old version. Minutes 25-30: keep one improvement, name the owner and choose the metric for next week.", body), p("Do not build an automation merely because a tool can connect two systems. Build only when the payoff is meaningful and someone owns maintenance.", body), Spacer(1, 12*mm), p("HACKS2 / APPLIED AI", kicker), p("Useful systems over noisy tool stacks.", h2)]
    doc.build(story)


if __name__ == "__main__":
    build()
