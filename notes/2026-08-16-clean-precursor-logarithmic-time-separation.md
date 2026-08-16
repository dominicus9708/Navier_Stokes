# Clean precursor and coherent crossing are separated by a logarithmically long normalized time

Date: 2026-08-16

Status: **EXACT CONSEQUENCE OF THE FIRST-HITTING `L^infty` CAP, THE CLEAN ENSTROPHY-MINIMUM CHECKPOINT, AND THE COHERENT-CROSSING `R^3` ENSTROPHY OCCUPANCY. GLOBAL REGULARITY NOT PROVED.**

## 1. First-hitting enstrophy growth ceiling

On the terminal first-hitting past,

\[
\|\Omega(s)\|_\infty\le1.
\]

The global enstrophy identity is

\[
\frac12E'(s)+\nu P(s)=Q(s),
\qquad
Q=\int S\Omega\cdot\Omega.
\]

Calderon--Zygmund and interpolation give

\[
|Q|
\lesssim
\|\Omega\|_\infty E
\lesssim E.
\]

Discarding the nonnegative viscous term,

\[
\boxed{
E'(s)\le C E(s).
}
\]

Thus enstrophy can grow at most exponentially at an order-one rate in terminal normalized time.

---

## 2. Clean minimum-enstrophy precursor

Choose the deep checkpoint

\[
q_\beta=W/R^\beta,
\qquad
0<\beta<4,
\]

and then choose

\[
s_m\in[s_-,s_c]
\]

at the minimum of enstrophy.

The first-hitting logistic ceiling gives

\[
E_m
\le E_-
\lesssim
\frac{R^\beta}{W^{1/2}}.
\]

The coherent crossing has an order-one vorticity field on an `O(R^3)` good core, so

\[
\boxed{
E_c:=E(s_c)\gtrsim R^3.
}
\]

---

## 3. Integrate the growth ceiling

From

\[
E'\le CE
\]

we get

\[
E_c
\le
E_m\exp(C(s_c-s_m)).
\]

Therefore

\[
\boxed{
s_c-s_m
\ge
c\log\frac{E_c}{E_m}.
}
\]

Using the preceding bounds,

\[
\frac{E_c}{E_m}
\gtrsim
R^{3-\beta}W^{1/2}.
\]

Hence

\[
\boxed{
s_c-s_m
\gtrsim
\log(R^{3-\beta}W^{1/2}).}
\]

---

## 4. Crossing-scale lower bound

The Gaussian-tail energy relation is

\[
W^{1/2}
\gtrsim
R^5(\log R)^{5/2}.
\]

Therefore

\[
R^{3-\beta}W^{1/2}
\gtrsim
R^{8-\beta}(\log R)^{5/2}.
\]

Thus

\[
\boxed{
s_c-s_m
\gtrsim
(8-\beta)\log R
+\frac52\log\log R
-O(1).
}
\]

For every fixed `0<beta<4`,

\[
\boxed{
s_c-s_m\to\infty.}
\]

In particular, for `beta=2`, the normalized separation is at least `c log R` with a positive universal coefficient after fixed constants are absorbed.

---

## 5. Physical-time interpretation

Terminal normalized time and physical time are related by

\[
ds=Wdt.
\]

Hence the physical duration corresponding to this lower bound is

\[
\Delta t_{m\to c}
\gtrsim
\frac{\log R}{W}.
\]

This still tends to zero along a hypothetical singular sequence, so the result does not contradict finite-time Zeno accumulation by itself.

What is important is that in the rescaled equation the vorticity has a logarithmically long interval on which viscosity acts with the fixed coefficient `nu`.

---

## 6. Diffusive significance

Over a time interval of length

\[
T_R\gtrsim\log R,
\]

ordinary isotropic diffusion has spatial scale

\[
\boxed{
\ell_{\rm diff}
\sim
\sqrt{\nu T_R}
\gtrsim
\sqrt{\nu\log R}.
}
\]

The pathwise deformation--diffusion theorem strengthens this along a large-deformation stochastic history: if the final stretch is `q_p`, then the two-dimensional pulled-back Malliavin diffusion area satisfies

\[
(\mu_2\mu_3)^{1/2}
\gtrsim
\frac{q_p}{J_p}.
\]

Thus the final random-Gramian smoothing problem is not a vanishing-time endpoint problem. It occurs across a terminal-normalized interval whose length diverges at least logarithmically.

---

## 7. Integrated logarithmic enstrophy identity

Retaining the exact viscous term gives

\[
\frac12(\log E)'
=
\frac{Q}{E}
-\nu\frac{P}{E}.
\]

Integrating from `s_m` to `s_c`,

\[
\boxed{
\frac12\log\frac{E_c}{E_m}
+
\nu\int_{s_m}^{s_c}\frac{P}{E}ds
=
\int_{s_m}^{s_c}\frac{Q}{E}ds.
}
\]

Therefore the large enstrophy growth requires a large accumulated normalized stretching efficiency, with viscous `P/E` making the required source action even larger rather than smaller.

This identity is a useful bridge to the projective/coherence source-depletion ledgers.

---

## 8. Updated use

A hypothetical survivor from the clean precursor to the coherent crossing must now satisfy simultaneously

\[
\boxed{
E_m\to0,
\quad
P_m\lesssim E_m,
\quad
M_{\Pi,e}^2\lesssim E_m\ \forall e,
}
\]

and

\[
\boxed{
s_c-s_m\gtrsim c\log R.}
\]

Thus any final Malliavin/mixed-norm smoothing theorem is allowed a logarithmically long normalized diffusion interval; failure must be paid by the already identified deformation-weighted Hessian / derivative channel.

Overall status: **CLEAN PRECURSOR CANNOT BE ARBITRARILY CLOSE IN NORMALIZED TIME TO THE COHERENT CROSSING / MINIMUM SEPARATION IS LOGARITHMIC IN `R`.**
