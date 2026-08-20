# Tightness/Analyticity Parameter Reduction — 2026-08-20

Overall status: **PARAMETER REDUCTION FOR THE RECURRENT P_V CLASS — GLOBAL REGULARITY NOT PROVED.**

This note reduces two class parameters used in the high-strain selection lemma to geometric tightness and first-hitting analytic regularity data.

---

## 1. Enstrophy tightness bounds strain L2 mass

At first-hitting normalization,

\[
\|\Omega\|_\infty\le1.
\]

Let

\[
Z=\|\Omega\|_2^2,
\qquad
E=\|S\|_2^2=\frac12Z.
\]

Suppose a non-T compact class is enstrophy-tight in radius `R_Z` in the quantitative sense

\[
\int_{B_{R_Z}}|\Omega|^2dx
\ge
(1-\varepsilon_Z)Z,
\qquad
0\le\varepsilon_Z<1.
\]

Since `|Omega| <= 1`,

\[
(1-\varepsilon_Z)Z
\le
|B_{R_Z}|
=\frac{4\pi}{3}R_Z^3.
\]

Therefore

\[
\boxed{
Z
\le
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}
}
\]

and

\[
\boxed{
E
\le
E_+
:=
\frac{2\pi R_Z^3}{3(1-\varepsilon_Z)}.
}
\]

Thus the strain `L2` bound is not an independent compact-class parameter.

---

## 2. Insert the analytic strain-gradient bound

Let

\[
L_+
\ge
\|\nabla S\|_\infty
\]

be the normalized strain Lipschitz bound on the fixed parent ball supplied by first-hitting analyticity plus the local elliptic strain-vorticity relation.

The high-strain selection lemma uses

\[
B_*
=
\left(
\frac{24}{\pi}E_+L_+^3
\right)^{1/5}.
\]

Insert the tightness bound for `E_+`:

\[
B_*
\le
\left[
\frac{16R_Z^3L_+^3}{1-\varepsilon_Z}
\right]^{1/5}.
\]

Hence

\[
\boxed{
B_*
\le
2^{4/5}
(R_ZL_+)^{3/5}
(1-\varepsilon_Z)^{-1/5}.
}
\]

Thus the class strain-amplitude ceiling is reduced to the dimensionless product `R_Z L_+` and the enstrophy-tail fraction.

---

## 3. Uniform production-amplitude ratio

At a Leray recovery checkpoint define

\[
q_-\le N/P.
\]

With

\[
C_H=\frac4{\sqrt6},
\]

the high-strain selection parameter satisfies

\[
\beta_K
\ge
\frac{q_-}{C_HB_*}.
\]

Therefore

\[
\boxed{
\beta_K
\ge
\frac{q_-(1-\varepsilon_Z)^{1/5}}
{C_H2^{4/5}(R_ZL_+)^{3/5}}.
}
\]

If the right side exceeds one, the recurrence is already inconsistent with the sharp static H1 production bound.

Otherwise the selected high-strain ball carries at least

\[
\boxed{
\alpha_K
\ge
\frac{9\beta_K^6}{1024(2-\beta_K)}
}
\]

of the whole strain-gradient energy.

---

## 4. What remains in the general local branch

For the non-global-moment/local ancient branch, the remaining quantitative inputs are now

\[
R_Z,
\qquad
\varepsilon_Z,
\qquad
L_+,
\qquad
q_-,
\qquad
e_T<1/6.
\]

The first two are tightness parameters, the third is an analytic/elliptic derivative parameter, the fourth is supplied by the Leray recurrence ledger once `kappa^+` is bounded, and the fifth is the explicit non-turnover annular leakage threshold.

---

## 5. First-hitting analyticity interpretation of L_+

The existing first-hitting analyticity bridge gives a normalized analytic strip

\[
\rho_{an}\ge\rho_0>0
\]

and bounded analytic vorticity amplitude on every fixed parent ball. Cauchy estimates bound `grad Omega`, and local elliptic estimates for

\[
-\Delta U=\nabla\times\Omega,
\qquad
S=\operatorname{sym}\nabla U
\]

then give

\[
\boxed{
L_+
\le
\mathcal L(\rho_0,M_0,A_*,R_{parent})<\infty,
}
\]

where `A_*` is the local Type-I parent-ball velocity-energy bound.

The exact numerical evaluation of `mathcal L` depends on the analyticity and interior elliptic constants. The structural dependence is now isolated; no new Navier--Stokes mechanism is hidden inside `B_*`.

---

Status: **THE STRAIN L2 MASS AND AMPLITUDE CEILING OF THE COMPACT FIRST-HITTING CLASS ARE REDUCED TO ENSTROPHY TIGHTNESS AND ANALYTIC DERIVATIVE CONTROL. THE HIGH-STRAIN DERIVATIVE-ENERGY OCCUPANCY CAN THEREFORE BE WRITTEN IN TERMS OF A SMALL FINITE SET OF NORMALIZED GEOMETRIC PARAMETERS.**