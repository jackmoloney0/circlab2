# EEEN20020 Experiment 2: Audio Amplifier Design (prototype pack)

A complete pre-lab and exemplar pack for the UCD EEEN20020 Lab 2 (741 variable-gain non-inverting amplifier, ±5 V). It is built against the lab sheet *REV1 10/26 MPK* and the official report template *(10/26)*.

> **Honesty rules used throughout**
> - **[KEEP]**: genuine pre-lab design or calculation. Check it, then use it.
> - **[SIM-REF]**: a real SPICE result from **ngspice 42**, using the same netlist and uA741 model. **LTspice was not run here.** Replace it with your own LTspice output.
> - **[PROTOTYPE]**: an illustrative value, mock oscilloscope screen, mock layout or hypothetical observation. **Never submit it.** Replace it with your own measurements, photos and the Demonstrator's verdict.

## Read in this order

| # | File | What it is | Deliverables |
|---|---|---|---|
| 1 | [`docs/00_MASTER_PLAN.md`](docs/00_MASTER_PLAN.md) | **PHASE 1 master plan**: lab analysis, marking scheme, design, all calculations, LTspice design and procedure, simulation results, build and measurement procedure, troubleshooting, data sheets | 1–9 |
| 2 | [`report/EEEN20020_Exp2_PROTOTYPE_REPORT.pdf`](report/EEEN20020_Exp2_PROTOTYPE_REPORT.pdf) (source: [`docs/01_PROTOTYPE_REPORT.md`](docs/01_PROTOTYPE_REPORT.md)) | **FULL A++ PROTOTYPE REPORT**, section by section in template order, with figures, tables, model commentary, audio analysis, Section G and screenshot specifications | 10–14 |
| 3 | [`docs/02_SUBMISSION_AND_AUDIT.md`](docs/02_SUBMISSION_AND_AUDIT.md) | **Exactly what I need to match** (checklist); **prototype → real replacement table** with tripwire search list; **commentary decision tree**; **zero-mark-left-on-the-table audit** | 15–16 |
| 4 | [`report/EEEN20020_Exp2_DATA_SHEET.pdf`](report/EEEN20020_Exp2_DATA_SHEET.pdf) | Two-page bench sheet to print and fill in by hand | 9 |
| 5 | [`spice/ltspice/`](spice/ltspice/) | LTspice schematics (`.asc`), netlists (`.cir`) and the `uA741.lib` model | 4–5 |

## The design in one table  **[KEEP]**

| R1max | R2 | R3 | AVmin | AVmax | Output at AVmax for 1 Vpp in |
|---|---|---|---|---|---|
| 50 kΩ trimmer (code 503), wiper + one end | 10 kΩ | 10 kΩ | 1.00 V/V | 6.00 V/V (15.6 dB) | 6.0 Vpp (±3 V), no clipping on ±5 V |

R1max/R2 = 5 against the ≥ 4 required, a 25 % ratio margin. The worst case with a ±10 % trimmer and ±5 % R2 is AVmax = 5.29, still ≥ 5. The SPICE reference (ngspice) gives AV = 0.99996 and 5.9996.

## Folder map

```
docs/            master plan, prototype report (markdown), submission checklist + audit
report/          PDFs (prototype report, data sheet) and the HTML they are printed from
figures/         all figures; mock_values.json = the synthetic numbers shown on the mock screens
spice/ltspice/   LTspice .asc + .cir + uA741.lib  (keep together in one folder)
spice/ngspice/   generated ngspice decks used for the reference runs (re-runnable)
spice/results/   simulation data (.csv) and summary.json (every SIM-REF number)
tools/           scripts that regenerate everything
```

## Regenerating everything

```bash
sudo apt-get install -y ngspice
pip install matplotlib numpy schemdraw markdown playwright
python3 tools/make_ltspice.py   # LTspice .asc/.cir files
python3 tools/run_sims.py       # ngspice reference runs -> spice/results
python3 tools/make_figures.py   # figures (mock screens are seeded, so the numbers are stable)
python3 tools/build_pdfs.py     # checks report tables vs mock screens, then prints the PDFs
```

`build_pdfs.py` uses Chromium through Playwright. Set `CHROME=/path/to/chrome` if it is not at the default location.

## What this pack does **not** contain

- **No LTspice output.** LTspice was not available. The `.asc` files follow standard LTspice symbol geometry and were connectivity-checked with a parser, and the equivalent `.cir` netlists were verified by running them through ngspice. Open them in LTspice and produce your own screenshots.
- **No measurement data, photographs or Demonstrator results.** Every such item is a labelled prototype.
- **The UCD lab sheet and report template are not included.** Use your own copies from Brightspace.
