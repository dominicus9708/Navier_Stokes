# DSD M5-671 — Miller strain-vorticity identity forces a CE-H spectral-gap compatibility law

Date: 2026-09-03

Status: **EXTERNAL-IDENTITY / INTERNAL CE-H REDUCTION / A KNOWN WHOLE-SPACE DIVERGENCE-FREE IDENTITY `int (-Delta Sigma):(W tensor W)=0` CAN BE COMBINED WITH THE CE-H EIGENLINE `Sigma W=sigma W` TO GIVE THE EXACT SPECTRAL-GAP LAW `(1/2)int rho^2 Delta sigma = int rho^2 sum_i partial_i xi · (sigma I-Sigma) partial_i xi` / COMBINING FURTHER WITH `Delta W=kappa W` GIVES `int sigma kappa rho^2 = -int sigma|grad rho|^2 - int rho^2 sum_i partial_i xi·Sigma partial_i xi` / THESE ARE GENUINELY PDE-SPECIFIC CONSTRAINTS ABSENT FROM THE M5-653 MULTI-SHEET TOY OSCILLATOR / NO SIGN CONTRADICTION IS YET OBTAINED IN THE INDEFINITE MIDDLE-EIGENVALUE CASE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. External strain-vorticity identity

For sufficiently regular divergence-free whole-space velocity fields, a strain-vorticity identity due to Miller gives

\[
\boxed{
\int_{\mathbb R^3}
(-\Delta\Sigma):(W\otimes W)\,dy
=0.
}
\]

Equivalently,

\[
\boxed{
\int W\cdot(\Delta\Sigma)W\,dy=0.
}
\]

This is treated as an external exact identity; the remaining reductions below are internal.

---

## 2. Differentiate the CE-H strain eigenline

CE-H gives

\[
\boxed{\Sigma W=\sigma W.}
\]

Apply the Laplacian:

\[
\Delta(\Sigma W)
=(\Delta\Sigma)W
+2\partial_i\Sigma\,\partial_iW
+\Sigma\Delta W.
\]

On the other hand,

\[
\Delta(\sigma W)
=(\Delta\sigma)W
+2\partial_i\sigma\,\partial_iW
+\sigma\Delta W.
\]

Since `Sigma W=sigma W`, the last terms coincide after using `Delta W=kappa W` and cancel.

Thus

\[
\boxed{
(\Delta\Sigma)W
=(\Delta\sigma)W
+2\nabla\sigma\cdot\nabla W
-2\partial_i\Sigma\,\partial_iW.
}
\]

---

## 3. Pair with W and integrate

Take the scalar product with `W`.

The first two scalar terms are

\[
(\Delta\sigma)\rho^2
+2\partial_i\sigma\,W\cdot\partial_iW
=
(\Delta\sigma)\rho^2
+\nabla\sigma\cdot\nabla(\rho^2).
\]

Their whole-space integral vanishes by integration by parts.

The external identity therefore yields

\[
\boxed{
\int
W\cdot(\partial_i\Sigma)\partial_iW\,dy
=0.
}
\]

---

## 4. Differentiate the eigenline once

Differentiate

\[
\Sigma W=\sigma W
\]

in coordinate `i`:

\[
(\partial_i\Sigma)W
+\Sigma\partial_iW
=(\partial_i\sigma)W
+\sigma\partial_iW.
\]

Pair with `partial_i W` and use symmetry of `partial_i Sigma`:

\[
W\cdot(\partial_i\Sigma)\partial_iW
=(\partial_i\sigma)W\cdot\partial_iW
+\sigma|\partial_iW|^2
-\partial_iW\cdot\Sigma\partial_iW.
\]

Summing and integrating gives

\[
\boxed{
\frac12\int\rho^2\Delta\sigma\,dy
=
\int
\left[
\sigma|\nabla W|^2
-
\sum_i\partial_iW\cdot\Sigma\partial_iW
\right]dy.
}
\]

---

## 5. Magnitude-direction decomposition

Write

\[
W=\rho\xi,
\qquad |\xi|=1.
\]

Then

\[
\partial_iW
=(\partial_i\rho)\xi
+\rho\partial_i\xi,
\qquad
\xi\cdot\partial_i\xi=0.
\]

Because `Sigma xi=sigma xi`, the magnitude-gradient pieces cancel in the bracket:

\[
\sigma|\partial_iW|^2
-
\partial_iW\cdot\Sigma\partial_iW
=
\rho^2
\partial_i\xi\cdot(\sigma I-\Sigma)\partial_i\xi.
\]

Hence

\[
\boxed{
\frac12\int\rho^2\Delta\sigma\,dy
=
\int\rho^2
\sum_i
\partial_i\xi\cdot(\sigma I-\Sigma)\partial_i\xi\,dy.
}
\]

This is the CE-H spectral-gap compatibility law.

---

## 6. Eigenvalue interpretation

Let the transverse strain eigenvalues be `lambda_2,lambda_3` and decompose each `partial_i xi` into the corresponding transverse eigendirections.

Then the right side is

\[
\int\rho^2
\sum_i
\left[
(\sigma-\lambda_2)|\partial_i\xi\cdot e_2|^2
+
(\sigma-\lambda_3)|\partial_i\xi\cdot e_3|^2
\right]dy.
\]

Thus:

- if `sigma` is the top strain eigenvalue, the integrand is nonnegative;
- if `sigma` is the bottom eigenvalue, it is nonpositive;
- if `sigma` is the middle eigenvalue, it is indefinite.

The current hard branch is not known to remain in one of the first two sign-definite classes.

---

## 7. Coupling to the kappa eigenfield

CE-H also gives

\[
\Delta W=\kappa W.
\]

Hence

\[
\int\sigma\kappa\rho^2dy
=
\int\sigma W\cdot\Delta Wdy.
\]

Integrating by parts,

\[
\int\sigma\kappa\rho^2
=
-\int\sigma|\nabla W|^2
+\frac12\int\rho^2\Delta\sigma.
\]

Insert the spectral-gap identity.

The direction terms simplify, yielding

\[
\boxed{
\int\sigma\kappa\rho^2dy
=
-\int\sigma|\nabla\rho|^2dy
-
\int\rho^2
\sum_i
\partial_i\xi\cdot\Sigma\partial_i\xi\,dy.
}
\]

This is a direct strain-viscosity covariance identity for CE-H.

---

## 8. Relation to the multi-sheet toy firewall

The M5-653 oscillator prescribes only scalar histories `kappa(theta)` and `h(theta)` with flux recurrence.

It has no strain tensor `Sigma`, no direction-gradient field `grad xi`, and no elliptic eigenfield equation.

Therefore it does not satisfy or test the two boxed identities above.

Any future contradiction derived from these identities would genuinely use Navier--Stokes/CE-H structure rather than quotient kinematics alone.

---

## 9. Current limitation

The spectral-gap law is not sign definite when `sigma` is the middle strain eigenvalue.

Moreover the weighted Laplacian term

\[
\int\rho^2\Delta\sigma
\]

has no universal sign on the recurrent hard hull.

Thus the identity is a new compatibility condition, not yet a contradiction.

---

## 10. Next target

The natural next split is to decompose the fixed high-amplitude production layer according to whether the vorticity eigenline corresponds to the top or middle strain eigenvalue.

The bottom eigenvalue cannot carry positive axial stretching.

A top-aligned production population pays a sign-definite spectral-gap term, while a positive middle-aligned population can be compared with known middle-eigenvalue regularity criteria and with the Betchov determinant identity already derived in M5-608--609.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
