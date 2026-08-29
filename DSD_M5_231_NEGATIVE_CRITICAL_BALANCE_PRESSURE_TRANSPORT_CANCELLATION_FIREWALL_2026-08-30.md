# DSD M5-231 — Negative Critical-Balance Pressure / Transport Cancellation Firewall

Date: 2026-08-30

Parent: `DSD_M5_230_SCALE_INVARIANT_R_WEIGHTED_RELATIVE_ENERGY_AND_NEGATIVE_CRITICAL_BALANCE_2026-08-30.md`

Status: **CHANNEL-SEPARATION AUDIT / ZERO SPHERICAL MASS FLUX DOES NOT CANCEL THE RADIAL-TRANSPORT TERM BECAUSE IT IS WEIGHTED BY `|Psi|^2` / THE RELATIVE PRESSURE SOLVES AN EXACT CROSS-GRADIENT POISSON EQUATION BUT ITS PAIRING WITH THE RADIAL RELATIVE MODE HAS NO SIGN AND DOES NOT VANISH FROM ZERO FLUX / THEREFORE M5-230'S STRICT NEGATIVE CRITICAL PAYMENT CANNOT YET BE ASSIGNED TO THE STRAIN CHANNEL ALONE / PRESSURE AND RADIAL TRANSPORT REMAIN GENUINE LARGE-AMPLITUDE CRITICAL CORRELATION CHANNELS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Negative balance from M5-230

For

\[
U=D_{h_*}T,
\qquad
V=T,
\qquad
W=U-V=r^{-1}\Psi,
\]

M5-230 proves

\[
\boxed{
\nu\langle\mathcal D_\Psi\rangle
+
\langle\mathcal N_{crit}\rangle
=0
}
\]

with

\[
\boxed{
\langle\mathcal D_\Psi\rangle
\ge d_D^*>0
}
\]

and

\[
\mathcal N_{crit}
=
\int_{S^2}
\left[
\Psi^T\mathcal S_\Phi\Psi
-
\frac12|\Psi|^2\Phi_{h,r}
-
\pi\Psi_r
\right]d\theta.
\]

Hence

\[
\boxed{
\langle\mathcal N_{crit}\rangle
\le-\nu d_D^*<0.
}
\]

The question is whether the last two terms vanish after spherical/log averaging.

---

## 2. Zero spherical flux identities

Each stationary tail is divergence free and has zero mass flux through spheres:

\[
\boxed{
\int_{S^2}\Phi_r(y,\theta)d\theta=0.
}
\]

The same holds for the dilate:

\[
\int_{S^2}\Phi_{h,r}d\theta=0,
\]

and for the difference:

\[
\boxed{
\int_{S^2}\Psi_r d\theta=0.
}
\]

These are exact scalar mean constraints.

---

## 3. Radial transport does not cancel

The radial transport term is

\[
\boxed{
\mathcal N_{tr}(y)
=-\frac12
\int_{S^2}
|\Psi(y,\theta)|^2
\Phi_{h,r}(y,\theta)d\theta.
}
\]

Zero flux supplies only

\[
\int_{S^2}\Phi_{h,r}=0.
\]

It does **not** imply

\[
\int_{S^2}|\Psi|^2\Phi_{h,r}=0.
\]

Indeed `|Psi|^2` can correlate with the positive and negative radial sectors.

Thus

\[
\boxed{
\text{zero spherical flux}
\not\Rightarrow
\mathcal N_{tr}=0.
}
\]

This is the stationary finite-dilate analogue of the radial Carleman-weight firewall encountered earlier in the dynamic critical-tail audit.

---

## 4. Exact relative pressure Poisson equation

The relative stationary equation is

\[
-\nu\Delta W
+(U\cdot\nabla)W
+(W\cdot\nabla)V
+\nabla q
=0.
\]

Take divergence.

Using

\[
\nabla\cdot U
=
\nabla\cdot V
=
\nabla\cdot W
=0,
\]

one gets

\[
\boxed{
-\Delta q
=
(\partial_iU_j)(\partial_jW_i)
+
(\partial_iW_j)(\partial_jV_i).
}
\]

Equivalently, from the whole-space pressure representation,

\[
q
=
\mathcal R_i\mathcal R_j
\left(
U_iW_j+W_iV_j
\right)
\]

modulo the fixed pressure gauge.

Thus pressure is a genuine nonlocal cross-correlation of the background and the finite-dilate mode.

---

## 5. Pressure term also does not cancel from zero flux

The pressure contribution in M5-230 is

\[
\boxed{
\mathcal N_p(y)
=-
\int_{S^2}
\pi(y,\theta)
\Psi_r(y,\theta)d\theta.
}
\]

