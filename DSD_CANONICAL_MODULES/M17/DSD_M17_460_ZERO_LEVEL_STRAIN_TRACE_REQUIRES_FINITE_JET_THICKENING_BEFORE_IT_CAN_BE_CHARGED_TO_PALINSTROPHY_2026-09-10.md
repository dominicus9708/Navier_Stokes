# DSD M17-460 — The zero-level strain trace requires finite-jet thickening before it can be charged to bulk palinstrophy

Date: 2026-09-10  
Canonical ID: **M17-460**

Status: **ACTIVE TRACE FIREWALL / CONDITIONAL PALINSTROPHY THICKENING / M17-459 SOURCE-RETURN AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-459

M17-459 gives the absolute coefficient-moment balance

\[
\dot A+2J_0
=-2C_{0\sigma}+G_A+2S_A+2\Delta Q,
\]

where

\[
J_0
=\int\rho^2\delta(\kappa)|\nabla\kappa|^2dx
=\int_{\{\kappa=0\}}\rho^2|\nabla\kappa|dS,
\]

and

\[
C_{0\sigma}
=\int\rho^2\delta(\kappa)\nabla\kappa\cdot\nabla\sigma\,dx
=\int_{\{\kappa=0\}}\rho^2\partial_n\sigma\,dS.
\]

The present module asks whether `C_{0sigma}` is automatically a bulk palinstrophy payer.

## 2. Exact Cauchy pairing on the zero level

At a regular zero hypersurface,

\[
|C_{0\sigma}|
\le
\left(
\int_{\{\kappa=0\}}\rho^2|\nabla\kappa|dS
\right)^{1/2}
\left(
\int_{\{\kappa=0\}}
\rho^2\frac{|\nabla\sigma|^2}{|\nabla\kappa|}dS
\right)^{1/2}.
\]

Thus

\[
\boxed{
|C_{0\sigma}|
\le J_0^{1/2}J_{\sigma,0}^{1/2},
}
\]

where

\[
\boxed{
J_{\sigma,0}
:=\int\rho^2\delta(\kappa)|\nabla\sigma|^2dx
=\int_{\{\kappa=0\}}
\rho^2\frac{|\nabla\sigma|^2}{|\nabla\kappa|}dS.
}
\]

Young gives

\[
\boxed{
2|C_{0\sigma}|
\le \varepsilon J_0
+\varepsilon^{-1}J_{\sigma,0}.
}
\]

The only remaining issue is whether `J_{sigma,0}` is controlled by a bulk resource.

## 3. No-go: a codimension-one trace is not controlled by bulk `L2` alone

Regularity of the coefficient zero level does not by itself give

\[
J_{\sigma,0}
\lesssim
\int_{\{|\kappa|<\delta\}}\rho^2|\nabla\sigma|^2dx.
\]

Indeed, in one normal coordinate `s`, one may choose a smooth profile `f_epsilon(s)` with

\[
f_\varepsilon(0)=1,
\]

supported on a normal layer of thickness `epsilon`, so that

\[
\int|f_\varepsilon(s)|^2ds
\to0
\qquad(\varepsilon\to0).
\]

Tensoring this profile with a smooth tangential cutoff produces a smooth codimension-one trace of order one while the bulk `L2` mass tends to zero.

Therefore

\[
\boxed{
\text{regular zero geometry alone}
\not\Rightarrow
\text{bulk palinstrophy control of }C_{0\sigma}.
}
\]

A normal derivative / finite-jet compactness input is genuinely required.

## 4. Regular zero-tube hypotheses that do suffice

Consider a normalized regular zero tube

\[
\mathcal T_\delta
:=\{|\kappa|<\delta\}
\]

with fixed normalized thickness `delta>0`.

Assume on this tube:

1. nondegenerate coefficient gradient
\[
0<g_*\le|\nabla\kappa|\le G_*<\infty;
\]

2. normalized amplitude ceiling
\[
0\le\rho\le M_\rho;
\]

3. finite-jet trace compactness sufficient to prevent concentration of `rho nabla sigma` in a vanishing normal sublayer. One convenient sufficient form is a uniform normal `H1` control of
\[
f:=\rho\nabla\sigma/|\nabla\kappa|^{1/2}.
\]

Then the one-dimensional trace theorem along the normal foliation gives

