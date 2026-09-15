# M19-291 — Gauge-invariant production-conditioned material energy identity

**Date:** 2026-09-16  
**Status:** CALCULATION / GAUGE-INVARIANT FIXED-LAG CORE BALANCE / CONDITIONAL ENERGY HYSTERESIS

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-290 shows that a partial pressure-containing wedge flux is not a canonical population observable unless a coherent pressure gauge is fixed. The safe carrier-level object is instead the closed material-population energy law of M19-284, whose pressure term is gauge invariant.

This module conditions that exact material energy law by the lag-shifted M5-589 production marker and derives the canonical fixed-lag correlation identity without choosing a pressure gauge.

## 2. Material energy law

Let \(\eta\) be a smooth material cutoff transported by

\[
B=U+\frac12y,
\qquad
D_B\eta=0.
\]

Define

\[
E_\eta:=\int \eta\,\frac{|U|^2}{2}\,dy.
\]

M19-284 gives

\[
\boxed{
E_\eta'
=
\frac12E_\eta
+X_P[\eta]
+X_\nu[\eta]
-\nu D_U[\eta],
}
\]

where

\[
X_P[\eta]
:=
\int PU\cdot\nabla\eta\,dy,
\]

\[
X_\nu[\eta]
:=
-\nu\int\nabla\eta\cdot\nabla e\,dy,
\qquad e=\frac12|U|^2,
\]

and

\[
D_U[\eta]
:=
\int\eta|\nabla U|^2dy\ge0.
\]

All four quantities are gauge invariant under \(P\mapsto P+C(\theta)\), because

\[
\int U\cdot\nabla\eta
=-\int\eta\nabla\cdot U=0.
\]

## 3. Lag-shifted production marker

Let

\[
\mathscr P_A(\theta)
=
\int_{\mathcal A_*}W\cdot\Sigma W\,dy
\]

be the M5-589 production functional and choose a smooth marker

\[
m_{pd}=\chi(\mathscr P_A),
\qquad 0\le m_{pd}\le1.
\]

For a fixed lag \(h\), define

\[
\boxed{
m_h(Y):=m_{pd}(\sigma_{-h}Y).}
\]

Then \(m_h\) marks present states whose past state at lag \(h\) was production-active. It is an ordinary bounded state observable on the marked recurrent hull.

## 4. Invariant integration by parts in time

Multiply the material energy law by \(m_h\) and take the invariant mean. Since

\[
\left\langle\frac d{d\theta}(m_hE_\eta)\right\rangle=0,
\]

we have

\[
\boxed{
\langle m_hE_\eta'\rangle
=-\langle m_h'E_\eta\rangle.
}
\]

Therefore

\[
\boxed{
\begin{aligned}
-\langle m_h'E_\eta\rangle
={}&
\frac12\langle m_hE_\eta\rangle
+\langle m_hX_P[\eta]\rangle\\
&+\langle m_hX_\nu[\eta]\rangle
-\nu\langle m_hD_U[\eta]\rangle.
\end{aligned}
}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
C_{P\to E}^{\eta}
:=\langle m_h'E_\eta\rangle
={}&
-\frac12\langle m_hE_\eta\rangle\\
&-\langle m_h(X_P+X_\nu)\rangle
+\nu\langle m_hD_U\rangle.
\end{aligned}
}
\]

This is the exact gauge-invariant production-conditioned material-energy identity.

## 5. Actual production-transition form

Because

\[
m_{pd}=\chi(\mathscr P_A),
\]

at the shifted production time

\[
m_h'
=
\chi'(\mathscr P_A)\,\mathscr P_A'
\]

up to the harmless sign convention induced by whether the lagged marker is written with \(\sigma_{-h}\) or the energy observable with \(\sigma_h\). Fixing the above convention gives the corresponding time derivative consistently.

Thus the signed correlation is of the form

\[
\boxed{
C_{P\to E}^{\eta}
=
\left\langle
\chi'(\mathscr P_A)\mathscr P_A'\,E_\eta(\sigma_hY)
\right\rangle
}
\]

after moving the lag by invariance.

Unlike the partial wedge current used in M19-283--289, this quantity is pressure-gauge invariant.

## 6. One-dimensional slaving firewall

If the later material energy is a single-valued function of the production scalar,

\[
E_\eta(\sigma_hY)=F(\mathscr P_A(Y)),
\]

then choose \(H' = \chi'F\). Invariance gives

\[
\boxed{
C_{P\to E}^{\eta}
=
\left\langle\frac d{d\theta}H(\mathscr P_A)\right\rangle
=0.
}
\]

Hence

\[
\boxed{
C_{P\to E}^{\eta}\ne0
\Longrightarrow
\text{genuine production--material-energy hysteresis / multidimensional recurrence}.
}
\]

This is the gauge-invariant replacement for the partial-current hysteresis statement of M19-289.

## 7. Four gauge-invariant payer channels

A nonzero production-conditioned material-energy circulation is exactly paid by:

1. **similarity baseline**
   \[
   -\frac12\langle m_hE_\eta\rangle;
   \]
2. **pressure exchange**
   \[
   -\langle m_hX_P\rangle;
   \]
3. **viscous boundary exchange**
   \[
   -\langle m_hX_\nu\rangle;
   \]
4. **bulk kinetic dissipation**
   \[
   +\nu\langle m_hD_U\rangle.
   \]

No pressure-gauge defect remains.

The baseline and bulk dissipation are unsigned after fixing \(m_h\ge0\). The pressure and viscous interface terms are signed, but require an independent sign, cancellation, or finite-budget theorem before they can close the recurrent branch.

## 8. What this does not prove

The identity is compatible with a bounded recurrent cycle. Production-active phases may be followed by phases of high dissipation or interface exchange and then return.

Therefore

\[
\boxed{
C_{P\to E}^{\eta}\ne0
\not\Rightarrow
\text{monotone energy accumulation or finite exhaustion}.
}
\]

The gain is that the fixed-lag dynamic-core problem is now written entirely in gauge-invariant material variables.

## 9. Next target

Apply the same production marker to a **complete closed finite material-population network** and sum the conditioned energy identities. Internal pressure/viscous exchanges should cancel pairwise even after conditioning by the common marker.

If so, the whole-core identity will reduce to

\[
\text{production-conditioned core-energy hysteresis}
=
\text{conditioned dissipation surplus relative to similarity baseline}
+\text{external/background exchange}.
\]

That will determine whether any internal population exchange can still serve as the M19-271 non-coboundary payer.

---

\[
\boxed{\text{M19-291 COMPLETE; THE FIXED-LAG PRODUCTION/ENERGY CORRELATION HAS A GAUGE-INVARIANT MATERIAL FORM WITH ONLY BASELINE, PRESSURE, VISCOUS, AND DISSIPATION CHANNELS.}}
\]
