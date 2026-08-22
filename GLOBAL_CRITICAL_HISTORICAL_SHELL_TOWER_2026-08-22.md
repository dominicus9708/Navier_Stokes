# Global Critical Historical-Shell Tower — 2026-08-22

Status: **SCALING-CONSISTENCY / ADVERSARIAL SURVIVOR AUDIT. THIS IS NOT A CONSTRUCTION OF A NAVIER--STOKES SINGULAR SOLUTION. GLOBAL REGULARITY NOT PROVED.**

This note tests whether the current smooth first-hitting inequalities, local P_V closures, T/H routing, remote-halo gates, and kinetic-energy packing already forbid reuse of one active packet through infinitely many geometric scales.

They do not. The remaining scaling-consistent object is a historical nested-shell tower with the critical velocity profile `U~1/R` and vorticity profile `Omega~1/R^2` in current first-hitting coordinates.

## 1. Geometric scales

Let

\[
W_j=K_j^2,
\qquad
K_{j+1}=\lambda K_j,
\qquad
\lambda>1.
\]

Equivalently the vorticity first-hitting ratio is

\[
q=\lambda^2.
\]

At stage `j`, consider the remnant of a natural packet created at an older stage `m<=j`. Its physical natural radius at creation was

\[
r_m\asymp K_m^{-1}.
\]

In the current normalized coordinate `y=K_j(x-X_j)`, the corresponding radius is

\[
\boxed{
R_{j,m}=\frac{K_j}{K_m}=\lambda^{j-m}.
}
\]

The scale-compatible historical amplitudes are

\[
\boxed{
|U_{j,m}|\asymp R_{j,m}^{-1},
\qquad
|\Omega_{j,m}|\asymp R_{j,m}^{-2}.
}
\]

These are exactly the amplitudes obtained by viewing an older natural packet in the newer normalization.

## 2. One shell is critical for L3

Take an annulus of radius and thickness comparable to `R` so its normalized volume is `~R^3`. Then

\[
\int_{A_R}|U|^3dy
\asymp
R^{-3}R^3
\asymp1.
\]

Thus each historical octave contributes a fixed amount to the **cube** of the strong critical norm:

\[
\boxed{
\|U_j\|_3^3
\gtrsim c\,N_{shell}(j).
}
\]

For one shell per geometric scale,

\[
N_{shell}(j)\asymp j
\asymp \frac{\log(K_j/K_0)}{\log\lambda}.
\]

Hence

\[
\boxed{
\|U_j\|_3^3\sim c\log K_j,
\qquad
\|U_j\|_3\sim c^{1/3}(\log K_j)^{1/3}.
}
\]

This is the logarithmic strong-L3 divergence of a truncated `1/R` profile.

## 3. Weak-L3 remains bounded

For the idealized radial size law

\[
|U(y)|\asymp c|y|^{-1}
\]

on `1<=|y|<=R_max`, the distribution function obeys

\[
|\{|U|>a\}|\asymp (c/a)^3
\]

for the relevant amplitude range. Therefore

\[
\boxed{
\|U\|_{L^{3,\infty}}\asymp c,
}
\]

uniformly in the number of shells.

So the tower is exactly at the large weak-L3 / Type-I critical frontier: strong L3 diverges because more logarithmic shells are exposed, while the weak-L3 amplitude need not grow.

## 4. Energy and enstrophy remain scaling-compatible

For one shell,

\[
\int_{A_R}|U|^2dy
\asymp R^{-2}R^3
\asymp R.
\]

Physical kinetic energy is related to current normalized kinetic energy by

\[
\|u\|_2^2=K_j^{-1}\|U_j\|_2^2.
\]

Hence the old stage-m shell costs

\[
K_j^{-1}R_{j,m}
=
K_j^{-1}\frac{K_j}{K_m}
=
\boxed{K_m^{-1}}.
\]

Thus historical shell energies form a geometric series and are compatible with finite kinetic energy.

For normalized enstrophy,

\[
Z_{shell}(R)
\asymp R^{-4}R^3
=R^{-1}.
\]

Hence

\[
\boxed{
\sum_{m\le j}Z_{shell}(R_{j,m})\lesssim1.
}
\]

Restoring physical scale,

\[
\|\omega(t_j)\|_2^2
=K_j Z_j
\asymp K_j,
\]

which is exactly the first-hitting endpoint scaling already permitted by the enstrophy/determinant ledger.

## 5. Derivative packets also remain summable in normalized space

On a shell of radius `R`,

