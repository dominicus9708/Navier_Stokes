# DSD M5-233 — Radial-Transport Outward-Sector Locking Gate

Date: 2026-08-30

Parent: `DSD_M5_232_STRAIN_NEGATIVE_MODE_COMPRESSIVE_SPECTRAL_GATE_2026-08-30.md`

Status: **POSITIVE CORRELATION REDUCTION / IF THE RADIAL-TRANSPORT CHANNEL PAYS ONE THIRD OF THE EXACT NEGATIVE CRITICAL BALANCE THEN THE FINITE-DILATE SCALE-PHASE DIFFERENCE MUST LOCK A FIXED FRACTION OF ITS CELL ENERGY TO OUTWARD RADIAL-VELOCITY SECTORS / THIS FORCES A LARGE POSITIVE RADIAL AMPLITUDE THRESHOLD AND A NONZERO OUTWARD-LOCKING RESIDUE / ZERO SPHERICAL FLUX CREATES COMPENSATING INWARD SECTORS BUT DOES NOT CANCEL THE WEIGHTED CORRELATION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact finite-dilate structure

Write

\[
T(r\theta)=r^{-1}\Phi(y,\theta),
\qquad y=\log r.
\]

For a dilation time `h`, put

\[
a:=h/2.
\]

Then the exact tail covariance gives

\[
D_hT(r\theta)
=
r^{-1}\Phi(y-a,\theta).
\]

Hence the relative profile is not arbitrary:

\[
\boxed{
\Psi_h(y,\theta)
=
\Phi(y-a,\theta)-\Phi(y,\theta).
}
\]

Let

\[
\Phi_h(y,\theta):=\Phi(y-a,\theta).
\]

The radial component entering M5-231 is therefore

\[
(\Phi_h)_r(y,\theta)
=
\Phi_r(y-a,\theta).
\]

---

## 2. Radial-transport payer against the actual viscous cell energy

Assume the radial branch in the sharpened M5-232 trichotomy:

\[
\boxed{
\mathcal N_{tr}
=-\frac12
\left\langle
\int_{S^2}
|\Psi_h|^2(\Phi_h)_r
\,d\theta
\right\rangle
\le
-\frac{\nu\mathcal D_h}{3}.
}
\]

Equivalently,

\[
\boxed{
\left\langle
\int_{S^2}
|\Psi_h|^2(\Phi_h)_r
\,d\theta
\right\rangle
\ge
\frac{2\nu}{3}\mathcal D_h.
}
\]

Thus the relative scale-phase energy has positive correlation with **outward** radial velocity.

---

## 3. Positive-sector locking residue

Split

\[
(\Phi_h)_r
=
((\Phi_h)_r)_+
-
((\Phi_h)_r)_-.
\]

Since the negative sector only decreases the signed correlation,

\[
\left\langle
\int
|\Psi_h|^2((\Phi_h)_r)_+
\right\rangle
\ge
\left\langle
\int
|\Psi_h|^2(\Phi_h)_r
\right\rangle.
\]

Therefore

\[
\boxed{
\left\langle
\int_{S^2}
|\Psi_h|^2((\Phi_h)_r)_+
\,d\theta
\right\rangle
\ge
\frac{2\nu}{3}\mathcal D_h.
}
\]

Define the normalized outward-locking coefficient

\[
\boxed{
\mathfrak C_{out}(h)
:=
\frac{
\left\langle
\int |\Psi_h|^2((\Phi_h)_r)_+
\right\rangle
}{\mathcal D_h}.
}
\]

Then every radial-paying finite dilation satisfies

\[
\boxed{
\mathfrak C_{out}(h)
\ge
\frac{2\nu}{3}.
}
\]

This is a scale-invariant correlation certificate.

---

## 4. Radial-amplitude threshold

Use the M5-230 solenoidal cell inequality

\[
\left\langle
\int|\Psi_h|^2
\right\rangle
\le
C_{\rm sol}\mathcal D_h.
\]

Let

\[
U_{r,+}^*
:=
\operatorname*{ess\,sup}_{(y,\theta)}
((\Phi_h)_r)_+.
\]

Then

\[
\mathfrak C_{out}(h)
\le
U_{r,+}^* C_{\rm sol}.
\]

Thus the radial payer forces

\[
\boxed{
U_{r,+}^*
\ge
\frac{2\nu}{3C_{\rm sol}}.
}
\]

Because translation in `y` does not change the hull supremum, this is equivalently a threshold on the original tail:

\[
\boxed{
\| (\Phi_r)_+\|_{L^\infty(cyl)}
\ge
\frac{2\nu}{3C_{\rm sol}}.
}
\]

