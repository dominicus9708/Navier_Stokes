# M17-481 — Weighted level-flux Gronwall removes artificial patch fragmentation and makes zero-current to raw-H2 partition-independent

**Date:** 2026-09-10  
**Status:** ACTIVE PARTITION-INDEPENDENT ZERO-CURRENT THEOREM / FRAGMENTATION AUDIT

## 1. Purpose

M17-480 proved level-flux persistence on a selected regular zero-level patch under absolute finite-jet/tube bounds. It left a possible fragmentation issue if the total zero current is distributed among many patches.

This module identifies a stronger **weighted relative normal-variation condition** under which the full transported level flux satisfies a Gronwall inequality. The conclusion is independent of the number of connected components or chart subdivisions.

Thus arbitrary patch fragmentation cannot create or destroy the zero-current payer. Only genuine failure of the weighted normal compactness, reach/tube geometry, or coefficient-gradient bounds remains.

## 2. Level-set transport identity

Use the notation of M17-480:
\[
g:=|\nabla\kappa|,
\qquad
n:=\frac{\nabla\kappa}{g},
\qquad
V:=\frac{n}{g}.
\]
The flow of \(V\) maps regular level surfaces \(\Sigma_0\subset\{\kappa=0\}\) to \(\Sigma_s\subset\{\kappa=s\}\).

Define
\[
F(s):=\int_{\Sigma_s}\rho^2g\,dS.
\]
M17-480 gives the exact derivative
\[
\boxed{
F'(s)
=
\int_{\Sigma_s}
\left[
2\rho\partial_n\rho
+\rho^2\frac{\partial_ng}{g}
+\rho^2\mathcal H_\Sigma
\right]dS.
}
\]

## 3. Weighted relative normal-variation hypothesis

Assume on the regular transported tube that there is a record-uniform constant \(L_w<\infty\) such that
\[
\boxed{
\left|
2\rho\partial_n\rho
+\rho^2\frac{\partial_ng}{g}
+\rho^2\mathcal H_\Sigma
\right|
\le
L_w\rho^2g.
}
\]

This formulation avoids dividing by \(\rho\) at nodal points. Where \(\rho>0\), it is equivalent to the bound
\[
\left|
\frac{2\partial_n\rho}{\rho g}
+
\frac{\partial_ng}{g^2}
+
\frac{\mathcal H_\Sigma}{g}
\right|
\le L_w.
\]

The hypothesis is stronger than mere bounded absolute jets near amplitude zeros, but it is exactly the partition-independent quantity controlling the weighted level flux.

## 4. Gronwall estimate

Section 3 inserted into the exact transport identity gives
\[
|F'(s)|
\le
L_w\int_{\Sigma_s}\rho^2g\,dS
=L_wF(s).
\]
Thus
\[
\boxed{|F'(s)|\le L_wF(s).}
\]
By Gronwall, for every \(|s|\) inside the common regular tube,
\[
\boxed{
 e^{-L_w|s|}F(0)
\le
F(s)
\le
 e^{L_w|s|}F(0).
}
\]

In particular, for any fixed tube width \(\delta>0\),
\[
\boxed{
F(s)\ge e^{-L_w\delta}J_0
\qquad(|s|\le\delta),
}
\]
where \(J_0=F(0)\).

No connected-component count, patch area, or arbitrary chart number appears.

## 5. Direct raw-H2 corridor lower bound

Let
\[
H_{0,\delta}
:=
\int_{\{|\kappa|<\delta\}}
\kappa^2\rho^2dx.
\]
By the coarea formula,
\[
H_{0,\delta}
=
\int_{-\delta}^{\delta}
s^2
\left(
\int_{\Sigma_s}\frac{\rho^2}{g}dS
\right)ds.
\]
Assume also the normalized coefficient-gradient ceiling
\[
 g\le G_*.
\]
Then
\[
\frac1g\ge\frac g{G_*^2},
\]
so
\[
\int_{\Sigma_s}\frac{\rho^2}{g}dS
\ge
G_*^{-2}F(s).
\]
Using Section 4,
\[
\begin{aligned}
H_{0,\delta}
&\ge
G_*^{-2}
\int_{-\delta}^{\delta}s^2F(s)ds\\
&\ge
G_*^{-2}e^{-L_w\delta}J_0
\int_{-\delta}^{\delta}s^2ds.
\end{aligned}
\]
Therefore
\[
\boxed{
H_{0,\delta}
\ge
\frac{2}{3}
G_*^{-2}e^{-L_w\delta}\delta^3J_0.
}
\]

This is a partition-independent version of the M17-470 zero-current-to-raw-H2 corridor estimate.

## 6. Fragmentation audit

Suppose the zero surface is decomposed into measurable transported pieces
\[
\Sigma_s=\bigsqcup_j\Sigma_{s,j}
\]
up to null boundaries. Then
\[
F(s)=\sum_jF_j(s),
\qquad
J_0=\sum_jJ_{0,j}.
\]
The lower bound in Section 5 is written for the total geometric measure and is unchanged by subdividing the same regular tube into more charts.

Therefore
\[
\boxed{
\text{arbitrary chart/patch fragmentation is not a resource and cannot evade the zero-current bulk payment.}
}
\]
This is analogous in spirit to the partition firewall of M17-439 and the disjoint coefficient-bin ownership of M17-381.

## 7. Genuine fragmentation exits

The conclusion can fail only if fragmentation is accompanied by a genuine loss of the hypotheses. The admissible split is
\[
\boxed{
\begin{aligned}
G_{\rm zero\text{-}current\ fragmentation}
\Longrightarrow{}&
G_{L_w\text{-}decompactification}\\
&\lor G_{|\nabla\kappa|\downarrow0\text{ / critical-level}}\\
&\lor G_{|\nabla\kappa|\uparrow\infty\text{ / coefficient-jet}}\\
&\lor G_{\rm tube/reach/self\text{-}clustering\ loss}\\
&\lor G_{\rm amplitude\ nodal/relative\text{-}jet\ degeneration}\\
&\lor G_{\rm interface/domain/genealogy\ loss}.
\end{aligned}
}
\]

A growing number of genuine connected components is relevant only insofar as it forces one of these invariant geometric/weighted quantities to decompactify. Component count by itself is not a canonical payer.

## 8. Relation to M17-470 and M17-480

M17-470 required a level-flux persistence input. M17-480 showed it follows locally from absolute compactness plus a positive patch floor. M17-481 provides the stronger global/partition-safe formulation:
\[
\boxed{
J_0>0
+
\text{uniform weighted normal variation}
+
\text{uniform regular tube}
\Longrightarrow
H_{0,\delta}\gtrsim J_0.
}
\]

Thus the old `zero-tube/level-flux collapse` label should be replaced by explicit weighted-relative-jet, critical-level, reach, nodal, or interface exits.

## 9. Ancestry firewall remains

Even when
\[
H_{0,\delta}\gtrsim J_0
\]
with record-uniform constants, a fixed normalized zero-current payment remains a fixed normalized raw-H2 payment. By M17-405 its parent contribution carries \(R_m^{-3}\), so geometric records remain summable unless M17-473's cubic/non-summable allocation threshold is met.

## 10. Next target

The local common-mode geometry has now been compressed substantially. The remaining new quantity in Section 7 is the weighted relative normal-variation constant \(L_w\). The next audit should expand \(L_w\) only into already certified invariant jets—without guessing \(\mathcal R_{\rm geom}\)—and determine whether its decompactification is already contained in the existing amplitude-gradient, coefficient-Hessian/curvature, critical-level, and reach branches.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
