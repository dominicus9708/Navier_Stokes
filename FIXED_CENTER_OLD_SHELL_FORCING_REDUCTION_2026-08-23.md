# Fixed-Center Old-Shell Forcing Reduction — 2026-08-23

Overall status: **ACTIVE PROOF ATTEMPT — ON THE NO-T CENTER-NESTED BRANCH, THE OLD-SHELL FORCING CEILING DEPENDS ONLY ON TYPE-I/MORREY/DERIVATIVE CONSTANTS; COHERENT-CENTER SPEED IS REMOVED — GLOBAL REGULARITY NOT PROVED.**

This note combines the no-T center nesting from `TYPEI_CENTER_NESTING_AND_CUBIC_2026-08-20.md` with the old-shell forcing audit.

The purpose is to eliminate an unnecessary moving-center parameter from the historical-shell closure.

---

## 1. No-T gives one limiting physical center

The no-T center condition gives

\[
|X_{j+1}-X_j|\le C_Tr_j,
\]

and hence a limiting physical point `X_*` with

\[
|X_*-X_j|\le C_Xr_j.
\]

Thus the non-turnover historical tower is naturally organized around one fixed singular-point candidate `X_*`.

If this fixed-center organization fails by an unbounded normalized center replacement, that failure is already `T`.

Therefore the historical-shell analysis on the non-T branch may use radial cutoffs centered at the fixed point `X_*`.

---

## 2. Fixed shell cutoff

For an old shell radius `R`, take

\[
\chi_R(x)=\chi(|x-X_*|/R).
\]

Then

\[
\boxed{\partial_t\chi_R=0.}
\]

The compact solenoidal packet is again

\[
f_R=\chi_Ru-b_R,
\]

with

\[
\nabla\cdot b_R=\nabla\chi_R\cdot u.
\]

The exact packet equation becomes

\[
(\partial_t-\nu\Delta)f_R
=\mathcal N_R+\mathcal R_R,
\]

with

\[
\mathcal N_R
=-\mathbb P\nabla\cdot(\chi_Ru\otimes u),
\]

and

\[
\boxed{
\begin{aligned}
\mathcal R_R
=\mathbb P\big[&
(u\cdot\nabla\chi_R)u
+p\nabla\chi_R\\
&-2\nu\nabla\chi_R\cdot\nabla u
-\nu(\Delta\chi_R)u\\
&-\partial_tb_R+\nu\Delta b_R
\big].
\end{aligned}
}
\]

There is no center-motion term.

---

## 3. Material term now follows from the shell Type-I envelope

Assume

\[
R\|u\|_{L^\infty(A_R^+)}\le A_0,
\]

and

\[
R^{-1}\|u\|_{L^2(A_R^+)}^2\le E_0.
\]

Then

\[
\begin{aligned}
\|(u\cdot\nabla\chi_R)u\|_2
&\le
\|u\|_\infty
\|\nabla\chi_R\|_\infty
\|u\|_2\\
&\le
C A_0E_0^{1/2}R^{-3/2}.
\end{aligned}
\]

Hence

\[
\boxed{
\|\mathcal R_{mat}\|_2
\le
C A_0E_0^{1/2}R^{-3/2}.
}
\]

No independent relative-velocity or center-speed constant is needed.

---

## 4. Bogovskii time derivative simplifies

The annulus and Bogovskii operator are now fixed in physical space.

Let

\[
g_R=\nabla\chi_R\cdot u.
\]

Because the operator is time-independent,

\[
\partial_tb_R
=\mathcal B_R[\partial_tg_R]
=\mathcal B_R[\nabla\chi_R\cdot\partial_tu].
\]

Thus

\[
\|\partial_tg_R\|_2
\le
CR^{-1}\|\partial_tu\|_2.
\]

With

\[
T_0=R^{3/2}\|\partial_tu\|_2,
\]

we obtain

\[
\|\partial_tg_R\|_2
\le
CT_0R^{-5/2}.
\]

Since the Bogovskii inverse gains one spatial scale,

\[
\boxed{
\|\partial_tb_R\|_2
\le
C_BT_0R^{-3/2}.
}
\]

The center-motion correction terms from the previous audit disappear completely.

---

## 5. Pressure constants are not independent

By `OLD_SHELL_PRESSURE_OSCILLATION_MORREY_BOUND_2026-08-23.md`,

