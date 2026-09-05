# DSD M17-180 — The global M5 `kappa=0` current sign does not fix the nodal boundary trace; an explicit regular label-plane countermodel

Date: 2026-09-06  
Canonical ID: **M17-180**

Status: **TRACE-LOCALIZATION FIREWALL / M17-179 IDENTIFIES THE CURRENT M5 WEIGHTED FLUX WITH ORDINARY `(q,x_3)` AREA ON REGULAR GREAT-CIRCLE CHARTS, SO `G_Phi(0)` IS AN INTEGRAL OF A REGULAR ZERO-CURVE CURRENT DENSITY OVER ALL REGULAR `q` LABELS. THE VERTICAL NODAL FILAMENT IS A CRITICAL BOUNDARY LEVEL, NOT AN INTERIOR FLUX LABEL. A NEGATIVE GLOBAL INTEGRAL DOES NOT DETERMINE THE SIGN OF THE CURRENT DENSITY AT THAT BOUNDARY TRACE. THIS IS NOT ONLY A LOGICAL POSSIBILITY: THE REDUCED LABEL SYSTEM `kappa=z`, `V_L=(0,j(q)+z^2/2)` HAS `div V_L=kappa` EXACTLY AND `h=j(q)` ON `kappa=0`; CHOOSING `j(q)>0` NEAR THE NODAL BOUNDARY `q=0` BUT A LARGER NEGATIVE CONTRIBUTION AWAY FROM IT GIVES `G_Phi(0)<0` WHILE THE NODAL-SIDE TRACE IS POSITIVE. THUS M5 GLOBAL HYSTERESIS CANNOT FORCE THE SIGN OF THE NODAL `O_V` WITHOUT A SEPARATE LOCALIZATION/TRACE THEOREM. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Regular current-density decomposition

By M17-179, on an adapted regular great-circle chart,

\[
\boxed{
G_\Phi(0,\theta)
=\int_{\Gamma_0^{reg}}
\frac{h}{|\nabla\kappa|}\,ds.
}
\]

If the regular zero curve is locally represented as finitely many roots

\[
z=z_j(q,\theta)
\]

with `partial_z kappa != 0`, then

\[
\boxed{
G_\Phi(0,\theta)
=\int j(q,\theta)dq,
}
\]

where

\[
\boxed{
j(q,\theta)
:=\sum_j
\frac{h(q,z_j(q,\theta),\theta)}
{|\partial_z\kappa(q,z_j(q,\theta),\theta)|}.
}
\]

This is the current density per regular `q`-flux label.

For a winding node whose critical level is normalized to `q=0`, the nodal core is a boundary trace `q -> 0+` (or `0-`, according to orientation), not an ordinary interior label.

---

## 2. What the M5 sign actually says

M5-685 gives on the retained hysteretic branch

\[
\boxed{
\overline{G_\Phi(0)}<0.
}
\]

In regular label-plane coordinates this becomes

\[
\boxed{
\overline{\int j(q,\theta)dq}<0.
}
\]

No measure-theoretic principle implies from this alone that

\[
\overline{j(0^+,\theta)}<0.
\]

A global integral sign is weaker than a boundary trace sign.

---

## 3. Explicit reduced-label countermodel

Take the regular half-strip

\[
0<q<1,
\qquad
|z|<z_*.
\]

Define

\[
\boxed{
\kappa(q,z)=z.
}
\]

Choose the reduced label velocity

\[
\boxed{
V_L=(\mathscr H,K)
=\left(0,\,j(q)+\frac12z^2\right).
}
\]

Then

\[
\partial_q\mathscr H+\partial_zK
=0+z
=\kappa.
\]

Hence the exact M17-013 area-divergence law

\[
\boxed{\operatorname{div}V_L=\kappa}
\]

is satisfied.

Since `kappa_theta=0`, the material crossing rate is

\[
\begin{aligned}
h
&=D_L\kappa\\
&=V_L\cdot\nabla\kappa\\
&=K.
\end{aligned}
\]

On the zero level `z=0`,

\[
\boxed{h(q,0)=j(q).}
\]

Also

\[
|\nabla\kappa|=1,
\]

so

\[
\boxed{G_\Phi(0)=\int_0^1j(q)dq.}
\]

---

## 4. Global negative current with positive nodal-side trace

Choose a smooth function `j(q)` such that

\[
\boxed{j(q)>0\quad\text{for }0<q<\varepsilon}
\]

but

\[
\boxed{
\int_0^1j(q)dq<0.
}
\]

For example, smooth a piecewise profile that is `+1` near `q=0` and `-2` on most of the remaining interval.

Then

\[
\boxed{G_\Phi(0)<0}
\]

while

\[
\boxed{j(0^+)>0.}
\]

Therefore the global M5 sign and the nodal-side trace can have opposite signs without violating the reduced label divergence law.

---

## 5. Why this is the relevant firewall

The example is not asserted to be a Navier--Stokes solution.

Its role is narrower: it satisfies the reduced label-plane structural law

\[
\operatorname{div}V_L=\kappa
\]

and the exact regular M5 current representation of M17-179, yet it violates the desired implication

\[
G_\Phi(0)<0
\Longrightarrow
j(0^+)<0.
\]

Hence no proof based only on

1. the label-area Jacobian law;
2. regular coarea;
3. the global M5 current sign

can determine the nodal boundary trace.

A genuinely PDE-specific localization theorem is necessary.

---

## 6. Consequence for the nodal octupole bridge

M17-090 relates the nodal-core crossing rate to

\[
O_V.
\]

To use M5-685 for `O_V`, one must first prove that a nonzero portion of the negative regular current is localized to the nodal boundary and converges to the nodal crossing rate.

Symbolically, one needs a statement of the form

\[
\boxed{
\liminf_{\varepsilon\downarrow0}
\frac{1}{\mathcal N(\varepsilon)}
\overline{
\int_{0<q<\varepsilon}
 j(q,\theta)dq
}<0
}
\]

with a normalization `N(epsilon)` strong enough to produce a nodal trace.

No such estimate follows from M5-685 alone.

---

## 7. Updated status of M17-165--177

The local/global pressure identities in M17-164 and M17-166--171 remain valid.

The M5-forced statements in M17-165 and M17-172--177 require exactly the missing nodal-localization/trace input exposed here.

Thus the correct vertical frontier is

\[
\boxed{
\text{regular M5 hysteresis}
\stackrel{?}{\longrightarrow}
\text{nodal trace localization}
\longrightarrow
O_V
\longrightarrow
\text{local/global axial pressure architecture}.
}
\]

The first arrow, not the last, is now the primary missing bridge.

---

## 8. DSD audit

### Audit A — global-to-local sign inference
Rejected by the explicit reduced-label countermodel.

### Audit B — treating the nodal critical level as an ordinary positive-flux label
Rejected by M17-178--179.

### Audit C — interpreting the countermodel as a Navier--Stokes counterexample
Rejected. It is a firewall model for the reduced kinematic implication only.

### Audit D — proof status
The correction removes an unjustified sign transfer and sharpens the required theorem.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
