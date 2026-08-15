# Mesoscopic annulus strain action has an `R (log q)^2` enstrophy price

Date: 2026-08-16

Status: **DERIVED DYADIC SHELL ACTION BOUND / CRITICAL PHYSICAL COST REMAINS SUMMABLE / GLOBAL REGULARITY NOT PROVED.**

## 1. Active annulus

The stochastic directional-stretching localization leaves the mesoscopic annulus

\[
\mathcal A_{R,M_*}
=\{y:R<|y-x_*|<M_*\},
\]

where

\[
M_*=R^{4/5}W^{1/10},
\qquad
M_*/R\to\infty,
\qquad
M_*/\sqrt W\to0.
\]

The coherent core and the region beyond `M_*` contribute only `O(1)` directional action on a crossing-parabolic block of normalized duration `T ~ R^2`.

Hence if the annular field is the branch responsible for a large amplification, it must provide an action

\[
A_{\rm ann}\gtrsim \log q-O(1).
\]

---

## 2. One dyadic shell

Let

\[
A_r=\{y:r<|y-x_*|<2r\},
\]

and define its enstrophy

\[
E_r(s)=\int_{A_r}|\Omega(y,s)|^2dy.
\]

The Biot--Savart strain kernel has size `|z|^-3`. Therefore the shell contribution to the common strain seen by the core obeys

\[
|S_r(s)|
\lesssim
r^{-3}\int_{A_r}|\Omega|dy.
\]

By Cauchy--Schwarz and `|A_r| ~ r^3`,

\[
\int_{A_r}|\Omega|dy
\lesssim
r^{3/2}E_r(s)^{1/2}.
\]

Hence

\[
\boxed{
|S_r(s)|
\lesssim
r^{-3/2}E_r(s)^{1/2}.
}
\]

This is the natural shell estimate at the borderline three-dimensional strain homogeneity.

---

## 3. Time-integrated shell action

Let `I` be a crossing-parabolic block with

\[
|I|\lesssim C R^2.
\]

Define

\[
D_r
=\int_I E_r(s)ds.
\]

Then Cauchy--Schwarz in time gives

\[
\begin{aligned}
A_r
&:=\int_I |S_r(s)|ds\\
&\lesssim
r^{-3/2}|I|^{1/2}D_r^{1/2}\\
&\lesssim
Rr^{-3/2}D_r^{1/2}.
\end{aligned}
\]

Thus

\[
\boxed{
A_r\lesssim Rr^{-3/2}D_r^{1/2}.
}
\]

---

## 4. Sum disjoint dyadic shells

Take

\[
r_k=2^kR,
\]

for all shells contained in `[R,M_*]`. The shell regions are disjoint, so

\[
\sum_k D_{r_k}
\le
D_{\rm ann},
\]

where

\[
D_{\rm ann}
:=
\int_I\int_{\mathcal A_{R,M_*}}|\Omega|^2dy ds.
\]

Summing the shell actions and applying Cauchy--Schwarz in `k`,

\[
\begin{aligned}
A_{\rm ann}
&\lesssim
R\sum_k r_k^{-3/2}D_{r_k}^{1/2}\\
&\le
R
\left(\sum_k r_k^{-3}\right)^{1/2}
\left(\sum_kD_{r_k}\right)^{1/2}.
\end{aligned}
\]

Because

\[
\sum_k r_k^{-3}
\lesssim R^{-3},
\]

we obtain

\[
\boxed{
A_{\rm ann}
\lesssim
R^{-1/2}D_{\rm ann}^{1/2}.
}
\]

Equivalently,

\[
\boxed{
D_{\rm ann}
\gtrsim
R A_{\rm ann}^2.
}
\]

---

## 5. Price of supplying the missing logarithmic amplification

If the coherent core and far field contribute only `O(1)` and direction/Hessian channels remain subcritical, then the annulus must supply

\[
A_{\rm ann}\gtrsim c\log q.
\]

Therefore

\[
\boxed{
D_{\rm ann}
\gtrsim
cR(\log q)^2.
}
\]

This is stronger than a bare logarithmic shell count: the disjoint-shell geometry converts the required strain action into a growing normalized enstrophy-action price.

---

## 6. Physical scaling audit

Under terminal normalization,

\[
E_{\rm norm}=W^{-1/2}E_{\rm phys},
\qquad
 ds=Wdt.
\]

Hence

\[
D_{\rm norm}
=W^{1/2}
\int E_{\rm phys}(t)dt.
\]

Thus one crossing with the annular lower bound costs in the physical kinetic-energy dissipation ledger

\[
\boxed{
\int_I E_{\rm phys}dt
\gtrsim
W^{-1/2}R(\log q)^2.
}
\]

This quantity can still be summable along a sufficiently rapidly separated singular cascade. Therefore the estimate is not a contradiction by itself.

---

## 7. What is now typed

The mesoscopic-annulus branch is no longer a cost-free common-strain source:

\[
\boxed{
\text{annular }\log q\text{ directional strain}
\Longrightarrow
D_{\rm ann}\gtrsim R(\log q)^2.
}
\]

If this price is avoided, the missing action must be supplied by

- fast temporal/eigenframe variation;
- projective/direction breakdown;
- Hessian/high-derivative concentration;
- or a resonant axisymmetric component not removed by fast-rotation averaging.

The next target is to use the coherent fast rotation to eliminate non-axisymmetric slowly varying annular strain, leaving only an axisymmetric extensional component or temporal-derivative resonance.

Overall status: **MESOSCOPIC ANNULAR COMMON STRAIN HAS A GROWING NORMALIZED ENSTROPHY PRICE / PHYSICAL CRITICAL SUMMABILITY REMAINS.**
