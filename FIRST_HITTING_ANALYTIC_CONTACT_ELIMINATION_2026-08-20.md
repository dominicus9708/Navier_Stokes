# First-Hitting Analyticity and Elimination of Active KKT Contact — 2026-08-20

Overall status: **CONDITIONAL LOCAL CONTACT CLOSURE ON THE NON-H/T TYPE-I TOWER — GLOBAL REGULARITY NOT PROVED.**

This note combines the first-hitting vorticity cap with standard short-time spatial analyticity of Navier-Stokes and the preceding `H^1` Helmholtz contact-rigidity lemma.

The conclusion is that, on the bounded non-`H/T` Type-I threshold core, an effective lower-dimensional KKT contact multiplier cannot remain active once the standard first-hitting analytic smoothing is transferred to the normalized core. The remaining variational problem is therefore the smooth-reaction fourth-order strain problem (`Gamma_K=0`), not an arbitrary singular-measure KKT problem.

---

## 1. Restart the solution one natural time before first hitting

At a first-hitting time `t_j`,

\[
W_j=\|\omega(t_j)\|_\infty,
\]

and by definition

\[
\|\omega(t)\|_\infty\le W_j
\qquad(t\le t_j).
\]

Choose a fixed sufficiently small `theta>0` and set

\[
t_j^- = t_j-\theta W_j^{-1}.
\]

For all sufficiently late `j`, `t_j^->0`, and

\[
\|\omega(t_j^-)\|_\infty\le W_j.
\]

Classical vorticity analyticity theory for 3D Navier-Stokes gives a mild analytic continuation for a time interval bounded below by

\[
\frac{c}{\|\omega(t_j^-)\|_\infty}
\ge
\frac{c}{W_j},
\]

with spatial analyticity radius at elapsed time `theta/W_j` comparable to

\[
\sqrt{\frac{\theta}{W_j}}.
\]

Choose `theta<c` so that `t_j` lies inside that guaranteed analytic interval.

---

## 2. Normalized analyticity radius is order one

The first-hitting length is

\[
r_j=W_j^{-1/2}.
\]

Under the fixed-center normalized coordinates

\[
y=\frac{x-X_*}{r_j},
\]

the physical analyticity radius `~sqrt(theta/W_j)` becomes

\[
\boxed{\rho_{an}^{(j)}\gtrsim\sqrt\theta,}
\]

independent of `j`.

Likewise the analytically extended vorticity satisfies a normalized complex bound

\[
\boxed{
\sup_{|\Im y|<\rho_0}|\Omega_j(y,0)|\le M_0
}
\]

for fixed `rho_0,M_0` depending only on the analyticity theorem constants and the chosen restart fraction.

Cauchy estimates therefore give, for every fixed integer `m`,

\[
\boxed{
\|\nabla_y^m\Omega_j(\cdot,0)\|_{L^\infty(B_R)}
\le C_{m,R}
}
\]

on every fixed normalized core ball.

---

## 3. Transfer to local strain regularity

On the non-`T` Type-I branch, the fixed-center local energy quantity is bounded on every fixed parent ball. The elliptic relations

\[
-\Delta U=\nabla\times\Omega,
\qquad
\Sigma=\operatorname{sym}\nabla U
\]

combined with interior elliptic estimates transfer the normalized vorticity derivative bounds and local velocity-energy bound to every finite local Sobolev order of the strain.

In particular, for a threshold cell contained in a fixed normalized ball and a slightly larger parent ball,

\[
\boxed{
\|\Sigma_j\|_{H^5(B_R)}\le C_R
}
\]

for the late first-hitting sequence, unless an off-center/parent-ball derivative packet violates the non-`H/T` hypothesis.

Thus the threshold-core limit is locally `H^5` (indeed analytic) near its contact set.

---

## 4. The visible KKT reaction is locally H1

The KKT Euler field has schematic form

\[
F(\Sigma)
=\mathcal E_N
-2\Lambda\Delta^2\Sigma
-2\alpha\Sigma
-2\beta |y|^2\Sigma,
\]

followed by the strain projection. On a fixed bounded core, local `H^5` regularity of `Sigma` places `F(Sigma)` in local `H^1`.

Applying the order-zero strain-to-vorticity operator `B`,

\[
2P_{df}\mu=\mathcal B F(\Sigma),
\]

so the effective divergence-free KKT reaction

\[
f=P_{df}\mu
\]

belongs to `H^1_loc` on a neighborhood of the contact set.

---

## 5. Measure-zero contact plus local H1 removes the singular reaction

The contact set

\[
\mathcal M=\{|\Omega|=1\}
\]

has zero three-dimensional Lebesgue measure for a nonzero finite-energy analytic Navier-Stokes snapshot.

On the complement of `M`, the contact measure vanishes. Writing the Helmholtz decomposition

\[
\mu=f+\nabla\phi,
\qquad f=P_{df}\mu,
\]

we have

\[
f=-\nabla\phi
\]

away from `M`, hence

\[
\nabla\times f=0
\]

there.

Because `f in H^1_loc` near `M`, its curl is locally `L^2`; an `L^2` curl cannot be supported on the measure-zero set `M`. Hence the curl also vanishes through the contact set.

The visible reaction is divergence free by definition. Therefore it is locally both divergence free and curl free across the contact set. Together with the global decay/finite-energy class inherited by the threshold profile, this eliminates the nontrivial visible contact reaction:

\[
\boxed{P_{df}\mu=0.}
\]

Consequently

\[
\boxed{\Gamma_K=\langle\mu,\Omega\rangle=0.}
\]

---

## 6. Pohozaev identities collapse to the smooth slice

The KKT-corrected identities were

\[
\alpha E=\frac{N-5\Gamma_K}{4},
\qquad
\beta M=\frac{N+3\Gamma_K}{4}.
\]

With the effective contact reaction eliminated,

\[
\boxed{
\alpha E=\beta M=\frac14N.
}
\]

Thus any non-`H/T` threshold maximizer with `Lambda>=nu` must satisfy the **smooth-reaction confined fourth-order strain Euler-Lagrange system**. The contact set may still geometrically contain first-hitting maxima, but it is variationally invisible: it carries no nonzero divergence-free KKT reaction.

---

## 7. What remains

This does not prove `Lambda_K<nu`. It removes the singular-measure contact branch from the non-`H/T` Type-I system and leaves the smoother problem

\[
\boxed{
P_{st}[\mathcal E_N
-2\Lambda\Delta^2S
-2\alpha S
-2\beta |x|^2S]=0,
\qquad
\alpha E=\beta M=N/4,
\qquad
\Lambda\ge\nu.
}
\]

The next target is to derive an additional virial/spectral identity for this confined fourth-order system and test whether a nonzero strain-compatible solution can cross the viscosity threshold.

Status: **ON THE NON-H/T TYPE-I FIRST-HITTING TOWER, STANDARD ANALYTIC SMOOTHING PROVIDES ORDER-ONE NORMALIZED ANALYTICITY ON THE BOUNDED THRESHOLD CORE. COMBINED WITH THE H1 HELMHOLTZ CONTACT LEMMA, THIS REMOVES THE EFFECTIVE SINGULAR KKT CONTACT REACTION AND REDUCES THE LOCAL ENDGAME TO A SMOOTH CONFINED FOURTH-ORDER VARIATIONAL SYSTEM. GLOBAL REGULARITY REMAINS UNPROVED.**