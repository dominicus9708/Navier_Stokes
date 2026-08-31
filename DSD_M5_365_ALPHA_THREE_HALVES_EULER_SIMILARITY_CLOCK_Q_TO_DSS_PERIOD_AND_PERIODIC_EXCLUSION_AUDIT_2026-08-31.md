# DSD M5-365 — `alpha=3/2` Euler Similarity Clock: Exact `q -> DSS` Period Match and Periodic-Endpoint Rigidity

Date: 2026-08-31

Status: **THE FIRST-HITTING VORTICITY FACTOR `q` MATCHES THE ENERGY-CONSERVING EULER DSS SCALING EXACTLY: `lambda=q^(2/5)` AND SIMILARITY PERIOD `S0=log q` / EXACT PERIODIC OR DSS LOCKING IS ROUTED TO EXISTING EULER RIGIDITY THEOREMS UNDER THEIR STATED GROWTH/TYPE-I HYPOTHESES / CHECKPOINT SPACING ALONE DOES NOT IMPLY DSS / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-363--364 reduced the saturated affine-shield Type-II endpoint to the energy-conserving Euler scaling

\[
 \alpha=\frac32.
\]

The remaining question is whether the Euler endpoint locks to a self-similar/DSS orbit or continues to reform its shape in similarity time.

This note computes the exact relation between the original first-hitting multiplier `q` and the Euler DSS scale/period.

## 2. Energy-conserving Euler similarity variables

Let \(\tau<0\) denote the Euler-limit physical time and define

\[
 s=-\log(-\tau),
 \qquad
 y=\frac{x}{(-\tau)^{2/5}},
\]

\[
 \boxed{
 V(y,s)=(-\tau)^{3/5}u(x,\tau).
 }
\]

Then \(V\) solves

\[
 \boxed{
 V_s+\frac35V+\frac25(y\cdot\nabla)V+(V\cdot\nabla)V+\nabla P=0,
 \qquad \nabla\cdot V=0.
 }
\]

The vorticity profile is

\[
 \Omega_V(y,s)=(-\tau)\omega(x,\tau).
\]

Thus the local Euler Type-I clock is exactly

\[
 \boxed{
 \Theta(\tau)=(-\tau)\|\omega(\tau)\|_\infty
 =\|\Omega_V(s)\|_\infty.
 }
\]

## 3. Euler DSS convention

An `(alpha,lambda)` discretely self-similar Euler solution obeys

\[
 u(x,t)=\lambda^\alpha u(\lambda x,\lambda^{\alpha+1}t)
\]

for one fixed \(\lambda>1\).

For \(\alpha=3/2\),

\[
 \alpha+1=\frac52.
\]

The velocity factor is

\[
 \lambda^{3/2},
\]

the time factor is

\[
 \lambda^{5/2},
\]

and the vorticity factor is also

\[
 \boxed{\lambda^{5/2}.}
\]

## 4. Match the first-hitting vorticity ratio

The first-hitting tower is defined by a fixed vorticity amplification factor

\[
 W_{j+1}=qW_j,
 \qquad q>1.
\]

If an Euler DSS orbit is to realize one first-hitting step as one DSS scale step, its vorticity factor must satisfy

\[
 \lambda^{5/2}=q.
\]

Therefore

\[
 \boxed{
 \lambda=q^{2/5}.
 }
\]

This is the same `2/5` exponent that appeared independently in the physical shield radius

\[
 d(t)\sim(T-t)^{2/5}.
\]

## 5. Similarity-time period

For the Euler similarity variables above, DSS with spatial factor \(\lambda\) is equivalent to periodicity of \(V(y,s)\) with period

\[
 S_0=(\alpha+1)\log\lambda.
\]

Using \(\alpha+1=5/2\) and \(\lambda=q^{2/5}\),

\[
 S_0
 =\frac52\log(q^{2/5})
 =\log q.
\]

Hence

\[
 \boxed{
 S_0=\log q.
 }
\]

This is an exact structural identity.

## 6. Other stage factors match automatically

The DSS spatial-radius ratio over one period is

\[
 \lambda^{-1}=q^{-2/5},
\]

which is exactly the saturated shield-radius ratio

\[
 \frac{d_{j+1}}{d_j}=q^{-2/5}.
\]

The velocity-amplitude factor is

\[
 \lambda^{3/2}
 =(q^{2/5})^{3/2}
 =q^{3/5},
\]

which matches the affine-shield velocity scaling under one vorticity-`q` step.

Thus

\[
 \boxed{
 \begin{aligned}
 \text{vorticity factor}&=q,\\
 \text{spatial factor}&=q^{-2/5},\\
 \text{velocity factor}&=q^{3/5},\\
 \text{similarity-time period}&=\log q.
 \end{aligned}
 }
\]

All four first-hitting/affine exponents coincide with the `alpha=3/2` Euler DSS scaling.

## 7. Critical-clock checkpoint spacing

At checkpoint \(j\), write

\[
 \Theta_j=(-\tau_j)W_j.
\]

Since \(W_{j+1}=qW_j\),

