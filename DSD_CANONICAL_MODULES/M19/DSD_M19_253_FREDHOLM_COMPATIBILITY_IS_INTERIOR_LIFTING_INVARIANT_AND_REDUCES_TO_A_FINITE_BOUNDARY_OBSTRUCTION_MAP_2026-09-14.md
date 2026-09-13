# M19-253 — Fredholm compatibility is interior-lifting invariant and reduces to a finite boundary obstruction map

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / FREDHOLM-QUOTIENT REDUCTION + LIFTING-INVARIANCE NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-230 reduced finite-spectator physical adjoint extension to

\[
\boxed{(I-\mathcal M_R^{ad})z_0=h_R,}
\]

with compact \(\mathcal M_R^{ad}\) and Fredholm index zero. M19-231--252 then analyzed possible primal cavity unit multipliers in detail.

However, the original Fredholm requirement is **not** that every cavity unit multiplier be absent. It is only

\[
\boxed{
\langle h_R,\varphi\rangle=0
\quad
\forall\varphi\in\ker(I-(\mathcal M_R^{ad})^*).
}
\]

This module returns to that narrower condition. It proves two facts:

1. changing the interior lifting while keeping the same physical boundary datum cannot tune the obstruction pairing;
2. on the retained finite hard boundary-data space, exact physical adjoint realization is equivalent to the kernel of a finite-dimensional boundary obstruction map.

## 2. Relative-periodic evolution notation

Work after the M19-230 time reversal. Let

\[
\partial_\tau Z=A_R(\tau)Z+f_L(\tau),
\qquad
Z|_{\partial B_R}=0,
\]

where \(L\) is a chosen smooth lifting of the prescribed physical adjoint boundary trace and

\[
f_L=-(\partial_\tau-A_R)L.
\]

Let \(U_R(\tau,\sigma)\) be the homogeneous zero-boundary propagator. Let \(Q_R\) denote the closing spatial holonomy/rotation used to compare the endpoint with the initial relative-periodic state. Define

\[
\boxed{
M_R:=Q_R^{-1}U_R(S,0).
}
\]

This is the relative zero-boundary monodromy; it is the operator denoted \(\mathcal M_R^{ad}\) in M19-230.

The Duhamel term is

\[
b_L:=\int_0^S U_R(S,\tau)f_L(\tau)d\tau.
\]

The physical field is

\[
Y=L+Z,
\]

and relative closure requires

\[
Y(S)=Q_RY(0).
\]

Substituting

\[
Z(S)=U_R(S,0)z_0+b_L
\]

gives

\[
\boxed{
(I-M_R)z_0=h_L,
}
\]

where

\[
\boxed{
h_L:=Q_R^{-1}b_L-L(0)+Q_R^{-1}L(S).}
\]

Thus the affine forcing contains both the interior Duhamel defect and the endpoint mismatch of the chosen lifting.

## 3. Change of lifting with the same physical boundary trace

Let \(\widetilde L\) be a second smooth lifting of the **same** physical boundary trace. Then

\[
q:=\widetilde L-L
\]

has homogeneous boundary data:

\[
q|_{\partial B_R}=0.
\]

The new forcing is

\[
f_{\widetilde L}
=f_L-(\partial_\tau-A_R)q.
\]

By variation of constants,

\[
\begin{aligned}
b_{\widetilde L}-b_L
&=-\int_0^S U_R(S,\tau)(\partial_\tau-A_R)q(\tau)d\tau\\
&=-q(S)+U_R(S,0)q(0).
\end{aligned}
\]

Therefore

\[
\begin{aligned}
h_{\widetilde L}-h_L
={}&Q_R^{-1}\big[-q(S)+U_R(S,0)q(0)\big]\\
&-q(0)+Q_R^{-1}q(S)\\
={}&M_Rq(0)-q(0).
\end{aligned}
\]

Hence

\[
\boxed{
 h_{\widetilde L}-h_L
=-(I-M_R)q(0).
}
\]

