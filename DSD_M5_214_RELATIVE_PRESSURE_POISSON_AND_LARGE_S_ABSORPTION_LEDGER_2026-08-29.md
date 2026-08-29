# DSD M5-214 — Relative Pressure Poisson Equation and Large-s Absorption Ledger

Date: 2026-08-29

Parent: `DSD_M5_213_SPATIAL_CARLEMAN_GAP_AND_TERMINAL_OSEEN_STOKES_TARGET_2026-08-29.md`

Status: **POSITIVE PRESSURE REDUCTION / ON A FIXED EXTERIOR THE RELATIVE OSEEN PRESSURE SOLVES AN ELLIPTIC POISSON EQUATION WHOSE SOURCE IS LINEAR IN THE FIRST DERIVATIVE `∇Z` WITH BOUNDED COEFFICIENTS; THERE IS NO SECOND-VELOCITY-DERIVATIVE LOSS / IF A TERMINAL PARABOLIC CARLEMAN ESTIMATE FOR `Z` AND A COMPATIBLE LOCAL ELLIPTIC CARLEMAN ESTIMATE FOR `q` USE THE SAME SPATIAL WEIGHT LEVELS, ALL BOUNDED OSEEN AND PRESSURE TERMS ARE ABSORBABLE FOR LARGE CARLEMAN PARAMETER `s` / THE ONLY UNPROVED ITEM IS NOW THE EXISTENCE/COMPATIBILITY OF THAT TERMINAL PARABOLIC–ELLIPTIC CARLEMAN PAIR WITH THE REQUIRED SOURCE GAP / GLOBAL REGULARITY UNPROVED.**

---

## 1. Relative Oseen system

On a fixed exterior terminal cylinder let

\[
Z_t-\nu\Delta Z
+(u^V\cdot\nabla)Z
+(Z\cdot\nabla)u^W
+\nabla q=0,
\]

with

\[
\nabla\cdot Z
=\nabla\cdot u^V
=\nabla\cdot u^W
=0.
\]

All coefficients and their finite derivatives are uniformly bounded on every fixed exterior.

---

## 2. Exact pressure Poisson equation

Take divergence of the relative velocity equation.

The time and Laplacian terms vanish after divergence because `div Z=0`.

For the first convection term,

\[
\begin{aligned}
\partial_i(u^V_j\partial_jZ_i)
&=(\partial_i u^V_j)(\partial_j Z_i)
+u^V_j\partial_j(\partial_iZ_i)\\
&=(\partial_i u^V_j)(\partial_j Z_i).
\end{aligned}
\]

Similarly,

\[
\begin{aligned}
\partial_i(Z_j\partial_j u^W_i)
&=(\partial_iZ_j)(\partial_j u^W_i)
+Z_j\partial_j(\partial_i u^W_i)\\
&=(\partial_iZ_j)(\partial_j u^W_i).
\end{aligned}
\]

Therefore

\[
\boxed{
-\Delta q
=(\partial_i u^V_j)(\partial_j Z_i)
+(\partial_iZ_j)(\partial_j u^W_i).
}
\]

Equivalently,

\[
\boxed{-\Delta q=\mathcal A(x,t):\nabla Z}
\]

for a bounded coefficient tensor `mathcal A` formed from `∇u^V,∇u^W`.

Status: **PROVED exactly.**

---

## 3. No derivative loss in the pressure source

On every fixed exterior,

\[
\|\mathcal A\|_\infty\le C_R.
\]

Hence

\[
\boxed{
\|\Delta q\|_{L^2}
\le
C_R\|\nabla Z\|_{L^2}.
}
\]

Thus an elliptic Carleman estimate applied directly to `q` sees an `L^2` source containing only one spatial derivative of `Z`.

There is no source of the form

\[
\nabla^2Z
\]

and no pressure derivative cascade is required.

This is stronger than the earlier schematic pressure concern.

---

## 4. Schematic compatible Carleman pair

The remaining target can now be written quantitatively.

Assume one has, after localization and with a common weight `Phi`, a terminal parabolic estimate

\[
\boxed{
I_Z(s)
:=
\int e^{2s\Phi}
\bigl(
 s|\nabla Z|^2
+s^3|Z|^2
\bigr)
\le
C\int e^{2s\Phi}|PZ|^2
+E_{in}(s),
}
\]

where

\[
PZ:=Z_t-\nu\Delta Z
\]

and `E_in(s)` denotes cutoff/source terms supported at the lower spatial weight level.

