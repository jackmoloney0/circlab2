#!/usr/bin/env python3
"""
Build the printable outputs:

  report/EEEN20020_Exp2_PROTOTYPE_REPORT.pdf   from docs/01_PROTOTYPE_REPORT.md
  report/EEEN20020_Exp2_DATA_SHEET.pdf         bench data-collection sheet

Markdown -> HTML (python-markdown) -> PDF (headless Chromium).
Before building, every mock-screen value quoted in the report is checked
against figures/mock_values.json so the tables cannot drift from the figures.
"""
import json
import os
import re
import sys

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REP = os.path.join(ROOT, "report")
CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")

CSS = r"""
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Liberation Sans", Arial, "DejaVu Sans", sans-serif; font-size: 9.6pt;
       line-height: 1.38; color: #111827; background: #ffffff; }
h1 { font-size: 19pt; margin: 0 0 4pt 0; color: #7f1d1d; }
h2 { font-size: 13.2pt; margin: 14pt 0 6pt 0; padding: 4pt 6pt; background: #f3f4f6;
     border-left: 5px solid #111827; break-after: avoid; }
h3 { font-size: 11pt; margin: 10pt 0 4pt 0; break-after: avoid; }
p { margin: 4pt 0 5pt 0; }
table { border-collapse: collapse; width: 100%; margin: 5pt 0 7pt 0; break-inside: avoid; font-size: 9pt; }
th, td { border: 1px solid #374151; padding: 3pt 5pt; vertical-align: top; }
th { background: #e5e7eb; }
img { display: block; max-width: 100%; max-height: 118mm; margin: 4pt auto 2pt auto; break-inside: avoid; }
em { color: #1f2937; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.4pt; background: #f3f4f6; padding: 0 2px; }
.tbox { border: 1.6px solid #111827; padding: 5pt 7pt; margin: 7pt 0; }
.tbhead { font-weight: bold; font-size: 9pt; background: #111827; color: #ffffff;
          margin: -5pt -7pt 6pt -7pt; padding: 3pt 7pt; }
.guide { border: 1.4px dashed #2563eb; background: #eff6ff; padding: 4pt 8pt; margin: 7pt 0;
         font-size: 8.6pt; break-inside: avoid; }
.notice { border: 2.2px solid #b91c1c; background: #fef2f2; padding: 5pt 9pt; margin: 6pt 0 8pt 0; }
.tag { display: inline-block; font-size: 7.4pt; font-weight: bold; padding: 0.5pt 4pt;
       border-radius: 3px; border: 1px solid; line-height: 1.25; }
.tag.proto { background: #fee2e2; color: #991b1b; border-color: #ef4444; }
.tag.sim { background: #dbeafe; color: #1e3a8a; border-color: #3b82f6; }
.tag.keep { background: #dcfce7; color: #14532d; border-color: #22c55e; }
.pb { break-after: page; height: 0; }
.wm { position: fixed; top: 40%; left: -12%; width: 124%; text-align: center; transform: rotate(-32deg);
      font-size: 54pt; font-weight: bold; color: rgba(220, 38, 38, 0.075); z-index: 0;
      pointer-events: none; white-space: nowrap; }
.content { position: relative; z-index: 1; }
"""


def tagify(html):
    def rep(m):
        txt = m.group(1)
        cls = "proto" if "PROTOTYPE" in txt else "sim" if "SIM-REF" in txt else "keep" if "KEEP" in txt else None
        if cls is None:
            return m.group(0)
        return f'<span class="tag {cls}">{txt}</span>'
    html = re.sub(r"<strong>\[([^\]<]+)\]</strong>", rep, html)
    html = re.sub(r"<p><strong>Template box — (.*?)</strong></p>",
                  r'<div class="tbhead">\1</div>', html)
    return html


def md_to_html(md_path, title, watermark):
    with open(md_path, encoding="utf-8") as f:
        src = f.read()
    body = markdown.markdown(src, extensions=["tables", "md_in_html", "attr_list", "sane_lists"])
    body = tagify(body)
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title>"
            f"<style>{CSS}</style></head><body>"
            f"<div class='wm'>{watermark}</div>"
            f"<div class='content'>{body}</div></body></html>")


def print_pdf(html_path, pdf_path, footer):
    """Render with Playwright driving the pre-installed Chromium (gives real page footers)."""
    from playwright.sync_api import sync_playwright
    foot = ("<div style='width:100%;font-family:Arial,sans-serif;font-size:7.5px;color:#991b1b;"
            "text-align:center;padding:0 12mm;'>" + footer +
            " &nbsp;·&nbsp; page <span class='pageNumber'></span> of <span class='totalPages'></span></div>")
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        pg = b.new_page()
        pg.goto("file://" + html_path, wait_until="networkidle")
        pg.pdf(path=pdf_path, format="A4", print_background=True, display_header_footer=True,
               header_template="<div></div>", footer_template=foot,
               margin={"top": "14mm", "bottom": "16mm", "left": "14mm", "right": "14mm"})
        b.close()
    if not os.path.exists(pdf_path):
        sys.exit("PDF generation failed")


def check_consistency():
    with open(os.path.join(ROOT, "figures", "mock_values.json")) as f:
        mv = json.load(f)
    with open(os.path.join(ROOT, "docs", "01_PROTOTYPE_REPORT.md"), encoding="utf-8") as f:
        rep = f.read()

    def v(x):
        return f"{x:.2f} V" if x >= 1 else f"{x * 1e3:.0f} mV"
    expect = []
    for key in ("sine_min", "sine_max", "bench_min", "bench_max"):
        d = mv[key]
        row = f"| **{v(d['vin_pp'])}** | **{v(d['vout_pp'])}** | **{d['vout_pp'] / d['vin_pp']:.2f} V/V** |"
        expect.append(row)
    missing = [e for e in expect if e not in rep]
    if missing:
        sys.exit("Report tables disagree with figures/mock_values.json:\n" + "\n".join(missing))
    print("consistency check passed:", len(expect), "measurement tables match the mock screens")


