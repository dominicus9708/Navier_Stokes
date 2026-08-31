# DSD M5-363 — Saturated Affine Shield = Seregin `alpha=3/2` Boundary

Date: 2026-08-31

Status: **THE ENERGY-SATURATED AFFINE/DUAL-HYPERBOLIC SHIELD LIES EXACTLY AT THE `alpha=3/2` BORDERLINE OF SEREGIN'S 2026 TYPE-II EULER-ZOOM SCHEME / THE `alpha>3/2` EXCLUSION DOES NOT APPLY AT THIS BORDERLINE / THE REMAINING OBJECT IS AN ANCIENT EULER ENDPOINT WITH NONTRIVIAL NS ANCESTRY / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The previous audits derived the sharp finite-energy affine-shield scales

\[
 d\asymp r^{4/5},
 \qquad
 a:=T_*-t\asymp \Theta r^2,
\]

where

- `r` is the natural vorticity length;
- `d` is the physical energy-shield radius;
- `Theta=a/r^2` is the local vorticity clock.

Seregin's Type-II rescaling uses an outer spatial scale `lambda` and a time-compression function `f(lambda)` through

\[
 x=\lambda y,
 \qquad
 t=\lambda^2 f(\lambda)\tau,
\]

and

\[
 v^\lambda(y,\tau)
 =\lambda f(\lambda)v(\lambda y,\lambda^2f(\lambda)\tau).
\]

This note matches the two scalings exactly.

## 2. Identify the Seregin clock

Set

\[
 \lambda=d\asymp r^{4/5}.
\]

To make the rescaled time window equal to the physical remaining time `a`, one must choose

\[
 \lambda^2 f(\lambda)=a.
\]

Hence

\[
 \boxed{
 f(d)=\frac{a}{d^2}
 \asymp
 \Theta r^{2/5}.
 }
\]

Since

\[
 d^{1/2}=r^{2/5},
\]

we obtain

\[
 \boxed{
 f(d)\asymp \Theta d^{1/2}.
 }
\]

In the critical-clock corridor

\[
 0<c_-\le\Theta\le c_+<\infty,
\]

this is exactly

\[
 \boxed{f(d)\asymp d^{1/2}.}
\]

## 3. Power notation

Seregin's power family is

\[
 f(\lambda)\sim \lambda^{\alpha-1}
\]

(up to optional logarithmic corrections).

Therefore

\[
 \alpha-1=\frac12,
\]

so

\[
 \boxed{\alpha=\frac32.}
\]

Thus the exponent `1/5` obtained from the finite-energy affine barrier is exactly equivalent, in Seregin's variables, to the Type-II borderline `alpha=3/2`.

## 4. Why the published `alpha>3/2` exclusion does not close this case

Seregin's 2026 Euler-limit argument rules out the relevant power scenario in the range

\[
 \alpha>\frac32
\]

because the limiting Euler profile is forced to vanish by the weighted energy structure in that regime.

The saturated affine shield is not in that range.

It lies at

\[
 \boxed{\alpha=\frac32.}
\]

Hence one must not cite the `alpha>3/2` theorem as excluding the saturated shield.

The borderline must be analyzed separately.

## 5. Affine field under the Euler zoom

Inside the affine shield, write schematically

\[
 u(x,t)\approx M(t)(x-X(t)),
 \qquad
 |M(t)|\asymp r^{-2}.
\]

The rescaled gradient is

\[
 \nabla_y v^\lambda
 =\lambda^2f(\lambda)\nabla_xu.
\]

Using

\[
 \lambda^2f=a=\Theta r^2,
\]

we get

\[
 \boxed{
 |\nabla_yv^\lambda|
 \asymp \Theta.
 }
\]

Likewise the rescaled vorticity is

\[
 \omega^\lambda
 =\lambda^2f(\lambda)\omega,
\]

so

\[
 \boxed{|\omega^\lambda|\asymp\Theta.}
\]

Thus the affine/dual-hyperbolic structure does not disappear under the borderline Euler zoom.

## 6. Velocity amplitude

At the shield radius

\[
 |u|\asymp r^{-2}d\asymp r^{-6/5}.
\]

The rescaled velocity amplitude is

\[
 \lambda f\,|u|
 \asymp
 r^{4/5}\,\Theta r^{2/5}\,r^{-6/5}
 \asymp\Theta.
\]

Hence

\[
 \boxed{|v^\lambda|\asymp\Theta}
\]

on an order-one rescaled region.

## 7. Circulation inheritance

Circulation transforms according to

\[
 \Gamma^\lambda
 =f(\lambda)\Gamma.
\]

The affine shield circulation obeys

\[
 \Gamma\asymp |\omega|d^2
 \asymp
 r^{-2}r^{8/5}
 =r^{-2/5}.
\]

