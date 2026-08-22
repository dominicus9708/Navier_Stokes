# Localized Packet Exact Evolution and Forgetting Gate — 2026-08-23

Overall status: **ACTIVE PROOF ATTEMPT — NATURAL-BAND FORGETTING NOW HAS AN EXACT LOCALIZED DUHAMEL GATE; THE REMAINING ISSUE IS TO BOUND OR TYPE THE BOUNDARY/CORRECTION ACTION — GLOBAL REGULARITY NOT PROVED.**

This note continues `LOCALIZED_SOLENOIDAL_PHASE_SPACE_TRICHOTOMY_2026-08-23.md` and `SLIDING_HISTORY_DUHAMEL_FORGETTING_TAX_2026-08-23.md`.

The previous phase-space lemma shows that every genuinely occupied non-H historical shell has a fixed `L2` fraction in a natural Fourier band. The present step writes the exact evolution of the compact solenoidal packet and identifies all terms that can erase that band.

---

## 1. Time-dependent shell packet

Fix a historical physical radius `r` and a smooth moving center `X(t)`.

Let

\[
\chi_r(x,t)=\chi(|x-X(t)|/r)
\]

with the same fixed-shape inner/core/outer annuli as in the localization lemma.

Let `b_r(t)` be the Bogovskii correction supported in the transition annuli, satisfying

\[
\nabla\cdot b_r
=\nabla\chi_r\cdot u.
\]

Define

\[
\boxed{
f_r=\chi_ru-b_r,
\qquad
\nabla\cdot f_r=0.
}
\]

The radius may also be allowed to vary; for clarity this note keeps the historical radius fixed. A variable radius produces one additional cutoff-velocity term proportional to `dot r` and is naturally another shell-boundary action.

---

## 2. Exact localized equation before Leray projection

The smooth Navier--Stokes equation is

\[
\partial_tu-
u\Delta u
=-(u\cdot\nabla)u-\nabla p.
\]

Multiplying by `chi_r` gives

\[
\begin{aligned}
(\partial_t-\nu\Delta)(\chi_ru)
&=-\chi_r(u\cdot\nabla)u
-\chi_r\nabla p\\
&\quad
+(\partial_t\chi_r)u
-2\nu\nabla\chi_r\cdot\nabla u
-\nu(\Delta\chi_r)u.
\end{aligned}
\]

Use

\[
\chi_r(u\cdot\nabla)u
=\nabla\cdot(\chi_ru\otimes u)
-(u\cdot\nabla\chi_r)u
\]

and

\[
\chi_r\nabla p
=\nabla(\chi_rp)-p\nabla\chi_r.
\]

Subtracting the Bogovskii correction yields

\[
\begin{aligned}
(\partial_t-\nu\Delta)f_r
&=-\nabla\cdot(\chi_ru\otimes u)
-\nabla(\chi_rp)\\
&\quad
+(\partial_t\chi_r+u\cdot\nabla\chi_r)u
+p\nabla\chi_r\\
&\quad
-2\nu\nabla\chi_r\cdot\nabla u
-\nu(\Delta\chi_r)u\\
&\quad
-\partial_tb_r+\nu\Delta b_r.
\end{aligned}
\]

---

## 3. Exact solenoidal packet equation

Apply the Leray projector `mathbb P`. Since `f_r` is divergence free and the heat operator commutes with `mathbb P`, while

\[
\mathbb P\nabla(\chi_rp)=0,
\]

we obtain

\[
\boxed{
(\partial_t-\nu\Delta)f_r
=
\mathcal N_r
+
\mathcal R_r,
}
\]

where the internal localized nonlinear term is

\[
\boxed{
\mathcal N_r
:=-\mathbb P\nabla\cdot(\chi_ru\otimes u),
}
\]

and the complete localization remainder is

\[
\boxed{
\begin{aligned}
\mathcal R_r
:=\mathbb P\big[&
(\partial_t\chi_r+u\cdot\nabla\chi_r)u
+p\nabla\chi_r\\
&-2\nu\nabla\chi_r\cdot\nabla u
-\nu(\Delta\chi_r)u\\
&-\partial_tb_r+\nu\Delta b_r
\big].
\end{aligned}
}
\]

No pressure term remains in the packet interior. Pressure survives only through the shell transition factor `p grad chi_r`.

---

## 4. Interpretation of every remainder term

