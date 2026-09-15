# M19-321 — Local carrier plus three-level saturation forces a uniform spectral-variance gap and excludes asymptotically monochromatic record packets

**Date:** 2026-09-16  
**Status:** NEW UNCERTAINTY / SPECTRAL-VARIANCE THEOREM / QUANTITATIVE NON-MONOCHROMATICITY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Inputs

M19-318 gives fixed local spacetime enstrophy in a bounded cylinder: there exist a fixed ball `B_L`, fixed normalized time interval `I_0`, and `c_loc>0` such that

\[
\boxed{
\int_{I_0}\int_{B_L}|\Omega_m(y,s)|^2dyds
\ge c_{loc}>0
}
\]

for all sufficiently late retained second-generation records.

M19-319 gives

\[
0<c_0\le q_{0,m}\le C_0,
\]

\[
0<c_1\le q_{1,m}\le C_1,
\]

\[
0<c_2\le q_{2,m}\le C_2,
\]

on one fixed interval `I` containing `I_0`, where

\[
q_{0,m}=\int_I\|\Omega_m\|_2^2ds,
\quad
q_{1,m}=\int_I\|\nabla\Omega_m\|_2^2ds,
\quad
q_{2,m}=\int_I\|\Delta\Omega_m\|_2^2ds.
\]

## 2. Spectral center and variance

Let

\[
d\mu_m(\xi,s)
:=
|\widehat{\Omega_m}(\xi,s)|^2d\xi ds.
\]

Define the mean squared frequency

\[
\boxed{
\lambda_m
:=
\frac{q_{1,m}}{q_{0,m}}.
}
\]

Then

\[
\frac{c_1}{C_0}
\le
\lambda_m
\le
\frac{C_1}{c_0}.
\]

Thus there are fixed constants

\[
0<\lambda_-\le\lambda_m\le\lambda_+<\infty.
\]

Define the unnormalized spectral variance

\[
\boxed{
\mathcal V_m
:=
\int
\left(|\xi|^2-\lambda_m\right)^2d\mu_m.
}
\]

Expanding gives

\[
\boxed{
\mathcal V_m
=
q_{2,m}
-
\frac{q_{1,m}^2}{q_{0,m}}.
}
\]

The usual log-convexity inequality only says `V_m >= 0`. We prove a uniform strict gap.

## 3. Thin spectral shell

Fix `0<delta<lambda_-/2` and define

\[
\boxed{
S_{m,\delta}
:=
\left\{
\xi:
\left||\xi|^2-\lambda_m\right|\le\delta
\right\}.
}
\]

Because `lambda_m` stays in one compact positive interval, the Euclidean volume of this shell satisfies uniformly

\[
\boxed{|S_{m,\delta}|\le C_{shell}\delta.}
\]

Indeed the radial thickness is `O(delta)` and the central radius remains bounded above and away from zero.

## 4. A thin frequency shell cannot concentrate order-one L2 mass in a fixed ball

Let `P_{m,delta}` be the Fourier projection to `S_{m,delta}`.

The operator

\[
1_{B_L}P_{m,\delta}:L^2(\mathbb R^3)\to L^2(\mathbb R^3)
\]

has Hilbert--Schmidt norm

\[
\|1_{B_L}P_{m,\delta}\|_{HS}^2
=
C_F|B_L||S_{m,\delta}|,
\]

where `C_F` depends only on the Fourier normalization.

Hence

\[
\boxed{
\|1_{B_L}P_{m,\delta}\|_{2\to2}^2
\le
C_B\delta
}
\]

uniformly in `m`.

Therefore, integrating over time,

\[
\int_I
\|1_{B_L}P_{m,\delta}\Omega_m(s)\|_2^2ds
\le
C_B\delta q_{0,m}
\le
C_BC_0\delta.
\]

## 5. Spectral variance controls the complement of the shell

On `S_{m,delta}^c`,

\[
\left(|\xi|^2-\lambda_m\right)^2>\delta^2.
\]

Thus Chebyshev gives

\[
\boxed{
\int_I
\|(I-P_{m,\delta})\Omega_m(s)\|_2^2ds
\le
\frac{\mathcal V_m}{\delta^2}.
}
\]

