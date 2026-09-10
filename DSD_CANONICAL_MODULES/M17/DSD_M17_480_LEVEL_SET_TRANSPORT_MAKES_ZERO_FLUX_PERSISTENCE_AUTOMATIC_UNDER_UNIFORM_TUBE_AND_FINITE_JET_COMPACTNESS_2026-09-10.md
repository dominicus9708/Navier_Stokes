# M17-480 — Level-set transport makes zero-flux persistence automatic under uniform tube and finite-jet compactness

**Date:** 2026-09-10  
**Status:** ACTIVE ZERO-TUBE COMPACTNESS THEOREM / M17-470 ASSUMPTION REDUCTION

## 1. Purpose

M17-470 used a near-zero level-flux persistence hypothesis
\[
F(s)\gtrsim F(0),
\qquad
F(s):=\int_{\{\kappa=s\}}\rho^2|\nabla\kappa|\,dS,
\]
to thicken the regular zero-current
\[
J_0=F(0)
\]
into a bulk raw-H2 slab.

This module shows that, on a selected regular zero-level patch, that persistence is **automatic** under an explicit record-uniform tube/finite-jet compactness package. Thus `zero-level flux collapse` is not an additional compact branch; it is a witness of tube/jet/amplitude/geometric decompactification or loss of the zero-current floor.

## 2. Local transported zero-level patch

Let \(\Sigma_0\) be a smooth compact patch of the regular level set
\[
\{\kappa=0\}
\]
with possibly nonempty boundary.

Assume a tubular neighborhood in which
\[
0<g_*\le g:=|\nabla\kappa|\le G_*.
\]
Define the level-set transport vector field
\[
\boxed{
V:=\frac{\nabla\kappa}{|\nabla\kappa|^2}
=\frac{n}{g},
}
\]
where
\[
n:=\frac{\nabla\kappa}{|\nabla\kappa|}.
\]
Then
\[
V\cdot\nabla\kappa=1.
\]
Hence the flow of \(V\) maps \(\Sigma_0\) to transported patches
\[
\Sigma_s\subset\{\kappa=s\}
\]
for \(|s|\) smaller than the available tube width.

If \(\Sigma_0\) has boundary, the boundary is transported by the same flow; no artificial fixed-chart boundary flux is introduced.

## 3. Exact derivative of the weighted level flux

Define the transported-patch flux
\[
\boxed{
F_\Sigma(s)
:=\int_{\Sigma_s}\rho^2g\,dS.
}
\]
The surface transport formula gives, for any scalar \(f\),
\[
\frac d{ds}\int_{\Sigma_s}f\,dS
=
\int_{\Sigma_s}
\left(V\cdot\nabla f+f\,\operatorname{div}_{\Sigma_s}V\right)dS.
\]
Since \(V=n/g\),
\[
\operatorname{div}_{\Sigma_s}V
=\frac{1}{g}\operatorname{div}_{\Sigma_s}n.
\]
Let
\[
\mathcal H_\Sigma:=\operatorname{div}_{\Sigma_s}n
\]
be the signed mean-curvature trace of the level surface. With \(f=\rho^2g\),
\[
V\cdot\nabla f
=\frac1g\partial_n(\rho^2g)
=2\rho\partial_n\rho
+\rho^2\frac{\partial_ng}{g}.
\]
Also
\[
f\operatorname{div}_{\Sigma_s}V
=\rho^2\mathcal H_\Sigma.
\]
Therefore
\[
\boxed{
F_\Sigma'(s)
=
\int_{\Sigma_s}
\left[
2\rho\partial_n\rho
+\rho^2\frac{\partial_ng}{g}
+\rho^2\mathcal H_\Sigma
\right]dS.
}
\]

This is the exact local level-flux variation formula needed for the audit.

## 4. Uniform finite-jet/tube bound

