# M19-313 — Mixed space-time Holder lowers the strong GMS derivative threshold to m>11/6, and physical palinstrophy m=2 already suffices

**Date:** 2026-09-16  
**Status:** ACTIVE GMS ANALYTIC IMPROVEMENT / PALINSTROPHY-LEVEL ENDPOINT / M19-310 ISOTROPIC THRESHOLD SUPERSEDED AS MINIMAL CLAIM

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Correction to the interpretation of M19-310

M19-310 used an isotropic spacetime norm `L^s_{x,t}` and found the sufficient threshold

\[
m>9/4.
\]

That statement remains valid as an isotropic sufficient condition, but it is **not the minimal strong derivative threshold** once the parabolic GMS kernel is treated with mixed space-time Holder.

The present module performs that optimization.

## 2. Mixed norm from energy plus D^m u in L_t^2L_x^2

Assume on a finite physical cylinder

\[
u\in L_t^\infty L_x^2,
\qquad
D^m u\in L_t^2L_x^2.
\]

For a spatial exponent `q`, Gagliardo--Nirenberg gives

\[
\|u(t)\|_{L_x^q}
\lesssim
\|u(t)\|_2^{1-a}
\|D^m u(t)\|_2^a,
\]

with

\[
\frac1q
=
\frac12-rac{am}{3}.
\]

Choose

\[
ap=2
\]

so that the derivative factor is time-integrable. Then

\[
\boxed{
\frac{2m}{p}+rac3q=rac32.
}
\]

Therefore

\[
\boxed{u\in L_t^pL_x^q}
\]

for every admissible pair on this interpolation line.

## 3. The weighted velocity term in mixed form

Let

\[
K(x,t)=\rho(x,t)^{-5/3},
\qquad
\rho=\max\{|x|,\sqrt\tau\},
\quad
\tau=t_0-t.
\]

At each time, apply spatial Holder to

\[
|u|^{10/3}K.
\]

We need

\[
q>10/3.
\]

Set

\[
B:=\frac{3q}{3q-10}.
\]

Then

\[
\int |u|^{10/3}Kdx
\le
\|u(t)\|_q^{10/3}
\|K(t)\|_{L_x^B}.
\]

## 4. Spatial kernel becomes uniformly integrable once q>15/2

For fixed `tau`,

\[
\|K(t)\|_{L_x^B}^B
\asymp
\int_0^R
\max\{r,\sqrt\tau\}^{-5B/3}r^2dr.
\]

This remains uniformly bounded as `tau->0` whenever

\[
\frac{5B}{3}<3,
\]

i.e.

\[
B<9/5.
\]

Using

\[
B=\frac{3q}{3q-10},
\]

this is equivalent to

\[
\boxed{q>15/2.}
\]

Thus for any `q>15/2`, the parabolic kernel has no remaining time singularity after the spatial Holder step.

## 5. Time integrability condition

On a finite time interval,

\[
\|u(t)\|_q^{10/3}
\]

is integrable whenever

\[
\boxed{p>10/3.}
\]

Therefore a sufficient mixed-norm condition is

\[
\boxed{
p>10/3,
\qquad
q>15/2,
\qquad
\frac{2m}{p}+rac3q=rac32.
}
\]

## 6. Optimize the derivative order

From the interpolation relation,

\[
m
=
\frac p2
\left(
\frac32-rac3q
\right).
\]

Let

\[
p\downarrow10/3,
\qquad
q\downarrow15/2
\]

from above. Then

\[
\frac32-rac3q
\to
\frac32-rac25
=
\frac{11}{10}.
\]

Hence

\[
m
\to
\frac{5}{3}\cdot\frac{11}{10}
=
\frac{11}{6}.
\]

Therefore for every

\[
\boxed{m>11/6}
\]

one may choose admissible `p,q` satisfying all strict inequalities.

Thus

\[
\boxed{
D^m u\in L_t^2L_x^2,
\quad m>11/6
\Longrightarrow
\text{velocity part of }\mathcal P_{GMS}^{log}\text{ is finite}.
}
\]

## 7. Pressure obeys the same mixed threshold

At each time, canonical pressure satisfies

