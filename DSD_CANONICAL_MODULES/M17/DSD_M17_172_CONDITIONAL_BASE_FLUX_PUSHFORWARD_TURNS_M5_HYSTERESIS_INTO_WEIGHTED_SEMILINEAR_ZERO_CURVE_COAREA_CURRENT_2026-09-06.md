# DSD M17-172 — Conditional base-flux pushforward turns M5 hysteresis into a weighted semilinear `kappa=0` coarea current

Date: 2026-09-06  
Canonical ID: **M17-172**

Status: **CONDITIONAL MEASURE-BRIDGE THEOREM / M5-685 DEFINES `dmu_0` AS A FIXED POSITIVE BASE TRANSVERSE-FLUX MEASURE ON MATERIAL VORTEX-LINE LABELS, NOT AS LEBESGUE AREA IN THE REDUCED `(q,x_3)` PLANE. M17-013 IDENTIFIES ONLY THE AMPLIFICATION FACTOR WITH THE REDUCED LABEL-FLOW JACOBIAN `a=J_L`. IF, IN ADDITION, THE RESTRICTION OF THE M5 BASE LABEL MEASURE TO THE GREAT-CIRCLE/VERTICAL STRATUM PUSHES FORWARD AT THE BASE TIME TO `dnu_0=w_0(q_0,x_{3,0})dq_0dx_{3,0}` WITH POSITIVE FINITE DENSITY, THEN THE CURRENT FLUX-WEIGHTED MEASURE `a dmu_0` PUSHES FORWARD EXACTLY TO `w_theta(q,x_3)dqdx_3`, WHERE `w_theta=w_0 circ Phi^{-1}`. CONSEQUENTLY `G_Phi(0,theta)=int_{Gamma_0(theta)} h w_theta/|grad kappa| ds`, WHILE THE UNWEIGHTED BASE CURRENT IS `G_0(0,theta)=int_{Gamma_0} h w_theta/(a_theta |grad kappa|) ds`. THIS PLACES M5 HYSTERESIS AND THE M17-170/171 SEMILINEAR PRESSURE-OCTUPOLE CURRENT ON THE SAME ZERO-CURVE GEOMETRY WITHOUT IDENTIFYING THEIR WEIGHTS. THE ABSOLUTE-CONTINUITY PUSHFORWARD ASSUMPTION IS NOT YET DERIVED FROM M5-647 AND REMAINS AN EXPLICIT CONDITIONAL GATE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. What M5 actually supplies

M5-685 starts from a fixed base transverse-flux measure

\[
\boxed{d\mu_0(\lambda)}
\]

on material vortex-line labels `lambda` after the M5-647 transverse-atlas assignment.

It defines

\[
G_0(k,\theta)
=\int h_\lambda\delta(k-\kappa_\lambda)d\mu_0,
\]

and

\[
G_\Phi(k,\theta)
=\int h_\lambda a_\lambda
\delta(k-\kappa_\lambda)d\mu_0,
\]

where

\[
a_\lambda'=\kappa_\lambda a_\lambda.
\]

The recurrent survivor satisfies

\[
\boxed{\overline G_0(0)=0,}
\qquad
\boxed{\overline G_\Phi(0)<0.}
\]

No reduced-label Lebesgue measure is part of this definition.

---

## 2. Reduced great-circle label flow

M17-013 gives the reduced coordinates

\[
\zeta=(q,x_3)
\]

and the flow

\[
\dot\zeta=V_L(\zeta,\theta)
=(\mathscr H,K).
\]

Its divergence is

\[
\boxed{\operatorname{div}_\zeta V_L=\kappa.}
\]

Let

\[
\Phi_{\theta_0}^{\theta}:\zeta_0\mapsto\zeta(\theta)
\]

be the reduced flow map.
M17-013 gives

\[
\boxed{
J_L(\theta)
:=\det D\Phi_{\theta_0}^{\theta}
=a(\theta)
}
\]

after normalizing `J_L(theta_0)=1`.

