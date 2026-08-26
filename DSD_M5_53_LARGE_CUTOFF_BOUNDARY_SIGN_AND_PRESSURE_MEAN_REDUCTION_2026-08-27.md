# DSD M5-53 — Large-Cutoff Boundary Sign and Pressure-Mean Reduction

Date: 2026-08-27

Status: **EXACT SIGN/SCALING AUDIT OF THE M5-50 CUTOFF LEDGER UNDER THE CRITICAL TAIL ENVELOPES / FOR A STANDARD MONOTONE RADIAL CUTOFF THE ONLY ORDER-ONE LARGE-R BOUNDARY TERM HAS NONPOSITIVE SIGN / ALL OTHER CUTOFF TERMS ARE `O(R^-2)` / THEREFORE POSITIVE-DENSITY CORE `D3` DISSIPATION CANNOT BE SUSTAINED BY A POSITIVE SIMILARITY-BOUNDARY MEAN AT LARGE R AND MUST BE MATCHED BY POSITIVE MEAN PRESSURE WORK / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-52 produced the long-time normalized balance

\[
\nu\overline{\mathcal D_{3,R}}
=
\overline{\mathcal P_R}
+
\overline{\mathcal B_R}
\]

up to the vanishing bounded endpoint term.

It left two possible positive supports:

1. pressure work;
2. cutoff/log-shell boundary work.

The second branch can be audited more sharply at large cutoff radius.

---

## 2. Standard monotone radial cutoff

Choose

\[
\chi_R(y)=\chi(|y|/R),
\]

where

\[
0\le\chi\le1,
\qquad
\chi(s)=1\quad(s\le1),
\qquad
\chi(s)=0\quad(s\ge2),
\]

and

\[
\chi'(s)\le0.
\]

Then on the cutoff annulus

\[
A_R:=\{R<|y|<2R\},
\]

we have

\[
y\cdot\nabla\chi_R\le0,
\]

\[
|\nabla\chi_R|\le C_\chi R^{-1},
\qquad
|\Delta\chi_R|\le C_\chi R^{-2}.
\]

---

## 3. Boundary decomposition from M5-50

The localized cubic ledger is

\[
\frac13\frac d{d\eta}\mathfrak L_R
+
\nu\mathcal D_{3,R}
=
\mathcal P_R
+
\mathcal B_R,
\]

where

\[
\mathcal P_R
=
\int\chi_RP\,\nabla\cdot(|U|U)dy
\]

and

\[
\mathcal B_R
=
B_R^{drift}
+B_R^{adv}
+B_R^{press}
+B_R^{visc},
\]

with

\[
B_R^{drift}
:=
\frac16
\int |U|^3 y\cdot\nabla\chi_Rdy,
\]

\[
B_R^{adv}
:=
\frac13
\int |U|^3U\cdot\nabla\chi_Rdy,
\]

\[
B_R^{press}
:=
\int P|U|U\cdot\nabla\chi_Rdy,
\]

and

\[
B_R^{visc}
:=
\frac\nu3
\int |U|^3\Delta\chi_Rdy.
\]

---

## 4. Exact sign of the similarity-drift boundary term

Because

\[
|U|^3\ge0
\]

and

\[
y\cdot\nabla\chi_R\le0,
\]

we have the exact pointwise-sign result

\[
\boxed{
B_R^{drift}\le0.
}
\]

This is the only cutoff term that is potentially order one under a critical `1/r` tail.

Hence the leading similarity-shell contribution is a sink in the right-hand-side convention of the M5-50 ledger, not a positive source.

---

## 5. Critical tail envelopes

Assume uniformly on the recurrent W1 orbit, for sufficiently large `|y|`,

\[
|U(y,\eta)|
\le
\frac{M_U}{|y|},
\]

and the corresponding pressure tail obeys

\[
|P(y,\eta)|
\le
\frac{M_P}{|y|^2}.
\]

The velocity bound is the M5-42/M5-48 critical tail envelope used in M5-51.

The pressure bound is the matching critical pressure scaling and is retained here as an explicit hypothesis.

---

## 6. Advective cutoff term is `O(R^-2)`

On `A_R`,

\[
|U|\lesssim M_UR^{-1}.
\]

Therefore

\[
\begin{aligned}
|B_R^{adv}|
&\le
C
\int_{A_R}|U|^4|\nabla\chi_R|dy\\
&\le
C M_U^4
R^{-4}R^{-1}|A_R|\\
&\le
\boxed{C M_U^4R^{-2}}.
\end{aligned}
\]

---

## 7. Pressure cutoff term is `O(R^-2)`

Likewise,

\[
\begin{aligned}
|B_R^{press}|
&\le
C
\int_{A_R}|P||U|^2|\nabla\chi_R|dy\\
&\le
C M_PM_U^2
R^{-2}R^{-2}R^{-1}|A_R|\\
&\le
\boxed{C M_PM_U^2R^{-2}}.
\end{aligned}
\]

