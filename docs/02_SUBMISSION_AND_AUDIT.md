# EXACTLY WHAT I NEED TO MATCH

(Deliverable 15: the "copy this standard" checklist)

The prototype in [`01_PROTOTYPE_REPORT.md`](01_PROTOTYPE_REPORT.md) sets the standard. Tick each box when **your** version reaches it.

### Before the lab

**Calculations**

- [ ] A<sub>V</sub> = 1 + R1/R2 derived in one line from the ideal op-amp rules (i₋ = 0, v₋ = v₊).
- [ ] A<sub>Vmin</sub> = 1.00 and A<sub>Vmax</sub> = 1 + R1max/R2 evaluated with units, to 3 s.f.
- [ ] The R2 ≤ R1max/4 condition stated, with the tolerance margin quantified (worst case ≥ 5).
- [ ] Headroom check: A<sub>Vmax</sub> × 1 V pk-pk < ≈ 7 V pk-pk (741 on ±5 V).
- [ ] Expected values tabulated: 1 V pk-pk in → 1 V / 6 V pk-pk out; 100 mV pk-pk → 100 / 600 mV pk-pk; bench ≈ 150 mV → ≈ 0.9 V pk-pk.

**Component values**

- [ ] R1max = 50 kΩ (trimmer code **503**), R2 = 10 kΩ (brown-black-orange), R3 = 10 kΩ.
- [ ] Plan B written down (10 kΩ pot → R2 = 2.0 or 1.8 kΩ; 20 kΩ → 3.9 kΩ; 5 kΩ → 1.0 kΩ).

**LTspice simulations** (your own, in LTspice, not the ngspice reference)

- [ ] Both schematics drawn by you; uA741 model loading; node labels `in`, `inv`, `out`.
- [ ] `.tran` at 1 V pk-pk for min and max gain; `.meas` gives AV ≈ 1.000 and ≈ 6.000.
- [ ] Re-run at 100 mV pk-pk (lab sheet §A); gains identical.
- [ ] `.op` at vin = +0.5 V DC for both, giving the node-voltage and branch-current table.
- [ ] Your numbers agree with the [SIM-REF] values to about 4 s.f. (0.99996 / 5.9996; 50.08 µA / 50.00 µA; V(out) = 3.0039 V). If not, find out why before the lab.

**Screenshots** (white background, readable at 100 % zoom in the PDF)

- [ ] Schematic, min gain (values and directives visible).
- [ ] Schematic, max gain.
- [ ] Waveforms, min gain: V(in), V(out) plus a pane of I(R1), I(R2), I(R3).
- [ ] Waveforms, max gain: same.
- [ ] `.op` table, min and max (or the `.meas` error log for both).

**Expected results to carry into the lab** (write them on the data sheet)

- [ ] A<sub>Vmin</sub> 1.00 (accept 1.00–1.02).
- [ ] A<sub>Vmax</sub> 6.00 (accept 5.3–6.8; **must be ≥ 5**).
- [ ] Output 6 V pk-pk at max gain with round peaks.
- [ ] Bench input ≈ 0.1–0.2 V pk-pk.

**Report pre-build**

- [ ] Official template copied. Cover page typed except signatures and date.
- [ ] A and B pasted, with captions written.
- [ ] Every figure placeholder captioned in advance (only the numbers are left to fill).
- [ ] Commentary skeleton chosen from the decision tree below.
- [ ] G nominal row filled.

### During the lab

**Breadboard construction**

- [ ] Resistors and pot **measured out of circuit before insertion** (R1min, R1max, end-to-end, R2, R3).
- [ ] 741 straddles the channel, pin 1 identified; pin 7 → +5 V, pin 4 → −5 V.
- [ ] Feedback to **pin 2**; R3 from pin 3 to GND; pot uses wiper + one end.
- [ ] Colour code followed; Table I recorded.

**Power checks**

