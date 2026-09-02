# DSD M5-589 — Thicken finite-depth production sphere to a positive spacetime annulus

Date: 2026-09-03

Status: **M5-587'S SINGLE FINITE-DEPTH PRODUCTION SPHERE CAN BE THICKENED, USING THE COMPACT HULL'S UNIFORM SMOOTHNESS, INTO A FIXED-RADIUS ANNULUS AND FIXED SIMILARITY-TIME WINDOWS WITH POSITIVE FREQUENCY AND POSITIVE VORTEX-STRETCHING SURPLUS. THIS CONVERTS THE EULERIAN SPHERE MARK INTO A POSITIVE SPACETIME-VOLUME PRODUCTION EVENT SUITABLE FOR M5-497'S LOCAL-PAYER GENEALOGY. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Input from M5-587/M5-588

There exists a finite radius

\[
\rho_*\in(0,\infty)
\]

such that

\[
\boxed{
\left\langle
\int_{S_{\rho_*}}
\bigl(W\cdot\Sigma W-|\nabla W|^2\bigr)dS
\right\rangle
=
\frac14
\left\langle
\int_{S_{\rho_*}}|W|^2dS
\right\rangle
=:m_*>0.
}
\]

Define

\[
g(r,\theta)
:=
\int_{S_r}
\bigl(W\cdot\Sigma W-|\nabla W|^2\bigr)dS.
\]

Then

\[
\langle g(\rho_*,\cdot)\rangle=m_*>0.
\]

## 2. Uniform continuity on the compact hull

M5-508 and the later compact-hull reductions give uniform bounds on every fixed spatial derivative on every fixed bounded region.

Hence there exist finite constants

\[
M_g,L_r,L_\theta<\infty
\]

such that, on a fixed neighborhood of \(\rho_*\),

\[
|g(r,\theta)|\le M_g,
\]

and

\[
|g(r_1,\theta_1)-g(r_2,\theta_2)|
\le
L_r|r_1-r_2|+L_\theta|\theta_1-\theta_2|.
\]

This uses only the already inherited smooth compactness; no new regularity hypothesis is added.

## 3. Positive-mean event set has positive density

Let

\[
\mathcal T_*
:=
\{\theta:g(\rho_*,\theta)\ge m_*/2\}.
\]

If the invariant density of \(\mathcal T_*\) were zero, then the invariant mean could not equal \(m_*>0\).

More quantitatively, if \(d_*\) denotes its lower invariant density, then

\[
m_*
\le
d_*M_g+(1-d_*)\frac{m_*}{2},
\]

so

\[
\boxed{
d_*
\ge
\frac{m_*}{2M_g-m_*}>0.
}
\]

## 4. Radial thickening

Choose

\[
\delta_r
\le
\frac{m_*}{8L_r}
\]

(with the obvious harmless convention when \(L_r=0\)).

Then for every \(\theta\in\mathcal T_*\) and every

\[
|r-\rho_*|\le\delta_r,
\]

we have

\[
g(r,\theta)
\ge
\frac{m_*}{2}-L_r\delta_r
\ge
\frac{3m_*}{8}.
\]

Therefore on the fixed annulus

\[
\boxed{
\mathcal A_*
:=
\{y:\rho_*-\delta_r<|y|<\rho_*+\delta_r\},
}
\]

one has

\[
\boxed{
\int_{\mathcal A_*}
\bigl(W\cdot\Sigma W-|\nabla W|^2\bigr)dy
\ge
\frac{3}{4}\delta_r m_*
=:c_{ann}>0
}
\]

at every time in \(\mathcal T_*\).

In particular, because the palinstrophy term is nonnegative,

\[
\boxed{
\int_{\mathcal A_*}W\cdot\Sigma W\,dy
\ge c_{ann}>0.
}
\]

Thus the annulus carries a fixed positive local vortex-stretching production charge.

## 5. Similarity-time thickening

Choose

\[
\delta_\theta
\le
\frac{m_*}{16L_\theta}.
\]

If \(\theta_0\in\mathcal T_*\), then for

\[
|\theta-\theta_0|\le\delta_\theta
\]

and

\[
|r-\rho_*|\le\delta_r,
\]

the same continuity estimate yields a fixed lower bound, for example

\[
g(r,\theta)\ge \frac{m_*}{4}.
\]

Hence every marked production time contains a fixed spacetime block

\[
I_{\theta_0}\times\mathcal A_*,
\qquad
|I_{\theta_0}|=2\delta_\theta,
\]

with

\[
\boxed{
\int_{I_{\theta_0}}
\int_{\mathcal A_*}
W\cdot\Sigma W\,dy\,d\theta
\ge
c_{st}>0.
}
\]

After the standard bounded-overlap selection of the event intervals, these blocks still occur with positive similarity-time density.

## 6. Why this solves the measure-zero sphere problem

M5-588 correctly maintained a firewall between

1. a material-lineage object, and
2. a single Eulerian sphere.

The present step removes the purely codimension-one part of that firewall.

The production object is now a fixed positive-volume annulus, persisting for a fixed positive similarity-time duration on a positive-density event set.

Therefore the local-payer extraction mechanism of M5-497 can be applied inside this same finite-depth region.

## 7. What is not yet claimed

This note does **not** yet claim that the previously selected M5-490 pair itself occupies \(\mathcal A_*\).

The valid statement is only

\[
\boxed{
\text{finite-depth sphere production}
\Longrightarrow
\text{positive-density finite-depth spacetime annular production}.
}
\]

The next step is to use M5-497's finite-payer saturation inside \(\mathcal A_*\) to identify which persistent material lineage pays this production.

Status: **THE PRODUCTION SPHERE HAS BEEN UPGRADED TO A POSITIVE-VOLUME, POSITIVE-TIME, POSITIVE-FREQUENCY ANNULAR PRODUCTION EVENT. THE GENEALOGICAL OVERLAP PROBLEM IS NOW ELIGIBLE FOR THE EXISTING LOCAL-PAYER SATURATION THEOREM. GLOBAL REGULARITY REMAINS UNPROVED.**