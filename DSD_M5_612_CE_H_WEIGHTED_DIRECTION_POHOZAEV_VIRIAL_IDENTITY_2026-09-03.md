# DSD M5-612 — CE-H weighted-direction Pohozaev virial identity

Date: 2026-09-03

Status: **DIRECTIONAL SCALE IDENTITY / GLOBAL CE-H GIVES THE WEIGHTED HARMONIC-MAP EQUATION `div(rho^2 nabla xi)+rho^2|nabla xi|^2 xi=0` ON THE ACTIVE SET / PAIRING THIS EQUATION WITH THE DILATION GENERATOR `y·nabla xi` KILLS THE SPHERE-CONSTRAINT TERM EXACTLY AND, AFTER AUDITING THE ZERO SET BY WEIGHTED REGULARIZATION AND THE INFINITY BOUNDARY BY THE TERMINAL-TAIL DECAY, YIELDS `P_dir + int (y·nabla rho^2)|nabla xi|^2 = 0` / EQUIVALENTLY THE ORIENTATION-GRADIENT MEASURE HAS ZERO MEAN OF `1+2 y·nabla log rho` / THUS ANY NONZERO CE-H DIRECTIONAL CHARGE REQUIRES RADIAL AMPLITUDE-SLOPE COMPENSATION AND CANNOT LIVE ON A SINGLE-SIGN HOMOGENEITY REGIME / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Weighted direction equation

On CE-H write

\[
W=\rho\xi,
\qquad
\rho=|W|,
\qquad
|\xi|=1
\]

on the active set.

The projected Laplacian condition

\[
P_\xi^\perp\Delta W=0
\]

is equivalent to

\[
\boxed{
\nabla\cdot(\rho^2\nabla\xi)
+
\rho^2|\nabla\xi|^2\xi
=0.
}
\]

This is the weighted harmonic-map equation already identified in M5-487 and specialized to zero weighted tension on CE-H.

---

## 2. Dilation test

Pair the equation with

\[
y\cdot\nabla\xi.
\]

Because `|xi|=1`,

\[
\xi\cdot\partial_j\xi=0,
\]

hence

\[
\xi\cdot(y\cdot\nabla\xi)=0.
\]

Therefore the constraint term drops out exactly:

\[
\rho^2|\nabla\xi|^2\xi\cdot(y\cdot\nabla\xi)=0.
\]

Thus only the divergence term remains.

---

## 3. Formal whole-space computation

Ignoring boundaries momentarily,

\[
0
=
\int
\nabla\cdot(\rho^2\nabla\xi)
\cdot(y\cdot\nabla\xi)dy.
\]

Integrate by parts:

\[
0
=
-\int\rho^2\partial_i\xi\cdot
\partial_i(y\cdot\nabla\xi)dy.
\]

Since

\[
\partial_i(y\cdot\nabla\xi)
=
\partial_i\xi+y\cdot\nabla\partial_i\xi,
\]

we get

\[
0
=
-P_{dir}
-
\frac12
\int\rho^2 y\cdot\nabla(|\nabla\xi|^2)dy,
\]

where

\[
P_{dir}:=\int\rho^2|\nabla\xi|^2dy.
\]

Using

\[
\int \rho^2 y\cdot\nabla f
=
-\int
(3\rho^2+y\cdot\nabla\rho^2)f,
\]

we obtain

\[
\boxed{
P_{dir}
+
\int
(y\cdot\nabla\rho^2)|\nabla\xi|^2dy
=0.
}
\]

---

## 4. Logarithmic-amplitude form

Where `rho>0`,

\[
y\cdot\nabla\rho^2
=
2\rho^2 y\cdot\nabla\log\rho.
\]

Hence

\[
\boxed{
\int
\left(
1+2y\cdot\nabla\log\rho
\right)
\rho^2|\nabla\xi|^2dy
=0.
}
\]

This is the scale-virial form.

---

## 5. Zero-set audit

The direction `xi` is undefined where `rho=0`.

The identity is therefore not justified by simply treating `xi` as a globally smooth map.

Use a standard weighted regularization on the sets

\[
\{\rho>\varepsilon\}
\]

with smooth cutoff in `rho`, derive the identity there, and let `epsilon -> 0`.

The needed weighted quantities are controlled by the smooth vector field `W` because

\[
\rho^2|\nabla\xi|^2
\le
|\nabla W|^2,
\]

and the CE-H projected equation holds distributionally in its `rho^2 nabla xi` form.

Thus the zero-set contribution vanishes in the weighted limit.

This step is recorded as a weighted weak-form argument; no unweighted regularity of `xi` at zeros is assumed.

---

## 6. Infinity boundary audit

M5-567--568 give the critical terminal-tail expansion

\[
W=O(r^{-2}),
\qquad
\nabla W=O(r^{-3}).
\]

Hence the weighted orientation-energy density satisfies

\[
\rho^2|\nabla\xi|^2
\le |\nabla W|^2
=O(r^{-6}).
\]

The dilation boundary terms on `S_R` therefore decay at least as a negative power of `R` and vanish as `R -> infinity`.

Thus the whole-space identity is legitimate on the retained tail class.

---

## 7. Sign consequence

Define the nonnegative orientation measure

\[
d\mu_{dir}
:=
\rho^2|\nabla\xi|^2dy.
\]

If

\[
P_{dir}=\mu_{dir}(\mathbb R^3)>0,
\]

then

\[
\boxed{
\mathbb E_{\mu_{dir}/P_{dir}}
\left[
1+2y\cdot\nabla\log\rho
\right]
=0.
}
\]

Therefore the support of the directional charge cannot remain entirely in a regime where

\[
1+2y\cdot\nabla\log\rho
\]

has one strict sign.

It requires amplitude-slope compensation across the directional-energy population.

---

## 8. Relation to a homogeneous tail

For the critical terminal vorticity scaling

\[
\rho\sim r^{-2},
\]

one has

\[
y\cdot\nabla\log\rho\sim-2,
\]

and therefore

\[
1+2y\cdot\nabla\log\rho\sim-3.
\]

Thus a nonzero global directional charge cannot live exclusively in the asymptotic `r^-2` tail.

Positive compensating contribution must occur at finite/intermediate similarity depth where the amplitude slope is substantially less negative and can cross the critical value

\[
y\cdot\nabla\log\rho=-\frac12.
\]

This further localizes the CE-H directional mechanism to the finite active core.

---

## 9. Updated CE-H directional hard core

The D branch now must satisfy simultaneously

\[
P_{dir}>0,
\]

\[
\int
(1+2y\cdot\nabla\log\rho)
\rho^2|\nabla\xi|^2=0,
\]

and the kappa constraints

\[
\int\kappa|W|^2=-P<0,
\]

\[
\int(y\cdot\nabla\kappa)|W|^2=2P>0.
\]

Hence both vorticity direction and viscous eigenvalue require finite-core transverse/radial compensation.

---

## 10. Firewall

The virial identity does not imply `P_dir=0` because the amplitude-slope factor is sign-indefinite.

A final contradiction would require controlling that sign using the persistent production genealogy or another monotone quantity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
