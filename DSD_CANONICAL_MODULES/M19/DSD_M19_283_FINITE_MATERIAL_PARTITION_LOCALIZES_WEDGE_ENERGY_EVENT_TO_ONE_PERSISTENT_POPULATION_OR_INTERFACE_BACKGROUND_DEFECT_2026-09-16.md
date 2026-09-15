# M19-283 — A finite material partition localizes the wedge-energy event to one persistent population or an interface/background defect

**Date:** 2026-09-16  
**Status:** CALCULATION / CARRIER LOCALIZATION / CONDITIONAL MATERIAL-PARTITION BRIDGE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-282 shows that the positive invariant mean of the M19-269/M19-270 wedge-energy observable is paid by ordinary wedge dissipation after the q-coboundary and depth-derivative means vanish.

The remaining mismatch is geometric:

- M5-590 gives one fixed production-paying persistent material lineage;
- the energy observable \(\Gamma_E\) is a whole-sphere quantity at fixed wedge depth.

This module derives the exact localization formula for a finite material-population partition. It does **not** assume that such a partition is automatically available with all desired regularity; failure of the representation is recorded explicitly.

## 2. Finite equivariant partition

Fix a bounded wedge-depth interval containing \(z_E\). Suppose the retained active core admits a finite smooth nonnegative partition

\[
\boxed{
\eta_0+\eta_1+\cdots+\eta_N=1.
}
\]

Here:

- \(\eta_1,\ldots,\eta_N\) are subordinate to the finite persistent material populations/lineages supplied by the M18 finite-memory architecture;
- \(\eta_0\) is a residual background/interface carrier;
- the partition is equivariant under the recurrent hull translation, so its q-dependence is part of the marked state rather than an externally reset gauge.

If such a finite smooth equivariant localization cannot be constructed, record

\[
\boxed{G_{energy\text{-}carrier\ representation}.}
\]

No silent assignment of the global energy current to a lineage is allowed.

## 3. Localized wedge variables

For each component define

\[
\boxed{
e_i(z,q):=\int_{S^2}\eta_iE\,d\omega,}
\]

\[
\boxed{
j_i(z,q):=\int_{S^2}\eta_i\mathcal J_r\,d\omega,}
\]

and

\[
\boxed{
d_i(z,q):=\int_{S^2}\eta_i\mathcal D_F\,d\omega\ge0.}
\]

Also define the localized signed radial-current derivative

\[
\boxed{
\Gamma_i
:=
\left.\partial_z\bigl(\sqrt z\,j_i(z,q)\bigr)\right|_{z=z_E}.
}
\]

By the partition of unity,

\[
\sum_i e_i=e,
\qquad
\sum_i j_i=j,
\qquad
\sum_i d_i=d,
\qquad
\boxed{\sum_i\Gamma_i=\Gamma_E.}
\]

## 4. Exact localized energy identity

Start from the angularly integrated pointwise wedge equality of M19-282:

\[
\partial_ze
=
\partial_qj-2z\partial_zj-j+d.
\]

Multiplying the pointwise local-energy equality by \(\eta_i\), integrating on \(S^2\), and moving derivatives through the cutoff gives

\[
\boxed{
\partial_ze_i
=
\partial_qj_i
-2z\partial_zj_i
-j_i
+d_i
+b_i,
}
\]

where the exact localization/exchange term is

\[
\boxed{
\begin{aligned}
b_i
:=\int_{S^2}
\Big[
&(\partial_z\eta_i)(E+2z\mathcal J_r)
-(\partial_q\eta_i)\mathcal J_r\\
&-\nabla_{S^2}\eta_i\cdot\mathcal J_T
\Big]d\omega.
\end{aligned}
}
\]

Equivalently,

\[
\boxed{
2\sqrt z\,\partial_z(\sqrt z\,j_i)
=
\partial_qj_i
+d_i+b_i
-\partial_ze_i.
}
\]

At \(z=z_E\),

\[
\boxed{
2\sqrt{z_E}\,\Gamma_i
=
\partial_qj_i+d_i+b_i-\partial_ze_i.
}
\]

## 5. Exact cancellation of localization defects

Since

\[
\sum_i\eta_i=1,
\]

we have

\[
\sum_i\partial_z\eta_i
=
\sum_i\partial_q\eta_i
=
\sum_i\nabla_{S^2}\eta_i
=0.
\]

Therefore

\[
\boxed{\sum_i b_i=0.}
\]

