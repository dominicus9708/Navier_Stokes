# DSD M5-84 — Tangential Interpolation from the Exact Endpoint Surplus

Date: 2026-08-27

Status: **COMPONENT-FREE STABILITY INEQUALITY DERIVED / TANGENT VECTOR FIELDS ANNIHILATE ALL AMPLITUDE-BRANCH MEANS AND ARE SKEW-ADJOINT FOR THE M5 WEIGHT / THE M5-82 LOCAL TANGENTIAL DEFECT IS CONTROLLED BY THE SQUARE ROOT OF THE M5-83 PAYER SURPLUS TIMES ONE FINITE HIGHER-TANGENTIAL-DERIVATIVE FACTOR / COMPONENT COUNT DOES NOT ENTER / UNIFORM W1 CONTROL OF THE HIGHER FACTOR IS THE NEXT AUDIT / GLOBAL REGULARITY UNPROVED.**

## 1. Residual from M5-83

Set

\[
a:=|U|>0,
\qquad
b:=U\cdot\nabla\log a,
\]

and

\[
q:=P-2\nu b.
\]

On each connected regular amplitude branch let

\[
m_k(a,t)
\]

be the componentwise pressure mean from M5-68.

Define

\[
r:=q-m_k(a,t).
\]

M5-83 gives

\[
\boxed{
\mathcal E_w
:=
S_{comp,w}
-4\nu^2(A_w+G_w)
-4\nu X_w
=
\int |r|^2d\mu,
}
\]

with

\[
\boxed{
d\mu=a\,w(a)\,dY.
}
\]

---

## 2. Tangential vector fields

For each pair `i<j`, define

\[
\boxed{
L_{ij}
:=(\partial_i a)\partial_j
-(\partial_j a)\partial_i.
}
\]

These vector fields are tangent to every regular amplitude level because

\[
\boxed{
L_{ij}a=0.
}
\]

Therefore for every scalar branch function `m(a,t)`,

\[
\boxed{
L_{ij}m(a,t)=0.
}
\]

Consequently

\[
\boxed{
L_{ij}r=L_{ij}q,
\qquad
L_{ij}^2r=L_{ij}^2q.
}
\]

No derivative of the unknown branch mean appears.

---

## 3. The tangent fields are divergence free

The vector field associated with `L_ij` has components

\[
V_j=\partial_i a,
\qquad
V_i=-\partial_j a,
\]

and all other components zero.

Hence

\[
\nabla\cdot V
=
\partial_j\partial_i a
-\partial_i\partial_j a
=0.
\]

Thus

\[
\boxed{
\nabla\cdot L_{ij}=0
}
\]

in the vector-field sense.

---

## 4. The M5 weight is invariant along Lij

Let

\[
\rho(a):=a\,w(a).
\]

Since `L_ij a=0`,

\[
L_{ij}\rho(a)
=
\rho'(a)L_{ij}a
=0.
\]

Therefore

\[
\nabla\cdot(\rho V)
=
\rho\nabla\cdot V
+V\cdot\nabla\rho
=0.
\]

Hence `L_ij` is formally skew-adjoint in the weighted space `L2(dmu)`:

\[
\boxed{
\int fL_{ij}g\,d\mu
=
-\int gL_{ij}f\,d\mu
}
\]

whenever the boundary terms vanish.

The amplitude-band boundaries themselves produce no tangential flux because `L_ij a=0`.

Spatial infinity may be handled by cutoff/exhaustion whenever the displayed weighted norms are finite.

---

## 5. One-step interpolation identity

Apply weighted skew-adjointness with

\[
f=r,
\qquad
g=L_{ij}r.
\]

Then

\[
\int |L_{ij}r|^2d\mu
=
-\int rL_{ij}^2r\,d\mu.
\]

Using `L_ij r=L_ij q` and `L_ij^2r=L_ij^2q`,

\[
\boxed{
\|L_{ij}q\|_{L^2(d\mu)}^2
\le
\|r\|_{L^2(d\mu)}
\|L_{ij}^2q\|_{L^2(d\mu)}.
}
\]

Because

\[
\|r\|_{L^2(d\mu)}
=\mathcal E_w^{1/2},
\]

we obtain

\[
\boxed{
\|L_{ij}q\|_2^2
\le
\mathcal E_w^{1/2}
\|L_{ij}^2q\|_2.
}
\]

---

## 6. Sum over the three tangential generators

Define

\[
M_{tan,2}
:=
\left(
\sum_{i<j}
\|L_{ij}^2q\|_{L^2(d\mu)}^2
\right)^{1/2}.
\]

By Cauchy--Schwarz in the three index pairs,

\[
\sum_{i<j}
\|L_{ij}^2q\|_2
\le
\sqrt3\,M_{tan,2}.
\]

Therefore

\[
\boxed{
\sum_{i<j}
\|L_{ij}q\|_2^2
\le
\sqrt3\,
M_{tan,2}
\mathcal E_w^{1/2}.
}
\]

---

## 7. Exact identification with the cross-gradient defect

The three components of

\[
\nabla a\times\nabla q
\]

are precisely, up to sign,

\[
L_{23}q,
\qquad
L_{31}q,
\qquad
L_{12}q.
\]

Hence

\[
\boxed{
|\nabla a\times\nabla q|^2
=
\sum_{i<j}|L_{ij}q|^2.
}
\]

Integrating gives the central stability estimate