This is an exact affine coboundary identity. No relative-periodicity assumption on the auxiliary interior lifting \(q\) is needed; its endpoint term cancels algebraically.

## 4. Fredholm obstruction pairing is lifting invariant

Let

\[
\varphi\in\ker(I-M_R^*).
\]

Then

\[
\begin{aligned}
\langle h_{\widetilde L}-h_L,\varphi\rangle
&=-\langle(I-M_R)q(0),\varphi\rangle\\
&=-\langle q(0),(I-M_R^*)\varphi\rangle\\
&=0.
\end{aligned}
\]

Thus

\[
\boxed{
\langle h_{\widetilde L},\varphi\rangle
=
\langle h_L,\varphi\rangle
\quad
\forall\varphi\in\ker(I-M_R^*).
}
\]

Therefore the Fredholm obstruction is a property of the **physical boundary datum**, not of its arbitrary interior extension.

Permanent NO-GO:

\[
\boxed{
\text{choose a cleverer interior lifting}
\neq
\text{repair a failing Fredholm compatibility}.}
\]

Interior lifting changes only the representative of \(h_L\) modulo \(\operatorname{Ran}(I-M_R)\).

## 5. Quotient-space formulation

The exact invariant is the class

\[
\boxed{
[h_R]
\in
H_R/\operatorname{Ran}(I-M_R),
}
\]

where \(H_R=L^2_\sigma(B_R)\) or the certified zero-boundary state space used in M19-230.

Because \(I-M_R\) is Fredholm with closed range,

\[
H_R/\operatorname{Ran}(I-M_R)
\cong
\ker(I-M_R^*)^*.
\]

The obstruction coordinates are exactly

\[
\varphi\mapsto\langle h_R,\varphi\rangle.
\]

Thus the M19-230 interior problem is canonically a finite-dimensional quotient problem.

## 6. Retained hard boundary-data space

Let \(\mathscr C_R^{hard}\) denote the finite-dimensional retained physical adjoint boundary-data space transported to the spectator sphere from the hard critical dual labels by M19-227--228.

For each

\[
C\in\mathscr C_R^{hard},
\]

choose any smooth lifting \(L_C\) of its physical boundary trace and form the affine defect \(h_R(C)\). By the lifting-invariance result, the projection of \(h_R(C)\) onto the Fredholm obstruction space is independent of the chosen lifting.

Define

\[
K_R:=\ker(I-M_R^*).
\]

Let \(\Pi_{K_R}\) be the orthogonal projection onto \(K_R\). The exact boundary obstruction map is

\[
\boxed{
\mathcal O_R:
\mathscr C_R^{hard}\to K_R,
\qquad
\mathcal O_R C:=\Pi_{K_R}h_R(C).
}
\]

Equivalently, its coordinates are

\[
\boxed{
\langle\mathcal O_RC,\varphi\rangle
=
\langle h_R(C),\varphi\rangle,
\qquad
\varphi\in K_R.
}
\]

Then exact physical relative-periodic adjoint extension is equivalent to

\[
\boxed{
C\text{ is physically extendible}
\iff
\mathcal O_RC=0.
}
\]

Hence the extendible hard boundary data are precisely

\[
\boxed{\ker\mathcal O_R.}
\]

## 7. The actual target is not kernel-freeness

Let \(B\neq0\) be the primal hard scattering datum that we wish to detect by the critical Green pairing. Define

\[
\ell_B(C):=\operatorname{Re}\langle B,C\rangle_{hard}
\]

(or the corresponding complex linear/Hermitian functional before taking real part).

The M19-225/228 contradiction mechanism needs **one** physical adjoint datum \(C\) such that

\[
\boxed{
\mathcal O_RC=0,
\qquad
\ell_B(C)\neq0.
}
\]

It does not require

\[
K_R=\{0\}.
\]

Finite-dimensional linear algebra gives

\[
(\ker\mathcal O_R)^\perp
=
\operatorname{Ran}\mathcal O_R^*.
\]

Therefore

