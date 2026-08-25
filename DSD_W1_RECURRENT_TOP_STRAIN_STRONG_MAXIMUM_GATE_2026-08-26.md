# DSD W1 Recurrent Top-Strain Strong-Maximum Gate

Date: 2026-08-26

Status: **STRICT RECURRENT TOP-STRAIN THRESHOLD DERIVED / EVERY NONTRIVIAL COMPACT MINIMAL W1 SET MUST HAVE sup lambda_3 > 1 / SUBCRITICAL lambda_3 <= 1 CORRIDOR EXCLUDED BY RECURRENCE PLUS PARABOLIC STRONG MAXIMUM PRINCIPLE / SUPERCRITICAL EVENTS RECUR SYNDENTICALLY / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The vorticity-maximum note proved that at a global state-space/spatial maximum of vorticity on a nontrivial compact minimal W1 set,

\[
\gamma=\xi^TS\xi\ge1,
\qquad
\lambda_3\ge1.
\]

This note asks whether the equality endpoint

\[
\lambda_3\le1
\]

can support a nontrivial recurrent W1 orbit.

It cannot.

## 2. Vorticity scalar inequality under lambda_3 <= 1

Let

\[
F=|\Omega|^2.
\]

The exact Leray magnitude equation is

\[
\frac12
\left(
\partial_s+U\cdot\nabla+\frac12Y\cdot\nabla
\right)F
+F
=
\Omega^TS\Omega
+\frac\nu2\Delta F
-\nu|\nabla\Omega|^2.
\]

Since

\[
\Omega^TS\Omega
\le\lambda_3F,
\]

if

\[
\lambda_3(Y,s)\le1
\]

through a trajectory, then

\[
\boxed{
\left(
\partial_s+U\cdot\nabla+\frac12Y\cdot\nabla
\right)F
-\nu\Delta F
\le
-2\nu|\nabla\Omega|^2
\le0.
}
\]

Thus `F` is a bounded nonnegative subsolution of a uniformly parabolic advection-diffusion equation on every bounded spacetime cylinder.

## 3. The vorticity supremum is nonincreasing

The W1 tail has

\[
F(Y,s)=O(|Y|^{-4})
\]

uniformly on the compact recurrent class. Hence the spatial supremum is attained in a finite core.

The parabolic maximum principle applied on successively large bounded balls, followed by the vanishing tail limit, gives

\[
\boxed{
m(s):=\|\Omega(s)\|_\infty^2
\quad\text{is nonincreasing in }s.
}
\]

This is conditional only on the corridor assumption `lambda_3<=1`.

## 4. Recurrence forces the nonincreasing supremum to be constant

Let `U_0` lie in a compact minimal W1 set M and assume

\[
\lambda_3\le1
\]

for every state of M.

Minimality implies recurrence. There exists a sequence

\[
s_n\to+\infty
\]

such that

\[
\Phi_{s_n}U_0\to U_0
\]

in the W1 compact smooth local topology, with the uniform vorticity tail upgrading this to convergence of the global vorticity supremum.

Therefore

\[
m(s_n)\to m(0).
\]

But `m(s)` is nonincreasing. Hence

\[
\boxed{
m(s)=m(0)
\qquad(s\ge0).}
\]

Applying the same argument after shifting the starting phase shows that the vorticity supremum is constant along the entire recurrent orbit.

## 5. Strong maximum principle excludes a positive constant supremum

Assume this constant is positive:

\[
m_*>0.
\]

Choose two times

\[
s_0<s_1.
\]

Uniform tail decay gives a large finite radius R such that

\[
\sup_{s\in[s_0,s_1]}
\sup_{|Y|=R}F(Y,s)
<\frac12m_*.
\]

At time `s_1`, the global maximum `m_*` is attained at some interior point

\[
Y_1\in B_R.
\]

On the bounded cylinder

\[
B_R\times(s_0,s_1],
\]

`F` is a smooth subsolution of

\[
\partial_sF+b\cdot\nabla F-\nu\Delta F\le0,
\qquad
b=U+Y/2,
\]

with smooth bounded drift on the cylinder.

