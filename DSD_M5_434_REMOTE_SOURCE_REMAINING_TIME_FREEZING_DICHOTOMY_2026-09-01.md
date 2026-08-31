# DSD M5-434 — Remote-source remaining-time freezing dichotomy

Date: 2026-09-01

Status: **THE GENERAL REMOTE STRAIN SOURCE OF M5-433 CAN BE FED INTO THE EXISTING COMPACT SOLENOIDAL PHASE-SPACE / REMAINING-TIME OLD-SHELL MACHINERY / OUTSIDE THE LARGE-DERIVATIVE BRANCH, ITS FORCED SOURCE ENERGY PRODUCES A NATURAL-BAND PACKET OF SIZE `~ nu K^2 R^(1/2)` WHILE ONLY `O(K^-2 R^(1/2))` QUIET FORCING ACTION IS AVAILABLE BEFORE THE HYPOTHETICAL SINGULAR TIME / THUS QUIET ERASURE HAS A `K^4` DEFICIT / A SUFFICIENTLY REMOTE FIXED-FRACTION SOURCE MUST EITHER ENTER STRONG CRITICAL DERIVATIVE/FORCING THROUGHPUT OR FREEZE AS A PHYSICAL OLD-SHELL PACKET TOWARD THE TERMINAL TIME / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Setup

Let the first-hitting target at stage `j` have natural scale

\[
r_j=\sqrt{\frac{\nu}{W_j}},
\]

and suppose a fixed fraction of its natural strain

\[
\frac{\nu}{r_j^2}
\]

is supplied by a dyadic-thickness source annulus of physical radius

\[
R_j\gg r_j.
\]

Set

\[
\boxed{K_j:=\frac{R_j}{r_j}\to\infty.}
\]

Assume the center-nesting corridor, so the remaining physical time obeys the established first-hitting estimate

\[
\boxed{T_*-t_j\le C_T\frac{r_j^2}{\nu}}
\]

with a fixed dimensionless constant `C_T` after the viscosity normalization is restored.

The source annulus has its own parabolic time

\[
\frac{R_j^2}{\nu},
\]

therefore

\[
\boxed{
\frac{T_*-t_j}{R_j^2/\nu}
\le C_TK_j^{-2}.
}
\]

Thus a genuinely remote source is already an old shell in the precise remaining-time sense of the historical-shell machinery.

---

## 2. Imported source-energy lower bound from M5-433

M5-433 proves that a fixed-fraction remote strain payer satisfies

\[
\boxed{
\|u(t_j)\|_{L^2(A_j^+)}
\ge c_E\nu R_j^{5/2}r_j^{-2},
}
\]

hence

\[
\boxed{
E_j^{src}
:=\int_{A_j^+}|u(x,t_j)|^2dx
\ge c_E^2\nu^2\frac{R_j^5}{r_j^4}.
}
\]

This conclusion is independent of an affine ansatz.

Partition `A_j^+` into a fixed finite number of comparable subannuli. At least one retained subannulus carries a fixed fraction of this energy. Choose the radial cutoff/Bogovskii localization so that the compact solenoidal packet `f_j` equals `u` on that retained subannulus.

Then

\[
\boxed{
\|f_j(t_j)\|_2
\ge c_f\nu R_j^{5/2}r_j^{-2}.
}
\]

Equivalently,

\[
\boxed{
\|f_j(t_j)\|_2
\ge c_f\nu K_j^2R_j^{1/2}.
}
\]

The remote strain payer is therefore much larger than an ordinary natural old-shell packet, whose canonical size is only `~R_j^(1/2)`.

---

## 3. Phase-space trichotomy at the remote source scale

Apply `LOCALIZED_SOLENOIDAL_PHASE_SPACE_TRICHOTOMY_2026-08-23.md` to `f_j` at scale `R_j`.

Define

\[
\Gamma_j
:=
\frac{R_j\|\nabla f_j\|_2}{\|f_j\|_2}.
\]

There are two branches.

### A. Large derivative ratio

If

\[
\Gamma_j>\Gamma_*,
\]

then the remote source already lies in the localized derivative/frequency critical-throughput branch.

This is not a quiet old shell.

### B. Bounded derivative ratio

If

\[
\Gamma_j\le\Gamma_*,
\]

then low frequencies are suppressed by compact support plus solenoidality and high frequencies are suppressed by the derivative bound. Therefore there are fixed `0<a<b<infinity` and `beta_*>0` such that

\[
\boxed{
\|P_jf_j(t_j)\|_2
\ge\beta_*\|f_j(t_j)\|_2
\ge c_P\nu K_j^2R_j^{1/2},
}
\]

where `P_j` projects to the natural shell band

\[
\frac a{R_j}<|\xi|<\frac b{R_j}.
\]

Thus a quiet remote strain source contains a very large natural-frequency old-shell packet.

---

## 4. Suppose the source is strongly forgotten before T*

