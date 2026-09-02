# DSD M5-570 — Terminal Vorticity / Backward-Uniqueness Gate

Date: 2026-09-02

Status: **NONTRIVIAL CRITICAL TERMINAL TRACE FORCES NONTRIVIAL TERMINAL VORTICITY. CLASSICAL ZERO-FINAL-VORTICITY BACKWARD UNIQUENESS IS THEREFORE BLOCKED EXACTLY BY THIS MODE. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Terminal trace and terminal vorticity coefficient

From M5-569,

\[
u_0(x)=r^{-1}A(q,\omega),
\qquad
\omega_0(x)=r^{-2}B_A(q,\omega),
\qquad q=\log r.
\]

The profile \(B_A\) is the first-order log-spherical curl of \(A\).

The hard non-L3 survivor requires

\[
A\notin L^3(dq\,d\omega).
\]

We now ask whether the leading terminal vorticity can nevertheless vanish.

---

## 2. Zero terminal-vorticity coefficient forces zero critical velocity coefficient

Assume on the retained regular/non-H log-cylinder lane that \(A\) is bounded with enough angular/log regularity and

\[
\boxed{B_A\equiv0.}
\]

Define the exact critical leading field

\[
v(x):=r^{-1}A(\log r,\omega)
\]

on an exterior domain \(\{|x|>R_0\}\).

By construction,

\[
\nabla\cdot v=0,
\qquad
\nabla\times v=0.
\]

The exterior of a ball in \(\mathbb R^3\) is simply connected, so

\[
v=\nabla\phi
\]

for a harmonic potential

\[
\Delta\phi=0.
\]

Because \(A\) is bounded,

\[
|\nabla\phi|=|v|\lesssim r^{-1}.
\]

The exterior spherical-harmonic expansion of a harmonic function contains only

\[
r^\ell Y_{\ell m}(\omega)
\quad\text{and}\quad
r^{-\ell-1}Y_{\ell m}(\omega).
\]

The gradient bound \(O(r^{-1})\) removes every growing \(\ell\ge1\) mode. The remaining constant mode has zero gradient, while every decaying mode has gradient \(O(r^{-2})\) or faster.

Therefore

\[
\boxed{v(x)=O(r^{-2}).}
\]

But \(v\) was exactly of the form \(r^{-1}A(\log r,\omega)\). Hence its critical coefficient must vanish:

\[
\boxed{A\equiv0.}
\]

Thus

\[
\boxed{
A\neq0
\Longrightarrow
B_A\neq0.
}
\]

In particular, every non-L3 critical terminal survivor necessarily carries nonzero terminal vorticity at order \(r^{-2}\).

---

## 3. Consequence for the classical backward-uniqueness route

The classical Escauriaza-Seregin-Sverak blow-up argument uses a backward-uniqueness theorem for the vorticity after obtaining terminal vanishing of the blow-up-limit velocity/vorticity outside a sufficiently large ball.

The present critical survivor does not satisfy that terminal vanishing:

\[
\omega_0(x)
=
r^{-2}B_A(\log r,\omega),
\qquad
B_A\not\equiv0.
\]

Therefore the classical implication

\[
\omega(\cdot,0)=0\text{ outside a ball}
\Longrightarrow
\omega\equiv0\text{ backwards}
\]

cannot be invoked on the retained hard branch.

This is not a technical omission: the nonzero terminal vorticity coefficient is structurally forced by the same \(1/r\) trace that prevents global \(L^3\).

---

## 4. Known terminal-profile vanishing condition is exactly saturated

A known Type-I blow-up profile criterion for a suitable weak solution gives terminal vanishing of the associated ancient blow-up limit under a condition of the form

\[
\boxed{
r^{-15/8}
\int_{B(r)}|u(x,0)|^{9/8}dx
\to0
\qquad(r\downarrow0).
}
\]

For the critical model

\[
|u(x,0)|\sim r^{-1},
\]

one instead has

\[
\int_{B(r)}|u|^{9/8}dx
\asymp
\int_0^r \rho^{2-9/8}d\rho
\asymp r^{15/8}.
\]

Hence

\[
\boxed{
r^{-15/8}
\int_{B(r)}|u|^{9/8}dx
\asymp1,}
\]

not zero.

Thus the \(1/r\) terminal branch exactly saturates the known vanishing criterion rather than contradicting it.

This is a useful sharpness check on the DSD reduction.

---

## 5. Nontrivial-final-data backward uniqueness: near miss, not closure

Recent backward-uniqueness results for 3D Navier-Stokes allow two bounded mild solutions with the same nontrivial bounded final data to be identified backwards, under boundedness assumptions on the solution/vorticity.

This does **not** immediately close the present branch because the singular terminal trace relevant to a Type-I blow-up is not known to be a bounded whole-space final datum at the singular core.

Although the trace is bounded on every fixed exterior domain, pressure is nonlocal and a direct exterior cutoff changes the equation by forcing/residual terms. A separate localization theorem would be required before the nontrivial-final-data BU theorem could be applied.

Therefore this route is recorded as a possible future bridge, not as a proved contradiction.

---

## 6. Updated hard-core split

The terminal trace branch now satisfies

\[
\boxed{
\begin{gathered}
u_0=r^{-1}A(q,\omega),\\
A\notin L^3(dq\,d\omega),\\
\omega_0=r^{-2}B_A(q,\omega),\\
A\neq0\Rightarrow B_A\neq0.
\end{gathered}
}
\]

Hence the remaining terminal obstruction is no longer just a velocity-tail problem. It is a **nonzero recurrent terminal vorticity trace** at the exactly critical \(r^{-2}\) scale.

The next useful task is to push the invariant similarity-hull measure onto translations of \(A\) and \(B_A\), turning the infinite shell stack into a stationary log-radius process and asking whether its mean vorticity/Dirichlet density can coexist with the inherited ancient production budgets.

## Literature firewall

- L. Escauriaza, G. Seregin, V. Sverak, *L3,infinity-solutions of the Navier-Stokes equations and backward uniqueness*, Russian Math. Surveys 58 (2003).
- G. Seregin, T. Shilkin, *Liouville-type theorems for the Navier-Stokes equations*; terminal blow-up-profile criterion giving zero terminal ancient limit under a subcritical local condition.
- Z. Lei, Z. Yang, C. Yuan, *Backward Uniqueness for 3D Navier-Stokes Equations with Non-trivial Final Data and Applications* (revised 2026): bounded mild-solution final-data uniqueness; not directly applicable to the singular whole-space terminal trace here.

Status: **THE CLASSICAL BACKWARD-UNIQUENESS DOOR IS BLOCKED PRECISELY BY THE NONZERO r^-2 TERMINAL VORTICITY TRACE FORCED BY ANY NONZERO r^-1 CRITICAL VELOCITY TRACE. GLOBAL REGULARITY REMAINS UNPROVED.**