# DSD M5-48 — Cell Infinity versus Original Physical Infinity Audit

Date: 2026-08-27

Status: **DSD COORDINATE AUDIT / THE STATIC `1/r` RESERVOIR OF THE PUMP-TO-DEFECT CELL LIVES AT INFINITY OF THE BLOW-UP COORDINATE, NOT AT LARGE DISTANCE IN THE ORIGINAL PHYSICAL DOMAIN / IT REPRESENTS CROSS-RADIUS ANCESTRY INSIDE A SHRINKING NEIGHBORHOOD OF THE SINGULAR POINT / GLOBAL REGULARITY UNPROVED.**

## 1. Blow-up coordinate

For the pump sequence,

\[
V_j(z,\sigma)
=L_j^{-1}
 u\!\left(
 X_*+\frac z{L_j},
 t_j+\frac\sigma{L_j^2}
 \right),
\qquad
L_j\to\infty.
\]

Thus

\[
\boxed{z=L_j(x-X_*).}
\]

A radius `R_z` in the ancient cell corresponds to original physical radius

\[
\boxed{
r_{phys}=\frac{R_z}{L_j}.
}
\]

For every fixed cell radius, this physical radius tends to zero as `j -> infinity`.

---

## 2. Meaning of `z -> infinity`

The limit operation is ordered:

1. first pass `j -> infinity` at fixed `z` to obtain the blow-up cell;
2. then inspect `|z| -> infinity` inside that limit object.

Therefore `z -> infinity` describes physical radii satisfying schematically

\[
L_j^{-1}\ll r_{phys}\ll r_{parent}
\]

before the limit, not points traveling to infinite distance in the original fluid.

The ancient static tail is the image of a hierarchy of intermediate physical radii around `X_*` that are expanded by the blow-up scaling.

---

## 3. Correct interpretation of the static reservoir

M5-42 gives

\[
V_{tail}(z)
\sim\frac1{|z|}\Phi(\theta,\log|z|).
\]

This should be interpreted as

\[
\boxed{
\text{cross-radius critical ancestry in the singular neighborhood}
}
\]

rather than

\[
\text{energy supplied from original physical infinity}.
\]

The word `reservoir` refers to the blow-up-cell boundary state, not an external physical energy source.

---

## 4. Relation to the earlier similarity-current audit

This is analogous to the earlier correction

\[
\text{similarity log-radius current}
\neq
\text{material radial transport}.
\]

Likewise here

\[
\boxed{
\text{ancient-cell spatial infinity}
\neq
\text{original physical spatial infinity}.
}
\]

Both distinctions are coordinate/description audits required by DSD.

---

## 5. Pump-to-defect history after correction

The correct physical picture is

\[
\boxed{
\begin{array}{c}
\text{nested shrinking physical radii around }X_*\\
\Downarrow\\
\text{expanded into the ancient cell as a static `1/r` outer ancestry}\\
\Downarrow\\
\text{finite-amplitude pump at the anchor scale}\\
\Downarrow\\
\text{terminal critical defect}.
\end{array}
}
\]

No claim of energy transfer from arbitrarily distant original locations is made.

---

## 6. Consequence for proof search

A closure theorem must therefore constrain **cross-scale coherence near the singular point**, not spatial decay at original physical infinity.

This further supports the current M5 target:

\[
\boxed{
\text{same-trajectory multiscale rigidity near }X_*
}
\]

rather than a far-field energy-supply argument.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
