# DSD M19-351 — Regular transverse condenser capacity turns any fixed-power sign-flux thinning into a nonsummable palinstrophy cost on persistent diffuse good times

Date: 2026-09-16  
Canonical ID: **M19-351**

Status: **ACTIVE CONDITIONAL CAPACITY CLOSURE / POWER-THINNING NO-GO / PALINSTROPHY RETURN**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

Use the persistent baseline diffuse good-time branch of M17-458:

\[
|G_R|\ge\beta_*|J_R|
\asymp
\beta_*R^2.
\]

On these good times the sign moments satisfy fixed lower bounds and near-perfect cancellation,

\[
K_+\sim K_-\sim O(1),
\qquad
K_--K_+=P_R\ll1
\]

in time-density sense.

M19-345 gives compact residence-weighted coefficient scales, hence each sign has an enstrophy floor

\[
\boxed{E_S\ge e_*>0.}
\]

Consider one sign sector \(S\) whose material-flux fraction obeys a fixed power thinning law

\[
\boxed{\eta_S\lesssim R^{-p}}
\]

for some fixed

\[
p>0.
\]

The goal is to test this branch under a regular transverse capacity hypothesis.

## 2. Sign and complementary flux-weighted amplitudes

At one coherent transverse section \(A_z\), let

\[
\Phi_S=\eta_S\Phi,
\qquad
\Phi_C=\Phi-\Phi_S.
\]

Define the sign-specific and complementary quadratic amplitudes

\[
\boxed{
a_S(z)
:=
\frac{1}{\Phi_S}
\int_{A_z\cap S}\rho^2dA,
}
\]

and

\[
\boxed{
a_C(z)
:=
\frac{1}{\Phi_C}
\int_{A_z\cap C}\rho^2dA.
}
\]

In coherent flux coordinates,

\[
E_S
=
\Phi_S\int_0^{\ell_R}a_S(z)dz,
\]

while

\[
E_C
=
\Phi_C\int_0^{\ell_R}a_C(z)dz.
\]

Assume the parent-length compact alternative

\[
\ell_R\asymp R.
\]

Since \(E_S\ge e_*\), \(\Phi_S\lesssim R^{-p}\), and \(\Phi\sim1\),

\[
\boxed{
\int_0^{\ell_R}a_S(z)dz
\gtrsim
R^p.
}
\]

By bounded total enstrophy,

\[
E_C\le E_*,
\qquad
\Phi_C\sim1,
\]

so

\[
\boxed{
\int_0^{\ell_R}a_C(z)dz
\lesssim1.
}
\]

Therefore for late \(R\),

\[
\int_0^{\ell_R}(a_S-a_C)_+dz
\gtrsim R^p.
\]

## 3. Longitudinal Cauchy lower bound

Since \(\ell_R\lesssim CR\),

\[
\left(
\int_0^{\ell_R}(a_S-a_C)_+dz
\right)^2
\le
\ell_R
\int_0^{\ell_R}(a_S-a_C)_+^2dz.
\]

Hence

\[
\boxed{
\int_0^{\ell_R}(a_S-a_C)_+^2dz
\gtrsim
R^{2p-1}.
}
\]

This lower bound uses only sign-flux thinning, fixed sign enstrophy, bounded complementary enstrophy, and parent-length compactness.

## 4. Conditional transverse condenser inequality

The new geometric input is the following scale-sharp condenser hypothesis.

Assume that on the retained compact transverse charts there is a record-uniform constant \(C_{cap}\) such that for almost every relevant section,

\[
\boxed{
(a_S(z)-a_C(z))_+^2
\le
C_{cap}\log R
\int_{A_z}|\nabla_\perp\rho|^2dA.
}
\]

The logarithm is the natural two-dimensional capacity loss between a flux-small sign phase and the mesoscopic area-\(R\) background. For the extremal \(\eta\sim R^{-1}\) geometry, an area-\(R^{-1}\) core inside an area-\(R\) section has radius ratio of order \(R\), whose annular condenser energy is of order \(1/\log R\).

This inequality is **not** claimed unconditionally. It is the precise regular-capacity hypothesis of the present module.

Failure is retained as one of:

1. transverse neck/shape degeneration;
2. disconnected or topologically separated sign phases;
3. amplitude transition hidden in a capacity-degenerate set;
4. chart/interface breakdown;
5. sign phase not spatially represented on a common coherent section.

## 5. Snapshot palinstrophy lower bound

Integrating the capacity inequality in \(z\) and using Section 3,

\[
\int_{\mathcal T_R}|\nabla_\perp\rho|^2dx
\ge
\frac{c}{\log R}
\int_0^{\ell_R}(a_S-a_C)_+^2dz.
\]

Thus

\[
\boxed{
P_R^{snap}
:=
\int_{\mathcal T_R}|\nabla\Omega|^2dx
\ge
\int|\nabla_\perp\rho|^2dx
\gtrsim
\frac{R^{2p-1}}{\log R}.
}
\]

