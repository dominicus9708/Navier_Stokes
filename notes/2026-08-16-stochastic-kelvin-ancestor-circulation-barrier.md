# Stochastic Kelvin ancestor circulation barrier

Date: 2026-08-16

Status: **EXACT EXTERNAL STOCHASTIC-KELVIN INPUT + DERIVED ANCESTOR AREA/LENGTH BARRIER / GLOBAL REGULARITY NOT PROVED**.

## 1. Why this note is needed

The previous frontier left a seemingly cheap escape:

\[
\text{precompress an almost flux-free material core}
\;\to\;
\text{inject the final circulation only at the smallest scale by viscosity}.
\]

That escape is real in a deterministic material-surface ledger because viscosity changes deterministic material vorticity flux.

However, smooth Navier--Stokes solutions satisfy a stochastic Kelvin theorem.  In that representation the present circulation is inherited, in expectation, from earlier stochastic backward loops.  Thus deterministic late injection is not creation from nothing once the correct stochastic Lagrangian ancestry is used.

Primary external inputs:

- P. Constantin and G. Iyer, *A stochastic Lagrangian representation of the three-dimensional incompressible Navier--Stokes equations*, Comm. Pure Appl. Math. 61 (2008), 330--345.
- G. L. Eyink, *Stochastic Least-Action Principle for the Incompressible Navier--Stokes Equation*, Physica D 239 (2010), 1236--1240; arXiv:0810.0817.

Eyink's Proposition 2 restates the Constantin--Iyer theorem in the backward form used below.

---

## 2. Stochastic Kelvin theorem in the present notation

Let `t_- < t_c` and let `C_c` be a closed rectifiable loop at the coherent crossing time `t_c`.

Let

\[
C_-^\varpi
=
X_{t_c,t_-}^\varpi(C_c)
\]

be its backward stochastic image under the Constantin--Iyer incompressible stochastic flow.

Then

\[
\boxed{
\Gamma_c
:=
\oint_{C_c}U(t_c)\cdot d\ell
=
\mathbb E\left[
\oint_{C_-^\varpi}U(t_-)\cdot d\ell
\right].
}
\]

Write

\[
\Gamma_-^\varpi
=
\oint_{C_-^\varpi}U(t_-)\cdot d\ell.
\]

Hence

\[
\boxed{
\Gamma_c=\mathbb E\Gamma_-^\varpi.
}
\]

This is the correct stochastic replacement for deterministic material-flux conservation.

---

## 3. Apply at the coherent Reynolds-one crossing

At the coherent crossing select a loop inside the nearly one-axis core so that its spanning disk has normalized area

\[
A_c\asymp R^2
\]

and, by the order-one coherent mean vorticity,

\[
\boxed{
\Gamma_c\ge \kappa R^2
}
\]

for a fixed `kappa>0` after choosing the orientation.

At a `q`-earlier first-hitting checkpoint,

\[
\boxed{
\|\Omega(t_-)\|_\infty\le q^{-1}.
}
\]

For each stochastic ancestor loop choose any spanning surface `Sigma_-^varpi`.  Stokes' theorem gives

\[
\Gamma_-^\varpi
=
\int_{\Sigma_-^\varpi}
\Omega(t_-)\cdot n\,dA.
\]

Therefore

\[
\boxed{
|\Gamma_-^\varpi|
\le q^{-1}\operatorname{Area}(\Sigma_-^\varpi).
}
\]

Taking the infimum over all spanning surfaces gives the same inequality with the minimal spanning area `A_min^varpi`:

\[
\boxed{
A_{\min}^\varpi
\ge q|\Gamma_-^\varpi|.
}
\]

---

## 4. Existence of a large-flux stochastic ancestor

Since

\[
\mathbb E\Gamma_-^\varpi
=
\Gamma_c>0,
\]

there exists at least one realization `varpi_*` such that

\[
\boxed{
\Gamma_-^{\varpi_*}
\ge
\Gamma_c
\ge
\kappa R^2.
}
\]

For that realization,

\[
\boxed{
A_{\min}^{\varpi_*}
\ge
\kappa qR^2.
}
\]

Thus a final coherent circulation of size `R^2` cannot have *all* earlier stochastic ancestors flux-free or small.

There is always at least one backward stochastic ancestor loop in the same physical earlier velocity/vorticity field which carries at least the final signed circulation.

This removes the previous deterministic picture

\[
\boxed{
\text{all ancestors empty}
\to
\text{circulation created only at the end}
}
\]

from the stochastic-Lagrangian proof tree.

---

## 5. RMS area barrier without selecting one realization

The same conclusion can be kept at the expectation level:

