# Leray Rotating Relative-Equilibrium Liouville Import — 2026-08-24

Status: **CONDITIONAL EXTERNAL LIOUVILLE ROUTING / GLOBAL REGULARITY NOT PROVED.**

This note connects the recurrent projective/eigenframe route to Pineau–Vicol, arXiv:2607.09619v2.

## 1. Rigidly rotating Leray orbit

Suppose a complete Leray trajectory has the relative-equilibrium form

\[
\boxed{
V(Y,s)
=R(\alpha s)
U(R(-\alpha s)Y)
}
\]

for a fixed axis and constant angular speed `alpha`.

Undoing the Leray transformation gives exactly a backwards rotated self-similar (RSS) Navier-Stokes solution.

Thus a projective/eigenframe rescue which settles into constant-speed rigid rotation is not a new class: it is precisely the RSS class studied by Pineau–Vicol.

## 2. Required spatial Type-I hypothesis

Their RSS theorem assumes the borderline spatial profile bound

\[
\boxed{
|U(Y)|\le\frac{C_{U,0}}{1+|Y|}.
}
\]

Equivalently in physical variables,

\[
|u(x,t)|\le\frac{C_{U,0}}{|x|+\sqrt{-t}}.
\]

The current first-hitting route by itself only gives the weaker temporal estimate

\[
\|u(t)\|_\infty\lesssim(-t)^{-1/2}.
\]

Therefore the external theorem is invoked only on the branch where `ANNULAR_H2_SPATIAL_TYPEI_TAIL_BRIDGE_2026-08-24.md` has supplied the spatial `1/r` bound.

## 3. Pineau–Vicol RSS exclusion

Under the spatial Type-I bound, Pineau–Vicol prove that there exist

\[
0<\underline\alpha(C_{U,0})\ll1,
\qquad
1\ll\overline\alpha(C_{U,0})<\infty
\]

such that an RSS profile is trivial if

\[
\boxed{
|\alpha|<\underline\alpha
\quad\text{or}\quad
|\alpha|>\overline\alpha.
}
\]

The intermediate regime

\[
\boxed{\underline\alpha\le|\alpha|\le\overline\alpha}
\]

remains open in that theorem.

Thus rigid projective rotation survives only at intermediate similarity angular speed after the spatial Type-I bridge is established.

## 4. Stationary endpoint

At

\[
\alpha=0
\]

the orbit is stationary in Leray time. Classical Nečas–Ružička–Šverák/Tsai Liouville theory excludes the nontrivial profile under the present `L6`/local-energy regularity.

Hence the small-rotation theorem is a genuine quantitative extension away from the stationary endpoint.

## 5. Relative-periodic / RDSS orbit

Suppose instead that after factoring out a constant rotation the Leray profile is periodic:

\[
V(Y,s)
=R(\alpha s)U(R(-\alpha s)Y,s),
\]

\[
U(\cdot,s+P)=U(\cdot,s).
\]

Then the physical solution is rotated discretely self-similar (RDSS), with

\[
\boxed{
P=2\log\lambda.
}
\]

Pineau–Vicol prove conditional triviality under the same spatial Type-I bound when the period is sufficiently small (`lambda` sufficiently close to one) and the angular speed is in their small- or large-rotation ranges, with a stronger small-period requirement in the large-alpha case.

Therefore the relative-periodic residual class is reduced to

\[
\boxed{
\text{non-small period}
\quad\lor\quad
\text{intermediate rotation speed}
}
\]

unless one of the tail hypotheses fails.

## 6. Relation to the projective-action branch

The current internal proof route says that persistent positive-middle source action must either

1. ribbonize/reshape the core;
2. turn over material/source identity;
3. rotate the transverse/projective strain geometry.

If option 3 converges to constant angular speed, the present note sends it to RSS.

If it converges to periodic motion modulo constant rotation, it is RDSS.

If neither happens, the last genuinely new object is aperiodic recurrent projective dynamics.

Thus, after the spatial Type-I tail bridge,

\[
\boxed{
\text{recurrent projective survivor}
\Longrightarrow
\begin{cases}
\text{RSS with intermediate }\alpha,\\
\text{RDSS with non-small period/intermediate }\alpha,\\
\text{aperiodic recurrent orbit}.
\end{cases}
}
\]

## 7. Exact role of the 2026 one-slice theorem

The same paper also proves that, under local spatial Type-I and a pressure-annulus bound, a single sufficiently late time at which the Leray derivative is small implies regularity.

Hence an aperiodic recurrent survivor on the spatial-Type-I branch must remain not only nonstationary but uniformly separated from zero self-similar-time speed in the precise sense recorded in `PINEAU_VICOL_LOCAL_TYPEI_RECURRENCE_GATE_2026-08-24.md`.

Status: **ONCE THE BORDERLINE SPATIAL TYPE-I TAIL IS PROVED, CONSTANT-SPEED PROJECTIVE ROTATION IS IDENTICAL TO RSS AND IS EXCLUDED FOR SUFFICIENTLY SMALL OR LARGE ROTATION SPEED; RELATIVE-PERIODIC MOTION IS RDSS AND IS PARTIALLY EXCLUDED FOR SMALL PERIOD. THE REMAINDER IS INTERMEDIATE-SPEED/FINITE-PERIOD OR GENUINELY APERIODIC RECURRENCE.**