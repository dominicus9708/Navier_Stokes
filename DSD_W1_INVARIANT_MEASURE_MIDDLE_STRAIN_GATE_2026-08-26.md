# DSD W1 Invariant-Measure Middle-Strain Gate

Date: 2026-08-26

Status: **PERIODIC MIDDLE-STRAIN GATE EXTENDED TO GENERAL COMPACT RECURRENT W1 INVARIANT MEASURES / APERIODIC MINIMAL BRANCH NOW CARRIES THE SAME POSITIVE MIDDLE-STRAIN PAYER / STRICT ABOVE-1/4 WEIGHTED THRESHOLD AND POSITIVE-FREQUENCY FINITE-CORE EXTENSIONAL EVENTS DERIVED FOR ERGODIC COMPONENTS / NO FINITE REPETITION BUDGET YET / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The previous note

`DSD_W1_PERIODIC_BETCHOV_MIDDLE_STRAIN_THRESHOLD_GATE_2026-08-26.md`

used exact periodicity to average the global Leray enstrophy identity.

However the W1 reduction already supplies a compact invariant recurrent set and invariant probability measures. The enstrophy and palinstrophy observables are sufficiently tight on this class to repeat the same argument without exact periodicity.

This removes an artificial distinction between the periodic and aperiodic branches at the strain-payer level.

## 2. Uniform global enstrophy tightness on W1

The old-shell W1 estimates give uniformly on the compact recurrent class

\[
\int_{A_R}|\Omega|^2\,dY
\le C R^{-1}.
\]

Therefore

\[
\boxed{
\sup_{U\in K}
\int_{|Y|>R}|\Omega|^2dY
=O(R^{-1})\to0.
}
\]

Local analyticity gives strong local derivative compactness. Hence convergence in the W1 recurrent class upgrades locally to strong convergence of vorticity, while the uniform tail above removes loss at infinity.

Thus

\[
\boxed{
Z(U):=\|\Omega\|_2^2
}
\]

is a bounded continuous observable on the compact W1 invariant set K in the effective compact topology used by the proof.

## 3. Uniform palinstrophy tightness

On the derivative-controlled W1 corridor,

\[
\int_{A_R}|\nabla\Omega|^2dY
\le C R^{-3}.
\]

Hence

\[
\boxed{
\sup_{U\in K}
\int_{|Y|>R}|\nabla\Omega|^2dY
=O(R^{-3})\to0.
}
\]

Local higher-order analyticity supplies compactness on bounded balls. Therefore

\[
\boxed{
P_\Omega(U):=\|\nabla\Omega\|_2^2
}
\]

is also bounded and continuous on K.

The same tail powers make the Betchov and middle-strain cubic observables absolutely integrable.

## 4. Invariant-measure enstrophy identity

Let `mu` be any invariant probability measure for the W1 Leray semiflow supported on a compact invariant recurrent subset.

For every smooth W1 state,

\[
\frac12\frac d{ds}Z
+\frac14Z
+\nu P_\Omega
=\mathcal S,
\]

where

\[
\mathcal S(U)
=\int\Omega^TS\Omega\,dY.
\]

Because Z is a bounded differentiable observable on the compact smooth class, invariance gives

\[
\boxed{
\left\langle\frac d{ds}Z\right\rangle_\mu=0.
}
\]

Hence

\[
\boxed{
\frac14\langle Z\rangle_\mu
+\nu\langle P_\Omega\rangle_\mu
=
\langle\mathcal S\rangle_\mu.
}
\]

No periodicity has been used.

## 5. Betchov routing under the invariant measure

For every W1 state the whole-space Betchov identity gives

\[
\mathcal S
=-4\int\det S.
\]

The trace-free eigenvalue inequality proved in the periodic note is

\[
(-\det S)_+
\le
\frac12\lambda_2^+|S|^2.
\]

Therefore statewise

\[
\boxed{
\mathcal S(U)
\le
2\int\lambda_2^+|S|^2dY.
}
\]

Average in mu:

\[
\boxed{
\left\langle
\int\lambda_2^+|S|^2
\right\rangle_\mu
\ge
\frac18\langle Z\rangle_\mu
+
\frac\nu2\langle P_\Omega\rangle_\mu.
}
\]

Because

\[
\int|S|^2=\frac12Z,
\]

we obtain the normalized strain-energy weighted inequality

\[
\boxed{
\frac{
\left\langle\int\lambda_2^+|S|^2\right\rangle_\mu
}{
\left\langle\int|S|^2\right\rangle_\mu
}
\ge
\frac14
+
\nu
\frac{\langle P_\Omega\rangle_\mu}{\langle Z\rangle_\mu}.
}
\]

This is the main invariant-measure gate.

## 6. The gap above 1/4 is strictly positive on a nontrivial minimal set

Let M be a nontrivial compact minimal W1 invariant set.

If for one state U in M

\[
P_\Omega(U)=0,
\]

then

\[
\nabla\Omega=0.
\]

Since Omega is in L2(R3),

\[
\Omega=0.
\]

The velocity is then divergence free, curl free, smooth, and belongs to the W1 global Lp class for some p>3; hence U=0.

But zero is an equilibrium, excluded from the W1 minimal set by the no-equilibrium gate.

Therefore

\[
P_\Omega(U)>0
\qquad(U\in M).
\]

By continuity and compactness,

\[
\boxed{
p_*:=\min_{U\in M}P_\Omega(U)>0.
}
\]