\[
\Gamma_c
\le
\mathbb E|\Gamma_-^\varpi|
\le
q^{-1}\mathbb E A_{\min}^\varpi.
\]

Hence

\[
\boxed{
\mathbb E A_{\min}^\varpi
\ge
q\Gamma_c
\gtrsim
qR^2.
}
\]

So the stochastic ancestor ensemble has an unavoidable mean area inflation by a factor of order `q` relative to the final cross-section.

---

## 6. Loop-length consequence

A standard Euclidean isoperimetric filling inequality for rectifiable closed curves gives a universal constant `C_iso` such that a loop of length `L` admits a spanning surface of area at most

\[
A_{\min}
\le
C_{\rm iso}L^2.
\]

Therefore

\[
L_-^{\varpi\,2}
\ge
C_{\rm iso}^{-1}A_{\min}^\varpi.
\]

For the selected large-circulation ancestor,

\[
\boxed{
L_-^{\varpi_*}
\gtrsim
R\sqrt q.
}
\]

At the expectation level,

\[
\boxed{
\mathbb E\big[L_-^{\varpi\,2}\big]
\gtrsim
qR^2.
}
\]

Thus the earlier stochastic ancestry is necessarily super-natural in geometric length.

---

## 7. Relation to the previous pancake obstruction

The deterministic flux-retaining precursor analysis had already shown that a bounded-shape cross-section with

\[
\Phi\sim R^2,
\qquad
\|\Omega_-\|_\infty\le q^{-1}
\]

requires transverse scale at least

\[
R\sqrt q,
\]

and cannot terminate cheaply because `div Omega=0`.

The stochastic Kelvin theorem now shows that viscosity does not eliminate this ancestry requirement.  Instead it randomizes which backward loop carries the circulation.

Hence the old late-injection branch is replaced by the dichotomy

\[
\boxed{
\text{stochastic ancestor has large geometric extent}
}
\]

or

\[
\boxed{
\text{the long ancestor loop/surface is packed by strong crumpling, curvature, or multiplicity}.
}
\]

The first option returns to the spatial non-tightness / oriented-flux persistence / critical-L3 shell routes.

The second option returns to material-probe `H2` distortion and higher-derivative/high-curvature channels.

---

## 8. Strain-action corollary

Because the additive Brownian noise has no spatial derivative, the derivative of each stochastic flow realization evolves through the physical velocity gradient.

If the final loop has length `L_c\asymp R`, then pathwise

\[
L_-^\varpi
\le
L_c
\exp\left(
\int_{t_-}^{t_c}\|S(t)\|_\infty dt
\right).
\]

For the selected ancestor with

\[
L_-^{\varpi_*}\gtrsim R\sqrt q,
\]

we obtain

\[
\boxed{
\int_{t_-}^{t_c}\|S(t)\|_\infty dt
\ge
\frac12\log q-O(1).
}
\]

This is weaker in coefficient than the previously derived material-area / maximum-vorticity `log q` action, but it is important conceptually: it follows even when deterministic material flux is allowed to reset viscously.

---

## 9. What this closes

The previous frontier treated

\[
\text{precompression}
+\text{late viscous flux injection}
\]

as the sharp escape from the deterministic reset-energy lower bound.

After stochastic Kelvin,

\[
\boxed{
\textbf{late deterministic injection is not an independent ancestry escape.}
}
\]

The final circulation must still possess stochastic backward ancestors with large circulation and correspondingly large filling area/loop length.

Therefore the true remaining issue is no longer whether the flux can be created only at the end.  It is whether the required stochastic ancestors can repeatedly evade all finite-energy/spatial-tightness constraints by becoming increasingly long, crumpled, curved, or intermittent.

---

## 10. Claim boundary

This note does **not** prove that a long stochastic ancestor loop forces a forbidden kinetic-energy cost without additional geometric control.

A rectifiable loop can in principle have very large length while remaining in a small spatial region by crumpling or high curvature.  Likewise a large minimal filling area does not by itself produce a three-dimensional coherent vortex tube.

Hence the next theorem must be a geometric compactness/curvature dichotomy for the stochastic ancestor family:

\[
\boxed{
\text{large inherited circulation + first-hitting cap}
\Longrightarrow
\text{large spatial extent}
\;\lor\;
\text{quantified curvature / derivative cost}.
}
\]

Overall status: **PRECOMPRESSION--LATE-INJECTION ESCAPE REMOVED AS AN INDEPENDENT STOCHASTIC-LAGRANGIAN BRANCH / STOCHASTIC ANCESTOR GEOMETRIC DEGENERATION IS THE NEW ACTIVE FRONTIER / GLOBAL REGULARITY NOT PROVED.**
