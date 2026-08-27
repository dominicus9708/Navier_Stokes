# DSD M5-86 — Full Local Velocity-Only Endpoint System

Date: 2026-08-27

Status: **PRESSURE / COMPONENT MEAN / LEVELWISE COEFFICIENT ALL ELIMINATED / THE EXACT M5-70 W1 ENDPOINT IMPLIES TWO COMPONENT-FREE LOCAL DIFFERENTIAL CONSTRAINTS WRITTEN ONLY IN `U` AND FINITE DERIVATIVES / NO LEVEL-SURFACE QUOTIENT OR COMPONENT COUNT REMAINS / POSITIVE CROSSING MAKES THE SYSTEM NONVACUOUS / NONEXISTENCE STILL OPEN / GLOBAL REGULARITY UNPROVED.**

## 1. Exact endpoint gradient form

Let

\[
a:=|U|>0,
\qquad
b:=U\cdot\nabla\log a.
\]

On an exact M5-70 endpoint define

\[
q:=P-2\nu b.
\]

M5-82 gives on every regular active patch

\[
\boxed{
\nabla q=\beta\nabla a,
}
\]

where locally

\[
\beta=\partial_a m(a,s).
\]

Since `q` is a scalar, the vector `beta grad a` is curl free. Therefore

\[
\boxed{
\nabla\beta\times\nabla a=0.
}
\]

Thus `beta` is itself a function of amplitude on every connected regular patch.

---

## 2. Leray amplitude equation

The W1 profile satisfies

\[
\partial_sU
-\nu\Delta U
+U\cdot\nabla U
+\frac12Y\cdot\nabla U
+\frac12U
+\nabla P
=0,
\qquad
\nabla\cdot U=0.
\]

Let

\[
\mathcal G
:=
|\nabla U|^2-|\nabla a|^2
\ge0.
\]

Dotting the Leray equation with `U/a` gives

\[
\boxed{
\partial_sa
+U\cdot\nabla a
+\frac12Y\cdot\nabla a
+\frac12a
+\frac Ua\cdot\nabla P
=
\nu\left(
\Delta a-rac{\mathcal G}{a}
\right).
}
\]

Since

\[
U\cdot\nabla a=ab
\]

and at the endpoint

\[
\nabla P
=
\beta\nabla a+2\nu\nabla b,
\]

we obtain

\[
\boxed{
F_L=\beta b,
}
\]

where the completely velocity-derived scalar is

\[
\boxed{
\begin{aligned}
F_L
:=\;&
\nu\Delta a
-\nu\frac{\mathcal G}{a}
-\partial_sa
-ab\\
&-
\frac12Y\cdot\nabla a
-
\frac12a
-
\frac{2\nu}{a}U\cdot\nabla b.
\end{aligned}
}
\]

This is the Leray-coordinate form of the M5-74 amplitude coefficient equation.

---

## 3. Eliminate beta from its tangential constancy

At points where `b` is nonzero,

\[
\beta=\frac{F_L}{b}.
\]

The condition

\[
\nabla\beta\times\nabla a=0
\]

therefore gives

\[
\nabla\left(\frac{F_L}{b}\right)
\times\nabla a
=0.
\]

Multiply by `b^2` to remove division:

\[
\boxed{
\nabla a
\times
\left(
 b\nabla F_L
-F_L\nabla b
\right)
=0.
}
\]

Define the first local velocity-only endpoint residual

\[
\boxed{
\mathcal R_{tan}
:=
\nabla a
\times
\left(
 b\nabla F_L
-F_L\nabla b
\right).
}
\]

Then every exact endpoint satisfies

\[
\boxed{\mathcal R_{tan}=0.}
\]

This formula remains algebraically meaningful at zeros of `b` and contains no component mean or pressure.

---

## 4. Pressure-Poisson still supplies an independent scalar equation

For the Leray profile, incompressibility gives the same pressure Poisson equation as in physical variables:

\[
\boxed{
-\Delta P
=Q_U,
\qquad
Q_U:=\partial_iU_j\,\partial_jU_i.
}
\]

The dilation terms make no contribution after taking divergence because `div U=0`.

Since

\[
P=q+2\nu b,
\qquad
q=m(a,s),
\]

we have

\[
\Delta q
=
\beta_a|\nabla a|^2
+
\beta\Delta a.
\]

Therefore

\[
\boxed{
\beta_a|\nabla a|^2
+
\beta\Delta a
+
2\nu\Delta b
+
Q_U
=0.
}
\]

This is the local M5-73 equation.

---

## 5. Eliminate beta and beta_a simultaneously

On a regular crossing point,

\[
\beta=\frac{F_L}{b}.
\]

Because `beta=beta(a,s)`,

\[
\nabla\beta
=
\beta_a\nabla a.
\]

Hence

\[
\beta_a|\nabla a|^2
=
\nabla\beta\cdot\nabla a.
\]

Also

\[
\nabla\beta
=
\frac{b\nabla F_L-F_L\nabla b}{b^2}.
\]

Insert these into pressure Poisson and multiply by `b^2`.

The result is the second local velocity-only constraint

