# Gaussian affine-mean decay on the mesoscopic parent ladder

Date: 2026-08-13

Status: **DERIVED FINITE-KINETIC-ENERGY AFFINE-MEAN DECAY / NON-AFFINE OUTER LADDER REMAINS OPEN**.

This note controls the self-consistent Gaussian affine representative at large normalized parent scales using only finite kinetic energy.

---

## 1. Gaussian affine representative

At a fixed time, let `gamma_R` be a centered Gaussian probability density with spatial width comparable to `R`, and define

\[
L_R=\int_{\mathbb R^3}\gamma_R(y)\nabla U(y)\,dy.
\]

For the self-consistent Gaussian construction this is the resolved affine gradient at that observation scale.

Integration by parts gives

\[
\boxed{
L_R=-\int U(y)\otimes\nabla\gamma_R(y)\,dy.
}
\]

Therefore

\[
\boxed{
|L_R|_F
\le
\|U\|_2\,\|\nabla\gamma_R\|_2.
}
\]

---

## 2. Gaussian scaling

For an isotropic Gaussian of width `R`,

\[
\gamma_R(y)=R^{-3}\gamma_1(y/R).
\]

Hence

\[
\nabla\gamma_R(y)=R^{-4}(\nabla\gamma_1)(y/R)
\]

and

\[
\boxed{
\|\nabla\gamma_R\|_2
=R^{-5/2}\|\nabla\gamma_1\|_2.
}
\]

For a uniformly conditioned anisotropic Gaussian the same law holds up to a constant depending only on the covariance condition number.

Thus

\[
\boxed{
|L_R|_F
\lesssim_K
R^{-5/2}\|U\|_2.
}
\]

---

## 3. First-hitting normalization

At terminal first-hitting vorticity level

\[
W=\|\omega(T)\|_\infty,
\qquad
r=W^{-1/2},
\]

use

\[
U(y,s)=r\,u(x_*+ry,T+r^2s).
\]

Then

\[
\boxed{
\|U(s)\|_2
=r^{-1/2}\|u(t)\|_2
=W^{1/4}\|u(t)\|_2.
}
\]

The kinetic-energy inequality gives

\[
\|u(t)\|_2\le\|u_0\|_2.
\]

Therefore

\[
\boxed{
|L_R(s)|_F
\lesssim_K
\|u_0\|_2\,W^{1/4}R^{-5/2}.
}
\]

---

## 4. Mesoscopic affine cutoff exponent

Let

\[
R(W)=W^\theta.
\]

Then

\[
|L_{R(W)}|
\lesssim_K
\|u_0\|_2
W^{1/4-(5/2)\theta}.
\]

Hence

\[
\boxed{
\theta>\frac1{10}
\Longrightarrow
|L_{W^\theta}|\to0
\quad(W\to\infty).
}
\]

The corresponding physical radius is

\[
rR(W)=W^{-1/2+\theta},
\]

which still tends to zero for every `theta<1/2`.

Thus there is a nonempty mesoscopic range

\[
\boxed{
W^{1/10+\varepsilon}
\lesssim R
\ll W^{1/2}
}
\]

on which the optimal Gaussian affine mean becomes asymptotically negligible while the physical observation radius still collapses to the candidate singular point.

---

## 5. Combine with the pressure-Hessian far-tail exponent

The kinetic-energy pressure-Hessian tail audit gives, for normalized radius `R=W^theta`,

\[
\operatorname{osc}_{B_1}\nabla_y^2P_{\rm far}
\to0
\qquad\text{whenever}\qquad
\theta>\frac1{12}.
\]

Since

\[
\frac1{10}>\frac1{12},
\]

choosing

\[
\theta>\frac1{10}
\]

simultaneously gives

\[
\boxed{
\text{small coherent Gaussian affine mean}
+\text{small far pressure-Hessian variation}.
}
\]

Therefore the outer mesoscopic ladder cannot be sustained primarily by either of these coherent/background mechanisms.

---

## 6. Consequence for the ancient critical-mass branch

The Albritton--Barker bridge shows that a nontrivial ancient route avoiding backward `L^3` tightness must transport critical velocity mass through normalized spatial infinity.

On parent scales

\[
R\gg W^{1/10},
\]

coherent affine transport is asymptotically negligible and pressure-Hessian variation from still farther scales is negligible.  Therefore any inward critical-mass transfer across this outer mesoscopic range must be typed primarily as

\[
\boxed{
\text{non-affine shell transport / residual transport}.
}
\]

This does not yet prove that such transport is impossible.  The remaining problem is to establish a scale-ratio or packing bound for that non-affine transport.

---

## 7. DSD interpretation

The parent-scale search now has a quantitative stopping rule.

The affine representative is retained only while its resolved coefficient is above the kinetic-energy resolution floor.  Once

\[
R\gg W^{1/10},
\]

the affine channel becomes asymptotically undescribable at order one and the unresolved state is forced into the residual/shell channels.

Thus the outer parent ladder is not another independent affine branch; it is a non-affine transport branch.

Status: **AFFINE OUTER-LADDER BRANCH PRUNED ABOVE THE `W^(1/10)` SCALE / NON-AFFINE SHELL PACKING REMAINS OPEN**.
