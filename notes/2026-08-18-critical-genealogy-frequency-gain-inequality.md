# Critical genealogy frequency-gain inequality

Date: 2026-08-18

Status: **SYNTHESIZED CONDITIONAL GENEALOGY INEQUALITY. AFTER STOPPING-TIME / SEQUENTIAL PRUNING OF ONE COMPACT HIGH-FREQUENCY LINEAGE, THE TOTAL LOGARITHMIC FREQUENCY GAIN IS CONTROLLED BY A FINITE LIST OF SCALE-CRITICAL ACTIONS: PROJECTIVE SCALE-MIGRATION FORCING, BKM RESET ACTION, MATERIAL-PROBE GEOMETRIC DISTORTION, SAME-SCALE PARTNER STRAIN-GRADIENT PRODUCT, AND THE ENDPOINT L3 SIZE OF CLEAN MATERIAL RUNS. THIS IS NOT A FINITE A-PRIORI BOUND AND DOES NOT PROVE REGULARITY.**

## 1. One pruned compact genealogy

Track one dangerous compact/natural-scale genealogy from physical frequency

\[
K_0
\]

to a later frequency

\[
K_*>K_0.
\]

Apply a stopping-time pruning so that the selected intervals/events are sequential and are not repeated descriptions of one persistent episode.

The genealogy is decomposed into the following typed pieces.

### R. Projectively rough migration intervals

The criticalized dynamic-radius projective functional satisfies

\[
\mathfrak P_\ell\ge p_0>0,
\qquad \ell\asymp K^{-1}.
\]

The cross-index inequality gives

\[
\boxed{
\Delta\log K_R
\lesssim
p_0^{-1/2}\int_R\mathfrak F_{\rm crit}dt
}
\]

up to fixed endpoint terms.  Define

\[
\boxed{
\mathcal A_F
:=\int_R\mathfrak F_{\rm crit}dt.
}
\]

### C. Clean signed-coherent material I-runs

On a clean embedded flux-preserving material run from `K_a` to `K_b`, the circulation/tube argument gives

\[
\|u\|_3\gtrsim K_b/K_a.
\]

Let

\[
M_3=\sup_{t\text{ on genealogy}}\|u(t)\|_3.
\]

Then every such run satisfies

\[
\boxed{
\Delta\log K_C
\le
\log(C(2+M_3)).
}
\]

(the harmless `2+` avoids small-norm logarithm conventions).

A clean run ends only when an exceptional event occurs or the genealogy exits the compact lane into a larger coherent merge.

### B. Bounded-shape viscous flux resets

At compact natural scale, the signed flux is order one.  The exact material-probe reset rate gives a fixed BKM action per genuine fixed-fraction reset:

\[
\int_{I_j}\|\omega(t)\|_\infty dt
\ge c_\nu>0.
\]

Define

\[
\boxed{
\mathcal A_{\rm BKM}
:=\int_{\cup B_j}\|\omega(t)\|_\infty dt.
}
\]

For sequential selected reset events,

\[
\boxed{
N_B\lesssim_\nu\mathcal A_{\rm BKM}.
}
\]

### G. Material-probe geometric distortion events

At scale `ell_j`, define

\[
\mathcal G_{\ell_j}
=\|\nabla u\|_\infty
+\ell_j\|\nabla^2u\|_\infty
+\ell_j^2\|\nabla^3u\|_\infty.
\]

A fixed-factor H2 probe-shape distortion costs

\[
\int_{G_j}\mathcal G_{\ell_j}dt\ge c_G>0.
\]

Set

\[
\boxed{
\mathcal A_{\rm geom}
:=\sum_j\int_{G_j}\mathcal G_{\ell_j}dt.
}
\]

Then

\[
\boxed{N_G\lesssim\mathcal A_{\rm geom}.}
\]

### P. Bounded-geometry same-scale partner/reach events

After the close-packet merge-or-defect reduction, a compact reach/partner event that does not merge into the large-radius coherent lane is charged to a genuine same-scale source/gradient event.

