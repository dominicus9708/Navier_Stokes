# Critical R^-2 residual-seed pinning

Date: 2026-08-16

Status: **DERIVED SHAPE-INDEPENDENT PINNING OF THE MINIMAL RESIDUAL-SEED SCALE. RESIDUAL ACTION ABOVE `R^(-2+epsilon)` RETURNS TO A SUPERCRITICAL/THIN-DERIVATIVE PULSE; RESIDUAL ACTION BELOW `R^(-2-epsilon)` FORCES EITHER GAUSSIAN SPATIAL ESCAPE OR POLYNOMIAL AFFINE STRAIN-ENERGY. ONLY AN `R^(-2+o(1))` BAND REMAINS SCALAR-CRITICAL. GLOBAL REGULARITY NOT PROVED.**

## 1. Recent coherent source interval

Work on the critical recent interval `I=[t0,T]` in terminal-normalized variables, with

\[
|I|\asymp R^2
\]

on the minimal parabolic branch.

Let

\[
\mathcal B_R
:=\int_I B_\gamma(s)ds,
\]

where `B_gamma` is the self-consistent Gaussian non-affinity variance.

The terminal mean vorticity is order one while the old/homogeneous contribution at `t0` is negligible.

The exact mean equation is

\[
\bar\Omega(T)
=F(T,t_0)\bar\Omega(t_0)
+\int_{t_0}^{T}F(T,s)J(s)ds,
\]

with

\[
|J(s)|\le C B_\gamma(s).
\]

## 2. Active source times carry large actual transition stretch

Let

\[
\mathcal J:=\int_I|J(s)|ds
\le C\mathcal B_R.
\]

As established in the exact small-seed transition lemma, a fixed fraction of the endpoint Duhamel contribution is carried by the set

\[
A_>
=\left\{
 s:\|F(T,s)\|\ge c\mathcal J^{-1}
\right\}.
\]

Therefore there exists an active source time `s_*` such that

\[
\boxed{
q_*:=\|F(T,s_*)\|
\gtrsim\mathcal B_R^{-1}.
}
\]

This is an actual matrix-transition stretch, not only an integrated strain norm.

## 3. Shape-independent affine deformation--diffusion product

Let

\[
\mathcal J_S(s_*,T)
:=\int_{s_*}^{T}
\|\operatorname{sym}L(\tau)\|_{op}^2d\tau.
\]

Let

\[
C(T,s_*)
=\int_{s_*}^{T}
F(\tau,s_*)^{-1}F(\tau,s_*)^{-T}d\tau
\]

and

\[
\Sigma(s_*)=2\nu C(T,s_*).
\]

The rotation-independent affine deformation--diffusion estimate gives, if `mu1<=mu2<=mu3` are the eigenvalues of `C`,

\[
\boxed{
\sqrt{\mu_2\mu_3}
\ge
\frac{(1-q_*^{-1})^2}{\mathcal J_S(s_*,T)}q_*.
}
\]

Because

\[
\mu_3\ge\sqrt{\mu_2\mu_3},
\]

we obtain for sufficiently large `q_*`

\[
\boxed{
\lambda_{\max}(\Sigma(s_*))
\,\mathcal J_S(s_*,T)
\gtrsim
\nu q_*.
}
\]

This statement is independent of whether the transition is uniaxial-like, balanced, or biaxial. The singular-value geometry affects how the covariance is distributed, but not this largest-covariance product lower bound.

Combining with the source stretch,

\[
\boxed{
\lambda_{\max}(\Sigma(s_*))
\,\mathcal J_S(s_*,T)
\gtrsim
\frac{\nu}{\mathcal B_R}.
}
\]

## 4. Core-scale covariance branch

Suppose the affine Gaussian remains spatially tied to the coherent core scale on the recent interval:

\[
\boxed{
\lambda_{\max}(\Sigma(s))
\le C_\Sigma R^2
\qquad(s\in I).
}
\]

Then the previous product implies

\[
\boxed{
\mathcal J_S(I)
\ge
\mathcal J_S(s_*,T)
\gtrsim
\frac{\nu}{R^2\mathcal B_R}.
}
\]

Hence for every fixed `epsilon>0`,

\[
\boxed{
\mathcal B_R\le R^{-2-\varepsilon}
\Longrightarrow
\mathcal J_S(I)
\gtrsim
\nu R^\varepsilon.
}
\]

Thus a very-small residual seed cannot coexist with both core-scale Gaussian covariance and merely logarithmic/minimal affine strain. It forces polynomial affine strain-energy.

## 5. Gaussian spatial-escape alternative