- [ ] PSU 5 V / 5 V in series, current limit at "9 o'clock", output off while wiring.
- [ ] After power-on: pin 7 ≈ +5 V and pin 4 ≈ −5 V measured and **recorded**; supply currents a few mA.

**Signal-generator setup**

- [ ] Sine, 1.000 kHz, 1.000 Vpp, offset 0 V, **Load = HighZ**, coax red → Input, black → GND.

**Oscilloscope setup**

- [ ] CH1 = Input, CH2 = Output, ground connected, DC coupling, probe setting **1×**, BWL on.
- [ ] Vpp(1), Vpp(2), Freq(1) (+ RMS) displayed together; each trace ≥ 5 div, not clipped.

**Minimum-gain measurement**

- [ ] Pot at its end stop (CH2 smallest). Record Vpp(1) and Vpp(2). **Photo P3.**
- [ ] Gain calculated on the spot (1.00–1.02).
- [ ] Channel-swap check done and recorded.

**Maximum-gain measurement**

- [ ] Pot at the other end stop (CH2 largest). CH2 at 1 V/div. Round peaks confirmed.
- [ ] Record values. **Photo P4.** Gain **≥ 5** confirmed before moving on.

**Bench-signal measurement**

- [ ] Coax moved to BENCH TEST SIGNAL. Timebase 2–5 ms/div.
- [ ] RUN/STOP capture at min gain: Vpp and RMS on both channels. **Photo P5.**
- [ ] Same at max gain. **Photo P6.**
- [ ] Note whether the headphones were connected.

**Audio test**

- [ ] Listen at A<sub>V</sub> = 1, then at A<sub>Vmax</sub>; write down audibility, loudness change, and any hiss, buzz or harshness.

**Demonstrator verification**

- [ ] Demonstrator called early. Sine at both gains and the bench signal with audio shown.
- [ ] The Yes/No is **their** answer; initials if local practice.

**Photographs**

- [ ] P1 breadboard, P2 whole set-up (breadboard + PSU + generator + scope), P3–P6 scope screens.
- [ ] Two shots of each, all checked for focus **before** dismantling.

**Actual component measurements**

- [ ] R1min, R1max, R2, R3 on the data sheet, ideally with photos of the DMM readings (P7).

### Before submission

**Replace every prototype value with actual data**

- [ ] Every row of the replacement table below is done.
- [ ] Tripwire search returns nothing.

**Replace every prototype image with actual evidence**

- [ ] No mock screen, stand-in schematic, layout diagram or ngspice plot remains.
- [ ] Your photos and LTspice screenshots only.

**Verify every calculation**

- [ ] Each gain = Output ÷ Input from the **same** row.
- [ ] Recomputed with a calculator; 3 s.f.; % differences recomputed.

**Verify every table**

- [ ] A, B, D, E, F and G tables complete, with units on every value.
- [ ] F table matches A (design), B (simulation) and D (measurement) exactly.

**Verify every caption**

- [ ] Each figure has a number and a caption: what, configuration, scales, key readouts.
- [ ] Each caption's numbers match the photo.

**Complete the commentary**

- [ ] Percentages quoted; a mechanism with a size estimate for each difference.
- [ ] Irrelevant effects ruled out with a reason; G used if available; audio observation included.

**Complete the declaration**

- [ ] Names, student numbers (8 digits), date of the session; declaration text unaltered.

**Obtain signatures**

- [ ] Both students have signed, in the form your module accepts.

**Export to PDF**

- [ ] *File > Save as PDF* (not "print to image"); images embedded at full resolution.
- [ ] File name such as `EEEN20020_Exp2_<Surname1>_<Surname2>.pdf`.

**Check the PDF visually**

- [ ] Open it on another device.
- [ ] All pages present; photos readable at 100 %; no boxes split badly across pages; no GUIDANCE boxes or [tags] left.

**Upload the same joint report for both students**

- [ ] **Both** students upload the **identical** PDF to Brightspace, within **1 hour of the session end**.
- [ ] Each student checks their own submission receipt.

---

