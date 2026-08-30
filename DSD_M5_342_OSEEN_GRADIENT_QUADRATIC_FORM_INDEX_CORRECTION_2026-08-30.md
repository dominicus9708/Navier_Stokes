# DSD M5-342 — Oseen-Gradient Quadratic Form / Index Correction

Date: 2026-08-30

Status: **IMPORTANT INDEX CORRECTION / THE PSD TENSOR CONTRACTED WITH PARENT STRAIN IN HUANG OSEEN PRODUCTION IS `G^T G`, NOT `G G^T` / ALL NORM AND SPECTRAL-SIGN ESTIMATES SURVIVE, BUT THE AXIS INTERPRETATION IS THE SPATIAL-DERIVATIVE RIGHT-SINGULAR DIRECTION / GLOBAL REGULARITY UNPROVED.**

## 1. Exact production term

Let

\[
G_{ik}=\partial_kH_i.
\]

The Oseen H1 production is

\[
\mathcal P
=-\int
\partial_\ell u_k\,
\partial_kH_i\,
\partial_\ell H_i\,dx.
\]

Define the parent velocity gradient

\[
A^u_{k\ell}=\partial_\ell u_k.
\]

Then the quadratic Oseen tensor carrying the derivative indices is

\[
\boxed{
C_H:=G^TG,
\qquad
(C_H)_{k\ell}=\sum_iG_{ik}G_{i\ell}.
}
\]

Therefore

\[
\boxed{
\mathcal P=-\int A^u:C_H\,dx.
}
\]

Since `C_H` is symmetric,

\[
A^u:C_H=S:C_H.
\]

Hence

\[
\boxed{
\mathcal P=-\int S:C_H\,dx.
}
\]

## 2. What was wrong in the previous axis notation

Several preceding atom notes denoted the PSD tensor schematically by

\[
A_H=GG^T.
\]

For scalar norm estimates this caused no numerical error because `GG^T` and `G^TG` have the same nonzero singular-value spectrum and

\[
\operatorname{tr}(GG^T)=\operatorname{tr}(G^TG)=|G|^2.
\]

However the **orientation** relative to the parent strain eigenvectors is different.

The correct compressive occupancy is

\[
\boxed{
\alpha_H
:=
\frac{e_3^TC_He_3}{\operatorname{tr}C_H}
=
\frac{|Ge_3|^2}{|G|^2}.
}
\]

Thus `e_3` is a **spatial derivative direction** of the Oseen field, not an Oseen component/output direction.

## 3. Spectral compression estimate survives

Write

\[
S=S_+-S_-.
\]

Since `C_H>=0`,

\[
-S:C_H
=S_-:C_H-S_+:C_H
\le S_-:C_H.
\]

Therefore all previous estimates of the form

\[
(\mathcal P)_+
\le
\|S_-\|_3\,\|G\|_6\,\|G\|_2
\]

remain valid.

Consequently the atom implication

\[
\boxed{
\int^{T_*}\|S_-(t)\|_3^2dt=\infty
}
\]

is unchanged.

## 4. Same-sector axis correction

In the two-positive/one-negative sector, positive Oseen production requires the **spatial derivative energy** of `H` to place sufficient mass in the compressive parent-strain direction `e_3`:

\[
\boxed{
|Ge_3|^2/|G|^2\ge c>0
}
\]

on an efficient production cell.

The physical vorticity condition remains a statement about the vector direction `xi` in the parent strain eigenframe.

Thus the corrected dual-axis descriptor is

\[
\boxed{
(\xi,\ e_3,\ Ge_3),
}
\]

not a comparison of `xi` with a left singular vector of `G`.

## 5. Audit impact

- M5-333 compressive spectral action: **unchanged**.
- M5-334 determinant/sign fork: **unchanged**.
- M5-338 joint-action target: **unchanged**.
- M5-341 algebra firewall: the example remains valid after replacing `A_H` by a PSD `C_H=e_3 tensor e_3`; the geometric language must be read as derivative-direction occupancy.

The next calculation must evolve

\[
C_H=G^TG
\]

under the constrained Oseen equation.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
