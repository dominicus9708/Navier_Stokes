# DSD M5-170 — Exact Dirichlet Quotient and Volterra Covariance Gate

Date: 2026-08-27

Status: **CORRECTED P1_B^S FREQUENCY REDUCTION / THE EXACT QUOTIENT DERIVATIVE REMAINS VALID; AFTER THE M5-168 SCALING CORRECTION THE FAST SOURCE IS `LF+N[F]`, SO THE RELATIVE COUPLING CONTRIBUTES `O(1+N)` IN BACKWARD `z` AND `O(z(1+N))=O(e^-tau(1+N))` IN FORWARD `tau` / THE SAME-POINT PRINCIPAL TERM IS A NONNEGATIVE SPECTRAL VARIANCE / ONE VOLTERRA PRINCIPAL-COVARIANCE LAG ESTIMATE REMAINS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Frequency objects

Define

\[
A:=I-4G^2-\Delta_{S^2}>0,
\]

\[
E(z):=\|F(z)\|^2,
\qquad
H(z):=\langle AF(z),F(z)\rangle,
\]

and, when `E>0`,

\[
\boxed{
\mathcal N(z):=\frac{H(z)}{E(z)}.
}
\]

---

## 2. Exact quotient derivative

Since M5-168 gives

\[
F_z=R/z,
\]

we have

\[
E'=\frac2z\operatorname{Re}\langle R,F\rangle,
\qquad
H'=\frac2z\operatorname{Re}\langle AF,R\rangle.
\]

Therefore

\[
\boxed{
\mathcal N_z
=
\frac{2}{zE}
\operatorname{Re}\langle(A-\mathcal N)F,R\rangle.
}
\]

This identity is exact and unaffected by the M5-168 scaling correction.

---

## 3. Corrected stable-kernel decomposition

M5-169 now gives

\[
R(z)
=
\int_0^z\mathcal K(z,\zeta)
\left[
LF(\zeta)+\mathcal N_{rel}F(\zeta)
\right]d\zeta.
\]

Thus

\[
\mathcal N_z
=
\mathcal V_{pr}+\mathcal V_{rel}
\]

with the obvious principal and relative kernel pairings.

---

## 4. Same-point principal covariance

If the normalized kernel is replaced by its leading same-point mass, then

\[
R_{pr}\approx zLF.
\]

Write

\[
L=\nu A_0-6\nu G-2\nu I,
\qquad
A=I+A_0.
\]

The skew term `G` commutes with `A`, and the scalar term cancels in the quotient covariance.

Hence

\[
\boxed{
\operatorname{Re}\langle(A-\mathcal N)F,LF\rangle
=
\nu\left[
\|AF\|^2
-\frac{\langle AF,F\rangle^2}{E}
\right]
\ge0
}
\]

up to the harmless fixed shift convention in `A`.

Therefore the principal same-point contribution satisfies

\[
\boxed{
\mathcal V_{pr}^{same}\ge0.
}
\]

This is the exact Dirichlet-quotient variance sign in backward `z`, or equivalently nonpositive frequency production in forward `tau=-log z`.

---

## 5. Corrected relative-coupling scale

The relative operator now enters the fast source without an extra `z`:

\[
S_{rel}=\mathcal N_{rel}F.
\]

The M5-169 kernel has mass `<=z`, so

\[
\boxed{
\|R_{rel}(z)\|
\le
z\sup_{\zeta\le z}
\|\mathcal N_{rel}F(\zeta)\|.
}
\]

Because the quotient derivative contains `1/z`, the natural backward-`z` contribution is first-order size

\[
\boxed{
O(1+\mathcal N).
}
\]

Using the M5-163/M5-166 commutator estimate, the target lower bound is

\[
\boxed{
\mathcal V_{rel}(z)
\ge
-C(1+\mathcal N(z))
}
\]

once the kernel-local future envelope is converted into the quotient form.

Since

\[
\mathcal N_\tau=-z\mathcal N_z,
\]

this becomes exactly

\[
\boxed{
\mathcal N_\tau
\le
Cz(1+\mathcal N)
=
Ce^{-\tau}(1+\mathcal N),
}
\]

which is the M5-166 scaling.

---

## 6. Remaining principal Volterra covariance gate

The principal kernel uses nearby smaller depths and a unitary genealogical shift:

\[
\int_0^z\mathcal K(z,\zeta)LF(\zeta)d\zeta.
\]

The exact remaining goal is therefore

\[
\boxed{
\mathcal V_{pr}(z)
\ge
-C(1+\mathcal N(z)).
}
\]

The positive same-point variance can be discarded.  Only the negative error produced by normal lag and genealogical shift needs control.

Combined with Section 5 this would give

\[
\boxed{
\mathcal N_z
\ge
-C(1+\mathcal N),
}
\]

or equivalently

\[
\boxed{
\mathcal N_\tau
\le
C e^{-\tau}(1+\mathcal N).
}
\]

Integration would uniformly bound the forward cross-section frequency and contradict the M5-154 necessary parabolic escape for a nonzero statistical flat fiber.

---

## 7. Kernel localization

The exact kernel moments remain

\[
|z-\zeta|=O(z^2),
\qquad
|\log(\zeta/z)|=O(z)
\]

under its normalized exponentially localized measure.

Thus the lag mechanisms carry:

- normal displacement `O(z^2)`;
- genealogical shift `O(z)`;
- coefficient change over the kernel width `O(z)`.

These are small in the forward `tau` asymptotic region, but they must be estimated without using a same-norm derivative/amplitude shortcut.

---

## 8. DSD correction audit

### Formation — GREEN

The quotient derivative is exact and the corrected kernel source matches M5-168/M5-169.

### Axis — GREEN

Backward `z` transfer of size `O(1)` becomes the expected integrable `O(z)` frequency-production rate in forward `tau`.

### Static aggregation — GREEN

The erroneous extra nonlinear factor `z` is removed; no artificial gain remains.

### Dynamics — GREEN / ONE YELLOW LEMMA

The only remaining compatibility edge is the principal Volterra covariance lower bound plus the routine kernel-local version of the first-order commutator estimate.

### Error status

All earlier M5-170 statements using `R_rel=O(z^2 N F)`, `V_rel=O(z...)` in backward `z`, or `N_tau=O(z^2...)` are **REJECTED**.

---

## 9. Next calculation

Prove

\[
\boxed{
\mathcal V_{pr}(z)
\ge-C(1+\mathcal N(z))
}
\]

from kernel localization and stable graph-norm slaving, and package the relative kernel commutator in the same form.

This would complete the M5-166 fast-normal compatibility edge.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
