# M18-029 — High harmonic collar conductance forces distributed flux-weighted gradient concentration across coefficient levels

**Date:** 2026-09-11  
**Status:** ACTIVE DSD ANALYSIS / CONDUCTANCE DISTRIBUTION / SPECTATOR-SPIKE EXCLUSION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-028 reduced the optimized cutoff-current cost on a record interval \(I\) to the harmonic coefficient-collar conductance

\[
\mathcal G_{c,I}
=
\left(
\int_{s_-}^{s_+}
\frac{ds}{\mathbb W_I(s)}
\right)^{-1},
\]

where

\[
\mathbb W_I(s)
:=
\int_I
\int_{\{\kappa=s\}}
\rho^2|\nabla\kappa|^3dSdt.
\]

A large value means that no coefficient-level bottleneck gives a cheap transition.

This module quantifies that statement and compares it with the existing first-coefficient-jet spacetime charge.

## 2. Time-integrated level flux and first-jet charge

Define

\[
\mathbb F_I(s)
:=
\int_I
F(s,t)dt
=
\int_I
\int_{\{\kappa=s\}}
\rho^2|\nabla\kappa|dSdt.
\]

Let the collar length be

\[
L_c:=s_+-s_-.
\]

By coarea, the collar first-coefficient-jet spacetime charge is

\[
\boxed{
Q_{B,I}
:=
\int_I\int_{\{s_-<\kappa<s_+\}}
\rho^2|\nabla\kappa|^2dxdt
=
\int_{s_-}^{s_+}\mathbb F_I(s)ds.
}
\]

This is the inherited M17-445 / M18 first-jet \(R^{-5}\) resource when the collar lies inside the certified compact CE-H bin.

## 3. High conductance excludes a large low-W level set

Fix

\[
0<a<1.
\]

Define

\[
E_W(a)
:=
\left\{
s\in[s_-,s_+]:
\mathbb W_I(s)
\le
a\,\mathcal G_{c,I}L_c
\right\}.
\]

Since

\[
\frac1{\mathcal G_{c,I}}
=
\int\frac{ds}{\mathbb W_I(s)},
\]

we have

\[
\frac1{\mathcal G_{c,I}}
\ge
\frac{|E_W(a)|}
{a\mathcal G_{c,I}L_c}.
\]

Hence

\[
\boxed{
|E_W(a)|\le aL_c.
}
\]

Equivalently, on at least a fraction \(1-a\) of the coefficient collar,

\[
\boxed{
\mathbb W_I(s)
>a\mathcal G_{c,I}L_c.
}
\]

Thus high harmonic conductance is necessarily distributed in coefficient level; it cannot be generated solely by a sparse collection of high-W levels.

## 4. Bounded first-jet charge gives many moderate-F levels

Fix

\[
0<b<1.
\]

By Markov's inequality, the set

\[
E_F(b)
:=
\left\{
s:
\mathbb F_I(s)
>
\frac{Q_{B,I}}{bL_c}
\right\}
\]

satisfies

\[
\boxed{
|E_F(b)|\le bL_c.
}
\]

Therefore on at least a fraction \(1-b\) of the collar,

\[
\mathbb F_I(s)
\le
\frac{Q_{B,I}}{bL_c}.
\]

## 5. Distributed normalized gradient concentration

Choose, for concreteness,

\[
a=b=\frac14.
\]

Then

\[
|E_W(1/4)^c|\ge\frac34L_c,
\]

and

\[
|E_F(1/4)^c|\ge\frac34L_c.
\]

Their intersection has measure at least

\[
\boxed{
\frac12L_c.
}
\]

On this intersection,

\[
\mathbb W_I(s)
>
\frac14\mathcal G_{c,I}L_c,
\]

while

\[
\mathbb F_I(s)
\le
\frac{4Q_{B,I}}{L_c}.
\]

Hence

\[
\boxed{
\frac{\mathbb W_I(s)}{\mathbb F_I(s)}
\ge
\frac{\mathcal G_{c,I}L_c^2}
{16Q_{B,I}}.
}
\]

For \(\mathbb F_I(s)>0\), define the time-integrated flux-weighted normalized gradient moment

\[
\boxed{
\gamma_I(s)
:=
\frac{\mathbb W_I(s)}
{\delta_0^3\mathbb F_I(s)}.
}
\]

Then on at least half of the coefficient collar,

\[
\boxed{
\gamma_I(s)
\ge
\frac{L_c^2}{16\delta_0^2}
\frac{\mathcal G_{c,I}}
{\delta_0Q_{B,I}}.
}
\]

