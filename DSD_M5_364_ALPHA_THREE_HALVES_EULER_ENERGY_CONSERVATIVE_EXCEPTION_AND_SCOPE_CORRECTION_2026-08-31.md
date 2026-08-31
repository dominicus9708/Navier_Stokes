# DSD M5-364 — `alpha=3/2` Euler Energy-Conservative Exception and Scope Correction

Date: 2026-08-31

Status: **SCOPE CORRECTION / THE `alpha=3/2`, `L^2` EULER SELF-SIMILAR ENDPOINT IS NOT GENERICALLY EXCLUDED BY THE CHAE--SHVYDKOY `L^p` THEOREM / IT IS THE ENERGY-CONSERVATIVE EXCEPTIONAL SCALING AND REQUIRES ADDITIONAL PROFILE INFORMATION / GLOBAL REGULARITY UNPROVED.**

## 1. Correction of the previous shortcut

M5-363 identified the saturated affine shield with Seregin's Euler scaling exponent

\[
 \alpha=\frac32.
\]

A tempting shortcut is to combine this with the Chae--Shvydkoy locally self-similar Euler nonexistence results and assert that finite-energy (`L^2`) profiles at `alpha=3/2` are automatically trivial.

That shortcut is too strong.

The detailed theorem structure in Chae--Shvydkoy distinguishes the energy-conservative scaling

\[
 \boxed{\alpha=\frac N2}
\]

from the generic `L^p` cases.

## 2. Generic `L^p` exclusion range

For a locally self-similar Euler profile `v`, the paper proves the velocity `L^p` exclusion

\[
 v\in L^p,
 \qquad p\ge3,
\]

under, among other ranges,

\[
 -1<\alpha\le \frac Np.
\]

Thus in three dimensions the direct critical case emphasized by this theorem is, for example,

\[
 p=3,
 \qquad
 \alpha\le1.
\]

It does **not** give a generic `p=2`, `alpha=3/2` Liouville theorem.

## 3. The exceptional energy-conservative scaling

For a self-similar Euler ansatz

\[
 u(x,t)
 =
 (T-t)^{-\frac{\alpha}{1+\alpha}}
 v\!\left(\frac{x-x_*}{(T-t)^{\frac1{1+\alpha}}}\right),
\]

the kinetic-energy scaling factor is

\[
 (T-t)^{\frac{N-2\alpha}{1+\alpha}}.
\]

Therefore

\[
 \boxed{\alpha=\frac N2}
\]

is exactly the scaling for which global `L^2` energy is invariant.

For `N=3`, this is

\[
 \boxed{\alpha=\frac32.}
\]

Hence ordinary finite-energy conservation cannot rule out this scaling by dimensional contradiction.

## 4. What Chae--Shvydkoy prove at `alpha=N/2`

At the energy-conservative exponent the paper obtains exclusion under additional profile assumptions.

One explicit result assumes

\[
 v\in L^2
\]

and two-sided asymptotic power bounds at spatial infinity of the schematic form

\[
 c|y|^{-N-1+\delta}
 \lesssim
 |v(y)|
 \lesssim
 C|y|^{1-\delta}
\]

for some `delta>0` and large `|y|`.

Under such extra structure the profile is trivial.

This is not a generic theorem for arbitrary finite-energy `L^2` profiles.

## 5. Consequence for the Seregin borderline endpoint

Seregin's theorem at the power law

\[
 f(\lambda)=\lambda^{\alpha-1}
\]

gives

\[
 F(a)=a^{\alpha-1}.
\]

At

\[
 \alpha=\frac32,
\]

we have

\[
 F(a)=a^{1/2}
\]

and therefore

\[
 \frac{F(a)^2}{a}=1.
\]

The limiting ancient Euler solution satisfies the uniform local/global-energy-type bound

\[
 \boxed{
 \sup_{a>0}
 \sup_{-a^2<\tau<0}
 \int_{B(a)}|u(y,\tau)|^2dy
 \le C.
 }
\]

