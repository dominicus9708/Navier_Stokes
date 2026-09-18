# M19-425 — Bernoulli sorting splits into a critical radial-strain floor or tangential pressure-gradient floor

Date: 2026-09-19  
Canonical ID: **M19-425**  
Status: **BERNOULLI-SORTING CHANNEL CLOSURE AUDIT / KINETIC SORTING FORCES A QUANTITATIVE RECURRENT RADIAL-STRAIN FLOOR / PRESSURE SORTING FORCES A QUANTITATIVE TANGENTIAL PRESSURE-GRADIENT FLOOR / BOTH ARE SCALE-CRITICAL AND DO NOT SUPPLY A NEW NONSUMMABLE OR MONOTONE RESOURCE / RADIAL BRC ROUTE RECLASSIFIED INTO EXISTING CRITICAL STRUCTURE / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-424

Assume the genuinely new radial subbranch has positive Bernoulli sorting

\[
\boxed{
\langle\Gamma_B\rangle
\ge
\gamma_B>0,
}
\]

where

\[
\Gamma_B
=
\int_{S^2}
\left(
\frac12|A|^2+P
\right)A_r,d\omega.
\]

Split

\[
\boxed{
\Gamma_B
=
\Gamma_K+\Gamma_P
}
\]

with

\[
\Gamma_K
:=
\frac12
\int_{S^2}|A|^2A_r,d\omega,
\]

and

\[
\Gamma_P
:=
\int_{S^2}P A_r,d\omega.
\]

Then at least one invariant mean satisfies

\[
\boxed{
\langle\Gamma_K\rangle
\ge
\frac{\gamma_B}{2}
}
\]

or

\[
\boxed{
\langle\Gamma_P\rangle
\ge
\frac{\gamma_B}{2}.
}
\]

## 2. Kinetic-sorting branch

Suppose

\[
\langle\Gamma_K\rangle
\ge
\frac{\gamma_B}{2}.
\]

Then

\[
\boxed{
\left\langle
\int|A|^2A_r
\right\rangle
\ge
\gamma_B.
}
\]

Since the negative radial sector can only lower the signed integral,

\[
\boxed{
\left\langle
\int|A|^2(A_r)_+
\right\rangle
\ge
\gamma_B.
}
\]

Let the compact hard hull have the amplitude ceiling

\[
|A|\le M_A.
\]

Define

\[
S_+(q)
:=
\int_{S^2}(A_r)_+d\omega.
\]

Then

\[
\gamma_B
\le
M_A^2\langle S_+\rangle,
\]

so

\[
\boxed{
\langle S_+\rangle
\ge
\frac{\gamma_B}{M_A^2}.
}
\]

Because

\[
\int A_r=0,
\]

the inward absolute crossing has the same mean.

## 3. Kinetic sorting forces an L2 radial-amplitude floor

For every sphere,

\[
S_+(q)
\le
(4\pi)^{1/2}
\|A_r(q)\|_{L^2(S^2)}.
\]

Hence, by Jensen/Cauchy-Schwarz in the invariant mean,

\[
\boxed{
\left\langle
\|A_r\|_2^2
\right\rangle
\ge
\frac{\gamma_B^2}
{4\pi M_A^4}.
}
\]

Thus positive kinetic Bernoulli sorting cannot be carried by an arbitrarily weak radial component.

## 4. Exact recurrent radial-strain identity

The physical radial normal strain coefficient is

\[
\boxed{
\Sigma_{rr}
=
\partial_qA_r-A_r.
}
\]

Translation invariance gives

\[
\left\langle
\int A_r\partial_qA_r
\right\rangle
=0.
\]

Therefore, exactly as in M5-235,

\[
\boxed{
\left\langle
\|\Sigma_{rr}\|_2^2
\right\rangle
=
\left\langle
\|\partial_qA_r\|_2^2
+
\|A_r\|_2^2
\right\rangle.
}
\]

Combining with Section 3,

\[
\boxed{
\left\langle
\|\Sigma_{rr}\|_2^2
\right\rangle
\ge
\frac{\gamma_B^2}
{4\pi M_A^4}.
}
\]

Hence

\[
\boxed{
\mathcal B_{kinetic-sort}
\Longrightarrow
\text{fixed recurrent critical radial-strain energy}.
}
\]

This imports the M5-235 branch merger into the current residual-active terminal frontier.

## 5. Pressure-sorting branch

Now suppose

\[
\boxed{
\langle\Gamma_P\rangle
=
\left\langle
\int P A_r
\right\rangle
\ge
\frac{\gamma_B}{2}.
}
\]

For every q,

\[
\int_{S^2}A_r,d\omega=0.
\]

Let \(\chi(q,\cdot)\) be the unique zero-mean solution

\[
\boxed{
-\Delta_{S^2}\chi=A_r.
}
\]

Then

\[
\int P A_r
=
\int
\nabla_{S^2}P
\cdot
\nabla_{S^2}\chi.
\]

