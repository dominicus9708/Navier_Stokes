# DSD M5-133 — Log-Cylinder Pressure-Poisson Resonance Audit

Date: 2026-08-27

Status: **NSE-SPECIFIC F-GATE REDUCTION / THE LEADING `r^-2` CANONICAL-TAIL PRESSURE IS ELLIPTICALLY DETERMINED BY THE `r^-1` TAIL VELOCITY ON THE TWO-SIDED LOG CYLINDER EXCEPT FOR ONE FINITE-DIMENSIONAL RESONANCE: THE RHO-INDEPENDENT SPHERICAL `l=1` HARMONIC-DIPOLE MODE / THIS MODE MUST NOT BE SET TO ZERO WITHOUT AN INDEPENDENT STRESS-FLUX ARGUMENT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Tail variables

Write the canonical critical tail as

\[
T(Y)=r^{-1}\Phi(\rho,\theta),
\qquad
r=|Y|,
\quad
\rho=\log r,
\quad
\theta=Y/r.
\]

For the leading critical pressure write

\[
P_T(Y)=r^{-2}\Psi(\rho,\theta).
\]

The audited Type-I/pressure-tail bounds place `Phi` and the leading `Psi` in bounded log-cylinder classes on the complete canonical tail.

---

## 2. Pressure Poisson equation

For a divergence-free velocity field,

\[
-\Delta P_T
=
\partial_iT_j\,\partial_jT_i
=:Q_T.
\]

Since `T=r^-1 Phi`,

\[
Q_T=r^{-4}\mathcal Q[\Phi]
\]

for a quadratic differential expression `mathcal Q` involving `Phi`, `partial_rho Phi`, and spherical first derivatives.

For a scalar field of the form

\[
f=r^\alpha\psi(\rho,\theta),
\]

one has in three dimensions

\[
\Delta f
=
r^{\alpha-2}
\left[
\psi_{\rho\rho}
+(2\alpha+1)\psi_\rho
+\alpha(\alpha+1)\psi
+\Delta_{S^2}\psi
\right].
\]

With `alpha=-2`,

\[
\Delta P_T
=
r^{-4}
\left[
\Psi_{\rho\rho}
-3\Psi_\rho
+2\Psi
+\Delta_{S^2}\Psi
\right].
\]

Hence the leading tail pressure satisfies the exact cylinder equation

\[
\boxed{
-\left(
\partial_\rho^2
-3\partial_\rho
+2
+\Delta_{S^2}
\right)\Psi
=
\mathcal Q[\Phi].
}
\]

This is the first elliptic NSE-specific constraint on the canonical tail factor.

---

## 3. Spherical harmonic decomposition

Expand

\[
\Psi(\rho,\theta)
=
\sum_{\ell,m}\psi_{\ell m}(\rho)Y_{\ell m}(\theta),
\]

and similarly for `mathcal Q`.

Since

\[
\Delta_{S^2}Y_{\ell m}
=-\ell(\ell+1)Y_{\ell m},
\]

each mode obeys

\[
\boxed{
-\psi_{\ell m}''
+3\psi_{\ell m}'
+[\ell(\ell+1)-2]\psi_{\ell m}
=q_{\ell m}.
}
\]

The homogeneous characteristic exponents are

\[
\boxed{
\lambda_+=\ell+2,
\qquad
\lambda_-=1-\ell.
}
\]

---

## 4. Two-sided bounded homogeneous modes

The canonical tail is a complete log-cylinder object, so inspect homogeneous solutions bounded for all

\[
\rho\in\mathbb R.
\]

### `ell=0`

The exponents are `2` and `1`. Every nonzero homogeneous solution blows up as `rho -> +infinity`.

### `ell=1`

The exponents are `3` and `0`.

The `e^{3rho}` mode is excluded by boundedness, but the constant mode survives:

\[
\boxed{
\psi_{1m}(\rho)=\text{constant}.
}
\]