## 6. Local carrier forces a uniform variance gap

Decompose

\[
\Omega_m
=P_{m,\delta}\Omega_m
+(I-P_{m,\delta})\Omega_m.
\]

Using `|a+b|^2 <= 2|a|^2+2|b|^2`,

\[
\begin{aligned}
 c_{loc}
&\le
\int_{I_0}\int_{B_L}|\Omega_m|^2\\
&\le
2C_BC_0\delta
+
2\frac{\mathcal V_m}{\delta^2}.
\end{aligned}
\]

Choose one fixed `delta_*` satisfying

\[
2C_BC_0\delta_*
\le
\frac{c_{loc}}2.
\]

Then

\[
\frac{c_{loc}}2
\le
2\frac{\mathcal V_m}{\delta_*^2},
\]

so

\[
\boxed{
\mathcal V_m
\ge
\frac{c_{loc}\delta_*^2}{4}
=:c_{var}>0.
}
\]

Therefore

\[
\boxed{
q_{2,m}
-
\frac{q_{1,m}^2}{q_{0,m}}
\ge c_{var}>0.
}
\]

Equivalently,

\[
\boxed{
q_{0,m}q_{2,m}-q_{1,m}^2
\ge
c_0c_{var}>0.
}
\]

## 7. Interpretation

Equality in the basic moment inequality

\[
q_1^2\le q_0q_2
\]

would require the spacetime spectral measure to be supported on one frequency sphere

\[
|\xi|^2=\lambda.
\]

M19-321 proves more: the canonical record sequence cannot even approach such a monochromatic shell state.

The fixed local physical carrier and the uncertainty principle enforce a quantitative radial spectral width.

Thus the packet is not only own-scale; it is genuinely multi-frequency at order-one normalized scales.

## 8. Relation to M19-320

M19-320 proves a fixed annulus

\[
a\le|\xi|\le b
\]

carries positive charge.

M19-321 strengthens this by ruling out concentration into arbitrarily thin spherical layers inside that annulus.

Therefore the surviving spectral population has both

- bounded nonzero central frequency;
- bounded-below radial spectral variance.

## 9. Physical first-ancient scaling

Under the inverse record scaling, the spectral center obeys

\[
|\eta|^2
\sim
R_m^{-2}\lambda_m,
\]

while the spectral width in `|eta|^2` is of order

\[
R_m^{-2}.
\]

Thus both the central frequency and its nontrivial spread remain tied to the Type-I scale `R_m^{-1}`.

The carrier does not collapse into a single asymptotic Helmholtz frequency after blow-down.

## 10. Conditional CE-H relevance

On an exact CE-H region one has

\[
\Delta\Omega=\kappa\Omega.
\]

If the record-cell CE-H representation is global enough that the `q_0,q_1,q_2` integrals are taken on the same exact field without derivative-tail/interface loss, then

\[
q_1
=-\int\kappa|\Omega|^2,
\]

and

\[
q_2
=\int\kappa^2|\Omega|^2.
\]

In that case the spectral variance is exactly the enstrophy-weighted variance of `kappa`.

This conditional consequence is developed separately because global CE-H representation/tightness is itself a nontrivial gate.

## 11. Firewall

The variance gap does not exclude additional low/high frequency tails.

It also does not by itself identify a finite parent budget or a monotone signed observable.

Therefore

\[
\boxed{
\text{spectral variance gap}
\not\Rightarrow
\text{global regularity contradiction}.
}
\]

## 12. Next target

On the exact CE-H compact lane, convert the spectral variance floor into a quantitative `kappa`-variance floor.

Then split that variance into

- bounded-core spatial coefficient variation, hence `grad kappa`/transition cost;
- recurrent temporal/phase coefficient variation;
- derivative-tail/interface loss.

This would connect the newly certified interior uncertainty directly to the M18-062--069 coefficient/strain segregation architecture.

---

\[
\boxed{\text{M19-321 COMPLETE; THE CANONICAL RECORD PACKET HAS A UNIFORM POSITIVE RADIAL SPECTRAL VARIANCE.}}
\]