The first nonzero scalar spherical eigenvalue is \(2\), so

\[
\boxed{
\|\nabla_{S^2}\chi\|_2
\le
\frac1{\sqrt2}
\|A_r\|_2.
}
\]

## 6. Quantitative pressure-gradient floor

Cauchy-Schwarz in the invariant mean gives

\[
\frac{\gamma_B}{2}
\le
\frac1{\sqrt2}
\left\langle
\|\nabla_SP\|_2^2
\right\rangle^{1/2}
\left\langle
\|A_r\|_2^2
\right\rangle^{1/2}.
\]

The compact amplitude ceiling gives

\[
\|A_r\|_2^2
\le
4\pi M_A^2.
\]

Therefore

\[
\boxed{
\left\langle
\|\nabla_{S^2}P\|_2^2
\right\rangle
\ge
\frac{\gamma_B^2}
{8\pi M_A^2}.
}
\]

Thus

\[
\boxed{
\mathcal B_{pressure-sort}
\Longrightarrow
\text{fixed recurrent tangential pressure-gradient energy}.
}
\]

## 7. Pressure is formed by the velocity field, not an independent resource

The critical pressure satisfies the exact log-cylinder Poisson equation

\[
-\left(
\partial_q^2-3\partial_q+2+\Delta_{S^2}
\right)P
=
F[A],
\]

with \(F[A]\) quadratic in the leading velocity and its first cylinder derivatives.

M19-059 already shows that, away from the neutral sector, the pressure map is a translation-equivariant elliptic convolution.

M19-135--140 further show that pressure resonances either cancel structurally/parity-wise or create compatible lower-order polyhomogeneous corrections unless an independent log-free theorem is supplied.

Therefore the pressure-gradient floor is a real formed constraint but not an independent finite payer.

It must be supported by the same recurrent velocity geometry.

## 8. Relation to historical M5-245

M5-245 obtained

\[
\Gamma_K+Gamma_P
=
\nu
\left\langle
\|\Phi_q\|_2^2
+
\|\nabla_S\Phi\|_2^2
\right\rangle
\]

on the stronger local energy-transverse branch where the residual correlation vanishes.

M19-423--425 provide the corrected generalization:

\[
\boxed{
\mathcal H_A
=
\langle\Gamma_K\rangle
+
\langle\Gamma_P\rangle
+
\mathscr E'(0).
}
\]

Thus the historical kinetic/pressure fork is recovered exactly when

\[
\mathscr E'(0)=0,
\]

while on the general residual-active branch the first parabolic jet is the third term that must not be omitted.

## 9. Both Bernoulli subbranches remain physically critical

The kinetic branch produces a normalized radial strain coefficient of order one.

In physical variables,

\[
S_{rr}(v)
=
r^{-2}\Sigma_{rr},
\]

which is exactly the critical strain scaling.

The pressure branch produces a normalized angular pressure gradient of order one.

In physical variables,

\[
\nabla p
=
O(r^{-3}),
\]

again the critical pressure-gradient scaling.

Neither branch supplies a better physical power merely from the positive invariant floor.

Therefore

\[
\boxed{
\text{Bernoulli sorting}
\not\Rightarrow
\text{noncritical accumulation}.
}
\]

## 10. Radial-route verdict

Combining M19-423--425,

\[
BRC
\]

has now been completely routed into

\[
\boxed{
\mathcal B_{res}^{finite-depth}
\lor
S_{rr}^{critical}
\lor
P_{tan}^{critical}.
}
\]

Here

- \(\mathcal B_{res}\) is the already audited M19-269 residual-slope branch;
- \(S_{rr}^{critical}\) is a recurrent radial-strain floor;
- \(P_{tan}^{critical}\) is a recurrent tangential pressure-gradient floor.

No new noncritical resource has appeared.

Thus the radial/poloidal branch should no longer be prioritized for another unsigned payer calculation.

## 11. Updated current frontier

The M19-421--422 frontier

\[
R3
\lor
BRC
\lor
T_{\ge2}
\]

is now more accurately written as

\[
\boxed{
R3^{syndetic,critical}
\lor
S_{rr}^{critical}
\lor
P_{tan}^{critical}
\lor
\mathcal B_{res}^{finite-depth}
\lor
T_{\ge2}^{syndetic}.
}
\]

The first four are already known to remain critical/transport-compatible under present budgets.

Therefore the highest-value unresolved formed channel is now

\[
\boxed{
T_{\ge2}^{syndetic},
}
\]

the higher-toroidal leading critical structure.

The next calculation should classify whether a syndetic toroidal \(l\ge2\) component necessarily generates higher residual harmonics/nonlinear spectral cascade, analogous to the pure \(l=1\to l=3\) leakage of M19-419.

\[
\boxed{\text{M19-425 COMPLETE; THE RADIAL BERNOULLI ROUTE IS REDUCED TO EXISTING CRITICAL STRAIN/PRESSURE/RESIDUAL CHANNELS.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
