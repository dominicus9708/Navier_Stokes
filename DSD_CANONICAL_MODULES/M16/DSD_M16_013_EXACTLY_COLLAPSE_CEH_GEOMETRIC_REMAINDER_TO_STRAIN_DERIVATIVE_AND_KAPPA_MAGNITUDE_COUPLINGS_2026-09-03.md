# DSD M16-013 — Exact collapse of the CE-H geometric remainder

Date: 2026-09-03
Canonical ID: **M16-013**
Legacy ID: none — first calculation born directly in the canonical numbering.

Status: **INTERNAL CONSTITUTIVE SIMPLIFICATION / THE EXPLICIT GEOMETRIC REMAINDER OF M16-006 (Legacy M5-682) IS NOT AN INDEPENDENT THREE-TERM PAYER AFTER THE EXPONENTIAL-KAPPA WEIGHT USED IN M16-012; INTEGRATION BY PARTS AND `div Sigma = -(1/2) curl W` CANCEL THE CURL-W / AMPLITUDE-GRADIENT TERM EXACTLY / THE INTERIOR REMAINDER REDUCES TO A STRAIN CONTRACTION WITH THE FULL VORTICITY-DERIVATIVE GRAM MATRIX PLUS A KAPPA-GRADIENT–MAGNITUDE-GRADIENT CROSS TERM / THE ONLY EXTRA PIECE IS SUPPORTED IN THE AMPLITUDE CUTOFF TRANSITION AND THEREFORE BELONGS TO THE ALREADY SEPARATE THRESHOLD-TRANSITION PAYER / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M16-006 and M16-012

On the retained CE-H active region write

\[
W=\rho\xi,
\qquad |\xi|=1,
\]

and

\[
\Sigma W=\sigma W,
\qquad
\Delta W=\kappa W.
\]

M16-006 (Legacy M5-682) gives

\[
\boxed{
\mathcal R_{\rm geom}
=-\frac{2}{\rho}\Sigma:\nabla^2\rho
+2\Sigma_{ij}\partial_i\xi\cdot\partial_j\xi
+(\nabla\times W)\cdot\nabla\log\rho.
}
\]

M16-012 uses the exponential-kappa weight. Put

\[
\boxed{
w(y):=e^{2\kappa(y)}\chi(\rho(y)),
}
\]

where the fixed smooth cutoff `chi` is supported away from `rho=0`.

Because the compact hard hull has uniform far-field decay, the support of `chi(rho)` lies inside one fixed spatial core. Thus all integrations by parts below have no boundary contribution at infinity.

---

## 2. Multiply the remainder by the spatial enstrophy weight

The weighted geometric contribution is

\[
\mathfrak R
:=
\int_{\mathbb R^3}
w\rho^2\mathcal R_{\rm geom}\,dy.
\]

Expanding,

\[
\begin{aligned}
\mathfrak R
={}&
-2\int w\rho\,\Sigma_{ij}\partial_{ij}\rho\,dy\\
&+2\int w\rho^2\Sigma_{ij}\partial_i\xi\cdot\partial_j\xi\,dy\\
&+\int w\rho(\nabla\times W)\cdot\nabla\rho\,dy.
\end{aligned}
\]

---

## 3. Divergence of the strain

For incompressible `U`,

\[
\Sigma_{ij}
=\frac12(\partial_iU_j+\partial_jU_i).
\]

Hence

\[
\partial_i\Sigma_{ij}
=\frac12\Delta U_j.
\]

Since

\[
\nabla\times W
=\nabla\times(\nabla\times U)
=-\Delta U
\]

for `div U=0`,

\[
\boxed{
\partial_i\Sigma_{ij}
=-\frac12(\nabla\times W)_j.
}
\]

---

## 4. Integrate the amplitude-Hessian term by parts

Let

\[
I_H
:=-2\int w\rho\Sigma_{ij}\partial_{ij}\rho\,dy.
\]

Integrating in `i`,

\[
\begin{aligned}
I_H
={}&
2\int w\Sigma_{ij}\partial_i\rho\partial_j\rho\,dy\\
&+2\int \rho\Sigma_{ij}(\partial_iw)\partial_j\rho\,dy\\
&+2\int w\rho(\partial_i\Sigma_{ij})\partial_j\rho\,dy.
\end{aligned}
\]

Use the previous identity:

\[
2\int w\rho(\partial_i\Sigma_{ij})\partial_j\rho
=-\int w\rho(\nabla\times W)\cdot\nabla\rho.
\]

This cancels **exactly** the explicit curl-W term in `mathfrak R`.

Therefore

\[
\boxed{
\begin{aligned}
\mathfrak R
={}&
2\int w\Sigma_{ij}
\left(
\partial_i\rho\partial_j\rho
+\rho^2\partial_i\xi\cdot\partial_j\xi
\right)dy\\
&+2\int \rho\,\Sigma\nabla w\cdot\nabla\rho\,dy.
\end{aligned}
}
\]

---

## 5. Full vorticity-derivative Gram tensor

For `W=rho xi`,