For a moving radial cutoff,

\[
\partial_t\chi_r
=-\dot X\cdot\nabla\chi_r.
\]

Thus

\[
(\partial_t\chi_r+u\cdot\nabla\chi_r)u
=
((u-\dot X)\cdot\nabla\chi_r)u.
\]

This is exactly material crossing of the shell boundary relative to the coherent center.

The other terms have equally direct meanings:

\[
\boxed{
\begin{array}{rcl}
((u-\dot X)\cdot\nabla\chi_r)u
&:& \text{material/kinetic shell crossing},\\[2mm]
p\nabla\chi_r
&:& \text{pressure transfer across the shell buffer},\\[2mm]
-2\nu\nabla\chi_r\cdot\nabla u
-\nu(\Delta\chi_r)u
&:& \text{viscous diffusion through the shell boundary},\\[2mm]
-\partial_tb_r+\nu\Delta b_r
&:& \text{solenoidal correction needed to encode those boundary changes}.
\end{array}
}
\]

Hence the localization does not introduce an untyped bulk mechanism. Every new source is a boundary/correction action.

---

## 5. Mild formula and fixed natural band

Let `P_r` denote a fixed Fourier projector to the natural band selected in the phase-space lemma,

\[
\frac a r<|\xi|<\frac b r,
\]

with fixed `0<a<b<infinity`.

For `t>=t_0`,

\[
\begin{aligned}
P_rf_r(t)
&=e^{\nu(t-t_0)\Delta}P_rf_r(t_0)\\
&\quad+
\int_{t_0}^{t}
 e^{\nu(t-s)\Delta}
P_r\mathcal N_r(s)ds\\
&\quad+
\int_{t_0}^{t}
 e^{\nu(t-s)\Delta}
P_r\mathcal R_r(s)ds.
\end{aligned}
\]

Assume the remaining lifetime obeys the Type-I natural-time ceiling

\[
0<t-t_0\le C_Tr^2.
\]

Then on the band

\[
\boxed{
\|e^{\nu(t-t_0)\Delta}P_rf_r(t_0)\|_2
\ge
\eta_*\|P_rf_r(t_0)\|_2,
}
\]

where

\[
\boxed{
\eta_*
:=e^{-\nu C_Tb^2}>0.
}
\]

---

## 6. Exact localized forgetting gate

Suppose the historical shell has been strongly forgotten at time `t` in its original natural band:

\[
\|P_rf_r(t)\|_2
\le
\varepsilon
\|P_rf_r(t_0)\|_2,
\qquad
0\le\varepsilon<\eta_*.
\]

The reverse triangle inequality and the heat lower bound give

\[
\boxed{
\int_{t_0}^{t}
\left(
\|P_r\mathcal N_r(s)\|_2
+
\|P_r\mathcal R_r(s)\|_2
\right)ds
\ge
(\eta_*-\varepsilon)
\|P_rf_r(t_0)\|_2.
}
\]

Define normalized actions

\[
\mathcal A_N
:=
\frac{
\int_{t_0}^{t}\|P_r\mathcal N_r\|_2ds
}{
\|P_rf_r(t_0)\|_2
},
\]

\[
\mathcal A_R
:=
\frac{
\int_{t_0}^{t}\|P_r\mathcal R_r\|_2ds
}{
\|P_rf_r(t_0)\|_2
}.
\]

Then

\[
\boxed{
\mathcal A_N+\mathcal A_R
\ge
\eta_*-\varepsilon.
}
\]

Therefore at least one of

\[
\boxed{
\mathcal A_N
\ge
\frac{\eta_*-\varepsilon}{2}
}
\]

or

\[
\boxed{
\mathcal A_R
\ge
\frac{\eta_*-\varepsilon}{2}
}
\]

must occur.

This is the exact localized version of the previous Duhamel forgetting tax.

---

## 7. Internal forgetting versus boundary forgetting

The two alternatives have a clean structural interpretation.

### Internal nonlinear forgetting

If

\[
\mathcal A_N
\ge
c_*>0,
\]

then the shell undergoes order-one scale-invariant nonlinear frequency/shape turnover before it is forgotten.

This is the direct `T_NL` channel.

### Boundary/correction forgetting

If

\[
\mathcal A_R
\ge
c_*>0,
\]

then the shell is forgotten through at least one of

