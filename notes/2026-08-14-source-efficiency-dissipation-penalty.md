# Source-efficiency dissipation penalty

Date: 2026-08-14

Status: **DERIVED REFINEMENT OF THE TYPED RESIDUAL DISSIPATION LEDGER / GLOBAL REGULARITY NOT PROVED**.

This note prices a second possible escape of the residual source: inefficient conversion of residual variance into mean-vorticity source.

## 1. Effective source efficiency

On a responsible bounded-affine interval `I`, write

\[
B=\mathcal B_\gamma,
\qquad
\Theta=\frac{V_\omega}{B}.
\]

The typed source estimate is

\[
|J|\lesssim_K B\sqrt\Theta.
\]

Define the interval efficiency cap

\[
\boxed{
\mathcal E
:=
\sup_I
\frac{|J|}{C_K B\sqrt\Theta}
\in[0,1],
}
\]

with the quotient set to zero when `B Theta=0`.

Also set

\[
\Theta_*:=\sup_I\Theta.
\]

Then

\[
|J|\le C_K\mathcal E\sqrt{\Theta_*}\,B.
\]

## 2. Required B-mass

Suppose the interval must supply a fixed endpoint residual source contribution at least `rho>0`.

Then

\[
\rho
\lesssim_K
\int_I |J|d\tau
\le
C_K\mathcal E\sqrt{\Theta_*}
\int_I B(\tau)d\tau.
\]

Therefore

\[
\boxed{
\int_I B(\tau)d\tau
\gtrsim_{K,\rho}
\frac1{\mathcal E\sqrt{\Theta_*}}.
}
\]

Thus low source efficiency forces proportionally more residual-variance time mass.

## 3. Rearrangement with efficiency

Let

\[
m=\|B\|_{L^\infty(I)}.
\]

The Gaussian-volume dissipation argument gives

\[
\|\nabla U(\tau)\|_2^2
\gtrsim_K
\tau^{3/2}B(\tau).
\]

For a nonnegative function bounded by `m` and with mass

\[
M_B\gtrsim
(\mathcal E\sqrt{\Theta_*})^{-1},
\]

the bathtub principle yields

\[
\int_I\tau^{3/2}B(\tau)d\tau
\gtrsim
M_B^{5/2}m^{-3/2}.
\]

Hence

\[
\boxed{
D_{\rm phys}(I)
\gtrsim
W^{-1/2}m^{-3/2}
\mathcal E^{-5/2}
\Theta_*^{-5/4}.
}
\]

This is the earlier typed dissipation lower bound with the additional efficiency penalty `E^(-5/2)`.

## 4. Survival variables

Write

\[
m=W^{-1/3}\Lambda
\]

and define

\[
H_*:=\Lambda\Theta_*^{5/6}.
\]

Then

\[
W^{-1/2}m^{-3/2}\Theta_*^{-5/4}
=
H_*^{-3/2}.
\]

Therefore

\[
\boxed{
D_{\rm phys}(I)
\gtrsim
H_*^{-3/2}\mathcal E^{-5/2}.
}
\]

For infinitely many disjoint first-hitting intervals and finite total physical dissipation, a necessary asymptotic escape condition is

\[
H_*^{-3/2}\mathcal E^{-5/2}\to0.
\]

Equivalently,

\[
\boxed{
\mathcal E\,H_*^{3/5}\to\infty.
}
\]

Thus a surviving infinite residual cascade cannot simultaneously have only moderate `H` and a highly inefficient residual-to-mean source conversion.

## 5. Revised source ledger

The old survival requirement was

\[
H=\Lambda\Theta^{5/6}\to\infty.
\]

The refined requirement is stronger when the responsible source is inefficient:

\[
\boxed{
\mathcal E H^{3/5}\to\infty
}
\]

in the approximately fixed-`Theta` formulation, or with `H_*` when using interval suprema.

This is useful for the quadratic Hermite core because the exact zero-set lemma shows that a source-efficient nonzero mean transfer must also generate a nonzero second-chaos output. Conversely, approaching the algebraic zero set necessarily drives the mean-source efficiency toward zero, which is now itself charged by physical dissipation.

## 6. Next use

The remaining finite-dimensional target is a quantitative relation of the form

\[
|J_{\rm core}|^2
\le
C\sqrt{BV_\omega}\,
\|N_{\omega,2}^{\rm core}\|_2.
\]

If obtained, source efficiency would force

\[
\|N_{\omega,2}^{\rm core}\|_2
\gtrsim
\mathcal E^2 B\sqrt\Theta,
\]

while the present lemma prevents `E` from becoming arbitrarily small fast enough to evade every stepwise budget.

Status: **INEFFICIENT SOURCE ESCAPE PRICED / SURVIVAL REQUIRES `E H^(3/5) -> infinity` / READY TO COMBINE WITH SECOND-CHAOS COERCIVITY.**
