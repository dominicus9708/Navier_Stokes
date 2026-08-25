# DSD W1 Minimal-Set Vorticity-Maximum Extension Gate

Date: 2026-08-26

Status: **FINITE-CORE MAXIMUM-VORTICITY EXTENSION THRESHOLD DERIVED / EVERY NONTRIVIAL COMPACT MINIMAL W1 SET CONTAINS A STATE-POINT WITH VORTICITY-DIRECTION STRAIN gamma >= 1 / MINIMALITY UPGRADES NEAR-THRESHOLD STATES TO SYNDENTIC RECURRENCE / LOCAL MIDDLE-STRAIN-OR-ALIGNMENT DICHOTOMY DERIVED / NO FINITE REPETITION BUDGET YET / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The invariant-measure middle-strain gate proves a positive-frequency finite-core payer without using the vorticity direction.

A complementary local fact can be obtained directly from the vorticity maximum principle structure on the compact minimal set.

Unlike the global `L^(3/2)` middle-strain criterion, this calculation uses only local smoothness, critical-tail decay, and compact recurrence.

## 2. Vorticity magnitude equation in Leray variables

The W1 Leray vorticity equation is

\[
\Omega_s
+\Omega
+\frac12Y\cdot\nabla\Omega
+(U\cdot\nabla)\Omega
=(\Omega\cdot\nabla)U
+\nu\Delta\Omega.
\]

Let

\[
F:=|\Omega|^2.
\]

Taking the scalar product with Omega gives

\[
\boxed{
\frac12
\left(
\partial_s+U\cdot\nabla+\frac12Y\cdot\nabla
\right)F
+F
=
\Omega^TS\Omega
+\frac\nu2\Delta F
-\nu|\nabla\Omega|^2.
}
\]

Where `Omega != 0`, define the vorticity direction

\[
\xi:=\frac\Omega{|\Omega|}
\]

and its strain rate

\[
\boxed{
\gamma:=\xi^TS\xi
=\frac{\Omega^TS\Omega}{|\Omega|^2}.
}
\]

## 3. Global state-space/spatial maximum exists in a finite core

Let M be a nontrivial compact minimal W1 invariant set.

The critical tail obeys uniformly on M

\[
|\Omega_U(Y)|\lesssim |Y|^{-2}.
\]

Therefore

\[
\sup_{U\in M}|\Omega_U(Y)|\to0
\qquad(|Y|\to\infty).
\]

Local analytic compactness makes the map

\[
(U,Y)\mapsto|\Omega_U(Y)|
\]

continuous on M times bounded balls.

Hence the global maximum

\[
\boxed{
M_\Omega
:=
\max_{U\in M,\,Y\in\mathbb R^3}
|\Omega_U(Y)|
}
\]

is attained at one pair

\[
(U_*,Y_*).
\]

Since M is nontrivial, `M_Omega>0`.

Because of the uniform tail decay, `Y_*` lies in one finite ball.

## 4. The maximum state gives zero Leray-time derivative at the maximizing point

Let

\[
U(s)=\Phi_sU_*
\]

be the Leray orbit through `U_*`.

Invariance of M gives

\[
\Phi_sU_*\in M
\]

for every admissible s.

Therefore, at the fixed spatial point `Y_*`,

\[
|\Omega_{\Phi_sU_*}(Y_*)|^2
\le M_\Omega^2
=|\Omega_{U_*}(Y_*)|^2.
\]

Thus `s=0` is a local maximum of this smooth scalar function of s and

\[
\boxed{
\partial_sF(U_*,Y_*)=0.
}
\]

Spatial maximality simultaneously gives

\[
\boxed{
\nabla F(U_*,Y_*)=0,
\qquad
\Delta F(U_*,Y_*)\le0.
}
\]

The transport and dilation directional derivatives vanish because the spatial gradient vanishes.

## 5. Universal extension threshold gamma >= 1

Evaluate the vorticity-magnitude equation at `(U_*,Y_*)`.

The time and first-order spatial terms vanish, giving

\[
F
=
\Omega^TS\Omega
+\frac\nu2\Delta F
-\nu|\nabla\Omega|^2.
\]

Hence

\[
\Omega^TS\Omega
=
F
-\frac\nu2\Delta F
+\nu|\nabla\Omega|^2
\ge F.
\]

Since `F=M_Omega^2>0`, divide by F:

\[
\boxed{
\gamma(U_*,Y_*)
\ge1.
}
\]

More precisely,

\[
\boxed{
\gamma-1
=
\nu\frac{|\nabla\Omega|^2}{|\Omega|^2}
-\frac\nu2
\frac{\Delta|\Omega|^2}{|\Omega|^2}
\ge0
}
\]

at the global maximizing pair.

The numerical threshold `1` is tied to the standard backward Leray normalization used in the repository.

## 6. Consequences for the strain eigenvalues

Since

\[
\gamma=\xi^TS\xi\le\lambda_3,
\]

we immediately obtain

\[
\boxed{
\lambda_3(U_*,Y_*)\ge1.
}
\]

Thus every nontrivial compact minimal W1 set contains a finite-core state-point with order-one normalized extensional strain.

This statement is stronger pointwise than the orientation-free `lambda_2^+>1/4` threshold, but it retains directional information.

## 7. Middle-strain-or-principal-alignment dichotomy at the maximum

Let

\[
\lambda_1\le\lambda_2\le\lambda_3
\]

be the strain eigenvalues at the maximizing pair and

\[
a_i=(\xi\cdot e_i)^2,
\qquad
a_1+a_2+a_3=1.
\]