# PROTOTYPE → REAL REPORT REPLACEMENT SYSTEM

Every item that must be replaced, with its location in the prototype. Work down the list; nothing illustrative may survive.

| # | Prototype item (location) | Prototype content | Replace with | Where obtained |
|---|---|---|---|---|
| 1 | Cover: names, student numbers | `‹placeholders›` | Real names and 8-digit numbers | You |
| 2 | Cover: signatures, date | `‹placeholders›` | Signatures; date of the session | You |
| 3 | A: design table | 50 k / 10 k / 10 k / 1.00 / 6.00 **[KEEP]** | Keep, or Plan-B values if a different pot was used | Pre-lab design |
| 4 | Fig. A1 design schematic | Python drawing **[KEEP]** | Keep, or your own drawing / LTspice schematic | — |
| 5 | Fig. B1, B2 SPICE schematics | Stand-in drawings | **Your LTspice schematic screenshots** | LTspice |
| 6 | Fig. B3, B4 waveforms | ngspice plots **[SIM-REF]** | **Your LTspice waveform screenshots** | LTspice |
| 7 | Table B1 node voltages/currents | ngspice `.op` values | **Your LTspice `.op` table / `.meas` log** (screenshot or transcribed) | LTspice |
| 8 | B: SPICE gain table | 1.000 / 6.000 (0.99996 / 5.9996) | **Your LTspice `.meas` AV values** | LTspice |
| 9 | Fig. B5 AC response | ngspice, optional | Your LTspice `.ac` plot, **or delete** | LTspice |
| 10 | Fig. E1 breadboard | PROTOTYPE LAYOUT diagram | **Photo P1** of your actual circuit | Laboratory |
| 11 | Table I colours | Red/Black/Green/Yellow/Blue | Your actual socket colours | Laboratory |
| 12 | Supply verification | +5.02 V / −5.01 V / +3 mV | Your DMM readings (or delete the optional table) | Multimeter |
| 13 | Fig. D1 set-up | Block diagram | **Photo P2**: breadboard + PSU + generator + scope | Laboratory |
| 14 | Fig. D2 scope, sine, min | Mock screen | **Photo P3** | Oscilloscope |
| 15 | D min table | 1.01 V / 1.02 V / 1.01 | Your Vpp(1), Vpp(2), calculated gain | Oscilloscope + calculation |
| 16 | Fig. D3 scope, sine, max | Mock screen | **Photo P4** | Oscilloscope |
| 17 | D max table | 1.01 V / 5.88 V / 5.82 | Your values | Oscilloscope + calculation |
| 18 | Fig. E2 scope, bench, min | Mock screen | **Photo P5** | Oscilloscope |
| 19 | E min table | 148 mV / 150 mV / 1.01 | Your values | Oscilloscope + calculation |
| 20 | Fig. E3 scope, bench, max | Mock screen | **Photo P6** | Oscilloscope |
| 21 | E max table | 162 mV / 928 mV / 5.73 | Your values | Oscilloscope + calculation |
| 22 | All D/E captions and "Working" lines | Prototype numbers | Your numbers and observations | Report analysis |
| 23 | F: Demonstrator Yes/No | ☒ Yes (hypothetical) | **The Demonstrator's actual answer** | Demonstrator |
| 24 | F: summary table, Simulation row | 1.000 / 6.000 | Your LTspice gains | LTspice |
| 25 | F: summary table, Measurement row | 1.01 / 5.82 | Your sine gains from D | Laboratory calculation |
| 26 | F: commentary | Model text built on prototype numbers | **Final data-based commentary** (decision tree below) | Report analysis |
| 27 | F: scope accuracy figure | "±2 % assumed" | HMO1002 data-sheet value (cite it) | R&S data sheet |
| 28 | F: audio analysis | Hypothetical outcome | What you and the Demonstrator actually heard | Laboratory |
| 29 | G: measured R1max / R1min | 47.62 kΩ / 35 Ω | Your DMM readings of the pot (wiper to the used end) | Multimeter |
| 30 | G: measured R2 | 9.93 kΩ | Your DMM reading | Multimeter |
| 31 | G: measured R3 | 9.97 kΩ | Your DMM reading | Multimeter |
| 32 | G: calculated AV from measured R | 1.0035 / 5.796 | Recalculate from your readings | Calculation |
| 33 | G: re-sim schematic (Fig. G1) | Stand-in with prototype `.param` | Your LTspice screenshot with **your** `.param` values | LTspice |
| 34 | G: re-sim output (Figs. G2, G3, table) | ngspice on prototype values | Your LTspice output | LTspice |
| 35 | G: predicted vs measured table | 1.0035 / 5.795 vs 1.01 / 5.82 | Your LTspice and measured values | LTspice + Laboratory |
| 36 | G: commentary | Model text | Your data-based commentary | Report analysis |
| 37 | GUIDANCE boxes, notice box, Appendices P1/P2, all [tags] | Exemplar scaffolding | **Delete** | — |