### `ell>=2`

The exponents are `ell+2>0` and `1-ell<0`. One mode blows up at `+infinity`, the other at `-infinity`, so no nonzero two-sided bounded homogeneous solution survives.

Therefore

\[
\boxed{
\ker_{\mathrm{bounded}}
\left[
-(\partial_\rho^2-3\partial_\rho+2+\Delta_{S^2})
\right]
=
\operatorname{span}\{Y_{1,-1},Y_{1,0},Y_{1,1}\}.
}
\]

---

## 5. Physical meaning of the resonance

A rho-independent `ell=1` pressure mode has physical form

\[
P_{dip}(Y)
=
r^{-2}(a\cdot\theta)
=
\frac{a\cdot Y}{|Y|^3}.
\]

This is harmonic on the punctured space:

\[
\Delta P_{dip}=0
\qquad(Y\ne0).
\]

It is a pressure dipole / point-stress type mode centered at the singular point.

Its pressure-traction contribution on any sphere is radius-independent:

\[
\int_{|Y|=r}P_{dip}\,n\,dS
=
\int_{S^2}(a\cdot\theta)\theta\,d\theta
=
\frac{4\pi}{3}a.
\]

Thus the surviving harmonic ambiguity is naturally tied to a constant momentum-stress offset.

---

## 6. Relation to M5-124

M5-124 derived a log-scale momentum-stress law of the form

\[
\mathfrak M'(\rho)
=
\int_{S^2}\mathfrak F(\rho,\theta)\,d\theta.
\]

A rho-independent pressure dipole shifts the momentum-stress flux by a constant vector but disappears under `partial_rho`.

Therefore the fact that an invariant mean of `mathfrak M'` vanishes does **not** determine the dipole coefficient.

This explains why the M5-124 net-force route could not by itself remove the final pressure ambiguity.

---

## 7. DSD four-chain audit

### Formation — GREEN

The pressure mode is formed from the actual pressure Poisson equation. No pressure branch is postulated independently.

### Axis — GREEN

Radial log dependence and spherical harmonic rank are separated. The only bounded resonance occurs at spherical rank `ell=1`, zero log frequency.

### Static aggregation — GREEN

The dipole is not added as a new force. It is the homogeneous ambiguity left after solving the elliptic pressure equation for a given tail velocity.

### Dynamics — GREEN

No recurrence is used to set the resonant coefficient to zero. It remains an explicit finite-dimensional degree of freedom.

### Cross-audit — GREEN

The result is consistent with M5-124: stress-flux derivatives cannot see a constant stress offset.

---

## 8. Consequence for the F gate

Modulo the three-dimensional dipole space, the leading critical pressure is a deterministic elliptic functional of the canonical tail velocity:

\[
\boxed{
\Phi
\longmapsto
\Psi\ \mathrm{mod}\ \mathcal H_{dip}^{(1)}.
}
\]

Hence the F gate splits into two much sharper questions:

1. **nonresonant tail pressure:** audit whether the elliptically determined part can support the required recurrent pressure/strain structure;
2. **dipole channel:** determine whether finite-energy unforced ancestry and the strong quotient can carry or cancel a nonzero constant momentum-stress offset.

The dipole coefficient may not be discarded by pressure gauge: an ordinary additive pressure constant is a different mode and does not have critical `r^-2` scaling.

---

## 9. RED firewall

Do not claim

\[
\text{pressure Poisson equation}
\Rightarrow
\Psi=\Psi[\Phi]\text{ uniquely}
\]

without accounting for the bounded `ell=1` dipole kernel.

Do not claim the dipole vanishes merely because the invariant mean momentum-stress derivative is zero.

---

## 10. Next calculation

The next NSE-specific audit is to combine the dipole/nonresonant pressure split with the divergence-free tail and quotient stress tensor, and determine whether the dipole coefficient is an actual conserved/transported fiber variable or must vanish for an unforced finite-energy prelimit.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]