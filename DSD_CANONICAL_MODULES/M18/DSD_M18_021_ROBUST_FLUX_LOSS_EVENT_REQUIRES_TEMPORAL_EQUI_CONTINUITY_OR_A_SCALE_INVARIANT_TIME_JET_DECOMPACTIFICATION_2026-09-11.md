# M18-021 — Robust flux-loss event requires temporal equicontinuity or a scale-invariant time-jet decompactification

**Date:** 2026-09-11  
**Status:** ACTIVE DSD ANALYSIS / TEMPORAL-EQUICONTINUITY FIREWALL / ROBUST EVENT CORRECTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose and correction to M18-020

M18-020 proved a correct conditional statement: if the half-flux-loss event occupies a time set of positive measure, then a measurable partition converts that time measure directly into one of the three spacetime payers from M18-019 without differentiating the payer itself.

However, its operational active set was written using the exact threshold equality

\[
F(\ell(t),t)=\frac12J(t).
\]

A smooth scalar function may cross an exact threshold at isolated times. Therefore exact equality does not by itself provide positive time measure.

This module replaces the operational event by a robust two-threshold inequality and audits what is required for its time measure to collapse.

M18-020 remains valid as a conditional measure-to-payer theorem; only the route used to produce the active time measure is refined here.

## 2. Weighted coefficient-level flux

On a regular exact CE-H coefficient tube, write

\[
\Sigma_s(t):=\{x:\kappa(x,t)=s\},
\qquad
g:=|\nabla\kappa|,
\]

and

\[
\boxed{
F(s,t):=\int_{\Sigma_s(t)}\rho^2g\,dS,
\qquad
J(t):=F(0,t).
}
\]

Assume throughout the local argument that

\[
J(t)>0.
\]

For a fixed regular witness level \(s_*\) that remains inside the retained tube, define the normalized flux ratio

\[
\boxed{
q_{s_*}(t):=\frac{F(s_*,t)}{J(t)}.
}
\]

This ratio is invariant under the physical Navier--Stokes record scaling because both numerator and denominator scale as \(R^5\).

## 3. Two-threshold robust event

Fix

\[
0<\theta_-<\theta_+<1,
\qquad
\gamma:=\theta_+-\theta_->0.
\]

A selected time \(t_0\) has a **strict flux-loss witness** if

\[
\boxed{
q_{s_*}(t_0)\le\theta_-.
}
\]

Define the robust active event by

\[
\boxed{
\mathcal A_{\theta_+}
:=
\left\{
 t:
\exists s\text{ in the retained regular tube with }
F(s,t)\le\theta_+J(t)
\right\}.
}
\]

At every \(t\in\mathcal A_{\theta_+}\), continuity in the coefficient level and

\[
F(0,t)=J(t)>\theta_+J(t)
\]

give a first level \(\ell(t)\) satisfying

\[
F(\ell(t),t)=\theta_+J(t).
\]

Therefore the M18-019 spatial payer decomposition applies at each robust active time, now with \(\theta=\theta_+\).

For the concrete choice

\[
\theta_-=\frac14,
\qquad
\theta_+=\frac12,
\]

a quarter-flux witness generates the half-flux active event, leaving a fixed margin \(\gamma=1/4\).

## 4. Intrinsic coefficient-time coordinate

A physical coefficient slab width scales as

\[
\delta_R=R^2\delta,
\]

while record time scales as

\[
ds=R^{-2}dt.
\]

Hence the product

\[
\delta\,dt
\]

is scale invariant.

Define the local coefficient-time coordinate

\[
\boxed{
\vartheta(t;t_0)
:=
\int_{t_0}^{t}\delta(r)\,dr.
}
\]

This is representation safe under the certified physical record scaling.

It is the natural temporal coordinate for asking whether a coefficient-level shape changes rapidly relative to its own coefficient scale.

## 5. Uniform-modulus persistence theorem

Assume a same-branch regular-tube time window \(W\) around \(t_0\) on which

\[
0<\delta_*\le\delta(t)\le\delta^*<\infty,
\]

\[
J(t)\ge j_*>0,
\]

and the fixed witness level \(s_*\) remains a regular level inside the tube.

Suppose the family of normalized ratios has a record-uniform modulus of continuity in coefficient time:

\[
\boxed{
|q_{s_*}(t)-q_{s_*}(t_0)|
\le
\omega\bigl(|\vartheta(t;t_0)|\bigr),
}
\]

where

\[
\omega(r)\downarrow0
\qquad(r\downarrow0)
\]

is independent of the record.

Choose \(r_\gamma>0\) such that

\[
\omega(r_\gamma)\le\gamma.
\]

If

\[
q_{s_*}(t_0)\le\theta_-,
\]

then for all times with

\[
|\vartheta(t;t_0)|\le r_\gamma
\]

inside the same-branch window,

\[
q_{s_*}(t)
\le
\theta_-+\gamma
=
\theta_+.
\]

Thus those times belong to \(\mathcal A_{\theta_+}\).

Since \(\delta(t)\le\delta^*\), a one-sided same-branch window of available length \(w_*\) gives