This identifies the scalar amplification law with the reduced label-area Jacobian.
It does **not** identify `dmu_0` with `d zeta_0`.

---

## 3. Explicit conditional pushforward assumption

Let

\[
\Psi_0:\lambda\mapsto\zeta_0=(q_0,x_{3,0})
\]

be the reduced-label coordinate map on the retained vertical/great-circle material stratum.

Assume the pushforward of the M5 base measure is absolutely continuous:

\[
\boxed{
(\Psi_0)_\#\mu_0
=w_0(\zeta_0)d\zeta_0.
}
\]

For the strongest comparison version, assume

\[
\boxed{
0<c_w\le w_0(\zeta_0)\le C_w<\infty
}
\]

on the compact retained label domain.

This is a **new conditional hypothesis**.
It is not currently proved by M5-647 or M17-013.

---

## 4. Pushforward of the current flux-weighted measure

At time `theta`, the reduced coordinate map is

\[
\Psi_\theta
=\Phi_{\theta_0}^{\theta}\circ\Psi_0.
\]

For a test function `f`,

\[
\int f(\Psi_\theta(\lambda))
a_\lambda d\mu_0(\lambda)
\]

becomes, using Section 3,

\[
\int
f(\Phi(\zeta_0))
a(\zeta_0)w_0(\zeta_0)d\zeta_0.
\]

Since

\[
d\zeta=a(\zeta_0)d\zeta_0,
\]

change variables to the current coordinate `zeta`:

\[
\boxed{
(\Psi_\theta)_\#(a\mu_0)
=w_\theta(\zeta)d\zeta,
}
\]

where

\[
\boxed{
w_\theta(\zeta)
:=w_0(\Phi^{-1}(\zeta)).}
\]

Thus the current M5 flux weight removes exactly the Jacobian needed to pass from base area to current reduced-label area.

---

## 5. Pushforward of the unweighted base measure

Similarly,

\[
\int f(\Psi_\theta(\lambda))d\mu_0
=
\int f(\Phi(\zeta_0))w_0(\zeta_0)d\zeta_0.
\]

Since `d zeta=a d zeta_0`, this becomes

\[
\boxed{
(\Psi_\theta)_\#\mu_0
=\frac{w_\theta(\zeta)}{a_\theta(\zeta)}d\zeta,
}
\]

where

\[
a_\theta(\zeta)
:=a(\Phi^{-1}(\zeta),\theta).
\]

Hence the base and current M5 measures become two different densities on the same reduced label plane:

\[
\boxed{
\text{base: }\frac{w_\theta}{a_\theta}d\zeta,
\qquad
\text{current: }w_\theta d\zeta.
}
\]

---

## 6. Transport law for `w_theta`

Because

\[
w_\theta=w_0\circ\Phi^{-1},
\]

it is materially transported by the reduced flow:

\[
\boxed{
(\partial_\theta+V_L\cdot\nabla_\zeta)w_\theta=0.
}
\]

Thus

\[
\partial_\theta w_\theta
+\operatorname{div}(w_\theta V_L)
=\kappa w_\theta.
\]

This is consistent with the fact that `w_theta d zeta` is the current flux-weighted measure and acquires local source `kappa` through label-area expansion.

By contrast, the density `w_theta/a_theta` satisfies the source-free continuity law appropriate to the fixed base measure.

---

## 7. Coarea formula for the current M5 crossing current

At a regular multiplier level, coarea in the **reduced label plane** gives

\[
\int
h(\zeta,\theta)w_\theta(\zeta)
\delta(k-\kappa(\zeta,\theta))d\zeta
\]

\[
=\int_{\{\kappa=k\}}
\frac{h w_\theta}{|\nabla_\zeta\kappa|}ds.
\]

Therefore, under the pushforward assumption,

\[
\boxed{
G_\Phi(k,\theta)
=\int_{\{\kappa=k\}}
\frac{h w_\theta}{|\nabla\kappa|}ds.
}
\]

At zero,

