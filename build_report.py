#!/usr/bin/env python3
"""Build a polished Expense Report PDF from Dave's expense-tracker Sheet."""
import json, os, urllib.request
from collections import Counter, defaultdict
from datetime import date

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import re

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, Image, PageBreak, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

URL = "https://script.google.com/macros/s/AKfycbzUQJ2Kjuu5-udsVZO49fQ4Mb89JyrhKETIIyjW-HPqC4Upv3F2XMzksg3uzk2cmQR8cg/exec"
OUT = "/home/hatch/workspace/your_files/expense-report"
os.makedirs(OUT + "/charts", exist_ok=True)

# palette
TEAL = HexColor("#0E4F4A")
TEAL_D = HexColor("#0A3B37")
TEAL_L = HexColor("#E3EFED")
GOLD = HexColor("#C98A1B")
GOLD_L = HexColor("#FBF3E2")
INK = HexColor("#1F2A2A")
MUTED = HexColor("#6B7B7B")
LINE = HexColor("#D8E2E1")
ROW_A = HexColor("#FFFFFF")
ROW_B = HexColor("#F4F8F7")
RED = HexColor("#B3261E")
GREEN = HexColor("#1E7E34")

CAT_COLORS = ["#0E4F4A", "#14705F", "#1E8E74", "#3AA88A", "#C98A1B",
              "#E0A83E", "#E8BE5F", "#8A9A9A", "#5B6E6E", "#3D4F4F",
              "#B3261E", "#7A5C9E", "#4A7FA5", "#946B4A", "#6B8E6B"]

def money(v):
    return "$%s" % format(v, ",.2f")

# Internal account-to-account movements are grouped as "Transfers" for display
# (they are not day-to-day spending). The Sheet data itself is untouched.
TRANSFER_RE = re.compile(r'moneylink|recurring transfer|online transfer|transfer (to|from)|line of credit', re.I)

def fetch():
    with urllib.request.urlopen(URL + "?action=list&tab=Transactions", timeout=90) as r:
        return json.load(r)["rows"]

def month_key(d):
    return str(d or "")[:7]

