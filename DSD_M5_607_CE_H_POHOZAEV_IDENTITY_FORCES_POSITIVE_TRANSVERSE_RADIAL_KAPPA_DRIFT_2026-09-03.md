# DSD M5-607 — CE-H Pohozaev identity forces positive enstrophy-weighted transverse radial kappa drift

Date: 2026-09-03

Status: **SCALE-MULTIPLIER IDENTITY / THE GLOBAL CE-H EIGENVALUE EQUATION `Delta W = kappa W` CAN BE PAIRED WITH THE DILATION GENERATOR `y·nabla W` / ON A FINITE BALL AN EXACT BOUNDARY DEFECT APPEARS AND MUST NOT BE DROPPED / THE M5-567--568 TERMINAL CRITICAL-TRACE EXPANSION GIVES `W=O(r^-2)`, `nabla W=O(r^-3)`, `Delta W=O(r^-4)`, WHICH MAKES THE POHOZAEV BOUNDARY DEFECT VANISH AS R→INFINITY / COMBINING WITH `int kappa|W|^2=-P` YIELDS THE EXACT GLOBAL IDENTITY `int (y·nabla kappa)|W|^2 = 2P > 0` / SINCE M5-600 GIVES `W·nabla kappa=0`, THE POSITIVE RADIAL DRIFT IS ENTIRELY TRANSVERSE TO VORTEX LINES / THIS IS A NEW SIGNED SPATIAL CONSTRAINT BUT NOT YET A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. CE-H eigenvalue equation

On CE-H,

\[
\boxed{\Delta W=\kappa W}
\]

and

\[
\boxed{\int\kappa|W|^2=-P.}
\]

M5-600 also gives

\[
\boxed{W\cdot\nabla\kappa=0.}
\]

---

## 2. Finite-ball dilation multiplier

Work first on `B_R` and pair

\[
\Delta W=\kappa W
\]

with

\[
y\cdot\nabla W.
\]

For the left side,

\[
\int_{B_R}\Delta W\cdot(y\cdot\nabla W)
=
\frac12P_R
+
\frac R2
\int_{S_R}
\left(
|\partial_rW|^2-|\nabla_TW|^2
\right)dS.
\]

Here

\[
P_R:=\int_{B_R}|\nabla W|^2dy.
\]

For the right side,

\[
\int_{B_R}\kappa W\cdot(y\cdot\nabla W)
=
-\frac12
\int_{B_R}
(3\kappa+y\cdot\nabla\kappa)|W|^2dy
+
\frac R2
\int_{S_R}\kappa|W|^2dS.
\]

---

## 3. Use the finite-ball eigenvalue energy identity

Integration by parts also gives

\[
\int_{B_R}\kappa|W|^2dy
=
-P_R
+
\int_{S_R}W\cdot\partial_rW\,dS.
\]

Substituting this into the dilation identity yields

\[
\boxed{
\int_{B_R}(y\cdot\nabla\kappa)|W|^2dy
=
2P_R+\mathcal B_R,
}
\]

where the exact boundary defect is

\[
\boxed{
\mathcal B_R
=
-3\int_{S_R}W\cdot\partial_rW\,dS
+
R\int_{S_R}
\left[
\kappa|W|^2
-|\partial_rW|^2
+|\nabla_TW|^2
\right]dS.
}
\]

This defect must not be silently discarded.

---

## 4. Boundary audit using the terminal critical trace

M5-567--568 identify the remote similarity tail with a terminal critical trace and give, on the smooth compact tail class,

\[
U=O(r^{-1}),
\qquad
W=\nabla\times U=O(r^{-2}),
\]

with differentiated expansion

\[
\nabla W=O(r^{-3}),
\qquad
\Delta W=O(r^{-4}).
\]

The last estimate may be used directly in the boundary term as

\[
\kappa|W|^2=W\cdot\Delta W=O(r^{-6}),
\]

so no separate pointwise bound on the quotient `kappa` near zeros of `W` is required.

Consequently,

\[
\int_{S_R}W\cdot\partial_rW=O(R^{-3}),
\]

\[
R\int_{S_R}|\nabla W|^2=O(R^{-3}),
\]

and

\[
R\int_{S_R}\kappa|W|^2=O(R^{-3}).
\]

Hence

\[
\boxed{\mathcal B_R\to0.}
\]

---

## 5. Global Pohozaev identity

Letting `R -> infinity`, `P_R -> P`, and therefore

\[
\boxed{
\int_{\mathbb R^3}
(y\cdot\nabla\kappa)|W|^2dy
=
2P.
}
\]

For every nonzero CE-H state,

\[
\boxed{
\int(y\cdot\nabla\kappa)|W|^2
=2P>0.
}
\]

Together with

\[
\int\kappa|W|^2=-P<0,
\]

we obtain the paired signed constraints

\[
\boxed{
\langle\kappa\rangle_{|W|^2}<0,
\qquad
\langle y\cdot\nabla\kappa\rangle_{|W|^2}>0
}
\]

in unnormalized form.

---

## 6. Vortex-line transverse form

Where `W != 0`, let

\[
\xi=W/|W|.
\]

M5-600 gives

\[
\xi\cdot\nabla\kappa=0.
\]

Decompose the radial vector as

\[
y=(y\cdot\xi)\xi+y_\perp.
\]

Then

\[
y\cdot\nabla\kappa
=y_\perp\cdot\nabla\kappa.
\]

Therefore

\[
\boxed{
\int
(y_\perp\cdot\nabla\kappa)|W|^2dy
=2P>0.
}
\]

The mandatory spatial increase of `kappa` is entirely transverse to the vortex lines.

---

## 7. Geometric interpretation

At each fixed time, `kappa` is constant along each vortex line but the enstrophy-weighted field has a strictly positive mean radial derivative across vortex lines.

Thus a CE-H survivor cannot organize `kappa` as a spatially constant scalar eigenvalue.

Indeed, if `kappa` were constant on all of `R3`, the identity would give `P=0`, hence `W=0`.

The nontrivial survivor requires a genuine transverse family of `kappa` level sets threaded tangentially by vorticity.

---

## 8. Relation to the material-flux cocycle

M5-603 gives, on every persistent material-flux lineage,

\[
\langle\bar\kappa_\Phi\rangle=0.
\]

M5-607 now adds the global spatial requirement

\[
\int(y_\perp\cdot\nabla\kappa)|W|^2=2P>0.
\]

Hence any zero-mean persistent flux lineage must move through or rearrange a spatially nontrivial transverse `kappa` landscape.

The next question is whether the required sign-changing flux oscillation in M5-606 can be compatible with the strict transverse radial organization above without producing a new replacement/separator or a bounded signed radial cocycle.

---

## 9. Firewall

The identity does **not** imply `kappa <= 0` pointwise.

A negative weighted mean together with positive radial derivative is compatible at the scalar level with profiles that are negative in the active core and increase toward zero outward.

Therefore M5-607 is a new rigidity condition, not by itself a contradiction.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
