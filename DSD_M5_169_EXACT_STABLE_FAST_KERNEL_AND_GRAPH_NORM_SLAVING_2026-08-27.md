# DSD M5-169 — Exact Stable Fast Kernel and Graph-Norm Slaving

Date: 2026-08-27

Status: **CORRECTED P1_B^S FAST COMPATIBILITY / THE FLAT-SELECTED FAST DEFECT IS AN EXACT VOLTERRA AVERAGE WITH TOTAL KERNEL NORM AT MOST `z`; AFTER THE M5-168 CORRECTION THE SOURCE IS `LF+N[F]`, SO `R=zF_z` IS SLAVED TO `z(LF+N[F])` / THE KERNEL ITSELF CREATES NO EXTRA CROSS-FREQUENCY DERIVATIVE LOSS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Corrected fast equation

M5-168 now gives

\[
4\nu zR_z
+\left(\frac1z+6\nu+8\nu G\right)R
=
S(z),
\]

with

\[
\boxed{S(z):=LF(z)+\mathcal N[F(z)]}.
\]

The earlier `LF+zN[F]` source was caused by the corrected M5-168 scaling error and is rejected.

---

## 2. Integrating factor

Divide by `4nu z` and define

\[
\mathcal M(z)
=
e^{-1/(4\nu z)}z^{3/2}z^{2G}.
\]

Since `G` is skew-adjoint,

\[
\|z^{2G}f\|=\|f\|.
\]

Then

\[
\frac d{dz}(\mathcal M R)
=
\mathcal M\frac{S(z)}{4\nu z}.
\]

The flat branch removes the growing homogeneous mode, so

\[
\boxed{
R(z)
=
\int_0^z\mathcal K(z,\zeta)S(\zeta)d\zeta,
}
\]

where

\[
\mathcal K(z,\zeta)
=
\frac1{4\nu\zeta}
\exp\left[
\frac1{4\nu z}-\frac1{4\nu\zeta}
\right]
\left(\frac\zeta z\right)^{3/2}
\left(\frac\zeta z\right)^{2G}.
\]

---

## 3. Kernel mass

Exactly as before,

\[
\boxed{
\int_0^z\|\mathcal K(z,\zeta)\|d\zeta
=
\frac z{4\nu}
\int_0^\infty
e^{-t/(4\nu)}(1+zt)^{-5/2}dt
\le z.
}
\]

The normalized mass divided by `z` tends to one as `z->0`.

---

## 4. Corrected slaving estimate

Therefore

\[
\boxed{
\|R(z)\|
\le
z\sup_{0<\zeta\le z}
\|LF(\zeta)+\mathcal N F(\zeta)\|.
}
\]

Since `R=zF_z`,

\[
\boxed{
\|F_z(z)\|
\le
\sup_{0<\zeta\le z}
\|LF(\zeta)+\mathcal N F(\zeta)\|.
}
\]

Thus the forward `tau` derivative obeys the expected schematic scaling

\[
F_\tau=-zF_z
=O\bigl(z(LF+\mathcal N F)\bigr).
\]

---

## 5. Graph-norm version

Let

\[
A:=I-4G^2-\Delta_{S^2}.
\]

The kernel commutes with Borel functions of `G` and the spherical spectral operator. Hence, for every finite graph order `m`,

\[
\boxed{
\|A^{m/2}R(z)\|
\le
z\sup_{0<\zeta\le z}
\|A^{m/2}(LF+\mathcal N F)(\zeta)\|.
}
\]

The fast kernel does not add a new derivative order.

The only projector-noncommuting derivative loss is the genuine first-order relative operator `N`, already controlled by M5-163/M5-166.

---

## 6. Localization moments

With

\[
t=\zeta^{-1}-z^{-1},
\]

the scalar kernel measure is exponentially localized in `t`.

Consequently every finite kernel moment satisfies the schematic bounds

\[
|z-\zeta|=O(z^2),
\qquad
|\log(\zeta/z)|=O(z).
\]

These are the small parameters for the remaining Volterra-lag covariance estimate.

---

## 7. DSD correction audit

### Formation — GREEN

The kernel derivation is unchanged; only its source is corrected.

### Axis — GREEN

The `z` kernel mass supplies one factor `z`, which becomes the expected `e^-tau` factor after `F_tau=-zF_z`.

### Static aggregation — GREEN

There is no fictitious second small factor multiplying the nonlinear relative coupling.

### Dynamics — GREEN

The exact slaving remains valid in every audited graph norm.

### Error status

All statements in the earlier version that used `LF+zN[F]` or inferred an extra nonlinear `z` are **REJECTED**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