---

## 8. Viscous cutoff term is `O(R^-2)`

Finally,

\[
\begin{aligned}
|B_R^{visc}|
&\le
C\nu
\int_{A_R}|U|^3|\Delta\chi_R|dy\\
&\le
C\nu M_U^3
R^{-3}R^{-2}|A_R|\\
&\le
\boxed{C\nu M_U^3R^{-2}}.
\end{aligned}
\]

---

## 9. Large-cutoff upper bound for the full boundary term

Combining Sections 4--8,

\[
\mathcal B_R
\le
B_R^{drift}
+
C_*(M_U,M_P,\nu)R^{-2}.
\]

Since `B_R^{drift}\le0`,

\[
\boxed{
\mathcal B_R(\eta)
\le
C_*R^{-2}
}
\]

uniformly in normalized time.

Therefore

\[
\boxed{
\limsup_{R\to\infty}
\sup_\eta
\mathcal B_R(\eta)
\le0.
}
\]

The boundary term may remain negative order one because of the critical cubic tail, but it cannot remain a positive order-one source.

---

## 10. Consequence for long-time mean support

M5-52 gives, for each fixed `R`,

\[
\nu\overline{\mathcal D_{3,R}}
=
\overline{\mathcal P_R}
+
\overline{\mathcal B_R}
\]

in the long-time mean, up to the vanishing bounded endpoint contribution.

Suppose the robust positive-density pump windows yield

\[
\overline{\mathcal D_{3,R}}
\ge d_0>0
\]

for every sufficiently large cutoff containing the pump core.

Then

\[
\overline{\mathcal P_R}
\ge
\nu d_0
-
C_*R^{-2}.
\]

Choose `R` large enough that

\[
C_*R^{-2}
\le
\frac12\nu d_0.
\]

Then

\[
\boxed{
\overline{\mathcal P_R}
\ge
\frac12\nu d_0
>0.
}
\]

Thus the positive mean support cannot be assigned to the similarity-shell boundary at large radius.

It must be carried by pressure work.

---

## 11. Combination with M5-51

M5-51 shows that pressure generated at source radii beyond a sufficiently large `S` contributes arbitrarily little to a fixed core/cutoff pressure work.

Therefore, after choosing first `R` large enough for the boundary-sign reduction and then `S\gg R` large enough for pressure-source localization,

\[
\boxed{
\text{positive mean critical dissipation}
\Longrightarrow
\text{positive mean pressure work generated by finitely many log-radius neighbors}
}
\]

up to an arbitrarily small controlled error.

This removes the second branch of the M5-52 dichotomy in the large-cutoff critical-tail regime.

---

## 12. Relation to the static `1/r` ancestry

If the leading tail is exactly of the form

\[
U_{tail}(y)
=
|y|^{-1}\Phi(\theta,\log|y|)
\]

with no normalized-time dependence, then `B_R^{drift}` is itself time independent to leading order.

Its possible order-one size reflects the logarithmic cubic content of the static similarity tail.

But its sign remains nonpositive for the monotone cutoff.

Hence the static tail cannot act as the missing positive source in the `p=3` mean ledger.

This is consistent with the earlier DSD warning that similarity-coordinate shell motion must not be interpreted as ordinary physical outward/inward material transport.

---

## 13. DSD audit

### GREEN — exact under the stated cutoff/tail hypotheses

- `B_R^{drift}\le0` for a monotone radial cutoff;
- `B_R^{adv}=O(R^-2)`;
- `B_R^{press}=O(R^-2)`;
- `B_R^{visc}=O(R^-2)`;
- hence the full cutoff boundary cannot provide a positive order-one large-`R` mean;
- positive-density local `D3` dissipation forces positive mean pressure work.

### YELLOW — surviving pressure branch

The proof search is now concentrated on the finite-neighbor pressure work

\[
\mathcal P_R
=
\int\chi_RP\,U\cdot\nabla|U|dy.
\]

The next task is to derive a sharp upper/lower structural inequality for this term using the pressure-Poisson relation and the weak-critical W1 bounds.

### RED — branch closed

At large cutoff radius, the critical similarity-shell boundary cannot be invoked as an independent positive source that sustains the recurrent pump mean.

---

## 14. New proof gate

After M5-53, the normalized mean-balance gate is

\[
\boxed{
\nu\overline{\mathcal D_3^{pump}}
\lesssim
\overline{\mathcal P^{near}}
}
\]

with remote pressure sources and positive boundary support both removed to arbitrarily small errors.

The next narrow calculation is therefore the **weighted pressure payer**:

\[
\int |U||P|^2,
\]

because Cauchy--Schwarz couples it directly to

\[
\mathcal P_R
\]

and the positive `D3` dissipation.

That weighted pressure quantity is the natural bridge between the M5-37 pressure-tail gap and the M5-50/M5-53 mean cubic ledger.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
