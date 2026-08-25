# DSD Critical-Memory Formal No-Resonance Audit — 2026-08-26

Status: **ANTI-PROOF / FAR-TAIL REPLENISHMENT CANNOT BE ROUTED TO H/T FROM ASYMPTOTICS ALONE / GLOBAL REGULARITY UNPROVED.**

## 1. Target under audit

The proposed endgame was to prove schematically

\[
\text{persistent }1/r\text{ critical memory}
\Longrightarrow
\text{finite-radius replenishment}
\Longrightarrow H\lor T.
\]

The first implication is geometrically natural in first-hitting coordinates, but the second must not be assumed. This note checks the far-field Leray expansion directly.

## 2. Projected Leray equation

Write the pressure-free Leray equation as

\[
L_0U
:=
\partial_sU+\frac12U+\frac12Y\cdot\nabla U
=
\nu\Delta U-\mathbb P\nabla\cdot(U\otimes U).
\]

Let

\[
r=|Y|,\qquad \rho=\log r,\qquad \eta=\rho-\frac s2.
\]

For an odd inverse-power term

\[
U_{2n+1}(Y,s)
=
r^{-(2n+1)}F_{2n+1}(\eta,\theta),
\qquad n\ge0,
\]

a direct calculation gives

\[
\partial_sU_{2n+1}
=-\frac12r^{-(2n+1)}\partial_\eta F_{2n+1},
\]

and

\[
r\partial_rU_{2n+1}
=r^{-(2n+1)}
\left[-(2n+1)F_{2n+1}+\partial_\eta F_{2n+1}\right].
\]

Hence the \(\partial_\eta\) terms cancel and

\[
\boxed{
L_0U_{2n+1}
=-n\,r^{-(2n+1)}F_{2n+1}.
}
\]

## 3. The only linear resonance is the critical 1/r mode

For \(n=0\),

\[
L_0(r^{-1}F_1(\eta,\theta))=0.
\]

Thus the critical conveyor is exactly the kernel of the linear dilation operator.

For every \(n\ge1\),

\[
L_0:r^{-(2n+1)}F\mapsto -n r^{-(2n+1)}F
\]

is algebraically invertible.

Therefore the next correction levels \(r^{-3},r^{-5},\ldots\) contain no further linear resonance.

## 4. Nonlinear and viscous orders

If

\[
U_1=r^{-1}F_1(\eta,\theta),
\]

then

\[
\Delta U_1=O(r^{-3}),
\qquad
\mathbb P\nabla\cdot(U_1\otimes U_1)=O(r^{-3}).
\]

Thus the complete leading Navier--Stokes residual has the form

\[
\mathcal R_3
=r^{-3}G_3(\eta,\theta).
\]

Because

\[
L_0(r^{-3}F_3)=-r^{-3}F_3,
\]

one may formally choose

\[
\boxed{F_3=-G_3}
\]

(up to the divergence-free/projected formulation) to absorb the entire order-\(r^{-3}\) residual.

At higher orders, viscosity raises inverse power by two and the quadratic term maps odd inverse powers to odd inverse powers. The coefficient of \(L_0\) at order \(r^{-(2n+1)}\) is \(-n\neq0\). Therefore the formal recursion continues without a far-field resonance obstruction.

## 5. Periodic/DSS compatibility

If the leading profile is periodic in the conveyor coordinate,

\[
F_1(\eta+S/2,\theta)=F_1(\eta,\theta),
\]

then all differential/quadratic forcing terms generated from it are periodic with the same period. Division by the nonzero scalar \(n\) preserves this periodicity at every higher formal order.

Thus a long-period DSS critical tail is formally compatible with an asymptotic expansion

\[
\boxed{
U
\sim
r^{-1}F_1(\eta,\theta)
+r^{-3}F_3(\eta,\theta)
+r^{-5}F_5(\eta,\theta)+\cdots.
}
\]

This is a formal asymptotic statement, not an existence theorem for an exact Navier--Stokes solution.

## 6. Consequence for the replenishment strategy

The far field does not generate a compatibility condition that forces the leading \(1/r\) coefficient to vanish or forces a derivative/turnover event. The nonlinear and viscous residuals appear two inverse powers lower and can be absorbed by nonresonant corrections.

Hence

\[
\boxed{
\text{far critical memory}
\not\Longrightarrow
H\lor T
\quad\text{from asymptotic order counting alone}.
}
\]

The critical-memory replenishment gate can at most reduce the problem to a finite-radius interface/core action. That interface action is precisely where the genuinely recurrent Leray dynamics lives, and it cannot be declared H/T without an additional coercive core rigidity theorem.

## 7. Updated interpretation

The last obstruction is therefore not a defect of the remote asymptotic expansion. The remote tail is a center direction of the Leray dilation operator, while all higher inverse-power corrections are stable/invertible directions.

The unresolved mathematical target is

\[
\boxed{
\text{nonzero compact recurrent core}
+\text{ critical center-mode memory}
\Longrightarrow
\text{contradiction or typed coercive action}.
}
\]

This applies both to the long-period DSS branch and to the aperiodic minimal recurrent branch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
