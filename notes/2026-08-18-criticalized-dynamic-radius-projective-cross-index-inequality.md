# Criticalized dynamic-radius projective inequality: a scale-to-derivative-order bridge

Date: 2026-08-18

Status: **DERIVED CROSS-INDEX INEQUALITY FROM THE EXACT ENERGY-WEIGHTED DERIVATIVE PROJECTIVE IDENTITY. A PROJECTIVELY ROUGH STATE CANNOT MIGRATE THROUGH AN ARBITRARILY LARGE FREQUENCY RATIO WHILE KEEPING THE SCALE-CRITICAL FACTORIAL NONLINEAR FORCING SMALL. THE ESCAPE IS PROJECTIVE COHERENCE OR CRITICAL FORCING/DERIVATIVE-RADIUS BLOWUP. GLOBAL REGULARITY NOT PROVED.**

## 1. Start from the exact factorial projective ledger

For derivative order `m`, let

\[
E_m=\sum_{|I|=m}\|\partial_I\omega\|_2^2,
\]

\[
C_m=\frac{N_m}{E_m},
\qquad
J_m=1-\operatorname{tr}(C_m^2),
\qquad
D_m=E_mJ_m.
\]

For factorial weights

\[
a_m(\ell)=\frac{\ell^{2m}}{(m!)^2},
\]

define

\[
\mathfrak D_\ell=\sum_{m\ge0}a_mD_m.
\]

The previously derived exact identity for a nonincreasing dynamic radius `ell(t)` gives schematically

\[
\begin{aligned}
\dot{\mathfrak D}_\ell
&+2\frac{-\dot\ell}{\ell}\sum_{m\ge1}m a_mD_m\\
&+\frac{2\nu}{\ell^2}\sum_{m\ge1}m^2a_mD_m\\
&+2\nu\sum_{m\ge0}a_mE_{m+1}\|C_{m+1}-C_m\|_F^2\\
&\le
6\mathfrak D_\ell^{1/2}\mathfrak F_\ell,
\end{aligned}
\]

where

\[
\mathfrak F_\ell
=\left(\sum_m(F_m^\#)^2\right)^{1/2}
\]

is the factorial nonlinear forcing amplitude.

The same algebra applies to a forced band/localized component, with projection/commutator/moving-window terms included in the forcing.

## 2. Criticalize the projective functional

Vorticity derivative energy `E_0=||omega||_2^2` scales like inverse length.  Therefore

\[
\boxed{
\mathfrak P_\ell:=\ell\mathfrak D_\ell
}
\]

is scale invariant.

Let

\[
r_\ell=-\frac{\dot\ell}{\ell}\ge0.
\]

Differentiate:

\[
\dot{\mathfrak P}_\ell
=\dot\ell\mathfrak D_\ell
+\ell\dot{\mathfrak D}_\ell
=-r_\ell\mathfrak P_\ell
+\ell\dot{\mathfrak D}_\ell.
\]

Insert the factorial inequality and discard the additional nonnegative damping terms.  This yields

\[
\boxed{
\dot{\mathfrak P}_\ell
+r_\ell\mathfrak P_\ell
\le
6\ell\mathfrak D_\ell^{1/2}\mathfrak F_\ell.
}
\]

Since

\[
\ell\mathfrak D_\ell^{1/2}
=\mathfrak P_\ell^{1/2}\ell^{1/2},
\]

define the scale-critical forcing

\[
\boxed{
\mathfrak F_{\rm crit}
:=\ell^{1/2}\mathfrak F_\ell.
}
\]

Then

\[
\boxed{
\dot{\mathfrak P}_\ell
+r_\ell\mathfrak P_\ell
\le
6\mathfrak P_\ell^{1/2}\mathfrak F_{\rm crit}.
}
\]

## 3. Square-root form

Where `P_ell>0`, divide by `2 sqrt(P_ell)`:

\[
\boxed{
\frac d{dt}\sqrt{\mathfrak P_\ell}
+\frac12r_\ell\sqrt{\mathfrak P_\ell}
\le
3\mathfrak F_{\rm crit}.
}
\]

Integrating over an interval `[t0,t1]` gives

\[
3\int_{t_0}^{t_1}\mathfrak F_{\rm crit}dt
\ge
\sqrt{\mathfrak P_\ell(t_1)}
-\sqrt{\mathfrak P_\ell(t_0)}
+\frac12\int_{t_0}^{t_1}r_\ell\sqrt{\mathfrak P_\ell}dt.
\]

## 4. Frequency-migration consequence

Track an active physical scale by

\[
\ell(t)\asymp K(t)^{-1}.
\]

Then

\[
\int r_\ell dt
=\log\frac{\ell(t_0)}{\ell(t_1)}
=\log\frac{K(t_1)}{K(t_0)}.
\]

Suppose a projectively rough critical component satisfies

\[
\mathfrak P_\ell(t)\ge p_0>0
\]

throughout the migration from `K0` to `K1`.  Then

\[
\boxed{
\int_{t_0}^{t_1}\mathfrak F_{\rm crit}dt
\gtrsim
\sqrt{p_0}\log\frac{K_1}{K_0}
-O(\sqrt{\mathfrak P(t_0)}+\sqrt{\mathfrak P(t_1)}).
}
\]

For a long frequency ratio the endpoint term is lower order.

Thus every logarithmic scale interval traversed while retaining a nonzero critical projective defect requires a fixed amount of scale-critical factorial forcing.

## 5. Local/band interpretation

For a natural packet at frequency `K`,

\[
E_0\asymp K,
\qquad
\ell\asymp K^{-1}.
\]

If the packet/band projective defect is `J>=j0`, then already the zeroth-order term gives

\[
\ell D_0
=\ell E_0J
\gtrsim j_0.
\]

Hence `P_ell>=p0` is exactly a scale-critical statement.

For a moving Littlewood--Paley / Gaussian band, the derivative of the moving projection contributes extra terms.  These must be included in `F_crit`; they are precisely radial-band transfer / scale-modulation forcing rather than an unpriced error.

## 6. Resulting trichotomy

A hypothetical high-frequency migration must choose:

\[
\boxed{
\text{projective coherence: }\mathfrak P_\ell\to0,
}
\]

which returns to signed-coherent tube/flux genealogy;

or

\[
\boxed{
\int\mathfrak F_{\rm crit}dt\to\infty,
}
\]

which is a scale-critical nonlinear/commutator/derivative forcing branch;

or the factorial description itself loses its controlled radius / forcing majorant, which is the analytic-radius / endpoint derivative concentration branch.

This supplies an explicit bridge between physical-scale migration and derivative-order projective structure.

## 7. Why this is not yet global regularity

There is no known globally finite a-priori budget for

\[
\int\mathfrak F_{\rm crit}dt
\]

near a hypothetical singularity.  Divergence of this critical forcing is compatible with blow-up.

Therefore the inequality closes a bookkeeping gap but does not rule out the critical cascade.

Status: **FIRST EXPLICIT SCALE-ORDER CROSS-INDEX PROJECTIVE INEQUALITY / ROUGH SCALE MIGRATION PAYS LOG-FREQUENCY CRITICAL FACTORIAL FORCING / ESCAPE = COHERENCE OR CRITICAL FORCING/RADIUS COLLAPSE / GLOBAL REGULARITY NOT PROVED.**