\[
\boxed{
\begin{aligned}
\mathcal R_P
:=\;&
\left(
 b\nabla F_L-F_L\nabla b
\right)\cdot\nabla a\\
&+
F_Lb\,\Delta a\\
&+
b^2
\left(
2\nu\Delta b+Q_U
\right)
=0.
\end{aligned}
}
\]

Thus exact endpoint compatibility requires

\[
\boxed{\mathcal R_P=0.}
\]

No pressure, `m`, `beta`, or `beta_a` remains.

---

## 6. The closed local endpoint system

On every exact smooth regular crossing patch of a minimal-payer W1 limit, define from `U` alone

\[
a=|U|,
\qquad
b=U\cdot\nabla\log a,
\qquad
F_L
\]

as above.

Then the endpoint must satisfy

\[
\boxed{
\begin{cases}
\mathcal R_{tan}=0,\\[1mm]
\mathcal R_P=0,
\end{cases}
}
\]

with

\[
\boxed{
\mathcal R_{tan}
=
\nabla a\times(b\nabla F_L-F_L\nabla b),
}
\]

and

\[
\boxed{
\mathcal R_P
=
(b\nabla F_L-F_L\nabla b)\cdot\nabla a
+F_Lb\Delta a
+b^2(2\nu\Delta b+Q_U).
}
\]

This is a fully local, component-free, velocity-only representation of the endpoint rigidity conditions inherited from amplitude dynamics plus pressure Poisson.

---

## 7. Recovery interpretation

Where

\[
b\ne0,
\qquad
|\nabla a|>0,
\]

and `R_tan=0`, the vector

\[
b\nabla F_L-F_L\nabla b
\]

is parallel to `grad a`.

Thus one reconstructs

\[
\boxed{
\beta
=\frac{F_L}{b}
}
\]

and

\[
\boxed{
\beta_a
=
\frac{
(b\nabla F_L-F_L\nabla b)\cdot\nabla a
}{
b^2|\nabla a|^2
}.
}
\]

Then `R_P=0` is exactly the pressure-Poisson coefficient equation.

Hence the two residuals are not arbitrary new conditions; they are the coefficient-locking system with all auxiliary variables eliminated.

---

## 8. Behavior at zeros of b

At an exact endpoint the amplitude equation gives

\[
F_L=\beta b.
\]

Therefore

\[
\boxed{
b=0\Longrightarrow F_L=0.}
\]

The no-division residuals automatically vanish to the appropriate algebraic order at such points.

This means isolated or nodal zeros of `b` do not create singular quotients.

M5-78/M5-85 separately guarantee that the positive returned endpoint cannot have

\[
b\equiv0
\]

on the entire active weighted region.

Thus the system is genuinely tested on a positive-crossing set.

---

## 9. Scaling audit

Under physical Navier--Stokes scaling,

\[
a\mapsto\Lambda a,
\qquad
b\mapsto\Lambda^2b,
\qquad
F\mapsto\Lambda^3F.
\]

Hence

\[
b\nabla F-F\nabla b
\mapsto
\Lambda^6
(b\nabla F-F\nabla b),
\]

and

\[
\mathcal R_{tan}
\mapsto
\Lambda^8\mathcal R_{tan}.
\]

The scalar residual scales as

\[
\mathcal R_P
\mapsto
\Lambda^8\mathcal R_P.
\]

Therefore dimensionless versions may be taken as

\[
\boxed{
\frac{|\mathcal R_{tan}|}{a^8},
\qquad
\frac{|\mathcal R_P|}{a^8}
}
\]

on the positive amplitude band.

The exact zero conditions are scale invariant regardless of normalization.

---

## 10. Why this is stronger operationally than the levelwise system

M5-73--M5-76 required:

- choosing regular level surfaces;
- following connected components;
- recovering `beta` by surface quotients;
- differentiating the recovered coefficient across levels.

M5-86 instead tests the endpoint at a point using only a finite jet of `U`.

Thus a computational or analytic audit can search directly for the simultaneous zero set

\[
\boxed{
\mathcal R_{tan}=0,
\qquad
\mathcal R_P=0,
\qquad
b\ne0.
}
\]

No branch bookkeeping is needed at the test stage.

---

## 11. DSD audit

### GREEN

The Leray amplitude equation gives `F_L=beta b` exactly at the endpoint.

### GREEN

Curl-free coefficient locking eliminates `beta` without division through `R_tan`.

### GREEN

Pressure Poisson eliminates `beta_a` and yields the second no-division residual `R_P`.

### GREEN

Both residuals are component-free and depend only on the velocity jet.

### GREEN

The positive-crossing lower bound prevents the resulting endpoint system from being vacuous everywhere.

### YELLOW

The simultaneous zero set of these local residuals may contain nontrivial local configurations. Global smoothness, finite-energy ancestry, and recurrence have not yet been inserted into their classification.

### RED

It would be invalid to infer global regularity merely because the endpoint system is overdetermined.

---

## 12. Next calculation

The next audit should test whether the local system is itself empty or whether local source/sink-type models can satisfy it.

If nontrivial local models exist, identify exactly which global W1 conditions exclude them. This prevents wasting the endgame on a false local nonexistence claim and should reveal the missing global rigidity input.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
