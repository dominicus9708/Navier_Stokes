# Deep-checkpoint affine branch forces a superlarge ordinary strain--palinstrophy product

Date: 2026-08-16

Status: **DERIVED FOR THE EXACT LINEAR AFFINE ADVECTION--STRETCH--DIFFUSION COMPARISON. IN A FULL NAVIER--STOKES WINDOW THIS IS THE AFFINE-DOMINANT BRANCH; FAILURE OF THE COMPARISON IS EXPLICITLY A RESIDUAL/NONLINEAR CHANNEL. GLOBAL REGULARITY NOT PROVED.**

## 1. Deep checkpoint and coherent crossing

At a terminal first-hitting normalization let

\[
\|\Omega\|_\infty\le 1,
\qquad
BR^4=1,
\qquad
R\to\infty.
\]

Choose a deep first-hitting checkpoint

\[
\boxed{q_\beta=\frac{W}{R^\beta}},
\qquad
0<\beta<4,
\]

so that the previous physical vorticity height is `R^beta` and, in terminal normalized variables,

\[
\boxed{\|\Omega_-\|_\infty\le q_\beta^{-1}.}
\]

The already-derived first-hitting enstrophy ceiling gives

\[
\boxed{E_-\lesssim \frac{R^\beta}{W^{1/2}}.}
\]

The coherent-crossing Gaussian-tail energy relation is

\[
\boxed{W^{1/2}\gtrsim R^5(\log R)^{5/2}.}
\]

---

## 2. Rotation-independent affine heat tradeoff

For an exact volume-preserving linear affine model

\[
\partial_s\omega+(L(s)y)\cdot\nabla\omega
=L(s)\omega+\nu\Delta\omega,
\qquad \operatorname{tr}L=0,
\]

write

\[
J=\int\|\operatorname{sym}L(s)\|_{op}^2ds.
\]

The existing rotation-independent affine theorem gives, for a genuine vector amplification factor `q>=2`,

\[
\boxed{J\,M_\Pi^2\gtrsim \nu q,}
\]

where `M_Pi` is the precursor `L^infty L^2_transverse` mixed norm in the accumulated-heat covariance frame.

The trace estimate gives

\[
\boxed{M_\Pi^4\le 4E_-P_{e,-},}
\]

with

\[
P_{e,-}=\|\partial_e\Omega_-\|_2^2.
\]

Therefore

\[
\boxed{J^2 E_-P_{e,-}\gtrsim \nu^2q^2.}
\]

This statement already includes arbitrary time intermittency and arbitrary rotation of the affine eigendirections.

---

## 3. Insert the deep-checkpoint ceiling

Take the affine amplification target to be a fixed fraction of

\[
q=q_\beta=\frac{W}{R^\beta}.
\]

Then

\[
J^2P_{e,-}
\gtrsim
\nu^2\frac{q_\beta^2}{E_-}.
\]

Using

\[
E_-\lesssim R^\beta W^{-1/2},
\]

we obtain

\[
\boxed{
J^2P_{e,-}
\gtrsim
\nu^2\frac{W^{5/2}}{R^{3\beta}}.
}
\]

This is the deep-checkpoint affine product barrier.

---

## 4. Crossing-scale form

The Gaussian-tail relation

\[
W^{1/2}\gtrsim R^5(\log R)^{5/2}
\]

implies

\[
W^{5/2}
\gtrsim
R^{25}(\log R)^{25/2}.
\]

Hence

\[
\boxed{
J^2P_{e,-}
\gtrsim
\nu^2
R^{25-3\beta}(\log R)^{25/2}.
}
\]

For every fixed

\[
0<\beta<4,
\]

the power satisfies

\[
25-3\beta>13.
\]

For the convenient choice `beta=2`,

\[
\boxed{
J^2P_{e,-}
\gtrsim
\nu^2R^{19}(\log R)^{25/2}.
}
\]

Thus an affine-dominant deep-to-late amplification cannot remain in a bounded ordinary strain-energy / ordinary directional-palinstrophy state.

---

## 5. Exact bounded-factor consequences

If `J<=J0` is bounded along a candidate sequence, then

\[
\boxed{
P_{e,-}
\gtrsim
\frac{\nu^2}{J_0^2}
\frac{W^{5/2}}{R^{3\beta}}
\to\infty.
}
\]

If instead `P_{e,-}<=P0` is bounded, then

\[
\boxed{
J
\gtrsim
\frac{\nu}{\sqrt{P_0}}
\frac{W^{5/4}}{R^{3\beta/2}}
\to\infty.
}
\]

Thus the affine branch has no bounded-state saturation. No arbitrary splitting exponent is needed: the product lower bound itself is the invariant statement.

---

## 6. Relation to the stochastic deformation endgame

The stochastic Cauchy analysis showed that a late coherent core can avoid large stochastic-invariant variance only by having a non-negligible set of histories with large deformation.

If those histories are approximately described by one common volume-preserving affine deformation and the exact path law remains perturbatively close to the matched affine Gaussian, then the present theorem applies and forces the huge ordinary product

\[
\boxed{J^2P_{e,-}.}
\]

Therefore a cheap low-variance stochastic deformation cannot remain simultaneously

- affine-dominant,
- low coherent strain-energy,
- and low ordinary precursor palinstrophy.

If the exact Navier--Stokes window is not perturbatively affine, the failure must be charged separately to the already typed residual transport / residual gradient / kernel non-Gaussianity / high-curvature channels.

---

## 7. Claim boundary

This note does **not** transfer the affine heat theorem automatically to the full nonlinear Navier--Stokes flow.

The remaining nonlinear transfer problem is now explicit:

\[
\boxed{
\text{either the exact stochastic tube is affine-Gaussian enough for the product barrier,}
\quad\text{or the deviation itself must be quantitatively charged.}
}
\]

The existing Girsanov residual-transport, kernel regression/relative-score, Gaussian residual `B_K`, and high-curvature ledgers are the intended charges.

Overall status: **AFFINE-DOMINANT STOCHASTIC SATURATION ROUTED TO A SUPERLARGE ORDINARY STRAIN--PALINSTROPHY PRODUCT / NONLINEAR AFFINE-TRANSFER ERROR REMAINS THE ACTIVE BRIDGE.**