\[
\boxed{
J_{\sigma,0}
\lesssim_{\delta,g_*,G_*}
\int_{\mathcal T_\delta}
\left(
\rho^2|\nabla\sigma|^2
+|\nabla(\rho\nabla\sigma)|^2
\right)dx.
}
\]

This is a sufficient trace-thickening estimate. The derivative term is not to be dropped unless separately controlled.

## 5. Lower-order bulk part is palinstrophy-controlled

The exact strain/vorticity singular-integral structure gives

\[
|\nabla\sigma|\le|\nabla\Sigma|
\]

pointwise in the direction derivative sense used in the late-M17 chain, while globally

\[
\|\nabla\Sigma\|_2^2
=\frac12\|\nabla\Omega\|_2^2.
\]

Under the amplitude ceiling,

\[
\int_{\mathcal T_\delta}\rho^2|\nabla\sigma|^2dx
\le
M_\rho^2\int|\nabla\sigma|^2dx
\lesssim
M_\rho^2P.
\]

Therefore the only genuinely new part of the trace estimate is the normal finite-jet term

\[
\int_{\mathcal T_\delta}|\nabla(\rho\nabla\sigma)|^2dx.
\]

This term belongs to the already explicit normalized high-jet / trace-concentration frontier rather than to ordinary palinstrophy.

## 6. Conditional absorption of the zero-level strain trace

Suppose the finite-jet term is controlled on the regular zero tube by

\[
\int_{\mathcal T_\delta}
|\nabla(\rho\nabla\sigma)|^2dx
\le C_{tr}P
\]

with a record-uniform constant.

Then

\[
J_{\sigma,0}\le C_*P.
\]

Consequently

\[
2|C_{0\sigma}|
\le
\varepsilon J_0+C_{\varepsilon,*}P.
\]

Substituting into M17-459 gives, for example with `epsilon=1`,

\[
\boxed{
\dot A+J_0
\le
C_*P
+|G_A|+2|S_A|+2|\Delta Q|.
}
\]

Thus under regular finite-jet trace compactness, the zero-level strain trace is **not an independent source-return currency**. It is absorbed by part of the zero-current plus a palinstrophy payer.

## 7. Cross-generation interpretation

If a zero-level strain-trace replenishment event persists over a positive parent-time fraction and the finite-jet trace compactness above is record-uniform, its bulk contribution returns to the favorable M17-307 ancestry resource

\[
\boxed{
\sum_mR_m^{-1}\int P_mds<\infty.
}
\]

Therefore a persistent strong `C_{0sigma}` source cannot survive through an ordinary compact regular zero tube without paying palinstrophy.

The escape is explicit:

\[
\boxed{
G_{\rm zero\text{-}trace\ concentration/high\text{-}jet\ decompactification}
}
\]

or degeneration of the regular zero-tube chart/nondegeneracy assumptions.

## 8. Updated source-return split

M17-459's source-return equation becomes

\[
\dot A+2J_0
=-2C_{0\sigma}+G_A+2S_A+2\Delta Q.
\]

For the first term:

\[
\boxed{
G_{C_{0\sigma}}
\Longrightarrow
G_{\rm palinstrophy\ payer}
\lor
G_{\rm zero\text{-}trace/high\text{-}jet\ decompactification}
\lor
G_{\rm zero\text{-}tube/chart\ loss}.
}
\]

Hence the lower-order unresolved source-return currencies are now concentrated in

1. geometry source `G_A`;
2. strain-weighted sign moment `S_A`;
3. second-moment asymmetry `Delta Q`;
4. the explicitly isolated high-jet trace escape.

## 9. DSD audit role

DSD is used only to distinguish a codimension-one trace from a bulk resource and to prevent an invalid dimension-lowering inequality. The actual argument is standard Kato/coarea calculus, one-dimensional trace theory, singular-integral strain control, and the certified M17-307 palinstrophy ledger.

## 10. Audit verdict

**PASS WITH A FIREWALL — the zero-level strain trace is conditionally reducible to palinstrophy, but not from regular zero geometry alone.**

Under record-uniform finite-jet trace compactness it can be absorbed into the zero-current plus palinstrophy. Without that extra compactness, trace concentration is a genuine normalized high-jet/interface exit and must remain OPEN.

The next module should isolate the second-moment asymmetry `Delta Q`, because M17-458 controls first-moment sign cancellation but does not control the different mean coefficient magnitudes carried by the two signs.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