**Tripwire search.** Before exporting, use *Ctrl+F* in your document for each of these strings. Each is a distinctive prototype value or label. **Every hit must be either deleted or confirmed as your own identical reading.**

`PROTOTYPE` · `ILLUSTRATIVE` · `GUIDANCE` · `SIM-REF` · `KEEP]` · `ngspice` · `stand-in` · `MOCK` · `47.62` · `9.93` · `9.97` · `35 Ω` · `5.82` · `5.88` · `1.02 V` · `148 mV` · `150 mV` · `162 mV` · `928 mV` · `5.73` · `157.9` · `27.2` · `24.8` · `+5.02` · `−5.01` · `5.795` · `1.0035` · `5.785` · `±2 % assumed`

---

# COMMENTARY DECISION TREE (adapt the F commentary to your real numbers in 10 minutes)

Compute: **d<sub>max</sub> = (A<sub>Vmax,meas</sub> − A<sub>Vmax,sim</sub>)/A<sub>Vmax,sim</sub> × 100 %**, and the same for d<sub>min</sub>.

| Your result | Diagnosis | Paragraph to write (fill in the brackets) |
|---|---|---|
| \|d<sub>max</sub>\| ≤ 3 % | Excellent agreement | "Measured A<sub>Vmax</sub> [x] V/V is within [d] % of the simulated [y] V/V. This is inside the ≈ ±3 % ratio uncertainty of the oscilloscope and well inside the ±12.5 % allowed by component tolerances, so no systematic discrepancy is detectable." Then point (d)–(g) as in the prototype. |
| 3 % < \|d<sub>max</sub>\| ≤ 13 % | Component tolerance | "The [d] % difference is consistent with tolerance: ΔA<sub>V</sub>/A<sub>V</sub> = 0.83(ΔR1/R1 − ΔR2/R2) …" **Use G**: "with measured R1max = [ ] and R2 = [ ], the prediction becomes [ ], within [ ] %." |
| A<sub>Vmax</sub> < 5 or \|d<sub>max</sub>\| > 13 % | Fault, which **must be fixed in the lab** | Look for clipping (flat tops: 50 Ω mode, input too large), the wrong pot (code), the pot not at its end stop, the wrong R2, or the scope probe at 10×. Fix it, re-measure, and report the fix honestly. |
| A<sub>Vmin</sub> 1.00–1.02 | Normal | "Within [ ] % of unity; pot end resistance (R1min = [ ] Ω → 1 + R1min/R2 = [ ]) and channel mismatch account for it." |
| A<sub>Vmin</sub> 1.02–1.06 | End resistance or channel mismatch | Use the channel-swap result and the measured R1min to separate the two. |
| A<sub>Vmin</sub> > 1.06 or < 0.98 | Setting or reading error | Pot not at its end stop, or misread V/div. Re-measure. |
| Bench Vpp gain within ±5 % of the sine gain | Normal | "Vpp of a non-repetitive signal is an extreme-value statistic; the RMS ratio [ ] agrees with the sine gain to [ ] %." |
| Bench gain differs by > 5 % | Method issue | Were input and output from the same capture? Was a trace clipped off-screen? Was V/div too fine? Explain or re-capture. |
| Distortion heard at max gain | Current limit / clipping | "Low-impedance headphones demand [Vpk/R] mA; the 741 limits at ≈ 25 mA …" Link it to flat tops on CH2 if visible. |
| Hum or buzz heard | Grounding | Open ground or a ground loop; check the coax shield and scope ground. Report it honestly. |

