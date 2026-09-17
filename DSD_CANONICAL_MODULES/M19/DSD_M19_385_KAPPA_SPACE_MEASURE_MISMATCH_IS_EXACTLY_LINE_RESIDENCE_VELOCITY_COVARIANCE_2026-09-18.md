# M19-385 — The kappa-space measure mismatch is exactly a line-residence / coefficient-velocity covariance

Date: 2026-09-18

Status: **NEW CANONICAL SYNTHESIS / M5-681 + M5-683 + M19-337. THE DIRECTED MATERIAL-FLUX CURRENT IN KAPPA SPACE AND THE ENSTROPHY-WEIGHTED PDE CURRENT DIFFER BY ONE EXACT CONDITIONAL COVARIANCE: THE VORTEX-LINE RESIDENCE WEIGHT `L_chi=int chi(rho) rho ds` CORRELATED WITH THE COEFFICIENT VELOCITY `h=D_B kappa`. THEREFORE FAILURE TO TRANSFER THE STRICT MATERIAL-FLUX SIGN `G_Phi(0)<0` TO THE SPATIAL PDE CURRENT IS NOT AN UNSTRUCTURED MEASURE MISMATCH; IT REQUIRES A QUANTITATIVE POSITIVE RESIDENCE--VELOCITY PHASE BIAS AT `kappa=0` (OR DEGENERATION OF THE CONDITIONAL DISINTEGRATION). THIS CONNECTS THE OLD M5-683 FIREWALL DIRECTLY TO THE M19-337 LINE-RESIDENCE ARCHITECTURE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material-flux kappa distribution

On the fixed base transversal material label space, let `dmu_Phi` denote the current positive oriented flux measure.

M5-681 defines

\[
F_\Phi(k)
:=
\int \delta(k-\kappa_\lambda)d\mu_\Phi(\lambda),
\]

and

\[
G_\Phi(k)
:=
\int h_\lambda\delta(k-\kappa_\lambda)d\mu_\Phi(\lambda),
\qquad
h=D_B\kappa.
\]

On the recurrent hard survivor,

\[
\boxed{\overline G_\Phi(0)<0.}
\]

This is the strict directed material-flux conveyor from positive-kappa amplification toward negative-kappa consumption.

---

## 2. Spatial/enstrophy-weighted distribution in flux coordinates

M5-683 uses

\[
F_E^\chi(k)
=
\int \delta(k-\kappa)\chi(\rho)\rho^2dy,
\]

\[
G_E^\chi(k)
=
\int h\,\delta(k-\kappa)\chi(\rho)\rho^2dy.
\]

In a vortex flow box,

\[
dy=\frac{d\Phi\,ds}{\rho}.
\]

Because `kappa` and `h` are constant along a vortex line at fixed time on CE-H,

\[
W\cdot\nabla\kappa=0,
\qquad
W\cdot\nabla h=0,
\]

we may integrate the spatial weight along each material line.

Define the cutoff line-residence weight

\[
\boxed{
L_\chi(\lambda)
:=
\int_{\Gamma_\lambda}
\chi(\rho)\rho\,ds.
}
\]

Then exactly

\[
\boxed{
F_E^\chi(k)
=
\int
L_\chi(\lambda)
\delta(k-\kappa_\lambda)
\,d\mu_\Phi(\lambda),
}
\]

and

\[
\boxed{
G_E^\chi(k)
=
\int
L_\chi(\lambda)h_\lambda
\delta(k-\kappa_\lambda)
\,d\mu_\Phi(\lambda).
}
\]

This is the cutoff version of the M19-337 Radon--Nikodym bridge.

---

## 3. Conditional flux law on one kappa level

Assume first

\[
F_\Phi(k)>0.
\]

Disintegrate the flux measure conditionally on the coefficient level `kappa=k` and write

\[
\mathbb E_k^\Phi[\cdot]
\]

for the conditional expectation.

Then

\[
F_E^\chi(k)
=
F_\Phi(k)
\mathbb E_k^\Phi[L_\chi],
\]

\[
G_\Phi(k)
=
F_\Phi(k)
\mathbb E_k^\Phi[h],
\]

and

\[
G_E^\chi(k)
=
F_\Phi(k)
\mathbb E_k^\Phi[L_\chi h].
\]

Use

\[
\mathbb E[Lh]
=
\mathbb E[L]\mathbb E[h]
+
\operatorname{Cov}(L,h).
\]

Therefore

\[
\boxed{
G_E^\chi(k)
=
\bar L_\chi(k)\,G_\Phi(k)
+
F_\Phi(k)
\operatorname{Cov}_k^\Phi(L_\chi,h),
}
\]