DATA_SHEET = r"""
# EEEN20020 Experiment 2 — Bench data sheet

Names: {B50} / {B50} &nbsp; Bench: {B15} &nbsp; Date: {B10} / {B10} / 2026

**Design:** R1max = 50 kΩ (trimmer code 503) · R2 = 10 kΩ · R3 = 10 kΩ · expected A<sub>Vmin</sub> = 1.00, A<sub>Vmax</sub> = 6.00 (**must measure ≥ 5**)

### 1. Components — measure OUT OF CIRCUIT before inserting (needed for Section G)

| Item | Nominal | Measured (DMM) | Notes |
|---|---|---|---|
| R1max — pot at max (wiper ↔ end used) | 50 kΩ | | |
| R1min — pot at min (wiper ↔ end used) | ≈ 0 Ω | | |
| Pot end-to-end | 50 kΩ | | |
| R2 | 10 kΩ | | bands: |
| R3 | 10 kΩ | | bands: |

### 2. Supplies and set-up

| Pin 7 (V<sub>S+</sub>) | Pin 4 (V<sub>S−</sub>) | Pin 6 DC, no input | PSU current (+ / −) | Generator: 1 kHz · 1.000 Vpp · 0 V offset · **HighZ** |
|---|---|---|---|---|
| | | | / | ☐ checked |

**Table I colours:** V<sub>S+</sub> {B25} V<sub>S−</sub> {B25} GND {B25} v<sub>in</sub> {B25} v<sub>out</sub> {B25}

### 3. Measurements (gain = CH2 ÷ CH1, from the SAME screen)

| Test | V/div CH1 / CH2 | t/div | Vpp CH1 (in) | Vpp CH2 (out) | Gain | RMS CH1 | RMS CH2 | RMS gain | Photo |
|---|---|---|---|---|---|---|---|---|---|
| Sine, min gain | / | | | | | | | | P3 |
| Sine, max gain | / | | | | | | | | P4 |
| Channel-swap check (min) | / | | | | | | | | — |
| Bench, min gain (STOP) | / | | | | | | | | P5 |
| Bench, max gain (STOP) | / | | | | | | | | P6 |

Headphones connected during bench captures?  ☐ Yes  ☐ No

### 4. Audio and Demonstrator

| Is the signal audible and free of distortion? (Demonstrator's answer) | ☐ Yes ☐ No | Initials: |
|---|---|---|
| What we heard at A<sub>V</sub> = 1 | | |
| What we heard at A<sub>Vmax</sub> | | |

### 5. Photo shot-list (two of each, check focus before dismantling)

☐ P1 breadboard top-down  ☐ P2 whole set-up (breadboard + PSU + generator + scope)  ☐ P3 sine min  ☐ P4 sine max  ☐ P5 bench min  ☐ P6 bench max  ☐ P7 DMM readings (optional)

### 6. Before leaving the bench

☐ A<sub>Vmin</sub> ≈ 1.00  ☐ **A<sub>Vmax</sub> ≥ 5**  ☐ peaks round (no clipping)  ☐ every number has a photo  ☐ R's measured  ☐ Demonstrator ticked  ☐ equipment returned  ☐ upload within 1 h — **both** students
"""

DS_CSS = CSS + r"""
.blank { display: inline-block; border-bottom: 1px solid #111827; height: 11pt; vertical-align: bottom; }
body { font-size: 10pt; }
td { height: 17pt; }
h1 { color: #111827; font-size: 15pt; }
h3 { margin-top: 9pt; }
"""


def main():
    check_consistency()
    os.makedirs(REP, exist_ok=True)
    html = md_to_html(os.path.join(ROOT, "docs", "01_PROTOTYPE_REPORT.md"),
                      "EEEN20020 Exp 2 — PROTOTYPE report", "PROTOTYPE — NOT FOR SUBMISSION")
    hp = os.path.join(REP, "prototype_report.html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write(html)
    print_pdf(hp, os.path.join(REP, "EEEN20020_Exp2_PROTOTYPE_REPORT.pdf"),
              "EEEN20020 Exp. 2 — PROTOTYPE EXEMPLAR, NOT FOR SUBMISSION — [PROTOTYPE] items are illustrative; "
              "[SIM-REF] items are ngspice, not LTspice")

    sheet = DATA_SHEET
    for n in (10, 15, 25, 50):
        sheet = sheet.replace("{B%d}" % n, f"<span class='blank' style='width:{n * 0.9:.0f}mm'></span>")
    body = tagify(markdown.markdown(sheet, extensions=["tables", "md_in_html"]))
    ds = (f"<!doctype html><html><head><meta charset='utf-8'><title>EEEN20020 Exp 2 data sheet</title>"
          f"<style>{DS_CSS}</style></head><body>{body}</body></html>")
    dp = os.path.join(REP, "data_sheet.html")
    with open(dp, "w", encoding="utf-8") as f:
        f.write(ds)
    print_pdf(dp, os.path.join(REP, "EEEN20020_Exp2_DATA_SHEET.pdf"),
              "EEEN20020 Exp. 2 — bench data sheet (fill in by hand during the lab)")
    print("built:", os.listdir(REP))


if __name__ == "__main__":
    main()
