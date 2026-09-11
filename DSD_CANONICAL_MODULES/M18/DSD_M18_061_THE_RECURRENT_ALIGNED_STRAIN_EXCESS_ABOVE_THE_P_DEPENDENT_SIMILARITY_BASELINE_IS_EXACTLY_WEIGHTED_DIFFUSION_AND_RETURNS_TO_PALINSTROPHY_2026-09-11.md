# M18-061 — Recurrent aligned-strain excess above the p-dependent similarity baseline is exactly weighted diffusion and returns to palinstrophy

**Date:** 2026-09-11  
**Status:** ALIGNED-STRAIN SOURCE COMPRESSION / P-MOMENT BASELINE INTERPOLATION / PALINSTROPHY RETURN

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-060 shows that for every finite \(p\ge2\), the CE-H amplitude moment

\[
M_p=\int\rho^pdy
\]

satisfies

\[
\frac1pM_p'
=A_p-D_p-c_pM_p,
\]

where

\[
A_p:=\int\sigma\rho^pdy,
\]

\[
D_p:=\int\rho^{p-2}|\nabla W|^2dy
+(p-2)\int\rho^{p-2}|\nabla\rho|^2dy,
\]

and

\[
\boxed{c_p:=1-\frac{3}{2p}.}
\]

The source \(A_p\) was the remaining global recharge mechanism after \(\kappa\) was shown to be entirely dissipative.

The present module asks whether recurrent positive aligned strain is an independent source currency.

It is not. Its **excess above the exact similarity baseline \(c_p\)** is precisely the weighted diffusion charge \(D_p\), and under the compact amplitude ceiling this is bounded by ordinary palinstrophy.

## 2. Exact recurrent strain-excess identity

On an invariant recurrent compact CE-H component, \(M_p\) is a bounded state observable for every fixed finite \(p\), so

\[
\langle M_p'\rangle=0.
\]

Therefore M18-060 gives

\[
\boxed{
\left\langle
A_p-c_pM_p
\right\rangle
=
\langle D_p\rangle.
}
\]

Equivalently,

\[
\boxed{
\left\langle
\int
(\sigma-c_p)\rho^pdy
\right\rangle
=
\left\langle
\int\rho^{p-2}|\nabla W|^2
+(p-2)\rho^{p-2}|\nabla\rho|^2dy
\right\rangle.
}
\]

The right-hand side is nonnegative.

Hence

\[
\boxed{
\left\langle
\int(\sigma-c_p)\rho^pdy
\right\rangle
\ge0.
}
\]

But, more importantly, this excess is not a new signed source: it is exactly diffusion.

## 3. The p=2 endpoint is the quarter-strain identity

For \(p=2\),

\[
c_2=1-\frac34=\frac14,
\]

and

\[
D_2=P:=\int|\nabla W|^2dy.
\]

Therefore

\[
\boxed{
\left\langle
\int\left(\sigma-\frac14\right)\rho^2dy
\right\rangle
=
\langle P\rangle.
}
\]

This is exactly the global quarter-strain residence excess appearing in the M16/M17 strain-residence line.

Thus the old quarter-strain payer is the \(p=2\) member of the full amplitude-moment family.

## 4. The high-p baseline tends to unit axial strain

As \(p\to\infty\),

\[
\boxed{c_p\uparrow1.}
\]

Thus high-amplitude-weighted recurrent states naturally compare aligned strain with the similarity value

\[
\boxed{\sigma=1.}
\]

This is the same baseline that appears independently in the material tube area law

\[
D_B\log A=1-\sigma
\]

and in M16-019: a perfectly closed same-lineage amplitude/area/flux cycle has

\[
\frac1T\int_0^T\sigma\,d\theta=1.
\]

Therefore the family \(c_p\) continuously interpolates between

\[
\boxed{
\text{enstrophy residence baseline }\frac14
\quad\text{and}\quad
\text{high-amplitude tube baseline }1.
}
\]

This unifies two previously separate-looking strain thresholds.

## 5. Weighted diffusion is bounded by palinstrophy

On the compact CE-H hull let

\[
\rho\le M_*.
\]

The amplitude gradient obeys

\[
|\nabla\rho|\le|\nabla W|.
\]

Therefore

\[
\begin{aligned}
D_p
&=
\int\rho^{p-2}|\nabla W|^2
+(p-2)\rho^{p-2}|\nabla\rho|^2dy\\
&\le
(p-1)M_*^{p-2}
\int|\nabla W|^2dy.
\end{aligned}
\]

Hence

\[
\boxed{
D_p
\le
(p-1)M_*^{p-2}P.
}
\]

After recurrent averaging,

\[
\boxed{
0\le
\left\langle
\int(\sigma-c_p)\rho^pdy
\right\rangle
\le
(p-1)M_*^{p-2}\langle P\rangle.
}
\]

Thus every finite-\(p\) aligned-strain excess returns to ordinary palinstrophy.

## 6. High-amplitude local lower bound

Suppose a recurrent coherent recharge packet occupies a set \(Q\) with

\[
\rho\ge a_*>0
\]

and

\[
\sigma\ge c_p+\delta
\]

for some fixed \(\delta>0\).

Then its local strain-excess contribution is at least