def build():
    rows = fetch()
    exp = [r for r in rows if r.get("txn_type") == "expense"]
    inc = [r for r in rows if r.get("txn_type") == "income"]
    for r in rows:
        r["_amt"] = float(r.get("amount") or 0)
        r["_m"] = month_key(r.get("date"))
        r["_cat"] = r.get("category") or "Uncategorized"
        desc = (r.get("merchant") or r.get("description") or "")
        r["_rep_cat"] = ("Transfers" if (r.get("txn_type") == "expense" and TRANSFER_RE.search(desc))
                         else r["_cat"])

    months = sorted(set(r["_m"] for r in rows if r["_m"]))
    tot_e = sum(r["_amt"] for r in exp)
    tot_i = sum(r["_amt"] for r in inc)

    cat_e = defaultdict(float); catn_e = Counter()
    for r in exp:
        cat_e[r["_rep_cat"]] += r["_amt"]; catn_e[r["_rep_cat"]] += 1
    cats_sorted = sorted(cat_e.items(), key=lambda x: -x[1])

    cat_i = defaultdict(float)
    for r in inc:
        cat_i[r["_cat"]] += r["_amt"]

    me = defaultdict(float); mi = defaultdict(float)
    for r in exp: me[r["_m"]] += r["_amt"]
    for r in inc: mi[r["_m"]] += r["_amt"]

    bp = Counter(r.get("business_personal") or "Personal" for r in exp)

    top_merch = defaultdict(float)
    for r in exp:
        top_merch[(r.get("merchant") or r.get("description") or "")[:48]] += r["_amt"]
    top_merch = sorted(top_merch.items(), key=lambda x: -x[1])[:10]

    biggest = sorted(exp, key=lambda r: -r["_amt"])[:10]

    # ---------- charts ----------
    plt.rcParams.update({"font.family": "DejaVu Sans", "axes.titlesize": 11,
                         "axes.titleweight": "bold"})
    # category bars
    fig, ax = plt.subplots(figsize=(7.2, max(2.6, 0.42 * len(cats_sorted))))
    items = cats_sorted[::-1]  # ascending so the largest bar sits on top
    labels = [c for c, _ in items]
    vals = [v for _, v in items]
    colors = [CAT_COLORS[i % len(CAT_COLORS)] for i in range(len(items))]
    ax.barh(labels, vals, color=colors, height=0.62)
    ax.set_title("Spending by category", pad=12, loc="left")
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: "$%dk" % (v / 1000)))
    for s in ["top", "right", "bottom"]:
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color("#D8E2E1")
    ax.tick_params(left=False)
    fig.tight_layout()
    fig.savefig(OUT + "/charts/cat.png", dpi=150)
    plt.close(fig)

    # monthly trend
    fig, ax = plt.subplots(figsize=(7.2, 3.2))
    xs = range(len(months))
    w = 0.36
    ax.bar([x - w / 2 for x in xs], [me[m] for m in months], width=w,
           color="#0E4F4A", label="Expenses")
    ax.bar([x + w / 2 for x in xs], [mi[m] for m in months], width=w,
           color="#C98A1B", label="Income")
    ax.set_xticks(list(xs)); ax.set_xticklabels(months)
    ax.set_title("Income vs expenses by month", pad=12, loc="left")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: "$%dk" % (v / 1000)))
    ax.legend(frameon=False, loc="upper left")
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUT + "/charts/trend.png", dpi=150)
    plt.close(fig)

    # ---------- PDF ----------
    pdf_path = OUT + "/expense-report.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=2 * cm, rightMargin=2 * cm,
                            topMargin=1.6 * cm, bottomMargin=1.8 * cm,
                            title="Expense Report", author="Expense Tracker")

    sTitle = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=30,
                            leading=34, textColor=white)
    sSub = ParagraphStyle("sub", fontName="Helvetica", fontSize=12, leading=16,
                          textColor=HexColor("#CFE3E1"))
    sH1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=15, leading=19,
                         textColor=TEAL, spaceBefore=14, spaceAfter=8)
    sH2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12, leading=15,
                         textColor=TEAL, spaceBefore=10, spaceAfter=6)
    sBody = ParagraphStyle("body", fontName="Helvetica", fontSize=10, leading=14.5,
                           textColor=INK, spaceAfter=6)
    sMuted = ParagraphStyle("muted", fontName="Helvetica", fontSize=9, leading=12.5,
                            textColor=MUTED, spaceAfter=4)
    sNum = ParagraphStyle("num", fontName="Helvetica-Bold", fontSize=16, leading=19,
                          textColor=TEAL, alignment=TA_CENTER)
    sNumLbl = ParagraphStyle("numlbl", fontName="Helvetica", fontSize=9, leading=11,
                             textColor=MUTED, alignment=TA_CENTER)
    sCell = ParagraphStyle("cell", fontName="Helvetica", fontSize=9.5, leading=12.5, textColor=INK)
    sCellR = ParagraphStyle("cellr", parent=sCell, alignment=TA_RIGHT)
    sCellB = ParagraphStyle("cellb", parent=sCell, fontName="Helvetica-Bold")
    sCellBR = ParagraphStyle("cellbr", parent=sCellB, alignment=TA_RIGHT)

    story = []
    W = A4[0] - 4 * cm

    def footer(canvas, doc_):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(2 * cm, 1.1 * cm, "Expense Tracker  ·  Generated %s" % date.today().strftime("%B %d, %Y"))
        canvas.drawRightString(A4[0] - 2 * cm, 1.1 * cm, "Page %d" % doc_.page)
        canvas.restoreState()

    # cover
    cover = Table([
        [Paragraph("Expense<br/>Report", sTitle)],
        [Paragraph("%s – %s<br/>%d transactions · %s" % (
            months[0], months[-1], len(rows),
            ", ".join(sorted(set(r.get("business_personal") or "Personal" for r in rows)))), sSub)],
    ], colWidths=[W])
    cover.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TEAL),
        ("TOPPADDING", (0, 0), (-1, 0), 34),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 30),
        ("LEFTPADDING", (0, 0), (-1, -1), 22),
        ("LINEBELOW", (0, 0), (-1, 0), 2, GOLD),
    ]))
    story.append(cover)
    story.append(Spacer(1, 14))
    story.append(Paragraph(
        "Prepared for <b>Dave</b> · Source: Expense Tracker Google Sheet · "
        "All figures in USD.", sMuted))
    story.append(Spacer(1, 6))

    # stat cards
    net = tot_i - tot_e
    cards = [
        ("Total expenses", money(tot_e), TEAL),
        ("Total income", money(tot_i), GREEN),
        ("Net cash flow", money(net), TEAL_D if net >= 0 else RED),
        ("Transactions", "%d" % len(rows), INK),
    ]
    card_cells = []
    for lbl, val, col in cards:
        t = Table([[Paragraph(val, ParagraphStyle("n", parent=sNum, textColor=col))],
                   [Paragraph(lbl, sNumLbl)]], colWidths=[W / 4 - 8])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), ROW_B),
            ("ROUNDEDCORNERS", [6, 6, 6, 6]),
            ("BOX", (0, 0), (-1, -1), 1, LINE),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ]))
        card_cells.append(t)
    ct = Table([card_cells], colWidths=[W / 4] * 4, spaceBefore=4, spaceAfter=4)
    ct.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 4),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 4)]))
    story.append(ct)
    story.append(Paragraph("Average monthly spending: <b>%s</b> over %d months." % (
        money(tot_e / max(1, len(months))), len(months)), sBody))

    # category chart + table
    story.append(Paragraph("Where the money went", sH1))
    cat_h = max(2.6, 0.42 * len(cats_sorted))
    story.append(Image(OUT + "/charts/cat.png", width=W, height=W * cat_h / 7.2))
    story.append(Spacer(1, 6))
    chead = [Paragraph("<b>Category</b>", sCell), Paragraph("<b>Txns</b>", sCellR),
             Paragraph("<b>Share</b>", sCellR), Paragraph("<b>Amount</b>", sCellBR)]
    crows = [chead]
    for c, v in cats_sorted:
        pct = 100 * v / tot_e if tot_e else 0
        crows.append([Paragraph(c, sCell), Paragraph("%d" % catn_e[c], sCellR),
                      Paragraph("%.1f%%" % pct, sCellR), Paragraph(money(v), sCellR)])
    crows.append([Paragraph("<b>Total</b>", sCellB), Paragraph("<b>%d</b>" % len(exp), sCellBR),
                  Paragraph("<b>100%</b>", sCellBR), Paragraph("<b>%s</b>" % money(tot_e), sCellBR)])
    cw = [W * 0.44, W * 0.14, W * 0.14, W * 0.28]
    t = Table(crows, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TEAL), ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [ROW_A, ROW_B]),
        ("BACKGROUND", (0, -1), (-1, -1), TEAL_L),
        ("LINEBELOW", (0, 0), (-1, 0), 1.5, TEAL_D),
        ("LINEABOVE", (0, -1), (-1, -1), 1.5, TEAL_D),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)

    # monthly trend
    story.append(Paragraph("Month by month", sH1))
    story.append(Image(OUT + "/charts/trend.png", width=W, height=W * 3.2 / 7.2))
    story.append(Spacer(1, 6))
    mhead = [Paragraph("<b>Month</b>", sCell), Paragraph("<b>Income</b>", sCellR),
             Paragraph("<b>Expenses</b>", sCellR), Paragraph("<b>Net</b>", sCellBR)]
    mrows = [mhead]
    for m in months:
        n = mi[m] - me[m]
        mrows.append([Paragraph(m, sCell), Paragraph(money(mi[m]), sCellR),
                      Paragraph(money(me[m]), sCellR),
                      Paragraph(money(n), ParagraphStyle("x", parent=sCellBR,
                               textColor=GREEN if n >= 0 else RED))])
    t = Table(mrows, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TEAL), ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [ROW_A, ROW_B]),
        ("LINEBELOW", (0, 0), (-1, 0), 1.5, TEAL_D),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)

    # largest expenses
    story.append(Paragraph("Largest expenses", sH1))
    lhead = [Paragraph("<b>Date</b>", sCell), Paragraph("<b>Description</b>", sCell),
             Paragraph("<b>Category</b>", sCell), Paragraph("<b>Amount</b>", sCellBR)]
    lrows = [lhead]
    for r in biggest:
        desc = (r.get("merchant") or r.get("description") or "")[:52]
        lrows.append([Paragraph(str(r.get("date"))[:10], sCell), Paragraph(desc, sCell),
                      Paragraph(r["_rep_cat"], sCell), Paragraph(money(r["_amt"]), sCellR)])
    t = Table(lrows, colWidths=[W * 0.14, W * 0.44, W * 0.22, W * 0.20], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TEAL), ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [ROW_A, ROW_B]),
        ("LINEBELOW", (0, 0), (-1, 0), 1.5, TEAL_D),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)

    # income summary
    story.append(Paragraph("Income summary", sH1))
    ihead = [Paragraph("<b>Category</b>", sCell), Paragraph("<b>Amount</b>", sCellBR),
             Paragraph("<b>Share</b>", sCellR)]
    irows = [ihead]
    for c, v in sorted(cat_i.items(), key=lambda x: -x[1]):
        irows.append([Paragraph(c, sCell), Paragraph(money(v), sCellR),
                      Paragraph("%.1f%%" % (100 * v / tot_i if tot_i else 0), sCellR)])
    t = Table(irows, colWidths=[W * 0.5, W * 0.28, W * 0.22], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TEAL), ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [ROW_A, ROW_B]),
        ("LINEBELOW", (0, 0), (-1, 0), 1.5, TEAL_D),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)

    # notes
    story.append(Paragraph("Notes", sH1))
    story.append(Paragraph(
        "Data source: the Transactions tab of your Expense Tracker Google Sheet, covering "
        "%s to %s. " % (months[0], months[-1]) +
        "On %s, income/expense classifications were corrected — the original statement import "
        "had marked every transaction as income. Classifications were assigned from description "
        "patterns (e.g. “Purchase authorized”, checks, fees → expense; payroll, deposits, "
        "transfers in → income)." % date.today().strftime("%B %d, %Y"), sBody))
    story.append(Paragraph(
        "“<b>Transfers</b>” in the charts above groups internal movements between your own accounts "
        "(brokerage, savings, line of credit) — money moving, not money spent. Your Sheet data is "
        "unchanged; this grouping applies to this report only.", sBody))

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print("wrote", pdf_path)

if __name__ == "__main__":
    build()
