# Smooth-Only Tightrope Frontier — 2026-08-20

Overall status: **ACTIVE 3D NAVIER--STOKES PROOF ATTEMPT ON THE ORIGINAL SMOOTH SOLUTION. GLOBAL REGULARITY NOT PROVED.**

The proof mainline is now deliberately restricted to finite first-hitting stages `t<T*`. Ancient limits and compact recurrent profiles are demoted to discovery/audit tools only.

## 1. Rigor labels

From this point onward:

- **S-level**: proved directly for the original smooth solution on a finite stage;
- **L-level**: proved only for a limiting/compact object and not yet pulled back uniformly;
- **Pruned**: reduced to another typed branch but not contradicted.

Only S-level statements may close the main proof.

## 2. Exact smooth stage ledger

For the running vorticity envelope `M(t)` and

\[
\chi=\frac{\|\nabla\Sigma\|_2^2}{\|\Sigma\|_2^2},
\]

every finite geometric stage `M_j -> q M_j` satisfies

\[
\boxed{
\frac12\log\frac{\chi_1}{\chi_0}
+\frac12\log q
+\nu\int
\left(
\frac{H}{P}-\frac{P}{E}
\right)ds
=
\int
\left(
\frac NP-\frac AE
\right)ds.
}
\]

The viscous spectral-gap term is nonnegative.

This is now the central balance equation.

## 3. Temporal gate

If

\[
\Delta\log\chi<-rac12\log q,
\]

the normalized derivative frequency collapses by at least `q^(-1/2)` and the stage leaves the persistent derivative-core lane.

Otherwise

\[
\int\left(\frac NP-\frac AE\right)_+ds
\ge\frac14\log q.
\]

At least half of this action occurs either

- during record growth `b>0`, or
- on a plateau `b=0`.

Plateau payment forces positive frequency variation or a fixed hyperdissipative spectral-gap payment.

Record payment yields an actual record time satisfying

\[
\boxed{
\frac NP\ge\frac b8.
}
\]

## 4. Record-point incompatibility

At a smooth vorticity record point,

\[
G\xi=0,
\qquad
b+\nu|G|^2\le\xi^T\Sigma\xi.
\]

With

\[
\delta_{align}=s_3-\xi^T\Sigma\xi,
\qquad
\Delta_*=s_3-b-\delta_{align},
\]

one has

\[
|G(y_*)|^2\le\Delta_*/\nu.
\]

The local H1 production density obeys

\[
(n_{H1})^+
\le
\frac{|\Sigma|}{\sqrt2\nu}\Delta_*.
\]

Thus a record point cannot be simultaneously amplification-efficient, diffusion-light, and a strong local H1 producer.

## 5. Record-ball capacity

If

\[
K_2=\|\nabla^2\Omega\|_\infty,
\]

then on `B_r(y_*)`,

\[
\boxed{
Q_r
\le
\frac{4\pi}{3}r^3
\left(
\sqrt{\Delta_*/\nu}+K_2r
\right)^2.
}
\]

Large derivative overlap therefore forces record slack, radius growth, or curvature growth.

## 6. Record-time production gives an instantaneous palinstrophy floor

At the selected record time `N/P >= b/8`, Hardy--Biot--Savart yields

\[
\boxed{
Q
\ge
\frac{\pi}{30^{5/2}}
 b^{5/2}K_2^{-1/2}.
}
\]

This is finite-stage and instantaneous.

## 7. Spatial H1 overlap closes the chain

If a record ball captures a fraction `alpha` of the positive H1 production, then

\[
\frac{Q_r}{Q}
\ge
\frac{\alpha b}{8\sqrt2 B_r^S}.
\]

Combining all S-level estimates gives

\[
\boxed{
\Delta_*
\ge
\nu
\left[
C_*
\frac{\alpha^{1/2}b^{7/4}}
{(B_r^S)^{1/2}K_2^{1/4}r^{3/2}}
-K_2r
\right]_+^2,
}
\]

with

\[
C_*\approx0.00366713224.
\]

This is the current direct closure inequality.

## 8. What is and is not closed

The present radius comparison does **not** yet yield a contradiction by itself. The analytic leakage radius and the new overlap radius are both lower-radius constraints, so treating them as opposing bounds would be incorrect.

The remaining mainline parameter is now the spatial overlap fraction

\[
\boxed{\alpha.}
\]

The proof-producing question is:

> On a smooth non-turnover single-core first-hitting stage, how small can the fraction of positive H1 production lying in the vorticity record core actually be?

If `alpha` has a fixed positive lower bound, the record-overlap inequality forces a quantitative record slack/radius/curvature cost.

If `alpha -> 0`, the H1 production core separates from the vorticity amplitude core, which is exactly the spatial derivative non-tightness / turnover route.

Thus `alpha` is no longer an arbitrary technical constant: it is the explicit switch between the two remaining smooth branches.

## 9. Immediate next target

Derive `alpha` from the existing non-turnover parent-core hypotheses using one of:

1. a finite-radius H1 production localization identity;
2. a low-leakage parent-buffer estimate;
3. a material-core overlap/packing argument;
4. the existing high-strain derivative-active ball selection, rewritten around the actual vorticity record core.

The target must be finite-stage and uniform before it is admitted to the mainline.

Status: **THE MAIN PROOF HAS MOVED TO A SINGLE SMOOTH FINITE-STAGE TIGHTROPE. THE CURRENT SWITCH PARAMETER IS THE RECORD/H1 SPATIAL OVERLAP FRACTION `alpha`: POSITIVE `alpha` FORCES RECORD COST; VANISHING `alpha` IS ITSELF SPATIAL SEPARATION.**