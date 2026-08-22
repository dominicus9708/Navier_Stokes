# Sliding-History Duhamel Forgetting Tax — 2026-08-23

Overall status: **ACTIVE PROOF ATTEMPT — SLIDING-HISTORY FORGETTING REQUIRES ORDER-ONE NATURAL-SCALE NONLINEAR ACTION UNDER A NATURAL-FREQUENCY OCCUPANCY HYPOTHESIS — GLOBAL REGULARITY NOT PROVED.**

This note continues the two historical-shell reductions:

1. `HISTORICAL_SHELL_LOG_RADIAL_CRITICAL_LEDGER_2026-08-23.md`;
2. `SOLENOIDAL_HARDY_GAP_AND_SLIDING_HISTORY_2026-08-23.md`.

After the solenoidal Hardy-gap reduction, the main quiet survivor is a sliding historical window:

\[
N_j\to\infty,
\qquad
R_j\to0,
\qquad
K_j=R_j/r_j\to\infty.
\]

The oldest shells must therefore be continually forgotten. This note asks whether viscosity alone can perform that forgetting.

The answer at the natural frequency scale is no: over the remaining Type-I time, the heat semigroup supplies only an order-one attenuation. Strong forgetting therefore forces an order-one nonlinear Duhamel action.

---

## 1. Natural stage scale and remaining time

Let a historical packet be created or first detected at stage `m` with physical scale

\[
r_m\sim W_m^{-1/2}.
\]

For a Type-I first-hitting sequence, its remaining time to the hypothetical singular time has the natural size

\[
0<T^*-t_m\le C_T r_m^2.
\]

Let `P_m` denote a smooth Littlewood--Paley band projection to

\[
\boxed{
\frac{c_f}{r_m}
\le
|\xi|
\le
\frac{C_f}{r_m},
}
\]

where `0<c_f<C_f<infinity` are fixed scale-independent constants.

This is the natural frequency band associated with a packet of spatial scale `r_m`.

---

## 2. Heat semigroup cannot erase a natural-frequency packet by a scale-dependent factor

For any `f` whose Fourier support is in the above band,

\[
\widehat{e^{\nu\Delta t\Delta}f}(\xi)
=
e^{-\nu\Delta t|\xi|^2}\widehat f(\xi).
\]

If

\[
0\le\Delta t\le C_T r_m^2,
\]

then on the band

\[
\Delta t|\xi|^2
\le
C_T C_f^2.
\]

Therefore

\[
\boxed{
\|e^{\nu\Delta t\Delta}P_mf\|_2
\ge
\eta_\nu\|P_mf\|_2,
}
\]

with the scale-independent constant

\[
\boxed{
\eta_\nu
:=
e^{-\nu C_T C_f^2}>0.
}
\]

Thus an old natural-scale packet does not vanish merely because `m` is very large. Linear viscosity only multiplies it by an order-one factor before `T^*`.

---

## 3. Mild Navier--Stokes evolution in the natural band

For the whole-space smooth solution,

\[
u(t)
=e^{\nu(t-t_m)\Delta}u(t_m)
-
\int_{t_m}^{t}
 e^{\nu(t-s)\Delta}
\mathbb P\nabla\cdot(u\otimes u)(s)\,ds,
\]

where `mathbb P` is the Leray projector.

Apply `P_m`:

\[
P_mu(t)
=
e^{\nu(t-t_m)\Delta}P_mu(t_m)
-
\int_{t_m}^{t}
 e^{\nu(t-s)\Delta}
P_m\mathbb P\nabla\cdot(u\otimes u)(s)\,ds.
\]

Since the heat semigroup is an `L2` contraction,

\[
\left\|
\int_{t_m}^{t}
 e^{\nu(t-s)\Delta}
P_m\mathbb P\nabla\cdot(u\otimes u)(s)\,ds
\right\|_2
\le
\int_{t_m}^{t}
\|P_m\mathbb P\nabla\cdot(u\otimes u)(s)\|_2ds.
\]

---

## 4. Quantitative forgetting inequality

Assume that at the late time `t` the natural-band packet has been strongly forgotten:

