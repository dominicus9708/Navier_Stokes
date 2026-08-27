# DSD M5-82 — Component-Free Local Tangential Endpoint Defect

Date: 2026-08-27

Status: **LOCAL EQUIVALENT FORM OF THE M5-70 ENDPOINT DERIVED ON REGULAR AMPLITUDE REGIONS / COMPONENTWISE PRESSURE MEANS ARE ELIMINATED BY TANGENTIAL DIFFERENTIATION / NAVIER--STOKES ELIMINATES PRESSURE GRADIENT AND PRODUCES A PURE VELOCITY LOCAL DEFECT / COMPONENT FRAGMENTATION DOES NOT HIDE THIS CONDITION / GLOBAL REGULARITY UNPROVED.**

## 1. Endpoint relation

Let

\[
a:=|U|>0,
\qquad
b:=U\cdot\nabla\log a.
\]

M5-70 exact saturation gives, on each regular connected amplitude branch,

\[
\boxed{
P-m_k(a,t)=2\nu b.
}
\]

Equivalently,

\[
q:=P-2\nu b
\]

is a function only of `a` on each connected regular branch:

\[
q=m_k(a,t).
\]

---

## 2. Eliminate the component mean by tangential differentiation

On a regular point

\[
\nabla a\ne0,
\]

define

\[
n:=\frac{\nabla a}{|\nabla a|}
\]

and the tangential projection

\[
\Pi_\tau:=I-n\otimes n.
\]

Because

\[
\nabla m_k(a,t)=m_{k,a}(a,t)\nabla a,
\]

M5-70 implies

\[
\boxed{
\Pi_\tau\nabla(P-2\nu b)=0.
}
\]

Equivalently,

\[
\boxed{
\nabla(P-2\nu b)\times\nabla a=0.
}
\]

This condition contains no componentwise additive pressure mean.

It is pointwise and remains meaningful no matter how many connected superlevel components exist.

---

## 3. Local converse on a regular foliation patch

Let `O` be a connected open region on which

\[
a>0,
\qquad
|\nabla a|>0,
\]

and the level sets form a smooth local foliation.

Suppose

\[
\Pi_\tau\nabla(P-2\nu b)=0
\]

throughout `O`.

Then every tangent vector `T` to an amplitude level satisfies

\[
T\cdot\nabla(P-2\nu b)=0.
\]

Therefore `P-2nu b` is constant on every connected piece of each amplitude level in `O`.

Hence there exists a scalar branch function `m` such that

\[
\boxed{
P-2\nu b=m(a,t)
}
\]

locally on `O`.

Thus, away from critical levels, the tangential-gradient condition is the local differential form of the M5-70 endpoint equation.

---

## 4. Eliminate pressure using physical Navier--Stokes

In ordinary Navier--Stokes variables,

\[
\partial_tU
+U\cdot\nabla U
+\nabla P
=\nu\Delta U.
\]

Therefore

\[
\nabla P
=
\nu\Delta U
-\partial_tU
-U\cdot\nabla U.
\]

Define the velocity-only vector

\[
\boxed{
Z_{NS}
:=
\nu\Delta U
-\partial_tU
-U\cdot\nabla U
-2\nu\nabla b.
}
\]

For every exact regular M5-70 endpoint,

\[
\boxed{
\Pi_\tau Z_{NS}=0.
}
\]

Equivalently,

\[
\boxed{
Z_{NS}\times\nabla a=0.
}
\]

Thus the pressure and all component means disappear completely.

---

## 5. Leray-coordinate form for W1

The W1 autonomous profile satisfies

\[
\partial_sU
-\nu\Delta U
+U\cdot\nabla U
+\frac12Y\cdot\nabla U
+\frac12U
+\nabla P
=0.
\]

Hence

\[
\nabla P
=
\nu\Delta U
-\partial_sU
-U\cdot\nabla U
-\frac12Y\cdot\nabla U
-\frac12U.
\]

Define

\[
\boxed{
Z_L
:=
\nu\Delta U
-\partial_sU
-U\cdot\nabla U
-\frac12Y\cdot\nabla U
-\frac12U
-2\nu\nabla b.
}
\]

Then the exact M5-70 endpoint in Leray coordinates requires

\[
\boxed{
\Pi_\tau Z_L=0.
}
\]

This is the form directly adapted to the W1 recurrent phase space.

---

## 6. Local nonnegative defect

Define

\[
\boxed{
K_{tan}(Y,s)
:=
|\Pi_\tau Z_L|^2
=
|Z_L|^2-|Z_L\cdot n|^2
\ge0.
}
\]

At every regular exact endpoint point,

\[
\boxed{K_{tan}=0.}
\]

An equivalent no-normalization form is

\[
\boxed{
C_{tan}
:=
|Z_L\times\nabla a|^2
=0.
}
\]

The latter remains algebraically meaningful as `|grad a|` becomes small, although it loses coercivity exactly at a critical point.

---

## 7. Scale-invariant normalization

Under Navier--Stokes scaling,

