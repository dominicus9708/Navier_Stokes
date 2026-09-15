# M19-282 — The signed wedge-energy event decomposes into a q-coboundary plus dissipation minus a depth derivative

**Date:** 2026-09-16  
**Status:** CALCULATION / FINITE-LAG CORE AUDIT / POSITIVE-MEAN SIGNED-EVENT NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-270--271 isolate a bounded finite-depth observable

\[
\Gamma_E(Y)
=
\left.
\frac d{dz}
\left(
\sqrt z
\int_{S^2}\mathcal J_{r,Y}(z,\omega)d\omega
\right)
\right|_{z=z_E}
\]

with strictly positive invariant mean, and show that a pure bounded finite-lag state coboundary cannot absorb it.

Before constructing a new material transport observable, the exact M5-583 pointwise wedge energy equality should be used to identify what non-coboundary part \(\Gamma_E\) already contains.

The result is decisive: its positive invariant mean is exactly the wedge dissipation at the energy-extremizing depth. Thus the positive mean itself is not a new signed conserved resource.

## 2. Angularly integrated wedge energy equality before invariant averaging

M5-583 gives the pointwise wedge local-energy identity

\[
\partial_zE
=
(\mathfrak D-1)\mathcal J_r
+
\operatorname{div}_{S^2}\mathcal J_T
+
\mathcal D_F,
\]

with

\[
\mathfrak D=\partial_q-2z\partial_z,
\qquad
\mathcal D_F\ge0.
\]

For one hull phase/state, define

\[
e(z,q):=\int_{S^2}E\,d\omega,
\]

\[
j(z,q):=\int_{S^2}\mathcal J_r\,d\omega,
\]

and

\[
d(z,q):=\int_{S^2}\mathcal D_F\,d\omega\ge0.
\]

The angular divergence integrates to zero. Hence

\[
\boxed{
\partial_ze
=
\partial_qj
-2z\partial_zj
-j
+d.
}
\]

Equivalently,

\[
\boxed{
2z\partial_zj+j
=
\partial_qj+d-\partial_ze.
}
\]

## 3. Exact decomposition of the signed radial-flux derivative

Define at every state

\[
g(z,q):=\sqrt z\,j(z,q).
\]

Then

\[
2\sqrt z\,\partial_zg
=
2z\partial_zj+j.
\]

Therefore

\[
\boxed{
2\sqrt z\,\partial_zg
=
\partial_qj
+d
-
\partial_ze.
}
\]

In the hull notation, \(\partial_q\) is the infinitesimal generator of log-radius translation. Thus the M19-270 observable has the exact structural form

\[
\boxed{
\Gamma_E
=
\frac1{2\sqrt{z_E}}
\left(
\mathcal L_q j
+d
-
\partial_ze
\right)_{z=z_E}.
}
\]

The three channels are therefore:

1. a translation-generator coboundary term \(\mathcal L_qj\);
2. nonnegative local wedge dissipation \(d\);
3. the signed depth derivative \(-\partial_ze\).

## 4. Invariant mean

Under the invariant hull measure,

\[
\boxed{\langle\mathcal L_qj\rangle=0.}
\]

Also

\[
\langle\partial_ze\rangle
=
\frac d{dz}\mathscr E(z).
\]

M19-269 chooses \(z_E\) at an interior maximum of the mean energy profile, so

\[
\boxed{\mathscr E'(z_E)=0.}
\]

Consequently

\[
\boxed{
\langle\Gamma_E\rangle
=
\frac{\langle d(z_E)\rangle}{2\sqrt{z_E}}
=
\frac{\mathscr D(z_E)}{2\sqrt{z_E}}
>0.
}
\]

This is precisely the M19-269 positivity, now decomposed before averaging.

## 5. Consequence for M19-271

M19-271 correctly proves that a bounded finite-lag scalar coboundary cannot pay the positive mean of \(\Gamma_E\).

M19-282 identifies the unavoidable non-coboundary mean payer:

\[
\boxed{
\text{positive mean of }\Gamma_E
=
\text{positive mean wedge dissipation at }z_E.
}
\]

Therefore the abstract remainder in

\[
\Gamma_E
=
\Delta_{h_*}\mathcal O+\mathcal R
\]

can always contain an ordinary positive dissipation contribution. Merely proving \(\langle\mathcal R\rangle>0\) is not enough to obtain a new signed obstruction.

## 6. M5-598 accumulation firewall reappears

The quantity

\[
d(z_E)\ge0
\]

is an unsigned local derivative cost. Recurrent positive normalized dissipation at geometric Type-I scales can still acquire summable physical scale weights, exactly as in the M5-598 firewall.

Hence

\[
\boxed{
\langle\Gamma_E\rangle>0
\not\Rightarrow
\text{nonsummable physical dissipation or global contradiction}.
}
\]

The term \(-\partial_ze\) has zero invariant mean at \(z_E\), while the \(q\)-generator term is an exact invariant-mean coboundary. Neither supplies the missing one-way resource.

Thus the earlier label “signed energy event” must not be interpreted as a new positive-mean signed conserved charge.

## 7. What the finite-lag route must now prove

The fixed-lag overlap of M19-270 remains useful, but the target becomes sharper.

A successful theorem must extract from the **correlation with the production-linked material event** something stronger than unconditional dissipation positivity. Examples include:

1. a same-lineage/cross-lineage conditional dissipation demand that exceeds an inherited finite budget;
2. a signed pressure/interface/export remainder whose invariant conditional mean cannot recycle;
3. a nontrivial covariance between production and the depth-derivative/generator terms producing a genuine non-coboundary signed quantity;
4. an exact incompatibility between the M5-592 anchored/projective geometry and the local wedge energy current.

Without such an additional coupling,

\[
\boxed{
\mathcal T_{tail}^{lag-defect/core}
\text{ does not close merely from }\langle\Gamma_E\rangle>0.
}
\]

## 8. Next target: carrier localization

The remaining mismatch is now explicit:

- M5-590 identifies a fixed production-paying persistent material lineage;
- \(\Gamma_E\) is still defined by a whole-sphere energy-current integral.

Therefore the next calculation should localize the wedge energy identity by a finite material-population partition of unity. This will determine whether the positive dissipation/current mean belongs to

\[
\boxed{
\text{the same persistent lineage}
\lor
\text{a different persistent population}
\lor
\text{an interface/background realization defect}.
}
\]

Only after this carrier localization is it legitimate to derive a material finite-lag energy budget for the selected carrier.

---

\[
\boxed{\text{M19-282 COMPLETE; THE POSITIVE-MEAN SIGNED WEDGE EVENT IS UNCONDITIONALLY PAID BY ORDINARY WEDGE DISSIPATION, SO FINITE-LAG OVERLAP NEEDS A STRONGER CARRIER-LEVEL COUPLING.}}
\]
