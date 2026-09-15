# M19-292 — A common production marker cancels all internal energy exchange and reduces closed-core hysteresis to a dissipation surplus

**Date:** 2026-09-16  
**Status:** CALCULATION / GAUGE-INVARIANT CLOSED-CORE CONDITIONAL BALANCE / INTERNAL-EXCHANGE ELIMINATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-291 gives a gauge-invariant production-conditioned material-energy identity for one population. M19-286 shows that pressure/viscous exchanges across shared population interfaces are antisymmetric.

The key question is whether event conditioning destroys that cancellation. If the **same global production marker** multiplies every population equation, it does not.

## 2. Finite material energy network

Let the retained active core be partitioned into finitely many material populations \(P_i\), with

\[
E_i=\int_{P_i}\frac{|U|^2}{2}\,dy,
\qquad
D_i=\int_{P_i}|\nabla U|^2dy.
\]

Their exact material energy equations are

\[
\boxed{
E_i'
=
\frac12E_i
-\nu D_i
+\sum_{j\ne i}Q_{ij}
+Q_{i,ext},
}
\]

with

\[
Q_{ij}=-Q_{ji}.
\]

Define

\[
E_{core}:=\sum_iE_i,
\qquad
D_{core}:=\sum_iD_i,
\qquad
Q_{ext}:=\sum_iQ_{i,ext}.
\]

## 3. Common lagged production marker

Use the same bounded production marker for every population:

\[
\boxed{
m_h(Y)=m_{pd}(\sigma_{-h}Y).}
\]

Multiply each population equation by \(m_h\), take invariant means, and sum.

For each population,

\[
\langle m_hE_i'\rangle
=-\langle m_h'E_i\rangle.
\]

Hence

\[
-\langle m_h'E_{core}\rangle
=
\frac12\langle m_hE_{core}\rangle
-\nu\langle m_hD_{core}\rangle
+\left\langle
m_h\sum_i\sum_{j\ne i}Q_{ij}
\right\rangle
+\langle m_hQ_{ext}\rangle.
\]

## 4. Exact conditional cancellation of internal exchange

Because the same scalar marker \(m_h\) multiplies every edge current and

\[
Q_{ij}+Q_{ji}=0
\]

pointwise,

\[
\boxed{
m_hQ_{ij}+m_hQ_{ji}=0.}
\]

Therefore

\[
\boxed{
\left\langle
m_h\sum_i\sum_{j\ne i}Q_{ij}
\right\rangle=0.
}
\]

Event conditioning by a common production marker does **not** create a net internal pressure/viscous energy source.

## 5. Exact closed-core conditional identity

The network balance becomes

\[
\boxed{
-\langle m_h'E_{core}\rangle
=
\frac12\langle m_hE_{core}\rangle
-\nu\langle m_hD_{core}\rangle
+\langle m_hQ_{ext}\rangle.
}
\]

Equivalently, define the gauge-invariant production--core-energy circulation

\[
\boxed{
C_{P\to E}^{core}
:=
\langle m_h'E_{core}\rangle.
}
\]

Then

\[
\boxed{
C_{P\to E}^{core}
=
\nu\langle m_hD_{core}\rangle
-\frac12\langle m_hE_{core}\rangle
-\langle m_hQ_{ext}\rangle.
}
\]

## 6. Closed retained core

On a branch with no external/background material-energy exchange,

\[
\boxed{Q_{ext}=0,}
\]

and therefore

\[
\boxed{
C_{P\to E}^{core}
=
\nu\langle m_hD_{core}\rangle
-\frac12\langle m_hE_{core}\rangle.
}
\]

Thus the entire production-conditioned energy hysteresis is exactly the conditioned **kinetic-dissipation surplus over the similarity baseline**.

No pressure gauge, internal lineage exchange, graph cycle, or partial-sphere flux remains.

## 7. Open-core alternative

If

\[
Q_{ext}\ne0,
\]

the correct explicit branch is

\[
\boxed{G_{external/background\ energy\ exchange}.}
\]

This includes failure of the chosen finite active core to be energetically closed under the material representation. It must not be hidden inside internal population circulation.

## 8. One-dimensional slaving consequence

If the later closed-core energy is a single-valued function of the production scalar,

\[
E_{core}(\sigma_hY)=F(\mathscr P_A(Y)),
\]

then as in M19-291,

\[
C_{P\to E}^{core}=0.
\]

On the closed branch this forces

\[
\boxed{
\nu\langle m_hD_{core}\rangle
=
\frac12\langle m_hE_{core}\rangle.
}
\]

Thus any nonzero production--core-energy hysteresis is equivalently a nonzero conditioned dissipation surplus.

## 9. Why this is not yet a contradiction

The difference

\[
\nu D_{core}-\frac12E_{core}
\]

has no fixed sign statewise. A recurrent flow can alternate between phases of above-baseline and below-baseline dissipation while keeping energy bounded.

Therefore

\[
\boxed{
C_{P\to E}^{core}\ne0
\not\Rightarrow
\text{finite exhaustion or monotone decay/growth}.
}
\]

The result is a strong reduction, not closure.

## 10. Dynamic-core frontier after M19-292

On the gauge-invariant closed-core branch, the fixed-lag production/energy problem has collapsed to

\[
\boxed{
\text{production-conditioned dissipation surplus}
\nu D_{core}-\frac12E_{core}.
}
\]

Thus the remaining theorem-level question is no longer whether pressure or internal population exchange can carry the lag event. They cannot contribute to the **net closed-core conditioned balance**.

The active alternatives are now:

\[
\boxed{
\mathcal T_{cond}^{diss-surplus}
\lor
G_{external/background\ energy\ exchange}
\lor
G_{core\ material/partition\ representation}.
}
\]

## 11. Next target

Compare the conditioned kinetic-dissipation surplus with the M5-589 vorticity production surplus

\[
\int_{\mathcal A_*}
\left(W\cdot\Sigma W-|\nabla W|^2\right)dy>0.
\]

The two dissipation notions live at different derivative levels and regions. The next audit must determine whether the production event forces a fixed sign or quantitative lower bound for

\[
\nu D_{core}-\frac12E_{core}
\]

at the fixed lag, or whether an explicit counter-configuration/recurrent phase separation shows that no such sign transfer follows.

---

\[
\boxed{\text{M19-292 COMPLETE; COMMON EVENT CONDITIONING REMOVES ALL INTERNAL ENERGY EXCHANGE AND LEAVES ONLY DISSIPATION SURPLUS OR EXTERNAL/BACKGROUND EXCHANGE.}}
\]