Then

\[
\gamma
=\lambda_1a_1+\lambda_2a_2+\lambda_3a_3.
\]

Because `lambda_1<=lambda_2`,

\[
\gamma
\le
\lambda_2(1-a_3)+\lambda_3a_3.
\]

Fix any threshold `a<1`.

If

\[
\lambda_2<a,
\]

then `gamma>=1` forces

\[
1
\le
a(1-a_3)+\lambda_3a_3,
\]

so

\[
\boxed{
a_3
\ge
\frac{1-a}{\lambda_3-a}.
}
\]

Compactness of M and finite-core localization give a uniform finite ceiling

\[
\lambda_3\le L_M.
\]

Therefore

\[
\boxed{
\lambda_2<a
\Longrightarrow
 a_3
\ge
\frac{1-a}{L_M-a}
>0.
}
\]

Taking, for example, the invariant-measure middle-strain threshold

\[
a=\frac14+\frac{\delta_M}{2}<1
\]

when this number is below 1, the vorticity maximum must satisfy one of:

\[
\boxed{
\lambda_2
\ge
\frac14+\frac{\delta_M}{2}
}
\]

or

\[
\boxed{
|\xi\cdot e_3|^2
\ge
\frac{3/4-\delta_M/2}{L_M-1/4-\delta_M/2}.
}
\]

Thus the local maximum gate connects directly to the previous middle-strain and principal-alignment branches.

## 8. Minimality upgrades the maximum state to recurrent near-maximum episodes

The exact maximizing state `U_*` need not lie on every chosen orbit at an exact time.

However in a compact minimal flow, the return set of every orbit to any nonempty open subset of M is syndetic: there exists a finite gap length depending on the open set such that every sufficiently long interval contains a return.

Choose a sufficiently small neighborhood `N_epsilon` of `U_*` in the W1 smooth local topology.

Continuity of Omega and S on the finite core gives, for sufficiently small epsilon,

\[
|\Omega_U(Y_*)|
\ge (1-\epsilon)M_\Omega
\]

and

\[
\gamma_U(Y_*)
\ge1-\epsilon
\]

for `U in N_epsilon`.

Hence every orbit in M has recurrent finite-core episodes satisfying

\[
\boxed{
|\Omega(Y_*)|
\gtrsim M_\Omega,
\qquad
\gamma(Y_*)
\gtrsim1,
}
\]

with bounded gaps in Leray time.

This is stronger topologically than merely saying that one invariant measure assigns positive average to the event.

## 9. Fixed-duration action per visit

Compact local analyticity also gives a uniform bound on the Leray-time derivative of the finite-core observables.

Therefore after shrinking the neighborhood if needed, each visit contains a uniform time subinterval of length `tau_epsilon>0` on which

\[
\gamma(Y_*,s)
\ge1-2\epsilon
\]

and

\[
|\Omega(Y_*,s)|
\ge(1-2\epsilon)M_\Omega.
\]

Since the visits have bounded gaps, the cumulative normalized extension exposure obeys a linear lower bound along every minimal orbit:

\[
\boxed{
\int_0^S
\mathbf1_{\{\text{near-max core event}\}}
\gamma_+(s)\,ds
\ge c_\epsilon S-O(1)
}
\]

for one `c_epsilon>0`.

Under inverse physical scaling this becomes the critical logarithmic strain-action accumulation expected of a singular Type-I scenario.

It is therefore a necessary recurrent cost, not yet a contradiction.

## 10. Relation to earlier first-hitting strain tax

The earlier repository calculation

`DSD_FIRST_HITTING_STRAIN_EXPOSURE_TAX_2026-08-19.md`

(or its commit-level predecessor) derived blockwise strain exposure from repeated vorticity growth between first-hitting levels.

The present result is different:

- it acts directly on the compact W1 minimal recurrent limit;
- it identifies a finite-core vorticity-maximum point;
- it gives the normalized pointwise threshold `gamma>=1`;
- minimality converts the maximizing configuration into recurrent near-max episodes with bounded time gaps.

Thus the old strain tax and the new maximum gate are consistent descriptions of the same necessary extensional activity at different stages of the reduction.

## 11. Why this still does not close W1

A compact recurrent flow can, in principle, sustain repeated order-one extensional strain if stretching is balanced by viscosity and redistribution.

The physical critical strain action is allowed to diverge logarithmically at a hypothetical singularity; known strain/eigenvalue regularity criteria require precisely such divergence.

Therefore

\[
\boxed{
\gamma\gtrsim1\text{ with positive/syndetic frequency}
}
\]

is a sharpened survivor signature, not a contradiction by itself.

A final closure must show that these repeated finite-core near-maximum extension episodes necessarily consume a one-sided finite resource, or force an already excluded turnover/H/projective event.

## 12. Audit verdict

### PROVED

- a nontrivial compact minimal W1 set has a global state-space/spatial vorticity maximum in a finite core;
- at that maximum the vorticity-direction strain satisfies `gamma>=1`;
- consequently `lambda_3>=1`;
- if middle strain is below a chosen subunit threshold, the vorticity must have a quantitative principal-eigenvector alignment;
- minimality produces syndetically recurrent near-max extension episodes;
- local compact smoothness gives a fixed-duration action for each visit.

### NOT PROVED

- a finite budget for the repeated extension exposure;
- forced projective rotation under persistent principal alignment;
- forced middle-strain escalation beyond the invariant-measure gate;
- exclusion of the compact W1 minimal set;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]