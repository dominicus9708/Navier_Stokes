# DSD M19-083 — Deep center-norm minima can recover only through logarithmically large core occupation and force diverging return gaps on the aperiodic survivor

**Date:** 2026-09-12  
**Status:** DEGENERATE-CENTER RECOVERY LAW / THE ONLY M19-082 ESCAPE HAS A QUANTITATIVE TEMPORAL SIGNATURE: DEEP NORM LOSS REQUIRES LONG CORE-AMPLIFICATION HISTORY AND CANNOT RECUR WITH UNIFORMLY BOUNDED RETURN GAPS / GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED

## 1. Purpose

M19-082 split a possible extra bounded center direction into:

\[
\text{uniformly nondegenerate center}
\quad\lor\quad
\text{deep norm-degeneration center}.
\]

The first branch gives fixed-window observability and finite-dimensionality.

The remaining branch has

\[
\boxed{
\sup_tE(t)<\infty,
\qquad
\inf_tE(t)=0,
}
\]

while the trajectory still returns infinitely often to an order-one norm if it is recurrent and nontrivial.

The present module quantifies the cost of each recovery from a deep minimum.

## 2. Remote damping identity in normalized form

Start from M19-079:

\[
\boxed{
\frac12E'
+c_*E_o
\le
K_RE_c.
}
\tag{1}
\]

Let

\[
f_c(t):=\frac{E_c(t)}{E(t)},
\qquad
f_o(t):=1-f_c(t),
\]

whenever \(E(t)>0\).

A nonzero linear parabolic trajectory cannot become exactly zero at one finite time without being identically zero by uniqueness, so this ratio is well defined for every finite time on a nontrivial complete trajectory.

Divide (1) by \(E\):

\[
\boxed{
\frac12(\log E)'
+c_*(1-f_c)
\le
K_Rf_c.
}
\]

Therefore

\[
\boxed{
\frac12(\log E)'
\le
(K_R+c_*)f_c-c_*.
}
\tag{2}
\]

This is the scale-invariant recovery inequality.

## 3. Logarithmic core-occupation cost of one recovery

Suppose

\[
E(a)=E_{min}>0,
\qquad
E(b)=E_{ret}>E_{min},
\qquad
b>a.
\]

Integrate (2):

\[
\frac12\log\frac{E_{ret}}{E_{min}}
\le
(K_R+c_*)
\int_a^bf_c(t)dt
-c_*(b-a).
\]

Hence

\[
\boxed{
\int_a^bf_c(t)dt
\ge
\frac{1}{2(K_R+c_*)}
\log\frac{E_{ret}}{E_{min}}
+
\frac{c_*}{K_R+c_*}(b-a).
}
\tag{3}
\]

In particular,

\[
\boxed{
\int_a^bf_c(t)dt
\ge
\frac{1}{2(K_R+c_*)}
\log\frac{E_{ret}}{E_{min}}.
}
\tag{4}
\]

Thus recovery from an arbitrarily deep norm minimum requires an arbitrarily large accumulated **fractional core residence**.

This cost is independent of the arbitrary linear normalization of \(W\).

## 4. Minimum recovery time

Since

\[
0\le f_c\le1,
\]

(2) also gives the crude maximal growth rate

\[
\frac12(\log E)'
\le K_R.
\]

Therefore

\[
\boxed{
 b-a
\ge
\frac{1}{2K_R}
\log\frac{E_{ret}}{E_{min}}
}
\tag{5}
\]

when \(K_R>0\).

If \(K_R=0\), no positive recovery is possible at all.

Hence deep norm degeneration has an unavoidable logarithmically diverging recovery time.

## 5. Additive core-energy cost

Dropping the negative exterior damping from (1) gives

\[
\frac12E'\le K_RE_c.
\]

Integrating,

\[
\boxed{
\int_a^bE_c(t)dt
\ge
\frac{E_{ret}-E_{min}}{2K_R}.
}
\tag{6}
\]

For a fixed return threshold

\[
E_{ret}\ge E_*>0
\]

and deep minima \(E_{min}\to0\), every recovery pays at least

\[
\boxed{
\int_a^bE_c(t)dt
\gtrsim
\frac{E_*}{2K_R}.
}
\]

This is an additive perturbation-core occupation cost.

It is **not** yet a finite original Navier--Stokes resource ledger, because \(E_c\) belongs to the linearized perturbation and its integral over infinite similarity time need not be finite.

## 6. Recurrent return to a fixed norm threshold

Assume a nontrivial bounded center trajectory has a sequence of deep minima

\[
a_n\to\infty,
\qquad
E(a_n)=\varepsilon_nE_*,
\qquad
\varepsilon_n\downarrow0,
\]

