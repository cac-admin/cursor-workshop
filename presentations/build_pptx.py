"""
Build the CAC Cursor workshop PowerPoint deck from student-facing slide content.
Output: presentations/cursor-cac-workshop.pptx

Source of truth for wording: presentations/cursor-cac-workshop.html
"""
from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Emu, Inches, Pt

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
OUT = HERE / "cursor-cac-workshop.pptx"

NAVY = RGBColor(0x00, 0x24, 0x52)
GOLD = RGBColor(0xFA, 0xBD, 0x0F)
RED = RGBColor(0xB9, 0x0E, 0x31)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PAPER = RGBColor(0xF7, 0xF5, 0xF0)
INK = RGBColor(0x0C, 0x1A, 0x2E)
MUTED = RGBColor(0x5A, 0x6A, 0x7E)
SOFT = RGBColor(0xB8, 0xC4, 0xD4)
PROMPT_BG = RGBColor(0xE8, 0xEE, 0xF6)

AUTHOR = (
    "Shadi Khalifa, PhD <khalifa.s@queensu.ca>, "
    "Centre for Advanced Computing, Queen's University"
)
FOOTER_TEXT = "CAC | Queen's University | cac.queensu.ca | Shadi Khalifa, PhD"

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
BAR_H = Inches(0.10)
FOOTER_H = Inches(0.38)
MARGIN = Inches(0.55)


def _set_run(run, size_pt, bold=False, color=INK, font_name="Calibri"):
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font_name


