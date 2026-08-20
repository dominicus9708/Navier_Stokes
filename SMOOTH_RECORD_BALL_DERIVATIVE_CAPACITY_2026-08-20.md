# Smooth Record-Ball Derivative Capacity — 2026-08-20

Status: **S-LEVEL LOCAL CAPACITY LEMMA ON A FINITE SMOOTH FIRST-HITTING STAGE. GLOBAL REGULARITY NOT PROVED.**

This note turns the pointwise record-growth/H1 tradeoff into a finite-radius statement. The purpose is to distinguish, without any limiting profile, whether the derivative-active `P_V` packet genuinely overlaps the vorticity record core.

## 1. Inputs at a record-growth time

At a time with positive running-envelope growth choose a record point `y_*` as in `SMOOTH_RECORD_POINT_GROWTH_H1_TRADEOFF_2026-08-20.md`.

Let

\[
G=\nabla_y\Omega,
\qquad
K_2=\|\nabla_y^2\Omega\|_\infty.
\]

Define

\[
\delta_{align}=s_3-\xi^T\Sigma\xi\ge0
\]

and the record slack

\[
\boxed{
\Delta_*=s_3-b-\delta_{align}\ge0.
}
\]

The record-point inequality gives

\[
\boxed{
|G(y_*)|^2\le\frac{\Delta_*}{\nu}.
}
\]

## 2. Hessian regularity propagates the pointwise constraint to a ball

For

\[
B_r=B_r(y_*),
\]

the fundamental theorem of calculus gives

\[
|G(y)-G(y_*)|
\le K_2|y-y_*|
\le K_2r.
\]

Hence throughout the record ball,

\[
\boxed{
|G(y)|
\le
\sqrt{\frac{\Delta_*}{\nu}}
+K_2r.
}
\]

Therefore the vorticity palinstrophy contained in the record ball satisfies

\[
Q_r
:=
\int_{B_r}|\nabla\Omega|^2dy
\]

and

\[
\boxed{
Q_r
\le
\frac{4\pi}{3}r^3
\left(
\sqrt{\frac{\Delta_*}{\nu}}
+K_2r
\right)^2.
}
\]

This is an explicit derivative-capacity upper bound for an efficiently amplifying record core.

## 3. Invert the capacity inequality

Suppose a branch requires the record ball to contain at least a fraction `alpha` of a known palinstrophy amount `Q0`:

\[
Q_r\ge\alpha Q_0,
\qquad 0<\alpha\le1.
\]

Then

\[
\sqrt{\frac{\Delta_*}{\nu}}
\ge
\left[
\sqrt{
\frac{3\alpha Q_0}{4\pi r^3}
}
-K_2r
\right]_+,
\]

so

\[
\boxed{
\Delta_*
\ge
\nu
\left[
\sqrt{
\frac{3\alpha Q_0}{4\pi r^3}
}
-K_2r
\right]_+^2.
}
\]

Thus fixed derivative overlap imposes a definite record inefficiency/diffusion slack whenever the required derivative mass is too large to fit into the analytic ball at near-zero gradient.

## 4. Record-core radius form

Equivalently, if the record slack is known to obey

\[
\Delta_*\le\Delta_0,
\]

then every ball carrying derivative mass `alpha Q0` must satisfy

\[
\boxed{
\frac{4\pi}{3}r^3
\left(
\sqrt{\frac{\Delta_0}{\nu}}+K_2r
\right)^2
\ge
\alpha Q_0.
}
\]

Hence a diffusion-light, spectrally efficient record core has a minimum radius if it is also required to carry a fixed amount of derivative mass.

## 5. Local H1 production capacity

The universal local nonnormality bound is

\[
(n_{H1})^+
\le
\frac{|\Sigma|}{\sqrt2}|G|^2.
\]

Let

\[
B_r^S=\|\Sigma\|_{L^\infty(B_r)}.
\]

Then the positive H1 production inside the record ball satisfies

\[
N_r^+
\le
\frac{B_r^S}{\sqrt2}Q_r.
\]

Using the capacity estimate,

\[
\boxed{
N_r^+
\le
\frac{4\pi}{3\sqrt2}
B_r^S r^3
\left(
\sqrt{\frac{\Delta_*}{\nu}}+K_2r
\right)^2.
}
\]

Therefore an efficiently growing small record ball has limited capacity not only for derivative mass but also for positive local H1 production.

## 6. Finite-stage overlap dichotomy

At a record-growth time fix a natural/analytic radius `r` and compare the record ball with the full derivative-active state.

### O1 — small record overlap

If

\[
\frac{Q_r}{Q}\ll1
\]

or

\[
\frac{N_r^+}{N^+}\ll1,
\]

then the vorticity-amplitude record core and the derivative/H1-production core are spatially separated.

This is not declared a contradiction by itself. It is routed to the already isolated spatial derivative non-tightness / turnover problem.

### O2 — large record overlap

If

\[
Q_r\ge\alpha Q_0
\]

for fixed `alpha,Q0>0`, the inverted capacity bound forces a positive `Delta_*` unless the record radius is sufficiently large.

Since

\[
\Delta_*
=s_3-b-\delta_{align},
\]

large overlap cannot coexist freely with all three of:

- near-maximal extensional amplification `b ~ s3`;
- small alignment defect;
- small vorticity-gradient diffusion.

### O3 — analytic spreading

If `K2 r` alone accounts for the derivative capacity, then a large derivative packet has been created across a finite spatial radius rather than at the record point itself. This feeds the finite-radius derivative-spreading/H analysis rather than opening a new equality regime.

## 7. Connection with the direct P_V-to-H lower bound

Whenever another smooth finite-stage estimate supplies a lower bound

\[
Q\ge Q_0,
\]

the present lemma immediately converts a chosen overlap fraction into either

- a positive record slack `Delta_*`;
- a minimum record-core radius;
- or failure of derivative overlap.

The previous Hardy--Biot--Savart calculation is one possible supplier of such a `Q0`, but the capacity lemma itself does not depend on ancient recurrence or on that particular lower bound.

## 8. Current mainline

The smooth proof line is now

\[
\boxed{
\text{finite-stage tightrope ledger}
\to
\text{record growth/H1 pointwise tradeoff}
\to
\text{record-ball derivative-capacity dichotomy}.
}
\]

The next task is temporal: quantify how much of the stage-integrated cross-order production excess

\[
\int_{I_j}\left(\frac NP-\frac AE\right)ds
\]

must occur during actual record-growth times rather than on plateaus of the running maximum. Plateau-dominated production should force normalized derivative-frequency growth or viscous hyperdissipation directly from the same smooth ledger.

Status: **A SMOOTH RECORD CORE HAS AN EXPLICIT FINITE DERIVATIVE/H1 CAPACITY. SIGNIFICANT P_V OVERLAP FORCES RECORD INEFFICIENCY OR DIFFUSIVE COST; SMALL OVERLAP ROUTES TO SPATIAL DERIVATIVE SEPARATION. NEXT = TEMPORAL RECORD/PLATEAU OVERLAP.**