\[
|\nabla\Omega|\asymp R^{-3},
\]

so

\[
Q_{shell}(R)
:=\int_{A_R}|\nabla\Omega|^2dy
\asymp R^{-6}R^3
=R^{-3}.
\]

Therefore

\[
\boxed{
\sum_{m\le j}Q_{shell}(R_{j,m})\lesssim1.
}
\]

The same scaling occurs for cubic strain/determinant contributions: `Sigma~R^-2` gives

\[
\int_{A_R}|\Sigma|^3dy\asymp R^{-3}.
\]

Thus old T/H activity can become a passive outer history while the newest inner shell carries the order-one derivative/determinant activity. There is no automatic growth of the normalized H/P_V costs with the number of historical shells.

## 6. Physical picture

At a late time, the tower occupies physical radii

\[
K_j^{-1}\lesssim r\lesssim K_0^{-1}.
\]

Its velocity magnitude has the critical form

\[
|u(r)|\sim r^{-1}
\]

across logarithmic scales, while vorticity behaves like

\[
|\omega(r)|\sim r^{-2}.
\]

The kinetic energy is locally finite because

\[
\int_0^{r_0}r^{-2}r^2dr<\infty,
\]

whereas the strong critical velocity norm has the logarithmic shell divergence

\[
\int_{r_j}^{r_0}r^{-3}r^2dr
\sim\log(r_0/r_j).
\]

This is the classical borderline geometry behind weak-L3 Type-I/DSS scenarios.

## 7. Why the current packing strategy cannot exclude it

A current natural packet pays physical kinetic-energy dissipation of order

\[
K_j^{-1}.
\]

One new packet per geometric stage therefore pays

\[
\sum_jK_j^{-1}<\infty.
\]

Old shells do not create an additional order-K_j multiplicity at the **current** terminal scale; their enstrophy and palinstrophy decay as `R^-1` and `R^-3` in current coordinates.

Consequently the previously hoped-for implication

\[
\text{repeated T/H cycle}\Longrightarrow N_j\gtrsim K_j
\]

is false at the level of scaling alone. Historical shell multiplicity can grow like `j` while current natural-scale multiplicity remains one.

## 8. Relation to known critical regularity theory

The tower explains why bounded strong `L3` would close the branch, but weak-L3 does not. A first singular time forces the strong `L3` norm to diverge, while a `1/r` shell tower achieves this by logarithmic accumulation with bounded weak-L3 size.

Quantitative Type-I results give logarithmic lower growth for the **integral** of `|u|^3` on expanding self-similar balls, which is exactly the shell-counting rate above. Thus this model sits at, rather than violates, the known Type-I/DSS critical barrier.

Exact backward self-similar solutions are excluded under classical hypotheses, and backward DSS singularities are excluded in several restricted regimes (including scaling factor sufficiently close to one under a pointwise Type-I bound), but the general nontrivial backward DSS problem remains open.

## 9. Corrected final global target

The remaining problem is no longer accurately described as only a same-stage packet-multiplicity problem.

The minimal surviving mechanism is

\[
\boxed{
\text{new inner active core per stage}
+
\text{passive historical }1/r\text{ shell tower}.
}
\]

To close it, at least one genuinely new statement is required:

1. a **shell-recycling obstruction** showing that one T/H event per scale cannot leave a passive critical remnant;
2. a **recurrence-to-DSS theorem** showing that sufficiently repetitive shell profiles force an asymptotically DSS regime to which a Liouville/nonexistence theorem applies;
3. a **nonrecurrence action theorem** showing that failure of shell recurrence accumulates a globally non-summable cost;
4. a new positive scale-critical global functional not already contained in kinetic-energy dissipation.

A fixed natural packet cost, fixed roughness packet, fixed determinant producer action, or fixed boundary-turnover cost per stage is insufficient by itself.

Status: **THE CURRENT SMOOTH-ONLY REDUCTIONS FORCE THE GLOBAL SURVIVOR TO A NEAR-FIELD, FREQUENCY-LOCAL CRITICAL SHELL-RECYCLING CASCADE. THIS TOWER HAS `U~1/R`, BOUNDED WEAK-L3, LOGARITHMIC STRONG-L3 CUBE GROWTH, FINITE ENERGY, AND O(1) CURRENT NORMALIZED ENSTROPHY/PALINSTROPHY. THE NEXT REQUIRED INPUT MUST BREAK SHELL RECYCLING OR ITS DSS-LIKE LIMIT; ORDINARY ENERGY PACKING CANNOT.**