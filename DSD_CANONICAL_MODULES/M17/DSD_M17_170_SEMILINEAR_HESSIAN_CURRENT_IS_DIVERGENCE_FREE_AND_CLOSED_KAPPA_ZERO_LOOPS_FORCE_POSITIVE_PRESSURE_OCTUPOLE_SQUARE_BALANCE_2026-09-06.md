# DSD M17-170 — A divergence-free semilinear Hessian current puts the vertical pressure coordinate and local-octupole square in one exact `kappa=0` flux balance

Date: 2026-09-06  
Canonical ID: **M17-170**

Status: **NEW CONSERVATIVE LABEL-PLANE STRUCTURE / M17-169 IDENTIFIES `H_V=F_33` AND `O_V=-(1/5)|Q|_F^2 F_q3` AT A VERTICAL KAPPA-ZERO CROSSING. AT EACH FIXED THETA THE TWO-COMPONENT CURRENT `J_F=(F_33,-F_q3)` IN THE SEMILINEAR `(q,x_3)` PLANE IS EXACTLY DIVERGENCE FREE BECAUSE `partial_q F_33=partial_3 F_q3`. THE KAPPA-ZERO CURVE HAS NORMAL `grad kappa=(F_qq,F_q3)`, SO THE NORMAL CURRENT IS `[F_qq H_V-25 O_V^2/|Q|_F^4]/|grad kappa|`. FOR ANY CLOSED REGULAR KAPPA-ZERO COMPONENT BOUNDING A REGION WHERE F IS SMOOTH, THE DIVERGENCE THEOREM FORCES THE EXACT POSITIVE SQUARE BALANCE `oint F_qq H_V/|grad kappa| ds =25 oint O_V^2/(|Q|_F^4|grad kappa|) ds >0` UNLESS THE OCTUPOLE VANISHES IDENTICALLY. THUS ON CLOSED LABEL-PLANE ZERO LOOPS THE GLOBAL PRESSURE COORDINATE CANNOT BE COVARIANCE-FREE: IT MUST HAVE A POSITIVE WEIGHTED CORRELATION WITH THE ROOT CURVATURE `F_qq`. OPEN ZERO COMPONENTS ARE ROUTED TO EXPLICIT ENDPOINT/BOUNDARY FLUX. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Semilinear coordinates

At fixed similarity time `theta`, use the semilinear variables

\[
(q,x_3)
\]

and the scalar

\[
F(q,x_3,\theta)
\]

from

\[
\Delta q=F(q,x_3,\theta),
\qquad
\kappa=F_q.
\]

M17-169 gives at the vertical nodal filament in nodal gauge

\[
\boxed{H_V=F_{33}}
\]

and, at a regular `kappa=0` crossing,

\[
\boxed{
O_V=-\frac15|Q|_F^2F_{q3}.
}
\]

---

## 2. Define the Hessian current

Define the two-component current in the `(q,x_3)` plane:

\[
\boxed{
\mathbf J_F
:=(J_q,J_3)
:=(F_{33},-F_{q3}).
}
\]

Then

\[
\begin{aligned}
\nabla_{(q,3)}\cdot\mathbf J_F
&=\partial_qF_{33}+\partial_3(-F_{q3})\\
&=F_{q33}-F_{q33}.
\end{aligned}
\]

Therefore

\[
\boxed{
\nabla_{(q,3)}\cdot\mathbf J_F=0.
}
\]

This identity uses only smooth commutation of mixed partial derivatives.
It is independent of the Navier--Stokes pressure recurrence argument.

---

## 3. Current components at a vertical crossing

At `kappa=0`, M17-169 gives

\[
F_{33}=H_V,
\]

and

\[
-F_{q3}
=\frac{5O_V}{|Q|_F^2}.
\]

Hence

\[
\boxed{
\mathbf J_F
=
\left(
H_V,
\frac{5O_V}{|Q|_F^2}
\right)
}
\]

on the physical vertical crossing point represented in semilinear coordinates.

Thus the global axial pressure coordinate and local octupole orientation are literally the two components of one divergence-free current.

---

## 4. Geometry of the kappa-zero curve

The zero set is

\[
\Gamma_0
:=\{(q,x_3):F_q(q,x_3)=0\}.
\]

Its gradient is

\[
\boxed{
\nabla_{(q,3)}\kappa
=(F_{qq},F_{q3}).
}
\]

At a regular zero point,

\[
|\nabla_{(q,3)}\kappa|>0.
\]

Choose the unit normal

\[
\boxed{
\mathbf n_\kappa
=\frac{(F_{qq},F_{q3})}
{|\nabla_{(q,3)}\kappa|}.
}
\]

---

## 5. Exact normal flux on `kappa=0`

Compute

\[
\begin{aligned}
\mathbf J_F\cdot\mathbf n_\kappa
&=\frac{F_{33}F_{qq}-F_{q3}^2}
{|\nabla\kappa|}.
\end{aligned}
\]

Thus

\[
\boxed{
\mathbf J_F\cdot\mathbf n_\kappa
=\frac{\det\nabla^2_{(q,3)}F}
{|\nabla\kappa|}.
}
\]

Using the vertical identities,

