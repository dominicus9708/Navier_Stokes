# M19-287 — Event-conditioned fixed-lag wedge identity is paid by dissipation, interface exchange, depth redistribution, and an event-boundary current

**Date:** 2026-09-16  
**Status:** CALCULATION / FIXED-LAG CONDITIONAL CORRELATION / EVENT-BOUNDARY CURRENT IDENTIFICATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-282--286 show that every **unconditional** finite-lag energy balance reduces to ordinary dissipation, similarity/geometric terms, conservative internal exchange, or explicit external/background defects.

The remaining nontrivial input from M19-270 is not an unconditional mean; it is a positive-measure **fixed-lag correlation** between a production-linked material event and a later localized energy-current event.

This module derives the exact event-conditioned wedge identity.

## 2. Smooth production-event marker

Let

\[
m_{pd}:\mathfrak H\to[0,1]
\]

be a bounded smooth/cylinder approximation to the production-linked event set \(\mathcal E_{pd}\), chosen so that it is positive on a compact subset of the productive event and retains positive invariant mean.

For the fixed lag \(h\) correlating production and one selected energy carrier, define the shifted marker

\[
\boxed{
m_h(Y):=m_{pd}(\sigma_{-h}Y).
}
\]

Then

\[
\langle m_h\Gamma_i\rangle
=
\langle m_{pd}(Y)\Gamma_i(\sigma_hY)\rangle.
\]

On a positively correlated branch this quantity is strictly positive after choosing the marker/threshold appropriately.

If no sufficiently regular marker approximation preserves the positive correlation, record

\[
\boxed{G_{event\ marker/representation}.}
\]

## 3. Localized state-level identity

M19-283 gives for one material-population component

\[
\boxed{
2\sqrt z\,\Gamma_i
=
\mathcal L_qj_i
+d_i+b_i
-\partial_ze_i,
}
\]

where

- \(\mathcal L_q\) is the generator of q-translation on the marked recurrent hull;
- \(d_i\ge0\) is localized wedge dissipation;
- \(b_i\) is the signed localization/interface exchange term;
- \(e_i\) is localized wedge energy.

## 4. Generator integration by parts under the invariant measure

For a measure-preserving flow and sufficiently regular bounded observables,

\[
\langle\mathcal L_q(fg)\rangle=0.
\]

Hence

\[
\boxed{
\langle f\,\mathcal L_qg\rangle
=-\langle(\mathcal L_qf)g\rangle.
}
\]

Apply this with

\[
f=m_h,
\qquad
g=j_i.
\]

Then

\[
\boxed{
\langle m_h\mathcal L_qj_i\rangle
=-\langle(\mathcal L_qm_h)j_i\rangle.
}
\]

This is the precise place where event conditioning prevents the q-generator term from disappearing.

## 5. Exact event-conditioned fixed-lag identity

Multiply the M19-283 localized identity by \(m_h\), take invariant means, and use Section 4. Since the marker is a state observable independent of the wedge-depth variable,

\[
\langle m_h\partial_ze_i\rangle
=
\partial_z\langle m_he_i\rangle.
\]

Therefore at \(z=z_E\),

\[
\boxed{
\begin{aligned}
2\sqrt{z_E}\,
\langle m_h\Gamma_i\rangle
={}&
\langle m_hd_i\rangle
+\langle m_hb_i\rangle\\
&-
\partial_z\langle m_he_i\rangle\big|_{z_E}
-
\langle(\mathcal L_qm_h)j_i\rangle.
\end{aligned}
}
\]

This is the exact fixed-lag production-conditioned wedge-energy balance.

## 6. Four payer channels

A positive conditioned correlation

\[
\boxed{
\langle m_h\Gamma_i\rangle>0
}
\]

must be paid by at least one of four channels:

### D — event-conditioned dissipation

\[
\boxed{
\langle m_hd_i\rangle>0.
}
\]

This is unsigned and remains subject to M5-598 unless the conditioning produces a stronger physical multiplicity/budget theorem.

