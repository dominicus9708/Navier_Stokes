# M18-026 — Normalized collar-gradient concentration requires first-jet packet growth or second-jet geometry or weighted-mass depletion

**Date:** 2026-09-11  
**Status:** ACTIVE DSD ANALYSIS / ANISOTROPIC PACKET THICKENING / GRADIENT-CONCENTRATION CLASSIFICATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-023 isolated the scale-invariant collar-gradient parameter

\[
\Gamma_{\mathcal K}
:=
\operatorname*{ess\,sup}_{\mathcal K}
\frac{|\nabla\kappa|^2}{\delta_0^3}.
\]

The cutoff-current branch is absorbed whenever \(\Gamma_{\mathcal K}\) stays bounded. The remaining question is what

\[
\Gamma_{\mathcal K}\to\infty
\]

actually means.

A pointwise large coefficient gradient is not automatically an integrated weighted payer. This module makes the missing thickness explicit.

The main result is that a high-gradient collar point has a natural anisotropic geometry:

- transverse/parabolic scale \(L_0=\delta_0^{-1/2}\);
- normal coefficient-crossing scale \(\ell_n=\delta_0/G\), where \(G=|\nabla\kappa|\).

Their ratio is

\[
\frac{\ell_n}{L_0}
=
\Gamma^{-1/2}.
\]

If the gradient remains comparable on such a packet and the packet retains weighted vorticity mass, then the weighted first-coefficient-jet charge grows like \(\sqrt\Gamma\). If not, the failure is necessarily assigned to second-coefficient-jet/level-geometry concentration, weighted-mass depletion, or tube/domain loss.

## 2. Intrinsic scales at a high-gradient point

Fix a point \(x_0\) in a fixed fractional interior subcollar and write

\[
G:=|\nabla\kappa(x_0)|,
\qquad
\Gamma:=\frac{G^2}{\delta_0^3}.
\]

Define

\[
\boxed{
L_0:=\delta_0^{-1/2},
\qquad
\ell_n:=\frac{\delta_0}{G}.
}
\]

Under Navier--Stokes record scaling,

\[
\delta_{0,R}=R^2\delta_0,
\qquad
G_R=R^3G,
\]

so both \(L_0\) and \(\ell_n\) scale as physical lengths, \(R^{-1}\).

Moreover

\[
\boxed{
\ell_n
=L_0\Gamma^{-1/2}.
}
\]

Thus \(\Gamma\gg1\) means that coefficient variation is much thinner in the normal direction than the natural transverse/parabolic spatial scale.

## 3. Anisotropic packet

Let \(n_0=\nabla\kappa(x_0)/G\). Choose fixed small constants \(c_t,c_n>0\), independent of the record, and define an anisotropic cylinder

\[
\mathcal C(x_0)
:=
\left\{
 x_0+z_t+z_n n_0:
 |z_t|<c_tL_0,
 |z_n|<c_n\ell_n
\right\},
\]

where \(z_t\perp n_0\).

Its volume satisfies

\[
\boxed{
|\mathcal C|
\asymp
L_0^2\ell_n
=
\delta_0^{-3/2}\Gamma^{-1/2}.
}
\]

This packet is the correct geometry for a steep coefficient layer: parabolic-size transverse footprint and gradient-determined normal thickness.

## 4. Scale-invariant second-jet shape parameter

Define

\[
\boxed{
\mathfrak H_2(\mathcal C)
:=
\delta_0^{-2}
\operatorname*{ess\,sup}_{\mathcal C}|D^2\kappa|.
}
\]

This is scale invariant because \(D^2\kappa\) and \(\delta_0^2\) both scale as \(R^4\).

To preserve a gradient of order \(G\) across the transverse radius \(L_0\), it is sufficient that

\[
\operatorname*{ess\,sup}_{\mathcal C}|D^2\kappa|
\le
c_H\frac{G}{L_0}
=
c_H\delta_0^2\sqrt\Gamma,
\]

i.e.

\[
\boxed{
\mathfrak H_2(\mathcal C)
\le c_H\sqrt\Gamma.
}
\]

With \(c_H,c_t,c_n\) chosen compatibly and with a fixed coefficient margin to the collar boundary, the mean-value theorem gives

\[
\boxed{
|\nabla\kappa(x)|\ge\frac G2
\qquad(x\in\mathcal C).
}
\]