\[
\partial_iW\cdot\partial_jW
=
\partial_i\rho\partial_j\rho
+\rho^2\partial_i\xi\cdot\partial_j\xi.
\]

Define

\[
\boxed{
\mathsf G_W{}_{ij}
:=\partial_iW\cdot\partial_jW.
}
\]

It is a positive-semidefinite `3 x 3` Gram tensor.

Thus the first term becomes simply

\[
\boxed{
2\int w\,\Sigma:\mathsf G_W\,dy.
}
\]

---

## 6. Differentiate the exponential-kappa cutoff weight

Since

\[
w=e^{2\kappa}\chi(\rho),
\]

\[
\boxed{
\nabla w
=e^{2\kappa}
\left(
2\chi\nabla\kappa
+\chi'\nabla\rho
\right).
}
\]

Hence

\[
\begin{aligned}
2\int \rho\Sigma\nabla w\cdot\nabla\rho
={}&
4\int e^{2\kappa}\chi\rho\,
\Sigma\nabla\kappa\cdot\nabla\rho\,dy\\
&+2\int e^{2\kappa}\chi'\rho\,
\Sigma\nabla\rho\cdot\nabla\rho\,dy.
\end{aligned}
\]

Therefore the exact weighted remainder is

\[
\boxed{
\begin{aligned}
\mathfrak R
={}&
2\int e^{2\kappa}\chi\,\Sigma:\mathsf G_W\,dy\\
&+4\int e^{2\kappa}\chi\rho\,
\Sigma\nabla\kappa\cdot\nabla\rho\,dy\\
&+2\int e^{2\kappa}\chi'\rho\,
\Sigma\nabla\rho\cdot\nabla\rho\,dy.
\end{aligned}
}
\]

---

## 7. Interior vs cutoff-transition split

Define

\[
\boxed{
\mathfrak T_{\Sigma W}
:=
\int e^{2\kappa}\chi\,\Sigma:\mathsf G_W\,dy,
}
\]

and

\[
\boxed{
\mathfrak X_{\kappa\rho}
:=
\int e^{2\kappa}\chi\rho\,
\Sigma\nabla\kappa\cdot\nabla\rho\,dy.
}
\]

The last term is supported where `chi' != 0`, i.e. in the fixed amplitude transition layer. Put it into the already existing threshold/cutoff payer class:

\[
\boxed{
\mathfrak C_{\rm geom}^{\chi}
:=
2\int e^{2\kappa}\chi'\rho\,
\Sigma\nabla\rho\cdot\nabla\rho\,dy.
}
\]

Then

\[
\boxed{
\mathfrak R
=2\mathfrak T_{\Sigma W}
+4\mathfrak X_{\kappa\rho}
+\mathfrak C_{\rm geom}^{\chi}.
}
\]

Thus the old `explicit geometric remainder` is not an independent uncontrolled object.

---

## 8. Quantitative bound for the cross term

On the compact active core let

\[
\|\Sigma\|_\infty\le S_*.
\]

Define

\[
D_\kappa
:=
\int e^{2\kappa}\chi\rho^2|\nabla\kappa|^2dy,
\]

and

\[
M_\rho
:=
\int e^{2\kappa}\chi|\nabla\rho|^2dy.
\]

Then Cauchy--Schwarz gives

\[
\boxed{
|\mathfrak X_{\kappa\rho}|
\le
S_*D_\kappa^{1/2}M_\rho^{1/2}.
}
\]

M16-011 gives a positive lower bound for `D_kappa`, while compact all-order bounds also give a finite upper bound.

Hence if the cross term pays a fixed amount, it forces a fixed magnitude-gradient charge `M_rho`.

---

## 9. Audit consequence

M16-012 listed the explicit CE-H geometry as one possible payer of the mandatory positive kappa-gradient charge.

M16-013 removes that as an opaque independent branch:

\[
\boxed{
\text{explicit geometry payer}
\Longrightarrow
\text{strain--derivative Gram payer}
\lor
\text{kappa/magnitude-gradient payer}
\lor
\text{amplitude-transition payer}.
}
\]

The second branch quantitatively forces magnitude-gradient activity; the third already belongs to the M14/M15 sheath-turnover family.

The only genuinely new interior object left here is the signed strain contraction

\[
\boxed{
\mathfrak T_{\Sigma W}
=
\int e^{2\kappa}\chi\,\Sigma:\mathsf G_W.
}
\]

---

## 10. Canonical frontier

Combining M16-012 and M16-013, the final PDE payer family can be rewritten without an opaque geometric remainder as:

\[
\boxed{
\begin{array}{l}
D_\sigma\text{ — aligned-strain gradient},\\
\mathcal S\text{ — aligned-strain residence},\\
\mathcal C\text{ — amplitude transition/sheath turnover},\\
\mathfrak T_{\Sigma W}\text{ — strain/derivative-Gram contraction},\\
M_\rho\text{ — magnitude-gradient activity}.
\end{array}
}
\]

The next step is to make this quantitative and show that a fixed M16-012 payer floor forces one of these five canonical local charges to have a uniform positive lower bound.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