\[
\boxed{
\int_Q(\sigma-c_p)\rho^pdy
\ge
\delta a_*^p|Q|.
}
\]

If such packets occur with fixed positive spacetime density and the negative part of \((\sigma-c_p)\rho^p\) is controlled so that a fixed positive recurrent **net** excess remains, the invariant identity forces a fixed positive weighted-diffusion payment.

On a fixed high-amplitude packet, \(\rho^{p-2}\ge a_*^{p-2}\), so this becomes a local first-derivative payment.

The global compact-hull conclusion remains: persistent net excess cannot avoid derivative payment.

## 7. Strain heterogeneity and same-tube geometry

M16-022--024 independently show that persistent same-tube axial-strain heterogeneity forces

\[
|\nabla\xi|\ge d_*>0
\]

on a recurrent coherent tube, and then splits into

- vortex-line curvature / label turnover;
- transverse director deformation.

M16-025--028 further reduce the latter to

- rank-two material director-area structure;
- or rank-one great-circle phase, whose nonzero survivor requires winding around the vorticity zero set.

Therefore the aligned-strain source has two complementary descriptions:

\[
\boxed{
\text{strain-paid recharge}
\Longrightarrow
\begin{cases}
\text{net p-moment excess}\to\text{weighted diffusion/palinstrophy},\\
\text{same-tube heterogeneity}\to\text{director geometry/turnover/topology}.
\end{cases}
}
\]

There is no remaining broad untyped `strain reservoir` category.

## 8. Relation to M17-399--400 phase tilt

M17-399 isolates the only non-gradient part of the exponentially tilted quarter-strain payer as a coefficient/strain phase covariance.

M17-400 then bounds that phase tilt by

\[
|\mathcal P_{\kappa\sigma}^{tilt}|
\lesssim
E_*^{1/2}
\langle H_{raw}\rangle^{1/2},
\]

so fixed phase-tilt residence forces raw-H2 occupancy.

The present module gives the complementary untitled hierarchy:

\[
\boxed{
\text{ordinary finite-p strain excess}
\to
P,
\qquad
\text{coefficient-phase tilted strain excess}
\to
H_{raw}.
}
\]

Both return to already known derivative-resource firewalls rather than defining new source currencies.

## 9. Why this does not close the branch globally

M18-059 remains in force.

A fixed normalized palinstrophy payment has favorable own-scale physical homogeneity but no certified finite original-parent total at a hypothetical singularity.

Across the finite-palinstrophy first ancient parent, second-generation records carry only the inverse-record weight

\[
R_m^{-1}.
\]

Therefore

\[
\boxed{
\text{strain excess}
\to
\text{palinstrophy}
\not\Rightarrow
\text{global ancestry contradiction}.
}
\]

The gain is classification, not final closure.

## 10. New interpretation of the recharge loop

The CE-H recurrent amplitude loop can now be written as

\[
\boxed{
\text{aligned strain source}
\to
\text{amplitude moment}
\to
\text{weighted diffusion / threshold retirement}
\to
\text{aligned strain source}.
}
\]

But the non-kinematic excess of the source is precisely paid by derivative structure.

Thus a quiet recurrent loop must either

1. live close to the exact p-dependent similarity baseline \(\sigma\approx c_p\) on each amplitude scale;
2. pay palinstrophy/raw-H2 for its excess;
3. develop same-tube director geometry/zero-set winding;
4. enter material/threshold/genealogy turnover.

This is substantially narrower than an arbitrary rechargeable strain mechanism.

## 11. Audit verdict

### Certified

1. The exact invariant identity
   \[
   \langle A_p-c_pM_p\rangle=\langle D_p\rangle
   \]
   holds for every finite \(p\ge2\).
2. \(p=2\) recovers the quarter-strain/palinstrophy relation.
3. \(c_p\to1\) links the amplitude-moment hierarchy to the unit-strain closed-tube baseline.
4. The weighted diffusion satisfies
   \[
   D_p\le(p-1)M_*^{p-2}P.
   \]
5. Ordinary recurrent aligned-strain excess is not an independent source currency; it returns to palinstrophy.
6. Coefficient-phase-tilted strain excess returns to raw-H2 by M17-400.
7. Same-tube strain heterogeneity routes to director geometry/turnover/topology.

### Still open

- ancestry closure of the resulting derivative payments;
- rank-two director-area recurrent geometry;
- zero-set winding in the rank-one great-circle branch;
- whether a multi-p baseline-coherent strain state can exist nontrivially without triggering one of the derivative/topological exits;
- remote and critical roots;
- global regularity.

## 12. Next target

The new sharp local target is the **multi-p baseline coherence** possibility.

A state cannot have

\[
\sigma\approx c_p
\]

for many substantially different values of \(p\) on the same high-amplitude material population unless either the amplitude distribution is sharply segregated or weighted diffusion remains active.

The next audit should compare two exponents \(2\le p<q\) and derive a covariance/segregation identity from

\[
\langle A_p-c_pM_p\rangle=\langle D_p\rangle,
\qquad
\langle A_q-c_qM_q\rangle=\langle D_q\rangle.
\]

The goal is to test whether a quiet strain source simultaneously compatible with the quarter-strain and unit-strain baselines must force amplitude/strain covariance, derivative payment, or concentration toward the top-amplitude set.