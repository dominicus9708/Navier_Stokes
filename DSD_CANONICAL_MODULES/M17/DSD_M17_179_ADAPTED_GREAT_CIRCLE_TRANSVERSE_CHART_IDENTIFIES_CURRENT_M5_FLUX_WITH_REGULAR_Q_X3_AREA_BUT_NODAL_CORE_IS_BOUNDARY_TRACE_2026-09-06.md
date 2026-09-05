# DSD M17-179 — An adapted great-circle transverse chart identifies current M5 flux with regular `(q,x_3)` area; the nodal core remains only a boundary trace

Date: 2026-09-06  
Canonical ID: **M17-179**

Status: **REGULAR-FLUX PUSHFORWARD THEOREM / ON A GREAT-CIRCLE FLOW BOX WITH `W_h=J grad_h q != 0`, ONE MAY PARAMETRIZE A TRANSVERSE SURFACE BY `(q,z)` WITH `partial_q x_h=grad_h q/|grad_h q|^2`. A DIRECT CROSS-PRODUCT CALCULATION GIVES `W dot (X_q cross X_z)=+-1`, SO THE ABSOLUTE PHYSICAL VORTICITY-FLUX FORM IS EXACTLY `dq dz`. M17-013 GIVES THE REDUCED LABEL-FLOW JACOBIAN `J_L=a`, HENCE THE CURRENT M5 WEIGHTED BASE FLUX `a dmu_0` PUSHES FORWARD TO ORDINARY `(q,x_3)` AREA ON EVERY SUCH REGULAR CHART. THEREFORE `G_Phi(0)` HAS AN EXACT REGULAR LABEL-PLANE COAREA REPRESENTATION. HOWEVER THE VERTICAL NODAL FILAMENT HAS `W=0`, IS NOT AN INTERIOR POINT OF THESE FLOW BOXES, AND APPEARS ONLY AS A CRITICAL-LEVEL/BOUNDARY TRACE. THE GLOBAL NEGATIVE M5 CURRENT DOES NOT BY ITSELF DETERMINE THE SIGN OF THE NODAL ENDPOINT CROSSING OR `O_V`. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Great-circle regular flow box

Use

\[
W=(J\nabla_hq,0)
\]

on a connected region where

\[
\boxed{\nabla_hq\neq0.}
\]

Fix `z=x_3` and choose a local curve transverse to the horizontal vorticity lines.

Parametrize the resulting two-dimensional transverse surface by

\[
\boxed{X(q,z)=(x_h(q,z),z)}
\]

with gauge

\[
\boxed{
\partial_qx_h
=\frac{\nabla_hq}{|\nabla_hq|^2}.
}
\]

Then indeed

\[
\partial_q q(x_h(q,z),z)=1.
\]

Write

\[
a:=\partial_qx_h,
\qquad
b:=\partial_zx_h.
\]

Thus

\[
X_q=(a,0),
\qquad
X_z=(b,1).
\]

---

## 2. Exact transverse vorticity flux

With the standard planar rotation `J`,

\[
W_h=J\nabla_hq.
\]

The horizontal part of the oriented surface element is

\[
(X_q\times X_z)_h=-Ja
\]

up to the chosen orientation convention.

Therefore

\[
\begin{aligned}
W\cdot(X_q\times X_z)
&=(J\nabla_hq)\cdot(-Ja)\\
&=-\nabla_hq\cdot a\\
&=-1.
\end{aligned}
\]

Reversing the surface orientation changes only the sign.

Hence

\[
\boxed{
|W\cdot(X_q\times X_z)|=1.
}
\]

The absolute physical transverse vorticity-flux form is exactly

\[
\boxed{|d\Phi_W|=dq\,dz.}
\]

This identity is independent of the `z`-gauge term `b=partial_z x_h`.

---

## 3. Base M5 flux measure in adapted coordinates

At the fixed M5 base time, choose the regular transverse flow-box atlas to be adapted to the great-circle coordinates above.

After the measurable first-chart assignment used by M5-647, each regular label is counted once.

Locally,

\[
\boxed{d\mu_0=dq_0\,dz_0}
\]

