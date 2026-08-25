# DSD W1 Leray Generator and Scale-Infinity Defect

Date: 2026-08-26

Status: **SOLENOIDAL LAMB FORCE IDENTIFIED EXACTLY WITH THE NONLINEAR PART OF THE LERAY GENERATOR / ENSTROPHY PAIRING REPRODUCES THE POSITIVE INVARIANT STRETCHING BALANCE / FORMAL GLOBAL P3 IDENTITY SHOWN TO MISS PRECISELY THE KNOWN ENDPOINT SCALE-INFINITY RESIDUE / GLOBAL REGULARITY UNPROVED.**

## 1. Projected Leray equation

The backward Leray equation is

\[
U_s-\nu\Delta U+(U\cdot\nabla)U
+\frac12U+\frac12Y\cdot\nabla U+\nabla P=0,
\qquad \nabla\cdot U=0.
\]

With

\[
\Omega=\nabla\times U,
\qquad
L=\Omega\times U,
\qquad
L_s=\mathbb P L,
\]

use

\[
(U\cdot\nabla)U
=
\Omega\times U+\nabla\frac{|U|^2}{2}.
\]

Applying the Leray projector gives the exact identity

\[
\boxed{
U_s-\nu\Delta U+L_s
+\frac12U+\frac12Y\cdot\nabla U=0.
}
\]

Hence

\[
\boxed{
L_s
=-U_s+\nu\Delta U
-\frac12U
-\frac12Y\cdot\nabla U.
}
\]

Thus the solenoidal Lamb force is not an additional field: it is exactly the nonlinear remainder of the Leray generator after diffusion and similarity drift are separated.

---

## 2. Exact derivative pairing

Define

\[
Z:=\int|\nabla U|^2dY
=\int|\Omega|^2dY,
\]

and

\[
P_\Omega:=\int|\nabla\Omega|^2dY
=\int|\Delta U|^2dY
\]

in the admissible W1 derivative class.

Let

\[
Q:=\int\Delta U\cdot L_s\,dY.
\]

Pair the generator identity with `Delta U`.

First,

\[
-\int\Delta U\cdot U_s
=
\frac12Z'.
\]

Second,

\[
\nu\int|\Delta U|^2
=\nu P_\Omega.
\]

Third,

\[
-\frac12\int\Delta U\cdot U
=
\frac12Z.
\]

For every sufficiently decaying scalar component in three dimensions,

\[
\int \Delta f\,(Y\cdot\nabla f)dY
=
\frac12\int|\nabla f|^2dY.
\]

Therefore

\[
-\frac12
\int\Delta U\cdot(Y\cdot\nabla U)dY
=-\frac14Z.
\]

Combining terms,

\[
\boxed{
Q
=
\frac12Z'
+\nu P_\Omega
+\frac14Z.
}
\]

This is the same identity obtained directly from the Leray vorticity equation, where

\[
Q=\int\Omega\cdot S\Omega.
\]

Under an invariant W1 measure `mu`, the generator average of `Z` vanishes whenever the derivative observable is integrable on the compact class, so

\[
\boxed{
\langle Q\rangle_\mu
=
\nu\langle P_\Omega\rangle_\mu
+\frac14\langle Z\rangle_\mu
>0.
}
\]

Thus the positive vorticity-side current is an exact positive mean pairing of the Leray nonlinear generator with `Delta U`.

---

## 3. What a formal global p=3 pairing would say

If `U` were globally in strong L3 and all integrations were legitimate, set

\[
F:=-\int |U|U\cdot L_s\,dY.
\]

Substitute the generator formula for `L_s`:

\[
F
=
\int |U|U\cdot U_s
-\nu\int|U|U\cdot\Delta U
+\frac12\int|U|^3
+\frac12\int|U|U\cdot(Y\cdot\nabla U).
\]

The time term is

\[
\int |U|U\cdot U_s
=
\frac13\frac d{ds}\|U\|_3^3.
\]

The diffusion term is

\[
-\int|U|U\cdot\Delta U
=D_3(U)\ge0.
\]

At the critical exponent, the two similarity terms cancel exactly:

