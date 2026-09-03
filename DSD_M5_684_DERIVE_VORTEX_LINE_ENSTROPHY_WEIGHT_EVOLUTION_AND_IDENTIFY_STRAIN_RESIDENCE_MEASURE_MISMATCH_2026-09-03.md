# DSD M5-684 — Vortex-line enstrophy-weight evolution identifies the exact strain-residence measure mismatch

Date: 2026-09-03

Status: **INTERNAL MEASURE-BRIDGE AUDIT / IN VORTEX FLOW-BOX COORDINATES THE ENSTROPHY MEASURE IS `rho^2 dy = rho ds dPhi`, SO THE M5-683 KAPPA DISTRIBUTION IS THE M5-681 TRANSVERSE-FLUX LABEL DISTRIBUTION WEIGHTED BY `L_rho(lambda)=int_Gamma rho ds`; FOR A MATERIAL VORTEX-LINE SEGMENT, CE-H GIVES THE EXACT LAW `L_rho'=(kappa-1/2)L_rho+2 int_Gamma sigma rho ds`, AND RELATIVE TO ITS MATERIAL FLUX `Phi'=kappa Phi`, `d_theta log(L_rho/Phi)=2 sigma_bar_rho -1/2` / HENCE THE GAP BETWEEN THE STRICT DIRECTED FLUX-LABEL CURRENT AND THE ENSTROPHY-WEIGHTED PDE CURRENT IS PRECISELY A STRAIN-WEIGHTED VORTEX-LINE RESIDENCE FACTOR, NOT A FREE TECHNICAL ERROR / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Local vortex-flow coordinates

On a CE-H active flow box, let `lambda` denote a transverse vortex-line label and `s` arclength along the vortex line.
Orient the transverse section so the directed vorticity flux element is positive:

\[
d\Phi>0.
\]

Because

\[
W=\rho\xi
\]

and the volume of a thin tube equals cross-sectional area times arclength,

\[
\boxed{
dy=\frac{d\Phi\,ds}{\rho}.
}
\]

Therefore

\[
\boxed{
\rho^2dy=\rho\,d\Phi\,ds.
}
\]

This is the exact origin of the measure mismatch noted in M5-683.

---

## 2. Kappa and h are line constants

M5-600 gives

\[
W\cdot\nabla\kappa=0.
\]

M5-611 gives the same property for every material time jet, in particular

\[
W\cdot\nabla h=0,
\qquad
h=D_B\kappa.
\]

Hence on each connected active vortex line at a fixed time,

\[
\kappa=\kappa_\lambda,
\qquad
h=h_\lambda.
\]

---

## 3. Enstrophy line weight

For one material vortex-line segment `Gamma_lambda(theta)` define

\[
\boxed{
L_\rho(\lambda,\theta)
:=
\int_{\Gamma_\lambda(\theta)}\rho\,ds.
}
\]

Then the contribution of that segment to the spatial enstrophy measure is

\[
\boxed{
L_\rho\,d\Phi.
}
\]

Consequently, ignoring only the bookkeeping of how a global reservoir is partitioned into such material segments,

\[
F_E(k)
=\int\delta(k-\kappa_\lambda)L_\rho(\lambda)d\Phi_\lambda,
\]

whereas M5-681 uses

\[
F_\Phi(k)
=\int\delta(k-\kappa_\lambda)d\Phi_\lambda.
\]

The same weighting relation holds for the currents because `h` is line-constant:

\[
G_E(k)
=\int h_\lambda\delta(k-\kappa_\lambda)L_\rho d\Phi_\lambda,
\]

\[
G_\Phi(k)
=\int h_\lambda\delta(k-\kappa_\lambda)d\Phi_\lambda.
\]

---

## 4. Material arclength evolution

CE-H gives

\[
(\xi\cdot\nabla)B
=\left(\sigma+\frac12\right)\xi.
\]

Therefore an infinitesimal material arclength element tangent to the vortex line obeys