up to orientation, which is irrelevant for the positive base flux measure.

Thus the conditional density `w_0` introduced in M17-172 is not needed on an adapted regular chart: the canonical density is exactly one.

---

## 4. Current weighted flux becomes current label-plane area

M17-013 gives the reduced material flow

\[
(q_0,z_0)\mapsto(q,z)
\]

with Jacobian

\[
\boxed{J_L=a}
\]

where `a` is precisely the M5 amplification factor.

Therefore

\[
\boxed{
dq\,dz
=J_Ldq_0\,dz_0
=a\,d\mu_0.
}
\]

Hence the current M5 weighted flux measure pushes forward exactly to ordinary current label-plane area on every regular adapted chart.

---

## 5. Exact regular coarea formula for the M5 current

The M5 current is

\[
G_\Phi(k,\theta)
=\int h_\lambda a_\lambda
\delta(k-\kappa_\lambda)d\mu_0.
\]

On the regular great-circle chart, Section 4 yields

\[
\boxed{
G_\Phi(k,\theta)
=\int h(q,z,\theta)
\delta(k-\kappa(q,z,\theta))dq\,dz.
}
\]

For a regular zero level

\[
\Gamma_0^{reg}=\{\kappa=0,\ W\neq0\},
\qquad
|\nabla_{(q,z)}\kappa|\neq0,
\]

ordinary two-dimensional coarea gives

\[
\boxed{
G_\Phi(0,\theta)
=\int_{\Gamma_0^{reg}}
\frac{h}{|\nabla_{(q,z)}\kappa|}\,ds,
}
\]

with a sum over the measurable first-chart partition if more than one chart is needed.

Thus the regular-label version of the M17-172 coarea bridge is unconditional inside the great-circle Rank-1 branch.

---

## 6. Why this still does not prove M17-095

The vertical nodal filament satisfies

\[
W=0,
\qquad
\nabla_hq=0.
\]

Hence the adapted regular transverse chart breaks down at the nodal critical level.

M17-090's `O_V` and nodal crossing factorization are evaluated precisely there.

The formula in Section 5 integrates the **regular zero curve** in the label plane.
It does not attach positive transverse-flux mass to an isolated nodal point or automatically identify a regular-label crossing rate with the nodal-core crossing rate.

Therefore

\[
\boxed{
\overline{G_\Phi(0)}<0
}
\]

does not by itself imply

\[
\boxed{
\overline{r_VO_V}>0
}
\]

at the nodal core.

---

## 7. Boundary-trace interpretation near a winding node

For a positive-index winding node, the critical value of `q` is a boundary value for nearby regular closed vorticity levels.

After gauge normalization, write it as

\[
q=0.
\]

Then regular vortex-line labels occupy one side, for example

\[
q>0,
\]

while the nodal filament lies at the boundary `q=0`.

The M5 current may have a well-defined **density trace** as `q -> 0+`, but such a trace is an additional statement.

A global integral sign over all regular `q` values cannot determine that boundary trace without localization.

---

## 8. Correct missing theorem

To recover a genuine M5-to-nodal bridge one would need at least one of the following:

1. a theorem localizing a fixed nonzero portion of `G_Phi(0)` to arbitrarily small regular `q`-neighborhoods of the nodal critical level;
2. a signed trace theorem showing that the regular zero-curve current density converges to the nodal crossing rate with a controlled sign;
3. a structural theorem forcing every relevant regular `kappa=0` component to terminate at, or be controlled by, the vertical nodal filament.

None is currently established.

---

## 9. DSD audit

### Audit A — regular measure bridge
Closed: on adapted regular charts `a dmu_0=dq dz` exactly.

### Audit B — nodal support
Not closed: the nodal filament is a zero-flux critical boundary, not an ordinary regular label.

### Audit C — M17-172
Its absolute-continuity hypothesis is unnecessary on regular great-circle charts, but its use to force nodal-core quantities remains conditional.

### Audit D — M17-095
Remains conditional after M17-178; this module explains exactly why.

### Audit E — proof status
No contradiction follows from the regular measure identification alone.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
