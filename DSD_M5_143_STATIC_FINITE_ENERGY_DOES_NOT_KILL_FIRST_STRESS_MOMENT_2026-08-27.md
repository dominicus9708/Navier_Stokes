# DSD M5-143 — Static Finite Energy Does Not Kill the First Stress Moment

Date: 2026-08-27

Status: **P1_A PRUNING / SMOOTH COMPACTLY SUPPORTED DIVERGENCE-FREE DATA FOR THE UNFORCED WHOLE-SPACE NSE CAN HAVE NONZERO FIRST MOMENTS OF THE QUADRATIC STRESS AND THEREFORE NONZERO `r^-4` FAR-PRESSURE MULTIPOLES / FINITE ENERGY AND ZERO EXTERNAL FORCE ALONE DO NOT ELIMINATE THE FIRST ODD CENTER-MOMENT CHANNEL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Whole-space pressure of compact data

Let

\[
a\in C_c^\infty(\mathbb R^3;\mathbb R^3),
\qquad
\nabla\cdot a=0,
\]

be nonzero smooth compactly supported divergence-free data.

At the initial time the pressure is determined by

\[
-\Delta p
=
\partial_i\partial_j(a_i a_j),
\]

or equivalently

\[
p(x)
=
K_{ij}*(a_i a_j)(x),
\]

where

\[
K_{ij}(x)=\partial_i\partial_j\frac{1}{4\pi|x|}
\]

is homogeneous of degree `-3`.

---

## 2. Far-field multipole expansion

For large `|x|` and compactly supported stress,

\[
K_{ij}(x-y)
=
K_{ij}(x)
-y_k\partial_kK_{ij}(x)
+\frac12y_ky_l\partial_{kl}K_{ij}(x)
+\cdots.
\]

Therefore

\[
\boxed{
\begin{aligned}
p(x)
&=
K_{ij}(x)M_{ij}^{(0)}
-
\partial_kK_{ij}(x)M_{ij,k}^{(1)}
+\cdots,
\end{aligned}
}
\]

with

\[
M_{ij}^{(0)}
:=\int a_i a_j\,dy,
\]

and

\[
\boxed{
M_{ij,k}^{(1)}
:=\int y_k a_i(y)a_j(y)\,dy.
}
\]

Since

\[
K_{ij}=O(r^{-3}),
\qquad
\partial_kK_{ij}=O(r^{-4}),
\]

the first stress moment generates an `r^-4` pressure contribution, including the degree-3 harmonic sector relevant to M5-142.

---

## 3. Translation makes the first moment generically nonzero

Translate the same velocity profile by a vector `c`:

\[
a^{(c)}(y):=a(y-c).
\]

It remains smooth, compactly supported, divergence-free, and finite energy.

Its zeroth stress moment is unchanged:

\[
M_{ij}^{(0)}[a^{(c)}]
=M_{ij}^{(0)}[a].
\]

But its first moment is

\[
\begin{aligned}
M_{ij,k}^{(1)}[a^{(c)}]
&=
\int y_k a_i(y-c)a_j(y-c)dy\\
&=
M_{ij,k}^{(1)}[a]
+c_kM_{ij}^{(0)}[a].
\end{aligned}
\]

Hence, for a nonzero stress tensor `M^(0)`, suitable translations produce nonzero first moments.

Therefore

\[
\boxed{
\text{finite energy + divergence free + no external force}
\not\Rightarrow
M^{(1)}=0.
}
\]

---

## 4. Compatibility with unforced NSE

Such smooth compactly supported divergence-free data are ordinary admissible initial data for the unforced whole-space Navier–Stokes equation and generate a local smooth solution.

Thus a nonzero first pressure/stress multipole is not an indication of an external point force.

It can be produced by ordinary spatial distribution of nonlinear stress.

---

## 5. DSD audit

### Formation — GREEN

The first moment is formed from the actual quadratic stress `a tensor a`.

### Axis — GREEN

External force, net stress moment, and center choice are separated.

### Static aggregation — GREEN

A nonzero `r^-4` pressure term is not counted as an external source merely because it is a far multipole.

### Dynamics — GREEN

The example is compatible with ordinary local unforced NSE evolution.

### Cross-audit — GREEN

M5-142 remains correct: terminal odd multipoles correspond to center stress moments. M5-143 shows that ordinary finite-energy/force-free assumptions do not force those moments to vanish.

---

## 6. Consequence for P1_A

The first odd algebraic fiber channel cannot be closed by a static theorem of the form

\[
\text{unforced finite energy}
\Rightarrow
\text{all odd stress moments vanish}.
\]

Such a theorem is false even for completely regular compactly supported data.

Any elimination of the `ell=3` terminal multipole must use additional blow-up-specific information, such as

- centering at the singular trajectory;
- compact W1 recurrence;
- canonical-tail matching;
- or a renormalized moment law along the terminal scaling flow.

---

## 7. RED firewall

Do not interpret higher pressure multipoles as external forces.

Only the leading critical point-stress-type channel has that direct interpretation. Faster multipoles can arise from ordinary internal stress geometry.

---

## 8. Next target

The correct first-moment question is dynamic:

\[
\boxed{
\text{Does terminal-centered W1 recurrence force the renormalized first stress moment to be constant, vanish, or drift incompatibly with the same-tail factor?}
}
\]

This requires deriving the scaling/transport law of the renormalized stress moment, not using finite energy alone.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]