## 6. Dimensionless conductance ratio

Define

\[
\boxed{
\mathfrak C_I
:=
\frac{\mathcal G_{c,I}}
{\delta_0Q_{B,I}}.
}
\]

This is scale invariant.

For a fixed fractional collar,

\[
L_c=c_L\delta_0
\]

with fixed \(c_L>0\), Section 5 becomes

\[
\boxed{
\gamma_I(s)
\ge
\frac{c_L^2}{16}\mathfrak C_I
}
\]

on a coefficient-level set of measure at least \(L_c/2\).

Thus

\[
\boxed{
\mathfrak C_I\to\infty
\quad\Longrightarrow\quad
\text{flux-weighted normalized gradient concentration on a positive fraction of coefficient levels}.
}
\]

This excludes the interpretation of high optimized cutoff cost as an isolated spectator spike.

## 7. Exact DSD split

The optimized cutoff cost now has a three-way classification.

### A. First-jet-owned regime

If

\[
\mathfrak C_I\le C_*,
\]

then

\[
\boxed{
\mathcal G_{c,I}
\le
C_*\delta_0Q_{B,I}.
}
\]

Under a compact normalized coefficient width, the cutoff residual is owned by the inherited first-jet spacetime ledger.

### B. Large first-jet charge

If \(Q_{B,I}\) itself becomes large, that is directly the existing first-coefficient-jet/D3 payer and must be tested against the \(R^{-5}\) ancestry weight.

### C. Distributed weighted-gradient concentration

If the cutoff cost is not first-jet-owned while \(Q_{B,I}\) remains controlled, then

\[
\boxed{
\mathfrak C_I\to\infty,
}
\]

which forces \(\gamma_I\to\infty\) on a fixed positive fraction of coefficient levels.

Hence

\[
\boxed{
\begin{aligned}
G_{\rm high\ optimized\ cutoff\ cost}
\Longrightarrow{}&
G_{\rm first\text{-}jet\ spacetime\ charge}\\
&\lor
G_{\rm distributed\ flux\text{-}weighted\ gradient\ concentration}\\
&\lor
G_{\rm collar/tube/domain\ loss}.
\end{aligned}
}
\]

## 8. What distributed concentration does not yet prove

Large \(\gamma_I(s)\) means that, under the spacetime level-flux measure at coefficient level \(s\), the normalized quantity

\[
|\nabla\kappa|^2/\delta_0^3
\]

has large mean.

It does **not** by itself imply:

- a fixed positive fraction of the flux sits above one specific gradient threshold;
- a full-Hessian lower bound;
- a D4 spacetime payment;
- a contradiction with the D3 ledger.

A large mean can still be carried by increasingly thin high-gradient tails inside each level. Any attempt to promote the mean to thickness requires an additional moment, second-jet regularity, or a geometric propagation theorem.

## 9. Relation to M18-026

M18-026 audited one pointwise high-gradient packet. M18-029 shows when such packets become relevant to the optimized cutoff problem:

- isolated high-gradient packets with negligible flux weight are spectators;
- if high conductance survives relative to the total first-jet charge, high normalized gradients must be seen by the flux measure across a positive fraction of coefficient levels.

Thus the local packet branch and the global collar conductance branch are now consistently linked.

## 10. Audit verdict

### Certified

1. High harmonic conductance forces high \(\mathbb W_I\) on most coefficient levels.
2. If the first-jet charge is controlled, at least half the collar has a quantitatively large flux-weighted normalized gradient mean.
3. The scale-invariant ratio \(\mathfrak C_I=\mathcal G_{c,I}/(\delta_0Q_{B,I})\) is the correct measure of cutoff cost not already owned by the first-jet ledger.
4. Isolated spectator spikes cannot explain \(\mathfrak C_I\to\infty\).

### Not certified

1. A higher-moment bound converting large mean into a positive flux fraction above a gradient threshold.
2. A second-jet/geometric propagation theorem for the distributed high-gradient tail.
3. A D4 ancestry ledger from this branch.
4. Global ancestry divergence.
5. Global 3D Navier--Stokes regularity.

## 11. Next target

At this point the local zero-tube/cutoff analysis has reached a genuine concentration endpoint rather than an algebraic bookkeeping gap.

M18-030 should perform a consolidation audit of M18-020--029 and separate:

- branches already reduced to certified standard resources;
- branches that are merely representation/domain/genealogy losses;
- genuinely new analytic concentration endpoints.

That audit should determine whether continuing to differentiate the local CE-H structure is still productive, or whether the analysis should move back upward to genealogy and the non-CE-H root branches.