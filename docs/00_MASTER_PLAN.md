# PHASE 1 — EEEN20020 EXPERIMENT 2 MASTER PLAN

**Experiment 2 — Audio Amplifier Design** (lab sheet *EEEN20020 Lab 2, REV1 10/26 MPK*; report template *EEEN20020 Laboratory Report, Experiment 2, 10/26*)

This file covers **Deliverables 1–9**. The fully worked exemplar report is in
[`01_PROTOTYPE_REPORT.md`](01_PROTOTYPE_REPORT.md), with a PDF version at [`../report/EEEN20020_Exp2_PROTOTYPE_REPORT.pdf`](../report/EEEN20020_Exp2_PROTOTYPE_REPORT.pdf).
The checklist, replacement table and examiner audit are in [`02_SUBMISSION_AND_AUDIT.md`](02_SUBMISSION_AND_AUDIT.md).

> ### Honesty legend used in every file of this pack
> | Tag | Meaning | What you do with it |
> |---|---|---|
> | **[KEEP]** | Genuine pre-lab design or calculation. It is true independent of the lab. | Check it, then use it. |
> | **[SIM-REF]** | A real SPICE result, produced with **ngspice 42** (not LTspice) on the same netlist and the same uA741 model. | Re-run in **LTspice** and paste *your* screenshot and numbers. They should agree to about 4 significant figures. |
> | **[PROTOTYPE]** | An illustrative or hypothetical value, mock screen, mock layout or hypothetical observation. | **Replace it** with your own measurement, photo or observation. **Never submit it.** |
>
> LTspice was **not** run in the environment that produced this pack, and no simulation here is presented as an LTspice output. No measurement here was taken by you.

---

## DELIVERABLE 1 — Complete laboratory analysis

### 1.1 What the experiment actually tests

You must design, simulate, build and characterise a **variable-gain, non-inverting op-amp amplifier** (741, ±5 V supplies).

- The gain must be adjustable with a potentiometer from **AV = 1 V/V** up to **at least 5 V/V**.
- You prove the gain range with a **1 kHz, 1 V pk-pk sinusoid**.
- You then use the amplifier on a real audio signal (the **Bench Test Signal**) and listen to it on headphones.

The marks reward four things:

1. **A correct design**, with the values stated.
2. **Simulation evidence**: schematics, waveforms, node voltages and branch currents, and gains.
3. **Measurement evidence**: photos, scope screens, Vpp tables and gains.
4. **Engineering judgement**: how well design, simulation and measurement agree, and why they differ.

### 1.2 Marking scheme (from the official report template)

The template's section letters are reproduced exactly, including its quirk, explained in §1.4.