Although

\[
\int_{S^2}\Psi_r=0,
\]

there is no reason for

\[
\int_{S^2}\pi\Psi_r=0.
\]

Only the angular mean of `Psi_r` vanishes; `pi` is nonconstant and dynamically correlated with `Psi` through the pressure Poisson equation.

Therefore

\[
\boxed{
\text{zero flux of }W
\not\Rightarrow
\mathcal N_p=0.
}
\]

---

## 6. Pressure is not an independent free field, but it remains an independent correlation channel

The Poisson formula means pressure does not add a new degree of freedom beyond `(U,V,W)`.

However eliminating it algebraically produces a nonlocal quadratic form rather than a sign-definite expression.

Schematically,

\[
\mathcal N_p
=
\left\langle
\mathcal R_i\mathcal R_j
(U_iW_j+W_iV_j),
\partial_r W
\right\rangle_{S^2/log}.
\]

Calderon--Zygmund estimates may bound this form in terms of critical background and derivative norms, but do not give a universal sign.

Thus

\[
\boxed{
\text{pressure determined by velocity}
\not\Rightarrow
\text{pressure pairing negligible}.
}
\]

---

## 7. Large-amplitude form bound only

On the compact critical tail class one has finite coefficient bounds of the schematic form

\[
|\Phi|+|\nabla_{cyl}\Phi|+|\Pi|
\le C_{tail}.
\]

Therefore the transport and strain pieces obey critical quadratic bounds, and the pressure Poisson equation supplies a corresponding critical nonlocal bound.

After the solenoidal cell coercivity of M5-230, one obtains only a schematic estimate

\[
\boxed{
|\langle\mathcal N_{crit}\rangle|
\le
C(C_{tail})
\langle\mathcal D_\Psi\rangle.
}
\]

Combining with

\[
\nu\langle\mathcal D_\Psi\rangle
=-\langle\mathcal N_{crit}\rangle
\]

shows that a survivor must lie outside any coefficient regime where

\[
C(C_{tail})<\nu.
\]

This is another perturbative amplitude gate, not an arbitrary-large closure.

---

## 8. Why Betchov/positive-middle strain cannot yet absorb the whole payment

The strain part is

\[
\mathcal N_S
=
\int_{S^2}
\Psi^T\mathcal S_\Phi\Psi.
\]

M5-230 proves negativity only for the **sum**

\[
\mathcal N_S+\mathcal N_{tr}+\mathcal N_p.
\]

Without separate estimates showing

\[
\langle\mathcal N_{tr}+\mathcal N_p\rangle\ge0
\]

or at least that these terms are too small to pay `nu d_D^*`, one cannot conclude

\[
\langle\mathcal N_S\rangle<0.
\]

Therefore the existing Betchov/eigenframe/projective machinery cannot yet be invoked as if it had received the full negative payment.

---

## 9. DSD firewall

The following cancellations are RED:

\[
\boxed{
\int\Phi_r=0
\Rightarrow
\int|\Psi|^2\Phi_r=0,
}
\]

and

\[
\boxed{
\int\Psi_r=0
\Rightarrow
\int\pi\Psi_r=0.
}
\]

Likewise

\[
\boxed{
q=\mathcal R_i\mathcal R_j(\cdots)
\Rightarrow
\text{pressure pairing has a sign}
}
\]

is false without another structural theorem.

---

## 10. Updated large-stationary certificate

The surviving fixed-force stationary branch must satisfy the exact three-channel balance

\[
\boxed{
\left\langle
\mathcal N_S
+
\mathcal N_{tr}
+
\mathcal N_p
\right\rangle
\le
-\nu d_D^*<0.
}
\]

Thus at least one of the three channels has negative mean of fixed size on a finite partition:

\[
\boxed{
\langle\mathcal N_S\rangle
\le-\frac{\nu d_D^*}{3}
\quad\lor\quad
\langle\mathcal N_{tr}\rangle
\le-\frac{\nu d_D^*}{3}
\quad\lor\quad
\langle\mathcal N_p\rangle
\le-\frac{\nu d_D^*}{3}.
}
\]

This finite trichotomy is valid even though no individual channel is yet excluded.

---

## 11. Next target

The stationary endpoint is now reduced to three explicit negative-payment mechanisms:

1. **strain-negative mode** — attack by eigenframe/Hardy/Betchov structure;
2. **radial-transport correlation** — attack using recurrent radial sectors and zero-flux compensation;
3. **pressure-radial correlation** — attack through the pressure Poisson/CZ structure.

A finite-partition argument allows one channel to be selected on a positive logarithmic density of scales.

This is the appropriate next level; no cancellation is assumed merely from zero spherical means.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]