Therefore

\[
 \boxed{
 \Gamma^\lambda
 \asymp
 \Theta r^{2/5}r^{-2/5}
 \asymp\Theta.
 }
\]

Thus a critical-clock Euler limit inherits nonzero order-one circulation.

## 8. Energy scaling

The rescaled kinetic energy on the order-one shield region satisfies

\[
 \int|v^\lambda|^2dy
 =
 \frac{f(\lambda)^2}{\lambda}
 \int_{B_\lambda}|u|^2dx.
\]

For a saturated shield

\[
 \int_{B_d}|u|^2dx\asymp1,
\]

and

\[
 \frac{f(d)^2}{d}
 \asymp
 \frac{\Theta^2r^{4/5}}{r^{4/5}}
 =\Theta^2.
\]

Hence

\[
 \boxed{
 \int_{B_1}|v^\lambda|^2dy\asymp\Theta^2.
 }
\]

The borderline Euler limit therefore retains nonzero finite local energy.

## 9. Seregin mixed nontriviality quantity

For the truncated mixed quantity used in the Type-II criterion, the previous scaling calculation gives

\[
 \overline M_\kappa^{s,l}(u,d)
 \asymp
 \Theta r^{-\frac25(l-1)}.
\]

With

\[
 g(d)=f(d)^{l-1}
 \asymp
 \Theta^{l-1}r^{\frac25(l-1)},
\]

we obtain the exact cancellation

\[
 \boxed{
 g(d)\overline M_\kappa^{s,l}(u,d)
 \asymp
 \Theta^l.
 }
\]

Thus in the critical-clock regime the nontriviality quantity is order one rather than tending to zero.

## 10. Weighted `A/E/D` scaling

The affine shield's own last-stage contributions are compatible with the borderline weighted quantities:

\[
 A_f=O(\Theta^2),
 \qquad
 E_f=O(\Theta^2),
 \qquad
 D_f=O(\Theta^3)
\]

at the level of the shield contribution.

This is a compatibility calculation, **not** a proof of Seregin's full global upper-bound hypothesis for the parent solution.

One must not promote the lower/local scaling computation into the theorem assumption.

## 11. Borderline endpoint

The correct reduction is therefore

\[
 \boxed{
 \text{saturated critical-clock affine shield}
 \Longrightarrow
 \text{`alpha=3/2' ancient Euler endpoint candidate}.
 }
\]

At this endpoint the rescaled object retains, on an order-one region,

\[
 \boxed{
 \text{nonzero energy}
 +
 \text{nonzero vorticity}
 +
 \text{nonzero circulation}
 +
 \text{order-one velocity gradient}.
 }
\]

## 12. Firewall: no generic Euler Liouville theorem

The appearance of an ancient finite-energy Euler endpoint is not itself a contradiction.

Nontrivial smooth finite-energy/compactly supported steady Euler flows exist in three dimensions, so one cannot use a generic statement of the form

\[
 \text{finite-energy ancient Euler}\Rightarrow0.
\]

Any closure must exploit the specific Navier--Stokes ancestry and first-hitting/affine structure inherited at `alpha=3/2`.

## 13. Formation-axiom interpretation

The `1/5` finite-energy shield law and the `alpha=3/2` Euler boundary are the same structural threshold described in two coordinate systems:

\[
 \boxed{
 d\sim r^{4/5}
 \quad\Longleftrightarrow\quad
 f(d)\sim d^{1/2}.
 }
\]

This identifies the correct endpoint object instead of treating `Type-II` as one undifferentiated branch.

## 14. Next target

The next audit should determine which Navier--Stokes ancestry survives strongly enough in this Euler limit.

The high-value inherited candidates are

- order-one first-hitting vorticity;
- order-one affine strain on a unit region;
- order-one circulation;
- the dual-hyperbolic eigenstructure;
- record-growth/nonstationarity information;
- material/flux genealogy constraints.

If these imply a forbidden local/asymptotically self-similar Euler blow-up structure, the borderline shield may be closed without pricing every H/T event separately.

## 15. Audit verdict

### DERIVED

- saturated affine shield maps exactly to `alpha=3/2`;
- vorticity, strain, velocity, energy and circulation remain order one under the corresponding Euler zoom;
- Seregin's mixed nontriviality quantity remains order one.

### FIREWALL

- the `alpha>3/2` Seregin exclusion does not cover the borderline;
- local shield scaling does not prove the global weighted theorem hypotheses;
- finite-energy ancient Euler is not generically trivial.

### OPEN

- inherited Euler endpoint rigidity at `alpha=3/2`;
- transfer of first-hitting and circulation genealogy into that endpoint;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
