# DSD M5-649 — Relative-flux normalization closes the nonzero synchronized-kappa relabeling branch

Date: 2026-09-03

Status: **INTERNAL FINITE-RESOURCE CONTRADICTION / WHEN THE SYNCHRONIZED PERSISTENT RELABELING LEVEL `c_*(theta)` HAS ZERO MEAN BUT IS NOT IDENTICALLY ZERO, NORMALIZING EVERY MATERIAL FLUX BY ONE BOUNDED NONDEGENERATE PERSISTENT REFERENCE FLUX REMOVES THE COMMON `c_*` DRIFT AND PRODUCES THE RELATIVE MULTIPLIER `kappa-c_*`; ORDER PRESERVATION MAKES EVERY LOWER LEVEL FORWARD-MONOTONE IN THIS RELATIVE FLUX / POSITIVE PHASES OF `c_*` FORCE THE GLOBAL VORTICITY MAXIMUM ONTO A UNIFORMLY LOWER LEVEL, GIVING POSITIVE-DENSITY STRONGLY-NEGATIVE RELATIVE-FLUX PACKETS / THE M5-647 FINITE BASE TRANSVERSAL RESOURCE THEN GIVES THE SAME IRREVERSIBLE-CONSUMPTION CONTRADICTION AS M5-648 / THEREFORE THE ENTIRE RELABELING BRANCH IS ELIMINATED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Nontrivial synchronized persistent level

Assume the relabeling branch

\[
D_B\kappa=f(\kappa,\theta)
\]

and the M5-628 synchronized persistent level

\[
\kappa=c_*(\theta)
\]

with

\[
\boxed{\langle c_*\rangle=0}
\]

but

\[
\boxed{c_*\not\equiv0.}
\]

Let `Phi_*(theta)` be the signed material vorticity flux of one persistent synchronized reference lineage.

M5-603 gives

\[
\boxed{
\frac d{d\theta}\log\Phi_*=c_*(\theta).
}
\]

By persistent fixed-flux nondegeneracy,

\[
\boxed{
0<\phi_-^*\le\Phi_*(\theta)\le\phi_+^*<\infty.
}
\]

Orient the reference once so `Phi_*>0`.

---

## 2. Bounded integrating factor

Define

\[
\boxed{
I(\theta)
:=
\exp\left(
-\int_{\theta_0}^{\theta}c_*(s)\,ds
\right)
=
\frac{\Phi_*(\theta_0)}{\Phi_*(\theta)}.
}
\]

Therefore

\[
\boxed{
0<I_-\le I(\theta)\le I_+<\infty
}
\]

with constants determined by the fixed reference-flux bounds.

For any material vortex-leaf flux element `dPhi`, define the relative/renormalized flux

\[
\boxed{
d\widehat\Phi:=I(\theta)d\Phi.
}
\]

Since

\[
D_B\log d\Phi=\kappa,
\]

we obtain the exact law

\[
\boxed{
D_B\log d\widehat\Phi
=\kappa-c_*.
}
\]

Thus the common synchronized drift has been removed.

---

## 3. Relative order is sign preserving

Let `kappa_lambda(theta)` be another material relabeling solution.

Scalar ODE uniqueness gives

\[
\kappa_\lambda(\theta_0)<c_*(\theta_0)
\Longrightarrow
\kappa_\lambda(\theta)<c_*(\theta)
\quad\forall\theta>\theta_0.
\]

Hence on every lower ordered leaf,

\[
\boxed{
\widetilde\kappa_\lambda
:=
\kappa_\lambda-c_*<0
}
\]

for all future times.

Therefore its relative flux is forward-monotone decreasing:

\[
\boxed{
D_B\widehat\Phi<0.
}
\]

The same monotone-resource structure as M5-648 is recovered without requiring absolute `kappa<0`.

---

## 4. Nonzero zero-mean `c_*` has positive phases of fixed size

Because `c_*` is bounded, measurable on the invariant component, has mean zero, and is not identically zero, its positive set has positive invariant measure.

Since

\[
\{c_*>0\}
=
\bigcup_{m\ge1}\{c_*\ge1/m\},
\]

there exists `a_*>0` such that

\[
\boxed{
\mu\{c_*\ge4a_*\}>0.
}
\]

Along a generic recurrent orbit these phases occur with positive frequency, hence infinitely often.

---

## 5. Vorticity maximum is on a uniformly lower level

M5-634 proves that at every positive spatial maximum of `rho=|W|`,

\[
\boxed{
\kappa\le-|\nabla\xi|^2\le0.
}
\]

At every time with

\[
c_*\ge4a_*,
\]

a global vorticity maximum therefore lies on a level satisfying

\[
\boxed{
\kappa_{max}-c_*
\le-4a_*.
}
\]

The hard component is compact, globally smooth and excludes the zero state.

Hence its global vorticity maximum has a uniform positive amplitude floor

\[
\rho_{max}\ge m_*>0.
\]