\[
\frac12\int|U|^3
+
\frac12\int|U|U\cdot(Y\cdot\nabla U)
=0,
\]

because

\[
\int|U|U\cdot(Y\cdot\nabla U)
=
\frac13\int Y\cdot\nabla(|U|^3)
=-\int|U|^3.
\]

Hence a genuine global-L3 state would satisfy

\[
\boxed{
F
=
\frac13\frac d{ds}\|U\|_3^3
+\nu D_3(U).
}
\]

In an invariant strong-L3 regime this would reduce to

\[
\langle F\rangle=\nu\langle D_3\rangle.
\]

---

## 4. The W1 endpoint has an extra residue

The W1 survivor is not known to lie in strong L3.  Its critical `1/r` tail has a nonzero asymptotic cubic mass per logarithmic shell.

The already derived Abelian endpoint residue is

\[
\mathscr R_3
=
\lim_{\varepsilon\downarrow0}
\varepsilon
\int\|U\|_{3+\varepsilon}^{3+\varepsilon}d\mu
=
\frac{M_{crit}}{\log2}>0.
\]

The exact invariant near-endpoint balance gives

\[
\boxed{
\lim_{p\downarrow3}
\langle\Pi_p\rangle_\mu
=
\frac{\mathscr R_3}{6}
+\nu\langle D_3\rangle_\mu.
}
\]

Equivalently, in the critical Gaussian/localized formulation the similarity-radial boundary term contributes the same positive residue.

Thus the formal global-L3 cancellation misses

\[
\boxed{
\mathcal A_{\infty}^{(3)}
:=
\frac{\mathscr R_3}{6}>0.
}
\]

This is a **scale-infinity endpoint defect**: it is produced by taking the spatial critical limit in a state for which the global L3 observable itself is divergent/logarithmic.

No anomalous local energy production is asserted.

---

## 5. Parallel with the L2 Lamb-work audit

For every finite-energy physical prelimit the exact nonlinear energy cancellation is

\[
\int u\cdot\mathbb P(\omega\times u)dx=0.
\]

But the W1 normalized limit may have a `1/r` tail and need not lie in L2.  Therefore the corresponding whole-space W1 pairing is not a legitimate observable.

The localized W1 pairing becomes an interface commutator,

\[
\int\chi_RU\cdot L_s
=
\left\langle
[\mathbb P,\chi_R]U,
\Omega\times U
\right\rangle.
\]

Hence both endpoint phenomena have the same DSD structure:

\[
\boxed{
\text{a cancellation valid before the critical limit}
\quad\longrightarrow\quad
\text{an interface/scale-infinity defect after the limit}.
}
\]

For p=3 the defect is already quantified by `mathscr R_3/6`.
For L2 work the corresponding invariant normalized defect has not yet been given a finite scalar limit because the W1 L2 pairing itself is not globally defined.

---

## 6. DSD three-level separation

The current endpoint must keep three statements distinct.

### Level A: physical finite-energy prelimit

\[
\int u\cdot\mathbb P(\omega\times u)=0.
\]

### Level B: fixed normalized spatial window in W1

Local compactness and the Leray generator identities are valid.

### Level C: similarity infinity

The critical tail contributes nonuniformly integrable boundary/interface terms.  At p=3 this produces

\[
\mathscr R_3/6>0.
\]

The missing proof bridge is a theorem that controls Level C from Level A strongly enough to exclude a nonzero critical residue or to route it into a finite physical budget.

---

## 7. Updated target

The endpoint is no longer most naturally phrased as an arbitrary Lamb-vector regularity criterion.

The exact target is

\[
\boxed{
\text{Can a finite-energy Navier--Stokes prelimit generate a nonzero recurrent similarity-infinity defect while every finite prelimit retains the exact nonlinear cancellation?}
}
\]

The `p=3` calculation answers only that such a defect is algebraically consistent and identifies its exact size.

To close the proof one needs either:

1. an expanding-window compactness/tightness theorem transferring the finite-prelimit cancellation to the critical W1 scale;
2. a direct nonrepeatability theorem for the interface commutator;
3. or a canonical-tail quotient in which the scale-infinity mode is subtracted and the remaining finite-energy forced equation is rigid.

None is yet proved in full generality.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