---

# ZERO-MARK-LEFT-ON-THE-TABLE AUDIT

(Deliverable 16: a hypothetical examiner audit against the official template)

**Question audited:** if the student reproduced the technical standard shown in the prototype, completed every required section correctly, replaced all prototype data with genuine experimental data, and submitted all required evidence, would any identifiable requirement in the supplied marking scheme remain unaddressed?

**Basis:** the official template gives **section totals only**: A 5, B 10, E (construction) 4, D 18, E (bench) 14, F 9; G is optional. The per-item splits below are **inferred** from the template's structure; they are not published. No grade is guaranteed. Marking judgement, local conventions and the Demonstrator's assessment are outside this audit.

### Cover / declaration (gate, 0 marks)

| What earns it | Where the prototype shows it | What you must do physically | What could lose it |
|---|---|---|---|
| Complete identity block, unaltered declaration, two signatures, date | Cover table with placeholders and guidance | Type names and numbers; both sign; date the session | Missing signature or student number; edited declaration; wrong module code (EEEN20040 file name) |

### A — Amplifier design [5]

| Likely mark | What earns it | Where the prototype earns it | Physical action to preserve it | What could lose it |
|---|---|---|---|---|
| 1 | R1max is a real available pot value | 50 kΩ (code 503) | Fetch the 503 trimmer | A value that is not 5/10/20/50 kΩ |
| 1 | R2 consistent with A<sub>Vmax</sub> ≥ 5 | 10 kΩ ≤ 12.5 kΩ, with margin analysis | Fetch 10 kΩ (brown-black-orange) | R2 too large (A<sub>Vmax</sub> < 5); value not stocked |
| 1 | Sensible R3 | 10 kΩ, role explained | — | R3 omitted or ≪ 1 kΩ |
| 1 | A<sub>Vmin</sub> = 1 | 1.00 V/V | — | 0, blank, or missing units |
| 1 | A<sub>Vmax</sub> = 1 + R1max/R2, ≥ 5 | 6.00 V/V, worked | — | Arithmetic error; inconsistency with B/F |

**Verdict:** fully addressed.

### B — Simulation of nominal design [10]

| Likely mark | What earns it | Where the prototype earns it | Physical action | What could lose it |
|---|---|---|---|---|
| ≈ 2 | Min-gain schematic | Fig. B1 + config table + `.asc` file | Draw it in LTspice and screenshot | Unreadable; values missing; not your own |
| ≈ 2 | Max-gain schematic | Fig. B2 | Same | Same |
| ≈ 2 | Min-gain SPICE output (waveforms + node V + branch I) | Fig. B3 + Table B1 | Run `.tran` and `.op`; screenshot both | Waveforms only (no currents or node values); no axes |
| ≈ 2 | Max-gain SPICE output | Fig. B4 + Table B1 | Same | Same |
| ≈ 2 | Predicted gains (nominal) | 1.000 / 6.000 table | Read the `.meas` AV | Gains not from SPICE; disagree with the figures |

**Verdict:** fully addressed. The prototype over-covers the ambiguous "node voltages and branch currents" requirement by including **both** `.op` and transient values.

### E — Amplifier construction [4]

