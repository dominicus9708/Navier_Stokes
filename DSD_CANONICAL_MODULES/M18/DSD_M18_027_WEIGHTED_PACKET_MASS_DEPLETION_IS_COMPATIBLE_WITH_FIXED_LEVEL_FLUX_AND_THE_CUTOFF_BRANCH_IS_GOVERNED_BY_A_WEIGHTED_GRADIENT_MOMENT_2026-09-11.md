# M18-027 — Weighted packet-mass depletion is compatible with fixed level flux, and the cutoff branch is governed by a weighted gradient moment

**Date:** 2026-09-11  
**Status:** ACTIVE DSD ANALYSIS / MASS-DEPLETION CORRECTION / WEIGHTED-GRADIENT REFINEMENT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-026 left the scale-invariant packet-mass parameter

\[
\mathfrak M_\rho
=\sqrt\Gamma\,\delta_0^{-1/2}
\int_{\mathcal C}\rho^2dx
\]

as a possible escape when the normalized collar gradient

\[
\Gamma=|\nabla\kappa|^2/\delta_0^3
\]

becomes large.

This module audits whether

\[
\mathfrak M_\rho\to0
\]

is itself incompatible with the retained robust level-flux witness.

The answer is **no**. A steep coefficient layer can keep a fixed surface flux while its volume-weighted vorticity mass decreases because the normal thickness shrinks. Therefore weighted packet-mass depletion must not be treated as an automatic nodal or palinstrophy contradiction.

The same calculation reveals that the essential-supremum parameter used in M18-023 is stronger than necessary for the cutoff current. The exact residual depends on a first-jet-weighted average of the normalized gradient.

## 2. Local coarea dictionary

Let

\[
g:=|\nabla\kappa|,
\qquad
F(s):=\int_{\{\kappa=s\}}\rho^2g\,dS.
\]

For a spatial region \(U\) contained in a regular coefficient slab, define the local level flux

\[
F_U(s):=\int_{\{\kappa=s\}\cap U}\rho^2g\,dS.
\]

Coarea gives

\[
\boxed{
\int_U\rho^2g^2dx
=\int F_U(s)ds.
}
\]

It also gives

\[
\boxed{
\int_U\rho^2dx
=\int
\left(
\int_{\{\kappa=s\}\cap U}\frac{\rho^2}{g}dS
\right)ds.
}
\]

These two formulas distinguish surface flux from volume mass.

## 3. Fixed flux does not force fixed packet mass

Suppose on an anisotropic packet from M18-026 one has

\[
g\asymp G
\]

and a coefficient interval of width

\[
\Delta s\asymp\delta_0.
\]

Then

\[
B_U:=\int_U\rho^2g^2dx
\asymp
\int_{\Delta s}F_U(s)ds.
\]

If

\[
F_U(s)\asymp J_U
\]

through the interval, then

\[
\boxed{
B_U\asymp\delta_0J_U.
}
\]

By contrast,

\[
M_U:=\int_U\rho^2dx
\asymp
\frac{1}{G^2}
\int_{\Delta s}F_U(s)ds
\asymp
\boxed{\frac{\delta_0J_U}{G^2}}.
\]

Since

\[
G^2=\delta_0^3\Gamma,
\]

we obtain

\[
M_U\asymp
\frac{J_U}{\delta_0^2\Gamma}.
\]

Therefore

\[
\boxed{
\sqrt\Gamma\,\delta_0^{-1/2}M_U
\asymp
\frac{J_U}{\delta_0^{5/2}\sqrt\Gamma}.
}
\]

Even if the normalized local flux ratio

\[
J_U/\delta_0^{5/2}
\]

stays nonzero, the packet-mass parameter decreases like \(\Gamma^{-1/2}\).

Hence

\[
\boxed{
\mathfrak M_\rho\to0
\not\Rightarrow
\text{loss of robust level flux}.
}
\]

This is a correction to any interpretation that treated packet-mass depletion by itself as a contradiction candidate.

## 4. What robust local flux does force

If a high-gradient packet carries a fixed fraction of the retained level flux through a fixed coefficient interval, i.e.

\[
F_U(s)\ge c_FJ_*
\]

for \(s\) in an interval of length \(c_\delta\delta_0\), then coarea directly gives

\[
\boxed{
B_U
\ge
c_Fc_\delta\,J_*\delta_0.
}
\]

This lower bound is independent of \(\Gamma\).

Thus high-gradient mass depletion does not erase the first-jet payment when the same packet actually carries persistent flux. The correct distinction is:

\[
\boxed{
\text{high-gradient packet is flux-bearing}
\quad\text{or}\quad
\text{it is a spectator relative to the retained flux event}.}
\]

A pointwise coefficient-gradient spike that carries vanishing weighted flux must not be charged to the robust flux branch merely because it lies in the same collar.

## 5. Re-audit of the M18-023 cutoff residual

M18-023 obtained, for \(\phi=\chi^2\),

\[
|\mathcal C_\phi|
\le
\varepsilon\nu^{-1}H_\phi
+
\frac{C\nu}{\varepsilon\delta_0^2}
\int_{\mathcal K}\rho^2g^4dx.
\]

Define

\[
B_{\mathcal K}
:=
\int_{\mathcal K}\rho^2g^2dx.
\]