\[
\|P_mu(t)\|_2
\le
\varepsilon
\|P_mu(t_m)\|_2,
\]

with

\[
0\le\varepsilon<\eta_\nu.
\]

The reverse triangle inequality and the heat lower bound give

\[
\begin{aligned}
\int_{t_m}^{t}
\|P_m\mathbb P\nabla\cdot(u\otimes u)(s)\|_2ds
&\ge
\|e^{\nu(t-t_m)\Delta}P_mu(t_m)\|_2
-
\|P_mu(t)\|_2\\
&\ge
(\eta_\nu-\varepsilon)
\|P_mu(t_m)\|_2.
\end{aligned}
\]

Hence

\[
\boxed{
\int_{t_m}^{t}
\|P_m\mathbb P\nabla\cdot(u\otimes u)(s)\|_2ds
\ge
(\eta_\nu-\varepsilon)
\|P_mu(t_m)\|_2.
}
\]

Define the dimensionless nonlinear forgetting action

\[
\boxed{
\mathcal T_m^{NL}(t)
:=
\frac{
\int_{t_m}^{t}
\|P_m\mathbb P\nabla\cdot(u\otimes u)(s)\|_2ds
}{
\|P_mu(t_m)\|_2
}.
}
\]

Then every strongly forgotten natural-frequency shell satisfies

\[
\boxed{
\mathcal T_m^{NL}(t)
\ge
\eta_\nu-\varepsilon
>0.
}
\]

This lower bound is independent of the shell index `m`.

---

## 5. Scaling check

For a critical packet of radius `r_m` and velocity amplitude `r_m^{-1}`,

\[
\|u_m\|_2
\sim
r_m^{1/2}.
\]

The nonlinear term has natural size

\[
|(u\cdot\nabla)u|
\sim
r_m^{-3},
\]

so

\[
\|(u\cdot\nabla)u\|_2
\sim
r_m^{-3/2}.
\]

Over a natural time interval `r_m^2`,

\[
\int\|(u\cdot\nabla)u\|_2dt
\sim
r_m^{1/2}.
\]

Thus the numerator and denominator of `mathcal T_m^{NL}` have the same scale.

Therefore

\[
\boxed{
\mathcal T_m^{NL}
}
\]

is exactly a scale-invariant turnover/cancellation action.

This is the correct scaling for a branch label `T`.

---

## 6. Natural-frequency occupancy dichotomy

To use the forgetting lemma on a spatial historical shell, one must first show that a fixed fraction of the shell's dynamically relevant mass occupies its natural frequency band.

Let `f_m` denote a divergence-free localized packet representing the historical shell and assume

\[
\boxed{
\|P_mf_m\|_2
\ge
\beta\|f_m\|_2
}
\]

for some scale-independent `beta>0`.

Then strong forgetting forces

\[
\mathcal T_m^{NL}\ge c(\nu,C_T,C_f,\varepsilon)>0.
\]

If natural-frequency occupancy fails, the missing mass must be classified into frequency escape channels:

### Low-frequency escape

If substantial packet mass lies at

\[
|\xi|\ll r_m^{-1},
\]

then the packet is no longer genuinely localized to its natural first-hitting scale. It feeds the low-frequency drift / parent-scale / coherent-frame channel and should be routed toward `T` or the drift-gauge branch.

### High-frequency escape

If substantial mass lies at

\[
|\xi|\gg r_m^{-1},
\]

then the shell contains derivative mass beyond its natural profile. By Bernstein scaling this increases gradient/palinstrophy cost and should be routed toward `H`.

Thus the phase-space refinement has the intended structure

\[
\boxed{
\text{natural band}
\Rightarrow
\text{forgetting costs }T,
}
\]

\[
\boxed{
\text{low-frequency escape}
\Rightarrow
T/\text{drift},
}
\]

\[
\boxed{
\text{high-frequency escape}
\Rightarrow
H.
}
\]

The quantitative thresholds for the low/high-frequency branches remain to be proved.

---

## 7. Consequence for the sliding historical window

A sliding historical window requires old shells to disappear continually:

