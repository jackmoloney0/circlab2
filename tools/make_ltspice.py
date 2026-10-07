#!/usr/bin/env python3
"""
Generate the LTspice schematics (.asc) and equivalent netlists (.cir) for
EEEN20020 Experiment 2. Everything lands in spice/ltspice/ next to uA741.lib
so the relative `.lib uA741.lib` resolves when the files are opened in LTspice.

Schematic geometry (LTspice grid units, R0 orientation):
  res        pins at (+16,+16) A and (+16,+96) B
  voltage    pins at (0,+16) '+' and (0,+96) '-'
  opamp2     In+ (-32,+80), In- (-32,+48), V+ (0,+32), V- (0,+96), OUT (+32,+64)
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "spice", "ltspice")

MEAS = [
    ".meas TRAN Vin_pp PP V(in) FROM 2m TO 6m",
    ".meas TRAN Vout_pp PP V(out) FROM 2m TO 6m",
    ".meas TRAN AV PARAM Vout_pp/Vin_pp",
    ".meas TRAN Vin_pk FIND V(in) AT 4.25m",
    ".meas TRAN Vinv_pk FIND V(inv) AT 4.25m",
    ".meas TRAN Vout_pk FIND V(out) AT 4.25m",
    ".meas TRAN IR1_pk FIND I(R1) AT 4.25m",
    ".meas TRAN IR2_pk FIND I(R2) AT 4.25m",
    ".meas TRAN IR3_pk FIND I(R3) AT 4.25m",
    ".meas TRAN IVCC_pk FIND I(VCC) AT 4.25m",
    ".meas TRAN IVEE_pk FIND I(VEE) AT 4.25m",
]

WIRES = [
    (96, 240, 224, 240), (224, 240, 368, 240),          # input node 'in'
    (432, 224, 512, 224), (512, 224, 512, 240),         # output node 'out'
    (368, 208, 336, 208), (336, 208, 336, 128),         # feedback to In-
    (336, 128, 608, 128), (608, 128, 608, 320),
    (608, 320, 512, 320),                               # R1/R2 junction 'inv'
    (400, 192, 400, 160), (400, 256, 400, 288),         # op-amp supply pins
    (704, 176, 704, 160), (704, 256, 704, 272),         # VCC source
    (816, 176, 816, 160), (816, 256, 816, 272),         # VEE source
    (96, 320, 96, 336), (224, 320, 224, 336), (512, 400, 512, 416),  # grounds
]
FLAGS = [
    (96, 336, "0"), (224, 336, "0"), (512, 416, "0"), (704, 272, "0"),
    (816, 160, "0"),
    (224, 240, "in"), (512, 224, "out"), (336, 208, "inv"),
    (400, 160, "vcc"), (704, 160, "vcc"), (400, 288, "vee"), (816, 272, "vee"),
]


def asc(title, notes, r1, r2, r3, vsig, directives):
    L = ["Version 4", "SHEET 1 1240 900"]
    L += [f"WIRE {a} {b} {c} {d}" for a, b, c, d in WIRES]
    L += [f"FLAG {x} {y} {n}" for x, y, n in FLAGS]
    L += ["SYMBOL voltage 96 224 R0", "SYMATTR InstName Vsig", f"SYMATTR Value {vsig}"]
    L += ["SYMBOL res 208 224 R0", "SYMATTR InstName R3", f"SYMATTR Value {r3}"]
    L += ["SYMBOL Opamps\\\\opamp2 400 160 R0", "SYMATTR InstName U1", "SYMATTR Value uA741"]
    L += ["SYMBOL res 496 224 R0", "SYMATTR InstName R1", f"SYMATTR Value {r1}"]
    L += ["SYMBOL res 496 304 R0", "SYMATTR InstName R2", f"SYMATTR Value {r2}"]
    L += ["SYMBOL voltage 704 160 R0", "SYMATTR InstName VCC", "SYMATTR Value 5"]
    L += ["SYMBOL voltage 816 160 R0", "SYMATTR InstName VEE", "SYMATTR Value 5"]
    y = 24
    for t in [title] + notes:
        L.append(f"TEXT 64 {y} Left 2 ;{t}")
        y += 28
    y = 480
    for d in directives:
        L.append(f"TEXT 64 {y} Left 2 !{d}")
        y += 28
    return "\n".join(L) + "\n"


def cir(title, notes, r1, r2, r3, vsig, directives):
    L = [f"* {title}"] + [f"* {n}" for n in notes] + [
        "* Open in LTspice (File > Open, 'Netlists (*.cir)') and click Run.",
        "VCC vcc 0 5",
        "VEE 0 vee 5",
        f"Vsig in 0 {vsig}",
        f"R3 in 0 {r3}",
        f"R1 out inv {r1}",
        f"R2 inv 0 {r2}",
        "XU1 in inv vcc vee out uA741",
    ] + directives + [".end"]
    return "\n".join(L) + "\n"


def tran_dirs(extra=()):
    return [".tran 0 6m 0 1u", ".lib uA741.lib", ".param Vpk=0.5",
            ".options plotwinsize=0", *extra, *MEAS]


VARIANTS = {
    "exp2_nominal_min_gain": dict(
        title="EEEN20020 Exp. 2 - NOMINAL design - MINIMUM gain (potentiometer R1 at 0 ohm)",
        notes=["R1 = 1 mohm stands in for 0 ohm (avoids a zero-value resistor; gain error ~1e-7)",
               "Vpk = 0.5 V -> 1 V pk-pk input (lab sheet Sec. B). Set Vpk=0.05 for the 100 mV pk-pk run (Sec. A)",
               "Results of .meas: View > SPICE Error Log (Ctrl+L)"],
        r1="1m", r2="10k", r3="10k", vsig="SINE(0 {Vpk} 1k)", d=tran_dirs()),
    "exp2_nominal_max_gain": dict(
        title="EEEN20020 Exp. 2 - NOMINAL design - MAXIMUM gain (potentiometer R1 = R1max = 50 kohm)",
        notes=["Design: AVmax = 1 + R1max/R2 = 1 + 50k/10k = 6.00 V/V",
               "Vpk = 0.5 V -> 1 V pk-pk input (lab sheet Sec. B). Set Vpk=0.05 for the 100 mV pk-pk run (Sec. A)",
               "Results of .meas: View > SPICE Error Log (Ctrl+L)"],
        r1="50k", r2="10k", r3="10k", vsig="SINE(0 {Vpk} 1k)", d=tran_dirs()),
    "exp2_nominal_step": dict(
        title="EEEN20020 Exp. 2 - NOMINAL design - min and max gain in ONE run (.step over R1)",
        notes=["Step 1: R1 = 1 mohm (pot at minimum)   Step 2: R1 = 50 kohm (pot at maximum)",
               "Plot V(in) and V(out): both steps overlay. .meas results are listed per step in the Error Log"],
        r1="{R1}", r2="10k", r3="10k", vsig="SINE(0 {Vpk} 1k)",
        d=tran_dirs([".step param R1 list 1m 50k"])),
    "exp2_nominal_op_min": dict(
        title="EEEN20020 Exp. 2 - NOMINAL - MIN gain - DC operating point at vin = +0.5 V (positive peak of 1 V pk-pk)",
        notes=["Run, and LTspice opens a table of every node voltage and branch current (screenshot it for Sec. B)"],
        r1="1m", r2="10k", r3="10k", vsig="0.5", d=[".op", ".lib uA741.lib"]),
    "exp2_nominal_op_max": dict(
        title="EEEN20020 Exp. 2 - NOMINAL - MAX gain - DC operating point at vin = +0.5 V (positive peak of 1 V pk-pk)",
        notes=["Run, and LTspice opens a table of every node voltage and branch current (screenshot it for Sec. B)"],
        r1="50k", r2="10k", r3="10k", vsig="0.5", d=[".op", ".lib uA741.lib"]),
    "exp2_measured_min_gain": dict(
        title="EEEN20020 Exp. 2 - Section G - MEASURED component values - MINIMUM gain",
        notes=["!! The .param values below are PROTOTYPE placeholders, NOT measurements. !!",
               "!! Replace them with your own DMM readings before using any result.      !!",
               "R1min_m = pot resistance measured at its minimum setting (end resistance)"],
        r1="{R1min_m}", r2="{R2_m}", r3="{R3_m}", vsig="SINE(0 {Vpk} 1k)",
        d=tran_dirs([".param R1min_m=35 R1max_m=47.62k R2_m=9.93k R3_m=9.97k"])),
    "exp2_measured_max_gain": dict(
        title="EEEN20020 Exp. 2 - Section G - MEASURED component values - MAXIMUM gain",
        notes=["!! The .param values below are PROTOTYPE placeholders, NOT measurements. !!",
               "!! Replace them with your own DMM readings before using any result.      !!",
               "R1max_m = pot resistance measured (wiper to the end you wired) at its maximum setting"],
        r1="{R1max_m}", r2="{R2_m}", r3="{R3_m}", vsig="SINE(0 {Vpk} 1k)",
        d=tran_dirs([".param R1min_m=35 R1max_m=47.62k R2_m=9.93k R3_m=9.97k"])),
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, v in VARIANTS.items():
        args = (v["title"], v["notes"], v["r1"], v["r2"], v["r3"], v["vsig"], v["d"])
        with open(os.path.join(OUT, name + ".asc"), "w", newline="\r\n") as f:
            f.write(asc(*args))
        with open(os.path.join(OUT, name + ".cir"), "w", newline="\r\n") as f:
            f.write(cir(*args))
    print("wrote", len(VARIANTS), "schematic/netlist pairs to", OUT)


if __name__ == "__main__":
    main()