\[
\boxed{
G_\Phi(0,\theta)
=\int_{\Gamma_0(\theta)}
\frac{h w_\theta}{|\nabla\kappa|}ds.
}
\]

This is **label-plane coarea**, not physical spatial coarea.

---

## 8. Coarea formula for the base current

The same calculation with the base density gives

\[
\boxed{
G_0(0,\theta)
=\int_{\Gamma_0(\theta)}
\frac{h w_\theta}{a_\theta|\nabla\kappa|}ds.
}
\]

Hence the M5 hysteresis pair becomes

\[
\boxed{
\overline{
\int_{\Gamma_0}
\frac{h w_\theta}{a_\theta|\nabla\kappa|}ds
}=0,
}
\]

while

\[
\boxed{
\overline{
\int_{\Gamma_0}
\frac{h w_\theta}{|\nabla\kappa|}ds
}<0.
}
\]

The phase bias is now expressed entirely on the same semilinear zero curve used by M17-170/171.

---

## 9. Comparison with the M17-171 geometric measure

M17-171 naturally uses

\[
\boxed{
d\nu_\Gamma=\frac{ds}{|\nabla\kappa|}.}
\]

Under the bounded-density version of the pushforward assumption,

\[
\boxed{
c_w d\nu_\Gamma
\le
w_\theta d\nu_\Gamma
\le
C_wd\nu_\Gamma.}
\]

Thus M5 current-flux crossing measure and M17-171 zero-curve measure are quantitatively comparable up to the transported base-flux density.

They are still not identical unless `w_0` is constant.

---

## 10. What this would buy for the pressure-octupole square balance

M17-171 gives

\[
\partial_sF_3
=
\frac{F_{qq}H_V-25O_V^2/|Q|_F^4}
{|\nabla\kappa|}.
\]

M17-172 places the M5 material crossing scalar `h` on the same curve with weight

\[
w_\theta\frac{ds}{|\nabla\kappa|}.
\]

Hence the remaining covariance problem would become a problem of **two flux densities on one regular zero curve**:

\[
\boxed{
\text{material crossing flux: }h w_\theta,
}
\]

and

\[
\boxed{
\text{pressure/octet tangential flux: }
F_{qq}H_V-25O_V^2/|Q|_F^4.
}
\]

No measure substitution would remain except the explicit density `w_theta`.

---

## 11. Why the assumption is nontrivial

M5's labels originate from transverse vortex-line flux charts.
The reduced semilinear pair `(q,x_3)` may fail to be:

1. injective on the M5 atlas;
2. nondegenerate as a coordinate map;
3. absolutely continuous with respect to the transverse base flux measure;
4. uniformly bounded in density near nodal or chart degeneracies.

Therefore Section 3 cannot be promoted to a theorem merely from `a=J_L`.

The missing result is a genuine coordinate/pushforward theorem relating the M5 transverse flux atlas to the semilinear reduced-label atlas.

---

## 12. DSD audit

### Audit A — writing `a dmu_0=dq dx_3` unconditionally
Rejected.

### Audit B — using physical spatial coarea
Rejected. All coarea statements here are in the reduced label plane.

### Audit C — confusing `a=J_L` with measure equality
Rejected. A Jacobian law does not specify the base measure density.

### Audit D — assuming bounded `w_0`
It is a stronger conditional branch and must be separately justified or exited through a density-degeneration gate.

### Audit E — proof status
The exact bridge is derived conditionally; the coordinate pushforward assumption remains open.

---

## 13. Updated measure frontier

The Rank-1 vertical covariance problem now has the precise split

\[
\boxed{
R_{1,V}^{cross}
\Longrightarrow
G_{pushforward}^{AC,bounded}
\lor
G_{label\ density/coordinate\ degeneration}.
}
\]

On the first branch, M5 and M17-171 live on the same semilinear zero curve and differ only by the transported positive density `w_theta` and the amplification factor in the base current.

The next target is a space-time zero-worldsheet formulation that is valid on this conditional branch and cleanly separates the material normal crossing flux from the pressure-octupole tangential flux.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
