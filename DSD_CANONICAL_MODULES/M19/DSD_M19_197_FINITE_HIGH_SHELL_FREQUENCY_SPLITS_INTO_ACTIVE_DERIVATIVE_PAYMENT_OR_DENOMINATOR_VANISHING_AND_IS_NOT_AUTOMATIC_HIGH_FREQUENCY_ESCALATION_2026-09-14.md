# M19-197 — Finite-high shell frequency splits into active derivative payment or denominator vanishing; it is not automatic high-frequency escalation

**Date:** 2026-09-14  
**Status:** BRANCH SPLIT / DENOMINATOR FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Shell-frequency quotient

Recall

\[
\Gamma_R(s)
=
\frac{R\|\nabla(U-m_R)\|_{L^2(A_R^*)}}
{\|U-m_R\|_{L^2(A_R^*)}}.
\]

Define the shell mass and shell derivative energy

\[
E_R:=\|U-m_R\|_{L^2(A_R^*)}^2,
\qquad
D_R:=\|\nabla(U-m_R)\|_{L^2(A_R^*)}^2.
\]

Then exactly

\[
\boxed{
D_R=\Gamma_R^2\frac{E_R}{R^2}.
}
\]

## 2. Critical normalization

For a critical \(r^{-1}\) shell, \(E_R\) has natural size \(R\). Set

\[
m_R:=\frac{E_R}{R}.
\]

Then

\[
\boxed{
D_R=\Gamma_R^2\frac{m_R}{R}.
}
\]

Thus if

\[
\Gamma_R\ge\gamma
\quad\text{and}\quad
m_R\ge m_0>0,
\]

one gets the active scale-matched derivative payer

\[
\boxed{
R D_R\ge\gamma^2m_0.
}
\]

## 3. Denominator-degeneration alternative

However, a large quotient \(\Gamma_R\) can also arise because

\[
E_R\ll R,
\qquad m_R\to0,
\]

while \(D_R\) remains small. In that case there is no order-one derivative payment despite large \(\Gamma_R\).

Therefore the correct split is

\[
\boxed{
\Gamma_R\text{-high}
\Longrightarrow
\begin{cases}
\text{active shell derivative payment},&m_R\ge m_0,\\
\text{shell-amplitude/denominator degeneration},&m_R<m_0.
\end{cases}
}
\]

## 4. Relation to the historical high-frequency branch

The historical branch \(G_{high\ remote\ frequency}\) concerns genuine derivative-frequency escalation. A finite-high value of the ratio \(\Gamma_R\) is not sufficient to enter that branch unless the shell amplitude is quantitatively retained.

Hence

\[
\boxed{
\Gamma^\sharp\text{-high}
\neq
\text{high-frequency escalation}
}
\]

without an amplitude floor.

## 5. Time persistence

Even on the active side, one high shell/time only gives a snapshot payer. A long-time contradiction still requires positive occupation or recurrence of active high-frequency shells.

On the denominator-degenerate side the issue is instead tail/shell vanishing or localization, which must be matched to existing vanishing-core / remote-localization routes rather than counted as derivative payment.

## 6. Verdict

Finite-high shell frequency is therefore a two-way diagnostic branch:

\[
\boxed{
\Gamma^\sharp\text{-high}
\Longrightarrow
\text{active derivative-frequency event}
\lor
\text{vanishing-shell denominator event}.
}
\]

Neither alternative is automatically closed by the value of the supremum alone.