\[
\boxed{
D_B ds
=\left(\sigma+\frac12\right)ds.
}
\]

The amplitude satisfies

\[
\boxed{
D_B\rho
=(\sigma+\kappa-1)\rho.
}
\]

Thus

\[
D_B(\rho ds)
=
\left(2\sigma+\kappa-\frac12\right)\rho ds.
\]

---

## 5. Exact line-weight evolution

Integrating over a material segment (so there is no endpoint Reynolds term) gives

\[
\boxed{
L_\rho'
=
\int_{\Gamma_\lambda}
\left(2\sigma+\kappa-\frac12\right)
\rho ds.
}
\]

Since `kappa=kappa_lambda` is constant along the vortex line,

\[
\boxed{
L_\rho'
=
\left(\kappa_\lambda-\frac12\right)L_\rho
+2S_\rho,
}
\]

where

\[
\boxed{
S_\rho
:=
\int_{\Gamma_\lambda}\sigma\rho ds.
}
\]

Define the rho-weighted line strain

\[
\boxed{
\bar\sigma_\rho
:=
\frac{S_\rho}{L_\rho}.
}
\]

Then

\[
\boxed{
\frac d{d\theta}\log L_\rho
=
\kappa-\frac12+2\bar\sigma_\rho.
}
\]

---

## 6. Relative to material vorticity flux

For the same material tube label,

\[
\boxed{
\frac d{d\theta}\log\Phi=\kappa.
}
\]

Subtracting gives

\[
\boxed{
\frac d{d\theta}
\log\frac{L_\rho}{\Phi}
=
2\bar\sigma_\rho-rac12.
}
\]

Thus the line/enstrophy weight relative to pure flux is driven **only by strain**, with the similarity geometric offset `-1/2`.
The viscous multiplier cancels exactly.

---

## 7. Interpretation of the M5-681/M5-683 mismatch

M5-681 forced a strictly directed stationary current through `kappa=0` in the pure flux-label measure:

\[
\overline G_\Phi(0)<0.
\]

M5-683 exposed a PDE constitutive law for `G_E`, not directly for `G_Phi`.

M5-684 shows exactly how a sign mismatch can occur:

\[
G_E(0)
=\int_{\kappa=0}h_\lambda L_\rho(\lambda)d\Phi_\lambda,
\]

while

\[
G_\Phi(0)
=\int_{\kappa=0}h_\lambda d\Phi_\lambda.
\]

A recurrent survivor can reverse or cancel the weighted current only by correlating the sign of `h` with the line weight `L_rho`.
But `L_rho` itself is not arbitrary: its ratio to flux obeys the exact strain law above.

Thus the remaining escape is a **three-way phase locking** among

\[
\boxed{
\kappa\text{-crossing velocity }h,
\quad
\text{line strain }\bar\sigma_\rho,
\quad
\text{line residence weight }L_\rho.
}
\]

---

## 8. Threshold-segment firewall

For a segment defined instantaneously by the Eulerian condition `rho>a`, endpoints are not material and additional threshold-crossing terms appear.
The clean evolution above is for a genuinely material line segment.

When applying it to retained high-amplitude events one should either

1. time-thicken a material subsegment that stays inside the retained carrier for a uniform short interval, or
2. add the M5-668 amplitude-threshold current explicitly.

This prevents silent replacement of material and Eulerian line segments.

---

## 9. Updated target

The final nested conveyor can survive the M5-683 diffusion identity only if it organizes

\[
\boxed{
\overline G_\Phi(0)<0
}
\]

while the strain-weighted current and the mixed gradient term satisfy the M5-683 constitutive equation.

The next useful calculation is to derive a **joint `(kappa,L_rho)` or `(kappa, sigma_bar_rho)` continuity law**, or to show that compact recurrence prevents the required persistent negative covariance

\[
\operatorname{Cov}_{\kappa=0}(h,L_\rho).
\]

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