The normal displacement changes \(\kappa\) by only \(O(\delta_0)\), so the packet remains inside a slightly enlarged fixed fractional collar.

If this Hessian condition fails, then the coefficient second jet itself is decompactifying at least at the scale

\[
\mathfrak H_2\gtrsim\sqrt\Gamma.
\]

## 5. Weighted packet-mass parameter

The coefficient-gradient ledger is weighted by \(\rho^2\). Therefore an unweighted high-gradient packet cannot be charged without tracking the vorticity mass inside it.

Define

\[
M_\rho(\mathcal C)
:=
\int_{\mathcal C}\rho^2dx.
\]

Since \(M_\rho\) scales as \(R\), define the representation-safe packet-mass parameter

\[
\boxed{
\mathfrak M_\rho
:=
\sqrt\Gamma\,\delta_0^{-1/2}M_\rho(\mathcal C).
}
\]

Indeed \(\sqrt\Gamma\) is invariant and \(\delta_0^{-1/2}M_\rho\) is invariant.

A uniform lower bound

\[
\mathfrak M_\rho\ge m_*>0
\]

is the integrated version of saying that the packet does not become vorticity-empty as it becomes thin.

## 6. First-coefficient-jet packet lower bound

Define the packet first-jet charge

\[
B_{\mathcal C}
:=
\int_{\mathcal C}ho^2|\nabla\kappa|^2dx.
\]

Under the gradient-persistence condition of Section 4,

\[
B_{\mathcal C}
\ge
\frac{G^2}{4}M_\rho(\mathcal C).
\]

Using

\[
G^2=\delta_0^3\Gamma
\]

and

\[
M_\rho
=\mathfrak M_\rho\,\delta_0^{1/2}\Gamma^{-1/2},
\]

we obtain

\[
\boxed{
B_{\mathcal C}
\ge
\frac14
\mathfrak M_\rho\,
\delta_0^{7/2}\sqrt\Gamma.
}
\]

Thus if \(\delta_0\) stays in a compact normalized bin and \(\mathfrak M_\rho\ge m_*>0\), then

\[
\boxed{
\Gamma\to\infty
\quad\Longrightarrow\quad
B_{\mathcal C}\to\infty
}
\]

at least like \(\sqrt\Gamma\), provided the second-jet shape remains below the threshold of Section 4.

The scaling is correct: \(\delta_0^{7/2}\) scales as \(R^7\), exactly the snapshot scaling of the weighted first-coefficient-jet charge.

## 7. Why isotropic thickening is the wrong model

If one instead used a ball of radius \(\ell_n\) in all three directions, its volume would be

\[
\ell_n^3
\asymp
\delta_0^{-3/2}\Gamma^{-3/2}.
\]

Even with natural amplitude, the resulting first-jet charge can decrease as \(\Gamma\) grows.

Therefore

\[
\boxed{
\text{high gradient}\not\Rightarrow\text{large integrated payer}
}
\]

without transverse-support information.

The anisotropic packet is not cosmetic: it identifies exactly which transverse collapse allows a large normal gradient to evade the weighted ledger.

## 8. Exact failure classification

Suppose \(\Gamma\to\infty\) along a retained fixed fractional collar. Then at least one of the following occurs.

### A. First-jet packet growth

The packet remains geometrically valid, the second-jet shape satisfies

\[
\mathfrak H_2\lesssim\sqrt\Gamma,
\]

and

\[
\mathfrak M_\rho\gtrsim1.
\]

Then

\[
\boxed{
B_{\mathcal C}\gtrsim
\delta_0^{7/2}\sqrt\Gamma.
}
\]

### B. Second-coefficient-jet concentration

\[
\boxed{
\frac{\mathfrak H_2}{\sqrt\Gamma}
\not\lesssim1.
}
\]

Then the gradient peak is spatially supported only by a comparably strong Hessian/second-jet concentration.

### C. Weighted-mass depletion

\[
\boxed{
\mathfrak M_\rho\to0.
}
\]

Then the coefficient geometry may remain steep, but the vorticity weight seen by the certified first-jet ledger disappears from its intrinsic anisotropic packet.

### D. Transverse/tube/domain loss