\[
\boxed{
\int
|\nabla a\times\nabla(P-2\nu b)|^2
\,d\mu
\le
\sqrt3\,
M_{tan,2}
\mathcal E_w^{1/2}.
}
\]

This is the component-free near-saturation bridge sought after M5-82/M5-83.

---

## 8. Velocity-only form

In physical Navier--Stokes coordinates,

\[
\nabla(P-2\nu b)
=
Z_{NS},
\]

where

\[
Z_{NS}
=
\nu\Delta U
-\partial_tU
-U\cdot\nabla U
-2\nu\nabla b.
\]

Therefore

\[
\boxed{
\int
|\nabla a\times Z_{NS}|^2d\mu
\le
\sqrt3\,
M_{tan,2}
\mathcal E_w^{1/2}.
}
\]

In Leray coordinates, replace `Z_NS` by

\[
Z_L
=
\nu\Delta U
-\partial_sU
-U\cdot\nabla U
-\frac12Y\cdot\nabla U
-\frac12U
-2\nu\nabla b.
\]

Then

\[
\boxed{
\int
|\nabla a\times Z_L|^2d\mu
\le
\sqrt3\,
M_{tan,2}
\mathcal E_w^{1/2}.
}
\]

---

## 9. Consequence for a saturating sequence

Suppose

\[
\mathcal E_{w,n}\to0
\]

and, along the returned W1 sequence,

\[
\boxed{
M_{tan,2,n}\le M_*<\infty.
}
\]

Then

\[
\boxed{
\int
|\nabla a_n\times Z_{L,n}|^2d\mu_n
\to0.
}
\]

Thus near-minimal pressure payment forces the component-free local M5-82 defect to vanish in weighted `L2`.

No lower bound on the crossing mass of any **individual** connected component is required.

No bound on the number of components is required.

No derivative of `m_k` is required.

This removes the main formulation-level fragmentation obstacle identified in M5-81.

---

## 10. Relation to regular tangential projection

At points where

\[
|\nabla a|>0,
\]

we have

\[
|\nabla a\times Z_L|^2
=
|\nabla a|^2
|\Pi_\tau Z_L|^2.
\]

Therefore, on any region with a quantitative regularity margin

\[
|\nabla a|\ge\kappa>0,
\]

M5-84 immediately yields

\[
\int|\Pi_\tau Z_L|^2d\mu
\le
\frac{\sqrt3}{\kappa^2}
M_{tan,2}\mathcal E_w^{1/2}.
\]

But the cross-product form remains valid without dividing by `|grad a|` and is therefore the safer global endpoint diagnostic.

---

## 11. Why the higher factor is plausible on W1

The quantity

\[
L_{ij}^2q
\]

contains only finitely many derivatives of

\[
a=|U|
\]

and

\[
q=P-2\nu U\cdot\nabla\log a.
\]

On a finite amplitude band bounded away from `a=0`, it involves finite-order derivatives of the smooth Navier--Stokes state.

The W1 compact class already provides uniform local analytic derivative bounds on every fixed core cylinder.

Therefore a **localized** version of

\[
M_{tan,2}\le M_*
\]

is directly compatible with the existing W1 compactness package.

What is not yet proved is a uniform global weighted bound if the active finite-amplitude region is allowed to migrate arbitrarily far into the W1 critical tail.

---

## 12. Critical-set and branch-gluing audit

The integration by parts is exact on smooth regular branch regions.

Critical amplitude sets and branch birth/merger values require an exhaustion argument.

The favorable facts are:

- critical values have measure zero for each smooth state;
- the tangential fields vanish in the relevant direction when `grad a=0`;
- `L_ij` has no normal flux through amplitude-band boundaries because `L_ij a=0`.

Nevertheless, a fully uniform passage through a sequence of increasingly complicated critical sets is not yet claimed.

This remains a technical YELLOW item rather than being silently ignored.

---

## 13. DSD audit

### GREEN

`L_ij` annihilates amplitude and every branch mean `m_k(a,t)`.

### GREEN

`L_ij` is divergence free and preserves the M5 weight `a w(a)`.

### GREEN

Weighted integration by parts gives an exact interpolation inequality from the scalar endpoint residual to the tangential cross-gradient defect.

### GREEN

The estimate is independent of component count and therefore bypasses component fragmentation at the quantitative level, provided the higher tangential factor is uniformly bounded.

### YELLOW

Uniform localized control of `M_tan,2` follows naturally from W1 analyticity, but the required global/active-region localization must be matched carefully to the existing pump support.

### YELLOW

Critical-set exhaustion across a varying sequence still requires a clean technical lemma.

### RED

The estimate forces near-endpoint geometry from near-minimal payment; it does not prove that the exact local endpoint geometry is impossible.

---

## 14. Next calculation

Audit the support of the M5 returned pump and prove that the active finite-amplitude region carrying the fixed positive crossing amount can be retained inside a fixed W1 core plus finitely many controlled neighbor shells.

If that localization gives

\[
M_{tan,2}\le M_*
\]

uniformly, then every saturating sequence satisfies the component-free vanishing defect

\[
\nabla a\times Z_L\to0
\]

in weighted `L2`.

The endpoint problem would then reduce to excluding a nonzero recurrent W1 limit satisfying the local first-order constraint

\[
\boxed{
\nabla a\times Z_L=0
}
\]

on a positive-crossing active set.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
