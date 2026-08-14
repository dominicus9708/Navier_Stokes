# Gaussian mean-vorticity kinetic-energy duality

Date: 2026-08-14

Status: **DERIVED. AN ORDER-ONE GAUSSIAN MEAN VORTICITY AT RADIUS `R` FORCES NORMALIZED KINETIC ENERGY OF ORDER `R^5`. THIS GIVES AN INSTANTANEOUS `W^(1/10)` CEILING, INDEPENDENT OF SPACETIME DISSIPATION PACKING. GLOBAL REGULARITY NOT PROVED.**

## 1. Setup

Let `U` be a divergence-free velocity field on `R^3` with

\[
\Omega=\nabla\times U,
\qquad
U\in L^2(\mathbb R^3).
\]

Let

\[
\gamma_R(x-a)
=R^{-3}\gamma_1((x-a)/R)
\]

be a normalized isotropic Gaussian of radius `R`, and define the Gaussian mean vorticity

\[
\bar\Omega_R(a)
=\int_{\mathbb R^3}\gamma_R(x-a)\Omega(x)\,dx.
\]

The same result holds up to condition-number constants for bounded-condition anisotropic Gaussians.

## 2. Curl duality

For any unit vector `e`, integration by parts gives

\[
\begin{aligned}
e\cdot\bar\Omega_R(a)
&=\int\gamma_R\,e\cdot(\nabla\times U)\,dx\\
&=\int U\cdot\nabla\times(\gamma_Re)\,dx\\
&=\int U\cdot(\nabla\gamma_R\times e)\,dx.
\end{aligned}
\]

Hence

\[
|e\cdot\bar\Omega_R(a)|
\le
\|U\|_2\,\|\nabla\gamma_R\|_2.
\]

Choosing `e` parallel to `bar Omega_R`,

\[
\boxed{
|\bar\Omega_R(a)|
\le
\|U\|_2\,\|\nabla\gamma_R\|_2.
}
\]

## 3. Exact radius scaling of the Gaussian derivative

Because

\[
\gamma_R(x)=R^{-3}\gamma_1(x/R),
\]

we have

\[
\nabla\gamma_R(x)=R^{-4}(\nabla\gamma_1)(x/R).
\]

Therefore

\[
\|\nabla\gamma_R\|_2^2
=R^{-8}R^3\|\nabla\gamma_1\|_2^2
=c_\gamma R^{-5}.
\]

Thus

\[
\boxed{
\|\nabla\gamma_R\|_2
=c_\gamma^{1/2}R^{-5/2}.
}
\]

Substituting into the curl duality estimate yields

\[
\boxed{
\|U\|_2^2
\ge
c\,R^5|\bar\Omega_R(a)|^2.
}
\]

This is an instantaneous `H^{-1}`-type lower bound for a coherent Gaussian vorticity mean.

## 4. Bounded-condition anisotropic form

Let `gamma_Sigma` have covariance `Sigma` with condition number bounded by `K`, and define

\[
R=(\det\Sigma)^{1/6}.
\]

Then scaling through `x=a+Sigma^(1/2)z` gives

\[
\|\nabla\gamma_\Sigma\|_2
\lesssim_K R^{-5/2}.
\]

Hence

\[
\boxed{
\|U\|_2^2
\gtrsim_K
R^5|\bar\Omega_\Sigma(a)|^2.
}
\]

No local regularity, pointwise vorticity control, Hermite truncation, or pressure estimate is used.

## 5. Terminal-normalized energy ceiling

Under terminal first-hitting normalization,

\[
E_U:=\|U\|_2^2
=W^{1/2}\|u\|_2^2.
\]

The physical kinetic energy is non-increasing, so

\[
E_U\le W^{1/2}E_{u,0}
\]

with `E_{u,0}` fixed by the initial data.

If a Gaussian window carries order-one mean vorticity,

\[
|\bar\Omega_R|\ge c_0>0,
\]

then

\[
R^5\lesssim_{K,c_0}W^{1/2}E_{u,0}.
\]

Therefore

\[
\boxed{
R\lesssim_{K,c_0,E_{u,0}}W^{1/10}.
}
\]

This recovers the `W^(1/10)` ceiling directly from instantaneous kinetic energy.

## 6. Combination with the residual mean-creation speed

On the bounded-affine residual branch, the co-affine Gaussian mean `Z` satisfies

\[
|Z'|\lesssim_K B\le C_Km,
\]

while `|Z(0)|=1`. Hence for backward time

\[
0\le\tau\le c_Km^{-1},
\]

we have

\[
|\bar\Omega(-\tau)|\ge c_K>0.
\]

The matched Gaussian covariance has radius

\[
R(\tau)\asymp_K\sqrt\tau.
\]

Evaluate the instantaneous duality at

\[
\tau=c_Km^{-1}.
\]

Then

\[
R_m\asymp_Km^{-1/2}
\]

and

\[
E_U
\gtrsim_K
R_m^5
\asymp_K
m^{-5/2}.
\]

Since `E_U <= C W^(1/2)`,

\[
m^{-5/2}\lesssim_KW^{1/2},
\]

or

\[
\boxed{
m\gtrsim_KW^{-1/5}.}
\]

Writing

\[
m=W^{-1/3}\Lambda,
\]

we obtain the instantaneous survival threshold

\[
\boxed{
\Lambda\gtrsim_KW^{2/15}.
}
\]

This does not use disjoint-step summability. It is forced within each individual bounded-affine terminal-mean creation episode.

## 7. Relation to the stronger repeated-step dissipation threshold

The mean-vorticity occupancy dissipation argument gives, for a disjoint infinite first-hitting sequence,

\[
D_{\rm phys}^{\rm mean}
\gtrsim W^{1/3}\Lambda^{-5/2}.
\]

Finite total dissipation then strengthens the instantaneous lower bound to the asymptotic survival requirement

\[
\boxed{
\Lambda/W^{2/15}\to\infty.
}
\]

Thus the two arguments have distinct logical roles:

- instantaneous kinetic-energy duality excludes `Lambda << W^(2/15)` even on a single step;
- repeated-step dissipation excludes constant-multiple saturation `Lambda ~ C W^(2/15)` on an infinite disjoint cascade.

## 8. Critical exponent coincidence

At the crossover,

\[
\Lambda\sim W^{2/15},
\]

we have

\[
m\sim W^{-1/5},
\qquad
R_m=m^{-1/2}\sim W^{1/10}.
\]

Thus the three exponents

\[
\boxed{
\Lambda:W^{2/15},
\qquad
m:W^{-1/5},
\qquad
R:W^{1/10}
}
\]

are the same kinetic-energy/mean-creation threshold expressed in three normalizations.

Status: **INSTANTANEOUS `W^(1/10)` MEAN-VORTICITY CORE CEILING PROVED BY CURL DUALITY / THE `2/15` SURVIVAL THRESHOLD IS INDEPENDENTLY CONFIRMED / REMAINING SURVIVOR LIES STRICTLY BELOW THE `W^(1/10)` MEAN-CREATION SCALE / GLOBAL REGULARITY NOT PROVED.**
