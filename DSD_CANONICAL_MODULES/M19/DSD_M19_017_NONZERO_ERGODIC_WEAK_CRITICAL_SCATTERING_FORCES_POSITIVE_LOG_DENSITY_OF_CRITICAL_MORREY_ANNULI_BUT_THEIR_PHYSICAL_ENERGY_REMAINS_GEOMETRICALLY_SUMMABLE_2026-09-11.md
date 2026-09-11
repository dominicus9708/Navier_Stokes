# M19-017 — Nonzero ergodic weak-critical scattering forces positive log-density of critical Morrey annuli, but their physical energy remains geometrically summable

**Date:** 2026-09-11  
**Status:** CALCULATION / R-CRITICAL ERGODIC SCATTERING / POSITIVE LOG-DENSITY / ENERGY SUMMABILITY NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-016 proves that a nontrivial recurrent scattering factor cannot be supported on global strong \(L^3\) data.

The surviving critical datum is a nonzero translation-invariant/ergodic weak-critical scattering field

\[
A(q,\omega).
\]

The present module asks whether recurrence of \(A\) forces sufficiently many critical Morrey annuli to contradict finite physical energy.

It does force **positive log-radius density** of nontrivial annuli.

But the corresponding physical radii form a geometric sequence, and the energy cost of an order-one critical shell is proportional to its radius. Therefore even positive log-density remains geometrically summable in the physical parent.

This closes another false route and isolates the need for a rigidity/stress/trace mechanism rather than ordinary energy counting.

## 2. Local scattering mass observable

Fix a log-window length

\[
L>0
\]

—for example \(L=\log2\)—and define

\[
\boxed{
F_L(A)
:=
\int_0^L
\|A(q,\cdot)\|_{L^2(S^2)}^2dq.
}
\]

M19-016 shows that, up to uniformly controlled weights and lower-order errors, \(F_{\log2}(T_sA)\) is the kinetic Morrey charge of the physical annulus whose log-radius coordinate begins at \(s\).

Here

\[
(T_sA)(q)=A(q+s).
\]

## 3. A nonzero invariant measure has a positive local-mass event

Let \(\mu_A\) be a nontrivial translation-invariant probability measure on the scattering data.

If

\[
F_L(A)=0
\qquad\mu_A\text{-a.s.},
\]

then \(A=0\) almost surely on \([0,L]\), and translation invariance gives \(A=0\) almost surely on every translated interval. Hence the measure would be trivial.

Therefore, for a nontrivial measure,

\[
\mu_A(F_L>0)>0.
\]

By monotone union,

\[
\{F_L>0\}
=
\bigcup_{n=1}^\infty
\{F_L\ge1/n\}.
\]

Hence there exists

\[
\boxed{\varepsilon_*>0}
\]

such that

\[
\boxed{
\delta_*
:=
\mu_A(F_L\ge\varepsilon_*)
>0.
}
\]

## 4. Ergodicity gives positive log-density

Work on an ergodic scattering component, which is available from the M18-052 factor construction after ergodic decomposition.

Apply the ergodic theorem to the indicator

\[
\mathbf 1_{\{F_L\ge\varepsilon_*\}}.
\]

For almost every datum \(A\),

\[
\boxed{
\lim_{Q\to\infty}
\frac1Q
\int_0^Q
\mathbf1_{\{F_L(T_sA)\ge\varepsilon_*\}}ds
=
\delta_*>0.
}
\]

Thus the set

\[
\boxed{
\mathcal Q_*(A)
:=
\{s:F_L(T_sA)\ge\varepsilon_*\}
}
\]

has positive asymptotic density in log radius.

## 5. Convert to critical Morrey annuli

M19-016 gives

\[
\mathcal A_U(R,\theta)
\asymp
F_L(T_{q_R}A)
\]

with

\[
q_R=\log R-\theta/2,
\]

for \(L=\log2\) and large \(R\), modulo the integrable scattering error.

Therefore there exists \(a_*>0\) such that a positive log-density set of radii satisfies

\[
\boxed{
\mathcal A_U(R,\theta)
\ge a_*>0.
}
\]

Thus a nonzero ergodic weak-critical scattering state cannot hide in a zero-density collection of isolated scales.

It produces a recurrent **positive-log-density critical stack**.

## 6. Discretize log radius

Choose a fixed multiplicative ratio

\[
\Lambda>1
\]

large enough that selected annuli are disjoint after a finite coloring.

Let

\[
R_n=R_0\Lambda^n.
\]

