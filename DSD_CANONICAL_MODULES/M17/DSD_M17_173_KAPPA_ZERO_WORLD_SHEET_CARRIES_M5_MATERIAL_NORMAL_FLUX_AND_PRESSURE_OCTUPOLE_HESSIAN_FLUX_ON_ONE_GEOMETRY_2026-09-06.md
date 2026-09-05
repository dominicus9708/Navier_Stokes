# DSD M17-173 — The `kappa=0` worldsheet carries M5 material normal flux and pressure–octupole Hessian flux on one common geometry

Date: 2026-09-06  
Canonical ID: **M17-173**

Status: **CONDITIONAL SPACE-TIME GEOMETRY BRIDGE / UNDER THE M17-172 ABSOLUTELY-CONTINUOUS PUSHFORWARD BRANCH, THE M5 CURRENT-FLUX HYSTERESIS CAN BE WRITTEN AS ACTUAL WEIGHTED NORMAL FLUX THROUGH THE SPACE-TIME ZERO-WORLDSHEET `Sigma_0={kappa(q,x_3,theta)=0}` IN `(q,x_3,theta)`. THE SPACE-TIME MATERIAL FIELD `M=(H,K,1)` SATISFIES `M dot grad_st kappa=h`, SO `int_I G_Phi(0,theta)dtheta=int_{Sigma_0 cap I} w M dot N dA`. THE SEMILINEAR HESSIAN CURRENT EMBEDS AS `J=(F_33,-F_q3,0)` AND REMAINS DIVERGENCE FREE IN SPACE-TIME; ITS NORMAL FLUX IS `[F_qq H_V-25O_V^2/|Q|^4]/|grad_st kappa|`. THUS TEMPORAL CROSSING HYSTERESIS AND THE PRESSURE/OCTUPOLE SQUARE BALANCE ARE NOW TWO DISTINCT NORMAL FLUXES ON THE SAME WORLDSHEET MEASURE. THERE IS STILL NO SIGN THEOREM RELATING THEIR PRODUCT, SO THE NEW FRONTIER IS A GENUINE SAME-MEASURE FLUX COVARIANCE RATHER THAN THE EARLIER CROSS-MEASURE LOCAL/GLOBAL FIREWALL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Space-time semilinear coordinates

Use

\[
X=(q,x_3,\theta)
\]

and

\[
\boxed{
\kappa(X)=F_q(q,x_3,\theta).
}
\]

Define the regular zero-worldsheet

\[
\boxed{
\Sigma_0:=\{X:\kappa(X)=0,\ \nabla_{st}\kappa(X)\neq0\}.
}
\]

The full space-time gradient is

\[
\boxed{
\nabla_{st}\kappa
=(F_{qq},F_{q3},F_{q\theta}).
}
\]

Choose unit normal

\[
\boxed{
\mathbf N
=\frac{\nabla_{st}\kappa}{|\nabla_{st}\kappa|}.
}
\]

---

## 2. Material space-time field

M17-013 gives the reduced material flow

\[
q'=\mathscr H,
\qquad
x_3'=K.
\]

Embed it in space-time as

\[
\boxed{
\mathbf M
:=(\mathscr H,K,1).
}
\]

Then

\[
\begin{aligned}
\mathbf M\cdot\nabla_{st}\kappa
&=F_{q\theta}+\mathscr H F_{qq}+K F_{q3}\\
&=D_B\kappa.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathbf M\cdot\nabla_{st}\kappa=h.
}
\]

On the zero-worldsheet,

\[
\boxed{
\mathbf M\cdot\mathbf N
=\frac{h}{|\nabla_{st}\kappa|}.
}
\]

So upward/downward M5 crossings are literally the two orientations of material label flow through `Sigma_0`.

---

## 3. Worldsheet coarea identity

For a regular level set in three variables,

\[
\delta(\kappa)dqdx_3d\theta
=\frac{dA_{st}}{|\nabla_{st}\kappa|}.
\]