\[
 \frac{-\tau_{j+1}}{-\tau_j}
 =\frac{\Theta_{j+1}}{q\Theta_j}.
\]

Therefore

\[
 s_{j+1}-s_j
 =\log q+\log\frac{\Theta_j}{\Theta_{j+1}}.
\]

If the local clock locks,

\[
 \Theta_{j+1}/\Theta_j\to1,
\]

then

\[
 \boxed{
 s_{j+1}-s_j\to\log q.
 }
\]

This identifies the natural candidate period.

## 8. Firewall: period spacing is not shape periodicity

The conclusion

\[
 s_{j+1}-s_j\to\log q
\]

does **not** imply

\[
 V(\cdot,s+\log q)=V(\cdot,s).
\]

A nonperiodic or aperiodic similarity orbit may cross the same vorticity levels at asymptotically regular time intervals while its full spatial shape continues to change.

Thus the proof tree must retain the distinction

\[
 \boxed{
 \text{clock locking}
 \neq
 \text{DSS shape locking}.
 }
\]

## 9. Exact DSS rigidity: Chae--Wolf 2017

Chae and Wolf, *Energy concentrations and Type I blow-up for the 3D Euler equations* (arXiv:1706.02020; later CMP), prove that an energy-conserving Euler DSS blow-up is excluded under the Euler Type-I velocity-gradient hypothesis

\[
 \sup_{t<0}(-t)\|\nabla u(t)\|_\infty<\infty
\]

in their regularity class.

At \(\alpha=3/2\), an exact periodic similarity profile with

\[
 \sup_{s\in[0,S_0]}\|\nabla V(s)\|_\infty<\infty
\]

automatically gives this physical Type-I bound.

Hence

\[
 \boxed{
 \text{exact `alpha=3/2` DSS}
 +
 \text{bounded profile gradient}
 \Longrightarrow
 V\equiv0.
 }
\]

This contradicts the nontrivial first-hitting vorticity witness.

## 10. Exact DSS rigidity: Chae--Wolf 2023

Chae and Wolf, *On the Discretely Self-similar Solutions to the Euler Equations in R^3*, J. Nonlinear Sci. 33 (2023), 115, prove a complementary result:

for

\[
 \alpha\ge\frac32,
\]

DSS Euler profiles with sublinear growth at spatial infinity are spatial constants.

Therefore at the current exponent

\[
 \boxed{
 \alpha=\frac32,
 }
\]

one also has

\[
 \boxed{
 \text{exact DSS}
 +
 \text{sublinear profile growth}
 \Longrightarrow
 \text{spatial constant profile}.
 }
\]

A finite-energy nontrivial profile cannot be a nonzero spatial constant, so this again yields the zero profile.

## 11. No-H route to the DSS theorems

The external theorems require a bridge from the current Navier--Stokes/Euler extraction to either

1. bounded similarity-profile gradient, or
2. sublinear profile growth.

This bridge is not automatic from `L2` alone.

However, in a periodic profile class, a uniform derivative/continuity bound plus uniform `L2` energy forces decay at infinity: if a fixed-amplitude spike persisted at arbitrarily large radii, uniform continuity would create disjoint balls with a fixed positive `L2` mass, contradicting finite energy.

Thus the expected no-H dichotomy is

\[
 \boxed{
 \text{periodic endpoint}
 \Longrightarrow
 H_{\nabla,\infty}
 \lor
 \text{sublinear/Type-I DSS rigidity}.
 }
\]

The detailed quantitative bridge is left to the next audit.

## 12. Similarity-dynamics formation fork

The energy-conserving Euler endpoint is therefore decomposed as

\[
 \boxed{
 \text{Euler endpoint}
 \Longrightarrow
 E_{\rm DSS}
 \lor
 E_{\rm RDSS}
 \lor
 E_{\rm aperiodic/reforming}.
 }
\]

- `E_DSS`: exact/limit periodic similarity shape;
- `E_RDSS`: periodic modulo a rigid rotation;
- `E_aperiodic/reforming`: genuinely nonperiodic similarity dynamics.

The first branch is strongly constrained by the two Chae--Wolf theorems above.

The rotated branch has separate external rigidity results under isolated-singularity/decay assumptions.

The genuinely aperiodic branch remains the main dynamic endpoint.

## 13. Audit verdict

### EXACTLY DERIVED

\[
 \boxed{\lambda=q^{2/5}},
 \qquad
 \boxed{S_0=\log q}.
\]

The first-hitting velocity, spatial and vorticity factors all match the `alpha=3/2` Euler DSS scaling.

### EXTERNAL THEOREMS

- Chae--Wolf 2017: energy-conserving DSS excluded under Type-I gradient control;
- Chae--Wolf 2023: DSS profiles for `alpha>=3/2` with sublinear growth are spatial constants.

### FIREWALL

- asymptotically equal checkpoint spacing does not imply DSS shape locking;
- `L2` energy alone does not imply the profile-growth hypotheses.

### OPEN

- rigorous no-H bridge from periodic finite-energy profile to bounded-gradient/sublinear growth;
- rotated DSS hypothesis match;
- aperiodic similarity-time endpoint;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
