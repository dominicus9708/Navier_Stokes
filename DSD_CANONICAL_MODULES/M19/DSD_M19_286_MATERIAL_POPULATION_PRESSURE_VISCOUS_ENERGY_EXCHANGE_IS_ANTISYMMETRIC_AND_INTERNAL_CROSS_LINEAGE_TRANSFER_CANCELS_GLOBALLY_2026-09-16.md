# M19-286 — Material-population pressure/viscous energy exchange is antisymmetric; internal cross-lineage transfer cancels globally

**Date:** 2026-09-16  
**Status:** CALCULATION / FINITE ENERGY-EXCHANGE NETWORK / CROSS-POPULATION NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-283 reduces carrier localization to a same-population branch, a cross-population branch, or an interface/background/representation defect.

M19-284--285 derive the exact material kinetic-energy law and identify the only signed material-boundary channel as pressure plus viscous energy exchange.

This module audits the cross-population branch on a compatible finite material partition.

## 2. Compatible finite material partition

Let

\[
\Omega_{core}(\theta)
=
\bigcup_{i=1}^{N}P_i(\theta)
\]

be a finite partition into material populations with disjoint interiors and sufficiently regular shared interfaces

\[
S_{ij}=\partial P_i\cap\partial P_j.
\]

All populations are transported by

\[
B=U+\frac12y.
\]

Assume the velocity, pressure, and kinetic-energy gradient have the regular traces required on internal interfaces. Failure of this compatible realization is recorded as

\[
\boxed{G_{energy\ interface/representation}.}
\]

## 3. Internal pressure/viscous energy current

Let

\[
e=\frac12|U|^2.
\]

For the oriented interface from \(P_i\) to \(P_j\), define

\[
\boxed{
Q_{ij}
:=
-\int_{S_{ij}}
(PU-\nu\nabla e)\cdot n_i\,dS,
}
\]

where \(n_i\) is the outward normal of \(P_i\). The sign convention is chosen so that positive \(Q_{ij}\) is energy imported into \(P_i\) from the interface term in its material energy law.

On the same interface,

\[
n_j=-n_i.
\]

Hence

\[
\boxed{Q_{ji}=-Q_{ij}.}
\]

The pressure and viscous exchange are therefore an exactly antisymmetric edge current.

## 4. Population energy equations

Let

\[
E_i=\int_{P_i}e\,dy,
\qquad
D_i=\int_{P_i}|\nabla U|^2dy.
\]

M19-284 gives

\[
\boxed{
E_i'
=
\frac12E_i
-\nu D_i
+\sum_{j\ne i}Q_{ij}
+Q_{i,ext},
}
\]

where \(Q_{i,ext}\) denotes exchange across the outer boundary of the retained core region.

This is a finite source-sink-exchange network.

## 5. Exact internal cancellation

Summing over all populations,

\[
\sum_i\sum_{j\ne i}Q_{ij}=0
\]

by antisymmetry. Therefore

\[
\boxed{
E_{core}'
=
\frac12E_{core}
-\nu D_{core}
+Q_{ext},
}
\]

with

\[
E_{core}:=\sum_iE_i,
\qquad
D_{core}:=\sum_iD_i,
\qquad
Q_{ext}:=\sum_iQ_{i,ext}.
\]

Thus internal cross-lineage energy transfer is redistribution, not a net energy source.

## 6. Recurrent closed-network mean

If the retained core network is recurrent, bounded/integrable, and closed to external material energy exchange,

\[
Q_{ext}=0,
\]

then

\[
\langle E_{core}'\rangle=0.
\]

Consequently

\[
\boxed{
\nu\langle D_{core}\rangle
=
\frac12\langle E_{core}\rangle.
}
\]

This is a perfectly consistent recurrent balance. It is not a contradiction.

If

\[
Q_{ext}\ne0,
\]

then the correct branch is

\[
\boxed{G_{external/background\ energy\ exchange}.}
\]

## 7. Graph formulation

Choose one orientation for each internal interface and let \(B_G\) be the graph incidence matrix. Let \(q_E\) be the vector of oriented energy currents.

Then

\[
\boxed{
E'
=
\frac12E
-\nu D
+B_Gq_E
+Q_{ext}.
}
\]

As before,

\[
\mathbf1^TB_G=0.
\]

Any cycle-space energy current

\[
q_C\in\ker B_G
\]

is invisible to the total energy equation. Such a cycle can redistribute energy indefinitely without creating net energy.

Therefore

\[
\boxed{
\text{cross-population recurrent energy circulation}
\not\Rightarrow
\text{global contradiction}.
}
\]

## 8. Consequence for M19-283 carrier trichotomy

Suppose the production-paying population is \(P_{\alpha_*}\) and the selected positive-mean energy-current population is \(P_{i_E}\ne P_{\alpha_*}\).

The difference of labels alone does not create a new payer. The later energy event may be supported by conservative pressure/viscous transfer through the finite material network.

Thus the cross-population branch reduces to

\[
\boxed{
G_{cross\text{-}population}
\Longrightarrow
G_{conservative\ internal\ energy\ exchange}
\lor
G_{external/background\ energy\ exchange}
\lor
G_{energy\ interface/representation}.
}
\]

The first branch is a redistribution mechanism, not closure.

## 9. Relation to the M18 diffusion-current graph

M18-089 found the antisymmetric amplitude-diffusion edge current

\[
e_{ij}^{(p)}=-e_{ji}^{(p)}.
\]

M19-286 shows the analogous statement for kinetic-energy pressure/viscous exchange:

\[
\boxed{
Q_{ij}=-Q_{ji}.
}
\]

The two graphs are not identical observables, but they share the same structural firewall:

\[
\boxed{
\text{internal conservative current redistributes a finite population budget but does not create its total.}
}
\]

## 10. Dynamic-core reduction after M19-282--286

The unconditional finite-lag energy route has now exhausted the following possibilities:

1. global signed-event mean \(\to\) ordinary wedge dissipation (M19-282);
2. carrier localization \(\to\) one persistent population or explicit background/interface defect (M19-283);
3. same-population lag energy \(\to\) similarity baseline + pressure/viscous exchange + bulk dissipation (M19-284);
4. Eulerian/material mismatch \(\to\) explicit geometric sweep (M19-285);
5. cross-population exchange \(\to\) antisymmetric conservative network current (M19-286).

Therefore none of these **unconditional mean balances** supplies the missing nonreplenishable signed payer by itself.

## 11. New precise target

The remaining useful information in M19-270 is not unconditional mean positivity but the **positive-measure fixed-lag correlation with the production-linked event**.

The next theorem must therefore be event-conditioned. Schematically, for a smooth production-event marker \(m_{pd}\ge0\), test whether

\[
\boxed{
\left\langle
m_{pd}(Y)\,\Gamma_{i_E}(\sigma_hY)
\right\rangle>0
}
\]

forces a signed covariance in pressure/interface/dissipation channels that cannot be represented by an internal conservative exchange or a bounded coboundary.

This is stronger than another global energy identity and is the remaining high-value dynamic-core calculation.

---

\[
\boxed{\text{M19-286 COMPLETE; CROSS-LINEAGE ENERGY TRANSFER IS AN INTERNAL CONSERVATIVE GRAPH CURRENT UNLESS EXTERNAL/BACKGROUND OR REPRESENTATION DEFECTS OCCUR.}}
\]
