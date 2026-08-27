# DSD M5-87 — Punctured Radial Stress Test and the Global Flux Obstruction

Date: 2026-08-27

Status: **LOCAL NONEMPTY MODEL FOUND / A PUNCTURED RADIAL HARMONIC SOURCE-SINK SOLVES NAVIER--STOKES AND SATISFIES THE LOCAL DIFFERENTIAL ENDPOINT FORM `grad(P-2nu b) parallel grad a` / IT FAILS THE ACTUAL M5-70 COMPONENTWISE CENTERING BECAUSE ITS CLOSED-LEVEL FLUX IS NONZERO AND ITS DIVERGENCE CARRIES A POINT SOURCE AT THE PUNCTURE / THEREFORE PURELY LOCAL NONEXISTENCE IS FALSE AS A STRATEGY / GLOBAL SMOOTH DIVERGENCE-FREE TOPOLOGY IS ESSENTIAL / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-86 reduced the exact endpoint to local velocity-only differential residuals.

Before attempting to prove that their simultaneous zero set is empty, one must test whether nontrivial local Navier--Stokes configurations can satisfy the underlying differential relation.

They can.

The simplest stress test is the radial harmonic source/sink on a punctured three-dimensional domain.

---

## 2. Radial punctured flow

Let

\[
U(x)
=
 c\frac{x}{|x|^3},
\qquad
c\ne0,
\qquad
r:=|x|>0.
\]

Write

\[
\sigma:=\operatorname{sgn}c.
\]

Then

\[
U
=
\sigma a e_r,
\qquad
\boxed{
a=|U|=|c|r^{-2}.}
\]

On the punctured domain

\[
\mathbb R^3\setminus\{0\},
\]

we have

\[
\boxed{
\nabla\cdot U=0,
\qquad
\nabla\times U=0,
\qquad
\Delta U=0.
}
\]

The field is the gradient of the harmonic potential `-c/r`.

---

## 3. It is an exact steady Navier--Stokes solution away from the puncture

Because the flow is irrotational,

\[
U\cdot\nabla U
=
\nabla\frac{|U|^2}{2}.
\]

Choose

\[
\boxed{
P
=-\frac12a^2+C.
}
\]

Then

\[
U\cdot\nabla U+\nabla P=0,
\]

and since `Delta U=0`,

\[
\boxed{
U\cdot\nabla U+\nabla P
=\nu\Delta U
}
\]

for every viscosity `nu>0` on `r>0`.

Thus the stress test is not merely a kinematic field; it solves the unforced stationary Navier--Stokes equation on the punctured domain.

---

## 4. Compute the crossing variable

Since

\[
\log a
=
\log|c|-2\log r,
\]

we have

\[
\nabla\log a
=-\frac2r e_r.
\]

Therefore

\[
\boxed{
b
:=
U\cdot\nabla\log a
=-2c\,r^{-3}.}
\]

Using

\[
r=\left(\frac{|c|}{a}\right)^{1/2},
\]

this becomes

\[
\boxed{
b
=-2\sigma
\frac{a^{3/2}}{|c|^{1/2}}.}
\]

Hence `b` is a scalar function of amplitude.

It is nonzero everywhere on the punctured domain.

---

## 5. The local differential endpoint relation holds

Define

\[
q:=P-2\nu b.
\]

Then

\[
\boxed{
q(a)
=
-\frac12a^2
+
4\nu\sigma
\frac{a^{3/2}}{|c|^{1/2}}
+C.
}
\]

Thus

\[
\boxed{
\nabla q
=q_a(a)\nabla a.
}
\]

Equivalently,

\[
\boxed{
\nabla(P-2\nu b)\times\nabla a=0.
}
\]

This is exactly the local M5-82 differential endpoint condition.

Because the field is an exact Navier--Stokes solution and `q=q(a)`, the local amplitude and pressure-Poisson coefficient identities behind M5-86 are also satisfied on the punctured region.

Therefore the simultaneous local differential endpoint system is **not empty**.

---

## 6. Why this is not an actual M5-70 endpoint

Fix a sphere

\[
\Gamma_r=\{|x|=r\}.
\]

Both `a` and `P` are constant on this sphere.

Therefore the actual componentwise pressure mean is

\[
\boxed{
m_P(a)=P.}
\]

The M5-70 centered endpoint equation would require

\[
P-m_P(a)=2\nu b.
\]

But the left side is zero while

\[
b\ne0.
\]

Hence

\[
\boxed{
P-m_P(a)=0
\ne
2\nu b.
}
\]