\[
N_j\to\infty,
\qquad
j-N_j\to\infty.
\]

Hence infinitely many historical packets must eventually cross from "remembered" to "forgotten" status.

Under natural-frequency occupancy, every such crossing pays

\[
\boxed{
\mathcal T_m^{NL}\ge c_*>0.
}

Therefore the sliding branch cannot be both

- continually forgetful; and
- uniformly `T`-quiet at every old-shell transition.

This does not yet give a global finite-sum contradiction: the physical `L2` action of a scale-`r_m` packet is `O(r_m^{1/2})`, which is geometrically summable. The gain is instead branch-theoretic: **forgetting itself is an order-one normalized nonlinear turnover event.**

If the pre-existing `T` closure is formulated in terms of natural-scale normalized turnover, the sliding branch is routed into `T`.

---

## 8. Localization issue

The formula above is exact for a whole-space Littlewood--Paley component of `u`.

A historical shell is a spatially localized object. A rigorous phase-space packet requires a localization operator, wavelet, or cutoff plus divergence correction. Then the packet evolution contains commutators of the form

\[
[\chi_m,u\cdot\nabla]u,
\qquad
[\chi_m,\Delta]u,
\qquad
[\chi_m,\mathbb P]\nabla\cdot(u\otimes u).
\]

These terms must not be discarded. Structurally they represent exactly

- material crossing of the shell boundary;
- derivative leakage across scales;
- pressure/nonlocal coupling;
- or coherent-frame drift.

Hence a successful localization audit should route the commutators into `T`, `H`, or pressure/drift branches rather than treating them as errors with no interpretation.

---

## 9. Combined historical-shell reduction after three steps

The historical branch is now organized as follows.

### A. Persistent history

Old shells remain to a fixed positive physical outer scale.

The solenoidal Hardy gap forces logarithmically growing weighted radial kinetic/pressure flux.

\[
\boxed{\text{persistent history}\Rightarrow T}
\]

subject to localization.

### B. Sliding history with natural-frequency occupancy

Old shells are continually forgotten while their scale-`r_m` band remains nontrivial.

The Duhamel forgetting inequality forces

\[
\boxed{\mathcal T_m^{NL}\ge c_*>0.}
\]

Hence

\[
\boxed{\text{sliding + natural band}\Rightarrow T.}
\]

### C. Sliding history without natural-frequency occupancy

The packet escapes to frequencies much lower or much higher than `r_m^{-1}`.

The intended routing is

\[
\boxed{\text{low frequency}\Rightarrow T/\text{drift},}
\]

\[
\boxed{\text{high frequency}\Rightarrow H.}
\]

The only genuinely unresolved point is to prove these phase-space routing estimates with the spatial shell localization and moving coherent frame used by the main proof tree.

---

## 10. Next theorem target

The next calculation should establish a **localized phase-space trichotomy** for every natural historical packet:

\[
\boxed{
\text{natural-band occupancy}
\quad\vee\quad
\text{low-frequency escape}
\quad\vee\quad
\text{high-frequency escape}.
}
\]

with quantitative implications

\[
\boxed{
\begin{aligned}
\text{natural band + forgetting}&\Longrightarrow T,\\
\text{low-frequency escape}&\Longrightarrow T/\text{drift},\\
\text{high-frequency escape}&\Longrightarrow H.
\end{aligned}
}
\]

If this trichotomy is made theorem-level and the already developed `H/T` closures accept these normalized costs, the historical-shell recycling branch would be closed.

Status: **LINEAR DIFFUSION ALONE CANNOT PRODUCE SCALE-DEPENDENT FORGETTING OF A NATURAL-FREQUENCY HISTORICAL PACKET. STRONG FORGETTING FORCES AN ORDER-ONE NORMALIZED NONLINEAR DUHAMEL ACTION. THE REMAINING TECHNICAL BOTTLENECK IS SPATIAL/PHASE-SPACE LOCALIZATION AND ROUTING OF LOW/HIGH-FREQUENCY ESCAPE. GLOBAL REGULARITY IS NOT PROVED.**