Assume there is a later time

\[
t_j^f<T_*
\]

at which the localized moving packet has lost a fixed fraction of its original natural-band norm:

\[
\|P_jf_j(t_j^f)\|_2
\le\varepsilon\|P_jf_j(t_j)\|_2,
\qquad0<\varepsilon<1.
\]

The exact localized Duhamel forgetting gate and the fact that only `O(K_j^-2)` of one source-natural time remains imply

\[
\boxed{
\int_{t_j}^{t_j^f}
\left(
\|P_j\mathcal N_j\|_2
+
\|P_j\mathcal R_j\|_2
\right)dt
\ge c_D\|P_jf_j(t_j)\|_2.
}
\]

Hence

\[
\boxed{
\int_{t_j}^{t_j^f}(\cdots)dt
\ge c_Dc_P\nu K_j^2R_j^{1/2}.
}
\]

This is the action actually required to erase the source packet.

---

## 5. Quiet forcing can supply only K^-2 of the natural packet scale

The old-shell forcing audit gives, on the bounded Type-I / derivative / pressure / coherent-frame corridor,

\[
\boxed{
\|P_j\mathcal N_j(t)\|_2
+
\|P_j\mathcal R_j(t)\|_2
\le K_*R_j^{-3/2}
}
\]

with a scale-independent `K_*`.

Integrating only until `T_*`,

\[
\begin{aligned}
\int_{t_j}^{t_j^f}(\cdots)dt
&\le K_*R_j^{-3/2}(T_*-t_j)\\
&\le C_TK_*R_j^{-3/2}\frac{r_j^2}{\nu}.
\end{aligned}
\]

Since `r_j=R_j/K_j`,

\[
\boxed{
\int_{t_j}^{t_j^f}(\cdots)dt
\le
\frac{C_TK_*}{\nu}
K_j^{-2}R_j^{1/2}.
}
\]

Comparing this with the required lower action yields

\[
c_Dc_P\nu K_j^2
\le
\frac{C_TK_*}{\nu}K_j^{-2}.
\]

Therefore

\[
\boxed{
K_j^4
\le
\frac{C_TK_*}{c_Dc_P\nu^2}.
}
\]

This is impossible once `K_j` is sufficiently large.

Thus the remote source has a **quartic remaining-time forgetting gap**.

---

## 6. Remote-source dichotomy

For a sufficiently remote fixed-fraction strain source, one of the following must hold:

1. `Gamma_j` is large: localized derivative/frequency critical throughput;
2. the quiet forcing ceiling fails: nonlinear/material/pressure/viscous/interface critical throughput;
3. the source natural-band packet is not strongly forgotten before `T_*`.

Hence

\[
\boxed{
S_{remote}^{fixed\ fraction}
\Longrightarrow
H_{strong\ throughput}
\lor
F_{frozen\ old\ shell}.
}
\]

The second branch means the remote source survives as an approximately frozen physical shell packet because the remaining target time is too short for natural-scale evolution of that shell.

---

## 7. Relation to the existing frozen-conveyor theorem

`DSD_FROZEN_CRITICAL_OLD_SHELL_CONVEYOR_2026-08-25.md` already proves that an age-`k` quiet natural-frequency shell changes by only `O(q^-k)` per current stage and that its total future variation is summable.

The present note supplies a new upstream bridge:

\[
\boxed{
\text{general fixed-fraction remote strain payer}
\Longrightarrow
\text{large compact natural-band old-shell packet}
}
\]

outside derivative throughput.

Therefore the general remote-source problem can enter the frozen-conveyor theorem without assuming a historical weak-`L3` tail construction first.

---

## 8. DSD audit

### Derived

- M5-433 source energy gives packet norm `~nu K^2 R^(1/2)`;
- compact solenoidal localization removes genuine low-frequency escape;
- bounded derivative ratio forces natural-band occupancy;
- strong forgetting requires `~nu K^2 R^(1/2)` forcing action;
- quiet remaining-time forcing supplies only `~K^-2 R^(1/2)`;
- the gap is quartic in `K`.

### Firewall

- the argument does not say a frozen remote shell is contradictory;
- failure of the quiet forcing ceiling is only routed to the already retained critical-throughput class;
- no energy is summed across different source times in this note;
- a separate packing step is required before using many frozen source shells simultaneously.

---

## 9. Updated remote frontier

Combining M5-433 and M5-434,

\[
\boxed{
\text{fixed-fraction remote source}
\Longrightarrow
A_{energy\ atom}
\lor
H_{strong\ throughput}
\lor
F_{sub5\ frozen}.
}
\]

Here the non-atomic frozen lane satisfies

\[
R_j=o(r_j^{4/5}),
\qquad
R_j/r_j\to\infty.
\]

The next step is to pack geometrically separated frozen source shells at one common late physical time, eliminating time-slice double counting.

---

## 10. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