The natural transverse disk of radius \(c_t\delta_0^{-1/2}\), the normal collar thickness, or the exact-CE-H domain does not survive. This is a geometric/domain decompactification rather than an analytic first-jet payer.

Hence

\[
\boxed{
\begin{aligned}
G_{\Gamma_{\mathcal K}\to\infty}
\Longrightarrow{}&
G_{\rm first\text{-}jet\ packet\ growth}\\
&\lor G_{\rm second\ coefficient\ jet}\\
&\lor G_{\rm weighted\ packet\ mass\ depletion}\\
&\lor G_{\rm transverse/tube/domain\ loss}.
\end{aligned}
}
\]

## 9. Trace versus trace-free second-jet audit

The M18-018 coefficient-shape parameter used \(\Delta\kappa\), whereas Section 4 uses the full Hessian \(D^2\kappa\).

Decompose

\[
D^2\kappa
=
\frac13(\Delta\kappa)I
+(D^2\kappa)^\circ.
\]

Therefore full-Hessian concentration implies

\[
\boxed{
G_{D^2\kappa\text{-high}}
\Longrightarrow
G_{\Delta\kappa\text{-high}}
\lor
G_{\rm trace\text{-}free\ Hessian\text{-}high}.
}
\]

The first branch returns directly to the M18-018--019 second-coefficient-jet analysis.

The trace-free branch is geometric. On a regular level set, tangential components satisfy schematically

\[
D^2\kappa(\tau,\tau)
=g\,\mathrm{II}(\tau,\tau),
\]

while mixed normal-tangential components measure tangential variation of \(g\). Thus large trace-free Hessian with bounded Laplacian is a level-shape/normal-field decompactification and belongs with curvature/reach/tube geometry rather than being silently absorbed into the Laplacian branch.

## 10. Relation to M18-017--019 level-flux machinery

M18-026 is a local packet theorem. It does not require level flux to remain large over a macroscopic coefficient interval.

If, in addition, a weighted surface-mass/level-flux floor persists across a fixed fraction of coefficient levels, then M18-017--019 strengthen the conclusion from one packet to a bulk collar first-jet/raw-H2/palinstrophy payment.

If that level-flux persistence fails, the prior dichotomies already send the failure to palinstrophy, coefficient-shape growth, critical-level degeneration, or tube/interface loss.

Thus the new packet classification is compatible with, rather than independent of, the earlier zero-level flux tree.

## 11. Snapshot-to-spacetime firewall

The lower bound

\[
B_{\mathcal C}\gtrsim\delta_0^{7/2}\sqrt\Gamma
\]

is a snapshot statement.

The certified ancestral first-coefficient-jet ledger is spacetime and carries \(R^{-5}\). Therefore one must not infer an ancestry contradiction from a single large packet.

A further temporal-thickness theorem for the packet charge, or a positive active-time measure as in M18-020--021, is still required.

This is the same DSD firewall already identified for endpoint raw-H2 and palinstrophy spikes.

## 12. DSD audit verdict

### Certified

1. \(\Gamma_{\mathcal K}\) has a natural anisotropic packet geometry.
2. High normalized gradient with bounded relative second-jet shape and nonvanishing weighted packet mass forces first-jet snapshot growth like \(\sqrt\Gamma\).
3. Failure of spatial thickening is precisely assigned to second-jet concentration, weighted-mass depletion, or transverse/tube/domain loss.
4. Full-Hessian concentration cannot be identified with Laplacian concentration without a trace-free geometry audit.
5. A snapshot first-jet packet is not yet a spacetime ancestry payer.

### Not certified

1. A record-uniform lower bound for \(\mathfrak M_\rho\).
2. Temporal persistence of the anisotropic packet.
3. A finite D4 ledger for full-Hessian coefficient concentration.
4. Elimination of trace-free level-geometry decompactification.
5. Global 3D Navier--Stokes regularity.

## 13. Next target

The most informative next step is to audit

\[
\boxed{
\mathfrak M_\rho
=
\sqrt\Gamma\,\delta_0^{-1/2}
\int_{\mathcal C}\rho^2dx
\to0.
}
\]

M18-027 should determine whether this weighted-mass depletion can coexist with the retained robust level-flux witness and exact CE-H geometry, or whether it necessarily forces transverse-area concentration, nodal migration, or a palinstrophy/raw-H2 payment.