Similarly

\[
Z^*:=\max_{U\in M}Z(U)<\infty.
\]

Hence every invariant probability measure supported on M satisfies

\[
\nu\frac{\langle P_\Omega\rangle_\mu}{\langle Z\rangle_\mu
}
\ge
\boxed{
\delta_M:=\nu\frac{p_*}{Z^*}>0.
}
\]

Thus

\[
\boxed{
\frac{
\left\langle\int\lambda_2^+|S|^2\right\rangle_\mu
}{
\left\langle\int|S|^2\right\rangle_\mu
}
\ge
\frac14+\delta_M.
}
\]

The aperiodic minimal branch therefore cannot live merely at the exact 1/4 threshold in invariant average; it must exceed it by a compact-class-dependent positive gap.

## 7. The high-middle-strain set lies in a finite core

The W1 tail obeys

\[
\lambda_2^+(Y,U)
\lesssim |Y|^{-2}
\]

uniformly on M.

Choose one finite radius R_M so large that

\[
\boxed{
|Y|>R_M
\Longrightarrow
\lambda_2^+(Y,U)
<\frac14+\frac{\delta_M}{2}
}
\]

for every U in M.

Thus any region satisfying

\[
\lambda_2^+
\ge
\frac14+\frac{\delta_M}{2}
\]

must lie inside B_{R_M}.

## 8. Positive strain-energy weight of threshold events

Define the probability measure on state-space times physical space weighted by strain energy:

\[
d\widehat\mu(U,Y)
:=
\frac{|S_U(Y)|^2\,dY\,d\mu(U)}{
\left\langle\int|S|^2\right\rangle_\mu}.
\]

Under this probability measure,

\[
\mathbb E_{\widehat\mu}[\lambda_2^+]
\ge
\frac14+\delta_M.
\]

Compactness and the remote decay give a finite upper bound

\[
\lambda_2^+\le L_M
\]

on M times R3.

Let

\[
a_M:=\frac14+\frac{\delta_M}{2}.
\]

Set

\[
E_M:=\{(U,Y):\lambda_2^+(Y,U)>a_M\}.
\]

If

\[
\theta_M:=\widehat\mu(E_M),
\]

then

\[
\mathbb E[\lambda_2^+]
\le
 a_M(1-\theta_M)+L_M\theta_M.
\]

Therefore

\[
\boxed{
\theta_M
\ge
\frac{\delta_M/2}{L_M-a_M}
>0.
}
\]

Because E_M is contained in B_{R_M}, this is a positive finite-core recurrent middle-strain occupancy.

## 9. Ergodic component gives positive Leray-time frequency

Every compact invariant set admits ergodic invariant probability measures. On a minimal set, the support of any invariant measure is an invariant closed nonempty subset and therefore equals the whole minimal set.

Choose an ergodic invariant measure mu on M.

The previous positive measure result implies that the finite-core high-middle-strain observable has positive mu average. By the Birkhoff ergodic theorem, for mu-almost every recurrent trajectory in M, the corresponding high-strain event is visited with positive asymptotic Leray-time frequency in the weighted/threshold sense.

Schematically,

\[
\boxed{
M_{min}
\Longrightarrow
\text{positive-frequency finite-core }
\lambda_2^+>\frac14+\frac{\delta_M}{2}
\text{ activity}.
}
\]

This applies whether M is a periodic orbit or a genuinely aperiodic minimal set.

## 10. Relation to known middle-eigenvalue regularity criteria

Known critical regularity criteria based on the positive middle strain eigenvalue require finiteness of suitable physical spacetime norms of lambda_2^+.

The W1 conclusion above does not satisfy such a finiteness condition near a hypothetical singular time. Under inverse Leray scaling, persistent normalized middle-strain activity produces the critical logarithmic divergence required by those blowup criteria.

Thus the external criterion is a consistency check and classification tool, not a closure of W1.

## 11. Unified W1 frontier

Before this note, the recurrent frontier was split into

\[
P_{DSS}^{long}
\lor
A_{min}^{aper}.
\]

At the middle-strain payer level, the split is no longer necessary.

Both branches now obey

\[
\boxed{
\text{compact nontrivial recurrent W1 dynamics}
\Longrightarrow
\text{positive-frequency finite-core extensional middle-strain payer}.
}
\]

The remaining proof obligation is correspondingly sharper:

> Can a compact recurrent Leray core cross and sustain a strictly super-1/4 positive middle-strain threshold with positive frequency while all previously typed H/T/turnover/export losses remain bounded or quiet?

A successful next lemma must price repeated **strain self-amplification** rather than merely velocity L3 occupancy or vorticity-direction motion.

## 12. Audit verdict

### PROVED

- global enstrophy and palinstrophy are continuous tight observables on the W1 compact recurrent class under the established shell bounds;
- invariant averaging gives the exact enstrophy/stretching identity without periodicity;
- Betchov converts the payer to positive middle strain;
- every nontrivial minimal set has a strictly positive compact-class gap `delta_M` above the Leray threshold 1/4 in strain-energy weighted invariant mean;
- high-middle-strain activity is confined to one finite core;
- an ergodic component carries positive Leray-time frequency of such activity;
- this unifies periodic and aperiodic W1 at the new gate.

### NOT PROVED

- a finite budget forbidding positive-frequency super-1/4 middle-strain activity;
- routing of that activity to an already closed H/T/projective/turnover channel;
- exclusion of the W1 minimal recurrent set;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]