- advective/material crossing relative to `X(t)`;
- pressure transfer across the shell buffer;
- viscous shell leakage;
- the divergence correction generated by those boundary changes.

This is not an error term. It is an order-one normalized shell-boundary action.

Thus a forgotten natural-band shell cannot disappear silently.

---

## 8. Scale invariance of the gate

For a natural packet

\[
|u|\sim r^{-1},
\qquad
\|f_r\|_2\sim r^{1/2}.
\]

Every natural forcing term in `N_r` or `R_r` has pointwise scale `r^{-3}` and hence `L2` scale

\[
r^{-3/2}.
\]

Integrated over a natural time `r^2`, its action has scale

\[
r^{1/2},
\]

matching the packet norm.

Therefore

\[
\mathcal A_N,
\qquad
\mathcal A_R
\]

are dimensionless and scale invariant. The forgetting gate is not an artifact of physical units.

---

## 9. Conditional minimum forgetting time under a quiet-corridor forcing ceiling

Suppose a non-H/non-T/non-pressure corridor provides a scale-independent forcing ceiling

\[
\boxed{
\|P_r\mathcal N_r(s)\|_2
+
\|P_r\mathcal R_r(s)\|_2
\le
K_*r^{-3/2}
}
\]

through the relevant interval.

Suppose also the good-shell occupancy estimate gives

\[
\|P_rf_r(t_0)\|_2
\ge
\beta_*\|f_r(t_0)\|_2
\ge
c_f r^{1/2},
\]

with fixed `beta_*,c_f>0`.

Then the forgetting gate implies

\[
K_*r^{-3/2}(t-t_0)
\ge
(\eta_*-\varepsilon)c_fr^{1/2}.
\]

Hence

\[
\boxed{
 t-t_0
\ge
L_{forget}^{phys}
:=
\frac{(\eta_*-\varepsilon)c_f}{K_*}
r^2.
}
\]

In the shell's own parabolic clock

\[
\tau=(t-t_0)/r^2,
\]

this is

\[
\boxed{
\tau_{forget}
\ge
\frac{(\eta_*-\varepsilon)c_f}{K_*}
=:L_{forget}>0.
}
\]

Thus a quiet non-H/non-T shell cannot be erased in arbitrarily small normalized time.

This is the direct analogue, for historical forgetting, of the finite-stage lower-time gates already used in the smooth closure matrix.

---

## 10. Relation to the existing finite-stage closure matrix

The current smooth matrix already contains lower-time gates for

- cross-order projective production;
- coherent deformation;
- robust material-vorticity-flux change;
- transverse-axis swap.

The present calculation adds a fifth mechanism-specific floor:

\[
\boxed{
L_{forget}>0
}
\]

for a genuinely occupied historical shell to disappear while all forcing channels remain below their chosen quiet-corridor ceilings.

However, a historical shell may live across several later first-hitting stages. Therefore `L_forget` cannot yet simply be compared with one current stage ceiling `L_var` without a lifetime-to-stage packing lemma.

The next required bridge is temporal:

> how many geometrically later first-hitting stages fit inside one old shell's natural lifetime, and can a sliding window discard a positive-density sequence of good shells while keeping every later stage below all existing T/H thresholds?

---

## 11. Immediate remaining task

The spatial/phase-space and local Duhamel parts are now explicit. The unresolved task has changed from a commutator identity to a quantitative temporal packing problem.

One must combine

\[
\text{positive density of good historical shells}
\]

with

\[
\tau_{forget}\ge L_{forget}>0
\]

and the geometric first-hitting times

\[
r_m^2\sim W_m^{-1}
\]

to determine whether the required forgetting intervals can overlap/reuse the same nonlinear/boundary action indefinitely.

If the action for many shells cannot be recycled, stage packing closes the sliding-history branch.

If it can be recycled, the recycling mechanism itself must be isolated as a coherent multiscale `T` event rather than counted shell by shell.

Status: **EVERY FORGOTTEN GOOD NON-H HISTORICAL SHELL PAYS ORDER-ONE NORMALIZED INTERNAL OR BOUNDARY ACTION, AND UNDER A QUIET FORCING CEILING REQUIRES A FIXED POSITIVE NATURAL-SCALE TIME. THE NEW BOTTLENECK IS WHETHER ONE MULTISCALE EVENT CAN PAY FOR MANY SHELLS AT ONCE. GLOBAL REGULARITY IS NOT PROVED.**