\[
P_0
\le
C
(A_0E_0^{1/2}+M_*),
\]

and

\[
P_1
\le
C
[A_0(G_0+E_0^{1/2})+M_*].
\]

Therefore pressure-buffer forcing and the pressure contribution to `partial_t u` are already controlled by the Type-I/Morrey/derivative corridor.

---

## 6. Time derivative is controlled by second derivative tightness

Using Navier--Stokes,

\[
\partial_tu
=\nu\Delta u-(u\cdot\nabla)u-\nabla p.
\]

Let

\[
H_2=R^{3/2}\|\nabla^2u\|_2.
\]

Then

\[
\boxed{
T_0
\le
C
\left[
\nu H_2
+A_0(G_0+E_0^{1/2})
+M_*
\right].
}
\]

Thus `T_0` introduces no new branch. If it is unbounded, second-derivative tightness, local amplitude/gradient control, or Morrey pressure control has already failed.

---

## 7. Reduced fixed-center forcing ceiling

Collecting the internal nonlinear, material, pressure, viscous, and Bogovskii estimates yields

\[
\boxed{
\|\mathcal N_R\|_2
+
\|\mathcal R_R\|_2
\le
K_*R^{-3/2},
}
\]

where now

\[
\boxed{
K_*
\le
\mathcal K_*
(A_0,E_0,G_0,H_2,M_*,\nu)
}
\]

for a function depending only on fixed cutoff/Bogovskii geometry and the displayed scale-invariant local quantities.

There is no independent

\[
V_0,
\quad
X_0,
\quad
P_0,
\quad
P_1,
\quad
T_0
\]

left in the final list.

---

## 8. Further reduction using Morrey energy

The parent Morrey corridor itself gives

\[
E_0
=R^{-1}\|u\|_{L^2(A_R^+)}^2
\le
C_M M_*.
\]

Hence schematically

\[
\boxed{
K_*
\le
\widetilde{\mathcal K}_*
(A_0,G_0,H_2,M_*,\nu).
}
\]

Therefore a scale-independent forcing ceiling follows from only four structural corridors:

1. old-shell Type-I amplitude `A_0`;
2. first-derivative tightness `G_0`;
3. second-derivative tightness `H_2`;
4. parent Morrey energy `M_*`.

---

## 9. Branch consequence

Insert this into the remaining-time contradiction

\[
c_*
\le
K_*C_TK_j^{-2}.
\]

If

\[
A_0,
G_0,
H_2,
M_*
\]

remain uniformly bounded on the selected old good shells, then `K_*` is fixed and

\[
K_j\to\infty
\]

makes quiet forgetting impossible.

If one of these quantities is not bounded, the historical shell has already left the quiet lane:

\[
\boxed{
\begin{aligned}
A_0\to\infty
&\Rightarrow
\text{super-Type-I shell amplitude / turnover or derivative escape},\\
G_0,H_2\to\infty
&\Rightarrow
H,\\
M_*\to\infty
&\Rightarrow
\text{parent local-energy / turnover branch}.
\end{aligned}
}
\]

If center nesting itself fails, that is `T` before this argument is invoked.

Thus the old-shell recycling route no longer needs a separate drift or pressure escape label.

---

## 10. Current status

On the no-T center-nested lane, the historical packet can be localized around the fixed point `X_*`. This removes all center-speed complications and reduces the entire forcing ceiling to Type-I amplitude, derivative tightness, and Morrey energy.

Combined with `SLIDING_HISTORY_REMAINING_TIME_CLOSURE_2026-08-23.md`, the independent historical-shell survivor is now routed as

\[
\boxed{
\text{historical recycling}
\Longrightarrow
H
\quad\text{or}\quad
T/\text{parent-energy failure},
}
\]

subject to theorem-level completion of the fixed-shell Bogovskii localization and explicit branch thresholds.

Status: **PRESSURE AND COHERENT-DRIFT ARE REMOVED AS INDEPENDENT HISTORICAL-SHELL ESCAPES ON THE NO-T CENTER-NESTED BRANCH. THE HISTORICAL RECYCLING PROBLEM IS REDUCED TO THE ALREADY EXISTING H OR T/PARENT-ENERGY EXITS. GLOBAL REGULARITY IS NOT PROVED.**