Equivalently, slicing at fixed `theta`,

\[
\frac{dA_{st}}{|\nabla_{st}\kappa|}
=\frac{ds\,d\theta}{|\nabla_{(q,3)}\kappa|}.
\]

This is the exact relation between worldsheet area and the M17-171 zero-curve coarea measure.

---

## 4. M5 current flux becomes worldsheet normal material flux

Under M17-172, the current flux-weighted M5 measure pushes forward to

\[
w_\theta(q,x_3)dqdx_3.
\]

Therefore on a time interval `I`,

\[
\begin{aligned}
\int_I G_\Phi(0,\theta)d\theta
&=\int_I\int
h w_\theta\delta(\kappa)dqdx_3d\theta\\
&=\int_{\Sigma_0\cap\{\theta\in I\}}
\frac{h w_\theta}{|\nabla_{st}\kappa|}dA_{st}.
\end{aligned}
\]

Using Section 2,

\[
\boxed{
\int_I G_\Phi(0,\theta)d\theta
=\int_{\Sigma_0\cap I}
 w_\theta\,\mathbf M\cdot\mathbf N\,dA_{st}.
}
\]

Thus the M5 hysteresis is a genuine weighted normal-flux asymmetry through the zero-worldsheet.

The recurrent condition

\[
\overline G_\Phi(0)<0
\]

means the long-time worldsheet flux of `w M` is biased toward the negative normal orientation.

---

## 5. Base current on the same worldsheet

M17-172 gives the base-current density

\[
\frac{w_\theta}{a_\theta}dqdx_3.
\]

Therefore

\[
\boxed{
\int_I G_0(0,\theta)d\theta
=\int_{\Sigma_0\cap I}
\frac{w_\theta}{a_\theta}
\mathbf M\cdot\mathbf N\,dA_{st}.
}
\]

The M5 recurrence pair becomes

\[
\boxed{
\overline{\text{base-weighted worldsheet normal flux}}=0,
}
\]

while

\[
\boxed{
\overline{\text{current-flux-weighted worldsheet normal flux}}<0.
}
\]

The hysteresis is therefore a worldsheet normal-flux covariance with amplification.

---

## 6. Embed the Hessian current in space-time

M17-171 gives the spatial semilinear current

\[
\mathbf J_F=(F_{33},-F_{q3}).
\]

Embed it as

\[
\boxed{
\mathcal J_F
:=(F_{33},-F_{q3},0).
}
\]

Then

\[
\boxed{
\nabla_{st}\cdot\mathcal J_F
=F_{q33}-F_{q33}=0.
}
\]

So it remains exactly divergence free in the three-dimensional semilinear space-time.

---

## 7. Pressure–octupole normal flux through the worldsheet

Compute

\[
\begin{aligned}
\mathcal J_F\cdot\mathbf N
&=\frac{F_{33}F_{qq}-F_{q3}^2}{|\nabla_{st}\kappa|}.
\end{aligned}
\]

At the vertical crossing,

\[
F_{33}=H_V,
\qquad
F_{q3}^2=\frac{25O_V^2}{|Q|_F^4}.
\]

Thus

\[
\boxed{
\mathcal J_F\cdot\mathbf N
=\frac{
F_{qq}H_V-25O_V^2/|Q|_F^4
}{|\nabla_{st}\kappa|}.
}
\]

This is the space-time version of the M17-170/171 Hessian flux.

---

## 8. Relation to fixed-time tangential variation

Let

\[
g_s:=|\nabla_{(q,3)}\kappa|,
\qquad
g_{st}:=|\nabla_{st}\kappa|.
\]

M17-171 gives on the fixed-time zero curve

\[
\partial_sF_3
=\frac{F_{qq}H_V-F_{q3}^2}{g_s}.
\]

Therefore