Assume also a local elliptic pressure estimate with the same spatial hierarchy,

\[
\boxed{
I_q(s)
:=
\int e^{2s\Phi}
\bigl(
 s|\nabla q|^2
+s^3|q|^2
\bigr)
\le
C\int e^{2s\Phi}|\Delta q|^2
+E_{q,in}(s).
}
\]

These are schematic normalizations; only the positive powers of `s` and common spatial weight ordering are essential for the absorption ledger below.

---

## 5. Bounded Oseen terms are absorbable

From the PDE,

\[
PZ
=-(u^V\cdot\nabla)Z
-(Z\cdot\nabla)u^W
-\nabla q.
\]

Therefore

\[
\int e^{2s\Phi}|PZ|^2
\le
C_R
\int e^{2s\Phi}
(|\nabla Z|^2+|Z|^2)
+C\int e^{2s\Phi}|\nabla q|^2.
\]

The first two terms are lower by factors

\[
\frac1s,
\qquad
\frac1{s^3}
\]

relative to the corresponding positive pieces in `I_Z`.

Thus they are absorbed for sufficiently large `s`.

---

## 6. Pressure is also absorbable through its Poisson equation

Section 2 gives

\[
|\Delta q|^2
\le
C_R|\nabla Z|^2.
\]

Therefore the elliptic estimate gives

\[
I_q(s)
\le
C_R
\int e^{2s\Phi}|\nabla Z|^2
+E_{q,in}(s).
\]

In particular,

\[
\boxed{
\int e^{2s\Phi}|\nabla q|^2
\le
\frac{C_R}{s}
\int e^{2s\Phi}|\nabla Z|^2
+\frac1sE_{q,in}(s).
}
\]

Inserted into the parabolic estimate, the pressure contribution is smaller than the principal gradient coercivity by another factor of order `1/s`.

Thus, at the formal Carleman-inequality level,

\[
\boxed{
\text{pressure does not prevent large-s absorption.}
}
\]

---

## 7. Result after absorption

For sufficiently large `s`, the combined ledger would reduce to

\[
\boxed{
I_Z(s)+cI_q(s)
\le
C\bigl(E_{in}(s)+E_{q,in}(s)\bigr).
}
\]

If the source/cutoff regions satisfy the M5-213 spatial gap

\[
\sup_{source}\Phi
<
\inf_{target}\Phi,
\]

then

\[
I_Z(s;target)
\le
C e^{-2s\delta_\Phi}
\mathcal E_{source}.
\]

Sending

\[
s\to\infty
\]

would give

\[
\boxed{Z=0}
\]

on the target backward cylinder.

This would close the same-tail flat fiber once ordinary smooth-time spatial analyticity/unique continuation is applied.

---

## 8. What has and has not been proved

### Proved

- the exact pressure Poisson equation;
- first-derivative-only pressure source;
- boundedness of the source coefficient on fixed exterior;
- the algebraic large-`s` absorption once the two displayed compatible Carleman estimates are granted.

### Not proved

- the required terminal-time parabolic Carleman estimate for the localized velocity in the Oseen–Stokes setting;
- the compatible elliptic pressure Carleman estimate using precisely the same spacetime/spatial weight hierarchy;
- the full cutoff bookkeeping proving all remaining terms lie strictly below the target weight level.

Thus no new theorem is silently assumed.

---

## 9. Updated frontier

The former large statement

\[
\text{`prove pressure-compatible exterior backward uniqueness'}
\]

has now been sharpened to one concrete compatibility question:

\[
\boxed{
\begin{array}{c}
\text{Can the standard terminal parabolic BU weight be paired with}\
\text{a local elliptic pressure Carleman weight so that}\
\text{(i) both use the same spatial level gap and}\
\text{(ii) the pressure estimate gains enough }s\text{ to absorb }\nabla q?
\end{array}
}
\]

All coefficient-size and derivative-count issues on the fixed exterior are already favorable.

---

## 10. DSD audit

### Formation — GREEN

The pressure equation is directly derived from the actual relative system.

### Axis — GREEN

Parabolic velocity coercivity and elliptic pressure coercivity are separated before combination.

### Static aggregation — GREEN

A schematic compatible pair is not counted as an established theorem.

### Dynamics — YELLOW, one explicit estimate pair

Only the terminal parabolic–elliptic Carleman compatibility remains.

### Cross-audit — GREEN

The route is consistent with Boulakia-style pressure handling and avoids the whole-space Hardy-critical tail amplitude entirely.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]