The parabolic strong maximum principle says that an interior positive maximum equal to the spacetime supremum at a positive time can persist only if `F` is constant on the backward connected component.

That is incompatible with the strict boundary inequality

\[
F<m_*/2
\quad\text{on }|Y|=R.
\]

Therefore

\[
\boxed{m_*=0.}
\]

So

\[
\Omega\equiv0.
\]

The W1 velocity is divergence free, curl free, smooth, and lies globally in `Lp` for some `p>3`; hence

\[
U\equiv0.
\]

This is the excluded equilibrium.

## 6. Strict top-strain threshold

We have proved the contrapositive:

\[
\boxed{
M\text{ nontrivial compact minimal W1}
\Longrightarrow
\sup_{U\in M,\,Y\in\mathbb R^3}
\lambda_3(U,Y)>1.
}
\]

Thus the Leray value `1` is a strict recurrent top-strain threshold.

It is the natural local threshold because the vorticity equation contains the explicit similarity damping `+Omega`.

## 7. A compact-set positive gap

Because the supremum is strictly above 1 and is attained on the compact state-space/finite-core region, define

\[
\varepsilon_{3,M}
:=
\frac12
\left(
\max_{U\in M,Y}\lambda_3(U,Y)-1
\right)>0.
\]

Then the open event

\[
\mathcal O_{3,M}
:=
\left\{
U\in M:
\exists Y\in B_{R_M}
\text{ with }
\lambda_3(U,Y)>1+\varepsilon_{3,M}
\right\}
\]

is nonempty.

## 8. Minimality gives syndetic recurrence of supercritical top strain

For a compact minimal continuous flow, return times of every orbit to every nonempty open set are relatively dense.

Therefore every orbit in M returns to `O_{3,M}` with bounded Leray-time gaps.

Consequently

\[
\boxed{
\text{every nontrivial minimal W1 orbit has syndetically recurrent finite-core events }
\lambda_3>1+\varepsilon_{3,M}.
}
\]

Local smooth compactness supplies a uniform short duration for a slightly weakened threshold, so the associated supercritical top-strain exposure has a positive asymptotic time density.

## 9. Relation to the middle-strain gate

The invariant-measure Betchov gate independently gives positive-frequency finite-core activity of

\[
\lambda_2^+>\frac14+\frac{\delta_M}{2}
\]

in a strain-energy weighted sense.

The present result gives

\[
\lambda_3>1+\varepsilon_{3,M}
\]

with syndetic state-space recurrence.

These events need not occur at exactly the same spatial point or time. No overlap is asserted without a separate argument.

Thus the W1 core must sustain both:

1. recurrent supercritical principal extension;
2. recurrent positive middle-strain production.

This rules out a globally subcritical strain spectrum but does not yet exclude alternating or spatially segregated production geometries.

## 10. Relation to H/far-strain decomposition

The far-strain estimate in the repository gives

\[
\|S_{>R}\|_\infty
\le C R^{-3/2}\|\Omega\|_2.
\]

Since enstrophy is uniformly bounded on the compact W1 class, choose R sufficiently large that the far contribution is much smaller than the supercritical threshold `1+epsilon_3,M`.

Therefore the recurrent top-strain events cannot be paid purely from arbitrarily remote historical memory. An order-one share of the principal extension must be generated within one fixed finite interaction radius around the event point.

This localizes the mechanism but does not impose a one-sided finite repetition budget.

## 11. Audit verdict

### PROVED

- `lambda_3<=1` makes vorticity magnitude a parabolic subsolution;
- its global supremum is nonincreasing under the W1 tail decay;
- recurrence forces the supremum to be constant;
- strong maximum principle plus spatial decay then forces the recurrent solution to be trivial;
- every nontrivial minimal W1 set therefore satisfies strict `sup lambda_3>1`;
- compactness yields a positive set-dependent gap above 1;
- minimality upgrades supercritical top-strain states to syndetic recurrence;
- remote historical strain alone cannot pay these events at arbitrarily large radius.

### NOT PROVED

- spatial/temporal overlap of the `lambda_3>1+epsilon` events with the middle-strain payer;
- a finite global budget for repeated local principal extension;
- an implication to H/T/turnover closure;
- exclusion of the W1 minimal set;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]