If the conclusion of Section 4 is avoided, then at the active source time

\[
\boxed{
\lambda_{\max}(\Sigma(s_*))\gg R^2.
}
\]

The affine heat kernel itself then occupies a spatial scale asymptotically larger than the coherent core.

This is a Gaussian spatial non-tightness / affine-deformation escape, already routed elsewhere to material transport, derivative, or scale-escape channels.

Therefore

\[
\boxed{
\mathcal B_R\le R^{-2-\varepsilon}
\Longrightarrow
\begin{cases}
\mathcal J_S\gtrsim\nu R^\varepsilon,\\
\text{or Gaussian spatial escape.}
\end{cases}
}
\]

The reverse-Girsanov result adds that on the first branch the nonlinear diffusion law is also close to its affine Gaussian reference whenever the same covariance ceiling holds.

## 6. Large residual-seed side

Suppose instead

\[
\boxed{
\mathcal B_R\ge R^{-2+\varepsilon}.
}
\]

Since the recent horizon has length comparable to `R^2`, if a fixed fraction of this action lies in the parabolic bulk, then for some bulk time

\[
B_\gamma
\gtrsim
R^{-4+\varepsilon}.
\]

Hence the Gaussian local Reynolds number satisfies

\[
\boxed{
\mathcal R_G
=R^2\sqrt{B_\gamma}
\gtrsim
R^{\varepsilon/2}\to\infty.
}
\]

Continuity toward the terminal subcritical endpoint forces another Reynolds-one crossing.

If the action does not occupy the parabolic bulk, it is concentrated into a thinner terminal layer. Gaussian Poincare plus the residual-variance dynamics route this to V2/high-curvature or global enstrophy concentration. The pressure-Hessian part has already been absorbed into the kernel-weighted enstrophy action.

Thus

\[
\boxed{
\mathcal B_R\ge R^{-2+\varepsilon}
\Longrightarrow
\text{supercritical residual crossing}
\quad\lor\quad
\text{thin derivative/enstrophy pulse}.
}
\]

## 7. Critical pinning

Combining Sections 4--6, a survivor which avoids

- supercritical residual recursion,
- thin derivative/enstrophy concentration,
- Gaussian spatial escape,
- and polynomial affine strain-energy

must satisfy, for every fixed `epsilon>0` along the selected subsequence,

\[
\boxed{
R^{-2-\varepsilon}
\lesssim
\mathcal B_R
\lesssim
R^{-2+\varepsilon}.
}
\]

Equivalently,

\[
\boxed{
\mathcal B_R=R^{-2+o(1)}.
}
\]

Thus the exponent `2` is not merely a convenient threshold. It is the unique scalar-critical residual-action scale left by the present source--deformation--diffusion ledger.

## 8. Interpretation at critical saturation

At

\[
\mathcal B_R\asymp R^{-2},
\]

the source-transition lemma gives

\[
q_*\gtrsim R^2.
\]

The deformation--diffusion product becomes

\[
\lambda_{\max}(\Sigma)\mathcal J_S
\gtrsim\nu R^2.
\]

Thus the minimally escaping episode sits exactly at a three-way balance:

\[
\boxed{
\text{residual seed }R^{-2}
\times
\text{actual deformation }R^2
\sim1,
}
\]

with the affine strain-energy and Gaussian diffusion covariance sharing the remaining burden.

This is a genuine critical saturation, not an artifact of temporal overlap.

## 9. Global scale packing consequence

On the polynomial-strain branch, Gaussian mean-strain Bessel packing gives for a geometrically separated physical-scale subsequence

\[
\sum_j
\ell_j^3 W_j\mathcal J_{S,j}
<\infty.
\]

Since

\[
\ell_j^3W_j
=\frac{R_j^3}{\sqrt{W_j}},
\]

the very-small-seed branch with

\[
\mathcal J_{S,j}\gtrsim R_j^\varepsilon
\]

requires

\[
\boxed{
\sum_j
\frac{R_j^{3+\varepsilon}}{\sqrt{W_j}}
<\infty.
}
\]

This is stronger than the terminal coherent-occupancy packing but can still hold on a sufficiently super-separated Zeno cascade.

Therefore the pinning theorem is a substantial branch reduction, not yet a contradiction.

Status: **RESIDUAL ACTION PINNED TO `R^-2` ON THE MINIMAL SURVIVOR / ABOVE IT RETURNS TO RESIDUAL-DERIVATIVE RECURSION / BELOW IT FORCES POLYNOMIAL AFFINE STRAIN OR GAUSSIAN SPATIAL ESCAPE / GLOBAL REGULARITY NOT PROVED.**