\[
a_\Lambda=\Lambda a,
\qquad
\nabla a_\Lambda=\Lambda^2\nabla a,
\qquad
Z_\Lambda=\Lambda^3Z.
\]

Therefore

\[
K_{tan,\Lambda}=\Lambda^6K_{tan}.
\]

Since

\[
a_\Lambda^6=\Lambda^6a^6,
\]

the normalized local defect

\[
\boxed{
\mathfrak T
:=
\frac{K_{tan}}{a^6}
}
\]

is scale invariant wherever `a>0`:

\[
\boxed{
\mathfrak T_\Lambda=\mathfrak T.
}
\]

One may alternatively use the angle defect

\[
1-\frac{|Z\cdot n|^2}{|Z|^2}
\]

where `Z` is nonzero.

---

## 8. Why this bypasses component fragmentation

M5-75 recovered a scalar `beta_k` separately on each connected superlevel component.

A sequence could therefore try to evade a uniform componentwise quotient by splitting the total crossing mass among many small components.

The new condition does not sum or divide by component masses.

It is imposed pointwise:

\[
\boxed{
\Pi_\tau Z_L(Y,s)=0
}
\]

at every regular active endpoint point.

Hence increasing the number of connected components does not weaken the zero condition.

Component fragmentation remains relevant only to the passage from a near-saturation integral inequality to a pointwise zero defect; it is no longer an obstruction to **formulating** the exact endpoint rigidity condition.

---

## 9. Relation to beta and the previous coefficient locking

If

\[
\Pi_\tau Z_L=0
\]

and `grad a` is nonzero, then

\[
Z_L=\beta_{loc}\nabla a
\]

with

\[
\boxed{
\beta_{loc}
=
\frac{Z_L\cdot\nabla a}{|\nabla a|^2}.
}
\]

At an exact endpoint this equals

\[
\beta_{loc}=m_a.
\]

Because `Z_L` is the gradient of `P-2nu b` for an exact Navier--Stokes solution, its curl vanishes.

Taking the curl of

\[
Z_L=\beta_{loc}\nabla a
\]

gives

\[
\nabla\beta_{loc}\times\nabla a=0.
\]

Thus `beta_loc` is itself constant along connected regular amplitude levels.

Therefore the local tangential condition already contains the geometric content behind the M5-75 statement that one scalar `m_a` must work along each component.

The pressure-Poisson identities remain useful as independent algebraic diagnostics, but they are no longer the only route to coefficient locking.

---

## 10. Local analytic continuity

The vector `Z_L` uses only

- `U`,
- first Leray-time derivative,
- spatial derivatives through second order in the Navier--Stokes terms,
- and `grad b`, which uses spatial derivatives through second order away from `a=0`.

Therefore on any compact region with

\[
a\ge a_0>0,
\qquad
|\nabla a|\ge\kappa>0,
\]

W1 local analytic convergence gives

\[
\boxed{
K_{tan,n}\to K_{tan,*}
}
\]

uniformly after time-translation subsequence extraction.

This continuity is substantially simpler than the moving-surface continuity required for `mathfrak I`.

---

## 11. Crossing guarantees the defect is tested on a nonempty regular set

At the positive endpoint,

\[
T
=
\int a\,w(a)|b|^2dY
>0.
\]

If `grad a=0`, then

\[
b=U\cdot\nabla\log a=0.
\]

Hence the positive crossing mass is carried on points where

\[
\nabla a\ne0.
\]

Thus the endpoint cannot avoid the local tangential defect solely by sitting on critical points.

The remaining issue is quantitative: a saturating **sequence** could still concentrate the crossing mass near regions where the regularity margin tends to zero.

---

## 12. DSD audit

### GREEN

Tangential differentiation removes all independent component pressure means exactly.

### GREEN

Navier--Stokes removes the pressure gradient and yields a velocity-only pointwise endpoint condition.

### GREEN

The local defect is independent of the number of superlevel components and therefore formulation-level fragmentation is removed.

### GREEN

On a regular foliation patch, vanishing tangential defect is locally equivalent to `P-2nu b` being a function of amplitude.

### GREEN

The normalized defect `mathfrak T=K_tan/a^6` is scale invariant.

### YELLOW

Passing from small integrated Cauchy/algebraic payer surplus to small `K_tan` requires an interpolation/analytic-compactness argument; equality alone gives the exact zero condition.

### RED

No current argument proves that every nonzero recurrent W1 state has `K_tan>0` somewhere in a quantitatively unavoidable way.

---

## 13. Next calculation

The most promising next step is now local rather than topological:

derive a **near-saturation stability estimate** of the form

\[
\text{M5-69/M5-70 payer surplus small}
\quad\Longrightarrow\quad
\int_{\text{regular active core}}
K_{tan}
\text{ small},
\]

using the uniform W1 analytic derivative bounds.

If successful, any saturating recurrent sequence would converge locally to a state satisfying

\[
\Pi_\tau Z_L=0
\]

on a positive-crossing regular region, without needing a uniform bound on the number of amplitude components.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