So the punctured radial solution satisfies the **differential** condition `q=q(a)` but fails the actual centered M5-70 equality.

The missing information is the global closed-level flux/mean constraint.

---

## 7. Exact flux failure

The outward flux through every sphere is

\[
\begin{aligned}
\int_{\Gamma_r}U\cdot n\,dS
&=
\frac c{r^2}\,4\pi r^2\\
&=
\boxed{4\pi c\ne0.}
\end{aligned}
\]

Thus the usual componentwise zero-flux identity used by M5-68/M5-72 does not hold for a volume enclosing the puncture.

Distributionally,

\[
\boxed{
\nabla\cdot\left(c\frac{x}{|x|^3}\right)
=4\pi c\,\delta_0.
}
\]

The puncture is precisely a source or sink carrying the missing flux.

Hence this local endpoint model is excluded from the actual whole-space smooth incompressible W1 class.

---

## 8. Coarea mean diagnosis

On a regular amplitude sphere,

\[
\frac{b}{|\nabla a|}
=
\frac1a U\cdot n_a
\]

up to the fixed normal-orientation convention.

For a smooth bounded superlevel component M5-72 uses

\[
\int_{\Gamma}
\frac{b}{|\nabla a|}dS
=
\frac1a
\int_\Gamma U\cdot n\,dS
=0.
\]

The radial punctured model instead gives a nonzero value because its flux is `4 pi c`.

Therefore the centered-pressure condition is not a cosmetic gauge choice. It encodes a genuinely global incompressibility constraint that the local differential equation cannot see.

---

## 9. Leray-coordinate version

Applying the inverse/forward Leray transformation to the same punctured physical solution produces a smooth Leray solution on every compact set avoiding the moving puncture.

At each Leray time the transformed quantities still satisfy

\[
P-2\nu b=m(a,s)
\]

locally, with a time-dependent scalar function `m`.

Thus the M5-86 local residuals vanish on the punctured region after the coordinate change as well.

The obstruction remains exactly the same: a closed surface enclosing the puncture carries nonzero flux.

So the stress test applies directly to the logic of the W1 local endpoint system.

---

## 10. Consequence for the proof strategy

The following target is now rejected:

\[
\boxed{
\text{prove that }
\mathcal R_{tan}=\mathcal R_P=0,\ b\ne0
\text{ has no local smooth solutions.}
}
\]

That statement is false on punctured domains.

The correct target must retain at least one global condition absent from the local jet system, such as

1. zero flux through every bounded connected superlevel component;
2. smooth extension across the entire enclosed region;
3. finite-energy whole-space ancestry;
4. recurrent W1 compactness.

The local differential endpoint equations should therefore be viewed as necessary local structure, while componentwise centering/zero flux remains an indispensable global closure condition.

---

## 11. A sharper surviving topology requirement

A genuine exact positive M5-70 endpoint must combine

\[
\boxed{
P-m_{P,k}(a,s)=2\nu b
}
\]

with

\[
\boxed{
\int_{\partial\Omega_{\lambda,k}}
U\cdot n\,dS=0
}
\]

for every bounded connected superlevel component.

Thus a source/sink-like normal crossing cannot simply terminate at an interior singular charge.

All inward and outward crossing must reconnect within one globally smooth divergence-free field.

This is the global geometric feature that the radial stress test fails.

---

## 12. DSD audit

### GREEN

The punctured radial source/sink is an exact stationary Navier--Stokes solution away from the puncture.

### GREEN

It satisfies the local differential endpoint relation and therefore demonstrates that the local M5-86 zero set is nonempty.

### GREEN

It fails the actual M5-70 centered equation for exactly the same reason that its enclosed flux is nonzero.

### GREEN

The point singularity carries the missing divergence distributionally.

### YELLOW

More complicated globally smooth source-sink reconnection geometries may still satisfy the centered endpoint on a finite amplitude band; they have not been classified.

### RED

A proof that ignores componentwise zero flux and attempts pure local endpoint nonexistence cannot close the W1 problem.

---

## 13. Next calculation

Use the exact centered relation to derive a **zero-flux sign-balance constraint for `b` on every full connected superlevel boundary** and combine it with local analyticity.

The target is to quantify the cost of reconnecting positive and negative crossing without a singular source/sink.

This cost should be compared directly with the angular/formation terms `A_w+G_w` in the exact endpoint identity

\[
X_w=\nu(T-A_w-G_w).
\]

If smooth zero-flux reconnection necessarily forces

\[
T\le A_w+G_w,
\]

then the positive exact endpoint would be excluded. Establishing or refuting precisely this inequality is now the most direct geometric gate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