\[
\boxed{
\exists C\in\ker\mathcal O_R
\text{ with }\ell_B(C)\neq0
\iff
\ell_B\notin\operatorname{Ran}\mathcal O_R^*.
}
\]

After the hard inner-product identification of the dual space, this may be written schematically as

\[
\boxed{
B\notin\operatorname{Ran}\mathcal O_R^*.
}
\]

This is strictly weaker than excluding every cavity unit multiplier.

## 8. Correction-space version

Choose a reference critical dual datum \(C_0\) with

\[
\ell_B(C_0)\neq0.
\]

To preserve its nonzero pairing while repairing compatibility, restrict corrections to

\[
\ker\ell_B.
\]

We seek

\[
C=C_0+c,
\qquad
c\in\ker\ell_B,
\]

with

\[
\mathcal O_R(C_0+c)=0.
\]

This is solvable exactly when

\[
\boxed{
-\mathcal O_RC_0
\in
\mathcal O_R(\ker\ell_B).
}
\]

Thus boundary-data freedom may repair compatibility, but **interior-lifting freedom cannot**. These are different operations and must not be conflated.

## 9. Approximate orthogonality is not Fredholm solvability

Suppose along \(R_j\to\infty\) normalized obstruction vectors

\[
\varphi_j\in K_{R_j}
\]

decompactify and, after a common identification, satisfy

\[
\varphi_j\rightharpoonup0.
\]

If simultaneously the affine data \(h_{R_j}(C)\) were strongly precompact, then one could obtain

\[
\langle h_{R_j}(C),\varphi_j\rangle\to0.
\]

But Fredholm solvability at each finite \(R_j\) requires

\[
\boxed{
\langle h_{R_j}(C),\varphi_j\rangle=0
}
\]

**exactly**, not merely asymptotically.

Moreover, strong precompactness of \(h_{R_j}(C)\) under an \(R\)-independent identification has not been established; the physical finite-spectator trace itself moves with \(R\).

Permanent firewall:

\[
\boxed{o(1)\text{ cavity obstruction}\neq0\text{ Fredholm obstruction}.}
\]

Therefore M19-231--252 decompactification alone cannot close the affine adjoint extension.

## 10. New exact theorem target

The bounded-period Fredholm problem is now sharpened from

\[
\text{exclude every cavity unit mode}
\]

to the weaker and more exact statement

\[
\boxed{
\mathcal T_{obs}^{row}:
\text{for the target hard datum }B,
\quad
\ell_B\notin\operatorname{Ran}\mathcal O_R^*
\text{ for at least one sufficiently remote spectator }R.
}
\]

Equivalently, prove that the cavity obstruction row space does not contain the target hard Green functional.

The existing cavity kernel analysis remains useful because it constrains the possible generators of \(\operatorname{Ran}\mathcal O_R^*\), but complete kernel nonexistence is no longer logically necessary.

## 11. Next target

The next calculation should identify \(\mathcal O_R^*\) by the exact Green boundary concomitant. The expected structure is that

\[
\mathcal O_R^*\varphi
\]

is precisely the finite-spectator hard boundary/scattering trace exported by a primal zero-boundary cavity unit mode \(\varphi\).

If this identification is exact, then the obstruction-row condition becomes a physical statement:

\[
\boxed{
B\in\operatorname{Ran}\mathcal O_R^*
\iff
\text{some combination of cavity unit modes exports the same hard critical boundary functional as }B.
}
\]

That would reconnect the Fredholm compatibility problem directly to the M19-231 core/escape dichotomy, but at the boundary-trace level rather than by demanding that all cavity kernels vanish.

## 12. Scope firewalls

\[
\boxed{
\text{interior lifting freedom}
\neq
\text{physical boundary-data freedom},
}
\[
\boxed{
\text{cavity kernel exists}
\neq
\text{target hard datum is Fredholm-obstructed},
}
\[
\boxed{
\text{asymptotically small obstruction}
\neq
\text{exact finite-R compatibility}.
}

Global regularity remains unproved.