and after each minimum returns to

\[
E(b_n)\ge E_*.
\]

Then (5) gives

\[
\boxed{
 b_n-a_n
\ge
\frac1{2K_R}\log\frac1{\varepsilon_n}
\longrightarrow\infty.
}
\tag{7}
\]

Therefore

\[
\boxed{
\text{deep center-norm degeneration}
\Longrightarrow
\text{diverging recovery/return gaps}.
}
\]

This is the precise temporal signature left open by M19-081.

## 7. Uniformly recurrent or relative-periodic branches cannot use this escape

Suppose there is a finite \(T_{max}\) such that every sufficiently late state returns to the fixed norm threshold within time at most \(T_{max}\).

Then (7) implies

\[
\log\frac{E_*}{E_{min}}
\le
2K_RT_{max},
\]

so

\[
\boxed{
E_{min}
\ge
E_*e^{-2K_RT_{max}}>0.
}
\]

Hence deep degeneration is impossible.

In particular, a relative-periodic screw branch from M19-076 has a finite recurrence period modulo rotation. Since rotations preserve the weighted radial norm,

\[
\boxed{
\text{relative periodicity}
\Longrightarrow
\text{uniform norm nondegeneration}
}
\]

for every nonzero relative-periodic center direction whose monodromy is bounded and invertible on the neutral subspace.

Thus the M19-083 escape belongs only to the genuinely aperiodic long-return branch.

## 8. Relation to M19-081 Bernoulli-type temporal gaps

M19-081 showed abstractly that recurrent mixing systems can have positive active density and arbitrarily long inactive gaps.

M19-083 now shows what the Navier--Stokes linearized energy inequality does inside such a gap:

\[
\boxed{
\text{long weak-core interval}
\Rightarrow
\text{strong norm decay},
}
\]

and conversely recovering that norm requires a proportionally long core-active history.

Therefore the surviving aperiodic center mechanism is not a cost-free symbolic churn. It must realize a genuine long-timescale amplitude excursion.

## 9. Projective interpretation

After normalizing the perturbation direction,

\[
\widehat W(t)=\frac{W(t)}{\|W(t)\|_X},
\]

the quantity

\[
f_c(t)
=
\frac{E_c}{E}
\]

is purely projective.

Equation (3) says that a large negative excursion of the scalar amplitude cocycle

\[
\log\|W(t)\|_X
\]

can be reversed only if the projective trajectory accumulates enough time in the core-visible region.

Thus the extra-center survivor has two inseparable coordinates:

\[
\boxed{
\text{projective core-return history}
+\text{scalar norm cocycle excursion}.
}
\]

This is a more precise target than an abstract zero Lyapunov exponent.

## 10. No contradiction from infinite recovery cost alone

If infinitely many disjoint deep-minimum recoveries occur, (6) implies

\[
\sum_n
\int_{a_n}^{b_n}E_c(t)dt
=\infty
\]

for returns to a fixed threshold.

But this is not yet contradictory.

There is no certified finite total budget for the perturbation quantity

\[
\int_{0}^{\infty}E_c(t)dt
\]

in similarity time.

Therefore one must not convert the recovery count directly into a global Navier--Stokes contradiction.

The positive result is temporal rigidity, not a finite-resource closure.

## 11. Updated branch tree

Combining M19-076 and M19-082--083:

\[
\boxed{
\mathcal C_{neutral}^{extra}
\Longrightarrow
\begin{cases}
\text{uniformly nondegenerate}
\Rightarrow
\text{fixed-window observable and finite-dimensional},\\
\text{deeply degenerate}
\Rightarrow
\text{aperiodic with diverging recovery gaps and logarithmic core residence}.
\end{cases}
}
\]

Relative-periodic or uniformly recurrent neutral motion is routed to the first branch.

## 12. What remains open

M19-083 does not prove:

1. that deep-degeneration center modes exist;
2. that they cannot exist;
3. a finite original-solution budget for their recovery cost;
4. that finite-dimensional observable centers are symmetry-only;
5. exclusion of an aperiodic weak-critical scattering factor;
6. global regularity.

## 13. Next target

The center problem is now naturally split by **amplitude cocycle behavior**.

For the finite-dimensional uniformly nondegenerate branch, the next useful calculation is to determine what the scattering map does to a finite-dimensional neutral bundle.

For the deep-degeneration branch, the natural question is whether the required diverging return gaps are compatible with the actual recurrent scattering translation law and the finite spectator-boundary history.

The next module should first test the finite-dimensional branch, because it has stronger algebraic structure and may reduce the allowable q-translation dynamics to a finite-dimensional representation.

---

\[
\boxed{\text{M19-083 COMPLETE.}}
\]