The inequality \(|\nabla\rho|\le|\nabla\Omega|\) is used in the last step.

For the endpoint \(p=1\),

\[
P_R^{snap}\gtrsim R/\log R.
\]

## 6. Persistent good-time ancestry cost

Suppose the regular-capacity package of Section 4 holds on a fixed positive fraction \(\gamma_*>0\) of the M17-458 good-time set.

Since

\[
|G_R|\gtrsim R^2,
\]

we obtain

\[
\int_{J_R}P_R(t)dt
\gtrsim
\gamma_*R^2
\frac{R^{2p-1}}{\log R}
=
\gamma_*
\frac{R^{2p+1}}{\log R}.
\]

M17-307 applies the ancestry weight \(R^{-1}\). Hence the parent contribution satisfies

\[
\boxed{
\mathcal P_{anc,R}
\gtrsim
\gamma_*
\frac{R^{2p}}{\log R}.
}
\]

For every fixed \(p>0\), this tends to infinity with \(R\), and therefore is incompatible with the finite ancestral palinstrophy ledger.

Thus

\[
\boxed{
\text{fixed-power sign-flux thinning}
+
\text{persistent regular transverse capacity}
\Longrightarrow
\text{ancestral contradiction}.
}
\]

## 7. Time-occupancy threshold

Let \(\gamma_R\) be the fraction of the parent-time record on which the Section 4 capacity package and the fixed-power thinning configuration both hold.

Then the same calculation gives

\[
\boxed{
\mathcal P_{anc,R}
\gtrsim
\gamma_R
\frac{R^{2p}}{\log R}.
}
\]

Finite ancestry therefore requires

\[
\boxed{
\sum_m
\gamma_{R_m}
\frac{R_m^{2p}}{\log R_m}
<\infty.
}
\]

Hence a power-thinning survivor must make the regular-capacity state extraordinarily sparse in parent time, or lose the capacity geometry itself.

## 8. Relation to M19-347

M19-347 prices the nontrivial oriented zero-crossing current when both sign flux-coefficient moments remain order one.

M19-351 addresses the complementary sparse-flux regime in which the sign flux moment can vanish while the enstrophy-weighted sign moment remains order one through high line residence.

The two branches are therefore complementary:

\[
\boxed{
\begin{aligned}
&\text{nontrivial sign flux moment}
\to
\text{oriented zero-current pricing},\\
&\text{thinning sign flux moment}
\to
\text{residence segregation}
\to
\text{transverse-capacity pricing or capacity degeneration}.
\end{aligned}
}
\]

## 9. Relation to M17-453

M17-453 identified palinstrophy as the only currently favorable ancestry currency on the diffuse carrier: raw-H2 and D3 payments are too heavily discounted.

M19-351 provides exactly the missing conditional coercivity mechanism. A sign sector that becomes flux-sparse while keeping fixed enstrophy creates a growing amplitude disparity relative to the complementary diffuse population. If regular two-dimensional capacity converts that disparity into transverse amplitude gradient, the favorable \(R^{-1}\) palinstrophy ledger closes the branch.

## 10. Scope firewall

The Section 4 condenser inequality is not yet certified from the current CE-H hypotheses.

In particular one must not infer it merely from:

- connectedness of the full cross-section;
- existence of two sign populations;
- total area \(\asymp R\);
- coefficient separation alone.

The sign interface is a \(\kappa\)-interface, not a Dirichlet boundary for \(\rho\). A capacity theorem must prove that the sign-resolved amplitude disparity is spatially realized through a regular common transverse chart.

Thus M19-351 is a conditional closure theorem and an exact new gate, not a completed proof.

## 11. Updated sparse-residence branch

For any fixed \(p>0\),

\[
\boxed{
\begin{aligned}
G_{\eta_S\lesssim R^{-p}}
\Longrightarrow{}&
G_{\rm transverse\ capacity\ palinstrophy\ contradiction}\\
&\lor G_{\rm capacity/neck/shape\ degeneration}\\
&\lor G_{\rm common\ section\ representation\ loss}\\
&\lor G_{\rm time\ occupancy\ thinning}\\
&\lor G_{\rm super\text{-}parent\ arclength/line\ folding}\\
&\lor G_{\rm coefficient/enstrophy/genealogy\ loss}.
\end{aligned}
}
\]

The new theorem obligation is

\[
\boxed{
\mathcal T_{cap}^{sign}:
\text{derive the logarithmic transverse condenser inequality from the retained CE-H geometry,}
}
\]

or classify its failure as an already controlled decompactification branch.

## 12. Audit verdict

**PASS AS A CONDITIONAL POWER-THINNING CLOSURE.**

A fixed-power sparse sign population cannot persist on a positive fraction of parent time if its amplitude disparity with the complementary population is connected by regular mesoscopic transverse capacity. The resulting palinstrophy ancestry cost is \(\gtrsim R^{2p}/\log R\).

The hard residue is now geometric and precise: prove the sign-phase condenser inequality, or show that its failure necessarily lands in neck/topology/interface/genealogy decompactification.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
