# DSD M17-291 — R^7 minimal parabolic growth forces a quadratic caloric polynomial incompatible with bounded-K CE-H

Date: 2026-09-06  
Canonical ID: **M17-291**

Status: **MINIMAL-INFINITY-GROWTH CLOSURE / M17-287 SHOWS THAT A NONZERO PRESENT SECOND-DERIVATIVE CORE REQUIRES AT LEAST `R^7` BACKWARD MASS GROWTH. IF AN ANCIENT RAW HEAT TANGENT HAS THE MATCHING GLOBAL PARABOLIC UPPER GROWTH `sup_{-R^2<=tau<=0} int_{B_R}|V|^2 <= C R^7`, STANDARD PARABOLIC INTERIOR DERIVATIVE ESTIMATES GIVE `|grad^m V| <= C R^(2-m)`, SO EVERY THIRD AND HIGHER SPATIAL DERIVATIVE VANISHES AS `R->infinity`. THUS `V` IS A SPATIAL QUADRATIC CALORIC POLYNOMIAL `Q(x)+Lx+c+tau d`, `d=Delta Q`. NONZERO RAW LAPLACIAN CHARGE FORCES `d!=0`; CE-H `Delta V=K V` THEN MAKES `V` EVERYWHERE PARALLEL TO THE FIXED VECTOR `d`, SO `V=phi d` WITH `phi_tau=Delta phi=1`. SUCH AN ENTIRE QUADRATIC CALORIC SCALAR CANNOT MAINTAIN A BOUNDED-K TIME-STATIONARY ACTIVE/NODAL SET FOR ALL ANCIENT TIMES: `K=1/phi` BLOWS AT ZERO CROSSINGS, AND THE `+tau` TERM FORCES THE ZERO GEOMETRY TO CHANGE OR THE ACTIVE CORRIDOR TO FAIL. THEREFORE THE EXACT R7 MINIMAL-GROWTH LANE CLOSES; A PAYER-FREE UNBOUNDED SURVIVOR MUST HAVE SUPER-R7 PARABOLIC GROWTH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Parabolic R7 growth hypothesis

Assume the ancient raw tangent is defined on all of `R3 x (-infinity,0]` or on an unbounded stationary component with no boundary contribution in the interior estimate under consideration.

Suppose there is a constant `C_G` such that for every sufficiently large `R`,

\[
\boxed{
\sup_{-R^2\le\tau\le0}
\int_{B_R}|V(x,\tau)|^2dx
\le C_G R^7.
}
\]

Then the spacetime cylinder mass satisfies

\[
\boxed{
\int_{-R^2}^0\int_{B_R}|V|^2dx\,d\tau
\le C_G R^9.
}
\]

Hence

\[
\|V\|_{L^2(Q_R)}\le C R^{9/2}.
\]

---

## 2. Interior derivative decay

For a caloric function in dimension three, the standard scale-invariant interior estimate gives, for every spatial derivative order `m`,

\[
|\nabla^m V(0,0)|
\le
C_m
R^{-m-(3+2)/2}
\|V\|_{L^2(Q_R)}.
\]

Using the `R^(9/2)` spacetime norm,

\[
\boxed{
|\nabla^m V(0,0)|
\le C_mR^{2-m}.
}
\]

For every

\[
m\ge3,
\]

letting `R->infinity` yields

\[
\boxed{
\nabla^m V(0,0)=0.
}
\]

The same argument centered at any fixed spatial point and fixed finite ancient time gives

\[
\boxed{
\nabla^3V\equiv0.
}
\]

---

## 3. Quadratic caloric classification

Therefore `V` is at most quadratic in the spatial variables:

\[
V(x,\tau)
=Q(x,\tau)+L(\tau)x+c(\tau).
\]

The heat equation

\[
\partial_\tau V=\Delta V
\]

shows that the quadratic and linear coefficients are time independent, while the constant coefficient is affine in time.

Thus

\[
\boxed{
V(x,\tau)
=Q(x)+Lx+c+\tau d,
\qquad
d:=\Delta Q\in\mathbb R^3.
}
\]

Here `d` is constant in space and time.

---

## 4. Raw spectral charge forces d nonzero

The root tangent retains a fixed nonzero raw Laplacian charge:

\[
\int_{B_0}|\Delta V(\cdot,0)|^2>0.
\]

But

\[
\Delta V\equiv d.
\]

Therefore

\[
\boxed{d\neq0.}
\]

---

## 5. CE-H collapses the target direction

The simultaneous CE-H relation is

\[
\boxed{\Delta V=KV.}
\]

Since `Delta V=d`, on every active point

\[
\boxed{d=K(x,\tau)V(x,\tau).}
\]

Because `d!=0`, every active `V(x,tau)` is parallel to the same fixed target vector `d`.

All target components orthogonal to `d` are polynomials vanishing on the nonempty active set and therefore vanish identically.

Hence

\[
\boxed{V=\phi d}
\]

for a scalar quadratic caloric polynomial `phi`.

After absorbing the constant magnitude of `d`,

\[
\boxed{
\partial_\tau\phi
=\Delta\phi
=1.
}
\]

Thus

\[
\boxed{
\phi(x,\tau)=q_2(x)+\ell(x)+c_0+\tau,
\qquad
\Delta q_2=1.
}
\]

Also

\[
\boxed{K=1/\phi}
\]

on the active set.

---

## 6. Bounded-K ancient nodal incompatibility

The trace of the Hessian of `q_2` is positive because

\[
\Delta q_2=1.
\]

Hence `q_2+ell+c_0` cannot be bounded above by a finite constant in every spatial direction.

At the same time the term

\[
+\tau
\]

tends to `-infinity` at every fixed spatial point as `tau->-infinity`.

Therefore the scalar cannot remain globally separated from zero with one time-stationary active/nodal geometry through the whole ancient interval.

Whenever

\[
\phi=0,
\]

we have a nodal point and

\[
K=1/\phi
\]

blows up.

Moreover, because `partial_tau phi=1`, any regular zero necessarily changes membership in time, contradicting the bounded-K nodal stationarity of M17-283.

Thus

\[
\boxed{
H_{R^7\ minimal\ parabolic\ growth}
\Longrightarrow
G_{K\text{-}failure}
\lor
G_{moving/nodal\ interface}
\lor
\bot.
}
\]

Both exits already return to the existing payer ledger.

---

## 7. Super-R7 survivor

Combining M17-287 with M17-291:

- slower than `R7` growth cannot feed the present nonzero second derivative;
- exact `O(R7)` parabolic growth gives a quadratic caloric polynomial and closes;
- therefore a payer-free infinity survivor must exceed the minimal polynomial rate.

Thus

\[
\boxed{
G_{unbounded\ infinity\ survivor}
\Longrightarrow
G_{super\text{-}R^7\ parabolic\ mass\ growth}
\lor
G_{far\text{-}boundary/coefficient/interface\ feed}.
}
\]

---

## 8. DSD audit

- The upper growth assumption is parabolic and uniform over `[-R^2,0]`; a single-time `R7` bound is not silently promoted to it.
- The classification uses direct interior estimates rather than importing a stronger global polynomial-growth theorem.
- CE-H is essential in reducing the vector quadratic polynomial to one scalar target line.
- The result closes only the minimal `R7` growth lane; super-`R7` growth remains open.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
