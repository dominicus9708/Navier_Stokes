# M17-482 — Level-flux variation simplifies exactly to amplitude normal jet plus coefficient Laplacian and removes curvature as an independent payer

**Date:** 2026-09-10  
**Status:** ACTIVE EXACT LEVEL-SET SIMPLIFICATION / ZERO-FLUX JET CLASSIFICATION

## 1. Purpose

M17-481 introduced the weighted relative normal-variation constant controlling
\[
F(s)=\int_{\Sigma_s}\rho^2|\nabla\kappa|\,dS.
\]
Its exact transport derivative contained
\[
\frac{\partial_n g}{g}+\mathcal H_\Sigma,
\qquad
g:=|\nabla\kappa|.
\]

This module simplifies that combination exactly. The curvature contribution is not independent: it combines with the normal derivative of \(|\nabla\kappa|\) into the scalar coefficient Laplacian \(\Delta\kappa\).

No coefficient evolution formula and no reconstruction of \(\mathcal R_{\rm geom}\) are used.

## 2. Level-set geometry identity

Let
\[
n:=\frac{\nabla\kappa}{g},
\qquad
g=|\nabla\kappa|>0.
\]
For a regular level surface,
\[
\mathcal H_\Sigma=\operatorname{div}n.
\]
Compute
\[
\operatorname{div}\left(\frac{\nabla\kappa}{g}\right)
=
\frac{\Delta\kappa}{g}
-\frac{\nabla\kappa\cdot\nabla g}{g^2}.
\]
Since
\[
\nabla\kappa=g n,
\qquad
\nabla\kappa\cdot\nabla g
=g\,\partial_n g,
\]
we obtain
\[
\boxed{
\mathcal H_\Sigma
=
\frac{\Delta\kappa}{g}
-
\frac{\partial_ng}{g}.
}
\]
Therefore
\[
\boxed{
\frac{\partial_ng}{g}+\mathcal H_\Sigma
=
\frac{\Delta\kappa}{g}.
}
\]

## 3. Simplified exact level-flux derivative

M17-480 gave
\[
F'(s)
=
\int_{\Sigma_s}
\left[
2\rho\partial_n\rho
+\rho^2\frac{\partial_ng}{g}
+\rho^2\mathcal H_\Sigma
\right]dS.
\]
Using Section 2,
\[
\boxed{
F'(s)
=
\int_{\Sigma_s}
\left[
2\rho\partial_n\rho
+\rho^2\frac{\Delta\kappa}{g}
\right]dS.
}
\]

Thus the entire regular zero-level flux variation is controlled by only two scalar jet channels:

\[
\boxed{
\text{amplitude normal jet }\partial_n\rho,
\qquad
\text{coefficient Laplacian }\Delta\kappa.
}
\]

Mean curvature is not an independent payer in this transport identity.

## 4. Partition-independent relative condition

The M17-481 weighted hypothesis becomes
\[
\boxed{
\left|
2\rho\partial_n\rho
+\rho^2\frac{\Delta\kappa}{g}
\right|
\le
L_w\rho^2g.
}
\]
Where \(\rho>0\), this is equivalent to
\[
\boxed{
\left|
2\frac{\partial_n\rho}{\rho g}
+
\frac{\Delta\kappa}{g^2}
\right|
\le L_w.
}
\]

Hence a sufficient separated condition is
\[
\boxed{
\left|\frac{\partial_n\rho}{\rho g}\right|\le L_\rho^{rel},
\qquad
\left|\frac{\Delta\kappa}{g^2}\right|\le L_\kappa^{rel},
}
\]
which gives
\[
L_w\le2L_\rho^{rel}+L_\kappa^{rel}.
\]

At nodal points \(\rho=0\), the undivided weighted inequality is the canonical formulation; division by \(\rho\) is not permitted.

## 5. Consequence for zero-current persistence

If a common regular tube satisfies
\[
0<g_*\le g\le G_*<\infty
\]
and the weighted bound in Section 4 with finite \(L_w\), M17-481 gives
\[
\boxed{
 e^{-L_w|s|}J_0
\le F(s)\le
 e^{L_w|s|}J_0.
}
\]
Consequently
\[
\boxed{
H_{0,\delta}
\ge
\frac23G_*^{-2}e^{-L_w\delta}\delta^3J_0.
}
\]

Thus zero-current persistence requires no separate curvature estimate once the coefficient Laplacian and amplitude normal jet are controlled.

## 6. Refined failure split

The M17-481 zero-flux failure tree can therefore be compressed to
\[
\boxed{
\begin{aligned}
G_{\rm zero\text{-}flux\ variation\ decompactification}
\Longrightarrow{}&
G_{\rm amplitude\ normal\ relative\text{-}jet}\\
&\lor G_{\Delta\kappa/|\nabla\kappa|^2\text{-}decompactification}\\
&\lor G_{|\nabla\kappa|\downarrow0\text{ / critical-level}}\\
&\lor G_{|\nabla\kappa|\uparrow\infty\text{ / coefficient-gradient}}\\
&\lor G_{\rm tube/reach/interface/domain\ loss}.
\end{aligned}
}
\]

Curvature decompactification may still destroy the existence of a common tubular chart, but **within an existing regular tube it is not an independent term in \(F'(s)\)**.

## 7. Relation to coefficient-jet hierarchy

The coefficient contribution is
\[
\frac{\Delta\kappa}{|\nabla\kappa|^2}.
\]
Therefore bounded absolute Hessian alone is not the invariant condition near critical levels: if \(|\nabla\kappa|\to0\), the normalized ratio can diverge even with bounded \(\Delta\kappa\).

This cleanly separates:

- regular finite-jet tubes with \(|\nabla\kappa|\ge g_*>0\);
- critical-level degeneration;
- genuine second-derivative coefficient growth.

The classification is geometric/spatial and does not require the unverified termwise formula for \(\mathcal R_{\rm geom}\). M17-463 remains fully intact.

## 8. Relation to DSD audit

DSD contributes only the channel-equivalence audit: two apparently separate geometric terms in the prior branch tree are exactly the same coefficient-Laplacian channel after the level-set identity is applied.

No DSD axiom enters the PDE estimate.

## 9. Next target

The zero-current geometry is now reduced to two genuine weighted jets plus tube existence. The next question is whether the amplitude-normal term
\[
2\rho\partial_n\rho
\]
can be controlled directly by already certified vorticity derivative ledgers in a way that is partition-safe, or whether its relative version necessarily leaves a nodal/amplitude-ratio decompactification branch.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