def _fill_solid(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def _add_rect(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    _fill_solid(shape, color)
    return shape


def _tricolour_bar(slide, top=0):
    third = int(SLIDE_W) // 3
    _add_rect(slide, 0, top, third, BAR_H, NAVY)
    _add_rect(slide, third, top, third, BAR_H, GOLD)
    _add_rect(slide, third * 2, top, int(SLIDE_W) - third * 2, BAR_H, RED)


def _footer(slide, light=True):
    color = MUTED if light else RGBColor(0xA8, 0xB8, 0xC8)
    box = slide.shapes.add_textbox(
        MARGIN, SLIDE_H - FOOTER_H, SLIDE_W - MARGIN * 2, FOOTER_H
    )
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    run = p.add_run()
    run.text = FOOTER_TEXT
    _set_run(run, 10, False, color)


def _bg(slide, color):
    _add_rect(slide, 0, 0, SLIDE_W, SLIDE_H, color)


def _textbox(
    slide,
    left,
    top,
    width,
    height,
    text,
    size=18,
    bold=False,
    color=INK,
    align=PP_ALIGN.LEFT,
):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    _set_run(run, size, bold, color)
    return box


def _bullets(slide, left, top, width, height, items, size=16, color=INK, space_after=8):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(space_after)
        run = p.add_run()
        run.text = "-  " + item
        _set_run(run, size, False, color)
    return box


def _maybe_picture(slide, image_name, left, top, width):
    img = ASSETS / image_name
    if img.exists():
        slide.shapes.add_picture(str(img), left, top, width=width)
        return True
    return False


def _content_chrome(slide):
    _bg(slide, PAPER)
    _tricolour_bar(slide, 0)
    _add_rect(slide, 0, BAR_H, Inches(0.07), SLIDE_H - BAR_H - FOOTER_H, NAVY)


def _kicker_title(slide, kicker, title, title_size=26):
    y = Inches(0.28)
    if kicker:
        _textbox(slide, MARGIN, y, Inches(12.2), Inches(0.32),
                 kicker, size=12, bold=True, color=RED)
        y = Inches(0.55)
    _textbox(slide, MARGIN, y, Inches(12.2), Inches(0.7),
             title, size=title_size, bold=True, color=NAVY)
    return Inches(1.25) if kicker else Inches(1.05)


def title_slide(prs, title, lede="", meta=None, image_name=None):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _bg(slide, NAVY)
    _tricolour_bar(slide, 0)
    _tricolour_bar(slide, SLIDE_H - BAR_H)
    _textbox(
        slide, Inches(0.7), Inches(0.55), Inches(12.0), Inches(0.4),
        "Queen's University  |  Centre for Advanced Computing",
        size=14, bold=True, color=GOLD, align=PP_ALIGN.LEFT,
    )
    _textbox(
        slide, Inches(0.7), Inches(1.7), Inches(12.0), Inches(1.5),
        title, size=36, bold=True, color=WHITE, align=PP_ALIGN.LEFT,
    )
    if lede:
        _textbox(
            slide, Inches(0.7), Inches(3.4), Inches(11.5), Inches(1.2),
            lede, size=16, bold=False, color=SOFT, align=PP_ALIGN.LEFT,
        )
    _textbox(
        slide, Inches(0.7), Inches(4.8), Inches(11.5), Inches(0.9),
        AUTHOR, size=14, bold=False, color=GOLD, align=PP_ALIGN.LEFT,
    )
    if meta:
        _textbox(
            slide, Inches(0.7), Inches(5.8), Inches(11.5), Inches(0.5),
            "  |  ".join(meta), size=12, bold=False, color=SOFT, align=PP_ALIGN.LEFT,
        )
    if image_name:
        _maybe_picture(slide, image_name, Inches(9.8), Inches(5.55), Inches(2.9))
    _footer(slide, light=False)
    return slide


def section_slide(prs, uc_code, title, blurb=""):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _bg(slide, NAVY)
    _tricolour_bar(slide, 0)
    _tricolour_bar(slide, SLIDE_H - BAR_H)
    _textbox(
        slide, Inches(0.8), Inches(2.0), Inches(11.5), Inches(0.45),
        uc_code, size=18, bold=True, color=GOLD,
    )
    full_title = f"{uc_code} {title}" if not title.startswith(uc_code) else title
    _textbox(
        slide, Inches(0.8), Inches(2.55), Inches(11.5), Inches(1.8),
        full_title, size=30, bold=True, color=WHITE,
    )
    if blurb:
        _textbox(
            slide, Inches(0.8), Inches(4.6), Inches(11.5), Inches(1.2),
            blurb, size=16, bold=False, color=SOFT,
        )
    _footer(slide, light=False)
    return slide


def content_slide(
    prs,
    title,
    bullets=None,
    body="",
    kicker="",
    image_name=None,
    note="",
    bullet_size=15,
):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _content_chrome(slide)
    y = _kicker_title(slide, kicker, title)
    text_width = Inches(7.2) if image_name else Inches(12.1)
    if body:
        body_h = Inches(1.35) if bullets else Inches(4.5)
        _textbox(slide, MARGIN, y, text_width, body_h, body, size=15, color=INK)
        y = Emu(int(y) + int(body_h) + int(Inches(0.1)))
    if bullets:
        remaining = SLIDE_H - FOOTER_H - y - Inches(0.15)
        if note:
            remaining -= Inches(0.35)
        _bullets(slide, MARGIN, y, text_width, remaining, bullets, size=bullet_size)
    if image_name:
        _maybe_picture(slide, image_name, Inches(8.15), Inches(1.35), Inches(4.6))
    if note:
        _textbox(
            slide, MARGIN, SLIDE_H - FOOTER_H - Inches(0.4),
            Inches(12.1), Inches(0.35), note, size=11, color=MUTED,
        )
    _footer(slide, light=True)
    return slide


def two_col_slide(prs, title, left_title, left_items, right_title, right_items, kicker=""):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _content_chrome(slide)
    _kicker_title(slide, kicker, title)
    _textbox(slide, MARGIN, Inches(1.25), Inches(5.9), Inches(0.35),
             left_title, size=16, bold=True, color=NAVY)
    _bullets(slide, MARGIN, Inches(1.65), Inches(5.9), Inches(4.8),
             left_items, size=14, space_after=6)
    _textbox(slide, Inches(6.9), Inches(1.25), Inches(5.9), Inches(0.35),
             right_title, size=16, bold=True, color=NAVY)
    _bullets(slide, Inches(6.9), Inches(1.65), Inches(5.9), Inches(4.8),
             right_items, size=14, space_after=6)
    _footer(slide, light=True)
    return slide


def prompt_slide(prs, title, prompts, kicker="", note="", bullet_size=13):
    """One or more labeled prompts on a single slide (merged for PPTX density)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _content_chrome(slide)
    y = _kicker_title(slide, kicker, title, title_size=24)
    for label, text in prompts:
        _textbox(slide, MARGIN, y, Inches(12.1), Inches(0.28),
                 label, size=11, bold=True, color=RED)
        y = Emu(int(y) + int(Inches(0.28)))
        # Prompt background band
        lines = max(2, (len(text) // 95) + 1)
        box_h = Inches(min(0.35 + lines * 0.28, 1.85))
        band = _add_rect(slide, MARGIN, y, Inches(12.1), box_h, PROMPT_BG)
        band.line.color.rgb = NAVY
        band.line.width = Pt(0.75)
        _textbox(
            slide, Emu(int(MARGIN) + int(Inches(0.12))),
            Emu(int(y) + int(Inches(0.06))),
            Inches(11.85), Emu(int(box_h) - int(Inches(0.1))),
            text, size=bullet_size, color=INK,
        )
        y = Emu(int(y) + int(box_h) + int(Inches(0.12)))
    if note:
        _textbox(
            slide, MARGIN, max(y, SLIDE_H - FOOTER_H - Inches(0.45)),
            Inches(12.1), Inches(0.35), note, size=12, color=MUTED,
        )
    _footer(slide, light=True)
    return slide


def closing_slide(prs, title, lede=""):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _bg(slide, NAVY)
    _tricolour_bar(slide, 0)
    _tricolour_bar(slide, SLIDE_H - BAR_H)
    _textbox(
        slide, Inches(0.7), Inches(1.5), Inches(12.0), Inches(0.4),
        "Thank you  |  Centre for Advanced Computing",
        size=14, bold=True, color=GOLD,
    )
    _textbox(
        slide, Inches(0.7), Inches(2.2), Inches(12.0), Inches(1.2),
        title, size=36, bold=True, color=WHITE,
    )
    if lede:
        _textbox(
            slide, Inches(0.7), Inches(3.6), Inches(11.5), Inches(1.2),
            lede, size=16, bold=False, color=SOFT,
        )
    _textbox(
        slide, Inches(0.7), Inches(5.1), Inches(11.5), Inches(0.9),
        AUTHOR, size=14, bold=False, color=GOLD,
    )
    _textbox(
        slide, Inches(0.7), Inches(5.95), Inches(11.5), Inches(0.4),
        "cac.queensu.ca  |  khalifa.s@queensu.ca",
        size=12, bold=False, color=SOFT,
    )
    _footer(slide, light=False)
    return slide


def build():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    # ----- Opening -----
    title_slide(
        prs,
        "Cursor for Research Computing",
        lede=(
            "From Laptop to CAC HPC. Three hours of hands-on practice so you can "
            "use an AI coding agent without abandoning scientific judgment, file "
            "hygiene, or your SLURM checklist."
        ),
        meta=["3 hours - hands-on", "Laptop + optional CAC SSH", "Dry-runs count as success"],
        image_name="hero-cac-cursor.jpg",
    )

    content_slide(
        prs,
        "Anysphere builds Cursor",
        kicker="Cursor the company",
        body=(
            "Cursor is the product of Anysphere, a company focused on AI-native "
            "software development tools rather than a generic chatbot bolted onto "
            "a text box. The company ships an editor that treats large language "
            "models as first-class collaborators inside your project files, "
            "terminals, and (when you allow it) external tools."
        ),
        bullets=[
            "You should care about the vendor story only insofar as it explains the product shape: Cursor is not a separate chat website you paste code into.",
            "It is a fork of a familiar VS Code-style IDE with deep hooks for agents, rules, skills, and Model Context Protocol servers.",
        ],
    )

    content_slide(
        prs,
        "An IDE with an agent, not a chat window with an afterthought editor",
        kicker="Cursor the tool",
        body=(
            "When you open Cursor you get the editor habits you already know "
            "(tabs, git, terminals, extensions) plus a chat and agent panel that "
            "can read your workspace, propose diffs, run commands you approve, "
            "and follow project rules you define."
        ),
        bullets=[
            "For research computing that combination matters because your work lives in repositories, scripts, SLURM templates, and lab conventions.",
            "An agent that can see those files in place is far more useful than one that only sees the last paste you remembered to include.",
        ],
    )

    content_slide(
        prs,
        "Speed with a seatbelt",
        kicker="Why researchers care",
        body=(
            "You already write analysis code, chase obscure traceback lines, draft "
            "job scripts, and translate methods sections into runnable steps. "
            "Cursor can accelerate the boring middle of that work."
        ),
        bullets=[
            "Typical wins: explaining a neighbor's pipeline, drafting argparse, turning a checklist into an sbatch template, or comparing a log against a broken script.",
            "What it cannot do is replace your judgment about data sensitivity, cluster etiquette, or whether a bootstrap CI actually matches Algorithm 1.",
            "This workshop trains the seatbelt habits so the speed does not become an expensive accident.",
        ],
    )

    content_slide(
        prs,
        "What you will do this afternoon",
        kicker="Workshop description",
        body=(
            "You will work through eight use cases, from Privacy Mode and chat "
            "hygiene through a GitHub MCP demo, using the synthetic workshop "
            "repository rather than your restricted research data."
        ),
        bullets=[
            "Each block combines a short concept explanation with prompts you copy into Cursor and concrete done-when checks so you know you finished for real.",
            "If CAC SSH is available you may sync the SLURM exercise and practice remote paths; if not, careful local dry-runs still count.",
            "The point is reproducible control: Ask before Agent, attach the few files you need, keep rules in the project, and never invent module names or accounts.",
        ],
    )

    content_slide(
        prs,
        "Where your materials live",
        kicker="Workshop description",
        bullets=[
            "Hands-on work lives under exercises/ for each use case, with shared templates under config/.cursor for rules and skills.",
            "Keep handouts/budget-card.md and handouts/privacy-and-context.md nearby; they are the one-page habits cards for privacy, context, and spend.",
            "You will not need a separate prompts folder. Every prompt you should type appears on the slides in labeled boxes so you can copy it straight into Cursor.",
        ],
    )

    content_slide(
        prs,
        "Privacy Mode how-to",
        kicker="Do this first",
        bullets=[
            "Windows/Linux: press Ctrl+Shift+J. macOS: Cmd+Shift+J.",
            "Open General and turn Privacy Mode on before you paste anything research-shaped.",
            "If you are on a Teams or Enterprise seat, check whether an admin already enforces Privacy Mode so you are not fighting policy.",
            "Skim handouts/privacy-and-context.md and keep it open while you work.",
        ],
        note="Do this before any exercise. Habit beats hope.",
    )

    content_slide(
        prs,
        "What it protects, and what it does not",
        kicker="Privacy Mode",
        body=(
            "With Privacy Mode on for supported models, Cursor documents that "
            "your code is not used to train Cursor or the model providers. That "
            "is the main protection you are buying with the toggle."
        ),
        bullets=[
            "Prompts and code context still travel to the model provider so answers can be generated. This is not a fully local offline mode.",
            "It also does not authorize pasting restricted, clinical, or identifiable research data into chat.",
            "Some models need admin approval for provider retention, and bring-your-own-key setups follow the provider's own terms.",
        ],
        note="cursor.com/help/security-and-privacy/privacy",
    )

    content_slide(
        prs,
        "What you should be able to do by the end",
        kicker="Objectives",
        bullets=[
            "Choose Ask, Plan, Agent, or Multitask with intent, keep one research objective per chat, and ground answers in files you actually attach rather than in hopeful invention.",
            "Place stable lab policy in Project rules and skills so you stop re-explaining SLURM hygiene in every conversation.",
            "Draft a reviewable sbatch script from a checklist, diagnose a broken job from paired stdout/stderr, and decide when a dry-run is the honest stopping point for the day.",
        ],
    )

    content_slide(
        prs,
        "Artifacts you will have produced",
        kicker="Outcomes",
        bullets=[
            "A grounded README for the literacy exercise, a local analysis script with a plot, and practice with /goal and a capped /loop against a mock job status file.",
            "A methods replication with notes on fidelity limits, and SLURM scripts that keep account and partition as placeholders.",
            "An Explorer-Implementer-Reviewer handoff and a read-then-approve GitHub MCP path. Those habits transfer to your own repos tomorrow morning.",
        ],
    )

    content_slide(
        prs,
        "Morning path: UC0 Foundations through UC3 Skills",
        kicker="Agenda - part 1",
        bullets=[
            "0:00-0:30  UC0 Foundations: Privacy Mode, chat context, modes, Projects, and tokenomics",
            "0:30-0:45  UC1 Codebase literacy and documentation grounding",
            "0:45-1:00  UC2 Local analysis pipeline",
            "1:00-1:10  Break",
            "1:10-1:30  UC3 Skills, /goal, and /loop",
        ],
    )

    content_slide(
        prs,
        "Afternoon path: UC4 Paper replication through UC7 GitHub MCP",
        kicker="Agenda - part 2",
        bullets=[
            "1:30-1:55  UC4 Paper method replication",
            "1:55-2:25  UC5 CAC remote work, SLURM jobs, and debugging",
            "2:25-2:30  Break",
            "2:30-2:45  UC6 Multi-agent orchestration",
            "2:45-3:00  UC7 GitHub MCP demo",
            "Dry-run paths are first-class. Not everyone needs a live sbatch today.",
        ],
    )

    # ----- UC0 -----
    section_slide(
        prs,
        "UC0",
        "Foundations: Privacy Mode, chat context, modes, Projects, and tokenomics",
        "The vocabulary and safety habits everything else depends on.",
    )

    content_slide(
        prs,
        "UC0 Foundations: when you need this",
        kicker="What this use case is",
        body=(
            "You use UC0 Foundations whenever you open Cursor for research work: "
            "before you touch cluster scripts, before you attach a methods brief, "
            "and before you let an agent edit files. It is deliberately off-cluster "
            "and local so you can practice control without burning SLURM time."
        ),
        bullets=[
            "What you will produce is a mental checklist (Privacy Mode on, mode chosen on purpose, context scoped, budget habits visible) plus a short scratch chat that shows the cost difference between vague Agent prompts and tight Ask-then-Plan-then-Agent sequences.",
            "Keep handouts/budget-card.md beside your laptop.",
        ],
    )

    content_slide(
        prs,
        "Large language models and agents in plain language",
        kicker="UC0 Foundations - concepts",
        bullets=[
            "A large language model predicts likely next tokens given the text you and the tools provide. It is extraordinarily good at drafting and explaining, and cheerfully willing to invent module names or cluster accounts that sound plausible.",
            "Treat the model as a fast junior collaborator that must cite files, stay inside placeholders when reality is unknown, and accept \"I do not know\" as a valid answer. Scientific judgment stays with you.",
            "In Cursor, an agent is a loop that can read your workspace, propose edits, call tools you have enabled, and iterate toward a goal you stated. Ask mode mostly explains; Agent mode can change the tree.",
            "You invite Agent mode when the goal is clear, the files are attached, and you are ready to review diffs. You stay in Ask when you are still mapping the territory.",
        ],
        bullet_size=14,
    )

    content_slide(
        prs,
        "Grounding, MCP, and Projects",
        kicker="UC0 Foundations - concepts",
        bullets=[
            "RAG-style grounding means you point the model at the documents that should constrain the answer (lab conventions, checklists, paper briefs) with @ file mentions, Project rules, and skills.",
            "When the model answers a conventions question, you should see quotes or clear pointers to the file it used. If it cannot find the policy, it should say so rather than invent one.",
            "MCP is a standard way for an agent to talk to external tools through servers you connect, with scopes you choose. Start read-only; draft writes for human approval. You will see it for real in UC7 GitHub MCP demo.",
            "A Project keeps stable guidance next to the code: rules that always apply, skills for recurring jobs like drafting SLURM scripts, and the habit of opening the right folder. Workshop templates live under config/.cursor.",
        ],
        bullet_size=14,
    )

    content_slide(
        prs,
        "Ask, Plan, Agent, Multitask",
        kicker="UC0 Foundations - modes",
        body=(
            "Ask is cheap reconnaissance and explanation. Plan outlines steps "
            "without editing. Agent implements with your review. Multitask runs "
            "parallel agents when scopes are disjoint and your budget allows."
        ),
        bullets=[
            "Default order for research work: Ask, then Plan, then Agent. Multitask last.",
            "Ask: explain files, diagnose logs, extract methods. No edits. Lowest blast radius.",
            "Plan: name functions, packages, and verification steps before any diff appears.",
            "Agent: implement a plan you already agree with. Review every diff.",
            "Multitask: parallel agents on disjoint paths. Never two writers on one file.",
        ],
        image_name="modes-diagram.jpg",
        bullet_size=13,
    )

    two_col_slide(
        prs,
        "UC0 Foundations: chat context hygiene",
        "What belongs in the same chat",
        [
            "One objective, short follow-ups, and @ only the files you need for that objective.",
            "Ask then Agent is fine when the goal has not changed and the plan is still visible.",
            "Stable policy should live in rules and skills, not as a novel you re-paste each morning.",
            "Keep restricted or clinical data out of workshop and public threads entirely.",
        ],
        "What does not belong",
        [
            "Unrelated topic hopping (README polish morphing into paper replication mid-thread).",
            "Re-pasting huge SLURM logs when a tail or grep summary would do.",
            "Scope creep after you already said \"done\".",
            "Leaving /loop running while you start another expensive task.",
        ],
        kicker="Chat context",
    )

    content_slide(
        prs,
        "Quality slips before the UI looks dramatic",
        kicker="UC0 Foundations - when context is full",
        body=(
            "Chat context is finite: prior turns, attachments, rules, tool output, "
            "and replies all compete for space. When it fills, older turns may drop "
            "or compact. Answers get vaguer, contradict earlier decisions, or re-ask "
            "questions you already settled, while cost often stays high."
        ),
        bullets=[
            "The fix is boring and effective: open a new chat, paste a three-line handoff, and @ the key files (or a short HANDOFF.md).",
            "Put durable policy in rules so you are not rebuilding the lab every session.",
            "Full context is not smarter; it is usually noisier and more expensive.",
        ],
    )

    content_slide(
        prs,
        "Included usage vs on-demand",
        kicker="UC0 Foundations - tokenomics",
        body=(
            "Your plan includes a monthly usage pool. On-demand usage is "
            "pay-as-you-go after that pool, billed for what you used, not a "
            "prepaid token pack you buy in advance."
        ),
        bullets=[
            "Check the dashboard before long Agent or Multitask sessions. On Teams, someone should set spending limits before a lab discovers curiosity is expensive.",
            "Requests are not silently downgraded in quality or speed when you move to on-demand.",
            "Alternative: upgrade the plan for a larger included pool. On-demand is a safety net, not a reason to attach the whole filesystem.",
        ],
        image_name="tokenomics.jpg",
        note="cursor.com/docs/models-and-pricing  |  handouts/budget-card.md",
    )

    content_slide(
        prs,
        "Twelve habits from the budget card",
        kicker="UC0 Foundations - budget habits",
        bullets=[
            "Privacy Mode first; still no restricted data in prompts.",
            "Ask, then Plan, then Agent, then Multitask. Attach few files. One goal per chat.",
            "Smaller or faster models for explain and refactor; stronger models for hard bugs or method fidelity.",
            "Summarize long SLURM logs before pasting (tail, grep). Cap /loop. One write-scope per agent.",
            "MCP: draft, then you click send. Dry-run SLURM review counts as success when you cannot submit today.",
            "A long chat with a full context window is often the quiet budget leak.",
        ],
    )

    prompt_slide(
        prs,
        "UC0 Foundations: Ask, Plan, Agent practice",
        kicker="UC0 Foundations - hands-on",
        prompts=[
            (
                "Prompt A - Ask mode (copy into Cursor)",
                "In Ask mode: In two short paragraphs, explain what files exist under "
                "exercises/uc1-codebase-literacy and what problem they seem to solve. "
                "Do not edit anything.",
            ),
            (
                "Prompt B - Plan mode (copy into Cursor)",
                "In Plan mode: I want a README for exercises/uc1-codebase-literacy that "
                "a new lab member can trust. Outline sections, which files you would "
                "read, and what you would verify by running code. Do not edit yet.",
            ),
            (
                "Prompt C - Agent mode (copy into Cursor)",
                "In Agent mode: Using your plan, draft exercises/uc1-codebase-literacy/"
                "README.md from README.starter.md. Keep claims tied to files you "
                "actually read. Do not touch other use cases.",
            ),
        ],
        note="You are practicing cheap reconnaissance before any edit.",
        bullet_size=12,
    )

    prompt_slide(
        prs,
        "UC0 Foundations: token sanity, context, on-demand",
        kicker="UC0 Foundations - hands-on",
        prompts=[
            (
                "Prompt D - Token sanity (Ask mode)",
                "In Ask mode: List five ways the previous Agent prompt could have "
                "wasted tokens, and rewrite the Agent prompt to be tighter without "
                "losing the goal.",
            ),
            (
                "Prompt E - Context hygiene (Ask mode)",
                "In Ask mode: We just finished the UC1 README goal. Should I keep "
                "using this same chat for UC4 paper replication? Explain in five "
                "bullets what happens to answer quality when a chat context is nearly "
                "full, and draft a three-line handoff I could paste into a new chat.",
            ),
        ],
        note=(
            "Prompt F (discuss, no tokens needed): What is included monthly usage "
            "versus on-demand on your seat? Who should set Teams spending limits? "
            "Open handouts/budget-card.md and mark habits you already follow."
        ),
        bullet_size=12,
    )

    content_slide(
        prs,
        "UC0 Foundations: you are done when",
        kicker="Done when",
        bullets=[
            "Privacy Mode is on and you can explain what it does and does not protect.",
            "You completed Ask, then Plan, then Agent on a narrow README goal without editing other use cases.",
            "You can describe context-full symptoms and produce a three-line handoff.",
            "You know included vs on-demand usage and where the budget card lives.",
        ],
    )

    # ----- UC1 -----
    section_slide(
        prs,
        "UC1",
        "Codebase literacy and documentation grounding",
        "Explain real files, then force the answer to cite lab conventions.",
    )

    content_slide(
        prs,
        "UC1 Codebase literacy: when you need this",
        kicker="What this use case is",
        body=(
            "You reach for UC1 Codebase literacy and documentation grounding when "
            "you inherit a lab folder, need to onboard yourself to a pipeline, or "
            "must write a README that a new student can trust. Work stays local "
            "under exercises/uc1-codebase-literacy; nothing needs the cluster."
        ),
        bullets=[
            "Researchers often ask an agent to \"clean up the code\" before anyone can say what the code does. UC1 flips that order: Ask to explain normalize.py and pipeline.py first.",
            "Only after that explanation do you ground answers in lab conventions and let Agent update the README. Grounding is how you stop polite fiction from becoming lab policy.",
            "You will produce a README whose run instructions match the repo and at least one claim explicitly tied to docs/lab-conventions.md.",
        ],
    )

    prompt_slide(
        prs,
        "UC1 Codebase literacy: explain, ground, README",
        kicker="UC1 Codebase literacy - hands-on",
        prompts=[
            (
                "Step 1 - Ask for an explanation",
                "@exercises/uc1-codebase-literacy/src Explain normalize.py and "
                "pipeline.py like I am a researcher who writes Python occasionally. "
                "What does each function do, and what could go wrong with messy CSV input?",
            ),
            (
                "Step 2 - Ground with docs (Ask)",
                "Using @exercises/uc1-codebase-literacy/docs/lab-conventions.md and "
                "the source files, answer: Does pipeline.py already follow our lab "
                "conventions? Quote the convention text you relied on. If something "
                "is missing, say what is missing without inventing policy.",
            ),
            (
                "Step 3 - Agent writes the README",
                "Update exercises/uc1-codebase-literacy/README.md so a new student "
                "can run the pipeline and knows where conventions live. Cite file "
                "paths. Do not invent CAC module names.",
            ),
        ],
        note="Open folder: exercises/uc1-codebase-literacy (or the whole workshop repo).",
        bullet_size=11,
    )

    content_slide(
        prs,
        "UC1 Codebase literacy: done when",
        kicker="Done when",
        bullets=[
            "README run instructions match the repo.",
            "At least one claim is explicitly tied to lab-conventions.md.",
            "You caught one model mistake, or confirmed there was none after checking.",
        ],
    )

    # ----- UC2 -----
    section_slide(
        prs,
        "UC2",
        "Local analysis pipeline",
        "Plan a small script, implement it, then harden lightly.",
    )

    content_slide(
        prs,
        "UC2 Local analysis pipeline: when you need this",
        kicker="What this use case is",
        body=(
            "UC2 Local analysis pipeline is the everyday laptop workflow: load a "
            "CSV, clean empties, summarize by condition, write a plot. You work in "
            "exercises/uc2-analysis with synthetic data/measurements.csv, still "
            "off-cluster."
        ),
        bullets=[
            "Plan mode is where you insist on a small tool surface: standard library plus pandas and matplotlib only if that is already reasonable for your audience.",
            "You list steps and packages before any file changes, which keeps Agent from helpfully introducing a project generator you did not ask for.",
            "You will produce a runnable analyze.py, an output/mean_by_condition.png plot, and light argparse so paths are not hard-coded forever. Empty treatment rows must not crash the summary.",
        ],
    )

    prompt_slide(
        prs,
        "UC2 Local analysis: plan, implement, harden",
        kicker="UC2 Local analysis - hands-on",
        prompts=[
            (
                "Step 1 - Plan the analysis",
                "Plan mode: Expand analyze_starter.py into a small analysis script "
                "that (1) loads data/measurements.csv (2) drops empty values "
                "(3) summarizes mean and count by condition (4) writes a simple bar "
                "plot to output/mean_by_condition.png. List packages you will use. "
                "Prefer the standard library plus pandas/matplotlib only if already "
                "reasonable. Do not edit yet.",
            ),
            (
                "Step 2 - Agent implements",
                "Agent mode: Implement the plan in analyze.py (you may replace or "
                "extend the starter). Create output/ if needed. Keep the script "
                "runnable with: python analyze.py",
            ),
            (
                "Step 3 - Light harden",
                "Add argparse so I can pass --data and --outdir. Add a one-line "
                "docstring at the top describing the expected columns. Do not add "
                "a large framework.",
            ),
        ],
        note="Open: exercises/uc2-analysis",
        bullet_size=11,
    )

    content_slide(
        prs,
        "UC2 Local analysis pipeline: done when",
        kicker="Done when",
        bullets=[
            "The script runs locally with python analyze.py.",
            "The plot exists under output/.",
            "An empty treatment row does not crash the summary.",
        ],
    )

    content_slide(
        prs,
        "Break (10 minutes)",
        kicker="Pause",
        body="Stretch. Refill coffee. Resist opening twelve new Agent chats just to try.",
        bullets=[
            "We return with skills, /goal, and a capped /loop against STATUS.mock.txt.",
            "If UC2 is unfinished, finish the plot first; polish later.",
        ],
    )

    # ----- UC3 -----
    section_slide(
        prs,
        "UC3",
        "Skills, /goal, and /loop",
        "Reusable skills, a sticky goal statement, and capped polling.",
    )

    content_slide(
        prs,
        "UC3 Skills, /goal, and /loop: when you need this",
        kicker="What this use case is",
        body=(
            "UC3 Skills, /goal, and /loop is for the moment your analysis script "
            "needs to become job-shaped without you retyping the same SLURM advice. "
            "You copy workshop skill and rule templates from config/.cursor, set a "
            "durable goal, and optionally poll a mock status file so you learn to "
            "stop loops on purpose."
        ),
        bullets=[
            "Work is mostly local; the skill drafts SLURM content with placeholders, and you dry-run only.",
            "Materials live under exercises/uc3-skills-directives with a mock status file you can edit yourself.",
        ],
    )

    content_slide(
        prs,
        "Reusable playbooks the agent can load on demand",
        kicker="UC3 Skills - how-to",
        body=(
            "A skill is a packaged set of instructions for a recurring job (here, "
            "drafting a reviewable sbatch script with time, cpus, mem, logs, and an "
            "explicit working directory). Unlike a one-off chat paragraph, a skill "
            "survives across sessions once it lives in your project or personal "
            "skills store."
        ),
        bullets=[
            "Before prompts, copy config/.cursor/skills/cac-slurm-job into the project .cursor/skills/ (or your user skills store).",
            "Copy config/.cursor/rules/cac-research.mdc into .cursor/rules/.",
            "Those standing rules mean you stop retyping \"do not invent CAC modules\" into every chat.",
        ],
    )

    content_slide(
        prs,
        "A sticky north star across several tool steps",
        kicker="UC3 /goal - when and how",
        body=(
            "Use /goal when the next fifteen minutes will involve multiple prompts, "
            "a skill invocation, and maybe a loop, and you do not want the agent to "
            "quietly redefine success as \"wrote any script.\" The goal statement "
            "stays visible and useful across steps."
        ),
        bullets=[
            "A good research goal names the artifact, the environment constraints (SLURM-ready, dry-run only), and the non-goals (do not submit).",
            "Vague goals like \"make it better\" invite expensive wandering.",
            "Research example: your UC2 analyze.py already runs on the laptop. The need is not more features; it is that this must be callable under SLURM with a data path via env or argparse, plus a draft sbatch that uses the cac-slurm-job skill.",
        ],
    )

    prompt_slide(
        prs,
        "UC3 Skills: set /goal and invoke the skill",
        kicker="UC3 Skills and directives - hands-on",
        prompts=[
            (
                "Step 1 - Set /goal (copy into Cursor)",
                "/goal Make exercises/uc2-analysis/analyze.py (or analyze_starter.py "
                "if analyze.py is missing) ready to run under SLURM on CAC: working "
                "entrypoint, data path via env or argparse, and a draft sbatch script "
                "using the cac-slurm-job skill. Dry-run only; do not submit.",
            ),
            (
                "Step 2 - Invoke the skill explicitly",
                "Using the cac-slurm-job skill, draft exercises/uc5-cac-slurm/scripts/"
                "job.generated.sh for python scripts/analyze_job.py with 10 minutes, "
                "1 CPU, 2G memory. Keep account/partition as placeholders. List "
                "verify-before-submit bullets.",
            ),
        ],
        bullet_size=12,
    )

    content_slide(
        prs,
        "Watch STATUS.mock.txt like a tiny SLURM status board",
        kicker="UC3 /loop - exact how",
        body=(
            "Use /loop when you are watching an external signal: a job status file, "
            "a build log path, a mock queue. Always set an interval and a maximum "
            "number of ticks, and define the stop states (DONE, FAILED) up front. "
            "Unbounded loops are how curiosity becomes an invoice."
        ),
        bullets=[
            "Open exercises/uc3-skills-directives/STATUS.mock.txt. It starts with JOB_STATE=RUNNING and a note that you may edit the state.",
            "Ask Cursor to read that file on an interval, summarize JOB_STATE in one sentence, and stop when the state is DONE or FAILED, or after four ticks.",
            "After one or two ticks, edit the file yourself to JOB_STATE=DONE (or FAILED) so you see a clean stop. That edit is the whole point: you are the human who decides the loop is finished.",
            "Tick pattern: Tick 1 reports RUNNING and waits ~30s; Tick 2 still RUNNING unless you edited; you change the file; Tick 3 sees DONE/FAILED and stops, or hits the 4-tick cap.",
        ],
        bullet_size=13,
    )

    prompt_slide(
        prs,
        "UC3 Skills: short capped /loop",
        kicker="UC3 Skills and directives - hands-on",
        prompts=[
            (
                "Step 3 - Short capped /loop (copy into Cursor)",
                "/loop 30s Read exercises/uc3-skills-directives/STATUS.mock.txt and "
                "summarize JOB_STATE in one sentence. Stop when JOB_STATE is DONE or "
                "FAILED, or after 4 ticks, whichever comes first.",
            ),
        ],
        note=(
            "After 1-2 ticks, edit STATUS.mock.txt to JOB_STATE=DONE yourself. "
            "Stop rules: stop on DONE/FAILED, stop at max ticks even if still "
            "RUNNING, stop if the loop is not helping, never leave a loop running "
            "while you start Multitask or a second expensive chat."
        ),
        bullet_size=13,
    )

    content_slide(
        prs,
        "UC3 Skills, /goal, and /loop: done when",
        kicker="Done when",
        bullets=[
            "The skill produced a reviewable script with placeholders.",
            "The goal statement stayed visible and useful across steps.",
            "The loop stopped on purpose (DONE/FAILED or tick cap), not by abandonment.",
        ],
    )

    # ----- UC4 -----
    section_slide(
        prs,
        "UC4",
        "Paper method replication",
        "Extract the method, plan functions, implement, then diff against Algorithm 1.",
    )

    content_slide(
        prs,
        "UC4 Paper method replication: when you need this",
        kicker="What this use case is",
        body=(
            "UC4 Paper method replication is for the common research need: a short "
            "methods brief (or paper supplement) must become runnable code with "
            "honest fidelity notes. You work in exercises/uc4-paper-replication "
            "using the workshop measurements CSV from the analysis exercise."
        ),
        bullets=[
            "Ask extracts the research question, Algorithm 1 steps, defaults, and acceptance checks before anyone writes code.",
            "Plan names functions and seed handling. Agent implements. Ask again diffs the implementation line by line against Algorithm 1.",
            "Approximations belong in REPLICATION_NOTES.md, not in silent shortcuts. You will produce replicate.py, printed mean difference and bootstrap CI with seed 7, and short fidelity notes.",
        ],
        image_name="paper-replication.jpg",
        bullet_size=13,
    )

    prompt_slide(
        prs,
        "UC4 Paper replication: extract, plan, implement, verify",
        kicker="UC4 Paper replication - hands-on",
        prompts=[
            (
                "Step 1 - Ask extracts the method",
                "Ask mode: Read PAPER_BRIEF.md. Extract the research question, "
                "Algorithm 1 steps, defaults, and acceptance checks as a bullet list "
                "I can implement against. Do not write code yet.",
            ),
            (
                "Step 2 - Plan the implementation",
                "Plan mode: Propose a Python implementation plan for Algorithm 1 that "
                "satisfies the acceptance checks, including random seed handling and "
                "how you will exclude empty values. Name the functions you will create.",
            ),
            (
                "Steps 3-4 - Agent implements, then Ask verifies",
                "Agent: Implement replicate.py from replicate_starter.py against "
                "PAPER_BRIEF.md and the measurements CSV. Print observed mean "
                "difference and 95% bootstrap CI. Use seed=7. Add a short "
                "REPLICATION_NOTES.md stating fidelity limits. Then Ask: Diff your "
                "implementation against Algorithm 1 line by line. Call out any step "
                "that is missing or approximated.",
            ),
        ],
        note="Open: exercises/uc4-paper-replication - Data: ../uc2-analysis/data/measurements.csv",
        bullet_size=11,
    )

    content_slide(
        prs,
        "UC4 Paper method replication: done when",
        kicker="Done when",
        bullets=[
            "Acceptance checks 1-4 in PAPER_BRIEF.md pass, or are honestly marked incomplete.",
            "REPLICATION_NOTES.md states fidelity limits in plain language.",
            "Seed 7 is used and the CI printout matches what you asked for.",
        ],
    )

    # ----- UC5 -----
    section_slide(
        prs,
        "UC5",
        "CAC remote work, SLURM jobs, and debugging",
        "SSH when available, checklist-driven drafts, logs that tell the truth.",
    )

    content_slide(
        prs,
        "UC5 CAC remote work, SLURM jobs, and debugging: when you need this",
        kicker="What this use case is",
        body=(
            "UC5 CAC remote work, SLURM jobs, and debugging is the bridge from "
            "laptop scripts to CAC. If SSH is available you may connect and keep "
            "work under a demo directory; if not, you stay local and treat drafts "
            "as dry-runs. Either path is legitimate workshop success."
        ),
        bullets=[
            "Heavy compute does not belong on the login node. Editing, git, and light checks are fine; analysis and training belong in jobs on compute nodes through SLURM.",
            "Never invent CAC account names, partitions, or module versions. Use YOUR_ACCOUNT / YOUR_PARTITION placeholders and SLURM_CHECKLIST.md.",
            "Under exercises/uc5-cac-slurm you will generate a script with placeholders, diagnose paired logs from a broken job, and write a fixed script.",
        ],
        image_name="ssh-slurm.jpg",
        bullet_size=13,
    )

    content_slide(
        prs,
        "Checklist-driven drafts beat folklore",
        kicker="UC5 CAC + SLURM - concept",
        bullets=[
            "A good sbatch script states time, cpus, mem, output and error logs, and an explicit working directory.",
            "The workshop template and SLURM_CHECKLIST.md exist so the agent (and you) stop relying on half-remembered flags from a different cluster.",
            "When logs disagree with the script, diagnose both stdout and stderr together with the broken script before you fix anything.",
            "Ranking failures beats guessing the first line that looks angry. If you cannot submit today, a reviewed dry-run still counts.",
        ],
    )

    prompt_slide(
        prs,
        "UC5 CAC + SLURM: Parts A and B",
        kicker="UC5 CAC + SLURM - hands-on",
        prompts=[
            (
                "Part A - Remote project (when connected to CAC)",
                "We are connected to CAC over SSH. Confirm the current workspace "
                "path, create a directory ~/cursor-workshop-demo if missing, and "
                "sync only the uc5-cac-slurm exercise files there if appropriate. "
                "Summarize login-node vs compute-node rules in three bullets.",
            ),
            (
                "Part B - Plan what must change",
                "Plan mode: Using exercises/uc5-cac-slurm/scripts/job.template.sh "
                "and SLURM_CHECKLIST.md, list what must change before a real submit "
                "on CAC.",
            ),
            (
                "Part B - Agent drafts job.generated.sh",
                "Agent mode: Create scripts/job.generated.sh from the template for "
                "analyze_job.py. Keep YOUR_ACCOUNT and YOUR_PARTITION placeholders. "
                "Fix the data path assumption in comments.",
            ),
        ],
        note="If SSH is unavailable, stay local and treat Parts B and C as dry-run.",
        bullet_size=11,
    )

    prompt_slide(
        prs,
        "UC5 CAC + SLURM: Part C debug from logs",
        kicker="UC5 CAC + SLURM - hands-on",
        prompts=[
            (
                "Part C - Diagnose the broken job (Ask)",
                "Ask mode: Diagnose exercises/uc5-cac-slurm/logs/slurm-4242.out and "
                "slurm-4242.err together with scripts/job.broken.sh. Rank the "
                "failures. Propose a minimal fixed script.",
            ),
            (
                "Part C - Write the fixed script (Agent)",
                "Agent mode: Write scripts/job.fixed.sh that addresses the module, "
                "path, and data issues without inventing a real CAC account.",
            ),
        ],
        note="Done when: you reviewed SLURM_CHECKLIST.md, can explain the broken job in plain language, and job.fixed.sh exists. Submit is optional.",
        bullet_size=12,
    )

    content_slide(
        prs,
        "Break (5 minutes)",
        kicker="Pause",
        body="Almost done. Multi-agent handoffs next, then a careful GitHub MCP demo.",
        bullets=[
            "If your job.fixed.sh still looks haunted, bring it to the wrap-up.",
        ],
    )

    # ----- UC6 -----
    section_slide(
        prs,
        "UC6",
        "Multi-agent orchestration",
        "Explorer, Implementer, Reviewer, with you as the gate.",
    )

    content_slide(
        prs,
        "UC6 Multi-agent orchestration: when you need this",
        kicker="What this use case is",
        body=(
            "UC6 Multi-agent orchestration is for work that benefits from separated "
            "roles: one read-only map of the tree, one implementer with a narrow "
            "write scope, one reviewer against a checklist. Follow "
            "exercises/uc6-multi-agent/ORCHESTRATION.md."
        ),
        bullets=[
            "Parallel agents are useful when paths are disjoint. Two agents editing the same file is how you get a merge conflict dressed up as productivity.",
            "Optional Multitask is only worth the budget when Explorer reads while Implementer writes elsewhere, then you merge judgment manually.",
            "You will produce Explorer bullets, a generated sbatch under the uc5 scripts folder, and a pass/fail review. No sbatch submit is required. You remain the human gate: accept, request revisions, or stop.",
        ],
        image_name="multi-agent.jpg",
        bullet_size=13,
    )

    prompt_slide(
        prs,
        "UC6 Multi-agent: Explorer, Implementer, Reviewer",
        kicker="UC6 Multi-agent - hands-on",
        prompts=[
            (
                "Agent 1 - Explorer (Ask, read-only)",
                "Ask mode / Explorer role: Map exercises/uc5-cac-slurm for a teammate "
                "who will write an sbatch script. Max 10 bullets: key files, risks, "
                "and what not to invent.",
            ),
            (
                "Agent 2 - Implementer (Plan then Agent)",
                "Implementer role: Create exercises/uc5-cac-slurm/scripts/"
                "job.generated.sh for analyze_job.py. Edit only under "
                "exercises/uc5-cac-slurm/scripts/. Assumptions as comments. Dry-run "
                "only. Paste the Explorer bullets first so Implementer inherits the map.",
            ),
            (
                "Agent 3 - Reviewer (Ask)",
                "Ask mode / Reviewer role: Grade scripts/job.generated.sh against "
                "SLURM_CHECKLIST.md. Pass/fail per item. Do not edit files.",
            ),
        ],
        note=(
            "Human gate: accept, revise, or stop. Multitask last, and only when "
            "write scopes are truly disjoint."
        ),
        bullet_size=11,
    )

    content_slide(
        prs,
        "UC6 Multi-agent orchestration: done when",
        kicker="Done when",
        bullets=[
            "Explorer map exists (max 10 bullets).",
            "Implementer wrote only under the allowed scripts path.",
            "Reviewer produced pass/fail against SLURM_CHECKLIST.md.",
            "You made an explicit accept / revise / stop decision.",
        ],
    )

    # ----- UC7 -----
    section_slide(
        prs,
        "UC7",
        "GitHub MCP demo",
        "Read with tools, draft writes, you click send.",
    )

    content_slide(
        prs,
        "UC7 GitHub MCP demo: when you need this",
        kicker="What this use case is",
        body=(
            "UC7 GitHub MCP demo shows how an agent talks to GitHub through MCP "
            "with minimal scopes. You use it when issue triage or README pointers "
            "should not require pasting personal access tokens into chat. Materials "
            "and notes live under exercises/uc7-github-mcp."
        ),
        bullets=[
            "Connect GitHub MCP with minimal scopes before the demo prompts. Prefer read-only first.",
            "You will watch a read path (list open issues, summarize titles) and a write path that stops at a draft until you say to post.",
            "The safety discussion is part of the deliverable: what is risky on a shared lab repo, and what narrower alternative you would recommend for class use.",
        ],
        image_name="mcp-github.jpg",
        bullet_size=13,
    )

    prompt_slide(
        prs,
        "UC7 GitHub MCP: read, draft, discuss risk",
        kicker="UC7 GitHub MCP - hands-on",
        prompts=[
            (
                "Demo prompt 1 - read only",
                "Using the GitHub MCP tools, list the open issues on <ORG/REPO> "
                "(your instructor will fill this). Summarize the top 3 by title only. "
                "Do not comment or close anything.",
            ),
            (
                "Demo prompt 2 - draft, then wait",
                "Draft a polite issue comment for issue #<N> that points newcomers "
                "to the workshop README section on SLURM dry-runs. Show me the "
                "comment text first. Do not post until I say \"post it\".",
            ),
            (
                "Optional follow-up - risk discussion (Ask)",
                "Ask mode: What GitHub MCP actions are risky on a shared lab repo, "
                "and what narrower alternative would you recommend for class use?",
            ),
        ],
        note="Done when: read path without writing; write path as draft-then-approve; short scope and safety discussion completed.",
        bullet_size=11,
    )

    # ----- Closing -----
    content_slide(
        prs,
        "Where to look after class",
        kicker="Materials map",
        bullets=[
            "exercises/uc1-codebase-literacy through exercises/uc7-github-mcp",
            "config/.cursor for rules and skills templates",
            "handouts/budget-card.md and handouts/privacy-and-context.md",
            "This deck: presentations/cursor-cac-workshop.html and the PPTX beside it",
        ],
    )

    content_slide(
        prs,
        "Take these back to your own repo",
        kicker="Closing habits",
        body=(
            "Privacy Mode on, Ask before Agent, few attachments, one goal per chat, "
            "rules and skills for durable policy, dry-run SLURM review as legitimate "
            "success, MCP drafts until you approve. Those habits matter more than "
            "any single clever prompt."
        ),
        bullets=[
            "When something fails on CAC, bring the checklist and both logs.",
            "When something fails in chat, bring a new thread and a three-line handoff.",
            "Curiosity is allowed; unbounded spend is not.",
        ],
    )

    closing_slide(
        prs,
        "Go build carefully",
        lede=(
            "You now have a path from laptop exploration to CAC-ready SLURM drafts, "
            "with Projects, modes, skills, and MCP as practical vocabulary rather "
            "than buzzwords."
        ),
    )

    prs.save(str(OUT))
    return len(prs.slides)


if __name__ == "__main__":
    n = build()
    print(f"Wrote {OUT} with {n} slides")
    print(f"Author: {AUTHOR}")
