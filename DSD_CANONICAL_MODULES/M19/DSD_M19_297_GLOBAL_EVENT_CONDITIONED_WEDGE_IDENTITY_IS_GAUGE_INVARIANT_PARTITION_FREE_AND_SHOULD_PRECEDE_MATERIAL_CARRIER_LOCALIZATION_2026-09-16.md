# M19-297 — The global event-conditioned wedge identity is gauge invariant, partition free, and should precede material-carrier localization

**Date:** 2026-09-16  
**Status:** CANONICAL STRATEGY CORRECTION / GLOBAL CONDITIONAL WEDGE BALANCE / PARTITION-FREE DYNAMIC CORE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-283--296 explored localization of the M19-269 energy-current event to material populations. That work identified useful conditional energy laws, but also introduced two extra gates:

- pressure-gauge coherence for partial pressure-containing sphere fluxes (M19-290);
- realization of flux-population labels as material spatial cutoffs/partitions (M19-296).

Neither gate is needed for the **global whole-sphere wedge observable**, which was gauge invariant from the start.

This module restores the correct canonical order: first analyze the global event-conditioned wedge identity; localize to material carriers only if a later argument genuinely needs it.

## 2. Global gauge-invariant wedge variables

At fixed depth \(z\), define

\[
e(z,Y)
:=
\int_{S^2}E_Y(z,\omega)d\omega,
\]

\[
j(z,Y)
:=
\int_{S^2}\mathcal J_{r,Y}(z,\omega)d\omega,
\]

and

\[
d(z,Y)
:=
\int_{S^2}\mathcal D_{F,Y}(z,\omega)d\omega\ge0.
\]

Because the sphere is closed and

\[
\int_{S_R}U\cdot n\,dS=0,
\]

the additive pressure gauge cancels in \(j\). Hence \(e,j,d\) and the global radial-current derivative are canonical whole-sphere observables.

## 3. State-level wedge identity

M19-282 gives

\[
\boxed{
2\sqrt z\,\Gamma(z,Y)
=
\mathcal L_qj(z,Y)
+d(z,Y)
-\partial_ze(z,Y),
}
\]

where

\[
\Gamma(z,Y)
:=
\partial_z\bigl(\sqrt z\,j(z,Y)\bigr).
\]

At the M19-269 energy-extremizing depth \(z_E\),

\[
\Gamma_E(Y):=\Gamma(z_E,Y).
\]

## 4. Production-conditioned global identity

Let

\[
m_h(Y)=m_{pd}(\sigma_{-h}Y)
\]

be the smooth lagged M5-589 production marker.

Multiply the global state-level identity by \(m_h\), take invariant means, and integrate the q-generator by parts:

\[
\langle m_h\mathcal L_qj\rangle
=-\langle(\mathcal L_qm_h)j\rangle.
\]

Therefore

\[
\boxed{
2\sqrt{z_E}\,
\langle m_h\Gamma_E\rangle
=
\langle m_hd(z_E)\rangle
-
\partial_z\langle m_he(z)\rangle\big|_{z_E}
-
\langle(\mathcal L_qm_h)j(z_E)\rangle.
}
\]

No population partition, material cutoff, interface current, or pressure gauge appears.

## 5. Exact three-channel global split

The positive fixed-lag production/energy correlation is paid by exactly three global channels:

### D — conditioned wedge dissipation

\[
\boxed{
D_{cond}
:=
\langle m_hd(z_E)\rangle
\ge0.
}
\]

### Z — conditioned depth redistribution

\[
\boxed{
Z_{cond}
:=
-\partial_z\langle m_he(z)\rangle\big|_{z_E}.
}
\]

The unconditioned derivative vanishes at \(z_E\), but the conditioned derivative need not.

### B — production-event boundary current

\[
\boxed{
B_{event}
:=
-\langle(\mathcal L_qm_h)j(z_E)\rangle.
}
\]

M19-288 resolves \(\mathcal L_qm_h\) into explicit strain-square, pressure-Hessian, viscous-derivative, and annular-transport channels. M19-289 identifies \(B_{event}\) as production--energy-current hysteresis/circulation.

Thus

\[
\boxed{
2\sqrt{z_E}\langle m_h\Gamma_E\rangle
=
D_{cond}+Z_{cond}+B_{event}.
}
\]

## 6. Canonical advantage over partial carrier localization

The global identity is:

- pressure-gauge invariant;
- representation safe on the existing compact hull;
- independent of whether finite lineage labels form a spatial partition;
- directly tied to the original M19-269 observable;
- compatible with the transparent observation-sphere interpretation.

Therefore it should be the primary dynamic-core balance.

Material-carrier localization remains useful only as a secondary refinement if one needs to ask which lineage pays one of the three global channels.

## 7. Scope of M19-283--296 after this correction

Those modules remain valid in their stated conditional scopes:

- M19-284/M19-291/M19-293: one realized material cutoff;
- M19-286/M19-292/M19-295: compatible finite material partition;
- M19-283/M19-287--289 partial-current versions: additionally one coherent fixed pressure gauge, as corrected by M19-290.

They should not replace the global partition-free identity as the canonical first step.

## 8. Dynamic-core frontier

The primary dynamic branch is now

\[
\boxed{
\mathcal T_{tail}^{lag-defect/global}:
D_{cond}+Z_{cond}+B_{event}
\text{ must pay the positive production-conditioned wedge event.}
}
\]

The three routes have distinct status:

- \(D_{cond}\): unsigned and subject to the M5-598 physical-accumulation firewall;
- \(B_{event}\): signed but recurrent hysteresis/circulation by M19-289 unless an extra rigidity theorem collapses it;
- \(Z_{cond}\): a signed production-conditioned depth redistribution and currently the least reduced global channel.

Therefore the highest-value next calculation is the conditioned depth term

\[
\boxed{
Z_{cond}
=-\partial_z\langle m_he(z)\rangle|_{z_E}.
}
\]

## 9. Next target

Study the full conditioned depth profile

\[
\mathscr E_m(z)
:=
\langle m_he(z)\rangle
\ge0
\]

with endpoint behavior inherited from the wedge:

\[
\mathscr E_m(\infty)=0,
\]

and terminal value at \(z=0\) determined by the critical scattering energy.

Determine whether recurrent production conditioning forces a forbidden monotone depth profile, or whether \(Z_{cond}\) is another reversible redistribution channel.

---

\[
\boxed{\text{M19-297 COMPLETE; THE PRIMARY FIXED-LAG DYNAMIC BALANCE IS A GLOBAL GAUGE-INVARIANT THREE-CHANNEL IDENTITY, WITH MATERIAL NETWORKS RETAINED ONLY AS CONDITIONAL REFINEMENTS.}}
\]