For every fixed `tau<0`, letting `a` grow beyond `sqrt(-tau)` and then to infinity gives

\[
 \boxed{
 \|u(\tau)\|_{L^2(\mathbb R^3)}^2\le C.
 }
\]

Thus the `alpha=3/2` Seregin endpoint is naturally a uniformly finite-energy ancient Euler object.

This does **not** make it trivial.

## 6. Correct evolving affine-shield scaling

A second scope correction concerns the local affine anti-model.

At a fixed reference stage it is possible to write the affine gradient as

\[
 |M(t)|\sim (T-t)^{-1}.
\]

However the finite-energy shield radius evolves simultaneously:

\[
 d(t)
 \sim
 r(t)^{4/5}
 \sim
 (T-t)^{2/5}
\]

in the critical vorticity clock.

Therefore the actual affine-shield velocity amplitude is

\[
 |u|
 \sim
 |M|d
 \sim
 (T-t)^{-1}(T-t)^{2/5}
 =
 (T-t)^{-3/5}.
\]

The spatial focusing exponent is

\[
 (T-t)^{2/5}.
\]

These are exactly

\[
 \frac{\alpha}{1+\alpha}=\frac35,
 \qquad
 \frac1{1+\alpha}=\frac25
\]

for

\[
 \boxed{\alpha=\frac32.}
\]

Thus the affine-shield scaling is consistent with the standard isotropic Euler self-similar exponent once the shrinking shield is included.

## 7. Energy consistency

Inside the evolving shield,

\[
 |u|^2\sim(T-t)^{-6/5},
\]

while the shield volume is

\[
 d(t)^3\sim(T-t)^{6/5}.
\]

Hence

\[
 \boxed{
 \int_{B_{d(t)}}|u|^2dx\sim O(1).
 }
\]

So the finite-energy atom/shield is exactly compatible with the energy-conservative Euler self-similar scaling.

There is no hidden `L^2` contradiction here.

## 8. What would close the endpoint

The Chae--Shvydkoy theory can become relevant if the Seregin Euler endpoint is shown to acquire one of their additional rigidity hypotheses, for example:

1. exact or sufficiently strong local self-similar locking;
2. a profile class covered by their infinity asymptotics;
3. a stronger `L^p`, `p>=3`, property at the relevant scaling;
4. vorticity integrability/strain-decay hypotheses of the alternative profile theorem.

At present none of these follows automatically from finite energy alone.

## 9. Formation-axiom interpretation

The endpoint has now been localized to a precise boundary object:

\[
 \boxed{
 \text{finite-energy, energy-conservative }\alpha=3/2
 \text{ ancient Euler endpoint with NS ancestry}.
 }
\]

This is more informative than the generic label `Type II` but is not itself forbidden.

The next decomposition should distinguish

\[
 \boxed{
 \text{self-similar/shape-locked Euler endpoint}
 \quad\lor\quad
 \text{shape-reforming Euler endpoint}.
 }
\]

The first may be attackable by self-similar Euler rigidity; the second is a genuine dynamic turnover/reformation branch.

## 10. Firewall

Do not assert

\[
 v\in L^2,\ \alpha=3/2
 \Longrightarrow
 v=0
\]

from the generic Chae--Shvydkoy `L^p` theorem.

The energy-conservative scaling is exceptional and must be treated separately.

## 11. Audit verdict

### CORRECTED

- `alpha=3/2`, `p=2` is not generically covered by the standard `p>=3` velocity exclusion;
- the evolving affine shield is exactly the energy-conservative self-similar scaling, not a fixed-radius `1/(T-t)` energy contradiction.

### PROVED/DERIVED

- Seregin's `alpha=3/2` endpoint has uniform global `L^2` energy at each negative Euler time under theorem hypotheses;
- the saturated shield has order-one energy precisely because `d(t)~(T-t)^{2/5}`.

### OPEN

- self-similar locking or asymptotic-profile rigidity of the Euler endpoint;
- shape-reformation cost when locking fails;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