When \(B_{\mathcal K}>0\), define the scale-invariant weighted gradient moment

\[
\boxed{
\overline\Gamma_{\mathcal K}
:=
\frac{
\int_{\mathcal K}\rho^2g^4dx
}{
\delta_0^3
\int_{\mathcal K}\rho^2g^2dx
}.
}
\]

This is scale invariant because the numerator scales as \(R^{13}\), while \(\delta_0^3B_{\mathcal K}\) also scales as \(R^{13}\).

Equivalently, with the probability measure

\[
d\mu_{\mathcal K}
:=
\frac{\rho^2g^2dx}{B_{\mathcal K}},
\]

one has

\[
\boxed{
\overline\Gamma_{\mathcal K}
=
\int_{\mathcal K}
\frac{g^2}{\delta_0^3}
\,d\mu_{\mathcal K}.
}
\]

Thus the cutoff current sees the normalized gradient only through the existing first-jet weight.

## 6. Exact weighted-moment cutoff bound

By definition,

\[
\int_{\mathcal K}\rho^2g^4dx
=
\delta_0^3
\overline\Gamma_{\mathcal K}
B_{\mathcal K}.
\]

Therefore the M18-023 estimate sharpens to

\[
\boxed{
|\mathcal C_\phi|
\le
\varepsilon\nu^{-1}H_\phi
+
C_{\chi,\varepsilon}\nu
\,\delta_0
\overline\Gamma_{\mathcal K}
B_{\mathcal K}.
}
\]

This is strictly weaker than requiring

\[
\Gamma_{\mathcal K}^{\sup}
:=
\operatorname*{ess\,sup}_{\mathcal K}
\frac{g^2}{\delta_0^3}
<\infty,
\]

because

\[
\overline\Gamma_{\mathcal K}
\le
\Gamma_{\mathcal K}^{\sup}.
\]

A very large pointwise gradient on a set with negligible first-jet weight can therefore be completely harmless for the cutoff current.

## 7. DSD correction to the branch tree

The earlier branch

\[
G_{\Gamma_{\mathcal K}^{\sup}\to\infty}
\]

was overinclusive as a cutoff obstruction.

For the cutoff-current problem, the canonical branch is instead

\[
\boxed{
G_{\overline\Gamma_{\mathcal K}\to\infty}.
}
\]

An essential-supremum gradient spike with bounded \(\overline\Gamma_{\mathcal K}\) is a **spectator spike** for this channel.

M18-026 remains a valid local packet theorem for such sup-gradient spikes, but its mass-depletion branch is no longer a necessary unresolved branch of the cutoff current.

## 8. Relation to robust level flux

By coarea,

\[
B_{\mathcal K}
=
\int_{I_{\mathcal K}}F(s)ds
\]

for the collar coefficient interval \(I_{\mathcal K}\).

Hence a robust level-flux floor across a fixed fraction of the collar gives a first-jet floor automatically.

However, it does **not** bound \(\overline\Gamma_{\mathcal K}\) from above. Large weighted gradient moment can occur if the first-jet measure itself shifts toward progressively steeper sublayers.

Therefore the refined live concentration branch is

\[
\boxed{
\text{weighted first-jet measure concentrates on high normalized gradient}.}
\]

This is stronger and more relevant than unweighted or essential-supremum coefficient-gradient concentration.

## 9. Snapshot-to-spacetime firewall remains

The quantity

\[
\overline\Gamma_{\mathcal K}B_{\mathcal K}
\]

appears inside an instantaneous cutoff bound. A large value is not yet an ancestry contradiction.

One still needs either

- positive time measure of the weighted-gradient concentration event;
- a temporal growth/thickening theorem;
- or a direct spacetime estimate of the quartic collar charge.

Thus

\[
\boxed{
\text{weighted-gradient concentration}
\neq
\text{ancestry contradiction}.
}
\]

## 10. Audit verdict

### Certified

1. Weighted packet-mass depletion can coexist with fixed local level flux in a steep layer.
2. Therefore \(\mathfrak M_\rho\to0\) is not by itself a nodal, palinstrophy, or flux-loss contradiction.
3. If the packet carries persistent local level flux, coarea already gives a first-jet payment independent of \(\Gamma\).
4. The cutoff current is governed by the weighted normalized-gradient moment \(\overline\Gamma_{\mathcal K}\), not by the essential supremum alone.
5. Pointwise high-gradient spectator spikes are removed from the canonical cutoff branch when their first-jet weight is negligible.

### Not certified

1. A uniform bound on \(\overline\Gamma_{\mathcal K}\).
2. A spacetime ledger for the quartic collar charge.
3. Temporal thickness of weighted-gradient concentration.
4. Elimination of trace-free Hessian / tube-geometry decompactification.
5. Global 3D Navier--Stokes regularity.

## 11. Next target

The next target is the exact quartic collar cost

\[
\delta_0^{-2}
\int_{\mathcal K}\rho^2|\nabla\kappa|^4dx.
\]

M18-028 should optimize the coefficient cutoff itself rather than fixing a uniform-slope cutoff. By coarea this becomes a one-dimensional weighted variational problem in coefficient level. The aim is to determine whether a low-current transition can always be placed through a favorable subcollar, or whether the collar must have high gradient-weighted conductance across every level.