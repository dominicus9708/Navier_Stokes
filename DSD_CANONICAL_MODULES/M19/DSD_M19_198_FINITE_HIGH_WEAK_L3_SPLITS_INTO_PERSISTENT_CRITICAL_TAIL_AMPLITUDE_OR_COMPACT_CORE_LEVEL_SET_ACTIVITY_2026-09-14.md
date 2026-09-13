# M19-198 — Finite-high weak-L3 splits into persistent critical-tail amplitude or compact-core level-set activity

**Date:** 2026-09-14  
**Status:** BRANCH SPLIT / CRITICAL-TAIL PERSISTENCE AUDIT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Intrinsic weak-L3 size

Let

\[
W(s):=\|U(s)\|_{L^{3,\infty}},
\qquad
W^\sharp:=\sup_s W(s)<\infty.
\]

If \(W(s)\ge w\), then by the Lorentz-space definition there is a level \(\lambda>0\) such that, up to a universal approximation factor,

\[
\boxed{
\lambda^3\,\big|\{|U(s)|>\lambda\}\big|\gtrsim w^3.
}
\]

Thus finite-high weak-L3 always represents a scale-critical amplitude-volume event, but not necessarily a derivative payer.

## 2. Leading critical tail is time-persistent in weak-L3

On the retained scattering corridor,

\[
U_0(y,s)
=
\frac1r A\!\left(\log r-\frac s2,\omega\right).
\]

For a time shift \(t\),

\[
U_0(y,s+t)
=
e^{-t/2}U_0(e^{-t/2}y,s).
\]

The weak-\(L^3\) norm is invariant under the critical scaling \(f(y)\mapsto a f(ay)\). Therefore

\[
\boxed{
\|U_0(\cdot,s+t)\|_{L^{3,\infty}}
=
\|U_0(\cdot,s)\|_{L^{3,\infty}}.
}
\]

Hence any large weak-L3 contribution carried by the leading \(r^{-1}\) scattering tail is automatically persistent in similarity time.

## 3. Core/remainder alternative

Write schematically

\[
U=U_0+U_{rem},
\]

where the far-field remainder is subcritical (beginning with the \(r^{-3}\) correction on the certified corridor) and the remaining contribution is concentrated in the finite spectator/core region.

By the Lorentz quasi-triangle inequality, if \(W^\sharp\) is large while the leading-tail weak-L3 norm is below a fixed fraction of that size, then a comparable part of the large weak-L3 event must be carried by the compact/core remainder.

Thus

\[
\boxed{
W^\sharp\text{-high}
\Longrightarrow
\text{persistent critical-tail weak-L3 amplitude}
\lor
\text{compact-core level-set activity}.
}
\]

## 4. What is and is not paid

The tail alternative is persistent but weak-L3 amplitude itself is scale-critical and does not create a finite ancestral contradiction. It strengthens the nonzero critical-tail floor already present in the RSS/RDSS/scattering analysis.

The compact-core alternative can be converted to local amplitude-volume mass at high times, but—as in M19-196—requires an occupation lower bound before it becomes a quantitative invariant-mean payer.

## 5. Relation to weak-L3 escalation

A finite-high value of \(W^\sharp\) is not the historical unbounded weak-L3 escalation branch. Therefore

\[
\boxed{
W^\sharp\text{-high}
\neq
W(s_n)\to\infty.
}
\]

The finite-high tail alternative is better viewed as a quantitative strengthening of the retained critical scattering branch.

## 6. Verdict

Among the three M19-193 diagnostics, weak-L3 has the strongest persistence mechanism because the leading critical tail transports its weak-L3 size isometrically under log-radius translation. Nevertheless, this persistence alone does not close the branch; it supplies a persistent critical-tail amplitude floor, not a dissipative contradiction.