| Likely mark | What earns it | Where the prototype earns it | Physical action | What could lose it |
|---|---|---|---|---|
| ≈ 2 | Photo present, clear, complete | Fig. E1 (spec) | Photo P1: top-down, in focus | Blurred, partial or dark photo |
| ≈ 2 | Neat, correct layout matching the schematic | Layout + Table I + caption | Build tidily with the colour code; label parts in the caption | Rat's-nest wiring; layout not matching the design |

**Verdict:** fully addressed, provided the photo is genuine and good.

### D — Sinusoidal measurements [18]

| Likely mark | What earns it | Where the prototype earns it | Physical action | What could lose it |
|---|---|---|---|---|
| ≈ 4 | Set-up photo showing all four instruments | Fig. D1 (spec) | Photo P2 with breadboard, PSU, generator and scope **in one frame** | Any instrument missing, especially the generator |
| ≈ 4 | Min-gain scope photo | Fig. D2 + Appendix P1 spec | Photo P3 with both traces and readouts legible | Single trace; readouts cut off; glare |
| ≈ 3 | Min-gain table (in, out, gain) | D min table + working | Record and divide | Units missing; gain ≠ out/in; numbers not in the photo |
| ≈ 4 | Max-gain scope photo | Fig. D3 | Photo P4 | Clipped waveform; CH2 off-screen |
| ≈ 3 | Max-gain table, A<sub>Vmax</sub> ≥ 5 | D max table | Record; **confirm ≥ 5** | A<sub>Vmax</sub> < 5 left unfixed |

**Verdict:** fully addressed. The set-up photo is the most commonly forgotten item; it is on the shot-list as P2.

### E — Bench test signal [14]

| Likely mark | What earns it | Where the prototype earns it | Physical action | What could lose it |
|---|---|---|---|---|
| ≈ 4 | Min-gain bench screen photo | Fig. E2 | RUN/STOP capture, photo P5 | Running (blurred) capture; readouts absent |
| ≈ 3 | Min-gain table | E min table | Values from the **same** capture | Input and output from different captures |
| ≈ 4 | Max-gain bench screen photo | Fig. E3 | Photo P6 | Output clipped off-screen |
| ≈ 3 | Max-gain table | E max table + RMS cross-check | Same | Gain inconsistent with the photo |

**Verdict:** fully addressed.

### F — Summary and commentary [9]

| Likely mark | What earns it | Where the prototype earns it | Physical action | What could lose it |
|---|---|---|---|---|
| ≈ 2 | Demonstrator confirms audible and undistorted | Yes/No row (hypothetical) | Working amplifier shown to the Demonstrator; headphones tested | No Demonstrator check (cannot be recovered after the session); a genuinely distorted output |
| ≈ 3 | Complete 3 × 2 summary table | F table | Copy from A, B and D | Mismatch with earlier sections; missing simulation row |
| ≈ 4 | Commentary: how closely they match, with differences explained | Full model commentary + box version + decision tree | Rewrite around your own numbers | Listing error sources without size or mechanism; no percentages; ignoring a large discrepancy |

**Verdict:** fully addressed. The Demonstrator item depends on an event you must make happen in the lab: call them early.

### G — Optional [unmarked]

| What earns credit | Where the prototype shows it | Physical action | Risk |
|---|---|---|---|
| Measured R values, re-simulation, comparison, commentary | Full worked G with hypothetical values | Measure R1min, R1max, R2 and R3 **before dismantling**; re-run LTspice | Measuring in circuit (wrong values); submitting the hypothetical values |

### Overall audit verdict

**No requirement in the supplied template is left unaddressed** by the standard shown, *on the stated condition* that every prototype item is replaced with genuine evidence. Five residual risks remain outside the document's control:

1. the Demonstrator check must actually happen during the session;
2. photo quality and legibility are decided at the bench;
3. a measured A<sub>Vmax</sub> < 5 must be fixed in the lab, not explained afterwards;
4. the scope's accuracy figure should be cited from the HMO1002 data sheet;
5. the one-hour upload deadline.

The fact that the per-item mark split is unpublished does not change this conclusion, because every box the template contains is filled to a standard that exceeds its literal request.
