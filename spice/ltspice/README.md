# LTspice files: EEEN20020 Experiment 2

Keep every file in this folder together: the schematics load the model with a relative `.lib uA741.lib`.

| File | Use |
|---|---|
| `exp2_nominal_min_gain.asc/.cir` | Section B, minimum gain (R1 = 1 mΩ ≈ 0 Ω), 1 V pk-pk 1 kHz, `.tran` + `.meas` |
| `exp2_nominal_max_gain.asc/.cir` | Section B, maximum gain (R1 = 50 kΩ) |
| `exp2_nominal_step.asc/.cir` | Both gains overlaid in one run (`.step param R1 list 1m 50k`) |
| `exp2_nominal_op_min.asc/.cir`, `exp2_nominal_op_max.asc/.cir` | `.op` at vin = +0.5 V DC: the node-voltage and branch-current table for "SPICE output" |
| `exp2_measured_min_gain.asc/.cir`, `exp2_measured_max_gain.asc/.cir` | Section G. **The `.param` values are PROTOTYPE placeholders.** Replace them with your DMM readings |
| `uA741.lib` | uA741 macromodel (pins: +in, −in, V+, V−, out), used with the `opamp2` symbol |

**Run:** open a `.asc` in LTspice → Run. To see the gain, node voltages and currents from the `.meas` lines, open **View → SPICE Error Log** (Ctrl+L).

- Set `.param Vpk=0.05` for the 100 mV pk-pk run (lab sheet §A); `Vpk=0.5` is 1 V pk-pk (§B).
- If a wire looks unconnected in your LTspice version, open the matching `.cir` instead (File → Open → Netlists) or redraw that wire.

**Expected results** (ngspice reference; your LTspice values should agree to about 4 s.f.):

- AV(min) = 0.99996
- AV(max) = 5.9996
- `.op` at +0.5 V: V(out) = 0.5000 / 3.0039 V; I(R1) = 50.08 µA, I(R2) = I(R3) = 50.00 µA.

The full step-by-step procedure is in [`../../docs/00_MASTER_PLAN.md`](../../docs/00_MASTER_PLAN.md), Deliverable 5.
