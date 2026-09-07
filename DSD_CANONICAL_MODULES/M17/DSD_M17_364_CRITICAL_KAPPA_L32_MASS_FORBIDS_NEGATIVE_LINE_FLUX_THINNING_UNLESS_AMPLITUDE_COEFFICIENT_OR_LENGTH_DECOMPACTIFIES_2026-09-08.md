# DSD M17-364 — Critical kappa L3/2 mass forbids negative-line flux thinning unless amplitude, coefficient, or length decompactifies

Date: 2026-09-08  
Canonical ID: **M17-364**

Status: **ACTIVE CRITICAL-NODAL FLUX-THINNING REDUCTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Critical negative coefficient mass in vortex-line coordinates

On the regular active set `rho>0`, use oriented vortex-flux coordinates

\[
\boxed{
dy=\frac{d\Phi\,ds}{\rho}.
}
\]

Let `Lambda_-` denote the negative-`kappa` line family from M17-362. Since `D_xi kappa=0`, `kappa_-` is constant along each connected regular vortex line, but the calculation below does not require pulling it outside the line integral.

The critical spatial mass is

\[
M_-^{crit}
:=
\int_{\{\kappa<0\}}
\kappa_-^{3/2}dy.
\]

In vortex coordinates,

\[
\boxed{
M_-^{crit}
=
\int_{\Lambda_-}
\int_{\Gamma_\lambda}
\frac{\kappa_-^{3/2}}{\rho}
\,ds\,d\Phi.
}
\]

M17-310 supplies a fixed lower bound on the full CE-H negative critical mass. On the present allocated branch write

\[
\boxed{M_-^{crit}\ge m_*>0.}
\]

If the M17-310 charge is not allocated to this regular line family, retain the corresponding nodal/interface/rank allocation exit.

## 2. Assume all three per-line quantities stay compact

Suppose on the negative-line family

\[
\boxed{\rho\ge a_*>0,}
\]

\[
\boxed{\kappa_-\le K_*<\infty,}
\]

and the retained fundamental line length satisfies

\[
\boxed{L_\lambda\le L_*<\infty.}
\]

Then for every label,

\[
\int_{\Gamma_\lambda}
\frac{\kappa_-^{3/2}}{\rho}ds
\le
\frac{K_*^{3/2}L_*}{a_*}.
\]

Let

\[
\Phi_-:=\int_{\Lambda_-}d\Phi.
\]

Therefore

\[
\boxed{
M_-^{crit}
\le
\frac{K_*^{3/2}L_*}{a_*}
\Phi_-.
}
\]

## 3. Quantitative lower bound on negative-line flux

Combining with

\[
M_-^{crit}\ge m_*,
\]

gives

\[
\boxed{
\Phi_-
\ge
\frac{a_*m_*}{K_*^{3/2}L_*}
>0.
}
\]

Hence the negative-line flux cannot thin to zero while amplitude, coefficient size, and fundamental line length all remain uniformly compact.

This is a direct quantitative complement to the conditional assumption used in M17-363.

## 4. Exact exits from flux thinning

If

\[
\Phi_-\to0
\]

while

\[
M_-^{crit}\ge m_*>0,
\]

then at least one of the compact bounds in Section 2 must fail.

Thus

\[
\boxed{
G_{negative\text{-}line\ flux\ thinning}
\Longrightarrow
G_{amplitude\ lower\text{-}bound\ collapse}
\lor
G_{coefficient\ magnitude\ decompactification}
\lor
G_{line\ length/tube\ geometry\ decompactification}
\lor
G_{charge\ allocation/interface\ loss}.
}
\]

The first alternative is precisely a genuine nodal/amplitude degeneration rather than a harmless measure repartition.

The second is a coefficient noncompactness branch.

The third is routed by M17-357 to flux fragmentation or tube-chart/transverse-geometry exits on coherent regular tube families.

## 5. Average per unit flux formulation

Even without uniform pointwise bounds, define the critical load per unit negative flux

\[
\mathcal A_-
:=
\frac1{\Phi_-}
\int_{\Lambda_-}\int
\frac{\kappa_-^{3/2}}{\rho}ds\,d\Phi.
\]

Then

\[
\boxed{
\mathcal A_-
=\frac{M_-^{crit}}{\Phi_-}.
}
\]

Hence fixed critical mass plus flux thinning forces

\[
\boxed{
\Phi_-\to0
\Longrightarrow
\mathcal A_-\to\infty.
}
\]

So some combination of low amplitude, large coefficient, long line residence, or loss of the regular coordinate representation must become arbitrarily strong on the surviving negative-line population.

## 6. Interaction with M17-363

M17-363 showed that if a fixed negative-line flux and bounded transversal area survive, then a fixed positive fraction of that flux must return to high amplitude.

The present module shows that the fixed negative-line flux assumption is itself automatic **provided** the critical negative mass is allocated to a regular line family with compact amplitude floor, coefficient ceiling, and fundamental length.

Therefore the only way to keep the M17-362 nodal branch genuinely low-amplitude is to abandon at least one of those compact properties.

## 7. DSD-theory role

The heuristic is to ask whether a vanishing structural measure can still carry a fixed critical descriptor. The mathematical answer is the exact vortex-coordinate Jacobian and a one-line integral estimate.

No DSD axiom is used as a PDE hypothesis.

## 8. Updated critical nodal branch

Combining M17-362--364,

\[
\boxed{
\begin{aligned}
G_{critical\ nodal\ \kappa_-}
\Longrightarrow{}&
G_{amplitude/nodal\ degeneration}\\
&\lor G_{coefficient\ magnitude\ decompactification}\\
&\lor G_{line/tube\ geometry\ decompactification}\\
&\lor G_{charge\ allocation/interface/rank/domain\ loss}\\
&\lor H_{high\text{-}amplitude\ negative\ capture}.
\end{aligned}
}
\]

Thus `negative-line flux thinning` is no longer an independent compact survivor.

## 9. Next target

The remaining genuinely nodal case is now amplitude collapse itself: fixed critical `kappa_-^{3/2}` mass carried where `rho` approaches zero. The next calculation should determine whether the vector equation

\[
\Delta W=\kappa W
\]

and compact derivative bounds force a quantitative relation between coefficient blow-up and the order of vanishing of `W`, or whether a scale-invariant nodal Schrödinger-type concentration remains possible.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