\[
F_{33}=H_V,
\qquad
F_{q3}^2
=\frac{25O_V^2}{|Q|_F^4},
\]

so

\[
\boxed{
\mathbf J_F\cdot\mathbf n_\kappa
=
\frac{
F_{qq}H_V
-25O_V^2/|Q|_F^4
}
{|\nabla\kappa|}.
}
\]

This is an atlas-invariant version of the Schur-complement identity in M17-169.
No division by `F_qq` is required.

---

## 6. Closed regular zero component

Assume a connected regular component `Gamma` of `kappa=0` is a closed curve bounding a region `D` in the semilinear plane and `F` is smooth on `D`.

By divergence-free current,

\[
0
=\int_D\nabla\cdot\mathbf J_F\,dqdx_3
=\oint_\Gamma\mathbf J_F\cdot\mathbf n_\kappa\,ds
\]

with the outward orientation.

Therefore

\[
\boxed{
\oint_\Gamma
\frac{F_{qq}H_V}{|\nabla\kappa|}ds
=
25\oint_\Gamma
\frac{O_V^2}{|Q|_F^4|\nabla\kappa|}ds.
}
\]

The right-hand side is nonnegative.
If `O_V` is not identically zero on the component, it is strictly positive.

Hence

\[
\boxed{
\oint_\Gamma
\frac{F_{qq}H_V}{|\nabla\kappa|}ds
>0
}
\]

for every closed regular zero component carrying nontrivial vertical octupole.

---

## 7. Pressure-root curvature covariance is forced

Define the natural zero-curve measure

\[
\boxed{
d\nu_\Gamma:=\frac{ds}{|\nabla\kappa|}.}
\]

Then the closed-loop identity becomes

\[
\boxed{
\int_\Gamma F_{qq}H_V\,d\nu_\Gamma
=25\int_\Gamma\frac{O_V^2}{|Q|_F^4}d\nu_\Gamma.
}
\]

Thus the covariance between `F_qq` and the global pressure coordinate is not free on a closed zero loop.
It is forced by a positive octupole-square source.

This removes the relative-speed factor from this label-plane spatial identity.

---

## 8. Relation to the M17-169 Schur complement

When `F_qq != 0` and the zero curve is graphed as `q=q_*(x_3)`, M17-169 gives

\[
H_V-\mathcal C_{*,33}
=\frac{25O_V^2}{|Q|_F^4F_{qq}}.
\]

Multiplying by `F_qq` gives

\[
F_{qq}H_V
-F_{qq}\mathcal C_{*,33}
=\frac{25O_V^2}{|Q|_F^4}.
\]

The current-flux formulation is stronger geometrically because it remains valid through points where `F_qq=0` as long as the full zero curve remains regular through `F_q3 != 0`.

Thus `F_qq=0` is recognized correctly as a chart turnover rather than automatically a physical degeneration.

---

## 9. Open zero components

If a regular zero component is open rather than closed, the divergence theorem applied to a truncated region produces additional boundary fluxes.

Therefore the branch split is

\[
\boxed{
\Gamma_0^{regular}
\Longrightarrow
\Gamma_{closed}^{square\ balance}
\ \lor\
\Gamma_{open}^{endpoint/boundary\ flux}.
}
\]

Open components are not silently treated as closed.
Their endpoint, infinity, chart, or domain flux must be recorded explicitly.

---

## 10. Connection to M5 crossing hysteresis

M5-685/M17-095 controls material temporal crossings of the same scalar

\[
\kappa=F_q.
\]

M17-170 instead controls spatial flux along the semilinear zero curve at fixed `theta`.

These are distinct measures:

\[
\boxed{
\text{M5 temporal crossing measure}
\neq
\text{zero-curve measure }ds/|\nabla\kappa|.
}
\]

However, both now use the same zero set and the same semilinear descriptors.
The remaining bridge is no longer between unrelated local/global quantities; it is between two natural flux measures on one analytic zero-set geometry.

---

## 11. DSD audit

### Audit A — treating `F_qq=0` as a singular zero set
Rejected. At the physical vertical regular crossing `F_q3=kappa_3 != 0`, so the zero set remains regular.

### Audit B — using the closed-loop identity on an open component
Rejected. Endpoint/boundary flux must be retained.

### Audit C — identifying the zero-curve measure with M5 label measure
Rejected.

### Audit D — reading positivity as pointwise `F_qq H_V>0`
Rejected. The theorem is an integrated positive covariance around a closed component.

### Audit E — proof status
A new exact conservative relation is obtained but temporal hysteresis and spatial zero-loop flux are not yet unified.

---

## 12. Updated Rank-1 vertical frontier

For every closed regular semilinear `kappa=0` component carrying nonzero octupole,

\[
\boxed{
\int_\Gamma F_{qq}H_V\frac{ds}{|\nabla\kappa|}
=25\int_\Gamma
\frac{O_V^2}{|Q|_F^4}
\frac{ds}{|\nabla\kappa|}
>0.
}
\]

The next target is to connect the M5 material-crossing current through `kappa=0` to this divergence-free zero-curve current without replacing either measure by the other. The natural object is a space-time zero-worldsheet of `kappa(q,x_3,theta)=0` carrying both the material relative flux and the semilinear Hessian flux.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