where

\[
\boxed{
\bar L_\chi(k)
:=
\mathbb E_k^\Phi[L_\chi].
}
\]

This identity is exact.

---

## 4. Zero-level current formula

At `k=0`, whenever the conditional level is nontrivial,

\[
\boxed{
G_E^\chi(0)
=
\bar L_0\,G_\Phi(0)
+
F_\Phi(0)
\operatorname{Cov}_0^\Phi(L_\chi,h).
}
\]

M5-681 gives

\[
G_\Phi(0)<0.
\]

Hence the natural first term is strictly negative.

If the spatial current fails to inherit that sign, i.e.

\[
G_E^\chi(0)\ge0,
\]

then necessarily

\[
\boxed{
\operatorname{Cov}_0^\Phi(L_\chi,h)
\ge
-
\frac{\bar L_0}{F_\Phi(0)}
G_\Phi(0)
>0.
}
\]

Thus a sign reversal or cancellation requires **positive correlation between long/high-amplitude line residence and upward kappa velocity** at the zero-coefficient interface.

---

## 5. Quantitative robust-sign branch

More generally, if for some `0<=eta<1`

\[
F_\Phi(0)
\left|
\operatorname{Cov}_0^\Phi(L_\chi,h)
\right|
\le
\eta\,
\bar L_0|G_\Phi(0)|,
\]

then

\[
\boxed{
G_E^\chi(0)
\le
-(1-\eta)
\bar L_0|G_\Phi(0)|<0.
}
\]

Therefore the material-flux sign transfers robustly to the spatial PDE current unless the residence--velocity covariance is of the same order as the directed current itself.

---

## 6. Relation to M19-337

M19-337 used the uncut residence weight

\[
L_1(\lambda)=\int_{\Gamma_\lambda}\rho ds
\]

to obtain

\[
\boxed{
 d\Pi
=
\frac{L_1}{\bar L_1}dp_\Phi.
}
\]

The present result is the dynamic-current analogue of exactly the same bridge:

\[
\boxed{
\text{measure mismatch}
\Longleftrightarrow
\text{line-residence reweighting},
}
\]

and, for currents,

\[
\boxed{
\text{current-sign mismatch}
\Longleftrightarrow
\text{line-residence / }D_B\kappa\text{ covariance}.
}
\]

Thus the M5-683 firewall is no longer an unspecified obstacle.

---

## 7. Relation to M19-382 phase segregation

The new covariance

\[
\operatorname{Cov}_0^\Phi(L_\chi,h)
\]

is itself a phase-sorting quantity.

Hence the two apparently distinct survivors

1. `M19-382` inter-state/component hysteresis;
2. `M5-683` flux/enstrophy measure mismatch;

are structurally linked.

To reverse the coefficient-space current, the recurrent system must preferentially assign larger residence weight to labels whose coefficient velocity `h` points upward at `kappa=0`.

This is a sharper dynamical statement than merely requiring high line residence.

---

## 8. New dichotomy

The coefficient-space conveyor now has the canonical split

\[
\boxed{
\text{directed spatial }\kappa\text{-current through zero}
\quad\lor\quad
H_{Lh}^{0,+},
}
\]

where

\[
\boxed{
H_{Lh}^{0,+}:
\operatorname{Cov}_0^\Phi(L_\chi,D_B\kappa)
\text{ is uniformly positive at the scale required to cancel }G_\Phi(0).
}
\]

The first branch can be attacked by the M5-683 constitutive formula.

The second is a line-residence/velocity hysteresis branch and should be compared with the M19-349 uniform-integrability gate and the M19-382 interstate/component phase architecture.

---

## 9. Firewalls

The formula is conditional on a meaningful disintegration at the coefficient level. If `F_Phi(0)=0` in the literal pointwise-density sense, use a shrinking coefficient slab around zero and pass to the limit where justified; do not divide by a nonexistent point density.

The cutoff residence weight may degenerate if a line barely intersects the high-amplitude collar; that is a genuine residence/participation exit, not something to suppress silently.

Positive covariance is still recurrently recyclable and is not by itself a contradiction.

---

## 10. Next target

The next calculation should attack the two branches separately:

1. evaluate/control `G_E^chi(0)` using the M5-683 constitutive current together with M19-379 palinstrophy reduction;
2. if sign transfer fails, determine whether the required `Cov(L_chi,h)` floor forces residence concentration, super-parent participation, or a nonreusable genealogy transition.

\[
\boxed{\text{M19-385 COMPLETE; THE M5-683 MEASURE MISMATCH IS NOW AN EXPLICIT RESIDENCE--VELOCITY COVARIANCE GATE.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