\[
\boxed{
\mathcal J_F\cdot\mathbf N
=\frac{g_s}{g_{st}}\partial_sF_3.
}
\]

The factor `g_s/g_st` is exactly the geometric tilt between a fixed-time zero curve and the full zero-worldsheet.

---

## 9. Two fluxes, one worldsheet

The two relevant normal flux densities are now

\[
\boxed{
\Phi_M:=w_\theta\mathbf M\cdot\mathbf N
=w_\theta\frac{h}{g_{st}},
}
\]

and

\[
\boxed{
\Phi_H:=\mathcal J_F\cdot\mathbf N
=\frac{F_{qq}H_V-25O_V^2/|Q|_F^4}{g_{st}}.
}
\]

They live on the same surface element `dA_st`.

This removes the main geometric measure mismatch **on the conditional M17-172 branch**.

The remaining problem is a genuine same-worldsheet covariance:

\[
\boxed{
\text{sign-biased material crossing flux }\Phi_M
\quad\leftrightarrow?\quad
\text{pressure/octet Hessian flux }\Phi_H.
}
\]

---

## 10. No automatic product sign

There is no algebraic identity forcing

\[
\Phi_M\Phi_H
\]

to have one sign.

Indeed `h` depends on the temporal/flow derivative of `kappa`, while the Hessian determinant depends on the spatial semilinear Hessian of `F`.

Therefore

\[
\boxed{
\overline G_\Phi(0)<0
\not\Longrightarrow
\operatorname{sgn}\Phi_H.
}
\]

The old cross-measure covariance firewall has been reduced, but not eliminated; it is now a same-worldsheet flux-correlation problem.

---

## 11. Flux matrix viewpoint

At a worldsheet point define the two-row normal-flux data

\[
\boxed{
\mathbb F_0
:=
\begin{pmatrix}
\mathbf M\cdot\mathbf N\\
\mathcal J_F\cdot\mathbf N
\end{pmatrix}
=
\frac1{g_{st}}
\begin{pmatrix}
h\\
F_{qq}H_V-25O_V^2/|Q|_F^4
\end{pmatrix}.
}
\]

M5 constrains the first component after amplification weighting.
M17-170/171 constrains spatial integrals of the second component.

A final covariance theorem would need to control their joint distribution on `Sigma_0`, not each marginal separately.

---

## 12. DSD audit

### Audit A — using M17-173 without the M17-172 pushforward hypothesis
Rejected for the M5 measure statement. The purely geometric worldsheet identities remain valid, but identification of the M5 integral with `w M dot N dA` is conditional.

### Audit B — using `|grad_st kappa|` in the fixed-time coarea formula
The slice measure is `ds/|grad_(q,3) kappa|`; the worldsheet formula uses `dA_st/|grad_st kappa|`. Section 3 records the exact equivalence.

### Audit C — claiming the Hessian current has a temporal component
It does not; its embedding has third component zero.

### Audit D — inferring a sign correlation between the two normal fluxes
Rejected.

### Audit E — proof status
The measure geometry is unified conditionally, but the flux covariance remains open.

---

## 13. Updated Rank-1 worldsheet frontier

On the conditional regular pushforward branch,

\[
\boxed{
\int_I G_\Phi(0,\theta)d\theta
=\int_{\Sigma_0\cap I}w_\theta\mathbf M\cdot\mathbf N\,dA,
}
\]

while

\[
\boxed{
\mathcal J_F\cdot\mathbf N
=\frac{F_{qq}H_V-25O_V^2/|Q|_F^4}{|\nabla_{st}\kappa|}.
}
\]

The next useful calculation is to examine whether `F_3` itself has a material transport law on `Sigma_0` that couples these two fluxes. In particular,

\[
D_LF_3-F_{3\theta}
=\mathscr H F_{q3}+K F_{33}
\]

combines the same mixed/axial Hessian entries with the material label velocity and may provide the missing off-diagonal relation.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