\[
\boxed{
|\mathcal A_{\theta_+}|
\ge
\min\left\{
 w_*,
\frac{r_\gamma}{\delta^*}
\right\}.
}
\]

Therefore a strict flux-loss witness plus uniform coefficient-time equicontinuity gives a positive record-uniform active duration.

## 6. Scale-invariant temporal flux-shape jet

A differentiable sufficient condition for the modulus theorem is obtained from

\[
\boxed{
\Theta_{s_*}(t)
:=
\frac1{\delta(t)}
\left|
\frac{d}{dt}
\frac{F(s_*,t)}{J(t)}
\right|.
}
\]

Under physical record scaling,

\[
F_R=R^5F,
\qquad
J_R=R^5J,
\]

so \(q_R=q\). Its time derivative scales as \(R^2\), exactly like \(\delta\). Hence

\[
\boxed{
\Theta_{s_*}\text{ is scale invariant.}
}
\]

If

\[
\Theta_{s_*}(t)\le\Theta_*<\infty
\]

on the same-branch window, then

\[
|q_{s_*}(t)-q_{s_*}(t_0)|
\le
\Theta_*|\vartheta(t;t_0)|.
\]

Consequently one may take

\[
r_\gamma=\frac{\gamma}{\Theta_*},
\]

and obtain

\[
\boxed{
|\mathcal A_{\theta_+}|
\ge
\min\left\{
 w_*,
\frac{\gamma}{\Theta_*\delta^*}
\right\}.
}
\]

This is the quantitative temporal-thickness theorem for a robust flux-loss margin.

## 7. Contrapositive: exact temporal-thinning classification

Suppose along a record sequence

\[
q_{s_m}(t_m)\le\theta_-<\theta_+
\]

with uniform strict margin, while

\[
J_m\ge j_*>0,
\qquad
0<\delta_*\le\delta_m\le\delta^*,
\]

and a nonvanishing same-branch regular-tube window survives.

If nevertheless

\[
|\mathcal A_{\theta_+,m}|\to0,
\]

then the family cannot remain uniformly equicontinuous in the invariant coefficient-time variable.

In the differentiable case,

\[
\boxed{
|\mathcal A_{\theta_+,m}|\to0
\quad\Longrightarrow\quad
\sup_W\Theta_{s_m}\to\infty,
}
\]

unless one of the compactness assumptions fails.

Thus the previous vague branch

\[
G_{\rm active\text{-}time\ thinning}
\]

is refined to

\[
\boxed{
\begin{aligned}
G_{\rm active\text{-}time\ thinning}
\Longrightarrow{}&
G_{\rm temporal\ flux\text{-}shape\ jet}\\
&\lor G_{\rm margin\ loss/tangency}\\
&\lor G_{J\text{-}floor\ loss}\\
&\lor G_{\rm tube/regular\ level\ loss}\\
&\lor G_{\rm same\text{-}branch/genealogy\ window\ loss}.
\end{aligned}
}
\]

Here `margin loss/tangency` means that only an exact threshold touch is known, with no record-uniform gap \(\gamma>0\).

## 8. Exact transport velocity for fixed coefficient levels

The temporal flux-shape jet can be audited directly without confusing coefficient-level transport with material transport.

Let

\[
h:=D_t\kappa
=\partial_t\kappa+u\cdot\nabla\kappa.
\]

A fixed coefficient level \(\Sigma_s(t)\) is transported by

\[
\boxed{
w
=u-\frac{h}{g^2}\nabla\kappa
=u-\frac hg n.
}
\]

Indeed,

\[
(\partial_t+w\cdot\nabla)\kappa
=D_t\kappa-h=0.
\]

Thus \(w\) is the correct Eulerian transport velocity of a fixed physical coefficient level.

## 9. Exact time derivative of the level flux

Let

\[
a_n:=n\cdot(\nabla u)n.
\]

On exact CE-H,

\[
D_t\rho=(\sigma+\nu\kappa)\rho,
\]

where \(\nu>0\) is the viscosity.

Also

\[
D_t\nabla\kappa
=\nabla h-(\nabla u)^T\nabla\kappa,
\]

so

\[
D_t g
=\partial_n h-g a_n.
\]

Using the surface transport formula with velocity \(w\), together with

\[
\operatorname{div}_\Sigma u=-a_n
\]

and

\[
\frac{\partial_ng}{g}+\mathcal H_\Sigma
=
\frac{\Delta\kappa}{g}
\]

from M18-016 (legacy M17-482), one obtains

\[
\boxed{
\begin{aligned}
\partial_tF(s,t)
=\int_{\Sigma_s(t)}
\Bigg[&
2(\sigma+\nu s-a_n)\rho^2g\\
&-2\rho h\,\partial_n\rho
+\rho^2\partial_n h
-\rho^2h\frac{\Delta\kappa}{g}
\Bigg]dS.
\end{aligned}
}
\]

At the zero level,