| Template section | Marks | Evidence the template asks for | Type |
|---|---:|---|---|
| Cover / declaration | — (a gate, not marks) | Names, 8-digit student numbers, plagiarism and eye-protection declaration, both signatures, date `__/__/2026` | Admin |
| **A** Amplifier design (pre-lab) | **5** | Table: R1max, R2, R3, AVmin, AVmax | Pre-lab |
| **B** Simulation of nominal design (pre-lab) | **10** | (i) SPICE schematics for min and max gain; (ii) SPICE output, meaning **node voltages and branch currents**, for both; (iii) table of SPICE-predicted AVmin and AVmax with nominal values | Pre-lab |
| **E** Amplifier construction *(template says "E"; it is the lab sheet's stage C)* | **4** | Photo of the breadboard layout | In lab |
| **D** Amplifier measurements (sinusoidal) | **18** | (i) Photo of the **whole measurement set-up**: breadboard, power supplies, signal source and oscilloscope; (ii) scope photo at min gain plus a table (Input pk-pk, Output pk-pk, measured AVmin); (iii) scope photo at max gain plus a table (… measured AVmax) | In lab |
| **E** Amplifier measurements (bench test signal) | **14** | Scope photo at min gain plus table; scope photo at max gain plus table | In lab |
| **F** Summary and commentary | **9** | Demonstrator's Yes/No for "audible and free of distortion"; a 3 × 2 table (Design / Simulation / Measurement × AVmin / AVmax); commentary: "How closely do the designed, simulated and measured gains match? Explain any differences" | In lab and post-lab |
| **G** Optional (re-simulation with measured component values) | unmarked/bonus | Nominal vs measured R1max, R2, R3, AVmin, AVmax; re-simulation schematics and output; predicted vs measured gains; commentary | In lab and post-lab |
| **Total** | **60** | Lab 2 = 5 % of the module | |

**Where the marks concentrate:** D (18) + E bench (14) = **32 of 60 marks for in-lab evidence**. Most of that is photos and three-number tables.

The two cheapest ways to lose many marks are:

- a missing or illegible photo;
- a Vpp table that does not match the photo next to it.

### 1.3 Hard constraints you cannot negotiate

| Constraint | Source | Consequence for planning |
|---|---|---|
| PDF uploaded to Brightspace **no later than one hour after the end of the session** | Lab sheet §G | The report must be **95 % written before you walk in**. In the lab you only drop in photos and numbers and adapt the commentary. |
| **Both** students upload the **same joint** PDF | Lab sheet §G and template footer | One file, uploaded twice. Agree who exports the PDF. |
| Demonstrator must see the working amplifier and judge audio quality | Lab sheet §F/G, template §F | Book the Demonstrator **early**, as soon as the bench signal is on the scope. Queues form late in sessions. |
| Return breadboard, wires, op amp, pot and headphones; fixed resistors may be discarded | Lab sheet §G | Measure R1, R2 and R3 with the DMM **before** you dismantle (needed for Section G). |
| Eye protection | Declaration | Bring safety glasses; the declaration says you will wear them. |
| ±5 V supplies, current limit at "9 o'clock" | Lab sheet §C | Protects the 741 from wiring errors. |

### 1.4 Inconsistencies in the supplied documents, and how to handle them

| # | Inconsistency | Recommended handling |
|---|---|---|
| 1 | Lab sheet §A says simulate with a **100 mV pk-pk** sine. Lab sheet §B says **1 V pk-pk**. | Simulate **both**. Use **1 V pk-pk** for the report figures, because it matches the 1 V pk-pk used on the bench in §D, so simulation and measurement compare directly. Put the 100 mV pk-pk gains in one extra table row. The gains are identical (the circuit is linear), and saying so earns credit. |
| 2 | The template labels **construction "E"** and the bench measurements **"E"** again; the lab sheet calls construction stage **C**. | Keep the template **exactly as issued** and do not renumber. Examiners mark against their own template. |
| 3 | The lab sheet says AVmax "approximately 5". Section D and the marking test say "**at least 5 V/V**". | Design for **AVmax ≈ 6** so the *measured* AVmax is ≥ 5 even with component tolerances (§2.3). |
| 4 | The lab sheet's stages run A–G (listening is **F**, demonstration is **G**). The template's **F** is "Summary and commentary". | Map them: lab §F (listen) feeds the template's **F** Yes/No row; lab §E/§F bench measurements go in template **E (bench)**. |
| 5 | The template file is named "EEEN20040" but its header says **EEEN20020**. | Use **EEEN20020** everywhere. |
| 6 | The template asks for a **photo of the measurement set-up** (§D). The lab-sheet procedure never tells you to take it. | Put it on the photo shot-list (§8.9). It is part of an 18-mark section. |
| 7 | "SPICE output (node voltages and branch currents)" is not defined further. | Supply **both**: (a) the LTspice **.op** table at vin = +0.5 V (the peak of the 1 V pk-pk input), and (b) the **.meas** log of V(in), V(inv), V(out), I(R1), I(R2), I(R3) and supply currents at the waveform peak. This covers every reasonable reading of the requirement. |

### 1.5 What separates an A++ submission from a merely complete one

1. **Every number is traceable.** The value in each Vpp table is readable on the scope photo directly above it, and every gain is the quotient of the two numbers beside it.
2. **The design is justified, not just stated.** Explain *why* 50 kΩ and 10 kΩ, *why* about 6 rather than exactly 5, and *why* R3 is needed.
3. **Simulation is used as evidence.** Show the node voltages and branch currents, and *interpret* them. For example, I(R1) − I(R2) = 80 nA is the 741 input bias current, which is why R3 exists.
4. **Discrepancies are quantified with mechanisms**, not listed. Component tolerance gives roughly ±10 % on AVmax, finite loop gain gives about 0.002 % at 1 kHz, and supply variation gives zero.
5. **Section G is completed.** It turns "probably tolerances" into "with measured resistances the prediction agrees with the measurement to 0.4 %".

### 1.6 Timeline

**Before the lab**

| When | Task | Output |
|---|---|---|
| T−7 to T−5 days | Read this pack; confirm the design (§2); hand-check calculations (§3) | Section A complete |
| T−5 to T−3 | Install LTspice; draw both schematics yourselves (§5); run .tran, .op and .meas; take screenshots | Section B complete with **your** LTspice figures |
| T−3 to T−2 | Copy the official template; paste A and B; pre-write captions and the commentary skeleton (§F decision tree in `02_SUBMISSION_AND_AUDIT.md`); fill the nominal row of G | Report about 70 % complete |
| T−1 | Print the data sheet (`report/EEEN20020_Exp2_DATA_SHEET.pdf`); charge phones; pack a USB stick and safety glasses; agree roles | Ready |

**In the lab (2-hour session; scale to your actual session)**

| Minute | Student A | Student B |
|---:|---|---|
| 0–5 | Collect parts; **measure R2, R3 and the pot (min and max) with the DMM before inserting** | Set the PSU to 5 V / 5 V, current limit at "9 o'clock", output OFF; set the generator to 1 kHz, 1 Vpp, **Load = HighZ**, output OFF |
| 5–25 | Build on the breadboard (§7) | Fill in Table I colours; check every connection against the pin map |
| 25–30 | Photo **P1**: breadboard layout | Power on (generator still off); **DMM: pin 7 ≈ +5 V, pin 4 ≈ −5 V**; record |
| 30–45 | Generator on; scope set-up (§8.4); min gain: photo **P3** and record | Photo **P2**: whole set-up; record readings on the data sheet |
| 45–55 | Max gain: photo **P4** and record; check AVmax ≥ 5 | Calculate gains on the sheet immediately |
| 55–75 | Bench signal: min-gain capture (STOP): photo **P5** and record; max-gain capture: photo **P6** and record | **Call the Demonstrator now** |
| 75–85 | Headphones: listen at min, then max gain; Demonstrator ticks Yes/No | Note what you heard in your own words |
| 85–95 | Power off; re-measure the pot **as wired** (min/max, out of circuit) if not already done | Photo of DMM readings (optional evidence) |
| 95–120 | Return equipment; start pasting photos into the report | Start the G re-simulation with the measured values |
| End + 0–60 | Finish F commentary and G; proof-read; export PDF; **both upload** | Done |

---

## DELIVERABLE 2 — Complete pre-lab design  **[KEEP]**

### 2.1 Requirements turned into equations

The non-inverting amplifier of lab-sheet Fig. 6 has, for an ideal op amp (v₊ = v₋, i₊ = i₋ = 0):

$$A_V=\frac{v_{out}}{v_{in}}=1+\frac{R_1}{R_2}$$

- **AVmin**: with R1 = 0 (pot at minimum), AVmin = 1 exactly, independent of R2. The amplifier is a unity-gain buffer.
- **AVmax**: with R1 = R1max, AVmax = 1 + R1max/R2. The requirement AVmax ≥ 5 means **R2 ≤ R1max/4**.
- **R3**: provides the DC path for the 741's non-inverting-input bias current (about 80 nA typical) and sets the amplifier's input resistance. The lab sheet says around 10 kΩ.

### 2.2 Choosing the potentiometer: every option evaluated

Assumptions: trimmer tolerance ±10 % (typical cermet trimmers; some are ±20 %), fixed resistors ±5 %. "P(AV<5)" is the Monte-Carlo probability (uniform tolerances, 200,000 trials) that the **as-built** AVmax fails the ≥ 5 requirement.

| Pot R1max | R2 limit (R1max/4) | R2 choice | Nominal AVmax | Worst-case low (pot −10 %, R2 +5 %) | Worst-case low (pot −20 %) | Worst-case high (pot +20 %, R2 −5 %) | P(AV<5) ±10 % pot | P(AV<5) ±20 % pot |
|---|---|---|---:|---:|---:|---:|---:|---:|
| 5 kΩ | 1.25 kΩ | 1.2 kΩ | 5.17 | 4.57 ✗ | 4.18 ✗ | 6.26 | 30 % | 40 % |
| 5 kΩ | 1.25 kΩ | **1.0 kΩ** | **6.00** | 5.29 ✓ | 4.81 | 7.32 | 0 % | 2.5 % |
| 10 kΩ | 2.5 kΩ | 2.2 kΩ | 5.55 | 4.90 ✗ | 4.46 ✗ | 6.74 | 1.7 % | 20 % |
| 10 kΩ | 2.5 kΩ | 1.8 kΩ | 6.56 | 5.76 ✓ | 5.23 ✓ | 8.02 (clip risk) | 0 % | 0 % |
| 20 kΩ | 5.0 kΩ | 4.7 kΩ | 5.26 | 4.65 ✗ | 4.24 ✗ | 6.38 | 20 % | 35 % |
| 20 kΩ | 5.0 kΩ | 3.9 kΩ | 6.13 | 5.40 ✓ | 4.91 | 7.48 | 0 % | 0.6 % |
| **50 kΩ** | **12.5 kΩ** | **10 kΩ** | **6.00** | **5.29 ✓** | 4.81 | 7.32 | **0 %** | **2.5 %** |
| 50 kΩ | 12.5 kΩ | 12 kΩ | 5.17 | 4.57 ✗ | 4.18 ✗ | 6.26 | 30 % | 40 % |

**Key insight:** choosing the largest R2 that *nominally* satisfies AVmax ≥ 5 (for example 12 kΩ with a 50 kΩ pot) fails about **30 %** of the time once tolerances are included. The design needs margin on the low side, but not so much that a 1 V pk-pk input clips at maximum gain (§3.6).

### 2.3 Chosen nominal design

| R1max | R2 | R3 | AVmin | AVmax |
|---|---|---|---|---|
| **50 kΩ** (trimmer, wired as a rheostat) | **10 kΩ** | **10 kΩ** | **1.00 V/V** | **6.00 V/V** |

Justification, which is the text to condense into Section A of the report:

1. **Meets the specification with margin.** R1max/R2 = 5, against ≥ 4 required: a **25 % margin** on the resistor ratio. AVmax stays ≥ 5 for any pot down to −16 % with R2 at +5 % (or −19 % with a 1 % R2), which covers ±10 % trimmers with room to spare.
2. **Does not clip at maximum gain.** The nominal output is 6 V pk-pk (±3 V), well inside the ≈ ±3.5–4 V a 741 can swing on ±5 V. Even the extreme +20 %/−5 % corner (7.3 V pk-pk) is borderline rather than certain to clip. If it clips, reduce the input to 0.5 V pk-pk (§8.10).
3. **One resistor value for everything.** R2 = R3 = 10 kΩ, the value the lab sheet itself recommends for R3, so it is certain to be in the drawers and impossible to mix up.
4. **Good DC balance.** At maximum gain the inverting input sees R1 ‖ R2 = 50 k ‖ 10 k = 8.3 kΩ, while the non-inverting input sees R3 = 10 kΩ. The bias-current-induced offsets therefore almost cancel (§3.9).
5. **Negligible loading of the 741.** The feedback network draws at most 3 V / 60 kΩ = 50 µA at maximum gain, or 0.5 V / 10 kΩ = 50 µA at unity gain. That is 0.2 % of the 25 mA output limit.
6. **Impedances are still low enough** that breadboard stray capacitance (a few pF) only matters above about 5 MHz, and resistor thermal noise (≈ 4 µV rms over 20 kHz for 50 kΩ) is about 76 dB below the bench signal.
7. **Smooth gain control.** The gain rises by 1 V/V per 10 kΩ of pot travel, about one fifth of the travel.

**Robustness tip (optional):** the lab sheet wires the pot with only two connections, wiper and one end. You *may* also tie the unused end to the wiper. The gain is unchanged, but if the wiper loses contact R1 becomes R1max rather than an open circuit. With an open circuit the loop opens and the output slams into a supply rail.

### 2.4 Plan B (if no 50 kΩ trimmer is available)

| Pot available | Use R2 = | AVmax | Notes |
|---|---|---:|---|
| 10 kΩ | 2.0 kΩ (E24) if stocked, else 1.8 kΩ | 6.00 / 6.56 | With 1.8 kΩ, reduce the generator to 0.5 V pk-pk if the output clips at maximum gain |
| 20 kΩ | 3.9 kΩ | 6.13 | |
| 5 kΩ | 1.0 kΩ | 6.00 | Unity-gain load on the output is 1 kΩ (0.5 mA peak), which is fine |

R3 = 10 kΩ in every case. Re-run the two LTspice files with the new values, which takes about 2 minutes.

---

## DELIVERABLE 3 — Complete worked theoretical calculations  **[KEEP]**

### 3.1 Gain derivation (ideal op amp)

The ideal op-amp rules are i₋ = 0, i₊ = 0 and v₊ = v₋.

- Since i₋ = 0, R1 and R2 form an unloaded divider: v₋ = v_out · R2/(R1 + R2).
- v₊ = v_in because the input drives pin 3 directly; R3 only connects that node to ground.
- Setting v₊ = v₋: v_in = v_out · R2/(R1 + R2), so

$$A_V=\frac{R_1+R_2}{R_2}=1+\frac{R_1}{R_2}$$

### 3.2 AVmin and AVmax

- **AVmin** = 1 + 0/10 kΩ = **1.00 V/V**. With the real pot, the end resistance R1min (≤ 1 % of R1max or a few Ω) gives AVmin = 1 + R1min/R2. For 35 Ω, AVmin = 1.0035.
- **AVmax** = 1 + 50 kΩ/10 kΩ = **6.00 V/V**.
- In decibels: 20 log₁₀ 6 = **15.6 dB** of voltage gain.

### 3.3 Expected input and output voltages

| Test | Input (pk-pk) | Output at AVmin | Output at AVmax | Output peak at AVmax |
|---|---:|---:|---:|---:|
| Lab §D / §B: 1 kHz sine | 1.00 V | 1.00 V | **6.00 V** | ±3.00 V |
| Lab §A: 1 kHz sine | 100 mV | 100 mV | 600 mV | ±0.30 V |
| Bench test signal (lab-sheet Fig. 9 shows ≈ 156 mV pk-pk, 35 mV rms) | ≈ 150 mV | ≈ 150 mV | **≈ 0.9 V** | ≈ ±0.47 V |
| RMS of the 1 V pk-pk sine | 0.354 V rms | 0.354 V rms | 2.12 V rms | — |

If the generator is in **HighZ** mode, the voltage actually reaching pin 3 is 1 V × 10 kΩ/(10 kΩ + 50 Ω) = **0.995 V pk-pk**. The 50 Ω is the generator's output resistance. This does not affect the *gain*, because you measure the actual input on CH1.

### 3.4 Node voltages and branch currents at the input's positive peak (vin = +0.5 V)

The input current into the op amp is ignored here; it is 80 nA, which is 0.16 % of these currents.

| Quantity | Minimum gain (R1 = 0) | Maximum gain (R1 = 50 kΩ) |
|---|---|---|
| V(in) = V(pin 3) | 0.500 V | 0.500 V |
| V(inv) = V(pin 2) | 0.500 V (v₋ = v₊) | 0.500 V |
| V(out) = V(pin 6) | 0.500 V | 0.5 × 6 = **3.000 V** |
| I(R3) = V(in)/R3 | 50 µA | 50 µA |
| I(R2) = V(inv)/R2 | 50 µA | 50 µA |
| I(R1) = (V(out) − V(inv))/R1 | = I(R2) = 50 µA (0 V across R1) | (3.0 − 0.5)/50 k = **50 µA** |
| Op-amp output current = I(R1) | 50 µA | 50 µA |
| Current supplied by the generator | 50 µA (all of it flows in R3) | 50 µA |

Because R2 = R3, every branch current is 50 µA at the peak. That makes a neat consistency check on your SPICE output.

### 3.5 Tolerance analysis: how component errors move the gain

Differentiating AV = 1 + R1/R2:

$$\frac{\Delta A_V}{A_V}=\frac{A_V-1}{A_V}\left(\frac{\Delta R_1}{R_1}-\frac{\Delta R_2}{R_2}\right)$$

At AVmax = 6 the sensitivity factor is (6 − 1)/6 = **0.83**. A pot that is 5 % low therefore lowers AVmax by 4.2 % (to 5.75). At AVmin = 1 the factor is 0: **AVmin is insensitive to tolerances**, apart from the pot's end resistance.

| Corner (pot / R2) | AVmax |
|---|---:|
| Nominal | 6.00 |
| −10 % / +5 % | 5.29 |
| +10 % / −5 % | 6.79 |
| −20 % / +5 % | 4.81 |
| +20 % / −5 % | 7.32 |

### 3.6 Output-swing headroom and the largest safe input

The 741 data sheet (typical, ±15 V) gives an output swing of ±14 V into ≥ 10 kΩ and ±13 V into 2 kΩ: **1–2 V of headroom below each rail**. On ±5 V, expect clipping at roughly **±3.5–4 V**, so about **7 V pk-pk** is the usable linear output. The uA741 macromodel clips at ±4.61 V (§6.5), which is more optimistic than a real part.

- At AVmax = 6, the largest input that will not clip is about 7 V/6 ≈ **1.2 V pk-pk**. The specified 1 V pk-pk is fine.
- **Pitfall:** if the generator's *Load* setting is **50 Ω** instead of HighZ, it outputs **twice** the displayed amplitude into the 10 kΩ input (≈ 2 V pk-pk). The output then clips, and the "measured gain" collapses to about 3.5–4.6. Figure `fig_pitfall_clipping.png` shows this. Always read the true input on CH1.

### 3.7 Finite open-loop gain and gain-bandwidth at 1 kHz

The 741 open-loop gain is A₀ ≈ 2 × 10⁵ with a dominant pole near 5 Hz, so at 1 kHz |A| ≈ GBW/f ≈ 10⁶/10³ = 1000, at about −90°. With feedback factor β = 1/AV (the "noise gain"):

- Loop gain T = |A|β = 1000/6 = **167** at maximum gain, and 1000 at minimum gain.
- Because A is essentially imaginary at 1 kHz, the closed-loop *magnitude* error is second-order: 1 − 1/√(1 + 1/T²) ≈ 1/(2T²) = **1.8 × 10⁻⁵ (0.002 %)** at maximum gain.
- The closed-loop phase lag is arctan(1/T) = **0.34°** at maximum gain and 0.057° at minimum gain. The ngspice AC analysis gives −0.348° and −0.058°, which agrees.
- Closed-loop −3 dB bandwidth ≈ GBW/AV ≈ 1 MHz/6 ≈ **170 kHz** at maximum gain (ngspice: 182 kHz) and ≈ 1 MHz at unity (ngspice: 1.4 MHz).

**Conclusion:** finite op-amp gain cannot explain a measurable gain error at 1 kHz. The audio band (20 Hz–20 kHz) is flat to within 0.6 % even at maximum gain.

### 3.8 Slew rate and full-power bandwidth

- 741 slew rate ≈ 0.5 V/µs.
- The steepest slope of a 3 V-peak, 1 kHz output is 2π·f·Vp = 2π × 10³ × 3 = **0.019 V/µs**, so the margin is about 26×.
- Full-power bandwidth at 3 V peak is SR/(2πVp) = **26.5 kHz**. There is no slew-induced distortion in this experiment.

### 3.9 Input bias current, offset voltage, and why R3 exists

These are data-sheet typicals: IB ≈ 80 nA (500 nA max), VOS ≈ 1 mV (5 mV max).

- **With R3 present** and the source unplugged, the bias current into pin 3 flows through R3: V(in) = −IB·R3 = −80 nA × 10 kΩ = **−0.8 mV**. ngspice gives −0.797 mV.
- **Without R3**, for example with an AC-coupled source or the input lead unplugged, the bias current has no DC path. Pin 3 drifts until the op amp saturates. In ngspice, R3 = 1 TΩ drives the output to **−4.61 V, the negative rail**.
- At maximum gain with the input driven, the inverting-input bias current flows through R1 and produces an output offset IB·R1 = 80 nA × 50 kΩ = **4.0 mV**. ngspice gives 4.10 mV.
- VOS adds up to ±1 × 6 = ±6 mV (typical). These DC offsets shift the trace vertically but **do not change Vpp**. They are irrelevant to the gain, which is a useful point for the commentary.

### 3.10 Loading effects

| Load | Mechanism | Size |
|---|---|---|
| Generator (50 Ω source) into R3 (10 kΩ) | Voltage divider at the input | vin is 0.5 % below the generator EMF. Gain unaffected because vin is measured |
| Oscilloscope CH1/CH2 (1 MΩ ‖ ≈ 16 pF) | Parallel load on the input and output | At the input, 1 MΩ ‖ 10 kΩ: negligible. At the output, the closed-loop output resistance is < 1 Ω, so no effect |
| Headphones (assume 32 Ω) | Heavy load on the 741 output | Closed-loop output impedance ≈ r_o/(1 + T), and it is *inductive* (T falls with frequency). At 1 kHz the gain drop is 0.02 % (ngspice: 5.9981 vs 5.9996); at 20 kHz it is 4 %. The real limit is the **25 mA output current**: a 0.47 V peak into 32 Ω needs 14.5 mA (ngspice: 15.1 mA peak). Current limiting would start at about 0.8 V peak |

### 3.11 Audio arithmetic (for Section F)

- Voltage gain 6, so the level rises by **15.6 dB**. Power into the same headphones rises 36× (P ∝ V²).
- Rule of thumb: +10 dB ≈ "twice as loud", so +15.6 dB ≈ **2.9× as loud**.
- Bench signal ≈ 35 mV rms gives 39 µW into 32 Ω at unity gain and 1.4 mW at gain 6. That is comfortably loud for typical headphones (≈ 100 dB SPL/mW sensitivity) while still far from the 741's current limit.

---

## DELIVERABLE 4 — Complete LTspice design

Everything is in [`../spice/ltspice/`](../spice/ltspice/). Keep these files in **one folder**, because the `.lib uA741.lib` path is relative.

| File | Purpose | Report section |
|---|---|---|
| `uA741.lib` | uA741 behavioural macromodel (classic TI/National Boyle-type model, pins: +in, −in, V+, V−, out) | All |
| `exp2_nominal_min_gain.asc` / `.cir` | Nominal design, R1 = 1 mΩ (pot at 0), 1 V pk-pk 1 kHz, .tran + .meas | B (min) |
| `exp2_nominal_max_gain.asc` / `.cir` | Nominal design, R1 = 50 kΩ | B (max) |
| `exp2_nominal_step.asc` / `.cir` | Both gains in one run (`.step param R1 list 1m 50k`) | B (overlay figure, optional) |
| `exp2_nominal_op_min.asc` / `.cir` | **.op** at vin = +0.5 V DC, min gain: node-voltage and branch-current table | B ("SPICE output") |
| `exp2_nominal_op_max.asc` / `.cir` | Same, max gain | B ("SPICE output") |
| `exp2_measured_min_gain.asc` / `.cir` | Section G: `.param` values for **measured** components (**[PROTOTYPE] placeholders**) | G |
| `exp2_measured_max_gain.asc` / `.cir` | Section G, max gain | G |

**Circuit, with node names identical in every file:**

```
VCC  vcc 0   5                 ; +5 V rail  (pin 7)
VEE  0   vee 5                 ; -5 V rail  (pin 4)
Vsig in  0   SINE(0 {Vpk} 1k)  ; Vpk = 0.5 V -> 1 V pk-pk  (0.05 -> 100 mV pk-pk)
R3   in  0   10k               ; bias-current return / input resistance
R1   out inv 50k   (or 1m)     ; potentiometer, max (or min) setting
R2   inv 0   10k
XU1  in inv vcc vee out uA741  ; opamp2 symbol: In+ In- V+ V- OUT
.tran 0 6m 0 1u
.options plotwinsize=0         ; turn off waveform compression (accurate peaks)
.meas TRAN Vin_pp  PP V(in)  FROM 2m TO 6m
.meas TRAN Vout_pp PP V(out) FROM 2m TO 6m
.meas TRAN AV PARAM Vout_pp/Vin_pp
.meas TRAN Vout_pk FIND V(out) AT 4.25m      ; and V(in), V(inv), I(R1..R3), I(VCC), I(VEE)
```

**Why these choices:**

- **R1 = 1 mΩ** rather than 0 avoids a zero-value resistor, which some SPICE versions reject. Its effect on the gain is 10⁻⁷.
- **6 ms** run, with measurements from 2 ms: the circuit has no slow time constants, but skipping the first 2 cycles removes any start-up transient.
- **1 µs maximum step** gives 1000 points per cycle, so the measured peaks are accurate to < 0.001 %.
- **t = 4.25 ms** is a positive peak of the 1 kHz input: sin(2π · 1000 · 4.25 ms) = sin(8.5π) = +1.

**Verification performed for this pack:** the `.cir` netlists were converted mechanically to ngspice syntax and run. They give AV = 0.99996 (min) and 5.9996 (max), which proves the topology. A connectivity extractor also confirmed that every pin in every `.asc` lands on the intended net, *given* the standard LTspice symbol pin coordinates. Those coordinates were not checked in LTspice itself. If LTspice shows an unconnected pin, simply re-draw the wire; the `.cir` netlists always work.

---

## DELIVERABLE 5 — Complete LTspice simulation procedure

**You must produce your own LTspice screenshots. The schematic drawings in the prototype report are stand-ins.**

1. **Install** LTspice (free, from analog.com). Put `uA741.lib` in the same folder as your schematic.
2. **New schematic** → *File > New Schematic* → *File > Save As* `exp2_min.asc` in that folder.
3. **Place the op amp:** press **F2** → *[Opamps]* → **opamp2** → place. Right-click it: **Value = `uA741`**, InstName = U1.
4. **Model directive:** press **S** (SPICE directive) → type `.lib uA741.lib` → place it anywhere.
5. **Resistors:** press **R** and place four resistors. Ctrl+R rotates. Right-click to set values: R1 = `1m` (min file) or `50k` (max file), R2 = `10k`, R3 = `10k`.
6. **Sources:** press **F2** → `voltage`, three times.
   - **VCC** = 5, + terminal to the op-amp **V+** pin.
   - **VEE** = 5 with **+ to ground**, − terminal to the op-amp **V−** pin.
   - **Vsig**: right-click → *Advanced* → **SINE**, DC offset 0, Amplitude `{Vpk}`, Freq `1k`.
7. **Wire** it exactly as lab-sheet Fig. 6 (press **F3** to draw a wire):
   - Vsig+ → pin 3 (+), and R3 from that node to ground.
   - Op-amp output → top of R1; bottom of R1 → top of R2 → ground.
   - Junction R1/R2 → pin 2 (−).
   - Press **G** to place grounds.
8. **Name the nodes:** press **F4** and label `in`, `inv`, `out`, `vcc`, `vee`. The labels make the plots and `.meas` lines readable.
9. **Analysis:** *Simulate > Edit Simulation Cmd > Transient*: Stop time `6m`, Maximum timestep `1u` → OK and place it.
10. **Directives:** press **S** and add `.param Vpk=0.5`, `.options plotwinsize=0`, and the `.meas` lines from Deliverable 4. You can paste them all as one multi-line directive.
11. **Run** (running-man icon).
    - In the plot window, click node `in` and node `out` to plot V(in) and V(out).
    - **Alt-click** (or click the body of) R1, R2 and R3 to plot I(R1), I(R2) and I(R3).
    - Right-click the plot → *Add Plot Pane* to put the currents in a second pane.
12. **Read the numbers:** *View > SPICE Error Log* (**Ctrl+L**) shows Vin_pp, Vout_pp, **AV**, and the peak node voltages and currents. **Screenshot this log**: it is your "SPICE output (node voltages and branch currents)".
13. **.op table:** *File > Save As* `exp2_min_op.asc`, set Vsig to **DC 0.5**, and replace `.tran` with `.op`. Run, and LTspice opens a table of every node voltage and device current. **Screenshot it.**
14. **Repeat steps 11–13 for maximum gain** (R1 = `50k`).
15. **100 mV pk-pk run** (lab sheet §A): set `.param Vpk=0.05`, re-run both files and note AV. It should be identical.
16. **Screenshot hygiene:**
    - Schematic: *View > Zoom to Fit*, white background (*Tools > Color Preferences*), all values visible.
    - Waveforms: two cycles visible, both traces labelled, axes readable.
    - Crop tightly. Use the same zoom for the min and max figures.

**What goes where in the template (Section B):**

| Template box | Paste |
|---|---|
| "SPICE schematics to simulate minimum and maximum voltage gain" | Your min-gain schematic and max-gain schematic (two screenshots side by side), with the `.tran`, `.lib` and `.meas` directives visible |
| "SPICE output (node voltages and branch currents) …" | For each configuration: (a) V(in)/V(out) waveforms with the currents pane, (b) the `.op` table, (c) the `.meas` log. Add a two-row summary table if space is short |
| "Voltage gain predicted by SPICE simulation (with nominal resistor values)" | AV from the `.meas` log, to 4 significant figures: about **1.000** and **6.000** (ngspice reference: 0.99996 and 5.9996) |

**LTspice troubleshooting**

| Symptom | Cause | Fix |
|---|---|---|
| "Unknown subcircuit called in: xu1 … uA741" | `.lib` not found | Put `uA741.lib` in the schematic's folder; check the directive spelling |
| Output stuck at about ±4.6 V | Feedback wired to pin 3 instead of pin 2, or + and − swapped | Feedback must go to the **−** input |
| Gain exactly 1 at "max" | R1 still `1m`, or R1 not between output and pin 2 | Check the R1 value and connections |
| Jagged sine, peaks wrong in the 3rd digit | Waveform compression | `.options plotwinsize=0` and maximum timestep `1u` |
| Currents look negative | LTspice current direction is pin 1 → pin 2 of the symbol | Rotate the resistor 180° or quote magnitudes |

---

## DELIVERABLE 6 — Prototype simulation results  **[SIM-REF]**

These are ngspice 42 runs of the same netlists and model (generated by `tools/run_sims.py`; raw data in `spice/results/`). **Your LTspice results replace them**, and should agree to about 4 significant figures.

### 6.1 Gains

| Run | Vin,pp | Vout,pp | AV |
|---|---:|---:|---:|
| Min gain, 1 V pk-pk, 1 kHz | 1.0000 V | 0.99996 V | **0.99996 ≈ 1.000** |
| Max gain, 1 V pk-pk, 1 kHz | 1.0000 V | 5.9996 V | **5.9996 ≈ 6.000** |
| Min gain, 100 mV pk-pk | 0.10000 V | 0.099996 V | 0.99996 |
| Max gain, 100 mV pk-pk | 0.10000 V | 0.59996 V | 5.9996 |
| Max gain, supplies ±4.75 V / ±5.25 V | 1.0000 V | 5.9996 V | 5.9996 / 5.9996 (unchanged) |
| Max gain, 50 Ω generator resistance | 0.99502 V | 5.9697 V | 5.9996 (unchanged) |

### 6.2 Node voltages and branch currents: `.op` at vin = +0.5 V DC

| | V(in) | V(inv) | V(out) | I(R1) | I(R2) | I(R3) | I(op-amp out) | I(VCC) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Min gain** | 0.5000 V | 0.5000 V | 0.5000 V | 50.08 µA | 50.00 µA | 50.00 µA | 50.08 µA | −0.566 mA |
| **Max gain** | 0.5000 V | 0.49999 V | 3.0039 V | 50.08 µA | 50.00 µA | 50.00 µA | 50.08 µA | −0.566 mA |

**Interpretation, which is what earns the "analysis" credit:**

- **v₋ = v₊ holds** to 10 µV, confirming the virtual-short assumption.
- **I(R1) − I(R2) = 80 nA**: by KCL at pin 2, this difference is the **inverting-input bias current**. It is real, but 0.16 % of the branch current.
- V(out) at maximum gain is 3.0039 V rather than 3.0000 V. The 3.9 mV excess is the DC offset IB·R1 ≈ 4 mV (§3.9), which shifts the DC level but not Vpp.
- I(VCC) is negative because SPICE counts current flowing *into* the source's + terminal. Here the source is delivering 0.566 mA. That is the model's quiescent current; a real 741 draws about 1–2 mA.

### 6.3 Transient values at the input's positive peak (t = 4.25 ms)

| | V(in) | V(inv) | V(out) | I(R1) | I(R2) | I(R3) |
|---|---:|---:|---:|---:|---:|---:|
| Min gain | 0.5000 V | 0.5000 V | 0.5000 V | 50.1 µA | 50.0 µA | 50.0 µA |
| Max gain | 0.5000 V | 0.49997 V | 3.0038 V | 50.1 µA | 50.0 µA | 50.0 µA |

### 6.4 Frequency response (supplementary)

| | Gain at 1 kHz | Phase at 1 kHz | Gain at 20 kHz | −3 dB bandwidth |
|---|---:|---:|---:|---:|
| Min gain | 0.99996 | −0.058° | 0.99999 | 1.40 MHz |
| Max gain | 5.9996 | −0.348° | 5.964 (−0.6 %) | 182 kHz |
| Max gain, 32 Ω load | 5.9981 | — | 5.747 (−4.2 %) | 67 kHz |

### 6.5 Stress cases (support the commentary and troubleshooting)

| Case | Result |
|---|---|
| 2 V pk-pk at maximum gain (generator wrongly in 50 Ω mode) | Output clipped at ±4.61 V (9.23 V pk-pk); apparent gain 4.61. A real 741 clips earlier |
| Source unplugged, R3 = 10 kΩ | V(in) = −0.80 mV, V(out) = −0.68 mV (fine) |
| Source unplugged, R3 removed (1 TΩ) | V(out) = **−4.61 V, saturated**. This shows why R3 is needed |
| 160 mV pk-pk at maximum gain into 32 Ω | Gain 5.998; peak output current **15.1 mA** (< 25 mA limit) |

Figures: `figures/fig_B_sim_min.png`, `fig_B_sim_max.png`, `fig_B_sim_ac.png`, `fig_pitfall_clipping.png`.

---

## DELIVERABLE 7 — Complete physical laboratory build instructions

**Fetch the right trimmer:** the code printed on it is 3 digits, the value in Ω × 10^(third digit). **503 = 50 kΩ** (203 = 20 kΩ, 103 = 10 kΩ, 502 = 5 kΩ).

**Before inserting anything, measure R2, R3 and the pot with the DMM**, and record them on the data sheet. Pot readings: wiper-to-end at both extremes, and end-to-end. Measuring later, in circuit, gives wrong readings because of the parallel paths.

1. **PSU first (output off):** set both sources to 5.0 V and both current-limit knobs to "9 o'clock". Link the two sources in series (lab-sheet Fig. 5): **red** = +5 V, **green** = 0 V (the junction), **black** = −5 V. Switch off.
2. **741:** pin 1 is marked by the dot or notch. Insert it **straddling the centre channel**. Pin map, viewed from above with the notch on the left:

   | Bottom row (row e) | pin 1 (offset null, NC) | **pin 2 (−)** | **pin 3 (+)** | **pin 4 (V−)** |
   |---|---|---|---|---|
   | **Top row (row f)** | pin 8 (NC) | **pin 7 (V+)** | **pin 6 (out)** | pin 5 (offset null, NC) |

3. **Rails:** red jumper, **pin 7 → +5 V rail**. Black jumper, **pin 4 → −5 V rail**. Link the top and bottom GND rails with green wire.
4. **R2 (10 kΩ):** from the **pin 2 column** to a GND column or rail.
5. **R3 (10 kΩ):** from the **pin 3 column** to GND.
6. **R1 (50 kΩ trimmer):** connect the **wiper and one end only**:
   - one terminal → **pin 6 column (output)**;
   - the other → **pin 2 column**.
   - Optionally tie the spare end to the wiper (§2.3).
7. **4 mm sockets:** red → +5 V rail; green → GND rail; black → −5 V rail; **yellow → pin 3 column (Input)**; **blue → pin 6 column (Output)**. Record the colours in Table I.
8. **Inspection before power (2 minutes, saves the chip):**
   - No component legs share a column unintentionally.
   - Pin 4 goes to −5 V, **not** +5 V.
   - Feedback goes to **pin 2**, not pin 3.
   - Use the DMM on Ω, power off: there is **no** short between the +5 V rail and GND, or between the −5 V rail and GND.
9. **Photo P1** (Section "E construction"):
   - Shoot from directly above, in good light, with the whole board in frame.
   - Lay a small paper label next to each part (R1, R2, R3, 741, pin 1). Annotate in the report if the labels are not legible.
   - A second, oblique shot showing component heights is optional.

**Table I (fill in):** VS+ red • VS− black • GND green • vin yellow • vout blue. Change the entries if your bench uses different socket colours.

---

## DELIVERABLE 8 — Complete measurement procedure

### 8.1 Power-up and supply verification

1. Signal generator **output OFF**. Connect the PSU leads to the breadboard sockets and switch on.
2. The current meters should show only about 1–3 mA per rail. If either source hits its current limit (voltage collapses), **switch off immediately** and re-check the wiring.
3. DMM on DC V, LO to circuit ground:
   - **pin 7** should read +5.0 V; **pin 4** should read −5.0 V. Record both, for example +5.02 V / −5.01 V.
   - Also measure **pin 6** with no input. It should be within tens of mV of 0 V; this is the DC offset. If it sits near a rail, the feedback is miswired.

### 8.2 Signal generator (Rigol DG822)

1. CH1: **Sine**, **Freq 1.000 kHz**, **Amplitude 1.000 Vpp**, **Offset 0 V**.
2. **Load / output impedance = HighZ**, in the channel's output settings. In 50 Ω mode the output into your 10 kΩ input is about 2 Vpp, enough to clip at maximum gain (§3.6).
3. BNC-to-4 mm coax: **red → Input (yellow socket)**, **black → GND**. Output ON.

### 8.3 Oscilloscope connections (HMO1002)

- **CH1** = Input node (yellow lead); **CH2** = Output node (blue lead).
- Scope ground (black) → circuit GND.
- Both channels **DC coupled**, probe/attenuation setting **1×** for the direct leads. A channel accidentally set to 10× makes that channel read 10× high, and the computed gain is off by a factor of 10.

### 8.4 Oscilloscope set-up for a submission-quality screen

| Setting | Minimum gain | Maximum gain |
|---|---|---|
| CH1 V/div | 200 mV/div | 200 mV/div |
| CH2 V/div | 200 mV/div | **1 V/div** |
| Vertical positions | CH1 +1 div, CH2 −1 div (both traces fully visible, separable) | Both 0 div |
| Timebase | 200 µs/div (2 cycles across the screen) | 200 µs/div |
| Trigger | CH1, rising edge, level 0 V | Same |
| Acquisition | Optional **Average 8–16** to suppress noise inflating Vpp | Same |
| Bandwidth limit | **BWL on** (20 MHz), which cuts noise without touching a 1 kHz signal | Same |
| Measurements on screen | **Vpp(CH1), Vpp(CH2), Freq(CH1)**, and RMS(CH1)/RMS(CH2) if space allows | Same |

**Rule:** each trace should span **≥ 5 vertical divisions** and **never clip off-screen**. Vpp resolution is about 1/25 of a division, so a 5-division trace is resolved to better than 1 %.

`AUTOSET` followed by `QUICK VIEW` is acceptable for a first look. Then set the scales above so that both channels' measurements are displayed together. QUICK VIEW shows one channel at a time, so it cannot show both Vpp values in one photo.

### 8.5 Minimum-gain measurement (Section D)

1. Turn the pot until CH2 is as **small** as possible, at the end stop. CH1 and CH2 should be identical sinusoids.
2. Freeze or keep running. Read **Vpp(CH1)** and **Vpp(CH2)** and write them **immediately** on the data sheet, with units and 3 significant figures.
3. **Photo P3**: square-on to the screen, no glare, the whole graticule and all readouts legible. Optionally also save a screenshot to USB stick (*SAVE/RECALL → Screenshot*, or the *FILE/PRINT* key).
4. AVmin = Vpp(CH2)/Vpp(CH1). Expect **1.00–1.01**. A value ≈ 1.05 suggests large pot end resistance; anything else suggests a wiring fault.
5. **Swap check (30 s, strongly recommended):** swap the two scope leads so CH1 = output and CH2 = input, and re-read. If the gain ratio changes, the difference is the **channel calibration mismatch**. Record it; it is gold for the commentary.

### 8.6 Maximum-gain measurement (Section D)

1. Turn the pot until CH2 is as **large** as possible, at the end stop. Change CH2 to 1 V/div.
2. Check the CH2 peaks are **round, not flat**. If flat (clipping), confirm HighZ mode and that Vpp(CH1) ≈ 1 V. If still clipping, reduce the input to 0.5 Vpp and note that in the caption.
3. Record Vpp(CH1) and Vpp(CH2). **Photo P4.** Calculate AVmax. Expect **5.4–6.6**, nominally 6.0. It **must be ≥ 5**; if not, see §8.10.

### 8.7 Bench-test-signal measurements (Section E)

1. Move the coax from the generator to the **BENCH TEST SIGNAL** BNC.
2. Scope: CH1 50 mV/div, CH2 50 mV/div (min gain) or 200 mV/div (max gain). Timebase **2–5 ms/div**.
   - Lab-sheet Fig. 9 uses 50 ms/div, which forces the sample rate down to ≈ 10 kSa/s, so the scope can miss short peaks.
   - Position the traces so they do not overlap, and trigger on CH1 (normal mode).
3. **Minimum gain:** press **RUN/STOP** to freeze a representative capture (both channels are frozen *at the same instant*, so their ratio is meaningful). Read Vpp(1), Vpp(2) and also RMS(1), RMS(2). **Photo P5.**
4. **Maximum gain:** pot to maximum, **RUN**, then **STOP** on a representative capture. Record the same quantities. **Photo P6.**
5. Expect Vin ≈ 150 mV pk-pk (it varies with the programme material), Vout ≈ Vin at minimum and ≈ 5.5–6 × Vin at maximum.
   - The Vpp-based gain on a non-repetitive audio signal is noisier (±3–5 %) than on the sine, because Vpp is set by single extreme samples.
   - The **RMS-based gain is the more robust estimate**. Quote it in the commentary as a cross-check.
6. Record whether the headphones were connected during each capture. Lab sheet §F has you measure after listening, so they usually are.

### 8.8 Audio test and Demonstrator verification (Section F)

1. Headphones on **CH2's socket** via the adapter, as the lab sheet specifies: yellow to the CH2 signal, green to ground.
2. Set the gain to 1 and listen: the original level, quiet but audible. Then go to maximum gain: a "comfortable" level.
3. Note in your own words: audibility, any hiss, buzz, crackle or harshness, and whether harshness appears only at maximum gain (which would point to clipping or current limiting).
4. **Demonstrator:** show the working amplifier: sine at both gain settings on the scope, then the bench signal and audio. The Demonstrator answers "audible and free of distortion? Yes/No", and you record their answer, not yours.
   - Ask them to initial your data sheet if that is local practice.
   - Do **not** fill in this box yourself before the check.

### 8.9 Photo shot-list (take every one; take two of each)

| ID | Content | Report location |
|---|---|---|
| P1 | Breadboard layout, top-down, all parts identifiable | "E Amplifier construction" |
| P2 | **Whole set-up**: breadboard + PSU + generator (display readable: 1 kHz, 1 Vpp, HighZ) + scope | D, first box |
| P3 | Scope, sine, **min gain**, both Vpp values legible | D, min gain |
| P4 | Scope, sine, **max gain**, both Vpp values legible | D, max gain |
| P5 | Scope, bench signal, **min gain**, STOP, readouts legible | E (bench), min gain |
| P6 | Scope, bench signal, **max gain**, STOP, readouts legible | E (bench), max gain |
| P7 (optional) | DMM reading of each resistor and the pot (min/max) | G evidence |
| P8 (optional) | DMM on pin 7 and pin 4 | Supply verification (credibility) |

### 8.10 Troubleshooting during the lab

| Symptom | Most likely cause | Check / fix |
|---|---|---|
| Output stuck near +4 V or −4 V | Feedback open (pot wiper not contacting, R1 not to pin 2), or + and − swapped | Trace R1 from pin 6 to pin 2; reseat the pot; tie the spare pot end to the wiper |
| Output = input at every pot setting | R1 shorted, or wired between the wiper and *the same* end; R2 not connected to ground | DMM across R1 while turning the pot (power off) |
| AVmax < 5 | Wrong pot value fetched (code **503** = 50 kΩ; 203 = 20 kΩ, 103 = 10 kΩ, 502 = 5 kΩ); pot not at its end stop; wrong R2; or clipping | Read the pot's code; DMM the pot as wired (power off); colour-check R2 (brown-black-orange = 10 kΩ); look for flat tops |
| Flat-topped output at max gain | Input too large (50 Ω mode) | Generator Load = HighZ; confirm Vpp(CH1) ≈ 1 V |
| PSU current limit reached | Short, or the op amp backwards (pins 4/7 reversed) | Power off immediately; check orientation (pin 1 dot) |
| Noisy or fuzzy trace | Ground lead missing; long unscreened input wire | Scope ground to circuit GND; use the coax for the input; BWL on |
| Gain off by exactly 10× | Scope channel probe setting at 10× | Set both channels to 1× |
| Bench signal not visible | Coax not on the BENCH TEST SIGNAL socket; V/div too coarse | 20–50 mV/div on CH1; check the BNC |

---

## DELIVERABLE 9 — Complete data collection sheets

Print **`report/EEEN20020_Exp2_DATA_SHEET.pdf`** (two A4 pages) and fill it in with pen during the lab. Its content is reproduced here.

**Sheet 1: components and supplies**

| Item | Nominal | Measured (DMM) | Units | Notes |
|---|---|---|---|---|
| R1max (pot at max, wiper to the used end) | 50 k | | kΩ | measured before insertion / as wired |
| R1min (pot at min, wiper to the used end) | ≈ 0 | | Ω | end resistance |
| Pot end-to-end | 50 k | | kΩ | |
| R2 | 10 k | | kΩ | colour bands: |
| R3 | 10 k | | kΩ | colour bands: |
| VS+ at pin 7 | +5.00 | | V | |
| VS− at pin 4 | −5.00 | | V | |
| Output DC offset, no input, max gain | ≈ 0 | | mV | |
| Generator setting | 1 kHz, 1.000 Vpp, offset 0, HighZ | ✓ | | |

**Table I: socket colours.** VS+ ___ VS− ___ GND ___ vin ___ vout ___

**Sheet 2: measurements**

| Test | V/div CH1 / CH2 | t/div | Vpp CH1 (in) | Vpp CH2 (out) | Gain = out/in | RMS CH1 | RMS CH2 | RMS gain | Photo # |
|---|---|---|---|---|---|---|---|---|---|
| Sine, min gain | / | | | | | | | | P3 |
| Sine, max gain | / | | | | | | | | P4 |
| Channel-swap check (min gain) | / | | | | | | | | — |
| Bench, min gain (STOP) | / | | | | | | | | P5 |
| Bench, max gain (STOP) | / | | | | | | | | P6 |
| Headphones connected during bench captures? | Y / N | | | | | | | | |

**Audio / Demonstrator**

| Audible and free of distortion? (Demonstrator) | Yes ☐ No ☐ | Demonstrator initials: |
|---|---|---|
| Our observation at min gain | | |
| Our observation at max gain | | |

**Quick checks before leaving the bench:**

- [ ] AVmin ≈ 1.00
- [ ] AVmax ≥ 5
- [ ] Every number has a photo
- [ ] P1–P6 taken
- [ ] Resistors measured
- [ ] Demonstrator ticked
