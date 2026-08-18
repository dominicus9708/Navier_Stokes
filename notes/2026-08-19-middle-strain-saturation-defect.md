# Middle-strain saturation defect and the critical L^(3/2) barrier

Date: 2026-08-19

Status: **DERIVED EXACT ALGEBRAIC DEFECT + CRITICAL INSTANTANEOUS BARRIER / GLOBAL REGULARITY NOT PROVED**.

This note continues the reduced `M` branch of the DSD-assisted Navier--Stokes proof challenge. It does not alter the equation and does not claim a solution of the global regularity problem.

---

## 1. Setup

Let

\[
S=\nabla_{\rm sym}u
\]

be the trace-free strain tensor with ordered eigenvalues

\[
\lambda_1\le \lambda_2\le \lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0.
\]

Write

\[
f=\lambda_2^+=\max\{\lambda_2,0\}.
\]

For smooth decaying incompressible flow on `R^3`, retain

\[
\frac{d}{dt}\|S\|_2^2
=-2\nu\|\nabla S\|_2^2-4\int\det S,
\]

and

\[
\|S\|_2^2=\frac12\|\omega\|_2^2,
\qquad
\|\nabla S\|_2^2=\frac12\|\nabla\omega\|_2^2.
\]

The external middle-eigenvalue regularity criterion remains an anchor; the calculation below is an internal refinement of the algebraic production estimate.

---

## 2. Exact saturation-defect identity

On the set `lambda_2>0`, trace-freeness gives

\[
\lambda_1=-(\lambda_2+\lambda_3),
\]

hence

\[
|S|^2
=2(\lambda_2^2+\lambda_2\lambda_3+\lambda_3^2).
\]

Therefore

\[
\boxed{
-\det S
=\frac12\lambda_2|S|^2-\lambda_2^3
\qquad(\lambda_2>0).
}
\]

If `lambda_2<=0`, then `-det S<=0`. Consequently the following global pointwise one-sided identity/inequality holds:

\[
\boxed{
-\det S
\le
\frac12 f|S|^2-f^3.
}
\]

The previously used estimate

\[
-\det S\le\frac12f|S|^2
\]

therefore loses the exact nonnegative defect

\[
\boxed{f^3=(\lambda_2^+)^3.}
\]

---

## 3. Refined enstrophy ledger

Let

\[
E_\omega=\|\omega\|_2^2,
\qquad
P_\omega=\|\nabla\omega\|_2^2.
\]

Using the exact defect,

\[
\frac12E_\omega'
+\nu P_\omega
\le
2\int f|S|^2
-4\int f^3.
\]

Let `C_S` denote a Sobolev constant in

\[
\|S\|_6^2\le C_S\|\nabla S\|_2^2.
\]

By Holder and Sobolev,

\[
\int f|S|^2
\le
\|f\|_{3/2}\|S\|_6^2
\le
\frac{C_S}{2}\|f\|_{3/2}P_\omega.
\]

Hence

\[
\boxed{
\frac12E_\omega'
+4\|f\|_3^3
\le
\left(C_S\|f\|_{3/2}-\nu\right)P_\omega.
}
\]

This is the main new ledger of this note.

---

## 4. Instantaneous critical barrier

Whenever

\[
E_\omega'(t)>0,
\]

the refined ledger forces

\[
\boxed{
\|\lambda_2^+(t)\|_{L^{3/2}}
>
\frac{\nu}{C_S}.
}
\]

Thus any positive enstrophy-growth episode must cross a fixed scale-critical `L^(3/2)` threshold in the positive middle eigenvalue.

This is an instantaneous smallness barrier, not an endpoint global regularity theorem.

Define the critical excess

\[
\mathfrak E_M(t)
=
C_S\|\lambda_2^+(t)\|_{3/2}-\nu.
\]

Then

\[
\boxed{
\frac12E_\omega'
+4\|\lambda_2^+\|_3^3
\le
\mathfrak E_M P_\omega.
}
\]

Therefore a positive-growth interval must pay through at least one of:

1. a definite critical `L^(3/2)` excess `mathfrak E_M`;
2. large palinstrophy `P_omega`;
3. loss through the cubic saturation defect `||lambda_2^+||_3^3`.

This couples the `M` branch directly to the higher-derivative/palinstrophy `H` branch.

---

## 5. Interval form

For an interval `I=[t_0,t_1]`,

\[
\boxed{
\frac12\bigl(E_\omega(t_1)-E_\omega(t_0)\bigr)
+4\int_I\|\lambda_2^+\|_3^3dt
\le
\int_I\mathfrak E_M P_\omega\,dt.
}
\]

If the enstrophy rises on `I`, then

\[
\boxed{
\sup_I \mathfrak E_M^+
\ge
\frac{
\frac12\Delta E_\omega
+4\int_I\|\lambda_2^+\|_3^3dt
}{
\int_I P_\omega dt
}.
}
\]

Hence repeated `M` pulses with only near-threshold `L^(3/2)` mass require an increasingly expensive derivative budget.

---

## 6. Geometry of near-saturation

Let

\[
A_I=\int_I\!\!\int f|S|^2,
\qquad
Q_I=\int_I\!\!\int f^3.
\]

The determinant production satisfies

\[
-\int_I\!\!\int\det S
\le
\frac12A_I-Q_I.
\]

Thus near-saturation of the old bound requires

\[
\boxed{
Q_I/A_I\to0.
}
\]

Introduce

\[
x=\frac{f}{|S|}
\]

on the productive set, and the production-weighted probability measure