\[
\boxed{
\begin{aligned}
\dot J
=\int_{\Sigma_0(t)}
\Bigg[&
2(\sigma-a_n)\rho^2g\\
&-2\rho h\,\partial_n\rho
+\rho^2\partial_n h
-\rho^2h\frac{\Delta\kappa}{g}
\Bigg]dS.
\end{aligned}
}
\]

These formulas are valid only while the relevant levels remain regular and the surface transport is justified.

## 10. What the temporal jet actually contains

M17-339 gives the physical coefficient constitutive law

\[
\boxed{
h=D_t\kappa
=L_\rho\kappa+L_\rho\sigma+\mathcal R_{\rm geom},
}
\]

with

\[
L_\rho f
:=
\rho^{-2}\nabla\cdot(\rho^2\nabla f).
\]

Therefore the exact flux-time derivative contains not only the already-audited spatial level-flux terms but also

\[
\boxed{h\quad\text{and}\quad\partial_n h.}
\]

In particular,

\[
\partial_nL_\rho\kappa
\]

contains a normal derivative of \(\Delta\kappa\) together with weighted lower terms. Thus a direct pointwise bound on the temporal flux jet naturally reaches a **third coefficient jet**.

Through

\[
\Delta\Omega=\kappa\Omega,
\]

a third coefficient jet naturally sits one derivative above the second-coefficient-jet/D4 branch isolated in M18-019. A naive pointwise conversion therefore reaches D5-type vorticity derivatives.

This is only a derivative-order warning, not a certified D5 ancestry ledger: cancellations and weighted identities must be audited before assigning a payer.

## 11. Geometry-source firewall remains necessary

The exact termwise physical formula for \(\mathcal R_{\rm geom}\) is available in M17-339. Nevertheless, M17-463's methodological firewall remains valid:

\[
\boxed{
\text{an exact formula does not by itself justify a lower-resource payer estimate.}
}
\]

In particular, differentiating \(\mathcal R_{\rm geom}\) in the normal direction introduces derivatives of the amplitude, direction, strain, and curl terms appearing in that remainder. No estimate of

\[
\partial_n\mathcal R_{\rm geom}
\]

by the existing palinstrophy/raw-H2/D3 ledgers is certified here.

Thus one must not close the temporal flux-shape branch by dimensional analogy alone.

## 12. Representation audit

The temporal quantity

\[
\Theta_{s_*}
=
\delta^{-1}|\dot q_{s_*}|
\]

is built entirely from the physical coefficient \(\kappa^{ph}\), physical coefficient width, and physical time.

This avoids the representation mixing quarantined by M17-338, where fixed positive similarity levels were incorrectly given physical \(R^2\) coefficient scaling.

The zero level remains representation-compatible, but the present positive witness level must always be interpreted as a physical coefficient level inside one record before scaling it to another record.

## 13. Updated local branch tree

Combining M18-019--021 gives the current compact regular-tube local tree:

\[
\boxed{
\begin{aligned}
G_{\rm robust\ zero\text{-}tube\ flux\ loss}
\Longrightarrow{}&
G_{\rm spacetime\ palinstrophy}^{R^{-1}}\\
&\lor G_{\rm spacetime\ first\ coefficient\ jet/D3}^{R^{-5}}\\
&\lor G_{\rm spacetime\ second\ coefficient\ jet/D4}^{R^{-7}}\\
&\lor G_{\rm temporal\ flux\text{-}shape\ jet/equicontinuity\ loss}\\
&\lor G_{\rm margin/J/tube/critical/domain/genealogy\ loss}.
\end{aligned}
}
\]

This is a sharper classification than treating all short-lived events as an undifferentiated temporal-thinning escape.

## 14. DSD audit verdict

### Certified here

1. The exact-equality active set in M18-020 is not a robust way to obtain positive time measure.
2. A two-threshold inequality event fixes that problem.
3. Uniform equicontinuity in the invariant coefficient-time variable forces positive active duration.
4. The scale-invariant differentiable temporal-shape parameter is
   \[
   \Theta=\delta^{-1}|\partial_t(F/J)|.
   \]
5. Temporal thinning with a strict margin and compact tube forces temporal-shape-jet decompactification or loss of one of the explicit compactness assumptions.
6. The exact fixed-level surface transport formula introduces \(h=D_t\kappa\) and \(\partial_nh\), explaining why a direct PDE bound can encounter a third coefficient jet / D5-type derivative barrier.

### Not certified here

1. A bound on \(\Theta\) by existing ancestral ledgers.
2. A D5 spacetime ledger.
3. An ancestry contradiction from fixed active duration.
4. Control of critical-level or domain/genealogy loss.
5. Global 3D Navier--Stokes regularity.

## 15. Next analysis target

The next DSD audit should split the temporal flux-shape jet itself before any D5 escalation:

\[
\partial_tF
=\text{strain/normal-stretch channel}
+\text{amplitude-transport channel}
+\text{coefficient-rate channel}.
\]

The key question is whether the integrated weighted combination involving

\[
h,\quad\partial_n h
\]

can be reduced by integration by parts, the physical coefficient constitutive law, or already-certified lower-order spacetime resources, leaving a genuine third-coefficient-jet branch only when all lower-order reductions fail.

That is the appropriate M18-022 target.