Thus the localization terms are internal redistribution/interface terms, not a new net source.

The sum of the localized identities is exactly the global M19-282 identity.

## 6. Invariant means

Taking the invariant q/hull mean gives

\[
\langle\partial_qj_i\rangle=0,
\]

hence

\[
\boxed{
2\sqrt{z_E}\,\langle\Gamma_i\rangle
=
\langle d_i\rangle
+
\langle b_i\rangle
-
\partial_z\langle e_i\rangle\big|_{z_E}.
}
\]

Summing over \(i\), using \(\sum b_i=0\) and the mean-energy extremum

\[
\mathscr E'(z_E)=0,
\]

gives

\[
\boxed{
2\sqrt{z_E}\sum_i\langle\Gamma_i\rangle
=
\sum_i\langle d_i\rangle
=
\mathscr D(z_E)>0.
}
\]

## 7. Finite carrier selection

There are only \(N+1\) partition components. Therefore at least one fixed component \(i_E\) satisfies

\[
\boxed{
\langle\Gamma_{i_E}\rangle
\ge
\frac{\langle\Gamma_E\rangle}{N+1}
>0.
}
\]

If \(i_E\ge1\), one fixed persistent material population carries a positive mean localized energy-current derivative.

If the only positive component is \(i_E=0\), then the global signed event is paid by the residual background/interface sector, giving the explicit branch

\[
\boxed{G_{energy\text{-}background/interface}.}
\]

Thus the global energy event can no longer be silently associated with the production-paying lineage.

## 8. Positive-measure event set for the selected energy carrier

Compactness makes \(\Gamma_{i_E}\) bounded on the controlled localization branch. Since its invariant mean is positive, there exists a threshold \(\gamma_E^{loc}>0\) such that

\[
\boxed{
\mathcal E_E^{i_E}
:=
\{Y:\Gamma_{i_E}(Y)\ge\gamma_E^{loc}\}
}
\]

has positive invariant measure.

M5-590 already gives a fixed production lineage \(L_{\alpha_*}\) with positive-measure event set \(\mathcal E_{pd}^{\alpha_*}\).

Ergodic correlation therefore supplies a fixed finite lag \(h_{\alpha_*i_E}\) such that

\[
\boxed{
\mu\left(
\mathcal E_{pd}^{\alpha_*}
\cap
\sigma_{-h_{\alpha_*i_E}}
\mathcal E_E^{i_E}
\right)>0.
}
\]

The lag may differ from the original global \(h_*\), but it is one fixed finite number.

## 9. Exact carrier trichotomy

The dynamic-core lag problem is therefore reduced to

\[
\boxed{
\begin{aligned}
\mathcal T_{tail}^{lag-defect/core}
\Longrightarrow{}&
G_{same\text{-}population}^{\alpha_*=i_E}
\\
&\lor
G_{cross\text{-}population}^{\alpha_*\ne i_E}
\\
&\lor
G_{energy\text{-}background/interface}
\\
&\lor
G_{energy\text{-}carrier\ representation}.
\end{aligned}
}
\]

This is stronger than the global fixed-lag overlap because it identifies the material carrier class of the energy current.

## 10. What is and is not closed

This localization does **not** prove that the production lineage and energy-current lineage coincide.

It also does not make the selected positive mean nonreplenishable: the localized identity still contains

- nonnegative dissipation \(d_i\);
- signed internal exchange \(b_i\);
- signed depth redistribution \(-\partial_ze_i\).

The gain is that these terms are now assigned to one finite carrier or to explicit interfaces/background.

The next calculation can therefore use a genuine material energy budget without pretending that the global sphere current already belongs to the productive lineage.

## 11. Next target

On the same-population branch, derive the exact finite-lag kinetic-energy balance for the selected material population and identify the pressure-work, viscous-boundary, and bulk-dissipation remainder.

On the cross-population branch, determine whether the transfer from \(L_{\alpha_*}\) to \(L_{i_E}\) is represented by the already finite conservative population network or requires a new pressure/energy exchange graph.

On the residual branch, classify \(G_{energy\text{-}background/interface}\) against the active-core/spectator-tail separation of M19-278.

---

\[
\boxed{\text{M19-283 COMPLETE; THE GLOBAL WEDGE-ENERGY EVENT LOCALIZES TO ONE FIXED MATERIAL POPULATION OR AN EXPLICIT INTERFACE/BACKGROUND/REPRESENTATION DEFECT.}}
\]