\[
\|p(t)\|_{L_x^{q/2}}
\lesssim
\|u(t)\|_{L_x^q}^2
\]

by Riesz-transform boundedness.

Then

\[
|p|^{5/3}
\]

has the same spatial Holder exponent as `|u|^{10/3}` because

\[
\frac{q/2}{5/3}
=
\frac{3q}{10}.
\]

Also

\[
\|p(t)\|_{q/2}^{5/3}
\lesssim
\|u(t)\|_q^{10/3}.
\]

Therefore exactly the same `p>10/3`, `q>15/2` conditions close the pressure contribution.

Hence

\[
\boxed{
D^m u\in L_t^2L_x^2,
\quad m>11/6
\Longrightarrow
\mathcal P_{GMS}^{log}(V)<\infty.
}
\]

The fixed Galilean constant contributes only a locally integrable bounded term.

## 8. Concrete palinstrophy-level choice m=2

Set

\[
m=2.
\]

Choose

\[
\boxed{p=32/9,
\qquad q=8.}
\]

Indeed,

\[
\frac4p+rac3q
=
\frac98+rac38
=
\frac32.
\]

Moreover

\[
p=32/9>10/3,
\qquad
q=8>15/2.
\]

Therefore

\[
\boxed{
D^2u\in L_t^2L_x^2
\Longrightarrow
u\in L_t^{32/9}L_x^8
\Longrightarrow
\mathcal P_{GMS}^{log}(V)<\infty.
}
\]

For divergence-free whole-space velocity,

\[
\|D^2u\|_2
\simeq
\|\nabla\omega\|_2.
\]

Thus **physical spacetime palinstrophy is already sufficient for the analytic GMS contradiction.**

## 9. Major consequence for the transfer gate

The analytic endpoint no longer requires the M17-404 raw-H2 / velocity-H3 resource.

The lower derivative M17-307 palinstrophy resource is sufficient **if it can be transferred to the original physical singular neighborhood without critical base-scale loss**.

Therefore the primary GMS transfer target should be lowered from

\[
\mathcal T_{GMS}^{raw-H2/base-gain}
\]

to

\[
\boxed{
\mathcal T_{GMS}^{pal/base-gain}:
\text{obtain physical }D^2u\in L_t^2L_x^2
\text{ near the candidate singular point from the ancestral palinstrophy structure.}
}
\]

## 10. Scaling firewall remains

This is a major analytic reduction but does not itself solve physical transfer.

Palinstrophy has physical spacetime scaling

\[
\int|D^2u|^2dxdt
\sim
r^{-1}.
\]

The M5-477 ancient palinstrophy tail obeys the critical Type-I rate

\[
\int_{-\infty}^{-T}\|D^2V\|_2^2d\tau
\lesssim T^{-1/2}.
\]

Restoring the physical base gives

\[
r_j^{-1}T^{-1/2}
=
(r_j\sqrt T)^{-1}
=
\rho^{-1}.
\]

Thus the known palinstrophy tail is still exactly critical after physical restoration.

The base-gain problem survives, but at a substantially weaker derivative level.

## 11. Relation to M19-310--312

- M19-310's `m>9/4` remains a valid **isotropic** sufficient threshold.
- M19-311--312 remain valid endpoint/Lorentz analyses for that isotropic route.
- M19-313 supersedes the claim that `9/4` is the minimal strong derivative order for GMS closure.

The mixed-norm minimal strong threshold is

\[
\boxed{m>11/6.}
\]

## 12. New immediate target

Because `m=2` is already sufficient and M17-307 is exactly a palinstrophy ancestry ledger, the highest-value GMS calculation is now:

\[
\boxed{
\text{re-audit the M17-307 palinstrophy ledger under the M19-260 two-scale radius correction and determine whether first-hitting incidence or bounded overlap yields any physical }D^2u\text{ gain.}
}
\]

This route is strictly closer to existing certified resources than the previous raw-H2 transfer route.

---

\[
\boxed{\text{M19-313 COMPLETE; PHYSICAL PALINSTROPHY, NOT RAW-H2, IS ALREADY SUFFICIENT FOR THE GMS ANALYTIC CONTRADICTION.}}
\]