Positive log-density implies that, after possibly changing the phase and passing to one of finitely many colors, there is a subset

\[
S\subset\mathbb N
\]

with positive lower density such that

\[
\boxed{
\mathcal A_U(R_n,\theta)
\ge a_*
\qquad(n\in S).
}
\]

Hence the normalized ancient state contains order-one critical annular energy on a positive fraction of logarithmic scales.

## 7. Map the stack to the physical parent

Let the blowup length be \(r_j\).

The normalized radius \(R_n\) corresponds to physical radius

\[
\boxed{
\ell_{j,n}=r_jR_n.
}
\]

A critical shell at physical radius \(\ell_{j,n}\) costs kinetic energy

\[
\boxed{
E_{j,n}
\gtrsim
a_*\ell_{j,n}.
}
\]

Restrict to the shells lying inside a fixed physical outer radius \(L_{phys}\):

\[
\ell_{j,n}\le L_{phys}.
\]

Although the number of active logarithmic shells tends to infinity as \(r_j\downarrow0\), their physical costs form a geometric sequence.

## 8. Positive log-density is still geometrically summable

Let \(n_{max}\) be the largest index with

\[
\ell_{j,n_{max}}\le L_{phys}.
\]

The selected physical radii increase geometrically toward \(L_{phys}\).

Even if **every** logarithmic shell were active,

\[
\sum_{n\le n_{max}}\ell_{j,n}
\le
C_\Lambda L_{phys}.
\]

Therefore on the positive-density subset \(S\),

\[
\boxed{
\sum_{n\in S,\ n\le n_{max}}
E_{j,n}
\lesssim
C a_*L_{phys}
}
\]

at the homogeneity level.

Positive log-density does not introduce an extra factor growing like the number of scales because the geometric weights are dominated by the largest radius.

Thus the finite physical energy budget remains compatible with the full positive-density critical stack.

## 9. Spacetime dissipation behaves the same way

If each active critical shell also carries an order-one scale-invariant local dissipation for a parabolic time comparable to \(\ell^2\), then its physical dissipation cost is

\[
\sim\ell.
\]

Summing over a positive log-density geometric stack again gives

\[
\sum\ell<\infty
\]

inside a fixed physical outer scale.

Therefore adding ordinary temporal thickening does not by itself change the conclusion.

## 10. No recurrence-multiplicity rescue from log density alone

This calculation is the R-critical analogue of the R-AC rerecording firewall.

The facts

\[
\text{infinitely many scales}
\]

and even

\[
\text{positive density of scales in }\log R
\]

do not imply a divergent physical parent cost when the per-scale cost is proportional to the physical radius.

Hence

\[
\boxed{
\text{positive log-density critical recurrence}
\not\Rightarrow
\text{finite-energy contradiction}.
}
\]

## 11. What the recurrent scattering structure does gain

The weak-critical root is now much more rigid than a vague escaping tail.

On a nontrivial ergodic component it contains:

1. a translation-covariant scattering datum \(A(q,\omega)\);
2. nonintegrability in global \(L^3_q\);
3. a fixed local scattering-mass threshold \(\varepsilon_*>0\);
4. positive log-density recurrence of that threshold;
5. corresponding positive log-density critical Morrey annuli.

Thus the remaining issue is not scarcity of critical scales.

It is the absence of a cross-scale rigidity law whose cost is stronger than the geometrically summable \(O(r)\) energy economics.

## 12. Highest-value next targets

Two existing structural routes now deserve calculation.

### A. Stress/force route

A \(1/R\) velocity tail has order-one momentum-stress flux through spheres because

\[
U\otimes U\sim R^{-2}
\]

and sphere area is \(R^2\).

Historical M5 stationary-tail modules already exploit this through point-force/stress identities.

The question is whether an invariant/ergodic **time-dependent scattering datum** has a corresponding mean stress-flux cocycle that can be compared with the smooth unforced core.

### B. Conditional CE-H harmonic route

Under the extra M17-349 coefficient-compact exterior-line hypotheses, M17-350 reduces the entire weak-critical harmonic obstruction to one toroidal dipole vector \(a\).

A direct M19 calculation can ask whether recurrent material flux/current structure forces that dipole coefficient to vanish or pay a remote/topological exit.

The stress route is more upstream and should be tested first.

---

\[
\boxed{\text{M19-017 COMPLETE; R-CRITICAL REQUIRES STRESS/RIGIDITY, NOT ENERGY COUNTING.}}
\]