\[
d\mu_I
=\frac{f|S|^2}{A_I}\,dxdt.
\]

Then

\[
\boxed{
\int x^2d\mu_I
=\frac{Q_I}{A_I}.
}
\]

Therefore for every `kappa>0`,

\[
\boxed{
\mu_I\{x\ge\kappa\}
\le
\frac{Q_I/A_I}{\kappa^2}.
}
\]

A determinant-production sequence that approaches saturation must therefore concentrate its productive weight in the regime

\[
\boxed{
\lambda_2^+/|S|\to0.
}
\]

Equivalently, the strain spectrum approaches the planar form

\[
\lambda_1\simeq-\lambda_3,
\qquad
\lambda_2\simeq0^+.
\]

---

## 7. Spectral-gap consequence

On `lambda_2>0`, write

\[
x=\lambda_2/|S|.
\]

Trace-freeness and the Frobenius normalization give

\[
\frac{\lambda_3}{|S|}
=
\frac{-x+\sqrt{2-3x^2}}{2}.
\]

Hence

\[
\boxed{
\frac{\lambda_3-\lambda_2}{|S|}
=
\frac{\sqrt{2-3x^2}-3x}{2},
}
\]

and

\[
\boxed{
\frac{\lambda_3-\lambda_1}{|S|}
=
\sqrt{2-3x^2}.
}
\]

For any fixed

\[
0<\kappa<1/\sqrt6,
\]

the region `x<=kappa` therefore has a uniform principal spectral gap

\[
\lambda_3-\lambda_2
\ge
c_\kappa|S|,
\]

where

\[
\boxed{
c_\kappa
=\frac{\sqrt{2-3\kappa^2}-3\kappa}{2}>0.}
\]

Thus `M` saturation does not collapse the principal eigenvalue gap; it opens a quantitative simple-eigenvalue regime for the most extensional axis.

---

## 8. Axis conversion or derivative cost

Let `e_3` be the principal strain eigenvector on the simple-gap set. Standard eigenvector differentiation gives, for each spatial derivative,

\[
e_j\cdot\partial_k e_3
=
\frac{e_j^T(\partial_kS)e_3}{\lambda_3-\lambda_j},
\qquad j=1,2.
\]

Therefore on `x<=kappa`,

\[
\boxed{
|\nabla S|^2
\ge
c_\kappa^2|S|^2|\nabla e_3|^2.
}
\]

Hence spatial bending of the principal extensional axis has a direct strain-gradient/palinstrophy cost.

Separately, for vorticity direction `xi=omega/|omega|`,

\[
\boxed{
|P_{\xi^\perp}S\xi|^2
=
\sum_{i<j}a_i a_j(\lambda_i-\lambda_j)^2,
\qquad
a_i=(\xi\cdot e_i)^2.
}
\]

On `x<=kappa`,

\[
\boxed{
|P_{\xi^\perp}S\xi|^2
\ge
c_\kappa^2|S|^2a_3(1-a_3).
}
\]

Thus a near-saturated `M` state has the following reduced alternatives:

1. principal-axis conversion is non-small;
2. the principal strain eigenframe bends, paying derivative/palinstrophy cost;
3. vorticity becomes projectively close to the principal extensional axis;
4. the productive set loses spatial tightness/coverage.

The first two are routed toward `H`; the fourth toward transport `T`. The third is the remaining alignment-rigidity subbranch.

---

## 9. Exact vorticity-direction equation

Where `rho=|omega|>0`, write `omega=rho xi`. Then

\[
(\partial_t+u\cdot\nabla-\nu\Delta)\rho
=
rho\left(\gamma-\nu|\nabla\xi|^2\right),
\qquad
\gamma=\xi^TS\xi.
\]

The direction equation is

\[
\boxed{
(\partial_t+u\cdot\nabla)\xi
=
P_{\xi^\perp}S\xi
+\nu P_{\xi^\perp}\Delta\xi
+2\nu\,\nabla\log\rho\cdot\nabla\xi.
}
\]

Therefore exact alignment with `e_3` suppresses the instantaneous strain-driven direction-rotation term, but it does not remove diffusion, direction curvature, magnitude-gradient coupling, eigenframe bending, or the palinstrophy cost of localization.

This is why pointwise alignment by itself does not close the `M` branch.

---

## 10. New reduced `M/H` target

The remaining near-saturation sequence must now sustain simultaneously:

\[
\boxed{
\|\lambda_2^+\|_{3/2}\gtrsim\nu/C_S,
}
\]

\[
\boxed{
\lambda_2^+/|S|\to0
\quad\text{on the determinant-productive measure},
}
\]

while avoiding a non-summable cost in

\[
\boxed{
P_\omega,
\quad
\|\lambda_2^+\|_3^3,
\quad
|S|^2|\nabla e_3|^2,
\quad
|P_{\xi^\perp}S\xi|^2,
}
\]

and also avoiding spatial non-tightness.

This is a stronger critical-saturation formulation than the previous scalar `lambda_2^+` branch, but it is not yet a nonrepeatability theorem.

---

## External anchor

E. Miller, *A Regularity Criterion for the Navier--Stokes Equation Involving Only the Middle Eigenvalue of the Strain Tensor*, Arch. Rational Mech. Anal. 235 (2020), 99--139; arXiv:1710.05569.

Status: **M BRANCH REFINED INTO CRITICAL-L^(3/2) EXCESS / CUBIC DEFECT / PALINSTROPHY / AXIS-RIGIDITY SUBBRANCHES — FINAL GLOBAL CLOSURE OPEN**.