### I — material/interface exchange

\[
\boxed{
\langle m_hb_i\rangle.
}
\]

This is signed. Across a complete finite partition, however,

\[
\sum_i b_i=0
\]

pointwise, so with the same marker

\[
\boxed{
\sum_i\langle m_hb_i\rangle=0.
}
\]

It redistributes the conditioned current among populations unless an external/background/representation branch intervenes.

### Z — conditioned depth redistribution

\[
\boxed{
-\partial_z\langle m_he_i\rangle|_{z_E}.
}
\]

The global unconditioned derivative vanishes at \(z_E\), but the conditioned derivative need not. This is a genuine signed correlation with the production event, not a new conserved charge.

### B — event-boundary current

\[
\boxed{
-\langle(\mathcal L_qm_h)j_i\rangle.
}
\]

This is the new term created solely by event conditioning. It measures radial energy current correlated with entry into and exit from the production-marked region of state space.

For a sharp indicator it should be interpreted distributionally as a flux through the boundary of the event set; the smooth-marker formula is the canonical regular version.

## 7. Why the event-boundary term is not a bounded coboundary

Although \(m_h\) is bounded and

\[
\langle\mathcal L_qm_h\rangle=0,
\]

its product with the current need not have zero mean:

\[
\langle(\mathcal L_qm_h)j_i\rangle
\ne0
\]

in general.

Indeed

\[
\langle(\mathcal L_qm_h)j_i\rangle
=-\langle m_h\mathcal L_qj_i\rangle.
\]

Thus the event-boundary current is a covariance/transfer term, not an ordinary scalar state increment.

This is the first genuinely signed term in the lag audit that survives the generic M19-271 coboundary cancellation without being merely a population-internal antisymmetric edge current.

## 8. It is still not automatically a contradiction

A recurrent trajectory may cross the boundary of a positive-measure event set infinitely often. Therefore

\[
\boxed{
-\langle(\mathcal L_qm_h)j_i\rangle>0
\not\Rightarrow
\text{finite exhaustion}.
}
\]

To turn this term into closure one still needs one of:

1. a finite total-variation/crossing budget for the production marker;
2. a sign theorem linking entry/exit orientation to the energy current;
3. a finite-state transition/index structure whose directed current cannot sustain the required mean;
4. an exact PDE relation showing that the event-boundary current reduces to already finite strain/diffusion/interface currency.

## 9. Dynamic-core frontier after M19-287

The generic fixed-lag target can now be stated precisely as

\[
\boxed{
\mathcal T_{tail}^{lag-defect/core}
\Longrightarrow
D_{cond}
\lor
I_{cond}
\lor
Z_{cond}
\lor
B_{event}.
}
\]

The first is unsigned dissipation; the second is conservative internal exchange on a closed partition; the third is conditioned depth redistribution; the fourth is the event-boundary state-space current.

Therefore the highest-value new object is

\[
\boxed{
\mathcal T_{event}^{boundary/current}:
\text{classify }-\langle(\mathcal L_qm_h)j_i\rangle
\text{ and determine whether it has a finite or forbidden directed budget.}
}
\]

The conditioned depth derivative remains a parallel signed-correlation route.

## 10. Next target

Use the actual production marker from M5-589--592 rather than an abstract \(m_h\). Differentiate a smooth production functional underlying the event marker and identify the PDE terms in \(\mathcal L_qm_{pd}\).

The expected channels include strain evolution, pressure Hessian, viscous derivative transfer, projective action, and anchored strain-diffusion terms. These must be checked against the historical M5/M17 resource ledgers before any new payer is declared.

---

\[
\boxed{\text{M19-287 COMPLETE; FIXED-LAG CONDITIONING CREATES AN EXPLICIT EVENT-BOUNDARY CURRENT, WHILE ALL OTHER CHANNELS ARE DISSIPATION, INTERNAL EXCHANGE, OR DEPTH REDISTRIBUTION.}}
\]