For each pruned partner event, let

\[
X_j=\int_{P_j}S_{2,K_j}ds,
\qquad
Y_j=\int_{P_j}(P_{\rm mag,K_j}+P_{\rm ang,K_j})ds.
\]

The duration-free partner-source product gives

\[
X_jY_j\ge c_P>0.
\]

Define

\[
\boxed{
\mathcal A_S=\sum_jX_j,
\qquad
\mathcal A_{\nabla\omega}=\sum_jY_j.
}
\]

Cauchy--Schwarz yields

\[
\boxed{
N_P
\lesssim
(\mathcal A_S\mathcal A_{\nabla\omega})^{1/2}.
}
\]

## 2. Count clean runs

Along one sequential genealogy, the number of clean coherent I-runs is at most a fixed constant plus the number of exceptional separators:

\[
N_C
\le
1+N_B+N_G+N_P,
\]

unless the lineage exits the compact lane into a larger coherent merge, in which case the large-R coherent/Betchov analysis takes over.

Therefore

\[
\Delta\log K_C^{\rm total}
\lesssim
\left[
1+N_B+N_G+N_P
\right]
\log(C(2+M_3)).
\]

## 3. Total frequency-gain inequality

Add the projectively rough migration contribution and the clean-run contribution.  The result is

\[
\boxed{
\begin{aligned}
\log\frac{K_*}{K_0}
\lesssim
&\;p_0^{-1/2}\mathcal A_F\\
&+\left[
1
+C_\nu\mathcal A_{\rm BKM}
+C\mathcal A_{\rm geom}
+C(\mathcal A_S\mathcal A_{\nabla\omega})^{1/2}
\right]
\log(C(2+M_3)).
\end{aligned}
}
\]

All constants depend only on the fixed nondegeneracy thresholds, viscosity, and the chosen normalized probe/window profiles.

## 4. Criticality audit

Every quantity entering the bound is Navier--Stokes scale critical or dimensionless:

- `log(K*/K0)` is dimensionless;
- `A_F` is the criticalized factorial/projective forcing action;
- `A_BKM=int ||omega||_inf dt` is BKM critical;
- `A_geom` is exactly invariant under NS scaling;
- `A_S` and `A_grad` are normalized unit-scale source/gradient actions and their event product is scale invariant;
- `M3=||u||_3` is endpoint critical.

Thus the inequality does not obtain a subcritical miracle.  Instead it states that **frequency cannot run to infinity while every known critical structural channel remains small**.

## 5. Interpretation

A hypothetical compact singular genealogy reaching arbitrarily large frequency must force at least one of the following to become large:

1. scale-critical projective/factorial forcing;
2. BKM vorticity action through repeated viscous resets;
3. scale-critical material-probe geometric derivative action;
4. same-scale strain and magnitude/angular gradient actions;
5. endpoint `L3` through long clean material I-runs;
6. or it must exit the compact lane into the large-radius coherent/Betchov branch.

This is a synthesized safety-map statement rather than a new continuation criterion.

## 6. Claim boundary

No finite a-priori bound is known for the right-hand side near a hypothetical singular time.  BKM, endpoint `L3`, critical strain/gradient actions, and factorial forcing are all allowed to diverge in a singular scenario.

The inequality therefore does **not** prove global regularity.

Its value is that the previously separate compact reproduction escapes are now represented by one explicit frequency-gain ledger.  The remaining mathematical question is whether the Navier--Stokes coupling permits all of these critical actions to saturate simultaneously along one Zeno radial genealogy.

Status: **COMPACT FREQUENCY GAIN CONTROLLED BY A FINITE CRITICAL GENEALOGY LEDGER / NO FREE MODULATION OR REPRODUCTION CHANNEL REMAINS UNDER THE STATED PRUNING AND BOUNDED-GEOMETRY ROUTING / SIMULTANEOUS CRITICAL SATURATION REMAINS OPEN.**