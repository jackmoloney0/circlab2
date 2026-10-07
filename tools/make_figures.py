#!/usr/bin/env python3
"""
Figures for the EEEN20020 Experiment 2 prototype report.

  * SPICE figures are drawn from ngspice output in spice/results (real
    simulation data, but ngspice -- not LTspice).
  * Oscilloscope screens, breadboard layout and bench set-up are MOCKS.
    Every mock carries a PROTOTYPE watermark and its numbers are written to
    figures/mock_values.json so the report tables match the mock screens.
    None of them is evidence that an experiment took place.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle

import schemdraw
import schemdraw.elements as elm

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "spice", "results")
FIG = os.path.join(ROOT, "figures")
os.makedirs(FIG, exist_ok=True)

YEL, CYN = "#f2e600", "#22d3ee"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})


def load(name):
    with open(os.path.join(RES, name + ".csv")) as f:
        hdr = f.readline().split()
    data = np.loadtxt(os.path.join(RES, name + ".csv"), skiprows=1)
    return {h: data[:, i] for i, h in enumerate(hdr)}


def watermark(fig, text, color="red", alpha=0.18, size=34):
    fig.text(0.5, 0.5, text, ha="center", va="center", rotation=22,
             fontsize=size, color=color, alpha=alpha, weight="bold",
             zorder=100)


# ============================================================ schematics ====
def amp_schematic(fname, r1_label, src_label=None, directives=None,
                  banner=None, show_pins=True, r2_label="R2\n10 kΩ",
                  r3_label="R3\n10 kΩ"):
    schemdraw.config(fontsize=11)
    d = schemdraw.Drawing(show=False)
    d.config(unit=2.4)
    # flipped so that '+' is on top and '-' at the bottom (as in lab-sheet Fig. 3)
    op = d.add(elm.Opamp(leads=True, sign=True).flip())
    top, bot = (op.vd, op.vs) if op.vd[1] > op.vs[1] else (op.vs, op.vd)
    if show_pins:
        d.add(elm.Label().at(op.in2).label("3", loc="center", ofst=(0.35, 0.25), fontsize=9))
        d.add(elm.Label().at(op.in1).label("2", loc="center", ofst=(0.35, -0.25), fontsize=9))
        d.add(elm.Label().at(op.out).label("6", loc="center", ofst=(-0.3, 0.25), fontsize=9))
    d.add(elm.Line().at(top).up(0.5))
    d.add(elm.Vdd().label("$V_{S+}$ = +5 V" + (" (pin 7)" if show_pins else "")))
    d.add(elm.Line().at(bot).down(0.5))
    d.add(elm.Vss().label("$V_{S-}$ = −5 V" + (" (pin 4)" if show_pins else ""), loc="bottom"))
    # non-inverting input + R3
    d.add(elm.Line().at(op.in2).left(2.8))
    d.add(elm.Dot())
    d.push()
    d.add(elm.Resistor().down(2.4).label(r3_label, loc="bottom"))
    d.add(elm.Ground())
    d.pop()
    if src_label:
        d.add(elm.Line().left(3.2))
        d.add(elm.Dot().label("in", loc="top"))
        d.push()
        d.add(elm.SourceSin().down(2.4).label(src_label, loc="top", ofst=0.25))
        d.add(elm.Ground())
        d.pop()
    else:
        d.add(elm.Line().left(1.6))
        d.add(elm.Dot(open=True).label("$v_{in}$\n(Input)", loc="left"))
    # output + feedback divider
    d.add(elm.Line().at(op.out).right(1.2))
    nout = d.here
    d.add(elm.Dot())
    d.add(elm.Line().right(1.2))
    d.add(elm.Dot(open=True).label("$v_{out}$\n(Output)" if not src_label else "out", loc="right"))
    d.add(elm.ResistorVar().at(nout).down(2.6).label(r1_label, loc="bottom", ofst=0.15))
    njn = d.here
    d.add(elm.Dot())
    d.add(elm.Resistor().down(2.4).label(r2_label, loc="bottom"))
    d.add(elm.Ground())
    xfb = op.in1[0] - 0.7
    d.add(elm.Line().at(njn).tox(xfb))
    d.add(elm.Line().toy(op.in1))
    d.add(elm.Line().tox(op.in1))
    d.add(elm.Label().at(((xfb + nout[0]) / 2, njn[1] - 0.38)).label(
        "inv (pin 2 node)" if show_pins else "inv", loc="center", fontsize=9))
    if directives:
        x0, y0 = op.in2[0] - 7.4, njn[1] - 3.9
        for i, t in enumerate(directives):
            d.add(elm.Label().at((x0, y0 - 0.55 * i)).label(t, loc="right", fontsize=9.5, color="#1d4ed8"))
    if banner:
        d.add(elm.Label().at((op.in2[0] - 7.4, top[1] + 2.2)).label(banner, loc="right", fontsize=10, color="#b91c1c"))
    d.save(os.path.join(FIG, fname), dpi=200)


def schematics():
    amp_schematic("fig_A_design_schematic.png",
                  "R1\n0–50 kΩ\ntrimmer")
    dirs = [".tran 0 6m 0 1u   .lib uA741.lib   .param Vpk=0.5",
            ".meas TRAN Vin_pp PP V(in) FROM 2m TO 6m",
            ".meas TRAN Vout_pp PP V(out) FROM 2m TO 6m",
            ".meas TRAN AV PARAM Vout_pp/Vin_pp"]
    amp_schematic("fig_B_spice_schematic_min.png", "R1 = 1 mΩ\n(pot at min ≈ 0 Ω)",
                  src_label="Vsig\nSINE(0 {Vpk} 1k)\n1 V pk-pk, 1 kHz",
                  directives=["U1 = uA741 (opamp2 symbol)   VCC = +5 V   VEE = −5 V"] + dirs,
                  banner="STAND-IN DRAWING of exp2_nominal_min_gain.asc — replace with your LTspice screenshot",
                  show_pins=False)
    amp_schematic("fig_B_spice_schematic_max.png", "R1 = 50 kΩ\n(pot at max)",
                  src_label="Vsig\nSINE(0 {Vpk} 1k)\n1 V pk-pk, 1 kHz",
                  directives=["U1 = uA741 (opamp2 symbol)   VCC = +5 V   VEE = −5 V"] + dirs,
                  banner="STAND-IN DRAWING of exp2_nominal_max_gain.asc — replace with your LTspice screenshot",
                  show_pins=False)
    amp_schematic("fig_G_spice_schematic_meas.png", "R1 = {R1min_m} / {R1max_m}\n(measured pot)",
                  src_label="Vsig\nSINE(0 {Vpk} 1k)\n1 V pk-pk, 1 kHz",
                  directives=[".param R1min_m=35 R1max_m=47.62k R2_m=9.93k R3_m=9.97k   <-- PROTOTYPE values",
                              "R1 = {R1min_m} in exp2_measured_min_gain.asc, {R1max_m} in exp2_measured_max_gain.asc"] + dirs[:1],
                  r2_label="R2\n{R2_m}", r3_label="R3\n{R3_m}",
                  banner="STAND-IN DRAWING of exp2_measured_*.asc — PROTOTYPE resistor values, NOT measurements",
                  show_pins=False)


# ======================================================= SPICE waveforms ====
def sim_wave(fname, case, title, tag):
    D = load(case)
    t = D["time"] * 1e3
    m = (t >= 2.0) & (t <= 6.0)
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(8.6, 5.6), sharex=True,
                                 gridspec_kw={"height_ratios": [1.5, 1]})
    a1.plot(t[m], D["v(in)"][m], color="#2563eb", lw=1.8, label="V(in)  — input")
    a1.plot(t[m], D["v(out)"][m], color="#dc2626", lw=1.8, label="V(out) — output")
    a1.plot(t[m], D["v(inv)"][m], color="#6b7280", lw=1.1, ls="--", label="V(inv) — pin 2")
    with open(os.path.join(RES, "summary.json")) as f:
        meas = json.load(f)[case]          # .meas results from the full-resolution run
    vin_pp, vout_pp = meas["vinpp"], meas["voutpp"]
    a1.set_ylabel("Voltage (V)")
    a1.grid(alpha=0.35)
    a1.legend(loc="upper right", fontsize=8.5, ncol=3, framealpha=0.9)
    a1.set_title(title, fontsize=11)
    a1.text(0.01, 0.04, f"Vin,pp = {vin_pp:.4f} V    Vout,pp = {vout_pp:.4f} V    "
            f"AV = {vout_pp / vin_pp:.4f} V/V", transform=a1.transAxes, fontsize=9,
            bbox=dict(fc="white", ec="#9ca3af"))
    lim = max(abs(D["v(out)"][m]).max(), 0.55) * 1.35
    a1.set_ylim(-lim, lim)
    for k, c in (("@r1[i]", "#16a34a"), ("@r2[i]", "#9333ea"), ("@r3[i]", "#ea580c")):
        a2.plot(t[m], D[k][m] * 1e6, color=c, lw=1.5 if k != "@r1[i]" else 2.6,
                alpha=0.95 if k != "@r1[i]" else 0.45,
                label=f"I({k[1:3].upper()})")
    a2.set_ylabel("Current (µA)")
    a2.set_xlabel("Time (ms)")
    a2.grid(alpha=0.35)
    a2.legend(loc="upper right", fontsize=8.5, ncol=3, framealpha=0.9)
    a2.set_ylim(-80, 80)
    fig.text(0.99, 0.005, f"ngspice-42 reference run of the same netlist ({tag}) — "
             "replace with your own LTspice plot", ha="right", fontsize=7.5, color="#b91c1c")
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(os.path.join(FIG, fname), dpi=200)
    plt.close(fig)


def sim_ac():
    fig, ax = plt.subplots(figsize=(8.6, 4.2))
    for case, lab, c, ls in (("ac_min", "min gain, no load", "#2563eb", "-"),
                             ("ac_max", "max gain, no load", "#dc2626", "-"),
                             ("ac_min_32ohm", "min gain, 32 Ω load", "#2563eb", ":"),
                             ("ac_max_32ohm", "max gain, 32 Ω load", "#dc2626", ":")):
        D = load(case)
        ax.semilogx(D["frequency"], 20 * np.log10(D["g"]), color=c, ls=ls, lw=1.8, label=lab)
    ax.axvspan(20, 20e3, color="#22c55e", alpha=0.08, label="audio band 20 Hz–20 kHz")
    ax.axvline(1e3, color="k", lw=0.8, ls="--")
    ax.text(1.05e3, -9, "1 kHz test\nfrequency", fontsize=8)
    ax.set_xlim(10, 1e7); ax.set_ylim(-12, 20)
    ax.set_xlabel("Frequency (Hz)"); ax.set_ylabel("|Vout/Vin| (dB)")
    ax.grid(which="both", alpha=0.3)
    ax.legend(fontsize=8, loc="lower left")
    ax.set_title("Closed-loop frequency response (uA741 macromodel, ±5 V)", fontsize=11)
    fig.text(0.99, 0.01, "ngspice-42 AC analysis — supplementary, optional in the report",
             ha="right", fontsize=7.5, color="#b91c1c")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(os.path.join(FIG, "fig_B_sim_ac.png"), dpi=200)
    plt.close(fig)


def sim_clip():
    D = load("tran2vpp_max_clip")
    t = D["time"] * 1e3
    m = (t >= 2) & (t <= 5)
    fig, ax = plt.subplots(figsize=(8.6, 3.6))
    ax.plot(t[m], D["v(in)"][m], color="#2563eb", lw=1.6, label="V(in): 2 V pk-pk (generator left in 50 Ω mode)")
    ax.plot(t[m], 6 * D["v(in)"][m], color="#dc2626", lw=1, ls="--", label="ideal 6 × V(in) = 12 V pk-pk")
    ax.plot(t[m], D["v(out)"][m], color="#dc2626", lw=2, label="V(out): clipped")
    ax.axhline(5, color="k", lw=0.8); ax.axhline(-5, color="k", lw=0.8)
    ax.text(2.02, 5.2, "+5 V rail", fontsize=8); ax.text(2.02, -5.6, "−5 V rail", fontsize=8)
    ax.set_ylim(-7, 7); ax.grid(alpha=0.3)
    ax.set_xlabel("Time (ms)"); ax.set_ylabel("Voltage (V)")
    ax.legend(fontsize=8, loc="upper right", ncol=1)
    ax.set_title("Pitfall: 2 V pk-pk at maximum gain drives the output into clipping", fontsize=11)
    fig.text(0.99, 0.01, "ngspice-42; a real 741 clips earlier (≈ ±3.5–4 V) than this macromodel (±4.6 V)",
             ha="right", fontsize=7.5, color="#b91c1c")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(os.path.join(FIG, "fig_pitfall_clipping.png"), dpi=200)
    plt.close(fig)


# ====================================================== mock oscilloscope ===
def quant(v, vdiv):
    lsb = vdiv / 25.0                      # ~8-bit over ~10 divisions
    return np.round(v / lsb) * lsb


def scope(fname, t, v1, v2, v1div, v2div, pos1, pos2, tdiv, state, meas, note, hdr=""):
    fig = plt.figure(figsize=(9.0, 5.9), facecolor="#d6d3d1")
    ax = fig.add_axes([0.07, 0.17, 0.86, 0.72], facecolor="#05070d")
    for x in range(-5, 6):
        ax.axvline(x, color="#4b5563", lw=0.6 if x else 0.9, ls=(0, (1, 3)) if x else "-")
    for y in range(-4, 5):
        ax.axhline(y, color="#4b5563", lw=0.6 if y else 0.9, ls=(0, (1, 3)) if y else "-")
    x = t / tdiv
    y1 = np.clip(v1 / v1div + pos1, -4.1, 4.1)
    y2 = np.clip(v2 / v2div + pos2, -4.1, 4.1)
    ax.plot(x, y1, color=YEL, lw=1.1)
    ax.plot(x, y2, color=CYN, lw=1.1)
    ax.text(-5.25, pos1, "1▸", color=YEL, va="center", ha="right", fontsize=10, weight="bold")
    ax.text(-5.25, pos2, "2▸", color=CYN, va="center", ha="right", fontsize=10, weight="bold")
    ax.set_xlim(-5, 5); ax.set_ylim(-4, 4)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color("#e5e7eb"); s.set_linewidth(1.2)
    fig.text(0.07, 0.905, f"TB: {tdiv_label(tdiv)}   T: 0 s", color="#111827", fontsize=10.5, family="DejaVu Sans Mono")
    fig.text(0.42, 0.905, f"CH1: ↗ Edge  DC", color="#a16207", fontsize=10.5, family="DejaVu Sans Mono")
    if hdr:
        fig.text(0.70, 0.905, hdr, color="#111827", fontsize=10.5, family="DejaVu Sans Mono")
    fig.text(0.93, 0.905, state, color="#b91c1c" if state == "STOP" else "#15803d",
             fontsize=11, weight="bold", ha="right", family="DejaVu Sans Mono")
    fig.text(0.07, 0.115, f"CH1: {v_label(v1div)}/div DC", color="#111827", fontsize=10,
             family="DejaVu Sans Mono", bbox=dict(fc=YEL, ec="none", pad=2))
    fig.text(0.07, 0.065, f"CH2: {v_label(v2div)}/div DC", color="#111827", fontsize=10,
             family="DejaVu Sans Mono", bbox=dict(fc=CYN, ec="none", pad=2))
    for i, line in enumerate(meas):
        fig.text(0.36 + 0.29 * (i // 2), 0.115 - 0.05 * (i % 2), line, fontsize=10,
                 family="DejaVu Sans Mono", color="#111827")
    fig.text(0.5, 0.012, note, ha="center", fontsize=8.2, color="#7f1d1d", weight="bold")
    fig.text(0.5, 0.955, "MOCK HMO1002-style screen  •  PROTOTYPE / ILLUSTRATIVE VALUES — REPLACE WITH ACTUAL MEASUREMENTS",
             ha="center", fontsize=8.6, color="#7f1d1d", weight="bold")
    watermark(fig, "PROTOTYPE — NOT A MEASUREMENT", color="#ef4444", alpha=0.32, size=30)
    fig.savefig(os.path.join(FIG, fname), dpi=170, facecolor=fig.get_facecolor())
    plt.close(fig)


def v_label(v):
    return f"{v * 1e3:g} mV" if v < 1 else f"{v:g} V"


def tdiv_label(t):
    return f"{t * 1e6:g} µs" if t < 1e-3 else f"{t * 1e3:g} ms"


def fmt_v(v):
    return f"{v * 1e3:.0f} mV" if v < 1 else f"{v:.2f} V" if v < 10 else f"{v:.1f} V"


def mocks():
    rng = np.random.default_rng(20020)
    # Hypothetical "truth" used to synthesise the screens (NOT measurements):
    G_MIN, G_MAX = 1.0035, 5.7952        # Section G resim with prototype R values
    K1, K2 = 1.008, 1.012                # assumed CH1/CH2 gain errors (+0.8 %, +1.2 %)
    sig = 0.006                          # trace noise, in divisions
    out = {}

    def chan(v, k, vdiv):
        return quant(k * v + rng.normal(0, sig * vdiv, v.size), vdiv)

    # ---------- sinusoid 1 kHz, 1 V pk-pk set on generator -------------
    tdiv = 200e-6
    t = np.linspace(-5 * tdiv, 5 * tdiv, 2400)
    vin = 0.4990 * np.sin(2 * np.pi * 1000.0 * t)      # 0.998 Vpp at the amp input
    for cfg, g, v2div, p1, p2 in (("min", G_MIN, 0.2, 1.0, -1.0),
                                  ("max", G_MAX, 1.0, 0.0, 0.0)):
        c1 = chan(vin, K1, 0.2)
        c2 = chan(g * vin, K2, v2div)
        vpp1, vpp2 = np.ptp(c1), np.ptp(c2)
        r1, r2 = np.sqrt(np.mean(c1 ** 2)), np.sqrt(np.mean(c2 ** 2))
        vpp1r, vpp2r = round(vpp1, 2), round(vpp2, 2)
        out[f"sine_{cfg}"] = dict(vin_pp=vpp1r, vout_pp=vpp2r,
                                  gain=round(vpp2r / vpp1r, 2), gain_4sf=vpp2r / vpp1r,
                                  vin_rms=round(r1, 3), vout_rms=round(r2, 3),
                                  gain_rms=round(r2 / r1, 3), v1div=0.2, v2div=v2div,
                                  pos1=p1, pos2=p2, tdiv=tdiv)
        scope(f"fig_D_scope_sine_{cfg}.png", t, c1, c2, 0.2, v2div, p1, p2, tdiv, "RUN",
              [f"Vpp(1): {fmt_v(vpp1r)}", f"RMS(1): {fmt_v(r1)}",
               f"Vpp(2): {fmt_v(vpp2r)}", f"RMS(2): {fmt_v(r2)}"],
              f"Sinusoid 1 kHz, {'MINIMUM' if cfg == 'min' else 'MAXIMUM'} gain — "
              f"replace with a photo of YOUR oscilloscope screen", hdr="f(1): 1.000 kHz")

    # ---------- bench test signal (speech/music-like) --------------------
    tdiv = 5e-3
    t = np.linspace(-5 * tdiv, 5 * tdiv, 5000)

    def audio(seed):
        r = np.random.default_rng(seed)
        s = np.zeros_like(t)
        for f0 in r.uniform(95, 260, 3):              # voiced fundamentals
            for h in range(1, 9):
                s += r.uniform(0.2, 1) / h ** 1.1 * np.sin(2 * np.pi * f0 * h * t + r.uniform(0, 6.3))
        s *= 0.75 + 0.25 * np.sin(2 * np.pi * r.uniform(3, 6) * t + r.uniform(0, 6.3))
        s += 0.04 * r.normal(size=t.size)
        return s - s.mean()

    for cfg, g, target, v2div, p1, p2, seed in (("min", G_MIN, 0.148, 0.05, 2.0, -2.0, 7),
                                                 ("max", G_MAX * 0.998, 0.160, 0.2, 2.2, -1.6, 11)):
        s = audio(seed)
        s = s * target / np.ptp(s) / K1
        c1 = chan(s, K1, 0.05)
        c2 = chan(g * s, K2, v2div)
        vpp1, vpp2 = np.ptp(c1), np.ptp(c2)
        r1, r2 = np.sqrt(np.mean(c1 ** 2)), np.sqrt(np.mean(c2 ** 2))
        vpp1r, vpp2r = round(vpp1, 3), round(vpp2, 3)
        out[f"bench_{cfg}"] = dict(vin_pp=vpp1r, vout_pp=vpp2r,
                                   gain=round(vpp2r / vpp1r, 2), gain_4sf=vpp2r / vpp1r,
                                   vin_rms=round(r1, 4), vout_rms=round(r2, 4),
                                   gain_rms=round(r2 / r1, 3), v1div=0.05, v2div=v2div,
                                   pos1=p1, pos2=p2, tdiv=tdiv)
        scope(f"fig_E_scope_bench_{cfg}.png", t, c1, c2, 0.05, v2div, p1, p2, tdiv, "STOP",
              [f"Vpp(1): {fmt_v(vpp1r)}", f"RMS(1): {r1 * 1e3:.1f} mV",
               f"Vpp(2): {fmt_v(vpp2r)}", f"RMS(2): {r2 * 1e3:.1f} mV"],
              f"Bench test signal, {'MINIMUM' if cfg == 'min' else 'MAXIMUM'} gain, single "
              f"capture held with RUN/STOP — replace with a photo of YOUR screen")
    out["_note"] = ("Synthetic values for the PROTOTYPE report only. They were generated in "
                    "tools/make_figures.py and are NOT measurements.")
    with open(os.path.join(FIG, "mock_values.json"), "w") as f:
        json.dump(out, f, indent=2)
    return out


# ======================================================= breadboard mock ====
def breadboard():
    fig, ax = plt.subplots(figsize=(15, 8.6))
    ax.set_xlim(-11.5, 39.5); ax.set_ylim(-5.8, 19.8); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(FancyBboxPatch((0.3, -2.3), 26.4, 16.7, boxstyle="round,pad=0.1",
                                fc="#f5f5f0", ec="#9ca3af"))
    rows = {"j": 11, "i": 10, "h": 9, "g": 8, "f": 7, "e": 5, "d": 4, "c": 3, "b": 2, "a": 1}
    for c in range(1, 27):
        for r, y in rows.items():
            ax.add_patch(Rectangle((c - 0.13, y - 0.13), 0.26, 0.26, fc="#4b5563", ec="none"))
    ax.add_patch(Rectangle((0.5, 5.8), 26, 0.4, fc="#e5e7eb", ec="none"))
    for r, y in rows.items():
        ax.text(0.15, y, r, fontsize=7, va="center", color="#6b7280")
    for c in (1, 5, 10, 15, 20, 25):
        ax.text(c, 11.8, str(c), fontsize=7, ha="center", color="#6b7280")
        ax.text(c, 0.2, str(c), fontsize=7, ha="center", color="#6b7280")
    rails = {"V+": (13.6, "#dc2626"), "GNDt": (12.8, "#16a34a"),
             "GNDb": (-0.8, "#16a34a"), "V-": (-1.6, "#111827")}
    for k, (y, col) in rails.items():
        ax.plot([0.8, 26.2], [y + 0.32 * (1 if k in ("V+", "GNDb") else -1)] * 2, color=col, lw=1)
        for c in range(1, 27):
            ax.add_patch(Rectangle((c - 0.11, y - 0.11), 0.22, 0.22, fc="#6b7280", ec="none"))
    ax.text(26.5, 13.6, "+5 V rail", fontsize=8, va="center", color="#dc2626")
    ax.text(26.5, 12.8, "GND rail", fontsize=8, va="center", color="#16a34a")
    ax.text(26.5, -0.8, "GND rail", fontsize=8, va="center", color="#16a34a")
    ax.text(26.5, -1.6, "−5 V rail", fontsize=8, va="center", color="#111827")

    def wire(pts, col, lw=3.2):
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color="#111" if col != "#111827" else "#555", lw=lw + 1.6, solid_capstyle="round", zorder=5)
        ax.plot(xs, ys, color=col, lw=lw, solid_capstyle="round", zorder=6)
        for p in (pts[0], pts[-1]):
            ax.add_patch(Circle(p, 0.16, fc=col, ec="k", lw=0.6, zorder=7))

    def resistor(p0, p1, label, bands):
        wire([p0, p1], "#9ca3af", lw=1.6)
        mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
        L = 1.9
        horiz = abs(p1[0] - p0[0]) > abs(p1[1] - p0[1])
        w, h = (L, 0.55) if horiz else (0.55, L)
        ax.add_patch(FancyBboxPatch((mx - w / 2, my - h / 2), w, h, boxstyle="round,pad=0.05",
                                    fc="#d6c8a8", ec="#6b5b3e", zorder=8))
        for i, b in enumerate(bands):
            o = -L / 2 + 0.35 + 0.33 * i
            if horiz:
                ax.add_patch(Rectangle((mx + o, my - h / 2), 0.12, h, fc=b, zorder=9))
            else:
                ax.add_patch(Rectangle((mx - w / 2, my + o), w, 0.12, fc=b, zorder=9))
        return mx, my

    # 4 mm sockets
    socks = [(3, "#dc2626", "VS+  +5 V"), (7, "#16a34a", "GND (ref.)"), (11, "#111827", "VS−  −5 V"),
             (16, "#eab308", "Input  vin"), (21, "#2563eb", "Output  vout")]
    for x, col, lab in socks:
        ax.add_patch(Circle((x, 17.4), 0.75, fc=col, ec="k", lw=1.2, zorder=4))
        ax.add_patch(Circle((x, 17.4), 0.28, fc="#111", zorder=5))
        ax.text(x, 18.75, lab, ha="center", fontsize=8.5, weight="bold")
    # 741 DIP: notch left; bottom row e = pins 1-4 at cols 14-17, top row f = pins 8-5
    ax.add_patch(FancyBboxPatch((13.55, 5.25), 3.9, 1.5, boxstyle="round,pad=0.02",
                                fc="#1f2937", ec="k", zorder=8))
    ax.add_patch(Circle((13.55, 6.0), 0.28, fc="#f5f5f0", ec="k", zorder=9))
    ax.add_patch(Circle((14.0, 5.55), 0.09, fc="#e5e7eb", zorder=9))
    ax.text(15.55, 6.0, "741", color="white", ha="center", va="center", fontsize=10, weight="bold", zorder=10)
    for i, c in enumerate(range(14, 18)):
        ax.text(c, 4.52, str(i + 1), ha="center", fontsize=7.5, color="#1d4ed8", weight="bold", zorder=10)
        ax.text(c, 7.42, str(8 - i), ha="center", fontsize=7.5, color="#1d4ed8", weight="bold", zorder=10)
    # supply wiring
    wire([(3, 16.65), (3, 13.6)], "#dc2626")
    wire([(7, 16.65), (7, 12.8)], "#16a34a")
    wire([(11, 16.65), (11, 15.4), (0.9, 15.4), (0.9, -1.6)], "#111827")
    wire([(25.6, 12.8), (25.6, -0.8)], "#16a34a")
    wire([(15, 11), (15, 13.6)], "#dc2626")                      # pin 7 -> +5 V
    wire([(17, 1), (17, -1.6)], "#111827")                       # pin 4 -> -5 V
    # signal wiring
    wire([(16, 11), (16.6, 12.3), (20.3, 15.6), (21, 16.65)], "#2563eb")   # pin 6 -> Output
    wire([(16, 16.65), (16.0, 15.0), (19.9, 13.0), (19.9, 6.3), (19, 5)], "#eab308")  # Input -> col 19
    wire([(16, 2), (19, 2)], "#eab308", lw=2.6)                  # pin 3 col -> input hub
    wire([(16, 9), (8.2, 9), (5.6, 6.6), (5, 5)], "#f8fafc")      # pin 6 col -> pot end A
    wire([(6, 4), (15, 4)], "#f8fafc", lw=2.6)                   # pot wiper -> pin 2 col
    wire([(10, 1), (10, -0.8)], "#16a34a", lw=2.6)               # R2 ground column
    wire([(23, 1), (23, -0.8)], "#16a34a", lw=2.6)               # R3 ground column
    # resistors (brown-black-orange-gold = 10 kOhm 5 %)
    br = ["#7c2d12", "#111827", "#ea580c", "#ca8a04"]
    resistor((10, 3), (15, 3), "R2", br)
    resistor((19, 3), (23, 3), "R3", br)
    # trimmer pot: pins in row a at cols 5 (end A), 6 (wiper), 7 (end B, unused)
    ax.add_patch(Rectangle((4.45, 1.3), 3.1, 1.75, fc="#1d4ed8", ec="k", zorder=8))
    ax.add_patch(Circle((6, 2.18), 0.55, fc="#93c5fd", ec="k", zorder=9))
    ax.plot([5.65, 6.35], [1.83, 2.53], color="k", lw=2, zorder=10)
    for c in (5, 6, 7):
        ax.add_patch(Circle((c, 1), 0.16, fc="#d1d5db", ec="k", zorder=9))

    def callout(xy, xytext, text, ha):
        ax.annotate(text, xy=xy, xytext=xytext, fontsize=8.6, zorder=20, ha=ha, va="center",
                    arrowprops=dict(arrowstyle="->", color="#374151", lw=0.9,
                                    shrinkA=2, shrinkB=2),
                    bbox=dict(fc="white", ec="#9ca3af", alpha=0.97, boxstyle="round,pad=0.3"))
    L, R = -1.2, 28.9
    callout((0.9, 14.6), (L, 15.6), "black: VS− socket → −5 V rail\n(runs down the left edge)", "right")
    callout((7.0, 8.0), (L, 9.6), "white: output column 16\n→ pot end A (column 5)", "right")
    callout((5.0, 1.0), (L, 4.4), "R1 = 50 kΩ trimmer as a rheostat:\nend A (col 5) + wiper (col 6);\nend B (col 7) unconnected", "right")
    callout((10.0, 0.2), (L, -1.0), "green: column 10 → GND rail\n(ground end of R2)", "right")
    callout((25.6, 10.5), (R, 11.6), "green: top GND rail ↔ bottom\nGND rail link", "left")
    callout((17.4, 6.0), (R, 8.6), "741 straddles the channel;\nnotch + dot mark pin 1\n(row e, column 14)", "left")
    callout((14.2, 4.0), (R, 5.9), "white: pot wiper (col 6)\n→ pin 2 column 15", "left")
    callout((21.8, 3.25), (R, 3.9), "R3 = 10 kΩ: input column 19\n→ GND column 23", "left")
    callout((18.2, 2.0), (R, 2.0), "yellow: pin 3 column 16\n→ input column 19", "left")
    callout((17.0, -0.2), (R, -0.4), "black: pin 4 (col 17) → −5 V rail\nred: pin 7 (col 15) → +5 V rail", "left")
    callout((12.5, 2.75), (12.5, -3.7), "R2 = 10 kΩ: pin 2 column 15 → GND column 10", "center")
    ax.text(13.5, -5.2, "Table I colours: VS+ red • VS− black • GND green • vin yellow • vout blue",
            ha="center", fontsize=9, color="#111827")
    ax.set_title("Prototype breadboard layout — non-inverting amplifier, 741, ±5 V", fontsize=12)
    watermark(fig, "PROTOTYPE LAYOUT — REPLACE WITH\nPHOTOGRAPH OF ACTUAL CIRCUIT", color="#dc2626", alpha=0.20, size=30)
    fig.savefig(os.path.join(FIG, "fig_C_breadboard_prototype.png"), dpi=170, bbox_inches="tight")
    plt.close(fig)


def setup_diagram():
    fig, ax = plt.subplots(figsize=(11, 5.4))
    ax.set_xlim(0, 22); ax.set_ylim(0, 11); ax.axis("off")

    def box(x, y, w, h, title, sub, fc):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", fc=fc, ec="k"))
        ax.text(x + w / 2, y + h - 0.45, title, ha="center", fontsize=10.5, weight="bold")
        ax.text(x + w / 2, y + h - 1.0, sub, ha="center", fontsize=8.2, va="top")
    box(0.4, 6.4, 5.6, 4.0, "Dual DC power supply", "two 5 V sources in series\n(Fig. 5): red = +5 V,\ngreen = 0 V, black = −5 V\ncurrent limit at '9 o'clock'", "#e5e7eb")
    box(0.4, 1.2, 5.6, 3.8, "Rigol DG822 generator", "Sine, 1 kHz, 1 V pk-pk\nOutput load = HighZ\nBNC → 4 mm coax\n(red = signal, black = GND)", "#e0f2fe")
    box(8.2, 3.0, 5.6, 4.6, "Breadboard amplifier", "741 + R1 (50 kΩ trimmer)\n+ R2, R3 (10 kΩ)\n5 × 4 mm sockets:\nVS+ GND VS− Input Output", "#fef9c3")
    box(16.0, 3.0, 5.6, 4.6, "HMO1002 oscilloscope", "CH1 = Input (yellow lead)\nCH2 = Output (blue lead)\nblack = circuit GND\nAuto-measure: Vpp(1), Vpp(2),\nf(1), RMS(1), RMS(2)", "#ecfeff")

    def cable(pts, col, lw=3):
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=col, lw=lw, solid_capstyle="round")
    cable([(6.0, 9.6), (9.0, 9.6), (9.0, 7.6)], "#dc2626")
    cable([(6.0, 8.8), (10.0, 8.8), (10.0, 7.6)], "#16a34a")
    cable([(6.0, 8.0), (8.6, 8.0), (8.6, 7.6)], "#111827")
    cable([(6.0, 2.6), (8.2, 4.6)], "#dc2626")
    cable([(6.0, 2.0), (9.5, 2.0), (9.5, 3.0)], "#111827")
    cable([(13.8, 6.4), (16.0, 6.4)], "#eab308")
    cable([(13.8, 5.4), (16.0, 5.4)], "#2563eb")
    cable([(13.8, 4.2), (16.0, 4.2)], "#111827")
    ax.text(14.9, 6.6, "CH1", fontsize=8, ha="center"); ax.text(14.9, 5.6, "CH2", fontsize=8, ha="center")
    ax.text(14.9, 3.65, "GND", fontsize=8, ha="center")
    ax.text(11, 0.25, "Photo must show breadboard + power supply + signal source + oscilloscope in ONE frame",
            ha="center", fontsize=9, color="#111827", style="italic")
    watermark(fig, "PROTOTYPE DIAGRAM — REPLACE WITH\nPHOTO OF YOUR MEASUREMENT SET-UP", color="#dc2626", alpha=0.20, size=28)
    fig.savefig(os.path.join(FIG, "fig_D_setup_prototype.png"), dpi=170, bbox_inches="tight")
    plt.close(fig)


def main():
    schematics()
    sim_wave("fig_B_sim_min.png", "tran1vpp_min",
             "Nominal design, MINIMUM gain (R1 = 0): 1 V pk-pk, 1 kHz input", "R1 = 1 mΩ")
    sim_wave("fig_B_sim_max.png", "tran1vpp_max",
             "Nominal design, MAXIMUM gain (R1 = 50 kΩ): 1 V pk-pk, 1 kHz input", "R1 = 50 kΩ")
    sim_wave("fig_G_sim_min.png", "G_tran1vpp_min",
             "Section G resim, MIN gain, PROTOTYPE 'measured' R values (R1min = 35 Ω)", "PROTOTYPE values")
    sim_wave("fig_G_sim_max.png", "G_tran1vpp_max",
             "Section G resim, MAX gain, PROTOTYPE 'measured' R values (R1max = 47.62 kΩ)", "PROTOTYPE values")
    sim_ac()
    sim_clip()
    mv = mocks()
    breadboard()
    setup_diagram()
    print(json.dumps(mv, indent=1))


if __name__ == "__main__":
    main()