Using the uniform spatial derivative caps, choose a fixed ball/transverse disk around the maximum on which

\[
|W|\ge\frac12m_*,
\]

and

\[
\kappa-c_*\le-2a_*.
\]

This disk carries a fixed directed material flux

\[
\boxed{
\Phi_{max}\ge\phi_{max,*}>0.
}
\]

---

## 6. Uniform time thickening

On the maximum carrier `|W|` is bounded away from zero, so both `kappa` and `c_*` vary uniformly continuously in similarity time on the compact hull.

After shrinking constants, there exists `delta_*>0` such that at every selected positive-phase time `theta_j`, a transported subpacket satisfies on

\[
I_j=[\theta_j,\theta_j+\delta_*]
\]

\[
\boxed{
\kappa-c_*\le-a_*,
\qquad
\Phi\ge\phi_{max,*}
\text{ at }\theta_j.
}
\]

Because `I(theta)>=I_->0`, its initial relative flux satisfies

\[
\boxed{
\widehat\Phi(\theta_j)
\ge
I_-\phi_{max,*}
=:\widehat\phi_*>0.
}
\]

---

## 7. Fixed irreversible relative-flux loss

On `I_j`,

\[
\frac d{d\theta}\log\widehat\Phi
\le-a_*.
\]

Therefore

\[
\widehat\Phi(\theta_j+\delta_*)
\le e^{-a_*\delta_*}\widehat\Phi(\theta_j).
\]

Thus every event consumes at least

\[
\boxed{
\widehat L_j
\ge
\widehat\ell_*
:=(1-e^{-a_*\delta_*})\widehat\phi_*>0.
}
\]

of relative transverse flux.

---

## 8. Finite base resource remains finite after normalization

At the chosen base time,

\[
I(\theta_0)=1.
\]

Hence the M5-647 finite transverse resource is also the initial relative-flux resource:

\[
\boxed{
\|\widehat\mu_{flux}\|(\mathcal T)
=
\|\mu_{flux}\|(\mathcal T)
<\infty.
}
\]

At later times the common factor `I(theta)` is uniformly bounded, so no hidden infinite normalization is introduced.

---

## 9. Telescoping on lower leaves

For one base leaf label `lambda`, define

\[
\widehat a_\lambda(\theta)
=
\exp\left(
\int_{\theta_0}^{\theta}
[\kappa_\lambda(s)-c_*(s)]ds
\right).
\]

On a lower ordered leaf this is positive and nonincreasing.

Choose infinitely many positive-phase event times with pairwise disjoint intervals `I_j`.

Even if the same lower leaf participates in many events,

\[
\sum_j
\mathbf 1_{\lambda\in A_j}
\left[
\widehat a_\lambda(\theta_j)
-
\widehat a_\lambda(\theta_j+\delta_*)
\right]
\le1.
\]

Integrating over the fixed base transverse resource gives

\[
\boxed{
\sum_j\widehat L_j
\le
\|\mu_{flux}\|(\mathcal T)
<\infty.
}
\]

But each event has

\[
\widehat L_j\ge\widehat\ell_*>0,
\]

which allows only finitely many events.

This contradicts the positive-frequency recurrence of the `c_*>=4a_*` phase.

Therefore

\[
\boxed{
R_{relabel}^{c_*\not\equiv0}
\Longrightarrow\bot.
}
\]

---

## 10. Full relabeling closure

M5-648 established

\[
R_{relabel}^{c_*\equiv0}\Longrightarrow\bot.
\]

The present note establishes

\[
R_{relabel}^{c_*\not\equiv0}\Longrightarrow\bot.
\]

Hence

\[
\boxed{
R_{relabel}
\Longrightarrow\bot.
}
\]

Thus the M5-627 level-surface dichotomy loses its relabeling survivor.

Any surviving CE-H trajectory must retain a genuinely transverse material evolution of the `kappa` level geometry, i.e. the non-relabeling forcing branch.

---

## 11. Audit firewalls

1. The argument does not assume absolute `kappa` sign preservation in the sign-changing synchronized branch.
2. It uses only order preservation relative to the persistent solution `c_*(theta)`.
3. The integrating factor is harmless only because the reference persistent flux is bounded above and below.
4. The maximum-point inequality `kappa<=0` is the bridge producing a uniformly lower relative level during positive `c_*` phases.
5. The finite resource remains the fixed base-slice M5-647 transversal mass.
6. No global material-volume contradiction is used.

---

## 12. Updated CE-H frontier

The M5-627 split

\[
\text{transverse }\nabla(D_B\kappa)
\quad\lor\quad
R_{relabel}
\]

now reduces to

\[
\boxed{
E_{CEH}
\Longrightarrow
F_{\nabla D_B\kappa}^{transverse}.
}
\]

The next task is to write this surviving cross-level acceleration in a quotient-free tensor form and test whether its invariant positive activity can be coupled to the already nondegenerate generalized-kappa-force virial of M5-625--626.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]