Assume throughout the transported tube
\[
\rho\le M_\rho,
\qquad
|\partial_n\rho|\le L_\rho,
\]
\[
|\partial_ng|\le L_g,
\qquad
|\mathcal H_\Sigma|\le K_\Sigma,
\]
and
\[
|\Sigma_s|\le A_\Sigma.
\]
Together with \(g\ge g_*\), Section 3 gives
\[
\begin{aligned}
|F_\Sigma'(s)|
&\le
\int_{\Sigma_s}
\left[
2M_\rho L_\rho
+M_\rho^2\frac{L_g}{g_*}
+M_\rho^2K_\Sigma
\right]dS\\
&\le
A_\Sigma
\left[
2M_\rho L_\rho
+M_\rho^2\left(\frac{L_g}{g_*}+K_\Sigma\right)
\right].
\end{aligned}
\]
Define
\[
\boxed{
L_F
:=A_\Sigma
\left[
2M_\rho L_\rho
+M_\rho^2\left(\frac{L_g}{g_*}+K_\Sigma\right)
\right].
}
\]
Then
\[
\boxed{|F_\Sigma'(s)|\le L_F.}
\]

## 5. Uniform persistence from a positive zero-current floor

Assume the selected patch carries
\[
\boxed{
F_\Sigma(0)\ge j_*>0.
}
\]
Let the geometric tube width be at least \(\delta_{\rm tube}>0\). Set
\[
\boxed{
\delta_*
:=
\min\left\{
\delta_{\rm tube},
\frac{j_*}{2L_F}
\right\},
}
\]
with the convention \(j_*/(2L_F)=\infty\) if \(L_F=0\).

Then for \(|s|\le\delta_*\),
\[
F_\Sigma(s)
\ge
F_\Sigma(0)-L_F|s|
\ge
F_\Sigma(0)-\frac{j_*}{2}.
\]
Since \(F_\Sigma(0)\ge j_*\),
\[
F_\Sigma(0)-\frac{j_*}{2}
\ge
\frac12F_\Sigma(0).
\]
Hence
\[
\boxed{
F_\Sigma(s)
\ge
\frac12F_\Sigma(0)
\qquad(|s|\le\delta_*).
}
\]

Thus the level-flux persistence needed by M17-470 is automatic on a uniformly compact regular tube carrying a fixed positive zero-current patch.

## 6. Consequence for M17-470

M17-470's coarea identity on the transported slab gives
\[
\int_{\{|\kappa|<\delta_*\}}
\rho^2|\nabla\kappa|^2dx
=
\int_{-\delta_*}^{\delta_*}F(s)ds.
\]
Using the local patch alone,
\[
\int_{\text{transported patch slab}}
\rho^2|\nabla\kappa|^2dx
\ge
\int_{-\delta_*}^{\delta_*}F_\Sigma(s)ds
\ge
\delta_*F_\Sigma(0).
\]
Together with the coefficient-gradient ceiling used in M17-470, this recovers a fixed near-zero bulk raw-H2 payment.

Therefore
\[
\boxed{
G_{J_0}^{\rm compact\ regular\ patch}
\Longrightarrow
G_{\rm raw\text{-}H^2}.
}
\]

## 7. Correct failure classification

Suppose a fixed positive zero-current contribution exists but uniform level-flux persistence fails. Then at least one input to Sections 2--5 must fail. Thus
\[
\boxed{
\begin{aligned}
G_{\rm zero\text{-}level\ flux\ collapse}
\Longrightarrow{}&
G_{|\nabla\kappa|\downarrow0\text{ / critical-level}}\\
&\lor G_{\nabla^2\kappa\text{ / curvature\ decompactification}}\\
&\lor G_{\rho\text{ or }\nabla\rho\text{ decompactification}}\\
&\lor G_{\rm surface\ area/reach/chart\ decompactification}\\
&\lor G_{J_0\text{-}patch\ floor\ collapse}\\
&\lor G_{\rm tube/domain/interface\ loss}.
\end{aligned}
}
\]

Thus `level-flux collapse` is not an independent compact terminal branch.

## 8. Patch selection firewall

The theorem is local. If the total zero current
\[
J_0=\int_{\{\kappa=0\}}\rho^2|\nabla\kappa|dS
\]
is spread among an increasing number of patches so that no patch retains a fixed \(j_*>0\), one cannot select a single uniform patch by fiat.

That possibility must be classified as a separate fragmentation/area/multiplicity geometry branch. It may be useful only if its multiplicity is representation-safe and non-reusable; arbitrary chart refinement does not create new payer mass.

## 9. Relation to M17-476

M17-476 listed `zero-tube/trace geometry loss` as a residual noncompact exit. M17-480 sharpens it:

- within a bounded tube/reach/finite-jet/amplitude/area family, zero-level flux persistence is automatic;
- failure is therefore already one of the named geometric, finite-jet, amplitude, critical-level, fragmentation, or interface exits.

This removes one more vague branch label from the compact common-mode frontier.

## 10. Next target

The remaining local zero-level escape with no single patch floor is **fragmentation**: the total \(J_0\) may be distributed among many smaller regular patches. The next audit should determine whether such patch multiplicity can become a genuine non-reusable resource or whether bounded-overlap/coarea ownership makes it another partition artifact analogous to M17-439 and M17-381.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