So the radial branch is another genuinely large-critical-amplitude branch.

---

## 5. Zero spherical flux supplies compensation, not cancellation

For every `y`, incompressibility gives zero physical mass flux:

\[
\boxed{
\int_{S^2}\Phi_r(y,\theta)d\theta=0.
}
\]

Therefore any nonzero positive radial sector is accompanied by a negative radial sector on the same sphere unless `Phi_r=0` identically.

But the transport payment uses the weighted quantity

\[
|\Psi_h|^2\Phi_r.
\]

Hence the positive and negative sectors need not cancel after weighting.

The radial-paying branch is therefore more precisely

\[
\boxed{
\text{zero net mass flux}
+
\text{nonzero inward/outward sector pair}
+
\text{scale-phase difference preferentially occupying outward sectors}.
}
\]

This is stronger than merely requiring a large radial velocity.

---

## 6. Incompressibility derivative consequence

For a degree `-1` divergence-free tail,

\[
\boxed{
\partial_y\Phi_r
+
\Phi_r
+
\operatorname{div}_{S^2}\Phi_\tau
=0.
}
\]

Thus a nontrivial radial sector cannot be completely decoupled from log-radial/angular derivatives.

In particular,

\[
\|\Phi_r\|_{L^2(S^2)}
\le
\|\partial_y\Phi_r\|_{L^2(S^2)}
+
\|\operatorname{div}_{S^2}\Phi_\tau\|_{L^2(S^2)}.
\]

Hence on any set of logarithmic cells carrying a fixed `L2` radial amplitude, at least one of

\[
\boxed{
\partial_y\Phi_r
}
\]

or

\[
\boxed{
\operatorname{div}_{S^2}\Phi_\tau
}
\]

must also carry a fixed derivative amplitude.

This is a **formed derivative witness**, but not a contradiction: a stationary critical tail may maintain `O(1)` normalized derivatives on every scale.

---

## 7. Small-dilation limit

For `a=h/2 -> 0`,

\[
\Psi_h
=
-a\Phi_y+O(a^2)
\]

on the compact smooth hull.

Also

\[
\mathcal D_h
=
a^2\mathcal D_{\Phi_y}+o(a^2).
\]

If the radial-transport branch persists along a sequence `h_n -> 0`, division by `a_n^2` yields the infinitesimal locking inequality

\[
\boxed{
\left\langle
\int_{S^2}
|\Phi_y|^2\Phi_r
\,d\theta
\right\rangle
\ge
\frac{2\nu}{3}
\mathcal D_{\Phi_y}.
}
\]

Thus the **scale generator itself** must preferentially live in outward radial sectors.

This is the infinitesimal stationary analogue of a one-sided turnover correlation.

---

## 8. Symmetric relative equation does not remove the obstruction

The relative stationary equation may equally be written with either state as the advecting background:

\[
-\nu\Delta W+(U\cdot\nabla)W+(W\cdot\nabla)V+\nabla q=0,
\]

or

\[
-\nu\Delta W+(V\cdot\nabla)W+(W\cdot\nabla)U+\nabla q=0.
\]

Averaging gives the symmetric background

\[
M=\frac{U+V}{2}.
\]

The weighted transport term then contains

\[
-\frac14|\Psi|^2(U_r+V_r).
\]

It is still a weighted radial correlation and still has no zero-flux cancellation.

Thus symmetrizing the relative equation does not close the branch.

---

## 9. DSD verdict

### PROVED

A radial-paying survivor requires:

\[
\boxed{
\mathfrak C_{out}(h)\ge2\nu/3,
}
\]

and hence

\[
\boxed{
\|(\Phi_r)_+\|_\infty
\ge2\nu/(3C_{sol}).
}
\]

If the branch persists to infinitesimal dilations, the scale generator obeys the same outward-locking inequality.

### FIREWALL

Zero spherical mass flux does not prohibit such locking.

### ROUTING

The branch is now typed as

\[
\boxed{
\text{large radial sector amplitude}
+
\text{outward scale-phase locking}
+
\text{compensating inward sector}.
}
\]

It is not yet an ordinary material-turnover contradiction because the tail is stationary in physical variables and the correlation is between **scale phase** and radial sectors, not between a tracked finite material packet and a moving boundary.

---

## 10. Next target

Audit the pressure branch

\[
\mathcal N_p\le-\frac{\nu\mathcal D}{3}.
\]

Use the zero spherical mean of `Psi_r` to invert the spherical Laplacian and rewrite the pressure pairing through tangential pressure gradients.  This should determine whether pressure-large necessarily creates a higher-derivative/H channel, or whether a purely critical nonlocal correlation remains.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]